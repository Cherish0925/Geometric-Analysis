# Kodaira slopes and Fino's existence question: sources and present status

Checked on 31 October 2026; updated after reading the private Geometric-Analysis repository.

**Conclusion.** The private repository supplies substantially more than summaries: the finite-density analytic proof, its preceding estimates, the two-orientation application, and the explicit Fino construction with its global completion and curvature program are available. The Fino program was run successfully, its frame inputs were checked against the displayed metric, and the smooth completion and completeness argument were examined. These checks support an affirmative answer to Fino's existence question. The Kodaira argument has the full quantifier of LeBrun's question; the critical finite-density proof chain was followed and no substantive error was identified in the steps examined. A separate reconstruction of every upstream spinor component identity has not been completed.

The literature examined did not supply an earlier resolution of either question in its full stated scope. Historical priority is not established by that finding. The new Fino manuscript does give an explicit distinction from the weakly \(*\)-Einstein subclass associated with Armstrong's ansatz; the broader comparison with the complete 2002 article and later constructions remains unfinished. Section 5 records the additional proof reading and computations, superseding the earlier statement that this investigation had only inspected the Fino formulas and FD2's proof outline.

## 1. The two questions and their dates

| Question | Exact scope | Dated primary source |
| --- | --- | --- |
| LeBrun's Kodaira-fibration slope question | Does one \(\varepsilon>0\) satisfy \(c_1^2(S)/c_2(S)\le 3-\varepsilon\) for **every** Kodaira fibred surface? | Catanese–Rollenske, *Double Kodaira fibrations*, introduction, p. 2; [preprint first submitted 14 November 2006](https://arxiv.org/abs/math/0611428), published in *J. reine angew. Math.* **628** (2009), 205–233. The introduction attributes the question to LeBrun. |
| Fino's existence question | Is there a **non-invariant, non-Ricci-flat, strictly almost-Kähler Einstein Riemannian metric** on a real four-dimensional Lie group? | Fino, *Almost Kähler 4-dimensional Lie groups with J-invariant Ricci tensor*, *Differential Geometry and its Applications* **23** (2005), 26–37, immediately after Corollary 2.1; [published article](https://doi.org/10.1016/j.difgeo.2005.03.003). |

The first question is publicly documented almost twenty years before this check; its 2009 journal publication is seventeen years old. The first oral formulation was not dated by this investigation. Fino's published question is approximately twenty-one years old. Her original question imposes neither compactness nor completeness.

Neither question is identical to the closed negative Goldberg problem. A uniform Kodaira slope gap also does not determine the optimal slope or establish that \(8/3\) is maximal.

## 2. Kodaira: what the primary literature establishes

