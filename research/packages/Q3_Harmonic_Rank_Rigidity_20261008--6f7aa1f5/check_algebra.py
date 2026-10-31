"""Exact tensor-algebra checks for the harmonic-rank rigidity note.

Requires Python 3 and SymPy. Run: python check_algebra.py
The script checks the finite-dimensional curvature identities; the
maximum and zero-set arguments are proved in the accompanying text.
"""
import sympy as s

def skew(i,j):
    M=s.zeros(4);M[i,j]=1;M[j,i]=-1
    return M
P=[skew(0,1)+skew(2,3),skew(0,2)-skew(1,3),skew(0,3)+skew(1,2)]
N=[skew(0,1)-skew(2,3),skew(0,2)+skew(1,3),skew(0,3)-skew(1,2)]
a,b,sc=s.symbols('a b sc',real=True)
w=s.symbols('w0:5');v=s.symbols('v0:5')
Wp=s.Matrix([[w[0],w[2],w[3]],[w[2],w[1],w[4]],[w[3],w[4],-w[0]-w[1]]])
Wm=s.Matrix([[v[0],v[2],v[3]],[v[2],v[1],v[4]],[v[3],v[4],-v[0]-v[1]]])
phi=a*P[0];psi=b*N[0];E=phi*psi;normE=s.trace(E.T*E)
phiW=sum((a*Wp[i,0]*P[i] for i in range(3)),s.zeros(4))
psiW=sum((b*Wm[i,0]*N[i] for i in range(3)),s.zeros(4))
D=s.eye(4)
def R(i,k,j,l):
    WW=sum(Wp[c,d]*P[c][i,k]*P[d][j,l]/2+Wm[c,d]*N[c][i,k]*N[d][j,l]/2 for c in range(3) for d in range(3))
    EE=(E[i,j]*D[k,l]+E[k,l]*D[i,j]-E[i,l]*D[k,j]-E[k,j]*D[i,l])/2
    SS=sc*(D[i,j]*D[k,l]-D[i,l]*D[k,j])/12
    return WW+EE+SS
RmE=s.Matrix(4,4,lambda i,j:sum(R(i,k,j,l)*E[k,l] for k in range(4) for l in range(4)))
target=phiW*psi+phi*psiW-sc*E/12+normE*D/4
assert all(s.expand(z)==0 for z in RmE-target)
assert s.expand(normE-4*a*a*b*b)==0
# Product map Lambda+ x Lambda- -> S^2_0 preserves tensor-product inner product.
for i in range(3):
 for j in range(3):
  for k in range(3):
   for l in range(3):
    z=s.trace((P[i]*N[j]).T*(P[k]*N[l]))-s.trace(P[i].T*P[k])*s.trace(N[j].T*N[l])/4
    assert z==0
print('Exact algebra verified: curvature contraction; product norm; all 81 inner-product basis identities.')
print('Ricci check:',s.Matrix(4,4,lambda i,j:sum(R(i,k,j,k) for k in range(4))) == E+sc*D/4)

# A self-dual tensor contracted with the derivative of a closed ASD
# two-form contributes no extra term to div(phi o psi).
dh = s.symbols("h0:12")
dpsi = [sum((dh[3*i+j]*N[j] for j in range(3)), s.zeros(4))
        for i in range(4)]
closed=[]
for i in range(4):
 for j in range(i+1,4):
  for k in range(j+1,4):
   closed.append(dpsi[i][j,k]+dpsi[j][k,i]+dpsi[k][i,j])
C,_=s.linear_eq_to_matrix(closed,dh)
null=C.nullspace()
for phi_basis in P:
 extra=s.Matrix([sum(phi_basis[i,k]*dpsi[i][k,j]
                     for i in range(4) for k in range(4))
                 for j in range(4)])
 A,_=s.linear_eq_to_matrix(list(extra),dh)
 for u in null:
  assert A*u == s.zeros(4,1)
print("Closed-ASD differentiated contraction verified on its full symbol kernel.")
