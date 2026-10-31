# Step 8 Preceptor review: positive-branch corrections, Weyl-budget stress test, and bridge target

Session: S0910A02. Agent4/Preceptor. Phase: Explore.

## 0. Target fidelity and status

The active target is still the full Yau Problem 26 proposition: for every `n >= 2`, decide whether dimension-only constants `c_n < C_n` force any closed connected smooth `n`-manifold carrying `c_n g <= Ric_g <= C_n g` to admit some Einstein metric.  The branch reduction still governs all conclusions: proving one normalized sign branch `P_n^+` or `P_n^-` in each dimension would prove the corresponding interval statement, while a refutation in a fixed dimension must defeat both signs on a no-Einstein topology.  The present review concerns the four-dimensional positive branch as a testbed.  It is not a solution of the all-dimensional problem.

Step 7 was useful because it aimed at the real difficulty: four-dimensional positive pinching can have bounded Ricci and bounded diameter while Weyl curvature concentrates or collapse occurs.  But Step 7 also overclaimed three points: `det R_+=0` is not the same as Kähler-Einstein selection; `#_k(S^2 x S^2)` is not automatically an Einstein-output consequence of `P_4^+` unless tight metrics exist on that family; and C^0-pinched epsilon-regularity is central but not the only uniformity gap.

## 1. Review question 1: Euler obstruction to free collapse

The valid statement is even simpler than Step 7 wrote.  If `|Ric_g-g|_op <= delta < 1` on a closed oriented four-manifold, then `Ric_g > 0`.  Bochner gives `b_1=0`, hence by Poincare duality

\[
\chi(M)=2+b_2(M)\ge 2.
\]

Equivalently the Step-4 CGB inequality also gives `chi>0` for `delta<1/2`.  Any free smooth `S^1` action on a closed manifold has empty fixed set and therefore `chi(M)=chi(M^{S^1})=0`; in the principal-bundle case this is also `chi(B^3) chi(S^1)=0`.  Thus global regular free circle collapse is impossible in dimension four under tight positive pinching.

This does **not** exclude the collapse regimes relevant to Yau 26.  It misses actions with fixed sets, singular orbit strata, orbifold quotients, rank drop, local `F`-structures without a global free action, and collapse with curvature concentration.  It also has no direct odd-dimensional analogue: round lens spaces and many Sasaki-Einstein quotients collapse with exact positive Einstein metrics.  The right all-dimensional statement, if true, would be that compatible collapse is already Einstein-compatible, not that collapse is impossible.

## 2. Review question 2: CGB gives both upper and lower curvature-energy bounds

Assume now a closed oriented four-manifold in the positive normalized branch:

\[
\|Ric_g-g\|_{op}\le \delta <1/2.
\]

Let `E=Ric^0` and `s` be scalar curvature.  The Chern--Gauss--Bonnet identity is

\[
8\pi^2\chi(M)=\int_M\left(|W|^2+{s^2\over24}-{|E|^2\over2}\right)d\mu .\tag{GB}
\]

The known Step-4 lower coefficient for
`B=s^2/24-|E|^2/2` is

\[
\beta(\delta)=
\begin{cases}
{2\over3}(1-\delta)^2,&0\le\delta\le1/3,\\[1mm]
{2\over3}(1+\delta)(1-2\delta),&1/3\le\delta<1/2.
\end{cases}
\]

Thus

\[
\int |W|^2+\beta(\delta)\operatorname{Vol}\le 8\pi^2\chi .\tag{2.1}
\]

This gives an upper curvature-energy budget and, with the standard norm convention

\[
|Rm|^2=|W|^2+2|E|^2+{s^2\over6},
\]

the exact identity

\[
\int |Rm|^2
=8\pi^2\chi+{5\over2}\int |E|^2+{1\over8}\int s^2 .\tag{2.2}
\]

Since `|E|^2 <= 4 delta^2` and `s^2 <=16(1+delta)^2` pointwise, Bishop's positive-branch volume ceiling

