"""Check the x-gauge (a1^2=x) form of the antisymmetric CH mass mode used in tail-augmented cells:
   F = x e^{-2 eps th},  w = log(1+x) - eps th (1+2x)/(1+x),  G = x(1+x) + eps (th x + 2 x^2 (1+x) th'),
with th = theta_1 = -(6x^2+4x+1)/(24x^2(1+x)^2).  Expect dz_i = 0, ds = 0 at first order in eps,
and v_- = u1-u3 = eps f_- + O(eps^2) with f_- = x/(1+x)^{5/2}.  Also check a general th(x): the
first-order Ric0 must then be proportional to the antisymmetric Jacobi operator only."""
import sympy as sp
x, eps = sp.symbols('x epsilon', positive=True)

def curv_x(a, G):
    D = lambda f: 2*sp.sqrt(G)*sp.diff(f, x)
    idx = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    u = [D(a[i]) - (a[j]**2 + a[k]**2 - a[i]**2)/(a[j]*a[k]) for i, j, k in idx]
    H = [u[i] + u[j]*u[k]/2 for i, j, k in idx]
    r = [D(u[i])/a[i] for i, j, k in idx]
    v = [2*H[i]/(a[j]*a[k]) for i, j, k in idx]
    z = [r[i] - v[i] for i in range(3)]
    s = -2*sum(r[i] + v[i] for i in range(3))
    return u, z, s

def first(e):
    return sp.simplify(sp.diff(e, eps).subs(eps, 0))

for label, th in [('mass', -(6*x**2+4*x+1)/(24*x**2*(1+x)**2)), ('general', sp.Function('th')(x))]:
    F = x*sp.exp(-2*eps*th)
    w = sp.log(1+x) - eps*th*(1+2*x)/(1+x)
    G = x*(1+x) + eps*(th*x + 2*x**2*(1+x)*sp.diff(th, x))
    u, z, s = curv_x([sp.sqrt(x), sp.sqrt(x*sp.exp(w)), sp.sqrt(F)], G)
    dz = [sp.factor(first(zz)) for zz in z]; ds = sp.factor(first(s))
    dv = sp.factor(first(u[0] - u[2])); dvp = sp.factor(first(u[0] + u[2])); du2 = sp.factor(first(u[1]))
    print(label, 'dz =', dz); print(label, 'ds =', ds)
    print(label, 'dv_- =', dv, ' dv_+ =', dvp, ' du2 =', du2)
