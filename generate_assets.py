import os
import sys
import xml.etree.ElementTree as ET

os.makedirs('assets', exist_ok=True)

# -------------------------------------------------------------
# 1. HERO BANNER (1200 x 440)
# -------------------------------------------------------------
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="100%" height="auto">
  <defs>
    <linearGradient id="h-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#02040a" />
      <stop offset="40%" stop-color="#060b18" />
      <stop offset="80%" stop-color="#040714" />
      <stop offset="100%" stop-color="#010206" />
    </linearGradient>

    <radialGradient id="h-neb-cyan" cx="25%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#0ea5e9" stop-opacity="0.2" />
      <stop offset="50%" stop-color="#0284c7" stop-opacity="0.06" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="h-neb-violet" cx="75%" cy="50%" r="65%">
      <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.18" />
      <stop offset="45%" stop-color="#6366f1" stop-opacity="0.05" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="h-neb-center" cx="50%" cy="48%" r="45%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.22" />
      <stop offset="35%" stop-color="#6366f1" stop-opacity="0.12" />
      <stop offset="70%" stop-color="#a855f7" stop-opacity="0.04" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <linearGradient id="h-accretion" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.1" />
      <stop offset="25%" stop-color="#22d3ee" stop-opacity="0.85" />
      <stop offset="50%" stop-color="#f8fafc" stop-opacity="1" />
      <stop offset="75%" stop-color="#818cf8" stop-opacity="0.85" />
      <stop offset="100%" stop-color="#c084fc" stop-opacity="0.1" />
    </linearGradient>

    <radialGradient id="h-core-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.5" />
      <stop offset="40%" stop-color="#38bdf8" stop-opacity="0.2" />
      <stop offset="80%" stop-color="#6366f1" stop-opacity="0.05" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <filter id="h-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <filter id="h-glow-subtle" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="1.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>

    <pattern id="h-grid" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 60 0 L 0 0 0 60" fill="none" stroke="#38bdf8" stroke-width="0.5" stroke-opacity="0.04" />
      <circle cx="60" cy="0" r="0.8" fill="#38bdf8" fill-opacity="0.15" />
    </pattern>
  </defs>

  <style>
    @keyframes h-twinkle-1 {
      0%, 100% { opacity: 0.25; transform: scale(0.8); }
      50% { opacity: 0.95; transform: scale(1.2); }
    }
    @keyframes h-twinkle-2 {
      0%, 100% { opacity: 0.85; transform: scale(1.1); }
      50% { opacity: 0.2; transform: scale(0.7); }
    }
    @keyframes h-twinkle-3 {
      0%, 100% { opacity: 0.4; }
      50% { opacity: 1; }
    }
    @keyframes h-orbit-slow {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    @keyframes h-orbit-rev {
      from { transform: rotate(360deg); }
      to { transform: rotate(0deg); }
    }
    @keyframes h-pulse-glow {
      0%, 100% { opacity: 0.35; transform: scale(0.98); }
      50% { opacity: 0.7; transform: scale(1.02); }
    }

    .st-1 { animation: h-twinkle-1 4.5s ease-in-out infinite; }
    .st-2 { animation: h-twinkle-2 6s ease-in-out infinite; }
    .st-3 { animation: h-twinkle-3 3.5s ease-in-out infinite; }
    .orb-cw { transform-origin: 600px 185px; animation: h-orbit-slow 90s linear infinite; }
    .orb-ccw { transform-origin: 600px 185px; animation: h-orbit-rev 120s linear infinite; }
    .cor-pulse { transform-origin: 600px 185px; animation: h-pulse-glow 7s ease-in-out infinite; }
  </style>

  <rect width="1200" height="440" fill="url(#h-bg)" />
  <rect width="1200" height="440" fill="url(#h-grid)" />
  <rect width="1200" height="440" fill="url(#h-neb-cyan)" />
  <rect width="1200" height="440" fill="url(#h-neb-violet)" />
  <circle cx="600" cy="185" r="280" fill="url(#h-neb-center)" />

  <g id="h-starfield">
    <g class="st-1">
      <circle cx="85" cy="65" r="1" fill="#f8fafc" />
      <circle cx="160" cy="140" r="1.2" fill="#38bdf8" />
      <circle cx="230" cy="80" r="0.8" fill="#f8fafc" />
      <circle cx="310" cy="50" r="1.5" fill="#e0f2fe" />
      <circle cx="380" cy="120" r="0.8" fill="#818cf8" />
      <circle cx="450" cy="70" r="1.1" fill="#f8fafc" />
      <circle cx="520" cy="110" r="0.9" fill="#38bdf8" />
      <circle cx="680" cy="75" r="1.3" fill="#f8fafc" />
      <circle cx="740" cy="130" r="0.8" fill="#c084fc" />
      <circle cx="810" cy="60" r="1.2" fill="#e0f2fe" />
      <circle cx="890" cy="115" r="1" fill="#f8fafc" />
      <circle cx="970" cy="85" r="1.4" fill="#38bdf8" />
      <circle cx="1050" cy="55" r="0.9" fill="#f8fafc" />
      <circle cx="1120" cy="125" r="1.2" fill="#818cf8" />
      <circle cx="140" cy="360" r="1.1" fill="#f8fafc" />
      <circle cx="280" cy="390" r="0.8" fill="#38bdf8" />
      <circle cx="420" cy="350" r="1.2" fill="#f8fafc" />
      <circle cx="780" cy="370" r="1" fill="#e0f2fe" />
      <circle cx="920" cy="400" r="1.3" fill="#f8fafc" />
      <circle cx="1060" cy="365" r="0.8" fill="#38bdf8" />
    </g>
    <g class="st-2">
      <circle cx="50" cy="190" r="0.9" fill="#f8fafc" />
      <circle cx="120" cy="240" r="1.4" fill="#e0f2fe" />
      <circle cx="190" cy="180" r="0.7" fill="#818cf8" />
      <circle cx="270" cy="260" r="1.1" fill="#f8fafc" />
      <circle cx="340" cy="210" r="1.3" fill="#38bdf8" />
      <circle cx="860" cy="220" r="1.2" fill="#f8fafc" />
      <circle cx="930" cy="270" r="0.8" fill="#c084fc" />
      <circle cx="1010" cy="190" r="1.3" fill="#e0f2fe" />
      <circle cx="1080" cy="250" r="1" fill="#f8fafc" />
      <circle cx="1150" cy="200" r="0.8" fill="#38bdf8" />
      <circle cx="80" cy="320" r="1.3" fill="#f8fafc" />
      <circle cx="220" cy="330" r="0.9" fill="#e0f2fe" />
      <circle cx="360" cy="310" r="1.1" fill="#818cf8" />
      <circle cx="840" cy="320" r="0.8" fill="#f8fafc" />
      <circle cx="980" cy="340" r="1.4" fill="#38bdf8" />
      <circle cx="1110" cy="310" r="1" fill="#f8fafc" />
    </g>
    <g class="st-3">
      <circle cx="70" cy="110" r="1.6" fill="#ffffff" filter="url(#h-glow-subtle)" />
      <circle cx="250" cy="150" r="1.8" fill="#38bdf8" filter="url(#h-glow-subtle)" />
      <circle cx="490" cy="40" r="1.5" fill="#ffffff" filter="url(#h-glow-subtle)" />
      <circle cx="710" cy="45" r="1.5" fill="#ffffff" filter="url(#h-glow-subtle)" />
      <circle cx="950" cy="150" r="1.7" fill="#818cf8" filter="url(#h-glow-subtle)" />
      <circle cx="1130" cy="70" r="1.6" fill="#38bdf8" filter="url(#h-glow-subtle)" />
      <circle cx="180" cy="290" r="1.5" fill="#ffffff" filter="url(#h-glow-subtle)" />
      <circle cx="1020" cy="290" r="1.5" fill="#ffffff" filter="url(#h-glow-subtle)" />
    </g>
  </g>

  <g stroke="#38bdf8" stroke-opacity="0.12" stroke-width="0.75" fill="none">
    <polyline points="85,65 160,140 230,80 310,50 380,120" />
    <polyline points="810,60 890,115 970,85 1050,55 1120,125" />
    <polyline points="140,360 220,330 280,390 360,310" />
    <polyline points="840,320 920,400 980,340 1060,365" />
  </g>

  <g id="h-monument">
    <ellipse cx="600" cy="185" rx="360" ry="125" fill="none" stroke="url(#h-accretion)" stroke-width="0.75" stroke-opacity="0.3" stroke-dasharray="6 14" class="orb-cw" />
    <ellipse cx="600" cy="185" rx="290" ry="98" fill="none" stroke="#818cf8" stroke-width="0.5" stroke-opacity="0.35" stroke-dasharray="4 8" class="orb-ccw" />
    <ellipse cx="600" cy="185" rx="220" ry="72" fill="none" stroke="url(#h-accretion)" stroke-width="2.5" filter="url(#h-glow)" class="cor-pulse" />
    <ellipse cx="600" cy="185" rx="218" ry="70" fill="none" stroke="#f8fafc" stroke-width="0.75" stroke-opacity="0.9" />

    <ellipse cx="600" cy="185" rx="140" ry="46" fill="#010206" />
    <ellipse cx="600" cy="185" rx="140" ry="46" fill="url(#h-core-glow)" />
    <ellipse cx="600" cy="185" rx="140" ry="46" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-opacity="0.8" filter="url(#h-glow-subtle)" />

    <g class="orb-cw">
      <circle cx="960" cy="185" r="2.5" fill="#38bdf8" filter="url(#h-glow)" />
      <circle cx="240" cy="185" r="2" fill="#818cf8" />
      <line x1="960" y1="175" x2="960" y2="195" stroke="#38bdf8" stroke-width="0.5" stroke-opacity="0.6" />
    </g>
    <g class="orb-ccw">
      <circle cx="600" cy="87" r="2" fill="#c084fc" filter="url(#h-glow-subtle)" />
      <circle cx="600" cy="283" r="2.5" fill="#22d3ee" filter="url(#h-glow-subtle)" />
    </g>

    <line x1="600" y1="35" x2="600" y2="335" stroke="#38bdf8" stroke-width="0.5" stroke-opacity="0.2" stroke-dasharray="3 6" />
    <line x1="380" y1="185" x2="820" y2="185" stroke="#38bdf8" stroke-width="0.5" stroke-opacity="0.2" stroke-dasharray="3 6" />

    <g stroke="#38bdf8" stroke-width="0.75" stroke-opacity="0.5">
      <path d="M 590 185 L 610 185 M 600 175 L 600 195" />
      <circle cx="600" cy="185" r="16" fill="none" stroke="#38bdf8" stroke-width="0.5" stroke-opacity="0.4" stroke-dasharray="2 4" />
    </g>
  </g>

  <g id="h-frame" stroke="#38bdf8" stroke-width="1" fill="none">
    <path d="M 30 50 L 30 30 L 50 30" stroke-opacity="0.7" />
    <line x1="55" y1="30" x2="120" y2="30" stroke-opacity="0.2" />
    <circle cx="30" cy="30" r="1.5" fill="#38bdf8" />

    <path d="M 1170 50 L 1170 30 L 1150 30" stroke-opacity="0.7" />
    <line x1="1145" y1="30" x2="1080" y2="30" stroke-opacity="0.2" />
    <circle cx="1170" cy="30" r="1.5" fill="#38bdf8" />

    <path d="M 30 390 L 30 410 L 50 410" stroke-opacity="0.7" />
    <line x1="55" y1="410" x2="120" y2="410" stroke-opacity="0.2" />
    <circle cx="30" cy="410" r="1.5" fill="#38bdf8" />

    <path d="M 1170 390 L 1170 410 L 1150 410" stroke-opacity="0.7" />
    <line x1="1145" y1="410" x2="1080" y2="410" stroke-opacity="0.2" />
    <circle cx="1170" cy="410" r="1.5" fill="#38bdf8" />
  </g>

  <g font-family="'JetBrains Mono', 'SF Mono', monospace" font-size="9" fill="#94a3b8" letter-spacing="1.5">
    <text x="60" y="34" fill="#38bdf8" fill-opacity="0.9">OBSERVATORY // NODE-01</text>
    <text x="600" y="34" text-anchor="middle" fill="#64748b" fill-opacity="0.8">SECTOR // DEEP-SPACE SCIENTIFIC VISTA</text>
    <text x="1140" y="34" text-anchor="end" fill="#38bdf8" fill-opacity="0.9">SYSTEM STATUS // ACTIVE</text>
  </g>

  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif">
    <text x="600" y="112" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="500" fill="#38bdf8" letter-spacing="4" filter="url(#h-glow-subtle)">
      // CELESTIAL COMPUTING &amp; EXPEDITIONS
    </text>

    <text x="600" y="172" text-anchor="middle" font-size="44" font-weight="800" fill="#ffffff" letter-spacing="14" filter="url(#h-glow)">
      LUMINANCEXE
    </text>

    <text x="600" y="222" text-anchor="middle" font-size="13" font-weight="400" fill="#cbd5e1" letter-spacing="3.5" opacity="0.95">
      EXPLORING COMPUTATIONAL RELATIVITY • DISTRIBUTED SYSTEMS • DIGITAL EXPANSES
    </text>

    <text x="600" y="260" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="400" fill="#64748b" letter-spacing="2">
      ORBITAL REF: 45°14'N • VECTOR: 0x7E4 • HORIZON MATRIX • ALL SYSTEMS STABLE
    </text>
  </g>

  <g font-family="'JetBrains Mono', monospace" font-size="9" fill="#64748b" letter-spacing="1.5">
    <text x="60" y="408">TRANSMISSION FREQ: 1420.405 MHz</text>
    <text x="1140" y="408" text-anchor="end">EXPLORATION LOG // 2026.08</text>
  </g>

  <g transform="translate(600, 395)">
    <rect x="-105" y="-12" width="210" height="24" rx="12" fill="#0b1329" stroke="#38bdf8" stroke-width="0.8" stroke-opacity="0.4" />
    <circle cx="-85" cy="0" r="3" fill="#22c55e" />
    <circle cx="-85" cy="0" r="5" fill="none" stroke="#22c55e" stroke-width="0.5" opacity="0.6">
      <animate attributeName="r" values="3;7;3" dur="2.5s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.8;0;0.8" dur="2.5s" repeatCount="indefinite" />
    </circle>
    <text x="-70" y="3.5" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="600" fill="#e2e8f0" letter-spacing="1.5">
      CORE TELEMETRY ONLINE
    </text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 2. COSMIC DIVIDER (1200 x 36)
# -------------------------------------------------------------
divider_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 36" width="100%" height="auto">
  <defs>
    <linearGradient id="d-line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0" />
      <stop offset="25%" stop-color="#38bdf8" stop-opacity="0.3" />
      <stop offset="45%" stop-color="#22d3ee" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="1" />
      <stop offset="55%" stop-color="#818cf8" stop-opacity="0.9" />
      <stop offset="75%" stop-color="#818cf8" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#818cf8" stop-opacity="0" />
    </linearGradient>

    <filter id="d-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes d-pulse {
      0%, 100% { opacity: 0.4; transform: scale(0.9); }
      50% { opacity: 1; transform: scale(1.1); }
    }
    .d-beacon { transform-origin: 600px 18px; animation: d-pulse 3s ease-in-out infinite; }
  </style>

  <line x1="40" y1="18" x2="1160" y2="18" stroke="url(#d-line-grad)" stroke-width="1" />
  <line x1="300" y1="18" x2="900" y2="18" stroke="url(#d-line-grad)" stroke-width="2" filter="url(#d-glow)" opacity="0.6" />

  <g stroke="#38bdf8" stroke-width="0.75" stroke-opacity="0.5">
    <line x1="200" y1="14" x2="200" y2="22" />
    <line x1="400" y1="15" x2="400" y2="21" />
    <line x1="800" y1="15" x2="800" y2="21" />
    <line x1="1000" y1="14" x2="1000" y2="22" />
  </g>

  <g class="d-beacon">
    <circle cx="600" cy="18" r="10" fill="#00f2fe" fill-opacity="0.15" filter="url(#d-glow)" />
    <polygon points="600,10 608,18 600,26 592,18" fill="#02040a" stroke="#22d3ee" stroke-width="1.2" />
    <circle cx="600" cy="18" r="2" fill="#ffffff" />
  </g>
