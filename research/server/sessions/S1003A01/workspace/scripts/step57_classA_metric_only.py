"""Step 57: metric-only formulation of invariant almost-Kahler Einstein structures
on diagonal Bianchi class-A cohomogeneity-one metrics.

Metric  g = dt^2 + sum a_i^2 s_i^2,  d s_i = 2 n_i s_j^s_k (cyclic).
Variables (homogeneous of weight 1):
    h_i = a_i'/a_i ,   W_i = n_i a_i/(a_j a_k).
All class-A types are the sign patterns of (W_1,W_2,W_3) (IX: +++, VIII: ++-,
VII0: ++0, VI0: +-0, II: +00, I: 000).  With eps=+1 (eps=-1 is W -> -W):
    Einstein:   h_i' = -h_i S + 2(W_i^2-(W_j-W_k)^2) - lam,   W_i' = W_i(h_i-h_j-h_k),
    constraint: Q + lam = 0,  Q = sum_{i<j} h_i h_j + sum W_i^2 - 2 sum_{i<j} W_i W_j,
    closure of Omega = sum x_i w_i:  x_i' = mu_i x_i,  mu_i = 2W_i - h_j - h_k.
Unit length sum X_i = 1 (X_i=x_i^2) propagates iff X.f^(n) = 0 for all n, where
    f^(0) = mu,   f^(n+1)_i = D f^(n)_i + 2 mu_i f^(n)_i.
q = |nabla Omega|^2 = 2[sum X_i mu_i^2 + (X1+X2) b3^2 + (X1+X3) b2^2 + (X2+X3) b1^2],
    b1 = h1+W1-W2-W3, b2 = h2-W1+W2-W3, b3 = h3-W1-W2+W3.

This script (i) checks the reformulation against step56_ake_propagate (exact),
(ii) builds the X-free invariance tower
    two-direction (X3=0):  Phi_n = mu1 f2^(n) - mu2 f1^(n),  X1=-mu2/(mu1-mu2),
    three-direction:       Psi_n = det(f^(0), f^(1), f^(n)), n>=2,
with lam eliminated by lam=-Q, and (iii) writes Singular inputs.
Usage: python step57_classA_metric_only.py [check] ; outputs ../data/step57/.
"""
import sympy as sp, os, sys, json

h = sp.symbols('h1 h2 h3'); W = sp.symbols('W1 W2 W3'); lam = sp.symbols('lam')
S = sum(h)
Q = h[0]*h[1] + h[0]*h[2] + h[1]*h[2] + sum(w**2 for w in W) - 2*(W[0]*W[1] + W[0]*W[2] + W[1]*W[2])
def jk(i): return (i+1) % 3, (i+2) % 3
V = {}
for i in range(3):
    j, k = jk(i)
    V[h[i]] = -h[i]*S + 2*(W[i]**2 - (W[j]-W[k])**2) - lam
    V[W[i]] = W[i]*(h[i] - h[j] - h[k])
mu = [2*W[i] - h[jk(i)[0]] - h[jk(i)[1]] for i in range(3)]
def D(e, L=lam):
    return sp.expand(sum(sp.diff(e, v)*V[v].subs(lam, L) for v in V))
b1 = h[0] + W[0] - W[1] - W[2]; b2 = h[1] - W[0] + W[1] - W[2]; b3 = h[2] - W[0] - W[1] + W[2]
X = sp.symbols('X1 X2 X3')
qexpr = 2*(sum(X[i]*mu[i]**2 for i in range(3)) + (X[0]+X[1])*b3**2 + (X[0]+X[2])*b2**2 + (X[1]+X[2])*b1**2)

def tower(nmax, L):
    f = [mu]
    for n in range(nmax):
        prev = f[-1]
        f.append([sp.expand(D(prev[i], L) + 2*mu[i]*prev[i]) for i in range(3)])
    return f

