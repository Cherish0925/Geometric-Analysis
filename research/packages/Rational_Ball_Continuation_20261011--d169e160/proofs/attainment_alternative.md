# Unrestricted optimal metrics: direct alternatives and a curvature obstruction

11 October 2026. This investigation concerns only

\[
P_*(M)=\inf_{g\in\operatorname{Met}(M)}\int_M|\operatorname{Ric}^{\circ}_g|^2\,dV_g.
\]

It did not produce a smooth non-Bach-flat global minimizer. The useful outcome is a precise restriction on any such minimizer, derived from classical critical-metric identities. It does not replace the attainment problem.

## 1. The original question and the explicit-model routes

LeBrun's 2004 *Curvature Functionals, Optimal Metrics, and the Differential Topology of 4-Manifolds*, Section 11, asks whether a compact optimal metric can fail to be Bach-flat. Optimal means the absolute minimum over all smooth metrics. The identity

\[
\int_M|\operatorname{Rm}_{\mathrm{op}}|^2=8\pi^2\chi(M)+P(g)
\]

makes this exactly the problem above. Source: https://arxiv.org/pdf/math/0404251 , PDF pp.39--40.

The project's previous notes already close the most obvious explicit alternatives:

* Every closed locally homogeneous P-critical metric is Einstein or the scalar-flat product of two opposite-curvature surfaces, hence Bach-flat. This uses the homogeneous classification at its parameter t=-1/4.
* Every closed Kähler P-critical metric is Einstein or scalar-flat Kähler, hence Bach-flat. The proof varies the Kähler class after the conformal equation has forced constant scalar curvature.
* Reversing orientation does not alter P or Bach-flatness.
* A minimizer of a different curvature functional, or a conformal minimum, is not an unrestricted P-minimizer.

These inherited exclusions appear in `research_q2_sprint_20261008/q3_direct_minimizer_followup.md`. They are not new contributions of this continuation.

## 2. Exact critical-point identity

Write E=Ric-(s/4)g. At a smooth closed P-critical metric the scalar curvature is constant, and

\[
\int_M|\nabla E|^2=2\int_M\operatorname{Rm}(E,E).
\tag{1}
\]

For constant scalar curvature the Cotton tensor is

\[
C_{ijk}=\nabla_kE_{ij}-\nabla_jE_{ik}.
\]

Catino's integrated Codazzi identity gives

\[
\int_M\left(|\nabla E|^2-\frac12|C|^2\right)
=\int_M\left[\operatorname{Rm}(E,E)-\operatorname{tr}(E^3)-\frac{s}{4}|E|^2\right].
\tag{2}
\]

Combining (1) and (2), and diagonalizing E at a point, with eigenvalues lambda_i and sectional curvatures K_ij, yields

\[
\frac12\int_M|C|^2
=\int_M\sum_{i<j}K_{ij}(\lambda_i+\lambda_j)^2.
\tag{3}
\]

Indeed Ric has eigenvalues lambda_i+s/4 and

\[
\operatorname{Rm}(E,E)+\operatorname{tr}(E^3)+\frac{s}{4}|E|^2
=\sum_{i<j}K_{ij}(\lambda_i+\lambda_j)^2.
\]

Equations (1)--(3) are classical identities, not a new estimate. Their exact source is Catino, *Some rigidity results on critical metrics for quadratic functionals*, arXiv:1404.0569, Proposition 4.1, Proposition 4.2 and the proof of Theorem 1.4: https://arxiv.org/pdf/1404.0569 .

## 3. Biorthogonal-curvature consequence

For a two-plane pi define

\[
K^\perp(\pi)=\frac12\{K(\pi)+K(\pi^\perp)\}.
\]

Since trace E=0, the squared sums for complementary pairs agree. Therefore (3) can be grouped as

\[
\frac12\int_M|C|^2
=2\int_M\sum_{j=2}^4 K^\perp(e_1\wedge e_j)(\lambda_1+\lambda_j)^2.
\tag{4}
\]

The expression is independent of the choice of eigenbasis through its invariant form in (3).

**Consequence.** If a closed oriented four-manifold has nonzero signature and a P-critical metric with K^perp<=0 on every plane, that metric is Einstein.

Proof: (4) forces C=0. Together with constant scalar curvature this gives harmonic Riemann curvature. Bourguignon's theorem then gives Einstein when the signature is nonzero. The theorem is *Les variétés de dimension 4 à signature non nulle dont la courbure est harmonique sont d'Einstein*, Invent. Math. 63 (1981), 263--286. Bibliographic/original-source entry: https://eudml.org/doc/142798 .

If K^perp<=-b<0, the signature assumption is unnecessary: the elementary identity

\[
\sum_{j=2}^4(\lambda_1+\lambda_j)^2=|E|^2
\]

makes the right side of (4) at most -2bP, so E=0 directly.

This is an immediate consequence of classical identities and rigidity, not a claim of a new major theorem or a solution to LeBrun's question.

## 4. Implication for the current candidate

On the Horikawa single blowup, tau=-24 and no Einstein metric exists by the already available classical obstruction. Consequently any smooth global P-minimizer, if it exists, must have positive biorthogonal curvature somewhere. Negative Yamabe type does not prevent this: it fixes the sign of the constant scalar curvature, not of every sectional or biorthogonal curvature.

Thus an attempted construction constrained to a homogeneous model, a Kähler metric, or an everywhere nonpositively biorthogonally curved geometry cannot yield the desired example. An unrestricted minimizer would have to have a genuinely different local curvature arrangement. This is a necessary condition, not an existence or compactness argument.

## 5. Remaining conclusion

No direct closed example with a proved unrestricted global lower bound and a non-Bach-flat equality metric was found. The existing strict P upper bound and Einstein exclusion still reduce the selected example to smooth attainment. Ordinary Ricci-flat ALE bubbling is not removed by any argument in this note. In particular, the critical-point identity (4) must not be applied to an arbitrary near-minimizing sequence without a justified test and derivative bound.
