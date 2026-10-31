"""Exact finite algebra used by the accompanying analytic proof.
These tests do not verify the analytic remainder or global topology.
"""
import sympy as s
import json
u=s.symbols('u1:4'); v=s.symbols('v1:4'); la=s.symbols('l1:4',positive=True)
H=[u[i]+u[(i+1)%3]*u[(i+2)%3]/2 for i in range(3)]
P=sum(la[i]/4*(v[i]-2*H[i]/la[i])**2 for i in range(3))
relative=(la[0]/4*(v[0]+2*H[0]/la[0])**2+
          la[1]/4*(v[1]-(2*u[1]-u[0]*u[2])/la[1])**2+
          la[2]/4*(v[2]+2*H[2]/la[2])**2+2*u[0]*u[1]*u[2]/la[1])
primitive=u[0]**2+u[2]**2+u[0]*u[1]*u[2]
res=s.simplify(relative-P-sum(s.diff(primitive,u[i])*v[i] for i in range(3)))
assert res==0
c=s.symbols('c1:4')
fP=11*sum(q*q for q in c)-10*(c[0]*c[1]+c[0]*c[2]+c[1]*c[2])-37*c[0]+11*c[1]+19*c[2]+s.Rational(59,4)
fJ=fP+(2*sum(c)-7)**2/4
star=[s.Rational(9,4),s.Rational(3,4),s.Rational(1,2)]
d=[c[i]-star[i] for i in range(3)]
assert s.expand(fP+18-16*sum(x*x for x in d)+5*sum(d)**2)==0
assert s.expand(fJ+18-16*sum(x*x for x in d)+4*sum(d)**2)==0
assert fJ.subs(dict(zip(c,star)))==-18
th,delta=s.symbols('theta delta')
replication=4*(1-th)+4*th*(1-delta)
assert s.simplify(replication.subs(th,s.Rational(2,9))-(4-s.Rational(8,9)*delta))==0
out={
 'relative_density_minus_P_equals_primitive_derivative':True,
 'corner_P_polynomial':str(s.expand(fP)),
 'corner_J_polynomial':str(s.expand(fJ)),
 'corner_minimizer':[str(x) for x in star],
 'corner_minimum':-18,
 'log_energy_coefficient':-9,
 'P_quadratic_form_eigenvalues':[1,16,16],
 'J_quadratic_form_eigenvalues':[4,16,16],
 'replication_theta_2_9':'4 - (8/9) delta',
 'scope':'Finite exact algebra only. Analytic estimates and topology are proved in the MD.'}
print(json.dumps(out,indent=2))
open('/mnt/data/line1_analytic_continuation_20261007/exact_algebra_results.json','w').write(json.dumps(out,indent=2)+'\n')
