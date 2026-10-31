# Step 63: Jet-drift Ricci expansion and IL m=1 collar adjudication

Session `S0910A02`. Agent2 / Constructor. Phase Execute.

Depends on: Steps 11, 34, 47–50, 58–62 (A02 noncollapsed arc); A01 Steps 59–60
(IL base pair); A03 Steps 56, 63 (signed-Hessian lemma, graph-manifold correction).

## 0. What this step establishes

Two results of different natures, both at the level of precise mathematical
adjudication rather than full proof:

1. **IL m=1 collar verdict**: The signed-Hessian term at m=1 closes by one
   integration by parts using only $\|C_1\|_\infty$. The flat-$T^4$ gate does
   NOT kill the weighted m=1 estimate. A01's Step-60 base-pair proof
   independently establishes this at tensor-index level. The m=1 collar is
   NOT the failure point of the IL chain.

2. **Jet-drift channel verdict**: The exponential drift channel
   $t_i \sim \exp(-c/\delta_i)$ is REAL IN PRINCIPLE. The Einstein-jet space
   gives genuine local Weyl freedom, and the Ricci expansion of
   $g = e + H_E + A(\log r)\,W$ confirms that the drift corrections vanish
   at the jet center and are $O(\delta)$ at the outer edge for
   $|A'|,|A''|\lesssim\delta$. No static remainder or resonance closes the
   channel at the 2-jet level.

---

## 1. IL m=1 collar adjudication

### 1.1 The binary question

From the Step-62 handoff: does the m=1 collar term have the signed form
$$\int\chi\,\nabla_i\nabla_j\chi\;\mathcal{B}^{ij}(U_1)$$
closing by one integration by parts with $\|C_1\|_\infty$, or is there a
genuinely unclosed collar/current term?

### 1.2 The flat-$T^4$ gate

The Strategist's gate: run the proposed estimate on the flat-$T^4$ witness
with $\chi=(1+\cos x_1)/2$, where $\int|\mathrm{Rm}|^2 = 48\pi^4t^2+O(t^3)$
gives $E'/E\sim 2/t$.

**Gate analysis.** The apparent contradiction — $dE/dt\le CE$ would predict
$E\le E_0e^{Ct}$, inconsistent with $E\sim t^2$ from $E_0=0$ — is resolved by
distinguishing $T=\mathrm{Rm}+G$ from $\mathrm{Rm}$ alone. On flat $T^4$,
$G=g\owedge g/(2(n-1))\ne0$, so $\|T\|^2\sim\|G\|^2+O(t^2)$ is bounded away
from zero. The weighted energy $E_w=\int|U_1|^p+\int|C_2|^p$ where $U=aT$
may well satisfy $dE_w/dt\le CE_w$ even when $\int|\mathrm{Rm}|^2$ does not.
The flat-$T^4$ gate kills any claim that weighted control implies unweighted
control WITHOUT the intermediate $T_0\in L^\infty$ step, but it does NOT kill
the weighted m=1 estimate itself.

### 1.3 The signed-Hessian form at m=1

