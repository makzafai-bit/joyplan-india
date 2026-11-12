"""Shared visual components for the JoyPlan India site (rendered into static HTML by build.py)."""


ARR = '<svg class="arr" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
WA_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 20.5l1.3-4.2A8.5 8.5 0 1 1 8 19.4z"/><path d="M9 8.6c.2 2.9 2.6 5.6 5.6 6.2l1.2-1.4-1.9-1-1 .8c-1-.4-1.9-1.3-2.3-2.3l.8-1-1-1.9z"/></svg>'


def logo_mark(uid="a"):
    return f'''<svg viewBox="0 0 300 300" aria-hidden="true"><defs><linearGradient id="jpW{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD400"/><stop offset=".55" stop-color="#FFC20E"/><stop offset="1" stop-color="#F9A21B"/></linearGradient><linearGradient id="jpL{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FDB813"/><stop offset="1" stop-color="#F37021"/></linearGradient><linearGradient id="jpR{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FCD29A"/><stop offset=".5" stop-color="#F8953A"/><stop offset="1" stop-color="#F26722"/></linearGradient></defs><rect width="300" height="300" rx="34" fill="#0B0B0B" stroke="rgba(255,255,255,.2)" stroke-width="8"/><g transform="scale(0.9772) translate(-27 -91)"><polygon points="172,130 268,181 268,298 172,248" fill="url(#jpW{uid})"/><polygon points="72,298 172,248 172,354" fill="url(#jpL{uid})"/><polygon points="172,248 268,298 172,354" fill="url(#jpR{uid})"/></g></svg>'''


def logo(uid="a", href="/"):
    return f'<a class="logo" href="{href}" aria-label="JoyPlan India home">{logo_mark(uid)}<span class="wm">joyplan</span><span class="in">INDIA</span></a>'


DEV_IMG = "/assets/site/img/joyplan-laser-device.webp"


def device(val="3.480", cycle=None, cls="", style=""):
    """The real JoyPlan laser measure (photo cut-out) with a live reading laid over its LCD."""
    c = f' data-lcd="{cycle}"' if cycle else ""
    st = f' style="{style}"' if style else ""
    return (f'<div class="dev {cls}"{st} aria-hidden="true"><img src="{DEV_IMG}" alt="" width="357" height="678" loading="lazy" decoding="async">'
            f'<div class="lcd"><i>DIST</i><b{c}>{val}</b><em>m</em></div></div>')


def pic(src, alt="", cls="", style="", w=None, h=None, lazy=True):
    """A real image (render, app screen or photo)."""
    wh = f' width="{w}" height="{h}"' if w and h else ""
    c = f' class="{cls}"' if cls else ""
    st = f' style="{style}"' if style else ""
    ld = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    return f'<img src="{src}" alt="{alt}"{c}{st}{wh}{ld} decoding="async">'


# Real imagery: JoyPlan renders and app screens, plus crops of JoyPlan India's own ad creative.
IMG = {
    "living": ("/assets/site/img/living.webp", 1040, 1134, "Living room with a curved sofa and pendant light, rendered in JoyPlan"),
    "lounge": ("/assets/site/img/lounge.webp", 504, 492, "Beige sofa and side table in a sunlit lounge, rendered in JoyPlan"),
    "armchair": ("/assets/site/img/armchair.webp", 504, 492, "Reading corner with an oak armchair, rendered in JoyPlan"),
    "villa": ("/assets/hero.webp", 1370, 960, "Two-storey home shown as a 3D cutaway with furnished interiors"),
    "whiterender": ("/assets/site/img/white-to-render.webp", 2372, 858, "The same living room as a white model on the left and a finished render on the right"),
    "render": ("/assets/site/img/render-final.webp", 1136, 858, "Rendered living room with modular sofa and sculptural lamps"),
    "apt3d": ("/assets/site/img/apartment-3d.webp", 632, 756, "Furnished apartment shown as a 3D cutaway: living, dining, bedrooms and kitchen"),
    "plan2d": ("/assets/site/img/plan-2d-dark.webp", 556, 714, "Furnished 2D floor plan of a three-bedroom apartment"),
    "site": ("/assets/site/img/site-measure.webp", 535, 960, "The JoyPlan laser measure taking a reading across an empty room"),
    "appplan": ("/assets/site/img/app-plan.webp", 600, 530, "Dimensioned 2D floor plan in the JoyPlan app"),
    "appfinish": ("/assets/site/img/app-plan-finishes.webp", 560, 530, "Floor plan with wood, tile and lawn finishes applied in the JoyPlan app"),
    "app3d": ("/assets/site/img/app-3d.webp", 620, 610, "The same plan as a furnished 3D model in the JoyPlan app"),
    "furnlib": ("/assets/step3.webp", 1000, 733, "Furniture library open beside a furnished plan in the JoyPlan app"),
    "material": ("/assets/f_material.webp", 740, 504, "Material editor recolouring an armchair in JoyPlan"),
    "lidar": ("/assets/f_lidar.webp", 734, 504, "A room captured as a 3D scan in JoyPlan"),
    "share": ("/assets/share.webp", 1500, 597, "The same JoyPlan project open on phone, tablet and laptop"),
    "cad": ("/assets/make3.webp", 1000, 1058, "Files and sharing screen with CAD export options in JoyPlan"),
    "areas": ("/assets/make1.webp", 836, 924, "Room area and perimeter details listed in JoyPlan"),
    "estimate": ("/assets/make2.webp", 840, 934, "Estimate broken down by trade in JoyPlan"),
    "sun": ("/assets/f_sun.webp", 712, 504, "Sunlight analysis dial over a 3D model in JoyPlan"),
}


def img(key, cls="", style="", alt=None, lazy=True):
    src, w, h, a = IMG[key]
    return pic(src, a if alt is None else alt, cls, style, w, h, lazy)


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
