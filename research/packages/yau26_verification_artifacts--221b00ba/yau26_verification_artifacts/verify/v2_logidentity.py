# Check DRic_e[eta(log r) K] = -(eta'' + (d+2) eta')/(2 r^2) K  for K_ij = C_ikjl x^k x^l, C an algebraic Weyl tensor, d=4,5
import sympy as sp, itertools, random
def random_weyl(d, seed):
    random.seed(seed)
    # build algebraic curvature tensor from random symmetric matrices via Kulkarni-Nomizu, then remove traces
    def KN(A,B):
        R={}
        for i,j,k,l in itertools.product(range(d),repeat=4):
            R[i,j,k,l]=A[i,k]*B[j,l]+A[j,l]*B[i,k]-A[i,l]*B[j,k]-A[j,k]*B[i,l]
        return R
    R={idx:0 for idx in itertools.product(range(d),repeat=4)}
    for _ in range(3):
        A=sp.Matrix(d,d,lambda i,j: random.randint(-3,3)); A=A+A.T
        B=sp.Matrix(d,d,lambda i,j: random.randint(-3,3)); B=B+B.T
        T=KN(A,B)
        for idx in R: R[idx]+=T[idx]
    # Weyl projection
    Ric=sp.Matrix(d,d,lambda j,l: sum(R[i,j,i,l] for i in range(d)))
    s=Ric.trace()
    g=sp.eye(d)
    P=(Ric-s*g/(2*(d-1)))/(d-2)
    T=KN(P,g)
    W={idx:sp.nsimplify(R[idx]-T[idx]) for idx in R}
    # checks
    assert all(sum(W[i,j,i,l] for i in range(d))==0 for j in range(d) for l in range(d))
    return W
for d in (4,5):
    X=sp.symbols('x0:%d'%d, real=True)
    r=sp.sqrt(sum(x**2 for x in X))
    eta=sp.Function('eta')
    u=sp.log(r)
    W=random_weyl(d,7+d)
    # curvature index convention R_{ikjl} with K_ij = W_{ikjl} x^k x^l (indices: first pair (i,k), second (j,l))
    K=sp.Matrix(d,d,lambda i,j: sum(W[i,k,j,l]*X[k]*X[l] for k in range(d) for l in range(d)))
    k=eta(u)*K
    def DRic(h):
        tr=sum(h[i,i] for i in range(d))
        div=[sum(sp.diff(h[l,j],X[l]) for l in range(d)) for j in range(d)]
        out=sp.zeros(d,d)
        for i in range(d):
            for j in range(d):
                lap=sum(sp.diff(h[i,j],x,2) for x in X)
                out[i,j]=sp.Rational(1,2)*(-lap+sp.diff(div[j],X[i])+sp.diff(div[i],X[j])-sp.diff(tr,X[i],X[j]))
        return out
    lhs=DRic(k)
    e1=sp.diff(eta(u),X[0])  # dummy to get derivative objects
    t=sp.symbols('t')
    etap=sp.Derivative(eta(t),t).subs(t,u); 
    rhs=-(sp.diff(eta(t),t,2).subs(t,u)+(d+2)*sp.diff(eta(t),t).subs(t,u))/(2*r**2)*K
    diff=(lhs-rhs).applyfunc(lambda e: sp.simplify(e.doit()))
    print('d=%d  max residual zero? '%d, all(e==0 for e in diff))
