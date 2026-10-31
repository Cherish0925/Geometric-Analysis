"""Exact U(2) linear algebra for divergence of a Kähler-type self-dual Weyl tensor.

At one Euclidean oriented four-frame let {n1,n2,n3} be the orthonormal
self-dual basis and
    W0 = a (I_{Lambda+}/3 - n1 tensor n1).
We compute delta W0 as a map of da and nabla n1.  We then restrict nabla n1
to the almost-Kähler first-jet condition d(sqrt(2)n1)=0 and calculate exact
Gram matrices/singular values.  Tensor norms use |2-form|^2=(1/2)F_ij F_ij
and |delta W|^2=sum_{j,k<l}(delta W)_{jkl}^2.
"""
from pathlib import Path
import json
import sympy as s

rt2=s.sqrt(2)
# components of orthonormal self-dual forms n_r = omega_r/sqrt(2)
def form(pairs):
    A=s.zeros(4,4)
    for i,j,val in pairs:
        A[i,j]=s.Rational(val,1)/rt2
        A[j,i]=-s.Rational(val,1)/rt2
    return A
n=[
    form([(0,1,1),(2,3,1)]),
    form([(0,2,1),(3,1,1)]), # e02 + e31 = e02-e13
    form([(0,3,1),(1,2,1)]),
]
# verify orthonormality in 2-form norm
Gforms=s.Matrix([[s.simplify(sum(n[r][i,j]*n[t][i,j] for i in range(4) for j in range(4))/2) for t in range(3)] for r in range(3)])

# variables: da_p then x_{p,2},x_{p,3} where nabla_p n1=xp2*n2+xp3*n3
da=s.symbols('d0:4')
x2=s.symbols('x20:24')
x3=s.symbols('x30:34')
vars_all=list(da)+list(x2)+list(x3)

# d n1 closure: cyclic derivative for triples i<j<k
closure=[]
for i in range(4):
  for j in range(i+1,4):
    for k in range(j+1,4):
      def dn(p,q,r):
        return x2[p]*n[1][q,r]+x3[p]*n[2][q,r]
      closure.append(s.simplify(dn(i,j,k)+dn(j,k,i)+dn(k,i,j)))
Cclose=s.zeros(4,8)
xvars=list(x2)+list(x3)
for r,e in enumerate(closure):
    for c,v in enumerate(xvars): Cclose[r,c]=s.diff(e,v)
N=s.Matrix.hstack(*Cclose.nullspace()) # 8 x 4, AK torsion coordinates

# derivative d_p W0_{ij kl}. I/3 derivative zero; K components not needed for da term:
# K= I/3 - n1 otimes n1; I on Lambda+ has components sum_r nr_ij nr_kl.
def Kcomp(i,j,k,l):
    return s.simplify(sum(nr[i,j]*nr[k,l] for nr in n)/3 - n[0][i,j]*n[0][k,l])
def dW(p,i,j,k,l):
    dncomp=lambda q,r: x2[p]*n[1][q,r]+x3[p]*n[2][q,r]
    return s.simplify(da[p]*Kcomp(i,j,k,l) - (dncomp(i,j)*n[0][k,l]+n[0][i,j]*dncomp(k,l)))
# delta W_{jkl}=-nabla_i W_{ij kl}, store k<l (24 components)
C=[]
for j in range(4):
  for k in range(4):
    for l in range(k+1,4):
      C.append(s.simplify(-sum(dW(i,i,j,k,l) for i in range(4))))
M=s.zeros(len(C),len(vars_all))
for r,e in enumerate(C):
    for c,v in enumerate(vars_all): M[r,c]=s.diff(e,v)
Mda=M[:,:4]
Mx=M[:,4:]
Mak=s.simplify(Mx*N)

# Gram forms. Coordinates y in the nullspace N; physical |nabla n|^2=x^T x.
Qn=s.simplify(N.T*N)
Qc=s.simplify(Mak.T*Mak)
Qda=s.simplify(Mda.T*Mda)
Qcross=s.simplify(Mda.T*Mak)
# generalized eigenvalues Qc y=lambda Qn y
lam=s.factor((Qc-s.symbols('lam')*Qn).det())
# whitening isn't needed: solve determinant and record.
eigs=s.solve(s.Eq(lam,0),s.symbols('lam'))

# Also calculate the exact bilinear identity: if cross vanishes and Qc=lambda Qn,
# |delta W0|^2=lambda a^2 |nabla n|^2 + da quadratic (we computed at a=1).
result={
  'self_dual_basis_gram': [[str(s.simplify(z)) for z in row] for row in Gforms.tolist()],
  'closure_matrix_rank': int(Cclose.rank()),
  'closure_nullspace_N': [[str(s.simplify(z)) for z in row] for row in N.tolist()],
  'torsion_metric_Qn': [[str(s.simplify(z)) for z in row] for row in Qn.tolist()],
  'divergence_torsion_Qc': [[str(s.simplify(z)) for z in row] for row in Qc.tolist()],
  'divergence_amplitude_Qda': [[str(s.simplify(z)) for z in row] for row in Qda.tolist()],
  'amplitude_torsion_cross': [[str(s.simplify(z)) for z in row] for row in Qcross.tolist()],
  'generalized_characteristic': str(lam),
  'generalized_eigenvalues': [str(s.simplify(z)) for z in eigs],
  'ranks': {'M_all':int(M.rank()),'M_da':int(Mda.rank()),'M_AK_torsion':int(Mak.rank())},
  'interpretation': 'All identities are pointwise at a=1. Restore amplitude by multiplying the torsion contribution by a. Check tensor normalization before importing constants into another convention.'
}
out=Path(__file__).resolve().parents[1]/'data'/'step43_w0_divergence_symbol.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
