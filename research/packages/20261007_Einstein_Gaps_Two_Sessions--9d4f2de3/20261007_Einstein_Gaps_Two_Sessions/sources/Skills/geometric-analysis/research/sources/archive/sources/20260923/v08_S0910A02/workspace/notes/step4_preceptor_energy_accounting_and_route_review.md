# Step 4 Preceptor review: four-dimensional pinching accounting, source gaps, and route discipline

Session: S0910A02. Agent4/Preceptor. Phase: Explore.

## 0. Target fidelity

The active target remains the full Yau Problem 26 proposition in the user statement: for every dimension `n >= 2`, decide whether there are constants `c_n < C_n` depending only on `n` such that any closed connected smooth `n`-manifold carrying a metric with

\[
 c_n g \le \operatorname{Ric}_g \le C_n g
\]

also carries some smooth Einstein metric, with no prescribed sign and no requirement that the Einstein metric be close to the input. The branch reduction still governs the logic: in fixed dimension, proving one sign-normalized branch `P_n^+` or `P_n^-` proves the interval statement in that dimension, while refuting the interval statement requires defeating both branches in the same dimension. A negative-branch LeBrun construction, even if successful, would not by itself refute `Q_4`; it would have to be paired with a positive-branch counterexample in dimension four.

The final completion standard has not changed: a complete mathematical proof or strict counterexample covering the exact proposition, followed by Lean 4 formalization/audit for the final theorem. The current session has not reached that level.

## 1. Small repair capped

Step 3's main correction remains valid. I repaired the remaining misleading endpoint in `Sessions/S0910A02/workspace/scripts/step3_corrected_lebrun_bounds.py` and regenerated `Sessions/S0910A02/workspace/data/step3_corrected_lebrun_bounds.json`. The scalar-only LeBrun estimate now records:

- corrected Einstein CGB:
  \[
  8\pi^2(2\chi+3\tau)=4\int |W^+|^2+\frac43\lambda^2V;
  \]
- for blow-ups `M=X#k CPbar^2`, the scalar-only contradiction begins at `p=k/A >= 2/3`, with the endpoint depending on LeBrun's strict inequality;
- the mixed LeBrun/Seiberg--Witten estimate gives, in the direct regime `1/3 < p < 1`,
  \[
  \frac{\delta}{1-\delta}\ge \sqrt{\frac{p-1/3}{2}}.
  \]

The hypothesis inventory is: closed oriented four-manifold with the relevant polarization/monopole-class input, complex orientation for the standard `X#k CPbar^2` application, `A=c_1^2(X)>0`, `T_+=A-k>0` for the displayed volume argument, and a separate strict/equality analysis at endpoints. If `b(\delta)=\frac23(1-\delta)^2-2\delta^2<=0`, then already `\delta >= 1/(1+sqrt3)`, stronger than the small-pinching window. On the positive-normalized branch for these general-type blow-ups, the statement is vacuous for `\delta<1` because positive pinching implies positive scalar/Ricci and the monopole obstruction already forbids it.

This repair is now capped: more LeBrun endpoint bookkeeping is lower value than the live global obstruction/existence questions.

## 2. Why the `p -> 1/3+` boundary cannot by itself refute `Q_4`

The refined LeBrun boundary remains mathematically interesting: if `delta_- -> 0` on no-Einstein blow-ups with `p=k/A -> 1/3+`, the mixed estimate is forced near equality. S0910A01's Step 4 note `Sessions/S0910A01/workspace/notes/step4_near_equality_and_boundary_calibration.md` gives a source-based equality mechanism: near equality should resemble an almost-Kähler structure with the almost-Kähler form in the lowest `W_+` eigenspace, `s+s*` constant, and exceptional classes forced toward zero symplectic area; exact equality is contradicted by Taubes's area theorem in the blown-up case. It also records the quantitative consequence

\[
D_a=I-\frac23(a^+)^2\le J-q,
\qquad q=k-A/3,
\]

