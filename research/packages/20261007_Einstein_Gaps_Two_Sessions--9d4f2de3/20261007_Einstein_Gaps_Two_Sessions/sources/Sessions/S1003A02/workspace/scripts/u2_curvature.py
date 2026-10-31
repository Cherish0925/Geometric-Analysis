"""Curvature of U(2)-invariant cohomogeneity-one metrics
    g = dt^2 + a(t)^2 s3^2 + b(t)^2 (s1^2 + s2^2)
on (0,T) x S^3, with left-invariant frame X_i on SU(2) satisfying
[X1,X2]=2X3 (cyclic); sum s_i^2 is the round unit S^3 (vol 2 pi^2).

Orthonormal frame E0=d/dt, E1=X1/b, E2=X2/b, E3=X3/a.
Outputs (sympy expressions in a,b and t-derivatives):
  scalar s, |Ric0|^2, |W+|^2, |W-|^2 (Hilbert-Schmidt norms of the
  endomorphisms of two-forms, i.e. the manuscript's operator convention),
  oriented by e0^e3^e1^e2 (the complex orientation for Kahler a = b b').
Writes the expressions to workspace/data/u2_curvature_exprs.txt and checks
FS, CH (Einstein, W- = 0) and the Burns metric.
"""
import itertools, os
import sympy as sp

t = sp.symbols('t', real=True)
a = sp.Function('a')(t)
b = sp.Function('b')(t)
n = 4
# structure functions c[i][j] = list of coefficients of [E_i,E_j] in E_k
C = [[[0]*4 for _ in range(4)] for _ in range(4)]
def setbr(i, j, vec):
    for k in range(4):
        C[i][j][k] = vec[k]
        C[j][i][k] = -vec[k]
bp, ap = sp.diff(b, t), sp.diff(a, t)
setbr(0, 1, [0, -bp/b, 0, 0])
setbr(0, 2, [0, 0, -bp/b, 0])
setbr(0, 3, [0, 0, 0, -ap/a])
setbr(1, 2, [0, 0, 0, 2*a/b**2])
setbr(2, 3, [0, 2/a, 0, 0])
setbr(3, 1, [0, 0, 2/a, 0])

def E(i, f):
    return sp.diff(f, t) if i == 0 else 0

# Koszul: G[i][j][k] = <nabla_{E_i} E_j, E_k>
c = lambda i, j, k: C[i][j][k]
G = [[[sp.simplify(sp.Rational(1, 2)*(c(i, j, k) - c(j, k, i) + c(k, i, j)))
       for k in range(4)] for j in range(4)] for i in range(4)]

def nabla(i, vec):
    # vec: components in frame; returns nabla_{E_i} vec
    out = [0]*4
    for j in range(4):
        out[j] += E(i, vec[j])
        for k in range(4):
            out[k] += vec[j]*G[i][j][k]
    return out

def unit(j):
    v = [0]*4; v[j] = 1; return v

R = {}
for i, j, k in itertools.product(range(4), repeat=3):
    v1 = nabla(i, nabla(j, unit(k)))
    v2 = nabla(j, nabla(i, unit(k)))
    br = C[i][j]
    v3 = [0]*4
    for m in range(4):
        if br[m] != 0:
            w = nabla(m, unit(k))
            for l in range(4):
                v3[l] += br[m]*w[l]
    for l in range(4):
        R[(i, j, k, l)] = sp.simplify(v1[l] - v2[l] - v3[l])  # <R(Ei,Ej)Ek, El>

# Rm(i,j,k,l) = <R(Ei,Ej)Ek,El>; Ric_jk = sum_i <R(Ei,Ej)Ek,Ei>
Ric = sp.Matrix(4, 4, lambda j, k: sp.simplify(sum(R[(i, j, k, i)] for i in range(4))))
s = sp.simplify(Ric.trace())
Ric0 = Ric - s/4*sp.eye(4)
ric0sq = sp.simplify(sum(Ric0[i, j]**2 for i in range(4) for j in range(4)))

# curvature operator on two-forms, basis of (anti)self-dual forms for orientation e0 e3 e1 e2
def form(p, q):
    F = sp.zeros(4)
    F[p, q] = 1; F[q, p] = -1
    return F
# orientation (0,3,1,2): self-dual forms
SD = [(form(0, 3) + form(1, 2))/sp.sqrt(2), (form(0, 1) + form(2, 3))/sp.sqrt(2), (form(0, 2) + form(3, 1))/sp.sqrt(2)]
ASD = [(form(0, 3) - form(1, 2))/sp.sqrt(2), (form(0, 1) - form(2, 3))/sp.sqrt(2), (form(0, 2) - form(3, 1))/sp.sqrt(2)]
# check orientation: e0^e3^e1^e2 = e0^e1^e2^e3 (even permutation 0312->0123: (3 1 2) cyclic) ok

def Rop(F, H):
    # <Rm(F), H> with Rm acting as curvature operator, R_{ijkl} F^{ij} H^{kl}/4 ; sign: Rm(e_i^e_j) = sum R_{ijlk}...
    tot = 0
    for i, j, k, l in itertools.product(range(4), repeat=4):
        if F[i, j] != 0 and H[k, l] != 0:
            tot += R[(i, j, k, l)]*F[i, j]*H[k, l]
    return -sp.simplify(tot/4)  # sign chosen so the round sphere has positive operator

def block(B1, B2):
    return sp.Matrix(3, 3, lambda p, q: sp.simplify(Rop(B1[p], B2[q])))
Ap = block(SD, SD); Am = block(ASD, ASD)
Wp = sp.simplify(Ap - s/12*sp.eye(3)); Wm = sp.simplify(Am - s/12*sp.eye(3))
wpsq = sp.simplify(sum(Wp[i, j]**2 for i in range(3) for j in range(3)))
wmsq = sp.simplify(sum(Wm[i, j]**2 for i in range(3) for j in range(3)))

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, '..', 'data', 'u2_curvature_exprs.txt')
    with open(out, 'w') as f:
        for name, e in [('s', s), ('ric0sq', ric0sq), ('wpsq', wpsq), ('wmsq', wmsq),
                        ('Ric_diag', [Ric[i, i] for i in range(4)]), ('trWp', sp.simplify(Wp.trace()))]:
            f.write(f'{name} = {e}\n')
    print('trace W+ ', sp.simplify(Wp.trace()), ' trace W- ', sp.simplify(Wm.trace()))
    print('offdiag Ric', [sp.simplify(Ric[i, j]) for i in range(4) for j in range(4) if i != j and Ric[i, j] != 0])
    def test(name, aa, bb):
        sub = lambda e: sp.simplify(e.subs({a: aa, b: bb}).doit())
        print(name, 's=', sub(s), ' ric0sq=', sub(ric0sq), ' |W+|^2=', sub(wpsq), ' |W-|^2=', sub(wmsq))
    test('flat', t, t)
    test('round S4? (sin t)', sp.sin(t), sp.sin(t))
    test('FS', sp.sin(t)*sp.cos(t), sp.sin(t))
    test('CH', sp.sinh(t)*sp.cosh(t), sp.sinh(t))
