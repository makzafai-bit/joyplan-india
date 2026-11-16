<?php
/*
 * Lead handler for the landing pages (/demo, /masterclass, /partner) and the main site forms (enquiry, book).
 *
 * Saves every lead as a row in a CSV file, one file per form:
 *   ../joyplan-leads/leads-demo.csv   (the folder next to public_html, not web-visible)
 * Falls back to ./leads-data/ (blocked from the web by .htaccess) if that folder can't be created.
 *
 * Every lead is also e-mailed to NOTIFY_EMAIL (sales@joyplanindia.com).
 * The mail is sent with PHP mail() from MAIL_FROM, an address on joyplanindia.com,
 * so Hostinger's SPF/DKIM for the domain applies. Reply-To is the submitter's e-mail
 * when the form has one, so "Reply" in the inbox goes straight to the lead.
 * If the CSV can't be written the e-mail still goes out (and vice versa); the visitor
 * only sees an error when both fail. Mail failures are logged to mail-errors.log
 * in the leads folder.
 */
declare(strict_types=1);

const NOTIFY_EMAIL = 'sales@joyplanindia.com';  // every form's leads go here
const MAIL_FROM    = 'no-reply@joyplanindia.com';

$FORMS = [
    'demo' => [
        'tag'    => 'Demo',
        'thanks' => '/demo/thank-you/',
        'fields' => ['full_name', 'mobile', 'email', 'city', 'role', 'team_size', 'current_tools', 'demo_time', 'consent'],
        'required' => ['full_name', 'mobile', 'email', 'city', 'role', 'team_size', 'demo_time', 'consent'],
    ],
    'masterclass' => [
        'tag'    => 'Masterclass',
        'thanks' => '/masterclass/thank-you/',
        'fields' => ['full_name', 'mobile', 'email', 'city', 'profession', 'firm_name', 'years_practice', 'owns_device', 'batch', 'consent'],
        'required' => ['full_name', 'mobile', 'email', 'city', 'profession', 'owns_device', 'batch', 'consent'],
    ],
    'enquiry' => [   // main site: homepage enquiry form
        'tag'    => 'Website enquiry',
        'thanks' => '/book-a-demo/thank-you/',
        'fields' => ['full_name', 'mobile', 'profession', 'city', 'product', 'message', 'nearest_team', 'consent'],
        'required' => ['full_name', 'mobile', 'profession', 'city'],
    ],
    'book' => [      // main site: /book-a-demo/ and /contact/
        'tag'    => 'Website demo booking',
        'thanks' => '/book-a-demo/thank-you/',
        'fields' => ['interest', 'profession', 'full_name', 'mobile', 'city', 'demo_format', 'message', 'package', 'nearest_team', 'consent'],
        'required' => ['full_name', 'mobile', 'city'],
    ],
    'partner' => [
        'tag'    => 'Partner',
        'thanks' => '/partner/thank-you/',
        'fields' => ['full_name', 'company', 'business_type', 'city_state', 'territory', 'years_business', 'team_size', 'mobile', 'email', 'investment', 'message', 'consent'],
        'required' => ['full_name', 'company', 'business_type', 'city_state', 'territory', 'mobile', 'email', 'investment', 'consent'],
    ],
];
$TRACKING = ['source_page', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'fbclid'];

$wantsJson = stripos($_SERVER['HTTP_ACCEPT'] ?? '', 'application/json') !== false;

function respond(bool $ok, string $error = '', string $redirect = '', int $code = 200): void
{
    global $wantsJson;
    if ($wantsJson || !$ok) {
        http_response_code($ok ? 200 : $code);
        header('Content-Type: application/json; charset=utf-8');
        header('Cache-Control: no-store');
        echo json_encode(['ok' => $ok, 'error' => $error, 'redirect' => $redirect]);
    } else {
        header('Location: ' . $redirect, true, 303);
    }
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(false, 'Method not allowed', '', 405);
}

