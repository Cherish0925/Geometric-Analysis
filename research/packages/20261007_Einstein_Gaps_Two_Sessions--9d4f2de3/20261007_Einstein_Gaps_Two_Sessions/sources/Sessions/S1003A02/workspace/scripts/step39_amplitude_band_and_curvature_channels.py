"""Step 39: exact amplitude-band constants and the X=128 curvature-channel comparison.

This does not solve a monopole boundary-value problem.  It records consequences that hold for
any full sign-family solution on the scalar -4 Yamabe representative of a closed host containing
replicas of the certified cell.

If c=P/(8*pi^2) for one blow-up and Delta=8*pi^2(1-c), the clean amplitude
identity forces L=E int(2-rho) >= Delta/4=2*pi^2(1-c).  The residual-polynomial
form forces int_{rho_*<rho<2} m(rho) >= Delta, hence the shallow-band volume is
at least Delta/max(m).  All volume statements use scalar -4 normalization.

The curvature comparison reads the numerical (not interval-certified) Yamabe decomposition
from cell_yamabe_rv_ch_x003_X128_d20.json.  Its entries are in 8*pi^2 units:
  P-1 = fourWplus_rel + scalar_channel,
  scalar_channel = 48 RV_hat + Q_square + Q_grad (up to discretization residual).
The P interval itself is the exact-dyadic Arb certificate.
"""
from pathlib import Path
import json, math
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
WS = Path(__file__).resolve().parents[1]
cert_path = ROOT / 'S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_P_exact.json'
yam_path = WS / 'data/cell_yamabe_rv_ch_x003_X128_d20.json'
cert = json.loads(cert_path.read_text())
yam = json.loads(yam_path.read_text())['rows'][-1]

rho = sp.symbols('rho', real=True)
m = sp.factor((2-rho)*(-rho**3+10*rho**2-2*rho-4)/6)
roots = [r for r in sp.nroots(-rho**3+10*rho**2-2*rho-4, n=40, maxsteps=200)
         if abs(complex(r).imag) < 1e-30 and 0 < float(sp.re(r)) < 2]
rhostar = float(sp.re(roots[0]))
critical = [r for r in sp.solve(sp.diff(m, rho), rho) if r.is_real is not False]
crit_in = [float(sp.N(r, 40)) for r in critical if 0 < float(sp.N(r, 40)) < 2]
rhomax = max(crit_in, key=lambda x: float(m.subs(rho, x)))
mmax = float(sp.N(m.subs(rho, rhomax), 40))

clo = float(cert['P']['lower_dec_outward'])
chi = float(cert['P']['upper_dec_outward'])
# Deficit is largest at lower P and smallest at upper P.
deficit_norm = [1-chi, 1-clo]
L_per_class = [2*math.pi**2*d for d in deficit_norm]
band_volume = [8*math.pi**2*d/mmax for d in deficit_norm]

fourW = float(yam['fourWplus_rel'])
scalar = float(yam['scalar_channel'])
rv48 = 48*float(yam['RV_hat'])
q_sq = float(yam['Q_square'])
q_grad = float(yam['Q_grad'])

out = {
    'normalizations': {
        'costs': 'P and Theorem-C channels divided by 8*pi^2',
        'amplitude_and_band_volume': 'closed Yamabe representative scaled to scalar -4',
        'yamabe_channels_status': 'finite-grid numerical decomposition; P interval is exact-dyadic Arb'
    },
    'amplitude_polynomial': {
        'm_exact': str(m),
        'rho_star': rhostar,
        'positive_band': [rhostar, 2.0],
        'rho_at_m_max': rhomax,
        'm_max': mmax
    },
    'certified_P_interval': [clo, chi],
    'normalized_tariff_deficit_interval': deficit_norm,
    'necessary_linear_amplitude_deficit_L_per_class': L_per_class,
    'necessary_shallow_band_volume_per_class': band_volume,
    'curvature_channels_X128_N2400': {
        'P_minus_1_from_certificate_midpoint': (clo+chi)/2-1,
        'P_minus_1_numerical_profile': float(yam['P'])-1,
        'four_Delta_Wplus': fourW,
        'scalar_channel_total': scalar,
        'sum_fourWplus_and_scalar': fourW+scalar,
        '48_RV_hat': rv48,
        'Q_square': q_sq,
        'Q_grad': q_grad,
        'yamabe_rhs_sum': rv48+q_sq+q_grad,
        'yamabe_identity_residual': float(yam['identity_residual'])
    },
    'structural_reading': {
        'volume_side': 'L=E int(2-rho), K, and the quadratic amplitude term enter the scalar slack Sigma=16V-32*pi^2*p; exactly L=K+(1/2)int(2-rho)^2.',
        'weyl_curvature_side': 'pairwise amplitude variance and 2|w|^2 equal the nonconstant self-dual Walsh-curvature energy; Wplus-W0 is direct Weyl misalignment.',
        'bridge': 'zeta is covariant spinor variation and couples amplitude/direction transport to curvature alignment.',
        'missing_measurement': 'The realized fraction (8*pi^2-P)/(4L) requires actual closed-host monopoles; the failed isolated-cell ODE outputs do not provide it.'
    }
}
out_path = WS / 'data/step39_amplitude_band_and_curvature_channels.json'
out_path.write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out, indent=1))