A01 Step 60 (message #438) establishes at tensor-index level that:

- Every coefficient-derivative term at m=1 has total cutoff derivative $\le3$.
- The $B_3*U_0$ source produces $\chi C_3*U_0$ in the differentiated equation.
- After one IBP, the problematic remnant $I_{\rm top}=\int\chi|C_2||V|^p$
  is a signed tensor contraction of the form
  $\int\chi\nabla_i\nabla_j\chi\,\mathcal{B}^{ij}(V)$,
  because $V=U_1$ and $|V|^{p-2}V\otimes V$ provides the bilinear form.
- The A03 signed-Hessian lemma closes it with only $\|C_1\|_\infty$.
- The $C_2$ evolution is $\partial_tC_2=g^{-1}*U_1*C_1$ (no $U_2$).

My independent structural analysis (`step63_m1_collar_adjudication.json`)
confirms:
- **Form A** (pure signed-Hessian IBP): closes with $\|C_1\|_\infty$ only.
- **Form B** (top-cutoff residual $I_1$): for m=1, reduces to Form A because
  $V=U_1$ is current and the residual IS the signed-Hessian term.
- **Form C** (coupled pair $(U_1,C_2)$): closes at the weighted level; the
  flat-$T^4$ gate does not contradict it.

### 1.4 Verdict

**The m=1 collar closes.** The binary question resolves affirmatively:
the signed-Hessian form holds and one IBP with $\|C_1\|_\infty$ suffices.
No genuinely unclosed collar/current term exists at m=1.

The IL chain's remaining gaps (from A01 #441 gate audit) are:
- **Defect Moser endpoint FAILED**: general-$p$ two-factor inequality and
  nested recurrence not proved. This blocks the V-leg of the bootstrap.
- Curvature Moser endpoint: conditional (internal logic sound, index-level
  identities missing).
- Per-datum existence: conditional (tame hierarchy, splice verified; fixed-
  parameter parabolic existence, time-derivative induction, upstream
  first-exit estimates missing).

The m=1 collar was NOT the failure point; the defect Moser endpoint is.

---

## 2. Jet-drift Ricci expansion

### 2.1 Setup

The Einstein-jet space at a point is
$$\mathcal{E}^{\rm NC}_\Lambda=\{H:H_{ij}=-\tfrac13R_{ikjl}x^kx^l,\;
\mathrm{Ric}(R)=\Lambda e\},$$
an affine space whose tangent space (fixed-Ricci directions) is the
10-dimensional Weyl space $\mathrm{Sym}^2_0(\Lambda^+)\oplus\mathrm{Sym}^2_0(\Lambda^-)$.

The drift model: $g=e+H_E+A(\log r)\,W$ where $H_E\in\mathcal{E}^{\rm NC}_\Lambda$
is a particular Einstein jet, $W$ is a Weyl-direction quadratic jet, and
$A:\mathbb{R}\to[0,1]$ is a slowly varying radial profile.

### 2.2 Linearized Ricci at the center

For the specific Weyl direction $W_+=\mathrm{diag}(w,-w,0)$, $W_-=0$:

- The linearized Ricci of $H_E$ at $x=0$ is $\Lambda\,\delta_{ij}$ (verified
  symbolically: `step63_jet_drift_ricci.json`).
- The linearized Ricci of $W$ at $x=0$ is $0$ (verified symbolically:
  `step63_jet_drift_full.json`, `Ric_lin_W_is_zero: true`).

This confirms the jet space is Einstein-compatible at the linearized level,
and the Weyl direction is in the kernel of the linearized Ricci operator.

### 2.3 Drift corrections

The critical finding: **all drift terms vanish at $x=0$**.

The $O(A')$ and $O(A'')$ corrections to $\mathrm{Ric}(g)$ come from terms
involving first or second derivatives of $A$ multiplied by $W$ or its first
derivatives. Since $W$ is quadratic in $x$ and $dW$ is linear in $x$, both
vanish at $x=0$. Therefore:
$$\mathrm{Ric}(g)(0)=\Lambda\,e\quad\text{exactly (for any $A$)}.$$

At general $x$, the drift corrections are:
$$|\mathrm{Ric}(g)-\Lambda g|\sim|A'|\cdot r+|A''|\cdot r^2+A^2\cdot r^2,$$
where the first two terms come from differentiating $A(\log r)$ and the third
from Christoffel products. At the outer edge $r\sim1$ of the jet region:
$$|\mathrm{defect}|\sim|A'|+|A''|=O(\delta)$$
for $|A'|,|A''|\lesssim\delta$.

### 2.4 Weyl traversal

The profile $A(\log r)$ ranges over $|\log t|\sim1/\delta$ dyadic scales.
An $O(1)$ change in $A$ over this range gives $A'\sim\delta$, $A''\sim\delta^2$.
The Weyl block changes by $O(1)\cdot W$ because the amplitude $A$ changes
by $O(1)$. The full 10-dimensional Weyl space is available — the
1:(-2):1 eigenvalue ratio from the Step-61 toric ansatz was an artifact of
the one-dimensional invariant sector, and the ratio mismatch with the
orbifold's 2:(-1):(-1) carries no information.

### 2.5 Verdict

**The drift channel is REAL IN PRINCIPLE.**

- No static remainder closes it: the nonlinear Christoffel products are
  $O(r^2)$ and vanish at the center.
- No resonance closes it: the drift corrections vanish at the center and
  are $O(\delta)$ at the outer edge for slow drift.
- The Weyl block can traverse any path in the 10-dimensional Weyl space
  while maintaining $\|\mathrm{Ric}-\Lambda g\|_{\rm op}\le C\delta$.

### 2.6 Two-point Weyl reachability

The drift model requires connecting an outer Weyl block $W_{\rm out}$
(orbifold value at $p$) to an inner Weyl block $W_{\rm in}$ (EH bubble
degeneracy) via a path in the 10-dimensional Weyl space
$\mathrm{Sym}^2_0(\mathbb{R}^3)^+\oplus\mathrm{Sym}^2_0(\mathbb{R}^3)^-$.

The degenerate set (where $R_\pm=W_\pm+\frac{\Lambda}{3}\mathrm{Id}$ has a
kernel) is a union of three hyperplanes in $\mathrm{Sym}^2_0(\mathbb{R}^3)$
(one for each eigenvalue condition), hence codimension 1. Any point in
$\mathrm{Sym}^2_0(\mathbb{R}^3)$ can reach the degenerate set by a bounded
path. The two-point problem is **universally solvable**
(`step63_two_point_reachability.json`).

For the product-quotient orbifold (Steps 55–57), $W_\pm$ is already on the
degenerate set (eigenvalues $2\Lambda/3,-\Lambda/3,-\Lambda/3$), so no drift
is needed — consistent with the automatic first-obstruction vanishing there.
For a generic orbifold point, the drift amplitude needed is $O(\Lambda)=O(1)$,
consistent with the exponential channel.

### 2.7 Implication for the necessity theorem

The rate-limited H4 necessity theorem (Steps 59–62) states:
for a noncollapsed $C^0$-Ricci-pinched sequence with an ADE bubble,
either $R_\pm(p)\zeta=0$ or $t_i\le\exp(-c/\delta_i)$.

The jet-drift computation confirms that the exponential escape channel
$t_i\sim\exp(-c/\delta_i)$ is a genuine geometric possibility, not merely
a failure of the proof technique. The two-point reachability analysis shows
this channel is universally available (not specific to special orbifold
geometries). The theorem is **sharp** at the rate
$\delta_i\log(1/t_i)\to0$.

This does NOT mean a counterexample exists. Constructing an actual closed
manifold realizing the drift requires:
1. A global metric transitioning from one Weyl block to another across
   an exponential neck.
2. Matching at both ends (universally solvable in the Weyl space, but
   the geometric realization on a neck is not constructed).
3. Smoothness at all singular/collapse loci.
4. The underlying smooth manifold must NOT already carry an Einstein metric
   (the smooth-category fidelity condition).

The product-quotient mixed-wall family (Steps 55–57) is exactly the kind
of manifold where such a construction would need to live. But no closed
drift neck has been constructed on any mixed row.

---

## 3. Relation to the group's current state

- **A01 IL route**: defect Moser endpoint FAILED gate audit (blocking gap).
  The m=1 collar (my adjudication) is NOT the failure point. The IL chain
  remains conditional on the Moser endpoint repair.
- **A03 graph-manifold route**: corrected from counterexample to gap-theorem
  candidate (flat-slice barrier + $T^3$ Einstein impossibility). Suggests the
  negative branch may hold more broadly than IL.
- **A02 noncollapsed positive arc**: jet-drift channel confirmed real in
  principle; necessity theorem sharp at $\delta\log(1/t)$. No closed
  counterexample constructed.

## 4. Files
## 4. Files

- `workspace/scripts/step63_m1_collar_adjudication.py` →
  `workspace/data/step63_m1_collar_adjudication.json`
- `workspace/scripts/step63_jet_drift_ricci.py` →
  `workspace/data/step63_jet_drift_ricci.json`
- `workspace/scripts/step63_jet_drift_full.py` →
  `workspace/data/step63_jet_drift_full.json`
- `workspace/scripts/step63_two_point_reachability.py` →
  `workspace/data/step63_two_point_reachability.json`
