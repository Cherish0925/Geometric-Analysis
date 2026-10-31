"""Exact algebra supporting the integral monopole gap in round4_rigidity.md.

The script checks branch inequalities by polynomial certificates and checks
the moment, spectral, and scaling calculations. It is not a numerical
solution of the Seiberg--Witten equations or a proof of monopole existence.
"""

import sympy as sp

R = sp.Rational

# On the clipping branch q<3 one has e=s+4>1, and Q^2-q_+^2<=9.
h = sp.symbols("h", nonnegative=True)
assert sp.expand(9*(1+h)**2-9) == 9*h**2+18*h

# On the cap branch x=(-s)_+>4 sqrt(3)>6, x<=3(x-4).
x = 6+h
assert sp.expand(9*(x-4)**2-x**2) == 8*h**2+24*h
assert (4*sp.sqrt(3)) > 6
assert 6**2 * R(9, 16) == R(81, 4)
assert 9 + R(81, 4) == R(117, 4)

# Hessian absorption with Ricci and bundle curvature both in L2.
H, K, rcurv, fcurv = sp.symbols("H K rcurv fcurv", nonnegative=True)
assert sp.expand(H**2/2+8*K**2*(rcurv+fcurv)**2
                 -4*K*(rcurv+fcurv)*H
                 -(H-4*K*(rcurv+fcurv))**2/2) == 0
assert sp.expand(16*(rcurv**2+fcurv**2)-8*(rcurv+fcurv)**2
                 -8*(rcurv-fcurv)**2) == 0
assert 2*16 == 32 and 2*(16+R(1, 2)) == 33

# Ideal moment factorization: v=Z^(1/3), a=E_Q^(1/3).
a, v, C = sp.symbols("a v C", positive=True)
P, holder = C-v**3, a*v**2-C
rhs = holder+a*(a+v)/v**2*(P+holder)
assert sp.simplify(rhs-(a**3-C)) == 0

# Coefficients for amplitude and the bounded polynomial Weyl model.
assert 2*R(4, 9)*R(1, 12) == R(2, 27)
assert (4+sp.sqrt(2))**2 < 36
assert R(16, 27)*2 + R(3, 2)*R(8, 27) == R(44, 27)
assert 2+2*4096 == 8194
assert R(3, 2)*R(2, 27) == R(1, 9)
ricci_coefficient = R(44, 27)*117+R(8, 9)
orbit_coefficient = 8194+R(12, 9)
assert R(44, 27) < 2
assert ricci_coefficient < 8500 and orbit_coefficient < 8500

# Calibrated-orbit distance formula and unrestricted signed-G identity.
alpha, z, scalar, t, e = sp.symbols("alpha z scalar t e", real=True)
w = -alpha+z
dist2 = R(3, 2)*alpha**2+R(1, 24)+w/2
assert sp.expand(dist2-(R(3, 2)*(alpha-R(1, 6))**2+z/2)) == 0
fscalar = R(2, 3)*scalar-2*alpha
assert sp.expand((scalar+24*alpha)**2+18*fscalar**2
                 -216*(scalar**2/24+3*alpha**2)) == 0
assert sp.expand(27*(scalar**2/24+3*alpha**2)
                 -(-scalar+3*alpha)**2-(scalar+24*alpha)**2/8) == 0

# On s>-3, e>1, z<=alpha. This is an exact sum of nonnegative terms
# proving F <= (t^2+5e^2)/64 on that branch.
F_upper_using_z = (t-e)**2/384+(t-e+4)/48
claimed_bound = (t**2+5*e**2)/64
certificate = ((t+e)**2/384+(t-1)**2/96
               +(e-1)*(3*e+4)/48+(e**2-1)/96)
assert sp.expand(claimed_bound-F_upper_using_z-certificate) == 0

# General family budget, with Q=P+Z/4.
P_r, Z_s = sp.symbols("P_r Z_s", nonnegative=True)
Q_r = P_r+Z_s/4
assert sp.expand(109*Q_r-(Q_r+Z_s+108*P_r)) == 26*Z_s
assert 109+R(27, 2) == R(245, 2)
assert 864+108 == 972
assert 972*R(5, 4) == 1215
assert R(245, 2) < 1215
assert sp.expand(2*e**2+32-(e-4)**2-(e+4)**2) == 0

# T>0 for normalized Ricci error r<=1/4; x=sqrt(r)<=1/2.
x = sp.symbols("x", nonnegative=True)
lower = (4-2*x)**2/24-x**2/2
assert sp.expand(lower-R(1, 4)-(R(1, 2)-x)*(4*x+10)/12) == 0

# Exact optimization over Einstein scale, assuming total scalar S<0.
lam, R2, volume = sp.symbols("lam R2 volume", positive=True)
S = sp.symbols("S", negative=True)
energy = R2/(lam**2*volume)+2*S/(lam*volume)+4
assert sp.simplify(sp.diff(energy, lam).subs(lam, -R2/S)) == 0
assert sp.simplify(energy.subs(lam, -R2/S)-(4-S**2/(R2*volume))) == 0
scalar_energy, traceless_energy = sp.symbols("scalar_energy traceless_energy")
assert sp.simplify((4*R2-S**2/volume).subs(R2, traceless_energy+scalar_energy/4)
                   -(4*traceless_energy+scalar_energy-S**2/volume)) == 0

print("Exact round-four rigidity checks passed.")
print("Truncation scalar cost:", R(117, 4))
print("Residual bound coefficients before rounding:", R(44, 27),
      ricci_coefficient, orbit_coefficient)
print("Integral-family coefficient:", 1215)
print("Optimal negative Einstein scale: lambda=-R2/S")
