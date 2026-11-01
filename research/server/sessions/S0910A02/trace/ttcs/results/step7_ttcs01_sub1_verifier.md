# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step7_positive_branch_four_constructions.md",
    "Sessions/S0910A02/workspace/notes/step1_initial_resolution_and_routes.md",
    "Sessions/S0910A02/workspace/data/step7_det_R_obstruction.json",
    "Sessions/S0910A02/workspace/notes/step6_positive_collapse_regularity_probes.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md",
    "Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

Verify the obstruction-amplitude principle for the positive branch of Yau Problem 26 in dimension 4. The claim: if a sequence (M_i, g_i) of closed oriented smooth 4-manifolds has |Ric_{g_i} - g_i|_{C^0} ≤ δ_i → 0 and is noncollapsed (Vol(B_1) ≥ v > 0), then at any orbifold singularity p of the GH limit, det R|_{Λ²_+}(p) = 0. The argument: (1) the MV Calabi region estimate gives Ric_{g_t} - Λg_t - tλχ_t o = O(t²ρ²) in g_cal-norm, where o is the first obstruction endomorphism; (2) converting to g_t-operator norm, the obstruction tλo has g_t-norm of order 1 (since g_t^{-1} ~ t^{-1} g_cal^{-1}); (3) since o is non-scalar when det R ≠ 0, it cannot be absorbed into a scalar Einstein constant; (4) therefore ||Ric - λg||_{C^0} ≥ c > 0, contradicting δ_i → 0. Check: (a) does this scaling argument apply to positive λ (the MV original is for negative Einstein orbifolds)? (b) is the conversion from g_cal-norm to g_t-norm correct in the core and transition regions? (c) does the non-scalar nature of o genuinely force a C^0 lower bound, or could cancellation between multiple singularities or between the obstruction and higher-order terms eliminate the defect? (d) Ozuch Example 1 on S^4/Z_2 shows L^p-close sequences exist without C^0 convergence when det R ≠ 0 — does this confirm or is it merely consistent with the principle? (e) What are the main gaps between this heuristic principle and a rigorous theorem?

## Output

## Scientific verification memo: obstruction-amplitude principle in the 4D positive branch

### 1. Source-grounded status

The scaling mechanism in the Step 7 note is scientifically sound **inside a Biquard/Ozuch-type gluing normal form**: if, near a resolving ALE core, the Ricci defect has leading term  
\[
t\,\lambda\,\chi_t\, o
\]
with \(o\) a nonzero trace-free infinitesimal Einstein deformation of the ALE model and the metric on the core is \(g_t\simeq t\,g_{\rm ALE}\), then the corresponding Ricci endomorphism defect is order one in the \(g_t\)-operator norm. A scalar Einstein constant shift cannot remove its trace-free part.

This does **not** by itself prove the proposed implication for an arbitrary sequence satisfying only  
\[
\|\operatorname{Ric}_{g_i}-g_i\|_{g_i\text{-op}}\le \delta_i\to0 .
\]
The missing mathematical input is a theorem placing such \(C^0\)-pinched, noncollapsed metrics into the weighted gluing coordinates and expansions used by Biquard/Ozuch, or an independent Pohozaev/projection argument valid under only \(L^\infty\) Ricci defect.

---

### 2. Sign of the Einstein constant and use of MV

The local scaling computation from Morteza–Viaclovsky is sign-insensitive. In the supplied MV source, Lemma 4.2 states on the Calabi region:
\[
\left|\nabla^k\left(\operatorname{Ric}_{g_t}-\Lambda g_t-t\lambda\chi_t(\rho)o\right)\right|_{g_{\rm cal}}
\le c_k t^2\rho^{2-k}.
\]
This formula is algebraic-local once the orbifold metric satisfies \(\operatorname{Ric}_{g_0}=\Lambda g_0\); replacing \(\Lambda<0\) by \(\Lambda>0\) does not change the \(t\)-scaling.

However, MV is not the direct 4D positive-branch source:

- MV treats real dimension \(2n\) with \(n\ge3\) for the Calabi \(\mathcal O(-n)\) model.
- In real dimension 4, the relevant ALE model is Eguchi–Hanson, and the appropriate references are Biquard and Ozuch.
- Ozuch Theorem 0.3 in the supplied source applies to **exact Einstein** 4-manifold sequences and Kähler Ricci-flat ALE bubbles in the chosen orientation, yielding
  \[
  \det \mathbf R_{g_o}(p)=0 .
  \]
  In 4D Einstein notation this is the determinant of the curvature-operator block selected by the bubble orientation, usually written \(R_+=W_+ + \frac{s}{12}\operatorname{Id}\) on \(\Lambda^2_+\), after fixing orientation conventions.

Thus: the sign issue is harmless for the scaling; the model/source transfer from MV to the 4D positive setting needs Biquard/Ozuch rather than MV alone.

---

### 3. Norm conversion: core and transition

Let \(g_t=t h_t\) on the ALE core, with \(h_t=g_{\rm ALE}+O(t\rho^2)\). Since \(\rho\le C t^{-1/4}\), the correction satisfies \(t\rho^2=O(t^{1/2})\), so \(h_t\) is uniformly equivalent to \(g_{\rm ALE}\).

