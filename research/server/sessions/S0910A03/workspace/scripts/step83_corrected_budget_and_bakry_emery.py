#!/usr/bin/env python3
"""
Step 83: Corrected K-production budget and Bakry-Émery Ricci analysis.

Corrections from TTCS:
1. Cov(H,|b|^2) is INDEFINITE (not positive)
2. <h^2(v-2u)> is INDEFINITE (pointwise u<=0,v>=0 not guaranteed)
3. Budget is -6+2delta, not -18
4. y >= 0 IS proven for delta < 3

New investigation: Bakry-Émery weighted Ricci Ric^sigma_B on the 2D base.
From the base identity E_B = Ric(gamma_B) - Hess(sigma) - (1/2)d sigma^2 
- (1/2)U*h_{H^2} + 3 gamma_B, exact Einstein gives:
Ric(gamma_B) + Hess(sigma) = 2 Hess(sigma) + (1/2)d sigma^2 + (1/2)U*h_{H^2} - 3 gamma_B

This is the effective (Bakry-Émery-type) Ricci of the orbit-weighted base.
On the round cusp (sigma=2r): Hess(sigma) = 2 diag(0,1) in Gaussian coords,
so Ric_B + Hess sigma = (-1,0) + (0,2) = (-1,2) — NOT semi-positive.

On general backgrounds the orbit stress U*h_{H^2} is positive semi-definite
but Hess(sigma) can have negative eigenvalues.
"""
import numpy as np
import json
from pathlib import Path

# ---- Part A: Corrected sign structure ----

sign_structure = {
    'proven_positive': {
        'IBP_orbit_velocity': (
            'int_0^R m[f\' + 2(x+y)f] dr = m(R)f(R) + int 2ymf dr >= 0 '
            'since y >= 0 (proven for delta < 3) and f = <|b|^2> >= 0. '
            'This covers ONLY the first two terms of Phi.'
        ),
        'y_nonnegativity': (
            'y\' = 6 - <E_orb> - y(x+y). For delta < 3: 6-<E_orb> >= 6-2delta > 0. '
            'At any zero of y from above, y\' > 0, contradiction. Hence y >= 0.'
        ),
    },
    'indefinite': {
        'Cov(H,|b|^2)': 'Sign depends on spatial correlation of H and |b|^2',
        'h^2(v-2u)': (
            'Pointwise u <= 0 and v >= 0 NOT guaranteed. '
            'Only averages x = <u> <= 0 and y = <v> >= 0. '
            'Covariance decomposition: <h^2(v-2u)> = <h^2>(y-2x) + Cov(h^2,v-2u), '
            'and the covariance can make the whole term negative.'
        ),
        'tension_h_A_b': 'Full sign indefinite',
        'Cov(v-u,k)': 'Full sign indefinite',
    },
    'forcing': {
        'bound': '|2<eps,b> + 2<h E_rs>| <= C delta (f^{1/2} + <h^2>^{1/2})',
        'not_uniformly_small': 'If f or <h^2> diverge, forcing can be O(1) even as delta -> 0',
    },
}

# ---- Part B: Corrected budget ----

budget = {
    'integrating_factor_identity': 'm(R)K(R) - 12 = int_0^R m Phi dr',
    'return_condition': 'K(R) <= 6 + 2delta, m(R) <= 1',
    'necessary_inequality': 'int_0^R m Phi dr <= m(R)(6+2delta) - 12 <= -6 + 2delta',
    'separating_positive': (
        'P_orb = m(R)f(R) + int 2ymf dr >= 0. '
        'Remaining terms N satisfy N <= -6 + 2delta - P_orb <= -6 + 2delta. '
        'Cannot claim N <= -18 without proving P_orb >= 12.'
    ),
    'early_production': (
        'The center expansion m(r)K(r) - 12 = [<|tau|^2> + 3Var(k)/16]r^2 + O(r^4). '
        'This coefficient CAN be zero (for constant-speed loops with Var(k)=0, '
        'if tau=0, i.e., geodesic circles in H^2 with h=0). '
        'The k=2 rotating loop has tau^2=16, giving coefficient 16+0=16 > 0, '
        'but this is model-specific.'
    ),
}

# ---- Part C: Bakry-Émery analysis on the round cusp ----

# On the round cusp: g = dr^2 + cosh^2(r) dz^2, sigma = 2r
# Hess(sigma):
# In coordinates: sigma = 2r, sigma_r = 2, sigma_rr = 0, sigma_rz = 0, sigma_zz = 0
# Hess(sigma)_rr = sigma_rr - Gamma^k_rr sigma_k = 0 - 0 = 0
# Hess(sigma)_zz = sigma_zz - Gamma^r_zz sigma_r = 0 - (-sinh r cosh r)(2) = 2 sinh r cosh r
# Hess(sigma)_rz = 0

