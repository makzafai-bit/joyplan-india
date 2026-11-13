from components import ARR, WA_ICON, btn, tlink, tbc, device, img, frame, fit
from shared import head, seg, pricing_cards, cmp_table, inr

WA = "Hi JoyPlan India, I'd like to book a demo."

# Animated hero composite. Positions are percentages of the 1870x841 design (JoyPlan's hero image),
# so the scene scales with the page. Cards slide in along the ribbon, then drift slowly; the device counts up a live reading.
HERO_TILES = [("f2d", "2D Plan", 1), ("f3d", "3D Design", 2), ("fai", "Render", 3)]
HERO_ANIM = (
    '<div class="hero-anim" role="img" aria-label="The JoyPlan laser measure reading 4.625 metres, with a 2D plan, a 3D design and a finished render moving along a ribbon of light">'
    + img("herobg", "ha-bg", alt="", lazy=False, sizes="(max-width: 720px) 100vw, 1280px")
    + "".join(f'<div class="ha-tile t{n}"><div class="ha-float"><div class="ha-card">{img(k, alt="", lazy=False, sizes="(max-width: 720px) 30vw, 260px")}</div><span class="ha-lab">{lab}</span></div></div>' for k, lab, n in HERO_TILES)
    + '<span class="ha-chev c1" aria-hidden="true"></span><span class="ha-chev c2" aria-hidden="true"></span>'
    + '<div class="ha-dev">' + device("0.000", cls="count", style="", ) + '</div>'
    + '</div>'
)

HERO = f'''
<section class="hero hero-scene dark" aria-labelledby="h1">
  {HERO_ANIM}
  <div class="hs-shade" aria-hidden="true"></div>
  <div class="hs-copy hero-copy" data-enter>
    <span class="kicker">Laser measurement &times; 2D/3D design software</span>
    <h1 class="h-xl" id="h1">Measure Smarter.<br>Design Faster.<br><span class="hl-box"><span class="hl">Impress Better.</span></span></h1>
    <p class="lead">Transform the way you measure, plan and present spaces with JoyPlan's connected measurement and design ecosystem.</p>
    <div class="btns">{btn("Experience JoyPlan", "#ecosystem")}{btn("Book a Free Demo", "/book-a-demo/", "ghost", False)}</div>
    <p class="hero-meta"><span>App Store</span><span>Google Play</span><span>Bengaluru</span><span>Kozhikode</span><span>Free business demo</span></p>
  </div>
</section>
<div class="strip" aria-hidden="true"><div class="strip-in">{"".join(f"<span>{w}</span>" for w in ["Measure", "Create", "Design", "Present", "2D floor plans", "3D design", "Renders", "720&deg; panorama", "CAD export", "Bengaluru", "Kozhikode"] * 2)}</div></div>
'''

TRANSFORM = f'''
<section class="sec bone" aria-labelledby="tr-h">
  <div class="wrap">
    {head("The transformation", "From Measurements to Meaningful Designs.", "Drag the line. On the left, the way most site visits still end: tape, paper, a second trip. On the right, the same room, measured once and already a plan.", hid="tr-h")}
    <div class="ba photo rv">
      <div class="ba-l">{fit("trad", sizes="(max-width: 720px) 100vw, 1280px")}<div class="tags l"><span class="tag" style="background:#fff">Traditional</span><span class="tag" style="background:#fff">Tape &middot; paper &middot; second visit</span></div></div>
      <div class="ba-r">{fit("jp", sizes="(max-width: 720px) 100vw, 1280px")}<div class="tags r"><span class="tag" style="background:#0B0B0B">JoyPlan</span><span class="tag o" style="background:var(--signal);color:var(--ink)">Measured once &middot; plan + 3D on site</span></div></div>
      <input type="range" min="0" max="100" value="50" aria-label="Compare traditional measuring with JoyPlan">
      <div class="ba-h"></div>
    </div>
    <div class="steps" data-stagger>
      <div class="rv"><span class="n">01</span><b>Measurement</b><p>Each laser reading lands in the app, against the right wall.</p></div>
      <div class="rv"><span class="n">02</span><b>2D floor plan</b><p>Walls, doors and windows drawn while you're still in the room.</p></div>
      <div class="rv"><span class="n">03</span><b>3D visualisation</b><p>The same plan, presented in immersive 3D, with no redrawing.</p></div>
    </div>
  </div>
</section>'''

