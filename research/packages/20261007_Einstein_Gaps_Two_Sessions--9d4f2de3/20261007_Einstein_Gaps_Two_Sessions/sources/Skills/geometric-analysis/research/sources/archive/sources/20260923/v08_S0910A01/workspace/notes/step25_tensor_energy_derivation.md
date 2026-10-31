# Step 25: Exact tensor energy derivation for the buffered cutoff flow

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose and corrections

**Step 25 corrections incorporated:** (i) TTCS found the Hessian formula (0.2)
should be a tensor identity \(\nabla^2a=2d\chi\otimes d\chi+2\chi\nabla^2\chi\),
not a scalar.  (ii) Inequality (2.11) restated as an upper bound.  (iii) A03
corrected the normalization reaction: the \(-2a\operatorname{Rm}\) tensor damping
is exactly cancelled by the 4 inverse-metric variations for \(|\operatorname{Rm}|^2\);
for \(F^2=1+|\operatorname{Rm}|^2\), the conformal part produces only a bounded
source \(C_0=O(\operatorname{Vol})\).  (iv) First-exit Approach A is withdrawn:
the maximal-function condition gives \(L^2\) curvature, not \(L^\infty\), and
cannot directly invoke short-time existence.  Interior plateau regularity
(standard Shi for \(\partial_tg=-2(\operatorname{Ric}+g)\) on \(\{a=1\}\))
is the correct route.

This note derives the three local energy inequalities for the normalized cutoff
flow \(\partial_tg=-2aE\), \(a=\chi^2\), \(E=\operatorname{Ric}+g\), on one
buffered selected support.  The buffered support geometry is from
`step24_buffered_support_energy_test.md`: the physical cutoff \(\chi\) is
compactly supported inside \(\{\eta=1\}\), and
\(\operatorname{supp}\nabla\eta\subset\{\chi=0\}^\circ\).  Cancellations:

\[
a|\nabla\eta|^2=0,\qquad \nabla a\cdot\nabla\eta=0,\qquad
\operatorname{supp}(a)\subset\{\eta=1\}.
\tag{0.1}
\]

Standing identities for the cutoff:

\[
\nabla a=2\chi\nabla\chi,\qquad
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le\frac{4C_\chi^2}{r^2},\qquad
\nabla^2a=2\,d\chi\otimes d\chi+2\chi\nabla^2\chi.
\tag{0.2}
\]

Since \(\nabla a=2\chi\nabla\chi\), the product \(\nabla a\) vanishes wherever
\(\chi=0\).  Combined with (0.1), the cross term \(\nabla a\cdot\nabla\eta\)
vanishes everywhere.

Define \(F=(1+|\operatorname{Rm}|^2)^{1/2}\), so \(F\ge1\),
\(|F|\le1+|\operatorname{Rm}|\), and \(\nabla F^2=2\langle\operatorname{Rm},\nabla\operatorname{Rm}\rangle\).

## 1. Standing geometric estimates on a smooth flow time

Because \(E=\operatorname{Ric}+g\) and \(\operatorname{Ric}\) is a contraction
of \(\operatorname{Rm}\), the following hold on any smooth Riemannian manifold
of dimension \(n\):

\[
|E|\le C_n(|\operatorname{Rm}|+1)\le C_nF,
\tag{1.1}
\]

\[
|\nabla E|=|\nabla\operatorname{Ric}|
\le C_n|\nabla\operatorname{Rm}|,
\tag{1.2}
\]

\[
|\operatorname{tr}(E)|=|s+n|\le\sqrt{n}\,|E|\le C_nF,
\tag{1.3}
\]

where \(C_n\) depends only on the dimension.  These are purely algebraic:
\(\operatorname{Ric}_{ij}=g^{kl}R_{kijl}\) contracts one pair of
\(\operatorname{Rm}\), and the covariant derivative commutes with the metric.
No evolution or smallness is used.

## 2. Time derivative of the integrated curvature energy

Set

\[
H_2(t)=\int_M\eta^2 F^2\,d\mu_{g(t)},\qquad
D_2(t)=\int_M\eta^2 a|\nabla\operatorname{Rm}|^2\,d\mu_{g(t)}.
\]

