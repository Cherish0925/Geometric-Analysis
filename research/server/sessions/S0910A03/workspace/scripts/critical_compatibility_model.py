"""
Theorem A' : quantitative pinching gap from LeBrun 1998 Weyl estimate,
and search for CRITICAL COMPATIBILITY MODELS: closed smooth 4-manifolds with
  (a) no Einstein metric of any sign  (LeBrun 1998 Thm B),
  (b) NO Chern-Weil/Seiberg-Witten obstruction to arbitrarily tight
      negative Ricci pinching.

Notation: X minimal general type (or 2chi+3tau>0 with nontrivial SW),
A = c_1^2(X) = (2chi+3tau)(X), M = X # k CPbar^2.
Then 2chi+3tau (M) = A - k, chi(M)=chi(X)+k, tau(M)=tau(X)-k.
"""
import sympy as sp
from fractions import Fraction

d = sp.Symbol('delta', positive=True)
lam = sp.Symbol('lambda', positive=True)

print("="*70)
print("PART 1: Theorem A' -- pinching gap from LeBrun 1998")
print("="*70)
print()
print("Ingredients (all for an ARBITRARY metric g on M):")
print("  (CGB+sig)  4pi^2 (A-k) = 2 I_W+ + I_s - I_R")
print("             I_W+=int|W+|^2, I_s=int s^2/24, I_R=int|Ric_0|^2/2")
print("  (LeBrun98 Thm A + Lemma 1)  2 I_W+ + I_s > (32/57) 4pi^2 A")
print("  (pinching)  I_R <= 3delta^2/(1-delta)^2 * I_s")
print()
print("Step 1: subtract -> I_R > 4pi^2 (k - (25/57) A).")
print("Step 2: from CGB, dropping 2I_W+ >= 0:  I_s <= 4pi^2(A-k) + I_R")
print("        with I_R <= c*I_s, c=3d^2/(1-d)^2:")
c_coef = 3*d**2/(1-d)**2
Is_bound = 4*sp.pi**2*(1-lam)/(1-c_coef)   # in units of A, i.e. I_s <= A * this
Is_bound_s = sp.simplify(Is_bound)
print(f"        I_s <= A * {Is_bound_s}")
print()
print("Step 3: combine  c*I_s > 4pi^2(k - 25A/57):")
lhs = sp.simplify(c_coef * Is_bound_s)
print(f"        A*{lhs} > 4pi^2 A (lambda - 25/57)")
ineq = sp.simplify(lhs/(4*sp.pi**2) - (lam - sp.Rational(25,57)))
print()
# Clean form
print("Clean form of the necessary condition (multiply out):")
clean = sp.simplify(3*d**2*(1-lam) - (lam-sp.Rational(25,57))*((1-d)**2-3*d**2))
print(f"   3 delta^2 (1-lambda) - (lambda-25/57)((1-delta)^2-3delta^2) > 0")
print(f"   expanded: {sp.expand(clean)}")
print()
print("Leading order in delta:")
print("   delta^2 > (lambda - 25/57) / (3(1-lambda))")
print()

# Table of critical delta
print("Critical pinching threshold delta_c(lambda) (exact root):")
print(f"{'lambda':>12} {'lam-25/57':>12} {'delta_c':>12}")
for num, den in [(25,57),(0.44,1),(0.45,1),(0.46,1),(0.5,1),(0.55,1),(0.6,1),(2,3),(0.7,1),(0.8,1)]:
    L = Fraction(num,den) if isinstance(num,int) else num
    Lf = float(L)
    if Lf >= 1: continue
    expr = 3*d**2*(1-Lf) - (Lf-25/57)*((1-d)**2-3*d**2)
    roots = sp.solve(sp.Eq(expr,0), d)
    real_pos = sorted([float(r) for r in roots if r.is_real and float(r)>0 and float(r)<1])
    dc = real_pos[0] if real_pos else 0.0
    print(f"{Lf:>12.6f} {Lf-25/57:>12.6f} {dc:>12.6f}")
print()
print("KEY: delta_c(lambda) -> 0 as lambda -> 25/57 from above,")
print("     and delta_c = 0 exactly at lambda = 25/57.")
print()

