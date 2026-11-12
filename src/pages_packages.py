from components import btn, tbc
from shared import head, seg, pricing_cards, cmp_table, band, faq, faq_ld, inr, PRICES

CR = [("Home", "/"), ("Packages", "/packages/")]
WA = "Hi JoyPlan India, I have a question about JoyPlan packages and pricing."

FAQS = [("Can I try JoyPlan before paying?", "Yes. The app is free to install, and JoyPlan offers a free business demo with a specialist."),
        ("Are prices inclusive of GST?", f"GST treatment {tbc()}."),
        ("Can I start with the app and add the device later?", f"Yes, the device is sold separately at {inr(8474)}. Upgrade paths {tbc()}."),
        ("What happens when my subscription ends?", f"Renewal and data terms {tbc()}."),
        ("Do you offer studio or team pricing?", "Yes. The Business package is quoted per team. Book a demo or message us to get a quote.")]

grid = '<span class="h">Term</span><span class="h" style="border-left:1px solid var(--line)">App only</span><span class="h" style="border-left:1px solid var(--line)">Device + app</span>'
for t in (1, 3, 6, 12):
    lab = f"{t} month" + ("s" if t > 1 else "")
    grid += f'<span class="term">{lab}</span><button type="button" data-kind="app" data-term="{t}" aria-pressed="false" aria-label="App only, {lab}, {inr(PRICES["app"][t]).replace("&#8377;", "Rs ")}">{inr(PRICES["app"][t])}</button><button type="button" data-kind="dev" data-term="{t}" aria-pressed="{"true" if t == 12 else "false"}" aria-label="Device and app, {lab}">{inr(PRICES["dev"][t])}</button>'

BODY = f'''
<section class="hero center dark grid-bg" aria-labelledby="h1" style="min-height:0;padding-bottom:var(--sec)" data-pricing>
  <div class="glow o" style="width:800px;height:500px;left:50%;margin-left:-400px;top:-160px;opacity:.26"></div>
  <div class="wrap">
    <div class="hero-copy" data-enter style="margin-bottom:48px">
      {{{{CRUMBS}}}}
      <span class="kicker">Packages &amp; pricing &middot; INR</span>
      <h1 class="h-xl" id="h1">Find your perfect <span class="hl-box"><span class="hl">JoyPlan</span></span> package.</h1>
      <p class="lead">Install the app free, then choose a subscription length, with or without the measuring device.</p>
      <div>{seg()}</div>
    </div>
    {pricing_cards()}
    <div class="addon rv"><span class="tag">Add-on</span><b style="flex:1;min-width:180px">JoyPlan measuring device only</b><span class="p">{inr(8474)}</span>{btn("About the device", "/products/joyplan-device/", "ghost", sm=True)}</div>
  </div>
</section>

<section class="sec carbon" aria-labelledby="pl-h">
  <div class="wrap split" style="align-items:start">
    <div class="rv">
      <span class="kicker">The full price list</span>
      <h2 class="h-l" id="pl-h" style="margin:20px 0">Every combination, side by side.</h2>
      <p class="lead">Tap a price to select it. Your selection carries into the demo booking.</p>
      <div class="panel" id="psel" style="margin-top:32px"><p class="label">Your selection</p><p class="h-m sel-name" style="margin:10px 0 6px">Device + app &middot; 12 months</p><p class="sel-price" style="font:850 40px/1 var(--f-disp);font-stretch:112%;color:var(--yellow)">{inr(15000)}</p><a class="btn primary" style="margin-top:22px" href="/book-a-demo/?package=device-12">Book a demo with this package</a></div>
    </div>
    <div class="rv"><div class="pgrid" data-pgrid="psel" role="group" aria-label="Full price list">{grid}</div><p class="tiny" style="margin-top:14px">Source: JoyPlan India's shared price list. GST, payment terms and any launch offers to be confirmed before publishing.</p></div>
  </div>
</section>

<section class="sec bone" aria-labelledby="cmp-h">
  <div class="wrap">
    <div class="head"><span class="kicker">Feature comparison</span><h2 class="h-l" id="cmp-h">What's in each package</h2><div>{tbc("Per-tier inclusions to be confirmed by JoyPlan")}</div></div>
    <div class="rv">{cmp_table()}</div>
  </div>
</section>

<section class="sec dark" aria-labelledby="ab-h">
  <div class="wrap">
    {head("After you buy", "Renewal, training and support.", hid="ab-h")}
    <div class="g3" data-stagger>
      <article class="panel case rv"><span class="label">Renewal</span><b>Keep your projects going</b><p>Renew for 1, 3, 6 or 12 months.</p><p style="margin-top:12px">{tbc("Renewal terms to be confirmed")}</p></article>
      <article class="panel case rv"><span class="label">Training</span><b>Learn fast</b><p>Short, searchable help videos, plus guided onboarding for packages.</p><p style="margin-top:12px">{tbc("Onboarding format TBC")}</p></article>
      <article class="panel case rv"><span class="label">Support</span><b>People nearby</b><p>Teams in Bengaluru and Kozhikode; email service@joyplan.com.</p><p style="margin-top:12px">{tbc("Hours &amp; SLA TBC")}</p></article>
    </div>
  </div>
</section>
{faq("Buying FAQs", "Questions before checkout", FAQS, cls="carbon", extra='<div style="margin-top:28px"><a class="btn wa" href="#" data-wa="' + WA + '">Ask on WhatsApp</a></div>')}
{band("Not sure which fits? We'll show you.", "WhatsApp an expert", "#", True, WA)}
'''

PAGES = [{"path": "/packages/", "active": "/packages/", "crumbs": CR, "wa": WA,
          "title": "JoyPlan Packages &amp; Pricing in India | Device + Software Plans",
          "desc": "Compare JoyPlan app-only and device + software packages for 1, 3, 6 and 12 months. Transparent INR pricing, training and support.",
          "ld": [faq_ld(FAQS)], "body": BODY}]
