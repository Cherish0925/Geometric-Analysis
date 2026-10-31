"""Exact local algebra for the whole-fibre critical-scale receiver theorem.

This checks identities, not compactness or the infinite-volume gauge proof.
Run: python round5_construction_check.py
"""
import sympy as s


def connection(metric, coords):
    inverse = metric.inv()
    n = len(coords)
    gamma = {}
    for k in range(n):
        for i in range(n):
            for j in range(n):
                gamma[k, i, j] = s.simplify(sum(
                    inverse[k, a] * (
                        s.diff(metric[j, a], coords[i])
                        + s.diff(metric[i, a], coords[j])
                        - s.diff(metric[i, j], coords[a])) / 2
                    for a in range(n)))
    return inverse, gamma


def ricci_component(gamma, coords, i, j):
    n = len(coords)
    return s.simplify(sum(
        s.diff(gamma[k, i, j], coords[k])
        - s.diff(gamma[k, i, k], coords[j])
        + sum(gamma[k, k, a] * gamma[a, i, j]
              - gamma[k, j, a] * gamma[a, i, k]
              for a in range(n))
        for k in range(n)))


# The fibre has arbitrary (t,u)-dependent anisotropy and off-diagonal shear.
# Its determinant is exactly one; no fibre constant-curvature assumption is used.
t, y, u, x = s.symbols('t y u x', real=True)
a = s.Function('a')(t, u)
c = s.Function('c')(t, u)
b = s.Function('b', positive=True)(t)
h = s.Matrix([[s.exp(2*a)+s.exp(-2*a)*c*c, s.exp(-2*a)*c],
              [s.exp(-2*a)*c, s.exp(-2*a)]])
assert s.simplify(h.det()) == 1
metric = s.diag(1, b*b, 1, 1)
metric[2:4, 2:4] = h
inverse, gamma = connection(metric, (t, y, u, x))
shape = h.inv() * h.diff(t) / 2
stress = s.simplify(s.trace(shape*shape))
assert s.simplify(stress - 2*s.diff(a,t)**2
                  - s.exp(-4*a)*s.diff(c,t)**2/2) == 0
assert s.simplify(ricci_component(gamma, (t,y,u,x), 0, 0)
                  + s.diff(b,t,2)/b + stress) == 0
assert s.simplify(ricci_component(gamma, (t,y,u,x), 1, 1)
                  + b*s.diff(b,t,2)) == 0
assert ricci_component(gamma, (t,y,u,x), 0, 1) == 0
print('PASS: full horizontal Ricci stress for an arbitrary determinant-one fibre matrix')


# Surface calculation on a hyperbolic cusp chart, with unrestricted components.
r, z = s.symbols('r z', real=True)
coords = (r, z)
surface = s.diag(1, s.exp(2*r))
si, sg = connection(surface, coords)
A, B = s.Function('A')(r,z), s.Function('B')(r,z)
k = s.Matrix([[A, s.exp(r)*B], [s.exp(r)*B, -s.exp(2*r)*A]])


def derivative_two(tensor):
    return {(ell,i,j): s.simplify(s.diff(tensor[i,j],coords[ell])
              - sum(sg[p,ell,i]*tensor[p,j]+sg[p,ell,j]*tensor[i,p]
                    for p in range(2)))
            for ell in range(2) for i in range(2) for j in range(2)}


def divergence_two(tensor):
    first = derivative_two(tensor)
    return s.Matrix([-s.simplify(sum(si[i,j]*first[i,j,k0]
                                      for i in range(2) for j in range(2)))
                     for k0 in range(2)])


def tf_sym_derivative(oneform):
    derivative = s.Matrix(2,2,lambda i,j:
        s.diff(oneform[j],coords[i])
        - sum(sg[p,i,j]*oneform[p] for p in range(2)))
    div = -s.trace(si*derivative)
    return ((derivative+derivative.T)/2 + div*surface/2).applyfunc(s.simplify)


first = derivative_two(k)
rough = s.zeros(2)
for i in range(2):
    for j in range(2):
        rough[i,j] = s.simplify(-sum(si[ell,m]*(
            s.diff(first[m,i,j],coords[ell])
            - sum(sg[p,ell,m]*first[p,i,j]
                  + sg[p,ell,i]*first[m,p,j]
                  + sg[p,ell,j]*first[m,i,p]
                  for p in range(2)))
            for ell in range(2) for m in range(2)))
surface_einstein = rough - 2*k
two_p_delta = 2*tf_sym_derivative(divergence_two(k))
assert (surface_einstein-two_p_delta).applyfunc(s.simplify) == s.zeros(2)
print('PASS: Delta_E = 2 P delta on all trace-free hyperbolic surface tensors')

v0,v1=s.Function('v0')(r,z),s.Function('v1')(r,z)
v=s.Matrix([v0,s.exp(r)*v1])
dv={(ell,i):s.diff(v[i],coords[ell])-sum(sg[p,ell,i]*v[p]
                    for p in range(2))
    for ell in range(2) for i in range(2)}
rough_v=s.Matrix([-s.simplify(sum(si[ell,m]*(
    s.diff(dv[m,i],coords[ell])-sum(sg[p,ell,m]*dv[p,i]
                               +sg[p,ell,i]*dv[m,p] for p in range(2)))
    for ell in range(2) for m in range(2))) for i in range(2)])
assert (2*divergence_two(tf_sym_derivative(v))-rough_v-v).applyfunc(s.simplify)==s.zeros(2,1)
print('PASS: delta P = (Delta_H+2)/2, including the curvature shift')


f=s.sech(t)**2
J=s.atan(s.sinh(t))
P=lambda w:s.diff(w,t,2)+s.tanh(t)*s.diff(w,t)
assert s.simplify(-P(f)+(2-4*f)*f)==0
assert s.simplify(P(J))==0
vfun=s.Function('v')(t)
assert s.simplify((-P(f*vfun)+(2-4*f)*f*vfun)/f
                  +s.diff(vfun,t,2)-3*s.tanh(t)*s.diff(vfun,t))==0
print('PASS: horizontal positive ground state, finite-measure transform, and transfer primitive')

# Independent matrix expansion for the fibre path exp(s H).
aa,bb,ap,bp,ss=s.symbols('aa bb ap bp ss',real=True)
H=s.Matrix([[aa,bb],[bb,-aa]])
Hp=s.Matrix([[ap,bp],[bp,-ap]])
hs=s.eye(2)+ss*H+ss**2*H*H/2
hs_inv=s.eye(2)-ss*H+ss**2*H*H/2
hs_t=ss*Hp+ss**2*(Hp*H+H*Hp)/2
S=hs_inv*hs_t/2
coefficient=s.expand(s.trace(S*S)).coeff(ss,2)
assert s.simplify(coefficient-s.trace(Hp*Hp)/4)==0
sech3=s.sqrt(s.pi)*s.gamma(s.Rational(3,2))/s.gamma(2)
assert s.simplify(-sech3/4+s.pi/8)==0
print('PASS: affine quadratic receiver coefficient is -pi ||B||_L2^2 / 8')

# Tail estimates used for the receiver measure, not ordinary total volume.
T,R,eps=s.symbols('T R eps',positive=True)
assert s.simplify((s.diff(2*s.atan(s.exp(t)),t)-s.sech(t)).rewrite(s.exp))==0
assert s.simplify(eps*s.integrate(s.cosh(u),(u,-R,R))-2*eps*s.sinh(R))==0
print('PASS: normalized receiver has sech(t) base density and explicit collar area tails')
