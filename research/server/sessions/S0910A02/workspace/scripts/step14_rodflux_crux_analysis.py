"""
Step 14 (S0910A02): Rod flux lower bound from unit closure and the
Bishop ceiling constraint.

KEY CHAIN:
  Vol_4 = 4 pi^2 int_Omega w                                              (1)
  2 int_Omega w = total boundary flux = sum_{rods} Phi_i                   (2)
  Bishop: Vol_4 <= 24 pi^2 / (1-delta)^2                                   (3)
  =>  total flux = sum Phi_i <= 12 / (1-delta)^2                           (4)

  If each rod has flux Phi_i >= Phi_min > 0, then
  m <= 12 / ((1-delta)^2 Phi_min)  =>  chi(M) is BOUNDED by delta only.    (5)

This would IMMEDIATELY imply the chi-UNIFORM volume gap if Phi_min > 0
universally, because Proposition A then does NOT need a volume input at all:
  chi(M) <= C(delta)  +  Faber-Krahn + unit slope  =>  each rod flux ~ O(1/m_max).

QUESTION: what is Phi_i and is there a universal lower bound?

For a twist-free exact Einstein metric (F=0), the orbit-volume function
w = p*q satisfies -Delta_B w = 2 w on the polygon Omega, with w=0 on the
boundary. On a rod R_i where the circle with angle theta collapses (p->0),
the remaining circle with angle phi has length 2 pi q along the rod. The
outward normal derivative of w at the rod is
  -dw/dnu = (dp/dnu) q = 1 * q     (unit closure: dp/dr -> 1 as p->0).
The flux over rod R_i is then
  Phi_i = int_{R_i} q ds = (Area of fixed 2-sphere over R_i) / (2 pi).

The fixed 2-sphere has metric ds^2 + Q(s)^2 d phi^2 (Q = q on the rod, phi period 2 pi).
Its area is 2 pi int_{R_i} Q ds = 2 pi Phi_i.

Now from Gauss-Bonnet on the fixed 2-sphere (which is topologically S^2):
  int K_Sigma dA_Sigma = 4 pi.  With K_Sigma = -Q''/Q:
  -int Q'' ds * 2 pi = 4 pi  =>  int Q'' ds = -2.
  But Q(s) = 0 at the endpoints of the rod (where the 2-sphere meets the other
  rods at the corners/vertices), and Q'(endpoint) = +-1 (primitive closure of the
  transverse circle at the vertex). So:
  Q'(L_i) - Q'(0) = int_0^{L_i} Q'' ds = -2, i.e. Q'(L_i) - Q'(0) = -2.
  With Q'(0) = 1 (outward slope at start vertex, primitive) and Q'(L_i) = -1
  (inward slope at end vertex): (-1) - (1) = -2. Check!

  The area of the fixed 2-sphere is then:
  Area(Sigma_i) = 2 pi int_0^{L_i} Q(s) ds.
  Q(s) satisfies Q'' + (1 + 2 a_2(s)) Q = 0, Q(0) = 0, Q'(0) = 1.
  So Q(s) ~ s for small s, Q(L_i) = 0, Q'(L_i) = -1.

  For CONSTANT a_2 = 0 (flat base at edge): Q'' + Q = 0, Q(s) = sin s,
  L_i = pi, int_0^pi sin s ds = 2, Area = 4 pi. This is the S^2xS^2 or S^4 rod.

  For variable a_2, we need to analyze Q'' + (1 + 2 a_2(s)) Q = 0 with
  Q(0) = Q(L) = 0, Q'(0) = 1, Q'(L) = -1. These are exactly the conditions
  for a smooth Einstein 2-sphere. By Sturm-Liouville theory, the first positive
  zero L of Q is a CONTINUOUS function of a_2; for the constant a_2 case,
  L_{max} = pi/sqrt(1+2 a_2). Large a_2 -> short L, short rod, short 2-sphere.

  But NOW: is Phi_i = int_0^{L_i} Q ds bounded below UNIVERSALLY?
  For constant positive a_2 = A: Q = sin(omega s)/omega, omega = sqrt(1+2A),
  L_i = pi/omega, Phi_i = int_0^{pi/omega} sin(omega s)/omega ds = 2/omega^2.
  As A -> infty, omega -> infty, Phi_i = 2/omega^2 -> 0.

  SO: the flux per rod CAN go to zero. Large a_2 (large negative K_B at edge)
  shrinks the rod and the flux. This does NOT violate Faber-Krahn because the
  base area stays bounded below, and it does NOT violate Gauss-Bonnet because
  int K_B = 2pi - (pi/2) m can be very negative for large m.

  HOWEVER: the TOTAL FLUX has an exact identity:
  sum_i Phi_i = 2 int_Omega w.
  And int w = (Vol_4)/(4 pi^2).
  Bishop: Vol_4 <= 24 pi^2/(1-delta)^2, so total flux <= 12/(1-delta)^2.
  And the question was about a LOWER bound, not upper. We need total flux >= c > 0.

  From the eigenfunction equation: 2 int_Omega w = total flux, and
  also 2 int_Omega w = int_Omega (-Delta_B w) (no wait, -Delta_B w = 2w gives
  int_Omega (-Delta_B w) = 2 int_Omega w, but int (-Delta w) = -int dw/dnu = total flux
  by the divergence theorem, so 2 int w = total flux. This is consistent.)

  For the total flux to vanish we need int_Omega w -> 0, i.e. w -> 0 in L^1.
  But w is a positive GROUND STATE of -Delta with eigenvalue 2 on a domain of
  area >= A_base > 0. Can such a ground state have ||w||_L1 -> 0?

  YES: multiply w by epsilon. The eigenfunction equation is LINEAR, so epsilon w
  is also a solution. The normalization is from unit closure. If EVERY rod has
  Q ~ epsilon (because omega is large), then w ~ epsilon on most of the domain,
  and ||w||_L1 ~ epsilon * area -> 0 while area >= A_base > 0.

  This is the mechanism: the collapsing circles have length epsilon, which makes
  w ~ epsilon, which makes Vol ~ epsilon. The base stays big. This is a "fiber
  collapse to a surface" -- a well-known phenomenon. The 4-manifold collapses
  to its 2D orbit space with bounded geometry.

  CRITICAL REALIZATION: this IS exactly the torus-fiber collapse that Einstein
  lens spaces demonstrate in odd dimensions. In 4D toric terms, making all fibers
  thin simultaneously while keeping the base big IS the collapse mechanism. The
  Faber-Krahn / spectral bound does NOT prevent it; it just says the limit
  surface has bounded geometry.

  BUT WAIT: unit closure says dp/dr -> 1, not dp/dr -> epsilon. The collapse
  needs the circle LENGTH 2 pi p to be small, but the SLOPE dp/dr is always 1
  at the rod. So near the rod, p ~ r (the normal coordinate), which PINS p to
  be O(distance from rod). If the rod is at distance L from the interior, then
  p_max on that rod ~ L. So short rods (L small) give small p_max, hence small
  w along that rod. But DEEP in the interior, far from all rods, p and q can
  be arbitrary (subject to the eigenvalue equation).

  For all circle lengths to be small everywhere, we need both p and q to be
  small in the interior. With -Delta(pq) = 2 pq and pq = 0 on the boundary,
  the maximum of pq is in the interior. The L^inf of pq on a domain of area A
  with eigenvalue 2 satisfies (by a reverse Faber-Krahn/eigenfunction bound):
  ||w||_Linf <= C lambda / area? No, this goes the wrong way.

  Actually the L^inf of the ground state ON A FIXED domain with eigenvalue lambda
  can be arbitrarily large or small (multiply by a constant). The normalization
  is ENTIRELY from the unit closure boundary condition. So the correct question
  is: given that dp/dnu = 1 on each p-rod and dq/dnu = 1 on each q-rod, what
  is the minimum of int_Omega pq?

  This is a genuinely hard two-dimensional variational question. Let me check
  the rectangle family analytically as a pilot.
"""
import json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

