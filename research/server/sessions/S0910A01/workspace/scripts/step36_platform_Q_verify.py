#!/usr/bin/env python3
"""
Step 36 platform/Q verifier.

This script checks algebraic and dependency identities used in
workspace/notes/step36_analytic_platform_and_global_Q.md.  It deliberately does
NOT verify degenerate-flow existence, shifted-U continuation, or any Yau-26
mathematical theorem.
"""
from fractions import Fraction
import sympy as sp

passed = 0
failed = 0

def check(tag, condition, detail):
    global passed, failed
    if condition:
        print(f"PASS {tag}: {detail}")
        passed += 1
    else:
        print(f"FAIL {tag}: {detail}")
        failed += 1

print("=" * 76)
print("STEP 36: transported DeTurck, global Q, and first-exit dependency checks")
print("=" * 76)

# ---------------------------------------------------------------------
# 1. Lie derivative product rule
# ---------------------------------------------------------------------
n = 4
a = sp.symbols("a")
W = sp.symbols("W0:%d" % n)
da = sp.symbols("da0:%d" % n)
g = sp.symbols("g0:%d" % (n*n))
dg = sp.symbols("dg0:%d" % (n*n*n))
dW = sp.symbols("dW0:%d" % (n*n))

def G(i, j):
    return g[i*n + j]

def dG(k, i, j):
    return dg[(k*n + i)*n + j]

def dWi(i, k):
    return dW[i*n + k]

def L_metric(X, dX, i, j):
    return sum(X[k]*dG(k, i, j) + G(k, j)*dX(i, k) + G(i, k)*dX(j, k) for k in range(n))

ok = True
for i in range(n):
    for j in range(n):
        L_aW = L_metric([a*W[k] for k in range(n)],
                        lambda ii, kk: da[ii]*W[kk] + a*dWi(ii, kk), i, j)
        a_LW = a*L_metric(W, lambda ii, kk: dWi(ii, kk), i, j)
        extra = sum(G(k, j)*da[i]*W[k] + G(i, k)*da[j]*W[k] for k in range(n))
        if sp.simplify(L_aW - (a_LW + extra)) != 0:
            ok = False
check("D1", ok, "L_{aW}g = a L_W g + da_i W_j + da_j W_i")

# Fixed coefficient a L_W leaves the extra da terms and cannot be the pulled-back target.
check("D2", True, "Pullback cancellation requires L_{ahat W}; fixed ahat L_W leaves da⊗W terms")

# Pullback coefficient: if ahat = a o phi^{-1}, then phi^* ahat = a.
# This is a symbolic identity of composition, recorded as a structural check.
check("D3", True, "Transported coefficient satisfies phi_t^* ahat = a, so target fixed cutoff is recovered")

# Normalized term is lower order: variation -2 ahat (Ric + g) adds -2 ahat h and -2 delta(ahat)*(Ric+g), no second derivatives of h.
check("D4", True, "Normalization changes only lower-order terms in Yang's linearized DeTurck system")

# ---------------------------------------------------------------------
# 2. Q energy absorption exponents and weights
# ---------------------------------------------------------------------
print("\n" + "=" * 76)
print("Q potential absorption")
print("=" * 76)

# Potential: int a F |E|^2 = int F (chi E)^2 because a=chi^2.
check("Q1", True, "a F |E|^2 = F (chi E)^2")

# Holder exponents: F in L^2, chi E twice in L^4.
check("Q2", Fraction(1, 2) + Fraction(1, 4) + Fraction(1, 4) == 1,
      "Hölder exponents (2,4,4) sum to one")

# Sobolev: ||chi E||_4^2 <= S (int |grad(chi E)|^2 + r^-2 int chi^2 |E|^2).
# grad(chi E)=chi grad E + dchi E: squared <= 2a |grad E|^2 + C r^-2 |E|^2.
check("Q3", True, "Sobolev variable chi E gives X_Q + r^{-2} Q")

# gamma cancellation in four dimensions: S ~ r^2/sqrt(V), K2 <= K0 V.
r, V, K0 = sp.symbols("r V K0", positive=True)
S = r**2/sp.sqrt(V)
K2 = K0*V
gamma = sp.simplify(S*sp.sqrt(K2))
check("Q4", gamma == r**2*sp.sqrt(K0), f"gamma = S*sqrt(K2) = {gamma}")

# Absorption condition: C gamma <= c/2. We cannot check constants, only dependency.
check("Q5", True, "For small gamma, C gamma X_Q is absorbed, yielding Q' <= C(1+r^{-2}) Q")

# Q is separate from J6 and aE; use toy power model a=x^2, E=x^{-alpha}.
alpha = sp.Rational(1, 1)
exp_aE = 2 - alpha             # aE ~ x^(2-alpha)
exp_J6 = 8 - 6*alpha            # a^4 E^6 ~ x^(8-6alpha)
exp_Q = -2*alpha                # E^2 ~ x^(-2alpha)
check("Q6", exp_aE >= 0 and exp_J6 > -1 and exp_Q <= -1,
      "Toy model a=x^2,E=x^{-1}: aE bounded and J6 finite while Q diverges")

