// Frostad ruta: dra med musen eller fingret för att torka bort frosten.
// Frosten kryper sakta tillbaka. Respekterar "reducera rörelse".
(() => {
  const win = document.querySelector("[data-frost]");
  if (!win) return;
  const canvas = win.querySelector("canvas");
  const ctx = canvas.getContext("2d");
  const clearBtn = document.querySelector("[data-frost-clear]");
  const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

  let w = 0, h = 0, dpr = 1, texture = null, last = null, lastTouch = 0, raf = 0;

  function makeTexture() {
    const t = document.createElement("canvas");
    t.width = w; t.height = h;
    const c = t.getContext("2d");
    // Bas: is-grått frostlager
    c.fillStyle = "#D9DADF";
    c.fillRect(0, 0, w, h);
    // Kornig dimma
    const dots = Math.floor((w * h) / 90);
    for (let i = 0; i < dots; i++) {
      const x = Math.random() * w, y = Math.random() * h;
      const r = Math.random() * 1.6 * dpr;
      c.fillStyle = Math.random() < 0.5 ? "rgba(252,248,216,0.55)" : "rgba(173,172,167,0.35)";
      c.beginPath(); c.arc(x, y, r, 0, Math.PI * 2); c.fill();
    }
    // Iskristaller från kanterna
    c.strokeStyle = "rgba(252,248,216,0.7)";
    c.lineCap = "round";
    const crystal = (x, y, len, ang, depth) => {
      if (depth <= 0 || len < 4 * dpr) return;
      const x2 = x + Math.cos(ang) * len, y2 = y + Math.sin(ang) * len;
      c.lineWidth = Math.max(0.6, depth * 0.45) * dpr;
      c.beginPath(); c.moveTo(x, y); c.lineTo(x2, y2); c.stroke();
      const n = 3;
      for (let k = 1; k <= n; k++) {
        const px = x + (x2 - x) * (k / (n + 1)), py = y + (y2 - y) * (k / (n + 1));
        crystal(px, py, len * 0.42, ang + 1.05, depth - 1);
        crystal(px, py, len * 0.42, ang - 1.05, depth - 1);
      }
      crystal(x2, y2, len * 0.6, ang + (Math.random() - 0.5) * 0.4, depth - 1);
    };
    const seeds = Math.round(w / (120 * dpr)) + 4;
    for (let i = 0; i < seeds; i++) {
      const edge = i % 4;
      const sx = edge === 1 ? w : edge === 3 ? 0 : Math.random() * w;
      const sy = edge === 0 ? 0 : edge === 2 ? h : Math.random() * h;
      const toward = Math.atan2(h / 2 - sy, w / 2 - sx) + (Math.random() - 0.5) * 1.2;
      crystal(sx, sy, (40 + Math.random() * 60) * dpr, toward, 4);
    }
    return t;
  }

  function resize() {
    const r = win.getBoundingClientRect();
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = Math.round(r.width * dpr); h = Math.round(r.height * dpr);
    canvas.width = w; canvas.height = h;
    texture = makeTexture();
    ctx.globalCompositeOperation = "source-over";
    ctx.globalAlpha = 1;
    ctx.drawImage(texture, 0, 0);
  }

  function wipe(x, y, r) {
    ctx.globalCompositeOperation = "destination-out";
    ctx.globalAlpha = 1;
    const g = ctx.createRadialGradient(x, y, 0, x, y, r);
    g.addColorStop(0, "rgba(0,0,0,1)");
    g.addColorStop(0.6, "rgba(0,0,0,0.85)");
    g.addColorStop(1, "rgba(0,0,0,0)");
    ctx.fillStyle = g;
    ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fill();
  }

  function stroke(x, y) {
    const r = Math.max(36, Math.min(w, h) * 0.09);
    if (last) {
      const dx = x - last.x, dy = y - last.y, dist = Math.hypot(dx, dy);
      const steps = Math.ceil(dist / (r * 0.25));
      for (let i = 1; i <= steps; i++) wipe(last.x + (dx * i) / steps, last.y + (dy * i) / steps, r);
    } else wipe(x, y, r);
    last = { x, y };
    lastTouch = performance.now();
    if (!reduce) loop();
  }

  // Frosten kryper tillbaka i ca 15 s efter senaste beröring
  function loop() {
    if (raf) return;
    const tick = (t) => {
      if (t - lastTouch > 15000) { raf = 0; return; }
      if (t - lastTouch > 1200) {
        ctx.globalCompositeOperation = "source-over";
        ctx.globalAlpha = 0.012;
        ctx.drawImage(texture, 0, 0);
      }
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
  }

  const pos = (e) => {
    const r = canvas.getBoundingClientRect();
    return { x: (e.clientX - r.left) * dpr, y: (e.clientY - r.top) * dpr };
  };
  canvas.addEventListener("pointermove", (e) => {
    if (e.pointerType === "mouse" || e.buttons || e.pressure > 0) { const p = pos(e); stroke(p.x, p.y); }
  });
  canvas.addEventListener("pointerdown", (e) => { last = null; const p = pos(e); stroke(p.x, p.y); });
  canvas.addEventListener("pointerleave", () => { last = null; });
  canvas.addEventListener("pointerup", () => { last = null; });

  clearBtn?.addEventListener("click", () => {
    ctx.globalCompositeOperation = "destination-out";
    ctx.globalAlpha = 1;
    ctx.fillRect(0, 0, w, h);
    lastTouch = performance.now();
    if (!reduce) loop();
  });

  let rt;
  addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(resize, 150); });
  resize();

  // Ett enda inledande torkdrag som visar att rutan går att torka
  if (!reduce) {
    let start = 0; const dur = 900;
    const path = (k) => ({ x: w * (0.06 + 0.5 * k), y: h * (0.78 - 0.22 * Math.sin(k * Math.PI)) });
    const intro = (t) => {
      const k = Math.min(1, (t - start) / dur);
      const p = path(k); stroke(p.x, p.y);
      if (k < 1) requestAnimationFrame(intro); else last = null;
    };
    setTimeout(() => { start = performance.now(); requestAnimationFrame(intro); }, 500);
  }
})();
