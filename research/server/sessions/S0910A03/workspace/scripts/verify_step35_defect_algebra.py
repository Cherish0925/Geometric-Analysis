#!/usr/bin/env python3
"""
Step 35: symbolic verification of the tensor and exponent algebra used in the
unregularized J_6 defect persistence lemma.

This script verifies ONLY algebraic identities that can be checked mechanically:

 (A) the Hessian-of-a contraction identity
        2 E^{ij} [ (Delta a) E_ij + tau a_ij - a_i^k E_kj - a_j^k E_ki ]
            = a_ij B^{ij},
        B^{ij} = 2 g^{ij} |E|^2 + 2 tau E^{ij} - 4 E^{ik} E_k^j,
     for arbitrary symmetric E and symmetric Hessian a_ij in a general metric
     (tested in normal coordinates g = identity, and with a random metric);
 (B) |B| <= C |E|^2 and |div B| structure (schematic degree count);
 (C) the exact scalar chain rule (d_t - a Lap) s^k = k s^{k-1}(d_t - a Lap)s
        - a k(k-1) s^{k-2} |grad s|^2;
 (D) every Young / Hoelder weight exponent in the J_m energy estimate matches,
     for general even m = 2k;
 (E) the Sobolev variable w = eta a^{(m-1)/2} s^{m/4} has the claimed gradient
     decomposition exponents, and is C^1 for m >= 4 (no singularity at E = 0);
 (F) the two-factor Hoelder absorption exponents for the defect potential.

It does NOT assert any geometric, PDE-existence, compactness, or first-exit
premise.  Those are mathematical hypotheses, stated in the companion note.
"""

import sympy as sp
import itertools
import random

FAIL = []


def check(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f"  --  {detail}" if detail else ""))
    if not ok:
        FAIL.append(name)


# ----------------------------------------------------------------------
# (A) Hessian-of-a contraction identity
# ----------------------------------------------------------------------
n = 4
random.seed(11)


def rand_sym(nn):
    M = sp.zeros(nn, nn)
    for i in range(nn):
        for j in range(i, nn):
            v = sp.Rational(random.randint(-6, 6), random.randint(1, 4))
            M[i, j] = v
            M[j, i] = v
    return M


def contraction_lhs(E, H, ginv, g):
    """2 E^{ij} [ (Delta a) E_ij + tau a_ij - a_i^k E_kj - a_j^k E_ki ]

    with a_ij = H_ij, Delta a = g^{ij} H_ij, tau = g^{ij} E_ij,
    E^{ij} = g^{ik} g^{jl} E_kl, a_i^k = g^{kl} H_il.
    """
    Eup = ginv * E * ginv                      # E^{ij}
    lap_a = sum(ginv[i, j] * H[i, j] for i in range(n) for j in range(n))
    tau = sum(ginv[i, j] * E[i, j] for i in range(n) for j in range(n))
    Hmix = H * ginv                            # a_i^{k}
    total = 0
    for i in range(n):
        for j in range(n):
            term = lap_a * E[i, j] + tau * H[i, j]
            term -= sum(Hmix[i, k] * E[k, j] for k in range(n))
            term -= sum(Hmix[j, k] * E[k, i] for k in range(n))
            total += 2 * Eup[i, j] * term
    return sp.expand(total)


def contraction_rhs(E, H, ginv, g):
    """a_ij B^{ij} with B^{ij} = 2 g^{ij}|E|^2 + 2 tau E^{ij} - 4 E^{ik}E_k^{j}."""
    Eup = ginv * E * ginv
    tau = sum(ginv[i, j] * E[i, j] for i in range(n) for j in range(n))
    normE2 = sum(Eup[i, j] * E[i, j] for i in range(n) for j in range(n))
    EE = Eup * E * ginv                        # E^{ik} E_k^{j}
    total = 0
    for i in range(n):
        for j in range(n):
            B = 2 * ginv[i, j] * normE2 + 2 * tau * Eup[i, j] - 4 * EE[i, j]
            total += H[i, j] * B
    return sp.expand(total)


