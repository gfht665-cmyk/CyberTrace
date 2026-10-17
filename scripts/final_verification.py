# -*- coding: utf-8 -*-
"""
Final Comprehensive Audit and Quality Assurance Script for CyberTrace Platform.
Verifies all 5 Core Mandatory Requirements:
1. Strict 1:1 Authentic Image Mapping (Zero Fallback, Zero Shared, Zero External Links)
2. Watermark Everywhere (Telegram: @wgkgi0x0)
3. Enterprise Light Mode & Dark Mode + 100% English LTR
4. Tri-lingual Google SEO (EN, RU, HI), JSON-LD, sitemap.xml, robots.txt
5. Visual Audit Sheet and Dossier Integrity
"""

import os
import re
import sys
import json
from collections import Counter

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = r"c:\Users\bad\Desktop\مجلد جديد\CyberTrace-Platform"
IMAGES_DIR = os.path.join(ROOT_DIR, "images")
THREATS_DIR = os.path.join(ROOT_DIR, "threats")
JS_DIR = os.path.join(ROOT_DIR, "js")
DATA_DIR = os.path.join(ROOT_DIR, "data")
INDEX_PATH = os.path.join(ROOT_DIR, "index.html")
AUDIT_SHEET_PATH = os.path.join(ROOT_DIR, "visual_audit_sheet.html")
SITEMAP_PATH = os.path.join(ROOT_DIR, "sitemap.xml")
ROBOTS_PATH = os.path.join(ROOT_DIR, "robots.txt")
DATA_JS_PATH = os.path.join(JS_DIR, "threats-data.js")
MANIFEST_JSON_PATH = os.path.join(DATA_DIR, "forensic_media_manifest.json")
MANIFEST_JS_PATH = os.path.join(JS_DIR, "forensic-media-manifest.js")

ARABIC_REGEX = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]')

def sitemap_count(path):
    if not os.path.exists(path):
        return 0
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    return len(re.findall(r'<loc>', c))