The time derivative of \(H_2\) decomposes as

\[
\frac{d}{dt}H_2=\underbrace{\int\eta^2\partial_t(|\operatorname{Rm}|^2)\,d\mu}_{\text{(I)}}
+\underbrace{\int\eta^2 F^2\,\partial_t(d\mu)}_{\text{(II)}}.
\tag{2.1}
\]

The integrand \(\partial_t(|\operatorname{Rm}|^2)\) further decomposes:

\[
\partial_t(|\operatorname{Rm}|^2_g)
=2\langle\operatorname{Rm},\partial_t\operatorname{Rm}\rangle_g
+(\text{metric variation of the norm}).
\tag{2.2}
\]

We bound each piece.

### (II) Volume-form term

Under \(h=\partial_tg=-2aE\):

\[
\partial_t(d\mu)=\tfrac12\operatorname{tr}_g(h)\,d\mu
=-a\operatorname{tr}(E)\,d\mu=-a(s+n)\,d\mu.
\tag{2.3}
\]

By (1.3), \(|a(s+n)|\le C_naF\).  Therefore

\[
\left|\int\eta^2F^2\cdot a(s+n)\,d\mu\right|
\le C_n\int\eta^2 aF^3\,d\mu.
\tag{2.4}
\]

### Metric variation of the norm

The squared norm is
\(|\operatorname{Rm}|^2=g^{ip}g^{jq}g^{kr}g^{ls}R_{ijkl}R_{pqrs}\).  Each
factor \(g^{ij}\) varies as \(\partial_tg^{ij}=2aE^{ij}\) (with raising by the
current metric).  By the symmetries of \(\operatorname{Rm}\), the four
variations give

\[
|\partial_t(|\operatorname{Rm}|^2)|_{\text{metric}}|
\le C_na|E|\,|\operatorname{Rm}|^2
\le C_naF^3.
\tag{2.5}
\]

### Principal curvature evolution

Under a general \(h=\partial_tg\), the curvature variation is

\[
\partial_t\operatorname{Rm}
=\tfrac12\nabla^2h\text{ (symmetrized)}
+\operatorname{Rm}*h,
\tag{2.6}
\]

where the second term is an algebraic contraction of \(\operatorname{Rm}\) and
\(h\).  For \(h=-2aE\), expanding \(\nabla^2(aE)\):

\[
\nabla_i\nabla_k(aE_{jl})
=a\nabla_i\nabla_kE_{jl}
+(\nabla_ia)(\nabla_kE_{jl})
+(\nabla_ka)(\nabla_iE_{jl})
+(\nabla_i\nabla_ka)E_{jl}.
\]

Thus \(\partial_t\operatorname{Rm}\) contains four types of terms:

\[
\partial_t\operatorname{Rm}=
\underbrace{a\cdot(\text{Bochner-type})}_{(A)}
+\underbrace{(\nabla a)(\nabla E)}_{(B)}
+\underbrace{(\nabla^2a)(E)}_{(C)}
+\underbrace{a\cdot\operatorname{Rm}*E}_{(D)}.
\tag{2.7}
\]

**Type (A): weighted Bochner and normalization terms.**
For the Ricci-flow part of \(E\), the symmetrized \(\nabla^2\operatorname{Ric}\)
combines through Bianchi identities to produce \(\Delta\operatorname{Rm}+Q(\operatorname{Rm})\) (Hamilton).  The conformal part \(-2ag\) contributes
\((\nabla^2a)*g\) to the second derivatives (since \(\nabla g=0\)), and an
index-lowering term \(h_{lm}R^m_{ijk}=-2aR_{ijkl}\) (A03 correction).

