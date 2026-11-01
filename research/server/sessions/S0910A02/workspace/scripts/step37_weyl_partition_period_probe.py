#!/usr/bin/env python3
"""Corrected Step 37 generalized Weyl partition-period probe.

The axis is partitioned into semi-infinite and finite intervals, each carrying
source density 1/2 for exactly one coordinate.  This is the source constraint
U1+U2=log r.  Finite same-label intervals correspond to multiple bolts for a
single circle.  Smoothness requires one global period per circle, so the
log-period coefficient ell_j = nu-(U_i-log r) must be equal for all finite rods
with label i, up to one global coordinate rescaling.

This remains a noncompact Weyl-line probe; compact toric polygon closure is a
separate monodromy problem.
"""
import json, math, os
from dataclasses import dataclass
from typing import List, Optional, Tuple
from scipy.integrate import quad

@dataclass
class Segment:
    a: Optional[float]  # None for -infty
    b: Optional[float]  # None for +infty
    label: int

    def finite(self): return self.a is not None and self.b is not None
    def contains_mid(self): return self.finite()
    def mid(self): return 0.5*(self.a+self.b)
    def length(self): return self.b-self.a if self.finite() else math.inf


def finite_pot(a,b,r,z):
    L=b-a; Ra=math.hypot(r,z-a); Rb=math.hypot(r,z-b); A=Ra+Rb
    u=0.5*(math.log(A-L)-math.log(A+L))
    denom=A*A-L*L
    ur=L*r*(1/Ra+1/Rb)/denom
    uz=L*((z-a)/Ra+(z-b)/Rb)/denom
    return u,ur,uz


def semi_right_pot(a,r,z):
    s=z-a; R=math.hypot(r,s)
    # potential of [a,+infty), up to additive constant
    u=0.5*math.log(R-s)
    ur=r/(2*R*(R-s))
    uz=-1/(2*R)
    return u,ur,uz


def semi_left_pot(b,r,z):
    s=z-b; R=math.hypot(r,s)
    # potential of (-infty,b], up to additive constant
    u=0.5*math.log(R+s)
    ur=r/(2*R*(R+s))
    uz=1/(2*R)
    return u,ur,uz


def U1_derivs(segments: List[Segment], r,z):
    U=Ur=Uz=0.0
    for seg in segments:
        if seg.label != 1: continue
        if seg.a is None:
            u,ur,uz=semi_left_pot(seg.b,r,z)
        elif seg.b is None:
            u,ur,uz=semi_right_pot(seg.a,r,z)
        else:
            u,ur,uz=finite_pot(seg.a,seg.b,r,z)
        U+=u; Ur+=ur; Uz+=uz
    return U,Ur,Uz


def nu_derivs(segments,r,z):
    U1,U1r,U1z=U1_derivs(segments,r,z)
    U2r=1/r-U1r; U2z=-U1z
    nur=-r*(U1r*U2r - U1z*U2z)
    nuz=-r*(U1r*U2z + U1z*U2r)
    return nur,nuz


def compute_nu(segments,r_target,z_target):
    finite_bounds=[x for seg in segments for x in (seg.a,seg.b) if x is not None]
    zmin=min(finite_bounds); zmax=max(finite_bounds); span=zmax-zmin
    R=max(80*span,80.0); z_ref=0.5*(zmin+zmax)
    if z_target>=z_ref:
        horiz=quad(lambda zz: nu_derivs(segments,R,zz)[1],z_ref,z_target,epsabs=1e-9,epsrel=1e-9,limit=300)[0]
    else:
        horiz=-quad(lambda zz: nu_derivs(segments,R,zz)[1],z_target,z_ref,epsabs=1e-9,epsrel=1e-9,limit=300)[0]
    vert=-quad(lambda rr: nu_derivs(segments,rr,z_target)[0],r_target,R,epsabs=1e-9,epsrel=1e-9,limit=500)[0]
    return horiz+vert


def log_period_coeff(segments, seg, eps=1e-5):
    z=seg.mid(); r=eps*max(1.0,seg.length())
    nu=compute_nu(segments,r,z)
    U1,_,_=U1_derivs(segments,r,z)
    if seg.label==1:
        V=U1-math.log(r)
    else:
        U2=math.log(r)-U1
        V=U2-math.log(r)
    return nu-V


def alternating_partition(m_finite:int, lengths=None, left_label=2):
    if lengths is None: lengths=[1.0]*m_finite
    segs=[]; z=0.0; label=3-left_label
    segs.append(Segment(None,0.0,left_label))
    for L in lengths:
        segs.append(Segment(z,z+L,label)); z+=L; label=3-label
    segs.append(Segment(z,None,label))
    return segs


def summarize(name,segs):
    rows=[]
    for i,seg in enumerate(segs):
        if not seg.finite(): continue
        ell=log_period_coeff(segs,seg)
        rows.append({"finite_segment_index":i,"label":seg.label,"a":seg.a,"b":seg.b,"length":seg.length(),"ell":ell})
    by={}
    for label in [1,2]:
        vals=[r["ell"] for r in rows if r["label"]==label]
        by[str(label)]={"count":len(vals),"range":max(vals)-min(vals) if vals else 0,"exp_range_ratio":math.exp(max(vals)-min(vals)) if vals else 1,"values":vals}
    return {"name":name,"segments":[seg.__dict__ for seg in segs],"rows":rows,"by_label":by}


def main():
    cases=[]
    for m in [4,6,8,10]: cases.append(summarize(f"equal_{m}_finite_left2", alternating_partition(m,left_label=2)))
    cases.append(summarize("m6_perturbed_left2", alternating_partition(6,[1.0,1.2,0.9,1.1,0.95,1.05],2)))
    cases.append(summarize("m8_perturbed_left2", alternating_partition(8,[1.0,1.2,0.8,1.1,0.95,1.05,1.3,0.9],2)))
    out={
      "title":"Step 37 corrected generalized Weyl partition period probe",
      "scope":"Noncompact Weyl-line source partition probe; not compact polygon closure and not proof/refutation of Yau-26.",
      "method":"Axis is partitioned so exactly one coordinate has density-1/2 source on every axis segment; U2=log r-U1. Same-label finite rods must share ell=nu-(U_i-log r) for a single global period.",
      "cases":cases,
      "review_use":"This supports only the qualitative correction that alternating adjacent labels do not eliminate rod-period mismatch. The compact alpha-family requires a closed-polygon transport/monodromy computation."}
    path="Sessions/S0910A02/workspace/data/step37_weyl_partition_period_probe.json"
    os.makedirs(os.path.dirname(path),exist_ok=True)
    with open(path,"w") as f: json.dump(out,f,indent=2)
    print(json.dumps({"output":path,"summaries":[{"name":c["name"],"by_label":c["by_label"]} for c in cases]},indent=2))

if __name__=='__main__': main()
