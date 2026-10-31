# Step 73: global positive-branch allocation and all-dimensional proof architecture

Session `S0910A02`. Agent1 / Orchestrator. Phase Explore.

This note consolidates the Step-72 obstruction catalogue with the new Strategist correction. It is an allocation and theorem-architecture note, not a proof of Yau--26.

## 0. Exact target and branch logic

The active target remains the full Yau--26 proposition in the smooth closed connected category:

\[
Q_n:
\exists c_n<C_n\;\forall (M^n,g),\quad c_n g\le \operatorname{Ric}_g\le C_n g
\Longrightarrow M\text{ carries some Einstein metric.}
\]

For a fixed dimension, the same-sign normalization from Step 1 remains decisive. Define
\[
P_n^\sigma:\quad \exists \delta_n>0\; \text{such that }\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{op}\le\delta_n
\Longrightarrow M\text{ carries an Einstein metric},\quad \sigma=\pm1.
\]
Then \(Q_n\) is proved by either \(P_n^+\) or \(P_n^-\). A strict refutation of \(Q_n\) in dimension \(n\) must defeat both sign branches in the same dimension; in particular a branch-failure candidate must be a closed \(n\)-manifold with no Einstein metric of any sign and with near-pinched input metrics of the relevant sign.

The working consequence after Step 72 is:

- Positive-branch refutation is gated by a new no-Einstein obstruction compatible with the entire positive-pinched hypothesis class: positive scalar curvature, finite fundamental group, and \(b_1=0\) (plus strict Hitchin--Thorpe in four dimensions under tight pinching).
- In dimensions \(n\ge5\), the inspected literature has not supplied any concrete closed smooth manifold known to admit no Einstein metric of any sign. A high-dimensional no-Einstein example would be route-changing, especially if it were finite-\(\pi_1\)/PSC-compatible and could plausibly carry tight positive Ricci pinching. Without such an example, high-dimensional counterexample construction is not presently evidence-led.

This is not a theorem that counterexamples do not exist. It is a falsifiability gate and an allocation fact: the current record gives proof-side mechanisms but no certified refutation reservoir.

## 1. Positive pinching: dimension-general consequences

For every dimension, if
\[
\delta_+(g):=\|g^{-1}\operatorname{Ric}_g-I\|_{op}\le \delta<1,
\]
then, as recorded in `workspace/notes/step5_positive_branch_all_dimensions.md` lines 31--79,
\[
(1-\delta)g\le \operatorname{Ric}_g\le(1+\delta)g,
\qquad s_g\ge n(1-\delta)>0.
\]
Thus the metric has positive scalar and positive Ricci curvature. Myers gives
\[
\operatorname{diam}(M,g)\le {\pi\sqrt{n-1}\over \sqrt{1-\delta}},
\]
Bishop comparison gives a dimension/\(\delta\) volume upper bound by the corresponding round sphere, the universal cover is compact and hence \(\pi_1(M)\) is finite, and Bochner gives \(b_1(M)=0\). There is no dimension-only upper bound for \(|\pi_1|\) without a volume lower bound, as round lens spaces show.

In dimension four, Step 4 adds the sign-blind Chern--Gauss--Bonnet estimate. Writing Ricci eigenvalues as \(\sigma+e_i\), \(|e_i|\le\delta\),
\[
8\pi^2\chi(M)=\int_M\left(|W|^2+{s^2\over24}-{|\mathring r|^2\over2}\right)d\mu,
\]
and
\[
b(\delta):={2\over3}(1-\delta)^2-2\delta^2>0
\quad\Longleftrightarrow\quad
\delta<{1\over1+\sqrt3}.
\]
Consequently tight four-dimensional pinching forces \(\chi>0\), and the signature version gives strict Hitchin--Thorpe. This is four-dimensional accounting only; it should not be used as a dimension-general proof mechanism.

## 2. Why the refutation hemisphere is presently blocked

The all-dimensional part of the catalogue is the positive-pinning just stated: any positive-branch counterexample must be a no-Einstein manifold admitting PSC, positive Ricci at least for the input metric, finite \(\pi_1\), and \(b_1=0\).

The four-dimensional catalogue then becomes structural rather than family-specific. The known no-Einstein four-manifolds fall into mechanisms that cannot coexist with the tightly positive input:

