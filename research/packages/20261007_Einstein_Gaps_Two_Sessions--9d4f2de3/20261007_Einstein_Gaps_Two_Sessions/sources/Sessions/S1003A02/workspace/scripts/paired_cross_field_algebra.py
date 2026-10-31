"""Step 37: exact algebra behind the paired cross-field form of the simultaneous identity.

Checks (symbolic where possible, otherwise random high-precision numerics):
 (1) Bloch/Fierz: for phi,psi in C^2 with unit Bloch vectors n,n'
       |<psi,phi>|^2 = |phi|^2|psi|^2 (1+n.n')/2,
       |phi ^ psi|^2 = |phi|^2|psi|^2 (1-n.n')/2,   so |u|^2+|w|^2 = rho rho'.
 (2) With f^+ = (rho/sqrt2) n (normalization |f^+|^2 = rho^2/2 of the paper):
       |f^+ - f'^+|^2 = (rho-rho')^2/2 + 2|w|^2 = ((rho+rho')^2 - 4|u|^2)/2.
 (3) Walsh: for any family F_eps (eps in {+-1}^k),
       sum_{I nonempty} |F_I|^2 = (1/2) E_{eps,eps'} |F_eps - F_eps'|^2,
     hence 2 sum_{I!=0}||f_I^+||^2 = E_{eps,eps'} int[(rho-rho')^2/2 + 2|w|^2].
 (4) Kinetic split: |nabla Phi|^2 = |zeta|^2/rho + rho |nabla n|^2/4 for a U(1)-twisted
     spinor curve (n = Bloch vector, connection drops out of n).
 (5) Weitzenboeck consistency in the paper's normalization (s=-4, rho<=2):
       Sigma = 16K + 4 int(rho-2)^2 + 8J,  Sigma = 16V - 32 pi^2 p,  int rho^2 = 8pi^2 p + 2J
     imply K = (1/2) int rho(2-rho); and the residual density
       m(rho) = 2 rho(2-rho) - b(rho)(2-rho)^2 = (2-rho)(-rho^3+10rho^2-2rho-4)/6.
Output: workspace/data/paired_cross_field_algebra.json
"""
import json, itertools
from pathlib import Path
import numpy as np
import sympy as sp

out = {}
# (1),(2) symbolic
a1, a2, b1, b2 = sp.symbols('a1 a2 b1 b2', complex=True)
phi = sp.Matrix([a1, a2]); psi = sp.Matrix([b1, b2])
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def bloch_unnorm(v):
    return [sp.expand((v.H * s * v)[0]) for s in sig]
nphi = bloch_unnorm(phi); npsi = bloch_unnorm(psi)
rho = sp.expand((phi.H * phi)[0]); rhop = sp.expand((psi.H * psi)[0])
u = (psi.H * phi)[0]; w = a1 * b2 - a2 * b1
absu2 = sp.expand(u * sp.conjugate(u)); absw2 = sp.expand(w * sp.conjugate(w))
dot = sp.expand(sum(x * y for x, y in zip(nphi, npsi)))  # = rho rho' n.n'
r1 = sp.simplify(sp.expand(absu2 - (rho * rhop + dot) / 2))
r2 = sp.simplify(sp.expand(absw2 - (rho * rhop - dot) / 2))
r3 = sp.simplify(sp.expand(absu2 + absw2 - rho * rhop))
# |f^+ - f'^+|^2 with f^+ = (rho/sqrt2) n, |n|=1  -> (rho^2+rho'^2-2 rho rho' n.n')/2
fdiff2 = (rho**2 + rhop**2 - 2 * dot) / 2
r4 = sp.simplify(sp.expand(fdiff2 - ((rho - rhop)**2 / 2 + 2 * absw2)))
r5 = sp.simplify(sp.expand(fdiff2 - ((rho + rhop)**2 - 4 * absu2) / 2))
# |n|^2 = rho^2 check for the unnormalized Bloch vector
r6 = sp.simplify(sp.expand(sum(x * x for x in nphi) - rho**2))
out['bloch_fierz_residuals'] = [str(r) for r in (r1, r2, r3, r4, r5, r6)]

