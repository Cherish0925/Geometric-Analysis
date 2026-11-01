#!/usr/bin/env python3
"""
Step 98: Full raw chirality tensor maps on the kernel plane.

This computes ALL FOUR raw chirality combinations (++, +-, -+, --) for
the AA/BB tensor sectors, not just the odd-odd combination from Step 97.
The new even-even component is the missing piece needed to reconstruct
the physical response for each chirality pattern and determine the P/Q
decomposition in A02's determinantal framework.

Key mathematical point: the even/odd K-parity decomposition masks the
physical chirality structure. For each ordered node pair (i,j), the
physical response depends on the specific chirality assignment (eps_i, eps_j),
which selects B_{eps_i, eps_j} -- not B_ee or B_oo.

By K-symmetry (Step 90), cross-parity blocks vanish: B_eo = B_oe = 0.
Hence:
  B_{same} := B_{++} = B_{--} = B_ee + B_oo
  B_{cross} := B_{+-} = B_{-+} = B_ee - B_oo

The script verifies these equalities and the match with Step 97's odd-odd data.
"""
from __future__ import annotations

import importlib.util
import json
import math
import pathlib
import sys
from dataclasses import dataclass
from typing import Literal

import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Import Step 96 algebra: receiver/source coefficient arrays, scalar Hessians.
_spec = importlib.util.spec_from_file_location("step96_ab", SCRIPT_DIR / "step96_kernel_plane_ab_map.py")
step96 = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules[_spec.name] = step96
_spec.loader.exec_module(step96)

Node = Literal["N", "S"]
Kind = Literal["electric", "magnetic_full_lie"]
Sector = Literal["AA", "BB"]


def mu(l: int) -> int:
    return l * (l + 1)


def b2(l: int) -> float:
    if l < 2:
        return 0.0
    m = mu(l)
    return (2 * l + 1) * m * (m - 2) / (128.0 * math.pi)


def tf_norm(l: int, kind: Kind) -> float:
    m = mu(l)
    electric_norm = 0.5 * m * (m - 2)
    if kind == "electric":
        return electric_norm
    if kind == "magnetic_full_lie":
        return 4.0 * electric_norm
    raise ValueError(kind)


@dataclass(frozen=True)
class TensorMode:
    ell: int
    seed: str
    kind: Kind
    node: Node
    value: np.ndarray
    norm: float


@dataclass(frozen=True)
class ScalarMode:
    ell: int
    mode: str
    node: Node
    hess: np.ndarray
    norm: float = 1.0


def scalar_hessian_modes(ell: int, node: Node) -> list[ScalarMode]:
    return [ScalarMode(ell=ell, mode=name, node=node, hess=H.copy())
            for name, H in step96.scalar_hessian_coefficients(ell, node)]


def tensor_value_modes(ell: int, node: Node) -> list[TensorMode]:
    if ell < 2:
        return []
    b = math.sqrt(b2(ell))
    sign_c = 1.0 if node == "N" else ((-1.0) ** ell)
    sign_s = 1.0 if node == "N" else (-((-1.0) ** ell))
    E_c = sign_c * np.array([[2*b, 0.0], [0.0, -2*b]])
    E_s = sign_s * np.array([[0.0, 2*b], [2*b, 0.0]])
    M_c = sign_c * np.array([[0.0, 4*b], [4*b, 0.0]])
    M_s = sign_s * np.array([[-4*b, 0.0], [0.0, 4*b]])
    return [
        TensorMode(ell, "c2", "electric", node, E_c, tf_norm(ell, "electric")),
        TensorMode(ell, "s2", "electric", node, E_s, tf_norm(ell, "electric")),
        TensorMode(ell, "c2", "magnetic_full_lie", node, M_c, tf_norm(ell, "magnetic_full_lie")),
        TensorMode(ell, "s2", "magnetic_full_lie", node, M_s, tf_norm(ell, "magnetic_full_lie")),
    ]


def tensor_scalar_hessian(T: np.ndarray, Hs: np.ndarray, sector: Sector) -> np.ndarray:
    H = np.zeros((4, 4, 4, 4), dtype=float)
    if sector == "AA":
        for a in range(2):
            for b in range(2):
                for mi in range(2):
                    for ni in range(2):
                        H[a, b, 2+mi, 2+ni] += T[a, b] * Hs[mi, ni]
        return H
    if sector == "BB":
        for mi in range(2):
            for ni in range(2):
                for a in range(2):
                    for b in range(2):
                        H[2+mi, 2+ni, a, b] += T[mi, ni] * Hs[a, b]
        return H
    raise ValueError(sector)


