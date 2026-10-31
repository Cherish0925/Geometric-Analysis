"""Step 37: SU(2)-invariant Seiberg--Witten reduction on diagonal Bianchi-IX metrics.

Metric g = dt^2 + sum a_i(t)^2 sigma_i^2, d sigma_i = 2 sigma_j ^ sigma_k (cyclic),
coframe e0=dt, ei=a_i sigma_i, orientation e0123.  Determinant connection
A = i sum alpha_i(t) sigma_i ; spinor twisted by L^{1/2} with connection A/2.
Invariant spinors are t-dependent vectors in the left-invariant frame.

Gamma matrices gamma^a=[[0,s_a],[-s_a^dag,0]], s_0=I, s_j=i tau_j  (gamma^2=-1).
Lower block = S^+ (self-dual forms act there).

This script derives symbolically:
  * the Levi-Civita connection forms;
  * which sign of the spin connection satisfies the Lichnerowicz formula
      D^2 = nabla^* nabla + s/4 + (1/2) c(F_A)
    on invariant spinors (checked as a rational identity in jets);
  * the reduced S^+ Dirac ODE  Phi' = M(t) Phi  and the curvature equation
      f^+ components phi_j = (alpha_j'/a_j + 2 alpha_j/(a_k a_l))/2 = n_j/2,
    n_j = Phi^* tau_j Phi,  which is the normalization F^+=2i sigma(Phi), |f^+|^2=rho^2/2.
Output: workspace/data/bianchi_sw_reduction.json (matrix M as strings, checks).
"""
import json
from pathlib import Path
import sympy as sp

t = sp.symbols('t', real=True)
a = [sp.Function(f'a{i}')(t) for i in (1, 2, 3)]
al = [sp.Function(f'al{i}')(t) for i in (1, 2, 3)]
I2 = sp.eye(2)
tau = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
s_ = [I2] + [sp.I * x for x in tau]
Z = sp.zeros(2)
gam = [sp.Matrix(sp.BlockMatrix([[Z, s_[k]], [-s_[k].H, Z]])) for k in range(4)]
for p in range(4):
    for q in range(4):
        ac = gam[p] * gam[q] + gam[q] * gam[p]
        assert sp.simplify(ac + 2 * (1 if p == q else 0) * sp.eye(4)) == sp.zeros(4)

# connection forms omega_{ab}(e_c): de^a = -omega_ab ^ e^b.
# de^0 = 0; de^i = (a_i'/a_i) e0^ei + 2 a_i/(a_j a_k) e^j ^ e^k.
# Solve with unknown coefficients w[a][b][c] = omega_ab(e_c), antisymmetric in ab.
W = {}
unk = []
for p in range(4):
    for q in range(p + 1, 4):
        for c in range(4):
            v = sp.Symbol(f'w{p}{q}{c}')
            W[(p, q, c)] = v; W[(q, p, c)] = -v; unk.append(v)
for p in range(4):
    for c in range(4):
        W[(p, p, c)] = 0
def de(p):
    # returns dict {(b,c):coef} with b<c meaning coef e^b^e^c
    d = {}
    if p == 0:
        return d
    i = p - 1; j = (i + 1) % 3; k = (i + 2) % 3
    d[(0, p)] = sp.diff(a[i], t) / a[i]
    jj, kk = j + 1, k + 1
    if jj < kk:
        d[(jj, kk)] = 2 * a[i] / (a[j] * a[k])
    else:
        d[(kk, jj)] = -2 * a[i] / (a[j] * a[k])
    return d
eqs = []
for p in range(4):
    lhs = de(p)
    # -omega_pb ^ e^b = - sum_b sum_c omega_pb(e_c) e^c ^ e^b
    rhs = {}
    for b in range(4):
        for c in range(4):
            if b == c: continue
            coef = -W[(p, b, c)]
            key = (min(c, b), max(c, b)); sg = 1 if c < b else -1
            rhs[key] = rhs.get(key, 0) + sg * coef
    keys = set(lhs) | set(rhs)
    for kk in keys:
        eqs.append(sp.Eq(lhs.get(kk, 0), rhs.get(kk, 0)))
sol = sp.solve(eqs, unk, dict=True)[0]
Wn = {key: sp.simplify(sp.sympify(v).subs(sol)) for key, v in W.items()}

def spin_conn(c, sign):
    return sign * sp.Rational(1, 4) * sum((Wn[(p, q, c)] * gam[p] * gam[q] for p in range(4) for q in range(4)), sp.zeros(4))
def Acomp(c):
    return 0 if c == 0 else al[c - 1] / a[c - 1]   # A(e_c) = i alpha_c/a_c

Phi4 = sp.Matrix([sp.Function(f'P{k}')(t) for k in range(4)])
def N(c, Psi, sign):
    d = sp.diff(Psi, t) if c == 0 else sp.zeros(4, 1)
    return d + spin_conn(c, sign) * Psi + sp.I * sp.Rational(1, 2) * Acomp(c) * Psi
def Dirac(Psi, sign):
    return sum((gam[c] * N(c, Psi, sign) for c in range(4)), sp.zeros(4, 1))
