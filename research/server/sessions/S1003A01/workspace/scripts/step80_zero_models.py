"""Exact local epsilon-regularization for model torsion zeros.

Computes the scalar regularized identity for q=c*rho^(2m) in R^4 near
(i) an isolated zero (rho=4D radius), and
(ii) a smooth codimension-two zero stratum (rho=normal 2D radius, per unit
surface area).  This distinguishes vanishing isolated flux from the 4*pi*m
surface residue.

Output: workspace/data/step80/zero_model_regularization.json
"""
import json, os
import mpmath as mp
mp.mp.dps=50

def isolated(m,eps,R=mp.mpf(1),c=mp.mpf(1)):
    # area S^3 = 2 pi^2; Delta q = 2m(2m+2)c r^(2m-2)
    A=2*mp.pi**2
    dq=lambda r: 2*m*c*r**(2*m-1)
    q=lambda r: c*r**(2*m)
    grad=mp.quad(lambda r:A*r**3*dq(r)**2/(q(r)+eps)**2,[0,eps**(mp.mpf(1)/(2*m)),R])
    lap=mp.quad(lambda r:A*r**3*(2*m*(2*m+2)*c*r**(2*m-2))/(q(r)+eps),[0,eps**(mp.mpf(1)/(2*m)),R])
    flux=A*R**3*dq(R)/(q(R)+eps)
    return grad,lap,flux

def codim2(m,eps,R=mp.mpf(1),c=mp.mpf(1)):
    # per unit surface area; normal circle length 2 pi r
    A=2*mp.pi
    dq=lambda r:2*m*c*r**(2*m-1)
    q=lambda r:c*r**(2*m)
    grad=mp.quad(lambda r:A*r*dq(r)**2/(q(r)+eps)**2,[0,eps**(mp.mpf(1)/(2*m)),R])
    lap=mp.quad(lambda r:A*r*(4*m*m*c*r**(2*m-2))/(q(r)+eps),[0,eps**(mp.mpf(1)/(2*m)),R])
    flux=A*R*dq(R)/(q(R)+eps)
    return grad,lap,flux

def main():
    out={}
    for geom,fn in [('isolated4',isolated),('codim2',codim2)]:
        out[geom]={}
        for m in [1,2,3,4]:
            rows=[]
            for e in ['1e-2','1e-4','1e-8','1e-16']:
                eps=mp.mpf(e); gr,la,fl=fn(m,eps)
                rows.append({'eps':e,'grad':mp.nstr(gr,18),'lap':mp.nstr(la,18),'flux':mp.nstr(fl,18),'lap_minus_grad':mp.nstr(la-gr,18)})
            out[geom][str(m)]=rows
    root=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); d=os.path.join(root,'data','step80');os.makedirs(d,exist_ok=True)
    with open(os.path.join(d,'zero_model_regularization.json'),'w') as f:json.dump(out,f,indent=1)
    print(json.dumps(out,indent=1))
if __name__=='__main__':main()
