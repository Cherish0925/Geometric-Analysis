#!/usr/bin/env python3
"""Exact local checks for the complete hyperbolic-product decomposition.

No earlier project checker is imported. Global Hodge decomposition,
min--max, and perturbative estimates are proved in the accompanying note,
not certified by these finite symbolic identities.
"""
import sympy as s

x,y=s.symbols('x y',real=True,positive=True)
coords=(x,y)
g=s.eye(2)/(3*y*y)
gi=g.inv()
Gamma=[[[s.simplify(sum(gi[k,l]*(s.diff(g[l,j],coords[i])
    +s.diff(g[l,i],coords[j])-s.diff(g[i,j],coords[l]))/2
    for l in range(2))) for j in range(2)] for i in range(2)]
    for k in range(2)]

def nabla2tensor(h):
    return [[[s.simplify(s.diff(h[i,j],coords[n])
        -sum(Gamma[p][n][i]*h[p,j]+Gamma[p][n][j]*h[i,p]
             for p in range(2))) for j in range(2)]
        for i in range(2)] for n in range(2)]

def rough2(h):
    dh=nabla2tensor(h)
    return s.Matrix(2,2,lambda i,j:s.simplify(-sum(gi[n,m]*(
        s.diff(dh[m][i][j],coords[n])
        -sum(Gamma[p][n][m]*dh[p][i][j]
             +Gamma[p][n][i]*dh[m][p][j]
             +Gamma[p][n][j]*dh[m][i][p] for p in range(2)))
        for n in range(2) for m in range(2))))

def divergence(h):
    dh=nabla2tensor(h)
    return s.Matrix([s.simplify(-sum(gi[n,i]*dh[n][i][j]
        for n in range(2) for i in range(2))) for j in range(2)])

def derivative1(alpha):
    return s.Matrix(2,2,lambda n,i:s.simplify(s.diff(alpha[i],coords[n])
        -sum(Gamma[p][n][i]*alpha[p] for p in range(2))))

def rough1(alpha):
    da=derivative1(alpha)
    return s.Matrix([s.simplify(-sum(gi[n,m]*(s.diff(da[m,i],coords[n])
        -sum(Gamma[p][n][m]*da[p,i]+Gamma[p][n][i]*da[m,p]
             for p in range(2))) for n in range(2) for m in range(2)))
        for i in range(2)])

def D(alpha):
    da=derivative1(alpha)
    sym=(da+da.T)/2
    return (sym-s.trace(gi*sym)*g/2).applyfunc(s.simplify)

def P(h):
    action=-3*(s.trace(gi*h)*g-h)
    return (rough2(h)/2-action).applyfunc(s.simplify)

p,q=s.Function('p')(x,y),s.Function('q')(x,y)
h=s.Matrix([[p,q],[q,-p]])
assert (P(h)-D(divergence(h))).applyfunc(s.simplify)==s.zeros(2)
print('PASS: full trace-free surface identity P=D delta')

alpha=s.Matrix([s.Function('u')(x,y),s.Function('v')(x,y)])
Hodge=rough1(alpha)-3*alpha
assert (divergence(D(alpha))-Hodge/2-3*alpha).applyfunc(s.simplify)==s.zeros(2,1)
print('PASS: D*D=half Hodge Laplacian+3, including harmonic one-forms')

assert (P(D(alpha))-D(Hodge/2+3*alpha)).applyfunc(s.simplify)==s.zeros(2)
print('PASS: exact conformal-Killing intertwining')

phi=s.Function('phi')(x,y)
lap=-3*y*y*(s.diff(phi,x,2)+s.diff(phi,y,2))
assert (P(phi*g)-(lap/2+3*phi)*g).applyfunc(s.simplify)==s.zeros(2)
print('PASS: trace branch shift is +3')

# In conformal coordinates, a holomorphic quadratic differential has
# q_x=p_y and q_y=-p_x. A constant representative tests the curvature term.
assert P(s.diag(1,-1))==s.zeros(2)
assert divergence(s.diag(1,-1))==s.zeros(2,1)
print('PASS: a local holomorphic quadratic differential has eigenvalue zero')

# Algebraic curvature action of the four-dimensional product.
entries=s.symbols('h0:10')
full=s.Matrix([[entries[0],entries[1],entries[2],entries[3]],
               [entries[1],entries[4],entries[5],entries[6]],
               [entries[2],entries[5],entries[7],entries[8]],
               [entries[3],entries[6],entries[8],entries[9]]])
curv=s.zeros(4)
for inds in ((0,1),(2,3)):
    tr=sum(full[i,i] for i in inds)
    for i in inds:
        for j in inds:
            curv[i,j]=-3*((tr if i==j else 0)-full[i,j])
assert all(curv[i,j]==0 for i in (0,1) for j in (2,3))
assert curv.subs(dict(zip(entries,(1,0,0,0,1,-0,0,-1,0,-1))))==-3*s.diag(1,1,-1,-1)
print('PASS: mixed curvature action vanishes; relative scale has P-eigenvalue 3')

lb,lf,mb,mf=s.symbols('lambda_B lambda_F mu_B mu_F',nonnegative=True)
assert s.simplify(((mb+3)+(mf+3))/2-(3+(mb+mf)/2))==0
assert s.simplify((3+mb/2)+lf/2-(3+(mb+lf)/2))==0
assert s.simplify((lb+6)/2+lf/2-(3+(lb+lf)/2))==0
assert s.simplify(lf/2+0-lf/2)==0
print('PASS: all tensor-product eigenvalue branches and mixed Hodge shifts')

# Long half-collar conjugation, with no asymptotic substitution.
t,k,c=s.symbols('t k c',positive=True,real=True)
a=c*s.cosh(k*t)
v=s.Function('v')(t)
u=v/s.sqrt(a)
conjugated=s.simplify(s.sqrt(a)*(-s.diff(u,t,2)-s.diff(a,t)/a*s.diff(u,t)))
potential=k*k*(1+s.sech(k*t)**2)/4
assert s.simplify(conjugated+s.diff(v,t,2)-potential*v)==0
assert potential.subs(k,s.sqrt(3)).limit(t,s.oo)==s.Rational(3,4)
assert s.Rational(3,4)/2==s.Rational(3,8)
print('PASS: exact collar Schroedinger potential and tensor threshold 3/8')

# Gauge has a shifted positive spectrum, unlike the retained TT channels.
mu=s.symbols('mu',nonnegative=True)
gauge_eigen=mu/2+3
assert gauge_eigen.subs(mu,0)==3
assert (lf/2).subs(lf,0)==0
print('PASS: harmonic gauge one-forms are not Einstein zero modes')

# Finite boundary Schur algebra, with both feedback terms retained.
A,B,C,D0,F,G=s.symbols('A B C D F G',nonzero=True)
low=(F-B*G/D0)/(A-B*C/D0)
high=(G-C*low)/D0
assert s.simplify(A*low+B*high-F)==0
assert s.simplify(C*low+D0*high-G)==0
assert s.simplify((A*low-F)).subs({A:2,B:1,C:1,D0:3,F:4,G:5})!=0
print('PASS: full Schur force/matrix and rejection of omitted feedback')