# Rectangle family check: p = sin(pi x / Lx), q = sin(pi y / Ly).
# Unit closure: dp/dx|_{x=0} = pi/Lx. For this to be 1: Lx = pi.
# Similarly Ly = pi. Eigenvalue condition: pi^2/Lx^2 + pi^2/Ly^2 = 2 => 1 + 1 = 2. OK.
# int w = int_0^pi int_0^pi sin x sin y dx dy = 4. Vol = 4 pi^2 * 4 = 16 pi^2.
# This is the S^2 x S^2 ground state.
#
# But for a GENERAL polygon with m corners, the edge lengths L_i satisfy:
# on each rod, Q'' + (1 + 2 a_2) Q = 0, Q(0)=0, Q'(0)=1, Q(L)=0, Q'(L)=-1.
# The simplest UNIFORM collapse model: a_2 -> infinity on all edges, making L -> 0.
# Then what happens in the interior? If all rods are short, the polygon is a
# small neighborhood of the vertex graph. But the area must be >= A_base > 0
# (Faber-Krahn). So the polygon has big interior but short edges. Near a vertex
# the local model is R^2 quarter-plane with w = s1 s2 ~ r^2, but s1, s2 rise
# only to ~ L ~ 0 before hitting the next vertex. So w_max ~ L^2 ~ 0.
#
# WAIT: this contradicts the eigenvalue equation! If w -> 0 uniformly on a
# domain of area >= A_base, then ||w||_L2 -> 0, but the eigenvalue lambda_1 of
# the domain is pi j0^2 / area, which gives a Rayleigh bound
# int |grad w|^2 / int w^2 = lambda_1 = 2. But if w -> 0 while area is bounded,
# int w^2 -> 0, so int |grad w|^2 -> 0. Then by Poincaré, w -> 0 in H^1.
# But |grad w| ~ 1 near each rod (unit slope!), and the "rod neighborhood"
# has some area. So int |grad w|^2 >= (measure of rod neighborhood) * (1/something).
#
# KEY COMPUTATION: near a rod at distance r from boundary, |grad w| >= |grad p| q,
# and |grad p| >= 1 - O(r) by the unit-slope condition (p ~ r).
# Actually more carefully: in the normal coordinate r from a rod,
# p ~ r, q ~ Q(s) where Q is the transverse circle profile.
# |grad w| = |q grad p + p grad q| >= |q dp/dr| - |p dq/ds|
#          >= q * 1 - p * |Q'| (near rod)
#          >= q (1 - r |Q'|/Q * Q/q) ... this needs more care.
#
# A cleaner approach: int_Omega |grad w|^2 >= int of (grad w)^2 over a thin strip
# near the boundary. On a rod of length L_i, p < epsilon (thin strip width epsilon),
# q ranges from 0 to Q_max ~ L_i/something.
# (grad w)^2 ~ (dp/dr)^2 q^2 + ... >= q^2 near the rod.
# int_strip >= int_0^{L_i} int_0^epsilon q(s)^2 ds dr = epsilon * int_0^{L_i} Q(s)^2 ds.
# For Q(s) = sin(omega s)/omega with omega = sqrt(1+2a_2): int Q^2 = L/(2 omega^2) = pi/(2 omega^3).
# As a_2 -> infty: this -> 0. So the H^1 seminorm near short rods CAN go to zero.
#
# But we also have the INTERIOR contribution. On a domain of area A >> epsilon^2
# with w = pq and -Delta w = 2w, the interior has w ~ smooth, and if |w| <= M
# everywhere, then int |grad w|^2 = 2 int w^2 <= 2 M^2 A.
# For collapse, M = max(pq) -> 0 as all rods shorten, so this is self-consistent.
#
# CONCLUSION: The unit-slope + eigenvalue equation does NOT by itself give a
# chi-uniform lower bound on int w. The mechanism is: as all rod lengths L_i -> 0
# (via a_2 -> infty on all edges), the ground state w = pq -> 0 in L^inf and
# hence L^1, while the domain area stays bounded below (Faber-Krahn). The
# normalization from unit slope becomes irrelevant in the bulk interior: w rises
# to ~ L^2 near each corner and stays ~ 0 in the big interior plateau.
#
# HOWEVER: is such a polygon actually consistent with being a SMOOTH toric
# Einstein orbit space? The Gauss-Bonnet constraint is
# int K_B = 2 pi - (pi/2) m.  Large a_2 on all edges means K_B << 0 near all
# edges. The integral constraint allows this for m >= 5 (where it is already
# negative). But also, the INTERIOR must have smooth geometry with the eigenvalue
# equation -Delta w = 2 w, and the base metric g_B must be smooth.
# The base curvature K_B from the Ricci equation and the eigenvalue equation
# is NOT free; it is determined by the Einstein system. So we cannot freely
# choose a_2 -> infty independently on all edges.
#
# This is where the EXACT reduced Einstein system constrains things. For the
# polar (F=0) system: -Delta_B w = 2w, Ric_B + Hess(log w) = g_B (from the
# base block of Ric = g, after reducing). So K_B = 1 - Delta log w.
# K_B is determined by w, not a free parameter. The question is whether a
# positive ground state w of -Delta w = 2w on a polygon can satisfy
# K_B = 1 - Delta log w with K_B << 0 near all boundaries simultaneously.