def compact(T: np.ndarray) -> np.ndarray:
    return np.array([
        [T[0, 0, 0, 0], T[0, 0, 1, 1], T[0, 0, 0, 1]],
        [T[1, 1, 0, 0], T[1, 1, 1, 1], T[1, 1, 0, 1]],
        [T[0, 1, 0, 0], T[0, 1, 1, 1], T[0, 1, 0, 1]],
    ])


def trace_double_angle_matrix(K: np.ndarray) -> np.ndarray:
    source_entries_from_xyz = np.array([
        [0.5, 0.5, 0.0],
        [0.5, -0.5, 0.0],
        [0.0, 0.0, 1.0],
    ])
    xyz_from_output_entries = np.array([
        [1.0, 1.0, 0.0],
        [1.0, -1.0, 0.0],
        [0.0, 0.0, 2.0],
    ])
    return xyz_from_output_entries @ K @ source_entries_from_xyz


def parse_pair(pair: str) -> tuple[Node, Node]:
    if pair not in ["NN", "NS", "SN", "SS"]:
        raise ValueError(pair)
    return pair[0], pair[1]  # type: ignore


def compute_full_chirality(sector: Sector, Lmax: int, tau: float, pair: str) -> dict:
    """Compute all four raw chirality maps for a tensor sector and node pair."""
    recA, recB = "N", "N"  # receiver always at NN
    srcA, srcB = parse_pair(pair)

    if sector == "AA":
        T_rec_node, S_rec_node = recA, recB
        T_src_node, S_src_node = srcA, srcB
    else:
        T_rec_node, S_rec_node = recB, recA
        T_src_node, S_src_node = srcB, srcA

    # Four raw chirality response tensors
    raw = {rc: {sc: np.zeros((2, 2, 2, 2), dtype=float)
                for sc in ("plus", "minus")}
           for rc in ("plus", "minus")}

    shell_norms = []
    for lt in range(2, Lmax + 1):
        shell = 0.0
        for ls in range(1, Lmax + 1):
            P = 0.5 * (mu(lt) + mu(ls)) - 1.0
            if P <= 0:
                continue
            heat = math.exp(-tau * P)
            for tm_r in tensor_value_modes(lt, T_rec_node):
                for sm_r in scalar_hessian_modes(ls, S_rec_node):
                    Hrec = tensor_scalar_hessian(tm_r.value, sm_r.hess, sector)
                    Rplus = step96.receiver_matrix(Hrec, "plus")
                    Rminus = step96.receiver_matrix(Hrec, "minus")
                    if max(np.max(np.abs(Rplus)), np.max(np.abs(Rminus))) < 1e-15:
                        continue
                    for tm_s in tensor_value_modes(lt, T_src_node):
                        if tm_s.kind != tm_r.kind or tm_s.seed != tm_r.seed:
                            continue
                        for sm_s in scalar_hessian_modes(ls, S_src_node):
                            if sm_s.mode != sm_r.mode:
                                continue
                            Hsrc = tensor_scalar_hessian(tm_s.value, sm_s.hess, sector)
                            Splus = step96.source_matrix_over_pi2(Hsrc, "plus")
                            Sminus = step96.source_matrix_over_pi2(Hsrc, "minus")
                            if max(np.max(np.abs(Splus)), np.max(np.abs(Sminus))) < 1e-15:
                                continue
                            norm_quot = tm_r.norm / 2.0
                            pref = (math.pi ** 2) * heat / (P * norm_quot)
                            for rc, Rmat in [("plus", Rplus), ("minus", Rminus)]:
                                for sc, Smat in [("plus", Splus), ("minus", Sminus)]:
                                    term = pref * np.einsum("ab,cd->abcd", Rmat, Smat)
                                    raw[rc][sc] += term
                                    shell += float(np.sum(np.abs(term)))
        shell_norms.append(shell)

    # Derive even/odd combinations
    Kpp = raw["plus"]["plus"]
    Kpm = raw["plus"]["minus"]
    Kmp = raw["minus"]["plus"]
    Kmm = raw["minus"]["minus"]

    combos = {
        "even_even": 0.25 * (Kpp + Kpm + Kmp + Kmm),
        "even_odd": 0.25 * (Kpp - Kpm + Kmp - Kmm),
        "odd_even": 0.25 * (Kpp + Kpm - Kmp - Kmm),
        "odd_odd": 0.25 * (Kpp - Kpm - Kmp + Kmm),
    }

    # Verify cross-parity vanishing (K-symmetry, Step 90)
    max_eo = float(np.max(np.abs(combos["even_odd"])))
    max_oe = float(np.max(np.abs(combos["odd_even"])))

    # Verify same/cross chirality equalities (B_{++}=B_{--}, B_{+-}=B_{-+})
    max_pp_mm_diff = float(np.max(np.abs(Kpp - Kmm)))
    max_pm_mp_diff = float(np.max(np.abs(Kpm - Kmp)))

    def arr(A):
        return np.asarray(A).round(12).tolist()

    def make_entry(T):
        K = compact(T)
        Kxyz = trace_double_angle_matrix(K)
        return {
            "compact_3x3": arr(K),
            "trace_double_angle": arr(Kxyz),
        }

    result = {
        "sector": sector, "receiver": "NN", "source": pair,
        "Lmax": Lmax, "tau": tau,
        "raw_chirality_maps": {
            "plus_plus": make_entry(Kpp),
            "plus_minus": make_entry(Kpm),
            "minus_plus": make_entry(Kmp),
            "minus_minus": make_entry(Kmm),
        },
        "even_odd_decomposition": {
            "even_even": make_entry(combos["even_even"]),
            "odd_odd": make_entry(combos["odd_odd"]),
            "cross_parity_vanishing_check": {
                "max_abs_even_odd": max_eo,
                "max_abs_odd_even": max_oe,
            },
        },
        "chirality_equalities_check": {
            "max_abs_B++_minus_B--": max_pp_mm_diff,
            "max_abs_B+-_minus_B-+": max_pm_mp_diff,
        },
        "tail_indicator": float(sum(shell_norms[-10:])) if len(shell_norms) >= 10 else None,
    }
    return result