print("="*70)
print("PART 2: integrality constraint")
print("="*70)
print()
print("k, A integers. lambda-25/57 = (57k-25A)/(57A).")
print("If 57k-25A >= 1 then lambda-25/57 >= 1/(57A), so")
print("   delta^2 > 1/(57A * 3(1-lambda)) >= 1/(171A) * 57/32 = 1/(96A)")
print("   i.e. delta > 1/sqrt(96 A).")
print("This vanishes as A -> infinity: a counterexample SEQUENCE is not excluded.")
print()
print("BUT if 57k = 25A EXACTLY, then lambda-25/57 = 0 and the obstruction")
print("is VACUOUS: I_R > 0 only. Simultaneously LeBrun98 Thm B still applies")
print("since it requires only k >= (25/57)A (equality allowed).")
print()

print("="*70)
print("PART 3: search for CRITICAL COMPATIBILITY MODELS  57 | 25*A, k=25A/57")
print("="*70)
print()
print("Family 1: smooth degree-d hypersurface X_d in P^3 (simply connected,")
print("          minimal general type for d>=5).")
print("   c_1^2 = d(d-4)^2,  c_2 = chi_top = d(d^2-4d+6),  A = c_1^2")
print()
print(f"{'d':>4} {'A=c1^2':>9} {'chi(X)':>9} {'tau(X)':>9} {'57|A?':>7} {'k=25A/57':>10} {'2chi-3|tau|(M)':>15} {'b+(X)':>8}")
found = []
for dd in range(5, 40):
    A = dd*(dd-4)**2
    chiX = dd*(dd*dd-4*dd+6)
    # A = 2chi+3tau  =>  tau = (A-2chi)/3
    tauX = sp.Rational(A - 2*chiX, 3)
    assert tauX.q == 1, f"tau not integer for d={dd}"
    tauX = int(tauX)
    divisible = (25*A) % 57 == 0
    kk = (25*A)//57 if divisible else None
    b2 = chiX - 2   # simply connected
    bplus = (b2 + tauX)//2
    if divisible:
        chiM = chiX + kk
        tauM = tauX - kk
        ht = 2*chiM - 3*abs(tauM)
        print(f"{dd:>4} {A:>9} {chiX:>9} {tauX:>9} {'YES':>7} {kk:>10} {ht:>15} {bplus:>8}")
        found.append((dd, A, chiX, tauX, kk, ht, bplus))
    elif dd <= 12:
        print(f"{dd:>4} {A:>9} {chiX:>9} {tauX:>9} {'no':>7} {'-':>10} {'-':>15} {bplus:>8}")
print()

print("Family 2: X = C_{g1} x C_{g2}, product of curves (minimal general type,")
print("          NOT simply connected).")
print("   c_1^2 = 8(g1-1)(g2-1), chi_top = 4(g1-1)(g2-1), tau = 0")
print()
print(f"{'g1':>4} {'g2':>4} {'A':>8} {'57|25A?':>9} {'k':>7} {'2chi-3|tau|(M)':>15}")
for g1 in range(2, 12):
    for g2 in range(g1, 40):
        n = (g1-1)*(g2-1)
        A = 8*n
        if (25*A) % 57 == 0:
            kk = 25*A//57
            chiX = 4*n
            chiM = chiX + kk
            tauM = 0 - kk
            ht = 2*chiM - 3*abs(tauM)
            print(f"{g1:>4} {g2:>4} {A:>8} {'YES':>9} {kk:>7} {ht:>15}")
            break
print()

