# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step15_ach_projected_theory.md",
    "Sessions/S1003A02/workspace/scripts/ach_weyl_degeneracy_offbolt.py",
    "Sessions/S1003A02/workspace/data/ach_capd/weyl_degeneracy_offbolt.json",
    "Sessions/S1003A02/workspace/data/ach_capd/rossi_enclosure_b0.8.json",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md"
  ]
}
```

## Task

Independently read the Theorem E proof package and the new off-bolt Weyl computation. Decide what is rigorously proved by the analytic/Fuchsian plus CAPD/Wazewski chain, and separately what the floating-point off-bolt spectra support about conformal Kählerness. Check the use of Derdzinski: does finding three distinct eigenvalues in both chiral Weyl blocks at one interior point exclude the Einstein metric from being locally conformal to a Kähler metric in either orientation? Note that at t=0.5 and d in the validated interval the reported A eigenvalues are approximately (-0.845829,-0.841893,1.687721) and B approximately (-1.9603,0.4966,1.4637), with scalar -24 and Ricci0 norm 2.5e-11. Explain what remains to turn this into a computer-assisted theorem if interval rigor matters.

## Output

# Theorem E and the off-bolt Weyl spectra: what the proof establishes, what the data show, and what an interval certificate would need

## 0. Main conclusions

1. **Theorem E.** The Fuchsian → CAPD → Ważewski → drift chain is logically complete as an existence argument. Every inequality I could recompute from the stated constants checks out. These are the Fuchsian inverse-operator bounds, the q-drift bound, the Rossi enclosure, the smoothness order at the bolt and the constraint propagation. What the proof rests on, beyond the written lemmas, is three things:
   - correctness of the interval code: Arb residual and Jacobian boxes, CAPD transport, and the block-face evaluations;
   - two small links that are true but not written down;
   - one external CR fact.

2. **Off-bolt spectra.** In floating point, both chiral Weyl blocks have three well-separated eigenvalues at t = 0.5, 1 and 2, for all three d values. The separation exceeds the numerical noise by about seven orders of magnitude. The curvature code also passes three independent consistency tests.

3. **Logic of the exclusion.** Three distinct eigenvalues in both blocks at one interior point do exclude conformal Kählerness in either orientation, and by real-analyticity on every open subset. The step needed is the elementary direction "Kähler ⇒ W⁺ degenerate, and degeneracy is conformally invariant", not Derdziński's theorem. The same data also exclude orthogonal Hermitian structures, and they fix the identity component of the isometry group as SU(2).

4. **Making it a theorem.** A computer-assisted version is a small addition to the existing CAPD run. In the invariant frame, W± are diagonal, so the certificate reduces to six signed differences of explicit functions, evaluated on the transported d-boxes at one radius.

## 1. The Theorem E chain

### 1.1 Lemma F (Fuchsian bolt solution)

**Inverse-operator bounds.** Recomputed from the radial integrals; all six are correct.
- (4D²)⁻¹ gives F/(4m²) and F/(4m).
- (4D²+2D)⁻¹ = ½D⁻¹(2D+1)⁻¹ gives F/(2m(2m+1)) and F/(2(2m+1)).
- The DR bound for (4D²−16)⁻¹ is the only one that is not a direct composition. It holds because of the partial-fraction identity D/((D−2)(D+2)) = ½[(D−2)⁻¹+(D+2)⁻¹]. This gives |DR| ≤ ⅛(1/(m−2)+1/(m+2))F|s|^m = Fm|s|^m/(4(m−2)(m+2)), as stated. No Cauchy-type derivative estimate is involved.

**Indicial structure.** Linearizing −2(A⁴−B⁴)/(AB²C²) at A = B = b, C = 1 gives −8δ in E_A and +8δ in E_B. This produces 4D²δ − 16δ, with its resonance at k = 2 (s², i.e. t⁴), carrying the free parameter d.

**Smoothness order at the bolt.** With dσ_i = 2σ_j∧σ_k and σ₃ = dψ + … of period 2π, the isotropy circle rotates σ₁ + iσ₂ by e^{−2iψ}. So (a₁² − a₂²)(σ₁² − σ₂²) carries weight 4. Smoothness then requires a₁² − a₂² = t⁴·(even function), which is exactly A − B = O(s²). This justification is not written in the note; it is the reason the resonance position coincides with the regularity condition.

**Constraint propagation.** With f = t²C_constraint:

f′ = 2tC(1 − tS) = f·O(t), and f(0) = 0.

Grönwall then gives f ≡ 0. This is correct.

The note uses the letter C both for a₃/t and for the constraint ("vanishes at t = 0 because C(0) = 1"). The intended meaning is that a₃′(0) = 1 kills the t⁻² term of the constraint. As written, a reader cannot tell which C is meant.

**Unwritten link 1: continuity in d.** The Ważewski step needs the map d ↦ X(t₀; d) to be continuous. This follows from the contraction, because Y_N is polynomial in d and the contraction constant 0.0325 is uniform on the d-interval. It is not stated.

### 1.2 CAPD transport and the field identity

- The repaired field is source-parsed and agrees symbolically with the exact potentials. The point-box enclosure contains DOP853 up to t = 2.7.
- The note says "zero in all seven components" for a six-variable system X = (m, δ_L, L₃, y_m, η, y₃). Presumably the seventh is the constraint. The data file should say so.

**Unwritten link 2: the transfer at T.** The map from CAPD variables to block coordinates (ub, s1b, s2b, ab, ζ, q) at T is a nonlinear change of variables. That it was evaluated in interval arithmetic is implicit in `wazewski_T2.75.json`, but it is not stated in the proof.

### 1.3 Isolating block and Ważewski argument

**q-drift.** |q′| ≤ (K + 4 sinh 0.9)ζ and ζ ≤ ζ(T)e^{−c(t−T)} give

total drift ≤ 5.106 × 0.009658 / 1.9985 = 0.0247.

The orbit starts at q(T) ≈ 0.801, which is about 0.10 from either q-face. So the q-faces are unreachable.

**Endpoint argument.** The note says d₋ ∈ S₋ "unless its orbit stays forever". The slab margin closes this alternative: −ub′ ≥ 1.87 on the lower slab forces exit within time (1 − 0.708)/1.87 ≈ 0.16. So d₋ ∈ S₋ and d₊ ∈ S₊ outright.

**Corners and the face ζ = 0.** The exit set is closed and every non-u face is strict ingress, so corner exits do not break openness of S±. The face functions were divided by ζ symbolically before evaluation, so ζ = 0 lies inside the verified box. This is necessary, because the block shrinks with ζ.

**Rossi readout.**
- M ζ(T)²/(2c) = 19.5825 × 0.0096574² / 3.99692 = 4.570 × 10⁻⁴.
- This gives q_∞ ∈ [0.783962, 0.785003] and e^q ∈ [2.19013, 2.19241], matching `rossi_enclosure_b0.8.json`.
- The limit Φ̃ → q_∞ holds because a → 0 and ζ → 0.

**ACH rate and completeness.**
- Inside B, all eigen-coordinates are at most Kζ = O(e^{−1.998t}).
- y′ is given by the field, so the second jet also converges at that rate.
- The curvature limit at E(q) is CH² for every q, because q enters the field only through terms carrying ζ.
- Completeness holds because t is arclength on [0, ∞) and the L_i stay finite.

**External fact 3: non-standard CR infinity.** "ρ_∞ ≠ 1 ⇒ CR infinity not the standard sphere" uses the classical fact that left-invariant CR structures on SU(2) are pairwise inequivalent except ρ ↔ 1/ρ. This is Cartan's homogeneous classification: the Cartan tensor is non-zero for ρ ≠ 1. No source passage for it is among the supplied files. Biquard–Herzlich's variation formula (Thm 8.1) in terms of the Cartan tensor would be the natural anchor.

**Conclusion.** Granting the software outputs and these three links, Theorem E is proved as stated: existence for some d₀ in the interval, b = 4/5, completeness, Ric = −6g, real-analyticity, ACH with fibre slot 1, and the stated ρ_∞-enclosure.

## 2. What the floating-point off-bolt spectra support

### 2.1 Reliability of the curvature code

The code takes the exact radial 2-jet (a′ = ay, a″ = a(y² + y′), with y′ from the field), places it in Euler coordinates, and uses autodiff (no finite differences). Three independent tests support it.

- **Einstein residual.** s = −24 and |Ric°| ~ 10⁻¹¹ at every radius. A mis-assembled metric would not produce this.
- **Bolt limit.** As t → 0, A tends to (−91/16, −91/16, 91/8) and B to (−41/16, −41/16, 41/8), and the approach is quadratic in t:
  - the A top eigenvalue deficit is 0.0131, 0.117 and 0.321 at t = 0.01, 0.03, 0.05, i.e. about 130t²;
  - the B deficit is about 35t².
  
  Evenness in t is what smoothness across the bolt requires. This independently confirms the repaired exact bolt blocks of §6.2.
- **Infinity.** At t = 2, B → (−3.9992, 1.937, 2.062) with ‖B‖² = 23.9986. A → 0, with ‖A‖² ≈ 3 × 10⁻⁶. This is the CH² pattern: W⁺ = (s/6, −s/12, −s/12) = (−4, 2, 2) with ‖W⁺‖² = 24, and W⁻ = 0.

These checks also confirm that LA and LB are orthonormal bases of Λ±, since the exact normalizations are reproduced at both ends.

### 2.2 Separation versus noise

**Noise level.** The near-bolt A-gaps for the three d values at t = 0.1 (2.71703, 2.71682, 2.71694 × 10⁻⁶) are non-monotone in d. Their spread therefore measures roundoff, about 2 × 10⁻¹⁰ absolute in W entries. This is consistent with the scalar residual.

**Margins at t = 0.5.** The A gaps are 0.0039 and 2.53; the B gaps are 0.97 and 2.46. That is a factor of at least 10⁷ above the noise. The variation across the validated d-interval is about 10⁻⁷ relative.

### 2.3 Near-bolt structure

Two distinct splitting laws appear near the bolt.

- **B splits at order t².** gap_B ≈ 8.6t², from 8.6 × 10⁻⁴ at t = 0.01 to 0.087 at t = 0.1.
- **A splits at order t⁶.** gap_A ≈ 3t⁶: 2.25 × 10⁻⁹ at t = 0.03 and 4.73 × 10⁻⁸ at t = 0.05, a ratio of 21 against (5/3)⁶ = 21.4. The t = 0.01 values are pure roundoff.

So the A side is degenerate to high order at the bolt, and its nondegeneracy is a high-order effect of the bolt data. Practically, no certificate of A-nondegeneracy should be attempted for t ≲ 0.2; t ∈ [0.5, 2] carries the margin.

The exact coefficient of the t⁶ splitting, a polynomial in (b, d) obtainable from the order-6 Fuchsian polynomial Y_N, would identify which bolt coefficient breaks the A-degeneracy. That is a mechanism statement, not needed for the theorem.

### 2.4 Chirality identification

B is the block that tends to the Kähler W⁺ of the ACH complex structure (J∞ rotates ∂_t into e₁, the fibre slot). In Biquard–Herzlich conventions, W⁺ = B and W⁻ = A.

The BH integrand becomes 3‖A‖² − ‖B‖² + 24, which at t = 2 is ≈ 1.4 × 10⁻³ and decays. This norm convention is the one forced by the CH² ball: the integrand vanishes pointwise there, matching χ − 3τ + ν = 1 − 0 − 1 = 0.

The stored norm² values, with the volume form a₁a₂a₃ dt ∧ σ₁∧σ₂∧σ₃ (∫σ₁σ₂σ₃ = 2π²), are therefore already the input to the ν(S³_ρ) cross-check of §8 of the note.

## 3. The Derdziński step: correct logic and how far it reaches

### 3.1 The direction actually used

1. A Kähler metric (ĝ, J), in the orientation induced by J, has W⁺_ĝ = (s/12)(3/2 ω⊗ω − Id), with spectrum (s/6, −s/12, −s/12). This is degenerate at every point, and identically zero if s = 0.
2. W is conformally invariant as a (1,3)-tensor, and Λ⁺ is a conformally invariant subbundle. Under g = f²ĝ, the operator W⁺ on Λ⁺ changes only by the factor f⁻², so its eigenvalue multiplicities are conformal invariants.
3. Hence g conformal to Kähler on an open set U, in orientation O, forces W⁺_O(g) to have a repeated eigenvalue at every point of U.

No Einstein hypothesis and no use of Derdziński's theorem are needed. Derdziński's theorem is the converse: Einstein together with W⁺ degenerate and nonzero implies that |W⁺|^{2/3}g is Kähler. The script docstring attributes the used direction to Derdziński and adds "on the nonzero-Weyl set". Both are unnecessary, since W⁺ = 0 is also a degenerate spectrum.

### 3.2 Both orientations

A complex structure inducing the opposite orientation forces W⁻ degenerate. With both blocks nondegenerate at p, and by continuity on a neighbourhood of p, neither orientation admits a conformally Kähler structure near p. This includes locally conformally Kähler structures in Vaisman's sense.

### 3.3 Global version via real-analyticity

For a trace-free symmetric 3×3 matrix W, the discriminant

Δ(W) = (tr W²)³ − 6(tr W³)²

is non-negative and vanishes exactly when the spectrum is degenerate. The check: λ(−1, −1, 2) gives 216λ⁶ − 6·36λ⁶ = 0.

Δ(W±) is real-analytic on the connected manifold, by Lemma F and the analytic ODE. By SU(2)-invariance it is an analytic function of t on (0, ∞). If Δ(W±)(t*) > 0 at one t*, then:
- W± is degenerate only on a discrete set of principal orbits (plus the bolt, where it is degenerate by the U(1) isotropy);
- no non-empty open subset is conformally Kähler, in either orientation.

The interior of an orbit hypersurface is empty, so a discrete set of orbits contains no open set.

### 3.4 Hermitian structures

The Riemannian Goldberg–Sachs theorem states that on an Einstein 4-manifold, an orthogonal integrable J inducing an orientation forces the corresponding W± to be degenerate. This is Apostolov–Gauduchon; it is a standard result, but the source is not among the supplied files. The same data then exclude Hermitian structures on any open set, in either orientation.

The underlying complex manifold O(−1) is of course complex. The statement concerns J orthogonal for this metric. Parallel J (Kähler) was already excluded exactly at the bolt, because neither (−41/16, −41/16, 41/8) nor (−91/16, −91/16, 91/8) equals (−4, 2, 2).

### 3.5 Isometry group

A non-trivial one-parameter isotropy at p acts non-trivially on at least one of Λ±, and an invariant symmetric operator there would be degenerate. With both blocks nondegenerate at p, isotropy is discrete.

‖A‖² + ‖B‖² is an isometry invariant that varies in t (≈ 233 at the bolt, ≈ 10.5 at t = 0.5). So isometry orbits have dimension at most 3. The identity component therefore has dimension at most 3 and contains left SU(2), so it equals SU(2).

This upgrades the note's "exactly SU(2) symmetry in the diagonal class" to a statement about the full isometry group. It also confirms that the metric lies in no U(2)-invariant or conformally Kähler family, such as Page–Pope, Calderbank–Singer or the biaxial Taub-bolt-AdS metrics.

### 3.6 A structural reason that B must split

tr B³ = 6(41/16)³ > 0 at the bolt, while tr B³ = −64 + 8 + 8 = −48 < 0 at the CH² limit. On a degenerate stretch, |tr W³| = ((tr W²)³/6)^{1/2}. So tr B³ cannot change sign along a degenerate path unless B vanishes there.

Hence B is nondegenerate somewhere, or B has a zero. The bolt values are exact and the CH² limit is rigorous from the block convergence, so this reduces B-nondegeneracy to B ≢ 0 along the orbit. There is no analogous argument for A, which tends to 0.

## 4. What an interval-rigorous theorem consists of

**Proposed statement.** For every d ∈ [0.28697953, 0.28701987] (hence for d₀), the bolt Einstein metric with b = 4/5 has Δ(W⁺) > 0 and Δ(W⁻) > 0 on the orbit t = 1/2. Consequently Theorem E's metric is not conformally Kähler or Hermitian on any open set, in either orientation, and its isometry identity component is SU(2).

**Ingredients.**

1. **Invariant-frame formula.** Right translations by the quaternion units are isometries of the diagonal metric. They flip the signs of two of the three σ_i. Together with left invariance, they kill every curvature component with an odd number of indices in any pair {j, k}.

   Consequently, in the frame e⁰ = dt, e^i = a_iσ_i, the curvature operator splits into the three 2×2 blocks {e^{0i}, e^{jk}}. W± are diagonal in the basis (e^{0i} ± e^{jk})/√2, with entries

   W±_i = ½(K_{0i} + K_{jk}) ± R_{0ijk} − s/12.

   Their explicit form in (a_i, y_i), with y′ replaced by the field, follows by symbolic computation from the structure equations. It can use the same cancellation-free exponentials as the CAPD field.

   - The JSON matrices are non-diagonal only because the Cholesky frame at the Euler angles ANG is rotated relative to the σ-frame. Their eigenvalues should coincide with these six diagonal entries to about 10⁻¹². That coincidence links the JAX computation to the formula.
   - The degenerate pairs are slots {1, 2} at the bolt for both blocks, and slots {2, 3} at infinity for B. The simple eigenvalue −4 belongs to fibre slot 1.

2. **State enclosures.** CAPD boxes at t = 1/2 are needed for all 40 d-subintervals, either as checkpoints of `ach_wazewski_run.py` or by rerunning to 0.5. Because d₀ is not located, the certificate must hold on the union of boxes; the existing tiling provides exactly that.

3. **Interval evaluation.** Six signed differences W±_i − W±_j are evaluated on each box. The expected margins are 3.9 × 10⁻³ for the smallest A-gap and 0.97 for B. Box widths at t = 0.5 should be well below 10⁻⁵, given point-box widths ≤ 3.3 × 10⁻⁶ at t = 2.7 and d-sensitivity growing toward T. t = 1 (A-gap 6.9 × 10⁻³) is an equally good choice.

4. **Written lemmas.**
   - Kähler W⁺ spectrum together with conformal invariance of the multiplicities.
   - Analyticity of Δ(W±) in t, discreteness of its zeros, and the resulting statement on open sets.
   - Riemannian Goldberg–Sachs for the Hermitian statement, with its source located.
   - The isotropy argument for the isometry group, using |W|² non-constant, which the same boxes give rigorously.

5. **Optional cross-check.** Integrating 3‖A‖² − ‖B‖² + 24 against a₁a₂a₃ over the enclosed orbit, with the tail bounded by the block rate, and comparing with ν(S³_ρ) obtained from BH Thm 8.1 at ρ ∈ [2.1901, 2.1925]. This would independently test ρ_∞ and the chirality assignment B = W⁺.

## 5. Textual inconsistencies in the package

- **Double use of C.** In note §4, C denotes both a₃/t and the constraint.
- **"Seven components."** The CAPD field has six variables; the seventh component in the field check is unexplained.
- **Stale scope paragraph.** Note §6 "Scope" and theorem_package §6.2 both list conformal Kählerness and Hermiticity as undecided. Once the certificate of §4 exists, both are decided negatively for every open set. Until then, the off-bolt JSON is numerical support for that conclusion.
- **Derdziński attribution.** The script docstring attributes the "conformally Kähler ⇒ degenerate" direction to Derdziński; as explained in §3.1, it is elementary.
- **Unmapped chirality.** The statement "the chiral ordering is still unmapped" is superseded by the data: the 41-block at the bolt is the block that becomes the asymptotic Kähler W⁺ (B), and the 91-block is W⁻ (A).