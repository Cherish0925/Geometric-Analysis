#!/usr/bin/env python3
"""Pointwise check of the conformal formulas used in BUN:conformal on the actual sheared background
G = dt^2 + b^2 dtheta^2 + du^2 + a^2(ds + z zeta' du)^2  (a = a0 cosh u, b = ell cosh t):
 (i)  Phi(e^{2w}G) = Phi(G) + (e^{2w}-1)G - 2 Hess w + 2 dw(x)dw - (Lap w + 2|dw|^2) G,   w = w(t,u) arbitrary;
 (ii) <Phi(e^{2w}G),Q>_G - <Phi(G),Q>_G = -2<Hess w,Q> + 2 Q(grad w,grad w)  for the TT tensor Q = sech^2 t (dt^2 - b^2 dtheta^2);
 (iii) scalar curvature: s(e^{2w}G) = e^{-2w}( s_G - 6 Lap w - 6|dw|^2 ).
Ricci of the conformal metric is computed directly from its coordinate expression."""
import sympy as sp
t, th, u, s = sp.symbols('t theta u s', real=True)
a0, ell = sp.symbols('a0 ell', positive=True)
X = [t, th, u, s]; n = 4
z = sp.Function('z')(t); zeta = sp.Function('zeta')(u); wf = sp.Function('w')(t, u)
a = a0*sp.cosh(u); b = ell*sp.cosh(t); sh = z*sp.diff(zeta, u)
G = sp.zeros(4,4); G[0,0]=1; G[1,1]=b**2; G[2,2]=1+a**2*sh**2; G[2,3]=G[3,2]=a**2*sh; G[3,3]=a**2
def ricci(g):
    ginv = g.inv()
    Gam = [[[sum(ginv[i,l]*(sp.diff(g[l,j],X[k])+sp.diff(g[l,k],X[j])-sp.diff(g[j,k],X[l])) for l in range(n))/2
             for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.zeros(n,n)
    for j in range(n):
        for l in range(j,n):
            Ric[j,l]=Ric[l,j]=sum(sp.diff(Gam[i][l][j],X[i])-sp.diff(Gam[i][i][j],X[l])
                 +sum(Gam[i][i][m]*Gam[m][l][j]-Gam[i][l][m]*Gam[m][i][j] for m in range(n)) for i in range(n))
    return Ric, Gam, ginv
RicG, Gam, Ginv = ricci(G)
RicC, _, _ = ricci(sp.exp(2*wf)*G)
dw = [sp.diff(wf, x_) for x_ in X]
Hess = sp.Matrix(n, n, lambda i,j: sp.diff(wf, X[i], X[j]) - sum(Gam[k][i][j]*dw[k] for k in range(n)))
Lap = sum(Ginv[i,j]*Hess[i,j] for i in range(n) for j in range(n))
nw2 = sum(Ginv[i,j]*dw[i]*dw[j] for i in range(n) for j in range(n))
dwdw = sp.Matrix(n, n, lambda i,j: dw[i]*dw[j])
lhs = RicC + sp.exp(2*wf)*G
rhs = RicG + G + (sp.exp(2*wf)-1)*G - 2*Hess + 2*dwdw - (Lap + 2*nw2)*G
print("(i)  max residual entry:", set((lhs-rhs).applyfunc(lambda e_: sp.simplify(e_.rewrite(sp.exp)))))
Q = sp.zeros(4,4); Q[0,0] = sp.sech(t)**2; Q[1,1] = -sp.sech(t)**2*b**2
pair = lambda S_: sum(Ginv[i,k]*Ginv[j,l]*S_[i,j]*Q[k,l] for i in range(n) for j in range(n) for k in range(n) for l in range(n))
gradw = [sum(Ginv[i,j]*dw[j] for j in range(n)) for i in range(n)]
Qgw = sum(Q[i,j]*gradw[i]*gradw[j] for i in range(n) for j in range(n))
print("(ii) residual:", sp.simplify((pair(lhs) - pair(RicG+G) + 2*pair(Hess) - 2*Qgw).rewrite(sp.exp)))
sC = sum((sp.exp(-2*wf)*Ginv)[i,j]*RicC[i,j] for i in range(n) for j in range(n))
sG = sum(Ginv[i,j]*RicG[i,j] for i in range(n) for j in range(n))
print("(iii) residual:", sp.simplify((sC - sp.exp(-2*wf)*(sG - 6*Lap - 6*nw2)).rewrite(sp.exp)))
