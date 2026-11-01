"""Step 98: full-matrix, two-sided charged-Koiso transition experiment.

This replaces the diagonal-field Step-97 trial.  On each half cylinder r in [0,R]
we write the complete positive-definite 3-metric as

    q(r,s) = q0(s)^(1/2) exp(X(r,s)) q0(s)^(1/2).

The center jets are fixed to the exact charged Koiso data.  If
A=q0^(-1/2) K0 q0^(-1/2) and Rhat=q0^(-1/2) Ric(q0) q0^(-1/2), then

    X(0)=0, X_r(0)= +/- 2 A, X_rr(0)=2(Rhat+3I)

reproduce q(0)=q0, q_r(0)=+/-2K0, and the exact Einstein second jet.
At r=R we impose X=2R I, X_r=2I, X_rr=0, so the metric attaches C2 to
the expanding exterior q=e^(2r)q0.  Matrix exponentiation guarantees positive
definiteness throughout.  Adjustable matrix fields vanish to third order at
both endpoints, so they preserve both attachments and all prescribed jets.

All ten components of E=Ric_g+3g are assembled in Gaussian coordinates,
including the normal-tangential/Codazzi block.  Norms are computed after
orthonormal-frame conjugation (equivalently by generalized eigenvalues against
g), never by Euclidean symmetrization of q^{-1}E.

The script computes the finite-dimensional Jacobian, its singular triplets,
residual projections <u_j,F>/s_j, a damped Gauss-Newton correction, and the
actual nonlinear residual along a line search.  This is an exploratory finite-
domain matching calculation, not a proof of existence or nonexistence.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import math
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import numpy as np

SESSION_ROOT = Path(__file__).resolve().parents[2]
EVOL_PATH = Path(__file__).with_name("step96_koiso_einstein_cauchy_evolution.py")
spec = importlib.util.spec_from_file_location("step96_evol", EVOL_PATH)
evol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evol)

PAIR3 = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
PAIR4 = [(i, j) for i in range(4) for j in range(i, 4)]


def chebyshev_lobatto_01(n: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Ascending nodes t in [0,1] and barycentric first/second derivative matrices."""
    j = np.arange(n)
    t = 0.5 * (1.0 - np.cos(np.pi * j / (n - 1)))
    lam = (-1.0) ** j
    lam[[0, -1]] *= 0.5
    D = np.zeros((n, n), dtype=float)
    for i in range(n):
        for k in range(n):
            if i != k:
                D[i, k] = lam[k] / (lam[i] * (t[i] - t[k]))
        D[i, i] = -np.sum(D[i])
    return t, D, D @ D


