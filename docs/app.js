/* Every Good Regulator — reading site behaviour.
   Every feature is optional: if any part fails, the page stays a plain, readable document. */
(function () {
  "use strict";
  var doc = document.documentElement;
  var body = document.body;
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function safe(fn) { try { fn(); } catch (e) { if (window.console) console.warn("egr:", e); } }

  // ---------- theme ----------
  safe(function () {
    var btns = document.querySelectorAll(".theme-btn");
    function isDark() {
      var t = doc.dataset.theme;
      if (t) return t === "dark";
      return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    }
    btns.forEach(function (b) {
      b.addEventListener("click", function () {
        var next = isDark() ? "light" : "dark";
        doc.dataset.theme = next;
        store("egr-theme", next);
      });
    });
  });

  // ---------- reveal on scroll ----------
  safe(function () {
    var els = document.querySelectorAll(".reveal");
    if (!els.length) return;
    if (reduce || !("IntersectionObserver" in window)) { els.forEach(function (e) { e.classList.add("in"); }); return; }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.06 });
    els.forEach(function (e) { io.observe(e); });
    // safety net: never leave content hidden
    setTimeout(function () { els.forEach(function (e) { e.classList.add("in"); }); }, 4000);
  });

  // ---------- reading progress + header state (one rAF per frame at most) ----------
  safe(function () {
    var bar = document.querySelector(".progress span");
    var top = document.querySelector(".topbar-home");
    var ticking = false;
    function update() {
      ticking = false;
      var h = doc.scrollHeight - window.innerHeight;
      var p = h > 0 ? Math.min(1, Math.max(0, window.scrollY / h)) : 0;
      if (bar) bar.style.transform = "scaleX(" + p.toFixed(4) + ")";
      if (top) top.classList.toggle("scrolled", window.scrollY > 10);
    }
    window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    window.addEventListener("resize", update, { passive: true });
    update();
  });

  // ---------- contents drawer (mobile) ----------
  safe(function () {
    var btn = document.querySelector(".menu-btn");
    var scrim = document.querySelector(".scrim");
    var toc = document.getElementById("toc");
    if (!btn || !toc) return;
    function set(open) {
      body.classList.toggle("toc-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      if (scrim) scrim.hidden = !open;
      if (open) { var cur = toc.querySelector(".current a") || toc.querySelector("a"); if (cur) cur.focus({ preventScroll: true }); }
    }
    btn.addEventListener("click", function () { set(!body.classList.contains("toc-open")); });
    if (scrim) scrim.addEventListener("click", function () { set(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && body.classList.contains("toc-open")) { set(false); btn.focus(); } });
    // keep the current chapter visible in the sidebar
    var cur = toc.querySelector(".current");
    if (cur && cur.scrollIntoView) cur.scrollIntoView({ block: "center" });
  });

  // ---------- download menu closes on outside click ----------
  safe(function () {
    var dl = document.querySelector("details.dl");
    if (!dl) return;
    document.addEventListener("click", function (e) { if (dl.open && !dl.contains(e.target)) dl.open = false; });
  });

  // ---------- image lightbox ----------
  safe(function () {
    var box = document.querySelector("dialog.lightbox");
    if (!box || typeof box.showModal !== "function") return;
    var frame = box.querySelector(".lb-frame");
    var cap = box.querySelector(".lb-cap");
    document.querySelectorAll(".prose img").forEach(function (img) {
      img.setAttribute("tabindex", "0");
      img.setAttribute("role", "button");
      function open() {
        while (frame.firstChild) frame.removeChild(frame.firstChild);
        var big = new Image();
        big.src = img.currentSrc || img.src;
        big.alt = img.alt || "";
        frame.appendChild(big);
        cap.textContent = img.alt || "";
        box.showModal();
      }
      img.addEventListener("click", open);
      img.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); open(); } });
    });
    box.addEventListener("click", function (e) { if (e.target === box || e.target.closest(".close")) box.close(); });
    box.addEventListener("close", function () { while (frame.firstChild) frame.removeChild(frame.firstChild); });
  });

  // ---------- keyboard: ← / → between chapters ----------
  safe(function () {
    var prev = document.querySelector(".pager .prev");
    var next = document.querySelector(".pager .next");
    document.addEventListener("keydown", function (e) {
      if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
      var t = e.target;
      if (t && (t.isContentEditable || /INPUT|TEXTAREA|SELECT/.test(t.tagName))) return;
      if (document.querySelector("dialog[open]") || body.classList.contains("toc-open")) return;
      if (e.key === "ArrowLeft" && prev) location.href = prev.href;
      if (e.key === "ArrowRight" && next) location.href = next.href;
    });
  });

  // ---------- remember where the reader was ----------
  safe(function () {
    var page = location.pathname.split("/").pop() || "index.html";
    if (body.classList.contains("reader")) {
      store("egr-last", page);
      var key = "egr-pos:" + page;
      var saved = parseFloat(store(key) || "0");
      if (saved > 0.02 && saved < 0.98 && !location.hash) {
        requestAnimationFrame(function () { window.scrollTo(0, saved * (doc.scrollHeight - window.innerHeight)); });
      }
      var t = null;
      window.addEventListener("scroll", function () {
        clearTimeout(t);
        t = setTimeout(function () {
          var h = doc.scrollHeight - window.innerHeight;
          if (h > 0) store(key, (window.scrollY / h).toFixed(3));
        }, 400);
      }, { passive: true });
    } else {
      var last = store("egr-last");
      var resume = document.querySelector(".resume");
      if (last && resume && /^[a-z0-9-]+\.html$/.test(last)) { resume.href = last; resume.hidden = false; }
    }
  });
})();
