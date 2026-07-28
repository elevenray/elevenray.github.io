(function () {
  var dungeon = document.getElementById('dungeon');
  var floor = document.getElementById('room-floor');
  var vignette = document.getElementById('vignette');
  var portals = Array.prototype.slice.call(document.querySelectorAll('.portal'));
  var rooms = Array.prototype.slice.call(document.querySelectorAll('.room'));
  var player = document.getElementById('player');
  var playerSprite = document.getElementById('player-sprite');
  var interactHint = document.getElementById('interact-hint');
  var touchInteractBtn = document.getElementById('touch-interact');
  var portalName = document.getElementById('portal-name');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var SPEED_PX_S = 150;
  var NEAR_PX = 68;
  var ROOM_OPEN_DELAY = reduceMotion ? 200 : 750;

  // Pixel-art sprite: a 6-frame walk cycle per one of 8 compass facings,
  // plus a single standing frame shown whenever the player isn't moving.
  var SPRITE_BASE = 'static/images/visitor/';
  var DIRECTIONS = ['east', 'south-east', 'south', 'south-west', 'west', 'north-west', 'north', 'north-east'];
  var WALK_FRAME_MS = 120;
  var WALK_FRAMES = {};
  var STATIC_FRAME = {};
  DIRECTIONS.forEach(function (dir) {
    WALK_FRAMES[dir] = [0, 1, 2, 3, 4, 5].map(function (i) { return SPRITE_BASE + dir + '-' + i + '.png'; });
    STATIC_FRAME[dir] = SPRITE_BASE + dir + '-static.png';
  });

  var pos = { x: 50, y: 82 };
  var facing = 'south';
  var moving = false;
  var walkFrameTimer = null;
  var walkFrameIndex = 0;
  var heldKeys = {};
  var touchTarget = null;
  var activeRoom = null;
  var nearPortal = null;
  var hoveredPortal = null;

  function angleToDirection(dx, dy) {
    var deg = (Math.atan2(dy, dx) * 180 / Math.PI + 360) % 360;
    var idx = Math.round(deg / 45) % 8;
    return DIRECTIONS[idx];
  }

  function setSpriteFrame(src) {
    if (playerSprite.getAttribute('src') !== src) playerSprite.setAttribute('src', src);
  }

  function startWalkFrames() {
    if (walkFrameTimer || reduceMotion) return;
    walkFrameIndex = 0;
    walkFrameTimer = window.setInterval(function () {
      walkFrameIndex = (walkFrameIndex + 1) % WALK_FRAMES[facing].length;
      setSpriteFrame(WALK_FRAMES[facing][walkFrameIndex]);
    }, WALK_FRAME_MS);
  }

  function stopWalkFrames() {
    clearInterval(walkFrameTimer);
    walkFrameTimer = null;
    setSpriteFrame(STATIC_FRAME[facing]);
  }

  function applyPosition() {
    player.style.left = pos.x + '%';
    player.style.top = pos.y + '%';
  }

  function clamp(n, min, max) { return Math.min(Math.max(n, min), max); }

  function getInputVector() {
    var x = 0, y = 0;
    if (heldKeys.left) x -= 1;
    if (heldKeys.right) x += 1;
    if (heldKeys.up) y -= 1;
    if (heldKeys.down) y += 1;
    if (x === 0 && y === 0 && touchTarget) {
      var rect = floor.getBoundingClientRect();
      var dx = (touchTarget.x - pos.x) / 100 * rect.width;
      var dy = (touchTarget.y - pos.y) / 100 * rect.height;
      if (Math.hypot(dx, dy) > 6) { x = dx; y = dy; }
    }
    return { x: x, y: y };
  }

  function updateMovement(dt) {
    if (activeRoom) return;
    var input = getInputVector();
    var mag = Math.hypot(input.x, input.y);

    if (mag < 0.001) {
      if (moving) { moving = false; player.classList.remove('player--walking'); stopWalkFrames(); }
      return;
    }

    var unitX = input.x / mag;
    var unitY = input.y / mag;
    facing = angleToDirection(input.x, input.y);

    if (!moving) { moving = true; player.classList.add('player--walking'); startWalkFrames(); }
    if (reduceMotion) setSpriteFrame(STATIC_FRAME[facing]);

    var rect = floor.getBoundingClientRect();
    var pxDelta = SPEED_PX_S * dt;
    // Y is clamped to the floor band only — the top of the room is the
    // back wall the portals are set into, not walkable space.
    pos.x = clamp(pos.x + (unitX * pxDelta / rect.width) * 100, 4, 96);
    pos.y = clamp(pos.y + (unitY * pxDelta / rect.height) * 100, 38, 97);
    applyPosition();
  }

  function updateProximity() {
    var rect = floor.getBoundingClientRect();
    var px = { x: rect.width * pos.x / 100, y: rect.height * pos.y / 100 };
    var best = null, bestDist = Infinity;

    portals.forEach(function (p) {
      var archRect = p.querySelector('.portal-arch').getBoundingClientRect();
      var px2 = { x: archRect.left + archRect.width / 2 - rect.left, y: archRect.bottom - rect.top };
      var dist = Math.hypot(px.x - px2.x, px.y - px2.y);
      if (dist < bestDist) { bestDist = dist; best = p; }
    });

    // A mouse hovering a portal counts as "near" too, same as the sprite
    // walking up to it — whichever is active wins (hover takes priority
    // since it's a deliberate cursor action).
    var proximityNear = best && bestDist < NEAR_PX;
    var effective = hoveredPortal || (proximityNear ? best : null);
    var isNear = effective && !activeRoom;

    portals.forEach(function (p) { p.classList.toggle('portal--near', isNear && p === effective); });

    if (isNear) {
      nearPortal = effective;
      var archRect = effective.querySelector('.portal-arch').getBoundingClientRect();
      interactHint.classList.add('is-visible');
      interactHint.style.left = (archRect.left + archRect.width / 2 - rect.left) + 'px';
      interactHint.style.top = (archRect.top - rect.top) + 'px';
      portalName.textContent = effective.dataset.role ? effective.dataset.title + ' — ' + effective.dataset.role : effective.dataset.title;
      portalName.style.setProperty('--accent', getComputedStyle(effective).getPropertyValue('--accent'));
      portalName.classList.add('is-visible');
    } else {
      nearPortal = null;
      interactHint.classList.remove('is-visible');
      portalName.classList.remove('is-visible');
    }
  }

  function openRoom(portalEl) {
    if (activeRoom) return;
    var room = document.getElementById(portalEl.dataset.target);
    if (!room) return;

    dungeon.classList.add('dungeon--transitioning');
    vignette.classList.add('vignette--active');
    interactHint.classList.remove('is-visible');
    portalName.classList.remove('is-visible');

    window.setTimeout(function () {
      room.classList.add('room--active');
      activeRoom = room;
      var back = room.querySelector('.room-back');
      if (back) back.focus();
    }, ROOM_OPEN_DELAY);
  }

  function closeRoom() {
    if (!activeRoom) return;
    activeRoom.classList.remove('room--active');
    activeRoom = null;
    dungeon.classList.remove('dungeon--transitioning');
    vignette.classList.remove('vignette--active');
  }

  portals.forEach(function (portal) {
    portal.addEventListener('click', function () { openRoom(portal); });
    portal.addEventListener('mouseenter', function () { hoveredPortal = portal; });
    portal.addEventListener('mouseleave', function () { if (hoveredPortal === portal) hoveredPortal = null; });
    portal.addEventListener('focus', function () { hoveredPortal = portal; });
    portal.addEventListener('blur', function () { if (hoveredPortal === portal) hoveredPortal = null; });
  });

  rooms.forEach(function (room) {
    var back = room.querySelector('.room-back');
    if (back) back.addEventListener('click', closeRoom);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeRoom(); return; }

    var key = e.key.toLowerCase();
    if (key === 'arrowleft' || key === 'a') { heldKeys.left = true; e.preventDefault(); }
    if (key === 'arrowright' || key === 'd') { heldKeys.right = true; e.preventDefault(); }
    if (key === 'arrowup' || key === 'w') { heldKeys.up = true; e.preventDefault(); }
    if (key === 'arrowdown' || key === 's') { heldKeys.down = true; e.preventDefault(); }

    if (key === 'enter' || key === ' ') {
      if (activeRoom) {
        e.preventDefault();
        closeRoom();
      } else if (nearPortal && document.activeElement && !document.activeElement.classList.contains('portal')) {
        e.preventDefault();
        openRoom(nearPortal);
      }
    }
  });

  document.addEventListener('keyup', function (e) {
    var key = e.key.toLowerCase();
    if (key === 'arrowleft' || key === 'a') heldKeys.left = false;
    if (key === 'arrowright' || key === 'd') heldKeys.right = false;
    if (key === 'arrowup' || key === 'w') heldKeys.up = false;
    if (key === 'arrowdown' || key === 's') heldKeys.down = false;
  });

  window.addEventListener('blur', function () { heldKeys = {}; touchTarget = null; });

  function setTouchTarget(clientX, clientY) {
    var rect = floor.getBoundingClientRect();
    touchTarget = {
      x: clamp((clientX - rect.left) / rect.width * 100, 0, 100),
      y: clamp((clientY - rect.top) / rect.height * 100, 0, 100)
    };
  }

  floor.addEventListener('touchstart', function (e) {
    if (activeRoom) return;
    var t = e.touches[0];
    setTouchTarget(t.clientX, t.clientY);
  }, { passive: true });

  floor.addEventListener('touchmove', function (e) {
    if (activeRoom) return;
    var t = e.touches[0];
    setTouchTarget(t.clientX, t.clientY);
  }, { passive: true });

  floor.addEventListener('touchend', function () { touchTarget = null; });

  if (touchInteractBtn) {
    touchInteractBtn.addEventListener('click', function () {
      if (nearPortal && !activeRoom) openRoom(nearPortal);
    });
  }

  applyPosition();
  setSpriteFrame(STATIC_FRAME[facing]);

  var last = null;
  function tick(now) {
    if (last === null) last = now;
    var dt = Math.min(now - last, 50) / 1000;
    last = now;
    updateMovement(dt);
    updateProximity();
    window.requestAnimationFrame(tick);
  }
  window.requestAnimationFrame(tick);
})();