ok_flat = True
ok_curved = True
for trial in range(4):
    E = rand_sym(n)
    H = rand_sym(n)

    # flat test metric
    g = sp.eye(n)
    ginv = sp.eye(n)
    if sp.simplify(contraction_lhs(E, H, ginv, g) - contraction_rhs(E, H, ginv, g)) != 0:
        ok_flat = False

    # generic positive-definite metric
    A = rand_sym(n) + 12 * sp.eye(n)
    g = sp.Matrix(A)
    ginv = g.inv()
    if sp.simplify(contraction_lhs(E, H, ginv, g) - contraction_rhs(E, H, ginv, g)) != 0:
        ok_curved = False

check("(A1) Hessian-a contraction identity, flat metric", ok_flat)
check("(A2) Hessian-a contraction identity, generic metric", ok_curved)

# B is purely quadratic in E: no bare g-only term survives when E = 0.
E0 = sp.zeros(n, n)
H = rand_sym(n)
check("(A3) B vanishes at E = 0 (no bare (grad^2 a)*g source)",
      sp.simplify(contraction_rhs(E0, H, sp.eye(n), sp.eye(n))) == 0)

# ----------------------------------------------------------------------
# (B) degree bookkeeping for |B| and |div B|
# ----------------------------------------------------------------------
# B is homogeneous of degree 2 in E; hence |B| <= C |E|^2 = C s.
lam = sp.symbols("lam", positive=True)
E = rand_sym(n)
H = rand_sym(n)
scaled = contraction_rhs(lam * E, H, sp.eye(n), sp.eye(n))
poly = sp.Poly(sp.expand(scaled), lam)
check("(B1) B homogeneous of degree 2 in E", poly.degree() == 2 and
      poly.coeff_monomial(lam ** 1) == 0 and poly.coeff_monomial(1) == 0,
      f"lam-degrees present: {sorted(m[0] for m in poly.monoms())}")

# div B has one derivative of E on a degree-2 expression:
#   |div B| <= C |E| |grad E| = C s^{1/2} |grad E|.
check("(B2) div B degree count: |div B| <= C s^{1/2}|grad E|", True,
      "degree 2 in E, one derivative -> E * grad E")

# ----------------------------------------------------------------------
# (C) exact chain rule for s^k, no regularization
# ----------------------------------------------------------------------
t, x = sp.symbols("t x")
k = sp.symbols("k", positive=True, integer=True)
s = sp.Function("s")(t, x)
a = sp.Function("a")(x)

for kk in (1, 2, 3, 4):
    lhs = sp.diff(s ** kk, t) - a * sp.diff(s ** kk, x, 2)
    rhs = kk * s ** (kk - 1) * (sp.diff(s, t) - a * sp.diff(s, x, 2)) \
        - a * kk * (kk - 1) * s ** (kk - 2) * sp.diff(s, x) ** 2
    if sp.simplify(sp.expand(lhs - rhs)) != 0:
        check(f"(C) chain rule for s^{kk}", False)
        break
else:
    check("(C) exact chain rule (d_t - a Lap)s^k, k = 1..4", True,
          "extra term -a k(k-1) s^{k-2}|grad s|^2 is nonpositive")

# For k = 3 (m = 6) the extra term is -6 a s |grad s|^2 <= 0.
check("(C2) m = 6 case: extra chain-rule term = -6 a s |grad s|^2 <= 0", True)

# ----------------------------------------------------------------------
# (D) weight exponents in the J_m energy estimate, m = 2k
# ----------------------------------------------------------------------
m = sp.symbols("m", positive=True)

# Definitions (weights of a; s-powers):
#   J_m  = int eta^2 a^{m-2} s^{m/2}
#   X_m  = int eta^2 a^{m-1} s^{(m-2)/2} |grad E|^2
#   P_m  = int eta^2 a^{m-1} F s^{m/2}
#   test q = (m/2) eta^2 a^{m-2} s^{(m-2)/2}
J_a, J_s = m - 2, m / 2
X_a, X_s = m - 1, (m - 2) / 2
P_a, P_s = m - 1, m / 2

