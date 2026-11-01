#!/usr/bin/env python3
"""Exact algebra supporting Step 75's reflection-core analysis."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

# 1. Linear anisotropy transfer.
x,k=sp.symbols('x k',positive=True,real=True)
A=1/(2*k*sp.exp(k));B=A*sp.exp(2*k)
psi=sp.simplify(A*sp.exp(x)*(x-1)+B*sp.exp(-x)*(x+1))
ode=sp.simplify(x**2*sp.diff(psi,x,2)-2*x*sp.diff(psi,x)-x**2*psi)
value_k=sp.simplify(psi.subs(x,k))
deriv_k=sp.simplify(sp.diff(psi,x).subs(x,k))
limit_0=sp.simplify(sp.limit(psi,x,0,dir='+'))

# 2. Normal identity. b=H-3 and E_rr=-H'-|S|^2+3, with |S|^2=3+2b+|B|^2.
r=sp.symbols('r',real=True)
b=sp.Function('b')(r); shear=sp.Function('q')(r); Err=sp.symbols('Err')
normal_res=sp.simplify((-sp.diff(b,r)-(3+2*b+shear)+3)-(-sp.diff(b,r)-2*b-shear))
weighted_res=sp.simplify(sp.diff(sp.exp(2*r)*b,r)-sp.exp(2*r)*(sp.diff(b,r)+2*b))

# 3. Two-dimensional shape algebra at a zero of H.
lambda1,lambda2=sp.symbols('lambda1 lambda2',real=True)
trace_zero_sub={lambda2:-lambda1}
norm2=sp.simplify((lambda1**2+lambda2**2).subs(trace_zero_sub))
det=sp.simplify((lambda1*lambda2).subs(trace_zero_sub))
Ktan=sp.simplify(-det)
K_minus_halfnorm=sp.simplify(Ktan-norm2/2)

# 4. Bookkeeping for the approximate center floor.
delta,e=sp.symbols('delta e',nonnegative=True,real=True)
# e=R_q+6=tr_T(E)-E_nn.  At downward H=0,
# K >= 3-e/2 and P_v=Ric_q(v,v)+3=e/2-K <= e-3.
# Do not bound e and E_vv separately: e-E_vv=E_11+E_22-E_nn.
Evv,E11,E22,Enn=sp.symbols('Evv E11 E22 Enn',real=True)
e_components=Evv+E11+E22-Enn
Klower=3-e/2
Pupper=sp.simplify(e/2-Klower)
Sprime_components=sp.simplify(Pupper.subs(e,e_components)-Evv)
Sprime_delta=sp.simplify(Sprime_components.subs({E11:delta,E22:delta,Enn:-delta}))

out={
 'linear_mode':{
  'x_equation_residual':str(ode),'psi_at_x_eq_k':str(value_k),
  'psi_x_at_x_eq_k':str(deriv_k),'limit_x_to_0':str(limit_0),
  'interpretation':'x=k exp(-t); psi(0)=1, psi_t(0)=0, lim_t_to_inf psi=sinh(k)/k'},
 'normal_balance':{
  'Err_rewrite_residual':str(normal_res),'weighted_derivative_residual':str(weighted_res),
  'identity':'(e^{2r}(H-3))\'=-e^{2r}(|S-I|^2+E_rr)'},
 'orbit_shape':{
  'trace_zero_norm_sq':str(norm2),'trace_zero_det':str(det),
  'tangent_gauss_curvature':str(Ktan),'K_minus_half_norm_sq':str(K_minus_halfnorm)},
 'approximate_center':{
  'scalar_error_bound':'|R_q+6|=|tr_T(E)-E_nn|<=4 delta',
  'K_lower_at_downward_H_zero':'3-(R_q+6)/2',
  'P_normal_upper_before_4d_tangential_error':str(Pupper),
  'direct_component_cancellation':'e-E_vv=E_11+E_22-E_nn',
  'Sprime_selected_direction_bound':str(Sprime_components),
  'Sprime_box_upper':str(Sprime_delta),
  'result':'some eigenvalue of S\'(0) <= -3+3 delta'}
}
path=Path(__file__).resolve().parents[1]/'data'/'step75_structural_identities.json'
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2));print('wrote',path)
