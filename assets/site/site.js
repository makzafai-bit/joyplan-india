/* JoyPlan India: main site script. No dependencies.
   SETTINGS: WhatsApp business number (digits with country code, e.g. "919876543210").
   Empty keeps number-less wa.me links that open WhatsApp with the message pre-filled. */
var JPS = {
  WHATSAPP: "",
  PRICES: { deviceOnly: 8474, app: { 1: 1000, 3: 2950, 6: 5500, 12: 9500 }, dev: { 1: 6500, 3: 8450, 6: 11000, 12: 15000 } }
};

(function () {
  "use strict";
  var d = document, root = d.documentElement, body = d.body;
  root.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };
  var inr = function (n) { return "₹" + Number(n).toLocaleString("en-IN"); };

  /* ---------- WhatsApp links ---------- */
  function waHref(text) {
    return "https://wa.me/" + (JPS.WHATSAPP || "") + "?text=" + encodeURIComponent(text || "Hi JoyPlan India, I'd like to book a demo.");
  }
  $$("[data-wa]").forEach(function (a) {
    a.href = waHref(a.getAttribute("data-wa"));
    a.target = "_blank"; a.rel = "noopener";
  });

  /* ---------- load sequence ---------- */
  requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add("ready"); }); });

  /* ---------- page wipe ---------- */
  var wipe = $(".pwipe");
  if (wipe && !reduce) {
    try { if (sessionStorage.getItem("jp-wipe")) { wipe.classList.add("out"); sessionStorage.removeItem("jp-wipe"); } } catch (e) {}
    d.addEventListener("click", function (e) {
      var a = e.target.closest && e.target.closest("a[href]");
      if (!a || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey || a.target === "_blank" || a.hasAttribute("download")) return;
      var url = new URL(a.href, location.href);
      if (url.origin !== location.origin || url.pathname === location.pathname || /\.(php|pdf|svg|xml)$/.test(url.pathname)) return;
      e.preventDefault();
      try { sessionStorage.setItem("jp-wipe", "1"); } catch (e2) {}
      wipe.classList.remove("out"); wipe.classList.add("go");
      setTimeout(function () { location.href = a.href; }, 520);
    });
    window.addEventListener("pageshow", function (e) { if (e.persisted) { wipe.className = "pwipe"; } });
  }

  /* ---------- sticky nav: hide on scroll down ---------- */
  var nav = $(".nav"), lastY = window.scrollY;
  window.addEventListener("scroll", function () {
    var y = window.scrollY;
    if (!nav) return;
    var hide = y > 600 && y > lastY + 4 && !body.classList.contains("locked");
    var show = y < lastY - 4 || y < 600;
    if (hide) { nav.classList.add("hide"); body.classList.add("nav-hidden"); }
    else if (show) { nav.classList.remove("hide"); body.classList.remove("nav-hidden"); }
    lastY = y;
  }, { passive: true });

  /* ---------- mobile menu ---------- */
  var menu = $("#menu"), burger = $(".burger");
  function trap(container, e) {
    var f = $$("a[href],button:not([disabled]),input,select,textarea", container).filter(function (x) { return x.offsetParent !== null; });
    if (!f.length) return;
    if (e.shiftKey && d.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && d.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
  }
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle("open", open);
    menu.setAttribute("aria-hidden", open ? "false" : "true");
    burger.setAttribute("aria-expanded", open ? "true" : "false");
    body.classList.toggle("locked", open);
    if (open) { setTimeout(function () { $(".menu-close", menu).focus(); }, 50); } else { burger.focus(); }
  }
  if (menu && burger) {
    burger.addEventListener("click", function () { setMenu(true); });
    $(".menu-close", menu).addEventListener("click", function () { setMenu(false); });
    d.addEventListener("keydown", function (e) { if (!menu.classList.contains("open")) return; if (e.key === "Escape") setMenu(false); if (e.key === "Tab") trap(menu, e); });
    $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { if (a.hash && a.pathname === location.pathname) setMenu(false); }); });
  }

  /* ---------- reveal on scroll ---------- */
  var io = "IntersectionObserver" in window ? new IntersectionObserver(function (ents) {
    ents.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
  }, { rootMargin: "0px 0px -15% 0px" }) : null;
  $$(".rv,.wipe,.ben-row,.plan2d.anim,[data-inview]").forEach(function (el) { if (io && !reduce) io.observe(el); else el.classList.add("in"); });
  // stagger children
  $$("[data-stagger]").forEach(function (g) { $$(".rv", g).forEach(function (el, i) { el.style.setProperty("--d", i); }); });

  /* ---------- hero iso plan: rise from flat ---------- */
  $$(".iso[data-rise]").forEach(function (iso) {
    if (reduce) return;
    iso.classList.add("flat", "draw");
    setTimeout(function () { iso.classList.remove("flat"); }, 500);
  });
  // hero scroll parallax
  var heroCopy = $(".hero [data-parallax-copy]"), heroVis = $(".hero [data-parallax-vis]");
  if ((heroCopy || heroVis) && !reduce && window.innerWidth > 1000) {
    window.addEventListener("scroll", function () {
      var y = Math.min(window.scrollY, 800), p = y / 800;
      if (heroCopy) { heroCopy.style.transform = "translateY(" + (-y * 0.18) + "px)"; heroCopy.style.opacity = String(1 - p * 0.75); }
      if (heroVis) heroVis.style.transform = "translateY(" + (y * 0.08) + "px)";
    }, { passive: true });
  }
  $$("[data-parallax]").forEach(function (el) {
    if (reduce) return;
    var amt = parseFloat(el.getAttribute("data-parallax")) || 60;
    window.addEventListener("scroll", function () {
      var r = el.parentElement.getBoundingClientRect();
      var p = (r.top + r.height / 2 - window.innerHeight / 2) / window.innerHeight;
      el.style.transform = "translateY(" + (p * amt) + "px)";
    }, { passive: true });
  });

  /* ---------- before / after sliders ---------- */
  $$(".ba").forEach(function (ba) {
    var input = $("input", ba);
    function set(v) { ba.style.setProperty("--x", v + "%"); }
    input.addEventListener("input", function () { set(input.value); });
    set(input.value);
  });

  /* ---------- tabs helper ---------- */
  function tabs(rootEl, btnSel, panelSel, onChange) {
    var btns = $$(btnSel, rootEl), panels = panelSel ? $$(panelSel, rootEl) : [];
    function go(i, user) {
      btns.forEach(function (b, j) { b.setAttribute("aria-selected", j === i ? "true" : "false"); b.tabIndex = j === i ? 0 : -1; });
      panels.forEach(function (p, j) { p.classList.toggle("on", j === i); p.setAttribute("aria-hidden", j === i ? "false" : "true"); });
      if (onChange) onChange(i, user);
    }
    btns.forEach(function (b, i) {
      b.addEventListener("click", function () { go(i, true); });
      b.addEventListener("keydown", function (e) {
        var k = e.key, n = null;
        if (k === "ArrowRight" || k === "ArrowDown") n = (i + 1) % btns.length;
        if (k === "ArrowLeft" || k === "ArrowUp") n = (i - 1 + btns.length) % btns.length;
        if (n !== null) { e.preventDefault(); btns[n].focus(); go(n, true); }
      });
    });
    return go;
  }

  /* ---------- workflow stages (auto-advance) ---------- */
  $$("[data-workflow]").forEach(function (wf) {
    var rail = $(".wf-rail", wf), n = $$(".wf-rail button", wf).length, cur = 0, timer = null, pauseT = null, visible = false;
    var go = tabs(wf, ".wf-rail button", ".wf-scene", function (i, user) {
      cur = i;
      $$(".wf-scene", wf).forEach(function (s, j) { if (j === i) $$(".plan2d.anim", s).forEach(function (p) { p.classList.remove("in"); void p.offsetWidth; p.classList.add("in"); }); });
      $$(".iso", $$(".wf-scene", wf)[i]).forEach(function (iso) { iso.classList.add("flat"); setTimeout(function () { iso.classList.remove("flat"); }, 250); });
      if (user) { rail.classList.add("paused"); clearTimeout(pauseT); stop(); pauseT = setTimeout(function () { rail.classList.remove("paused"); start(); }, 15000); }
    });
    function start() { stop(); if (reduce || !visible) return; timer = setInterval(function () { go((cur + 1) % n); }, 5000); }
    function stop() { clearInterval(timer); }
    if (reduce) rail.classList.add("paused");
    if (io) new IntersectionObserver(function (e) { visible = e[0].isIntersecting; if (visible && !rail.classList.contains("paused")) { go(cur); start(); } else stop(); }, { threshold: 0.3 }).observe(wf);
    go(0);
  });

  /* ---------- feature explorer ---------- */
  $$("[data-explorer]").forEach(function (ex) {
    var info = $$(".fx-text", ex);
    tabs(ex, ".fx-list button", ".fx-scr", function (i) {
      info.forEach(function (t, j) { t.hidden = j !== i; });
    })(0);
  });

  /* generic tab sets */
  $$("[data-tabs]").forEach(function (t) { tabs(t, "[role=tab]", "[role=tabpanel]")(0); });

  /* ---------- material swatches recolour the sofa ---------- */
  $$("[data-swatches]").forEach(function (sw) {
    var target = d.getElementById(sw.getAttribute("data-swatches"));
    $$("button", sw).forEach(function (b) {
      b.addEventListener("click", function () {
        $$("button", sw).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        if (target) $$(".sofa", target).forEach(function (p) { p.style.fill = b.getAttribute("data-c"); });
      });
    });
  });

  /* ---------- hotspots ---------- */
  $$("[data-hotspots]").forEach(function (h) {
    var t = $(".hcap .t", h), p = $(".hcap p:not(.t)", h);
    $$(".hot", h).forEach(function (b) {
      b.addEventListener("click", function () {
        $$(".hot", h).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        p.style.opacity = 0;
        setTimeout(function () { t.textContent = b.getAttribute("data-t"); p.textContent = b.getAttribute("data-c"); p.style.opacity = 1; }, 180);
      });
    });
  });

  /* ---------- 2D / 3D toggle on a tablet ---------- */
  $$("[data-dim-toggle]").forEach(function (box) {
    var iso = $(".iso, .dimswap", box);
    $$("[data-dim]", box).forEach(function (b) {
      b.addEventListener("click", function () {
        $$("[data-dim]", box).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        iso.classList.toggle("flat", b.getAttribute("data-dim") === "2d");
      });
    });
  });

  /* ---------- 2D to 3D range ---------- */
  $$("[data-tilt-range]").forEach(function (r) {
    var iso = d.getElementById(r.getAttribute("data-tilt-range")), out = d.getElementById(r.getAttribute("data-out"));
    function set() { var v = r.value / 100; iso.style.setProperty("--t", v); if (out) out.textContent = r.value + "%"; }
    r.addEventListener("input", set); set();
  });

  /* ---------- device: pointer tilt + LCD cycle ---------- */
  $$("[data-tilt]").forEach(function (el) {
    if (reduce || window.matchMedia("(hover: none)").matches) return;
    var box = el.closest("[data-tilt-area]") || el.parentElement;
    box.addEventListener("pointermove", function (e) {
      var r = box.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
      el.style.transform = "rotateY(" + (x * 30) + "deg) rotateX(" + (-y * 15) + "deg)";
    });
    box.addEventListener("pointerleave", function () { el.style.transform = ""; });
  });
  $$("[data-lcd]").forEach(function (b) {
    if (reduce) return;
    var vals = b.getAttribute("data-lcd").split(","), i = 0;
    setInterval(function () { i = (i + 1) % vals.length; b.textContent = vals[i]; }, 2200);
  });

  /* ---------- hero device: measure, count up to the reading, hold, repeat ---------- */
  $$(".dev.count .lcd b").forEach(function (b) {
    var target = 4.625;
    function show(v) { b.textContent = v.toFixed(3); }
    if (reduce) { show(target); return; }
    function measure() {
      var t0 = null, dur = 1300;
      b.parentNode.classList.add("busy");
      function step(ts) {
        if (!t0) t0 = ts;
        var k = Math.min(1, (ts - t0) / dur), e = 1 - Math.pow(1 - k, 3);
        show(target * e);
        if (k < 1) requestAnimationFrame(step); else b.parentNode.classList.remove("busy");
      }
      show(0); requestAnimationFrame(step);
    }
    setTimeout(measure, 900);
    setInterval(measure, 6000);
  });

  /* ---------- pricing toggle ---------- */
  $$("[data-pricing]").forEach(function (pr) {
    var btns = $$(".seg button", pr);
    function set(term, user) {
      btns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-term") === String(term) ? "true" : "false"); });
      $$("[data-price]", pr).forEach(function (el) {
        var key = el.getAttribute("data-price"), v = JPS.PRICES[key][term];
        var span = d.createElement("span"); span.textContent = inr(v); if (user) span.className = "swap";
        el.innerHTML = ""; el.appendChild(span);
      });
      $$("[data-term-label]", pr).forEach(function (el) { el.textContent = el.getAttribute("data-term-label") + " · " + term + (term === 1 ? " month" : " months"); });
      $$("[data-pkg-link]", pr).forEach(function (a) { var u = a.getAttribute("data-pkg-link"); a.href = "/book-a-demo/?package=" + u + "-" + term; });
    }
    btns.forEach(function (b) { b.addEventListener("click", function () { set(+b.getAttribute("data-term"), true); }); });
    set(12, false);
  });
  $$("[data-toggle]").forEach(function (b) {
    var t = d.getElementById(b.getAttribute("data-toggle"));
    b.setAttribute("aria-expanded", "false");
    b.addEventListener("click", function () { var open = t.hidden; t.hidden = !open; b.setAttribute("aria-expanded", open ? "true" : "false"); });
  });

  /* ---------- full price grid selection ---------- */
  $$("[data-pgrid]").forEach(function (g) {
    var out = d.getElementById(g.getAttribute("data-pgrid"));
    $$("button", g).forEach(function (b) {
      b.addEventListener("click", function () {
        $$("button", g).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        var term = +b.getAttribute("data-term"), kind = b.getAttribute("data-kind");
        $(".sel-name", out).textContent = (kind === "dev" ? "Device + app" : "App only") + " · " + term + (term === 1 ? " month" : " months");
        var v = $(".sel-price", out); v.innerHTML = "<span class=swap>" + inr(JPS.PRICES[kind][term]) + "</span>";
        $("a", out).href = "/book-a-demo/?package=" + (kind === "dev" ? "device" : "app") + "-" + term;
      });
    });
  });

  /* ---------- gallery filter + lightbox ---------- */
  $$("[data-gallery]").forEach(function (gal) {
    var tiles = $$(".gt", gal), chips = $$("[data-filter]", gal.parentElement);
    chips.forEach(function (c) {
      c.addEventListener("click", function () {
        var f = c.getAttribute("data-filter");
        chips.forEach(function (x) { x.setAttribute("aria-pressed", x === c ? "true" : "false"); });
        tiles.forEach(function (t) { t.hidden = !(f === "all" || (" " + t.getAttribute("data-f") + " ").indexOf(" " + f + " ") > -1); });
      });
    });
    var lb = $("#lightbox"), last = null;
    if (!lb) return;
    function close() { lb.classList.remove("open"); lb.setAttribute("aria-hidden", "true"); body.classList.remove("locked"); if (last) last.focus(); }
    tiles.forEach(function (t) {
      t.addEventListener("click", function () {
        last = t;
        $(".im", lb).innerHTML = $(".im", t).innerHTML;
        $(".lb-t", lb).textContent = $(".cap b", t).textContent;
        $(".lb-c", lb).textContent = $(".cap i", t).textContent;
        lb.classList.add("open"); lb.setAttribute("aria-hidden", "false"); body.classList.add("locked");
        setTimeout(function () { $(".lb-x", lb).focus(); }, 30);
      });
    });
    $(".lb-x", lb).addEventListener("click", close);
    lb.addEventListener("click", function (e) { if (e.target === lb) close(); });
    d.addEventListener("keydown", function (e) { if (!lb.classList.contains("open")) return; if (e.key === "Escape") close(); if (e.key === "Tab") trap(lb, e); });
  });

  /* ---------- features page filter ---------- */
  var flib = $("[data-flib]");
  if (flib) {
    var rows = $$(".frow", flib), fbtns = $$("[data-ffilter]");
    function setF(f, scroll) {
      fbtns.forEach(function (b) { b.setAttribute("aria-pressed", b.getAttribute("data-ffilter") === f ? "true" : "false"); });
      rows.forEach(function (r) { r.hidden = !(f === "all" || r.getAttribute("data-cat") === f); });
      if (scroll) { var t = $(".sticky-filter"); window.scrollTo({ top: t.getBoundingClientRect().top + window.scrollY - (nav ? nav.offsetHeight : 0) + 2, behavior: reduce ? "auto" : "smooth" }); }
    }
    fbtns.forEach(function (b) { b.addEventListener("click", function () { setF(b.getAttribute("data-ffilter"), b.closest(".stage-bar") !== null); }); });
  }

  /* ---------- solutions sticky tabs ---------- */
  var ptabs = $(".ptabs");
  if (ptabs && io) {
    var links = $$("a", ptabs);
    var secs = links.map(function (a) { return d.getElementById(a.hash.slice(1)); });
    var tio = new IntersectionObserver(function (ents) {
      ents.forEach(function (en) {
        if (!en.isIntersecting) return;
        var i = secs.indexOf(en.target);
        links.forEach(function (l, j) { l.classList.toggle("on", i === j); });
        var on = links[i]; if (on) ptabs.querySelector(".wrap").scrollTo({ left: on.offsetLeft - 40, behavior: "smooth" });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    secs.forEach(function (s) { if (s) tio.observe(s); });
  }

  /* ---------- software callouts ---------- */
  $$("[data-callouts]").forEach(function (c) {
    var nums = $$(".cnum", d.getElementById(c.getAttribute("data-callouts")));
    $$("button", c).forEach(function (b, i) {
      b.addEventListener("click", function () {
        $$("button", c).forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
        nums.forEach(function (n, j) { n.classList.toggle("on", i === j); });
      });
    });
  });

  /* ---------- panorama drag ---------- */
  $$(".pano").forEach(function (p) {
    var inner = $(".pano-in", p), bar = p.parentElement.querySelector(".pano-bar i"), x = 0, sx = 0, down = false, startX = 0;
    function wrapX() { var w = inner.offsetWidth / 2; x = ((x % w) - w) % w; inner.style.transform = "translateX(" + x + "px)"; if (bar) bar.style.left = (Math.abs(x) / w * 75) + "%"; }
    p.addEventListener("pointerdown", function (e) { down = true; startX = e.clientX; sx = x; p.setPointerCapture(e.pointerId); });
    p.addEventListener("pointermove", function (e) { if (!down) return; x = sx + (e.clientX - startX); wrapX(); });
    p.addEventListener("pointerup", function () { down = false; });
    p.addEventListener("keydown", function (e) { if (e.key === "ArrowLeft") { x += 40; wrapX(); } if (e.key === "ArrowRight") { x -= 40; wrapX(); } });
    if (!reduce) { var auto = setInterval(function () { if (!down) { x -= 0.4; wrapX(); } }, 30); p.addEventListener("pointerdown", function () { clearInterval(auto); }, { once: true }); }
    wrapX();
  });

  /* ---------- phone panorama: drag to look around (clamped) ---------- */
  $$(".ph-pano").forEach(function (p) {
    var inner = $(".ph-in", p), scr = $(".ph-scr", p), x = 0, sx = 0, startX = 0, down = false, dir = -1, auto = null;
    function max() { return Math.max(0, inner.offsetWidth - scr.offsetWidth); }
    function set() { x = Math.min(0, Math.max(-max(), x)); inner.style.transform = "translateX(" + x + "px)"; }
    function stop() { if (auto) { clearInterval(auto); auto = null; } }
    p.addEventListener("pointerdown", function (e) { stop(); down = true; startX = e.clientX; sx = x; p.setPointerCapture(e.pointerId); });
    p.addEventListener("pointermove", function (e) { if (down) { x = sx + (e.clientX - startX); set(); } });
    p.addEventListener("pointerup", function () { down = false; });
    p.addEventListener("pointercancel", function () { down = false; });
    p.addEventListener("keydown", function (e) { if (e.key === "ArrowLeft") { stop(); x += 30; set(); } if (e.key === "ArrowRight") { stop(); x -= 30; set(); } });
    if (!reduce) auto = setInterval(function () { x += dir * 0.5; if (x <= -max()) dir = 1; if (x >= 0) dir = -1; set(); }, 30);
    set();
  });

  /* ---------- chips (single-select groups bound to hidden inputs) ---------- */
  $$("[data-chips]").forEach(function (g) {
    var input = d.getElementsByName(g.getAttribute("data-chips"))[0];
    $$(".chip", g).forEach(function (c) {
      c.addEventListener("click", function () {
        $$(".chip", g).forEach(function (x) { x.setAttribute("aria-pressed", x === c ? "true" : "false"); });
        if (input) input.value = c.getAttribute("data-v") || c.textContent.trim();
      });
    });
  });

  /* ---------- forms ---------- */
  var KERALA = /kerala|kozhikode|calicut|kochi|cochin|ernakulam|trivandrum|thiruvananthapuram|thrissur|kannur|malappuram|palakkad|kollam|alappuzha|kottayam|kasaragod|wayanad|pathanamthitta|idukki/i;
  var params = new URLSearchParams(location.search);
  $$("form[data-lead]").forEach(function (f) {
    // utm + source tracking
    ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "fbclid"].forEach(function (k) {
      if (params.get(k)) { var h = d.createElement("input"); h.type = "hidden"; h.name = k; h.value = params.get(k); f.appendChild(h); }
    });
    var src = d.createElement("input"); src.type = "hidden"; src.name = "source_page"; src.value = location.pathname; f.appendChild(src);
    var pkg = params.get("package");
    if (pkg) {
      if (f.package) f.package.value = pkg;
      var sel = f.querySelector("select[name=product]");
      if (sel) { var map = { starter: "Software only (Starter)", professional: "Device + Software (Professional)", business: "Business / studio package" }; var key = pkg.split("-")[0]; if (/^device/.test(pkg)) key = "professional"; if (/^app/.test(pkg)) key = "starter"; if (map[key]) sel.value = map[key]; }
      var chipG = f.querySelector("[data-chips=interest]");
      if (chipG) { var want = /^business/.test(pkg) ? "Business / studio" : /^(starter|app)/.test(pkg) ? "Software only" : "Device + Software"; $$(".chip", chipG).forEach(function (c) { if (c.textContent.trim() === want) c.click(); }); }
    }
    var prof = params.get("profession");
    if (prof) { var pg = f.querySelector("[data-chips=profession]"); if (pg) $$(".chip", pg).forEach(function (c) { if (c.textContent.trim().toLowerCase() === prof.toLowerCase()) c.click(); }); }
    var msg = $(".form-msg", f);
    function validate() {
      var ok = true;
      $$("[required]", f).forEach(function (el) {
        var fld = el.closest(".field"), bad = !el.value.trim();
        if (el.name === "mobile" && !bad) { var dg = el.value.replace(/\D/g, ""); if (dg.length > 10 && dg.indexOf("91") === 0) dg = dg.slice(2); if (dg.length === 11 && dg[0] === "0") dg = dg.slice(1); bad = !/^[6-9]\d{9}$/.test(dg); }
        if (fld) fld.classList.toggle("bad", bad);
        if (bad && ok) { el.focus(); ok = false; }
      });
      return ok;
    }
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      if (msg) msg.textContent = "";
      if (!validate()) return;
      var city = (f.city && f.city.value) || "";
      f.nearest_team.value = KERALA.test(city) ? "Kozhikode" : "Bengaluru";
      var btn = $("button[type=submit]", f); btn.disabled = true;
      var fd = new FormData(f);
      fetch(f.action, { method: "POST", body: fd, headers: { Accept: "application/json" } })
        .then(function (r) { return r.json().catch(function () { return { ok: false, error: "Something went wrong. Please try again or message us on WhatsApp." }; }); })
        .then(function (res) {
          btn.disabled = false;
          if (!res.ok) { if (msg) msg.textContent = res.error || "Please check the form and try again."; return; }
          var th = d.getElementById(f.getAttribute("data-thanks"));
          var first = (f.full_name.value || "").trim().split(/\s+/)[0];
          $$("[data-first]", th).forEach(function (x) { x.textContent = first; });
          $$("[data-sum]", th).forEach(function (x) { var k = x.getAttribute("data-sum"); x.textContent = k === "nearest_team" ? f.nearest_team.value + " team" : (fd.get(k) || "Not given"); });
          f.hidden = true; th.classList.add("on"); th.setAttribute("tabindex", "-1"); th.focus();
          if (window.fbq) fbq("track", "Lead");
          if (window.gtag) gtag("event", "form_submit", { profession: fd.get("profession"), city: city });
        })
        .catch(function () { btn.disabled = false; if (msg) msg.textContent = "We couldn't send that just now. Please try again, or message us on WhatsApp."; });
    });
    $$("input,select", f).forEach(function (el) { el.addEventListener("input", function () { var fld = el.closest(".field"); if (fld) fld.classList.remove("bad"); }); });
  });
  $$("[data-reset]").forEach(function (b) {
    b.addEventListener("click", function () {
      var th = b.closest(".thanks"), f = d.getElementById(b.getAttribute("data-reset"));
      th.classList.remove("on"); f.reset(); f.hidden = false; f.querySelector("input:not([type=hidden])").focus();
    });
  });
})();