def check():
    # (a) constraint propagation: D(Q+lam) proportional to Q+lam
    dH = sp.expand(D(Q))
    quo, rem = sp.div(sp.Poly(dH, *h, *W, lam), sp.Poly(Q + lam, *h, *W, lam))
    print('D(Q+lam) = (', quo.as_expr(), ')*(Q+lam) + ', rem.as_expr())
    # (b) compare with the step56 (a,b,c,A,B,C) formulation at random rational points (Bianchi IX)
    sys.path.insert(0, os.path.dirname(__file__))
    os.environ['EPS'] = '1'
    import step56_ake_propagate as P
    import random
    random.seed(3)
    for trial in range(3):
        vals = {P.sa: sp.Rational(random.randint(2, 9), 3), P.sb: sp.Rational(random.randint(2, 9), 4),
                P.sc: sp.Rational(random.randint(2, 9), 5), P.A_: sp.Rational(random.randint(-9, 9), 7),
                P.B_: sp.Rational(random.randint(-9, 9), 7), P.C_: sp.Rational(random.randint(-9, 9), 7),
                P.lam: sp.Rational(-3), P.X[0]: sp.Rational(1, 3), P.X[1]: sp.Rational(1, 2), P.X[2]: sp.Rational(1, 6)}
        a_, b_, c_ = vals[P.sa], vals[P.sb], vals[P.sc]
        hv = [vals[P.A_]/a_, vals[P.B_]/b_, vals[P.C_]/c_]
        Wv = [a_/(b_*c_), b_/(a_*c_), c_/(a_*b_)]
        sub = dict(zip(h, hv)); sub.update(dict(zip(W, Wv))); sub[lam] = -3
        sub.update({X[0]: sp.Rational(1, 3), X[1]: sp.Rational(1, 2), X[2]: sp.Rational(1, 6)})
        e1 = [sp.simplify(P.MU[i].subs(vals) - mu[i].subs(sub)) for i in range(3)]
        Hold = sp.simplify(P.H.subs(vals) - (Q + lam).subs(sub))
        qold = sp.simplify(P.q.subs(vals) - qexpr.subs(sub))
        # derivative of h1 = A/a : (A'/a - A^2/a^2)
        hd = sp.simplify((P.DER[P.A_]/P.sa - P.A_**2/P.sa**2).subs(vals) - V[h[0]].subs(sub))
        print('check', trial, e1, Hold, qold, hd)

def write_two(N, char=0, out='../data/step57'):
    f = tower(N, -Q)
    Phi = [sp.expand(mu[0]*f[n][1] - mu[1]*f[n][0]) for n in range(1, N+1)]
    names = ['h1', 'h2', 'h3', 'W1', 'W2', 'W3']
    S_ = lambda z: str(sp.expand(z)).replace('**', '^')
    d = os.path.join(os.path.dirname(__file__), out); os.makedirs(d, exist_ok=True)
    json.dump({'Phi': [str(p) for p in Phi], 'mu': [str(m) for m in mu], 'Q': str(Q)},
              open(os.path.join(d, f'two_tower_N{N}.json'), 'w'), indent=1)
    for p in Phi: print('deg', sp.Poly(p, *h, *W).total_degree(), 'terms', len(sp.Add.make_args(p)))
    return Phi

def write_three(N, out='../data/step57'):
    f = tower(N, -Q)
    Psi = []
    for n in range(2, N+1):
        M = sp.Matrix([f[0], f[1], f[n]])
        Psi.append(sp.expand(M.det(method='berkowitz')))
        print('Psi', n, 'deg', sp.Poly(Psi[-1], *h, *W).total_degree(), 'terms', len(sp.Add.make_args(Psi[-1])), flush=True)
    d = os.path.join(os.path.dirname(__file__), out); os.makedirs(d, exist_ok=True)
    json.dump({'Psi': [str(p) for p in Psi], 'f0': [str(z) for z in f[0]], 'f1': [str(z) for z in f[1]]},
              open(os.path.join(d, f'three_tower_N{N}.json'), 'w'), indent=1)
    return Psi

if __name__ == '__main__':
    if 'check' in sys.argv: check()
    if 'two' in sys.argv: write_two(int(os.environ.get('N', '6')))
    if 'three' in sys.argv: write_three(int(os.environ.get('N', '6')))