- Hitchin--Thorpe violators are excluded by the pinching CGB estimate when \(\delta<1/(1+\sqrt3)\).
- Gromov/simplicial-volume/entropy obstructions are void for finite fundamental group; finite groups are amenable and give zero simplicial volume.
- LeBrun, Kotschick, Ishida--LeBrun, and Bauer--Furuta strict-Hitchin--Thorpe examples use Seiberg--Witten/monopole/Bauer--Furuta data. The source catalogue checked in Step 72 includes `Monopole-classes-and-Einstein-metrics...` and `Spin-Manifolds-Einstein-Metrics-and-Differential-Topology...`; their examples are explicitly monopole/Bauer--Furuta driven. Such data obstruct PSC by the Lichnerowicz--Weitzenböck mechanism, while positive pinching supplies PSC.

For \(n\ge5\), the strongest source anchors read in this step point the other way from refutation. `Einstein-Metrics-from-Symmetry-and-Bundle-Constructions-A-Sequel.../object.md` lines 316--318 says that in dimensions \(\ge5\) it is still unknown whether every closed manifold admits an Einstein metric and that there are no known general obstructions to existence; it also warns that homogeneous spaces with no invariant Einstein metrics may still admit non-invariant Einstein metrics. `Global-obstructions-to-conformally-Einstein-metrics-in-dimension-six.../object.md` lines 29 and 78--80 similarly says there are no known higher-dimensional obstructions and that the proposed six-dimensional diffeomorphism invariant has no known finite/nonpositive examples. Therefore current high-dimensional sources do not supply a closed no-Einstein reservoir for either sign branch.

The message to carry forward: counterexample construction in any dimension should not proceed by merely adding topology or symmetry unless it first passes one of two gates:

1. **PSC-compatible no-Einstein gate:** a new Einstein-nonexistence criterion compatible with positive scalar curvature, finite \(\pi_1\), and \(b_1=0\) (and in dimension four strict Hitchin--Thorpe).
2. **High-dimensional no-Einstein gate:** a concrete closed smooth \(n\ge5\) manifold known to admit no Einstein metric of any sign, with enough topology to attack at least one sign branch and, for positive-branch refutation, enough compatibility with the positive-pinning class.

Until such a gate opens, Yau--26 should be treated as a proof problem, with \(P_n^+\) the main all-dimensional route.

## 3. Positive proof architecture: subsequential split

For a sequence \((M_i^n,g_i)\) with \(\delta_+(g_i)\to0\), Myers and Bishop give uniform diameter and volume upper bounds. Hence every sequence has a subsequence in exactly one of two regimes:

\[
\operatorname{Vol}(M_i,g_i)\ge v>0
\quad\text{or}\quad
\operatorname{Vol}(M_i,g_i)\to0.
\]

The proof of \(P_n^+\) must handle both regimes.

### 3.1 Noncollapsed regime

Known bounded-Ricci regularity is useful but not a finished proof. Cheeger--Naber (`1406.6534.../object.md` lines 95--123) gives, under \(|\operatorname{Ric}|\le n-1\) and noncollapse, \(L^q\) curvature bounds for \(q<2\), codimension-four control of the bad set, and in dimension four an \(L^2\) curvature estimate and finiteness of diffeomorphism types. The Einstein or \(\nabla\operatorname{Ric}\)-bounded hypotheses are needed to upgrade harmonic-radius control to regularity-scale control. Thus mere \(C^0\) Ricci pinching still lacks an Einstein-like epsilon-regularity theorem.

The noncollapsed proof skeleton is:

1. Extract a Ricci-limit space and regular-set limit with \(\operatorname{Ric}=g\) in a weak/harmonic-coordinate sense.
2. If no curvature concentration or singular set remains, upgrade to a smooth positive Einstein metric on the recovered smooth manifold. This requires a genuine harmonic-coordinate elliptic bootstrapping argument for \(\operatorname{Ric}_{g_i}-g_i\to0\); it is plausible but should remain an explicit proof obligation.
3. If bubbling occurs, identify the correct obstruction datum and show tight pinching forces all obstruction coefficients/towers that prevent exact Einstein desingularization to vanish.
4. Use a desingularization/existence theorem (Biquard/Ozuch-type) to recover an exact Einstein metric on the same smooth manifold.

In dimension four, singularities are isolated under the noncollapsed/finiteness hypotheses, and the Biquard--Ozuch A\(_1\) analysis is the current laboratory. For \(n\ge5\), the generic singular set is codimension four rather than isolated; the proof must be written for strata or must explicitly state that isolated-singularity hypotheses are temporary.

