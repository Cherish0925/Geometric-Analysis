# Route assessment after Step 9

## Advances (retained after sign correction)

1. **General normal-cover transport lemma** (fully proved, no error): For any normal Riemannian cover with Ric ≥ -(n-1)Kg and buffer domain B_{3r}(p̂) ⊂ Û:
   fint_{B_r(p̂)} π*φ ≤ C(n,K,r) · fint_{B_r(p)} φ,   C = V_K(3r)/V_K(r).
   The sheet count cancels entirely. No group-structure hypothesis needed. This removes the "deck-counting estimate" from the list of needed hypotheses, subsumes all model-specific proofs in step8_model_deck_transport.md, and makes the collapse-unwrapping route depend ONLY on noncollapse of the cover (not on transport).

2. **Corrected nil³ orbit-volume equation**: v'' = (3-μ)v, where μ = a₃²/(2a₁²a₂²). This is WEAKER than the original claim v'' = (3+μ)v but still excludes nil³ collapse on circle bases via two mechanisms:
   - Max principle: μ ≤ 2/3 on periodic solutions → v'' ≥ (8/3)v > 0 → integral contradiction
   - Monotonicity: (vf₃)' = (1+μ)v > 0 contradicts periodicity of vf₃

3. **Cover-noncollapsed exclusion theorem** (from §1): If collapsed regions have noncollapsed normal covers at fixed scale, the transport lemma + Derdziński/projector chain gives a contradiction for LeBrun near-boundary sequences. This is independent of the orbit-volume sign error.

## Retracted claims

- v'' ≥ 3v for all nil³ (WRONG: correct is v'' = (3-μ)v, can be negative for μ > 3)
- All regular collapse excluded (WRONG: interval-base nil³ cusp exists — CH2 model)
- Fixed-topology contradiction proved (WRONG: cusp neighborhoods are not excluded)

## Current four-dimensional negative-branch picture

| Collapse regime | Status |
|---|---|
| Noncollapsed (Vol(B₁) ≥ v) | Excluded: Step 8 volume-proportion theorem |
| Noncollapsed cover at fixed scale | Excluded: transport lemma + Derdziński (Step 9 §1) |
| Regular abelian collapse (S¹,T²,T³) | Excluded: Lott orbit-volume (S0910A03) |
| Regular nil³ on circle base | Excluded: corrected orbit-volume + max principle |
| Nil³ cusp near singular fibers | NOT excluded: CH2 model exists |
| Curvature blowup / singular strata | NOT excluded |
| General Ric-bounded collapse (|Rm| unbounded) | Structural gap: CFG needs |Rm| bounded |

## Key remaining difficulties

1. **Ric-bounded vs Rm-bounded collapse.** CFG N-structure theorem requires bounded SECTIONAL curvature, not just bounded Ricci. Under Ric ≈ -g, the Weyl curvature can be unbounded. This prevents automatic application of CFG to convert "collapsed" into "has N-structure" for general near-pinched metrics.

2. **Curvature concentration.** For the LeBrun families, ∫|Rm|² ~ A. Chebyshev gives bounded-curvature regions, but their volume fraction is not obviously close to 1. The curvature can concentrate on a positive-volume set where |W⁻| is large.

3. **Cusp neighborhoods.** The CH2 model shows that Ric = -g nil³ cusps exist on intervals. Near singular-fiber points in a CFG decomposition, the collapse can have this cusp structure. The orbit-volume equation does not exclude such neighborhoods.

4. **Positive branch.** S0910A02's Cheeger-Naber finiteness theorem (noncollapse + two-sided Ricci → finite diffeomorphism types) is a useful structural result but does not close P₄⁺. The uniform noncollapse hypothesis is the single remaining gap.

5. **Dimensions n ≥ 5.** No Seiberg-Witten structure, no W⁺/W⁻ decomposition, different mechanisms needed.

## Most promising next directions

A. **ε-regularity under Ric ≈ -g**: Investigate whether the Bianchi identity div W = d(Ric°) with |Ric°| ≤ δ gives enough control for L² Weyl ε-regularity. If ∫_{B₁}|W|² ≤ ε and |Ric| ≤ 2 imply |Rm| ≤ C on B_{1/2}, then the Chebyshev + orbit-volume argument would work for varying topology.

B. **Energy concentration structure**: For the LeBrun families, characterize where |W⁻|² concentrates. The CGB formula ∫|W⁻|² = ∫|W⁺|² + 32π²k constrains the total but not the distribution. If |W⁻| concentration is geometrically rigid (e.g., localized near curvature-blowup points), the regular region would have bounded |Rm| and the orbit-volume argument would apply.

C. **S0910A02's all-dimensional Cheeger-Naber structure**: The noncollapsed Einstein regular-set structure from CN Thm 1.4 works in all dimensions. If a near-pinching sequence can be shown to be noncollapsed (either directly or through the universal cover), this gives the most general framework.

D. **Positive branch via Pohozaev/Komar identity**: S0910A02's approximate-to-exact bridge using L∞ Ricci defect paired with smooth test tensors (no ∇Ric needed). This could convert near-Einstein to exact Einstein at orbifold limits.

## Files

- Transport lemma: `notes/step9_general_cover_transport.md` (VALID)
- Corrected orbit-volume: `scripts/step9_nil3_orbit_volume_corrected.py` (CORRECTED)
- Original orbit-volume (SIGN ERROR): `scripts/step9_nil3_orbit_volume.py` (RETRACTED)
- Regular collapse note: `notes/step9_regular_collapse_exclusion.md` (NEEDS CORRECTION)
- Transport verification: `scripts/step9_normal_cover_transport.py` (VALID)
