"""Compute exact/numerical first normal Taylor invariants of Step 94 charged data.

This uses only the prescribed Cauchy data and the Gauss-Codazzi Einstein evolution
formula, hence it is cheaper and more reliable than forward elliptic evolution.
It determines the initial direction of mean curvature, orbit area, base scale,
physical twist Q, and conserved coordinate charge.
"""
from pathlib import Path
import json, math
import numpy as np
import importlib.util

p=Path('workspace/scripts/step96_koiso_einstein_cauchy_evolution.py')
spec=importlib.util.spec_from_file_location('evol',p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

N=256; wind=1; S=1.0; Qmax=.5
s,q,k,meta=mod.initial_data(N,wind,S,Qmax)
qi=np.linalg.inv(q); gamma,ric,scalar=mod.christoffel_and_ricci(q)
W=np.einsum('nij,njk->nik',qi,k); H=np.trace(W,axis1=1,axis2=2)
K2=np.einsum('nij,nji->n',W,W)
kqik=np.einsum('nij,njk,nkl->nil',k,qi,k)
kn=ric+3*q-H[:,None,None]*k+2*kqik
qn=2*k
qnn=2*kn
# H_n = tr(q^{-1} K_n) - tr(q^{-1}q_n q^{-1}K) = tr(q^-1 K_n)-2|W|²
Hn=np.einsum('nij,nji->n',qi,kn)-2*K2

# Quotient block notation q=[[a2+v^TG^-1v,v^T],[v,G]], center has a=1,v=0.
G=q[:,1:,1:]; Gi=np.linalg.inv(G); v=q[:,1:,0]
Gn=qn[:,1:,1:]; vn=qn[:,1:,0]; qssn=qn[:,0,0]
Gnn=qnn[:,1:,1:]; vnn=qnn[:,1:,0]; qssnn=qnn[:,0,0]
# At center v=0, A=0. base a²=qss-v^T G^-1 v.
a2n=qssn
# second derivative of v^T Gi v at v=0 is 2 vn^T Gi vn.
a2nn=qssnn-2*np.einsum('ni,nij,nj->n',vn,Gi,vn)
an=.5*a2n
ann=.5*a2nn-.25*a2n*a2n
# rho=sqrt(det G); sigma_n=.5 tr(Gi Gn), sigma_nn formula.
sigman=.5*np.einsum('nij,nji->n',Gi,Gn)
sigmann=.5*(np.einsum('nij,nji->n',Gi,Gnn)-np.einsum('nij,njk,nkl,nli->n',Gi,Gn,Gi,Gn))
# Connection A=Gi v; A_n=Gi vn at center; A_nn=Gi vnn-2Gi Gn Gi vn.
Avecn=np.einsum('nij,nj->ni',Gi,vn)
Avecnn=np.einsum('nij,nj->ni',Gi,vnn)-2*np.einsum('nij,njk,nkl,nl->ni',Gi,Gn,Gi,vn)
# The base connection curvature in Gaussian coordinates is F_ns=A_n.
# In the non-orthogonal quotient base metric diag(a^2,1), the orthonormal
# coefficient is f=A_n/a.  Coordinate charge is rho*G*f.
charge=np.einsum('nij,nj->ni',G,Avecn)
# Qphys=.5 f^T G f. Differentiate f=A_n/a at the center.
fn=Avecnn-an[:,None]*Avecn
Qphys=.5*np.einsum('ni,nij,nj->n',Avecn,G,Avecn)
Qn=np.einsum('ni,nij,nj->n',fn,G,Avecn)+.5*np.einsum('ni,nij,nj->n',Avecn,Gn,Avecn)
# qcoord_n = sigma_n qcoord + G_n f + G f_n at rho=a=1.
charge_n=sigman[:,None]*charge+np.einsum('nij,nj->ni',Gn,Avecn)+np.einsum('nij,nj->ni',G,fn)

out={
 'parameters':meta,
 'initial_constraints':{
   'H_abs_max':float(abs(H).max()),'K2_range':[float(K2.min()),float(K2.max())],
   'scalar_range':[float(scalar.min()),float(scalar.max())],
 },
 'first_second_normal_invariants':{
   'H_n_range':[float(Hn.min()),float(Hn.max())],
   'H_n_expected_constant':2.0,
   'base_a_n_range':[float(an.min()),float(an.max())],
   'base_a_nn_range':[float(ann.min()),float(ann.max())],
   'sigma_n_range':[float(sigman.min()),float(sigman.max())],
   'sigma_nn_range':[float(sigmann.min()),float(sigmann.max())],
   'connection_A_n_abs_max':float(abs(Avecn).max()),
   'connection_A_nn_abs_max':float(abs(Avecnn).max()),
   'physical_Q_range':[float(Qphys.min()),float(Qphys.max())],
   'physical_Q_n_range':[float(Qn.min()),float(Qn.max())],
   'coordinate_charge_means':[float(x) for x in charge.mean(axis=0)],
   'coordinate_charge_std':[float(x) for x in charge.std(axis=0)],
   'coordinate_charge_n_abs_max':float(abs(charge_n).max()),
 },
 'interpretation':(
   'For the sign K=+q_n/2 used here, the exact Einstein germ initially has H_n=2; '
   'the opposite normal reverses K but not H_n at the same minimal slice. Both sides '
   'therefore initially expand away from the stable separator. Coordinate charge is '
   'constant along s to numerical precision, while physical Q varies through M.'
 )
}
path=Path('workspace/data/step96_initial_taylor_invariants.json');path.write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
