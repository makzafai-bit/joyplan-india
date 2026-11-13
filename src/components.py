import os

"""Shared visual components for the JoyPlan India site (rendered into static HTML by build.py)."""


ARR = '<svg class="arr" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
WA_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 20.5l1.3-4.2A8.5 8.5 0 1 1 8 19.4z"/><path d="M9 8.6c.2 2.9 2.6 5.6 5.6 6.2l1.2-1.4-1.9-1-1 .8c-1-.4-1.9-1.3-2.3-2.3l.8-1-1-1.9z"/></svg>'


def logo_mark(uid="a"):
    return f'''<svg viewBox="0 0 300 300" aria-hidden="true"><defs><linearGradient id="jpW{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD400"/><stop offset=".55" stop-color="#FFC20E"/><stop offset="1" stop-color="#F9A21B"/></linearGradient><linearGradient id="jpL{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FDB813"/><stop offset="1" stop-color="#F37021"/></linearGradient><linearGradient id="jpR{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FCD29A"/><stop offset=".5" stop-color="#F8953A"/><stop offset="1" stop-color="#F26722"/></linearGradient></defs><rect width="300" height="300" rx="34" fill="#0B0B0B" stroke="rgba(255,255,255,.2)" stroke-width="8"/><g transform="scale(0.9772) translate(-27 -91)"><polygon points="172,130 268,181 268,298 172,248" fill="url(#jpW{uid})"/><polygon points="72,298 172,248 172,354" fill="url(#jpL{uid})"/><polygon points="172,248 268,298 172,354" fill="url(#jpR{uid})"/></g></svg>'''


def logo(uid="a", href="/"):
    return f'<a class="logo" href="{href}" aria-label="JoyPlan India home">{logo_mark(uid)}<span class="wm">joyplan</span><span class="in">INDIA</span></a>'


DEV_IMG = "/assets/site/img/device-front-cutout.webp"
DEV_W, DEV_H = 687, 1458
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "site", "img")


def device(val="3.480", cycle=None, cls="", style=""):
    """The JoyPlan SW-TB50 laser measure (product render, background removed) with a live reading on its LCD."""
    c = f' data-lcd="{cycle}"' if cycle else ""
    st = f' style="{style}"' if style else ""
    return (f'<div class="dev {cls}"{st} aria-hidden="true"><img src="{DEV_IMG}" alt="" width="{DEV_W}" height="{DEV_H}" loading="lazy" decoding="async">'
            f'<div class="lcd"><i>DIST</i><b{c}>{val}</b><em>m</em></div></div>')


def dev_img(style="", alt=""):
    return f'<img src="{DEV_IMG}" alt="{alt}" width="{DEV_W}" height="{DEV_H}" loading="lazy" decoding="async"{f' style="{style}"' if style else ""}>'


def pic(src, alt="", cls="", style="", w=None, h=None, lazy=True, sizes=None):
    """A real image. If a 960px-wide copy exists next to it (name-960.webp) it is offered to phones via srcset."""
    wh = f' width="{w}" height="{h}"' if w and h else ""
    c = f' class="{cls}"' if cls else ""
    st = f' style="{style}"' if style else ""
    ld = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    ss = ""
    if src.startswith("/assets/site/img/") and w and w > 1100:
        small = src[:-5] + "-960.webp"
        if os.path.exists(os.path.join(IMG_DIR, os.path.basename(small))):
            ss = f' srcset="{small} 960w, {src} {w}w" sizes="{sizes or "(max-width: 720px) 100vw, 60vw"}"'
    return f'<img src="{src}"{ss} alt="{alt}"{c}{st}{wh}{ld} decoding="async">'