# Let me compute K_B = 1 - Delta log w for a known case. On S^2 x S^2:
# w = sin x sin y. log w = log sin x + log sin y.
# Delta log w = -cot^2 x - 1 + (-cot^2 y - 1) = -csc^2 x - csc^2 y + 2.
# Wait: d/dx log sin x = cos x / sin x = cot x. d^2/dx^2 = -csc^2 x.
# Delta log w = -csc^2 x - csc^2 y.
# K_B = 1 - Delta log w = 1 + csc^2 x + csc^2 y.
# At the interior point (pi/2, pi/2): K_B = 1 + 1 + 1 = 3.
# Near the edge x = 0: csc^2 x -> infinity, so K_B -> +infinity!
# That means near the rods, K_B is ALWAYS large positive, not negative.
# This is the opposite of what the collapsing model needs!

# Let me verify: for a general w satisfying -Delta w = 2w, K_B = 1 - Delta log w.
# Delta log w = Delta w / w - |grad w|^2 / w^2 = -2 + |grad w|^2 / w^2 ... wait:
# Delta log w = (w Delta w - |grad w|^2) / w^2 ... no.
# In 2D: Delta f = d^2 f/dx^2 + d^2 f/dy^2.
# f = log w. df/dx = w_x/w. d^2f/dx^2 = (w_xx w - w_x^2)/w^2.
# Delta f = (w_xx + w_yy)/w - (w_x^2 + w_y^2)/w^2 = Delta w / w - |grad w|^2/w^2.
# = -2 w/w - |grad w|^2/w^2 = -2 - |grad w/w|^2.
# So K_B = 1 - Delta log w = 1 + 2 + |grad log w|^2 = 3 + |d log w|^2.
# K_B = 3 + |grad log w|^2 >= 3 > 0.

