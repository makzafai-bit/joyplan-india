from components import ARR, btn, tbc

WA = "Hi JoyPlan India, I'd like to book a demo."


def chips(name, opts, default=0):
    b = "".join(f'<button type="button" class="chip" aria-pressed="{"true" if i == default else "false"}">{o}</button>' for i, o in enumerate(opts))
    return f'<div class="chips" data-chips="{name}" role="group">{b}</div><input type="hidden" name="{name}" value="{opts[default]}">'


def body(h1_id="h1"):
    return f'''
<section class="hero dark grid-bg" aria-labelledby="{h1_id}" style="align-items:flex-start;padding-top:56px">
  <div class="glow o" style="width:700px;height:700px;right:-260px;bottom:-300px;opacity:.22"></div>
  <div class="wrap demo-grid">
    <div class="hero-copy" data-enter style="gap:24px">
      {{{{CRUMBS}}}}
      <span class="kicker">Free &middot; live &middot; about 30 minutes {tbc("duration TBC")}</span>
      <h1 class="h-xl" id="{h1_id}" style="font-size:clamp(44px,6vw,96px)">Book your free <span class="hl-box"><span class="hl">JoyPlan</span></span> demo.</h1>
      <p class="lead">See the device and software working on a real floor plan: online, at our office, or at your site.</p>
      <div class="kv" style="width:100%">
        <div><span class="n">01</span><span><b>Tell us about your work</b><p>Six quick fields. One minute.</p></span></div>
        <div><span class="n">02</span><span><b>We call to fix a time</b><p>From the Bengaluru or Kozhikode team, whichever is nearer.</p></span></div>
        <div><span class="n">03</span><span><b>Measure, design, present: live</b><p>Bring a plan or a room you're working on.</p></span></div>
      </div>
      <div class="contact-cards" style="width:100%;margin-top:8px">
        <div class="panel"><span class="label">Head office &middot; Karnataka</span><p>BL Commerce, 7th Cross Road, Dollar Layout, Stage 2, Bengaluru, Karnataka</p></div>
        <div class="panel"><span class="label">Kerala branch</span><p>Third Floor, CK Tower, Near Bismi Hypermarket, Kannur Rd, West Nadakkave, Vandipetta, Vellayil, Kozhikode, Kerala 673011</p></div>
        <div class="panel"><span class="label">Email</span><p><a href="mailto:service@joyplan.com">service@joyplan.com</a></p></div>
        <div class="panel"><span class="label">Phone &middot; WhatsApp</span><p>{tbc("Number to be confirmed")}</p></div>
      </div>
      <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center"><span class="tag">App Store</span><span class="tag">Google Play</span><span class="tiny">Install the app free before your demo</span></div>
    </div>
    <div class="form-card rv">
      <form class="form" id="book" action="/lead.php" method="post" data-lead data-thanks="book-thanks" novalidate>
        <input type="hidden" name="form" value="book"><input type="hidden" name="nearest_team" value=""><input type="hidden" name="consent" value="yes"><input type="hidden" name="package" value="">
        <div class="hp" aria-hidden="true"><label>Website<input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
        <div class="field full"><span class="lab" id="lab-int">I'm interested in</span>{chips("interest", ["Device + Software", "Software only", "Device only", "Business / studio"])}</div>
        <div class="field full"><span class="lab">My profession</span>{chips("profession", ["Interior designer", "Architect", "Civil engineer", "Modular kitchen", "Furniture designer", "Other"])}</div>
        <div class="field"><label for="b-name">Full name</label><input id="b-name" name="full_name" autocomplete="name" required><span class="err">Please enter your name.</span></div>
        <div class="field"><label for="b-mob">Mobile number</label><input id="b-mob" name="mobile" type="tel" inputmode="tel" placeholder="+91" autocomplete="tel" required><span class="err">Enter a 10-digit Indian mobile number.</span></div>
        <div class="field"><label for="b-city">City</label><input id="b-city" name="city" placeholder="e.g. Kozhikode" autocomplete="address-level2" required><span class="err">Please enter your city.</span></div>
        <div class="field"><label for="b-fmt">Demo format</label><select id="b-fmt" name="demo_format"><option>Online (video call)</option><option>At a JoyPlan office</option><option>At my site / studio</option></select></div>
        <div class="field full"><label for="b-msg">Message (optional)</label><textarea id="b-msg" name="message" placeholder="Tell us about a current project"></textarea></div>
        <div class="full" style="display:grid;gap:10px"><button class="btn primary full" type="submit">Book my free demo{ARR}</button><a class="btn wa full" href="#" data-wa="{WA}">Prefer WhatsApp? Message us</a></div>
        <p class="form-msg full" role="alert"></p>
        <p class="tiny full" style="text-align:center">No spam. We use these details only to arrange your demo. <a href="/privacy/" style="text-decoration:underline">Privacy</a></p>
      </form>
      <div class="thanks" id="book-thanks" role="status">
        <span class="kicker">Request received</span>
        <h2 class="h-m">Thank you, <span data-first></span>. Your demo request is in.</h2>
        <dl><dt>Interest</dt><dd data-sum="interest"></dd><dt>Profession</dt><dd data-sum="profession"></dd><dt>Format</dt><dd data-sum="demo_format"></dd><dt>Nearest team</dt><dd data-sum="nearest_team"></dd></dl>
        <p class="muted">We'll call you to confirm a time {tbc("response time TBC")}.</p>
        <div class="btns"><a class="btn primary" href="#" data-wa="{WA}">Continue on WhatsApp</a>{btn("Explore features", "/features/", "ghost", False)}<button class="btn ghost" type="button" data-reset="book">New enquiry</button></div>
      </div>
    </div>
  </div>
</section>'''


