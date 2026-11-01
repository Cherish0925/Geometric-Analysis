"""Fast exact/numerical regularized q+eps budgets on the complete Bianchi-VIII
strict AKE model.

Unlike the full Step-79 frame engine, all scalar densities are inserted from
exact rational formulas already proved in Steps 58--59.  The model is used only
as a noncompact control for the epsilon limit.

Outputs workspace/data/step80/regularized_model_fast.json.
"""
import json, os
import numpy as np
import mpmath as mp

mp.mp.dps = 40

def G(p):
    return 4*(3*p*p+1)/((1-p)**2*(1+p)**2*(3*p-1)*(3*p+1))
def vol(p):
    # sqrt(A1 A2 A3), simplified exactly on 1/3<p<1.
    return 32*p*mp.sqrt((9*p*p-1)*(3*p*p+1))/(3*(1-p*p)**2)
def q(p): return 36*(1-p*p)**3/(1+3*p*p)**3
def eta2(p):
    # Step-59 eta_squared uses the Step-59 form norm, twice the Step-62/79
    # vector norm.  Divide by two here.
    return 9*(1-p*p)**3*(9*p*p-1)/(3*p*p+1)**4
def trV2(p):
    # Step-59 W3plus_squared is the HS norm tr V^2.
    return 81*(1-p*p)**4*(9*p*p-1)**2/(2*(3*p*p+1)**6)
def qp(p): return mp.diff(q,p)
def lapq(p):
    return mp.diff(lambda z: vol(z)/mp.sqrt(G(z))*qp(z),p)/(vol(p)*mp.sqrt(G(p)))
def D(p):
    # Delta q = -D + 18q - 9q^2/4 for s=-12.  This evaluates to
    # 108(1-p^2)^3(9p^2-1)(33p^4-26p^2+25)/(1+3p^2)^6.
    return -lapq(p)+18*q(p)-mp.mpf(9)/4*q(p)**2

# Exact radial current fluxes Phi=vol*j through p-levels.  These are recovered
# from the pointwise Kodaira density F by Phi'=vol*sqrt(G)*F and normalized by
# Phi(1/3)=0.  This scalar-only script does not evaluate the Kodaira currents;
# those remain in the full Step-79 frame engine.

def p_of_u(u):
    x=1-mp.e**(-u)
    return mp.mpf(1)/3+mp.mpf(2)/3*x*x
def dpdu(u):
    x=1-mp.e**(-u)
    return mp.mpf(4)/3*x*mp.e**(-u)

def main():
    root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outdir=os.path.join(root,'data','step80'); os.makedirs(outdir,exist_ok=True)
    # Piecewise Gauss-Legendre in u.  Tail u>U is handled by choosing U=32;
    # fixed-epsilon currents then vanish exponentially, while the moving layer
    # u~(1/3)log(1/eps) is resolved for eps>=1e-24.
    order=32; U=32
    zz,ww=np.polynomial.legendre.leggauss(order)
    nodes=[]
    for k in range(U):
        for zf,wf in zip(zz,ww):
            u=mp.mpf(k)+(mp.mpf(1)+mp.mpf(float(zf)))/2
            w=mp.mpf(float(wf))/2
            p=p_of_u(u); jac=dpdu(u)
            meas=vol(p)*mp.sqrt(G(p))*jac*w
            nodes.append((u,p,w,jac,meas))
    epss=[mp.mpf(x) for x in ['1e-1','1e-2','1e-3','1e-4','1e-6','1e-8','1e-10','1e-12','1e-16','1e-20','1e-24']]
    res={}
    for eps in epss:
        sums={k:mp.mpf(0) for k in ['grad','D','q2','rhs','eta','V','cross']}
        peak=(mp.mpf(0),mp.mpf(0),mp.mpf(0))
        for u,p,w,jac,meas in nodes:
            qv=q(p); den=qv+eps; qprime=qp(p)
            grad=(qprime*qprime/G(p))/den**2
            et=24*eta2(p)/den
            vv=-8*trV2(p)/den
            cr=D(p)/den-et-vv
            vals={'grad':grad,'D':D(p)/den,'q2':mp.mpf(9)/4*qv*qv/den,
                  'rhs':18*qv/den,'eta':et,'V':vv,'cross':cr}
            for key,val in vals.items(): sums[key]+=val*meas
            flux=abs(vol(p)/mp.sqrt(G(p))*qprime/den)
            if flux>peak[0]: peak=(flux,u,p)
        lhs=sums['grad']+sums['D']+sums['q2']
        key=mp.nstr(eps,2)
        res[key]={**{k:mp.nstr(v,18) for k,v in sums.items()},
                  'lhs':mp.nstr(lhs,18),'residual':mp.nstr(lhs-sums['rhs'],10),
                  'peak_log_flux':mp.nstr(peak[0],15),'peak_u':mp.nstr(peak[1],12),
                  'peak_p':mp.nstr(peak[2],15)}
        print(key,res[key],flush=True)
    # Pointwise profile of Delta log q and regularized peak scaling.
    profile=[]
    for p in [mp.mpf('0.333334'),mp.mpf('0.34'),mp.mpf('0.4'),mp.mpf('0.5'),mp.mpf('0.6'),mp.mpf('0.75'),mp.mpf('0.9'),mp.mpf('0.99'),mp.mpf('0.999')]:
        dl=lapq(p)/q(p)-qp(p)**2/(G(p)*q(p)**2)
        profile.append({'p':mp.nstr(p,12),'q':mp.nstr(q(p),15),'Delta_log_q':mp.nstr(dl,15)})
    out={'quadrature':{'u_max':U,'order_per_unit':order,'nodes':len(nodes)},'results':res,'profile':profile}
    with open(os.path.join(outdir,'regularized_model_fast.json'),'w') as f: json.dump(out,f,indent=1)

if __name__=='__main__': main()