# THIS IS ENORMOUS. K_B >= 3 EVERYWHERE on the orbit space of a positive
# Einstein polar T^2-invariant metric. The base curvature is UNIFORMLY POSITIVE.
# And near rods where w -> 0, |grad log w| -> infinity, so K_B -> +infinity.
# This contradicts the m >= 5 Gauss-Bonnet allowance of negative total curvature!

# Gauss-Bonnet: int K_B = 2 pi - (pi/2) m. With K_B >= 3:
# 3 * Area(Omega) <= int K_B = 2 pi - (pi/2) m.
# For m >= 5: right side = 2pi - 5pi/2 = -pi/2 < 0. But left side >= 0.
# CONTRADICTION! So m >= 5 is IMPOSSIBLE for polar positive Einstein T^2 metrics.
# And m = chi(M), so chi(M) <= 4 for positive Einstein toric four-manifolds!

result = {
    "MAJOR_DISCOVERY": "K_B = 3 + |grad log w|^2 >= 3 for polar positive Einstein T^2-invariant metrics",
    "derivation": {
        "step1": "Delta log w = Delta w / w - |grad w|^2/w^2 = -2 - |grad log w|^2",
        "step2": "K_B = 1 - Delta log w = 1 + 2 + |grad log w|^2 = 3 + |grad log w|^2",
        "conclusion": "K_B >= 3 everywhere on the orbit space of a positive Einstein polar T^2-invariant metric"
    },
    "gauss_bonnet_constraint": {
        "identity": "int K_B dA = 2 pi - (pi/2) chi(M)",
        "with_lower_bound": "3 * Area(Omega) <= 2 pi - (pi/2) chi(M)",
        "chi_upper_bound": "chi(M) <= (4 pi - 6 Area(Omega)) / pi <= 4 (using Area >= 0)",
        "simple_bound": "chi(M) <= 4. Equality at Area = 0 but Area > 0 gives strict: chi(M) <= 3 or chi(M) = 4 with K_B identically 3."
    },
    "verification": {
        "S4_check": {"chi": 2, "OK": True, "m_vertices": 2, "int_K_B": "pi", "3_times_area_S4_quarter": "3 * (pi * 3 / 4) = 9pi/4 < pi"},
        "note_S4": "S4: Area(Omega) = area of spherical lune = pi*R^2/4 * angle? Let me compute properly below.",
        "S2xS2_check": {"chi": 4, "OK": True, "m_vertices": 4, "int_K_B": "0",
                         "but": "K_B = 3 + csc^2 x + csc^2 y >= 5; int K_B = 0 violates 3*A <= 0. CONTRADICTION."},
        "CP2_check": {"chi": 3, "OK": "to check"}
    },
    "WAIT": "S^2 x S^2 has K_B = 1 + csc^2 x + csc^2 y >= 3 (at (pi/2,pi/2) K_B=3), int K_B should be checked."
}

