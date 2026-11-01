# TTCS Independent Branch Record

```json
{
  "step_id": 95,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step94_filler_screen_dichotomy.md",
    "Sessions/S1003A02/workspace/notes/step95_verified_transfer_lattice_thresholds.md",
    "Sessions/S1003A02/workspace/scripts/step95_filler_lattice_screen.py",
    "Sessions/S1003A02/workspace/data/step95/filler_lattice_screen_certificate.json",
    "Sessions/S1003A02/workspace/notes/step93_paired_A1_transfer_review.md"
  ]
}
```

## Task

Independently verify the mathematical substance of Step 95. Focus on (i) the exact supporting-plane identity and derivation of 9C_-+2C_++42k+12(3c2-c1^2)>=0; (ii) the k_b budget and its interpretation as a structural blind direction of smooth transfer; (iii) whether the finite canonical root search really justifies E6/E7/E8 non-embedding in any diagonal lattice, the A_r slot rule, and the classification of full-rank Kronheimer subsystems as sums of D-blocks; and (iv) the exact beta formula and D6/D7/mixed thresholds. Look hard for missing topological assumptions, overextension from bounded computation, or arithmetic errors. Distinguish what is a mathematical theorem from what remains merely a necessary arithmetic/lattice possibility. Return concrete corrections if needed.

## Output

# Verification memo: Step 95 (transfer algebra, the k_b budget, root embeddings, D-block thresholds)

## Summary

The algebra is correct throughout. The root search is a valid exhaustive argument, and the threshold numbers check exactly.

Three statements need correction:

- **The "blind direction" interpretation is stated too broadly.** It holds only when the number of retained bulk classes is at least the number of fillers.
- **The A_r slot rule and the full-rank D-block classification for all k need a structural argument.** The computation reaches only r ≤ 12; Borel–de Siebenthal supplies the general proof.
- **The wall A = 3k is excluded by a convention in the script, not by the transfer.**

## (i) Supporting-plane identity and the host inequality

**The identity.** Expanding F = 7x + T + 4√2 √(x(T−x)) gives

  9x + 3T − F = 2T + 2x − 4√2 √(x(T−x)) = 2(√(T−x) − √(2x))².

This is exact, with equality iff T = 3x.

**Where F comes from.** With P = 0 we have I₊ = 2π²(T₊ − x). Since s < 0, Minkowski's inequality gives ∫(s − √6|W⁺|)² ≤ 12π²(√(8x) + √(T₊ − x))². This matches the transferred right-hand side 72π²A + 12π²C₊.

**The chain.** The steps are 6A + C₊ ≤ F ≤ 9x + 3T₊ ≤ 9T₋^orb + 3T₊^orb, using x ≤ T₋ and that the coefficient 9 is positive. Expanding:

  9(4c₂ − A + 5k + C₋) + 3(A − k + C₊) − 6A − C₊ = 9C₋ + 2C₊ + 42k + 12(3c₂ − c₁²).

This is verified by hand. The host inputs T₊(M_k) = A − k and T₋(M_k) = 4c₂ − A + 5k are also correct.

**Inputs this rests on.** None is new in Step 95:

- Lemma 86.S decay hypotheses on the fillers.
- Step 93's all-b⁺ use of LeBrun 2001, Prop. 3.2. This matters for general-type hosts with b⁺ = 1.
- s < 0 for the Einstein bulk. This follows directly from ∫(s⁻)² ≥ 32π²A > 0.

**A scope point.** (94.1) is only the tangent envelope. The sharp finite-A condition is T₋^orb ≥ x_min(A, T₊^orb, C₊), the smaller root of F = 6A + C₊. This has been derived only for ball quotients with C₊ = 0. For general hosts, and whenever reversed fillers are present, only the weaker (94.1) is available.

## (ii) The k_b budget and what "blind" actually means

**The budget algebra is correct.**