### 3.2 Bubble trees and finiteness

The previous four-dimensional skeleton must make bubble trees visible. LeBrun--Ozuch's `Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds...` line 512 begins Section 9, `Without Trees of Singularities`, and lines 514--516 explicitly allow multiple singularities while excluding bubble trees. Lines 600--603 describe the later general case for conformally Kähler settings by replacing trees with a single Ricci-flat Kähler ALE approximation. The Yau--26 positive-pinching problem is not confined to that conformally Kähler/admissible scope. Therefore any current noncollapsed theorem should either assume no trees, or include a nested tower-subtraction/flux argument across all tree scales.

The correct finite-system statement in dimension four uses noncollapse plus Cheeger--Naber finiteness: fixed diffeomorphism type, fixed \(\chi\), and finite bubble count. Without noncollapse this finite obstruction system is not available.

## 4. General flux mechanism and the next Agent2 theorem

The manuscript `Skills/qiushi-yau26/references/research/20260912.tex` contains a dimension-general clean annulus flux proposition, not merely a four-dimensional identity. Lines 891--907 state:

- cone dimension \(d\ge4\) (there called \(n\));
- \(\Gamma\subset O(d)\) acts freely on \(S^{d-1}\);
- \(A=\{b<r<R\}/\Gamma\), \(L=\log(R/b)\);
- nonzero homogeneous quadratic \(\Gamma\)-invariant \(K\) with \(\operatorname{tr}K=\operatorname{div}K=\Delta K=0\), \(K(x,\cdot)=0\);
- dual tensor \(o=r^{-d-2}K\);
- if \(u\) interpolates from \(0\) to \(K\), then
\[
\int_A\langle D\operatorname{Ric}_e u,o\rangle=-{d+2\over2}I_K,
\qquad
\|D\operatorname{Ric}_e u\|_{op,\infty}
\ge{(d+2)I_K\over2LJ_K}.
\]
Lines 915--937 give nonlinear and weighted-energy versions.

This is the main proof-side asset that should now be developed in general dimension. The next theorem should not be a four-dimensional-only restatement. Agent2 should formulate a **mode-by-mode higher-obstruction flux necessity lemma** with cone dimension parameter \(d\ge4\): for a homogeneous TT/Bianchi mode of degree \(\ell\ge2\), the dual indicial root should be \(-((d-2)+\ell)\); equivalently if \(K_\ell\) is homogeneous of degree \(\ell\), the natural dual is
\[
o_\ell=r^{-(d-2)-2\ell}K_\ell,
\]
and the expected Wronskian coefficient is
\[
-{d+2\ell-2\over2}I_{K_\ell},
\]
specializing at \(\ell=2\) to the proved \(-(d+2)I_K/2\). This coefficient and the gauge-term cancellation must be proved, not assumed. The proof should track trace, divergence, harmonicity, radial-gauge boundary terms, endpoint errors, and nonlinear weighted-energy remainders.

### Isolated points versus strata: deliberate choice

For total dimension \(N\ge5\), Cheeger--Naber singularities are usually codimension-four strata, not isolated \(\mathbb R^N/\Gamma\) points. Therefore the correct notation should separate:

- \(d\): transverse cone dimension in the flux calculation;
- \(m\): stratum dimension;
- \(N=m+d\): total manifold dimension.

A two-tier theorem is the safest path:

1. Prove the general **isolated cone annulus lemma** for arbitrary \(d\ge4\). This is directly supported by the manuscript and is the clean analytic kernel.
2. State a **stratified product/bundle version** as the intended extension: local model \(S^m\times (\mathbb R^4/\Gamma)\) with an obstruction bundle over the stratum. The leading condition should be pointwise/elliptic along the stratum, not merely integrated.

Step 53's exact bounded probe (`workspace/data/step53_crepant_wall_and_stratum_probe.json`) already identifies the stratum object:

> bundle-valued pointwise/elliptic condition along S: R_normal,±(y) zeta(y) plus possible normal-connection/tangential derivative terms must vanish, rather than only an integral condition

It also records why the naive integral obstruction is too weak: Yau--26 pinching is a \(C^0\) pointwise operator norm, so a nonzero first-obstruction coefficient at one stratum point gives an \(O(1)\) Ricci-endomorphism defect on the corresponding ALE core; integration over the stratum cannot cancel it. Tangential variation of ALE parameters is itself dangerous: in the toy metric \(dy^2+a(y)^2dx^2\), \(K=-a''/a\), so scaling a fiber does not suppress curvature caused by \(O(1)\) variation in the base direction.

