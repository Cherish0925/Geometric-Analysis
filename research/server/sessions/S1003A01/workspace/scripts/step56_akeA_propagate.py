"""Step 56b: constraint propagation for SU(2)-invariant AK Einstein (diagonal Bianchi IX).

State: (a,b,c,A,B,C,X1,X2,X3), A=a' etc, X_i = x_i^2, Omega = sum x_i w_i,
w_i = e0^e_i + eps e_j^e_k.  Closure: x_i' = mu_i x_i,
   mu_i = 2 eps a_i/(a_j a_k) - (a_j a_k)'/(a_j a_k).
Unit length:  K1 = sum X_i mu_i = 0.  Einstein: a_i'' from Ric_ii = lam (i=1..3),
Hamiltonian constraint H = G_00 + lam = 0.
We compute the derivation D along the Einstein+closure flow and the tower
K1, K2=D K1, ...; then test (numerically, exactly at rational points when
possible) the dimension of the constraint variety and q=|nabla Omega|^2.
"""
import sympy as sp, json, os, sys, random
sys.path.insert(0, os.path.dirname(__file__))
import step56_bianchiA_ake as B

t = B.t
a, b, c = B.a, B.b, B.c
lam = sp.symbols('lam')
eps = int(os.environ.get('EPS', '1'))
sa, sb, sc, A_, B_, C_ = sp.symbols('a b c A B C')
App, Bpp, Cpp = sp.symbols('App Bpp Cpp')
X = sp.symbols('X1 X2 X3')
def tosym(e):
    e = e.subs({sp.diff(a, t, 2): App, sp.diff(b, t, 2): Bpp, sp.diff(c, t, 2): Cpp})
    e = e.subs({sp.diff(a, t): A_, sp.diff(b, t): B_, sp.diff(c, t): C_})
    return sp.simplify(e.subs({a: sa, b: sb, c: sc}))
Ric = B.Ric.applyfunc(tosym)
for i in range(4):
    for j in range(4):
        if i != j: assert sp.simplify(Ric[i, j]) == 0, (i, j, Ric[i, j])
sol = sp.solve([Ric[1, 1]-lam, Ric[2, 2]-lam, Ric[3, 3]-lam], [App, Bpp, Cpp], dict=True)[0]
Rs = sum(Ric[i, i] for i in range(4))
H = sp.simplify((Ric[0, 0] - Rs/2 + lam).subs(sol))   # G_00 = -lam  <=> R=4lam with Ric_ii=lam
H = sp.factor(sp.together(H))
fr = [sa, sb, sc]; dr = [A_, B_, C_]
def mu(i):
    j, k = (i+1) % 3, (i+2) % 3
    return 2*eps*B.NB[i]*fr[i]/(fr[j]*fr[k]) - (dr[j]*fr[k] + fr[j]*dr[k])/(fr[j]*fr[k])
MU = [sp.simplify(mu(i)) for i in range(3)]
DER = {sa: A_, sb: B_, sc: C_, A_: sol[App], B_: sol[Bpp], C_: sol[Cpp]}
for i in range(3):
    DER[X[i]] = 2*X[i]*MU[i]
def Dt(e):
    return sp.together(sum(sp.diff(e, v)*DER[v] for v in DER))

# |nabla Omega|^2 : Omega components in frame; use B.G (connection) with functions -> symbols
G = [[[tosym(B.G[i][j][k]) for k in range(4)] for j in range(4)] for i in range(4)]
xs = sp.symbols('x1 x2 x3')
def Omega_tensor():
    O = sp.zeros(4)
    for i, (j, k) in zip([1, 2, 3], [(2, 3), (3, 1), (1, 2)]):
        O[0, i] += xs[i-1]; O[i, 0] -= xs[i-1]
        O[j, k] += eps*xs[i-1]; O[k, j] -= eps*xs[i-1]
    return O
O = Omega_tensor()
xder = {xs[i]: MU[i]*xs[i] for i in range(3)}
def nablaO(m):  # (nabla_{E_m} Omega)_{pq}
    M = sp.zeros(4)
    for p in range(4):
        for q in range(4):
            val = sum(sp.diff(O[p, q], xs[i])*xder[xs[i]] for i in range(3)) if m == 0 else 0
            for r in range(4):
                val -= G[m][p][r]*O[r, q] + G[m][q][r]*O[p, r]
            M[p, q] = val
    return M
q = sp.simplify(sum(nablaO(m)[p, r]**2 for m in range(4) for p in range(4) for r in range(4))/2)
q = sp.simplify(q.subs({xs[i]**2: X[i] for i in range(3)}))

if __name__ == '__main__':
    out = {'eps': eps, 'H': str(H), 'mu': [str(m) for m in MU], 'q': str(q)}
    print('H =', H); print('mu =', MU); print('q =', q)
    os.makedirs(os.path.join(os.path.dirname(__file__), '../data/step56'), exist_ok=True)
    json.dump(out, open(os.path.join(os.path.dirname(__file__), f'../data/step56/setupA_{"".join(map(str,B.NB))}_eps{eps}.json'), 'w'), indent=1)
