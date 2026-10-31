"""Exact Hamiltonian of the variable-coefficient seed S=-f(a,u2) Phi (Step 17).
Checks  H_S = -f[(1-f)Q+kappa] - Phi D0 f + (a2^2 Phi f_{u2}/W)(2 f Phi_{u2} + Phi f_{u2}),
with Q = sum a_i^2 Phi_{u_i}^2/W, kappa = 2 u1 u2 u3/lambda_2.
"""
import sympy as sp
a = sp.symbols('a1:4', positive=True); u = sp.symbols('u1:4', real=True)
W = a[0]*a[1]*a[2]
jk = lambda i: ((i+1) % 3, (i+2) % 3)
gam = [(a[jk(i)[0]]**2+a[jk(i)[1]]**2-a[i]**2)/(a[jk(i)[0]]*a[jk(i)[1]]) for i in range(3)]
H = [u[i]+u[jk(i)[0]]*u[jk(i)[1]]/2 for i in range(3)]
lam = [a[jk(i)[0]]*a[jk(i)[1]]/a[i] for i in range(3)]
D0 = lambda S: sum(sp.diff(S, a[i])*(u[i]+gam[i])+sp.diff(S, u[i])*2*H[i]/lam[i] for i in range(3))
HS = lambda S: D0(S)+sum(a[i]**2*sp.diff(S, u[i])**2 for i in range(3))/W
f = sp.Function('f')(*a, u[1])
Phi = u[0]**2+u[2]**2+u[0]*u[1]*u[2]
Q = sum(a[i]**2*sp.diff(Phi, u[i])**2 for i in range(3))/W
kap = 2*u[0]*u[1]*u[2]/lam[1]
fu2 = sp.diff(f, u[1])
rhs = -f*((1-f)*Q+kap)-Phi*D0(f)+(a[1]**2*Phi*fu2/W)*(2*f*sp.diff(Phi, u[1])+Phi*fu2)
r = sp.simplify(sp.expand(HS(-f*Phi)-rhs))
print('variable-coefficient seed residual =', r)
assert r == 0
