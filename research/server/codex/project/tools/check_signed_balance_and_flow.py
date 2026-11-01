#!/usr/bin/env python3
"""Finite algebra checks; not certification of PDE existence or compactness."""

from fractions import Fraction as F
import unittest

import sympy as s


class FlowChecks(unittest.TestCase):
    def test_defect_derivative(self):
        P,V,G = s.symbols('P V G', positive=True)
        alpha = 4*P/(P+4*V)
        Pdot = -2*G-P**2/V
        actual = s.diff(alpha,P)*Pdot-s.diff(alpha,V)*P
        expected = -2*(4-alpha)*G/(P+4*V)
        self.assertEqual(s.simplify(actual-expected), 0)
        self.assertEqual(s.simplify(-expected/alpha-(4-alpha)*G/(2*P)), 0)

    def test_pressure_and_gradient_cancellation(self):
        P,V,N,Rm = s.symbols('P V N Rm')
        b = P/(4*V)
        inner = N-2*Rm-2*b*P
        self.assertEqual(s.expand(-2*inner-P**2/V+2*N-4*Rm), 0)
        q = s.Rational(1,3)-2*b
        self.assertEqual(s.simplify(-2*q*P-P**2/V+2*P/3), 0)

    def test_normalized_walls(self):
        y,p,U,h,mu = s.symbols('y p U h mu')
        alpha = 4*p/(p+4*y)
        kappa = 4*mu/(4-mu)
        self.assertEqual(s.simplify(alpha.subs(p,kappa*y)-mu), 0)
        self.assertEqual(s.expand((p+4*y-4*(1+h)).subs(p,4*(1+h-y))), 0)
        self.assertEqual(s.expand((p-4*y/3+4*U/3).subs(p,4*(y-U)/3)), 0)

    def test_crossings(self):
        h,mu,U,bbar = s.symbols('h mu U bbar', positive=True)
        k = 4*mu/(4-mu)
        lo = (1+h)*(1-mu/4)
        hi = U*(4-mu)/(4*(1-mu))
        top = U/(1-3*bbar)
        self.assertEqual(s.simplify(k*lo-4*(1+h-lo)), 0)
        self.assertEqual(s.simplify(k*hi-4*(hi-U)/3), 0)
        gap=3*U*(4*bbar-bbar*mu-mu)/(4*(3*bbar-1)*(mu-1))
        self.assertEqual(s.simplify(top-hi-gap), 0)

    def test_antiderivatives(self):
        y,h,U,mu = s.symbols('y h U mu', positive=True)
        pairs = [(-s.log(1+h-y)/4, 1/(4*(1+h-y))),
                 ((4-mu)*s.log(y)/(4*mu), (4-mu)/(4*mu*y)),
                 (s.Rational(3,4)*s.log(y-U), 3/(4*(y-U)))]
        for primitive,target in pairs:
            self.assertEqual(s.simplify(s.diff(primitive,y)-target), 0)

    def test_asymptotic_lifetime(self):
        h,c = s.symbols('h c', positive=True)
        d,q = s.symbols('d q', real=True)
        U,mu,bbar = 1+h+d*h*h,c*h,h+q*h*h
        first = s.log(4*h/((1+h)*mu))/4
        middle = (4-mu)/(4*mu)*s.log(U/((1-mu)*(1+h)))
        last = s.Rational(3,4)*s.log(4*bbar*(1-mu)/(mu*(1-3*bbar)))
        self.assertEqual(s.limit(first,h,0), s.log(4/c)/4)
        self.assertEqual(s.limit(middle,h,0), 1)
        self.assertEqual(s.limit(last,h,0), 3*s.log(4/c)/4)

    def test_initial_slack(self):
        h = s.symbols('h', positive=True)
        alpha = 4*h/(1+h)+h*h
        bbar = alpha/(4-alpha)
        self.assertEqual(s.limit((bbar-h)/h**2,h,0), s.Rational(1,4))

    def test_wall_selection_rational_samples(self):
        for c in [F(1,4), F(1), F(2), F(3)]:
            h = F(1,10000)
            mu,U,bbar = c*h,1+h+h*h,h+h*h
            kappa = 4*mu/(4-mu)
            lo,hi,top = (1+h)*(1-mu/4),U*(4-mu)/(4*(1-mu)),U/(1-3*bbar)
            self.assertTrue(1 < lo < hi < top)
            for left,right,index in [(F(1),lo,1),(lo,hi,0),(hi,top,2)]:
                y=(left+right)/2
                walls=[kappa*y,4*(1+h-y),F(4,3)*(y-U)]
                self.assertEqual(max(walls),walls[index])

    def test_tube_rate(self):
        q = F(1,3)-2*F(1,24)
        # H/P <=2 gives sqrt(8H/(9P)) <=4/3.
        rate=F(3,2)*(q-F(4,3)*F(1,32))
        self.assertEqual(rate,F(5,16))
        self.assertGreater(rate,F(1,4))


