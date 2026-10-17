/**
 * CYBERTRACE INTERACTIVE COMMAND CONTROLLER
 * High-performance state manager and tactical drawer inspector
 * CrowdStrike Falcon & Mandiant Advantage Enterprise Grade (100% English)
 */

(function () {
  'use strict';

  // Application State
  const state = {
    activeCategory: 'ALL',
    searchQuery: '',
    selectedThreatId: null,
    activeDrawerTab: 'overview'
  };

  // Dedicated Whitepapers Registry (All 50 Cataloged Threats)
  const WHITEPAPERS = {
    'TF-001': { url: 'threats/asyncrat.html', title: 'AsyncRAT Technical Dossier' },
    'TF-002': { url: 'threats/dolphinx.html', title: 'Dolphin X AI-Stealer Whitepaper' },
    'TF-003': { url: 'threats/lumma-whitepaper.html', title: 'Lumma Stealer C2 Dossier' },
    'TF-004': { url: 'threats/redline-whitepaper.html', title: 'RedLine Stealer Technical Dossier' },
    'TF-005': { url: 'threats/vidar-whitepaper.html', title: 'Vidar Stealer Technical Dossier' },
    'TF-006': { url: 'threats/agenttesla-whitepaper.html', title: 'Agent Tesla Spyware Dossier' },
    'TF-007': { url: 'threats/remcos-whitepaper.html', title: 'Remcos RAT Technical Dossier' },
    'TF-008': { url: 'threats/xworm-whitepaper.html', title: 'XWorm Hybrid RAT & Clipper Dossier' },
    'TF-009': { url: 'threats/darkgate-whitepaper.html', title: 'DarkGate Loader Technical Whitepaper' },
    'TF-010': { url: 'threats/rhadamanthys-whitepaper.html', title: 'Rhadamanthys Stealer Technical Dossier' },
    'TF-011': { url: 'threats/stealc-whitepaper.html', title: 'Stealc InfoStealer Technical Dossier' },
    'TF-012': { url: 'threats/havoc-whitepaper.html', title: 'Havoc C2 Demon Agent Technical Dossier' },
    'TF-013': { url: 'threats/sliver-whitepaper.html', title: 'Sliver C2 Framework Dossier' },
    'TF-014': { url: 'threats/mythic-whitepaper.html', title: 'Mythic C2 Framework Dossier' },
    'TF-015': { url: 'threats/quasarrat-whitepaper.html', title: 'QuasarRAT Technical Dossier' },
    'TF-016': { url: 'threats/warzone-whitepaper.html', title: 'Warzone RAT Ave Maria Dossier' },
    'TF-017': { url: 'threats/guloader-whitepaper.html', title: 'GuLoader Shellcode Loader Dossier' },
    'TF-018': { url: 'threats/pikabot-whitepaper.html', title: 'Pikabot Modular Loader Dossier' },
    'TF-019': { url: 'threats/qakbot-whitepaper.html', title: 'Qakbot Banking Trojan Dossier' },
    'TF-020': { url: 'threats/emotet-whitepaper.html', title: 'Emotet Modular Botnet Dossier' },
    'TF-021': { url: 'threats/lockbit-whitepaper.html', title: 'LockBit 3.0 Black Technical Dossier' },
    'TF-022': { url: 'threats/blackcat-whitepaper.html', title: 'BlackCat ALPHV Ransomware Dossier' },
    'TF-023': { url: 'threats/akira-whitepaper.html', title: 'Akira Ransomware Technical Dossier' },
    'TF-024': { url: 'threats/medusa-whitepaper.html', title: 'Medusa Ransomware Technical Dossier' },
    'TF-025': { url: 'threats/phobos-whitepaper.html', title: 'Phobos 8Base Ransomware Dossier' },
    'TF-026': { url: 'threats/formbook-whitepaper.html', title: 'Formbook XLoader Technical Dossier' },
    'TF-027': { url: 'threats/bumblebee-whitepaper.html', title: 'Bumblebee Loader Technical Dossier' },
    'TF-028': { url: 'threats/icedid-whitepaper.html', title: 'IcedID BokBot Technical Dossier' },
    'TF-029': { url: 'threats/danabot-whitepaper.html', title: 'DanaBot Banking Stealer Dossier' },
    'TF-030': { url: 'threats/smokeloader-whitepaper.html', title: 'SmokeLoader Modular Loader Dossier' },
    'TF-031': { url: 'threats/cobaltstrike-whitepaper.html', title: 'Cobalt Strike Malleable C2 Dossier' },
    'TF-032': { url: 'threats/bruteratel-whitepaper.html', title: 'Brute Ratel C4 Commander Dossier' },
    'TF-033': { url: 'threats/netsupport-whitepaper.html', title: 'NetSupport RAT Investigation Dossier' },
    'TF-034': { url: 'threats/njrat-whitepaper.html', title: 'NjRAT Bladabindi Investigation Dossier' },
    'TF-035': { url: 'threats/dcrat-whitepaper.html', title: 'DCRat DarkCrystal Technical Dossier' },
    'TF-036': { url: 'threats/purecrypter-whitepaper.html', title: 'PureCrypter PureLogs Dossier' },
    'TF-037': { url: 'threats/privateloader-whitepaper.html', title: 'PrivateLoader Distribution Dossier' },
    'TF-038': { url: 'threats/systembc-whitepaper.html', title: 'SystemBC SOCKS Proxy Botnet Dossier' },
    'TF-039': { url: 'threats/mirai-whitepaper.html', title: 'Mirai IoT Botnet Technical Dossier' },
    'TF-040': { url: 'threats/mozi-whitepaper.html', title: 'Mozi P2P Botnet Technical Dossier' },
    'TF-041': { url: 'threats/meduza-whitepaper.html', title: 'Meduza Stealer Technical Dossier' },
    'TF-042': { url: 'threats/risepro-whitepaper.html', title: 'RisePro InfoStealer Technical Dossier' },
    'TF-043': { url: 'threats/bunnyloader-whitepaper.html', title: 'BunnyLoader Modular Loader Dossier' },
    'TF-044': { url: 'threats/latrodectus-whitepaper.html', title: 'Latrodectus Advanced Loader Dossier' },
    'TF-045': { url: 'threats/strelastealer-whitepaper.html', title: 'StrelaStealer Outlook Dossier' },
    'TF-046': { url: 'threats/hijackloader-whitepaper.html', title: 'HijackLoader In-Memory Loader Dossier' },
    'TF-047': { url: 'threats/rustbucket-whitepaper.html', title: 'RustBucket macOS Malware Dossier' },
    'TF-048': { url: 'threats/atomic-stealer-whitepaper.html', title: 'Atomic Stealer macOS Investigation Dossier' },
    'TF-049': { url: 'threats/shadowpad-whitepaper.html', title: 'ShadowPad C2 Framework Dossier' },
    'TF-050': { url: 'threats/plugx-whitepaper.html', title: 'PlugX Korplug Modular RAT Dossier' }
  };

  // DOM Elements
  const el = {
    utcClock: document.getElementById('utc-clock-val'),
    searchInput: document.getElementById('threat-search-input'),
    filterPills: document.getElementById('filter-pills-row'),
    threatGrid: document.getElementById('threat-cards-grid'),
    countShowing: document.getElementById('count-showing'),
    countTotal: document.getElementById('count-total'),
    dossierOverlay: document.getElementById('dossier-overlay'),
    dossierDrawer: document.getElementById('dossier-drawer'),
    drawerCloseBtn: document.getElementById('drawer-close-btn'),
    drawerWhitepaperBanner: document.getElementById('drawer-whitepaper-banner'),
    drawerBody: document.getElementById('drawer-body-content'),
    drawerTabsContainer: document.getElementById('drawer-tabs-row'),
    drawerIdBadge: document.getElementById('drawer-id-badge'),
    drawerName: document.getElementById('drawer-name'),
    drawerType: document.getElementById('drawer-type'),
    statTotalVal: document.getElementById('stat-total-val'),
    statActiveVal: document.getElementById('stat-active-val'),
    statTestedVal: document.getElementById('stat-tested-val'),
    statMonitoredVal: document.getElementById('stat-monitored-val')
  };

  // Initialize Application
  function init() {
    setupClock();
    updateStatsRibbon();
    renderFilterPills();
    renderThreatGrid();
    setupEventListeners();
    setupLightbox();
    checkUrlHash();
  }

  // Live UTC Clock
  function setupClock() {
    function tick() {
      const now = new Date();
      const utcString = now.toUTCString().replace('GMT', 'UTC');
      if (el.utcClock) el.utcClock.textContent = utcString.slice(17, 25) + ' UTC';
    }
    tick();
    setInterval(tick, 1000);
  }

  // Update Stats Ribbon
  function updateStatsRibbon() {
    const total = THREATS_DATA.length;
    const active = THREATS_DATA.filter(t => t.status === 'ACTIVE').length;
    const tested = THREATS_DATA.filter(t => t.teamStatus === 'TESTED' || t.teamStatus === 'TESTED_PRIOR').length;
    const monitored = THREATS_DATA.filter(t => t.teamStatus === 'MONITORED').length;

    if (el.statTotalVal) el.statTotalVal.textContent = total;
    if (el.statActiveVal) el.statActiveVal.textContent = active;
    if (el.statTestedVal) el.statTestedVal.textContent = tested;
    if (el.statMonitoredVal) el.statMonitoredVal.textContent = monitored;
    if (el.countTotal) el.countTotal.textContent = total;
  }

  // Render Filter Pills
  function renderFilterPills() {
    if (!el.filterPills) return;

    const categories = [
      { key: 'ALL', label: 'All Threats' },
      { key: 'RAT', label: 'RATs' },
      { key: 'InfoStealer', label: 'InfoStealers' },
      { key: 'Loader', label: 'Loaders' },
      { key: 'Ransomware', label: 'Ransomware' },
      { key: 'C2 Framework', label: 'C2 Frameworks' },
      { key: 'Botnet', label: 'Botnets' }
    ];

    el.filterPills.innerHTML = categories.map(cat => `
      <button class="pill-btn ${state.activeCategory === cat.key ? 'active' : ''}" data-category="${cat.key}">
        ${cat.label}
      </button>
    `).join('');

    el.filterPills.querySelectorAll('.pill-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        state.activeCategory = btn.getAttribute('data-category');
        renderFilterPills();
        renderThreatGrid();
      });
    });
  }

  // Filter Threats
  function getFilteredThreats() {
    const q = state.searchQuery.trim().toLowerCase();
    return THREATS_DATA.filter(item => {
      const matchesCategory = state.activeCategory === 'ALL' || item.category === state.activeCategory;
      if (!matchesCategory) return false;
      if (!q) return true;

      const enData = item.en || item;
      return (
        item.name.toLowerCase().includes(q) ||
        item.id.toLowerCase().includes(q) ||
        item.category.toLowerCase().includes(q) ||
        item.lang.toLowerCase().includes(q) ||
        item.c2.toLowerCase().includes(q) ||
        (enData.desc && enData.desc.toLowerCase().includes(q)) ||
        (enData.summary && enData.summary.toLowerCase().includes(q))
      );
    });
  }

  // Render Main Threat Cards Grid (with 140px Visual Thumbnail Banner)
  function renderThreatGrid() {
    if (!el.threatGrid) return;
    const filtered = getFilteredThreats();

    if (el.countShowing) el.countShowing.textContent = filtered.length;

    if (filtered.length === 0) {
      el.threatGrid.innerHTML = `
        <div class="empty-results">
          <h3>No Matching Threat Dossiers Found</h3>
          <p>Please adjust your search query or reset the category filters to display the full threat index.</p>
        </div>
      `;
      return;
    }

    el.threatGrid.innerHTML = filtered.map(threat => {
      const data = threat.en || threat;
      const wp = WHITEPAPERS[threat.id];
      const manifestEntry = (typeof FORENSIC_MEDIA_MANIFEST !== 'undefined' && FORENSIC_MEDIA_MANIFEST[threat.id]) 
        ? FORENSIC_MEDIA_MANIFEST[threat.id] : null;
      const mediaCount = manifestEntry && manifestEntry.items ? manifestEntry.items.length : 2;
      const primaryImg = (manifestEntry && manifestEntry.items && manifestEntry.items[0]) 
        ? manifestEntry.items[0].url : threat.image;
      const severityClass = (threat.relevance === 'CRITICAL') ? 'crit' : 'high';
      const statusClass = (threat.status === 'ACTIVE') ? 'active' : 'monitored';
      const statusLabel = (threat.status === 'ACTIVE') ? 'ACTIVE 2026' : 'MONITORED';

      return `
        <article class="threat-card" data-id="${threat.id}">
          <div class="card-thumb-banner" onclick="window.CyberTraceApp.openDossier('${threat.id}')">
            <img src="${primaryImg}" alt="${threat.name} forensic artifact" class="thumb-img" loading="lazy">
            <div class="thumb-overlay"></div>
            <div class="thumb-badges-top">
              <span class="thumb-category-tag">${threat.category}</span>
              <span class="thumb-severity-tag ${severityClass}">${threat.relevance || 'HIGH'}</span>
            </div>
            <div class="thumb-evidence-pill">📸 ${mediaCount} Forensic Assets</div>
          </div>

          <div class="card-content-body">
            <div>
              <div class="card-meta-line">
                <span class="card-id-code">${threat.id}</span>
                <span class="card-status-pill ${statusClass}">${statusLabel}</span>
              </div>
              <h3 class="card-title">${threat.name}</h3>
              <p class="card-summary">${data.summary}</p>
            </div>

            <div>
              <div class="card-specs-row">
                <div class="spec-line">
                  <span class="spec-lbl">Toolchain:</span>
                  <span class="spec-val">${threat.lang}</span>
                </div>
                <div class="spec-line">
                  <span class="spec-lbl">Architecture:</span>
                  <span class="spec-val">${threat.arch}</span>
                </div>
              </div>

              <div class="card-actions-row">
                <button class="card-btn-inspect" onclick="window.CyberTraceApp.openDossier('${threat.id}')">
                  <span>Inspect Dossier</span>
                </button>
                <a href="${wp ? wp.url : '#'}" class="card-btn-whitepaper" target="_blank" rel="noopener">
                  <span>Whitepaper ↗</span>
                </a>
              </div>
            </div>
          </div>
        </article>
      `;
    }).join('');
  }

  // Open Dossier Drawer
  function openDossier(id) {
    state.selectedThreatId = id;
    state.activeDrawerTab = 'overview';
    window.location.hash = id;
    renderDrawerTabs();
    renderDrawerContent();

    el.dossierOverlay.classList.add('open');
    el.dossierDrawer.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  // Close Dossier Drawer
  function closeDossier() {
    el.dossierOverlay.classList.remove('open');
    el.dossierDrawer.classList.remove('open');
    if (el.drawerWhitepaperBanner) {
      el.drawerWhitepaperBanner.classList.remove('active');
      el.drawerWhitepaperBanner.innerHTML = '';
    }
    document.body.style.overflow = '';
    state.selectedThreatId = null;
    history.replaceState(null, null, ' ');
  }

  // Render Drawer Tabs (7 Enterprise Tabs)
  function renderDrawerTabs() {
    if (!el.drawerTabsContainer) return;

    const tabs = [
      { id: 'overview', label: 'Overview' },
      { id: 'infection', label: 'Infection Flow' },
      { id: 'technical', label: 'Anatomy & C2' },
      { id: 'defense', label: 'Defense Playbook' },
      { id: 'detection', label: 'YARA & Hunting' },
      { id: 'media', label: 'Forensic Visuals' },
      { id: 'sources', label: 'Verified Sources' }
    ];

    el.drawerTabsContainer.innerHTML = tabs.map(tab => `
      <button class="drawer-tab-btn ${state.activeDrawerTab === tab.id ? 'active' : ''}" data-tab="${tab.id}">
        ${tab.label}
      </button>
    `).join('');

    el.drawerTabsContainer.querySelectorAll('.drawer-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        state.activeDrawerTab = btn.getAttribute('data-tab');
        renderDrawerTabs();
        renderDrawerContent();
      });
    });
  }

  // Render Detailed Content inside Drawer
  function renderDrawerContent() {
    const threat = THREATS_DATA.find(t => t.id === state.selectedThreatId);
    if (!threat || !el.drawerBody) return;

    const data = threat.en || threat;
    const wp = WHITEPAPERS[threat.id];

    // Header metadata
    if (el.drawerIdBadge) el.drawerIdBadge.textContent = `${threat.id} // #${threat.num || '000'}`;
    if (el.drawerName) el.drawerName.textContent = threat.name;
    if (el.drawerType) el.drawerType.textContent = data.type;

    // Render Whitepaper Banner if Available
    if (el.drawerWhitepaperBanner) {
      if (wp) {
        el.drawerWhitepaperBanner.innerHTML = `
          <div class="whitepaper-cta-text-group">
            <span class="whitepaper-cta-tag">FULL EDITORIAL WHITEPAPER</span>
            <span class="whitepaper-cta-headline">${wp.title}</span>
          </div>
          <a href="${wp.url}" class="whitepaper-cta-btn" target="_blank" rel="noopener">
            <span>Read Whitepaper ↗</span>
          </a>
        `;
        el.drawerWhitepaperBanner.classList.add('active');
      } else {
        el.drawerWhitepaperBanner.innerHTML = '';
        el.drawerWhitepaperBanner.classList.remove('active');
      }
    }

    let html = '';

    // TAB 1: OVERVIEW
    if (state.activeDrawerTab === 'overview') {
      html = `
        <div class="dossier-section">
          <h4 class="dossier-section-title">01 | Executive Summary</h4>
          <p class="dossier-desc-text">${data.summary}</p>
        </div>

        <div class="dossier-section">
          <h4 class="dossier-section-title">Threat Landscape &amp; Operational Context</h4>
          <p class="dossier-desc-text">${data.desc}</p>
        </div>

        <div class="dossier-section">
          <h4 class="dossier-section-title">Why Watch in 2026?</h4>
          <div class="whitepaper-callout" style="margin: 0;">
            <p class="dossier-desc-text" style="color: var(--color-cyan); font-weight: 500;">${data.whyWatch}</p>
          </div>
        </div>

        <div class="dossier-section">
          <h4 class="dossier-section-title">Propagation Vectors</h4>
          <p class="dossier-desc-text">${data.propagation}</p>
        </div>
      `;
    } 
    // TAB 2: INFECTION CHAIN
    else if (state.activeDrawerTab === 'infection') {
      const steps = data.infectionChain.map((step, idx) => `
        <div class="infection-stage-card" style="margin-bottom: 0.75rem;">
          <div class="stage-header">
            <span class="stage-tag">PHASE 0${idx + 1}</span>
            <h3 class="stage-title">${step.stage}</h3>
          </div>
          <p class="stage-desc">${step.desc}</p>
        </div>
      `).join('');

      html = `
        <div class="dossier-section">
          <h4 class="dossier-section-title">02 | Multi-Stage Infection Flow</h4>
          <div class="infection-chain-list">
            ${steps}
          </div>
        </div>
      `;
    } 
    // TAB 3: TECHNICAL & C2 ANATOMY
    else if (state.activeDrawerTab === 'technical') {
      const techList = data.tech.map(t => `
        <div class="tech-bullet-item">
          <span class="tech-bullet-dot">▪</span>
          <span>${t}</span>
        </div>
      `).join('');

      const mitreChips = threat.mitre.map(m => `
        <span class="mitre-chip">${m}</span>
      `).join('');

      html = `
        <div class="dossier-section">
          <h4 class="dossier-section-title">03 | Technical Architecture</h4>
          <div class="tech-spec-grid">
            ${techList}
          </div>
        </div>

        <div class="dossier-section">
          <h4 class="dossier-section-title">C2 Protocol &amp; Traffic Telemetry</h4>
          <div class="c2-protocol-box" style="margin: 0;">
            <code class="c2-protocol-desc">${data.c2Anatomy}</code>
          </div>
        </div>

        <div class="dossier-section">
          <h4 class="dossier-section-title">MITRE ATT&amp;CK Alignment</h4>
          <div class="mitre-chips-row">
            ${mitreChips}
          </div>
        </div>
      `;
    } 
    // TAB 4: DEFENSE & CONTAINMENT
    else if (state.activeDrawerTab === 'defense') {
      const defenseSteps = data.defense.map((step, idx) => `
        <div class="defense-step-card" style="margin-bottom: 0.75rem;">
          <span class="defense-step-num">[0${idx + 1}]</span>
          <p class="defense-step-text">${step}</p>
        </div>
      `).join('');

      html = `
        <div class="dossier-section">
          <h4 class="dossier-section-title">04 | Immediate Containment Procedures</h4>
          <div class="defense-action-box" style="background: transparent; border: none; padding: 0;">
            ${defenseSteps}
          </div>
        </div>
      `;
    } 
    // TAB 5: DETECTION (YARA & SIGMA)
    else if (state.activeDrawerTab === 'detection') {
      const iocsHtml = (threat.iocs && threat.iocs.length > 0) ? `
        <div class="dossier-section" style="margin-top: 1.5rem;">
          <h4 class="dossier-section-title">Observable Indicators of Compromise (IoCs)</h4>
          <div class="iocs-container">
            ${threat.iocs.map(ioc => `
              <div class="ioc-row">
                <span class="ioc-badge">${ioc.type}</span>
                <code class="ioc-val">${ioc.val}</code>
              </div>
            `).join('')}
          </div>
        </div>
      ` : '';

      html = `
        <div class="dossier-section">
          <h4 class="dossier-section-title">05 | YARA Rule // In-Memory Detection</h4>
          <div class="detection-code-block">
            <div class="code-header">
              <span class="code-title">YARA // ${threat.id}</span>
              <button class="copy-btn" onclick="navigator.clipboard.writeText(document.getElementById('drawer-yara-code').innerText)">Copy YARA</button>
            </div>
            <pre id="drawer-yara-code" class="code-viewport"><code>${threat.yara}</code></pre>
          </div>
        </div>

        <div class="dossier-section" style="margin-top: 1.5rem;">
          <h4 class="dossier-section-title">Sigma Rule // Behavioral Telemetry</h4>
          <div class="detection-code-block">
            <div class="code-header">
              <span class="code-title">SIGMA DETECT // YAML</span>
              <button class="copy-btn" onclick="navigator.clipboard.writeText(document.getElementById('drawer-sigma-code').innerText)">Copy Sigma</button>
            </div>
            <pre id="drawer-sigma-code" class="code-viewport"><code>${threat.sigma}</code></pre>
          </div>
        </div>

        ${iocsHtml}
      `;
    }
    // TAB 6: FORENSIC VISUALS & MEDIA
    else if (state.activeDrawerTab === 'media') {
      let galleryItems = [];
      if (typeof FORENSIC_MEDIA_MANIFEST !== 'undefined' && FORENSIC_MEDIA_MANIFEST[threat.id] && FORENSIC_MEDIA_MANIFEST[threat.id].items) {
        galleryItems = FORENSIC_MEDIA_MANIFEST[threat.id].items;
      } else if (threat.gallery && threat.gallery.length > 0) {
        galleryItems = threat.gallery;
      } else {
        galleryItems = [
          {
            url: threat.image,
            id: `EVID-${threat.id.replace('TF-', '')}-01`,
            type: 'Forensic Artifact',
            title: `${threat.name} Operator Management Interface`,
            desc: 'Local forensic capture archived in the intelligence vault.'
          }
        ];
      }

      const evidenceCards = galleryItems.map((item, idx) => {
        const evId = item.id || `EVID-${threat.id.replace('TF-', '')}-0${idx + 1}`;
        const evType = item.type || 'Forensic Artifact';
        const title = item.title || `${threat.name} Forensic Artifact #0${idx + 1}`;
        const desc = item.desc || item.caption || '';
        const safeTitle = title.replace(/'/g, "\'");
        const safeDesc = desc.replace(/'/g, "\'");

        return `
          <figure class="evidence-card" onclick="openLightbox('${item.url}', '${safeTitle}', '${safeDesc}')">
            <div class="evidence-header">
              <div class="evidence-meta">
                <span class="evidence-badge id">[${evId}]</span>
                <span class="evidence-badge type">${evType}</span>
                <span class="evidence-badge vault">LOCAL FORENSIC VAULT</span>
              </div>
              <span class="evidence-zoom-hint">🔍 ZOOM // FULL RESOLUTION</span>
            </div>
            <div class="evidence-img-container">
              <img src="${item.url}" alt="${title}" class="evidence-img zoomable-asset" loading="lazy">
            </div>
            <figcaption class="evidence-caption">
              <div class="caption-title-en">${title}</div>
              <p class="caption-desc">${desc}</p>
            </figcaption>
          </figure>
        `;
      }).join('');

      html = `
        <div class="dossier-section">
          <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border-subtle); padding-bottom: 0.5rem; margin-bottom: 0.75rem;">
            <h4 class="dossier-section-title" style="border-bottom: none; padding-bottom: 0; margin-bottom: 0;">06 | Forensic Visual Evidence</h4>
            <span class="evidence-badge id">${galleryItems.length} Verified Assets</span>
          </div>
          <p style="font-size: 0.82rem; color: var(--text-muted); margin-bottom: 1rem;">
            High-fidelity forensic captures, operator control interfaces, and in-memory execution schematics stored locally in the CyberTrace laboratory. Click any asset to inspect in full resolution.
          </p>
          <div class="evidence-grid" style="grid-template-columns: 1fr; gap: 1.25rem;">
            ${evidenceCards}
          </div>
        </div>
      `;
    } 
    // TAB 7: SOURCES
    else if (state.activeDrawerTab === 'sources') {
      const sourceList = threat.sources.map(s => `
        <div class="source-item" style="display: flex; justify-content: space-between; align-items: center; padding: 0.65rem 0.85rem; background: #0f172a; border: 1px solid #1e293b; border-radius: 6px; margin-bottom: 0.5rem;">
          <span style="font-weight: 600; color: #f1f5f9; font-size: 0.82rem;">${s.name}</span>
          <span class="source-type-tag" style="color: var(--color-cyan); font-family: var(--font-mono); font-size: 0.72rem;">[${s.type}]</span>
        </div>
      `).join('');

      html = `
        <div class="dossier-section">
          <h4 class="dossier-section-title">07 | Verified Threat Intelligence References</h4>
          <div class="sources-list">
            ${sourceList}
          </div>
        </div>
      `;
    }

    el.drawerBody.innerHTML = html;
  }

  // Lightbox Controller
  function setupLightbox() {
    const modal = document.getElementById('cybertrace-lightbox');
    const closeBtn = document.getElementById('ct-lightbox-close-btn');
    const backdrop = document.getElementById('ct-lightbox-backdrop');

    if (closeBtn) closeBtn.addEventListener('click', closeLightbox);
    if (backdrop) backdrop.addEventListener('click', closeLightbox);
    if (modal) {
      modal.addEventListener('click', (e) => {
        if (e.target === modal || e.target === backdrop) closeLightbox();
      });
    }
  }

  function openLightbox(imgSrc, titleText, captionText) {
    const modal = document.getElementById('cybertrace-lightbox');
    const img = document.getElementById('ct-lightbox-img');
    const titleEl = document.getElementById('ct-lightbox-title');
    const captionEl = document.getElementById('ct-lightbox-caption');
    if (!modal || !img) return;

    img.src = imgSrc;
    if (titleEl) titleEl.textContent = titleText || 'CYBERTRACE FORENSIC ARTIFACT';
    if (captionEl) captionEl.textContent = captionText || '';
    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    const modal = document.getElementById('cybertrace-lightbox');
    if (!modal) return;
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    if (!el.dossierDrawer || !el.dossierDrawer.classList.contains('open')) {
      document.body.style.overflow = '';
    }
  }

  // Setup Global Event Listeners
  function setupEventListeners() {
    // Search input
    if (el.searchInput) {
      el.searchInput.addEventListener('input', (e) => {
        state.searchQuery = e.target.value;
        renderThreatGrid();
      });
    }

    // Drawer close buttons
    if (el.drawerCloseBtn) el.drawerCloseBtn.addEventListener('click', closeDossier);
    if (el.dossierOverlay) el.dossierOverlay.addEventListener('click', closeDossier);

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      // Ctrl+K focuses search
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (el.searchInput) {
          el.searchInput.focus();
          el.searchInput.select();
        }
      }
      // Escape closes modal / drawer
      if (e.key === 'Escape') {
        const modal = document.getElementById('cybertrace-lightbox');
        if (modal && modal.classList.contains('active')) {
          closeLightbox();
        } else {
          closeDossier();
        }
      }
    });

    // Hash change monitoring
    window.addEventListener('hashchange', checkUrlHash);
  }

  // Check URL Hash for direct threat linking
  function checkUrlHash() {
    const hash = window.location.hash.replace('#', '');
    if (hash) {
      const exists = THREATS_DATA.find(t => t.id === hash);
      if (exists) openDossier(exists.id);
    }
  }

  // Expose API to global scope for inline button handlers
  window.CyberTraceApp = {
    openDossier,
    closeDossier,
    openLightbox,
    closeLightbox
  };
  window.openLightbox = openLightbox;
  window.closeLightbox = closeLightbox;

  // Initialize on load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }


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

})();
