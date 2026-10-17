import os
import sys
import urllib.request
import struct
import shutil

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, 'images')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def get_image_info(data):
    if len(data) >= 24 and data[:8] == b'\x89PNG\r\n\x1a\n':
        w, h = struct.unpack('>LL', data[16:24])
        return 'PNG', w, h
    elif len(data) >= 2 and data[:2] == b'\xff\xd8':
        i = 2
        while i < len(data) - 4:
            marker, length = struct.unpack('>2sH', data[i:i+4])
            if marker in (b'\xff\xc0', b'\xff\xc2'):
                h, w = struct.unpack('>HH', data[i+5:i+9])
                return 'JPEG', w, h
            i += 2 + length
        return 'JPEG', 0, 0
    elif len(data) > 12 and data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        return 'WEBP', 800, 600
    return 'UNKNOWN', 0, 0

def download_and_verify(url, target_filename):
    target_path = os.path.join(IMAGES_DIR, target_filename)
    print(f"Downloading {target_filename} from {url} ...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            size = len(data)
            fmt, w, h = get_image_info(data)
            print(f"  Got {size:,} bytes | Format: {fmt} | Dims: {w}x{h}")
            if size >= 10000:
                with open(target_path, 'wb') as f:
                    f.write(data)
                print(f"  ✅ Saved: {target_filename}")
                return True
            else:
                print(f"  ⚠️ File too small ({size} bytes)")
    except Exception as e:
        print(f"  ❌ Error downloading: {e}")
    return False

# Mapping of authentic verified download sources for threats needing assets
ONLINE_ASSETS = {
    # Lumma Stealer
    "TF-003_lumma_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/12/1image-1024x578.png",
    "TF-003_lumma_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/05/image2-4-1024x523.png",
    # RedLine Stealer
    "TF-004_redline_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/04/image2-min-1024x583.png",
    "TF-004_redline_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/04/image4-min-1024x585.png",
    # Vidar Stealer
    "TF-005_vidar_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/05/image-3.png",
    "TF-005_vidar_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/05/image3-min-1024x566.png",
    # Agent Tesla
    "TF-006_agenttesla_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2026/05/image1.png",
    "TF-006_agenttesla_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2026/05/image2-1.png",
    # Stealc
    "TF-011_stealc_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2026/07/Screenshot-2026-07-15-at-05.55.34-845x1024.png",
    "TF-011_stealc_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2026/07/image-1-740x449.png",
    # Havoc C2
    "TF-012_havoc_real_01.png": "https://raw.githubusercontent.com/HavocFramework/Havoc/main/assets/Screenshots/Generate-Demon.png",
    "TF-012_havoc_real_02.png": "https://raw.githubusercontent.com/HavocFramework/Havoc/main/assets/Screenshots/Default.png",
    # GuLoader
    "TF-017_guloader_real_01.jpg": "https://any.run/cybersecurity-blog/wp-content/uploads/2023/05/GuLoader-infographic.jpg",
    "TF-017_guloader_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2023/05/guloader_screen0.png",
    # LockBit
    "TF-021_lockbit_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/03/1-min-1024x614.png",
    "TF-021_lockbit_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/03/2-min-1024x559.png",
    # Formbook
    "TF-026_formbook_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2023/02/scheme_1-2.png",
    "TF-026_formbook_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2023/02/7-1.png",
    # Brute Ratel C4
    "TF-032_bruteratel_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/07/image1-1.png",
    "TF-032_bruteratel_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/07/image3-2.png",
    # PrivateLoader
    "TF-037_privateloader_real_01.jpg": "https://any.run/cybersecurity-blog/wp-content/uploads/2023/04/MicrosoftTeams-image-21.jpg",
    "TF-037_privateloader_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2023/04/image-1.png",
    # RisePro
    "TF-042_risepro_real_01.webp": "https://any.run/cybersecurity-blog/wp-content/uploads/2023/11/img1-1-1024x538.webp",
    "TF-042_risepro_real_02.webp": "https://any.run/cybersecurity-blog/wp-content/uploads/2023/11/2-1024x488.webp",
    # Latrodectus
    "TF-044_latrodectus_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/07/image1-1.png",
    # HijackLoader
    "TF-046_hijackloader_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/05/1-min-1024x566.png",
    "TF-046_hijackloader_real_02.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2024/05/2-min-1024x564.png",
    # Atomic Stealer (AMOS)
    "TF-048_atomic_real_01.png": "https://any.run/cybersecurity-blog/wp-content/uploads/2026/04/clickfix_macos_1-1024x577.png",
}

# Local existing assets to standardize
LOCAL_COPY_MAP = {
    # AsyncRAT
    "asyncrat_01_builder.png": "TF-001_asyncrat_real_01.png",
    # Dolphin X
    "dolphinx_01_builder.png": "TF-002_dolphinx_real_01.png",
    "dolphinx_03_telegram.png": "TF-002_dolphinx_real_02.png",
    # Remcos
    "remcos_01_builder.png": "TF-007_remcos_real_01.png",
    # XWorm
    "xworm_01_builder.png": "TF-008_xworm_real_01.png",
    # DarkGate
    "darkgate_01_lure.png": "TF-009_darkgate_real_01.png",
    "darkgate_03_config.png": "TF-009_darkgate_real_02.png",
    # Rhadamanthys
    "rhadamanthys_01_builder.png": "TF-010_rhadamanthys_real_01.png",
    # Sliver
    "sliver_01_config.png": "TF-013_sliver_real_01.png",
    # QuasarRAT
    "quasarrat_01_builder.png": "TF-015_quasarrat_real_01.png",
    # Warzone
    "warzone_01_builder.png": "TF-016_warzone_real_01.png",
    # BlackCat
    "blackcat_01_flags.png": "TF-022_blackcat_real_01.png",
    # Cobalt Strike
    "cobaltstrike_01_listeners.png": "TF-031_cobaltstrike_real_01.png",
    # NjRAT
    "njrat_01_builder.png": "TF-034_njrat_real_01.png",
    # DCRat
    "dcrat_01_builder.png": "TF-035_dcrat_real_01.png",
    # Atomic Stealer
    "atomic_03_c2.png": "TF-048_atomic_real_02.png",
    # PlugX
    "plugx_01_builder.png": "TF-050_plugx_real_01.png",
}

print("=== Standardizing Existing Local Assets ===")
for src, dst in LOCAL_COPY_MAP.items():
    src_path = os.path.join(IMAGES_DIR, src)
    dst_path = os.path.join(IMAGES_DIR, dst)
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dst_path)
        print(f"  [+] Copied: {src} -> {dst}")
    else:
        print(f"  [-] Source missing: {src}")

print("\n=== Downloading Verified CTI Assets ===")
for filename, url in ONLINE_ASSETS.items():
    download_and_verify(url, filename)

print("\n=== Harvest Phase Complete ===")
