#!/usr/bin/env python3
"""Finite identities and source hygiene only; not PDE/gluing certification."""

from pathlib import Path
import re
import unittest

import sympy as s


ROOT = Path(__file__).resolve().parents[1]
R = s.Rational


class EndpointIdentities(unittest.TestCase):
    def test_scalar_polynomial_at_endpoint(self):
        rho = R(4, 3)
        self.assertEqual(2*rho**3-rho**4, R(128, 81))

    def test_reciprocal_decomposition(self):
        rho, mass, total, base = s.symbols("rho mass total base", positive=True)
        lam = 4*mass/base**6
        self.assertEqual(s.factor(
            2-lam*rho**6/total
            -2*(total-2*mass)/total-lam*(base**6-rho**6)/total), 0)

    def test_weight_derivative(self):
        rho, k, mass = s.symbols("rho k mass", positive=True)
        total = mass+2*rho**2*k
        weight = rho**4/total
        self.assertEqual(s.factor(s.diff(weight, rho)
                         -4*rho**3*(mass+rho**2*k)/total**2), 0)
        # dk = 2 Re<Pi,H>.
        self.assertEqual(s.factor(2*s.diff(weight, k)
                                  +4*rho**6/total**2), 0)

    def test_radial_hopf_derivative_survives(self):
        mass, base, rho = s.symbols("mass base rho", positive=True)
        a = rho**3/(base+mass)
        # a J+ dm + m J- da; normalize by a.
        self.assertEqual(s.factor(mass*s.diff(a, mass)/a
                                  +mass/(base+mass)), 0)
        self.assertEqual((mass/(base+mass)).subs(mass, base), R(1, 2))

    def test_simple_zero_shell_constants(self):
        r, ell, m1, m2 = s.symbols("r ell m1 m2", positive=True)
        bounds = (r, ell*s.sqrt(m1), ell*s.sqrt(m2))
        phase_curvature = s.integrate(4/r**4*2*s.pi**2*r**3, bounds)
        mixed = s.integrate(4/r**2*3/r**2*2*s.pi**2*r**3, bounds)
        phase = s.integrate(1/r**2*2*s.pi**2*r**3, bounds)
        self.assertEqual(s.simplify(s.expand_log(
            phase_curvature-4*s.pi**2*s.log(m2/m1), force=True)), 0)
        self.assertEqual(s.simplify(s.expand_log(
            mixed-12*s.pi**2*s.log(m2/m1), force=True)), 0)
        self.assertEqual(s.factor(phase-s.pi**2*ell**2*(m2-m1)), 0)


