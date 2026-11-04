/* Shared script for the Meta ads landing pages.
   ---------------------------------------------------------------
   SETTINGS: fill these in, commit, and every page picks them up.
   WHATSAPP  digits only with country code, e.g. "919876543210".
             Empty hides every WhatsApp button.
   PIXEL_ID  Meta Pixel ID. Empty means no Pixel loads.
   GA4_ID    Google Analytics 4 measurement ID ("G-XXXXXXX"). Empty means no GA4.
   --------------------------------------------------------------- */
var JP = {
  WHATSAPP: "",
  WHATSAPP_TEXT: "Hi Joyplan India, I'd like to know more.",
  PIXEL_ID: "",
  GA4_ID: ""
};

(function () {
  var d = document, root = d.documentElement, body = d.body;
  root.classList.add("js");
  var page = body.getAttribute("data-page") || "";        // demo | masterclass | partner
  var isThanks = body.hasAttribute("data-thanks");

  /* ---------- tracking ---------- */
  function loadScript(src) { var s = d.createElement("script"); s.async = true; s.src = src; d.head.appendChild(s); }
  if (JP.PIXEL_ID) {
    !function (f, b, e, v, n) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments) }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = "2.0"; n.queue = []; }(window, d);
    loadScript("https://connect.facebook.net/en_US/fbevents.js");
    fbq("init", JP.PIXEL_ID);
    fbq("track", "PageView");
  }
  if (JP.GA4_ID) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { dataLayer.push(arguments); };
    gtag("js", new Date());
    gtag("config", JP.GA4_ID);
    loadScript("https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(JP.GA4_ID));
  }
  function px(ev, params) { if (window.fbq) fbq("track", ev, params || {}); }
  function ga(ev, params) { if (window.gtag && JP.GA4_ID) gtag("event", ev, params || {}); }
  JP.track = { px: px, ga: ga };

  /* ---------- WhatsApp links ---------- */
  if (JP.WHATSAPP) {
    body.classList.add("has-wa");
    var waHref = "https://wa.me/" + JP.WHATSAPP + "?text=" + encodeURIComponent(JP.WHATSAPP_TEXT);
    [].forEach.call(d.querySelectorAll("a.wa"), function (a) {
      a.href = waHref; a.target = "_blank"; a.rel = "noopener";
      a.addEventListener("click", function () { px("Contact"); ga("contact", { method: "whatsapp", page: page }); });
    });
  }

  /* ---------- thank-you pages: fire Lead only after a real submit ---------- */
  if (isThanks) {
    var flag = null;
    try { flag = sessionStorage.getItem("jp_lead_" + page); sessionStorage.removeItem("jp_lead_" + page); } catch (e) {}
    if (flag) {
      px("Lead", { content_name: page });
      if (page === "masterclass") px("CompleteRegistration", { content_name: "masterclass" });
      ga("generate_lead", { lead_type: page });
    }
    return;
  }

  /* ---------- ViewContent when a marked section scrolls into view ---------- */
  var vc = d.querySelector("[data-viewcontent]");
  if (vc && "IntersectionObserver" in window) {
    var vio = new IntersectionObserver(function (es) {
      if (es[0].isIntersecting) { px("ViewContent", { content_name: vc.getAttribute("data-viewcontent") }); vio.disconnect(); }
    }, { threshold: 0.5 });
    vio.observe(vc);
  }

  /* ---------- form ---------- */
  var form = d.getElementById("leadForm");
  if (!form) return;
  var card = d.getElementById("form");
  var bars = form.querySelectorAll(".steps-bar span");
  var err = form.querySelector(".form-err");
  var submitBtn = form.querySelector("button[type=submit]");
  var GA_SUBMIT = { demo: "demo_booking_submit", masterclass: "masterclass_register", partner: "partner_enquiry_submit" }[page];

  // UTM + source capture
  var qs = new URLSearchParams(location.search);
  ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "fbclid"].forEach(function (k) {
    var v = qs.get(k); if (!v) return;
    var i = d.createElement("input"); i.type = "hidden"; i.name = k; i.value = v.slice(0, 200); form.appendChild(i);
  });
  var sp = form.querySelector("[name=source_page]"); if (sp) sp.value = location.pathname;

  // Indian mobile: accept spaces, +91, leading 0; require 10 digits starting 6-9
  var tel = form.querySelector("input[type=tel]");
  function checkTel() {
    if (!tel) return true;
    var v = tel.value.replace(/\D/g, "");
    if (v.length > 10 && (v.indexOf("91") === 0)) v = v.slice(2);
    if (v.length === 11 && v[0] === "0") v = v.slice(1);
    var ok = /^[6-9]\d{9}$/.test(v);
    tel.setCustomValidity(tel.value && !ok ? "Enter a 10-digit Indian mobile number" : "");
    if (ok) tel.value = v;
    return ok || !tel.value;
  }
  if (tel) { tel.addEventListener("blur", checkTel); tel.addEventListener("input", function () { tel.setCustomValidity(""); }); }

  function fieldsValid(scope) {
    checkTel();
    var els = scope.querySelectorAll("input,select,textarea");
    for (var i = 0; i < els.length; i++) { if (!els[i].checkValidity()) { scope.classList.add("was-checked"); els[i].reportValidity(); return false; } }
    return true;
  }
  function setStep(n) {
    form.classList.toggle("on2", n === 2);
    if (bars.length) { bars[1].classList.toggle("on", n === 2); }
  }
  var step1 = form.querySelector(".step1");
  var next = form.querySelector("[data-next]");
  if (next) next.addEventListener("click", function () {
    if (!fieldsValid(step1)) return;
    setStep(2);
    var first = form.querySelector(".step2 input:not([type=hidden]),.step2 select");
    card.scrollIntoView({ block: "start" });
    if (first) setTimeout(function () { first.focus({ preventScroll: true }); }, 50);
    ga("form_step_2", { form: page });
  });
  var back = form.querySelector("[data-back]");
  if (back) back.addEventListener("click", function () { setStep(1); card.scrollIntoView({ block: "start" }); });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    err.classList.remove("show");
    if (!fieldsValid(form.querySelector(".step2"))) return;
    if (!fieldsValid(step1)) { setStep(1); return; }
    submitBtn.disabled = true;
    var label = submitBtn.innerHTML; submitBtn.textContent = "Sending…";
    fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
      .then(function (r) { return r.json().then(function (j) { if (!r.ok || !j.ok) { var x = new Error("x"); x.userMsg = j.error; throw x; } return j; }); })
      .then(function (j) {
        try { sessionStorage.setItem("jp_lead_" + page, "1"); } catch (x) {}
        ga(GA_SUBMIT, { lead_type: page });
        location.href = j.redirect || form.getAttribute("data-thanks");
      })
      .catch(function (x) {
        submitBtn.disabled = false; submitBtn.innerHTML = label;
        err.textContent = (x && x.userMsg ? x.userMsg : "Sorry, we couldn't send that. Please check your connection and try again.") + (JP.WHATSAPP ? " You can also message us on WhatsApp." : "");
        err.classList.add("show");
      });
  });

  /* ---------- CTA buttons that jump to the form ---------- */
  [].forEach.call(d.querySelectorAll("[data-to-form]"), function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      card.scrollIntoView({ block: "start" });
      var f = form.querySelector(form.classList.contains("on2") ? ".step2 select,.step2 input" : ".step1 input:not([type=hidden])");
      if (f) setTimeout(function () { f.focus({ preventScroll: true }); }, 400);
    });
  });

  /* ---------- sticky mobile CTA once the form is off screen ---------- */
  var sticky = d.querySelector(".sticky");
  if (sticky && "IntersectionObserver" in window) {
    new IntersectionObserver(function (es) {
      sticky.classList.toggle("show", !es[0].isIntersecting && es[0].boundingClientRect.top < 0);
    }).observe(card);
  }
})();
