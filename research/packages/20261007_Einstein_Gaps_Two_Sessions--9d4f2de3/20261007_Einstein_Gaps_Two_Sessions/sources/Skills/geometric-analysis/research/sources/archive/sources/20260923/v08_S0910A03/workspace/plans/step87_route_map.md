# Step 87 route map: after the resolvent obstruction

> **Superseded by Step 88** for nonreflection and current route scope. See
> `workspace/plans/step88_route_map.md` and
> `workspace/notes/step88_reflection_free_minimal_separator.md`.

## Established results

### Exact OT connectors: COMPLETELY BLOCKED
Step 85 Bochner comparison: on reflected exact OT Einstein connectors,
sup e ≤ max{6, exit e}. Center identity gives ⟨e(0,·)⟩ ≥ 12. Contradiction.

### Forced OT connectors: BLOCKED AT δ < 0.246
Step 87 resolvent comparison: on complete extensions of reflected free-OT
approximate Einstein connectors with cusp-type exits,
sup e ≤ B(δ) = [4δ/√(3+δ) + √(2(3+δ)+20δ²/(3+δ))]²
Center floor: ⟨e(0,·)⟩ ≥ 12-8δ. Threshold δ* ≈ 0.24625.

### Warped products k ≥ 0: BLOCKED AT δ ≥ 3/2
A02 waist barrier (#614, verified by A01 #617): pointwise, cannot be amortized.

### Volume-convergent orbifold + ALE Sambusetti route: INACCESSIBLE IN THAT CLASS
A02 Chern-Weil neutrality + BCG (#625; scope corrected by #633) obstructs the
specific volume-convergent orbifold-resolution construction. It is not a theorem
about every near-pinched metric or every possible no-Einstein mechanism.

## Remaining constructions for negative-branch refutation

1. **Non-OT connectors on graph manifolds.** The OT reduction requires commuting
   Killing fields and free action. A general Riemannian metric on a graph manifold
   need not have any continuous symmetry. Could the obstruction be extended by
   an averaging or symmetrization argument? This would require showing that a
   hypothetical near-Einstein metric on a graph manifold has approximate T²-invariant
   structure on most of the collar.

2. **Non-reflected connectors (superseded).** Step 88 proves that on a complete
   OT quotient cylinder with two exact outward-expanding ends, a primitive
   weighted-length minimizer lifts to a minimal invariant $T^3$ and restores the
   same floor $12-8\delta$. Nonreflection alone is therefore not an escape in that
   class. Connection twist, failure of torus symmetry, or different end topology
   remain genuinely different mechanisms.

3. **Approximate twist.** The twist vanishing theorem (Step 79) applies only to
   exact reflected Einstein metrics with commuting Killing fields. Under small
   Ricci defect, the twist scalars c_X, c_Y satisfy a perturbed equation that
   does not force them to zero. Twist adds O(c²) terms to the orbit energy;
   its effect on the resolvent comparison is unclear.

4. **N#N S³ necks.** The connected-sum interface is S³, not T³. There is no
   free T² action on S³. The BCG threshold gives δ ≳ 3/(4χ), so
   the defect would need to be O(1/χ) for large χ. The construction problem
   is fundamentally different: the neck must be a near-Einstein metric on
   S³ × [0,R] interpolating between two hyperbolic pieces.

## Positive branch

Unresolved and independent. A01 is working on the Ozuch desingularization
coefficient for mixed-chirality #₃(S²×S²), but the AA/BB sector divergence
(A01 #628) means the full coefficient needs the ALE source structure.
A02's triple disjointness shows no cross-branch bypass exists.

## Higher dimensions

No known no-Einstein manifolds in dimension ≥ 5 (dated evidence, not a proof
of nonexistence). The four-dimensional tools (Chern-Weil, Seiberg-Witten)
do not directly transfer. This is a separate and largely unexplored regime.

## Evidence files

- `workspace/notes/step87_resolvent_obstruction_theorem.md` — main theorem
- `workspace/data/step87_resolvent_corrected.json` — all computations
- `workspace/scripts/step87_resolvent_corrected.py` — corrected computation
- `trace/ttcs/results/step87_ttcs01_verifier1_integration.md` — TTCS verification
