"""Test U(2)-invariant Kahler (Calabi) profiles a1=a3=sqrt(x), a2=sqrt(G), dt=dx/(2 sqrt G)
for the Einstein condition with Ric=-6g.  Candidate: G = x + x^2 + m/x + n (general check)."""
import sympy as sp
x, m, n = sp.symbols('x m n')
def curv_x(a, G):
    # a_i functions of x; d/dt = 2 sqrt(G) d/dx
    D = lambda f: 2*sp.sqrt(G)*sp.diff(f, x)
    idx = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    u = [D(a[i]) - (a[j]**2 + a[k]**2 - a[i]**2)/(a[j]*a[k]) for i, j, k in idx]
    H = [u[i] + u[j]*u[k]/2 for i, j, k in idx]
    r = [D(u[i])/a[i] for i, j, k in idx]
    v = [2*H[i]/(a[j]*a[k]) for i, j, k in idx]
    z = [sp.simplify(r[i] - v[i]) for i in range(3)]
    s = sp.simplify(-2*sum(r[i] + v[i] for i in range(3)))
    return u, z, s
G = x + x**2 + m/x + n
u, z, s = curv_x([sp.sqrt(x), sp.sqrt(G), sp.sqrt(x)], G)
print('z =', [sp.factor(zz) for zz in z]); print('s =', sp.factor(s))
print('u =', [sp.simplify(uu) for uu in u])
