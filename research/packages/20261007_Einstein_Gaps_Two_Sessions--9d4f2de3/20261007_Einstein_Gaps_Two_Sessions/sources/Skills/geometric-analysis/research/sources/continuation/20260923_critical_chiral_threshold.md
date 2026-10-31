# Critical one-half energy thresholds and paired curvature concentration

23 September 2026. Continuation of the
[compact-regime realization theorem](20260923_compact_realization.md).
The increment is at the scale-invariant exponent: supercritical control
or critical equiintegrability is replaced by a fixed small local critical
energy threshold. The small chirality may vary from ball to ball.

## 1. Conventions and statements

Use the Hilbert--Schmidt curvature-operator convention
\[
 |W^\pm|^2=\tfrac14 W^\pm_{ijkl}(W^\pm)^{ijkl}.             \tag{1}
\]
This is not the largest-eigenvalue norm. In the full tensor convention,
all energy thresholds below must be multiplied by four.
Let \(\omega_4=\pi^2/2\), and let \(V_{-K/3}(R)\) be the volume of
a radius-\(R\) ball in the simply connected four-dimensional space
form of sectional curvature \(-K/3\). For fixed \(K,D,v>0\), set
\[
 \theta_0=\frac{v}{V_{-K/3}(D+1)},\qquad
 S_0=\frac9{16\sqrt{\omega_4\theta_0}},\qquad
 \kappa_0=\frac1{6S_0^2}=\frac{128\omega_4\theta_0}{243},
 \qquad \epsilon_0=\frac{\kappa_0}{4}.                    \tag{2}
\]
If the class below is nonempty then \(0<\theta_0\le1\).
These are sufficient constants, not claimed to be sharp.

The topological assumption is
\[
 \pi_1(M)\text{ torsion-free},\qquad \pi_2(M)=0.            \tag{H}
\]
Every closed aspherical manifold has (H). The
[topological core-scope extension](20260923_topological_core_scope.md)
shows that half-flat ALE core exclusion needs only (H): the universal
cover has \(H_1=H_2=0\), and a finite-fundamental-group core lifts to
that cover. In particular, everything below may also be read in the
older aspherical scope.

**Theorem A (critical local compactness).** Fix \(K,D,v,r_0>0\) and
\(0<\alpha<1\). There is a uniform positive lower bound for the
\(C^{1,\alpha}\) harmonic radius on closed connected smooth oriented
four-manifolds satisfying (H),
\[
 \|\operatorname{Ric}^{\sharp}\|_{\infty,\mathrm{op}}\le K,
 \qquad \operatorname{diam}(M,g)\le D,\qquad
 \operatorname{Vol}(M,g)\ge v,                            \tag{3}
\]
and
\[
 \sup_{x\in M}\min\left\{
   \int_{B_{r_0}(x)}|W^+|^2\,d\mu,\
   \int_{B_{r_0}(x)}|W^-|^2\,d\mu
                   \right\}\le\epsilon_0.               \tag{4}
\]
Consequently the class has geometric \(C^{1,\beta}\) and weak
\(W^{2,p}\) precompactness, and only finitely many smooth types.
Here \(\beta<1\) and \(p<\infty\). No uniform \(L^q\), \(q>2\),
bound or vanishing equiintegrability modulus is required.

**Theorem B (critical-regime realization).** Fix \(D,v,r_0>0\).
Use (2) with \(K=2\). There is \(\delta_0(D,v,r_0)>0\) such that
a closed connected smooth oriented four-manifold satisfying (H)
and carrying a metric with these diameter/volume bounds, (4), and
\[
 \delta_-(g)=\|\operatorname{Ric}^{\sharp}_g+I\|_{\infty,\mathrm{op}}
                       <\delta_0                       \tag{5}
\]
admits a smooth metric \(h\) with \(\operatorname{Ric}_h=-h\).

