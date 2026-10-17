import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'c:\Users\bad\Desktop\مجلد جديد\CyberTrace-Platform'
images_dir = os.path.join(base_dir, 'images')

# List of extraneous malware names to purge
extraneous_prefixes = [
    'adwind', 'androrat', 'bandook', 'bifrost', 'bitrat', 'blackshades',
    'cerberus', 'craxsrat', 'cybergate', 'darkcomet', 'gh0strat',
    'imminentmonitor', 'luminositylink', 'nanocore', 'netwire', 'optix',
    'pandorahvnc', 'poisonivy', 'prorat', 'spynet', 'spynote',
    'subseven', 'turkojan', 'venomrat', 'xenorat'
]

print("Scanning for extraneous files in images/ ...")
removed = []
kept = []

for f in sorted(os.listdir(images_dir)):
    lower_f = f.lower()
    is_extraneous = False
    for prefix in extraneous_prefixes:
        if lower_f.startswith(prefix):
            is_extraneous = True
            break
            
    fpath = os.path.join(images_dir, f)
    if is_extraneous:
        os.remove(fpath)
        removed.append(f)
    else:
        kept.append(f)

print(f"Purged {len(removed)} extraneous images:")
for r in removed:
    print(f"  [-] Removed: {r}")

print(f"\nRemaining legitimate threat assets: {len(kept)}")
