from components import ARR, btn, img
from shared import band

CR = [("Home", "/"), ("Solutions", "/solutions/")]
WA = "Hi JoyPlan India, I'd like to see how JoyPlan fits my work."

P = [
    ("interior-designers", "Interior Designers", "Measure, design and win the client, in one visit.",
     "Turn the first site visit into a presentation. Measure with the device, lay out the space, try finishes live and send renders before the competition has sent a quote.",
     ["Laser-linked measurement straight into the plan", "Furniture library and material editor for live options", "Renders and 720&deg; panoramas for faster approvals"],
     [("2BHK makeover", "Measure, propose two layouts and render both in the same week."), ("Client meeting", "Recolour the sofa and swap the flooring while the client watches."), ("Quote on the spot", "Area inventory and estimates generated from the design.")],
     "Book an interior designer demo", "living", "Rendered in JoyPlan", "Interior designer"),
    ("architects", "Architects", "Accurate as-builts. Multi-level. Sun-aware.",
     "Capture existing conditions quickly, build multi-level plans and test daylight before you commit to the drawing set.",
     ["Multi-level floor plans for houses and villas", "Sunlight analysis inside and around the building", "CAD export into your drafting workflow"],
     [("Renovation survey", "Document an existing villa floor by floor with photo notes."), ("Daylight check", "Simulate sun position for a west-facing living room."), ("Hand-off", "Export the CAD set for detailed drawings.")],
     "Book an architect demo", "villa", "3D cutaway in JoyPlan", "Architect"),
    ("civil-engineers", "Civil Engineers", "From site measurement to drawings, without the notebook.",
     "Record measurements, site photos and annotations in one place, then share professional drawings and area schedules with the team.",
     ["Photo notes and annotations pinned to the plan", "Area inventory for quantity estimation", "Shared across phone, tablet and desktop"],
     [("Site inspection", "Log conditions with photos attached to exact locations."), ("Quantities", "Pull room areas for flooring and plastering estimates."), ("Team handover", "The office team opens the same project on desktop.")],
     "Book an engineer demo", "site", "On-site measuring with the JoyPlan laser", "Civil engineer"),
    ("modular-kitchen", "Modular Kitchen Professionals", "Wall-accurate kitchens your customer can see.",
     "Measure each wall precisely, plan modules against real dimensions and show the customer their kitchen in 3D before production.",
     ["Exact wall lengths for module planning", "3D views and renders of the finished kitchen", "Estimates generated from the design"],
     [("Showroom to site", "Visit, measure and share a 3D kitchen the same day."), ("Finish selection", "Try shutter colours and countertops in the material editor."), ("Production check", "Drawings with dimensions for the factory.")],
     "Book a kitchen-studio demo", "furnlib", "Kitchen and furniture library in the JoyPlan app", "Modular kitchen"),
    ("furniture-designers", "Furniture Designers", "Custom furniture that fits the first time.",
     "Measure the niche, design the wardrobe or unit around it and present it in the room it will live in.",
     ["Freeform modelling for custom pieces", "Place designs in the client's measured room", "Rendered images for approval"],
     [("Fitted wardrobe", "Measure the wall, design the internals, render it in place."), ("TV unit", "Check proportions against the real living room."), ("Retail display", "Plan fixtures for a commercial fit-out.")],
     "Book a furniture-designer demo", "armchair", "Furniture rendered in JoyPlan", "Furniture designer"),
]

jump = "".join(f'<a href="#{s}"><span class="label" style="color:var(--orange)">0{i+1}</span><b>{n}</b><span class="tlink">Jump{ARR}</span></a>' for i, (s, n, *_r) in enumerate(P))
tabs = "".join(f'<a href="#{s}"{" class=on" if i == 0 else ""}><span>0{i+1}</span>{n}</a>' for i, (s, n, *_r) in enumerate(P))


def sec(i, p):
    s, n, h2, intro, bens, cases, cta, v, lab, prof = p
    tone = "dark" if i % 2 == 0 else "bone"
    rev = " rev" if i % 2 else ""
    bg = "#121212"
    ul = "".join(f"<li>{b}</li>" for b in bens)
    cs = "".join(f'<article class="panel case rv"><span class="label">Use case</span><b>{t}</b><p>{d}</p></article>' for t, d in cases)
    return f'''<section class="sec {tone}" id="{s}" aria-labelledby="{s}-h"><div class="wrap">
<div class="split{rev}"><div class="rv"><span class="kicker">0{i+1} &middot; {n}</span><h2 class="h-l" id="{s}-h" style="margin:20px 0">{h2}</h2><p class="lead">{intro}</p><ul class="ticks">{ul}</ul><div class="btns">{btn(cta, "/book-a-demo/?profession=" + prof.replace(" ", "+"))}{btn("See packages", "/packages/", "ghost", False)}</div></div>
<div class="vis-box photo rv" style="background:{bg}">{img(v, alt="")}<span class="illus">{lab}</span></div></div>
<div class="g3 cases" data-stagger>{cs}</div></div></section>'''


BODY = f'''
<section class="hero dark grid-bg" aria-labelledby="h1" style="min-height:0;padding-bottom:72px">
  <div class="glow o" style="width:600px;height:600px;left:-200px;top:-200px" data-parallax="60"></div>
  <div class="wrap">
    <div class="hero-copy" data-enter>
      {{{{CRUMBS}}}}
      <span class="kicker">Solutions by profession</span>
      <h1 class="h-xl" id="h1">Built for the people who <span class="hl-box"><span class="hl">build spaces.</span></span></h1>
      <p class="lead">Five professions, one connected workflow. Jump to yours.</p>
    </div>
    <nav class="jump rv" aria-label="Professions">{jump}</nav>
  </div>
</section>
<nav class="ptabs" aria-label="Profession sections"><div class="wrap">{tabs}</div></nav>
{"".join(sec(i, p) for i, p in enumerate(P))}
{band("Show us your workflow. We'll show you JoyPlan in it.", "WhatsApp an expert", "#", True, WA)}
'''

PAGES = [{"path": "/solutions/", "active": "/solutions/", "crumbs": CR, "wa": WA,
          "title": "JoyPlan Solutions for Design &amp; Construction Professionals",
          "desc": "How interior designers, architects, civil engineers, kitchen and furniture businesses use JoyPlan to measure, design and present.",
          "ld": [], "body": BODY}]
