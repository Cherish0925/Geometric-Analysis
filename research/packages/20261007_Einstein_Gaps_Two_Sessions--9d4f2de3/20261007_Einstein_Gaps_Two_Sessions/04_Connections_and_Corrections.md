# Proof connections, corrections, and questions

This file connects the two Session catalogues. The mathematical synthesis
states the common setting; the catalogues retain the individual results and
their proof locations. Original source texts are unchanged.

## The common question and the distinct outputs

The normalized infimum \(\alpha(M)=\inf_g\mathcal E(g)\) concerns all
admissible metrics on a closed manifold. A field-alignment estimate for
\(\kappa_\beta\), an infimum over marked cells, and an exact Einstein
filling with specified infinity answer different questions. Their
relationships require explicit transfer arguments.

```text
Inherited actual-field theory
  N1, finite-parameter estimates, I40/I41, finite-density O10
  ├─ A02 L′: density-free estimate in the stated T+/A < 3/4 region
  │   └─ Corollary K for the specified general-type blow-up families
  ├─ linear lower order on the supplied balanced families
  │   └─ A01 two-parameter lower law (new organization/application)
  └─ same-metric, all-sign monopole identities
      └─ A02 Nijenhuis/Weyl saving formula
          ├─ integrable-family tariff under the stated supplier
          ├─ exact exceptional-period exclusions under extra hypotheses
          └─ missing: a sharp global constraint on actual saving

Geometric constructions and exact boundary data
  classical Burns/handle recovery
  ├─ A02 F: general-background first-order insertion response
  ├─ A01/A02 certified strict cheap CH-ended blow-up cell
  │   ├─ selected-cover closed construction: limsup alpha/h < 4
  │   └─ A01 ramified KE transfer + two-parameter upper law
  └─ A01 general exact-CH-ended conformal selection
      └─ equivalence of the specified local infima, not their values

Independent exact-existence branch
  analytic bolt + validated Einstein flow + asymptotic block
  └─ A02 E: complete O(-1) Einstein filling, nonstandard Rossi infinity
      └─ not a zero-cost standard-CH-boundary filling

Boundary, variation, and degeneration tools
  chiral flux, joint duals, AK boundary terms, diagonal calibration
  └─ estimates under specified collar/field/regularity assumptions
      └─ missing: those inputs for arbitrary genuine near-minimizers,
         or a direct global estimate that avoids needing them
```

The final two arrows are mathematical problems, not consequences of drawing
the tree. A complete bubble decomposition is one possible method, not a
mandatory prerequisite. For O11 the total error must be \(o(Q)\), not merely
\(o(V)\).

## Shared results and source ownership

| Result | Source chain | Count and interpretation |
| --- | --- | --- |
| Strict sub-four upper construction | A02 perpendicular cell formulation and checks; A01 analytic admissibility, interval certificate and global placement; later common theorem package | One joint construction, not two breakthroughs; later tighter digits refine its certificate |
| General CH-ended conformal selection | A01 Step 22, used by A02's relative-volume and truncation statements | One A01 analytical result reused in the joint theory |
| Rossi Einstein filling | A02 analytic/validated construction; A01 bolt-spectrum diagnostics; A02 off-bolt interval spectrum | One existence theorem with separate geometric diagnostics |
| Nijenhuis/Weyl identities | A02 Steps 38–40 and detailed returned derivations; cited by later A01 cap work | One actual-field mechanism, not a new A01 proof each time it is cited |
| Ramified KE transfer | A01 Step 31, using inherited supplier/coercivity and the common cheap cell | A genuine enlargement of the construction family; independent of unfinished near-divisor cap matching |
| Pure-handle sharp cost | Inherited all-metric theorem, localized in the Sessions | New local use of an existing sharp result, not a second proof of a new global coefficient |
| Ordinary monopole convex budget | Classical bounds and recovery applied to the ordinary family | Not a solution of the complete BF-budget problem on different connected-sum families |

