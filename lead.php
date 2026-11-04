<?php
/*
 * Lead handler for the landing pages (/demo, /masterclass, /partner).
 *
 * Saves every lead as a row in a CSV file, one file per form:
 *   ../joyplan-leads/leads-demo.csv   (the folder next to public_html, not web-visible)
 * Falls back to ./leads-data/ (blocked from the web by .htaccess) if that folder can't be created.
 *
 * Optional e-mail alert: put an address in NOTIFY_EMAIL below.
 */
declare(strict_types=1);

const NOTIFY_EMAIL = '';                       // e.g. 'sales@joyplanindia.com'
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
if (!filter_var($row['email'], FILTER_VALIDATE_EMAIL)) {
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

// Pick a storage folder outside the web root if we can.
$dir = dirname(__DIR__) . '/joyplan-leads';
if (!is_dir($dir) && !@mkdir($dir, 0750, true)) {
    $dir = __DIR__ . '/leads-data';
    if (!is_dir($dir)) @mkdir($dir, 0750, true);
}
if (!is_dir($dir) || !is_writable($dir)) {
    respond(false, 'Sorry, we could not save your details right now. Please try again shortly.', '', 500);
}
if (str_starts_with($dir, __DIR__) && !file_exists($dir . '/.htaccess')) {
    @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n");
}

$file = $dir . '/leads-' . $type . '.csv';
$fh = @fopen($file, 'ab');
if (!$fh) {
    respond(false, 'Sorry, we could not save your details right now. Please try again shortly.', '', 500);
}
flock($fh, LOCK_EX);
if (filesize($file) === 0) {
    fwrite($fh, "\xEF\xBB\xBF");               // UTF-8 BOM so Excel shows ₹ and Indian names correctly
    fputcsv($fh, array_keys($record));
}
// Guard against spreadsheet formula injection.
$safe = array_map(fn($v) => preg_match('/^[=+\-@\t\r]/', (string)$v) ? "'" . $v : $v, array_values($record));
fputcsv($fh, $safe);
fflush($fh);
flock($fh, LOCK_UN);
fclose($fh);

if (NOTIFY_EMAIL !== '') {
    $lines = [];
    foreach ($record as $k => $v) {
        $lines[] = str_pad($k, 16) . ': ' . $v;
    }
    $subject = 'New ' . $cfg['tag'] . ' lead: ' . preg_replace('/[\r\n]+/', ' ', $row['full_name']);
    $headers = 'From: Joyplan India <' . MAIL_FROM . ">\r\n"
             . 'Reply-To: ' . preg_replace('/[\r\n]+/', '', $row['email']) . "\r\n"
             . "Content-Type: text/plain; charset=utf-8\r\n";
    @mail(NOTIFY_EMAIL, '=?UTF-8?B?' . base64_encode($subject) . '?=', implode("\n", $lines), $headers);
}

respond(true, '', $cfg['thanks']);
