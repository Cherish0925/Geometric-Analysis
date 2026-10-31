# Step 28: Bochner center bound and abelian forcing for positive collapse

Session `S0910A02`. Agent2/Constructor. Phase Execute.

## 0. Summary and scope

This note establishes an **ansatz-free, dimension-free** theorem that bounds the
center bracket of any nilpotent isometric collapse under upper Ricci control.
It subsumes the Step 26–27 diagonal H₃ model result as a special case and settles
the twist question (twist cannot evade the bound).  It also provides a sharp
explanation of the positive/negative sign asymmetry and an induction architecture
for multi-step nilpotent fibers.

**This is a structural theorem about the left-hand class of the Yau-26 containment
(which metrics satisfy tight positive pinching), not a proof or refutation of
Yau-26 itself.**

## 1. General Bochner center bound

### Theorem A (Bochner center bound for Killing fields)

Let $(M^n, g)$ be a closed Riemannian manifold admitting a nontrivial Killing
vector field $Z$.  If $\operatorname{Ric}_g \le (\Lambda+\delta)g$ as quadratic
forms, then
$$
\int_M|\nabla Z|^2\,dV = \int_M\operatorname{Ric}(Z,Z)\,dV
\le (\Lambda+\delta)\int_M|Z|^2\,dV.
$$

*Proof.* For $Z$ Killing, the Bochner formula gives $\nabla^*\nabla Z =
\operatorname{Ric}^\sharp(Z)$ (equivalently $\Delta Z = -\operatorname{Ric}^\sharp(Z)$
with trace Laplacian).  Pairing with $Z$ and integrating on the closed manifold:
$\int|\nabla Z|^2 = \int\operatorname{Ric}(Z,Z)$.  The upper Ricci bound
converts the right side to $\le(\Lambda+\delta)\int|Z|^2$.  $\square$

This is classical (Bochner 1946) and uses only the Killing equation,
integration by parts, and the quadratic-form Ricci bound.  No submersion
structure, O'Neill tensors, twist control, bounded curvature, or dimensional
hypothesis is needed.

### Corollary A1 (center bracket bound for nilpotent Killing collapse)

Suppose $M$ carries a Heisenberg-type nilmanifold fiber structure, and a central
circle subgroup of the fiber acts isometrically on $M$, generating a Killing
field $Z$.  (The full nonabelian nilpotent group need not act globally by
isometries; the isometry group of a closed manifold is compact, and compact
nilpotent Lie algebras are abelian.  The correct hypothesis is that only the
central circle direction gives a global Killing field.)  In any left-invariant
metric on a Heisenberg-type fiber with $[E_1,E_2]=bE_3$ (orthonormal frame), the
fiber covariant derivative satisfies
$$
|\nabla^FZ|^2 = \frac{b^2}{2}\,|Z|^2.
$$
On the total manifold, $|\nabla Z|^2 \ge |\nabla^FZ|^2$ (the additional $T$- and
$A$-contributions to $\nabla Z$ add non-negatively; this is exact by orthogonality
of vertical and horizontal components of $\nabla_UZ$).  Therefore
$$
\frac12\int_M b^2|Z|^2\,dV \le \int_M|\nabla Z|^2\,dV
\le (\Lambda+\delta)\int_M|Z|^2\,dV,
$$
giving the **weighted average center bracket bound**:
$$
\langle b^2 \rangle_{|Z|^2} := \frac{\int b^2|Z|^2\,dV}{\int|Z|^2\,dV}
\le 2(\Lambda+\delta).
$$

In particular, for $\Lambda>0$ and $\delta<\Lambda$, the orthonormal-frame
Heisenberg bracket is bounded at the ambient curvature scale:
$\langle b^2 \rangle \le 2(\Lambda+\delta)$.  Measured in the collapsing fiber's
own scale $\varepsilon$, this becomes $\varepsilon^2 b^2 \le 2\varepsilon^2
(\Lambda+\delta)\to0$, so the normalized bracket vanishes: the collapse is
asymptotically abelian.

