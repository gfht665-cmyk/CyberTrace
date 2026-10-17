import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
DATA_DIR = os.path.join(BASE_DIR, 'data')
JS_DIR = os.path.join(BASE_DIR, 'js')
THREATS_DIR = os.path.join(BASE_DIR, 'threats')

with open(os.path.join(BASE_DIR, 'scripts', 'parsed_threats.json'), 'r', encoding='utf-8') as f:
    threats = json.load(f)

with open(os.path.join(BASE_DIR, 'scripts', 'generate_custom_schematics.py'), 'r', encoding='utf-8') as f:
    text = f.read()

slug_map_str = text.split('SLUG_MAP = {')[1].split('}')[0]
slug_map = {}
for line in slug_map_str.strip().split('\n'):
    if ':' in line:
        k, v = line.strip().split(':')
        slug_map[k.strip(' ",\'')] = v.strip(' ",\'')

files_on_disk = set(os.listdir(IMAGES_DIR))

# Threat-specific technical descriptions
DESCRIPTIONS = {
    "TF-001": {
        "r1_type": "Builder UI",
        "r1_title": "AsyncRAT Client Payload Builder & Configurator",
        "r1_desc": "Operator configurator GUI showing TLS X.509 certificate generation, keylogger toggles, process injection, and persistence configuration.",
        "r2_type": "Surveillance Telemetry",
        "r2_title": "AsyncRAT Remote Desktop & Session Monitoring",
        "r2_desc": "Interactive desktop surveillance module capturing victim screen buffers and keystroke telemetry streams.",
    },
    "TF-002": {
        "r1_type": "Builder UI",
        "r1_title": "Dolphin X AI Stealer Builder Interface",
        "r1_desc": "Builder interface setting target heuristics, browser extension targeting, and polymorphic stub compilation parameters.",
        "r2_type": "Exfiltration Channel",
        "r2_title": "Dolphin X Encrypted Telegram Exfiltration Feed",
        "r2_desc": "Operator notification channel broadcasting compromised victim specifications, geolocations, and encrypted credential archives.",
    },
    "TF-003": {
        "r1_type": "Sandbox Execution",
        "r1_title": "Lumma Stealer Process Execution Graph",
        "r1_desc": "ANY.RUN sandbox telemetry displaying multi-stage process injection, anti-analysis loops, and credential harvesting routines.",
        "r2_type": "C2 Communication",
        "r2_title": "LummaC2 Fast-Flux Network Handshake",
        "r2_desc": "Encrypted HTTP C2 beaconing protocol showing dynamic domain resolution and target configuration retrieval.",
    },
    "TF-004": {
        "r1_type": "Process Injection",
        "r1_title": "RedLine Stealer Lua Bytecode Execution",
        "r1_desc": "ANY.RUN sandbox capture showing Lua bytecode decompression and process hollowing into legitimate Windows processes.",
        "r2_type": "Memory Extraction",
        "r2_title": "RedLine Browser Credential Vault Grabbing",
        "r2_desc": "Forensic memory trace extracting DPAPI-protected credentials, session cookies, and cryptocurrency wallets.",
    },
    "TF-005": {
        "r1_type": "C2 Telemetry",
        "r1_title": "Vidar Dead-Drop Resolver Telemetry",
        "r1_desc": "ANY.RUN network capture displaying Telegram channel lookups used as dead-drop resolvers for C2 IP address retrieval.",
        "r2_type": "Payload Execution",
        "r2_title": "Vidar Stealer SQLite Harvesting Routine",
        "r2_desc": "Memory analysis showing automated extraction of login data from Chromium and Gecko-based browser databases.",
    },
    "TF-006": {
        "r1_type": "Execution Chain",
        "r1_title": "Agent Tesla Process Tree & Weaponized Document",
        "r1_desc": "Forensic sandbox process hierarchy showing weaponized office document execution and payload staging.",
        "r2_type": "Exfiltration Module",
        "r2_title": "Agent Tesla SMTP Exfiltration Routine",
        "r2_desc": "Decompiled .NET routine responsible for packaging keystroke logs and dispatching them via TLS SMTP channels.",
    },
    "TF-007": {
        "r1_type": "Builder UI",
        "r1_title": "Remcos Professional Client Builder & Evasion Configurator",
        "r1_desc": "Builder interface displaying TLS encryption parameters, rootkit cloaking, watchdog persistence, and anti-analysis options.",
        "r2_type": "Operator Console",
        "r2_title": "Remcos Remote Administration Management Console",
        "r2_desc": "Management console monitoring connected remote bots, system telemetry, and active surveillance streams.",
    },
    "TF-008": {
        "r1_type": "Builder UI",
        "r1_title": "XWorm Advanced Payload Builder Interface",
        "r1_desc": "Configurator interface setting USB spreaders, clipper addresses, ransomware routines, and HVNC modules.",
        "r2_type": "Clipper Module",
        "r2_title": "XWorm Cryptocurrency Clipper Memory Routine",
        "r2_desc": "Disassembly showing clipboard regex monitoring for Bitcoin, Ethereum, and Monero wallet string replacement.",
    },
    "TF-009": {
        "r1_type": "Infection Vector",
        "r1_title": "DarkGate Malicious MSI & AutoIt Lure",
        "r1_desc": "Malwarebytes forensic capture showing rogue MSI installer dropping obfuscated AutoIt interpreter script stubs.",
        "r2_type": "Config Extractor",
        "r2_title": "DarkGate Extracted C2 Configuration Parameters",
        "r2_desc": "Automated extractor output displaying AES-encrypted C2 servers, botnet flags, and evasion switches.",
    },
    "TF-010": {
        "r1_type": "Builder UI",
        "r1_title": "Rhadamanthys Stealer Operator Panel Interface",
        "r1_desc": "Web-based management console tracking active victim infections, geolocations, and extracted credential counts.",
        "r2_type": "Memory VM",
        "r2_title": "Rhadamanthys Custom Virtual Machine Architecture",
        "r2_desc": "Disassembly showing custom bytecode VM interpreter designed to thwart static analysis and heuristic emulators.",
    },
    "TF-011": {
        "r1_type": "C2 Config",
        "r1_title": "Stealc C2 Communication Protocol Analysis",
        "r1_desc": "ANY.RUN forensic capture showing RC4 string decryption and endpoint registration with command-and-control servers.",
        "r2_type": "Target Grabbing",
        "r2_title": "Stealc Modular Data Harvesting Pipeline",
        "r2_desc": "Execution capture showing file-grabbing rules targeting browser extensions, Discord tokens, and crypto wallet paths.",
    },
    "TF-012": {
        "r1_type": "Payload Generator",
        "r1_title": "Havoc Framework Demon Payload Configurator",
        "r1_desc": "Official Havoc client UI configuring Demon agent sleep obfuscation, indirect syscalls, and x64 shellcode injection stubs.",
        "r2_type": "Operator Console",
        "r2_title": "Havoc C2 Interactive Session Console",
        "r2_desc": "Operator UI managing compromised enterprise hosts, active Demon beacons, and lateral movement listeners.",
    },
    "TF-013": {
        "r1_type": "Operator Console",
        "r1_title": "Sliver C2 Interactive Command Console",
        "r1_desc": "Operator shell session showing active multiplayer beacons, WireGuard tunnels, and mTLS listener parameters.",
        "r2_type": "Injection Routine",
        "r2_title": "Sliver Process Injection & Evasion Engine",
        "r2_desc": "Technical visualization of indirect syscall execution and thread stack spoofing mechanisms.",
    },
    "TF-014": {
        "r1_type": "Operator Dashboard",
        "r1_title": "Mythic C2 Operation Management Dashboard",
        "r1_desc": "Web interface aggregating active agent callbacks, tasking queues, and modular payload build profiles.",
        "r2_type": "Payload Architecture",
        "r2_title": "Mythic Modular Agent Communication Engine",
        "r2_desc": "C2 communication trace showing JSON-RPC tasking and staging across custom translation containers.",
    },
    "TF-015": {
        "r1_type": "Builder UI",
        "r1_title": "QuasarRAT Open-Source Builder & Certificate Generator",
        "r1_desc": "Client builder GUI configuring TLS certificate pinning, startup registry persistence, and keylogger hooks.",
        "r2_type": "Surveillance Module",
        "r2_title": "QuasarRAT Surveillance & File Manager Interface",
        "r2_desc": "Interactive operator panel monitoring victim file systems, reverse socks proxies, and active processes.",
    },
    "TF-016": {
        "r1_type": "Builder UI",
        "r1_title": "Warzone RAT (Ave Maria) Builder Interface",
        "r1_desc": "Configurator GUI showing UAC bypass method selection, privilege escalation hooks, and password recovery modules.",
        "r2_type": "Privilege Escalation",
        "r2_title": "Warzone RAT AveMaria Memory Persistence Engine",
        "r2_desc": "Forensic disassembly showing task scheduler registration and explorer.exe process hollowing routines.",
    },
    "TF-017": {
        "r1_type": "Execution Chain",
        "r1_title": "GuLoader (CloudEyE) Multi-Stage Shellcode Chain",
        "r1_desc": "ANY.RUN threat infographic detailing VBS dropper, registry payload storage, and shellcode injection sequence.",
        "r2_type": "Anti-Analysis Routine",
        "r2_title": "GuLoader Vectored Exception Handling (VEH) Check",
        "r2_desc": "Process memory disassembly showing hardware breakpoint detection and anti-debugging exception routines.",
    },
    "TF-018": {
        "r1_type": "Loader Routine",
        "r1_title": "Pikabot Modular Core Loader Architecture",
        "r1_desc": "Forensic sandbox process tree displaying encrypted blob unpacking and DLL injection into legitimate system processes.",
        "r2_type": "C2 Protocol",
        "r2_title": "Pikabot Network Beacon & RC4 Decryption",
        "r2_desc": "Network capture analyzing AES-CBC C2 beaconing structure and infected endpoint fingerprinting.",
    },
    "TF-019": {
        "r1_type": "Banking Module",
        "r1_title": "Qakbot (QBot) Core Web-Inject & Delivery Engine",
        "r1_desc": "Forensic memory trace showing thread hijacking and man-in-the-browser banking credential interception.",
        "r2_type": "Process Hollowing",
        "r2_title": "Qakbot Process Replacement in wermgr.exe",
        "r2_desc": "Process monitor telemetry tracking hollowed process creation and memory section remapping.",
    },
    "TF-020": {
        "r1_type": "Botnet Architecture",
        "r1_title": "Emotet Epoch Tier-1 Command Infrastructure",
        "r1_desc": "Telemetry diagram illustrating compromised router proxy chains and automated spambot email harvesting modules.",
        "r2_type": "Payload Execution",
        "r2_title": "Emotet Encrypted DLL Loader Disassembly",
        "r2_desc": "Disassembly showing control flow flattening and string decryption routines executing inside regsvr32.exe.",
    },
    "TF-021": {
        "r1_type": "Ransomware Execution",
        "r1_title": "LockBit 3.0 (Black) Execution Process Tree",
        "r1_desc": "ANY.RUN sandbox capture showing service termination, shadow copy deletion, and high-speed file encryption.",
        "r2_type": "Leak Infrastructure",
        "r2_title": "LockBit Darknet Tor Extortion Portal",
        "r2_desc": "Onion portal interface detailing ransom demands, countdown timers, and stolen proof-of-concept data archives.",
    },
    "TF-022": {
        "r1_type": "Execution Flags",
        "r1_title": "BlackCat (ALPHV) Rust CLI Execution Parameters",
        "r1_desc": "Forensic terminal capture displaying command-line switches for domain escalation, safemode reboot, and shadow wipe.",
        "r2_type": "Ransom Artifact",
        "r2_title": "BlackCat Recover-My-Files Note & Tor Gateway",
        "r2_desc": "Generated ransom text note dropped on encrypted endpoints pointing to the ALPHV negotiation portal.",
    },
    "TF-023": {
        "r1_type": "Extortion Engine",
        "r1_title": "Akira Ransomware Enterprise Encryption Routine",
        "r1_desc": "Forensic capture detailing C++ multi-threaded file encryption using ChaCha20 and RSA public key wrapping.",
        "r2_type": "Disassembly Analysis",
        "r2_title": "Akira Volume Shadow Deletion & Service Killer",
        "r2_desc": "IDA Pro disassembly highlighting PowerShell invocations wiping backup repositories and stopping SQL services.",
    },
    "TF-024": {
        "r1_type": "Extortion Portal",
        "r1_title": "Medusa Ransomware Blog & Victim Negotiation Console",
        "r1_desc": "Tor negotiation portal showing victim countdown timers, ransom payment deadlines, and published leak archives.",
        "r2_type": "Disassembly Analysis",
        "r2_title": "Medusa Service Termination & Process Sweeper",
        "r2_desc": "Disassembly showing enumeration and killing of antivirus, database, and backup management services.",
    },
    "TF-025": {
        "r1_type": "Decryptor Utility",
        "r1_title": "Phobos / 8Base Ransomware Execution & Recovery Stub",
        "r1_desc": "Forensic capture displaying file extension appending (.id[...].[email].phobos) and ransom note deployment.",
        "r2_type": "Network Telemetry",
        "r2_title": "Phobos Command and Control Beaconing",
        "r2_desc": "Network telemetry trace tracking victim system registration and AES encryption key escrow exchange.",
    },
    "TF-026": {
        "r1_type": "Injection Scheme",
        "r1_title": "Formbook / XLoader Multi-Level Injection Chain",
        "r1_desc": "ANY.RUN technical diagram illustrating payload decryption and nested thread injection into system binaries.",
        "r2_type": "C2 Decryption",
        "r2_title": "Formbook Traffic Encryption & Decryption Engine",
        "r2_desc": "Forensic memory trace detailing base64 and RC4 decoding of command-and-control responses.",
    },
    "TF-027": {
        "r1_type": "Stager Routine",
        "r1_title": "Bumblebee Modular Loader Staging Routine",
        "r1_desc": "Forensic sandbox process showing WMI reconnaissance, process hollowing, and secondary payload staging.",
        "r2_type": "Disassembly Analysis",
        "r2_title": "Bumblebee WebSocket C2 Handshake Routine",
        "r2_desc": "Disassembly tracking WebSocket connection initialization and JSON-formatted command exchange.",
    },
    "TF-028": {
        "r1_type": "Steganography",
        "r1_title": "IcedID (BokBot) Steganographic PNG Loader",
        "r1_desc": "Forensic image analysis showing extraction of hidden encrypted payload from downloaded PNG image files.",
        "r2_type": "Banking Module",
        "r2_title": "IcedID Process Injection into svchost.exe",
        "r2_desc": "Process monitor trace tracking hollowed svchost.exe instances used for banking credential theft.",
    },
    "TF-029": {
        "r1_type": "Operator Panel",
        "r1_title": "DanaBot Banking Trojan Control Interface",
        "r1_desc": "Operator web panel tracking active banking bot infections, compromised corporate networks, and injection rules.",
        "r2_type": "Disassembly Analysis",
        "r2_title": "DanaBot Modular Architecture & Plugin Loader",
        "r2_desc": "Disassembly showing dynamic download and decryption of specialized sniffing and video capture modules.",
    },
    "TF-030": {
        "r1_type": "Plugin Engine",
        "r1_title": "SmokeLoader Modular Plugin System",
        "r1_desc": "Technical visualization of SmokeLoader core memory resident loop loading encrypted payload extensions.",
        "r2_type": "Anti-Analysis",
        "r2_title": "SmokeLoader API Hashing & VM Detection",
        "r2_desc": "Disassembly showing API name hashing algorithms used to bypass security solution import table monitoring.",
    },
    "TF-031": {
        "r1_type": "Listeners UI",
        "r1_title": "Cobalt Strike Listener Management & Beacon Console",
        "r1_desc": "Operator interface configuring HTTP, HTTPS, and DNS malleable C2 listeners and tracking active Beacons.",
        "r2_type": "Beacon Architecture",
        "r2_title": "Cobalt Strike In-Memory Beacon Reflection Engine",
        "r2_desc": "Technical schematic showing Reflective DLL loading, sleep masking, and thread stack spoofing mechanisms.",
    },
    "TF-032": {
        "r1_type": "Payload Execution",
        "r1_title": "Brute Ratel C4 Badger Execution Graph",
        "r1_desc": "ANY.RUN sandbox process trace tracking Badger payload injection and memory manipulation routines.",
        "r2_type": "Syscall Engine",
        "r2_title": "Brute Ratel Indirect Syscall Execution Routine",
        "r2_desc": "Disassembly showing dynamic SSN resolution and indirect syscall execution bypassing user-mode EDR hooks.",
    },
    "TF-033": {
        "r1_type": "Gateway Config",
        "r1_title": "NetSupport RAT Gateway Configuration & Deployment",
        "r1_desc": "Forensic analysis of client32.ini configuration parameters establishing covert gateway reverse connections.",
        "r2_type": "Disassembly Analysis",
        "r2_title": "NetSupport RAT Screen Capture & Keystroke Monitor",
        "r2_desc": "Disassembly tracking surveillance API hooks capturing remote desktop buffers and operator commands.",
    },
    "TF-034": {
        "r1_type": "Builder UI",
        "r1_title": "NjRAT (Bladabindi) Golden Edition Builder Interface",
        "r1_desc": "Visual Basic .NET builder configuring payload persistence, dynamic DNS connection strings, and mutex flags.",
        "r2_type": "Operator Console",
        "r2_title": "NjRAT Victim Management & Webcam Surveillance Console",
        "r2_desc": "Operator UI managing connected victim bots, remote desktop viewing, and live microphone capture streams.",
    },
    "TF-035": {
        "r1_type": "Builder UI",
        "r1_title": "DCRat (DarkCrystal) Studio & Plugin Builder",
        "r1_desc": "Modern builder interface displaying modular plugin selections, stealer configurations, and obfuscation options.",
        "r2_type": "Operator Console",
        "r2_title": "DCRat Botnet Administration Dashboard",
        "r2_desc": "Web-based administration console tracking active victim nodes, geolocations, and extracted credentials.",
    },
    "TF-036": {
        "r1_type": "Obfuscation Engine",
        "r1_title": "PureCrypter Multi-Layer Obfuscation Architecture",
        "r1_desc": "Forensic diagram detailing .NET runtime compression, dynamic decryption stubs, and AMSI memory patching.",
        "r2_type": "Disassembly Analysis",
        "r2_title": "PureCrypter In-Memory Payload Decryption",
        "r2_desc": "Disassembly tracking AES payload extraction from encrypted resources and injection into target processes.",
    },
    "TF-037": {
        "r1_type": "Distribution Network",
        "r1_title": "PrivateLoader Pay-Per-Install Distribution Topology",
        "r1_desc": "ANY.RUN technical diagram detailing corporate endpoint compromise via Pay-Per-Install malware distribution channels.",
        "r2_type": "Payload Decryption",
        "r2_title": "PrivateLoader Payload Decryption & Execution Trace",
        "r2_desc": "Process memory capture showing secondary payload downloading, decryption, and execution validation.",
    },
    "TF-038": {
        "r1_type": "Proxy Engine",
        "r1_title": "SystemBC SOCKS5 Tor Proxy Tunnel Architecture",
        "r1_desc": "Technical visualization of SystemBC acting as a covert encrypted proxy for ransomware gang lateral movement.",
        "r2_type": "Network Telemetry",
        "r2_title": "SystemBC Beacon Traffic & Command Protocol",
        "r2_desc": "Packet capture analysis showing RC4-encrypted beaconing communicating with adversary command servers.",
    },
    "TF-039": {
        "r1_type": "Telnet Scanner",
        "r1_title": "Mirai IoT Telnet Brute-Force Scanner Routine",
        "r1_desc": "ANY.RUN analysis capture showing Mirai bot scanning IPv4 address space using hardcoded default credential dictionaries.",
        "r2_type": "DDoS Engine",
        "r2_title": "Mirai SYN and UDP Flood Attack Engine",
        "r2_desc": "Disassembly showing raw socket creation and automated transmission of high-volume DDoS packets.",
    },
    "TF-040": {
        "r1_type": "P2P Network",
        "r1_title": "Mozi Botnet DHT P2P Coordination Protocol",
        "r1_desc": "Technical schematic illustrating BitTorrent DHT protocol abuse for distributed C2 command broadcasting.",
        "r2_type": "Exploit Module",
        "r2_title": "Mozi IoT Zero-Day Exploit Propagation Module",
        "r2_desc": "Disassembly tracking automated execution of UPnP and router vulnerability exploits against target subnets.",
    },
    "TF-041": {
        "r1_type": "Collector Dashboard",
        "r1_title": "Meduza Stealer Web Administration Dashboard",
        "r1_desc": "Operator web console aggregating infected victim logs, browser credential databases, and cold storage crypto keys.",
        "r2_type": "Network Telemetry",
        "r2_title": "Meduza Stealer C2 Exfiltration Handshake",
        "r2_desc": "Network telemetry trace showing encrypted ZIP archive exfiltration containing harvested endpoint data.",
    },
    "TF-042": {
        "r1_type": "Network Protocol",
        "r1_title": "RisePro Stealer Network Communication & Encryption",
        "r1_desc": "ANY.RUN forensic capture analyzing custom TCP protocol used by RisePro to transmit exfiltrated system data.",
        "r2_type": "Exfiltration Packet",
        "r2_title": "RisePro Credential Archive Assembly & Dispatch",
        "r2_desc": "Memory analysis showing compilation of password logs, system information, and browser artifacts into C2 packets.",
    },
    "TF-043": {
        "r1_type": "Modular Core",
        "r1_title": "BunnyLoader 3.0 Modular Control Interface",
        "r1_desc": "C2 web panel displaying active loader instances, modular plugin downloads, and cryptocurrency clipper status.",
        "r2_type": "Network Telemetry",
        "r2_title": "BunnyLoader Tasking & Secondary Drop Telemetry",
        "r2_desc": "Network capture analyzing endpoint registration and automated retrieval of secondary stealer payloads.",
    },
    "TF-044": {
        "r1_type": "Execution Pipeline",
        "r1_title": "Latrodectus High-Stealth Loader Execution Pipeline",
        "r1_desc": "ANY.RUN sandbox telemetry tracking multi-stage loader execution, WMI reconnaissance, and string hashing routines.",
        "r2_type": "C2 Telemetry",
        "r2_title": "Latrodectus FNV-1a Hashing & C2 Beacon Protocol",
        "r2_desc": "Network telemetry trace showing encrypted command-and-control handshakes and bot ID registration.",
    },
    "TF-045": {
        "r1_type": "Mail Harvester",
        "r1_title": "StrelaStealer Outlook & Thunderbird Credential Harvester",
        "r1_desc": "Technical visualization of StrelaStealer parsing email client configuration files to extract IMAP/POP3 passwords.",
        "r2_type": "Network Telemetry",
        "r2_title": "StrelaStealer C2 Exfiltration Traffic",
        "r2_desc": "Packet inspection showing multipart HTTP POST transmission of extracted email credentials to adversary nodes.",
    },
    "TF-046": {
        "r1_type": "Chunk Extraction",
        "r1_title": "HijackLoader (IDAT Loader) Image Chunk Extraction",
        "r1_desc": "ANY.RUN technical capture showing extraction and decryption of hidden shellcode from PNG IDAT chunks.",
        "r2_type": "Process Hollowing",
        "r2_title": "HijackLoader Process Injection into Clean Windows Binary",
        "r2_desc": "Process monitor telemetry tracking hollowed process creation and memory section remapping.",
    },
    "TF-047": {
        "r1_type": "macOS Lure",
        "r1_title": "RustBucket macOS PDF Viewer Lure & Execution",
        "r1_desc": "Forensic trace analyzing AppleScript invocation and fake PDF reader application dropping Mach-O binaries.",
        "r2_type": "Network Telemetry",
        "r2_title": "RustBucket Multi-Stage C2 Domain Resolution",
        "r2_desc": "Network capture tracking second-stage Mach-O payload retrieval from adversary-controlled infrastructure.",
    },
    "TF-048": {
        "r1_type": "ClickFix Lure",
        "r1_title": "Atomic Stealer (AMOS) macOS ClickFix Delivery Lure",
        "r1_desc": "ANY.RUN sandbox capture showing social engineering prompt tricking macOS users into executing malicious terminal commands.",
        "r2_type": "C2 Exfiltration",
        "r2_title": "Atomic Stealer Telegram & HTTP Exfiltration Traffic",
        "r2_desc": "Network capture tracking exfiltration of Keychain databases, browser cookies, and hardware specs to adversary C2.",
    },
    "TF-049": {
        "r1_type": "Plugin Engine",
        "r1_title": "ShadowPad Modular Backdoor Architecture",
        "r1_desc": "Technical visualization of ShadowPad virtual file system and dynamic DLL plugin dispatch table.",
        "r2_type": "Disassembly Analysis",
        "r2_title": "ShadowPad Root Loader & DLL Sideloading Routine",
        "r2_desc": "Disassembly showing legitimate signed host binary abused for DLL search-order hijacking.",
    },
    "TF-050": {
        "r1_type": "Builder UI",
        "r1_title": "PlugX (Korplug) Payload Builder & Configurator",
        "r1_desc": "Operator configurator GUI showing encryption key generation, C2 domain insertion, and service installation options.",
        "r2_type": "DLL Sideloading",
        "r2_title": "PlugX DLL Search-Order Hijacking Routine",
        "r2_desc": "Forensic diagram tracking legitimate executable loading malicious proxy DLL and decrypting .dat payload.",
    }
}

