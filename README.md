# JoyPlan India website

Static site, no build step on the server. Deployed to Hostinger with hPanel's Git deployment: the `main` branch goes into `public_html`.

## Main site

Built from the Zelto Tech build spec and design template (November 2026).

| Page | Address |
| --- | --- |
| Home | `/` |
| Device | `/products/joyplan-device/` |
| Software | `/software/joyplan-software/` |
| Features | `/features/` |
| Packages | `/packages/` |
| Solutions | `/solutions/` |
| Book a demo / Contact | `/book-a-demo/`, `/contact/` (thank-you: `/book-a-demo/thank-you/`) |

- Styles and script: `assets/site/site.css`, `assets/site/site.js`. Colours and fonts are the tokens at the top of `site.css`.
- WhatsApp number: set `JPS.WHATSAPP` at the top of `assets/site/site.js` (digits with country code). Empty opens WhatsApp with a pre-filled message and no number.
- Prices: `JPS.PRICES` in `site.js` (used by the duration toggles) and `PRICES` in `src/shared.py` (printed into the pages). Change both.
- Anything not yet confirmed by JoyPlan is shown as a yellow `[To be confirmed]` tag. Search the `src/` files for `tbc(` to find them.

### Editing pages

The HTML is generated. Edit copy in `src/pages_*.py` (one file per page) and shared parts in `src/build.py`, `src/shared.py` and `src/components.py`, then run:

```
python3 src/build.py
```

and commit the regenerated `index.html` files together with the source change. It also rewrites `sitemap.xml` and `robots.txt`.

### Forms

The homepage enquiry form and the book-a-demo form post to `lead.php` (form types `enquiry` and `book`), which saves leads to `../joyplan-leads/leads-enquiry.csv` and `leads-book.csv`, next to `public_html`.

## Meta ads landing pages

- `/demo/`, `/masterclass/`, `/partner/` with a thank-you page under each (`/demo/thank-you/` etc.) and `/privacy/`.
- Shared styles and script: `lp/lp.css`, `lp/lp.js`. WhatsApp number, Meta Pixel ID and GA4 ID are set at the top of `lp/lp.js`; empty values switch those features off.
- Forms post to `lead.php`, which saves each lead to `../joyplan-leads/leads-<page>.csv` (the folder next to `public_html`, not reachable from the web). Set `NOTIFY_EMAIL` in `lead.php` to also get an e-mail per lead.
- The Lead / CompleteRegistration Pixel events fire on the thank-you pages, only after a real form submit.
