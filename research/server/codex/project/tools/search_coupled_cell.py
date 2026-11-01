#!/usr/bin/env python3
"""Explore actual smooth diagonal cells, not formal curvature moments.

Implements (6.10) of 20260928_relative_cell_cost.md. Every finite parameter
vector gives a positive smooth ordinary bolt and an unchanged CH collar.
Floating-point optimization is exploratory; neither failure nor convergence
proves a lower bound. Print receipts to stdout; redirect only generated data.
"""

import argparse
import json

import numpy as np
from numpy.polynomial import Legendre, Polynomial
from numpy.polynomial.legendre import leggauss
from scipy.optimize import least_squares
from scipy.special import expit


def step_jet(x, left=0.65, right=0.9):
    """C-infinity step and two derivatives in x, exactly flat outside."""
    y = (x - left) / (right - left)
    ans = np.zeros((3, len(x)))
    ans[0, y >= 1] = 1
    active = (y > 0) & (y < 1)
    t = y[active]
    logit = -1 / t + 1 / (1 - t)
    p = expit(logit)
    lp = 1 / t**2 + 1 / (1 - t)**2
    lpp = -2 / t**3 + 2 / (1 - t)**3
    ans[0, active] = p
    ans[1, active] = p * (1 - p) * lp / (right - left)
    ans[2, active] = p * (1 - p) * ((1 - 2*p)*lp**2 + lpp) / (right-left)**2
    return ans


def product(a, b):
    return np.array([a[0]*b[0], a[1]*b[0]+a[0]*b[1],
                     a[2]*b[0]+2*a[1]*b[1]+a[0]*b[2]])


def basis(x, count, power):
    cutoff = -step_jet(x)
    cutoff[0] += 1
    dense = np.linspace(0, 1, 2001)
    dense_cutoff = 1-step_jet(dense)[0]
    result = []
    for k in range(count):
        poly = Legendre.basis(k, domain=[0, 1]).convert(kind=Polynomial)
        poly *= Polynomial([0]*power + [1])
        scale = np.max(np.abs(poly(dense)*dense_cutoff))
        jet = np.array([poly(x), poly.deriv()(x), poly.deriv(2)(x)]) / scale
        result.append(product(jet, cutoff))
    return np.array(result)


