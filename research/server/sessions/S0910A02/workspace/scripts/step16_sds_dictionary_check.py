"""
Step 16 (S0910A02): algebraic check that the Step-15 separated edge germ
is Euclidean Schwarzschild-de Sitter, and record exact cone-angle/volume
formulas for the cohomogeneity-one rod class.

We use the normalized positive Einstein convention Ric = g in dimension 4.
The usual Euclidean Schwarzschild-de Sitter metric is
    G = f(rho) d tau^2 + f(rho)^(-1) d rho^2 + rho^2 g_{S^2},
    f(rho)=1-2M/rho-rho^2/3,
which satisfies Ric(G)=G.  If rho_h is the smaller positive horizon and
rho_c the larger, set a=rho/rho_h and rescale the S^2 metric so its sectional
curvature is kappa=1/rho_h^2.  In the arclength coordinate dr=d rho/sqrt(f),
the metric has the Step-15 form dr^2+p(r)^2 dtheta^2+a(r)^2 g_{S^2(kappa)}.
The normalized first-bolt smoothness fixes p'(0)=1, and A=a''(0)=(kappa-1)/2.
"""
import json, math
from pathlib import Path
import sympy as sp

A = sp.symbols('A', nonnegative=True)
kappa = 1 + 2*A
rho_h = 1/sp.sqrt(kappa)
# From f(rho_h)=0: 2M/rho_h = 1-rho_h^2/3.
M = rho_h/2 * (1 - rho_h**2/3)
# Factor the cubic rho^3 - 3 rho + 6 M with root rho_h.
rho = sp.symbols('rho')
cubic = rho**3 - 3*rho + 6*M
factor = sp.factor(cubic)
rho_c = (-rho_h + sp.sqrt(12 - 3*rho_h**2))/2  # larger positive root from quotient
aplus = sp.simplify(rho_c/rho_h)
aplus_expected = (-1 + sp.sqrt(9 + 24*A))/2
aplus_diff = sp.simplify(aplus - aplus_expected)

f = 1 - 2*M/rho - rho**2/3
fp = sp.diff(f, rho)
# surface gravities absolute values at horizons: |f'|/2. ratio independent of 1/2.
mu = sp.simplify(abs(1)) # placeholder; use symbolic sign-aware formula below
# f'(rho_h)>0 for 0<=M<1/(3sqrt3); f'(rho_c)<0.
mu_symbolic = sp.simplify((-fp.subs(rho, rho_c))/(fp.subs(rho, rho_h)))
mu_in_a = sp.simplify((2*aplus_expected + 1)/(aplus_expected*(aplus_expected + 2)))
mu_diff = sp.simplify(mu_symbolic - mu_in_a)

# A expressed from rho_h; Nariai A=0 -> rho_h=1, M=1/3; M->0 -> rho_h->0, A->infty.
# Volumes in Step-15 convention for smooth A=0 S2xS2: flux per rod=2, 4 rods total flux 8, Vol=2pi^2*8=16pi^2.
# SdS full smoothness if both horizons have same theta period -> mu=1, i.e. A=0.
mu_sq_minus_one = sp.factor(sp.simplify(mu_in_a**2 - 1))
# solve mu=1 for A>=0
mu_minus_one = sp.factor(sp.simplify(mu_in_a - 1))

samples=[]
for Aval in [0, 0.01, 0.1, 0.5, 1, 4, 9, 100, 10000]:
    kappav = 1+2*Aval
    rh = 1/math.sqrt(kappav)
    Mv = rh/2*(1-rh*rh/3)
    rc = (-rh+math.sqrt(12-3*rh*rh))/2
    av = rc/rh
    muv = (2*av+1)/(av*(av+2))
    samples.append({
        'A': Aval,
        'kappa': kappav,
        'rho_h': rh,
        'M': Mv,
        'rho_c': rc,
        'a_plus': av,
        'mu_surface_gravity_ratio': muv,
        'cone_angle_second_if_first_smooth': 2*math.pi*muv,
        'rod_flux_first_rod': 2/(1+2*Aval),
    })

report={
    'title':'Step 16 Schwarzschild-de Sitter dictionary check for separated edge germ',
    'normalized_convention':'Ric = g in dimension 4; f(rho)=1-2M/rho-rho^2/3',
    'symbolic_identities':{
        'rho_h':'1/sqrt(1+2A)',
        'M_from_horizon':str(sp.simplify(M)),
        'cubic_factorization':str(factor),
        'rho_c_over_rho_h_minus_step15_a_plus':str(aplus_diff),
        'surface_gravity_ratio_minus_step15_mu':str(mu_diff),
        'mu_minus_one':str(mu_minus_one),
        'mu_squared_minus_one':str(mu_sq_minus_one),
        'smooth_both_horizons_condition':'mu=1 iff A=0 in the A>=0 branch',
    },
    'limits':{
        'A_to_0':'rho_h=rho_c=1, M=1/3, Nariai/S2xS2 limit; mu=1; rod flux=2',
        'A_to_infty':'rho_h->0, M->0, rho_c->sqrt(3), a_plus~sqrt(6A), mu~2/a_plus->0; small black hole in round S4/de Sitter',
    },
    'singularity_interpretation':'If theta period is chosen to smooth the first S2 bolt, then at the second S2 bolt the same circle collapses with slope mu(A). For A>0 this is a codimension-2 edge cone of angle 2*pi*mu along an embedded S2, not an isolated R4/Gamma singularity.',
    'cohomogeneity_one_gap_mechanism':'Exact Einstein smooth closure at both ends forces A=0. A quantitative pinched theorem should control the change of the slope/holonomy matching under |Ric-g|<=delta; the cone-angle defect is O(1) when A>=A0>0 and cannot be hidden by small scale.',
    'samples':samples,
}
out=Path('Sessions/S0910A02/workspace/data/step16_sds_dictionary_check.json')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
print(f'Saved {out}')
