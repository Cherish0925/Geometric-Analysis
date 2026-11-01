#!/usr/bin/env python3
"""Exact coefficient checks; not certification of PDE or global decomposition."""

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import unittest

import sympy as s

ROOT = Path(__file__).resolve().parents[1]


class MarkedChargeChecks(unittest.TestCase):
    def test_plumbing_last_column(self):
        for k in range(1, 65):
            n = 2*k+1
            col = [F(-i, n) for i in range(1, k+1)]
            for i in range(k):
                out = (-3 if i == k-1 else -2)*col[i]
                out += col[i-1] if i else 0
                out += col[i+1] if i+1 < k else 0
                self.assertEqual(out, int(i == k-1))

    def test_fractional_atom_and_integer_charge(self):
        for n in range(3, 202, 2):
            f = F(n-1, 2*n)
            self.assertGreaterEqual(f, F(1, 3))
            self.assertLess(f, F(1, 2))
            for m in range(-10, 11):
                self.assertGreaterEqual(abs(m-f), f)
                self.assertLessEqual(abs(m), 2*abs(m-f))

    def test_relative_spinor_indices(self):
        n,m,chi,tau = s.symbols('n m chi tau')
        f=(n-1)/(2*n)
        eta=-(n-1)*(n-5)/(6*n)
        boundary=2/n+3*eta
        j=2*chi+3*tau-(5-n)/2
        plus=(m-f-(2*chi+3*tau-boundary))/4
        minus=(9*(m-f)+2*chi-3*tau-(2/n-3*eta))/4
        self.assertEqual(s.simplify(plus-(m-j)/4), 0)
        self.assertEqual(s.simplify(minus-plus-(chi-1+2*m)), 0)

    def test_unbounded_opposite_index(self):
        k=s.symbols('k', positive=True)
        n=2*k+1
        f=k/n
        eta=-(n-1)*(n-5)/(6*n)
        minus=(-9*f+2*(k+1)-3*(-k)-(2/n-3*eta))/4
        self.assertEqual(s.simplify(minus-k), 0)
        self.assertEqual(s.simplify(minus/f-n), 0)

    def test_telescoping(self):
        # A binary shell, one unary shell, and three terminal fillings.
        root,a,b,c,m0,m1,m2,m3,m4=s.symbols('r a b c m0:5')
        shells=[m0+root-a-b,m1+a-c,m2+b,m3+c]
        self.assertEqual(s.expand(sum(shells)-(m0+m1+m2+m3+root)), 0)

    def test_trace_holder_exponents(self):
        self.assertEqual(F(1,4)+F(1,2)+F(1,4), 1)
        self.assertEqual(F(1,4)+F(3,4), 1)
        # h^(1/4) j^(3/4) of constant order requires j ~ h^(-1/3).
        self.assertEqual(F(1,4)+F(3,4)*F(-1,3), 0)


class SignedFluxChecks(unittest.TestCase):
    def test_exact_spatial_balance(self):
        k,l,z,J,Bo,Po,M,q=s.symbols('k l z J Bo Po M q')
        pi2=s.pi**2
        B=4*pi2*(z+k)+J
        Pchi=32*pi2*l+2*(B-Bo)+2*M-32*pi2*q
        left=Pchi+Po-8*pi2*(k+4*l)
        right=Po+8*pi2*z+2*J-2*Bo+2*M-32*pi2*q
        self.assertEqual(s.expand(left-right), 0)

    def test_balanced_fractions(self):
        x,y=s.symbols('x y')
        sol=s.solve([x+4*y-1,15*x-12*y-1],[x,y])
        self.assertEqual(sol, {x:s.Rational(2,9),y:s.Rational(7,36)})
        self.assertEqual(16*sol[y], s.Rational(28,9))

    def test_flux_threshold_and_critical_cost(self):
        c=s.symbols('c')
        bound=s.Rational(7,36)-c/16
        self.assertEqual(bound.subs(c,s.Rational(28,9)), 0)
        self.assertEqual(32*s.Rational(7,36), s.Rational(56,9))
        self.assertEqual(4*s.Rational(2,9), s.Rational(8,9))
        self.assertEqual(s.Rational(2,3)-s.Rational(1,8), s.Rational(13,24))

    def test_cutoff_volume_bound(self):
        for rho in [F(i,100) for i in range(51,100)]:
            self.assertGreaterEqual((4-rho)**2, 9)

    def test_euler_density_lower_bound(self):
        x=s.symbols('x')
        self.assertEqual(s.expand((4-2*x)**2/24-x*x/2-
                                 (s.Rational(2,3)-2*x/3-x*x/3)), 0)


class ActualLocalSeedChecks(unittest.TestCase):
    def test_antiholomorphic_seed_and_cubic_components(self):
        x1,x2,x3,x4=s.symbols('x1 x2 x3 x4', real=True)
        z1,z2=x1-s.I*x2,x3-s.I*x4
        for d in range(1, 9):
            # Normalize c_d to one; it multiplies every derivative linearly.
            g=(z1**(d+1)-z2**(d+1))/(2*(d+1))
            self.assertEqual(s.expand(s.diff(g,x1)-s.I*s.diff(g,x2)), 0)
            self.assertEqual(s.expand(s.diff(g,x3)-s.I*s.diff(g,x4)), 0)
            self.assertEqual(s.expand(s.diff(g,x1)+s.I*s.diff(g,x2)-z1**d), 0)
            self.assertEqual(s.expand(-s.diff(g,x3)-s.I*s.diff(g,x4)-z2**d), 0)

    def test_unit_direction_bounds(self):
        for d in range(1,25):
            for a in range(1,40):
                x,y=F(a,40),F(40-a,40)
                denom=x**d+y**d
                phase=(x**(d-1)+y**(d-1))/denom
                angular=(x*y)**(d-1)/denom**2
                self.assertGreaterEqual(phase,1)
                self.assertLessEqual(phase,2)
                self.assertLessEqual(angular,1)
                self.assertGreaterEqual(2**(d-1)*denom,1)

    def test_scale_exponents(self):
        # A first derivative of the unit torsion scales as epsilon^-1.
        self.assertEqual(4-4,0)
        self.assertEqual(4-2,2)
        self.assertGreater(F(4,9),F(16,81))


class SourcePreservationChecks(unittest.TestCase):
    def test_selected_guidance_hashes(self):
        receipt=json.loads((ROOT/'guidance/source/20260927_review_guidance_receipt.json').read_text())
        for record in receipt['records']:
            data=(ROOT/record['path']).read_bytes()
            self.assertEqual(len(data),record['bytes'])
            self.assertEqual(hashlib.sha256(data).hexdigest(),record['sha256'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
