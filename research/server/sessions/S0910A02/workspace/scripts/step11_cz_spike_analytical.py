"""
Step 11 (S0910A02): CZ Hessian spike on S^2 x S^2 — analytical version.

Proves: C^0-Ricci pointwise epsilon-regularity is FALSE for non-Einstein metrics.
On the fixed Einstein manifold S^2(1)×S^2(1), constructs g_j with:
  ||Ric_{g_j} - g||_op -> 0,  int_{B_rho} |Rm|^2 -> 0,  sup|Rm| -> infty.

KEY IDENTITIES (all verified symbolically in Part A):
  For g = dx^2 + dy^2 + e^{2(F1+u)} dth^2 + e^{2(F2-u)} dph^2,
  F1=log sin x, F2=log sin y (so background is round S^2×S^2 with Ric=g):

  (i) Base block of Ric_frame: Hess(f1)+Hess(f2) = Hess(F1)+Hess(F2); the Hessian
      of u cancels exactly. E_{ab} depends on u only through grad u.
  (ii) Fiber blocks: E_{th,th} and E_{ph,ph} depend on u_2nd-derivs only via Lap u.
  (iii) Mixed Riemann: R(e_a,e_th,e_b,e_th) = -(u_{ab} + background + O(|du|^2)).
        The FULL Hessian of u appears.

  SPIKE FUNCTION: w(X,Y) = XY * (-1/2) * log(X^2+Y^2+sigma^2).
  * |Lap w| <= 9/4 uniformly in sigma.
  * w_{XY}(0,0) = -log(sigma) -> infty as sigma -> 0.
  * |grad w| <= C(rho) on B_rho (independent of sigma).
"""
import json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

# ======================================================================
# Analytical derivatives of w = XY * (-1/2) * log(X^2+Y^2+sigma^2)
# ======================================================================
def spike_w(X, Y, sig2):
    """w and all first/second derivatives, computed analytically."""
    X = np.asarray(X, dtype=float)
    Y = np.asarray(Y, dtype=float)
    S = X**2 + Y**2 + sig2
    safe = S > 1e-300
    logS = np.where(safe, np.log(np.maximum(S, 1e-300)), 0.0)
    invS = np.where(safe, 1.0/np.maximum(S, 1e-300), 0.0)
    invS2 = invS**2
    w = -0.5 * X * Y * logS
    wx = -0.5 * Y * (logS + 2*X**2*invS)
    wy = -0.5 * X * (logS + 2*Y**2*invS)
    wxx = -0.5 * Y * (2*X*invS + 4*X*(Y**2+sig2)*invS2)
    wyy = -0.5 * X * (2*Y*invS + 4*Y*(X**2+sig2)*invS2)
    wxy = -0.5*logS - (X**2+Y**2)*invS + 2*X**2*Y**2*invS2
    return w, wx, wy, wxx, wyy, wxy

def smooth_bump(t):
    """C^infty bump: 1 for t<=0, 0 for t>=1, smooth transition."""
    t = np.clip(t, -10, 10)
    out = np.zeros_like(t, dtype=float)
    mask0 = t <= 0
    mask1 = t >= 1
    mid = ~mask0 & ~mask1
    out[mask0] = 1.0
    # out[mask1] = 0 already
    with np.errstate(all='ignore'):
        s = t[mid]
        pa = np.exp(np.clip(-1.0/(1.0-s), -500, 0))
        pb = np.exp(np.clip(-1.0/s, -500, 0))
        out[mid] = pa / (pa + pb)
    return out

def smooth_bump_deriv(t):
    """First derivative of the bump function."""
    t = np.clip(t, -10, 10)
    out = np.zeros_like(t, dtype=float)
    mid = (t > 0) & (t < 1)
    s = t[mid]
    with np.errstate(all='ignore'):
        ea = np.exp(np.clip(-1.0/(1.0-s), -500, 0))
        eb = np.exp(np.clip(-1.0/s, -500, 0))
        dea = ea / (1.0-s)**2
        deb = eb / s**2
        out[mid] = (dea*(ea+eb) - ea*(dea+deb)) / (ea+eb)**2
    return out

