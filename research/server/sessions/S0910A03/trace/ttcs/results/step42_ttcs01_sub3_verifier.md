# TTCS Independent Branch Record

```json
{
  "step_id": 42,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md",
    "Sessions/S0910A01/workspace/notes/step39_complete_conditional_defect_gap_theorem.md",
    "Sessions/S0910A03/workspace/notes/step29_terminal_density_bridge_lemma.md",
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Independently examine the terminal contradiction and the claimed full spectral calibration. There are two possible routes in the files: the explicit nonnegative LeBrun spectral density G=f²-(b_-)², and the positive-part rescaled-monopole harmonic form/eigenline density. Determine which route is actually sufficient once a smooth Einstein chart with s=-4 and |W+|²=1/24 is obtained. Verify algebraically that G=0 forces the calibrated spectrum under the stated eigenvalue ordering, and identify the regularity/convergence needed to pass ∫G→0 to the limit. In parallel, assess whether the positive-part monopole construction is proven in the session files or only generator/Codex-level material, and whether it should be removed from the load-bearing proof. Finally check the local Derdziński/projector contradiction constants and orientation. Ground the answer in the supplied files and do not assume weak W2p convergence passes curvature nonlinearities.

## Output

# Scientific verification memo

## 1. The \(G\)-density already supplies the full spectrum

A smooth Einstein chart satisfying only
\[
\operatorname{Ric}=-g,\qquad s=-4,\qquad |W^+|^2=\frac1{24}
\]
does not yet determine the eigenvalues of \(W^+\). The additional equation
\(\mathcal G=0\) does, and this equation is already present in the terminal density of A01 Step 28, equations (1.5)–(1.7), and A01 Step 39, equations (6.2)–(6.3). No harmonic form is needed for the terminal spectral step.

Let the ordered eigenvalues be
\[
\lambda_3\ge \lambda_2\ge w,\qquad
\lambda_3+\lambda_2+w=0,\qquad
u=|W^+|.
\]
Set
\[
\alpha=\sqrt{\frac23},\qquad
f=\frac23s-2\alpha u,\qquad
b=\frac23s+2w,\qquad
\xi=w+\alpha u.
\]
For every traceless symmetric endomorphism of a three-dimensional Euclidean space,
\[
u^2=w^2+\lambda_2^2+\lambda_3^2
\ge w^2+\frac{(\lambda_2+\lambda_3)^2}{2}
=\frac32w^2.
\]
Since \(w\le0\),
\[
-\alpha u\le w\le0,
\]
so \(\xi\ge0\).

At the calibrated values,
\[
u=\frac1{2\sqrt6},\qquad \alpha u=\frac16,
\]
and therefore
\[
0\le\xi\le\frac16,\qquad f=-3,\qquad b=f+2\xi=-3+2\xi.
\]
In particular \(b<0\), so with the file convention \(b_-=\min\{b,0\}\),
\[
\mathcal G=f^2-(b_-)^2
=9-(-3+2\xi)^2
=4\xi(3-\xi).
\]
Thus
\[
\mathcal G=0\quad\Longrightarrow\quad \xi=0
\quad\Longrightarrow\quad w=-\frac16.
\]
The other two eigenvalues then satisfy
\[
\lambda_2+\lambda_3=\frac16,
\qquad
\lambda_2^2+\lambda_3^2
=\frac1{24}-\frac1{36}
=\frac1{72}.
\]
Hence
\[
\lambda_2\lambda_3
=\frac{(1/6)^2-1/72}{2}
=\frac1{144},
\]
and the quadratic with roots \(\lambda_2,\lambda_3\) has zero discriminant. Therefore
\[
\boxed{\operatorname{spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).}
\]

This exactly confirms the algebra in A01 Step 8 §2. The interval
\(0\le\xi\le1/6\) also excludes the second formal root \(\xi=3\).

## 2. What convergence is actually needed

The terminal estimate gives
\[
\int_M\mathcal G_i\,d\mu_i\le 6Q_i(T),
\]
and the combined density satisfies
\[
\int_M\mathfrak D_i\,d\mu_i\le119Q_i(T).
\]
After exponential-pullback selection, \(A_\rho\mathfrak D_i(p_i)\to0\). Rauch comparison bounds the pullback-volume denominator above and below, so on the selected tangent ball
\[
\int \mathcal G_i\,d\mu_{\widehat g_i}\longrightarrow0.
\]

To identify this with \(\mathcal G(g_\infty)\), weak \(W^{2,p}\) metric convergence alone is insufficient. Curvature contains second derivatives, and \(\mathcal G\) is quadratic in scalar and Weyl curvature. In particular, the sentence in A01 Step 39 §7.2 that curvature eigenvalues are “Lipschitz in the metric coefficients” needs correction: eigenvalues are Lipschitz in the curvature endomorphism after the varying metric bundles have been identified.

Either of the following is enough on a smaller chart:

1. **Smooth convergence**, obtained from sequence-uniform positive-time curvature derivative estimates on a larger plateau buffer.

2. **Strong finite-\(W^{2,p}\) convergence**, together with strong \(C^1\) convergence and uniform ellipticity. Strong \(W^{2,2}_{\mathrm{loc}}\) already suffices for this density; taking \(p>2\) is cleaner.

Indeed, in common coordinates,
\[
\operatorname{Rm}(g_i)
=g_i^{-1}*\partial^2g_i
 +g_i^{-2}*\partial g_i*\partial g_i.
\]
Strong \(C^1\) and strong \(W^{2,2}\) convergence imply
\[
\operatorname{Rm}(g_i)\to\operatorname{Rm}(g_\infty)
\quad\text{strongly in }L^2_{\mathrm{loc}}.
\]
With fixed orientation, the Hodge projections onto \(\Lambda^+\) converge uniformly, hence
\[
s_i\to s_\infty,\qquad W_i^+\to W_\infty^+
\quad\text{strongly in }L^2.
\]
The norm and least-eigenvalue maps are Lipschitz on symmetric matrices, and \(x\mapsto\min\{x,0\}\) is \(1\)-Lipschitz. Consequently
\[
f_i\to f_\infty,\qquad (b_i)_-\to(b_\infty)_-
\quad\text{strongly in }L^2,
\]
and
\[
\mathcal G_i\to\mathcal G_\infty
\quad\text{strongly in }L^1.
\]
Thus \(\int\mathcal G_\infty=0\). Since the Einstein limit is smooth and \(\mathcal G_\infty\ge0\), one obtains \(\mathcal G_\infty=0\) everywhere.

The harmonic-coordinate argument in A01 Step 8 §5 supplies a suitable route to strong convergence. Once
\[
E_i=\operatorname{Ric}_{g_i}+g_i\to0
\quad\text{strongly in }L^2
\]
and \(g_i\to g_\infty\) in \(C^{1,\beta}\), the harmonic-coordinate Ricci equation
\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=-2(\operatorname{Ric}_{g_i})_{jk}
 +Q_{jk}(g_i^{-1},\partial g_i)
\]
has a strongly convergent right-hand side. Interior elliptic estimates for the difference equation then give strong \(W^{2,2}\) convergence after shrinking the chart. Uniform curvature bounds and interpolation give strong \(W^{2,p}\) for any desired finite \(p\).

There is also a small geometric repair between A01 Steps 28 and 39. Step 28 correctly requires that every radius-\(\rho\) geodesic from a selected center remain inside the bounded-curvature buffer. Step 39 averages over all of \(B_{2r}(x_\alpha)\), while its displayed curvature estimate is only stated on that same set. Centers near its edge do not automatically have the required buffer. One can instead average over \(B_r(x_\alpha)\), retain a fixed fraction of the total plateau volume by Bishop–Gromov comparison, and choose \(\rho<r\); then all sampled geodesics remain in \(B_{2r}(x_\alpha)\).

## 3. Positive-part monopole route

The finite-dimensional endpoint of this route is mathematically sufficient if all its analytic inputs are available. Define
\[
\mathscr A=W^++\sqrt{\frac23}|W^+|I.
\]
The sharp eigenvalue estimate above shows \(\mathscr A\) is positive semidefinite. If a smooth limiting harmonic form satisfies
\[
H_\infty\ne0,\qquad
\langle\mathscr A_\infty H_\infty,H_\infty\rangle=0,
\]
then \(\mathscr A_\infty H_\infty=0\), so
\[
W_\infty^+H_\infty
=-\sqrt{\frac23}|W_\infty^+|H_\infty
=-\frac16H_\infty.
\]
Trace and norm then force the other two eigenvalues to be \(1/12,1/12\). Thus the endpoint algebra is sound. The terminology “projector” in A03 Step 29 is imprecise: \(\mathscr A\) is a positive semidefinite endomorphism, becoming a scalar multiple of the complementary projection only after the calibrated spectrum is known.

Within the supplied record, however, the positive-part construction does not have the same derivational support as the \(G\)-route:

- A03 `quantitative_deficit_analysis.md` gives a detailed formal decomposition, but identities (5) and (9) are asserted as the result of retaining all terms in the rescaled Seiberg–Witten argument rather than derived line by line from a cited source passage.
- A03 Step 16 explicitly states that its script verifies finite-dimensional algebra only, not the rescaled Seiberg–Witten existence input or the analytic chart passage.
- A03 Step 29 depends on a generator trace and the Codex note for the positive-weight construction.
- The regularization \(f^2\approx q^++\varepsilon\), existence of a suitable rescaled monopole for each regularized weight, uniform estimates, and diagonal selection are described but not assembled into a self-contained theorem in the supplied files.
- Step 29 states eigenline control on the bounded-curvature set \(P\), while exponential averaging samples the union of radius-\(\rho\) neighborhoods of \(P\). The estimate must be formulated on that entire buffered union.
- Its displayed selection estimate is derived as
  \[
  A_\rho\mathfrak D(p)\le C\,\frac QA,
  \]
  whereas the lemma statement phrases it as \(C\varepsilon\) from
  \(Q/(8\pi^2)\le\varepsilon\). The \(Q/A\) normalization is the quantity actually used by the sequence argument.
- Passing the eigenline term to the chart also requires strong local convergence of \(H_i\), obtained from local \(L^2\) control and interior Hodge estimates after smooth metric convergence.

Accordingly, the load-bearing terminal argument is already complete at the scientific level with
\[
\int\mathcal G_i\to0
\quad+\quad
\text{strong curvature convergence}.
\]
The positive-part monopole density is best viewed as an auxiliary refinement rather than an essential dependency of the spectral contradiction. A01 Step 39 in fact uses the \(G\)-route and does not need the additional harmonic-form terms.

## 4. Derdziński and projector constants

Once the spectrum has been established,
\[
s=-4,\qquad
|W^+|^2=\frac1{24},\qquad
\operatorname{spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right),
\]
all local constants in A01 Step 8 and A03 Step 6 are consistent.

Because the metric is Einstein,
\[
\delta W^+=0.
\]
Derdziński Proposition 5, as recorded from the primary 1983 source in A01 Step 8 §1, gives the locally Kähler metric
\[
\widehat g=(24|W^+|^2)^{1/3}g.
\]
Here the factor equals \(1\), so \(g\) itself is locally Kähler. The source statement gives the Kähler orientation as the prescribed orientation, which is essential because the calibrated tensor is \(W^+\).

For a Kähler surface in its complex orientation,
\[
\operatorname{spec}(W^+)
=\left(\frac s6,-\frac s{12},-\frac s{12}\right).
\]
At \(s=-4\),
\[
\operatorname{spec}(W^+)
=\left(-\frac23,\frac13,\frac13\right),
\qquad
|W^+|^2=\frac{s^2}{24}=\frac23,
\]
contradicting \(|W^+|^2=1/24\).

The direct projector calculation is also consistent. Constant distinct simple/double eigenvalues and \(\delta W^+=0\) give
\[
(\nabla^a\omega_{ab})\omega_{cd}
+\omega_{ab}\nabla^a\omega_{cd}=0.
\]
Contraction with \(\omega^{cd}\) gives \(d^*\omega=0\); substitution then gives
\[
\omega_{ab}\nabla^a\omega_{cd}=0.
\]
A nonzero self-dual two-form in four dimensions is nondegenerate, so
\(\nabla\omega=0\), hence \(\nabla W^+=0\).

Finally,
\[
\det W^+
=\left(-\frac16\right)\left(\frac1{12}\right)^2
=-\frac1{864}.
\]
The Einstein–Weyl scalar identity
\[
\Delta|W^+|^2
=2|\nabla W^+|^2+s|W^+|^2-36\det W^+
\]
therefore yields, since \(|W^+|\) is constant,
\[
0
=2|\nabla W^+|^2-\frac16+\frac1{24}
=2|\nabla W^+|^2-\frac18,
\]
so
\[
|\nabla W^+|^2=\frac1{16},
\]
contradicting \(\nabla W^+=0\).

Thus both local contradictions have the correct constants and orientation. The scientifically decisive terminal chain is:

\[
\text{terminal }\int\mathcal G_i\to0
\;\Longrightarrow\;
\text{strong curvature passage}
\;\Longrightarrow\;
\operatorname{spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right)
\;\Longrightarrow\;
\text{Derdziński/projector contradiction}.
\]