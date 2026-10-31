# Round 21: integral calibration rigidity beyond the spinor formulation

22 September 2026.

The main mathematical addition is a two-form formulation of the integral
self-test, extended to an entire one-parameter family of Weyl spectra. It
identifies which nonzero calibration amplitude can survive small integral
defect and a controlled Hodge-Laplacian budget. The monopole construction is
one way of supplying these inputs, not part of the analytic theorem itself.

The other results clarify the existing topological theorem: a geometric
criterion settles the small chamber for symplectic bases with \(b_+=1\);
an explicit infinite family demonstrates that the stronger threshold adds
actual topologies relative to the cited classical \(1/3\) bound.

## 1. The new analytic statement

Let \((M^4,g)\) be smooth, closed and oriented. For a smooth self-dual
two-form \(\psi\), with \(\|\psi\|_\infty\le K\), and a constant real
parameter \(|t|\le T\), define

\[
q=|\psi|^2,\qquad
A_{\psi,t}=t\left(\frac q3 I-\psi\otimes\psi\right),\qquad
B=\fint_M|\Delta_H\psi|^2,
\]
\[
d_t=\fint_M\left(
|\operatorname{Ric}+g|^2+
|W^+-A_{\psi,t}|^2+(q-2)^2
\right).
\]

All norms and the normalization are specified in the
[analytic proof](round21_analytic.md). The result is

\[
\boxed{\;
|t|\,|1-2t|
\le C(K,T)\sqrt{d_t(1+B+d_t)}.
\;}                                                       \tag{1}
\]

In particular, for \(d_t\le1\),

\[
\boxed{\;
\operatorname{dist}\!\left(t,\{0,\tfrac12\}\right)^2
\le C(K,T)(1+B)d_t.
\;}                                                       \tag{2}
\]

This is a quantitative selection of the calibration amplitude. When
\(q=2\), the target Weyl eigenvalues are
\((-4t/3,2t/3,2t/3)\). With bounded \(B\) and vanishing defect, a
nonzero amplitude bounded away from zero must approach \(t=1/2\), the
negative Kähler--Einstein value. The proof also gives
\(\fint|\nabla\psi|^2\to0\) in that case. At exactly zero defect and
nonzero amplitude, \(\psi\) is parallel and the metric is negative
Kähler--Einstein; this does not force a global product.

At \(t=0\), this particular divergence test loses sensitivity. Equation
(2) is not an existence assertion for that endpoint.

The former forbidden calibration is \(t=1/8\). Consequently

\[
(1+B)d_{1/8}\ge c(K)>0.                                  \tag{3}
\]

The analytic argument also covers either normalized Einstein sign.
Replacing \(\operatorname{Ric}+g\) by
\(\operatorname{Ric}-\sigma g\), \(\sigma=\pm1\), changes the selected
nonzero amplitude to \(-\sigma/2\). The proof does not use a
negative-side monopole to make this extension; supplying suitable
forms in a new positive-side application is a separate task.

The defect contains only the Ricci, Weyl and amplitude errors;
closedness is not an extra input. For harmonic \(\psi\), \(B=0\) as well.
There is no monopole assumption, no control of \(W^-\), and no uniform
Sobolev, injectivity-radius, diameter or noncollapse hypothesis.

### Why this formulation is useful

The proof works on the self-dual bundle itself. Its connection curvature
uses \(W^+\), scalar curvature and trace-free Ricci, but not \(W^-\).
A covariant Hessian estimate obtained by integration by parts supplies
the second-order budget without a Sobolev inequality.

The smooth amplitude \(q\), including at zeros of \(\psi\), satisfies

\[
\fint|dq|^2
=\fint(q-2)\Delta q
\le C\sqrt{d_t(1+B+d_t)}.
\]

Write \(J_t=\operatorname{div}W(A_{\psi,t})\). A pointwise estimate,
valid for \(t\ne0\), supplies the missing derivative control:

\[
q\bigl(|\nabla\psi|^2+|d\psi|^2\bigr)
\le\frac{|J_t|^2}{t^2}+\frac43|dq|^2.
\]

