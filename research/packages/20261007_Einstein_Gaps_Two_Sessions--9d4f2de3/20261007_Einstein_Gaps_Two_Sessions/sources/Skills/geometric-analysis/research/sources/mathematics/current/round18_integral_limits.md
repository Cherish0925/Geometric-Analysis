# A complete test of the unrestricted integral extension

The actual-monopole and relative topology hypotheses of the integral
rigidity theorem cannot simply be discarded. The following classical
construction gives a concrete reason, even if collapse and curvature
blow-up are excluded. Its role is to distinguish a viable extension from
a false one, not to supply a pointwise Yau26 counterexample.

## 1. Statement

There are closed oriented smooth four-manifolds \(M_j\) and smooth
metrics \(g_j\) such that:

1. No \(M_j\) admits an Einstein metric of any sign.
2. For every nonnegative integer \(r\), there are constants \(C_r\),
   and there is \(i_0>0\), independent of \(j\), with
   \[
   |\nabla^r\operatorname{Rm}_{g_j}|\le C_r,\qquad
   \operatorname{inj}(M_j,g_j)\ge i_0 .
   \tag{1}
   \]
3. The volume tends to infinity and, for every \(1\le p<\infty\),
   \[
   \fint_{M_j}|\operatorname{Ric}_{g_j}+3g_j|^p
      =\frac{C_p}{\operatorname{Vol}(M_j,g_j)}\longrightarrow0 .
   \tag{2}
   \]
   In particular the relative integral Einstein defect satisfies
   \[
   \mathcal E(g_j):=
   \inf_{\lambda\ne0}
   \frac{\int|\operatorname{Ric}_{g_j}-\lambda g_j|^2}
        {\lambda^2\operatorname{Vol}(M_j,g_j)}
   \le\frac{C_2}{9\operatorname{Vol}(M_j,g_j)}\longrightarrow0 .
   \tag{3}
   \]
4. The pointwise operator-norm defect of these metrics is a fixed
   positive number:
   \[
   \|g_j^{-1}\operatorname{Ric}_{g_j}+3I\|_\infty=c_\infty>0.
   \tag{4}
   \]

Thus a dimension-only relative integral gap on all no-Einstein
four-manifolds is false, including within a uniformly bounded-geometry
class. This statement permits the smooth topology and total volume to
vary; it asserts neither \(\inf_g\mathcal E(g)=0\) on one fixed \(M_j\)
nor pointwise Einstein approximation.

## 2. The manifolds and the all-sign obstruction

Fix a closed connected oriented real-hyperbolic four-manifold
\((N,h)\), with sectional curvature \(-1\). Its finitely generated
linear fundamental group is infinite and residually finite. It therefore
has connected finite covers \(N_j\to N\) of unbounded degree \(d_j\).
For example, the intersections of finitely many finite-index subgroups
separating successive nontrivial elements form a tower of unbounded
index. Write \(h_j\) for the lifted hyperbolic metric and set
\[
 M_j=N_j\#(S^1\times S^3),\qquad
 V_N=\operatorname{Vol}(N,h).
 \tag{5}
\]
Then
\[
 \chi(M_j)=d_j\chi(N)-2,\qquad
 \operatorname{Vol}(N_j,h_j)=d_jV_N
                  =\frac{4\pi^2}{3}d_j\chi(N).
 \tag{6}
\]
Collapsing the second punctured summand gives a degree-one map
\(M_j\to N_j\).

The Besson--Courtois--Gallot degree inequality gives
\[
 h_{\mathrm{vol}}(g)^4\operatorname{Vol}(M_j,g)
                         \ge3^4d_jV_N .
 \tag{7}
\]
If \(g\) were Einstein with nonnegative Einstein constant, Bishop
comparison on its universal cover would give zero volume entropy,
contradicting (7).

