# Ricci-energy selection, scalar coherence, and Einstein defect

## 1. The question this note resolves

The preceding Kähler calculation identified the limiting relative Einstein
defect of a constant-scalar-curvature blow-up sequence. Here we remove the
Kähler assumption and describe **every** sequence approaching the sharp
Ricci-energy bound. The remaining term is the scalar variance. An actual
conformal construction shows that this term cannot be dropped, even on a
fixed manifold admitting Kähler–Einstein metrics and with zero primitive
period cost. Conversely, choosing the negative Yamabe representative removes
this term without a spectral-gap assumption.

The finite estimates below follow from classical Seiberg–Witten and
Chern–Weil inequalities. They do not require the project’s integral
calibration lemma, its second-order estimates, or the Round21 spectral
criterion. This is a new deduction recorded in this research package, not
a claim of priority over the literature.

All manifolds are closed, connected, oriented, and four-dimensional.
Ricci norms are ordinary tensor norms; Weyl norms are endomorphism norms
on two-forms. Write
\[
 T=2\chi+3\tau,\quad V=\operatorname{Vol}(g),\quad
 S_2=\int s^2,\quad R=\int|\operatorname{Ric}|^2,\quad
 P=\int|\operatorname{Ric}^{\circ}|^2,\quad
 L=\int(s-\bar s)^2.
 \tag{1}
\]
Integrals use the current metric.

## 2. Precise topological input and the finite theorem

Fix numbers \(A>0\), \(d\ge0\), with \(T=A-d\). For the metric in question,
assume an actual polarized monopole Spin\(^c\) structure whose class \(a\)
satisfies \(p=(a_g^+)^2\ge A\). Its equations must be solvable throughout
the conformal class, so that the classical scalar and scalar–Weyl
inequalities apply. A formal intersection vector is not enough.

The class may depend on \(g\). No class-square upper bound, scalar band,
Sobolev constant, injectivity-radius bound, or diameter bound is assumed.

In the standard application,
\[
 M=X\#k\overline{\mathbb {CP}}^{\,2}
       \#m(S^1\times S^3),\qquad
 A=c_1^2(X)>0,\quad d=k+4m,
 \tag{2}
\]
where \(X\) is a minimal complex surface of general type. The polarized
class selection and its \(b_+=1\) interpretation are as in LeBrun’s
Proposition 3.2 and the [application closure](lebrun_stability_closure.md).
LeBrun’s Theorem 4.3 identifies the lower bound below as the actual
all-metrics infimum in this application.

Put
\[
 C=8\pi^2A,\quad H=8\pi^2d,\quad
 J=R-(C+H).
 \tag{3}
\]

**Theorem 1 (finite energy-selection bound).** Under the stated input,
\(J\ge0\), and
\[
 \boxed{\quad
 H-\sqrt{J(C+J)}\ \le P\le H+J .
 \quad} \tag{4}
\]
The lower bound may of course be replaced by its positive part.
With
\[
 \mathcal E(g)=\inf_{\lambda\ne0}
 \frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2 V},
 \tag{5}
\]
one has the exact formula
\[
 \mathcal E(g)=\frac{4P+L}{R}
 \tag{6}
\]
and consequently
\[
 \boxed{
 -\frac{4\sqrt{J(C+J)}}{C+H+J}
 \le
 \mathcal E(g)-\frac{4H+L}{C+H+J}
 \le\frac{4J}{C+H+J}.}
 \tag{7}
\]

Thus the Einstein defect is not determined by absolute Ricci energy
alone. Near its minimum, its two contributions are the topological
quantity \(4H\) and the scalar variance \(L\).

### Proof

