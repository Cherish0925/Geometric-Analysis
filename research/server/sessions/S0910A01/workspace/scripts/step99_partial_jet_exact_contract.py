#!/usr/bin/env python3
"""Exact-rational contraction check for Step99 same-factor partial tensor jets."""
from __future__ import annotations

import importlib.util
import json
import pathlib
import sys

import numpy as np
import sympy as sp

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"

# Import the partial-jet formulas. This module also writes its numerical JSON; that is harmless here.
_spec = importlib.util.spec_from_file_location("step99_partial", SCRIPT_DIR / "step99_tensor_partial_jets.py")
partial = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules[_spec.name] = partial
_spec.loader.exec_module(partial)

# Import Step96 coefficient arrays.
_spec2 = importlib.util.spec_from_file_location("step96_ab_exact", SCRIPT_DIR / "step96_kernel_plane_ab_map.py")
step96 = importlib.util.module_from_spec(_spec2)
assert _spec2.loader is not None
sys.modules[_spec2.name] = step96
_spec2.loader.exec_module(step96)


def rat(x: float) -> sp.Rational:
    if abs(float(x)) < 1e-15:
        return sp.Rational(0)
    return sp.Rational(str(float(x))).limit_denominator(10**6)

RCOEFF = {chir: np.empty(step96.RCOEFF[chir].shape, dtype=object) for chir in ["plus", "minus"]}
SCOEFF = {chir: np.empty(step96.SCOEFF[chir].shape, dtype=object) for chir in ["plus", "minus"]}
for chir in ["plus", "minus"]:
    for idx in np.ndindex(*step96.RCOEFF[chir].shape):
        RCOEFF[chir][idx] = rat(step96.RCOEFF[chir][idx])
    for idx in np.ndindex(*step96.SCOEFF[chir].shape):
        SCOEFF[chir][idx] = rat(step96.SCOEFF[chir][idx])


def embed_symbolic(K2: np.ndarray, sector: str) -> np.ndarray:
    H = np.empty((4,4,4,4), dtype=object)
    for idx in np.ndindex(4,4,4,4):
        H[idx] = sp.Rational(0)
    for a,c,p,q in np.ndindex(2,2,2,2):
        if sector == "AA":
            H[a,c,p,q] = K2[a,c,p,q]
        else:
            H[2+a,2+c,2+p,2+q] = K2[a,c,p,q]
    return H


def contract_coeff(C, H):
    out = np.empty((2,2), dtype=object)
    for a,b in np.ndindex(2,2):
        s = sp.Rational(0)
        for i,j,p,q in np.ndindex(4,4,4,4):
            s += C[a,b,i,j,p,q]*H[i,j,p,q]
        out[a,b] = sp.factor(sp.simplify(s))
    return out

results = {"step": 99, "purpose": "exact symbolic source/receiver contractions for actual same-factor partial tensor jets", "checks": {}}
max_nonzero = []
for name, K2 in partial.Kform.items():
    entry = {}
    for sector in ["AA", "BB"]:
        H = embed_symbolic(K2, sector)
        centry = {}
        for chir in ["plus", "minus"]:
            R = contract_coeff(RCOEFF[chir], H)
            S = contract_coeff(SCOEFF[chir], H)
            centry[f"R_{chir}"] = [[str(R[a,b]) for b in range(2)] for a in range(2)]
            centry[f"S_{chir}_over_pi2"] = [[str(S[a,b]) for b in range(2)] for a in range(2)]
            for arrname, Arr in [(f"R_{chir}", R), (f"S_{chir}", S)]:
                for idx in np.ndindex(2,2):
                    if sp.simplify(Arr[idx]) != 0:
                        max_nonzero.append({"tensor": name, "sector": sector, "functional": arrname, "idx": idx, "value": str(Arr[idx])})
        entry[sector] = centry
    results["checks"][name] = entry
results["nonzero_contractions"] = max_nonzero
results["conclusion"] = "All exact contractions vanish" if not max_nonzero else "Some contractions are nonzero"

out = DATA_DIR / "step99_partial_jet_exact_contract.json"
with open(out, "w") as f:
    json.dump(results, f, indent=2)
print(json.dumps({"conclusion": results["conclusion"], "nonzero_count": len(max_nonzero), "output": str(out)}, indent=2))