HOTS = [("Laser aperture", "Point at the wall. The reading targets the spot you see.", "calc(50% - 6px)", "-1%"),
        ("Built-in levels", "Two bubble levels help you hold the device straight for a true reading.", "calc(100% + 10px)", "27%"),
        ("Live readout", "Distance shown on the device and in the app at the same time.", "-24px", "33%"),
        ("Bluetooth to app", "The 50 m model carries a Bluetooth mark and pairs with the JoyPlan app, so readings land on the plan.", "calc(100% + 10px)", "53%"),
        ("One-press READ key", "The red READ key takes the reading. Accuracy and battery specs to be confirmed.", "-24px", "62%")]
hot_html = "".join(f'<button type="button" class="hot" style="left:{x};top:{y}" aria-pressed="{"true" if i == 0 else "false"}" data-t="{t}" data-c="{c}" aria-label="{t}"></button>' for i, (t, c, x, y) in enumerate(HOTS))

ECO = f'''
<section class="sec dark" id="ecosystem" aria-labelledby="eco-h">
  <div class="wrap">
    {head("The ecosystem", "One Ecosystem. Endless Design Possibilities.", "A measuring device and a design app, built to talk to each other. Use them together on site, or the app on its own anywhere.", hid="eco-h")}
    <div class="g2" data-stagger>
      <article class="panel prod-card rv">
        <div class="prod-top"><span class="tag">Product 01</span><span class="label">Hardware</span></div>
        <h3 class="h-m">JoyPlan Measurement Device</h3>
        <div class="prod-vis devbox grid-bg" data-hotspots data-tilt-area>
          <div class="glow o" style="width:300px;height:300px;left:50%;top:50%;margin:-150px 0 0 -150px;opacity:.4"></div>
          <div class="dev-wrap"><div data-tilt style="transition:transform .3s var(--ease-out);position:relative">{device("3.480", cycle="3.480,4.625,2.715,11.200,7.600")}{hot_html}</div></div>
          <div class="hcap glass"><p class="t">Laser aperture</p><p>Point at the wall. The reading targets the spot you see.</p></div>
        </div>
        <dl class="facts"><div><dt>Measurement</dt><dd>Laser distance, up to 50 m<br>{tbc("Accuracy TBC")}</dd></div><div><dt>Function</dt><dd>Aim, press, read: one-handed on site</dd></div><div><dt>Integration</dt><dd>Bluetooth link sends readings to the app</dd></div><div><dt>On site</dt><dd>Wall-by-wall capture as you walk the space</dd></div></dl>
        {btn("Explore the device", "/products/joyplan-device/", "ghost")}
      </article>
      <article class="panel prod-card rv">
        <div class="prod-top"><span class="tag">Product 02</span><span class="label">Software &middot; iOS &middot; Android &middot; Desktop</span></div>
        <h3 class="h-m">JoyPlan Design Software</h3>
        <div class="prod-vis" style="aspect-ratio:auto;border:0;background:none;padding:6px 0" data-dim-toggle>
          <div class="sw-shot" style="aspect-ratio:1506/1044"><div class="dimswap">{img("f2d", "d2", sizes="(max-width: 720px) 100vw, 600px")}{img("f3d", "d3", sizes="(max-width: 720px) 100vw, 600px")}</div><span class="mini-seg"><button type="button" data-dim="2d" aria-pressed="false">2D</button><button type="button" data-dim="3d" aria-pressed="true">3D</button></span></div>
        </div>
        <dl class="facts"><div><dt>Plan &rarr; 3D</dt><dd>Draw in 2D, view in immersive 3D instantly</dd></div><div><dt>Design</dt><dd>Hard surfaces, furniture, materials</dd></div><div><dt>Present</dt><dd>Rendered images and 720&deg; panoramas</dd></div><div><dt>Document</dt><dd>Drawings, area inventory, estimates, CAD</dd></div></dl>
        {btn("Explore the software", "/software/joyplan-software/", "ghost")}
      </article>
    </div>
  </div>
</section>'''

STAGES = [("Measure", "Laser readings flow to the app over Bluetooth."), ("Create", "The 2D floor plan builds wall by wall."),
          ("Design", "One tap turns the plan into a 3D interior."), ("Present", "Renders and 720&deg; views shared with the client.")]
rail = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-controls="st{i}" id="stb{i}"><i class="bar"></i><span class="n">0{i+1}</span><span class="t">{t}</span><span class="d">{d}</span></button>' for i, (t, d) in enumerate(STAGES))

