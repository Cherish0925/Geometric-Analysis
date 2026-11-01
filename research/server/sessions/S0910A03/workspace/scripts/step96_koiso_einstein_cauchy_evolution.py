"""
Step 96: spectral method-of-lines experiment for the exact analytic Einstein
continuation of the charged Koiso separator from Step 94.

The 4-metric is put in Gaussian normal form
    g = dn^2 + q(n,s)_{ij} dy^i dy^j,
where y=(s,x,y), all coefficients are T^2-invariant, and s is periodic.  If
K=(1/2) partial_n q is the second fundamental form, Ric_g=-3g is equivalent to

    partial_n q = 2 K,
    partial_n K = Ric(q)+3q-HK+2 K q^{-1} K,

provided the Hamiltonian and momentum constraints hold at n=0.  The Step 94
charged data satisfy those constraints exactly.  This script evolves the full
spatially varying 3x3 tensors; it is not a radial/constant-coefficient T^3
ansatz.  Fourier differentiation is used only in the periodic s direction.

The experiment is intended to reveal the first global failure/success mode of
the genuine charged Einstein germ.  Since elliptic Einstein Cauchy evolution is
ill-posed as a forward numerical problem, only intervals on which constraints
remain small are interpreted.  Resolution comparisons are recorded.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
from scipy.integrate import solve_ivp


L = 2.0 * math.pi
DIM = 3
PAIR = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]


def spectral_derivative(a: np.ndarray, order: int = 1) -> np.ndarray:
    """Periodic s derivative along axis 0, with period 2 pi."""
    n = a.shape[0]
    wave = 2.0 * math.pi * np.fft.fftfreq(n, d=L / n)
    # With L=2pi this gives integer wave numbers.
    multiplier = (1j * wave) ** order
    shape = (n,) + (1,) * (a.ndim - 1)
    out = np.fft.ifft(np.fft.fft(a, axis=0) * multiplier.reshape(shape), axis=0)
    return out.real


def pack_symmetric(q: np.ndarray, k: np.ndarray) -> np.ndarray:
    cols = [q[:, i, j] for i, j in PAIR] + [k[:, i, j] for i, j in PAIR]
    return np.stack(cols, axis=1).ravel()


def unpack_symmetric(y: np.ndarray, ngrid: int) -> Tuple[np.ndarray, np.ndarray]:
    z = y.reshape(ngrid, 12)
    q = np.zeros((ngrid, DIM, DIM))
    k = np.zeros_like(q)
    for c, (i, j) in enumerate(PAIR):
        q[:, i, j] = z[:, c]
        q[:, j, i] = z[:, c]
        k[:, i, j] = z[:, c + 6]
        k[:, j, i] = z[:, c + 6]
    return q, k


def christoffel_and_ricci(q: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Christoffel symbols, covariant Ricci, scalar curvature of q(s)."""
    ngrid = q.shape[0]
    qi = np.linalg.inv(q)
    qs = spectral_derivative(q, 1)
    gamma = np.zeros((ngrid, DIM, DIM, DIM))  # gamma[:, upper, lower, lower]
    for up in range(DIM):
        for i in range(DIM):
            for j in range(DIM):
                total = np.zeros(ngrid)
                for ell in range(DIM):
                    term = np.zeros(ngrid)
                    if i == 0:
                        term += qs[:, j, ell]
                    if j == 0:
                        term += qs[:, i, ell]
                    if ell == 0:
                        term -= qs[:, i, j]
                    total += qi[:, up, ell] * term
                gamma[:, up, i, j] = 0.5 * total

    gammas = spectral_derivative(gamma, 1)
    ric = np.zeros_like(q)
    for i in range(DIM):
        for j in range(DIM):
            val = np.zeros(ngrid)
            # partial_k Gamma^k_ij: only k=0 differentiates
            val += gammas[:, 0, i, j]
            # -partial_j Gamma^k_ik: only j=0 differentiates
            if j == 0:
                trace_g = np.zeros(ngrid)
                for kk in range(DIM):
                    trace_g += gamma[:, kk, i, kk]
                val -= spectral_derivative(trace_g, 1)
            for kk in range(DIM):
                trace2 = np.zeros(ngrid)
                for ell in range(DIM):
                    trace2 += gamma[:, ell, kk, ell]
                val += gamma[:, kk, i, j] * trace2
                for ell in range(DIM):
                    val -= gamma[:, ell, i, kk] * gamma[:, kk, j, ell]
            ric[:, i, j] = val
    ric = 0.5 * (ric + np.swapaxes(ric, 1, 2))
    scalar = np.einsum("nij,nij->n", qi, ric)
    return gamma, ric, scalar


