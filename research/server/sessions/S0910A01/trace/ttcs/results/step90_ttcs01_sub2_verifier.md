# TTCS Independent Branch Record

```json
{
  "step_id": 90,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step90_K_symmetry_cross_parity_elimination.md",
    "Sessions/S0910A01/workspace/data/step90_K_symmetry_chirality_exchange.json",
    "Sessions/S0910A01/workspace/data/step90_K_symmetry_H4_transport_fix.json",
    "Sessions/S0910A01/workspace/notes/step89_correction_and_relative_green.md",
    "Sessions/S0910A01/workspace/notes/step88_four_node_structural_theorem.md"
  ]
}
```

## Task

Verify the K-symmetry argument for the product orbifold (S^2 x S^2)/Z_2 desingularization. K(z,w) = (bar(z), w) is complex conjugation on the first sphere, identity on the second. The central claims to verify are:

1. K fixes all four A_1 nodes (NN, NS, SN, SS), has tangent DK = diag(1,-1,1,1), det = -1, and commutes with sigma, A, J.

2. K^* maps omega_2^+ to omega_2^- with sign +1, hence exchanges the positive and negative Eguchi-Hanson models at each node.

3. Cross-parity vanishing: if S_j^1 = (S_j^+ - S_j^-)/2 is K-odd and L_i^0 is K-even, then L_i^0 G_tau S_j^1 = 0 for ALL node pairs (i,j), including diagonal. This eliminates all even-odd and odd-even interactions.

4. Geometric annihilation: q = g_A - g_B is K-even (because K preserves both metrics), hence K-parity orthogonality gives <S_j^1, q> = 0 at the full geometric level, not just the flat V_2 level. Similarly for the four scalar Ozuch zero modes.

5. The relative mixed-minus-all-same interaction reduces to off-diagonal odd-odd terms only. Diagonal odd-odd terms vanish by epsilon_i^2 - 1 = 0. No singular self-subtraction is needed.

Critically examine: (a) whether the Bianchi correction and gauge terms in the Ozuch construction respect K-equivariance, (b) whether there could be additional negative TT modes in the K-odd sector beyond the known K-even mode q, (c) the exact mechanism by which K acts on the linearized curvature functional (receiver).

## Output

## Verification memo: K-symmetry argument for the (S²×S²)/ℤ₂ desingularization

Session S0910A01, Steps 88–90. I recomputed the group-theoretic and 2-form statements independently, traced the representation-theory argument behind cross-parity vanishing and geometric annihilation, and examined the three points you flagged. The core algebraic content is correct; the geometric upgrade rests on one equivariance hypothesis that is stated but only partially checked; and there is one place where the memo prose (§7) reads more optimistically than the accompanying data file, which is the accurate version.

---

### 1. Node-fixing, tangent action, determinant, commutation (statement 1) — independently reproduced

Take the ℤ₂ generator as σ(z,w)=(−z,−w) (rotation by π about the pole axis on each factor), fixed points z,w∈{0,∞}, giving the four A₁ points NN, NS, SN, SS. Conjugation K(z,w)=(z̄,w) fixes 0 and ∞ on the first factor and is the identity on the second, so K fixes all four nodes — reproduced. K²=I is immediate.

Commutation with σ, which is what lets K descend to 𝒪: Kσ(z,w)=(−z̄,−w)=σK(z,w). Confirmed — this is the necessary condition for K to be an isometry of the quotient orbifold, and it holds.

KJ=JK=K_B: KJ(z,w)=(z,w̄)=JK(z,w), and J=K·K_B, K=K_A. All reproduced.

Tangent action: conjugation on S² is reflection across the great circle through the poles, whose differential at a pole fixes one tangent direction and flips the other, giving diag(1,−1) on the first factor and diag(1,1) on the second, hence DK=diag(1,−1,1,1), det=−1, orientation-reversing. Reproduced.

The one item I cannot recheck without its definition is A. The data records `K_A_commute: true` from computation, and the A-orbit grouping {NN,SS}↔{NS,SN} is used elsewhere. The parity conclusions of Steps 89–90 do not depend on A commuting with K (they use only the K-representation on TT tensors), so this is not load-bearing, but the definition of A should be stated where it is invoked so the reader can confirm the recorded commutation.

### 2. SD/ASD exchange with sign +1 on ω₂ (statement 2) — verified by hand

