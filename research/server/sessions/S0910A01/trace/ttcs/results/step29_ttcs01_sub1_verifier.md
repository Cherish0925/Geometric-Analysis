# TTCS Independent Branch Record

```json
{
  "step_id": 29,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step29_simultaneous_support_theorem.md",
    "Sessions/S0910A03/workspace/notes/step29_consolidated_conditional_theorem.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md"
  ]
}
```

## Task

Verify the complete conditional chain for the four-dimensional negative-branch Yau Problem 26 argument on the Ishida-LeBrun no-Einstein family. The chain has three layers: (1) TOPOLOGICAL: For above-critical manifolds (sigma = D - A/3 > 0), CGB + Hirzebruch + SW monopole inequality give R >= sigma >= delta^2 Vol/(2pi^2), hence delta >= c sqrt(sigma/A) with no PDE. (2) ANALYTIC: For the critical boundary (sigma = 0), a buffered cutoff flow partial_t g = -2 chi^2(Ric+g) on selected maximal-function good supports produces: H_2 persistence -> S^2Y <= C beta^3/t -> ||aF||_inf <= C beta/t (three-factor Moser) -> J_6 persistence -> ||aE||_inf <= C delta(r^2/t)^{1/3} -> integrable velocity V(T) <= C delta theta^{2/3} r^2 -> metric comparison closes bootstrap. The shifted curvature T = Rm + G, U = aT gives continuation via Wang's theorem. (3) GEOMETRIC DOWNSTREAM: terminal recalibration gives int mathfrak_D <= 119 Q(T) = o(A); exponential pullback on fixed-volume plateau selects centers with vanishing pulled-back defect; Rauch tangent-space noncollapse; harmonic-coordinate compactness; smooth Einstein limit with calibrated Weyl spectrum (-1/6, 1/12, 1/12); Derdzinski contradiction (locally conformally Kahler but |W+|^2 = 1/24 != 2/3). KEY CLAIM: K_0 = Vol^{-1} int |Rm|^2 is uniformly bounded by 9 + O(1/A) + O(delta^2) across the IL family, making the critical product beta = S * H_2^{1/2} = C r^2 K_0^{1/2} a universal constant, hence the gap delta_0 is universal. Check: (a) Is the above-critical algebraic gap correct? (b) Is the bootstrap dependency graph non-circular? (c) Does the volume cancellation in beta hold exactly? (d) Is the Moser time exponent (1+n/2)/p_0 correct for the parabolic iteration? (e) Is the Derdzinski contradiction valid at the calibrated spectrum? (f) Are there any hidden gaps in the conditional chain?

## Output

# Scientific verification memo

## 1. Topological layer

Let \(E=\operatorname{Ric}+g\) and assume
\(\|g^{-1}E\|_{\mathrm{op}}\le \delta\). In dimension four,
\(\operatorname{Ric}^{\circ}=E^{\circ}\), and if \(e_1,\dots,e_4\) are the
eigenvalues of \(g^{-1}E\), then

\[
|\operatorname{Ric}^{\circ}|^2
=\sum_i(e_i-\bar e)^2
\le \sum_i e_i^2
\le 4\delta^2.
\]

Consequently,

\[
R=\frac1{8\pi^2}\int |\operatorname{Ric}^{\circ}|^2
\le \frac{\delta^2}{2\pi^2}\operatorname{Vol}(M,g).
\tag{1}
\]

The topological identity and monopole inequality in A03 Step 29 give

\[
I-R=\frac{2A}{3}-\sigma,
\qquad I\ge \frac{2A}{3},
\]

hence

\[
R\ge \sigma.
\tag{2}
\]

Thus the correct sandwich is

\[
\boxed{\sigma\le R\le
\frac{\delta^2}{2\pi^2}\operatorname{Vol}(M,g).}
\tag{3}
\]

The inequality direction stated in the task as
\(\sigma\ge \delta^2\operatorname{Vol}/(2\pi^2)\) is reversed.

A volume upper bound proportional to \(A\) follows directly from the scalar
term. Since \(|s+4|\le4\delta\),

\[
I\ge \frac{(1-\delta)^2}{6\pi^2}\operatorname{Vol}.
\]