# In orthonormal frame: e_0 = dr, e_1 = (1/cosh r) dz
# Hess(sigma)_00 = 0
# Hess(sigma)_11 = Hess(sigma)_zz / cosh^2(r) = 2 sinh r cosh r / cosh^2(r) = 2 tanh r

# Ric(gamma_B) for g = dr^2 + cosh^2(r) dz^2:
# K_gauss = -cosh''(r)/cosh(r) = -cosh(r)/cosh(r) = -1
# Ric_B = -1 * g_B, so Ric_{00} = -1, Ric_{11} = -1

# d sigma tensor d sigma / 2: (1/2)(2)^2 dr tensor dr = 2 dr^2
# In orthonormal frame: (d sigma)^2/2 = (sigma_r e_0)^2 / 2 = 2 delta_{00}

# U*h_{H^2}: On the round cusp, U is constant (M = identity), so this is 0.

# Check: E_B = Ric_B - Hess sigma - (1/2)(d sigma)^2 - (1/2)U*h_{H^2} + 3 g_B
# = diag(-1,-1) - diag(0, 2 tanh r) - diag(2, 0) - 0 + diag(3, 3)
# = diag(-1-0-2+3, -1-2 tanh r - 0 + 3) = diag(0, 2-2 tanh r) = diag(0, 2 sech^2 r / ...)

# Hmm let me recompute: -1 - 2 tanh r + 3 = 2 - 2 tanh r = 2(1-tanh r) = 2 sech^2 r / (1+tanh r)
# Actually: 2 - 2 tanh r = 2(1 - tanh r) which is > 0 for all r. Good.
# E_B_11 = 2(1-tanh r) -> 0 as r -> infinity. This is correct: the cusp is asymptotically Einstein.

# Now the Bakry-Émery Ricci: Ric^sigma_B = Ric_B + Hess sigma
# = diag(-1, -1) + diag(0, 2 tanh r) = diag(-1, -1 + 2 tanh r)

# At r=0: diag(-1, -1). Both eigenvalues negative.
# At r->inf: diag(-1, -1 + 2) = diag(-1, 1). One negative, one positive.

# So even on the exact round cusp, Ric^sigma_B has a negative eigenvalue (-1) in the r-direction.
# This is expected: the cusp is negatively curved.

# For Bochner-type arguments, we need Ric^sigma >= -kappa for some kappa.
# On the cusp: kappa = 1 (the r-eigenvalue is -1).

r_arr = np.linspace(0, 5, 100)
hess_sigma_rr = np.zeros_like(r_arr)
hess_sigma_11 = 2 * np.tanh(r_arr)
ric_B_rr = -np.ones_like(r_arr)
ric_B_11 = -np.ones_like(r_arr)
bakry_emery_rr = ric_B_rr + hess_sigma_rr  # = -1
bakry_emery_11 = ric_B_11 + hess_sigma_11  # = -1 + 2 tanh r

# For the PERTURBED cusp with nontrivial orbit map:
# E_B = 0 gives Ric_B + Hess sigma = -(1/2)d sigma^2 - (1/2)U*h_{H^2} + 3 g_B + Hess sigma
# Wait, let me re-derive from E_B = 0:
# Ric_B = Hess sigma + (1/2)d sigma^2 + (1/2)U*h_{H^2} - 3 g_B
# So Ric^sigma_B = Ric_B + Hess sigma = 2 Hess sigma + (1/2)|d sigma|^2 g_B^{-1}tensor + (1/2)U*h_{H^2} - 3 g_B
# 
# Actually: Ric_B + Hess sigma = [Hess sigma + (1/2)d sigma tensor d sigma + (1/2)U*h_{H^2} - 3 g_B] + Hess sigma
# = 2 Hess sigma + (1/2)d sigma tensor d sigma + (1/2)U*h_{H^2} - 3 g_B

# On the cusp: 2*diag(0, 2 tanh r) + diag(2,0) + 0 - 3*diag(1,1)
# = diag(0 + 2 - 3, 4 tanh r + 0 - 3) = diag(-1, 4 tanh r - 3)

# At r=0: diag(-1, -3). At r=inf: diag(-1, 1). 
# Hmm, the 11 component is now 4 tanh r - 3, which crosses zero at tanh r = 3/4, r = atanh(3/4) ≈ 0.973.

crossover_r = np.arctanh(3.0/4)
bakry_emery_exact_11 = 4*np.tanh(r_arr) - 3

