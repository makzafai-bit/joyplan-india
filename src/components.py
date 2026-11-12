"""Shared visual components for the JoyPlan India site (rendered into static HTML by build.py)."""

WALLS = "M20 20H580V400H20Z M260 20V160 M260 210V250 M400 20V110 M400 160V300 M400 350V400 M20 250H90 M140 250H300 M350 250H580"

ARR = '<svg class="arr" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
WA_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3.5 20.5l1.3-4.2A8.5 8.5 0 1 1 8 19.4z"/><path d="M9 8.6c.2 2.9 2.6 5.6 5.6 6.2l1.2-1.4-1.9-1-1 .8c-1-.4-1.9-1.3-2.3-2.3l.8-1-1-1.9z"/></svg>'


def logo_mark(uid="a"):
    return f'''<svg viewBox="0 0 300 300" aria-hidden="true"><defs><linearGradient id="jpW{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFD400"/><stop offset=".55" stop-color="#FFC20E"/><stop offset="1" stop-color="#F9A21B"/></linearGradient><linearGradient id="jpL{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FDB813"/><stop offset="1" stop-color="#F37021"/></linearGradient><linearGradient id="jpR{uid}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FCD29A"/><stop offset=".5" stop-color="#F8953A"/><stop offset="1" stop-color="#F26722"/></linearGradient></defs><rect width="300" height="300" rx="34" fill="#0B0B0B" stroke="rgba(255,255,255,.2)" stroke-width="8"/><g transform="scale(0.9772) translate(-27 -91)"><polygon points="172,130 268,181 268,298 172,248" fill="url(#jpW{uid})"/><polygon points="72,298 172,248 172,354" fill="url(#jpL{uid})"/><polygon points="172,248 268,298 172,354" fill="url(#jpR{uid})"/></g></svg>'''


def logo(uid="a", href="/"):
    return f'<a class="logo" href="{href}" aria-label="JoyPlan India home">{logo_mark(uid)}<span class="wm">joyplan</span><span class="in">INDIA</span></a>'


def plan(cls="", dims=True, labels=True, sel=False, furn=False, anim=False, areas=False):
    out = [f'<svg class="plan2d{" anim" if anim else ""} {cls}" viewBox="-30 -40 660 490" aria-hidden="true">']
    if furn:
        out.append('<rect class="furn" x="60" y="60" width="110" height="130" rx="4"/><rect class="furn" x="430" y="60" width="110" height="130" rx="4"/><rect class="furn" x="80" y="300" width="170" height="60" rx="6"/><rect class="furn" x="290" y="40" width="80" height="40"/>')
    out.append(f'<path class="w" d="{WALLS}"/>')
    if sel:
        out.append('<path class="sel" d="M20 400H400"/>')
    if dims:
        out.append('<g class="dl"><path d="M20 -18H580M20 -26V-10M580 -26V-10"/><path d="M-12 20V400M-20 20H-4M-20 400H-4"/></g>'
                   '<text class="dt" x="300" y="-24" text-anchor="middle">11.200 m</text>'
                   '<text class="dt" x="-20" y="214" text-anchor="middle" transform="rotate(-90 -20 210)">7.600 m</text>')
    if labels:
        a = ' · 15.2 m²' if areas else ''
        out.append(f'<text class="rl" x="40" y="48">BEDROOM 1{a}</text><text class="rl" x="278" y="48">KITCHEN</text><text class="rl" x="418" y="48">BEDROOM 2</text><text class="rl" x="40" y="388">LIVING{" · 22.8 m²" if areas else ""}</text><text class="rl" x="418" y="388">BATH</text>')
    out.append('</svg>')
    return "".join(out)


