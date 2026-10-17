import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_PATH = os.path.join(BASE_DIR, 'css', 'styles.css')
JS_APP_PATH = os.path.join(BASE_DIR, 'js', 'app.js')

# --- 1. UPDATE CSS ---
with open(CSS_PATH, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace :root definition with robust Dark & Light mode definitions
theme_vars = """/**
 * CYBERTRACE ADVANCED CTI PLATFORM
 * Design System: Elite Command Center UI (Light & Dark Theme Engine)
 * Strictly calibrated for 100% LTR Technical English & Forensic Clarity
 */

:root, [data-theme="dark"] {
  /* Dark Obsidian Palette */
  --bg-deep: #07080a;
  --bg-panel: #0d0f14;
  --bg-panel-hover: #131720;
  --bg-elevated: #161b26;
  --bg-glass: rgba(13, 15, 20, 0.85);
  
  /* Borders & Dividers */
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-medium: rgba(255, 255, 255, 0.14);
  --border-active: #0284c7;

  /* Typography Colors */
  --text-high: #f3f4f6;
  --text-med: #9ca3af;
  --text-muted: #6b7280;
  --text-mono: #e5e7eb;

  /* Tactical Accents */
  --color-crimson: #ef4444;
  --color-crimson-glow: rgba(239, 68, 68, 0.18);
  --color-cyan: #06b6d4;
  --color-cyan-glow: rgba(6, 182, 212, 0.15);
  --color-emerald: #10b981;
  --color-emerald-glow: rgba(16, 185, 129, 0.15);
  --color-amber: #f59e0b;
  --color-amber-glow: rgba(245, 158, 11, 0.15);
  --color-purple: #a855f7;

  /* Card Shadows */
  --card-shadow: 0 4px 16px rgba(0, 0, 0, 0.4);
  --card-shadow-hover: 0 12px 32px rgba(0, 0, 0, 0.6);

  /* Fonts */
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: "JetBrains Mono", "SF Mono", "Fira Code", Menlo, Monaco, Consolas, monospace;

  /* Emil Kowalski Springs & Easing Curves */
  --ease-out-snappy: cubic-bezier(0.23, 1, 0.32, 1);
  --duration-fast: 160ms;
  --duration-med: 240ms;

  /* Layout Constants */
  --header-height: 68px;
  --drawer-width: 680px;
}

[data-theme="light"] {
  /* Enterprise Light Palette (CrowdStrike / Mandiant CTI Report Style) */
  --bg-deep: #f8fafc;
  --bg-panel: #ffffff;
  --bg-panel-hover: #f1f5f9;
  --bg-elevated: #ffffff;
  --bg-glass: rgba(255, 255, 255, 0.94);
  
  /* Clean Light Borders */
  --border-subtle: #e2e8f0;
  --border-medium: #cbd5e1;
  --border-active: #0284c7;

  /* High-Contrast Light Typography */
  --text-high: #0f172a;
  --text-med: #334155;
  --text-muted: #64748b;
  --text-mono: #0f172a;

  /* Tactical Accents for Light Mode */
  --color-crimson: #dc2626;
  --color-crimson-glow: rgba(220, 38, 38, 0.12);
  --color-cyan: #0284c7;
  --color-cyan-glow: rgba(2, 132, 199, 0.12);
  --color-emerald: #059669;
  --color-emerald-glow: rgba(5, 150, 105, 0.12);
  --color-amber: #d97706;
  --color-amber-glow: rgba(217, 119, 6, 0.12);
  --color-purple: #7c3aed;

  /* Clean Paper Shadows */
  --card-shadow: 0 2px 8px rgba(15, 23, 42, 0.05), 0 1px 2px rgba(15, 23, 42, 0.04);
  --card-shadow-hover: 0 10px 25px -5px rgba(15, 23, 42, 0.1), 0 8px 10px -6px rgba(15, 23, 42, 0.05);
}
"""

css = re.sub(r'/\*\*[\s\S]*?:root\s*\{[\s\S]*?--drawer-width:\s*680px;\s*\}', theme_vars, css, count=1)

extra_styles = """
/* ==========================================================================
   ENTERPRISE LIGHT MODE ENHANCEMENTS & MULTILINGUAL CTI STYLING
   ========================================================================== */

[data-theme="light"] body {
  background-color: var(--bg-deep);
  background-image: 
    radial-gradient(ellipse at 50% 0%, rgba(2, 132, 199, 0.04) 0%, transparent 60%),
    linear-gradient(to right, rgba(15, 23, 42, 0.03) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(15, 23, 42, 0.03) 1px, transparent 1px);
}

[data-theme="light"] .command-hud-header {
  background: var(--bg-glass);
  border-bottom: 1px solid var(--border-subtle);
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

[data-theme="light"] .hud-brand-name {
  color: #0f172a;
}

[data-theme="light"] .threat-card {
  background: var(--bg-panel);
  border-color: var(--border-subtle);
  box-shadow: var(--card-shadow);
}

[data-theme="light"] .threat-card:hover {
  background: var(--bg-panel);
  border-color: var(--color-cyan);
  box-shadow: var(--card-shadow-hover);
}

[data-theme="light"] .threat-card-name {
  color: #0f172a;
}

[data-theme="light"] .threat-card-summary {
  color: #475569;
}

[data-theme="light"] .threat-meta-val {
  color: #1e293b;
}

[data-theme="light"] .threat-search-bar {
  background: #ffffff;
  border-color: #cbd5e1;
  color: #0f172a;
  box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}

[data-theme="light"] .filter-pill {
  background: #ffffff;
  border-color: #cbd5e1;
  color: #475569;
}

[data-theme="light"] .filter-pill:hover,
[data-theme="light"] .filter-pill.active {
  background: #0284c7;
  color: #ffffff;
  border-color: #0284c7;
}

[data-theme="light"] .tactical-drawer {
  background: #ffffff;
  border-left-color: #cbd5e1;
  box-shadow: -8px 0 32px rgba(15, 23, 42, 0.12);
}

[data-theme="light"] .drawer-header {
  background: #f8fafc;
  border-bottom-color: #e2e8f0;
}

[data-theme="light"] .drawer-title {
  color: #0f172a;
}

[data-theme="light"] .drawer-tab {
  color: #64748b;
  border-bottom-color: transparent;
}

[data-theme="light"] .drawer-tab.active {
  color: #0284c7;
  border-bottom-color: #0284c7;
}

[data-theme="light"] .code-viewport {
  background: #0f172a;
  color: #f8fafc;
}

[data-theme="light"] .whitepaper-page {
  background-color: #f8fafc;
}

[data-theme="light"] .whitepaper-container {
  background: transparent;
}

[data-theme="light"] .whitepaper-header {
  background: #ffffff;
  border-color: #e2e8f0;
  box-shadow: var(--card-shadow);
}

[data-theme="light"] .whitepaper-title {
  color: #0f172a;
}

[data-theme="light"] .whitepaper-subtitle {
  color: #475569;
}

[data-theme="light"] .whitepaper-section {
  background: #ffffff;
  border-color: #e2e8f0;
  box-shadow: var(--card-shadow);
}

[data-theme="light"] .whitepaper-section-title {
  color: #0f172a;
  border-bottom-color: #e2e8f0;
}

[data-theme="light"] .whitepaper-prose {
  color: #334155;
}

[data-theme="light"] .infection-stage-card,
[data-theme="light"] .defense-step-card,
[data-theme="light"] .whitepaper-meta-item {
  background: #f8fafc;
  border-color: #e2e8f0;
}

[data-theme="light"] .stage-title {
  color: #0f172a;
}

[data-theme="light"] .stage-desc,
[data-theme="light"] .defense-step-text {
  color: #475569;
}

[data-theme="light"] .evidence-card {
  background: #ffffff;
  border-color: #e2e8f0;
  box-shadow: var(--card-shadow);
}

[data-theme="light"] .evidence-header {
  background: #f8fafc;
  border-bottom-color: #e2e8f0;
}

[data-theme="light"] .caption-title-en {
  color: #0f172a;
}

[data-theme="light"] .caption-desc {
  color: #475569;
}

[data-theme="light"] .whitepaper-footer {
  background: #ffffff;
  border-top-color: #e2e8f0;
  color: #64748b;
}

/* Theme Switcher Button */
.theme-toggle-btn {
  background: var(--bg-panel);
  border: 1px solid var(--border-medium);
  color: var(--text-high);
  font-family: var(--font-mono);
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  transition: all var(--duration-fast) var(--ease-out-snappy);
  user-select: none;
}

.theme-toggle-btn:hover {
  background: var(--bg-panel-hover);
  border-color: var(--color-cyan);
  transform: translateY(-1px);
}

/* Telegram Topbar & Footer CTA */
.tg-topbar-link {
  background: rgba(14, 165, 233, 0.12);
  border: 1px solid rgba(14, 165, 233, 0.4);
  color: #0284c7;
  font-family: var(--font-mono);
  font-size: 0.78rem;
  font-weight: 700;
  padding: 0.4rem 0.85rem;
  border-radius: 6px;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  transition: all var(--duration-fast) var(--ease-out-snappy);
}

[data-theme="dark"] .tg-topbar-link {
  color: #38bdf8;
}

.tg-topbar-link:hover {
  background: #0ea5e9;
  color: #ffffff;
  border-color: #38bdf8;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(14, 165, 233, 0.25);
}

.tg-icon {
  font-size: 0.85rem;
}

.footer-telegram-cta {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  font-family: var(--font-mono);
  font-size: 0.85rem;
  color: var(--text-med);
  margin-top: 0.75rem;
}

.tg-footer-link {
  color: var(--color-cyan);
  text-decoration: none;
  font-weight: 700;
}

.tg-footer-link:hover {
  text-decoration: underline;
}

.tg-pulse-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background-color: #0ea5e9;
  box-shadow: 0 0 8px #0ea5e9;
  animation: pulseBeacon 2s infinite;
}

/* Evidence Watermark Badge */
.evidence-watermark-meta {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 6px 12px;
  background: var(--bg-deep);
  border-top: 1px solid var(--border-subtle);
  font-family: var(--font-mono);
  font-size: 0.7rem;
}

.wm-stamp {
  color: var(--color-emerald);
  font-weight: 800;
  letter-spacing: 0.05em;
}

.wm-author {
  color: var(--color-cyan);
  text-decoration: none;
  font-weight: 700;
}

.wm-author:hover {
  text-decoration: underline;
}

/* Multilingual Search Indexing Section */
.multilingual-index-section {
  padding: 0 !important;
  overflow: hidden;
}

.multilingual-accordion {
  border-radius: 8px;
}

.multilingual-summary-header {
  padding: 18px 24px;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--bg-panel-hover);
  user-select: none;
  font-family: var(--font-mono);
  font-size: 0.95rem;
  color: var(--text-high);
}

.multilingual-summary-header:hover {
  background: var(--bg-elevated);
}

.globe-icon {
  font-size: 1.2rem;
}

.seo-badge {
  margin-left: auto;
  font-size: 0.7rem;
  color: var(--color-cyan);
  background: rgba(6, 182, 212, 0.1);
  border: 1px solid rgba(6, 182, 212, 0.3);
  padding: 2px 8px;
  border-radius: 4px;
  text-transform: uppercase;
  font-weight: 700;
}

.multilingual-content-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  padding: 24px;
  border-top: 1px solid var(--border-subtle);
}

.lang-block {
  background: var(--bg-deep);
  border: 1px solid var(--border-subtle);
  border-radius: 6px;
  padding: 18px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.lang-tag {
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 800;
  color: var(--color-cyan);
  letter-spacing: 0.08em;
}

.lang-heading {
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--text-high);
  margin: 0;
  line-height: 1.4;
}

.lang-block p {
  font-size: 0.85rem;
  color: var(--text-med);
  line-height: 1.6;
  margin: 0;
}

.lang-block a {
  color: var(--color-cyan);
  text-decoration: none;
  font-weight: 700;
}

.lang-block a:hover {
  text-decoration: underline;
}
"""

if 'ENTERPRISE LIGHT MODE ENHANCEMENTS' not in css:
    css += extra_styles
    with open(CSS_PATH, 'w', encoding='utf-8') as f:
        f.write(css)
    print("✅ Successfully updated css/styles.css with Light/Dark Mode and UI enhancements!")
else:
    print("css/styles.css already contains enhancements, updated variable palette.")
    with open(CSS_PATH, 'w', encoding='utf-8') as f:
        f.write(css)

# --- 2. UPDATE JS/APP.JS WITH THEME CONTROLLER ---
with open(JS_APP_PATH, 'r', encoding='utf-8') as f:
    app_js = f.read()

theme_js = """
  // =========================================================================
  // THEME CONTROLLER (Light & Dark Mode with LocalStorage Persistence)
  // =========================================================================
  function initTheme() {
    const savedTheme = localStorage.getItem('ct_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeToggleBtn(savedTheme);
  }

  function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('ct_theme', newTheme);
    updateThemeToggleBtn(newTheme);
  }

  function updateThemeToggleBtn(theme) {
    const btn = document.getElementById('theme-toggle-btn');
    if (!btn) return;
    if (theme === 'light') {
      btn.innerHTML = '🌙 Dark';
      btn.setAttribute('title', 'Switch to Dark Mode');
    } else {
      btn.innerHTML = '☀️ Light';
      btn.setAttribute('title', 'Switch to Light Mode');
    }
  }

  // Expose toggleTheme globally
  window.toggleTheme = toggleTheme;
  initTheme();
"""

if 'function initTheme()' not in app_js:
    app_js = app_js.replace("})();", theme_js + "\n})();")
    with open(JS_APP_PATH, 'w', encoding='utf-8') as f:
        f.write(app_js)
    print("✅ Successfully injected Theme Controller into js/app.js!")
else:
    print("js/app.js already contains Theme Controller.")