Weak Bianchi makes \(J_t\) small in integral norm, while the weighted
Hodge identity assigns its squared norm the leading value
\((16/3)t^2(1-2t)\). The derivative terms are controlled by the
displayed estimate, not by assuming that the form is almost closed.
Comparing these evaluations proves (1).
This both explains the old forbidden spectrum and identifies its
realizable nonzero endpoint.

For the old bounded-spinor construction, its estimates give
\(d_{1/8}\le C\kappa+o(1)\) and
\(B\le C(1+\kappa+B_a)+o(1)\), where
\(B_a=(-a^2)_+/\operatorname{Vol}\). Thus (3) recovers the earlier
\((1+B_a)\kappa\ge c\). The negative-square cost has not disappeared:
a different calibration construction would have to supply its own
Hodge budget. This is the precise interface for extending the method
beyond the existing gauge-theoretic inputs.

## 2. Scope beyond complex surfaces

The polarized \(b_+=1\) extension and handle additions were already
proved in Round 13. They are not new results of this round.

The new applicability note discharges its chamber condition for a closed
symplectic base \((X,\omega)\) with

\[
b_+(X)=1,\qquad K_\omega^2>0,\qquad
K_\omega\cdot[\omega]>0.
\]

The positive cone puts \(K_\omega\) on the forward side of every metric
polarization. Hence the determinant class \(-K_\omega\) lies in the
negative small-perturbation chamber, where classical Taubes nonvanishing
applies. The inherited integral theorem therefore holds on
\[
X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3)
\]
with \(A=K_\omega^2\), without an integrable complex structure. The sign
condition is essential: it excludes a false application to
\(\mathbb{CP}^2\).

[Chamber proof and primary-source conventions](round21_chambers.md).
This is an application of classical gauge theory to the integral
theorem, not a new nonvanishing theorem.

## 3. The precise strengthening of LeBrun's obstruction

In the positive-square setting of the inherited theorem,

\[
\mathcal E(g)+
\left(\frac13-\frac{k+4\ell}{A}\right)_+\ge c_*.
\]

Non-Ricci-flat Einstein metrics have \(\mathcal E=0\).
Ricci-flat metrics have \(\mathcal E=4\) under this definition and
must instead be excluded by the positive scalar-monopole budget.
Both points are needed to recover an all-sign nonexistence statement.

Taking \(\gamma=c_*/2\) gives a closed band
\[
\frac{k+4\ell}{A}\ge\frac13-\gamma
\quad\Longrightarrow\quad
\mathcal E(g)\ge c_*/2
\]
for every metric, and consequently
\(\delta_\sigma(g)\ge\sqrt{c_*/8}\), for either normalized sign.
The quantitative estimate implies the classical exact obstruction;
exact nonexistence alone does not imply quantitative stability.

The extra band is realized. Take
\[
X_m=\Sigma_2\times\Sigma_m,\qquad
A_m=8(m-1),\qquad k_m=\lceil A_m/3\rceil-1.
\]
Then \(0<1/3-k_m/A_m\le1/A_m\to0\). These distinct topologies lie
strictly below LeBrun's cited threshold but eventually inside the new
band. This establishes a nonvacuous strengthening relative to that
threshold, not priority over every other obstruction in the literature.

The comparison concerns [LeBrun's Einstein-obstruction results,
Proposition 3.2 through Corollary 3.4](https://arxiv.org/pdf/math/0003068).
It neither subsumes his absolute Ricci-energy and minimal-volume
theory nor removes the classical curvature inequalities from our proof.

[Full comparison, optimized defect and discrete qualifications](round21_comparison.md).

## 4. Proofs, checks, and resulting research position

- [Analytic theorem and parameterized extension](round21_analytic.md).
- [Symplectic chamber application](round21_chambers.md).
- [Classical comparison and realized strict threshold](round21_comparison.md).
- [Exact tensor-contraction checker](round21_analytic_check.py).
- [Defect optimization and integer checks](round21_comparison_check.py).
- [Executed verification](round21_verification.md).

The first line now has a more general analytic formulation with an
explicit equality model. It remains necessary to produce the required
calibrations on additional topological families before claiming a
broader topological obstruction. No Yau26 sign branch is settled here.
The established integral theorem, its source hypotheses, and this
new analytic extension are kept distinct in the proofs.