\[
\operatorname{Vol}(M,g)\le {24\pi^2\over(1-\delta)^2}
\]

gives the sharper positive-branch bound

\[
\int |Rm|^2
\le 8\pi^2\chi(M)
+\left(10\delta^2+2(1+\delta)^2\right){24\pi^2\over(1-\delta)^2}.\tag{2.3}
\]

At `delta=0` this is sharp for round `S^4` with `Ric=g`: `Vol=24 pi^2` and `int |Rm|^2=64 pi^2`.

The Strategist's main correction is the **lower** Weyl-energy bound.  From (GB),

\[
\int |W|^2
=8\pi^2\chi-\int{s^2\over24}+{1\over2}\int |E|^2
\ge 8\pi^2\chi-{2\over3}(1+\delta)^2\operatorname{Vol}.
\]

Using Bishop,

\[
\boxed{\int_M |W|^2\,d\mu
\ge 8\pi^2\left[\chi(M)-2\left({1+\delta\over1-\delta}\right)^2\right].}\tag{2.4}
\]

This is sharp at round `S^4`, where `chi=2` and both sides vanish.  For

\[
M_k=\#_k(S^2\times S^2),\qquad \chi(M_k)=2+2k,\quad \tau=0,
\]

(2.4) gives

\[
\int |W|^2\ge 16\pi^2 k-O_\delta(1),\tag{2.5}
\]

and exactly `16 pi^2 k` at `delta=0`.  Since the volume is bounded above by the round `S^4` value plus the `(1-delta)^{-2}` factor, the mean `|W|^2` is forced to grow like `k`; if this energy is spread at Ricci scale, the associated curvature length scale is `k^{-1/4}`.  This is a necessary condition on any tight positive-pinching metrics on high-`b_2` examples, not just a permissive budget.

Reproducible constants are in `Sessions/S0910A02/workspace/scripts/step8_weyl_budget_positive4.py` and `Sessions/S0910A02/workspace/data/step8_weyl_budget_positive4.json`.  The script records, for example, that at `delta=0`, `#_2(S^2 x S^2)` requires `int|W|^2 >= 32 pi^2`, while `#_100(S^2 x S^2)` requires `>=1600 pi^2` inside `Vol<=24 pi^2`.

Consequences for the Step-7 thick--thin claim:

* C^0-pinched epsilon-regularity is a central analytic bottleneck, but it is not literally the only unknown in the full uniform problem.  High `chi` allows arbitrarily many concentration sites, collapse/unwrapping must still be controlled, and topology recovery from a pinched (not exact Einstein) limit is separate.
* A fixed-topology noncollapsed sequence has enough bounded data to seek an orbifold/ALE description.  A uniform theorem over `#_k(S^2 x S^2)` as `k->infty` cannot assume noncollapse or bounded energy independent of `k`; the Weyl lower bound shows high topology must be paid for by many units of curvature energy or by collapse.
* Cheeger--Naber Theorem 1.13 gives local `L^2` curvature and weak harmonic-radius control under bounded Ricci and noncollapse in dimension four; it does not by itself give pointwise regularity or gluing normal form for arbitrary C^0-pinched metrics.  On harmonic-radius patches, however, `Ric_g -> g` passes through the harmonic-coordinate elliptic equation to a smooth local Einstein limit, as A01/A03 have now used in the negative branch.

## 3. Review question 3: obstruction-amplitude principle and source scope

The TTCS-verified part of Step 7 is sound within the Biquard--Ozuch/Eguchi--Hanson gluing normal form.  If on a core

\[
Ric(g_t)-\Lambda g_t=t\mathcal O_p o+Q_t,
\qquad |Q_t|_{g_{EH}}\le C t^2\rho^2,
\qquad g_t=t(g_{EH}+O(t\rho^2)),
\]

then raising an index by `g_t^{-1}` makes `Q_t` small (`O(t)` in the fixed core, `O(t^{1/2})` in the transition), while the nonzero non-scalar obstruction term has order-one operator norm.  The precise lower bound is the spectral spread estimate