</svg>'''

# -------------------------------------------------------------
# 3. PROJECT 1: EVENT HORIZON (580 x 240)
# -------------------------------------------------------------
project_eh_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 240" width="100%" height="auto">
  <defs>
    <linearGradient id="eh-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#02040a" />
      <stop offset="50%" stop-color="#050a17" />
      <stop offset="100%" stop-color="#020308" />
    </linearGradient>

    <linearGradient id="eh-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.5" />
      <stop offset="50%" stop-color="#6366f1" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.1" />
    </linearGradient>

    <radialGradient id="eh-nebula" cx="20%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.25" />
      <stop offset="60%" stop-color="#6366f1" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <linearGradient id="eh-ring-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee" />
      <stop offset="40%" stop-color="#818cf8" />
      <stop offset="70%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#38bdf8" />
    </linearGradient>

    <filter id="eh-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes eh-spin {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    @keyframes eh-pulse {
      0%, 100% { opacity: 0.4; transform: scale(0.96); }
      50% { opacity: 0.85; transform: scale(1.04); }
    }
    .eh-rot { transform-origin: 90px 120px; animation: eh-spin 40s linear infinite; }
    .eh-pulse-cor { transform-origin: 90px 120px; animation: eh-pulse 5s ease-in-out infinite; }
  </style>

  <rect x="1" y="1" width="578" height="238" rx="12" fill="url(#eh-card-bg)" stroke="url(#eh-border)" stroke-width="1.2" />
  <rect x="1" y="1" width="578" height="238" rx="12" fill="url(#eh-nebula)" />

  <g stroke="#38bdf8" stroke-width="1" stroke-opacity="0.6" fill="none">
    <path d="M 12 24 L 12 12 L 24 12" />
    <path d="M 568 24 L 568 12 L 556 12" />
    <path d="M 12 216 L 12 228 L 24 228" />
    <path d="M 568 216 L 568 228 L 556 228" />
  </g>

  <g id="eh-visual">
    <ellipse cx="90" cy="120" rx="68" ry="46" fill="none" stroke="#38bdf8" stroke-width="0.5" stroke-opacity="0.3" stroke-dasharray="3 6" class="eh-rot" />
    <ellipse cx="90" cy="120" rx="52" ry="34" fill="none" stroke="url(#eh-ring-grad)" stroke-width="1.8" stroke-opacity="0.85" filter="url(#eh-glow)" class="eh-pulse-cor" />
    <ellipse cx="90" cy="120" rx="50" ry="32" fill="none" stroke="#ffffff" stroke-width="0.6" stroke-opacity="0.9" />

    <circle cx="90" cy="120" r="22" fill="#010206" stroke="#00f2fe" stroke-width="0.8" stroke-opacity="0.7" />

    <g class="eh-rot">
      <circle cx="158" cy="120" r="2.2" fill="#38bdf8" filter="url(#eh-glow)" />
      <circle cx="22" cy="120" r="1.5" fill="#f59e0b" />
    </g>

    <line x1="90" y1="45" x2="90" y2="195" stroke="#38bdf8" stroke-width="0.5" stroke-opacity="0.25" stroke-dasharray="2 4" />
    <circle cx="90" cy="52" r="1.5" fill="#22d3ee" />
    <circle cx="90" cy="188" r="1.5" fill="#818cf8" />
  </g>

  <line x1="172" y1="28" x2="172" y2="212" stroke="#38bdf8" stroke-width="0.5" stroke-opacity="0.15" stroke-dasharray="4 4" />

  <g font-family="'JetBrains Mono', 'SF Mono', monospace">
    <text x="190" y="38" font-size="9" font-weight="600" fill="#38bdf8" letter-spacing="1.5">
      EXPEDITION 01 // DEEP SPACE SIMULATION
    </text>

    <g transform="translate(435, 26)">
      <rect x="0" y="0" width="125" height="18" rx="9" fill="#0a192f" stroke="#22c55e" stroke-width="0.6" stroke-opacity="0.5" />
      <circle cx="10" cy="9" r="2.5" fill="#22c55e">
        <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite" />
      </circle>
      <text x="20" y="12.5" font-size="7.5" font-weight="600" fill="#86efac" letter-spacing="1">SIMULATION ACTIVE</text>
    </g>
  </g>

  <text x="190" y="74" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="#ffffff" letter-spacing="1.5">
    EVENT HORIZON
  </text>

  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" fill="#94a3b8">
    <text x="190" y="102">Interactive real-time relativistic astrophysics sandbox</text>
    <text x="190" y="120">featuring black hole gravitational lensing, accretion</text>
    <text x="190" y="138">disks, frame dragging &amp; computational physics.</text>
  </g>

  <g font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="500" fill="#38bdf8">
    <rect x="190" y="172" width="82" height="22" rx="4" fill="#0b1a33" stroke="#38bdf8" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="231" y="186" text-anchor="middle">JAVASCRIPT</text>

    <rect x="278" y="172" width="60" height="22" rx="4" fill="#0b1a33" stroke="#38bdf8" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="308" y="186" text-anchor="middle">WEBGL</text>

    <rect x="344" y="172" width="68" height="22" rx="4" fill="#0b1a33" stroke="#38bdf8" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="378" y="186" text-anchor="middle">THREE.JS</text>

    <rect x="418" y="172" width="138" height="22" rx="4" fill="#0b1a33" stroke="#818cf8" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="487" y="186" text-anchor="middle" fill="#a5b4fc">PHYSICS ENGINE</text>
  </g>

  <g font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b">
    <text x="190" y="218" letter-spacing="1">ACCESS REPOSITORY →</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 4. PROJECT 2: PHARMALOGIX (580 x 240)
# -------------------------------------------------------------
project_pl_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 240" width="100%" height="auto">
  <defs>
    <linearGradient id="pl-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#02040a" />
      <stop offset="50%" stop-color="#040e1b" />
      <stop offset="100%" stop-color="#010309" />
    </linearGradient>

    <linearGradient id="pl-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22d3ee" stop-opacity="0.5" />
      <stop offset="50%" stop-color="#3b82f6" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#22d3ee" stop-opacity="0.1" />
    </linearGradient>

    <radialGradient id="pl-nebula" cx="20%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0891b2" stop-opacity="0.22" />
      <stop offset="60%" stop-color="#1e3a8a" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <filter id="pl-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes pl-mesh-pulse {
      0%, 100% { opacity: 0.3; transform: scale(0.95); }
      50% { opacity: 0.8; transform: scale(1.05); }
    }
    @keyframes pl-transit {
      0% { stroke-dashoffset: 40; }
      100% { stroke-dashoffset: 0; }
    }
    .pl-pulse { transform-origin: 90px 120px; animation: pl-mesh-pulse 4.5s ease-in-out infinite; }
    .pl-flow { stroke-dasharray: 4 6; animation: pl-transit 3s linear infinite; }
  </style>

  <rect x="1" y="1" width="578" height="238" rx="12" fill="url(#pl-card-bg)" stroke="url(#pl-border)" stroke-width="1.2" />
  <rect x="1" y="1" width="578" height="238" rx="12" fill="url(#pl-nebula)" />

  <g stroke="#22d3ee" stroke-width="1" stroke-opacity="0.6" fill="none">
    <path d="M 12 24 L 12 12 L 24 12" />
    <path d="M 568 24 L 568 12 L 556 12" />
    <path d="M 12 216 L 12 228 L 24 228" />
    <path d="M 568 216 L 568 228 L 556 228" />
  </g>

  <g id="pl-visual">
    <circle cx="90" cy="120" r="62" fill="none" stroke="#22d3ee" stroke-width="0.5" stroke-opacity="0.25" stroke-dasharray="3 6" />

    <g stroke="#22d3ee" stroke-width="1" fill="none" class="pl-pulse">
      <polygon points="90,88 118,104 118,136 90,152 62,136 62,104" stroke-opacity="0.8" filter="url(#pl-glow)" />
      <circle cx="90" cy="120" r="12" fill="#083344" stroke="#22d3ee" stroke-width="1.2" />
      <circle cx="90" cy="120" r="3" fill="#ffffff" />
    </g>

    <g stroke="#38bdf8" stroke-width="0.8" class="pl-flow">
      <line x1="90" y1="58" x2="90" y2="88" stroke-opacity="0.7" />
      <line x1="118" y1="136" x2="142" y2="160" stroke-opacity="0.7" />
      <line x1="62" y1="136" x2="38" y2="160" stroke-opacity="0.7" />
    </g>

    <circle cx="90" cy="58" r="3" fill="#22d3ee" />
    <circle cx="142" cy="160" r="3" fill="#38bdf8" />
    <circle cx="38" cy="160" r="3" fill="#22d3ee" />
  </g>

  <line x1="172" y1="28" x2="172" y2="212" stroke="#22d3ee" stroke-width="0.5" stroke-opacity="0.15" stroke-dasharray="4 4" />

  <g font-family="'JetBrains Mono', 'SF Mono', monospace">
    <text x="190" y="38" font-size="9" font-weight="600" fill="#22d3ee" letter-spacing="1.5">
      EXPEDITION 02 // LOGISTICS ARCHITECTURE
    </text>

    <g transform="translate(425, 26)">
      <rect x="0" y="0" width="135" height="18" rx="9" fill="#06283d" stroke="#22d3ee" stroke-width="0.6" stroke-opacity="0.5" />
      <circle cx="10" cy="9" r="2.5" fill="#22d3ee">
        <animate attributeName="opacity" values="1;0.3;1" dur="2.4s" repeatCount="indefinite" />
      </circle>
      <text x="20" y="12.5" font-size="7.5" font-weight="600" fill="#a5f3fc" letter-spacing="1">SUPPLY MATRIX ONLINE</text>
    </g>
  </g>

  <text x="190" y="74" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="#ffffff" letter-spacing="1.5">
    PHARMALOGIX
  </text>

  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" fill="#94a3b8">
    <text x="190" y="102">Modern pharmacy inventory &amp; supply chain matrix</text>
    <text x="190" y="120">featuring multi-branch tracking, procurement workflows,</text>
    <text x="190" y="138">supplier portals &amp; real-time consumption analytics.</text>
  </g>

  <g font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="500" fill="#22d3ee">
    <rect x="190" y="172" width="86" height="22" rx="4" fill="#082f49" stroke="#22d3ee" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="233" y="186" text-anchor="middle">TYPESCRIPT</text>

    <rect x="282" y="172" width="56" height="22" rx="4" fill="#082f49" stroke="#22d3ee" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="310" y="186" text-anchor="middle">REACT</text>

    <rect x="344" y="172" width="105" height="22" rx="4" fill="#082f49" stroke="#22d3ee" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="396" y="186" text-anchor="middle">TAILWIND CSS</text>

    <rect x="455" y="172" width="48" height="22" rx="4" fill="#082f49" stroke="#22d3ee" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="479" y="186" text-anchor="middle">VITE</text>
  </g>

  <g font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b">
    <text x="190" y="218" letter-spacing="1">ACCESS REPOSITORY →</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 5. PROJECT 3: CLAIMIQ (580 x 240)
# -------------------------------------------------------------
project_ciq_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 240" width="100%" height="auto">
  <defs>
    <linearGradient id="ciq-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#02040a" />
      <stop offset="50%" stop-color="#0d081f" />
      <stop offset="100%" stop-color="#020308" />
    </linearGradient>

    <linearGradient id="ciq-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.5" />
      <stop offset="50%" stop-color="#6366f1" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#a855f7" stop-opacity="0.1" />
    </linearGradient>

    <radialGradient id="ciq-nebula" cx="20%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7e22ce" stop-opacity="0.22" />
      <stop offset="60%" stop-color="#312e81" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <filter id="ciq-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes ciq-wave {
      0%, 100% { opacity: 0.3; transform: scaleY(0.85); }
      50% { opacity: 0.9; transform: scaleY(1.15); }
    }
    @keyframes ciq-scan {
      0% { transform: translateY(-25px); opacity: 0; }
      50% { opacity: 0.8; }
      100% { transform: translateY(25px); opacity: 0; }
    }
    .ciq-anim-wave { transform-origin: 90px 120px; animation: ciq-wave 3.5s ease-in-out infinite; }
    .ciq-anim-scan { transform-origin: 90px 120px; animation: ciq-scan 4s ease-in-out infinite; }
  </style>

  <rect x="1" y="1" width="578" height="238" rx="12" fill="url(#ciq-card-bg)" stroke="url(#ciq-border)" stroke-width="1.2" />
  <rect x="1" y="1" width="578" height="238" rx="12" fill="url(#ciq-nebula)" />

  <g stroke="#a855f7" stroke-width="1" stroke-opacity="0.6" fill="none">
    <path d="M 12 24 L 12 12 L 24 12" />
    <path d="M 568 24 L 568 12 L 556 12" />
    <path d="M 12 216 L 12 228 L 24 228" />
    <path d="M 568 216 L 568 228 L 556 228" />
  </g>

  <g id="ciq-visual">
    <circle cx="90" cy="120" r="62" fill="none" stroke="#a855f7" stroke-width="0.5" stroke-opacity="0.25" stroke-dasharray="3 6" />

    <rect x="45" y="75" width="90" height="90" fill="#1e1035" fill-opacity="0.3" stroke="#a855f7" stroke-width="0.6" stroke-opacity="0.4" />
    <line x1="45" y1="120" x2="135" y2="120" stroke="#a855f7" stroke-width="0.5" stroke-opacity="0.3" />
    <line x1="90" y1="75" x2="90" y2="165" stroke="#a855f7" stroke-width="0.5" stroke-opacity="0.3" />

    <path d="M 45 120 Q 60 90, 75 120 T 105 120 T 135 120" fill="none" stroke="#c084fc" stroke-width="1.8" filter="url(#ciq-glow)" class="ciq-anim-wave" />
    <path d="M 45 120 Q 65 140, 85 120 T 120 120 T 135 120" fill="none" stroke="#818cf8" stroke-width="1" stroke-opacity="0.7" />

    <line x1="45" y1="120" x2="135" y2="120" stroke="#f472b6" stroke-width="1.5" filter="url(#ciq-glow)" class="ciq-anim-scan" />

    <circle cx="90" cy="120" r="3" fill="#ffffff" />
  </g>

  <line x1="172" y1="28" x2="172" y2="212" stroke="#a855f7" stroke-width="0.5" stroke-opacity="0.15" stroke-dasharray="4 4" />

  <g font-family="'JetBrains Mono', 'SF Mono', monospace">
    <text x="190" y="38" font-size="9" font-weight="600" fill="#c084fc" letter-spacing="1.5">
      EXPEDITION 03 // INTELLIGENCE &amp; QA
    </text>

    <g transform="translate(425, 26)">
      <rect x="0" y="0" width="135" height="18" rx="9" fill="#2e1065" stroke="#a855f7" stroke-width="0.6" stroke-opacity="0.5" />
      <circle cx="10" cy="9" r="2.5" fill="#c084fc">
        <animate attributeName="opacity" values="1;0.3;1" dur="2.8s" repeatCount="indefinite" />
      </circle>
      <text x="20" y="12.5" font-size="7.5" font-weight="600" fill="#e9d5ff" letter-spacing="1">DIAGNOSTICS ONLINE</text>
    </g>
  </g>

  <text x="190" y="74" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="#ffffff" letter-spacing="1.5">
    CLAIMIQ
  </text>

  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" fill="#94a3b8">
    <text x="190" y="102">Healthcare claims data quality &amp; operations engine</text>
    <text x="190" y="120">for discrepancy detection, RCM validation workflows,</text>
    <text x="190" y="138">QA analytics &amp; AI-assisted operational investigations.</text>
  </g>

  <g font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="500" fill="#c084fc">
    <rect x="190" y="172" width="65" height="22" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="222" y="186" text-anchor="middle">PYTHON</text>

    <rect x="261" y="172" width="112" height="22" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="317" y="186" text-anchor="middle">DATA QUALITY</text>

    <rect x="379" y="172" width="105" height="22" rx="4" fill="#3b0764" stroke="#a855f7" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="431" y="186" text-anchor="middle">RCM WORKFLOW</text>

    <rect x="490" y="172" width="68" height="22" rx="4" fill="#3b0764" stroke="#c084fc" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="524" y="186" text-anchor="middle" fill="#f3e8ff">ANALYTICS</text>
  </g>

  <g font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b">
    <text x="190" y="218" letter-spacing="1">ACCESS REPOSITORY →</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 6. PROJECT 4: GAMEDOCK (580 x 240)
# -------------------------------------------------------------
project_gd_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 240" width="100%" height="auto">
  <defs>
    <linearGradient id="gd-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#02040a" />
      <stop offset="50%" stop-color="#080f1d" />
      <stop offset="100%" stop-color="#010308" />
    </linearGradient>

    <linearGradient id="gd-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.5" />
      <stop offset="50%" stop-color="#0284c7" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.1" />
    </linearGradient>

    <radialGradient id="gd-nebula" cx="20%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#2563eb" stop-opacity="0.2" />
      <stop offset="60%" stop-color="#0f172a" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <filter id="gd-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes gd-dock-rot {
      from { transform: rotate(0deg); }
      to { transform: rotate(360deg); }
    }
    @keyframes gd-dock-rev {
      from { transform: rotate(360deg); }
      to { transform: rotate(0deg); }
    }
    .gd-cw { transform-origin: 90px 120px; animation: gd-dock-rot 30s linear infinite; }
    .gd-ccw { transform-origin: 90px 120px; animation: gd-dock-rev 45s linear infinite; }
  </style>

  <rect x="1" y="1" width="578" height="238" rx="12" fill="url(#gd-card-bg)" stroke="url(#gd-border)" stroke-width="1.2" />
  <rect x="1" y="1" width="578" height="238" rx="12" fill="url(#gd-nebula)" />

  <g stroke="#3b82f6" stroke-width="1" stroke-opacity="0.6" fill="none">
    <path d="M 12 24 L 12 12 L 24 12" />
    <path d="M 568 24 L 568 12 L 556 12" />
    <path d="M 12 216 L 12 228 L 24 228" />
    <path d="M 568 216 L 568 228 L 556 228" />
  </g>

  <g id="gd-visual">
    <circle cx="90" cy="120" r="62" fill="none" stroke="#3b82f6" stroke-width="0.5" stroke-opacity="0.25" stroke-dasharray="3 6" />

    <g class="gd-cw">
      <circle cx="90" cy="120" r="46" fill="none" stroke="#60a5fa" stroke-width="1.5" stroke-opacity="0.8" stroke-dasharray="24 12" filter="url(#gd-glow)" />
      <circle cx="136" cy="120" r="2.5" fill="#93c5fd" />
      <circle cx="44" cy="120" r="2.5" fill="#93c5fd" />
    </g>

    <g class="gd-ccw">
      <circle cx="90" cy="120" r="28" fill="none" stroke="#38bdf8" stroke-width="1.2" stroke-opacity="0.6" stroke-dasharray="14 8" />
      <circle cx="90" cy="92" r="2" fill="#38bdf8" />
      <circle cx="90" cy="148" r="2" fill="#38bdf8" />
    </g>

    <circle cx="90" cy="120" r="14" fill="#0f172a" stroke="#60a5fa" stroke-width="1.2" />
    <polygon points="90,113 96,120 90,127 84,120" fill="#93c5fd" />
  </g>

  <line x1="172" y1="28" x2="172" y2="212" stroke="#3b82f6" stroke-width="0.5" stroke-opacity="0.15" stroke-dasharray="4 4" />

  <g font-family="'JetBrains Mono', 'SF Mono', monospace">
    <text x="190" y="38" font-size="9" font-weight="600" fill="#60a5fa" letter-spacing="1.5">
      EXPEDITION 04 // INTERACTIVE NEXUS
    </text>

    <g transform="translate(420, 26)">
      <rect x="0" y="0" width="140" height="18" rx="9" fill="#172554" stroke="#3b82f6" stroke-width="0.6" stroke-opacity="0.5" />
      <circle cx="10" cy="9" r="2.5" fill="#60a5fa">
        <animate attributeName="opacity" values="1;0.3;1" dur="2.6s" repeatCount="indefinite" />
      </circle>
      <text x="20" y="12.5" font-size="7.5" font-weight="600" fill="#bfdbfe" letter-spacing="1">EXCHANGE HUB ACTIVE</text>
    </g>
  </g>

  <text x="190" y="74" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="800" fill="#ffffff" letter-spacing="1.5">
    GAMEDOCK
  </text>

  <g font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" fill="#94a3b8">
    <text x="190" y="102">All-in-one gaming ecosystem &amp; exchange platform</text>
    <text x="190" y="120">featuring digital PC sales, console rentals, P2P exchange</text>
    <text x="190" y="138">&amp; interactive community forums with dynamic theming.</text>
  </g>

  <g font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="500" fill="#60a5fa">
    <rect x="190" y="172" width="48" height="22" rx="4" fill="#1e3a5f" stroke="#3b82f6" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="214" y="186" text-anchor="middle">PHP</text>

    <rect x="244" y="172" width="92" height="22" rx="4" fill="#1e3a5f" stroke="#3b82f6" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="290" y="186" text-anchor="middle">JAVASCRIPT</text>

    <rect x="342" y="172" width="128" height="22" rx="4" fill="#1e3a5f" stroke="#3b82f6" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="406" y="186" text-anchor="middle">MARIADB / MYSQL</text>

    <rect x="476" y="172" width="82" height="22" rx="4" fill="#1e3a5f" stroke="#60a5fa" stroke-width="0.6" stroke-opacity="0.4" />
    <text x="517" y="186" text-anchor="middle" fill="#dbeafe">COMMERCE</text>
  </g>

  <g font-family="'JetBrains Mono', monospace" font-size="8.5" fill="#64748b">
    <text x="190" y="218" letter-spacing="1">ACCESS REPOSITORY →</text>
  </g>
</svg>'''

