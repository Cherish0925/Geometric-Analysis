"""Exact endpoint and global-integral checks for the rational Bianchi-VIII AKE branch."""
import sympy as s, json, os
p=s.symbols('p', positive=True); d=s.symbols('d', positive=True); r=s.symbols('r', positive=True)
G=4*(3*p**2+1)/((1-p)**2*(1+p)**2*(3*p-1)*(3*p+1))
A1=4*(3*p-1)*(3*p**2+1)/(3*(1-p)*(1+p)**2)
A2=4*(3*p+1)*(3*p**2+1)/(3*(1-p)**2*(1+p))
A3=64*p**2/((1-p)*(1+p)*(3*p**2+1))
X1=(1-p)**3*(3*p+1)/(16*p**3);X2=(1+p)**3*(3*p-1)/(16*p**3)
q=36*(1-p**2)**3/(1+3*p**2)**3
vol=64*p*(3*p**2+1)/(3*(1-p)**3*(1+p)**3)
eta2=-18*(p-1)**3*(p+1)**3*(3*p-1)*(3*p+1)/(3*p**2+1)**4
W32=81*(p-1)**4*(p+1)**4*(3*p-1)**2*(3*p+1)**2/(2*(3*p**2+1)**6)
# Bolt: geodesic distance r, solve delta=p-1/3 as series c2 r2+c4 r4+c6 r6 using (dp/dr)^2=1/G.
c2,c4,c6=s.symbols('c2 c4 c6'); delta=c2*r**2+c4*r**4+c6*r**6
P=s.Rational(1,3)+delta
lhs=s.diff(delta,r)**2
rhs=s.series((1/G).subs(p,P),r,0,8).removeO()
poly=s.Poly(s.series(lhs-rhs,r,0,8).removeO(),r)
sol=[]; eq=[s.Eq(poly.coeff_monomial(r**k),0) for k in [2,4,6]]
S=s.solve(eq,[c2,c4,c6],dict=True); S=[z for z in S if z[c2]>0][0]
def ser(expr,n=8): return s.factor(s.series(expr.subs(p,P).subs(S),r,0,n).removeO())
# Coefficients of the mixed omega_2 piece:
# sqrt(X2 A2) dr^sigma2 + sqrt(X2 A3 A1) sigma3^sigma1.
Cdr=s.sqrt(X2*A2); Cth=s.sqrt(X2*A3*A1)
bolt={'delta':str(s.expand(delta.subs(S))),'A1':str(ser(A1)),'A2':str(ser(A2)),'A3':str(ser(A3)),'A2-A3':str(ser(A2-A3)),'X1':str(ser(X1)),'X2':str(ser(X2)),'q':str(ser(q)),'Omega2_dr_coeff':str(ser(Cdr)),'Omega2_theta_coeff':str(ser(Cth)),'Omega2_module_difference':str(ser(Cdr/r-Cth/r**2))}
# Infinity x=1-p. expansions and exact leading geodesic relation.
x=s.symbols('x',positive=True)
def infser(expr,n=5):return str(s.factor(s.series(expr.subs(p,1-x),x,0,n).removeO()))
infty={'G':infser(G,3),'A1':infser(A1,3),'A2':infser(A2,1),'A3':infser(A3,3),'X1':infser(X1,5),'X2':infser(X2,5),'q':infser(q,6),'vol':infser(vol,2)}
# Exact convergence and integrated AAD balance. Integrate terms separately where finite.
Iq=s.integrate(s.cancel(q*vol),(p,s.Rational(1,3),1))
Iq2=s.integrate(s.cancel(q**2*vol),(p,s.Rational(1,3),1))
Ieta=s.integrate(s.cancel(eta2*vol),(p,s.Rational(1,3),1))
IW3=s.integrate(s.cancel(W32*vol),(p,s.Rational(1,3),1))
balance=s.simplify(Ieta+2*IW3+s.Rational(3,16)*Iq2-s.Rational(3,2)*Iq)
ints={'Iq':str(Iq),'Iq2':str(Iq2),'Ieta':str(Ieta),'IW3':str(IW3),'balance':str(balance)}
# Euler-type volume divergence and completeness: sqrtG ~ 1/(sqrt2 x).
assert balance==0
out={'bolt_series':bolt,'infinity_series_x=1-p':infty,'integrals_per_orbit_volume':ints}
here=os.path.dirname(os.path.abspath(__file__));od=os.path.join(here,'../data/step58');os.makedirs(od,exist_ok=True);json.dump(out,open(os.path.join(od,'global_exact.json'),'w'),indent=1)
print(json.dumps(out,indent=1))
