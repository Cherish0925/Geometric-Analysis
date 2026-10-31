# TTCS Independent Branch Record

```json
{
  "step_id": 23,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/angular_isotype_conformal.py",
    "Sessions/S1003A01/workspace/data/angular_isotype/j1_tf_conformal_r2p10_q160.json",
    "Sessions/S1003A01/workspace/data/angular_isotype/j1_tf_conformal_r4p12_q160.json",
    "Sessions/S1003A01/workspace/data/angular_isotype/j1_tf_conformal_r6p16_q192.json",
    "Sessions/S1003A01/workspace/notes/step23_scalar_relaxed_j1_CR_pinning_and_certification.md",
    "Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md"
  ]
}
```

## Task

Read the scalar-relaxed j=1 angular construction result as a geometric analyst. Check whether the conformal Schur-complement experiment, pure-trace redundancy repair, finite-basis interpretation, two-sided line tests, and conclusions are mathematically and numerically consistent. Identify any substantive error in formulas or interpretation, especially whether positivity of the finite blocks says only what the note says and whether an actual scalar-normalized construction would require further work. Ground the answer in the actual script, canonical JSON outputs, and synthesis note; give concrete repairs or next decisive computation if needed.

## Output

## Scientific verification memo

### Overall assessment

The script and the three canonical JSON files are internally consistent as a finite-dimensional \(j=1\) construction search. They establish the following numerical fact:

> For the sampled trace-free tensor spaces, the sampled conformal spaces, and the stated quadrature, the raw Hessian, the conformally relaxed Schur complement, and the sampled scalar-tangent subspaces all have strictly positive generalized Rayleigh minima.

The synthesis note correctly does **not** infer unrestricted local minimality or a positive lower spectral bound from these matrices. The sequence
\[
0.89575,\qquad 0.17823,\qquad 0.12095
\]
is decreasing as the radial tensor space grows, and the lowest order-four and order-six vectors have a strong gauge-like polarization. An actual \(s=-24\) path is also not produced by the finite conformal ansatz.

There is one formula-level error in a script comment, plus several interpretive points that should be sharpened.

---

## 1. Exact meaning of the conformal Schur complement

Let \(\bar g\) have \(s_{\bar g}=-24\), and consider endpoint-flat variations so that Chern–Gauss–Bonnet transgression terms vanish. In four dimensions,
\[
P(g)=2\int |W_g|^2\,dV_g+\frac1{12}\int s_g^2\,dV_g-\text{topological constant}.
\]
Hence
\[
J_6
=2\int |W|^2\,dV+\int f(s)\,dV-\text{constant},
\qquad
f(s)=\frac{s^2}{3}+12s+144.
\]

For a conformal variation \(\delta g=2\phi g\),
\[
D s[2\phi g]=-6\Delta\phi-2s\phi.
\]
A direct calculation gives
\[
D_{\mathrm{conf}}J_6(\phi)
=\int \phi\bigl[-4\Delta s+24(s+24)\bigr]\,dV.
\]
Thus this conformal derivative vanishes at \(s=-24\). If \(h\) is an arbitrary metric variation, define
\[
L=-6\Delta+48,\qquad A=-4\Delta+24.
\]
At \(s=-24\),
\[
D^2J_6(h,2\phi g)=\int \phi\,A\,Ds[h]\,dV,
\]
and
\[
D^2J_6(2v g,2\phi g)=\int \phi\,A L v\,dV.
\]
Consequently, minimizing the quadratic form over all conformal responses \(v\) yields
\[
A\bigl(Lv+Ds[h]\bigr)=0.
\]
Since \(A\) is positive and invertible on the decaying function space,
\[
Lv=-Ds[h].
\]

This verifies the main conceptual statement in the docstring: in a dense conformal space at an exactly scalar-normalized base, the Schur response converges to the linearized scalar-normalization response.

### Formula-level correction

The script comment

> “the mixed Hessian \(H_{ab}\) comes entirely from the scalar residual”

is incorrect if “scalar residual” means only
\[
\frac14\int(s+24)^2.
\]
That term contributes
\[
\frac12\int Ds[h]\,L\phi,
\]
whereas the \(P\)-term supplies an additional contribution. The full mixed block is the \(A\)-filtered scalar linearization above.

A precise replacement is:

> At an exact \(s=-24\) base, \(H_{\phi h}\) is the Galerkin matrix of \(A\,Ds[h]\), while \(H_{\phi\phi}\) is the Galerkin matrix of \(AL\). In the dense conformal-space limit, Schur minimization therefore solves \(Lv=-Ds[h]\).