Combining this with
\(I=2A/3-\sigma+R\le2A/3+R\) and (1) gives

\[
\operatorname{Vol}\,
\frac{1-2\delta-2\delta^2}{6\pi^2}
\le \frac{2A}{3}.
\tag{4}
\]

For example, when \(\delta\le1/4\),

\[
\operatorname{Vol}\le \frac{32\pi^2}{3}A,
\qquad
\delta^2\ge \frac{3}{16}\frac{\sigma}{A}.
\tag{5}
\]

Without assuming \(\delta\le1/4\), the direct conclusion is

\[
\boxed{\delta\ge
\min\left\{\frac14,\frac{\sqrt3}{4}\sqrt{\frac{\sigma}{A}}\right\}.}
\tag{6}
\]

Therefore the fixed-manifold above-critical obstruction is valid and uses no
flow. A formula \(c\sqrt{\sigma/A}\) without the minimum requires an a priori
upper bound for \(\sigma/A\), or a constant allowed to depend on the chosen
manifold.

The exact hypotheses of the cited Ishida–LeBrun Theorem 7 are not included in
the supplied files. In particular, its treatment of equality \(D=A/3\) and
the assumptions on \(X_j,N\) remain source-level inputs here.

---

## 2. Bootstrap dependency

The intended analytic order is mathematically natural:

\[
H_2
\longrightarrow Y
\longrightarrow \|aF\|_\infty
\longrightarrow J_6
\longrightarrow \|aE\|_\infty
\longrightarrow V
\longrightarrow \text{metric and Sobolev comparison}.
\]

However, the first-exit set in A01 Step 29 is defined only through (B1)–(B4),
while Step A uses

\[
\beta_a(t)\le4\beta_0,
\qquad
\beta_a=S(t)\|F(t)\|_{L^2},
\]

before \(H_2\) persistence has been proved. Neither the singular estimate
\(\|aF(t)\|_\infty\le C\beta_0/t\) nor metric comparison alone supplies that
uniform \(L^2\) estimate near \(t=0\).

Thus the written first-exit definition is incomplete. A simultaneous
first-exit set containing, for example,

\[
S(t)\le 4S(0),\qquad H_2(t)\le4H_2(0),
\]

makes Step A a standard self-improving energy estimate. With those variables
included, the dependency is triangular: Step A improves the assumed \(H_2\)
bound, and every later estimate uses only earlier outputs and metric/Sobolev
comparison.

Two additional support-construction details require explicit constants:

* A03 §3.1 uses threshold \(4K_0\) and then assumes a doubling constant
  \(C_D\le2\). A four-dimensional doubling constant is not generally at most
  \(2\). Taking threshold \(2C_DK_0\), or any larger fixed multiple, restores
  the stated good-set volume fraction.
* An \(r/5\)-separated net does not make the supports
  \(B_{2r/3}(p_\alpha)\) disjoint. The bounded-degree coloring described in
  A01 Step 29 is needed; one color retains a fixed fraction of the plateau
  volume.

---

## 3. Cancellation in \(\beta\) and the \(K_0\) issue

For one selected support, let \(V_\Omega\) denote its volume. The
Maheux–Saloff-Coste constant and maximal-function estimate have the form

\[
S\le C_{\rm Sob}\frac{r^2}{V_\Omega^{1/2}},
\qquad
H_2(0)\le M V_\Omega,
\qquad M=1+K_0.
\]

Therefore

\[
\boxed{\beta_0=S\,H_2(0)^{1/2}
\le C_{\rm Sob}r^2\sqrt{M}.}
\tag{7}
\]

The volume cancels exactly when the same support volume is used, and up to a
fixed Bishop–Gromov volume-ratio factor for nested supports. This part is
correct and is insensitive to collapse.

If

\[
r=c\,M^{-1/4},
\]

then

\[
\beta_0\le C_{\rm Sob}c^2.
\tag{8}
\]

Thus \(\beta_0\) can be placed below the absorption threshold by choosing the
dimensionless scale factor \(c\) sufficiently small. Uniform boundedness of
\(K_0\) is not needed for this cancellation itself.

