"""Blocks reused across pages: pricing, CTA band, FAQ, comparison table."""
from components import ARR, WA_ICON, btn, tbc

# Customer price list (Joyplan India poster, Nov 2026). Prices exclude 18% GST.
# INCL holds the poster's GST-inclusive final prices. The poster sells the device and
# the app separately, so "Device + app" = device price + app price (no bundle discount).
DEVICE, DEVICE_INCL = 8474, 9999
APP = {1: 1200, 3: 3300, 6: 6000, 12: 10000}
APP_INCL = {1: 1416, 3: 3894, 6: 7080, 12: 11800}
PRICES = {"dev": {t: DEVICE + p for t, p in APP.items()}, "app": dict(APP)}
INCL = {"dev": {t: DEVICE_INCL + p for t, p in APP_INCL.items()}, "app": dict(APP_INCL)}
TAGS = {6: "Most popular", 12: "Best value"}


def inr(n):
    s = str(n)
    if len(s) <= 3:
        return "&#8377;" + s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:]); head = head[:-2]
    if head:
        parts.insert(0, head)
    return "&#8377;" + ",".join(parts + [tail])


def gst(n):
    """Small line under a price: GST note plus the GST-inclusive figure."""
    return f"+ 18% GST &middot; {inr(n)} incl. GST"


def head(kicker, title, lead=None, cls="", level=2, hid=None):
    tag = f"h{level}"
    hc = "h-xl" if level == 1 else "h-l"
    i = f' id="{hid}"' if hid else ""
    ld = f'<p class="lead">{lead}</p>' if lead else ""
    if "split" in cls:
        return f'<div class="head {cls}"><div style="display:grid;gap:24px"><span class="kicker">{kicker}</span><{tag} class="{hc}"{i}>{title}</{tag}></div>{ld}</div>'
    return f'<div class="head {cls}"><span class="kicker">{kicker}</span><{tag} class="{hc}"{i}>{title}</{tag}>{ld}</div>'


def seg(default=12):
    b = "".join(f'<button type="button" data-term="{t}" aria-pressed="{"true" if t == default else "false"}">{t} mo</button>' for t in (1, 3, 6, 12))
    return f'<div class="seg" role="group" aria-label="Subscription length">{b}</div>'


def pricing_cards():
    t = tbc
    return f'''<div class="g3" data-stagger>
  <article class="pcard rv">
    <span class="tag" style="align-self:flex-start">Starter</span>
    <p class="aud">For individual professionals</p>
    <p class="price" data-price="app">{inr(PRICES["app"][12])}</p>
    <p class="gst" data-gst="app">{gst(INCL["app"][12])}</p>
    <p class="term" data-term-label="App subscription">App subscription &middot; 12 months</p>
    <ul><li class="no">Device not included (device-only price {inr(DEVICE)} + GST)</li><li>JoyPlan app: 2D, 3D, renders, drawings</li><li>Rendering / AI credits {t("TBC")}</li><li>Training &amp; support {t("TBC")}</li><li>Renewal {t("Terms TBC")}</li></ul>
    <a class="btn ghost" href="/book-a-demo/?package=starter" data-pkg-link="app">Get started</a>
  </article>
  <article class="pcard rec rv">
    <span class="ribbon">RECOMMENDED</span>
    <span class="tag o" style="align-self:flex-start">Professional</span>
    <p class="aud">For active interior designers &amp; architects</p>
    <p class="price" data-price="dev">{inr(PRICES["dev"][12])}</p>
    <p class="gst" data-gst="dev">{gst(INCL["dev"][12])}</p>
    <p class="term" data-term-label="Device + app subscription">Device + app subscription &middot; 12 months</p>
    <ul><li><b>JoyPlan measuring device included</b></li><li>Full app: measure-to-plan on site</li><li>Rendering / AI credits {t("TBC")}</li><li>Onboarding training {t("TBC")}</li><li>Renewal {t("Terms TBC")}</li></ul>
    <a class="btn primary" href="/book-a-demo/?package=professional" data-pkg-link="device">Get started{ARR}</a>
  </article>
  <article class="pcard rv">
    <span class="tag" style="align-self:flex-start">Business</span>
    <p class="aud">For design studios &amp; teams</p>
    <p class="price tbd">[Price to be confirmed]</p>
    <p class="term">Multi-seat &middot; custom term</p>
    <ul><li>Devices for the team {t("Qty TBC")}</li><li>Shared projects across devices</li><li>Seats &amp; credits {t("TBC")}</li><li>Team training &amp; priority support {t("TBC")}</li><li>Free business demo (offered today)</li></ul>
    <a class="btn ghost" href="/book-a-demo/?package=business">Talk to sales</a>
  </article>
</div>'''


