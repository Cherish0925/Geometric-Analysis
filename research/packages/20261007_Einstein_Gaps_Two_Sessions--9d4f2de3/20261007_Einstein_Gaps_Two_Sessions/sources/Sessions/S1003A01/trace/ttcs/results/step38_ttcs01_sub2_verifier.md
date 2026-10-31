# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/step38_expmap_gn_response.py",
    "Sessions/S1003A01/workspace/notes/step38_curvature_conditioned_cap_response.md",
    "Sessions/S1003A01/workspace/notes/step37_cap_congruence_transport.md",
    "Sessions/S1003A01/workspace/data/step38/ch_band_gn1_fit32.json",
    "Sessions/S1003A01/workspace/data/step38/cap_band_gn1_cv.json",
    "Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md"
  ]
}
```

## Task

Read the Step-37 exponential-chart construction, the new Step-38 curvature-conditioned response method and records, and the peer Step-42/43 mathematical notes. Check the scientific and numerical substance: (i) whether the residual weighting and SVD whitening really implement the Gauss–Newton norm for D(Ric+g); (ii) whether the positive congruence response has first variation h; (iii) whether the paired control-variate comparisons support the stated narrow conclusions, including the CH control and coarse-fit overfitting; (iv) whether any interpretation improperly promotes the fixed-bolt cap experiment into a cap infimum or lower theorem; and (v) how the Taubes period obstruction and Cotton/quadratic law should alter the global research direction. Give precise corrections and the strongest supportable mathematical interpretation, not procedural advice.

## Output

# Verification memo: Step 37/38 cap-response construction and Step 42/43 global mechanisms

The five task items are answered in order in §1–§5. Text defects in the artifacts are in §6.

## 1. Residual weighting, the Gauss–Newton form, and the SVD whitening (item i)

**What the residual computes.** `tensor_residual` uses \(g=LL^T\) and \(A=L^{-1}EL^{-T}\) with \(E=\mathrm{Ric}+g\). The factors \(\sqrt2\) on off-diagonals and \(\sqrt{w\sqrt{\det g}/8\pi^2}\) give
\[
\|r\|^2=\sum_{\text{nodes}} w\,|E|_g^2\sqrt{\det g}/8\pi^2 ,
\]
since \(|E|_g^2=\mathrm{tr}(g^{-1}Eg^{-1}E)=\|A\|_F^2\). This is the correct quadrature of \(D/(8\pi^2)\). It also matches the data: the 32-node CH fit gives 0.68057, and the validated CH band integral is \(0.1961+0.3089+0.1729\approx0.6779\).

**The Gram form is \(J^TJ\), not exactly \(\int|D(\mathrm{Ric}+g)[h]|^2\).** Differentiating \(r(c)=W^{1/2}(c)\,\Phi_c(E(c))\), with \(\Phi_c=L^{-1}\cdot L^{-T}\), gives
\[
Jh=W^{1/2}\Phi_0(DE[h])+W^{1/2}(D\Phi[h])E+\tfrac14\mathrm{tr}(g_0^{-1}h)\,W^{1/2}\Phi_0(E).
\]
Only the first term is the stated \(D(\mathrm{Ric}+g)[h]\) norm. The other two are proportional to \(E\), and \(E\) is not small here: its band integral is about 0.68.

The middle term depends on the Cholesky convention. A pointwise frame rotation \(O(c)\) leaves \(|r|\) and the gradient \(J^Tr\) unchanged, but changes \(J^TJ\) by the cross terms \(J^TO^TdO\,r+\dots\), which are linear in \(r\). The Cholesky factor of an \(SU(2)\)-invariant metric in Cartesian \(\xi\) is not equivariant, so the Gram form carries a coordinate-ordering artefact of order \(|E||h|\).

The form that does implement the stated norm freezes \(\Phi\) and \(W\) at \(c=0\):
\[
\|h\|_{GN}^2=\textstyle\sum w_0\,|DE[h]|_{g_0}^2\sqrt{\det g_0}/8\pi^2 .
\]
The Step-38 note should either describe the form as "GN form of the weighted residual map" or use this frozen version.

**Gauge directions are not quotiented.** \(D\) is exactly invariant under compactly supported diffeomorphisms. At a base with \(E\neq0\), however, \(J(\mathcal L_Xg)=\mathcal L_XE+O(E)\neq0\). Gauge directions therefore get small but nonzero singular values, and \(T=V\Sigma^{-1}\) amplifies exactly these.

The data are consistent with this. In both runs the weakest singular direction is concentrated in the \((0,1)\) mode \(\mathrm{sym}(\theta_0\theta_1)\):
- CH: \(T_{1,10}=13.6\) with \(\sigma=0.073\).
- Cap: \(T_{1,10}=9.33\) with \(\sigma=0.107\).

In the coarse cap step, this direction produces the largest coefficient, \(c_{(0,1)}=0.131\). It does so even though it contributes only \(y_{10}^2=2\times10^{-4}\) of the predicted decrease of \(8.8\times10^{-3}\). Whether this direction is near-gauge is unresolved. It can be decided by projecting it onto \(\mathcal L_{f(r)v_k}g_0\).

**In the reported runs the whitening is mathematically inert.** With full rank (10 of 10 retained in both records) and an inactive clip (\(\max|y|=6\times10^{-4}\) and \(0.051\), both below 0.35), the step is
\[
c=T(-U^Tr_0)=-V\Sigma^{-1}U^Tr_0=-J^+r_0 .
\]
This is the ordinary minimum-norm Gauss–Newton step, which does not depend on parametrization. What changed relative to Step 37 is the switch from L-BFGS gradient iterations to a second-order least-squares model. Coefficient scaling was not repaired by whitening; whitening would matter only through `ybound`, the TRF trust region, or rank truncation.

The linear model is accurate on the fit nodes:
| run | predicted decrease \(\|U^Tr_0\|^2\) | in-sample nonlinear decrease |
|---|---|---|
| CH | \((6.60\times10^{-4})^2=4.36\times10^{-7}\) | \(0.68057087-0.68057045=4.26\times10^{-7}\) |
| cap (coarse) | \(8.76\times10^{-3}\) | \(9.92\times10^{-3}\) |

The line search is monotone up to \(\alpha=1\) in both runs; no \(\alpha>1\) was tested.

## 2. The congruence response (item ii)

With \(B=I+\tfrac12g_0^{-1}h\), and \((g_0^{-1}h)^T=hg_0^{-1}\), the metric is
\[
g(c)=B^Tg_0B=g_0+h+\tfrac14hg_0^{-1}h .
\]
- The first variation is exactly \(h\).
- The second-order term is positive semidefinite.
- \(g(c)>0\) if and only if \(-2\notin\mathrm{spec}(g_0^{-1}h)\).

The quadratic term enters the nonlinear line search, but not \(J\) at \(c=0\). The positivity statements in the script and note are correct.

## 3. Paired control-variate evidence (item iii)

### CH control

The numbers agree three ways:
- predicted decrease \(-4.4\times10^{-7}\);
- in-sample decrease \(-4.3\times10^{-7}\);
- validated change \((-5.9\pm9.1)\times10^{-7}\).

The validated uncertainty comes from four replicates (replicate standard deviation about \(1.8\times10^{-6}\)). The per-replicate i.i.d. standard error of \(3.6\times10^{-5}\) overstates scrambled-Sobol error about twentyfold, so the note is right to use replicate errors.

Per shell, the change is real but redistributive:

| shell | change | standard error |
|---|---|---|
| \(0.45<r<0.487\) | \(-3.08\times10^{-6}\) | \(3\times10^{-7}\) |
| middle shell | \(+7.6\times10^{-5}\) | — |
| outer shell | \(-7.3\times10^{-5}\) | — |

The net is zero within \(10^{-6}\).

**A symmetry fact sets how much this control can show.** The CH cell is diagonal, with radial coefficients, in the frame \(v_a\), where \(v_0=z\) and \(v_{1,2,3}\) are left multiplications by quaternion units. Left multiplications \(L_q\), \(q\in\{i,j,k\}\), satisfy \(dL_q(v_a)=v_{\mathrm{Ad}_qe_a}\), and \(\mathrm{Ad}_q\) flips the signs of two of the three vectors.

Consequences:
- Any diagonal radial metric is invariant under this Klein four-group. So is the CH background.
- The \(L_q\) map complex lines to complex lines, so they extend to the blow-up.
- Every off-diagonal product \(\theta_a\theta_b\) is odd under some element of the group.

By symmetric criticality, the first variation of \(D\) along the six off-diagonal modes is therefore exactly zero. The data agree: the GN step is dominated by \(c_{(0,0)}=-2.7\times10^{-4}\), with \(c_{(1,1)}=-3.4\times10^{-5}\). The only off-diagonal component above \(10^{-6}\) is \(c_{(0,1)}=1.9\times10^{-5}\), which is the amplified weakest direction responding to node and Cholesky asymmetry.

So the CH run tests four diagonal radial modes plus the pipeline. Two related statements need correcting:
- Step 37 §5.4 calls non-descent along 350 nonsymmetric modes "weak evidence of stationarity beyond the diagonal sector". First-order stationarity there is a theorem, not evidence.
- Second-order stability in symmetry-breaking directions is untested by every run so far. A GN form is positive semidefinite and cannot detect descending directions of the true Hessian \(J^TJ+\sum r_k\nabla^2r_k\), whose second term is \(O(|E|)\) here. The true 10×10 Hessian of the support cost is the object that would decide this.

### Coarse cap fit

The in-sample decrease agrees with the linear model (\(8.8\times10^{-3}\) predicted, \(9.9\times10^{-3}\) obtained). The off-sample reversal is therefore a spatial-sampling effect, not a nonlinear one: the fit used 12 nodes in total.

The mean validated response change, \(+0.0087\pm0.0011\) over three replicates, hides a localized structure:

| shell | replicate values | interpretation |
|---|---|---|
| \(0.45\)–\(0.597\) | \(-0.0116,\ -0.0111,\ -0.0114\) | real descent, about \(-0.0115\) |
| \(0.597\)–\(0.78\) | \(+0.0197,\ +0.0219,\ +0.0186\) | increase concentrated in the outer shell |

The GN direction is thus a genuine descent direction on the inner part of the switching band. It was undersampled in the outer fit shell, where four nodes covered \(0.62\)–\(0.78\). This is more informative than "the fit failed off-sample".

With \(t_2\), the 95% half-width on the net change is about \(\pm0.005\), so the sign of the net is established.

**Cap-minus-CH band excess.** The paired difference is \(0.059\pm0.007\) for the optimized cap; for the base cap it is \(0.059-0.0087\approx0.050\), consistent with Step 37's \(0.047\)–\(0.057\). The CH control variate works poorly here: replicate 23 gives shell-2 excess 0.027 against about 0.009 for the others. The base cap density in shell 2 varies by 5% across seeds, while CH varies by less than 1%. The anisotropic switching term has no counterpart in CH, so the CH cell cannot cancel it. The base-cap control (`imp`) is the one that works.

**Implementation details that affect reading.**
- The docstring identity \(D_{\rm cap}(c)=D_{\rm cert}+\int(F_{\rm cap}-F_{\rm CH})\) needs integration out to \(R_{\rm cell}=7.645\). The code integrates only over \([a,\max\text{support}]=[0.45,0.78]\), so its outputs are band partials, correctly named "partial".
- The records do not store `validate_nlog2` or `validate_nshell`. The edges show three shells, not the default 16.
- The records use `nstep=16`, against 64 in Step 37. Because JAX differentiates the discrete map \(\phi_h\) exactly, \(\phi_h^*g_C\) is still exactly Einstein wherever \(\phi_h\) is a local diffeomorphism. RK4 error therefore changes only the marking, at order \(h^4\), not the Einstein residual.

The refined 32-node cap record is not among the supplied files, so the four comparisons listed in Step-38 §3 remain unresolved.

## 4. Representation-theoretic reading of the cap experiment (item iv)

**Symmetry structure.** The cell is invariant under \(SU(2)_R\), the right multiplications. These preserve each \(v_a\), fix \(\Lambda^+\) pointwise, and act on \(\Lambda^-\) as \(SO(3)\). The frame products \(\theta_a\theta_b\) with radial coefficients, which make up the whole `nang=1` family, are \(SU(2)_R\)-invariant.

In the exponential chart,
\[
\delta G=g_C-g_{CH}=-\tfrac13W^-(\xi,\cdot,\xi,\cdot)+\dots
\]
Its terms linear in \(W^-,\dots,\nabla^3W^-\) carry \(SU(2)_R\) spins 2, 3/2, 5/2, …, and never spin 0. Schur's lemma then gives three consequences:

1. **The band excess is second order.** It equals \(D'(G_*)[\delta G]+\tfrac12H_*[\delta G,\delta G]+\dots\), and the first-order term vanishes. The same holds for the tail \(+0.010\). Both are dominated by \(\tfrac12H_*[\delta G,\delta G]\), with linear terms only from the invariant part of \(\nabla^4W^-\), as Step 37 §4 says.

2. **The `nang=1` family is blind to the environment at first order.** It has no first-order coupling to \(W^-\). The real inner descent of \(-0.0115\) is driven by spin-0 parts of \(\delta G\otimes\delta G\), which are sizeable because the switching band has \(|H''|\sim(b-a)^{-2}=16\). Positivity of any `nang=1` run says nothing about the sign of the environment effect.

3. **The relaxed second-order shift is a Schur complement.**
\[
Q=\tfrac12H_*[\delta G,\delta G]-\tfrac12\langle b,H_{\rm resp}^{-1}b\rangle,\qquad b=H_*[\cdot,\delta G],
\]
with \(b\) nonzero only in the \(SU(2)_R\) spin-2 isotypic sector. Those responses need degree-4 \(S^3\) harmonics, of type \((2,2)\), multiplying the frame products. Among the script's angular functions only \(c_2^2\) has such a component; \(c_2\), \(\mathrm{Re}\,w\) and \(\mathrm{Im}\,w\) are \((1,1)\). The relevant components are those invariant under the isotropy torus at \(p\).

So the fixed-deformation \(+0.010\) is the first term of \(Q\), not \(Q\) itself. Because \(H_*\) is indefinite away from Einstein (\(E\neq0\)), no sign of \(Q\) follows.

**Sentences that promote the experiment beyond what it shows.**
- Step 37 §4, "intrinsic tail interaction … its sign is positive", and §5.2, "the only intrinsic piece measured cleanly". Both should read: "second-order fixed-deformation term; its relaxation in the spin-2 sector is unmeasured."
- Step 37 §4, "neither has a sign that makes the cap favorable". This is unsupported.
- The Fermi-versus-exponential comparison. It compares two non-isometric metrics, because \(L\) is transported in different charts. The 0.74 is a real cost of a worse construction, not a representation error.

Step 38 §3's last paragraph and §5 bullet 2 are consistent with this analysis.

## 5. Global consequences of the Taubes and Cotton mechanisms (item v)

**Taubes dichotomy.** Lemma T and Corollaries T1–T2 are correct under \(b^+\ge2\) and basic classes \(\pm K_X+\sum\pm E_i\). The AKΓ algebra checks:
- \(G=[2\sigma^2+(3\delta-2\sigma)^2]/192\pi^2\);
- the Jensen value gives \(\ell^2\Gamma/(128\pi^2V)\);
- \(\min\Gamma=2/3\) at \(\theta=1/3\);
- Proposition G's \(\kappa/(\kappa+2)\);
- the \(\min_b\) formula of Step 43, \(\tfrac12a^2(1-c^2)(1+3c^2)\).

The exceptional-area term can be made explicit. Under \(H_L\), \(A[(1+\alpha)^2-1]=2A\alpha+A\alpha^2\) with \(\alpha=\sum a_i/\sqrt{2AV}\). At KE volume \(V=2\pi^2A\) (\(s=-4\)), this gives \(\alpha=\sum a_i/(2\pi A)\). The Taubes contribution to \(P/8\pi^2\) is then
\[
\Gamma(\theta)\Bigl[\textstyle\sum a_i/\pi+(\sum a_i)^2/(4\pi^2A)\Bigr],
\]
a per-class tariff of about \(\Gamma\,a_i/\pi\).

The two branches:
- **Almost-Kähler branch.** A diffuse mode must make every \(\omega\)-area \(a_i\ll\pi\). By monotonicity this forces concentration at scale \(\sqrt{a_i}\) around each \(J\)-sphere.
- **Zero branch.** The SD harmonic form has zeros or near-zeros. The certified cell sits here, with its form vanishing on the bolt.

The missing quantitative statement common to both branches is an ε-regularity bound on the \(\mathrm{Ric}^\circ\)-energy (not the \(W^-\)-energy) near a small-area \((-1)\)-sphere or a zero component. Burns-type scalar-flat Kähler bubbles saturate the Kähler unit. The certified cell shows the concentrated constant is not rigidly 1; its upper value is about 0.9957.

**The quadratic law is homogeneous.** Under degree-\(d\) covers, \(A\mapsto dA\), \(k\mapsto dk\) (spheres lift), and \(P\mapsto dP\). The Step-43 optimum
\[
P\ge\bigl(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\bigr)^2
\]
therefore gives a per-class coefficient
\[
\frac{P}{8\pi^2k}\ge f_\Lambda(t)=\frac{(\sqrt{\Lambda+8\pi^2t}-\sqrt\Lambda)^2}{8\pi^2t}\approx\frac{2\pi^2t}{\Lambda},\qquad t=k/A,
\]
which is invariant under covers. If \(\Lambda\) is cover-uniform, the per-class coefficient cannot tend to zero along covering towers. It can do so only as \(k/A\to0\).

This corrects the last paragraph of Step 43 §8. The "vanishing coefficient along towers" scenario requires either loss of cover-uniformity in \(\Lambda\) (through \(\|E\|\), \(\nabla a\), or zero-set terms) or \(k/A\to0\). It also separates the two programs by scale:
- Local cells and the cap work fix an \(A\)-independent concentrated constant, at most 0.9957.
- Diffuse modes can compete only in the small-\(k/A\) regime, where the quadratic law permits a cost of order \(k^2/A\).

**Weighted Cotton pairing (structural reasoning, not proved).** The exact identity \(\tfrac12\int a|\nabla n|^2=\dots\) already weights by \(a=\rho^2/4\). The left side is a fixed multiple of Theorem N's \(\mathcal N=\tfrac12\mathbb E\int\rho^2|\nabla n|^2\). The assumption \(a\ge a_0\) is needed only to pass to unweighted \(R\). Near zeros, \(\nabla n\sim1/\mathrm{dist}\), so a weighted test field \(aU\) moves the singularity into \(\nabla a\otimes U\) terms.

Taubes' zero branch and Step 43's \(\nabla a\) escape term are therefore the same object. A cover-uniform bound on \(\int|\nabla a||U|\) by noncircular quantities is the decisive missing estimate.

## 6. Artifact defects

- **Step 43 §6:** `\frac` was converted to form-feed plus "rac" (`rac S2`, `rac14`). The Kirchberg identity, including the sign-bearing \((S/2)|\nabla J|^2\) term, is unreadable as written.
- **Step 42 §3:** the saving 0.0043373 corresponds to \(c=0.9956627\). The certificate value is \(D/8\pi^2=0.9956700\), which would give a saving of 0.0043300. Since \(P\le D\), the note should say which of \(P\) or \(D\) is meant. The bound \(\kappa\le229.6\) depends on this choice.
- **Step 38 script:** the docstring control-variate identity describes a full-cell quantity that the code does not compute (see §3).