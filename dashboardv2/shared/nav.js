// Tiny script: brand toggle (prototype only) + active-link from data-page.
// In production, Laravel's ResolveBrand middleware sets data-brand on <html>.

(function () {
  const STORAGE_KEY = 'twin-dashboard-brand';
  const BRAND_NAMES = { proasiste: 'ProAsiste', eduasiste: 'EduAsiste', aivp: 'AiVP Internal' };
  const BRAND_MARKS = { proasiste: 'P', eduasiste: 'E', aivp: 'A' };

  const stored = localStorage.getItem(STORAGE_KEY);
  if (stored && Object.prototype.hasOwnProperty.call(BRAND_NAMES, stored)) {
    document.documentElement.dataset.brand = stored;
  }

  function applyBrandLabels(brand) {
    document.querySelectorAll('[data-brand-name]').forEach((el) => {
      el.textContent = BRAND_NAMES[brand];
    });
    document.querySelectorAll('[data-brand-mark]').forEach((el) => {
      el.textContent = BRAND_MARKS[brand];
    });
  }

  function mountBrandToggle() {
    const host = document.getElementById('proto-toggle');
    if (!host) return;
    const current = document.documentElement.dataset.brand || 'proasiste';

    const label = document.createElement('span');
    label.className = 'proto-toggle__label';
    label.textContent = 'Brand';
    host.appendChild(label);

    Object.keys(BRAND_NAMES).forEach((key) => {
      const btn = document.createElement('button');
      btn.dataset.brandSet = key;
      btn.setAttribute('aria-pressed', key === current ? 'true' : 'false');
      btn.textContent = BRAND_NAMES[key];
      btn.addEventListener('click', () => {
        document.documentElement.dataset.brand = key;
        localStorage.setItem(STORAGE_KEY, key);
        host.querySelectorAll('button').forEach((x) => {
          x.setAttribute('aria-pressed', x === btn ? 'true' : 'false');
        });
        applyBrandLabels(key);
      });
      host.appendChild(btn);
    });
  }

  function mountActiveLink() {
    const page = document.body.dataset.page;
    if (!page) return;
    document.querySelectorAll('.sidebar__link').forEach((a) => {
      if (a.dataset.page === page) a.setAttribute('aria-current', 'page');
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    mountBrandToggle();
    mountActiveLink();
    applyBrandLabels(document.documentElement.dataset.brand || 'proasiste');
  });
})();
