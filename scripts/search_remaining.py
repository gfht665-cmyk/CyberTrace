import urllib.request
import urllib.parse
import re
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

remaining_threats = [
    ("TF-005", "Vidar", "vidar"),
    ("TF-014", "Mythic C2", "mythic"),
    ("TF-018", "Pikabot", "pikabot"),
    ("TF-019", "Qakbot", "qakbot"),
    ("TF-020", "Emotet", "emotet"),
    ("TF-023", "Akira", "akira"),
    ("TF-024", "Medusa", "medusa"),
    ("TF-025", "Phobos", "phobos"),
    ("TF-027", "Bumblebee", "bumblebee"),
    ("TF-028", "IcedID", "icedid"),
    ("TF-029", "DanaBot", "danabot"),
    ("TF-030", "SmokeLoader", "smokeloader"),
    ("TF-033", "NetSupport", "netsupport"),
    ("TF-036", "PureCrypter", "purecrypter"),
    ("TF-038", "SystemBC", "systembc"),
    ("TF-039", "Mirai", "mirai"),
    ("TF-040", "Mozi", "mozi"),
    ("TF-041", "Meduza", "meduza"),
    ("TF-043", "BunnyLoader", "bunnyloader"),
    ("TF-045", "StrelaStealer", "strelastealer"),
    ("TF-047", "RustBucket", "rustbucket"),
    ("TF-049", "ShadowPad", "shadowpad"),
]

print("Searching ANY.RUN search API for remaining threats...")
results = {}

for tid, name, kw in remaining_threats:
    url = f"https://any.run/cybersecurity-blog/?s={urllib.parse.quote(kw)}"
    req = urllib.request.Request(url, headers=headers)
    found = []
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            articles = re.findall(r'<h2 class="entry-title[^"]*"><a href="([^"]+)"[^>]*>([^<]+)</a>', html)
            for a_url, title in articles:
                found.append((a_url, title.strip()))
    except Exception as e:
        pass
    results[tid] = (name, found)
    print(f"[{tid}] {name:<15}: {len(found)} articles found")
    for u, t in found[:2]:
        print(f"      {t} -> {u}")
    time.sleep(0.3)

import json
with open(r'c:\Users\bad\Desktop\مجلد جديد\CyberTrace-Platform\scripts\remaining_search_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)