# Let me verify: S^2 x S^2 polar, orbit space = [0,pi] x [0,pi], g_B = dx^2 + dy^2.
# w = sin x sin y. K_B (of the FLAT metric g_B = dx^2 + dy^2) is 0.
# BUT: the formula K_B = 3 + |grad log w|^2 should give the base curvature of
# the INDUCED quotient metric, not the standard flat metric.
# I think the issue is that g_B is NOT flat for S^2xS^2. Let me reconsider.
#
# For S^2(1) x S^2(1) with coordinates (x, theta) on first S^2 and (y, phi) on second:
# g = dx^2 + sin^2 x dtheta^2 + dy^2 + sin^2 y dphi^2.
# The T^2 action rotates theta and phi. The orbit space has coordinates (x,y) in [0,pi]^2.
# The quotient metric IS g_B = dx^2 + dy^2 (flat!). The fiber metric has
# h = diag(sin^2 x, sin^2 y), so w = sin x sin y.
# K_B = 0 (flat). And the formula says K_B = 3 + |grad log w|^2 >= 3. Contradiction!
#
# So the formula is WRONG or does not apply to S^2xS^2.
# The issue: S^2(1)xS^2(1) has Ric = g but it is NOT normalized to Ric = g
# in the metric I wrote: Ric_{S^2(1)} = 1 * g_{S^2(1)}, so Ric_full = g. OK.
# Then K_B should be computed from the Einstein equation.
#
# The base Ricci condition for Ric_g = lambda g (with lambda=1) in a T^2 reduction is:
# Ric_B - Hess_B(log w) = lambda g_B  (this is the standard reduced horizontal equation).
# In 2D: Ric_B = K_B g_B. So: K_B g_B - Hess_B(log w) = g_B, i.e.
# K_B - (trace of Hess_B(log w))/2 != this formula.
# Wait, in 2D the Ricci tensor is K_B g_B. And Hess_B(log w) is a (0,2)-tensor.
# The equation K_B g_B - Hess_B(log w) = g_B means:
# K_B delta_ij - (log w)_{,ij} = delta_ij
# i.e. (log w)_{,ij} = (K_B - 1) delta_ij.
# This means Hess_B(log w) = (K_B - 1) g_B, i.e. log w is a CONFORMAL function.
# Taking the trace: Delta_B(log w) = 2(K_B - 1).
# But also Delta log w = -2 - |grad log w|^2 (from -Delta w = 2w).
# So 2(K_B - 1) = -2 - |grad log w|^2, giving K_B = -|grad log w|^2/2.
# That is K_B <= 0, not K_B >= 3!

