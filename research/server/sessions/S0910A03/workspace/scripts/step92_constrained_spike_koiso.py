"""
Step 92: construct analytic T^2-invariant Einstein Cauchy data with concentrated
normal orbit energy on a minimal T^3.

For an analytic positive periodic P(s), choose a closed H^2 curve U(s) with
|U_s|^2=12+2P.  Let q=ds^2+M(U(s)) on T^3, det M=1.  Choose the vertical
trace-free Weingarten block B pointwise target-orthogonal to U_s and with
|B|^2=P.  Then
  Scal_q=-|U_s|^2/2=-6-P,
  tr W=0, |W|^2=P,
  div W=0 (equivalent to <U_s,U_n>=0),
so the lambda=-3 Einstein Cauchy constraints hold exactly.  If
-d^2/ds^2+3-P >=0, the hypersurface is stable for invariant speeds.
Koiso then supplies a local analytic Ric=-3g germ.

The code samples a von Mises analytic spike and numerically checks the matrix
normalizations, orthogonality, constraints, periodicity, and invariant Jacobi
eigenvalue.  The proof is algebraic; numerics are a normalization check.
"""
from pathlib import Path
import json
import math
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.special import i0e
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

L = 2 * math.pi
N = 4096
kappa = 800.0
mass = 1.0
s = np.linspace(0.0, L, N, endpoint=False)
ds = L / N

# Stable analytic approximate delta; i0e avoids overflow.
P = mass * np.exp(kappa * (np.cos(s) - 1.0)) / (L * i0e(kappa))
v = np.sqrt(12.0 + 2.0 * P)
# Periodic trapezoid total and cumulative target arclength.
total_v = ds * np.sum(v)
sinhR = total_v / (2 * math.pi)
R = np.arcsinh(sinhR)
theta_prime = v / sinhR
# Spectral/periodic cumulative via trapezoid, then normalize tiny quadrature drift.
theta = np.concatenate(([0.0], cumulative_trapezoid(theta_prime, dx=ds)))
# The analytic construction uses theta(s)=sinh(R)^(-1)∫_0^s v; no discrete
# rescaling is mathematically needed.  Retain the raw quadrature values so
# theta and theta_prime remain mutually consistent in the normalization check.

cR, sR = math.cosh(R), math.sinh(R)
den = cR - sR * np.sin(theta)
y = 1.0 / den
alpha = np.log(y)
beta = sR * np.cos(theta) / den

# Analytic derivatives with respect to theta, then s.
dden_dtheta = -sR * np.cos(theta)
alpha_theta = -dden_dtheta / den
beta_theta = (-sR * np.sin(theta) * den - sR * np.cos(theta) * dden_dtheta) / den**2
alpha_s = alpha_theta * theta_prime
beta_s = beta_theta * theta_prime
es_coord = alpha_s**2 + np.exp(-2 * alpha) * beta_s**2

# Unit target tangent and its +pi/2 rotation in metric diag(1,e^{-2alpha}).
talpha = alpha_s / v
tbeta = beta_s / v
nalpha = -np.exp(-alpha) * tbeta
nbeta = np.exp(alpha) * talpha
normal_norm = nalpha**2 + np.exp(-2 * alpha) * nbeta**2
orth_coord = talpha * nalpha + np.exp(-2 * alpha) * tbeta * nbeta


def M_and_derivs(a, b):
    em = math.exp(-a)
    ep = math.exp(a)
    M = np.array([[ep + b*b*em, b*em], [b*em, em]])
    Ma = np.array([[ep - b*b*em, -b*em], [-b*em, -em]])
    Mb = np.array([[2*b*em, em], [em, 0.0]])
    return M, Ma, Mb

