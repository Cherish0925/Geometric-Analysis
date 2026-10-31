"""Fresh component derivation of the first-jet identity and scale consequences.
No input/import from the submitted verification scripts is used.
"""
import sympy as S
import itertools, json
from pathlib import Path
R=S.Rational
rho=S.symbols('rho', real=True)
c=S.symbols('c0:4',real=True); a=S.symbols('a0:4',real=True); b=S.symbols('b0:4',real=True)
omega=[]
for pairs in [[(0,1),(2,3)],[(0,2),(3,1)],[(0,3),(1,2)]]:
    w=S.zeros(4)
    for i,j in pairs:w[i,j]=1;w[j,i]=-1
    omega.append(w)
eps=[w/S.sqrt(2) for w in omega]
dpsi=[c[m]*eps[0]+a[m]*eps[1]+b[m]*eps[2] for m in range(4)]
dA=[S.Matrix([[-rho*c[m]/6,-rho*a[m]/8,-rho*b[m]/8],[-rho*a[m]/8,rho*c[m]/12,0],[-rho*b[m]/8,0,rho*c[m]/12]]) for m in range(4)]
D={I:S.expand(dpsi[I[0]][I[1],I[2]]+dpsi[I[1]][I[2],I[0]]+dpsi[I[2]][I[0],I[1]]) for I in itertools.combinations(range(4),3)}
star=[0]*4
for I,val in D.items():
    k=next(i for i in range(4) if i not in I)
    star[k]+=S.LeviCivita(*I,k)*val
ip=[sum(c[i]*rho*eps[0][i,j] for i in range(4)) for j in range(4)]
C=sum(ip[j]*star[j] for j in range(4))
J2=0
for j,k,l in itertools.product(range(4),repeat=3):
    z=sum(dA[i][u,v]*omega[u][i,j]*omega[v][k,l]/2 for i,u,v in itertools.product(range(4),range(3),range(3)))
    J2+=S.expand(z*z)
gradA2=sum(sum(z*z for z in da) for da in dA)
gradpsi2=sum(z*z for z in (*c,*a,*b))
dr2=sum(z*z for z in c)
d2=sum(z*z for z in D.values())
checks={}
checks['gradient_operator_norm_identity']=S.expand(gradA2-rho**2*gradpsi2/32-rho**2*dr2/96)==0
checks['divergence_hodge_first_jet_identity']=S.expand(gradA2-J2-rho**2*(gradpsi2-2*d2)/64-rho**2*dr2/32+rho*C/16)==0
# Elimination using independent linear algebra of the two integrated relations.
A,B,D2,T,Cc=S.symbols('A B D2 T Cc')
# A=integral rho^2 |nabla psi|^2; B=integral rho^2 Bpsi;
# D2=integral rho^2 |dpsi|^2; T=integral rho^2 |drho|^2; Cc=integral rho Cpsi.
J_from_point=A/64+D2/32-S.Rational(1,48)*T+Cc/16
J_final=S.expand(J_from_point.subs(A,2*D2-B+4*Cc-2*T))
checks['integrated_energy_elimination']=S.expand(J_final-(-B/64+D2/16-5*T/96+Cc/8))==0
checks['calibrated_positive_value']=S.simplify(-(-4)*(S.sqrt(2))**4/192-(S.sqrt(2))**6/384)==R(1,16)
lam,RR,V,SS=S.symbols('lambda RR V SS',nonzero=True)
f=RR/(lam**2*V)-2*SS/(lam*V)+4
checks['scale_optimization']=S.simplify(f.subs(lam,RR/SS)-(4-SS**2/(RR*V)))==0
results={'checks':checks,'passed':all(checks.values()),'scope':'exact finite-component algebra; does not certify bundle/PDE existence, analytic estimates, or novelty', 'variables':12,'no_source_script_imports':True}
p=Path('/mnt/data/yau26_rounds12_audit_20260921/independent_local_check.json');p.write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2));assert results['passed']
