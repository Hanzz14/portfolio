# Portfolio – modern gallery (three.js r170)

## Preview (needs a local server – ES modules/textures don't load from file://)
    cd gallery
    python3 -m http.server 8080      # or: npx serve .
    # open http://localhost:8080
three.js is loaded from jsDelivr (pinned 0.170.0) via the import map at the top of `index.html`.
For fully offline use, download that version's `build/three.module.js` and `examples/jsm/` into `vendor/` and point the import map there.

## Structure
    index.html                 all code; edit ME / HISTORY / WORKS at the top of the module script
    assets/textures/           floor_*, wall_*, pillar_* (+ pillar_ao.jpg)
    assets/hdri/studio.hdr     environment lighting only (never the background)
    assets/projects/           project-01..04.webp (1920×1080), project-05.webp (1080×1920 portrait, About)
    tools/make_placeholders.py regenerates the grey placeholder covers

## Replacing covers
Overwrite the files in `assets/projects/` (same names) – no code change. For a portrait project set `orient:'portrait'` in WORKS and use a 1080×1920 image.

## Texture note
The uploaded pillar files were rotated relative to their names; they are renamed here by content:
uploaded `pillar_normal` → `pillar_color` (travertine) · `pillar_color` → `pillar_ao` (white) · `pillar_rough` → `pillar_normal` (flat) · `pillar_ao` → `pillar_rough` (near-black).

## Load failures
Any file that fails to load is logged to the console (`[gallery] FAILED TO LOAD: …`) and listed in a red box bottom-left. The surface falls back to a flat colour instead of going black.
