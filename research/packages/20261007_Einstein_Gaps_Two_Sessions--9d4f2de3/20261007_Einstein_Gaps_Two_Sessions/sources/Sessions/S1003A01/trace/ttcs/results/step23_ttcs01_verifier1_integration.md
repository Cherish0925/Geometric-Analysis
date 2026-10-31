# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 23,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step23_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step23_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the scalar-relaxed j=1 angular construction result as a geometric analyst. Check whether the conformal Schur-complement experiment, pure-trace redundancy repair, finite-basis interpretation, two-sided line tests, and conclusions are mathematically and numerically consistent. Identify any substantive error in formulas or interpretation, especially whether positivity of the finite blocks says only what the note says and whether an actual scalar-normalized construction would require further work. Ground the answer in the actual script, canonical JSON outputs, and synthesis note; give concrete repairs or next decisive computation if needed.

## Integrated Scientific Memo

## Verification memo

### Bottom line

The script and JSON outputs are internally consistent **as a finite-dimensional compression experiment**. They support only this statement:

> For the stated trace-free tensor basis, the single scalar angular factor \(F=\sqrt3\,\mathrm{Ad}_{00}\), the given radial bases, and the sampled objective, the raw metric Hessian, conformally minimized Schur complement, and reported sampled-coupling restrictions have positive generalized minima.

They do **not** establish positivity of the full \(j=1\) isotype, a positive continuum spectral gap, gauge-sliced local stability, or positivity on the nonlinear hypersurface \(s=-24\). The synthesis note is appropriately cautious about finite-basis positivity, but it overstates both the angular completeness and some scalar-relaxation conclusions.

---

## 1. Schur complement: algebraically correct, interpretation needs repair

Writing the Hessian in metric/conformal coordinates as
\[
H=\begin{pmatrix}H_{aa}&H_{ab}\\H_{ba}&H_{bb}\end{pmatrix},
\]
the code computes
\[
H_{\rm rel}=H_{aa}-H_{ab}H_{bb}^{-1}H_{ba}.
\]
All three files have \(H_{bb}>0\):
\[
\lambda_{\min}(H_{bb})
=1.98\times10^{-3},\quad 9.01\times10^{-4},\quad 2.51\times10^{-4},
\]
so this is the correct finite-dimensional minimization over the sampled conformal coefficients.

At an **exact** \(s=-24\) base, let
\[
L=-6\Delta+48,\qquad A=-4\Delta+24.
\]
For compactly supported or sufficiently decaying variations,
\[
D^2J_6(h,2\phi g)=\langle A\,Ds[h],\phi\rangle,
\qquad
D^2J_6(2v g,2\phi g)=\langle ALv,\phi\rangle.
\]
Thus minimization over a dense conformal space yields
\[
Lv=-Ds[h],
\]
the linearized scalar-normalization equation. The docstring’s limiting interpretation is therefore structurally correct.

However, the script comment

> “the mixed Hessian \(H_{ab}\) comes entirely from the scalar residual”

is misleading if “scalar residual” means only \(\frac14\int(s+24)^2\). The \(P\)-part also contributes. The correct statement is:

> At an exact scalar-normalized base, \(H_{ab}\) is the Galerkin matrix of \(A\,Ds[h]\), and \(H_{bb}\) is the Galerkin matrix of \(AL\).

Consequently,
\[
H_{ab}^{T}a=0
\]
means only that \(A\,Ds[h_a]\) is orthogonal to the **sampled conformal test space**. It is not, in general, the pointwise condition \(Ds[h_a]=0\). “Sampled scalar-coupling kernel” is safer than “scalar-preserving tangent space.”

The outputs also do not quantify the base residual \(s+24\). The tiny gradients \(10^{-17}\)–\(10^{-18}\) do not certify scalar normalization, because every tested first variation carries mean-zero \(j=1\) angular dependence and therefore pairs trivially with an invariant base-gradient density. The agreement of \(J_0\) with the stored energy checks integration, not \(\|s+24\|\). The computation should report at least
\[
\|s+24\|_{L^2},\qquad \|s+24\|_{L^\infty}.
\]

