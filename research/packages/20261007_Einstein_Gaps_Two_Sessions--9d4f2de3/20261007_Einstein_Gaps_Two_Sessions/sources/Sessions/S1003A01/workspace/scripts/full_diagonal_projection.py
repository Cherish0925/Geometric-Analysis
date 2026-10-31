"""Pointwise/full functional projection of diagonal trace-free Ricci onto dual fields.

For a fixed computed cell, augment the two scalar Green shape fields and the relative-spin
field by smooth radial scalar multipliers.  The resulting finite Gram projection measures
how much of the full three-component diagonal Ricci variable is visible to these geometric
directions before one asks whether their moments can be controlled for every competitor.

This is a representation experiment, not a competitor-independent lower bound.
"""
import argparse,json,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parent))
from joint_dual_calibration import load_profile,greens,integrate,gram_bound


def evaluate(path,n,deg):
 rec,v,t,dtdv,W,z,e,ec,u,H,bspin,a=load_profile(path,n); mu=W*dtdv; G=greens(t,W)
 d13=np.array([-1.,0.,1.]); d21=np.array([1.,-1.,0.]); B=[]; names=[]
 # Polynomial multipliers in normalized geodesic radius.  Green fields already
 # carry the bolt-to-collar singular response and are also multiplied by powers.
 tau=t/t[-1]
 for k in range(deg+1):
  p=tau**k
  for tag,psi in [('p',p),('Gp',G*p)]:
   B += [-psi[:,None]*d13,-psi[:,None]*d21]
   names += [f'{tag}{k}_shape13',f'{tag}{k}_shape21']
 # Spin field and low-order radial multipliers.
 spin=a*bspin/W[:,None]
 for k in range(deg+1):
  B.append((tau**k)[:,None]*spin); names.append(f'p{k}_spin')
 B=np.stack(B,axis=1)
 P=integrate(mu*np.sum(z*z,axis=1),v)/4
 R=gram_bound(B,z,mu,v,names)
 R['share_of_P']=R['bound']/P
 return dict(record=path,n=n,degree=deg,P=P,projection=R)

def main():
 ap=argparse.ArgumentParser();ap.add_argument('record');ap.add_argument('--n',type=int,default=8001);ap.add_argument('--deg',type=int,default=3);ap.add_argument('--out')
 a=ap.parse_args();r=evaluate(a.record,a.n,a.deg);print(json.dumps(r,indent=1));
 if a.out:Path(a.out).write_text(json.dumps(r,indent=1)+'\n')
if __name__=='__main__':main()
