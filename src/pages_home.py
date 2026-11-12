from components import ARR, WA_ICON, btn, tlink, tbc, device, tablet, img
from shared import head, seg, pricing_cards, cmp_table, inr

WA = "Hi JoyPlan India, I'd like to book a demo."

HERO = f'''
<section class="hero dark grid-bg" aria-labelledby="h1">
  <div class="glow o" style="width:620px;height:620px;right:-160px;top:-120px" data-parallax="70"></div>
  <div class="glow y" style="width:420px;height:420px;right:22%;bottom:-220px" data-parallax="-60"></div>
  <div class="wrap hero-grid">
    <div class="hero-copy" data-enter data-parallax-copy>
      <span class="kicker">Laser measurement &times; 2D/3D design software</span>
      <h1 class="h-xl" id="h1">Measure Smarter.<br>Design Faster.<br><span class="hl-box"><span class="hl">Impress</span></span><br><span class="hl-box"><span class="hl">Better.</span></span></h1>
      <p class="lead">Transform the way you measure, plan and present spaces with JoyPlan's connected measurement and design ecosystem.</p>
      <div class="btns">{btn("Experience JoyPlan", "#ecosystem")}{btn("Book a Free Demo", "/book-a-demo/", "ghost", False)}</div>
      <p class="hero-meta"><span>App Store</span><span>Google Play</span><span>Bengaluru</span><span>Kozhikode</span><span>Free business demo</span></p>
    </div>
    <div class="hero-vis hv-photo" data-parallax-vis>
      <figure class="hv-main">{img("living", lazy=False)}<figcaption class="illus">Rendered in JoyPlan</figcaption></figure>
      <div class="glass readout float" style="position:absolute;left:0;top:14%"><p class="t">Living &middot; Wall A</p><p class="v">4.625<small>m</small></p><p class="s">&#9679; Sent to plan</p></div>
      <div class="tab float d2 hv-tab"><div class="tab-scr"><div class="tab-bar"><span class="fn">Apartment_3BHK.jp</span><span style="color:var(--signal)">&#9679; LIVE</span></div><div class="canvas lite">{img("appplan", alt="")}</div></div></div>
      <div class="hv-dev"><div class="float d3">{device("4.625")}</div></div>
      <div class="glass readout float d3" style="position:absolute;right:0;bottom:12%"><p class="t">Area inventory</p><p class="v">86.4<small>m&sup2;</small></p><div style="display:flex;gap:4px;margin-top:8px"><i style="height:3px;width:34px;background:var(--signal)"></i><i style="height:3px;width:24px;background:var(--amber)"></i><i style="height:3px;width:20px;background:var(--yellow)"></i><i style="height:3px;width:16px;background:#444"></i></div></div>
    </div>
  </div>
</section>
<div class="strip" aria-hidden="true"><div class="strip-in">{"".join(f"<span>{w}</span>" for w in ["Measure", "Create", "Design", "Present", "2D floor plans", "3D design", "Renders", "720&deg; panorama", "CAD export", "Bengaluru", "Kozhikode"] * 2)}</div></div>
'''

