"""Exact Cartan verification of the spin-connection formulas used for O11 cells.

For g=dt^2+a^2 sigma1^2+b^2 sigma2^2+c^2 sigma3^2 with
 d sigma_i=2 sigma_j wedge sigma_k and int sigma123=2*pi^2, derive the
Levi-Civita curvature from Cartan's equations.  Verify, as polynomial/rational
identities in first and second radial jets, that for

  u_i = adot_i-(a_j^2+a_k^2-a_i^2)/(a_j a_k),
  H_i = u_i+u_j u_k/2,
  r_i = udot_i/a_i,  v_i=2H_i/(a_j a_k),

one has |Ric^o|^2=sum_i(r_i-v_i)^2 and s=-2 sum_i(r_i+v_i).
It also checks the Chern--Simons derivative Cdot=abc sum r_i v_i for
C=sum u_i^2+u1*u2*u3 and the orbit-volume conversion
P/(8*pi^2)=int abc |Ric^o|^2/4 dt.
"""
import itertools
import sympy as sp

# Work with independent jet symbols.
a,b,c,a1,b1,c1,a2,b2,c2=sp.symbols(
    'a b c a1 b1 c1 a2 b2 c2', positive=True, real=True)
A=[a,b,c]; A1=[a1,b1,c1]; A2=[a2,b2,c2]
idx=range(4)

# de^i in the orthonormal coframe e0=dt, ei=A_i sigma_i.
de={0:{}}
for i in range(3):
    j,k=(i+1)%3,(i+2)%3
    jj,kk=j+1,k+1
    key=(min(jj,kk),max(jj,kk)); sgn=1 if jj<kk else -1
    de[i+1]={(0,i+1):A1[i]/A[i],key:sgn*2*A[i]/(A[j]*A[k])}

def add(u,v,scale=1):
    out=dict(u)
    for key,val in v.items(): out[key]=out.get(key,0)+scale*val
    return out

def wedge11(u,v):
    out={}
    for i,x in u.items():
        for j,y in v.items():
            if i==j: continue
            key=(min(i,j),max(i,j)); sgn=1 if i<j else -1
            out[key]=out.get(key,0)+sgn*x*y
    return out

# Solve de^a=-omega_ab wedge e^b.
G={}; unknown=[]
for i in idx:
    for j in idx:
        if i<j:
            for k in idx:
                z=sp.symbols(f'G{i}{j}{k}')
                G[(i,j,k)]=z; unknown.append(z)

def om(i,j):
    if i==j: return {}
    if i<j: return {k:G[(i,j,k)] for k in idx}
    return {k:-G[(j,i,k)] for k in idx}

eq=[]
for i in idx:
    rhs={}
    for j in idx: rhs=add(rhs,wedge11(om(i,j),{j:1}),-1)
    diff=add(de[i],rhs,-1)
    eq += [sp.expand(diff.get(pair,0)) for pair in itertools.combinations(idx,2)]
sol=sp.solve(eq,unknown,dict=True)[0]

def omv(i,j): return {k:sp.factor(v.subs(sol)) for k,v in om(i,j).items()}

# Total derivative of rational jet functions and exterior derivative of a 1-form.
def Dt(x):
    return (sp.diff(x,a)*a1+sp.diff(x,b)*b1+sp.diff(x,c)*c1+
            sp.diff(x,a1)*a2+sp.diff(x,b1)*b2+sp.diff(x,c1)*c2)

def dform1(u):
    out={}
    for k,x in u.items():
        out=add(out,wedge11({0:Dt(x)},{k:1}))
        if k>0: out=add(out,{pair:x*val for pair,val in de[k].items()})
    return out

Om={}
for i in idx:
    for j in idx:
        if i==j: Om[(i,j)]={}; continue
        cur=dform1(omv(i,j))
        for k in idx: cur=add(cur,wedge11(omv(i,k),omv(k,j)))
        Om[(i,j)]={pair:sp.factor(val) for pair,val in cur.items()}

# For c<d, the coefficient of e^c wedge e^d in Omega_ab is R_abcd.
def R(i,j,k,l):
    if k==l: return sp.Integer(0)
    if k<l: return Om[(i,j)].get((k,l),0)
    return -Om[(i,j)].get((l,k),0)

# Ric_ii=sum_j R_{j i j i}=sum_j K_{ij}; the Cartan convention below is
# checked by the round Euclidean cone a=b=c=t, where all entries vanish.
Ric=[]
for i in idx:
    Ric.append(sp.factor(sum(R(j,i,j,i) for j in idx if j!=i)))
s=sp.factor(sum(Ric))
ric0sq=sp.factor(sum((q-s/4)**2 for q in Ric))

# Spin-connection variables.
gamma=[]; u=[]
for i in range(3):
    j,k=(i+1)%3,(i+2)%3
    ga=(A[j]**2+A[k]**2-A[i]**2)/(A[j]*A[k])
    gamma.append(ga); u.append(sp.factor(A1[i]-ga))
ud=[sp.factor(Dt(q)) for q in u]
H=[sp.factor(u[i]+u[(i+1)%3]*u[(i+2)%3]/2) for i in range(3)]
r=[sp.factor(ud[i]/A[i]) for i in range(3)]
v=[sp.factor(2*H[i]/(A[(i+1)%3]*A[(i+2)%3])) for i in range(3)]
C=sp.factor(sum(q*q for q in u)+u[0]*u[1]*u[2])

checks={
    'flat_Ric00': sp.factor(Ric[0].subs({a:b,b:c,c:sp.Symbol('t',positive=True),a1:1,b1:1,c1:1,a2:0,b2:0,c2:0})),
    'scalar_identity': sp.factor(s+2*sum(r[i]+v[i] for i in range(3))),
    'ric0_identity': sp.factor(ric0sq-sum((r[i]-v[i])**2 for i in range(3))),
    'C_gradient_identity': sp.factor(Dt(C)-2*sum(H[i]*ud[i] for i in range(3))),
    'C_transgression_identity': sp.factor(Dt(C)-a*b*c*sum(r[i]*v[i] for i in range(3))),
    'P_density_conversion': sp.factor(a*b*c*ric0sq/4-sum((A[(i+1)%3]*A[(i+2)%3]/A[i])/4*(ud[i]-2*H[i]/(A[(i+1)%3]*A[(i+2)%3]/A[i]))**2 for i in range(3)))
}
print('connection forms omega_0i:')
for i in range(1,4): print(i,omv(0,i))
print('Ric diagonal:')
for i,q in enumerate(Ric): print(i,sp.factor(q))
print('checks:')
for key,val in checks.items(): print(key,'=',val)
if any(sp.simplify(vv)!=0 for vv in checks.values()):
    raise SystemExit('one or more exact identities failed')
