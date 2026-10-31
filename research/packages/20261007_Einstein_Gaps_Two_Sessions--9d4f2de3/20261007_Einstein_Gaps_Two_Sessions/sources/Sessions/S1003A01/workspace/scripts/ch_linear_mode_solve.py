"""Solve the linearized Einstein equations of ch_linear_einstein_modes.py.

Antisymmetric sector: verify the two-parameter family
   theta = k^{-1} [ C + (c/2) int_0^x f_-^2 ],   k=(x/(1+x))^2, f_-=x/(1+x)^{5/2}
gives dz=0 (and ds=0 identically).  The decaying member (c-mode, normalised to theta->0)
is the 'mass' mode  v_- = c f_-,  theta = -c (6Y^2-8Y+3)/(24 x^2 Y^2), Y=1+x.

Symmetric (U(2)) sector: indicial exponents at infinity of dz=ds=0 with sigma=e^{-qt},
beta=kappa e^{-qt}, and exact rational solutions found by ansatz.
"""
import sympy as sp
from ch_linear_einstein_modes import curvature, lin, A, B, t, eps

x = sp.symbols('x', positive=True)
c, C = sp.symbols('c C')
Y = 1 + x
# int_0^x s^2/(1+s)^5 ds
s_ = sp.symbols('s', positive=True)
I0x = sp.integrate(s_**2/(1+s_)**5, (s_, 0, x))
k = (x/(1+x))**2
theta_x = (C + c/2*I0x)/k
# convert to t: x=sinh^2 t
theta_t = theta_x.subs(x, sp.sinh(t)**2)
uA, zA, sA = curvature([A*sp.exp(eps*theta_t/2), B, A*sp.exp(-eps*theta_t/2)])
dz1 = lin(zA[0])
res = sp.simplify(dz1.rewrite(sp.exp))
print('antisym dz1 residual for 2-param family:', res)
du = [lin(e) for e in uA]
vm = sp.simplify((du[0]-du[2]).subs(t, sp.asinh(sp.sqrt(x))))
print('v_- of family:', sp.simplify(vm), ' ;  expected c*x/(1+x)^(5/2)')
I0inf = sp.integrate(s_**2/(1+s_)**5, (s_, 0, sp.oo))
print('int_0^inf f_-^2 =', I0inf)
mass = sp.simplify(((-c/2*(I0inf - I0x))/k))
print('decaying mass-mode theta:', sp.factor(mass))
print('  as x->oo:', sp.series(mass, x, sp.oo, 3))

# ---------------- symmetric sector ----------------
q, kap = sp.symbols('q kappa')
sg = sp.Function('sigma')(t); bt = sp.Function('beta')(t)
uS, zS, sS = curvature([A*sp.exp(eps*sg), B*sp.exp(eps*bt), A*sp.exp(eps*sg)])
eqs = [lin(zS[0]), lin(zS[1]), lin(sS)]
# gauge mode check
gauge = {sg: sp.cosh(t)/sp.sinh(t), bt: sp.cosh(t)/sp.sinh(t) + sp.sinh(t)/sp.cosh(t)}
def sub(e, s1, b1):
    return sp.simplify(e.subs({sp.Derivative(sg, (t, 2)): sp.diff(s1, t, 2), sp.Derivative(bt, (t, 2)): sp.diff(b1, t, 2)})
                       .subs({sp.Derivative(sg, t): sp.diff(s1, t), sp.Derivative(bt, t): sp.diff(b1, t)})
                       .subs({sg: s1, bt: b1}))
print('gauge mode residuals:', [sub(e, gauge[sg], gauge[bt]) for e in eqs])

# rational ansatz in x for the symmetric sector: sigma, beta = P(x)/(x^m (1+x)^n)
xs = sp.symbols('xs', positive=True)
def to_t(expr):
    return expr.subs(xs, sp.sinh(t)**2)
sols = []
N = 4
a_ = sp.symbols('a0:%d' % (N+1)); b_ = sp.symbols('b0:%d' % (N+1))
for m, n in [(1, 1), (2, 1), (1, 2), (2, 2), (2, 3), (3, 2), (2, 4), (3, 3)]:
    s1 = sum(a_[i]*xs**i for i in range(N+1))/(xs**m*(1+xs)**n)
    b1 = sum(b_[i]*xs**i for i in range(N+1))/(xs**m*(1+xs)**n)
    S1, B1 = to_t(s1), to_t(b1)
    rs = []
    for e in eqs:
        r = sub(e, S1, B1)
        r = sp.simplify(r.subs(t, sp.asinh(sp.sqrt(xs))))
        num = sp.numer(sp.together(sp.expand(r)))
        rs += sp.Poly(sp.expand(num), xs).coeffs()
    sol = sp.solve(rs, list(a_)+list(b_), dict=True)
    if sol:
        for so in sol:
            ss = sp.factor(s1.subs(so)); bb = sp.factor(b1.subs(so))
            free = (ss.free_symbols | bb.free_symbols) - {xs}
            if free:
                sols.append((m, n, ss, bb))
                print('ansatz', m, n, ': sigma =', ss, ' beta =', bb)
