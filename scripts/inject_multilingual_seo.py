import os
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, 'index.html')
SITEMAP_PATH = os.path.join(BASE_DIR, 'sitemap.xml')
ROBOTS_PATH = os.path.join(BASE_DIR, 'robots.txt')
MANIFEST_PATH = os.path.join(BASE_DIR, 'data', 'forensic_media_manifest.json')

with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

from generate_all_whitepapers_english import FILENAME_MAPPING

# ==============================================================================
# 1. GENERATE SITEMAP.XML (WITH GOOGLE IMAGES & MULTILINGUAL HREFLANG)
# ==============================================================================
sitemap_entries = []

# Index page
sitemap_entries.append('''  <url>
    <loc>https://cybertrace.io/index.html</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://cybertrace.io/index.html"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://cybertrace.io/index.html#lang-ru"/>
    <xhtml:link rel="alternate" hreflang="hi" href="https://cybertrace.io/index.html#lang-hi"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://cybertrace.io/index.html"/>
    <lastmod>2026-10-17</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>''')

for tid, fname in FILENAME_MAPPING.items():
    tdata = manifest.get(tid, {})
    name = tdata.get('name', tid)
    items = tdata.get('items', [])
    
    img_xml_tags = ""
    for it in items:
        img_url = f"https://cybertrace.io/{it['url']}"
        img_title = it['title'].replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
        img_caption = f"{img_title} // Forensic Reverse Engineering Capture stamped Telegram @wgkgi0x0"
        img_xml_tags += f'''
    <image:image>
      <image:loc>{img_url}</image:loc>
      <image:title>{img_title}</image:title>
      <image:caption>{img_caption}</image:caption>
    </image:image>'''

    entry = f'''  <url>
    <loc>https://cybertrace.io/threats/{fname}</loc>
    <xhtml:link rel="alternate" hreflang="en" href="https://cybertrace.io/threats/{fname}"/>
    <xhtml:link rel="alternate" hreflang="ru" href="https://cybertrace.io/threats/{fname}#lang-ru"/>
    <xhtml:link rel="alternate" hreflang="hi" href="https://cybertrace.io/threats/{fname}#lang-hi"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://cybertrace.io/threats/{fname}"/>
    <lastmod>2026-10-17</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.85</priority>{img_xml_tags}
  </url>'''
    sitemap_entries.append(entry)

sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
{chr(10).join(sitemap_entries)}
</urlset>'''

with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)
print(f"✅ Generated sitemap.xml ({len(sitemap_entries)} URLs with Google Images schema)")

# ==============================================================================
# 2. GENERATE ROBOTS.TXT
# ==============================================================================
robots_txt = """# CyberTrace Defensive Threat Intelligence Platform
# Robots.txt for Global CTI Indexing (Google, Yandex, Bing)

User-agent: *
Allow: /
Allow: /images/
Allow: /threats/
Allow: /css/
Allow: /js/

User-agent: Googlebot
Allow: /
Allow: /images/
Allow: /threats/

User-agent: Googlebot-Image
Allow: /images/

User-agent: Yandex
Allow: /
Allow: /images/
Allow: /threats/

User-agent: Bingbot
Allow: /
Allow: /images/
Allow: /threats/

Sitemap: https://cybertrace.io/sitemap.xml
"""

with open(ROBOTS_PATH, 'w', encoding='utf-8') as f:
    f.write(robots_txt)
print("✅ Generated robots.txt")

# ==============================================================================
# 3. UPDATE INDEX.HTML WITH TRI-LINGUAL SEO, LIGHT MODE & TELEGRAM @wgkgi0x0
# ==============================================================================
with open(INDEX_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# Update <head>
head_replacement = '''<!DOCTYPE html>
<html lang="en" dir="ltr" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Tri-Lingual Google Search SEO Meta Tags (English, Russian, Hindi) -->
  <title>CyberTrace Defensive CTI Radar // 50 Threat Families &amp; Reverse Engineering (@wgkgi0x0)</title>
  <meta name="description" content="CyberTrace Defensive Threat Intelligence: Technical disassembly, YARA &amp; Sigma detection rules, and C2 forensic captures for 50 active malware families. Official Telegram: @wgkgi0x0">
  <meta name="keywords" content="CyberTrace, Threat Intelligence, CTI, Malware Analysis, Reverse Engineering, YARA rules, Sigma rules, C2 Architecture, RAT, Ransomware, InfoStealer, Киберразведка, Вредоносное ПО, Анализ угроз, декомпиляция C2, मैलवेयर विश्लेषण, साइबर सुरक्षा, YARA नियम">
  <meta name="author" content="CyberTrace Intelligence (@wgkgi0x0)">
  
  <!-- Multi-Lingual Alternate Hreflang Tags -->
  <link rel="canonical" href="https://cybertrace.io/index.html">
  <link rel="alternate" hreflang="en" href="https://cybertrace.io/index.html">
  <link rel="alternate" hreflang="ru" href="https://cybertrace.io/index.html#lang-ru">
  <link rel="alternate" hreflang="hi" href="https://cybertrace.io/index.html#lang-hi">
  <link rel="alternate" hreflang="x-default" href="https://cybertrace.io/index.html">
  
  <!-- OpenGraph & Twitter Cards -->
  <meta property="og:title" content="CyberTrace Threat Intelligence // 50 Active Threat Families (@wgkgi0x0)">
  <meta property="og:description" content="Defensive CTI Radar: In-depth reverse engineering, YARA detection signatures, and 100% verified local forensic captures. Telegram: @wgkgi0x0">
  <meta property="og:image" content="https://cybertrace.io/images/TF-001_asyncrat_real_01.png">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://cybertrace.io/index.html">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="CyberTrace Defensive CTI Platform">
  <meta name="twitter:description" content="Continuous surveillance and forensic disassembly of 50 active cyber threat families. Telegram: @wgkgi0x0">
  <meta name="twitter:image" content="https://cybertrace.io/images/TF-001_asyncrat_real_01.png">
  
  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "WebSite",
        "@id": "https://cybertrace.io/#website",
        "url": "https://cybertrace.io",
        "name": "CyberTrace Intelligence Platform",
        "description": "Defensive Cyber Threat Intelligence, Malware Reverse Engineering & Detection Rule Database.",
        "inLanguage": ["en", "ru", "hi"],
        "publisher": {
          "@type": "Organization",
          "name": "CyberTrace Intelligence (@wgkgi0x0)",
          "url": "https://t.me/wgkgi0x0"
        }
      },
      {
        "@type": "Organization",
        "@id": "https://cybertrace.io/#organization",
        "name": "CyberTrace Intelligence",
        "url": "https://cybertrace.io",
        "sameAs": ["https://t.me/wgkgi0x0"],
        "contactPoint": {
          "@type": "ContactPoint",
          "contactType": "threat intelligence feed",
          "url": "https://t.me/wgkgi0x0"
        }
      }
    ]
  }
  </script>
  
  <!-- Instant Theme Loader (Zero FOUT) -->
  <script>
    (function() {
      var savedTheme = localStorage.getItem('ct_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
    })();
  </script>
  
  <link rel="stylesheet" href="css/styles.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>'''

html = re.sub(r'<!DOCTYPE html>[\s\S]*?</head>', head_replacement, html, count=1)

# Update Topbar Controls (Add Theme Switcher and Telegram @wgkgi0x0)
topbar_replacement = '''        <!-- Center Badges & Status -->
        <div class="hud-telemetry">
          <div class="telemetry-node">
            <span class="status-beacon"></span>
            <span>50 Active Families (2026)</span>
          </div>
          <div class="telemetry-node">
            <span style="color: var(--color-cyan);">[VAULT]</span>
            <span>100% Offline Air-Gapped</span>
          </div>
          <div class="telemetry-node">
            <span style="color: var(--color-emerald);">[RULES]</span>
            <span>YARA &amp; Sigma Ready</span>
          </div>
          <div class="telemetry-node">
            <span style="color: var(--color-crimson);">[OPS]</span>
            <span id="utc-clock-val">--:--:-- UTC</span>
          </div>
          <div class="telemetry-node">
            <a href="visual_audit_sheet.html" style="color: var(--color-cyan); text-decoration: none; font-weight: 700; border: 1px solid rgba(6,182,212,0.4); padding: 3px 8px; border-radius: 4px; background: rgba(6,182,212,0.1);">[AUDIT MATRIX ↗]</a>
          </div>
          <div class="telemetry-node">
            <button id="theme-toggle-btn" class="theme-toggle-btn" onclick="toggleTheme()" title="Toggle Light / Dark Mode">☀️ Light</button>
          </div>
          <div class="telemetry-node">
            <a href="https://t.me/wgkgi0x0" target="_blank" rel="noopener noreferrer" class="tg-topbar-link" title="Official Telegram Feed">
              <span class="tg-icon">✈</span> Telegram: <strong>@wgkgi0x0</strong>
            </a>
          </div>
        </div>'''

html = re.sub(r'<!-- Center Badges & Status -->[\s\S]*?</div>\s*</div>\s*</div>\s*</header>', topbar_replacement + '\n      </div>\n    </div>\n  </header>', html, count=1)

# Update Footer with Telegram @wgkgi0x0
footer_replacement = '''  <!-- Tactical Footer -->
  <footer class="tactical-footer">
    <div class="cyber-container">
      <div class="footer-inner">
        <div class="footer-legal">
          <span style="font-weight: 700; color: var(--text-high);">CYBERTRACE // DEFENSIVE THREAT RESEARCH</span>
          <span>CyberTrace Intelligence Platform © 2026. Strictly educational &amp; defensive CTI telemetry.</span>
          <div class="footer-telegram-cta">
            <span class="tg-pulse-dot"></span>
            <span>Direct CTI Dispatches: <a href="https://t.me/wgkgi0x0" target="_blank" rel="noopener noreferrer" class="tg-footer-link">Telegram: @wgkgi0x0 (t.me/wgkgi0x0)</a></span>
          </div>
        </div>
        <div class="footer-social-links">
          <a href="https://t.me/wgkgi0x0" target="_blank" rel="noopener noreferrer" class="footer-link">Telegram: @wgkgi0x0</a>
          <span style="color: var(--border-medium);">•</span>
          <span class="mono" style="color: var(--color-emerald); font-size: 0.75rem;">100% AIR-GAPPED</span>
          <span style="color: var(--border-medium);">•</span>
          <span class="mono" style="color: var(--color-cyan); font-size: 0.75rem;">SHA-256 VERIFIED</span>
        </div>
      </div>
    </div>
  </footer>'''

html = re.sub(r'<!-- Tactical Footer -->[\s\S]*?</footer>', footer_replacement, html, count=1)

# Inject Multilingual Knowledge Graph Section before Footer
multilingual_section = '''
  <!-- INTERNATIONAL CTI SEARCH ENGINE INDEXING SECTION (EN | RU | HI) -->
  <section class="cyber-container" style="margin-bottom: 2.5rem;">
    <div class="whitepaper-section multilingual-index-section" style="border: 1px solid var(--border-subtle); border-radius: 8px;">
      <details class="multilingual-accordion" open>
        <summary class="multilingual-summary-header">
          <span class="globe-icon">🌐</span>
          <strong>International CTI Search Engine Indexing (EN | RU | HI)</strong>
          <span class="seo-badge">Tri-Lingual Knowledge Graph</span>
        </summary>
        <div class="multilingual-content-grid">
          <!-- English Block -->
          <div class="lang-block lang-en" id="lang-en">
            <div class="lang-tag">ENGLISH (EN) // PLATFORM OVERVIEW</div>
            <h3 class="lang-heading">CyberTrace Threat Intelligence Radar (50 Active Families)</h3>
            <p>Comprehensive enterprise repository tracking 50 premier malware families including Remote Access Trojans (AsyncRAT, Remcos, XWorm), Information Stealers (Lumma, RedLine, Vidar, Stealc), Ransomware cartels (LockBit 3.0, BlackCat, Akira), and Advanced C2 Frameworks (Cobalt Strike, Havoc, Sliver).</p>
            <p>Every threat profile incorporates validated YARA memory rules, Sigma behavioral detection logic, MITRE ATT&amp;CK mappings, and forensic screenshots stamped with <a href="https://t.me/wgkgi0x0" target="_blank" rel="noopener noreferrer">@wgkgi0x0</a>.</p>
          </div>
          <!-- Russian Block -->
          <div class="lang-block lang-ru" id="lang-ru" lang="ru">
            <div class="lang-tag">РУССКИЙ (RU) // ОБЗОР ПЛАТФОРМЫ КИБЕРРАЗВЕДКИ</div>
            <h3 class="lang-heading">Платформа киберразведки CyberTrace (50 семейств угроз)</h3>
            <p>Централизованный исследовательский центр для анализа 50 активных семейств вредоносного ПО: трояны удаленного доступа (AsyncRAT, Remcos), инфостилеры (Lumma Stealer, RedLine, Stealc), программы-вымогатели (LockBit, Akira) и командные серверы C2 (Cobalt Strike, Havoc).</p>
            <p>Каждое досье содержит декомпилированный код, структуру сетевых протоколов C2, правила YARA и Sigma для обнаружения в SIEM и EDR. Официальный канал: Telegram <a href="https://t.me/wgkgi0x0" target="_blank" rel="noopener noreferrer">@wgkgi0x0</a>.</p>
          </div>
          <!-- Hindi Block -->
          <div class="lang-block lang-hi" id="lang-hi" lang="hi">
            <div class="lang-tag">हिन्दी (HI) // साइबर इंटेलिजेंस प्लेटफॉर्म अवलोकन</div>
            <h3 class="lang-heading">CyberTrace साइबर थ्रेट इंटेलिजेंस प्लेटफॉर्म (50 मैलवेयर परिवार)</h3>
            <p>CyberTrace 50 प्रमुख साइबर खतरों का संपूर्ण विश्लेषण प्रदान करता है, जिसमें रिमोट एक्सेस ट्रोजन (RATs), इन्फोस्टीलर (Lumma, RedLine), रैंसमवेयर सिंडिकेट (LockBit, BlackCat) और कमांड और कंट्रोल (C2) फ्रेमवर्क शामिल हैं।</p>
            <p>प्रत्येक रिपोर्ट में रिवर्स इंजीनियरिंग विवरण, YARA और Sigma सुरक्षा नियम और MITRE ATT&amp;CK संकेतक शामिल हैं। आधिकारिक साइबर इंटेलिजेंस अपडेट: Telegram <a href="https://t.me/wgkgi0x0" target="_blank" rel="noopener noreferrer">@wgkgi0x0</a>.</p>
          </div>
        </div>
      </details>
    </div>
  </section>
'''

if 'INTERNATIONAL CTI SEARCH ENGINE INDEXING SECTION' not in html:
    html = html.replace('<!-- Tactical Footer -->', multilingual_section + '\n  <!-- Tactical Footer -->')

with open(INDEX_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
print("✅ Successfully updated index.html with Tri-Lingual SEO, Light/Dark Mode toggle, and Telegram @wgkgi0x0 integration!")
