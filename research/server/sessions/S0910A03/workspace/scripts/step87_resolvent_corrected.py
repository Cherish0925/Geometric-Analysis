#!/usr/bin/env python3
"""Step 87: CORRECTED massive-resolvent comparison with Riccati Fisher bound.

CORRECTION from TTCS verification:
  The Fisher information estimate I(t) <= N/(2t) + NK/2 is NOT valid for all t.
  The correct CD(-K,N) Riccati bound is:
    I(t) <= NK / (1 - e^{-2Kt})
  which satisfies I(t) ~ N/(2t) + NK/2 + ... for small t but grows differently.

  With kappa = 2K (our exact choice), the upper-bound integral evaluates exactly:
    C_kappa <= sqrt(NK)/(2K) * B(kappa/(2K), 1/2) = sqrt(N/K) = 2/sqrt(3+delta)

  This gives a clean, closed-form upper bound; equality for the actual resolvent norm is not asserted.
"""

import numpy as np
from scipy import integrate, optimize, special
import json
from pathlib import Path

results = {}

N_eff = 4  # effective Bakry-Emery dimension

# --- Part 1: Verify the Riccati Fisher bound ---

def fisher_riccati(t, N, K):
    """Correct CD(-K,N) Fisher bound: NK/(1-e^{-2Kt})."""
    if K * t < 1e-10:
        return N / (2*t)  # small-t limit
    return N * K / (1 - np.exp(-2*K*t))

def fisher_naive(t, N, K):
    """WRONG bound (small-t expansion only): N/(2t) + NK/2."""
    return N / (2*t) + N*K/2

# Verify on round cusp: sigma=2r, L = d_rr + 3d_r + e^{-2r}d_zz
# Radial Fisher info = 9 + 1/(2t) for t > 0
# (from conjugation phi = e^{-3r/2}y: I_rad = integral e^{3r}|phi_r|^2 / phi^2)
# At N=4, K=3: naive gives 2/t + 6, fails when 9 + 1/(2t) > 2/t + 6 i.e. t > 1/6
# Riccati gives 12/(1-e^{-6t})

t_test = np.array([0.01, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0])
K_cusp = 3.0

cusp_check = []
for t in t_test:
    riccati = fisher_riccati(t, N_eff, K_cusp)
    naive = fisher_naive(t, N_eff, K_cusp)
    rad_lower = 9 + 1/(2*t)  # known lower bound from radial part
    cusp_check.append({
        't': float(t),
        'riccati_bound': round(float(riccati), 6),
        'naive_WRONG': round(float(naive), 6),
        'radial_lower': round(float(rad_lower), 6),
        'naive_fails': bool(naive < rad_lower - 1e-10),
        'riccati_valid': bool(riccati >= rad_lower - 1e-10),
    })

results['fisher_correction'] = {
    'cusp_test': cusp_check,
    'diagnosis': ('Naive bound I(t)<=N/(2t)+NK/2 fails for t > 1/(2(NK/2-N_radial)) = 1/6 '
                  'on the round cusp. Riccati bound NK/(1-e^{-2Kt}) is always valid.'),
}

# --- Part 2: Exact resolvent constant via Beta function ---

def C_kappa_exact(kappa, N, K):
    """
    Closed-form upper bound obtained from the Fisher estimate:
    C_kappa <= sqrt(NK)/(2K) * B(kappa/(2K), 1/2)
    
    For kappa = 2K: B(1, 1/2) = Gamma(1)*Gamma(1/2)/Gamma(3/2) = sqrt(pi)/(sqrt(pi)/2) = 2
    Hence C_kappa <= sqrt(N/K).
    """
    a = kappa / (2*K)
    b = 0.5
    beta_val = special.beta(a, b)
    return np.sqrt(N * K) / (2*K) * beta_val

def C_kappa_at_2K(N, K):
    """When kappa = 2K, return the proved upper bound sqrt(N/K)."""
    return np.sqrt(N / K)

# Verify Beta function identity
K_test = 3.0
kappa_test = 6.0
C_exact = C_kappa_exact(kappa_test, N_eff, K_test)
C_simple = C_kappa_at_2K(N_eff, K_test)
C_numerical_int, _ = integrate.quad(
    lambda t: np.exp(-kappa_test * t) * np.sqrt(fisher_riccati(t, N_eff, K_test)),
    1e-15, 50, limit=200
)

