"""Finite checks for the actual Yamabe endpoint example and estimates.

The checks do not replace the Yamabe theorem, semigroup estimates, implicit
function theorem, or the global smooth bump estimates in the manuscript.
"""

import sympy as sp


def zero(value, label):
    assert sp.simplify(sp.expand(value)) == 0, (label, value)
    print(f"PASS: {label}")


x, y = sp.symbols("x y", real=True)
b, L = sp.symbols("b L", positive=True)
r2 = x*x+y*y
bump = x*y*sp.log(r2+b)
lap_eucl = sp.diff(bump,x,2)+sp.diff(bump,y,2)
zero(lap_eucl-4*x*y*(2*r2+3*b)/(r2+b)**2,
     "exact logarithmic bump Laplacian")
zero(4*(r2+b)**2-2*r2*(2*r2+3*b)-(2*r2*b+4*b*b),
     "pointwise Laplacian bound numerator")
scaled = -bump/(2*L)
hessian = sp.hessian(scaled,(x,y)).subs({x:0,y:0,b:sp.exp(-2*L)})
assert sp.simplify(hessian) == sp.Matrix([[0,1],[1,0]])
print("PASS: amplitude-one bump has exact trace-free Hessian at its center")
grown = sp.simplify(sp.log(L)*hessian)
assert grown == sp.log(L)*sp.Matrix([[0,1],[1,0]])
print("PASS: logarithmically amplified bump has the asserted central Hessian")

v = sp.Function("v")(x,y)
w = sp.Function("w")(x,y)
delta = lambda f: -sp.diff(f,x,2)-sp.diff(f,y,2)
u = sp.exp(-v/3)*w
original = 6*delta(u)+(2*delta(v)-2-2*sp.exp(2*v))*u+4*sp.exp(2*v)*u**3
dv2 = sp.diff(v,x)**2+sp.diff(v,y)**2
dvdw = sp.diff(v,x)*sp.diff(w,x)+sp.diff(v,y)*sp.diff(w,y)
transformed = 6*delta(w)+4*dvdw+(-sp.Rational(2,3)*dv2-2-2*sp.exp(2*v))*w+4*sp.exp(sp.Rational(4,3)*v)*w**3
zero(sp.expand(original*sp.exp(v/3)-transformed),
     "gauge cancellation in full scalar-normalization equation")

t = sp.symbols("t", real=True)
h = sp.Function("h")(x,y)
linear = sp.diff(6*delta(1+t*h)-4*(1+t*h)+4*(1+t*h)**3,t).subs(t,0)
zero(linear-(6*delta(h)+8*h), "implicit-function linearization")

H = sp.zeros(4)
H[0,1]=H[1,0]=1
assert H.eigenvals() == {-1:1,1:1,0:2}
assert sp.trace(H)==0
print("PASS: limiting Hessian has operator norm one and zero trace")
w0 = sp.symbols("w0", positive=True)
assert sp.simplify(-2/w0*(-w0*sp.log(L)*H/3)) == 2*sp.log(L)*H/3
print("PASS: conformal coefficient cancels exactly at the unbounded endpoint")

v0, e = sp.symbols("v0 e", real=True)
zero(4*(1+v0)*((1+v0)**2-1)-(8*v0+12*v0**2+4*v0**3),
     "positive-mass scalar equation expansion")
zero((10*sp.Rational(3,16)+sp.Rational(9,8))/6-sp.Rational(1,2),
     "Laplacian L2 coefficient")
zero(sp.Rational(1,4)+sp.Rational(5,4)*sp.Rational(9,256)-sp.Rational(301,1024),
     "Bochner Hessian coefficient")
zero(sp.Rational(3,8)-(2*sp.Rational(9,256)+sp.Rational(301,1024))-sp.Rational(11,1024),
     "combined W2,2 coefficient has positive slack")
assert sp.Rational(27,32)+sp.Rational(9,8) == sp.Rational(63,32) < 2
assert sp.Rational(22,7) < sp.Rational(27,8)
print("PASS: elementary upper bound for heat-resolvent constant")

alpha = sp.symbols("alpha", positive=True)
# L>e, so the factors here are positive and powers can be combined.
rate = sp.powdenest((sp.log(L)/L)**(1-alpha)*sp.log(L)**alpha, force=True)
assert sp.simplify(sp.expand_power_base(rate,force=True)/
                   (sp.log(L)*L**(alpha-1))) == 1
print("PASS: interpolated Holder rate is log(L) times L^(alpha-1)")

print("All 14 finite checks passed; the analytic proof remains separate.")
