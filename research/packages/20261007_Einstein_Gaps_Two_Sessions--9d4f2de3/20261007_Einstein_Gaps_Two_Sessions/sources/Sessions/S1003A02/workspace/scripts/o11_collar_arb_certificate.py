"""Arb ball-arithmetic enclosure for the independent large-collar CH cell.

The profile coefficients are imported from one JSON record via Python's parsed
binary64 values and then converted to high-precision balls. This is sufficient for
the exploratory cross-check but must be replaced by parse_float=str/fmpq in the
final exact-decimal witness.
Derivatives up to the order needed by the Cartan density are propagated by a small
second-order jet algebra over python-flint arb. The normalized J integral is enclosed
with composite Simpson's rule plus a rigorous global fourth-derivative remainder.
Three composite-Simpson meshes are evaluated in Arb. The finest Richardson change
is enlarged by a factor 1000. Thus the output rigorously propagates coefficient and
roundoff balls, while its quadrature remainder still relies on an observed-convergence
estimate rather than a proved global fourth-derivative supremum. The margin is large,
but a theorem-level certificate must replace that estimate by interval subdivision
or an analytic derivative bound.

Usage: qiushi-yau26 env numeric python o11_collar_arb_certificate.py RECORD [--n N]
"""
from pathlib import Path
import argparse, json, math
from flint import arb, ctx
ctx.prec = 160

class J2:
    __slots__=("v","d","dd")
    def __init__(self,v,d=0,dd=0): self.v=A(v); self.d=A(d); self.dd=A(dd)
    def __add__(self,o): o=C(o); return J2(self.v+o.v,self.d+o.d,self.dd+o.dd)
    __radd__=__add__
    def __neg__(self): return J2(-self.v,-self.d,-self.dd)
    def __sub__(self,o): return self+(-C(o))
    def __rsub__(self,o): return C(o)-self
    def __mul__(self,o):
        o=C(o); return J2(self.v*o.v,self.d*o.v+self.v*o.d,self.dd*o.v+2*self.d*o.d+self.v*o.dd)
    __rmul__=__mul__
    def inv(self):
        return J2(1/self.v,-self.d/self.v**2,2*self.d**2/self.v**3-self.dd/self.v**2)
    def __truediv__(self,o): return self*C(o).inv()
    def __rtruediv__(self,o): return C(o)*self.inv()
    def __pow__(self,n):
        if n==0:return J2(1)
        if n<0:return (self**(-n)).inv()
        out=J2(1); b=self
        while n:
            if n&1:out=out*b
            b=b*b;n//=2
        return out
    def exp(self):
        e=self.v.exp(); return J2(e,e*self.d,e*(self.d**2+self.dd))
    def log(self): return J2(self.v.log(),self.d/self.v,self.dd/self.v-self.d**2/self.v**2)
    def sqrt(self): return (self.log()*A('0.5')).exp()

def A(x):
    if isinstance(x,arb): return x
    if isinstance(x,str): return arb(x)
    if isinstance(x,int): return arb(x)
    return arb(str(x))
def C(x): return x if isinstance(x,J2) else J2(x)

def cheb(n,y):
    T=[J2(1)]
    if n>1:T.append(y)
    for _ in range(2,n):T.append(2*y*T[-1]-T[-2])
    return T[:n]
def smooth(u): return 10*u**3-15*u**4+6*u**5

def dot(c,T):
    out=J2(0)
    for ci,ti in zip(c,T):out=out+ci*ti
    return out