The simpler condition
\(\min\{\int_M|W^+|^2,\int_M|W^-|^2\}\le\epsilon_0\) implies
(4), but is usually unnecessarily restrictive. Condition (4) allows
substantial total Weyl energy and different choices of the small half
in different regions.

## 2. A Sobolev--Weitzenböck gap on the exact blowup

**Lemma C.** Let \(X\) be a complete noncompact smooth Ricci-flat
oriented four-manifold, ALE of some positive order, with asymptotic
volume ratio \(\theta\ge\theta_0>0\). Each Weyl half separately satisfies
\[
 W^\pm\equiv0\quad\hbox{or}\quad
                       \int_X|W^\pm|^2\,d\mu\ge\kappa_0. \tag{6}
\]
This is a classical analytic mechanism, not a classification of
general Ricci-flat ALE spaces.

**Proof.** Brendle's nonnegative-Ricci Sobolev inequality applied to
compactly supported \(f=|u|^3\), by approximation at zeros, gives
\[
 4(\omega_4\theta)^{1/4}
       \left(\int|u|^4\right)^{3/4}
 \le3\int|u|^2|\nabla u|
 \le3\left(\int|u|^4\right)^{1/2}
           \left(\int|\nabla u|^2\right)^{1/2}.
\]
Consequently
\[
 \|u\|_4^2\le S(\theta)\|\nabla u\|_2^2,\qquad
 S(\theta)=\frac9{16\sqrt{\omega_4\theta}}\le S_0.          \tag{7}
\]
For either half let \(w=|W^\pm|\). On the Ricci-flat limit the
Einstein Weitzenböck identity reads
\[
 \tfrac12\Delta w^2=|\nabla W^\pm|^2-18\det W^\pm,
 \qquad\Delta=\operatorname{div}\nabla.                   \tag{8}
\]
For a real symmetric trace-free \(3\times3\) matrix,
\[
 |\det W^\pm|\le\frac{w^3}{3\sqrt6}.                      \tag{9}
\]
Indeed, with eigenvalues summing to zero,
\[
 (\sum\lambda_i^2)^3-54(\lambda_1\lambda_2\lambda_3)^2
       =2\prod_{i<j}(\lambda_i-\lambda_j)^2\ge0.
\]

ALE asymptotics of a positive order \(\tau\) suffice for exhaustion:
\(W=O(r^{-2-\tau})\), \(\nabla W=O(r^{-3-\tau})\).
Einstein elliptic regularity gives the derivative asymptotics.
Thus \(w\in L^2\cap L^4\), \(\nabla W\in L^2\), and boundary errors
in (8) vanish. Cutoffs and Kato extend (7) to \(w\).
No assertion about the optimal ALE coordinate order is used.
Integration followed by Hölder, Kato and (7) yields
\[
 \begin{aligned}
 J:=\int|\nabla W^\pm|^2
 &=18\int\det W^\pm
 \le\sqrt6\int w^3\\
 &\le\sqrt6\,\|w\|_2\|w\|_4^2
 \le\sqrt6\,S_0\|w\|_2J.
 \end{aligned}                                          \tag{10}
\]
If \(\|w\|_2^2<\kappa_0\), the last coefficient is less than one,
so \(J=0\). A parallel \(L^2\) tensor on this infinite-volume
connected manifold vanishes. This proves (6). \(\square\)

The Sobolev estimate is on an **exact Ricci-flat blowup** with a
controlled volume ratio. It does not add a hidden uniform Sobolev
assumption to the earlier unrestricted monopole integral-gap theorem.

## 3. Topology forces both halves to concentrate together

Suppose a sequence satisfying (H) and (3) has minimum harmonic radius
\(\rho_j\to0\), attained at \(x_j\). The harmonic-radius argument of
the preceding continuation gives a complete smooth nonflat
Ricci-flat limit
\[
 (M_j,\rho_j^{-2}g_j,x_j)\longrightarrow
                  (X,g_\infty,x_\infty).                 \tag{11}
\]
Here are the necessary inputs, rather than an implicit invocation of
smooth almost-Einstein compactness.