class ActualDeformationChecks(unittest.TestCase):
    def test_signed_polynomial(self):
        x,T = s.symbols('x T')
        K=4*x*(1-x)
        gamma=8*x*x*(1-x)-T
        L0=s.Rational(2,3)*(1-x)**2*(1+8*x-2*x*x)
        expected=T-s.Rational(2,3)*(1-x*x)*(1+2*x*x)
        self.assertEqual(s.expand(K-gamma-L0-expected),0)

    def test_regular_solution_completion(self):
        rho,K,d = s.symbols('rho K d')
        completed=K-rho+rho**2/8+2+d/2
        self.assertEqual(s.expand(completed-K-(rho-4)**2/8-d/2),0)

    def test_mixed_connection_norm(self):
        a,b,v,w=s.symbols('a b v w',real=True)
        H=s.zeros(4)
        H[0,0],H[0,1],H[1,0],H[1,1]=a,b,b,-a
        deriv=[s.zeros(4),s.zeros(4),v*H,w*H]
        omega=s.zeros(4)
        omega[0,1]=omega[2,3]=1
        omega[1,0]=omega[3,2]=-1
        christ=lambda i,j,k:(deriv[i][j,k]+deriv[j][i,k]-deriv[k][i,j])/2
        val=0
        for i in range(4):
            for j in range(4):
                for k in range(j+1,4):
                    cov=-sum(christ(i,j,l)*omega[l,k]+christ(i,k,l)*omega[j,l] for l in range(4))
                    val+=cov**2
        self.assertEqual(s.expand(val-(a*a+b*b)*(v*v+w*w)),0)
        self.assertEqual(s.expand(val-s.trace(H.T*H)*(v*v+w*w)/2),0)

    def test_compensation_ratios(self):
        lam=s.symbols('lam',positive=True)
        FoverK=(lam+2)/4
        DoverK=18*FoverK
        self.assertEqual(s.simplify(1/(lam+DoverK)-2/(11*lam+18)),0)
        self.assertEqual(s.limit(1/FoverK,lam,0),2)
        self.assertEqual(s.limit(lam/FoverK,lam,0),0)

    def test_collar_integral(self):
        r=s.symbols('r',real=True)
        val=s.integrate((1-r*r)*s.cosh(r),(r,-1,1))
        self.assertEqual(s.simplify(s.expand_trig(val).rewrite(s.exp)-4/s.E),0)
        self.assertEqual(s.integrate(s.cosh(r),(r,-1,1)),2*s.sinh(1))


class HessianAndEndpointChecks(unittest.TestCase):
    def test_hessian_square(self):
        alpha,lam,f,phi,Q=s.symbols('alpha lam f phi Q')
        a=4-alpha
        c=(1-alpha)/(3*a)
        L,M=3*lam+4,a*lam+4
        raw=a*(Q-24*c*phi*lam*f+24*c*f*f*lam*L)+2*(-phi+2*L*f)**2
        reduced=a*(Q-6*c*phi*phi*lam/L)+8*(f-phi/(2*L))**2*L*M
        self.assertEqual(s.simplify(raw-reduced),0)

    def test_conformal_hessian(self):
        alpha,lam=s.symbols('alpha lam')
        a=4-alpha
        c=(1-alpha)/(3*a)
        L=3*lam+4
        self.assertEqual(s.simplify(24*a*c*lam*L+8*L**2-8*L*(a*lam+4)),0)

    def test_endpoint_volume_constants(self):
        L=s.symbols('L')
        z=s.Rational(1,3)
        self.assertEqual(s.simplify(4*z+L**4/6+s.Rational(2,3)-(2+L**4/6)),0)
        self.assertEqual(s.Rational(2,3)-z/2,s.Rational(1,2))
        self.assertEqual(4*z,s.Rational(4,3))

    def test_endpoint_model_norm(self):
        rho,t=s.symbols('rho t')
        norm=(-2*t*rho/3)**2+2*(t*rho/3)**2
        self.assertEqual(s.expand(norm.subs(t,s.Rational(1,4))-rho*rho/24),0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