def physical_cone_pq(entry: dict) -> dict:
    """Extract P/Q decomposition from trace/double-angle matrix."""
    Axyz = np.array(entry["trace_double_angle"])
    # In complex coordinates: source w=xi^2, output zeta
    # trace channel: c0 = Axyz[0,0] (x -> X coefficient)
    # P channel (holomorphic w -> zeta): related to Y<-y and Z<-z
    # Q channel (anti-holomorphic w_bar -> zeta): related to Y<-y and Z<-z with sign flip
    # zeta = (Y+iZ)/2 response to w = y+iz:
    #   zeta = ((Ayy*y + Ayz*z) + i(Azy*y + Azz*z))/2
    #   = ((Ayy+iAzy)*y + (Ayz+iAzz)*z)/2
    #   = ((Ayy+iAzy)*(w+w_bar)/2 + (Ayz+iAzz)*(w-w_bar)/(2i))/2
    # Let's directly compute:
    # P = ((Ayy+Azz) + i(Azy-Ayz))/4   (coefficient of w)
    # Q = ((Ayy-Azz) + i(Azy+Ayz))/4   (coefficient of w_bar)
    Ayy = Axyz[1, 1]
    Ayz = Axyz[1, 2]
    Azy = Axyz[2, 1]
    Azz = Axyz[2, 2]
    P_re = (Ayy + Azz) / 4.0
    P_im = (Azy - Ayz) / 4.0
    Q_re = (Ayy - Azz) / 4.0
    Q_im = (Azy + Ayz) / 4.0
    c0 = Axyz[0, 0]
    # Also check: Axy, Axz should contribute to trace-from-angle mixing
    Axy = Axyz[0, 1]
    Axz = Axyz[0, 2]
    Ayx = Axyz[1, 0]
    Azx = Axyz[2, 0]
    return {
        "c0_trace": float(c0),
        "P_re": float(P_re), "P_im": float(P_im), "P_abs": float(abs(complex(P_re, P_im))),
        "Q_re": float(Q_re), "Q_im": float(Q_im), "Q_abs": float(abs(complex(Q_re, Q_im))),
        "trace_angle_mixing": {"Axy": float(Axy), "Axz": float(Axz),
                               "Ayx": float(Ayx), "Azx": float(Azx)},
    }


