"""Regular nut series for diagonal Bianchi IX Einstein metrics Ric=-6g.

Metric g=dt^2+sum a_i^2 sigma_i^2 with d sigma_i=2 sigma_j^sigma_k.
At a smooth nut (R^4), a_i=t+O(t^3).  We solve the Einstein equations and
constraint order by order and save the exact series for numerical ball tests.
"""
import json
from pathlib import Path
import sympy as sp

t=sp.symbols('t')
OUT=Path(__file__).resolve().parents[1]/'data'/'einstein_nut'
OUT.mkdir(parents=True,exist_ok=True)


def series(N=9):
    # smooth odd radial series in the fixed left-invariant gauge
    coeff={}
    A=[]
    unknown=[]
    for i in range(3):
        cs=sp.symbols('c%d_3:%d:2'%(i+1,N+1))  # not used: awkward range
        ai=t
        for k in range(3,N+1,2):
            c=sp.Symbol(f'c{i+1}_{k}')
            coeff[(i,k)]=c; unknown.append(c); ai += c*t**k
        A.append(ai)
    d1=[sp.diff(a,t) for a in A]; d2=[sp.diff(a,t,2) for a in A]
    V2=(A[0]*A[1]*A[2])**2
    eq=[]
    for i in range(3):
        j,k=(i+1)%3,(i+2)%3
        e=(d2[i]*V2+d1[i]*(d1[j]*A[j]*A[i]**2*A[k]**2+d1[k]*A[k]*A[i]**2*A[j]**2)
           -6*A[i]*V2-2*A[i]*(A[i]**4-(A[j]**2-A[k]**2)**2))
        eq.append(sp.expand(e))
    con=sp.expand(sum(d2[i]*A[i]*A[(i+1)%3]**2*A[(i+2)%3]**2 for i in range(3))-6*V2)
    sol={}; free=[]
    # Through N+4 determines the N-jet while leaving the two curvature parameters free.
    # Higher residual orders require coefficients beyond the truncation and must not be imposed.
    for order in range(0,N+5):
        cur=[]
        for e in eq+[con]:
            co=sp.factor(sp.expand(e).coeff(t,order).subs(sol))
            if co!=0: cur.append(co)
        if not cur: continue
        syms=sorted(set().union(*[c.free_symbols for c in cur]) & set(unknown)-set(sol),key=str)
        if not syms:
            bad=[sp.simplify(c) for c in cur if sp.simplify(c)!=0]
            if bad:
                print('inconsistent',order,bad[:2]); break
            continue
        ss=sp.solve(cur,syms,dict=True,simplify=False)
        if not ss:
            print('no solution',order,syms,cur[:2]); break
        s0=ss[0]
        for q,v in s0.items(): sol[q]=sp.factor(v.subs(sol))
        sol={q:sp.factor(v.subs(sol)) for q,v in sol.items()}
        und=[q for q in syms if q not in s0]
        free += und
        print('order',order,'solved',list(s0),'free',und,flush=True)
    allsym=set().union(*[v.free_symbols for v in sol.values()]) if sol else set()
    truefree=sorted((allsym|set(free)) & set(unknown)-set(sol),key=str)
    print('free',truefree)
    for q in sorted(sol,key=str): print(q,'=',sp.factor(sol[q]))
    res={str(q):sp.srepr(v) for q,v in sol.items()}
    res['_free']=[str(q) for q in truefree]; res['_N']=N
    (OUT/'series.json').write_text(json.dumps(res,indent=1)+'\n')

if __name__=='__main__': series(5)
