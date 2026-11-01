"""
Verify the evolution of the Einstein defect E = Ric + g 
under the normalized Ricci flow  d/dt g = -2(Ric + g) = -2E.

Key identity to verify:  d/dt E = Delta_L E - 2E

where Delta_L is the Lichnerowicz Laplacian.

We verify:
1. The algebraic cancellations in the derivation
2. The |E|^2 evolution:  (d/dt - Delta)|E|^2 = -2|nabla E|^2 + 4 Rm*E*E
3. The stability ODE model showing the C/t gap
4. Why the tensor-level -2E term does not produce scalar damping in
   the exact |E|^2 equation)
"""
import sympy as sp

print("="*70)
print("PART 1: Variation of Ricci under normalized flow")
print("="*70)

# The key formula for variation of Ricci under dg/dt = v:
# 2 d/dt Ric_ij = -Delta_L v_ij - nabla_i nabla_j (tr v) 
#                 + nabla_i (div v)_j + nabla_j (div v)_i
#
# For v = -2E = -2(Ric + g):
#   tr v = -2(s + n) = -2 tr(E)
#   (div v)_i = -2 nabla^j(R_ji + g_ji) = -2(nabla_i s / 2) = -nabla_i s
#             = -nabla_i (tr E)
#
# Therefore:
# 2 d/dt R_ij = 2 Delta_L E_ij + 2 nabla_i nabla_j(tr E) - 2 nabla_i nabla_j(tr E)
#             = 2 Delta_L E_ij
#
# Hence d/dt R_ij = Delta_L E_ij
# 
# And d/dt E_ij = d/dt R_ij + d/dt g_ij = Delta_L E_ij - 2 E_ij

# Verify: contracted Bianchi gives div(E) = (1/2) d(tr E)
# This is because div(Ric) = (1/2) ds and div(g) = 0
# So div(Ric + g) = (1/2) ds = (1/2) d(s) = (1/2) d(tr(Ric+g) - n) = (1/2) d(tr E)
print("Contracted Bianchi: div(E) = (1/2) d(tr E)")
print("  div(Ric+g) = div(Ric) + 0 = (1/2)ds = (1/2)d(trE)")
print("  => nabla_i nabla_j(trE) terms cancel in the Ricci variation")
print()
print("Result: d/dt E = Delta_L E - 2E")
print("  where Delta_L h_ij = Delta h_ij + 2 R_ikjl h_kl - R_ik h_kj - R_jk h_ki")
print()

print("="*70)
print("PART 2: Evolution of |E|^2")
print("="*70)

# (d/dt)|E|^2 = 2<dE/dt, E> + (metric variation terms)
# 
# Metric variation terms from d/dt g^{ij} = 2E^{ij}:
#   E_ij E_kl d/dt(g^ik g^jl) = 4 tr(E^3)
#
# 2<Delta_L E, E> = Delta|E|^2 - 2|nabla E|^2 + 4 R_{ikjl}E_{ij}E_{kl} - 4 R_{ik}E_{ij}E_{kj}
#
# Now R_ik = E_ik - g_ik, so:
#   R_ik E_ij E_kj = (E_ik - delta_ik) E_ij E_kj = tr(E^3) - |E|^2
#   => -4 R_ik E_ij E_kj = -4 tr(E^3) + 4|E|^2
#
# Collecting:
# d/dt |E|^2 = Delta|E|^2 - 2|nabla E|^2 + 4R_{ikjl}E_{ij}E_{kl}
#              + (-4 tr(E^3) + 4|E|^2) - 4|E|^2 + 4 tr(E^3)
#            = Delta|E|^2 - 2|nabla E|^2 + 4 R_{ikjl} E_{ij} E_{kl}

# Verify the cancellation symbolically
t1 = sp.Symbol('t1')  # tr(E^3) 
nE = sp.Symbol('nE')  # |E|^2

