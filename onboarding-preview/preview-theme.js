/* Static-preview theme bootstrap. Reads ?theme= or localStorage, applies
   data-theme on <html>, swaps wordmark/logo/title, propagates ?theme= to
   in-page links, mounts a small theme switcher into the topbar. Production
   Laravel does this server-side via App\Http\Middleware\ResolveTenant —
   this file only exists for the public static-HTML preview. */
(function () {
  var THEMES = {
    aiaxia:    { wordmark: 'AiAxia',    style: 'italic', weight: 500, title: 'AiAxia',    logo: null },
    eduasiste: { wordmark: 'EduAsiste', style: 'normal', weight: 700, title: 'EduAsiste', logo: 'https://eduasiste.org/chat/v3/avatar_eduardo_owl.png' },
    proasiste: { wordmark: 'ProAsiste', style: 'normal', weight: 500, title: 'ProAsiste', logo: null }
  };

  // Per-tenant copy overrides. Mirrors config/tenants.php "copy" arrays.
  // Keys must match data-tenant-copy attributes in the HTML.
  var COPY = {
    aiaxia:    {},
    eduasiste: {
      'company.name_label': 'School name',
      'upload.subhead':     'Course materials, lesson plans, prior assessments, sample student work. PDF, DOCX, TXT, images. Up to 10 files.'
    },
    proasiste: {}
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

    // Mount switcher in topbar
    var bar = document.querySelector('.ob-topbar');
    if (!bar || bar.querySelector('.ob-theme-switcher')) return;

    var wrap = document.createElement('div');
    wrap.className = 'ob-theme-switcher';
    wrap.setAttribute('role', 'group');
    wrap.setAttribute('aria-label', 'Preview theme');

    Object.keys(THEMES).forEach(function (slug) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.dataset.theme = slug;
      btn.textContent = THEMES[slug].wordmark;
      if (slug === theme) btn.setAttribute('aria-pressed', 'true');
      btn.addEventListener('click', function () {
        var url = new URL(window.location.href);
        url.searchParams.set('theme', slug);
        window.location.href = url.toString();
      });
      wrap.appendChild(btn);
    });

    var progress = bar.querySelector('.ob-progress');
    if (progress) bar.insertBefore(wrap, progress);
    else bar.appendChild(wrap);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyDom);
  } else {
    applyDom();
  }
})();
