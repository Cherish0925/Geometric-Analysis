# Referee check of Lemma lem:weylgauge (sec3) -- independent derivation
import sympy as sp, itertools, random
n=4
x=sp.symbols('x1:5',real=True)
J=sp.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])   # J e1=e2, J e3=e4 ; (Jx)_i=J_ij x_j
assert J*J==-sp.eye(4)
d=lambda i,j: 1 if i==j else 0
R1={};B={}
for i,k,j,l in itertools.product(range(n),repeat=4):
    R1[i,k,j,l]=d(i,j)*d(k,l)-d(i,l)*d(j,k)
    B[i,k,j,l]=J[i,j]*J[k,l]-J[i,l]*J[k,j]+2*J[i,k]*J[j,l]
Rs={key:sp.Rational(5,12)*R1[key]-sp.Rational(1,12)*B[key] for key in R1}

def check_sym(R,name):
    ok=True
    for i,k,j,l in itertools.product(range(n),repeat=4):
        ok&= (R[i,k,j,l]==-R[k,i,j,l]) and (R[i,k,j,l]==-R[i,k,l,j]) and (R[i,k,j,l]==R[j,l,i,k])
        # first Bianchi: cyclic in (k,j,l) with i fixed, tensor R(e_i,e_k,e_j,e_l)
        ok&= (R[i,k,j,l]+R[i,j,l,k]+R[i,l,k,j]==0)
    print(name,"curvature symmetries + first Bianchi:",ok)
for R,nm in ((R1,'R1'),(B,'B'),(Rs,'R*')): check_sym(R,nm)
ric=lambda R: sp.Matrix(n,n,lambda i,j: sum(R[i,k,j,k] for k in range(n)))
print("Ric(R1)=",ric(R1).tolist()); print("Ric(B)=",ric(B).tolist()); print("Ric(R*)=",ric(Rs).tolist())

# H_* as a matrix of coefficients
X=sp.Matrix(x); r2=sum(t**2 for t in x); JX=J*X
Hstar=-sp.Rational(5,36)*(r2*sp.eye(4)-X*X.T)+sp.Rational(1,12)*JX*JX.T
HR=lambda R: sp.Matrix(n,n,lambda i,j: -sp.Rational(1,3)*sum(R[i,k,j,l]*x[k]*x[l] for k in range(n) for l in range(n)))
print("H_* == -1/3 R* x x :", sp.simplify(Hstar-HR(Rs))==sp.zeros(4))
print("B x x == 3 Jx Jx^T :", sp.simplify(sp.Matrix(n,n,lambda i,j: sum(B[i,k,j,l]*x[k]*x[l] for k in range(n) for l in range(n)))-3*JX*JX.T)==sp.zeros(4))

def DRic(h):
    lap=lambda f: sum(sp.diff(f,t,2) for t in x)
    div=[sum(sp.diff(h[i,j],x[i]) for i in range(n)) for j in range(n)]
    tr=sum(h[i,i] for i in range(n))
    return sp.Matrix(n,n,lambda i,j: sp.Rational(1,2)*(-lap(h[i,j])+sp.diff(div[j],x[i])+sp.diff(div[i],x[j])-sp.diff(tr,x[i],x[j])))
print("DRic_e(H_*) =",sp.simplify(DRic(Hstar)).tolist())

# random algebraic curvature tensor: R = sum of Kulkarni-Nomizu products of random symmetric matrices (spans all)
def KN(a,b):
    return {(i,k,j,l): a[i,j]*b[k,l]+a[k,l]*b[i,j]-a[i,l]*b[k,j]-a[k,j]*b[i,l] for i,k,j,l in itertools.product(range(n),repeat=4)}
random.seed(1)
def rsym():
    m=sp.Matrix(n,n,lambda i,j: random.randint(-5,5)); return m+m.T
R={key:0 for key in R1}
for _ in range(12):
    t=KN(rsym(),rsym())
    for key in R: R[key]+=t[key]
check_sym(R,'random R')
H=HR(R)
print("DRic_e(H_R)-Ric(R) =",sp.simplify(DRic(H)-ric(R)).tolist())
print("H_R(x,.)=",sp.simplify(H*X).T.tolist())
lapH=sp.Matrix(n,n,lambda i,j: sum(sp.diff(H[i,j],t,2) for t in x))
print("Lap H_R + 2/3 Ric =",sp.simplify(lapH+sp.Rational(2,3)*ric(R)).tolist())
# Weyl part of random R  (n=4): W = R - (1/(n-2)) KN(Ric0,g)/... use standard decomposition
g=sp.eye(4); Rc=ric(R); s=Rc.trace()
P=(Rc-s*g/(2*(n-1)))/(n-2)      # Schouten
PK=KN(P,g)                        # with our KN normalisation: KN(P,g)_{ikjl}=P_ij g_kl + P_kl g_ij - P_il g_kj - P_kj g_il
W={key:R[key]-PK[key] for key in R}
check_sym(W,'Weyl(R)')
print("Ric(W)=",ric(W).tolist())
K=HR(W)
print("tr K=",sp.simplify(K.trace()),"; div K=",[sp.simplify(sum(sp.diff(K[i,j],x[i]) for i in range(n))) for j in range(n)],
      "; Lap K=",sp.simplify(sp.Matrix(n,n,lambda i,j: sum(sp.diff(K[i,j],t,2) for t in x))).tolist(),"; K(x,.)=",sp.simplify(K*X).T.tolist())

# curvature operator on 2-forms, convention  Rop(e_i^e_k) = 1/2 sum R_{ikjl} e_j^e_l  (sphere: identity)
pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
def Rop(R): return sp.Matrix(6,6,lambda a,b: R[pairs[a][0],pairs[a][1],pairs[b][0],pairs[b][1]])
# Hodge star for orientation e1^e2^e3^e4
star=sp.zeros(6)
for a,(i,k) in enumerate(pairs):
    rest=[m for m in range(4) if m not in (i,k)]
    sign=sp.LeviCivita(i,k,rest[0],rest[1]); star[pairs.index(tuple(rest)),a]=sign
Pp=(sp.eye(6)+star)/2
omega=sp.Matrix([1,0,0,0,0,1])  # e12+e34 = omega_J (self-dual for the complex orientation)
print("star omega_J == omega_J:", star*omega==omega)
s_star=ric(Rs).trace()
Wstar={key:Rs[key]-sp.Rational(s_star,12)*R1[key] for key in Rs}
print("scal(R*)=",s_star,"; Weyl(R*) == -(1/12)(B-R1):",all(Wstar[key]==-sp.Rational(1,12)*(B[key]-R1[key]) for key in Rs), "; Ric(W*)=",ric(Wstar).tolist())
Wop=Rop(Wstar)
print("W+ block eigen:", (Pp*Wop*Pp).eigenvals(), " W- block eigen:", ((sp.eye(6)-Pp)*Wop*(sp.eye(6)-Pp)).eigenvals())
print("W*(omega_J) =",(Wop*omega).T.tolist(),"  => eigenvalue", (Wop*omega)[0], " ; -s/12 =",-sp.Rational(s_star,12))
print("R*_op(omega_J) = (W+ + s/12) omega_J =",(Rop(Rs)*omega).T.tolist())