The 4 October copies under the Skill's supplements preserve Session results;
their new storage location does not change attribution or date of origin.

## Corrections that change what may be concluded

### 1. The coefficient 4 is no longer the right universal target

The old upper bound \(4h/(1+h)\) being below \(4h\) at finite \(h\) was
not a strict asymptotic improvement. The current construction gives
\(\limsup\alpha/h<4\) on its selected families. Therefore a purported
all-metric lower bound \(P\ge8\pi^2Q-o(Q)\) on those same families would
contradict the construction. This does not determine their optimal
coefficient or contradict a coefficient-4 result in another family.

### 2. Alignment and direct Einstein defect cannot be interchanged

L′ and K concern \(\kappa_\beta\), including gauge/Weyl alignment. A
positive lower bound for that quantity is compatible with a zero direct
Einstein infimum in a different regime. Conversely, ruling out exact
Einstein metrics does not prove a uniformly positive infimum.

### 3. Local cost and global optimum are not automatically equal

A controlled collar cost, an exact diagonal calibration, or a positive
pure-handle tariff does not prove that arbitrary mixed near-minimizers
decompose into independently chargeable pieces. Boundary contributions,
shared field constraints, volume, and Weyl redistribution may interact.
The standard-CR truncation theorem requires its specified ACH control;
selection arguments preserve an available regular competitor family but
do not create one for free.

### 4. The completed KE transfer is not the unfinished cap transfer

A01 Step 31 uses a fixed compact region away from the divisor and a fixed
buffer. Step 35's near-divisor Theorem T still needs uniform lifted charts,
potential and coefficient control; Proposition P still needs the specific
Heisenberg lattice and central-index calculation. The earlier comparison of
infima prescribing the same *whole* collar was withdrawn. The valid
replacement transfers a given competitor with an extra buffer. Neither
limitation removes the completed away-from-divisor construction.

### 5. The latest actual-field scope is narrower than some summaries suggest

The affine exhaustion in A02 Step 40 concerns constant affine combinations,
discarding signed terms, and the displayed sharp Weyl estimate. It does not
show that every use of Seiberg–Witten identities is exhausted. The Taubes
argument applies to the stated pure-blow-up/basic-class setting and excludes
an exact zero-period common mode, not every small-period limiting sequence.
The AK profile retains its period factor; a Lorentzian reverse
Cauchy–Schwarz step requires the extra \(H_L\) condition.

The same-field identities may retain \(Q=k+4\ell\), but the actual all-sign
solutions and higher-type/holonomy input for handles must be supplied. A
later calculation restricted to \(\ell=0\) does not itself close the
original mixed O11.

### 6. Step 44 contains a valid pocket inequality and an uncompleted comparison

The original [Step 44 note](sources/Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md)
and [its returned mathematical review](sources/Sessions/S1003A02/trace/ttcs/results/step44_ttcs01_sub1_verifier.md)
are both included.

At \(Q=0\), the exact relation
\[
 -P=\frac{R_N}{2}-\mathcal B,\qquad\mathcal B\ge0,
\]
does not imply \(2P\le R_N\). Nearby non-Einstein Kähler metrics also
explain why Nijenhuis rotation cannot generally bound every Einstein
departure from below: the canonical integrable direction has
\(R_N=0\), while \(P\) need not vanish. The possible one-sided estimate
\(R_N\le CP\) requires its own proof.

The displayed linearized SW estimate uses the derivative energy twice;
splitting that energy may yield a weaker valid coercivity estimate, but not
the displayed constants. Standard and doubled SW spinor normalizations
must be reconciled. An \(L^2\) gap alone is not the supplied proof of the
claimed quotient-independent Hölder inverse and nonlinear neighborhood.
Even a repaired theorem on a fixed-topology CH host would still require
field selection and localization before application to surgery bulk.