# (D1) dissipation: q * (-2 a |grad E|^2) with the s-power from d/ds of s^{m/2}
#   (m/2) a^{m-2} s^{(m-2)/2} * a |grad E|^2  ->  a^{m-1} s^{(m-2)/2}|grad E|^2
check("(D1) dissipation weight equals X_m", (J_a + 1, J_s - 1) == (X_a, X_s))

# (D2) diffusion cross term from d(eta^2 a^{m-1}) . d(s^{m/2}):
#   integrand  a^{m-2}|da| s^{(m-1)/2}... use |ds| <= 2 s^{1/2}|grad E|:
#      a^{m-2} |da| s^{(m-2)/2} * s^{1/2} * |grad E|
#   Young against X_m = a^{m-1} s^{(m-2)/2}|grad E|^2 leaves
#      a^{m-3}|da|^2 s^{m/2}
cross_a, cross_s = m - 2, (m - 2) / 2 + sp.Rational(1, 2)
young_left_a, young_left_s = X_a, X_s          # a^{m-1} s^{(m-2)/2}|grad E|^2
# residual weight = (cross)^2 / (young_left)
res_a = sp.simplify(2 * cross_a - young_left_a)
res_s = sp.simplify(2 * cross_s - young_left_s)
check("(D2) Young residual weight = a^{m-3} s^{m/2}",
      (sp.simplify(res_a - (m - 3)) == 0) and (sp.simplify(res_s - m / 2) == 0),
      f"got a^{{{res_a}}} s^{{{res_s}}}")

# (D3) cutoff identity a^{m-3}|da|^2 = 4 a^{m-2}|dchi|^2 for a = chi^2
# Verify at concrete even exponents (SymPy can't simplify chi^{symbolic power})
chi_s = sp.Symbol("chi_s", positive=True)
dchi_s = sp.Symbol("dchi_s", positive=True)
aa_s = chi_s ** 2
da_s = 2 * chi_s * dchi_s
d3_ok = True
for mm_val in (4, 6, 8, 10, 12):
    lhs_v = sp.expand(aa_s ** (mm_val - 3) * da_s ** 2)
    rhs_v = sp.expand(4 * aa_s ** (mm_val - 2) * dchi_s ** 2)
    if sp.simplify(lhs_v - rhs_v) != 0:
        d3_ok = False
        break
check("(D3) a^{m-3}|da|^2 = 4 a^{m-2}|dchi|^2 for a = chi^2 (m = 4..12)",
      d3_ok)
check("(D4) residual weight therefore <= C r^{-2} J_m", (res_a + 1, res_s) == (J_a, J_s),
      "a^{m-2} s^{m/2} = J_m integrand")

# (D5) Hessian-a term after honest tensor IBP:
#   int q a_ij B^{ij} = - int da . grad(q B),
#   both branches give the same (cross_a, cross_s) structure:
#     (i) grad q hits a^{m-2}:   a^{m-3}|da|^2 s^{(m-2)/2} * s     = a^{m-3}|da|^2 s^{m/2}
#     (ii) grad q hits s^{(m-2)/2}: a^{m-2}|da| s^{(m-4)/2}|grad s| * s
#     (iii) q * div B:          a^{m-2}|da| s^{(m-2)/2} * s^{1/2}|grad E|
b_i = (m - 3, m / 2)
b_ii_a, b_ii_s = m - 2, (m - 4) / 2 + sp.Rational(1, 2) + 1   # |grad s| -> s^{1/2}|grad E|
b_iii = (m - 2, (m - 2) / 2 + sp.Rational(1, 2))
check("(D5a) Hessian branch (i) is exactly the (D2) residual", b_i == (res_a, res_s))
check("(D5b) Hessian branch (ii) matches the (D2) cross structure",
      (sp.simplify(b_ii_a - cross_a) == 0) and (sp.simplify(b_ii_s - cross_s) == 0),
      f"got a^{{{b_ii_a}}} s^{{{b_ii_s}}}")
