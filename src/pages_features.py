from components import fvis
from shared import band

CR = [("Home", "/"), ("Features", "/features/")]
WA = "Hi JoyPlan India, I'd like to see JoyPlan's features in a demo."

# (cat, slug, title, explanation, use case, benefit, visual key, real screenshot or None, file name)
F = [
    ("Measure", "laser-linked-measurement", "Laser-linked measurement", "Pair the JoyPlan device and each reading drops onto the selected wall in the plan.", "First site visit to a new apartment.", "No copying numbers from a notepad.", "laser", None, "Site_Visit.jp"),
    ("Measure", "lidar-scanning", "LiDAR scanning", "On supported devices, scan a room with LiDAR to create the 3D space.", "Furnished rooms where walls are hard to reach.", "Capture in moments, refine later.", "lidar", ("/assets/f_lidar.webp", "A room captured as a 3D scan in JoyPlan"), "Scan_Living.jp"),
    ("Measure", "photos-and-notes", "Photos &amp; notes", "Record house conditions with photos, notes and annotations pinned to the plan.", "Documenting cracks, sockets, plumbing points.", "Site memory that travels with the project.", "photos", None, "Site_Notes.jp"),
    ("Plan", "2d-floor-plans", "2D floor plans", "Draw walls, doors and windows; complex structures are no problem. JoyPlan shows it in 3D as you go.", "As-built plans and layout options.", "The plan exists before you leave the site.", "plan2d", None, "Apartment_3BHK.jp"),
    ("Plan", "multi-level", "Multi-level", "Create multi-level floor plans for duplexes and villas.", "Kerala villas, G+1 homes.", "One project, every floor aligned.", "multi", ("/assets/f_multi.webp", "Floor level controls for a two-storey plan in JoyPlan"), "Villa_G+1.jp"),
    ("Plan", "ai-assisted-floor-plans", "AI-assisted floor plans", "Create 2D/3D floor plans manually or with AI automation, as listed in the JoyPlan app.", "Quick concept layouts.", "A head start on early options.", "ai", None, "AI_Layout.jp"),
    ("Design", "hard-surface-design", "Hard-surface design", "Apply floors, wall finishes and ceilings room by room.", "Tile and flooring selections.", "Surfaces specified, not just sketched.", "hard", None, "Finishes.jp"),
    ("Design", "freeform-modelling", "Freeform modelling", "Create freeform shapes on the ground, ceiling and walls.", "False ceilings, curved partitions.", "Custom geometry without leaving the app.", "freeform", ("/assets/f_freeform.webp", "Freeform shape drawn on a plan with JoyPlan's drawing tools"), "Ceiling.jp"),
    ("Design", "furniture-library", "Furniture library", "Arrange furniture and decor models for interiors and exteriors.", "Living room and wardrobe layouts.", "Clients see real furniture, not boxes.", "furn", ("/assets/step3.webp", "Furniture library open beside a floor plan in JoyPlan"), "Living_Layout.jp"),
    ("Design", "material-editor", "Material editor", "Customise model colours and materials to match your design vision.", "Trying fabrics live with the client.", "Decisions made in the meeting.", "material", ("/assets/f_material.webp", "Material editor recolouring an armchair in JoyPlan"), "Material_Editor.jp"),
    ("Visualise", "3d-walkthrough", "3D walkthrough", "Walk through your 3D interior designs from any viewpoint.", "Client presentations.", "Spatial decisions without guesswork.", "walk", None, "Walkthrough.jp"),
    ("Visualise", "rendered-images", "Rendered images", "Produce rendered images of any view directly from the app.", "Proposals and social posts.", "Photo-style output without a separate visualiser.", "render", ("/assets/learn2.webp", "A rendered living room produced in JoyPlan"), "Render_01.jp"),
    ("Visualise", "720-panorama", "720&deg; panorama", "Publish immersive 720&deg; panoramas clients can explore themselves.", "Remote approvals.", "Clients &ldquo;stand in&rdquo; the design anywhere.", "pano", None, "Living_720.jp"),
    ("Visualise", "sunlight-analysis", "Sunlight analysis", "Simulate sunlight position and projection inside and around the space.", "Window placement, west-facing rooms.", "Design for Indian light and heat.", "sun", ("/assets/f_sun.webp", "Sunlight analysis dial over a 3D model in JoyPlan"), "Sun_Study.jp"),
    ("Document", "professional-drawings", "Professional drawings", "Generate professional drawings from the model in one click.", "Drawing sets for execution.", "Consistent drawings without redrafting.", "drawings", None, "Drawings.jp"),
    ("Document", "area-inventory", "Area inventory", "Room-by-room area schedules generated automatically.", "Flooring and paint quantities.", "Accurate quantities, instantly.", "area", ("/assets/make1.webp", "Room area and perimeter details listed in JoyPlan"), "Areas.jp"),
    ("Document", "estimates", "Estimates", "Export estimate reports with one click from the design.", "Quoting on the spot.", "From measurement to quotation, faster.", "estimate", ("/assets/make2.webp", "Estimate broken down by trade in JoyPlan"), "Estimate.jp"),
    ("Document", "cad-export", "CAD export", "One-click export of a full CAD drawing set (per app listing).", "Hand-off to drafting teams.", "Fits your existing CAD workflow.", "cad", ("/assets/make3.webp", "Files and sharing screen with CAD export options in JoyPlan"), "Export.jp"),
    ("Collaborate", "share-across-devices", "Share across devices", "Share work among phone, tablet, laptop and desktop.", "Site-to-studio handover.", "The whole team on one version.", "share", ("/assets/share.webp", "The same JoyPlan project open on phone, tablet and laptop"), "Shared.jp"),
    ("Collaborate", "learning-videos", "Learning videos", "Short, searchable help videos to learn design in no time.", "Onboarding new team members.", "Productive in days, not weeks.", "learn", None, "Learn.jp"),
]
CATS = ["Measure", "Plan", "Design", "Visualise", "Document", "Collaborate"]


