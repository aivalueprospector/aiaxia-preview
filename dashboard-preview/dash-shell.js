/* Dashboard shell interactions — preview only.
   Toggles user-menu popover and twin-rail collapse. Production Laravel
   will reimplement the same behaviors as resources/js/dashboard-twin-rail.js
   and a small user-menu module. */
(function () {
  var STORAGE_RAIL = 'aiaxia.dashboard.twinRailCollapsed';

  function applyRailState() {
    try {
      var collapsed = localStorage.getItem(STORAGE_RAIL) === '1';
      var body = document.querySelector('.dash-body');
      if (!body) return;
      body.classList.toggle('dash-body--rail-collapsed', collapsed);
      var rail = document.querySelector('.dash-twin-rail');
      if (rail) {
        rail.classList.toggle('dash-twin-rail--collapsed', collapsed);
      }
      var toggles = document.querySelectorAll('[data-action="rail-toggle"]');
      toggles.forEach(function (b) { b.setAttribute('aria-expanded', String(!collapsed)); });
    } catch (e) {}
  }

  function setupRailToggles() {
    document.querySelectorAll('[data-action="rail-toggle"]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        try {
          var current = localStorage.getItem(STORAGE_RAIL) === '1';
          localStorage.setItem(STORAGE_RAIL, current ? '0' : '1');
        } catch (e) {}
        applyRailState();
      });
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
    setupUserMenu();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
