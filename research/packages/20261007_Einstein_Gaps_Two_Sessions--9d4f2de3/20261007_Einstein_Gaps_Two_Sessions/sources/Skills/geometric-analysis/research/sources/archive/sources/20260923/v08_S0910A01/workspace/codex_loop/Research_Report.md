# Research Report: Step 24 buffered cutoff-flow tensor energies

## Task and context

This run checked the load-bearing tensor calculus for the four-dimensional normalized cutoff flow

\[
\partial_tg=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\]

with an auxiliary energy cutoff \(\eta\) satisfying \(\eta=1\) on a neighbourhood of \(\operatorname{supp}\chi\) and \(\operatorname{supp}d\eta\subset\{a=0\}^{\circ}\). The objective was to decide whether the Step 24 \(q=2\), weighted \(q=3\), and triangular defect inequalities have the stated weights and whether a hidden \((\nabla^2a)*g\) source survives.

## Work performed

I derived the curvature variation from the exact connection formula

\[
\partial_t\Gamma^\ell{}_{jk}
=\tfrac12g^{\ell m}(\nabla_jh_{km}+\nabla_kh_{jm}-\nabla_mh_{jk}),
\qquad
\partial_tR^\ell{}_{kij}
=\nabla_i(\partial_t\Gamma^\ell{}_{jk})
-\nabla_j(\partial_t\Gamma^\ell{}_{ik}).
\]

For \(h=-2aE\), the resulting mixed-index equation is

\[
\partial_t\operatorname{Rm}
=a\Delta\operatorname{Rm}+a\mathcal Q(\operatorname{Rm})
+(da)*\nabla E+(\nabla^2a)*E,
\]

