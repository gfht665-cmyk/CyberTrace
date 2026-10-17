import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r'c:\Users\bad\Desktop\مجلد جديد\CyberTrace-Platform'
images_dir = os.path.join(base_dir, 'images')

files = sorted(os.listdir(images_dir))
print(f"Total files in images/: {len(files)}")

# Group by extension
exts = {}
for f in files:
    ext = os.path.splitext(f)[1].lower()
    exts[ext] = exts.get(ext, 0) + 1
print("Extension breakdown:", exts)

# Print all files
for i, f in enumerate(files, 1):
    fpath = os.path.join(images_dir, f)
    sz = os.path.getsize(fpath)
    print(f"{i:03d}: {f} ({sz:,} bytes)")
