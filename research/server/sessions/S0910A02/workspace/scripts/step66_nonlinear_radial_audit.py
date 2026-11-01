#!/usr/bin/env python3
"""Step 66: nonlinear solver-agnostic Ricci-endomorphism audit for radial EH insert metrics.

For a radial U(2)-invariant correction h=f1 e0^2+f2(e1^2+e2^2)+f3 e3^2, assemble
    hat_g_eps = EH + eps*h
on the EH insert.  The actual scaled inserted metric is eps*hat_g_eps, so its Ricci
endomorphism eigenvalues are R_i(hat_g_eps)/eps, where R_i are frame Ricci components
with respect to hat_g_eps.  The positive-branch target is Lambda=1, so the operator defect is
    delta_eps(r)=max_i | R_i(hat_g_eps)/eps - 1 |.

This is a direct Ricci-endomorphism audit independent of BVP convergence.  It currently audits:
  raw h=0;
  r2metric f_i=r^2;
  kpot_parallel f_i=4;
  scalar_cutoff profiles from Step 66 (local Kähler scalar source away from bolt).
The scalar_cutoff profile is diagnostic only: it should pass away from the artificial core cutoff
and fail with O(1) defect in the compact core/transition, identifying the obstruction support.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import CubicSpline

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'data'/'step66_nonlinear_radial_audit.json'
Lam=1.0
av=1.0

# Bianchi IX frame-Ricci formulas for metric G1 dr^2 + G2(s1^2+s2^2)+G3 s3^2.
G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp=sp.symbols('G1 G2 G3 g1p g2p g3p g1pp g2pp g3pp')
R00f = -g3pp/(2*G1*G3) + g3p**2/(4*G1*G3**2) - g2pp/(G1*G2) + g2p**2/(2*G1*G2**2) + g1p*g3p/(4*G1**2*G3) + g1p*g2p/(2*G1**2*G2)
R11f = (1 - G3/(2*G2) - g2pp/(2*G1) - g2p*g3p/(4*G1*G3) + g1p*g2p/(4*G1**2))/G2
R33f = (G3**2/(2*G2**2) - g3pp/(2*G1) + g3p**2/(4*G1*G3) - g2p*g3p/(2*G1*G2) + g1p*g3p/(4*G1**2))/G3
R00n=sp.lambdify([G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp],R00f,'numpy')
R11n=sp.lambdify([G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp],R11f,'numpy')
R33n=sp.lambdify([G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp],R33f,'numpy')

def ricci_from_profile(x, eps, prof):
    f1,f2,f3,f1p,f2p,f3p,f1pp,f2pp,f3pp=prof(x)
    W=1-av**4/x**4; Wp=4*av**4/x**5; Wpp=-20*av**4/x**6
    E1=1+eps*f1; E2=1+eps*f2; E3=1+eps*f3
    E1p=eps*f1p; E2p=eps*f2p; E3p=eps*f3p
    E1pp=eps*f1pp; E2pp=eps*f2pp; E3pp=eps*f3pp
    base3=x**2*W/4; base3p=x*W/2+x**2*Wp/4; base3pp=W/2+x*Wp+x**2*Wpp/4
    G1v=E1/W
    G1pv=E1p/W - E1*Wp/W**2
    G1ppv=E1pp/W - 2*E1p*Wp/W**2 - E1*Wpp/W**2 + 2*E1*Wp**2/W**3
    G2v=E2*x**2/4
    G2pv=E2p*x**2/4 + E2*x/2
    G2ppv=E2pp*x**2/4 + E2p*x + E2/2
    G3v=E3*base3
    G3pv=E3p*base3 + E3*base3p
    G3ppv=E3pp*base3 + 2*E3p*base3p + E3*base3pp
    R=np.vstack([
        R00n(G1v,G2v,G3v,G1pv,G2pv,G3pv,G1ppv,G2ppv,G3ppv),
        R11n(G1v,G2v,G3v,G1pv,G2pv,G3pv,G1ppv,G2ppv,G3ppv),
        R33n(G1v,G2v,G3v,G1pv,G2pv,G3pv,G1ppv,G2ppv,G3ppv)
    ]).T
    min_metric=float(min(np.min(E1),np.min(E2),np.min(E3)))
    return R,min_metric

def raw(x):
    z=np.zeros_like(x); return z,z,z,z,z,z,z,z,z

def r2metric(x):
    return x**2,x**2,x**2,2*x,2*x,2*x,2+0*x,2+0*x,2+0*x

def kpot_parallel(x):
    f=4+0*x; z=0*x; return f,f,f,z,z,z,z,z,z

def make_scalar_cutoff(cutoff_width=0.3,Rmax=30.0,eps_bolt=1e-3):
    grid=np.linspace(1+eps_bolt,Rmax,5000)
    W=1-grid**-4
    # potential uK with ddbar(uK)=4 omega; source factor -0.5 chosen by exact master identity.
    uK=grid**2+0.5*np.log((grid**2-1)/(grid**2+1))
    s=(grid-(1+eps_bolt))/cutoff_width
    y=np.clip(s,0,1)
    chi=y**3*(10-15*y+6*y**2)
    S=-0.5*Lam*uK*chi
    flux=cumulative_trapezoid(grid**3*S,grid,initial=0.0)
    q=flux/(grid**3*W)
    B=2*q*W/grid
    A=(2/grid)*np.gradient(q*grid*W/2,grid,edge_order=2)
    csA=CubicSpline(grid,A); csB=CubicSpline(grid,B)
    def prof(x):
        return csA(x),csB(x),csA(x),csA(x,1),csB(x,1),csA(x,1),csA(x,2),csB(x,2),csA(x,2)
    return prof,{"cutoff_width":cutoff_width,"Rmax":Rmax,"eps_bolt":eps_bolt}

profiles={"raw":(raw,{}),"r2metric":(r2metric,{}),"kpot_parallel":(kpot_parallel,{})}
for cf in [0.15,0.3,0.6]:
    profiles[f"scalar_cutoff_{cf}"]=make_scalar_cutoff(cutoff_width=cf)

summary={}
for eps in [1e-2,3e-3,1e-3,3e-4]:
    Rcap=min(30.0, eps**(-0.25))
    x=np.concatenate([np.linspace(1.01,1.5,250),np.linspace(1.5,Rcap,500)])
    summary[str(eps)]={}
    print('\neps=',eps,' Rcap=',Rcap)
    for name,(prof,meta) in profiles.items():
        R,minE=ricci_from_profile(x,eps,prof)
        if minE<=0:
            delta_all=float('inf'); delta_far=float('inf'); med_far=float('inf')
        else:
            defect=np.max(np.abs(R/eps-Lam),axis=1)
            delta_all=float(np.max(defect))
            # far: after scalar cutoff; for non-scalar use r>1.5
            cf=meta.get('cutoff_width',0.15)
            mask=x>1+3*cf
            delta_far=float(np.max(defect[mask])) if np.any(mask) else None
            med_far=float(np.median(defect[mask])) if np.any(mask) else None
        sampleR=ricci_from_profile(np.array([2.0]),eps,prof)[0][0]
        summary[str(eps)][name]={"Rcap":float(Rcap),"min_metric_factor":minE,
                                  "delta_all":delta_all,"delta_far":delta_far,"median_far":med_far,
                                  "sample_scaled_Rminus1_at_r2":[float(v/eps-Lam) for v in sampleR],
                                  "meta":meta}
        print(name,'minE',f'{minE:.3g}','delta_all',f'{delta_all:.3g}','delta_far',f'{delta_far:.3g}','median_far',f'{med_far:.3g}')

OUT.write_text(json.dumps({"status":"ok","Lambda":Lam,"summary":summary,
                           "meaning":"delta values are operator defects for scaled insert eps*hat_g_eps on radial EH region r<=eps^{-1/4}. raw remains O(1); scalar_cutoff kills defect away from compact obstruction but fails near cutoff/core."},indent=2))
print('Output:',OUT)
