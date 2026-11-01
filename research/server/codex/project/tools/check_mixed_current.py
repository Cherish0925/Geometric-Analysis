#!/usr/bin/env python3
"""Finite algebra checks for mixed-current continuation, not PDE certification."""
import unittest
from math import gcd
import sympy as s


DEG = [1, 1, 1, 2, 2, 2, 2]


def add(*forms):
    out = {}
    for form in forms:
        for key, value in form.items():
            out[key] = out.get(key, 0) + value
    return {k: s.expand(v) for k, v in out.items() if s.expand(v) != 0}


def scale(value, form):
    return {k: s.expand(value*v) for k, v in form.items() if value*v != 0}


def wedge(left, right):
    out = {}
    for ka, va in left.items():
        for kb, vb in right.items():
            keys = ka + kb
            if any(DEG[i] % 2 and keys.count(i) > 1 for i in keys):
                continue
            sign = (-1)**sum(DEG[i]*DEG[j] for i in ka for j in kb if i > j)
            key = tuple(sorted(keys))
            out[key] = out.get(key, 0) + sign*va*vb
    return add(out)


def mmul(a, b):
    return [[add(*(wedge(a[i][k], b[k][j]) for k in range(2)))
             for j in range(2)] for i in range(2)]


class MixedCurrentChecks(unittest.TestCase):
    def test_full_transgression(self):
        a, b, bc, f11, f12, f21, f22 = [{(i,): s.Integer(1)} for i in range(7)]
        B = [[a, scale(-1, bc)], [b, {}]]
        F = [[f11, f12], [f21, f22]]
        F0 = [[{}, {}], [{}, add(f22, scale(-1, wedge(bc, b)))]]
        B2 = mmul(B, B)
        t = s.symbols('t', real=True)
        Ft = [[add(scale(1-t, F0[i][j]), scale(t, F[i][j]),
                   scale(-t*(1-t), B2[i][j])) for j in range(2)] for i in range(2)]
        prod = mmul(B, Ft)
        integrand = add(prod[0][0], prod[1][1],
                        scale(-1, wedge(a, add(Ft[0][0], Ft[1][1]))))
        result = {k: s.integrate(v, (t, 0, 1)) for k, v in integrand.items()}
        target = add(scale(-1, wedge(a, f22)),
                     scale(s.Rational(1, 2), wedge(b, f12)),
                     scale(-s.Rational(1, 2), wedge(bc, f21)),
                     wedge(a, wedge(bc, b)))
        self.assertEqual(add(result, scale(-1, target)), {})
        # da=F11+bar(b) wedge b; F_A=F11+F22.
        current = add(wedge(a, add(f11, wedge(bc, b))),
                      scale(-1, wedge(a, add(f11, f22))),
                      scale(s.Rational(1, 2), wedge(b, f12)),
                      scale(-s.Rational(1, 2), wedge(bc, f21)))
        self.assertEqual(add(current, scale(-1, target)), {})

    def test_signed_completion(self):
        B, C, chi, x, y = s.symbols('B C chi x y', nonzero=True, real=True)
        original = chi*y*y+4*B*x*x-4*C*x*y
        complete = 4*B*(x-C*y/(2*B))**2+(chi-C*C/B)*y*y
        self.assertEqual(s.expand(original-complete), 0)

    def test_current_primitives(self):
        rho = s.symbols('rho', positive=True)
        chi = 4*(1-rho)**2
        B = 8*(1/rho+s.log(rho)-1)
        C = 8*(-s.log(rho)-1+rho)
        self.assertEqual(s.simplify(s.diff(B, rho)-s.diff(chi, rho)/rho**2), 0)
        self.assertEqual(s.simplify(s.diff(C, rho)-s.diff(chi, rho)/rho), 0)
        self.assertEqual(B.subs(rho, 1), 0)
        self.assertEqual(C.subs(rho, 1), 0)

    def test_model_annihilation_and_mass(self):
        rho = s.symbols('rho', real=True)
        root = 4/s.sqrt(6)
        first = rho**2/4+s.Rational(1, 3)-s.sqrt(6)*rho/4
        self.assertEqual(s.simplify(first-(rho-root)*(rho-2/s.sqrt(6))/4), 0)
        self.assertEqual(s.simplify(rho**2/8-s.Rational(1, 3)
                                   -(rho-root)*(rho+root)/8), 0)
        beta = s.symbols('beta', positive=True)
        q = 4*(1+1/beta)
        rb, Ub = 2*s.sqrt(q)/3, s.Rational(4, 3)*(2/beta-1)
        mass = 16*q**s.Rational(3, 2)*(1-2/beta)/81
        self.assertEqual(s.simplify(mass+Ub*rb**3/2), 0)
        self.assertEqual(mass.subs(beta, 2), 0)
        self.assertEqual(s.limit(mass, beta, s.oo), s.Rational(128, 81))

    def test_replacement_identity(self):
        A, h, PX, HC, HM = s.symbols('A h PX HC HM', real=True)
        common = 4*s.pi**2*A+PX/2-HC
        PM = 2*(common+HM-4*s.pi**2*A*(1-h))
        self.assertEqual(s.expand(PM-(PX+2*HM-2*HC+8*s.pi**2*A*h)), 0)
        U, b = s.symbols('U b', positive=True)
        E = b/(U+b)
        self.assertEqual(s.simplify(E*U-b*(1-E)), 0)

    def test_family_limits_and_indices(self):
        h = s.symbols('h', positive=True)
        F = (4-s.sqrt(1-3*h))**2/9
        x = (F-1+3*h)/18
        y = (15*h-F+1)/72
        self.assertEqual(s.limit(x/h, h, 0), s.Rational(2, 9))
        self.assertEqual(s.limit(y/h, h, 0), s.Rational(7, 36))
        A, k = s.symbols('A k', real=True)
        a2, tau = A-k, A/9-k
        self.assertEqual(s.expand((a2-tau)/8-A/9), 0)
        self.assertEqual(s.expand(-(9*a2-tau)/8-(k-10*A/9)), 0)
        self.assertEqual(4*s.pi**2*s.Rational(7, 36), 7*s.pi**2/9)

    def test_eguchi_hanson_profile(self):
        r, a = s.symbols('r a', positive=True)
        volume_factor = 1-a**4/r**4
        f = (r*r-a*a)/(r*r+a*a)
        self.assertEqual(s.simplify(r**3*volume_factor*s.diff(s.log(f), r)), 4*a*a)
        bulk = -2*(1-a**4/r**4)
        flux = 2*a**4/r**4
        self.assertEqual(s.expand(bulk-flux), -2)

    def test_beta_two_topological_bootstrap(self):
        P, Sigma, D, J, K, rem = s.symbols('P Sigma D J K rem', real=True)
        p_minus_T = (s.Rational(9, 2)*P+s.Rational(9, 8)*Sigma-D)/(36*s.pi**2)
        b_upper = 4*s.pi**2*p_minus_T+J
        self.assertEqual(s.expand(b_upper-(P/2+Sigma/8-D/9+J)), 0)
        self.assertEqual(s.expand(b_upper.subs(Sigma, 8*s.sqrt(6)*K+rem)
                                 -(P/2+s.sqrt(6)*K+rem/8-D/9+J)), 0)
        # Young absorption: C sqrt(Theta K) <= K/2+C^2 Theta/2.
        x, c, t = s.symbols('x c t', nonnegative=True)
        self.assertEqual(s.expand(x*x/2+c*c*t*t/2-c*t*x-(x-c*t)**2/2), 0)

    def test_all_metric_window_constants(self):
        E, e, h, z, alpha = s.symbols('E e h z alpha', real=True)
        D_A = 36*s.pi**2*(e-1-h-2*z)
        Xi_A = 8*s.pi**2*e*E/(4-E)+D_A
        lhs = Xi_A/(36*s.pi**2)-alpha*(h+z)
        rhs = e*(1+2*E/(9*(4-E)))-1-(1+alpha)*h-(2+alpha)*z
        self.assertEqual(s.simplify(lhs-rhs), 0)
        self.assertLess(s.Rational(96, 1)+s.Rational(96, 7), 112)
        # D/V <=36 Delta+48 E, r=E; hence kappa<=49(E+Delta).
        self.assertEqual(s.Rational(96, 2)+1, 49)
        self.assertLessEqual(s.Rational(72, 2), 49)
        F = (4-s.sqrt(1-3*h))**2/9
        self.assertEqual(s.simplify(F-1-h-4*h*h/(1+s.sqrt(1-3*h))**2), 0)

    def test_parameter_transfer_and_shortfall(self):
        z, w, delta = s.symbols('z w delta', real=True)
        # The only pointwise estimate in the D2/Dbeta transfer.
        self.assertEqual(s.expand(z*z+delta*delta*w*w
                                 -(z-delta*w)**2/2-(z+delta*w)**2/2), 0)
        x, y = s.symbols('x y', nonnegative=True)
        self.assertEqual(s.simplify(2*x*(x+y)-(x+s.sqrt(x*y))**2
                                   -x*(s.sqrt(x)-s.sqrt(y))**2), 0)

    def test_dirac_torsion_defect_bounds(self):
        C = [s.eye(2), s.diag(s.I, -s.I), s.Matrix([[0, 1], [-1, 0]]),
             s.Matrix([[0, -s.I], [-s.I, 0]])]
        v = s.symbols('v0:12', real=True)
        P = [None]+[s.Matrix([v[4*k]+s.I*v[4*k+1],
                              v[4*k+2]+s.I*v[4*k+3]]) for k in range(3)]
        P[0] = -sum((C[i]*P[i] for i in range(1, 4)), s.zeros(2, 1))
        phi = s.Matrix([1, 0])
        t = sum((C[i]*phi*P[i][1] for i in range(4)), s.zeros(2, 1))
        x = s.expand(sum((p.conjugate().T*p)[0] for p in P))
        m = s.expand((t.conjugate().T*t)[0])
        zeta2 = s.expand(sum(s.conjugate(p[0])*p[0] for p in P))
        d = 2*x-m
        for polynomial in (d, 4*zeta2-d):
            matrix = s.hessian(polynomial, v)/2
            self.assertTrue(all(eigenvalue >= 0 for eigenvalue in matrix.eigenvals()))
        # Homogeneity recovers d=2 rho^2 |P|^2-|t|^2 <=4 rho |zeta|^2.

    def test_reciprocal_torsion_test(self):
        rho, x, m0, S = s.symbols('rho x m0 S', positive=True)
        denominator = m0+2*rho*rho*x
        a = 2*rho*rho/denominator
        self.assertEqual(s.simplify(s.diff(a, rho)-4*m0*rho/denominator**2), 0)
        self.assertEqual(s.simplify(s.diff(a, x)+4*rho**4/denominator**2), 0)
        self.assertEqual(s.expand((S-2*m0)**2/S-(S-4*m0+4*m0*m0/S)), 0)
        self.assertEqual(s.simplify((S-2*m0)*(s.sqrt(S)-s.sqrt(2*m0))
                                   -(S-2*m0)**2/(s.sqrt(S)+s.sqrt(2*m0))), 0)

    def test_regularized_lichnerowicz_completion(self):
        t, dt, S, dS = s.symbols('t dt S dS', positive=True)
        du = dt/s.sqrt(S)-t*dS/(2*S**s.Rational(3, 2))
        lhs = dt*dt/S-t*dt*dS/S**2
        rhs = du**2-t*t*dS*dS/(4*S**3)
        self.assertEqual(s.simplify(lhs-rhs), 0)
        beta = s.symbols('beta', positive=True)
        rb = 2*s.sqrt(4*(1+1/beta))/3
        Ub = s.Rational(4, 3)*(2/beta-1)
        mb = -Ub*rb**3/2
        self.assertEqual(s.simplify(rb**3/2+3*mb/4-rb**3*(1-1/beta)), 0)
        self.assertEqual(s.limit(rb**3*(1-1/beta), beta, s.oo), s.Rational(64, 27))

    def test_conformal_energy_and_minimizing_excess(self):
        SY, WY, T, p, delta = s.symbols('SY WY T p delta', real=True)
        PY = 4*WY+SY/12-8*s.pi**2*T
        P = 4*WY+(SY+delta)/12-8*s.pi**2*T
        DY = 3*SY/2+18*WY-72*s.pi**2*p
        D = 3*(SY+delta)/2+18*WY-72*s.pi**2*p
        RY, R = PY+SY/4, P+(SY+delta)/4
        self.assertEqual(s.expand(P-PY-delta/12), 0)
        self.assertEqual(s.expand(D-DY-3*delta/2), 0)
        self.assertEqual(s.expand(R-RY-delta/3), 0)
        alpha, L = s.symbols('alpha L', real=True)
        JY, E = 4*PY/RY, (4*P+L)/R
        excess = RY/R*(JY-alpha)+(1-alpha)*delta/(3*R)+L/R
        self.assertEqual(s.factor(E-alpha-excess), 0)

    def test_scalar_free_linear_energy_wall(self):
        e, h, z, J, c = s.symbols('e h z J c', real=True)
        PiA = 2*s.pi**2*e*J+36*s.pi**2*(e-1-h-2*z)
        wall = e*(1+J/18)-1-h-2*z-c*(h+z)
        self.assertEqual(s.expand(PiA/(36*s.pi**2)-c*(h+z)-wall), 0)
        L, U = s.symbols('L U', positive=True)
        Jstar = (L-U)/(L+U/18)
        self.assertEqual(s.factor(L*(1-Jstar)-U*(1+Jstar/18)), 0)

    def test_moving_bf_strip(self):
        N, d, A, eta, theta, alpha, beta = s.symbols(
            'N d A eta theta alpha beta', real=True)
        a = 9*N-d
        u = 3-18*(2*(N-d))/(2*a)
        self.assertEqual(s.factor(u-1-16*d/a), 0)
        Ustar = 1+(1+theta)*eta
        x = (Ustar-u+3*eta)/18
        y = (eta-x)/4
        k, m = A*x-alpha, A*y-beta-4
        h = (4+k+4*m)/A
        actualU = u-3*h+18*k/A
        self.assertEqual(s.factor(h-eta+(12+alpha+4*beta)/A), 0)
        self.assertEqual(s.factor(actualU-Ustar-(36-15*alpha+12*beta)/A), 0)
        h0 = s.symbols('h0', positive=True)
        F = (4-s.sqrt(1-3*h0))**2/9
        self.assertEqual(s.limit((1+(1+theta)*h0-F)/h0, h0, 0), theta)

    def test_zero_end_determinant_saturation(self):
        t = s.symbols('t', nonnegative=True)
        q = 4*(1+t)
        rb = 2*s.sqrt(q)/3
        Ub = s.Rational(4, 3)*(2*t-1)
        mb = -Ub*rb**3/2
        Btop = q*q/18-s.Rational(2, 3)-16*t*t/3
        Bmodel = mb*mb/(2*rb**6)
        self.assertEqual(s.simplify(Bmodel-Ub*Ub/8), 0)
        self.assertEqual(s.simplify(Btop-Bmodel-8*t*(1-2*t)/3), 0)
        self.assertEqual(s.simplify((4*mb/rb**6).subs(t, 0)), s.Rational(9, 8))
        self.assertEqual(s.simplify(Bmodel.subs(t, 0)), s.Rational(2, 9))
        kzero = 9*(s.Rational(8, 9)-s.Rational(2, 9))+s.Rational(2, 3)
        self.assertEqual(kzero, s.Rational(20, 3))

    def test_exact_and_approximate_upper_walls(self):
        beta, e, h, z, J, ell = s.symbols('beta e h z J ell', positive=True)
        B = 3*(1-h)
        b = B/e-1+J
        # S2/V=4 ell(4-J), W+/V=ell b/3, 72pi²p/V=36 ell(1+z)/e.
        direct = (beta+1)/beta*(4*ell*(4-J)+2*beta*ell*b)-36*ell*(1+z)/e
        target = ell*(16-4*J-36*(1+z)/e+2*b+2*beta*b+(16-4*J)/beta)
        self.assertEqual(s.factor(direct-target), 0)
        exact = 16+16/beta-36*(1+z)/e+2*(beta+1)*(B-e)/e
        self.assertEqual(s.factor(target.subs({J: 0, ell: 1})-exact), 0)
        eps = s.symbols('eps', positive=True)
        a0 = eps-16/beta
        H = 2*(beta-7)+a0
        wall = (6*(beta+1)*(1-h)-36)/H
        self.assertEqual(s.factor(exact.subs({z: 0, e: wall})-eps), 0)
        gamma = 9*a0/(4*H)
        self.assertEqual(s.factor(wall-s.Rational(9, 4)+gamma
                                 +6*(beta+1)*(h-s.Rational(1, 4))/H), 0)
        v = s.symbols('v', positive=True)
        F0 = 16-36/v+2*(B/v-1)+8*s.sqrt(2*(B/v-1))
        self.assertEqual(s.simplify(v*F0-((4*s.sqrt(v)+s.sqrt(2*(B-v)))**2-36)), 0)

    def test_projected_torsion_and_signed_hessian_jets(self):
        C = [s.eye(2), s.diag(s.I, -s.I), s.Matrix([[0, 1], [-1, 0]]),
             s.Matrix([[0, -s.I], [-s.I, 0]])]
        h = s.Matrix(4, 4, s.symbols('h0:16'))
        k = s.Matrix(4, 4, s.symbols('k0:16'))
        K = k-k.T
        d1 = [h[j, 0]+s.I*h[j, 1]+k[j, 2]-s.I*k[j, 3] for j in range(4)]
        d2 = [-h[j, 2]-s.I*h[j, 3]+k[j, 0]-s.I*k[j, 1] for j in range(4)]
        def lin(Z):
            return s.Matrix([[Z[0, 2]-Z[1, 3]+s.I*(Z[0, 3]+Z[1, 2]),
                              -Z[2, 2]+Z[3, 3]-s.I*(Z[2, 3]+Z[3, 2])],
                             [Z[0, 0]-Z[1, 1]+s.I*(Z[0, 1]+Z[1, 0]),
                              -Z[2, 0]+Z[3, 1]-s.I*(Z[2, 1]+Z[3, 0])]])
        CK = s.Matrix([[2*s.I*K[0, 1], -K[0, 2]-s.I*K[0, 3]+s.I*K[1, 2]-K[1, 3]],
                       [K[0, 2]+s.I*K[1, 2]-s.I*K[0, 3]+K[1, 3], 2*s.I*K[2, 3]]])
        dt = [s.Matrix([k[j, 0]+s.I*k[j, 1], -k[j, 2]-s.I*k[j, 3]]) for j in range(4)]
        raw = sum((C[j].conjugate().T[0, :].T*dt[j].T for j in range(4)), s.zeros(2))
        errors = s.Matrix([[d2[0]+s.I*d2[1], -d2[2]-s.I*d2[3]],
                           [-d1[0]-s.I*d1[1], d1[2]+s.I*d1[3]]])
        self.assertEqual((raw-lin(h)-CK-errors).applyfunc(s.expand), s.zeros(2))
        # A real positive-Jacobian torsion jet with vanishing projected mode.
        kh = s.Matrix([[s.Rational(1, 2), -s.I/2, 0, 0],
                       [-s.I/2, -s.Rational(1, 2), 0, 0],
                       [0, 0, -s.Rational(1, 2), s.I/2],
                       [0, 0, s.I/2, s.Rational(1, 2)]])
        replacements = dict(zip(h, [0]*16)) | dict(zip(k, kh))
        self.assertEqual(kh-kh.T, s.zeros(4))
        self.assertEqual(s.trace(kh), 0)
        self.assertTrue(all(s.expand(x.subs(replacements)) == 0 for x in d1+d2))
        cols = [x.subs(replacements).applyfunc(s.simplify) for x in dt]
        real_jacobian = s.Matrix.hstack(*(s.Matrix([s.re(x[0]), s.im(x[0]),
                                                     s.re(x[1]), s.im(x[1])]) for x in cols))
        self.assertEqual(real_jacobian.det(), 1)
        self.assertEqual(raw.subs(replacements), s.zeros(2))

    def test_local_gauge_core_right_inverse_symbols(self):
        x = s.symbols('x1:5', real=True)
        T = s.Matrix([x, [-x[1], x[0], -x[3], x[2]],
                      [-x[2], x[3], x[0], -x[1]],
                      [-x[3], -x[2], x[1], x[0]]])
        norm2 = sum(v*v for v in x)
        self.assertEqual((T*T.T-norm2*s.eye(4)).applyfunc(s.expand), s.zeros(4))
        C = [s.eye(2), s.diag(s.I, -s.I), s.Matrix([[0, 1], [-1, 0]]),
             s.Matrix([[0, -s.I], [-s.I, 0]])]
        symbol = sum((x[j]*C[j] for j in range(4)), s.zeros(2))
        self.assertEqual((symbol*symbol.conjugate().T-norm2*s.eye(2)).applyfunc(s.expand), s.zeros(2))
        g = ((x[0]-s.I*x[1])**2-(x[2]-s.I*x[3])**2)/4
        phi = s.Matrix([1, g])
        self.assertEqual(sum((C[j]*phi.diff(x[j]) for j in range(4)), s.zeros(2, 1)), s.zeros(2, 1))
        torsion = sum((C[j]*phi*s.diff(g, x[j]) for j in range(4)), s.zeros(2, 1))
        target = s.Matrix([x[0]-s.I*x[1], x[2]-s.I*x[3]])
        self.assertEqual((torsion-target).applyfunc(s.expand), s.zeros(2, 1))
        self.assertEqual(sum((-C[j].conjugate().T*target.diff(x[j]) for j in range(4)), s.zeros(2, 1)), s.zeros(2, 1))
        m = s.symbols('m', positive=True)
        # A concrete cutoff profile calibrates the radial flux sign; the proof
        # uses smooth cutoffs with these endpoint values, not this polynomial extension.
        chi = (1-m)**2
        self.assertEqual(-s.integrate(s.diff(chi, m), (m, 0, 1)), 1)

    def test_local_torsion_transition_costs(self):
        a, r, lo, hi = s.symbols('a r lo hi', positive=True)
        jac = 2*s.pi**2*r**3
        bounds = (r, s.sqrt(lo)/a**2, s.sqrt(hi)/a**2)
        quartic = s.integrate((4*a**4)**2*jac, bounds)
        mixed = s.integrate((2*a**8*r**2)*(4*a**4)*jac, bounds)
        radial = s.integrate((4*a**8*r**2)*(4*a**4)*jac, bounds)
        self.assertEqual(s.simplify(quartic-8*s.pi**2*(hi**2-lo**2)), 0)
        self.assertEqual(s.simplify(mixed-s.Rational(8, 3)*s.pi**2*(hi**3-lo**3)), 0)
        self.assertEqual(s.simplify(radial-s.Rational(16, 3)*s.pi**2*(hi**3-lo**3)), 0)
        eps = s.symbols('eps', positive=True)
        spherical_factor = (s.sqrt(3)*s.sinh(eps*r/s.sqrt(3))/(eps*r))**2
        self.assertEqual(s.series(spherical_factor, eps, 0, 4).removeO(), 1+eps**2*r**2/9)
        rho = s.Rational(4, 3)
        fplus2 = 2**2*rho**2/8
        self.assertEqual(fplus2, s.Rational(8, 9))
        self.assertEqual(9*fplus2+s.Rational(2, 3), s.Rational(26, 3))

    def test_sharp_coefficient_slack_reduction(self):
        h, z, d, sigma = s.symbols('h z d sigma', real=True)
        e = 1+h+2*z+d
        x = h+z+d-sigma
        self.assertEqual(s.expand(e-x-(1+z+sigma)), 0)
        self.assertEqual(s.expand(e-4*x-(1+h)-(d+2*z-4*x)), 0)
        A, K, Q, J, D, p = s.symbols('A K Q J D p', real=True)
        rem = K+Q/8+J-D/9-4*s.pi**2*(p-A)
        substitution = {sigma:(8*K+Q+8*J)/(32*s.pi**2*A),
                        d:D/(36*s.pi**2*A), z:p/A-1}
        self.assertEqual(s.simplify(4*s.pi**2*A*(sigma-d-z).subs(substitution)-rem), 0)
        t, A0 = s.symbols('t A0', positive=True)
        pp, PP = A0/(1-t*t), 8*s.pi**2*A0*t*t/(1-t*t)
        self.assertEqual(s.simplify(pp-A0-PP/(8*s.pi**2)), 0)
        self.assertEqual(s.Rational(18, 19)*s.Rational(2, 9), s.Rational(4, 19))

    def test_handle_signature_defect_identity(self):
        A, k, ell, S, B, L = s.symbols('A k ell S B L', real=True)
        h = (k+4*ell)/A
        theta = h-6*k/A
        Wplus = B+12*s.pi**2*(A/9-k)
        P = 4*Wplus+S/12-8*s.pi**2*(A-k-4*ell)
        target = S/12+4*B+8*s.pi**2*A*(theta-s.Rational(1, 3))
        self.assertEqual(s.expand(P-target), 0)
        R = P+S/4
        excess = ((1-3*theta)*(S-32*s.pi**2*A)/3+16*B+(1+theta)*L)
        self.assertEqual(s.simplify((4*P+L)-4*theta*R/(1+theta)
                                   -excess/(1+theta)), 0)
        self.assertEqual(s.simplify(4*P+L-R
                                   -(8*s.pi**2*A*(3*theta-1)+12*B+L)), 0)

    def test_weyl_only_blowdown_cap_identity(self):
        A, h, k, S, L, Bn, Kp, Cp = s.symbols('A h k S L Bn Kp Cp', real=True)
        Bm = 12*s.pi**2*k+Bn+Kp-Cp
        Pm = S/12+4*Bm+8*s.pi**2*A*(h-s.Rational(1, 3))-48*s.pi**2*k
        target = 8*s.pi**2*A*h+(S-32*s.pi**2*A)/12+4*(Bn+Kp-Cp)
        self.assertEqual(s.expand(Pm-target), 0)
        Rm = Pm+S/4
        excess = (1-3*h)*(S-32*s.pi**2*A)/3+16*(Bn+Kp-Cp)+(1+h)*L
        self.assertEqual(s.simplify((4*Pm+L)*(1+h)-4*h*Rm-excess), 0)
        self.assertEqual(s.simplify(16*Cp/((1+h)*8*s.pi**2*A*(1+h))
                                   -2*Cp/(s.pi**2*A*(1+h)**2)), 0)
        c = s.symbols('c', real=True)
        cap_cost = (1+h)*(8*s.pi**2*A*(1+h))/16*(4*h/(1+h)-c*h)
        self.assertEqual(s.limit(cap_cost/(A*h), h, 0), s.pi**2*(4-c)/2)

    def test_euler_density_and_balanced_signature(self):
        W, P, S, chi = s.symbols('W P S chi', real=True)
        cgb = W-P/2+S/24
        curvature_operator = W+P/2+S/24
        self.assertEqual(s.expand(curvature_operator-cgb-P), 0)
        h = s.symbols('h', positive=True)
        F = (4-s.sqrt(1-3*h))**2/9
        blowup_ratio = (F-1+3*h)/18
        theta = h-6*blowup_ratio
        self.assertEqual(s.limit(theta/h, h, 0), -s.Rational(1, 3))

    def test_round_boundary_signed_weyl_flux(self):
        r, t = s.symbols('r t', positive=True)
        F = s.Function('F')(r)
        flux = -4*(1-F**2)**2-2*r**2*s.diff(F, r)**2
        density = 4*s.diff(F, r)*(4*F*(1-F**2)
                    -r*s.diff(F, r)-r**2*s.diff(F, r, 2))
        self.assertEqual(s.simplify(s.diff(flux, r)-density), 0)
        polynomial = 1+t*r**2*(1-r**2)
        boundary_flux = flux.subs(F, polynomial).doit()
        self.assertEqual(s.simplify(2*s.pi**2*(boundary_flux.subs(r, 1)
                         -boundary_flux.subs(r, 0))), -16*s.pi**2*t**2)

    def test_variational_threshold_and_stationarity(self):
        alpha, S, W, chi = s.symbols('alpha S W chi', real=True)
        tau = -1/(4-alpha)
        R = 2*W+S/3-16*s.pi**2*chi
        target = 2*W+(1-alpha)*S/(3*(4-alpha))-16*s.pi**2*chi
        self.assertEqual(s.simplify(R+tau*S-target), 0)
        S1, V, Ric = s.symbols('S1 V Ric', nonzero=True, real=True)
        E = 4-S1**2/(V*Ric)
        self.assertEqual(s.simplify(-1/(4-E)+V*Ric/S1**2), 0)
        # Parallel Ricci of rank r has E=4-r; no integer lies in (0,1).
        self.assertTrue(all(not 0 < 4-r < 1 for r in range(1, 5)))

    def test_directional_weyl_and_finite_cost(self):
        V, A, h, t = s.symbols('V A h t', positive=True)
        Weyl = s.Rational(3, 8)/V*(-4*V/3+t/2)**2
        self.assertEqual(s.expand(Weyl-(2*V/3-t/2+3*t*t/(32*V))), 0)
        P = 4*Weyl+4*V/3-8*s.pi**2*A*(1-h)
        gap = 4*(1-h)*(V-2*s.pi**2*A)-2*t+3*t*t/(8*V)
        self.assertEqual(s.simplify(P-4*h*V-gap), 0)
        self.assertEqual(s.simplify(8/((1+h)*8*s.pi**2*A*(1+h))
                                   -1/(s.pi**2*A*(1+h)**2)), 0)

    def test_smooth_form_cost_and_scaling(self):
        V, a, b, T, q = s.symbols('V a b T q', positive=True)
        cost = s.Rational(4, 3)*(V-a*a/b)+a*T/b-3*T*T/(16*b)
        scaled = cost.subs({a:q*q*a, b:q**4*b, T:q*q*T}, simultaneous=True)
        self.assertEqual(s.simplify(scaled-cost), 0)
        self.assertEqual(s.simplify(cost.subs({a:V, b:V})-(T-3*T*T/(16*V))), 0)

    def test_improved_compact_parameter(self):
        t = s.symbols('t', positive=True)
        beta = 1/t
        self.assertEqual(s.simplify(t*(beta-2)**2/beta**2-t*(1-2*t)**2), 0)
        self.assertEqual(s.simplify(t*(beta-2)**2/beta**4-t**3*(1-2*t)**2), 0)

    def test_spin_c_resonant_characters(self):
        for n in range(2, 101):
            for q in range(1, n):
                if gcd(q, n) != 1:
                    continue
                actual = []
                for a in range(n):
                    pos = a % n == 0 or (a+1+q) % n == 0
                    neg = (3*a+q+2) % n == 0 or (3*a+1+2*q) % n == 0
                    if pos and neg:
                        actual.append(a)
                predicted = (q+2) % n == 0 or (2*q+1) % n == 0
                self.assertEqual(bool(actual), predicted)
                if predicted:
                    self.assertEqual(n % 2, 1)
                    self.assertEqual(set(actual), {0, (-1-q) % n})
                    self.assertEqual({(2*a+1+q) % n for a in actual},
                                     {(1+q) % n, (-1-q) % n})
        for n in range(3, 101, 2):
            for a in range(n):
                k = (2*a-1) % n
                self.assertEqual(a in {0, 1}, k in {1, n-1})

    def test_clifford_seed_and_holonomy(self):
        lam = s.symbols('lam', nonzero=True)
        z1, z2, zb1, zb2 = s.symbols('z1 z2 zb1 zb2')
        Q = s.Matrix([[z1, -zb2], [z2, zb1]])
        Ap, Am = s.diag(1, lam), s.diag(1/lam, lam**2)
        target = s.Matrix([[z1/lam, -zb2/lam**2], [lam**2*z2, lam*zb1]])
        self.assertEqual(s.simplify(Am*Q*Ap.inv()-target), s.zeros(2))
        a, r, c = s.symbols('a r c', real=True)
        C1, C2 = s.eye(2), s.diag(s.I, -s.I)
        e1, e2 = s.Matrix([1, 0]), s.Matrix([0, 1])
        self.assertEqual(C1*c*e2+C2*(-s.I*c*e2), s.zeros(2, 1))
        Phi = a*e1+r*c*zb1*e2
        self.assertEqual(s.simplify(a*c*(C1*Phi-s.I*C2*Phi)-2*a*a*c*e1),
                         s.zeros(2, 1))
        self.assertEqual(4*s.Rational(4, 3)**2*s.Rational(2, 9),
                         s.Rational(128, 81))

    def test_annular_critical_scaling(self):
        q = s.Rational(4, 3)
        self.assertEqual(q-4, -s.Rational(8, 3))
        self.assertEqual(4-s.Rational(8, 3), s.Rational(4, 3))
        # Density packing: r^4 <= O(eta^.5), r^(8/3) <= O(eta^(2/3)).
        self.assertEqual(s.Rational(1, 2)/4, s.Rational(1, 8))
        self.assertEqual(s.Rational(2, 3)/s.Rational(8, 3), s.Rational(1, 4))

    def test_surgery_euler_ratio(self):
        x, y = s.symbols('x y', nonnegative=True)
        h, chi_A = x+4*y, s.Rational(1, 3)+x-2*y
        self.assertEqual(s.expand(s.Rational(1, 3)+h-chi_A), 6*y)

    def test_topological_density_and_opposite_bundles(self):
        chi, tau, a2 = s.symbols('chi tau a2', real=True)
        Tp, Tm = 2*chi+3*tau, 2*chi-3*tau
        Cp, Cm = (a2-Tp)/4, (a2+Tm)/4
        self.assertEqual(s.expand(Cm-chi-Cp), 0)
        self.assertEqual(s.expand(Cm+2*a2-chi-2*Tp-9*Cp), 0)
        beta = s.symbols('beta', positive=True)
        Tdensity = 1/(6*s.pi**2)+4/(3*s.pi**2*beta**2)
        self.assertEqual(s.simplify(2*Tdensity-1/(3*s.pi**2)
                                   -8/(3*s.pi**2*beta**2)), 0)
        scalar = s.symbols('scalar', real=True)
        self.assertEqual(s.expand(scalar**2/12+(scalar+4)**2/4
                                   -1-(scalar+3)**2/3), 0)
        self.assertEqual((41+s.Rational(1, 3))/(1-s.Rational(1, 3)), 62)


if __name__ == '__main__':
    unittest.main(verbosity=2)