- Kronheimer and Şuvaina fillers have finite π₁ and b₁ = b₃ = 0, so χ = 1 + b₂.
- By Lemma 94.L, reversed Kähler fillers must have b₂ = 0, so they are Wahl balls with |Γ| = n².
- Hence Σ_cx(χ − 1/|Γ|) = (k − k_b) + S_cx.
- Then −36[(k − k_b) + S_cx] − 8S_rev + 42k = 6k + 36k_b − 36S_cx − 8S_rev, which is (94.2).
- Lemma 94.L itself is sound. The restriction of c to N_j is null-homotopic because π₁(N_j) is finite and π₁(X) is torsion-free. The rational Mayer–Vietoris sequence along rational-homology-sphere links gives an isometric injection into ker c_* = ⊕ZE_i. Ball-quotient π₁ is torsion-free automatically.

**Correction: k_b > 0 is not automatically invisible.** Each filler costs strictly less than 1, and β ≥ k/18 > 0. The precise statement is:

> Any configuration with N_cx + N_rev ≤ k_b satisfies both (94.2) and (94.3) identically.

Configurations with more fillers than retained classes can still fail. Counterexample at k = 5: two D₂ blocks (four Eguchi–Hanson fillers) plus one unused coordinate.

- Here k_b = 1 and S_cx = 2.
- The budget is k/6 + k_b = 11/6 < 2, so this configuration is excluded.

More generally, m D₂ blocks with one bulk class require m ≤ 1.

**The Wahl sentence needs the same correction.** "Every Wahl channel lies in this blind direction" should read as follows:

- Wahl balls contribute nothing to k − k_b.
- Pure cx-Wahl configurations pass iff Σ(1 − n⁻²) ≤ 7k/6, which is automatic when there are at most k balls.
- Configurations with more balls than that are excluded by transfer.

So the genuine invisible sector is k_b ≥ (number of fillers), or more generally (94.2)/(94.3) with slack. Only that sector needs singular-point information such as η/Dedekind terms or local type-T analysis.

**General hosts.** k_b := b₂(V) − b₂(X) may be negative there, because filler classes can absorb host classes. So (94.2) has no direct analogue without Lemma 94.L.

## (iii) Root search: what is theorem and what is computation

**Canonicalization is valid.**

- Norm-2 vectors of I_k are exactly ±e_i ± e_j.
- Signed permutations act transitively on them, so fixing e₁ − e₂ is legitimate.
- Inner product −1 between two such roots forces exactly one shared coordinate. So in a connected BFS order each new root introduces at most one new coordinate.
- Relabeling unused coordinates and flipping their signs fixes all previously assigned roots.
- A rank-r connected system therefore lives in at most r + 1 coordinates, and searching I_{r+1} covers every I_k.
- The code's `candidate_roots` and `embedding_search` implement exactly this.

**E₆/E₇/E₈ non-embedding into any I_k is a theorem.**

- The E₆ search fails at node 6 in its BFS order.
- E₇ and E₈ use the same first six nodes, which form the E₆ subdiagram. This explains why the three counters are identical (15 DFS nodes, maximum 5 coordinates).
- An independent proof: roots of I_k form D_k, and by Dynkin's classification no subsystem of D_k is of type E.

**The A_r slot rule is computed only for 4 ≤ r ≤ 12.** The general statement, and the full-rank classification for all k, need a structural argument:

- Every root subsystem of a simply-laced system is closed.
- Iterating Borel–de Siebenthal on the extended D_k diagram (interior nodes have coefficient 2) shows that full-rank subsystems are ⊕D_{a_i} with Σa_i = k, a_i ≥ 2, D₂ = 2A₁, D₃ = A₃.
- This alone gives L4 and the full-absorption reduction for every k, with no computational bound.
- A quick independent check: a full-rank A_r ⊂ Z^r has index² equal to r + 1. This kills every r except r + 1 a perfect square (r = 3, 8, 15, …), and Borel–de Siebenthal handles the rest.

**Recommendation.** The note should cite this argument and present the search as corroboration. As written, "the conceptual classification now follows" leans on the bounded search.

**One more step that is needed and is true.** Each irreducible component equals a single Kronheimer filler, because ADE lattices are irreducible. The only exception is D₂, which is two Eguchi–Hanson fillers. Norm-2 vectors of the orthogonal sum ⊕L_j are exactly the union of the filler roots. So the cost of a block is well defined: D₃ = A₃ with |Γ| = 4, and D_a with binary dihedral |Γ| = 4(a − 2).