# CORRECTION: I made an error. The base-horizontal Einstein equation is:
# Ric_B(X,Y) - Hess(log w)(X,Y) - 1/2 sum_I [F^I(X,-) F^I(Y,-)] h = lambda g_B.
# For the polar case F=0, it's Ric_B - Hess(log w) = lambda g_B.
# In 2D: K_B g - Hess(log w) = g. So Hess(log w) = (K_B - 1) g.
# Trace: Delta log w = 2(K_B - 1). And Delta log w = -2 - |d log w|^2.
# So 2K_B - 2 = -2 - |d log w|^2, hence K_B = -|d log w|^2 / 2 <= 0.

corrected_result = {
    "CORRECTION": "The base-horizontal Einstein reduction gives K_B = -|grad log w|^2/2 <= 0, NOT K_B >= 3.",
    "derivation": {
        "base_equation": "Ric_B - Hess(log w) = lambda g_B (polar, F=0)",
        "2D_form": "K_B g_B - Hess(log w) = g_B => Hess(log w) = (K_B - 1) g_B",
        "trace": "Delta log w = 2(K_B - 1)",
        "eigenvalue": "Delta log w = -2 - |grad log w|^2 (from -Delta w = 2w)",
        "combining": "2(K_B - 1) = -2 - |grad log w|^2 => K_B = -|grad log w|^2 / 2 <= 0"
    },
    "S2xS2_check": {
        "w": "sin x sin y (flat orbit space)",
        "grad_log_w": "(cot x, cot y)",
        "K_B_formula": "-(cot^2 x + cot^2 y)/2",
        "K_B_at_center": "-(0+0)/2 = 0 (flat at center, correct!)",
        "K_B_at_x=0": "-inf (negative infinity at edge, consistent with degeneration)"
    },
    "gauss_bonnet_check": {
        "S2xS2": "int K_B dA = int_0^pi int_0^pi -(cot^2 x + cot^2 y)/2 dx dy. Both int_0^pi cot^2 x dx diverge (-infinity). But this is the FLAT metric on the square; the orbit-space metric IS flat, and K_B should be 0. The discrepancy means the formula K_B = -|d log w|^2/2 is the base Gauss curvature only IF the base metric is the REDUCED metric, not the original quotient metric."
    },
    "resolution": "The base equation Hess(log w) = (K_B - 1) g_B forces log w to be a conformal function. In 2D, Hess f = (Delta f/2) g_B iff f is harmonic in isothermal coordinates PLUS a conformal factor. The formula K_B = -|d log w|^2/2 holds for the QUOTIENT metric g_B induced from the submersion, not for a conformally changed metric. For S^2 x S^2 with g_B = dx^2+dy^2, K_B = 0 (flat), and the formula gives 0 = -(cot^2 x + cot^2 y)/2 which is FALSE. So the base equation is WRONG for flat g_B."
}

# The error is in the base equation itself. Let me re-derive it from scratch.
# For g = g_B + p^2 dtheta^2 + q^2 dphi^2 (twist-free, diagonal), the horizontal
# Ricci tensor in 2D orbit space is:
# Ric_B^{(2D)} = Ric_B(g_B) (the intrinsic curvature of g_B)
# and the FULL 4D Ric restricted to horizontal directions is:
# Ric(X,Y)|_{hor} = Ric_B(X,Y) - (Hess p / p + Hess q / q)(X,Y).
# For Ric(X,Y) = lambda g(X,Y) = lambda g_B(X,Y) on horizontal vectors:
# Ric_B - Hess p / p - Hess q / q = lambda g_B.   (*)
# Taking trace: 2 K_B - Delta p / p - Delta q / q = 2 lambda.
# And from the vertical equations: Delta p / p = K_B - lambda + |grad p|^2/p^2 - ...
# This is getting complicated. Let me just check S^2 x S^2 directly.

# S^2(1) x S^2(1): g = dx^2 + sin^2 x dth^2 + dy^2 + sin^2 y dph^2.
# p = sin x, q = sin y. g_B = dx^2 + dy^2 (flat).
# Hess_B(p)/p: (d^2/dx^2)(sin x)/sin x = -1, and (d^2/dy^2)(sin x)/sin x = 0.
# So Hess(p)/p = diag(-1, 0) in (dx, dy) frame.
# Similarly Hess(q)/q = diag(0, -1).
# Hess(p)/p + Hess(q)/q = diag(-1, -1) = -I.
# So (*): 0 * I - (-I) = I = lambda I with lambda=1. CHECK!

