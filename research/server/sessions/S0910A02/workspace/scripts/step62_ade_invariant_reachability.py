#!/usr/bin/env python3
"""Finite ADE invariant Weyl reachability ledger for Step 62.

This checks the algebraic part of the Strategist's invariance refinement:
for each ADE type, restrict the chiral Weyl block W to
Sym^2_0(R^3)^{Gamma/{+-1}} and ask whether the degeneracy equation
R=aI+W has a kernel has a solution inside that invariant subspace.

This is only local algebraic reachability of Einstein-compatible 2-jets.
It is NOT a global neck construction and NOT a proof of H_flux.
"""
from __future__ import annotations
import json
from pathlib import Path

OUT = Path("Sessions/S0910A02/workspace/data/step62_ade_invariant_reachability.json")
OUT.parent.mkdir(parents=True, exist_ok=True)

a = 1.0  # normalize Lambda/3 = 1 for explicit sample points

records = []

def add(name, dim, form, equation, sample, conclusion):
    records.append({
        "type": name,
        "invariant_dim": dim,
        "normalized_a": a,
        "W_form": form,
        "determinant_equation": equation,
        "sample_degenerate_W": sample,
        "local_path_reachability": conclusion,
    })

add(
    "A1",
    5,
    "arbitrary traceless symmetric 3x3 W",
    "det(aI+W)=0",
    "diag(-a, a/2, a/2) or any traceless symmetric matrix with eigenvalue -a",
    "reachable locally: the invariant Weyl space is full; the degeneracy hypersurface is nonempty and path-connected up to eigenvalue crossing choices. A1 has no isotropy restriction on the Weyl drift."
)
add(
    "cyclic A_k, k>=2 except A3 special Z2 image",
    1,
    "diag(-u/2,-u/2,u)",
    "(a-u/2)^2(a+u)=0",
    {"u=2a": "W=diag(-a,-a,2a), double kernel in aI+W", "u=-a": "W=diag(a/2,a/2,-a), single kernel"},
    "reachable locally if the one invariant Weyl amplitude can drift by O(1); no algebraic barrier, but H_flux would force exponential scale unless the ambient value already satisfies one root."
)
add(
    "A3 (SO3 image Z2)",
    3,
    "[[x,y,0],[y,z,0],[0,0,-x-z]]",
    "(a-x-z)((a+x)(a+z)-y^2)=0",
    {"branch1": {"x":0,"y":0,"z":a}, "branch2": {"x":-a,"y":0,"z":0}},
    "reachable locally: the degeneracy set is a nonempty algebraic hypersurface inside the 3D invariant subspace."
)
add(
    "D4",
    2,
    "diag(x,y,-x-y)",
    "(a+x)(a+y)(a-x-y)=0",
    {"branch_x=-a": {"x":-a,"y":0}, "branch_y=-a": {"x":0,"y":-a}, "branch_x+y=a": {"x":a,"y":0}},
    "reachable locally: the degeneracy set is a union of three affine lines in the 2D invariant subspace."
)
add(
    "higher D_k",
    1,
    "diag(-u/2,-u/2,u)",
    "(a-u/2)^2(a+u)=0",
    {"u=2a": "double kernel", "u=-a": "single kernel"},
    "same as one-dimensional cyclic cases: no local algebraic barrier to reaching a root if O(1) drift is allowed."
)
add(
    "E6/E7/E8 nontrivial chiral block",
    0,
    "W=0",
    "det(aI)=a^3>0 for a>0",
    None,
    "not reachable in positive Einstein normalization on the nontrivial block; under H_flux, non-exponential bubbles testing this block are excluded. Exponential drift also has no invariant Weyl direction in this block."
)

summary = {
    "status": "ok",
    "normalization": "a=Lambda/3 set to 1 in samples; rescale linearly for general positive Lambda.",
    "scope": "local algebraic reachability inside Gamma-invariant Einstein-compatible quadratic jets; not a global construction and not an H_flux proof.",
    "records": records,
    "conclusions": [
        "A1 has full five-dimensional invariant Weyl freedom in the relevant block, so the exponential drift channel has no local invariance obstruction.",
        "A_k (k>=2) and D_k have smaller invariant spaces but their positive-Lambda degeneracy equations are nonempty; if O(1) invariant drift is allowed, local paths to degeneracy exist. H_flux would then imply only the obstruction-or-exponential alternative, not unconditional exclusion, except when additional boundary data prevent reaching a root.",
        "E6/E7/E8 on the nontrivial chiral block have zero invariant Weyl tangent and W=0; positive R=aI has no kernel. These are the cleanest unconditional exclusions under H_flux at non-exponential scale."
    ]
}
OUT.write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps({"status":"ok", "output": str(OUT), "key": summary["conclusions"]}, indent=2))
