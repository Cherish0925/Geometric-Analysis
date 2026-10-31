# A compact-regime Einstein realization theorem on aspherical four-manifolds

23 September 2026. Research continuation; standard geometric compactness
inputs are separated from the new application of the compact-core exclusion.
The result concerns the original pointwise Ricci defect, not a replacement
by a volume-normalized integral defect.

## 1. Statement and mathematical increment

For a closed Riemannian four-manifold define
\[
 \delta_-(g)=\|\operatorname{Ric}_g^{\sharp}+I\|_{L^\infty,\mathrm{op}}.
\]
All Weyl norms below are tensor norms; a fixed equivalent curvature-operator
norm changes only constants. An oriented manifold is **aspherical** when
its universal cover is contractible.

**Theorem A (compact-regime realization).** Fix
\(D,v,\Lambda>0\) and \(2<q<\infty\). There exists
\(\varepsilon(D,v,\Lambda,q)>0\) with the following property. If a
closed connected smooth oriented aspherical four-manifold \(M\) carries
a smooth metric \(g\) satisfying
\[
 \operatorname{diam}(M,g)\le D,\qquad
 \operatorname{Vol}(M,g)\ge v,\qquad
 \|W_g^+\|_{L^q(M,g)}\le\Lambda,\qquad
 \delta_-(g)<\varepsilon,
                                                        \tag{1}
\]
then the **same smooth manifold** carries a smooth metric \(h\) with
\[
                         \operatorname{Ric}_h=-h.        \tag{2}
\]
The threshold is uniform across the manifolds satisfying (1). One may
replace \(W^+\) by \(W^-\), by reversing orientation. A pointwise bound
on one Weyl half is a sufficient special case, since volume has a
diameter-dependent upper bound under the Ricci bounds in (1).

No bound on \(\nabla\operatorname{Ric}\), the full pointwise curvature,
Euler characteristic, injectivity radius, or a separately supplied full
curvature energy occurs in the theorem. The volume, diameter, and
supercritical one-sided Weyl assumptions are genuine restrictions. In
particular, the threshold is not dimension-only.

The preceding [aspherical compact-core exclusion and exact no-bubbling
theorem](../mathematics/current/line1_aspherical_no_bubbles.md) used
Einstein regularity after rescaling a maximum of the full curvature.
That proof does **not** apply verbatim to almost-Einstein metrics. The
new argument normalizes a harmonic radius instead. Ricci convergence
in the harmonic-coordinate elliptic equation supplies precisely the
regularity needed for a smooth Einstein limit and for preservation of
the smooth type; derivatives of the Ricci error are never estimated.

## 2. Inputs, with the regularity actually used

We use the following results.

1. The inherited compact-core lemma states that no large compact core
   of a nonflat smooth Ricci-flat anti-self-dual ALE four-manifold
   embeds smoothly into a closed aspherical four-manifold. Its proof
   treats both the negative-definite \(b_2>0\) case and the rational-ball
   \(b_2=0\) case. For the latter, lifting the core to the contractible
   universal cover and applying integral Mayer--Vietoris would give
   \(\mathbb Z_{n^2}\cong\mathbb Z_n\oplus G\), \(|G|=n\), which is
   impossible. The classification inputs are Wright and Suvaina.
2. Uniform harmonic-coordinate radii give pointed geometric
   \(C^{1,\alpha}\) precompactness, with a loss of Hölder exponent
   before using the metric equation. On harmonic charts,
   \[
     g^{ab}\partial_a\partial_b g_{ij}
        =-2\operatorname{Ric}_{ij}+Q_{ij}(g,\partial g), \tag{3}
   \]
   where \(Q\) is quadratic in first derivatives. Bounded Ricci and
   controlled charts give local \(W^{2,p}\) bounds for every finite
   \(p\). Strong convergence of the right side gives strong
   \(W^{2,p}\) convergence on smaller charts. These are the harmonic
   coordinate compactness tools of Anderson; the strong convergence
   step is also discussed explicitly by Zhang--Zhu.
3. Jiang--Naber's local \(L^2\) curvature estimate applies to
   noncollapsed balls with two-sided bounded Ricci curvature, without
   any derivative bound on Ricci. With fixed diameter and positive
   total volume it gives a uniform global \(L^2\) curvature bound in
   dimension four. Section 3 records the covering argument.