TRANSFORM = f'''
<section class="sec bone" aria-labelledby="tr-h">
  <div class="wrap">
    {head("The transformation", "From Measurements to Meaningful Designs.", "Drag the line. On the left, the way most site visits still end: tape, paper, a second trip. On the right, the same room, measured once and already a plan.", hid="tr-h")}
    <div class="ba rv">
      <div class="ba-l">
        <svg viewBox="0 0 1000 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs><pattern id="gp" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="#d8cdb8" stroke-width="1"/></pattern></defs><rect width="1000" height="500" fill="#efe6d4"/><rect width="1000" height="500" fill="url(#gp)"/>
        <path d="M200 90L640 96L636 420L204 414Z M380 92L384 230 M384 262L386 300 M206 300L290 302 M330 302L520 304" fill="none" stroke="#2b2b2b" stroke-width="4" stroke-linecap="round"/>
        <text x="400" y="70" font-family="Georgia,serif" font-style="italic" font-size="28" fill="#333">11.2 m?</text>
        <text x="160" y="270" font-family="Georgia,serif" font-style="italic" font-size="24" fill="#333" transform="rotate(-90 160 260)">7.6</text>
        <text x="470" y="200" font-family="Georgia,serif" font-style="italic" font-size="22" fill="#a33" text-decoration="line-through">kit 3.4</text><text x="470" y="228" font-family="Georgia,serif" font-style="italic" font-size="22" fill="#c2410c">3.48 &#215;</text>
        <text x="300" y="380" font-family="Georgia,serif" font-style="italic" font-size="22" fill="#333">4.6 x 3.9</text>
        <g transform="translate(720 120) rotate(4)"><rect width="200" height="150" fill="#FFE27A"/><text x="16" y="44" font-family="Georgia,serif" font-style="italic" font-size="21" fill="#5a4600">re-measure</text><text x="16" y="74" font-family="Georgia,serif" font-style="italic" font-size="21" fill="#5a4600">kitchen wall +</text><text x="16" y="104" font-family="Georgia,serif" font-style="italic" font-size="21" fill="#5a4600">redraw in CAD</text></g>
        <g transform="translate(120 400) rotate(-20)"><rect x="0" y="0" width="120" height="110" rx="18" fill="#F9A21B"/><circle cx="60" cy="55" r="26" fill="#2b2b2b"/><rect x="118" y="34" width="230" height="30" fill="#FFC20E"/><g stroke="#2b2b2b" stroke-width="2">{"".join(f'<path d="M{130+i*14} 34V{46 if i % 2 else 52}"/>' for i in range(16))}</g></g>
        </svg>
        <div class="tags l"><span class="tag" style="background:#fff">Traditional</span><span class="tag" style="background:#fff">Tape &middot; paper &middot; second visit</span></div>
      </div>
      <div class="ba-r">
        <div class="ba-real">{img("appplan", "ba-plan", alt="The same apartment as a dimensioned floor plan in the JoyPlan app")}<figure class="ba-inset">{img("apt3d", alt="")}<figcaption class="label">3D preview</figcaption></figure></div>
        <div class="tags r"><span class="tag" style="background:#0B0B0B">JoyPlan</span><span class="tag o" style="background:var(--signal);color:var(--ink)">Measured once &middot; plan + 3D on site</span></div>
      </div>
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

HOTS = [("Laser aperture", "Point at the wall. The reading targets the spot you see.", "calc(50% - 6px)", "-2%"),
        ("Built-in levels", "Two bubble levels help you hold the device straight for a true reading.", "calc(100% + 10px)", "27%"),
        ("Live readout", "Distance shown on the device and in the app at the same time.", "-24px", "36%"),
        ("Bluetooth to app", "The 50 m model carries a Bluetooth mark and pairs with the JoyPlan app, so readings land on the plan.", "calc(100% + 10px)", "56%"),
        ("One-press READ key", "The red READ key takes the reading. Accuracy and battery specs to be confirmed.", "-24px", "65%")]
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
          {tablet("Apartment_3BHK.jp", '<span class="mini-seg"><button type="button" data-dim="2d" aria-pressed="false">2D</button><button type="button" data-dim="3d" aria-pressed="true">3D</button></span>', '<div class="dimswap">' + img("appplan", "d2") + img("app3d", "d3") + '</div>')}
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
        <div class="wf-scene" id="st0" role="tabpanel" aria-labelledby="stb0"><div class="duo">{img("site", "bg", alt="")}{img("site")}</div>
          <div class="glass readout st0-read"><p class="t">Bluetooth &middot; connected</p><p class="v">4.625<small>m</small></p><p class="s">&rarr; Wall A &middot; Living</p></div>
          <span class="illus stagetag">Stage 01 &middot; on site</span></div>
        <div class="wf-scene lite" id="st1" role="tabpanel" aria-labelledby="stb1">{img("appplan", "contain")}<span class="illus stagetag">Stage 02 &middot; 2D plan generated</span></div>
        <div class="wf-scene" id="st2" role="tabpanel" aria-labelledby="stb2" style="background:#151515">{img("apt3d", "contain")}
          <div class="glass" style="position:absolute;right:4%;top:6%"><p class="label">Materials</p><div style="display:flex;gap:6px;margin-top:8px"><i style="width:26px;height:18px;background:#d9cfc0"></i><i style="width:26px;height:18px;background:#8a5a3a"></i><i style="width:26px;height:18px;background:#4b5058"></i><i style="width:26px;height:18px;background:var(--signal)"></i></div></div>
          <span class="illus stagetag">Stage 03 &middot; same plan, now 3D</span></div>
        <div class="wf-scene" id="st3" role="tabpanel" aria-labelledby="stb3" style="background:#151515">
          <div style="position:absolute;left:8%;top:12%;width:58%"><div class="tab" style="padding:8px;border-radius:16px"><div style="border-radius:10px;overflow:hidden;aspect-ratio:16/10">{img("render", alt="", style="width:100%;height:100%;object-fit:cover")}</div></div></div>
          <div class="glass" style="position:absolute;right:5%;top:18%;max-width:40%"><p class="label">Shared with client</p><p style="font-weight:600;margin-top:6px;font-size:14px">Render + 720&deg; link</p></div>
          <div class="glass" style="position:absolute;right:8%;bottom:20%;max-width:40%"><p class="label">Client</p><p style="font-weight:600;margin-top:6px;font-size:14px;display:flex;gap:8px;align-items:center"><span style="color:var(--signal)">&#10003;</span> Design approved</p></div>
          <span class="illus stagetag">Stage 04 &middot; present &amp; close</span></div>
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


FX_IMG = {"plan": ("appplan", "contain lite"), "walk": ("app3d", "contain"), "drawings": ("plan2d", "contain"), "pano": ("render", "cover"), "cad": ("cad", "contain lite"),
          "sofa": ("material", "cover"), "ai": ("lounge", "cover"), "lidar": ("lidar", "cover"), "share": ("share", "contain lite")}


def fx_screen(k):
    key, c = FX_IMG[k]
    badge = '<span class="illus" style="position:absolute;right:10px;top:10px">720&deg; view</span>' if k == "pano" else ""
    return img(key, c) + badge


fx_scr = "".join(f'<div class="fx-scr{" lite" if "lite" in FX_IMG[k][1] else ""}" role="tabpanel">{fx_screen(k)}</div>' for (_t, _d, _u, k) in FEATS)
fx_text = "".join(f'<div class="fx-text fx-info"{" hidden" if i else ""}><p class="mono small" style="color:var(--orange)">0{i+1} / 09</p><h3 class="h-m">{t}</h3><p class="muted">{d}</p><div class="usebox"><p class="label">Use it for</p><p class="small">{u}</p></div>{btn("All features", "/features/", "ghost", sm=True)}</div>' for i, (t, d, u, k) in enumerate(FEATS))

EXPLORER = f'''
<section class="sec dark grid-bg" aria-labelledby="fx-h">
  <div class="wrap">
    {head("Software feature explorer", "Everything You Need to Design with Confidence.", "Pick a feature and the tablet switches to that tool.", hid="fx-h")}
    <div class="fx rv" data-explorer>
      <div><div class="fx-list" role="tablist" aria-label="Software features">{fx_btns}</div><p class="tiny" style="margin-top:16px">AR perspective will be added once JoyPlan confirms support.</p></div>
      <div class="tab"><div class="tab-scr"><div class="tab-bar"><span class="fn">Apartment_3BHK.jp</span><span class="mono">JoyPlan</span></div><div class="tab-body"><div class="rail"><span class="on"></span><span></span><span></span><span></span><span></span></div><div class="canvas">{fx_scr}</div></div></div></div>
      <div>{fx_text}</div>
    </div>
  </div>