def sym_sqrt_and_inv(a: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    vals, vecs = np.linalg.eigh(a)
    if np.min(vals) <= 0:
        raise ValueError("matrix is not positive definite")
    sq = (vecs * np.sqrt(vals)[None, :]) @ vecs.T
    isq = (vecs * (1.0 / np.sqrt(vals))[None, :]) @ vecs.T
    return sq, isq


def sym_exp(a: np.ndarray) -> np.ndarray:
    vals, vecs = np.linalg.eigh(0.5 * (a + a.T))
    # Bounds in the optimizer keep this safely below overflow.  Clipping here
    # makes failed trial points finite without changing accepted calculations.
    vals = np.clip(vals, -40.0, 40.0)
    return (vecs * np.exp(vals)[None, :]) @ vecs.T


def quintic_coefficients(
    y0: np.ndarray,
    dy0: np.ndarray,
    ddy0: np.ndarray,
    y1: np.ndarray,
    dy1: np.ndarray,
    ddy1: np.ndarray,
    R: float,
) -> np.ndarray:
    """Coefficients c_k of sum c_k t^k, matching two n-jets at t=0,1."""
    c0 = y0
    c1 = R * dy0
    c2 = 0.5 * R * R * ddy0
    d0 = y1 - c0 - c1 - c2
    d1 = R * dy1 - c1 - 2.0 * c2
    d2 = R * R * ddy1 - 2.0 * c2
    mat = np.array([[1.0, 1.0, 1.0], [3.0, 4.0, 5.0], [6.0, 12.0, 20.0]])
    rhs = np.stack([d0, d1, d2], axis=0)
    tail = np.tensordot(np.linalg.inv(mat), rhs, axes=(1, 0))
    return np.stack([c0, c1, c2, tail[0], tail[1], tail[2]], axis=0)


def eval_poly(coeff: np.ndarray, t: np.ndarray) -> np.ndarray:
    out = np.zeros((len(t),) + coeff.shape[1:], dtype=float)
    for k in range(coeff.shape[0] - 1, -1, -1):
        out = out * t[:, None, None, None] + coeff[k][None, ...]
    return out


def normalized_radial_shapes(t: np.ndarray, count: int) -> List[np.ndarray]:
    base = t**3 * (1.0 - t) ** 3
    shapes = []
    candidates = [base, base * (2.0 * t - 1.0), base * (6.0 * t**2 - 6.0 * t + 1.0)]
    for b in candidates[:count]:
        m = np.max(np.abs(b))
        shapes.append(b / m)
    return shapes


def matrix_basis(s: np.ndarray, wind: int, richer: bool = False) -> Tuple[List[np.ndarray], List[str]]:
    """Symmetric matrix fields in the q0 square-root frame."""
    mats = []
    names = []
    elementary = []
    for i, j in PAIR3:
        e = np.zeros((3, 3))
        if i == j:
            e[i, j] = 1.0
        else:
            e[i, j] = e[j, i] = 1.0 / math.sqrt(2.0)
        elementary.append((e, f"E{i}{j}"))
    modes = [(np.ones_like(s), "1"), (np.cos(wind * s), f"cos{wind}s"), (np.sin(wind * s), f"sin{wind}s")]
    if richer:
        modes += [(np.cos(2 * wind * s), f"cos{2*wind}s"), (np.sin(2 * wind * s), f"sin{2*wind}s")]
    for amp, mname in modes:
        for e, ename in elementary:
            mats.append(amp[:, None, None] * e[None, :, :])
            names.append(f"{mname}*{ename}")
    return mats, names


def center_geometry(ns: int, wind: int, S: float, qmax: float) -> Dict[str, np.ndarray]:
    s, q0, k0, meta = evol.initial_data(ns, wind, S, qmax)
    _, ric0, scalar0 = evol.christoffel_and_ricci(q0)
    sq = np.zeros_like(q0)
    isq = np.zeros_like(q0)
    A = np.zeros_like(q0)
    Rhat = np.zeros_like(q0)
    for k in range(ns):
        sq[k], isq[k] = sym_sqrt_and_inv(q0[k])
        A[k] = isq[k] @ k0[k] @ isq[k]
        Rhat[k] = isq[k] @ ric0[k] @ isq[k]
    B = Rhat + 3.0 * np.eye(3)[None, :, :]
    return dict(s=s, q0=q0, k0=k0, ric0=ric0, scalar0=scalar0, sq=sq, isq=isq, A=A, B=B, meta=meta)


def build_half(
    geom: Dict[str, np.ndarray],
    R: float,
    nr: int,
    sign: int,
    theta: np.ndarray,
    radial_count: int,
    richer: bool,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, List[str]]:
    """Return r, derivative matrices, q(r,s), and parameter names for one half."""
    t, Dt, D2t = chebyshev_lobatto_01(nr)
    r = R * t
    ns = geom["q0"].shape[0]
    z = np.zeros_like(geom["q0"])
    end = 2.0 * R * np.eye(3)[None, :, :] * np.ones((ns, 1, 1))
    dend = 2.0 * np.eye(3)[None, :, :] * np.ones((ns, 1, 1))
    ddend = np.zeros_like(end)
    coeff = quintic_coefficients(z, 2.0 * sign * geom["A"], 2.0 * geom["B"], end, dend, ddend, R)
    X = eval_poly(coeff, t)

    fields, field_names = matrix_basis(geom["s"], int(geom["meta"]["wind"]), richer=richer)
    radial = normalized_radial_shapes(t, radial_count)
    names = []
    expected = len(fields) * radial_count
    if len(theta) != expected:
        raise ValueError(f"theta length {len(theta)} != expected {expected}")
    p = 0
    for ir, rb in enumerate(radial):
        for f, name in zip(fields, field_names):
            X += theta[p] * rb[:, None, None, None] * f[None, :, :, :]
            names.append(f"b{ir}:{name}")
            p += 1

    q = np.zeros_like(X)
    for a in range(nr):
        for b in range(ns):
            q[a, b] = geom["sq"][b] @ sym_exp(X[a, b]) @ geom["sq"][b]
    Dr = Dt / R
    D2r = D2t / (R * R)
    return r, Dr, D2r, q, names


def normal_derivatives(q: np.ndarray, Dr: np.ndarray, D2r: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    qn = np.einsum("ab,bsij->asij", Dr, q)
    qnn = np.einsum("ab,bsij->asij", D2r, q)
    return qn, qnn


def full_residual(
    q: np.ndarray, Dr: np.ndarray, D2r: np.ndarray,
    qn_override: np.ndarray | None = None,
    qnn_override: np.ndarray | None = None,
) -> Dict[str, np.ndarray]:
    nr, ns = q.shape[:2]
    qn, qnn = normal_derivatives(q, Dr, D2r)
    if qn_override is not None:
        qn = qn_override
    if qnn_override is not None:
        qnn = qnn_override
    K = 0.5 * qn
    Kn = 0.5 * qnn
    qi = np.linalg.inv(q)
    W = np.einsum("rsij,rsjk->rsik", qi, K)
    H = np.trace(W, axis1=2, axis2=3)
    W2 = np.einsum("rsij,rsji->rs", W, W)
    KqiK = np.einsum("rsij,rsjk,rskl->rsil", K, qi, K)

    ric3 = np.zeros_like(q)
    mom = np.zeros((nr, ns, 3))
    scalar3 = np.zeros((nr, ns))
    for a in range(nr):
        # Compute Codazzi with H differentiated from K/q. This remains consistent
        # when exact endpoint q_n jets override the global spectral derivative.
        gamma, rr, scal = evol.christoffel_and_ricci(q[a])
        ric3[a] = rr
        scalar3[a] = scal
        ks = evol.spectral_derivative(K[a], 1)
        hs = evol.spectral_derivative(H[a], 1)
        for i in range(3):
            val = np.zeros(ns)
            for j in range(3):
                for kk in range(3):
                    nab = ks[:, kk, i] if j == 0 else np.zeros(ns)
                    for ell in range(3):
                        nab -= gamma[:, ell, j, kk] * K[a, :, ell, i]
                        nab -= gamma[:, ell, j, i] * K[a, :, kk, ell]
                    val += qi[a, :, j, kk] * nab
            if i == 0:
                val -= hs
            mom[a, :, i] = val

    ET = ric3 + 3.0 * q - Kn - H[:, :, None, None] * K + 2.0 * KqiK
    Enn = 3.0 - np.einsum("rsij,rsji->rs", qi, Kn) + W2

    Eorth = np.zeros((nr, ns, 4, 4))
    op = np.zeros((nr, ns))
    mineig_q = np.zeros((nr, ns))
    for a in range(nr):
        for b in range(ns):
            E = np.zeros((4, 4))
            E[0, 0] = Enn[a, b]
            E[0, 1:] = mom[a, b]
            E[1:, 0] = mom[a, b]
            E[1:, 1:] = ET[a, b]
            g = np.zeros((4, 4))
            g[0, 0] = 1.0
            g[1:, 1:] = q[a, b]
            L = np.linalg.cholesky(g)
            left = np.linalg.solve(L, E)
            eo = np.linalg.solve(L, left.T).T
            eo = 0.5 * (eo + eo.T)
            Eorth[a, b] = eo
            op[a, b] = np.max(np.abs(np.linalg.eigvalsh(eo)))
            mineig_q[a, b] = np.min(np.linalg.eigvalsh(q[a, b]))

    # Frobenius-isometric packing of symmetric Eorth.
    vec_parts = []
    for i, j in PAIR4:
        factor = 1.0 if i == j else math.sqrt(2.0)
        vec_parts.append(factor * Eorth[:, :, i, j])
    packed = np.stack(vec_parts, axis=2)
    return dict(qn=qn, qnn=qnn, K=K, Kn=Kn, W=W, H=H, W2=W2,
                ric3=ric3, scalar3=scalar3, mom=mom, ET=ET, Enn=Enn,
                Eorth=Eorth, packed=packed, op=op, mineig_q=mineig_q)


def weighted_vector(res: Dict[str, np.ndarray], endpoint_weight: float = 1.0) -> np.ndarray:
    """Chebyshev-node residual vector; mild quadrature-like endpoint weighting."""
    arr = res["packed"].copy()
    arr[0] *= endpoint_weight
    arr[-1] *= endpoint_weight
    return arr.ravel()


def summarize_half(r: np.ndarray, res: Dict[str, np.ndarray]) -> Dict[str, object]:
    op = res["op"]
    idx = np.unravel_index(np.argmax(op), op.shape)
    eo = res["Eorth"]
    block = {
        "nn": float(np.max(np.abs(eo[:, :, 0, 0]))),
        "normal_tangential_frobenius": float(np.max(np.linalg.norm(eo[:, :, 0, 1:], axis=2))),
        "tangential_operator": float(np.max([np.max(np.abs(np.linalg.eigvalsh(eo[a,b,1:,1:]))) for a in range(eo.shape[0]) for b in range(eo.shape[1])])),
    }
    return {
        "operator_sup": float(op[idx]),
        "peak_r": float(r[idx[0]]),
        "peak_s_index": int(idx[1]),
        "frobenius_rms": float(np.sqrt(np.mean(res["packed"] ** 2))),
        "center_operator_sup": float(np.max(op[0])),
        "end_operator_sup": float(np.max(op[-1])),
        "minimum_q_eigenvalue": float(np.min(res["mineig_q"])),
        "blocks": block,
    }


def finite_difference_jacobian(fun, x: np.ndarray, f0: np.ndarray, eps: float) -> np.ndarray:
    J = np.empty((len(f0), len(x)))
    for j in range(len(x)):
        h = eps * max(1.0, abs(x[j]))
        xp = x.copy(); xp[j] += h
        xm = x.copy(); xm[j] -= h
        J[:, j] = (fun(xp) - fun(xm)) / (2.0 * h)
    return J


def svd_analysis(J: np.ndarray, F: np.ndarray, ridge: float) -> Tuple[np.ndarray, Dict[str, object]]:
    U, s, Vt = np.linalg.svd(J, full_matrices=False)
    proj = U.T @ F
    coeff = -s * proj / (s * s + ridge * ridge)
    dx = Vt.T @ coeff
    accessible = U @ proj
    record = {
        "singular_values": [float(x) for x in s],
        "condition_nonzero": float(s[0] / max(s[-1], 1e-300)),
        "residual_norm": float(np.linalg.norm(F)),
        "range_projection_norm": float(np.linalg.norm(accessible)),
        "linear_inaccessible_norm": float(np.linalg.norm(F - accessible)),
        "range_fraction": float(np.linalg.norm(accessible) / np.linalg.norm(F)),
        "ridge": float(ridge),
        "predicted_correction_norm": float(np.linalg.norm(dx)),
        "modes": [
            {
                "index": int(j),
                "s": float(s[j]),
                "left_projection": float(proj[j]),
                "undamped_required_coefficient": float(-proj[j] / s[j]) if s[j] > 1e-14 else None,
                "ridge_coefficient": float(coeff[j]),
            }
            for j in range(len(s))
        ],
    }
    return dx, record


def run_side(
    geom: Dict[str, np.ndarray], R: float, nr: int, sign: int,
    radial_count: int, richer: bool, gn_steps: int, fd_eps: float, ridge: float,
) -> Tuple[Dict[str, object], np.ndarray]:
    fields, _ = matrix_basis(geom["s"], int(geom["meta"]["wind"]), richer=richer)
    p = len(fields) * radial_count
    theta = np.zeros(p)

    cache = {}
    def evaluate(x: np.ndarray, details: bool = False):
        r, Dr, D2r, q, names = build_half(geom, R, nr, sign, x, radial_count, richer)
        qn_fd, qnn_fd = normal_derivatives(q, Dr, D2r)
        qn_fd[0] = 2.0 * sign * geom["k0"]
        qnn_fd[0] = 2.0 * (geom["ric0"] + 3.0 * geom["q0"] + 2.0 * np.einsum(
            "sij,sjk,skl->sil", geom["k0"], np.linalg.inv(geom["q0"]), geom["k0"]))
        qn_fd[-1] = 2.0 * q[-1]
        qnn_fd[-1] = 4.0 * q[-1]
        res = full_residual(q, Dr, D2r, qn_override=qn_fd, qnn_override=qnn_fd)
        if details:
            return r, q, res, names
        return weighted_vector(res)

    r, q, res, names = evaluate(theta, details=True)
    history = [{"iteration": 0, "theta_norm": 0.0, **summarize_half(r, res)}]
    spectral_records = []
    for it in range(gn_steps):
        F = weighted_vector(res)
        J = finite_difference_jacobian(evaluate, theta, F, fd_eps)
        dx, sr = svd_analysis(J, F, ridge)
        sr["iteration"] = it
        spectral_records.append(sr)
        # Trust the linear correction only after a nonlinear line search.
        candidates = []
        for alpha in [1.0, 0.5, 0.25, 0.125, 0.0625]:
            trial = np.clip(theta + alpha * dx, -3.0, 3.0)
            rr, qq, rs, _ = evaluate(trial, details=True)
            candidates.append((np.linalg.norm(weighted_vector(rs)), alpha, trial, rr, qq, rs))
        candidates.sort(key=lambda z: z[0])
        best = candidates[0]
        oldnorm = np.linalg.norm(F)
        if best[0] >= oldnorm:
            history.append({"iteration": it + 1, "accepted": False, "linear_vector_norm_old": float(oldnorm),
                            "best_trial_vector_norm": float(best[0]), "best_alpha": float(best[1]),
                            "reason": "no nonlinear line-search decrease"})
            break
        _, alpha, theta, r, q, res = best
        h = {"iteration": it + 1, "accepted": True, "alpha": float(alpha),
             "theta_norm": float(np.linalg.norm(theta)), "linear_vector_norm_old": float(oldnorm),
             "nonlinear_vector_norm_new": float(best[0]), **summarize_half(r, res)}
        history.append(h)

    final = summarize_half(r, res)
    # Largest coefficients are the most interpretable finite-dimensional changes.
    order = np.argsort(-np.abs(theta))[:min(12, len(theta))]
    record = {
        "side": "positive" if sign > 0 else "negative",
        "global_n_center_jet_sign": int(sign),
        "parameter_count": int(p),
        "radial_shape_count": int(radial_count),
        "richer_fourier_basis": bool(richer),
        "baseline": history[0],
        "history": history,
        "spectral_analysis": spectral_records,
        "final": final,
        "largest_coefficients": [{"name": names[j], "value": float(theta[j])} for j in order],
    }
    return record, theta


def jet_validation(geom: Dict[str, np.ndarray], R: float, nr: int, sign: int,
                   radial_count: int, richer: bool) -> Dict[str, float]:
    fields, _ = matrix_basis(geom["s"], int(geom["meta"]["wind"]), richer=richer)
    theta = np.zeros(len(fields) * radial_count)
    r, Dr, D2r, q, _ = build_half(geom, R, nr, sign, theta, radial_count, richer)
    qn, qnn = normal_derivatives(q, Dr, D2r)
    target_qnn = 2.0 * (geom["ric0"] + 3.0 * geom["q0"] + 2.0 * np.einsum(
        "sij,sjk,skl->sil", geom["k0"], np.linalg.inv(geom["q0"]), geom["k0"]))
    # Exact endpoint jets follow analytically from the matrix-exponential construction;
    # the numerical fields below quantify global Chebyshev differentiation resolution.
    Xn0 = 2.0 * sign * geom["A"]
    Xnn0 = 2.0 * geom["B"]
    qn_exact0 = np.einsum("sij,sjk,skl->sil", geom["sq"], Xn0, geom["sq"])
    # For exp(X), the second derivative at X=0 is X_nn + X_n^2.
    qnn_exact0 = np.stack([geom["sq"][k] @ (Xnn0[k] + 4.0 * geom["A"][k] @ geom["A"][k]) @ geom["sq"][k]
                           for k in range(geom["q0"].shape[0])])
    return {
        "q0_exact_abs": float(np.max(np.abs(q[0] - geom["q0"]))),
        "analytic_qn0_abs": float(np.max(np.abs(qn_exact0 - 2.0 * sign * geom["k0"]))),
        "analytic_qnn0_abs": float(np.max(np.abs(qnn_exact0 - target_qnn))),
        "spectral_qn0_abs": float(np.max(np.abs(qn[0] - 2.0 * sign * geom["k0"]))),
        "spectral_qnn0_abs": float(np.max(np.abs(qnn[0] - target_qnn))),
        "spectral_end_qn_minus_2q_abs": float(np.max(np.abs(qn[-1] - 2.0 * q[-1]))),
        "spectral_end_qnn_minus_4q_abs": float(np.max(np.abs(qnn[-1] - 4.0 * q[-1]))),
    }


def known_metric_validation(nr: int, ns: int, R: float) -> Dict[str, float]:
    t, Dt, D2t = chebyshev_lobatto_01(nr)
    r = R * t
    Dr, D2r = Dt / R, D2t / (R * R)
    q = np.zeros((nr, ns, 3, 3))
    for a, rv in enumerate(r):
        q[a] = math.exp(2.0 * rv) * np.eye(3)[None, :, :]
    res = full_residual(q, Dr, D2r)
    # Exact endpoint jets remove differentiation noise in the attachment rows.
    qn, qnn = normal_derivatives(q, Dr, D2r)
    qn[[0,-1]] = 2.0 * q[[0,-1]]
    qnn[[0,-1]] = 4.0 * q[[0,-1]]
    res = full_residual(q, Dr, D2r, qn_override=qn, qnn_override=qnn)
    return {"hyperbolic_flat_slice_operator_sup": float(np.max(res["op"])),
            "hyperbolic_center_sup": float(np.max(res["op"][0])),
            "hyperbolic_end_sup": float(np.max(res["op"][-1]))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nr", type=int, default=27)
    ap.add_argument("--ns", type=int, default=32)
    ap.add_argument("--R", type=float, default=2.5)
    ap.add_argument("--wind", type=int, default=2)
    ap.add_argument("--S", type=float, default=1.0)
    ap.add_argument("--Qmax", type=float, default=0.5)
    ap.add_argument("--radial-count", type=int, default=1)
    ap.add_argument("--richer", action="store_true")
    ap.add_argument("--gn-steps", type=int, default=1)
    ap.add_argument("--fd-eps", type=float, default=2e-4)
    ap.add_argument("--ridge", type=float, default=1e-2)
    ap.add_argument("--output", default="workspace/data/step98_full_matrix_joint_transition.json")
    args = ap.parse_args()

    geom = center_geometry(args.ns, args.wind, args.S, args.Qmax)
    validation = {
        "known_metric": known_metric_validation(args.nr, args.ns, args.R),
        "positive_jets": jet_validation(geom, args.R, args.nr, +1, args.radial_count, args.richer),
        "negative_jets": jet_validation(geom, args.R, args.nr, -1, args.radial_count, args.richer),
        "center_constraint": {
            "scalar_target_error": float(np.max(np.abs(geom["scalar0"] + 6.0 + args.S))),
            "initial_meta": geom["meta"],
        },
    }

    pos, theta_pos = run_side(geom, args.R, args.nr, +1, args.radial_count, args.richer,
                              args.gn_steps, args.fd_eps, args.ridge)
    neg, theta_neg = run_side(geom, args.R, args.nr, -1, args.radial_count, args.richer,
                              args.gn_steps, args.fd_eps, args.ridge)
    out = {
        "model": "full SPD 3x3 matrix transition from one charged Koiso center to two expanding exteriors",
        "parameters": vars(args),
        "center_jets": {
            "X0": "0",
            "Xr0_positive_negative": "+/- 2 q0^(-1/2) K0 q0^(-1/2)",
            "Xrr0": "2(q0^(-1/2)Ric(q0)q0^(-1/2)+3I)",
            "end": "X=2RI, Xr=2I, Xrr=0",
        },
        "validation": validation,
        "positive_half": pos,
        "negative_half": neg,
        "joint": {
            "baseline_operator_sup": float(max(pos["baseline"]["operator_sup"], neg["baseline"]["operator_sup"])),
            "final_operator_sup": float(max(pos["final"]["operator_sup"], neg["final"]["operator_sup"])),
            "positive_theta_norm": float(np.linalg.norm(theta_pos)),
            "negative_theta_norm": float(np.linalg.norm(theta_neg)),
            "shared_center_parameters": {"S": args.S, "Qmax": args.Qmax, "wind": args.wind},
        },
        "interpretation": (
            "Finite-dimensional pressure test only. A decrease shows that genuine full-matrix inner-transition "
            "directions compensate part of the complete Ricci residual while preserving the exact center and "
            "both C2 attachments. It does not establish an arbitrarily small defect, a nonlinear PDE solution, "
            "or a Yau-26 counterexample. A persistent residual in this ansatz is not a geometric obstruction."
        ),
    }
    path = Path(args.output)
    if not path.is_absolute():
        path = SESSION_ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    compact = {
        "output": str(path), "validation": validation,
        "positive": {"baseline": pos["baseline"], "final": pos["final"]},
        "negative": {"baseline": neg["baseline"], "final": neg["final"]},
        "joint": out["joint"],
    }
    print(json.dumps(compact, indent=2))


if __name__ == "__main__":
    main()