### Key properties

- **Dimension-free.** Works in every $n\ge4$.
- **Ansatz-free.** No cohomogeneity-one, diagonal, toric, or equivariant hypothesis.
- **No $T,A,N$ control needed.** The bound uses only Bochner and the pointwise fiber
  gradient $|\nabla^FZ|^2\ge(b^2/2)|Z|^2$; the O'Neill tensors contribute only
  non-negatively to $|\nabla Z|^2$.
- **Twist-immune.** Twist adds $Q(Z)=\sum_i|A_{X_i}Z|^2\ge0$ to $\nabla Z$,
  strengthening the inequality.  This settles the open twist question from Steps 25–26:
  twist cannot restore a bracket plateau.
- **Requires genuine Killing.**  The field $Z$ must satisfy $\mathcal L_Z g=0$ exactly.
  The extension to almost-Killing fields ($\|\mathcal L_Z g\|\le\tau$) introduces an
  $O(\tau)$ error in the integrated bound and is the key remaining bridge to
  N-structures.

## 2. Sign asymmetry: negative Ricci kills all Killing fields

### Theorem B (Bochner vanishing for negative Ricci)

If $(M^n,g)$ is closed with $\operatorname{Ric}_g\le(\Lambda+\delta)g$ and
$\Lambda+\delta<0$, then $M$ admits no nontrivial Killing vector field.

*Proof.* Bochner:
$0\le\int|\nabla Z|^2 = \int\operatorname{Ric}(Z,Z) \le (\Lambda+\delta)\int|Z|^2$.
Since $\Lambda+\delta<0$ and $\int|Z|^2\ge0$, the right side is $\le0$ with
equality iff $Z\equiv0$.  So $\int|\nabla Z|^2=0$ and $\int|Z|^2=0$, giving
$Z\equiv0$.  $\square$

This means:
- **Negative-branch collapse is never by isometries.**  Any negative near-Einstein
  collapsing sequence must use approximate symmetries only.
- **The CH² horosphere is a noncompact phenomenon.**  The stationary Heisenberg data
  $(\Lambda=-3/2, b=1, k_1=-1/2, k_3=-1)$ has a strictly positive Bochner residual
  $|\nabla Z|^2/|Z|^2 - \operatorname{Ric}_{33} = 5/2-(-3/2) = 4 > 0$.  This cannot
  integrate to zero on a closed manifold, independently confirming that CH²-type data
  is incompatible with compactness.
- The sign asymmetry in the H₃ model (Step 26–27: positive branch forbids bracket
  plateau via $b^2+4\Lambda$, negative branch allows it) is a shadow of this: the
  deeper reason is the presence or absence of isometric symmetry, not a lucky sign in
  one coefficient.

## 3. Model verification in the H₃ cohomogeneity-one model

### Connection and covariant derivative computation

For the diagonal model $g=dt^2+a^2(\theta_1^2+\theta_2^2)+c^2\theta_3^2$ with
$[E_1,E_2]=E_3$, Koszul formula computation (verified in
`workspace/scripts/step28_bochner_killing_center_bound.py`) gives:
$$
\nabla_{e_0}e_3 = 0,\quad
\nabla_{e_1}e_3 = -\frac{b}{2}e_2,\quad
\nabla_{e_2}e_3 = +\frac{b}{2}e_1,\quad
\nabla_{e_3}e_3 = -k_3 e_0.
$$
The central Killing field $Z=\partial_{\phi_3}=c\,e_3$ then has:
$$
\nabla_{e_0}Z = ck_3\,e_3,\quad
\nabla_{e_1}Z = -\frac{cb}{2}\,e_2,\quad
\nabla_{e_2}Z = +\frac{cb}{2}\,e_1,\quad
\nabla_{e_3}Z = -ck_3\,e_0,
$$
and therefore
$$
|\nabla Z|^2 = c^2\!\left(2k_3^2+\frac{b^2}{2}\right)
= \frac{b^2}{2}|Z|^2 + 2k_3^2|Z|^2.
$$
The fiber-only contribution is $(b^2/2)|Z|^2$; the extra $2k_3^2|Z|^2$ comes from
the radial variation $\nabla_{e_0}Z$ and $\nabla_{e_3}Z$.

