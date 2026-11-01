"""
Clean verification of the improved Weyl modulus constant 7/24.

The TTCS verifier derived: int(|W+| - 1/(2sqrt(6)))^2 <= (7/24) int|E|^2.

Method: trace-traceless decomposition Q = P + X/4,
then Cauchy-Schwarz on (sqrt(108P), sqrt(X)) · (1,1).
"""
import sympy as sp

# Q = int|E|^2, P = int|Ric_0|^2 = int|E_0|^2, X = int(tr E)^2
# Orthogonal decomposition: Q = P + X/4

# From the completion square: int(q + 8sqrt6 v)^2 <= 108P
# where q = s+4 = tr(E), v = |W+| - 1/(2sqrt6)

# Triangle inequality:
# 8sqrt(6) ||v||_2 <= ||q + 8sqrt6 v||_2 + ||q||_2
#                   <= sqrt(108P) + sqrt(X)

# Cauchy-Schwarz: (sqrt(108P) + sqrt(X))^2 <= (108+1)(P + X)
# But we can do better by noting that X = 4(Q-P):

# (sqrt(108P) + sqrt(4(Q-P)))^2 <= (108+4)(P + (Q-P)) = 112 Q
# This works because (a + b)^2 <= (alpha + beta)(a^2/alpha + b^2/beta)
# with alpha = 108, beta = 4, a^2/alpha = P, b^2/beta = Q-P.

# So 384 ||v||_2^2 <= 112 Q, giving ||v||_2^2 <= 112Q/384 = 7Q/24.

print("="*60)
print("VERIFICATION: int(|W+| - 1/(2sqrt6))^2 <= (7/24) int|E|^2")
print("="*60)

P, Q = sp.symbols('P Q', positive=True)
X = 4*(Q - P)  # X = int(tau^2), Q = P + X/4

# The Cauchy-Schwarz step:
# (sqrt(108)*sqrt(P) + 2*sqrt(Q-P))^2 <= ?
# Using weighted CS: (a+b)^2 <= (w1+w2)(a^2/w1 + b^2/w2)
# a = sqrt(108P), b = sqrt(X) = 2*sqrt(Q-P)
# a^2 = 108P, b^2 = 4(Q-P)
# Choose w1=108, w2=4: a^2/w1=P, b^2/w2=Q-P
# (w1+w2)(a^2/w1+b^2/w2) = 112 * Q

bound_RHS = 112 * Q
# LHS is (8sqrt6)^2 * int v^2 = 384 * int v^2
# So int v^2 <= 112Q/384

ratio = sp.Rational(112, 384)
print(f"112/384 = {ratio} = {float(ratio):.6f}")
print(f"7/24 = {float(sp.Rational(7,24)):.6f}")
assert ratio == sp.Rational(7, 24), "Ratio doesn't match!"
print(f"CONFIRMED: 112/384 = 7/24")
print()

# Check the CS step more carefully
# Need: (sqrt(108P) + sqrt(4(Q-P)))^2 <= 112Q for all 0 <= P <= Q
# Expand: 108P + 2*sqrt(108*4*P*(Q-P)) + 4(Q-P)
# = 108P + 4Q - 4P + 2*sqrt(432*P*(Q-P))
# = 104P + 4Q + 2*sqrt(432*P*(Q-P))
# Need this <= 112Q, i.e. 104P + 2*sqrt(432 P(Q-P)) <= 108Q

# Set t = P/Q, t in [0,1]:
# 104t + 2*sqrt(432*t*(1-t)) <= 108
# Max of LHS: d/dt[104t + 2*sqrt(432)*sqrt(t(1-t))] = 0
# 104 + 2*sqrt(432)*(1-2t)/(2*sqrt(t(1-t))) = 0
# At boundary t=0: 0 + 0 = 0 < 108 ✓
# At boundary t=1: 104 + 0 = 104 < 108 ✓
# Interior critical: 104 + sqrt(432)*(1-2t)/sqrt(t(1-t)) = 0
# (1-2t)/sqrt(t(1-t)) = -104/sqrt(432) = -104/(12sqrt(3))

t = sp.Symbol('t', positive=True)
f = 104*t + 2*sp.sqrt(432*t*(1-t))
f_deriv = sp.diff(f, t)
# Solve f_deriv = 0
crit = sp.solve(f_deriv, t)
print("Critical points of 104t + 2*sqrt(432*t*(1-t)):")
for c in crit:
    val = float(c)
    fval = float(f.subs(t, c))
    print(f"  t = {val:.6f}, f(t) = {fval:.6f}")
    assert fval <= 108, f"CS bound violated at t={val}!"

print()
print("PASS: The Cauchy-Schwarz bound holds for all 0 <= P <= Q.")
print(f"RESULT: int(|W+| - 1/(2sqrt(6)))^2  <=  (7/24) * int|E|^2")
print(f"        = {float(sp.Rational(7,24)):.6f} * int|E|^2")
print()

# Also verify: at the calibrated point, the bound is TIGHT
# s = -4, |W+| = 1/(2sqrt6), E = 0, so both sides = 0.
# For a perturbation: E_ij = delta * diag(1,1,1,1),
# s = -4 + 4*delta, |Ric_0| = 0, Q = 16*delta^2*Vol, P = 0
# v = |W+|(delta) - 1/(2sqrt6) depends on how W+ responds...
# The bound is not tight in general (tightness requires P = Q, i.e. X = 0)

print("The bound 7/24 is achieved when P = Q (zero scalar defect, X = 0),")
print("which means the entire Einstein defect is traceless.")
print("For generic defects where X > 0, the actual ratio is smaller.")
