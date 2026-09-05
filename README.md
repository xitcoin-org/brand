# Xitcoin visual identity

This repository is the canonical source for Xitcoin (XTC) artwork. The
[Xitcoin Guide](https://xitcoin.gitbook.io/guide/) explains its public use.
No typography, wordmark or additional logo variant is defined here.

## Choose an asset

Use the [standard PNG exports](assets/png/standard/) for wallets, explorers
and token lists. Available square sizes are 32, 200, 500 and 3000 pixels.
Keep the original aspect ratio and choose enough source pixels for the final
display density. Preview at the actual display size.

Read the [asset inventory](ASSETS.md) before choosing legacy SVG or `white`
files: the SVGs wrap raster images, and the `white` files are not monochrome
marks. The white raster files contain JPEG data despite their `.png` names.

[Download specifications and SHA-256 identifiers](asset-manifest.json) bind
each integration to an exact source file. Production integrations should record
the full commit and file hash; a `main` URL can change. If a platform requires
a local copy, record its canonical source and check for reviewed updates.

## Official colors

| Color | Hex |
|---|---|
| Xitcoin Orange | `#FB8D00` |
| Xitcoin Graphite | `#53585E` |
| White | `#FFFFFF` |

These are the published palette values. Existing raster artwork includes
gradients and does not reproduce them as uniform fills. Do not change the
palette or repaint the artwork based on pixel sampling.

## Placement and integrity

- Preserve the square canvas, orientation and complete symbol.
- Keep adjacent text, controls and other marks outside the artwork canvas;
  leave visible breathing room and inspect the result at final size.
- No numeric clear-space ratio or minimum display size has been approved.
  The 32-pixel export is an available file, not an approved minimum-size rule.
- Use a quiet background with visible separation from the symbol. Inspect
  both light and dark themes; the legacy white-background files remain opaque.
- Do not crop, stretch, rotate, redraw, recolor, outline or add effects.
- Do not combine the symbol with another chain's mark or imply endorsement.

## Integration

Use Xitcoin for the project name and XTC for the public asset symbol. A logo
is not proof of asset identity: verify the network and complete contract or
native denomination through the Guide. Use alternative text such as
“Xitcoin symbol”; supply descriptive link text when the image is a control.
Do not create a bridge-specific or mainnet-specific symbol.

## Licensing and contact

The repository publishes the assets under [CC0 1.0 Universal](LICENSE).
[Legacy embedded notices](ASSETS.md#format-and-provenance-findings) still need
owner reconciliation. Usage rules describe official presentation and do not
add restrictions to the CC0 dedication or grant endorsement.

For source artwork and integration questions, use
[Brand repository issues](https://github.com/xitcoin-org/brand/issues).
Report security concerns through the Guide's responsible-disclosure process.
