"""
Step 19 (S0910A02): finite rod/corner matching certificate for the periodic
#_k(S^2 x S^2) toric crux family.

This is not a PDE solve.  It records the finite 1D rod data proposed in the
Strategist note and checks compatibility with the local diagonal smooth-corner
jets computed symbolically in step19_corner_*.

For each even m=2k+2, take periodic rod labels e1,e2,-e1,-e2,... and a common
large edge-curvature parameter A=m^2.  On each rod, use the exact 1D edge profile
    Q'' + (1+2A) Q = 0,
    Q(0)=Q(L)=0, Q'(0)=1, Q'(L)=-1,
so L=pi/sqrt(1+2A), Phi=int Q=2/(1+2A).
At each standard-basis corner, Lemma 2.2 smoothness allows diagonal p,q, and the
local exact Ric=g corner matching through r^2 is solvable with A free.  Choosing
the free q05 coefficient to match the rod Taylor coefficient gives explicit
corner jets compatible with the 1D rod expansion.

Scientific meaning: this rules out the simplest BUILD shortcut "corner closure
alone caps A" at the finite rod + low-corner-jet level.  It does NOT construct a
global smooth Ricci-pinched metric; global base geometry, horizontal/traceless
Ricci, spectral determinant equation, holonomy/twist, and higher-order matching
remain open.
"""
import json, math, os


def labels_for_m(m):
    base=[(1,0),(0,1),(-1,0),(0,-1)]
    return [base[i%4] for i in range(m)]

def det(u,v): return u[0]*v[1]-u[1]*v[0]

def corner_type_ok(labels):
    # Adjacent labels must be a Z^2 basis up to sign.  For diagonal ansatz we also
    # require each label line to be one of coordinate axes, signs irrelevant.
    out=[]
    for i in range(len(labels)):
        v=labels[i]; w=labels[(i+1)%len(labels)]
        coordinate_lines=(abs(v[0])+abs(v[1])==1 and abs(w[0])+abs(w[1])==1)
        out.append({'corner':i,'labels':[v,w], 'det':det(v,w),
                    'unimodular':abs(det(v,w))==1,
                    'diagonal_standard_basis_up_to_sign':coordinate_lines and abs(det(v,w))==1})
    return out

def separated_transfer(A):
    if A == 0:
        return {'a_plus':1.0,'second_same_circle_slope_mu':1.0,'cone_angle_2pi_mu':2*math.pi,'mu_inverse':1.0}
    ap=(-1+math.sqrt(9+24*A))/2
    mu=(2*ap+1)/(ap*(ap+2))
    return {'a_plus':ap,'second_same_circle_slope_mu':mu,
            'cone_angle_2pi_mu':2*math.pi*mu,'mu_inverse':1/mu,
            'asymptotic_mu_sqrt_3A_over_2':mu*math.sqrt(3*A/2)}

def rod_data(A):
    omega=math.sqrt(1+2*A)
    L=math.pi/omega
    Phi=2/(1+2*A)
    return {'A':A,'K_edge':-A,'omega':omega,'rod_length':L,'rod_flux':Phi,
            'Q_profile':'sin(omega*s)/omega',
            'separated_same_circle_transfer':separated_transfer(A)}

def corner_jets(A):
    # From step19_corner_formal_series_order2_fast, with q05 chosen from
    # Q(s)=sin(omega s)/omega: q05=omega^4/120=(1+2A)^2/120.
    q05=(1+2*A)**2/120
    return {
      'A':A,
      'constant_order':{
        'a_p_cubic':'-(2A+1)/6',
        'b_q_cubic':'-(2A+1)/6',
        'numeric':{'a':-(2*A+1)/6,'b':-(2*A+1)/6}},
      'chosen_free_q05_matches_rod_fifth_order':q05,
      'r2_order_coefficients_with_this_choice':{
        'mu_r4_m40':(-16*A*A-10*A+120*q05-1)/144,
        'mu_r2t2_m22':-(-4*A*A-4*A+120*q05-1)/24,
        'p_r5_p50':-(-13*A*A-7*A+60*q05-1)/60,
        'p_r3t2_p32':(-4*A*A-4*A+120*q05-1)/36,
        'q_r2t3_q23':-(-2*A+120*q05-1)/24,
        'q_t5_q05':q05},
      'simplified_expected':{
        'mu_r4_m40':'-A(2A+1)/24',
        'mu_r2t2_m22':'0',
        'p_r5_p50':'(22A^2+10A+1)/120',
        'p_r3t2_p32':'0',
        'q_r2t3_q23':'-A(2A+1)/12',
        'q_t5_q05':'(1+2A)^2/120'},
      'residual_statement':'constant and r^2 coefficients of Ric-g vanish for all ray slopes z by step19_corner_formal_series_order2_fast.json'
    }

