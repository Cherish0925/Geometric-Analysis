#!/usr/bin/env python3
"""Combinatorial/exponent checks for the Step 40 staggered continuation schedule.

Does not verify tensor coefficients, PDE existence, or terminal restart.
"""
from fractions import Fraction as Q

ok = []
def chk(name, cond, detail=''):
    ok.append((name,bool(cond),detail))

# Exhaust current/higher allocations in alpha+beta+gamma=m+2 with two cutoff factors.
for m in range(2,9):
    triples=[]
    for a in range(m+3):
        for b in range(m+3-a):
            g=m+2-a-b
            if g<=m+1 and a+b>=1:
                triples.append((a,b,g))
    high=[t for t in triples if t[2]>=m or t[0]>=m+1 or t[1]>=m+1]
    allowed=True
    bad=[]
    for a,b,g in high:
        pair=sorted((a,b))
        typ=None
        if g==m+1 and pair==[0,1]: typ='grad-current'
        elif g==m and pair in ([0,2],[1,1]): typ='current'
        elif g==1 and pair==[0,m+1]: typ='hard-jet-U1'
        elif g==0 and pair in ([0,m+2],[1,m+1]): typ='top-jet-U0'
        if typ is None:
            allowed=False; bad.append((a,b,g))
    chk(f'U_m high allocation exhaustion m={m}',allowed,f'bad={bad}')
    # No C_{m+1} U_j for j>=2 follows from total order.
    forbidden=[t for t in triples if max(t[0],t[1])==m+1 and t[2]>=2]
    chk(f'no current cutoff jet times U_j>=2 m={m}',not forbidden,f'forbidden={forbidden}')

# Current same-p products.
for p in [4,6,8,12,25]:
    chk(f'Z^2 V^(p-2) same-p p={p}',Q(2,p)+Q(p-2,p)==1)
    chk(f'Z V^(p-1) same-p p={p}',Q(1,p)+Q(p-1,p)==1)
    chk(f'two previous factors V^(p-1) p={p}',Q(1,2*p)+Q(1,2*p)+Q(p-1,p)==1)
    chk(f'squared previous factors with volume p={p}',
        Q(2,4*p)+Q(2,4*p)+Q(p-2,p)+Q(1,p)==1)

# Honest a-derivative structure: partitions of r into two nonnegative cutoff orders.
for r in range(2,11):
    pairs=[(s,r-s) for s in range(r+1)]
    top=[x for x in pairs if max(x)==r]
    internal=[x for x in pairs if min(x)>=1]
    chk(f'nabla^{r} a has exactly two chi*C_r edge terms',len(top)==2,f'top={top}')
    chk(f'nabla^{r} a internal terms lack forced chi',all(min(x)>=1 for x in internal))
    # For r=m+2, internal maximum cutoff order is m+1=r-1.
    chk(f'internal max derivative r={r}',max(max(x) for x in internal)==r-1)

# Current factor in second U sum i+j+k=m,k<=m-1: if j=m, then i=k=0.
for m in range(1,10):
    current=[]
    for i in range(m+1):
        for j in range(m+1-i):
            k=m-i-j
            if k<=m-1 and j==m:
                current.append((i,j,k))
    chk(f'current U_m coefficient is aT at m={m}',current==[(0,m,0)],f'{current}')

failed=[x for x in ok if not x[1]]
for i,(name,yes,detail) in enumerate(ok,1):
    print(f"{'PASS' if yes else 'FAIL'} {i}: {name}"+(f' -- {detail}' if detail else ''))
print(f"\n{len(ok)-len(failed)}/{len(ok)} combinatorial/exponent checks passed.")
print('NOT CHECKED: exact tensor provenance, commutator coefficients, PDE existence, terminal restart, smoothing, or Yau 26.')
raise SystemExit(1 if failed else 0)
