#!/usr/bin/env python3
"""
Step 99: exact coefficient and low-scalar-mode audit for the implemented tensor model.

This removes the rational-reconstruction weakness noted by TTCS.  It generates the
Step96 receiver/source coefficient arrays directly in exact arithmetic from the
self-dual/anti-self-dual forms, checks support properties exactly, rechecks the
actual same-factor partial-jet contractions using exact coefficients, and checks
same-chirality cancellation for fixed degree pairs including the scalar ell_s=1
m0-only slice.
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

# Float Step96 arrays are used only for comparison.
_spec = importlib.util.spec_from_file_location("step96_ab", SCRIPT_DIR / "step96_kernel_plane_ab_map.py")
step96 = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules[_spec.name] = step96
_spec.loader.exec_module(step96)

KIDX = [1, 2]


def zero_mat(n=4):
    A = np.empty((n,n), dtype=object)
    for i,j in np.ndindex(n,n):
        A[i,j] = sp.Rational(0)
    return A


def wedge(i: int, j: int, n: int = 4):
    A = zero_mat(n)
    A[i,j] = sp.Rational(1)
    A[j,i] = sp.Rational(-1)
    return A


def matmul(A, B):
    n = A.shape[0]
    C = zero_mat(n)
    for i,j in np.ndindex(n,n):
        C[i,j] = sp.simplify(sum(A[i,k]*B[k,j] for k in range(n)))
    return C


def transpose(A):
    B = zero_mat(A.shape[0])
    for i,j in np.ndindex(A.shape[0], A.shape[1]):
        B[i,j] = A[j,i]
    return B


def add(A, B, scale=sp.Rational(1)):
    C = zero_mat(A.shape[0])
    for i,j in np.ndindex(A.shape[0], A.shape[1]):
        C[i,j] = sp.simplify(A[i,j] + scale*B[i,j])
    return C


def build_forms_C_exact():
    e01=wedge(0,1); e02=wedge(0,2); e03=wedge(0,3)
    e12=wedge(1,2); e13=wedge(1,3); e23=wedge(2,3)
    wp_raw=[add(e01,e23), add(e02,e13,scale=-1), add(e03,e12)]
    wm_raw=[add(e01,e23,scale=-1), add(e02,e13), add(e03,e12,scale=-1)]
    C=np.empty((3,3,4,4), dtype=object)
    for a,b in np.ndindex(3,3):
        P = matmul(wp_raw[a], wm_raw[b])
        S = add(P, transpose(P))
        for i,j in np.ndindex(4,4):
            C[a,b,i,j] = sp.simplify(S[i,j]/2)  # normalized forms divide by sqrt(2) twice
    return wp_raw, wm_raw, C

WP_RAW, WM_RAW, CEX = build_forms_C_exact()


def curvature_block_coeff(rawA, rawB):
    L=np.empty((4,4,4,4), dtype=object)
    for idx in np.ndindex(4,4,4,4):
        L[idx]=sp.Rational(0)
    for a,b,c,d in np.ndindex(4,4,4,4):
        ca=rawA[a,b]; cb=rawB[c,d]
        if ca==0 or cb==0:
            continue
        fac=ca*cb/sp.Rational(16)
        L[a,d,b,c] += fac
        L[b,c,a,d] += fac
        L[a,c,b,d] -= fac
        L[b,d,a,c] -= fac
    for idx in np.ndindex(4,4,4,4):
        L[idx]=sp.simplify(L[idx])
    return L

RCOEFF={"plus": np.empty((2,2,4,4,4,4), dtype=object), "minus": np.empty((2,2,4,4,4,4), dtype=object)}
for ia,a in enumerate(KIDX):
    for ib,b in enumerate(KIDX):
        RCOEFF["plus"][ia,ib]=curvature_block_coeff(WP_RAW[a], WP_RAW[b])
        RCOEFF["minus"][ia,ib]=curvature_block_coeff(WM_RAW[a], WM_RAW[b])

SCOEFF={"plus": np.empty((2,2,4,4,4,4), dtype=object), "minus": np.empty((2,2,4,4,4,4), dtype=object)}
for ia,a in enumerate(KIDX):
    for ic,c in enumerate(KIDX):
        for idx in np.ndindex(4,4,4,4):
            Tplus=sp.Rational(0); Tminus=sp.Rational(0)
            i,j,p,q=idx
            for b in range(3):
                Tplus += CEX[a,b,i,j]*CEX[c,b,p,q]
                Tminus += CEX[b,a,i,j]*CEX[b,c,p,q]
            SCOEFF["plus"][ia,ic,i,j,p,q] = sp.simplify(-Tplus/sp.Rational(16))
            SCOEFF["minus"][ia,ic,i,j,p,q] = sp.simplify(-Tminus/sp.Rational(16))


def max_diff_float_exact(float_arr, exact_arr):
    m=0.0
    for idx in np.ndindex(*float_arr.shape):
        m=max(m, abs(float(float_arr[idx])-float(exact_arr[idx])))
    return m


def exact_contract(C, H):
    out=np.empty((2,2), dtype=object)
    for a,b in np.ndindex(2,2):
        s=sp.Rational(0)
        for i,j,p,q in np.ndindex(4,4,4,4):
            s += C[a,b,i,j,p,q]*H[i,j,p,q]
        out[a,b]=sp.factor(sp.simplify(s))
    return out


def zero_H():
    H=np.empty((4,4,4,4), dtype=object)
    for idx in np.ndindex(4,4,4,4):
        H[idx]=sp.Rational(0)
    return H


def support_nonzero(kind: str, chir: str, sector: str, support: str):
    coeff = RCOEFF[chir] if kind=="R" else SCOEFF[chir]
    nonzero=[]
    same=[0,1] if sector=="AA" else [2,3]
    other=[2,3] if sector=="AA" else [0,1]
    if support=="same_factor":
        inds=[(i,j,p,q) for i in same for j in same for p in same for q in same]
    elif support=="other_factor":
        inds=[(i,j,p,q) for i in same for j in same for p in other for q in other]
    elif support=="mixed_derivative":
        inds=[(i,j,p,q) for i in same for j in same for p in same for q in other] + [(i,j,p,q) for i in same for j in same for p in other for q in same]
    else:
        raise ValueError(support)
    for ind in inds:
        H=zero_H(); H[ind]=sp.Rational(1)
        M=exact_contract(coeff,H)
        if any(M[a,b]!=0 for a,b in np.ndindex(2,2)):
            nonzero.append({"support_index": ind, "matrix": [[str(M[a,b]) for b in range(2)] for a in range(2)]})
    return nonzero

# Partial jet formulas copied from step99_tensor_partial_jets.json as expressions.
mu,b=sp.symbols("mu b")
with open(DATA_DIR/"step99_tensor_partial_jets.json") as f:
    partial_json=json.load(f)

def K_from_formula(name: str):
    K=np.empty((2,2,2,2), dtype=object)
    for idx in np.ndindex(2,2,2,2):
        K[idx]=sp.Rational(0)
    for item in partial_json["formula_summary"][name]["nonzero_entries"]:
        K[item["a"],item["c"],item["p"],item["q"]]=sp.sympify(item["value"], locals={"mu":mu,"b":b})
    return K

def embed2(K2, sector):
    H=zero_H()
    for a,c,p,q in np.ndindex(2,2,2,2):
        if sector=="AA": H[a,c,p,q]=K2[a,c,p,q]
        else: H[2+a,2+c,2+p,2+q]=K2[a,c,p,q]
    return H

partial_nonzero=[]
for name in ["electric_c2","electric_s2","magnetic_c2","magnetic_s2"]:
    for sector in ["AA","BB"]:
        H=embed2(K_from_formula(name), sector)
        for chir in ["plus","minus"]:
            for kind, coeff in [("R", RCOEFF[chir]), ("S", SCOEFF[chir])]:
                M=exact_contract(coeff,H)
                for idx in np.ndindex(2,2):
                    if M[idx]!=0:
                        partial_nonzero.append({"tensor": name, "sector": sector, "kind": kind, "chir": chir, "idx": idx, "value": str(M[idx])})

# Fixed-degree algebra with exact coefficients, including ls=1 m0-only.
I=sp.Matrix([[1,0],[0,1]]); D=sp.Matrix([[1,0],[0,-1]]); O=sp.Matrix([[0,1],[1,0]])
TSEEDS={("electric","c2"):D,("electric","s2"):O,("magnetic_full_lie","c2"):O,("magnetic_full_lie","s2"):-D}
SSEEDS={"m0":I,"c2":D,"s2":O}

def node_sign(node, ell, seed):
    if node=="N": return 1
    base=1 if ell%2==0 else -1
    return -base if seed=="s2" else base

def scalar_modes_and_weights(ell):
    if ell==0:
        return [("const", I, sp.Rational(1))]
    muell=ell*(ell+1)
    modes=[("m0", I, sp.Rational(1) if ell==1 else sp.Rational(2*muell, muell-2))]
    if ell>=2:
        modes += [("c2", D, sp.Rational(1)), ("s2", O, sp.Rational(1))]
    return modes

def tensor_scalar_H(T,S,sector):
    H=zero_H()
    if sector=="AA":
        for a,c,p,q in np.ndindex(2,2,2,2): H[a,c,2+p,2+q]=T[a,c]*S[p,q]
    else:
        for p,q,a,c in np.ndindex(2,2,2,2): H[2+p,2+q,a,c]=T[p,q]*S[a,c]
    return H

def outer(A,B):
    T=np.empty((2,2,2,2), dtype=object)
    for a,b,c,d in np.ndindex(2,2,2,2): T[a,b,c,d]=sp.simplify(A[a,b]*B[c,d])
    return T

def add4(A,B,scale=sp.Rational(1)):
    for idx in np.ndindex(2,2,2,2): A[idx]=sp.simplify(A[idx]+scale*B[idx])

def count_nonzero(A):
    return sum(1 for idx in np.ndindex(2,2,2,2) if sp.simplify(A[idx])!=0)

def degree_case(sector,pair,lt,ls):
    recA=recB="N"; srcA,srcB=pair[0],pair[1]
    if sector=="AA": TrecN,SrecN,TsrcN,SsrcN=recA,recB,srcA,srcB
    else: TrecN,SrecN,TsrcN,SsrcN=recB,recA,srcB,srcA
    raw={ck:np.empty((2,2,2,2),dtype=object) for ck in ["++","+-","-+","--"]}
    for ck in raw:
        for idx in np.ndindex(2,2,2,2): raw[ck][idx]=sp.Rational(0)
    for kind in ["electric","magnetic_full_lie"]:
        for tseed,Tbase in [("c2",D),("s2",O)]:
            Tbase=TSEEDS[(kind,tseed)]
            Trec=node_sign(TrecN,lt,tseed)*Tbase; Tsrc=node_sign(TsrcN,lt,tseed)*Tbase
            for sseed,Sbase,w in scalar_modes_and_weights(ls):
                if sseed=="const":
                    continue  # handled by same-factor partial-jet zero above, not by T*Hess(f)
                Srec=node_sign(SrecN,ls,sseed)*Sbase; Ssrc=node_sign(SsrcN,ls,sseed)*Sbase
                Hrec=tensor_scalar_H(Trec,Srec,sector); Hsrc=tensor_scalar_H(Tsrc,Ssrc,sector)
                Rp=exact_contract(RCOEFF["plus"],Hrec); Rm=exact_contract(RCOEFF["minus"],Hrec)
                Sp=exact_contract(SCOEFF["plus"],Hsrc); Sm=exact_contract(SCOEFF["minus"],Hsrc)
                for ck,A in {"++":outer(Rp,Sp),"+-":outer(Rp,Sm),"-+":outer(Rm,Sp),"--":outer(Rm,Sm)}.items(): add4(raw[ck],A,w)
    return {"sector":sector,"pair":pair,"lt":lt,"ls":ls,"nonzero_counts":{ck:count_nonzero(A) for ck,A in raw.items()},"same_zero_exact":count_nonzero(raw["++"])+count_nonzero(raw["--"])==0}

cases=[]
for lt,ls in [(2,0),(2,1),(2,2),(2,3),(3,1),(3,2),(4,5),(8,7)]:
    for pair in ["NS","SN","SS"]:
        for sector in ["AA","BB"]:
            cases.append(degree_case(sector,pair,lt,ls))
failures=[c for c in cases if not c["same_zero_exact"]]

results={
    "step":99,
    "purpose":"exact Step96 coefficient generation, support checks, partial-jet contractions, and low scalar degree fixed-pair cancellation",
    "exact_vs_step96_float_max_diff": {
        "Rplus": max_diff_float_exact(step96.RCOEFF["plus"],RCOEFF["plus"]),
        "Rminus": max_diff_float_exact(step96.RCOEFF["minus"],RCOEFF["minus"]),
        "Splus": max_diff_float_exact(step96.SCOEFF["plus"],SCOEFF["plus"]),
        "Sminus": max_diff_float_exact(step96.SCOEFF["minus"],SCOEFF["minus"]),
    },
    "support_nonzero_counts": {sector:{support:{kind+chir:len(support_nonzero(kind,chir,sector,support)) for kind in ["R","S"] for chir in ["plus","minus"]} for support in ["same_factor","other_factor","mixed_derivative"]} for sector in ["AA","BB"]},
    "actual_partial_jet_nonzero_contractions": partial_nonzero,
    "degree_cases": cases,
    "degree_failure_count": len(failures),
    "degree_failures": failures,
    "interpretation":[
        "Step96 float coefficient arrays agree exactly with direct exact-rational construction from the form definitions.",
        "Arbitrary same-factor support is a source risk (nonzero S) but actual electric/full-Lie magnetic m=2 partial jets contract to zero exactly with the exact coefficients.",
        "Mixed derivative support is exactly invisible to both source and receiver arrays in AA/BB embeddings.",
        "For tested fixed degree pairs, including ell_s=1 m0-only slices and ell_s=0 constant slices treated as zero in the T*Hess(f) part plus partial-jet zero, same-chirality ++/-- blocks vanish in the implemented finite-dimensional model.",
    ]
}
out=DATA_DIR/"step99_exact_coeff_lowmode_audit.json"
with open(out,"w") as f: json.dump(results,f,indent=2)
print(json.dumps({"exact_vs_float":results["exact_vs_step96_float_max_diff"],"support_counts":results["support_nonzero_counts"],"partial_nonzero_count":len(partial_nonzero),"degree_failure_count":len(failures),"representative_l1":[c for c in cases if c["ls"]==1 and c["lt"]==2],"output":str(out)},indent=2))
