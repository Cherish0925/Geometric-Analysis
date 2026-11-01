"""Formal polarization of the leading scalar identity about a rank-two zero-surface jet.

This is not by itself a curved tubular theorem.  It asks what the homogeneous
identity predicts in a flat adapted frame for
    f1 = kappa*conjugate(z2)*e1
and the most general degree-two half-twistor term vanishing on {z2=0}.
It records the degree-one coefficient equations, which are candidates for the
first tangential transport constraints and must subsequently be compared with
connection/second-fundamental-form corrections.
"""
from pathlib import Path
import sympy as sp, json

OUT = Path(__file__).resolve().parents[1]/"data"/"step65"
OUT.mkdir(parents=True,exist_ok=True)
# Fix kappa real positive by the residual compatible U(1) frame freedom.
k = sp.symbols('k', positive=True, real=True)
names = ['d','u','v','r'] # d=delta2, u=Q12^1, v=Q12^2, r=Q22^1, t=Q22^2 below
rr = sp.symbols('dr ur vr rr tr', real=True)
ii = sp.symbols('di ui vi ri ti', real=True)
d,u,v,R,T = [rr[j]+sp.I*ii[j] for j in range(5)]
x = sp.symbols('x0:4', real=True)
z=sp.Matrix([x[0]+sp.I*x[1],x[2]+sp.I*x[3]]); w=sp.conjugate(z)
# h=d*w2; g=(k*w2+2u*w1*w2+R*w2^2, 2v*w1*w2+T*w2^2)
h=d*w[1]
g=sp.Matrix([k*w[1]+2*u*w[0]*w[1]+R*w[1]**2,
             2*v*w[0]*w[1]+T*w[1]**2])
f=z*h+g
Dh=sp.Matrix([0,d])
B=sp.Matrix(2,2,lambda a,b: z[a]*Dh[b]+sp.diff(g[a],w[b]) if False else 0)
# SymPy cannot differentiate wrt conjugate expressions; enter D_w g directly.
Dg=sp.Matrix([[2*u*w[1], k+2*u*w[0]+2*R*w[1]],
              [2*v*w[1], 2*v*w[0]+2*T*w[1]]])
B=z*Dh.T+Dg
A=(B-B.T)/2; S=(B+B.T)/2
norm2=lambda M: sp.expand(sum(sp.conjugate(e)*e for e in M))
source=sp.re(sum(sp.conjugate(f[j])*Dh[j] for j in range(2)))
H=sp.expand_complex(sp.expand(norm2(A)-norm2(S)-8*sp.conjugate(h)*h-6*source))
P=sp.Poly(H,*x)
lin=[]
for j in range(4):
 e=[0]*4;e[j]=1
 lin.append(sp.factor(P.coeff_monomial(tuple(e))))
const=sp.factor(P.coeff_monomial((0,0,0,0)))
# Impose v=0, the cone-along-C condition in the flat adapted frame.
subv={rr[2]:0,ii[2]:0}
lin_v0=[sp.factor(q.subs(subv)) for q in lin]
# rank as real-linear equations in real/imaginary d,u,v,R,T.
vars_=list(rr)+list(ii)
J=sp.Matrix(lin).jacobian(vars_)
Jv=sp.Matrix(lin_v0).jacobian([q for j,q in enumerate(vars_) if j not in (2,7)])
out={
 'f1':'k*conjugate(z2)*e1',
 'f2':'z*(d*conjugate(z2))+(2u*conjugate(z1)conjugate(z2)+R*conjugate(z2)^2, 2v*conjugate(z1)conjugate(z2)+T*conjugate(z2)^2)',
 'constant_coefficient':str(const),
 'degree1_coefficients':[str(q) for q in lin],
 'degree1_rank_generic_k':int(J.subs(k,1).rank()),
 'degree1_coefficients_after_v_equals_0':[str(q) for q in lin_v0],
 'degree1_rank_after_v_equals_0':int(Jv.subs(k,1).rank()),
 'interpretation':'Flat principal polarization only; curved tubular connection and second fundamental form terms are not included.'
}
(OUT/'rank2_surface_linearization.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
assert const==0
