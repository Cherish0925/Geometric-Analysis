"""Step 53a: exact check of the geometric (conformal + diffeomorphism) Ric0 corrector for the perpendicular
Burns tail (Spirit #62 candidate).

Setting (same conventions/engine as step50_exact_identity.py and step52_ric0_corrector.py):
  flat chart, zeta = J3, Burns g_eps = delta + eps*kB, kB = (v0 v0^T + v1 v1^T)/u^2, v_m = J_m x, u = |x|^2.
  Pure-Ric0 normal 2-jet  h_E = -(1/6)(E u + q delta - Ex x^T - x (Ex)^T),  E trace-free, q = x.Ex.
Claims tested:
  (a) h_E = 2 f delta + L_V delta,  f = -q/4,  V = -u E x/12 + q x/6.
  (b) f_eps = f - eps q_H/(8u), q_H = x.E_H x, E_H = (E + J^T E J)/2, is g_eps-harmonic to first order in eps.
  (c) with k0E = L_V kB - (q/2) kB - (q_H/(4u)) delta,
        W+''_flat(h_E, kB) + W+'_flat(k0E) = 0,   s''_flat(h_E, kB) + s'_flat(k0E) = 0   identically.
  Controls: the source without k0E is nonzero; dropping the q_H term breaks (c) (scalar part).
Usage: python step53_ric0_geometric_corrector.py  -> workspace/data/step53/ric0_geometric_corrector.json
"""
import os, json, time
import sympy as sp
import step52_ric0_corrector as E52

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "data", "step53"); os.makedirs(OUT, exist_ok=True)
x, X, u, kB, J3, I4 = E52.x, E52.X, E52.u, E52.kB, E52.J3, E52.I4

def lie(V, k):
    # (L_V k)_ij = V^l d_l k_ij + k_lj d_i V^l + k_il d_j V^l   (flat coordinates)
    return sp.Matrix(4, 4, lambda i, j: sum(V[l]*sp.diff(k[i, j], x[l]) + k[l, j]*sp.diff(V[l], x[i])
                                            + k[i, l]*sp.diff(V[l], x[j]) for l in range(4)))

def lap(g, f):
    gi = g.inv(); dg = sp.sqrt(g.det())
    return sum(sp.diff(dg*sum(gi[i, j]*sp.diff(f, x[j]) for j in range(4)), x[i]) for i in range(4))/dg

import random
random.seed(7)
PTS = [[sp.Rational(random.randint(-9, 9), random.randint(1, 7)) for _ in range(4)] for _ in range(5)]
def zero(e):
    # exact evaluation at 5 random rational points (Schwartz-Zippel style check of a rational-function identity)
    return all(sp.nsimplify(e.subs(dict(zip(x, p)))) == 0 for p in PTS)

def lap1(k, f):
    # first-order-in-eps part of the Laplacian of delta + eps k acting on f
    dk = [sum(sp.diff(k[i, m], x[i]) for i in range(4)) - sp.Rational(1, 2)*sp.diff(k.trace(), x[m]) for m in range(4)]
    return -sum(k[i, j]*sp.diff(f, x[i], x[j]) for i in range(4) for j in range(4)) - sum(dk[m]*sp.diff(f, x[m]) for m in range(4))

def run(Em, tag, res, with_qH=True):
    t0 = time.time()
    q = (X.T*Em*X)[0, 0]
    EH = (Em + J3.T*Em*J3)/2; qH = (X.T*EH*X)[0, 0]
    f = -q/4; V = -u*(Em*X)/12 + q*X/6
    h = E52.hR_of(Em)
    res[f"{tag}_a_hE_eq_2fdelta_plus_LVdelta"] = all(zero(z) for z in (2*f*I4 + lie(V, I4) - h))
    k0 = lie(V, kB) - (q/2)*kB - (((qH/(4*u))*I4) if with_qH else sp.zeros(4, 4))
    k0 = sp.Matrix(4, 4, lambda i, j: sp.together(sp.expand(k0[i, j])))
    Rh = E52.R_lin(h); RK = E52.R_lin(kB)
    src = E52.add(E52.R_bil(h, kB), E52.frame_corr(h, RK), E52.frame_corr(kB, Rh))
    tot = E52.vec_out(E52.add(src, E52.R_lin(k0)))
    vals = [[sp.nsimplify(z.subs(dict(zip(x, p)))) for p in PTS] for z in tot]
    res[f"{tag}_c_pointvalues{'_noqH' if not with_qH else ''}"] = [[str(v) for v in row] for row in vals]
    res[f"{tag}_c_identity_holds{'_noqH' if not with_qH else ''}"] = all(v == 0 for row in vals for v in row)
    if with_qH:
        S = E52.vec_out(src)
        res[f"{tag}_source_nonzero"] = not all(zero(z) for z in S)
    print(tag, with_qH, time.time()-t0, flush=True)

def main():
    t0 = time.time(); res = {}
    E1 = sp.Matrix([[1, 3, 0, 2], [3, -5, 4, 0], [0, 4, 7, -1], [2, 0, -1, -3]])/10
    E2 = sp.Matrix([[2, -1, 1, 0], [-1, 0, 2, 3], [1, 2, -1, 1], [0, 3, 1, -1]])/7
    # (b) harmonicity of f_eps to first order in eps (symbolic in eps, E1)
    q = (X.T*E1*X)[0, 0]; EH = (E1 + J3.T*E1*J3)/2; qH = (X.T*EH*X)[0, 0]
    f = -q/4; f1 = -qH/(8*u)
    L0 = sum(sp.diff(f, xi, 2) for xi in x)
    L1 = lap1(kB, f) + sum(sp.diff(f1, xi, 2) for xi in x)
    res["b_flat_harmonic_f"] = zero(L0); res["b_first_order_harmonic_feps"] = zero(L1)
    res["b_control_first_order_of_plain_f_nonzero"] = not zero(lap1(kB, f))
    print("b", res, time.time()-t0, flush=True)
    run(E1, "E1", res); run(E2, "E2", res); run(E1, "E1", res, with_qH=False)
    res["time_s"] = time.time()-t0
    print(json.dumps(res, indent=1))
    json.dump(res, open(os.path.join(OUT, "ric0_geometric_corrector.json"), "w"), indent=1)
    return res

if __name__ == "__main__":
    main()
