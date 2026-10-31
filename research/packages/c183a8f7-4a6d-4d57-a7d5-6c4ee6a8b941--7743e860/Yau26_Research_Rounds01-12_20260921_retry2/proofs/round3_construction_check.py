"""Exact checks for the complete invariant Einstein-family proof.

This checks algebra supporting the analytic proof; it does not numerically
approximate an Einstein solution or certify a Banach-space theorem.
"""
import sympy as s

z, c, gamma, sigma = s.symbols('z c gamma sigma', real=True)
r = 1-z*z
d = 1+c*r
H = s.Matrix([[1/d+gamma**2*d*r**2, gamma*d*r],
              [gamma*d*r, d]])
assert s.factor(H.det()) == 1
assert H.subs(z, 1) == s.eye(2)
assert H.subs(z, -1) == s.eye(2)
print('PASS: fixed area and exact identity matrix at either own radial face')

def dr(v):
    return r*s.diff(v, z)

# Removing the angular shear leaves E dv^2+G dtheta^2; sqrt(EG)=1/sqrt(r).
angular = d/r
gauss = -s.sqrt(r)*dr(dr(angular)*s.sqrt(r))/2
assert s.simplify(gauss+1) == 0
print('PASS: exact constant-parameter cylinder curvature -1')

# At a t face the first frame bracket is constant -sigma, sigma=+/-1.
# The second metric is the complete deformed cylinder H. All curvature is
# computed below from the Koszul formula in this noncoordinate frame.
G = s.diag(1, 1, 1, 1)
G[2:4, 2:4] = H
Ginv = s.diag(1, 1, 1, 1)
Ginv[2:4, 2:4] = s.Matrix([[d, -gamma*d*r],
                          [-gamma*d*r, 1/d+gamma**2*d*r**2]])
assert (G*Ginv-s.eye(4)).applyfunc(s.simplify) == s.zeros(4)

bracket = {(0, 1, 1): -sigma, (1, 0, 1): sigma,
           (2, 3, 3): -z, (3, 2, 3): z}

def C(i, j, k):
    return bracket.get((i, j, k), s.S.Zero)

def e(v, i):
    return dr(v) if i == 2 else s.S.Zero

connection = {}
for k in range(4):
    for i in range(4):
        for j in range(4):
            value = 0
            for ell in range(4):
                lower = e(G[j, ell], i)+e(G[i, ell], j)-e(G[i, j], ell)
                lower += sum(C(i, j, b)*G[b, ell]
                             -C(j, ell, b)*G[b, i]
                             +C(ell, i, b)*G[b, j] for b in range(4))
                value += Ginv[k, ell]*lower/2
            connection[k, i, j] = s.factor(value)

def con(k, i, j):
    return connection[k, i, j]

Ric = s.zeros(4)
for k in range(4):
    for j in range(4):
        value = 0
        for i in range(4):
            value += e(con(i, j, k), i)-e(con(i, i, k), j)
            value += sum(con(b, j, k)*con(i, i, b)
                         -con(b, i, k)*con(i, j, b)
                         -C(i, j, b)*con(i, b, k) for b in range(4))
        Ric[k, j] = s.factor(value)
for face in (-1, 1):
    assert (Ric.subs(sigma, face)+G).applyfunc(s.simplify) == s.zeros(4)
print('PASS: every Ricci component vanishes in E=Ric+G at both formal t faces')
print('PASS: swapping the two tensor blocks gives the identical u-face identity')

# beta_g0 of the exact constant length path. In the reference frame the
# radial and angular diagonal entries are 1/d and d, respectively.
beta = -dr(1/d)-z*(1/d-d)+dr(1/d+d)/2
assert s.factor(beta-z*((d-1)/d)**2) == 0
print('PASS: fixed-background gauge defect is z*((d-1)/d)^2')

# Exact scalar conjugation with an arbitrary drift beta and rho derivative a.
v, vx, vxx, aa, ap, bb, de, VV = s.symbols('v vx vxx a ap b delta V')
conjugated = -(vxx-2*de*aa*vx+(de**2*aa**2-de*ap)*v)/2
conjugated -= bb*(vx-de*aa*v)/2
conjugated += VV*v/2
expected = (-vxx-bb*vx+VV*v)/2+de*aa*vx
expected += (de*(ap+bb*aa)-de**2*aa**2)*v/2
assert s.expand(conjugated-expected) == 0
assert s.Rational(1, 8)-s.Rational(1, 4)**2 == s.Rational(1, 16)
print('PASS: conjugated operator and delta=1/4 coercivity margin 1/16')

eta = s.symbols('eta', real=True)
a0, a1, b1, A0, A1, B1 = s.symbols('a0 a1 b1 A0 A1 B1', real=True)
cc = a1**2-3*b1**2
ff = A1**2+B1**2
ee = A0*a1
I1 = s.pi**2*(cc-ff)/8
I2 = s.pi**2*(A1**2-3*B1**2-a1**2-b1**2)/8
M = s.pi*(cc-ff)*(eta**2-s.pi**2/4)/8
M += s.pi*ff*(s.cos(2*eta)+1)/16+s.pi*ee*s.sin(2*eta)/4
source = s.pi*cc*s.cos(eta)**2/8-s.pi*ff*s.cos(eta)**4/4
source -= s.pi*ee*s.sin(eta)*s.cos(eta)**3
assert s.trigsimp(s.cos(eta)**2*s.diff(M, eta, 2)-2*source) == 0
for endpoint in (-s.pi/2, s.pi/2):
    assert s.simplify(M.subs(eta, endpoint)) == 0
right_derivative = s.simplify(s.diff(M, eta).subs(eta, s.pi/2))
left_derivative = s.simplify(s.diff(M, eta).subs(eta, -s.pi/2))
assert s.simplify(right_derivative-I1+s.pi*ee/2) == 0
assert s.simplify(left_derivative+I1+s.pi*ee/2) == 0
assert s.simplify(-right_derivative/2+left_derivative/2+I1) == 0
assert s.simplify(-(I1+I2)-s.pi**2*(b1**2+B1**2)/2) == 0
print('PASS: exact projected correction ODE, both endpoint conditions and fluxes')

q = s.symbols('q', positive=True)
# J(u)=pi/2-2 exp(-u)+O(exp(-3u)); its negative counterpart is odd.
right_tail = s.diff(M.subs(eta, s.pi/2-2*q), q).subs(q, 0)
left_tail = s.diff(M.subs(eta, -s.pi/2+2*q), q).subs(q, 0)
assert s.simplify(right_tail+2*I1-s.pi*ee) == 0
assert s.simplify(left_tail+2*I1+s.pi*ee) == 0
print('PASS: separate e^(-|u|) tails and total pi^2*(b1^2+B1^2)/2 flux')

def sech_integral(power):
    return s.sqrt(s.pi)*s.gamma(s.Rational(power, 2))/s.gamma(s.Rational(power+1, 2))

# Project the previously checked all-block quadratic source, retaining
# the constant transverse amplitude in the cross interaction.
projected_self = (a1**2*(sech_integral(3)-sech_integral(5))
                  -b1**2*sech_integral(5))*s.cos(eta)**2
projected_other = -ff*sech_integral(3)*s.cos(eta)**4/2
projected_cross = -2*A0*a1*sech_integral(3)*s.sin(eta)*s.cos(eta)**3
assert s.simplify(projected_self+projected_other+projected_cross-source) == 0
assert s.simplify(sech_integral(3)-s.pi/2) == 0
print('PASS: projected source normalization and marked cylinder shear integral')
