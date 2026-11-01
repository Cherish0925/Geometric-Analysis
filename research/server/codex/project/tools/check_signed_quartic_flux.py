#!/usr/bin/env python3
"""Exact exterior algebra and quadratic checks; not an endpoint proof."""

import itertools
import unittest
import sympy as s


def wedge(a, b):
    out = {}
    for x, ax in a.items():
        for y, by in b.items():
            indices = x+y
            if len(set(indices)) != len(indices):
                continue
            sign = (-1)**sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))
            key = tuple(sorted(indices))
            out[key] = out.get(key,0)+sign*ax*by
    return out


def add(*forms):
    out = {}
    for a in forms:
        for k,v in a.items():
            out[k] = out.get(k,0)+v
    return out


def scale(c, a):
    return {k:c*v for k,v in a.items()}


def dot(a, b):
    return sum(v*b.get(k,0) for k,v in a.items())


def one(x):
    return {(j,):x[j] for j in range(4)}


OMEGA = [{(0,1):1,(2,3):-1}, {(0,2):1,(1,3):1}, {(0,3):1,(1,2):-1}]
PLUS = {(0,1):1,(2,3):1}


class FluxChecks(unittest.TestCase):
    def test_weighted_dirac_cutoff(self):
        t,g,h,d=[s.Matrix(s.symbols(name+'0:4',real=True)) for name in ('t','g','h','d')]
        cs=[s.eye(2),s.diag(s.I,-s.I),s.Matrix([[0,1],[-1,0]]),s.Matrix([[0,-s.I],[-s.I,0]])]
        du=[s.Matrix([s.I*t[j],g[j]+s.I*h[j]]) for j in range(4)]
        dirac=-sum((cs[j].conjugate().T*du[j] for j in range(4)),s.zeros(2,1))
        cliff=-sum((d[j]*cs[j].conjugate().T*s.Matrix([1,0]) for j in range(4)),s.zeros(2,1))
        actual=s.re((dirac.conjugate().T*cliff)[0])
        expected=sum(dot(wedge(one(d),one(v)),om) for v,om in zip((t,-g,-h),OMEGA))
        self.assertEqual(s.expand(actual-expected),0)

    def test_central_scalar_cancellation(self):
        # The central component has independent SD and ASD coefficients.
        sd=[PLUS,{(0,2):1,(1,3):-1},{(0,3):1,(1,2):1}]
        x=s.symbols('x0:3',real=True)
        y=s.symbols('y0:3',real=True)
        c=add(*[scale(a,om) for a,om in zip(x,OMEGA)],
              *[scale(a,om) for a,om in zip(y,sd)])
        aa,bb,cc=s.symbols('a b c',real=True)
        wrow=[aa,bb,cc]
        f11=add(c,*[scale(-a/2,om) for a,om in zip(wrow,OMEGA)],
                scale(s.Rational(1,6),OMEGA[0]))
        top=(0,1,2,3)
        actual=4*wedge(c,f11).get(top,0)+s.Rational(2,3)*(1+2*x[0])
        expected=4*wedge(c,c).get(top,0)+s.Rational(2,3)+4*sum(a*b for a,b in zip(wrow,x))
        self.assertEqual(s.expand(actual-expected),0)

    def test_full_weyl_linear_and_cubic(self):
        d, t, g, h = [one(s.symbols(name+'0:4',real=True)) for name in ('d','t','g','h')]
        aa,bb,cc,ee,ff,cut = s.symbols('a b c e f cut',real=True)
        w = s.Matrix([[aa,bb,cc],[bb,ee,ff],[cc,ff,-aa-ee]])
        rows = [add(*[scale(w[j,k],OMEGA[k]) for k in range(3)]) for j in range(3)]
        f22 = scale(s.I/2,rows[0])
        f12 = add(scale(-s.Rational(1,2),rows[1]),scale(s.I/2,rows[2]))
        f21 = add(scale(s.Rational(1,2),rows[1]),scale(s.I/2,rows[2]))
        alpha = scale(s.I,t)
        b = add(g,scale(s.I,h))
        bar_b = add(g,scale(-s.I,h))
        tw = add(scale(-1,wedge(alpha,f22)),scale(s.Rational(1,2),wedge(b,f12)),
                 scale(-s.Rational(1,2),wedge(bar_b,f21)))
        top = (0,1,2,3)
        actual = -8*cut*wedge(d,tw).get(top,0)
        k = s.Matrix([[dot(wedge(d,v),om) for om in OMEGA] for v in (t,scale(-1,g),scale(-1,h))])
        expected = 4*cut*s.trace(k.T*w)
        self.assertEqual(s.expand(actual-expected),0)
        cubic = wedge(wedge(alpha,bar_b),b)
        actual_cubic = -8*cut*wedge(d,cubic).get(top,0)
        expected_cubic = 16*cut*wedge(wedge(wedge(d,t),g),h).get(top,0)
        self.assertEqual(s.expand(actual_cubic-expected_cubic),0)

    def test_budget_square(self):
        theta,sigma,ww,mm,mw=s.symbols('theta sigma ww mm mw',positive=True)
        original=4*theta*mw-2*theta**2*ww
        squared=((2*theta**2+sigma)*ww-4*theta*mw
                 +4*theta**2*mm/(2*theta**2+sigma))
        completed=4*theta**2*mm/(2*theta**2+sigma)+sigma*ww-squared
        self.assertEqual(s.factor(original-completed),0)

    def test_calibrated_bulk_quadratic(self):
        t,g,h=[s.Matrix(s.symbols(name+'0:4',real=True)) for name in ('t','g','h')]
        gh,th,tg=wedge(one(g),one(h)),wedge(one(t),one(h)),wedge(one(t),one(g))
        q=(-8*dot(gh,PLUS)+s.Rational(16,3)*dot(gh,OMEGA[0])
           +s.Rational(4,3)*dot(th,OMEGA[1])-s.Rational(4,3)*dot(tg,OMEGA[2]))
        u=[s.Matrix([s.I*t[j],g[j]+s.I*h[j]]) for j in range(4)]
        cs=[s.eye(2),s.diag(s.I,-s.I),s.Matrix([[0,1],[-1,0]]),s.Matrix([[0,-s.I],[-s.I,0]])]
        dirac=-sum((cs[j].conjugate().T*u[j] for j in range(4)),s.zeros(2,1))
        norm=lambda v: (v.conjugate().T*v)[0]
        anorm=(norm(u[0]-s.I*u[1])+norm(u[2]-s.I*u[3]))/2
        jg=s.Matrix([-g[1],g[0],g[3],-g[2]])
        rhs=(s.Rational(20,3)*(norm(t)+norm(g)+norm(h))-2*norm(t)
             -8*anorm-s.Rational(2,3)*norm(dirac)-2*norm(h-jg))
        self.assertEqual(s.expand(q-rhs),0)


if __name__ == '__main__':
    unittest.main()