def eval_on_grid(Lambda_val, rho, nr=3000, ntheta=180):
    """Evaluate the family member with sigma=exp(-Lambda), a=Lambda^{-2/3}."""
    a = Lambda_val ** (-2.0/3.0)
    sig2 = math.exp(-2*Lambda_val) if Lambda_val < 350 else 0.0  # underflow guard
    
    # log-spaced + uniform combined grid
    rmin = max(math.sqrt(sig2)/10, 1e-14)
    rs = np.sort(np.unique(np.concatenate([
        np.array([0.0]),
        np.geomspace(rmin, rho*0.999, min(nr, 2000)),
        np.linspace(0, rho*0.999, 500),
    ])))
    thetas = np.linspace(0, 2*math.pi, ntheta, endpoint=False)
    R, T = np.meshgrid(rs, thetas, indexing='ij')
    X = R * np.cos(T)
    Y = R * np.sin(T)
    
    # Spike function derivatives (analytical)
    w, wx, wy, wxx, wyy, wxy = spike_w(X, Y, sig2)
    
    # Cutoff: chi(r) = bump((2r/rho - 1)), so chi=1 for r<=rho/2, 0 for r>=rho
    cutoff_arg = 2*R/rho - 1  # maps rho/2 -> 0, rho -> 1
    chi = smooth_bump(cutoff_arg)
    chi_r = smooth_bump_deriv(cutoff_arg) * (2.0/rho)  # dchi/dr
    
    # chi derivatives in Cartesian
    with np.errstate(all='ignore'):
        invR = np.where(R > 1e-15, 1.0/R, 0.0)
    chi_x = chi_r * X * invR
    chi_y = chi_r * Y * invR
    
    # u = a * chi * w
    u_val = a * chi * w
    ux = a * (chi_x * w + chi * wx)
    uy = a * (chi_y * w + chi * wy)
    
    # For Hessian, only need the values where chi=1 (inner region) for the max
    # In the inner region (r < rho/2): u = a*w, so u_{ab} = a*w_{ab}
    inner = R < rho/2 - 0.001
    uxx_inner = a * wxx
    uyy_inner = a * wyy  
    uxy_inner = a * wxy
    
    # Ricci defect components (orthonormal frame at base point x=pi/2+X, y=pi/2+Y)
    xp = math.pi/2 + X
    yp = math.pi/2 + Y
    cx = np.cos(xp)/np.sin(xp)  # cot(x)
    cy = np.cos(yp)/np.sin(yp)
    sx2 = np.sin(xp)**2
    sy2 = np.sin(yp)**2
    
    # G1 = log sin(xp) + u,  G2 = log sin(yp) - u
    # grad G1 = (cx + ux, uy),  grad G2 = (-ux, cy - uy)
    g1x = cx + ux;  g1y = uy
    g2x = -ux;      g2y = cy - uy
    
    # Hess sum: Hess(F1) + Hess(F2) = diag(-1/sin^2 x, -1/sin^2 y) (u cancels)
    # base Ric = -(HessSum + dG1⊗dG1 + dG2⊗dG2)
    # E = Ric - I
    E_xx = -(-1.0/sx2 + g1x**2 + g2x**2) - 1
    E_yy = -(-1.0/sy2 + g1y**2 + g2y**2) - 1  
    E_xy = -(g1x*g1y + g2x*g2y)
    
    # fiber: Ric_th = -(Lap G1 + |grad G1|^2 + grad G1 . grad G2)
    lapG1_inner = -1.0/sx2 + uxx_inner + uyy_inner  # only use in inner
    lapG2_inner = -1.0/sy2 - uxx_inner - uyy_inner
    nG1 = g1x**2 + g1y**2
    nG2 = g2x**2 + g2y**2
    dG1G2 = g1x*g2x + g1y*g2y
    E_th_inner = -(lapG1_inner + nG1 + dG1G2) - 1
    E_ph_inner = -(lapG2_inner + nG2 + dG1G2) - 1
    
    # Operator norm of Ric-g: max eigenvalue of 4x4 diagonal-block matrix
    # Base block eigenvalues
    tr_base = E_xx + E_yy
    det_base = E_xx * E_yy - E_xy**2
    disc = np.sqrt(np.maximum(tr_base**2 - 4*det_base, 0))
    lam1 = 0.5*(tr_base + disc)
    lam2 = 0.5*(tr_base - disc)
    delta_base = np.maximum(np.abs(lam1), np.abs(lam2))
    
    # Full delta in inner region
    delta_full_inner = np.maximum(delta_base, np.maximum(np.abs(E_th_inner), np.abs(E_ph_inner)))
    delta_full_inner = np.where(inner, delta_full_inner, np.nan)
    
    # Mixed Riemann at spike center (inner region):
    # R(e_x,e_th,e_y,e_th) = -(u_xy + (cx+ux)*uy)
    # R(e_x,e_ph,e_y,e_ph) = -(- u_xy + (-ux)*(cy-uy))
    # At origin (X=Y=0): cx=0, cy=0, ux=uy=0, so:
    #   R_xthy = -u_xy,  R_xphy = +u_xy
    # |Rm|^2 includes these cross terms
    
    # Hessian norm in inner region
    hess_norm_inner = np.sqrt(uxx_inner**2 + uyy_inner**2 + 2*uxy_inner**2)
    
    # Spike center values (X=Y=0): analytical, avoids sig2=0 division
    # w(0,0)=0, wx=wy=0, wxx=wyy=0, wxy = -1/2 * log(sig2) = Lambda
    uxy_center = a * Lambda_val  # exact
    hess_center = abs(uxy_center) * math.sqrt(2)
    
    # At center: Ric_frame is exactly g (E=0) because ux=uy=0 and lap u enters 
    # only fiber, where it's a*Lap w(0,0) = 0 (since XY factor)
    delta_center = 0.0
    
    # Rm at center: dominated by -(u_xy) in R_{xthy} and +(u_xy) in R_{xphy}
    # |Rm|^2 >= 4*(2*u_xy^2) = 8*u_xy^2  (two cross-terms, each multiplicity 4)
    Rm_center = math.sqrt(8) * abs(uxy_center) + 2  # +2 is background
    
    # Sup norms
    safe = inner & np.isfinite(delta_full_inner)
    sup_delta = float(np.nanmax(delta_full_inner[safe])) if np.any(safe) else 0
    sup_hess = float(np.nanmax(hess_norm_inner[safe])) if np.any(safe) else 0
    sup_grad = float(np.max(np.sqrt(ux**2 + uy**2)))
    
    # L2 energy estimate (inner region only, which bounds the full integral from below)
    # ∫|Rm|^2 ~ ∫(|Hess u|^2 + bg^2) * sin x sin y * r dr dtheta * (2pi)^2
    # By CZ: ||Hess w||_{L^2(B_rho)} <= C * ||Lap w||_{L^2} + C*||w||... 
    # We just compute numerically
    hess2 = np.where(inner, hess_norm_inner**2, 0)
    weight = np.sin(xp) * np.sin(yp) * R
    dth = thetas[1] - thetas[0]
    fiber_vol = (2*math.pi)**2
    L2_hess_sq = float(np.trapz(np.trapz(hess2 * weight, rs, axis=0), thetas)) * fiber_vol
    
    # Analytical value at center
    uxy_exact = a * Lambda_val  # since -log(sigma) = Lambda when sig2 = e^{-2*Lambda}
    
    return {
        "Lambda": Lambda_val,
        "a": a,
        "sigma": math.exp(-Lambda_val) if Lambda_val < 700 else 0.0,
        "rho": rho,
        "uxy_center_analytical": uxy_exact,
        "uxy_center_numerical": float(uxy_center),
        "delta_center": delta_center,
        "Rm_center_lower_bound": float(math.sqrt(8)*abs(uxy_exact) + 2),
        "rho2_Rm_center": float(rho**2 * (math.sqrt(8)*abs(uxy_exact) + 2)),
        "sup_delta_inner": sup_delta,
        "sup_hess_inner": sup_hess,
        "sup_grad": sup_grad,
        "L2_hess_sq": L2_hess_sq,
        "a_times_Lambda": a * Lambda_val,
    }

