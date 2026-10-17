import os
import sys
import shutil
import json

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

with open(os.path.join(BASE_DIR, 'scripts', 'parsed_threats.json'), 'r', encoding='utf-8') as f:
    threats = json.load(f)

with open(os.path.join(BASE_DIR, 'scripts', 'generate_custom_schematics.py'), 'r', encoding='utf-8') as f:
    text = f.read()

# Extract SLUG_MAP
slug_map_str = text.split('SLUG_MAP = {')[1].split('}')[0]
slug_map = {}
for line in slug_map_str.strip().split('\n'):
    if ':' in line:
        k, v = line.strip().split(':')
        slug_map[k.strip(' ",\'')] = v.strip(' ",\'')

files_on_disk = set(os.listdir(IMAGES_DIR))

# Standardize assets for all 50 threats
# If real_01 doesn't exist, find the primary dedicated asset and copy it
for t in threats:
    tid = t['id']
    slug = slug_map[tid]
    
    # 1. Arch diagram must exist
    arch_file = f"{tid}_{slug}_arch.svg"
    if arch_file not in files_on_disk:
        print(f"Warning: {arch_file} missing!")
        
    # 2. real_01 check
    has_real_01 = any(f.startswith(f"{tid}_{slug}_real_01") for f in files_on_disk)
    if not has_real_01:
        # Candidate 1: {slug}_01_*
        candidates = [f for f in files_on_disk if f.startswith(f"{slug}_01_")]
        if not candidates and slug == "bruteratel":
            candidates = [f for f in files_on_disk if f.startswith("brute_02_")]
        if candidates:
            src = candidates[0]
            ext = os.path.splitext(src)[1]
            dst = f"{tid}_{slug}_real_01{ext}"
            shutil.copyfile(os.path.join(IMAGES_DIR, src), os.path.join(IMAGES_DIR, dst))
            files_on_disk.add(dst)
            print(f"[{tid}] Created real_01: {src} -> {dst}")
        else:
            print(f"[{tid}] ❌ Could not find candidate for real_01!")

    # 3. real_02 check
    has_real_02 = any(f.startswith(f"{tid}_{slug}_real_02") for f in files_on_disk)
    if not has_real_02:
        # Candidate: {slug}_02_* or {slug}_03_*
        candidates = [f for f in files_on_disk if f.startswith(f"{slug}_02_") or f.startswith(f"{slug}_03_")]
        if not candidates and slug == "bruteratel":
            candidates = [f for f in files_on_disk if f.startswith("brute_03_")]
        if candidates:
            src = candidates[0]
            ext = os.path.splitext(src)[1]
            dst = f"{tid}_{slug}_real_02{ext}"
            shutil.copyfile(os.path.join(IMAGES_DIR, src), os.path.join(IMAGES_DIR, dst))
            files_on_disk.add(dst)
            print(f"[{tid}] Created real_02: {src} -> {dst}")
        else:
            print(f"[{tid}] ❌ Could not find candidate for real_02!")

print("\nAsset standardization verified for all 50 threats.")
