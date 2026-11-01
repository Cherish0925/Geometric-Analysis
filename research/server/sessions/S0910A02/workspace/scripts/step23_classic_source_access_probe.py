#!/usr/bin/env python3
"""Step 23: reproducible access probe for Anderson 1989 and Ye 1993 classics.

This script does not bypass access controls. It records stable metadata and whether
public endpoints expose theorem text/PDF in this runtime.
"""
import json
import urllib.parse
from pathlib import Path

import requests

records = []
urls = [
    "https://doi.org/10.1090/s0894-0347-1989-0999661-1",
    "https://www.ams.org/journals/jams/1989-2-03/S0894-0347-1989-0999661-1/",
    "https://www.ams.org/journals/jams/1989-2-03/S0894-0347-1989-0999661-1/S0894-0347-1989-0999661-1.pdf",
    "https://www.jstor.org/stable/1999661",
    "https://doi.org/10.1090/s0002-9947-1993-1108615-3",
    "https://www.ams.org/journals/tran/1993-338-02/S0002-9947-1993-1108615-3/",
    "https://www.ams.org/journals/tran/1993-338-02/S0002-9947-1993-1108615-3/S0002-9947-1993-1108615-3.pdf",
    "https://www.jstor.org/stable/2154433",
]
headers = {"User-Agent": "Mozilla/5.0", "Accept": "text/html,application/pdf,*/*"}
for url in urls:
    rec = {"url": url}
    try:
        r = requests.get(url, timeout=25, headers=headers, allow_redirects=True)
        rec.update({
            "status_code": r.status_code,
            "final_url": r.url,
            "content_type": r.headers.get("content-type"),
            "content_length": len(r.content),
            "starts_pdf": r.content[:4] == b"%PDF",
            "text_preview": (r.text[:300].replace("\n", " ") if "text" in (r.headers.get("content-type") or "") or "html" in (r.headers.get("content-type") or "") else ""),
        })
    except Exception as e:
        rec["error"] = repr(e)
    records.append(rec)

metadata = []
for doi in [
    "10.1090/s0894-0347-1989-0999661-1",
    "10.1090/s0002-9947-1993-1108615-3",
    "10.2307/2154433",
]:
    rec = {"doi": doi}
    try:
        endpoint = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
        r = requests.get(endpoint, timeout=25, headers=headers)
        rec["status_code"] = r.status_code
        if r.status_code == 200:
            m = r.json()["message"]
            rec["fields"] = {
                k: m.get(k)
                for k in ["title", "author", "container-title", "published-print", "volume", "issue", "page", "URL", "link", "abstract"]
            }
        else:
            rec["text_preview"] = r.text[:300]
    except Exception as e:
        rec["error"] = repr(e)
    metadata.append(rec)

out = {
    "title": "Step 23 classic source access probe",
    "purpose": "Record exact Anderson 1989 and Ye 1993 source-access/metadata status for Yau-26 route map.",
    "access_records": records,
    "crossref_metadata": metadata,
    "interpretation": [
        "Stable bibliographic metadata is available for both classics.",
        "In this runtime the AMS/JSTOR public endpoints did not provide directly readable theorem text/PDF when probed; any use of exact hypotheses still needs primary text or source-grade quotation.",
        "Do not infer Anderson Corollary B(4) or Ye theorem hypotheses from titles alone."
    ]
}
out_path = Path("Sessions/S0910A02/workspace/data/step23_classic_source_access_probe.json")
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(json.dumps(out, indent=2, ensure_ascii=False)[:6000])
print(f"Saved {out_path}")