# With orbit stress U*h_{H^2}: this adds a positive semi-definite term.
# For a rotating loop at radius d* with e_{H^2} = 12: the stress has eigenvalues
# depending on the direction of the orbit map gradient.
# The maximum eigenvalue is at most e_{H^2} = 12 (per the Step 79 normalization).
# This can make the Bakry-Émery Ricci more positive.

# So the perturbative question is: does nontrivial orbit map make Ric^sigma_B more positive?
# Answer: yes, through the (1/2)U*h_{H^2} term. But the Hess sigma term can go either way
# when the base metric deforms.

bakry_emery_data = {
    'cusp_background': {
        'metric': 'dr^2 + cosh^2(r) dz^2',
        'sigma': '2r (orbit area = e^{2r})',
        'Hess_sigma_orthonormal': {'rr': 0.0, '11': '2 tanh r'},
        'Ric_B_orthonormal': {'rr': -1.0, '11': -1.0},
        'bakry_emery_rr': -1.0,
        'bakry_emery_11_formula': '-1 + 2 tanh r',
        'bakry_emery_11_at_r0': -1.0,
        'bakry_emery_11_at_rinf': 1.0,
        'note': 'r-eigenvalue is universally -1 on the round cusp',
    },
    'exact_einstein_identity': {
        'formula': 'Ric^sigma_B = 2 Hess sigma + (1/2) d sigma tensor d sigma + (1/2) U*h_{H^2} - 3 g_B',
        'cusp_check': {
            'rr': '-1 = 0 + 2 + 0 - 3',
            '11': '4 tanh r - 3 = 4 tanh r + 0 + 0 - 3',
        },
        'crossover_r': float(crossover_r),
        'note': 'Without orbit stress, 11-component crosses zero at r ≈ 0.973',
    },
    'orbit_stress_effect': {
        'sign': 'positive semi-definite (U*h_{H^2} >= 0)',
        'magnitude': 'up to e_{H^2} = 12 for constant-speed loops',
        'consequence': 'Can make Ric^sigma_B more positive in orbit-gradient direction',
    },
    'obstruction_assessment': (
        'The r-eigenvalue of Ric^sigma_B is -1 on the round cusp, '
        'indicating that the Bochner approach cannot give a positive '
        'lower bound. It can only give Ric^sigma >= -1 (or worse), '
        'which yields exponential growth estimates, not monotonicity. '
        'The orbit stress improves the tangential direction but does '
        'not help the radial direction. Therefore the Bochner route '
        'does NOT provide a monotone functional excluding the K-drop.'
    ),
}

# ---- Part D: What the corrected analysis establishes ----

conclusion = {
    'proven': [
        'K\' + 2xK = Phi (exact kinematic identity)',
        'y >= 0 for delta < 3 (from y\' equation)',
        'IBP: int mu [f\'+2(x+y)f] dr = m(R)f(R) + int 2ymf dr >= 0',
        'Necessary budget: int m Phi dr <= -6 + 2delta for return',
        'K\'\'(0) >= 72 (universal initial worsening)',
        'K\'(0) = 0 (by reflection symmetry)',
        'The exact constant-exit obstruction from Step 79 convexity',
    ],
    'not_proven': [
        'No Lyapunov/monotone functional excluding K-drop in full OT system',
        'No universal lower bound on P_orb (orbit velocity contribution)',
        'No control on Cov(H,|b|^2), h^2(v-2u), or tension terms',
        'No Bochner obstruction (Ric^sigma_B has -1 eigenvalue)',
        'No uniform control on area gradient growth h^2',
    ],
    'status': (
        'The K-production framework organizes the problem but does NOT '
        'close it. The integrating-factor form correctly isolates the '
        'positive orbit-velocity contribution, but the remaining terms '
        'are all indefinite. No monotone quantity, Lyapunov function, '
        'Bochner estimate, or finite-moment closure has been found to '
        'prevent the K-drop. The problem remains genuinely open: the '
        'connector may or may not exist.'
    ),
    'mechanisms_for_K_drop': [
        'Phase flip: b aligns with tau later, making -2<tau,b> negative',
        'Area gradient growth: h^2 increase lowers K directly',
        'Weight redistribution: d mu concentrates on low-k regions',
        'Covariance engineering: Cov(v-u,k) made negative',
        'Noether-compatible oscillation: zero-mean but large L^2 orbit velocity',
    ],
}

out = {
    'sign_structure_corrected': sign_structure,
    'budget_corrected': budget,
    'bakry_emery_analysis': bakry_emery_data,
    'conclusion': conclusion,
}

path = Path(__file__).resolve().parents[1]/'data'/'step83_corrected_budget.json'
path.write_text(json.dumps(out, indent=2, default=str), encoding='utf-8')
print(json.dumps(out, indent=2, default=str))
print(f'\nwrote {path}')
