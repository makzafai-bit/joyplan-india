from components import ARR, btn, tbc, device, img
from shared import head, band, faq, faq_ld

WA = "Hi JoyPlan India, I'd like a demo of the JoyPlan design software."
CR = [("Home", "/"), ("Software", "/software/joyplan-software/"), ("JoyPlan Software", "/software/joyplan-software/")]

FAQS = [("Which devices does JoyPlan run on?", "JoyPlan is available on the App Store and Google Play, and work can be shared across phone, tablet, laptop and desktop."),
        ("Do I need design experience?", "No. Short, searchable help videos cover each tool, and a free demo walks you through your own project."),
        ("Can I export to CAD?", "Yes. JoyPlan exports a CAD drawing set in one click, along with area inventories, professional drawings and estimate reports."),
        ("Does it support multi-storey buildings?", "Yes. Multi-level floor plans keep every floor of a duplex or villa in one aligned project."),
        ("How are renders and panoramas billed?", f"Rendering and AI credit details {tbc()}.")]

CALLS = [("Design modes", "Switch between 2D plan, 3D and render in one tap.", "50%", "6%"),
         ("Tool rail", "Walls, doors and windows, hard surfaces, furniture, annotations.", "4%", "36%"),
         ("Laser-linked wall", "The selected wall takes the next device reading.", "40%", "78%"),
         ("Properties panel", "Exact lengths, heights and materials for anything selected.", "86%", "30%"),
         ("Live area", "Room areas and perimeters update as you draw.", "30%", "64%")]
cnums = "".join(f'<span class="cnum{" on" if i == 0 else ""}" style="left:{x};top:{y}">{i+1}</span>' for i, (_t, _d, x, y) in enumerate(CALLS))
cbtns = "".join(f'<button type="button" aria-pressed="{"true" if i == 0 else "false"}"><span>{i+1}</span><b>{t}</b><em>{d}</em></button>' for i, (t, d, *_r) in enumerate(CALLS))
props = ('<p class="label" style="font-size:9px">Selected &middot; wall</p><div class="r"><span>Length</span><b>7.400 m</b></div><div class="r"><span>Height</span><b>2.850 m</b></div><div class="r"><span>Thickness</span><b>0.230 m</b></div>'
         '<p class="label" style="font-size:9px;margin-top:8px">Material</p><div class="sw"><i style="background:#EDE6DA"></i><i style="background:#C9A27A"></i><i style="background:#4b5058"></i><i style="background:#F26722"></i></div>'
         '<p class="label" style="font-size:9px;margin-top:8px">Room</p><div class="r"><span>Area</span><b>22.8 m&sup2;</b></div><div class="r"><span>Perimeter</span><b>19.6 m</b></div>')

STEPS = [("Draw", "Draw the plan", "Create your 2D floor plan and JoyPlan presents it in immersive 3D. Measure walls, place doors and windows, complex structures included.", "appplan"),
         ("Hard-surface", "Finish every surface", "Apply flooring, wall finishes and ceilings. Freeform modelling lets you shape the floor, ceiling and walls as you please.", "appfinish"),
         ("Furniture", "Furnish and recolour", "Place furniture from the model library and recolour anything in the material editor to match your design vision.", "furnlib"),
         ("View", "Walk through and present", "Walk through in 3D, render images and publish 720&deg; panoramas. Sunlight analysis shows how light falls through the day.", "render")]
st_tabs = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" style="text-align:left;padding:16px 0;border-top:2px solid var(--line)"><span class="label" style="color:var(--orange)">Step 0{i+1}</span><span class="h-s" style="display:block;margin-top:6px">{t}</span></button>' for i, (t, *_r) in enumerate(STEPS))
st_panels = "".join(f'<div role="tabpanel" class="split stp" style="margin-top:40px"><div><h3 class="h-m">{h}</h3><p class="muted" style="margin-top:14px;max-width:460px">{d}</p></div><div class="fvis"><div class="scr{" lite" if k.startswith("app") or k == "furnlib" else ""}">{img(k)}</div></div></div>' for (_t, h, d, k) in STEPS)

DOCS = [("CAD drawing set", "CAD", "One-click export of plans for your drafting workflow.", "cad"), ("Professional drawings", "PDF", "Clean, dimensioned drawings ready to share.", "plan2d"),
        ("Area inventory", "Report", "Room-by-room areas generated automatically.", "areas"), ("Estimate report", "Report", "Estimates produced from the design in one click.", "estimate"),
        ("Rendered images", "Image", "Photo-style renders of any view.", "render"), ("720&deg; panorama", "Link", "Immersive panoramas clients open on their phone.", "lounge")]
