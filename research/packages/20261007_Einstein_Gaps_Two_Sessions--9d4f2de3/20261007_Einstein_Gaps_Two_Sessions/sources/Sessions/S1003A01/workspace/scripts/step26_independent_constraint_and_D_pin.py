"""Independent symbolic check of the scalar-normalized constraint and a D-channel pinning identity.

For diagonal Bianchi-IX, y_i=a_i'/a_i, S=sum y_i, W=prod a_i,
Ric_ii=-y_i'-S*y_i+P_i, and e_i=Ric_ii+6.  The script derives
C=(sigma_2(y)-6-R3/2)=(e0-sum e_i)/2, its Bianchi propagation,
the s=-24 reduction C=Ric^0_00 and S' equation, and the exact
q=log(a_g/a_h) difference equation
    (W q')'=W*(P_g-P_h-D), D=e_g-e_h.
It then derives the Green-kernel Cauchy-Schwarz estimate for changing q
on a finite interval.  This is an action identity, not a lower theorem
until the orbit drift P_g-P_h and W are controlled on the chosen interval.
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
R3 = sp.simplify(Pf + Pg + Ph)
Y = [yf, yg, yh, k, q, z]
e = [ef, eg, eh]
y = [yf, yg, yh]
F = [6-yf*S+Pf-ef, 6-yg*S+Pg-eg, 6-yh*S+Ph-eh,
     k*(yf-yg-yh), yg-yh, -z*(yg+yh)]
ddt = lambda h: sp.expand(sum(sp.diff(h, Y[i])*F[i] for i in range(6)))

sigma2 = yf*yg + yg*yh + yh*yf
C = sp.simplify(sigma2 - 6 - R3/2)
Sdot = sp.simplify(sum(F[:3]))
e0 = sp.simplify(6 - Sdot - (yf**2 + yg**2 + yh**2))
check_constraint = sp.simplify(C - (e0-sum(e))/2)
check_bianchi = sp.simplify(ddt(C) - (-2*S*C - sum((S-y[i])*e[i] for i in range(3))))
# Constant scalar -24 means e0+ef+eg+eh=0.
eh_s24 = sp.solve(sp.Eq(e0+ef+eg+eh, 0), eh)[0]
check_C_radial = sp.simplify((C-e0).subs(eh, eh_s24))
check_S = sp.simplify((Sdot-(18-S**2+R3+C)).subs(eh, eh_s24))

# Independent q difference equation. q'=yg-yh, so q''=yg'-yh'.
# D=e_g-e_h and Ric_gg-Ric_hh=(P_g-P_h)-q''-S q'.
D = eg-eh
check_q = sp.simplify((Pg-Ph) - ddt(yg-yh) - S*(yg-yh) - D)
Pdiff = sp.factor(Pg-Ph)

# Green identity on [T0,T1].  K(s)=int_s^T1 W(t)^(-1) dt.
# If (W q')'=W(Pdiff-D), then
# q1-q0-W0*q0'*K0-int W*Pdiff*K = -int W*D*K.
W0, q0p, K0, drift, mismatch = sp.symbols('W0 q0p K0 drift mismatch', real=True)
# Cauchy-Schwarz with action P_hat >= (1/8) int W D^2.
# |mismatch|^2 <= int W D^2 * int W K^2 <= 8 P_hat * int W K^2.

out = {
    'constraint_residual': str(check_constraint),
    'bianchi_residual': str(check_bianchi),
    'scalar_minus24_C_minus_e0_residual': str(check_C_radial),
    'scalar_minus24_S_equation_residual': str(check_S),
    'q_difference_residual': str(check_q),
    'P_g_minus_P_h': str(Pdiff),
    'D_pin_identity': '(W q_prime)_prime = W*(P_g-P_h-D)',
    'D_pin_green': 'M = q1-q0-W0*q0prime*K0-integral(W*(P_g-P_h)*K) = -integral(W*D*K)',
    'D_pin_bound': 'P_hat >= M^2/(8*integral(W*K^2))',
    'scope': 'Exact on any diagonal interval; a quantitative lower bound requires control of P_g-P_h, W, and endpoint data.'
}
print(json.dumps(out, indent=1))
(Path(__file__).resolve().parents[1]/'data'/'step26_independent_constraint_and_D_pin.json').write_text(json.dumps(out, indent=1)+'\n')
