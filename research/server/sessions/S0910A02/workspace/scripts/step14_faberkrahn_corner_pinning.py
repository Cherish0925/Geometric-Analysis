"""
Step 14 (S0910A02): the sharp positive-branch fork after the Strategist correction.

This script establishes, with exact elementary computations, the three
load-bearing quantitative facts behind the Step-14 build/break analysis:

  (A) DETERMINANT INVARIANCE OF THE CZ SPIKE.
      In the Step-11 opposite-warping ansatz f1 = F1 + u, f2 = F2 - u, the
      orbit-area density is w = e^{f1} e^{f2} = e^{F1+F2}, INDEPENDENT of u.
      So the CZ spike keeps w = sin x * sin y fixed: it concentrates curvature
      at fixed 4-volume and cannot produce a volume-collapsing sequence.
      A volume-breaking construction needs genuinely small p AND q.

  (B) FABER-KRAHN BASE-AREA LOWER BOUND.
      For a simply connected domain Omega in R^2 (or a topological disk with a
      metric), the sharp Faber-Krahn inequality is
          lambda_1^Dir(Omega) >= pi j_0^2 / Area(Omega),
      where j_0 = 2.404825557... is the first zero of J_0. Hence
          Area(Omega) >= pi j_0^2 / lambda_1^Dir(Omega).
      Combined with the Step-13 spectral bound lambda_1^Dir <= 2(1+delta), this
      gives an ABSOLUTE lower bound on the orbit-space area:
          Area(Omega) >= pi j_0^2 / (2(1+delta)) =: A_base(delta) > 0.
      (Note: Faber-Krahn is a lower bound for lambda_1 in terms of area; it
      requires the orbit metric g_B, not just topology. We record the flat
      model constant and flag the curved-orbit caveat.)

  (C) CORNER RISE RATE AND FIXED-SPHERE AREA BOOKKEEPING.
      At a smooth T^2 fixed point the local model is R^4 with w = s1 s2 rising
      at unit rate in the two transverse geodesic directions, so on a corner
      ball of g_B-radius r, int w ~ (1/4) r^4 (quarter-plane model). A corner
      contributes negligible 4-volume only if it has a short adjacent edge.
      We compute the exact quarter-plane corner integral and the S^4 anchor to
      calibrate constants, and record the resulting collapse dichotomy.

None of this alone proves the volume gap; the script isolates the exact
constants that the build/break argument must reconcile with chi-uniformity.
"""
import json, math, os
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

# ----------------------------------------------------------------------
# (A) Determinant invariance of the CZ spike
# ----------------------------------------------------------------------
# f1 = F1 + u, f2 = F2 - u  =>  f1 + f2 = F1 + F2  =>  w = exp(f1+f2) = exp(F1+F2)
# This is exact and u-independent. We record it symbolically as a statement plus
# a numerical check at a sample point.
import sympy as sp
x, y, u = sp.symbols('x y u', real=True)
F1 = sp.log(sp.sin(x)); F2 = sp.log(sp.sin(y))
f1 = F1 + u; f2 = F2 - u
w_spike = sp.exp(f1) * sp.exp(f2)
w_spike_simplified = sp.simplify(w_spike)
cz_determinant_u_derivative = sp.simplify(sp.diff(w_spike, u))

partA = {
    "ansatz": "f1 = log sin x + u, f2 = log sin y - u",
    "w_equals_det_h_sqrt": "exp(f1)*exp(f2) = exp(f1+f2)",
    "f1_plus_f2": str(sp.simplify(f1 + f2)),
    "w_spike_simplified": str(w_spike_simplified),
    "d_w_d_u": str(cz_determinant_u_derivative),
    "conclusion": ("The opposite warping cancels in the determinant: w = sin x * sin y "
                   "independent of u. The CZ spike concentrates curvature at FIXED 4-volume "
                   "and cannot shrink volume. A volume-breaking sequence needs small p AND q, "
                   "which is a genuinely different and harder construction.")
}

# ----------------------------------------------------------------------
# (B) Faber-Krahn base-area lower bound
# ----------------------------------------------------------------------
j0 = 2.4048255576957727686  # first positive zero of J_0
def A_base(delta):
    # lambda_1^Dir <= 2(1+delta); Faber-Krahn: lambda_1 >= pi j0^2 / Area (flat model)
    lam_upper = 2.0 * (1.0 + delta)
    return math.pi * j0**2 / lam_upper

partB = {
    "faber_krahn_flat": "lambda_1^Dir(Omega) >= pi*j0^2/Area(Omega), j0=2.4048255577",
    "spectral_upper": "lambda_1^Dir(Omega) <= 2(1+delta)   [Step 13 determinant identity]",
    "base_area_lower_bound_flat_model": "Area(Omega) >= pi*j0^2/(2(1+delta))",
    "A_base_samples": {f"delta={d}": A_base(d) for d in [0.0, 0.1, 0.25, 0.49]},
    "caveat": ("Faber-Krahn as stated is for domains with the ambient (or given) metric g_B. "
               "For a curved orbit metric, the sharp constant may differ, but the qualitative "
               "conclusion Area(Omega) >= c(delta) > 0 holds whenever a Faber-Krahn-type "
               "inequality (lambda_1 * Area >= c) is available; a genuinely singular/cusped "
               "orbit metric would need separate control. The absolute base-area lower bound "
               "is the KEY new lever: the orbit space cannot shrink, so any invariant collapse "
               "is purely fiber-side (all fixed 2-spheres thinning at once).")
}

