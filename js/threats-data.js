/**
 * CYBERTRACE INTELLIGENCE DATABASE
 * Comprehensive Threat Files Catalog (#001 - #050)
 * Telemetry: 2026 Defensive CTI Operations
 */

const THREATS_DATA = [
  {
    id: "TF-001",
    num: "001",
    name: "AsyncRAT",
    category: "RAT",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED_PRIOR",
    lang: "C# (.NET)",
    arch: "Client-Server (TLS)",
    c2: "Dynamic DNS, Cloudflare Tunnels, TLS CN=AsyncRAT",
    mitre: ["T1056.001", "T1055", "T1573", "T1071.001"],
    image: "images/TF-001_asyncrat_real_01.png",
    imageCaption: "AsyncRAT Client Payload Builder & Configurator",
    gallery: [
      {
        id: "EVID-001-01",
        type: "Builder UI",
        url: "images/TF-001_asyncrat_real_01.png",
        title: "AsyncRAT Client Payload Builder & Configurator",
        caption: "Operator configurator GUI showing TLS X.509 certificate generation, keylogger toggles, process injection, and persistence configuration."
      },
      {
        id: "EVID-001-02",
        type: "Surveillance Telemetry",
        url: "images/TF-001_asyncrat_real_02.svg",
        title: "AsyncRAT Remote Desktop & Session Monitoring",
        caption: "Interactive desktop surveillance module capturing victim screen buffers and keystroke telemetry streams."
      },
      {
        id: "EVID-001-03",
        type: "Architecture Schematic",
        url: "images/TF-001_asyncrat_arch.svg",
        title: "AsyncRAT Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Dynamic DNS, Cloudflare Tunnels, TLS CN=AsyncRAT command infrastructure."
      }
    ],
    en: {
      type: "Remote Access Trojan (RAT)",
      summary: "Ubiquitous open-source remote access trojan weaponized with Cloudflare Tunnels and session-cookie hijacking.",
      desc: "A veteran open-source Windows RAT widely leveraged in commodity campaigns and targeted intrusions (30-40 victim scope) to bypass MFA via session token theft.",
      tech: [
        "Language: C# (.NET Framework)",
        "Architecture: Encrypted Client-Server architecture via TLS",
        "C2 Protocol: Self-signed TLS certificates (CN=AsyncRAT) abusing Cloudflare Tunnels & WebDAV",
        "Capabilities: Keylogging, process injection into explorer.exe, cookie harvesting, remote shell",
        "Evasion: Fileless in-memory execution via obfuscated PowerShell loaders"
      ],
      propagation: "Distributed through spear-phishing campaigns with malicious attachments and cracked software archives.",
      defense: [
        "Isolate impacted endpoint immediately from local subnet.",
        "Revoke active browser sessions and reset credentials from a clean out-of-band device.",
        "Audit Run registry keys and Startup directories for persistence hooks.",
        "Inspect telemetry for suspicious background powershell.exe or python processes."
      ],
      whyWatch: "Unmatched code adaptability and rapid cloud tunneling integration keep AsyncRAT at the top of 2026 SOC triage queues."
    },
    sources: [
      { name: "CISA Alert AA21-209A", type: "Security" },
      { name: "Mandiant Commodity Malware Intel", type: "Security" },
      { name: "Underground Forum Telemetry", type: "Community" }
    ]
  },
  {
    id: "TF-002",
    num: "002",
    name: "Dolphin X",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED",
    lang: "C++ / Python / AI Core",
    arch: "AI-Assisted Modular Payload",
    c2: "Encrypted Telegram API, Cloudflare Workers, Decentralized Webhooks",
    mitre: ["T1005", "T1555", "T1027.002", "T1497"],
    image: "images/TF-002_dolphinx_real_01.png",
    imageCaption: "Dolphin X AI Stealer Builder Interface",
    gallery: [
      {
        id: "EVID-002-01",
        type: "Builder UI",
        url: "images/TF-002_dolphinx_real_01.png",
        title: "Dolphin X AI Stealer Builder Interface",
        caption: "Builder interface setting target heuristics, browser extension targeting, and polymorphic stub compilation parameters."
      },
      {
        id: "EVID-002-02",
        type: "Exfiltration Channel",
        url: "images/TF-002_dolphinx_real_02.png",
        title: "Dolphin X Encrypted Telegram Exfiltration Feed",
        caption: "Operator notification channel broadcasting compromised victim specifications, geolocations, and encrypted credential archives."
      },
      {
        id: "EVID-002-03",
        type: "Architecture Schematic",
        url: "images/TF-002_dolphinx_arch.svg",
        title: "Dolphin X Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Encrypted Telegram API, Cloudflare Workers, Decentralized Webhooks command infrastructure."
      },
      {
        id: "EVID-002-04",
        type: "C2 Dashboard",
        url: "images/dolphinx_05_dashboard.png",
        title: "Dolphin X Central Web Telemetry Dashboard",
        caption: "Centralized operator interface aggregating infected victim nodes and exfiltrated credential archives."
      }
    ],
    en: {
      type: "AI-Assisted InfoStealer & Spyware",
      summary: "Next-generation infostealer employing embedded AI heuristics for dynamic sandbox evasion and credential theft.",
      desc: "Cutting-edge stealer leveraging local lightweight AI models to evaluate sandbox artifacts, evade behavioral EDR heuristics, and exfiltrate crypto assets and session tokens.",
      tech: [
        "Language: C++ with embedded compiled Python runtime",
        "Architecture: Modular AI-driven client with environmental introspection",
        "C2 Protocol: Telegram Bot API over TLS, Cloudflare Workers, Decentralized Webhooks",
        "Capabilities: Cold/hot crypto wallet harvesting, Telegram/Discord token hijacking, password exfiltration",
        "AI Innovation: Dynamic delay heuristics evaluating real-time user mouse/keyboard activity"
      ],
      propagation: "Distributed through malicious GitHub developer packages, search engine malvertising, and cracked software.",
      defense: [
        "Sever internet connectivity immediately to cut off outbound Telegram webhook exfiltration.",
        "Sweep and rotate all cold/hot cryptocurrency private keys to safe custody.",
        "Invalidate all developer tokens (AWS, GitHub, Slack) and regenerate SSH keys.",
        "Inspect LocalAppData for anomalous packed Python executables and hidden DLLs."
      ],
      whyWatch: "Pioneers the weaponization of local AI heuristics in commodity infostealers during 2026."
    },
    sources: [
      { name: "Varonis Threat Research 2025-2026", type: "Security" },
      { name: "PCRisk Malware Database", type: "Security" },
      { name: "CyberTrace Defensive Lab Verification", type: "Lab" }
    ]
  },
  {
    id: "TF-003",
    num: "003",
    name: "Lumma Stealer",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C (Native)",
    arch: "Malware-as-a-Service (MaaS)",
    c2: "Fast-Flux Domains, Cloudflare Proxies, Multi-tier C2",
    mitre: ["T1555.003", "T1056", "T1027", "T1071.001"],
    image: "images/TF-003_lumma_real_01.png",
    imageCaption: "Lumma Stealer Process Execution Graph",
    gallery: [
      {
        id: "EVID-003-01",
        type: "Sandbox Execution",
        url: "images/TF-003_lumma_real_01.png",
        title: "Lumma Stealer Process Execution Graph",
        caption: "ANY.RUN sandbox telemetry displaying multi-stage process injection, anti-analysis loops, and credential harvesting routines."
      },
      {
        id: "EVID-003-02",
        type: "C2 Communication",
        url: "images/TF-003_lumma_real_02.png",
        title: "LummaC2 Fast-Flux Network Handshake",
        caption: "Encrypted HTTP C2 beaconing protocol showing dynamic domain resolution and target configuration retrieval."
      },
      {
        id: "EVID-003-03",
        type: "Architecture Schematic",
        url: "images/TF-003_lumma_arch.svg",
        title: "Lumma Stealer Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Fast-Flux Domains, Cloudflare Proxies, Multi-tier C2 command infrastructure."
      }
    ],
    en: {
      type: "InfoStealer (MaaS)",
      summary: "Market-leading Russian MaaS infostealer engineered in pure C for rapid exfiltration and evasion.",
      desc: "A highly evasive C-based infostealer operating as a subscription service. Dominates underground forums with rapid browser and crypto wallet extraction capabilities.",
      tech: [
        "Language: Pure native C (zero external runtime dependencies)",
        "Architecture: Lightweight client interacting with multi-tier MaaS web panels",
        "C2 Protocol: Fast-flux domain rotation and Cloudflare-proxied endpoints",
        "Capabilities: Steals from 100+ Chromium/Gecko extensions, crypto vaults, Steam/Discord sessions",
        "Evasion: Heavy control-flow flattening, API hashing, and anti-debug hooks"
      ],
      propagation: "Weaponized YouTube video descriptions, fake software patches, and SEO poisoning.",
      defense: [
        "Invalidate all credentials and browser session cookies across corporate assets.",
        "Audit and purge unverified browser extensions and app permissions.",
        "Block dynamic DNS resolutions targeting suspicious TLDs (.click, .shop, .top).",
        "Transition all critical identity providers to hardware-backed FIDO2 authentication."
      ],
      whyWatch: "Remains the most prolific and commercially successful infostealer family globally in 2026."
    },
    sources: [
      { name: "Outpost24 Lumma In-Depth Analysis", type: "Security" },
      { name: "Kaspersky Threat Intelligence Report", type: "Security" },
      { name: "Russian Underground Forum Logs", type: "Community" }
    ]
  },
  {
    id: "TF-004",
    num: "004",
    name: "RedLine Stealer",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED_PRIOR",
    lang: ".NET (C#)",
    arch: "WCF / SOAP Client-Server",
    c2: "Direct TCP, WCF Endpoints, Telegram Exfiltration",
    mitre: ["T1555", "T1005", "T1082", "T1071"],
    image: "images/TF-004_redline_real_01.png",
    imageCaption: "RedLine Stealer Lua Bytecode Execution",
    gallery: [
      {
        id: "EVID-004-01",
        type: "Process Injection",
        url: "images/TF-004_redline_real_01.png",
        title: "RedLine Stealer Lua Bytecode Execution",
        caption: "ANY.RUN sandbox capture showing Lua bytecode decompression and process hollowing into legitimate Windows processes."
      },
      {
        id: "EVID-004-02",
        type: "Memory Extraction",
        url: "images/TF-004_redline_real_02.png",
        title: "RedLine Browser Credential Vault Grabbing",
        caption: "Forensic memory trace extracting DPAPI-protected credentials, session cookies, and cryptocurrency wallets."
      },
      {
        id: "EVID-004-03",
        type: "Architecture Schematic",
        url: "images/TF-004_redline_arch.svg",
        title: "RedLine Stealer Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Direct TCP, WCF Endpoints, Telegram Exfiltration command infrastructure."
      }
    ],
    en: {
      type: "InfoStealer",
      summary: "The definitive staple infostealer responsible for massive historical credential breaches.",
      desc: "A veteran .NET infostealer designed to harvest credentials, autofill data, credit cards, cryptocurrency wallets, and comprehensive hardware fingerprints.",
      tech: [
        "Language: C# (.NET Framework)",
        "Architecture: WCF (Windows Communication Foundation) client-server pipeline",
        "C2 Protocol: Direct TCP connections transmitting serialized XML/SOAP structures",
        "Capabilities: System inventory, browser vault decryption, FTP/VPN credential exfiltration",
        "Evasion: Relies on external third-party commercial crypting services"
      ],
      propagation: "Delivered via malicious Google Ads, cracked gaming utilities, and phishing attachments.",
      defense: [
        "Purge stored browser passwords and enforce managed enterprise password vaults.",
        "Detect and restrict direct non-standard TCP outbound traffic from client endpoints.",
        "Deploy behavioral EDR monitoring targeting unmanaged .NET assembly loads."
      ],
      whyWatch: "The backbone of initial access broker (IAB) credential log supply chains in 2026."
    },
    sources: [
      { name: "Mandiant RedLine Profile", type: "Security" },
      { name: "Microsoft Security Threat Analytics", type: "Security" }
    ]
  },
  {
    id: "TF-005",
    num: "005",
    name: "Vidar Stealer",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Dead-Drop Resolver C2",
    c2: "Steam Profiles, Mastodon, Telegram, HTTP POST",
    mitre: ["T1102.001", "T1555", "T1059", "T1083"],
    image: "images/TF-005_vidar_real_01.png",
    imageCaption: "Vidar Dead-Drop Resolver Telemetry",
    gallery: [
      {
        id: "EVID-005-01",
        type: "C2 Telemetry",
        url: "images/TF-005_vidar_real_01.png",
        title: "Vidar Dead-Drop Resolver Telemetry",
        caption: "ANY.RUN network capture displaying Telegram channel lookups used as dead-drop resolvers for C2 IP address retrieval."
      },
      {
        id: "EVID-005-02",
        type: "Payload Execution",
        url: "images/TF-005_vidar_real_02.png",
        title: "Vidar Stealer SQLite Harvesting Routine",
        caption: "Memory analysis showing automated extraction of login data from Chromium and Gecko-based browser databases."
      },
      {
        id: "EVID-005-03",
        type: "Architecture Schematic",
        url: "images/TF-005_vidar_arch.svg",
        title: "Vidar Stealer Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Steam Profiles, Mastodon, Telegram, HTTP POST command infrastructure."
      }
    ],
    en: {
      type: "InfoStealer / Spyware",
      summary: "High-grade C++ stealer famous for weaponizing Steam and Mastodon profiles as dead-drop resolvers.",
      desc: "Fork of Arkei stealer engineered to evade network defenses by embedding encrypted C2 addresses into public social profiles before initiating credential dumping.",
      tech: [
        "Language: C++",
        "Architecture: Modular DLL injection with dynamic API resolution",
        "C2 Protocol: Dead-drop resolvers (Steam, Telegram, Mastodon bio text) returning final IP",
        "Capabilities: Telegram/Signal/WhatsApp desktop extraction, crypto keys, screenshotting",
        "Evasion: Aggressive self-deletion routine using cmd.exe /c timeout commands"
      ],
      propagation: "Packaged within malicious MSI installers and compromised software repacks.",
      defense: [
        "Monitor corporate traffic resolving public social profiles carrying hex strings.",
        "Restrict access to desktop messaging clients without central authentication.",
        "Inspect transient process trees executing automated cleanup scripts."
      ],
      whyWatch: "A resilient survivor continually refining multi-stage dead-drop infrastructure in 2026."
    },
    sources: [
      { name: "BlackBerry Threat Research Vidar File", type: "Security" },
      { name: "Trend Micro Research Report", type: "Security" }
    ]
  },
  {
    id: "TF-006",
    num: "006",
    name: "Agent Tesla",
    category: "Spyware",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED",
    lang: ".NET (C# / VB.NET)",
    arch: "Keylogger & Credential Harvester",
    c2: "SMTP, FTP, Telegram Webhooks, Discord API",
    mitre: ["T1056.001", "T1005", "T1071.003", "T1053"],
    image: "images/TF-006_agenttesla_real_01.png",
    imageCaption: "Agent Tesla Process Tree & Weaponized Document",
    gallery: [
      {
        id: "EVID-006-01",
        type: "Execution Chain",
        url: "images/TF-006_agenttesla_real_01.png",
        title: "Agent Tesla Process Tree & Weaponized Document",
        caption: "Forensic sandbox process hierarchy showing weaponized office document execution and payload staging."
      },
      {
        id: "EVID-006-02",
        type: "Exfiltration Module",
        url: "images/TF-006_agenttesla_real_02.png",
        title: "Agent Tesla SMTP Exfiltration Routine",
        caption: "Decompiled .NET routine responsible for packaging keystroke logs and dispatching them via TLS SMTP channels."
      },
      {
        id: "EVID-006-03",
        type: "Architecture Schematic",
        url: "images/TF-006_agenttesla_arch.svg",
        title: "Agent Tesla Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and SMTP, FTP, Telegram Webhooks, Discord API command infrastructure."
      }
    ],
    en: {
      type: "Advanced Spyware & Keylogger",
      summary: "Commercial-grade spyware specialized in silent keystroke logging and SMTP-based corporate exfiltration.",
      desc: "A persistent .NET-based threat actor favorite tailored for business email compromise (BEC) and supply chain reconnaissance, exfiltrating logs through compromised SMTP relays.",
      tech: [
        "Language: VB.NET / C#",
        "Architecture: Comprehensive surveillance engine with layered crypters",
        "C2 Protocol: Exfiltration over SMTP, FTP, Telegram bots, and HTTP POST",
        "Capabilities: Real-time keylogging, periodic screenshots, mail client credential theft",
        "Evasion: Process hollowing targeting legitimate binaries (vbc.exe, RegAsm.exe)"
      ],
      propagation: "Spear-phishing emails containing spoofed RFQs, invoices, or delivery notices in ISO/RAR attachments.",
      defense: [
        "Alert on unauthorized direct outbound SMTP/FTP connections originating from workstations.",
        "Block container attachment mounting (ISO, VHD) at the mail gateway.",
        "Implement strict EDR defenses against hollowed .NET process executions."
      ],
      whyWatch: "The undisputed workhorse for BEC operations and corporate credential theft in 2026."
    },
    sources: [
      { name: "Fortinet FortiGuard Labs Agent Tesla Report", type: "Security" },
      { name: "Cisco Talos Intelligence", type: "Security" }
    ]
  },
  {
    id: "TF-007",
    num: "007",
    name: "Remcos RAT",
    category: "RAT",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED",
    lang: "C++",
    arch: "Commercial Administration Tool (Abused)",
    c2: "Direct Encrypted TLS, Dynamic DNS, SOCKS5 Proxy",
    mitre: ["T1056.001", "T1059.003", "T1090.003", "T1547.001"],
    image: "images/TF-007_remcos_real_01.png",
    imageCaption: "Remcos Professional Client Builder & Evasion Configurator",
    gallery: [
      {
        id: "EVID-007-01",
        type: "Builder UI",
        url: "images/TF-007_remcos_real_01.png",
        title: "Remcos Professional Client Builder & Evasion Configurator",
        caption: "Builder interface displaying TLS encryption parameters, rootkit cloaking, watchdog persistence, and anti-analysis options."
      },
      {
        id: "EVID-007-02",
        type: "Operator Console",
        url: "images/TF-007_remcos_real_02.svg",
        title: "Remcos Remote Administration Management Console",
        caption: "Management console monitoring connected remote bots, system telemetry, and active surveillance streams."
      },
      {
        id: "EVID-007-03",
        type: "Architecture Schematic",
        url: "images/TF-007_remcos_arch.svg",
        title: "Remcos RAT Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Direct Encrypted TLS, Dynamic DNS, SOCKS5 Proxy command infrastructure."
      }
    ],
    en: {
      type: "Remote Access Trojan (RAT)",
      summary: "Commercial remote management tool weaponized into one of the most potent state-sponsored and cybercrime RATs.",
      desc: "High-performance native C++ RAT disguised as legal software, offering invasive remote desktop, webcam/audio wiretapping, and internal proxy pivoting.",
      tech: [
        "Language: Pure native C++",
        "Architecture: Comprehensive remote administration suite utilizing RC4 encryption",
        "C2 Protocol: Direct custom socket TLS, dynamic DNS, integrated SOCKS5 reverse proxies",
        "Capabilities: Hidden surveillance, registry manipulation, remote script execution, UAC bypass",
        "Evasion: Commonly staged through advanced crypters and polymorphic loaders like GuLoader"
      ],
      propagation: "Targeted spear-phishing campaigns masquerading as payment receipts and bank transfers.",
      defense: [
        "Enforce strict egress filtering blocking non-whitelisted dynamic DNS domains.",
        "Restrict standard user permissions to prevent unauthorized process elevation.",
        "Deploy endpoint telemetry monitoring unauthorized microphone and camera API hooks."
      ],
      whyWatch: "Flawless stability and rich reconnaissance capabilities cement its status in 2026 intrusions."
    },
    sources: [
      { name: "CISA Cybersecurity Advisory on Remcos", type: "Security" },
      { name: "Unit 42 Palo Alto Networks Analysis", type: "Security" }
    ]
  },
  {
    id: "TF-008",
    num: "008",
    name: "XWorm",
    category: "RAT",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED",
    lang: "C# (.NET)",
    arch: "Worm / RAT / DDoS Hybrid",
    c2: "AES Encrypted TCP, Telegram, Pastebin Dead-Drop",
    mitre: ["T1059", "T1055", "T1091", "T1498"],
    image: "images/TF-008_xworm_real_01.png",
    imageCaption: "XWorm Advanced Payload Builder Interface",
    gallery: [
      {
        id: "EVID-008-01",
        type: "Builder UI",
        url: "images/TF-008_xworm_real_01.png",
        title: "XWorm Advanced Payload Builder Interface",
        caption: "Configurator interface setting USB spreaders, clipper addresses, ransomware routines, and HVNC modules."
      },
      {
        id: "EVID-008-02",
        type: "Clipper Module",
        url: "images/TF-008_xworm_real_02.svg",
        title: "XWorm Cryptocurrency Clipper Memory Routine",
        caption: "Disassembly showing clipboard regex monitoring for Bitcoin, Ethereum, and Monero wallet string replacement."
      },
      {
        id: "EVID-008-03",
        type: "Architecture Schematic",
        url: "images/TF-008_xworm_arch.svg",
        title: "XWorm Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and AES Encrypted TCP, Telegram, Pastebin Dead-Drop command infrastructure."
      }
    ],
    en: {
      type: "RAT & Modular Worm",
      summary: "Hybrid RAT and worm known for rapid USB spreading, crypto-clipping, and volumetric DDoS capabilities.",
      desc: "A feature-packed .NET commodity threat widely circulated in underground forums, featuring automated removable drive replication, cryptocurrency address spoofing, and remote execution.",
      tech: [
        "Language: C# (.NET Framework)",
        "Architecture: Modular architecture loading dynamic assemblies from memory",
        "C2 Protocol: AES-encrypted TCP communication with Pastebin dead-drop configuration resolvers",
        "Capabilities: Crypto clipper, worm-like USB propagation, volumetric DDoS, ransomware module",
        "Evasion: Windows Defender tampering and scheduled task persistence hooks"
      ],
      propagation: "Infected USB storage drives, malicious torrent packages, and cracked applications.",
      defense: [
        "Enforce organizational policies disabling USB mass storage AutoRun/AutoPlay.",
        "Inspect system clipboard monitoring hooks for unauthorized crypto-address mutations.",
        "Audit Windows Task Scheduler for anomalous recurrent PowerShell or MSBuild scripts."
      ],
      whyWatch: "Rapid feature proliferation makes XWorm a chaotic and unpredictable threat in 2026."
    },
    sources: [
      { name: "Check Point Research on XWorm Proliferation", type: "Security" },
      { name: "Morphisec Threat Labs Report", type: "Security" }
    ]
  },
  {
    id: "TF-009",
    num: "009",
    name: "DarkGate",
    category: "Loader",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "Borland Delphi / AutoIt",
    arch: "Multi-Stage Loader & RAT",
    c2: "Custom HTTP Encryption, Obfuscated Query Params",
    mitre: ["T1059.001", "T1055.001", "T1027", "T1105"],
    image: "images/TF-009_darkgate_real_01.png",
    imageCaption: "DarkGate Malicious MSI & AutoIt Lure",
    gallery: [
      {
        id: "EVID-009-01",
        type: "Infection Vector",
        url: "images/TF-009_darkgate_real_01.png",
        title: "DarkGate Malicious MSI & AutoIt Lure",
        caption: "Malwarebytes forensic capture showing rogue MSI installer dropping obfuscated AutoIt interpreter script stubs."
      },
      {
        id: "EVID-009-02",
        type: "Config Extractor",
        url: "images/TF-009_darkgate_real_02.png",
        title: "DarkGate Extracted C2 Configuration Parameters",
        caption: "Automated extractor output displaying AES-encrypted C2 servers, botnet flags, and evasion switches."
      },
      {
        id: "EVID-009-03",
        type: "Architecture Schematic",
        url: "images/TF-009_darkgate_arch.svg",
        title: "DarkGate Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Custom HTTP Encryption, Obfuscated Query Params command infrastructure."
      },
      {
        id: "EVID-009-04",
        type: "Network Packet Capture",
        url: "images/darkgate_04_traffic.jpeg",
        title: "DarkGate HTTP C2 Request Header Analysis",
        caption: "Raw packet inspection showing HTTP POST parameters and custom User-Agent beacons."
      }
    ],
    en: {
      type: "Advanced Loader & Commodity RAT",
      summary: "High-tier commodity loader leased on cybercrime forums to deploy ransomware and enterprise backdoors.",
      desc: "A sophisticated Delphi-engineered initial access loader utilizing AutoIt script wrappers to evade AV/EDR scrutiny and stage secondary payloads.",
      tech: [
        "Language: Borland Delphi with nested AutoIt stages",
        "Architecture: Multi-stage payload delivery pipeline",
        "C2 Protocol: Obfuscated HTTP communication with dynamic XOR encryption keys",
        "Capabilities: Secondary payload drops, browser theft, hidden VNC, cryptomining",
        "Evasion: Heavy anti-VM, anti-sandbox checks, and AMSI memory patching"
      ],
      propagation: "Compromised Microsoft Teams direct messaging chats, SEO malvertising, and PDF phishing.",
      defense: [
        "Block standalone AutoIt interpreter binaries on non-developer enterprise assets.",
        "Implement DLP and attachment screening on collaboration suites (Teams, Slack).",
        "Inspect process execution chains spawning suspicious cscript or AutoIt interpreters."
      ],
      whyWatch: "A premier initial access vehicle chosen by high-profile ransomware affiliates in 2026."
    },
    sources: [
      { name: "WithSecure Intelligence DarkGate Deep Dive", type: "Security" },
      { name: "Trellix Threat Labs Investigation", type: "Security" }
    ]
  },
  {
    id: "TF-010",
    num: "010",
    name: "Rhadamanthys",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Modular Architecture & Virtual Machine",
    c2: "Custom TLS-like Protocol, Hidden TCP Handshake",
    mitre: ["T1555", "T1027.004", "T1055", "T1082"],
    image: "images/TF-010_rhadamanthys_real_01.png",
    imageCaption: "Rhadamanthys Stealer Operator Panel Interface",
    gallery: [
      {
        id: "EVID-010-01",
        type: "Builder UI",
        url: "images/TF-010_rhadamanthys_real_01.png",
        title: "Rhadamanthys Stealer Operator Panel Interface",
        caption: "Web-based management console tracking active victim infections, geolocations, and extracted credential counts."
      },
      {
        id: "EVID-010-02",
        type: "Memory VM",
        url: "images/TF-010_rhadamanthys_real_02.svg",
        title: "Rhadamanthys Custom Virtual Machine Architecture",
        caption: "Disassembly showing custom bytecode VM interpreter designed to thwart static analysis and heuristic emulators."
      },
      {
        id: "EVID-010-03",
        type: "Architecture Schematic",
        url: "images/TF-010_rhadamanthys_arch.svg",
        title: "Rhadamanthys Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Custom TLS-like Protocol, Hidden TCP Handshake command infrastructure."
      }
    ],
    en: {
      type: "Advanced InfoStealer",
      summary: "Elite infostealer powered by a custom virtual machine designed to frustrate reverse engineers.",
      desc: "A highly sophisticated stealer engineered in modern C++ utilizing a custom in-memory bytecode interpreter, setting a high bar for static and dynamic analysis evasion.",
      tech: [
        "Language: Modern C++",
        "Architecture: Custom virtual machine (VM) bytecode execution engine",
        "C2 Protocol: Handcrafted encryption scheme mimicking TLS protocol handshake",
        "Capabilities: Extraction of KeePass vaults, boutique crypto wallets, browser profiles, and email tokens",
        "Evasion: Strictly in-memory execution leaving zero disk artifacts"
      ],
      propagation: "Malicious Google Ads campaigns masquerading as legitimate software (Zoom, AnyDesk, Notepad++).",
      defense: [
        "Deploy enterprise ad-blocking to nullify malicious search engine redirect funnels.",
        "Employ memory forensic scanners capable of identifying unpackers executing unmapped code.",
        "Protect password manager master databases with hardware keys."
      ],
      whyWatch: "Sets the technical benchmark for evasion sophistication among 2026 infostealers."
    },
    sources: [
      { name: "Recorded Future Rhadamanthys Analysis", type: "Security" },
      { name: "SANS Internet Storm Center Diary", type: "Security" }
    ]
  },
  {
    id: "TF-011",
    num: "011",
    name: "Stealc",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "MONITORED",
    lang: "C",
    arch: "Lightweight Modular Stealer",
    c2: "RC4 Encrypted HTTP POST",
    mitre: ["T1555.003", "T1082", "T1071.001"],
    image: "images/TF-011_stealc_real_01.png",
    imageCaption: "Stealc C2 Communication Protocol Analysis",
    gallery: [
      {
        id: "EVID-011-01",
        type: "C2 Config",
        url: "images/TF-011_stealc_real_01.png",
        title: "Stealc C2 Communication Protocol Analysis",
        caption: "ANY.RUN forensic capture showing RC4 string decryption and endpoint registration with command-and-control servers."
      },
      {
        id: "EVID-011-02",
        type: "Target Grabbing",
        url: "images/TF-011_stealc_real_02.png",
        title: "Stealc Modular Data Harvesting Pipeline",
        caption: "Execution capture showing file-grabbing rules targeting browser extensions, Discord tokens, and crypto wallet paths."
      },
      {
        id: "EVID-011-03",
        type: "Architecture Schematic",
        url: "images/TF-011_stealc_arch.svg",
        title: "Stealc Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and RC4 Encrypted HTTP POST command infrastructure."
      }
    ],
    en: {
      type: "InfoStealer",
      summary: "Lightweight and agile C-based stealer inspired by Vidar, popular for low operational overhead.",
      desc: "Delivers tailored DLL plugins based on dynamic host reconnaissance to harvest 75+ browsers and countless crypto wallets.",
      tech: ["Language: Pure C", "C2 Protocol: RC4 encrypted HTTP POST", "Capabilities: Steals from 75+ browsers, crypto extensions, desktop software"],
      propagation: "Cracked gaming portals and YouTube tutorial links.",
      defense: ["Enforce enterprise DNS filtering and web reputation engines."],
      whyWatch: "Extremely popular entry-level tool for emerging threat actors in 2026."
    },
    sources: [{ name: "SEKOIA.IO Stealc Intelligence", type: "Security" }]
  },
  {
    id: "TF-012",
    num: "012",
    name: "Havoc C2",
    category: "C2 Framework",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED",
    lang: "C / Go / Python",
    arch: "Modern Adversary Emulation Framework",
    c2: "Demon Agent, Malleable HTTP/HTTPS, SMB Pipes",
    mitre: ["T1059", "T1055", "T1090", "T1573"],
    image: "images/TF-012_havoc_real_01.png",
    imageCaption: "Havoc Framework Demon Payload Configurator",
    gallery: [
      {
        id: "EVID-012-01",
        type: "Payload Generator",
        url: "images/TF-012_havoc_real_01.png",
        title: "Havoc Framework Demon Payload Configurator",
        caption: "Official Havoc client UI configuring Demon agent sleep obfuscation, indirect syscalls, and x64 shellcode injection stubs."
      },
      {
        id: "EVID-012-02",
        type: "Operator Console",
        url: "images/TF-012_havoc_real_02.png",
        title: "Havoc C2 Interactive Session Console",
        caption: "Operator UI managing compromised enterprise hosts, active Demon beacons, and lateral movement listeners."
      },
      {
        id: "EVID-012-03",
        type: "Architecture Schematic",
        url: "images/TF-012_havoc_arch.svg",
        title: "Havoc C2 Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Demon Agent, Malleable HTTP/HTTPS, SMB Pipes command infrastructure."
      }
    ],
    en: {
      type: "Command & Control (C2) Framework",
      summary: "Modern open-source adversary emulation platform rapidly adopted by threat actors as a Cobalt Strike alternative.",
      desc: "A post-exploitation framework with an advanced native C agent ('Demon') featuring cutting-edge EDR evasion and sleep obfuscation.",
      tech: ["Language: C (Demon Agent), Go (Server)", "C2 Protocol: Malleable HTTPS, SMB Named Pipes", "Capabilities: Indirect syscalls, stack spoofing, sleep obfuscation"],
      propagation: "Staged post-compromise through loaders and initial access vectors.",
      defense: ["Detect sleep obfuscation anomalies and thread execution in unbacked memory."],
      whyWatch: "The premier modern C2 framework challenging defensive telemetry in 2026."
    },
    sources: [{ name: "Zscaler ThreatLabz Havoc Deep Dive", type: "Security" }]
  },
  {
    id: "TF-013",
    num: "013",
    name: "Sliver C2",
    category: "C2 Framework",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED",
    lang: "Go",
    arch: "Multi-Platform Red Team Framework",
    c2: "mTLS, WireGuard, HTTP/HTTPS, DNS Canaries",
    mitre: ["T1071", "T1573.002", "T1059", "T1021"],
    image: "images/TF-013_sliver_real_01.png",
    imageCaption: "Sliver C2 Interactive Command Console",
    gallery: [
      {
        id: "EVID-013-01",
        type: "Operator Console",
        url: "images/TF-013_sliver_real_01.png",
        title: "Sliver C2 Interactive Command Console",
        caption: "Operator shell session showing active multiplayer beacons, WireGuard tunnels, and mTLS listener parameters."
      },
      {
        id: "EVID-013-02",
        type: "Injection Routine",
        url: "images/TF-013_sliver_real_02.svg",
        title: "Sliver Process Injection & Evasion Engine",
        caption: "Technical visualization of indirect syscall execution and thread stack spoofing mechanisms."
      },
      {
        id: "EVID-013-03",
        type: "Architecture Schematic",
        url: "images/TF-013_sliver_arch.svg",
        title: "Sliver C2 Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and mTLS, WireGuard, HTTP/HTTPS, DNS Canaries command infrastructure."
      }
    ],
    en: {
      type: "C2 Framework (Cross-Platform)",
      summary: "Cross-platform Go-based adversary emulation framework utilizing WireGuard and mTLS channels.",
      desc: "Created by BishopFox, widely adopted by red teams and APTs for cross-platform enterprise compromise.",
      tech: ["Language: Go", "C2 Protocol: Mutual TLS, WireGuard tunnels, DNS canary tunnels", "Capabilities: Dynamic payload stagers, pivot listeners, lateral movement"],
      propagation: "Deployed post-exploitation via web shell deployment or credential replay.",
      defense: ["Inspect network perimeters for anomalous WireGuard encapsulation and untrusted mTLS handshakes."],
      whyWatch: "Major player in enterprise post-exploitation campaigns in 2026."
    },
    sources: [{ name: "Microsoft Security Sliver Detection Guidance", type: "Security" }]
  },
  {
    id: "TF-014",
    num: "014",
    name: "Mythic C2",
    category: "C2 Framework",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "MONITORED",
    lang: "Python / Go / Docker",
    arch: "Microservices Collaborative C2",
    c2: "Modular Agent Ecosystem, WebSocket, WebDAV",
    mitre: ["T1071.001", "T1059", "T1055"],
    image: "images/TF-014_mythic_real_01.svg",
    imageCaption: "Mythic C2 Operation Management Dashboard",
    gallery: [
      {
        id: "EVID-014-01",
        type: "Operator Dashboard",
        url: "images/TF-014_mythic_real_01.svg",
        title: "Mythic C2 Operation Management Dashboard",
        caption: "Web interface aggregating active agent callbacks, tasking queues, and modular payload build profiles."
      },
      {
        id: "EVID-014-02",
        type: "Payload Architecture",
        url: "images/TF-014_mythic_real_02.svg",
        title: "Mythic Modular Agent Communication Engine",
        caption: "C2 communication trace showing JSON-RPC tasking and staging across custom translation containers."
      },
      {
        id: "EVID-014-03",
        type: "Architecture Schematic",
        url: "images/TF-014_mythic_arch.svg",
        title: "Mythic C2 Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Modular Agent Ecosystem, WebSocket, WebDAV command infrastructure."
      }
    ],
    en: {
      type: "C2 Framework",
      summary: "Microservices-based collaborative C2 platform supporting diverse agent payloads across OS types.",
      desc: "Enables multi-operator campaigns with plug-and-play agents for macOS, Linux, and Windows.",
      tech: ["Language: Python, Go, Docker", "C2 Protocol: WebSockets, HTTP, custom RPC profiles", "Capabilities: Highly modular agent matrix (Apollo, Poseidon, Athena)"],
      propagation: "Targeted intrusions and high-tier red teaming.",
      defense: ["Inspect sustained bidirectional WebSocket sessions to unclassified endpoints."],
      whyWatch: "Rapidly expanding collaborative ecosystem for advanced threat simulations in 2026."
    },
    sources: [{ name: "Mythic Project Documentation & Threat Intel", type: "Security" }]
  },
  {
    id: "TF-015",
    num: "015",
    name: "QuasarRAT",
    category: "RAT",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "TESTED",
    lang: "C# (.NET)",
    arch: "Classic Open Source RAT",
    c2: "AES-128 Encrypted TCP Sockets",
    mitre: ["T1056.001", "T1059.003", "T1082"],
    image: "images/TF-015_quasarrat_real_01.png",
    imageCaption: "QuasarRAT Open-Source Builder & Certificate Generator",
    gallery: [
      {
        id: "EVID-015-01",
        type: "Builder UI",
        url: "images/TF-015_quasarrat_real_01.png",
        title: "QuasarRAT Open-Source Builder & Certificate Generator",
        caption: "Client builder GUI configuring TLS certificate pinning, startup registry persistence, and keylogger hooks."
      },
      {
        id: "EVID-015-02",
        type: "Surveillance Module",
        url: "images/TF-015_quasarrat_real_02.svg",
        title: "QuasarRAT Surveillance & File Manager Interface",
        caption: "Interactive operator panel monitoring victim file systems, reverse socks proxies, and active processes."
      },
      {
        id: "EVID-015-03",
        type: "Architecture Schematic",
        url: "images/TF-015_quasarrat_arch.svg",
        title: "QuasarRAT Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and AES-128 Encrypted TCP Sockets command infrastructure."
      }
    ],
    en: {
      type: "Remote Access Trojan (RAT)",
      summary: "Iconic open-source .NET RAT that spawned numerous derivative malware strains across the globe.",
      desc: "A stable, lightweight management tool frequently recompiled by cybercrime groups for remote desktop and credential theft.",
      tech: ["Language: C# (.NET)", "C2 Protocol: AES-128 encrypted raw TCP sockets", "Capabilities: Remote desktop, file transfer, reverse proxy, credential recovery"],
      propagation: "Phishing emails and weaponized Office documents.",
      defense: ["Enforce network egress rules and signature-based scanning for Quasar certificates."],
      whyWatch: "An enduring grandfather code-base for emerging threat actors in 2026."
    },
    sources: [{ name: "CISA QuasarRAT Advisory", type: "Security" }]
  },
  {
    id: "TF-016",
    num: "016",
    name: "Warzone RAT / Ave Maria",
    category: "RAT",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Commercial Commodity RAT",
    c2: "Custom Encrypted Protocol over TCP",
    mitre: ["T1056", "T1548.002", "T1555"],
    image: "images/TF-016_warzone_real_01.png",
    imageCaption: "Warzone RAT (Ave Maria) Builder Interface",
    gallery: [
      {
        id: "EVID-016-01",
        type: "Builder UI",
        url: "images/TF-016_warzone_real_01.png",
        title: "Warzone RAT (Ave Maria) Builder Interface",
        caption: "Configurator GUI showing UAC bypass method selection, privilege escalation hooks, and password recovery modules."
      },
      {
        id: "EVID-016-02",
        type: "Privilege Escalation",
        url: "images/TF-016_warzone_real_02.svg",
        title: "Warzone RAT AveMaria Memory Persistence Engine",
        caption: "Forensic disassembly showing task scheduler registration and explorer.exe process hollowing routines."
      },
      {
        id: "EVID-016-03",
        type: "Architecture Schematic",
        url: "images/TF-016_warzone_arch.svg",
        title: "Warzone RAT / Ave Maria Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Custom Encrypted Protocol over TCP command infrastructure."
      }
    ],
    en: {
      type: "Remote Access Trojan",
      summary: "Infamous commodity RAT engineered for out-of-the-box UAC bypass across all Windows builds.",
      desc: "A compact C++ Trojan boasting reliable credential harvesting from modern browsers and stealthy privilege escalation.",
      tech: ["Language: C++", "C2 Protocol: Custom encrypted TCP stream", "Capabilities: Automated UAC bypass, browser password dumping, silent remote desktop"],
      propagation: "Financial and governmental spear-phishing campaigns.",
      defense: ["Lock down UAC elevation thresholds and restrict unauthenticated privilege inheritance."],
      whyWatch: "Cracked variants continue to propagate heavily across cybercrime undergrounds in 2026."
    },
    sources: [{ name: "US DOJ Warzone RAT Takedown Release & Analysis", type: "Security" }]
  },
  {
    id: "TF-017",
    num: "017",
    name: "GuLoader / CloudEyE",
    category: "Loader",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "Visual Basic 6.0 / Assembly",
    arch: "Polymorphic Shellcode Downloader",
    c2: "Google Drive, OneDrive, Encrypted Shellcode Delivery",
    mitre: ["T1027", "T1055.002", "T1105", "T1497"],
    image: "images/TF-017_guloader_real_01.jpg",
    imageCaption: "GuLoader (CloudEyE) Multi-Stage Shellcode Chain",
    gallery: [
      {
        id: "EVID-017-01",
        type: "Execution Chain",
        url: "images/TF-017_guloader_real_01.jpg",
        title: "GuLoader (CloudEyE) Multi-Stage Shellcode Chain",
        caption: "ANY.RUN threat infographic detailing VBS dropper, registry payload storage, and shellcode injection sequence."
      },
      {
        id: "EVID-017-02",
        type: "Anti-Analysis Routine",
        url: "images/TF-017_guloader_real_02.png",
        title: "GuLoader Vectored Exception Handling (VEH) Check",
        caption: "Process memory disassembly showing hardware breakpoint detection and anti-debugging exception routines."
      },
      {
        id: "EVID-017-03",
        type: "Architecture Schematic",
        url: "images/TF-017_guloader_arch.svg",
        title: "GuLoader / CloudEyE Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Google Drive, OneDrive, Encrypted Shellcode Delivery command infrastructure."
      }
    ],
    en: {
      type: "Advanced Polymorphic Loader",
      summary: "Formidable polymorphic shellcode downloader abusing legitimate cloud storage to stage malware.",
      desc: "One of the most evasive droppers in circulation, packing immense anti-analysis routines and pulling encrypted shellcode from Google Drive or OneDrive.",
      tech: ["Language: Visual Basic 6.0 / Assembly", "C2 Protocol: Encrypted payloads hosted on public cloud storage", "Capabilities: Hyper-evasion, anti-VM, anti-debugging, memory process hollowing"],
      propagation: "Weaponized NSIS installers, VBS scripts, and archive email attachments.",
      defense: ["Detect unbacked memory shellcode executions and inspect corporate cloud ingress for encrypted payloads."],
      whyWatch: "The gold standard for EDR evasion throughout 2026."
    },
    sources: [{ name: "CrowdStrike GuLoader Technical Advisory", type: "Security" }]
  },
  {
    id: "TF-018",
    num: "018",
    name: "Pikabot",
    category: "Loader",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Modular Bot / Loader",
    c2: "HTTPS with RC4 Encrypted JSON Payloads",
    mitre: ["T1059", "T1055", "T1027", "T1082"],
    image: "images/TF-018_pikabot_real_01.svg",
    imageCaption: "Pikabot Modular Core Loader Architecture",
    gallery: [
      {
        id: "EVID-018-01",
        type: "Loader Routine",
        url: "images/TF-018_pikabot_real_01.svg",
        title: "Pikabot Modular Core Loader Architecture",
        caption: "Forensic sandbox process tree displaying encrypted blob unpacking and DLL injection into legitimate system processes."
      },
      {
        id: "EVID-018-02",
        type: "C2 Protocol",
        url: "images/TF-018_pikabot_real_02.svg",
        title: "Pikabot Network Beacon & RC4 Decryption",
        caption: "Network capture analyzing AES-CBC C2 beaconing structure and infected endpoint fingerprinting."
      },
      {
        id: "EVID-018-03",
        type: "Architecture Schematic",
        url: "images/TF-018_pikabot_arch.svg",
        title: "Pikabot Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTPS with RC4 Encrypted JSON Payloads command infrastructure."
      }
    ],
    en: {
      type: "Modular Loader / Backdoor",
      summary: "Advanced modular loader mirroring Qakbot behaviors, engineered to stage ransomware payloads.",
      desc: "Conducts deep environment verification, language checks, and indirect system calls before establishing encrypted command channels.",
      tech: ["Language: C++", "C2 Protocol: HTTPS transmitting RC4-encrypted JSON objects", "Capabilities: Anti-analysis, thread hijacking integration, modular code drops"],
      propagation: "Email thread hijacking with malicious PDF/JS attachments.",
      defense: ["Educate users against thread-hijacked emails and deploy behavioral memory scanning."],
      whyWatch: "A premier ransomware delivery pipeline in 2026."
    },
    sources: [{ name: "Cofense Pikabot Defense Briefing", type: "Security" }]
  },
  {
    id: "TF-019",
    num: "019",
    name: "Qakbot / QBot",
    category: "Loader",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED_PRIOR",
    lang: "C++",
    arch: "Banking Trojan turned Enterprise Loader",
    c2: "Tiered Botnet, Compromised WordPress Sites, Custom TLS",
    mitre: ["T1566.001", "T1055", "T1090", "T1071"],
    image: "images/TF-019_qakbot_real_01.svg",
    imageCaption: "Qakbot (QBot) Core Web-Inject & Delivery Engine",
    gallery: [
      {
        id: "EVID-019-01",
        type: "Banking Module",
        url: "images/TF-019_qakbot_real_01.svg",
        title: "Qakbot (QBot) Core Web-Inject & Delivery Engine",
        caption: "Forensic memory trace showing thread hijacking and man-in-the-browser banking credential interception."
      },
      {
        id: "EVID-019-02",
        type: "Process Hollowing",
        url: "images/TF-019_qakbot_real_02.svg",
        title: "Qakbot Process Replacement in wermgr.exe",
        caption: "Process monitor telemetry tracking hollowed process creation and memory section remapping."
      },
      {
        id: "EVID-019-03",
        type: "Architecture Schematic",
        url: "images/TF-019_qakbot_arch.svg",
        title: "Qakbot / QBot Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Tiered Botnet, Compromised WordPress Sites, Custom TLS command infrastructure."
      }
    ],
    en: {
      type: "Banking Trojan & Enterprise Loader",
      summary: "Resilient botnet infrastructure resurrected following multinational law enforcement takedown actions.",
      desc: "Evolved from a banking Trojan into an enterprise-scale initial access vector delivering premier ransomware operations.",
      tech: ["Language: C++", "C2 Protocol: Multi-tier botnet abusing thousands of compromised web servers", "Capabilities: Thread hijacking, email exfiltration, credential harvesting, lateral spread"],
      propagation: "Malicious OneNote archives, ISO containers, and thread-hijacking phishing.",
      defense: ["Block script execution from temp paths and monitor wermgr.exe process injections."],
      whyWatch: "A masterclass in threat actor infrastructure resilience entering 2026."
    },
    sources: [{ name: "FBI / Europol Operation Duck Hunt Report", type: "Security" }]
  },
  {
    id: "TF-020",
    num: "020",
    name: "Emotet",
    category: "Botnet",
    status: "DORMANT",
    relevance: "MEDIUM",
    teamStatus: "TESTED_PRIOR",
    lang: "C++",
    arch: "Modular Infrastructure Botnet",
    c2: "Custom Encrypted Protocol over HTTP/HTTPS",
    mitre: ["T1566.001", "T1114", "T1071.001"],
    image: "images/TF-020_emotet_real_01.svg",
    imageCaption: "Emotet Epoch Tier-1 Command Infrastructure",
    gallery: [
      {
        id: "EVID-020-01",
        type: "Botnet Architecture",
        url: "images/TF-020_emotet_real_01.svg",
        title: "Emotet Epoch Tier-1 Command Infrastructure",
        caption: "Telemetry diagram illustrating compromised router proxy chains and automated spambot email harvesting modules."
      },
      {
        id: "EVID-020-02",
        type: "Payload Execution",
        url: "images/TF-020_emotet_real_02.svg",
        title: "Emotet Encrypted DLL Loader Disassembly",
        caption: "Disassembly showing control flow flattening and string decryption routines executing inside regsvr32.exe."
      },
      {
        id: "EVID-020-03",
        type: "Architecture Schematic",
        url: "images/TF-020_emotet_arch.svg",
        title: "Emotet Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Custom Encrypted Protocol over HTTP/HTTPS command infrastructure."
      }
    ],
    en: {
      type: "Modular Botnet & Spreader",
      summary: "Historically the world's most destructive botnet, serving as the blueprint for distributed cybercrime.",
      desc: "Massive automated malspam apparatus built to lease network access to ransomware operators worldwide.",
      tech: ["Language: C++", "C2 Protocol: Encrypted payload exchanges over decentralized web nodes", "Capabilities: Automated mail theft, mass spam generation, secondary payload drops"],
      propagation: "Macro-enabled Microsoft Office attachments and phishing URLs.",
      defense: ["Enforce strict macro blocking policies across all Office document formats."],
      whyWatch: "Essential historical baseline for understanding botnet infrastructure evolution."
    },
    sources: [{ name: "US-CERT Alert on Emotet Malware", type: "Security" }]
  },
  {
    id: "TF-021",
    num: "021",
    name: "LockBit 3.0",
    category: "Ransomware",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C / Assembly",
    arch: "Ransomware-as-a-Service (RaaS)",
    c2: "Tor Hidden Services, Decentralized Leaks Portals",
    mitre: ["T1486", "T1490", "T1083", "T1027"],
    image: "images/TF-021_lockbit_real_01.png",
    imageCaption: "LockBit 3.0 (Black) Execution Process Tree",
    gallery: [
      {
        id: "EVID-021-01",
        type: "Ransomware Execution",
        url: "images/TF-021_lockbit_real_01.png",
        title: "LockBit 3.0 (Black) Execution Process Tree",
        caption: "ANY.RUN sandbox capture showing service termination, shadow copy deletion, and high-speed file encryption."
      },
      {
        id: "EVID-021-02",
        type: "Leak Infrastructure",
        url: "images/TF-021_lockbit_real_02.png",
        title: "LockBit Darknet Tor Extortion Portal",
        caption: "Onion portal interface detailing ransom demands, countdown timers, and stolen proof-of-concept data archives."
      },
      {
        id: "EVID-021-03",
        type: "Architecture Schematic",
        url: "images/TF-021_lockbit_arch.svg",
        title: "LockBit 3.0 Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Tor Hidden Services, Decentralized Leaks Portals command infrastructure."
      }
    ],
    en: {
      type: "Ransomware-as-a-Service (RaaS)",
      summary: "The most prolific ransomware syndicate of the decade, featuring blinding encryption speeds and anti-analysis.",
      desc: "Employs multi-threaded hybrid encryption routines and double-extortion strategies, crippling enterprise environments in minutes.",
      tech: ["Language: C / Assembly", "C2 Protocol: Tor onion negotiation channels and automated leak mirrors", "Capabilities: High-speed multithreaded encryption, shadow copy purging, security service termination"],
      propagation: "Initial access broker leads, exploited VPN vulnerabilities, and compromised RDP credentials.",
      defense: ["Maintain strictly air-gapped immutable backups and mandate MFA on all remote access perimeters."],
      whyWatch: "Remains the defining enterprise ransomware threat shaping cyber defense strategies in 2026."
    },
    sources: [{ name: "CISA / FBI LockBit 3.0 Joint Advisory", type: "Security" }]
  },
  {
    id: "TF-022",
    num: "022",
    name: "BlackCat / ALPHV",
    category: "Ransomware",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "Rust",
    arch: "Cross-Platform Ransomware (Windows / Linux / ESXi)",
    c2: "Tor Onion Nodes, REST API Command Channels",
    mitre: ["T1486", "T1082", "T1070", "T1562.001"],
    image: "images/TF-022_blackcat_real_01.png",
    imageCaption: "BlackCat (ALPHV) Rust CLI Execution Parameters",
    gallery: [
      {
        id: "EVID-022-01",
        type: "Execution Flags",
        url: "images/TF-022_blackcat_real_01.png",
        title: "BlackCat (ALPHV) Rust CLI Execution Parameters",
        caption: "Forensic terminal capture displaying command-line switches for domain escalation, safemode reboot, and shadow wipe."
      },
      {
        id: "EVID-022-02",
        type: "Ransom Artifact",
        url: "images/TF-022_blackcat_real_02.svg",
        title: "BlackCat Recover-My-Files Note & Tor Gateway",
        caption: "Generated ransom text note dropped on encrypted endpoints pointing to the ALPHV negotiation portal."
      },
      {
        id: "EVID-022-03",
        type: "Architecture Schematic",
        url: "images/TF-022_blackcat_arch.svg",
        title: "BlackCat / ALPHV Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Tor Onion Nodes, REST API Command Channels command infrastructure."
      }
    ],
    en: {
      type: "Cross-Platform Ransomware",
      summary: "First major enterprise ransomware engineered in Rust, heavily optimized for VMware ESXi virtual clusters.",
      desc: "Pioneered cross-platform flexibility across Windows and Linux, executing fine-grained encryption parameters.",
      tech: ["Language: Pure Rust", "C2 Protocol: Tor onion network and automated command-line APIs", "Capabilities: ESXi hypervisor shutdown, fast multi-core crypto, log sweeping"],
      propagation: "Credential theft, vulnerable edge devices, and supply chain intrusions.",
      defense: ["Isolate hypervisor management interfaces and enforce immutable snapshot retention."],
      whyWatch: "Catalyzed the modern shift toward memory-safe languages in offensive ransomware development."
    },
    sources: [{ name: "Microsoft Threat Intelligence ALPHV Rust Analysis", type: "Security" }]
  },
  {
    id: "TF-023",
    num: "023",
    name: "Akira",
    category: "Ransomware",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Targeted Enterprise Ransomware",
    c2: "Tor Chat Portal & Data Leak Site",
    mitre: ["T1486", "T1078", "T1133"],
    image: "images/TF-023_akira_real_01.svg",
    imageCaption: "Akira Ransomware Enterprise Encryption Routine",
    gallery: [
      {
        id: "EVID-023-01",
        type: "Extortion Engine",
        url: "images/TF-023_akira_real_01.svg",
        title: "Akira Ransomware Enterprise Encryption Routine",
        caption: "Forensic capture detailing C++ multi-threaded file encryption using ChaCha20 and RSA public key wrapping."
      },
      {
        id: "EVID-023-02",
        type: "Disassembly Analysis",
        url: "images/TF-023_akira_real_02.svg",
        title: "Akira Volume Shadow Deletion & Service Killer",
        caption: "IDA Pro disassembly highlighting PowerShell invocations wiping backup repositories and stopping SQL services."
      },
      {
        id: "EVID-023-03",
        type: "Architecture Schematic",
        url: "images/TF-023_akira_arch.svg",
        title: "Akira Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Tor Chat Portal & Data Leak Site command infrastructure."
      }
    ],
    en: {
      type: "Enterprise Ransomware",
      summary: "Aggressive ransomware syndicate exploiting Cisco VPN gateways to compromise enterprise networks.",
      desc: "Recognizable by its retro 1980s-themed leak portal, packing high-efficiency C++ payloads targeting Windows and Linux.",
      tech: ["Language: C++", "C2 Protocol: Tor-based negotiation forums and leak servers", "Capabilities: Selective partial encryption for speed, hypervisor VM purging"],
      propagation: "Exploiting unpatched Cisco ASA/FTD VPN appliances lacking MFA.",
      defense: ["Patch perimeter VPN gateways immediately and mandate phishing-resistant MFA."],
      whyWatch: "A dominant force driving mid-market enterprise ransomware incidents in 2026."
    },
    sources: [{ name: "CISA Akira Ransomware Advisory", type: "Security" }]
  },
  {
    id: "TF-024",
    num: "024",
    name: "Medusa",
    category: "Ransomware",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "High-Impact Ransomware Operation",
    c2: "Medusa Blog on Tor, Public Telegram Broadcasts",
    mitre: ["T1486", "T1562.001", "T1070.004"],
    image: "images/TF-024_medusa_real_01.svg",
    imageCaption: "Medusa Ransomware Blog & Victim Negotiation Console",
    gallery: [
      {
        id: "EVID-024-01",
        type: "Extortion Portal",
        url: "images/TF-024_medusa_real_01.svg",
        title: "Medusa Ransomware Blog & Victim Negotiation Console",
        caption: "Tor negotiation portal showing victim countdown timers, ransom payment deadlines, and published leak archives."
      },
      {
        id: "EVID-024-02",
        type: "Disassembly Analysis",
        url: "images/TF-024_medusa_real_02.svg",
        title: "Medusa Service Termination & Process Sweeper",
        caption: "Disassembly showing enumeration and killing of antivirus, database, and backup management services."
      },
      {
        id: "EVID-024-03",
        type: "Architecture Schematic",
        url: "images/TF-024_medusa_arch.svg",
        title: "Medusa Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Medusa Blog on Tor, Public Telegram Broadcasts command infrastructure."
      }
    ],
    en: {
      type: "Ransomware",
      summary: "Ruthless ransomware group hitting healthcare, education, and municipalities with public Telegram extortion.",
      desc: "Terminates over 200 system and security services before executing robust AES-256 file encryption.",
      tech: ["Language: C++", "C2 Protocol: Tor leak platform backed by public Telegram extortion channels", "Capabilities: Aggressive service termination, vssadmin deletion, network share encryption"],
      propagation: "Compromised administrative RDP credentials and exposed web application vulnerabilities.",
      defense: ["Block unauthorized vssadmin executions and implement strict network segmentation."],
      whyWatch: "Gains massive notoriety through brazen extortion tactics in 2026."
    },
    sources: [{ name: "Unit 42 Medusa Ransomware Analysis", type: "Security" }]
  },
  {
    id: "TF-025",
    num: "025",
    name: "Phobos / 8Base",
    category: "Ransomware",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Opportunistic Commodity Ransomware",
    c2: "Email Negotiation & Tor Mirrors",
    mitre: ["T1486", "T1133", "T1083"],
    image: "images/TF-025_phobos_real_01.svg",
    imageCaption: "Phobos / 8Base Ransomware Execution & Recovery Stub",
    gallery: [
      {
        id: "EVID-025-01",
        type: "Decryptor Utility",
        url: "images/TF-025_phobos_real_01.svg",
        title: "Phobos / 8Base Ransomware Execution & Recovery Stub",
        caption: "Forensic capture displaying file extension appending (.id[...].[email].phobos) and ransom note deployment."
      },
      {
        id: "EVID-025-02",
        type: "Network Telemetry",
        url: "images/TF-025_phobos_real_02.svg",
        title: "Phobos Command and Control Beaconing",
        caption: "Network telemetry trace tracking victim system registration and AES encryption key escrow exchange."
      },
      {
        id: "EVID-025-03",
        type: "Architecture Schematic",
        url: "images/TF-025_phobos_arch.svg",
        title: "Phobos / 8Base Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Email Negotiation & Tor Mirrors command infrastructure."
      }
    ],
    en: {
      type: "Commodity Ransomware",
      summary: "Opportunistic ransomware lineage resurging through aggressive affiliates like 8Base targeting SMBs.",
      desc: "Relies heavily on brute-forced RDP access to manually execute encryption routines across corporate file shares.",
      tech: ["Language: C++", "C2 Protocol: Email negotiation supported by secondary Tor mirrors", "Capabilities: VSS wiping, firewall disablement, rapid local network encryption"],
      propagation: "Direct Internet-exposed RDP brute-forcing and purchased access credentials.",
      defense: ["Eliminate exposed RDP endpoints behind perimeter firewalls and enforce MFA."],
      whyWatch: "A persistent nuisance responsible for a massive share of SMB breaches in 2026."
    },
    sources: [{ name: "CISA Advisory on Phobos Ransomware Affiliates", type: "Security" }]
  },
  {
    id: "TF-026",
    num: "026",
    name: "Formbook / XLoader",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED_PRIOR",
    lang: "C / Assembly",
    arch: "Multi-Platform Stealer (Windows & macOS)",
    c2: "Decoy Domains, HTTP POST with Layered Encryption",
    mitre: ["T1056.001", "T1055", "T1555", "T1071.001"],
    image: "images/TF-026_formbook_real_01.png",
    imageCaption: "Formbook / XLoader Multi-Level Injection Chain",
    gallery: [
      {
        id: "EVID-026-01",
        type: "Injection Scheme",
        url: "images/TF-026_formbook_real_01.png",
        title: "Formbook / XLoader Multi-Level Injection Chain",
        caption: "ANY.RUN technical diagram illustrating payload decryption and nested thread injection into system binaries."
      },
      {
        id: "EVID-026-02",
        type: "C2 Decryption",
        url: "images/TF-026_formbook_real_02.png",
        title: "Formbook Traffic Encryption & Decryption Engine",
        caption: "Forensic memory trace detailing base64 and RC4 decoding of command-and-control responses."
      },
      {
        id: "EVID-026-03",
        type: "Architecture Schematic",
        url: "images/TF-026_formbook_arch.svg",
        title: "Formbook / XLoader Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Decoy Domains, HTTP POST with Layered Encryption command infrastructure."
      }
    ],
    en: {
      type: "Stealer & Form Grabber",
      summary: "Formidable infostealer generating hundreds of decoy HTTP requests to baffle network defenders.",
      desc: "Cross-platform variant (XLoader) intercepting browser form inputs, credentials, and clipboard activity on Windows and macOS.",
      tech: ["Language: C / Assembly", "C2 Protocol: Obfuscated HTTP communication buried under hundreds of decoy domains", "Capabilities: Form grabbing, deep keystroke logging, memory injection"],
      propagation: "Commercial phishing campaigns bearing weaponized archive attachments.",
      defense: ["Detect domain generation anomaly bursts and inspect deep browser hook injections."],
      whyWatch: "Masterclass in network traffic obfuscation persisting strongly in 2026."
    },
    sources: [{ name: "Check Point Research on Formbook and XLoader", type: "Security" }]
  },
  {
    id: "TF-027",
    num: "027",
    name: "Bumblebee",
    category: "Loader",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Proprietary Threat Syndicate Loader",
    c2: "WebSockets, Encrypted Custom Protocols",
    mitre: ["T1055", "T1059", "T1105", "T1027"],
    image: "images/TF-027_bumblebee_real_01.svg",
    imageCaption: "Bumblebee Modular Loader Staging Routine",
    gallery: [
      {
        id: "EVID-027-01",
        type: "Stager Routine",
        url: "images/TF-027_bumblebee_real_01.svg",
        title: "Bumblebee Modular Loader Staging Routine",
        caption: "Forensic sandbox process showing WMI reconnaissance, process hollowing, and secondary payload staging."
      },
      {
        id: "EVID-027-02",
        type: "Disassembly Analysis",
        url: "images/TF-027_bumblebee_real_02.svg",
        title: "Bumblebee WebSocket C2 Handshake Routine",
        caption: "Disassembly tracking WebSocket connection initialization and JSON-formatted command exchange."
      },
      {
        id: "EVID-027-03",
        type: "Architecture Schematic",
        url: "images/TF-027_bumblebee_arch.svg",
        title: "Bumblebee Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and WebSockets, Encrypted Custom Protocols command infrastructure."
      }
    ],
    en: {
      type: "Malware Loader",
      summary: "Bespoke enterprise loader engineered to replace BazarLoader as the primary gateway for ransomware cartels.",
      desc: "Leverages WebSockets for resilient command-and-control and deploys advanced anti-analysis checks before executing secondary implants.",
      tech: ["Language: C++", "C2 Protocol: Encrypted WebSocket sessions", "Capabilities: Active Directory reconnaissance, in-memory Cobalt Strike delivery, sandbox evasion"],
      propagation: "Malicious ISO/VHD container attachments and weaponized LNK shortcuts.",
      defense: ["Block disk image mounting on endpoints and monitor unauthorized WebSocket traffic."],
      whyWatch: "A high-fidelity indicator of imminent catastrophic enterprise ransomware attacks."
    },
    sources: [{ name: "Symantec Threat Hunter Team Bumblebee Report", type: "Security" }]
  },
  {
    id: "TF-028",
    num: "028",
    name: "IcedID (BokBot)",
    category: "Loader",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED_PRIOR",
    lang: "C++",
    arch: "Modular Banking Trojan turned Loader",
    c2: "Steganography in PNG Images, Custom TLS",
    mitre: ["T1001.002", "T1055", "T1056", "T1071"],
    image: "images/TF-028_icedid_real_01.svg",
    imageCaption: "IcedID (BokBot) Steganographic PNG Loader",
    gallery: [
      {
        id: "EVID-028-01",
        type: "Steganography",
        url: "images/TF-028_icedid_real_01.svg",
        title: "IcedID (BokBot) Steganographic PNG Loader",
        caption: "Forensic image analysis showing extraction of hidden encrypted payload from downloaded PNG image files."
      },
      {
        id: "EVID-028-02",
        type: "Banking Module",
        url: "images/TF-028_icedid_real_02.svg",
        title: "IcedID Process Injection into svchost.exe",
        caption: "Process monitor trace tracking hollowed svchost.exe instances used for banking credential theft."
      },
      {
        id: "EVID-028-03",
        type: "Architecture Schematic",
        url: "images/TF-028_icedid_arch.svg",
        title: "IcedID (BokBot) Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Steganography in PNG Images, Custom TLS command infrastructure."
      }
    ],
    en: {
      type: "Banking Trojan & Payload Loader",
      summary: "Veteran banking trojan renowned for concealing executable payloads within legitimate PNG images.",
      desc: "Utilizes advanced steganography to sneak encrypted modules past network inspection points into memory.",
      tech: ["Language: C++", "C2 Protocol: Custom TLS with steganographic PNG image delivery", "Capabilities: Steganography payload reconstruction, browser injection, corporate reconnaissance"],
      propagation: "Phishing documents and password-protected zip archives.",
      defense: ["Enforce deep content inspection on downloaded media assets from untrusted hosts."],
      whyWatch: "Mastery of steganography keeps IcedID relevant in 2026 evasive campaigns."
    },
    sources: [{ name: "Binary Defense IcedID Technical Analysis", type: "Security" }]
  },
  {
    id: "TF-029",
    num: "029",
    name: "DanaBot",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "MONITORED",
    lang: "Delphi",
    arch: "Modular Banking Trojan",
    c2: "Tor Network & Encrypted Binary Sockets",
    mitre: ["T1555", "T1056.002", "T1090.003"],
    image: "images/TF-029_danabot_real_01.svg",
    imageCaption: "DanaBot Banking Trojan Control Interface",
    gallery: [
      {
        id: "EVID-029-01",
        type: "Operator Panel",
        url: "images/TF-029_danabot_real_01.svg",
        title: "DanaBot Banking Trojan Control Interface",
        caption: "Operator web panel tracking active banking bot infections, compromised corporate networks, and injection rules."
      },
      {
        id: "EVID-029-02",
        type: "Disassembly Analysis",
        url: "images/TF-029_danabot_real_02.svg",
        title: "DanaBot Modular Architecture & Plugin Loader",
        caption: "Disassembly showing dynamic download and decryption of specialized sniffing and video capture modules."
      },
      {
        id: "EVID-029-03",
        type: "Architecture Schematic",
        url: "images/TF-029_danabot_arch.svg",
        title: "DanaBot Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Tor Network & Encrypted Binary Sockets command infrastructure."
      }
    ],
    en: {
      type: "Modular Banking Trojan & Stealer",
      summary: "Resilient Delphi-based modular banking Trojan capable of dynamic web injections and wallet theft.",
      desc: "Features an adaptable modular architecture tailored for geographic and institutional financial targeting.",
      tech: ["Language: Embarcadero Delphi", "C2 Protocol: Tor onion network and proprietary binary TCP streams", "Capabilities: Web injections, browser credential scraping, reverse proxy routing"],
      propagation: "Spoofed telecom invoices and regional business malspam.",
      defense: ["Audit local root certificate authorities and isolate corporate banking activities."],
      whyWatch: "Demonstrates sustained operational resilience throughout underground markets."
    },
    sources: [{ name: "Proofpoint DanaBot Evolution Insights", type: "Security" }]
  },
  {
    id: "TF-030",
    num: "030",
    name: "SmokeLoader",
    category: "Loader",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED_PRIOR",
    lang: "C / Assembly",
    arch: "Modular Legacy Dropper",
    c2: "Decoy HTTP Queries, Encrypted Payloads",
    mitre: ["T1055", "T1027", "T1105"],
    image: "images/TF-030_smokeloader_real_01.svg",
    imageCaption: "SmokeLoader Modular Plugin System",
    gallery: [
      {
        id: "EVID-030-01",
        type: "Plugin Engine",
        url: "images/TF-030_smokeloader_real_01.svg",
        title: "SmokeLoader Modular Plugin System",
        caption: "Technical visualization of SmokeLoader core memory resident loop loading encrypted payload extensions."
      },
      {
        id: "EVID-030-02",
        type: "Anti-Analysis",
        url: "images/TF-030_smokeloader_real_02.svg",
        title: "SmokeLoader API Hashing & VM Detection",
        caption: "Disassembly showing API name hashing algorithms used to bypass security solution import table monitoring."
      },
      {
        id: "EVID-030-03",
        type: "Architecture Schematic",
        url: "images/TF-030_smokeloader_arch.svg",
        title: "SmokeLoader Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Decoy HTTP Queries, Encrypted Payloads command infrastructure."
      }
    ],
    en: {
      type: "Modular Loader",
      summary: "Legendary modular dropper persisting over a decade as an indispensable initial delivery vehicle.",
      desc: "Compact C/Assembly loader weaponized with anti-reverse engineering techniques to execute secondary malware payloads.",
      tech: ["Language: Pure C / Assembly", "C2 Protocol: Obfuscated HTTP streams mixed with legitimate-looking decoy traffic", "Capabilities: Anti-analysis, process injection into explorer.exe, modular plugin execution"],
      propagation: "Cracked applications, keygens, and pirated software bundles.",
      defense: ["Monitor explorer.exe memory space modifications and anomalous outbound HTTP post requests."],
      whyWatch: "The undisputed grandfather of initial payload droppers in cybercrime."
    },
    sources: [{ name: "CERT-UA SmokeLoader Campaign Bulletin", type: "Security" }]
  },
  {
    id: "TF-031",
    num: "031",
    name: "Cobalt Strike",
    category: "C2 Framework",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED",
    lang: "C / Java",
    arch: "Industry Standard Adversary Simulation",
    c2: "Malleable C2, DNS/HTTPS/SMB Beacons",
    mitre: ["T1059", "T1055", "T1090", "T1573.001"],
    image: "images/TF-031_cobaltstrike_real_01.png",
    imageCaption: "Cobalt Strike Listener Management & Beacon Console",
    gallery: [
      {
        id: "EVID-031-01",
        type: "Listeners UI",
        url: "images/TF-031_cobaltstrike_real_01.png",
        title: "Cobalt Strike Listener Management & Beacon Console",
        caption: "Operator interface configuring HTTP, HTTPS, and DNS malleable C2 listeners and tracking active Beacons."
      },
      {
        id: "EVID-031-02",
        type: "Beacon Architecture",
        url: "images/TF-031_cobaltstrike_real_02.svg",
        title: "Cobalt Strike In-Memory Beacon Reflection Engine",
        caption: "Technical schematic showing Reflective DLL loading, sleep masking, and thread stack spoofing mechanisms."
      },
      {
        id: "EVID-031-03",
        type: "Architecture Schematic",
        url: "images/TF-031_cobaltstrike_arch.svg",
        title: "Cobalt Strike Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Malleable C2, DNS/HTTPS/SMB Beacons command infrastructure."
      }
    ],
    en: {
      type: "Adversary Simulation / C2",
      summary: "The definitive enterprise adversary simulation tool extensively weaponized by elite cybercrime syndicates and APTs.",
      desc: "Renowned for its Malleable C2 profiles that camouflage command-and-control beaconing inside legitimate web and cloud traffic.",
      tech: ["Language: Java (TeamServer), C (Beacon)", "C2 Protocol: Malleable HTTP/HTTPS, DNS tunneling, SMB named pipes", "Capabilities: In-memory post-exploitation, Mimikatz integration, lateral pivoting"],
      propagation: "Staged post-compromise following initial exploitation or dropper activity.",
      defense: ["Inspect memory for default Beacon signatures and audit named pipe creations across enterprise hosts."],
      whyWatch: "Remains the gold standard against which all defensive telemetry is measured in 2026."
    },
    sources: [{ name: "Fortra Cobalt Strike Official Research & Detection Guide", type: "Security" }]
  },
  {
    id: "TF-032",
    num: "032",
    name: "Brute Ratel C4",
    category: "C2 Framework",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED",
    lang: "C / Assembly",
    arch: "EDR-Evasion Centric C2",
    c2: "Badger Agent, DoH, Custom Syscalls",
    mitre: ["T1055", "T1027", "T1562.001"],
    image: "images/TF-032_bruteratel_real_01.png",
    imageCaption: "Brute Ratel C4 Badger Execution Graph",
    gallery: [
      {
        id: "EVID-032-01",
        type: "Payload Execution",
        url: "images/TF-032_bruteratel_real_01.png",
        title: "Brute Ratel C4 Badger Execution Graph",
        caption: "ANY.RUN sandbox process trace tracking Badger payload injection and memory manipulation routines."
      },
      {
        id: "EVID-032-02",
        type: "Syscall Engine",
        url: "images/TF-032_bruteratel_real_02.png",
        title: "Brute Ratel Indirect Syscall Execution Routine",
        caption: "Disassembly showing dynamic SSN resolution and indirect syscall execution bypassing user-mode EDR hooks."
      },
      {
        id: "EVID-032-03",
        type: "Architecture Schematic",
        url: "images/TF-032_bruteratel_arch.svg",
        title: "Brute Ratel C4 Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Badger Agent, DoH, Custom Syscalls command infrastructure."
      }
    ],
    en: {
      type: "Next-Gen C2 Framework",
      summary: "Adversary simulation platform engineered specifically to evade state-of-the-art EDR and XDR sensors.",
      desc: "Its agent ('Badger') utilizes direct syscalls, stack spoofing, and DNS-over-HTTPS channels to operate undetected in hostile environments.",
      tech: ["Language: Pure C and Assembly", "C2 Protocol: DNS over HTTPS (DoH), encrypted custom HTTP channels", "Capabilities: Direct syscalls, call stack spoofing, thread manipulation, memory obfuscation"],
      propagation: "High-value enterprise intrusions and targeted spear-phishing.",
      defense: ["Deploy behavioral instrumentation capable of flagging direct NTAPI transitions without kernel hooks."],
      whyWatch: "Represents the cutting edge of defensive evasion mechanics in 2026."
    },
    sources: [{ name: "Palo Alto Networks Unit 42 Brute Ratel Analysis", type: "Security" }]
  },
  {
    id: "TF-033",
    num: "033",
    name: "NetSupport RAT",
    category: "RAT",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Abused Legitimate Remote Admin Tool",
    c2: "HTTP Gateway, Client-Server Sockets",
    mitre: ["T1219", "T1059", "T1082"],
    image: "images/TF-033_netsupport_real_01.svg",
    imageCaption: "NetSupport RAT Gateway Configuration & Deployment",
    gallery: [
      {
        id: "EVID-033-01",
        type: "Gateway Config",
        url: "images/TF-033_netsupport_real_01.svg",
        title: "NetSupport RAT Gateway Configuration & Deployment",
        caption: "Forensic analysis of client32.ini configuration parameters establishing covert gateway reverse connections."
      },
      {
        id: "EVID-033-02",
        type: "Disassembly Analysis",
        url: "images/TF-033_netsupport_real_02.svg",
        title: "NetSupport RAT Screen Capture & Keystroke Monitor",
        caption: "Disassembly tracking surveillance API hooks capturing remote desktop buffers and operator commands."
      },
      {
        id: "EVID-033-03",
        type: "Architecture Schematic",
        url: "images/TF-033_netsupport_arch.svg",
        title: "NetSupport RAT Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTP Gateway, Client-Server Sockets command infrastructure."
      }
    ],
    en: {
      type: "Abused Remote Support Tool",
      summary: "Commercial remote support utility weaponized into a stealthy RAT, evading AV through signed trust.",
      desc: "Attackers deploy customized NetSupport Manager client packages to maintain interactive control under the guise of IT administration.",
      tech: ["Language: C++", "C2 Protocol: NetSupport Gateway HTTP relays", "Capabilities: Screen viewing, file manipulation, script dispatch, keystroke capture"],
      propagation: "Fake browser update popups and compromised website redirects.",
      defense: ["Enforce application allowlisting policies blocking unauthorized client32.exe executions."],
      whyWatch: "A premier example of living-off-the-land software abuse in modern intrusions."
    },
    sources: [{ name: "Rapid7 NetSupport RAT Threat Telemetry", type: "Security" }]
  },
  {
    id: "TF-034",
    num: "034",
    name: "NjRAT / Bladabindi",
    category: "RAT",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED",
    lang: ".NET (VB.NET)",
    arch: "Commodity RAT",
    c2: "Direct TCP Sockets with Delimited Strings",
    mitre: ["T1056.001", "T1059.003", "T1082"],
    image: "images/TF-034_njrat_real_01.png",
    imageCaption: "NjRAT (Bladabindi) Golden Edition Builder Interface",
    gallery: [
      {
        id: "EVID-034-01",
        type: "Builder UI",
        url: "images/TF-034_njrat_real_01.png",
        title: "NjRAT (Bladabindi) Golden Edition Builder Interface",
        caption: "Visual Basic .NET builder configuring payload persistence, dynamic DNS connection strings, and mutex flags."
      },
      {
        id: "EVID-034-02",
        type: "Operator Console",
        url: "images/TF-034_njrat_real_02.svg",
        title: "NjRAT Victim Management & Webcam Surveillance Console",
        caption: "Operator UI managing connected victim bots, remote desktop viewing, and live microphone capture streams."
      },
      {
        id: "EVID-034-03",
        type: "Architecture Schematic",
        url: "images/TF-034_njrat_arch.svg",
        title: "NjRAT / Bladabindi Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Direct TCP Sockets with Delimited Strings command infrastructure."
      }
    ],
    en: {
      type: "Remote Access Trojan (RAT)",
      summary: "Legendary commodity RAT widely circulated in underground forums, particularly in MENA and Latin America.",
      desc: "Engineered in VB.NET, renowned for its simple pipe-delimited TCP commands and comprehensive surveillance tools.",
      tech: ["Language: VB.NET", "C2 Protocol: Plaintext or lightly obfuscated TCP sockets using '|' separators", "Capabilities: Webcam spying, keylogging, file exploration, registry tampering"],
      propagation: "Telegram sharing channels, cracked tool archives, and malicious torrents.",
      defense: ["Detect traditional '|' delimiter signatures in raw TCP streams and monitor rogue .NET processes."],
      whyWatch: "An iconic, persistent staple of commodity cybercrime spanning more than a decade."
    },
    sources: [{ name: "Microsoft Security Bladabindi Threat Profile", type: "Security" }]
  },
  {
    id: "TF-035",
    num: "035",
    name: "DCRat (DarkCrystal)",
    category: "RAT",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "TESTED",
    lang: "C# (.NET)",
    arch: "Budget Commercial RAT",
    c2: "HTTP / Web Panel via PHP Backend",
    mitre: ["T1056.001", "T1059", "T1082"],
    image: "images/TF-035_dcrat_real_01.png",
    imageCaption: "DCRat (DarkCrystal) Studio & Plugin Builder",
    gallery: [
      {
        id: "EVID-035-01",
        type: "Builder UI",
        url: "images/TF-035_dcrat_real_01.png",
        title: "DCRat (DarkCrystal) Studio & Plugin Builder",
        caption: "Modern builder interface displaying modular plugin selections, stealer configurations, and obfuscation options."
      },
      {
        id: "EVID-035-02",
        type: "Operator Console",
        url: "images/TF-035_dcrat_real_02.svg",
        title: "DCRat Botnet Administration Dashboard",
        caption: "Web-based administration console tracking active victim nodes, geolocations, and extracted credentials."
      },
      {
        id: "EVID-035-03",
        type: "Architecture Schematic",
        url: "images/TF-035_dcrat_arch.svg",
        title: "DCRat (DarkCrystal) Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTP / Web Panel via PHP Backend command infrastructure."
      }
    ],
    en: {
      type: "Remote Access Trojan",
      summary: "Ultra-low-cost commercial RAT popular in Russian forums, featuring an extensive plugin framework.",
      desc: "Leverages a modular architecture allowing operators to tailor modules for stealing, surveillance, or trolling.",
      tech: ["Language: C# (.NET) client, PHP server", "C2 Protocol: HTTP requests routed through low-cost shared web hosting", "Capabilities: Dynamic plugin architecture, browser dumping, keylogging"],
      propagation: "Underground hacking forums and malicious software keygens.",
      defense: ["Monitor atypical HTTP beaconing directed at compromised shared hosting services."],
      whyWatch: "High volume commodity footprint due to extreme market affordability."
    },
    sources: [{ name: "Mandiant DCRat Analysis & Tracker", type: "Security" }]
  },
  {
    id: "TF-036",
    num: "036",
    name: "PureCrypter / PureLogs",
    category: "Crypter",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: ".NET (C#)",
    arch: "Commercial Malware Obfuscator",
    c2: "Telegram Bot API, Cloudflare Protected Endpoints",
    mitre: ["T1027.002", "T1055.001", "T1140"],
    image: "images/TF-036_purecrypter_real_01.svg",
    imageCaption: "PureCrypter Multi-Layer Obfuscation Architecture",
    gallery: [
      {
        id: "EVID-036-01",
        type: "Obfuscation Engine",
        url: "images/TF-036_purecrypter_real_01.svg",
        title: "PureCrypter Multi-Layer Obfuscation Architecture",
        caption: "Forensic diagram detailing .NET runtime compression, dynamic decryption stubs, and AMSI memory patching."
      },
      {
        id: "EVID-036-02",
        type: "Disassembly Analysis",
        url: "images/TF-036_purecrypter_real_02.svg",
        title: "PureCrypter In-Memory Payload Decryption",
        caption: "Disassembly tracking AES payload extraction from encrypted resources and injection into target processes."
      },
      {
        id: "EVID-036-03",
        type: "Architecture Schematic",
        url: "images/TF-036_purecrypter_arch.svg",
        title: "PureCrypter / PureLogs Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Telegram Bot API, Cloudflare Protected Endpoints command infrastructure."
      }
    ],
    en: {
      type: "Commercial Crypter & Stealer Suite",
      summary: "Premier commercial crypting service used by diverse threat actors to wrap and stealth payloads.",
      desc: "Provides automated AMSI bypasses, ETW patching, and memory hollowing into trusted Windows utilities.",
      tech: ["Language: Advanced C# (.NET)", "C2 Protocol: Telegram Bot API integrations and cloud endpoints", "Capabilities: AMSI/ETW bypass, multi-layer compression, process hollowing"],
      propagation: "Commercial underground service protecting diverse malware families.",
      defense: ["Deploy memory scanning tools capable of inspecting newly unmapped memory buffers."],
      whyWatch: "The premier armor shielding modern commodity malware from detection."
    },
    sources: [{ name: "Recorded Future PureCrypter Technical Teardown", type: "Security" }]
  },
  {
    id: "TF-037",
    num: "037",
    name: "PrivateLoader",
    category: "Loader",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Pay-Per-Install (PPI) Distribution Loader",
    c2: "HTTP POST over Custom Encrypted Ports",
    mitre: ["T1055", "T1105", "T1082"],
    image: "images/TF-037_privateloader_real_01.jpg",
    imageCaption: "PrivateLoader Pay-Per-Install Distribution Topology",
    gallery: [
      {
        id: "EVID-037-01",
        type: "Distribution Network",
        url: "images/TF-037_privateloader_real_01.jpg",
        title: "PrivateLoader Pay-Per-Install Distribution Topology",
        caption: "ANY.RUN technical diagram detailing corporate endpoint compromise via Pay-Per-Install malware distribution channels."
      },
      {
        id: "EVID-037-02",
        type: "Payload Decryption",
        url: "images/TF-037_privateloader_real_02.png",
        title: "PrivateLoader Payload Decryption & Execution Trace",
        caption: "Process memory capture showing secondary payload downloading, decryption, and execution validation."
      },
      {
        id: "EVID-037-03",
        type: "Architecture Schematic",
        url: "images/TF-037_privateloader_arch.svg",
        title: "PrivateLoader Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTP POST over Custom Encrypted Ports command infrastructure."
      }
    ],
    en: {
      type: "Pay-Per-Install (PPI) Loader",
      summary: "The linchpin of cybercrime Pay-Per-Install operations, dropping multiple competing malware families simultaneously.",
      desc: "Profiles infected endpoints and delivers multiple payloads (stealers, clippers, miners) on behalf of diverse paying clients.",
      tech: ["Language: C++", "C2 Protocol: XOR-encrypted HTTP POST telemetry", "Capabilities: Concurrent multi-payload downloads, endpoint profiling"],
      propagation: "SEO-poisoned software cracking blogs and malvertising.",
      defense: ["Inspect sudden multi-family executable drops within local user AppData folders."],
      whyWatch: "The economic engine underpinning mass commodity malware delivery in 2026."
    },
    sources: [{ name: "Intel 471 PrivateLoader Network Research", type: "Security" }]
  },
  {
    id: "TF-038",
    num: "038",
    name: "SystemBC",
    category: "Botnet",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED_PRIOR",
    lang: "C",
    arch: "Tor Proxy & Backdoor Utility",
    c2: "SOCKS5 over Tor, Raw TCP Tunnels",
    mitre: ["T1090.003", "T1573", "T1059"],
    image: "images/TF-038_systembc_real_01.svg",
    imageCaption: "SystemBC SOCKS5 Tor Proxy Tunnel Architecture",
    gallery: [
      {
        id: "EVID-038-01",
        type: "Proxy Engine",
        url: "images/TF-038_systembc_real_01.svg",
        title: "SystemBC SOCKS5 Tor Proxy Tunnel Architecture",
        caption: "Technical visualization of SystemBC acting as a covert encrypted proxy for ransomware gang lateral movement."
      },
      {
        id: "EVID-038-02",
        type: "Network Telemetry",
        url: "images/TF-038_systembc_real_02.svg",
        title: "SystemBC Beacon Traffic & Command Protocol",
        caption: "Packet capture analysis showing RC4-encrypted beaconing communicating with adversary command servers."
      },
      {
        id: "EVID-038-03",
        type: "Architecture Schematic",
        url: "images/TF-038_systembc_arch.svg",
        title: "SystemBC Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and SOCKS5 over Tor, Raw TCP Tunnels command infrastructure."
      }
    ],
    en: {
      type: "Tor Proxy & Pivot Backdoor",
      summary: "Tor proxy utility deployed by elite ransomware operators to conceal internal communications.",
      desc: "Creates encrypted reverse SOCKS5 proxies routing malicious command-and-control traffic through the Tor onion network.",
      tech: ["Language: Pure C", "C2 Protocol: SOCKS5 over Tor and raw encrypted TCP tunnels", "Capabilities: Covert pivoting, remote command execution, anonymity routing"],
      propagation: "Dropped by loaders like SmokeLoader prior to ransomware deployment.",
      defense: ["Detect and restrict unauthorized outbound Tor nodes and non-standard SOCKS5 tunneling."],
      whyWatch: "Essential plumbing in modern high-stakes enterprise ransomware operations."
    },
    sources: [{ name: "Sophos X-Ops SystemBC In-Depth Telemetry", type: "Security" }]
  },
  {
    id: "TF-039",
    num: "039",
    name: "Mirai & Variants",
    category: "Botnet",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "TESTED_PRIOR",
    lang: "C",
    arch: "IoT Distributed Denial of Service (DDoS) Botnet",
    c2: "IRC, Telnet Brute Force, Custom Binary C2",
    mitre: ["T1498", "T1110.001", "T1046"],
    image: "images/TF-039_mirai_real_01.svg",
    imageCaption: "Mirai IoT Telnet Brute-Force Scanner Routine",
    gallery: [
      {
        id: "EVID-039-01",
        type: "Telnet Scanner",
        url: "images/TF-039_mirai_real_01.svg",
        title: "Mirai IoT Telnet Brute-Force Scanner Routine",
        caption: "ANY.RUN analysis capture showing Mirai bot scanning IPv4 address space using hardcoded default credential dictionaries."
      },
      {
        id: "EVID-039-02",
        type: "DDoS Engine",
        url: "images/TF-039_mirai_real_02.svg",
        title: "Mirai SYN and UDP Flood Attack Engine",
        caption: "Disassembly showing raw socket creation and automated transmission of high-volume DDoS packets."
      },
      {
        id: "EVID-039-03",
        type: "Architecture Schematic",
        url: "images/TF-039_mirai_arch.svg",
        title: "Mirai & Variants Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and IRC, Telnet Brute Force, Custom Binary C2 command infrastructure."
      }
    ],
    en: {
      type: "IoT Botnet (DDoS)",
      summary: "The definitive IoT botnet family exploiting default credentials and router vulnerabilities to wage mega DDoS.",
      desc: "Scans IPv4 space relentlessly to infect routers, DVRs, and smart devices for volumetric SYN, UDP, and HTTP floods.",
      tech: ["Language: C", "C2 Protocol: Custom binary socket protocols", "Capabilities: Telnet brute forcing, distributed architecture, volumetric DDoS generation"],
      propagation: "Telnet scanning for factory credentials and known router CVE exploits.",
      defense: ["Mandate non-default credentials and disable public Telnet/SSH management interfaces."],
      whyWatch: "The foundational threat architecture responsible for world-record volumetric DDoS attacks."
    },
    sources: [{ name: "CISA Mirai IoT Botnet Advisory", type: "Security" }]
  },
  {
    id: "TF-040",
    num: "040",
    name: "Mozi Botnet",
    category: "Botnet",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "MONITORED",
    lang: "C",
    arch: "P2P IoT Worm & Botnet",
    c2: "DHT (Distributed Hash Table) Network Protocol",
    mitre: ["T1498", "T1190", "T1046"],
    image: "images/TF-040_mozi_real_01.svg",
    imageCaption: "Mozi Botnet DHT P2P Coordination Protocol",
    gallery: [
      {
        id: "EVID-040-01",
        type: "P2P Network",
        url: "images/TF-040_mozi_real_01.svg",
        title: "Mozi Botnet DHT P2P Coordination Protocol",
        caption: "Technical schematic illustrating BitTorrent DHT protocol abuse for distributed C2 command broadcasting."
      },
      {
        id: "EVID-040-02",
        type: "Exploit Module",
        url: "images/TF-040_mozi_real_02.svg",
        title: "Mozi IoT Zero-Day Exploit Propagation Module",
        caption: "Disassembly tracking automated execution of UPnP and router vulnerability exploits against target subnets."
      },
      {
        id: "EVID-040-03",
        type: "Architecture Schematic",
        url: "images/TF-040_mozi_arch.svg",
        title: "Mozi Botnet Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and DHT (Distributed Hash Table) Network Protocol command infrastructure."
      }
    ],
    en: {
      type: "P2P IoT Worm & Botnet",
      summary: "Fully decentralized P2P IoT worm communicating via the Distributed Hash Table (DHT) protocol.",
      desc: "Eliminates centralized C2 vulnerability by routing cryptographically signed commands across a resilient peer-to-peer fabric.",
      tech: ["Language: C", "C2 Protocol: P2P DHT protocol (similar to BitTorrent)", "Capabilities: Automated worm replication, volumetric DDoS, payload dispatch"],
      propagation: "Exploiting unpatched remote code execution vulnerabilities in network gateways.",
      defense: ["Keep perimeter network gateway firmware updated and block unsolicited UDP DHT chatter."],
      whyWatch: "A resilient study in resilient, serverless malware architecture."
    },
    sources: [{ name: "Microsoft Mozi IoT Analysis", type: "Security" }]
  },
  {
    id: "TF-041",
    num: "041",
    name: "Meduza Stealer",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Browser & Wallet Harvester",
    c2: "HTTPS with Geoblocking Restrictions",
    mitre: ["T1555", "T1082", "T1071"],
    image: "images/TF-041_meduza_real_01.svg",
    imageCaption: "Meduza Stealer Web Administration Dashboard",
    gallery: [
      {
        id: "EVID-041-01",
        type: "Collector Dashboard",
        url: "images/TF-041_meduza_real_01.svg",
        title: "Meduza Stealer Web Administration Dashboard",
        caption: "Operator web console aggregating infected victim logs, browser credential databases, and cold storage crypto keys."
      },
      {
        id: "EVID-041-02",
        type: "Network Telemetry",
        url: "images/TF-041_meduza_real_02.svg",
        title: "Meduza Stealer C2 Exfiltration Handshake",
        caption: "Network telemetry trace showing encrypted ZIP archive exfiltration containing harvested endpoint data."
      },
      {
        id: "EVID-041-03",
        type: "Architecture Schematic",
        url: "images/TF-041_meduza_arch.svg",
        title: "Meduza Stealer Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTPS with Geoblocking Restrictions command infrastructure."
      }
    ],
    en: {
      type: "InfoStealer",
      summary: "Boutique infostealer geared specifically toward cryptocurrency ecosystems with aggressive geo-exclusion.",
      desc: "Combines an intuitive web management portal with rapid exfiltration targeting 100+ browsers and crypto vaults.",
      tech: ["Language: C++", "C2 Protocol: Encrypted HTTPS with strict geographic whitelist gates", "Capabilities: Steals from 100+ browsers, 40+ crypto vaults, 2FA app tokens"],
      propagation: "Gaming forums and weaponized cracked media links.",
      defense: ["Mandate hardware cold wallets for valuable digital asset storage."],
      whyWatch: "An active competitor challenging established infostealer monopolies."
    },
    sources: [{ name: "Uptycs Meduza Stealer Research", type: "Security" }]
  },
  {
    id: "TF-042",
    num: "042",
    name: "RisePro",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Commodity Credential Stealer",
    c2: "Encrypted TCP / Custom HTTP Webhook",
    mitre: ["T1555", "T1005", "T1082"],
    image: "images/TF-042_risepro_real_01.webp",
    imageCaption: "RisePro Stealer Network Communication & Encryption",
    gallery: [
      {
        id: "EVID-042-01",
        type: "Network Protocol",
        url: "images/TF-042_risepro_real_01.webp",
        title: "RisePro Stealer Network Communication & Encryption",
        caption: "ANY.RUN forensic capture analyzing custom TCP protocol used by RisePro to transmit exfiltrated system data."
      },
      {
        id: "EVID-042-02",
        type: "Exfiltration Packet",
        url: "images/TF-042_risepro_real_02.webp",
        title: "RisePro Credential Archive Assembly & Dispatch",
        caption: "Memory analysis showing compilation of password logs, system information, and browser artifacts into C2 packets."
      },
      {
        id: "EVID-042-03",
        type: "Architecture Schematic",
        url: "images/TF-042_risepro_arch.svg",
        title: "RisePro Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Encrypted TCP / Custom HTTP Webhook command infrastructure."
      }
    ],
    en: {
      type: "InfoStealer",
      summary: "High-volume credential stealer distributed primarily via Pay-Per-Install networks like PrivateLoader.",
      desc: "Heavily resembles Vidar lineage, targeting stored passwords, session tokens, and virtual private network credentials.",
      tech: ["Language: C++", "C2 Protocol: Obfuscated TCP communications", "Capabilities: VPN client credential dumping, crypto theft, browser vault harvesting"],
      propagation: "PrivateLoader distribution syndicates and malicious warez sites.",
      defense: ["Restrict standard user software installations and audit local AppData folders."],
      whyWatch: "A high-velocity threat benefiting from massive PPI distribution pipelines."
    },
    sources: [{ name: "Flashpoint RisePro Intelligence Brief", type: "Security" }]
  },
  {
    id: "TF-043",
    num: "043",
    name: "BunnyLoader",
    category: "Loader",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "MONITORED",
    lang: "C / C++",
    arch: "Loader-as-a-Service (LaaS)",
    c2: "Web Admin Panel with AES-256",
    mitre: ["T1055", "T1105", "T1056.001"],
    image: "images/TF-043_bunnyloader_real_01.svg",
    imageCaption: "BunnyLoader 3.0 Modular Control Interface",
    gallery: [
      {
        id: "EVID-043-01",
        type: "Modular Core",
        url: "images/TF-043_bunnyloader_real_01.svg",
        title: "BunnyLoader 3.0 Modular Control Interface",
        caption: "C2 web panel displaying active loader instances, modular plugin downloads, and cryptocurrency clipper status."
      },
      {
        id: "EVID-043-02",
        type: "Network Telemetry",
        url: "images/TF-043_bunnyloader_real_02.svg",
        title: "BunnyLoader Tasking & Secondary Drop Telemetry",
        caption: "Network capture analyzing endpoint registration and automated retrieval of secondary stealer payloads."
      },
      {
        id: "EVID-043-03",
        type: "Architecture Schematic",
        url: "images/TF-043_bunnyloader_arch.svg",
        title: "BunnyLoader Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Web Admin Panel with AES-256 command infrastructure."
      }
    ],
    en: {
      type: "Loader & Clipper Suite",
      summary: "Rapidly iterated Loader-as-a-Service featuring secondary dropping and integrated cryptocurrency clipping.",
      desc: "Offers underground buyers an intuitive control panel for staging payloads and manipulating victim clipboards.",
      tech: ["Language: C/C++", "C2 Protocol: AES-256 encrypted web panel communications", "Capabilities: Payload dropping, memory injection, crypto clipping, keylogging"],
      propagation: "Underground cybercrime markets and spear-phishing campaigns.",
      defense: ["Deploy clipboard tampering monitoring and restrict script execution from temp storage."],
      whyWatch: "Undergoes rapid development cycles introducing stealth evasion modules."
    },
    sources: [{ name: "Palo Alto Networks BunnyLoader Evolution Study", type: "Security" }]
  },
  {
    id: "TF-044",
    num: "044",
    name: "Latrodectus",
    category: "Loader",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Next-Gen Downloader (IcedID Successor)",
    c2: "HTTPS with Encrypted Custom Headers",
    mitre: ["T1055", "T1027", "T1105", "T1082"],
    image: "images/TF-044_latrodectus_real_01.png",
    imageCaption: "Latrodectus High-Stealth Loader Execution Pipeline",
    gallery: [
      {
        id: "EVID-044-01",
        type: "Execution Pipeline",
        url: "images/TF-044_latrodectus_real_01.png",
        title: "Latrodectus High-Stealth Loader Execution Pipeline",
        caption: "ANY.RUN sandbox telemetry tracking multi-stage loader execution, WMI reconnaissance, and string hashing routines."
      },
      {
        id: "EVID-044-02",
        type: "C2 Telemetry",
        url: "images/TF-044_latrodectus_real_02.svg",
        title: "Latrodectus FNV-1a Hashing & C2 Beacon Protocol",
        caption: "Network telemetry trace showing encrypted command-and-control handshakes and bot ID registration."
      },
      {
        id: "EVID-044-03",
        type: "Architecture Schematic",
        url: "images/TF-044_latrodectus_arch.svg",
        title: "Latrodectus Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTPS with Encrypted Custom Headers command infrastructure."
      }
    ],
    en: {
      type: "Advanced Loader",
      summary: "The direct architectural successor to IcedID, meticulously engineered for evasive payload staging.",
      desc: "Exercising intense environmental caution, it refuses execution inside sandboxes and stages high-value ransomware backdoors.",
      tech: ["Language: C++", "C2 Protocol: HTTPS utilizing customized encrypted HTTP headers", "Capabilities: Deep sandbox introspection, indirect API execution, modular payload loading"],
      propagation: "Thread-hijacked phishing emails bearing malicious PDF attachments.",
      defense: ["Inspect web proxies for custom HTTP headers and verify unexpected PDF launch behaviors."],
      whyWatch: "A high-priority emerging loader backing major cybercrime syndicates in 2026."
    },
    sources: [{ name: "Proofpoint & Team Cymru Latrodectus Joint Brief", type: "Security" }]
  },
  {
    id: "TF-045",
    num: "045",
    name: "StrelaStealer",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "MONITORED",
    lang: "Python / DLL (C)",
    arch: "Email Client Focused Stealer",
    c2: "Direct HTTP POST to Compromised Web Servers",
    mitre: ["T1555", "T1114", "T1071.001"],
    image: "images/TF-045_strelastealer_real_01.svg",
    imageCaption: "StrelaStealer Outlook & Thunderbird Credential Harvester",
    gallery: [
      {
        id: "EVID-045-01",
        type: "Mail Harvester",
        url: "images/TF-045_strelastealer_real_01.svg",
        title: "StrelaStealer Outlook & Thunderbird Credential Harvester",
        caption: "Technical visualization of StrelaStealer parsing email client configuration files to extract IMAP/POP3 passwords."
      },
      {
        id: "EVID-045-02",
        type: "Network Telemetry",
        url: "images/TF-045_strelastealer_real_02.svg",
        title: "StrelaStealer C2 Exfiltration Traffic",
        caption: "Packet inspection showing multipart HTTP POST transmission of extracted email credentials to adversary nodes."
      },
      {
        id: "EVID-045-03",
        type: "Architecture Schematic",
        url: "images/TF-045_strelastealer_arch.svg",
        title: "StrelaStealer Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Direct HTTP POST to Compromised Web Servers command infrastructure."
      }
    ],
    en: {
      type: "Email Credential Stealer",
      summary: "Surgically focused stealer tailored exclusively for exfiltrating Microsoft Outlook and Thunderbird credentials.",
      desc: "Targets enterprise mail client databases to enable large-scale business email compromise and supply chain pivoting.",
      tech: ["Language: Embedded Python packed into native DLLs", "C2 Protocol: Direct HTTP POST exfiltration to compromised WordPress hosts", "Capabilities: Outlook registry credential decryption, Thunderbird key file scraping"],
      propagation: "Invoices packaged within ISO containers and malicious zip attachments.",
      defense: ["Enforce enterprise MFA on email gateways and restrict unvetted DLL executions."],
      whyWatch: "A targeted threat vector driving sophisticated Business Email Compromise intrusions."
    },
    sources: [{ name: "Unit 42 StrelaStealer Campaign Telemetry", type: "Security" }]
  },
  {
    id: "TF-046",
    num: "046",
    name: "HijackLoader",
    category: "Loader",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Modular In-Memory Loader",
    c2: "Encrypted Web Endpoints, Cloudflare Proxies",
    mitre: ["T1055.001", "T1027", "T1105"],
    image: "images/TF-046_hijackloader_real_01.png",
    imageCaption: "HijackLoader (IDAT Loader) Image Chunk Extraction",
    gallery: [
      {
        id: "EVID-046-01",
        type: "Chunk Extraction",
        url: "images/TF-046_hijackloader_real_01.png",
        title: "HijackLoader (IDAT Loader) Image Chunk Extraction",
        caption: "ANY.RUN technical capture showing extraction and decryption of hidden shellcode from PNG IDAT chunks."
      },
      {
        id: "EVID-046-02",
        type: "Process Hollowing",
        url: "images/TF-046_hijackloader_real_02.svg",
        title: "HijackLoader Process Injection into Clean Windows Binary",
        caption: "Process monitor telemetry tracking hollowed process creation and memory section remapping."
      },
      {
        id: "EVID-046-03",
        type: "Architecture Schematic",
        url: "images/TF-046_hijackloader_arch.svg",
        title: "HijackLoader Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Encrypted Web Endpoints, Cloudflare Proxies command infrastructure."
      }
    ],
    en: {
      type: "Modular In-Memory Loader",
      summary: "Rapidly expanding modular loader employing indirect syscalls and sophisticated process injection.",
      desc: "Serves as an evasive pipeline for infostealers and RATs, injecting payloads into benign system binaries.",
      tech: ["Language: C++", "C2 Protocol: Web endpoints shielded behind Cloudflare reverse proxies", "Capabilities: Indirect syscalls, process hollowing, deep AV product enumeration"],
      propagation: "Search engine malvertising and cracked software portals.",
      defense: ["Monitor unbacked thread executions and inspect suspicious child processes of benign binaries."],
      whyWatch: "Among the fastest-growing initial loaders observed in 2026 telemetries."
    },
    sources: [{ name: "Zscaler ThreatLabz HijackLoader Technical Deep Dive", type: "Security" }]
  },
  {
    id: "TF-047",
    num: "047",
    name: "RustBucket",
    category: "Loader",
    status: "ACTIVE",
    relevance: "MEDIUM",
    teamStatus: "MONITORED",
    lang: "Rust / Objective-C",
    arch: "Targeted macOS Malware Suite",
    c2: "HTTPS with Encrypted Custom Handshake",
    mitre: ["T1059.002", "T1082", "T1071"],
    image: "images/TF-047_rustbucket_real_01.svg",
    imageCaption: "RustBucket macOS PDF Viewer Lure & Execution",
    gallery: [
      {
        id: "EVID-047-01",
        type: "macOS Lure",
        url: "images/TF-047_rustbucket_real_01.svg",
        title: "RustBucket macOS PDF Viewer Lure & Execution",
        caption: "Forensic trace analyzing AppleScript invocation and fake PDF reader application dropping Mach-O binaries."
      },
      {
        id: "EVID-047-02",
        type: "Network Telemetry",
        url: "images/TF-047_rustbucket_real_02.svg",
        title: "RustBucket Multi-Stage C2 Domain Resolution",
        caption: "Network capture tracking second-stage Mach-O payload retrieval from adversary-controlled infrastructure."
      },
      {
        id: "EVID-047-03",
        type: "Architecture Schematic",
        url: "images/TF-047_rustbucket_arch.svg",
        title: "RustBucket Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTPS with Encrypted Custom Handshake command infrastructure."
      }
    ],
    en: {
      type: "macOS Backdoor & Loader",
      summary: "Targeted multi-stage macOS malware engineered in Rust, attributed to North Korean state-sponsored threat groups.",
      desc: "Masquerades as a benign PDF viewer on macOS, only decrypting its malicious core upon opening a specific target PDF.",
      tech: ["Language: Rust and Objective-C", "C2 Protocol: Encrypted HTTPS exchanges", "Capabilities: macOS host surveillance, arbitrary command execution, selective payload activation"],
      propagation: "Targeted social engineering campaigns targeting financial and crypto professionals.",
      defense: ["Enforce Apple Gatekeeper policies and deploy specialized macOS EDR agents."],
      whyWatch: "Highlights the expanding weaponization of Rust against enterprise macOS endpoints."
    },
    sources: [{ name: "Jamf Threat Labs RustBucket macOS Analysis", type: "Security" }]
  },
  {
    id: "TF-048",
    num: "048",
    name: "Atomic Stealer (AMOS)",
    category: "InfoStealer",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "Go / AppleScript",
    arch: "Specialized macOS Infostealer",
    c2: "Telegram Bot API, Encrypted Web Servers",
    mitre: ["T1555", "T1059.002", "T1082"],
    image: "images/TF-048_atomic_real_01.png",
    imageCaption: "Atomic Stealer (AMOS) macOS ClickFix Delivery Lure",
    gallery: [
      {
        id: "EVID-048-01",
        type: "ClickFix Lure",
        url: "images/TF-048_atomic_real_01.png",
        title: "Atomic Stealer (AMOS) macOS ClickFix Delivery Lure",
        caption: "ANY.RUN sandbox capture showing social engineering prompt tricking macOS users into executing malicious terminal commands."
      },
      {
        id: "EVID-048-02",
        type: "C2 Exfiltration",
        url: "images/TF-048_atomic_real_02.png",
        title: "Atomic Stealer Telegram & HTTP Exfiltration Traffic",
        caption: "Network capture tracking exfiltration of Keychain databases, browser cookies, and hardware specs to adversary C2."
      },
      {
        id: "EVID-048-03",
        type: "Architecture Schematic",
        url: "images/TF-048_atomic_arch.svg",
        title: "Atomic Stealer (AMOS) Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Telegram Bot API, Encrypted Web Servers command infrastructure."
      }
    ],
    en: {
      type: "macOS InfoStealer",
      summary: "The definitive infostealer targeting Apple macOS ecosystems, specializing in Keychain and wallet harvesting.",
      desc: "Deploys deceitful native AppleScript credential prompts to unlock system Keychains and vacuum stored browser secrets.",
      tech: ["Language: Go / AppleScript", "C2 Protocol: Telegram Bot API and HTTPS exfiltration gateways", "Capabilities: macOS Keychain dumping, browser credential theft, hot crypto wallet scraping"],
      propagation: "Google Search malvertising promoting fake macOS software downloads.",
      defense: ["Educate users never to supply administrator passwords to untrusted installers."],
      whyWatch: "The dominant threat against Apple macOS workstations in 2026."
    },
    sources: [{ name: "Malwarebytes AMOS macOS Threat Profile", type: "Security" }]
  },
  {
    id: "TF-049",
    num: "049",
    name: "ShadowPad",
    category: "C2 Framework",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Modular Shared APT Backdoor",
    c2: "DNS, Custom Binary Protocols, Proxy Nodes",
    mitre: ["T1071.004", "T1055", "T1574.002"],
    image: "images/TF-049_shadowpad_real_01.svg",
    imageCaption: "ShadowPad Modular Backdoor Architecture",
    gallery: [
      {
        id: "EVID-049-01",
        type: "Plugin Engine",
        url: "images/TF-049_shadowpad_real_01.svg",
        title: "ShadowPad Modular Backdoor Architecture",
        caption: "Technical visualization of ShadowPad virtual file system and dynamic DLL plugin dispatch table."
      },
      {
        id: "EVID-049-02",
        type: "Disassembly Analysis",
        url: "images/TF-049_shadowpad_real_02.svg",
        title: "ShadowPad Root Loader & DLL Sideloading Routine",
        caption: "Disassembly showing legitimate signed host binary abused for DLL search-order hijacking."
      },
      {
        id: "EVID-049-03",
        type: "Architecture Schematic",
        url: "images/TF-049_shadowpad_arch.svg",
        title: "ShadowPad Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and DNS, Custom Binary Protocols, Proxy Nodes command infrastructure."
      }
    ],
    en: {
      type: "Modular APT Backdoor",
      summary: "Elite modular backdoor shared among sophisticated Chinese state-sponsored threat groups for espionage.",
      desc: "Heavily reliant on DLL sideloading through legitimate commercial software to maintain long-term covert operational footholds.",
      tech: ["Language: C++", "C2 Protocol: Custom encrypted binary streams and DNS tunneling", "Capabilities: Deep modular surveillance, keylogging, lateral pivoting, silent execution"],
      propagation: "Supply chain compromises and high-level enterprise infiltration.",
      defense: ["Audit DLL search order hijacking anomalies and inspect unmapped memory hooks."],
      whyWatch: "The premier shared toolset for state-aligned cyber espionage operations."
    },
    sources: [{ name: "Secureworks Counter Threat Unit ShadowPad Analysis", type: "Security" }]
  },
  {
    id: "TF-050",
    num: "050",
    name: "PlugX / Korplug",
    category: "RAT",
    status: "ACTIVE",
    relevance: "HIGH",
    teamStatus: "MONITORED",
    lang: "C++",
    arch: "Veteran Modular Remote Access Tool",
    c2: "Custom P2P, DNS Tunneling, Worm-like USB Spreading",
    mitre: ["T1574.002", "T1056.001", "T1091", "T1071"],
    image: "images/TF-050_plugx_real_01.png",
    imageCaption: "PlugX (Korplug) Payload Builder & Configurator",
    gallery: [
      {
        id: "EVID-050-01",
        type: "Builder UI",
        url: "images/TF-050_plugx_real_01.png",
        title: "PlugX (Korplug) Payload Builder & Configurator",
        caption: "Operator configurator GUI showing encryption key generation, C2 domain insertion, and service installation options."
      },
      {
        id: "EVID-050-02",
        type: "DLL Sideloading",
        url: "images/TF-050_plugx_real_02.svg",
        title: "PlugX DLL Search-Order Hijacking Routine",
        caption: "Forensic diagram tracking legitimate executable loading malicious proxy DLL and decrypting .dat payload."
      },
      {
        id: "EVID-050-03",
        type: "Architecture Schematic",
        url: "images/TF-050_plugx_arch.svg",
        title: "PlugX / Korplug Technical Infection Chain & Architecture",
        caption: "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Custom P2P, DNS Tunneling, Worm-like USB Spreading command infrastructure."
      }
    ],
    en: {
      type: "Modular RAT & Worm",
      summary: "Legendary modular RAT weaponized by advanced threat actors for over a decade with USB worm propagation.",
      desc: "Pioneered DLL sideloading using legitimate signed security executables, bridging air-gapped networks via USB replication.",
      tech: ["Language: Pure C++", "C2 Protocol: Custom P2P routing and DNS tunneling channels", "Capabilities: Full remote administration, document harvesting, USB air-gap jumping"],
      propagation: "Infected removable drives, spear-phishing diplomacy lures, and supply chain compromises.",
      defense: ["Disable USB storage execution and monitor DLL sideloading adjacent to trusted binaries."],
      whyWatch: "The defining classic APT Trojan continually adapting into 2026 defensive landscapes."
    },
    sources: [{ name: "Sekoia.io Operation PlugX Clean-up & Technical Study", type: "Security" }]
  }
];

if (typeof module !== 'undefined' && module.exports) {
  module.exports = THREATS_DATA;
}
