#!/usr/bin/env python3
"""Exact-source access probe for Step 32 classification bypass.

This script attempts lightweight HTTP access to exact URLs named in the Qiushi-Yau26
research dossier. It does not interpret the papers; it only records whether this
runtime can fetch source text/PDF/HTML for later source-grade reading.
"""
from __future__ import annotations

import json
import os
import re
import time
import urllib.request
import urllib.error

URLS = [
    {
        "label": "LeBrun-Ozuch 2026 arxiv html",
        "url": "https://arxiv.org/html/2601.19215v2",
        "need": "Theorem B hypotheses for Desingularizations of Conformally Kaehler, Einstein Orbifolds",
    },
    {
        "label": "LeBrun-Ozuch 2026 arxiv abs",
        "url": "https://arxiv.org/abs/2601.19215v2",
        "need": "metadata and abstract",
    },
    {
        "label": "Chen-LeBrun-Weber arxiv abs",
        "url": "https://arxiv.org/abs/0705.0710",
        "need": "On conformally Kähler, Einstein manifolds: Theorem A/Corollary 2",
    },
    {
        "label": "Chen-LeBrun-Weber arxiv pdf",
        "url": "https://arxiv.org/pdf/0705.0710",
        "need": "full PDF for source-grade reading if reachable",
    },
    {
        "label": "OSS 2016 JDG landing",
        "url": "https://projecteuclid.org/journals/journal-of-differential-geometry/volume-102/issue-1/Compact-moduli-spaces-of-del-Pezzo-surfaces-and-K%c3%a4hler-Einstein/10.4310/jdg/1456754013.full",
        "need": "Odaka-Spotti-Sun full text/landing page",
    },
    {
        "label": "Spotti-Sun explicit GH compactifications arxiv abs",
        "url": "https://arxiv.org/abs/1603.02995",
        "need": "follow-up explicit compactification source if identifier matches",
    },
]

KEYWORDS = [
    "Theorem B", "Hermitian", "Kähler", "Kaehler", "anti-self-dual", "Odaka", "Spotti", "Sun",
    "Page", "Chen", "LeBrun", "Weber", "del Pezzo", "Corollary", "Theorem A",
]


def fetch(url: str, max_bytes: int = 250000, timeout: int = 25) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "QiushiResearchProbe/1.0"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status = getattr(resp, "status", None)
            headers = dict(resp.headers.items())
            content = resp.read(max_bytes)
            elapsed = time.time() - t0
            ctype = headers.get("Content-Type", "")
            text = ""
            if "text" in ctype or "html" in ctype or content[:5] != b"%PDF-":
                text = content.decode("utf-8", errors="replace")
            keyword_hits = {}
            for kw in KEYWORDS:
                if text:
                    hits = [m.start() for m in re.finditer(re.escape(kw), text, flags=re.IGNORECASE)]
                    keyword_hits[kw] = len(hits)
            return {
                "ok": True,
                "status": status,
                "elapsed_sec": round(elapsed, 3),
                "content_type": ctype,
                "bytes_read": len(content),
                "starts_with_pdf": content[:5] == b"%PDF-",
                "final_url": resp.geturl(),
                "keyword_hits": keyword_hits,
                "text_preview": text[:1200] if text else "<binary or PDF>",
            }
    except Exception as e:  # noqa: BLE001
        return {
            "ok": False,
            "error_type": type(e).__name__,
            "error": str(e),
        }


def main() -> None:
    results = []
    for item in URLS:
        got = fetch(item["url"])
        results.append({**item, **got})
    out = "Sessions/S0910A02/workspace/data/step32_exact_source_access_probe.json"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    payload = {
        "title": "Step 32 exact source access probe",
        "scope": "Access/provenance only; not a substitute for reading the sources.",
        "results": results,
    }
    with open(out, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    print(f"\nSaved to {out}")

if __name__ == "__main__":
    main()