---

## 2. Pure-trace redundancy repair is correct

At first order,
\[
e^{2\phi}(g+h)=g+h+2\phi g+O((h,\phi)^2).
\]
Hence the trace component of a metric variation is already represented by the conformal variable:
\[
h=h^\circ+\frac{\operatorname{tr}h}{4}g,
\qquad
\phi=\frac{\operatorname{tr}h}{8}.
\]
Including both an arbitrary pure-trace tensor and an independent conformal coefficient makes the parametrization noninjective. The observed equal-diagonal metric coefficients cancelled by a conformal coefficient are therefore a coordinate redundancy, not a geometric near-zero mode. Removing the pure-trace tensor is the right repair.

Two textual corrections are needed:

* The top docstring says “all ten symmetric … tensors,” but the code actually uses nine trace-free tensors per radial function.
* The nine matrices span trace-free symmetric tensors but are not an orthonormal tensor basis: off-diagonal matrices have norm \(\sqrt2\), and the diagonal differences are mutually nonorthogonal. This is harmless because the code computes and uses the Gram matrix.

There is also a finite-space mismatch: metric modes have envelope \(u^2(1-u)^3\), while conformal modes have \(u^2(1-u)^4\). Thus exact trace/conformal redundancy is not represented with identical radial spaces. Removing trace remains appropriate, but this discretization does not represent every trace perturbation allowed by the metric endpoint class.

---

## 3. Substantive angular incompleteness: this is not the full \(j=1\) isotype

The most important interpretive defect is the claim that fixing
\[
F=\sqrt3\,\mathrm{Ad}(q)_{00}
\]
selects one representative and that the remaining copies are equivalent by left \(SU(2)\).

For matrix coefficients \(\mathrm{Ad}_{ab}\), left translation rotates the first index \(a\), so fixing that index is legitimate. The second index \(b\) is a multiplicity index and is generally mixed by frame derivatives/right actions. On the anisotropic diagonal base, right translations are not full symmetries. A full fixed-left-row \(j=1\) tensor space requires
\[
\operatorname{span}\{\mathrm{Ad}_{0b}H_A:\ b=0,1,2\},
\]
not only \(\mathrm{Ad}_{00}H_A\).

Therefore the script computes a compression of the full \(j=1\) Hessian, not an invariant \(j=1\) block. This matters especially for scalar relaxation: the conformal ansatz contains only \(\mathrm{Ad}_{00}\phi_0(x)\). Tensor modes whose scalar linearization lies in the \(\mathrm{Ad}_{01}\) or \(\mathrm{Ad}_{02}\) channel cannot be compensated by this scalar basis. Their vanishing sampled coupling can arise by angular symmetry rather than because \(Ds[h]=0\).

Accordingly, the note’s statement that the order-four and order-six lowest modes are “already in the sampled scalar kernel” is numerically true but not evidence that they are scalar-preserving geometrically. Their zero conformal coefficients may be forced by the compressed angular symmetry.

The repaired experiment should include
\[
h=\sum_{b=0}^{2}\mathrm{Ad}_{0b}\sum_A k_{bA}(x)H_A,
\qquad
\phi=\sum_{b=0}^{2}\mathrm{Ad}_{0b}\phi_b(x),
\]
then block this full space by the residual discrete symmetries of the diagonal background.

---

## 4. Numerical outputs and two-sided tests are coherent

The reported data are consistent with the code:

* Haar means are \(O(10^{-16})\), and the reported triplet Gram matrix is the identity to that accuracy.
* The base objective agrees with the stored value to \(3.0\times10^{-13}\) at \(n_{qx}=160\) and \(5.7\times10^{-13}\) at \(192\).
* No metric Gram directions are discarded: ranks are \(18,36,54\).
* Every reported raw and relaxed generalized eigenvalue is positive.
* The two-sided quotients reproduce the AD Hessian. For example,
  \[
  \lambda_{\rm rel}^{(6)}=0.1209451284747587,
  \]
  while at \(\varepsilon=10^{-3}\),
  \[
  \frac{J(+\varepsilon d)+J(-\varepsilon d)-2J(0)}{\varepsilon^2}
  =0.12094371082405075.
  \]

The deterioration at \(\varepsilon=1.25\times10^{-4}\) is consistent with subtractive cancellation, since the energy increment is only \(O(10^{-9})\).

These tests do **not** independently validate the continuum functional: `oj` and `hj` use the same curvature routine and quadrature. They check AD differentiation and the local Taylor expansion of the same discretized objective. Moreover, the finite-amplitude path is not scalar-normalized.

Conditioning is worsening rapidly:
\[
\kappa(G)\approx1.5\times10^2,\ 3.7\times10^4,\ 1.5\times10^6,
\]
and
\[
\kappa(H_{bb})\approx5.1\times10^4,\ 1.9\times10^5,\ 1.8\times10^6.
\]
The sign \(0.1209>0\) is not presently threatened, but localized radial bases are warranted.

The angular Haar diagnostic is also not exactly a direct check of `ad00`: it invokes `ad_row0` in a different coordinate convention. Analytically the normalization is right, but a direct Euler-coordinate check using the same `ad00` routine would be cleaner.

---

## 5. The order-two scalar-lowering interpretation is incorrect

At order two,
\[
\lambda_{\rm raw,min}=0.89574958
\]
also appears unchanged in the sampled scalar-kernel spectrum. After relaxation a **different coupled branch** becomes the new minimum
\[
\lambda_{\rm rel,min}=0.74992162.
\]
Thus the data do not show that the same mode moved from \(0.89575\) to \(0.74992\). The stored `lowest_metric_mode` is the relaxed minimizer, not the raw minimizer.

Indeed the raw spectrum contains a likely coupled branch at
\[
14.849066,
\]
which disappears from that location after relaxation. Sector-wise, the appropriate reading is that a coupled branch is lowered dramatically and crosses below the uncoupled \(0.89575\) branch. Therefore
```python
scalar_lowering = eraw[0] - erel[0]
```
is not a meaningful branchwise scalar-lowering statistic.

A correct sentence is:

> At order two, scalar relaxation lowers a coupled branch enough to make it the new ground branch; it does not lower the original raw ground eigenvector from \(0.89575\) to \(0.74992\).

Likewise, at orders four and six the equality of the global minima before and after relaxation does not mean scalar relaxation is negligible throughout the low spectrum. New relaxed levels appear at
\[
0.2825284\quad(n_{\rm rad}=4),\qquad
0.1444707\quad(n_{\rm rad}=6),
\]
so the coupled scalar-relaxed sector is decreasing strongly and is close to the reported global minimum \(0.1209451\). The conclusion

> “integrating out scalar response does not destabilize the current lowest mode”

is defensible only for the particular compressed global minimizer, not as a statement about the coupled \(j=1\) sector.

Branchwise lowering should be measured by raw Rayleigh quotients of each relaxed eigenvector and by overlaps between the raw and relaxed eigenbases.

---

## 6. Exact meaning of finite-block positivity

The note is correct that the values
\[
0.89575,\quad0.17823,\quad0.12095
\]
are finite-space approximations and do not prove a positive spectral lower bound. In fact the conclusion should be even narrower:

1. The metric spaces change with \(n_{\rm rad}\), and the conformal spaces change simultaneously with \(n_\phi\), so metric and scalar convergence are confounded.
2. The angular space is only a fixed-index compression, not the full \(j=1\) isotype.
3. No geometric gauge quotient has been imposed.
4. The generalized denominator is the \(L^2\) Gram norm of the trace-free seed \(h\), not of the full normalized tangent
   \[
   h+2vg.
   \]
   Since \(h\) is trace-free,
   \[
   \|h+2vg\|_{L^2}^2=\|h\|_{L^2}^2+16\|v\|_{L^2}^2.
   \]
   Signs are unchanged, but the printed relaxed values are not standard full-tangent Hessian eigenvalues.

The low order-four and order-six vectors are concentrated in paired off-diagonal polarizations, compatible with projected Lie-derivative sectors. This is suggestive rather than conclusive. The full \(j=1\) space contains genuine diffeomorphism directions \(\mathcal L_Xg\), so without a gauge slice one should expect zero modes at a critical base. The falling positive compressed minima may be approximating such directions while being unable to represent them exactly because the other \(\mathrm{Ad}_{0b}\) components are absent.

---

## 7. An actual scalar-normalized construction requires further work

The line paths are
\[
g_\varepsilon
=e^{2\varepsilon\phi}\bigl(g+\varepsilon h\bigr)
\]
with a finite, first-order optimal \(\phi\). They are not shown to satisfy
\[
s_{g_\varepsilon}=-24.
\]
A genuine normalized path requires solving, for each \(\varepsilon\),
\[
-6\Delta_{g+\varepsilon h}u_\varepsilon
+s_{g+\varepsilon h}u_\varepsilon
+24u_\varepsilon^3=0,\qquad u_\varepsilon\to1,
\]
then setting
\[
\widehat g_\varepsilon=u_\varepsilon^2(g+\varepsilon h).
\]
One must evaluate
\[
P(\widehat g_\varepsilon)=J_6(\widehat g_\varepsilon)
\]
and report the residual of the nonlinear solve.

There is also an exterior-tail issue. Both sampled fields vanish at \(x=X\), whereas the solution of
\[
Lv=-Ds[h]
\]
generally has a nonzero decaying homogeneous CH tail outside the source. Increasing \(n_\phi\) at fixed \(X\) within the factor \((1-u)^4\) cannot recover that tail. A correct continuum limit needs an exact CH exterior Dirichlet-to-Neumann condition, an explicit decaying-tail basis, or a limit \(X\to\infty\).

Finally, \((1-u)^3\) gives only finite-order contact with the zero extension, not a smooth exact-CH collar. For application of the smooth conformal theorem, one needs a \(C^\infty\) cutoff or a quantified smoothing argument.

---

## Decisive next computation

The clean repair is a full scalar-and-gauge reduced radial problem:

1. Include all three multiplicity components \(\mathrm{Ad}_{0b}\) for both tensors and conformal scalars.
2. Compute \(Ds[h]\) explicitly and solve
   \[
   (-6\Delta+48)v=-Ds[h]
   \]
   with the exact decaying CH exterior response.
3. Report the residual
   \[
   \|Ds[h]+Lv\|_{L^2}
   \]
   rather than inferring scalar tangency from \(H_{ab}^{T}a=0\).
4. Construct the full \(j=1\) Lie-derivative family, test the Hessian Ward identities, and form a gauge-orthogonal slice.
5. Use localized radial bases and vary \(n_{\rm rad}\), \(n_\phi\), radial quadrature, and angular quadrature independently.
6. Track coupled branches by eigenvector overlaps; in particular follow the branches producing \(0.28253\) and \(0.14447\), not only the global minimum.
7. If a negative sliced mode appears, solve the nonlinear scalar-normalization equation for both signs and evaluate \(P\) with independent/certified quadrature.

Thus the finite matrices and line tests are numerically coherent, and the pure-trace repair is sound. The substantive corrections are that the experiment is not the full \(j=1\) isotype, the sampled coupling kernel is not the true scalar tangent space, the order-two “lowering” compares different branches, and no actual nonlinear scalar-normalized construction has yet been produced.