This also sharpens the interpretation of `scalar_kernel`. In finite dimension,
\[
H_{\phi h}^{T}a=0
\]
means that \(A\,Ds[h_a]\) is orthogonal to the sampled conformal test space. It does not imply \(Ds[h_a]=0\) pointwise. The note's phrase “sampled scalar-kernel” is appropriate; the stronger script comment should be revised.

---

## 2. The base scalar residual is not quantified in the supplied outputs

The preceding identities are exact at \(s=-24\). The script describes the base as “nearly scalar-normalized,” but none of the JSON files reports
\[
\|s+24\|_{L^2},\qquad \|s+24\|_{L^\infty},
\]
or the corresponding radial profile.

The tiny first derivatives,
\[
\|\nabla_a J_6\|\sim 10^{-17},
\qquad
\|\nabla_b J_6\|\sim 10^{-18},
\]
do not establish scalar normalization. Every sampled first variation carries the mean-zero \(j=1\) factor \(F\), while the base first-variation density is orbit-invariant. Haar orthogonality already forces these derivatives to vanish.

Likewise, the agreement
\[
J_0=0.9951781866081983
\]
versus
\[
J_{\mathrm{stored}}=0.9951781866078961
\]
at \(160\) radial nodes, and the \(5.7\times10^{-13}\) agreement at \(192\) nodes, verifies objective normalization and radial integration of the base energy, not the size of \(s+24\).

A direct output of the scalar residual is therefore needed before the exact \(A\,Ds\) interpretation can be assigned a numerical error bar.

---

## 3. Pure-trace removal is geometrically correct

At first order,
\[
e^{2\phi}(g+h)
=g+h+2\phi g+O((h,\phi)^2).
\]
Every symmetric variation decomposes as
\[
k=k^\circ+\frac{\operatorname{tr}k}{4}g,
\]
and its trace component is represented conformally by
\[
\phi=\frac{\operatorname{tr}k}{8}.
\]
Thus including both an arbitrary pure-trace metric tensor and an independent conformal field produces a noninjective first-order parametrization. The observed near-zero branch with equal diagonal coefficients and compensating conformal coefficient is exactly the expected coordinate redundancy.

The repair in the code—six off-diagonal tensors plus three diagonal differences—is mathematically sound. Two textual details should be corrected:

1. The top docstring still says “all ten symmetric … tensors”; the code uses nine trace-free tensors.
2. These nine tensors are expressed in an orthonormal coframe, but they are not an orthonormal tensor basis. Each off-diagonal \(S_{AB}+S_{BA}\) has norm \(\sqrt2\), and the three diagonal differences are mutually nonorthogonal. This does not affect the generalized eigenvalues because the script explicitly assembles the Gram matrix \(G\).

There is also a finite-space subtlety: the trace-free metric functions use \(u^2(1-u)^3\), while conformal functions use \(u^2(1-u)^4\). Geometric trace redundancy is exact when both descriptions use the same function space. With the present envelopes, the conformal coordinate covers a somewhat smaller outer-endpoint class. This is harmless for removing the spurious duplicate parameter, but the resulting block is not a complete discretization of every trace perturbation allowed by the metric envelope.

---

## 4. Numerical consistency of the matrices and line tests

The numerical data are mutually consistent.

### Haar and base-energy calibration

All three files give
\[
\int F_i\,d\mu_{\mathrm{Haar}}\approx0,\qquad
\int F_iF_j\,d\mu_{\mathrm{Haar}}\approx\delta_{ij}
\]
to roughly \(2\times10^{-16}\). This verifies the normalization of the sampled triplet.

The base value agrees with the independently stored value to \(3.0\times10^{-13}\) at \(n_{qx}=160\) and \(5.7\times10^{-13}\) at \(n_{qx}=192\).

### Schur algebra

Every reported conformal block is positive definite:
\[
\lambda_{\min}(H_{\phi\phi})
=
1.98\times10^{-3},\ 
9.01\times10^{-4},\ 
2.51\times10^{-4}
\]
for the three runs. Therefore
\[
H_{\mathrm{rel}}
=H_{hh}-H_{h\phi}H_{\phi\phi}^{-1}H_{\phi h}
\]
is the correct finite-dimensional minimized quadratic form.

