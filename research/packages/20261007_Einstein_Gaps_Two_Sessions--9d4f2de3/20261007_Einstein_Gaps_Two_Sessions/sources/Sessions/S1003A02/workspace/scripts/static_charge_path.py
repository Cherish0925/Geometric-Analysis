"""Static (dynamics-free) test of the Lemma-V charge obstruction for non-round opening.

Question.  Lemma V gives, for every diagonal annulus, P_hat >= int max(0, b_+', b_-') dt.
Both charges are explicit algebraic functions of the scale-free first-jet state
   X = (u_f, u_g, u_h, beta, q),
   a_f = e^{2beta/3}, a_g = e^{-beta/3+q/2}, a_h = e^{-beta/3-q/2}   (a_f a_g a_h = 1),
   gamma_i = (a_j^2 + a_k^2 - a_i^2)/(a_j a_k),
   u_i = a_i' - gamma_i,  w_i = a_i' + gamma_i = u_i + 2 gamma_i,
   b_+ = 2 - |u|^2 - u_f u_g u_h,      (depends on u only)
   b_- = |w|^2 - w_f w_g w_h - 2.
If every continuous path from the Hopf-collapsed state to a CH orbit with tau >= 0.70 had
   Lambda(path) = int max(0, d b_+, d b_-) >= p_* = 0.995848,
the non-round input N would follow with no dynamics.  This script minimizes the discretized
Lambda over polygonal paths (slack LP form, IPOPT), with a step bound so that the polygon is
an honest continuous path, and then re-evaluates Lambda on a 40x refined linear interpolation.

Start: TN/ALF collapsed state, h-slot collapsed with ratio lam: a' = (1,1,0)
       => u = (1-lam, 1-lam, -2+lam^2), shape beta = q/2, q = log(1/lam).
End:   CH orbit at radius tau (free in [tau_lo, tau_hi]): u = (3 sinh^2, 0, 0), beta = log cosh, q = 0.
Option K bounds |u_i| <= K (tests whether the static value depends on large first jets).
Usage: python static_charge_path.py K tau_lo tau_hi [N] [tag]
Output: workspace/data/static_charge/path_K{K}_{tag}.json
"""
import json, math, sys
from pathlib import Path
import numpy as np
import casadi as ca

HERE = Path(__file__).resolve().parent
OUTD = HERE.parent/'data'/'static_charge'


def charges_np(X):
    u = np.array(X[:3], float); beta, q = X[3], X[4]
    a = np.array([math.exp(2*beta/3), math.exp(-beta/3+q/2), math.exp(-beta/3-q/2)])
    g = np.array([(a[1]**2+a[2]**2-a[0]**2)/(a[1]*a[2]), (a[2]**2+a[0]**2-a[1]**2)/(a[2]*a[0]),
                  (a[0]**2+a[1]**2-a[2]**2)/(a[0]*a[1])])
    w = u+2*g
    return 2-u@u-np.prod(u), w@w-np.prod(w)-2


def charges_ca(X):
    u = [X[0], X[1], X[2]]; beta, q = X[3], X[4]
    af = ca.exp(2*beta/3); ag = ca.exp(-beta/3+q/2); ah = ca.exp(-beta/3-q/2)
    g = [(ag**2+ah**2-af**2)/(ag*ah), (ah**2+af**2-ag**2)/(ah*af), (af**2+ag**2-ah**2)/(af*ag)]
    w = [u[i]+2*g[i] for i in range(3)]
    bp = 2-(u[0]**2+u[1]**2+u[2]**2)-u[0]*u[1]*u[2]
    bm = w[0]**2+w[1]**2+w[2]**2-w[0]*w[1]*w[2]-2
    return bp, bm


def start_state(lam):
    q = math.log(1/lam)
    return [1-lam, 1-lam, -2+lam**2, q/2, q]


def ch_state(tau):
    return [3*math.sinh(tau)**2, 0.0, 0.0, math.log(math.cosh(tau)), 0.0]