4. A complete Ricci-flat four-manifold with Euclidean lower volume
   growth and finite \(L^2\) curvature is ALE, by the
   Bando--Kasue--Nakajima asymptotic theorem, Theorem 1.5; in dimension
   four the resulting ALE order is four. This result is applied
   only to a smooth, complete **exact Ricci-flat limit**, not to the
   original approximate metrics.

These inputs do not include an assertion that an almost-Einstein
sequence converges smoothly. The convergence established below is
\(C^{1,\alpha}\) and strong \(W^{2,p}\) for finite \(p\), after
diffeomorphisms. The limiting metric is smooth by (3).

## 3. Noncollapse and curvature energy from the bounded global regime

Fix a two-sided Ricci bound \(|\operatorname{Ric}|\le K\), diameter
bound \(D\), and volume lower bound \(v\). Set \(D_*=D+1\). Relative
Bishop--Gromov comparison gives, for all \(x\in M\) and
\(0<r\le D_*\),
\[
 \operatorname{Vol}B_r(x)
   \ge v\,\frac{V_{-K/3}(r)}{V_{-K/3}(D_*)}
   \ge c(K,D,v)r^4.                                    \tag{4}
\]
Here \(V_{-K/3}\) denotes the four-dimensional model-ball volume;
using a larger negative comparison constant causes no problem.
The same comparison gives
\(\operatorname{Vol}(M)\le V_{-K/3}(D_*)\).

Choose a fixed small radius \(r_*=r_*(K,D)>0\). A maximal disjoint
collection of \(r_*/4\)-balls has uniformly bounded cardinality by
(4) and the total-volume upper bound. The concentric \(r_*/2\)-balls
cover \(M\). On these balls the rescaled Ricci bound and volume lower
bound meet Jiang--Naber's hypotheses, with constants depending only
on \(K,D,v\). Summing their estimates gives
\[
                 \int_M|\operatorname{Rm}|^2\le E(K,D,v).
                                                               \tag{5}
\]
Thus neither a bound on \(\chi(M)\) nor an additional curvature-energy
assumption is needed. If one elects not to use the Jiang--Naber
theorem, all subsequent statements remain valid with (5) supplied as
an extra hypothesis and constants also depending on that energy bound.

## 4. Half-Weyl control prevents harmonic-radius collapse

**Theorem B (harmonic compactness).** Given
\(K,D,v,\Lambda>0\), \(q>2\), and \(0<\alpha<1\), there is a
positive uniform lower bound for the \(C^{1,\alpha}\) harmonic radius
on every closed connected smooth oriented aspherical four-manifold
with
\[
 |\operatorname{Ric}|\le K,\quad \operatorname{diam}\le D,
 \quad\operatorname{Vol}\ge v,
 \quad\|W^+\|_{L^q}\le\Lambda.                         \tag{6}
\]
Consequently this class is geometrically precompact in
\(C^{1,\beta}\), \(\beta<1\), and weak \(W^{2,p}\), \(p<\infty\),
and has only finitely many diffeomorphism types.

**Proof.** Fix a standard harmonic-radius definition with metric
comparability and scaled \(C^{1,\alpha}\) norm bounded by fixed
constants. Suppose its global minimum \(\rho_j\), attained at
\(x_j\), tends to zero. Write
\[
 \widehat g_j=\rho_j^{-2}g_j,
 \quad r_h(\widehat g_j,x_j)=1,
 \quad r_h(\widehat g_j,x)\ge1\quad\hbox{for all }x.      \tag{7}
\]
The rescaled Ricci tensors satisfy
\[
                |\operatorname{Ric}_{\widehat g_j}|
                     \le K\rho_j^2\longrightarrow0.   \tag{8}
\]
For any fixed \(R\), (4) gives, for large \(j\),
\[
        \operatorname{Vol}_{\widehat g_j}B_R(x_j)
                          \ge c(K,D,v)R^4.              \tag{9}
\]
The lower volume and Ricci bounds ensure that the rescaled diameters
tend to infinity. Indeed, the unscaled diameters have a positive
lower bound from \(v\) and Bishop comparison.

The uniform harmonic charts in (7), bounded numbers of charts on each
fixed-radius ball, and completeness produce pointed
\(C^{1,\beta}\) convergence on compact sets, \(\beta<\alpha\), to a
complete smoothable manifold \((X,g_\infty,x_\infty)\). Initially the
limiting metric has only the indicated low regularity. Equation (3)
and (8) imply distributionally \(\operatorname{Ric}(g_\infty)=0\).
Local elliptic bootstrapping in harmonic coordinates makes
\(g_\infty\) smooth and Ricci-flat.

