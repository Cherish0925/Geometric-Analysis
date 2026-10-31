# Independent review of the coupled spinor--Weyl approximation

Date: 2026-09-19. Scope: task-local `round2_rigidity.md`, especially Section 5a, and its checker. The independent reviewing agent used task-local files. The root follow-up below also checks the stated spinor input in the live manuscript and the later weighted-energy argument. The symbolic checker passes.

## Conclusion

The coupled approximation follows with the displayed constants from the declared spinor amplitude, Hodge, and eigenline-defect inputs. Its construction avoids division at spinor zeros. The intrinsic negative-Sobolev estimate uses no hidden Sobolev, injectivity-radius, or coordinate comparison assumption, provided its norm is defined as below.

Two exposition points identified by the independent review, both subsequently corrected in the proof:

* The original ambiguous Weyl norm label is now `u=|W+|HS`, distinct from the Ricci spectral operator norm. Identities such as `u²=(3/2)a²` and the squared-distance formula use the Hilbert--Schmidt convention.
* Section 1 now explicitly derives the spinor estimate `integral_U |(I-Pi)psi|² <= 2Delta/(27gamma)+eta` from the spectral component of the rescaled Seiberg--Witten deficit. This input is distinct from its harmonic-form counterpart.

## 1. Pointwise algebra and all rounded constants

With `rho=|psi|`, the tensor

\[
 A_\psi=\frac{\rho^2}{24}I-\frac18\psi\otimes\psi
\]

is trace-free and has eigenvalues `(-rho²/12,rho²/24,rho²/24)`. Thus

\[
 |A_\psi|_{HS}^2=\rho^4/96,
 \quad \rho\le3\Longrightarrow |A_\psi|_{HS}\le9/(4\sqrt6).
\]

For an orthogonal rank-one projection `Pi`, let `y=(I-Pi)psi`. Direct expansion gives

\[
 |\psi\otimes\psi-\rho^2\Pi|_{HS}^2=2\rho^2|y|^2.
\]

Writing `A_psi=(rho²/2)A0(Pi)-(psi tensor psi-rho²Pi)/8` and using `|A0|²=1/24` yields the stated upper bound

\[
 |A_\psi-A_0|^2\le\rho^2|y|^2/16+(\rho^2-2)^2/48.
\]

The preliminary pointwise estimate `|W+-A0|²<=D/16` is valid globally under the stated small Ricci defect, not just on the good set. Indeed `0<=z=w+a<=a` and

\[
 G=2z(-4s/3+4a-2z)\ge(-8s/3)z\ge8z
\]

because `s<=-4+1/16`. Thus no derivative of a lowest-eigenline choice is used on the bad set.

The amplitude calculation is correct:

\[
 \|\rho-\sqrt2\|_2^2
 \le8\Delta/27+41\,dcal/432+\eta.
\]

Using `(3+sqrt(2))²<20`, the resulting constants are exactly

\[
 \frac98\frac{16}{27}+\frac{20}{24}\frac8{27}
 =\frac{74}{81}<1,
\]

\[
 \frac18+\frac98(576)+\frac{20}{24}\frac{41}{432}
 =648+\frac18+\frac{205}{2592}<649.
\]

The rounded `Delta+649dcal+eta` bound is therefore justified.

For a covariant derivative `v=nabla psi`, differentiation gives

\[
 |dA_\psi(v)|^2=\rho^2|v|^2/32+\langle\psi,v\rangle^2/96
 \le\rho^2|v|^2/24.
\]

The two-form Weitzenbock identity gives, with `rho<=3` and `-s<=5`,

\[
 \int|\nabla\psi|^2\le4\Delta/27+15V+18\int u+\eta.
\]

Since `u²=(t-s)²/384 <= (t²+s²)/192`,

\[
 \int|\nabla\psi|^2
 \le\frac4{27}\Delta+
       \left(24+\frac{225}{192}\right)V+
       \frac9{192}dcal+\eta
 \le26V+\Delta+dcal+\eta.
\]

Multiplication by `3/8` then gives the claimed `10V+Delta+dcal+eta` bound for `integral |nabla A_psi|²`. No extra spatial regularity of an eigenframe enters.

## 2. Approximation errors

The statement is an existence assertion for each fixed metric, class and `eta>0`: choose a sufficiently accurate smooth positive approximation to `sqrt(q)`, then a corresponding rescaled monopole solution. It does not assert that these solutions converge as the smoothing parameter changes.