All generalized eigenvalues reported in the JSON files are positive. No Gram direction was discarded: the reported Gram ranks are \(18,36,54\), respectively.

### Two-sided paths

The finite-difference quotients accurately reproduce the AD Hessian. For example, at radial order six,
\[
\lambda_{\mathrm{rel}}=0.1209451284747587,
\]
while the \(\varepsilon=10^{-3}\) two-sided quotient is
\[
0.12094371082405075.
\]
Both \(J_6(+\varepsilon d)\) and \(J_6(-\varepsilon d)\) exceed \(J_0\). Similar agreement occurs at orders two and four. The drift at \(\varepsilon=1.25\times10^{-4}\) is ordinary subtraction loss: the energy increment is then around \(10^{-9}\).

These line tests verify the Taylor expansion of the same quadrature objective used to form the Hessian. They are not independent tests of the angular quadrature, curvature routine, or continuum functional.

### Conditioning

The basis becomes rapidly less well conditioned:
\[
\begin{array}{c|cc}
n_{\rm rad}&\kappa(G)&\kappa(H_{\phi\phi})\\ \hline
2&1.46\times10^2&5.08\times10^4\\
4&3.73\times10^4&1.89\times10^5\\
6&1.50\times10^6&1.76\times10^6 .
\end{array}
\]
Double precision is still adequate for the sign of \(0.1209\), particularly because the line quotient agrees, but this trend supports the note's proposal to replace global Chebyshev envelopes by localized, better-conditioned radial functions.

All canonical runs use `nqa=3`. The exact Haar Gram test is useful, but it does not by itself verify every derivative-tensor bilinear entering the Hessian. A fixed-block comparison at `nqa=4,5,6` would distinguish representation-theoretic exactness from angular aliasing. Likewise, the current files do not compare the same \(n_{\rm rad},n_\phi\) block at several radial quadratures.

---

## 5. The order-two interpretation needs a small correction

At order two,
\[
\lambda_{\rm raw}=0.8957495836205992,
\qquad
\lambda_{\rm scalar\ kernel}=0.8957495836206062.
\]
Thus the raw lowest vector already lies in the sampled coupling kernel, to numerical precision. After relaxation, another coupled vector becomes the new lowest vector at
\[
0.7499216166935329.
\]

Therefore the data do not show that the *same* eigenvector moved from \(0.89575\) to \(0.74992\). They show that the bottom of the ordered finite spectrum moved, most likely through eigenvalue reordering. The stored `lowest_metric_mode` is the relaxed vector, not the raw lowest vector.

A precise sentence is:

> At order two, scalar relaxation lowers a coupled branch enough to place it below the uncoupled raw ground branch, changing the bottom from \(0.89575\) to \(0.74992\).

Branch tracking would require the raw Rayleigh quotient of each relaxed eigenvector and overlaps between raw and relaxed eigenbases.

At orders four and six, the lowest vector itself is uncoupled:
\[
\lambda_{\rm raw}=\lambda_{\rm rel}=\lambda_{\rm scalar\ kernel}
\]
to about \(10^{-14}\), and its optimal conformal coefficients are around \(10^{-10}\) or smaller. That part of the note is fully supported.

Scalar relaxation still matters elsewhere in the low spectrum. It creates values \(0.2825\) at order four and \(0.14447\) at order six. The stored line tests at orders four and six follow the global lowest vector, whose conformal component is essentially zero, so they do not test these genuinely coupled low branches. A two-sided test of the most strongly lowered low eigenvector would be more informative about the conformal Schur block.

---

## 6. What finite-block positivity means

The note's principal finite-basis interpretation is correct:

- positivity holds for the sampled spaces and sampled objective;
- it supplies no positive continuum lower bound;
- adding tensor functions or conformal responses can lower the minimum;
- the decreasing sequence is compatible with convergence to zero;
- it says nothing definitive about the unrestricted metric space.

One further precision concerns the word “Ritz.” The script whitens \(H_{\mathrm{rel}}\) with the Gram matrix of the trace-free seed \(h\) only. The actual scalar-normalized tangent is
\[
\dot{\widehat g}=h+2vg.
\]
Since \(h\) is trace-free,
\[
\|\dot{\widehat g}\|_{L^2}^2
=\|h\|_{L^2}^2+16\|v\|_{L^2}^2.
\]
Thus the printed relaxed values are Rayleigh quotients relative to the trace-free seed norm, not the standard \(L^2\) norm of the full normalized metric variation. Their signs are unaffected, but they should not be described as eigenvalues of the full geometric Hessian without assembling the induced Gram matrix.