Relative Bishop comparison gives, at every centre and for \(r\le D+1\),
\[
 \operatorname{Vol}B_r(x)
 \ge \frac{vV_{-K/3}(r)}{V_{-K/3}(D+1)}
 \ge\theta_0\omega_4r^4.                                 \tag{12}
\]
Every fixed-radius ball in the rescaled limit obeys this Euclidean
lower bound, so its asymptotic volume ratio is at least \(\theta_0\).
Ricci tends uniformly to zero after rescaling. The normalized
harmonic-radius lower bound gives \(C^1\) charts; their elliptic
metric equation gives strong \(W^{2,p}\) convergence for every finite
\(p\), then a smooth Ricci-flat limit. Strong
\(C^{1,\alpha}\) recovery makes the limiting harmonic-radius
normalization nontrivial, excluding a flat limit. No derivative of
the original Ricci error is estimated.

Jiang--Naber's local full \(L^2\) curvature estimate, summed over the
bounded global covering provided by (3), bounds the scale-invariant
full energy. The bound passes to (11). Finite energy and Euclidean
growth give ALE structure by the Ricci-flat asymptotic theorem.
Only a positive ALE order is needed here.

The geometric convergence embeds every large smooth compact core of
\(X\) in \(M_j\). If \(W^+_\infty=0\), the half-flat compact-core
exclusion contradicts that embedding. If \(W^-_\infty=0\), the same
argument applies with reversed orientation. Therefore both halves of
this **same** blowup are nonzero, and Lemma C gives
\[
              \int_X|W^+|^2\ge\kappa_0,\qquad
              \int_X|W^-|^2\ge\kappa_0.                  \tag{13}
\]
For every fixed \(r>0\), strong local curvature convergence and
exhaustion in the rescaled radius imply
\[
 \liminf_j\int_{B_r(x_j)}|W^+_{g_j}|^2\ge\kappa_0,\qquad
 \liminf_j\int_{B_r(x_j)}|W^-_{g_j}|^2\ge\kappa_0.          \tag{14}
\]
To see this, a fixed radius-\(R\) ball in (11) is eventually contained
in the unscaled radius-\(r\) ball. First let \(j\to\infty\),
then \(R\to\infty\).

**Paired-concentration alternative.** In the bounded Ricci, diameter
and noncollapse regime (3), harmonic-radius degeneration on the
topological class (H) forces a definite critical amount of **both**
Weyl energies at a common shrinking location, in the precise sense
(14), after a subsequence.

This is stronger than saying that one half must concentrate. It does
not assert the existence of non-half-flat Ricci-flat ALE spaces or
assume their classification. It identifies the curvature required of
any surviving bubble. If such bubbles are excluded by additional
arguments, compactness strengthens further.

## 4. Proofs of compactness and realization

**Proof of Theorem A.** If the harmonic radii were not uniformly
positive, apply (14) with \(r=r_0\). Both energies at \(x_j\)
eventually exceed \(\kappa_0/2\), contradicting (4) and
\(\epsilon_0=\kappa_0/4\). No globally consistent choice of chirality
in (4) is needed. The controlled harmonic atlases give the stated
compactness and smooth-type finiteness exactly as in the preceding
continuation. \(\square\)

**Proof of Theorem B.** Failure would give input metrics with
\(\delta_-(g_j)\to0\), the fixed bounds and (4), but no normalized
negative Einstein metric on their smooth manifolds. For large \(j\)
the Ricci bound (3) holds with \(K=2\). Theorem A gives a subsequence
identified with a fixed smooth manifold, and harmonic-coordinate
\(C^{1,\alpha}\) convergence. Pass to
\[
 g^{ab}\partial_a\partial_bg_{ij}
    =-2\operatorname{Ric}_{ij}+Q_{ij}(g,\partial g).
\]
The limiting metric weakly solves \(\operatorname{Ric}=-g\).
Elliptic bootstrapping makes it smooth. Transporting this metric
through the smooth identifications supplies the forbidden Einstein
metric on each late original manifold. \(\square\)