def roughlap(Psi, sign):
    # nabla^*nabla Psi = -sum_a [N_a N_a Psi - sum_b omega_ba(e_a) N_b Psi]  (nabla_{e_a} e_a = sum_b omega_ba(e_a) e_b)
    out = sp.zeros(4, 1)
    for c in range(4):
        out += N(c, N(c, Psi, sign), sign)
        for b in range(4):
            out -= Wn[(b, c, c)] * N(b, Psi, sign)
    return -out
# scalar curvature from standard formula via A01 convention: compute by Cartan curvature
# Omega_ab = d omega_ab + omega_ac ^ omega_cb ; easier: use Lichnerowicz residual to read s.
# Curvature Clifford action of F_A
def Fform():
    F = {}
    for i in range(3):
        j = (i + 1) % 3; k = (i + 2) % 3
        F[(0, i + 1)] = sp.diff(al[i], t) / a[i]
        jj, kk = j + 1, k + 1
        val = 2 * al[i] / (a[j] * a[k])
        if jj < kk: F[(jj, kk)] = val
        else: F[(kk, jj)] = -val
    return F   # F_A = i * sum F_{bc} e^b ^ e^c  (b<c)
Fd = Fform()
cF = sp.I * sum((v * gam[p] * gam[q] for (p, q), v in Fd.items()), sp.zeros(4))

res = {}
for sign in (1, -1):
    L = Dirac(Dirac(Phi4, sign), sign) - roughlap(Phi4, sign) - sp.Rational(1, 2) * cF * Phi4
    L = sp.simplify(L)
    # L should be (s/4) Phi4 : check that L_k/Phi_k is the same function, independent of Phi
    ratios = []
    ok = True
    for k in range(4):
        expr = sp.expand(L[k])
        # coefficient structure: must be proportional to P_k only
        others = [sp.Function(f'P{m}')(t) for m in range(4) if m != k]
        for o in others + [sp.diff(sp.Function(f'P{m}')(t), t) for m in range(4)]:
            if sp.simplify(sp.diff(expr, o)) != 0:
                ok = False
        ratios.append(sp.simplify(sp.diff(expr, sp.Function(f'P{k}')(t))))
    same = all(sp.simplify(r - ratios[0]) == 0 for r in ratios)
    res[sign] = dict(ok=ok, same=same, s_over_4=str(sp.simplify(ratios[0])) if same else None)
print('Lichnerowicz checks', {k: (v['ok'], v['same']) for k, v in res.items()})
good = [sg for sg, v in res.items() if v['ok'] and v['same']]
assert good, 'no consistent spin-connection sign'
sign = good[0]
s4 = sp.sympify(res[sign]['s_over_4'])
# compare with standard Bianchi-IX scalar curvature
a1, a2, a3 = a
def scal():
    # s = -2 sum a_i''/a_i - 2 sum_{i<j} a_i'a_j'/(a_i a_j) + (2/(a1a2a3)^2)*(2(a1^2a2^2+...) - (a1^4+a2^4+a3^4))*?  -> compare numerically instead
    return None
# Reduced S^+ Dirac: lower block. D maps S^+ (lower) to S^- (upper): upper rows of Dirac applied to (0,0,phi).
ph = sp.Matrix([sp.Function('p1')(t), sp.Function('p2')(t)])
Psi = sp.Matrix([0, 0, ph[0], ph[1]])
Dp = sp.simplify(Dirac(Psi, sign))
upper = sp.Matrix([Dp[0], Dp[1]])
lowerzero = [sp.simplify(Dp[2]), sp.simplify(Dp[3])]
# Solve upper = 0 for ph'
d1, d2 = sp.symbols('d1 d2')
eqs = [sp.Eq(upper[k].subs({sp.diff(ph[0], t): d1, sp.diff(ph[1], t): d2}), 0) for k in range(2)]
sl = sp.solve(eqs, [d1, d2], dict=True)[0]
P1, P2 = sp.symbols('P1 P2')
rep = {ph[0]: P1, ph[1]: P2}
M = sp.zeros(2)
for r, dd in enumerate((d1, d2)):
    ex = sp.expand(sl[dd].subs(rep))
    M[r, 0] = sp.simplify(sp.diff(ex, P1)); M[r, 1] = sp.simplify(sp.diff(ex, P2))
# Check c(F^+) on S^+ block: lower-right block of cF equals 2 sum phi_j tau_j where phi_j = SD component
cFl = cF[2:, 2:]
phij = [sp.Rational(1, 2) * (sp.diff(al[i], t) / a[i] + 2 * al[i] / (a[(i + 1) % 3] * a[(i + 2) % 3])) for i in range(3)]
chk = sp.simplify(cFl - 2 * sum((phij[i] * tau[i] for i in range(3)), sp.zeros(2)))
# sign check: maybe -2
chk2 = sp.simplify(cFl + 2 * sum((phij[i] * tau[i] for i in range(3)), sp.zeros(2)))
out = dict(spin_sign=sign, lichnerowicz=res, s_over_4=str(s4),
           M=[[str(M[r, c]) for c in range(2)] for r in range(2)],
           lower_rows_zero=[str(x) for x in lowerzero],
           cF_plus_minus_2phitau=str(chk), cF_plus_plus_2phitau=str(chk2),
           omega={f'{p}{q}{c}': str(Wn[(p, q, c)]) for p in range(4) for q in range(p + 1, 4) for c in range(4) if Wn[(p, q, c)] != 0})
path = Path(__file__).resolve().parents[1] / 'data' / 'bianchi_sw_reduction.json'
path.write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out, indent=1))