For a \((0,2)\)-tensor \(T\),
\[
\|T\|_{g_t\text{-op}}
=
\|g_t^{-1}T\|_{\rm op}
\sim
t^{-1}\|g_{\rm ALE}^{-1}T\|_{\rm op}.
\]

Apply this to the two terms in the expansion.

#### Remainder term

If
\[
Q_t:=\operatorname{Ric}_{g_t}-\Lambda g_t-t\lambda\chi_t o
\]
satisfies
\[
|Q_t|_{g_{\rm ALE}}\le C t^2\rho^2,
\]
then
\[
\|Q_t\|_{g_t\text{-op}}\le C t\rho^2.
\]

- On a fixed compact ALE core, \(\rho=O(1)\), hence
  \[
  \|Q_t\|_{g_t\text{-op}}=O(t).
  \]
- In the transition zone \(\rho\sim t^{-1/4}\), hence
  \[
  \|Q_t\|_{g_t\text{-op}}=O(t^{1/2}).
  \]

So the remainder becomes small in the unweighted \(g_t\)-operator norm.

#### Obstruction term

For
\[
O_t=t\lambda\chi_t o,
\]
one gets
\[
\|O_t\|_{g_t\text{-op}}
\sim
|\lambda|\chi_t\,\|g_{\rm ALE}^{-1}o\|_{\rm op}.
\]

On a fixed compact core where \(\chi_t=1\) and \(o\neq0\), this is order one. In the transition region, \(o\) decays; for the 4D Eguchi–Hanson/Calabi case \(o=O(\rho^{-4})\), so the obstruction term is small there. The relevant \(C^0\) lower bound comes from the compact core, whose diameter and volume shrink with \(t\), but whose pointwise operator defect does not.

Therefore the conversion used in Step 7 is correct in the core and transition zones, provided the metric really has the quoted gluing expansion.

---

### 4. Why a non-scalar obstruction gives a \(C^0\) lower bound in a gluing normal form

On the ALE core,
\[
g_t^{-1}(t\lambda o)
=
\lambda\, h_t^{-1}o
=
\lambda\, g_{\rm ALE}^{-1}o+O(t).
\]
For Eguchi–Hanson/Calabi, \(o\) is trace-free and nonzero; in an orthonormal splitting its eigenvalues are not all equal. Hence for any scalar \(a\),
\[
\| \lambda g_{\rm ALE}^{-1}o-a\operatorname{Id}\|_{\rm op}
\ge
\frac12\bigl(\lambda_{\max}-\lambda_{\min}\bigr)
\ge c_0|\lambda|
\]
on some fixed compact part of the ALE core. Thus
\[
\inf_{a\in\mathbb R}
\|t\lambda o-a g_t\|_{g_t\text{-op}}
\ge c_0|\lambda|-O(t).
\]

This proves the intended point: a scalar shift of the Einstein constant can absorb only the scalar part of the Ricci defect, not the trace-free obstruction direction.

For the specific determinant obstruction in four dimensions, the coefficient is not literally the MV scalar \(\lambda\). In Biquard/Ozuch language, the leading local obstruction is determined by the curvature block \(R_+(p)\) acting on the Eguchi–Hanson orientation parameter. The condition
\[
\det R_+(p)=0
\]
means there is a nonzero orientation vector in the kernel. If \(\det R_+(p)\neq0\), no rotation of the Eguchi–Hanson model removes the first obstruction. The same norm scaling then gives an order-one trace-free pointwise defect in the corresponding gluing model.

---

### 5. Can cancellations remove the defect?

Inside a fixed gluing expansion with nonzero first obstruction coefficient, ordinary higher-order terms cannot cancel the obstruction: after raising an index with \(g_t^{-1}\), the obstruction is \(O(1)\) on the compact core, while the quoted remainder is \(O(t)\) there.

Multiple singularities also do not cancel pointwise if the obstruction terms are supported in disjoint shrinking cores. A supremum norm sees each core separately. A scalar Einstein-constant shift is global and scalar, so it cannot remove trace-free local endomorphism components.

There are, however, genuine mathematical ways the first coefficient may disappear:

1. **Local rotation/moduli parameters.** In the Eguchi–Hanson case, changing the orientation parameter changes the obstruction vector. The algebraic condition \(\det R_+(p)=0\) is exactly the condition permitting a first-order vanishing choice.

2. **Global deformation parameters.** If the orbifold metric has infinitesimal Einstein deformations, local curvature jets at singular points can vary in a finite-dimensional way. A rigorous obstruction equation must include these parameters.

3. **Different approximate families.** A metric sequence with only \(C^0\) Ricci pinching might not be close in weighted \(C^{2,\alpha}\) norms to the Biquard/Ozuch gluing ansatz. Without such proximity, the displayed obstruction term need not be available as a pointwise expansion.

Thus the non-scalar argument is decisive for metrics already in the gluing normal form, but it is not yet a theorem for all \(C^0\)-pinched noncollapsed sequences.

