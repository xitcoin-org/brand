# Asset inventory

Inspected 5 September 2026 at source revision `8a3e841dbb1f78b0a15386bc1fbad411e3334241`. The [machine-readable manifest](asset-manifest.json) records byte lengths and SHA-256 identifiers. No artwork bytes were changed.

| File | Actual format | Dimensions | Notes |
|---|---|---|---|
| [assets/png/standard/xitcoin-symbol-200.png](assets/png/standard/xitcoin-symbol-200.png) | PNG | 200 × 200 | Standard RGBA PNG export |
| [assets/png/standard/xitcoin-symbol-3000.png](assets/png/standard/xitcoin-symbol-3000.png) | PNG | 3000 × 3000 | Standard RGBA PNG export |
| [assets/png/standard/xitcoin-symbol-32.png](assets/png/standard/xitcoin-symbol-32.png) | PNG | 32 × 32 | Standard RGBA PNG export |
| [assets/png/standard/xitcoin-symbol-500.png](assets/png/standard/xitcoin-symbol-500.png) | PNG | 500 × 500 | Standard RGBA PNG export |
| [assets/png/white/xitcoin-symbol-white-200.png](assets/png/white/xitcoin-symbol-white-200.png) | JPEG | 200 × 200 | JPEG bytes under a legacy .png filename; opaque white background |
| [assets/png/white/xitcoin-symbol-white-3000.png](assets/png/white/xitcoin-symbol-white-3000.png) | JPEG | 3000 × 3000 | JPEG bytes under a legacy .png filename; opaque white background |
| [assets/png/white/xitcoin-symbol-white-32.png](assets/png/white/xitcoin-symbol-white-32.png) | JPEG | 32 × 32 | JPEG bytes under a legacy .png filename; opaque white background |
| [assets/png/white/xitcoin-symbol-white-500.png](assets/png/white/xitcoin-symbol-white-500.png) | JPEG | 512 × 512 | JPEG bytes under a legacy .png filename; opaque white background |
| [assets/svg/xitcoin-symbol-white.svg](assets/svg/xitcoin-symbol-white.svg) | SVG | 3000 × 3000 | Raster wrapper, not path-based vector artwork |
| [assets/svg/xitcoin-symbol.svg](assets/svg/xitcoin-symbol.svg) | SVG | 3000 × 3000 | Raster wrapper, not path-based vector artwork |

## Format and provenance findings

Both SVG documents contain one embedded 1000 × 1000 PNG displayed on a
3000 × 3000 canvas, with no vector paths. XML inspection found no scripts,
event handlers, foreignObject elements or external image references in those
two files. Their embedded images were visually inspected. This is a scoped
inspection, not a guarantee about every renderer or future revision.

The files called `white` show the orange symbol on an opaque white background;
they are not monochrome reverse marks. The nominal 500-pixel white file is
actually 512 × 512. Consumers must check magic bytes and dimensions instead
of trusting legacy names. Keep existing URLs stable until a reviewed migration.

The standard exports contain gradients and raster colors (including a common
orange pixel of `#FB8C05`) that do not exactly equal the published palette.
Do not sample those pixels to redefine the official colors or recolor the
artwork automatically. A genuine vector master, a monochrome variant and any
color correction require an approved source from the brand owner.

The repository LICENSE dedicates assets under CC0 1.0, but SVG comments contain
an older “All rights reserved” notice. The owner must reconcile the source
notices; this inventory does not invent a new license or remove attribution.
