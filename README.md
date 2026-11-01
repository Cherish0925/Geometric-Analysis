# Einstein Geometry on Four-Manifolds: Gaps, Curvature Extremals, and Realization

<strong>Shuxing Yang, Junyao Wu, Rui Zhao, Hongsheng Chen<sup>&#42;</sup>, Yihao Yang<sup>&#42;</sup></strong>  
College of Information Science and Electronic Engineering, Zhejiang University  
Qiushi Engine Team

<sup>&#42;</sup> Corresponding authors: [Hongsheng Chen](mailto:hansomchen@zju.edu.cn) and [Yihao Yang](mailto:yangyihao@zju.edu.cn).

[Manuscripts](manuscripts/README.md) · [Mathematical overview](docs/RESEARCH_MAP.md) · [Methods and references](docs/METHODS_AND_LITERATURE.md) · [BibTeX](CITATION.bib)

## Research

This collection studies Einstein metrics on smooth four-manifolds: their existence, approximation, curvature extrema, and degeneration. It relates integral curvature estimates to topology and Seiberg–Witten theory, develops geometric constructions for variational upper bounds, and investigates the integrability of almost-Kähler Einstein structures.

For a closed oriented smooth four-manifold, one of the central variational problems is

```math
P_*(M)=\inf_{g\in\mathcal G(M)}\int_M\left|\operatorname{Ric}_g-\frac{s_g}{4}g\right|_g^2\,dV_g,
```

where the infimum is taken over all smooth Riemannian metrics. The research concerns positive lower bounds, sharp upper bounds, smooth attainment, and the geometry of minimizing sequences. Normalized Einstein defects additionally describe separation from Einstein metrics with nonzero Einstein constant.

The analytic arguments use the differential compatibility of curvature and gauge fields. The constructions examine how background curvature interacts with blow-ups, orbifold resolutions, and collapsing regions. In almost-Kähler geometry, the Einstein equation is studied together with the equations for a compatible closed two-form.

## Manuscripts

| Title | Contents | Files |
|---|---|---|
| **Einstein Gaps on Four-Manifolds** | Trace-free Ricci estimates, parameter endpoints, two-orientation inequalities, Kodaira slopes, and Ricci flow. | [PDF](manuscripts/einstein_gaps.pdf) · [LaTeX](manuscripts/einstein_gaps.tex) |
| **Curvature Extremals on Four-Manifolds: Surgery, Orbifolds, and Attainment** | Strict surgery upper bounds, variational estimates, orbifold extrema, ALE degeneration, and smooth attainment. | [PDF](manuscripts/curvature_extremals.pdf) · [LaTeX](manuscripts/curvature_extremals.tex) |
| **Approximate Einstein Metrics and Geometric Realization in Dimension Four** | Fixed-manifold constructions, deformation theory, small eigenvalues, nonlinear correction, and geometric limits. | [PDF](manuscripts/einstein_realization.pdf) · [LaTeX](manuscripts/einstein_realization.tex) |
| **Almost-Kähler Einstein Four-Manifolds: Constructions and Rigidity** | Complete examples, torsion zeros, curvature identities, conditional rigidity, and the closed Goldberg problem. | [PDF](manuscripts/almost_kahler_einstein.pdf) · [LaTeX](manuscripts/almost_kahler_einstein.tex) |

## Mathematical exposition

Detailed expositions in Chinese provide the statements, proofs, constructions, and references for each subject:

- [Einstein gaps and parameter endpoints](docs/GAPS_AND_ENDPOINTS.md)
- [Curvature variation and extremal geometry](docs/CURVATURE_VARIATION.md)
- [Approximation and exact Einstein metrics](docs/CONSTRUCTIONS_AND_REALIZATION.md)
- [Almost-Kähler Einstein geometry](docs/GOLDBERG.md)

The [mathematical overview](docs/RESEARCH_MAP.md) explains the relations among these subjects and formulates the remaining problems. These include endpoint estimates without a topological density bound, sharp curvature extrema on smooth blow-ups, smooth attainment by non-Bach-flat metrics, Einstein existence on specified manifolds, and the closed negative Goldberg conjecture.

## Sources and computations

[Supplementary notes](research/notes/) and [computational programs](research/computations/) accompany the manuscripts. The [source guide](docs/COVERAGE.md) links the supporting mathematical texts; the [archive catalogue](catalog/README.md) contains earlier manuscripts, source packages, and their bibliographic records.

## Citation

Cite the relevant manuscript using [CITATION.bib](CITATION.bib). A citation for the collection is available in [CITATION.cff](CITATION.cff). See [authors and affiliation](AUTHORS.md), [edition information](manuscripts/VERSION.md), and [rights and permissions](RIGHTS.md).