Because `q>=-s>3` with a strict uniform margin, the smooth weight can be chosen with `f²>=3`. The maximum-principle estimate has strict room below `rho=3`, so that cap can hold simultaneously. There are only finitely many errors and subsequent amplification constants in this proof; choosing their preliminary tolerance sufficiently smaller than `eta` justifies using a single final `eta`. This selection need not be uniform over geometries, and the final estimates do not assume that it is.

For normalized conclusions along a sequence, choose `eta_j/Vol(M_j)→0`. Merely fixing an absolute `eta` does not automatically imply a negligible normalized error if volumes are allowed to vary toward zero. The quantified theorem permits the appropriate choice.

## 3. Intrinsic weak Bianchi estimate

Define the normalized inhomogeneous covariant Sobolev norm by

\[
 \|\phi\|_{H^1,av}^2=\fint_M(|\phi|^2+|\nabla\phi|^2),
\]

and define its dual by the averaged distribution pairing. Tensor bundles and all contractions use the same metric as the covariant derivative. On the closed manifold, integration by parts gives

\[
 \|\operatorname{div}R\|_{H^{-1},av}\le C\|R\|_{2,av}
\]

and, from Cotton expressed as a covariant first derivative of `E` and its trace,

\[
 \|\operatorname{div}W^+\|_{H^{-1},av}
 \le C\|E\|_{2,av}\le C\delta.
\]

The dimensional constant includes conversion between the Weyl-operator and full-tensor conventions. Metric and Hodge contractions are covariantly parallel, so their derivatives produce no uncontrolled geometric coefficient. Combining these inequalities with the coupled `L²` error gives (18e) exactly in its stated strength.

This is a uniform inequality **within each geometry**. It does not identify Sobolev spaces for different metrics or imply an intrinsic compact embedding uniform across a collapsed sequence. The note's final limitation is therefore mathematically necessary and correctly retained.

## 4. What cannot be concluded from the new approximation

The bounds furnish smooth bounded tensor models whose normalized first-derivative energies are bounded, with small normalized `L²` curvature error and weak divergence. They do not show that `nabla A_psi` tends to zero. They also do not supply controlled coordinate frames or a uniform negative-order elliptic estimate across varying metrics.

The error product `R nabla psi` has small normalized `L¹` norm by Cauchy--Schwarz, but an `H^{-1}` conclusion would need another argument. The task's explicit four-dimensional bump construction correctly obstructs that inference from these norms alone. None of the preceding checks upgrades it into a counterexample satisfying the curvature and monopole equations.

## 5. Root follow-up: source normalization and the weighted energy identity

The root read the live manuscript's rescaled Seiberg--Witten decomposition
in `20260916_rigidity.tex`, beginning at line 645. Its definitions are
`psi=2sqrt(2)sigma(Phi)` and
`D_eig=2 integral(<W+psi,psi>+sqrt(2/3)|W+|HS|psi|²)`.
The nonnegative-defect identity gives `D_eig<=4Delta/27+o(1)`.
On a region with lowest-eigenvalue gap at least gamma, the integrand
dominates `2gamma|(I-Pi)psi|²`. This confirms the exact coefficient in
(2a), with smoothing error chosen before the subsequent estimates.
This is a check of the input and its algebraic use, not an independent
new proof of monopole solvability.

For the new Section 8, the root independently checked the integration
signs. With `w=rho²`, self-duality gives `d*psi=-*dpsi`, and

\[
 \langle d\psi,d(w\psi)\rangle+
 \langle d^*\psi,d^*(w\psi)\rangle
 =2w|d\psi|^2+2\langle *d\psi,i_{\nabla w}\psi\rangle.
\]

The rough-Laplacian side is
`w|nabla psi|²+(1/2)|dw|²`, plus `w B_psi`. Since
`dw=2rho drho`, this gives (24), including both signs and coefficients.
The exact first-jet identity (22) and curvature polynomial (23) therefore
combine to (25) with complete cancellation of the two cross terms.

For the normalized energy limits, the bounded amplitude and its L2
convergence imply convergence of every finite amplitude moment. The
curvature error R contributes at most `C||R||_(2,av)` to all relevant
averages. The unweighted Hodge equation then gives average gradient
energy 2. In the weighted equation the two error terms are bounded by
`C||drho||_(2,av)||dpsi||_(2,av)` and `C||drho||_(2,av)²`, respectively,
so they vanish. The weighted gradient energy tends to 4. Substitution
in the differentiated quadratic-map identity and (22) gives exactly
`1/8` and `1/16`. No uniform integrability of derivative energy was
assumed to interchange a variable weight with a limit; the weighted
energy limit was proved directly instead.

Thus Section 8 supplies a necessary energy defect under the explicitly
stated vanishing normalized monopole/calibration deficits. It does not
construct such a sequence or establish a uniform geometric compactness
principle.