CMP = [
    ("JoyPlan measuring device", f"&mdash; ({inr(DEVICE)} + GST separately)", "Included", "[TBC]"),
    ("Subscription length", "1 / 3 / 6 / 12 mo", "1 / 3 / 6 / 12 mo", "Custom"),
    ("2D floor plans &amp; multi-level", "&#10003;*", "&#10003;*", "&#10003;*"),
    ("3D view &amp; walkthrough", "&#10003;*", "&#10003;*", "&#10003;*"),
    ("Hard surfaces, furniture, materials", "&#10003;*", "&#10003;*", "&#10003;*"),
    ("Laser-linked measurement", "With compatible device", "&#10003;*", "&#10003;*"),
    ("Rendered images", "[TBC]", "[TBC]", "[TBC]"),
    ("720&deg; panoramas", "[TBC]", "[TBC]", "[TBC]"),
    ("AI image generation credits", "[TBC]", "[TBC]", "[TBC]"),
    ("Drawings, area inventory, estimates", "&#10003;*", "&#10003;*", "&#10003;*"),
    ("CAD export", "[TBC]", "[TBC]", "[TBC]"),
    ("Seats", "1", "1", "[TBC]"),
    ("Onboarding training", "Help videos", "[TBC]", "[TBC]"),
    ("Support", "[TBC]", "[TBC]", "[TBC]"),
    ("Renewal", "[TBC]", "[TBC]", "[TBC]"),
]


def cmp_table():
    def cell(v):
        return '<span class="tbc">[TBC]</span>' if v == "[TBC]" else v
    rows = "".join(f'<tr><th scope="row">{r}</th><td>{cell(a)}</td><td class="rec">{cell(b)}</td><td>{cell(c)}</td></tr>' for r, a, b, c in CMP)
    return f'''<div class="tbl-wrap"><table class="cmp"><caption class="sr-only">Feature comparison by package</caption><thead><tr><th scope="col">Included</th><th scope="col">Starter</th><th scope="col" class="rec">Professional &#9733;</th><th scope="col">Business</th></tr></thead><tbody>{rows}</tbody></table></div>
<p class="tiny" style="margin-top:12px">* Feature exists in the JoyPlan app today; availability per package to be confirmed. [TBC] = commercial detail awaiting JoyPlan sign-off.</p>'''


def band(title, second_label="WhatsApp an expert", second_href="#", second_wa=True, wa_text="Hi JoyPlan India, I'd like to book a demo."):
    extra = f'data-wa="{wa_text}"' if second_wa else ""
    return f'''<section class="band" aria-label="Book a demo"><div class="wrap"><h2 class="h-l rv">{title}</h2><div class="btns rv">{btn("Book a Free Demo", "/book-a-demo/", "darkb")}<a class="btn ghost" href="{second_href}" {extra}>{second_label}</a></div></div></section>'''


def faq(kicker, title, items, lead=None, cls="dark", extra=""):
    ds = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(items))
    ld = f'<p class="lead" style="margin-top:20px">{lead}</p>' if lead else ""
    return f'''<section class="sec {cls}" aria-labelledby="faq-h"><div class="wrap faq-grid"><div class="rv"><span class="kicker">{kicker}</span><h2 class="h-l" id="faq-h" style="margin-top:20px">{title}</h2>{ld}{extra}</div><div class="faq rv">{ds}</div></div></section>'''


def faq_ld(faqs):
    import re
    strip = lambda s: re.sub(r"<[^>]+>", "", s)
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}