# (3) Walsh variance identity, numerically for k=1..4 with random vectors in R^3
rng = np.random.default_rng(37)
walsh = {}
for k in range(1, 5):
    signs = list(itertools.product([-1, 1], repeat=k))
    F = {e: rng.normal(size=3) for e in signs}
    tot = 0.0
    for r in range(1, k + 1):
        for I in itertools.combinations(range(k), r):
            fI = np.mean([np.prod([e[i] for i in I]) * F[e] for e in signs], axis=0)
            tot += fI @ fI
    pair = 0.5 * np.mean([np.sum((F[e] - F[f])**2) for e in signs for f in signs])
    walsh[k] = [tot, pair, abs(tot - pair)]
out['walsh_variance_check'] = walsh

# (4) kinetic split along a random curve: Phi(t) in C^2, connection i a(t) dt
t = sp.symbols('t', real=True)
ph = sp.Matrix([sp.exp(sp.I * sp.sin(t)) * (1 + t / 3) + sp.I * t**2 / 5, sp.cos(2 * t) - sp.I * t / 2])
a = sp.Rational(1, 3) + sp.sin(t) / 2
Dph = ph.diff(t) + sp.I * a * ph
def num(expr, tv):
    return complex(sp.N(expr.subs(t, tv), 30))
checks = []
for tv in [0.1, 0.7, 1.3, 2.2]:
    P = np.array([num(ph[0], tv), num(ph[1], tv)])
    D = np.array([num(Dph[0], tv), num(Dph[1], tv)])
    rho_v = np.vdot(P, P).real
    zeta = np.vdot(P, D)
    kin = np.vdot(D, D).real
    # Bloch vector derivative by finite differences of the normalized Bloch vector
    def nvec(tt):
        Q = np.array([num(ph[0], tt), num(ph[1], tt)])
        S = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
        return np.array([np.vdot(Q, s @ Q).real for s in S]) / np.vdot(Q, Q).real
    h = 1e-6
    dn = (nvec(tv + h) - nvec(tv - h)) / (2 * h)
    rhs = abs(zeta)**2 / rho_v + rho_v * (dn @ dn) / 4
    checks.append([tv, kin, rhs, abs(kin - rhs)])
out['kinetic_split_check'] = checks

# (5) Weitzenboeck consistency and residual polynomial
r_, V, J, p, K = sp.symbols('rho V J p K', real=True)
pi = sp.pi
# treat integrals of polynomials in rho formally: I1=int rho, I2=int rho^2
I1, I2 = sp.symbols('I1 I2', real=True)
Ksol = sp.solve(sp.Eq(16 * V - 32 * pi**2 * p, 16 * K + 4 * (I2 - 4 * I1 + 4 * V) + 8 * J), K)[0]
Ksol = sp.simplify(Ksol.subs(p, (I2 - 2 * J) / (8 * pi**2)))
out['K_from_slack'] = str(sp.simplify(Ksol))  # expect I1 - I2/2
b = (-r_**2 + 8 * r_ + 2) / 6
m = sp.factor(sp.expand(2 * r_ * (2 - r_) - b * (2 - r_)**2))
out['m_rho_factored'] = str(m)
out['m_at'] = {str(v): float(m.subs(r_, v)) for v in [0, sp.Rational(1, 2), 1, sp.Rational(3, 2), 2]}
out['m_prime_at_2'] = str(sp.diff(m, r_).subs(r_, 2))
# kinetic-cost combination per unit |zeta|^2: 8 - 4/rho
out['zeta_weight'] = '8 - 4/rho  (nonnegative iff rho >= 1/2)'
path = Path(__file__).resolve().parents[1] / 'data' / 'paired_cross_field_algebra.json'
path.write_text(json.dumps(out, indent=1, default=str) + '\n')
print(json.dumps(out, indent=1, default=str))
