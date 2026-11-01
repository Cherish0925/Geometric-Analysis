#!/usr/bin/env python3
"""Probe exact public sources for Step 35 collapsed-front references.
Saves source/provenance snippets only. Does not treat unfetched facts as proofs.
"""
import json, re, urllib.request, urllib.parse, xml.etree.ElementTree as ET
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "step35_raw_sources"
RAW.mkdir(parents=True, exist_ok=True)
OUT = ROOT / "data" / "step35_source_probe_edge_weyl.json"

def arxiv_entry(arxiv_id):
    url = f"http://export.arxiv.org/api/query?id_list={urllib.parse.quote(arxiv_id)}"
    data = urllib.request.urlopen(url, timeout=20).read()
    root = ET.fromstring(data)
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    e = root.find('a:entry', ns)
    if e is None: return None
    return {
        'id': e.find('a:id', ns).text,
        'title': ' '.join(e.find('a:title', ns).text.split()),
        'summary': ' '.join(e.find('a:summary', ns).text.split()),
        'authors': [a.find('a:name', ns).text for a in e.findall('a:author', ns)],
        'published': e.find('a:published', ns).text,
        'updated': e.find('a:updated', ns).text,
        'links': [l.attrib for l in e.findall('a:link', ns)],
    }

def fetch_text(url, name):
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Qiushi research source probe'})
        with urllib.request.urlopen(req, timeout=25) as r:
            data = r.read()
        text = data.decode('utf-8', errors='replace')
        path = RAW / name
        path.write_text(text, encoding='utf-8')
        return {'ok': True, 'url': url, 'path': str(path), 'chars': len(text), 'head': text[:500]}
    except Exception as e:
        return {'ok': False, 'url': url, 'error': repr(e)}

ids = {
    'Atiyah_LeBrun_edge_cone':'1203.6389',
    'Emparan_Reall_generalized_Weyl':'hep-th/0110258',
    'Elvang_Horowitz_black_holes_compactified':'hep-th/0209051',
    'Elvang_Horowitz_black_holes_compactified_v2':'hep-th/0302085',
    'Yazadjiev_multi_black_hole_5D':'hep-th/0306044',
    'Weyl_card_diagrams':'hep-th/0506023'
}
entries = {}
for label, aid in ids.items():
    try:
        entries[label] = arxiv_entry(aid)
    except Exception as e:
        entries[label] = {'error': repr(e)}

fetches = {
    'edge_html': fetch_text('https://arxiv.org/html/1203.6389', 'Atiyah_LeBrun_1203.6389_html.txt'),
    'weyl_eprint': fetch_text('https://arxiv.org/e-print/hep-th/0110258', 'Generalized_Weyl_hep-th_0110258_eprint.bin.txt'),
    'weyl_html': fetch_text('https://arxiv.org/html/hep-th/0110258', 'Generalized_Weyl_hep-th_0110258_html.txt'),
}

# Extract formula-like snippets from edge html if present.
edge_text = ''
if fetches['edge_html'].get('ok'):
    edge_text = Path(fetches['edge_html']['path']).read_text(encoding='utf-8', errors='replace')
patterns = {
    'edge_Euler_formula_keywords': r'(Euler|Gauss|Bonnet|signature|self-intersection|cone angle|edge-cone|\u03b2|beta)',
    'edge_theorem': r'(Theorem\s+[0-9A-Za-z.]+|THEOREM|Theorem)',
}
edge_snippets = []
if edge_text:
    plain = re.sub(r'<[^>]+>', ' ', edge_text)
    plain = re.sub(r'\s+', ' ', plain)
    for pat_name, pat in patterns.items():
        for m in re.finditer(pat, plain, flags=re.I):
            a=max(0,m.start()-400); b=min(len(plain),m.end()+600)
            edge_snippets.append({'pattern': pat_name, 'snippet': plain[a:b]})
            if len(edge_snippets) >= 12:
                break
        if len(edge_snippets) >= 12:
            break

result = {
    'title': 'Step 35 source probe: edge-cone and Weyl/rod references',
    'entries': entries,
    'fetches': fetches,
    'edge_snippets': edge_snippets,
    'provisional_source_status': {
        'edge_cone': 'arXiv entry 1203.6389 identified as Atiyah-LeBrun Curvature, Cones, and Characteristic Numbers; formula extraction may require PDF/LaTeX inspection if HTML unavailable.',
        'generalized_weyl': 'arXiv entry hep-th/0110258 identified as Emparan-Reall Generalized Weyl Solutions; establishes a source target for rod/Weyl structure, but detailed regularity conditions still need reading.',
        'israel_khan_periodic': 'Search identified related black-hole compactification/multi-black-hole sources but not a direct Myers periodic-array source; strut-free periodic possibility remains unverified in session.'
    }
}
OUT.write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({'output': str(OUT), 'labels': list(entries.keys()), 'edge_fetch_ok': fetches['edge_html'].get('ok'), 'weyl_html_ok': fetches['weyl_html'].get('ok'), 'snippets': len(edge_snippets)}, indent=2))
