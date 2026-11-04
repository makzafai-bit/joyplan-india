# JoyPlan India website

Static site: `index.html` plus images in `assets/`. No build step.

Deployed to Hostinger with hPanel's Git deployment. The `main` branch goes into `public_html`.

## Meta ads landing pages

- `/demo/`, `/masterclass/`, `/partner/` with a thank-you page under each (`/demo/thank-you/` etc.) and `/privacy/`.
- Shared styles and script: `lp/lp.css`, `lp/lp.js`. WhatsApp number, Meta Pixel ID and GA4 ID are set at the top of `lp/lp.js`; empty values switch those features off.
- Forms post to `lead.php`, which saves each lead to `../joyplan-leads/leads-<page>.csv` (the folder next to `public_html`, not reachable from the web). Set `NOTIFY_EMAIL` in `lead.php` to also get an e-mail per lead.
- The Lead / CompleteRegistration Pixel events fire on the thank-you pages, only after a real form submit.
