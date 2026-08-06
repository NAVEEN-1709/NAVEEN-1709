```html
<!-- name=README.md -->
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<title>NAVEEN KUMAR — Developer</title>
<style>
  :root{
    --bg:#0d1117;
    --card: rgba(255,255,255,0.04);
    --muted: #9aa4b2;
    --accent-pink: #ff4ecd;
    --accent-purple: #8b5cf6;
    --accent-blue: #38bdf8;
    --glass: rgba(255,255,255,0.03);
    --glass-2: rgba(255,255,255,0.02);
    color-scheme: dark;
  }
  html,body{height:100%;margin:0;background:var(--bg);font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial;display:flex;align-items:center;justify-content:center}
  .wrap{max-width:980px;padding:28px;text-align:center;color:#dbe7ff;}
  .centered{margin:0 auto;display:flex;flex-direction:column;gap:22px;align-items:center;justify-content:center}
  .banner{width:100%;border-radius:18px;overflow:hidden;box-shadow:0 10px 30px rgba(2,6,23,0.7);border:1px solid rgba(255,255,255,0.03)}
  .meta{display:flex;gap:12px;align-items:center;justify-content:center;flex-wrap:wrap}
  .pill{background:linear-gradient(90deg,var(--accent-pink),var(--accent-purple));padding:8px 14px;border-radius:999px;color:#041024;font-weight:600;box-shadow:0 6px 18px rgba(139,92,246,0.12);font-size:13px}
  .typed{font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, monospace; color:#bfe7ff; background:rgba(255,255,255,0.02); padding:8px 12px;border-radius:8px; display:inline-block}
  .section{width:100%;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); border-radius:12px;padding:18px}
  .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;align-items:start}
  @media (max-width:880px){.grid{grid-template-columns:1fr}}
  .skills{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}
  .skill{background:var(--glass);padding:10px 14px;border-radius:12px;color:#e9f2ff;font-weight:600;transition:transform .28s,box-shadow .28s}
  .skill:hover{transform:translateY(-6px);box-shadow:0 18px 40px rgba(56,189,248,0.12)}
  .icons{display:flex;gap:8px;justify-content:center;align-items:center}
  .svg-inline{max-width:100%;height:auto;display:block;margin:0 auto}
  .centerlinks{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
  a.badge{display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:10px;background:linear-gradient(90deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));color:#dbe7ff;text-decoration:none}
  /* Typing animations */
  .typewriter{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,monospace; color:#bfe7ff; display:inline-block; overflow:hidden; border-right:.14em solid rgba(190,231,255,0.4); white-space:nowrap; letter-spacing:.03em; animation:typing 3s steps(30,end) infinite, blink-caret .7s step-end infinite}
  @keyframes typing{0%{width:0}50%{width:22ch}100%{width:22ch}}
  @keyframes blink-caret{50%{border-color:transparent}}
  /* simple center footer */
  footer{margin-top:18px;color:var(--muted);font-size:13px}
  /* light theme switch preview inside README uses picture element */
  /* small counters */
  .footer-row{display:flex;gap:12px;justify-content:center;align-items:center;flex-wrap:wrap;margin-top:10px}
  .footer-row img{height:34px;border-radius:8px}
  .lead{color:#e4f3ff;font-size:15px}
  .about-list{list-style:none;padding:0;margin:12px 0;display:inline-block;text-align:left}
  .about-list li{padding:6px 0}
  .stats-row{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
  .stat-card{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));padding:10px 14px;border-radius:12px;min-width:120px}
</style>
</head>
<body>
  <div class="wrap">
    <div class="centered">
      <!-- Banner with dark/light using local assets -->
      <picture class="banner">
        <source srcset="./assets/banner-light.svg?v=1" media="(prefers-color-scheme:light)">
        <img src="./assets/banner.svg?v=1" alt="NAVEEN KUMAR banner" style="width:100%;height:auto;display:block">
      </picture>

      <div style="height:16px"></div>

      <div class="meta">
        <div class="pill">NAVEEN KUMAR</div>
        <div class="pill">Developer</div>
        <div class="pill">MCA</div>
        <div class="typed">"Turning ideas into intelligent software, one commit at a time."</div>
      </div>

      <div style="height:14px"></div>

      <div class="section grid" role="region" aria-label="about and skills">
        <div>
          <h3 style="margin:0;color:#fff">About Me</h3>
          <p class="lead">I build thoughtful, well-tested software and delightful front-end experiences. Always learning, building AURA AI, and contributing to open-source.</p>
          <ul class="about-list">
            <li>• MCA Graduate</li>
            <li>• Python Developer</li>
            <li>• Web Development</li>
            <li>• Always Learning</li>
            <li>• Building AURA AI</li>
          </ul>

          <div style="height:10px"></div>

          <h4 style="margin-bottom:8px">Tech Stack</h4>
          <div class="skills" aria-hidden="false">
            <span class="skill">Python</span>
            <span class="skill">JavaScript</span>
            <span class="skill">HTML</span>
            <span class="skill">CSS</span>
            <span class="skill">SQL</span>
          </div>

          <div style="height:12px"></div>

          <h4 style="margin-bottom:8px">Contact</h4>
          <div class="centerlinks">
            <a class="badge" href="mailto:nk9997201@gmail.com">✉️ Email</a>
            <a class="badge" href="https://linkedin.com/in/your-linkedin" target="_blank" rel="noopener">🔗 LinkedIn</a>
            <a class="badge" href="https://your-portfolio.example" target="_blank" rel="noopener">🖥️ Portfolio</a>
            <a class="badge" href="https://github.com/NAVEEN-1709" target="_blank" rel="noopener">🐙 GitHub</a>
          </div>
        </div>

        <div>
          <h3 style="margin:0;color:#fff">Projects & Stats</h3>
          <p class="lead">Local project summaries, achievements and live stats below (SVG-based).</p>

          <div style="margin:10px 0">
            <img class="svg-inline" src="./assets/stats.svg?v=1" alt="local stats svg" />
          </div>

          <div style="margin-top:8px">
            <img class="svg-inline" src="./assets/langs.svg?v=1" alt="languages svg" />
          </div>

          <div style="margin-top:8px">
            <img class="svg-inline" src="./assets/trophies.svg?v=1" alt="trophies svg" />
          </div>
        </div>
      </div>

      <div style="height:16px"></div>

      <div class="section" style="display:flex;gap:12px;flex-direction:column;align-items:center">
        <h3 style="margin:0">Contribution & Snake</h3>
        <p class="lead">Contribution heatmap (generated locally) and a GitHub-snake SVG.</p>

        <div style="width:100%;max-width:860px;margin:12px auto">
          <img class="svg-inline" src="./assets/github-contribution-grid-snake.svg?v=1" alt="contribution grid snake" />
        </div>
      </div>

      <div style="height:10px"></div>

      <div class="section">
        <h3 style="margin:0">Social & Visitors</h3>
        <div class="footer-row">
          <a class="badge" href="https://github.com/NAVEEN-1709"><img src="./assets/banner.svg?v=1" alt="mini" style="height:30px;border-radius:6px"> GitHub</a>
          <span class="badge">👥 Visitors: <strong>—</strong></span>
          <span class="badge">📫 Email: nk9997201@gmail.com</span>
        </div>
      </div>

      <footer>
        © 2026 NAVEEN KUMAR • Turning ideas into intelligent software, one commit at a time.
      </footer>
    </div>
  </div>
</body>
</html>