Thus Agent2 should write the lemma with strata in view from the beginning, but should not claim a full stratified ALE-bundle theorem until normal-connection, tangential-derivative, and parameter-parallelism errors have been controlled.

## 5. Collapse half

The collapse branch is the hardest part of \(P_n^+\). Positive Ricci collapse is real: exact Einstein lens/Kaluza--Klein examples from Step 24 show collapse cannot be forbidden abstractly. The proof question is whether tight positive collapse can occur on topologies lacking an Einstein metric, or whether collapse itself forces an Einstein-compatible structure.

In dimension four the CGB/chirality ledger supplies special instruments. Step 71/72 corrected the spin balanced row \(\#_3(S^2\times S^2)\): \(\chi=8\), \(\tau=0\), and in a \(\operatorname{Ric}\approx g\), \(\operatorname{Vol}\to0\) sequence
\[
\int |W|^2\to64\pi^2,
\qquad
\int|W^+|^2,\int|W^-|^2\to32\pi^2.
\]
The pure half-flat ADE atom gate is sporadic: integer targets reachable by pure ADE half-flat quanta are \(0,3,6,8\), and all checked integers \(\ge9\), so the blocked set is \(1,2,4,5,7\). For \(\#_k(S^2\times S^2)\), the chiral target is \(Q=k+1\), so the gate blocks only the corresponding sporadic \(k\)'s such as \(k=1,3,4,6\). It is a diagnostic, not a collapse theorem.

The finite next computation, when Agent3 receives it, is an atom table with chirality and APS boundary terms for Taub--NUT, multi-Taub--NUT, Euclidean Schwarzschild/Taub-bolt type models, Atiyah--Hitchin variants/quotients, and relevant ALF/ALG/ALH/Ooguri--Vafa transition models. Its value is not the \(\chi=8\) coincidence, but determining which atom sets can realize the general four-dimensional targets \((2\chi\pm3\tau)/4\) once eta terms and non-half-flat splitting are included.

For general dimensions, four-dimensional CGB accounting disappears. The durable analytic keystone remains: produce almost-Killing/nilpotent/collapsing structure and a concentration compactness/energy identity from only \(C^0\) Ricci pinching. Existing rod or graph-neck models should be treated as stress tests, not as the main all-dimensional proof unless they directly advance that keystone.

## 6. Lean formalization allocation

Step 71 showed that the locked Lean/Mathlib environment has Riemannian metric/manifold infrastructure but no usable visible Ricci/Riemann/scalar/sectional curvature layer under the searched names. `Step71Yau26SyntheticStatement.lean` is only an uninterpreted quantifier shell and must not be counted as formal progress toward the required proposition-consistency audit.

A bounded background Codex task should therefore attempt the reusable infrastructure work without consuming core mathematical steps: inspect Mathlib imports, identify whether true Levi--Civita/curvature APIs exist under non-obvious names, and if possible prototype a faithful curvature interface for the Yau--26 statement. If no real API exists, the worker should report that precisely and design the minimal layer; it should not produce another clean-auditing synthetic theorem.

## 7. Immediate queue

1. **Peer communication:** tell A01/A03 that negative IL/graph-neck progress may produce valuable restricted negative theorems, but cannot refute any \(Q_n\) while the positive branch lacks a PSC-compatible no-Einstein obstruction. The current allocation is proof of \(P_n^+\) in all dimensions, not more counterexample-family construction.
2. **Agent2 mathematical task:** formulate and begin proving the general cone/stratum-aware higher-obstruction flux necessity lemma. Use cone dimension \(d\) and total dimension \(N\) separately. Start from the isolated annulus identity, prove the mode coefficient and gauge cancellation, then state the stratified bundle extension with exact error terms and hypotheses.
3. **Agent3 later task:** after sources/formulas are assembled, build the ALF/non-half-flat atom table with APS eta and chirality split. Do not start another loose rod model before the atom-table inputs are source-pinned.
4. **Background Codex:** run a bounded Lean curvature-interface prototype; core agents should read its report later before using any artifact.

No branch of Yau--26 is proved or refuted by this note. The note changes allocation: current evidence makes the proof side, especially \(P_n^+\), the strongest target, with the general flux mechanism and Ricci-only collapse structure as the two central proof fronts.
