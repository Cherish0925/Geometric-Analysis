# Step 10: Execute pivot — finite-cover reduction, Cheeger--Tian audit, and the real pinched-regularity bottleneck

Session: S0910A02. Agent1/Orchestrator. Phase: Explore evaluation after the required nine-step opening.

## 0. Target fidelity

The active target remains the full all-dimensional Yau Problem 26 statement.  Nothing in this note proves or refutes it.  The note evaluates whether A02 should now leave Explore and what the first Execute target should be.

The strongest A02 result so far is still four-dimensional and positive-sign:

\[
\|\operatorname{Ric}_g-g\|_{L^\infty,op}\le \delta<1/2,
\qquad \operatorname{Vol}(M,g)\ge v>0
\]

implies finite diffeomorphism types by Myers + Bishop--Gromov + Cheeger--Naber Theorem 1.12.  This is a noncollapsed theorem; it does not itself produce Einstein metrics on the resulting smooth manifolds.

## 1. Conditional finite-cover reduction from a simply-connected volume gap

The Strategist's finite-cover observation is mathematically sound, with two qualifications recorded below.

### Proposition 1.1 (conditional universal volume gap in dimension four)

Fix \(0<\delta_0<1/2\).  Suppose there exists \(v_0>0\) such that every closed simply connected smooth four-manifold \((X^4,g)\) satisfying

\[
\|\operatorname{Ric}_g-g\|_{op}\le \delta_0
\]

has \(\operatorname{Vol}(X,g)\ge v_0\).  Then there is \(v_1=v_1(\delta_0,v_0)>0\) such that every closed connected smooth four-manifold \((M^4,g)\), orientable or not, satisfying the same pinching has

\[
\operatorname{Vol}(M,g)\ge v_1.
\]

Consequently, the class of all such \(M\) has only finitely many diffeomorphism types.

### Proof

The positive pinching gives \(\operatorname{Ric}\ge (1-\delta_0)g>0\), hence Myers makes \(\pi_1(M)\) finite.  Let

\[
\pi:(\widetilde M,\widetilde g)\to (M,g)
\]

be the universal cover and let \(d=|\pi_1(M)|\).  The lifted metric satisfies the same pinching and \(\widetilde M\) is closed and simply connected, so by the assumed simply-connected gap,

\[
\operatorname{Vol}(\widetilde M,\widetilde g)\ge v_0.
\]

Apply the Step 9 noncollapsed finiteness theorem (Cheeger--Naber Theorem 1.12 plus Myers/Bishop) to the simply connected covers with lower volume \(v_0\).  Only finitely many oriented diffeomorphism types of \(\widetilde M\) occur; hence

\[
\chi(\widetilde M)\le X(\delta_0,v_0)<\infty.
\]

Because \(\widetilde M\) is simply connected and oriented,

\[
\chi(\widetilde M)=2+b_2(\widetilde M)\ge2.
\]

Euler characteristic is multiplicative under finite covers:

\[
\chi(\widetilde M)=d\,\chi(M).
\]

Since \(\chi(M)\) is a positive integer (the quotient of a positive Euler characteristic by a finite covering degree and still an integer), \(\chi(M)\ge1\), hence

\[
d\le \chi(\widetilde M)\le X(\delta_0,v_0).
\]

Therefore

\[
\operatorname{Vol}(M,g)=\frac{\operatorname{Vol}(\widetilde M,\widetilde g)}{d}
\ge {v_0\over X(\delta_0,v_0)}=:v_1>0.
\]

Now Theorem A applies directly to all orientable members of the class.  For nonorientable members, apply the same argument to the orientable double cover or use the finite universal-cover degree bound; equivalently the class has a uniform volume lower bound, diameter bound, Ricci bound, and hence finitely many underlying smooth types by the same Cheeger--Naber finite-type theorem after passing through orientable covers.  \(\square\)

### Qualifications

1. Cheeger--Naber gives finite diffeomorphism types, not an effective explicit list in our current records.
2. Finite diffeomorphism types do not themselves give Einstein metrics.  To prove \(P_4^+\), one still needs an approximate-to-exact bridge for each possible limiting type: smooth noncollapsed convergence is enough, but noncollapsed orbifold limits require desingularization/obstruction analysis, and total collapse requires the simply-connected volume gap above.

Thus the simply-connected volume gap is a genuine strengthening target because it removes the total-collapse hypothesis from the four-dimensional positive program, but it is not by itself Yau 26.

## 2. All-dimensional positive-collapse split by the universal cover

For any dimension \(n\), positive normalized pinching with \(\delta<1\) gives Myers, hence finite fundamental group.  Let \(\widetilde M\) be the universal cover.  Bishop gives a dimension-only upper volume bound

\[
\operatorname{Vol}(\widetilde M,\widetilde g)\le V_n(\delta).
\]

