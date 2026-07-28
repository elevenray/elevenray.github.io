(function () {
  var gallery = document.getElementById('gallery');
  var vignette = document.getElementById('vignette');
  var hallwayBg = document.querySelector('.hallway-bg');
  var frames = Array.prototype.slice.call(document.querySelectorAll('.frame'));
  var rooms = Array.prototype.slice.call(document.querySelectorAll('.room'));
  var prevBtn = document.getElementById('nav-prev');
  var nextBtn = document.getElementById('nav-next');
  var observatory = document.getElementById('observatory');
  var bench = document.getElementById('bench');
  var visitor = document.getElementById('visitor');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var pointerFine = window.matchMedia('(pointer: fine)').matches;

  var WALK_OUT_MS = 900;
  var WALK_IN_MS = 1600;
  var FRAME_SLIDE_MS = WALK_OUT_MS + WALK_IN_MS;

  var activeRoom = null;
  var activeIndex = -1;
  var sitTimer = null;
  var walkOutTimer = null;
  var walkEndTimer = null;
  var frameCleanupTimer = null;

  function clamp(n, min, max) { return Math.min(Math.max(n, min), max); }

  function updateFrameClasses() {
    frames.forEach(function (f, i) {
      f.classList.toggle('frame--active', i === activeIndex);
    });
  }

  // Slide the outgoing frame off to one side and bring the incoming frame
  // in from the opposite edge, instead of a plain crossfade in place —
  // so browsing reads as "frames passing by" in the direction you're moving.
  function slideFrames(oldIndex, newIndex, direction) {
    var oldFrame = frames[oldIndex];
    var newFrame = frames[newIndex];
    var oldSide = direction === 1 ? 'frame--offside-l' : 'frame--offside-r';
    var newSide = direction === 1 ? 'frame--offside-r' : 'frame--offside-l';

    if (oldFrame) {
      oldFrame.classList.remove('frame--active');
      oldFrame.classList.add(oldSide);
    }
    if (newFrame) {
      newFrame.classList.add(newSide);
      void newFrame.offsetWidth; // apply the offside start position before animating in
      newFrame.classList.add('frame--active');
    }

    clearTimeout(frameCleanupTimer);
    frameCleanupTimer = window.setTimeout(function () {
      frames.forEach(function (f) {
        f.classList.remove('frame--offside-l', 'frame--offside-r');
      });
    }, FRAME_SLIDE_MS);
  }

  function visitorHomeX() {
    var obsRect = observatory.getBoundingClientRect();
    return obsRect.width / 2 - visitor.offsetWidth / 2;
  }

  function settleVisitorInstant() {
    visitor.style.transition = 'none';
    visitor.style.transform = 'translateX(' + visitorHomeX() + 'px)';
    void visitor.offsetWidth; // force reflow so later transitions re-apply
    visitor.style.transition = '';
  }

  // The visitor exits off one edge of the observatory, then walks back in
  // from the same side — its own two-beat "leave, then arrive" stride.
  function walkAcross(direction) {
    var obsRect = observatory.getBoundingClientRect();
    var exitX = visitorHomeX() + direction * (obsRect.width / 2 + 50);

    visitor.classList.add('visitor--walking');
    visitor.style.transition = 'transform ' + WALK_OUT_MS + 'ms ease-in';
    visitor.style.transform = 'translateX(' + exitX + 'px)';

    clearTimeout(walkOutTimer);
    walkOutTimer = window.setTimeout(function () {
      visitor.style.transition = 'transform ' + WALK_IN_MS + 'ms cubic-bezier(0.2, 0.7, 0.3, 1)';
      visitor.style.transform = 'translateX(' + visitorHomeX() + 'px)';
      clearTimeout(walkEndTimer);
      walkEndTimer = window.setTimeout(function () {
        visitor.classList.remove('visitor--walking');
      }, WALK_IN_MS);
    }, WALK_OUT_MS);
  }

  // The bench moves with the FRAME, not the visitor: it jumps to the same
  // edge the incoming frame slides in from, then glides to center over the
  // exact same duration/easing as the frame's own transition — so a new
  // bench arrives together with the new artwork, one synchronized move.
  function benchHomeX() {
    var obsRect = observatory.getBoundingClientRect();
    return obsRect.width / 2 - bench.offsetWidth / 2;
  }

  function settleBenchInstant() {
    bench.style.transition = 'none';
    bench.style.transform = 'translateX(' + benchHomeX() + 'px)';
    void bench.offsetWidth;
    bench.style.transition = '';
  }

  function slideBench(direction) {
    var obsRect = observatory.getBoundingClientRect();
    var offsideX = benchHomeX() + direction * (obsRect.width / 2 + 50);

    bench.style.transition = 'none';
    bench.style.transform = 'translateX(' + offsideX + 'px)';
    void bench.offsetWidth;

    bench.style.transition = 'transform ' + FRAME_SLIDE_MS + 'ms cubic-bezier(0.3, 0.1, 0.3, 1)';
    bench.style.transform = 'translateX(' + benchHomeX() + 'px)';
  }

  function setActiveIndex(i, opts) {
    var next = clamp(i, 0, frames.length - 1);
    var isInitial = !!(opts && opts.initial);
    if (next === activeIndex && !isInitial) return;
    var direction = next > activeIndex ? 1 : -1;
    var oldIndex = activeIndex;
    activeIndex = next;

    if (isInitial) {
      updateFrameClasses();
      settleBenchInstant();
    } else {
      slideFrames(oldIndex, next, direction);
      if (reduceMotion) {
        settleBenchInstant();
      } else {
        slideBench(direction);
      }
    }

    clearTimeout(sitTimer);
    clearTimeout(walkOutTimer);
    clearTimeout(walkEndTimer);
    visitor.classList.remove('visitor--sitting');

    if (isInitial || reduceMotion) {
      settleVisitorInstant();
    } else {
      walkAcross(direction);
    }

    sitTimer = window.setTimeout(function () {
      visitor.classList.add('visitor--sitting');
    }, 3000);
  }

  function openRoom(frame) {
    if (activeRoom) return;
    var room = document.getElementById(frame.dataset.target);
    if (!room) return;

    frame.classList.add('frame--selected');
    gallery.classList.add('gallery--transitioning');
    vignette.classList.add('vignette--active');
    clearTimeout(sitTimer);
    clearTimeout(walkEndTimer);

    var delay = reduceMotion ? 250 : 850;
    window.setTimeout(function () {
      room.classList.add('room--active');
      activeRoom = room;
      var back = room.querySelector('.room-back');
      if (back) back.focus();
    }, delay);
  }

  function closeRoom() {
    if (!activeRoom) return;
    activeRoom.classList.remove('room--active');
    activeRoom = null;

    frames.forEach(function (f) { f.classList.remove('frame--selected'); });
    gallery.classList.remove('gallery--transitioning');
    vignette.classList.remove('vignette--active');

    sitTimer = window.setTimeout(function () {
      visitor.classList.add('visitor--sitting');
    }, 3000);
  }

  frames.forEach(function (frame) {
    frame.addEventListener('click', function () { openRoom(frame); });
  });

  rooms.forEach(function (room) {
    var back = room.querySelector('.room-back');
    if (back) back.addEventListener('click', closeRoom);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeRoom(); return; }
    if (activeRoom) return;
    if (e.key === 'ArrowRight') setActiveIndex(activeIndex + 1);
    if (e.key === 'ArrowLeft') setActiveIndex(activeIndex - 1);
  });

  prevBtn.addEventListener('click', function () { if (!activeRoom) setActiveIndex(activeIndex - 1); });
  nextBtn.addEventListener('click', function () { if (!activeRoom) setActiveIndex(activeIndex + 1); });

  if (pointerFine) {
    gallery.addEventListener('mousemove', function (e) {
      if (activeRoom) return;
      var rect = gallery.getBoundingClientRect();
      var fraction = clamp((e.clientX - rect.left) / rect.width, 0, 0.999);
      setActiveIndex(Math.floor(fraction * frames.length));
    });
  } else {
    var touchStartX = 0;
    gallery.addEventListener('touchstart', function (e) {
      touchStartX = e.touches[0].clientX;
    }, { passive: true });
    gallery.addEventListener('touchend', function (e) {
      if (activeRoom) return;
      var delta = e.changedTouches[0].clientX - touchStartX;
      if (Math.abs(delta) < 40) return;
      setActiveIndex(activeIndex + (delta < 0 ? 1 : -1));
    });
  }

  // Subtle parallax on the ambient wall backdrop for a "looking around" feel.
  if (!reduceMotion && pointerFine) {
    window.addEventListener('mousemove', function (e) {
      var x = (e.clientX / window.innerWidth - 0.5) * 2;
      var y = (e.clientY / window.innerHeight - 0.5) * 2;
      hallwayBg.style.transform = 'translate(' + (x * -12) + 'px,' + (y * -8) + 'px)';
    });
  }

  window.addEventListener('resize', function () {
    settleVisitorInstant();
    settleBenchInstant();
  });

  setActiveIndex(Math.floor((frames.length - 1) / 2), { initial: true });
})();
