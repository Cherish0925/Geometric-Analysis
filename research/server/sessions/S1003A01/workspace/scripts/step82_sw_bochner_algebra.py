"""Step 82: algebraic integrands of the global constraints on a closed
negative almost-Kahler Einstein 4-manifold, in Step-62/79 norms.

Scale s=-1 (all statements are scale invariant).  Pointwise variables
  q = |nabla omega|^2,  e = |eta|^2,  v = tr V^2,  x = eta^T V eta,
  r = s/6 + q/4,  |W+|^2 = 3r^2/2 + 2e + v,
  det W+ = r^3/4 - r v/2 + r e/2 + x,   |x| <= e*sqrt(v/2).
Integral relations used (closed manifold):
  (S)  int Zs = 0,  Zs = |s|q/16 - e - v - 3q^2/32            (AAD/Sekigawa)
  (SW) int psi0 >= 72 pi^2 |c1^-|^2 >= 0,
        psi0 = (|s|+sqrt6|W+|)^2 - 9 s^2/4 + 36 (v + 3q^2/32)   (LeBrun Weyl
        estimate, b+>1, with 72pi^2 c1^2 = 9/4 (s^2 V - 16 T_AK))
  (B)  int Bo = int |nabla W+|^2,  Bo = -s/2 |W+|^2 + 18 det W+
  (Y)  32 int |Y|^2 = int[|s| q^2/2 + 8 q e - 8 q v - 3 q^3/4]  (multiplier q
        in div(dq-16X)=rho, the eps^-2 coefficient of (80.S))
  and |nabla W+|^2 >= 5|Y|^2.
The script prints linear parts, the common null direction and second-order
terms along it.
"""
import sympy as sp

q, e, v, x, lam, mu1, mu2 = sp.symbols('q e v x lam mu1 mu2', real=True)
s = -1
S = sp.Integer(1)  # |s|
r = sp.Rational(s, 6) + q/4
W2 = sp.Rational(3, 2)*r**2 + 2*e + v
det = r**3/4 - r*v/2 + r*e/2 + x
Zs = S*q/16 - e - v - sp.Rational(3, 32)*q**2
A = sp.sqrt(6*W2)
psi0 = (S + A)**2 - sp.Rational(9, 4) + 36*(v + sp.Rational(3, 32)*q**2)
Bo = -sp.Rational(s, 2)*W2 + 18*det
Ylow = sp.Rational(5, 32)*(S*q**2/2 + 8*q*e - 8*q*v - sp.Rational(3, 4)*q**3)
Bnet = sp.expand(Bo - Ylow)   # int Bnet >= 10 int|dv|^2 + 2 int|..|^2 >= 0

t = sp.symbols('t', positive=True)
def series_t(expr, subs, order=3):
    ex = expr.subs(subs)
    return sp.series(ex, t, 0, order).removeO()

print('Kahler values: psi0=', sp.simplify(psi0.subs({q: 0, e: 0, v: 0, x: 0})),
      ' Bo=', sp.simplify(Bo.subs({q: 0, e: 0, v: 0, x: 0})))
lin = {}
for name, f in [('Zs', Zs), ('psi0', psi0), ('Bo', Bo), ('Bnet', Bnet)]:
    g = [sp.simplify(sp.diff(f, z).subs({q: 0, e: 0, v: 0, x: 0})) for z in (q, e, v, x)]
    lin[name] = g
    print('linear part of', name, '(dq,de,dv,dx):', g)

# Null direction: v=0, x=0, e=q/16 kills Zs, psi0, Bo at linear order.
# Second order along e = q/16 + a q^2, v = b q^2, x = c q^2 (|c| <= sqrt(b/2)/16).
a, b, c = sp.symbols('a b c', real=True)
sub = {q: t, e: t/16 + a*t**2, v: b*t**2, x: c*t**2}
for name, f in [('Zs', Zs), ('psi0', psi0), ('Bo', Bo), ('Bnet', Bnet)]:
    print(name, 'along null direction:', sp.expand(series_t(f, sub)))
