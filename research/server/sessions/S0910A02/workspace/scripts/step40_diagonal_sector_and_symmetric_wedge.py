#!/usr/bin/env python3
"""Step 40: Diagonal-sector verification and symmetric-wedge eigenvalue analysis.

Three independent computations:
1. Diagonal-sector structural check: verify that h diagonal + label (a,b) 
   forces a=0 or b=0 (only ±e1, ±e2 labels).
2. Right-angled polygon side length vs rod length: exact formulas for all m.
3. Eigenvalue constraint: lambda_1(Sigma) = 2Lambda for the orbit-space Dirichlet problem.

Session S0910A02, Agent2/Constructor, Phase Execute.
"""
import json, math, os
from fractions import Fraction

OUT = "Sessions/S0910A02/workspace/data/step40_diagonal_sector_and_symmetric_wedge.json"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

results = {}

# ============================================================
# 1. Diagonal-sector structural verification
# ============================================================
# For a diagonal fiber metric h = diag(p^2, q^2) in a fixed lattice basis,
# a rod with label v=(a,b) requires h(v,v) = a^2 p^2 + b^2 q^2 -> 0
# on a codimension-2 set (an edge of the orbit space).
#
# For a generic interior point, p > 0 and q > 0.
# On an edge (rod), exactly one combination vanishes:
#   - If a != 0 and b != 0: need both p -> 0 AND q -> 0,
#     which is codimension 4 (a corner), not codimension 2.
#   - If a = 0: need q -> 0 (allowed on a rod). Label is (0, ±1).
#   - If b = 0: need p -> 0 (allowed on a rod). Label is (±1, 0).
#
# Conclusion: diagonal h allows ONLY labels ±e1 and ±e2.
# This means exactly two unoriented circle classes.
# The alternating polygon (1,0),(0,1),(-1,0),(0,-1),... IS the full diagonal sector.

diag_check = {
    "claim": "Diagonal fiber metric h=diag(p^2,q^2) allows only rod labels (±1,0) and (0,±1)",
    "proof": (
        "h(v,v) = a^2 p^2 + b^2 q^2. On a rod (codim-2), this must vanish identically. "
        "Since p,q > 0 in the interior, the zero set of h(v,v) for |a|,|b| >= 1 would be "
        "{p=0} ∩ {q=0}, which is codim-4 (vertices). Only a=0 or b=0 gives codim-2 rods."
    ),
    "consequence": (
        "The diagonal sector IS the alternating-label sector. Any Einstein metric "
        "on a simply connected 4-manifold with a diagonal T^2 action must be diagonal "
        "(Liu Prop 5), so this is the complete sector for alternating actions."
    ),
    "non_diagonal_examples": {
        "Page_F1": {
            "labels": "[(1,0),(0,1),(-1,1),(0,-1)]",
            "circle_classes": 3,
            "note": "(-1,1) requires h_{11}-2h_{12}+h_{22} -> 0, impossible diagonally"
        },
        "CLW_dP2": {
            "labels": "5 edges with 3+ circle classes",
            "circle_classes": ">=3",
            "note": "Not in diagonal sector"
        },
        "toric_KE_dP3": {
            "labels": "[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]",
            "circle_classes": 3,
            "note": "Not in diagonal sector"
        }
    },
    "diagonal_examples": {
        "S4": {"m": 2, "topology": "S^4", "has_Einstein": True},
        "S2xS2": {"m": 4, "topology": "S^2 x S^2", "has_Einstein": True,
                   "note": "Product metric is the unique diagonal Einstein (Liu Prop 4 for sec>=0)"},
        "hash_k_S2xS2_k2": {"m": 6, "topology": "#_2(S^2 x S^2)", "has_Einstein": "UNKNOWN"},
        "hash_k_S2xS2_k3": {"m": 8, "topology": "#_3(S^2 x S^2)", "has_Einstein": "UNKNOWN"},
    }
}
results["diagonal_sector"] = diag_check

