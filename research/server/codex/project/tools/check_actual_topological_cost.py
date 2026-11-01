#!/usr/bin/env python3
"""Finite identities only; not verification of the analytic concentration theorem."""
import unittest
import sympy as s


class ActualCostIdentities(unittest.TestCase):
    def test_weighted_remainder(self):
        scalar, rho, f, c, K, J, p = s.symbols("S rho f c K J p", real=True)
        # Integrated moments: x=int(s rho), y=int(rho^2), z=int(f rho^2),
        # w=int(f^2 rho^2). The weight is not treated as pointwise constant.
        x, y, z, w = s.symbols("x y z w", real=True)
        Sigma = scalar - 32*s.pi**2*p
        lhs = Sigma + w-2*c*z+c*c*y
        rhs = scalar+2*c*x+c*c*y+8*c*K+8*J
        self.assertEqual(s.expand((lhs-rhs).subs({x: -4*K-z,
                                               w: 32*s.pi**2*p+8*J})), 0)

    def test_cost_constants(self):
        self.assertEqual(2*(s.Rational(9, 4)+6), s.Rational(33, 2))
        self.assertEqual(s.Rational(4, 9)*2*(39+6), 40)
        self.assertEqual(2*(4+6*40), 488)
        self.assertEqual(16*s.Rational(33, 2), 264)
        self.assertEqual(s.Rational(4, 9)*117, 52)
        self.assertEqual(2*(488+264), 1504)
        self.assertEqual(488+52, 540)

    def test_chern_and_signed_energy(self):
        a2, chi, tau = s.symbols("a2 chi tau", real=True)
        Tp = 2*chi+3*tau
        cm = (a2+2*chi-3*tau)/4
        self.assertEqual(s.expand(cm+2*a2-(5*chi+6*tau+9*(a2-Tp)/4)), 0)
        wp, wm, scalar2, P, fp, fm = s.symbols("wp wm scalar2 P fp fm", real=True)
        Tp4pi = 2*wp+scalar2/24-P/2
        cplus16pi = fp-fm-2*wp-scalar2/24+P/2
        self.assertEqual(s.expand(cplus16pi-((fp-fm)-Tp4pi)), 0)
        cB16pi = 2*wm+scalar2/24-P/2+9*fp-9*fm
        FB2 = wm+scalar2/48+P/4+s.Rational(9, 2)*(fp+fm)
        self.assertEqual(s.expand(FB2-cB16pi/2-P/2-9*fm), 0)

    def test_normalization_and_limits(self):
        R, I, V, u = s.symbols("R I V u", nonzero=True, real=True)
        E = 4-I**2/(V*R)
        residual = R*u*u/V-2*I*u/V+4
        self.assertEqual(s.simplify(residual.subs(u, I/R)-E), 0)
        self.assertEqual(s.simplify((R/I)**2*V-R/(4-E)), 0)
        b = s.symbols("b", positive=True)
        rb = s.Rational(2, 3)*s.sqrt(4*(1+1/b))
        Ub = s.Rational(4, 3)*(2/b-1)
        self.assertEqual(s.limit(-Ub*rb/4, b, s.oo), s.Rational(4, 9))
        self.assertEqual(s.Rational(1, 2)*s.Rational(4, 3)*s.Rational(64, 27),
                         s.Rational(128, 81))
        h = s.symbols("h", positive=True)
        F = (4-s.sqrt(1-3*h))**2/9
        y = (15*h-F+1)/72
        self.assertEqual(s.limit(y/h, h, 0), s.Rational(7, 36))

    def test_hopf_derivative(self):
        r, a, b, c, d = s.symbols("r a b c d", real=True)
        rho = r*r
        spinor_derivative = a*a+b*b+c*c+d*d
        form_derivative = 4*r*r*(a*a+c*c+d*d)
        gamma2 = r*r*b*b
        drho2 = 4*r*r*a*a
        self.assertEqual(s.expand(4*rho*spinor_derivative-form_derivative-4*gamma2), 0)
        self.assertEqual(s.expand(drho2/4+gamma2-r*r*(a*a+b*b)), 0)

    def test_clifford_cubic_dirac(self):
        eye = s.eye(2)
        C = [eye, s.diag(s.I, -s.I), s.Matrix([[0, 1], [-1, 0]]),
             s.Matrix([[0, -s.I], [-s.I, 0]])]
        M = [-c.conjugate().T for c in C]
        for i in range(4):
            for j in range(4):
                self.assertEqual(M[i]*C[j]+M[j]*C[i],
                                 -2*int(i == j)*eye)
        r = s.symbols("r", real=True)
        phi = s.Matrix([r, 0])
        coeff = s.symbols("v0:12", real=True)
        P = [None] + [s.Matrix([coeff[4*k]+s.I*coeff[4*k+1],
                               coeff[4*k+2]+s.I*coeff[4*k+3]]) for k in range(3)]
        P[0] = -sum((C[i]*P[i] for i in range(1, 4)), s.zeros(2, 1))
        wedge = lambda x, y: x[0]*y[1]-x[1]*y[0]
        w = [wedge(phi, p) for p in P]
        Q = s.zeros(2, 1)
        for j in range(4):
            for i in range(4):
                Q += M[j]*C[i]*(P[j]*w[i]+phi*wedge(P[j], P[i]))
        rhs = -4*sum((P[i]*w[i] for i in range(4)), s.zeros(2, 1))
        self.assertEqual((Q-rhs).applyfunc(s.expand), s.zeros(2, 1))
        J = [(M[0]*C[1]+M[2]*C[3])/2,
             (M[0]*C[2]-M[1]*C[3])/2,
             (M[0]*C[3]+M[1]*C[2])/2]
        self.assertEqual(sum((j*phi*wedge(phi, j*phi) for j in J),
                             s.zeros(2, 1)).applyfunc(s.expand), s.zeros(2, 1))
        for j in J:
            self.assertEqual(j*j, -eye)
        for anti in (M[0]*C[1]-M[2]*C[3], M[0]*C[2]+M[1]*C[3],
                     M[0]*C[3]-M[1]*C[2]):
            self.assertEqual(anti, s.zeros(2))

    def test_squared_cutoff_ratio(self):
        eta, eta_prime = s.symbols("eta eta_prime", real=True)
        chi = (1-eta)**2
        derivative = -2*(1-eta)*eta_prime
        self.assertEqual(s.cancel(derivative**2/chi), 4*eta_prime**2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
