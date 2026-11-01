# Working manuscripts

**Shuxing Yang, Junyao Wu, Rui Zhao, Hongsheng Chen<sup>*</sup>, Yihao Yang<sup>*</sup>**  
College of Information Science and Electronic Engineering, Zhejiang University  
Qiushi Engine Team

*Corresponding authors: Hongsheng Chen (hansomchen@zju.edu.cn) and Yihao Yang (yangyihao@zju.edu.cn).*

Version 1.0, 1 November 2026. These working manuscripts organize the current research into four complementary papers. Each includes definitions, principal statements, mathematical arguments, references, and its remaining questions. Detailed source proofs and computations are linked at the point of use. The repository also retains the underlying research manuscripts.

| Manuscript | Files | Pages | Scope |
|---|---|---:|---|
| **Einstein Gaps on Four-Manifolds** | [PDF](einstein_gaps.pdf) · [LaTeX](einstein_gaps.tex) | 20 | Gauge-field compatibility, normalized gaps, finite-density endpoints, two-orientation applications, and Ricci flow consequences. |
| **Curvature Extremals on Four-Manifolds: Surgery, Orbifolds, and Attainment** | [PDF](curvature_extremals.pdf) · [LaTeX](curvature_extremals.tex) | 19 | Strict surgery bounds, variational selection, orbifold extrema, ALE transfer, and attainment. |
| **Approximate Einstein Metrics and Geometric Realization in Dimension Four** | [PDF](einstein_realization.pdf) · [LaTeX](einstein_realization.tex) | 17 | Pointwise approximation, fixed-manifold constructions, slow modes, nonlinear repair, and marked fillings. |
| **Almost-Kähler Einstein Four-Manifolds: Constructions and Rigidity** | [PDF](almost_kahler_einstein.pdf) · [LaTeX](almost_kahler_einstein.tex) | 19 | Complete noncompact examples, torsion zeros, Green potentials, moduli, degeneration, and the closed Goldberg problem. |

## Relation to the mathematical sources

The four papers respectively develop the analytic obstruction, variational, realization, and almost-Kähler branches of a common research programme on four-dimensional Einstein geometry. A shared geometric question does not identify the hypotheses of the four branches: every use of a gap estimate, a compactness theorem, a reconstruction theorem, or a curvature identity retains its stated assumptions.

- [Einstein Gaps on Four-Manifolds](../docs/GAPS_AND_ENDPOINTS.md): maintained detailed exposition and source references.
- [Curvature Extremals on Four-Manifolds: Surgery, Orbifolds, and Attainment](../docs/CURVATURE_VARIATION.md): maintained detailed exposition and source references.
- [Approximate Einstein Metrics and Geometric Realization in Dimension Four](../docs/CONSTRUCTIONS_AND_REALIZATION.md): maintained detailed exposition and source references.
- [Almost-Kähler Einstein Four-Manifolds: Constructions and Rigidity](../docs/GOLDBERG.md): maintained detailed exposition and source references.

Classical results retain their original citations. Open statements, including the unrestricted endpoint problem, general smooth curvature extrema and attainment, and the closed negative Goldberg conjecture, are stated as questions rather than theorem conclusions.

## Citation and compilation

Use the individual BibTeX entry in [CITATION.bib](../CITATION.bib) when citing one paper. Use the collection entry for the research programme as a whole. Authorship and correspondence are listed in [AUTHORS.md](../AUTHORS.md).

Each source is standalone and uses an inline bibliography. Run `make -C manuscripts` with a standard LaTeX installation to regenerate the PDFs. The papers are working manuscripts; no journal publication or arXiv identifier is assigned in this version.