def row(i, f):
    cat, slug, t, d, u, b, k, img, fn = f
    if img:
        v = f'<img src="{img[0]}" alt="{img[1]}" loading="lazy">'
        tag = "App screen"
    else:
        v = fvis(k)
        tag = "Illustrative"
    return (f'<article class="frow" id="{slug}" data-cat="{cat}"><div class="rv"><div style="display:flex;gap:10px;align-items:center"><span class="mono small" style="color:var(--orange)">{i+1:02d}</span><span class="tag">{cat}</span></div>'
            f'<h2>{t}</h2><p class="muted">{d}</p><div class="boxes"><div class="usebox"><p class="label">Use case</p><p>{u}</p></div><div class="usebox"><p class="label">Professional benefit</p><p>{b}</p></div></div></div>'
            f'<div class="fvis rv"><div class="bar"><span>{fn}</span><span>{tag}</span></div><div class="scr">{v}</div></div></article>')


rows = "".join(row(i, f) for i, f in enumerate(F))
stage = "".join(f'<button type="button" data-ffilter="{c}" aria-pressed="false"><span class="label">0{i+1} &middot; {sum(1 for x in F if x[0] == c)} tools</span><b>{c}</b></button>' for i, c in enumerate(CATS))
chips = '<button type="button" class="chip" data-ffilter="all" aria-pressed="true">All</button>' + "".join(f'<button type="button" class="chip" data-ffilter="{c}" aria-pressed="false">{c}</button>' for c in CATS)

BODY = f'''
<section class="hero dark grid-bg" aria-labelledby="h1" style="min-height:0;padding-bottom:72px">
  <div class="glow o" style="width:620px;height:620px;right:-200px;top:-260px" data-parallax="60"></div>
  <div class="wrap">
    <div class="hero-copy" data-enter>
      {{{{CRUMBS}}}}
      <span class="kicker">Feature library &middot; 20 tools</span>
      <h1 class="h-xl" id="h1" style="max-width:980px">Every tool between site visit and <span class="hl-box"><span class="hl">sign-off.</span></span></h1>
      <p class="lead">Filter by stage of your workflow. Every feature shows what it looks like, when you'd use it and what it saves you.</p>
    </div>
    <div class="stage-bar rv" role="group" aria-label="Jump to a workflow stage">{stage}</div>
  </div>
</section>
<div class="sticky-filter"><div class="wrap"><div class="chips" role="group" aria-label="Filter features">{chips}</div></div></div>
<section class="dark" aria-label="Feature list" data-flib style="padding-bottom:64px">
  <div class="wrap">{rows}
    <p class="tiny" style="margin-top:40px">Feature list compiled from joyplanindia.com and the JoyPlan app store listing. AR perspective is not listed and is held until JoyPlan confirms support. Screens marked illustrative will be replaced with real app captures.</p>
  </div>
</section>
{band("See every feature on your own floor plan.", "Compare packages", "/packages/", False)}
'''

PAGES = [{"path": "/features/", "active": "/features/", "crumbs": CR, "wa": WA,
          "title": "Floor Plan, 3D Design, Rendering &amp; CAD Features | JoyPlan India",
          "desc": "Explore every JoyPlan feature: laser-linked 2D plans, LiDAR scanning, multi-level design, materials, sunlight analysis, renders, 720&deg; panoramas and CAD export.",
          "ld": [{"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": f[2].replace("&amp;", "&").replace("&deg;", "°"), "url": "https://joyplanindia.com/features/#" + f[1]} for i, f in enumerate(F)]}],
          "body": BODY}]
