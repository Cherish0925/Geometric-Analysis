"""Symbolically derive the charged Koiso separator constraint components.

Coordinates are (s,x,y).  The slice metric is diag(1,M(s)); the Weingarten
endomorphism is [[0,m_b],[m^a,B^a_b]].  We compute
  div W, d tr W,
and compare with the formulas used in Step 94.
"""
import sympy as sp
from pathlib import Path
import json

s=sp.symbols('s', real=True)
a,b,c=sp.Function('a')(s),sp.Function('b')(s),sp.Function('c')(s)
# Keep general symmetric M, then impose det M=1 only in simplification notes.
M=sp.Matrix([[a,b],[b,c]])
Mi=sp.simplify(M.inv())
q=sp.zeros(3);q[0,0]=1;q[1:,1:]=M
qi=sp.simplify(q.inv())
coords=[s,sp.symbols('x'),sp.symbols('y')]
Gamma=[[[0 for j in range(3)] for i in range(3)] for k in range(3)]
for k in range(3):
 for i in range(3):
  for j in range(3):
   val=0
   for l in range(3):
    def d(expr,idx): return sp.diff(expr,s) if idx==0 else 0
    val += qi[k,l]*(d(q[j,l],i)+d(q[i,l],j)-d(q[i,j],l))/2
   Gamma[k][i][j]=sp.simplify(val)

m1,m2=sp.symbols('m1 m2', real=True)
m=sp.Matrix([m1,m2]); mc=Mi*m
B11,B12,B21,B22=[sp.Function(x)(s) for x in ('B11','B12','B21','B22')]
B=sp.Matrix([[B11,B12],[B21,B22]])
W=sp.zeros(3)
W[0,1]=m1;W[0,2]=m2
W[1,0]=mc[0];W[2,0]=mc[1]
W[1:,1:]=B
H=sp.simplify(sp.trace(W))
# Divergence of (1,1) W: nabla_i W^i_j = d_i W^i_j + Gamma^i_{i l}W^l_j-Gamma^l_{ij}W^i_l
div=[]
for j in range(3):
 val=0
 for i in range(3):
  val += sp.diff(W[i,j],s) if i==0 else 0
  for l in range(3):
   val += Gamma[i][i][l]*W[l,j]-Gamma[l][i][j]*W[i,l]
 div.append(sp.simplify(val))

A=sp.simplify(Mi*sp.diff(M,s)/2)
expected_s=sp.simplify(-sp.trace(A*B))
expected_v=[]
for aa in range(2):
 expected_v.append(sp.simplify(sp.trace(A)*m[aa]-(A.T*m)[aa]+(M*A).T[aa,:].dot(mc)))

# Covariant K=qW and divergence as an independent check.
K=sp.simplify(q*W)
divK=[]
for i in range(3):
 val=0
 for j in range(3):
  for k in range(3):
   nab=(sp.diff(K[k,i],s) if j==0 else 0)
   for l in range(3):
    nab-=Gamma[l][j][k]*K[l,i]+Gamma[l][j][i]*K[k,l]
   val+=qi[j,k]*nab
 val-=sp.diff(H,s) if i==0 else 0
 divK.append(sp.simplify(val))

out={
 'H':str(H),
 'divW':[str(x) for x in div],
 'momentum_divK_minus_dH':[str(x) for x in divK],
 'expected_s':str(expected_s),
 'expected_vertical':[str(x) for x in expected_v],
 'residual_s':str(sp.simplify(div[0]-expected_s)),
 'residual_vertical':[str(sp.simplify(div[i+1]-expected_v[i])) for i in range(2)],
 'note':'Under det M=1, tr A=0. For M-self-adjoint B target-normal to M_s, tr(AB)=0; constant m then gives all momentum components zero.'
}
path=Path('workspace/data/step96_symbolic_initial_constraints.json');path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
