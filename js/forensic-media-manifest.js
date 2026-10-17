/**
 * CYBERTRACE INTELLIGENCE PLATFORM
 * Strict 1-to-1 Forensic Media Manifest (Pure Technical English)
 */

const FORENSIC_MEDIA_MANIFEST = {
  "TF-001": {
    "name": "AsyncRAT",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-001-01",
        "url": "images/TF-001_asyncrat_real_01.png",
        "type": "Builder UI",
        "title": "AsyncRAT Client Payload Builder & Configurator",
        "desc": "Operator configurator GUI showing TLS X.509 certificate generation, keylogger toggles, process injection, and persistence configuration."
      },
      {
        "id": "EVID-001-02",
        "url": "images/TF-001_asyncrat_real_02.svg",
        "type": "Surveillance Telemetry",
        "title": "AsyncRAT Remote Desktop & Session Monitoring",
        "desc": "Interactive desktop surveillance module capturing victim screen buffers and keystroke telemetry streams."
      },
      {
        "id": "EVID-001-03",
        "url": "images/TF-001_asyncrat_arch.svg",
        "type": "Architecture Schematic",
        "title": "AsyncRAT Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Dynamic DNS, Cloudflare Tunnels, TLS CN=AsyncRAT command infrastructure."
      }
    ]
  },
  "TF-002": {
    "name": "Dolphin X",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-002-01",
        "url": "images/TF-002_dolphinx_real_01.png",
        "type": "Builder UI",
        "title": "Dolphin X AI Stealer Builder Interface",
        "desc": "Builder interface setting target heuristics, browser extension targeting, and polymorphic stub compilation parameters."
      },
      {
        "id": "EVID-002-02",
        "url": "images/TF-002_dolphinx_real_02.png",
        "type": "Exfiltration Channel",
        "title": "Dolphin X Encrypted Telegram Exfiltration Feed",
        "desc": "Operator notification channel broadcasting compromised victim specifications, geolocations, and encrypted credential archives."
      },
      {
        "id": "EVID-002-03",
        "url": "images/TF-002_dolphinx_arch.svg",
        "type": "Architecture Schematic",
        "title": "Dolphin X Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Encrypted Telegram API, Cloudflare Workers, Decentralized Webhooks command infrastructure."
      },
      {
        "id": "EVID-002-04",
        "url": "images/dolphinx_05_dashboard.png",
        "type": "C2 Dashboard",
        "title": "Dolphin X Central Web Telemetry Dashboard",
        "desc": "Centralized operator interface aggregating infected victim nodes and exfiltrated credential archives."
      }
    ]
  },
  "TF-003": {
    "name": "Lumma Stealer",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-003-01",
        "url": "images/TF-003_lumma_real_01.png",
        "type": "Sandbox Execution",
        "title": "Lumma Stealer Process Execution Graph",
        "desc": "ANY.RUN sandbox telemetry displaying multi-stage process injection, anti-analysis loops, and credential harvesting routines."
      },
      {
        "id": "EVID-003-02",
        "url": "images/TF-003_lumma_real_02.png",
        "type": "C2 Communication",
        "title": "LummaC2 Fast-Flux Network Handshake",
        "desc": "Encrypted HTTP C2 beaconing protocol showing dynamic domain resolution and target configuration retrieval."
      },
      {
        "id": "EVID-003-03",
        "url": "images/TF-003_lumma_arch.svg",
        "type": "Architecture Schematic",
        "title": "Lumma Stealer Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Fast-Flux Domains, Cloudflare Proxies, Multi-tier C2 command infrastructure."
      }
    ]
  },
  "TF-004": {
    "name": "RedLine Stealer",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-004-01",
        "url": "images/TF-004_redline_real_01.png",
        "type": "Process Injection",
        "title": "RedLine Stealer Lua Bytecode Execution",
        "desc": "ANY.RUN sandbox capture showing Lua bytecode decompression and process hollowing into legitimate Windows processes."
      },
      {
        "id": "EVID-004-02",
        "url": "images/TF-004_redline_real_02.png",
        "type": "Memory Extraction",
        "title": "RedLine Browser Credential Vault Grabbing",
        "desc": "Forensic memory trace extracting DPAPI-protected credentials, session cookies, and cryptocurrency wallets."
      },
      {
        "id": "EVID-004-03",
        "url": "images/TF-004_redline_arch.svg",
        "type": "Architecture Schematic",
        "title": "RedLine Stealer Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Direct TCP, WCF Endpoints, Telegram Exfiltration command infrastructure."
      }
    ]
  },
  "TF-005": {
    "name": "Vidar Stealer",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-005-01",
        "url": "images/TF-005_vidar_real_01.png",
        "type": "C2 Telemetry",
        "title": "Vidar Dead-Drop Resolver Telemetry",
        "desc": "ANY.RUN network capture displaying Telegram channel lookups used as dead-drop resolvers for C2 IP address retrieval."
      },
      {
        "id": "EVID-005-02",
        "url": "images/TF-005_vidar_real_02.png",
        "type": "Payload Execution",
        "title": "Vidar Stealer SQLite Harvesting Routine",
        "desc": "Memory analysis showing automated extraction of login data from Chromium and Gecko-based browser databases."
      },
      {
        "id": "EVID-005-03",
        "url": "images/TF-005_vidar_arch.svg",
        "type": "Architecture Schematic",
        "title": "Vidar Stealer Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Steam Profiles, Mastodon, Telegram, HTTP POST command infrastructure."
      }
    ]
  },
  "TF-006": {
    "name": "Agent Tesla",
    "category": "Spyware",
    "items": [
      {
        "id": "EVID-006-01",
        "url": "images/TF-006_agenttesla_real_01.png",
        "type": "Execution Chain",
        "title": "Agent Tesla Process Tree & Weaponized Document",
        "desc": "Forensic sandbox process hierarchy showing weaponized office document execution and payload staging."
      },
      {
        "id": "EVID-006-02",
        "url": "images/TF-006_agenttesla_real_02.png",
        "type": "Exfiltration Module",
        "title": "Agent Tesla SMTP Exfiltration Routine",
        "desc": "Decompiled .NET routine responsible for packaging keystroke logs and dispatching them via TLS SMTP channels."
      },
      {
        "id": "EVID-006-03",
        "url": "images/TF-006_agenttesla_arch.svg",
        "type": "Architecture Schematic",
        "title": "Agent Tesla Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and SMTP, FTP, Telegram Webhooks, Discord API command infrastructure."
      }
    ]
  },
  "TF-007": {
    "name": "Remcos RAT",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-007-01",
        "url": "images/TF-007_remcos_real_01.png",
        "type": "Builder UI",
        "title": "Remcos Professional Client Builder & Evasion Configurator",
        "desc": "Builder interface displaying TLS encryption parameters, rootkit cloaking, watchdog persistence, and anti-analysis options."
      },
      {
        "id": "EVID-007-02",
        "url": "images/TF-007_remcos_real_02.svg",
        "type": "Operator Console",
        "title": "Remcos Remote Administration Management Console",
        "desc": "Management console monitoring connected remote bots, system telemetry, and active surveillance streams."
      },
      {
        "id": "EVID-007-03",
        "url": "images/TF-007_remcos_arch.svg",
        "type": "Architecture Schematic",
        "title": "Remcos RAT Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Direct Encrypted TLS, Dynamic DNS, SOCKS5 Proxy command infrastructure."
      }
    ]
  },
  "TF-008": {
    "name": "XWorm",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-008-01",
        "url": "images/TF-008_xworm_real_01.png",
        "type": "Builder UI",
        "title": "XWorm Advanced Payload Builder Interface",
        "desc": "Configurator interface setting USB spreaders, clipper addresses, ransomware routines, and HVNC modules."
      },
      {
        "id": "EVID-008-02",
        "url": "images/TF-008_xworm_real_02.svg",
        "type": "Clipper Module",
        "title": "XWorm Cryptocurrency Clipper Memory Routine",
        "desc": "Disassembly showing clipboard regex monitoring for Bitcoin, Ethereum, and Monero wallet string replacement."
      },
      {
        "id": "EVID-008-03",
        "url": "images/TF-008_xworm_arch.svg",
        "type": "Architecture Schematic",
        "title": "XWorm Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and AES Encrypted TCP, Telegram, Pastebin Dead-Drop command infrastructure."
      }
    ]
  },
  "TF-009": {
    "name": "DarkGate",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-009-01",
        "url": "images/TF-009_darkgate_real_01.png",
        "type": "Infection Vector",
        "title": "DarkGate Malicious MSI & AutoIt Lure",
        "desc": "Malwarebytes forensic capture showing rogue MSI installer dropping obfuscated AutoIt interpreter script stubs."
      },
      {
        "id": "EVID-009-02",
        "url": "images/TF-009_darkgate_real_02.png",
        "type": "Config Extractor",
        "title": "DarkGate Extracted C2 Configuration Parameters",
        "desc": "Automated extractor output displaying AES-encrypted C2 servers, botnet flags, and evasion switches."
      },
      {
        "id": "EVID-009-03",
        "url": "images/TF-009_darkgate_arch.svg",
        "type": "Architecture Schematic",
        "title": "DarkGate Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Custom HTTP Encryption, Obfuscated Query Params command infrastructure."
      },
      {
        "id": "EVID-009-04",
        "url": "images/darkgate_04_traffic.jpeg",
        "type": "Network Packet Capture",
        "title": "DarkGate HTTP C2 Request Header Analysis",
        "desc": "Raw packet inspection showing HTTP POST parameters and custom User-Agent beacons."
      }
    ]
  },
  "TF-010": {
    "name": "Rhadamanthys",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-010-01",
        "url": "images/TF-010_rhadamanthys_real_01.png",
        "type": "Builder UI",
        "title": "Rhadamanthys Stealer Operator Panel Interface",
        "desc": "Web-based management console tracking active victim infections, geolocations, and extracted credential counts."
      },
      {
        "id": "EVID-010-02",
        "url": "images/TF-010_rhadamanthys_real_02.svg",
        "type": "Memory VM",
        "title": "Rhadamanthys Custom Virtual Machine Architecture",
        "desc": "Disassembly showing custom bytecode VM interpreter designed to thwart static analysis and heuristic emulators."
      },
      {
        "id": "EVID-010-03",
        "url": "images/TF-010_rhadamanthys_arch.svg",
        "type": "Architecture Schematic",
        "title": "Rhadamanthys Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Custom TLS-like Protocol, Hidden TCP Handshake command infrastructure."
      }
    ]
  },
  "TF-011": {
    "name": "Stealc",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-011-01",
        "url": "images/TF-011_stealc_real_01.png",
        "type": "C2 Config",
        "title": "Stealc C2 Communication Protocol Analysis",
        "desc": "ANY.RUN forensic capture showing RC4 string decryption and endpoint registration with command-and-control servers."
      },
      {
        "id": "EVID-011-02",
        "url": "images/TF-011_stealc_real_02.png",
        "type": "Target Grabbing",
        "title": "Stealc Modular Data Harvesting Pipeline",
        "desc": "Execution capture showing file-grabbing rules targeting browser extensions, Discord tokens, and crypto wallet paths."
      },
      {
        "id": "EVID-011-03",
        "url": "images/TF-011_stealc_arch.svg",
        "type": "Architecture Schematic",
        "title": "Stealc Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and RC4 Encrypted HTTP POST command infrastructure."
      }
    ]
  },
  "TF-012": {
    "name": "Havoc C2",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-012-01",
        "url": "images/TF-012_havoc_real_01.png",
        "type": "Payload Generator",
        "title": "Havoc Framework Demon Payload Configurator",
        "desc": "Official Havoc client UI configuring Demon agent sleep obfuscation, indirect syscalls, and x64 shellcode injection stubs."
      },
      {
        "id": "EVID-012-02",
        "url": "images/TF-012_havoc_real_02.png",
        "type": "Operator Console",
        "title": "Havoc C2 Interactive Session Console",
        "desc": "Operator UI managing compromised enterprise hosts, active Demon beacons, and lateral movement listeners."
      },
      {
        "id": "EVID-012-03",
        "url": "images/TF-012_havoc_arch.svg",
        "type": "Architecture Schematic",
        "title": "Havoc C2 Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Demon Agent, Malleable HTTP/HTTPS, SMB Pipes command infrastructure."
      }
    ]
  },
  "TF-013": {
    "name": "Sliver C2",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-013-01",
        "url": "images/TF-013_sliver_real_01.png",
        "type": "Operator Console",
        "title": "Sliver C2 Interactive Command Console",
        "desc": "Operator shell session showing active multiplayer beacons, WireGuard tunnels, and mTLS listener parameters."
      },
      {
        "id": "EVID-013-02",
        "url": "images/TF-013_sliver_real_02.svg",
        "type": "Injection Routine",
        "title": "Sliver Process Injection & Evasion Engine",
        "desc": "Technical visualization of indirect syscall execution and thread stack spoofing mechanisms."
      },
      {
        "id": "EVID-013-03",
        "url": "images/TF-013_sliver_arch.svg",
        "type": "Architecture Schematic",
        "title": "Sliver C2 Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and mTLS, WireGuard, HTTP/HTTPS, DNS Canaries command infrastructure."
      }
    ]
  },
  "TF-014": {
    "name": "Mythic C2",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-014-01",
        "url": "images/TF-014_mythic_real_01.svg",
        "type": "Operator Dashboard",
        "title": "Mythic C2 Operation Management Dashboard",
        "desc": "Web interface aggregating active agent callbacks, tasking queues, and modular payload build profiles."
      },
      {
        "id": "EVID-014-02",
        "url": "images/TF-014_mythic_real_02.svg",
        "type": "Payload Architecture",
        "title": "Mythic Modular Agent Communication Engine",
        "desc": "C2 communication trace showing JSON-RPC tasking and staging across custom translation containers."
      },
      {
        "id": "EVID-014-03",
        "url": "images/TF-014_mythic_arch.svg",
        "type": "Architecture Schematic",
        "title": "Mythic C2 Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Modular Agent Ecosystem, WebSocket, WebDAV command infrastructure."
      }
    ]
  },
  "TF-015": {
    "name": "QuasarRAT",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-015-01",
        "url": "images/TF-015_quasarrat_real_01.png",
        "type": "Builder UI",
        "title": "QuasarRAT Open-Source Builder & Certificate Generator",
        "desc": "Client builder GUI configuring TLS certificate pinning, startup registry persistence, and keylogger hooks."
      },
      {
        "id": "EVID-015-02",
        "url": "images/TF-015_quasarrat_real_02.svg",
        "type": "Surveillance Module",
        "title": "QuasarRAT Surveillance & File Manager Interface",
        "desc": "Interactive operator panel monitoring victim file systems, reverse socks proxies, and active processes."
      },
      {
        "id": "EVID-015-03",
        "url": "images/TF-015_quasarrat_arch.svg",
        "type": "Architecture Schematic",
        "title": "QuasarRAT Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and AES-128 Encrypted TCP Sockets command infrastructure."
      }
    ]
  },
  "TF-016": {
    "name": "Warzone RAT / Ave Maria",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-016-01",
        "url": "images/TF-016_warzone_real_01.png",
        "type": "Builder UI",
        "title": "Warzone RAT (Ave Maria) Builder Interface",
        "desc": "Configurator GUI showing UAC bypass method selection, privilege escalation hooks, and password recovery modules."
      },
      {
        "id": "EVID-016-02",
        "url": "images/TF-016_warzone_real_02.svg",
        "type": "Privilege Escalation",
        "title": "Warzone RAT AveMaria Memory Persistence Engine",
        "desc": "Forensic disassembly showing task scheduler registration and explorer.exe process hollowing routines."
      },
      {
        "id": "EVID-016-03",
        "url": "images/TF-016_warzone_arch.svg",
        "type": "Architecture Schematic",
        "title": "Warzone RAT / Ave Maria Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Custom Encrypted Protocol over TCP command infrastructure."
      }
    ]
  },
  "TF-017": {
    "name": "GuLoader / CloudEyE",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-017-01",
        "url": "images/TF-017_guloader_real_01.jpg",
        "type": "Execution Chain",
        "title": "GuLoader (CloudEyE) Multi-Stage Shellcode Chain",
        "desc": "ANY.RUN threat infographic detailing VBS dropper, registry payload storage, and shellcode injection sequence."
      },
      {
        "id": "EVID-017-02",
        "url": "images/TF-017_guloader_real_02.png",
        "type": "Anti-Analysis Routine",
        "title": "GuLoader Vectored Exception Handling (VEH) Check",
        "desc": "Process memory disassembly showing hardware breakpoint detection and anti-debugging exception routines."
      },
      {
        "id": "EVID-017-03",
        "url": "images/TF-017_guloader_arch.svg",
        "type": "Architecture Schematic",
        "title": "GuLoader / CloudEyE Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Google Drive, OneDrive, Encrypted Shellcode Delivery command infrastructure."
      }
    ]
  },
  "TF-018": {
    "name": "Pikabot",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-018-01",
        "url": "images/TF-018_pikabot_real_01.svg",
        "type": "Loader Routine",
        "title": "Pikabot Modular Core Loader Architecture",
        "desc": "Forensic sandbox process tree displaying encrypted blob unpacking and DLL injection into legitimate system processes."
      },
      {
        "id": "EVID-018-02",
        "url": "images/TF-018_pikabot_real_02.svg",
        "type": "C2 Protocol",
        "title": "Pikabot Network Beacon & RC4 Decryption",
        "desc": "Network capture analyzing AES-CBC C2 beaconing structure and infected endpoint fingerprinting."
      },
      {
        "id": "EVID-018-03",
        "url": "images/TF-018_pikabot_arch.svg",
        "type": "Architecture Schematic",
        "title": "Pikabot Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTPS with RC4 Encrypted JSON Payloads command infrastructure."
      }
    ]
  },
  "TF-019": {
    "name": "Qakbot / QBot",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-019-01",
        "url": "images/TF-019_qakbot_real_01.svg",
        "type": "Banking Module",
        "title": "Qakbot (QBot) Core Web-Inject & Delivery Engine",
        "desc": "Forensic memory trace showing thread hijacking and man-in-the-browser banking credential interception."
      },
      {
        "id": "EVID-019-02",
        "url": "images/TF-019_qakbot_real_02.svg",
        "type": "Process Hollowing",
        "title": "Qakbot Process Replacement in wermgr.exe",
        "desc": "Process monitor telemetry tracking hollowed process creation and memory section remapping."
      },
      {
        "id": "EVID-019-03",
        "url": "images/TF-019_qakbot_arch.svg",
        "type": "Architecture Schematic",
        "title": "Qakbot / QBot Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Tiered Botnet, Compromised WordPress Sites, Custom TLS command infrastructure."
      }
    ]
  },
  "TF-020": {
    "name": "Emotet",
    "category": "Botnet",
    "items": [
      {
        "id": "EVID-020-01",
        "url": "images/TF-020_emotet_real_01.svg",
        "type": "Botnet Architecture",
        "title": "Emotet Epoch Tier-1 Command Infrastructure",
        "desc": "Telemetry diagram illustrating compromised router proxy chains and automated spambot email harvesting modules."
      },
      {
        "id": "EVID-020-02",
        "url": "images/TF-020_emotet_real_02.svg",
        "type": "Payload Execution",
        "title": "Emotet Encrypted DLL Loader Disassembly",
        "desc": "Disassembly showing control flow flattening and string decryption routines executing inside regsvr32.exe."
      },
      {
        "id": "EVID-020-03",
        "url": "images/TF-020_emotet_arch.svg",
        "type": "Architecture Schematic",
        "title": "Emotet Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Custom Encrypted Protocol over HTTP/HTTPS command infrastructure."
      }
    ]
  },
  "TF-021": {
    "name": "LockBit 3.0",
    "category": "Ransomware",
    "items": [
      {
        "id": "EVID-021-01",
        "url": "images/TF-021_lockbit_real_01.png",
        "type": "Ransomware Execution",
        "title": "LockBit 3.0 (Black) Execution Process Tree",
        "desc": "ANY.RUN sandbox capture showing service termination, shadow copy deletion, and high-speed file encryption."
      },
      {
        "id": "EVID-021-02",
        "url": "images/TF-021_lockbit_real_02.png",
        "type": "Leak Infrastructure",
        "title": "LockBit Darknet Tor Extortion Portal",
        "desc": "Onion portal interface detailing ransom demands, countdown timers, and stolen proof-of-concept data archives."
      },
      {
        "id": "EVID-021-03",
        "url": "images/TF-021_lockbit_arch.svg",
        "type": "Architecture Schematic",
        "title": "LockBit 3.0 Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Tor Hidden Services, Decentralized Leaks Portals command infrastructure."
      }
    ]
  },
  "TF-022": {
    "name": "BlackCat / ALPHV",
    "category": "Ransomware",
    "items": [
      {
        "id": "EVID-022-01",
        "url": "images/TF-022_blackcat_real_01.png",
        "type": "Execution Flags",
        "title": "BlackCat (ALPHV) Rust CLI Execution Parameters",
        "desc": "Forensic terminal capture displaying command-line switches for domain escalation, safemode reboot, and shadow wipe."
      },
      {
        "id": "EVID-022-02",
        "url": "images/TF-022_blackcat_real_02.svg",
        "type": "Ransom Artifact",
        "title": "BlackCat Recover-My-Files Note & Tor Gateway",
        "desc": "Generated ransom text note dropped on encrypted endpoints pointing to the ALPHV negotiation portal."
      },
      {
        "id": "EVID-022-03",
        "url": "images/TF-022_blackcat_arch.svg",
        "type": "Architecture Schematic",
        "title": "BlackCat / ALPHV Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Tor Onion Nodes, REST API Command Channels command infrastructure."
      }
    ]
  },
  "TF-023": {
    "name": "Akira",
    "category": "Ransomware",
    "items": [
      {
        "id": "EVID-023-01",
        "url": "images/TF-023_akira_real_01.svg",
        "type": "Extortion Engine",
        "title": "Akira Ransomware Enterprise Encryption Routine",
        "desc": "Forensic capture detailing C++ multi-threaded file encryption using ChaCha20 and RSA public key wrapping."
      },
      {
        "id": "EVID-023-02",
        "url": "images/TF-023_akira_real_02.svg",
        "type": "Disassembly Analysis",
        "title": "Akira Volume Shadow Deletion & Service Killer",
        "desc": "IDA Pro disassembly highlighting PowerShell invocations wiping backup repositories and stopping SQL services."
      },
      {
        "id": "EVID-023-03",
        "url": "images/TF-023_akira_arch.svg",
        "type": "Architecture Schematic",
        "title": "Akira Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Tor Chat Portal & Data Leak Site command infrastructure."
      }
    ]
  },
  "TF-024": {
    "name": "Medusa",
    "category": "Ransomware",
    "items": [
      {
        "id": "EVID-024-01",
        "url": "images/TF-024_medusa_real_01.svg",
        "type": "Extortion Portal",
        "title": "Medusa Ransomware Blog & Victim Negotiation Console",
        "desc": "Tor negotiation portal showing victim countdown timers, ransom payment deadlines, and published leak archives."
      },
      {
        "id": "EVID-024-02",
        "url": "images/TF-024_medusa_real_02.svg",
        "type": "Disassembly Analysis",
        "title": "Medusa Service Termination & Process Sweeper",
        "desc": "Disassembly showing enumeration and killing of antivirus, database, and backup management services."
      },
      {
        "id": "EVID-024-03",
        "url": "images/TF-024_medusa_arch.svg",
        "type": "Architecture Schematic",
        "title": "Medusa Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Medusa Blog on Tor, Public Telegram Broadcasts command infrastructure."
      }
    ]
  },
  "TF-025": {
    "name": "Phobos / 8Base",
    "category": "Ransomware",
    "items": [
      {
        "id": "EVID-025-01",
        "url": "images/TF-025_phobos_real_01.svg",
        "type": "Decryptor Utility",
        "title": "Phobos / 8Base Ransomware Execution & Recovery Stub",
        "desc": "Forensic capture displaying file extension appending (.id[...].[email].phobos) and ransom note deployment."
      },
      {
        "id": "EVID-025-02",
        "url": "images/TF-025_phobos_real_02.svg",
        "type": "Network Telemetry",
        "title": "Phobos Command and Control Beaconing",
        "desc": "Network telemetry trace tracking victim system registration and AES encryption key escrow exchange."
      },
      {
        "id": "EVID-025-03",
        "url": "images/TF-025_phobos_arch.svg",
        "type": "Architecture Schematic",
        "title": "Phobos / 8Base Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Email Negotiation & Tor Mirrors command infrastructure."
      }
    ]
  },
  "TF-026": {
    "name": "Formbook / XLoader",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-026-01",
        "url": "images/TF-026_formbook_real_01.png",
        "type": "Injection Scheme",
        "title": "Formbook / XLoader Multi-Level Injection Chain",
        "desc": "ANY.RUN technical diagram illustrating payload decryption and nested thread injection into system binaries."
      },
      {
        "id": "EVID-026-02",
        "url": "images/TF-026_formbook_real_02.png",
        "type": "C2 Decryption",
        "title": "Formbook Traffic Encryption & Decryption Engine",
        "desc": "Forensic memory trace detailing base64 and RC4 decoding of command-and-control responses."
      },
      {
        "id": "EVID-026-03",
        "url": "images/TF-026_formbook_arch.svg",
        "type": "Architecture Schematic",
        "title": "Formbook / XLoader Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Decoy Domains, HTTP POST with Layered Encryption command infrastructure."
      }
    ]
  },
  "TF-027": {
    "name": "Bumblebee",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-027-01",
        "url": "images/TF-027_bumblebee_real_01.svg",
        "type": "Stager Routine",
        "title": "Bumblebee Modular Loader Staging Routine",
        "desc": "Forensic sandbox process showing WMI reconnaissance, process hollowing, and secondary payload staging."
      },
      {
        "id": "EVID-027-02",
        "url": "images/TF-027_bumblebee_real_02.svg",
        "type": "Disassembly Analysis",
        "title": "Bumblebee WebSocket C2 Handshake Routine",
        "desc": "Disassembly tracking WebSocket connection initialization and JSON-formatted command exchange."
      },
      {
        "id": "EVID-027-03",
        "url": "images/TF-027_bumblebee_arch.svg",
        "type": "Architecture Schematic",
        "title": "Bumblebee Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and WebSockets, Encrypted Custom Protocols command infrastructure."
      }
    ]
  },
  "TF-028": {
    "name": "IcedID (BokBot)",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-028-01",
        "url": "images/TF-028_icedid_real_01.svg",
        "type": "Steganography",
        "title": "IcedID (BokBot) Steganographic PNG Loader",
        "desc": "Forensic image analysis showing extraction of hidden encrypted payload from downloaded PNG image files."
      },
      {
        "id": "EVID-028-02",
        "url": "images/TF-028_icedid_real_02.svg",
        "type": "Banking Module",
        "title": "IcedID Process Injection into svchost.exe",
        "desc": "Process monitor trace tracking hollowed svchost.exe instances used for banking credential theft."
      },
      {
        "id": "EVID-028-03",
        "url": "images/TF-028_icedid_arch.svg",
        "type": "Architecture Schematic",
        "title": "IcedID (BokBot) Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Steganography in PNG Images, Custom TLS command infrastructure."
      }
    ]
  },
  "TF-029": {
    "name": "DanaBot",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-029-01",
        "url": "images/TF-029_danabot_real_01.svg",
        "type": "Operator Panel",
        "title": "DanaBot Banking Trojan Control Interface",
        "desc": "Operator web panel tracking active banking bot infections, compromised corporate networks, and injection rules."
      },
      {
        "id": "EVID-029-02",
        "url": "images/TF-029_danabot_real_02.svg",
        "type": "Disassembly Analysis",
        "title": "DanaBot Modular Architecture & Plugin Loader",
        "desc": "Disassembly showing dynamic download and decryption of specialized sniffing and video capture modules."
      },
      {
        "id": "EVID-029-03",
        "url": "images/TF-029_danabot_arch.svg",
        "type": "Architecture Schematic",
        "title": "DanaBot Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Tor Network & Encrypted Binary Sockets command infrastructure."
      }
    ]
  },
  "TF-030": {
    "name": "SmokeLoader",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-030-01",
        "url": "images/TF-030_smokeloader_real_01.svg",
        "type": "Plugin Engine",
        "title": "SmokeLoader Modular Plugin System",
        "desc": "Technical visualization of SmokeLoader core memory resident loop loading encrypted payload extensions."
      },
      {
        "id": "EVID-030-02",
        "url": "images/TF-030_smokeloader_real_02.svg",
        "type": "Anti-Analysis",
        "title": "SmokeLoader API Hashing & VM Detection",
        "desc": "Disassembly showing API name hashing algorithms used to bypass security solution import table monitoring."
      },
      {
        "id": "EVID-030-03",
        "url": "images/TF-030_smokeloader_arch.svg",
        "type": "Architecture Schematic",
        "title": "SmokeLoader Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Decoy HTTP Queries, Encrypted Payloads command infrastructure."
      }
    ]
  },
  "TF-031": {
    "name": "Cobalt Strike",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-031-01",
        "url": "images/TF-031_cobaltstrike_real_01.png",
        "type": "Listeners UI",
        "title": "Cobalt Strike Listener Management & Beacon Console",
        "desc": "Operator interface configuring HTTP, HTTPS, and DNS malleable C2 listeners and tracking active Beacons."
      },
      {
        "id": "EVID-031-02",
        "url": "images/TF-031_cobaltstrike_real_02.svg",
        "type": "Beacon Architecture",
        "title": "Cobalt Strike In-Memory Beacon Reflection Engine",
        "desc": "Technical schematic showing Reflective DLL loading, sleep masking, and thread stack spoofing mechanisms."
      },
      {
        "id": "EVID-031-03",
        "url": "images/TF-031_cobaltstrike_arch.svg",
        "type": "Architecture Schematic",
        "title": "Cobalt Strike Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Malleable C2, DNS/HTTPS/SMB Beacons command infrastructure."
      }
    ]
  },
  "TF-032": {
    "name": "Brute Ratel C4",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-032-01",
        "url": "images/TF-032_bruteratel_real_01.png",
        "type": "Payload Execution",
        "title": "Brute Ratel C4 Badger Execution Graph",
        "desc": "ANY.RUN sandbox process trace tracking Badger payload injection and memory manipulation routines."
      },
      {
        "id": "EVID-032-02",
        "url": "images/TF-032_bruteratel_real_02.png",
        "type": "Syscall Engine",
        "title": "Brute Ratel Indirect Syscall Execution Routine",
        "desc": "Disassembly showing dynamic SSN resolution and indirect syscall execution bypassing user-mode EDR hooks."
      },
      {
        "id": "EVID-032-03",
        "url": "images/TF-032_bruteratel_arch.svg",
        "type": "Architecture Schematic",
        "title": "Brute Ratel C4 Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Badger Agent, DoH, Custom Syscalls command infrastructure."
      }
    ]
  },
  "TF-033": {
    "name": "NetSupport RAT",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-033-01",
        "url": "images/TF-033_netsupport_real_01.svg",
        "type": "Gateway Config",
        "title": "NetSupport RAT Gateway Configuration & Deployment",
        "desc": "Forensic analysis of client32.ini configuration parameters establishing covert gateway reverse connections."
      },
      {
        "id": "EVID-033-02",
        "url": "images/TF-033_netsupport_real_02.svg",
        "type": "Disassembly Analysis",
        "title": "NetSupport RAT Screen Capture & Keystroke Monitor",
        "desc": "Disassembly tracking surveillance API hooks capturing remote desktop buffers and operator commands."
      },
      {
        "id": "EVID-033-03",
        "url": "images/TF-033_netsupport_arch.svg",
        "type": "Architecture Schematic",
        "title": "NetSupport RAT Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTP Gateway, Client-Server Sockets command infrastructure."
      }
    ]
  },
  "TF-034": {
    "name": "NjRAT / Bladabindi",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-034-01",
        "url": "images/TF-034_njrat_real_01.png",
        "type": "Builder UI",
        "title": "NjRAT (Bladabindi) Golden Edition Builder Interface",
        "desc": "Visual Basic .NET builder configuring payload persistence, dynamic DNS connection strings, and mutex flags."
      },
      {
        "id": "EVID-034-02",
        "url": "images/TF-034_njrat_real_02.svg",
        "type": "Operator Console",
        "title": "NjRAT Victim Management & Webcam Surveillance Console",
        "desc": "Operator UI managing connected victim bots, remote desktop viewing, and live microphone capture streams."
      },
      {
        "id": "EVID-034-03",
        "url": "images/TF-034_njrat_arch.svg",
        "type": "Architecture Schematic",
        "title": "NjRAT / Bladabindi Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Direct TCP Sockets with Delimited Strings command infrastructure."
      }
    ]
  },
  "TF-035": {
    "name": "DCRat (DarkCrystal)",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-035-01",
        "url": "images/TF-035_dcrat_real_01.png",
        "type": "Builder UI",
        "title": "DCRat (DarkCrystal) Studio & Plugin Builder",
        "desc": "Modern builder interface displaying modular plugin selections, stealer configurations, and obfuscation options."
      },
      {
        "id": "EVID-035-02",
        "url": "images/TF-035_dcrat_real_02.svg",
        "type": "Operator Console",
        "title": "DCRat Botnet Administration Dashboard",
        "desc": "Web-based administration console tracking active victim nodes, geolocations, and extracted credentials."
      },
      {
        "id": "EVID-035-03",
        "url": "images/TF-035_dcrat_arch.svg",
        "type": "Architecture Schematic",
        "title": "DCRat (DarkCrystal) Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTP / Web Panel via PHP Backend command infrastructure."
      }
    ]
  },
  "TF-036": {
    "name": "PureCrypter / PureLogs",
    "category": "Crypter",
    "items": [
      {
        "id": "EVID-036-01",
        "url": "images/TF-036_purecrypter_real_01.svg",
        "type": "Obfuscation Engine",
        "title": "PureCrypter Multi-Layer Obfuscation Architecture",
        "desc": "Forensic diagram detailing .NET runtime compression, dynamic decryption stubs, and AMSI memory patching."
      },
      {
        "id": "EVID-036-02",
        "url": "images/TF-036_purecrypter_real_02.svg",
        "type": "Disassembly Analysis",
        "title": "PureCrypter In-Memory Payload Decryption",
        "desc": "Disassembly tracking AES payload extraction from encrypted resources and injection into target processes."
      },
      {
        "id": "EVID-036-03",
        "url": "images/TF-036_purecrypter_arch.svg",
        "type": "Architecture Schematic",
        "title": "PureCrypter / PureLogs Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Telegram Bot API, Cloudflare Protected Endpoints command infrastructure."
      }
    ]
  },
  "TF-037": {
    "name": "PrivateLoader",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-037-01",
        "url": "images/TF-037_privateloader_real_01.jpg",
        "type": "Distribution Network",
        "title": "PrivateLoader Pay-Per-Install Distribution Topology",
        "desc": "ANY.RUN technical diagram detailing corporate endpoint compromise via Pay-Per-Install malware distribution channels."
      },
      {
        "id": "EVID-037-02",
        "url": "images/TF-037_privateloader_real_02.png",
        "type": "Payload Decryption",
        "title": "PrivateLoader Payload Decryption & Execution Trace",
        "desc": "Process memory capture showing secondary payload downloading, decryption, and execution validation."
      },
      {
        "id": "EVID-037-03",
        "url": "images/TF-037_privateloader_arch.svg",
        "type": "Architecture Schematic",
        "title": "PrivateLoader Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTP POST over Custom Encrypted Ports command infrastructure."
      }
    ]
  },
  "TF-038": {
    "name": "SystemBC",
    "category": "Botnet",
    "items": [
      {
        "id": "EVID-038-01",
        "url": "images/TF-038_systembc_real_01.svg",
        "type": "Proxy Engine",
        "title": "SystemBC SOCKS5 Tor Proxy Tunnel Architecture",
        "desc": "Technical visualization of SystemBC acting as a covert encrypted proxy for ransomware gang lateral movement."
      },
      {
        "id": "EVID-038-02",
        "url": "images/TF-038_systembc_real_02.svg",
        "type": "Network Telemetry",
        "title": "SystemBC Beacon Traffic & Command Protocol",
        "desc": "Packet capture analysis showing RC4-encrypted beaconing communicating with adversary command servers."
      },
      {
        "id": "EVID-038-03",
        "url": "images/TF-038_systembc_arch.svg",
        "type": "Architecture Schematic",
        "title": "SystemBC Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and SOCKS5 over Tor, Raw TCP Tunnels command infrastructure."
      }
    ]
  },
  "TF-039": {
    "name": "Mirai & Variants",
    "category": "Botnet",
    "items": [
      {
        "id": "EVID-039-01",
        "url": "images/TF-039_mirai_real_01.svg",
        "type": "Telnet Scanner",
        "title": "Mirai IoT Telnet Brute-Force Scanner Routine",
        "desc": "ANY.RUN analysis capture showing Mirai bot scanning IPv4 address space using hardcoded default credential dictionaries."
      },
      {
        "id": "EVID-039-02",
        "url": "images/TF-039_mirai_real_02.svg",
        "type": "DDoS Engine",
        "title": "Mirai SYN and UDP Flood Attack Engine",
        "desc": "Disassembly showing raw socket creation and automated transmission of high-volume DDoS packets."
      },
      {
        "id": "EVID-039-03",
        "url": "images/TF-039_mirai_arch.svg",
        "type": "Architecture Schematic",
        "title": "Mirai & Variants Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and IRC, Telnet Brute Force, Custom Binary C2 command infrastructure."
      }
    ]
  },
  "TF-040": {
    "name": "Mozi Botnet",
    "category": "Botnet",
    "items": [
      {
        "id": "EVID-040-01",
        "url": "images/TF-040_mozi_real_01.svg",
        "type": "P2P Network",
        "title": "Mozi Botnet DHT P2P Coordination Protocol",
        "desc": "Technical schematic illustrating BitTorrent DHT protocol abuse for distributed C2 command broadcasting."
      },
      {
        "id": "EVID-040-02",
        "url": "images/TF-040_mozi_real_02.svg",
        "type": "Exploit Module",
        "title": "Mozi IoT Zero-Day Exploit Propagation Module",
        "desc": "Disassembly tracking automated execution of UPnP and router vulnerability exploits against target subnets."
      },
      {
        "id": "EVID-040-03",
        "url": "images/TF-040_mozi_arch.svg",
        "type": "Architecture Schematic",
        "title": "Mozi Botnet Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and DHT (Distributed Hash Table) Network Protocol command infrastructure."
      }
    ]
  },
  "TF-041": {
    "name": "Meduza Stealer",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-041-01",
        "url": "images/TF-041_meduza_real_01.svg",
        "type": "Collector Dashboard",
        "title": "Meduza Stealer Web Administration Dashboard",
        "desc": "Operator web console aggregating infected victim logs, browser credential databases, and cold storage crypto keys."
      },
      {
        "id": "EVID-041-02",
        "url": "images/TF-041_meduza_real_02.svg",
        "type": "Network Telemetry",
        "title": "Meduza Stealer C2 Exfiltration Handshake",
        "desc": "Network telemetry trace showing encrypted ZIP archive exfiltration containing harvested endpoint data."
      },
      {
        "id": "EVID-041-03",
        "url": "images/TF-041_meduza_arch.svg",
        "type": "Architecture Schematic",
        "title": "Meduza Stealer Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTPS with Geoblocking Restrictions command infrastructure."
      }
    ]
  },
  "TF-042": {
    "name": "RisePro",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-042-01",
        "url": "images/TF-042_risepro_real_01.webp",
        "type": "Network Protocol",
        "title": "RisePro Stealer Network Communication & Encryption",
        "desc": "ANY.RUN forensic capture analyzing custom TCP protocol used by RisePro to transmit exfiltrated system data."
      },
      {
        "id": "EVID-042-02",
        "url": "images/TF-042_risepro_real_02.webp",
        "type": "Exfiltration Packet",
        "title": "RisePro Credential Archive Assembly & Dispatch",
        "desc": "Memory analysis showing compilation of password logs, system information, and browser artifacts into C2 packets."
      },
      {
        "id": "EVID-042-03",
        "url": "images/TF-042_risepro_arch.svg",
        "type": "Architecture Schematic",
        "title": "RisePro Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Encrypted TCP / Custom HTTP Webhook command infrastructure."
      }
    ]
  },
  "TF-043": {
    "name": "BunnyLoader",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-043-01",
        "url": "images/TF-043_bunnyloader_real_01.svg",
        "type": "Modular Core",
        "title": "BunnyLoader 3.0 Modular Control Interface",
        "desc": "C2 web panel displaying active loader instances, modular plugin downloads, and cryptocurrency clipper status."
      },
      {
        "id": "EVID-043-02",
        "url": "images/TF-043_bunnyloader_real_02.svg",
        "type": "Network Telemetry",
        "title": "BunnyLoader Tasking & Secondary Drop Telemetry",
        "desc": "Network capture analyzing endpoint registration and automated retrieval of secondary stealer payloads."
      },
      {
        "id": "EVID-043-03",
        "url": "images/TF-043_bunnyloader_arch.svg",
        "type": "Architecture Schematic",
        "title": "BunnyLoader Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Web Admin Panel with AES-256 command infrastructure."
      }
    ]
  },
  "TF-044": {
    "name": "Latrodectus",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-044-01",
        "url": "images/TF-044_latrodectus_real_01.png",
        "type": "Execution Pipeline",
        "title": "Latrodectus High-Stealth Loader Execution Pipeline",
        "desc": "ANY.RUN sandbox telemetry tracking multi-stage loader execution, WMI reconnaissance, and string hashing routines."
      },
      {
        "id": "EVID-044-02",
        "url": "images/TF-044_latrodectus_real_02.svg",
        "type": "C2 Telemetry",
        "title": "Latrodectus FNV-1a Hashing & C2 Beacon Protocol",
        "desc": "Network telemetry trace showing encrypted command-and-control handshakes and bot ID registration."
      },
      {
        "id": "EVID-044-03",
        "url": "images/TF-044_latrodectus_arch.svg",
        "type": "Architecture Schematic",
        "title": "Latrodectus Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTPS with Encrypted Custom Headers command infrastructure."
      }
    ]
  },
  "TF-045": {
    "name": "StrelaStealer",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-045-01",
        "url": "images/TF-045_strelastealer_real_01.svg",
        "type": "Mail Harvester",
        "title": "StrelaStealer Outlook & Thunderbird Credential Harvester",
        "desc": "Technical visualization of StrelaStealer parsing email client configuration files to extract IMAP/POP3 passwords."
      },
      {
        "id": "EVID-045-02",
        "url": "images/TF-045_strelastealer_real_02.svg",
        "type": "Network Telemetry",
        "title": "StrelaStealer C2 Exfiltration Traffic",
        "desc": "Packet inspection showing multipart HTTP POST transmission of extracted email credentials to adversary nodes."
      },
      {
        "id": "EVID-045-03",
        "url": "images/TF-045_strelastealer_arch.svg",
        "type": "Architecture Schematic",
        "title": "StrelaStealer Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Direct HTTP POST to Compromised Web Servers command infrastructure."
      }
    ]
  },
  "TF-046": {
    "name": "HijackLoader",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-046-01",
        "url": "images/TF-046_hijackloader_real_01.png",
        "type": "Chunk Extraction",
        "title": "HijackLoader (IDAT Loader) Image Chunk Extraction",
        "desc": "ANY.RUN technical capture showing extraction and decryption of hidden shellcode from PNG IDAT chunks."
      },
      {
        "id": "EVID-046-02",
        "url": "images/TF-046_hijackloader_real_02.svg",
        "type": "Process Hollowing",
        "title": "HijackLoader Process Injection into Clean Windows Binary",
        "desc": "Process monitor telemetry tracking hollowed process creation and memory section remapping."
      },
      {
        "id": "EVID-046-03",
        "url": "images/TF-046_hijackloader_arch.svg",
        "type": "Architecture Schematic",
        "title": "HijackLoader Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Encrypted Web Endpoints, Cloudflare Proxies command infrastructure."
      }
    ]
  },
  "TF-047": {
    "name": "RustBucket",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-047-01",
        "url": "images/TF-047_rustbucket_real_01.svg",
        "type": "macOS Lure",
        "title": "RustBucket macOS PDF Viewer Lure & Execution",
        "desc": "Forensic trace analyzing AppleScript invocation and fake PDF reader application dropping Mach-O binaries."
      },
      {
        "id": "EVID-047-02",
        "url": "images/TF-047_rustbucket_real_02.svg",
        "type": "Network Telemetry",
        "title": "RustBucket Multi-Stage C2 Domain Resolution",
        "desc": "Network capture tracking second-stage Mach-O payload retrieval from adversary-controlled infrastructure."
      },
      {
        "id": "EVID-047-03",
        "url": "images/TF-047_rustbucket_arch.svg",
        "type": "Architecture Schematic",
        "title": "RustBucket Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and HTTPS with Encrypted Custom Handshake command infrastructure."
      }
    ]
  },
  "TF-048": {
    "name": "Atomic Stealer (AMOS)",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-048-01",
        "url": "images/TF-048_atomic_real_01.png",
        "type": "ClickFix Lure",
        "title": "Atomic Stealer (AMOS) macOS ClickFix Delivery Lure",
        "desc": "ANY.RUN sandbox capture showing social engineering prompt tricking macOS users into executing malicious terminal commands."
      },
      {
        "id": "EVID-048-02",
        "url": "images/TF-048_atomic_real_02.png",
        "type": "C2 Exfiltration",
        "title": "Atomic Stealer Telegram & HTTP Exfiltration Traffic",
        "desc": "Network capture tracking exfiltration of Keychain databases, browser cookies, and hardware specs to adversary C2."
      },
      {
        "id": "EVID-048-03",
        "url": "images/TF-048_atomic_arch.svg",
        "type": "Architecture Schematic",
        "title": "Atomic Stealer (AMOS) Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Telegram Bot API, Encrypted Web Servers command infrastructure."
      }
    ]
  },
  "TF-049": {
    "name": "ShadowPad",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-049-01",
        "url": "images/TF-049_shadowpad_real_01.svg",
        "type": "Plugin Engine",
        "title": "ShadowPad Modular Backdoor Architecture",
        "desc": "Technical visualization of ShadowPad virtual file system and dynamic DLL plugin dispatch table."
      },
      {
        "id": "EVID-049-02",
        "url": "images/TF-049_shadowpad_real_02.svg",
        "type": "Disassembly Analysis",
        "title": "ShadowPad Root Loader & DLL Sideloading Routine",
        "desc": "Disassembly showing legitimate signed host binary abused for DLL search-order hijacking."
      },
      {
        "id": "EVID-049-03",
        "url": "images/TF-049_shadowpad_arch.svg",
        "type": "Architecture Schematic",
        "title": "ShadowPad Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and DNS, Custom Binary Protocols, Proxy Nodes command infrastructure."
      }
    ]
  },
  "TF-050": {
    "name": "PlugX / Korplug",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-050-01",
        "url": "images/TF-050_plugx_real_01.png",
        "type": "Builder UI",
        "title": "PlugX (Korplug) Payload Builder & Configurator",
        "desc": "Operator configurator GUI showing encryption key generation, C2 domain insertion, and service installation options."
      },
      {
        "id": "EVID-050-02",
        "url": "images/TF-050_plugx_real_02.svg",
        "type": "DLL Sideloading",
        "title": "PlugX DLL Search-Order Hijacking Routine",
        "desc": "Forensic diagram tracking legitimate executable loading malicious proxy DLL and decrypting .dat payload."
      },
      {
        "id": "EVID-050-03",
        "url": "images/TF-050_plugx_arch.svg",
        "type": "Architecture Schematic",
        "title": "PlugX / Korplug Technical Infection Chain & Architecture",
        "desc": "Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and Custom P2P, DNS Tunneling, Worm-like USB Spreading command infrastructure."
      }
    ]
  }
};

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { FORENSIC_MEDIA_MANIFEST };
}
