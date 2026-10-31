"""Exact coordinate verification for the translation-invariant GH zero-locus test.
No Einstein equation is inserted: Ricci is computed from the displayed metric.
"""
import sympy as S
w,v,a,b,c,d=S.symbols('w v a b c d', real=True)
g=S.Matrix([[w,0,0,0],[0,w,0,0],[0,0,w+v*v/w,v/w],[0,0,v/w,1/w]])
gi=S.simplify(g.inv())

def D(f,k):
    if k==0:return S.diff(f,w)*a-S.diff(f,v)*b+S.diff(f,a)*c+S.diff(f,b)*d
    if k==1:return S.diff(f,w)*b+S.diff(f,v)*a+S.diff(f,a)*d-S.diff(f,b)*c
    return S.S(0)

G=[[[S.factor(sum(gi[l,h]*(D(g[h,j],i)+D(g[h,i],j)-D(g[i,j],h))/2 for h in range(4))) for j in range(4)]for i in range(4)]for l in range(4)]
Ric=S.Matrix(4,4,lambda i,j:S.factor(sum(D(G[k][i][j],k)-D(G[k][i][k],j)+sum(G[k][k][l]*G[l][i][j]-G[k][j][l]*G[l][i][k] for l in range(4)) for k in range(4))))
assert Ric==S.zeros(4),Ric
O=S.zeros(4);O[0,1]=w;O[1,0]=-w;O[2,3]=-1;O[3,2]=1
T=[S.Matrix(4,4,lambda i,j:S.factor(D(O[i,j],k)-sum(G[h][k][i]*O[h,j]+G[h][k][j]*O[i,h] for h in range(4)))) for k in range(4)]
q=S.factor(sum(gi[k,l]*gi[i,p]*gi[j,r]*T[k][i,j]*T[l][p,r]/2 for k in range(4) for l in range(4) for i in range(4) for j in range(4) for p in range(4) for r in range(4)))
assert S.simplify(q-4*(a*a+b*b)/w**3)==0,q
assert S.factor((gi*O)**2+S.eye(4))==S.zeros(4)
for i in range(4):
 for j in range(4):
  for k in range(4):assert S.simplify(D(O[j,k],i)+D(O[k,i],j)+D(O[i,j],k))==0
print('PASS: Ric=0; J^2=-Id; dOmega=0; |nabla Omega|^2=4(a^2+b^2)/w^3.')