| Source read | Relevant statement | Consequence for the priority question |
| --- | --- | --- |
| [Catanese–Rollenske, 2006/2009](https://www.math.uni-bielefeld.de/~rollenske/papers/kodairafibrations.pdf), introduction | Explicitly asks whether slopes are bounded away from 3; constructs slope \(8/3\). | Establishes the question and a construction, not a uniform upper bound. |
| [Catanese, *Kodaira fibrations and beyond: methods for moduli theory*](https://arxiv.org/abs/1611.06617), §1.3, p. 9 | Records the uniform-\(\varepsilon\) question as open. | A later explicit statement of the same problem. |
| [Causin–Polizzi, 2021](https://iris.uniss.it/retrieve/c59a64c5-d05f-4a99-9488-d066d9f401e7/Heisenberg-and_double-kodaira-AAM.pdf), introduction | Still describes possible slopes approaching 3 as unknown. | No resolution by that paper. A repository cover dated 2026 is not its publication date. |
| [Polizzi, *Diagonal double Kodaira structures on finite groups*, 2022 version](https://arxiv.org/pdf/2002.01363), Remark 4.10 | Explicitly says that approach to 3 remains unknown. | The latest explicit open-status statement located in the relevant original texts during this investigation. |
| Same paper, Proposition 4.12 and Remark 4.13 | Gives \(\nu<8-4\sqrt2\) for **diagonal double** Kodaira fibrations. | The restricted class does not include all Kodaira fibrations; it cannot settle LeBrun's question. |
| [Liu–Lu, *On the Geography of Slopes of Fibrations*, 2024](https://ems.press/journals/prims/articles/14298288), definition (1.1) | Studies the relative slope \(K_f^2/\deg f_*\omega_f\). | This is not the geographic Chern slope \(c_1^2/c_2\). Its realization results do not settle the present question. |
| [Bieri, *On fibrations approaching the Arakelov equality*, 2021 online / 2022 volume](https://link.springer.com/article/10.1007/s00209-021-02847-y), Proposition 1.1 | For a smooth Kodaira fibration of fibre genus \(g\), \(L_f\le(g-1)/3\). | This is a separation from the Arakelov bound for a different invariant, not a uniform Chern slope gap. |
| [Polizzi–Sabatino, 17 April 2026](https://link.springer.com/article/10.1007/s10231-026-01691-3) | Constructs double Kodaira families with the same biregular invariants but different fundamental groups. | Its stated results do not give the required uniform slope separation. Silence about a problem is not evidence that it remains open. |

For the Bieri comparison, put \(B=(g-1)(b-1)\) and \(d=\deg f_*\omega_f\). Smoothness gives
\[
c_2=4B,\qquad c_1^2=8B+12d,\qquad L_f=\frac{d}{b-1}.
\]
Consequently
\[
\nu=2+\frac{3L_f}{g-1}.
\]
The cited bound yields \(\nu\le3\); it does not yield \(\nu\le3-\varepsilon\). This conversion explains why its title and abstract cannot be treated as a resolution of LeBrun's question.

Kotschick's [*On regularly fibered complex surfaces* (1999)](https://msp.org/gtm/1999/02/gtm-1999-02-015p.pdf), Theorem 3, proves \(3|\tau|<\chi\) for the relevant surface bundles admitting a complex structure or an Einstein metric. Its proof already uses the two orientations. The potential new assertion in the project is a **single positive separation valid across the entire class**, not the first use of two orientations.

### The project's actual implication

Chapter 10 of [the collected source](</home/ubuntu/下载/00_All_Recent_Research(1).tex:3189>) explicitly states its dependence on FD2. It asserts
\[
\mathcal J(g)+\left(1-\frac{3|\tau(M)|}{\chi(M)}\right)_+
\ge\varepsilon_{\rm SB}>0,
\qquad
\mathcal J(g)=\frac{4\int|\operatorname{Ric}^{\circ}|^2}{\int|\operatorname{Ric}|^2}.
\]
For a Kodaira fibred surface, ampleness of the canonical bundle supplies a negative Kähler–Einstein metric. On that metric \(\mathcal J=0\), so
\[
\frac{c_1^2}{c_2}
=2+\frac{3\tau}{\chi}
\le3-\varepsilon_{\rm SB}.
\]
If the required FD2 theorem and the stated input supply are established, this implication has the full quantifier of LeBrun's question.

The precise endpoint calculation also exposes the essential dependence. Normalize the Kähler–Einstein metric by \(s=-4\), write \(e=\chi\) and \(r=c_1^2/e\), and use the reverse-orientation actual class. The manuscript obtains
\[
A_-=e(4-r),\qquad
\frac{\chi}{A_-}=\frac1{4-r}\le1,\qquad
p_-=\frac{4e^2}{c_1^2},\qquad
V=2\pi^2c_1^2.
\]
Its normalized parameter defect is
\[
\bar\kappa_\beta
=16(1+\beta^{-1})
+8(\beta+1)\frac{3-r}{r}
-\frac{144}{r^2}.
\]
If \(r\to3\), choose \(\beta=(3-r)^{-1/2}\). This expression tends to zero, whereas FD2 would give
\[
\bar\kappa_\beta\ge
c_{\rm FD}(2)\frac{(\beta-2)^2}{\beta^2}\longrightarrow c_{\rm FD}(2)>0.
\]
Thus the application uses a **fixed finite-density theorem**; it does not await unrestricted O10. The algebraic limit is consistent. It cannot establish FD2's analytic hypotheses or proof by itself.

The finite-density source [O10_All_Finite_Density.md](../../Geometric-Analysis/archive/originals/2026-09-29/O10_All_Finite_Density.md) uses actual fields, a fifth-power line-bundle section, resolvent estimates and Chern pairing. The repository now makes its preceding strong-current, bounded-resolvent and scalar covariance arguments available for continuous reading. Their substantive estimates were read in this follow-up, including the logarithmic parameter selection and the rank-one transgression. The upstream differential identities were traced to the integrated source; not every spinor component identity was independently reconstructed.

**Status:** an explicit solution manuscript with the full scope of the public question and an available analytic foundation. No error was identified in the examined chain. The remaining limit on this investigation is the extent of independent reconstruction, not an identified missing step in the manuscript. No earlier full-scope solution was found; historical priority remains unestablished.

## 3. Fino: nearby constructions and why they do not settle the comparison

Fino's original published text was located through the indexed publisher text, including Corollary 2.1 and the following question. Direct publisher retrieval was intermittently unavailable. The original 2003 arXiv version is not a substitute for the exact wording in the 2005 publication.

| Primary source examined | What it supplies | Relation to the exact question |
| --- | --- | --- |
| [Apostolov–Armstrong–Drăghici, *Local rigidity of certain classes of almost Kähler 4-manifolds*](https://faculty.fiu.edu/~draghici/research/paperfiles/AGAG2.pdf), introduction and local models | Discusses the Nurowski–Przanowski/Tod four-dimensional strictly almost-Kähler Einstein examples. | Those examples are Ricci-flat, expressly excluded by Fino's question. |
| [Apostolov–Drăghici–Moroianu, 2001](https://moroianu.perso.math.cnrs.fr/tex/2001ijm.pdf) | Complete negative Einstein strictly almost-Kähler constructions in even real dimensions greater than four. | The dimension restriction matters. |
| [Armstrong, *Almost Kähler Geometry*, 1998 thesis](https://johnarmstrongmaths.com/publications/resources/thesis.pdf) | Discusses weakly \(*\)-Einstein/Ricci-flat models and the limitation of an attempted local existence argument. | The thesis does not substitute for reading the distinct 2002 article. |
| [Armstrong, *An ansatz for almost-Kähler, Einstein 4-manifolds*, 2002](https://doi.org/10.1515/crll.2002.009) | A directly relevant ansatz paper, *J. reine angew. Math.* **542**, 53–84. | Full text was not obtained. The project's October 8 manuscript supplies a positive Weyl off-diagonal invariant excluding the weakly \(*\)-Einstein subclass as a metric–form pair. This does not replace comparison with the complete article and later models. |
| [Apostolov–Drăghici, 2003 survey](https://faculty.fiu.edu/~draghici/research/paperfiles/survey-web.pdf), §6 | Describes the difficulty of negative Einstein strictly almost-Kähler four-dimensional geometry. | Historical context, not a current open-status certificate. |
| [Di Scala–Nagy, 2010](https://www.numdam.org/item/10.1016/j.crma.2010.01.005.pdf), Theorem 1.1 and Corollary 1.1 | Integrability/uniqueness for orthogonal almost-Kähler structures on specified Kähler–Einstein backgrounds, including the canonical complex-hyperbolic models. | Resolves a restricted background question; it does not exclude every other Einstein metric. |
| [Aazami–Ream, *Almost Kähler metrics and pp-wave spacetimes*, 2022](https://arxiv.org/pdf/2203.02825), Proposition 2 | Complete strictly almost-Kähler Riemannian metrics, including negative constant scalar curvature examples. | Negative scalar curvature alone is insufficient. The displayed Ricci tensor rules out nonzero Einstein constant in the standard construction; calculation below. |
| [Dekić, *Almost Kähler structures on complex hyperbolic space*, 2023](https://www.pmf.ni.ac.rs/filomat-content/2023/37-25/37-25-26-20476.pdf), Theorem 2.1 and Remark 2.2 | Left-invariant almost-Kähler metrics on the underlying solvable group. | In the identified standard Einstein case the structure is Kähler; strict cases do not provide Fino's required metric. |

For the Aazami–Ream family, Proposition 2 gives, in its orthonormal frame,
\[
\operatorname{Ric}(T,T)=\tfrac12\Delta H,\qquad
\operatorname{Ric}(Z,Z)=-\tfrac12\Delta H.
\]
If \(\operatorname{Ric}=\lambda g\), adding these equations gives \(2\lambda=0\). Therefore this family cannot answer the non-Ricci-flat question. This exclusion uses the actual tensor, rather than the words “complete” and “negative scalar curvature.”

Neutral-signature Walker examples, higher-dimensional examples, nearly Kähler examples and approximate Kähler–Einstein metrics also do not meet the stated Riemannian four-dimensional problem.

One further scope point matters for future comparison: a genuine local non-Ricci-flat strictly almost-Kähler Einstein metric on a coordinate ball can be pulled back to \(\mathbb R^4\), hence to its additive Lie-group manifold. It need not be complete. Consequently an earlier local construction could already answer Fino's original existence question even if its title never mentions Lie groups or Fino. The project's completeness claim would then be a separate strengthening to compare.

### What the project's files actually say

[A01 Step 58](/data/qiushi/qiushi_engine_v08/users/user2/Sessions/S1003A01/workspace/notes/step58_verified_bianchiVIII_AKE_and_closed_zero_locus.md) records a rational Bianchi VIII metric and compatible form with
\[
\operatorname{Ric}=-3g,\quad W^-=0,\quad
d\Omega=0,\quad|\Omega|^2=2,\quad
|\nabla\Omega|^2=\frac{36(1-p^2)^3}{(1+3p^2)^3}>0
\quad(1/3<p<1).
\]
The subsequent completion argument gives a smooth bolt, an infinite-distance end and a lift with underlying manifold \(\mathbb R^4\). Variation of \(|W^+|^2\) from \(2/3\) at the bolt to \(6\) at infinity establishes nonhomogeneity, hence excludes a left-invariant metric.

The follow-up examination described in Section 5 checks these properties using the complete October 8 manuscript and an actual run of its curvature program. They meet Fino's existence requirements and additionally give completeness. They do not answer the closed Goldberg problem.

The original research records are explicit about priority:

- [Step 58, §5](/data/qiushi/qiushi_engine_v08/users/user2/Sessions/S1003A01/workspace/notes/step58_verified_bianchiVIII_AKE_and_closed_zero_locus.md:190): Armstrong 2002 comparison unfinished; novelty unresolved.
- [Step 59, literature discussion](/data/qiushi/qiushi_engine_v08/users/user2/Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md:194): the complete pair remains usable independently of whether an equivalent metric occurs in Armstrong's ansatz; failure to identify it is not a priority result.
- [A02 Step 74](/data/qiushi/qiushi_engine_v08/users/user2/Sessions/S1003A02/workspace/notes/step74_packing_weyl_theorem_and_scope.md:142): records a Fino answer without a historical-first assertion.

The initial literature investigation inspected these statements and their formulas. The subsequent private-repository examination additionally ran the independent Koszul calculation and read the global completion proof; its concrete findings are recorded below.

**Status:** the examined construction supports an affirmative mathematical answer, including completeness. No earlier exact-scope answer was identified among the examined constructions. The full Armstrong comparison and wider equivalence comparison remain relevant to a claim of historical novelty or a first answer.

## 4. What can presently be said

The source-based description is:

> The project contains a solution manuscript for uniform separation of Kodaira-fibration Chern slopes from 3, based on its finite-density theorem, and a complete strictly almost-Kähler negative Einstein construction on \(\mathbb R^4\) answering Fino's existence question. The latter's exact curvature calculation was successfully rerun and its completion argument examined. The former's key analytic chain and full-scope application were read without finding a substantive error, but not every upstream spinor identity has been independently reconstructed. No earlier resolution in the same scope was found; neither historical-first claim is established by this report.

The consequential unfinished work is specific:

1. For a fully independent Kodaira proof reconstruction, complete the component-by-component derivation of the upstream cubic Dirac, torsion-curvature and first torsion-projection identities in the conventions used by FD2. The strong-current, resolvent, covariance, rank-one and application arguments are now available and have received substantive reading; this is no longer merely a check of the final slope substitution.
2. For Fino priority, obtain Armstrong 2002 in full and compare the metric/form pair and completion with its actual scope and subsequent models. The positive off-diagonal Weyl invariant already distinguishes the proposed pair from the weakly \(*\)-Einstein subclass. It does not by itself settle all historical equivalences.
3. Before a first-solution announcement, bring the full manuscripts and these exact questions to qualified independent readers. This is a remaining scholarly comparison, not an action taken in this investigation.

Searches covered the exact questions, Chern and relative slopes, two-orientation arguments, local and complete strictly almost-Kähler Einstein constructions, self-dual and Bianchi VIII models, cited antecedents and later papers. Full text was used where available; metadata-only and inaccessible material is identified above. The search found no evidence that the selected later papers solve the exact questions. It cannot prove that no other publication or equivalent construction exists.

The private-repository reading strengthens the mathematical assessment, especially for Fino. It does not turn a proof check into evidence of historical priority. Missing full chat exports are not a mathematical gap in these two arguments: their necessary proof texts have been located.

## 5. Private-repository proof examination

The complete repository was read locally at `/data/qiushi/research/Geometric-Analysis`. The repository and its original sources were not modified or republished.

| Material examined | Mathematical content checked |
| --- | --- |
| [Fino construction](../../Geometric-Analysis/archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex) | Explicit metric and form; positive signature on \(1/3<x<1\); polar smoothness over the weight-one plane bundle over \(\mathbb H^2\); triviality of that bundle; infinite radial distance and horizontal completeness; nonconstant Weyl norm. |
| [Exact curvature program](../../Geometric-Analysis/research/packages/Q3_Q4_Direct_Continuation_20261008--bfdaa282/Q4_independent_cartan.py) | Ran successfully with exit code 0. It computes curvature from frame brackets and Koszul's formula, and checks Ricci, both curvature blocks, closure, torsion norm and two Weyl-norm endpoint values. |
| [Strong-current argument](../../Geometric-Analysis/archive/originals/2026-09-29/O10_Strong_Current_Prerequisite.md) | Slow gradient truncation, derivative interchange without curvature derivatives, critical uniform integrability, and the passage from the bounded curvature fit to the full current derivative. |
| [Bounded resolvent](../../Geometric-Analysis/archive/originals/2026-09-29/O10_Direct_Resolvent_Prerequisite.md) | Direct \((4+\nabla^*\nabla)^{-1}\) construction, boundedness, strong \(H^1\) comparison and control without inserting a uniform Sobolev estimate. |
| [Scalar covariance and fifth line](../../Geometric-Analysis/archive/originals/2026-09-29/O10_Weak_Bianchi.md) | Mass–phase–Dirac reduction, the bounded test \(q/(1+q)\), the nonzero limiting modulus and the bundle power \(L^5\). |
| [Finite-density proof](../../Geometric-Analysis/archive/originals/2026-09-29/O10_All_Finite_Density.md) | Logarithmic resolvent selection, small transition-region gradient energy, rank-one transgression and the contradictory nonzero Chern-square density. The fixed-density dependence is retained. |
| [Integrated upstream source](../../Geometric-Analysis/archive/originals/2026-09-29/27b3cef6-aeed-442c-9e66-fef1a757828e.tex) | Relevant portions of `sec:bounded-forms`, `sec:single-parameter`, `sec:mixed-current` and `proof:zero-end-geometry:s14`: Hessian estimates, same-solution calibration, bounded ASD fit and the displayed full first torsion projection. This was targeted reading, not a review of every section. |
| [Two-orientation application](../../Geometric-Analysis/archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md) | Actual canonical classes in both orientations; the Hodge cross-pairing; the fixed density bound; parameter choice and the Kodaira Kähler–Einstein specialization. |

The [fifth-line algebra program](../../Geometric-Analysis/archive/originals/2026-09-29/verify_fifth_line_symbols.py) also ran with exit code 0. Its finite basis checks establish the stated Cartan and Clifford formulas, not the analytic convergence arguments.

A separate exact symbolic calculation checked the curvature program's input coefficients against the metric: \(v^2=G^{-1}\), \(H_i=A_i'/(2A_i)\), and \(V_i^2=GA_i/(A_jA_k)\), with signs supplied by the displayed structure equations. It checked the radial bolt expansion and \(A_2-A_3=(10/3)r^4+O(r^6)\). Thus the curvature run was not accepted solely because it used the same named coefficients as the manuscript.

The same calculation verified
\[
\left|\operatorname{pr}_{(\Omega/\sqrt2)^\perp}
W^+(\Omega/\sqrt2)\right|^2
=\frac{9(1-x^2)^3(9x^2-1)}{(1+3x^2)^4}>0
\]
on the regular domain. This is the concrete distinction from a weakly \(*\)-Einstein pair; no claim about every possible earlier Einstein model follows from it.

For FD2, the decisive contradiction is not merely almost-constant length of a section. The proof obtains a bounded first-derivative budget for a section of \(L^5\), selects a logarithmic regularization scale so that the transition energy vanishes, and uses the actual closed line curvature in Stokes' theorem. It then has both
\[
\frac{c_1(L^5)^2[M_j]}{V_j}\longrightarrow0,
\qquad
\frac{c_1(L^5)^2[M_j]}{V_j}
\longrightarrow\frac{25}{6\pi^2}.
\]
The bound on opposite Weyl energy used in producing this section depends on the fixed density bound. In the Kodaira application that bound is fixed because \(\chi/A_-=1/(4-r_K)\le1\). No unbounded-density theorem is being inserted.

The retained limitation is precise: the source contains explicit upstream spinor identities, which were traced and used in checking the analytic estimates, but this investigation has not independently recomputed all of their components from the Spin\(^{c}\) connection. The successful finite algebra and Fino curvature calculations should not be described as a machine verification of the entire FD2 theorem.
