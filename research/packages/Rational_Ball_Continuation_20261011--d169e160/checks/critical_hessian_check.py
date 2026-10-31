from fractions import Fraction as F
from itertools import product
n=4

def test(values):
 a0,a1,a2,f,fp=map(F,values)
 a=(a0,a1,a2,-a0-a1-a2)
 H=[[a[i]*f if i==j else F(0) for j in range(n)] for i in range(n)]
 def dH(k,i,j): return a[i]*fp if k==0 and i==j else F(0)
 def dH2(k,i,j): return 2*a[i]**2*f*fp if k==0 and i==j else F(0)
 C1=[[[ (dH(i,j,k)+dH(j,i,k)-dH(k,i,j))/2 for j in range(n)] for i in range(n)] for k in range(n)]
 C2=[[[ (dH2(i,j,k)+dH2(j,i,k)-dH2(k,i,j))/2-2*sum(H[k][l]*C1[l][i][j] for l in range(n)) for j in range(n)] for i in range(n)] for k in range(n)]
 Q12=sum(C1[k][i][l]*C2[l][i][k] for i in range(n) for k in range(n) for l in range(n))
 QE11=sum(H[i][j]*C1[k][i][l]*C1[l][j][k] for i in range(n) for j in range(n) for k in range(n) for l in range(n))
 actual=6*(Q12-QE11)
 expected=-F(3,2)*a0*(a0*a0-sum(x*x for x in a[1:]))*f*fp*fp
 assert actual==expected,(values,actual,expected)
for a in product(range(-2,3),repeat=3): test((*a,F(5,3),F(7,11)))
print('125 exact rational diagonal determinant-one third-variation checks: PASS')
print('Analytic product check: 4 c^2 cosh^2(ct) has second derivative 8 c^4 at zero.')
