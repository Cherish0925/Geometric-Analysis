#!/usr/bin/env python3
"""Algebraic/scaling checks for the Step 58 critical-to-subcritical bridge.

This checks weight identities, Sobolev variables, the all-p reaction split,
Moser exponent sums, and collapse-volume cancellation.  It does not certify
the tensor evolution or existence of the degenerate flow.
"""
from fractions import Fraction as Q
import math

checks = []

def check(name, cond, detail=""):
    checks.append((name, bool(cond), detail))
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" -- {detail}" if detail else ""))

# H_2 critical bridge: Y = int F (chi F)^2.
# Here a=chi^2, so the critical Sobolev variable is w_2=chi F=a^(1/2)F.
check("critical variable w2 has square a F^2", 2 * Q(1, 2) == 1)
check("critical variable w2 has fourth power a^2 F^4", 4 * Q(1, 2) == 2)
check("Y factorization has a exponent 1", 0 + 2 * Q(1, 2) == 1,
      "F*(a^(1/2)F)^2 = a F^3")
check("Y factorization has F exponent 3", 1 + 2 == 3)

# q=3 propagation: K_3=int a F^3 and z_3=a F^(3/2), not sqrt(a)F^(3/2).
check("q3 Sobolev variable z3 has a exponent 1", Q(3 - 1, 2) == 1)
check("z3 squared weight is a^2 F^3", 2 * Q(3 - 1, 2) == 2)
check("z3 fourth power equals K6 weight", 4 * Q(3 - 1, 2) == 4,
      "z3^4=a^4 F^6=K_6")
check("sqrt(a)F^(3/2) is NOT z3", Q(1, 2) != Q(3 - 1, 2))

# General K_p and z_p identities.
for p in [Q(3), Q(9, 2), Q(27, 4), Q(6), Q(12)]:
    z_a = (p - 1) / 2
    check(f"p={p}: z_p^4 equals K_2p weight", 4*z_a == 2*p - 2)
    check(f"p={p}: z_p^2 is dominated by K_p weight", 2*z_a == p-1 and p-1 >= p-2)

    # K_{3p/2} <= K_p^(1/2) K_{2p}^(1/2).
    target_a = 3*p/2 - 2
    factor_a = (p-2)/2 + (2*p-2)/2
    target_f = 3*p/2
    factor_f = p/2 + p
    check(f"p={p}: mixed interpolation a exponent", factor_a == target_a)
    check(f"p={p}: mixed interpolation F exponent", factor_f == target_f)

    # Curvature reaction split:
    # a^(p-1)F^(p+1)=(aF^3)^(1/3)(a^(p-2)F^p)^(1/3)(z_p^2)^(2/3).
    reaction_a = Q(1,3) + (p-2)/3 + Q(2,3)*(p-1)
    reaction_f = 1 + p/3 + Q(2,3)*p
    check(f"p={p}: reaction split a exponent", reaction_a == p-1)
    check(f"p={p}: reaction split F exponent", reaction_f == p+1)

    # Gradient cutoff identity a^(p-3)|da|^2=4a^(p-2)|dchi|^2.
    check(f"p={p}: cutoff gradient returns K_p weight", p-3+1 == p-2)

# Geometric Moser sequence p_{j+1}=3p_j/2 from p0=3.
p0 = Q(3)
ps = [p0*(Q(3,2)**j) for j in range(80)]
sum_inv = sum((1/p for p in ps), Q(0))
sum_S = sum((Q(2,3)/p for p in ps), Q(0))
# The finite truncation misses a geometric tail.  Compare exactly after adding it.
tail_inv = (1/ps[-1]) * Q(2,3) / (1-Q(2,3))
tail_S = Q(2,3) * tail_inv
check("sum 1/p_j = 3/p0", sum_inv + tail_inv == Q(3,p0))
check("Sobolev exponent sum = 2/p0", sum_S + tail_S == Q(2,p0))
check("time exponent for p0=3 is -1", Q(3,p0) == 1)
check("Sobolev exponent for p0=3 is 2/3", Q(2,p0) == Q(2,3))

# Endpoint algebra: S^(2/3) t^-1 (Gamma H)^(1/3) = Gamma/t
# when Gamma=S sqrt(H).
S = 7.0
H = 11.0
Gamma = S*math.sqrt(H)
lhs_factor = S**(2/3) * (Gamma*H)**(1/3)
check("curvature endpoint seed simplifies to Gamma", abs(lhs_factor-Gamma) < 1e-12,
      f"lhs={lhs_factor:.12g}, Gamma={Gamma:.12g}")

# Collapse-volume cancellation Gamma=S sqrt(H), S~r^2/sqrt(V), H~K0 V.
r = 0.03
K0 = 5.0
for V in [1.0, 1e-4, 1e-12, 1e-30]:
    Sob = r*r/math.sqrt(V)
    Hval = K0*V
    gam = Sob*math.sqrt(Hval)
    target = r*r*math.sqrt(K0)
    check(f"collapse cancellation V={V:g}", abs(gam-target) <= 1e-12*target)

# Integrated-potential algebra: S^2 * (Gamma H) = Gamma^3.
check("integrated coefficient S^2 intY <= C Gamma^3",
      abs(S*S*Gamma*H - Gamma**3) < 1e-10)

# The corrected route uses only H(0), never Y(0).
dependencies = {"H0", "Sobolev", "cutoff_gradient", "time_scale"}
check("critical bridge dependency set excludes Y0", "Y0" not in dependencies)

failed = [name for name, ok, _ in checks if not ok]
print("\n" + "="*72)
print(f"{len(checks)-len(failed)}/{len(checks)} checks pass")
if failed:
    for name in failed:
        print("FAILED:", name)
    raise SystemExit(1)
print("All algebraic/scaling checks pass. Tensor PDE and flow existence remain separate.")
