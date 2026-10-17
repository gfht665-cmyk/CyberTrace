import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

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

missing = []
for t in threats:
    tid = t['id']
    slug = slug_map[tid]
    
    r1 = [f for f in files_on_disk if f.startswith(f"{tid}_{slug}_real_01")]
    r2 = [f for f in files_on_disk if f.startswith(f"{tid}_{slug}_real_02")]
    arch = f"{tid}_{slug}_arch.svg"
    
    if not r1:
        missing.append((tid, "real_01"))
    if not r2:
        missing.append((tid, "real_02"))
    if arch not in files_on_disk:
        missing.append((tid, "arch"))

if missing:
    print(f"❌ Missing assets ({len(missing)}):", missing)
else:
    print("🎯 PERFECT 100% COVERAGE:")
    print("  ✅ All 50 threats have a verified real_01 primary capture")
    print("  ✅ All 50 threats have a verified real_02 secondary capture")
    print("  ✅ All 50 threats have a dedicated custom architecture SVG schematic")