If the constant is negative, rescale to \(\operatorname{Ric}_g=-3g\).
The sharp real-hyperbolic Ricci-volume consequence of (7) gives
\(\operatorname{Vol}(M_j,g)\ge d_jV_N\).
In the convention where \(W\) is an endomorphism of two-forms,
Chern--Gauss--Bonnet for an Einstein four-metric gives
\[
 8\pi^2\chi(M_j)=
      \int\left(|W|^2+\frac{s^2}{24}\right)
      =\int|W|^2+6\operatorname{Vol}(M_j,g).
 \tag{8}
\]
Combining (6)--(8) would require
\[
 d_jV_N\le\operatorname{Vol}(M_j,g)
       \le d_jV_N-\frac{8\pi^2}{3},
 \tag{9}
\]
which is impossible. This excludes every Einstein constant, not merely
metrics close to a chosen gluing.

The entropy and degree input is the main theorem and its Ricci-volume
corollary on printed page 734 of
[Besson--Courtois--Gallot, GAFA 5 (1995)](https://www.aimath.org/WWN/entropyrigidity/papers/BessonCourtoisGallot.pdf).
The same comparison already underlies the inherited \(N\#N\) obstruction
in [the global manuscript](skill/research/20260921_global.tex),
Section “A fixed hyperbolic connected sum already has a gap.”
No new entropy inequality is claimed here.

## 3. A single fixed replacement, with no shrinking limit

Choose \(r>0\) so small that a radius-\(4r\) ball in \(N\) is
embedded. Select one lift of its center to every \(N_j\). Delete the
radius-\(r\) ball. Replace it by a fixed compact manifold
\[
 K=(S^1\times S^3)\setminus\operatorname{int}B^4
 \]
equipped with a fixed smooth metric \(k\) agreeing with the hyperbolic
ball metric on its boundary collar, in the boundary identification used
for (5). To construct such \(k\), prescribe the hyperbolic metric in a
collar and combine it with any interior positive-definite metric by a
partition of unity away from a smaller collar. The metrics agree exactly
near the seam, so the resulting \(g_j\) is smooth and equals \(h_j\)
outside the chosen ball.

Both the deleted ball and the inserted piece are independent of \(j\).
Consequently, with a fixed real constant \(c_V\),
\[
 \operatorname{Vol}(M_j,g_j)=d_jV_N+c_V,\qquad
 \int_{M_j}|\operatorname{Ric}_{g_j}+3g_j|^p
          =\int_K|\operatorname{Ric}_k+3k|^p=:C_p .
 \tag{10}
\]
The residual is zero on the entire exterior and on the matching collar.
Equations (2)--(3) follow.

There is also a direct bounded-geometry proof. Every point sufficiently
far from \(K\) has a fixed-radius neighborhood isometric to a
hyperbolic ball; the cover cannot shorten the base injectivity radius.
Every other point has a fixed-radius neighborhood inside the one fixed
compact model consisting of \(K\) and its radius-\(3r\) hyperbolic
buffer. A finite collection of smaller normal neighborhoods covers that
model. Taking the minimum of their admissible radii and of the exterior
hyperbolic radius proves a uniform injectivity lower bound. All curvature
derivatives are bounded on the compact model and are fixed on the
hyperbolic exterior. This proves (1). No rescaling of the replacement,
thin neck, or unproved degeneration estimate is involved.

The residual on \(K\) is not identically zero: otherwise every
constructed \(g_j\) would be Einstein with constant \(-3\), contradicting
Section 2. Its operator-norm maximum is therefore the same positive
number for every \(j\), proving (4).

## 4. Consequence for the research program

This is a completed counterexample to an *unrestricted integral
extension*, derived by fixed-piece insertion and classical comparison.
Its mechanism is dilution of a fixed, nonzero defect by growing
hyperbolic volume. It is not a new solution of the pointwise problem.

In particular, replacing Yau26's pointwise Ricci requirement by a
normalized finite-\(p\) requirement changes the problem even under
bounded curvature and a uniform injectivity radius. The successful
actual-monopole gap must retain information that rules out this type of
dilution. Adding bounded local geometry alone would not provide that
information.

The construction gives no decreasing maximum defect on \(M_j\).
Whether entirely different metrics on these varying no-Einstein
topologies can achieve pointwise defects tending to zero remains open
in this note. A lower bound tending to zero would not construct them.

[The exact checker](round18_integral_limits_check.py) checks the
Euler/volume incompatibility and the normalized defect algebra; the
existence of finite covers, degree comparison, and the smooth
fixed-piece construction are the mathematical arguments above.