It is important that convergence can now be improved without
differentiating (8). In compatible harmonic charts, subtract the
limiting version of (3). For \(u_j=g_j-g_\infty\), the right side of
the resulting uniformly elliptic equation is a sum of
\[
 -2\operatorname{Ric}_{g_j},\qquad
 Q(g_j,\partial g_j)-Q(g_\infty,\partial g_\infty),\qquad
 (g_\infty^{ab}-g_j^{ab})\partial_a\partial_b g_\infty.
                                                               \tag{10}
\]
Each tends to zero in \(L^p\) on compact smaller charts for every
finite \(p\), by (8), the initial \(C^1\) convergence, and smoothness
of the limit. Interior elliptic estimates imply
\[
                    g_j\longrightarrow g_\infty
                    \quad\hbox{strongly in }W^{2,p}_{\rm loc}
                    \quad(p<\infty).                   \tag{11}
\]
Choose \(p>4/(1-\alpha)\) to recover strong \(C^{1,\alpha}\)
convergence. Harmonic-coordinate transition maps are controlled by
their own harmonic equations; the usual geometric compactness
construction yields embeddings of compact subsets. More explicitly,
take an open neighbourhood of any chosen smooth compact core of the
limit and a finite harmonic atlas there. Controlled transition maps
give a common \(C^1\) differentiable structure and \(C^1\) embeddings
into the approximating smooth manifolds. A compatible smoothing of
this atlas is unique up to diffeomorphism; \(C^1\) approximation of
each embedding by a smooth map remains an embedding on the compact
core. This preserves its smooth type. No convergence of holomorphic
curves or \(C^2\) convergence of the approximating metrics is used.

The limit is not flat. If it were flat, (9) forces it to be Euclidean
space: a complete flat quotient with an infinite deck group has
sub-Euclidean volume growth, and a finite Euclidean isometry group
acting freely is trivial. Equivalently, the ALE conclusion below also
excludes every nontrivial smooth flat limit with (9). On a fixed
Euclidean ball of radius greater than two there are harmonic charts
with strict margins in all defining inequalities. Strong convergence
in (11), followed by solving the harmonic coordinate Dirichlet problem
on a slightly smaller ball, gives such a chart of radius greater than
one on \((M_j,\widehat g_j,x_j)\). This contradicts (7). This is the
harmonic-radius normalization argument, not an assertion that a
pointwise maximum of curvature survives weak convergence.

Under the rescaling in (7), the half-Weyl norm has the decisive
transformation rule
\[
 \int_{M_j}|W^+_{\widehat g_j}|^q\,d\mu_{\widehat g_j}
       =\rho_j^{2q-4}\int_{M_j}|W^+_{g_j}|^q\,d\mu_{g_j}
       \le\rho_j^{2q-4}\Lambda^q\longrightarrow0.        \tag{12}
\]
By (11), curvature converges strongly in local finite \(L^p\) spaces.
The Hodge star also converges, so (12) implies \(W^+_{g_\infty}=0\).
The full \(L^2\) curvature is scale invariant in dimension four;
(5), (11), and exhaustion imply
\[
                       \int_X|\operatorname{Rm}_{g_\infty}|^2
                              \le E(K,D,v).              \tag{13}
\]
Equations (9), (13), and Ricci-flatness place the complete nonflat
limit within the Bando--Kasue--Nakajima ALE theorem. It is therefore
a smooth nonflat ASD Ricci-flat ALE four-manifold. Its end is unique:
a complete Ricci-flat manifold with two ends splits as a line times
a compact manifold, which is incompatible with (9). The finite
fundamental group, negative-definite intersection form, and the
rational-ball alternatives used by the compact-core lemma are supplied
by Wright's classification; simple connectivity is not assumed.

Choose a sufficiently large compact core \(B\subset X\). The compact
geometric convergence embeds \(B\) into \(M_j\) for large \(j\),
contradicting the inherited aspherical compact-core exclusion. Thus
the assumed convergence \(\rho_j\to0\) is impossible, proving the
uniform harmonic-radius bound.
Standard finite-atlas geometric compactness, using the fixed diameter,
now proves the final assertions of the theorem. \(\square\)

**Endpoint variation.** The same argument permits the \(L^q\) bound
in (6) to be replaced by uniform local equiintegrability of one Weyl
half:
\[
 \sup_{(M,g)}\sup_{x\in M}
       \int_{B_r(x)}|W^+|^2\,d\mu\le\eta(r),
              \qquad \eta(r)\longrightarrow0\ (r\downarrow0).
                                                               \tag{14}
\]
Indeed the integral on every fixed rescaled ball is bounded by
\(\eta(R\rho_j)\to0\). Constants then depend on the common modulus
\(\eta\). A bare bounded critical \(L^2\) norm does **not** supply
(14); the proof makes no assertion at that unrestricted endpoint.

