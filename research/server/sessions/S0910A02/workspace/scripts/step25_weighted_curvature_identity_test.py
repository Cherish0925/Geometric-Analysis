"""
Step 25: The weighted base-curvature identity int K_B w = int w and its
coupling to the rod flux identity int(1-2K_edge)Q = 2.

Session S0910A02, Agent2/Constructor, Execute.

GOAL (from the strategist note): one clean analytic verdict.
Couple the exact rod identity to the horizontal (base-trace) equation and
decide whether the coupled reduced system forces the Q-weighted curvature
sum  sum_i int(-K_edge) Q_i  to be bounded (BUILD) or not (BREAK) as the
number of rods m -> infinity in the periodic-label #_k(S^2 x S^2) family.

We use ONLY equations already verified in Steps 12-21:
  (1) vertical trace / eigenvalue:  -Delta_B w = 2 w,  w=0 on dOmega, lambda=1
  (2) vertical difference:          div_B(w grad v) = 0
  (3) traceless horizontal:         (log w)_zz + 1/2[(log w)_z^2 + v_z^2] = 0
  (4) horizontal trace:             K_B = 1/4(|grad v|^2 - |grad log w|^2)
  rod identity:                     int_rod (1-2K_edge) Q ds = 2,  Phi_i=int Q ds

We DO NOT run finite-difference PDE residuals on an uncontrolled global family
(the Step 18/20 trap the strategist flagged). This is exact algebra of
integral identities.
"""
import sympy as sp
import json
import os

OUT = {}

# ---------------------------------------------------------------------------
# PART A. Derive the weighted-curvature identity  int_Omega K_B w = int_Omega w
# ---------------------------------------------------------------------------
# The individual fiber-warping equations (Step 14, verified) are, for
#   g = g_B + p^2 dtheta^2 + q^2 dphi^2,  Ric = g:
#     -Delta_B p = (K_B - 1) p          (p vanishes at unit slope on p-rods)
#     -Delta_B q = (K_B - 1) q          (q vanishes at unit slope on q-rods)
#     <grad p, grad q> = -K_B p q
# Multiply the p-equation by q and integrate over Omega (Green's identity):
#   int_Omega grad p . grad q  -  int_Omega (K_B-1) p q  =  int_dOmega q d_nu p
# Use <grad p, grad q> = -K_B w:
#   -int K_B w - int(K_B-1) w = int_dOmega q d_nu p
#   -int(2 K_B - 1) w         = int_dOmega q d_nu p
# On a p-rod, p=0, |grad p|=1 (inward unit slope) so d_nu p = -1 and the
# surviving fiber q = Q(s); on a q-rod q=0 so the term vanishes. Hence
#   int_dOmega q d_nu p = - sum_{p-rods} int Q ds = - (flux through p-rods).
# Therefore
#   int(2 K_B - 1) w = flux through p-rods = Phi_p.
# Symmetric computation with the q-equation gives
#   int(2 K_B - 1) w = Phi_q.
# So Phi_p = Phi_q and total flux Phi = Phi_p + Phi_q = 2 int(2K_B - 1) w.
# But the eigenvalue equation gives total flux Phi = 2 int w. Equate:
#   2 int(2K_B - 1) w = 2 int w   ==>   int(2K_B - 1) w = int w
#                                  ==>   2 int K_B w = 2 int w
#                                  ==>   int_Omega K_B w = int_Omega w.       (WCI)

OUT["part_A_weighted_curvature_identity"] = {
    "individual_equations": [
        "-Delta_B p = (K_B - 1) p, p=0 unit-slope on p-rods",
        "-Delta_B q = (K_B - 1) q, q=0 unit-slope on q-rods",
        "<grad p, grad q> = -K_B w, w=pq",
    ],
    "derivation": "Green(p-eq * q) with <grad p,grad q>=-K_B w gives "
                  "int(2K_B-1)w = flux through p-rods = Phi_p; symmetric for q; "
                  "eigenvalue total flux = 2 int w forces the identity.",
    "identity_WCI": "int_Omega K_B w dA = int_Omega w dA",
    "meaning": "The w-weighted base curvature has average EXACTLY +1 "
               "(w>0 in interior, w=0 on boundary).",
}

# ---------------------------------------------------------------------------
# PART A'. Sanity check WCI on the three exact anchors.
# ---------------------------------------------------------------------------
# S^2 x S^2: g_B flat rectangle [0,pi]x[0,pi], w = sin x sin y, K_B = 0.
#   int K_B w = 0, int w = (int_0^pi sin)^2 = 2*2 = 4. WCI would give 0 = 4?!
# That cannot be right unless the flat-rectangle "K_B" secretly carries corner
# delta-curvature. Resolve carefully.
x, y = sp.symbols('x y', positive=True)
w_sq = sp.sin(x)*sp.sin(y)
int_w = sp.integrate(sp.integrate(w_sq, (x, 0, sp.pi)), (y, 0, sp.pi))
OUT["part_Aprime_anchor_S2xS2"] = {
    "w": "sin x sin y on [0,pi]^2",
    "int_w": str(int_w),
    "int_KB_w_smooth_interior": "0 (K_B=0 in the flat interior)",
    "resolution": "WCI must include the CORNER/edge curvature concentration: "
                  "the smooth interior K_B=0, but Gauss-Bonnet for the orbit "
                  "space assigns pi/2 exterior angle at each of the 4 corners. "
                  "The identity int K_B w = int w is an interior identity ONLY "
                  "if w vanishes fast enough at corners that corner curvature "
                  "carries no w-weight; since w = sin x sin y ~ x*y -> 0 "
                  "quadratically at each corner, corner delta-curvature has "
                  "ZERO w-weight. So the smooth-interior int K_B w must equal "
                  "int w = 4 -- contradiction with K_B=0. Hence the naive "
                  "identification is WRONG; the correct WCI carries the "
                  "SECOND-derivative (Hessian) structure, not scalar K_B.",
}