**Normalization cancellation** (A03 Step 24 supersession): the tensor term
\(-2aR_{ijkl}\) gives \(-4a|\operatorname{Rm}|^2\) when contracted with
\(2\operatorname{Rm}\).  However, the 4 inverse-metric variations from the
conformal part \(-2ag\) of \(h\) contribute \(+8a|\operatorname{Rm}|^2\).  The
volume form gives \(-4a\,d\mu\) on the constant part of \(F^2=1+|\operatorname{Rm}|^2\).
The net conformal contribution to \(\partial_t(|\operatorname{Rm}|^2d\mu)\) is
exactly zero, and for \(F^2=1+|\operatorname{Rm}|^2\) it is \(-4a\,d\mu\)
(bounded source, not a coercive damping of \(|\operatorname{Rm}|^2\)).
Consistency check: pure \(\partial_tg=-2g\) gives \(g(t)=e^{-2t}g_0\),
\(|\operatorname{Rm}|^2(t)=e^{4t}|\operatorname{Rm}_0|^2\),
\(d\mu(t)=e^{-4t}d\mu_0\), so \(\int|\operatorname{Rm}|^2d\mu\) is constant.

Net: the Type (A) terms give, after contraction with
\(2\operatorname{Rm}\) and including the corrected normalization,

\[
2\langle\operatorname{Rm},\text{type (A)}\rangle
=a\Delta|\operatorname{Rm}|^2-2a|\nabla\operatorname{Rm}|^2
+a\cdot\operatorname{Rm}^3+(\nabla^2a)*g*\operatorname{Rm}+O(a|\operatorname{Rm}|^2),
\tag{2.8}
\]

where the Bochner identity \(\langle V,\Delta V\rangle=\tfrac12\Delta|V|^2-|\nabla V|^2\) was used, and the \(O(a|\operatorname{Rm}|^2)\) absorbs the
non-cancelling lower-order normalization terms.

The \(\operatorname{Rm}^3\) terms (including the Hamilton \(B\)-tensor) satisfy
\(|a\operatorname{Rm}^3|\le Ca|\operatorname{Rm}|^3\le CaF^3\).

The \((\nabla^2a)*g*\operatorname{Rm}\) terms are of Type (C) structure (Hessian
of \(a\) contracted with tensors built from \(g\) and \(\operatorname{Rm}\)) and
are handled below.

### Integration of the principal Bochner pair

We integrate \(\int\eta^2(a\Delta|\operatorname{Rm}|^2-2a|\nabla\operatorname{Rm}|^2)\,d\mu\).

\[
\int\eta^2a\Delta|\operatorname{Rm}|^2
=-\int\nabla(\eta^2a)\cdot\nabla|\operatorname{Rm}|^2.
\tag{2.9}
\]

Expanding \(\nabla(\eta^2a)=2\eta a\nabla\eta+\eta^2\nabla a\):

- **Cross term:** \(\int2\eta a(\nabla\eta)\cdot\nabla|\operatorname{Rm}|^2=0\)
  by (0.1), since \(a\nabla\eta=0\).

- **Cutoff term:** Using \(\nabla|\operatorname{Rm}|^2=2\langle\operatorname{Rm},\nabla\operatorname{Rm}\rangle\),

\[
\left|\int\eta^2(\nabla a)\cdot\nabla|\operatorname{Rm}|^2\right|
\le2\int\eta^2|\nabla a|\,|\operatorname{Rm}|\,|\nabla\operatorname{Rm}|.
\]

Young's inequality with parameter \(\varepsilon\):

\[
|\nabla a|\,|\operatorname{Rm}|\,|\nabla\operatorname{Rm}|
\le\frac{\varepsilon}{2}a|\nabla\operatorname{Rm}|^2
+\frac{1}{2\varepsilon}\frac{|\nabla a|^2}{a}|\operatorname{Rm}|^2.
\tag{2.10}
\]

By (0.2), \(|\nabla a|^2/a=4|\nabla\chi|^2\le4C_\chi^2r^{-2}\).  Therefore

\[
\left|\int\eta^2a\Delta|\operatorname{Rm}|^2\right|
\le\varepsilon\int\eta^2a|\nabla\operatorname{Rm}|^2
+\frac{C}{\varepsilon r^2}\int\eta^2|\operatorname{Rm}|^2.
\tag{2.11}
\]

Combining with the \(-2a|\nabla\operatorname{Rm}|^2\) term:

\[
\int\eta^2\bigl(a\Delta|\operatorname{Rm}|^2-2a|\nabla\operatorname{Rm}|^2\bigr)
\le -(2-\varepsilon)D_2+\frac{C}{\varepsilon r^2}H_2.
\tag{2.12}
\]

