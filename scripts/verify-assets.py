#!/usr/bin/env python3
"""Verify the published asset inventory without changing artwork or licensing."""
import hashlib
import json
from pathlib import Path


def verify(root: Path) -> int:
    manifest = json.loads((root / "asset-manifest.json").read_text())
    if manifest["schemaVersion"] != 1:
        raise ValueError("unsupported asset manifest schema")
    recorded = {}
    for asset in manifest["assets"]:
        name = asset["path"]
        path = root / name
        if name in recorded or not name.startswith("assets/"):
            raise ValueError(f"duplicate or invalid asset path: {name}")
        if path.is_symlink() or not path.resolve().is_relative_to((root / "assets").resolve()):
            raise ValueError(f"asset escapes inventory directory: {name}")
        data = path.read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest != asset["sha256"] or len(data) != asset["bytes"]:
            raise ValueError(f"asset integrity mismatch: {name}")
        recorded[name] = digest
    actual = {p.relative_to(root).as_posix() for p in (root / "assets").rglob("*") if p.is_file()}
    if actual != set(recorded):
        raise ValueError(f"asset inventory mismatch: {sorted(actual ^ set(recorded))}")
    lines = "".join(f"{digest}  {name}\n" for name, digest in sorted(recorded.items()))
    if hashlib.sha256(lines.encode()).hexdigest() != manifest["assetSetSha256"]:
        raise ValueError("asset set digest mismatch")
    return len(recorded)


if __name__ == "__main__":
    print(f"Verified {verify(Path(__file__).resolve().parents[1])} assets and asset set digest")
