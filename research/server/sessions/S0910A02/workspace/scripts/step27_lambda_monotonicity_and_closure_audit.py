"""
Step 27: Lambda-restored H3 cohomogeneity-one audit.

Purpose: critically consolidate Step 26's diagonal Heisenberg model by restoring
Einstein constant Lambda, checking the CH^2 negative witness, and recording the
positive-branch monotonicity/closure consequences at the exact scope justified by
the algebra.

The model is
    g = dt^2 + a(t)^2(theta1^2+theta2^2) + c(t)^2 theta3^2,
    [E1,E2] = E3,
with b=c/a^2, k1=a'/a, k3=c'/c, H=2k1+k3.
"""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

b, k1, k3, Lam, delta, B = sp.symbols('b k1 k3 Lambda delta B', real=True)
H = 2*k1 + k3
rate = k3 - 2*k1
T2 = 2*k1**2 + k3**2
S = b**2 + 4*k1**2 + 8*k1*k3
C = S + 4*Lam

# Exact Ric=Lambda vertical ODEs.
k1p = -Lam - b**2/2 - H*k1
k3p = -Lam + b**2/2 - H*k3
bp_over_b = rate

def simp(x):
    return sp.factor(sp.simplify(x))

# Constraint preservation: b' = b*rate.
Cp = sp.diff(C, b)*(b*rate) + sp.diff(C, k1)*k1p + sp.diff(C, k3)*k3p

# Algebraic certificates.
T_cert = simp(2*T2 - (b**2 + 4*Lam) - (2*H**2 - C))
rate_cert = simp(4*rate**2 - 5*(b**2 + 4*Lam) - (4*(3*k1+k3)**2 - 5*C))

# Sectional curvatures under exact vertical equations; K12 is independent of derivatives.
K01 = simp(-(k1p + k1**2))
K03 = simp(-(k3p + k3**2))
K12 = simp(-sp.Rational(3,4)*b**2 - k1**2)
K13 = simp(sp.Rational(1,4)*b**2 - k1*k3)
ric0_check = simp(2*K01 + K03)
ric1_check = simp(K01 + K12 + K13)
ric3_check = simp(K03 + 2*K13)

# CH^2 horosphere witness in the negative branch.
ch2_vals = {Lam: sp.Rational(-3,2), b: sp.Integer(1), k1: sp.Rational(-1,2), k3: sp.Integer(-1)}
ch2 = {
    'Lambda': '-3/2',
    'b': '1',
    'k1': '-1/2',
    'k3': '-1',
    'H': str(simp(H.subs(ch2_vals))),
    'C_Lambda': str(simp(C.subs(ch2_vals))),
    'd_log_b': str(simp(rate.subs(ch2_vals))),
    'k1_prime_from_vertical_ODE': str(simp(k1p.subs(ch2_vals))),
    'k3_prime_from_vertical_ODE': str(simp(k3p.subs(ch2_vals))),
    'T2': str(simp(T2.subs(ch2_vals))),
    'rhs_T_bound_(b2+4Lambda)/2': str(simp(((b**2+4*Lam)/2).subs(ch2_vals))),
    'rhs_rate_bound_5_over_4_(b2+4Lambda)': str(simp((sp.Rational(5,4)*(b**2+4*Lam)).subs(ch2_vals))),
    'sectional_curvatures_exact_model': {
        'K01': str(K01.subs(ch2_vals)),
        'K03': str(K03.subs(ch2_vals)),
        'K12': str(K12.subs(ch2_vals)),
        'K13=K23': str(K13.subs(ch2_vals)),
    },
    'interpretation': 'The negative Einstein horosphere data have constant bracket: C=0 and d(log b)=0 because b^2+4 Lambda=-5<0 makes the positive-branch lower bounds vacuous.'
}

# Positive exact sample used in Step 26, generalized as B>0 initial data.
positive_family = {
    'initial_data_for_any_B_positive': {
        'b0': 'B',
        'k1_0': 'B/2',
        'k3_0': '-B/2 - Lambda/B (so for Lambda=1 and B=20 this is -10.05)',
    }
}
# General choice k1=B/2, solve C=0 for k3:
# B^2 + 4(B/2)^2 + 8(B/2)k3 + 4 Lambda = 0.
k3_general = simp(-(B**2 + 2*Lam)/(2*B))
positive_family['initial_data_for_any_B_positive']['k3_general_with_k1=B/2'] = str(k3_general)
positive_family['initial_data_for_any_B_positive']['rate_general'] = str(simp((k3 - 2*k1).subs({b:B, k1:B/2, k3:k3_general})))
positive_family['initial_data_for_any_B_positive']['T2_general'] = str(simp(T2.subs({b:B, k1:B/2, k3:k3_general})))
positive_family['initial_data_for_any_B_positive']['C_check'] = str(simp(C.subs({b:B, k1:B/2, k3:k3_general})))

