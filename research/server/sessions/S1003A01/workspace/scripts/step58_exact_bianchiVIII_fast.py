"""Fast exact verification of the explicit rational Bianchi-VIII AKE branch.
Uses a rationalizing auxiliary variable y with
    y^2=(3p-1)(3p+1)(3p^2+1),  1/3<p<1.
All h_i,W_i are rational multiples of y, so every Einstein/closure/torsion
identity reduces in Q(p)[y]/(y^2-D).  Curvature is evaluated by the independent Step-56 Koszul engine at three
rational p-values with algebraic y.  Those exact point checks confirm the
Einstein conventions and sample half-conformal flatness/non-eigenform behavior;
they are not an all-p proof of half-conformal flatness.
"""
import sympy as s, os, sys, json
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
p,y=s.symbols('p y', positive=True)
D=(3*p-1)*(3*p+1)*(3*p**2+1)
# metric coefficients and geodesic derivative d/dt=c(p)y d/dp
G=4*(3*p**2+1)/((1-p)**2*(1+p)**2*(3*p-1)*(3*p+1))
A=[4*(3*p-1)*(3*p**2+1)/(3*(1-p)*(1+p)**2),4*(3*p+1)*(3*p**2+1)/(3*(1-p)**2*(1+p)),64*p**2/((1-p)*(1+p)*(3*p**2+1))]
c=(1-p)*(1+p)/(2*(3*p**2+1))
def red(z):
    z=s.cancel(s.together(z))
    num,den=s.fraction(z)
    # Expressions here have y powers at most modest degree. Reduce numerator and denominator.
    num=s.rem(s.Poly(s.expand(num),y),s.Poly(y**2-D,y)).as_expr()
    den=s.rem(s.Poly(s.expand(den),y),s.Poly(y**2-D,y)).as_expr()
    # rationalize a linear denominator a+b y
    P=s.Poly(den,y); a=P.nth(0); b=P.nth(1)
    if b!=0:
        num=s.expand(num*(a-b*y)); den=s.expand(a*a-b*b*D)
        num=s.rem(s.Poly(num,y),s.Poly(y**2-D,y)).as_expr()
    return s.factor(s.cancel(num/den))
def Dt(z):
    # y'=D'/(2y), then d/dt=c*y*d/dp along y^2=D.
    return red(c*y*(s.diff(z,p)+s.diff(z,y)*s.diff(D,p)/(2*y)))
# h = (1/2)d_t log A.  W signs are (-,+,+).
h=[red(c*y*s.diff(Ai,p)/(2*Ai)) for Ai in A]
W=[-(1-p)*y/(8*p*(3*p+1)),(1+p)*y/(8*p*(3*p-1)),6*p*(1-p)*(1+p)/((3*p**2+1)*y)]
W=[red(z) for z in W]
S=sum(h)
Q=red(h[0]*h[1]+h[0]*h[2]+h[1]*h[2]+sum(z*z for z in W)-2*(W[0]*W[1]+W[0]*W[2]+W[1]*W[2]))
resh=[];resW=[]
for i in range(3):
 j,k=(i+1)%3,(i+2)%3
 resh.append(red(Dt(h[i])-(-h[i]*S+2*(W[i]**2-(W[j]-W[k])**2)+3)))
 resW.append(red(Dt(W[i])-W[i]*(h[i]-h[j]-h[k])))
mu=[red(2*W[i]-h[(i+1)%3]-h[(i+2)%3]) for i in range(3)]
X=[(1-p)**3*(3*p+1)/(16*p**3),(1+p)**3*(3*p-1)/(16*p**3),s.Integer(0)]
resX=[red(Dt(X[i])-2*mu[i]*X[i]) for i in range(2)]
# Direct closure without radicals by squaring is not needed: X propagation plus choose fixed signs
# gives x_i'=mu_i x_i, equivalent to closure. At p=1/2 direct signed square roots are checked below.
b=[h[0]+W[0]-W[1]-W[2],h[1]-W[0]+W[1]-W[2],h[2]-W[0]-W[1]+W[2]]
q=red(2*(sum(X[i]*mu[i]**2 for i in range(3))+(X[0]+X[1])*b[2]**2+(X[0]+X[2])*b[1]**2+(X[1]+X[2])*b[0]**2))
q0=36*(1-p**2)**3/(1+3*p**2)**3
print('Qres',red(Q-3));print('hres',resh);print('Wres',resW);print('Xres',resX);print('unitres',red(X[0]+X[1]-1));print('qres',red(q-q0),flush=True)
assert red(Q-3)==0 and all(z==0 for z in resh+resW+resX) and red(X[0]+X[1]-1)==0 and red(q-q0)==0
# Exact real witness from Spirit: verify every lifted ideal generator and all stated invariants.
import step57_classA_metric_only as M
wv=[-s.Rational(1,15),s.Integer(1),s.Rational(192,245)]
hv=[s.Rational(176,147),s.Rational(656,735),s.Rational(76,147)]
txt=open(os.path.join(here,'../data/step57/two_lift_P1.txt')).read().replace('^','**')
gens=[s.sympify(z) for z in txt.replace('\n','').split(',') if z.strip()]
pt=dict(zip(list(M.h)+list(M.W),hv+wv))
assert all(s.factor(g.subs(pt))==0 for g in gens)
Qpt=s.factor(M.Q.subs(pt)); mupt=[s.factor(z.subs(pt)) for z in M.mu]
Xpt=[-mupt[1]/(mupt[0]-mupt[1]),mupt[0]/(mupt[0]-mupt[1]),s.Integer(0)]
qpt=s.factor(M.qexpr.subs(pt).subs(dict(zip(M.X,Xpt))))
assert Qpt==s.Rational(256,105) and mupt[:2]==[-s.Rational(54,35),s.Rational(2,7)] and Xpt[:2]==[s.Rational(5,32),s.Rational(27,32)] and qpt==s.Rational(27648,12005)
# Independent Koszul curvature at p values. Substitute algebraic positive sqrt(D).
os.environ['NB']='-1,1,1'; import step56_bianchiA_ake as B
t=B.t; af=[B.a,B.b,B.c]
sa,sb,sc,sA,sB,sC,sAp,sBp,sCp=s.symbols('sa sb sc sA sB sC sAp sBp sCp')
def cv(e):
 e=e.subs({s.diff(af[0],t,2):sAp,s.diff(af[1],t,2):sBp,s.diff(af[2],t,2):sCp})
 e=e.subs({s.diff(af[0],t):sA,s.diff(af[1],t):sB,s.diff(af[2],t):sC})
 return e.subs({af[0]:sa,af[1]:sb,af[2]:sc})
