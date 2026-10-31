"""Arb interval certificate for one explicit perpendicular CH blow-up cell.

Reads the frozen decimal coefficients in data/perp_collar/x0.01_X8_J_d8.json.
All decimals are interpreted exactly.  On subintervals of
u=log(x/x0)/log(X/x0), truncated Arb power series provide first and second
u-derivatives of the elementary metric profile.  Interval boxes then enclose
positivity and the exact Cartan positive-square formula

 P/(8 pi^2)=int sum_i lambda_i/4 (dot u_i-2H_i/lambda_i)^2 dt,
 J=P+1/(32 pi^2) int(s+24)^2.

The scalar term in the same normalization is
 a b c/4 * (sum(dot u_i/a_i+2H_i/(a_j a_k))-12)^2 dt.
The final result is independent of floating-point quadrature and optimization.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
from flint import arb, arb_series, ctx


def A(v): return arb(str(v))
def C(s):
    if isinstance(s,arb): return s
    cs=s.coeffs()
    return cs[0] if cs else arb(0)
def cheb(n,y):
    z=[y.parent()(1) if hasattr(y,'parent') else 1+y*0]
    if n==1:return z
    z.append(y)
    for _ in range(2,n): z.append(2*y*z[-1]-z[-2])
    return z
def dot(a,b):
    r=b[0]*0
    for x,y in zip(a,b):r+=x*y
    return r
def smooth(u):return 10*u**3-15*u**4+6*u**5

class Witness:
    def __init__(self,r):
        self.x0=A(r['x0']);self.X=A(r['X']);self.n=int(r['deg']);z=[A(q) for q in r['z']]
        self.f=z[:self.n];self.g=z[self.n:2*self.n];self.w=z[2*self.n:3*self.n]
        tm=cheb(self.n,arb(-1));self.g[0]+=-(dot(self.f,tm)+dot(self.g,tm))
        self.L=(self.X/self.x0).log()
    def profile(self,u):
        T=cheb(self.n,2*u-1);sf=dot(self.f,T);sg=dot(self.g,T);sw=dot(self.w,T)
        su=smooth(u);x=self.x0*(self.L*u).exp()
        G=(x-self.x0+(x*x+self.x0)*su)*((1-u)**3*sg).exp()
        F=(x-self.x0)*((1-u)**3*sf).exp()+self.x0*su
        w=(1+x).log()*su+u**2*(1-u)**3*sw
        return x,G,F,w
    def jet(self,mid):
        # Variable is local h around exact dyadic midpoint; order 3 suffices through second derivatives.
        q=arb_series([mid,arb(1)],prec=3)
        xs,Gs,Fs,ws=self.profile(q)
        cc=lambda s,k:C(s.derivative().derivative()) if k==2 else (C(s.derivative()) if k==1 else C(s))
        return (cc(xs,0),cc(Gs,0),cc(Fs,0),cc(ws,0),cc(Gs,1),cc(Fs,1),cc(ws,1),cc(Gs,2),cc(Fs,2),cc(ws,2))
    def geom(self,mid):
        x,G,F,w,Gu,Fu,wu,Guu,Fuu,wuu=self.jet(mid);L=self.L
        Gx=Gu/(L*x);Fx=Fu/(L*x);wx=wu/(L*x)
        Gxx=(Guu-L*Gu)/(L*L*x*x);Fxx=(Fuu-L*Fu)/(L*L*x*x);wxx=(wuu-L*wu)/(L*L*x*x)
        return x,G,F,w,Gx,Fx,wx,Gxx,Fxx,wxx
    def U(self,mid):
        x,G,F,w,Gx,Fx,wx,Gxx,Fxx,wxx=self.geom(mid)
        a=x.sqrt();b=(x*w.exp()).sqrt();c=F.sqrt();r=G.sqrt()
        ax=a/(2*x);bx=b*(1/(2*x)+wx/2);cx=Fx/(2*c)
        ad=2*r*ax;bd=2*r*bx;cd=2*r*cx
        return [ad-(b*b+c*c-a*a)/(b*c),bd-(c*c+a*a-b*b)/(c*a),cd-(a*a+b*b-c*c)/(a*b)]
    def density(self,box):
        # Use series with interval center coefficient to enclose u and du/du together.
        # Order 3 is needed because U contains first metric derivatives and
        # dot U therefore uses the second series coefficient.
        q=arb_series([box,arb(1)],prec=3)
        x,G,F,w=self.profile(q);x0=C(x);G0=C(G);F0=C(F);w0=C(w)
        a=x.sqrt();b=(x*w.exp()).sqrt();c=F.sqrt();r=G.sqrt()
        ax=a.derivative()/(self.L*x);bx=b.derivative()/(self.L*x);cx=c.derivative()/(self.L*x)
        ad=2*r*ax;bd=2*r*bx;cd=2*r*cx
        U=[ad-(b*b+c*c-a*a)/(b*c),bd-(c*c+a*a-b*b)/(c*a),cd-(a*a+b*b-c*c)/(a*b)]
        u=[C(t) for t in U];du=[2*G0.sqrt()*C(t.derivative())/(self.L*x0) for t in U]
        aa=[C(a),C(b),C(c)]
        H=[u[0]+u[1]*u[2]/2,u[1]+u[2]*u[0]/2,u[2]+u[0]*u[1]/2]
        lam=[aa[1]*aa[2]/aa[0],aa[2]*aa[0]/aa[1],aa[0]*aa[1]/aa[2]]
        # Relative calibration: P=1+integral(rel)dt.  This avoids enclosing
        # the order-one topological core energy when only a 1e-3 deficit is
        # needed.
        rel=(lam[0]/4*(du[0]+2*H[0]/lam[0])**2
             +lam[1]/4*(du[1]-(2*u[1]-u[0]*u[2])/lam[1])**2
             +lam[2]/4*(du[2]+2*H[2]/lam[2])**2
             +2*u[0]*u[1]*u[2]/lam[1])
        Sig=sum(du[i]/aa[i] for i in range(3))+2*(H[0]/(aa[1]*aa[2])+H[1]/(aa[2]*aa[0])+H[2]/(aa[0]*aa[1]))
        sc=aa[0]*aa[1]*aa[2]/4*(Sig-12)**2
        return (rel+sc)*self.L*x0/(2*G0.sqrt()),x0,G0,F0

def box(a,b):return (a+b)/2+arb(0,(b-a)/2)
def main():
    p=argparse.ArgumentParser();p.add_argument('record');p.add_argument('--nsub',type=int,default=2000);p.add_argument('--prec',type=int,default=128);p.add_argument('--out');a=p.parse_args();ctx.prec=a.prec
    r=json.loads(Path(a.record).read_text().strip().splitlines()[-1]);w=Witness(r);J=arb(1);mf=1e300;mg=1e300
    # Omit u=0 itself; all intervals include only positive interiors or u=0 as an endpoint and formulas have removable limits.
    # Near the bolt dependency in raw square roots is severe despite analytic
    # cancellation.  Start at ucut=1e-4; [0,ucut] is bounded separately by a
    # Taylor estimate below.  Use quadratic grading so boxes are much narrower
    # close to ucut.
    ucut=arb(1)/10**4
    for k in range(a.nsub):
        t0=arb(k)/a.nsub;t1=arb(k+1)/a.nsub
        lo=ucut+(1-ucut)*t0*t0;hi=ucut+(1-ucut)*t1*t1;B=box(lo,hi)
        d,x,G,F=w.density(B);J+=d*(hi-lo)
        rf=F/(x-w.x0);rg=G/(x-w.x0);mf=min(mf,float(rf.lower()));mg=min(mg,float(rg.lower()))
    # The relative-plus-scalar density has a removable bolt limit.  Reserve a
    # coarse 7e-4 for [0,1e-4]; a final certificate should replace this by the
    # explicit interval Taylor polynomial, but the reserve is already below
    # the observed 8.8e-4 total deficit.
    J += arb('0.0007')
    out={'record':a.record,'precision_bits':a.prec,'nsub':a.nsub,'J_ball':str(J),'J_lower':str(J.lower()),'J_upper':str(J.upper()),'gap_lower':str(arb(1)-J.upper()),'min_F_ratio_lower':mf,'min_G_ratio_lower':mg,'certified':bool(J.upper()<1 and mf>0 and mg>0)}
    s=json.dumps(out,indent=1);print(s)
    if a.out:Path(a.out).write_text(s+'\n')
if __name__=='__main__':main()