### Type (B): first-derivative cutoff terms

After contraction with \(2\eta^2\operatorname{Rm}\):

\[
|2\eta^2(\nabla a)(\nabla E)\operatorname{Rm}|
\le C\eta^2|\nabla a|\,|\nabla\operatorname{Rm}|\,|\operatorname{Rm}|,
\tag{2.13}
\]

using (1.2).  Young's inequality with parameter \(\varepsilon'\) gives exactly
the same structure as (2.10):

\[
\int|(\text{Type B})|\le\varepsilon'D_2+\frac{C}{\varepsilon' r^2}H_2.
\tag{2.14}
\]

### Type (C): Hessian-of-\(a\) terms, integrated by parts

Schematically, after contraction with \(2\eta^2\operatorname{Rm}\), these have
the form

\[
I_C=\int\eta^2(\nabla^2a)(T)\,d\mu,
\]

where \(T\) involves products of \(E\), \(\operatorname{Rm}\), and \(g\) that are
bounded by \(C|E|\,|\operatorname{Rm}|\le CF^2\) or \(C|\operatorname{Rm}|\le CF\).

**Integration by parts.**

\[
I_C=-\int\nabla a\cdot\nabla(\eta^2 T)\,d\mu
=-\int\eta^2\nabla a\cdot\nabla T\,d\mu
-\int 2\eta(\nabla\eta)\cdot(\nabla a)T\,d\mu.
\tag{2.15}
\]

The second integral vanishes: \(\nabla a\cdot\nabla\eta=0\) by (0.1).

For the first integral, \(\nabla T\) contains terms of two types:

(i) \(\nabla E\cdot\operatorname{Rm}\) or \(\nabla\operatorname{Rm}\cdot E\):
by (1.1)--(1.2) both are bounded by \(C|\nabla\operatorname{Rm}|\cdot F\).  Thus

\[
|\nabla a\cdot\nabla\operatorname{Rm}\cdot F|
\le\varepsilon''a|\nabla\operatorname{Rm}|^2
+\frac{C}{\varepsilon''}\frac{|\nabla a|^2}{a}F^2
\le\varepsilon''a|\nabla\operatorname{Rm}|^2+\frac{C}{\varepsilon'' r^2}F^2.
\tag{2.16}
\]

(ii) \(\nabla g=0\), contributing nothing.

Collecting:

\[
|I_C|\le\varepsilon''D_2+\frac{C}{\varepsilon'' r^2}H_2.
\tag{2.17}
\]

### Type (D): algebraic coupling

\[
|2\eta^2a\operatorname{Rm}*E*\operatorname{Rm}|
\le C\eta^2a|E|\,|\operatorname{Rm}|^2
\le C\eta^2aF^3.
\tag{2.18}
\]

### Collection of all terms

