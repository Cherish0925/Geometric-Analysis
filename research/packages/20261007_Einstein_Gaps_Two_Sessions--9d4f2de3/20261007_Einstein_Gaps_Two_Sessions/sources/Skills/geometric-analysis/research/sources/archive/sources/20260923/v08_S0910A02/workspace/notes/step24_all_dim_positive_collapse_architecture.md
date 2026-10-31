# Step 24: all-dimensional positive-collapse architecture for Yau 26

Session S0910A02. Agent1/Orchestrator. Phase Explore.

## 1. Exact target and the class that must be understood

For each fixed dimension, write
\[
P_n^\sigma(\delta):\quad \|\operatorname{Ric}_g-\sigma g\|_{op}\le \delta
\Rightarrow M\text{ admits an Einstein metric},\qquad \sigma=\pm1.
\]
Apart from the degenerate case of an interval containing \(0\), which would force \(\mathcal E_n\) to be the class of all closed \(n\)-manifolds by rescaling arbitrary metrics, the interval version of Yau 26 is equivalent to proving, for each \(n\), one of the two normalized signs for some dimension-only \(\delta>0\). Thus
\[
Q_n\text{ is true if and only if either all closed }n\text{-manifolds lie in }\mathcal E_n,
\]
or, for some sign \(\sigma\in\{+,-\}\) and some \(\delta>0\),
\[
\mathcal P_n^\sigma(\delta)\subset \mathcal E_n.
\]
Here \(\mathcal P_n^\sigma(\delta)\) is the class of smooth closed \(n\)-manifolds carrying normalized \(\sigma\)-pinched metrics and \(\mathcal E_n\) is the class carrying some Einstein metric.  A refutation in a fixed dimension must defeat both normalized signs on no-Einstein underlying manifolds.  The current high-value work is to understand the left-hand class, especially for positive pinching.

The Anderson/Ye source obligation is now closed for route purposes.  `workspace/data/step23_classic_source_access_probe.json` and `workspace/data/step23_classic_open_api_probe.json` identify Anderson 1989 (JAMS, DOI `10.1090/s0894-0347-1989-0999661-1`) and Ye 1993 (Trans. AMS, DOI `10.1090/s0002-9947-1993-1108615-3`, JSTOR `2154433`), but AMS/JSTOR access returned challenge HTML rather than theorem text.  Anderson-type compactness under bounded Ricci, diameter and noncollapse is already superseded for our use by the directly read Cheeger--Naber/Naber--Zhang material in Steps 6 and 9.  A near-Einstein-to-Einstein deformation theorem is a local linearized/stability statement (modern accessible forms include Biquard--Kröncke--Ozuch) and cannot be invoked from mere \(C^0\) Ricci pinching without closeness to a fixed Einstein metric.  Ye's abstract-level statement concerns stable metrics or stronger space-form/sectional or critical-norm pinching; the Step-11 CZ spike shows that \(C^0\) Ricci pinching does not control the curvature information such theorems need.  No further AMS/JSTOR probing should shape the route.

## 2. What positive pinching already gives

If \(\|\operatorname{Ric}-g\|_{op}\le\delta<1\), then Ricci is positive: Myers gives a dimension-only diameter bound, Bishop gives a dimension-only volume upper bound, \(b_1=0\) by Bochner, and \(\pi_1\) is finite.  In dimension four, Chern--Weil optimization further gives \(\chi>0\), strict Hitchin--Thorpe for \(\delta<1/(1+\sqrt3)\), the \(\beta(\delta)\) volume/Weyl budgets, and Cheeger--Naber finite diffeomorphism type under a fixed volume lower bound.  In all dimensions, noncollapsed sequences have Cheeger--Naber regular Einstein limits off codimension-\(4\) singular sets, but this does not recover the topology or produce an Einstein metric on each input manifold.

Thus the positive branch is a collapse problem, not a compactness slogan.  Earlier notes sometimes treated collapse as the enemy because exact Einstein collapse exists.  The better formulation is: positive-pinched collapse must be either Einstein-compatible (finite quotients/products/Sasaki--Einstein-type total spaces, hence harmless for Yau 26) or obstructed by the approximate Kaluza--Klein equations.

