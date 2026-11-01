#!/usr/bin/env python3
"""Dimensionless multiscale diagnostics for small-nu Taub--NUT--AdS.

Uses the exact invariant derived in compute_taub_nut_ads_curvature.py:
 |W|^2 = 32 nu^2 (4nu^2-3)^2 / [3(r+nu)^6].
The angularly complete shell volume is
 dV/dr = 64 pi^2 nu (r^2-nu^2).
We compare cumulative shell averages with the critical LeBrun target
 |W^+|^2=1/24 and the completed-square scalar-Weyl defect
 (s+8 sqrt(6)|W^+|)^2, with s=-4.
"""
import sympy as sp

x, nu = sp.symbols('x nu', positive=True, real=True)
# r = nu*x.  Exact formulas for cumulative region nu <= r <= nu*x.
r = nu*x
W2 = sp.factor(32*nu**2*(4*nu**2-3)**2/(3*(r+nu)**6))
vol = sp.factor(32*sp.pi**2*nu * ((r**3-nu**3)/3 - nu**2*(r-nu)))
energy = sp.factor(32*sp.pi**2*(r-nu)**2*(4*nu**2-3)**2*(r**2+6*r*nu+17*nu**2)/(9*(r+nu)**4))
avg = sp.factor(sp.cancel(energy/vol))
print('Volume(nu..nu*x) =', vol)
print('Weyl energy =', energy)
print('mean |W|^2 =', avg)
print('small-nu coefficient lim nu^4*mean at fixed x =', sp.factor(sp.limit(nu**4*avg,nu,0,dir='+')))
print('large-x coefficient lim x^3*(lim nu^4*mean) =', sp.factor(sp.limit(x**3*sp.limit(nu**4*avg,nu,0,dir='+'),x,sp.oo)))

# Radius in the nut scale x=O(1): mean diverges like nu^-4.  Fixed physical
# outer radius corresponds x=R/nu and captures finite Weyl energy in O(nu)
# volume, so its mean diverges like 1/nu.
R=sp.symbols('R',positive=True,real=True)
rR=R
volR=sp.factor(32*sp.pi**2*nu * ((rR**3-nu**3)/3 - nu**2*(rR-nu)))
energyR=sp.factor(32*sp.pi**2*(rR-nu)**2*(4*nu**2-3)**2*(rR**2+6*rR*nu+17*nu**2)/(9*(rR+nu)**4))
avgR=sp.factor(sp.cancel(energyR/volR))
print('fixed-R mean asymptotic coefficient lim nu*mean =',sp.factor(sp.limit(nu*avgR,nu,0,dir='+')))
print('fixed-R energy limit =',sp.factor(sp.limit(energyR,nu,0,dir='+')))
print('fixed-R volume/nu limit =',sp.factor(sp.limit(volR/nu,nu,0,dir='+')))

# Pointwise annular limit (r fixed): W2 -> 0, hence completed-square defect ->16.
print('pointwise fixed-r W2 limit =', sp.limit((32*nu**2*(4*nu**2-3)**2/(3*(R+nu)**6)),nu,0,dir='+'))
print('annular completed-square defect limit = 16')

# W2 above is the four-index full-Weyl norm.  In our chosen orientation
# Taub--NUT--AdS has W+=0 and W- nonzero.  If orientation is reversed, the
# calibrated endomorphism norm |W+|^2=1/24 corresponds to full tensor W2=1/6.
# That magnitude occurs only at r~C nu^(1/3), not in a multiscale bulk.
sol_scale_const = sp.factor((sp.Rational(32,3)*9*6)**sp.Rational(1,6))
print('leading r at full-Weyl calibrated magnitude / nu^(1/3) =', sol_scale_const)
