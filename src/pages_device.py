from components import ARR, btn, tbc, device, room_scene
from shared import head, band, faq, inr

WA = "Hi JoyPlan India, I'd like to know more about the JoyPlan measuring device."
CR = [("Home", "/"), ("Products", "/products/joyplan-device/"), ("JoyPlan Device", "/products/joyplan-device/")]

FAQS = [("Do I need the app to use the device?", f"The device is designed to work with the JoyPlan app, which turns readings into plans. Stand-alone use details {tbc()}."),
        ("Which phones and tablets does it work with?", "JoyPlan is on the App Store and Google Play, and projects share across phone, tablet, laptop and desktop."),
        ("Can I use my existing laser meter instead?", "The JoyPlan app lists compatible hardware and currently does not support Bosch Bluetooth laser measures. Check with us before you buy."),
        ("What is the warranty?", f"Warranty terms {tbc()}."),
        ("Can I see it working before I buy?", "Yes. JoyPlan offers a free business demo, online or in person.")]

SPECS = [("Measurement type", "Laser distance"), ("Connectivity", "Bluetooth, pairs with the JoyPlan app"), ("Measuring range", None), ("Accuracy", None),
         ("Units", None), ("Display", None), ("Battery &amp; charging", None), ("Dimensions &amp; weight", None), ("In the box", None)]
spec_rows = "".join(f'<tr><td>{k}</td><td>{v if v else tbc()}</td></tr>' for k, v in SPECS)

WAYS = [("Device only", "JoyPlan measuring device", 8474, False), ("Device + 1 month", "Device + 1-month app subscription", 6500, False),
        ("Device + 3 months", "Device + 3-month app subscription", 8450, False), ("Device + 6 months", "Device + 6-month app subscription", 11000, False),
        ("Device + 12 months", "Device + 12-month app subscription &middot; Professional", 15000, True)]
ways_rows = "".join(f'<tr{" class=hi" if hi else ""}><td>{o}</td><td>{inc}</td><td class="p">{inr(p)}</td><td>{btn("Get started" if hi else "Enquire", "/book-a-demo/?package=" + ("professional" if hi else "device"), "primary" if hi else "ghost", hi, sm=True)}</td></tr>' for o, inc, p, hi in WAYS)

USES = [("New flat, Bengaluru", "Apartment handover", "Capture an as-built plan room by room."), ("Villa, Kozhikode", "Villa renovation", "Multi-level homes measured floor by floor."),
        ("Kitchen fit-out", "Kitchen site visit", "Wall lengths ready for module planning."), ("Caf&eacute; interior", "Commercial fit-out", "Retail and office spaces, quickly mapped.")]


def use_vis(i):
    c = ["#C8961E", "#C8961E", "#a0522d", "#a0522d"][i]
    return f'<svg viewBox="0 0 300 200" aria-hidden="true"><rect width="300" height="200" fill="#151515"/><path d="M0 0L80 50H220L300 0Z" fill="#1b1b1b"/><path d="M0 200L80 150H220L300 200Z" fill="#1d1d1d"/><rect x="80" y="50" width="140" height="100" fill="#222"/><rect x="125" y="70" width="40" height="36" fill="{c}" opacity=".8"/><path d="M60 175L190 110" stroke="#FD4100" stroke-width="2.5"/><circle cx="190" cy="110" r="4" fill="#FD4100"/></svg>'


uses = "".join(f'<article class="panel rv" style="padding:0;overflow:hidden"><div style="position:relative;border-bottom:1px solid var(--line)">{use_vis(i)}<span class="illus" style="position:absolute;left:10px;top:10px">Shot: {s}</span></div><div style="padding:18px"><b class="h-s" style="font-size:16px">{t}</b><p class="small muted" style="margin-top:6px">{d}</p></div></article>' for i, (s, t, d) in enumerate(USES))

