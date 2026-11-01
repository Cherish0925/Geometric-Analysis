"""Step 56 control tests for the log-interaction computation.
(1) generic (non-invariant) Bianchi curvature R_p, correct tail: full S^3 quadrature (chi x alpha x beta).
(2) invariant R_p with the WRONG-sign A2 (tail not linearized Ricci-flat): does the S^3 integral still vanish?
(3) generic R_p, wrong-sign tail.
Writes workspace/data/step56_log_interaction_controls.json
"""
import numpy as np, math, os, json, sys
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, "step56_Tpoint_log_interaction.py")).read().replace("\nrun()\n", "\n")
ns = {"__file__": os.path.join(here, "step56_Tpoint_log_interaction.py")}
exec(compile(src, "m", "exec"), ns)
make_evaluator, ricci, F_density, tail, Y = ns["make_evaluator"], ns["ricci"], ns["F_density"], ns["tail"], ns["Y"]
import sympy as sp

def qmat_from_T(T):
    return sp.Matrix(4, 4, lambda i, j: -sp.Rational(1, 3) * sum(sp.Float(T[i, k, j, l], 17) * Y[k] * Y[l]
                     for k in range(4) for l in range(4) if abs(T[i, k, j, l]) > 1e-14))

def T_from_6x6(Rm):
    Om = []
    def form(pairs):
        M = np.zeros((4, 4))
        for (i, j), c in pairs:
            M[i, j] += c; M[j, i] -= c
        return M / math.sqrt(2)
    Om = [form([((0, 1), 1), ((2, 3), 1)]), form([((0, 2), 1), ((1, 3), -1)]), form([((0, 3), 1), ((1, 2), 1)]),
          form([((0, 1), 1), ((2, 3), -1)]), form([((0, 2), 1), ((1, 3), 1)]), form([((0, 3), 1), ((1, 2), -1)])]
    return np.einsum('AB,Aij,Bkl->ijkl', Rm, np.array(Om), np.array(Om))

rng = np.random.default_rng(7)
A = rng.normal(size=(6, 6)); Rm = (A + A.T) / 2
d = (np.trace(Rm[:3, :3]) - np.trace(Rm[3:, 3:])) / 6
Rm[:3, :3] -= d * np.eye(3); Rm[3:, 3:] += d * np.eye(3)   # Bianchi: tr R+ = tr R-
Tgen = T_from_6x6(Rm)
Tinv = ns["curv_tensor"](1.0, 0.5, -0.7, 0.9)

def coef_fn(evq, evt, p, h=4e-3, k=2e-4):
    gq, dgq, ddgq = evq(p); gt, dgt, ddgt = evt(p)
    F = lambda e, m: F_density(np.eye(4) + e * gq + m * gt, e * dgq + m * dgt, e * ddgq + m * ddgt)[0]
    def a21(h, k):
        G = lambda e: (F(e, k) - F(e, -k)) / (2 * k)
        return (G(h) + G(-h) - 2 * G(0)) / (2 * h * h)
    rk = lambda h: (4 * a21(h, k / 2) - a21(h, k)) / 3
    return (4 * rk(h / 2) - rk(h)) / 3

def S3_full(evq, evt, nchi=24, nang=12):
    xg, wg = np.polynomial.legendre.leggauss(nchi)
    chis = (xg + 1) * math.pi / 4; wch = wg * math.pi / 4
    angs = 2 * math.pi * np.arange(nang) / nang
    tot = 0.0; absint = 0.0
    for c, w in zip(chis, wch):
        for a in angs:
            for b in angs:
                p = np.array([math.cos(c) * math.cos(a), math.cos(c) * math.sin(a), math.sin(c) * math.cos(b), math.sin(c) * math.sin(b)])
                v = coef_fn(evq, evt, p)
                tot += w * math.sin(c) * math.cos(c) * v; absint += w * math.sin(c) * math.cos(c) * abs(v)
    f = (2 * math.pi / nang) ** 2
    return tot * f, absint * f

evt_good = make_evaluator(tail(1)); evt_bad = make_evaluator(tail(-1))
evq_gen = make_evaluator(qmat_from_T(Tgen)); evq_inv = make_evaluator(qmat_from_T(Tinv))
res = {}
res["generic_R_good_tail"] = S3_full(evq_gen, evt_good)
print("generic good", res["generic_R_good_tail"], flush=True)
res["invariant_R_bad_tail"] = S3_full(evq_inv, evt_bad, nang=4)
print("inv bad", res["invariant_R_bad_tail"], flush=True)
res["generic_R_bad_tail"] = S3_full(evq_gen, evt_bad)
print("generic bad", res["generic_R_bad_tail"], flush=True)
res["invariant_R_good_tail"] = S3_full(evq_inv, evt_good, nang=4)
print("inv good", res["invariant_R_good_tail"], flush=True)
res["format"] = "(signed S^3 integral of the e^2 m coefficient, S^3 integral of its absolute value)"
res["generic_R_6x6"] = Rm.tolist()
json.dump(res, open(os.path.join(here, "..", "data", "step56_log_interaction_controls.json"), "w"), indent=1)
