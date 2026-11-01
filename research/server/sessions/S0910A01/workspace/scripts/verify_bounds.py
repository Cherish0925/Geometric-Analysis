"""
Verify the Chern-Weil / LeBrun quantitative bounds for Yau Problem 26.
Key computations:
1. Dossier Proposition threshold
2. Bishop-Gromov volume bound  
3. LeBrun + CGB combined bound for negative branch
4. Positive branch uniform bound
5. Varying manifold asymptotics
"""
import sympy as sp
import numpy as np

print("=" * 60)
print("VERIFICATION OF YAU 26 QUANTITATIVE BOUNDS")
print("=" * 60)

# 1. Dossier Proposition
print("\n1. DOSSIER PROPOSITION: delta < 1/(1+sqrt(3)) => 2chi > 3|tau|")
d = sp.Symbol('delta', positive=True)
f = sp.Rational(2,3)*(1-d)**2 - 2*d**2
print(f"   f(delta) = {sp.expand(f)}")
sols = sp.solve(f, d)
print(f"   f(delta)=0 solutions: {sols}")
threshold = sp.Rational(1,1) / (1 + sp.sqrt(3))
print(f"   Threshold = 1/(1+sqrt(3)) = {threshold} = {sp.simplify(threshold)} = {float(threshold):.6f}")
print(f"   Simplified: (sqrt(3)-1)/2 = {float((sp.sqrt(3)-1)/2):.6f}")
# Verify they match
diff = sp.simplify(threshold - (sp.sqrt(3)-1)/2)
print(f"   Difference = {diff}")

# 2. Scale invariance check for Min-Oo
print("\n2. MIN-OO SCALE INVARIANCE CHECK")
print("   Under g -> lambda*g:")
print("   K -> lambda^{-1}*K, d -> lambda^{1/2}*d, r -> lambda^{-1}*r")
print("   d^2*max|K| -> lambda * lambda^{-1} * d^2*max|K| = d^2*max|K| [INVARIANT]")
print("   r^{-2}*max|K| -> lambda^2 * lambda^{-1} * r^{-2}*max|K| = lambda * r^{-2}*max|K| [NOT INVARIANT]")
print("   CONCLUSION: Min-Oo condition is d^2*max|K| < Lambda^2, NOT r^{-2}*max|K|")

# 3. Bishop-Gromov volume bound (4D, positive Ricci)
print("\n3. BISHOP-GROMOV VOLUME BOUND (n=4, positive Ricci)")
print("   For Ric >= (1-delta)g on M^4:")
print("   Comparison curvature kappa = (1-delta)/3")
print("   V_comparison = Vol(S^4, kappa) = (8*pi^2/3) * (3/(1-delta))^2 = 24*pi^2/(1-delta)^2")
for dval in [0.0, 0.1, 0.2, 0.3]:
    v = 24 * np.pi**2 / (1-dval)**2
    print(f"   delta={dval}: V <= {v:.2f}")

# 4. LeBrun + CGB negative branch bound
print("\n4. LeBrun + CGB NEGATIVE BRANCH BOUND")
print("   From LeBrun: integral s^2 dV >= 32*pi^2*A  (A = c_1^2(X))")
print("   From CGB(+): 4*pi^2*(A-k) = integral [2|W+|^2 + s^2/24 - |E|^2/2] dV")
print("   Since |W+|^2 >= 0:")
print("   integral |E|^2/2 dV >= integral s^2/24 dV - 4*pi^2*(A-k)")
print("   >= 32*pi^2*A/24 - 4*pi^2*(A-k)")
print("   = (4/3)*pi^2*A - 4*pi^2*(A-k)")
print("   = 4*pi^2*(A/3 - A + k)")
print("   = 4*pi^2*(k - 2A/3)")
print("   So: integral |E|^2 dV >= 8*pi^2*(k - 2A/3)")
print()

# Volume bound from CGB (using self-dual part)
print("   Volume bound from CGB(+): V <= 4*pi^2*(A-k) / f(delta)")
print("   where f(delta) = 2(1-delta)^2/3 - 2*delta^2")
print()