# ============================================================
# 2. Right-angled polygon side length vs rod length
# ============================================================
# In H^2(kappa) with kappa = -A (Gaussian curvature -A), A > 0:
# Regular right-angled m-gon exists iff m >= 5 (for m=4, flat only).
# 
# Side length formula in H^2(-1):
#   cosh(s/2) = cos(pi/m) / sin(pi/4) = sqrt(2) cos(pi/m)
#   s_m = 2 arccosh(sqrt(2) cos(pi/m))
#
# In H^2(-A): distances scale by 1/sqrt(A), so
#   s_reg(m,A) = s_m / sqrt(A)
#
# Rod length from Einstein equation Ric = Lambda g with Lambda = 1:
#   -Q''/Q = 1 + 2A (= Lambda + 2A in general)
#   Q(s) = sin(omega*s)/omega, omega = sqrt(1+2A)
#   L_rod = pi/omega = pi/sqrt(1+2A)

def s_reg_unit(m):
    """Side length of regular right-angled m-gon in H^2(-1)."""
    if m < 5:
        return None  # Doesn't exist in H^2
    val = math.sqrt(2) * math.cos(math.pi / m)
    if val <= 1:
        return None
    return 2 * math.acosh(val)

def L_rod(A):
    """Rod length for constant edge curvature -A."""
    return math.pi / math.sqrt(1 + 2*A)

polygon_comparison = {}
for m in [4, 5, 6, 8, 10, 12, 20, 50, 100]:
    s = s_reg_unit(m)
    entry = {"m": m, "topology": f"#_{m//2-1}(S^2 x S^2)" if m >= 4 else ""}
    if s is None:
        entry["s_reg_H2(-1)"] = None
        entry["status"] = "No right-angled polygon in H^2 for m=4; flat only"
    else:
        entry["s_reg_H2(-1)"] = s
        # Asymptotic ratio at large A: L_rod ~ pi/sqrt(2A), s_reg ~ s/sqrt(A)
        # ratio = (pi/sqrt(2)) / s
        ratio_large_A = (math.pi / math.sqrt(2)) / s
        entry["L_rod_over_s_reg_large_A"] = ratio_large_A
        entry["gap_percent_large_A"] = (ratio_large_A - 1) * 100
        
        # Find A where L_rod = s_reg(m,A)
        # pi/sqrt(1+2A) = s/sqrt(A)
        # pi^2 * A = s^2 * (1+2A)
        # A(pi^2 - 2s^2) = s^2
        # A_match = s^2 / (pi^2 - 2s^2)
        denom = math.pi**2 - 2 * s**2
        if denom > 0:
            A_match = s**2 / denom
            entry["A_match"] = A_match
            entry["A_match_note"] = "L_rod = s_reg at this A; for A > A_match, L_rod > s_reg"
        else:
            entry["A_match"] = None
            entry["A_match_note"] = "L_rod > s_reg for all A > 0"
    
    # Gauss-Bonnet for the orbit space disk with m right angles
    GB_integral = 2 * math.pi - m * math.pi / 2
    entry["Gauss_Bonnet_int_K_dA"] = GB_integral
    entry["GB_note"] = f"int K_Sigma dA = {GB_integral:.4f} (= 2pi - m*pi/2)"
    
    polygon_comparison[str(m)] = entry

results["polygon_comparison"] = polygon_comparison

# ============================================================
# 2b. Explicit hexagonal comparison
# ============================================================
m6_s = s_reg_unit(6)
m6_data = {
    "m": 6,
    "s_reg_H2(-1)": m6_s,
    "cos_pi_6": math.cos(math.pi/6),
    "sqrt2_cos_pi_6": math.sqrt(2) * math.cos(math.pi/6),
    "arccosh_val": math.acosh(math.sqrt(2) * math.cos(math.pi/6)),
    "L_rod_over_s_reg_large_A": (math.pi / math.sqrt(2)) / m6_s,
    "gap_percent": ((math.pi / math.sqrt(2)) / m6_s - 1) * 100,
    "interpretation": (
        f"For m=6, the constant-curvature right-angled hexagon has side {m6_s:.6f}/sqrt(A), "
        f"while the rod requires pi/sqrt(2A) = {math.pi/math.sqrt(2):.6f}/sqrt(A). "
        f"The rod is {((math.pi/math.sqrt(2))/m6_s - 1)*100:.1f}% longer than the polygon side. "
        "This gap is much larger than the asymptotic 26% at m -> infinity."
    )
}
results["hexagonal_comparison"] = m6_data