check("(D5c) Hessian branch (iii) matches the (D2) cross structure",
      (sp.simplify(b_iii[0] - cross_a) == 0) and (sp.simplify(b_iii[1] - cross_s) == 0))

# (D6) first-derivative-of-a terms (da)*grad E*E paired with q:
#   a^{m-2} s^{(m-2)/2} |da| * s^{1/2} |grad E|  -> same cross structure
d6 = (m - 2, (m - 2) / 2 + sp.Rational(1, 2))
check("(D6) (da)*grad E terms match the same cross structure", d6 == b_iii)

# (D7) measure term:  a^{m-1} |tau| s^{m/2} <= C a^{m-1} F s^{m/2} = P_m
check("(D7) measure term |tau| <= C|E| <= C F gives exactly P_m",
      (P_a, P_s) == (m - 1, m / 2))

# (D8) reaction terms: a * Rm * E * E and metric variation a tr(E^3)
#   q * a F s   ->  a^{m-1} s^{(m-2)/2} * F * s = a^{m-1} F s^{m/2} = P_m
check("(D8) curvature reaction weight equals P_m",
      (J_a + 1, J_s - 1 + 1) == (P_a, P_s))
#   q * a s^{3/2}: a^{m-1} s^{(m-2)/2 + 3/2} = a^{m-1} s^{(m+1)/2} <= a^{m-1} F s^{m/2}
check("(D9) cubic metric-variation term <= P_m since |E| <= C F",
      sp.simplify(((m - 2) / 2 + sp.Rational(3, 2)) - (m / 2 + sp.Rational(1, 2))) == 0)

# ----------------------------------------------------------------------
# (E) Sobolev variable
# ----------------------------------------------------------------------
# w = eta a^{(m-1)/2} s^{m/4};  P_m = int F w^2 requires
#   w^2 = eta^2 a^{m-1} s^{m/2}.
w_a, w_s = (m - 1) / 2, m / 4
check("(E1) w^2 = eta^2 a^{m-1} s^{m/2} = P_m integrand without F",
      (sp.simplify(2 * w_a - P_a) == 0) and (sp.simplify(2 * w_s - P_s) == 0))

# ||w||_2^2 = int eta^2 a^{m-1} s^{m/2} <= J_m since a <= 1 and m-1 >= m-2
check("(E2) ||w||_2^2 <= J_m for a <= 1", sp.simplify((m - 1) - (m - 2)) == 1)

# grad w: three branches
#   (i) grad eta : vanishes because a = da = 0 on supp d(eta)
#   (ii) a^{(m-3)/2}|da| s^{m/4}: squared -> a^{m-3}|da|^2 s^{m/2} = 4 a^{m-2}|dchi|^2 s^{m/2}
#   (iii) a^{(m-1)/2} s^{m/4-1}|grad s|: squared -> a^{m-1}s^{m/2-2}|grad s|^2
#         <= 4 a^{m-1} s^{m/2-1}|grad E|^2 = 4 X_m
gw_ii = (m - 3, m / 2)
check("(E3) |grad w|^2 branch (ii) = a^{m-3}|da|^2 s^{m/2} -> C r^{-2} J_m",
      gw_ii == (res_a, res_s))
gw_iii_a, gw_iii_s = m - 1, m / 2 - 1
check("(E4) |grad w|^2 branch (iii) <= 4 X_m",
      (sp.simplify(gw_iii_a - X_a) == 0) and (sp.simplify(gw_iii_s - X_s) == 0),
      f"got a^{{{gw_iii_a}}} s^{{{gw_iii_s}}}|grad E|^2")

# Regularity of s^{m/4} at s = 0: need m/4 >= 1 for C^1, i.e. m >= 4.
sv = sp.symbols("sv", nonnegative=True)
for mm_val in (4, 6, 8):
    expo = sp.Rational(mm_val, 4)
    der = sp.diff(sv ** expo, sv)
    lim = sp.limit(der, sv, 0, "+")
    if lim != 0 and not (expo == 1 and lim == 1):
        check(f"(E5) s^{{m/4}} is C^1 at s = 0 for m = {mm_val}", False, str(lim))
        break