def constraints(q: np.ndarray, k: np.ndarray) -> Dict[str, np.ndarray]:
    gamma, ric, scalar = christoffel_and_ricci(q)
    qi = np.linalg.inv(q)
    w = np.einsum("nij,njk->nik", qi, k)
    h = np.trace(w, axis1=1, axis2=2)
    w2 = np.einsum("nij,nji->n", w, w)
    # With K=(1/2)q_n and the convention used by the evolution equation,
    # Gauss gives R-H^2+|K|^2=-6.
    ham = scalar - h * h + w2 + 6.0

    ks = spectral_derivative(k, 1)
    hs = spectral_derivative(h, 1)
    mom = np.zeros((q.shape[0], DIM))
    # mom_i = q^{jk} nabla_j K_{ki} - partial_i H.
    # The derivative direction is j (not k); this matters for off-diagonal
    # mixed Weingarten data.
    for i in range(DIM):
        val = np.zeros(q.shape[0])
        for j in range(DIM):
            for kk in range(DIM):
                nab = ks[:, kk, i] if j == 0 else np.zeros(q.shape[0])
                for ell in range(DIM):
                    nab -= gamma[:, ell, j, kk] * k[:, ell, i]
                    nab -= gamma[:, ell, j, i] * k[:, kk, ell]
                val += qi[:, j, kk] * nab
        if i == 0:
            val -= hs
        mom[:, i] = val
    mom_norm2 = np.einsum("ni,nij,nj->n", mom, qi, mom)
    return {
        "scalar": scalar,
        "H": h,
        "W2": w2,
        "ham": ham,
        "mom": mom,
        "mom_norm": np.sqrt(np.maximum(mom_norm2, 0.0)),
        "W": w,
    }


def initial_data(ngrid: int, wind: int, total_s: float, qmax: float):
    s = np.linspace(0.0, L, ngrid, endpoint=False)
    speed = math.sqrt(12.0 + 2.0 * total_s)
    radius = math.asinh(speed / wind)
    theta = wind * s
    cR, sR = math.cosh(radius), math.sinh(radius)
    den = cR - sR * np.sin(theta)
    y = 1.0 / den
    alpha = np.log(y)
    beta = sR * np.cos(theta) / den

    # Use spectral derivatives so initial data and evolution share a discretization.
    alpha_s = spectral_derivative(alpha)
    beta_s = spectral_derivative(beta)
    es = alpha_s**2 + np.exp(-2.0 * alpha) * beta_s**2

    eminus = np.exp(-alpha)
    q0 = math.sqrt(2.0 * qmax / float(eminus.max()))
    qcov = np.array([q0, 0.0])
    charge_q = 0.5 * q0 * q0 * eminus
    p = total_s - charge_q
    if np.min(p) <= 0:
        raise ValueError("Need P=S-Q>0 pointwise")

    speed_grid = np.sqrt(es)
    talpha = alpha_s / speed_grid
    tbeta = beta_s / speed_grid
    nalpha = -np.exp(-alpha) * tbeta
    nbeta = np.exp(alpha) * talpha

    qmetric = np.zeros((ngrid, DIM, DIM))
    w = np.zeros_like(qmetric)
    mcov = -0.5 * qcov

    for j in range(ngrid):
        a = float(alpha[j])
        b = float(beta[j])
        em, ep = math.exp(-a), math.exp(a)
        m = np.array([[ep + b * b * em, b * em], [b * em, em]])
        ma = np.array([[ep - b * b * em, -b * em], [-b * em, -em]])
        mb = np.array([[2.0 * b * em, em], [em, 0.0]])
        mi = np.linalg.inv(m)
        cn = mi @ (ma * nalpha[j] + mb * nbeta[j])
        bblock = math.sqrt(float(p[j]) / 2.0) * cn
        mcontra = mi @ mcov

        qmetric[j, 0, 0] = 1.0
        qmetric[j, 1:, 1:] = m
        w[j, 0, 1:] = mcov
        w[j, 1:, 0] = mcontra
        w[j, 1:, 1:] = bblock

    kcov = np.einsum("nij,njk->nik", qmetric, w)
    kcov = 0.5 * (kcov + np.swapaxes(kcov, 1, 2))
    meta = {
        "wind": wind,
        "S": total_s,
        "Qmax_target": qmax,
        "target_circle_radius": radius,
        "coordinate_charge_q0": q0,
        "discrete_es_range": [float(es.min()), float(es.max())],
        "discrete_Q_range": [float(charge_q.min()), float(charge_q.max())],
    }
    return s, qmetric, kcov, meta