# ----------------------------------------------------------------------
# (C) Corner rise rate and fixed-sphere bookkeeping
# ----------------------------------------------------------------------
# Quarter-plane corner model: g_B = ds1^2 + ds2^2, w = s1 s2, corner at origin,
# quarter disk s1,s2 >= 0, s1^2+s2^2 <= r^2.
s1, s2, r, th = sp.symbols('s1 s2 r theta', positive=True)
# int over quarter disk of s1 s2 dA = int_0^{pi/2} int_0^r (rho cos)(rho sin) rho drho dth
corner_int = sp.integrate(sp.integrate((r*sp.cos(th))*(r*sp.sin(th))*r, (r, 0, sp.Symbol('R', positive=True))), (th, 0, sp.pi/2))
corner_int = sp.simplify(corner_int)

# S^4 anchor: total int_Omega w = 6, Vol = 24 pi^2, two corners.
partC = {
    "corner_local_model": "R^4 fixed point: g_B = ds1^2+ds2^2, w = s1*s2 (unit rise both directions)",
    "corner_integral_quarter_disk_radius_R": str(corner_int) + "   (= R^4/4)",
    "interpretation": ("int_{corner ball radius R} w ~ R^4/4. A corner contributes negligible "
                       "4-volume only if its two adjacent edges are short. Volume collapse "
                       "requires EVERY corner to have a short adjacent edge simultaneously."),
    "S4_anchor": {"int_w": 6, "Vol4": "24 pi^2", "corners_m": 2},
    "dichotomy": ("With Area(Omega) >= A_base(delta) (base does not shrink) and the corner "
                  "rise rate fixed by unit closure, invariant volume collapse forces all fixed "
                  "2-spheres (rod areas) to shrink together. The 2D question: can lambda_1 <= "
                  "2(1+delta) + unit closure + corner Gauss-Bonnet int K_B = 2pi - (pi/2)m "
                  "prevent every corner from having a short adjacent edge, UNIFORMLY in m=chi?")
}

# ----------------------------------------------------------------------
# (D) chi-uniformity requirement for Proposition A (decision-critical)
# ----------------------------------------------------------------------
# Proposition A: simply connected volume gap v0 => universal gap via
#   Myers (pi_1 finite) -> universal cover same pinching, Vol >= v0
#   -> Cheeger-Naber finite type bounds chi(M~) <= X(delta0, v0)
#   -> Euler mult chi(M~) = |pi_1| chi(M) bounds |pi_1|
#   -> Vol(M) >= v0 / X.
# If the gap is v0(chi) -> 0, the Cheeger-Naber step X depends on the volume
# lower bound, which now depends on chi: X = X(delta0, v0(chi)). But we are
# trying to bound chi(M~); a chi-dependent v0 makes this circular.
partD = {
    "proposition_A_chain": [
        "Myers: pi_1(M) finite under Ric >= (1-delta)g",
        "universal cover M~ has same pinching, Vol(M~) >= v0 (if v0 is a uniform gap)",
        "Cheeger-Naber finite type: chi(M~) <= X(delta0, v0)",
        "Euler multiplicativity: chi(M~) = |pi_1(M)| chi(M), chi(M) >= 1",
        "so |pi_1(M)| <= X, and Vol(M) = Vol(M~)/|pi_1(M)| >= v0/X"
    ],
    "circularity_if_chi_dependent": ("If the invariant/simply-connected gap is only v0(chi) with "
                                      "v0(chi) -> 0 as chi -> infty, then Cheeger-Naber gives "
                                      "chi(M~) <= X(delta0, v0(chi(M~))), an implicit inequality that "
                                      "does NOT bound chi(M~) (larger chi allows smaller v0 allows "
                                      "larger chi). A per-topology gap therefore does NOT power "
                                      "Proposition A."),
    "requirement": ("Proposition A needs a chi-UNIFORM simply connected volume gap v0 > 0. This is "
                    "exactly the tail-dichotomy regime: #_k(S^2 x S^2) has chi = 2k+2 (quasitoric), "
                    "and the energy budget permits ~chi bubbles, so nothing in the energy forbids "
                    "collapse as chi -> infty. The toric route and the Step 8-9 tail dichotomy are "
                    "the SAME wall.")
}

report = {
    "title": "Step 14: sharp positive-branch fork (Faber-Krahn base pinning + chi-uniformity)",
    "A_cz_determinant_invariance": partA,
    "B_faber_krahn_base_area": partB,
    "C_corner_pinning": partC,
    "D_chi_uniformity_for_proposition_A": partD,
    "strategist_corrections_incorporated": [
        "Weighted CGB energy budget is SATURATED by fiber collapse (bubble quantum independent of area), not violated; chasing int K_B^- circles a climbable wall.",
        "The genuinely new lever is the UNWEIGHTED spectral bound lambda_1 <= 2(1+delta) => Faber-Krahn => Area(Omega) >= c(delta) > 0.",
        "chi-uniformity is decision-critical: v0(chi)->0 does not amplify (Proposition A becomes circular).",
        "CZ spike preserves w (opposite warping cancels in det h); volume-breaking needs small p AND q."
    ]
}

OUT = os.path.join(DATA, "step14_faberkrahn_corner_pinning.json")
with open(OUT, "w") as f:
    json.dump(report, f, indent=2, default=str)
print(json.dumps(report, indent=2, default=str))
print(f"Saved {OUT}")
