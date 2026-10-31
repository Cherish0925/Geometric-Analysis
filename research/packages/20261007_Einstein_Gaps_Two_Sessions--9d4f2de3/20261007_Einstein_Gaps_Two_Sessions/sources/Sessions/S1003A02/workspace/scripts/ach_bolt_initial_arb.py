"""Pure-Arb enclosure of the n=1 regular Einstein bolt series used by ach_bolt_capd.cpp.

The retained series is the exact order-6/7 solution in data/einstein_bolt/series_n1.json,
parametrized by b=4/5 and d=p4-q4.  For a supplied d interval and dyadic t0, this script
encloses the polynomial initial state X=(m,delta,L3,ym,eta,y3,d) and emits outward-rounded
binary64 endpoints suitable for CAPD.  This encloses the displayed truncated polynomial;
a Fuchsian tail estimate remains a separate mathematical obligation.
"""
import argparse, json, math
from pathlib import Path
from flint import arb, ctx
import sympy as sp

HERE=Path(__file__).resolve().parent
SER=HERE.parent/'data'/'einstein_bolt'/'series_n1.json'

def A(q): return arb(str(q))

def endpoints(x):
    """Outward binary64 endpoints from an Arb ball."""
    lo=float(x.lower()); hi=float(x.upper())
    lo=math.nextafter(lo,-math.inf); hi=math.nextafter(hi,math.inf)
    return [lo,hi]

def init_box(dlo,dhi,t0,b=arb(4)/5):
    rec=json.loads(SER.read_text())
    bs,ds=sp.symbols('b d', positive=True)
    q4,q6=sp.symbols('q4 q6')
    loc={'Integer':sp.Integer,'Rational':sp.Rational,'Symbol':sp.Symbol,'Mul':sp.Mul,
         'Add':sp.Add,'Pow':sp.Pow}
    vals={k:sp.sympify(v,locals=loc) for k,v in rec.items() if not k.startswith('_')}
    # Algebraically use d=p4-q4 and the lower-order solution to determine q6.
    p4=vals['p4']; qq4=vals['q4']
    q6sol=sp.solve(sp.Eq(p4-qq4,ds),q6)[0]
    subs={sp.Symbol('b', positive=True):bs, q6:q6sol}
    coeff={k:sp.factor(v.subs(subs)) for k,v in vals.items()}
    # Exact Arb evaluator via recursive sympy traversal.
    d=arb.union(arb(str(dlo)),arb(str(dhi)))
    env={bs:b,ds:d}
    def ev(e):
        if e.is_Integer: return arb(int(e))
        if e.is_Rational: return arb(int(e.p))/int(e.q)
        if e.is_Symbol: return env[e]
        if e.is_Add:
            z=arb(0)
            for a in e.args: z += ev(a)
            return z
        if e.is_Mul:
            z=arb(1)
            for a in e.args: z *= ev(a)
            return z
        if e.is_Pow:
            base,ex=e.args
            if ex.is_Integer: return ev(base)**int(ex)
        raise ValueError(e)
    # q6 is the free coefficient solved above, while p4 and q4 then differ by d.
    coeff['q6']=sp.factor(q6sol)
    P=[arb(0)]+[ev(coeff[f'p{k}']) for k in range(1,7)]
    Q=[arb(0)]+[ev(coeff[f'q{k}']) for k in range(1,7)]
    # r2..r7; a3=t + sum r_k t^k
    R={k:ev(coeff[f'r{k}']) for k in range(2,8)}
    t=arb(str(t0))
    a1=b+sum((P[k]*t**k for k in range(1,7)),arb(0))
    a2=b+sum((Q[k]*t**k for k in range(1,7)),arb(0))
    da1=sum((k*P[k]*t**(k-1) for k in range(1,7)),arb(0))
    da2=sum((k*Q[k]*t**(k-1) for k in range(1,7)),arb(0))
    a3=t+sum((R[k]*t**k for k in range(2,8)),arb(0))
    da3=arb(1)+sum((k*R[k]*t**(k-1) for k in range(2,8)),arb(0))
    L1=a1.log(); L2=a2.log(); L3=a3.log()
    y1=da1/a1; y2=da2/a2; y3=da3/a3
    X=[(L1+L2)/2,L1-L2,L3,(y1+y2)/2,y1-y2,y3,d]
    return X, q6sol, coeff

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--dlo',type=float,required=True); ap.add_argument('--dhi',type=float,required=True)
    ap.add_argument('--t0',type=float,default=0.01); ap.add_argument('--bits',type=int,default=256); ap.add_argument('--out')
    a=ap.parse_args(); ctx.prec=a.bits
    X,q6,coeff=init_box(a.dlo,a.dhi,a.t0)
    out={'b':'4/5','d':[a.dlo,a.dhi],'t0':a.t0,'bits':a.bits,'binary64_box':[endpoints(x) for x in X],
         'arb':[str(x) for x in X],'q6_of_b_d':str(q6)}
    text=json.dumps(out,indent=1); print(text)
    if a.out: Path(a.out).write_text(text+'\n')
