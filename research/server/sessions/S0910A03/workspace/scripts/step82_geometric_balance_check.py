#!/usr/bin/env python3
"""Derive the Step 82 slice balances from the 3+1 hypersurface equations.

This check avoids coordinate-component ambiguity.  For q_r a metric on T^3,
S=diag(u,B), H=u+v, and E=Ric_g+3g, use
  S' + H S = Ric(q)+3I-E_T,
  R(q) = -6 + H^2-|S|^2 + 2 E_rr.
The first equation follows from Ric_g|_{Tq}=Ric_q-S'-HS.
Trace its orbit and horizontal blocks and integrate against dmu_q.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

# Formal scalar symbols for the radial terms and defect components.
u,v,B0sq,Rq,Rzz,Rorb,Err,Ezz,Eorb=sp.symbols(
    'u v B0sq Rq Rzz Rorb Err Ezz Eorb', real=True)
# Flat T^2 orbits imply scalar Rq=Rzz+Rorb, but Rorb is an intrinsic
# divergence under the slice integral (with dmu_q).
H=u+v
# Tangential evolution traces.
Jdensity=sp.expand(Rorb+6-Eorb)            # v'+Hv
Idensity=sp.expand(Rzz+3-Ezz)              # u'+Hu
I_using_scalar=sp.expand(Rq-Rorb+3-Ezz)
# After integration int Rorb dmu=0.
I_integrated_density=sp.expand(Rq+3-Ezz)
# Contracted Gauss relation in E=Ric+3g conventions:
# Rq=-6+H^2-|S|^2+tr(E)-2E_rr.
Ssq=u**2+sp.Rational(1,2)*v**2+B0sq
traceE=Err+Ezz+Eorb
Rq_gauss=-6+H**2-Ssq+traceE-2*Err
I_gauss=sp.expand(I_integrated_density.subs(Rq,Rq_gauss))
expected=-3+2*u*v+sp.Rational(1,2)*v**2-B0sq+Eorb-Err

out={
 'conventions':{
  'E':'Ric_g+3g','S_prime_equation':'S_prime+H S=Ric(q)+3I-E_T',
  'contracted_gauss':'R(q)=-6+H^2-|S|^2+tr(E)-2E_rr',
  'S_norm':'u^2+v^2/2+|B0|^2'},
 'pointwise_block_traces':{
  'v_prime_plus_Hv':str(Jdensity),
  'u_prime_plus_Hu':str(Idensity),
  'Rq_decomposition':'R(q)=Ric_q(zz)+tr_orbit Ric_q'},
 'integrated':{
  'intrinsic_orbit_trace_integral':'0 on each closed free-T2 slice (Einstein-Hilbert variation under orbit homothety / direct divergence)',
  'J_prime':'6V-integral E_orbit dmu',
  'I_prime':'3V+integral R(q)dmu-integral E_zz dmu',
  'I_prime_gauss_density':str(sp.simplify(I_gauss)),
  'expected_density':str(expected),
  'identity_residual':str(sp.simplify(I_gauss-expected))},
 'defect_formula':{
  'exact_defect':'E_orbit-E_rr',
  'reason':'tr(E)-2E_rr-E_zz = E_orbit-E_rr after insertion into I prime',
  'traceE_symbol':str(traceE)}, 
 'first_return':{
  'facts':'I=0 implies <u>=0; hence <uv>=Cov(u,v). At a differentiable first return from I<0, I_prime>=0.',
  'necessary_inequality':'2 Cov(u,v)+<v^2>/2-<|B0|^2> >= 3-3delta',
  'interpretation':'Mean reversal requires orbit expansion variance/correlation to beat radial orbit shear; this is necessary, not sufficient.'}
}
p=Path(__file__).resolve().parents[1]/'data'/'step82_geometric_balance.json'
p.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2)); print('wrote',p)
