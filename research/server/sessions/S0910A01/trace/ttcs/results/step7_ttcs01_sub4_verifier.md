# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/scripts/step7_bochner_conformal_kahler.py",
    "Sessions/S0910A01/workspace/notes/step7_local_vs_global_rigidity.md",
    "Sessions/S0910A01/workspace/scripts/step6_tensor_slack_algebra.py"
  ]
}
```

## Task

Verify the following chain of claims for the negative-branch analysis of Yau Problem 26 in dimension 4.

1. BOCHNER FORMULA: On a 4-dimensional Einstein manifold with div(W+)=0, the scalar Bochner formula is (1/2)Δ|W+|² = |∇W+|² + (s/3)|W+|² - 4·tr(W+³), where tr(W+³) = α³+β³+γ³ = 3αβγ for trace-free eigenvalues α+β+γ=0. Check the coefficient -4 against the ℂℍ² example (s=-4, eigenvalues (1/3,1/3,-2/3), |W+|²=2/3, W+ parallel).

2. CALIBRATED PROFILE CONSISTENCY: At the target eigenvalues (1/12,1/12,-1/6) with |W+|²=1/24 and s=-4, the Bochner formula gives |∇W+|² = 1/24 > 0. Is this calculation correct? Does it mean the calibrated two-eigenvalue profile with constant norm is consistent but NOT parallel?

3. CONFORMAL-KÄHLER OBSTRUCTION: On a smooth Einstein 4-manifold with Ric=-g, if W+ has the two-eigenvalue profile, Derdziński gives conformally Kähler: g̃=f²g is Kähler. The conformal weight gives |W+_g|² = f⁴s̃²/24 where s̃ is the Kähler scalar curvature. For constant |W+_g|²=1/24: f²|s̃|=1. The conformal scalar curvature relation s̃=f⁻²(s-6f⁻¹Δf) with s=-4 and f²s̃=-1 gives Δf=-f/2. On a COMPACT Einstein manifold: Stokes gives ∫Δf=0=-(1/2)∫f<0, contradiction, so f=const and the metric is Kähler with |W+|²=s²/24=2/3≠1/24. On a NONCOMPACT limit: Δf=-f/2 can have nonconstant positive solutions. Verify each step, especially the sign conventions and the conformal transformation formula.

4. STRUCTURAL CONSEQUENCE: Does this correctly show that the local Derdziński mechanism cannot give a contradiction on noncompact pointed limits, making the negative-branch argument inherently global?

## Output

## Verification Memo — Ric=−g four-dimensional route, Bochner + conformal-Kähler chain

Headline: statements 1 and 2 hold qualitatively but the Bochner constants used are not the standard ones and the ℂℍ² test cannot detect that. Statement 3's conformal-curvature formula is correct, but its interpretation is where the chain breaks. Statement 4's structural conclusion — "the local Derdziński mechanism gives no contradiction on smooth pointed limits, so the route is inherently global" — is contradicted by Derdziński's own theorem: for the calibrated *constant-norm two-eigenvalue* profile there is a purely local contradiction, needing no compactness. I lay out the arithmetic so you can check this against the primary sources.

---

### 1. Bochner formula: the ℂℍ² test validates only a ratio

Write the formula as $\tfrac12\Delta|W^+|^2 = |\nabla W^+|^2 + a\,s|W^+|^2 + b\,\mathrm{tr}(W^{+3})$. On ℂℍ² the gradient term vanishes ($W^+$ parallel) **and** the two curvature terms cancel individually. So the ℂℍ² check reduces to one linear equation, $a\,s|W^+|^2 + b\,\mathrm{tr}(W^{+3})=0$, i.e. $a(-4)(2/3)+b(-2/9)=0 \Rightarrow b=-12a$. Every pair with $b=-12a$ passes. The script's $(a,b)=(1/3,-4)$ passes; so does the standard $(1/2,-6)$; so does the sign-reversed $(-1/2,6)$. The example cannot fix the absolute magnitude or the overall sign.

The widely used form (Derdziński, Compositio 49 (1983); Besse, *Einstein Manifolds* §16) is
$$
\Delta|W^+|^2 = 2|\nabla W^+|^2 + s|W^+|^2 - 36\det W^+,\qquad \tfrac12\Delta|W^+|^2=|\nabla W^+|^2+\tfrac{s}{2}|W^+|^2-6\,\mathrm{tr}(W^{+3}),
$$
using $\det W^+=\alpha\beta\gamma$ and $\mathrm{tr}(W^{+3})=3\alpha\beta\gamma=3\det W^+$. That is $(a,b)=(1/2,-6)$, not $(1/3,-4)$. The $s/3$ coefficient is the constant that appears in the Weitzenböck formula for a self-dual *2-form* $\omega\in\Lambda^+$ (spin-1), $\nabla^*\nabla\omega-2W^+(\omega)+\tfrac{s}{3}\omega=0$; $W^+$ itself lives in $S^2_0\Lambda^+$ (spin-2) and carries a different curvature constant. It looks like the two Weitzenböck constants were merged. Please reconcile against the exact normalization in the cited LeBrun source and Derdziński before this coefficient propagates further.

Impact: with the standard $(1/2,-6)$ the constant-norm profile gives $|\nabla W^+|^2 = 6\,\mathrm{tr}(W^{+3}) - \tfrac{s}{2}|W^+|^2 = 6(-\tfrac{1}{288}) - (-2)(\tfrac{1}{24}) = -\tfrac{1}{48}+\tfrac{1}{12}=\tfrac{1}{16}$, not $1/24$. The sign of the $s$-term (which the source must fix) is what guarantees positivity; under the standard form it stays positive.

### 2. Calibrated arithmetic is internally consistent

$(\alpha,\beta,\gamma)=(1/12,1/12,-1/6)$: $|W^+|^2=6/144=1/24$; $\mathrm{tr}(W^{+3})=3\alpha\beta\gamma=-1/288$; $s=g^{ij}\mathrm{Ric}_{ij}=-4$. The script's $|\nabla W^+|^2=1/24$ follows from its own $(1/3,-4)$ constants; the standard constants give $1/16$. Either way the qualitative reading "consistent with Bochner and not parallel" holds. But this is a necessary condition only, and §4 shows it is not sufficient.

### 3. Conformal scalar-curvature relation is correct; the Stokes step is fine but mis-phrased

For $\tilde g=f^2 g$ in $n=4$ (so $\tilde g=u^{4/(n-2)}g=u^2g$, $u=f$), Yamabe gives $\tilde s=f^{-3}(sf-6\Delta f)=f^{-2}(s-6f^{-1}\Delta f)$ with $\Delta=\mathrm{div\,grad}$ (analyst's Laplacian, negative spectrum). This matches the script. Substituting $s=-4$ and $f^2\tilde s=-1$ yields $\Delta f=-f/2$. Correct.

The Stokes step is essentially right but stated as a non-sequitur. On closed $M$, $\int_M\Delta f\,dV=0$ while $\int_M(-f/2)\,dV<0$ for $f>0$ shows $\Delta f=-f/2$ has **no positive solution at all** — not that "$f=\mathrm{const}$." A constant $f\neq0$ gives $0=-f/2$, also impossible. So the correct reading is: no globally defined positive conformal factor produces a $|W^+|^2=1/24$ Kähler structure on compact $M$. That is the right fact; the route to it in §4 is the issue.

### 4. Central point: the calibrated profile is locally impossible via Derdziński's factor

Derdziński's theorem does not present $f$ as a free function. For an oriented Einstein 4-manifold whose $W^+\neq0$ has at most two distinct eigenvalues, the metric
$$
h \;=\; (\text{const})\,|W^+|_g^{2/3}\,g
$$
is Kähler on $\{W^+\neq0\}$. The conformal factor **is** $\propto|W^+|^{2/3}$. This is exactly why the Page metric and the Chen–LeBrun–Weber metric — the known two-eigenvalue conformally-Kähler Einstein 4-manifolds — all have **nonconstant** $|W^+|$: their conformal factor is nonconstant precisely because $|W^+|$ varies.

The calibrated limit is built to have $|W^+|$ **constant** ($=1/(2\sqrt6)$, from $s+8\sqrt6|W^+|=0$ with $s=-4$). Then $|W^+|^{2/3}$ is constant, so $h$ is homothetic to $g$, so $g$ is itself Kähler, hence Kähler–Einstein, hence
$$
|W^+|^2 = \frac{s^2}{24}=\frac{16}{24}=\frac23 \neq \frac{1}{24}.
$$
This is a contradiction on any open set — no compactness, no Stokes. The calibrated eigenvalues $(1/12,1/12,-1/6)$ are already in exact Kähler ratio ($\text{simple}=-2\times\text{double}$), so Derdziński applies cleanly, and the conclusion is Kähler–Einstein, whose $W^+$ is parallel ($\nabla W^+=0$). Yet §2's Bochner value gives $|\nabla W^+|^2>0$ (parallel is excluded). Parallel vs non-parallel is the same contradiction seen from the Bochner side. Consistently: the hypotheses "Einstein, $s=-4$, constant $|W^+|=1/(2\sqrt6)$, two eigenvalues" are mutually incompatible.

Why the script's escape is spurious: it re-derives $\Delta f=-f/2$ as if $f$ were unknown. But the actual Derdziński Kähler metric with constant $|W^+|$ is $h=(\text{const})g$, i.e. constant $f$, for which $\tilde s=f^{-2}s=-4/f^2$ and $f^2\tilde s=s=-4$, giving $|W^+_g|^2=(f^2\tilde s)^2/24=16/24=2/3$. The equation $\Delta f=-f/2$ arose only from **imposing** $f^2\tilde s=-1$ (equivalently $|W^+|^2=1/24$), a value the geometry forbids. The absence of a constant solution to $\Delta f=-f/2$ is not a door to a nonconstant one; it is the same incompatibility re-expressed. The "noncompact limit lets $f$ be nonconstant" reasoning ignores that Derdziński fixes $f=|W^+|^{2/3}$, which is constant here on compact and noncompact limits alike.

Consequence for statement 4: under the two-eigenvalue + constant-norm hypothesis, the smooth (noncollapsed) Einstein limit is locally obstructed. The local Derdziński mechanism **does** close the noncollapsed case. The part that genuinely resists a smooth-limit argument is the *collapsed* case, where no smooth Einstein limit and no Derdziński structure is available. This is the opposite of the structural summary in the step-7 note.

### Grounding question that decides the whole picture: the target relation $s+8\sqrt6|W^+|=0$

The Kähler–Einstein equality relation ($s<0$) is $|W^+|=|s|/(2\sqrt6)$, i.e. $s+2\sqrt6|W^+|=0$, giving $|W^+|^2=s^2/24=2/3$. The scripts instead calibrate to $s+8\sqrt6|W^+|=0$ — a factor of 4 in the Weyl coefficient, hence a factor of 16 in $|W^+|^2$ (target $1/24$ vs Kähler $2/3$). This is decisive:

- If the relevant sharp LeBrun estimate has its equality case at Kähler–Einstein (the usual situation for the $c_1^2$/mixed scalar–Weyl estimates), then near-equality pushes $|W^+|^2\to 2/3$, Derdziński gives a genuine Kähler–Einstein limit, and there is no obstruction — the limit simply *is* Einstein.
- If the estimate genuinely forces $|W^+|^2\to1/24$ with two eigenvalues, then §4's local contradiction fires and the noncollapsed case closes locally.

Either way, the arithmetic of the "$8\sqrt6$" needs to be traced to the exact LeBrun inequality being used (from the cited `Ricci-curvature-minimal-volumes...` object) and its equality case identified explicitly. As written I cannot locate a standard estimate whose equality lies at $s+8\sqrt6|W^+|=0$; the Kähler relation is $s+2\sqrt6|W^+|=0$. Confirm which inequality, with the exact constant and equality condition, underlies the target.

### What is unresolved and what would settle it

- **Bochner constants.** Extract $\tfrac12\Delta|W^+|^2=|\nabla W^+|^2+a\,s|W^+|^2+b\,\mathrm{tr}(W^{+3})$ with numeric $a,b$ and the sign convention of $\Delta$ from Derdziński 1983 / Besse §16 / the cited LeBrun paper. Expectation: $(a,b)=(1/2,-6)$, giving $|\nabla W^+|^2=1/16$ at the target, not $1/24$. The ℂℍ² check does not decide this.
- **Derdziński factor.** Confirm from Derdziński (Compositio 49, 1983) that the conformal-to-Kähler factor is $\propto|W^+|^{2/3}$ (the Page/CLW metrics are the test cases: nonconstant $|W^+|$ ⇒ nonconstant factor). If confirmed, constant $|W^+|$ forces Kähler–Einstein, and §4's local contradiction is rigorous, overturning the "inherently global" conclusion.
- **Target relation.** Pin the exact LeBrun inequality and its equality case to decide whether the calibrated limit sits at $|W^+|^2=1/24$ (local contradiction fires) or at the Kähler value $2/3$ (no obstruction; limit is Einstein). This determines whether the noncollapsed case is already handled and the real open work is the collapsed regime.

The reusable structural lesson: the invariant object controlling this route is the *combination* (constant $|W^+|$) + (two-eigenvalue $W^+$) + (Einstein). Derdziński converts that combination directly into Kähler–Einstein rigidity, so the eigenvalue-magnitude constraint $|W^+|^2=s^2/24$ is automatic and pointwise — the Bochner inequality $|\nabla W^+|^2\ge0$ is strictly weaker and should not be read as "consistent, therefore possible."