# ============================================================
# 3. Eigenvalue constraint
# ============================================================
# The orbit volume phi = ab satisfies -Delta_Sigma phi = 2 Lambda phi
# with Dirichlet BCs (phi = 0 on boundary).
# For Lambda = 1: lambda_1(Sigma) = 2.
#
# For a flat rectangle [0,L]x[0,L]: lambda_1 = 2(pi/L)^2. 
# Setting lambda_1 = 2: L = pi. This is the product metric.
#
# For a right-angled hexagon in H^2(-A):
# The Dirichlet eigenvalue depends on the geometry.
# Faber-Krahn: lambda_1 >= pi j_{0,1}^2 / Area
# where j_{0,1} ≈ 2.4048 is the first zero of J_0.
#
# For m=6 in H^2(-A): Area = pi/A (from Gauss-Bonnet).
# Faber-Krahn gives: lambda_1 >= pi * 5.7832 / (pi/A) = 5.7832 A
# We need lambda_1 = 2, so A <= 2/5.7832 ≈ 0.346.
# But the rod ODE with this small A gives L_rod ≈ pi/sqrt(1.692) ≈ 2.415,
# while s_reg(6, 0.346) ≈ 1.317/sqrt(0.346) ≈ 2.239.
# Gap is still positive (2.415/2.239 ≈ 1.079 = 7.9%).

j01_sq = 2.4048**2  # ≈ 5.7831

eigenvalue_analysis = {}
for m in [4, 6, 8, 10, 20]:
    GB = 2*math.pi - m*math.pi/2
    entry = {"m": m}
    if m == 4:
        # Flat rectangle: lambda_1 = 2 gives L = pi
        entry["flat_rectangle_L"] = math.pi
        entry["flat_lambda_1"] = 2.0
        entry["note"] = "Product metric: L=pi, lambda_1 = 2. Only known diagonal Einstein."
    else:
        # Area from Gauss-Bonnet in H^2(-A): Area = |GB|/A = (m/2-2)*pi/A
        # (since int K dA = -A * Area = GB, so Area = |GB|/A)
        area_coeff = abs(GB)  # Area = area_coeff / A
        
        # Faber-Krahn: lambda_1 >= pi * j01^2 / Area = pi * j01^2 * A / area_coeff
        # Need lambda_1 = 2: A <= 2 * area_coeff / (pi * j01_sq)
        A_FK_upper = 2 * area_coeff / (math.pi * j01_sq)
        
        # At this A, what are the rod and polygon lengths?
        L_at_FK = L_rod(A_FK_upper)
        s_at_FK = s_reg_unit(m) / math.sqrt(A_FK_upper) if s_reg_unit(m) else None
        
        entry["area_formula"] = f"Area = {area_coeff/math.pi:.1f}*pi/A"
        entry["Faber_Krahn_A_upper"] = A_FK_upper
        entry["FK_note"] = f"lambda_1 >= 2 requires A <= {A_FK_upper:.4f} (Faber-Krahn)"
        entry["L_rod_at_FK_A"] = L_at_FK
        if s_at_FK:
            entry["s_reg_at_FK_A"] = s_at_FK
            entry["gap_at_FK_A_percent"] = (L_at_FK / s_at_FK - 1) * 100
        
        # Domain monotonicity: for larger domains, lambda_1 is smaller.
        # A smaller A means larger area, hence easier to achieve lambda_1 = 2.
        # But larger area + fixed eigenvalue constrains the geometry.
        
        # Cheeger constant estimate for the hexagon: h >= 2/diam.
        # Cheeger: lambda_1 >= h^2/4. For H^2(-A): diam ~ s/sqrt(A), so
        # h ~ 2sqrt(A)/s, lambda_1 >= A/s^2.
        if s_reg_unit(m):
            s_unit = s_reg_unit(m)
            cheeger_A_upper = 2 * s_unit**2
            entry["Cheeger_A_upper"] = cheeger_A_upper
            entry["Cheeger_note"] = f"Rough Cheeger: A <= {cheeger_A_upper:.4f}"
    
    eigenvalue_analysis[str(m)] = entry

