# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A03/workspace/notes/step8_cover_mean_transport_and_model_scope_corrections.md",
    "Sessions/S0910A01/workspace/notes/step10_accessible_cover_reassessment.md"
  ]
}
```

## Task

Verify or refute the following regularity claim and identify the precise obstruction if false:

CLAIM (the regularity question): On a 4-dimensional Riemannian ball (B_1(p), g) with Ric ≥ -3g that arises as the local universal cover of a collapsed near-Einstein ball, suppose:
(a) fint_{B_r(p)} |Rm|² ≤ K for all 0 < r ≤ 1/3 (controlled maximal curvature function)
(b) Ric ≥ -(1+δ)(n-1)g with δ small

Does (a)+(b) force Vol(B_{r*}(p)) ≥ c(K)r*⁴ for some fixed r*(K) > 0?

Consider:
1. Known ε-regularity theorems (Anderson, Cheeger-Naber) and whether they apply without noncollapse as input
2. Whether the 4D conformal invariance of ∫|Rm|² adds structure
3. Whether a countermodel exists: a collapsed ball with Ric ≥ -3g, controlled normalized curvature mean at every scale, and Vol → 0
4. The distinction between 'local universal cover' and 'arbitrary ball' - the cover has no short loops
5. Whether Naber-Zhang Prop 6.4 hypotheses (GH model, maximal rank, model noncollapsing) follow from (a)+(b)

Give a precise mathematical assessment, not a survey.

## Output

## Scientific memo

### Assessment

The proposed implication is false. Even the stronger equation

\[
\operatorname{Ric}_g=-g
\]

does not turn the centered bounds

\[
\fint_{B_r(p)}|\operatorname{Rm}|^2\le K,\qquad 0<r\le \tfrac13,
\]

into a four-dimensional volume lower bound on the local universal cover.

The geometric obstruction is a collapsed circle that is contractible inside the unit ball through a “nut” region lying farther than \(1/3\) from the center. The universal cover therefore does not unwrap that circle, while the centered curvature means through radius \(1/3\) do not see the contraction region.

---

## 1. Exact Einstein countermodel

Let \(\ell=\sqrt3\), let \(\nu>0\), and define

\[
F_\nu(r)
=
\frac{r-\nu}{r+\nu}
\left(
1+\frac{(r-\nu)(r+3\nu)}{\ell^2}
\right),
\qquad r\ge \nu .
\]

On coordinates
\[
\theta\in[0,\pi],\quad \phi\in\mathbb R/2\pi\mathbb Z,
\quad \psi\in\mathbb R/4\pi\mathbb Z,
\]
consider the Taub–NUT–AdS metric

\[
g_\nu
=
\frac{dr^2}{F_\nu(r)}
+(r^2-\nu^2)(d\theta^2+\sin^2\theta\,d\phi^2)
+4\nu^2F_\nu(r)(d\psi+\cos\theta\,d\phi)^2.
\tag{1}
\]

Direct substitution in the cohomogeneity-one Einstein equations gives

\[
\operatorname{Ric}_{g_\nu}
=
-\frac{3}{\ell^2}g_\nu=-g_\nu.
\tag{2}
\]

Thus this family satisfies much more than the Ricci lower estimates in the question.

### Smooth nut

Set

\[
r=\nu+\frac{\rho^2}{8\nu}.
\]

Since

\[
F_\nu(r)=\frac{\rho^2}{16\nu^2}+O(\rho^4),
\]

the metric near \(r=\nu\) becomes

\[
g_\nu
=
d\rho^2+
\frac{\rho^2}{4}
\left[
d\theta^2+\sin^2\theta\,d\phi^2+
(d\psi+\cos\theta\,d\phi)^2
\right]
+O(\rho^4).
\]

The bracket divided by \(4\) is the round metric on \(S^3\). Hence \(r=\nu\) is a smooth point, the nut, and the manifold is smooth and simply connected near it.

---

## 2. Choice of center and uniform curvature means

Let

\[
t_\nu(r)=\int_\nu^r F_\nu(u)^{-1/2}\,du
\]

be radial distance from the nut. Choose \(p_\nu\) with

\[
t_\nu(p_\nu)=d_0=\frac12 .
\]

For every \(q\in B_{1/3}(p_\nu)\), the triangle inequality gives

\[
\frac16
<
d(q,\mathrm{nut})
<
\frac56.
\tag{3}
\]

Consequently these balls lie in an annulus uniformly separated from the nut. On this annulus the coefficients in (1), expressed in an orthonormal frame, and all curvature expressions are uniformly bounded as \(\nu\to0\). Equivalently, the explicit rational curvature expressions have denominators bounded away from zero there. Thus there is a finite constant \(K_0\), independent of \(\nu\), such that

\[
\sup_{B_{1/3}(p_\nu)}|\operatorname{Rm}_{g_\nu}|^2\le K_0.
\]

It follows immediately that

\[
\fint_{B_r(p_\nu)}|\operatorname{Rm}_{g_\nu}|^2\le K_0
\qquad
\text{for every }0<r\le\frac13.
\tag{4}
\]

This is stronger than the requested centered maximal-function estimate.

---

## 3. Collapse of every fixed centered ball

The volume form of (1) is

\[
d\mu_{g_\nu}
=
2\nu(r^2-\nu^2)\sin\theta\,
dr\,d\theta\,d\phi\,d\psi .
\tag{5}
\]

For fixed \(s\le1/3\), equation (3) places \(B_s(p_\nu)\) in an \(r\)-interval whose endpoints remain in a fixed compact subset of \((0,\infty)\). Integrating (5) over the entire corresponding angular region gives

\[
\operatorname{Vol}_{g_\nu}(B_s(p_\nu))
\le C_s\nu.
\tag{6}
\]

Hence, for every fixed \(s\in(0,1/3]\),

\[
\frac{\operatorname{Vol}_{g_\nu}(B_s(p_\nu))}{s^4}
\longrightarrow0.
\tag{7}
\]

In particular, no positive \(c(K_0)\) and no fixed \(r_*(K_0)\le1/3\) can satisfy the proposed lower estimate.

---

## 4. Why the local universal cover remains collapsed

Let

\[
U_\nu=B_1(p_\nu).
\]

The short \(\psi\)-orbit through \(p_\nu\) has length \(O(\nu)\). It contracts through the two-dimensional radial cigar

\[
D_\nu
=
\{\,\nu\le r\le r(p_\nu),\ 
\theta=\theta_0,\ \phi=\phi_0,\ \psi\in S^1\,\},
\]

because the \(\psi\)-circle shrinks to a point at \(r=\nu\).

Every point of this cigar can be reached from \(p_\nu\) by first moving along at most half of the \(\psi\)-orbit and then moving radially. Therefore

\[
D_\nu\subset B_{d_0+C\nu}(p_\nu)\subset U_\nu
\]

for small \(\nu\). The short fiber generator is consequently trivial in \(\pi_1(U_\nu)\).

To see the effect on the covering ball, project the annular region to the three-dimensional base with metric

\[
h_\nu
=
\frac{dr^2}{F_\nu(r)}
+(r^2-\nu^2)d\Omega_2^2.
\]

An enlarged base ball containing the projection of \(B_{1/3}(p_\nu)\) is contractible and stays away from the nut. Its inverse image \(W_\nu\) is a circle bundle over a contractible set, so

\[
\pi_1(W_\nu)\cong\mathbb Z,
\]

generated by the short \(\psi\)-circle. The inclusion

\[
\pi_1(W_\nu)\longrightarrow\pi_1(U_\nu)
\]

is the zero map because the generator bounds \(D_\nu\).

Therefore each component of the lift of \(W_\nu\) to the universal cover of \(U_\nu\) maps one-to-one onto \(W_\nu\). For every fixed \(s\le1/3\),

\[
B_s(\widetilde p_\nu)
\]

lies in such a component and is isometric to the corresponding downstairs ball. Thus

\[
\operatorname{Vol}(B_s(\widetilde p_\nu))
\le C_s\nu\longrightarrow0.
\tag{8}
\]

The phrase “the universal cover has no short loops” is mathematically insufficient: it has no loops representing a nontrivial element of the ambient fundamental group. Short contractible loops remain, and here they are exactly the collapsing directions.

---

## 5. Relation to \(\varepsilon\)-regularity

The countermodel also isolates why the standard regularity theorems do not apply.

From (4), (6),

\[
\int_{B_s(p_\nu)}|\operatorname{Rm}|^2
\le K_0C_s\nu\longrightarrow0.
\tag{9}
\]

Thus the absolute four-dimensional curvature energy tends to zero, and the metrics are exactly Einstein. Nevertheless their volume ratios tend to zero.

Anderson-type \(\varepsilon\)-regularity requires a volume-ratio or Sobolev input to obtain a harmonic-radius or injectivity-radius estimate. Cheeger–Naber’s codimension-four theory likewise starts from quantitative noncollapse. Without that input, small \(L^2\) curvature energy can coexist with collapse, as (9) shows.

Curvature regularity by itself would not help here: the curvature is already uniformly bounded on the tested annulus. The missing quantity is four-dimensional geometric size.

---

## 6. Four-dimensional conformal invariance

The identity that

\[
\int |\operatorname{Rm}|^2\,d\mu
\]

is invariant under a global homothety in dimension four gives no volume-ratio information. The degeneration in (1) is not a common homothety: one circle direction has length \(O(\nu)\), while the three-dimensional base remains at fixed scale. Consequently both volume and absolute curvature energy of the tested ball are \(O(\nu)\), while their quotient stays bounded.

Thus conformal criticality supplies neither a Sobolev constant nor an injectivity-radius estimate.

---

## 7. Naber–Zhang interface

As \(\nu\to0\), the annular balls converge in the GH sense to the smooth three-dimensional metric

\[
h_0
=
\frac{dr^2}{1+r^2/3}+r^2d\Omega_2^2,
\]

which is hyperbolic three-space with sectional curvature \(-1/3\). The lower-dimensional model has a fixed noncollapsing radius.

Here the collapsed-limit dimension is \(k=3\), so maximal fibered nilpotency rank would require rank

\[
4-k=1.
\]

Instead, the short circle generator contracts through the nut inside \(B_1(p_\nu)\), and hence its image in the buffered ball’s fundamental group is trivial. The fibered group has rank zero.

Therefore:

- a smooth GH model is present;
- the model scale is uniformly noncollapsed;
- the curvature mean is uniformly controlled;
- the metric is exactly Einstein;
- maximal fiber rank is absent.

This directly shows that the Naber–Zhang rank hypothesis does not follow from the two estimates in the question. Proposition 6.4 is fully consistent with the example: its essential topological input is precisely what excludes this nut-capped collapse.

---

## 8. Additional elementary model for the formal Ricci-lower assumptions

If one retains only the written Ricci lower estimate, an even simpler family is

\[
dt^2+a^2(\sigma_1^2+\sigma_2^2+\varepsilon^2\sigma_3^2)
\quad\text{on }\mathbb R\times S^3,
\]

where \(\sigma_i\) are standard left-invariant forms. Its sectional curvatures are

\[
0,\qquad
\frac{4-3\varepsilon^2}{a^2},\qquad
\frac{\varepsilon^2}{a^2},\qquad
\frac{\varepsilon^2}{a^2}.
\]

Hence \(\operatorname{Ric}\ge0\) and \(|\operatorname{Rm}|^2\le C a^{-4}\), uniformly in \(\varepsilon\). Choosing fixed \(a\) so that the Berger sphere has diameter below \(1\), the unit ball retracts to \(S^3\) and is simply connected, yet every fixed ball has volume \(O(\varepsilon)\). This shows that simple connectivity plus even a pointwise full-curvature bound does not exclude collapse by contractible Hopf circles.

The Taub–NUT–AdS family is stronger for the research setting because it also satisfies \(\operatorname{Ric}=-g\) exactly.

---

## Conclusion

The regularity implication is false. The precise obstruction is:

\[
\boxed{\text{rank-dropping collapse along short contractible fibers}}
\]

whose contraction region lies inside the unit cover domain but outside the centered scales on which curvature means are controlled. The local universal cover unwraps only fiber classes that survive in the buffered domain’s fundamental group. Conditions (a) and (b) contain no quantitative information about that survival, so they do not furnish the maximal-rank hypothesis used by Naber–Zhang and do not imply any fixed four-dimensional volume ratio.