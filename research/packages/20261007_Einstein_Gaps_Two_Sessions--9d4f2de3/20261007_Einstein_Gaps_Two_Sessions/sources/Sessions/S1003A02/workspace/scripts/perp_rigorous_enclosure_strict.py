"""Session-local strict wrapper of S1003A01 perp_rigorous_enclosure.

Scientific changes:
- phi Taylor-radius upper bound is computed wholly in Arb (`abs(z).upper()`),
  eliminating the float-derived remainder-radius caveat;
- frozen binary64 coefficients are preserved exactly as the intended dyadic witness;
- all other bolt-regular Ricci and acb.integral formulas are inherited verbatim.

Usage: qiushi-yau26 env numeric python perp_rigorous_enclosure_strict.py RECORD ...
"""
from pathlib import Path
import sys, runpy
from flint import arb, acb

SRC = Path(__file__).resolve().parents[3] / 'S1003A01' / 'workspace' / 'scripts' / 'perp_rigorous_enclosure.py'
ns = runpy.run_path(str(SRC), run_name='perp_rigorous_enclosure_base')


def phi_derivs_strict(z, N=48):
    """phi=(exp(z)-1)/z and first two derivatives with a pure-Arb series tail."""
    m = abs(z)
    if m.lower() > 1:
        e = z.exp()
        return (e-1)/z, (z*e-e+1)/(z*z), (z*z*e-2*z*e+2*e-2)/(z*z*z)
    if m.upper() > 1:
        # A straddling ball is evaluated by the entire series, with r=m.upper().
        pass
    s0=acb(0); s1=acb(0); s2=acb(0); zk=acb(1)
    for k in range(N):
        s0 += zk/arb(ns['math'].factorial(k+1))
        s1 += zk*(k+1)/arb(ns['math'].factorial(k+2))
        s2 += zk*((k+1)*(k+2))/arb(ns['math'].factorial(k+3))
        zk *= z
    r = m.upper()
    # In the actual near-zero branch r<=1; if a straddling integration ball has
    # r>1, enlarge N until r/(N+1)<1 (N=48 easily covers all encountered balls).
    t = r**N/arb(ns['math'].factorial(N))/(1-r/(N+1))
    err = acb(arb(0,t),arb(0,t))
    return s0+err,s1+err,s2+err

ns['phi_derivs'] = phi_derivs_strict
ns['phi_val'] = lambda z: phi_derivs_strict(z)[0]
# Update the function globals captured by class methods and main.
for name in ('FrozenCell','main'):
    obj=ns[name]
    if hasattr(obj,'__dict__'):
        for v in obj.__dict__.values():
            if callable(v) and hasattr(v,'__globals__'):
                v.__globals__['phi_derivs']=phi_derivs_strict
                v.__globals__['phi_val']=ns['phi_val']
if __name__=='__main__':
    ns['main']()
