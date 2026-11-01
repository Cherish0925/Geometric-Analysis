# Manuscripts

<strong>Shuxing Yang, Junyao Wu, Rui Zhao, Hongsheng Chen<sup>&#42;</sup>, Yihao Yang<sup>&#42;</sup></strong>  
College of Information Science and Electronic Engineering, Zhejiang University  
Qiushi Engine Team

<sup>&#42;</sup> Corresponding authors: Hongsheng Chen ([hansomchen@zju.edu.cn](mailto:hansomchen@zju.edu.cn)) and Yihao Yang ([yangyihao@zju.edu.cn](mailto:yangyihao@zju.edu.cn)).

Four working manuscripts on Einstein geometry, curvature functionals, and almost-Kähler structures in dimension four.

| Title | Files | Pages | Contents |
|---|---|---:|---|
| **Einstein Gaps on Four-Manifolds** | [PDF](einstein_gaps.pdf) · [LaTeX](einstein_gaps.tex) | 21 | Gauge equations and curvature compatibility; normalized Einstein gaps; endpoint estimates with bounded Euler density; two-orientation applications. |
| **Curvature Extremals on Four-Manifolds: Surgery, Orbifolds, and Attainment** | [PDF](curvature_extremals.pdf) · [LaTeX](curvature_extremals.tex) | 19 | Curvature bounds from surgery; almost-minimizing sequences; exact orbifold infima; asymptotically locally Euclidean degeneration and attainment. |
| **Approximate Einstein Metrics and Geometric Realization in Dimension Four** | [PDF](einstein_realization.pdf) · [LaTeX](einstein_realization.tex) | 17 | Approximation on fixed manifolds; Teichmüller deformations; nonlinear correction of approximate metrics; orbifold resolutions and fillings. |
| **Almost-Kähler Einstein Four-Manifolds: Constructions and Rigidity** | [PDF](almost_kahler_einstein.pdf) · [LaTeX](almost_kahler_einstein.tex) | 18 | Complete noncompact constructions; torsion zeros and Green potentials; deformation and degeneration; rigidity on closed manifolds. |

## Supplementary exposition

The following expository chapters contain additional derivations and links to source proofs and computations:

- [Einstein gaps and endpoint estimates](../docs/GAPS_AND_ENDPOINTS.md).
- [Curvature extrema, constructions, and attainment](../docs/CURVATURE_VARIATION.md).
- [Approximation and exact Einstein metrics](../docs/CONSTRUCTIONS_AND_REALIZATION.md).
- [Almost-Kähler Einstein geometry](../docs/GOLDBERG.md).

The [research overview](../docs/RESEARCH_MAP.md) describes the relations among the results and the remaining open problems. The [source guide](../docs/COVERAGE.md) indexes the supplementary manuscripts.

## Citation

[CITATION.bib](../CITATION.bib) contains an entry for each manuscript and one for the collection. See [authors and correspondence](../AUTHORS.md) and the [version record](VERSION.md).

## Compilation

Each LaTeX source includes its bibliography and can be compiled independently. To regenerate all four PDFs, run:

```sh
make -C manuscripts
```