results["eigenvalue_analysis"] = eigenvalue_analysis

# ============================================================
# 4. The b+ question
# ============================================================
# Known simply connected positive Einstein 4-manifolds:
# S^4: b+ = 0
# CP^2: b+ = 1
# S^2 x S^2: b+ = 1 (form [[0,1],[1,0]], eigenvalues ±1)
# CP^2 # k CPbar, k=1..8: b+ = 1 (Kähler, and Page/CLW/toric KE)
#
# ALL have b+ <= 1. For #_k(S^2 x S^2) with k >= 2: b+ = k >= 2.
#
# If there's a theorem that b+ <= 1 for simply connected positive Einstein 4-manifolds
# with T^2 action, then #_k(S^2 x S^2) for k >= 2 cannot carry such metrics.
# Liu proved this under sec >= 0. Without that hypothesis, it's open.

b_plus_analysis = {
    "known_examples": {
        "S4": {"b+": 0, "b-": 0},
        "CP2": {"b+": 1, "b-": 0},
        "S2xS2": {"b+": 1, "b-": 1},
        "Page_F1": {"b+": 1, "b-": 1},
        "CLW_dP2": {"b+": 1, "b-": 2},
        "toric_KE_dP3": {"b+": 1, "b-": 3},
        "KE_dP4": {"b+": 1, "b-": 4},
        "KE_dP5": {"b+": 1, "b-": 5},
        "KE_dP6": {"b+": 1, "b-": 6},
        "KE_dP7": {"b+": 1, "b-": 7},
        "KE_dP8": {"b+": 1, "b-": 8},
    },
    "stress_family": {
        "hash_k_S2xS2": "b+ = k, b- = k for k >= 1",
        "first_unknown_diagonal": {"k": 2, "m": 6, "b+": 2, "b-": 2}
    },
    "observation": (
        "Every known simply connected positive Einstein 4-manifold has b+ <= 1. "
        "No theorem prohibits b+ >= 2 without additional hypotheses. "
        "Liu proved the classification under sec >= 0. "
        "The diagonal T^2 action on #_k(S^2xS^2) has b+ = k; "
        "if b+ <= 1 is necessary, this immediately excludes k >= 2."
    ),
    "known_non_existence_theorems": {
        "Ricci_flat": "Lambda = 0 on compact => no Killing fields unless parallel, hence flat torus. b+ free.",
        "negative_Einstein": "Lambda < 0 on compact => no Killing fields (Bochner). No T^2 action possible.",
        "positive_Einstein": "Lambda > 0: T^2 action possible. b+ <= 1 for all known examples."
    },
    "question": (
        "Is there a closed simply connected positive Einstein 4-manifold "
        "with an isometric T^2 action having fixed points and b+ >= 2? "
        "The known list S^4, CP^2, S^2xS^2, Page, CLW, dP3 all have b+ <= 1. "
        "This is a topology-uniform question that may be cheaper to decide from sources."
    )
}
results["b_plus_analysis"] = b_plus_analysis

