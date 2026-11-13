#!/usr/bin/env python3
"""Builds the JoyPlan India main site into static HTML.

Run from the repo root:  python3 src/build.py
Every page is written as <path>/index.html. Edit copy in src/pages_*.py and shared parts here.
The /demo, /masterclass, /partner landing pages are separate and are not touched.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from components import logo, ARR, WA_ICON  # noqa: E402
import pages_home, pages_device, pages_software, pages_features, pages_packages, pages_solutions, pages_demo  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://joyplanindia.com"
VER = "8"
NAV = [("Device", "/products/joyplan-device/"), ("Software", "/software/joyplan-software/"), ("Features", "/features/"),
       ("Solutions", "/solutions/"), ("Packages", "/packages/"), ("Contact", "/contact/")]

ORG = {"@context": "https://schema.org", "@type": "Organization", "name": "Joyplan India", "url": SITE + "/",
       "logo": SITE + "/assets/joyplan-india-logo.svg", "email": "service@joyplan.com",
       "address": [{"@type": "PostalAddress", "streetAddress": "BL Commerce, 7th Cross Road, Dollar Layout, Stage 2", "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "addressCountry": "IN"},
                   {"@type": "PostalAddress", "streetAddress": "Third Floor, CK Tower, Near Bismi Hypermarket, Kannur Rd, West Nadakkave, Vandipetta, Vellayil", "addressLocality": "Kozhikode", "addressRegion": "Kerala", "postalCode": "673011", "addressCountry": "IN"}]}


def crumbs_html(items):
    lis = []
    for i, (name, href) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li><span aria-current="page">{name}</span></li>')
        else:
            lis.append(f'<li><a href="{href}">{name}</a></li>')
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{"".join(lis)}</ol></nav>'


def crumbs_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + h} for i, (n, h) in enumerate(items)]}


def page(p):
    path, active = p["path"], p.get("active")
    links = "".join(f'<a href="{h}"{" aria-current=page" if h == active else ""}>{n}</a>' for n, h in NAV)
    mlinks = "".join(f'<a href="{h}"{" aria-current=page" if h == active else ""}>{n}<span aria-hidden="true">&rarr;</span></a>' for n, h in [("Home", "/")] + NAV)
    if p.get("nav_wa"):
        cta = f'<a class="btn wa sm" href="#" data-wa="Hi JoyPlan India, I\'d like to book a demo.">{WA_ICON}WhatsApp</a>'
    else:
        cta = f'<a class="btn primary sm" href="/book-a-demo/">Book a Free Demo{ARR}</a>'
    lds = [ORG] + p.get("ld", [])
    if p.get("crumbs"):
        lds.append(crumbs_ld(p["crumbs"]))
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    body = p["body"]
    if p.get("crumbs"):
        body = body.replace("{{CRUMBS}}", crumbs_html(p["crumbs"]))
    canonical = SITE + path
    noindex = '<meta name="robots" content="noindex">' if p.get("noindex") else ""
    return f'''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p["title"]}</title>
<meta name="description" content="{p["desc"]}">
<link rel="canonical" href="{canonical}">
{noindex}
<meta property="og:type" content="website">
<meta property="og:site_name" content="JoyPlan India">
<meta property="og:title" content="{p["title"]}">
<meta property="og:description" content="{p["desc"]}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/site/og-share.jpg">
<meta property="og:image:secure_url" content="{SITE}/assets/site/og-share.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="JoyPlan India home page: Measure Smarter. Design Faster. Impress Better.">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{p["title"]}">
<meta name="twitter:description" content="{p["desc"]}">
<meta name="twitter:image" content="{SITE}/assets/site/og-share.jpg">
<meta name="theme-color" content="#0B0B0B">
<link rel="icon" href="/assets/joyplan-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..900&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/site/site.css?v={VER}">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="pwipe" aria-hidden="true"></div>
<header class="nav">
  <div class="wrap">
    {logo("n")}
    <nav class="nav-links" aria-label="Main">{links}</nav>
    <div class="nav-cta">{cta}<button class="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span></button></div>
  </div>
</header>
<div class="menu" id="menu" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="menu-top">{logo("m")}<button class="menu-close" type="button" aria-label="Close menu">&times;</button></div>
  <nav aria-label="Mobile">{mlinks}</nav>
  <a class="btn primary full" href="/book-a-demo/">Book a Free Demo{ARR}</a>
  <p class="tiny meta">service@joyplan.com &middot; Bengaluru &middot; Kozhikode</p>
</div>
<main id="main">
{body}
</main>
<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div>{logo("f")}<p class="blurb">Laser measurement and 2D/3D design software for interior designers, architects and builders across India.</p><a class="mono small" href="mailto:service@joyplan.com">service@joyplan.com</a>
        <div class="apps"><span class="tag">App Store</span><span class="tag">Google Play</span></div></div>
      <div><h4>Product</h4><ul><li><a href="/products/joyplan-device/">JoyPlan Device</a></li><li><a href="/software/joyplan-software/">JoyPlan Software</a></li><li><a href="/features/">Features</a></li><li><a href="/packages/">Packages</a></li><li><a href="/book-a-demo/">Book a demo</a></li></ul></div>
      <div><h4>Solutions</h4><ul><li><a href="/solutions/#interior-designers">Interior designers</a></li><li><a href="/solutions/#architects">Architects</a></li><li><a href="/solutions/#civil-engineers">Civil engineers</a></li><li><a href="/solutions/#modular-kitchen">Modular kitchens</a></li><li><a href="/solutions/#furniture-designers">Furniture designers</a></li></ul></div>
      <div><h4>Offices</h4><address><span><b class="label">Head office</b><br>BL Commerce, 7th Cross Road, Dollar Layout, Stage 2, Bengaluru, Karnataka</span><span><b class="label">Kerala branch</b><br>Third Floor, CK Tower, Kannur Rd, West Nadakkave, Kozhikode, Kerala 673011</span></address></div>
    </div>
    <div class="giant" aria-hidden="true">joyplan</div>
    <div class="foot-base"><span>&copy; 2026 JoyPlan India</span><span><a href="/privacy/">Privacy</a> &middot; <a href="/contact/">Contact</a></span></div>
  </div>
</footer>
<a class="wa-float"{" hidden" if p.get("nav_wa") else ""} href="#" data-wa="{p.get("wa", "Hi JoyPlan India, I'd like to book a demo.")}" aria-label="WhatsApp us"><i>{WA_ICON}</i><span>WhatsApp us</span></a>
<div class="mbar"><a class="btn primary" href="/book-a-demo/">Book a Free Demo</a><a class="btn wa" href="#" data-wa="{p.get("wa", "Hi JoyPlan India, I'd like to book a demo.")}">WhatsApp</a></div>
<script src="/assets/site/site.js?v={VER}" defer></script>
</body>
</html>
'''


def write(p):
    rel = p["path"].strip("/")
    out = os.path.join(ROOT, rel, "index.html") if rel else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(page(p))
    print("wrote", os.path.relpath(out, ROOT))


def main():
    pages = []
    for mod in (pages_home, pages_device, pages_software, pages_features, pages_packages, pages_solutions, pages_demo):
        pages.extend(mod.PAGES)
    for p in pages:
        write(p)
    urls = "".join(f"<url><loc>{SITE}{p['path']}</loc></url>" for p in pages if not p.get("noindex"))
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /src/\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    main()