ORGS = [{"@context": "https://schema.org", "@type": "LocalBusiness", "name": "JoyPlan India, Bengaluru head office", "email": "service@joyplan.com", "address": {"@type": "PostalAddress", "streetAddress": "BL Commerce, 7th Cross Road, Dollar Layout, Stage 2", "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "addressCountry": "IN"}},
        {"@context": "https://schema.org", "@type": "LocalBusiness", "name": "JoyPlan India, Kerala branch", "email": "service@joyplan.com", "address": {"@type": "PostalAddress", "streetAddress": "Third Floor, CK Tower, Near Bismi Hypermarket, Kannur Rd, West Nadakkave, Vandipetta, Vellayil", "addressLocality": "Kozhikode", "addressRegion": "Kerala", "postalCode": "673011", "addressCountry": "IN"}}]

THANKS = f'''
<section class="hero dark grid-bg" aria-labelledby="h1"><div class="glow o" style="width:600px;height:600px;right:-200px;top:-200px"></div>
<div class="wrap"><div class="hero-copy" data-enter><span class="kicker">Request received</span><h1 class="h-xl" id="h1">Thank you. Your demo request is in.</h1><p class="lead">A JoyPlan specialist from the nearest team will call you to fix a time. Prefer to talk now? Message us on WhatsApp.</p>
<div class="btns"><a class="btn primary" href="#" data-wa="{WA}">Continue on WhatsApp</a>{btn("Explore features", "/features/", "ghost", False)}</div></div></div></section>'''

PAGES = [
    {"path": "/book-a-demo/", "active": None, "nav_wa": True, "crumbs": [("Home", "/"), ("Book a demo", "/book-a-demo/")], "wa": WA,
     "title": "Book a Free JoyPlan Demo | Bengaluru &amp; Kozhikode",
     "desc": "Book a free live demo of the JoyPlan device and software, or talk to an expert on WhatsApp.", "ld": ORGS, "body": body()},
    {"path": "/contact/", "active": "/contact/", "nav_wa": True, "crumbs": [("Home", "/"), ("Contact", "/contact/")], "wa": WA,
     "title": "Contact JoyPlan India | Bengaluru &amp; Kozhikode",
     "desc": "Contact JoyPlan India in Bengaluru or Kozhikode, book a free demo or message us on WhatsApp.", "ld": ORGS, "body": body()},
    {"path": "/book-a-demo/thank-you/", "active": None, "noindex": True, "wa": WA, "title": "Thank you | JoyPlan India",
     "desc": "Your JoyPlan demo request is in.", "ld": [], "body": THANKS},
]
