import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'c:\Users\bad\Desktop\مجلد جديد\CyberTrace-Platform\scripts\anyrun_posts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

print(f"Loaded {len(posts)} posts from ANY.RUN")

threats = [
    ("TF-001", "AsyncRAT", ["asyncrat"]),
    ("TF-002", "Dolphin X", ["dolphinx", "dolphin"]),
    ("TF-003", "Lumma Stealer", ["lumma"]),
    ("TF-004", "RedLine Stealer", ["redline"]),
    ("TF-005", "Vidar Stealer", ["vidar"]),
    ("TF-006", "Agent Tesla", ["agent-tesla", "agenttesla", "tesla"]),
    ("TF-007", "Remcos RAT", ["remcos"]),
    ("TF-008", "XWorm", ["xworm"]),
    ("TF-009", "DarkGate", ["darkgate"]),
    ("TF-010", "Rhadamanthys", ["rhadamanthys"]),
    ("TF-011", "Stealc", ["stealc"]),
    ("TF-012", "Havoc C2", ["havoc"]),
    ("TF-013", "Sliver C2", ["sliver"]),
    ("TF-014", "Mythic C2", ["mythic"]),
    ("TF-015", "QuasarRAT", ["quasar", "quasarrat"]),
    ("TF-016", "Warzone RAT", ["warzone"]),
    ("TF-017", "GuLoader", ["guloader"]),
    ("TF-018", "Pikabot", ["pikabot"]),
    ("TF-019", "Qakbot", ["qakbot", "qbot"]),
    ("TF-020", "Emotet", ["emotet"]),
    ("TF-021", "LockBit", ["lockbit"]),
    ("TF-022", "BlackCat", ["blackcat", "alphv"]),
    ("TF-023", "Akira", ["akira"]),
    ("TF-024", "Medusa", ["medusa"]),
    ("TF-025", "Phobos", ["phobos", "8base"]),
    ("TF-026", "Formbook", ["formbook", "xloader"]),
    ("TF-027", "Bumblebee", ["bumblebee"]),
    ("TF-028", "IcedID", ["icedid"]),
    ("TF-029", "DanaBot", ["danabot"]),
    ("TF-030", "SmokeLoader", ["smokeloader", "smoke"]),
    ("TF-031", "Cobalt Strike", ["cobalt-strike", "cobaltstrike"]),
    ("TF-032", "Brute Ratel C4", ["brute-ratel", "bruteratel"]),
    ("TF-033", "NetSupport RAT", ["netsupport"]),
    ("TF-034", "NjRAT", ["njrat", "bladabindi"]),
    ("TF-035", "DCRat", ["dcrat"]),
    ("TF-036", "PureCrypter", ["purecrypter"]),
    ("TF-037", "PrivateLoader", ["privateloader"]),
    ("TF-038", "SystemBC", ["systembc"]),
    ("TF-039", "Mirai & Variants", ["mirai"]),
    ("TF-040", "Mozi Botnet", ["mozi"]),
    ("TF-041", "Meduza Stealer", ["meduza"]),
    ("TF-042", "RisePro", ["risepro"]),
    ("TF-043", "BunnyLoader", ["bunnyloader", "bunny"]),
    ("TF-044", "Latrodectus", ["latrodectus"]),
    ("TF-045", "StrelaStealer", ["strelastealer", "strela"]),
    ("TF-046", "HijackLoader", ["hijackloader", "idat"]),
    ("TF-047", "RustBucket", ["rustbucket"]),
    ("TF-048", "Atomic Stealer (AMOS)", ["atomic-stealer", "amos"]),
    ("TF-049", "ShadowPad", ["shadowpad"]),
    ("TF-050", "PlugX", ["plugx", "korplug"]),
]

matches = {}
for tid, name, keywords in threats:
    matched_urls = []
    for p in posts:
        for kw in keywords:
            if kw in p.lower():
                matched_urls.append(p)
                break
    matches[tid] = (name, matched_urls)
    print(f"[{tid}] {name:<22}: {len(matched_urls)} matching posts")
    if matched_urls:
        print(f"      -> {matched_urls[0]}")
