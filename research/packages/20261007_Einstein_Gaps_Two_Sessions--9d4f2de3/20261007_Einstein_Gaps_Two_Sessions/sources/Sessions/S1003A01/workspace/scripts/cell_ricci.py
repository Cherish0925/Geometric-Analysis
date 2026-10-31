"""Exact Ricci eigenvalues for conformal triaxial one-bolt cells.

Metric (inherited notation, relative_cell_cost.md eq. (6.3), (6.10)):
    G = exp(2 phi) K,
    K = dr^2/F + r^2 (e^{2w} s1^2 + e^{-2w} s2^2) + r^2 F s3^2,
with d s_i = 2 s_j ^ s_k, int s1 s2 s3 = 2 pi^2.
Orthonormal coframe e0 = A dr, e_i = a_i s_i,
    A = e^phi / sqrt(F), a1 = e^phi r e^w, a2 = e^phi r e^-w, a3 = e^phi r sqrt(F).
Bianchi IX Ricci (derivatives in arclength t, d/dt = (1/A) d/dr):
    Ric_00 = -sum a_i''/a_i
    Ric_ii = -a_i''/a_i - (a_i'/a_i)(a_j'/a_j + a_k'/a_k)
             + 2 (a_i^4 - (a_j^2 - a_k^2)^2) / (a_i^2 a_j^2 a_k^2).
Normalized cost j = J/(2 pi^2) = int e^{4 phi} r^3 sum_a (Ric_aa + 1)^2 dr,
J = int |Ric_G + G|^2 dV_G.

Output: function `ricci_exprs()` returning sympy expressions of the four
eigenvalues multiplied by e^{2 phi} (so they are polynomial-exponential in
the jet (r,F,F1,F2,w,w1,w2,p,p1,p2)), and a lambdified evaluator.
"""
import sympy as sp

r = sp.symbols('r', positive=True)
Fs, F1, F2, ws, w1, w2, ps, p1, p2 = sp.symbols('F F1 F2 w w1 w2 p p1 p2', real=True)


def ricci_exprs():
    Ff = sp.Function('F')(r)
    wf = sp.Function('w')(r)
    pf = sp.Function('p')(r)
    A = sp.exp(pf) / sp.sqrt(Ff)
    a = [sp.exp(pf) * r * sp.exp(wf), sp.exp(pf) * r * sp.exp(-wf), sp.exp(pf) * r * sp.sqrt(Ff)]
    D = lambda f: sp.diff(f, r) / A
    a1d = [D(x) for x in a]
    a2d = [D(x) for x in a1d]
    lg = [a1d[i] / a[i] for i in range(3)]
    sec = [a2d[i] / a[i] for i in range(3)]
    ric = [-(sec[0] + sec[1] + sec[2])]
    for i in range(3):
        j, k = [(1, 2), (0, 2), (0, 1)][i]
        ric.append(-sec[i] - lg[i] * (lg[j] + lg[k])
                   + 2 * (a[i]**4 - (a[j]**2 - a[k]**2)**2) / (a[i]**2 * a[j]**2 * a[k]**2))
    subs = {}
    out = []
    for e in ric:
        e = sp.expand(e * sp.exp(2 * pf))
        e = e.subs({sp.diff(Ff, r, 2): F2, sp.diff(wf, r, 2): w2, sp.diff(pf, r, 2): p2})
        e = e.subs({sp.diff(Ff, r): F1, sp.diff(wf, r): w1, sp.diff(pf, r): p1})
        e = e.subs({Ff: Fs, wf: ws, pf: ps})
        e = sp.simplify(sp.expand(e))
        out.append(e)
    return out  # e^{2p} * Ric_aa, a = 0,1,2,3


if __name__ == '__main__':
    ex = ricci_exprs()
    for i, e in enumerate(ex):
        print(f'e^(2phi) Ric_{i}{i} =', e)
