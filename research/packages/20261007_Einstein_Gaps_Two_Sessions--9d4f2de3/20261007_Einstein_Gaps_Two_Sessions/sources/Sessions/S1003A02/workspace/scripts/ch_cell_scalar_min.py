"""Sample the certified x0=3/100, X=64 CH cell's scalar curvature.

Uses the same desingularized FrozenCell formulas as the Arb enclosure.  This is
a dense floating profile plus local scalar minimization; the certified cost is
separate.  It tests whether the known cheap CH witness obeys s >= -24.
"""
from pathlib import Path
import sys,json
import numpy as np
from scipy.optimize import minimize_scalar
from flint import acb,arb,ctx

ROOT=Path(__file__).resolve().parents[1]
PEER=ROOT.parent.parent/'S1003A01'/'workspace'
sys.path.insert(0,str(PEER/'scripts'))
from perp_rigorous_enclosure import FrozenCell
REC=PEER/'data'/'perp_area'/'x00.03_X64_d16.json'
OUT=ROOT/'data'/'ch_cell_scalar_profile_x003_X64.json'


def main():
    ctx.prec=128
    rec=json.loads(REC.read_text()); c=FrozenCell(rec)
    c.x0=arb(3)/100; c.ell=(c.X/c.x0).log()
    def scal(u):
        R,_=c.ricci(acb(arb(float(u))))
        return float(sum(r.real.mid() for r in R))
    u=np.r_[np.linspace(0,0.02,1001),np.linspace(0.02,0.2,1801)[1:],np.linspace(.2,1,4001)[1:]]
    s=np.array([scal(x) for x in u])
    cand=[]
    for i in range(1,len(u)-1):
        if s[i]<=s[i-1] and s[i]<=s[i+1]:
            q=minimize_scalar(scal,bounds=(u[i-1],u[i+1]),method='bounded',options={'xatol':1e-14})
            cand.append([float(q.x),float(q.fun)])
    i=int(np.argmin(s)); sm=float(s[i]); um=float(u[i])
    if cand:
        um,sm=min([[um,sm]]+cand,key=lambda x:x[1])
    neg=u[s < -24-1e-10]
    R0,_=c.ricci(acb(arb(0))); S0=sum(r.real for r in R0)
    out={'status':'dense floating scalar profile of the certified frozen metric',
         'record':str(REC),'samples':len(u),'minimum_u':um,'minimum_scalar':sm,
         'grid_minimum_u':float(u[i]),'grid_minimum_scalar':float(s[i]),
         'scalar_at_bolt':float(s[0]),'scalar_at_bolt_interval':[float(S0.lower()),float(S0.upper())],
         'scalar_at_collar':float(s[-1]),
         'minimum_s_plus_24':sm+24,'has_s_below_minus24':bool(S0.upper() < -24),
         'grid_u_range_s_below_minus24':[float(neg.min()),float(neg.max())] if len(neg) else None,
         'local_minima':cand}
    OUT.write_text(json.dumps(out,indent=1)+'\n'); print(json.dumps(out,indent=1))
if __name__=='__main__':main()