For a sequence \((M_i,g_i)\) with \(\|\operatorname{Ric}-g\|_{op}\to0\) and \(\operatorname{Vol}(M_i,g_i)\to0\), exactly the following alternatives may occur after passing to subsequences:

1. \(|\pi_1(M_i)|\to\infty\) while the universal covers stay noncollapsed or Einstein-compatible.  Round lens spaces and higher odd-dimensional spherical/Sasaki--Einstein quotients show this alternative is real and can be exactly Einstein.
2. The universal covers themselves collapse in volume.

Thus in general dimension the collapse goal can never be "collapse is impossible."  It must be: every collapse mechanism compatible with tight two-sided positive Ricci pinching is also compatible with an Einstein metric on the smooth topology, or can be ruled out by a dimension-specific invariant.  Dimension four is special because Euler characteristic interacts with finite covers and Cheeger--Naber finite type; higher dimensions lack the Step 8/9 CGB--Euler loop.

## 3. Cheeger--Tian / Li / Naber--Zhang source audit

A DOI/title-specific `knowledge_request` still did not retrieve the primary Cheeger--Tian JAMS paper.  I therefore used only source text actually available in Knowledge and kept the primary paper as a source gap.

### 3.1 What the secondary sources state about Cheeger--Tian

Ge--Jiang quote Cheeger--Tian as follows in `Knowledge/objects/papers/1707.05511-ε-regularity-for-shrinking-Ricci-solitons-and-Ricci-flows--77d745e7dfc7--9e2e179bf3bc/object.md`, lines 29--36:

\[
\text{Einstein four-manifold},\quad \operatorname{Ric}=\lambda g,
\quad |\lambda|\le3,
\quad \int_{B_r(p)}|\operatorname{Rm}|^2\le\varepsilon
\]

implies

\[
\sup_{B_{r/2}(p)}|\operatorname{Rm}|\le C r^{-2}.
\]

They emphasize that this theorem has **no volume noncollapse assumption**, and that the proof uses chopping, Chern--Gauss--Bonnet, Cheeger--Colding almost-cone theory, and the Einstein equation.

### 3.2 What survives for bounded Ricci alone

Two bounded-Ricci results are already locally available, and they separate the roles sharply.

**Li 2010 / Li II.**  The locally available Li continuation paper `Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md` states in its abstract and introduction (lines 23--50) that bounded Ricci plus no local curvature concentration can be smoothed without assuming noncollapse.  It quotes Cheeger--Tian's technical estimate and says Li generalized the scale-selection/chopping part to bounded Ricci: a volume-normalized local \(L^2\) curvature quantity is controlled and can be made small on a smaller comparable ball.  This is not the same as a direct pointwise curvature bound for the original metric.

**Naber--Zhang.**  `Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md`, lines 1437--1461, is decisive for the collapsed setting.  Proposition 6.4 gives lower harmonic radius on the local universal cover under bounded Ricci, residual dimension \(\ell\le3\), and maximal fibered nilpotency rank.  But Proposition 6.5 then says that a curvature bound follows from this harmonic-radius bound only if one assumes either

\[
\sup |\nabla\operatorname{Ric}|\le\Lambda
\]

or the metric is Einstein.  This is exactly the missing regularity in the Yau-26 hypothesis, which gives only \(L^\infty\) control of \(\operatorname{Ric}-g\).

### 3.3 Where the Einstein equation enters

The CT/Einstein input enters in the step that converts small \(L^2\) curvature and harmonic/Sobolev control into pointwise curvature control.  For Einstein metrics one has elliptic curvature equations schematically

\[
\Delta \operatorname{Rm}=\operatorname{Rm}*\operatorname{Rm}+\lambda\operatorname{Rm},
\]

and derivative estimates/Moser iteration apply.  For bounded Ricci only, harmonic coordinates give an elliptic equation for the metric with an \(L^\infty\) right-hand Ricci tensor, hence finite \(W^{2,p}\) and \(C^{1,\alpha}\) control where harmonic radius is known, but not \(W^{2,\infty}\), curvature supremum bounds, or estimates on \(\nabla \operatorname{Ric}\).  The divergence of Weyl involves derivatives of the Schouten tensor, so it cannot be used pointwise from \(C^0\) Ricci data; it can only be used after pairing against smooth test fields or adding a real regularizing mechanism.

This source audit changes the Execute target: do **not** assume a Cheeger--Tian pointwise \(\varepsilon\)-regularity theorem for \(C^0\)-Ricci-pinched metrics.  The first Execute work should either prove a carefully weakened substitute or produce a controlled counterexample to the too-strong version.

## 4. Why the naive simply-connected collapse contradiction is not yet a proof

The Strategist's finite-cover reduction is strong, but the suggested energy/F-structure route has an important gap.

