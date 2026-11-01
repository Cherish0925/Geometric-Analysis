#!/usr/bin/env python3
"""Step 66: nonlinear audit of the least-squares EH correction profile.

Reads step66_ls_h_profile.npz. Computes Ricci frame components of hat_g_eps=EH+eps*h using
Bianchi-IX radial formulas and reports scaled inserted-metric defect max_i |Ric_i/eps - 1|.
This is a certificate-style audit of the candidate profile, not a proof.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.interpolate import CubicSpline
ROOT=Path(__file__).resolve().parents[1]
IN=ROOT/'data'/'step66_ls_h_profile.npz'
OUT=ROOT/'data'/'step66_ls_profile_nonlinear_audit.json'
npz=np.load(IN)
xgrid=npz['r']; F1=npz['f1']; F2=npz['f2']; F3=npz['f3']
cs1,cs2,cs3=CubicSpline(xgrid,F1),CubicSpline(xgrid,F2),CubicSpline(xgrid,F3)
# Bianchi IX formulas
G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp=sp.symbols('G1 G2 G3 g1p g2p g3p g1pp g2pp g3pp')
R00f = -g3pp/(2*G1*G3) + g3p**2/(4*G1*G3**2) - g2pp/(G1*G2) + g2p**2/(2*G1*G2**2) + g1p*g3p/(4*G1**2*G3) + g1p*g2p/(2*G1**2*G2)
R11f = (1 - G3/(2*G2) - g2pp/(2*G1) - g2p*g3p/(4*G1*G3) + g1p*g2p/(4*G1**2))/G2
R33f = (G3**2/(2*G2**2) - g3pp/(2*G1) + g3p**2/(4*G1*G3) - g2p*g3p/(2*G1*G2) + g1p*g3p/(4*G1**2))/G3
R00n=sp.lambdify([G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp],R00f,'numpy')
R11n=sp.lambdify([G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp],R11f,'numpy')
R33n=sp.lambdify([G1,G2,G3,g1p,g2p,g3p,g1pp,g2pp,g3pp],R33f,'numpy')

def ric(x,eps):
    f1,f2,f3=cs1(x),cs2(x),cs3(x)
    f1p,f2p,f3p=cs1(x,1),cs2(x,1),cs3(x,1)
    f1pp,f2pp,f3pp=cs1(x,2),cs2(x,2),cs3(x,2)
    W=1-x**-4; Wp=4*x**-5; Wpp=-20*x**-6
    E1=1+eps*f1; E2=1+eps*f2; E3=1+eps*f3
    E1p=eps*f1p; E2p=eps*f2p; E3p=eps*f3p
    E1pp=eps*f1pp; E2pp=eps*f2pp; E3pp=eps*f3pp
    base3=x**2*W/4; base3p=x*W/2+x**2*Wp/4; base3pp=W/2+x*Wp+x**2*Wpp/4
    G1v=E1/W
    G1p=E1p/W-E1*Wp/W**2
    G1pp=E1pp/W-2*E1p*Wp/W**2-E1*Wpp/W**2+2*E1*Wp**2/W**3
    G2v=E2*x**2/4; G2p=E2p*x**2/4+E2*x/2; G2pp=E2pp*x**2/4+E2p*x+E2/2
    G3v=E3*base3; G3p=E3p*base3+E3*base3p; G3pp=E3pp*base3+2*E3p*base3p+E3*base3pp
    R=np.vstack([R00n(G1v,G2v,G3v,G1p,G2p,G3p,G1pp,G2pp,G3pp),R11n(G1v,G2v,G3v,G1p,G2p,G3p,G1pp,G2pp,G3pp),R33n(G1v,G2v,G3v,G1p,G2p,G3p,G1pp,G2pp,G3pp)]).T
    minE=float(min(np.min(E1),np.min(E2),np.min(E3)))
    return R,minE
summary={}
for eps in [1e-2,3e-3,1e-3,3e-4,1e-4]:
    x=np.linspace(max(xgrid[0],1.02),min(xgrid[-1],eps**(-0.25)),1000)
    R,minE=ric(x,eps)
    defect=np.max(np.abs(R/eps-1),axis=1) if minE>0 else np.full_like(x,np.inf)
    masks={
      'all':np.ones_like(x,dtype=bool),
      'interior_r_gt_1p08':x>1.08,
      'interior_r_gt_1p2':x>1.2,
      'mid_1p2_to_Rcap_minus':(x>1.2)&(x<x[-1]-0.2),
    }
    summary[str(eps)]={'Rcap':float(x[-1]),'min_metric_factor':minE}
    for name,m in masks.items():
        summary[str(eps)][name]={'max':float(np.max(defect[m])),'median':float(np.median(defect[m])),'p95':float(np.quantile(defect[m],0.95))}
    print('eps',eps,'minE',minE,'all max',summary[str(eps)]['all']['max'],'r>1.2 max',summary[str(eps)]['interior_r_gt_1p2']['max'],'med',summary[str(eps)]['interior_r_gt_1p2']['median'])
OUT.write_text(json.dumps({'status':'ok','profile':str(IN),'summary':summary,'warning':'heuristic LS profile; bolt and ambient-H not valid. Interior defect only.'},indent=2))
print('Output',OUT)
