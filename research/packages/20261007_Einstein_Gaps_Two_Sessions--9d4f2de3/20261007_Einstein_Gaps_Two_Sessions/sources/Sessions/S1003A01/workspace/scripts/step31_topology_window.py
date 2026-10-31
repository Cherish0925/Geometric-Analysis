"""Step 31: exact topology and balanced-window algebra for ramified compactifications.

Let A=K^2 of the smooth compact KE surface and Delta=3 chi-A.  The surface
signature is tau=(A-2 chi)/3=A/9-2 Delta/9.  After k blowups and l
S1xS3 sums:
  T+=A-(k+4l),
  T-=A/3+4 Delta/3+5k-4l.
This script checks these identities and the balance that makes
3*T-/A=1+Q/A: 16l-14k=4Delta. It also evaluates an explicit integer choice
near k=2Q/9-2Delta/9, l=7Q/36+Delta/18 and records the resulting errors.
"""
import argparse, json
from pathlib import Path
import sympy as sp

A,D,k,l,Q=sp.symbols('A D k l Q', real=True)
chi=(A+D)/3
tau=(A-2*chi)/3
chiM=chi+k-2*l
tauM=tau-k
Tp=sp.simplify(2*chiM+3*tauM)
Tm=sp.simplify(2*chiM-3*tauM)
sol=sp.solve([sp.Eq(k+4*l,Q),sp.Eq(16*l-14*k,4*D)],[k,l], dict=True)[0]
h,FF=sp.symbols('h FF', real=True)
full_window=sp.solve([sp.Eq(k+4*l,A*h),sp.Eq(1+4*D/A+15*k/A-12*l/A,FF)],[k,l], dict=True)[0]
assert sp.simplify(Tp-(A-k-4*l))==0
assert sp.simplify(Tm-(A/sp.Integer(3)+4*D/sp.Integer(3)+5*k-4*l))==0
assert sp.simplify(Tm-(A+k+4*l)/3-(4*D+14*k-16*l)/3)==0

ap=argparse.ArgumentParser(); ap.add_argument('--A',type=int,default=10**9); ap.add_argument('--Delta',type=int,default=10**4); ap.add_argument('--Q',type=int,default=10**6); ap.add_argument('--out'); args=ap.parse_args()
# Search a bounded neighborhood of the real balanced solution while preserving nonnegativity.
kstar=float(sol[k].subs({Q:args.Q,D:args.Delta})); lstar=float(sol[l].subs({Q:args.Q,D:args.Delta}))
best=None
for ki in range(max(0,int(round(kstar))-10),int(round(kstar))+11):
  for li in range(max(0,int(round(lstar))-10),int(round(lstar))+11):
    Qi=ki+4*li
    h=Qi/args.A
    tp=args.A-Qi
    tm=args.A/3+4*args.Delta/3+5*ki-4*li
    U=3*min(tp,tm)/args.A
    rec=dict(k=ki,l=li,Q=Qi,h=h,Tplus=tp,Tminus=tm,U_top=U,
             U_minus_1_minus_h=U-1-h,balance_residual=16*li-14*ki-4*args.Delta,
             k_over_Q=ki/Qi,l_over_Q=li/Qi)
    key=(abs(rec['balance_residual']),abs(Qi-args.Q))
    if best is None or key<best[0]: best=(key,rec)
out={'symbolic':{'chi':str(chi),'tau':str(sp.simplify(tau)),'Tplus':str(Tp),'Tminus':str(Tm),'exact_equal_chirality_solution':{str(x):str(y) for x,y in sol.items()},'full_window_solution':{str(x):str(sp.factor(y)) for x,y in full_window.items()}},
     'example_parameters':{**vars(args),'out':None},'integer_choice':best[1],
     'interpretation':'If Delta=o(Q), Q=o(A), and rounding is O(1), then k/Q->2/9, l/Q->7/36 and U_top=1+h+o(h).'}
text=json.dumps(out,indent=1); print(text)
if args.out: Path(args.out).write_text(text+'\n')