It is needed later to retain a fixed unrescaled radius \(r\), hence a fixed
\(\rho\) for the local Einstein limit.

### Curvature-energy identity

A03 §6.1 states

\[
\int|\operatorname{Rm}|^2
=32\pi^2\chi+6\int|\operatorname{Ric}^{\circ}|^2.
\tag{9}
\]

With the full-tensor norm convention used in its displayed decomposition

\[
|\operatorname{Rm}|^2
=|W|^2+2|\operatorname{Ric}^{\circ}|^2+\frac{s^2}{6},
\]

Chern–Gauss–Bonnet instead gives

\[
\boxed{
\int|\operatorname{Rm}|^2
=32\pi^2\chi+4\int|\operatorname{Ric}^{\circ}|^2.}
\tag{10}
\]

Consequently,

\[
K_0
\le \frac{32\pi^2\chi(M)}{\operatorname{Vol}}
+16\delta^2.
\tag{11}
\]

Using the asserted calibration
\(\operatorname{Vol}/A\to32\pi^2/9\), this yields

\[
K_0=9\,\frac{\chi(M)}{A}+o(1)+O(\delta^2),
\tag{12}
\]

not \(9+O(A^{-1})+O(\delta^2)\) unless one also proves

\[
\chi(M)=A+O(1).
\tag{13}
\]

The relation \(2\chi+3\tau=A-D\) does not by itself imply (13). No estimate
\(\chi(M)/A\le C\), much less \(\chi(M)/A=1+O(A^{-1})\), appears in the supplied
material. Hence the stated numerical bound \(9+O(A^{-1})\) is not established.
A topology theorem giving \(\chi(M)\le CA\) would still suffice for a uniform
upper bound on \(K_0\), although not for the number \(9\).

There is also an internal radius inconsistency: A03 Assumption (A1) writes

\[
r_*=c(A/K_0)^{1/4},
\]

whereas §3 and §6 use \(r_*=cK_0^{-1/4}\). Since \(K_0\) is defined as an
average curvature energy, the latter is the curvature scale used by the
subsequent estimates.

---

## 4. Moser exponent and weighted recurrence

The parabolic time exponent itself is correct. Starting from a spacetime
\(L^{p_0}\) seed in dimension \(n\), parabolic scaling gives

\[
t^{-(n+2)/(2p_0)}
=t^{-(1+n/2)/p_0}.
\tag{14}
\]

Thus:

* for curvature, \(n=4,p_0=3\), the exponent is \(t^{-1}\);
* for the defect, \(n=4,p_0=6\), it is \(t^{-1/2}\), and the seed integral
  contributes \(t^{1/6}\), leaving \(t^{-1/3}\).

The Sobolev powers \(S^{2/3}\) and \(S^{1/3}\) also agree with the reciprocal
exponent sums.

There is, however, a concrete mismatch between the weighted energy and the
stated recurrence. Step 27 defines

\[
H_p=\int a^{p-2}f^p,
\qquad
z_p=a^{(p-1)/2}f^{p/2}.
\]

In dimension four, the parabolic Sobolev step controls

\[
\int z_p^3
=\int a^{\frac32(p-1)}f^{3p/2}.
\tag{15}
\]

But the next energy in the displayed iteration is

\[
H_{3p/2}
=\int a^{3p/2-2}f^{3p/2}.
\tag{16}
\]

The integrand in (15) equals \(a^{1/2}\) times the integrand in (16). Since
\(a\) approaches zero in the transition region, (15) does not uniformly
control (16). Infinite flatness of \(\chi\) does not by itself supply a bound
for \(a^{-1/2}\).

Therefore Step 27 equation (4.4) does not follow from equations (2.1)–(3.3)
as written. A weighted parabolic lemma with an explicitly evolving cutoff
exponent, or a different energy for \(U=aF\) and \(aE\), is the missing
analytic object. The polynomial \(p^4\) loss in A03 §4 is harmless once such a
recurrence is available, but it does not resolve this half-power mismatch.

The fixed-\(p\) absorptions for \(H_2\), \(Y\), and \(J_6\) are algebraically
plausible. Their tensor evolution formulas, Hessian-cutoff integrations by
parts, and Kato passage remain schematic in the supplied notes.