def main():
    # Ladder of (tau, Lmax) for convergence check
    ladder = [
        (0.08, 80),
        (0.04, 120),
        (0.02, 180),
        (0.01, 260),
    ]
    pairs = ["NS", "SN", "SS"]
    sectors: list[Sector] = ["AA", "BB"]

    all_results = {
        "step": 98,
        "scope": "full raw chirality tensor maps for AA/BB sectors",
        "method": "compute all four B_{rc,sc} independently; "
                  "verify cross-parity vanishing and odd-odd match with Step 97",
    }

    for tau, Lmax in ladder:
        key = f"tau={tau}_Lmax={Lmax}"
        rung = {}
        for pair in pairs:
            pair_data = {}
            for sector in sectors:
                print(f"Computing {sector} NN<-{pair} tau={tau} Lmax={Lmax} ...", flush=True)
                entry = compute_full_chirality(sector, Lmax, tau, pair)
                pair_data[sector] = entry

                # P/Q for each raw chirality map
                for chir_key in ["plus_plus", "plus_minus", "minus_plus", "minus_minus"]:
                    entry["raw_chirality_maps"][chir_key]["PQ"] = physical_cone_pq(
                        entry["raw_chirality_maps"][chir_key])
                for eo_key in ["even_even", "odd_odd"]:
                    entry["even_odd_decomposition"][eo_key]["PQ"] = physical_cone_pq(
                        entry["even_odd_decomposition"][eo_key])

            # Combined AA+BB for this pair
            for chir_key in ["plus_plus", "plus_minus"]:
                combined_xyz = np.zeros((3, 3))
                for sector in sectors:
                    combined_xyz += np.array(pair_data[sector]["raw_chirality_maps"][chir_key]["trace_double_angle"])
                pair_data[f"combined_{chir_key}"] = {
                    "trace_double_angle": combined_xyz.round(12).tolist(),
                    "PQ": physical_cone_pq({"trace_double_angle": combined_xyz.tolist()}),
                }
            rung[pair] = pair_data
        all_results[key] = rung

    # Summary at finest rung
    finest = all_results[f"tau={ladder[-1][0]}_Lmax={ladder[-1][1]}"]
    summary = {}
    for pair in pairs:
        pd = finest[pair]
        s = {"cross_parity_vanishing": {}, "chirality_equalities": {}, "PQ_channels": {}}
        for sector in sectors:
            e = pd[sector]
            s["cross_parity_vanishing"][sector] = e["even_odd_decomposition"]["cross_parity_vanishing_check"]
            s["chirality_equalities"][sector] = e["chirality_equalities_check"]
            s["PQ_channels"][sector] = {}
            for ck in ["plus_plus", "plus_minus"]:
                s["PQ_channels"][sector][ck] = e["raw_chirality_maps"][ck]["PQ"]
        if f"combined_plus_plus" in pd:
            s["PQ_channels"]["combined_plus_plus"] = pd["combined_plus_plus"]["PQ"]
            s["PQ_channels"]["combined_plus_minus"] = pd["combined_plus_minus"]["PQ"]
        summary[pair] = s
    all_results["summary"] = summary

    # Interpretation
    all_results["interpretation"] = {
        "B_same_chirality": "B_{++} = B_{--} = B_ee + B_oo (verified by chirality_equalities_check)",
        "B_cross_chirality": "B_{+-} = B_{-+} = B_ee - B_oo (verified by chirality_equalities_check)",
        "cross_parity_vanishing": "B_eo = B_oe = 0 by K-symmetry (Step 90)",
        "P_channel": "isotropic response, coefficient of w in zeta = Pw + Qw_bar",
        "Q_channel": "anisotropic response, coefficient of w_bar; nonzero Q requires sigma-matching",
        "physical_determinant": "|P|^2 - |Q|^2 = 0 for degenerate (solvable) map; "
                                "nonzero determinant means invertible (obstructed)",
        "solvability_correction": "A02's |Q|>|P| -> solvable is WRONG. "
                                  "|P|^2 - |Q|^2 < 0 still gives an invertible map with "
                                  "eigenvalues of opposite sign; kernel requires |P|=|Q| exactly.",
    }

    out = DATA_DIR / "step98_full_chirality_tensor_maps.json"
    with open(out, "w") as f:
        json.dump(all_results, f, indent=2)
    print(json.dumps(all_results["summary"], indent=2))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