## (iv) β and the thresholds

**β is exact.** With A = 3k/(1 − y²):

- A/3 + k − x_min = 2k(1 + 5y)(1 − y)/[9(1 − y²)], so β = k(1 + 5y)/[18(1 + y)].
- The derivative is ∝ 4/(1 + y)² > 0, so β is strictly increasing.
- x_min is the correct root. Writing √(8x) + √(T₊ − x) = √(2A/27)·[2(4 − y) + (1 + 2y)] = √(6A) confirms it solves F = 6A.
- x_min lies on the increasing branch (x_min ≤ 8T₊/9) and satisfies x_min ≥ A/3 for y ≤ 1.
- The t-series matches Steps 93 and 94.

**Thresholds recomputed by hand.** All rows agree with the certificate.

| Block(s) | k | y_crit | A_crit | Smallest A ∈ 9Z |
|---|---|---|---|---|
| D₆ | 6 | 29/35 | 3675/64 | 63 |
| D₇ | 7 | 101/179 | 32041/1040 | 36 |
| D₃ ⊕ D₈ | 11 | 79/97 | 9409/96 | 99 |
| D₄ ⊕ D₇ | 11 | 437/443 | 196249/160 | 1233 |
| D₂ ⊕ D₁₀ | 12 | 125/131 | 51483/128 | 405 |

**Further checks.**

- A ∈ 9Z for ball quotients holds because c₁² = 9χ(O).
- The surplus values are correct.
- At k = 6 only D₆ survives: {2,4} costs 15/8, {3,3} costs 3/2, {2,2,2} costs 3, and all exceed 1.
- At k = 11, D₅ ⊕ D₆ (cost 89/48) and D₂ ⊕ D₉ (cost 55/28) both exceed 11/6. So exactly three rows survive.
- The per-k survivor counts sum to 16,049.
- The partition totals equal p(n) − p(n − 1); for example 6153 at k = 40.

**Correction on the wall.** `first_multiple_9_for_open_range` imposes A > 3k by convention. At A = 3k the transferred inequality allows equality, with x = 16A/27 and β = k/18. So rows flagged "already allowed at the wall limit" with 3k ∈ 9Z have A = 3k as an equality-case candidate:

- k = 18, A = 54;
- k = 21, A = 63;
- k = 24, A = 72;
- and so on.

These are governed by the open wall-rigidity problem of Step 94 §7, not excluded by transfer. The table's "smallest multiple of 9" for those rows should be read as "smallest off-wall value".

## Extension that comes for free

Adding cx Wahl balls, which change S_cx but not k_b, or reversed Wahl balls, which add (2/9)S_rev in (94.2), only increases cost. So the conclusions "some a_i ≥ 6" and "k ≥ 6" persist for full absorptions that also contain Wahl points. The exact A-thresholds need recomputation only when C₊ ≠ 0, because x_min changes.

## Status ledger

**Theorems, given the prior transfer lemmas:**

- (94.1) for all minimal general-type hosts.
- (94.2) and (94.3) over ball quotients.
- E-types never embed.
- Full absorption with Kronheimer fillers forces ⊕D_{a_i} with Σa_i = k (via Borel–de Siebenthal), some a_i ≥ 6, and k ≥ 6.
- At k = 6 only D₆, and it requires A ≥ 3675/64.
- The exact threshold formula and the tabulated thresholds.
- Automatic passage when k_b ≥ (number of fillers).

**Necessary-condition possibilities only.** All 16,049 surviving rows, the Wahl and unpaired-A_r channels, and the wall cases.

**Unresolved, with the substance each needs:**

- Whether the D_a prism-manifold link admits the rational-homology complement required by k_b = 0, with H₂(X) as the orthogonal complement of the absorbed lattice. This needs smooth embedding or obstruction data for the D_a plumbing in #a CP̄², for example d-invariant or rational-ball results for prism manifolds.
- The Şuvaina d ≥ 2 lattices.
- Existence of the negative Einstein bulk.