---

### 6. Ozuch Example 1: what it supports

Ozuch Example 1 in the supplied source states that for the round orbifold \(\mathbb S^4/\mathbb Z_2\), whose curvature block has nonzero determinant, there is a smooth 4-manifold \(M\) and metrics \(g_i\) with
\[
\|\operatorname{Ric}(g_i)-3g_i\|_{L^p(g_i)}\to0,\qquad
\operatorname{Ric}(g_i)\ge 3g_i,
\]
and
\[
(M,g_i)\to \mathbb S^4/\mathbb Z_2
\]
in GH sense, while no exact Einstein sequence with \(\operatorname{Ric}=3g\) has the same GH limit.

This is strong supporting evidence for the scaling picture: an order-one pointwise obstruction located in a region of volume tending to zero gives \(L^p\)-small defect for every finite \(p\), but not \(C^0\)-small defect.

It does not by itself prove the desired \(C^0\) determinant statement. The example distinguishes \(L^p\) proximity from pointwise operator pinching; it does not show that every possible smoothing of \(\mathbb S^4/\mathbb Z_2\) with \(\det R_+\neq0\) has a uniform \(C^0\) Ricci defect. That stronger statement requires the obstruction-amplitude theorem for approximate metrics.

---

### 7. Main mathematical gaps before a rigorous determinant theorem

To turn the heuristic into a theorem of the form

\[
\|\operatorname{Ric}_{g_i}-g_i\|_{C^0}\to0
\quad+\quad
\text{noncollapsed}
\quad\Longrightarrow\quad
\det R_+(p)=0
\]
at each orbifold singularity, the following mathematical pieces are needed.

1. **Orbifold/ALE structure for the approximate sequence.**  
   Ozuch Theorem 0.1 and 0.3 are stated for exact Einstein sequences. For merely \(C^0\)-pinched Ricci metrics, one needs an analogue giving an Einstein orbifold limit, ALE bubbles, bubble-tree scales, and orientation data.

2. **Weighted gluing normal form or substitute identity.**  
   The supplied Ozuch Theorem 0.2 says exact Einstein metrics GH-close to an Einstein orbifold arise from a gluing-perturbation procedure. The desired sequence is not exact Einstein. One needs either weighted \(C^{2,\alpha}\)-type gluing coordinates for approximate metrics, or a direct Pohozaev/projection formula using only
   \[
   \|\operatorname{Ric}_{g_i}-g_i\|_{L^\infty}\to0.
   \]

3. **A first-obstruction formula with \(L^\infty\) residual.**  
   The natural projection scaling is favorable in dimension four: on a core of scale \(t\), the exact obstruction projection is of size \(\sim t\), while an \(L^\infty\) Ricci defect \(\delta_i\) contributes \(\sim \delta_i t\). Thus \(\delta_i\to0\) should force the first obstruction coefficient to vanish, once the test tensor and coordinate comparison are justified.

4. **Orientation and block notation.**  
   The determinant must be attached to the curvature block corresponding to the bubble orientation. Reversing orientation swaps \(R_+\) and \(R_-\). The Step 7 Python data for \(S^4\), \(S^2\times S^2\), and \(\mathbb{CP}^2\) are consistent with the normalization \(\operatorname{Ric}=g\):
   \[
   R_+ = W_+ + \frac{s}{12}\operatorname{Id}
        = W_+ + \frac13\operatorname{Id}.
   \]

5. **Bubble-model assumptions.**  
   Ozuch Theorem 0.3 assumes Kähler Ricci-flat ALE blow-ups in the chosen orientation. If a \(C^0\)-pinched sequence could produce a different Ricci-flat ALE model, the supplied theorem would not directly apply.

6. **Interactions among singularities and scales.**  
   For a local determinant conclusion, one must show that localized obstruction tests isolate one singularity and one scale, with cross-terms from other cores and deeper bubbles of lower order.

7. **Regularity under only \(C^0\) Ricci pinching.**  
   The central analytic obstacle remains the lack of \(\nabla\operatorname{Ric}\), Einstein equation, or weighted \(C^{k,\alpha}\) control. Cheeger–Naber gives powerful bounded-Ricci information, but the Ozuch neck-coordinate and gluing machinery uses exact Einstein structure.

---

### Bottom line

The obstruction-amplitude scaling is correct and robust **once a Biquard/Ozuch-style local expansion is available**. The sign of \(\Lambda\) does not affect the scaling. The conversion from \(g_{\rm ALE}\)-norm to \(g_t\)-operator norm is correct: the remainder becomes small, while the trace-free obstruction stays order one on the compact core. A scalar Einstein-constant shift cannot remove it.

What is not yet supplied is the theorem connecting arbitrary noncollapsed \(C^0\)-Ricci-pinched 4-manifolds to that expansion. Ozuch Example 1 strongly illustrates why \(L^p\)-small defect is compatible with nonzero determinant, and why \(C^0\)-pinching is the right strength for the proposed obstruction, but it is supporting evidence rather than a proof of the determinant implication.