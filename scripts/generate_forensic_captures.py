#!/usr/bin/env python3
"""
CyberTrace High-Resolution Forensic Workbench Capture Generator
Generates realistic, professional reverse-engineering workbench captures
(IDA Pro 8.4 Disassembly, x64dbg Memory Dumps, Wireshark C2 Dissectors, Ghidra AST Views)
for all cataloged threat families.
"""

import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

def svg_header(title, tool_badge, w=1100, h=620):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&amp;family=Inter:wght@400;600;700&amp;display=swap');
      .title {{ font-family: 'Inter', system-ui, sans-serif; font-size: 13px; font-weight: 600; fill: #cbd5e1; }}
      .badge {{ font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 700; }}
      .code {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; fill: #e2e8f0; }}
      .addr {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; fill: #64748b; }}
      .bytes {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; fill: #94a3b8; }}
      .instr {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700; fill: #38bdf8; }}
      .reg {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; fill: #f472b6; }}
      .api {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; font-weight: 700; fill: #4ade80; }}
      .str {{ font-family: 'JetBrains Mono', monospace; font-size: 12px; fill: #fbbf24; }}
      .comm {{ font-family: 'JetBrains Mono', monospace; font-size: 11px; fill: #06b6d4; font-style: italic; }}
      .tab {{ font-family: 'Inter', sans-serif; font-size: 11px; font-weight: 600; }}
      .panel {{ fill: #0b0f19; stroke: #1e293b; stroke-width: 1; }}
    </style>
  </defs>

  <!-- Window Frame -->
  <rect x="0" y="0" width="{w}" height="{h}" rx="8" fill="#090d16" stroke="#223046" stroke-width="1.5"/>
  
  <!-- Titlebar -->
  <rect x="0" y="0" width="{w}" height="36" rx="8" fill="#0f172a"/>
  <rect x="0" y="28" width="{w}" height="8" fill="#0f172a"/>
  <line x1="0" y1="36" x2="{w}" y2="36" stroke="#1e293b" stroke-width="1"/>
  
  <!-- Window Controls -->
  <circle cx="20" cy="18" r="5.5" fill="#ef4444"/>
  <circle cx="38" cy="18" r="5.5" fill="#f59e0b"/>
  <circle cx="56" cy="18" r="5.5" fill="#10b981"/>
  
  <!-- Window Title -->
  <text x="80" y="22" class="title">{title}</text>
  <rect x="{w - 240}" y="9" width="225" height="18" rx="4" fill="#1e293b" stroke="#334155" stroke-width="0.8"/>
  <text x="{w - 232}" y="22" class="badge" fill="#38bdf8">{tool_badge}</text>
'''

def svg_footer():
    return '</svg>'

def generate_ida_view(title, badge, code_lines, threat_name, sample_sha, out_path, w=1100, h=620):
    svg = svg_header(f"IDA Pro 8.4 // [Advanced Disassembly] - {title}", badge, w, h)
    
    # Subheader / Tabs Bar
    svg += f'''
  <!-- Tab Bar -->
  <rect x="0" y="36" width="{w}" height="28" fill="#0b1120"/>
  <line x1="0" y1="64" x2="{w}" y2="64" stroke="#1e293b" stroke-width="1"/>
  
  <!-- Active Tab -->
  <rect x="10" y="42" width="130" height="22" rx="3" fill="#1e293b"/>
  <text x="22" y="57" class="tab" fill="#38bdf8">IDA-View: .text</text>
  
  <!-- Inactive Tabs -->
  <text x="160" y="57" class="tab" fill="#64748b">Hex-Rays C</text>
  <text x="245" y="57" class="tab" fill="#64748b">Imports (IAT)</text>
  <text x="340" y="57" class="tab" fill="#64748b">Strings Table</text>
  <text x="440" y="57" class="tab" fill="#64748b">Functions Map</text>
  
  <!-- Left Side: Functions Navigation Pane -->
  <rect x="10" y="74" width="220" height="{h - 110}" rx="4" class="panel"/>
  <rect x="10" y="74" width="220" height="26" fill="#131c2e" rx="4"/>
  <text x="20" y="91" class="tab" fill="#94a3b8">Functions Window</text>
  
  <text x="20" y="118" class="badge" fill="#4ade80">.text:sub_140001000</text>
  <text x="20" y="136" class="badge" fill="#94a3b8">.text:sub_140001840</text>
  <text x="20" y="154" class="badge" fill="#38bdf8">.text:fn_{threat_name}_Entry</text>
  <text x="20" y="172" class="badge" fill="#94a3b8">.text:sub_1400021A0</text>
  <text x="20" y="190" class="badge" fill="#94a3b8">.text:sub_140002F40</text>
  <text x="20" y="208" class="badge" fill="#f472b6">.text:Decrypt_RC4_Config</text>
  <text x="20" y="226" class="badge" fill="#94a3b8">.text:sub_1400034B0</text>
  <text x="20" y="244" class="badge" fill="#fb7185">.text:Hollow_Remote_Proc</text>
  <text x="20" y="262" class="badge" fill="#94a3b8">.text:sub_140004110</text>
  <text x="20" y="280" class="badge" fill="#94a3b8">.text:sub_1400048A0</text>
  
  <!-- Sample Telemetry Box -->
  <rect x="15" y="{h - 180}" width="210" height="96" rx="4" fill="#080c14" stroke="#1e293b"/>
  <text x="22" y="{h - 164}" class="badge" fill="#38bdf8">SAMPLE TELEMETRY</text>
  <text x="22" y="{h - 148}" class="code" font-size="10" fill="#94a3b8">Arch: x86-64 PE32+</text>
  <text x="22" y="{h - 134}" class="code" font-size="10" fill="#94a3b8">Subsystem: Windows GUI</text>
  <text x="22" y="{h - 120}" class="code" font-size="9" fill="#64748b">Hash: {sample_sha[:16]}...</text>
  <text x="22" y="{h - 104}" class="code" font-size="10" fill="#ef4444">Classification: {threat_name}</text>

  <!-- Right Side: Code Viewport -->
  <rect x="240" y="74" width="{w - 250}" height="{h - 110}" rx="4" class="panel"/>
'''
    # Render Code Lines
    y = 100
    for line in code_lines:
        addr = line.get('addr', '')
        bytes_hex = line.get('bytes', '')
        instr = line.get('instr', '')
        args = line.get('args', '')
        comm = line.get('comm', '')
        
        svg += f'  <text x="255" y="{y}" class="addr">{addr}</text>\n'
        if bytes_hex:
            svg += f'  <text x="375" y="{y}" class="bytes">{bytes_hex}</text>\n'
        if instr:
            svg += f'  <text x="495" y="{y}" class="instr">{instr}</text>\n'
        if args:
            svg += f'  <text x="545" y="{y}" class="code">{args}</text>\n'
        if comm:
            svg += f'  <text x="735" y="{y}" class="comm">; {comm}</text>\n'
        y += 20
        if y > h - 45:
            break

    # Bottom Status Bar
    svg += f'''
  <!-- Status Bar -->
  <rect x="0" y="{h - 26}" width="{w}" height="26" fill="#0f172a"/>
  <line x1="0" y1="{h - 26}" x2="{w}" y2="{h - 26}" stroke="#1e293b" stroke-width="1"/>
  <text x="15" y="{h - 9}" class="badge" fill="#4ade80">AU: idle</text>
  <text x="95" y="{h - 9}" class="badge" fill="#94a3b8">DOWN-SILENT</text>
  <text x="210" y="{h - 9}" class="badge" fill="#38bdf8">0000000140001040</text>
  <text x="{w - 240}" y="{h - 9}" class="badge" fill="#cbd5e1">CYBERTRACE LAB AIR-GAP ENGINE</text>
'''
    svg += svg_footer()
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(svg)

def generate_wireshark_view(title, badge, packets, threat_name, out_path, w=1100, h=620):
    svg = svg_header(f"Wireshark 4.2 // [C2 Network Stream Dissector] - {title}", badge, w, h)
    
    # Packet Table Header
    svg += f'''
  <!-- Network Table Header -->
  <rect x="10" y="46" width="{w - 20}" height="26" fill="#131c2e" rx="4"/>
  <text x="20" y="63" class="badge" fill="#38bdf8">No.</text>
  <text x="65" y="63" class="badge" fill="#38bdf8">Time</text>
  <text x="130" y="63" class="badge" fill="#38bdf8">Source</text>
  <text x="270" y="63" class="badge" fill="#38bdf8">Destination</text>
  <text x="410" y="63" class="badge" fill="#38bdf8">Proto</text>
  <text x="470" y="63" class="badge" fill="#38bdf8">Len</text>
  <text x="520" y="63" class="badge" fill="#38bdf8">Dissected Payload Information / C2 Handshake</text>
  
  <!-- Packet Rows -->
  <rect x="10" y="74" width="{w - 20}" height="260" rx="4" class="panel"/>
'''
    y = 95
    for pkt in packets:
        bg_col = "#111827" if pkt.get('highlight') else "transparent"
        if pkt.get('highlight'):
            svg += f'  <rect x="12" y="{y - 14}" width="{w - 24}" height="20" fill="{bg_col}"/>\n'
        num = pkt.get('no', '1')
        time = pkt.get('time', '0.0000')
        src = pkt.get('src', '192.168.1.105')
        dst = pkt.get('dst', '185.220.101.44')
        proto = pkt.get('proto', 'TCP')
        length = pkt.get('len', '64')
        info = pkt.get('info', '')
        col = "#f43f5e" if "POST" in info or "Beacon" in info or "Payload" in info else ("#38bdf8" if "TLS" in proto else "#e2e8f0")
        
        svg += f'  <text x="20" y="{y}" class="code" font-size="11">{num}</text>\n'
        svg += f'  <text x="65" y="{y}" class="code" font-size="11" fill="#94a3b8">{time}</text>\n'
        svg += f'  <text x="130" y="{y}" class="code" font-size="11">{src}</text>\n'
        svg += f'  <text x="270" y="{y}" class="code" font-size="11">{dst}</text>\n'
        svg += f'  <text x="410" y="{y}" class="badge" fill="#a855f7">{proto}</text>\n'
        svg += f'  <text x="470" y="{y}" class="code" font-size="11" fill="#94a3b8">{length}</text>\n'
        svg += f'  <text x="520" y="{y}" class="code" font-size="11" fill="{col}">{info}</text>\n'
        y += 22

    # Bottom Packet Bytes Inspector
    svg += f'''
  <!-- Hex Dump Panel -->
  <rect x="10" y="342" width="{w - 20}" height="240" rx="4" class="panel"/>
  <rect x="10" y="342" width="{w - 20}" height="24" fill="#131c2e" rx="4"/>
  <text x="20" y="358" class="badge" fill="#4ade80">Packet Hex &amp; ASCII Stream Details [Follow C2 Stream]</text>
  
  <text x="25" y="385" class="addr">0000</text>
  <text x="75" y="385" class="bytes">50 4f 53 54 20 2f 61 70 69 2f 76 31 2f 67 61 74</text>
  <text x="440" y="385" class="str">POST /api/v1/gat</text>
  
  <text x="25" y="405" class="addr">0010</text>
  <text x="75" y="405" class="bytes">65 20 48 54 54 50 2f 31 2e 31 0d 0a 48 6f 73 74</text>
  <text x="440" y="405" class="str">e HTTP/1.1..Host</text>
  
  <text x="25" y="425" class="addr">0020</text>
  <text x="75" y="425" class="bytes">3a 20 74 65 6c 65 6d 65 74 72 79 2d 63 32 2e 69</text>
  <text x="440" y="425" class="str">: telemetry-c2.i</text>

  <text x="25" y="445" class="addr">0030</text>
  <text x="75" y="445" class="bytes">6e 66 6f 0d 0a 58 2d 42 6f 74 2d 49 44 3a 20 42</text>
  <text x="440" y="445" class="str">nfo..X-Bot-ID: B</text>

  <text x="25" y="465" class="addr">0040</text>
  <text x="75" y="465" class="bytes">4f 54 2d 37 41 38 46 2d 39 30 43 31 0d 0a 43 6f</text>
  <text x="440" y="445" class="str">OT-7A8F-90C1..Co</text>

  <text x="25" y="485" class="addr">0050</text>
  <text x="75" y="485" class="bytes">6e 74 65 6e 74 2d 54 79 70 65 3a 20 6f 63 74 65</text>
  <text x="440" y="485" class="str">nt-Type: octe</text>

  <text x="25" y="505" class="addr">0060</text>
  <text x="75" y="505" class="bytes">74 2d 73 74 72 65 61 6d 0d 0a 0d 0a e2 9a a0 4b</text>
  <text x="440" y="505" class="str">t-stream....[ENC</text>

  <text x="25" y="525" class="addr">0070</text>
  <text x="75" y="525" class="bytes">8d 1a 9f 43 0b 77 c4 12 a8 90 2f b6 51 0e 77 a9</text>
  <text x="440" y="525" class="str">...C.w..../.Q.w.</text>

  <text x="25" y="545" class="addr">0080</text>
  <text x="75" y="545" class="bytes">ff 41 8c 30 19 bd 70 e4 22 18 55 a0 6c 73 11 09</text>
  <text x="440" y="545" class="str">.A.0..p.".U.ls..</text>

  <text x="25" y="565" class="addr">0090</text>
  <text x="75" y="565" class="bytes">99 44 bb 10 3a 28 e0 71 85 43 a1 90 ce 54 8f 21</text>
  <text x="440" y="565" class="str">.D..:(.q.C...T.!</text>
'''
    svg += svg_footer()
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(svg)

def generate_x64dbg_view(title, badge, registers, stack_entries, threat_name, out_path, w=1100, h=620):
    svg = svg_header(f"x64dbg // [Live Process Memory Dump &amp; Thread Context] - {title}", badge, w, h)
    
    # Left Pane: Disassembly & Registers
    svg += f'''
  <!-- Registers Viewport -->
  <rect x="10" y="46" width="320" height="260" rx="4" class="panel"/>
  <rect x="10" y="46" width="320" height="24" fill="#131c2e" rx="4"/>
  <text x="20" y="62" class="badge" fill="#fb7185">CPU REGISTERS (x86-64 Context)</text>
'''
    y = 88
    for r, v, comm in registers:
        svg += f'  <text x="20" y="{y}" class="instr">{r}</text>\n'
        svg += f'  <text x="65" y="{y}" class="code" fill="#38bdf8">{v}</text>\n'
        if comm:
            svg += f'  <text x="200" y="{y}" class="comm">{comm}</text>\n'
        y += 20

    # Right Pane: Thread Call Stack
    svg += f'''
  <!-- Call Stack Pane -->
  <rect x="340" y="46" width="{w - 350}" height="260" rx="4" class="panel"/>
  <rect x="340" y="46" width="{w - 350}" height="24" fill="#131c2e" rx="4"/>
  <text x="350" y="62" class="badge" fill="#38bdf8">THREAD CALL STACK &amp; API HOOK TRACE</text>
'''
    y = 88
    for addr, frame, module in stack_entries:
        svg += f'  <text x="355" y="{y}" class="addr">{addr}</text>\n'
        svg += f'  <text x="475" y="{y}" class="code">{frame}</text>\n'
        svg += f'  <text x="820" y="{y}" class="badge" fill="#a855f7">{module}</text>\n'
        y += 20

    # Bottom Pane: Live Memory Hex Dump
    svg += f'''
  <!-- Live Memory Hex Dump -->
  <rect x="10" y="316" width="{w - 20}" height="260" rx="4" class="panel"/>
  <rect x="10" y="316" width="{w - 20}" height="24" fill="#131c2e" rx="4"/>
  <text x="20" y="332" class="badge" fill="#4ade80">MEMORY DUMP // VirtualAlloc Range: [0x00007FF720000000 - PAGE_EXECUTE_READWRITE]</text>
  
  <text x="25" y="360" class="addr">00007FF720000000</text>
  <text x="170" y="360" class="bytes">4D 5A 90 00 03 00 00 00 04 00 00 00 FF FF 00 00</text>
  <text x="590" y="360" class="str">MZ..............</text>
  <text x="750" y="360" class="comm">; Decrypted PE Header in Memory</text>

  <text x="25" y="380" class="addr">00007FF720000010</text>
  <text x="170" y="380" class="bytes">B8 00 00 00 00 00 00 00 40 00 00 00 00 00 00 00</text>
  <text x="590" y="380" class="str">........@.......</text>

  <text x="25" y="400" class="addr">00007FF720000020</text>
  <text x="170" y="400" class="bytes">00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00</text>
  <text x="590" y="400" class="str">................</text>

  <text x="25" y="420" class="addr">00007FF720000030</text>
  <text x="170" y="420" class="bytes">00 00 00 00 00 00 00 00 00 00 00 00 F0 00 00 00</text>
  <text x="590" y="420" class="str">................</text>

  <text x="25" y="440" class="addr">00007FF720000040</text>
  <text x="170" y="440" class="bytes">0E 1F BA 0E 00 B4 09 CD 21 B8 01 4C CD 21 54 68</text>
  <text x="590" y="440" class="str">........!..L.!Th</text>
  <text x="750" y="440" class="comm">; DOS stub execution signature</text>

  <text x="25" y="460" class="addr">00007FF720000050</text>
  <text x="170" y="460" class="bytes">69 73 20 70 72 6F 67 72 61 6D 20 63 61 6E 6E 6F</text>
  <text x="590" y="460" class="str">is program canno</text>

  <text x="25" y="480" class="addr">00007FF720000060</text>
  <text x="170" y="480" class="bytes">74 20 62 65 20 72 75 6e 20 69 6e 20 44 4F 53 20</text>
  <text x="590" y="480" class="str">t be run in DOS </text>

  <text x="25" y="500" class="addr">00007FF720000070</text>
  <text x="170" y="500" class="bytes">6D 6F 64 65 2E 0D 0D 0A 24 00 00 00 00 00 00 00</text>
  <text x="590" y="500" class="str">mode....$.......</text>

  <text x="25" y="520" class="addr">00007FF720000080</text>
  <text x="170" y="520" class="bytes">50 45 00 00 64 86 06 00 48 31 C0 48 89 C7 48 31</text>
  <text x="590" y="520" class="str">PE..d...H1.H..H1</text>
  <text x="750" y="520" class="comm">; PE Signature + Injected Shellcode</text>

  <text x="25" y="540" class="addr">00007FF720000090</text>
  <text x="170" y="540" class="bytes">D2 65 48 8B 52 60 48 8B 52 18 48 8B 52 20 48 8B</text>
  <text x="590" y="540" class="str">.eH.R`H.R.H.R H.</text>
  <text x="750" y="540" class="comm">; PEB traversal to resolve ntdll</text>
'''
    svg += svg_footer()
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(svg)

print("Writing generators for all 21 threats...")

# Definition of the 21 threats requiring extra forensic workbench captures
WORKBENCH_DATA = {
    'TF-011': {
        'name': 'Stealc',
        'sha': '8f92c10a4e8d3b7156cf389140aa41d7e23901b092834b7a126781290384aa12',
        'ida_title': 'Stealc SQLite Harvester & Browser Decryptor',
        'ida_lines': [
            {'addr': '140001840', 'bytes': '48 89 5C 24 08', 'instr': 'mov', 'args': '[rsp+8], rbx', 'comm': 'Stealc_Extract_Chrome_Vault'},
            {'addr': '140001845', 'bytes': '48 89 74 24 10', 'instr': 'mov', 'args': '[rsp+10h], rsi', 'comm': 'Save non-volatile context'},
            {'addr': '14000184A', 'bytes': '57', 'instr': 'push', 'args': 'rdi', 'comm': ''},
            {'addr': '14000184B', 'bytes': '48 83 EC 60', 'instr': 'sub', 'args': 'rsp, 60h', 'comm': 'Allocate stack frame'},
            {'addr': '14000184F', 'bytes': '48 8D 0D A0 31 00', 'instr': 'lea', 'args': 'rcx, aAppDataLocalGo', 'comm': '"%LOCALAPPDATA%\\\\Google\\\\Chrome\\\\User Data"'},
            {'addr': '140001856', 'bytes': 'E8 C5 10 00 00', 'instr': 'call', 'args': 'Resolve_Environment_Path', 'comm': 'Locate target Login Data DB'},
            {'addr': '14000185B', 'bytes': '48 8D 54 24 38', 'instr': 'lea', 'args': 'rdx, [rsp+38h]', 'comm': 'Pointer to sqlite3 db handle'},
            {'addr': '140001860', 'bytes': '41 B8 01 00 00 00', 'instr': 'mov', 'args': 'r8d, 1', 'comm': 'SQLITE_OPEN_READONLY'},
            {'addr': '140001866', 'bytes': 'FF 15 40 40 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_sqlite3_open_v2]', 'comm': 'Open credentials database'},
            {'addr': '14000186C', 'bytes': '85 C0', 'instr': 'test', 'args': 'eax, eax', 'comm': 'Check SQLITE_OK'},
            {'addr': '14000186E', 'bytes': '75 42', 'instr': 'jnz', 'args': 'short loc_1400018B2', 'comm': 'Jump on lock/failure'},
            {'addr': '140001870', 'bytes': '48 8D 15 85 32 00', 'instr': 'lea', 'args': 'rdx, aSelectOriginUr', 'comm': '"SELECT origin_url, username_value, password_value FROM logins"'},
            {'addr': '140001877', 'bytes': '48 8B 4C 24 38', 'instr': 'mov', 'args': 'rcx, [rsp+38h]', 'comm': 'db handle'},
            {'addr': '14000187C', 'bytes': 'FF 15 58 40 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_sqlite3_prepare_v2]', 'comm': 'Compile SQL statement'},
            {'addr': '140001882', 'bytes': 'FF 15 70 40 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_CryptUnprotectData]', 'comm': 'Decrypt DPAPI Master Key (v10 format)'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.10.12', 'dst': '185.196.8.44', 'proto': 'TCP', 'len': '66', 'info': '49382 → 80 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0142', 'src': '185.196.8.44', 'dst': '192.168.10.12', 'proto': 'TCP', 'len': '66', 'info': '80 → 49382 [SYN, ACK] Seq=0 Ack=1 Win=29200'},
            {'no': '3', 'time': '0.0145', 'src': '192.168.10.12', 'dst': '185.196.8.44', 'proto': 'TCP', 'len': '54', 'info': '49382 → 80 [ACK] Seq=1 Ack=1'},
            {'no': '4', 'time': '0.0210', 'src': '192.168.10.12', 'dst': '185.196.8.44', 'proto': 'HTTP', 'len': '482', 'info': 'POST /api/v1/gate.php HTTP/1.1 (HWID, System Tokens)', 'highlight': True},
            {'no': '5', 'time': '0.0890', 'src': '185.196.8.44', 'dst': '192.168.10.12', 'proto': 'HTTP', 'len': '1240', 'info': 'HTTP/1.1 200 OK (Task: Grab Chrome, Wallets, Telegram)', 'highlight': True},
            {'no': '6', 'time': '0.3412', 'src': '192.168.10.12', 'dst': '185.196.8.44', 'proto': 'HTTP', 'len': '1460', 'info': 'POST /api/v1/upload.php (Compressed ZIP Vault Archive: 42 KB)', 'highlight': True},
        ]
    },
    'TF-014': {
        'name': 'Mythic C2',
        'sha': '38ab20184c718b293041928374a901bcf829103847aa192834b71029384bc819',
        'ida_title': 'Mythic C2 Agent Tasking & JSON-RPC Dispatcher',
        'ida_lines': [
            {'addr': '140003000', 'bytes': '48 83 EC 48', 'instr': 'sub', 'args': 'rsp, 48h', 'comm': 'Mythic_Agent_Poll_Tasks'},
            {'addr': '140003004', 'bytes': '48 8D 0D C0 1A 00', 'instr': 'lea', 'args': 'rcx, szEndpoint', 'comm': '"/api/v1.4/agent_message"'},
            {'addr': '14000300B', 'bytes': '48 8D 15 F5 1A 00', 'instr': 'lea', 'args': 'rdx, aPayloadUUID', 'comm': '"uuid: 9b201f4c-mythic-agent-token"'},
            {'addr': '140003012', 'bytes': 'E8 40 22 00 00', 'instr': 'call', 'args': 'AES256_HMAC_Encrypt', 'comm': 'Encrypt JSON tasking envelope'},
            {'addr': '140003017', 'bytes': 'FF 15 10 50 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_WinHttpSendRequest]', 'comm': 'Transmit Mythic C2 beacon'},
            {'addr': '14000301D', 'bytes': '48 85 C0', 'instr': 'test', 'args': 'rax, rax', 'comm': 'Check HTTP Response 200 OK'},
            {'addr': '140003020', 'bytes': '74 38', 'instr': 'jz', 'args': 'short loc_RetryJitter', 'comm': 'Sleep with configurable jitter'},
            {'addr': '140003022', 'bytes': '48 8B 4C 24 30', 'instr': 'mov', 'args': 'rcx, [rsp+30h]', 'comm': 'Dissect returned JSON array: "tasks"'},
            {'addr': '140003027', 'bytes': 'E8 90 18 00 00', 'instr': 'call', 'args': 'Execute_Mythic_Subcommand', 'comm': 'Invoke: execute-assembly / socks5 / shinject'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '10.0.0.45', 'dst': '10.0.0.10', 'proto': 'TCP', 'len': '66', 'info': '52194 → 7443 [SYN] Seq=0 Win=65535'},
            {'no': '2', 'time': '0.0012', 'src': '10.0.0.10', 'dst': '10.0.0.45', 'proto': 'TLSv1.3', 'len': '198', 'info': 'Server Hello, Change Cipher Spec'},
            {'no': '3', 'time': '0.0045', 'src': '10.0.0.45', 'dst': '10.0.0.10', 'proto': 'WebSocket', 'len': '512', 'info': 'WebSocket Text Frame: {"action":"get_tasking","delegates":[]}', 'highlight': True},
            {'no': '4', 'time': '0.0120', 'src': '10.0.0.10', 'dst': '10.0.0.45', 'proto': 'WebSocket', 'len': '840', 'info': 'WebSocket Text Frame: {"tasks":[{"command":"shellcode_inject"}]}', 'highlight': True},
        ]
    },
    'TF-018': {
        'name': 'Pikabot',
        'sha': '19f82bc0148ad912847c1902834710bc829103847aa192834b71029384bc9102',
        'ida_title': 'Pikabot In-Memory Core & Process Hollowing',
        'ida_lines': [
            {'addr': '1400021A0', 'bytes': '48 83 EC 38', 'instr': 'sub', 'args': 'rsp, 38h', 'comm': 'Pikabot_Inject_SearchIndexer'},
            {'addr': '1400021A4', 'bytes': '48 8D 0D 80 12 00', 'instr': 'lea', 'args': 'rcx, aSearchIndexerE', 'comm': '"C:\\\\Windows\\\\System32\\\\searchindexer.exe"'},
            {'addr': '1400021AB', 'bytes': 'BA 04 00 00 00', 'instr': 'mov', 'args': 'edx, CREATE_SUSPENDED', 'comm': 'Flags = 0x00000004'},
            {'addr': '1400021B0', 'bytes': 'FF 15 90 60 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_CreateProcessW]', 'comm': 'Spawn target host process'},
            {'addr': '1400021B6', 'bytes': '48 8B 4C 24 20', 'instr': 'mov', 'args': 'rcx, [rsp+20h]', 'comm': 'hProcess handle'},
            {'addr': '1400021BB', 'bytes': '41 B9 40 00 00 00', 'instr': 'mov', 'args': 'r9d, PAGE_EXECUTE_READWRITE', 'comm': 'Protection mask'},
            {'addr': '1400021C1', 'bytes': 'FF 15 A0 60 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_VirtualAllocEx]', 'comm': 'Allocate RWX injection stub'},
            {'addr': '1400021C7', 'bytes': 'FF 15 B0 60 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_WriteProcessMemory]', 'comm': 'Write decrypted Pikabot payload'},
            {'addr': '1400021CD', 'bytes': 'FF 15 C0 60 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_ResumeThread]', 'comm': 'Execute in memory silently'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.18', 'dst': '104.21.34.120', 'proto': 'TCP', 'len': '66', 'info': '51920 → 443 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0210', 'src': '192.168.1.18', 'dst': '104.21.34.120', 'proto': 'TLSv1.3', 'len': '517', 'info': 'Client Hello (JA3: 771,4865-4866-4867,0-23-65281)'},
            {'no': '3', 'time': '0.0680', 'src': '104.21.34.120', 'dst': '192.168.1.18', 'proto': 'TLSv1.3', 'len': '1460', 'info': 'Server Hello, Encrypted Extensions, Certificate'},
            {'no': '4', 'time': '0.1140', 'src': '192.168.1.18', 'dst': '104.21.34.120', 'proto': 'HTTP', 'len': '890', 'info': 'POST /api/net_telemetry (AES-CBC HWID Packet)', 'highlight': True},
        ]
    },
    'TF-020': {
        'name': 'Emotet',
        'sha': '64bc0192834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'Emotet Modular State Machine & Anti-Sandbox Loop',
        'ida_lines': [
            {'addr': '140004100', 'bytes': 'FF 15 20 70 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_GetTickCount]', 'comm': 'Anti-analysis timing probe 1'},
            {'addr': '140004106', 'bytes': '89 44 24 10', 'instr': 'mov', 'args': '[rsp+10h], eax', 'comm': 'Save initial tick'},
            {'addr': '14000410A', 'bytes': 'B9 E8 03 00 00', 'instr': 'mov', 'args': 'ecx, 1000', 'comm': 'Sleep 1000ms'},
            {'addr': '14000410F', 'bytes': 'FF 15 30 70 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_Sleep]', 'comm': 'Test for sandbox fast-forwarding'},
            {'addr': '140004115', 'bytes': 'FF 15 20 70 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_GetTickCount]', 'comm': 'Anti-analysis timing probe 2'},
            {'addr': '14000411B', 'bytes': '2B 44 24 10', 'instr': 'sub', 'args': 'eax, [rsp+10h]', 'comm': 'Calculate delta'},
            {'addr': '14000411F', 'bytes': '3D E8 03 00 00', 'instr': 'cmp', 'args': 'eax, 950', 'comm': 'Validate real hardware timer'},
            {'addr': '140004124', 'bytes': '7C 40', 'instr': 'jl', 'args': 'short loc_AbortSandbox', 'comm': 'Self-terminate if in hypervisor sandbox'},
            {'addr': '140004126', 'bytes': 'E8 80 12 00 00', 'instr': 'call', 'args': 'Emotet_Decouple_C2_List', 'comm': 'Unpack internal IP:Port matrix'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.120', 'dst': '85.209.135.14', 'proto': 'TCP', 'len': '66', 'info': '49821 → 8080 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0340', 'src': '192.168.1.120', 'dst': '85.209.135.14', 'proto': 'HTTP', 'len': '620', 'info': 'POST /data/cookie/ (ECDH Key Exchange Packet)', 'highlight': True},
            {'no': '3', 'time': '0.1120', 'src': '85.209.135.14', 'dst': '192.168.1.120', 'proto': 'HTTP', 'len': '1460', 'info': 'HTTP/1.1 200 OK (Encrypted DLL Module Payload)', 'highlight': True},
        ]
    },
    'TF-023': {
        'name': 'Akira',
        'sha': 'a810bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'Akira Ransomware ChaCha20 File Encryption Engine',
        'ida_lines': [
            {'addr': '140005200', 'bytes': '48 89 5C 24 10', 'instr': 'mov', 'args': '[rsp+10h], rbx', 'comm': 'Akira_EncryptFile_ChaCha20'},
            {'addr': '140005205', 'bytes': '48 8D 15 40 10 00', 'instr': 'lea', 'args': 'rdx, aAkiraExtension', 'comm': '".akira" extension'},
            {'addr': '14000520C', 'bytes': 'E8 20 15 00 00', 'instr': 'call', 'args': 'Generate_ChaCha20_Key', 'comm': 'Generate 256-bit symmetric stream key'},
            {'addr': '140005211', 'bytes': '48 8D 0D 80 20 00', 'instr': 'lea', 'args': 'rcx, szAkiraRSAPublicKey', 'comm': 'Hardcoded RSA-4096 Master Key'},
            {'addr': '140005218', 'bytes': 'E8 A0 19 00 00', 'instr': 'call', 'args': 'RSA_Encrypt_SymmetricKey', 'comm': 'Encrypt file key, append to footer'},
            {'addr': '14000521D', 'bytes': '48 8D 0D C0 30 00', 'instr': 'lea', 'args': 'rcx, aVssadminDelete', 'comm': '"vssadmin.exe delete shadows /all /quiet"'},
            {'addr': '140005224', 'bytes': 'FF 15 80 80 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_WinExec]', 'comm': 'Obliterate Shadow Copies'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.99', 'dst': '185.180.222.10', 'proto': 'TCP', 'len': '66', 'info': '58120 → 443 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0150', 'src': '192.168.1.99', 'dst': '185.180.222.10', 'proto': 'TLSv1.3', 'len': '410', 'info': 'Client Hello (SNI: akira-leak-portal.onion)'},
            {'no': '3', 'time': '0.0890', 'src': '192.168.1.99', 'dst': '185.180.222.10', 'proto': 'HTTP', 'len': '740', 'info': 'POST /negotiation (Victim ID, Disk Encryption Statistics)', 'highlight': True},
        ]
    },
    'TF-024': {
        'name': 'Medusa',
        'sha': 'c820bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'Medusa Ransomware AES-256 Multi-threaded Encryptor',
        'ida_lines': [
            {'addr': '140006100', 'bytes': '48 8D 0D 10 10 00', 'instr': 'lea', 'args': 'rcx, aGlobalMedusaMu', 'comm': '"Global\\\\MedusaLockerMutex"'},
            {'addr': '140006107', 'bytes': 'FF 15 10 90 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_CreateMutexW]', 'comm': 'Prevent multiple ransomware instances'},
            {'addr': '14000610D', 'bytes': 'FF 15 20 90 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_GetLastError]', 'comm': 'Check ERROR_ALREADY_EXISTS'},
            {'addr': '140006113', 'bytes': '3D B7 00 00 00', 'instr': 'cmp', 'args': 'eax, 183', 'comm': '0xB7 = Already Running'},
            {'addr': '140006118', 'bytes': '74 45', 'instr': 'jz', 'args': 'short loc_ExitMedusa', 'comm': 'Abort execution'},
            {'addr': '14000611A', 'bytes': 'E8 F0 20 00 00', 'instr': 'call', 'args': 'Enumerate_Local_Drives', 'comm': 'Scan FIXED and REMOTE drive letters'},
            {'addr': '14000611F', 'bytes': 'E8 40 25 00 00', 'instr': 'call', 'args': 'Spawn_Encryption_Threads', 'comm': 'High performance multi-threading'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.77', 'dst': '193.106.191.24', 'proto': 'TCP', 'len': '66', 'info': '53210 → 443 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0220', 'src': '192.168.1.77', 'dst': '193.106.191.24', 'proto': 'HTTP', 'len': '580', 'info': 'POST /medusa/register (Victim ID, Volume Key Token)', 'highlight': True},
        ]
    },
    'TF-025': {
        'name': 'Phobos / 8Base',
        'sha': 'd930bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'Phobos / 8Base Fast Cryptographic File Traversal',
        'ida_lines': [
            {'addr': '140007000', 'bytes': '48 8D 0D A0 15 00', 'instr': 'lea', 'args': 'rcx, aSoftwareMicroso', 'comm': '"HKCU\\\\Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run"'},
            {'addr': '140007007', 'bytes': 'FF 15 40 A0 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_RegOpenKeyExW]', 'comm': 'Open Persistence Run Key'},
            {'addr': '14000700D', 'bytes': '48 8D 15 C0 15 00', 'instr': 'lea', 'args': 'rdx, aPhobosIdFormat', 'comm': '"id[{VICTIM_ID}].[el8ba@onion].8base"'},
            {'addr': '140007014', 'bytes': 'E8 80 18 00 00', 'instr': 'call', 'args': 'AES_CBC_File_Encrypt', 'comm': 'Encrypt file headers and append marker'},
            {'addr': '140007019', 'bytes': 'E8 20 19 00 00', 'instr': 'call', 'args': 'Drop_Info_HTA_Note', 'comm': 'Launch info.hta on desktop'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.111', 'dst': '91.215.85.19', 'proto': 'TCP', 'len': '66', 'info': '59100 → 80 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0190', 'src': '192.168.1.111', 'dst': '91.215.85.19', 'proto': 'HTTP', 'len': '410', 'info': 'GET /8base/verify.php?id=PHOBOS-7A19 HTTP/1.1', 'highlight': True},
        ]
    },
    'TF-027': {
        'name': 'Bumblebee',
        'sha': 'e410bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'Bumblebee WebSocket Loader & Anti-Analysis Checks',
        'ida_lines': [
            {'addr': '140008100', 'bytes': '0F A2', 'instr': 'cpuid', 'args': '', 'comm': 'Query Hypervisor / CPU Signature'},
            {'addr': '140008102', 'bytes': '81 FA 56 4D 58 68', 'instr': 'cmp', 'args': 'edx, 68584D56h', 'comm': '"VMXh" VMware backdoor probe'},
            {'addr': '140008108', 'bytes': '74 38', 'instr': 'jz', 'args': 'short loc_AbortBumblebee', 'comm': 'Abort on virtual sandbox'},
            {'addr': '14000810A', 'bytes': '48 8D 0D E0 20 00', 'instr': 'lea', 'args': 'rcx, szWebSocketURI', 'comm': '"wss://telemetry-gateway.live/ws"'},
            {'addr': '140008111', 'bytes': 'E8 70 21 00 00', 'instr': 'call', 'args': 'Init_WebSocket_Transport', 'comm': 'Establish bidirectional C2 pipe'},
            {'addr': '140008116', 'bytes': 'E8 C0 22 00 00', 'instr': 'call', 'args': 'Inject_Cobalt_Beacon', 'comm': 'Stage Cobalt Strike into explorer.exe'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.88', 'dst': '185.220.101.5', 'proto': 'TCP', 'len': '66', 'info': '55120 → 443 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0180', 'src': '192.168.1.88', 'dst': '185.220.101.5', 'proto': 'WebSocket', 'len': '490', 'info': 'WebSocket Handshake (Upgrade: websocket)', 'highlight': True},
            {'no': '3', 'time': '0.0350', 'src': '185.220.101.5', 'dst': '192.168.1.88', 'proto': 'WebSocket', 'len': '1460', 'info': 'WebSocket Binary Frame (Reflective DLL Payload)', 'highlight': True},
        ]
    },
    'TF-030': {
        'name': 'SmokeLoader',
        'sha': 'f520bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'SmokeLoader Anti-Hooking & Decryption Loop',
        'ida_lines': [
            {'addr': '140009000', 'bytes': '65 48 8B 04 25 60 00', 'instr': 'mov', 'args': 'rax, gs:[60h]', 'comm': 'Access PEB (Process Environment Block)'},
            {'addr': '140009009', 'bytes': '0F B6 40 02', 'instr': 'movzx', 'args': 'eax, byte ptr [rax+2]', 'comm': 'PEB.BeingDebugged flag'},
            {'addr': '14000900D', 'bytes': '85 C0', 'instr': 'test', 'args': 'eax, eax', 'comm': 'Check debugger presence'},
            {'addr': '14000900F', 'bytes': '75 40', 'instr': 'jnz', 'args': 'short loc_SmokeCrash', 'comm': 'Crash process immediately if debugged'},
            {'addr': '140009011', 'bytes': 'E8 40 18 00 00', 'instr': 'call', 'args': 'ZwQueryInformationProcess', 'comm': 'Direct syscall to verify ProcessDebugPort'},
            {'addr': '140009016', 'bytes': 'E8 90 19 00 00', 'instr': 'call', 'args': 'Decrypt_Smoke_Plugins', 'comm': 'Decrypt in-memory DLL modules'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.15', 'dst': '194.87.68.10', 'proto': 'TCP', 'len': '66', 'info': '51020 → 80 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0210', 'src': '192.168.1.15', 'dst': '194.87.68.10', 'proto': 'HTTP', 'len': '412', 'info': 'POST /load/gate.php (Machine GUID, Bot Version)', 'highlight': True},
            {'no': '3', 'time': '0.0780', 'src': '194.87.68.10', 'dst': '192.168.1.15', 'proto': 'HTTP', 'len': '1460', 'info': 'HTTP/1.1 200 OK (Plugin Binary: Grabber + Miner)', 'highlight': True},
        ]
    },
    'TF-032': {
        'name': 'Brute Ratel C4',
        'sha': 'b102bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'Brute Ratel C4 Badger Indirect Syscall Stubs',
        'ida_lines': [
            {'addr': '14000A100', 'bytes': '4C 8B D1', 'instr': 'mov', 'args': 'r10, rcx', 'comm': 'Syscall argument preparation'},
            {'addr': '14000A103', 'bytes': 'B8 18 00 00 00', 'instr': 'mov', 'args': 'eax, 18h', 'comm': 'SSN = NtAllocateVirtualMemory (Windows 11)'},
            {'addr': '14000A108', 'bytes': '49 BB 00 00 00 00 7B 7F 00 00', 'instr': 'mov', 'args': 'r11, 7FFF7B000000h', 'comm': 'ntdll.dll syscall instruction address'},
            {'addr': '14000A112', 'bytes': '41 FF E3', 'instr': 'jmp', 'args': 'r11', 'comm': 'Indirect Syscall invocation (Bypasses EDR Hooks)'},
            {'addr': '14000A115', 'bytes': 'E8 60 20 00 00', 'instr': 'call', 'args': 'Ekko_Sleep_Obfuscation', 'comm': 'Encrypt Badger memory footprint during sleep'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '10.10.10.50', 'dst': '10.10.10.200', 'proto': 'TCP', 'len': '66', 'info': '58190 → 443 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0080', 'src': '10.10.10.50', 'dst': '10.10.10.200', 'proto': 'TLSv1.3', 'len': '620', 'info': 'Client Hello (Custom Malleable TLS Profile)'},
            {'no': '3', 'time': '0.0450', 'src': '10.10.10.50', 'dst': '10.10.10.200', 'proto': 'HTTP', 'len': '780', 'info': 'POST /push/notify.json (Badger Telemetry Heartbeat)', 'highlight': True},
        ]
    },
    'TF-037': {
        'name': 'PrivateLoader',
        'sha': 'c302bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'PrivateLoader GeoIP Verification & Payload Dropper',
        'ida_lines': [
            {'addr': '14000B200', 'bytes': '48 8D 0D F0 18 00', 'instr': 'lea', 'args': 'rcx, aGeoIpCheck', 'comm': '"http://ip-api.com/json"'},
            {'addr': '14000B207', 'bytes': 'FF 15 10 A0 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_InternetOpenUrlW]', 'comm': 'Fetch geolocation JSON'},
            {'addr': '14000B20D', 'bytes': 'E8 A0 19 00 00', 'instr': 'call', 'args': 'Verify_CIS_Exclusion', 'comm': 'Check country code against blacklist'},
            {'addr': '14000B212', 'bytes': '85 C0', 'instr': 'test', 'args': 'eax, eax', 'comm': '1 = Excluded Country'},
            {'addr': '14000B214', 'bytes': '75 35', 'instr': 'jnz', 'args': 'short loc_ExitPrivateLoader', 'comm': 'Immediate exit on CIS match'},
            {'addr': '14000B216', 'bytes': 'E8 40 21 00 00', 'instr': 'call', 'args': 'Download_Payload_Cluster', 'comm': 'Retrieve RedLine + SmokeLoader + Vidar'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.33', 'dst': '185.161.248.12', 'proto': 'TCP', 'len': '66', 'info': '52100 → 80 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0180', 'src': '192.168.1.33', 'dst': '185.161.248.12', 'proto': 'HTTP', 'len': '460', 'info': 'GET /config/get_tasks.php HTTP/1.1', 'highlight': True},
            {'no': '3', 'time': '0.0890', 'src': '185.161.248.12', 'dst': '192.168.1.33', 'proto': 'HTTP', 'len': '1460', 'info': 'HTTP/1.1 200 OK (Drop: %TEMP%\\\\stealer_bin.exe)', 'highlight': True},
        ]
    },
    'TF-038': {
        'name': 'SystemBC',
        'sha': 'd402bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'SystemBC SOCKS5 Reverse Proxy Handshake Loop',
        'ida_lines': [
            {'addr': '14000C100', 'bytes': '48 83 EC 28', 'instr': 'sub', 'args': 'rsp, 28h', 'comm': 'SystemBC_SOCKS5_Worker'},
            {'addr': '14000C104', 'bytes': 'BA 05 01 00 00', 'instr': 'mov', 'args': 'edx, 0105h', 'comm': 'SOCKS5 Version = 0x05, 1 Method'},
            {'addr': '14000C109', 'bytes': 'FF 15 50 B0 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_send]', 'comm': 'Transmit SOCKS5 handshake'},
            {'addr': '14000C10F', 'bytes': 'E8 60 14 00 00', 'instr': 'call', 'args': 'XOR_Encrypt_Packet', 'comm': 'Custom XOR stream key cipher'},
            {'addr': '14000C114', 'bytes': 'E8 B0 15 00 00', 'instr': 'call', 'args': 'Forward_Internal_Traffic', 'comm': 'Bridge ransomware operator into LAN'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.44', 'dst': '194.26.29.112', 'proto': 'TCP', 'len': '66', 'info': '49152 → 4001 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0210', 'src': '192.168.1.44', 'dst': '194.26.29.112', 'proto': 'SOCKS', 'len': '68', 'info': 'Connect: 192.168.1.1:445 (SMB Pivot)', 'highlight': True},
            {'no': '3', 'time': '0.0450', 'src': '194.26.29.112', 'dst': '192.168.1.44', 'proto': 'SOCKS', 'len': '64', 'info': 'Connection Succeeded (Tunnel Established)', 'highlight': True},
        ]
    },
    'TF-039': {
        'name': 'Mirai & Variants',
        'sha': 'e502bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'Mirai Botnet Telnet Dictionary Scanner (Linux ELF)',
        'ida_lines': [
            {'addr': '00012000', 'bytes': '48 89 E5', 'instr': 'mov', 'args': 'rbp, rsp', 'comm': 'mirai_scanner_init()'},
            {'addr': '00012003', 'bytes': 'BF 02 00 00 00', 'instr': 'mov', 'args': 'edi, AF_INET', 'comm': 'Create raw socket'},
            {'addr': '00012008', 'bytes': 'BE 01 00 00 00', 'instr': 'mov', 'args': 'esi, SOCK_STREAM', 'comm': 'TCP Socket'},
            {'addr': '0001200D', 'bytes': 'E8 40 10 00 00', 'instr': 'call', 'args': 'socket', 'comm': 'Syscall: socket()'},
            {'addr': '00012012', 'bytes': 'BA 17 00 00 00', 'instr': 'mov', 'args': 'edx, 23', 'comm': 'Target Port: 23 (Telnet) & 2323'},
            {'addr': '00012017', 'bytes': 'E8 90 12 00 00', 'instr': 'call', 'args': 'scanner_try_creds', 'comm': 'Brute force: admin/admin, root/123456, default/root'},
            {'addr': '0001201C', 'bytes': 'E8 C0 14 00 00', 'instr': 'call', 'args': 'attack_udp_flood', 'comm': 'High volume amplification flood engine'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.200', 'dst': '71.18.99.14', 'proto': 'TCP', 'len': '60', 'info': '41200 → 23 [SYN] Seq=0 Win=14600'},
            {'no': '2', 'time': '0.0240', 'src': '192.168.1.200', 'dst': '71.18.99.14', 'proto': 'TELNET', 'len': '82', 'info': 'Data: admin\\npassword123\\n', 'highlight': True},
            {'no': '3', 'time': '0.0510', 'src': '192.168.1.200', 'dst': '185.100.85.1', 'proto': 'UDP', 'len': '1460', 'info': 'UDP Flood [Len: 1460, Attack Vector: DNS-AMP]', 'highlight': True},
        ]
    },
    'TF-040': {
        'name': 'Mozi Botnet',
        'sha': 'f602bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'Mozi P2P DHT Peer Synchronization & ECDSA Verifier',
        'ida_lines': [
            {'addr': '00014100', 'bytes': '55', 'instr': 'push', 'args': 'rbp', 'comm': 'mozi_dht_find_node()'},
            {'addr': '00014101', 'bytes': '48 89 E5', 'instr': 'mov', 'args': 'rbp, rsp', 'comm': ''},
            {'addr': '00014104', 'bytes': '48 8D 3D A0 20 00', 'instr': 'lea', 'args': 'rdi, aDhtQueryPing', 'comm': '"d1:ad2:id20:[20_BYTE_PEER_ID]e1:q4:ping1:t2:001:y1:qe"'},
            {'addr': '0001410B', 'bytes': 'E8 60 11 00 00', 'instr': 'call', 'args': 'bencode_serialize', 'comm': 'Format standard Kademlia DHT packet'},
            {'addr': '00014110', 'bytes': 'E8 B0 13 00 00', 'instr': 'call', 'args': 'verify_ecdsa_signature', 'comm': 'Validate signed bot command payload'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.210', 'dst': '112.85.42.19', 'proto': 'UDP', 'len': '124', 'info': 'DHT Query: find_node (Target: 8a7f90c1...)'},
            {'no': '2', 'time': '0.0320', 'src': '112.85.42.19', 'dst': '192.168.1.210', 'proto': 'UDP', 'len': '256', 'info': 'DHT Response: nodes=[Peer Cluster: 8 Nodes]', 'highlight': True},
            {'no': '3', 'time': '0.0890', 'src': '192.168.1.210', 'dst': '112.85.42.19', 'proto': 'HTTP', 'len': '512', 'info': 'POST /mozi.m (Payload Propagation)', 'highlight': True},
        ]
    },
    'TF-041': {
        'name': 'Meduza Stealer',
        'sha': 'a702bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'Meduza Stealer Browser & Extension Key Grabber',
        'ida_lines': [
            {'addr': '14000D000', 'bytes': '48 89 5C 24 08', 'instr': 'mov', 'args': '[rsp+8], rbx', 'comm': 'Meduza_Scan_Wallets'},
            {'addr': '14000D005', 'bytes': '48 8D 0D C0 10 00', 'instr': 'lea', 'args': 'rcx, aMetaMaskExt', 'comm': '"nkbihfbeogaeaoehlefnkodbefgpgknn" (MetaMask)'},
            {'addr': '14000D00C', 'bytes': 'E8 50 18 00 00', 'instr': 'call', 'args': 'Extract_IndexedDB_Vault', 'comm': 'Extract wallet seed phrases and keystores'},
            {'addr': '14000D011', 'bytes': '48 8D 0D F0 10 00', 'instr': 'lea', 'args': 'rcx, aTelegramSession', 'comm': '"%APPDATA%\\\\Telegram Desktop\\\\tdata"'},
            {'addr': '14000D018', 'bytes': 'E8 90 19 00 00', 'instr': 'call', 'args': 'Exfiltrate_Zipped_Bundle', 'comm': 'Compress and upload encrypted archive'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.14', 'dst': '193.106.191.88', 'proto': 'TCP', 'len': '66', 'info': '54120 → 443 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0210', 'src': '192.168.1.14', 'dst': '193.106.191.88', 'proto': 'HTTP', 'len': '780', 'info': 'POST /c2/client_log (Decrypted Wallets + Passwords)', 'highlight': True},
        ]
    },
    'TF-042': {
        'name': 'RisePro',
        'sha': 'b802bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'RisePro InfoStealer Decryption & TCP Exfiltration',
        'ida_lines': [
            {'addr': '14000E100', 'bytes': '48 83 EC 38', 'instr': 'sub', 'args': 'rsp, 38h', 'comm': 'RisePro_C2_Connect'},
            {'addr': '14000E104', 'bytes': 'BA 38 C5 00 00', 'instr': 'mov', 'args': 'edx, 50500', 'comm': 'Port: 50500'},
            {'addr': '14000E109', 'bytes': 'FF 15 10 B0 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_connect]', 'comm': 'Direct non-HTTP TCP Socket'},
            {'addr': '14000E10F', 'bytes': 'E8 40 12 00 00', 'instr': 'call', 'args': 'Encrypt_RC4_Header', 'comm': 'Package tokens, Discord credentials'},
            {'addr': '14000E114', 'bytes': 'FF 15 20 B0 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_send]', 'comm': 'Transmit structured binary stream'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.55', 'dst': '194.26.29.112', 'proto': 'TCP', 'len': '66', 'info': '50120 → 50500 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0150', 'src': '192.168.1.55', 'dst': '194.26.29.112', 'proto': 'RisePro', 'len': '1460', 'info': 'Encrypted Credential Stream [Len: 1460, Tokens: 42]', 'highlight': True},
        ]
    },
    'TF-043': {
        'name': 'BunnyLoader',
        'sha': 'c902bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'BunnyLoader In-Memory Stager & Clipper Hook',
        'ida_lines': [
            {'addr': '14000F200', 'bytes': '48 8D 0D A0 11 00', 'instr': 'lea', 'args': 'rcx, aBtcRegex', 'comm': '"^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$"'},
            {'addr': '14000F207', 'bytes': 'E8 60 14 00 00', 'instr': 'call', 'args': 'Hook_Clipboard_API', 'comm': 'Install SetClipboardViewer hook'},
            {'addr': '14000F20C', 'bytes': 'E8 B0 15 00 00', 'instr': 'call', 'args': 'Replace_Bitcoin_Address', 'comm': 'Hijack crypto paste buffer'},
            {'addr': '14000F211', 'bytes': 'E8 40 18 00 00', 'instr': 'call', 'args': 'Fetch_Payload_From_Panel', 'comm': 'Retrieve additional stealer modules'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.66', 'dst': '185.196.8.55', 'proto': 'TCP', 'len': '66', 'info': '52190 → 80 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0210', 'src': '192.168.1.66', 'dst': '185.196.8.55', 'proto': 'HTTP', 'len': '520', 'info': 'POST /bunny/api/tasks.php (Bot Register)', 'highlight': True},
        ]
    },
    'TF-044': {
        'name': 'Latrodectus',
        'sha': 'd102bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'Latrodectus FNV-1a Hash Resolver & Downloader',
        'ida_lines': [
            {'addr': '140010100', 'bytes': '8B 44 24 08', 'instr': 'mov', 'args': 'eax, [rsp+8]', 'comm': 'Latrodectus_Resolve_API_FNV1a'},
            {'addr': '140010104', 'bytes': '35 84 22 22 81', 'instr': 'xor', 'args': 'eax, 81222284h', 'comm': 'FNV prime initialization'},
            {'addr': '140010109', 'bytes': '69 C0 93 01 00 01', 'instr': 'imul', 'args': 'eax, eax, 1000193h', 'comm': 'Hash loop for ntdll functions'},
            {'addr': '14001010F', 'bytes': 'E8 80 18 00 00', 'instr': 'call', 'args': 'RC4_Decrypt_C2_Domain', 'comm': 'Unmask command server address'},
            {'addr': '140010114', 'bytes': 'E8 D0 19 00 00', 'instr': 'call', 'args': 'Send_Registration_POST', 'comm': 'Register infected node'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.19', 'dst': '141.98.11.45', 'proto': 'TCP', 'len': '66', 'info': '53820 → 443 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0240', 'src': '192.168.1.19', 'dst': '141.98.11.45', 'proto': 'HTTP', 'len': '640', 'info': 'POST /files/register.php (RC4 Encrypted OS Profile)', 'highlight': True},
        ]
    },
    'TF-045': {
        'name': 'StrelaStealer',
        'sha': 'e202bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'StrelaStealer Outlook & Thunderbird Extraction',
        'ida_lines': [
            {'addr': '140011000', 'bytes': '48 8D 0D E0 12 00', 'instr': 'lea', 'args': 'rcx, aOutlookRegistry', 'comm': '"Software\\\\Microsoft\\\\Office\\\\16.0\\\\Outlook\\\\Profiles"'},
            {'addr': '140011007', 'bytes': 'FF 15 10 B0 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_RegOpenKeyExW]', 'comm': 'Read Outlook Mail Settings'},
            {'addr': '14001100D', 'bytes': '48 8D 0D 10 13 00', 'instr': 'lea', 'args': 'rcx, aThunderbirdProfiles', 'comm': '"%APPDATA%\\\\Thunderbird\\\\Profiles\\\\*.default"'},
            {'addr': '140011014', 'bytes': 'E8 60 18 00 00', 'instr': 'call', 'args': 'Extract_Key4_Db', 'comm': 'Extract master password & key4.db'},
            {'addr': '140011019', 'bytes': 'E8 B0 19 00 00', 'instr': 'call', 'args': 'Exfiltrate_Email_Credentials', 'comm': 'Base64 HTTP POST to C2 server'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.91', 'dst': '185.161.248.88', 'proto': 'TCP', 'len': '66', 'info': '51900 → 80 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0190', 'src': '192.168.1.91', 'dst': '185.161.248.88', 'proto': 'HTTP', 'len': '580', 'info': 'POST /upload.php (Outlook SMTP/IMAP Decrypted Keys)', 'highlight': True},
        ]
    },
    'TF-046': {
        'name': 'HijackLoader',
        'sha': 'f302bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'HijackLoader DLL Search-Order & Hollower',
        'ida_lines': [
            {'addr': '140012100', 'bytes': '48 8D 0D C0 10 00', 'instr': 'lea', 'args': 'rcx, aLegitDllName', 'comm': '"version.dll" (DLL Search Order Hijack)'},
            {'addr': '140012107', 'bytes': 'E8 50 14 00 00', 'instr': 'call', 'args': 'Load_Payload_From_Overlay', 'comm': 'Extract shellcode hidden in PE overlay'},
            {'addr': '14001210C', 'bytes': '48 8D 0D F0 10 00', 'instr': 'lea', 'args': 'rcx, aSvchostExe', 'comm': '"C:\\\\Windows\\\\System32\\\\svchost.exe"'},
            {'addr': '140012113', 'bytes': 'E8 90 16 00 00', 'instr': 'call', 'args': 'Early_Bird_APC_Injection', 'comm': 'QueueUserAPC injection into suspended thread'},
            {'addr': '140012118', 'bytes': 'FF 15 20 A0 00 00', 'instr': 'call', 'args': 'qword ptr [__imp_ResumeThread]', 'comm': 'Trigger shellcode execution'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.28', 'dst': '194.26.29.99', 'proto': 'TCP', 'len': '66', 'info': '54100 → 443 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0220', 'src': '192.168.1.28', 'dst': '194.26.29.99', 'proto': 'HTTP', 'len': '490', 'info': 'GET /stream/stage2.bin (Encrypted Payload Block)', 'highlight': True},
        ]
    },
    'TF-047': {
        'name': 'RustBucket',
        'sha': 'a402bc92834b71029384bc81902834710bc829103847aa192834b71029384bc9',
        'ida_title': 'RustBucket macOS ARM64 Objective-C Stager',
        'ida_lines': [
            {'addr': '0000000100004100', 'bytes': 'FD 7B BE A9', 'instr': 'stp', 'args': 'x29, x30, [sp, #-32]!', 'comm': 'RustBucket_Init_ARM64'},
            {'addr': '0000000100004104', 'bytes': 'FD 03 00 91', 'instr': 'mov', 'args': 'x29, sp', 'comm': ''},
            {'addr': '0000000100004108', 'bytes': 'E0 03 1F 2A', 'instr': 'mov', 'args': 'w0, wzr', 'comm': 'Query LaunchServices / macOS Version'},
            {'addr': '000000010000410C', 'bytes': '00 00 00 94', 'instr': 'bl', 'args': '_objc_msgSend', 'comm': '[NSWorkspace sharedWorkspace]'},
            {'addr': '0000000100004110', 'bytes': '00 00 00 94', 'instr': 'bl', 'args': 'drop_fake_pdf_lure', 'comm': 'Display decoy internal advisory document'},
            {'addr': '0000000100004114', 'bytes': '00 00 00 94', 'instr': 'bl', 'args': 'beacon_c2_https', 'comm': 'Lazarus C2 beacon over HTTPS'},
        ],
        'pkts': [
            {'no': '1', 'time': '0.0000', 'src': '192.168.1.102', 'dst': '172.67.180.22', 'proto': 'TCP', 'len': '66', 'info': '51920 → 443 [SYN] Seq=0 Win=64240'},
            {'no': '2', 'time': '0.0180', 'src': '192.168.1.102', 'dst': '172.67.180.22', 'proto': 'TLSv1.3', 'len': '520', 'info': 'Client Hello (macOS Sonoma Darwin/23.4.0)'},
            {'no': '3', 'time': '0.0650', 'src': '192.168.1.102', 'dst': '172.67.180.22', 'proto': 'HTTP', 'len': '680', 'info': 'POST /gate/query.php (System UUID, Hardware Model)', 'highlight': True},
        ]
    }
}

generated_count = 0
for tid, info in WORKBENCH_DATA.items():
    prefix = tid.lower().replace('-', '_')
    threat_slug = info['name'].lower().split()[0].replace('/', '').replace('&', '')
    
    # 1. IDA Pro Disassembly Capture
    ida_filename = f"{threat_slug}_02_decompiler.svg"
    ida_path = os.path.join(IMAGES_DIR, ida_filename)
    generate_ida_view(info['ida_title'], f"IDA PRO // {tid} - {info['name'].upper()}", info['ida_lines'], info['name'], info['sha'], ida_path)
    generated_count += 1
    
    # 2. Wireshark Network Capture or x64dbg Memory Dump
    if 'pkts' in info:
        net_filename = f"{threat_slug}_03_traffic.svg"
        net_path = os.path.join(IMAGES_DIR, net_filename)
        generate_wireshark_view(f"{info['name']} C2 Telemetry Stream", f"WIRESHARK // {tid} - {info['name'].upper()}", info['pkts'], info['name'], net_path)
        generated_count += 1

print(f"SUCCESS: Generated {generated_count} high-resolution forensic workbench captures in {IMAGES_DIR}!")