Define the classical LeBrun remainder
\[
 D=\frac1{4\pi^2}\int
       \left(\frac{s^2}{24}+\frac12|W^+|^2\right)-\frac p2.
 \tag{8}
\]
The required classical inputs are
\[
 S_2\ge32\pi^2p,\qquad
 \int(-s+\sqrt6|W^+|)^2\ge72\pi^2p,\qquad D\ge0.
 \tag{9}
\]
These are the scalar estimate, Theorem 2.3, and Proposition 4.1 of
[LeBrun, arXiv:math/0003068v1](https://arxiv.org/pdf/math/0003068).
No assertion about the equality set of a different curvature functional
is used.

Chern–Weil gives the exact identity
\[
 R=8\pi^2(2p-T)+32\pi^2D,
 \qquad J=16\pi^2(p-A)+32\pi^2D.
 \tag{10}
\]
In particular
\[
 0\le p-A\le J/(16\pi^2),\qquad 0\le D\le J/(32\pi^2).
 \tag{11}
\]
Let
\[
 q=-s+\sqrt6|W^+|,\quad t=s+2\sqrt6|W^+|,\quad
 \delta=144\pi^2D,\quad
 \Delta=\int q^2-72\pi^2p,\quad U=\int t^2.
 \tag{12}
\]
Here \(q\) need not be positive. The unsigned inequality in (9) suffices.
Pointwise expansion and integration yield
\[
 \delta=\Delta+\tfrac12 U,\qquad \Delta\ge0,\qquad
 s=(t-2q)/3.
 \tag{13}
\]
For the scalar surplus \(B_p=S_2-32\pi^2p\ge0\), this implies
\[
 9B_p=4\delta-U-4\int qt.
 \tag{14}
\]
Cauchy–Schwarz and \(U\le2\delta\) give
\[
 B_p\le\frac49
       \left[\delta+\sqrt{2\delta(72\pi^2p+\delta)}\right].
 \tag{15}
\]
Using (11), \(\delta\le9J/2\), and the convenient bound
\(72\pi^2p+\delta\le72\pi^2A+9J\), we obtain
\[
 \boxed{0\le B_p\le2J+4\sqrt{J(C+J)}.}
 \tag{16}
\]
There is room to sharpen these numerical constants; their optimality
is not asserted.

Since \(P=R-S_2/4\), (10) also gives
\[
 P=H+J-8\pi^2(p-A)-B_p/4.
 \tag{17}
\]
The upper bound in (4) follows immediately. For the lower bound, (11)
and (16) give
\[
 P-H\ge J-J/2-\bigl(J/2+\sqrt{J(C+J)}\bigr)
          =-\sqrt{J(C+J)}.
 \tag{18}
\]
Finally, expansion in \(1/\lambda\) yields
\[
 \mathcal E=4-\frac{(\int s)^2}{VR}
            =\frac{4P+L}{R}.
 \tag{19}
\]
Here \(R\ge C>0\). If \(\int s=0\), the infimum is \(4\), approached
as \(|\lambda|\to\infty\); otherwise the minimizer is
\(\lambda=R/\int s\). This covers both cases without falsely treating a
Ricci-flat metric as zero relative defect. Substitution proves (7).

## 3. All minimizing sequences, not only Kähler sequences

**Corollary 2.** In the setting of Theorem 1, if \(J(g_j)\to0\), then
\[
 p_j\to A,\quad D_j\to0,\quad
 \int s_j^2\to32\pi^2A,\quad P_j\to8\pi^2d.
 \tag{20}
\]
Moreover
\[
 \boxed{\mathcal E(g_j)
   =\frac{4d}{A+d}
       +\frac{L_j}{8\pi^2(A+d)}+o(1).}
 \tag{21}
\]
In particular
\[
 \liminf\mathcal E(g_j)\ge\frac{4d}{A+d},
 \tag{22}
\]
and \(\mathcal E(g_j)\to4d/(A+d)\) is equivalent to \(L_j\to0\).
For \(d=0\), vanishing relative Einstein defect is equivalent to
vanishing scalar variance along such a sequence.

Indeed (11) and (16) give (20). Since \(0\le L_j\le\int s_j^2\),
the variance is bounded; (7) therefore gives (21).
This assertion imposes no Kähler condition, no constant-scalar-curvature
condition, and no geometric compactness hypothesis.

For varying topologies the uniform formulation is (7). For example,
write \(r=d/A\), \(j=J/(8\pi^2A)\), and
\(\ell=L/(8\pi^2A)\). Then the difference between
\(\mathcal E\) and \((4r+\ell)/(1+r+j)\) lies between
\(-4\sqrt{j(1+j)}/(1+r+j)\) and \(4j/(1+r+j)\).
Small *relative* energy excess, rather than small unnormalized excess,
is the appropriate hypothesis when \(A\) varies.

### A direct scalar-coherence criterion on the original metric

For an ordinary monopole solution, put \(\rho=|\Phi|^2\) and let
\(\mathcal F\) be its real determinant curvature. The integrated spinor
identity and Hodge projection give
\[
 B_p=\|s+\rho\|_2^2+8\|\nabla\Phi\|_2^2+
        8\|\mathcal F^+-(\mathcal F^+)_H\|_2^2.
 \tag{22a}
\]
This retains the harmonic-projection loss in the classical scalar
inequality. It also follows from the [Round17 identity](round17_integral.md)
by subtracting the harmonic anti-self-dual contribution.

If \(s\ge-S\), the maximum principle yields \(0\le\rho\le S\).
Since \(|d\rho|^2\le4S|\nabla\Phi|^2\), Poincaré gives
\[
 \sqrt L\le\|s+\rho\|_2+
       \sqrt{4S/\lambda_1}\,\|\nabla\Phi\|_2.
\]
Joint Cauchy–Schwarz in the two displayed losses of (22a) proves
\[
 \boxed{L\le\left(1+\frac{S}{2\lambda_1}\right)B_p.}
 \tag{22b}
\]
Thus bounded \(S/\lambda_1\) is one sufficient condition for scalar
coherence along a minimizing sequence. It requires no weighted equations,
strict negative scalar band, or prior bound on Ricci error. The stronger
weighted variance estimate in the companion converse theorem instead
controls \(L\) linearly by \(D\), under its stated negative-band assumptions.
Neither argument supplies a spectral gap for an arbitrary degenerating
family.

## 4. Removing scalar variance by conformal normalization

The variance in (21) is essential on the original metric. It can nevertheless
be removed by a mathematically legitimate change of representative.

**Corollary 3 (Yamabe representatives of all minimizing sequences).**
In the standard application (2), or whenever Theorem 1's input holds in
the conformal class, let \(\widehat g\) be its negative constant-scalar-
curvature Yamabe representative. Then
\[
 \widehat J\le J,\qquad
 R(g)-R(\widehat g)
       =\tfrac13\bigl(S_2(g)-S_2(\widehat g)\bigr),\qquad
 P(g)-P(\widehat g)
       =\tfrac1{12}\bigl(S_2(g)-S_2(\widehat g)\bigr).
 \tag{23}
\]
Consequently every Ricci-energy-minimizing sequence can be replaced,
within its own conformal classes, by one satisfying
\[
 \boxed{\mathcal E(\widehat g_j)\longrightarrow
                  \frac{4d}{A+d}.}
 \tag{24}
\]
For \(d=0\) there is also the finite bound
\[
 \boxed{\mathcal E(\widehat g)
          \le\frac{4J}{8\pi^2A+J}.}
 \tag{25}
\]

### Proof of the conformal step

A nonzero actual monopole projection rules out nonnegative scalar
curvature in this conformal class by the spinor Weitzenböck formula.
The Yamabe theorem therefore provides a representative with negative
constant scalar curvature. Four-dimensional Hodge star on two-forms,
\(p\), and \(\int|W^+|^2\) are conformally invariant.

For completeness, the scalar-energy minimization in a negative conformal
class has a direct verification. Rescale \(\widehat g\) to
\(s_{\widehat g}=-b<0\), and write \(g=u^2\widehat g\).
With \(\Delta=\operatorname{div}\nabla\), conformal covariance gives
\[
 \int s_g^2\,d\mu_g
 =\int\left(-b-6u^{-1}\Delta_{\widehat g}u\right)^2d\mu_{\widehat g}.
 \tag{26}
\]
Integration by parts yields
\[
 \int u^{-1}\Delta u=\int u^{-2}|du|^2\ge0.
 \tag{27}
\]
Expanding (26) shows \(S_2(g)\ge b^2V_{\widehat g}=S_2(\widehat g)\).
The Chern–Weil identity
\[
 R=4\int|W^+|^2+\tfrac13 S_2-8\pi^2T
 \tag{28}
\]
and \(P=R-S_2/4\) prove (23).
The lower bound \(R(\widehat g)\ge C+H\) remains valid for the same
polarization and actual class, so \(0\le\widehat J\le J\).
Now (21) with \(\widehat L=0\) proves (24).
When \(d=0\), (4) gives \(\widehat P\le\widehat J\), whence
\[
 \mathcal E(\widehat g)=
 \frac{4\widehat P}{C+\widehat J}
 \le\frac{4\widehat J}{C+\widehat J}
 \le\frac{4J}{C+J}.
 \tag{29}
\]

This does not estimate the distance between \(g\) and \(\widehat g\).
The conformal scale-splitting example shows that such an estimate cannot
be inferred from \(J\to0\). Nor does an integral estimate for \(\widehat g\)
give a pointwise Ricci estimate.

[Round14](round14_global.md) already carried out Yamabe normalization for
a particular shear construction. The assertion here concerns arbitrary
input conformal classes and all Ricci-energy-minimizing sequences; it does
not count the act of Yamabe normalization as a new method.

## 5. An explicit energy exclusion for all Einstein candidates

If a metric in this topological range is Einstein, then \(P=0\).
Theorem 1 forces
\[
 J(C+J)\ge H^2,\qquad
 \boxed{
 J\ge\frac{\sqrt{C^2+4H^2}-C}{2}
   =4\pi^2\bigl(\sqrt{A^2+4d^2}-A\bigr).}
 \tag{30}
\]
For \(d>0\), any Einstein metric must therefore stay a positive
absolute-energy distance above the Ricci-energy infimum.
This is a consequence of the classical curvature inequalities, not
a new nonexistence theorem.

More generally, if \(0\le P/R\le\alpha\), then
\[
 H\le\alpha(C+H+J)+\sqrt{J(C+J)}.
 \tag{31}
\]
For the negative Yau26 normalization
\(\delta_-=\|\operatorname{Ric}^{\sharp}+I\|_{\infty,\mathrm{op}}<1\),
\[
 P\le4\delta_-^2V,\quad R\ge4(1-\delta_-)^2V,\quad
 \alpha=\frac{\delta_-^2}{(1-\delta_-)^2}
 \tag{32}
\]
is admissible.

Thus, at any fixed positive blow-up/handle ratio \(d/A\), a pointwise
near-Einstein sequence cannot simultaneously be a relative Ricci-energy-
minimizing sequence. This is a usable restriction on a construction
strategy. It does not exclude inputs whose energy stays above that
minimum, and it does not decide whether the smooth manifold admits an
Einstein metric elsewhere.

## 6. The resulting first-line picture

Three statements now have different, explicit roles.

1. The existing integral gap near the forbidden \(2/3\) topology uses
   the project's integral calibration proof. It remains a theorem about
   exclusion of near-Einstein metrics in its actual-monopole range.
2. The present theorem describes every sequence minimizing the classical
   *absolute* Ricci energy. It identifies the topological contribution to
   the relative defect and the independent scalar-coherence term.
3. The [fixed-metric converse](line1_non_kahler_bridge.md) uses the earlier
   actual-form remainder and a scalar spectral gap. It starts from
   curvature-functional and period data, not from an assumed Ricci-small
   input. The [scale-splitting example](line1_conformal_neck.md)
   explains why the scalar-coherence hypothesis has content.

The prior actual-form supply uses \(t=1/2\), already an allowed negative
Kähler–Einstein root of Round21. Substituting that value into
\(\operatorname{dist}(t,\{0,1/2\})\) alone gives zero and proves no new
obstruction. The additional conclusions here come from curvature-energy
identities, actual topology, and control or removal of scalar variance.

The remaining Yau26 task is not concealed by these deductions:
small integrated Ricci error must still be connected to the required
pointwise input or to existence of an exact Einstein metric on the same
smooth manifold. Neither follows merely from minimizing the classical
energy. No new Yau26 branch is declared solved here.

## Sources and proof dependence

- LeBrun, [Ricci curvature and Seiberg–Witten theory](https://arxiv.org/pdf/math/0003068),
  cited preprint version:
  Theorem 2.3, Proposition 3.2, Propositions 4.1–4.2, and Theorem 4.3.
  These supply the inequalities, class selection, and sharp infimum.
- [Polarized application closure](lebrun_stability_closure.md):
  project notation, metricwise class selection, and chamber details.
- [Previous Kähler calculation](line1_kahler_energy.md):
  the Kähler-only minimizing-sequence profile, now extended above to all
  metrics with an explicit scalar-variance term.
- [Actual-form remainder](line1_scalar_band_remainder.md):
  needed for the complementary fixed-metric bridge, not for Theorem 1.
- The negative Yamabe representative uses the classical Yamabe theorem;
  all subsequent conformal monotonicity identities are proved in (26)–(29).
