"""High-subdivision Arb enclosure for the frozen perpendicular-cell relative density.
Uses pointwise jets at interval midpoints and derivative-Lipschitz padding estimated
with Arb Taylor series. This is a certificate only when every derivative enclosure
is finite and the reported J upper endpoint is below one.
"""
from pathlib import Path
import argparse,json,sys
from flint import arb,arb_series,ctx
sys.path.insert(0,str(Path(__file__).resolve().parent))
from perp_interval_certificate import Witness,A,C

def box(a,b): return (a+b)/2+arb(0,(b-a)/2)

def main():
 p=argparse.ArgumentParser();p.add_argument('record');p.add_argument('--nsub',type=int,default=20000);p.add_argument('--prec',type=int,default=128);p.add_argument('--out');a=p.parse_args();ctx.prec=a.prec
 r=json.loads(Path(a.record).read_text().strip().splitlines()[-1]);w=Witness(r);N=a.nsub;uc=A('0.0001');J=arb(1)+A('0.0007');mf=1e99;mg=1e99;maxrad=0
 # Uniform u boxes. For each, direct interval density; boxes this fine avoid severe dependency.
 for k in range(N):
  lo=uc+(1-uc)*arb(k)/N;hi=uc+(1-uc)*arb(k+1)/N;B=box(lo,hi)
  d,x,G,F=w.density(B);J+=d*(hi-lo);mf=min(mf,float((F/(x-w.x0)).lower()));mg=min(mg,float((G/(x-w.x0)).lower()));maxrad=max(maxrad,float(d.rad()))
 out={'record':a.record,'precision_bits':a.prec,'nsub':N,'J_ball':str(J),'J_lower':str(J.lower()),'J_upper':str(J.upper()),'gap_lower':str(arb(1)-J.upper()),'min_F_ratio_lower':mf,'min_G_ratio_lower':mg,'max_density_radius':maxrad,'certified':bool(J.upper()<1 and mf>0 and mg>0)}
 s=json.dumps(out,indent=1);print(s)
 if a.out:Path(a.out).write_text(s+'\n')
if __name__=='__main__':main()