class Cell:
    def __init__(self, bolt=0.1, radius=1., count=5, panels=32, order=12):
        if not 0 < bolt < radius:
            raise ValueError('Require 0 < bolt < radius.')
        self.bolt, self.radius, self.count = bolt, radius, count
        self.length = np.log(radius / bolt)
        # Include all cutoff breakpoints as panel boundaries.
        edges = np.unique(np.r_[np.linspace(0, 1, panels+1), 0.65, 0.9])
        z, weight = leggauss(order)
        self.x = np.concatenate([(b+a)/2+(b-a)*z/2 for a,b in zip(edges[:-1],edges[1:])])
        self.weight = np.concatenate([(b-a)*weight/2 for a,b in zip(edges[:-1],edges[1:])])
        self.r = bolt*np.exp(self.length*self.x)
        r, mu, ell = self.r, bolt**2, self.length
        # Derivatives here are with respect to x.
        ch = np.array([1+r*r/6, ell*r*r/3, 2*ell*ell*r*r/3])
        correction = np.array([
            -(mu+mu*mu/2)/r**2 + mu**3/(3*r**4),
            2*ell*(mu+mu*mu/2)/r**2 - 4*ell*mu**3/(3*r**4),
            -4*ell**2*(mu+mu*mu/2)/r**2+16*ell**2*mu**3/(3*r**4)])
        cutoff = -step_jet(self.x)
        cutoff[0] += 1
        self.base = ch + product(correction, cutoff)
        self.bases = [basis(self.x, count, power) for power in (1, 2, 0)]
        # r^3 dr = length * r^4 dx.
        self.sqrt_weight = np.sqrt(self.weight*ell*r**4)

    def radial(self, jet):
        value, dx, dxx = jet
        return np.array([value, dx/(self.length*self.r),
                         (dxx/self.length**2-dx/self.length)/self.r**2])

    def profiles(self, parameters):
        v, w, phi = [np.einsum('i,ijk->jk', c, b)
                     for c,b in zip(np.reshape(parameters,(3,self.count)),self.bases)]
        exponent = np.array([np.exp(v[0]), np.exp(v[0])*v[1],
                             np.exp(v[0])*(v[2]+v[1]**2)])
        return [self.radial(product(self.base, exponent)), self.radial(w), self.radial(phi)]

    def residual(self, parameters):
        (f,fp,fpp),(w,wp,wpp),(phi,pp,ppp) = self.profiles(parameters)
        r = self.r
        ev = 1-fpp/2-5*fp/(2*r)
        eh = 1-fp/r+4*(1-f)/r**2
        c = 8*np.sinh(w)**2/r**2
        z = 8*np.sinh(2*w)**2/(r**2*f)
        u = -f*wpp-(fp+3*f/r)*wp+4*np.sinh(4*w)/(r**2*f)-4*np.sinh(2*w)/r**2
        d0 = ev+np.expm1(2*phi)-3*f*ppp-(2*fp+3*f/r)*pp
        d3 = ev+np.expm1(2*phi)-f*ppp-(2*fp+5*f/r)*pp-2*f*pp**2
        dh = eh+np.expm1(2*phi)-f*ppp-(fp+5*f/r)*pp-2*f*pp**2
        return (np.array([d0-2*f*wp**2,d3-z,np.sqrt(2)*(dh+c),
                          np.sqrt(2)*(u-2*f*pp*wp)])*self.sqrt_weight).ravel()

    def cost(self, parameters):
        v = self.residual(parameters)
        return float(np.dot(v,v))  # J/(2*pi^2), threshold = 4.

    def receipt(self, parameters):
        f,w,phi = self.profiles(parameters)
        r, wt = self.r, self.sqrt_weight**2
        ev = 1-f[2]/2-5*f[1]/(2*r)
        eh = 1-f[1]/r+4*(1-f[0])/r**2
        scalar = (2*ev+2*eh-4-2*f[0]*w[1]**2
                  +16*np.sinh(w[0])**2/r**2-8*np.sinh(2*w[0])**2/(r**2*f[0]))
        n = 2*np.dot(wt,f[0]*(w[1]+2*np.sinh(2*w[0])/(r*f[0]))**2)
        # All quantities here divided by 2*pi^2.
        d = self.radius**4/4
        m = 4*d+2*self.bolt**2
        integrated_scalar = np.dot(wt,scalar)
        return {'J_over_2pi2':self.cost(parameters),
                'N_over_2pi2':float(n),'scalar_identity_error':float(integrated_scalar+m+n),
                'max_abs_w':float(max(abs(w[0]))),'max_abs_phi':float(max(abs(phi[0]))),
                'min_F':float(min(f[0]))}


def run(args):
    cell = Cell(args.bolt,args.radius,args.count,args.panels)
    zero = np.zeros(3*args.count)
    rng = np.random.default_rng(args.seed)
    print(json.dumps({'kind':'baseline','bolt':args.bolt,'radius':args.radius,
                      'count':args.count,**cell.receipt(zero)}),flush=True)
    for j in range(args.starts):
        start = np.zeros_like(zero) if j == 0 else rng.normal(0,args.amplitude,len(zero))
        fit = least_squares(cell.residual,start,jac='cs',max_nfev=args.evaluations,
                            ftol=1e-10,xtol=1e-10,gtol=1e-9,bounds=(-args.bound,args.bound))
        fine = Cell(args.bolt,args.radius,args.count,args.panels*4,16)
        print(json.dumps({'kind':'fit','start':j,'evaluations':fit.nfev,
                          'success':bool(fit.success),'optimality':float(fit.optimality),
                          'parameters':fit.x.tolist(),'coarse':cell.receipt(fit.x),
                          'refined':fine.receipt(fit.x)}),flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--bolt',type=float,default=.1)
    p.add_argument('--radius',type=float,default=1.)
    p.add_argument('--count',type=int,default=5)
    p.add_argument('--panels',type=int,default=24)
    p.add_argument('--starts',type=int,default=4)
    p.add_argument('--evaluations',type=int,default=200)
    p.add_argument('--amplitude',type=float,default=.03)
    p.add_argument('--bound',type=float,default=2.)
    p.add_argument('--seed',type=int,default=928)
    run(p.parse_args())