def iso(id_="", layers=12, rise=False, cls="", rooms=True, furn=False):
    base = ['<div class="iso-l base" style="--i:0"><svg viewBox="0 0 600 420"><rect class="fl" x="20" y="20" width="560" height="380"/>']
    if rooms:
        base.append('<rect class="rm" x="270" y="30" width="120" height="210"/><rect class="rm o" x="410" y="260" width="160" height="130"/><rect class="rm p" x="30" y="260" width="360" height="130"/>')
    if furn:
        base.append('<rect x="60" y="60" width="110" height="130" fill="#d9cfc0" opacity=".8"/><rect x="440" y="70" width="100" height="120" fill="#d9cfc0" opacity=".8"/><rect x="90" y="300" width="170" height="54" fill="#FD4100"/>')
    base.append('</svg></div>')
    ls = []
    for i in range(1, layers + 1):
        top = " top" if i == layers else ""
        ls.append(f'<div class="iso-l{top}" style="--i:{i}"><svg viewBox="0 0 600 420"><path class="w" d="{WALLS}"/></svg></div>')
    rid = f' id="{id_}"' if id_ else ""
    r = " data-rise" if rise else ""
    return f'<div class="iso {cls}"{rid}{r} aria-hidden="true"><div class="iso-stage">{"".join(base)}{"".join(ls)}</div></div>'


def device(val="3.480", cycle=None, cls="", style=""):
    c = f' data-lcd="{cycle}"' if cycle else ""
    st = f' style="{style}"' if style else ""
    return (f'<div class="dev {cls}"{st} aria-hidden="true"><div class="cap"><div class="lens"></div></div>'
            f'<div class="lcd"><i>DIST</i><b{c}>{val}</b><em>m</em></div><div class="key"></div>'
            f'<div class="brand">joyplan</div><div class="pills"><span></span><span></span><span></span></div></div>')


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
def svg_box(inner, vb="0 0 400 300", bg="#121212"):
    return f'<svg viewBox="{vb}" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="100%" height="100%" fill="{bg}"/>{GRID_PATTERN}{inner}</svg>'


GRID_PATTERN = '<defs><pattern id="g20" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="rgba(255,255,255,.05)"/></pattern></defs><rect width="100%" height="100%" fill="url(#g20)"/>'

VIS = {
    # profession / use visuals
    "designer": '<rect x="70" y="50" width="110" height="140" fill="#C9A27A"/><rect x="195" y="50" width="135" height="60" fill="#4b5058"/><rect x="195" y="122" width="62" height="68" fill="#F26722"/><rect x="268" y="122" width="62" height="68" fill="#E9E1D3"/><rect x="70" y="205" width="260" height="46" rx="8" fill="#2a2a2a" stroke="#3a3a3a"/><path d="M70 268H330M70 262V274M330 262V274" stroke="#FFC20E" stroke-width="1.5"/>',
    "architect": '<path d="M100 250V140L200 70L300 140V250Z" fill="none" stroke="#F4F1EC" stroke-width="3"/><path d="M100 140H300" stroke="#F4F1EC" stroke-width="1.5" opacity=".5"/><rect x="135" y="160" width="40" height="28" fill="none" stroke="#F26722" stroke-width="2.5"/><rect x="225" y="160" width="40" height="28" fill="none" stroke="#F26722" stroke-width="2.5"/><rect x="185" y="205" width="32" height="45" fill="#FD4100"/><path d="M325 70V250M318 70H332M318 250H332" stroke="#FFC20E" stroke-width="1.5"/><circle cx="320" cy="48" r="14" fill="#FFC20E"/><path d="M308 60L270 100" stroke="#FFC20E" stroke-dasharray="4 4"/>',
    "engineer": '<g stroke="#F4F1EC" stroke-dasharray="5 5" opacity=".45"><path d="M90 110H330M90 200H330M120 80V240M210 80V240M300 80V240"/></g><g fill="#FD4100"><rect x="114" y="104" width="12" height="12"/><rect x="204" y="104" width="12" height="12"/><rect x="294" y="104" width="12" height="12"/><rect x="114" y="194" width="12" height="12"/><rect x="204" y="194" width="12" height="12"/><rect x="294" y="194" width="12" height="12"/></g><path d="M126 86H204" stroke="#FFC20E" stroke-width="1.5"/><text x="165" y="80" fill="#FFC20E" font-family="JetBrains Mono" font-size="11" text-anchor="middle">4.500</text><text x="70" y="114" fill="#FFC20E" font-family="JetBrains Mono" font-size="11">1</text><text x="70" y="204" fill="#FFC20E" font-family="JetBrains Mono" font-size="11">2</text>',
    "kitchen": '<rect x="80" y="60" width="240" height="60" fill="none" stroke="#F4F1EC" stroke-width="2"/><path d="M140 60V120M200 60V120M260 60V120" stroke="#F4F1EC" stroke-width="1.5"/><rect x="175" y="135" width="50" height="10" fill="#666"/><rect x="80" y="155" width="240" height="10" fill="#FD4100"/><rect x="80" y="165" width="240" height="70" fill="#2b2b2b" stroke="#F4F1EC" stroke-width="2"/><path d="M160 165V235M240 165V235" stroke="#F4F1EC" stroke-width="1.5"/><path d="M80 252H320M80 246V258M320 246V258" stroke="#FFC20E" stroke-width="1.5"/>',
    "furniture": '<rect x="110" y="50" width="180" height="200" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><path d="M200 50V250M110 150H290" stroke="#F4F1EC" stroke-width="1.5"/><rect x="120" y="60" width="70" height="50" fill="#8a6f55"/><rect x="215" y="190" width="65" height="50" fill="#b5532a"/><circle cx="190" cy="155" r="3" fill="#F4F1EC"/><circle cx="210" cy="155" r="3" fill="#F4F1EC"/><path d="M310 50V250M304 50H316M304 250H316" stroke="#FFC20E" stroke-width="1.5"/><text x="322" y="154" fill="#FFC20E" font-family="JetBrains Mono" font-size="11">2.40</text>',
}


