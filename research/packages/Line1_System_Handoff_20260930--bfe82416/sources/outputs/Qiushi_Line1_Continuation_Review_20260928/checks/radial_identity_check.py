from radial_search_new import Model
import numpy as np,json

def audit(m,p):
 base=p.copy();base[2*m.n:]=0
 delta=m.residual(base);delta_bar=delta[0]+delta[1]+np.sqrt(2)*delta[2]
 v,vt,vtt=np.einsum('ijk,k->ij',m.B[0],p[:m.n]);phi,pt,ptt=np.einsum('ijk,k->ij',m.B[2],p[2*m.n:]);F=np.exp(v)*m.F0;Ft=np.exp(v)*(m.F0t+m.F0*vt);a=np.exp(2*phi)
 Hbar=F*ptt+(Ft+2*F)*pt+F*pt**2
 terms=np.array([12*(Hbar-delta_bar/6)**2,4*(m.r2*(a-1)+delta_bar/4)**2,(16+12*a)*F*pt**2*m.r2,-7*delta_bar**2/12])
 vals=terms@m.weights;lhs=m.fun(p)-m.fun(base)
 return {'jG':float(m.fun(p)),'jK':float(m.fun(base)),'lhs':float(lhs),'rhs':float(sum(vals)),'error':float(lhs-sum(vals)),'four_terms':vals.tolist(),'scalar_error':float(np.dot(delta_bar**2,m.weights))}
if __name__=='__main__':
 rng=np.random.default_rng(7)
 for mu,R in [(.001,3),(.03,2),(.2,4)]:
  for q in [24,46]:
   m=Model(mu,R,3,q);p=rng.normal(0,.03,m.dim) if q==24 else p
   print(json.dumps({'mu':mu,'R':R,'q':q,**audit(m,p)}))
