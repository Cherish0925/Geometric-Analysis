#!/usr/bin/env python3
"""Exact checks for the rank-one circle reduction used in Step 12.

Conventions:
  g = q + ell^2 (dpsi + A)^2,  Z = ell F, z = *_q Z,
  u = d_q log ell, H = Hess_q(ell)/ell = nabla u + u tensor u.
For Ric_g = -g define the electric and magnetic Weyl matrices
  E = W(.,e4,.,e4)
    = I/3 - H + (|z|^2 I - z tensor z)/4,
  B = -1/2 [nabla z + 2 u tensor z - <u,z>I].
The Einstein mixed and Bianchi equations make the bracket symmetric and
trace-free.  Up to orientation, W^+ and W^- are E+B and E-B.

The script checks:
  * the static product H^2 x H^2 gives spectrum (-2/3,1/3,1/3),
    disproving any general 'static constant spectrum implies W=0' statement;
  * Taub-NUT-AdS satisfies the reduced vertical/mixed identities and one
    chiral Weyl block E +/- B vanishes identically, while the other agrees
    with the independently computed exact spectrum.
"""
import sympy as s

r, nu = s.symbols('r nu', positive=True)
V = (r-nu)/(r+nu) * (1 + (r-nu)*(r+3*nu)/3)
b2 = r**2-nu**2
ell = 2*nu*s.sqrt(V)

# Orthonormal radial variables on q=dr^2/V+b(r)^2 dOmega^2.
u = s.simplify(s.sqrt(V)*s.diff(s.log(ell), r))
z = s.simplify(-ell/b2)  # z=*_q(ell F), radial component
Hrad = s.simplify(s.diff(V, r, 2)/2)
Hang = s.simplify(r*s.diff(V, r)/(2*b2))

# P=|z|^2 I-z*z is diag(0,z^2,z^2).
Erad = s.simplify(s.Rational(1,3)-Hrad)
Eang = s.simplify(s.Rational(1,3)-Hang+z**2/4)

# Covariant derivative of radial z on q in proper radial coordinate t.
z_t = s.simplify(s.sqrt(V)*s.diff(z, r))
b_over = s.simplify(s.sqrt(V)*r/b2)
Crad = s.simplify(z_t + u*z)
Cang = s.simplify(b_over*z - u*z)
Brad = s.simplify(-Crad/2)
Bang = s.simplify(-Cang/2)

# Vertical equation tr H = 1 + |z|^2/2 (raw |Z_ab|^2=2|z|^2).
vertical_residual = s.factor(Hrad+2*Hang-1-z**2/2)
# Mixed/Bianchi equations imply C trace zero.
magnetic_trace = s.factor(Crad+2*Cang)

Wp = [s.factor(Erad+Brad), s.factor(Eang+Bang), s.factor(Eang+Bang)]
Wm = [s.factor(Erad-Brad), s.factor(Eang-Bang), s.factor(Eang-Bang)]
known_simple = s.factor(-4*nu*(4*nu**2-3)/(3*(r+nu)**3))
known_double = s.factor(2*nu*(4*nu**2-3)/(3*(r+nu)**3))

print('V =', s.factor(V))
print('u =', s.factor(u))
print('z =', s.factor(z))
print('vertical residual =', vertical_residual)
print('magnetic trace residual =', magnetic_trace)
print('E =', [s.factor(Erad), s.factor(Eang), s.factor(Eang)])
print('B =', [s.factor(Brad), s.factor(Bang), s.factor(Bang)])
print('E+B =', Wp)
print('E-B =', Wm)
print('known nonzero spectrum (simple,double,double) =',
      [known_simple, known_double, known_double])

plus_zero = all(s.simplify(x) == 0 for x in Wp)
minus_zero = all(s.simplify(x) == 0 for x in Wm)
minus_match = (s.simplify(Wm[0]-known_simple)==0 and
               s.simplify(Wm[1]-known_double)==0)
plus_match = (s.simplify(Wp[0]-known_simple)==0 and
              s.simplify(Wp[1]-known_double)==0)
print('E+B zero:', plus_zero)
print('E-B zero:', minus_zero)
print('E-B matches known:', minus_match)
print('E+B matches known:', plus_match)

# Static product H^2 x H^2: choose the circle in the first H^2.
H_product = [s.Integer(1), s.Integer(0), s.Integer(0)]
W_product = [s.Rational(1,3)-x for x in H_product]
print('H2xH2 static H spectrum =', H_product)
print('H2xH2 W+ spectrum =', W_product)
assert sorted(W_product) == sorted([s.Rational(-2,3), s.Rational(1,3), s.Rational(1,3)])
assert vertical_residual == 0
assert magnetic_trace == 0
assert plus_zero or minus_zero
assert plus_match or minus_match