def vis(name, label=None, bg="#121212"):
    inner = VIS[name]
    lab = f'<span class="illus">{label}</span>' if label else ""
    return f'{svg_box(inner, bg=bg)}{lab}'


def room_scene(stage):
    """One-point perspective room used in workflow stage 1."""
    return ('<svg viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="800" height="500" fill="#151515"/>'
            '<path d="M0 0L240 130H560L800 0Z" fill="#1b1b1b"/><path d="M0 500L240 370H560L800 500Z" fill="#1d1d1d"/><path d="M0 0L240 130V370L0 500Z" fill="#181818"/><path d="M800 0L560 130V370L800 500Z" fill="#181818"/>'
            '<rect x="240" y="130" width="320" height="240" fill="#222"/>'
            '<g stroke="rgba(255,255,255,.06)"><path d="M240 400H560M200 430H600M150 465H650"/></g>'
            '<rect x="350" y="180" width="100" height="90" fill="#3a2f22" stroke="#6b5640"/><path d="M400 180V270M350 225H450" stroke="#6b5640"/>'
            '<path d="M260 160H540M260 152V168M540 152V168" stroke="#FFC20E" stroke-width="2" class="drawline"/>'
            '<rect x="362" y="150" width="76" height="20" fill="#0B0B0B"/><text x="400" y="164" fill="#FFC20E" font-family="JetBrains Mono" font-size="12" text-anchor="middle">4.625 m</text>'
            '<path d="M150 420L520 300" stroke="#FD4100" stroke-width="3"/><path d="M150 420L520 300" stroke="#FD4100" stroke-width="12" opacity=".18"/><circle cx="520" cy="300" r="6" fill="#FD4100"/>'
            '<g transform="translate(118 390) rotate(-28)"><rect width="34" height="80" rx="9" fill="#222" stroke="#333"/><rect width="34" height="16" rx="8" fill="#FD4100"/><circle cx="17" cy="48" r="8" fill="#FD4100"/></g>'
            '</svg>')