WORKFLOW = f'''
<section class="sec carbon" aria-labelledby="wf-h">
  <div class="wrap">
    {head("How JoyPlan works", 'Your Entire Workflow. <span class="hl-box"><span class="hl">Connected.</span></span>', hid="wf-h")}
    <div class="wf rv" data-workflow>
      <div class="wf-rail" role="tablist" aria-label="Workflow stages">{rail}</div>
      <div class="wf-stage">
        <div class="wf-scene" id="st0" role="tabpanel" aria-labelledby="stb0">{fit("measure")}<span class="illus stagetag">Stage 01 &middot; on site</span></div>
        <div class="wf-scene" id="st1" role="tabpanel" aria-labelledby="stb1">{fit("f2d")}<span class="illus stagetag">Stage 02 &middot; 2D plan</span></div>
        <div class="wf-scene" id="st2" role="tabpanel" aria-labelledby="stb2">{fit("f3d")}<span class="illus stagetag">Stage 03 &middot; same plan, now 3D</span></div>
        <div class="wf-scene" id="st3" role="tabpanel" aria-labelledby="stb3">{fit("f720tour")}<span class="illus stagetag">Stage 04 &middot; present &amp; close</span></div>
      </div>
    </div>
  </div>
</section>'''

FEATS = [
    ("2D Floor Plans", "Draw walls, place doors and windows and handle complex structures, with laser readings dropping straight onto the right wall.", "As-built plans on the first site visit.", "plan"),
    ("3D Visualisation", "Your 2D plan is presented in immersive 3D automatically. Walk through it, orbit it, check proportions with the client.", "Showing clients the space before work begins.", "walk"),
    ("Drawings &amp; Elevations", "Generate professional drawings from the model. Elevation output to be confirmed with JoyPlan.", "Joinery, kitchen and wardrobe detailing.", "drawings"),
    ("720&deg; Panorama", "Publish rendered 720&deg; panoramas the client can look around in from their own phone.", "Remote presentations and approvals.", "pano"),
    ("CAD Export", "One-click export of a CAD drawing set, plus area inventories and estimate reports.", "Handing over to drafting or contractors.", "cad"),
    ("Furniture &amp; Materials", "Furnish rooms from a large model library and recolour any model with the material editor.", "Trying finishes live in front of the client.", "sofa"),
    ("AI-Assisted Design", "AI image generation and AI-assisted floor plan creation, as listed in the JoyPlan app.", "Fast mood options in early concepts.", "ai"),
    ("LiDAR Scanning", "On supported devices, capture a room with LiDAR scanning to create the 3D space.", "Quick capture of furnished rooms.", "lidar"),
    ("Share &amp; Sync", "Work continues across phone, tablet, laptop and desktop: measure on site, refine at the studio.", "Teams and site-to-studio handover.", "share"),
]
fx_btns = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}"><span>0{i+1}</span>{t}</button>' for i, (t, *_r) in enumerate(FEATS))


FX_IMG = {"plan": "f2d", "walk": "f3d", "drawings": "felev", "pano": "f720", "cad": "fcad",
          "sofa": "ffurn", "ai": "fai", "lidar": "flidar", "share": "fsync"}


def fx_screen(k):
    return fit(FX_IMG[k], sizes="(max-width: 720px) 100vw, 640px")


fx_scr = "".join(f'<div class="fx-scr" role="tabpanel">{fx_screen(k)}</div>' for (_t, _d, _u, k) in FEATS)
fx_text = "".join(f'<div class="fx-text fx-info"{" hidden" if i else ""}><p class="mono small" style="color:var(--orange)">0{i+1} / 09</p><h3 class="h-m">{t}</h3><p class="muted">{d}</p><div class="usebox"><p class="label">Use it for</p><p class="small">{u}</p></div>{btn("All features", "/features/", "ghost", sm=True)}</div>' for i, (t, d, u, k) in enumerate(FEATS))

EXPLORER = f'''
<section class="sec dark grid-bg" aria-labelledby="fx-h">
  <div class="wrap">
    {head("Software feature explorer", "Everything You Need to Design with Confidence.", "Pick a feature to see it in JoyPlan.", hid="fx-h")}
    <div class="fx rv" data-explorer>
      <div><div class="fx-list" role="tablist" aria-label="Software features">{fx_btns}</div><p class="tiny" style="margin-top:16px">AR perspective will be added once JoyPlan confirms support.</p></div>
      <div class="fx-shot" style="aspect-ratio:1672/941">{fx_scr}</div>
      <div>{fx_text}</div>
    </div>
  </div>
</section>'''