so `delta_- -> 0` and `q/A -> 0` imply `D_a/A -> 0`; averaging sign choices forces `A^{-1}\sum_j(E_j^+)^2 -> 0` for actual pinched metrics.

But even a successful negative-branch construction at this boundary would not refute the original dimension-four statement. Refutation requires a positive-branch sequence on no-Einstein four-manifolds as well. The known positive-branch obstruction mechanisms do not currently provide such a sequence:

- On LeBrun/SW-type manifolds, `delta_+<1` implies `Ric>0` and hence positive scalar curvature, contradicting the nonzero Seiberg--Witten/monopole obstruction. Thus these same manifolds cannot refute `P_4^+`.
- Hitchin--Thorpe violating examples such as connected sums of `CP^2` are no-Einstein for Chern--Weil reasons, but the sign-blind pinching inequality forces strict `2 chi > 3|tau|` under sufficiently tight pinching, so those topologies are also excluded as arbitrarily tight positive-branch inputs.
- Positive Ricci existence on connected sums such as `#_k(±CP^2)` is a separate weak condition. The dossier's safe attribution is through Perelman/core-metric and Sha--Yang/Wraith/Reiser surgery literature; it does not give Einstein metrics or tight Ricci pinching. Reiser-style sources explicitly distinguish positive Ricci surgery/core metrics from Einstein existence.

Thus the counterexample program is gated by a genuinely new positive-branch no-Einstein obstruction compatible with `Ric ≈ +g`, or by a high-dimensional no-Einstein family with both branches defeated. The current record has neither. This is not proof of `Q_n`; it is a research allocation judgment and a guard against overvaluing the four-dimensional negative boundary.

## 3. Four-dimensional CGB/Weyl-energy accounting for both branches

Let `(M^4,g)` be closed; orientability is not essential for the Euler-form identity, and orientation/signature refinements require choosing an orientation. For either sign-normalized branch write Ricci endomorphism eigenvalues as

\[
\sigma + e_i,
\qquad \sigma\in\{+1,-1\},\qquad |e_i|\le \delta<1.
\]

Then

\[
|s|\ge 4(1-\delta),\qquad |\mathring r|^2=\sum_i(e_i-\bar e)^2\le \sum_i e_i^2\le4\delta^2.
\]

The four-dimensional Chern--Gauss--Bonnet identity in the full-Weyl convention is

\[
8\pi^2\chi(M)=\int_M\left(|W|^2+\frac{s^2}{24}-\frac{|\mathring r|^2}{2}\right)d\mu. \tag{GB}
\]

Hence, with

\[
b(\delta)=\frac23(1-\delta)^2-2\delta^2
          =\frac23-\frac43\delta-\frac43\delta^2,
\]

one obtains the sign-blind inequality

\[
\boxed{\int_M |W|^2\,d\mu + b(\delta)\operatorname{Vol}(M,g)
       \le 8\pi^2\chi(M).}\tag{1}
\]

The linear `O(delta)` term is real for the normalization `|Ric-σg|<=delta`; one can write `2/3-O(delta)` rather than `2/3-C delta^2` unless an additional scalar-centering normalization is imposed. The positivity window is

\[
b(\delta)>0 \iff \delta<\frac1{1+\sqrt3}.
\]

Consequences in this window:

1. **Euler positivity.** Any sufficiently tightly pinched four-manifold has `chi(M)>0`. Together with the `2chi>3|tau|` sign-blind version using `W^±`, this gives a second elementary topological filter independent of signature.

2. **Volume ceiling.**
   \[
   \operatorname{Vol}(M,g)\le \frac{8\pi^2\chi(M)}{b(\delta)}
   =12\pi^2\chi(M)+O(\delta)\chi(M).
   \]
   At `delta=0` this is exactly `Vol <= 12 pi^2 chi` for an Einstein metric with `Ric=±g`.

