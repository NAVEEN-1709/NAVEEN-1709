# -*- coding: utf-8 -*-
"""Rebuild banner.svg + banner-light.svg from scratch.
Clean dark bg, no giant blobs. Name rendered with stroked SVG path letters.
CSS + SMIL only. Embeds assets/profile.png as Base64 PNG.
"""
import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "profile.png"), "rb") as f:
    B64 = base64.b64encode(f.read()).decode("ascii")

LT = chr(38) + "lt;"
GT = chr(38) + "gt;"
BULL = chr(38) + "#8226;"

# Block-letter paths (local cell: width ~33, vertical 4..76). Stroke-style.
LP = {
    "N": "M6 4 L6 76 M6 4 L27 76 M27 4 L27 76",
    "A": "M6 76 L16.5 4 L27 76 M9.5 50 L23.5 50",
    "V": "M6 4 L16.5 76 L27 4",
    "E": "M6 4 L6 76 M6 4 L29 4 M6 40 L26 40 M6 76 L29 76",
    "K": "M6 4 L6 76 M27 4 L8 42 L27 76",
    "U": "M6 4 L6 62 M6 64 L27 64 M27 62 L27 4",
    "M": "M6 4 L6 76 M6 4 L16.5 44 L27 4 M27 4 L27 76",
    "R": "M6 4 L6 76 M6 4 L24 4 L24 38 L6 38 M17 39 L27 76",
}
WORDS = [("NAVEEN", [55, 104, 153, 202, 251, 300]), ("KUMAR", [395, 444, 493, 542, 591])]


def name_letters():
    i = 0
    out = []
    for word, xs in WORDS:
        for ch, x in zip(word, xs):
            out.append(
                f'<g class="namel ng{i}" transform="translate({x},214)" opacity="0">'
                f'<path d="{LP[ch]}" fill="none" stroke="url(#nameGrad)" '
                f'stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></g>'
            )
            i += 1
    return "\n".join(out)


STARS = (
    '<circle class="tw" cx="70" cy="120" r="1.4" fill="#9b8ec0"/>'
    '<circle class="tw" cx="180" cy="70" r="1.1" fill="#9b8ec0" style="animation-delay:.9s"/>'
    '<circle class="tw" cx="330" cy="90" r="1.4" fill="#9b8ec0" style="animation-delay:1.4s"/>'
    '<circle class="tw" cx="430" cy="50" r="1.0" fill="#9b8ec0" style="animation-delay:.5s"/>'
    '<circle class="tw" cx="700" cy="130" r="1.2" fill="#9b8ec0" style="animation-delay:1.8s"/>'
    '<circle class="tw" cx="940" cy="210" r="1.1" fill="#9b8ec0" style="animation-delay:.3s"/>'
    '<circle class="tw" cx="1150" cy="60" r="1.3" fill="#9b8ec0" style="animation-delay:1.1s"/>'
    '<circle class="tw" cx="1240" cy="150" r="1.0" fill="#9b8ec0" style="animation-delay:1.6s"/>'
    '<circle class="tw" cx="860" cy="300" r="1.2" fill="#9b8ec0"/>'
    '<circle class="tw" cx="520" cy="680" r="1.2" fill="#9b8ec0" style="animation-delay:1.2s"/>'
)

PART = (
    '<circle class="float" cx="90" cy="430" r="2" fill="#ff4ecd" opacity=".4"/>'
    '<circle class="float" cx="160" cy="650" r="1.6" fill="#38bdf8" opacity=".35"/>'
    '<circle class="float" cx="300" cy="360" r="1.6" fill="#8b5cf6" opacity=".4"/>'
    '<circle class="float" cx="470" cy="620" r="1.8" fill="#ff4ecd" opacity=".35"/>'
    '<circle class="float" cx="600" cy="300" r="1.4" fill="#38bdf8" opacity=".35"/>'
    '<circle class="float" cx="560" cy="700" r="1.6" fill="#8b5cf6" opacity=".4"/>'
    '<circle class="float" cx="700" cy="690" r="1.5" fill="#ff4ecd" opacity=".35"/>'
    '<circle class="float" cx="130" cy="260" r="1.5" fill="#8b5cf6" opacity=".4"/>'
)


