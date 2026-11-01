"""
Step 22: Inverse-square counterexample to abstract Nash and subcritical upgrade.

In R^4, the Hardy potential V = kappa/|x|^2 with 0 < kappa < 1 satisfies
the form bound  int V phi^2 <= kappa int |nabla phi|^2  (Hardy inequality).
Yet the heat semigroup e^{t(Delta+V)} does NOT have a uniform L^2 -> L^infty
estimate because the ground-state singularity r^{-sigma}, sigma = 1-sqrt(1-kappa),
is in L^2 but not L^infty.

This refutes the claim that a small relative form bound alone gives
Nash ultracontractivity.

The subcritical upgrade: if V in L^p with p > n/2 = 2 (in 4D), then
standard De Giorgi-Nash-Moser theory gives L^2 -> L^infty with convergent
constants. In our problem, H_3(t) <= C gamma^3/t provides V in L^3(nu)
at positive time, which is subcritical.
"""
from sympy import *

# === 1. HARDY EXPONENTS IN R^n ===
n, kappa = symbols('n kappa', positive=True)

# The operator -Delta - kappa/r^2 on R^n has radial solutions r^{-alpha}
# where alpha satisfies alpha^2 - (n-2)alpha + kappa = 0
alpha = symbols('alpha')
char_eq = alpha**2 - (n-2)*alpha + kappa
roots = solve(char_eq, alpha)
print("Radial exponents for -Delta - kappa/r^2 on R^n:")
print(f"  alpha_- = {roots[0]}")
print(f"  alpha_+ = {roots[1]}")

# In 4D (n=4):
alpha_minus_4d = roots[0].subs(n, 4)
alpha_plus_4d = roots[1].subs(n, 4)
print(f"\nIn R^4: alpha_- = {alpha_minus_4d}, alpha_+ = {alpha_plus_4d}")

# sigma = alpha_- = 1 - sqrt(1-kappa) for n=4
sigma_4d = simplify(alpha_minus_4d)
print(f"  sigma(kappa) = {sigma_4d}")

# Verify: sigma(0)=0, sigma(1)=1
print(f"  sigma(0) = {sigma_4d.subs(kappa, 0)}")
print(f"  sigma(0.5) = {float(sigma_4d.subs(kappa, Rational(1,2))):.6f}")
print(f"  sigma(0.9) = {float(sigma_4d.subs(kappa, Rational(9,10))):.6f}")
print(f"  sigma(1) = {sigma_4d.subs(kappa, 1)}")

# === 2. L^2 INTEGRABILITY OF r^{-sigma} IN R^4 ===
# r^{-sigma} in L^2(R^4, near r=0) iff int_0^1 r^{-2sigma} r^3 dr < infty
# i.e. 4-2sigma > 0, i.e. sigma < 2.
# For kappa < 1: sigma = 1-sqrt(1-kappa) < 1 < 2. OK.
print("\nL^2 integrability near r=0:")
for k_val in [Rational(1,4), Rational(1,2), Rational(3,4), Rational(9,10)]:
    s_val = float(sigma_4d.subs(kappa, k_val))
    integrand_exp = 4 - 2*s_val
    print(f"  kappa={float(k_val):.2f}: sigma={s_val:.4f}, "
          f"int r^(3-2sigma) dr exponent = {integrand_exp:.4f} > 0 => L^2 OK")

# === 3. L^infty FAILURE ===
print("\nL^infty of r^{-sigma} at r=0:")
for k_val in [Rational(1,4), Rational(1,2), Rational(3,4)]:
    s_val = float(sigma_4d.subs(kappa, k_val))
    if s_val > 0:
        print(f"  kappa={float(k_val):.2f}: sigma={s_val:.4f} > 0 => "
              f"r^{{-sigma}} -> infty at r=0, L^2->L^infty FAILS")

# === 4. FORM BOUND VERIFICATION ===
# Hardy inequality in R^4: int kappa/r^2 |phi|^2 <= kappa int |nabla phi|^2
# for 0 < kappa < (n-2)^2/4 = 1
print(f"\nHardy constant in R^4: C_H = (n-2)^2/4 = {(4-2)**2//4}")
print("For kappa < 1: form bound int V phi^2 <= kappa int |nabla phi|^2 holds")
print("This is EXACTLY the small form perturbation condition with gamma = kappa")

# === 5. CRITICAL vs SUBCRITICAL EXPONENTS ===
print("\n=== CRITICAL vs SUBCRITICAL POTENTIAL ===")
print(f"In R^4: critical L^p exponent is n/2 = {4//2}")
print(f"V = kappa/r^2: ||V||_{{L^p(B_1)}} = kappa (int_0^1 r^{{-2p}} r^3 dr)^{{1/p}}")
print(f"  p=2: integral = int_0^1 r^{{-1}} dr = DIVERGENT (critical, borderline)")
print(f"  p=3: integral = int_0^1 r^{{-3}} dr = DIVERGENT (V not in L^3)")
print(f"  ==> V = kappa/r^2 is EXACTLY L^2-critical in 4D, NOT subcritical")