\[
\inf_{a\in\mathbb R}\|t\mathcal O_p o-a g_t\|_{op,g_t}
\ge c|\mathcal O_p|-o(1).
\]

Multiple singularities cannot cancel a `C^0` pointwise defect, and higher-order terms are lower order as long as the first obstruction coefficient stays nonzero.

The unsupported step is the passage from an arbitrary noncollapsed `C^0`-pinched sequence to this normal form.  Ozuch's normal-form theorem is for **exact Einstein** metrics sufficiently GH-close to an Einstein orbifold; Cheeger--Naber gives harmonic-radius patch information under bounded Ricci but not the weighted gluing expansion.  Thus the currently justified conditional statement is:

> If a C^0-pinched noncollapsed sequence is known, by some separate theorem or argument, to have an orbifold/ALE neck with the same first-obstruction projection as in the Biquard--Ozuch normal form, then pinching forces that projected first obstruction to vanish up to `O(delta_i)`.

The determinant correction is essential.  In four dimensions, for `Ric=g` and the orientation selected by an Eguchi--Hanson bubble,

\[
R_+=W_++{1\over3}I,
\qquad \det R_+=0 \Longleftrightarrow \text{one eigenvalue of } W_+ \text{ is } -1/3.
\]

Kähler-Einstein metrics have spectrum `(2/3,-1/3,-1/3)` and hence satisfy this condition, but the condition alone is weaker.  A trace-free spectrum such as `(1/3,0,-1/3)` also gives `det R_+=0` and is not Kähler-Einstein.  Therefore Step 7's sentence that the determinant condition "precisely selects Kähler-Einstein geometry" is false and has been patched in the Step-7 note.

Actual sources give the following stronger but narrower facts:

* Ozuch's `Higher-order obstructions...` states for exact Einstein GH desingularizations of `R^4/Z_2` singularities that either `det R_+` or `det R_-` vanishes; under additional stability/rigidity assumptions the curvature block has the more special matrix form `diag(0,0,Λ)` in the relevant orientation.  This is still an exact-Einstein compact-boundary result.
* LeBrun--Ozuch `Desingularizations of Conformally Kähler, Einstein Orbifolds` Theorem B applies to positive Einstein four-orbifold limits that are already Hermitian and to admissible exact Einstein sequences whose Ricci-flat ALE bubbles are anti-self-dual in the induced orientation.  Then the smooth metrics are eventually Kähler-Einstein and the limit is among Odaka--Spotti--Sun Kähler-Einstein orbifold limits.  It does not say that `det R_+=0` alone makes the limit Hermitian, nor does it apply directly to merely C^0-pinched sequences.
* Yichen Yao's general-dimensional theorem is for negative Einstein orbifolds admitting noncollapsed **Einstein** resolution sequences with critical energy bounds and a smooth ALE blow-up.  The obstruction links the negative Einstein constant, the ALE renormalized volume, and a contraction of orbifold Weyl curvature with asymptotic Weyl curvature.  It is valuable as an all-dimensional analogue of first-obstruction projection, but it does not transfer the current four-dimensional positive-branch argument to all `n`.

## 4. A bridge stated so C^0 Ricci data could suffice

The most valuable technical object is no longer to assert the gluing normal form; it is to replace it by a local projection/flux identity whose error only contains the Ricci defect in `L^\infty` paired with smooth test data.

A useful schematic formulation is this.  Suppose a pinched sequence has, after rescaling near a concentration point, a neck separating an orbifold scale from an ALE bubble scale, with `C^{1,alpha} cap W^{2,p}` control good enough to define approximate Bianchi/ALE coordinates.  Let `\phi_i` be a cutoff approximate cokernel tensor obtained from the relevant ALE infinitesimal Einstein deformation (or equivalently from a Komar/rotation-field flux).  A self-adjoint linearized Einstein identity should give

