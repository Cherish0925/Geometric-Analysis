"""Exact identities for q4_finite_energy_boundary.md; no numerical fitting."""
import sympy as s

t, x = s.symbols('t x', positive=True)
D = 1 + 3*x**2
tx = (1-x**2)/D
volume_x = 64*x*D/(3*(1-x**2)**3)
q_x = 36*(1-x**2)**3/D**3
assert s.factor(q_x-36*tx**3) == 0
assert s.factor(volume_x/(-s.diff(tx,x)) - s.Rational(8,3)*tx**-3) == 0

inverse_G = (1-x*x)**2*(9*x*x-1)/(4*D)
K = (t-1)*(3*t-2)*(3*t+1)
assert s.factor(s.diff(tx,x)**2*inverse_G - (t*t*K).subs(t,tx)) == 0

u = s.symbols('u')
w_x = 96*(81*x**12-54*x**10+315*x**8-168*x**6+99*x**4-18*x**2+1)/D**6
w = 6+486*t**6-486*t**5+108*t**4-18*t**3
assert s.factor(w_x-w.subs(t,tx)) == 0

V = s.Rational(8,3)*t**-3
lap = lambda f: s.factor(s.diff(V*t*t*K*s.diff(f,t),t)/V)
assert lap(t*t) == 2*t**3*(27*t**2-24*t+1)
assert s.integrate(lap(t*t)*V,(t,0,s.Rational(2,3))) == -s.Rational(32,3)
assert s.integrate((w-6)*V,(t,0,s.Rational(2,3))) == -32
assert s.integrate((36*t**3)*V,(t,0,s.Rational(2,3))) == 64
assert s.integrate((36*t**3)**2*V,(t,0,s.Rational(2,3))) == s.Rational(512,3)

eps = s.symbols('eps', positive=True)
euler_bulk_per_orbit = s.integrate((w+6)*V,(t,eps,s.Rational(2,3)))
target = 16/eps**2 -68+48*eps-144*eps**2+432*eps**3-324*eps**4
assert s.factor(euler_bulk_per_orbit-target) == 0
print('All volume, gradient, curvature-defect, flux, and boundary identities pass.')