def solve(K, tau_lo, tau_hi, N=160, lam=0.02, hmax=0.25, init='straight', seed=0):
    opti = ca.Opti()
    X = opti.variable(5, N+1)
    tau = opti.variable()
    s = opti.variable(N)
    x0 = start_state(lam)
    opti.subject_to(X[:, 0] == ca.DM(x0))
    sh = ca.sinh(tau); chh = ca.cosh(tau)
    opti.subject_to(X[0, N] == 3*sh**2); opti.subject_to(X[1, N] == 0); opti.subject_to(X[2, N] == 0)
    opti.subject_to(X[3, N] == ca.log(chh)); opti.subject_to(X[4, N] == 0)
    opti.subject_to(opti.bounded(tau_lo, tau, tau_hi))
    opti.subject_to(s >= 0)
    for i in range(3):
        opti.subject_to(opti.bounded(-K, X[i, :], K))
    reg = 0
    bprev = charges_ca(X[:, 0])
    for k in range(N):
        bk1 = charges_ca(X[:, k+1])
        opti.subject_to(s[k] >= bk1[0]-bprev[0])
        opti.subject_to(s[k] >= bk1[1]-bprev[1])
        d = X[:, k+1]-X[:, k]
        opti.subject_to(ca.sumsqr(d) <= hmax**2)
        reg += ca.sumsqr(d)
        bprev = bk1
    opti.minimize(ca.sum1(s)+1e-4*reg)
    # initial guess
    rng = np.random.default_rng(seed)
    t0 = 0.5*(tau_lo+tau_hi)
    x1 = np.array(ch_state(t0)); xa = np.array(x0)
    for k in range(N+1):
        th = k/N
        guess = (1-th)*xa+th*x1
        if init == 'detour':  # go out to larger first jets in the middle
            guess[:3] += 4*math.sin(math.pi*th)*np.array([1.0, 1.0, 1.0])
        if init == 'random':
            guess[:3] += math.sin(math.pi*th)*rng.normal(0, 2, 3)
        opti.set_initial(X[:, k], guess)
    opti.set_initial(tau, t0)
    opti.set_initial(s, 0.1)
    opti.solver('ipopt', {'print_time': False}, {'max_iter': 4000, 'print_level': 0, 'tol': 1e-9})
    try:
        sol = opti.solve(); ok = True; Xs = sol.value(X); ts = float(sol.value(tau))
    except RuntimeError:
        ok = False; Xs = opti.debug.value(X); ts = float(opti.debug.value(tau))
    # refined honest evaluation on linear interpolation
    fine = []
    for k in range(N):
        for j in range(40):
            fine.append(Xs[:, k]+(j/40)*(Xs[:, k+1]-Xs[:, k]))
    fine.append(Xs[:, N])
    B = np.array([charges_np(x) for x in fine])
    dB = np.diff(B, axis=0)
    lam_fine = float(np.sum(np.maximum(0, np.maximum(dB[:, 0], dB[:, 1]))))
    rise_p = float(np.max(B[:, 0]-np.minimum.accumulate(B[:, 0])))
    rise_m = float(np.max(B[:, 1]-np.minimum.accumulate(B[:, 1])))
    nodes = np.array([charges_np(Xs[:, k]) for k in range(N+1)])
    return {'K': K, 'tau_range': [tau_lo, tau_hi], 'N': N, 'lam': lam, 'hmax': hmax, 'init': init,
            'solver_success': ok, 'tau_end': ts, 'Lambda_nodes': float(np.sum(np.maximum(0, np.maximum(np.diff(nodes[:, 0]), np.diff(nodes[:, 1]))))),
            'Lambda_refined': lam_fine, 'max_rise_bplus': rise_p, 'max_rise_bminus': rise_m,
            'b_start': list(map(float, B[0])), 'b_end': list(map(float, B[-1])),
            'max_abs_u': float(np.max(np.abs(Xs[:3]))), 'X': Xs.T.tolist(), 'charges_nodes': nodes.tolist()}


if __name__ == '__main__':
    K = float(sys.argv[1]); lo = float(sys.argv[2]); hi = float(sys.argv[3])
    N = int(sys.argv[4]) if len(sys.argv) > 4 else 160
    init = sys.argv[5] if len(sys.argv) > 5 else 'straight'
    OUTD.mkdir(parents=True, exist_ok=True)
    r = solve(K, lo, hi, N=N, init=init)
    tag = f"K{K:g}_t{lo:g}-{hi:g}_{init}"
    (OUTD/f'path_{tag}.json').write_text(json.dumps(r)+'\n')
    print(json.dumps({k: v for k, v in r.items() if k not in ('X', 'charges_nodes')}))
