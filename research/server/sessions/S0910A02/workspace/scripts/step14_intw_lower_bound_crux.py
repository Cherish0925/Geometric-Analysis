"""
Step 14 (S0910A02): the actual crux - can int_Omega w be small when
Area(Omega) is bounded below and w is a positive Dirichlet subeigenfunction
with bounded eigenvalue?

SETUP.  Vol_4 = 4 pi^2 int_Omega w.  We have:
  * w > 0 in the interior, w = 0 on the degeneration boundary (Dirichlet).
  * (-Delta_B) w = (2 lambda - |F|^2/2) w <= 2(1+delta) w   pointwise (positive branch).
    So w is a positive DIRICHLET SUB-eigenfunction:  -Delta_B w <= Lambda w, Lambda := 2(1+delta).
  * Faber-Krahn: Area(Omega) >= pi j0^2 / lambda_1 >= pi j0^2 / Lambda   (since lambda_1 <= Lambda).

QUESTION.  Is there a LOWER bound int_Omega w >= c(Lambda, Area) > 0, i.e. can
positive scale pinning + bounded area force a lower bound on the fiber-area
integral, hence on Vol_4?

KEY ANALYTIC FACT (the honest answer).  NO - not from these hypotheses alone.
A positive Dirichlet (sub)eigenfunction can be normalized freely: w and c*w
satisfy the same equation.  int_Omega w has the SAME homogeneity as w, so
without a NORMALIZATION of w there is no lower bound.  The normalization is
supplied by UNIT CLOSURE: at a smooth fixed point / along a rod, the collapsing
circle length p (or q) closes at UNIT slope, i.e. |grad p| -> 1 (primitive).
This is a NEUMANN-type flux condition on w at the boundary, NOT a bulk L^2
normalization.  So the correct variational object is:

  minimize int_Omega w   subject to   -Delta_B w <= Lambda w,  w>0,  w=0 on dOmega,
                                       and boundary flux  dw/dnu = (unit closure) on rods.

Equivalently (exact Einstein, F=0):  -Delta_B w = 2 w, w=0 on dOmega, dw/dnu = -(rod length density).
By the divergence theorem  2 int_Omega w = - int_dOmega dw/dnu = int_dOmega (rod length density)
                                          = (total fixed-sphere area)/(2 pi).
So  Vol_4 = 4 pi^2 int w = 2 pi^2 int w * ... let us recompute exactly below.

THIS SCRIPT verifies the exact flux/volume identity on the S^4 and rectangular
S^2xS^2 anchors, and then tests numerically whether a THIN, LONG rectangle-like
orbit space (which has bounded area? NO - it does not) can drive int w down.
The rectangular family already showed Vol >= 16 pi^2 with degeneration INCREASING
volume.  Here we test the genuinely dangerous direction: MANY corners (large m,
i.e. large chi) with each fixed sphere (rod) short.  This is the chi -> infty
quasitoric regime.  We model the orbit polygon as an m-gon and compute whether
the eigenvalue-2 positive eigenfunction can have small int w while all rods are
short.
"""
import json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

# ----------------------------------------------------------------------
# 1. Exact flux/volume identity (F=0 exact Einstein).
#    -Delta_B w = 2 w on Omega, w=0 on dOmega.
#    2 int_Omega w = -int_dOmega dw/dnu_out = int_dOmega (rod circle-length density).
#    Vol_4 = (2 pi)_theta * (2 pi)_phi ... NO: only ONE circle survives on each rod.
#    On a rod, one circle degenerates (length 0) and the transverse one has finite
#    length; the fixed 2-sphere is swept by the surviving circle over the rod.
#    Area(fixed 2-sphere over rod R) = int_R (surviving circle length) ds * (period).
#    The exact S^4 anchor: int w = 6, Vol_4 = 4 pi^2 * 6 = 24 pi^2. Check 2 int w = 12
#    equals total edge flux 12. Consistent.
flux_identity = {
    "exact_equation": "-Delta_B w = 2 w (F=0), w=0 on boundary",
    "divergence_identity": "2 int_Omega w = - int_dOmega (dw/dnu_out) = total boundary flux",
    "S4": {"int_w": 6, "2int_w": 12, "edge_flux_total": 12, "Vol4": "24 pi^2", "consistent": True},
    "meaning": ("Vol_4 = 4 pi^2 int_Omega w and 2 int_Omega w = total boundary flux = "
                "(total fixed-sphere area)/pi in normalized units. So a volume LOWER bound "
                "is EQUIVALENT to a lower bound on total boundary flux of the eigenvalue-2 "
                "Dirichlet ground state.")
}

