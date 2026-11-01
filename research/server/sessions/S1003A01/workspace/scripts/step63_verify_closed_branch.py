"""Exact symbolic verification of the Step-63 surviving Bianchi-IX nut branch."""
import sympy as sp, json, os
t=sp.symbols('t', positive=True)
r=t/sp.sqrt(2)
a=[sp.sinh(sp.sqrt(2)*t)/sp.sqrt(2), sp.sqrt(2)*sp.sinh(r), sp.sqrt(2)*sp.sinh(r)]
h=[sp.diff(z,t)/z for z in a]
W=[a[i]/(a[(i+1)%3]*a[(i+2)%3]) for i in range(3)]
mu=[sp.trigsimp(2*W[i]-h[(i+1)%3]-h[(i+2)%3]) for i in range(3)]
b=[sp.trigsimp(h[0]+W[0]-W[1]-W[2]),sp.trigsimp(h[1]-W[0]+W[1]-W[2]),sp.trigsimp(h[2]-W[0]-W[1]+W[2])]
# Einstein flow residuals lambda=-3
res=[]
for i in range(3):
 j,k=(i+1)%3,(i+2)%3
 res.append(sp.trigsimp(sp.diff(h[i],t)+h[i]*sum(h)-2*(W[i]**2-(W[j]-W[k])**2)-3))
Q=sum(h[i]*h[j] for i in range(3) for j in range(i+1,3))+sum(z*z for z in W)-2*sum(W[i]*W[j] for i in range(3) for j in range(i+1,3))
# simplify via rewrite exp if needed
simp=lambda e:sp.simplify(sp.trigsimp(sp.expand_trig(e.rewrite(sp.exp))))
out={'mu':[str(simp(x)) for x in mu], 'b':[str(simp(x)) for x in b],
     'Einstein_flow_residual':[str(simp(x)) for x in res], 'Q_minus_3':str(simp(Q-3)),
     'closure_axis1':str(simp(mu[0])), 'q_axis1':str(simp(2*(mu[0]**2+b[1]**2+b[2]**2)))}
od=os.path.join(os.path.dirname(__file__),'../data/step63');os.makedirs(od,exist_ok=True)
json.dump(out,open(os.path.join(od,'bix_closed_branch_exact.json'),'w'),indent=1)
print(json.dumps(out,indent=1))