PROS = [("Interior Designers", "Measure, lay out and present in the same visit.", ["Laser-linked site measurement", "Layouts with furniture &amp; materials", "Renders and 720&deg; for client sign-off"], "fai", "Designed in JoyPlan", "interior-designers"),
        ("Architects", "Accurate as-built plans, across every level.", ["Multi-level floor plans", "Sunlight analysis", "CAD export for the drawing set"], "villa", "3D cutaway in JoyPlan", "architects"),
        ("Civil Engineers", "On-site measurement straight into drawings.", ["Photo notes and annotations", "Area inventory for quantities", "Professional drawings to share"], "measure", "On-site measuring", "civil-engineers"),
        ("Modular Kitchen &amp; Furniture", "Wall-accurate layouts your customer can see.", ["Measured walls for modules", "3D kitchen and wardrobe views", "Estimates generated from the design"], "felev", "Joinery elevations in JoyPlan", "modular-kitchen")]
pro_cards = "".join(f'''<a class="pro rv" href="/solutions/#{slug}"><div class="pro-vis">{fit(v, alt="", sizes="(max-width: 720px) 100vw, 320px")}<span class="illus">{lab}</span></div><div class="pro-b"><span class="n">0{i+1}</span><h3 class="h-s">{t}</h3><p class="small" style="color:var(--text-dark)">{d}</p><ul>{"".join(f"<li>{b}</li>" for b in bs)}</ul><span class="tlink">Explore{ARR}</span></div></a>''' for i, (t, d, bs, v, lab, slug) in enumerate(PROS))

SOLUTIONS = f'''
<section class="sec bone" aria-labelledby="pro-h">
  <div class="wrap">
    <div class="head split"><div style="display:grid;gap:24px"><span class="kicker">Solutions by profession</span><h2 class="h-l" id="pro-h">Built for the People Who Build Spaces.</h2></div><div>{btn("All solutions", "/solutions/", "darkb")}</div></div>
    <div class="g4" data-stagger>{pro_cards}</div>
  </div>
</section>'''

PRICING = f'''
<section class="sec dark" id="pricing" aria-labelledby="pr-h" data-pricing>
  <div class="glow o" style="width:600px;height:600px;left:30%;bottom:-300px;opacity:.18"></div>
  <div class="wrap">
    <div class="head" style="margin-bottom:32px"><span class="kicker">Packages &amp; pricing</span><h2 class="h-l" id="pr-h">Find Your Perfect JoyPlan Package.</h2></div>
    <div class="price-head"><div style="display:grid;gap:10px"><span class="label">Subscription length</span>{seg()}</div></div>
    {pricing_cards()}
    <div class="price-head" style="margin:28px 0 0;align-items:center"><p class="tiny" style="max-width:520px">INR, per JoyPlan India's shared price list. Current prices, GST and inclusions to be confirmed before launch.</p><div class="btns"><button class="btn ghost sm" type="button" data-toggle="cmp-inline">Compare packages</button>{btn("Packages page", "/packages/", "ghost", sm=True)}</div></div>
    <div id="cmp-inline" class="on-bone bone" hidden style="margin-top:24px;padding:24px;border-radius:4px">{cmp_table()}</div>
  </div>
</section>'''

GALLERY_ITEMS = [
    ("Warm contemporary living room", "Interior &middot; Render", "rnd", "fai"),
    ("3BHK apartment in 3D", "Interior &middot; 3D", "3d", "f3d"),
    ("3BHK floor plan with areas", "Floor plan", "plan", "f2d"),
    ("Living &amp; dining 720&deg; tour", "720&deg; panorama", "pano rnd", "f720tour"),
    ("Living room render", "Interior &middot; Render", "rnd", "living"),
    ("Bedroom elevations", "Drawings &middot; Elevation", "plan", "felev"),
    ("Furniture &amp; material options", "Interior &middot; Design", "rnd", "ffurn"),
    ("White model to render", "Interior &middot; Render", "rnd", "whiterender"),
    ("Living room 720&deg; view", "720&deg; panorama", "pano rnd", "f720"),
    ("Villa cutaway", "Residential &middot; 3D", "3d", "villa"),
    ("Reading corner", "Interior &middot; Render", "rnd", "armchair"),
    ("LiDAR room scan", "Scan &middot; 3D", "3d", "flidar"),
]
gal_tiles = "".join(f'<button type="button" class="gt" data-f="{f}"><div class="im">{im}</div><div class="cap"><div><b>{t}</b><i>{c}</i></div><span aria-hidden="true">&#8599;</span></div></button>' for t, c, f, k in GALLERY_ITEMS for im in [img(k, sizes="(max-width: 720px) 100vw, 420px")])
filters = [("all", "All"), ("rnd", "Renders"), ("3d", "3D views"), ("plan", "Plans &amp; drawings"), ("pano", "720&deg;")]
fchips = "".join(f'<button type="button" class="chip" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>' for k, v in filters)

