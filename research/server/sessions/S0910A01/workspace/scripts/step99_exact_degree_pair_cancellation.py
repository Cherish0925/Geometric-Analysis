#!/usr/bin/env python3
"""
Step 99: exact fixed-degree cancellation certificate for implemented AA/BB tensor sums.

This strips the Step98 tensor calculation to its finite-dimensional algebra at a
fixed degree pair (ell_tensor, ell_scalar).  It uses exact rational Step96 source
and receiver coefficients, exact relative scalar-Hessian weights from the S^2
addition theorem, and integer electric/full-Lie magnetic seed matrices.  The heat
factor, eigenvalue denominator, and common tensor normalization are positive common
factors and are omitted.

The output tests whether the same-chirality cancellation B++=B-- occurs exactly
at each fixed degree pair in the implemented model, and records where the remaining
cross-chirality blocks live.
"""
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
DATA_DIR.mkdir(parents=True, exist_ok=True)

_spec = importlib.util.spec_from_file_location("step96_ab", SCRIPT_DIR / "step96_kernel_plane_ab_map.py")
step96 = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules[_spec.name] = step96
_spec.loader.exec_module(step96)


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

I = sp.Matrix([[1,0],[0,1]])
D = sp.Matrix([[1,0],[0,-1]])
O = sp.Matrix([[0,1],[1,0]])
Z = sp.Matrix([[0,0],[0,0]])
# Unit seed matrices; amplitude weights are supplied separately.
TENSOR_SEEDS = {
    # kind, seed -> 2x2 matrix; electric and magnetic have equal common amplitude^2/norm after Step94 repair.
    ("electric", "c2"): D,
    ("electric", "s2"): O,
    ("magnetic_full_lie", "c2"): O,
    ("magnetic_full_lie", "s2"): -D,
}
SCALAR_SEEDS = {"m0": I, "c2": D, "s2": O}


def node_sign(node: str, ell: int, seed: str) -> int:
    if node == "N":
        return 1
    base = 1 if ell % 2 == 0 else -1
    if seed == "s2":
        return -base
    return base


def scalar_weight(ell: int, seed: str) -> sp.Rational:
    if seed == "m0":
        mu = ell*(ell+1)
        return sp.Rational(2*mu, mu-2)  # H0^2 / (m=2 Hessian amplitude)^2
    return sp.Rational(1)


def zero_H():
    H = np.empty((4,4,4,4), dtype=object)
    for idx in np.ndindex(4,4,4,4):
        H[idx] = sp.Rational(0)
    return H


def tensor_scalar_H(T: sp.Matrix, S: sp.Matrix, sector: str):
    H = zero_H()
    if sector == "AA":
        for a,b,m,n in np.ndindex(2,2,2,2):
            H[a,b,2+m,2+n] += T[a,b]*S[m,n]
    elif sector == "BB":
        for m,n,a,b in np.ndindex(2,2,2,2):
            H[2+m,2+n,a,b] += T[m,n]*S[a,b]
    else:
        raise ValueError(sector)
    return H


def contract(C, H):
    out = np.empty((2,2), dtype=object)
    for a,b in np.ndindex(2,2):
        s = sp.Rational(0)
        for i,j,p,q in np.ndindex(4,4,4,4):
            s += C[a,b,i,j,p,q]*H[i,j,p,q]
        out[a,b] = sp.simplify(s)
    return out


def outer(A, B):
    T = np.empty((2,2,2,2), dtype=object)
    for a,b,c,d in np.ndindex(2,2,2,2):
        T[a,b,c,d] = sp.simplify(A[a,b]*B[c,d])
    return T


def add4(A, B, scale=sp.Rational(1)):
    for idx in np.ndindex(2,2,2,2):
        A[idx] = sp.simplify(A[idx] + scale*B[idx])


def norm_nonzero(A) -> list:
    nz=[]
    for idx in np.ndindex(2,2,2,2):
        v=sp.simplify(A[idx])
        if v != 0:
            nz.append({"idx": idx, "value": str(v)})
    return nz


def compact(A):
    K = [[A[0,0,0,0], A[0,0,1,1], A[0,0,0,1]],
         [A[1,1,0,0], A[1,1,1,1], A[1,1,0,1]],
         [A[0,1,0,0], A[0,1,1,1], A[0,1,0,1]]]
    return [[str(sp.simplify(x)) for x in row] for row in K]


