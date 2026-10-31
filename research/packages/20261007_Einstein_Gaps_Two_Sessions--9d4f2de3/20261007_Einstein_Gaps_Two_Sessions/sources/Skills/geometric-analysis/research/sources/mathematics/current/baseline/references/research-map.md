# Research Map: Ricci Pinching and Einstein Metrics

This map locates mathematical statements, proofs, constructions, computations, failed methods, and open questions. Topics are expandable navigation, not a count of original results. Related lemmas remain in their proof chains.

Set $\delta_\sigma(g)=\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{\infty,\mathrm{op}}$. In a fixed dimension the working interval statement is $Q_n\Longleftrightarrow P_n^+\lor P_n^-$. The output may be any Einstein metric on the same smooth manifold. Disproof requires both signs in one fixed dimension, with different manifolds allowed for the two sequences. Historical problem text and the expressly adopted working formulation remain distinct.

“Full argument” means that a statement and its argument appear under the specified hypotheses; “merged” means that a repeated or weaker version is incorporated into a later one; “model” specifies a restricted geometric, algebraic, or numerical setting; “withdrawn” identifies an invalid inference and its replacement; “open” identifies a missing mathematical step.

## Three connected lines and their papers

| Line | Mathematical question | Papers and complementary material |
| --- | --- | --- |
| Rigidity | How does topological near-equality force a local contradiction, uniformly across a family? | U: general monopole/Euler gap and blowup application. R: calibration, unfolding, necessary degeneration, spinors, local flows. |
| Pointwise construction | How can the Ricci defect tend to zero on fixed smooth topology, and when can the residual be repaired? | C: both A1/log-Weyl and $E_D$ constructions, flux, spectra and exact repair. L: full extended derivations. |
| Global Einstein existence | Does the same smooth manifold carry any Einstein metric, regardless of sign, complex structure, or adaptation? | G: $E_D$ attainment, graph connectors, algebraic smoothing, toric topology and higher dimensions. C and L retain explicit algebraic examples. |

The lines share foundations, computations, and local tools. They neither partition every result into disjoint classes nor assign fixed Session roles or a priority order. The A1 and surface-bundle constructions are separate arguments; the latter also supports the global variational results. Paper boundaries follow mathematical dependencies, not the number of research lines.

| Key | Local text | Content |
| --- | --- | --- |
| F | [Problem and foundations](../research/20260910.tex) | Quantifiers, classical methods, hypotheses, and the analytic repair argument |
| L | [Extended constructions and analysis](../research/20260912.tex) | Full cumulative manuscript from the uploaded synthesis |
| U | [Uniform topological gap](../research/20260916_uniform_gap.tex) | Dedicated proof manuscript |
| R | [Rigidity and degeneration](../research/20260916_rigidity.tex) | First scientific line, including the detailed Session arguments |
| C | [Pointwise near-Einstein construction](../research/20260916_construction.tex) | Second line, including two distinct core constructions |
| G | [Global geometry and topology](../research/20260916_global.tex) | Third line, organized by the actual smooth objects |

Use the displayed TeX labels to locate arguments; line numbers change with editing. U/R/C/G and this map are English research texts. F/L and the historical appendices retain the original language and complete derivations. The three supplementary scientific-line manuscripts and the final `yau26_3mainline.md` uploaded on 2026-09-17 are integrated into the corresponding papers, not installed as a second set of parallel summaries.

A01, A02 and A03 denote S0910A01, S0910A02 and S0910A03. Their Step numbers are separate timelines. Sections 1–322 in the web accumulation are manuscript sections, not Session Steps. Uploaded material comes from A03's briefing; its progress archive, full research archive, cumulative manuscript, separate uniform-gap proof, and two sets of three-line manuscripts contribute different mathematical content. The source index retains the correspondence.

## 1. Exact-Einstein uniform topological gap

The general statement in U, under $\mathrm{MP}(A)$ and $\chi(M)\le LA$, is
$(2\chi+3\tau)/A\ge2/3+\eta(L)$ for every Einstein metric, with $\eta(L)>0$.
Here $\mathrm{MP}(A)$ requires $b_+>1$ and, for each metric, an applicable monopole class whose self-dual projection has square at least $A$. R `def:MP`, `thm:relative-gap`, `sec:relative-proof` and `sec:relative-application` now give this general input, full local proof and blowup application consecutively. R `cor:Euler-escape` records the resulting necessary relative-Euler divergence near the critical value.

The blowup application is U `thm:intro-exact` and R `thm:topgap`: for a minimal surface of general type $X$, $b_+(X)>1$, $A=c_1^2(X)>0$, some nonexplicit $\gamma>0$ independent of $X,k$ excludes every Einstein metric on $X\#k\overline{\mathbb{CP}}^2$ when $k\ge(1/3-\gamma)A$.

The reusable proof is in U: `eq:budget-general` for calibration; `lem:fubini` for selection; `lem:transfer` for buffered local-isometry unfolding and multiplicity; collapse-tolerant small-energy regularity for exact Einstein metrics; and `lem:forbidden` for the impossible local spectrum. The classical blowup obstruction and Noether inequality establish $L=42$ before the new gap is applied. Uniformity is across the family, not merely strictness for each $X$.

Source: the separate uploaded U manuscript; A01 Steps 4–14 and A03 Steps 3–12 supply related near-equality and unfolding work. The exact theorem does not use (SC). U `prop:conditional` assumes the additional uniform weak-harmonic-chart property for arbitrarily collapsed bounded-Ricci inputs. Failure to establish (SC) does not invalidate the exact theorem; the exact theorem does not establish the unrestricted near-Einstein gap.

