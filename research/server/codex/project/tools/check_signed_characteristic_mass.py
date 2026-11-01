#!/usr/bin/env python3
"""Exact identities and an actual cell receipt; no PDE/existence certification."""

import json
import unittest

import numpy as np
import sympy as s
from scipy.integrate import quad
from scipy.optimize import brentq

from search_coupled_cell import product, step_jet


class Identities(unittest.TestCase):
    def test_conformal_radial_characteristic_primitive(self):
        r = s.symbols('r', positive=True)
        f, v = s.Function('F')(r), s.Function('v')(r)
        fp, vp, vpp = s.diff(f, r), s.diff(v, r), s.diff(v, r, 2)
        rv = -s.diff(f, r, 2)/2-5*fp/(2*r)
        rh = -fp/r+4*(1-f)/r**2
        a0 = rv-3*f*vpp-(2*fp+3*f/r)*vp
        a3 = rv-f*vpp-(2*fp+5*f/r)*vp-2*f*vp**2
        ah = rh-f*vpp-(fp+5*f/r)*vp-2*f*vp**2
        scalar = a0+a3+2*ah
        ric0 = a0*a0+a3*a3+2*ah*ah-scalar**2/4
        scalar_k = 2*(rv+rh)
        q = 2*f+r*fp/2+r*f*vp-2
        primitive = q*q+(2+q)*r*r*f*vp*vp
        density = r**3/4*(scalar**2/12+scalar_k**2/6-ric0)
        self.assertEqual(s.simplify(density-s.diff(primitive, r)), 0)

    def test_recovery_primitive_and_negative_mass(self):
        r, mu = s.symbols('r mu', positive=True)
        c = mu*(mu+2)
        f = 1+r*r/6-c/(2*r*r)+mu**3/(3*r**4)
        q = 2*f+r*s.diff(f, r)/2-2
        self.assertEqual(s.simplify(q-(r*r-c/r**2)/2), 0)
        self.assertEqual(s.simplify(q.subs(r, s.sqrt(mu))+1), 0)
        mass = c*c/(4*mu**2)-c/2+mu**2/4
        self.assertEqual(s.simplify(mass), 1)

    def test_minimum_second_variation(self):
        eps, a, b, d, z = s.symbols('eps a b d z', real=True)
        # q0=a(r-r*), first-order q shift=b eps; r-r*=z eps.
        energy = (a*z+b)**2+2*d
        self.assertEqual(s.simplify(energy.subs(z, -b/a)), 2*d)

    def test_kahler_characteristic_density(self):
        l1, l2 = s.symbols('l1 l2', real=True)
        scalar = 2*(l1+l2)
        p = (l1-l2)**2
        self.assertEqual(s.expand(scalar**2/4-p-4*l1*l2), 0)

    def test_pluricanonical_euler_difference(self):
        m, a, k, chi = s.symbols('m A k chi')
        h0 = a*m*(m-1)/2+chi
        euler = (a-k)*m*(m-1)/2+chi
        self.assertEqual(s.expand(h0-euler-k*m*(m-1)/2), 0)

    def test_csc_finite_moment_first_variation(self):
        v, p, dv, di, dr, t = s.symbols('V P dv di dr t')
        r = 4*v+p
        defect = 4-(-4*v+t*di)**2/((v+t*dv)*(r+t*dr))
        first = s.diff(defect, t).subs(t, 0)
        self.assertEqual(s.factor(first-4*(dr+2*di+4*dv)/r+4*p*dr/r**2), 0)

    def test_actual_torsion_shell_cutoff(self):
        m, t, dt, a, b = s.symbols('m t dt a b', positive=True)
        self.assertEqual(s.expand(((2*m*dt+t)**2-(2*m*dt-t)**2)/m-8*t*dt), 0)
        minimizer = (1/a-1/m)/(1/a-1/b)/s.sqrt(b)
        energy = s.integrate(12*s.pi**2*m*m*s.diff(minimizer, m)**2, (m, a, b))
        self.assertEqual(s.factor(energy-12*s.pi**2*a/(b-a)), 0)


def actual_cell(epsilon, mu=.01, radius=2.5):
    critical = (mu*(mu+2))**.25
    width = critical/3

    def values(r):
        ch = np.array([[1+r*r/6], [r/3], [1/3]])
        c = mu+mu*mu/2
        correction = np.array([[-c/r**2+mu**3/(3*r**4)],
                               [2*c/r**3-4*mu**3/(3*r**5)],
                               [-6*c/r**4+20*mu**3/(3*r**6)]])
        cutoff = -step_jet(np.array([r]), 1., 2.)
        cutoff[0] += 1
        f, fp, fpp = (ch+product(correction, cutoff))[:, 0]
        x = r-critical
        t = x/width
        if abs(t) < 1:
            z = 1-t*t
            bump = np.exp(1-1/z)
            lp = -2*t/(width*z*z)
            lpp = -2*(1+3*t*t)/(width*width*z**3)
            v = epsilon*x*bump
            vp = epsilon*bump*(1+x*lp)
            vpp = epsilon*bump*(2*lp+x*(lp*lp+lpp))
        else:
            v = vp = vpp = 0.
        rv = -fpp/2-5*fp/(2*r)
        rh = -fp/r+4*(1-f)/r**2
        a0 = rv-3*f*vpp-(2*fp+3*f/r)*vp
        a3 = rv-f*vpp-(2*fp+5*f/r)*vp-2*f*vp*vp
        ah = rh-f*vpp-(fp+5*f/r)*vp-2*f*vp*vp
        scalar = a0+a3+2*ah
        p = a0*a0+a3*a3+2*ah*ah-scalar*scalar/4
        density = r**3/4*(scalar*scalar/12+(2*rv+2*rh)**2/6-p)
        cost = r**3*((a0+np.exp(2*v))**2+(a3+np.exp(2*v))**2
                     +2*(ah+np.exp(2*v))**2)
        q = 2*f+r*fp/2+r*f*vp-2
        primitive = q*q+(2+q)*r*r*f*vp*vp
        return density, cost, primitive

    edges = sorted(set([np.sqrt(mu), critical-width, critical+width, 1., 2., radius]))
    grid = np.unique(np.r_[np.linspace(np.sqrt(mu), radius, 20001), edges])
    roots = []
    previous = values(grid[0])[0]
    for left, right in zip(grid[:-1], grid[1:]):
        current = values(right)[0]
        if previous*current < 0:
            roots.append(brentq(lambda r: values(r)[0], left, right, xtol=1e-14))
        previous = current
    integration_edges = sorted(set(edges+roots))
    negative = cost = total = 0.
    for left, right in zip(integration_edges[:-1], integration_edges[1:]):
        negative += quad(lambda r: max(-values(r)[0], 0.), left, right,
                         epsabs=1e-11, epsrel=1e-11)[0]
        total += quad(lambda r: values(r)[0], left, right,
                      epsabs=1e-11, epsrel=1e-11)[0]
        cost += quad(lambda r: values(r)[1], left, right,
                     epsabs=1e-10, epsrel=1e-10)[0]
    return {'mu': mu, 'radius': radius, 'epsilon': epsilon,
            'negative_characteristic_mass': negative,
            'J_over_2pi2': cost, 'sample_bracketed_density_roots': roots,
            'primitive_at_roots': [values(r)[2] for r in roots],
            'total_characteristic_error': total-(radius**4/4-1),
            'scope': 'Actual smooth conformally Kahler cell; numerical integration, not a universal bound.'}


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Identities)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
    for epsilon in (0., .01, .02):
        print(json.dumps(actual_cell(epsilon), sort_keys=True))
