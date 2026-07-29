(function () {
  var btn = document.getElementById('more-btn');
  if (btn) {
    setTimeout(function () {
      btn.classList.add('is-visible');
      btn.removeAttribute('aria-hidden');
      btn.removeAttribute('tabindex');
    }, 5000);
  }

  var dungeonItem = document.getElementById('nav-dungeon-item');
  var dungeonLink = document.getElementById('nav-dungeon-link');
  if (dungeonItem && dungeonLink) {
    setTimeout(function () {
      dungeonItem.classList.add('is-visible');
      dungeonLink.removeAttribute('aria-hidden');
      dungeonLink.removeAttribute('tabindex');
    }, 3000);
  }

  var toggle = document.getElementById('nav-toggle');
  var links = document.getElementById('nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var isOpen = links.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    links.addEventListener('click', function (event) {
      if (event.target.closest('a')) {
        links.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }
})();