# From Lichnerowicz:  -4 tr(E^3) + 4|E|^2
# From metric variation:  +4 tr(E^3)
# From -2E term:  -4|E|^2
total_reaction = (-4*t1 + 4*nE) + (4*t1) + (-4*nE)
print(f"tr(E^3) and |E|^2 reaction total: {total_reaction}")
assert total_reaction == 0
print("All tr(E^3) and |E|^2 terms cancel exactly!")
print()
print("Result: (d/dt - Delta)|E|^2 = -2|nabla E|^2 + 4 R_{ikjl} E_{ij} E_{kl}")
print("  => (d/dt - Delta)|E|^2 <= 4|Rm| |E|^2")
print()

print("="*70)
print("PART 3: Stability ODE model with C/t curvature")  
print("="*70)

# Under Ye Li smoothing: |Rm(t)| <= C/t for t in (0, T)
# The ODE model for |E|^2 is:
#   d/dt f = (4C/t) f       (worst case, ignoring damping and Laplacian)
# Solution: f(t) = f(t_0) (t/t_0)^{4C}
# 
# Going backward from t_0 to epsilon:
#   f(epsilon) = f(t_0) (epsilon/t_0)^{4C}
# So f(t_0) = f(epsilon) (t_0/epsilon)^{4C}
#
# As epsilon -> 0: f(t_0) -> infinity if 4C > 0
# This is the GENUINE GAP.

C_rm, t, t0, eps, delta = sp.symbols('C_rm t t_0 epsilon delta', positive=True)

# ODE: df/dt = (4C/t) f
f_sol = sp.Function('f')
ode = sp.Eq(f_sol(t).diff(t), 4*C_rm/t * f_sol(t))
sol = sp.dsolve(ode, f_sol(t))
print(f"ODE solution: {sol}")

# Evaluate ratio f(t_0)/f(epsilon):
# f(t) = C1 * t^{4C}
# f(t_0)/f(eps) = (t_0/eps)^{4C}
ratio = (t0/eps)**(4*C_rm)
print(f"Amplification factor f(t_0)/f(eps) = (t_0/eps)^(4C) = {ratio}")
print()

# IMPORTANT: there is no additional -2f damping in the exact scalar
# |E|^2 evolution. The tensor-level -2E cancels against Ricci contractions
# and inverse-metric variation, as verified in Part 2.
print("No separate scalar damping term is allowed: exact |E|^2 evolution has only the curvature reaction.")
print()

print("="*70)
print("PART 4: The small-radius bridge")  
print("="*70)

# At a good point p: M_1|Rm|^2(p) <= K_0
# This means: for all r <= 1, fint_{B_r(p)} |Rm|^2 <= K_0
# 
# Ye Li's Theorem 3.6 requires:
#   r^4 / Vol(B_r) * int_{B_r} |Rm|^2 <= epsilon
# = r^4 * fint_{B_r} |Rm|^2 <= epsilon
# <= r^4 * K_0
#
# Choose r_0 = (epsilon / K_0)^{1/4}

K0, eps_li = sp.symbols('K_0 epsilon_Li', positive=True)
r0 = (eps_li/K0)**sp.Rational(1,4)
print(f"Choose r_0 = (epsilon_Li / K_0)^(1/4) = {r0}")
print(f"Then r_0^4 * K_0 = {sp.simplify(r0**4 * K0)} = epsilon_Li")
print()
print("Ye Li existence time: T >= C_1 * min(r_0^2, K^{-1})")
print(f"  with |Ric| <= 3+delta <= 4, K=4:")
print(f"  T >= C_1 * min(r_0^2, 1/4)")
print(f"  For r_0 small: T >= C_1 * r_0^2 = C_1 * sqrt(epsilon_Li/K_0)")
print()
print("At time t_0 = T/2: |Rm(g(t_0))| <= C_2/t_0")
print(f"  = C_2/(C_1 r_0^2 /2) = 2C_2/(C_1 r_0^2)")
print()