With DK flipping the second tangent coordinate, take the standard basis
ω₁^± = e¹²±e³⁴, ω₂^± = e¹³±e⁴², ω₃^± = e¹⁴±e²³. Then K*e¹²=−e¹², K*e⁴²=−e⁴², K*e²³=−e²³, others fixed, and

- ω₁^+ = e¹²+e³⁴ → −e¹²+e³⁴ = −ω₁^− (sign −1),
- ω₂^+ = e¹³+e⁴² → e¹³−e⁴² = +ω₂^− (sign +1),
- ω₃^+ = e¹⁴+e²³ → e¹⁴−e²³ = +ω₃^− (sign +1).

So the transport matrix on (ω₁,ω₂,ω₃) is diag(−1,1,1), and in particular ω₂^+↦ω₂^− with sign +1. This matches the recorded `transport_matrix` and `omega2_plus_to_omega2_minus_sign: 1.0` exactly, and the 20 000-sample zero-error H⁴ transport is consistent with it. The physical content — an orientation-reversing isometry exchanges Λ⁺↔Λ⁻ and therefore swaps the Eguchi–Hanson chirality inserted at each fixed node — is convention-free; the specific placement of the −1 on ω₁ is a basis label and does not affect any conclusion.

### 3. Cross-parity vanishing (statement 3) — sound as a representation statement, contingent on the reference operator being K-invariant

The argument is the standard ℤ₂-isotypic decomposition: on the K-invariant orbifold, K* is an isometry, so the Lichnerowicz operator P commutes with K*, TT-ness is preserved, and an inner product built from the K-invariant metric pairs the K-even and K-odd isotypic pieces to zero. If S_j¹ is genuinely K-odd and the regularized Green operator G_τ is built from the K-invariant operator (so it preserves K-parity), then G_τS_j¹ is K-odd and L_i⁰∘G_τ∘S_j¹=0 for every pair (i,j).

The diagonal case i=j is the interesting one, and the argument does hold there: the singular self-interaction G_τS_i¹ is still K-odd term by term (G_τ preserves parity regardless of the singularity), so pairing with the K-even receiver L_i⁰ gives zero for each τ and in any limit that exists. So the even–odd and odd–even diagonal self-interactions genuinely drop by symmetry, with no matched subtraction. This is a real simplification and I find no error in it.

The single load-bearing hypothesis is that G_τ (and the receivers) are constructed from the **K-invariant orbifold operator**, not from a chirality-fixed glued metric. This matters because K exchanges the +bubble and the −bubble at each node, so the glued metric for a fixed chirality assignment is *not* K-invariant; only the singular orbifold background and the assignment-flipped configuration are related by K. The formal source space carrying both S_j^± is where the K-representation lives, and K*S_j^+=S_j^− is what makes S_j¹ K-odd. As long as the parametrix/Green operator used for the leading inversion is the orbifold one, everything is internally consistent. This is exactly what the note assumes when it says "K-equivariant regularization," and it is a genuine modeling choice, not automatic.

### 4. Geometric annihilation of q and the scalar zero modes (statement 4) — correct, and exactly as strong as full-construction K-equivariance

q=g_A−g_B: K is an isometry of each factor metric, so K*g_A=g_A, K*g_B=g_B, hence K*q=q, K-even. Then ⟨S_j¹,q⟩=0 because S_j¹ is K-odd and q is K-even. Reproduced.

The four scalar modes u g: u_A=cosθ_A is the first-factor height (=x₂ in coordinates with the fixed axis along x₂). K flips x₁ and fixes x₂, so u_A is K-invariant; u_B=y₂ lies on the second factor where K is the identity. All four u_A g_A, u_A g_B, u_B g_A, u_B g_B are K-even. Reproduced.

The upgrade from the Step-89 flat V₂ computation (which showed S_odd(q)=0 by explicit index support in the fully mixed sector) to a "full geometric" statement is legitimate, but its strength is precisely the strength of the assertion K*S_j^+=S_j^− at the **full** geometric level. The flat V₂ identity is unconditional (verified on the 100-dimensional Hessian basis, zero failures). The geometric orthogonality is unconditional **only after** one knows the full source (with cutoff, Bianchi correction, curved parametrix, and Ozuch radial corrections) is K-odd. So statement 4's "full, not just principal" inherits the equivariance hypothesis and is no stronger than it. The note flags this correctly in §9 item 4; I want to make explicit that the flat identity and the geometric upgrade are two distinct tiers of evidence, the first proven, the second conditional.