</section>'''

PROS = [("Interior Designers", "Measure, lay out and present in the same visit.", ["Laser-linked site measurement", "Layouts with furniture &amp; materials", "Renders and 720&deg; for client sign-off"], "living", "Rendered in JoyPlan", "interior-designers"),
        ("Architects", "Accurate as-built plans, across every level.", ["Multi-level floor plans", "Sunlight analysis", "CAD export for the drawing set"], "villa", "3D cutaway in JoyPlan", "architects"),
        ("Civil Engineers", "On-site measurement straight into drawings.", ["Photo notes and annotations", "Area inventory for quantities", "Professional drawings to share"], "site", "On-site measuring", "civil-engineers"),
        ("Modular Kitchen &amp; Furniture", "Wall-accurate layouts your customer can see.", ["Measured walls for modules", "3D kitchen and wardrobe views", "Estimates generated from the design"], "furnlib", "JoyPlan furniture &amp; kitchen library", "modular-kitchen")]
pro_cards = "".join(f'''<a class="pro rv" href="/solutions/#{slug}"><div class="pro-vis">{img(v, alt="")}<span class="illus">{lab}</span></div><div class="pro-b"><span class="n">0{i+1}</span><h3 class="h-s">{t}</h3><p class="small" style="color:var(--text-dark)">{d}</p><ul>{"".join(f"<li>{b}</li>" for b in bs)}</ul><span class="tlink">Explore{ARR}</span></div></a>''' for i, (t, d, bs, v, lab, slug) in enumerate(PROS))

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
    ("Living room render", "Interior &middot; Render", "rnd", "living"),
    ("3BHK apartment in 3D", "Interior &middot; 3D", "3d", "apt3d"),
    ("Apartment floor plan", "Floor plan", "plan", "appplan"),
    ("Reading corner", "Interior &middot; Render", "rnd", "armchair"),
    ("White model to render", "Interior &middot; Render", "rnd", "whiterender"),
    ("Furnished 3BHK plan", "Floor plan", "plan", "plan2d"),
    ("Lounge render", "Interior &middot; Render", "rnd", "lounge"),
    ("Villa cutaway", "Residential &middot; 3D", "3d", "villa"),
    ("Plan with finishes", "Floor plan", "plan", "appfinish"),
    ("Living room with sculptural lamps", "Interior &middot; Render", "rnd", "render"),
    ("Plan as a 3D model", "Interior &middot; 3D", "3d", "app3d"),
]
gal_tiles = "".join(f'<button type="button" class="gt" data-f="{f}"><div class="im">{im}</div><div class="cap"><div><b>{t}</b><i>{c}</i></div><span aria-hidden="true">&#8599;</span></div></button>' for t, c, f, k in GALLERY_ITEMS for im in [img(k)])
filters = [("all", "All"), ("rnd", "Renders"), ("3d", "3D views"), ("plan", "Floor plans")]
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