# The contradiction above is important: it shows the *scalar* reading
# "int K_B w = int w" is NOT literally true for the flat product. The correct
# statement, re-derived below, is that the flux partition identity is
#   Phi_p = int(2K_B - 1) w + (corner/edge boundary terms).
# For the flat rectangle the boundary term is exactly what supplies the flux.
# So WCI as a clean interior identity is FALSE in general; the honest content
# is the flux PARTITION with explicit boundary data. We record this correction.

OUT["part_Aprime_correction"] = {
    "verdict": "The clean interior identity int K_B w = int w is NOT valid; "
               "it drops boundary/corner contributions from the Green identity. "
               "For the flat product int K_B w = 0 but int w = 4.",
    "correct_object": "The honest identities are the FLUX identities: "
                      "total flux = 2 int w (eigenvalue), and the rod identity "
                      "int(1-2K_edge)Q = 2 per rod. These are boundary-anchored "
                      "and DO hold. The interior weighted-curvature average is "
                      "NOT pinned by a clean scalar identity.",
}

# ---------------------------------------------------------------------------
# PART B. The genuine coupling: rod identity vs the traceless equation.
# ---------------------------------------------------------------------------
# Rod identity (verified, boundary-anchored):
#   Phi_i = int_{rod_i} Q_i ds = 2 + 2 int_{rod_i} K_edge Q_i ds.
# Define the Q-weighted negative-curvature charge of rod i:
#   G_i := int_{rod_i} (-K_edge) Q_i ds  >= 0  (for K_edge <= 0 collars).
# Then  Phi_i = 2 - 2 G_i, so  0 <= Phi_i <= 2  requires  0 <= G_i <= 1.
# Total flux  Phi = sum Phi_i = 2m - 2 sum G_i, and volume Vol_4 = 2 pi^2 Phi.
# For BREAK (Vol -> 0) we need  Phi = sum(2 - 2G_i) -> 0, i.e.
#   sum_i G_i -> m   with each  G_i -> 1.
# So the WHOLE question is whether the coupled system permits every rod to have
# G_i -> 1, i.e. each rod's Q-weighted negative curvature charge saturates 1.

# For a single constant-K_edge=-A rod:  Q=sin(w s)/w, w=sqrt(1+2A), L=pi/w.
A = sp.symbols('A', positive=True)
wro = sp.sqrt(1 + 2*A)
s = sp.symbols('s', positive=True)
Q = sp.sin(wro*s)/wro
L = sp.pi/wro
Phi_i = sp.integrate(Q, (s, 0, L))
G_i = sp.integrate(A*Q, (s, 0, L))     # (-K_edge)=A
Phi_i = sp.simplify(Phi_i)
G_i = sp.simplify(G_i)
OUT["part_B_single_rod"] = {
    "Q": "sin(sqrt(1+2A) s)/sqrt(1+2A)",
    "L": "pi/sqrt(1+2A)",
    "Phi_i": str(Phi_i),
    "G_i = int(-K_edge)Q": str(G_i),
    "check_Phi=2-2G": str(sp.simplify(Phi_i - (2 - 2*G_i))),
    "limit_G_as_A_to_inf": str(sp.limit(G_i, A, sp.oo)),
    "limit_Phi_as_A_to_inf": str(sp.limit(Phi_i, A, sp.oo)),
}

# So a SINGLE constant-A rod already gives G_i = A/(1+2A) -> 1/2, NOT 1.
# Therefore a constant-curvature collar saturates G_i at 1/2, giving
#   Phi_i = 2 - 2*(1/2) = ... let's check:
Phi_from_G = sp.simplify(2 - 2*G_i)
OUT["part_B_single_rod"]["Phi_recovered_from_2-2G"] = str(Phi_from_G)
OUT["part_B_single_rod"]["G_i_max_over_A"] = str(sp.limit(G_i, A, sp.oo))
OUT["part_B_single_rod"]["KEY"] = (
    "A CONSTANT negative-curvature rod has G_i = A/(1+2A) -> 1/2, so its flux "
    "Phi_i = 2/(1+2A) -> 0 while G_i -> 1/2, NOT 1. The rod identity "
    "Phi_i = 2 - 2 G_i then FAILS numerically unless we track it exactly: "
    "check below."
)
# Reconcile: Phi_i = 2/(1+2A). And 2 - 2 G_i where G_i = A/(1+2A):
#   2 - 2A/(1+2A) = (2(1+2A) - 2A)/(1+2A) = (2 + 2A)/(1+2A). 
# That is NOT 2/(1+2A)! So there is a sign/derivation slip to resolve.
reconcile = sp.simplify(2 - 2*(A/(1+2*A)) - 2/(1+2*A))
OUT["part_B_reconcile"] = {
    "2-2G_i": str(sp.simplify(2 - 2*A/(1+2*A))),
    "Phi_i_direct": str(sp.simplify(2/(1+2*A))),
    "difference": str(reconcile),
    "note": "If these differ, the rod identity constant or the sign of the "
            "curvature term in Q''+(1-2K)Q=0 must be re-derived. Resolve now.",
}

with open(os.path.join(os.path.dirname(__file__), "..", "data",
          "step25_weighted_curvature_identity_test.json"), "w") as f:
    json.dump(OUT, f, indent=2)
print(json.dumps(OUT, indent=2))