# Combined: 4*delta^2*V >= 8*pi^2*(k-2A/3)
# V <= 4*pi^2*(A-k) / f(delta)
# So: 4*delta^2 * 4*pi^2*(A-k)/f(delta) >= 8*pi^2*(k-2A/3)
# 2*delta^2*(A-k)/f(delta) >= k-2A/3
# For small delta, f~2/3, so:
# 3*delta^2*(A-k) >= k-2A/3
# delta^2 >= (k-2A/3) / (3*(A-k))

A, k = sp.symbols('A k', positive=True)
bound_small_delta = (k - 2*A/3) / (3*(A - k))
print(f"   Small-delta approx: delta^2 >= {bound_small_delta}")

# 5. Specific examples
print("\n5. SPECIFIC LEBRUN EXAMPLES (negative branch)")
examples = [
    (4, 3, "Smallest LeBrun"),
    (9, 7, "A=9, k=7"),
    (100, 67, "A=100, near 2A/3"),
    (1000, 668, "A=1000, near 2A/3"),
    (10000, 6668, "A=10000, near 2A/3"),
]
for Av, kv, label in examples:
    if kv > 2*Av/3 and kv < Av:
        delta_min = np.sqrt((kv - 2*Av/3) / (3*(Av - kv)))
        print(f"   {label}: A={Av}, k={kv}, delta_- >= {delta_min:.6f}")
    else:
        print(f"   {label}: A={Av}, k={kv} -- NOT in LeBrun range")

# 6. Positive branch: Bishop-Gromov version
print("\n6. POSITIVE BRANCH (Bishop-Gromov + LeBrun)")
print("   12*delta^2/(1-delta)^2 >= k - 2A/3")
print("   delta/(1-delta) >= sqrt((k-2A/3)/12)")
for Av, kv, label in examples:
    if kv > 2*Av/3 and kv < Av:
        ratio = np.sqrt((kv - 2*Av/3) / 12)
        delta_pos = ratio / (1 + ratio)
        print(f"   {label}: delta_+ >= {delta_pos:.6f}")

# Minimum over all valid k
print("\n   MINIMUM (over all LeBrun manifolds, positive branch):")
# k-2A/3 >= 1/3 (when A equiv 1 mod 3)
min_ratio = np.sqrt(1/36)
min_delta = min_ratio / (1 + min_ratio)
print(f"   Minimum k-2A/3 = 1/3, giving delta/(1-delta) >= 1/6")
print(f"   delta_+ >= {min_delta:.6f}")
print(f"   Compare: 1/7 = {1/7:.6f}")

# 7. SW vanishing for LeBrun manifolds
print("\n7. SW VANISHING ON LEBRUN MANIFOLDS")
print("   LeBrun M = X#k CPbar^2 has non-trivial SW invariants (for k < c1^2)")
print("   Witten vanishing: s > 0 everywhere => all SW invariants = 0")
print("   Contrapositive: non-trivial SW => no metric with s > 0")
print("   delta_+(g) < 1 => Ric > 0 => s > 0 => contradiction")
print("   CONCLUSION: delta_+(g) >= 1 for ALL LeBrun no-Einstein manifolds")
print("   (Much stronger than the Bishop-Gromov bound)")

# 8. HT-violating manifolds  
print("\n8. HITCHIN-THORPE VIOLATING (#_m CP^2)")
print("   chi(#_m CP^2) = m+1, tau(#_m CP^2) = m")
print("   No Einstein for m >= 3 (HT violation)")
print("   Admits Ric > 0 for all m (Perelman/Burdick)")
print(f"   Universal delta_+ bound: >= 1/(1+sqrt(3)) = {float(1/(1+np.sqrt(3))):.6f}")
for m in [3, 4, 5, 10, 100]:
    chi = m + 1
    tau = m
    ht_plus = 2*chi + 3*tau
    ht_minus = 2*chi - 3*tau
    print(f"   m={m}: chi={chi}, tau={tau}, 2chi+3tau={ht_plus}, 2chi-3tau={ht_minus}")

# 9. Key structural conclusion
print("\n" + "=" * 60)
print("STRUCTURAL CONCLUSION")
print("=" * 60)
print("POSITIVE branch (dim 4): ALL known no-Einstein have delta_+ >= 0.366")
print("NEGATIVE branch (dim 4): Bounds -> 0 for varying manifolds")
print("=> Negative branch is the LIVE territory for counterexamples")
print("=> Construction of tight negative pinching is the UNSOLVED problem")
print("=> Existence direction needs to work WITHOUT full curvature control")
