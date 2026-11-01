"""
STEP 94 SUPERSESSION NOTICE: this exploratory file contains a false
maximum-principle interpretation. Its raw diagonal identity is retained only as
historical algebra. Negative LQ at an interior maximum is compatible with the
maximum and yields no upper bound. See step94_invariant_charge_identity.py and
step94_charge_sign_correction_and_global_flux.md.

Step 93b: Investigate whether a global maximum principle or subsolution
inequality for the physical twist energy Q can bound Q_+ = sup_B Q.

The question: on the free-T² base with drift Laplacian L and the
coupled Einstein equations, does Q satisfy a useful differential
inequality?

From Step 90:
  Q = (1/2)rho^{-3} q^T M^{-1} q
  Hess_{H^2} Q = Q h  (target convexity)
  |grad Q|^2 = Q^2
  L sigma = 6 + Q
  
For exact Einstein (dq=0), compute LQ:
  Q = (1/2)e^{-3sigma} q^T M^{-1}(U) q
  
  dQ/dx^i = -(3/2)sigma_i Q + (1/2)e^{-3sigma} q^T (d/dx^i M^{-1}) q
  
The M^{-1} derivative involves dU:
  d(M^{-1}) = -M^{-1}(dM)M^{-1}
  
So dQ contains terms proportional to dU and d sigma.

In the orbit-map language: on the target H^2, Q is a function of the
orbit shape M and the charge q. When q is constant (exact Einstein):
  Q(x) = Q_0 * F(U(x))
where F is a specific function on H^2 depending on q.

Since Hess_H F = F h (horospherical), F is a convex function on H^2.
For a sigma-harmonic map U: B -> H^2:
  L(F∘U) = <Hess F(dU,dU)> + <grad F, tau_sigma>
         = F * |dU|^2 + 0  (since tau_sigma = 0)
         = F * e

Therefore in the exact case:
  LQ = Qe + area terms

More precisely: Q = e^{-3sigma} * (Q_0 F(U)), and
  L(e^{-3sigma}) = e^{-3sigma}[-3 L sigma + 9|grad sigma|^2]
                 = e^{-3sigma}[-3(6+Q) + 9|grad sigma|^2]
                 = e^{-3sigma}[-18 - 3Q + 9|grad sigma|^2]

L(Q) = L(e^{-3sigma} * (1/2)q^T M^{-1}q)
     = (1/2)q^TM^{-1}q * L(e^{-3sigma}) + e^{-3sigma}*(1/2)*L(q^TM^{-1}q)
     + 2 * grad(e^{-3sigma}) . grad((1/2)q^TM^{-1}q)

Let me compute each term symbolically.
"""
import sympy as sp
from sympy import symbols, Function, exp, sqrt, diff, simplify, collect

r, z = symbols('r z', real=True)
sigma = Function('sigma')(r, z)
alpha = Function('alpha')(r, z)  # orbit anisotropy (M = diag(e^alpha, e^-alpha))
q0 = symbols('q0', real=True, positive=True)  # constant charge (exact Einstein)

# Physical twist: Q = (1/2) q0^2 e^{-3sigma - alpha}  (diagonal, one-charge)
Q = sp.Rational(1,2) * q0**2 * exp(-3*sigma - alpha)

# Drift Laplacian: L = Delta + grad(sigma) . grad
# For flat base metric: L f = f_rr + f_zz + sigma_r f_r + sigma_z f_z
def drift_laplacian(f, base_vars=(r, z)):
    r_, z_ = base_vars
    return (diff(f, r_, 2) + diff(f, z_, 2) + 
            diff(sigma, r_) * diff(f, r_) + 
            diff(sigma, z_) * diff(f, z_))

LQ = drift_laplacian(Q)
LQ_simplified = sp.expand(LQ)

# Collect terms
# Factor out Q where possible
print("LQ = ", LQ_simplified)

# Express in terms of Q, |grad sigma|^2, |grad alpha|^2, etc.
# Q = (1/2)q0^2 exp(-3sigma-alpha)
# grad Q = Q * (-3 grad sigma - grad alpha)
# |grad Q|^2 = Q^2 * (9|grad sigma|^2 + 6 <grad sigma, grad alpha> + |grad alpha|^2)
# Delta Q = Q * [9|grad sigma|^2 + 6<grad sigma, grad alpha> + |grad alpha|^2
#                - 3 Delta sigma - Delta alpha]
# L Q = Delta Q + grad sigma . grad Q
#     = Q * [9|grad sigma|^2 + 6<grad sigma, grad alpha> + |grad alpha|^2
#            - 3 Delta sigma - Delta alpha
#            - 3|grad sigma|^2 - <grad sigma, grad alpha>]
#     = Q * [6|grad sigma|^2 + 5<grad sigma, grad alpha> + |grad alpha|^2
#            - 3 Delta sigma - Delta alpha]

