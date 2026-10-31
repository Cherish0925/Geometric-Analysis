"""Independent Koszul verification of the system A01 Bianchi VIII pair.
Run: python Q4_independent_cartan.py
Dependency: SymPy. All asserted identities are exact rational identities.
The explicit model is inherited; this program derives full curvature from brackets.
"""
import sympy as s
x=s.symbols('x');D=1+3*x*x
v2=(1-x*x)**2*(9*x*x-1)/(4*D)
ell=-2*x/(1-x*x)+9*x/(9*x*x-1)-3*x/D
H=[s.Rational(1,2)*(3/(3*x-1)+6*x/D+1/(1-x)-2/(1+x)),s.Rational(1,2)*(3/(3*x+1)+6*x/D+2/(1-x)-1/(1+x)),1/x+x/(1-x*x)-3*x/D]
V=[-D/(4*x*(1+x)*(3*x+1)),D/(4*x*(1-x)*(3*x-1)),12*x/((9*x*x-1)*D)]
C=s.MutableDenseNDimArray.zeros(4,4,4)
for i in range(1,4): C[0,i,i]=-H[i-1];C[i,0,i]=H[i-1]
for i,j,k in [(1,2,3),(2,3,1),(3,1,2)]:C[j,k,i]=-2*V[i-1];C[k,j,i]=2*V[i-1]
# connection divided by v, nabla_a E_b = v G[a,b,c] E_c
G=s.MutableDenseNDimArray.zeros(4,4,4)
for a in range(4):
 for b in range(4):
  for c in range(4):G[a,b,c]=s.factor((C[a,b,c]-C[b,c,a]+C[c,a,b])/2)
def R(a,b,c,d):
 t=(s.diff(G[b,c,d],x)+ell*G[b,c,d] if a==0 else 0)-(s.diff(G[a,c,d],x)+ell*G[a,c,d] if b==0 else 0)
 for e in range(4):t+=G[b,c,e]*G[a,e,d]-G[a,c,e]*G[b,e,d]-C[a,b,e]*G[e,c,d]
 return s.factor(v2*t)
print('Ricci independent Koszul:')
for b in range(4):print([s.factor(sum(R(a,b,c,a) for a in range(4))) for c in range(4)])
pairs=[[(0,1),(2,3)],[(0,2),(3,1)],[(0,3),(1,2)]]
def block(sign1,sign2):
 A=s.zeros(3)
 for i in range(3):
  for j in range(3):
   value=0
   for m,(a,b) in enumerate(pairs[i]):
    for n,(c,d) in enumerate(pairs[j]):value+=sign1**m*sign2**n*R(a,b,d,c)/2
   A[i,j]=s.factor(value)
 return A
print('Rminus',block(-1,-1));print('mixed',block(1,-1));print('Rplus',block(1,1))
f1,f2=s.symbols('f1 f2');X1=(1-x)**3*(3*x+1)/(16*x**3);X2=(1+x)**3*(3*x-1)/(16*x**3)
O=s.zeros(4)
for (a,b),f in [((0,1),f1),((2,3),f1),((0,2),f2),((3,1),f2)]:O[a,b]=f;O[b,a]=-f
DO=s.MutableDenseNDimArray.zeros(4,4,4)
for a in range(4):
 for b in range(4):
  for c in range(4):
   val=0
   if a==0:val=s.diff(O[b,c],f1)*f1*s.diff(X1,x)/(2*X1)+s.diff(O[b,c],f2)*f2*s.diff(X2,x)/(2*X2)
   val-=sum(G[a,b,e]*O[e,c]+G[a,c,e]*O[b,e] for e in range(4))
   DO[a,b,c]=s.factor(val)
print('closed', [s.factor(DO[a,b,c]+DO[b,c,a]+DO[c,a,b]) for a,b,c in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]])
q=s.factor(v2*sum(DO[a,b,c]**2 for a in range(4) for b in range(4) for c in range(b+1,4)))
q=s.factor(s.expand(q).coeff(f1,2)*X1+s.expand(q).coeff(f2,2)*X2+s.expand(q).coeff(f1,1).coeff(f2,1)*f1*f2)
print('q',q)
assert all(s.factor(sum(R(a,b,c,a) for a in range(4)) + (3 if b==c else 0)) == 0 for b in range(4) for c in range(4))
assert block(-1,-1) == -s.eye(3)
assert block(1,-1) == s.zeros(3)
assert all(s.factor(DO[a,b,c]+DO[b,c,a]+DO[c,a,b]) == 0 for a,b,c in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)])
assert s.factor(X1+X2-1)==0
assert s.factor(q-36*(1-x*x)**3/D**3)==0
W=block(1,1)+s.eye(3)
wnorm=s.factor(s.trace(W*W))
assert wnorm.subs(x,s.Rational(1,3))==s.Rational(2,3)
assert wnorm.subs(x,1)==6
print('Weyl operator norm squared:',wnorm)
print('All exact curvature, closure, and torsion checks passed.')
