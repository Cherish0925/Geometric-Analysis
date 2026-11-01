"""Exact finite checks for the compactified pencil, not a PDE verifier."""
import sympy as s

t, z, R, P, T, p, S, W = s.symbols('t z R P T p S W', real=True)
pi = s.pi
k = (1+t)*(8*t-1)/2
ell = 2*(1+t)*(1-2*t)
pt = t*(1+t)*S + 6*(1+t)*W - 72*pi**2*t*p
cw = pt.subs({S: 4*(R-P), W: 2*pi**2*T-R/12+P/3})
assert s.expand(cw-(k*R+ell*P+12*pi**2*(1+t)*T-72*pi**2*t*p)) == 0
print('PASS compactified Chern--Weil reduction')

h = (1-z*z)/3
lo = (4-z)**2/9
hi = (4+z)**2/9
tl = (1+2*z)/(8-2*z)
tu = (1-2*z)/(8+2*z)
for tr, er in ((tl, lo), (tu, hi)):
    v = k.subs(t,tr)*er+s.Rational(3,2)*(1+tr)*(1-h)-9*tr
    assert s.factor(v) == 0
print('PASS both opposite-sign energy-envelope roots')

beta = s.symbols('beta', positive=True)
weight = t*t*(1-2*t)**2
assert s.factor(weight.subs(t,1/beta)-(beta-2)**2/beta**4) == 0
assert s.factor(s.diff(weight,t)) == 2*t*(2*t-1)*(4*t-1)
assert weight.subs(t,s.Rational(1,4)) == s.Rational(1,64)
print('PASS cutoff-independent compatibility weight')

rho = tu**3*(1-2*tu)**2
assert s.limit(rho/(h-s.Rational(1,4))**3,z,s.Rational(1,2),dir='-') == s.Rational(8,27)
assert s.factor(hi-lo) == 16*z/9
print('PASS distinct endpoint degeneration and interval width')

assert lo.subs(z,s.Rational(1,4)) == s.Rational(25,16)
assert hi.subs(z,s.Rational(1,4)) == s.Rational(289,144)
assert tu.subs(z,s.Rational(1,4)) == s.Rational(1,17)
assert rho.subs(z,s.Rational(1,4)) == s.Rational(225,17**5)
assert s.Rational(33,16) > s.Rational(289,144)
print('PASS realized product-surface blow-up energy window')

ke = pt.subs({S:16,W:s.Rational(2,3),p:1/(2*pi*pi)})
assert s.factor(ke-4*(1-2*t)**2) == 0
print('PASS actual negative KE normalization')

mutants = [
    k.subs(t,tu)*lo+s.Rational(3,2)*(1+tu)*(1-h)-9*tu,
    s.expand(cw-(-k*R+ell*P+12*pi**2*(1+t)*T-72*pi**2*t*p)),
    ke-4*(1+2*t)**2,
]
assert all(s.factor(v) != 0 for v in mutants)
print('PASS 3 deliberately incorrect sign/root variants rejected')
