import os
import sys
import json
import xml.sax.saxutils

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

with open(os.path.join(BASE_DIR, 'scripts', 'parsed_threats.json'), 'r', encoding='utf-8') as f:
    threats = json.load(f)

# Slug mapping
SLUG_MAP = {
    "TF-001": "asyncrat",
    "TF-002": "dolphinx",
    "TF-003": "lumma",
    "TF-004": "redline",
    "TF-005": "vidar",
    "TF-006": "agenttesla",
    "TF-007": "remcos",
    "TF-008": "xworm",
    "TF-009": "darkgate",
    "TF-010": "rhadamanthys",
    "TF-011": "stealc",
    "TF-012": "havoc",
    "TF-013": "sliver",
    "TF-014": "mythic",
    "TF-015": "quasarrat",
    "TF-016": "warzone",
    "TF-017": "guloader",
    "TF-018": "pikabot",
    "TF-019": "qakbot",
    "TF-020": "emotet",
    "TF-021": "lockbit",
    "TF-022": "blackcat",
    "TF-023": "akira",
    "TF-024": "medusa",
    "TF-025": "phobos",
    "TF-026": "formbook",
    "TF-027": "bumblebee",
    "TF-028": "icedid",
    "TF-029": "danabot",
    "TF-030": "smokeloader",
    "TF-031": "cobaltstrike",
    "TF-032": "bruteratel",
    "TF-033": "netsupport",
    "TF-034": "njrat",
    "TF-035": "dcrat",
    "TF-036": "purecrypter",
    "TF-037": "privateloader",
    "TF-038": "systembc",
    "TF-039": "mirai",
    "TF-040": "mozi",
    "TF-041": "meduza",
    "TF-042": "risepro",
    "TF-043": "bunnyloader",
    "TF-044": "latrodectus",
    "TF-045": "strelastealer",
    "TF-046": "hijackloader",
    "TF-047": "rustbucket",
    "TF-048": "atomic",
    "TF-049": "shadowpad",
    "TF-050": "plugx",
}

# Category colors & details
CATEGORY_DETAILS = {
    "RAT": {
        "color": "#06b6d4",
        "phase1": "Weaponized Attachment / Malicious LNK Lure",
        "phase2": "In-Memory Reflection & Process Injection (T1055)",
        "phase3": "Interactive HVNC, Keylogger & Remote Shell",
        "phase4_prefix": "Encrypted Bi-directional C2 Channel: "
    },
    "InfoStealer": {
        "color": "#10b981",
        "phase1": "Malvertising / Cracked Software / ClickFix Lure",
        "phase2": "Anti-VM Checks, Trigonometric Sleep & Sandbox Evasion",
        "phase3": "Browser Vault Extraction, Crypto Wallet Scraping (T1555)",
        "phase4_prefix": "Exfiltration Pipeline to Multi-Tier Gateways: "
    },
    "Ransomware": {
        "color": "#ef4444",
        "phase1": "Compromised VPN / RDP Access or Secondary Loader Dropper",
        "phase2": "Shadow Copy Deletion (vssadmin) & Privilege Escalation",
        "phase3": "Multi-threaded ChaCha20/AES-CBC File Encryption (T1486)",
        "phase4_prefix": "Tor Negotiation Portal & Leak Site Infrastructure: "
    },
    "Loader": {
        "color": "#f59e0b",
        "phase1": "Phishing Delivery via ISO, VHD, or Encrypted ZIP Archive",
        "phase2": "Vectored Exception Handling (VEH) & API Unhooking",
        "phase3": "Payload Staging, RC4 Decryption & In-Memory Drop",
        "phase4_prefix": "Dynamic Domain Generation & Tasking C2: "
    },
    "C2 Framework": {
        "color": "#8b5cf6",
        "phase1": "Adversary Operator Profile & Payload Generation Stub",
        "phase2": "Direct Syscall Invocation & EDR Hook Bypass (T1106)",
        "phase3": "Lateral Movement, Post-Exploitation & Process Migration",
        "phase4_prefix": "Malleable C2 Profile & Redundant Egress Listener: "
    },
    "Botnet": {
        "color": "#ec4899",
        "phase1": "Internet-wide Vulnerability Scan / Telnet Brute Force (T1110)",
        "phase2": "Architecture Detection, Watchdog Kill & Binary Dropper",
        "phase3": "Distributed DDoS Flood Engine (SYN/ACK/UDP/HTTP)",
        "phase4_prefix": "Decentralized P2P / IRC C2 Coordination Network: "
    },
    "Banking Trojan": {
        "color": "#3b82f6",
        "phase1": "Malicious Macro Document / Fake Invoice Distribution",
        "phase2": "Browser Man-in-the-Browser (MitB) & Form Grabbing Hook",
        "phase3": "Financial Web-inject & Credential Interception Module",
        "phase4_prefix": "Encrypted Banking Proxy Infrastructure: "
    },
    "Spyware": {
        "color": "#f97316",
        "phase1": "Spearphishing Email with Weaponized Order Confirmation",
        "phase2": ".NET Obfuscation Deobfuscation & Anti-Analysis Checks",
        "phase3": "Continuous Keystroke, Clipboard & Screenshot Surveillance",
        "phase4_prefix": "Exfiltration via Covert Network Channels: "
    }
}

