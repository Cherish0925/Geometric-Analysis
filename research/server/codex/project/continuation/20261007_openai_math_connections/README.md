# OpenAI mathematics: connections to Einstein gaps

7 October 2026. Supplement to the existing Einstein-gap research, not a replacement for its goals or proofs.

## Start here

The useful new inputs are **joint concentration estimates, same-test stability identities, curvature-action decompositions, and global lower-bound constructions**. The detailed formulas, hypotheses and source passages are in [Mathematical connections](connections.md). Original papers and searchable text are in [the source collection](../../archive/sources/20261007-openai-math/README.md).

The official release describes 722 manuscripts in 372 result families, with differing levels of verification. Family numbers below are catalogue locators, not theorem numbers. We read the relevant statements and proof passages; this supplement does not assume that the release as a whole is a verified theorem library.

## Relation to the present research

The established N1 and I40/I41 estimates, linear small-parameter scale, finite-density endpoint theorem, and L′/K extensions remain the starting point. On selected balanced covering families, the construction already gives

\[
\limsup_j\frac{\alpha(M_j)}{h_j}\le 3.9961511381\ldots<4.
\]

Consequently, a general lower-bound mechanism for these families must allow genuine background–surgery interaction. It cannot impose an independent cost of \(8\pi^2\) per blow-up and thereby recover the disproved coefficient-four target. Later Session results take precedence over this dated starting point.

| Mathematical connection | Read in the original | What it could add | What still has to be proved here |
| --- | --- | --- | --- |
| Positive-current concentration (342) | Taming paper, Lemma 4.4, Theorem 5.1, §6 | Joint directional and transverse moments, rather than separate absolute-value bounds | An actual closed-current representation and moment bounds uniform through the relevant geometric degeneration |
| Shared-amplitude stability (375) | De Giorgi paper, (5.6)–(5.8), Lemma 9.3, §10 | A negative defect-mass term controlled by the same weighted gradient used in a second geometric identity | The corresponding coercive localization for the actual SW system; residual-square positivity alone is insufficient |
| Bianchi-constrained curvature action (348) | Zero-plane paper, Proposition 2.4 and §5 | Decompose the actual tensor before estimating it; keep cancellations and weighted squares | Near-Einstein Cotton sources and a positive form not supplied by nonnegative sectional curvature |
| Global dual lower bounds (090) | Coulomb paper, §§3–5 and Proposition 2.4 | Preserve the infimum, obtain geometry for minimizers, then build a globally admissible comparison object | An appropriate global identity for the nonlinear metric functional; no automatic convexity or marked-core decomposition |
| Ricci-preserving extension (351) | Ricci-flow extension paper, Theorem 5.1 | Controlled collars can be extended with quadratic Ricci cost | Supply the collars from the original competitors and prove a total error \(o(Q)\) |
| Exact two-form correction (341) | Hypersymplectic paper, Lemma 10.4 | An \(L^2\) correction controlled directly as a two-form, without a primitive's spectral-gap estimate | Preserve the coupled field equations and obtain any derivative bounds the application needs |
| Scalar curvature and simplicial volume (335) | Scalar-integral paper, Theorem 1.1 | A different topological input for a normalized gap; a precise corollary is derived below | The imported theorem and its companion are substantive prerequisites; the resulting criterion does not determine the balanced small-\(h\) optimum |

The wider reading is in [§10](connections.md#10-further-inputs-backgrounds-exact-rigidity-and-limit-spaces): **051** supplies canonical ampleness and hence a negative KE background via Aubin–Yau; **339** supplies exact entropy rigidity under strictly negative sectional curvature; **337** supplies sharp isoperimetry under a sectional upper bound; **355** illustrates all-scale convergence from summable geometric motion; **356–357** concern weak Hessians and coordinates once the relevant RCD limit structure is available. These expand the subject's input and realization branches without turning all of them into compulsory tasks.

Two distinctions materially sharpen the reading:

1. **The zero-plane paper does not eliminate \(W^-\) from its final estimate.** Its positive Hessian operator still uses \(\sec\ge0\). The related \(L^2\) gap also requires nonnegative sectional curvature and absolute, not volume-normalized, small Ricci energy.
2. **The Coulomb paper does not assume that all competitors have controlled cells.** It first obtains separated finite-volume minimizers, proves the lower bound there, and transfers it to all competitors. That bridge, not merely its local energy formula, is relevant to O11.

## Two concrete deductions to retain

Under the full conformal-class actual supply of the finite-density O10 theorem, a putative sequence with \(\beta_j\to\infty\) and \(\kappa_{\beta_j}\to0\) necessarily has

\[
\frac{\chi(M_j)}{p_j}\to\infty,
\qquad
\frac{p_j}{V_j}\to\frac{2}{9\pi^2},
\qquad
\fint_{M_j}|W^-|^2\to\infty.
\]

The first conclusion uses the conformal invariance of \(p_j=(a^+_{g_j})^2\), so the existing finite-density theorem can be applied with its budget reset to \(A_j=p_j\). Unbounded \(\chi/A\) alone would not justify the last conclusion. See [§2](connections.md#2-the-remaining-endpoint-has-unbounded-actual-density).

Assuming the scalar–simplicial-volume theorem, set

\[
H=a_4\|M\|>0,\qquad
b=\frac{96\pi^2(2\chi-3|\tau|)_+}{H}<1.
\]

Then the Chern–Weil identities give, for every smooth metric,

\[
\boxed{\mathcal E(g)\ge\mathcal J(g)\ge\frac{4(1-b)}{4-b}.}
\]

This is a short derived application of the external theorem, not a claim that the remaining O10 or O11 problem has been solved. Its useful and ineffective ranges are computed in [§8](connections.md#8-a-different-topological-input-simplicial-volume).

## A direct downstream consequence

The new finite-time Ricci-flow extension theorem, combined with the classical negative-Yamabe dissipation argument, gives:

\[
\mathcal Y(M)<0,\quad \inf_gP(g)>0
\quad\Longrightarrow\quad
\sup_{0\le t<T_{\max}}\|s_{g(t)}\|_\infty=\infty
\]

for every maximal volume-normalized Ricci flow. [§11](connections.md#11-a-direct-ricci-flow-consequence-of-a-positive-traceless-ricci-gap) gives the full short proof, including the changing volume form and the conversion between the two flow normalizations. The immortal branch is classical; the finite-time branch imports family 351, Theorem 1.1. A lower bound for \(P+D_2\) does not suffice, and finite-time blow-up is not asserted.

[§12](connections.md#12-two-further-proof-mechanisms-retained-from-the-web-discussion) also retains the closed concentrated-current strategy and the finite-weighted-variation path argument, including why neither is an automatic static Einstein-gap theorem.

## Using the material

Read the common formulas once, then pursue whichever connection changes the actual missing implication in the current work. A useful outcome is an applicable estimate, a failed identity with a precise reason, a genuine construction, or a reduction that removes an existing assumption. The papers are resources for mathematical choice, not an instruction to pursue every candidate or abandon another productive route.

For O10, the most concrete tests are a same-field localization with a negative alignment-defect term, and a curvature-action identity retaining its Cotton sources. For O11, examine the infimum-preserving global bridge and the background interaction already exhibited by the sub-four constructions. Share usable intermediate formulas through the existing Session Group; continue from each other's results rather than duplicating the same local calculation.