Independently, the two-region almost-Kähler calculation yields
\[
 C_+\ge\frac{\ell_{AK}^2}{128\pi^2V}
 \left[3\theta^2-2\theta+1+
 \frac{\varphi}{1-\varphi}(1-\theta)_+^2\right]
 \ge\frac{\ell_{AK}^2}{128\pi^2V}\frac2{3-2\varphi}.
\]
Here \(\ell_{AK}=8\pi K_\omega\cdot[\omega]>0\),
\(\theta=\int|\nabla\omega|^2/\ell_{AK}\),
\(\varphi=\operatorname{Vol}\{s^*\ge0\}/V<1\), and
\(C_+=(S/24+2\int|W^+|^2)/(4\pi^2)\).
This prices a volume fraction, not a uniform charge per exceptional class.
Connecting its form to the canonical actual branch remains separate.

### 7. Computations retain their actual mathematical role

The fixed-profile Arb enclosure and the validated Einstein-flow records are
proof components with specified analytic prerequisites. Floating optimizer
values, finite Ritz spectra and sampled positivity are exploratory results.
The smaller floating cell value near \(0.995178\) is not the certified
value used in the closed theorem. A01 Step 38's training improvement failed
its independent sample; its incomplete refined output is not a result.

The three Lean files verify their stated algebraic identities, not the
whole geometric construction. Earlier incorrect bolt spectra, the pilot
Einstein field, the scale-free AK evaluation and the hardcoded zero
numerical residual are retained only with their explicit corrections.

## Seven questions for the next mathematical discussion

1. **L′ and K.** Does the full proof establish the stated metric quantifiers
   and one positive constant for every finite \(\beta\ge2\)? Check the
   supplier, class-square hypothesis, parameter split and conformal
   transfer. What is the largest range actually proved?

2. **Strict sub-four construction.** Do analytic admissibility, interval
   integration, collar smoothing, site count, actual supply and
   normalization together give the claimed closed-manifold bound? Which
   selected ball-quotient and ramified KE sequences are covered? Which
   geometric interaction supplies the fixed saving?

3. **General-background response.** Is Theorem F's curvature contraction
   and \(O(x^{6/5})\) remainder justified for each fixed smooth background?
   Which further information, if any, controls the smaller kernel-direction
   term without confusing an upper construction with a lower bound?

4. **Exact Einstein filling.** Do the bolt argument, constraint propagation,
   validated transport, isolating block and asymptotic estimates establish
   the stated complete filling and non-conformal-Kähler property? Compare
   exact topology and CR infinity with the classical existence literature.

5. **Sharp global lower information.** Can the actual Nijenhuis/Weyl saving
   identity constrain the amount of saving on all competing metrics while
   permitting the construction in question 2? What precise implication
   supplies local field/period/collar inputs, or avoids needing them?
   Distinguish pure blow-ups from the original mixed families.

6. **Latest perturbative and pocket claims.** Which one-sided statements
   survive the Step 44 corrections? Separate fixed-host, cover-uniform,
   nonlinear and changed-topology assertions. Does the valid pocket
   inequality lead to additional information once its actual period and
   field hypotheses are retained?

7. **Contribution and next decisive step.** Which results are classical
   applications, which add a new quantitative mechanism or actual
   construction, and which remain conditional? Identify a concrete missing
   implication whose proof or counterexample would change unrestricted O10
   or the true O11 optimum, without presupposing a particular method.

## How the archive supports these questions

The two full note volumes retain the chronological derivations; source
files retain their original layout. Mathematical TTCS returns contain
proofs and corrections that are sometimes longer than the final note,
especially for L′, F, the actual-field identities and Step 44. They are
included in full, not replaced by their integrator summaries.

The inherited manuscript and sources preserve the earlier month's work.
The [literature index](LITERATURE_INDEX.md) supplies the directly cited
local paper objects. The [source index](SOURCE_INDEX.tsv) locates every
captured source. These are aids to reading and reproducing the arguments;
file completeness is not a substitute for a mathematical proof.
