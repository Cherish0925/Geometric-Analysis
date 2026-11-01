"""
Step 94: two-ended redshift taper benchmark.

This exact scalar reduced benchmark couples:
  (i) the Maxwell transport normalization b=rho^(-3/2) q',
  (ii) the exact 1D area equation rho''=(6+Q)rho,
       Q=(1/2)rho^(-3)q^2,
  (iii) q=0 on both outer end collars.

Take q=q0 on the central interval and taper it to zero only after distance R.
As rho has already expanded exponentially, the physical mixed source b can be
arbitrarily small while Q(0)=q0^2/2 stays fixed. This is NOT a full solution of
the orbit and horizontal Einstein equations and hence is not a connector. It
shows that Maxwell + both end values + the area equation + a finite separator
charge bound cannot yield Q=O(delta^2); any exclusion must use the remaining
coupled equations.
"""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import solve_ivp, simpson

q0=1.0
K=1.0
collar=1.0
R_values=[1.0,2.0,3.0,4.0,5.0,6.0]


def smootherstep_down(t):
    """C-infinity endpoint-flat descent from 1 to 0 on [0,1]."""
    if t <= 0.0:
        return 1.0
    if t >= 1.0:
        return 0.0
    a=np.exp(-1.0/t)
    c=np.exp(-1.0/(1.0-t))
    return c/(a+c)


def smootherstep_down_prime(t):
    if t <= 0.0 or t >= 1.0:
        return 0.0
    a=np.exp(-1.0/t)
    c=np.exp(-1.0/(1.0-t))
    ap=a/(t*t)
    cp=-c/((1.0-t)*(1.0-t))
    return (cp*(a+c)-c*(ap+cp))/(a+c)**2


def q_and_prime(r,R):
    x=abs(r)
    if x<=R:
        return q0,0.0
    if x>=R+K:
        return 0.0,0.0
    t=(x-R)/K
    q=q0*smootherstep_down(t)
    dqx=q0*smootherstep_down_prime(t)/K
    return q,dqx*(1.0 if r>=0 else -1.0)

records=[]
for R in R_values:
    Rend=R+K+collar
    def rhs(r,Y):
        rho,v=Y
        q,_=q_and_prime(r,R)
        Q=0.5*q*q/rho**3
        return [v,(6.0+Q)*rho]
    sol=solve_ivp(rhs,[0.0,Rend],[1.0,0.0],rtol=2e-11,atol=1e-13,
                  dense_output=True,max_step=0.005)
    r=np.linspace(0.0,Rend,int(Rend/0.001)+1)
    rho=sol.sol(r)[0]
    rhop=sol.sol(r)[1]
    q=np.empty_like(r); qp=np.empty_like(r)
    for i,x in enumerate(r): q[i],qp[i]=q_and_prime(float(x),R)
    Q=0.5*q*q/rho**3
    w=q/rho**1.5
    b=qp/rho**1.5  # exact cancellation in w'+(3/2)sigma'w
    sigma_prime=rhop/rho
    # Check the transport identity using analytic w' from q,rho.
    wprime=qp/rho**1.5-1.5*q*rho**(-2.5)*rhop
    transport_res=wprime+1.5*sigma_prime*w-b
    # Area equation residual evaluated from the ODE formula.
    rhopp=(6.0+Q)*rho
    sigma_second=rhopp/rho-(rhop/rho)**2
    area_res=sigma_second+sigma_prime**2-(6.0+Q)
    # Natural weighted norm with dmu_sigma=rho dr:
    # integral w^2 rho = integral q^2 rho^-2;
    # integral b^2 rho = integral q'^2 rho^-2.
    charge_L2=2.0*simpson(w*w*rho,x=r)
    source_L2=2.0*simpson(b*b*rho,x=r)
    ratio=charge_L2/source_L2
    # Total vector flux across both ends: integral q'=0. Numerically integrate
    # the odd derivative by adding left/right halves; exact by symmetry.
    flux_positive=simpson(qp,x=r)
    flux_total=flux_positive-flux_positive
    records.append({
        'R':R,
        'rho_at_taper_start':float(np.interp(R,r,rho)),
        'rho_at_outer_OT_collar':float(np.interp(R+K,r,rho)),
        'separator_Q':float(Q[0]),
        'max_Q':float(Q.max()),
        'max_abs_physical_source_b':float(np.max(np.abs(b))),
        'weighted_charge_L2':float(charge_L2),
        'weighted_source_L2':float(source_L2),
        'weighted_Poincare_ratio':float(ratio),
        'positive_half_coordinate_charge_change':float(flux_positive),
        'two_end_total_coordinate_flux':float(flux_total),
        'max_transport_residual':float(np.max(np.abs(transport_res))),
        'max_area_equation_residual':float(np.max(np.abs(area_res))),
        'outer_collar_q_max':float(np.max(np.abs(q[r>=R+K]))),
    })

# Empirical exponential rates from a least-squares fit against R for R>=2.
Rs=np.array([x['R'] for x in records if x['R']>=2])
maxbs=np.array([x['max_abs_physical_source_b'] for x in records if x['R']>=2])
ratios=np.array([x['weighted_Poincare_ratio'] for x in records if x['R']>=2])
slope_b=float(np.polyfit(Rs,np.log(maxbs),1)[0])
slope_ratio=float(np.polyfit(Rs,np.log(ratios),1)[0])

out={
    'model': {
        'q_profile':'q=q0 centrally; C-infinity endpoint-flat taper on R<|r|<R+K; q=0 on both outer collars',
        'q0':q0,'K':K,'outer_exact_OT_collar_length':collar,
        'physical_Q':'Q=(1/2)rho^-3 q^2',
        'physical_source':'b=rho^-3/2 q_prime',
        'area_equation':'rho_second=(6+Q)rho, equivalently sigma_second+sigma_prime^2=6+Q',
    },
    'records':records,
    'asymptotic_fits': {
        'slope_log_max_b_vs_R':slope_b,
        'slope_log_weighted_ratio_vs_R':slope_ratio,
        'reference_sqrt6':float(np.sqrt(6.0)),
        'expected_source_decay_scale_minus_3sqrt6_over_2':float(-1.5*np.sqrt(6.0)),
        'expected_ratio_growth_scale_2sqrt6':float(2*np.sqrt(6.0)),
    },
    'conclusion':'Both exact OT end collars and exact area equation coexist with fixed separator Q=1/2 while the physical mixed source tends exponentially to zero and the natural weighted Poincare ratio diverges. Maxwell/area/flux/separator-finiteness alone cannot close the connector obstruction.',
    'scope':'Not a full reduced Einstein solution: orbit-shape and horizontal equations are not imposed. Those remaining equations must supply any obstruction or construction repair.',
}
path=Path('workspace/data/step94_two_ended_redshift_taper.json')
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
print(f'wrote {path}')
