#!/usr/bin/env python3
"""Rigorous W+ saving using certified P and direct certified relative ∫s².

The relative Chern--Weil identity for the one-blow-up CH-collared cell is
 P/(8π²) - 1 = 4 ΔW+/(8π²) + ΔS/(96π²).
The existing Arb P certificate and the same bolt-regular Arb evaluator give the
right side without any Yamabe solve.  Here ΔS is integrated directly against
the CH density s_CH²=576, so no subtraction of huge absolute integrals occurs.
"""
import argparse,json,sys,time
from pathlib import Path
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'Sessions'/'S1003A01'/'workspace'/'scripts'))
from perp_rigorous_enclosure import FrozenCell,_dyadic,_dec  # noqa

def enc(x):
 lo,up=_dyadic(x.lower()),_dyadic(x.upper());return {'ball':x.str(30,radius=True),'lower_dec_outward':_dec(lo,False),'upper_dec_outward':_dec(up,True),'lower_dyadic':[str(lo.numerator),str(lo.denominator)],'upper_dyadic':[str(up.numerator),str(up.denominator)]}
def hull(obj):
 ln,ld=map(int,obj['lower_dyadic']);un,ud=map(int,obj['upper_dyadic']);return arb.union(arb(ln)/ld,arb(un)/ud)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--record',default='Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json');ap.add_argument('--P',default='Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_P_exact.json');ap.add_argument('--out',default='Sessions/S1003A02/workspace/data/step73_certified_wplus_identity.json');ap.add_argument('--prec',type=int,default=192);ap.add_argument('--tol',type=float,default=1e-16);ap.add_argument('--pieces',type=int,default=2);a=ap.parse_args();ctx.prec=a.prec
 r=json.load(open(ROOT/a.record));c=FrozenCell(r);c.x0=arb(3)/100;c.ell=(c.X/c.x0).log()
 def f(u,analytic):
  R,v,pr=c.ricci(u,analytic,want_profile=True);vch=pr['x']*c.ell*pr['x']/8;s=sum(R)
  return (s*s*v-576*vch)/12 # Delta S/(96pi²), since v=dV/(8pi²)
 z=acb(0);t=time.time()
 for k in range(a.pieces):z+=acb.integral(f,arb(k)/a.pieces,arb(k+1)/a.pieces,rel_tol=a.tol,abs_tol=a.tol/a.pieces)
 ds96=z.real;p=hull(json.load(open(ROOT/a.P))['P'])
 fourdwp=p-1-ds96 # 4 DeltaW+/(8pi²)=DeltaW+/(2pi²)
 delta=-fourdwp/2 # (W_CH-W_cell)/(4pi²)
 loss=1-delta;hcrit=1/(3*loss)
 out={'record':a.record,'prec':a.prec,'seconds':time.time()-t,'p':enc(p),'ds96':enc(ds96),'fourdwp':enc(fourdwp),'delta':enc(delta),'loss':enc(loss),'hcrit':enc(hcrit)}
 Path(ROOT/a.out).write_text(json.dumps(out,indent=1)+'\n');print(json.dumps(out,indent=1))
if __name__=='__main__':main()
