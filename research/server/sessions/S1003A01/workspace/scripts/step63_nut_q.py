"""Leading torsion of regular Bianchi-IX nut branches."""
import sympy as s,json,os
here=os.path.dirname(__file__)
D=json.load(open(os.path.join(here,'../data/step63/bix_nut_series_order5.json')))
u=s.symbols('u', positive=True)
d1,d2,R1,R2,R3=s.symbols('d1 d2 R1 R2 R3')
loc={str(x):x for x in (d1,d2,R1,R2,R3)}
M=[s.sympify(x,locals=loc) for x in D['M']]
Xc={int(k):[s.sympify(x,locals=loc) for x in v] for k,v in D['X_coeffs'].items()}
X=[sum(Xc[k][i]*u**k for k in Xc) for i in range(3)]
# H,Z from saved metric coefficients, reconstruct f through order 5
A=[s.Rational(1,6)+d1,s.Rational(1,6)+d2,s.Rational(1,6)-d1-d2]
coeff={1:A}
for rec in D['metric_records']:
 k=rec['order']; coeff[k]=[s.sympify(x,locals=loc) for x in rec['coeff']]
f=[1+sum(coeff[k][i]*u**k for k in coeff) for i in range(3)]
tr=lambda e:s.series(e,u,0,5).removeO().expand()
H=[tr(1+2*u*s.diff(fi,u)/fi) for fi in f]
Z=[tr(f[i]/(f[(i+1)%3]*f[(i+2)%3])) for i in range(3)]
b=[H[0]+Z[0]-Z[1]-Z[2],H[1]-Z[0]+Z[1]-Z[2],H[2]-Z[0]-Z[1]+Z[2]]
# Original q has weight 1/t^2: h_i=H_i/t,W_i=Z_i/t,mu=M_i/t.
Qnum=sum(X[i]*M[i]**2 for i in range(3))+(X[0]+X[1])*b[2]**2+(X[0]+X[2])*b[1]**2+(X[1]+X[2])*b[0]**2
q=tr(2*Qnum/u)
branches=[('axis1',{d1:s.Rational(1,6),d2:-s.Rational(1,12),R1:1,R2:0,R3:0}),('axis2',{d1:-s.Rational(1,12),d2:s.Rational(1,6),R1:0,R2:1,R3:0}),('axis3',{d1:-s.Rational(1,12),d2:-s.Rational(1,12),R1:0,R2:0,R3:1})]
out={}
for name,sub in branches:
 # Substitute into the analytic numerator before dividing by u to avoid 0/0
 # artifacts introduced by generic rational expressions in higher coefficients.
 num=s.series(Qnum.subs(sub),u,0,5).removeO().expand()
 qq=s.factor(2*num/u); out[name]=str(qq); print(name,qq,'leading',s.limit(qq,u,0))
os.makedirs(os.path.join(here,'../data/step63'),exist_ok=True)
json.dump(out,open(os.path.join(here,'../data/step63/bix_nut_q.json'),'w'),indent=1)
