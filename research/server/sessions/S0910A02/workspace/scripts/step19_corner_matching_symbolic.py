"""
Step 19 (S0910A02): symbolic corner matching for the diagonal toric ansatz.

We test whether a globally diagonal fiber ansatz is locally compatible with the
smooth fixed-point corner conditions and what exact Ric=g imposes on the first
corner jets.  Coordinates are a local corner chart for a T^2 fixed point with
adjacent collapsing circles p=0 and q=0:

    g = dr^2 + mu(r,t)^2 dt^2 + p(r,t)^2 dtheta^2 + q(r,t)^2 dphi^2.

The smoothness source (Toric-Einstein... Lemma 2.2) implies, in this gauge,
    mu^2 even, mu(0,t)=1,
    p^2 in r^2 + r^4 R_even,
    q^2 in t^2 mu(r,0)^2 + t^4 R_even,
    cross fiber term b=0 is allowed.
Thus the lowest nontrivial diagonal jets are
    mu = 1 + u r^2 + O(4),
    p  = r + a r^3 + O(5),
    q  = t(1+u r^2) + b t^3 + O(5).
The coefficient u encodes base edge curvature K_B|_{p=0}=-2u.

We compute the total Ricci endomorphism for the double-warped metric using
warped-product formulas and expand along t=z r. Exact Ric=g to zeroth order
should hold for all z; this gives algebraic corner matching conditions.
"""
import json, os
import sympy as sp

r,t,z=sp.symbols('r t z')
u,a,b=sp.symbols('u a b')

mu=1+u*r**2
p=r+a*r**3
q=t*(1+u*r**2)+b*t**3

# Base metric dr^2 + mu^2 dt^2
mur=sp.diff(mu,r); mut=sp.diff(mu,t)
K=-sp.diff(mu,r,2)/mu

def hess(f):
    fr,ft=sp.diff(f,r),sp.diff(f,t)
    frr,frt,ftt=sp.diff(f,r,2),sp.diff(f,r,t),sp.diff(f,t,2)
    Hrr=frr
    Hrt=frt - (mur/mu)*ft
    Htt=ftt + mu*mur*fr - (mut/mu)*ft
    return Hrr,Hrt,Htt

def lap(f):
    Hrr,Hrt,Htt=hess(f)
    return Hrr + Htt/mu**2

def inner(f,g):
    return sp.diff(f,r)*sp.diff(g,r) + sp.diff(f,t)*sp.diff(g,t)/mu**2

Hp=hess(p); Hq=hess(q)
# Total horizontal Ricci endomorphism matrix in coordinate basis.  Since g_B is diag(1,mu^2):
RicH_rr=K - Hp[0]/p - Hq[0]/q
RicH_rt=0 - Hp[1]/p - Hq[1]/q
RicH_tt=K*mu**2 - Hp[2]/p - Hq[2]/q
A_rr=RicH_rr
A_rt=RicH_rt/mu**2  # one-index mixed component row r col t? offdiag must vanish anyway
A_tt=RicH_tt/mu**2
rp= -lap(p)/p - inner(p,q)/(p*q)
rq= -lap(q)/q - inner(p,q)/(p*q)

exprs={'RicH_rr_minus1':sp.simplify(A_rr-1),
       'RicH_tt_minus1':sp.simplify(A_tt-1),
       'RicH_rt':sp.simplify(RicH_rt),
       'rp_minus1':sp.simplify(rp-1),
       'rq_minus1':sp.simplify(rq-1),
       'K_corner':sp.simplify(K)}

# Expand along t=z*r through O(r^0) and O(r^1/r^2 as available.
path_expansions={}
constant_terms={}
for name,e in exprs.items():
    er=sp.simplify(e.subs(t,z*r))
    # Laurent series around r=0.  RemoveO; ask to order 3 to see leading residual.
    ser=sp.series(er, r, 0, 3).removeO().expand()
    path_expansions[name]=str(sp.factor(ser))
    constant_terms[name]=str(sp.factor(ser.coeff(r,0)))

# Solve exact zeroth-order conditions.  Offdiag RicH_rt has leading r*z*(...) maybe; constant zero automatically.
conditions=[sp.factor(sp.sympify(constant_terms['RicH_rr_minus1'])),
            sp.factor(sp.sympify(constant_terms['RicH_tt_minus1'])),
            sp.factor(sp.sympify(constant_terms['rp_minus1'])),
            sp.factor(sp.sympify(constant_terms['rq_minus1']))]
sol=sp.solve(conditions, [a,b,u], dict=True)

# Express conditions in terms of A=-K_edge=2u and compare with rod ODE coefficient b=-(1+2A)/6.
A=sp.symbols('A')
rod_b=-(1+2*A)/6
rod_a_same=-(1+2*A)/6  # if the adjacent edge had the same edge curvature in its own Fermi gauge
subA={u:A/2}
A_conditions=[str(sp.factor(c.subs(subA))) for c in conditions]

report={
  'title':'Step 19 diagonal toric fixed-corner lowest-jet matching',
  'smooth_diagonal_ansatz_scope':(
    'For adjacent labels ±e1, ±e2, a diagonal fiber matrix with p vanishing on e1-rods and q on e2-rods satisfies the local smoothness parity conditions of Lemma 2.2: p^2=r^2+r^4 even, q^2=t^2 mu(r,0)^2+t^4 even, b=0 in r^2 t^2 R_even. This confirms local smoothness of the diagonal ansatz at standard-basis corners; it does not cover arbitrary labels.'),
  'jet_ansatz':{'mu':'1+u r^2','p':'r+a r^3','q':'t(1+u r^2)+b t^3'},
  'base_edge_curvature':'K_B|_{p=0}= -2u, so A=-K=2u',
  'path_expansions_t_equals_zr':path_expansions,
  'constant_terms':constant_terms,
  'zeroth_order_conditions_equal_zero': [str(sp.factor(c)) for c in conditions],
  'solutions_for_exact_Ric_eq_g_to_order0': [{str(k):str(sp.factor(v)) for k,v in s.items()} for s in sol],
  'conditions_with_A_equals_2u': A_conditions,
  'rod_ODE_expected_b_on_p0_edge':'b = -(1+2A)/6 = '+str(rod_b),
  'interpretation':(
    'The corner zeroth-order equations are consistent for arbitrary u/A once a and b are chosen as exact functions of u. With A=-K_B(0)=2u, both a and b equal -(2A+1)/6, exactly the Step-15 rod ODE cubic coefficient for a constant-curvature rod. Thus the standard-basis diagonal corner imposes no lowest-jet cap on A: adjacent large-negative-curvature rods can meet smoothly to this order. Any obstruction must enter through higher jets, finite-length matching/holonomy, nonlocal polygon compatibility, the spectral/eigenfunction condition, or through the full matrix/twist system.'),
  'caution':'This is a lowest-jet exact-Einstein corner calculation, not a pinched global construction and not a proof that all large-A rods close.'
}

HERE=os.path.dirname(os.path.abspath(__file__))
OUT=os.path.abspath(os.path.join(HERE,'..','data','step19_corner_matching_symbolic.json'))
os.makedirs(os.path.dirname(OUT),exist_ok=True)
with open(OUT,'w') as f:
    json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
print('Saved',OUT)