def case(m):
    A=m*m
    labs=labels_for_m(m)
    rd=rod_data(A)
    total_flux=m*rd['rod_flux']
    return {
      'm':m,
      'k_for_#kS2xS2_if_topology_certificate_applies':(m-2)//2,
      'labels':labs,
      'all_corners':corner_type_ok(labs),
      'all_corners_unimodular_diagonal':all(c['diagonal_standard_basis_up_to_sign'] for c in corner_type_ok(labs)),
      'common_rod_data':rd,
      'total_flux':total_flux,
      'volume_proxy_2pi2_total_flux':2*math.pi**2*total_flux,
      'perimeter_sum_mL':m*rd['rod_length'],
      'corner_jets_for_each_standard_corner':corner_jets(A),
      'finite_matching_status':(
          'The 1D rods close exactly and every corner is a standard-basis fixed point up to sign. Local diagonal smoothness and Ric=g formal matching through r^2 impose no cap on A. This is a formal finite rod/corner configuration, not a global metric.')
    }

reports={
  'title':'Step 19 finite rod/corner matching for periodic toric crux labels',
  'decision_question':'Does the finite 1D rod + right-angle corner system itself cap A_i and force a chi-uniform flux lower bound?',
  'answer_at_tested_formal_level':'No cap appears: the symmetric all-A=m^2 configurations satisfy rod ODE/endpoint slopes and local standard-corner matching through the first nontrivial formal order, with total flux ~1/m.',
  'cases':{f'm{m}':case(m) for m in [6,8,10,12,20,50,100]},
  'asymptotics':{
    'A_m':'m^2',
    'rod_flux':'2/(1+2m^2)',
    'total_flux':'2m/(1+2m^2) ~ 1/m',
    'perimeter':'m*pi/sqrt(1+2m^2) -> pi/sqrt(2)',
    'volume_proxy':'2*pi^2*total_flux ~ 2*pi^2/m'},
  'scientific_interpretation':(
    'This is evidence against a BUILD proof based only on finite constant-curvature rod ODEs plus local smooth corner closure. The obstruction, if true, must use global base filling, horizontal traceless Ricci away from rods, determinant eigenfunction/spectral scale, holonomy/twist/non-diagonal fiber effects, Chern-Weil energy, or higher-order/global analytic matching.'),
  'not_established':[
    'No global base metric with these collars is constructed.',
    'No full Ricci pinching inequality is checked on the interior/collar overlaps.',
    'No collapse counterexample to Yau-26 or to P_4^+ is obtained.',
    'The separated same-circle transfer still has mu<1 for A>0; the formal polygon configuration assumes alternating adjacent rods absorb the edge bubble instead of closing the same circle at a second bolt.'
  ]
}

HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.abspath(os.path.join(HERE,'..','data','step19_finite_rod_corner_matching.json'))
os.makedirs(os.path.dirname(OUT),exist_ok=True)
with open(OUT,'w') as f: json.dump(reports,f,indent=2)
print(json.dumps({
    'title':reports['title'],
    'answer':reports['answer_at_tested_formal_level'],
    'sample_m6':reports['cases']['m6'],
    'sample_m100_summary':{k:reports['cases']['m100'][k] for k in ['m','common_rod_data','total_flux','volume_proxy_2pi2_total_flux','perimeter_sum_mL','all_corners_unimodular_diagonal']},
    'saved':OUT}, indent=2))
