#!/usr/bin/env python3
"""Exact coefficient checks; not an existence or unique-continuation proof."""

import unittest
import sympy as s


class RelativeCellIdentities(unittest.TestCase):
    def test_two_scale_transfer_square(self):
        m,n,g=s.symbols('m n g',real=True)
        self.assertEqual(s.expand((m+n+6*g)**2+2*(m-2*n)**2
                         -9*(n-(m-2*g)/3)**2-2*(m+4*g)**2),0)

    def test_global_radial_moment_density(self):
        r = s.symbols('r', positive=True)
        f, phi, w = [s.Function(name)(r) for name in ('F','phi','w')]
        fp, pp, wp = s.diff(f,r), s.diff(phi,r), s.diff(w,r)
        ev = 1-s.diff(f,r,2)/2-5*fp/(2*r)
        eh = 1-fp/r+4*(1-f)/r**2
        d0 = ev+s.exp(2*phi)-1-3*f*s.diff(phi,r,2)-(2*fp+3*f/r)*pp
        d3 = ev+s.exp(2*phi)-1-f*s.diff(phi,r,2)-(2*fp+5*f/r)*pp-2*f*pp**2
        dh = eh+s.exp(2*phi)-1-f*s.diff(phi,r,2)-(fp+5*f/r)*pp-2*f*pp**2
        c = 4*(s.cosh(2*w)-1)/r**2
        z = 8*s.sinh(2*w)**2/(r**2*f)
        x = 2*(dh+c)-(d0-2*f*wp**2)-(d3-z)
        positive = 2*f*wp**2/r+2*c/r+z/r
        primitive = fp/r+4*f/r**2+2*f*pp/r
        self.assertEqual(s.simplify(x/r-s.diff(primitive,r)-8/r**3
                                   -positive+2*f*pp**2/r),0)

    def test_global_radial_residual_squares(self):
        a0,a3,ah,v = s.symbols('a0 a3 ah v')
        x,y,z = 2*ah-a0-a3,a0+a3+2*ah,a0-a3
        self.assertEqual(s.expand(a0*a0+a3*a3+2*ah*ah+2*v*v
                                 -(x*x+y*y)/4-z*z/2-2*v*v),0)

    def test_global_radial_boundary_and_threshold(self):
        mu,radius,p = s.symbols('mu R P', positive=True)
        boundary = 1+4/radius**2-2/mu+4/mu-4/radius**2
        self.assertEqual(s.simplify(boundary-1-2/mu),0)
        integral = (mu**-2-radius**-4)/4
        lower = (1+2/mu+p)**2/(4*integral)
        self.assertEqual(s.factor(lower-(mu+2+mu*p)**2/(1-mu**2/radius**4)),0)
        threshold = 1+2/mu*(1-s.sqrt(1-mu**2/radius**4))
        self.assertEqual(s.simplify((1+2/mu-threshold)**2/(4*integral)-4),0)

    def test_complete_exterior_defect_remainder(self):
        a, b, v, t, delta = s.symbols('a b v t delta', positive=True)
        c = 4*a+b
        r = c+t*t/(3*v)+delta
        k = 16*a*a/c+3*v
        remainder = (3*v*c+4*a*t)**2/(3*v*c)
        defect = 4-(-4*a+t)**2/((a+v)*r)
        lower = (4*a*b/c+v)/(a+v)
        self.assertEqual(s.factor(defect-lower-(k*delta+remainder)/((a+v)*r)), 0)

    def test_general_exterior_defect_remainder(self):
        a, b, v, t, delta, r, i = s.symbols('a b v t delta r i', positive=True)
        c = r+b
        total = c+t*t/(3*v)+delta
        k = i*i/c+3*v
        remainder = (3*v*c-i*t)**2/(3*v*c)
        ell = 4-i*i/(a*c)
        defect = 4-(i+t)**2/((a+v)*total)
        self.assertEqual(s.factor(defect-(a*ell+v)/(a+v)
                                 -(k*delta+remainder)/((a+v)*total)), 0)
        ext = 4-i*i/(a*r)
        self.assertEqual(s.factor(ell-ext-(4-ext)*b/(r+b)), 0)

    def test_localization_volume_threshold(self):
        a, q, d, h, theta, e = s.symbols('a q d h theta e')
        bound = 4*(q-d/(2*s.pi**2))/(a+q-d/s.pi**2)
        substitution = bound.subs({q:a*h,d:2*s.pi**2*a*h*theta}, simultaneous=True)
        self.assertEqual(s.factor(substitution-4*h*(1-theta)/(1+h-2*theta*h)),0)
        theta_star = (4-e*(1+h))/(4-2*e*h)
        self.assertEqual(s.factor(4*(1-theta_star)-e*(1+h-2*theta_star*h)),0)

    def test_relative_density(self):
        q, scalar2, weyl, d, total_scalar, volume = s.symbols(
            'q scalar2 weyl d total_scalar volume')
        ric = 8*s.pi**2*q+scalar2/3+4*weyl-4*d
        residual = ric+2*total_scalar+4*volume
        rhs = 8*s.pi**2*q+(scalar2+6*total_scalar+9*volume)/3+volume+4*weyl-4*d
        self.assertEqual(s.expand(residual-rhs), 0)

    def test_exact_dilution(self):
        volume, n, cost, trace = s.symbols('volume n cost trace', positive=True)
        ric = 4*volume+n*(cost-2*trace)
        total_scalar = -4*volume+n*trace
        defect = 4-total_scalar**2/(volume*ric)
        rhs = (4*n*cost-n**2*trace**2/volume)/ric
        self.assertEqual(s.factor(defect-rhs), 0)

    def test_first_order_and_balanced_ratio(self):
        eps, q, cost, trace, delta_v = s.symbols('eps q cost trace delta_v')
        volume = 2*s.pi**2+eps*delta_v
        defect = (4*eps*cost-eps**2*trace**2/volume)/(4*volume+eps*(cost-2*trace))
        self.assertEqual(s.simplify(s.limit(defect/(eps*q), eps, 0)
                                   -cost/(2*s.pi**2*q)), 0)
        self.assertEqual(s.Rational(8, 36), s.Rational(2, 9))
        self.assertEqual(s.Rational(7, 36)*4+s.Rational(2, 9), 1)

    def test_conformal_cell_lower_bound(self):
        d, t1, t2, k = s.symbols('d t1 t2 k')
        v = d-t2/2
        integral = -4*(d+s.pi*t1)
        lower = 8*s.pi**2*k-4*d+integral**2/(4*v)
        target = (8*s.pi**2*k+8*s.pi*t1+2*t2
                  +(2*s.pi*t1+t2)**2/v)
        self.assertEqual(s.factor(lower-target), 0)
        t = s.symbols('t')
        self.assertEqual(s.factor(lower.subs({k: 1, t1: t, t2: t**2})
                                   -2*d*(2*s.pi+t)**2/(d-t**2/2)), 0)

    def test_kahler_scalar_square(self):
        d, t1, t2, l = s.symbols('d t1 t2 l')
        v, integral = d-t2/2, -4*d-4*s.pi*t1
        scalar2 = l-8*integral-16*v
        self.assertEqual(s.expand(scalar2-(16*d+32*s.pi*t1+8*t2+l)), 0)

    def test_actual_nijenhuis_cancellation(self):
        kap, zr, zi, wr, wi = s.symbols('kap zr zi wr wi', real=True)
        z, w = zr+s.I*zi, wr+s.I*wi
        eta = [kap+z, -s.I*kap+s.I*z, -w, -s.I*w]
        # Evaluation of a conjugated one-form on Z1=e1-i e2, Z2=e3-i e4.
        self.assertEqual(s.simplify(s.conjugate(eta[0])-s.I*s.conjugate(eta[1])), 2*kap)
        self.assertEqual(s.simplify(s.conjugate(eta[2])-s.I*s.conjugate(eta[3])), 0)

    def test_triaxial_square_difference(self):
        e0, ea, e3, derivative, c, u, z = s.symbols('e0 ea e3 derivative c u z')
        difference = ((e0-2*derivative**2)**2+(ea+c+u)**2
                      +(ea+c-u)**2+(e3-z)**2-e0**2-2*ea**2-e3**2)
        expected = (-4*e0*derivative**2+4*derivative**4+4*ea*c
                    +2*c**2+2*u**2-2*e3*z+z**2)
        self.assertEqual(s.expand(difference-expected), 0)

    def test_bolt_and_core_energy(self):
        r, q, rc = s.symbols('r q rc', positive=True)
        f = 1+r**2/6-(q+q**2/2)/r**2+q**3/(3*r**4)
        self.assertEqual(s.simplify(f.subs(r, s.sqrt(q))), 0)
        self.assertEqual(s.simplify(s.diff(f, r).subs(r, s.sqrt(q))-2/s.sqrt(q)), 0)
        p = q*(q+2)/r**4
        cost = s.integrate(8*s.pi**2*p**2*r**3, (r, s.sqrt(q), rc))
        self.assertEqual(s.factor(cost-2*s.pi**2*(q+2)**2*(1-q**2/rc**4)), 0)

    def test_general_cell_squares_and_volume_window(self):
        scalar, weyl, t = s.symbols('scalar weyl t', real=True)
        density = (scalar+3)**2/3+1+2*weyl**2/3
        squares = (s.Rational(2, 27)*(-scalar+weyl)**2
                   +(scalar+4)**2/4+s.Rational(16, 27)*(weyl+scalar/8)**2)
        self.assertEqual(s.expand(density-squares), 0)
        # t=sqrt(v/d), on the branch t<=2.
        self.assertEqual(s.expand(-4+t**2+2*(2-t)**2-(t-2)*(3*t-2)), 0)
        self.assertEqual(s.simplify((-4+t**2+2*(2-t)**2).subs(t, s.Rational(4, 3))),
                         -s.Rational(4, 3))

    def test_bolt_scalar_and_positive_factorization(self):
        r, mu = s.symbols('r mu', positive=True)
        f = 1+r**2/6-(mu+mu**2/2)/r**2+mu**3/(3*r**4)
        factored = (r**2-mu)/r**2+(r**2-mu)**2*(r**2+2*mu)/(6*r**4)
        la = -s.diff(f, r)/r+4*(1-f)/r**2
        l0 = -s.diff(f, r, 2)/2-5*s.diff(f, r)/(2*r)
        p = mu*(mu+2)/r**4
        self.assertEqual(s.factor(f-factored), 0)
        self.assertEqual(s.factor(la+1-p), 0)
        self.assertEqual(s.factor(l0+1+p), 0)
        self.assertEqual(s.factor(2*la+2*l0+4), 0)

    def test_free_weyl_plane_with_independent_derivatives(self):
        xr = s.symbols('xr0:4', real=True)
        xi = s.symbols('xi0:4', real=True)
        yr = s.symbols('yr0:4', real=True)
        yi = s.symbols('yi0:4', real=True)
        x = [xr[j]+s.I*xi[j] for j in range(4)]
        y = [yr[j]+s.I*yi[j] for j in range(4)]
        d, e = s.symbols('d e', real=True)
        wedge = lambda a, b, i, j: a[i]*b[j]-a[j]*b[i]
        om2 = lambda a, b: wedge(a,b,0,2)+wedge(a,b,1,3)
        om3 = lambda a, b: wedge(a,b,0,3)-wedge(a,b,1,2)
        b22 = om2(xr,yr)+om2(xi,yi)
        b33 = om3(xr,yi)-om3(xi,yr)
        b23 = om3(xr,yr)+om3(xi,yi)
        b32 = om2(xr,yi)-om2(xi,yr)
        b1 = x[0]+s.I*x[1]
        c2 = y[2]+s.I*y[3]
        a21 = x[2]-s.I*x[3]
        a12 = y[0]-s.I*y[1]
        actual = s.re((d-s.I*e)*(s.conjugate(b1)*c2-s.conjugate(a21)*a12))
        self.assertEqual(s.expand(actual-d*(b22-b33)-e*(b23+b32)), 0)

    def test_dirac_polynomial_seeds(self):
        x = s.symbols('x1:5', real=True)
        z1, z2 = x[0]+s.I*x[1], x[2]+s.I*x[3]
        plus = lambda f, i: s.diff(f,x[2*i])+s.I*s.diff(f,x[2*i+1])
        minus = lambda f, i: s.diff(f,x[2*i])-s.I*s.diff(f,x[2*i+1])
        seeds = [(s.conjugate(z1*z2), x[0]**2+x[1]**2-x[2]**2-x[3]**2),
                 (s.Integer(0), s.conjugate(z2)**3/6)]
        torsions = []
        for h,g in seeds:
            self.assertEqual(s.simplify(plus(h,0)+minus(g,1)), 0)
            self.assertEqual(s.simplify(-plus(h,1)+minus(g,0)), 0)
            t = (plus(g,0), -plus(g,1))
            self.assertEqual(s.simplify(minus(t[1],1)-minus(t[0],0)), 0)
            self.assertEqual(s.simplify(-plus(t[1],0)-plus(t[0],1)), 0)
            torsions.append(t)
        self.assertEqual(s.simplify(minus(torsions[0][0],0)), 4)
        self.assertEqual(s.simplify(plus(plus(torsions[1][1],1),1)), -8)

    def test_coupled_almost_kahler_balance(self):
        d, m, v, n = s.symbols('d m v n', positive=True)
        direct = -4*d+(m+n)**2/(12*v)+(m-2*n)**2/(6*v)
        completed = -4*d+m**2/(6*v)+3*(n-m/3)**2/(4*v)
        self.assertEqual(s.factor(direct-completed), 0)
        roots = [(m-s.sqrt(48*d*v-2*m**2))/3,
                 (m+s.sqrt(48*d*v-2*m**2))/3]
        for root in roots:
            self.assertEqual(s.simplify(direct.subs(n,root)), 0)
        t = s.symbols('t', positive=True)
        difference = ((4*d-8*s.pi*t)**2
                      -(48*d*(d-t**2/2)-2*(4*d+4*s.pi*t)**2))
        self.assertEqual(s.expand(difference-(96*s.pi**2+24*d)*t**2), 0)
        a, b = s.symbols('a b', positive=True)
        self.assertEqual(s.factor(16*a+(b-4*a)**2/(v-a)-b**2/v
                                   -a*(b-4*v)**2/(v*(v-a))), 0)

    def test_descending_plateau_hessian(self):
        ell = s.symbols('ell', positive=True)
        x = s.symbols('x', real=True)
        f = s.sin(s.pi*x/ell)**2
        integral = s.integrate(s.diff(f,x,2)**2+4*s.diff(f,x)**2-16*f**2,
                               (x,0,ell))
        self.assertEqual(s.simplify(integral-(2*s.pi**4/ell**3+2*s.pi**2/ell-6*ell)),0)
        self.assertEqual(s.simplify(8*integral.subs(ell,s.pi)), -16*s.pi)
        z = s.symbols('z', positive=True)
        radius2 = 4/(1+z)
        self.assertEqual(s.factor(radius2**2*(1-z**2)-8*radius2*(1-z)
                                   +16*(1-z)/(1+z)), 0)

    def test_almost_kahler_scalar_boundary_identity(self):
        r = s.symbols('r', positive=True)
        f, w = s.Function('f')(r), s.Function('w')(r)
        scalar = -s.diff(f,r,2)-7*s.diff(f,r)/r+8*(1-f)/r**2
        boundary = r**3*s.diff(f,r)+4*r**2*(f-1)
        self.assertEqual(s.simplify(r**3*scalar+s.diff(boundary,r)), 0)
        change = (-2*f*s.diff(w,r)**2+8*(s.cosh(2*w)-1)/r**2
                  -8*s.sinh(2*w)**2/(r**2*f))
        torsion_half = 2*f*(s.diff(w,r)+2*s.sinh(2*w)/(r*f))**2
        divergence = 4*s.diff(r**2*(s.cosh(2*w)-1),r)/r**3
        self.assertEqual(s.simplify(change+torsion_half-divergence), 0)

    def test_coupled_conformal_trace(self):
        r,f,fp,fpp,p,pp,ep,wp,c,z = s.symbols('r f fp fpp p pp ep wp c z')
        ev = 1-fpp/2-5*fp/(2*r)
        eh = 1-fp/r+4*(1-f)/r**2
        d0 = ev+ep-1-3*f*pp-(2*fp+3*f/r)*p
        d3 = ev+ep-1-f*pp-(2*fp+5*f/r)*p-2*f*p**2
        dh = eh+ep-1-f*pp-(fp+5*f/r)*p-2*f*p**2
        actual = d0-2*f*wp**2+d3-z+2*(dh+c)
        scalar_k = 2*ev+2*eh-4-2*f*wp**2+2*c-z
        expected = scalar_k-6*(f*pp+(fp+3*f/r)*p)-6*f*p**2+4*ep
        self.assertEqual(s.expand(actual-expected), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
