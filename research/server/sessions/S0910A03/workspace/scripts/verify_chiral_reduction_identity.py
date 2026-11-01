#!/usr/bin/env python3
"""Symbolically verify the chiral Riccati factorization of rank-one reduction.

For an exact Riemannian Einstein circle metric Ric=-kappa*g, write
 u=d log ell, z=* (ell F), H=nabla u+u⊗u, P=|z|^2 I-z⊗z.
The electric and magnetic Weyl tensors are
 E=kappa I/3-H+P/4,
 B=1/2(sym nabla z+u⊗z+z⊗u-<u,z>I),
where the reduced equations make B symmetric trace-free.
Set a_plus=u-z/2 and a_minus=u+z/2.  Then
 E+B=-(sym nabla a_plus+a_plus⊗a_plus)_0,
 E-B=-(sym nabla a_minus+a_minus⊗a_minus)_0.
This check is purely tensor-algebraic once the vertical/mixed equations hold.
"""
import sympy as s

n=3
kap=s.symbols('kappa')
u=s.Matrix(s.symbols('u0:3'))
z=s.Matrix(s.symbols('z0:3'))
# U is symmetric nabla u; S is symmetric part of nabla z.
U=s.Matrix(3,3,lambda i,j:s.symbols(f'U{min(i,j)}{max(i,j)}'))
S=s.Matrix(3,3,lambda i,j:s.symbols(f'S{min(i,j)}{max(i,j)}'))
I=s.eye(3)
inner=(u.dot(z))
z2=z.dot(z)
H=U+u*u.T
P=z2*I-z*z.T
E=kap*I/3-H+P/4
B=(S+u*z.T+z*u.T-inner*I)/2

# Reduced scalar equations: tr H=kappa+|z|^2/2 and div z=<u,z>.
subs={s.trace(U): kap+z2/2-u.dot(u), s.trace(S): inner}
# SymPy cannot substitute a trace expression directly; impose last diagonal entries.
subs_explicit={
    U[2,2]:kap+z2/2-u.dot(u)-U[0,0]-U[1,1],
    S[2,2]:inner-S[0,0]-S[1,1],
}

def tf(M):
    return s.simplify(M-s.trace(M)*I/3)

ap=u-z/2
am=u+z/2
Nap=U-S/2+ap*ap.T
Nam=U+S/2+am*am.T
lhs_plus=(E+B).subs(subs_explicit)
lhs_minus=(E-B).subs(subs_explicit)
rhs_plus=(-tf(Nap)).subs(subs_explicit)
rhs_minus=(-tf(Nam)).subs(subs_explicit)
Dplus=s.simplify(lhs_plus-rhs_plus)
Dminus=s.simplify(lhs_minus-rhs_minus)
print('trace(E)=',s.simplify(s.trace(E).subs(subs_explicit)))
print('trace(B)=',s.simplify(s.trace(B).subs(subs_explicit)))
print('E+B Riccati residual =')
s.print_latex(Dplus)
print(Dplus)
print('E-B Riccati residual =')
print(Dminus)
assert Dplus==s.zeros(3)
assert Dminus==s.zeros(3)

# Maurer-Cartan relation follows from dz=-2u wedge z.
# In components, da_plus = -.5 dz = u wedge z = a_plus wedge a_minus.
for i in range(3):
    for j in range(i+1,3):
        dz=-2*(u[i]*z[j]-u[j]*z[i])
        da_plus=-s.Rational(1,2)*dz
        wedge=ap[i]*am[j]-ap[j]*am[i]
        assert s.simplify(da_plus-wedge)==0
print('Maurer-Cartan check: da_plus=a_plus∧a_minus, da_minus=-a_plus∧a_minus')

# Trace modes are fixed by the scalar reduced equations but can grow through z.
# tr(S)=<u,z>, tr(U)=kappa+|z|^2/2-|u|^2.
tp=s.simplify(kap+z2/2-u.dot(u)-inner/2+ap.dot(ap))
tm=s.simplify(kap+z2/2-u.dot(u)+inner/2+am.dot(am))
print('trace mode plus =',s.expand(tp))
print('trace mode minus =',s.expand(tm))
assert s.simplify(tp-(kap+s.Rational(3,4)*z2-s.Rational(3,2)*inner))==0
assert s.simplify(tm-(kap+s.Rational(3,4)*z2+s.Rational(3,2)*inner))==0
