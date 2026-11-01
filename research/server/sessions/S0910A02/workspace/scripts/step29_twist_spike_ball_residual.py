"""
Step 29 refinement: finite-ball residual scaling for the local twist-spike jet.

The point-jet script proves that arbitrarily large connection curvature |F|^2=S
can be cancelled in the total Ricci tensor at one point by choosing the dilaton
and base 2-jets.  This script asks a sharper execution question: on the actual
analytic local metric

  g = exp(2 psi)(dx^2+dy^2+dz^2) + exp(2u)(dtheta+A)^2,
  A=(-B y/2)dx+(B x/2)dy,
  u=(H/2)(x^2+y^2+z^2),
  psi=(pa/2)(x^2+y^2)+(pc/2)z^2,

with H,pa,pc chosen so Ric(0)=Lambda g(0), how small is the Ricci-endomorphism
defect on a shrinking ball |(x,y,z)|<=r?  The expected Taylor scaling is roughly
O(S^2 r^2) because the uncancelled nonlinear terms are quadratic in distance.
If r=S^{-3/2}, the residual should decay like S^{-1} while |F|^2=S diverges at
the center.  This does not create a global closed metric, but it strengthens the
formal warning that pointwise twist bounds cannot follow from local Ricci algebra.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np
import sympy as sp


def build_lambdas():
    x, y, z, th = sp.symbols('x y z th')
    S, Lam = sp.symbols('S Lam', positive=True)
    B = sp.sqrt(S)
    coords = (x, y, z, th)
    n = 4
    H = (S - 2*Lam) / 6
    pa = -(4*Lam + 7*S) / 24
    pc = (5*S - 4*Lam) / 24
    psi = sp.Rational(1, 2) * pa * (x**2 + y**2) + sp.Rational(1, 2) * pc * z**2
    u = sp.Rational(1, 2) * H * (x**2 + y**2 + z**2)
    s = sp.exp(2 * psi)
    f2 = sp.exp(2 * u)
    A = [-B*y/2, B*x/2, sp.Integer(0)]
    g = sp.zeros(4)
    for i in range(3):
        g[i, i] = s
    for i in range(3):
        for j in range(3):
            g[i, j] += f2 * A[i] * A[j]
        g[i, 3] = f2 * A[i]
        g[3, i] = f2 * A[i]
    g[3, 3] = f2
    ginv = sp.simplify(g.inv())
    Gamma = [[[sp.Integer(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for bidx in range(n):
            for cidx in range(n):
                expr = sp.Integer(0)
                for d in range(n):
                    expr += ginv[a, d]*(sp.diff(g[d, cidx], coords[bidx]) + sp.diff(g[d, bidx], coords[cidx]) - sp.diff(g[bidx, cidx], coords[d]))
                Gamma[a][bidx][cidx] = sp.simplify(expr/2)
    Ric = sp.zeros(n)
    for bidx in range(n):
        for didx in range(n):
            expr = sp.Integer(0)
            for a in range(n):
                expr += sp.diff(Gamma[a][bidx][didx], coords[a]) - sp.diff(Gamma[a][bidx][a], coords[didx])
                for e in range(n):
                    expr += Gamma[a][a][e]*Gamma[e][bidx][didx] - Gamma[a][didx][e]*Gamma[e][bidx][a]
            Ric[bidx, didx] = sp.simplify(expr)
    End = sp.simplify(ginv * Ric - Lam*sp.eye(4))
    # Lambdify the 16 entries. theta does not appear.
    func = sp.lambdify((x, y, z, S, Lam), list(End), 'numpy')
    return func


def op_norm_4(mat):
    # Symmetrize relative to Euclidean coordinates as a rough diagnostic of the endomorphism entries.
    # For these tiny balls g is very close to identity; we also report max entry norm.
    M = np.array(mat, dtype=float).reshape(4, 4)
    return float(np.linalg.norm(M, 2)), float(np.max(np.abs(M)))


def sample_for_S(func, Sval, Lam=1.0, exponent=1.5):
    r = Sval ** (-exponent)
    pts = []
    # deterministic grid including axes and corners, scaled so max radius <= r
    vals = [-1.0, -0.5, 0.0, 0.5, 1.0]
    for a in vals:
        for b in vals:
            for c in vals:
                rad = (a*a+b*b+c*c)**0.5
                if rad <= 1.0 + 1e-12:
                    pts.append((r*a, r*b, r*c))
    max_op = 0.0
    max_entry = 0.0
    worst = None
    for p in pts:
        entries = func(p[0], p[1], p[2], Sval, Lam)
        op, ent = op_norm_4(entries)
        if op > max_op:
            max_op = op
            max_entry = ent
            worst = p
    return {
        "S": Sval,
        "Lambda": Lam,
        "radius_exponent": exponent,
        "r": r,
        "sample_count": len(pts),
        "max_operator_norm_approx": max_op,
        "max_entry_abs": max_entry,
        "worst_point": worst,
        "S_times_residual": Sval*max_op,
        "central_twist_norm_squared": Sval,
        "central_twist_norm": Sval**0.5,
        "scale_checks": {
            "S*r": Sval*r,
            "S*r^2": Sval*r*r,
            "S^2*r^2": Sval*Sval*r*r,
        }
    }


def main():
    func = build_lambdas()
    results = []
    for exp in [1.25, 1.5, 1.75]:
        for Sval in [10.0, 30.0, 100.0, 300.0, 1000.0]:
            results.append(sample_for_S(func, Sval, exponent=exp))
    # Estimate log-log slopes for each exponent.
    slopes = []
    for exp in [1.25, 1.5, 1.75]:
        sub = [r for r in results if r["radius_exponent"] == exp]
        xs = np.log([r["S"] for r in sub])
        ys = np.log([max(r["max_operator_norm_approx"], 1e-300) for r in sub])
        slope, intercept = np.polyfit(xs, ys, 1)
        slopes.append({"exponent": exp, "log_residual_vs_log_S_slope": float(slope), "intercept": float(intercept)})
    out = {
        "title": "Step 29 twist-spike finite-ball residual scaling",
        "scope": "Local analytic metric on shrinking balls; not a global closed metric and not a Yau-26 counterexample.",
        "expected_scaling": "uncancelled terms O(S^2 r^2); with r=S^{-alpha}, residual O(S^{2-2alpha})",
        "results": results,
        "loglog_slopes": slopes,
        "interpretation": [
            "For alpha>1 the Ricci-endomorphism defect on the sampled ball decreases while central |F|^2=S increases.",
            "This strengthens the point-jet evidence that no pointwise horizontal-twist bound can be obtained from C0 Ricci control without additional full-curvature, Sobolev, or collapse-scale structure.",
            "The construction is local and analytic before cutoff; global embedding would need transition control or a local prescribed-Ricci/gluing argument. It should be used as an adversarial test against pointwise-Moser claims, not as a counterexample to Yau-26."
        ]
    }
    path = Path(__file__).resolve().parents[1] / 'data' / 'step29_twist_spike_ball_residual.json'
    path.write_text(json.dumps(out, indent=2), encoding='utf-8')
    print(json.dumps(out, indent=2))
    print(f"\nSaved to {path}")


if __name__ == '__main__':
    main()
