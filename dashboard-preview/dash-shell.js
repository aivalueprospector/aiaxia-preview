/* Dashboard shell interactions: twin-rail collapse + user-menu popover.
   Mirrors public/dashboard-preview/dash-shell.js. */
(function () {
  var STORAGE_RAIL = 'aiaxia.dashboard.twinRailCollapsed';
  var FULLSCREEN_CLASS = 'dash-twin-rail--fullscreen';
  var BODY_LOCK_CLASS = 'dash-twin-rail-locked';

  function applyRailState() {
    try {
      var collapsed = localStorage.getItem(STORAGE_RAIL) === '1';
      var body = document.getElementById('dash-body');
      var rail = document.getElementById('dash-twin-rail');
      if (body) body.classList.toggle('dash-body--rail-collapsed', collapsed);
      if (rail) rail.classList.toggle('dash-twin-rail--collapsed', collapsed);
      document.querySelectorAll('[data-action="rail-toggle"]').forEach(function (b) {
        b.setAttribute('aria-expanded', String(!collapsed));
      });
    } catch (e) {}
  }

  function isNarrow() {
    return window.matchMedia('(max-width: 640px)').matches;
  }

  function setupRailToggles() {
    document.querySelectorAll('[data-action="rail-toggle"]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        // At narrow viewports the rail can't expand inline (no room).
        // Tap the speech-bubble at top of the collapsed strip → open fullscreen.
        if (isNarrow()) {
          openFullscreen();
          return;
        }
        try {
          var current = localStorage.getItem(STORAGE_RAIL) === '1';
          localStorage.setItem(STORAGE_RAIL, current ? '0' : '1');
        } catch (e) {}
        applyRailState();
      });
    });
  }

  function openFullscreen() {
    var rail = document.getElementById('dash-twin-rail');
    if (!rail) return;
    rail.classList.add(FULLSCREEN_CLASS);
    document.body.classList.add(BODY_LOCK_CLASS);
  }

  function closeFullscreen() {
    var rail = document.getElementById('dash-twin-rail');
    if (!rail) return;
    rail.classList.remove(FULLSCREEN_CLASS);
    document.body.classList.remove(BODY_LOCK_CLASS);
  }

  function isFullscreen() {
    var rail = document.getElementById('dash-twin-rail');
    return !!(rail && rail.classList.contains(FULLSCREEN_CLASS));
  }

  function setupFullscreenToggles() {
    document.querySelectorAll('[data-action="rail-fullscreen-open"]').forEach(function (btn) {
      btn.addEventListener('click', openFullscreen);
    });
    document.querySelectorAll('[data-action="rail-fullscreen-close"]').forEach(function (btn) {
      btn.addEventListener('click', closeFullscreen);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isFullscreen()) closeFullscreen();
    });
  }

  var NAV_DRAWER_OPEN = 'dash-nav--drawer-open';
  var SHELL_DRAWER_OPEN = 'dash-shell-v2--drawer-open';

  function closeNavDrawer() {
    var nav = document.getElementById('dash-nav');
    var shell = document.querySelector('.dash-shell-v2');
    if (nav) nav.classList.remove(NAV_DRAWER_OPEN);
    if (shell) shell.classList.remove(SHELL_DRAWER_OPEN);
    document.querySelectorAll('[data-action="nav-toggle"]').forEach(function (b) {
      b.setAttribute('aria-expanded', 'false');
    });
  }

  function openNavDrawer() {
    var nav = document.getElementById('dash-nav');
    var shell = document.querySelector('.dash-shell-v2');
    if (nav) nav.classList.add(NAV_DRAWER_OPEN);
    if (shell) shell.classList.add(SHELL_DRAWER_OPEN);
    document.querySelectorAll('[data-action="nav-toggle"]').forEach(function (b) {
      b.setAttribute('aria-expanded', 'true');
    });
  }

  function isNavDrawerOpen() {
    var nav = document.getElementById('dash-nav');
    return !!(nav && nav.classList.contains(NAV_DRAWER_OPEN));
  }

  function setupNavDrawer() {
    document.querySelectorAll('[data-action="nav-toggle"]').forEach(function (btn) {
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        if (isNavDrawerOpen()) closeNavDrawer(); else openNavDrawer();
      });
    });
  }

  function setupDrawerDismissal() {
    document.addEventListener('click', function (e) {
      var nav = document.getElementById('dash-nav');
      if (isNavDrawerOpen() && nav && !nav.contains(e.target) &&
          !e.target.closest('[data-action="nav-toggle"]')) {
        closeNavDrawer();
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isNavDrawerOpen()) closeNavDrawer();
    });
  }

  function setupUserMenu() {
    var trigger = document.querySelector('[data-action="user-menu-toggle"]');
    var menu = document.querySelector('.dash-usermenu');
    if (!trigger || !menu) return;

    function close() {
      menu.dataset.open = 'false';
      trigger.setAttribute('aria-expanded', 'false');
    }
    function toggle() {
      var open = menu.dataset.open === 'true';
      menu.dataset.open = open ? 'false' : 'true';
      trigger.setAttribute('aria-expanded', String(!open));
    }

    trigger.addEventListener('click', function (e) {
      e.stopPropagation();
      toggle();
    });
    document.addEventListener('click', function (e) {
      if (menu.dataset.open === 'true' && !menu.contains(e.target) && e.target !== trigger) {
        close();
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.dataset.open === 'true') close();
    });
  }

  function init() {
    applyRailState();
    setupRailToggles();
    setupFullscreenToggles();
    setupNavDrawer();
    setupDrawerDismissal();
    setupUserMenu();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