## 3. Circle-collapse computation: the dimension-four obstruction does not generalize

For a constant-fibre principal circle metric, with circle parameter period \(2\pi\), connection form \(\alpha(\xi)=1\), \(d\alpha=\pi^*F\), and two-form norm \(|F|^2=\sum_{i<j}F_{ij}^2\), set
\[
g_t=\pi^*g_B+t^2\alpha^2,
\qquad U=t^{-1}\xi,
\qquad \phi=tF.
\]
O'Neill/Kaluza--Klein gives
\[
\operatorname{Ric}_M^H=\operatorname{Ric}_B-\tfrac12(\phi\circ\phi),\qquad
\operatorname{Ric}_M(U,U)=\tfrac12|\phi|^2,\qquad
\operatorname{Ric}_M^{mix}=\pm\tfrac12 d_B^*\phi .
\]
Therefore exact \(\operatorname{Ric}_M=g_M\) in this constant-length connection class is equivalent to
\[
|\phi|^2=2,
\qquad d_B^*\phi=0,
\qquad \operatorname{Ric}_B=g_B+\tfrac12\phi\circ\phi. \tag{KK}
\]
In addition \(d\phi=0\) holds automatically from \(dF=0\) and constant \(t\), not as a separate Einstein equation.  Step 6 used \(\dim B=3\), where \(\phi=*b\), to turn the automatic closure plus the mixed equation into a harmonic one-form and a Bochner contradiction; quantitatively it obstructs \(\delta<1/(1+\sqrt2)\) in that closed constant-length model.

The proposed extension to all odd-dimensional bases is false.  `workspace/scripts/step24_kk_circle_product_family_audit.py` and `workspace/data/step24_kk_circle_product_family_audit.json` check the exact algebraic family
\[
B=S^2_{\operatorname{Ric}=2}\times N^d_{\operatorname{Ric}=1},
\qquad \phi=\sqrt2\,\omega_{S^2}.
\]
It satisfies (KK) for every \(d\ge2\), where \(N\) must be a closed positive Einstein manifold normalized by \(\operatorname{Ric}_N=g_N\) (for example a round sphere of radius \(\sqrt{d-1}\)).  Taking a circle bundle with Chern number \(q\) over the \(S^2\) factor and fibre scale \(t=\sqrt2/q\) gives exact positive Einstein collapse on
\[
L(q,1)\times N^d,
\qquad n=d+3\ge5,
\]
for instance \(L(q,1)\times S^{n-3}\).  More explicitly, the metric is \((S^3(\sqrt2)/\mathbb Z_q)\times N\), a constant-curvature lens-space factor with \(\operatorname{Ric}=g\) times an Einstein factor with the same constant; the GH limit is \(S^2\times N\), fibre length is \(2\pi\sqrt2/q\), volume is proportional to \(q^{-1}\), and sectional curvature is uniformly bounded.  Taking \(d=0\) recovers the familiar three-dimensional lens collapse.  For \(d=1\) (total dimension four) the missing equation is \(\operatorname{Ric}_{S^1}=g_{S^1}\), impossible; Step 6 in fact proves the stronger statement for any closed three-dimensional base in this constant-length free-circle model.  Hence codimension-one positive Einstein collapse exists in \(n=3\) and every \(n\ge5\), but the Step-6 Bochner mechanism blocks the corresponding four-dimensional model.

The lesson is not that collapse defeats \(P_n^+\), but that the correct theorem must characterize compatible collapse rather than forbid it.

## 4. Higher-rank and singular collapse program