def apply_filter(a: np.ndarray, fraction: float = 2.0 / 3.0) -> np.ndarray:
    """Sharp Fourier dealiasing filter along s."""
    n = a.shape[0]
    coeff = np.fft.fft(a, axis=0)
    modes = np.fft.fftfreq(n) * n
    coeff[np.abs(modes) > fraction * (n // 2)] = 0.0
    return np.fft.ifft(coeff, axis=0).real


def rhs_factory(ngrid: int, dealias: bool = False):
    def rhs(_n: float, y: np.ndarray) -> np.ndarray:
        q, k = unpack_symmetric(y, ngrid)
        qi = np.linalg.inv(q)
        _, ric, _ = christoffel_and_ricci(q)
        w = np.einsum("nij,njk->nik", qi, k)
        h = np.trace(w, axis1=1, axis2=2)
        kqik = np.einsum("nij,njk,nkl->nil", k, qi, k)
        qn = 2.0 * k
        kn = ric + 3.0 * q - h[:, None, None] * k + 2.0 * kqik
        if dealias:
            qn = apply_filter(qn)
            kn = apply_filter(kn)
        return pack_symmetric(qn, kn)
    return rhs


def quotient_observables(q: np.ndarray, k: np.ndarray) -> Dict[str, np.ndarray]:
    """Recover quotient area, connection jet, conserved charge, and physical Q."""
    g = q[:, 1:, 1:]
    gi = np.linalg.inv(g)
    v = q[:, 1:, 0]
    avec = np.einsum("nij,nj->ni", gi, v)
    a2 = q[:, 0, 0] - np.einsum("ni,nij,nj->n", v, gi, v)
    a = np.sqrt(np.maximum(a2, 0.0))
    detg = np.linalg.det(g)
    rho = np.sqrt(np.maximum(detg, 0.0))
    sigma = np.log(rho)

    # q_n=2K gives the connection normal derivative without differencing in n.
    gn = 2.0 * k[:, 1:, 1:]
    vn = 2.0 * k[:, 1:, 0]
    an = np.einsum("nij,nj->ni", gi, vn - np.einsum("nij,nj->ni", gn, avec))
    f = an / a[:, None]
    charge = rho[:, None] * np.einsum("nij,nj->ni", g, f)
    physical_q = 0.5 * np.einsum("ni,nij,nj->n", f, g, f)
    return {
        "base_a": a,
        "rho": rho,
        "sigma": sigma,
        "connection": avec,
        "connection_n": an,
        "charge": charge,
        "Q": physical_q,
    }


def summarize(nval: float, q: np.ndarray, k: np.ndarray) -> Dict[str, object]:
    c = constraints(q, k)
    o = quotient_observables(q, k)
    qeig = np.linalg.eigvalsh(q)
    weig = np.linalg.eigvals(c["W"])
    # W is q-self-adjoint, so imaginary parts should be numerical noise.
    return {
        "n": float(nval),
        "q_eigenvalue_min": float(np.min(qeig)),
        "q_eigenvalue_max": float(np.max(qeig)),
        "H_range": [float(c["H"].min()), float(c["H"].max())],
        "H_mean": float(c["H"].mean()),
        "W_eigenvalue_real_range": [float(np.real(weig).min()), float(np.real(weig).max())],
        "W_eigenvalue_imag_max": float(np.abs(np.imag(weig)).max()),
        "scalar_range": [float(c["scalar"].min()), float(c["scalar"].max())],
        "hamiltonian_abs_max": float(np.abs(c["ham"]).max()),
        "momentum_norm_max": float(c["mom_norm"].max()),
        "base_a_range": [float(o["base_a"].min()), float(o["base_a"].max())],
        "rho_range": [float(o["rho"].min()), float(o["rho"].max())],
        "Q_range": [float(o["Q"].min()), float(o["Q"].max())],
        "charge_component_means": [float(x) for x in o["charge"].mean(axis=0)],
        "charge_component_std": [float(x) for x in o["charge"].std(axis=0)],
        "connection_abs_max": float(np.abs(o["connection"]).max()),
    }


def run_one(ngrid: int, nmax: float, wind: int, total_s: float, qmax: float, dealias: bool):
    s, q0, k0, meta = initial_data(ngrid, wind, total_s, qmax)
    y0 = pack_symmetric(q0, k0)
    sample = np.linspace(0.0, nmax, 21)
    sol = solve_ivp(
        rhs_factory(ngrid, dealias=dealias),
        (0.0, nmax),
        y0,
        method="DOP853",
        t_eval=sample,
        rtol=2e-9,
        atol=2e-11,
        max_step=min(0.02, nmax / 50.0),
    )
    summaries = []
    for col, nval in enumerate(sol.t):
        q, k = unpack_symmetric(sol.y[:, col], ngrid)
        summaries.append(summarize(float(nval), q, k))
    return {
        "ngrid": ngrid,
        "dealias": bool(dealias),
        "nmax_requested": nmax,
        "initial_meta": meta,
        "solver_success": bool(sol.success),
        "solver_message": sol.message,
        "n_reached": float(sol.t[-1]),
        "nfev": int(sol.nfev),
        "samples": summaries,
        "interpretation_rule": (
            "Only samples with positive q and small Hamiltonian/momentum residuals are "
            "scientifically interpreted; Einstein Cauchy evolution is elliptically ill-posed."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ngrids", default="48,64")
    parser.add_argument("--nmax", type=float, default=0.8)
    parser.add_argument("--wind", type=int, default=2)
    parser.add_argument("--S", type=float, default=1.0)
    parser.add_argument("--Qmax", type=float, default=0.5)
    parser.add_argument("--dealias", action="store_true")
    parser.add_argument(
        "--output",
        default="workspace/data/step96_koiso_einstein_cauchy_evolution.json",
    )
    args = parser.parse_args()
    runs = []
    for text in args.ngrids.split(","):
        runs.append(run_one(int(text), args.nmax, args.wind, args.S, args.Qmax, args.dealias))
    out = {
        "model": "full T2-invariant, s-dependent charged Koiso Einstein Cauchy evolution",
        "equations": {
            "q_n": "2K",
            "K_n": "Ric(q)+3q-HK+2K q^{-1} K",
            "constraints": "R(q)-H^2+|K|^2=-6 and div K-dH=0",
        },
        "runs": runs,
        "status": (
            "Numerical experiment on the exact local continuation. It is not a proof of "
            "global existence or nonexistence and is not the excluded radial cylindrical BVP."
        ),
    }
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps({
        "output": str(path),
        "runs": [
            {
                "N": r["ngrid"],
                "success": r["solver_success"],
                "reached": r["n_reached"],
                "nfev": r["nfev"],
                "first": r["samples"][0],
                "last": r["samples"][-1],
            }
            for r in runs
        ],
    }, indent=2))


if __name__ == "__main__":
    main()
