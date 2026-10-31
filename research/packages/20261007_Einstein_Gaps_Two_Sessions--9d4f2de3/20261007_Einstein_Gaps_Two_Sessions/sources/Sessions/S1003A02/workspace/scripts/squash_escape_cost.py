"""Cost of changing the CR (Rossi) squashing of a complex-hyperbolic end at large radius.

Linearized diagonal Bianchi-IX problem about CH (Ric=-6g), antisymmetric sector
    a1 = A e^{theta/2}, a2 = B, a3 = A e^{-theta/2},  A=sinh t, B=sinh t cosh t,
which changes the ratio of the two contact-plane radii, i.e. the Rossi squashing of the
standard CR sphere at infinity (theta -> C is a non-decaying linearized Einstein mode).
Conventions as in S1003A01/workspace/scripts/ch_linear_einstein_modes.py:
    P/(8 pi^2) = int (W/4) sum_i z_i^2 dt,  W=a1 a2 a3.
Second-order cost Q[theta] = int (W0/4) sum_i (dz_i)^2 dt, dz linear in theta.

Question decided here: the infimum of Q over theta with theta = k^{-1} C (the linearized
squashed Einstein filling) for t<T and theta = 0 for t large.  Writing theta = k^{-1} phi,
the Einstein operator has kernel {k^{-1}, k^{-1} int f^2}, hence Abel form
    sum_i dz_i^2 = c(t)^2 (psi')^2,  psi = phi'/m(t),
and the constrained minimum is  Q_min(T) = C^2 / G(T),  G(T) = int_T^inf M(t)^2 / w(t) dt,
with w = W0 c^2/4 and M(t) = int_t^inf m.  Output: exact coefficients and the asymptotics of
Q_min(T) as T -> infinity.  Writes workspace/data/squash_escape_cost.json.
"""
import json, pathlib
import sympy as sp
import mpmath as mp

ROOT = pathlib.Path(__file__).resolve().parents[1]
t, eps = sp.symbols('t epsilon', positive=True)
A = sp.sinh(t); B = sp.sinh(t) * sp.cosh(t)


def curvature(a):
    idx = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    u = [sp.diff(a[i], t) - (a[j]**2 + a[k]**2 - a[i]**2) / (a[j] * a[k]) for i, j, k in idx]
    H = [u[i] + u[j] * u[k] / 2 for i, j, k in idx]
    r = [sp.diff(u[i], t) / a[i] for i, j, k in idx]
    v = [2 * H[i] / (a[j] * a[k]) for i, j, k in idx]
    z = [r[i] - v[i] for i in range(3)]
    s = -2 * sum(r[i] + v[i] for i in range(3))
    return z, s


th = sp.Function('theta')(t)
z, s = curvature([A * sp.exp(eps * th / 2), B, A * sp.exp(-eps * th / 2)])
dz = [sp.simplify(sp.diff(e, eps).subs(eps, 0)) for e in z]
ds = sp.simplify(sp.diff(s, eps).subs(eps, 0))
z0, s0 = curvature([A, B, A])
assert all(sp.simplify(e) == 0 for e in z0)
W0 = A * B * A

# operator: dz1 = p2 th'' + p1 th' + p0 th
T2, T1, T0 = sp.symbols('T2 T1 T0')
e1 = dz[0].subs(sp.Derivative(th, (t, 2)), T2).subs(sp.Derivative(th, t), T1).subs(th, T0)
p2, p1, p0 = [sp.simplify(sp.diff(e1, v)) for v in (T2, T1, T0)]
assert sp.simplify(e1 - (p2 * T2 + p1 * T1 + p0 * T0)) == 0
ratio = [sp.simplify(dz[i] / dz[0]) if dz[0] != 0 else None for i in range(3)]

# kernel check: theta = k^{-1}, k = tanh^4 t
kinv = 1 / sp.tanh(t)**4
ker1 = sp.simplify((p2 * sp.diff(kinv, t, 2) + p1 * sp.diff(kinv, t) + p0 * kinv).rewrite(sp.exp))
# second kernel element from reduction of order: theta = kinv * phi, operator on phi
phi = sp.Function('phi')(t)
Lphi = sp.expand(p2 * sp.diff(kinv * phi, t, 2) + p1 * sp.diff(kinv * phi, t) + p0 * kinv * phi)
q2 = sp.simplify(Lphi.coeff(sp.Derivative(phi, (t, 2))))
q1 = sp.simplify(Lphi.coeff(sp.Derivative(phi, t)))
q0 = sp.simplify(Lphi.subs(sp.Derivative(phi, (t, 2)), 0).subs(sp.Derivative(phi, t), 0).subs(phi, 1))
# q2 phi'' + q1 phi' = q2 m (phi'/m)',  m = exp(-int q1/q2)
mlog = sp.simplify(sp.integrate(sp.simplify(-q1 / q2), t))
m = sp.simplify(sp.exp(mlog))
nz = sum(sp.simplify(ratio[i])**2 for i in range(3))  # sum dz_i^2 = nz * dz1^2
c2 = sp.simplify(nz * (q2 * m)**2)                      # sum dz^2 = c2 * (psi')^2
w = sp.simplify(W0 * c2 / 4)

res = dict(p2=str(p2), p1=str(p1), p0=str(p0), ratios=[str(r) for r in ratio], ds=str(ds),
           kernel_residual=str(ker1), q0=str(q0), q2=str(q2), q1=str(q1), m=str(m),
           sum_dz2_over_dz1sq=str(nz), w=str(w))
print(json.dumps(res, indent=1))

# numerics: M(t) = int_t^inf m, G(T) = int_T^inf M^2/w
mp.mp.dps = 30
mf = sp.lambdify(t, m, 'mpmath'); wf = sp.lambdify(t, w, 'mpmath')
Mf = lambda tt: mp.quad(mf, [tt, tt + 5, mp.inf])
asym_m = sp.limit(m * sp.exp(4 * t), t, sp.oo) if True else None
asym_w = sp.limit(w * sp.exp(-4 * t), t, sp.oo)
rows = []
for T in [0.5, 1, 2, 3, 4, 6, 8]:
    G = mp.quad(lambda tt: Mf(tt)**2 / wf(tt), [T, T + 3, T + 10, mp.inf])
    rows.append(dict(T=T, G=float(G), Qmin_per_C2=float(1 / G), Qmin_e4T=float(1 / G / mp.e**(4 * T))))
    print(rows[-1])
res.update(asym_m_e4t=str(asym_m), asym_w_em4t=str(asym_w), table=rows)
(ROOT / 'data').mkdir(exist_ok=True)
(ROOT / 'data' / 'squash_escape_cost.json').write_text(json.dumps(res, indent=1) + '\n')