For abelian \(T^k\)-collapse with local metric
\[
g=g_B+h_{IJ}(d\phi^I+A^I)(d\phi^J+A^J),
\qquad w=\sqrt{\det h},
\]
Steps 12--17 verified the determinant trace in the tested settings (and a complete coordinate-free proof remains a useful future formalization target outside those settings):
\[
\operatorname{tr}_h\operatorname{Ric}^V
=-\frac{\Delta_Bw}{w}+\tfrac12|F|_h^2.
\]
In the exact positive Einstein case this is
\[
(-\Delta_B+\tfrac12|F|_h^2)w=k w . \tag{det}
\]
With a degeneration boundary, (det) gives the Dirichlet spectral/flux equations used in the toric four-dimensional work; in a free principal collapse there is no boundary, and integration yields an Einstein--Maxwell/Kaluza--Klein constraint instead.  The mixed equations are Yang--Mills/twist conservation equations, and the horizontal equations contain the base Ricci term, the curvature/twist energy, and the second fundamental form of the fibre metric.  These terms must be retained; the determinant trace alone is not the full collapse theorem.

For nonabelian nilpotent fibres, Milnor-type formulas suggest a strong obstruction: bracket-scale nilpotent directions have negative scalar curvature and Ricci eigenvalues of mixed sign, while almost-flat fibres have curvature tending to zero, not to the positive scale \(1\).  This makes it plausible that tight positive pinching forces the collapsing nilpotent structure to be abelian or to appear only in regions whose total space is already an Einstein-compatible quotient.  This is not yet a theorem under only bounded Ricci; Naber--Zhang provides almost-nilpotent fibre fundamental groups and noncollapsed covers under maximal-rank/local-model hypotheses, not a Cheeger--Fukaya--Gromov fibration with full curvature control.

## 5. Missing theorems and the next mathematical target

The most promising all-dimensional proof architecture for \(P_n^+\) is now:

1. **Collapse extraction under \(C^0\) positive Ricci pinching.**  From a collapsed sequence with \(\operatorname{Ric}\approx g\), obtain on regular regions local/orbifold nilpotent fibrations or covers with enough regularity to write the approximate KK equations for \((g_B,h,A)\), including second fundamental, mean-curvature and twist terms, and with controlled singular/fixed strata.
2. **Positive-pinching fibre forcing.**  Prove that nonabelian nilpotent bracket-scale collapse is incompatible with \(\operatorname{Ric}\approx g\), or else identify it as an Einstein-compatible quotient mechanism.  In the abelian case, use (det), Yang--Mills conservation and integrality of curvature classes to reduce to Einstein--Maxwell/Sasaki--Einstein-type lower-dimensional data.
3. **Induction/deformation of compatible collapse.**  Show that the approximate lower-dimensional Einstein--Maxwell or almost-Kähler--Einstein data can be promoted to an actual Einstein metric on the same total smooth manifold.  This is hard; it includes almost-KE-to-KE and topology recovery questions.
4. **Dimension four as the sharp test.**  Regular free circle collapse is blocked by the Step-6 Bochner/topology argument.  The remaining four-dimensional positive collapse is essentially the \(T^2\)-with-boundary/fixed-strata problem; the toric \(\alpha\)-family is the concrete adversary for the missing global determinant/horizontal/twist equations, not merely a side laboratory.

This program speaks to every dimension and uses only verified session assets.  It does not close Yau 26.  The Step-24 TTCS verification (`trace/ttcs/results/step24_ttcs01_verifier1_integration.md`) independently checked the KK correction and added the convention caveats above: two-form norm and circle period must be fixed, \(d\phi=0\) is connection closure, the real volume ratio includes a factor \(2\pi\), and the constructed family is the bounded-curvature space-form product \((S^3(\sqrt2)/\mathbb Z_q)\times N\).  The next mathematics should be a precise theorem in the positive branch: either an all-dimensional KK collapse-extraction/forcing lemma, or, more economically, the four-dimensional toric fixed-strata theorem defeating or realizing the \(\alpha\)-family.  The former has broader scope but depends on hard Naber--Zhang-to-KK regularity; the latter is narrower but already has explicit equations and adversaries.  Current best chance of rigorous completion remains the four-dimensional positive toric/fixed-strata problem, while the all-dimensional program should guide what such a theorem must generalize.
