"""Exact rational check of the invariant nodal quintic used in Q3 boundary analysis."""
import itertools
import sympy as s
x = s.symbols('x1:5')
E = [e for e in itertools.product(range(6), repeat=4)
     if sum(e)==5 and sum((i+1)*e[i] for i in range(4))%5==0 and max(e)<5]
assert len(E)==8
F = 2*sum(t**5 for t in x)-sum(s.prod(t**a for t,a in zip(x,e)) for e in E)
dF = [s.diff(F,t) for t in x]
one=dict.fromkeys(x,1)
assert F.subs(one)==0 and all(f.subs(one)==0 for f in dF)
H=s.hessian(F,x).subs(one)
assert H==40*s.eye(4)-10*s.ones(4)
assert H.rank()==3
G=s.groebner([f.subs(x[3],1) for f in dF],*x[:3],order='grevlex').fglm('lex')
assert [f.as_expr() for f in G.polys]==[x[0]-x[2]**3,x[1]-x[2]**2,x[2]**5-1]
for k in range(3):
    v=[t for t in x[:3] if t!=x[k]]
    Gi=s.groebner([f.subs(x[3],0).subs(x[k],1) for f in dF],*v)
    assert [f.as_expr() for f in Gi.polys]==[1]
for r in range(1,10):
    Q=-2*s.eye(r);Q[0,0]=-3
    for i in range(r-1): Q[i,i+1]=Q[i+1,i]=1
    assert -Q.inv()[0,0]==s.Rational(r,2*r+1)
print('All exact nodal-quintic and chain-charge checks passed.')
print('F =', F)
print('Affine singular ideal:', G)
print('Projective Hessian nonzero eigenvalues:', {k:v for k,v in H.eigenvals().items() if k!=0})