def parse_pair(pair: str):
    return pair[0], pair[1]


def degree_response(sector: str, pair: str, lt: int, ls: int) -> dict:
    recA, recB = "N", "N"
    srcA, srcB = parse_pair(pair)
    if sector == "AA":
        T_rec_node, S_rec_node = recA, recB
        T_src_node, S_src_node = srcA, srcB
    else:
        T_rec_node, S_rec_node = recB, recA
        T_src_node, S_src_node = srcB, srcA
    raw = {ck: np.empty((2,2,2,2), dtype=object) for ck in ["++","+-","-+","--"]}
    for ck in raw:
        for idx in np.ndindex(2,2,2,2):
            raw[ck][idx] = sp.Rational(0)

    for kind in ["electric", "magnetic_full_lie"]:
        for tseed in ["c2", "s2"]:
            Tbase = TENSOR_SEEDS[(kind, tseed)]
            Trec = node_sign(T_rec_node, lt, tseed)*Tbase
            Tsrc = node_sign(T_src_node, lt, tseed)*Tbase
            for sseed in ["m0", "c2", "s2"]:
                w = scalar_weight(ls, sseed)
                Sbase = SCALAR_SEEDS[sseed]
                Srec_base = node_sign(S_rec_node, ls, sseed)*Sbase
                Ssrc_base = node_sign(S_src_node, ls, sseed)*Sbase
                Hrec = tensor_scalar_H(Trec, Srec_base, sector)
                Hsrc = tensor_scalar_H(Tsrc, Ssrc_base, sector)
                Rplus = contract(RCOEFF["plus"], Hrec)
                Rminus = contract(RCOEFF["minus"], Hrec)
                Splus = contract(SCOEFF["plus"], Hsrc)
                Sminus = contract(SCOEFF["minus"], Hsrc)
                terms = {"++": outer(Rplus,Splus), "+-": outer(Rplus,Sminus), "-+": outer(Rminus,Splus), "--": outer(Rminus,Sminus)}
                for ck, A in terms.items():
                    add4(raw[ck], A, w)

    return {
        "sector": sector, "pair": pair, "lt": lt, "ls": ls,
        "nonzero_counts": {ck: len(norm_nonzero(A)) for ck,A in raw.items()},
        "compact": {ck: compact(A) for ck,A in raw.items()},
        "same_zero_exact": len(norm_nonzero(raw["++"])) == 0 and len(norm_nonzero(raw["--"])) == 0,
    }


def main():
    cases=[]
    # Use ls>=2 so the m=2 scalar polarization exists; ls=1 belongs to a separate AB/one-form family and makes the relative m0/m2 weight undefined.
    for lt, ls in [(2,2),(2,3),(3,2),(4,5),(5,4),(8,7)]:
        for pair in ["NS","SN","SS"]:
            for sector in ["AA","BB"]:
                cases.append(degree_response(sector,pair,lt,ls))
    failures=[c for c in cases if not c["same_zero_exact"]]
    results={
        "step": 99,
        "purpose": "exact fixed-degree algebra for same-chirality cancellation in implemented tensor-scalar model",
        "normalization": "common heat/eigenvalue/tensor factors omitted; scalar m0 weight is 2*mu/(mu-2), c2/s2 weights 1; Step96 coefficients exact rational; only scalar degrees ls>=2 are included because m=2 polarizations are needed for this relative normalization",
        "cases": cases,
        "failure_count": len(failures),
        "failures": failures,
        "conclusion": "same-chirality ++/-- blocks vanish exactly for all tested fixed degree pairs in the implemented finite-dimensional algebra" if not failures else "some fixed-degree cases failed",
    }
    out=DATA_DIR/"step99_exact_degree_pair_cancellation.json"
    with open(out,"w") as f:
        json.dump(results,f,indent=2)
    # compact summary with active cross blocks at one representative degree
    rep=[c for c in cases if c["lt"]==2 and c["ls"]==2]
    print(json.dumps({"failure_count": len(failures), "representative_nonzero_counts": {f"{c['sector']}_{c['pair']}": c["nonzero_counts"] for c in rep}, "output": str(out), "conclusion": results["conclusion"]}, indent=2))

if __name__ == "__main__":
    main()
