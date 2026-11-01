#!/usr/bin/env python3
"""Finite identities only; not harmonic compactness or a gluing certificate."""

import json
import itertools
from pathlib import Path
import unittest
import sympy as s


class MarkedSliceIdentities(unittest.TestCase):
    def test_euler_energy_rearrangement(self):
        p, scalar, variance, weyl = s.symbols("p scalar variance weyl")
        ric = p+scalar/4
        e = (4*p+variance)/ric
        euler = weyl+scalar/24-p/2
        self.assertEqual(s.expand(euler-(weyl+ric/6-2*p/3)), 0)
        self.assertEqual(s.factor(
            euler-(1-e)*ric/6-(weyl+variance/6)), 0)

    def test_partial_cap_identity(self):
        a, h, scalar, b, bn, kp, cp, variance = s.symbols(
            "a h scalar b bn kp cp variance")
        scalar0 = 32*s.pi**2*a
        p = 8*s.pi**2*(a*h-6*b)+(scalar-scalar0)/12+4*(bn+kp-cp)
        ric = p+scalar/4
        lhs = (1+h)*(4*p+variance)-4*h*ric
        rhs = ((1-3*h)*(scalar-scalar0)/3+16*(bn+kp-cp)
               +(1+h)*variance-192*s.pi**2*b)
        self.assertEqual(s.expand(lhs-rhs), 0)
        loss = (192*s.pi**2*b+16*cp)/(8*s.pi**2*a*(1+h)**2)
        self.assertEqual(s.factor(loss-(24*b+2*cp/s.pi**2)
                                  /(a*(1+h)**2)), 0)

    def test_bernstein_quotient_at_a_maximum(self):
        # At grad(w/d)=0, grad(w)=(w/d)grad(d).
        w, d, grad_d2 = s.symbols("w d grad_d2", positive=True)
        cross = 2*(w/d)*grad_d2/d**2-2*w*grad_d2/d**3
        self.assertEqual(s.simplify(cross), 0)
        # The negative term from Ld >= c*w-C*v has the required power.
        c, f = s.symbols("c f", positive=True)
        self.assertEqual(s.simplify((-c*w*w/d**2).subs(w, f*d)
                                   + c*f*f), 0)

    def test_result_identifiers_and_dependencies_are_unique(self):
        root = Path(__file__).resolve().parents[1]
        entries = json.loads((root / "catalog/results.json").read_text())["results"]
        identifiers = [entry["id"] for entry in entries]
        self.assertEqual(len(identifiers), len(set(identifiers)))
        for entry in entries:
            self.assertTrue(set(entry.get("depends_on", [])) <= set(identifiers))

    def test_exact_bianchi_harmonic_identity(self):
        # Normal coordinates for the source. No closeness of target q is used.
        q = s.Matrix([[3, 1, 0, 0], [1, 2, 0, 0],
                      [0, 0, 4, 1], [0, 0, 1, 2]])
        inv = q.inv()
        dq = [[[s.Rational((a + 1) * (i + j + 2), 7)
                for j in range(4)] for i in range(4)] for a in range(4)]
        beta = s.Matrix([
            -sum(dq[i][i][l] for i in range(4))
            + sum(dq[l][i][i] for i in range(4))/2
            for l in range(4)
        ])
        tension = s.Matrix([
            sum(inv[k, l]*(2*dq[i][i][l]-dq[l][i][i])/2
                for i in range(4) for l in range(4))
            for k in range(4)
        ])
        self.assertEqual(tension + inv*beta, s.zeros(4, 1))

    def test_unfixed_weyl_block_in_transgression(self):
        c = [s.eye(2), s.diag(s.I, -s.I),
             s.Matrix([[0, 1], [-1, 0]]),
             s.Matrix([[0, -s.I], [-s.I, 0]])]
        u = [s.Matrix([1, 0]), s.Matrix([-s.I, 0]),
             s.Matrix([0, 1]), s.Matrix([0, -s.I])]
        omega = [{(0, 1): 1, (2, 3): -1},
                 {(0, 2): 1, (1, 3): 1},
                 {(0, 3): 1, (1, 2): -1}]
        cliff = [sum((-c[i]*c[j].conjugate().T*v
                      for (i, j), v in form.items()), s.zeros(2))
                 for form in omega]
        curvature = {p: (-omega[1].get(p, 0)*cliff[1]
                         + omega[2].get(p, 0)*cliff[2])/4
                     for p in itertools.combinations(range(4), 2)}
        contraction = 0
        for perm in itertools.permutations(range(4)):
            i, j, k, ell = perm
            if j > k:
                continue
            inversions = sum(perm[a] > perm[b] for a in range(4)
                             for b in range(a+1, 4))
            contraction += (-1)**inversions*(
                u[i].conjugate().T*curvature[j, k]*u[ell])[0]
        self.assertEqual(s.simplify(s.re(contraction)), 4)
        self.assertEqual(sum((c[i].conjugate().T*u[i]
                              for i in range(4)), s.zeros(2, 1)), s.zeros(2, 1))
        principal = s.Matrix(2, 2, lambda b, k:
            sum(c[i].conjugate().T[0, b]*u[i][k] for i in range(4)))
        self.assertEqual(principal, s.zeros(2))

    def test_conformal_defect_identity(self):
        p, r, d, ell = s.symbols("p r d ell", positive=True)
        e0 = 4*p/r
        e1 = (4*p+d/3+ell)/(r+d/3)
        self.assertEqual(s.factor(
            e1-e0-((1-e0)*d/3+ell)/(r+d/3)), 0)
        # An explicit weighted average explains the lower bound by min(e0,1).
        self.assertEqual(s.factor(
            e1-(e0*r+d/3)/(r+d/3)-ell/(r+d/3)), 0)

    def test_schwarzschild_potential(self):
        lam, v = s.symbols("lam v", real=True)
        sigma = 1-v*v
        matrix = s.Matrix([[lam+4, -2*s.sqrt(lam)*v],
                           [-2*s.sqrt(lam)*v, lam-2*sigma]])
        self.assertEqual(s.factor((matrix-s.eye(2)).det()
                         -(lam-3)*(lam+3-2*v*v)), 0)
        for eig in (3, 8, 15, 24):
            for value in (s.Rational(-1), s.Rational(-1, 2),
                          s.Rational(0), s.Rational(1, 2), s.Rational(1)):
                test = (matrix-s.eye(2)).subs({lam: eig, v: value})
                self.assertGreaterEqual(test[0, 0], 0)
                self.assertGreaterEqual(test[1, 1], 0)
                self.assertGreaterEqual(test.det(), 0)

    def test_schwarzschild_radial_transform(self):
        # rho'/rho=v, v'=sigma, with integration by parts of -4v*z*z'.
        lam, v, sig = s.symbols("lam v sig")
        # (z'-2vz)^2 contributes 2*sigma*z² after integration by parts.
        potential = 4*v*v+2*sig+lam+2*sig
        self.assertEqual(s.expand(
            potential.subs(sig, 1-v*v)-(lam+4)), 0)
        tangential = 4*v*v+2*sig+lam-4
        self.assertEqual(s.expand(
            tangential.subs(sig, 1-v*v)-(lam-2*(1-v*v))), 0)

    def test_warped_scalar_equation(self):
        a, ap, b, bp = s.symbols("a ap b bp")
        r = s.symbols("r", positive=True)
        # Logarithmic derivatives of the three warp factors are a,-a,b.
        # Scalar = -2(sum(alpha_i' + alpha_i^2)
        #               + sum_{i<j} alpha_i alpha_j).
        scalar = -2*((ap+a*a)+(-ap+a*a)+(bp+b*b)
                     -a*a+a*b-a*b)
        self.assertEqual(s.expand(
            scalar.subs(bp, 2*r*r-a*a-b*b)+4*r*r), 0)

    def test_slab_exponents(self):
        p = s.Rational(7, 4)
        self.assertGreater(p, 0)       # C0 amplitude
        self.assertGreater(2*p-1, 0)   # integrated ODE source
        self.assertGreater(2*p-3, 0)   # L2 curvature energy
        self.assertLess(p-2, 0)        # curvature supremum

    def test_valid_cluster_scale_hierarchy(self):
        # R=t, d=t², r=t³, a=t⁷, as t decreases to zero.
        outer, separation, cutoff, donor = 1, 2, 3, 7
        self.assertGreater(separation, outer)
        self.assertGreater(cutoff, separation)
        self.assertGreater(donor, 2*cutoff)

    def test_endpoint_phase_constants(self):
        rho, mass = s.Rational(4, 3), s.Rational(128, 81)
        weight = rho**3/(2*mass)
        lam = 4*mass/rho**6
        self.assertEqual(weight, s.Rational(3, 4))
        self.assertEqual(lam, s.Rational(9, 8))
        q2 = mass**2/8
        algebraic = s.Rational(2, 3)*weight**2*q2
        algebraic += s.Rational(3, 2)*lam*weight**3*mass*q2
        self.assertEqual(algebraic, s.Rational(1024, 2187))

    def test_opposite_clifford_anchor(self):
        c = [s.eye(2), s.diag(s.I, -s.I),
             s.Matrix([[0, 1], [-1, 0]]),
             s.Matrix([[0, -s.I], [-s.I, 0]])]
        omega = -c[0]*c[1].conjugate().T+c[2]*c[3].conjugate().T
        e1 = s.Matrix([1, 0])
        self.assertEqual(omega*e1, 2*s.I*e1)
        mass = s.symbols("mass", positive=True)
        self.assertEqual((-s.I*mass/4*omega)*e1, mass/2*e1)

    def test_negative_torsion_index_seed(self):
        x = s.symbols("x1:5", real=True)
        x1, x2, x3, x4 = x
        h = 2*x2*x4-s.I*(x1*x4+3*x2*x3)
        g = (x1*x1+x2*x2-3*x3*x3+x4*x4)/2
        c = [s.eye(2), s.diag(s.I, -s.I),
             s.Matrix([[0, 1], [-1, 0]]),
             s.Matrix([[0, -s.I], [-s.I, 0]])]
        seed = s.Matrix([h, g])
        d_plus = sum((c[i]*seed.diff(x[i]) for i in range(4)),
                     s.zeros(2, 1))
        self.assertEqual(s.simplify(d_plus), s.zeros(2, 1))
        torsion = s.Matrix([s.diff(g, x1)+s.I*s.diff(g, x2),
                            -s.diff(g, x3)-s.I*s.diff(g, x4)])
        real = s.Matrix([s.re(torsion[0]), s.im(torsion[0]),
                         s.re(torsion[1]), s.im(torsion[1])])
        self.assertEqual(real.jacobian(x).det(), -3)


if __name__ == "__main__":
    unittest.main()
