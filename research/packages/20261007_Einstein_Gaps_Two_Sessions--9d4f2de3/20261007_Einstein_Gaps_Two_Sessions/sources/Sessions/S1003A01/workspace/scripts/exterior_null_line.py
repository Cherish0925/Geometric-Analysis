"""Exact CH exterior response of the antisymmetric (v_-, theta) sector and comparison with LM cells.

Raw quadratic P/(8pi^2) of the minus channel on CH (Step 7, re-derived Step 19):
    E = int mu (w')^2 dx,   w = v_-/f,  f=f_-=x/(1+x)^{5/2},  mu = x(1+x) f^2/4 = x^3/(4(1+x)^4),
torsion-free constraint  d/dx[k theta] = (1/2) f^2 w,  k=(x/(1+x))^2.
Exact-collar end at X:  w(X)=0, theta(X)=0.  Entrance data at rho: w(rho)=w0, theta(rho)=Th.
=> minimise int_rho^X mu w'^2  s.t. w(rho)=w0, w(X)=0, int_rho^X f^2 w = -2 k(rho) Th =: m.
X=infinity: w(X) free (v_- -> 0 anyway), cost = delta^2/I(rho),
   G(x)=int_x^inf f^2 = (6x^2+4x+1)/(12(1+x)^4),  I(rho)=int_rho^inf G^2/mu,
   delta = m - w0 G(rho)  (null line delta=0: the decaying Einstein mass mode),
   optimal profile  mu w' = -lam G,  w = w0 - lam[2 log(x/rho) - 4/3(1/x-1/rho) - 1/6(1/x^2-1/rho^2)],
   lam = -delta/I.
Usage: python exterior_null_line.py  (reads data/tail_modes/lm_tails.json, LM records)
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.integrate import quad

f2 = lambda x: x*x/(1+x)**5
mu = lambda x: x**3/(4*(1+x)**4)
k = lambda x: (x/(1+x))**2
Gf = lambda x: (6*x*x+4*x+1)/(12*(1+x)**4)
theta1 = lambda x: -(6*x*x+4*x+1)/(24*x*x*(1+x)**2)
def Lshape(x, rho):
    return 2*math.log(x/rho) - 4/3*(1/x-1/rho) - 1/6*(1/x**2-1/rho**2)

def I_inf(rho):
    return quad(lambda s: Gf(s)**2/mu(s), rho, np.inf, limit=400)[0]

def finite_cost(rho, X, w0, m):
    """min int_rho^X mu psi'^2 with w=w0+psi, psi(rho)=0, psi(X)=-w0, int f^2 psi = m - w0*int_rho^X f^2."""
    GX = lambda x: quad(f2, x, X)[0]
    R = quad(lambda s: 1/mu(s), rho, X, limit=400)[0]
    M = quad(lambda s: GX(s)/mu(s), rho, X, limit=400)[0]
    N = quad(lambda s: GX(s)**2/mu(s), rho, X, limit=400)[0]
    target = m - w0*quad(f2, rho, X)[0]
    # psi' = (nu - lam GX)/mu ; psi(X) = nu R - lam M = -w0 ; int f^2 psi = nu M - lam N = target
    A = np.array([[R, -M], [M, -N]]); nu, lam = np.linalg.solve(A, [-w0, target])
    return nu*(-w0) - lam*target, nu, lam

def main():
    import sys
    root = Path(__file__).resolve().parents[1]
    src = sys.argv[1] if len(sys.argv) > 1 else str(root/'data/tail_modes/lm_tails.json')
    dst = sys.argv[2] if len(sys.argv) > 2 else str(root/'data/tail_modes/exterior_null_line.json')
    tails = json.loads(Path(src).read_text())
    out = []
    for t in tails:
        X = t['X']; rows = [r for r in t['rows'] if 4 <= r['x'] <= X/8]
        xs = np.array([r['x'] for r in rows]); cv = np.array([r['c_v'] for r in rows])
        th = np.array([r['theta'] for r in rows])
        rho = 10.0
        # fit c_v = A - lam*Lshape(x, rho)
        B = np.c_[np.ones_like(xs), -np.array([Lshape(x, rho) for x in xs])]
        (Afit, lamfit), *_ = np.linalg.lstsq(B, cv, rcond=None)
        resid = float(np.max(np.abs(B @ [Afit, lamfit] - cv)))
        # entrance trace at rho from data
        w0 = float(np.interp(math.log(rho), np.log(xs), cv)); Th = float(np.interp(math.log(rho), np.log(xs), th))
        m = -2*k(rho)*Th
        Iinf = I_inf(rho); delta = m - w0*Gf(rho); lam_pred = -delta/Iinf
        Einf = delta**2/Iinf
        EX, nuX, lamX = finite_cost(rho, X, w0, m)
        rec = dict(record=t['record'], X=X, J=t['J'], rho=rho, fit_A=float(Afit), fit_lambda=float(lamfit),
                   fit_maxresid=resid, w0=w0, Theta=Th, m=m, null_m=w0*Gf(rho), delta=delta, I_inf=Iinf,
                   lambda_from_trace=lam_pred, E_ext_inf=Einf, E_ext_X=EX, trunc_excess=EX-Einf)
        out.append(rec); print(json.dumps(rec))
    # predicted truncation law for the X=512 trace
    t = out[-1]
    law = []
    for X in [64, 128, 256, 512, 1024, 2048, 4096]:
        EX, _, _ = finite_cost(t['rho'], X, t['w0'], t['m'])
        law.append(dict(X=X, E_ext_X=EX, excess=EX-t['E_ext_inf']))
    print(json.dumps(dict(truncation_law_from_X512_trace=law)))
    Path(dst).write_text(json.dumps(dict(cells=out, law=law), indent=1)+'\n')

if __name__ == '__main__': main()