# Pinched loss certificate. If rho_i in [Lambda-delta,Lambda+delta], then S <= -4 Lambda + 8 delta.
S_upper_assumption = 'S=b^2+4k1^2+8k1k3 <= -4 Lambda + 8 delta (from rho0,rho1,rho3 in [Lambda-delta,Lambda+delta])'
pinched = {
    'eliminated_relation': 'S = 2 rho0 - 4 rho1 - 2 rho3, hence S <= -4 Lambda + 8 delta under |rho_i-Lambda|<=delta',
    'T_bound': '|T|^2 >= (b^2+4 Lambda-8 delta)/2 whenever the right side is meaningful',
    'rate_bound': '|d log b/dt|^2 >= (5/4)(b^2+4 Lambda-8 delta) whenever the right side is meaningful',
    'normalized_positive_threshold': 'For Lambda=1 and delta<1/2, the rate lower bound is positive even at b=0: |d log b/dt| >= sqrt(5(1-2 delta)).',
    'exact_positive_threshold': 'For delta=0, Lambda>0, |d log b/dt| >= sqrt(5 Lambda) everywhere and |d(1/b)/dt| >= sqrt(5)/2 on {b>0}.',
}

# Closure theorem scope, formulated as mathematical text, not checked by sympy.
closure_scope = {
    'periodic_orbit_space': {
        'statement': 'No C^1 positive periodic b can satisfy |(log b)\'|^2 >= c0>0. Hence no exact Ric=Lambda>0, or pinched Lambda>0 with delta<Lambda/2, diagonal H3 model over S^1.',
        'proof': 'The derivative of log b is continuous and never zero, so it has constant sign; log b is strictly monotone, contradicting periodicity. Equivalently a positive periodic C^1 function has a critical point.',
    },
    'two_center_bolt_interval': {
        'statement': 'If the only smooth compactification allowed at both finite ends is collapse of the central circle with a -> a0>0 and c -> 0, then b=c/a^2 -> 0 at both ends, so an interior maximum of b exists; the positive rate lower bound forbids it.',
        'fidelity_warning': 'This is not yet a classification of every possible singular orbit for a nilmanifold principal orbit. It proves the standard periodic/two-center-bolt diagonal closures and identifies the endpoint-classification needed before saying all closed diagonal H3 cohomogeneity-one manifolds are excluded.',
    },
    'large_b_shell': {
        'exact_Lambda_nonnegative': 'On {b>=B}, |d(1/b)/dt| = |d log b/dt|/b >= sqrt(5)/2, so a monotone component reaching arbitrarily large b has thickness <= 2/(sqrt(5) B) from b=B to b=infinity.',
        'curvature_concentration': 'The sectional curvature K12 = -3 b^2/4 - k1^2 always satisfies |K12| >= 3 b^2/4; large nonabelian bracket is a thin high-curvature shell in the positive model.',
    }
}

out = {
    'title': 'Step 27 Lambda-restored H3 monotonicity and closure audit',
    'scope': 'Diagonal cohomogeneity-one H3 model; not a general Ricci-pinched collapse theorem and not a Yau-26 proof/refutation.',
    'exact_Ricci_Lambda_equations': {
        'Ric11=Ric22=Lambda': "k1' = -Lambda - b^2/2 - (2k1+k3) k1",
        'Ric33=Lambda': "k3' = -Lambda + b^2/2 - (2k1+k3) k3",
        'b_evolution': "(log b)' = k3 - 2 k1",
        'Ric00=Lambda_constraint': 'C_Lambda = b^2 + 4 k1^2 + 8 k1 k3 + 4 Lambda = 0',
        'constraint_derivative': str(simp(Cp)),
        'constraint_preservation': "C_Lambda' = -2(2k1+k3) C_Lambda",
    },
    'algebraic_certificates': {
        'T_identity': '2|T|^2-(b^2+4 Lambda) = 2(2k1+k3)^2 - C_Lambda',
        'T_identity_check_zero': str(T_cert),
        'rate_identity': "4((log b)')^2 - 5(b^2+4 Lambda) = 4(3k1+k3)^2 - 5 C_Lambda",
        'rate_identity_check_zero': str(rate_cert),
        'exact_consequences_on_C=0': [
            '|T|^2 >= (b^2+4 Lambda)/2',
            "|d log b/dt|^2 >= (5/4)(b^2+4 Lambda)",
        ],
    },
    'pinched_loss': pinched,
    'sectional_curvature_check': {
        'K01_after_vertical_equations': str(K01),
        'K03_after_vertical_equations': str(K03),
        'K12': str(K12),
        'K13=K23': str(K13),
        'Ric0=2K01+K03': str(ric0_check),
        'Ric1=K01+K12+K13': str(ric1_check),
        'Ric3=K03+2K13': str(ric3_check),
        'large_b_lower_bound': '|Rm| >= |K12| >= 3 b^2/4 in this diagonal model.',
    },
    'CH2_negative_witness': ch2,
    'large_positive_local_family': positive_family,
    'closure_scope': closure_scope,
    'research_judgment': 'The Step-26 inequalities do contain a strong positive-branch model theorem: positive Lambda forbids a bracket plateau and makes ungraded H3 collapse a monotone high-curvature shell. The closed periodic/two-center-bolt diagonal models are excluded. A fully unconditional “no closed diagonal H3 cohomogeneity-one structure” statement still needs endpoint/singular-orbit classification; twist-active higher-base models remain outside this A=0 codimension-one calculation.'
}

path = Path(__file__).resolve().parents[1] / 'data' / 'step27_lambda_monotonicity_and_closure_audit.json'
path.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(out, indent=2))
print(f"\nSaved to {path}")
