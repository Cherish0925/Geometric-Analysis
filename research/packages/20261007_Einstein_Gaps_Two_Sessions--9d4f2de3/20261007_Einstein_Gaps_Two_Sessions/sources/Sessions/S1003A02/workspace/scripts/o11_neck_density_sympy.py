"""Analytic neck density for the perpendicular Burns cell in CH (sympy).

Family (exact Burns at the bolt, exact CH at the collar, used in o11_perp_logneck.py):
   a1 = sqrt(S^2+x0) e^{x0 C1}, a2 = sqrt(S^2+x0) cosh(t) e^{x0 C2}, a3 = sinh(t) e^{x0 C3},
with constant C_i in the neck  sqrt(x0) << t << 1.
We expand the calibrated P density (S1+S2+S3+cubic) and the scalar density (J-P) per unit
s = log t to order x0^2, and extract the t^0 coefficient (the log-divergent part).
Output: the quadratic forms in C, their minima, and the optimal plateau u1/x0.
"""
import sympy as sp

t, x0 = sp.symbols('t x0', positive=True)
C1, C2, C3 = sp.symbols('C1 C2 C3', real=True)
eps = sp.symbols('epsilon', positive=True)

S = sp.sinh(t); Ch = sp.cosh(t)
X = eps*x0
a = [sp.sqrt(S**2 + X)*sp.exp(X*C1), sp.sqrt(S**2 + X)*Ch*sp.exp(X*C2), S*sp.exp(X*C3)]

def u_i(i):
    j, k = (i+1) % 3, (i+2) % 3
    return sp.diff(a[i], t) - (a[j]**2 + a[k]**2 - a[i]**2)/(a[j]*a[k])

u = [u_i(i) for i in range(3)]
ud = [sp.diff(ui, t) for ui in u]
H = [u[0] + u[1]*u[2]/2, u[1] + u[2]*u[0]/2, u[2] + u[0]*u[1]/2]
lam = [a[1]*a[2]/a[0], a[2]*a[0]/a[1], a[0]*a[1]/a[2]]
S1 = lam[0]/4*(ud[0] + 2*H[0]/lam[0])**2
S2 = lam[1]/4*(ud[1] - (2*u[1] - u[0]*u[2])/lam[1])**2
S3 = lam[2]/4*(ud[2] + 2*H[2]/lam[2])**2
cub = 2*u[0]*u[1]*u[2]/lam[1]
Sig = sum(ud[i]/a[i] + 2*H[i]/(a[(i+1) % 3]*a[(i+2) % 3]) for i in range(3))
scal = a[0]*a[1]*a[2]/4*(Sig - 12)**2

def neck_coeff(expr, name):
    # per ds density = t * expr; take order eps^2, then Laurent-expand in t and keep t^0
    e2 = sp.diff(t*expr, eps, 2).subs(eps, 0)/2
    e2 = sp.simplify(e2)
    ser = sp.series(e2, t, 0, 2).removeO()
    c0 = sp.simplify(sp.expand(ser).coeff(t, 0))
    print(name, ' t^0 coefficient / x0^2 :', sp.factor(sp.expand(c0/x0**2)))
    # also show the singular part (t^-2, t^-4) for the record
    for p in (-4, -2):
        print('   t^%d coefficient:' % p, sp.factor(sp.expand(ser).coeff(t, p)))
    return sp.expand(c0/x0**2)

dS1 = neck_coeff(S1, 'S1'); dS2 = neck_coeff(S2, 'S2'); dS3 = neck_coeff(S3, 'S3')
dcub = neck_coeff(cub, 'cubic'); dscal = neck_coeff(scal, 'scalar(J-P)')
# u1 neck value
u1n = sp.series(sp.diff(u[0], eps).subs(eps, 0), t, 0, 1).removeO()
print('u1/x0 in neck (leading):', sp.simplify(sp.expand(u1n).coeff(t, 0)/x0))
fP = sp.expand(dS1 + dS2 + dS3 + dcub); fJ = sp.expand(fP + dscal)
print('P neck density / x0^2 =', fP)
print('J neck density / x0^2 =', fJ)
for name, f in (('P', fP), ('J', fJ)):
    sol = sp.solve([sp.diff(f, c) for c in (C1, C2, C3)], [C1, C2, C3], dict=True)
    Hm = sp.hessian(f, (C1, C2, C3))
    print(name, 'Hessian eigen:', [sp.nsimplify(e) for e in Hm.eigenvals()])
    for so in sol:
        print(name, 'optimum', so, ' value', sp.nsimplify(f.subs(so)),
              ' u1/x0 =', sp.nsimplify(sp.expand(u1n).coeff(t, 0).subs(so)/x0))