## 5. Proof of exact realization on the same smooth manifold

Suppose Theorem A fails. There are closed aspherical \(M_j\) and
metrics satisfying its fixed \(D,v,\Lambda,q\) bounds such that
\(\delta_-(g_j)\to0\), but no \(M_j\) admits a normalized negative
Einstein metric. Discard finitely many terms so that
\(\delta_-(g_j)\le1/2\). This gives a fixed two-sided Ricci bound.

Theorem B and compact geometric convergence give, after a subsequence,
a fixed closed smooth \(M_\infty\), diffeomorphisms
\(\phi_j:M_\infty\to M_j\), and
\[
                       \phi_j^*g_j\longrightarrow g_\infty
                              \quad\hbox{in }C^{1,\alpha}
                                                               \tag{15}
\]
for every fixed \(\alpha<1\), with weak local \(W^{2,p}\) control.
In these charts,
\[
     \operatorname{Ric}_{\phi_j^*g_j}=-\phi_j^*g_j+e_j,
                         \qquad\|e_j\|_\infty\to0.       \tag{16}
\]
Pass to the harmonic-coordinate equation (3). The strong convergence
of the lower-order terms and (16) imply
\(\operatorname{Ric}_{g_\infty}=-g_\infty\) weakly. Elliptic
bootstrapping makes the limit a smooth negative Einstein metric.
The difference-equation argument (10) gives strong \(W^{2,p}\)
convergence for every finite \(p\), if desired. Transporting
\(g_\infty\) by \(\phi_j\) gives a smooth metric with Ricci equal to
minus itself on **each sufficiently late \(M_j\)**, a contradiction.
This proves Theorem A. \(\square\)

This argument establishes existence, not an effective Newton radius,
uniqueness, or a canonical choice of the output. It also does not
claim \(C^2\), let alone smooth, convergence of the input metrics.
Small, rapidly oscillating Ricci errors cannot be differentiated for
free. Finite-\(p\) harmonic elliptic control is exactly what the
topology-preserving limit argument needs.

## 6. The gauge-theoretic input can supply noncollapse

**Corollary C.** Fix \(D,\Lambda,A_0>0\) and \(q>2\). In Theorem A,
the explicit volume lower bound may be replaced by the following
actual monopole supply: for every allowed input metric, there is an
actual class \(a_g\) for which the scalar-curvature estimate holds and
\[
                           (a_g^+)^2\ge A_0.             \tag{17}
\]
The resulting threshold depends on \(D,\Lambda,q,A_0\).

**Proof.** The actual monopole scalar estimate and \(\delta_-\le1/2\)
give
\[
 32\pi^2 A_0\le\int_M s_-^2\,d\mu
       \le16(1+\delta_-)^2\operatorname{Vol}(M,g).
\]
Consequently
\[
             \operatorname{Vol}(M,g)
                 \ge\frac{2\pi^2A_0}{(1+\delta_-)^2}
                 \ge\frac{8\pi^2A_0}{9}.               \tag{18}
\]
Use this \(v\) in Theorem A. The class is allowed to depend on the
metric. No assertion about an arbitrary formal cohomology vector is
substituted for the actual scalar estimate. \(\square\)

This supplies a genuine bridge between the established gauge budget
and exact Einstein existence: the gauge input is used to prevent
collapse, the one-sided curvature budget determines the possible
blowup orientation, and asphericity excludes the resulting smooth ALE
cores. It is not the false implication “no numerical obstruction,
therefore existence.” The independent geometric hypotheses remain.

## 7. Consequences for Yau26 and the precise remaining escape

Let \(M_j\) be closed oriented aspherical four-manifolds with no
Einstein metric, and suppose \(\delta_-(g_j)\to0\). For every fixed
\(q>2\), the following three properties cannot all hold uniformly:
\[
 \operatorname{diam}(g_j)\le D,
 \qquad\operatorname{Vol}(g_j)\ge v>0,
 \qquad\|W^+_{g_j}\|_{L^q}\le\Lambda.                  \tag{19}
\]
If the actual positive projection budget (17) is uniform, the volume
condition is automatic. In that setting a hypothetical counterexample
sequence must escape every joint diameter/half-Weyl bound. This is a
statement about the approximate inputs themselves; unlike the earlier
spectral escape theorem, it does not assume that the inputs are exact
Einstein metrics or satisfy a rank-one Weyl spectral ansatz.

