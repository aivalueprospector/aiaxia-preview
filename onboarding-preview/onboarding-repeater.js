/* Generic add/remove row for onboarding repeater steps.
   Wires up [data-repeater-add] -> clones [data-repeater-template]
   into [data-repeater-list]. Removal via [data-repeater-remove].
   Re-numbers row labels (e.g. "Teacher 1", "Teacher 2") via
   [data-repeater-index] tokens. */
(function () {
  function makeNamesUnique(node, listKey, index) {
    node.querySelectorAll('[name]').forEach(function (el) {
      var n = el.getAttribute('name');
      // expand patterns like teachers[][first_name] -> teachers[INDEX][first_name]
      el.setAttribute('name', n.replace(/\[\]/, '[' + index + ']'));
    });
    node.querySelectorAll('[data-repeater-index]').forEach(function (el) {
      el.textContent = String(index + 1);
    });
  }

  function relabel(list, key) {
    var rows = list.querySelectorAll(':scope > .ob-row');
    rows.forEach(function (row, i) {
      row.dataset.repeaterRow = key + ':' + i;
      row.querySelectorAll('[data-repeater-index]').forEach(function (el) {
        el.textContent = String(i + 1);
      });
      row.querySelectorAll('[name]').forEach(function (el) {
        var n = el.getAttribute('name');
        el.setAttribute('name', n.replace(/\[\d+\]|\[\]/, '[' + i + ']'));
      });
    });
  }

  function init() {
    document.querySelectorAll('[data-repeater-add]').forEach(function (btn) {
      var key = btn.dataset.repeaterAdd;
      btn.addEventListener('click', function () {
        var tpl = document.querySelector('template[data-repeater-template="' + key + '"]');
        var list = document.querySelector('[data-repeater-list="' + key + '"]');
        if (!tpl || !list) return;

        var clone = tpl.content.cloneNode(true);
        list.appendChild(clone);
        relabel(list, key);

        // Focus first input in the new row
        var rows = list.querySelectorAll(':scope > .ob-row');
        var last = rows[rows.length - 1];
        if (last) {
          var firstInput = last.querySelector('input, select, textarea');
          if (firstInput) firstInput.focus();
        }

        // Remove empty hint if present
        var emptyHint = list.querySelector('.ob-repeater__empty');
        if (emptyHint) emptyHint.remove();
      });
    });

    document.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-repeater-remove]');
      if (!btn) return;
      var row = btn.closest('.ob-row');
      var list = btn.closest('[data-repeater-list]');
      if (!row || !list) return;
      row.remove();
      relabel(list, list.dataset.repeaterList);
    });

    // Initial relabel for any rows present at page load
    document.querySelectorAll('[data-repeater-list]').forEach(function (list) {
      relabel(list, list.dataset.repeaterList);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
