#!/usr/bin/env python3
"""Finite algebra/scaling checks, not certification of the analytic theorems."""

from pathlib import Path
import hashlib
import unittest

import sympy as s

ROOT = Path(__file__).resolve().parents[1]
Q = s.Rational


class ConstantWeightChecks(unittest.TestCase):
    def setUp(self):
        self.beta, self.rho, self.w, self.j = s.symbols(
            "beta rho w j", positive=True
        )
        beta, rho, w, j = self.beta, self.rho, self.w, self.j
        self.c = 4 * (beta + 1) / (3 * beta)
        self.alpha = 9 * beta / (8 * (beta + 1) ** 2)
        self.d = 16 * (1 + 1 / beta) + (beta + 1) * w**2 - 9*rho**2 + 18*j
        self.d0 = Q(2, 3) * (4+w)*rho**2 - 2*rho**3
        self.coeff = rho + self.c/2 - (rho+self.c)**2/(2*self.c*(beta+1))

    def test_completed_identity(self):
        beta, rho, w, j = self.beta, self.rho, self.w, self.j
        c = self.c
        square = w - 4/beta - 3*(rho**2-c**2)/(c*(beta+1))
        rhs = self.d0/2 + c*j + (rho-c)**2*self.coeff
        rhs += c*(beta+1)*square**2/18
        self.assertEqual(s.factor(c*self.d/18-rhs), 0)

    def test_positivity_certificate(self):
        beta, rho = self.beta, self.rho
        cert = Q(2, 3) + beta*rho/(beta+1)*(1-3*rho/(8*(beta+1)))
        self.assertEqual(s.factor(self.coeff-cert), 0)
        self.assertEqual(s.factor(self.coeff.subs(rho, 0)), Q(2, 3))

    def test_full_weyl_completion(self):
        beta, rho, w, j = self.beta, self.rho, self.w, self.j
        el = s.symbols("e_lambda")
        current = (self.d0-2*el)/8
        fit = (w-2*self.alpha*rho**2)**2/6 + 2*self.alpha*el
        rhs = j + 4*current/self.c + (beta+1)*fit/3
        rhs += self.coeff*(rho-self.c)**2/self.c
        self.assertEqual(s.factor(self.d/18-rhs), 0)

    def test_model_normalization_and_wrong_half(self):
        # omega=sqrt(2)*psi/c; its model coefficient is t, not t/2.
        good = 2/(self.beta*self.c**2)
        self.assertEqual(s.factor(good-self.alpha), 0)
        self.assertNotEqual(s.factor(good/2-self.alpha), 0)

    def test_beta_two_rescaling(self):
        self.assertEqual(self.c.subs(self.beta, 2), 2)
        self.assertEqual(self.alpha.subs(self.beta, 2), Q(1, 4))
        self.assertEqual((4/self.c).subs(self.beta, 2), 2)

    def test_exterior_kinetic_payment(self):
        beta = self.beta
        target = Q(4, 9)*(1-1/beta-2/beta**2)
        self.assertEqual(s.factor(self.c-self.c**2/2-target), 0)
        self.assertEqual(6*Q(4, 9)**2, Q(32, 27))
        self.assertEqual(Q(8, 9)-4*Q(1, 6), Q(2, 9))

    def test_signed_endpoint_balance(self):
        rho, mass = Q(4, 3), Q(128, 81)
        k_coeff = -2/rho**3
        first = rho**3*Q(2, 9)
        second = 2*k_coeff*mass**2/8
        self.assertEqual(first, Q(128, 243))
        self.assertEqual(first+second, 0)

    def test_proof_has_no_hidden_control_characters(self):
        raw = (ROOT / "continuation/20260927_constant_weight_and_global_fit.md").read_bytes()
        self.assertFalse([b for b in raw if b < 32 and b not in (9, 10, 13)])

    def test_conformal_scalar_identity(self):
        u, lap, grad = s.symbols("u lap grad", positive=True)
        # Integrated cross term uses int (u-u^-1) Delta u
        # = int (1+u^-2)|du|^2; this check tests its coefficients.
        residual = 36*lap**2/u**2 + 16*(u**2-1)**2 + 48*(1+u**-2)*grad
        delta = 36*lap**2/u**2 + 48*u**-2*grad
        self.assertEqual(s.expand(residual-delta-16*(u**2-1)**2-48*grad), 0)

    def test_anisotropic_conformal_numerator(self):
        p, d, delta, t = s.symbols("p d delta t")
        actual = p-delta/12 + t*(d-(1+t)*delta)
        target = p+t*d-(Q(1, 12)+t+t*t)*delta
        self.assertEqual(s.expand(actual-target), 0)

    def test_new_endpoint_power(self):
        t = 1/self.beta
        self.assertEqual(s.factor(t*t*(1-2*t)**2-
                                 (self.beta-2)**2/self.beta**4), 0)
        self.assertEqual(s.factor(t*(1-2*t)**2-
                                 (self.beta-2)**2/self.beta**3), 0)

    def test_upper_wall_cancellation_and_rate(self):
        z, eps = s.symbols("z eps", real=True)
        h = (1-z*z)/3
        t = (1-2*z)/(8+2*z)
        k = (1+t)*(8*t-1)/2
        g = (4+z)**2/9
        self.assertEqual(s.factor(k*g+Q(3, 2)*(1+t)*(1-h)-9*t), 0)
        ts = t.subs(z, s.sqrt(1-3*(Q(1, 4)+eps)))
        self.assertEqual(s.limit(ts**2*(1-2*ts)**2/eps**2, eps, 0), Q(4, 9))


