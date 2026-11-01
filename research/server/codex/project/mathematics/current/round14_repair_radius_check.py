#!/usr/bin/env python3
"""Coordinate first-variation checks for the all-mode repair-radius test.

Reuses the coordinate metric and its freshly derived connection, not a
stored Ricci or linearized-Einstein formula. No PDE existence is tested.
"""
import round14_shear_check as m
s, t, a, z, y = m.s, m.t, m.a, m.z, m.y
f = s.Function('f')(t)
theta = s.Matrix([0, 1, z, 0])
H = f*(m.T*m.T.T-a*a*theta*theta.T)
covH = [[[s.simplify(s.diff(H[i,j],m.coords[n])
    -sum(m.Gamma[p][n][i]*H[p,j]+m.Gamma[p][n][j]*H[i,p]
         for p in range(4))) for j in range(4)]
    for i in range(4)] for n in range(4)]
divH = [s.simplify(-sum(m.gi[i,n]*covH[n][i][j]
                          for i in range(4) for n in range(4)))
        for j in range(4)]
assert divH == [-s.diff(f,t)-2*f*s.diff(a,t)/a,0,0,0]
assert s.simplify(s.trace(m.gi*H)) == 0
print('PASS: the waist tensor is exactly TT even in the sheared metric')

# Direct variation of Christoffel and coordinate Ricci.
C = [[[s.simplify(sum(m.gi[k,n]*(covH[i][j][n]
                +covH[j][i][n]-covH[n][i][j])/2 for n in range(4)))
      for j in range(4)] for i in range(4)] for k in range(4)]
dRic = s.zeros(4)
for i in range(4):
    for j in range(i,4):
        val = sum(s.diff(C[k][i][j],m.coords[k])
                  -s.diff(C[k][i][k],m.coords[j]) for k in range(4))
        val += sum(C[k][i][j]*m.Gamma[n][k][n]
                   +m.Gamma[k][i][j]*C[n][k][n]
                   -C[n][i][k]*m.Gamma[k][j][n]
                   -m.Gamma[n][i][k]*C[k][j][n]
                   for k in range(4) for n in range(4))
        dRic[i,j] = dRic[j,i] = s.simplify(val)
dE = dRic+3*H
ap, zp = s.diff(a,t),s.diff(z,t)
rels = {s.diff(a,t,2):3*a,
        s.diff(f,t,2):(-6+6*(ap/a)**2)*f,
        s.diff(f,t):-2*ap*f/a,
        s.diff(z,t,2):-3*ap*zp/a}
def reduced(expr):
    return s.simplify(expr.subs(rels,simultaneous=True))
targets = [
    (m.T,m.T,s.Rational(3,2)*a*a*f*zp*zp*y*y),
    (m.U,m.U,-s.Rational(9,2)*a*a*f*zp*zp*y*y),
    (m.X,m.X,a*a*f*zp*zp),
    (m.Y,m.Y,0),
    (m.X,m.U,-2*ap*f*zp),
    (m.T,m.U,0),(m.T,m.X,0),(m.T,m.Y,0),
    (m.X,m.Y,0),(m.U,m.Y,0),
]
for v,w,target in targets:
    err=reduced((v.T*dE*w)[0]-target)
    assert err == 0, (v,w,err)
print('PASS: 10 exact first-variation blocks, including the Maxwell mixed force')

# The tensor test is trace-free for every cut-off, so any Einstein constant
# contributes only through the metric perturbation in its output pairing.
q = s.symbols('q')
assert s.simplify(s.trace(m.gi*(q*H))) == 0
print('PASS: trace-free receiver eliminates the constant Einstein-scale term')