class SurgeryIdentities(unittest.TestCase):
    def test_conformal_limit_comparison(self):
        p, ric, delta, cost, variance = s.symbols("p ric delta cost variance")
        alpha = 4*(p+cost)/(ric+cost)
        raw = (4*(p+delta/12+cost)+variance)/(ric+delta/3+cost)
        rhs = ((1-alpha)*delta/3+variance)/(ric+delta/3+cost)
        self.assertEqual(s.factor(raw-alpha-rhs), 0)

    def test_two_exact_sharp_remainders(self):
        b0, p, wm, h, variance = s.symbols("b0 p wm h variance")
        ric = b0+4*p-12*wm
        scalar = 4*b0+12*p-48*wm
        raw = (4*(p+b0*h)+variance)/(ric+b0*h)
        n1 = 4*(1-3*h)*p+48*h*wm+(1+h)*variance
        n2 = (1-3*h)*(scalar-4*b0)/3+16*wm+(1+h)*variance
        den = (1+h)*(ric+b0*h)
        self.assertEqual(s.factor(raw-4*h/(1+h)-n1/den), 0)
        self.assertEqual(s.factor(n1-n2), 0)

    def test_background_penalty(self):
        b0, p, h = s.symbols("b0 p h")
        lower = 4*(p+b0*h)/(b0*(1+h)+4*p)
        penalty = 4*(1-3*h)*p/((1+h)*(b0*(1+h)+4*p))
        self.assertEqual(s.factor(lower-4*h/(1+h)-penalty), 0)

    def test_first_order_penalties(self):
        h, a, p, b, delta, variance = s.symbols(
            "h a p b delta variance", positive=True)
        q = a*h
        ric_hat = 8*s.pi**2*a+(4*p-12*b)*q
        alpha = 4*(p+8*s.pi**2)*q/(ric_hat+8*s.pi**2*q)
        raw = (4*(p+delta/12+8*s.pi**2)+variance)*q
        raw /= ric_hat+(delta/3+8*s.pi**2)*q
        self.assertEqual(s.simplify(s.limit(alpha/h, h, 0)
                         -4-p/(2*s.pi**2)), 0)
        self.assertEqual(s.simplify(s.limit(raw/h, h, 0)
                         -4-p/(2*s.pi**2)-delta/(24*s.pi**2)
                         -variance/(8*s.pi**2)), 0)

    def test_identification_conformal_cancellation(self):
        phi = s.symbols("phi")
        z = s.diag(1, 2, 3, -6)
        velocity = 2*phi*s.eye(4)
        correction = -(velocity*z+z*velocity)/2+s.trace(velocity)*z/4
        self.assertEqual(correction, s.zeros(4))

    def test_conformal_scalar_difference_equation(self):
        u, e = s.symbols("u e")
        self.assertEqual(s.expand((-4+e)*u+4*u**3
                         -4*u*(u+1)*(u-1)-e*u), 0)

    def test_gradient_scalar_coefficient(self):
        scalar = -4
        self.assertEqual(R(1, 12)*(-2*scalar), R(2, 3))
        # Covariant Bach weight -2, norm weight -2, volume weight +4.
        self.assertEqual(-2-2+4, 0)

    def test_scalar_loss_without_conformal_supremum(self):
        scalar, integral, volume = s.symbols("S I V", positive=True)
        residual = scalar+8*integral+16*volume
        variance = scalar-integral**2/volume
        self.assertEqual(s.factor(residual-variance
                                  -(integral+4*volume)**2/volume), 0)

    def test_identified_first_variation(self):
        z = s.Matrix([[1, 2, 0, 1], [2, -1, 1, 0],
                      [0, 1, 3, 2], [1, 0, 2, -3]])
        velocity = s.Matrix([[2, 1, 0, 0], [1, 0, 2, 0],
                             [0, 2, 1, 1], [0, 0, 1, -1]])
        dz = s.diag(3, 1, -2, 4)
        identified = (dz-(velocity*z+z*velocity)/2
                      +s.trace(velocity)*z/4)
        direct = (2*s.trace(z*dz)-2*s.trace(velocity*z*z)
                  +s.trace(velocity)*s.trace(z*z)/2)
        self.assertEqual(2*s.trace(z*identified)-direct, 0)

    def test_tt_remainder_scale(self):
        h, a0 = s.symbols("h a0", positive=True)
        # Dividing a*sqrt(Q)+a^2*sqrt(A) by sqrt(Q), Q=A*h.
        expression = a0+a0**2/s.sqrt(h)
        self.assertEqual(s.simplify(expression.subs(a0, s.sqrt(h))
                                    -2*s.sqrt(h)), 0)
        e = s.symbols("e", positive=True)
        self.assertEqual(s.simplify(expression.subs(a0, e*h**R(1, 4))
                                    -e*h**R(1, 4)-e**2), 0)

    def test_complex_hyperbolic_curvature_action(self):
        j = s.Matrix([[0, -1, 0, 0], [1, 0, 0, 0],
                      [0, 0, 0, -1], [0, 0, 1, 0]])
        basis = []
        for row in range(4):
            for col in range(row, 4):
                value = s.zeros(4)
                value[row, col] = value[col, row] = 1
                basis.append(value)
        def action(value):
            return -(s.trace(value)*s.eye(4)-value+3*j.T*value*j)/6
        for value in basis:
            trace = s.trace(value)*s.eye(4)/4
            hermitian = (value+j.T*value*j)/2-trace
            antihermitian = (value-j.T*value*j)/2
            self.assertEqual(action(trace), -trace)
            self.assertEqual(action(hermitian), -hermitian/3)
            self.assertEqual(action(antihermitian), 2*antihermitian/3)
        # Classical Koiso identity has lower-order term (I-R_action).
        self.assertEqual(min(1-ev for ev in [-1, -R(1, 3), R(2, 3)]),
                         R(1, 3))

    def test_square_completion_and_chiral_conversion(self):
        x, q, a, c = s.symbols("x q a c", positive=True)
        expression = x**2/2-c*a*s.sqrt(q)*x
        completed = (x-c*a*s.sqrt(q))**2/2-c**2*a**2*q/2
        self.assertEqual(s.expand(expression-completed), 0)
        h, u, y = s.symbols("h u y", positive=True)
        relative = 4*y/(u+4*h*y)
        self.assertEqual(s.factor(s.diff(relative, y)
                                  -4*u/(u+4*h*y)**2), 0)
        e = s.symbols("e")
        # E/h=4q/(U+4hq) -> q=EU/[4h(1-E)].
        self.assertEqual(s.factor(
            relative.subs(y, e*u/(4*h*(1-e)))-e/h), 0)

    def test_weighted_gauge_and_inverse_conformal_scales(self):
        h = s.symbols("h", positive=True)
        amplitude, frequency = h, h**(-R(2, 3))
        gauge_over_sqrt_q = amplitude*frequency**2/s.sqrt(h)
        self.assertEqual(s.simplify(gauge_over_sqrt_q-h**(-R(5, 6))), 0)
        self.assertEqual(s.simplify(
            amplitude*gauge_over_sqrt_q-h**R(1, 6)), 0)
        v, lap = s.symbols("v lap", positive=True)
        scalar = -6*lap/v-4*v**2
        self.assertEqual(s.expand(scalar**2-16*v**4
                                  -36*(lap/v)**2-48*v*lap), 0)
        self.assertEqual(s.factor(v**4*(v**(-2)-1)**2
                                  -(1-v**2)**2), 0)

    def test_concentrated_tt_critical_scaling(self):
        ell, h = s.symbols("ell h", positive=True)
        # Fourth-order Bach seed normalization, then second-order Ricci.
        self.assertEqual(ell**4*ell**(-4), 1)
        self.assertEqual((ell**(-2))**2*ell**4, 1)
        amplitude = h**R(3, 4)
        self.assertEqual(s.simplify(amplitude**2/h-h**R(1, 2)), 0)
        self.assertEqual(s.simplify(amplitude*h**(-2)-h**(-R(5, 4))), 0)

    def test_sixth_order_seed(self):
        x = s.symbols("x")
        for order in range(6):
            self.assertEqual(s.diff(x**6, x, order).subs(x, 0), 0)
        self.assertEqual(s.diff(x**6, x, 6), 720)

    def test_escape_constant_and_alignment(self):
        sigma = s.symbols("sigma", positive=True)
        cost = 8*s.pi**2*(1-s.sqrt(1-sigma/4))**2
        self.assertEqual(s.limit(cost/sigma**2, sigma, 0), s.pi**2/8)
        norm, cross = s.symbols("norm cross")
        # P_final - P_base <= -2*pi^2*sigma*Q gives this signed bound.
        self.assertEqual(s.expand(
            (2*cross+norm+2*s.pi**2*sigma)/2
            -(cross+norm/2+s.pi**2*sigma)), 0)


class DocumentHygiene(unittest.TestCase):
    def test_source_integrity(self):
        path = ROOT/"continuation/20260927_endpoint_covariance_and_surgery_limits.md"
        raw = path.read_bytes()
        self.assertFalse([b for b in raw if b < 32 and b not in (9, 10, 13)])
        text = raw.decode()
        self.assertEqual(text.count(r"\["), text.count(r"\]"))
        self.assertEqual(text.count(r"\("), text.count(r"\)"))
        self.assertNotIn(r"\\)", text)
        self.assertFalse(re.search(r"\]\\\([^)]*\.md", text))
        self.assertIn("Neither the unrestricted weak", text)
        self.assertIn("does not establish positivity in every reduced TT", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