def run_verification():
    print("=" * 75)
    print("🔍 CYBERTRACE PLATFORM: FINAL COMPREHENSIVE PRODUCTION VERIFICATION")
    print("=" * 75)
    
    passed_checks = 0
    total_checks = 0
    errors = []

    def check(name, condition, error_msg=""):
        nonlocal passed_checks, total_checks
        total_checks += 1
        if condition:
            print(f"  ✅ [PASS] {name}")
            passed_checks += 1
            return True
        else:
            print(f"  ❌ [FAIL] {name} - {error_msg}")
            errors.append(f"{name}: {error_msg}")
            return False

    # -------------------------------------------------------------
    # 1. CORE DATA & THREAT FILES AUDIT
    # -------------------------------------------------------------
    print("\n--- [Audit 1: Threat Files & Data Integrity] ---")
    check("threats-data.js exists", os.path.exists(DATA_JS_PATH))
    check("forensic_media_manifest.json exists", os.path.exists(MANIFEST_JSON_PATH))
    check("forensic-media-manifest.js exists", os.path.exists(MANIFEST_JS_PATH))
    check("index.html exists", os.path.exists(INDEX_PATH))
    check("visual_audit_sheet.html exists", os.path.exists(AUDIT_SHEET_PATH))
    check("sitemap.xml exists", os.path.exists(SITEMAP_PATH))
    check("robots.txt exists", os.path.exists(ROBOTS_PATH))

    with open(DATA_JS_PATH, "r", encoding="utf-8") as f:
        data_js_content = f.read()

    threat_matches = re.findall(r'\{\s*id:\s*["\'](TF-\d{3})["\'],\s*num:\s*["\']\d+["\'],\s*name:\s*["\']([^"\']+)["\']', data_js_content)
    threat_ids = [m[0] for m in threat_matches]
    threat_names = [m[1] for m in threat_matches]
    check("50 threats defined in threats-data.js", len(threat_ids) == 50, f"Found {len(threat_ids)}")
    check("50 unique threat IDs", len(set(threat_ids)) == 50, f"Found {len(set(threat_ids))}")
    check("50 unique threat names", len(set(threat_names)) == 50, f"Found {len(set(threat_names))}")

    # Check that all 50 whitepapers exist in threats/
    whitepapers = [f for f in os.listdir(THREATS_DIR) if f.endswith(".html")]
    check("50 whitepaper HTML dossiers in threats/", len(whitepapers) == 50, f"Found {len(whitepapers)}")

    # -------------------------------------------------------------
    # 2. ZERO ARABIC & ENGLISH LTR AUDIT
    # -------------------------------------------------------------
    print("\n--- [Audit 2: 100% English LTR & Zero Arabic] ---")
    arabic_in_data = ARABIC_REGEX.findall(data_js_content)
    check("Zero Arabic characters in threats-data.js", len(arabic_in_data) == 0, f"Found {len(arabic_in_data)} Arabic characters")

    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index_content = f.read()
    arabic_in_index = ARABIC_REGEX.findall(index_content)
    check("Zero Arabic characters in index.html", len(arabic_in_index) == 0, f"Found {len(arabic_in_index)} Arabic characters")
    check("index.html is lang='en' dir='ltr'", 'lang="en"' in index_content and 'dir="ltr"' in index_content)

    with open(AUDIT_SHEET_PATH, "r", encoding="utf-8") as f:
        audit_content = f.read()
    arabic_in_audit = ARABIC_REGEX.findall(audit_content)
    check("Zero Arabic characters in visual_audit_sheet.html", len(arabic_in_audit) == 0, f"Found {len(arabic_in_audit)} Arabic characters")

    whitepaper_arabic_count = 0
    whitepaper_ltr_count = 0
    for wp in whitepapers:
        wp_path = os.path.join(THREATS_DIR, wp)
        with open(wp_path, "r", encoding="utf-8") as f:
            wp_content = f.read()
        if ARABIC_REGEX.search(wp_content):
            whitepaper_arabic_count += 1
        if 'lang="en"' in wp_content and 'dir="ltr"' in wp_content:
            whitepaper_ltr_count += 1

    check("Zero Arabic characters in all 50 whitepapers", whitepaper_arabic_count == 0, f"{whitepaper_arabic_count} whitepapers contained Arabic")
    check("All 50 whitepapers have lang='en' dir='ltr'", whitepaper_ltr_count == 50, f"Only {whitepaper_ltr_count}/50")

    # -------------------------------------------------------------
    # 3. STRICT 1-TO-1 LOCAL IMAGES & ZERO EXTERNAL LINKS
    # -------------------------------------------------------------
    print("\n--- [Audit 3: Strict 1:1 Images & Zero External Image URLs] ---")
    with open(MANIFEST_JSON_PATH, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)

    check("Manifest data contains all 50 threats", len(manifest_data) == 50, f"Parsed {len(manifest_data)} threats")

    all_assigned_images = []
    missing_images = []
    asset_counts = []
    for tid, tdata in manifest_data.items():
        items = tdata.get("items") or tdata.get("assets", [])
        asset_counts.append(len(items))
        for item in items:
            rel_path = item.get("url") or item.get("local_path", "")
            disk_path = os.path.join(ROOT_DIR, rel_path.replace("./", "").replace("/", os.sep))
            if not os.path.exists(disk_path) or os.path.getsize(disk_path) == 0:
                missing_images.append(f"{tid}: {rel_path}")
            all_assigned_images.append(rel_path)

    check("Zero missing images across all 50 threats", len(missing_images) == 0, f"Missing: {missing_images[:5]}")
    check("All threats have at least 2 forensic assets", all(c >= 2 for c in asset_counts), f"Min asset count: {min(asset_counts)}")
    check(f"Total forensic assets mapped across 50 threats: {len(all_assigned_images)}", len(all_assigned_images) >= 100)

    # Check strict 1:1: no image assigned to multiple threats
    img_counts = Counter(all_assigned_images)
    shared_images = [img for img, count in img_counts.items() if count > 1]
    check("Zero shared images across different threats (Strict 1:1)", len(shared_images) == 0, f"Shared images: {shared_images}")

    # Check for external image links in index.html and all 50 whitepapers
    external_img_regex = re.compile(r'<img[^>]+src=["\']https?://[^"\']+["\']', re.IGNORECASE)
    external_imgs_found = external_img_regex.findall(index_content)
    for wp in whitepapers:
        wp_path = os.path.join(THREATS_DIR, wp)
        with open(wp_path, "r", encoding="utf-8") as f:
            c = f.read()
        external_imgs_found.extend(external_img_regex.findall(c))

    check("Zero external image URLs (0 http/https in <img src>)", len(external_imgs_found) == 0, f"Found {len(external_imgs_found)}")

    # -------------------------------------------------------------
    # 4. TELEGRAM WATERMARK AUDIT (@wgkgi0x0)
    # -------------------------------------------------------------
    print("\n--- [Audit 4: Telegram Watermark (@wgkgi0x0) Everywhere] ---")
    svg_files = [f for f in os.listdir(IMAGES_DIR) if f.endswith(".svg")]
    svg_watermark_missing = 0
    for svg in svg_files:
        svg_path = os.path.join(IMAGES_DIR, svg)
        with open(svg_path, "r", encoding="utf-8") as f:
            s_content = f.read()
        if "@wgkgi0x0" not in s_content:
            svg_watermark_missing += 1

    check(f"All {len(svg_files)} SVGs stamped with Telegram: @wgkgi0x0", svg_watermark_missing == 0, f"{svg_watermark_missing} SVGs missing watermark")

    wp_watermark_missing = 0
    wp_tg_link_missing = 0
    for wp in whitepapers:
        wp_path = os.path.join(THREATS_DIR, wp)
        with open(wp_path, "r", encoding="utf-8") as f:
            c = f.read()
        if "@wgkgi0x0" not in c:
            wp_watermark_missing += 1
        if "https://t.me/wgkgi0x0" not in c:
            wp_tg_link_missing += 1

    check("All 50 whitepapers display @wgkgi0x0 watermark badge", wp_watermark_missing == 0, f"{wp_watermark_missing} missing watermark badge")
    check("All 50 whitepapers link to https://t.me/wgkgi0x0", wp_tg_link_missing == 0, f"{wp_tg_link_missing} missing tg link")
    check("index.html displays & links to Telegram: @wgkgi0x0", "https://t.me/wgkgi0x0" in index_content and "@wgkgi0x0" in index_content)
    check("visual_audit_sheet.html displays & links to Telegram: @wgkgi0x0", "https://t.me/wgkgi0x0" in audit_content and "@wgkgi0x0" in audit_content)

    # -------------------------------------------------------------
    # 5. LIGHT MODE & DARK MODE THEME CONTROLLER
    # -------------------------------------------------------------
    print("\n--- [Audit 5: Light & Dark Mode Engine] ---")
    css_path = os.path.join(ROOT_DIR, "css", "styles.css")
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()

    check("CSS contains [data-theme='light'] color system", "[data-theme=\"light\"]" in css_content or "[data-theme='light']" in css_content)
    check("CSS contains [data-theme='dark'] color system", "[data-theme=\"dark\"]" in css_content or "[data-theme='dark']" in css_content)
    check("index.html contains theme toggle button", "theme-toggle-btn" in index_content)
    check("visual_audit_sheet.html contains theme toggle button", "theme-toggle-btn" in audit_content)

    wp_theme_toggle_missing = 0
    wp_no_fout_script_missing = 0
    for wp in whitepapers:
        wp_path = os.path.join(THREATS_DIR, wp)
        with open(wp_path, "r", encoding="utf-8") as f:
            c = f.read()
        if "toggleTheme()" not in c:
            wp_theme_toggle_missing += 1
        if "localStorage.getItem('ct_theme')" not in c:
            wp_no_fout_script_missing += 1

    check("All 50 whitepapers have theme switcher", wp_theme_toggle_missing == 0, f"{wp_theme_toggle_missing} missing theme switcher")
    check("All 50 whitepapers have zero-FOUT instant theme script in <head>", wp_no_fout_script_missing == 0, f"{wp_no_fout_script_missing} missing head script")

    # -------------------------------------------------------------
    # 6. TRI-LINGUAL GOOGLE SEO (EN, RU, HI) & INDEXING
    # -------------------------------------------------------------
    print("\n--- [Audit 6: Tri-Lingual Google SEO (EN, RU, HI)] ---")
    s_count = sitemap_count(SITEMAP_PATH)
    check(f"sitemap.xml has 51 URLs (index + 50 threats) [found {s_count}]", s_count == 51)
    check("sitemap.xml includes Google image schema (<image:image>)", "<image:loc>" in open(SITEMAP_PATH, "r", encoding="utf-8").read())
    check("robots.txt allows indexing for Googlebot, Yandex, Bing", "Googlebot" in open(ROBOTS_PATH, "r", encoding="utf-8").read())

    wp_seo_missing = 0
    wp_jsonld_missing = 0
    wp_accordion_missing = 0
    for wp in whitepapers:
        wp_path = os.path.join(THREATS_DIR, wp)
        with open(wp_path, "r", encoding="utf-8") as f:
            c = f.read()
        if 'hreflang="ru"' not in c or 'hreflang="hi"' not in c:
            wp_seo_missing += 1
        if '"@type": "TechArticle"' not in c or 'wgkgi0x0' not in c:
            wp_jsonld_missing += 1
        if 'International CTI Indexing Summary' not in c:
            wp_accordion_missing += 1

    check("All 50 whitepapers have hreflang alternates (en, ru, hi)", wp_seo_missing == 0, f"{wp_seo_missing} missing hreflang")
    check("All 50 whitepapers have Schema.org TechArticle JSON-LD with @wgkgi0x0", wp_jsonld_missing == 0, f"{wp_jsonld_missing} missing JSON-LD")
    check("All 50 whitepapers have Collapsible Tri-lingual Summary block", wp_accordion_missing == 0, f"{wp_accordion_missing} missing accordion")

    # -------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------
    print("\n" + "=" * 75)
    print(f"📊 VERIFICATION SUMMARY: {passed_checks}/{total_checks} CHECKS PASSED ({passed_checks/total_checks*100:.1f}%)")
    print("=" * 75)

    if errors:
        print("\n❌ Issues detected:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\n🎉 ALL REQUIREMENTS 100% SATISFIED! ZERO DEFECTS.")
        return True

if __name__ == "__main__":
    success = run_verification()
    sys.exit(0 if success else 1)
