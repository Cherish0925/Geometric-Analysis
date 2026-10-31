# Route assessment after Step 49

> **Step 49 supersedes Step 47/48 route assessment for the product-quotient front.**
> The earlier route note treated product-quotient surfaces as potential stress tests or counterexample candidates. Step 49 reverses this: they are Einstein existence candidates.

## 1. Strategic reversal: product-quotient surfaces as existence evidence

The kernel-directed Eguchi–Hanson replacement at $A_1$ orbifold nodes corresponds to complex smoothing (the $(2,0)+(0,2)$ directions in the hyperkähler parameter space), not holomorphic resolution. This identifies the local near-Einstein gluing parameters with Q-Gorenstein deformation parameters.

If the canonical model $Z$ of a $p_g = q = 0$ product-quotient surface with only $A_1$ nodes admits a global Q-Gorenstein smoothing, then:
- ampleness of $K_Z$ persists to smooth fibers (openness of ampleness),
- Aubin–Yau gives a negative KE metric on the smooth fiber,
- Brieskorn simultaneous resolution gives diffeomorphism between the smooth fiber and the minimal resolution $S$.

Therefore $S$ carries an Einstein metric. This is **existence**, not obstruction.

The $b_+ = 1$ of all these resolutions rules out Ishida–LeBrun overlap ($m \ge 2$ blocks need $b_+ \ge 2$).

## 2. Status of the four main routes

### 2.1 Restricted negative IL theorem (four-dimensional)

Status: **Strong restricted architecture, unfinished analytic module.**

The restricted family-uniform negative gap theorem for the IL geography $(\#_{j=1}^m X_j)\# N$ with $m \in \{2,3\}$, $b_+(N) = 0$, $A > 0$, $q \ge 0$ has a coherent proof architecture based on:
- Mixed SW inequality + calibrated Weyl spectrum + Derdziński forbidden germ
- Selected-support cutoff flow with coefficient regularization
- Terminal $\Phi$-calibration and local compactness gap

The analytic flow module (transported-DeTurck/Yang existence, common-time estimates, $\varepsilon \to 0$ passage) is source-compatible but not self-contained. A03 Step 50 corrects the earlier invalid $b_\varepsilon$ start.

**Key point:** This route addresses manifolds with $b_+ \ge 2$, not the product-quotient surfaces. The two routes are complementary, not competing.

### 2.2 Product-quotient existence route (NEW in Step 49)

Status: **Mechanism identified, obstruction analysis complete, computation pending.**

For $K^2 = 2, 4$: $\chi(T_S) = 2K^2 - 10 < 0$, so $H^2(T_S) = 0$ is possible. Concrete computation needed for named families.
For $K^2 = 6$: $\chi(T_S) = 2 > 0$, sufficient condition fails, need alternative argument.
For $K^2 = 8$: no singularities, product KE metric descends, already Einstein.

**Immediate next work:** Compute $H^2(T_S)$ for a named $K^2 = 2$ family using equivariant cohomology on $H^0(2K_{C_1} \boxtimes K_{C_2})^G$.

### 2.3 Entropy/degree-map route

Status: **Target-dependent partial existence theorem.**

The degree-one comparison gives target-dependent Einstein existence when the Euler/degree ratio lies in the BBCG window. The $X\#X$ no-Einstein gap degenerates as $\sim 1/(4\chi(X))$. Not dimension-only.

### 2.4 High-dimensional routes

Status: **Speculative.** Farrell–Jones exotic smooth structures with near-pinched curvature; negative Einstein rigidity unknown. No current viable mechanism.

## 3. Positive branch

The positive product-quotient orbifold rows ($S^2 \times S^2$ quotients) need a different mechanism: the Fano/Tian–Yau theory for the anti-canonical direction. Mixed-chirality insertions give non-holomorphic deformations that fall outside the Q-Gorenstein framework. Ordinary monopole and entropy obstructions are ineffective for simply connected positive manifolds.

This remains the most poorly understood direction.

## 4. Priority ranking for next work

1. **Compute $H^2(T_S)$ for named $K^2 = 2$ product-quotient families** — most tractable, could establish first concrete Einstein existence via QG smoothing + Aubin–Yau.

2. **Complete restricted IL analytic module** — strongest existing route for the negative branch on $b_+ \ge 2$ manifolds.

3. **Positive branch: smooth types and Einstein existence/obstruction** — hardest, least developed.

4. **Entropy route: normalized margin for varying targets** — interesting mathematics but not dimension-only.

## 5. Relation to Yau 26

None of the current routes resolves the full proposition. The product-quotient existence route, if successful, would be a new family of Einstein existence results for manifolds with tight Ricci pinching—consistent with the positive answer to Yau 26 for the negative branch in dimension 4. But it does not constitute a proof because it covers only specific topologies, not all manifolds satisfying the pinching condition.

The restricted IL theorem, if completed, would be a restricted negative forcing theorem—also consistent with Yau 26 but not sufficient.

A complete proof or refutation requires:
- For proof: a dimension-only forcing mechanism applicable to all topologies.
- For refutation: a specific closed manifold with tight two-sided Ricci pinching and no Einstein metric of any sign.

Both remain distant from the current state.