# -------------------------------------------------------------
# 7. TECH MATRIX (1200 x 300)
# -------------------------------------------------------------
tech_matrix_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="100%" height="auto">
  <defs>
    <linearGradient id="tm-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#02040a" />
      <stop offset="50%" stop-color="#050a18" />
      <stop offset="100%" stop-color="#010206" />
    </linearGradient>

    <linearGradient id="tm-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.4" />
      <stop offset="50%" stop-color="#6366f1" stop-opacity="0.15" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.4" />
    </linearGradient>

    <radialGradient id="tm-nebula-left" cx="20%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="tm-nebula-mid" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#6366f1" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="tm-nebula-right" cx="80%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.12" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <filter id="tm-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes tm-star-pulse {
      0%, 100% { opacity: 0.3; transform: scale(0.9); }
      50% { opacity: 0.9; transform: scale(1.1); }
    }
    .tm-node-pulse { transform-origin: center; animation: tm-star-pulse 4s ease-in-out infinite; }
  </style>

  <rect x="1" y="1" width="1198" height="298" rx="14" fill="url(#tm-card-bg)" stroke="url(#tm-border)" stroke-width="1.2" />
  <rect x="1" y="1" width="1198" height="298" rx="14" fill="url(#tm-nebula-left)" />
  <rect x="1" y="1" width="1198" height="298" rx="14" fill="url(#tm-nebula-mid)" />
  <rect x="1" y="1" width="1198" height="298" rx="14" fill="url(#tm-nebula-right)" />

  <g stroke="#38bdf8" stroke-width="1" stroke-opacity="0.6" fill="none">
    <path d="M 16 32 L 16 16 L 32 16" />
    <path d="M 1184 32 L 1184 16 L 1168 16" />
    <path d="M 16 268 L 16 284 L 32 284" />
    <path d="M 1184 268 L 1184 284 L 1168 284" />
  </g>

  <g font-family="'JetBrains Mono', 'SF Mono', monospace">
    <text x="40" y="38" font-size="9" font-weight="600" fill="#38bdf8" letter-spacing="2">
      // ORBITAL CAPABILITIES &amp; TECHNICAL CONSTELLATION
    </text>
    <text x="1160" y="38" text-anchor="end" font-size="9" font-weight="400" fill="#64748b" letter-spacing="1.5">
      VERIFIED SYSTEM PROFICIENCIES
    </text>
  </g>

  <line x1="400" y1="58" x2="400" y2="262" stroke="#38bdf8" stroke-width="0.5" stroke-opacity="0.15" stroke-dasharray="4 6" />
  <line x1="800" y1="58" x2="800" y2="262" stroke="#38bdf8" stroke-width="0.5" stroke-opacity="0.15" stroke-dasharray="4 6" />

  <!-- SECTOR 01: CORE LOGIC -->
  <g transform="translate(40, 68)">
    <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600" fill="#38bdf8" letter-spacing="1">
      SECTOR 01 // CORE SYNTHESIS &amp; LOGIC
    </text>

    <path d="M 12 52 L 72 86 L 168 56 L 240 92 L 310 52" fill="none" stroke="#38bdf8" stroke-width="0.75" stroke-opacity="0.25" stroke-dasharray="2 4" />

    <g transform="translate(0, 40)">
      <rect x="0" y="0" width="150" height="30" rx="6" fill="#081e36" stroke="#38bdf8" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#38bdf8" filter="url(#tm-glow)" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">TypeScript</text>
    </g>

    <g transform="translate(162, 40)">
      <rect x="0" y="0" width="168" height="30" rx="6" fill="#081e36" stroke="#38bdf8" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#facc15" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">JavaScript (ESNext)</text>
    </g>

    <g transform="translate(0, 82)">
      <rect x="0" y="0" width="150" height="30" rx="6" fill="#081e36" stroke="#38bdf8" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#38bdf8" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">Python</text>
    </g>

    <g transform="translate(162, 82)">
      <rect x="0" y="0" width="168" height="30" rx="6" fill="#081e36" stroke="#38bdf8" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#818cf8" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">PHP &amp; Ecosystem</text>
    </g>

    <g transform="translate(0, 124)">
      <rect x="0" y="0" width="330" height="30" rx="6" fill="#081e36" stroke="#38bdf8" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#4ade80" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">Bash &amp; Linux Shell Scripting</text>
    </g>
  </g>

  <!-- SECTOR 02: INTERFACES -->
  <g transform="translate(430, 68)">
    <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600" fill="#818cf8" letter-spacing="1">
      SECTOR 02 // INTERFACES &amp; RENDERING
    </text>

    <path d="M 12 52 L 80 92 L 180 52 L 260 88 L 310 52" fill="none" stroke="#818cf8" stroke-width="0.75" stroke-opacity="0.25" stroke-dasharray="2 4" />

    <g transform="translate(0, 40)">
      <rect x="0" y="0" width="160" height="30" rx="6" fill="#14183a" stroke="#818cf8" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#c084fc" filter="url(#tm-glow)" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">Three.js / WebGL</text>
    </g>

    <g transform="translate(172, 40)">
      <rect x="0" y="0" width="158" height="30" rx="6" fill="#14183a" stroke="#818cf8" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#22d3ee" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">React &amp; Radix UI</text>
    </g>

    <g transform="translate(0, 82)">
      <rect x="0" y="0" width="160" height="30" rx="6" fill="#14183a" stroke="#818cf8" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#38bdf8" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">Tailwind CSS</text>
    </g>

    <g transform="translate(172, 82)">
      <rect x="0" y="0" width="158" height="30" rx="6" fill="#14183a" stroke="#818cf8" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#f472b6" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">Vite Bundler</text>
    </g>

    <g transform="translate(0, 124)">
      <rect x="0" y="0" width="330" height="30" rx="6" fill="#14183a" stroke="#818cf8" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#818cf8" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">HTML5 / Modern Responsive CSS</text>
    </g>
  </g>

  <!-- SECTOR 03: SYSTEMS -->
  <g transform="translate(830, 68)">
    <text x="0" y="14" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="600" fill="#c084fc" letter-spacing="1">
      SECTOR 03 // SYSTEMS &amp; DATA MATRIX
    </text>

    <path d="M 12 52 L 72 86 L 168 56 L 240 92 L 310 52" fill="none" stroke="#c084fc" stroke-width="0.75" stroke-opacity="0.25" stroke-dasharray="2 4" />

    <g transform="translate(0, 40)">
      <rect x="0" y="0" width="160" height="30" rx="6" fill="#201036" stroke="#c084fc" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#f59e0b" filter="url(#tm-glow)" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">MariaDB / MySQL</text>
    </g>

    <g transform="translate(172, 40)">
      <rect x="0" y="0" width="158" height="30" rx="6" fill="#201036" stroke="#c084fc" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#4ade80" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">Linux Systems</text>
    </g>

    <g transform="translate(0, 82)">
      <rect x="0" y="0" width="160" height="30" rx="6" fill="#201036" stroke="#c084fc" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#c084fc" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">Data Quality &amp; QA</text>
    </g>

    <g transform="translate(172, 82)">
      <rect x="0" y="0" width="158" height="30" rx="6" fill="#201036" stroke="#c084fc" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#38bdf8" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">REST &amp; APIs</text>
    </g>

    <g transform="translate(0, 124)">
      <rect x="0" y="0" width="330" height="30" rx="6" fill="#201036" stroke="#c084fc" stroke-width="0.7" stroke-opacity="0.4" />
      <circle cx="16" cy="15" r="3" fill="#e879f9" />
      <text x="32" y="19" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="600" fill="#f8fafc">Computational Physics &amp; Algorithms</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 8. TELEMETRY STATS (1200 x 200)
