#!/usr/bin/env python3
"""Exact curvature invariants for the self-dual Taub--NUT--AdS metric.

Metric convention:
 g = dr^2/F + (r^2-nu^2)(dtheta^2+sin^2(theta)dphi^2)
     + 4 nu^2 F (dpsi+cos(theta)dphi)^2,
 F=(r-nu)/(r+nu)*(1+(r-nu)(r+3nu)/3), so Ric=-g.

The SU(2) action makes scalar invariants independent of theta,phi,psi.  We
construct all coordinate derivatives first and only then evaluate at theta=pi/2.
"""
import sympy as sp

r, th, ph, ps, nu = sp.symbols('r th ph ps nu', positive=True, real=True)
x = (r, th, ph, ps)
n = 4
F = sp.factor((r-nu)/(r+nu) * (1 + (r-nu)*(r+3*nu)/sp.Integer(3)))
A = r**2 - nu**2
B = 4*nu**2*F
s = sp.sin(th)
c = sp.cos(th)

g = sp.zeros(n)
g[0,0] = 1/F
g[1,1] = A
g[2,2] = A*s**2 + B*c**2
g[2,3] = g[3,2] = B*c
g[3,3] = B

ginv = sp.zeros(n)
ginv[0,0] = F
ginv[1,1] = 1/A
ginv[2,2] = 1/(A*s**2)
ginv[2,3] = ginv[3,2] = -c/(A*s**2)
ginv[3,3] = 1/B + c**2/(A*s**2)

# Verify inverse before doing tensor algebra.
assert sp.simplify(g*ginv - sp.eye(n)) == sp.zeros(n)

print('F =', F)
print('building Christoffels...')
Gamma = [[[sp.S.Zero for k in range(n)] for j in range(n)] for i in range(n)]
for a in range(n):
    for b in range(n):
        for cc in range(n):
            val = sp.S.Zero
            for d in range(n):
                val += ginv[a,d]*(sp.diff(g[d,cc],x[b]) + sp.diff(g[d,b],x[cc]) - sp.diff(g[b,cc],x[d]))
            Gamma[a][b][cc] = sp.factor(val/2)

print('building mixed Riemann tensor at theta=pi/2...')
# R^a_{ b c d } = d_c Gamma^a_{db} - d_d Gamma^a_{cb} + Gamma^a_{ce}Gamma^e_{db} - Gamma^a_{de}Gamma^e_{cb}
Rmix = [[[[sp.S.Zero for d in range(n)] for cc in range(n)] for b in range(n)] for a in range(n)]
subs_eq = {th: sp.pi/2}
for a in range(n):
    for b in range(n):
        for cc in range(n):
            for d in range(n):
                val = sp.diff(Gamma[a][d][b],x[cc]) - sp.diff(Gamma[a][cc][b],x[d])
                for e in range(n):
                    val += Gamma[a][cc][e]*Gamma[e][d][b] - Gamma[a][d][e]*Gamma[e][cc][b]
                Rmix[a][b][cc][d] = sp.factor(sp.trigsimp(val.subs(subs_eq)))

geq = sp.simplify(g.subs(subs_eq))
gieq = sp.simplify(ginv.subs(subs_eq))

print('checking Ricci...')
Ric = sp.zeros(n)
for b in range(n):
    for d in range(n):
        Ric[b,d] = sp.factor(sum(Rmix[a][b][a][d] for a in range(n)))
print('Ric+g entries:')
print(sp.simplify(Ric + geq))

print('lowering first index...')
Rlow = [[[[sp.S.Zero for d in range(n)] for cc in range(n)] for b in range(n)] for a in range(n)]
for a in range(n):
    for b in range(n):
        for cc in range(n):
            for d in range(n):
                Rlow[a][b][cc][d] = sp.factor(sum(geq[a,e]*Rmix[e][b][cc][d] for e in range(n)))

print('contracting Kretschmann scalar...')
# At theta=pi/2 the metric is diagonal, so contraction is particularly cheap.
diag_inv = [sp.factor(gieq[i,i]) for i in range(n)]
Kretsch = sp.S.Zero
for a in range(n):
    for b in range(n):
        for cc in range(n):
            for d in range(n):
                if Rlow[a][b][cc][d] != 0:
                    Kretsch += diag_inv[a]*diag_inv[b]*diag_inv[cc]*diag_inv[d]*Rlow[a][b][cc][d]**2
Kretsch = sp.factor(sp.cancel(sp.trigsimp(Kretsch)))
W2 = sp.factor(sp.cancel(Kretsch - sp.Rational(8,3)))
print('Kretschmann =', Kretsch)
print('|W|^2 =', W2)
print('|W|^2 at r=nu =', sp.factor(sp.limit(W2, r, nu, dir='+')))

# Curvature-operator blocks on Lambda^+ and Lambda^- in the oriented
# orthonormal coframe (e0,e1,e2,e3).  Pair order is 01,02,03,23,31,12,
# so the self-dual basis is (01+23),(02+31),(03+12), each /sqrt(2).
h = [sp.sqrt(geq[i,i]) for i in range(n)]
pairs = [(0,1),(0,2),(0,3),(2,3),(3,1),(1,2)]
R6 = sp.zeros(6)
for I,(a,b) in enumerate(pairs):
    for J,(cc,d) in enumerate(pairs):
        R6[I,J] = sp.factor(sp.cancel(Rlow[a][b][cc][d]/(h[a]*h[b]*h[cc]*h[d])))
Splus = sp.zeros(6,3)
Sminus = sp.zeros(6,3)
for j in range(3):
    Splus[j,j]=1/sp.sqrt(2); Splus[j+3,j]=1/sp.sqrt(2)
    Sminus[j,j]=1/sp.sqrt(2); Sminus[j+3,j]=-1/sp.sqrt(2)
Rp = sp.simplify(Splus.T*R6*Splus)
Rm = sp.simplify(Sminus.T*R6*Sminus)
Wplus = sp.simplify(Rp + sp.eye(3)/3)  # s/12=-1/3
Wminus = sp.simplify(Rm + sp.eye(3)/3)
# On r>nu all square-root arguments are positive, so sqrt(Q)*sqrt(1/Q)=1.
Q = 3*nu**3 - 5*nu**2*r + nu*r**2 - 3*nu + r**3 + 3*r
def simp_pos(z):
    z = z.subs(sp.sqrt(1/Q), 1/sp.sqrt(Q))
    z = sp.powdenest(z, force=True)
    return sp.factor(sp.cancel(z))
Wplus = Wplus.applyfunc(simp_pos)
Wminus = Wminus.applyfunc(simp_pos)
print('W+ operator =')
print(Wplus)
print('W- operator =')
print(Wminus)
print('W+ eigenvalues =', Wplus.eigenvals())
print('W- eigenvalues =', Wminus.eigenvals())

# Radial cumulative Weyl energy.  Angular integral of dmu is 32*pi^2*nu*(r^2-nu^2)
# for phi period 2pi, psi period 4pi, theta integral 2.
R = sp.symbols('R', positive=True, real=True)
density_radial = sp.factor(32*sp.pi**2*nu*(r**2-nu**2)*W2)
print('radial Weyl-energy density =', density_radial)
primitive = sp.integrate(density_radial, r)
print('radial primitive =', sp.factor(primitive))
energy_to_R = sp.factor(sp.simplify(primitive.subs(r,R)-sp.limit(primitive,r,nu,dir='+')))
print('Weyl energy nut..R =', energy_to_R)
print('Weyl energy nut..infinity =', sp.factor(sp.limit(energy_to_R,R,sp.oo)))