The theorem works equally for changing smooth types, because its
compactness conclusion recovers the smooth type of each late term.
It does not complete the negative Yau26 branch: arbitrary diameter,
collapse without a gauge volume budget, and concentration of both
Weyl halves remain outside (1). No assumption is silently made that
the first-line scalar or spectral inequalities control those freedoms.

The meaningful increment is a theorem-level realization mechanism:
\[
 \boxed{
 \begin{gathered}
 \text{pointwise almost-Einstein input}
 +\text{bounded global regime}
 +\text{one-sided supercritical Weyl control}\\
 +\text{aspherical topology}
 \quad\Longrightarrow\quad
 \text{Einstein metric on the same smooth manifold}.
 \end{gathered}}
\]
The compactness, curvature-energy, and ALE classification theorems are
not newly proved here. The continuation is their explicit composition
with the inherited compact-core obstruction, including the missing
almost-Einstein regularity argument. No worldwide-priority claim is
made.

### Comparison with an existing no-bubbling mechanism

Fine's 2017 twistor argument also excludes locally hyperkähler bubbles,
but uses a different input: a curvature inequality making the twistor
space tamed. His Corollary 4 gives compactness for normalized ASD
Einstein metrics under diameter and volume bounds, without our
asphericity assumption. His Remark 5 explicitly identifies the lack
of \(C^2\) convergence for bounded-Ricci sequences as an obstacle to
using his holomorphic-curve persistence proof. We do not remove that
obstacle for his theorem. Here no twistor taming or persistence is
assumed; the compact-core contradiction is purely topological once
the smooth ALE limit and core embedding have been obtained. Neither
result subsumes the other with its hypotheses unchanged.

## 8. Primary sources and dependency trace

- M. T. Anderson, *Convergence and rigidity of manifolds under Ricci
  curvature bounds*, Invent. Math. **102** (1990), 429–445:
  <https://doi.org/10.1007/BF01233434>. Harmonic-radius and geometric
  compactness framework; equation (3) and the strong-convergence
  argument are specified above rather than hidden in an “Einstein
  compactness” citation.
- Q. S. Zhang and M. Zhu, *Bounds on harmonic radius and limits of
  manifolds with bounded Bakry–Émery Ricci curvature*, introduction
  and Section 2:
  <https://arxiv.org/html/1705.10071>. In particular their discussion
  distinguishes convergence in the classical Ricci case from the
  weaker Bakry–Émery setting and explains the strong Sobolev issue.
- W. Jiang and A. Naber, *L2 Curvature Bounds on Manifolds with Bounded
  Ricci Curvature*, Theorem 1.6:
  <https://arxiv.org/html/1605.05583>. This provides (5) under precisely
  a Ricci bound and local noncollapse, not Ricci derivative control.
- S. Bando, A. Kasue and H. Nakajima, *On a construction of coordinates
  at infinity on manifolds with fast curvature decay and maximal
  volume growth*, Invent. Math. **97** (1989), 313–349:
  <https://doi.org/10.1007/BF01389045>, Theorem 1.5. Its precise
  finite-energy Ricci-flat formulation is reproduced as Theorem 2.7
  in R. Buzano and L. Yudowitz, *Bubble-tree convergence and local
  diffeomorphism finiteness for gradient Ricci shrinkers*:
  <https://link.springer.com/article/10.1007/s00209-023-03272-z>.
- E. P. Wright, *Quotients of gravitational instantons*:
  <https://arxiv.org/pdf/1102.2442>, and I. Suvaina, *ALE Ricci-flat
  Kähler metrics and deformations of quotient surface singularities*:
  <https://arxiv.org/pdf/1102.2672>. They are used in the inherited
  [compact-core proof](../mathematics/current/line1_aspherical_no_bubbles.md).
- For the actual scalar budget and its quantifiers, see the inherited
  [all-sign stability proof](../mathematics/current/line1_integral_rigidity_paper.md)
  and [Bauer–Furuta class supply](../mathematics/current/line1_bauer_furuta_geography.md).
- J. Fine, *Limits of Riemannian 4-manifolds and the symplectic geometry
  of their twistor spaces*, Theorem 3, Corollary 4 and Remark 5:
  <https://arxiv.org/html/1602.03829>. This is a comparison, not an
  input to the proof.