# -------------------------------------------------------------
telemetry_stats_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 200" width="100%" height="auto">
  <defs>
    <linearGradient id="ts-card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#02040a" />
      <stop offset="50%" stop-color="#060c1c" />
      <stop offset="100%" stop-color="#010206" />
    </linearGradient>

    <linearGradient id="ts-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.4" />
      <stop offset="50%" stop-color="#818cf8" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#38bdf8" stop-opacity="0.4" />
    </linearGradient>

    <radialGradient id="ts-nebula" cx="50%" cy="50%" r="60%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.1" />
      <stop offset="50%" stop-color="#6366f1" stop-opacity="0.05" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>

    <filter id="ts-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <style>
    @keyframes ts-beacon-pulse {
      0%, 100% { opacity: 0.4; }
      50% { opacity: 1; }
    }
    .ts-pulse { animation: ts-beacon-pulse 2.5s ease-in-out infinite; }
  </style>

  <rect x="1" y="1" width="1198" height="198" rx="12" fill="url(#ts-card-bg)" stroke="url(#ts-border)" stroke-width="1.2" />
  <rect x="1" y="1" width="1198" height="198" rx="12" fill="url(#ts-nebula)" />

  <g stroke="#38bdf8" stroke-width="1" stroke-opacity="0.6" fill="none">
    <path d="M 14 26 L 14 14 L 26 14" />
    <path d="M 1186 26 L 1186 14 L 1174 14" />
    <path d="M 14 174 L 14 186 L 26 186" />
    <path d="M 1186 174 L 1186 186 L 1174 186" />
  </g>

  <g font-family="'JetBrains Mono', monospace">
    <text x="36" y="34" font-size="9" font-weight="600" fill="#38bdf8" letter-spacing="2">
      // CELESTIAL EXPEDITION TELEMETRY &amp; ACTIVITY
    </text>
    <text x="1164" y="34" text-anchor="end" font-size="9" font-weight="400" fill="#64748b" letter-spacing="1.5">
      TRANSMISSION PROTOCOL // LIVE
    </text>
  </g>

  <!-- 4 Telemetry Metric Blocks -->
  <g transform="translate(36, 56)">
    <rect x="0" y="0" width="265" height="114" rx="8" fill="#081426" stroke="#38bdf8" stroke-width="0.6" stroke-opacity="0.3" />
    <text x="20" y="28" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="600" fill="#64748b" letter-spacing="1">OBSERVATORY STATUS</text>
    <text x="20" y="62" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="700" fill="#ffffff" letter-spacing="0.5">Active Exploration</text>
    <g transform="translate(20, 84)">
      <circle cx="4" cy="0" r="3" fill="#22c55e" class="ts-pulse" />
      <text x="14" y="3.5" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="500" fill="#86efac" letter-spacing="1">SYSTEMS OPTIMAL</text>
    </g>
  </g>

  <g transform="translate(321, 56)">
    <rect x="0" y="0" width="265" height="114" rx="8" fill="#081426" stroke="#38bdf8" stroke-width="0.6" stroke-opacity="0.3" />
    <text x="20" y="28" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="600" fill="#64748b" letter-spacing="1">RESEARCH &amp; DEV NODES</text>
    <text x="20" y="62" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="18" font-weight="700" fill="#38bdf8" letter-spacing="0.5">8 Repositories</text>
    <g transform="translate(20, 84)">
      <circle cx="4" cy="0" r="3" fill="#38bdf8" />
      <text x="14" y="3.5" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="500" fill="#93c5fd" letter-spacing="1">OPEN SCIENTIFIC CODE</text>
    </g>
  </g>

  <g transform="translate(606, 56)">
    <rect x="0" y="0" width="265" height="114" rx="8" fill="#081426" stroke="#818cf8" stroke-width="0.6" stroke-opacity="0.3" />
    <text x="20" y="28" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="600" fill="#64748b" letter-spacing="1">PRIMARY DISCIPLINES</text>
    <text x="20" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="700" fill="#ffffff" letter-spacing="0.5">Physics &amp; Architecture</text>
    <g transform="translate(20, 84)">
      <circle cx="4" cy="0" r="3" fill="#818cf8" />
      <text x="14" y="3.5" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="500" fill="#c7d2fe" letter-spacing="1">ASTROPHYSICS • WEBGL</text>
    </g>
  </g>

  <g transform="translate(891, 56)">
    <rect x="0" y="0" width="273" height="114" rx="8" fill="#081426" stroke="#c084fc" stroke-width="0.6" stroke-opacity="0.3" />
    <text x="20" y="28" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="600" fill="#64748b" letter-spacing="1">EXPLORATION VECTOR</text>
    <text x="20" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="14" font-weight="700" fill="#ffffff" letter-spacing="0.5">High-Precision Systems</text>
    <g transform="translate(20, 84)">
      <circle cx="4" cy="0" r="3" fill="#c084fc" />
      <text x="14" y="3.5" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="500" fill="#e9d5ff" letter-spacing="1">MODULAR • RELIABLE</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------