GALLERY = f'''
<section class="sec carbon" aria-labelledby="gal-h">
  <div class="wrap">
    {head("Project gallery", "Imagine What You Can Create.", "Interior renders, 3D views and floor plans made with JoyPlan. Tap any project to see it larger.", hid="gal-h")}
    <div class="chips rv" role="group" aria-label="Filter projects" style="margin-bottom:28px">{fchips}</div>
    <div class="gal" data-gallery>{gal_tiles}</div>
  </div>
</section>
<div class="lb" id="lightbox" role="dialog" aria-modal="true" aria-label="Project preview" aria-hidden="true">
  <button class="lb-x" type="button" aria-label="Close preview">&times;</button>
  <div class="lb-in"><div class="im"></div><div class="lb-foot"><div><p class="h-s lb-t"></p><p class="label lb-c" style="margin-top:6px"></p></div>{btn("Design like this: book a demo", "/book-a-demo/")}</div></div>
</div>'''

BENS = [("Faster workflows", "Measuring and drawing happen in one pass, so the plan exists before you leave the site."),
        ("Better visualisation", "Plans become 3D, renders and 720&deg; views without redrawing in another tool."),
        ("Professional presentations", "Clients see a finished-looking design early, not a sketch and a promise."),
        ("Connected process", "Device, phone, tablet and desktop work on the same project."),
        ("Clearer communication", "Photo notes, drawings, area inventories and estimates come from one source of truth.")]
