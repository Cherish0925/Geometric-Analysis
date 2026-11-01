"""Step 95: exact test of the triangular formal-completion recursion for
Seiberg--Witten fields at a Wahl point Gamma = 1/n^2 (1, n-1).

Purpose.  Lemma 95.1 (notes/step95_*) states that, for ANY Gamma-invariant
smooth metric jet (Einstein or not), every permitted leading equivariant
monogenic term P_ell and every choice of free kernel data extend to a formal
power-series solution (Phi, a) of the unperturbed SW equations in Coulomb
gauge, with no obstruction at any order.  This script checks the recursion
exactly (Gaussian rationals) on a genuinely non-flat test metric.

Test metric.  g = e^{2u} g_0 on C^2 with Gamma-invariant
    u = |z1|^2 + 2|z2|^2 + |z1|^2 |z2|^2 + 2 Re(z1^{n-1} conj z2)
(the last term is Gamma-invariant but not torus-invariant, so the test metric
has no continuous symmetry; for n=3 it is quadratic).
Conformal covariance (dimension four) gives, with Psi = e^{3u/2} Phi:
    D_{g,A} Phi = e^{-5u/2} D_{0,A} Psi,
    F_A^+ = rho_g^{-1} q(Phi) = e^{-u} q_0(Psi)     (Hodge star on 2-forms is conformal),
    Coulomb gauge d^*_g a = 0  <=>  d^*_0 (e^{2u} a) = 0 .
So the system solved for (Psi, a) is
    E1  D_{0,A} Psi = 0                         (2 complex equations, S^-)
    E2  (da)^{2,0}       = + e^{-u} conj(psi0) psi1
    E2' (da)^{0,2}       = - e^{-u} psi0 conj(psi1)      (reality partner of E2)
    E3  tr (da)^{1,1}    = e^{-u} (|psi0|^2 - |psi1|^2)
    E4  sum_i dbar_i(e^{2u} a_i) + d_i(e^{2u} a_ibar) = 0 .
Constants are immaterial for solvability.  a = a1 dz1 + a2 dz2 + a1b dzb1 + a2b dzb2
is treated as four independent complex polynomials; the Moore--Penrose (least
norm) choice commutes with the antiunitary real structure, so reality
a_ibar = -conj(a_i) is an output check, not an input.

Flat Dirac convention (Step 94, verified equivariant):
    D^+ = [[d_z1, d_zb2], [-d_z2, d_zb1]],
    D_{0,A} = D^+ + M1 a1 + M2 a2 + N1 a1b + N2 a2b,
with M1=[[1,0],[0,0]], M2=[[0,0],[-1,0]], N1=[[0,0],[0,1]], N2=[[0,1],[0,0]].

Free data included: the invariant constant-ASD-curvature connection
    a^(1) = t (zb1 dz1 - z1 dzb1 - zb2 dz2 + z2 dzb2),
which is closed under d^+, d^* and reality.

Output: workspace/data/step95/sw_formal_completion.json with, per degree,
domain/target sector dimensions, rank (surjectivity), residual checks, and the
reality and equivariance checks of the constructed jet.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

z1, z2, w1, w2 = sp.symbols("z1 z2 w1 w2")  # w_i = conj(z_i) as independent variables
VARS = (z1, z2, w1, w2)


def wt(mono_exp, n):
    a, b, c, d = mono_exp
    return a + (n - 1) * b - c - (n - 1) * d


def monos(deg):
    out = []
    for a in range(deg + 1):
        for b in range(deg + 1 - a):
            for c in range(deg + 1 - a - b):
                d = deg - a - b - c
                out.append((a, b, c, d))
    return out


def mono(e):
    return z1 ** e[0] * z2 ** e[1] * w1 ** e[2] * w2 ** e[3]


def pconj(expr):
    """Polynomial complex conjugation: swap z<->w and conjugate coefficients."""
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    p = sp.Poly(expr, *VARS)
    res = 0
    for (a, b, c, d), co in p.terms():
        res += sp.conjugate(co) * z1 ** c * z2 ** d * w1 ** a * w2 ** b
    return sp.expand(res)


def homog(expr, deg):
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    p = sp.Poly(expr, *VARS)
    return sp.expand(sum(co * mono(e) for e, co in p.terms() if sum(e) == deg))


def trunc(expr, maxdeg):
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    p = sp.Poly(expr, *VARS)
    return sp.expand(sum(co * mono(e) for e, co in p.terms() if sum(e) <= maxdeg))


def exp_series(f, maxdeg):
    """Truncated exp(f) for a polynomial f with f(0)=0 and lowest degree >=2."""
    res = sp.Integer(1)
    term = sp.Integer(1)
    for kk in range(1, maxdeg // 2 + 2):
        term = trunc(term * f / kk, maxdeg)
        res += term
    return trunc(res, maxdeg)


def d(f, v):
    return sp.diff(f, v)


def equations(Psi, a, u_em, u_e2):
    """Return list of (name, expr) residual expressions."""
    p0, p1 = Psi
    a1, a2, a1b, a2b = a
    E1_0 = d(p0, z1) + d(p1, w2) + a1 * p0 + a2b * p1
    E1_1 = -d(p0, z2) + d(p1, w1) - a2 * p0 + a1b * p1
    E2 = d(a2, z1) - d(a1, z2) - u_em * pconj(p0) * p1
    E2b = d(a2b, w1) - d(a1b, w2) + u_em * p0 * pconj(p1)
    E3 = d(a1b, z1) - d(a1, w1) + d(a2b, z2) - d(a2, w2) - u_em * (p0 * pconj(p0) - p1 * pconj(p1))
    E4 = d(u_e2 * a1, w1) + d(u_e2 * a2, w2) + d(u_e2 * a1b, z1) + d(u_e2 * a2b, z2)
    return [("E1_0", E1_0), ("E1_1", E1_1), ("E2", E2), ("E2b", E2b), ("E3", E3), ("E4", E4)]


def run(n, j, K, t_free):
    N = n * n
    m = (n * j) % N
    fw = (m % N, (m - n) % N)
    # coefficient weights required for invariance of a = sum a_i dz_i + ...
    aw = ((-1) % N, (-(n - 1)) % N, 1 % N, (n - 1) % N)
    ell = 2 * min(j - 1, n - j)
    if j - 1 <= n - j:
        P = (sp.Integer(0), (z1 * z2) ** (j - 1))
    else:
        P = ((w1 * w2) ** (n - j), sp.Integer(0))

    u = z1 * w1 + 2 * z2 * w2 + z1 * w1 * z2 * w2 + z1 ** (n - 1) * w2 + w1 ** (n - 1) * z2
    maxdeg = K + 2
    u_em = exp_series(-u, maxdeg)
    u_e2 = exp_series(2 * u, maxdeg)

    Psi = [P[0], P[1]]
    a = [t_free * w1, -t_free * w2, -t_free * z1, t_free * z2]

    log = []
    # unknown blocks at degree k: Psi_k (sectors fw), a_k (sectors aw)
    for k in range(1, K + 1):
        # residual at degree k-1 with current truncation (unknown degree-k pieces are zero)
        eqs = equations(Psi, a, u_em, u_e2)
        rhs = {name: homog(expr, k - 1) for name, expr in eqs}
        # build linear operator on degree-k unknowns
        unk = []  # (slot, exponent)
        for slot, w in enumerate(fw):
            for e in monos(k):
                if (wt(e, n) - w) % N == 0:
                    unk.append(("psi", slot, e))
        for slot, w in enumerate(aw):
            for e in monos(k):
                if (wt(e, n) - w) % N == 0:
                    unk.append(("a", slot, e))
        cols = []
        for kind, slot, e in unk:
            dPsi = [sp.Integer(0), sp.Integer(0)]
            da = [sp.Integer(0)] * 4
            if kind == "psi":
                dPsi[slot] = mono(e)
            else:
                da[slot] = mono(e)
            # linear part at degree k-1: flat principal operators only (lower-order
            # couplings land in degree >= k)
            p0, p1 = dPsi
            a1, a2, a1b, a2b = da
            col = {
                "E1_0": d(p0, z1) + d(p1, w2),
                "E1_1": -d(p0, z2) + d(p1, w1),
                "E2": d(a2, z1) - d(a1, z2),
                "E2b": d(a2b, w1) - d(a1b, w2),
                "E3": d(a1b, z1) - d(a1, w1) + d(a2b, z2) - d(a2, w2),
                "E4": d(a1, w1) + d(a2, w2) + d(a1b, z1) + d(a2b, z2),
            }
            cols.append(col)
        # target sector basis: all monomials of degree k-1 in the equivariant sectors of each equation
        rows = []
        tw = {"E1_0": (fw[0] - 1) % N, "E1_1": (fw[0] - (n - 1)) % N,
              "E2": (-n) % N, "E2b": n % N, "E3": 0, "E4": 0}
        for name in ["E1_0", "E1_1", "E2", "E2b", "E3", "E4"]:
            for e in monos(k - 1):
                if (wt(e, n) - tw[name]) % N == 0:
                    rows.append((name, e))
        ridx = {r: i for i, r in enumerate(rows)}

        def coeff_vec(exprs):
            v = sp.zeros(len(rows), 1)
            for name, expr in exprs.items():
                expr = sp.expand(expr)
                if expr == 0:
                    continue
                p = sp.Poly(expr, *VARS)
                for e, co in p.terms():
                    key = (name, e)
                    if key not in ridx:
                        raise RuntimeError(f"term outside equivariant target sector: {key}")
                    v[ridx[key]] += co
            return v

        M = sp.zeros(len(rows), len(unk))
        for c, col in enumerate(cols):
            M[:, c] = coeff_vec(col)
        b = -coeff_vec(rhs)
        rank = M.rank()
        surj = rank == len(rows)
        # least-norm solution x = M^T (M M^T)^{-1} b  (M is integer)
        G = M * M.T
        y = G.LUsolve(b)
        x = M.T * y
        for (kind, slot, e), xv in zip(unk, x):
            if xv == 0:
                continue
            if kind == "psi":
                Psi[slot] = sp.expand(Psi[slot] + xv * mono(e))
            else:
                a[slot] = sp.expand(a[slot] + xv * mono(e))
        # verify residual at degree k-1 now vanishes
        eqs2 = equations(Psi, a, u_em, u_e2)
        res_ok = all(homog(expr, k - 1) == 0 for _, expr in eqs2)
        log.append({"k": k, "unknowns": len(unk), "targets": len(rows), "rank": int(rank),
                    "surjective": bool(surj), "kernel_dim": len(unk) - int(rank),
                    "source_nonzero": bool(any(v != 0 for v in b)),
                    "residual_degree_k_minus_1_zero": bool(res_ok)})
        print(n, j, log[-1], flush=True)

    # final checks: all residuals vanish through degree K-1
    eqs = equations(Psi, a, u_em, u_e2)
    all_ok = all(homog(expr, dd) == 0 for _, expr in eqs for dd in range(0, K))
    # reality: a_ibar = -conj(a_i)
    real_ok = (sp.expand(a[2] + pconj(a[0])) == 0) and (sp.expand(a[3] + pconj(a[1])) == 0)
    # equivariance (by construction of sectors) and curvature onset degree
    a_low = min((sum(e) for comp in a for e, _ in (sp.Poly(comp, *VARS).terms() if comp != 0 else [])), default=None)
    return {
        "n": n, "j": j, "ell": ell, "K": K, "t_free_ASD": str(t_free),
        "leading": [str(P[0]), str(P[1])],
        "steps": log,
        "all_residuals_vanish_below_degree_K": bool(all_ok),
        "reality_a_bar_eq_minus_conj_a": bool(real_ok),
        "lowest_degree_in_a": a_low,
        "Psi_degree_terms": {str(k): bool(homog(Psi[0], k) != 0 or homog(Psi[1], k) != 0) for k in range(K + 1)},
    }


def main():
    cases = [(5, 2, 7, sp.Rational(1, 3)), (5, 3, 9, sp.Rational(1, 2)), (3, 2, 7, sp.Integer(1)), (7, 3, 9, sp.Rational(2, 5))]
    if len(sys.argv) > 1 and sys.argv[1] == "quick":
        cases = cases[:1]
    out = {"lemma": "Step 95 formal completion of SW at a Wahl point, conformal non-flat metric", "cases": []}
    for n, j, K, t in cases:
        out["cases"].append(run(n, j, K, t))
    path = Path(__file__).resolve().parents[1] / "data" / "step95" / "sw_formal_completion.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2) + "\n")
    print(path)
    for c in out["cases"]:
        print(c["n"], c["j"], "ok", c["all_residuals_vanish_below_degree_K"], "real", c["reality_a_bar_eq_minus_conj_a"],
              "surj", all(s["surjective"] for s in c["steps"]))


if __name__ == "__main__":
    main()