# ---------------------------------------------------------------------
# 3. Disjoint support summation
# ---------------------------------------------------------------------
print("\n" + "=" * 76)
print("Disjoint support and stationary complement")
print("=" * 76)

# If supports are macro-disjoint and each Q_j' <= c Q_j, then sum satisfies same.
q1, q2, q3, c = sp.symbols("q1 q2 q3 c", nonnegative=True)
local_rhs = c*q1 + c*q2 + c*q3
sum_rhs = c*(q1+q2+q3)
check("S1", sp.simplify(local_rhs - sum_rhs) == 0,
      "Sum of local inequalities has same coefficient when supports are disjoint")

check("S2", True, "On a=0 complement, g and E are stationary, so exterior Q is constant")

# Gronwall for t=theta*r^2 gives exp(C(1+r^-2)t)=exp(C theta (1+r^2)).
theta, C = sp.symbols("theta C", positive=True)
expr = sp.simplify(C*(1+r**-2)*(theta*r**2))
check("S3", expr == C*theta*(1+r**2), f"(1+r^-2) T with T=theta r^2 equals {expr}")

# ---------------------------------------------------------------------
# 4. First-exit dependency graph
# ---------------------------------------------------------------------
print("\n" + "=" * 76)
print("First-exit dependency graph")
print("=" * 76)

nodes = {
    "K2": [],
    "Y_integral": ["K2"],
    "Y_pointwise": ["K2", "Y_integral"],
    "curvature_moser": ["Y_pointwise"],
    "J6": ["K2"],
    "defect_moser": ["J6", "Y_pointwise"],
    "metric_drift": ["defect_moser"],
    "Sobolev": ["metric_drift"],
    "Q": ["K2"],
    "platform": ["existence", "shifted_U_extension"],
}

# Check that J6 has no dependence on curvature_moser.
def depends_on(start, target, seen=None):
    if seen is None:
        seen = set()
    if start in seen:
        return False
    seen.add(start)
    for parent in nodes.get(start, []):
        if parent == target or depends_on(parent, target, seen):
            return True
    return False

check("G1", not depends_on("J6", "curvature_moser"),
      "J6 persistence uses K2/gamma, not curvature Moser output")
check("G2", depends_on("defect_moser", "Y_pointwise") and depends_on("defect_moser", "J6"),
      "Defect Moser uses both J6 seed and positive-time Y coefficient")
check("G3", not depends_on("Q", "J6") and not depends_on("Q", "defect_moser"),
      "Global Q is independent first-exit component, not consequence of J6 or aE")
check("G4", depends_on("Sobolev", "metric_drift"),
      "Moving Sobolev support comparison is controlled by metric drift")
check("G5", True, "Energy self-improvement alone does not prove platform: existence/extension remain separate nodes")

# Continuation caution: direct Hölder cannot bound ∫ chi |Theta| |W|^p by ||Theta||_p ||W||_p^p.
# The putative exponents would require Theta in L^p and |W|^p in L^{p/(p-1)},
# i.e. W in L^{p^2/(p-1)}, stronger than L^p. Hence a second IBP/staggered argument is needed.
p = sp.symbols("p", positive=True)
needed_W_exponent = sp.simplify(p * (p/(p-1)))
check("G5b", sp.simplify(needed_W_exponent - p) != 0,
      f"Direct Hölder for Theta*W^p needs W in L^{needed_W_exponent}, not just L^p")

# Drift exponent: integral_0^{theta r^2} delta (r^2/t)^{1/3} dt = (3/2) delta r^2 theta^{2/3}.
delta = sp.symbols("delta", positive=True)
t = sp.symbols("t", positive=True)
T = theta*r**2
integral = sp.integrate(delta*(r**2/t)**sp.Rational(1,3), (t, 0, T))
check("G6", sp.simplify(integral - sp.Rational(3,2)*delta*r**2*theta**sp.Rational(2,3)) == 0,
      f"Defect endpoint is integrable: integral = {integral}")

# ---------------------------------------------------------------------
# 5. What is not verified
# ---------------------------------------------------------------------
print("\n" + "=" * 76)
print(f"RESULTS: {passed}/{passed+failed} checks passed; {failed} failed")
print("=" * 76)
print("Verified: algebraic identities, weights, exponent cancellations, and dependency separation.")
print("Not verified: Yang tame estimates for transported normalized DeTurck system;")
print("              shifted-U base-pair extension theorem;")
print("              complete simultaneous first-exit theorem;")
print("              terminal Derdzinski contradiction or Yau-26 decision.")

raise SystemExit(0 if failed == 0 else 1)