## 2. Log-Weyl construction on fixed A1 resolutions

Full arguments: L `FND:A1construction`, `FND:Hstar`, `FND:logoperator`; C `thm:A1` and its construction sections. Fix the closed Einstein four-orbifold, nodes, orientation, end markings and EH fillings. The corrected core solves $D\operatorname{Ric}_{g_{EH}}\widetilde h=g_{EH}$. In a common radial gauge, the quadratic difference $K$ lies in the Weyl part of the Ricci kernel, with

$$D\operatorname{Ric}_e[\eta(\log r)K]=-\frac{\eta''+6\eta'}{2r^2}K.$$

The nonlinear estimates on core, logarithmic annulus and exterior cutoff yield $\delta_\sigma(g_a)\le C/|\log a|\to0$ on a fixed smooth resolution, together with the exterior GH limit and rescaled EH-core limit. This is the unweighted pointwise endomorphism norm, not merely a finite-$L^p$ residual.

C `sec:exact-desingularization` compares the finite-$L^p$ result, logarithmic cutoff, and pointwise endpoint question in Ozuch's noncollapsed-degeneration paper. C `sec:football-comparison` and `cor:football-separation` specify the two-pole spherical quotient and prove, under the stated marked-resolution hypotheses, the contrast between pointwise approximate realization of its GH limit and the obstruction to any exact normalized Einstein sequence with that limit. The scaling from $\operatorname{Ric}\approx g$ to $\operatorname{Ric}\approx3g$ and equivalence of tensor and endomorphism norms are explicit. This is not all-metrics nonexistence on the smooth resolution.

Sources: the uploaded cumulative local constructions, including sections 55–85; the A02 line manuscript; A02 Steps 60–70 and 83. ADE, type-T, Wahl and quartic extensions have separate hypotheses. Open: all-sign Einstein nonexistence on an arbitrary specified resolution. An obstruction to one asymptotic matching family does not prove it.

C `sec:scalechoice` links the target error to both cutoff radii. C `sec:eh-ls` retains all radial equations of the earlier three-function EH correction, rank-two compatibility, bolt conditions, Kähler-potential restriction, least-squares objective, and nonlinear samples. The old final-node coefficient overwrite is identified in `eq:eh-ls-boundary`; `eq:eh-ls-linear-floor` explains why shrinking the core does not remove a fixed linear residual. This A02 Step 66 attempt remains a useful failed method, not a dependency of the explicit log-Weyl construction.

The later independent package adds C `sec:two-pole-fillings` and `prop:two-pole-fillings`: the actual standard two-pole gluing, its collar-isotopy reduction to a torus-equivariant model, and its definite or hyperbolic intersection form. C `lem:hyperbolic-A1` constructs a compact arithmetic orbifold with only A1 stabilizers; `cor:both-sign-GH` gives normalized smooth-Einstein GH separation for either sign. C `sec:profile-coefficient` distinguishes the selected numerical cutoff coefficient from an optimality theorem. These supplement the existing A1 construction rather than replace it.

## 3. Fixed Dehn-twist surface bundles $E_D$

L `BUN:chapter` contains the full construction and analysis, now also developed as a distinct center in C. Sources include cumulative sections 223–270, 274–275, 279–280, 282, 288–289. The TT pairings and conformal arguments remain part of the mathematical text.

- `BUN:slow`, `BUN:ricci-matrix`, `BUN:slow-bound`: fix the total space, use $h_1=D^*h_0$, and interpolate slowly across the long base collar. Every Ricci block is included, giving $\delta_-(G_\ell)=O(L^{-1})$ and fixed volume. For this fixed-fiber family, `BUN:slow-geometric` and the structure equations give bounded full curvature and all fixed-order derivatives; defect derivatives are $O(L^{-1})$. This is not a general regularity theorem for Ricci pinching.
- `BUN:double`, `BUN:balanced-profiles`, `BUN:exact-second`: balance fiber parameter $\varepsilon$ and base parameter $\beta=\varepsilon^2$, with $I_R\to\pi/2$ and $J_L\to\pi$. The leading defect is $2\varepsilon^2/\pi^4+O(\varepsilon^4)$.
- `BUN:three-equations`, `BUN:B-solution`, `BUN:bianchi`, `BUN:decay`: split the actual second-order source into three scalar equations. Two potential operators are coercive; the third is solved explicitly. Bianchi, tail and closed-manifold cutoff estimates give `BUN:third-bound`, of order $O(\varepsilon^3)$.
- `BUN:global-pairings`, `BUN:nonlinear-obstruction`: use genuine global TT tensors and keep the adjoint defect of the non-Einstein reference metric. `BUN:whole-conformal-third` and the bootstrap for arbitrary positive conformal factors give $\inf_u\delta_-(u^2\widetilde G_\varepsilon)=\Theta(\varepsilon^3)$ for the specified corrected background.
- `BUN:fifth-volume` retains the fifth-order volume term. `BUN:negative-ritz` and `BUN:corrected-ritz` distinguish reference metrics. `BUN:exact-product-gap` and `BUN:closed-log-loss` establish maximum-norm inverse loss on a closed product after removal of the full kernel. A positive $L^2$ spectral gap does not remove that loss.

These are not all-metrics obstructions. L `BUN:conformal` also uses an unchanged product open set to exclude Einstein metrics of every sign within the specified conformal classes; other conformal classes are not excluded. L `BUNTOP:Einstein-necessary` gives the volume window and necessary sectional/Weyl conditions. G develops attainment and the missing structural implications for arbitrary Einstein metrics.

Fixed-fiber interpolation, double degeneration and tensor-corrected metrics are separate families. Exact volume and submersion properties of the first family do not automatically hold after correction.

The English construction chain in C is `sec:ED-object`, `sec:ED-Ricci`, `sec:ED-derivatives`, `sec:ED-double`, `sec:ED-three-equations`, `sec:ED-third-gluing`, `sec:ED-flux`, `sec:ED-global-pairing`, `sec:ED-conformal` and `sec:ED-inverse`. The actual repair and kernel/complement arguments follow in `sec:construction-repair` and `sec:construction-obstruction`. G `sec:bundle-values`, `eq:bundle-attainment-equivalence`, `eq:bundle-einstein-window` and `sec:bundle-structure-bridge` connect the construction to global attainment and arbitrary Einstein structure.

In G `eq:bundlefunctionals`, matching construction and monopole bounds determine the Yamabe invariant, minimal scalar/Ricci volumes, and all three curvature-energy infima on every specified finite cover. The full-curvature identity `eq:bundle-full-energy` makes its attainment equivalent to Einstein existence; nonattainment of the other extrema does not decide it. The open volume window, positive sectional plane, and Weyl restrictions concern any hypothetical normalized Einstein metric, whereas `par:bundle-endpoint-scope` requires the additional assumption of an exact sequence approaching the lower endpoint.

## 4. Near-equality Weyl profile, forbidden germ and necessary degeneration

Full arguments: U `eq:density`, `eq:calibration`, `lem:forbidden`, `thm:local`, `thm:proportion`, `cor:diam`; R's spinor and near-equality analysis. Zero density forces $\operatorname{Ric}=-g$ and $\operatorname{spec}W^+=(-1/6,1/12,1/12)$. Divergence-freeness makes the simple eigenline parallel; the resulting local Kähler relation contradicts this spectrum. This is differential rigidity on an open set, not algebraic impossibility at one point.

U gives $\fint\mathcal D\le436\delta^2+675d$, with $d=(1/3-k/A)_+$. Near-critical sequences collapse in normalized-volume measure and their diameters escape. Neither pointwise uniform collapse nor existence of the sequence is asserted. R retains the bounds `eq:109`, `eq:436675` and `eq:119`: the 109 and 119 bounds concern the same joint density under their respective topological assumptions; they are not different densities to be interchanged.

Sources: A01 Steps 4–14, A03 Steps 3–12, U, and the uploaded IL/calibration archive. R `eq:spinor-deficit` through `eq:walsh` retain the spinor defect, two Hölder steps, harmonic projection, Walsh polarization and spatial phase separation. Open: uniform positive density for arbitrarily collapsed approximate inputs. Selection of a low-energy ball is not construction of a uniform weak harmonic chart.

R `sec:strong-density-bridge` proves the difference equation and strong curvature convergence in the same harmonic chart. `sec:walsh-phases` relates near-orthogonality, eigenline concentration and phase separation, distinguishing a fixed compactness limit from normalized integrals on varying topology.

The old Step 7 claim of a locally possible calibrated model is [withdrawn beside the program](computations.md#correction-step7-local-rigidity). Derdziński's conformal factor is determined by the Weyl norm; it cannot be chosen freely. Constant norm gives local parallelism without compactness. The current proof is U `lem:forbidden`.

## 5. Negative-pinching bound at a fixed supercritical ratio

Full argument: L `FND:SWgap`. Write $K=k+4\ell$, $c=c_1^2(X)$ and $r=K/c-1/3$, retaining the polarization and monopole hypotheses of the cited LeBrun theorem. For $c/3\le K<c$,

$$\delta_-(g)\ge\Phi(r)=
\begin{cases}
\sqrt{r/2},&r\le2(2-\sqrt3)^2,\\
2\sqrt r/(\sqrt6+\sqrt r),&2(2-\sqrt3)^2\le r<2/3.
\end{cases}$$

The proof optimizes over vertices of the Ricci-eigenvalue box and uses the trace-free Ricci/Chern–Weil budget. A fixed ratio $p=K/c>1/3$ cannot have vanishing negative defect. As the ratio approaches $1/3$, the lower bound vanishes but constructs no metric. Small defect also gives $K/c\le1/3+2\delta^2$ and an integral supercritical restriction.

Sources: the early general screening in L, cumulative sections 115 and 212, and the initial A01/A03 budgets. The older fractional bound remains valid in its stated $1/3<p<1$, $\delta<1$ range and is subsumed by the sharper box estimate. It must not be extended past the denominator's sign range. This is different from the nonexplicit exact-Einstein gap below $1/3$.

## 6. ALE first obstruction, gauge-free flux and critical scales

C `eq:firstobs` computes the physical leading term $\lambda h_t^{-1}o+o(1)$ for the refined family $g_t=t(g_{cal}+th)$. A nonzero first obstruction leaves order-one endomorphism defect on the fixed core. Shrinking alone does not remove it. The statement restricts fixed asymptotic matching, not the logarithmic Weyl drift of line 2.

C `sec:ellflux` and `eq:ellfluxbound` prove a gauge-free Wronskian pairing on the flat cone for all angular perturbations in the stated setting. For homogeneity $\ell\ge2$, the dual mass is $J_{K_\ell}\int_b^Rr^{1-\ell}\,dr$: only the quadratic mode produces unweighted $1/\log(R/b)$; higher modes have power-law behavior. `eq:nonlinearflux` and `eq:energyflux` retain the nonlinear and weighted-energy errors after one integration by parts, together with the sharp coefficient for fixed spherical mismatch.

Sources: L `FND:flux`, `FND:nonlinearflux`, `FND:energyflux`; A02 Steps 34, 42, 46–50, 59–74; archive sections 05 and 07. The inference from $|\mathcal O_i|\le C\delta_i\log(1/t_i)+o(1)$ to $\mathcal O_i\to0$ was withdrawn unless the product $\delta_i\log(1/t_i)$ is controlled. C `sec:c0pairing` proposes a mass-$O(t_i)$ test tensor; its existence for arbitrary bubble trees remains open.

## 7. Calderón–Zygmund full-curvature spikes

C's spike construction and `eq:CZ` retain the analytic argument from A02 Step 11. Compactly supported opposite warping cancels the Hessian in the base Ricci block; vertical Ricci sees the Laplacian and first derivatives, while mixed Riemann components still see $u_{xy}$. With
$w_\sigma=-XY\log(X^2+Y^2+\sigma^2)/2$ and
$u_j=\Lambda_j^{-2/3}\psi w_{e^{-\Lambda_j}}$,
the defect is $O(\Lambda_j^{-2/3})$ and central curvature is at least of order $\Lambda_j^{1/3}$. The global metric remains smooth and positive definite.

The [analytic program](computations.md#step11_cz_spike_analytical-py) and numerical variants retain the calculation. On a fixed region, the perturbation-curvature $L^2$ norm tends to zero; total curvature energy tends to the nonzero product-background energy. Choosing a smaller background region first gives small local total energy, not total energy tending to zero on the fixed ball or closed manifold. The underlying $S^2\times S^2$ already admits an Einstein metric. The construction refutes an overly strong input-regularity claim, not Yau 26, and is not a collapse example.

## 8. Algebraic smoothing and Einstein existence

### The BCGP $\mathbb Z_4^2$, $K^2=2$ six-node example

Full arguments: R's product-quotient section, especially `eq:reflexive`, `eq:qg-obstruction`, `eq:H2zero`; C `prop:bcgp-smooth-einstein` and `eq:bcgp-pullback-ke`. A01 Step 49 proposed the mechanism, Step 50 retained its condition, Step 51 supplied the reflexive-tangent bridge, and Step 52 compared characters.

The specified branch data give $g(C_1)=g(C_2)=3$, six A1 nodes and $K_{X_0}^2=2$. The proof uses $T_{X_0}=(\pi_*T_Y)^G$ for the quasi-étale quotient, cohomology under finite maps and invariants, equivariant Serre duality/Künneth and the listed characters to obtain $H^2(X_0,T_{X_0})=0$. It does not replace this with $H^2(T_S)=0$. The local-to-global QG smoothing opens the nodes; canonical-bundle descent and openness of ampleness give an ample canonical bundle on the smooth fiber. Aubin–Yau, simultaneous ADE resolution and Ehresmann then give a negative Einstein metric on the underlying smooth type of the standard complex resolution.

The complex structure may change: the original $(-2)$ curves still prevent its original canonical bundle from being ample. Arbitrary mixed-chirality fillings are not covered. The $S_5,K^2=4$ four-node comparison, two-dimensional $H^2$ and kernel of $\beta:\mathbb C^4\to\mathbb C^2$ provide first-order information, not nonzero smoothing parameters at every node or all-order lifting. Other scan rows are not a complete classification. The [finite-group check](computations.md#step51_reflexive_bridge_verify-py) supports the character calculation; the geometric bridge is proved in the text.

### The seven-line Campedelli cover

C `sec:campedelli-seven-lines` preserves the distinct classical $\mathbb Z_2^3$ seven-line cover from A01 Step 50. `eq:campedelli-lines` and `eq:campedelli-incidences` give the equations, inertia labels and nine intersection points. Independent labels at six triple points give the six local A1 covers in `eq:campedelli-local-node`. `eq:campedelli-cover-algebra` specifies the cover algebra. Moving the lines smooths the nodes, and the canonical-class and simultaneous-resolution arguments give negative Einstein existence on the underlying smooth manifold.

Equality of $K^2,p_g,q$ does not identify this manifold with the BCGP example. The [original combinatorial program](computations.md#step50_six_nodal_campedelli_arrangement-py) checks intersections and labels; it does not replace the cover, smoothing or metric argument.

G `sec:bcgp-global-object` and `sec:campedelli-global-object` keep these positive existence results distinct. G `sec:wahl-global-scope` treats the height-four Wahl model separately: unobstructed deformation of the specified canonical-cover stack coexists with a Wahl smoothing parameter that vanishes at every Artin order. This is not a third instance of the same smoothing argument.

## 9. Product-orbifold chirality, diagonal cancellation and four nodes

Model identities are in C `sec:fullkernel`, `sec:greenjet`, `sec:chiralitytable`, `eq:samechiralityblocks`. A01 Step 94 corrected AA/BB tensor modes; Steps 95–97 separated gauges, source cones and kernel planes; Step 99 checked omitted jets of electric/magnetic modes; Step 100 proved finite algebra at each spectral level. For the specified inter-node AA/BB transport, $B_{++}=B_{--}=0$. This identity does not need a summed spectral tail but does not include self-interaction or the full AB source bridge.

A02 Steps 96 and 99–100 give four receiver equations in the same model. C retains $q_{diag}=0$ by pairing cancellation. The coefficients
$c_{adj}\simeq0.06288499$, $c_{diag}\simeq-0.03545352$, $q_{adj}\simeq0.00800500$
remain spectral-truncation values. An adjacent-balanced row requires
$|c_{adj}+c_{diag}|\le q_{adj}$; the other listed mixed rows require
$|c_{adj}|\le q_{adj}$. A rigorous exclusion needs a tail bound smaller than the displayed margin.

Five rows are classified by square-node permutations preserving adjacency: one compatible and four mixed. Global chirality reversal is not treated as a geometric equivalence at fixed background, and the all-negative row is not listed. The older “five mixed rows,” the unrestricted reciprocal-intersection claim, and the use of zero trace response to test a trace-free response are replaced by their precise versions.

Open: the full equation C `eq:LS`,
$F^{self}+F^{deform}+F^{inter}+F^{complement}+\mathcal R=0$,
with all required same-order terms, $o(t^3)$ control, degenerating ratios and directions. Even complete local exclusion would concern only that degeneration neighborhood. See the [A01 algebraic proof program](computations.md#step100_chirality_cancellation_proof-py) and [A02 four-node program](computations.md#step100_four_node_closure_and_q_diag-py).

C `sec:productspectrum` retains the full tensor types, electric/magnetic normalization, quotient invariance and zero/negative modes. `sec:spectralerrors` writes the projected Green response as a spectral sum, separating heat-regularization error, missing tails and finite computational error. These retain the actual objects of A01/A02 Steps 76–100 without claiming the missing tail estimate.

## 10. Positive-branch finite type and conditional orbifold/ALE limits

C `sec:coveramplifier` gives the classical finite-type consequence under fixed $\delta_0<1$ and $\operatorname{Vol}\ge v>0$, using Myers, volume comparison and four-dimensional noncollapsed finiteness. A separate proposition assumes a uniform volume lower bound for a simply connected family, then uses universal-cover finite type and $\chi(\widetilde M)=|\pi_1M|\chi(M)$ to reach the general family. Myers/Bishop alone do not supply the assumed volume lower bound.

Sources: A02 Steps 9–10, 24–31, 73–85; F `sec:frontier` and R's approximate-equation discussion. Orbifold/ALE descriptions, transfer of actual kernel projections, bubble trees and exact Einstein limits require their respective hypotheses. Finite type does not produce a metric, and an Einstein metric on a cover has not thereby been made deck-invariant. Exact desingularization obstructions do not automatically apply to arbitrary approximate inputs.

### Torus rods, corners and multi-rod families

G `sec:toric-rods` develops the full equations. `eq:toric-lattice-corner` gives primitive rod labels and smooth corners. `eq:toric-integral-chain` computes the intersection form $kH$ in an integral basis and uses smooth torus-action classification to identify $\#_k(S^2\times S^2)$. The hexagonal Delzant object is different: `eq:toric-hexagon-form` and `eq:toric-hexagon-blowups` identify $\mathbb{CP}^2\#3\overline{\mathbb{CP}}^2$.

`eq:toric-diagonal-Ricci` retains three horizontal and two vertical Ricci components and the trace-free equation. `eq:toric-edge-ode` and `eq:toric-flux-volume` give unit endpoint slopes, flux and volume. `eq:toric-corner-order2` lists cancellation coefficients, but the mismatch $A(3A+1)/20$ in `eq:toric-corner-mismatch` shows why matching one edge did not close both common constant-curvature rods.

`eq:toric-separated-first` gives a genuine local Einstein germ and first integral; `eq:toric-separated-angle` and `eq:toric-separated-volume` describe the two cone angles and periods. The multi-rod family `eq:toric-alpha-data` satisfies individual necessary conditions and integral scales, not a closed near-Einstein filling. Failure of the regular-hyperbolic-polygon ansatz excludes only that model. See G `sec:toric-provenance`, the [corner calculation](computations.md#step19_finite_rod_corner_matching-py) and [six-rod calculation](computations.md#step36_alternating_rod_analysis-py).

## 11. Graph manifolds, collapse models, Koiso germs and two-ended connectors

This topic contains several complete restricted results, not one completed global construction.

- G `eq:graphvol`, `eq:graphW`, `eq:graphconcentration`: in the specified Di Cerbo pure-hyperbolic-block class, the all-sign Einstein obstruction is an input. An approximating negative sequence must nearly saturate volume and satisfy $\fint|W|^2\le8\delta/3$ while $\|W\|_\infty\ge(1-3\delta)/\sqrt3$. `eq:graphdiameter` additionally requires derivative control. L `GLB:graphpinch`, `GLB:diam` retain cumulative sections 317 and 320–321. Hyperbolic local limits are possible, unlike the forbidden spectrum in line 1.
- G `eq:bcg-threshold`: degree-two BCG/CGB on the specified hyperbolic connected sums gives a positive bound depending on the target Euler characteristic. Its decay as $\chi\to\infty$ neither constructs inputs nor supplies a dimension-uniform bound.
- G `eq:fullRic` contains normal, tangential and mixed Gaussian Ricci blocks. Flat slices, the fixed helical frame in `prop:helical`, and the complete two-expanding-ended free isometric OT-$T^2$ setting of `thm:OT` have separate proofs. They do not cover twist, singular orbits, nonsymmetry or every connector. R `app:reduction` retains the corrected Nil monotonicity sign, genuine Einstein cusps and circle reduction; removal of the absolute fiber period does not control reconstruction of the base.
- G `eq:gaussian-constraint`, `eq:exp-first`, `eq:exp-second`, `eq:hermite-matrix`, `prop:center-contraction`, `sec:diagonal-core`: center constraints, noncommutative derivatives, outward-normal signs, six actual endpoint jets, initial contraction and weighted anisotropic flux. The actual A03 Steps 75/98 ansatz, sample residual and endpoint overwrite are retained. Full matching must use common scales, center data and peripheral gluing, not independently optimized halves.
- G `eq:separator-jacobi`, `eq:separator-schrodinger`, `eq:separator-Q-bound`: separator stability, capacity and weighted Maxwell source give a length-independent charge bound on the separator, not charge vanishing throughout the base. Stable exact Koiso germs and normal-energy spikes show why stability does not supply normal transport control. Local analytic existence time may depend on the data.
- G `eq:charged-dictionary`, `eq:physical-charge-source`, `eq:charged-taylor`, `eq:charged-logQ`, `eq:charged-noether`, `eq:charged-pairing`: charged stable centers, coordinate versus physical charge, the corrected forcing sign, Noether pairings and Bochner cancellation. $L\log Q=-18-4Q+e_\perp$ gives no formerly claimed maximum-principle ceiling. The scalar redshift countermodel is not a complete Einstein solution.
- G's shared-parameter matching operator retains the full-variable principal-symbol test, common center parameters, two Dirichlet-to-Neumann returns and orbit holonomy. Symbol injectivity is not a Fredholm theorem, a cokernel description or a uniform inverse. The fixed-charge local $K_X$ identity is kinematic, not an extra closing equation.
- G `eq:relative`, `eq:relativebound`: the Step 100 relative CGB identity is
  $2\int_N|W|^2+12(V_N-V_{rem})=\int_N(|E^\circ|^2+2e-e^2/12)$,
  with $E=\operatorname{Ric}+3g$. Approximate exteriors require their signed curvature and volume errors. `eq:peripheral-rank`, `eq:cusp-tail`, `eq:cusp-cover-scale` retain the specific 24cdc1.1 peripheral positive rank, $V_{tail}=A/3$ and common $N^{-2}$ scale. `eq:RN` requires $T=\log N-R+O(1)$ and $N\gg e^R$ for a genuinely long neck.

Sources: A03 Steps 63–78, 79–87, 88–97, 98–100 and archive section 08. Step 100 withdrew Step 99's use of the closed $\chi\le0$ lower bound, approximately 1.098, as a connector-with-boundary target. A local torus action does not force the completed graph manifold to have $\chi=0$. The continuation target is one actual family with defect tending to zero, a rigorous adjoint obstruction or a new global existence argument, not a single finite-error example.

The Step 95 charged-OT ceiling is [withdrawn beside the program and its conclusion](computations.md#correction-step95-charged-ceiling). Forcing derivatives cancel the curvature contribution; omitting them does not justify importing the twist-free Bochner bound.

G `sec:OT-critical`, `lem:OT-critical` and `prop:OT-Morse` extend the twist-free energy argument to a necessary finite-type base/end restriction. G `sec:AH-matching` retains all three local Ricci blocks and the flattening estimate; `prop:AH-volume-budget` identifies the fixed-topology contradiction in the proposed W-to-closed-manifold gluing. G `sec:connector-continuation` keeps the invariant AH exact-OT argument, conformal-boundary restriction, charged-throat scalar constraint, and the shooting instability, without turning them into a general nonexistence theorem.

The supplemental report and all 39 programs are embedded in the existing appendices, including corrections adjacent to the W, branch-logic and sharp-coefficient passages. [Reproduction](reproduction.md#supplemental-independent-programs) explains extraction and bounded checks. The `supplemental_sources` entry in [source coverage](source-coverage.json) maps all 62 uploaded files; the older coverage tables and three hundred Step entries remain intact.

## 12. Classical low dimensions and open higher-dimensional questions

F gives the classical reductions: uniformization in dimension two; Hamilton for positive Ricci in dimension three; and, for sufficiently small negative defect in dimension three, $K_{ij}=(r_i+r_j-r_k)/2<0$ together with geometrization. These are not higher-dimensional theorems.

G's cover/product section and C's product propagation retain the maximum formula for product defects. A positive Einstein sphere factor has dimension at least two, so that direct product construction skips dimension five. Propagation of input defect does not propagate all-sign nonexistence: an unknown Einstein metric need not split. Sources: A02 Steps 5, 24, 70–74, 94 and the higher-dimensional/product archive. Earlier claims that only dimension four remained or that all higher-dimensional obstructions had been removed have no corresponding general proof.

Open: a uniform existence mechanism for $n\ge5$. Critical $L^{n/2}$ energy, ALE bundles, special holonomy and new topology remain possible approaches, each with its own hypotheses. This gap limits an all-dimensional affirmative proof; a fixed-dimensional two-sign counterexample needs no separate resolution of every higher dimension.

## Further substantive proof modules

These modules retain arguments beyond the main theorem statements. A shared heading does not replace their proofs.

| Module | Location and mathematical scope | Origin |
| --- | --- | --- |
| Analytic repair of approximate inputs | F `prop:repair-radius` proves a contraction with explicit constants. F `sec:obstruction-bridge` separates complement correction and the full finite-dimensional obstruction. Spaces, inverse bounds, positive-definite radius and gauge removal must match the pointwise input. | Classical perturbation method, developed for these constructions |
| Strict Hitchin–Thorpe endpoint and complex/symplectic positive branch | L `FND:HT`, `FND:positive`: ratio-three endpoint, equality line bundle and reductions in specified classes; not an optimal general existence threshold. | Early general screening |
| Full ADE cokernel, type-T and Wahl | L's ADE and type-T sections retain the $3b_2$ kernel. The free Wahl quotient gives $T^*\mathbb{RP}^2$ and the lowest-order construction. `FND:quarticbound` assumes the additional quartic extension. | Cumulative sections 55–85; C |
| Scalar inverse, Hessian endpoint and variational flux | L `FND:weightedscalar`, `FND:Hessian`, `FND:volumevariation`: inverse for $0<\mu<2$, a true near-kernel excluding a global $\mu=2$ bound, local endpoint powers, and constant-scalar volume cancellation. | Full cumulative derivations |
| Short handles and nonsymmetric boundary obstructions | L `FND:short-handle`, `FND:covervolume`, `FND:boundarymean`. Short-handle exclusion does not exclude long thin handles; mean-curvature thresholds retain exterior jets and topology. | Cumulative sections 213–222 |
| Berger core and failed continuation | L `FND:berger`: exact local negative-Einstein core, finite-distance singularity of the specified biaxial extension, and partial triaxial restrictions. Local flexibility and restricted extension failure coexist. | Cumulative sections 213–222; A03 |
| Height-four canonical ring and Artin parameters | L `ALG:quadratic`, `ALG:allartinlocal`, `ALG:QG`, `ALG:ext38`, `ALG:allartinring`: explicit relations and the 38/0 computation. QG formal smoothness of the specified canonical-cover stack does not assert smoothing of every singularity: the Wahl smoothing parameter vanishes to every Artin order. `ALG:moduliconditional` has separate descent hypotheses. | Cumulative sections 58, 61, 70, 73–74, 79, 90, 99, 102–104, 112–120, 133, 135, 139, 144; G |
| Natural deformations and isotrivial exceptions | L `ALG:noniso`, `ALG:isotrivial`, `ALG:localglobal`, `ALG:wahlquotient`, `ALG:redundancy`, `ALG:heightn`. The universal $h^2=1$ claim is replaced by two-/three-dimensional isotrivial exceptions. `ALG:naturalconditional` does not follow from canonical-cover Ext² alone. | The same algebraic branch, with later corrections |
| SW saturation, ordinary monopole classes and volume | L `GAU:SW-to-KE`, `GAU:ordinary`, `GAU:four-term`, `GAU:ratios`; retain fixed exterior convergence and core-homology assumptions for full class identification. | Cumulative sections 85–211 |
| Critical analysis and exterior response | L `GAU:bundle-gradient`, `GAU:Hessian-critical`, `GAU:Kuranishi`, `GAU:Dirac-gap`, `GAU:external-Jacobi`, `GAU:residue-constant`; finite bubble-tree/fixed-background conditions remain. Kernel orthogonality does not square a first-order residual. Lorentz–Kuranishi retraction is conditional. | Gauge-analysis branch |
| Local KE cancellation, periods and all-point evaluation | L `GAU:local-KE`, `GAU:net-flux`, `GAU:period-local`, `GAU:all-point-zero`. `GAU:gap-conditional` also needs full limit classification and finite-point evaluation injectivity. | Later gauge-analysis arguments |
| Effective degenerate local-flow estimates | R `app:flow`: support selection, relative Sobolev, full tensor variation, three weak energies, exact defect homogeneity, real-exponent Moser, endpoint volume cancellation, highest cutoff jets and background connection. See `eq:H2energy`, `eq:H3energy`, `eq:Qenergy`, `eq:realp`, `eq:weighted-endpoint`. | A01 Steps 15–48, 54–70; A03 Steps 13–61; archive 06 |
| Remaining local-flow problem | R's common-time/terminal analysis and U (SC). Per-datum smooth existence and fixed-order estimates do not give common time across degeneration. `sec:ungauged-restart` identifies the ungauged difference-energy symbol issue; `sec:smooth-terminal-splice` is conditional; `sec:terminal-liouville` combines terminal decomposition, positive support fraction and Liouville averaging on the same small-density chart. | A01 Steps 30, 40, 55–67; A03 Steps 40, 50, 60–61 |
| $E_D$ topology and variational infima | L `BUNTOP:covers`, `BUNTOP:global-values`, `BUNTOP:all-monopoles`, `BUNTOP:SW-four`, `BUNTOP:endpoint`, `BUNTOP:reducible-core`: covers, Yamabe/energy infima, conditional endpoint degeneration and closed-product cores. For a degree-$d$ cover, the energy infima are $16V_*,4V_*,8V_*$. Only the first two have the stated nonattainment proof; attainment of the last is equivalent to Einstein existence. | Later surface-bundle analysis; G |
| Negative Weyl eigenline and source terms | L `WYL:balance`, `WYL:closed`, `WYL:kernel`, `WYL:source`, `WYL:nonclosed`: closedness gives rigidity, a source gives balance. The slow-interpolation Cotton term contributes at leading order; absolute smallness is not the required relative estimate. | Cumulative sections 271, 276–278, 281, 283–286 |
| Adapted-submersion structure | L `SUB:blocks`, `SUB:integrable`, `SUB:basic`, `SUB:area`, `SUB:quartic`, `SUB:oscillation`, `SUB:all-product-submersions`: all curvature blocks, two product-rigidity statements, nonbasic area and moment identities. An arbitrary Einstein metric need not adapt to the given projection. | Cumulative sections 287, 293–301, 304–305, 309–310, 313–314 |
| Covariance and high-frequency tests | L `SUB:negative-covariance`, `SUB:extension-gap`, `SUB:frequency-scaling`, `SUB:TT-source`: exact constant-negative-curvature local covariance models and thresholds for a fiber-preserving closed extension. | Adapted-submersion branch |
| Harmonic representatives, Hodge/cup product and optimal target | L `SUB:harmonic-bochner`, `SUB:area-counterexample`, `SUB:area-parallel`, `SUB:cup-product-bound`, `SUB:one-form-test`, `SUB:hyperelliptic`, `SUB:optimal-target`, `SUB:optimal-nonconformal`. Fixed-source optimal-target attainment is classical; it does not imply pointwise conformality. Hodge projection does not preserve decomposability. | Cumulative sections 302, 306, 311, 315, 318–319 |
| Weil–Petersson effective equation | L `GLB:WPsource`, `GLB:WPbalance`: unforced length obstruction and signed forced balance. The actual four-dimensional forcing/error must still be derived on the same geometry. | Cumulative section 290 |

## Actual Session endpoints and continuation

These describe the original handoffs; they do not reset Sessions or replace Step 100 with an earlier plan.

- A01 Step 100 retained the AA/BB same-chirality finite-algebra proof. Its handoff compares the restricted IL estimates from Steps 68/65/67, the missing approximately pinched input in the hyperbolic BCG route, dimension five, the AB structural bridge, and other methods. Continuing the product quotient requires actual physical sources, AB transport, self-interaction, complement and remainder. The uniform gap remains a separate retained result, not a completed mixed-resolution obstruction.
- A02 Step 100 retained diagonal cancellation and the four-receiver reciprocity window. Its handoff calls for checking enumeration, exchange symmetry, physical diagonal coupling and the dominance of $O(t^{5/2})$ over $t^3$, then comparing rigorous remainder control, negative-mirror coefficients, global nonexistence or direct existence. Algebra/spectral certification is separate from complete curvature formalization. The corrected one-compatible/four-mixed wording does not turn the handoff into a global theorem. Standard-complex negative-KE smoothing does not settle mixed fillings.
- A03 Step 100 retained relative CGB, peripheral rank and common scaling. The remaining object is a complete matrix connector, full Ricci field, Weyl energy and exterior correction for the same $(N,T,R,\text{center data},\text{affine gluing})$, or an obstruction covering its allowed freedom. Step 98's coarse grid did not preserve a reliable continuous field and all actual endpoint jets. Stagnation of one quintic interpolation is not nonexistence.

The 2026-09-16 and 2026-09-17 three-line manuscripts broaden the organization without replacing these endpoints. “Three open interfaces” is a thematic grouping, not the total number of independent mathematical gaps. Algebraic descent, evaluation injectivity, collapsed regularity, full mixed reduction, end matching and all-metrics existence have different quantifiers.

## Coverage of the three hundred Steps and uploaded manuscripts

The ranges below compress chronology, not mathematical content. Each Session's Steps 1–100 has a canonical relay entry in the retained source index.

| Source | Step ranges and mathematical locations |
| --- | --- |
| A01 | 1–14: near-equality/unfolding (U,R); 15–48: weighted local flow and revisions (R); 49–53: QG smoothing/characters (R,C); 54–70: continuation/Moser/terminal calibration (R); 71–75: graph neck/center comparisons (G); 76–100: product quotient, kernels, Green response and chirality (C). |
| A02 | 1–10: positive branch, noncollapse, obstruction scope (F,C); 11–29: spikes, rods/corners and circle collapse (C,G,R); 30–59: bubble-tree projections, orientations and negative calibration (C,R); 60–75: resonant flux, log scales, higher modes and products (C); 76–100: nodes, source cones, ALE topology and four receivers (C and computational appendices). |
| A03 | 1–12: topology, Weyl, unfolding, circle reduction (R); 13–61: degenerate-flow estimates and continuation revisions (R); 62–70: graph manifolds, centers, endpoints (G); 71–87: anisotropy, helical and OT obstructions (G); 88–97: charged stability, Koiso and matching (G); 98–100: full-matrix tests, quantifier corrections and relative CGB (G, appendices). |

The [source index](source-coverage.json), read on demand rather than loaded into the default context, contains:

| Historical table | Retained information |
| --- | --- |
| step-index-provenance.json | Number, research excerpt and relay identity for all 300 Steps |
| embedded-sources.json | 1990 source records, including 300 relays and 49 web materials, with original identity and archive location |
| computational-coverage.json | 1014 computational sources: 1004 distinct locations and 10 same-content references |
| omitted-derivatives.json | Disposition of 79 items not embedded verbatim: 37 binary/image derivatives, one regenerable mesh and 41 third-party/generated dependencies |

The current computational entries resolve sources to actual package anchors and fingerprints of programs, outputs and adjacent corrections. The problem-source entry identifies the later compilation, problem page, commentary boundary and cited 1982 bibliography. Later manuscript-integration entries locate the added scientific arguments in these papers without rewriting the historical counts.

Historical archive destinations such as S0910A01.md are not current proof links. Read the papers at the locations above. The source tables preserve checkable identities and correspondence, not a claim that every original relay or every historical inference is reproduced verbatim.