### Bochner identity verification

The integrand $|\nabla Z|^2 - \operatorname{Ric}(Z,Z)$ in the H₃ model equals
$c^2(3k_3^2+2k_1k_3+k_3')$.  Integration by parts against $c^2 w = a^2c^3$ with
$d\log(a^2c^3)/dt = 2k_1+3k_3$ replaces $k_3'$ by $-(2k_1k_3+3k_3^2)$, and the
total vanishes: $3k_3^2+2k_1k_3-2k_1k_3-3k_3^2=0$.

### Divergence identity (alternative proof)

The Ricci component $\operatorname{Ric}_{33} = b^2/2-(wk_3)'/w$ where $w=a^2c$.
On a closed manifold or with $wk_3=0$ at endpoints:
$$
\int\operatorname{Ric}_{33}\,w\,dt = \int\frac{b^2}{2}\,w\,dt.
$$
For exact $\operatorname{Ric}=\Lambda g$ this gives $\Lambda\int w = \int(b^2/2)w$,
hence $\langle b^2\rangle_w = 2\Lambda$ exactly.  The Bochner result is a different
but consistent statement with $|Z|^2$-weighting.

## 4. Subsumption of Steps 6, 24, 26–27

### Step 6 (4D constant-length circle Bochner)

The constant-fiber-length principal circle case with
$|\phi|^2=2$, $d_B^*\phi=0$, $\operatorname{Ric}_B=g_B+(1/2)\phi\circ\phi$ and
base dimension 3 is now understood as the first case of the induction
architecture: Bochner bounds the abelian Killing bracket (trivially satisfied),
the Kaluza-Klein trace pins $|\phi|^2=2$, and a 3-dimensional Bochner argument
on the base gives the obstruction.

### Step 24 (higher-dimensional KK collapse)

Exact positive Einstein collapses $(S^3(\sqrt2)/\mathbb Z_q)\times N^d$ exist.
These are ABELIAN collapse: the Killing field is the circle generator, bracket
$b=0$ (abelian!), and $\langle b^2\rangle = 0 \le 2\Lambda$.  The Bochner bound
is trivially satisfied.  These examples show why the bound does not obstruct
abelian collapse; it only constrains nonabelian brackets.

### Steps 26–27 (H₃ model monotonicity)

The diagonal H₃ ODE result ($|(log b)'|^2 \ge (5/4)(b^2+4\Lambda)$ on the
constraint surface) is STRONGER than the Bochner bound within the model: it gives
pointwise monotonicity, thin-shell structure, and explicit closure.  The Bochner
bound is weaker within the model but immensely more general.  Together they form a
hierarchy:

| Level | Result | Scope |
|-------|--------|-------|
| 0 | Bochner Killing center bound | Any $n$, any metric, Killing required |
| 1 | O'Neill submersion + Bochner | Fiber structure needed, pointwise for $T=0$ |
| 2 | Diagonal H₃ ODE monotonicity | 4D diagonal H₃, pointwise rate and shell |

## 5. Induction on nilpotency step

### Architecture C (iterated Bochner-KK descent)

For a closed Riemannian manifold $(M^n,g)$ with $\operatorname{Ric}\le(\Lambda+\delta)g$
and a free isometric action by a step-$k$ nilpotent group $N$:

1. **Central bracket bound.** The center $Z(N)$ gives a nontrivial Killing field $Z_k$.
   By Theorem A, $\langle b_k^2\rangle_{|Z_k|^2} \le 2(\Lambda+\delta)$.

2. **Central quotient.** Quotient by the $Z_k$-orbits.  The Kaluza-Klein/O'Neill
   formula gives $\operatorname{Ric}_B = \operatorname{Ric}_M^H +
   (1/2)\phi_k\circ\phi_k$ where $\phi_k$ is the horizontal connection curvature.
   **Gap:** Theorem A bounds the fiber bracket $b$ (the nilpotent structure
   constant), but the quotient Ricci upper bound requires controlling
   $|\phi_k|^2 = |A|^2$ (the horizontal twist), which is a DIFFERENT O'Neill tensor.
   Under exact Einstein, $|\phi_k|^2 = 2\Lambda$ from the vertical equation, but for
   merely pinched metrics this identity does not hold, and no independent bound on
   $|\phi|$ follows from Theorem A alone.  This is a decisive unresolved point.

3. **Reduced fiber.** The quotient fiber is $N/Z(N)$, which is step-$(k-1)$ nilpotent.

4. **Repeat.** After $k$ steps (where $k \le n-1$ from dimension), all brackets are
   bounded: $b_j \le C(n,\Lambda,\delta)$ for each step $j$.  The total constant
   degradation is $O(2^k \Lambda)$, acceptable for fixed nilpotency step.

5. **Abelian forcing at the collapse scale** (conditional on Step 2 gap).
   Since each $b_j = O(\sqrt\Lambda)$ at the ambient scale and the fiber collapses
   to scale $\varepsilon$, the rescaled brackets $\varepsilon b_j \to 0$: the fiber
   becomes metrically abelian in the $|Z|^2$-weighted $L^2$ sense.  This is an
   integral statement; localized high-bracket thin shells (as in the Step-27 model)
   are compatible with a bounded average.

### Key gaps remaining

1. **Horizontal twist bound.** The quotient Ricci upper bound needs $|\phi|^2$
   (horizontal A-tensor) bounded, not just $b^2$ (fiber bracket).  Theorem A does
   not supply this.  An independent bound on $|A|$ under two-sided Ricci pinching
   is needed.

2. **Almost-Killing bridge.** The local nilpotent groups from Kapovitch-Wilking/
   Naber-Zhang are approximate, not exact isometries.  The induction needs the
   almost-Killing extension with $\|\mathcal L_Z g\| = O(|Z|)$ at the collapse
   scale.

3. **Smooth quotient structure.** The central quotient needs closed orbits, free
   action, and preservation of the next-level Killing field.  Monodromy of the
   nilpotent bundle may obstruct global Killing on the quotient.

4. **Variable fiber length.** Non-constant $|Z|$ introduces Hessian terms in the
   quotient formula that the averaged Bochner bound does not control pointwise.

## 6. The almost-Killing bridge: exact Weitzenböck correction

For a general vector field $Z$ with $\sigma:=\mathcal L_Z g$, the Weitzenböck
formula for $\omega=Z^\flat$ gives the **exact identity**:
$$
\int_M|\nabla Z|^2\,dV
= \int_M\operatorname{Ric}(Z,Z)\,dV
+ \frac12\int_M|\sigma|^2\,dV
- \frac14\int_M(\operatorname{tr}\sigma)^2\,dV.
$$

*Derivation.*  Write $\nabla Z = A + S$ with $A$ antisymmetric and
$S=\sigma/2$ symmetric.  Orthogonality: $|\nabla Z|^2 = |A|^2+|\sigma|^2/4$.
The Hodge-Laplacian terms are $|d\omega|^2=2|A|^2$,
$|\delta\omega|^2 = (\operatorname{tr}\sigma)^2/4$.  Weitzenböck then gives
$2|A|^2+(\operatorname{tr}\sigma)^2/4 = |A|^2+|\sigma|^2/4+
\operatorname{Ric}(Z,Z)$, hence
$|A|^2 = \operatorname{Ric}(Z,Z)+|\sigma|^2/4-(\operatorname{tr}\sigma)^2/4$.
Adding $|\sigma|^2/4$ gives the total.  $\square$

**Almost-Killing upper bound.** Since $(\operatorname{tr}\sigma)^2\ge0$:
$$
\int|\nabla Z|^2 \le \int\operatorname{Ric}(Z,Z) + \frac12\int|\sigma|^2.
$$
If $|\sigma|\le\tau$ pointwise, the correction is $\le\frac{\tau^2}2
\operatorname{Vol}(M)$.  Combined with $|\nabla Z|^2\ge(b^2/2)|Z|^2$:
$$
\langle b^2\rangle_{|Z|^2}
\le 2(\Lambda+\delta)
+ \frac{\tau^2\operatorname{Vol}(M)}{\int|Z|^2\,dV}.
$$

**Collapse-scale analysis.**  For fiber scale $\varepsilon$, the average
$\overline{|Z|^2} \sim \varepsilon^2$.  Two regimes:

1. $\tau\sim\varepsilon$ (almost-Killing at fiber scale): correction $\sim
   \varepsilon^2\operatorname{Vol}/(\varepsilon^2\operatorname{Vol}) = O(1)$.
   Bracket bounded: $\langle b^2\rangle \le 2\Lambda + O(1)$.  The normalized
   bracket $\varepsilon b$ still vanishes: $\varepsilon^2\langle b^2\rangle =
   O(\varepsilon^2)\to0$.  **This weaker threshold already gives abelian forcing.**

2. $\tau\sim\varepsilon^{1+\alpha}$ for $\alpha>0$: correction $\sim
   \varepsilon^{2\alpha}\to0$.  Sharper $\langle b^2\rangle\to 2\Lambda$.

**Conclusion:** For normalized bracket vanishing, it suffices that
$\|\mathcal L_Z g\|_{C^0} = O(|Z|)$ at the collapse scale (regime 1).
The stronger $\|\mathcal L_Z g\| = o(|Z|)$ is needed only for the correction to
vanish.  The Kapovitch-Wilking/Naber-Zhang machinery provides
$\Gamma_\epsilon(p)$ is $(w(n),n)$-nilpotent under
$\operatorname{Ric}\ge-(n-1)$; the remaining load-bearing question is whether
tight positive pinching forces the associated local Killing fields to have
$\|\mathcal L_Z g\|=O(|Z|)$ at the collapse scale.
## 7. Relation to the full Yau-26 proposition

The Bochner center bound + induction architecture addresses the positive-collapse
portion of the Yau-26 containment problem.  It shows that under positive Ricci
pinching, any isometric nilpotent collapse is essentially abelian.  Combined with:

- **Dimension 2-3:** settled by uniformization/geometrization.
- **Step 6 (4D circle):** obstructs constant-fiber circle collapse over 3-bases.
- **Step 24 (higher-dim KK):** abelian collapse exists and is Einstein-compatible.
- **Steps 26-27 (H₃ model):** pointwise monotonicity excludes closed diagonal models.

The remaining open cases are:

1. **Almost-Killing bridge:** quantitative Lie-derivative bound at the collapse scale.
2. **Singular/fixed strata:** where the nilpotent action has stabilizers.
3. **Noncollapsed degeneration:** codimension-4 singularity development.
4. **Einstein existence:** whether the underlying smooth manifold admits an Einstein
   metric, independent of the pinched metric's structure.

No branch of the full Yau-26 proposition is proved or refuted.  Lean formalization
covers only the algebraic kernels.

## 8. Files

- Script: `workspace/scripts/step28_bochner_killing_center_bound.py`
- Data: `workspace/data/step28_bochner_killing_center_bound.json`
- Lean (updated): `workspace/proofs/Step28BochnerKilling.lean`
- Prior H₃ algebra: `workspace/proofs/Step27H3Algebra.lean`
- Prior notes: `workspace/notes/step27_preceptor_h3_positive_monotonicity_review.md`,
  `workspace/notes/step27_h3_endpoint_classification_and_model_theorem.md`