# ============================================================
# 5. Symmetric-sector reduced problem for m=4
# ============================================================
# For the diagonal action on S^2 x S^2 with Z_2 symmetry a(x,y) <-> b(y,x):
# The orbit space [0,L]^2 with g_Sigma.
# 
# Product metric: g_Sigma = dx^2 + dy^2, a = sin(x), b = sin(y), L = pi.
# K_Sigma = 0.
#
# Question: are there non-flat orbit-space metrics giving diagonal Einstein metrics?
#
# From the coupled system:
# -Delta_Sigma a = (1 - K_Sigma) a ... (*)
# -Delta_Sigma b = (1 - K_Sigma) b ... (**)
# K_Sigma g_Sigma - a^{-1} Hess_Sigma(a) - b^{-1} Hess_Sigma(b) = Lambda g_Sigma
#
# With Z_2 symmetry: b(x,y) = a(y,x). Equations (*) and (**) become the same.
# The horizontal Einstein equation becomes:
# K_Sigma(x,y) - a^{-1} Hess(a) - b^{-1} Hess(b) = g_Sigma
#
# In the product case with flat g_Sigma:
# a = sin x, Hess(a) = -sin(x) dx^2 (only xx component)
# b = sin y, Hess(b) = -sin(y) dy^2 (only yy component)
# So: 0 - (-dx^2) - (-dy^2) = dx^2 + dy^2 = g_Sigma. ✓
# 
# For non-flat perturbations: the traceless part of the horizontal equation
# provides an additional constraint beyond the two eigenfunction equations.

m4_symmetric = {
    "framework": (
        "For the diagonal action on S^2 x S^2 with Z_2 symmetry a(x,y) = b(y,x): "
        "the two eigenfunction equations merge into one, but the traceless horizontal "
        "Einstein equation provides an independent constraint. Together with the "
        "Dirichlet eigenvalue condition lambda_1 = 2, this is an overdetermined system."
    ),
    "product_metric_check": {
        "g_Sigma": "flat: dx^2 + dy^2",
        "a": "sin(x)", "b": "sin(y)",
        "K_Sigma": 0,
        "eigenvalue": "lambda_1 = 2 for [0,pi]^2",
        "traceless_check": "(-sin x dx^2) + (-sin y dy^2) = -(dx^2 + dy^2) after dividing by sin",
        "status": "product metric satisfies all equations"
    },
    "uniqueness_question": (
        "Is the product metric the ONLY diagonal T^2-Einstein metric on S^2 x S^2? "
        "Liu Prop 4 proves uniqueness with sec >= 0 (forcing flat orbit space). "
        "Without sec >= 0, the orbit space could be non-flat. "
        "A definitive uniqueness proof would immediately tell us whether the m=6 "
        "extension is blocked or open."
    ),
    "connection_to_liu": (
        "Liu Prop 3: given g_Sigma, at most one Einstein metric exists. "
        "But different g_Sigma could give different Einstein metrics. "
        "The coupled system (eigenfunction + horizontal traceless) must be solved "
        "simultaneously for both g_Sigma and a. This is genuinely overdetermined."
    )
}
results["m4_symmetric_sector"] = m4_symmetric

# ============================================================
# 6. Key structural observation: b+ and the diagonal action
# ============================================================
# For the alternating m-gon with m = 2k+2:
# chi(M) = m (from toric formula: #vertices = #edges = m for a polygon)
# b_2 = chi - 2 = m - 2
# Intersection form: k copies of [[0,1],[1,0]] for #_k(S^2 x S^2)
# b+ = k = m/2 - 1
#
# So m=4 gives b+ = 1 (S^2 x S^2), m=6 gives b+ = 2 (#_2(S^2 x S^2)), etc.
# If b+ >= 2 is impossible for diagonal positive Einstein 4-manifolds,
# then m >= 6 is excluded in one stroke.

b_plus_versus_m = {}
for m in [4, 6, 8, 10, 12]:
    k = m // 2 - 1
    b_plus_versus_m[str(m)] = {
        "k": k,
        "b+": k,
        "b-": k,
        "b2": 2*k,
        "chi": m,
        "known_diagonal_Einstein": m == 2 or m == 4
    }
results["b_plus_versus_m"] = b_plus_versus_m