BODY = f'''
<section class="hero dark grid-bg" aria-labelledby="h1">
  <div class="glow o" style="width:640px;height:640px;right:-120px;top:-160px" data-parallax="70"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy" data-enter data-parallax-copy>
      {{{{CRUMBS}}}}
      <span class="kicker">JoyPlan measurement device</span>
      <h1 class="h-xl" id="h1">The measuring device that <span class="hl-box"><span class="hl">draws</span></span> while you measure.</h1>
      <p class="lead">A laser measuring device built to pair with the JoyPlan app. Every reading lands on the wall you're measuring, so the floor plan exists before you leave the site.</p>
      <div class="btns">{btn("Book a demo", "/book-a-demo/?package=professional")}{btn("Buy with a package", "/packages/", "ghost", False)}</div>
      <div><div class="stat-chips"><div><span class="label">Device only</span><b>{inr(8474)}</b></div><div><span class="label">Device + 1-month app</span><b>{inr(6500)}</b></div></div><p class="tiny" style="margin-top:10px">Per JoyPlan India's shared price list. Confirm before launch.</p></div>
    </div>
    <div class="hero-vis dev-hero" data-tilt-area data-parallax-vis>
      <svg viewBox="0 0 600 560" style="position:absolute;inset:0;width:100%;height:100%" aria-hidden="true"><g fill="none" stroke="rgba(253,65,0,.35)"><circle cx="300" cy="290" r="170"><animateTransform attributeName="transform" type="rotate" from="0 300 290" to="360 300 290" dur="40s" repeatCount="indefinite"/></circle><circle cx="300" cy="290" r="240" stroke-dasharray="4 10"><animateTransform attributeName="transform" type="rotate" from="360 300 290" to="0 300 290" dur="60s" repeatCount="indefinite"/></circle></g><path d="M300 20V150" stroke="#FD4100" stroke-width="2"/><circle cx="300" cy="80" r="4" fill="#FD4100"/></svg>
      <div style="position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);perspective:900px"><div data-tilt style="transition:transform .3s var(--ease-out)">{device("3.480", cycle="3.480,4.625,2.715,11.200,7.600", cls="lg", style="--s:1.55")}</div></div>
      <div class="glass float" style="position:absolute;left:2%;top:24%"><p class="label">Connection</p><p style="font-weight:600;font-size:14px;margin-top:4px;display:flex;gap:8px;align-items:center"><i class="livedot"></i>Bluetooth &rarr; JoyPlan app</p></div>
      <div class="glass float d2" style="position:absolute;right:0;top:46%"><p class="label">Range</p><p style="margin-top:6px">{tbc()}</p></div>
      <div class="glass float d3" style="position:absolute;left:4%;bottom:12%"><p class="label">Accuracy</p><p style="margin-top:6px">{tbc()}</p></div>
      <span class="illus" style="position:absolute;right:0;bottom:0">Illustrative render &middot; move pointer to rotate</span>
    </div>
  </div>
</section>

<section class="sec dark tight" style="border-top:1px solid var(--line)" aria-label="Introduction">
  <div class="wrap split">
    <h2 class="h-l rv">A laser for distance.<br><span class="hl">An app for everything after.</span></h2>
    <p class="lead rv">On its own it measures. Paired with JoyPlan it becomes the first step of a design: walls, doors and windows placed as you go, then 3D, renders, drawings and estimates from the same data.</p>
  </div>
</section>

<section class="sec bone" aria-labelledby="spec-h">
  <div class="wrap split" style="align-items:start">
    <div>
      {head("Specifications", "Technical sheet", "Specifications will be published from JoyPlan's official product data. Placeholders are marked until then.", hid="spec-h")}
      <svg viewBox="0 0 260 300" style="width:220px;margin-top:-16px" aria-hidden="true"><rect x="70" y="40" width="70" height="200" rx="16" fill="none" stroke="#111" stroke-width="2.5"/><path d="M70 72h70" stroke="#111" stroke-width="2"/><rect x="70" y="40" width="70" height="30" rx="14" fill="#FD4100"/><circle cx="105" cy="55" r="5" fill="#111"/><rect x="84" y="90" width="42" height="40" rx="3" fill="none" stroke="#111" stroke-width="2"/><circle cx="105" cy="170" r="16" fill="none" stroke="#111" stroke-width="2"/><path d="M105 40V8" stroke="#C2410C" stroke-dasharray="3 3"/><text x="112" y="16" font-family="JetBrains Mono" font-size="9" fill="#55504A">LASER</text><path d="M170 40V240M164 40H176M164 240H176" stroke="#C2410C" stroke-width="1.5"/><text x="180" y="144" font-family="JetBrains Mono" font-size="10" fill="#C2410C">H [TBC]</text><path d="M70 262H140M70 256V268M140 256V268" stroke="#C2410C" stroke-width="1.5"/><text x="80" y="286" font-family="JetBrains Mono" font-size="10" fill="#C2410C">W [TBC]</text></svg>
    </div>
    <div class="tbl-wrap rv"><table class="spec"><caption class="sr-only">Device specifications</caption><tbody>{spec_rows}</tbody></table></div>
  </div>
</section>

<section class="sec dark" aria-labelledby="ppd-h">
  <div class="wrap">
    {head("How the device works", "Pair. Point. Done.", hid="ppd-h")}
    <div class="g3" data-stagger>
      <article class="panel lift rv"><span class="label" style="color:var(--orange)">01 &middot; Pair</span><svg viewBox="0 0 300 140" style="margin:22px 0" aria-hidden="true"><rect x="60" y="30" width="30" height="80" rx="8" fill="#222" stroke="#444"/><rect x="60" y="30" width="30" height="14" rx="6" fill="#FD4100"/><path d="M100 70H190" stroke="#FD4100" stroke-width="2"/><rect x="195" y="25" width="60" height="90" rx="10" fill="none" stroke="#F4F1EC" stroke-width="2"/><circle cx="225" cy="70" r="12" fill="none" stroke="#FFC20E" stroke-width="2"/><path d="M219 70l4 4 8-8" stroke="#FFC20E" stroke-width="2" fill="none"/></svg><h3 class="h-s">Connect to the app</h3><p class="small muted" style="margin-top:8px">Pair the device with JoyPlan on your phone or tablet over Bluetooth.</p></article>
      <article class="panel lift rv"><span class="label" style="color:var(--orange)">02 &middot; Point &amp; press</span><svg viewBox="0 0 300 140" style="margin:22px 0" aria-hidden="true"><rect x="30" y="58" width="80" height="26" rx="8" fill="#222" stroke="#444"/><rect x="30" y="58" width="16" height="26" rx="6" fill="#FD4100"/><path d="M110 71H250" stroke="#FD4100" stroke-width="2.5"/><path d="M252 30V112" stroke="#F4F1EC" stroke-width="3"/><circle cx="250" cy="71" r="5" fill="#FD4100"/><text x="180" y="58" font-family="JetBrains Mono" font-size="12" fill="#FFC20E" text-anchor="middle">3.480 m</text></svg><h3 class="h-s">Measure the wall</h3><p class="small muted" style="margin-top:8px">Aim at the surface and press once. The reading appears on the device and in the app.</p></article>
      <article class="panel lift rv"><span class="label" style="color:var(--orange)">03 &middot; Watch it build</span><svg viewBox="0 0 300 140" style="margin:22px 0" aria-hidden="true" class="plan2d anim"><path class="w" d="M70 20H230V120H70Z M150 20V70 M70 80H120" style="stroke-width:4"/><path d="M70 10H230" stroke="#FFC20E" stroke-width="1.5"/></svg><h3 class="h-s">The plan draws itself</h3><p class="small muted" style="margin-top:8px">Each value snaps to the selected wall, so the 2D plan grows as you walk the space.</p></article>
    </div>
  </div>
</section>

<section class="sec carbon" aria-labelledby="use-h">
  <div class="wrap">
    {head("Real-world usage", "Wherever the tape used to go.", "Photography of JoyPlan users on Indian sites goes here. Until then, these line drawings mark each scene from the shot list.", cls="split", hid="use-h")}
    <div class="g4" data-stagger>{uses}</div>
  </div>
</section>

<section class="sec dark" aria-labelledby="con-h">
  <div class="wrap">
    {head("Device &times; software connectivity", "One reading. Every screen.", cls="center", hid="con-h")}
    <div class="diagram rv">
      <div class="node"><svg viewBox="0 0 40 90" width="34" aria-hidden="true"><rect x="4" y="2" width="32" height="86" rx="9" fill="#222" stroke="#444"/><rect x="4" y="2" width="32" height="18" rx="8" fill="#FD4100"/><circle cx="20" cy="56" r="8" fill="#FD4100"/></svg><b>JoyPlan device</b></div>
      <div class="link"><b>BLUETOOTH</b></div>
      <div class="node"><svg viewBox="0 0 110 80" width="110" aria-hidden="true"><rect x="2" y="2" width="106" height="76" rx="8" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><path d="M20 18H90V62H20Z M55 18V40" fill="none" stroke="#FD4100" stroke-width="2"/></svg><b>JoyPlan app &middot; phone / tablet</b></div>
      <div class="link"><b>SHARE ACROSS DEVICES</b></div>
      <div class="node"><svg viewBox="0 0 120 90" width="120" aria-hidden="true"><rect x="10" y="2" width="100" height="66" rx="4" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><path d="M2 76H118" stroke="#F4F1EC" stroke-width="3"/><path d="M28 50L48 28L66 44L92 22" fill="none" stroke="#FFC20E" stroke-width="2"/></svg><b>Laptop &middot; desktop</b></div>
    </div>
    <p class="tiny" style="margin-top:16px;text-align:center">Compatibility note: the JoyPlan app publishes a compatible-hardware list and currently does not support Bosch Bluetooth laser measures.</p>
  </div>
</section>

<section class="sec bone" aria-labelledby="lr-h">
  <div class="wrap">
    {head("Benefits for professionals", "Less re-measuring. More designing.", hid="lr-h")}
    <div class="g4" data-stagger>
      <article class="panel case rv"><span class="label">01</span><b>No transcription</b><p>Readings go straight into the plan: nothing copied from a notepad.</p></article>
      <article class="panel case rv"><span class="label">02</span><b>One visit</b><p>See gaps in the plan while you're still on site, not back at the office.</p></article>
      <article class="panel case rv"><span class="label">03</span><b>Client confidence</b><p>Measuring with a connected device looks as professional as it is.</p></article>
      <article class="panel case rv"><span class="label">04</span><b>Ready for 3D</b><p>The same data feeds 3D, renders, drawings and estimates.</p></article>
    </div>
  </div>
</section>

<section class="sec dark" aria-labelledby="ways-h">
  <div class="wrap">
    <div class="head split"><div style="display:grid;gap:24px"><span class="kicker">Package compatibility</span><h2 class="h-l" id="ways-h">Ways to get the device</h2></div><div>{btn("Compare all packages", "/packages/", "ghost")}</div></div>
    <div class="tbl-wrap rv"><table class="ways"><caption class="sr-only">Device purchase options in INR</caption><thead><tr><th scope="col">Option</th><th scope="col">Includes</th><th scope="col">Price (INR)</th><th scope="col"><span class="sr-only">Action</span></th></tr></thead><tbody>{ways_rows}</tbody></table></div>
    <p class="tiny" style="margin-top:12px">Prices as per JoyPlan India's shared price list. GST, warranty and delivery terms to be confirmed.</p>
  </div>
</section>
{faq("FAQs", "Before you buy", FAQS, lead="Still unsure? A specialist can walk you through it in a free demo.", cls="carbon")}
{band("Hold it on your next site visit.", "Buy now", "/packages/", False)}
'''

PAGES = [{"path": "/products/joyplan-device/", "active": "/products/joyplan-device/", "crumbs": CR, "wa": WA,
          "title": "JoyPlan Laser Measuring Device for Interior Designers | JoyPlan India",
          "desc": "A Bluetooth laser measuring device that sends every reading straight into the JoyPlan app, so the floor plan builds itself on site.",
          "ld": [], "faqs": FAQS, "body": BODY}]
from shared import faq_ld  # noqa: E402
PAGES[0]["ld"].append(faq_ld(FAQS))