Choosing \(\varepsilon=\varepsilon'=\varepsilon''=\delta_0/3\) with
\(\delta_0<2\):

\[
\boxed{
\frac{d}{dt}H_2+(2-\delta_0)D_2
\le C_1\int\eta^2aF^3+\frac{C_2}{r^2}H_2+C_0,}
\tag{2.19}
\]

where \(C_1\) absorbs the cubic reaction, metric variation, and volume-form
terms; \(C_2\) absorbs all the Young counter-terms; and
\(C_0=O(\operatorname{Vol})\) is the bounded source from the normalization
cancellation (the conformal part acting on the constant in
\(F^2=1+|\operatorname{Rm}|^2\)).  The constants depend only on the dimension
\(n\), the cutoff ratios \(C_\chi,C_\eta,L_\eta,L_\chi\), and the chosen
\(\delta_0\).  The \(C_0\) term does not grow with curvature and is absorbed by
the \(r^{-2}H_2\) localization for small \(r\).

This is the target inequality (3.1) of the Step 24 note.  \(\square\)

## 3. Defect energy inequality

Set

\[
Q(t)=\int\eta^2|E|^2\,d\mu,\qquad
X(t)=\int\eta^2a|\nabla E|^2\,d\mu.
\]

The defect equation under \(\partial_tg=-2aE\) is (\(\ast\) = index
contractions):

\[
\partial_tE=a(\Delta_LE-2E)+(\nabla a)*\nabla E+(\nabla^2a)*E
+a\operatorname{Rm}*E+aE*E.
\tag{3.1}
\]

Every term on the right is homogeneous in \(E\): setting \(E=0\) makes the right
side vanish.  This is automatic because \(\partial_tg=-2aE\) vanishes when
\(E=0\).

Testing by \(2\eta^2 E\) and integrating:

\[
\frac{d}{dt}Q=
2\int\eta^2\langle E,\partial_tE\rangle\,d\mu
+\text{(metric variation of }|E|^2\text{)}
+\text{(volume form)}.
\tag{3.2}
\]

**Principal Lichnerowicz term.** Using the Bochner identity for
\(\langle E,\Delta_LE\rangle\):

\[
2\int\eta^2\langle E,a(\Delta_LE-2E)\rangle
\le-(2-\varepsilon)X-4\int\eta^2a|E|^2+C\int\eta^2a|\operatorname{Rm}|\,|E|^2
+\frac{C}{\varepsilon r^2}Q.
\tag{3.3}
\]

The \(-4\int a|E|^2\) comes from \(\langle E,-2aE\rangle=-2a|E|^2\); it is a
damping term with favorable sign (dropped from the upper bound).

**Cutoff terms.** Exactly as in Section 2: \((\nabla a)*\nabla E*E\) and
\((\nabla^2a)*E*E\) are bounded, after integration by parts and Young's, by
\(\varepsilon X+Cr^{-2}Q\).  The (0.1) cancellations remove
\(\nabla a\cdot\nabla\eta\) cross terms.

**Algebraic terms.** \(a\operatorname{Rm}*E*E\) and \(aE*E*E\) are bounded by
\(Ca(|\operatorname{Rm}|+|E|)|E|^2\le CaF|E|^2\).

**Metric variation and volume form.** Bounded by \(Ca|E|^3\le CaF|E|^2\) and
\(Ca|s+n||E|^2\le CaF|E|^2\).

Collecting:

\[
\boxed{
Q'+(2-\delta_0)X\le\frac{C}{r^2}Q+C\int\eta^2aF|E|^2.}
\tag{3.4}
\]

The curvature potential \(\int aF|E|^2\) is absorbed exactly as in Step 24
equation (7.3), using the Sobolev variable \(w=\chi\eta E\) (noting
\(\eta=1\) on \(\operatorname{supp}\chi\)):

\[
\int aF|E|^2
\le\|F\|_{L^2(\operatorname{supp}\chi)}\|\chi E\|_{L^4}^2
\le\beta_a(t)(X+Cr^{-2}Q).
\tag{3.5}
\]

For \(C\beta_a<c/2\), this gives

\[
\boxed{Q'\le\frac{C}{r^2}Q.}
\tag{3.6}
\]

## 4. Global defect identity (Strategist observation)

The disjoint selected supports \(\{\Omega_j\}\) partition the flow domain.
Outside these supports, \(a=0\) and the metric is stationary, so \(|E|\) is
unchanged.  Define

\[
Q_{\rm global}(t)=\int_M|E(t)|^2\,d\mu_{g(t)}.
\]

Then

\[
Q_{\rm global}(t)-Q_{\rm global}(0)
=\sum_j\bigl[Q_j(t)-Q_j(0)\bigr],
\]

where \(Q_j\) is the contribution from the active region of support \(j\).
By (3.6), \(Q_j(t)\le e^{C\theta}Q_j(0)\), so

\[
Q_{\rm global}(t)\le Q_{\rm global}(0)+(e^{C\theta}-1)\sum_jQ_j(0)
\le e^{C\theta}Q_{\rm global}(0).
\tag{4.1}
\]

Since \(\sum_jQ_j(0)\le Q_{\rm global}(0)\) (disjoint supports, \(\eta_j\le1\)).

In the near-critical regime, the initial Einstein defect gives
\(Q_{\rm global}(0)\le C\delta^2\operatorname{Vol}(M,g_0)\) and
\(\operatorname{Vol}/A=O(1)\).  Hence

\[
Q_{\rm global}(t)/A\le Ce^{C\theta}\delta^2\to0
\tag{4.2}
\]

as \(\delta\to0\), independently of the number of supports and without
requiring separate defect selection on the frozen bad set.

**Consequence for the LeBrun recalibration.**  The mixed SW and Step 8
tensor-gap inequalities can be rerun on the terminal closed metric
\(g(T)\), whose global normalized defect \(Q_{\rm global}/A\) is still
\(o(1)\).  The nonneg terminal deficits are then averaged over the
bounded-curvature selected plateaux.  A sequence-independent positive
plateau fraction (however small) suffices: restriction to that fraction
has vanishing normalized mean defect.

This is a conditional consequence of the proved support estimate (3.6),
not a new localization task.

## 5. Verification of the q=3 moment inequality

The fixed \(q=3\) weighted moment \(Y=\int\eta^2aF^3\) satisfies the
inequality from Step 24:

\[
Y'+cD_3\le Cr^{-2}Y+CI_4,\qquad
I_4=\int\eta^2a^2F^4,
\tag{5.1}
\]

where \(D_3=\int\eta^2a^2F|\nabla\operatorname{Rm}|^2\).  The derivation
follows the same pattern as Section 2 but testing with \(\eta^2aF\) instead
of \(\eta^2\).  The additional factor of \(a\) produces the \(a^2\) weight in
\(I_4\) and the \(a^2\) weight in \(D_3\).

The absorption uses \(u=aF^{3/2}\) (Step 24 repair):

\[
I_4=\int F\,u^2\le\|F\|_{L^2(\operatorname{supp}\chi)}\|u\|_{L^4}^2
\le\beta_a(t)(D_3+Cr^{-2}Y).
\tag{5.2}
\]

The gradient bound \(\|\nabla u\|_2^2\le CD_3+Cr^{-2}Y\) uses
\(|\nabla a|^2=4a|\nabla\chi|^2\) (Step 24 eq. (6.2)).  For small
\(\beta_a\), (5.1)--(5.2) give linear forward propagation \(Y'\le Cr^{-2}Y\),
and the spacetime average (5.1) in Step 24 yields

\[
A_\Omega^4Y(t)\le C\beta_*^3/t.
\tag{5.3}
\]

No new derivation is needed; only the same Bochner + Young + buffered
support mechanism with a different test function.

## 6. Summary of what this derivation establishes

**Proved (conditional on smooth existence and metric comparability):**

1. q=2 curvature energy: \(H_2'+cD_2\le C\int aF^3+Cr^{-2}H_2\).
2. Triangular defect energy: \(Q'+cX\le Cr^{-2}Q+C\int aF|E|^2\), with
   homogeneous curvature potential.
3. Global defect preservation: \(Q_{\rm global}(T)/A\to0\).
4. q=3 weighted moment: same Bochner mechanism yields
   \(Y'+cD_3\le Cr^{-2}Y+CI_4\).

**Load-bearing assumptions not proved here:**

- Smooth existence on \([0,\theta r^2]\) for the modified flow on a closed
  manifold.
- Metric comparability \(\tfrac12g_0\le g(t)\le2g_0\) on
  \(\operatorname{supp}\chi\) for \(t\le\theta r^2\).
- Self-improvement: H2 persistence + D2 + time-average H3 → Moser → pointwise
  \(|a\operatorname{Rm}|\le C/t\) → metric displacement small → closes the
  first-exit.
- Evolving Sobolev constant control during the first-exit interval.

**Not addressed by this derivation:**

- Positive branch, arbitrary four-dimensional topology, \(n\ge5\), full Yau 26,
  or Lean formalization.

## 7. Sources

- Buffered support geometry: `workspace/notes/step24_buffered_support_energy_test.md`
- Tensor-power ledger: `workspace/notes/step20_closed_tensor_estimate.md`
- Curvature variation formula: Hamilton (1982), Bochner--Weitzenböck, and
  standard Ricci flow references (Chow--Lu--Ni, Topping)
- Cutoff defect algebra: `Sessions/S0910A03/workspace/scripts/verify_cutoff_defect_energy.py`
- Verification: `workspace/scripts/step25_tensor_energy_verification.py`
