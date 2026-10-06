#!/usr/bin/env python3
"""Regenera materials.json a partir de content/**/*.md (capçalera --- clau: valor ---)."""
import json, re, pathlib
root = pathlib.Path(__file__).parent
items = []
for p in sorted((root / "content").rglob("*.md")):
    t = p.read_text(encoding="utf-8")
    m = re.match(r"---\r?\n(.*?)\r?\n---\r?\n", t, re.S)
    meta = {}
    if m:
        for l in m.group(1).splitlines():
            if ":" in l:
                k, v = l.split(":", 1); meta[k.strip()] = v.strip()
    meta["path"] = p.relative_to(root).as_posix()
    meta.setdefault("title", p.stem)
    items.append(meta)
(root / "materials.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(items)} fitxes indexades")
