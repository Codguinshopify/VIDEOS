/* Evoquex V12 — deterministic effects for one host-owned GSAP timeline.
 * Runtime: GSAP 3.14.2, DOM and SVG only. This file creates no timelines,
 * clocks, media playback, async setup, randomness or network requests.
 *
 * Adapted motion mechanics, HyperFrames / HeyGen, Apache-2.0:
 * https://github.com/heygen-com/hyperframes/tree/08ee1bd5ad59987a7f2525222683e24ca30971f9/registry/components
 *   iris-reveal: one radial proxy drives clip-path and the optional SVG rim.
 *   whip-pan-cut: one shared strip, power3 ramp, directional SVG blur envelope.
 *   modal-morph: supplied-rectangle FLIP with reciprocal child scaling.
 *   focus-blur-resolve: sharp type resolves from soft focus and scale.
 * Original archives / licenses remain in the project resource catalog.
 * GSAP is supplied by the host and retains its own license.
 */
(function (global) {
  'use strict';

  function engine() {
    if (!global.gsap) throw new Error('EvoquexFX requires the host GSAP instance.');
    return global.gsap;
  }

  function elements(selector) {
    if (typeof selector === 'string') {
      return Array.from(global.document.querySelectorAll(selector));
    }
    if (!selector) return [];
    if (selector.nodeType === 1) return [selector];
    return Array.from(selector);
  }

  function finite(value, fallback) {
    return Number.isFinite(value) ? value : fallback;
  }

  function duration(value, fallback) {
    return Math.max(0.001, finite(value, fallback));
  }

  function rect(value, name) {
    if (!value || !['x', 'y', 'width', 'height'].every(key => Number.isFinite(value[key]))) {
      throw new Error('EvoquexFX.flipBox requires a finite ' + name + ' rectangle.');
    }
    if (value.width <= 0 || value.height <= 0) {
      throw new Error('EvoquexFX.flipBox rectangle dimensions must be positive.');
    }
    return { x: value.x, y: value.y, width: value.width, height: value.height };
  }

  function letters(tl, selector, at, options = {}) {
    const nodes = elements(selector);
    const top = options.from === 'top';
    tl.from(nodes, {
      yPercent: top ? -110 : 110,
      rotationX: top ? -75 : 75,
      opacity: 0,
      transformOrigin: top ? '50% 0%' : '50% 100%',
      duration: duration(options.duration, 0.42),
      stagger: Math.max(0, finite(options.stagger, 0.025)),
      ease: 'power4.out',
      immediateRender: true,
    }, at);
    return tl;
  }

  function iris(tl, selector, at, options = {}) {
    const nodes = elements(selector);
    const width = Math.max(1, finite(options.width, 1080));
    const height = Math.max(1, finite(options.height, 1920));
    const cx = Math.max(0, Math.min(width, finite(options.cx, 540)));
    const cy = Math.max(0, Math.min(height, finite(options.cy, 960)));
    const finalRadius = Math.hypot(Math.max(cx, width - cx), Math.max(cy, height - cy)) * 1.02 + 2;
    const progress = { value: 0 };
    const circles = elements(options.borderSelector).flatMap(node =>
      node.localName === 'circle' ? [node] : Array.from(node.querySelectorAll('circle'))
    );

    // Host CSS must initially clip this layer to circle(0px at cx cy),
    // rather than opacity:0; opacity/visibility remain owned by the host.
    // A rim selector may point directly to a circle or to its SVG wrapper.
    circles.forEach(circle => {
      circle.setAttribute('cx', String(cx));
      circle.setAttribute('cy', String(cy));
      circle.setAttribute('r', '0');
    });

    function applyRadius() {
      const radius = Math.max(0, progress.value * finalRadius);
      const clip = 'circle(' + radius.toFixed(4) + 'px at ' + cx + 'px ' + cy + 'px)';
      nodes.forEach(node => { node.style.clipPath = clip; });
      circles.forEach(circle => { circle.setAttribute('r', radius.toFixed(4)); });
    }

    tl.fromTo(progress, { value: 0 }, {
      value: 1,
      duration: duration(options.duration, 0.58),
      ease: 'power2.inOut',
      immediateRender: false,
      onUpdate: applyRadius,
    }, at);
    return tl;
  }

  function whip(tl, strip, at, options = {}) {
    const nodes = elements(strip);
    const width = Math.max(1, finite(options.width, 1080));
    const length = duration(options.duration, 0.5);
    tl.fromTo(nodes, { x: 0 }, {
      x: -width,
      duration: length,
      ease: 'power3.inOut',
      immediateRender: false,
    }, at);

    const blurNodes = elements(options.blurSelector);
    if (blurNodes.length) {
      const blur = { value: 0 };
      const applyBlur = () => blurNodes.forEach(node => {
        node.setAttribute('stdDeviation', Math.max(0, blur.value).toFixed(4) + ' 0');
      });
      applyBlur();
      tl.fromTo(blur, { value: 0 }, {
        value: 18,
        duration: length / 2,
        ease: 'power3.in',
        immediateRender: false,
        onUpdate: applyBlur,
      }, at);
      tl.to(blur, {
        value: 0,
        duration: length / 2,
        ease: 'power3.out',
        onUpdate: applyBlur,
      }, at + length / 2);
    }
    return tl;
  }

  function flipBox(tl, selector, at, options = {}) {
    const gsap = engine();
    const nodes = elements(selector);
    const from = rect(options.from, 'from');
    const to = rect(options.to, 'to');
    const progress = { value: 0 };
    const children = options.innerSelector ? nodes.flatMap(node =>
      Array.from(node.querySelectorAll(options.innerSelector))
    ) : [];

    // Host CSS describes the final box: left/top and dimensions match `to`.
    // Supplied rects are in that parent's coordinate system, not viewport
    // measurements. No bounding-box reads or font/layout waits occur here.
    // Root transform and each opted-in child scale are exclusive channels.
    function applyBox() {
      const p = progress.value;
      const x = from.x + (to.x - from.x) * p;
      const y = from.y + (to.y - from.y) * p;
      const sx = (from.width + (to.width - from.width) * p) / to.width;
      const sy = (from.height + (to.height - from.height) * p) / to.height;
      gsap.set(nodes, {
        x: x - to.x,
        y: y - to.y,
        scaleX: sx,
        scaleY: sy,
        transformOrigin: '0 0',
      });
      if (children.length) {
        gsap.set(children, {
          scaleX: 1 / sx,
          scaleY: 1 / sy,
          transformOrigin: '0 0',
        });
      }
    }

    // Seed the supplied source rectangle once. Subsequent writes are an
    // absolute function of tween progress, so seeking backwards is safe.
    applyBox();
    tl.fromTo(progress, { value: 0 }, {
      value: 1,
      duration: duration(options.duration, 0.65),
      ease: 'power3.inOut',
      immediateRender: false,
      onUpdate: applyBox,
    }, at);
    return tl;
  }

  function draw(tl, selector, at, length = 0.5) {
    const nodes = elements(selector);
    nodes.forEach(node => {
      node.setAttribute('pathLength', '1');
      node.style.strokeDasharray = '1';
      node.style.strokeDashoffset = '1';
    });
    tl.fromTo(nodes, { strokeDashoffset: 1 }, {
      strokeDashoffset: 0,
      duration: duration(length, 0.5),
      ease: 'power2.inOut',
      immediateRender: false,
    }, at);
    return tl;
  }

  function focus(tl, selector, at, length = 0.45) {
    tl.fromTo(elements(selector), {
      filter: 'blur(8px)',
      scale: 1.12,
      opacity: 0,
    }, {
      filter: 'blur(0px)',
      scale: 1,
      opacity: 1,
      duration: duration(length, 0.45),
      ease: 'power3.out',
      immediateRender: false,
    }, at);
    return tl;
  }

  global.EvoquexFX = Object.freeze({ letters, iris, whip, flipBox, draw, focus });
})(window);
