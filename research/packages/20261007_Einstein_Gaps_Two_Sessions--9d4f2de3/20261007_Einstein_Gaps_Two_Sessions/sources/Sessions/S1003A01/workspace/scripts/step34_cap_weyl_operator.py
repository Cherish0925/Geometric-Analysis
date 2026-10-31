"""Step 34: chiral Weyl operators of the exact cusp-closing Calabi KE cap.

Metric and orientation:
  g = tau (dx^2+dy^2) + d tau^2/Theta + Theta (d psi + x dy)^2,
  Theta = 2 tau^2/3 - c/tau,
  vol orientation e0^e1^e2^e3, with
  e0=d tau/sqrt(Theta), e1=sqrt(tau) dx,
  e2=sqrt(tau) dy, e3=sqrt(Theta)(d psi+x dy).
Then omega=e0^e3+e1^e2 is self-dual.  The script computes the
3x3 matrices of W^+ and W^- on the normalized self-dual/anti-self-dual
bases, checks their norms, and evaluates the smooth-cap endpoint tau0.

Usage: python step34_cap_weyl_operator.py [--out PATH]
"""
import argparse
import json
from pathlib import Path
import sympy as sp

# Coordinates and metric
tau, x, y, psi, c = sp.symbols('tau x y psi c', positive=True)
Th = sp.Rational(2, 3)*tau**2 - c/tau
X = [tau, x, y, psi]
g = sp.zeros(4)
g[0, 0] = 1/Th
g[1, 1] = tau
g[2, 2] = tau + Th*x**2
g[2, 3] = g[3, 2] = Th*x
g[3, 3] = Th
gi = sp.simplify(g.inv())
n = 4

Gam = [[[sp.simplify(sum(
    gi[a, d]*(sp.diff(g[d, b], X[cc]) + sp.diff(g[d, cc], X[b]) - sp.diff(g[b, cc], X[d]))
    for d in range(n))/2)
    for cc in range(n)] for b in range(n)] for a in range(n)]

def rup(a, b, cc, d):
    val = sp.diff(Gam[a][b][d], X[cc]) - sp.diff(Gam[a][b][cc], X[d])
    val += sum(Gam[a][cc][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][cc]
               for k in range(n))
    return val

R = sp.MutableDenseNDimArray.zeros(n, n, n, n)
for a in range(n):
    for b in range(n):
        for cc in range(n):
            for d in range(cc+1, n):
                val = sp.simplify(sum(g[a, k]*rup(k, b, cc, d) for k in range(n)))
                R[a, b, cc, d] = val
                R[a, b, d, cc] = -val
Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(
    gi[a, cc]*R[a, b, cc, d] for a in range(n) for cc in range(n))))
s = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
P = (Ric - s*g/6)/2
W = sp.MutableDenseNDimArray.zeros(n, n, n, n)
for a in range(n):
    for b in range(n):
        for cc in range(n):
            for d in range(n):
                W[a, b, cc, d] = sp.simplify(
                    R[a, b, cc, d]
                    - (P[a, cc]*g[b, d] + P[b, d]*g[a, cc]
                       - P[a, d]*g[b, cc] - P[b, cc]*g[a, d]))

# Dual orthonormal vectors E_A = E[A,a] partial_a.  Curvature is homogeneous,
# so after differentiating we evaluate in the gauge x=0.
E = sp.zeros(4)
E[0, 0] = sp.sqrt(Th)
E[1, 1] = 1/sp.sqrt(tau)
E[2, 2] = 1/sp.sqrt(tau)
E[2, 3] = -x/sp.sqrt(tau)
E[3, 3] = 1/sp.sqrt(Th)

def Worth(A, B, C, D):
    val = 0
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for d in range(n):
                    if E[A, a] and E[B, b] and E[C, cc] and E[D, d] and W[a,b,cc,d]:
                        val += E[A,a]*E[B,b]*E[C,cc]*E[D,d]*W[a,b,cc,d]
    return sp.simplify(sp.sympify(val).subs(x, 0))

# A two-form is stored by antisymmetric orthonormal components alpha[A,B].
def form(terms):
    A = sp.zeros(4)
    for i, j, coeff in terms:
        A[i, j] += coeff
        A[j, i] -= coeff
    return A

rt2 = sp.sqrt(2)
plus = [
    form([(0,3,1/rt2),(1,2,1/rt2)]),     # omega/sqrt(2)
    form([(0,1,1/rt2),(2,3,1/rt2)]),
    form([(0,2,1/rt2),(1,3,-1/rt2)]),
]
minus = [
    form([(0,3,1/rt2),(1,2,-1/rt2)]),
    form([(0,1,1/rt2),(2,3,-1/rt2)]),
    form([(0,2,1/rt2),(1,3,1/rt2)]),
]

cache = {}
def wc(A,B,C,D):
    key=(A,B,C,D)
    if key not in cache:
        cache[key]=Worth(A,B,C,D)
    return cache[key]

def op_entry(alpha, beta):
    # <alpha,W beta> = (1/4) alpha_AB W_ABCD beta_CD.
    val = 0
    for A in range(4):
        for B in range(4):
            if alpha[A,B] == 0:
                continue
            for C in range(4):
                for D in range(4):
                    if beta[C,D] != 0:
                        val += alpha[A,B]*wc(A,B,C,D)*beta[C,D]/4
    return sp.factor(sp.simplify(val))

Wp = sp.Matrix(3,3,lambda i,j: op_entry(plus[i],plus[j]))
Wm = sp.Matrix(3,3,lambda i,j: op_entry(minus[i],minus[j]))
tau0 = (sp.Rational(3,2)*c)**sp.Rational(1,3)
Wm0 = sp.simplify(Wm.subs(tau,tau0))
out = {
    'scalar': str(s),
    'einstein_residual_zero': bool(sp.simplify(Ric+g) == sp.zeros(4)),
    'orientation': 'e0^e1^e2^e3; omega=e0^e3+e1^e2 is self-dual',
    'plus_basis': ['(e03+e12)/sqrt2','(e01+e23)/sqrt2','(e02-e13)/sqrt2'],
    'minus_basis': ['(e03-e12)/sqrt2','(e01-e23)/sqrt2','(e02+e13)/sqrt2'],
    'Wplus': [[str(sp.factor(Wp[i,j])) for j in range(3)] for i in range(3)],
    'Wminus': [[str(sp.factor(Wm[i,j])) for j in range(3)] for i in range(3)],
    'Wplus_trace': str(sp.factor(sp.trace(Wp))),
    'Wminus_trace': str(sp.factor(sp.trace(Wm))),
    'Wplus_norm_sq': str(sp.factor(sp.trace(Wp*Wp))),
    'Wminus_norm_sq': str(sp.factor(sp.trace(Wm*Wm))),
    'tau0': str(tau0),
    'Wminus_at_tau0': [[str(sp.factor(Wm0[i,j])) for j in range(3)] for i in range(3)],
}
text=json.dumps(out,indent=1)
print(text)
ap=argparse.ArgumentParser(); ap.add_argument('--out'); args=ap.parse_args()
if args.out:
    Path(args.out).write_text(text+'\n')