For a four-dimensional metric with \(\operatorname{Ric}=g+E\), \(|E|\le C\delta\), and \(s=4+O(\delta)\), Chern--Gauss--Bonnet gives, in the usual full-curvature norm up to convention-dependent scalar coefficients,

\[
\int |\operatorname{Rm}|^2
=8\pi^2\chi(M)+O(\operatorname{Vol}(M))+O(\delta^2\operatorname{Vol}(M)).
\]

Thus for a **fixed topology** collapsed sequence, the total \(L^2\) curvature tends to a quantized topological value.  But a simply-connected volume-gap theorem must handle topologies with unbounded \(\chi\), such as the Sha--Yang family \(\#_k(S^2\times S^2)\).  Then \(\int|\operatorname{Rm}|^2\sim 8\pi^2\chi\) may be unbounded.  Cheeger--Tian-style chopping would bound the number of curvature-concentration balls by \(O(\chi/\varepsilon)\), not by a dimension-only constant.  The bounded-curvature collapsed complement can carry a positive-rank F-structure and zero Euler characteristic, while the many concentration regions can carry all of \(\chi\).  That is not a contradiction without a new localization theorem controlling the topology/energy of the concentration regions.

Also, in collapsed Ricci-flat or almost Ricci-flat four-dimensional geometry, the bubbles are often ALF/ALG/ALH rather than ALE.  Lott's K3 collapse discussion (lines 286--289 of `The-collapsing-geometry-of-almost-Ricci-flat-4-manifolds`) explicitly mentions Taub--NUT ALF bubbles and Ooguri--Vafa transition regions.  Therefore the Eguchi--Hanson ALE quantum \(12\pi^2\) is not the correct universal table in total collapse.

## 5. Execute target after this evaluation

The session should now transition to Execute, but the primary target should be the **pinched Cheeger--Tian / Li / Naber--Zhang infrastructure**, not the one-neck projection bridge in isolation and not a premature proof of the simply-connected volume gap.

The concrete Execute problem is:

> Determine the strongest true replacement for Cheeger--Tian \(\varepsilon\)-regularity under the Yau-26 hypothesis \(\|\operatorname{Ric}-g\|_{L^\infty}\le\delta\): does any useful pointwise curvature estimate survive, or only scale-selection, harmonic-radius-on-covers, smoothing, or test-field/projection estimates?

This problem is shared by the positive and negative branches:

- In the positive branch, it is the missing ingredient in any simply-connected volume-gap proof and in controlling collapsed high-\(\chi\) Weyl concentration.
- In the noncollapsed orbifold branch, it is the analytic core of the projection bridge: Ricci defects must be paired against smooth test data rather than differentiated.
- In the negative branch, Min--Oo escape and A01/A03's accessible-cover theorem both need to know when curvature concentration or fixed-scale cover harmonic charts can be forced from small calibrated defect.

### First Execute subtargets

1. **Refute or salvage the naive bounded-Ricci pointwise epsilon theorem.**  Try to build a local high-frequency transverse-traceless Weyl packet on a nearly constant-curvature background with \(\|\operatorname{Ric}-g\|_{L^\infty}=O(\delta)\), arbitrarily large \(|W|\), and arbitrarily small local \(L^2\) energy.  A rigorous construction or even a well-checked formal asymptotic expansion would prevent the session from chasing a false theorem.
2. **Extract the true Li/CT bounded-Ricci scale-selection theorem.**  Source-check Li 2010/II enough to state a precise proposition: bounded Ricci + small absolute local \(L^2\) energy implies a smaller comparable ball with small volume-normalized energy, but not necessarily curvature bound.
3. **Connect to Naber--Zhang accessible covers.**  Use Proposition 6.4 exactly at its scope: it gives harmonic radius on local covers under fixed-scale residual-dimension/model/rank assumptions; Proposition 6.5 shows why extra Einstein/\(\nabla\operatorname{Ric}\) data is needed for curvature bounds.
4. **Keep Proposition 1.1 as the positive branch amplifier.**  If a simply-connected volume gap is later proved by the corrected infrastructure, it immediately upgrades to universal noncollapse, finite diffeomorphism types, and collapse-side closure in dimension four.  But it should not be assumed.

## 6. Coordination proposal

A02 should tell A01/A03 that the shared infrastructure theorem is not "prove CT epsilon regularity for C0 Ricci" in the strong pointwise form.  The source-grounded version is a fork:

- either produce a counterexample to the strong pointwise statement (likely via high-frequency Weyl packets or known bounded-Ricci smoothing examples), then focus on weak/test-field regularity;
- or identify an additional pinching-specific structure absent from general bounded-Ricci metrics that restores enough curvature control.

A03's normal-cover mean transport and A01's accessible-cover reassessment should be used as the collapsed-interface side of the same project.  A02's role should be to own the positive-branch finite-cover amplifier and the analytic regularity/projection infrastructure, while preserving the all-dimensional limits of any four-dimensional success.