3. **Weyl deficit versus noncollapse, with two-sided constants.** From (GB), define
   \[
   B=\frac{s^2}{24}-\frac{|\mathring r|^2}{2}.
   \]
   Pointwise,
   \[
   b(\delta)\le B\le a(\delta):=\frac23(1+\delta)^2.
   \]
   Therefore
   \[
   \operatorname{Vol}\ge v \Longrightarrow
   \int|W|^2\le 8\pi^2\chi-b(\delta)v,
   \]
   while
   \[
   \int|W|^2\le 8\pi^2\chi-\eta \Longrightarrow
   \operatorname{Vol}\ge \eta/a(\delta).
   \]
   Thus, up to the natural `delta` constants, a volume lower bound is equivalent to a definite deficit of Weyl energy from the topological ceiling `8 pi^2 chi`. Collapse is exactly the regime in which `\int|W|^2` saturates the CGB budget.

4. **No bounded-curvature collapse in dimension four under tight pinching.** If additionally `|Rm|<=K`, then `|W|^2<=K^2` and `B<=a(\delta)`, so (GB) gives
   \[
   8\pi^2\chi(M)\le (K^2+a(\delta))\operatorname{Vol}(M,g).
   \]
   Since tight pinching already forces `chi>0`, there is a uniform positive lower bound
   \[
   \operatorname{Vol}(M,g)\ge \frac{8\pi^2\chi(M)}{K^2+a(\delta)}
   \ge \frac{8\pi^2}{K^2+a(\delta)}
   \]
   for orientable or nonorientable connected four-manifolds with integer `chi>=1` in this regime; in the positive branch on an oriented manifold, Bochner plus Poincare duality gives `b_1=0` and `chi=2+b_2>=2`. Hence four-dimensional collapse compatible with tight pinching must have curvature concentration. The bounded-sectional-curvature/F-structure intuition is the wrong model here; the remaining problem is collapse with Weyl energy concentrating to fill the entire `8 pi^2 chi` budget.

5. **Trace-free Ricci energy is small relative to the same budget.** The pinching and volume ceiling give
   \[
   \int |\mathring r|^2\le 4\delta^2\operatorname{Vol}
   \le \frac{32\pi^2\delta^2}{b(\delta)}\chi.
   \]
   Thus for fixed topology, near pinching makes full curvature energy approach `8 pi^2 chi`; for varying topology, energy can grow only with Euler characteristic. Nonflat ALE bubbles in a noncollapsed blow-up carry quantized positive energy, so any bubble-tree accounting must spend the same finite/topological Weyl budget rather than rely on unconstrained local handles.

This accounting unifies the positive-collapse and negative-bubbling questions in dimension four. The first-obstruction Calabi/Morteza--Viaclovsky analysis from Step 1 addresses exactly how an ALE-type local model can or cannot be reattached while preserving unweighted pointwise Ricci pinching. S0910A01's Taub--Bolt calibration further shows that local exact `Ric=-g` caps exist for their own boundary Cauchy data; the obstruction, if present, must be matching/global/near-equality, not a free local ansatz residual.

## 4. Literature status after renewed retrieval

I attempted another focused retrieval for Anderson 1989 and Ye 1993. The primary theorem texts were still not obtained. The returned and locally searchable evidence gives only bounded-scope information:

- `Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md` cites Anderson--Bando--Kasue--Nakajima: normalized **Einstein** four-manifolds with bounded diameter, volume bounded below, and bounded `L^2` curvature have subsequences converging to Einstein orbifolds with isolated singularities, with Ricci-flat ALE bubbles (lines 67--82). Ozuch's Theorem 0.2 then assumes an actual Einstein manifold with `Vol>=v0`, `diam<=D0`, and `|Ric|<=3` sufficiently GH-close to an Einstein orbifold, and concludes weighted-Hölder closeness to a gluing-perturbation model (lines 112--124). This is about exact Einstein metrics and noncollapsed degeneration, not a pure almost-Ricci-pinching existence theorem.

