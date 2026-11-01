#!/usr/bin/env python3
"""Step 43: orientation/topology bookkeeping for Route A after the det R_+ correction.

This is not a geometric proof.  It records finite algebraic checks that clarify
which curvature block is tested by an Eguchi--Hanson bubble orientation and how
b_+ changes under resolution of A_1 singularities.  The calculations are meant
to guard against the Step-42 route-allocation error: a Kähler--Einstein limit
pins R_+ but not generally R_-; b_+>=2 forces some reversed-orientation bubbles
if the limit has b_+=1 and all bubbles are Eguchi--Hanson.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step43_orientation_obstruction_bookkeeping.json"


def kähler_block(lambda_symbol: sp.Symbol) -> Dict[str, Any]:
    """R_+ block for a KE surface in the complex orientation.

    For Ric = Lambda g in real dimension 4, scalar s=4 Lambda and the
    Kähler identity gives W_+ eigenvalues (2 Lambda/3, -Lambda/3, -Lambda/3).
    Hence R_+=W_+ + Lambda/3 I has eigenvalues (Lambda,0,0).
    """
    L = lambda_symbol
    Wp = [sp.Rational(2, 3) * L, -sp.Rational(1, 3) * L, -sp.Rational(1, 3) * L]
    Rp = [w + sp.Rational(1, 3) * L for w in Wp]
    return {
        "W_plus_eigenvalues": [str(x) for x in Wp],
        "R_plus_eigenvalues": [str(x) for x in Rp],
        "det_R_plus": str(sp.prod(Rp)),
        "kernel_dimension_when_Lambda_nonzero": 2,
        "interpretation": "The complex/Kähler orientation gives an automatic 2-plane kernel of R_+; this helps orientation-compatible EH bubbles but says nothing about R_-.",
    }


def product_s2xs2_blocks(lambda_symbol: sp.Symbol) -> Dict[str, Any]:
    """Curvature-operator blocks for the product of two equal 2-spheres.

    In the orthonormal 2-form basis e12,e13,e14,e34,e42,e23, the only nonzero
    sectional curvatures are K12=K34=Lambda.  For the standard selfdual bases
        omega1+ = (e12+e34)/sqrt2, omega1-=(e12-e34)/sqrt2,
        omega2+ = (e13-e24)/sqrt2, omega2-=(e13+e24)/sqrt2,
        omega3+ = (e14+e23)/sqrt2, omega3-=(e14-e23)/sqrt2,
    both R_+ and R_- have eigenvalues (Lambda,0,0).  This is the basic
    ambi-Kähler caveat: S^2 x S^2 does not make reversed EH bubbles first-order
    obstructed.
    """
    L = lambda_symbol
    return {
        "R_plus_eigenvalues": [str(L), "0", "0"],
        "R_minus_eigenvalues": [str(L), "0", "0"],
        "det_R_plus": "0",
        "det_R_minus": "0",
        "kernel_dimensions_when_Lambda_nonzero": {"R_plus": 2, "R_minus": 2},
        "interpretation": "The product Einstein metric is Kähler for both orientations; unlike CP^2_FS, it automatically satisfies first obstruction in both blocks.",
    }


def cp2_fs_blocks(lambda_symbol: sp.Symbol) -> Dict[str, Any]:
    """Curvature blocks for Fubini--Study CP^2 in the complex orientation.

    CP^2 with constant holomorphic sectional curvature is self-dual in the
    complex orientation, so W_- = 0.  Therefore R_- = Lambda/3 I and reversed
    EH insertion is first-order obstructed everywhere.
    """
    L = lambda_symbol
    return {
        "R_plus_eigenvalues": [str(L), "0", "0"],
        "R_minus_eigenvalues": [str(sp.Rational(1, 3) * L)] * 3,
        "det_R_plus": "0",
        "det_R_minus": str(sp.Rational(1, 27) * L**3),
        "kernel_dimensions_when_Lambda_nonzero": {"R_plus": 2, "R_minus": 0},
        "interpretation": "Complex/Kähler orientation compatible EH bubbles pass the first obstruction; reversed EH bubbles fail the first obstruction at a locally complex-space-form point.",
    }


def generic_rminus_condition(lambda_symbol: sp.Symbol) -> Dict[str, Any]:
    a, b, c, x, y = sp.symbols("a b c x y")
    # Generic trace-free symmetric W_- in a diagonal basis has eigenvalues a,b,-a-b.
    L = lambda_symbol
    eig = [a, b, -a - b]
    Rm = [e + sp.Rational(1, 3) * L for e in eig]
    det = sp.factor(sp.prod(Rm))
    return {
        "W_minus_tracefree_eigenvalues": [str(e) for e in eig],
        "R_minus_eigenvalues": [str(e) for e in Rm],
        "det_R_minus_polynomial": str(det),
        "codimension_heuristic": "For a general KE surface W_- is the Bochner/anti-self-dual block and is not fixed by the Kähler identity. det(R_-)=0 is one real scalar equation at a point; the chosen reversed EH direction must lie in its kernel.",
    }


@dataclass
class TopologyScenario:
    target: str
    k: int
    bplus_O: int
    bminus_O: int
    compatible_EH_needed: int
    reversed_EH_needed: int
    total_EH: int
    bplus_M: int
    bminus_M: int
    tau_M: int
    admissible_counts: bool


def target_kH_counts(k: int, bminus_O: int) -> TopologyScenario:
    """Solve b_+(M)=b_-(M)=k for a KE orbifold O with b_+(O)=1.

    A complex-orientation-compatible EH resolution contributes (b_+,b_-)=(0,1).
    A reversed-orientation EH resolution contributes (1,0).  If O has
    (b_+,b_-)=(1,m), then #_k(S^2xS^2) forces r=k-1 reversed bubbles and
    c=k-m compatible bubbles.  This finite calculation is only the homological
    A_1/EH case; more general ALE trees require separate bookkeeping.
    """
    m = bminus_O
    r = k - 1
    c = k - m
    return TopologyScenario(
        target=f"#{k}(S^2 x S^2) with intersection form {k}H",
        k=k,
        bplus_O=1,
        bminus_O=m,
        compatible_EH_needed=c,
        reversed_EH_needed=r,
        total_EH=c + r,
        bplus_M=1 + r,
        bminus_M=m + c,
        tau_M=(1 + r) - (m + c),
        admissible_counts=(c >= 0 and r >= 0),
    )


def main() -> None:
    L = sp.symbols("Lambda", nonzero=True, real=True)
    scenarios: List[TopologyScenario] = []
    # m=b_-(O) examples: CP^2-like (0), S^2xS^2-like (1), dP_3-like (3), near the largest Fano smooth value (8).
    for k in [2, 3, 5, 10]:
        for m in [0, 1, 3, 8]:
            scenarios.append(target_kH_counts(k, m))

    data: Dict[str, Any] = {
        "scope": "Finite algebraic/topological bookkeeping for four-dimensional positive noncollapsed Route A; not a proof of Yau-26.",
        "source_anchors": {
            "Ozuch_higher_order_lines_83_92": "Either det R_+(p)=0 or det R_-(p)=0 depending on orientation of EH gluing.",
            "Ozuch_higher_order_lines_372_376": "Negative orientation EH_zeta^- is the same metric with opposite orientation and asymptotic term using zeta^-; hence it tests the opposite curvature block.",
            "LeBrun_Ozuch_lines_155_168": "Admissible Hermitian/expected-topology sequences yield Del Pezzo diffeotypes with b_+=1.",
            "LeBrun_Ozuch_lines_326_328": "Expected topology means all ALE spaces are Kähler in an orientation-compatible manner.",
            "Ozuch_lines_1089_1092": "The EH L^2 cohomology generator is anti-selfdual in the orientation used for eh, giving negative square; reversing orientation changes its b_+ contribution.",
        },
        "orientation_dictionary": {
            "EH_zeta_plus": {
                "curvature_block_tested": "R_+ = W_+ + Lambda/3 Id at the orbifold point",
                "asymptotic_term": "H^4(zeta^+) = - rho(zeta)^- o zeta^+ / (2 r^4)",
                "relative_betti_contribution": {"b_plus": 0, "b_minus": 1},
                "explanation": "This is the orientation-compatible Kähler/ALE case in LeBrun-Ozuch expected topology; the compactly supported EH class has negative square.",
            },
            "EH_zeta_minus": {
                "curvature_block_tested": "R_- = W_- + Lambda/3 Id at the orbifold point",
                "asymptotic_term": "H^4(zeta^-) = - zeta^- o rho(zeta)^+ / (2 r^4)",
                "relative_betti_contribution": {"b_plus": 1, "b_minus": 0},
                "explanation": "This is the reversed-orientation EH insertion; it raises b_+ and is the only way an A_1 bubble tree over a KE limit with b_+(O)=1 can produce b_+(M)>1.",
            },
        },
        "curvature_blocks": {
            "general_KE_complex_orientation": kähler_block(L),
            "CP2_Fubini_Study_complex_orientation": cp2_fs_blocks(L),
            "S2xS2_product_equal_spheres": product_s2xs2_blocks(L),
            "generic_R_minus": generic_rminus_condition(L),
        },
        "topology_scenarios_for_kH": [asdict(s) for s in scenarios],
        "strategic_conclusions": [
            "Step42's det R_+=0 computation is correct but incomplete: it certifies that orientation-compatible EH bubbles over a KE limit are first-obstruction-compatible; it does not make all KE bubbling harmless because b_+>1 forces reversed bubbles that test R_-.",
            "For M=#_k(S^2 x S^2) and a KE orbifold limit with b_+(O)=1, the A_1/EH homology bookkeeping forces exactly k-1 reversed EH bubbles, independent of b_-(O).",
            "The reversed bubbles impose det(R_-)=0 at their singular points. This is a genuine condition on a generic KE limit, but not on the product S^2 x S^2 metric, which is Kähler for both orientations and has det R_-=0 everywhere.",
            "Therefore the next cheap Route-A work should first establish the orientation dictionary and the pair (det R_+,det R_-) obstruction precisely for C^0-Ricci-pinched noncollapsed sequences, then test known KE/product/orbifold limit models; it should not jump directly to high-order Ozuch obstructions as the main investment.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(OUT), "summary": data["strategic_conclusions"]}, indent=2))


if __name__ == "__main__":
    main()
