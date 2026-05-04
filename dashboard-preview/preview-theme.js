/* Static-preview theme bootstrap. Reads ?theme= or localStorage, applies
   data-theme on <html>, swaps wordmark/logo/title, propagates ?theme= to
   in-page links. Brand is locked in at session start — no runtime switcher.
   Production Laravel resolves tenant from host via ResolveTenant; this
   file only exists for the public static-HTML preview. */
(function () {
  var THEMES = {
    aiaxia:    { wordmark: 'AiAxia',    style: 'italic', weight: 500, title: 'AiAxia',    logo: null },
    eduasiste: { wordmark: 'EduAsiste', style: 'normal', weight: 700, title: 'EduAsiste', logo: 'https://eduasiste.org/chat/v3/avatar_eduardo_owl.png' },
    proasiste: { wordmark: 'ProAsiste', style: 'normal', weight: 500, title: 'ProAsiste', logo: null }
  };

  // Per-tenant copy overrides. Mirrors config/tenants.php "copy" arrays.
  // Keys must match data-tenant-copy attributes in the HTML.
  var COPY = {
    aiaxia:    {
      'dashboard.company_name':   'Acme Health',
      'dashboard.user_first_name': 'Maya',
      'dashboard.org_label':      'Company'
    },
    eduasiste: {
      'company.name_label':       'School name',
      'upload.subhead':           'Course materials, lesson plans, prior assessments, sample student work. PDF, DOCX, TXT, images. Up to 10 files.',
      'dashboard.project_pill':   'Lincoln High · active project',
      'dashboard.company_name':   'Lincoln High School',
      'dashboard.user_first_name': 'Mara',
      'dashboard.org_label':      'School'
    },
    proasiste: {
      'dashboard.company_name':   'Stiles & Co Consulting',
      'dashboard.user_first_name': 'Walt',
      'dashboard.org_label':      'Practice'
    }
  };

  var STORAGE_KEY = 'aiaxiaTheme';

  function readTheme() {
    var params = new URLSearchParams(window.location.search);
    var t = params.get('theme');
    if (t && THEMES[t]) return t;
    try {
      var stored = localStorage.getItem(STORAGE_KEY);
      if (stored && THEMES[stored]) return stored;
    } catch (e) {}
    return 'aiaxia';
  }

  function writeTheme(t) {
    if (!THEMES[t]) return;
    document.documentElement.dataset.theme = t;
    try { localStorage.setItem(STORAGE_KEY, t); } catch (e) {}
  }

  // Pre-paint
  var theme = readTheme();
  writeTheme(theme);

  function applyDom() {
    var t = THEMES[theme];

    // Wordmark
    var wm = document.querySelector('.ob-wordmark');
    if (wm) {
      wm.textContent = t.wordmark;
      wm.style.fontStyle = t.style;
      wm.style.fontWeight = t.weight;
    }

    // Logo
    var logo = document.querySelector('.ob-logo');
    if (logo) {
      if (t.logo) {
        logo.src = t.logo;
        logo.alt = '';
        logo.hidden = false;
      } else {
        logo.removeAttribute('src');
        logo.hidden = true;
      }
    }

    // Title
    document.title = t.title;

    // Per-tenant copy swaps (data-tenant-copy="key.subkey")
    var overrides = COPY[theme] || {};
    document.querySelectorAll('[data-tenant-copy]').forEach(function (el) {
      var key = el.dataset.tenantCopy;
      if (!('tenantCopyDefault' in el.dataset)) {
        el.dataset.tenantCopyDefault = el.textContent.trim();
      }
      var override = overrides[key];
      el.textContent = (override != null) ? override : el.dataset.tenantCopyDefault;
    });

    // Propagate ?theme= to in-page links
    document.querySelectorAll('a[href]').forEach(function (a) {
      try {
        var u = new URL(a.getAttribute('href'), window.location.href);
        if (u.origin !== window.location.origin) return;
        if (u.searchParams.has('theme')) return;
        u.searchParams.set('theme', theme);
        a.href = u.pathname + u.search + u.hash;
      } catch (e) {}
    });

    // Sample-logo placeholder for dashboard topbar v2 (when no user upload).
    // In production, the topbar logo binds to companies.logo_path; here in
    // the static preview we paint a wordmark cap into the 75x75 box so
    // every theme renders something recognizable.
    var dashLogoBox = document.querySelector('.dash-topbar-v2__logo');
    if (dashLogoBox) {
      var img = dashLogoBox.querySelector('img');
      if (t.logo) {
        if (!img) { img = document.createElement('img'); dashLogoBox.appendChild(img); }
        img.src = t.logo;
        img.alt = t.title + ' logo';
        var ph = dashLogoBox.querySelector('.dash-topbar-v2__logo--placeholder');
        if (ph) ph.remove();
      } else {
        if (img) img.remove();
        var existing = dashLogoBox.querySelector('.dash-topbar-v2__logo--placeholder');
        if (!existing) {
          var ph2 = document.createElement('span');
          ph2.className = 'dash-topbar-v2__logo--placeholder';
          ph2.textContent = t.wordmark.charAt(0);
          dashLogoBox.appendChild(ph2);
        } else {
          existing.textContent = t.wordmark.charAt(0);
        }
      }
    }

    // Brand is locked in at start of session via ?theme= URL param (or
    // localStorage carryover). No runtime switcher in topbar — the choice
    // made during onboarding/signup drives the entire experience.
    // Production Laravel resolves tenant from host via ResolveTenant
    // middleware; this static preview reads ?theme= once and persists.
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyDom);
  } else {
    applyDom();
  }
})();