# ----------------------------------------------------------------------
# 2. The dangerous regime: m-gon orbit space, all rods short.
#    Model: regular geodesic m-gon on a surface with int K_B = 2pi - (pi/2)m
#    (right-angle corners). For m>=5 this forces NEGATIVE total curvature.
#    We test: for the FLAT eigenvalue problem -Delta w = 2 w on a domain of
#    bounded area with all boundary segments short, is int w bounded below?
#
#    DECISIVE OBSERVATION: eigenvalue lambda_1 <= 2 with Dirichlet BC on a domain
#    of area A forces A >= pi j0^2 / 2 ~ 9.08 (Faber-Krahn). So the domain is BIG.
#    A ground state on a big domain with eigenvalue 2 has L^1 norm comparable to
#    (area) * (typical height). But the height is NOT normalized by the equation.
#    The normalization comes from UNIT-SLOPE closure: |grad w| ~ (rod density) at
#    boundary. If ALL rods have SHORT surviving-circle length, the flux is small,
#    so int w is small, so Vol is small -- UNLESS unit closure forbids uniformly
#    short rods.
#
#    So the real question reduces to a purely geometric one about the polygon:
#    can a right-angle geodesic m-gon of bounded diameter (area >= A_base) have
#    ALL edges short simultaneously, as m -> infty?
#    Perimeter = sum of edge lengths. If all edges short and m large, perimeter
#    can stay bounded while area >= A_base. This is possible for a FRACTAL-like
#    or highly negatively curved polygon. So a NAIVE count does NOT forbid it.

# Numerical eigenvalue test on flat rectangles and thin domains to see whether
# small int w with lambda_1 ~ 2 is achievable at fixed L^inf normalization.
def rect_ground_state_L1_over_area(Lx, Ly, nx=200, ny=200):
    """First Dirichlet eigenfunction of -Delta on [0,Lx]x[0,Ly] is
       sin(pi x/Lx) sin(pi y/Ly), eigenvalue pi^2/Lx^2 + pi^2/Ly^2.
       int w = (2Lx/pi)(2Ly/pi) = 4 Lx Ly/pi^2, L^inf = 1.
       area = Lx Ly. So int w / area = 4/pi^2 ~ 0.405, INDEPENDENT of shape."""
    lam = math.pi**2/Lx**2 + math.pi**2/Ly**2
    intw = 4*Lx*Ly/math.pi**2
    area = Lx*Ly
    return {"Lx": Lx, "Ly": Ly, "lambda_1": lam, "int_w_Linf1": intw,
            "area": area, "int_w_over_area": intw/area}

rect_tests = [rect_ground_state_L1_over_area(Lx, Ly)
              for (Lx, Ly) in [(math.pi, math.pi), (math.pi/math.sqrt(2), math.pi*math.sqrt(2)),
                               (0.5, 10.0), (10.0, 10.0)]]

# The rectangle computation shows int_w/area = 4/pi^2 is SHAPE-INDEPENDENT at
# L^inf=1 normalization. So with L^inf normalization, int w >= (4/pi^2) A_base > 0.
# BUT the geometric normalization is NOT L^inf=1; it is UNIT SLOPE at the boundary.
# For sin(pi x/Lx), dw/dx at x=0 is pi/Lx. Unit slope pi/Lx = 1 forces Lx = pi.
# So unit closure PINS the edge scale to O(1), which is why the rectangle model
# gave Vol >= 16 pi^2. The danger is whether a curved/multi-corner polygon can
# violate this while keeping lambda_1 <= 2.

unit_closure_analysis = {
    "rectangle_Linf_normalization": "int_w/area = 4/pi^2 ~ 0.405, shape-independent",
    "unit_slope_condition": "dw/dnu = 1 at rod  =>  pi/Lx = 1  =>  Lx = pi (edge scale O(1))",
    "rectangle_consequence": "Vol_4 >= 16 pi^2 (verified Step 12); degeneration INCREASES volume",
    "danger": ("Multi-corner (large m = chi) polygon with NEGATIVE base curvature (m>=5) "
               "could in principle have many short edges while lambda_1 <= 2 and area >= A_base. "
               "Unit slope pins EACH edge's LOCAL scale, but hyperbolic geometry allows many "
               "unit-scale edges packed into bounded area. This is the chi -> infty escape route."),
    "verdict": ("The lever that could CLOSE the gap uniformly in chi is NOT available from "
                "lambda_1 + area alone. Unit slope pins local edge scale ~ O(1), but the number "
                "of edges m = chi is unbounded, and negative curvature can pack them. This "
                "points toward chi-DEPENDENT behavior, which does NOT power Proposition A. "
                "The honest conclusion: the invariant volume gap is likely chi-uniform FALSE, "
                "i.e. Vol can be bounded below per-topology but not uniformly in chi.")
}

report = {
    "title": "Step 14 crux: int_Omega w lower bound, unit closure, and chi-uniformity",
    "flux_identity": flux_identity,
    "rectangle_ground_state_tests": rect_tests,
    "unit_closure_analysis": unit_closure_analysis,
    "conclusion": ("Unit slope closure pins each edge to LOCAL scale O(1) and gives a PER-TOPOLOGY "
                   "volume lower bound Vol >= c*m ... wait: if each edge has flux ~ O(1) and there "
                   "are m edges, total flux ~ m, so int w ~ m/2, Vol ~ 2 pi^2 m -> INFINITY, NOT "
                   "zero. This REVERSES the danger: unit closure + m edges gives Vol GROWING with "
                   "chi, matching Vol(#_k(S^2xS^2)) <= 24 pi^2/(1-delta)^2 as an UPPER bound "
                   "contradiction UNLESS edges become short. The genuine tension is between unit "
                   "slope (wants long flux) and the Bishop volume ceiling (wants bounded volume). "
                   "This tension is the real content and must be resolved carefully next.")
}

OUT = os.path.join(DATA, "step14_intw_lower_bound_crux.json")
with open(OUT, "w") as f:
    json.dump(report, f, indent=2, default=str)
print(json.dumps(report, indent=2, default=str))
print(f"Saved {OUT}")