ben_rows = "".join(f'<div class="ben-row"><span class="n">0{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(BENS))

BENEFITS = f'''
<section class="sec bone" aria-labelledby="ben-h">
  <div class="wrap">
    {head("Benefits", "More Than a Measuring Device. A Better Way to Work.", hid="ben-h")}
    <div class="ben">{ben_rows}</div>
  </div>
</section>'''

TRUST = f'''
<section class="sec dark tight" aria-labelledby="tst-h">
  <div class="wrap">
    <div class="price-head"><div style="display:grid;gap:14px"><span class="kicker">Trusted on site</span><h2 class="h-m" id="tst-h">What professionals say</h2></div>{tbc("Testimonials to be collected with written consent")}</div>
    <div class="g3" data-stagger>
      <figure class="panel quote rv" style="margin:0"><span class="q" aria-hidden="true">&ldquo;</span><blockquote style="margin:0"><p>[Testimonial from an interior designer: quote to be supplied]</p></blockquote><figcaption class="who"><span class="av">?</span><span><b>[Name]</b><span class="tiny">Interior designer &middot; [City]</span></span></figcaption></figure>
      <figure class="panel quote rv" style="margin:0"><span class="q" aria-hidden="true">&ldquo;</span><blockquote style="margin:0"><p>[Testimonial from an architect: quote to be supplied]</p></blockquote><figcaption class="who"><span class="av">?</span><span><b>[Name]</b><span class="tiny">Architect &middot; [Firm, City]</span></span></figcaption></figure>
      <figure class="panel quote rv" style="margin:0"><span class="q" aria-hidden="true">&ldquo;</span><blockquote style="margin:0"><p>[Testimonial from a modular kitchen business: quote to be supplied]</p></blockquote><figcaption class="who"><span class="av">?</span><span><b>[Name]</b><span class="tiny">Kitchen studio &middot; [City]</span></span></figcaption></figure>
    </div>
    <div class="trust rv"><div><span class="label">Available on</span><b>App Store &middot; Google Play</b></div><div><span class="label">Head office</span><b>Bengaluru, Karnataka</b></div><div><span class="label">Branch</span><b>Kozhikode, Kerala</b></div><div><span class="label">Learning</span><b>Short how-to video library</b></div></div>
  </div>
</section>'''

FORM = f'''
<section class="conv" id="form" aria-labelledby="cv-h">
  <div class="conv-l">
    <svg class="plan-deco" viewBox="0 0 600 420" aria-hidden="true"><path d="M20 20H580V400H20Z M260 20V160 M260 210V250 M400 20V110 M400 160V300 M400 350V400 M20 250H90 M140 250H300 M350 250H580" fill="none" stroke="#0B0B0B" stroke-width="8"/></svg>
    <div class="in rv">
      <span class="kick">Free &middot; live &middot; no obligation</span>
      <h2 class="h-l" id="cv-h">Your Next Project Deserves a Smarter Workflow.</h2>
      <p style="font-size:17px;max-width:460px">Discover how JoyPlan can transform the way you measure, design and present your projects.</p>
      <div class="btns">{btn("Book a Free Demo", "#enquiry", "darkb")}<a class="btn ghost ink" href="#" data-wa="{WA}">Talk to a JoyPlan Expert</a></div>
    </div>
  </div>
  <div class="conv-r">
    <div class="in">
      <form class="form" id="enquiry" action="/lead.php" method="post" data-lead data-thanks="enq-thanks" novalidate>
        <input type="hidden" name="form" value="enquiry"><input type="hidden" name="nearest_team" value=""><input type="hidden" name="consent" value="yes">
        <div class="hp" aria-hidden="true"><label>Website<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
        <div class="field"><label for="e-name">Full name</label><input id="e-name" name="full_name" autocomplete="name" required><span class="err">Please enter your name.</span></div>
        <div class="field"><label for="e-mob">Mobile number</label><input id="e-mob" name="mobile" type="tel" inputmode="tel" placeholder="+91" autocomplete="tel" required><span class="err">Enter a 10-digit Indian mobile number.</span></div>
        <div class="field"><label for="e-pro">Profession</label><select id="e-pro" name="profession" required><option value="">Select&hellip;</option><option>Interior designer</option><option>Architect</option><option>Civil engineer</option><option>Modular kitchen / furniture</option><option>Other</option></select><span class="err">Please choose your profession.</span></div>
        <div class="field"><label for="e-city">City</label><input id="e-city" name="city" placeholder="e.g. Bengaluru" autocomplete="address-level2" required><span class="err">Please enter your city.</span></div>
        <div class="field full"><label for="e-prod">Interested product</label><select id="e-prod" name="product"><option>Device + Software (Professional)</option><option>Software only (Starter)</option><option>Device only</option><option>Business / studio package</option></select></div>
        <div class="field full"><label for="e-msg">Message (optional)</label><textarea id="e-msg" name="message"></textarea></div>
        <div class="form-actions full"><button class="btn primary" type="submit">Book my free demo{ARR}</button><a class="btn wa" href="#" data-wa="{WA}">Or enquire on WhatsApp</a></div>
        <p class="form-msg full" role="alert"></p>
        <p class="tiny full">No spam. We use these details only to arrange your demo. <a href="/privacy/" style="text-decoration:underline">Privacy</a></p>
      </form>
      <div class="thanks" id="enq-thanks" role="status">
        <span class="kicker">Request received</span>
        <h3 class="h-m">Thank you, <span data-first></span>. Your demo request is in.</h3>
        <p class="muted">A JoyPlan specialist from the <span data-sum="nearest_team"></span> will call you to fix a time. Prefer to talk now? Message us on WhatsApp.</p>
        <div class="btns"><a class="btn primary" href="#" data-wa="{WA}">Continue on WhatsApp</a><button class="btn ghost" type="button" data-reset="enquiry">Send another enquiry</button></div>
      </div>
    </div>
  </div>
</section>'''

PAGES = [{
    "path": "/", "active": None,
    "title": "Laser Measuring Device &amp; Interior Design Software | JoyPlan India",
    "desc": "Measure rooms with the JoyPlan device, draw 2D plans, design in 3D and present renders and 720&deg; panoramas: one connected workflow for Indian design professionals.",
    "ld": [{"@context": "https://schema.org", "@type": "WebSite", "name": "JoyPlan India", "url": "https://joyplanindia.com/"}],
    "body": HERO + TRANSFORM + ECO + WORKFLOW + EXPLORER + SOLUTIONS + PRICING + GALLERY + BENEFITS + TRUST + FORM,
}]