class CoreAndCouplingChecks(unittest.TestCase):
    def test_shell_beta_recurrence(self):
        a = s.symbols("a", positive=True)
        b2 = s.gamma(2-a)*s.gamma(a)/s.gamma(2)
        b3 = s.gamma(3-a)*s.gamma(a)/s.gamma(3)
        self.assertEqual(s.simplify(s.expand_func(2*b3-(2-a)*b2)), 0)

    def test_simple_zero_shell_constants(self):
        m1, m2 = s.symbols("m1 m2", positive=True)
        d = 1
        beta_value = 1
        quartic = 4*s.pi**2*d*d*(beta_value+1)*(m2*m2-m1*m1)
        mixed = 4*s.pi**2*d*d/3*((2-Q(1,d))*beta_value+1)*(m2**3-m1**3)
        self.assertEqual(s.expand(quartic-8*s.pi**2*(m2*m2-m1*m1)), 0)
        self.assertEqual(s.expand(mixed-Q(8, 3)*s.pi**2*(m2**3-m1**3)), 0)

    def test_split_scales(self):
        r, length, b, d = s.symbols("r L b d", positive=True)
        ell = r*length/(b*d)
        self.assertEqual(s.factor(d*d*ell**2-r*r*length**2/b**2), 0)
        self.assertEqual(s.factor(d*d*ell**4-r**4*length**4/(b**4*d**2)), 0)

    def test_nonexact_finite_shift_quartic(self):
        q1, q2 = s.symbols("q1 q2", positive=True)
        actual = 4*(q2*q2/(q1*q1)+q1*q1/(q2*q2)+2)
        self.assertEqual(s.factor(actual-16-4*(q2/q1-q1/q2)**2), 0)

    def test_curvature_action_cancellation(self):
        a, d, b1, b2 = s.symbols("a d b1 b2", real=True)
        ric = 2*(a-d)**2+8*(b1*b1+b2*b2)
        det = (a+d)**2
        x = a*a+b1*b1+b2*b2
        y = a*(a+d)
        self.assertEqual(s.expand(ric-2*det-8*(x-y)), 0)

    def test_no_free_sign_from_chern(self):
        xm, ym, xp, yp = s.symbols("xm ym xp yp")
        q_times_4pi2 = (xm-ym)-(xp-yp)
        self.assertEqual(s.expand(ym-xm+q_times_4pi2-(yp-xp)), 0)

    def test_guidance_bytes(self):
        source = ROOT / "guidance/source/20260927_unified_research_directive.zh.md"
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),
                         "5c796f18944bd3987dfd0e92f4c84ea1ff7c526dbe52b2c473cd29dcdab62244")


if __name__ == "__main__":
    unittest.main(verbosity=2)