An actual monopole projection budget \((a_g^+)^2\ge A_0>0\) can
replace the lower volume hypothesis: if \(\delta_-\le1/2\), the
scalar estimate gives \(V\ge8\pi^2A_0/9\).
Substitute this \(v\) into (2). This observation does not delete
actual solvability or square costs from other theorems.

## 5. Increment and the remaining original-problem gap

The preceding \(L^q\), \(q>2\), hypothesis and uniform critical
equiintegrability each imply (4) at a common sufficiently small
radius. Conversely, (4) does not itself impose uniform vanishing
of small-ball energy: it permits a fixed nonzero subthreshold
amount. No actual new geometric family is claimed merely from this
measure-theoretic weakening.

The variable-chirality form is useful when global control of one
fixed half is unavailable but the two energies have different spatial
distributions. It provides a mathematically precise potential role
for chiral information in existence, rather than just another global
curvature coefficient.

For a hypothetical negative-side Yau26 counterexample sequence in
(H), with bounded diameter and a uniform positive actual projection
budget, harmonic radii must degenerate along a subsequence; otherwise
the smooth-type realization argument produces Einstein metrics.
Consequently (14) holds at suitable centres: the remaining
compact-regime escape must spend critical energy in **both** halves
at the same location.

Diameter escape, collapse without a positive volume budget, and
paired concentration above threshold remain possible. No
dimension-only Yau26 threshold is proved. Sobolev and Weyl gap
estimates are classical ingredients; the increment is their explicit
composition with the topological core exclusion to obtain critical,
locally variable-chirality compactness and same-type realization.
No exhaustive publication-priority claim is made.

## 6. Sources and finite verification

- S. Brendle, *Sobolev inequalities in manifolds with nonnegative
  curvature*, Theorem 1.1:
  <https://arxiv.org/html/2009.13717>. Only the exact blowup uses this
  theorem. Equation (7) is the displayed elementary deduction.
- A. Derdziński, *Self-dual Kähler manifolds and Einstein manifolds
  of dimension four*:
  <https://www.numdam.org/article/CM_1983__49_3_405_0.pdf>.
  The harmonic-half-Weyl identity, with convention (1), is explicitly
  recorded in Section 3 of Gursky--McKeown--Tyrrell,
  *Self-dual and even Poincaré--Einstein metrics in dimension four*:
  <https://arxiv.org/html/2407.08851>. Only the local identity is
  used, not their Poincaré--Einstein boundary hypotheses.
- W. Jiang and A. Naber, *L2 Curvature Bounds on Manifolds with
  Bounded Ricci Curvature*, Theorem 1.6:
  <https://arxiv.org/html/1605.05583>. Its separate derivative theorem
  has additional hypotheses and is not used.
- Bando--Kasue--Nakajima, *On a construction of coordinates at infinity
  on manifolds with fast curvature decay and maximal volume growth*:
  <https://doi.org/10.1007/BF01389045>. Only positive-order ALE
  asymptotics of the finite-energy Ricci-flat limit are needed.
- E. P. Wright, *Quotients of gravitational instantons*, Theorem A,
  Remark 1 and Corollary C: <https://arxiv.org/html/1102.2442>.
  Its classification covers the half-flat case. Remark 1 explicitly
  separates the conjectural general Ricci-flat ALE classification,
  which is not assumed here.
- [Inherited compact-core proof](../mathematics/current/line1_aspherical_no_bubbles.md)
  and [topological scope extension](20260923_topological_core_scope.md).

The accompanying exact checker verifies the determinant polynomial,
threshold arithmetic, absorption margin and critical scaling. It does
not certify the compactness, asymptotic or topological arguments.