results['resolvent_constant'] = {
    'formula': 'C_kappa <= sqrt(NK)/(2K) * B(kappa/(2K), 1/2)',
    'at_kappa_2K': 'C_{2K} <= sqrt(N/K)',
    'N': N_eff,
    'K_at_delta_0': K_test,
    'kappa_at_delta_0': kappa_test,
    'C_exact_beta': round(C_exact, 10),
    'C_simple_sqrt': round(C_simple, 10),
    'C_numerical_integration': round(C_numerical_int, 10),
    'agreement': bool(abs(C_exact - C_simple) < 1e-10 and abs(C_exact - C_numerical_int) < 1e-6),
    'beta_1_half': round(float(special.beta(1, 0.5)), 10),
    'should_be_2': True,
}

# --- Part 3: Corrected threshold computation ---

def ceiling_bound_corrected(delta):
    """
    B(delta) using the resolvent upper bound C_kappa <= 2/sqrt(3+delta).
    
    kappa = 6 + 2*delta
    f0 = 2*delta
    alpha = kappa + 2*f0^2/kappa = kappa + 8*delta^2/kappa
    C_kappa = 2/sqrt(3+delta)
    beta = 2*C_kappa*f0 = 4*delta*C_kappa = 8*delta/sqrt(3+delta)
    
    B <= (beta/2 + sqrt(beta^2/4 + alpha))^2
    """
    K = 3 + delta
    kappa = 2*K
    f0 = 2*delta
    
    alpha = kappa + 2*f0**2 / kappa  # = 2K + 4delta^2/K
    Ck = 2 / np.sqrt(K)
    beta = 2 * Ck * f0  # = 8*delta/sqrt(K)
    
    sqrtB = beta/2 + np.sqrt(beta**2/4 + alpha)
    B = sqrtB**2
    
    return B, alpha, beta, Ck

def gap_corrected(delta):
    """B(delta) - (12-8*delta). Negative means obstruction holds."""
    if delta <= 0:
        return 6.0 - 12.0
    B, _, _, _ = ceiling_bound_corrected(delta)
    return B - (12 - 8*delta)

# Find threshold
delta_star = optimize.brentq(gap_corrected, 0.01, 0.4)

results['corrected_threshold'] = {
    'delta_star': round(float(delta_star), 8),
    'B_at_threshold': round(float(ceiling_bound_corrected(delta_star)[0]), 8),
    'floor_at_threshold': round(float(12 - 8*delta_star), 8),
    'gap_at_threshold': round(float(gap_corrected(delta_star)), 12),
}

# --- Part 4: Detailed table ---
test_deltas = [0.0, 0.05, 0.10, 0.15, 0.20, 0.24, delta_star, 0.25, 0.30, 0.375, 0.50]
detail = []
for d in test_deltas:
    d_safe = max(d, 1e-15)
    B, alpha, beta, Ck = ceiling_bound_corrected(d_safe)
    floor_val = 12 - 8*d
    detail.append({
        'delta': round(float(d), 8),
        'kappa': round(float(6+2*d), 6),
        'C_kappa': round(float(Ck), 8),
        'alpha': round(float(alpha), 8),
        'beta': round(float(beta), 8),
        'ceiling_B': round(float(B), 8),
        'center_floor': round(float(floor_val), 8),
        'gap': round(float(B - floor_val), 8),
        'obstruction': bool(B < floor_val),
    })

results['detail_table'] = detail

# --- Part 5: Closed-form analysis ---

# The TTCS provides the closed-form ceiling:
# B(delta) = [4delta/sqrt(3+delta) + sqrt(2(3+delta) + 20delta^2/(3+delta))]^2
# Center floor: 12 - 8delta
# 
# At delta=0: B=6, floor=12, gap=-6.
# Leading order: B ~ 6 + (2+4sqrt(6)*2/sqrt(3))*delta = 6 + (2+8sqrt(2))*delta
# Floor ~ 12 - 8*delta
# Gap ~ -6 + (10 + 8sqrt(2))*delta

import sympy as sp
d = sp.Symbol('delta', positive=True)
K_s = 3 + d
kappa_s = 2*K_s
alpha_s = kappa_s + 8*d**2/kappa_s
Ck_s = 2/sp.sqrt(K_s)
beta_s = 2*Ck_s*2*d

B_s = (beta_s/2 + sp.sqrt(beta_s**2/4 + alpha_s))**2
floor_s = 12 - 8*d
gap_s = B_s - floor_s

# Series expansion
B_series = sp.series(B_s, d, 0, 3)
gap_series = sp.series(gap_s, d, 0, 3)

# Leading-order threshold
# gap ~ -6 + C1*delta where C1 = coefficient of delta in gap_series
C1 = float(gap_series.coeff(d, 1))
delta_leading = 6 / C1

