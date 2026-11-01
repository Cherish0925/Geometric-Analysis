"""Step 90 algebraic verification of the structured forced Bochner bounds."""
from pathlib import Path
import json
import sympy as sp

# Symbols are nonnegative magnitudes except X, which is a signed exchange term.
e, Q, p, b, d = sp.symbols('e Q p b d', nonnegative=True, real=True)
X = sp.symbols('X', real=True)

# Exact structured part after the +Qe drift term cancels -Qe from D(-grad Q).
# The remaining sigma-charge exchange is 3X.
structured_reaction = sp.Rational(1,2)*e**2 - 3*e + 3*X

# Cauchy estimates:
#   |X| <= p sqrt(Q e),
#   |R_q| <= sqrt(2 Q e) b,
# where p=|d sigma| and b=|rho^{-3/2}M^{-1/2}dq|.
X_bound = p*Q*sp.sqrt(e)
Rq_bound = sp.sqrt(2*Q*e)*b

# A pointwise Young-family lower bound for any eta,zeta > 0.
eta, zeta = sp.symbols('eta zeta', positive=True, real=True)
young_exchange_rhs = -(sp.Rational(9,2)*eta*p**2*e + Q**2/(2*eta))
young_charge_rhs = -(zeta*Q*e + b**2/(2*zeta))

# Verify scalar Young squares.
exchange_square = sp.expand((3*sp.sqrt(eta)*p*sp.sqrt(e) - Q/sp.sqrt(eta))**2/2)
exchange_young_residual = sp.simplify(
    exchange_square - (sp.Rational(9,2)*eta*p**2*e + Q**2/(2*eta) - 3*p*Q*sp.sqrt(e))
)
charge_square = sp.expand((sp.sqrt(2*zeta*Q*e) - b/sp.sqrt(zeta))**2/2)
charge_young_residual = sp.simplify(
    charge_square - (zeta*Q*e + b**2/(2*zeta) - sp.sqrt(2*Q*e)*b)
)

# Area equation for forced metrics.  If T is the trace of the vertical defect,
# then L sigma = 6 + Q - T, so the combined W=e+c|d sigma|^2 route is the
# natural place to absorb p^2 e.  The e-only equation cannot remove p.
T, c = sp.symbols('T c', real=True)
area_equation = 6 + Q - T

# Physical Maxwell toy equation on round cusp, w'+3w=b with |b|<=B.
# Exact variation-of-constants envelope from t0 to t.
t, t0, B, w0 = sp.symbols('t t0 B w0', positive=True, real=True)
envelope = sp.exp(-3*(t-t0))*w0 + B*(1-sp.exp(-3*(t-t0)))/3
envelope_ode_residual = sp.simplify(sp.diff(envelope,t) + 3*envelope - B)

# Separator and curvature quantities must remain distinct for variable Q.
Qinf, Qsup, Qsep, delta = sp.symbols('Qinf Qsup Qsep delta', nonnegative=True)
CD_K = 3 - Qinf + delta
forcing_sup = Qsup + 2*delta
separator_floor = 12 + 2*Qsep - 8*delta

out = {
    'post_cancellation_structured_reaction': str(structured_reaction),
    'exchange_bound': '|3X| <= 3 |d sigma| Q sqrt(e)',
    'charge_derivative_bound': '|R_q| <= sqrt(2 Q e) |b|',
    'young_exchange_lower_bound': str(young_exchange_rhs),
    'young_charge_lower_bound': str(young_charge_rhs),
    'exchange_young_square_residual': str(exchange_young_residual),
    'charge_young_square_residual': str(charge_young_residual),
    'forced_area_equation': f'L sigma = {area_equation}',
    'variable_Q_quantities': {
        'curvature_parameter': str(CD_K),
        'curvature_uses': 'inf_B Q (with exact OT ends this is 0)',
        'tension_or_source_size_uses': str(forcing_sup),
        'separator_uses': str(Qsep),
        'warning': 'These cannot be replaced by one Q_max or put into a spatially varying mass without a new variable-potential resolvent theorem.'
    },
    'separator_floor': str(separator_floor),
    'round_cusp_envelope': str(envelope),
    'round_cusp_envelope_ode_residual': str(envelope_ode_residual),
    'round_cusp_consequence': 'If |b|<=B then |w(t)| <= exp(-3 Delta)|w(t0)| + (B/3)(1-exp(-3 Delta)); sustained forcing permits O(B), not forced e^{-r} decay.',
    'all_symbolic_checks_zero': exchange_young_residual == 0 and charge_young_residual == 0 and envelope_ode_residual == 0,
}
path = Path('workspace/data/step90_exchange_inequality_verify.json')
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
print(f'\nwrote {path}')