# Now use the Einstein equations for the exact diagonal one-charge case:
# L sigma = 6 + Q       (area)
# L alpha = Q            (orbit traceless) -- from Step 89 eq (1.5)
# Ric_B - Hess sigma = (-3+Q)gamma + (1/2)d sigma^2 + (1/2)d alpha^2

# Therefore:
# L sigma = Delta sigma + |grad sigma|^2 = 6 + Q
# L alpha = Delta alpha + <grad sigma, grad alpha> = Q

# So:
# Delta sigma = 6 + Q - |grad sigma|^2
# Delta alpha = Q - <grad sigma, grad alpha>

# Substituting:
# LQ = Q * [6|grad sigma|^2 + 5<gs,ga> + |ga|^2
#           - 3(6+Q-|gs|^2) - (Q - <gs,ga>)]
#    = Q * [6|gs|^2 + 5<gs,ga> + |ga|^2
#           - 18 - 3Q + 3|gs|^2 - Q + <gs,ga>]
#    = Q * [9|gs|^2 + 6<gs,ga> + |ga|^2 - 18 - 4Q]
#    = Q * [|3gs + ga|^2 - 18 - 4Q]

# But |grad Q|^2 = Q^2 * |3gs + ga|^2 = Q^2 * (9|gs|^2 + 6<gs,ga> + |ga|^2)
# So: |3gs + ga|^2 = |grad Q|^2 / Q^2

# Therefore:
# LQ = Q * (|grad Q|^2/Q^2 - 18 - 4Q)
# LQ = |grad Q|^2/Q - 18Q - 4Q^2

print("\n=== Exact diagonal one-charge LQ formula ===")
print("LQ = |grad Q|^2 / Q  - 18 Q  - 4 Q^2")
print("   = |grad(log Q)|^2 * Q  - 18 Q  - 4 Q^2")
print("\nSTEP 94 CORRECTION:")
print("At a maximum of Q: grad Q = 0 and LQ = -18Q - 4Q^2 < 0.")
print("This is compatible with an interior maximum and gives no boundary maximum rule.")
print("Q -> 0 at both ends can occur by redshift with nonzero conserved charge.")
print("Exact OT on an open end implies q=0 by charge conservation, a separate fact.")

# Forced case: LQ = |grad Q|^2/Q - 18Q - 4Q^2 + forcing terms
# The forcing comes from dq ≠ 0 and mixed Ricci E_mix
# Under ||E||_op ≤ delta, the forcing contributes terms of order delta
print("\n=== Forced case ===")
print("Under ||Ric+3g||_op ≤ δ:")
print("  L sigma = 6 + Q + O(δ)   (area equation modified)")
print("  L alpha = Q + O(δ)        (orbit traceless modified)")
print("  dq = O(δ ρ)               (Maxwell forcing)")
print("")
print("The additional terms in LQ from:")
print("  1. Area: Δσ uses 6+Q+O(δ), giving +3δQ + lower")
print("  2. Orbit: Δα uses Q+O(δ), giving +δQ + lower")
print("  3. Charge: d/dt(q^T M^{-1} q) has terms O(δρQ^{1/2})")
print("  4. Cross: grad corrections O(δ|grad Q|)")
print("")
print("The negative reaction does NOT furnish a forced upper bound:")
print("an inequality LQ<0 is allowed at an interior maximum. Variable charge also")
print("introduces source derivatives in logarithmic formulas and zeros where log is")
print("undefined. The remaining problem is global vector-charge flux/coercivity.")

import json
from pathlib import Path
result = {
    "exact_LQ": "LQ = |grad Q|^2/Q - 18Q - 4Q^2",
    "step94_correction": "At a maximum, LQ=-18Q-4Q^2<0 is compatible with LQ<=0; no maximum estimate follows.",
    "exact_conservation_statement": "Exact OT on an open end plus exact Einstein gives q=0 globally by dq=0; Q->0 alone does not.",
    "forced_status": "No Q=O(delta^2) inference. Seek a two-ended weighted vector-charge flux/coercivity estimate.",
    "status": "raw diagonal identity verified; former interpretation superseded by Step 94"
}
out = Path("workspace/data/step93_Q_maximum_principle.json")
out.parent.mkdir(exist_ok=True, parents=True)
out.write_text(json.dumps(result, indent=2))
print(f"\nwrote {out}")