def render_scene(white=False):
    """A living room as white model or as warm render (for before/after)."""
    if white:
        return ('<svg viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="800" height="450" fill="#ECEBE7"/><rect y="330" width="800" height="120" fill="#DEDCD6"/>'
                '<rect x="330" y="70" width="190" height="200" fill="#F7F6F3" stroke="#cfcdc7"/><path d="M180 330V260a20 20 0 0 1 20-20h330a20 20 0 0 1 20 20v70z" fill="#d6d4cf"/><rect x="160" y="280" width="410" height="70" rx="16" fill="#cfcdc7"/>'
                '<rect x="610" y="250" width="70" height="120" fill="#e3e1dc"/><circle cx="645" cy="230" r="34" fill="#dcdad4"/><rect x="380" y="350" width="110" height="40" fill="#c9c7c1"/></svg>')
    return ('<svg viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><defs><linearGradient id="rw" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6E7CF"/><stop offset="1" stop-color="#E7CFAE"/></linearGradient><linearGradient id="rf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9A6B43"/><stop offset="1" stop-color="#6E4A2E"/></linearGradient></defs>'
            '<rect width="800" height="450" fill="url(#rw)"/><rect y="330" width="800" height="120" fill="url(#rf)"/><path d="M520 0L800 0L800 330L640 330Z" fill="#fff" opacity=".25"/>'
            '<rect x="330" y="70" width="190" height="200" fill="#FFF8EA" stroke="#C9A87E" stroke-width="6"/><path d="M180 330V260a20 20 0 0 1 20-20h330a20 20 0 0 1 20 20v70z" fill="#5d5650"/><rect x="160" y="280" width="410" height="70" rx="16" fill="#4c4641"/><rect x="200" y="252" width="70" height="40" rx="8" fill="#F26722"/>'
            '<rect x="625" y="270" width="40" height="100" fill="#7a5a3c"/><circle cx="645" cy="230" r="44" fill="#6F8F55"/><rect x="380" y="350" width="110" height="40" fill="#3b3430"/><ellipse cx="400" cy="420" rx="280" ry="22" fill="#000" opacity=".15"/></svg>')


def pano_svg():
    return ('<svg viewBox="0 0 1200 400" preserveAspectRatio="none" aria-hidden="true"><defs><linearGradient id="pw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8B6A4E"/><stop offset=".62" stop-color="#6B4D36"/><stop offset=".62" stop-color="#4A3424"/><stop offset="1" stop-color="#3A291C"/></linearGradient></defs>'
            '<rect width="1200" height="400" fill="url(#pw)"/><path d="M0 250Q300 210 600 250T1200 250V400H0Z" fill="#3A291C"/>'
            '<rect x="180" y="110" width="160" height="110" fill="#EADBC0"/><rect x="560" y="240" width="190" height="70" rx="10" fill="#3d3d3d"/><rect x="590" y="215" width="70" height="36" rx="8" fill="#F26722"/>'
            '<ellipse cx="460" cy="270" rx="70" ry="30" fill="#6F8F55"/><rect x="900" y="120" width="120" height="170" fill="#2a2a2a" opacity=".6"/><rect x="40" y="160" width="60" height="150" fill="#1d1d1d" opacity=".7"/></svg>')


def elevation(kind="kitchen", bg="#F4F1EC"):
    if kind == "kitchen":
        inner = '<rect x="60" y="40" width="280" height="80" fill="none" stroke="#111" stroke-width="2"/><rect x="60" y="150" width="280" height="90" fill="#F6DDB5" stroke="#111" stroke-width="2"/><path d="M130 150V240M200 150V240M270 150V240M130 40V120M200 40V120M270 40V120" stroke="#111" stroke-width="1.5"/><path d="M60 262H340M60 256V268M340 256V268" stroke="#C2410C" stroke-width="1.5"/><text x="200" y="282" font-family="JetBrains Mono" font-size="11" fill="#C2410C" text-anchor="middle">3.480 m</text>'
    elif kind == "wardrobe":
        inner = '<rect x="80" y="30" width="240" height="220" fill="none" stroke="#111" stroke-width="2"/><rect x="80" y="160" width="240" height="90" fill="#D9CBB8"/><path d="M140 30V250M200 30V250M260 30V250" stroke="#111" stroke-width="1.5"/><path d="M80 268H320M80 262V274M320 262V274" stroke="#C2410C" stroke-width="1.5"/><text x="200" y="288" font-family="JetBrains Mono" font-size="11" fill="#C2410C" text-anchor="middle">2.400 m</text>'
    else:  # cafe plan
        inner = '<rect x="50" y="30" width="300" height="240" fill="none" stroke="#F4F1EC" stroke-width="3"/><path d="M150 30V150M50 150H150" stroke="#F4F1EC" stroke-width="2"/><rect x="65" y="45" width="70" height="30" fill="#C8961E"/><g fill="#3a3a3a">' + "".join(f'<rect x="{180+c*55}" y="{55+r*55}" width="30" height="22"/>' for r in range(4) for c in range(3)) + '</g><circle cx="95" cy="225" r="20" fill="#2a2a2a"/>'
        return f'<svg viewBox="0 0 400 300" aria-hidden="true"><rect width="400" height="300" fill="#111"/>{inner}</svg>'
    return f'<svg viewBox="0 0 400 300" aria-hidden="true"><rect width="400" height="300" fill="{bg}"/>{inner}</svg>'


