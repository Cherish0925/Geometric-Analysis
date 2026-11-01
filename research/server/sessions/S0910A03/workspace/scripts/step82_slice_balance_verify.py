#!/usr/bin/env python3
"""Verify the Step 82 physical slice balances for diagonal OT metrics.

Metric:
  g = dr^2 + e^{2a(r,z)} dz^2
      + e^{sigma(r,z)+w(r,z)} dx^2
      + e^{sigma(r,z)-w(r,z)} dy^2.
Here rho=e^sigma, u=a_r, B=1/2 G^{-1}G_r,
v=tr B=sigma_r, B0=B-(v/2)I, dmu=e^a rho dz.

The script verifies pointwise divergence formulas underlying
  J' = 6V - int tr_orbit(E) dmu,
  I' = 3V + int R(q_r) dmu - int E_zz dmu,
and verifies the Hamilton-rewritten turning formula.  It also evaluates
all identities on a nontrivial periodic test field by quadrature and finite
radial differencing.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
import sympy as sp

r,z=sp.symbols('r z', real=True)
a=sp.Function('a')(r,z)
s=sp.Function('s')(r,z)      # sigma
w=sp.Function('w')(r,z)      # diagonal H^2 coordinate
D=sp.diff
ar,az=D(a,r),D(a,z); arr=D(a,r,2)
sr,sz=D(s,r),D(s,z); srr=D(s,r,2)
wr,wz=D(w,r),D(w,z); wrr=D(w,r,2)
azz=D(a,z,2); szz=D(s,z,2); wzz=D(w,z,2)

# Logarithmic orbit lengths b,c.
b=(s+w)/2
c=(s-w)/2
br,cr=D(b,r),D(c,r); brr,crr=D(b,r,2),D(c,r,2)
bz,cz=D(b,z),D(c,z); bzz,czz=D(b,z,2),D(c,z,2)

em2a=sp.exp(-2*a)
# Orthonormal components E=Ric+3g, from the independently direct Ricci formulas.
Err=3-ar**2-arr-br**2-brr-cr**2-crr
Erz=sp.exp(-a)*(ar*bz+ar*cz-br*bz-cr*cz-D(b,r,z)-D(c,r,z))
Ezz=3-ar**2-ar*br-ar*cr-arr+em2a*(az*bz+az*cz-bz**2-bzz-cz**2-czz)
Ex=3-ar*br-br**2-br*cr-brr+em2a*(az*bz-bz**2-bz*cz-bzz)
Ey=3-ar*cr-br*cr-cr**2-crr+em2a*(az*cz-bz*cz-cz**2-czz)
Eorb=sp.expand(Ex+Ey)

u=ar
v=sr
H=u+v
B0sq=sp.Rational(1,2)*wr**2
mu=sp.exp(a+s)

# Scalar curvature of q_r=e^{2a}dz^2+e^{s+w}dx^2+e^{s-w}dy^2.
# In unit arclength ell with d/dell=e^{-a}d/dz:
# Rq=-2(vdot)-|A|^2-v^2, |A|^2=(v^2+w_ell^2)/2.
Rq=sp.expand(em2a*(-2*(szz-az*sz)-sp.Rational(3,2)*sz**2-sp.Rational(1,2)*wz**2))

# Pointwise formulas.  Since dmu_r=H dmu,
# J'=int mu*(v_r+Hv), I'=int mu*(u_r+Hu).
Jdensity=sp.expand(srr+H*sr)
Idensity=sp.expand(arr+H*ar)
# Tangential orbit trace has a z-divergence whose integral vanishes.
# Compute exact residual and identify it.
Jres=sp.simplify(Jdensity-(6-Eorb))
Jdiv_expected=sp.simplify(-sp.exp(-a-s)*D(sp.exp(-a+s)*sz,z))
# Horizontal balance has a z-divergence too.
Ires=sp.simplify(Idensity-(3+Rq-Ezz))

# Find compact divergence representative for Ires by direct simplification.
# The horizontal residual is the opposite intrinsic orbit-trace divergence.
Idiv_candidate=sp.simplify(sp.exp(-a-s)*D(sp.exp(-a+s)*sz,z))

# Contracted Gauss formula in conventions E=Ric+3g:
# Rq = Rg-2 Ric_rr+H^2-|S|^2
#    = -6+H^2-|S|^2+tr(E)-2E_rr.
# Since tr(E)=E_rr+E_zz+E_orb, substitution into I' cancels E_zz
# and gives the exact turning defect E_orb-E_rr.
traceE=sp.expand(Err+Ezz+Eorb)
Rq_gauss=-6+H**2-(u**2+sp.Rational(1,2)*v**2+B0sq)+traceE-2*Err
gauss_res=sp.simplify(Rq-Rq_gauss)
turn_rhs=-3+2*u*v+sp.Rational(1,2)*v**2-B0sq+Eorb-Err
turn_point_res=sp.simplify(Idensity-turn_rhs)
turn_minus_Idiv=sp.simplify(turn_point_res-Idiv_candidate)

# Numerical periodic test, using analytic formulas and central differencing for I,J.
zv=np.linspace(0,2*np.pi,32768,endpoint=False)
def fields(rv):
    A=0.12*np.cos(zv)+0.03*np.cos(2*zv)
    S=-0.07*np.sin(zv)+0.025*np.cos(3*zv)
    W=0.18*np.sin(2*zv)+0.02*np.cos(zv)
    # Nontrivial even/odd radial polynomials; no field equation imposed.
    aa=A+rv*(0.15+0.04*np.cos(zv))+rv**2*(0.03*np.sin(zv))
    ss=S+rv*(-0.08+0.05*np.sin(2*zv))+rv**2*(0.02*np.cos(zv))
    ww=W+rv*(0.11*np.cos(3*zv))+rv**2*(-0.025*np.sin(zv))
    return aa,ss,ww

def dz_fft(f,order=1):
    n=len(f); kk=np.fft.fftfreq(n,1/n)
    return np.fft.ifft((1j*kk)**order*np.fft.fft(f)).real

def eval_all(rv):
    aa,ss,ww=fields(rv)
    # exact r derivatives of chosen polynomials
    ar_n=0.15+0.04*np.cos(zv)+2*rv*(0.03*np.sin(zv))
    sr_n=-0.08+0.05*np.sin(2*zv)+2*rv*(0.02*np.cos(zv))
    wr_n=0.11*np.cos(3*zv)+2*rv*(-0.025*np.sin(zv))
    arr_n=2*0.03*np.sin(zv); srr_n=2*0.02*np.cos(zv); wrr_n=-2*0.025*np.sin(zv)
    az_n=dz_fft(aa); sz_n=dz_fft(ss); wz_n=dz_fft(ww)
    szz_n=dz_fft(ss,2); wzz_n=dz_fft(ww,2)
    # convert b,c derivatives and residuals
    br_n=(sr_n+wr_n)/2; cr_n=(sr_n-wr_n)/2
    brr_n=(srr_n+wrr_n)/2; crr_n=(srr_n-wrr_n)/2
    bz_n=(sz_n+wz_n)/2; cz_n=(sz_n-wz_n)/2
    bzz_n=(szz_n+wzz_n)/2; czz_n=(szz_n-wzz_n)/2
    em=np.exp(-2*aa)
    Err_n=3-ar_n**2-arr_n-br_n**2-brr_n-cr_n**2-crr_n
    Ezz_n=3-ar_n**2-ar_n*br_n-ar_n*cr_n-arr_n+em*(az_n*bz_n+az_n*cz_n-bz_n**2-bzz_n-cz_n**2-czz_n)
    Ex_n=3-ar_n*br_n-br_n**2-br_n*cr_n-brr_n+em*(az_n*bz_n-bz_n**2-bz_n*cz_n-bzz_n)
    Ey_n=3-ar_n*cr_n-br_n*cr_n-cr_n**2-crr_n+em*(az_n*cz_n-bz_n*cz_n-cz_n**2-czz_n)
    Rq_n=em*(-2*(szz_n-az_n*sz_n)-1.5*sz_n**2-0.5*wz_n**2)
    mu_n=np.exp(aa+ss)
    mean=lambda f: float(np.mean(f)*2*np.pi)
    return {
      'V':mean(mu_n),'I':mean(mu_n*ar_n),'J':mean(mu_n*sr_n),
      'rhsJ':6*mean(mu_n)-mean(mu_n*(Ex_n+Ey_n)),
      'rhsI':3*mean(mu_n)+mean(mu_n*Rq_n)-mean(mu_n*Ezz_n),
      'gauss_integral_residual':mean(mu_n*(Rq_n-(-6+(ar_n+sr_n)**2-(ar_n**2+0.5*sr_n**2+0.5*wr_n**2)+(Err_n+Ezz_n+Ex_n+Ey_n)-2*Err_n))),
      'rhsTurnExact':mean(mu_n*(-3+2*ar_n*sr_n+0.5*sr_n**2-0.5*wr_n**2+(Ex_n+Ey_n)-Err_n)),
      'traceE':mean(mu_n*(Err_n+Ezz_n+Ex_n+Ey_n)),
    }
h=1e-5
m0=eval_all(0.217); mp=eval_all(0.217+h); mm=eval_all(0.217-h)
Ip=(mp['I']-mm['I'])/(2*h); Jp=(mp['J']-mm['J'])/(2*h)
num={
 'I_prime_fd':Ip,'I_rhs_direct':m0['rhsI'],
 'I_rhs_turn_exact':m0['rhsTurnExact'],
 'gauss_integral_residual':m0['gauss_integral_residual'],
 'J_prime_fd':Jp,'J_rhs':m0['rhsJ'],
 'I_error_direct':Ip-m0['rhsI'],
 'J_error':Jp-m0['rhsJ'],
}

out={
 'conventions':{
   'metric':'dr^2+e^{2a}dz^2+e^{sigma+w}dx^2+e^{sigma-w}dy^2',
   'E':'Ric+3g; all E components orthonormal',
   'dmu':'e^{a+sigma} dz','u':'a_r','v':'sigma_r','B0_norm_sq':'w_r^2/2'},
 'symbolic':{
   'J_point_residual':str(Jres),
   'J_divergence_expected':str(Jdiv_expected),
   'J_residual_minus_divergence':str(sp.simplify(Jres-Jdiv_expected)),
   'I_point_residual':str(Ires),
   'I_divergence_candidate':str(Idiv_candidate),
   'I_residual_minus_divergence':str(sp.simplify(Ires-Idiv_candidate)),
  'contracted_gauss_residual':str(gauss_res),
  'turn_point_residual':str(turn_point_res),
  'turn_residual_minus_intrinsic_divergence':str(turn_minus_Idiv),
 },
 'integrated_balances':{
  'J_prime':'6 V - integral tr_orbit(E) dmu',
  'I_prime':'3 V + integral R(q_r) dmu - integral E_zz dmu',
  'I_prime_gauss':'integral[-3+2uv+v^2/2-|B0|^2+E_orbit-E_rr] dmu',
  'correction':'The exact contracted Gauss equation contains tr(E)-2E_rr; after cancellation in I prime the defect is E_orbit-E_rr.',
  'turning_bound':'If ||E||_op<=delta and I first returns from negative values to 0, then 2Cov(u,v)+<v^2>/2-<|B0|^2> >= 3-3delta.'
 },
 'numerical_periodic_test':num,
}
path=Path(__file__).resolve().parents[1]/'data'/'step82_slice_balance.json'
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2)); print('wrote',path)
