"""Lemma N: in the scalar-(-24) normalization the H channel of Ric° is the
Hamiltonian-constraint residual, an algebraic function of the compact state.

Compact diagonal Bianchi-IX variables (as in ach_projected.py / beta_pinning_identity.py):
  y_i = a_i'/a_i (i=f,g,h), kappa=a_f/(a_g a_h), zeta=z=1/(a_g a_h), q=log(a_g/a_h),
  y_i' = 6 - y_i S + P_i - e_i,  e_i = Ric_ii + 6,  S = y_f+y_g+y_h,
  P_i = orbit Ricci components, R3 = P_f+P_g+P_h.
Radial component: Ric_00 = -sum(y_i'+y_i^2), e_0 = Ric_00+6.

Checks (exact, sympy):
 (1) C := sigma_2(y) - 6 - R3/2 equals (e_0 - sum e_i)/2   [constraint = G_00 - 6]
 (2) Bianchi: C' = -2 S C - sum_i (S - y_i) e_i along the controlled flow
     (with e_0 eliminated through (1)); i.e. the constraint is propagated by Ric only.
 (3) With s=-24 (e_0 + sum e_i = 0): C = Ric°_00, hence H = -4C/3 and the H-part
     of P_hat = int W |Ric°|^2/4 dt equals int W C^2/3 dt.
 (4) S' = 18 - S^2 + R3 + C   (s=-24).
Output: workspace/data/scalar_normalized_constraint.json
"""
import json
from pathlib import Path
import sympy as sp

yf, yg, yh, k, q, z = sp.symbols('yf yg yh k q z', real=True)
ef, eg, eh = sp.symbols('ef eg eh', real=True)
S = yf + yg + yh
Pf = 2*k**2 - 8*z**2*sp.sinh(q)**2/k**2
Pg = -2*k**2 + 4*z*sp.exp(-q) + 4*z**2*sp.sinh(2*q)/k**2
Ph = -2*k**2 + 4*z*sp.exp(q) - 4*z**2*sp.sinh(2*q)/k**2
R3 = Pf + Pg + Ph
Y = [yf, yg, yh, k, q, z]
e = [ef, eg, eh]
y = [yf, yg, yh]
F = [6 - yf*S + Pf - ef, 6 - yg*S + Pg - eg, 6 - yh*S + Ph - eh,
     k*(yf - yg - yh), yg - yh, -z*(yg + yh)]
ddt = lambda expr: sum(sp.diff(expr, Y[i])*F[i] for i in range(6))

sigma2 = yf*yg + yg*yh + yh*yf
C = sigma2 - 6 - R3/2
# (1)
Sdot = sum(F[:3])
e0 = 6 - Sdot - (yf**2 + yg**2 + yh**2)
chk1 = sp.simplify(C - (e0 - sum(e))/2)
# (2)
chk2 = sp.simplify(sp.expand(ddt(C) - (-2*S*C - sum((S - y[i])*e[i] for i in range(3)))))
# (3) and (4) at s = -24: sum of all e's vanishes -> e0 = -sum e
# Ric°_00 = Ric_00 - s/4 = Ric_00 + 6 = e0
s24 = {eh: -ef - eg - e0}  # impose e0 + ef + eg + eh = 0 implicitly
chk3 = sp.simplify((C - e0).subs(eh, sp.solve(sp.Eq(e0 + ef + eg + eh, 0), eh)[0]))
chk4 = sp.simplify((Sdot - (18 - S**2 + R3 + C)).subs(eh, sp.solve(sp.Eq(e0 + ef + eg + eh, 0), eh)[0]))
# Norm check: with Ric°=(e0, ef, eg, eh) traceless, H defined by Ric°_00=-3H/4,
# E=ef-(eg+eh)/2, D=eg-eh : |Ric°|^2 = 3H^2/4 + 2E^2/3 + D^2/2.
a, b, c = sp.symbols('a b c', real=True)
r0 = -(a + b + c)
H = -4*r0/3
E = a - (b + c)/2
D = b - c
chk5 = sp.simplify(r0**2 + a**2 + b**2 + c**2 - (3*H**2/4 + 2*E**2/3 + D**2/2))
# CH: k=coth t, z=csch^2 t, q=0, y=(coth+tanh, coth, coth): C must vanish
t = sp.symbols('t', positive=True)
chsub = {yf: sp.coth(t) + sp.tanh(t), yg: sp.coth(t), yh: sp.coth(t), k: sp.coth(t), q: 0, z: sp.csch(t)**2}
chk6 = sp.simplify(C.subs(chsub).rewrite(sp.exp))
out = {
    'C': str(C), 'R3': str(sp.simplify(R3)),
    'check1_C_equals_(e0-sum e)/2': str(chk1),
    'check2_bianchi_residual': str(chk2),
    'check3_C_equals_Ric0_00_at_s-24': str(chk3),
    'check4_S_riccati_residual': str(chk4),
    'check5_norm_decomposition': str(chk5),
    'check6_C_on_CH': str(chk6),
    'consequence': 'P_hat >= int W C^2/3 dt in the s=-24 class; S\' = 18 - S^2 + R3 + C',
}
print(json.dumps(out, indent=1))
(Path(__file__).resolve().parents[1]/'data'/'scalar_normalized_constraint.json').write_text(json.dumps(out, indent=1) + '\n')