\[
\int_{\Omega_i}\langle Ric(g_i)-g_i,\phi_i\rangle\,d\mu_{g_i}
= t_i\,\mathcal O(R_+(p),\text{orientation},\text{ALE asymptotics})+o(t_i),\tag{4.1}
\]

where `t_i` is the gluing scale.  Since `||Ric-g||_{op}<=delta_i`, and the model scaling gives `||\phi_i||_{L^1}=O(t_i)`, the left side is `O(delta_i t_i)`.  Dividing by `t_i` forces the first obstruction to be `O(delta_i)+o(1)` and hence to vanish in the limit.  No derivative of the Ricci defect is needed; any integration by parts moves derivatives onto the smooth approximate test field:

\[
\int\langle \nabla E,T\rangle=-\int\langle E,\nabla T\rangle.
\]

In Komar language, for an approximate rotation Killing field `X` on a cone annulus, the flux `\int_{\Sigma_r} *dX^\flat` is conserved for an exact Einstein metric up to the explicit Einstein-constant volume term.  For a pinched metric, the flux difference across the annulus is an `O(delta_i)` pairing plus an error from `X` not being exactly Killing, controlled by annular `C^{1,alpha}` closeness to the cone.  Inner and outer flux asymptotics should reproduce the Biquard/Ozuch first obstruction.

This bridge has precise failure modes: construction of gauges and test tensors, multiple scales/bubble trees, rank-drop or singular collapsed strata, uniform control of `||phi_i||_{L^1}`, and showing annular closeness from C^0 pinching plus finite energy.  It is nevertheless the right target because it attacks the normal-form gap without demanding `\nabla Ric` estimates.

## 5. Review question 4: the `#_k(S^2 x S^2)` calibration is a uniformity stress test, not an automatic consequence

The family

\[
M_k=\#_k(S^2\times S^2),\qquad \chi=2+2k,
\qquad \tau=0,
\]

is important because Sha--Yang/Burdick/Perelman-type constructions give positive Ricci metrics for all `k`, while Einstein existence is unknown for `k>=2`.  But positive Ricci alone is far weaker than tight positive pinching.  `P_4^+` would imply an Einstein metric on `M_k` only if some metric on `M_k` satisfies the unknown dimension-only pinching threshold.  Therefore Step 7's unqualified phrase "a proof of P_4^+ would produce Einstein metrics on #_k(S^2 x S^2) for all k" was too strong.

The corrected calibration is sharper and more useful:

* If `delta_+(M_k):=inf_a ||Ric-a g||/a` (or an equivalent normalized infimum) has a positive lower bound independent of `k`, then high connected-sum topology is excluded from tight pinching and this supports the positive branch by a new pinching-rigidity theorem.
* If instead `delta_+(M_k)->0` along some construction, then Yau 26 would force Einstein metrics on a family where no such metrics are known; failure of Einstein existence would refute `P_4^+`.
* Any such tight metrics must satisfy the forced Weyl lower bound (2.5), so the construction cannot be near-round with small total curvature.  It must build approximately Ricci-isotropic metrics with Weyl energy `~16 pi^2 k` inside bounded volume, i.e. many ALE-scale concentration regions or collapsed/singular docking geometry.

Thus `#_k(S^2 x S^2)` is not a side example.  It is the positive branch's uniformity failure mode: any dimension-only `delta_4` must survive Euler characteristic going to infinity while volume stays Bishop-bounded.

There is a plausible but unproved closing chain suggested by the current assets: high-`chi` tight metrics force many Weyl/ALE concentration sites; a pinched orbifold/ALE bridge forces first obstructions to vanish; LeBrun--Ozuch/Ozuch rigidity might then push an admissible exact-Einstein-style limit toward Hermitian/Kähler-Einstein geometry; complex-surface constraints would obstruct many `#_k(S^2 x S^2)` diffeotypes.  Every arrow in this chain currently needs proof for pinched rather than exact Einstein sequences, especially collapse and diffeomorphism-type recovery.