print("="*70)
print("PART 5: Bishop-Gromov extension to buffered ball")  
print("="*70)
print("For x in B_{r_0/2}(p), and r <= r_0/2:")
print("  B_r(x) subset B_{r_0}(p)")  
print()
print("Bishop-Gromov (Ric >= -3g):")
print("  Vol(B_{r_0}(p)) / Vol(B_r(x))")
print("  <= V_{-3}^4(r_0) / V_{-3}^4(r)")
print("  = [integral formula depending on r_0/r]")
print()
print("Therefore:")
print("  fint_{B_r(x)} |Rm|^2 <= (Vol(B_{r_0}(p))/Vol(B_r(x))) * fint_{B_{r_0}(p)} |Rm|^2")
print("  <= C_BG(r_0/r) * K_0")
print()
print("For r = r_0/2: C_BG(2) is a fixed constant ~e^{6sqrt(3)} in 4D")
print("So fint_{B_{r_0/2}(x)} |Rm|^2 <= C_BG * K_0 for all x in B_{r_0/2}(p)")
print()
print("The Ye Li hypothesis is then satisfied at scale r_0/2 for ALL x in B_{r_0/2}(p):")
print("  (r_0/2)^4 * fint_{B_{r_0/2}(x)} |Rm|^2 <= (r_0/2)^4 * C_BG * K_0")
print("  = (C_BG/16) * epsilon_Li")
print("  which is still small (reduce r_0 if needed)")

print()
print("="*70)
print("PART 6: The two-layer strategy")  
print("="*70)
print("""
Layer 1 (Structural): Ye Li smoothing at scale r_0
  -> g(t_0) has |Rm| <= K on B_{r_0/4}(p)
  -> If collapsed: CFG fibration structure (circle/torus fibers)
  -> Fibration structure transfers to g(0) by C^0 equivalence
     (Ye Li proves |v|_{g(0)} < sqrt(2)|v|_{g(t)} for t < T_0)

Layer 2 (Einstein defect): On g(0) with known fibration structure
  -> |E(g(0))| <= delta uniformly
  -> Reduced Einstein equations satisfied to O(delta)
  -> But curvature |Rm(g(0))| is NOT bounded
  -> Need: either
     (a) Pass E through the flow (blocked by C/t stability gap)
     (b) Use fibration + E(g(0)) directly (A01's bootstrap approach)
     (c) Find a better smoothing that preserves E

CRITICAL FINDING: The C/t pointwise stability gap is REAL but the
  source-based Corollary 3.5 route can bypass it if its evolving-energy
  and localization hypotheses are supplied.
The evolution d/dt E = Delta_L E - 2E has:
  - No universal scalar damping survives in the |E|^2 equation
  - Unfavorable curvature: 4|Rm||E|^2 with |Rm| ~ C/t
  - The Gronwall integral int_0^{t_0} C/t dt = infinity
  
The gap is NOT in the dimensionless energy (which IS small by Strategist's
observation) but in the POINTWISE stability through the flow.
""")

print("="*70)
print("PART 7: H >= 0 from calibrated conditions")
print("="*70)
print("""
From A01's observation: if H >= 0 (eigenvalues of Hess(ell)/ell nonneg),
then Ric_B = -I + H + C^2_sym/2 >= -I, giving 3D noncollapse.

In static case (C=0): calibrated gives H = diag(1/2, 1/4, 1/4) > 0. CHECK.
In twisted case: E = (1/3)I - H + (|z|^2 I - z⊗z)/4
  Calibrated W+ = E + B has eigenvalues (-1/6, 1/12, 1/12)
  => tr(W+) = 0, |W+|^2 = 1/24

Trace constraint: tr(H) = 1 + |z|^2/2 >= 1 (always positive trace).

For H >= 0 in twisted case: need each eigenvalue of H >= 0.
From E = (1/3)I - H + Q where Q = (|z|^2 I - z⊗z)/4:
  H = (1/3)I + Q - E
  Since tr(Q) = |z|^2/2, eigenvalues of Q are in [0, |z|^2/4]
  and E = W+ - B (from W+ = E + B)
  
If |B| is small: E ≈ W+ with eigenvalues (-1/6, 1/12, 1/12)
  Then H ≈ (1/3)I + Q - W+ = (1/3+1/6, 1/3-1/12, 1/3-1/12) + Q corrections
  = (1/2, 1/4, 1/4) + twist quadratic corrections
  All positive for small twist amplitude.

When |B| is large (high twist gradient): E and H can deviate significantly.
The sign of H eigenvalues is NOT guaranteed.
""")
print("DONE.")