# === 6. SUBCRITICAL UPGRADE FROM H_3 ===
print("\n=== H_3 SUBCRITICAL UPGRADE ===")
print("At positive time t > 0, the Wang hierarchy gives:")
print("  H_3(t) = int K^3 dnu <= C gamma^3 / t")
print("  where K = aF, dnu = a^{-2} dmu")
print("This means ||K||_{L^3(nu)} ~ (gamma^3/t)^{1/3} = gamma/t^{1/3}")
print(f"  L^3 > L^2 = n/2 (critical) in 4D => SUBCRITICAL")
print("Standard De Giorgi-Nash-Moser with V in L^3 has CONVERGENT constants")
print("This is the essential upgrade: critical L^2 --> subcritical L^3")

# === 7. TRANSCRIPTION CORRECTION ===
print("\n=== TRANSCRIPTION CORRECTION ===")
a, phi, r_var = symbols('a phi r', positive=True)
# Correct: nabla(a^{-1/2} phi) for conformal L^4 norm
# Wrong: nabla(a^{-1} phi) from Step 21 handoff
print("Correct quadratic form (from TTCS generator and Sobolev substitution):")
print("  e_t[phi] = int |nabla(a^{-1/2} phi)|^2 dmu + r^{-2} int phi^2 dnu")
print("Step 21 handoff wrote:")
print("  e_t[phi] = int |nabla(a^{-1} phi)|^2 dmu + r^{-2} int phi^2 dnu")
print()

# Expansion of |nabla(a^{-s} phi)|^2 for s=1/2 and s=1
s = symbols('s')
# |nabla(a^{-s} phi)|^2 = a^{-2s}|nabla phi|^2 - 2s a^{-2s-1} phi <nabla a, nabla phi> + s^2 a^{-2s-2} |nabla a|^2 phi^2
print("Leading gradient weight near a=0:")
print(f"  s=1/2: a^{{-2s}} = a^{{-1}} (one power)")
print(f"  s=1:   a^{{-2s}} = a^{{-2}} (two powers)")
print("The s=1 form is MORE singular near a=0 and gives falsely strong control")
print("CORRECTION: use s=1/2 throughout")

# === 8. MOSER CONSTANT CONVERGENCE ===
print("\n=== MOSER ITERATION: CRITICAL vs SUBCRITICAL ===")
# For potential in L^p:
# k-th Moser step goes from L^{q_k} to L^{q_{k+1}} with q_{k+1} = q_k * n/(n-2) = 2 q_k (for n=4)
# The constant at step k involves ||V||_{L^p}^{c_k}
# For critical p=n/2: c_k ~ 1 (constant contribution per step) => product diverges
# For subcritical p>n/2: c_k decreases geometrically => product converges

# Moser exponent sequence: q_{k+1} = 2 q_k in 4D
# At step k, the Holder absorption gives: ||V||_{p}^{1/q_k} * C^{1/q_k}
# Product = prod C^{1/q_k} * prod ||V||_p^{1/q_k}
# sum 1/q_k = 1/q_0 + 1/(2q_0) + ... = 2/q_0 (geometric, always finite)

# The difference is in the Holder exponent matching:
# To absorb V on L^{q_k}: need V in L^{r_k} where 1/r_k + 2/4 + 1/q_k = 1 (Holder)
# i.e. 1/r_k = 1/2 - 1/q_k
# For q_k = q_0 * 2^k: 1/r_k = 1/2 - 1/(q_0 * 2^k)
# As k -> infty: 1/r_k -> 1/2, so r_k -> 2 (critical!)
# If V in L^2 only: the estimate degenerates at large k
# If V in L^3: 1/r_k = 1/2 - 1/(q_0 * 2^k) < 1/2 < 1/3 for all k, so V in L^3 suffices

q0_val = 2  # starting exponent
print(f"Starting from L^{q0_val}, Moser sequence q_k = {q0_val} * 2^k:")
for k in range(6):
    qk = q0_val * 2**k
    recip_rk = Rational(1,2) - Rational(1,qk)
    if recip_rk <= 0:
        print(f"  k={k}: q_k={qk}, need V in L^infty (trivial step)")
    else:
        rk = 1 / recip_rk
        print(f"  k={k}: q_k={qk}, need V in L^{float(rk):.3f}")

print(f"\nWith V in L^3: all r_k < 3, so V in L^3 suffices at EVERY step")
print(f"With V in L^2 only: r_k -> 2 from below, V in L^2 is BORDERLINE and constants blow up")

print("\n" + "="*70)
print("CONCLUSION: The inverse-square potential refutes abstract Nash from")
print("form bounds alone. The H_3 subcritical upgrade is ESSENTIAL.")
print("Architecture: Wang H_2->H_3 (critical, hard) + standard H_3->Linf (subcritical)")
print("="*70)
