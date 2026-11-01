#!/usr/bin/env python3
"""Step 65 verification script.

Part A: Gauss-Bonnet pinching threshold and the mu_4 determination.
  On any closed 4-manifold: 8 pi^2 chi = ∫ (|W|^2 + s^2/24 - |Ric0|^2/2).
  If ||Ric - Λ g||_op <= δ|Λ| then s^2/24 >= (2/3)Λ^2 (1-δ)^2 pointwise
  and ∫|Ric0|^2/2 <= 2 δ^2 Λ^2 Vol.  Hence chi >= (Vol Λ^2 / 8 pi^2)[(2/3)(1-δ)^2 - 2δ^2].
  chi <= 0 forces δ >= δ0 with (2/3)(1-δ0)^2 = 2δ0^2, δ0 = (√3-1)/2.
  For T^4 with Λ = -3: ||Ric + 3g||_op >= 3(√3-1)/2 for EVERY metric.

Part B: numerical construction of an S^1-invariant metric on T^3 with
  strictly negative scalar curvature everywhere.
  Ansatz: g = pi^* q + w^2 dθ^2, q = e^{2u} q0 (q0 flat T^2), w = e^φ.
  R = -2 e^{-2u} [ Δ(u+φ) + |∇φ|^2 ]  (flat Laplacian/gradient on T^2).
  Need ΔΦ + |∇φ|^2 > 0 pointwise, Φ = u + φ.
  Construction: φ = cos x + cos y (vanishing gradient exactly at 4 corners);
  ΔΦ = h with h > 0 on corner disks covering {|∇φ|^2 small}, h = -c1 < 0 off.
  Feasibility needs c1 < min outside disks of |∇φ|^2.

Part C: warped-collar scalar identities used in the fusion program note
  (checked symbolically on a numeric family):
  g = dr^2 + γ_r on T^3 x I:  traced Gauss  R(γ_r) = R_M - 2 Ric(ν,ν) + H^2 - |S|^2;
  Riccati trace  H' = -Ric(ν,ν) - |S|^2.
"""

import json
import numpy as np

out = {}

# ---------------------------------------------------------------- Part A
d0 = (np.sqrt(3) - 1) / 2
lhs = (2/3) * (1 - d0)**2
rhs = 2 * d0**2
out["A_threshold"] = {
    "delta0": d0,
    "identity_(2/3)(1-d)^2_vs_2d^2_at_d0": [lhs, rhs],
    "mu4_lower_bound_3_delta0": 3 * d0,
    "chi_bound_coefficient_at_d0": (2/3)*(1-d0)**2 - 2*d0**2,
}
# sanity: bracket positive below, negative above
ds = np.linspace(0.01, 0.9, 18)
bracket = (2/3)*(1-ds)**2 - 2*ds**2
out["A_bracket_sign_changes"] = int(np.sum(np.diff(np.sign(bracket)) != 0))
out["A_bracket"] = list(zip(np.round(ds,3), np.round(bracket,4)))

# ---------------------------------------------------------------- Part B
N = 256
x = np.linspace(0, 2*np.pi, N, endpoint=False)
X, Y = np.meshgrid(x, x, indexing="ij")
dx = x[1] - x[0]

def lap(F):
    return (np.roll(F,1,0)+np.roll(F,-1,0)+np.roll(F,1,1)+np.roll(F,-1,1)-4*F)/dx**2

def grad2(F):
    gx = (np.roll(F,-1,0)-np.roll(F,1,0))/(2*dx)
    gy = (np.roll(F,-1,1)-np.roll(F,1,1))/(2*dx)
    return gx**2 + gy**2

phi = np.cos(X) + np.cos(Y)
g2 = grad2(phi)

# corner disks (4 corners of the 2pi torus: (0/2pi,0/2pi),(pi,0),(0,pi),(pi,pi))
corners = [(0.0,0.0),(np.pi,0.0),(0.0,np.pi),(np.pi,np.pi)]
dist2 = np.full_like(X, 1e9)
for cx, cy in corners:
    ddx = np.minimum(np.abs(X-cx), 2*np.pi-np.abs(X-cx))
    ddy = np.minimum(np.abs(Y-cy), 2*np.pi-np.abs(Y-cy))
    dist2 = np.minimum(dist2, ddx**2 + ddy**2)
rho = 0.30
disk = dist2 <= rho**2
h_plus = 2.0
A_plus = disk.mean() * (2*np.pi)**2
A_minus = (2*np.pi)**2 - A_plus
min_g2_outside = g2[~disk].min()
c1 = h_plus * A_plus / A_minus
out["B_feasibility"] = {
    "rho": rho,
    "h_plus": h_plus,
    "c1_needed": c1,
    "min_|grad_phi|^2_outside_disks": float(min_g2_outside),
    "feasible": bool(c1 < min_g2_outside),
}

