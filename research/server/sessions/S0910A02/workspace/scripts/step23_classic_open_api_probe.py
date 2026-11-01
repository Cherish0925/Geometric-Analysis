#!/usr/bin/env python3
"""Step 23: bounded public API/source probe for Anderson 1989 and Ye 1993.
No paywall bypass; records whether open scholarly APIs or JSTOR PDF endpoints expose usable text.
"""
import json, urllib.parse
from pathlib import Path
import requests

headers = {"User-Agent":"Mozilla/5.0 (Qiushi research metadata probe)", "Accept":"application/json,text/html,application/pdf,*/*"}
queries = {
    "anderson": {
        "title": "Ricci curvature bounds and Einstein metrics on compact manifolds",
        "doi": "10.1090/s0894-0347-1989-0999661-1",
        "jstor": "1999661",
    },
    "ye": {
        "title": "Ricci flow, Einstein metrics and space forms",
        "doi": "10.1090/s0002-9947-1993-1108615-3",
        "jstor": "2154433",
    }
}

def get(url, accept=None):
    h = dict(headers)
    if accept:
        h["Accept"] = accept
    rec = {"url": url}
    try:
        r = requests.get(url, headers=h, timeout=25, allow_redirects=True)
        rec.update({
            "status_code": r.status_code,
            "final_url": r.url,
            "content_type": r.headers.get("content-type"),
            "length": len(r.content),
            "starts_pdf": r.content[:4] == b"%PDF",
        })
        ct = r.headers.get("content-type") or ""
        if "json" in ct:
            try: rec["json_preview"] = json.dumps(r.json(), ensure_ascii=False)[:2000]
            except Exception: rec["text_preview"] = r.text[:1000]
        elif "text" in ct or "html" in ct:
            rec["text_preview"] = r.text[:1000].replace("\n", " ")
    except Exception as e:
        rec["error"] = repr(e)
    return rec

records = {}
for key, q in queries.items():
    titleq = urllib.parse.quote(q["title"])
    doiq = urllib.parse.quote(q["doi"], safe="")
    records[key] = []
    records[key].extend([
        get(f"https://www.jstor.org/stable/pdf/{q['jstor']}.pdf", "application/pdf,*/*"),
        get(f"https://api.openalex.org/works/doi:{urllib.parse.quote(q['doi'], safe=':/')}", "application/json"),
        get(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{urllib.parse.quote(q['doi'], safe='')}?fields=title,authors,year,venue,abstract,openAccessPdf,externalIds", "application/json"),
        get(f"https://api.crossref.org/works?query.title={titleq}&rows=5", "application/json"),
    ])

out = {"title":"Step 23 classic open API probe", "records": records}
out_path = Path("Sessions/S0910A02/workspace/data/step23_classic_open_api_probe.json")
out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(json.dumps(out, indent=2, ensure_ascii=False)[:8000])
print(f"Saved {out_path}")