# 9. FOOTER (1200 x 140)
# -------------------------------------------------------------
footer_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 140" width="100%" height="auto">
  <defs>
    <linearGradient id="f-line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0" />
      <stop offset="30%" stop-color="#38bdf8" stop-opacity="0.4" />
      <stop offset="50%" stop-color="#22d3ee" stop-opacity="0.9" />
      <stop offset="70%" stop-color="#818cf8" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#818cf8" stop-opacity="0" />
    </linearGradient>

    <radialGradient id="f-glow" cx="50%" cy="40%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.18" />
      <stop offset="100%" stop-color="#000000" stop-opacity="0" />
    </radialGradient>
  </defs>

  <style>
    @keyframes f-pulse-beacon {
      0%, 100% { r: 3; opacity: 0.4; }
      50% { r: 5; opacity: 0.95; }
    }
    .f-beacon { animation: f-pulse-beacon 3s ease-in-out infinite; }
  </style>

  <rect width="1200" height="140" fill="url(#f-glow)" />

  <line x1="100" y1="40" x2="1100" y2="40" stroke="url(#f-line-grad)" stroke-width="1" />

  <circle cx="600" cy="40" r="14" fill="#0284c7" fill-opacity="0.12" />
  <circle cx="600" cy="40" r="3" fill="#22d3ee" class="f-beacon" />
  <circle cx="600" cy="40" r="7" fill="none" stroke="#38bdf8" stroke-width="0.6" stroke-opacity="0.6" stroke-dasharray="2 2" />

  <g font-family="'JetBrains Mono', 'SF Mono', monospace" text-anchor="middle">
    <text x="600" y="78" font-size="10.5" font-weight="600" fill="#e2e8f0" letter-spacing="3">
      TRANSMISSION VECTOR // LUMINANCEXE
    </text>

    <text x="600" y="104" font-size="9" font-weight="400" fill="#64748b" letter-spacing="2">
      DEEP SPACE OBSERVATORY • OPEN TO NOVEL ARCHITECTURES &amp; EXPLORATIONS
    </text>
  </g>
</svg>'''

# -------------------------------------------------------------
# Write and Validate All Assets
# -------------------------------------------------------------
assets = {
    'assets/hero.svg': hero_svg,
    'assets/divider.svg': divider_svg,
    'assets/project_event_horizon.svg': project_eh_svg,
    'assets/project_pharmalogix.svg': project_pl_svg,
    'assets/project_claimiq.svg': project_ciq_svg,
    'assets/project_gamedock.svg': project_gd_svg,
    'assets/tech_matrix.svg': tech_matrix_svg,
    'assets/telemetry_stats.svg': telemetry_stats_svg,
    'assets/footer.svg': footer_svg,
}

for path, content in assets.items():
    try:
        ET.fromstring(content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[OK] Validated & Written: {path} ({len(content)} bytes)')
    except ET.ParseError as e:
        print(f'[ERROR] XML Parse Error in {path}: {e}')
        sys.exit(1)

print('\nAll 9 SVG assets successfully generated and validated.')