$type = (string)($_POST['form'] ?? '');
if (!isset($FORMS[$type])) {
    respond(false, 'Unknown form', '', 400);
}
$cfg = $FORMS[$type];

// Honeypot: bots fill the hidden "website" field. Pretend success, store nothing.
if (trim((string)($_POST['website'] ?? '')) !== '') {
    respond(true, '', $cfg['thanks']);
}

function clean($v, int $max): string
{
    if (is_array($v)) {
        $v = implode('; ', array_map('strval', $v));
    }
    $v = trim(preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', (string)$v) ?? '');
    return mb_substr($v, 0, $max);
}

$row = [];
foreach ($cfg['fields'] as $f) {
    $row[$f] = clean($_POST[$f] ?? '', $f === 'message' ? 2000 : 300);
}
foreach ($cfg['required'] as $f) {
    if ($row[$f] === '') {
        respond(false, 'Please fill in all required fields.', '', 422);
    }
}
if (isset($row['email']) && ($row['email'] !== '' || in_array('email', $cfg['required'], true)) && !filter_var($row['email'], FILTER_VALIDATE_EMAIL)) {
    respond(false, 'Please enter a valid email address.', '', 422);
}
$digits = preg_replace('/\D/', '', $row['mobile']);
if (strlen($digits) > 10 && str_starts_with($digits, '91')) $digits = substr($digits, 2);
if (strlen($digits) === 11 && $digits[0] === '0') $digits = substr($digits, 1);
if (!preg_match('/^[6-9]\d{9}$/', $digits)) {
    respond(false, 'Please enter a valid 10-digit mobile number.', '', 422);
}
$row['mobile'] = $digits;           // 10 digits, India (+91)
$row['consent'] = 'yes';

$track = [];
foreach ($TRACKING as $f) {
    $track[$f] = clean($_POST[$f] ?? '', 300);
}

$record = array_merge(
    ['submitted_at' => (new DateTime('now', new DateTimeZone('Asia/Kolkata')))->format('Y-m-d H:i:s'), 'lead_tag' => $cfg['tag']],
    $row,
    $track,
    ['ip' => $_SERVER['REMOTE_ADDR'] ?? '', 'user_agent' => clean($_SERVER['HTTP_USER_AGENT'] ?? '', 300)]
);

$LABELS = [
    'submitted_at' => 'Submitted (IST)', 'lead_tag' => 'Form', 'full_name' => 'Name', 'mobile' => 'Mobile',
    'email' => 'E-mail', 'city' => 'City', 'city_state' => 'City / state', 'role' => 'Role',
    'profession' => 'Profession', 'team_size' => 'Team size', 'current_tools' => 'Current tools',
    'demo_time' => 'Preferred demo time', 'firm_name' => 'Firm name', 'years_practice' => 'Years in practice',
    'owns_device' => 'Owns a device', 'batch' => 'Batch', 'product' => 'Product', 'message' => 'Message',
    'nearest_team' => 'Nearest team', 'interest' => 'Interested in', 'demo_format' => 'Demo format',
    'package' => 'Package', 'company' => 'Company', 'business_type' => 'Business type',
    'territory' => 'Territory', 'years_business' => 'Years in business', 'investment' => 'Investment',
    'consent' => 'Consent', 'source_page' => 'Page', 'utm_source' => 'UTM source', 'utm_medium' => 'UTM medium',
    'utm_campaign' => 'UTM campaign', 'utm_content' => 'UTM content', 'utm_term' => 'UTM term',
    'fbclid' => 'fbclid', 'ip' => 'IP', 'user_agent' => 'Browser',
];

// Pick a storage folder outside the web root if we can.
$dir = dirname(__DIR__) . '/joyplan-leads';
if (!is_dir($dir) && !@mkdir($dir, 0750, true)) {
    $dir = __DIR__ . '/leads-data';
    if (!is_dir($dir)) @mkdir($dir, 0750, true);
}
$dirOk = is_dir($dir) && is_writable($dir);
if ($dirOk && str_starts_with($dir, __DIR__) && !file_exists($dir . '/.htaccess')) {
    @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n");
}

function save_csv(string $file, array $record): bool
{
    $fh = @fopen($file, 'ab');
    if (!$fh) return false;
    flock($fh, LOCK_EX);
    clearstatcache(true, $file);
    if (filesize($file) === 0) {
        fwrite($fh, "\xEF\xBB\xBF");               // UTF-8 BOM so Excel shows ₹ and Indian names correctly
        fputcsv($fh, array_keys($record));
    }
    // Guard against spreadsheet formula injection.
    $safe = array_map(fn($v) => preg_match('/^[=+\-@\t\r]/', (string)$v) ? "'" . $v : $v, array_values($record));
    $ok = fputcsv($fh, $safe) !== false;
    fflush($fh);
    flock($fh, LOCK_UN);
    fclose($fh);
    return $ok;
}

function send_lead_mail(array $record, array $row, array $cfg, array $labels): bool
{
    if (NOTIFY_EMAIL === '' || !function_exists('mail')) return false;
    $oneLine = fn(string $v): string => trim(preg_replace('/[\r\n]+/', ' ', $v) ?? '');

    $lines = ['New lead from the ' . $cfg['tag'] . ' form on joyplanindia.com', ''];
    foreach ($record as $k => $v) {
        if ($v === '' || $k === 'lead_tag') continue;
        $lines[] = str_pad(($labels[$k] ?? $k) . ':', 22) . ($k === 'message' ? "\n" . $v . "\n" : $oneLine((string)$v));
    }
    $lines[] = '';
    $lines[] = 'Call: +91 ' . $row['mobile'];
    $lines[] = 'WhatsApp: https://wa.me/91' . $row['mobile'];
    $body = implode("\r\n", $lines);

    $where = $row['city'] ?? $row['city_state'] ?? '';
    $subject = 'New ' . $cfg['tag'] . ' lead: ' . $oneLine($row['full_name']) . ($where !== '' ? ' (' . $oneLine($where) . ')' : '');

    $headers = [
        'From: Joyplan India Website <' . MAIL_FROM . '>',
        'MIME-Version: 1.0',
        'Content-Type: text/plain; charset=UTF-8',
        'Content-Transfer-Encoding: 8bit',
        'X-Mailer: joyplanindia.com lead.php',
    ];
    $email = $row['email'] ?? '';
    if ($email !== '' && filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $name = preg_replace('/[^\p{L}\p{N} .\'-]/u', '', $row['full_name']) ?? '';
        $headers[] = 'Reply-To: ' . ($name !== '' ? '=?UTF-8?B?' . base64_encode($name) . '?= ' : '') . '<' . $email . '>';
    }

    // "-f" sets the envelope sender (Return-Path) to our own domain, which SPF checks.
    return @mail(
        NOTIFY_EMAIL,
        '=?UTF-8?B?' . base64_encode($subject) . '?=',
        $body,
        implode("\r\n", $headers),
        '-f' . MAIL_FROM
    );
}

$saved  = $dirOk && save_csv($dir . '/leads-' . $type . '.csv', $record);
$mailed = send_lead_mail($record, $row, $cfg, $LABELS);

if (!$mailed && $dirOk) {
    @file_put_contents(
        $dir . '/mail-errors.log',
        $record['submitted_at'] . "\t" . $type . "\t" . ($saved ? 'saved to CSV' : 'NOT SAVED') . "\t" . (error_get_last()['message'] ?? 'mail() returned false') . "\n",
        FILE_APPEND | LOCK_EX
    );
}
if (!$saved && !$mailed) {
    respond(false, 'Sorry, we could not save your details right now. Please try again shortly.', '', 500);
}

respond(true, '', $cfg['thanks']);
