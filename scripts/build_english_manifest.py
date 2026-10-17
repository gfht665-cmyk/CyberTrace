#!/usr/bin/env python3
"""
CyberTrace 100% Pure Technical English Forensic Media Manifest Builder
Maps all 50 cataloged threats (TF-001 through TF-050) to 2-5 local forensic assets
Zero Arabic characters, 100% pure technical CTI English descriptions.
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
JS_DIR = os.path.join(BASE_DIR, 'js')
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

# Comprehensive mapping for all 50 threats
MANIFEST_DATA = {
  "TF-001": {
    "name": "AsyncRAT",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-001-01",
        "url": "images/asyncrat_01_builder.png",
        "type": "Builder UI",
        "title": "AsyncRAT Client Payload Builder & Configurator",
        "desc": "Payload configurator GUI displaying TLS X.509 certificate generation, keylogger toggles, and persistence hooks."
      },
      {
        "id": "EVID-001-02",
        "url": "images/asyncrat_02_console.svg",
        "type": "C2 Panel",
        "title": "AsyncRAT Server Management & Telemetry Console",
        "desc": "Operator telemetry console monitoring connected victim nodes, IP addresses, and Cloudflare tunnel channels."
      },
      {
        "id": "EVID-001-03",
        "url": "images/venomrat_01_builder.png",
        "type": "Derivative Builder",
        "title": "VenomRAT Forked Client Builder Interface",
        "desc": "Derivative variant integrating HVNC desktop surveillance and cryptocurrency clipper memory hooks."
      },
      {
        "id": "EVID-001-04",
        "url": "images/xenorat_01_builder.png",
        "type": "Derivative Builder",
        "title": "XenoRat C# Payload Builder with SOCKS5 Proxying",
        "desc": "Advanced C# builder with reverse proxy tunneling, dual-layer AES encryption, and evasion stubs."
      }
    ]
  },
  "TF-002": {
    "name": "Dolphin X",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-002-01",
        "url": "images/dolphinx_01_builder.png",
        "type": "Builder UI",
        "title": "Dolphin X AI Stealer Builder Interface",
        "desc": "Builder interface setting target heuristics, browser extension targeting, and polymorphic stub compilation."
      },
      {
        "id": "EVID-002-02",
        "url": "images/dolphinx_02_mutation.png",
        "type": "Execution Artifact",
        "title": "Polymorphic Stub Mutation & Anti-Analysis Routine",
        "desc": "Visualizing automated code mutation layers and junk instruction interleaving to bypass heuristic EDR signatures."
      },
      {
        "id": "EVID-002-03",
        "url": "images/dolphinx_03_telegram.png",
        "type": "C2 Channel",
        "title": "Telegram Bot Exfiltration & Notification Feed",
        "desc": "Real-time bot logs broadcasting compromised host specs, geolocation data, and compressed credential archives."
      },
      {
        "id": "EVID-002-04",
        "url": "images/dolphinx_04_wallet.png",
        "type": "Memory Extraction",
        "title": "Crypto Wallet Heuristic Extraction Pipeline",
        "desc": "Heuristic memory scanner searching for MetaMask, Phantom, Exodus, and cold storage seed phrases."
      },
      {
        "id": "EVID-002-05",
        "url": "images/dolphinx_05_dashboard.png",
        "type": "C2 Panel",
        "title": "Dolphin X Operator Control Dashboard",
        "desc": "Centralized web telemetry panel aggregating infected endpoint counts, active bot tokens, and exfiltrated logs."
      }
    ]
  },
  "TF-003": {
    "name": "Lumma Stealer",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-003-01",
        "url": "images/lumma_01_dashboard.svg",
        "type": "C2 Panel",
        "title": "LummaC2 Fast-Flux Operator Web Dashboard",
        "desc": "Web-based C2 panel displaying live campaign telemetry, active bots, and automated Telegram alerts."
      },
      {
        "id": "EVID-003-02",
        "url": "images/lumma_02_logs.svg",
        "type": "Memory Flow Diagram",
        "title": "Lumma Stealer Control Flow Flattening & String Obfuscation",
        "desc": "Control flow flattening graph and XOR string table decoding routines analyzed during binary reversing."
      }
    ]
  },
  "TF-004": {
    "name": "RedLine Stealer",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-004-01",
        "url": "images/redline_01_panel.svg",
        "type": "C2 Panel",
        "title": "RedLine Web Panel & Log Ingestion Console",
        "desc": "Operator web panel indexing harvested credential archives, system hardware tokens, and browser profiles."
      },
      {
        "id": "EVID-004-02",
        "url": "images/redline_02_logs.svg",
        "type": "Memory Flow Diagram",
        "title": "WCF Binary Framing & SOAP Network Communication Flow",
        "desc": "Dissection of Net.Tcp communication stream transferring XML-serialized browser databases."
      }
    ]
  },
  "TF-005": {
    "name": "Vidar Stealer",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-005-01",
        "url": "images/vidar_01_deaddrop.svg",
        "type": "C2 Panel",
        "title": "Vidar Dead-Drop Resolver Architecture",
        "desc": "Resolution pipeline scraping covert C2 IP addresses from public social media profiles (Steam, Mastodon, Telegram)."
      },
      {
        "id": "EVID-005-02",
        "url": "images/vidar_02_network.svg",
        "type": "Memory Flow Diagram",
        "title": "In-Memory Dependency Loading & Self-Deletion",
        "desc": "Reflective dependency injection and automated self-deletion via cmd.exe cleanup routines."
      }
    ]
  },
  "TF-006": {
    "name": "Agent Tesla",
    "category": "Spyware",
    "items": [
      {
        "id": "EVID-006-01",
        "url": "images/agenttesla_01_smtp.svg",
        "type": "Memory Flow Diagram",
        "title": "Multi-Channel Exfiltration Pipeline (SMTP / FTP / Webhooks)",
        "desc": "Data transmission pipeline dispatching harvested keystrokes and screenshots across encrypted protocols."
      },
      {
        "id": "EVID-006-02",
        "url": "images/agenttesla_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: Keylogger Hook & Mail Dispatch",
        "desc": "Reverse-engineered SetWindowsHookExW routine and SMTP background sender thread."
      }
    ]
  },
  "TF-007": {
    "name": "Remcos RAT",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-007-01",
        "url": "images/remcos_01_builder.png",
        "type": "Builder UI",
        "title": "Remcos Professional Client Builder & Stub Generator",
        "desc": "Configuration interface setting up dynamic DNS listeners, persistence keys, and webcam monitoring."
      },
      {
        "id": "EVID-007-02",
        "url": "images/remcos_01_console.svg",
        "type": "C2 Panel",
        "title": "Remcos Remote Management & SOCKS5 Proxy Console",
        "desc": "Command center managing live host sessions, audio wiretapping feeds, and internal pivot tunnels."
      },
      {
        "id": "EVID-007-03",
        "url": "images/remcos_02_builder.svg",
        "type": "Memory Flow Diagram",
        "title": "Remcos RC4 In-Memory Decryption & UAC Bypass Chain",
        "desc": "Memory execution flow depicting payload unpacking and mock-folder UAC elevation bypass."
      }
    ]
  },
  "TF-008": {
    "name": "XWorm",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-008-01",
        "url": "images/xworm_01_builder.png",
        "type": "Builder UI",
        "title": "XWorm Hybrid RAT & Clipper Builder Interface",
        "desc": "Payload builder configuring AES encryption keys, port listeners, and USB spreading stubs."
      },
      {
        "id": "EVID-008-02",
        "url": "images/xworm_02_clipper.svg",
        "type": "Memory Flow Diagram",
        "title": "XWorm Crypto Clipper Memory Interception Flow",
        "desc": "Clipboard monitoring routine hijacking cryptocurrency addresses during paste transactions."
      },
      {
        "id": "EVID-008-03",
        "url": "images/craxsrat_01_builder.png",
        "type": "Derivative Builder",
        "title": "CraxsRAT v7.4 Android Hybrid Builder",
        "desc": "Mobile intrusion builder deployed alongside XWorm campaigns for 2FA SMS interception."
      },
      {
        "id": "EVID-008-04",
        "url": "images/craxsrat_02_builder.png",
        "type": "C2 Panel",
        "title": "CraxsRAT Mobile Command & Surveillance Center",
        "desc": "Mobile operator dashboard managing connected phone bots, live audio, and screen streaming."
      }
    ]
  },
  "TF-009": {
    "name": "DarkGate",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-009-01",
        "url": "images/darkgate_01_lure.png",
        "type": "Execution Artifact",
        "title": "DarkGate Initial Access Lure Document & VBS Dropper",
        "desc": "Malicious PDF lure impersonating financial statements initiating multi-stage AutoIt payload drops."
      },
      {
        "id": "EVID-009-02",
        "url": "images/darkgate_02_ahk.png",
        "type": "Execution Artifact",
        "title": "Obfuscated AutoIt Script Decompilation",
        "desc": "Deobfuscated AutoIt script loading shellcode directly into memory without touching disk."
      },
      {
        "id": "EVID-009-03",
        "url": "images/darkgate_03_config.png",
        "type": "C2 Panel",
        "title": "DarkGate Operator Management Console",
        "desc": "C2 administration panel displaying active bots, AV evasion toggles, and HVNC modules."
      },
      {
        "id": "EVID-009-04",
        "url": "images/darkgate_04_traffic.jpeg",
        "type": "Execution Artifact",
        "title": "DarkGate Process Injection & Memory Telemetry",
        "desc": "Sandbox capture tracing process hollowing into legitimate Windows executables."
      }
    ]
  },
  "TF-010": {
    "name": "Rhadamanthys",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-010-01",
        "url": "images/rhadamanthys_01_builder.png",
        "type": "Builder UI",
        "title": "Rhadamanthys Stealer Builder & Custom Compiler",
        "desc": "Custom compilation GUI configuring polymorphic encryption keys, bot IDs, and C2 fallbacks."
      },
      {
        "id": "EVID-010-02",
        "url": "images/rhadamanthys_01_vm.svg",
        "type": "Memory Flow Diagram",
        "title": "Custom Bytecode Virtual Machine (VM) Architecture",
        "desc": "Reverse engineering diagram illustrating custom instruction set interpreter used to bypass static analyzers."
      },
      {
        "id": "EVID-010-03",
        "url": "images/rhadamanthys_02_stealer.svg",
        "type": "C2 Panel",
        "title": "Rhadamanthys Stealer Operator Logs & Telemetry",
        "desc": "Dashboard aggregating decrypted browser credentials, cryptocurrency extensions, and VPN tokens."
      },
      {
        "id": "EVID-010-04",
        "url": "images/rhadamanthys_03_pipe.svg",
        "type": "Execution Artifact",
        "title": "Named Pipe IPC Architecture & Core Injection",
        "desc": "Inter-process communication scheme staging modular stealer DLLs into suspended system processes."
      }
    ]
  },
  "TF-011": {
    "name": "Stealc",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-011-01",
        "url": "images/stealc_01_admin.svg",
        "type": "C2 Panel",
        "title": "Stealc InfoStealer Operator Admin Console",
        "desc": "Web-based management console tracking active infostealer bots and automated credential categorization."
      },
      {
        "id": "EVID-011-02",
        "url": "images/stealc_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: SQLite Chrome Harvester",
        "desc": "Decompiled C routines showing sqlite3_open_v2 calls on Chrome Login Data and CryptUnprotectData DPAPI decryption."
      },
      {
        "id": "EVID-011-03",
        "url": "images/stealc_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark C2 HTTP POST Stream Dissection",
        "desc": "Packet inspection of Stealc bot registration and encrypted credential vault exfiltration stream."
      }
    ]
  },
  "TF-012": {
    "name": "Havoc C2",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-012-01",
        "url": "images/havoc_01_client.svg",
        "type": "C2 Panel",
        "title": "Havoc C2 Demon Agent Operator Console",
        "desc": "Cross-platform C2 interface managing active Demon agents, process injection jobs, and listener profiles."
      },
      {
        "id": "EVID-012-02",
        "url": "images/havoc_02_payload.svg",
        "type": "Memory Flow Diagram",
        "title": "Demon Agent Sleep Obfuscation & Indirect Syscalls",
        "desc": "Diagram of Demon agent in-memory execution, Ekko sleep masking, and indirect syscall invocation."
      }
    ]
  },
  "TF-013": {
    "name": "Sliver C2",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-013-01",
        "url": "images/sliver_01_config.png",
        "type": "Builder UI",
        "title": "Sliver C2 Implant Configuration & Armory Stager",
        "desc": "Implant generation terminal configuring mTLS, WireGuard, and DNS canary beacons."
      },
      {
        "id": "EVID-013-02",
        "url": "images/sliver_02_injection.svg",
        "type": "Memory Flow Diagram",
        "title": "Sliver Process Injection & Shellcode Execution",
        "desc": "Technical schematic tracing reflective DLL loading and process hollowing routines."
      },
      {
        "id": "EVID-013-03",
        "url": "images/sliver_03_alerts.svg",
        "type": "Execution Artifact",
        "title": "EDR Alert Telemetry & Behavioral Signatures",
        "desc": "Microsoft Defender for Endpoint alert matrix mapping Sliver in-memory API telemetry."
      }
    ]
  },
  "TF-014": {
    "name": "Mythic C2",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-014-01",
        "url": "images/mythic_01_dashboard.svg",
        "type": "C2 Panel",
        "title": "Mythic C2 Web Management Console & Agent Radar",
        "desc": "Enterprise web dashboard orchestrating multi-agent red team campaigns and task queues."
      },
      {
        "id": "EVID-014-02",
        "url": "images/mythic_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: Mythic Tasking Dispatcher",
        "desc": "Reversed agent routines dispatching execute-assembly jobs and managing encrypted HMAC payloads."
      },
      {
        "id": "EVID-014-03",
        "url": "images/mythic_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark WebSocket C2 Stream Dissection",
        "desc": "Dissection of persistent bidirectional WebSocket communication carrying encrypted task envelopes."
      }
    ]
  },
  "TF-015": {
    "name": "QuasarRAT",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-015-01",
        "url": "images/quasarrat_01_builder.png",
        "type": "Builder UI",
        "title": "QuasarRAT Client Builder Interface",
        "desc": "Configuration interface setting up network socket encryption, autostart registry keys, and installation paths."
      },
      {
        "id": "EVID-015-02",
        "url": "images/quasarrat_01_builder.svg",
        "type": "Memory Flow Diagram",
        "title": "Quasar Network Architecture & Serialized Sockets",
        "desc": "Protocol schema illustrating non-blocking asynchronous socket serialization and TLS handshake."
      }
    ]
  },
  "TF-016": {
    "name": "Warzone RAT",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-016-01",
        "url": "images/warzone_01_builder.png",
        "type": "Builder UI",
        "title": "Warzone RAT (Ave Maria) Client Builder",
        "desc": "Builder window configuring UAC auto-elevation bypasses, reverse SOCKS5 proxies, and stealth installation."
      },
      {
        "id": "EVID-016-02",
        "url": "images/warzone_01_console.svg",
        "type": "C2 Panel",
        "title": "Warzone RAT Server Command & Surveillance Console",
        "desc": "Operator console tracking active sessions, real-time desktop video streaming, and credential dumping."
      }
    ]
  },
  "TF-017": {
    "name": "GuLoader",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-017-01",
        "url": "images/guloader_01_shellcode.svg",
        "type": "Memory Flow Diagram",
        "title": "GuLoader Anti-Analysis Vectored Exception Handling (VEH)",
        "desc": "Architectural breakdown of VEH hijacking and hardware breakpoint detection routines."
      },
      {
        "id": "EVID-017-02",
        "url": "images/guloader_02_veh.svg",
        "type": "Memory Flow Diagram",
        "title": "GuLoader Multi-Layer Shellcode Decryption & Hollower",
        "desc": "Staged memory layout illustrating RC4 key extraction and remote process hollowing into clean binaries."
      }
    ]
  },
  "TF-018": {
    "name": "Pikabot",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-018-01",
        "url": "images/pikabot_01_loader.svg",
        "type": "Memory Flow Diagram",
        "title": "Pikabot Modular Core Architecture & Evasion Chain",
        "desc": "Structural diagram illustrating stack-string assembly, anti-hooking probes, and second-stage payload delivery."
      },
      {
        "id": "EVID-018-02",
        "url": "images/pikabot_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: Pikabot Process Hollowing",
        "desc": "Reverse engineered VirtualAllocEx and WriteProcessMemory injection routine into searchindexer.exe."
      },
      {
        "id": "EVID-018-03",
        "url": "images/pikabot_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Pikabot C2 Heartbeat Packet Stream",
        "desc": "Dissection of TLS 1.3 encrypted HTTP POST requests transferring victim HWID and system telemetry."
      }
    ]
  },
  "TF-019": {
    "name": "Qakbot",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-019-01",
        "url": "images/qakbot_01_banking.svg",
        "type": "Memory Flow Diagram",
        "title": "Qakbot Multi-Module Architecture & Banking Injections",
        "desc": "Detailed schema illustrating modular DLL architecture, thread hijacking, and credential scraping loops."
      },
      {
        "id": "EVID-019-02",
        "url": "images/qakbot_02_hollowing.svg",
        "type": "Memory Flow Diagram",
        "title": "Qakbot Process Replacement & In-Memory Unpacking",
        "desc": "Process injection workflow mapping hollowed wermgr.exe memory execution."
      }
    ]
  },
  "TF-020": {
    "name": "Emotet",
    "category": "Botnet",
    "items": [
      {
        "id": "EVID-020-01",
        "url": "images/emotet_01_botnet.svg",
        "type": "Memory Flow Diagram",
        "title": "Emotet Modular Botnet Architecture & C2 Mesh",
        "desc": "Topological map of Emotet Tier-1 and Tier-2 command controllers with automated spamming engines."
      },
      {
        "id": "EVID-020-02",
        "url": "images/emotet_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: Emotet Anti-Sandbox State Machine",
        "desc": "Timing probe routines comparing GetTickCount deltas to detect accelerated virtual execution."
      },
      {
        "id": "EVID-020-03",
        "url": "images/emotet_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Emotet ECDH Handshake & Payload Stream",
        "desc": "Network dissection tracing ECDH key agreement packets and encrypted DLL download streams."
      }
    ]
  },
  "TF-021": {
    "name": "LockBit",
    "category": "Ransomware",
    "items": [
      {
        "id": "EVID-021-01",
        "url": "images/lockbit_01_builder.svg",
        "type": "Builder UI",
        "title": "LockBit 3.0 Black Builder Configuration Console",
        "desc": "Leaked builder GUI configuring RSA-4096 / AES-256 keys, thread worker limits, and shadow copy wiping."
      },
      {
        "id": "EVID-021-02",
        "url": "images/lockbit_02_encryption.svg",
        "type": "Memory Flow Diagram",
        "title": "LockBit High-Speed Intermittent Encryption Flow",
        "desc": "Algorithmic flowchart detailing partial encryption routines designed to evade ransomware EDR canaries."
      },
      {
        "id": "EVID-021-03",
        "url": "images/lockbit_02_wallpaper.svg",
        "type": "Execution Artifact",
        "title": "LockBit 3.0 Ransom Desktop Wallpaper & Note Drop",
        "desc": "Forensic artifact showing the characteristic LockBit desktop wallpaper replacement and instruction note."
      }
    ]
  },
  "TF-022": {
    "name": "BlackCat",
    "category": "Ransomware",
    "items": [
      {
        "id": "EVID-022-01",
        "url": "images/blackcat_01_flags.png",
        "type": "Execution Artifact",
        "title": "BlackCat (ALPHV) Rust CLI Execution Parameters",
        "desc": "Terminal execution parameters including token-based authentication and lateral domain propagation flags."
      },
      {
        "id": "EVID-022-02",
        "url": "images/blackcat_02_note.svg",
        "type": "Execution Artifact",
        "title": "BlackCat Ransom Note & Recovery Token Structure",
        "desc": "Artifact showing ransom note structure, Tor negotiation portal address, and cryptographic victim token."
      },
      {
        "id": "EVID-022-03",
        "url": "images/blackcat_03_tor.svg",
        "type": "C2 Panel",
        "title": "BlackCat Dark Web Tor Negotiation & Leak Portal",
        "desc": "Forensic view of ALPHV Tor portal managing live ransom negotiations and double-extortion leak data."
      }
    ]
  },
  "TF-023": {
    "name": "Akira",
    "category": "Ransomware",
    "items": [
      {
        "id": "EVID-023-01",
        "url": "images/akira_01_ransomware.svg",
        "type": "Memory Flow Diagram",
        "title": "Akira Ransomware Multi-Threaded ChaCha20 Pipeline",
        "desc": "Structural diagram illustrating recursive folder traversal, ChaCha20 encryption loops, and file renaming."
      },
      {
        "id": "EVID-023-02",
        "url": "images/akira_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: ChaCha20 File Encryptor",
        "desc": "Decompiled C code demonstrating ChaCha20 stream generation, RSA master key encryption, and shadow copy wiping."
      },
      {
        "id": "EVID-023-03",
        "url": "images/akira_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Akira Tor Negotiation Network Stream",
        "desc": "Network packet dissection tracing outbound SSL/TLS handshake with Akira leak portal infrastructure."
      }
    ]
  },
  "TF-024": {
    "name": "Medusa",
    "category": "Ransomware",
    "items": [
      {
        "id": "EVID-024-01",
        "url": "images/medusa_01_extortion.svg",
        "type": "C2 Panel",
        "title": "Medusa Blog & Double-Extortion Portal",
        "desc": "Forensic view of Medusa public leak site hosting corporate victim countdown timers and stolen archives."
      },
      {
        "id": "EVID-024-02",
        "url": "images/medusa_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: Medusa Mutex & Drive Traversal",
        "desc": "Reverse engineered mutex validation routine and multi-threaded drive traversal loop."
      },
      {
        "id": "EVID-024-03",
        "url": "images/medusa_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Medusa Registration Packet Stream",
        "desc": "Packet inspection of Medusa ransomware bot reporting volume key tokens to C2 gateway."
      }
    ]
  },
  "TF-025": {
    "name": "Phobos / 8Base",
    "category": "Ransomware",
    "items": [
      {
        "id": "EVID-025-01",
        "url": "images/phobos_01_decryptor.svg",
        "type": "Execution Artifact",
        "title": "Phobos / 8Base Ransomware Execution & File Renaming",
        "desc": "Forensic view showing appended victim ID formatting and dropping of info.hta instructions."
      },
      {
        "id": "EVID-025-02",
        "url": "images/phobos_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: Run Key Persistence & Encryption",
        "desc": "Decompiled routines illustrating registry persistence creation and AES-CBC file block processing."
      },
      {
        "id": "EVID-025-03",
        "url": "images/phobos_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Phobos Bot Verification Stream",
        "desc": "Dissection of HTTP GET request verifying infected victim ID against C2 gateway."
      }
    ]
  },
  "TF-026": {
    "name": "Formbook",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-026-01",
        "url": "images/formbook_01_hooking.svg",
        "type": "Memory Flow Diagram",
        "title": "Formbook / XLoader User-Mode API Hooking Architecture",
        "desc": "Dissection of user-mode ntdll unhooking and memory detour patching across browser processes."
      },
      {
        "id": "EVID-026-02",
        "url": "images/formbook_02_injection.svg",
        "type": "Memory Flow Diagram",
        "title": "Formbook Multi-Stage Process Hollowing & C2 Decoy Web",
        "desc": "Complex execution flow diagram showing decoys contacting multiple benign domains to mask real C2 IPs."
      }
    ]
  },
  "TF-027": {
    "name": "Bumblebee",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-027-01",
        "url": "images/bumblebee_01_stager.svg",
        "type": "Memory Flow Diagram",
        "title": "Bumblebee Modular Stager & Process Injection Chain",
        "desc": "Injection flow tracing VBox/VMware detection before reflective DLL staging into explorer.exe."
      },
      {
        "id": "EVID-027-02",
        "url": "images/bumblebee_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: Bumblebee Anti-Analysis & WebSocket",
        "desc": "Reversed CPUID hypervisor validation routine and initialization of secure WebSocket C2 communication."
      },
      {
        "id": "EVID-027-03",
        "url": "images/bumblebee_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Bumblebee WebSocket Binary Stream",
        "desc": "Network stream capture showing WebSocket handshake and transmission of reflective DLL payload."
      }
    ]
  },
  "TF-028": {
    "name": "IcedID",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-028-01",
        "url": "images/icedid_01_stego.svg",
        "type": "Memory Flow Diagram",
        "title": "IcedID (BokBot) Steganographic Payload Extraction",
        "desc": "Workflow illustrating hidden encrypted payload extraction from PNG pixel bytes and in-memory execution."
      },
      {
        "id": "EVID-028-02",
        "url": "images/icedid_02_stego.svg",
        "type": "Memory Flow Diagram",
        "title": "IcedID In-Memory Hooking & Banking Proxy Architecture",
        "desc": "Local proxy redirection architecture hooking browser sockets to intercept corporate banking credentials."
      }
    ]
  },
  "TF-029": {
    "name": "DanaBot",
    "category": "Banking Trojan",
    "items": [
      {
        "id": "EVID-029-01",
        "url": "images/danabot_01_panel.svg",
        "type": "C2 Panel",
        "title": "DanaBot Modular Banking Trojan Administration Panel",
        "desc": "Command panel showing active bot network clusters, web-injection scripts, and Tor proxy bridges."
      },
      {
        "id": "EVID-029-02",
        "url": "images/danabot_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: DanaBot Web-Injection Hook",
        "desc": "Reverse engineered Man-in-the-Browser socket hooking and AES-GCM credential encryption routines."
      }
    ]
  },
  "TF-030": {
    "name": "SmokeLoader",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-030-01",
        "url": "images/smokeloader_01_plugins.svg",
        "type": "Memory Flow Diagram",
        "title": "SmokeLoader Modular Plugin System & C2 Beacon Loop",
        "desc": "Architecture diagram illustrating encrypted plugin download mechanisms and multi-layered anti-hooking probes."
      },
      {
        "id": "EVID-030-02",
        "url": "images/smokeloader_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: PEB Debugger Probe & Syscalls",
        "desc": "Reversed PEB.BeingDebugged inspection and direct ZwQueryInformationProcess syscall routines."
      },
      {
        "id": "EVID-030-03",
        "url": "images/smokeloader_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark SmokeLoader Gate POST Stream",
        "desc": "Dissection of encrypted HTTP POST request delivering machine GUID and downloading plugin payloads."
      }
    ]
  },
  "TF-031": {
    "name": "Cobalt Strike",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-031-01",
        "url": "images/cobaltstrike_01_listeners.png",
        "type": "Builder UI",
        "title": "Cobalt Strike Listener Management & Payload Generator",
        "desc": "Listener configurator interface showing HTTP/HTTPS beacon staging and port configuration."
      },
      {
        "id": "EVID-031-02",
        "url": "images/cobaltstrike_02_beacon.svg",
        "type": "C2 Panel",
        "title": "Cobalt Strike Beacon Console & File Browser",
        "desc": "Live interactive operator session executing remote triage commands, token theft, and process queries."
      },
      {
        "id": "EVID-031-03",
        "url": "images/cobaltstrike_03_aggressor.svg",
        "type": "Execution Artifact",
        "title": "Aggressor Scripting Engine & Script Loader",
        "desc": "Aggressor script manager loading custom CNA offensive modules and automated lateral movement workflows."
      }
    ]
  },
  "TF-032": {
    "name": "Brute Ratel C4",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-032-01",
        "url": "images/bruteratel_01_badger.svg",
        "type": "C2 Panel",
        "title": "Brute Ratel C4 Dark Mode Operator Commander Console",
        "desc": "Enterprise command interface showing active Badger agents, pivot channels, and payload generator."
      },
      {
        "id": "EVID-032-02",
        "url": "images/brute_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: Badger Indirect Syscall Stubs",
        "desc": "Disassembly showing manual SSN invocation and Ekko sleep memory encryption routines."
      },
      {
        "id": "EVID-032-03",
        "url": "images/brute_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Malleable C2 Telemetry Dissection",
        "desc": "Packet inspection of encrypted Badger heartbeat telemetry over custom TLS profiles."
      }
    ]
  },
  "TF-033": {
    "name": "NetSupport RAT",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-033-01",
        "url": "images/netsupport_01_gateway.svg",
        "type": "C2 Panel",
        "title": "NetSupport Manager Gateway Infrastructure",
        "desc": "Network schema illustrating weaponized NetSupport client instances connecting through gateway servers."
      },
      {
        "id": "EVID-033-02",
        "url": "images/netsupport_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: NetSupport Client32.ini Hook",
        "desc": "Reversed client32.ini parser and hidden window thread initialization routines."
      }
    ]
  },
  "TF-034": {
    "name": "NjRAT",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-034-01",
        "url": "images/njrat_01_builder.png",
        "type": "Builder UI",
        "title": "NjRAT (Bladabindi) .NET Client Payload Builder",
        "desc": "Classic .NET payload builder configuring direct TCP listeners, persistence keys, and mutex names."
      },
      {
        "id": "EVID-034-02",
        "url": "images/njrat_01_goldengui.svg",
        "type": "C2 Panel",
        "title": "NjRAT Golden Edition Operator Management Console",
        "desc": "Administration console showing connected victim nodes, IP geolocation flags, and active keystroke streams."
      },
      {
        "id": "EVID-034-03",
        "url": "images/njrat_02_camspy.svg",
        "type": "C2 Panel",
        "title": "NjRAT Remote Desktop & Webcam Surveillance Module",
        "desc": "Interactive window capturing live desktop display and webcam video streams in real time."
      }
    ]
  },
  "TF-035": {
    "name": "DCRat",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-035-01",
        "url": "images/dcrat_01_builder.png",
        "type": "Builder UI",
        "title": "DCRat (DarkCrystal) Payload Configurator GUI",
        "desc": "Builder interface setting up modular plugins, obfuscation profiles, and reverse connection endpoints."
      },
      {
        "id": "EVID-035-02",
        "url": "images/dcrat_01_studio.svg",
        "type": "C2 Panel",
        "title": "DarkCrystal Studio Operator Administration Console",
        "desc": "C2 dashboard monitoring connected bot clusters, active plugins, and automated log parsing."
      }
    ]
  },
  "TF-036": {
    "name": "PureCrypter",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-036-01",
        "url": "images/purecrypter_01_obfuscation.svg",
        "type": "Memory Flow Diagram",
        "title": "PureCrypter In-Memory Injection & Encryption Flow",
        "desc": "Flowchart detailing multi-layered payload decompression, AMSI bypass, and process hollowing."
      },
      {
        "id": "EVID-036-02",
        "url": "images/purecrypter_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: PureCrypter AMSI Bypass & Unpacker",
        "desc": "Reversed AmsiScanBuffer patch routine and in-memory GZip payload decompression."
      }
    ]
  },
  "TF-037": {
    "name": "PrivateLoader",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-037-01",
        "url": "images/privateloader_01_ppi.svg",
        "type": "Memory Flow Diagram",
        "title": "PrivateLoader Pay-Per-Install Distribution Architecture",
        "desc": "Architectural overview tracing PPI dropper clusters, GeoIP filtering, and second-stage payload delivery."
      },
      {
        "id": "EVID-037-02",
        "url": "images/privateloader_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: GeoIP Check & Multi-Downloader",
        "desc": "Decompiled routines querying IP geolocation and dropping multiple stealer and ransomware payloads."
      },
      {
        "id": "EVID-037-03",
        "url": "images/privateloader_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark PrivateLoader Task Retrieval Stream",
        "desc": "Network stream capture showing HTTP GET task query and downloading of second-stage binaries."
      }
    ]
  },
  "TF-038": {
    "name": "SystemBC",
    "category": "Botnet",
    "items": [
      {
        "id": "EVID-038-01",
        "url": "images/systembc_01_torproxy.svg",
        "type": "Memory Flow Diagram",
        "title": "SystemBC SOCKS5 Reverse Proxy & Tor Gateway Architecture",
        "desc": "Network topology showing SystemBC bot routing attacker traffic through corporate networks via SOCKS5 proxies."
      },
      {
        "id": "EVID-038-02",
        "url": "images/systembc_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: SOCKS5 Handshake & XOR Loop",
        "desc": "Disassembly of raw SOCKS5 socket initialization and custom stream encryption routines."
      },
      {
        "id": "EVID-038-03",
        "url": "images/systembc_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark SystemBC SOCKS5 Tunnel Dissection",
        "desc": "Dissection of internal SMB lateral movement traffic proxied through infected SystemBC nodes."
      }
    ]
  },
  "TF-039": {
    "name": "Mirai & Variants",
    "category": "Botnet",
    "items": [
      {
        "id": "EVID-039-01",
        "url": "images/mirai_01_telnet.svg",
        "type": "Memory Flow Diagram",
        "title": "Mirai Telnet Scanner & Distributed DDoS Engine",
        "desc": "Execution model detailing default credential dictionary brute-forcing and synchronized UDP/SYN flood routines."
      },
      {
        "id": "EVID-039-02",
        "url": "images/mirai_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "Ghidra Decompiler: Mirai Telnet Scanner Loop (Linux ELF)",
        "desc": "Decompiled C code illustrating raw socket creation and credential brute-forcing targeting port 23."
      },
      {
        "id": "EVID-039-03",
        "url": "images/mirai_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Telnet Brute-Force & UDP Flood Stream",
        "desc": "Packet stream capture tracing credential spray and high-volume amplification attack packets."
      }
    ]
  },
  "TF-040": {
    "name": "Mozi Botnet",
    "category": "Botnet",
    "items": [
      {
        "id": "EVID-040-01",
        "url": "images/mozi_01_p2p.svg",
        "type": "Memory Flow Diagram",
        "title": "Mozi Decentralized P2P DHT Network Architecture",
        "desc": "Decentralized topological graph showing BitTorrent DHT communication and peer-to-peer payload replication."
      },
      {
        "id": "EVID-040-02",
        "url": "images/mozi_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: DHT Packet Formatter & ECDSA Verifier",
        "desc": "Reversed bencode serialization and cryptographic validation of bot command signatures."
      },
      {
        "id": "EVID-040-03",
        "url": "images/mozi_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Mozi P2P DHT Peer Query Stream",
        "desc": "Network capture tracing find_node queries and peer cluster synchronization."
      }
    ]
  },
  "TF-041": {
    "name": "Meduza Stealer",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-041-01",
        "url": "images/meduza_01_collector.svg",
        "type": "Memory Flow Diagram",
        "title": "Meduza Stealer In-Memory Harvester Pipeline",
        "desc": "Diagram tracing automated collection of browser credentials, crypto extension vaults, and Telegram sessions."
      },
      {
        "id": "EVID-041-02",
        "url": "images/meduza_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: MetaMask & Crypto Wallet Grabber",
        "desc": "Decompiled C code scanning IndexedDB directories for crypto wallet private keys and seed phrases."
      },
      {
        "id": "EVID-041-03",
        "url": "images/meduza_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Meduza Stealer Log Exfiltration Stream",
        "desc": "Packet inspection of encrypted HTTP POST request transmitting stolen credentials to C2 IP."
      }
    ]
  },
  "TF-042": {
    "name": "RisePro",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-042-01",
        "url": "images/risepro_01_stealer.svg",
        "type": "Memory Flow Diagram",
        "title": "RisePro Credential Extraction Engine & Network Protocol",
        "desc": "Architectural overview detailing multi-threaded credential grabbing and direct TCP socket transmission."
      },
      {
        "id": "EVID-042-02",
        "url": "images/risepro_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "Ghidra Decompiler: Custom TCP Socket Exfiltrator",
        "desc": "Reverse engineered non-HTTP TCP client connecting to port 50500 with RC4-encrypted headers."
      },
      {
        "id": "EVID-042-03",
        "url": "images/risepro_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark RisePro Direct TCP Exfiltration Stream",
        "desc": "Dissection of raw TCP binary stream transmitting harvested Discord tokens and browser data."
      }
    ]
  },
  "TF-043": {
    "name": "BunnyLoader",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-043-01",
        "url": "images/bunnyloader_01_modular.svg",
        "type": "Memory Flow Diagram",
        "title": "BunnyLoader Modular Loader Architecture",
        "desc": "Overview of BunnyLoader modular framework featuring keylogger, clipper, and dynamic dropper modules."
      },
      {
        "id": "EVID-043-02",
        "url": "images/bunnyloader_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: Clipboard Clipper & Injection",
        "desc": "Reversed regex pattern matching routines and automated cryptocurrency wallet replacement."
      },
      {
        "id": "EVID-043-03",
        "url": "images/bunnyloader_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark BunnyLoader Task Polling Stream",
        "desc": "Network stream capture showing automated bot registration and payload task retrieval."
      }
    ]
  },
  "TF-044": {
    "name": "Latrodectus",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-044-01",
        "url": "images/latrodectus_01_pipeline.svg",
        "type": "Memory Flow Diagram",
        "title": "Latrodectus Execution Pipeline & Evasion Matrix",
        "desc": "Technical diagram mapping string decryption, API hashing, and process hollowing execution stages."
      },
      {
        "id": "EVID-044-02",
        "url": "images/latrodectus_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: FNV-1a Hash Resolver & Decryptor",
        "desc": "Disassembly showing custom FNV-1a API hashing algorithm and RC4 domain decryption loop."
      },
      {
        "id": "EVID-044-03",
        "url": "images/latrodectus_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark Latrodectus Registration Packet Stream",
        "desc": "Dissection of encrypted HTTPS POST requests transmitting victim hardware profile."
      }
    ]
  },
  "TF-045": {
    "name": "StrelaStealer",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-045-01",
        "url": "images/strelastealer_01_mailvault.svg",
        "type": "Memory Flow Diagram",
        "title": "StrelaStealer Outlook & Thunderbird Extraction Pipeline",
        "desc": "Structural diagram illustrating registry query loops for Outlook profiles and key4.db decryption."
      },
      {
        "id": "EVID-045-02",
        "url": "images/strelastealer_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: Mail Profile & Key Extraction",
        "desc": "Reversed registry traversal routines and Base64 exfiltration formatting."
      },
      {
        "id": "EVID-045-03",
        "url": "images/strelastealer_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark StrelaStealer Exfiltration Stream",
        "desc": "Packet inspection of HTTP POST request uploading harvested IMAP/POP3 credentials to C2 server."
      }
    ]
  },
  "TF-046": {
    "name": "HijackLoader",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-046-01",
        "url": "images/hijackloader_01_injection.svg",
        "type": "Memory Flow Diagram",
        "title": "HijackLoader DLL Search-Order Hijacking & APC Injection",
        "desc": "Detailed schema illustrating legitimate executable weaponization and early-bird APC injection into system binaries."
      },
      {
        "id": "EVID-046-02",
        "url": "images/hijackloader_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: DLL Hijack & QueueUserAPC Hook",
        "desc": "Disassembly showing PE overlay shellcode extraction and QueueUserAPC injection into svchost.exe."
      },
      {
        "id": "EVID-046-03",
        "url": "images/hijackloader_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark HijackLoader Stage-2 Retrieval Stream",
        "desc": "Network stream capture showing encrypted payload block retrieval over port 443."
      }
    ]
  },
  "TF-047": {
    "name": "RustBucket",
    "category": "Loader",
    "items": [
      {
        "id": "EVID-047-01",
        "url": "images/rustbucket_01_macos.svg",
        "type": "Memory Flow Diagram",
        "title": "RustBucket macOS Multi-Stage Architecture (Lazarus Group)",
        "desc": "Architectural breakdown illustrating weaponized PDF viewer, AppleScript triggers, and Mach-O ARM64 payload staging."
      },
      {
        "id": "EVID-047-02",
        "url": "images/rustbucket_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro 8.4 Mach-O Decompiler: Objective-C Stager",
        "desc": "ARM64 disassembly illustrating Objective-C method dispatching and decoy PDF presentation."
      },
      {
        "id": "EVID-047-03",
        "url": "images/rustbucket_03_traffic.svg",
        "type": "C2 Traffic Dissection",
        "title": "Wireshark macOS Telemetry Beacon Stream",
        "desc": "Dissection of HTTPS beacon packets conveying macOS system UUID and Darwin kernel version."
      }
    ]
  },
  "TF-048": {
    "name": "Atomic Stealer (AMOS)",
    "category": "InfoStealer",
    "items": [
      {
        "id": "EVID-048-01",
        "url": "images/atomic_01_prompt.svg",
        "type": "Execution Artifact",
        "title": "Atomic Stealer Fake AppleScript System Authentication Prompt",
        "desc": "Forensic recreation of the deceptive macOS system credentials prompt spoofing Apple System Preferences."
      },
      {
        "id": "EVID-048-02",
        "url": "images/atomic_02_traffic.png",
        "type": "Execution Artifact",
        "title": "Telegram Bot Exfiltration Traffic & Victim Profile",
        "desc": "Captured Telegram C2 channel broadcasting compromised keychain databases, browser profiles, and wallet tokens."
      },
      {
        "id": "EVID-048-03",
        "url": "images/atomic_03_c2.png",
        "type": "C2 Panel",
        "title": "Atomic Stealer Web Panel & Log Ingestion Dashboard",
        "desc": "Web-based administration interface categorizing stolen Apple Keychain records, Safari history, and notes."
      }
    ]
  },
  "TF-049": {
    "name": "ShadowPad",
    "category": "C2 Framework",
    "items": [
      {
        "id": "EVID-049-01",
        "url": "images/shadowpad_01_plugins.svg",
        "type": "Memory Flow Diagram",
        "title": "ShadowPad Modular Plugin & In-Memory Execution Architecture",
        "desc": "Topological schema illustrating modular plugin initialization, encrypted virtual file system, and C2 routing."
      },
      {
        "id": "EVID-049-02",
        "url": "images/shadowpad_02_decompiler.svg",
        "type": "Workbench Disassembly",
        "title": "IDA Pro Decompiler: DLL Sideload & Plugin Decryptor",
        "desc": "Reverse engineered hijacked DllMain entrypoint and RC4/XOR dynamic plugin decryption routine."
      }
    ]
  },
  "TF-050": {
    "name": "PlugX",
    "category": "RAT",
    "items": [
      {
        "id": "EVID-050-01",
        "url": "images/plugx_01_builder.png",
        "type": "Builder UI",
        "title": "PlugX (Korplug) Builder & Configuration Utility",
        "desc": "APT builder interface configuring DLL sideloading trios, shellcode obfuscation, and C2 domain arrays."
      },
      {
        "id": "EVID-050-02",
        "url": "images/plugx_01_sideload.svg",
        "type": "Memory Flow Diagram",
        "title": "Classic DLL Sideloading Trio (EXE + DLL + DAT)",
        "desc": "Diagram of classic execution chain: legitimate signed executable, rogue DLL, and encrypted payload file."
      }
    ]
  }
}

# Write to data/forensic_media_manifest.json
manifest_json_path = os.path.join(DATA_DIR, 'forensic_media_manifest.json')
with open(manifest_json_path, 'w', encoding='utf-8') as f:
    json.dump(MANIFEST_DATA, f, indent=2, ensure_ascii=False)
print(f"Updated {manifest_json_path}")

# Write to js/forensic-media-manifest.js
manifest_js_path = os.path.join(JS_DIR, 'forensic-media-manifest.js')
js_content = f"""/**
 * CYBERTRACE FORENSIC MEDIA MANIFEST
 * Unified Local Forensic Assets Registry for TF-001 through TF-050
 * 100% Pure Technical CTI English Edition - Zero External Dependencies
 */

const FORENSIC_MEDIA_MANIFEST = {json.dumps(MANIFEST_DATA, indent=2, ensure_ascii=False)};
"""

with open(manifest_js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)
print(f"Updated {manifest_js_path}")

# Verification of all 50 items and counts
item_counts = {}
for tid, tdata in MANIFEST_DATA.items():
    cnt = len(tdata['items'])
    item_counts[cnt] = item_counts.get(cnt, 0) + 1
    for it in tdata['items']:
        p = os.path.join(BASE_DIR, it['url'])
        if not os.path.exists(p) or os.path.getsize(p) == 0:
            print(f"ERROR: Missing file {it['url']} for {tid}")

print("\nManifest Item Count Distribution:", item_counts)
print(f"Total Threats Indexed: {len(MANIFEST_DATA)}")
total_assets = sum(len(d['items']) for d in MANIFEST_DATA.values())
print(f"Total Forensic Assets Linked: {total_assets}")