results['closed_form'] = {
    'B_expression': 'B(delta) = [4delta/sqrt(3+delta) + sqrt(2(3+delta)+20delta^2/(3+delta))]^2',
    'B_series': str(B_series),
    'gap_series': str(gap_series),
    'linear_gap_coefficient': round(C1, 8),
    'leading_order_threshold': round(delta_leading, 8),
    'note': 'delta_star < leading-order because of quadratic and higher corrections',
}

# --- Part 6: Verify the Duhamel semigroup proof ---
# TTCS recommends the semigroup proof over Omori-Yau:
# e <= e^{-kappa T} P_T e + integral_0^T e^{-kappa t} P_t S dt
# As T -> infty, e^{-kappa T} P_T e -> 0 (since kappa>0 and e bounded, P_T e bounded).
# So e <= R_kappa S.

results['comparison_principle'] = {
    'method': 'Duhamel semigroup formula',
    'identity': 'e = e^{-kappa T} P_T e + integral_0^T e^{-kappa t} P_t [(-L+kappa)e] dt',
    'inequality': 'Since (-L+kappa)e <= S, and P_t is positivity-preserving: '
                  'e <= e^{-kappa T} P_T e + integral_0^T e^{-kappa t} P_t S dt',
    'limit': 'As T -> infty: e^{-kappa T} P_T e -> 0 (kappa>0, e bounded, P_T conserves mass). '
             'The integral converges to R_kappa S.',
    'conclusion': 'e <= R_kappa[kappa^2+8delta^2-2div_sigma V] everywhere.',
    'advantage': 'No Omori-Yau or maximum principle needed; only semigroup positivity + conservation.',
}

# --- Part 7: TTCS Ric_f^4 correction ---
# On the round cusp: Ric_B-Hess sigma = diag(-1,-3),
# but Ric_f^4 = Ric_B-Hess sigma-1/2 d sigma^2 = diag(-1,-3)-diag(2,0) = diag(-3,-3) = -3gamma.
# So the cusp satisfies CD(-3,4) exactly.

results['cusp_ric_f4_correction'] = {
    'Ric_B_minus_Hess_sigma': 'diag(-1,-3) on gamma=dr^2+e^{2r}dz^2, sigma=2r',
    'half_dsigma_squared': 'diag(2,0) since d sigma = 2dr',
    'Ric_f4': '-3gamma_B (not diag(-1,-3))',
    'CD_condition': 'CD(-3,4) sharp',
}

# --- Part 8: Complete ceiling and Step-88 floor interface ---
results['theorem'] = {
    'statement': (
        'CEILING THEOREM. Let (B^2, gamma_B, dmu=e^sigma dA) be a complete '
        'smooth weighted base with orbit map U: B -> H^2 satisfying the forced '
        'free-T2 OT equations, Ric_f^4 >= -(3+delta)gamma_B, weighted tension '
        '|tau_sigma(U)| <= 2delta, and bounded orbit energy e=|dU|^2 with '
        'e -> 0 at all ends. Then sup e <= B(delta), where '
        'B(delta) = [4delta/sqrt(3+delta) + '
        'sqrt(2(3+delta)+20delta^2/(3+delta))]^2. Step 88 supplies a '
        'reflection-free floor 12-8delta for quotient cylinders with two exact '
        'outward-expanding ends.'
    ),
    'delta_star': round(float(delta_star), 6),
    'proof_chain': [
        '1. Forced Bochner (Steps 85-86): (1/2)Le >= (1/2)e^2-(3+delta)e-4delta^2+div_sigma V',
        '2. Massive comparison: (-L+kappa)e <= kappa^2+8delta^2-2div_sigma V, kappa=6+2delta',
        '3. Riccati Fisher: I(t) <= NK/(1-e^{-2Kt}) under CD(-K,N) [corrected from naive bound]',
        '4. Resolvent upper bound: C_kappa <= 2/sqrt(3+delta) via Beta(1,1/2)=2; equality is not asserted',
        '5. Duhamel comparison: e <= R_kappa[source] on complete manifold [semigroup positivity]',
        '6. Quadratic closure + reflected-center or Step-88 minimal-separator floor: delta >= delta_star'
    ],
    'scope': ('Free-T2 orthogonally transitive complete weighted bases; Step 88 '
              'removes reflection when the quotient is a cylinder with two exact '
              'outward-expanding ends. Does not cover connection twist, singular '
              'orbits, fully non-symmetric graph metrics, N#N S3 necks, or the '
              'positive branch.'),
}

# --- Output ---
out_path = Path('workspace/data/step87_resolvent_corrected.json')
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(results, indent=2, default=str), encoding='utf-8')
print(json.dumps(results, indent=2, default=str))
print(f'\nwrote {out_path}')
