#!/usr/bin/env python3
"""Rigorous direct enclosure of the self-dual Weyl saving of the Step-33 cell.

Uses the already certified desingularized diagonal Bianchi-IX curvature variables.
For a diagonal metric dt^2+sum a_i^2 sigma_i^2, define
 K0i=-a_i''/a_i,
 Kjk=(a_i^4-(a_j^2-a_k^2)^2)/(a_i^2 a_j^2 a_k^2)-L_jL_k,
 C_i=(K0i+Kjk)/2.
The curvature block on Lambda^+ in the chosen orientation has diagonal C_i;
its trace-free part is W^+, so |W^+|^2=sum_i(C_i-s/12)^2.  The opposite
orientation is checked too.  On the CH collar, the correct block has
|W^+|^2=24 and the opposite block vanishes in the Ric=-6 normalization.
"""
import argparse,json,sys,time
from pathlib import Path
from flint import arb,acb,ctx
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'Sessions'/'S1003A01'/'workspace'/'scripts'))
from perp_rigorous_enclosure import FrozenCell,_dyadic,_dec  # noqa

class WeylCell(FrozenCell):
    def weyl(self,u,analytic=False):
        # This copies the cancellation-free geometric intermediates from ricci(),
        # retaining the sectional components needed for the two chiral blocks.
        # To avoid a second fragile derivation, recover D_i and algebraic A_i from
        # Ricci equations plus direct formulas by a local copy of the parent source.
        from perp_rigorous_enclosure import Jet,phi_derivs,phi_val,cheb_jets
        x0,ell=acb(self.x0),acb(self.ell); uj=Jet(u,1,0)
        xj=x0*Jet(ell*u,ell,0).exp(); p0,p1,p2=phi_derivs(ell*u); phij=Jet(p0,ell*p1,ell*ell*p2)
        yj=x0*ell*uj*phij; T=cheb_jets(self.deg,2*uj-1)
        CF=sum((T[k]*acb(self.cF[k]) for k in range(self.deg)),Jet(0)); CG=sum((T[k]*acb(self.cG[k]) for k in range(self.deg)),Jet(0)); CW=sum((T[k]*acb(self.cw[k]) for k in range(self.deg)),Jet(0))
        om=1-uj;om3=om*om*om;poly=10-15*uj+6*uj*uj
        FH=(om3*CF).exp()+uj*uj*poly/(ell*phij)
        GH=(1+(xj*xj+x0)*uj*uj*poly/(x0*ell*phij))*(om3*CG).exp()
        L1x=(1+xj).log(analytic=analytic);wj=L1x*uj*uj*uj*poly+uj*uj*om3*CW
        WH=(L1x.v*u*poly.v+om3.v*CW.v)/((x0*ell*p0)**2)
        x=xj.v
        def dx(f):
            fx=f.d/(ell*x); fxx=(f.dd-ell*f.d)/(ell*ell*x*x); return f.v,fx,fxx
        h1j=yj*FH;Gj=yj*GH;h3j=xj*wj.exp()
        h1,h1x,h1xx=dx(h1j);FHv,FHx,_=dx(FH);GHv,GHx,_=dx(GH);Gv,Gx,_=dx(Gj);h3,h3x,h3xx=dx(h3j)
        y=yj.v;w=wj.v;ew=w.exp();rho=GHv/FHv
        D1=2*rho*h1xx+h1x*(GHx*FHv-GHv*FHx)/(FHv*FHv)
        D2=Gx/x-Gv/(x*x)
        D3=Gx*h3x/h3+2*Gv*h3xx/h3-Gv*h3x*h3x/(h3*h3)
        L12=rho*h1x/x;L13=rho*h1x*h3x/h3;L23=Gv*h3x/(x*h3)
        E1=phi_val(w);shc=(E1+phi_val(-w))/2
        A1=2*h1/(x*h3)-2*y*y*y*WH*WH*E1*E1/(FHv*ew)
        A2=-4*y*WH*shc/FHv+4/x-2*h1/(x*x*ew)
        A3=4*y*WH*shc/FHv+4/(x*ew)-2*h1/(x*x*ew)
        R=[-(D1+D2+D3),-D1-L12-L13+A1,-D2-L12-L23+A2,-D3-L13-L23+A3];s=sum(R)
        # A_i=2*(algebraic sectional K_jk), hence K_jk=A_i/2.
        # In these conventions K_{0i}=-D_i and K_{jk}=A_i/2.
        # On the normalized chiral forms the diagonal curvature block is the
        # sectional sum K_{0i}+K_{jk}; no additional factor occurs in the
        # curvature-operator convention used by curvature_scalars.  The CH
        # collar then has one Weyl block of norm 24 and the other zero.
        Cp=[-D1+A1/2,-D2+A2/2,-D3+A3/2]
        Cm=[-D1-A1/2,-D2-A2/2,-D3-A3/2]
        wp=sum((c-s/12)**2 for c in Cp); wm=sum((c-s/12)**2 for c in Cm)
        vol=x*(w/2).exp()*(FHv/GHv).sqrt(analytic=analytic)*ell*x/8
        return wp,wm,vol

def enc(re):
    lo,up=_dyadic(re.lower()),_dyadic(re.upper())
    return {'ball':re.str(30,radius=True),'lower_dec_outward':_dec(lo,False),'upper_dec_outward':_dec(up,True),'lower_dyadic':[str(lo.numerator),str(lo.denominator)],'upper_dyadic':[str(up.numerator),str(up.denominator)]}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--record',default='Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json');ap.add_argument('--out',default='Sessions/S1003A02/workspace/data/step73_certified_wplus_direct.json');ap.add_argument('--prec',type=int,default=192);ap.add_argument('--tol',type=float,default=1e-16);ap.add_argument('--pieces',type=int,default=2);a=ap.parse_args();ctx.prec=a.prec
    rec=json.load(open(ROOT/a.record));c=WeylCell(rec);c.x0=arb(3)/100;c.ell=(c.X/c.x0).log()
    checks={}
    for u in ['0','0.5','1']:
        wp,wm,v=c.weyl(acb(arb(u)));checks[u]={'wp':wp.real.str(20,radius=True),'wm':wm.real.str(20,radius=True)}
    def integ(which):
        z=acb(0)
        def f(u,analytic):
            wp,wm,v=c.weyl(u,analytic);return (wp if which=='plus' else wm)*v
        for k in range(a.pieces):z+=acb.integral(f,arb(k)/a.pieces,arb(k+1)/a.pieces,rel_tol=a.tol,abs_tol=a.tol/a.pieces)
        return z.real
    t=time.time();plus=integ('plus');minus=integ('minus')
    # integrals are normalized by 8pi^2; CH plus integral on [0,X] is (12pi^2 X^2)/(8pi^2)=3X^2/2.
    ch=arb(3)*c.X*c.X/2; delta4=2*(ch-plus) # (W_CH^+-W_cell^+)/(4pi^2)
    loss=1-delta4;hcrit=1/(3*loss)
    out={'record':a.record,'prec':a.prec,'checks':checks,'seconds':time.time()-t,'Wplus_over_8pi2':enc(plus),'Wminus_over_8pi2':enc(minus),'CH_Wplus_over_8pi2':enc(ch),'delta':enc(delta4),'loss':enc(loss),'hcrit':enc(hcrit)}
    Path(ROOT/a.out).write_text(json.dumps(out,indent=1)+'\n');print(json.dumps(out,indent=1))
if __name__=='__main__':main()