docs = "".join(f'<article class="panel lift rv"><div class="thumb{" lite" if k in ("cad", "areas", "estimate") else ""}" style="width:100%;padding:0;overflow:hidden">{img(k, alt="")}</div><div class="row"><b>{t}</b><span class="tag">{tg}</span></div><p>{d}</p></article>' for t, tg, d, k in DOCS)

BODY = f'''
<section class="hero center dark grid-bg" aria-labelledby="h1" style="min-height:0;padding-bottom:40px">
  <div class="glow o" style="width:700px;height:500px;left:50%;margin-left:-350px;top:-200px;opacity:.28"></div>
  <div class="wrap">
    <div class="hero-copy" data-enter>
      {{{{CRUMBS}}}}
      <span class="kicker">JoyPlan design software &middot; iOS &middot; Android &middot; desktop</span>
      <h1 class="h-xl" id="h1">Your whole design studio, <span class="hl-box"><span class="hl">in your pocket.</span></span></h1>
      <p class="lead">Draw 2D floor plans, see them in 3D, add hard surfaces, furniture and materials, render, and export professional documents: from the site, the car or the studio.</p>
      <div class="btns" style="justify-content:center">{btn("Book a Free Demo", "/book-a-demo/?package=starter")}{btn("Tour the interface", "#ui", "ghost", False)}</div>
    </div>
  </div>
</section>

<section class="sec dark" id="ui" aria-labelledby="ui-h" style="padding-top:40px">
  <div class="wrap">
    <h2 class="sr-only" id="ui-h">The JoyPlan interface</h2>
    <div class="split ui-split rv">
      <div style="position:relative" id="ui-mock">
        {"".join([])}<div class="tab"><div class="tab-scr"><div class="tab-bar"><span class="fn">Residence_Kozhikode.jp</span><span class="mini-seg"><span class="on">2D</span><span>3D</span><span>Render</span></span><span style="color:var(--mute)">&#9679; Synced</span></div><div class="tab-body props"><div class="rail"><span class="on"></span><span></span><span></span><span></span><span></span><span></span></div><div class="canvas lite">{img("appplan", alt="Dimensioned floor plan open in the JoyPlan app")}</div><div class="pp">{props}</div></div></div></div>
        {cnums}
        <span class="illus" style="position:absolute;right:14px;bottom:-34px">JoyPlan plan view &middot; panel values are sample data</span>
      </div>
      <div><p class="label" style="margin-bottom:12px">The interface &middot; tap a callout</p><div class="callouts" data-callouts="ui-mock">{cbtns}</div></div>
    </div>
  </div>
</section>

<section class="sec carbon" aria-labelledby="steps-h">
  <div class="wrap" data-tabs>
    <div class="head split"><div style="display:grid;gap:24px"><span class="kicker">Feature explorer</span><h2 class="h-l" id="steps-h">Four steps from empty room to finished design.</h2></div><div>{btn("See all features", "/features/", "ghost")}</div></div>
    <div role="tablist" aria-label="Design steps" style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px" class="steptabs">{st_tabs}</div>
    {st_panels}
  </div>
</section>

<section class="sec dark" aria-labelledby="t3-h">
  <div class="wrap split">
    <div class="rv">
      <span class="kicker">2D to 3D</span>
      <h2 class="h-l" id="t3-h" style="margin:20px 0">Drag your plan into the third dimension.</h2>
      <p class="lead">There's no export and no second program. The plan you drew is already a 3D model. Drag the slider to switch between them.</p>
      <div class="rangebox"><label class="label" for="tilt">2D plan &rarr; 3D model &middot; <span id="tilt-out">70%</span></label><input class="range" id="tilt" type="range" min="0" max="100" value="70" data-tilt-range="iso-try" data-out="tilt-out"><div class="lbls"><span>2D</span><span>3D</span></div></div>
    </div>
    <div class="vis-box rv" style="aspect-ratio:1/0.85;background:rgb(210,213,223)"><div class="dimswap" id="iso-try">{img("appplan", "d2")}{img("app3d", "d3")}</div></div>
  </div>
</section>

<section class="sec bone" aria-labelledby="wm-h">
  <div class="wrap">
    {head("Interior visualisation", "From white model to rendered image.", "The same room as a white model and as a finished render. Rendering runs from the app, with no separate visualiser.", cls="split", hid="wm-h")}
    <figure class="wm rv">{img("whiterender")}<div class="tags l"><span class="tag" style="background:#fff">White model</span></div><div class="tags r"><span class="tag o" style="background:var(--signal);color:var(--ink)">Rendered</span></div></figure>
  </div>
</section>

<section class="sec dark" aria-labelledby="doc-h">
  <div class="wrap">
    {head("CAD &amp; export", "One click. A full document set.", "Generate professional documents and estimate reports straight from the model.", cls="split", hid="doc-h")}
    <div class="g3 docs" data-stagger>{docs}</div>
  </div>
</section>

<section class="sec carbon" aria-labelledby="pano-h">
  <div class="wrap">
    {head("Panoramic presentation", "Let the client stand in the room.", "Panoramas your client explores on their own phone. Drag inside the phone to look around.", cls="split", hid="pano-h")}
    <div class="split pano-split rv">
      <div class="ph-pano" tabindex="0" role="img" aria-label="A rendered living room on a phone screen. Drag or use the arrow keys to look around."><div class="ph-scr"><div class="ph-in">{img("render", alt="")}</div><span class="ph-hint">&#8596; Drag to look around</span></div></div>
      <div><ul class="ticks"><li>Publish 720&deg; panoramas straight from the JoyPlan app</li><li>Share a link the client opens on their own phone</li><li>Approvals without a site visit or a studio meeting</li></ul></div>
    </div>
    <div class="addon rv"><span class="tag">AR perspective</span><span class="small" style="flex:1;min-width:200px">Space reserved for AR presentation once JoyPlan confirms it is supported in the India release.</span>{tbc("Support to be confirmed")}</div>
  </div>
</section>

<section class="sec dark" aria-labelledby="bd-h">
  <div class="wrap split">
    <div class="vis-box rv" style="aspect-ratio:5/3.6;display:flex;align-items:center;justify-content:center;gap:40px;background:#121212">
      <div style="transform:scale(.8)">{device("2.715")}</div>
      <div style="width:60px;height:2px;background:var(--signal);box-shadow:0 0 12px var(--signal)"></div>
      <div style="width:120px;height:210px;border-radius:26px;padding:8px;background:linear-gradient(150deg,#2a2a2a,#151515);box-shadow:inset 0 0 0 1px rgba(255,255,255,.08)"><div style="height:100%;border-radius:20px;background:#fff;overflow:hidden;display:flex;align-items:center">{img("appplan", alt="", style="width:100%")}</div></div>
    </div>
    <div class="rv">
      <span class="kicker">Device integration</span>
      <h2 class="h-l" id="bd-h" style="margin:20px 0">Better with the device.</h2>
      <p class="lead">Pair the JoyPlan measuring device and readings land on the selected wall. The app works on its own too; the device just removes the typing.</p>
      <div class="btns" style="margin-top:28px">{btn("Explore the device", "/products/joyplan-device/", "ghost")}</div>
    </div>
  </div>
</section>

<section class="sec bone" aria-labelledby="uc-h">
  <div class="wrap">
    {head("Professional use cases", "Where it earns its keep", hid="uc-h")}
    <div class="g3" data-stagger>
      <article class="panel case rv"><span class="label">On site</span><b>Measure and plan in one visit</b><p>Photo notes and annotations record the site condition alongside the plan.</p></article>
      <article class="panel case rv"><span class="label">In the meeting</span><b>Design live with the client</b><p>Swap materials and furniture while the client watches, then render.</p></article>
      <article class="panel case rv"><span class="label">After approval</span><b>Hand over clean documents</b><p>CAD drawings, area inventory and estimates for execution teams.</p></article>
    </div>
  </div>
</section>
{faq("FAQs", "Software questions", FAQS)}
{band("See your own project in JoyPlan.", "View packages", "/packages/", False)}
'''

PAGES = [{"path": "/software/joyplan-software/", "active": "/software/joyplan-software/", "crumbs": CR, "wa": WA,
          "title": "2D &amp; 3D Interior Design Software for Professionals | JoyPlan India",
          "desc": "Draw 2D floor plans, switch to 3D, add materials and furniture, render, export CAD and share 720&deg; panoramas from phone, tablet or desktop.",
          "ld": [faq_ld(FAQS), {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "JoyPlan", "operatingSystem": "iOS, Android", "applicationCategory": "DesignApplication"}],
          "body": BODY}]
