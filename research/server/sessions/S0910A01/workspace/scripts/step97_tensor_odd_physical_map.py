#!/usr/bin/env python3
"""
Step 97: source-compatible K-odd AA/BB tensor-sector maps on the kernel plane.

This computes the part that is presently justified without reconstructing the full
even source: the chirality-odd receiver paired with the chirality-odd H^4 source.
By the Step 96/97 physical Sym^2(K) identity, S_odd=(1/2)R_odd on all kernel-plane
entries, so the sparse receiver data determine this K-odd source-compatible sector.

The output is a map Sym^2(K_source)->Sym^2(K_receiver) for AA (tensor on A,
scalar on B) and BB (tensor on B, scalar on A), and then its action on physical
rank-one sources M=t^2 u u^T is interpreted through radial/angular receiver
components.
"""
from __future__ import annotations

import importlib.util
import json
import math
import pathlib
import random
import sys
from dataclasses import dataclass
from typing import Literal

import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Import the corrected Step 96 algebra conventions: receiver and H4 source tensors.
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
    value: np.ndarray  # 2x2 trace-free tensor value at the pole
    norm: float


@dataclass(frozen=True)
class ScalarMode:
    ell: int
    mode: str
    node: Node
    hess: np.ndarray  # 2x2 scalar Hessian at the pole
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
    # Full Lie magnetic tensor M=L_{(*df)^#}g = 2[[-c,a],[a,c]] when E=[[a,c],[c,-a]].
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
                for mu_i in range(2):
                    for nu_i in range(2):
                        H[a, b, 2+mu_i, 2+nu_i] += T[a, b] * Hs[mu_i, nu_i]
        return H
    if sector == "BB":
        for mu_i in range(2):
            for nu_i in range(2):
                for a in range(2):
                    for b in range(2):
                        H[2+mu_i, 2+nu_i, a, b] += T[mu_i, nu_i] * Hs[a, b]
        return H
    raise ValueError(sector)


def parse_pair(pair: str) -> tuple[Node, Node]:
    if pair not in ["NN", "NS", "SN", "SS"]:
        raise ValueError(pair)
    return pair[0], pair[1]


def compact(T: np.ndarray) -> np.ndarray:
    return np.array([
        [T[0, 0, 0, 0], T[0, 0, 1, 1], T[0, 0, 0, 1]],
        [T[1, 1, 0, 0], T[1, 1, 1, 1], T[1, 1, 0, 1]],
        [T[0, 1, 0, 0], T[0, 1, 1, 1], T[0, 1, 0, 1]],
    ])


def trace_double_angle_matrix(K: np.ndarray) -> np.ndarray:
    # Compact maps use columns [M22, M33, 2*M23] effectively when evaluated
    # on symmetric sources, because the stored coefficient is T[...,0,1]=T[...,1,0].
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


def compute_sector_pair(sector: Sector, Lmax: int, tau: float, pair: str) -> dict:
    recA, recB = "N", "N"
    srcA, srcB = parse_pair(pair)
    response = np.zeros((2, 2, 2, 2), dtype=float)  # receiver ab, source cd, odd/odd only
    shell_abs = []
    for lt in range(2, Lmax + 1):
        shell = 0.0
        for ls in range(1, Lmax + 1):
            P = 0.5 * (mu(lt) + mu(ls)) - 1.0
            if P <= 0:
                continue
            heat = math.exp(-tau * P)
            if sector == "AA":
                T_rec_node, S_rec_node = recA, recB
                T_src_node, S_src_node = srcA, srcB
            else:
                T_rec_node, S_rec_node = recB, recA
                T_src_node, S_src_node = srcB, srcA
            for tm_r in tensor_value_modes(lt, T_rec_node):
                for sm_r in scalar_hessian_modes(ls, S_rec_node):
                    Hrec = tensor_scalar_hessian(tm_r.value, sm_r.hess, sector)
                    Rodd = 0.5 * (step96.receiver_matrix(Hrec, "plus") - step96.receiver_matrix(Hrec, "minus"))
                    if np.max(np.abs(Rodd)) < 1e-15:
                        continue
                    for tm_s in tensor_value_modes(lt, T_src_node):
                        if tm_s.kind != tm_r.kind or tm_s.seed != tm_r.seed:
                            continue
                        for sm_s in scalar_hessian_modes(ls, S_src_node):
                            if sm_s.mode != sm_r.mode:
                                continue
                            Hsrc = tensor_scalar_hessian(tm_s.value, sm_s.hess, sector)
                            Sodd = 0.5 * (step96.source_matrix_over_pi2(Hsrc, "plus") - step96.source_matrix_over_pi2(Hsrc, "minus"))
                            if np.max(np.abs(Sodd)) < 1e-15:
                                continue
                            norm_quot = tm_r.norm / 2.0  # scalar modes L2-normalized; quotient halves cover norm
                            term = (math.pi ** 2) * heat * np.einsum("ab,cd->abcd", Rodd, Sodd) / (P * norm_quot)
                            response += term
                            shell += float(np.sum(np.abs(term)))
        shell_abs.append(shell)
    K = compact(response)
    Kxyz = trace_double_angle_matrix(K)
    return {
        "sector": sector,
        "receiver": "NN",
        "source": pair,
        "Lmax": Lmax,
        "tau": tau,
        "compact_odd_odd_rows_R22_R33_R23_cols_M22_M33_M23": K.round(12).tolist(),
        "trace_double_angle_[X,Y,Z]_<-[x,y,z]": Kxyz.round(12).tolist(),
        "selected_entries": {
            "R22_from_M22": float(response[0,0,0,0]),
            "R33_from_M33": float(response[1,1,1,1]),
            "R23_from_M23": float(response[0,1,0,1]),
            "R22_from_M33": float(response[0,0,1,1]),
            "R33_from_M22": float(response[1,1,0,0]),
        },
        "tail_indicator_last_10_lt_abs_sum": float(sum(shell_abs[-10:])) if len(shell_abs) >= 10 else None,
    }


