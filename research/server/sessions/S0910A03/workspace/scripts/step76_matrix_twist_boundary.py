#!/usr/bin/env python3
"""Verify the non-diagonal T^2-orbit / Li--Liu boundary identities.

Metric on T^3:
    q = exp(phi(z)) (dz^2 + dx^2) + (dy + A(z) dx)^2.
For a Type-I Li--Liu PE boundary, A_z=(1/2) exp(phi) p,
where p=v_xi(0,z) is the nonlinear Dirichlet-to-Neumann datum.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

z,x,y=sp.symbols('z x y', real=True)
phi=sp.Function('phi')(z)
AA=sp.Function('A')(z)
coords=[z,x,y]
G=sp.Matrix([
    [sp.exp(phi),0,0],
    [0,sp.exp(phi)+AA**2,AA],
    [0,AA,1],
])
Gi=sp.simplify(G.inv())
n=3
Gamma=[[[0 for k in range(n)] for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            Gamma[k][i][j]=sp.simplify(sp.Rational(1,2)*sum(
                Gi[k,l]*(sp.diff(G[l,j],coords[i])+sp.diff(G[l,i],coords[j])-sp.diff(G[i,j],coords[l]))
                for l in range(n)))
Ric=sp.zeros(n)
for i in range(n):
    for j in range(n):
        Ric[i,j]=sp.simplify(sum(
            sp.diff(Gamma[k][i][j],coords[k])-sp.diff(Gamma[k][i][k],coords[j])
            +sum(Gamma[k][k][l]*Gamma[l][i][j]-Gamma[k][j][l]*Gamma[l][i][k] for l in range(n))
            for k in range(n)))
R=sp.factor(sp.simplify(sum(Gi[i,j]*Ric[i,j] for i in range(n) for j in range(n))))

# Substitute the Type-I boundary connection law A'=exp(phi)*p/2.
p=sp.Function('p')(z)
R_sub=sp.factor(R.subs(sp.diff(AA,z)**2,sp.exp(2*phi)*p**2/4))

# Unimodular orbit matrix and its H^2 target energy.
# Orbit block in (x,y), rho=sqrt(det)=exp(phi/2).
rho=sp.exp(phi/2)
Gorb=G[1:3,1:3]
U=sp.simplify(Gorb/rho)
Us=sp.simplify(sp.exp(-phi/2)*sp.diff(U,z))  # d/ds, ds=exp(phi/2) dz
Uinv=sp.simplify(U.inv())
M=sp.simplify(Uinv*Us)
Henergy=sp.factor(sp.simplify(sp.trace(M*M)/2))
Henergy_sub=sp.factor(Henergy.subs(sp.diff(AA,z)**2,sp.exp(2*phi)*p**2/4))
h=sp.simplify(sp.exp(-phi/2)*sp.diff(sp.log(rho),z))

# Boundary relation from W=1-xi*v_xi/2:
# (W exp(v))_xi at xi=0 equals exp(phi)*p/2.
xi=sp.symbols('xi', real=True)
v=sp.Function('v')(xi,z)
W=1-sp.Rational(1,2)*xi*sp.diff(v,xi)
boundary_curv=sp.simplify(sp.diff(W*sp.exp(v),xi).subs(xi,0))
# Replace boundary v and v_xi by symbols for readable output.
ph0,p0=sp.symbols('phi p', real=True)
boundary_curv_readable=boundary_curv.xreplace({v.subs(xi,0):ph0,sp.Subs(sp.diff(v,xi),xi,0):p0})

out={
  'metric':'q=e^phi(dz^2+dx^2)+(dy+A dx)^2',
  'scalar_curvature':str(R),
  'typeI_connection_law':'A_z=(1/2)e^phi p, p=v_xi(0,z)',
  'scalar_after_connection_law':str(R_sub),
  'expected_scalar':'-exp(-phi)*phi_zz-p^2/8',
  'orbit_rho':str(rho),
  'unimodular_orbit_matrix':str(U),
  'H2_target_energy_ds':str(Henergy),
  'H2_target_energy_after_connection_law':str(Henergy_sub),
  'mean_orbit_rate_h':str(h),
  'exact_R_minus6_integrated_consequence':'int e^phi p^2 dz = 48 int e^phi dz',
  'boundary_curvature_direct_formula':str(boundary_curv),
  'boundary_curvature_at_v_phi_p':'exp(phi)*p/2',
  'interpretation':'Li-Liu nonconstant boundary data activates the off-diagonal orbit/twist direction; diagonal scalar anisotropy is only a geodesic subspace of the SPD(2)/scale target.'
}
path=Path(__file__).resolve().parents[1]/'data'/'step76_matrix_twist_boundary.json'
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2)); print('wrote',path)
