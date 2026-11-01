"""Step 83: exact algebra behind the Weyl-deficit / normalized-action results.

Conventions (session, Step 77): for a closed oriented Einstein 4-manifold
  4 pi^2 (2chi+3tau) = int (2|W+|^2 + s^2/24)        (Ric° = 0)
  Shat^2 := s^2 Vol  (normalized Einstein-Hilbert action squared, dim 4)
  D(g)   := int (s^2/24 - |W+|^2)                    (Weyl deficit)
For an almost-Kahler Einstein metric (Step 77, Prop 77.1)
  |W+|^2 - s^2/24 = 2|eta|^2 + trV^2 + s q/8 + 3 q^2/32   (pointwise)
  |s| Q/16 = int|eta|^2 + int trV^2 + (3/32) int q^2      (AAD balance, s<0)
  T_AK = int (trV^2 + 3 q^2/32)
Checks:
  (1) D = Shat^2/16 - 2 pi^2 T+,  T+ = 2chi+3tau.
  (2) AKE: D = T_AK, hence s^2 V = 32 pi^2 T+ + 16 T_AK.
  (3) reversed orientation in a KE component: T_AK' = 12 pi^2 tau.
  (4) ball quotient, reversed orientation: with W+'=0 and s*=s+q (Step-77 convention)
      the direct value s^2V/24 agrees with the forced 12 pi^2 tau (no contradiction;
      exclusion of a reversed AK structure on the CH metric needs Armstrong's theorem).
  (5) blowups: Shat^2 >= 32 pi^2 A and T+ = A - k + C+ with C+ <= 0 give
      D(V) >= 2 pi^2 (k - C+).
Output: printed residuals (all must be 0) and a JSON record.
"""
import json, os
import sympy as sp

pi = sp.pi
s, V, W2, chi, tau = sp.symbols('s V W2 chi tau', real=True)  # W2 = int|W+|^2
Shat2 = s**2*V
Tplus = (2*W2 + s**2*V/24)/(4*pi**2)          # Gauss-Bonnet+signature, Einstein
D = s**2*V/24 - W2
r1 = sp.simplify(D - (Shat2/16 - 2*pi**2*Tplus))

# (2) AKE
E, TV, Q, Q2 = sp.symbols('E TV Q Q2', real=True)  # int|eta|^2, int trV^2, int q, int q^2
int_W2_minus = 2*E + TV + s*Q/8 + sp.Rational(3, 32)*Q2   # int(|W+|^2 - s^2/24)
aad = sp.Eq(-s*Q/16, E + TV + sp.Rational(3, 32)*Q2)      # s<0
Qsol = sp.solve(aad, Q)[0]
T_AK = TV + sp.Rational(3, 32)*Q2
r2 = sp.simplify(-int_W2_minus.subs(Q, Qsol) - T_AK)

# (3) reversed orientation: AK for -orientation, c1(J')^2 = 2chi-3tau; KE value Shat^2 = 32pi^2(2chi+3tau)
TAKp = (32*pi**2*(2*chi+3*tau) - 32*pi**2*(2*chi-3*tau))/16
r3 = sp.simplify(TAKp - 12*pi**2*tau)

# (4) ball quotient chi = 3 tau.  If W+' = 0 (reversed orientation of CH^2/Gamma) and AK:
# s* = s/3 (W+'=0) and s* = s + q  => q = -2s/3, W3+ = 0 => T_AK' = 3 q^2 V/32 = s^2 V/24
Sh2 = 32*pi**2*(2*chi+3*tau)
TAK_direct = Sh2/24
TAK_forced = 12*pi**2*tau
r4 = sp.simplify((TAK_direct - TAK_forced).subs(chi, 3*tau))   # 0: consistent

# (5) blowups
A, k, Cp = sp.symbols('A k C_plus', real=True)
# D(V) = Shat^2(V)/16 - 2 pi^2 T+(V), T+(V) = A - k + C+ (C+ = -m/2pi^2 <= 0),
# LeBrun 2001 Prop 4.2/Thm 4.3: int|Ric|^2 >= 8 pi^2 (A+k) => Shat^2 >= 32 pi^2 (A+k) (Einstein)
DV_lower = 32*pi**2*(A + k)/16 - 2*pi**2*(A - k + Cp)
r5 = sp.simplify(DV_lower - 2*pi**2*(2*k - Cp))

res = {'r1_D_affine_in_Shat2': str(r1), 'r2_AKE_D_equals_TAK': str(r2),
       'r3_reversed_TAK_12pi2tau': str(r3),
       'r4_ballquotient_reversed_consistency': str(r4),
       'r5_blowup_D_bound': str(r5)}
for kk, vv in res.items():
    print(kk, '=', vv)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'step83')
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, 'weyl_deficit_algebra.json'), 'w') as f:
    json.dump(res, f, indent=1)