args=[sa,sb,sc,sA,sB,sC,sAp,sBp,sCp]
# Metric derivatives can be recovered without differentiating radicals: a'=h a, a''=(h'+h^2)a.
a=[s.sqrt(z) for z in A]; hp=[Dt(z) for z in h]
subs=dict(zip(args,a+[red(h[i]*a[i]) for i in range(3)]+[red((hp[i]+h[i]**2)*a[i]) for i in range(3)]))
Ric=B.Ric.applyfunc(cv)
point={}
for r in [s.Rational(2,5),s.Rational(1,2),s.Rational(3,4)]:
 yr=s.sqrt(D.subs(p,r)); sr={p:r,y:yr}; vals={v:s.simplify(z.subs(sr)) for v,z in subs.items()}
 R=Ric.applyfunc(lambda z:s.simplify(z.subs(vals)))
 point[str(r)]=[[str(s.simplify(R[i,j]+(3 if i==j else 0))) for j in range(4)] for i in range(4)]
assert all(v=='0' for R in point.values() for row in R for v in row)
# Curvature blocks at exact rational points. Vanishing at three points is a strong
# independent check, but it is not an all-p proof of half-conformal flatness.
def bases(sign):
 out=[]
 for i,(j,k) in zip([1,2,3],[(2,3),(3,1),(1,2)]):
  F=s.zeros(4);F[0,i]=1;F[i,0]=-1;F[j,k]=sign;F[k,j]=-sign;out.append(F)
 return out
BP,BM=bases(1),bases(-1)
# only exact pointwise blocks to keep runtime small
def block_at(r,basis):
 yr=s.sqrt(D.subs(p,r)); sr={p:r,y:yr}; vals={v:s.simplify(z.subs(sr)) for v,z in subs.items()}
 Rm={(i,j,k):[s.simplify(cv(z).subs(vals)) for z in vv] for (i,j,k),vv in B.Rm.items()}
 def rop(F,H):
  return s.simplify(sum(s.Rational(1,4)*Rm[(i,j,k)][l]*F[i,j]*H[k,l] for i in range(4) for j in range(4) for k in range(4) for l in range(4)))
 return s.Matrix([[rop(F,H) for H in basis] for F in basis])
blocks={}; eta={}
for r in [s.Rational(2,5),s.Rational(1,2),s.Rational(3,4)]:
 mm=block_at(r,BM); mp=block_at(r,BP); tf=s.simplify(mm-s.trace(mm)/3*s.eye(3))
 assert tf==s.zeros(3)
 xr=s.Matrix([s.sqrt(X[0].subs(p,r)),s.sqrt(X[1].subs(p,r)),0]); z=mp*xr
 wedge=s.simplify(xr[0]*z[1]-xr[1]*z[0]); assert wedge!=0
 blocks[str(r)]={'minus':[[str(mm[i,j]) for j in range(3)] for i in range(3)],'plus':[[str(mp[i,j]) for j in range(3)] for i in range(3)]};eta[str(r)]=str(wedge)
out={'h':[str(z) for z in h],'W':[str(z) for z in W],'mu':[str(z) for z in mu],'Q':str(Q),'flow_residuals':[str(z) for z in resh+resW+resX], 'q':str(q),'exact_witness':{'W':[str(z) for z in wv],'h':[str(z) for z in hv],'Q':str(Qpt),'mu':[str(z) for z in mupt],'X':[str(z) for z in Xpt],'q':str(qpt),'all_ideal_generators_zero':True},'Ricci_residuals':point,'curvature_blocks':blocks,'Omega_MOmega_wedge':eta}
outdir=os.path.join(here,'../data/step58');os.makedirs(outdir,exist_ok=True);json.dump(out,open(os.path.join(outdir,'exact_verification_fast.json'),'w'),indent=1)
print('EXACT FLOW, EINSTEIN, UNIT-LENGTH, TORSION CHECKS PASSED')
print('h=',h);print('W=',W);print('mu=',mu);print('q=',q)
print('EXACT KOSZUL RICCI AND THREE-POINT HALF-CONFORMAL/NONEIGENFORM CHECKS PASSED')