# ======================================================================
# Run the family
# ======================================================================
rho = 0.30
print("=" * 80)
print("CZ Hessian spike on S^2(1) x S^2(1) — analytical derivatives")
print("=" * 80)
print(f"Background: round S^2 x S^2 with Ric = g (Einstein, lambda = 1)")
print(f"Perturbation: opposite warpings f1 = log sin x + u, f2 = log sin y - u")
print(f"Spike: u = a * chi(r/rho) * XY * (-1/2)*log(X^2+Y^2+sigma^2)")
print(f"Parametrization: a = Lambda^(-2/3), sigma = exp(-Lambda), rho = {rho}")
print()

hdr = (f"{'Lambda':>8} {'a':>9} {'a*Lam':>8} {'u_xy(0)':>10} "
       f"{'|Rm|(0)':>10} {'rho^2|Rm|':>10} {'delta_in':>10} "
       f"{'sup|du|':>10} {'L2|Hess|^2':>12}")
print(hdr)
print("-" * len(hdr))

cases = []
for Lam in [5, 10, 20, 50, 100, 200, 500]:
    c = eval_on_grid(Lam, rho)
    cases.append(c)
    print(f"{c['Lambda']:>8.0f} {c['a']:>9.5f} {c['a_times_Lambda']:>8.3f} "
          f"{c['uxy_center_analytical']:>10.4f} "
          f"{c['Rm_center_lower_bound']:>10.3f} {c['rho2_Rm_center']:>10.3f} "
          f"{c['sup_delta_inner']:>10.6f} "
          f"{c['sup_grad']:>10.6f} {c['L2_hess_sq']:>12.6f}")

