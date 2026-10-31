"""Numerical tests for the multi-centre Gibbons--Hawking O10 tangent.

For equal NUT charges ell at centres p_a,
    V=1+ell sum_a |x-p_a|^{-1},   m=m0/V,
we use the exact pointwise identities (away from centres)
    |nabla v|_g^2 = m0 |grad_R3 V|^2 / V^4,
    |dm|_g^2      = m0^2 |grad_R3 V|^2 / V^5,
and dvol_g=V d^3x dpsi, period(psi)=4*pi*ell.
Thus Ev=4*pi*ell*m0 int |grad V|^2/V^3 dx and
Em=4*pi*ell*m0^2 int |grad V|^2/V^4 dx.

Divergence gives exact centre-count laws
  int |grad V|^2/V^3 = 2*pi*k/ell,
  int |grad V|^2/V^4 = 4*pi*k/(3*ell),
so Ev=8*pi^2*m0*k and Em=16*pi^2*m0^2*k/3 in the normalization
where V has charge ell/r and psi period 4*pi*ell.  This script checks
those values by deterministic tensor-product Gauss quadrature in prolate
spheroidal coordinates for two centres at z=+-a.
"""
import argparse, json, os
import numpy as np
from numpy.polynomial.legendre import leggauss


def integrate_two(a=1.0, ell=1.0, m0=128/81, nmu=320, nnu=240):
    # prolate coords: r_+ + r_- = 2a mu, r_+-r_-=2a nu;
    # x=(a sqrt(mu^2-1)sqrt(1-nu^2) cosphi,...), z=a mu nu.
    # map mu in [1,infty) by t in [0,1], mu=1+t/(1-t).
    xt, wt = leggauss(nmu)
    t=(xt+1)/2; wt=wt/2
    xn, wn = leggauss(nnu)
    nu=xn
    mu=1+t/(1-t)
    dmu_dt=1/(1-t)**2
    MU,NU=np.meshgrid(mu,nu,indexing='ij')
    # distances to centres, assignment immaterial
    rp=a*(MU+NU); rm=a*(MU-NU)
    V=1+ell/rp+ell/rm
    # grad V in cylindrical variables (rho,z), robust away from the measure-zero focal points
    rho=a*np.sqrt(MU**2-1)*np.sqrt(1-NU**2)
    z=a*MU*NU
    drp_rho=rho/rp; drm_rho=rho/rm
    drp_z=(z+a)/rp; drm_z=(z-a)/rm
    Vr=-ell*(drp_rho/rp**2+drm_rho/rm**2)
    Vz=-ell*(drp_z/rp**2+drm_z/rm**2)
    grad2=Vr**2+Vz**2
    jac=2*np.pi*a**3*(MU**2-NU**2) # integrated phi
    W=wt[:,None]*wn[None,:]*dmu_dt[:,None]
    I3=np.sum(W*jac*grad2/V**3)
    I4=np.sum(W*jac*grad2/V**4)
    Ev=4*np.pi*ell*m0*I3
    Em=4*np.pi*ell*m0**2*I4
    exact3=4*np.pi/ell # k=2
    exact4=8*np.pi/(3*ell)
    return dict(a=a,ell=ell,nmu=nmu,nnu=nnu,I3=I3,I4=I4,
                exact_I3=exact3,exact_I4=exact4,
                relerr_I3=(I3-exact3)/exact3,relerr_I4=(I4-exact4)/exact4,
                Ev=Ev,Em=Em,exact_Ev=16*np.pi**2*m0,
                exact_Em=32*np.pi**2*m0**2/3)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--nmu',type=int,default=320); ap.add_argument('--nnu',type=int,default=240)
    args=ap.parse_args()
    rows=[integrate_two(a=a,nmu=args.nmu,nnu=args.nnu) for a in [0.25,1.0,4.0]]
    out=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','data','gh_multicentre_energy.json')
    with open(out,'w') as f: json.dump(rows,f,indent=2)
    print(json.dumps(rows,indent=2))