# feature-library panel visuals (line art on the app grid)
def fvis(key):
    W = '#F4F1EC'
    box = f'<rect x="90" y="60" width="220" height="150" fill="none" stroke="{W}" stroke-width="3"/><path d="M200 60V210M90 135H200" stroke="{W}" stroke-width="2.5"/>'
    lab = lambda t: f'<text x="200" y="244" fill="#FFC20E" font-family="JetBrains Mono" font-size="10" letter-spacing="1.5" text-anchor="middle">{t}</text>'
    m = {
        "laser": box + '<rect x="92" y="62" width="106" height="72" fill="#FD4100" opacity=".18"/><path d="M110 225L300 70" stroke="#FD4100" stroke-width="3"/><circle cx="300" cy="70" r="5" fill="#FD4100"/>' + lab("READING · WALL A · 4.625 M"),
        "lidar": '<path d="M140 70H260L310 200H90Z" fill="#FFC20E" fill-opacity=".08" stroke="#F4F1EC" stroke-width="3"/><path d="M80 140H320" stroke="#FD4100" stroke-width="2.5"/>' + lab("SCANNING…"),
        "photos": box + '<rect x="255" y="72" width="40" height="30" fill="#2a2a2a" stroke="#FD4100"/><path d="M262 96L286 76" stroke="#FD4100" stroke-width="2"/><path d="M120 185L135 170" stroke="#FD4100" stroke-width="3"/>' + lab("3 PHOTO NOTES"),
        "plan2d": box + '<path d="M90 45H310" stroke="#FD4100" stroke-width="2"/><rect x="92" y="137" width="106" height="71" fill="#FD4100" opacity=".14"/>' + lab("11.200 M"),
        "multi": '<rect x="150" y="70" width="100" height="26" fill="#FFC20E" fill-opacity=".1" stroke="#F4F1EC" stroke-width="2.5"/><rect x="130" y="110" width="140" height="26" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><rect x="110" y="150" width="180" height="26" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><path d="M260 83H300M280 123H320M300 163H330" stroke="#FD4100" stroke-width="2"/>' + lab("LEVELS · G · 1 · 2"),
        "ai": box + '<path d="M265 85l7 16 16 7-16 7-7 16-7-16-16-7 16-7z" fill="none" stroke="#FD4100" stroke-width="2"/><rect x="202" y="137" width="106" height="71" fill="#FD4100" opacity=".14"/>' + lab("AI LAYOUT"),
        "hard": box + '<rect x="92" y="137" width="106" height="71" fill="#8a5a3a" opacity=".6"/><path d="M100 200L160 140M130 205L190 145" stroke="#FD4100" stroke-width="2"/>' + lab("FLOOR · TERRAZZO"),
        "freeform": '<path d="M110 190Q200 60 290 190" fill="none" stroke="#F4F1EC" stroke-width="3"/><path d="M130 190Q200 100 270 190" fill="none" stroke="#FD4100" stroke-width="3"/><path d="M90 190H310" stroke="#F4F1EC" stroke-width="2"/>' + lab("CEILING PROFILE"),
        "furn": '<rect x="120" y="120" width="120" height="60" fill="#3a3a3a" stroke="#F4F1EC" stroke-width="2"/><rect x="130" y="100" width="100" height="25" fill="none" stroke="#F4F1EC" stroke-width="2"/><rect x="260" y="120" width="35" height="60" fill="none" stroke="#F4F1EC" stroke-width="2"/>' + lab("SOFA · 3 SEATER"),
        "material": '<rect x="130" y="100" width="140" height="70" fill="#F26722"/><path d="M290 90V180" stroke="#FD4100" stroke-width="2" stroke-dasharray="6 6"/>' + lab("LINEN · BURNT ORANGE"),
        "walk": '<path d="M200 70L310 120L200 170L90 120Z" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><path d="M90 120V160L200 210L310 160V120" fill="none" stroke="#F4F1EC" stroke-width="2"/><rect x="170" y="125" width="60" height="30" fill="#FD4100" opacity=".25"/><path d="M200 110V180" stroke="#FD4100" stroke-width="2"/>' + lab("ORBIT · WALK"),
        "render": '<rect x="90" y="70" width="220" height="130" fill="#EADBC0"/><rect x="230" y="85" width="60" height="70" fill="#F8F1E4" stroke="#c9b79c"/><path d="M110 185V160H160V185" fill="none" stroke="#FD4100" stroke-width="3"/>' + lab("RENDERING · 1920×1080"),
        "pano": '<rect x="80" y="90" width="240" height="90" fill="#6B4D36"/><path d="M80 150Q200 120 320 150" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><circle cx="200" cy="130" r="14" fill="none" stroke="#FD4100" stroke-width="2.5"/>' + lab("DRAG TO LOOK AROUND"),
        "sun": box + '<rect x="202" y="62" width="106" height="72" fill="#FFC20E" opacity=".15"/><path d="M220 210L300 120M240 210L310 140" stroke="#FD4100" stroke-width="2.5"/>' + lab("SUN · 16:30"),
        "drawings": '<rect x="100" y="60" width="200" height="150" fill="#EDE6DA"/><rect x="115" y="75" width="110" height="80" fill="none" stroke="#333" stroke-width="2"/><rect x="240" y="160" width="45" height="35" fill="none" stroke="#333"/><path d="M115 172H225" stroke="#FD4100" stroke-width="2"/>' + lab("A-101 · 1:50"),
        "area": '<path d="M110 90H290M110 120H290M110 150H290M110 180H290" stroke="#F4F1EC" stroke-width="2.5"/><path d="M250 75V195" stroke="#FD4100" stroke-width="3"/>' + lab("TOTAL · 86.4 M²"),
        "estimate": '<path d="M110 200H300" stroke="#FD4100" stroke-width="2.5"/><path d="M130 200V150M160 200V120M190 200V165M220 200V95M250 200V140M280 200V125" stroke="#F4F1EC" stroke-width="3"/>' + lab("ESTIMATE REPORT"),
        "cad": box + '<path d="M280 180V205M270 195L280 205L290 195" stroke="#FD4100" stroke-width="2.5" fill="none"/><rect x="92" y="62" width="106" height="72" fill="#FD4100" opacity=".12"/>' + lab("EXPORT · CAD"),
        "share": '<rect x="160" y="95" width="80" height="60" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><rect x="100" y="110" width="30" height="45" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><rect x="270" y="80" width="50" height="40" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><path d="M130 130H160M240 120H270" stroke="#FD4100" stroke-width="2" stroke-dasharray="4 4"/>' + lab("IN SYNC"),
        "learn": '<rect x="120" y="70" width="160" height="110" fill="none" stroke="#F4F1EC" stroke-width="2.5"/><path d="M185 100L225 125L185 150Z" fill="none" stroke="#FD4100" stroke-width="3"/>' + lab("HOW TO · WALLS"),
    }
    return f'<svg viewBox="0 0 400 260" aria-hidden="true"><rect width="400" height="260" fill="#161616"/>{GRID_PATTERN}{m[key]}</svg>'


def sofa_screen():
    return ('<svg viewBox="0 0 400 260" aria-hidden="true" id="sofa-screen"><rect width="400" height="260" fill="#1a1a1a"/>'
            '<rect x="60" y="180" width="280" height="10" fill="#2a2a2a"/>'
            '<path class="sofa" d="M90 180V125a16 16 0 0 1 16-16h188a16 16 0 0 1 16 16v55z" fill="#F26722"/>'
            '<rect class="sofa" x="72" y="140" width="256" height="48" rx="12" fill="#F26722" style="filter:brightness(.85)"/>'
            '<rect x="110" y="188" width="8" height="16" fill="#555"/><rect x="282" y="188" width="8" height="16" fill="#555"/>'
            '<text x="200" y="232" fill="#FFC20E" font-family="JetBrains Mono" font-size="10" letter-spacing="1.5" text-anchor="middle">MATERIAL EDITOR · TAP A SWATCH</text></svg>')
