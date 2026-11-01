#!/usr/bin/env python3
"""Finite algebra checks only: not PDE, gauge existence, or metric construction."""
import itertools
import unittest

import sympy as s


class BoundaryAlgebra(unittest.TestCase):
    def test_near_closed_constant(self):
        self.assertEqual(s.Rational(9, 8) * s.Rational(1, 2) *
                         s.Rational(4, 27) * 117, s.Rational(39, 4))
        self.assertEqual(2 * s.Rational(2, 3) * (3 * s.sqrt(2))**4, 432)

    def test_rounding_identities(self):
        q, A, alpha, beta = s.symbols("q A alpha beta", positive=True)
        eta = (1 - q*q) / 3
        F = (4-q)**2 / 9
        x, y = (F-1+3*eta)/18, (15*eta-F+1)/72
        self.assertEqual(s.simplify(x+4*y-eta), 0)
        self.assertEqual(s.simplify(1+15*x-12*y-F), 0)
        k, ell = A*x-alpha, A*y-beta-2
        self.assertEqual(s.simplify((k+4*ell)/A-
                                    (eta-(alpha+4*beta+8)/A)), 0)
        self.assertEqual(s.simplify(1+(15*k-12*ell)/A-
                                    (F+(-15*alpha+12*beta+24)/A)), 0)
        self.assertEqual(s.simplify((A-k)-(A-k-4*ell)-4*ell), 0)

    def test_relative_defect_and_gluing(self):
        R, V, I, z, A, h = s.symbols("R V I z A h", positive=True)
        residual = R*z*z/V-2*I*z/V+4
        self.assertEqual(s.simplify(residual.subs(z, I/R)), 4-I*I/(R*V))
        limit = 4-(-8*s.pi**2*A)**2/((2*s.pi**2*A)*(8*s.pi**2*A*(1+h)))
        self.assertEqual(s.simplify(limit-4*h/(1+h)), 0)

    def test_chern_boundary(self):
        S, P, p, chi, tau = s.symbols("S P p chi tau")
        Tp, Tm = 2*chi+3*tau, 2*chi-3*tau
        Wp = (4*s.pi**2*Tp-S/24+P/2)/2
        Wm = (4*s.pi**2*Tm-S/24+P/2)/2
        D = s.Rational(3, 2)*S+18*Wp-72*s.pi**2*p
        self.assertEqual(s.simplify(D+72*s.pi**2*(p-Tp)+54*Wm-
                                    18*P-144*s.pi**2*(chi-3*tau)), 0)

    def test_slack_and_formal_moments(self):
        scalar, w, p = s.symbols("scalar w p")
        D = s.Rational(3, 2)*(scalar**2+2*w*w)-72*s.pi**2*p
        z = scalar+2*w
        expression = s.Rational(4, 9)*D+s.Rational(2, 3)*scalar*z-z*z/3
        self.assertEqual(s.expand(expression-(scalar**2-32*s.pi**2*p)), 0)
        h = s.symbols("h", positive=True)
        R, P, S, W = 1+h+2*h*h, h*h, 4*(1+h+h*h), (1-h)**2/6
        D = s.expand(s.Rational(3, 2)*S+18*W-9)
        Sigma = S-4
        self.assertEqual(D, 9*h*h)
        self.assertEqual(s.simplify(Sigma/(P+D)-2*(1+h)/(5*h)), 0)
        self.assertEqual(s.simplify(4-S/R+D/R), 13*h*h/(1+h+2*h*h))
        self.assertEqual(s.simplify(S/24+2*W-P/2), (1-h)/2)

    def test_joint_certificate_example(self):
        Q = s.Matrix([[1, -s.Rational(1, 2), -s.Rational(1, 2)],
                      [-s.Rational(1, 2), 1, -s.Rational(1, 2)],
                      [-s.Rational(1, 2), -s.Rational(1, 2), 1]])
        Y = s.eye(3)-s.ones(3)/3
        maximum = max((s.Matrix(v).T*Y*s.Matrix(v))[0]
                      for v in itertools.product((-1, 1), repeat=3))
        self.assertEqual(Y*Y, Y)
        self.assertEqual(s.trace(Y*Q), 3)
        self.assertEqual(maximum, s.Rational(8, 3))
        self.assertEqual(2*(s.Rational(49, 2))+2*(2*6480+2*180), 26689)

    def test_full_cube_threshold(self):
        rows = list(itertools.product((-1, 1), repeat=3))
        Z = s.Matrix(rows)
        m = len(rows)
        F, N = Z[:, :2], Z[:, 2:]
        Y = F*F.T/m
        self.assertEqual(Y*Y, Y)
        self.assertEqual(Y*N, s.zeros(m, 1))
        H = max((s.Matrix(v).T*Y*s.Matrix(v))[0]
                for v in itertools.product((-1, 1), repeat=m))
        self.assertEqual(H, m)
        for total in (s.Rational(4, 5), s.Integer(1), s.Rational(3, 2)):
            Q = F*s.diag(total/3, 2*total/3)*F.T-s.Rational(7, 9)*N*N.T
            self.assertEqual(s.trace(Y*Q), m*total)
            if total <= 1:
                C = F*s.diag(total/3, 2*total/3)*F.T+(1-total)*s.eye(m)
                self.assertTrue((C-Q).is_positive_semidefinite)
            else:
                self.assertGreater(s.trace(Y*Q), H)


if __name__ == "__main__":
    unittest.main(verbosity=2)