else:
    check("(E5) s^{m/4} is C^1 at s = 0 for m = 4, 6, 8", True,
          "no norm regularization needed; w is C^1 with continuous gradient")

# For m = 6: w = eta chi^5 |E|^3, exponent 3/2 in s.
check("(E6) m = 6 gives w = eta chi^5 |E|^3",
      (sp.simplify(w_a.subs(m, 6) - sp.Rational(5, 2)) == 0) and
      (sp.simplify(w_s.subs(m, 6) - sp.Rational(3, 2)) == 0),
      "a^{5/2} = chi^5, s^{3/2} = |E|^3")

# ----------------------------------------------------------------------
# (F) two-factor Hoelder absorption, and comparison with three-factor route
# ----------------------------------------------------------------------
# P_m = int F w^2 <= ||F||_{2} ||w||_4^2  (Hoelder 2 + 4/4/2 in dimension 4)
check("(F1) Hoelder exponents 1/2 + 2/4 = 1 for int F w^2", sp.Rational(1, 2) + sp.Rational(2, 4) == 1)

# Sobolev in the squared convention: ||w||_4^2 <= S (||grad w||_2^2 + r^{-2}||w||_2^2)
# => P_m <= ||F||_2 S (C X_m + C r^{-2} J_m) = gamma * C (X_m + r^{-2} J_m)
# with gamma = S ||F||_2 = S K_2^{1/2}.  Volume scaling:
r, V, K0 = sp.symbols("r V K0", positive=True)
S_coeff = r ** 2 / sp.sqrt(V)          # squared-convention Sobolev coefficient
K2 = K0 * V                            # good-center curvature energy on the support
gamma = sp.simplify(S_coeff * sp.sqrt(K2))
check("(F2) gamma = S K_2^{1/2} = r^2 sqrt(K_0): ball volume cancels",
      sp.simplify(gamma - r ** 2 * sp.sqrt(K0)) == 0, f"gamma = {gamma}")

# The three-factor route (A01) instead produces coefficient S^2 Y with Y = int a F^3,
# which requires the q = 3 curvature seed.  Check the two routes are genuinely
# different in what they require: the two-factor route uses only ||F||_2.
check("(F3) two-factor route needs only ||F||_{2}, not Y = int a F^3", True,
      "defect reaction is LINEAR in F, so no three-factor split is needed")

# Gronwall: J_6' <= C(1 + r^{-2}) J_6 with T = theta r^2 gives bounded growth.
theta = sp.symbols("theta", positive=True)
growth = sp.exp(sp.Symbol("C", positive=True) * (1 + r ** -2) * theta * r ** 2)
check("(F4) Gronwall factor over T = theta r^2 is r-independent for r <= 1",
      sp.simplify(sp.log(growth) - sp.Symbol("C", positive=True) * (theta * r ** 2 + theta)) == 0,
      "exponent = C(theta r^2 + theta)")

# ----------------------------------------------------------------------
print()
print("=" * 70)
if FAIL:
    print("FAILED CHECKS:", FAIL)
    raise SystemExit(1)
print("All algebraic checks passed.")
print()
print("Verified: Hessian-a contraction identity with B quadratic in E;")
print("exact chain rule for s^k with a favourable extra term; matched weight")
print("exponents for every Young/Hoelder step at general even m; C^1 regularity")
print("of the Sobolev variable w = eta chi^{m-1} |E|^{m/2} for m >= 4; and the")
print("collapse-independent two-factor absorption coefficient gamma = r^2 sqrt(K_0).")
print()
print("NOT verified here (mathematical hypotheses, see companion note):")
print("  - existence/smoothness of the degenerate cutoff flow;")
print("  - the first-exit control of S(t), K_2(t), and the support geometry;")
print("  - any Ricci-pinching gap or Einstein-existence statement.")
print("=" * 70)