---

## 5. Shifted-curvature continuation

The shift

\[
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\operatorname{Rm}+G,\qquad U=aT
\]

is structurally appropriate because

\[
\operatorname{Ric}(T)=E,\qquad
\operatorname{Ric}(U)=aE,\qquad \nabla G=0.
\]

It removes the pure \(a g\) normalization term from the Ricci contraction and
leads to the expected schematic equation

\[
(\partial_t-a\Delta)U
=(\nabla a)*\nabla U+(\nabla^2a)*U
+a(U*U+G*U).
\]

What is not supplied is the full derivative induction establishing uniform
bounds for \(\nabla^mU\) under degeneracy of \(a\). A01 Step 29 itself records
that Wang Proposition 4.14’s grouped integration by parts and staggered
Hölder estimates have not been expanded. The continuation theorem therefore
remains an assumption rather than a consequence of the displayed equation.

---

## 6. Terminal geometry and Derdziński

The terminal arithmetic is correct:

\[
Q=\int|E|^2,\qquad
\int(s+4)^2\le4Q,
\]

and Step 28’s other two estimates give \(108Q\) and \(6Q\). Hence

\[
\int\mathfrak D\le(1+4+108+6)Q=119Q.
\]

Given uniform constants

\[
\operatorname{Vol}(P_i)\ge\alpha A_i,\qquad
|\sec|\le K,\qquad \rho>0,\qquad K\rho^2<\pi^2/4,
\]

the exponential-pullback averaging is sound. The upper Rauch estimate,
extension of the center integral from \(P_i\) to \(M_i\), and Liouville
invariance control multiplicity even on a collapsed base.

Smooth compactness needs more than a terminal sectional-curvature bound.
The required extra object is a smaller plateau buffer carrying curvature
derivative estimates from a positive-time parabolic interval. The cutoff flow
has the ordinary normalized Ricci-flow equation where \(a=1\), so local Shi
estimates should provide this once the buffer and time slab are stated
uniformly.

The Derdziński contradiction is valid. The calibrated data give

\[
s=-4,\qquad |W^+|^2=\frac1{24},\qquad
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

Since the metric is Einstein, \(\delta W^+=0\). Derdziński’s theorem makes
\(|W^+|^{2/3}g\) locally Kähler on the nonzero-\(W^+\) set. Here
\(|W^+|\) is constant, so \(g\) itself is locally Kähler up to constant
rescaling. A Kähler four-metric has

\[
\operatorname{Spec}(W^+)
=\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right),
\]

and therefore, for \(s=-4\),

\[
|W^+|^2=\frac{s^2}{24}=\frac23,
\]

contradicting \(1/24\).

---

## 7. Overall findings

| Question | Scientific result |
|---|---|
| (a) Above-critical algebra | Correct after replacing the stated chain by \(\sigma\le R\le\delta^2\operatorname{Vol}/(2\pi^2)\). The clean general estimate is \(c\min\{1,\sqrt{\sigma/A}\}\). |
| (b) Bootstrap dependency | The intended order is triangular, but \(H_2\) and \(S\) must be included in the first-exit set. |
| (c) Cancellation in \(\beta\) | Yes, up to fixed nested-support volume ratios. The separate formula \(K_0=9+O(A^{-1})+O(\delta^2)\) is not derived; the supplied CGB coefficient is also incorrect. |
| (d) Moser time exponent | Yes. The weighted Sobolev recurrence has an unresolved \(a^{1/2}\) mismatch. |
| (e) Derdziński step | Valid with the stated spectrum and norm convention. |
| (f) Remaining mathematical substance | Full tensor power inequalities, a compatible weighted Moser lemma, shifted-curvature derivative induction, uniform \(\chi(M)/A\), consistent support radius, colored support assembly, and uniform parabolic plateau buffers. |

Accordingly, the topological and terminal-geometric portions are largely
coherent, while the universal family constant and the central weighted
regularization theorem do not yet follow from the supplied derivations. Even
after those points are completed, this family result addresses only the
four-dimensional \(\operatorname{Ric}\simeq-g\) construction; the
all-dimensional Yau 26 proposition requires additional topology and both
Einstein-sign regimes.