- `Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md` gives noncollapsed bounded-Ricci regularity: codimension-4 singular set for noncollapsed limits, `L^q` curvature estimates for `q<2`, and in dimension four local `L^2` curvature bounds/finiteness under `|Ric|<=3`, volume lower bound, and diameter bounds (lines 23--25, 95--113). These are regularity/finiteness tools under noncollapse; they are not an Einstein-existence theorem.

- Min-Oo's theorem remains the only source-grade almost-Einstein-to-Einstein result read directly here. It applies for `n>3` and negative average scalar curvature under `d^2 max|K| < Lambda^2`, with `epsilon=epsilon(n,Lambda)`, and uses Sobolev constants controlled by Ricci lower bound plus diameter. It is not dimension-only Ricci pinching.

- Kröncke's stability paper cites Ye 1993 as a stability result near existing Einstein metrics assuming positivity of an Einstein operator. Without Ye's original text, this cannot be used as a Yau26 theorem. The current evidence only supports treating Ye as a local/stability source, not as a global existence result from arbitrary tight Ricci pinching.

Therefore the exact gap to known literature is now sharper but still open: on the positive branch, Myers supplies a diameter bound and bounded Ricci automatically, but not a volume lower bound. Noncollapsed bounded-Ricci literature would become relevant once `Vol>=v` is known; Yau26 needs constants independent of such `v`, so the collapsed/Weyl-saturation regime is the missing case. On the negative branch, even diameter is missing, and Min-Oo additionally needed full sectional-curvature/diameter scale control, so a thick--thin/local-to-global argument would have to be stronger.

## 5. Route review and collaboration split

The strongest next research object is not another LeBrun census pass. It is the four-dimensional CGB/Weyl accounting plus the noncollapsed/collapsed almost-Einstein gap:

- **Positive existence route (`P_n^+`, with a 4D testbed).** Determine whether tight positive Ricci pinching plus the 4D Weyl-energy accounting forces either noncollapsed bounded-Ricci compactness leading to an Einstein metric on the same smooth manifold, or a collapsed curvature-concentration model whose topology is already Einstein-compatible. The first concrete proof target is a four-dimensional theorem excluding no-Einstein positive-branch sequences by showing Weyl-budget saturation yields either an orbifold/ALE gluing model with solvable Einstein correction or contradicts a topological/equality mechanism.

- **Negative boundary route (`P_4^-` refutation/proof discriminator).** The `p->1/3+` LeBrun boundary and S0910A01's near-equality analysis remain valuable, but only as a discriminator: does near equality under pointwise Ricci pinching quantitatively force the exact almost-Kähler/Taubes contradiction, or can exceptional topology collapse with `D_a/A->0`? This is not enough to refute `Q_4` unless the positive branch is also defeated.

- **Cap/matching route.** A local cap defect should include boundary metric and second fundamental form data, not just interior ansatz residual. Exact Taub--Bolt--AdS caps show zero interior defect for their own boundary data, so the useful question is whether the Cauchy data needed by the exterior/bubble tree lies in the attainable Einstein/near-Einstein cap set and whether transitions preserve unweighted Ricci operator pinching.

- **Source route.** Anderson 1989 Corollary B(4) and Ye 1993 remain source obligations. Since two focused retrievals in this step and earlier attempts failed, the next attempt should use library-style access, citation trails from Besse/Anderson surveys, or peer retrieval rather than repeating the same web query. Until then, do not cite them as theorem support.

Suggested split for the session group: A02 should develop the positive/existence-side four-dimensional Weyl-energy accounting and the Anderson/Ye source gap; A01 can continue the LeBrun near-equality/Taub--Bolt boundary calibration; A03 can independently probe local cap matching and corrected first-obstruction-zero gluing, while all sessions avoid reusing the withdrawn Weyl-only derivation or the false no-collapse slogan.