### 5. Reduction to off-diagonal odd–odd (statement 5) — algebra is correct given statement 3

With K^{01}=K^{10}=0 for all pairs, the (ε_j−1) and (ε_i−1) terms in Δ_ε drop, leaving Σ a_i b_j(ε_iε_j−1)K_{ij}^{11}; the diagonal odd–odd coefficient ε_i²−1=0 removes i=j in the difference (both the mixed and all-same assignments carry the same singular a_i b_i K_{ii}^{11}, which cancels). The even–even K^{00} term carries coefficient (1−1)=0 in the relative comparison and drops. So Δ_ε is an off-diagonal odd–odd sum over distinct nodes, finite because the link integrals sit at points separated by a definite orbifold distance. The algebra is correct.

---

### (a) K-equivariance of the Bianchi correction, gauge, and cutoff

The parts that are structurally forced:
- The gluing cutoff depends on geodesic distance to the node; K is an isometry fixing each node, so that distance is K-invariant and the cutoff is K-invariant. Automatic.
- The Bianchi/de Donder gauge operator δ_g δ_g* built from the K-invariant orbifold metric commutes with K*, so the gauge-fixed correction is K-equivariant at the level of the orbifold background. Automatic.

The parts that are **not** automatic and are where the equivariance must actually be verified:
- The full link-integral source in Ozuch's expansion is 3∫⟨H⁴,V_{l,2}⟩+∫⟨H₂⁴,V_{l,0}⟩ (Step 89 §2, Ozuch lines 625–638). The transport K*H⁴_+=H⁴_− is verified exactly. The analogous transport of the **second multipole H₂⁴** and of the radial profile functions V_{l,0}, V_{l,2} entering the same formula has not been checked, and these are precisely the objects that carry the full geometric source. Because H₂⁴ and the radial profiles are determined by the Eguchi–Hanson geometry, and EH with reversed orientation is isometric to EH with flipped chirality, it is plausible they transport identically to H⁴; but the explicit sample check that was done for H⁴ (20 000 points, zero error) should be repeated for H₂⁴ and for the V_{l,·} profiles before the "full geometric" tier of statement 4 is treated as established rather than plausible.
- Beyond the leading order, a Green operator built from the assignment-dependent glued metric acquires bubble-dependent corrections that K maps to the flipped-assignment corrections; K-equivariance of these is only the orbifold-reference equivariance, valid for the leading spectral inversion. Since the surviving object Δ_ε and its sign are anyway placed at the O(t³) inter-node layer (below Ozuch Prop 2.19's O(t^{5/2}) reach, Step 89 §10 — and t³=o(t^{5/2}) is correct since 3>5/2), the equivariance one actually needs for the parity vanishing (statements 3–4) is the orbifold-level one, which holds; the higher-order assignment-dependent equivariance is only relevant to the still-open sign, where the note already leaves the answer undetermined.

Net: the cutoff and gauge equivariance are structurally fine; the concrete remaining verification is the transport of H₂⁴ and the radial profiles, which is a direct extension of the H⁴ transport script.

### (b) Additional non-positive modes in the K-odd TT sector

This is the pivotal unresolved point, and the note correctly frames it as a concrete spectral question rather than an assumption. Independent assessment:

- The single sub-zero eigentensor exhibited is q=g_A−g_B with Pq=−q, K-even. This is the classic destabilizing direction of the product Einstein metric on S²×S² (relative rescaling of the two factors). The stability literature for product Einstein metrics (Kröncke; Page–Pope type analyses) indicates coindex one for S²×S² — i.e., q is expected to be the unique eigentensor with P-eigenvalue < 0. If that is confirmed, the K-odd TT sector has no sub-zero eigenvalue, since q is K-even.
- The question is finite and computable: the TT symmetric 2-tensors on S²(1)×S²(1) decompose under SO(3)×SO(3) into (harmonic on factor A) ⊗ (harmonic on factor B) ⊗ (tensor type), and P is diagonalized block-wise by separation of variables. Enumerating the low blocks, computing their P-eigenvalues, and labeling each block's K-parity would settle whether any non-positive eigenvalue sits in the K-odd sector. The census in Step 90 §8 lists only a handful of low modes and is not yet such an enumeration.
- The zero modes must be enumerated with the same care as the sub-zero ones. The four scalar u g modes are the l=1 conformal directions from each factor's conformal group; the note lists them all K-even. One should also confirm there are no further P-kernel tensors (e.g., additional infinitesimal Einstein deformations of the product) and check their K-parity. S²×S² product is expected rigid Einstein up to the relative-scale direction, so no extra zero modes are expected, but this should be stated as a computed fact, not inferred.

So (b) is genuinely open, and it is the decisive input for any sign statement.

### (c) How K acts on the receiver (linearized curvature functional)

The mechanism is concrete and consistent. The receiver is R_odd(H)=½[(δR^+)_{22}−(δR^−)_{22}] (Step 89 §3), with Step 87 values δR^+=diag(−2,1,1), δR^−=diag(2,−1,−1) for insertion ζ=ω₂, giving R_odd=½(1−(−1))=1. Under K*, ω₂^+↔ω₂^− with sign +1 (and K²=I forces the reverse map also with +1), so the two chirality slots (δR^+)_{22} and (δR^−)_{22} are interchanged; hence R_even=½[(δR^+)_{22}+(δR^−)_{22}] is fixed (K-even) and R_odd flips sign (K-odd). Equivalently, as functionals, L_i^+∘K*=L_i^−, so L_i⁰=½(L_i^++L_i^−) is K-even by construction and L_i¹ K-odd — non-circular, since the swap L_i^+↔L_i^− is derived from the ω₂ chirality exchange, not assumed. This is exactly the parity assignment the vanishing argument uses.

---

### One internal tension to reconcile

Step 90 §7 states that if P|_{K-odd TT}>0, then "the finite off-diagonal odd–odd interaction inherits a definite sign structure." The data file's `sign_not_determined` field states the accurate position: K-symmetry removes the singular and cross terms but does not fix the sign. The data-file version is the correct one. Positivity of P on the K-odd sector makes the *full* odd–odd kernel matrix K^{11} a positive-semidefinite Gram-type object (under the source–receiver duality suggested by the exact flat identity S_odd=(π²/2)R_odd), but Δ_ε uses only the **off-diagonal** entries, with asymmetric radial weights a_i=t_i, b_j=t_j², and signed coefficients (ε_iε_j−1). As Step 89 §9 itself observed, an off-diagonal matrix with zero diagonal is not positive unless it is zero, so the sign of Δ_ε does not follow from positivity of P. The isolated axial-channel computation gives coefficient (9/128)(1−s_is_j)≥0 with strict positivity on opposite-sign node pairs (reproduced: (s_is_j−1)s_is_j=1−s_is_j), but this is one λ=1 channel; the full off-diagonal K^{11} sums all K-odd modes with 1/λ weights and its sign is not implied by the single positive channel. I recommend §7 be brought into line with the data file: K-odd positivity is necessary but not sufficient for the sign of the relative interaction.

### What would materially advance the positive branch

1. Repeat the exact transport check (as done for H⁴) for H₂⁴ and for the radial profiles V_{l,0}, V_{l,2}, closing the equivariance input to the "full geometric" tier of statement 4.
2. Carry out the finite SO(3)×SO(3) block enumeration of the product Lichnerowicz TT spectrum, tabulating each low block's eigenvalue and K-parity, to settle whether the K-odd sector is free of non-positive eigenvalues (and to confirm the P-kernel is exactly the four K-even scalar modes). This is the input that turns the surviving object into a positive-operator problem.
3. Compute the off-diagonal K_{ij}^{11}(i≠j) at distinct nodes — either through the K-odd spectral sum or a direct PDE solve on the orbifold — since even with K-odd positivity the sign of the asymmetric-weight, signed-coefficient, off-diagonal sum Δ_ε must be evaluated directly.

The K-symmetry step is a real structural simplification: it collapses a multi-sector, self-singular inter-node problem to a single finite off-diagonal odd–odd quantity, and the parity vanishing (statements 3–5) is mathematically sound at the orbifold-reference level. It does not, and the note does not assert that it does, decide Einstein existence on #₃(S²×S²) or Yau-26; the decisive sign question is transferred intact to items (b) and (3) above.