The lowest order-four and order-six eigenvectors provide an additional reason for geometric gauge projection. Reading the coefficient ordering from `OFFDIAG`, almost all their mass lies in the \((0,1)\) and \((2,3)\) tensor polarizations at every radial order. Such paired radial-angular and angular-angular components are typical of Lie-derivative sectors. This does not identify them as gauge vectors by itself, but it makes the observed drift toward zero especially suggestive. Explicit \(j=1\) vector fields \(X\) and their tensors \(\mathcal L_Xg\) would settle the point.

Because the base is not shown to be a full critical metric, an affine-path Hessian is not automatically the usual gauge-invariant Jacobi form: along a diffeomorphism flow,
\[
J_6(\Phi_t^*g)=J_6(g),
\]
but the second derivative contains both \(D^2J_6[\mathcal L_Xg,\mathcal L_Xg]\) and a term involving the second derivative of the pullback metric. This is exactly why the proposed Lie-derivative projection and Ward identities are mathematically important.

---

## 7. The finite conformal path is not an actual scalar normalization

For a perturbation \(q_t=g+t h+\cdots\), actual scalar normalization requires solving
\[
-6\Delta_{q_t}u_t+s_{q_t}u_t+24u_t^3=0,
\qquad u_t\to1,
\]
and setting
\[
\widehat g_t=u_t^2q_t.
\]
The script instead chooses a finite linear conformal response
\[
\phi_t=t\sum b_nV_n
\]
and evaluates \(J_6(e^{2\phi_t}(g+t h))\). It does not report
\[
s_{e^{2\phi_t}(g+t h)}+24,
\]
so these line-test metrics are not shown to lie on \(s=-24\).

There is also an outer-end issue. Both \(h\) and \(\phi\) are forced to vanish at \(x=X\), and are implicitly zero on the exact CH exterior. The true solution of
\[
Lv=-Ds[h]
\]
generally has a nonzero decaying homogeneous tail on that exterior. At fixed \(X\), increasing `nphi` within the envelope \(u^2(1-u)^4\) cannot reproduce that tail. Thus the “convergent-basis limit” statement needs either:

1. \(X\to\infty\) with the source kept in a fixed inner region, or
2. an exact CH exterior Dirichlet-to-Neumann form attached at \(x=X\), or
3. an explicit basis of decaying exterior solutions.

Finally, \(h=O((1-u)^3)\) gives only \(C^2\) contact with the zero extension, while \(\phi=O((1-u)^4)\) gives \(C^3\) contact. The curvature integral is meaningful for the sampled piecewise metric, but the smooth exact-CH-ended class used by the conformal theorem requires a \(C^\infty\) cutoff or a quantified smoothing argument.

---

## 8. Most decisive strengthening computation

The most informative continuation is a direct scalar-and-gauge reduced \(j=1\) radial calculation:

1. Assemble \(Ds[h]\) explicitly for every trace-free \(j=1\) tensor polarization.
2. Solve
   \[
   (-6\Delta+48)v=-Ds[h]
   \]
   with regular inner behavior and the exact decaying CH exterior response, preferably through an exterior Dirichlet-to-Neumann matrix.
3. Report
   \[
   \|Ds[h]+Lv\|_{L^2}
   \]
   for each low eigenvector, rather than inferring scalar tangency only from \(H_{\phi h}\).
4. Construct the \(j=1\) Lie-derivative tensors \(\mathcal L_Xg\), identify their overlap with the \((0,1)\)–\((2,3)\) low branch, and form a geometric slice.
5. Use localized radial functions and repeat fixed-block calculations across radial quadrature and angular quadrature orders.
6. For any resulting descending vector, solve the nonlinear scalar equation for several two-sided amplitudes and evaluate \(P(\widehat g_t)=J_6(\widehat g_t)\) independently.

That computation would distinguish three currently intertwined mechanisms: a genuine trace-free geometric mode, an approximated diffeomorphism direction, and an incompletely represented scalar-normalization response.

In summary, the finite-block data and line tests are numerically coherent, the pure-trace repair is correct, and the note appropriately treats the result as a finite construction search. The mixed-block explanation, order-two branch wording, full-metric normalization of the Rayleigh quotient, scalar-tail treatment, and direct verification of scalar normalization all require refinement before the experiment can be read as a geometric Hessian computation on the \(s=-24\) hypersurface.