manifest = {}

print("=== Building Strict 1-to-1 Forensic Media Manifest ===")
for t in threats:
    tid = t['id']
    slug = slug_map[tid]
    name = t['name']
    cat = t['category']
    desc_info = DESCRIPTIONS.get(tid, {})
    
    # Locate files on disk strictly matching {tid}_{slug}_*
    r1_files = [f for f in files_on_disk if f.startswith(f"{tid}_{slug}_real_01")]
    r2_files = [f for f in files_on_disk if f.startswith(f"{tid}_{slug}_real_02")]
    arch_files = [f for f in files_on_disk if f == f"{tid}_{slug}_arch.svg"]
    
    if not r1_files or not r2_files or not arch_files:
        print(f"Error: missing triad for {tid}: r1={r1_files}, r2={r2_files}, arch={arch_files}")
        sys.exit(1)
        
    r1_file = r1_files[0]
    r2_file = r2_files[0]
    arch_file = arch_files[0]
    
    items = [
        {
            "id": f"EVID-{t['num']}-01",
            "url": f"images/{r1_file}",
            "type": desc_info.get("r1_type", "Forensic Capture"),
            "title": desc_info.get("r1_title", f"{name} Primary Forensic Capture"),
            "desc": desc_info.get("r1_desc", f"Forensic analysis capture for {name} ({cat}).")
        },
        {
            "id": f"EVID-{t['num']}-02",
            "url": f"images/{r2_file}",
            "type": desc_info.get("r2_type", "Telemetry Analysis"),
            "title": desc_info.get("r2_title", f"{name} Telemetry & Disassembly"),
            "desc": desc_info.get("r2_desc", f"Technical disassembly and execution trace for {name}.")
        },
        {
            "id": f"EVID-{t['num']}-03",
            "url": f"images/{arch_file}",
            "type": "Architecture Schematic",
            "title": f"{name} Technical Infection Chain & Architecture",
            "desc": f"Tailored forensic schematic mapping initial access, defense evasion, core capabilities, and {t['c2']} command infrastructure."
        }
    ]
    
    # Check for additional threat-exclusive files (e.g. Dolphin X, DarkGate, etc.)
    if tid == "TF-002" and "dolphinx_05_dashboard.png" in files_on_disk:
        items.append({
            "id": "EVID-002-04",
            "url": "images/dolphinx_05_dashboard.png",
            "type": "C2 Dashboard",
            "title": "Dolphin X Central Web Telemetry Dashboard",
            "desc": "Centralized operator interface aggregating infected victim nodes and exfiltrated credential archives."
        })
    elif tid == "TF-009" and "darkgate_04_traffic.jpeg" in files_on_disk:
        items.append({
            "id": "EVID-009-04",
            "url": "images/darkgate_04_traffic.jpeg",
            "type": "Network Packet Capture",
            "title": "DarkGate HTTP C2 Request Header Analysis",
            "desc": "Raw packet inspection showing HTTP POST parameters and custom User-Agent beacons."
        })
        
    manifest[tid] = {
        "name": name,
        "category": cat,
        "items": items
    }

# Save manifest to JSON
manifest_json_path = os.path.join(DATA_DIR, 'forensic_media_manifest.json')
with open(manifest_json_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2)
print(f"✅ Saved: {manifest_json_path} ({len(manifest)} threats)")

# Save manifest to JS
manifest_js_path = os.path.join(JS_DIR, 'forensic-media-manifest.js')
with open(manifest_js_path, 'w', encoding='utf-8') as f:
    f.write("/**\n * CYBERTRACE INTELLIGENCE PLATFORM\n * Strict 1-to-1 Forensic Media Manifest (Pure Technical English)\n */\n\n")
    f.write("const FORENSIC_MEDIA_MANIFEST = ")
    json.dump(manifest, f, indent=2)
    f.write(";\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = { FORENSIC_MEDIA_MANIFEST };\n}\n")
print(f"✅ Saved: {manifest_js_path}")
