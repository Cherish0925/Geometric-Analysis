"""Evaluate the exact beta-pinning observable on node data.

This is a route-reading helper only.  It reports B~ and the weighted-E payment
that appears in the exact identity; it does not replace interval integration of
F_beta and is not used as theorem evidence.
"""
import json,math,sys
from pathlib import Path
import numpy as np

def run(path):
 r=json.loads(Path(path).read_text()); X=np.asarray(r['X'],float); U=np.asarray(r['U'],float)
 x,z,p,chi,eta=X.T; q=-3*np.log(z); beta=x+q/2; xi=chi+eta/2
 af=np.exp(2*beta/3); ag=np.exp(-beta/3+q/2); ah=np.exp(-beta/3-q/2)
 yf=p+2*xi/3; yg=p-xi/3+eta/2; yh=p-xi/3-eta/2
 k=af/(ag*ah); zeta=1/(ag*ah); v=yf-(yg+yh)/2
 B=np.log(k/np.sqrt(1+zeta))+(v-1/k)/4
 # In the scale-free controls, Ebar=r^2 E and d tau=dt/r; the exact action
 # component is int Ebar^2/6 d tau.  Trapezoid values only indicate where it sits.
 tau=np.linspace(0,float(r['T']),len(X)); e_action=float(np.trapezoid(U[:,1]**2/6,x=tau))
 return {'path':str(path),'B0':float(B[0]),'B1':float(B[-1]),'DeltaB':float(B[-1]-B[0]),
         'max_abs_B':float(np.max(np.abs(B))),'Ebar_action_trap':e_action,'total_cost':r['cost']}
if __name__=='__main__': print(json.dumps([run(p) for p in sys.argv[1:]],indent=1))
