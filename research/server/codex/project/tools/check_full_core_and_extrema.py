#!/usr/bin/env python3
"""Exact finite checks for full-core cost and extrema; not PDE certification."""

from fractions import Fraction as F
import unittest

import sympy as s


def saw(numerator, denominator):
    residue = numerator % denominator
    return F(residue, denominator) - F(1, 2) if residue else F(0)


def eta(n, q):
    return 4 * sum((saw(k, n) * saw(q * k, n) for k in range(1, n)), F(0))


def hj(n, q):
    out = []
    while q:
        a = (n + q - 1) // q
        out.append(a)
        n, q = q, a * q - n
    return out


class FullCoreChecks(unittest.TestCase):
    def test_eta_exact_dedekind(self):
        for n in range(3, 102, 2):
            self.assertEqual(eta(n, n - 2), -F((n - 1) * (n - 5), 6 * n))

    def test_continued_fraction(self):
        for n in range(3, 102, 2):
            self.assertEqual(hj(n, n - 2), [2] * ((n - 3) // 2) + [3])
            self.assertEqual(((n - 2) * ((n - 1) // 2)) % n, 1)

    def test_boundary_fraction_and_resolution(self):
        for n in range(3, 102, 2):
            boundary = F(2, n) + 3 * eta(n, n - 2)
            frac = F(n - 1, 2 * n)
            chi, tau = F(n + 1, 2), -F(n - 1, 2)
            self.assertEqual(boundary, F(5 - n, 2) + frac)
            self.assertEqual(2 * chi + 3 * tau, boundary - frac)
            self.assertGreaterEqual(frac, F(1, 3))
            self.assertLess(frac, F(1, 2))

    def test_opposite_orientation_is_different(self):
        self.assertEqual(F(2, 3) + 3 * eta(3, 1), F(4, 3))
        self.assertEqual(F(2, 3) + 3 * eta(3, 2), 0)
        self.assertEqual(F(2, 9) + 3 * eta(9, 7), -F(14, 9))
        self.assertEqual(F(2, 9) + 3 * eta(9, 2), 2)

    def test_binary_and_trivalent(self):
        for n in range(3, 24, 2):
            for a in range(3, 24, 2):
                for b in range(3, 24, 2):
                    diff = F(n - 1, 2 * n) - F(a - 1, 2 * a) - F(b - 1, 2 * b)
                    self.assertGreater(diff, -F(2, 3))
                    self.assertLess(diff, -F(1, 6))
        self.assertEqual(F(1, 3) - 3 * F(4, 9), -1)

    def test_sfk_energy(self):
        for n in range(3, 102, 2):
            # Curvature integrals divided by pi^2.
            ric = 4 * F(n - 1, n)
            minus = 4 * n + 6 - F(10, n)
            self.assertEqual((minus - ric / 2) / 8 + F(1, n), F(n + 1, 2))
            self.assertEqual(-minus / 12 + eta(n, n - 2), -F(n - 1, 2))

    def test_signed_branch_and_small_volume_cost(self):
        for n in range(3, 102, 2):
            f = F(n - 1, 2 * n)
            self.assertGreaterEqual(8 * f, F(8, 3))
            self.assertEqual(2 * (1 - f), 1 + F(1, n))
            self.assertGreater(2 * (1 - f), 1)
            for j in range(-3, 1):
                self.assertGreaterEqual(8 * (f - j), 8 * f)

    def test_scale_and_core_model_bound(self):
        t, L = s.symbols('t L', nonnegative=True)
        # A has eigenvalues -2t rho/3, t rho/3, t rho/3.
        self.assertEqual(s.expand((-2*t*L**2/3)**2 + 2*(t*L**2/3)**2), 2*t**2*L**4/3)
        self.assertEqual(s.simplify((8 * 2*t**2*L**4/3).subs(t, s.Rational(1, 4))), L**4/3)


class ActualRemainderChecks(unittest.TestCase):
    def test_nonnegative_remainder_identity(self):
        x, W, gamma, p = s.symbols('x W gamma p')
        actual_f = W - gamma/2 + s.Rational(2, 3)*x**4 - 4*x**3 + s.Rational(8, 3)*x**2
        harmonic = 2*x**2 - 4*s.pi**2*p
        amplitude = s.Rational(2, 3)*(1-x)**2*(2+4*x-x**2)
        self.assertEqual(s.expand(actual_f+gamma/2+harmonic+amplitude), W+s.Rational(4, 3)-4*s.pi**2*p)

    def test_amplitude_estimates(self):
        for k in range(101):
            x = F(k, 100)
            H = F(2, 3)*(1-x)**2*(2+4*x-x*x)
            self.assertGreaterEqual(H, F(4, 3)*(1-x)**2)
            self.assertLessEqual(16*(1-x)**2, 12*H)
            L0 = 2*H-2*(1-x)**2
            self.assertEqual(L0, F(2, 3)*(1-x)**2*(1+8*x-2*x*x))
            self.assertGreaterEqual(L0, 0)

    def test_dirac_hopf_coefficients(self):
        u2,u3,u4,v2,v3,v4,w2,w3,w4,z2,z3,z4 = s.symbols('u2 u3 u4 v2 v3 v4 w2 w3 w4 z2 z3 z4')
        u = [v2-w3-z4,u2,u3,u4]
        v = [-u2-z3+w4,v2,v3,v4]
        w = [-z2+u3-v4,w2,w3,w4]
        z = [w2+v3+u4,z2,z3,z4]
        # rho=1 suffices by homogeneity. omega derivative components are
        # (u_i Sigma1+z_i Sigma2-w_i Sigma3)/2.
        comps = {(0,1):u,(2,3):u,(0,2):z,(1,3):[-a for a in z],
                 (0,3):[-a for a in w],(1,2):[-a for a in w]}
        exterior = []
        for a,b,c in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]:
            exterior.append((comps[b,c][a]-comps[a,c][b]+comps[a,b][c])/2)
        self.assertEqual(s.expand(sum(a*a for a in exterior)-sum(a*a for a in v)/4), 0)
        nabla_omega = sum(a*a for block in (u,w,z) for a in block)/2
        nabla_phi = sum(a*a for block in (u,v,w,z) for a in block)
        self.assertEqual(s.expand(nabla_omega-nabla_phi/2+sum(a*a for a in v)/2), 0)

    def test_exact_signed_balance(self):
        F0,G,J,H,K,Q,excess,ah = s.symbols('F G J H K Q excess ah')
        D = 18*(F0+G/2+J+H)
        sigma = 8*K+Q+8*J
        # Chern-Weil at s=-4: P = 8 pi^2 Ah + 8 pi^2(p-A)+2D/9-Sigma/4.
        P = 8*s.pi**2*ah+8*s.pi**2*excess+2*D/9-sigma/4
        target = 2*(2*F0+G+J+(2*H-Q/8)+4*s.pi**2*excess-K)
        self.assertEqual(s.expand(P-8*s.pi**2*ah-target), 0)


class VariationalChecks(unittest.TestCase):
    def test_frozen_parameter(self):
        alpha = s.symbols('alpha')
        b = alpha/(4-alpha)
        tau = -1/(4-alpha)
        self.assertEqual(s.simplify(2+8*tau+2*b), 0)
        self.assertEqual(s.simplify((s.Rational(1,3)-2*b).subs(alpha,s.Rational(4,7))), 0)

    def test_gradient_scalar_coefficient(self):
        P,V = s.symbols('P V', positive=True)
        alpha = 4*P/(P+4*V)
        R,S2 = P+4*V,16*V
        self.assertEqual(s.simplify(S2/R**2-(4-alpha)/R), 0)
        self.assertEqual(s.simplify(alpha/(4-alpha)-P/(4*V)), 0)

    def test_complementary_pairs(self):
        a,b,c = s.symbols('a b c')
        eigen = [a,b,c,-a-b-c]
        self.assertEqual(s.expand(sum((eigen[0]+z)**2 for z in eigen[1:])-sum(z*z for z in eigen)), 0)

    def test_weighted_weyl_cauchy(self):
        f,g = s.symbols('f g')
        self.assertEqual(s.expand(s.Rational(8,9)*(f*f+3*g*g)-s.Rational(2,3)*(f+g)**2-s.Rational(2,9)*(f-3*g)**2), 0)

    def test_signed_energy_budget(self):
        A,P,e,h,z,u = s.symbols('A P e h z u')
        D18 = 2*s.pi**2*A*(e-1-h-2*z)
        minus = P/3+2*s.pi**2*A*(u-e)/3
        self.assertEqual(s.expand(D18+3*minus-P-2*s.pi**2*A*(u-1-h-2*z)), 0)

    def test_low_level_and_limit(self):
        h = s.symbols('h', positive=True)
        alpha = 4*h/(1+h)
        self.assertEqual(s.simplify(alpha/(4-alpha)), h)
        self.assertEqual(s.Rational(9,8)*s.Rational(1,3)**2, s.Rational(1,8))
        self.assertEqual((s.sqrt(s.Rational(1,8))/2)**2, s.Rational(1,32))


class NormalizedGeometryChecks(unittest.TestCase):
    def test_small_diameter_arithmetic(self):
        self.assertEqual(F(2*32**4,16**4), 32)
        self.assertEqual(32*8**4, 2**17)
        self.assertEqual(F(2**17,2**20), F(1,8))

    def test_good_center_fraction(self):
        self.assertLessEqual(F(32,2**20), F(1,2))
        self.assertEqual(2*2**4, 32)

    def test_normalized_scaling(self):
        r = s.symbols('r', positive=True)
        # The probability measure is unchanged by homothety. Ric and Rm
        # tensor norms both multiply by r^2 under h=r^-2 g.
        self.assertEqual((r**2)**2, r**4)
        self.assertEqual(s.simplify((r**2)**2/r**4), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