## 6. Review question 5: current gap structure

A faithful positive-branch gap structure is:

1. **Regular free collapse in dimension four:** global free `S^1` collapse is excluded by Euler characteristic; constant-fibre-length principal connection models are independently Bochner-obstructed (Step 6).  This is not a general collapse theorem.
2. **High-topology Weyl concentration:** the lower bound (2.4) shows large `chi` compels large Weyl energy at bounded volume.  This is the key new correction to Step 7.
3. **Noncollapsed bounded-topology concentration:** Cheeger--Naber gives regular harmonic patches, but a full orbifold/ALE bubble tree for C^0-pinched metrics still needs proof or a source-grade theorem.  Classical Anderson--BKN/Ozuch normal forms are exact-Einstein results.
4. **First-obstruction projection:** within normal form, the C^0 obstruction-amplitude argument is correct; outside normal form, build the integral Pohozaev/Komar projection (Section 4).
5. **Higher-order obstructions and topology recovery:** first-order vanishing does not by itself produce an Einstein metric on the original smooth manifold.  Ozuch's exact-Einstein theory has higher-order and global conditions.
6. **General collapse/unwrapping:** Naber--Zhang maximal-rank local covers give harmonic/conjugate radius under hypotheses, but one still needs deck-averaged defect transport and handling of rank drop/singular strata.  A03's negative-branch orbit-volume theorem is a useful analogue: exact negative Einstein regular free abelian collapse is excluded by a strict subharmonic orbit-volume equation, leaving nilpotent and singular cases.
7. **All dimensions:** the four-dimensional Euler/CGB/Weyl budget has no direct analogue in `n>=5`.  Yao's general-dimensional obstruction is a negative-Einstein exact-resolution theorem under noncollapse/energy/ALE hypotheses; it is a guide to the type of first-obstruction identity one might seek, not a solution of Yau 26.

## 7. Peer assimilation

A01/A03 have repaired the negative LeBrun boundary route.  The Derdziński factor is now primary-source checked: if `delta W^+=0` and `W^+` has at most two eigenvalues, `(24|W^+|^2)^{1/3}g` is locally Kähler; at the calibrated constant spectrum the factor is constant, forcing a local contradiction with the Einstein-Weyl identity.  For varying topology this gives only a volume-proportion exclusion of noncollapsed regions, not a pointwise no-noncollapse theorem.  A03's orbit-volume equation for exact negative Einstein regular abelian collapse further excludes abelian collapse on parabolic bases; nil^3 and singular strata remain.

The positive branch should import the method, not the conclusion: use local averaging, harmonic-coordinate passage, and deck/cover defect transport to test special curvature profiles on unwrapped charts.  The profile is different: in the positive orbifold route the candidate obstruction is `R_+`/ALE first-obstruction data rather than the negative LeBrun calibrated `W^+` spectrum.

## 8. Next concrete work

The next highest-value work is constructive, not final expression:

1. Build the local first-obstruction projection identity (Section 4) in a simplified four-dimensional `R^4/Z_2` Eguchi--Hanson neck.  State the exact scaling of the test tensor, the boundary fluxes, and the `O(delta t)` error from `||Ric-g||_{L^\infty}`.  This should be done before attempting a full collapsed theorem.
2. In parallel, quantify the Weyl-budget stress test for explicit Sha--Yang/Burdick/Perelman docking metrics on `#_k(S^2 x S^2)`: estimate or compute `Vol`, `int|W|^2`, and the Ricci eigenvalue spread.  The lower bound (2.5) is the necessary benchmark any construction must meet.
3. Keep source scope strict: LeBrun--Ozuch and Yao apply to exact Einstein/admissible resolution sequences; any use for C^0-pinched metrics requires the projection bridge or a new compactness theorem.

No current result proves or refutes Yau 26.  The Step-8 contribution is to correct the positive-branch program, identify forced high-`chi` Weyl concentration, and isolate the Pohozaev/Komar projection as the next bridge that can be attacked mathematically.