def svg():
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1280" height="740" viewBox="0 0 1280 740" role="img" aria-labelledby="t d">
<title id="t">Naveen Kumar — Developer</title>
<desc id="d">Dark developer banner with terminal, large vector name, roles, quote, tech, about, stats, code editor, neon sign and anime character.</desc>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#0d0717"/><stop offset="100%" stop-color="#100a1c"/>
  </linearGradient>
<radialGradient id="ambient" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0%" stop-color="#8b5cf6" stop-opacity=".05"/>
    <stop offset="100%" stop-color="#8b5cf6" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="nameGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#ff4ecd"><animate attributeName="stop-color" values="#ff4ecd;#c084fc;#ff4ecd" dur="4s" repeatCount="indefinite"/></stop>
    <stop offset="55%" stop-color="#c084fc"><animate attributeName="stop-color" values="#c084fc;#ff4ecd;#8b5cf6;#c084fc" dur="5s" repeatCount="indefinite"/></stop>
    <stop offset="100%" stop-color="#8b5cf6"><animate attributeName="stop-color" values="#8b5cf6;#38bdf8;#8b5cf6" dur="4.5s" repeatCount="indefinite"/></stop>
  </linearGradient>
  <linearGradient id="pp" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#ff4ecd"/><stop offset="1" stop-color="#8b5cf6"/></linearGradient>
  <linearGradient id="glass" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#ffffff" stop-opacity=".08"/><stop offset="100%" stop-color="#ffffff" stop-opacity=".03"/>
  </linearGradient>
  <filter id="nameGlow" x="-60%" y="-60%" width="220%" height="220%">
    <feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="#ff4ecd" flood-opacity=".7"/>
  </filter>
  <filter id="shadow" x="-30%" y="-30%" width="160%" height="160%">
    <feDropShadow dx="0" dy="8" stdDeviation="14" flood-color="#000" flood-opacity=".5"/>
  </filter>
  <pattern id="grid" width="34" height="34" patternUnits="userSpaceOnUse">
    <path d="M34 0H0V34" fill="none" stroke="#ffffff" stroke-opacity=".035"/>
  </pattern>
  <clipPath id="clip"><rect x="6" y="6" width="1268" height="728" rx="32"/></clipPath>
  <style>
    .mono{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}}
    .ui{{font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif}}
    .panel{{fill:#151022;stroke:#ffffff;stroke-opacity:.14}}
    .namel{{transform-box:fill-box;transform-origin:center;animation:pop .5s cubic-bezier(.2,.8,.2,1) forwards}}
    .ng0{{animation-delay:.15s}}.ng1{{animation-delay:.23s}}.ng2{{animation-delay:.31s}}
    .ng3{{animation-delay:.39s}}.ng4{{animation-delay:.47s}}.ng5{{animation-delay:.55s}}
    .ng6{{animation-delay:.63s}}.ng7{{animation-delay:.71s}}.ng8{{animation-delay:.79s}}
    .ng9{{animation-delay:.87s}}.ng10{{animation-delay:.95s}}
    @keyframes pop{{0%{{opacity:0;transform:scale(.2)}}100%{{opacity:1;transform:scale(1)}}}}
    .blink{{animation:blk 1s steps(1,end) infinite}}@keyframes blk{{50%{{opacity:0}}}}
    .tw{{animation:twk 2.6s ease-in-out infinite}}@keyframes twk{{0%,100%{{opacity:.2}}50%{{opacity:1}}}}
    .float{{animation:flt 5s ease-in-out infinite}}@keyframes flt{{50%{{transform:translateY(-8px)}}}}
    .role{{opacity:0;position:absolute}}.r1{{animation:rol 15s 0s infinite}}.r2{{animation:rol 15s 3s infinite}}
    .r3{{animation:rol 15s 6s infinite}}.r4{{animation:rol 15s 9s infinite}}.r5{{animation:rol 15s 12s infinite}}
    @keyframes rol{{0%,4%{{opacity:0;transform:translateY(6px)}}7%,18%{{opacity:1;transform:translateY(0)}}21%,100%{{opacity:0;transform:translateY(-6px)}}}}
    .q{{opacity:0;animation:qr .8s 1.5s forwards}}@keyframes qr{{to{{opacity:1}}}}
    .c1{{animation:li .4s 2s both}}.c2{{animation:li .4s 2.3s both}}.c3{{animation:li .4s 2.6s both}}
    .c4{{animation:li .4s 2.9s both}}.c5{{animation:li .4s 3.2s both}}.c6{{animation:li .4s 3.5s both}}
    .c7{{animation:li .4s 3.8s both}}.c8{{animation:li .4s 4.1s both}}
    @keyframes li{{from{{opacity:0;transform:translateX(-10px)}}to{{opacity:1;transform:translateX(0)}}}}
    .sign{{animation:fck 6s infinite}}@keyframes fck{{0%,8.5%,10%,100%{{opacity:1}}9%{{opacity:.2}}52%{{opacity:.7}}53%{{opacity:.35}}54%{{opacity:1}}}}
    .holo{{animation:hol 1.6s cubic-bezier(.2,.8,.2,1) both}}@keyframes hol{{0%{{opacity:0;filter:brightness(1.7) saturate(0);transform:translateY(-30px)}}100%{{opacity:1;filter:none;transform:translateY(0)}}}}
    .scan{{animation:sc 3.5s linear infinite}}@keyframes sc{{0%{{transform:translateY(-10px);opacity:0}}8%{{opacity:.5}}55%{{opacity:0}}100%{{transform:translateY(750px);opacity:0}}}}
  </style>
</defs>

<g clip-path="url(#clip)">
  <rect width="1280" height="740" fill="url(#bg)"/>
  <rect width="1280" height="740" fill="url(#grid)"/>
  <circle cx="640" cy="380" r="280" fill="url(#ambient)"/>
  <rect x="6" y="6" width="1268" height="728" rx="32" fill="none" stroke="url(#pp)" stroke-opacity=".4"/>
  {STARS}
  {PART}

  <!-- LEFT: terminal -->
  <g transform="translate(55 42)" class="float" filter="url(#shadow)">
    <rect width="440" height="52" rx="14" class="panel"/>
    <circle cx="20" cy="26" r="4.5" fill="#ff5f57"/><circle cx="37" cy="26" r="4.5" fill="#febc2e"/><circle cx="54" cy="26" r="4.5" fill="#28c840"/>
    <text x="74" y="31" class="mono" font-size="14" fill="#7fffb2">user@dev:~$</text>
    <text x="180" y="31" class="mono" font-size="14" fill="#ffffff">cat README.md</text>
    <rect x="312" y="16" width="8" height="22" rx="2" fill="#ff4ecd" class="blink"/>
  </g>

  <!-- GREETING -->
  <text x="58" y="150" class="ui" font-size="24" font-weight="700" fill="#ffffff">Hi, I'm Naveen &#128075;</text>

  <!-- NAME: SVG path letters -->
  <g filter="url(#nameGlow)">
    {name_letters()}
    <circle cx="635" cy="250" r="6" fill="#ff4ecd"><animate attributeName="r" values="5;8;5" dur="2.4s" repeatCount="indefinite"/></circle>
  </g>

  <!-- ROLE -->
  <g transform="translate(52 330)" filter="url(#nameGlow)">
    <text class="mono role r1" font-size="17" fill="#ff9ee5">{LT} Developer {GT}</text>
    <text class="mono role r2" font-size="17" fill="#c4b5fd">{LT} Python Programmer {GT}</text>
    <text class="mono role r3" font-size="17" fill="#7dd3fc">{LT} Full Stack Learner {GT}</text>
    <text class="mono role r4" font-size="17" fill="#f9a8d4">{LT} Problem Solver {GT}</text>
    <text class="mono role r5" font-size="17" fill="#a78bfa">{LT} Open Source Enthusiast {GT}</text>
  </g>

  <!-- QUOTE -->
  <g transform="translate(52 362)" class="q">
    <rect width="560" height="82" rx="16" fill="url(#glass)" stroke="#ffffff" stroke-opacity=".14"/>
    <rect width="5" height="82" rx="3" fill="url(#pp)"/>
    <text x="24" y="32" class="mono" font-size="14" fill="#ffffff">"Turning ideas into intelligent software,</text>
    <text x="24" y="58" class="mono" font-size="14" fill="#d9c9ff">one commit at a time."</text>
  </g>

  <!-- TECH -->
  <g transform="translate(52 462)">
    <text class="ui" font-size="14" font-weight="700" fill="#c4b5fd">&#10022; Tech I Know</text>
    <g transform="translate(0 22)">
      <rect width="84" height="28" rx="14" fill="#ff4ecd" opacity=".1" stroke="#ff4ecd" stroke-opacity=".6"/>
      <text x="42" y="19" text-anchor="middle" class="mono" font-size="12" fill="#ff9ee5">Python</text>
      <rect x="96" width="106" height="28" rx="14" fill="#8b5cf6" opacity=".1" stroke="#8b5cf6" stroke-opacity=".6"/>
      <text x="149" y="19" text-anchor="middle" class="mono" font-size="12" fill="#c4b5fd">JavaScript</text>
      <rect x="214" width="66" height="28" rx="14" fill="#38bdf8" opacity=".1" stroke="#38bdf8" stroke-opacity=".6"/>
      <text x="247" y="19" text-anchor="middle" class="mono" font-size="12" fill="#7dd3fc">HTML</text>
      <rect x="292" width="62" height="28" rx="14" fill="#ff4ecd" opacity=".1" stroke="#ff4ecd" stroke-opacity=".6"/>
      <text x="323" y="19" text-anchor="middle" class="mono" font-size="12" fill="#ff9ee5">CSS</text>
      <rect x="366" width="58" height="28" rx="14" fill="#8b5cf6" opacity=".1" stroke="#8b5cf6" stroke-opacity=".6"/>
      <text x="395" y="19" text-anchor="middle" class="mono" font-size="12" fill="#c4b5fd">SQL</text>
    </g>
  </g>

  <!-- ABOUT -->
  <g transform="translate(52 545)">
    <text class="ui" font-size="14" font-weight="700" fill="#ff9ee5">&#9829; About Me</text>
    <text x="0" y="28" class="ui" font-size="13" fill="#ffffff">MCA Graduate {BULL} Python Developer {BULL} Web Development</text>
    <text x="0" y="50" class="ui" font-size="13" fill="#c4b5fd">Always Learning {BULL} Building AURA AI</text>
    <text x="0" y="72" class="ui" font-size="13" fill="#c4b5fd">Turning ideas into practical software</text>
  </g>

  <!-- STATS -->
  <g transform="translate(52 636)">
    <rect width="560" height="56" rx="16" fill="#151022" stroke="#ffffff" stroke-opacity=".16"/>
    <g class="mono" font-size="12" text-anchor="middle">
      <text x="70" y="22" fill="#ff9ee5">PROJECTS</text><text x="70" y="42" fill="#ffffff">5+</text>
      <line x1="140" y1="14" x2="140" y2="46" stroke="#ffffff" stroke-opacity=".25"/>
      <text x="210" y="22" fill="#c4b5fd">SKILLS</text><text x="210" y="42" fill="#ffffff">5</text>
      <line x1="280" y1="14" x2="280" y2="46" stroke="#ffffff" stroke-opacity=".25"/>
      <text x="350" y="22" fill="#7dd3fc">FOCUS</text><text x="350" y="42" fill="#ffffff">AI</text>
      <line x1="420" y1="14" x2="420" y2="46" stroke="#ffffff" stroke-opacity=".25"/>
      <text x="490" y="22" fill="#f9a8d4">MODE</text><text x="490" y="42" fill="#ffffff">BUILD</text>
    </g>
  </g>

  <!-- CENTER: code editor (small) -->
  <g transform="translate(635 42)" class="float" filter="url(#shadow)">
    <rect width="230" height="180" rx="15" fill="#120e1e" stroke="#d9d2ec" stroke-opacity=".22"/>
    <rect width="230" height="32" rx="15" fill="#201a33"/>
    <circle cx="18" cy="16" r="4.5" fill="#ff5f57"/><circle cx="34" cy="16" r="4.5" fill="#febc2e"/><circle cx="50" cy="16" r="4.5" fill="#28c840"/>
    <text x="72" y="20" class="mono" font-size="10" fill="#c4b5fd">dreams.jsx</text>
    <g class="mono" font-size="9.5">
      <text class="c1" x="14" y="50" fill="#c4b5fd">function <tspan fill="#ff9ee5">buildDreams</tspan>() {{</text>
      <text class="c2" x="22" y="68" fill="#e7e2f2">const skills = [</text>
      <text class="c3" x="32" y="86" fill="#7dd3fc">"Python",</text>
      <text class="c4" x="32" y="103" fill="#7dd3fc">"JavaScript",</text>
      <text class="c5" x="32" y="120" fill="#7dd3fc">"HTML", "CSS",</text>
      <text class="c6" x="32" y="137" fill="#7dd3fc">"SQL"</text>
      <text class="c7" x="22" y="155" fill="#e7e2f2">];</text>
      <text class="c8" x="22" y="172" fill="#f9a8d4">return "Keep Coding"</text>
    </g>
  </g>

  <!-- TOP RIGHT: neon sign -->
  <g transform="translate(1020 42)" class="sign" filter="url(#nameGlow)">
    <rect width="215" height="120" rx="18" fill="#160d24" stroke="#ff4ecd" stroke-width="2" stroke-opacity=".85"/>
    <text x="107" y="38" text-anchor="middle" font-size="22" fill="#ff9ee5">{LT}/{GT}</text>
    <text x="107" y="72" text-anchor="middle" class="mono" font-size="13" font-weight="700" letter-spacing="2" fill="#ff9ee5">KEEP CODING</text>
    <text x="107" y="96" text-anchor="middle" class="mono" font-size="13" font-weight="700" letter-spacing="2" fill="#c4b5fd">KEEP GROWING</text>
  </g>

  <!-- RIGHT: large anime character -->
  <g class="holo">
    <rect x="788" y="55" width="482" height="660" rx="28" fill="#130d20" opacity=".88"/>
    <rect x="790" y="57" width="478" height="656" rx="26" fill="none" stroke="url(#pp)" stroke-opacity=".35"/>
    <image x="783" y="40" width="492" height="680" href="data:image/png;base64,{B64}" preserveAspectRatio="xMidYMid meet"/>
  </g>

  <!-- horizontal scanner -->
  <g class="scan" opacity="0">
    <rect width="1280" height="3" fill="#ff4ecd" opacity=".5"/>
    <rect width="1280" height="1" fill="#8b5cf6" opacity=".6"/>
  </g>
</g>
</svg>
'''


dark = svg()
light = svg()

with open(os.path.join(HERE, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(dark)
with open(os.path.join(HERE, "banner-light.svg"), "w", encoding="utf-8") as f:
    f.write(light)

print("banner.svg", len(dark))
print("banner-light.svg", len(light))
print("DONE")

