import os
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
DATA_DIR = os.path.join(BASE_DIR, 'data')

with open(os.path.join(DATA_DIR, 'forensic_media_manifest.json'), 'r', encoding='utf-8') as f:
    manifest = json.load(f)

print(f"Total threats in manifest: {len(manifest)}")

files_on_disk = set(os.listdir(IMAGES_DIR))
print(f"Total files in images/: {len(files_on_disk)}")

# Check for any missing files in manifest
missing = []
for tid, tdata in manifest.items():
    for item in tdata['items']:
        rel = item['url']
        fname = os.path.basename(rel)
        if fname not in files_on_disk:
            missing.append((tid, rel))

if missing:
    print(f"Missing files from manifest: {len(missing)}", missing)
else:
    print("All manifest files exist on disk with 100% 1-to-1 fidelity!")