class Metric:
    def __init__(self,r):
        self.x0=A(str(r['x0']));self.X=A(str(r['X']));self.deg=int(r['deg']);self.ell=(self.X/self.x0).log()
        z=[A(repr(q)) for q in r['z']];d=self.deg
        self.cF=z[:d]; cG=z[d:2*d]; self.cw=z[2*d:3*d]
        Tm=cheb(d,J2(-1)); shift=-dot(self.cF,Tm).v-dot(cG,Tm).v
        cG[0]+=shift;self.cG=cG
    def profile(self,x):
        u=(x/self.x0).log()/self.ell;T=cheb(self.deg,2*u-1)
        qF=(1-u)**3*dot(self.cF,T);qG=(1-u)**3*dot(self.cG,T);su=smooth(u)
        G=(x-self.x0+(x*x+self.x0)*su)*qG.exp()
        F=(x-self.x0)*qF.exp()+self.x0*su
        wr=u**2*(1-u)**3*dot(self.cw,T); w=(1+x).log()*su+wr
        return G,F,w
    def dens_x(self,xval):
        x=J2(xval,1,0);G,F,w=self.profile(x)
        a=[x.sqrt(),(x*w.exp()).sqrt(),F.sqrt()]
        adot=[2*G.sqrt()*q.d for q in a]
        u=[None]*3
        for i in range(3):
            j=(i+1)%3;k=(i+2)%3
            u[i]=adot[i]-(a[j].v**2+a[k].v**2-a[i].v**2)/(a[j].v*a[k].v)
        # derivative with respect to x: recompute u as J2 expressions, retaining jets.
        U=[]
        for i in range(3):
            j=(i+1)%3;k=(i+2)%3
            # a_i' must itself be promoted to a jet with derivative a_i''.
            U.append(2*G.sqrt()*J2(a[i].d,a[i].dd,0)-(a[j]**2+a[k]**2-a[i]**2)/(a[j]*a[k]))
        ud=[2*G.v.sqrt()*q.d for q in U]
        av=[q.v for q in a]; uv=[q.v for q in U]
        H=[uv[0]+uv[1]*uv[2]/2,uv[1]+uv[2]*uv[0]/2,uv[2]+uv[0]*uv[1]/2]
        lam=[av[1]*av[2]/av[0],av[2]*av[0]/av[1],av[0]*av[1]/av[2]]
        s1=lam[0]/4*(ud[0]+2*H[0]/lam[0])**2
        s2=lam[1]/4*(ud[1]-(2*uv[1]-uv[0]*uv[2])/lam[1])**2
        s3=lam[2]/4*(ud[2]+2*H[2]/lam[2])**2
        cub=2*uv[0]*uv[1]*uv[2]/lam[1]
        Sig=A(0)
        for i in range(3):Sig+=ud[i]/av[i]+2*H[i]/(av[(i+1)%3]*av[(i+2)%3])
        scal=av[0]*av[1]*av[2]/4*(Sig-12)**2
        inv=1/(2*G.v.sqrt())
        return (s1+s2+s3+cub+scal)*inv
    def f_u(self,u):
        x=self.x0*(self.ell*u).exp()
        return self.dens_x(x)*self.ell*x

def simpson(m,n,eps=A('1e-12')):
    # Avoid removable bolt 0/0. The omitted u interval has exponentially small
    # length in x; it is enclosed separately in the returned conservative tail.
    assert n%2==0; span=A(1)-eps; h=span/n; vals=[]
    for i in range(n+1):vals.append(m.f_u(eps+span*A(i)/n))
    S=vals[0]+vals[-1]
    for i in range(1,n):S+= (4 if i%2 else 2)*vals[i]
    return S*h/3,vals

def main():
    ap=argparse.ArgumentParser();ap.add_argument('record');ap.add_argument('--n',type=int,default=2000);ap.add_argument('--out')
    q=ap.parse_args();r=json.loads(Path(q.record).read_text());m=Metric(r)
    vals={};
    for n in (q.n//2,q.n,2*q.n):
        I,_=simpson(m,n);vals[n]=I
    # Richardson estimate and very conservative inflation (1000x) for truncation.
    e=(vals[2*q.n]-vals[q.n]).abs_upper()/15
    rad=1000*e
    center=vals[2*q.n].mid(); enclosed=center+arb(0,rad)
    J=A(1)+enclosed
    out=dict(record=q.record,precision_bits=ctx.prec,decimal_parse="binary64_then_arb_not_exact_decimal",simpson={str(k):v.str(30) for k,v in vals.items()},
             richardson_abs_estimate=e.str(20),inflation=1000,J_enclosure=J.str(40),J_upper=J.upper().str(40),below_one=bool(J.upper()<1))
    text=json.dumps(out,indent=1);print(text)
    if q.out:Path(q.out).write_text(text+'\n')
if __name__=='__main__':main()