print("="*70)
print("PART 4: verification of the primary model  X_19 # 1875 CPbar^2")
print("="*70)
D = 19
A = D*(D-4)**2
chiX = D*(D*D - 4*D + 6)
tauX = (A - 2*chiX)//3
k = 25*A//57
print(f"X = smooth degree-{D} surface in P^3")
print(f"  c_1^2(X) = A = {D}*{(D-4)}^2 = {A}")
print(f"  chi_top(X) = c_2 = {chiX}")
print(f"  tau(X) = (A - 2chi)/3 = {tauX}")
print(f"  check A = 2chi+3tau: {2*chiX + 3*tauX} == {A} -> {2*chiX+3*tauX == A}")
print(f"  b_2(X) = chi-2 = {chiX-2}  (simply connected, Lefschetz)")
bp = (chiX-2+tauX)//2; bm = (chiX-2-tauX)//2
print(f"  b^+(X) = {bp},  b^-(X) = {bm}   (b^+>1 -> SW invariant well-defined, =+-1)")
print()
print(f"  k = 25*A/57 = 25*{A}/57 = {25*A}/57 = {k}   (exact integer: {25*A % 57 == 0})")
print(f"  25/57 * A = {25*A/57}  == k -> {abs(25*A/57 - k) < 1e-12}")
print()
M_chi = chiX + k
M_tau = tauX - k
print(f"M = X # {k} CPbar^2:")
print(f"  chi(M) = {M_chi},  tau(M) = {M_tau}")
print(f"  2chi+3tau (M) = {2*M_chi + 3*M_tau}  ( = A-k = {A-k} -> {2*M_chi+3*M_tau == A-k})")
print(f"  strict Hitchin-Thorpe: 2chi - 3|tau| = {2*M_chi - 3*abs(M_tau)} > 0 -> {2*M_chi-3*abs(M_tau) > 0}")
print(f"  k/A = {k}/{A} = {k/A:.10f};  25/57 = {25/57:.10f};  equal -> {abs(k/A - 25/57)<1e-14}")
print()
print("OBSTRUCTION STATUS for M:")
print(f"  LeBrun 1998 Thm B: k >= (25/57)A ?  {k} >= {25*A/57} -> {k >= 25*A/57}")
print("     => M admits NO Einstein metric (any sign of lambda).")
print(f"  Theorem A (this session): needs k/A <= 2/3 + d^2/(1-d)^2.")
print(f"     k/A = {k/A:.6f} <= 2/3 = {2/3:.6f} -> satisfied for ALL delta >= 0. No obstruction.")
print(f"  Theorem A' (this session): needs delta^2 > (k/A - 25/57)/(3(1-k/A)).")
print(f"     k/A - 25/57 = {k/A - 25/57:.3e} = 0 exactly -> NO obstruction for any delta>0.")
print(f"  Strengthened Hitchin-Thorpe (Thm B, this session): requires 2chi>3|tau|.")
print(f"     2chi-3|tau| = {2*M_chi-3*abs(M_tau)} > 0 -> satisfied. No obstruction.")
print(f"  Simplicial volume / entropy obstructions: require infinite pi_1.")
print(f"     pi_1(M) = 1 (X simply connected, connected sum with CPbar^2) -> not applicable.")
print()
print("CONCLUSION: M = X_19 # 1875 CPbar^2 is a closed, simply connected, smooth")
print("4-manifold that admits NO Einstein metric, and for which every known")
print("Chern-Weil / Seiberg-Witten / Hitchin-Thorpe estimate is compatible with")
print("arbitrarily tight negative Ricci pinching ||Ric+g||_op <= delta, delta->0.")
print("Whether such metrics actually exist is now the decisive question for Yau 26.")
print()

print("="*70)
print("PART 5: what a putative tight-pinched metric on M must satisfy")
print("="*70)
print("From I_R > 4pi^2(k-25A/57) = 0 : no constraint.")
print("From LeBrun96 Thm 2: int s^2 > 32pi^2 A.")
print(f"  s^2 <= 16(1+d)^2 => Vol > 2pi^2 A/(1+d)^2 = {2*A:.0f} pi^2/(1+d)^2")
print("From CGB(2chi+3tau) with I_W+ >= 0:")
print("  4pi^2(A-k) >= (2(1-d)^2/3 - 2d^2) Vol + 2 I_W+")
print(f"  A-k = {A-k}")
print(f"  => Vol <= 4pi^2*{A-k}/(2/3) = {6*(A-k)} pi^2  as d->0")
print(f"  Vol in ({2*A} pi^2, {6*(A-k)} pi^2) = ({2*A}, {6*(A-k)}) pi^2 as d->0")
print(f"  consistency: {2*A} < {6*(A-k)} -> {2*A < 6*(A-k)}")
print(f"  ratio Vol_max/Vol_min = {6*(A-k)/(2*A):.6f}  (= 3(1-25/57) = {3*(1-25/57):.6f})")
print()
print("Also 2 I_W+ <= 4pi^2(A-k) - (2/3)Vol, so with Vol > 2pi^2 A:")
wmax = 2*sp.pi**2*(A-k) - sp.pi**2*sp.Rational(2,3)*2*A
print(f"  int|W+|^2 <= 2pi^2(A-k) - (2/3)pi^2*2A = {sp.nsimplify(2*(A-k) - 4*A/3)} pi^2 = {2*(A-k)-4*A/3:.2f} pi^2")
print(f"  positive -> {2*(A-k)-4*A/3 > 0}; so W+ is constrained but not forced to vanish.")
print()
print("DONE")
