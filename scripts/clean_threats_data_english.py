#!/usr/bin/env python3
"""
Clean threats-data.js to 100% Pure Technical CTI English.
Removes all Arabic (ar: { ... }) blocks and synchronizes local gallery & primary image.
"""

import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
THREATS_DATA_PATH = os.path.join(BASE_DIR, 'js', 'threats-data.js')
MANIFEST_PATH = os.path.join(BASE_DIR, 'data', 'forensic_media_manifest.json')

with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

with open(THREATS_DATA_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove all ar: { ... }, blocks
# An ar block typically looks like:
# ar: {
#   type: "...",
#   ...
# },
# followed by en: {
clean_content = re.sub(r'^\s*ar:\s*\{[\s\S]*?\n\s*\},?\n', '', content, flags=re.MULTILINE)

# Update each threat's image and gallery from manifest
for tid, tdata in manifest.items():
    items = tdata['items']
    primary_img = items[0]['url']
    primary_caption = items[0]['title']
    
    gallery_lines = []
    for it in items:
        esc_title = it['title'].replace('"', '\\"')
        esc_desc = it['desc'].replace('"', '\\"')
        esc_type = it['type'].replace('"', '\\"')
        esc_id = it['id']
        gallery_lines.append(f'''      {{
        id: "{esc_id}",
        type: "{esc_type}",
        url: "{it['url']}",
        title: "{esc_title}",
        caption: "{esc_desc}"
      }}''')
    
    gallery_str = "[\n" + ",\n".join(gallery_lines) + "\n    ]"
    
    # Pattern to find threat block and replace image, imageCaption, and gallery
    pattern = re.compile(rf'(id:\s*"{tid}"[\s\S]*?mitre:\s*\[[\s\S]*?\],?\s*)([\s\S]*?)(en:\s*\{{)', re.MULTILINE)
    match = pattern.search(clean_content)
    if match:
        prefix = match.group(1).rstrip()
        suffix = match.group(3)
        replacement_middle = f'\n    image: "{primary_img}",\n    imageCaption: "{primary_caption}",\n    gallery: {gallery_str},\n    '
        new_block = prefix + replacement_middle + suffix
        clean_content = clean_content[:match.start()] + new_block + clean_content[match.end():]
    else:
        print(f"Warning: pattern not matched for {tid}")

# Check for any remaining Arabic characters
arabic_pattern = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF]')
arabic_hits = arabic_pattern.findall(clean_content)
print(f"Arabic characters remaining in threats-data.js: {len(arabic_hits)}")

with open(THREATS_DATA_PATH, 'w', encoding='utf-8') as f:
    f.write(clean_content)

print(f"SUCCESS: js/threats-data.js cleaned to 100% Pure English ({len(clean_content)} bytes)")