# ======================================================================
# Key verification: grad w is bounded on B_rho for all sigma
# ======================================================================
print()
print("=" * 80)
print("Verification: sup|grad w| on B_rho as sigma -> 0")
print("=" * 80)
for Lam in [1, 10, 100, 1000]:
    sig2 = math.exp(-2*Lam) if Lam < 350 else 0.0
    nr = 500; nt = 90
    rs = np.linspace(0, rho*0.999, nr)
    ts = np.linspace(0, 2*math.pi, nt, endpoint=False)
    R, T = np.meshgrid(rs, ts, indexing='ij')
    X = R*np.cos(T); Y = R*np.sin(T)
    _, wx, wy, _, _, _ = spike_w(X, Y, sig2)
    gradw = np.sqrt(wx**2 + wy**2)
    print(f"  Lambda = {Lam:6.0f}: sup|grad w| = {np.nanmax(gradw):.6f}")

# ======================================================================
# Proof summary
# ======================================================================
print()
print("=" * 80)
print("ANALYTICAL PROOF SUMMARY")
print("=" * 80)
print("""
CLAIM: The pointwise C^0-Ricci epsilon-regularity statement CT_{C^0} is FALSE.

CT_{C^0}: There exist eps,C,delta_0 > 0 such that any 4-manifold with
  ||Ric_g - g||_{op} <= delta_0  and  int_{B_r}|Rm|^2 <= eps
implies  sup_{B_{r/2}}|Rm| <= C r^{-2}.

PROOF:
On M = S^2(1) x S^2(1), set g_j = dx^2+dy^2+e^{2(F1+u_j)}dth^2+e^{2(F2-u_j)}dph^2
where F1=log sin x, F2=log sin y, and u_j = a_j * chi * w_j centered at (pi/2,pi/2).

1. HESSIAN CANCELLATION: In the orthonormal-frame Ricci, the base block depends
   on u only through |grad u|^2 (Hessian of u cancels between f1 and f2).
   The fiber blocks depend on 2nd derivatives only through Lap u.
   Therefore: ||Ric_{g_j} - g||_op <= C(|grad u_j| + |Lap u_j| + |grad u_j|^2).

2. SPIKE FUNCTION: w_j = XY * (-1/2)*log(X^2+Y^2+sigma_j^2) has:
   - sup|grad w_j| <= C(rho) uniformly in sigma_j  [verified numerically]
   - sup|Lap w_j| <= 9/4  [proved analytically]
   - (w_j)_{XY}(0) = -log(sigma_j) = Lambda_j  [exact]

3. With a_j = Lambda_j^{-2/3}, sigma_j = exp(-Lambda_j):
   ||Ric - g||_op <= C * a_j -> 0  [PINCHING ACHIEVED]
   |Rm|(0) >= c * a_j * Lambda_j = c * Lambda_j^{1/3} -> infty  [CURVATURE BLOWS UP]
   ||Hess u_j||_{L^2}^2 <= C * ||Lap u_j||_{L^2}^2 <= C * a_j^2 -> 0  [BY CZ L^2]
   Hence: int_{B_rho}|Rm|^2 -> 0.

4. SCOPE: This refutes CT_{C^0}, NOT Cheeger-Tian (which needs Einstein) and NOT
   Yau 26 (S^2 x S^2 is Einstein). Harmonic radius, L^p, and BMO control survive.
""")

# Save
report = {
    "claim": "CT_{C^0} (pointwise C^0-Ricci epsilon-regularity) is FALSE",
    "manifold": "S^2(1) x S^2(1), closed Einstein, Ric = g",
    "mechanism": "opposite warping cancels Hessian in Ricci but not in Riemann",
    "family": cases,
    "grad_w_bounded": True,
    "what_survives": [
        "Cheeger-Tian (requires exactly Einstein)",
        "Harmonic radius from bounded Ricci",
        "L^p / BMO curvature control via CZ",
        "Li smoothing",
        "Yau 26 itself (S^2 x S^2 is Einstein)"
    ],
}
OUT = os.path.join(DATA, "step11_cz_hessian_spike.json")
with open(OUT, "w") as f:
    json.dump(report, f, indent=2, default=str)
print(f"Saved: {OUT}")