# Now: Hess(log w) = Hess(log(sin x sin y)) = Hess(log sin x) + Hess(log sin y).
# Hess(log sin x) = d^2(log sin x)/dx^2 dx^2 = -csc^2(x) dx^2 (only xx component nonzero).
# Similarly for log sin y.
# So Hess(log w) = diag(-csc^2 x, -csc^2 y).
# (K_B - 1) g_B = -I, i.e. Hess(log w) should equal -I. But diag(-csc^2 x, -csc^2 y) != -I.

# So the relation Hess(log w) = (K_B - 1) g_B is FALSE for S^2 x S^2.
# The correct horizontal equation is NOT Ric_B - Hess(log w) = lambda g_B.
# Instead it is Ric_B - Hess p/p - Hess q/q = lambda g_B.
# And Hess p/p + Hess q/q != Hess(log(pq)) in general because
# Hess(log w) = Hess(log p) + Hess(log q) = (Hess p/p - dp^{otimes 2}/p^2) + similar.
# The cross terms |d log p|^2 + |d log q|^2 are missing.

s2_check = {
    "horizontal_equation_correct": "Ric_B - Hess(p)/p - Hess(q)/q = lambda g_B",
    "horizontal_equation_log_form": "Ric_B - Hess(log p) - |d log p|^2 g_B? NO: Hess(log p) = Hess(p)/p - dp tensor dp/p^2",
    "S2xS2_verification": {
        "Hess_p_over_p": "diag(-1, 0)",
        "Hess_q_over_q": "diag(0, -1)",
        "sum": "diag(-1, -1) = -I",
        "equation": "0 - (-I) = I = g_B. CHECK with lambda=1."
    },
    "log_w_equation": {
        "Hess_log_w": "diag(-csc^2 x, -csc^2 y)",
        "NOT_equal_to": "(K_B - 1) g_B = -I",
        "reason": "Hess(log(pq)) = Hess(p)/p + Hess(q)/q - (dp^2/p^2 + dq^2/q^2)",
        "missing_terms": "|d log p|^2 + |d log q|^2 tensor parts"
    },
    "conclusion": ("The earlier formula K_B = -|grad log w|^2/2 was derived from the FALSE "
                   "equation Hess(log w) = (K_B-1) g_B. The correct base equation is "
                   "Ric_B - Hess p/p - Hess q/q = lambda g_B, which involves the fiber lengths "
                   "SEPARATELY, not just their product w. This means the orbit-space curvature "
                   "K_B is NOT determined by w alone; it depends on p and q separately. "
                   "In particular K_B CAN be negative on some regions.")
}

full_report = {
    "title": "Step 14: crux analysis of int_w lower bound",
    "flux_identity": result["flux_identity"] if "flux_identity" in result else {"note": "see previous script"},
    "initial_K_B_formula": result,
    "correction": corrected_result,
    "s2xs2_direct_check": s2_check,
    "final_conclusion": {
        "K_B_formula_status": "RETRACTED. K_B is NOT determined by w alone. The earlier K_B >= 3 was wrong.",
        "base_curvature_truth": ("K_B depends on p, q separately via the horizontal Einstein equation "
                                  "Ric_B - Hess(p)/p - Hess(q)/q = lambda g_B. In 2D orbit space this "
                                  "gives 2 K_B - Delta p/p - Delta q/q = 2 lambda."),
        "volume_gap_status": ("The chi-uniform volume gap remains OPEN. The Faber-Krahn base-area bound "
                              "is established; the unit-slope normalization per rod is correct; but whether "
                              "all rods can simultaneously have small flux (int Q ds) while maintaining "
                              "the eigenvalue equation and smooth toric topology is unresolved. The answer "
                              "depends on the joint system for p, q, g_B and not just w. "
                              "A decisive test is a numerical FEM computation on a multi-corner "
                              "(m=6 or m=8) polygon with the full reduced Einstein system.")
    }
}

OUT = os.path.join(DATA, "step14_rodflux_crux_analysis.json")
with open(OUT, "w") as f:
    json.dump(full_report, f, indent=2, default=str)
print(json.dumps(full_report, indent=2, default=str))
print(f"Saved {OUT}")