# Every photo, render and app screen on the site, registered once. Point a key at a new file to swap it everywhere.
I = "/assets/site/img/"
IMG = {
    # JoyPlan India's own images (Nov 2026 set, full frame, never cropped)
    "hero": (I + "hero-measure-to-design.webp", 1870, 841, "The JoyPlan laser measure reading 4.625 m beside a 2D plan turning into a 3D design and a finished render"),
    "trad": (I + "transform-traditional.webp", 1438, 1094, "A designer redrawing a plan by hand with a tape measure, calculator and a site-revisit checklist"),
    "jp": (I + "transform-joyplan.webp", 1672, 941, "The same apartment in JoyPlan on a laptop, as a measured 2D plan and a furnished 3D model side by side"),
    "measure": (I + "workflow-measure.webp", 1670, 941, "A site engineer measuring an empty room with the JoyPlan laser measure"),
    "f2d": (I + "feature-2d-plan.webp", 1506, 1044, "Dimensioned 2D floor plan of a 3BHK apartment in JoyPlan, with room areas"),
    "f3d": (I + "feature-3d.webp", 1506, 1044, "The same 3BHK apartment as a furnished 3D model in JoyPlan"),
    "f720": (I + "feature-720.webp", 1672, 941, "720 degree panorama of a living room open in JoyPlan"),
    "f720tour": (I + "feature-720-tour.webp", 1671, 941, "720 degree panorama tour of a living and dining room"),
    "fcad": (I + "feature-cad-export.webp", 1671, 941, "CAD and export options in JoyPlan: DWG/DXF, PDF drawings and 3D models"),
    "felev": (I + "feature-elevations.webp", 1670, 941, "Bedroom key plan with bed-wall and wardrobe-wall elevations in JoyPlan"),
    "fsync": (I + "feature-sync.webp", 1671, 941, "A JoyPlan project syncing between phone, CAD on a desktop and a 3D model on a laptop"),
    "flidar": (I + "feature-lidar.webp", 1671, 941, "LiDAR scan of a living room captured as a 3D point model"),
    "fai": (I + "feature-ai-living.webp", 1672, 941, "Warm, neutral contemporary living room designed with AI assistance"),
    "ffurn": (I + "feature-furniture-materials.webp", 1670, 941, "Furniture and materials panel recolouring an armchair's upholstery and frame finish"),
    "devfront": (I + "device-front.webp", 1024, 1536, "Front of the JoyPlan SW-TB50 laser measure with its LCD, READ key and bubble levels"),
    "devangled": (I + "device-angled.webp", 1024, 1536, "The JoyPlan SW-TB50 laser measure showing area, volume and a 12.560 m reading"),
    "devviews": (I + "device-views.webp", 1536, 1024, "The JoyPlan SW-TB50 from six sides: front, angled, side, back label, laser window and base"),
    # Earlier JoyPlan renders and app screens
    "living": (I + "living.webp", 1040, 1134, "Living room with a curved sofa and pendant light, rendered in JoyPlan"),
    "lounge": (I + "lounge.webp", 504, 492, "Beige sofa and side table in a sunlit lounge, rendered in JoyPlan"),
    "armchair": (I + "armchair.webp", 504, 492, "Reading corner with an oak armchair, rendered in JoyPlan"),
    "villa": ("/assets/hero.webp", 1370, 960, "Two-storey home shown as a 3D cutaway with furnished interiors"),
    "whiterender": (I + "white-to-render.webp", 2372, 858, "The same living room as a white model on the left and a finished render on the right"),
    "render": (I + "render-final.webp", 1136, 858, "Rendered living room with modular sofa and sculptural lamps"),
    "appfinish": (I + "app-plan-finishes.webp", 560, 530, "Floor plan with wood, tile and lawn finishes applied in the JoyPlan app"),
    "furnlib": ("/assets/step3.webp", 1000, 733, "Furniture library open beside a furnished plan in the JoyPlan app"),
    "share": ("/assets/share.webp", 1500, 597, "The same JoyPlan project open on phone, tablet and laptop"),
    "areas": ("/assets/make1.webp", 836, 924, "Room area and perimeter details listed in JoyPlan"),
    "estimate": ("/assets/make2.webp", 840, 934, "Estimate broken down by trade in JoyPlan"),
    "sun": ("/assets/f_sun.webp", 712, 504, "Sunlight analysis dial over a 3D model in JoyPlan"),
}


def img(key, cls="", style="", alt=None, lazy=True, sizes=None):
    src, w, h, a = IMG[key]
    return pic(src, a if alt is None else alt, cls, style, w, h, lazy, sizes)


def ratio(key):
    _s, w, h, _a = IMG[key]
    return f"{w}/{h}"


def frame(key, cls="", alt=None, lazy=True, sizes=None, extra=""):
    """Show an image whole (never cropped) in a box that takes the image's own aspect ratio."""
    return f'<figure class="frame {cls}" style="aspect-ratio:{ratio(key)}">{img(key, alt=alt, lazy=lazy, sizes=sizes)}{extra}</figure>'


def fit(key, cls="", alt=None, sizes=None):
    """Show an image whole inside a fixed box: contained, with a blurred copy of itself filling any spare space."""
    src = IMG[key][0]
    small = src[:-5] + "-960.webp"
    bg = small if os.path.exists(os.path.join(IMG_DIR, os.path.basename(small))) and src.startswith(I) else src
    return f'<div class="fit {cls}"><span class="fit-bg" style="background-image:url({bg})"></span>{img(key, alt=alt, sizes=sizes)}</div>'


def tablet(fname, right_html, screen, props=None, cls="", attrs=""):
    body_cls = "tab-body props" if props else "tab-body"
    rail = '<div class="rail"><span class="on"></span><span></span><span></span><span></span><span></span></div>'
    pp = f'<div class="pp">{props}</div>' if props else ""
    return (f'<div class="tab {cls}" {attrs}><div class="tab-scr"><div class="tab-bar"><span class="fn">{fname}</span>{right_html}</div>'
            f'<div class="{body_cls}">{rail}<div class="canvas">{screen}</div>{pp}</div></div></div>')


def btn(label, href, kind="primary", arrow=True, extra="", sm=False):
    s = " sm" if sm else ""
    a = ARR if arrow else ""
    return f'<a class="btn {kind}{s}" href="{href}" {extra}>{label}{a}</a>'


def tlink(label, href):
    return f'<a class="tlink" href="{href}">{label}{ARR}</a>'


def tbc(text="To be confirmed"):
    return f'<span class="tbc">[{text}]</span>'


# ---------- small line-art visuals (illustrative, replace with real photos/screens) ----------