# ============================================================
# 7. Summary
# ============================================================
results["summary"] = {
    "diagonal_sector_result": (
        "The diagonal twist-free framework covers EXACTLY the alternating-label toric sector: "
        "labels ±e1, ±e2 only. Page, CLW, dP3 are NOT in this sector. "
        "The only known diagonal Einstein 4-manifolds are S^4 (m=2) and S^2xS^2 (m=4)."
    ),
    "polygon_gap": (
        f"For m=6 in constant-curvature H^2(-A): rod is {m6_data['gap_percent']:.1f}% longer "
        "than polygon side (at large A). This gap grows with smaller m: "
        f"m=6: {((math.pi/math.sqrt(2))/s_reg_unit(6) - 1)*100:.1f}%, "
        f"m=8: {((math.pi/math.sqrt(2))/s_reg_unit(8) - 1)*100:.1f}%, "
        f"m→∞: {((math.pi/math.sqrt(2))/s_reg_unit(100) - 1)*100:.1f}%. "
        "Variable K_B could narrow the gap but faces Gauss-Bonnet and eigenvalue constraints."
    ),
    "eigenvalue_constraint": (
        "The orbit volume is the principal Dirichlet eigenfunction with eigenvalue 2. "
        "Faber-Krahn bounds the edge curvature A from above (for constant curvature). "
        "For m=6: A <= ~0.35 from Faber-Krahn, which still leaves a ~8% gap."
    ),
    "b_plus_observation": (
        "All known simply connected positive Einstein 4-manifolds have b+ <= 1. "
        "The diagonal stress family #_k(S^2xS^2) for k >= 2 has b+ >= 2. "
        "If b+ <= 1 is necessary, all m >= 6 diagonal Einstein are excluded. "
        "This is open; Liu proved it only with sec >= 0."
    ),
    "next_steps": [
        "1. Search for a b+ >= 2 non-existence theorem in the positive Einstein literature",
        "2. Set up the linearized stability analysis at the product metric (m=4) to check for non-flat deformations",
        "3. Formulate the m=6 eigenfunction BVP on the hexagonal wedge and check feasibility"
    ]
}

with open(OUT, 'w') as f:
    json.dump(results, f, indent=2)

print(f"Saved to {OUT}")
print()
print("=== DIAGONAL SECTOR ===")
print(f"Only labels ±e1, ±e2: confirmed from h(v,v) = a^2 p^2 + b^2 q^2 argument")
print()
print("=== POLYGON SIDE vs ROD LENGTH (constant K_B, large A) ===")
for m_str, data in polygon_comparison.items():
    m = int(m_str)
    if data.get("L_rod_over_s_reg_large_A"):
        print(f"  m={m:3d}: gap = {data['gap_percent_large_A']:6.1f}%, "
              f"s_reg = {data['s_reg_H2(-1)']:.6f}/√A, "
              f"A_match = {data.get('A_match', 'N/A')}")
    else:
        print(f"  m={m:3d}: flat only (no H^2 polygon)")

print()
print("=== EIGENVALUE CONSTRAINT (Faber-Krahn) ===")
for m_str, data in eigenvalue_analysis.items():
    m = int(m_str)
    if m == 4:
        print(f"  m=4: flat rectangle, L=pi, lambda_1=2. Product metric only.")
    else:
        print(f"  m={m:3d}: Faber-Krahn A <= {data['Faber_Krahn_A_upper']:.4f}, "
              f"L_rod = {data['L_rod_at_FK_A']:.4f}, "
              f"s_reg = {data.get('s_reg_at_FK_A', 'N/A')}")
        if data.get('gap_at_FK_A_percent') is not None:
            print(f"         gap at FK bound: {data['gap_at_FK_A_percent']:.1f}%")

print()
print("=== b+ ANALYSIS ===")
for m_str, data in b_plus_versus_m.items():
    m = int(m_str)
    print(f"  m={m}: k={data['k']}, b+={data['b+']}, "
          f"diagonal Einstein: {'YES' if data['known_diagonal_Einstein'] else 'UNKNOWN'}")