where \(\mathcal Q\) is algebraic quadratic curvature. The memo records every index in the two cutoff tensors. Lowering an index adds the expected \(-2aE*\operatorname{Rm}\) algebraic term. The standard all-covariant Hamilton polynomial was cross-checked against the published Ricci-flow curvature formula in the [Cao–Zhu exposition](https://archive.intlpress.com/site/pub/files/_fulltext/journals/ajm/2006/0010/0002/AJM-2006-0010-0002-a002.pdf), and the normalized scaling contributes the additional \(-2R_{ijkl}\) term.

I then tested the regularized tensor norm \(F=(1+|\operatorname{Rm}|^2)^{1/2}\), including inverse-metric and volume-form variations. The Hessian-\(a\) terms were integrated by parts once. The exact contractions

\[
|E|\le C_4F,\qquad
|\nabla E|\le C_4|\nabla\operatorname{Rm}|,
\qquad |\nabla F|\le|\nabla\operatorname{Rm}|
\]

close all resulting first-derivative terms against curvature dissipation. Because \(a=\chi^2\),

\[
\frac{|da|^2}{a}=4|d\chi|^2,
\]

so no inverse power of \(\chi\) remains. The strict support buffer makes every term containing \(a\,d\eta\) or \(da\,d\eta\) vanish pointwise.

Finally, I derived the exact defect equation

\[
\partial_tE_{ij}=a(\Delta_LE_{ij}-2E_{ij})+\mathcal C_a(E)_{ij}
\]

and expanded all seven terms of \(\mathcal C_a(E)\). Contracting with \(2\eta^2E\), integrating Hessians of \(a\), and using \(\operatorname{div}E=\tfrac12d\operatorname{tr}E\) leaves only expressions quadratic in \(E,\nabla E\). The calculation also keeps the norm-variation cancellation: there is no separate strict \(-4a|E|^2\) damping term in the final squared-norm identity.

## Main results

The three proposed local inequalities are supported exactly, for every smooth time slice on which \(|d\chi|_{g(t)}\le C r^{-1}\) and \(0<r\le1\):

\[
\boxed{
H_2'+cD_2\le C\int\eta^2aF^3+Cr^{-2}H_2,}
\]

\[
\boxed{
Y'+cD_3\le Cr^{-2}Y+C\int\eta^2a^2F^4,}
\]

and

\[
\boxed{
Q'+cX\le Cr^{-2}Q+C\int\eta^2aF|E|^2.}
\]

The claimed weights are correct:

- The \(q=2\) Hessian/cutoff remainder is \((|da|^2/a)F^2\lesssim r^{-2}F^2\).

- Differentiating the extra testing factor \(a\) at \(q=3\) instead leaves \(|da|^2F^3\lesssim r^{-2}aF^3\), while the equation and test factors combine to give dissipation \(a^2F|\nabla\operatorname{Rm}|^2\) and reaction \(a^2F^4\).

- The defect curvature term is only the multiplicative potential \(aF|E|^2\). There is no additive curvature-only forcing and no independent \((\nabla^2a)*g\) source.

The Step 24 Sobolev variables are likewise correct:

\[
aF^3=F(\chi F)^2,\qquad
a^2F^4=F(aF^{3/2})^2,\qquad
aF|E|^2=F|\chi E|^2.
\]

Thus \(\chi F\), \(aF^{3/2}\), and \(\chi E\), respectively, give the proposed critical \(L^2\times L^4\) absorptions. No pointwise curvature bound is needed for these estimates.

## Artifacts and verification

The full derivation is in `Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md`. It contains the exact index formulas, metric and measure variations, both curvature energy tests, the exact defect Hessian cancellation, the Sobolev factorizations, and the assumptions needed to evolve the constants.

The supporting symbolic check is `Sessions/S0910A01/workspace/codex_loop/work/verify_tensor_energy_ledger.py`. It was run with:

```text
"$QIUSHI_PYTHON" Sessions/S0910A01/workspace/codex_loop/work/verify_tensor_energy_ledger.py
```

The script returned `All symbolic ledger checks: PASS`. It verifies the exact integrated contraction

\[
\begin{aligned}
\int2q\langle E,\mathcal C_a(E)\rangle
=\int\{&-2|E|^2\langle da,dq\rangle-2\tau E(dq,da)
+4E^2(dq,da)\\
&+q[-\tau\langle da,d\tau\rangle+2E(da,d\tau)]\},
\end{aligned}
\]

its degree-two homogeneity under \(E,\nabla E\mapsto\varepsilon(E,\nabla E)\), the square-cutoff identities, and all three Sobolev monomial factorizations.

No files outside `Sessions/S0910A01/workspace/codex_loop/` were modified.

## Unresolved issues and required next steps

The tensor inequalities themselves need no weight repair. The remaining gap is the uniform analytic bootstrap around them.

First, the calculation assumes an already smooth cutoff-flow solution. A quantitative existence or nondegenerate-approximation theorem is still needed for the degenerate coefficient \(a=0\) outside the selected support.

Second, initial cutoff and Sobolev bounds do not automatically persist. If \(g(t)\) remains \(\Lambda\)-bilipschitz to \(g_0\), then the initial relative Sobolev inequality, volume comparison, and \(|d\chi|\lesssim r^{-1}\) transfer with constants depending only on \(\Lambda\). But such metric comparison requires

\[
\int_0^t\|aE(s)\|_\infty\,ds<\infty
\]

uniformly. It does not follow from the three energy inequalities alone. The rigorous route should therefore be a simultaneous first-exit bootstrap carrying metric equivalence, the Sobolev constant, the cutoff-gradient bound, and current-time critical smallness \(A(t)^2\|F(t)\|_{L^2(\operatorname{supp}\chi)}\ll1\).

Qiushi should use the derivation memo as the tensor-calculus foundation for Step 24, then focus the next analytic work on: (1) cutoff-flow existence/approximation; (2) closure of that simultaneous first-exit bootstrap; (3) the positive-time finite-exponent/mean-value stage based on the verified weighted \(q=3\) estimate; and (4) an integrable weighted pointwise defect bound that improves the metric-equivalence bootstrap. Pointwise curvature must remain an output of this later stage, not an assumption in the energy lemma.