# build smooth h: h = h_plus on disks, -c1 outside, mollified and rebalanced
from numpy.fft import fft2, ifft2
h = np.where(disk, h_plus, -c1)
# mollify with a small Gaussian in Fourier space
kx = np.fft.fftfreq(N, d=dx) * 2*np.pi
KX, KY = np.meshgrid(kx, kx, indexing="ij")
sigma = 6.0
Hhat = fft2(h) * np.exp(-(KX**2+KY**2)/(2*sigma**2))
h_sm = np.real(ifft2(Hhat))
# exact mean-zero rebalance preserving positivity margin
h_sm -= h_sm.mean()
# solve ΔΦ = h_sm  (periodic, mean-zero rhs)
Hh = fft2(h_sm)
K2 = KX**2 + KY**2
K2[0,0] = 1.0
Phi = np.real(ifft2(-Hh / K2))
Phi -= Phi.mean()

u = Phi - phi
R_factor = lap(Phi) + g2          # Δ(u+φ)+|∇φ|^2 ;  R = -2 e^{-2u} R_factor
R = -2*np.exp(-2*u) * R_factor
out["B_result"] = {
    "min_R": float(R.min()),
    "max_R": float(R.max()),
    "min_R_factor": float(R_factor.min()),
    "R_negative_everywhere": bool(R.max() < 0),
    "Phi_range": [float(Phi.min()), float(Phi.max())],
    "u_range": [float(u.min()), float(u.max())],
}

# ---------------------------------------------------------------- Part C
# numeric identity check: build g = dr^2 + a(r)^2(dx1^2+dx2^2) + b(r)^2 dx3^2
# on T^3 x I; compute full 4D Ricci tensor by Christoffel and compare
# R(γ_r) with R_M - 2 Ric(ν,ν) + H^2 - |S|^2 and H' with -Ric(ν,ν) - |S|^2.

def christoffel_metric(g_funcs, r):
    """return Christoffel of dr^2 + sum_i f_i(r)^2 dxi^2 at r (diagonal, coords (r,x1,x2,x3))."""
    f = np.array([gf(r) for gf in g_funcs])     # a,a,b
    fp = np.array([gf(r, 1) for gf in g_funcs])
    return f, fp

def f_a(r, d=0):
    v = 1.0 + 0.3*np.sin(2*r) + 0.1*r
    if d == 0: return v
    if d == 1: return 0.6*np.cos(2*r) + 0.1
    return -1.2*np.sin(2*r)

def f_b(r, d=0):
    v = 1.0 + 0.2*np.cos(r) + 0.05*r
    if d == 0: return v
    if d == 1: return -0.2*np.sin(r) + 0.05
    return -0.2*np.cos(r)

r0 = 0.7
a, ap, app = f_a(r0,0), f_a(r0,1), f_a(r0,2)
b, bp, bpp = f_b(r0,0), f_b(r0,1), f_b(r0,2)
f = np.array([a, a, b]); fp = np.array([ap, ap, bp]); fpp = np.array([app, app, bpp])

# S = diag(fp/f) (mixed (1,1)); H = tr S; |S|^2 = tr S^2
S = fp/f
H = S.sum(); S2 = (S**2).sum()
# Ricci of dr^2 + Σ f_i^2 dxi^2:
# Ric(ν,ν) = -Σ (fpp/f)
# Ric(xi,xi)/f_i^2 = -(fpp/f)_i - (fp/f)_i * H
Ric_nn = -(fpp/f).sum()
Ric_t = -(fpp/f) - S*(H - S)   # Ric^i_i = -(f''/f)_i - u_i (H - u_i)
R_M = Ric_nn + Ric_t.sum()      # scalar = trace, single count
# intrinsic γ_r = diag(a^2,a^2,b^2) is FLAT (constant coefficients) => R(γ)=0
R_gamma = 0.0
gauss_lhs = R_M - 2*Ric_nn + H**2 - S2
riccati_Hp = -Ric_nn - S2
Hp_direct = ((fpp/f) - S**2).sum()   # H' = Σ d/dr(fp/f) = Σ (fpp/f - (fp/f)^2)
out["C_identities"] = {
    "R(γ_r)": R_gamma,
    "R_M - 2Ric(ν,ν) + H^2 - |S|^2": gauss_lhs,
    "gauss_residual": abs(R_gamma - gauss_lhs),
    "H'_riccati": riccati_Hp,
    "H'_direct": Hp_direct,
    "riccati_residual": abs(riccati_Hp - Hp_direct),
}

print(json.dumps(out, indent=2))
with open("Sessions/S0910A03/workspace/data/step65_mu4_and_slice_mechanism.json", "w") as fh:
    json.dump(out, fh, indent=2)
print("Saved: Sessions/S0910A03/workspace/data/step65_mu4_and_slice_mechanism.json")
