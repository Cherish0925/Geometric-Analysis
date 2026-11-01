# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md",
    "Sessions/S0910A02/workspace/notes/step3_corrections_lebrun_and_collapse.md",
    "Sessions/S0910A02/workspace/notes/step3_stable_integral_obstruction_principle.md",
    "Sessions/S0910A02/workspace/scripts/step3_corrected_lebrun_bounds.py",
    "Sessions/S0910A02/workspace/scripts/lens_space_positive_collapse.py",
    "Knowledge/objects/papers/Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8/object.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Knowledge/objects/papers/Curvature-Connected-Sums-and-Seiberg-Witten-Theory--7e92a6723434--2ac6d11897c5/object.md",
    "Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md"
  ]
}
```

## Task

Check the Step 3 repaired LeBrun/Ishida-LeBrun analysis for Yau Problem 26. Read the active goal, the correction note, the stable integral obstruction theorem note, the repaired script, and the primary source excerpts/files. Verify the constants in the 4D Chern-Gauss-Bonnet identity, the scalar-only k/A=2/3 and mixed k/A=1/3 thresholds, the derivation of the pinching lower bound δ/(1-δ) >= sqrt((p-1/3)/2), and the corrected interpretation of positive collapse via lens spaces. Identify any algebraic mistakes, missing hypotheses (orientation, b_+, monopole class, strict/equality cases), or overclaims relative to the full Yau26 proposition. Give a direct scientific memo, not a checklist.

## Output

## Verification memo — Step 3 LeBrun / Ishida–LeBrun analysis for Yau 26

I reworked every constant and every derivation step independently against the three LeBrun source files. The core algebra is correct. The main results — the corrected CGB factor, the $k/A=2/3$ scalar threshold, the $k/A=1/3$ mixed threshold, and the pinching lower bound $\frac{\delta}{1-\delta}\ge\sqrt{(p-1/3)/2}$ — all hold as written, and the interpretation of the lens-space computation is right. Below I record the reproduced steps, then the few hypotheses that deserve to be stated more visibly and one place where an application remark is empty on the very family it is applied to.

### 1. Chern–Gauss–Bonnet factor

The signature/Euler identity
$$
2\chi+3\tau=\frac{1}{4\pi^2}\int\Big(2|W_+|^2+\frac{s^2}{24}-\frac{|\mathring r|^2}{2}\Big)
$$
is exactly the form printed in all three LeBrun files. For an Einstein metric in dimension four, $s=4\lambda$, so $\int\frac{s^2}{24}=\frac{16\lambda^2}{24}V=\frac23\lambda^2 V$, giving $4\pi^2(2\chi+3\tau)=2\int|W_+|^2+\frac23\lambda^2 V$ and hence
$$
8\pi^2(2\chi+3\tau)=4\int|W_+|^2+\tfrac43\lambda^2V,\qquad \int|W_+|^2=2\pi^2(2\chi+3\tau)-\tfrac13\lambda^2 V.
$$
This confirms the retraction of the Step 2 factor $16/3$ in favor of $4/3$, and the corrected $\int|W_+|^2$ coefficient $-\tfrac13$ rather than $-\tfrac43$. The script's `corrected_einstein_threshold` uses $\int|W_+|^2\le\pi^2A(\tfrac43-2p)$, which follows from $\lambda^2V>2\pi^2A$ and the corrected identity; it turns nonnegative-only when $p>2/3$. Correct.

### 2. The two thresholds

Scalar-only (LeBrun 1996): with $\int s^2>32\pi^2A$ and $\int s^2=16\lambda^2V$ one gets $\lambda^2V>2\pi^2A$, then $\int|W_+|^2<2\pi^2(\tfrac23A-k)$; nonnegativity forces $k<\tfrac23A$, so no Einstein for $k\ge\tfrac23A$. This reproduces LeBrun 1996 Theorem 3 exactly.

Mixed (LeBrun 2001 Prop 3.1–3.2, Cor 3.4): $F_+(g):=\frac{1}{4\pi^2}\int(\frac{s^2}{24}+2|W_+|^2)\ge\frac23(c_1^+)^2\ge\frac23A$ for *every* metric, so for Einstein $A-k=F_+\ge\frac23A$ gives $k\le\frac13A$, i.e. no Einstein for $k\ge A/3$. This matches Corollary 3.4 verbatim, and the $A/3$ range is a stated theorem in that file, not an extrapolation. The convex-hull fact $(c_1^+)^2\ge (c_1(X))^2=A$ is correct: for $v$ with $v^2>0$, $(v^+)^2=v^2+|(v^-)^2|\ge v^2$, and the blow-up sign trick keeps the cross terms nonnegative.

### 3. Pinching lower bound — full reproduction

Take $\|\operatorname{Ric}_g+g\|_{op}\le\delta<1$, Ricci-endomorphism eigenvalues $-1+e_i$, $|e_i|\le\delta$.

- $s=-4+\sum e_i\le-4+4\delta<0$, so $|s|\ge4(1-\delta)$ and $\frac{s^2}{24}\ge\frac23(1-\delta)^2$.
- $\mathring r$ eigenvalues are $e_i-\bar e$, so $|\mathring r|^2=\sum(e_i-\bar e)^2\le\sum e_i^2\le4\delta^2$, hence $\int\frac{|\mathring r|^2}{2}\le2\delta^2V$.

From CGB, $\frac{1}{4\pi^2}\int\frac{|\mathring r|^2}{2}=F_+-T_+\ge L_+-T_+$ with $L_+=\frac23A$, $T_+=A-k$, giving
$$
L_+-T_+\le\frac{\delta^2V}{2\pi^2}.\qquad(1)
$$
Dropping $|W_+|^2\ge0$ in CGB and using the pointwise bounds,
$$
T_+\ge\frac{V}{4\pi^2}\,b(\delta),\quad b(\delta)=\tfrac23(1-\delta)^2-2\delta^2,\qquad(2)
$$
so if $b(\delta)>0$ then $V\le 4\pi^2T_+/b(\delta)$. Substituting into (1):
$$
(L_+-T_+)\,b(\delta)\le 2\delta^2T_+.
$$
Expanding $b(\delta)$ and moving the $-2\delta^2(L_+-T_+)$ term:
$$
(L_+-T_+)\tfrac23(1-\delta)^2\le 2\delta^2T_++2\delta^2(L_+-T_+)=2L_+\delta^2,
$$
which is the algebraic identity the note uses (I checked $2\delta^2T_++2\delta^2(L_+-T_+)=2L_+\delta^2$ explicitly). Dividing by $\tfrac23$ and taking roots,
$$
\frac{\delta}{1-\delta}\ge\sqrt{\frac{L_+-T_+}{3L_+}}=\sqrt{\frac{k-A/3}{2A}}=\sqrt{\frac{p-1/3}{2}}.
$$
At $p=2/3$: $\sqrt{1/6}=1/\sqrt6$, so $\delta\ge 1/(1+\sqrt6)=0.28989795$. Matches the reported value and the JSON. The whole derivation is sound.

The window $b(\delta)>0$ is $\delta<1/(1+\sqrt3)\approx0.366$, where $\frac{\delta}{1-\delta}<1/\sqrt3$; setting $\sqrt{(p-1/3)/2}=1/\sqrt3$ gives $p=1$. So the theorem's regime is exactly $1/3<p<1$, which also coincides with the hypothesis $T_+=A-k>0$, i.e. $k<A$. This internal consistency (regime of validity = regime where $T_+>0$) is worth stating explicitly in the theorem note; right now the reader has to notice that $T_+>0$ silently caps $p<1$.

The logical form is correct: for small $\delta$, $b(\delta)>0$ holds, so any $\delta$-pinched metric forces $(*)$; hence no $\delta\to0$ pinched metric exists at fixed $p>1/3$. This is a necessary condition on an assumed metric — it constructs nothing — and both notes say so.

### 4. Two hypotheses to surface

**$b_+$ and monopole class.** The uniform lower bound $F_+(g)\ge\frac23A$ for *all* $g$ rests on $X$ minimal of general type carrying a nonzero Seiberg–Witten/monopole class for every metric. For $b_+(X)=1$ this needs care, but LeBrun 2001 Prop 3.2 explicitly settles it: because $(2\chi+3\tau)(X)>0$, the invariant is polarization-independent even at $b_+=1$. So the estimate is valid across the family, but the theorem note should name this dependence rather than leave $b_+$ unmentioned, since without it the metric-uniformity of $L_+$ is not automatic. Orientation is handled (the note gives the $T_-$/$F_-$ variant), and $L_+>T_+$ (i.e. $p>1/3$) is what powers the argument.

**Existence versus obstruction.** The result bounds $\delta$ from below *given* a pinched metric; it does not produce any tightly pinched metric on these manifolds. Correctly stated in both notes.

### 5. Positive-pinch remark is empty on the general-type family

The theorem note states the same proof runs for $\|\operatorname{Ric}_g-g\|_{op}\le\delta$ "because only $s^2$ and $|\mathring r|^2$ enter," and the application asserts a lower bound for "both positive- and negative-normalized Ricci pinching (subject to the relevant sign being compatible with other obstructions)." The abstract statement is true, but on $M=X\#k\overline{\mathbb{CP}}{}^2$ with $X$ general type the parenthetical is doing heavy lifting: a monopole class forbids any metric with $s\ge0$ (LeBrun 2006 Prop 3.3), whereas $\operatorname{Ric}\approx+g$ forces $s>0$. So there are *no* $\operatorname{Ric}\to+g$ pinched metrics on these manifolds at all — the positive branch of the application is vacuous rather than merely bounded. The substantive content on this family is the $\operatorname{Ric}\to-g$ branch. This is why §5 of the correction moves the positive-pinching discussion to round lens spaces, which is the right move. I'd recommend the theorem note say plainly that the positive branch is void on general-type blow-ups, to prevent a reader from thinking it constrains a positive-Einstein refutation on those same spaces.

### 6. Lens-space computation

Round $S^3/\mathbb Z_m$ has constant curvature $1$, so $\operatorname{Ric}=(n{-}1)Kg=2g$; with $h=2g$, $\operatorname{Ric}_h=\operatorname{Ric}_g=2g=h$, so the normalized $\operatorname{Ric}\to+g$ pinching parameter is exactly $0$ for every $m$, while $\mathrm{Vol}=2\pi^2/m$ and injectivity radius $\to0$. All correct; the length/volume scalings $\sqrt2$ and $2^{3/2}$ under $h=2g$ are right. Note these are dimension-three, and each such space is itself Einstein, so it satisfies Yau 26 trivially — it is a demonstration that exact positive pinching coexists with collapse, not a candidate refutation. The reframed positive-branch question (does collapse force Einstein-compatible quotient/orbifold structure) is the correct spirit of Anderson / Cheeger–Tian / Cheeger–Fukaya–Gromov.

### 7. Link to the full Yau 26 statement

The $\delta$ used here is a normalized half-width. Given $c_n\le\operatorname{Ric}\le C_n g$ with $c_n,C_n$ of one sign, scaling $g\mapsto tg$ (Ricci endomorphism eigenvalues scale $1/t$) recenters the spectrum at $-1$ when $c_n+C_n<0$, and then $\delta=\dfrac{C_n-c_n}{|C_n+c_n|}$. This translation should be written into the notes, because Yau 26 is about a *fixed* dimensional window $[c_n,C_n]$, i.e. a fixed $\delta$. The obstruction says $\delta\ge\delta_{\min}(p)$ on LeBrun families, and $\delta_{\min}(p)\to0$ as $p\to1/3^+$; therefore this machinery does not close off the refutation route near $p=1/3$, and it says nothing about arbitrary manifolds or dimensions $\ne4$. Both notes state this correctly and do not present the result as bearing on the full proposition. Measured against the full Yau 26 statement (all $n\ge2$, all closed manifolds), the standing content is: one four-dimensional Seiberg–Witten family cannot furnish a fixed-margin $\operatorname{Ric}\to-g$ refutation, and the surviving four-dimensional slot is the zero-margin regime $p\to1/3^+$ (plus any mechanism that uses $\mathring r\equiv0$ discontinuously, e.g. holonomy/rigidity rather than an all-metric curvature integral). That framing is accurate and not stronger than the mathematics supports.

### Unresolved items the material cannot settle here
- Whether $M=X\#k\overline{\mathbb{CP}}{}^2$ with $p\to1/3^+$ actually *admits* any $\operatorname{Ric}\to-g$ pinched metric (the obstruction is silent on existence; a construction is needed to make the surviving slot real).
- Whether the zero-margin sequence can simultaneously respect all-sign Einstein nonexistence and produce genuinely tight pinching — this needs a separate estimate for $|W_+|$ or a direct metric construction, neither present in the files.
- The refined direct optimization (`maximize_refined_F`) is a self-consistency check that only reproduces $p=1/3$ at $\delta=0$; its $\delta>0$ objective uses separated bounds and is weaker than the CGB-subtraction route, as the note itself records. It does not affect any conclusion, but it should not be cited as an independent strengthening.