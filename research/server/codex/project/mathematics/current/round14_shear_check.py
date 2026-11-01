#!/usr/bin/env python3
"""Exact local Ricci, harmonic-stress, and finite-capacity checks.

No old project checker is imported. Numerical quadrature checks constants,
not a continuous curvature supremum or a closed Einstein theorem.
"""
import sympy as s
import mpmath as mp

t, ph, x, y = s.symbols('t ph x y', real=True)
coords = (t, ph, x, y)
a, z = s.Function('a')(t), s.Function('z')(t)
g = s.Matrix([
    [1, 0, 0, 0],
    [0, a*a, a*a*z, 0],
    [0, a*a*z, a*a*z*z + 1/(3*y*y), 0],
    [0, 0, 0, 1/(3*y*y)],
])
gi = s.simplify(g.inv())
Gamma = [[[s.simplify(sum(
    gi[i, m] * (s.diff(g[m, j], coords[k])
                + s.diff(g[m, k], coords[j])
                - s.diff(g[j, k], coords[m])) / 2
    for m in range(4))) for k in range(4)] for j in range(4)]
    for i in range(4)]
ric = s.zeros(4)
for i in range(4):
    for j in range(i, 4):
        val = sum(s.diff(Gamma[k][i][j], coords[k])
                  - s.diff(Gamma[k][i][k], coords[j])
                  for k in range(4))
        val += sum(Gamma[k][i][j]*Gamma[m][k][m]
                   - Gamma[m][i][k]*Gamma[k][j][m]
                   for k in range(4) for m in range(4))
        ric[i, j] = ric[j, i] = s.simplify(val)

T = s.Matrix([1, 0, 0, 0])
U = s.Matrix([0, 1/a, 0, 0])
X = s.Matrix([0, -z, 1, 0])
Y = s.Matrix([0, 0, 0, 1])
residual = ric + 3*g
sub = {s.diff(a, t, 2): 3*a}
expected = [
    (T, T, -s.Rational(3, 2)*a*a*s.diff(z,t)**2*y*y),
    (U, U, s.Rational(3, 2)*a*a*s.diff(z,t)**2*y*y),
    (X, X, -s.Rational(1, 2)*a*a*s.diff(z,t)**2),
    (Y, Y, 0),
    (X, U, -a*(s.diff(z,t,2)+3*s.diff(a,t)*s.diff(z,t)/a)/2),
    (T, X, 0), (T, U, 0), (T, Y, 0), (X, Y, 0), (Y, U, 0),
]
for v, w, target in expected:
    assert s.simplify(((v.T*residual*w)[0]-target).subs(sub)) == 0
print('PASS: 10 Ricci blocks derived independently from Christoffel symbols')

# Harmonic one-form jet in normal surface coordinates.
p, q, A, B = s.symbols('p q A B', real=True)
stress = s.Matrix([[(p*p-q*q)/2, p*q], [p*q, (q*q-p*p)/2]])
dx = lambda expr: s.diff(expr,p)*A + s.diff(expr,q)*B
dy = lambda expr: s.diff(expr,p)*B - s.diff(expr,q)*A
assert s.simplify(dx(stress[0,0])+dy(stress[1,0])) == 0
assert s.simplify(dx(stress[0,1])+dy(stress[1,1])) == 0
assert s.simplify(s.trace(stress)) == 0
assert s.simplify(s.trace(stress*stress)-(p*p+q*q)**2/2) == 0
star_stress = stress.subs({p:-q,q:p}, simultaneous=True)
assert s.simplify(star_stress+stress) == s.zeros(2)
print('PASS: harmonic stress is TT, has norm |beta|^4/2, and star reverses it')

# Hodge energy variation at an L2 minimizer; harmonic-representative
# derivative is exact, so its integral contribution is zero analytically.
tau = s.symbols('tau', real=True)
metric_var = s.eye(2)+tau*stress
beta = s.Matrix([p,q])
energy_density = (beta.T*metric_var.inv()*beta)[0]*s.sqrt(metric_var.det())
assert s.simplify(s.diff(energy_density,tau).subs(tau,0)
                  +(p*p+q*q)**2/2) == 0
print('PASS: Hodge-energy metric variation along its harmonic stress is negative')

mp.mp.dps = 60
k = mp.sqrt(3)
for R in (mp.mpf('0.4'), mp.mpf('1.7'), mp.mpf('5')):
    jm = lambda m: mp.quad(lambda v: mp.sech(k*v)**m, [-R,0,R])
    j1,j3,j5 = (jm(m) for m in (1,3,5))
    primitive = lambda v: (mp.sech(k*v)*mp.tanh(k*v)
                            +mp.atan(mp.sinh(k*v)))/(2*k)
    zz = lambda v: mp.mpf('.5')+primitive(v)/j3
    zp = lambda v: mp.sech(k*v)**3/j3
    capacity = mp.quad(lambda v: mp.cosh(k*v)**3*zp(v)**2, [-R,0,R])
    force = mp.quad(lambda v: mp.cosh(k*v)*zp(v)**2, [-R,0,R])
    assert abs(capacity-1/j3) < mp.mpf('1e-50')
    assert abs(force-j5/j3**2) < mp.mpf('1e-50')
    assert force >= 1/j1
    # v'/c^2=(1/2-z)sech/J3. Its endpoint value integrates to zero.
    vvprime = lambda v: (mp.mpf('.5')-zz(v))*mp.sech(k*v)/j3
    assert abs(mp.quad(vvprime,[-R,0,R])) < mp.mpf('1e-50')
    for v in (-R/2, mp.mpf('0'), R/3):
        # Normalized Maxwell equation and TT backreaction equation.
        assert abs(mp.diff(lambda r: mp.cosh(k*r)**3*zp(r),v)) < mp.mpf('1e-50')
        assert abs(mp.diff(lambda r: mp.cosh(k*r)*vvprime(r),v)
                   +mp.cosh(k*v)**3*zp(v)**2) < mp.mpf('1e-50')
    # Wrong weight: receiver-minimizing profile fails the Maxwell equation.
    wrong_flux_derivative = mp.diff(lambda r: mp.cosh(k*r)**2/j1,R/3)
    assert abs(wrong_flux_derivative) > mp.mpf('0.01')
print('PASS: finite-interval capacity, receiver, TT response, and wrong-weight rejection')

j3inf = mp.pi/(2*k)
j5inf = 3*mp.pi/(8*k)
assert abs(2*mp.pi*j5inf/j3inf**2-3*k) < mp.mpf('1e-50')
# Evaluate the exact compact integral after u=atan(sinh(k*t)).
peak = (2/mp.pi**2)*mp.quad(lambda u: -mp.cos(u)*mp.sin(u)-u,
                           [-mp.pi/2,0])
assert abs(peak-(mp.mpf('0.25')+1/mp.pi**2)) < mp.mpf('1e-50')
print('PASS: complete-throat force 3*sqrt(3) and TT peak 1/4+1/pi^2')