def compact_source_entries(t: float, theta: float) -> np.ndarray:
    c, s = math.cos(theta), math.sin(theta)
    return t*t*np.array([c*c, s*s, 2*c*s])


def block_from_entries(v: np.ndarray) -> np.ndarray:
    return np.array([[v[0], v[2]], [v[2], v[1]]], dtype=float)


def radial_angular(A: np.ndarray, theta: float) -> tuple[float, float]:
    u = np.array([math.cos(theta), math.sin(theta)])
    up = np.array([-math.sin(theta), math.cos(theta)])
    return float(u @ A @ u), float(up @ A @ u)


def sample_physical(Kcompact: np.ndarray) -> list[dict]:
    rng = random.Random(9702)
    rows = []
    for _ in range(8):
        t = 0.3 + 1.4*rng.random()
        ths = 2*math.pi*rng.random()
        thr = 2*math.pi*rng.random()
        out_entries = Kcompact @ compact_source_entries(t, ths)
        A = block_from_entries(out_entries)
        rad, ang = radial_angular(A, thr)
        rows.append({
            "t_source": t,
            "theta_source": ths,
            "theta_receiver": thr,
            "output_block": A.tolist(),
            "radial": rad,
            "angular": ang,
        })
    return rows


def main() -> None:
    ladders = []
    for tau, L in [(0.08, 80), (0.04, 120), (0.02, 180), (0.01, 260)]:
        row = {"tau": tau, "Lmax": L, "pairs": {}}
        for pair in ["NS", "SN", "SS"]:
            row["pairs"][pair] = {
                "AA": compute_sector_pair("AA", L, tau, pair),
                "BB": compute_sector_pair("BB", L, tau, pair),
            }
        ladders.append(row)

    final = ladders[-1]["pairs"]
    combined_adjacent_NS = np.array(final["NS"]["AA"]["compact_odd_odd_rows_R22_R33_R23_cols_M22_M33_M23"]) + np.array(final["NS"]["BB"]["compact_odd_odd_rows_R22_R33_R23_cols_M22_M33_M23"])
    combined_adjacent_SN = np.array(final["SN"]["AA"]["compact_odd_odd_rows_R22_R33_R23_cols_M22_M33_M23"]) + np.array(final["SN"]["BB"]["compact_odd_odd_rows_R22_R33_R23_cols_M22_M33_M23"])

    results = {
        "step": 97,
        "scope": "K-odd AA/BB tensor-sector source-compatible map using the physical odd H4 adjoint identity",
        "method": "sum tensor-on-one-factor times scalar-on-other-factor modes; source uses S_odd=(B_+-B_-)/(2*pi^2) from the H4 formula, receiver uses R_odd=(R^+-R^-)/2",
        "normalization": "product quotient norm is ||TF tensor||^2/2 for scalar L2 norm 1; magnetic full-Lie norm is four times electric norm as in Step94; compact map columns are evaluated as [M22,M33,2M23] on symmetric physical sources",
        "ladders": ladders,
        "final_tau_0p01_L260_summary": {
            "NS_AA_plus_BB_compact": combined_adjacent_NS.round(12).tolist(),
            "NS_AA_plus_BB_trace_double_angle": trace_double_angle_matrix(combined_adjacent_NS).round(12).tolist(),
            "SN_AA_plus_BB_compact": combined_adjacent_SN.round(12).tolist(),
            "SN_AA_plus_BB_trace_double_angle": trace_double_angle_matrix(combined_adjacent_SN).round(12).tolist(),
            "NS_physical_samples": sample_physical(combined_adjacent_NS),
            "SN_physical_samples": sample_physical(combined_adjacent_SN),
        },
        "interpretation_warnings": [
            "This is only the chirality-odd/odd tensor sector, justified by the corrected physical Sym^2(K) odd source identity; it does not include even sources or individual plus/minus residual components.",
            "Only value-of-T times Hessian-of-scalar pieces are needed for the odd receiver/source identity. The full even source would require the complete second jet of tensor harmonics and is not computed here.",
            "The output should be interpreted on physical sources M=t^2uu^T and receiver components u^T A u, u_perp^T A u; a kernel in unconstrained Sym^2(K) need not represent a physical insertion.",
        ],
    }
    out = DATA_DIR / "step97_tensor_odd_physical_map.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