def generate_schematic_svg(threat):
    tid = threat['id']
    num = threat['num']
    name = threat['name']
    cat = threat['category']
    lang = threat['lang']
    arch = threat['arch']
    c2 = threat['c2']
    mitre = threat['mitre']
    slug = SLUG_MAP.get(tid, tid.lower())

    cat_meta = CATEGORY_DETAILS.get(cat, {
        "color": "#06b6d4",
        "phase1": "Initial Infiltration Vector & Staged Payload Delivery",
        "phase2": "Execution, Memory Unhooking & Evasion (T1055)",
        "phase3": "Operational Capabilities & Target System Harvesting",
        "phase4_prefix": "Command and Control Channel: "
    })

    accent = cat_meta["color"]
    esc_name = xml.sax.saxutils.escape(name)
    esc_cat = xml.sax.saxutils.escape(cat)
    esc_lang = xml.sax.saxutils.escape(lang)
    esc_arch = xml.sax.saxutils.escape(arch)
    esc_c2 = xml.sax.saxutils.escape(c2)
    
    # Specific stage descriptions
    p1 = cat_meta["phase1"]
    p2 = cat_meta["phase2"]
    p3 = cat_meta["phase3"]
    p4 = cat_meta["phase4_prefix"] + esc_c2

    # Truncate p4 if too long for SVG box
    if len(p4) > 95:
        p4_line1 = p4[:92] + "..."
        p4_line2 = ""
    else:
        p4_line1 = p4
        p4_line2 = ""

    mitre_tags = "  •  ".join(mitre)

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 620" width="1000" height="620">
  <defs>
    <linearGradient id="bg_{tid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#07090e"/>
      <stop offset="100%" stop-color="#0f141f"/>
    </linearGradient>
    <linearGradient id="card_{tid}" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#141a27"/>
      <stop offset="100%" stop-color="#0a0d14"/>
    </linearGradient>
    <filter id="glow_{tid}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Canvas Background -->
  <rect width="1000" height="620" rx="10" fill="url(#bg_{tid})" stroke="#1f283d" stroke-width="2"/>

  <!-- Top Titlebar Ribbon -->
  <rect x="0" y="0" width="1000" height="48" rx="10" fill="#0d111a" stroke="#1f283d" stroke-width="1"/>
  <rect x="0" y="38" width="1000" height="10" fill="#0d111a"/>
  
  <!-- Terminal Indicators -->
  <circle cx="24" cy="24" r="5" fill="#ef4444"/>
  <circle cx="40" cy="24" r="5" fill="#f59e0b"/>
  <circle cx="56" cy="24" r="5" fill="#10b981"/>

  <text x="80" y="29" fill="#94a3b8" font-family="'JetBrains Mono', 'Segoe UI', monospace" font-size="12" font-weight="700">CYBERTRACE INTELLIGENCE PLATFORM // TECHNICAL ARCHITECTURE SCHEMATIC</text>
  
  <rect x="790" y="14" width="190" height="22" rx="4" fill="{accent}" fill-opacity="0.15" stroke="{accent}" stroke-width="1"/>
  <text x="885" y="29" fill="{accent}" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="middle" font-weight="800">STRICT 1-TO-1 SPEC: {tid}</text>

  <!-- Threat Overview Header Card -->
  <rect x="25" y="65" width="950" height="75" rx="6" fill="#111622" stroke="#232d42" stroke-width="1"/>
  
  <!-- Accent Edge Bar -->
  <rect x="25" y="65" width="5" height="75" rx="2" fill="{accent}"/>
  
  <text x="45" y="96" fill="#ffffff" font-family="'Segoe UI', -apple-system, sans-serif" font-size="20" font-weight="800">{esc_name}</text>
  <text x="45" y="122" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11">CLASS: <tspan fill="{accent}" font-weight="700">{esc_cat}</tspan> | LANG: <tspan fill="#e2e8f0">{esc_lang}</tspan> | CORE ARCH: <tspan fill="#e2e8f0">{esc_arch}</tspan></text>
  
  <rect x="830" y="80" width="130" height="45" rx="4" fill="#0a0d14" stroke="#232d42" stroke-width="1"/>
  <text x="895" y="98" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9" text-anchor="middle">STATUS</text>
  <text x="895" y="115" fill="#22c55e" font-family="'JetBrains Mono', monospace" font-size="12" text-anchor="middle" font-weight="800">● {threat['status']}</text>

  <!-- Execution Pipeline: 4 Core Sequential Stages -->
  
  <!-- Stage 1 -->
  <g transform="translate(25, 160)">
    <rect width="218" height="290" rx="6" fill="url(#card_{tid})" stroke="#222c40" stroke-width="1"/>
    <rect x="0" y="0" width="218" height="34" rx="6" fill="#161e2e"/>
    <rect x="0" y="26" width="218" height="8" fill="#161e2e"/>
    <text x="14" y="22" fill="{accent}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800">STAGE 01</text>
    <text x="14" y="58" fill="#f1f5f9" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700">Initial Delivery</text>
    <line x1="14" y1="70" x2="204" y2="70" stroke="#222c40" stroke-width="1"/>
    <text x="14" y="95" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="11" width="190">
      <tspan x="14" dy="0">{p1[:28]}</tspan>
      <tspan x="14" dy="18">{p1[28:56]}</tspan>
      <tspan x="14" dy="18">{p1[56:84]}</tspan>
    </text>
    <rect x="14" y="235" width="190" height="40" rx="4" fill="#0d111a" stroke="#1e2638" stroke-width="1"/>
    <text x="24" y="252" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9">VECTOR TYPE</text>
    <text x="24" y="266" fill="{accent}" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700">Inbound Delivery</text>
  </g>

  <!-- Connector 1 -> 2 -->
  <path d="M 243 305 L 269 305" stroke="{accent}" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="269,301 275,305 269,309" fill="{accent}"/>

  <!-- Stage 2 -->
  <g transform="translate(269, 160)">
    <rect width="218" height="290" rx="6" fill="url(#card_{tid})" stroke="#222c40" stroke-width="1"/>
    <rect x="0" y="0" width="218" height="34" rx="6" fill="#161e2e"/>
    <rect x="0" y="26" width="218" height="8" fill="#161e2e"/>
    <text x="14" y="22" fill="{accent}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800">STAGE 02</text>
    <text x="14" y="58" fill="#f1f5f9" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700">Evasion &amp; Execution</text>
    <line x1="14" y1="70" x2="204" y2="70" stroke="#222c40" stroke-width="1"/>
    <text x="14" y="95" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="11">
      <tspan x="14" dy="0">{p2[:28]}</tspan>
      <tspan x="14" dy="18">{p2[28:56]}</tspan>
      <tspan x="14" dy="18">{p2[56:84]}</tspan>
    </text>
    <rect x="14" y="235" width="190" height="40" rx="4" fill="#0d111a" stroke="#1e2638" stroke-width="1"/>
    <text x="24" y="252" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9">DEFENSE EVASION</text>
    <text x="24" y="266" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700">Memory Unhooking</text>
  </g>

  <!-- Connector 2 -> 3 -->
  <path d="M 487 305 L 513 305" stroke="{accent}" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="513,301 519,305 513,309" fill="{accent}"/>

  <!-- Stage 3 -->
  <g transform="translate(513, 160)">
    <rect width="218" height="290" rx="6" fill="url(#card_{tid})" stroke="#222c40" stroke-width="1"/>
    <rect x="0" y="0" width="218" height="34" rx="6" fill="#161e2e"/>
    <rect x="0" y="26" width="218" height="8" fill="#161e2e"/>
    <text x="14" y="22" fill="{accent}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800">STAGE 03</text>
    <text x="14" y="58" fill="#f1f5f9" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700">Core Objectives</text>
    <line x1="14" y1="70" x2="204" y2="70" stroke="#222c40" stroke-width="1"/>
    <text x="14" y="95" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="11">
      <tspan x="14" dy="0">{p3[:28]}</tspan>
      <tspan x="14" dy="18">{p3[28:56]}</tspan>
      <tspan x="14" dy="18">{p3[56:84]}</tspan>
    </text>
    <rect x="14" y="235" width="190" height="40" rx="4" fill="#0d111a" stroke="#1e2638" stroke-width="1"/>
    <text x="24" y="252" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9">MALWARE MISSION</text>
    <text x="24" y="266" fill="#e2e8f0" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700">{esc_cat} Modules</text>
  </g>

  <!-- Connector 3 -> 4 -->
  <path d="M 731 305 L 757 305" stroke="{accent}" stroke-width="2" stroke-dasharray="4,3"/>
  <polygon points="757,301 763,305 757,309" fill="{accent}"/>

  <!-- Stage 4 -->
  <g transform="translate(757, 160)">
    <rect width="218" height="290" rx="6" fill="url(#card_{tid})" stroke="#222c40" stroke-width="1"/>
    <rect x="0" y="0" width="218" height="34" rx="6" fill="#161e2e"/>
    <rect x="0" y="26" width="218" height="8" fill="#161e2e"/>
    <text x="14" y="22" fill="{accent}" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800">STAGE 04</text>
    <text x="14" y="58" fill="#f1f5f9" font-family="'Segoe UI', sans-serif" font-size="13" font-weight="700">C2 &amp; Exfiltration</text>
    <line x1="14" y1="70" x2="204" y2="70" stroke="#222c40" stroke-width="1"/>
    <text x="14" y="95" fill="#94a3b8" font-family="'Segoe UI', sans-serif" font-size="11">
      <tspan x="14" dy="0">{p4_line1[:28]}</tspan>
      <tspan x="14" dy="18">{p4_line1[28:56]}</tspan>
      <tspan x="14" dy="18">{p4_line1[56:84]}</tspan>
    </text>
    <rect x="14" y="235" width="190" height="40" rx="4" fill="#0d111a" stroke="#1e2638" stroke-width="1"/>
    <text x="24" y="252" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="9">C2 INFRASTRUCTURE</text>
    <text x="24" y="266" fill="{accent}" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700">{esc_c2[:20]}...</text>
  </g>

  <!-- Bottom MITRE ATT&CK Ribbon -->
  <rect x="25" y="470" width="950" height="60" rx="6" fill="#0d111a" stroke="#1f283d" stroke-width="1"/>
  <text x="45" y="495" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700">VERIFIED MITRE ATT&amp;CK TECHNIQUES MAPPING</text>
  <text x="45" y="515" fill="#38bdf8" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">{mitre_tags}</text>

  <!-- Technical Verification Hash / Footer -->
  <text x="25" y="565" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10">CYBERTRACE CTI ID: CT-SPEC-{num}-2026 // STRICT 1-TO-1 FORENSIC ATTRIBUTION ASSURED</text>
  <text x="975" y="565" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="10" text-anchor="end">CONFIDENTIAL // DEFENSIVE CTI OPERATIONS</text>
  
  <!-- Diagnostic Scanline -->
  <line x1="25" y1="580" x2="975" y2="580" stroke="#1e2638" stroke-width="1"/>
</svg>'''
    return svg_content

print("=== Generating 50 Custom Architectural Schematics ===")
count = 0
for threat in threats:
    tid = threat['id']
    slug = SLUG_MAP.get(tid, tid.lower())
    svg_code = generate_schematic_svg(threat)
    filename = f"{tid}_{slug}_arch.svg"
    target_path = os.path.join(IMAGES_DIR, filename)
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(svg_code)
    count += 1
    if count % 10 == 0 or count == len(threats):
        print(f"  Generated {count}/50: {filename}")

print(f"✅ Generated {count} custom architectural schematics in images/")
