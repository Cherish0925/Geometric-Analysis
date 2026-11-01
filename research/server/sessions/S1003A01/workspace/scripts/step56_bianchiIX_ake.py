"""Step 56: SU(2)-invariant (diagonal Bianchi IX) almost-Kahler Einstein test.

Question: does the diagonal Bianchi IX class
    g = dt^2 + a^2 s1^2 + b^2 s2^2 + c^2 s3^2,   d s_i = 2 s_j ^ s_k (cyclic)
contain strictly almost-Kahler Einstein metrics with lambda<0, where the
almost-Kahler form is an SU(2)-invariant unit self-dual form
    Omega = x1 w1 + x2 w2 + x3 w3,  w_i = e0^e_i + eps e_j^e_k,  sum x_i^2 = 1 ?

Method: frame Cartan/Koszul curvature (exact sympy), Einstein ODE solved for
second derivatives, then closure d Omega = 0 is a first-order system for
(x_i) and constraint propagation along t is computed exactly.
Output: printed constraint ideal; JSON in workspace/data/step56/.
"""
import sympy as sp, json, os, itertools, sys

t = sp.symbols('t')
lam = sp.symbols('lambda')
a, b, c = [sp.Function(n)(t) for n in 'abc']
F = [None, a, b, c]

# coframe e0=dt, e1=a s1, e2=b s2, e3=c s3.  de^i = 1/2 D^i_jk e^j e^k
D = [[[0]*4 for _ in range(4)] for _ in range(4)]
def setD(i, j, k, val):
    D[i][j][k] = val; D[i][k][j] = -val
for i, (j, k) in zip([1, 2, 3], [(2, 3), (3, 1), (1, 2)]):
    fi, fj, fk = F[i], F[j], F[k]
    # d(f_i s_i) = f_i' dt^s_i + 2 f_i s_j^s_k = (f_i'/f_i) e0^ei + (2 f_i/(f_j f_k)) ej^ek
    setD(i, 0, i, sp.diff(fi, t)/fi)
    setD(i, j, k, 2*fi/(fj*fk))
# [E_j,E_k] = - D^i_jk E_i
def brk(j, k):
    return [-D[i][j][k] for i in range(4)]
def E(i, f):
    return sp.diff(f, t) if i == 0 else 0
# Koszul for orthonormal frame: 2 G_ijk = c_ijk - c_jki + c_kij, c_ijk=g([Ei,Ej],Ek)
cc = [[[brk(i, j)[k] for k in range(4)] for j in range(4)] for i in range(4)]
G = [[[sp.simplify((cc[i][j][k] - cc[j][k][i] + cc[k][i][j])/2) for k in range(4)]
      for j in range(4)] for i in range(4)]   # g(nabla_Ei Ej, Ek)
def nab(i, vec):  # vec: components in frame
    out = [E(i, vec[k]) for k in range(4)]
    for j in range(4):
        if vec[j] != 0:
            for k in range(4):
                out[k] += vec[j]*G[i][j][k]
    return out
basis = [[1 if m == n else 0 for m in range(4)] for n in range(4)]
def Rvec(i, j, k):
    t1 = nab(i, nab(j, basis[k])); t2 = nab(j, nab(i, basis[k]))
    br = brk(i, j); t3 = [0]*4
    for m in range(4):
        if br[m] != 0:
            v = nab(m, basis[k])
            t3 = [t3[n] + br[m]*v[n] for n in range(4)]
    return [sp.simplify(t1[n] - t2[n] - t3[n]) for n in range(4)]
Rm = {}
for i in range(4):
    for j in range(4):
        for k in range(4):
            Rm[(i, j, k)] = Rvec(i, j, k)
Ric = sp.zeros(4)
for j in range(4):
    for k in range(4):
        Ric[j, k] = sp.simplify(sum(Rm[(i, j, k)][i] for i in range(4)))

if __name__ == '__main__' and 'test' in sys.argv:
    s = sp.symbols('s', positive=True)
    for kk in [sp.Rational(1, 2), 1, 2]:
        sub = {a: kk*sp.sinh(t), b: kk*sp.sinh(t), c: kk*sp.sinh(t)}
        print(kk, [sp.simplify(Ric[i, i].subs(sub).doit()) for i in range(4)])
    sys.exit()