max_det_res = 0.0
max_target_metric_res = 0.0
max_AB_inner = 0.0
max_trace_B = 0.0
max_norm_B_res = 0.0
max_symmetry_res = 0.0
for j in range(N):
    M, Ma, Mb = M_and_derivs(float(alpha[j]), float(beta[j]))
    Mi = np.linalg.inv(M)
    Ms = Ma * alpha_s[j] + Mb * beta_s[j]
    CN = Mi @ (Ma * nalpha[j] + Mb * nbeta[j])
    A = 0.5 * Mi @ Ms
    B = math.sqrt(P[j] / 2.0) * CN
    max_det_res = max(max_det_res, abs(np.linalg.det(M) - 1.0))
    matrix_es = 0.5 * np.trace((Mi @ Ms) @ (Mi @ Ms))
    max_target_metric_res = max(max_target_metric_res, abs(matrix_es - es_coord[j]))
    max_AB_inner = max(max_AB_inner, abs(np.trace(A @ B)))
    max_trace_B = max(max_trace_B, abs(np.trace(B)))
    max_norm_B_res = max(max_norm_B_res, abs(np.trace(B @ B) - P[j]))
    max_symmetry_res = max(max_symmetry_res, np.max(np.abs(M @ B - (M @ B).T)))

# Hamiltonian residual: Scal_q+|W|^2-(-6), with Scal_q=-es/2.
hamiltonian = -0.5 * es_coord + P + 6.0
# Momentum: only nonzero candidate is proportional to tr(A B); checked above.

# Lowest eigenvalue of periodic -d2 + 3-P, second-order finite differences.
main = np.full(N, 2.0 / ds**2 + 3.0) - P
off = np.full(N - 1, -1.0 / ds**2)
J = diags([off, main, off], [-1, 0, 1], shape=(N, N), format='lil')
J[0, N-1] = -1.0 / ds**2
J[N-1, 0] = -1.0 / ds**2
J = J.tocsr()
lambda0 = float(eigsh(J, k=1, which='SA', return_eigenvectors=False, tol=1e-10)[0])

out = {
    'parameters': {'L': L, 'N': N, 'kappa': kappa, 'mass': mass},
    'spike': {
        'P_max': float(P.max()),
        'P_integral': float(ds * P.sum()),
        'effective_width_mass_over_height': float(mass / P.max()),
        'invariant_Jacobi_lowest_eigenvalue': lambda0,
        'full_stability_note': 'For torus Fourier mode k, the potential gains k^T M^{-1} k >= 0; hence the invariant k=0 mode is the lowest and strict invariant stability implies full stability for this block metric.',
    },
    'closed_H2_curve': {
        'target_length': float(total_v),
        'geodesic_circle_radius_R': float(R),
        'theta_total_quadrature': float(theta[-1] + theta_prime[-1] * ds),
        'theta_total_exact': 2 * math.pi,
        'max_speed_squared_residual': float(np.max(np.abs(es_coord - (12 + 2*P)))),
        'max_unit_normal_residual': float(np.max(np.abs(normal_norm - 1))),
        'max_tangent_normal_inner_product': float(np.max(np.abs(orth_coord))),
    },
    'matrix_checks': {
        'max_det_M_minus_1': max_det_res,
        'max_H2_matrix_metric_residual': max_target_metric_res,
        'max_tr_A_B_momentum_residual': max_AB_inner,
        'max_trace_B': max_trace_B,
        'max_norm_B_squared_minus_P': max_norm_B_res,
        'max_M_B_symmetry_residual': max_symmetry_res,
    },
    'constraint_checks': {
        'max_Hamiltonian_residual': float(np.max(np.abs(hamiltonian))),
        'momentum_vertical_components': 'zero by T2 invariance and absence of mixed W components',
        'momentum_s_component': 'proportional to tr(A B), numerical residual above',
        'mean_curvature': 'tr W = 0',
        'Einstein_constant': -3,
    },
    'mathematical_status': 'analytic constrained data and invariant stability; Koiso gives an exact local analytic Einstein germ. This is not a complete two-ended connector and the germ width need not be uniform as kappa grows.',
}
path = Path('workspace/data/step92_constrained_spike_koiso.json')
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2), encoding='utf-8')
print(json.dumps(out, indent=2))
print(f'wrote {path}')
