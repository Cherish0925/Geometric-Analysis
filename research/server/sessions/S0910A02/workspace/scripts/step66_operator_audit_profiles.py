#!/usr/bin/env python3
"""Step 66: solver-agnostic operator-norm audit for radial EH correction profiles.

Purpose: decouple the pinching certificate from BVP convergence.
Given any radial U(2)-invariant diagonal correction h = f1 e0^2+f2(e1^2+e2^2)+f3 e3^2,
assemble g_t = t*(g_EH + t*h) on the EH insert and directly compute, from Step-65's full-4D
linearized Ricci formulas, the first-order frame Ricci-endomorphism defect

    delta_lin(r) = max_i | dRic_i(h) - Lambda |.

For the actual finite-t nonlinear audit one must compute Ric(g_EH+t h) directly; this script is the
cheap first-order audit that identifies whether the profile has the correct source structure and where
it fails.  It audits:
  raw:       h=0  -> defect |Lambda| everywhere (Step-65 calibration).
  r2metric:  f1=f2=f3=r^2 -> illustrates trace/gauge cancellation; dRic=0, still defect 1.
  kpot:      h=i ddbar phi with q=phi'=2r^5/(r^4-1), so A=B=4 (parallel multiple of g); defect 1.
  scalar_phi_R: solve truncated scalar potential Delta_K phi = -2 Lambda u_K cut off away from bolt,
                then compute dRic defect; expected to improve only away from bolt and expose cohomology/core obstruction.

This is not a final Biquard h solve. It provides a reusable audit interface and confirms which shortcuts do or do not reduce operator defect.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_bvp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "step66_operator_audit_profiles.json"

# Load Step-65 full dRic formulas and lambdify for arbitrary f and derivatives.
r = sp.symbols('r', positive=True)
LamSym = sp.symbols('Lambda')
f1 = sp.Function('f1'); f2 = sp.Function('f2'); f3 = sp.Function('f3')
import json as _json
D = _json.loads((ROOT/"data"/"step65_full4d_lichnerowicz.json").read_text())
loc = {'r': r, 'Derivative': sp.Derivative, 'f1': f1, 'f2': f2, 'f3': f3}
exprs = {k: sp.sympify(v, locals=loc) for k,v in D['dRic_at_point'].items()}
# Convert coordinate components to frame components (a=1): frame00=W*coord00, frame11=4/r^2 coord11, frame33=4/(r^2 W) coord33.
Wexpr = 1 - r**(-4)
frame_exprs = {
    '00': sp.simplify(Wexpr*exprs['00']),
    '11': sp.simplify(4*exprs['11']/r**2),
    '33': sp.simplify(4*exprs['33']/(r**2*Wexpr)),
}
vars_ = [r, f1(r), f2(r), f3(r), sp.Derivative(f1(r),r), sp.Derivative(f2(r),r), sp.Derivative(f3(r),r), sp.Derivative(f1(r),(r,2)), sp.Derivative(f2(r),(r,2)), sp.Derivative(f3(r),(r,2))]
frame_fun = {k: sp.lambdify(vars_, v, 'numpy') for k,v in frame_exprs.items()}

Lam = 1.0

def eval_profile(rr, prof):
    f1v,f2v,f3v,f1p,f2p,f3p,f1pp,f2pp,f3pp = prof(rr)
    vals = [rr, f1v,f2v,f3v,f1p,f2p,f3p,f1pp,f2pp,f3pp]
    R = np.vstack([frame_fun['00'](*vals), frame_fun['11'](*vals), frame_fun['33'](*vals)]).T
    defect = np.max(np.abs(R - Lam), axis=1)
    return R, defect

# utilities for derivatives by finite differences on vector arrays

def fd_first(y, x): return np.gradient(y, x, edge_order=2)
def fd_second(y, x): return np.gradient(np.gradient(y, x, edge_order=2), x, edge_order=2)

def make_interp_profile(grid, F1,F2,F3):
    from scipy.interpolate import CubicSpline
    cs1,cs2,cs3 = CubicSpline(grid,F1),CubicSpline(grid,F2),CubicSpline(grid,F3)
    def prof(x):
        return cs1(x),cs2(x),cs3(x),cs1(x,1),cs2(x,1),cs3(x,1),cs1(x,2),cs2(x,2),cs3(x,2)
    return prof

# analytic profiles

def raw(x):
    z=np.zeros_like(x); return (z,z,z,z,z,z,z,z,z)
def r2metric(x):
    return (x**2,x**2,x**2,2*x,2*x,2*x,2+0*x,2+0*x,2+0*x)
def kpot_parallel(x):
    # q=2r^5/(r^4-1) gives A=B=4 in current normalization, i.e. h=4g (parallel scale)
    f=4+0*x; z=0*x; return (f,f,f,z,z,z,z,z,z)

# scalar BVP profile: solve Delta_K phi = S, with S=-2*uK_cut.
# For h=i ddbar phi, dRic = -1/2 ddbar(Delta_K phi), so if S=-2*uK and ddbar(uK)=4 omega,
# the target sign/factor is approximate; we audit, not assume.
def scalar_profile(Rmax=20.0, eps_bolt=1e-3, cutoff_width=0.25):
    a=1.0
    grid=np.linspace(1+eps_bolt,Rmax,1200)
    W=1-grid**-4
    uK = grid**2 + 0.5*np.log((grid**2-1)/(grid**2+1))
    # cutoff source to zero near bolt to avoid log/cohomology singularity
    s=(grid-(1+eps_bolt))/cutoff_width
    chi=np.clip(s,0,1)**3*(10-15*np.clip(s,0,1)+6*np.clip(s,0,1)**2)
    S = -0.5*Lam*uK*chi  # guessed factor from identity; audit will determine value
    # Solve (r^3 W q)' = r^3 S, q=phi'. regular at bolt -> flux=0.
    from scipy.integrate import cumulative_trapezoid
    flux = cumulative_trapezoid(grid**3*S, grid, initial=0.0)
    q = flux/(grid**3*W)
    # compute A,B from q
    B = 2*q*W/grid
    A = (2/grid)*fd_first(q*grid*W/2, grid)
    return grid, make_interp_profile(grid,A,B,A), {"Rmax":Rmax,"eps_bolt":eps_bolt,"cutoff_width":cutoff_width,"source_factor":"-0.5*Lambda*uK*chi"}

rr = np.concatenate([
    np.linspace(1.01,1.5,200),
    np.linspace(1.5,5,300),
    np.linspace(5,20,300)
])
profiles={"raw": raw, "r2metric": r2metric, "kpot_parallel": kpot_parallel}
summary={}
for name,prof in profiles.items():
    R,defect=eval_profile(rr,prof)
    summary[name]={"max_defect":float(np.max(defect)),"median_defect":float(np.median(defect)),
                   "sample_R_frame_at_2": [float(x) for x in eval_profile(np.array([2.0]),prof)[0][0]]}
    print(name, summary[name])

# scalar cutoff profile
for cf in [0.15,0.3,0.6]:
    grid, prof, meta = scalar_profile(cutoff_width=cf)
    # audit away from bolt and whole interval
    R, defect = eval_profile(grid, prof)
    mask_far = grid>1+3*cf
    name=f"scalar_cutoff_{cf}"
    summary[name]={"max_defect_all":float(np.max(defect)),"max_defect_far":float(np.max(defect[mask_far])) if np.any(mask_far) else None,
                   "median_defect_far":float(np.median(defect[mask_far])) if np.any(mask_far) else None,
                   "sample_R_frame_at_2": [float(x) for x in eval_profile(np.array([2.0]),prof)[0][0]],
                   "meta":meta}
    print(name, summary[name])

OUT.write_text(json.dumps({"status":"ok","Lambda":Lam,"summary":summary,
                           "interpretation":"raw/parallel profiles retain O(1) defect; scalar cutoff test is solver-agnostic first-order audit, not Biquard h."}, indent=2))
print("Output:", OUT)
