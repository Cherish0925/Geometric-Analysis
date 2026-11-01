# TTCS Independent Branch Record

```json
{
  "step_id": 42,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step39_complete_conditional_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step41_continuation_criterion_and_first_exit_assembly.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md",
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Critically verify and repair the connected first-exit and terminal-chart proof for the near-critical Ishida–LeBrun negative four-dimensional route. Focus on three exact interfaces raised by the strategist. (1) A01's first-exit equation (4.13) contains an additive C0*T term that may dominate a shrinking support energy. Determine from the index-level curvature identity whether the correct q=2 inequality is homogeneous relative to K2=∫η²(1+|Rm|²), or whether a nonhomogeneous term remains; give a precise relative self-improvement estimate valid componentwise under collapse. (2) Determine whether the support construction needs a sequence-uniform Hessian bound for χ. Use the signed Hessian-a integration mechanism and distinguish zero-order smoothing estimates from per-datum continuation. (3) Repair the terminal chart passage: give a precise buffered-center construction and a rigorous route from positive-time plateau estimates to strong curvature convergence on exponential pullback charts. Check whether standard interior normalized Ricci-flow derivative estimates apply when χ=1 on a larger plateau, and state required radius/time margins. Also identify any remaining load-bearing issue in passing the explicit spectral density G to the limit. Do not accept either note's theorem status; reason from the equations and files.

## Output

# Scientific verification memo

## Main findings

1. The \(q=2\) curvature energy inequality is homogeneous in
   \[
   K_{2,\alpha}(t)=\int \eta_\alpha^2(1+|\operatorname{Rm}|^2)\,d\mu_t.
   \]
   The additive \(C_0T\) in A01 equation (4.13) is an artifact of estimating a local volume by an absolute constant. With \(F^2=1+|\operatorname{Rm}|^2\), every such term is bounded by \(C(1+r^{-2})K_{2,\alpha}\). This gives a componentwise multiplicative estimate that remains valid when the component volume tends to zero.

2. A sequence-uniform pointwise Hessian estimate for \(\chi_\alpha\) is neither supplied by the Ricci lower bound nor needed for the smoothing estimates. The signed Hessian-\(a\) integration by parts uses only \(|d\chi_\alpha|\le C/r\). Higher cutoff jets enter only the per-datum continuation argument.

3. The terminal chart argument needs nested plateau radii. Taking all of \(B_{2r}(x_\alpha)\) as centers while assuming only \(\chi_\alpha=1\) there leaves no spatial margin. A construction with centers in \(B_r\), \(\chi_\alpha=1\) on \(B_{4r}\), and \(\operatorname{supp}\chi_\alpha\subset B_{5r}\) supplies a uniform parabolic cylinder. On that cylinder the equation is exactly normalized Ricci flow, so local Shi estimates apply on \([T/2,T]\). They yield sequence-uniform curvature derivative estimates and hence smooth convergence of the exponential pullback metrics after shrinking the tangent ball.

4. The explicit spectral density \(G\) passes continuously under this smooth curvature convergence, despite eigenvalue multiplicity. What does not suffice is A01’s stated \(C^{1,\alpha}\) plus weak \(W^{2,p}\) convergence. The terminal integral estimate for \(G\), and the sign of \(q_i=k_i-A_i/3\), must also be recorded correctly.

---

## 1. Correct componentwise \(q=2\) estimate

Write
\[
a=\chi^2,\qquad E=\operatorname{Ric}+g,\qquad
F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]
Let \(\eta\equiv1\) on a neighborhood of \(\operatorname{supp}a\), with \(a=da=0\) near \(\operatorname{supp}d\eta\). Set
\[
K_2=\int\eta^2F^2\,d\mu,\qquad
D_2=\int\eta^2a|\nabla\operatorname{Rm}|^2\,d\mu,\qquad
Y=\int\eta^2aF^3\,d\mu.
\]

### 1.1 Terms from the index-level identity

The supplied tensor computation gives the structural equation
\[
\partial_t|\operatorname{Rm}|^2
=a\Delta|\operatorname{Rm}|^2
-2a|\nabla\operatorname{Rm}|^2
+da*\operatorname{Rm}*\nabla E
+(\nabla^2a)_{pq}B_{\rm curv}^{pq}
+O(aF^3),
\]
where
\[
B_{\rm curv}^{pq}=R^p{}_j{}^q{}_lE^{jl},
\]
and
\[
|B_{\rm curv}|\le CF^2,\qquad
|\nabla B_{\rm curv}|\le CF|\nabla\operatorname{Rm}|.
\]

The Hessian term is retained with its tensor placement:
\[
\int\eta^2(\nabla_p\nabla_qa)B_{\rm curv}^{pq}
=-\int \nabla_qa\,\nabla_p(\eta^2B_{\rm curv}^{pq}).
\]
The \(d\eta\) contribution vanishes by the stationary collar. Using
\[
\frac{|da|^2}{a}=4|d\chi|^2\le Cr^{-2},
\]
one obtains
\[
\left|\int\eta^2(\nabla^2a):B_{\rm curv}\right|
\le \varepsilon D_2+C_\varepsilon r^{-2}K_2.
\]
The \(da*\operatorname{Rm}*\nabla E\) terms and the \(da\)-term arising from integration of \(a\Delta|\operatorname{Rm}|^2\) have the same estimate.

The volume form evolves by
\[
\partial_td\mu=-a\,\operatorname{tr}E\,d\mu.
\]
Since \(|\operatorname{tr}E|\le CF\),
\[
\left|\int\eta^2F^2\,\partial_td\mu\right|
\le C\int\eta^2aF^3=C Y.
\]
The inverse-metric and normalization contributions are also bounded by \(CaF^3\), as verified by the scaling calculation in Step 35.

Consequently,
\[
\boxed{
K_2'+cD_2
\le CY+C(1+r^{-2})K_2.}
\tag{1.1}
\]
For \(r\le1\), the last coefficient can be written \(Cr^{-2}\).

There is no additive term independent of \(K_2\). Spatially varying conformal scaling can create curvature in a flat transition region, but the resulting contribution is proportional to the local volume. The constant \(1\) in \(F^2\) records precisely that volume.

### 1.2 Absorption of \(Y\)

The relative Sobolev inequality is
\[
\|u\|_4^2\le\mathcal S
\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right).
\]
Because \(\eta=1\) on \(\operatorname{supp}\chi\),
\[
Y=\int(\eta F)(\chi F)^2
\le K_2^{1/2}\|\chi F\|_4^2.
\]
Hence
\[
Y\le C\mathcal S K_2^{1/2}
       (D_2+r^{-2}K_2)
=C\gamma(D_2+r^{-2}K_2),
\qquad
\gamma=\mathcal S K_2^{1/2}.
\tag{1.2}
\]
If \(C\gamma\le c/2\), equations (1.1)–(1.2) give
\[
\boxed{
K_2'+\frac c2D_2
\le C(1+r^{-2})K_2.}
\tag{1.3}
\]

### 1.3 Relative self-improvement under collapse

For every component \(\alpha\),
\[
K_{2,\alpha}(t)
\le
\exp\!\bigl(C(1+r^{-2})t\bigr)K_{2,\alpha}(0).
\]
At \(t\le\theta r^2\),
\[
\boxed{
\frac{K_{2,\alpha}(t)}{K_{2,\alpha}(0)}
\le
\exp\!\bigl(C\theta(1+r^2)\bigr)
\le
\exp\!\bigl(C\theta(1+r_0^2)\bigr).}
\tag{1.4}
\]
Thus a choice such as
\[
C\theta(1+r_0^2)<\log(3/2)
\]
gives
\[
K_{2,\alpha}(t)<\frac32K_{2,\alpha}(0)<2K_{2,\alpha}(0)
\]
simultaneously for all components. The estimate controls the ratio and is unaffected when \(K_{2,\alpha}(0)\to0\).

For the initial smallness of \(\gamma_\alpha\), the maximal-function construction must control the whole \(\eta_\alpha\)-support, not merely \(B_r(x_\alpha)\). Taking the maximal radius \(R\ge7r\) gives
\[
K_{2,\alpha}(0)
\le C\bigl(1+\Lambda\overline K_0\bigr)
       \operatorname{Vol}B_{7r}(x_\alpha),
\]
while the relative Sobolev estimate gives
\[
\mathcal S_{\alpha}(0)
\le
C\frac{r^2}{\operatorname{Vol}(B_{7r}(x_\alpha))^{1/2}}.
\]
Therefore
\[
\gamma_\alpha(0)
\le Cr^2\bigl(1+\Lambda\overline K_0\bigr)^{1/2},
\]
with complete cancellation of the local volume factor.

For a common terminal metric, all macro-components must be flowed simultaneously. Since the \(B_{7r}(x_\alpha)\) are disjoint, one may set
\[
\chi_{\rm tot}=\sum_\alpha\chi_\alpha,\qquad
a=\chi_{\rm tot}^2=\sum_\alpha\chi_\alpha^2.
\]
Every componentwise calculation above then remains unchanged.

---

## 2. Cutoff Hessians: smoothing versus continuation

### 2.1 What the support geometry actually supplies

A Ricci lower bound and local doubling do not by themselves furnish
\[
|\nabla^2\chi_\alpha|\le Cr^{-2}
\]
with a sequence-uniform constant. The corresponding sentence in Lemma 3.1(a) is unsupported by the stated geometric hypotheses.

The support construction can instead use:

\[
\chi_\alpha=1\ \text{on }B_{4r}(x_\alpha),\qquad
\operatorname{supp}\chi_\alpha\subset B_{5r}(x_\alpha),\qquad
|d\chi_\alpha|\le C/r,
\tag{2.1}
\]
and
\[
\eta_\alpha=1\ \text{on }B_{6r}(x_\alpha),\qquad
\operatorname{supp}\eta_\alpha\subset B_{7r}(x_\alpha).
\tag{2.2}
\]
A Lipschitz distance cutoff followed by smooth Lipschitz approximation gives (2.1), with all higher derivatives finite for each individual smooth metric.

### 2.2 Why no uniform Hessian enters the smoothing estimates

For curvature, the tensor
\[
B_{\rm curv}=\operatorname{Rm}*E
\]
has
\[
|B_{\rm curv}|\le CF^2,\qquad
|\nabla B_{\rm curv}|\le CF|\nabla\operatorname{Rm}|.
\]
For the defect,
\[
B_{\rm def}^{pq}
=|E|^2g^{pq}+(\operatorname{tr}E)E^{pq}-2(E^2)^{pq},
\]
with
\[
|B_{\rm def}|\le C|E|^2,\qquad
|\nabla B_{\rm def}|\le C|E||\nabla E|.
\]
In both cases, one derivative is integrated from \(\nabla^2a\), and every resulting term is controlled by \(|da|^2/a=4|d\chi|^2\). This covers:

- the \(q=2\) curvature seed;
- the fixed and general \(p\) curvature inequalities;
- the \(J_6\) defect seed;
- the general \(p\) defect inequalities.

Thus the sequence-uniform parabolic estimates use only the gradient estimate in (2.1) and the stationary collar in (2.2).

### 2.3 Role of higher cutoff jets

The staggered continuation mechanism involves \(\nabla^m\chi\) for arbitrarily large \(m\). These constants may depend on the individual metric and cutoff. That is sufficient for extending one smooth flow, because continuation only needs finiteness on each datum.

This distinction is essential:

- sequence-uniform zero-order smoothing: gradient-only cutoff control;
- per-datum smooth extension: finite higher cutoff jets;
- sequence-uniform terminal regularity: obtained independently from local Ricci-flow estimates inside the plateau.

The supplied files refer to a transported-coefficient DeTurck theorem but do not contain its full proof. Accordingly, start and restart remain external analytic inputs in the material provided here.

---

## 3. Buffered terminal centers and interior Ricci-flow regularity

### 3.1 Nested support geometry

Use the radii in (2.1)–(2.2) and define
\[
P_\alpha=B_{g_0}(x_\alpha,r).
\]
The original volume estimate for \(B_{2r}(x_\alpha)\), together with Bishop–Gromov comparison, gives
\[
\operatorname{Vol}_{g_0}P_\alpha
\ge c_{\rm BG}\operatorname{Vol}_{g_0}B_{2r}(x_\alpha).
\]
Hence
\[
\sum_\alpha\operatorname{Vol}_{g_0}P_\alpha
\ge\alpha_1A_i
\tag{3.1}
\]
for a sequence-uniform \(\alpha_1>0\).

Suppose the first-exit estimate gives
\[
e^{-\Lambda}g_0\le g(t)\le e^\Lambda g_0,
\qquad 0\le t\le T,\qquad T=\theta r^2.
\tag{3.2}
\]
Then
\[
\operatorname{Vol}_{g(T)}
\Bigl(\bigcup_\alpha P_\alpha\Bigr)
\ge e^{-2\Lambda}\alpha_1A_i
\tag{3.3}
\]
in dimension four.

For \(p\in P_\alpha\), set
\[
R=\frac12e^{-\Lambda/2}r.
\tag{3.4}
\]
If \(q\in B_{g(t)}(p,2R)\), then
\[
d_{g_0}(p,q)\le e^{\Lambda/2}2R=r,
\]
and therefore
\[
d_{g_0}(x_\alpha,q)<2r.
\]
Thus
\[
B_{g(t)}(p,2R)\subset B_{g_0}(x_\alpha,2r)
\subset\{\chi_\alpha=1\}
\tag{3.5}
\]
for every \(t\in[0,T]\). This is the required spatial margin.

### 3.2 Curvature bound on a positive-time cylinder

On the region in (3.5), \(a=1\), so
\[
\partial_tg=-2(\operatorname{Ric}+g).
\tag{3.6}
\]
The weighted Moser estimate gives, for \(t\in[T/2,T]\),
\[
|\operatorname{Rm}|(t)
\le K_*,
\qquad
K_*=C\left(1+\frac{\gamma_*}{T}\right),
\tag{3.7}
\]
throughout \(B_{g(t)}(p,2R)\).

Equation (3.6) is converted to ordinary Ricci flow by
\[
\bar g(t)=e^{2(t-T/2)}g(t),
\qquad
\frac{ds}{dt}=e^{2(t-T/2)}.
\]
Then
\[
\partial_s\bar g=-2\operatorname{Ric}_{\bar g}.
\]
The scaling factors are uniformly bounded on \([T/2,T]\). Local Shi estimates therefore apply inside the cylinder (3.5), independently of the transition region outside it.

After shrinking from radius \(2R\) to \(R\), one obtains
\[
\boxed{
\sup_{B_{g(T)}(p,R)}
|\nabla^m\operatorname{Rm}|(T)
\le
C_mK_*
\left(1+K_*+R^{-2}+T^{-1}\right)^{m/2}}
\tag{3.8}
\]
for every \(m\ge0\). Here \(R\simeq r\) and \(T=\theta r^2\), so all constants are sequence-uniform once \(r,\theta,\Lambda,\gamma_*\) are fixed. Taking \(\theta\) small also ensures \(T/2\lesssim R^2\).

No finite-propagation statement is being used. The local derivative estimate uses only that the normalized Ricci-flow equation and the curvature bound hold on the larger spacetime cylinder.

### 3.3 Exponential pullback charts

Choose
\[
0<\rho<
\min\left\{\frac R8,\frac{\pi}{4\sqrt{K_*}}\right\}.
\tag{3.9}
\]
Then every terminal radial geodesic of length \(2\rho\) from \(p\in P_\alpha\) stays in the derivative-controlled plateau, and there are no radial conjugate points.

Apply the exponential averaging lemma to the terminal density \(\mathfrak D_i\). From (3.3) and \(\int\mathfrak D_i=o(A_i)\), there is \(p_i\in\bigcup_\alpha P_\alpha\) such that
\[
\frac{
\int_{B_\rho(0)}
\mathfrak D_i(\exp_{p_i}v)\,d\mu_{h_i}(v)}
{\operatorname{Vol}_{h_i}B_\rho(0)}
\longrightarrow0,
\qquad
h_i=(\exp_{p_i}^{g_i(T)})^*g_i(T).
\tag{3.10}
\]
The measure here is the pullback Riemannian measure, not unweighted Euclidean measure.

Choose oriented terminal orthonormal frames to identify \(T_{p_i}M_i\) with \(\mathbb R^4\). Rauch comparison gives uniform ellipticity of \(h_i\) on \(B_{2\rho}(0)\). Equation (3.8), pulled back to this ball, gives uniform bounds for all covariant curvature derivatives. The Jacobi-field equations in normal coordinates then give uniform \(C^k\) bounds for the metric coefficients for every \(k\). After shrinking to \(B_\rho(0)\),
\[
h_i\longrightarrow h_\infty
\quad\text{smoothly}.
\tag{3.11}
\]
Self-overlap of the exponential map in the base manifold is harmless: \(h_i\) is defined on the tangent ball, and absence of radial conjugacy makes it a smooth Riemannian metric there.

This repairs the mathematically incorrect sentence in A01 §7.2 that curvature eigenvalues are “Lipschitz in the metric coefficients” under \(C^{1,\alpha}\) plus weak \(W^{2,p}\) convergence. Curvature depends on second derivatives. The strong curvature convergence supplied by (3.8)–(3.11) is the needed input.

---

## 4. Passage of the spectral density \(G\)

Let \(w\) be the least eigenvalue of \(W^+\), and define
\[
f=\frac23s-2\sqrt{\frac23}|W^+|,
\qquad
b=\frac23s+2w,
\qquad
G=f^2-(b_-)^2,
\quad b_-=\max\{-b,0\}.
\]

For a trace-free symmetric endomorphism of a three-dimensional space,
\[
w\ge-\sqrt{\frac23}|W^+|.
\]
Indeed, if the other eigenvalues are \(\alpha,\beta\), then
\[
\alpha+\beta=-w,\qquad
\alpha^2+\beta^2\ge\frac12w^2,
\]
so
\[
|W^+|^2\ge\frac32w^2.
\]
It follows that \(b\ge f\), and therefore \(G\ge0\).

The least eigenvalue is Lipschitz in the curvature operator, and \(x\mapsto x_-\) is Lipschitz. Under (3.11),
\[
G_i\longrightarrow G_\infty
\quad\text{uniformly on compact subballs}.
\]
Equation (3.10) then implies \(G_\infty\equiv0\).

The other density components give
\[
s_\infty=-4,\qquad
|W_\infty^+|=\frac1{2\sqrt6}.
\]
Hence \(f_\infty=-3\). Since \(G_\infty=0\),
\[
(b_\infty)_-=3,
\]
and \(b_\infty\ge f_\infty=-3\) forces \(b_\infty=-3\). Thus
\[
w_\infty=-\frac16.
\]
Trace zero and \(|W_\infty^+|^2=1/24\) then force the remaining two eigenvalues to be equal:
\[
\operatorname{spec}(W_\infty^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

### Terminal topological correction

The displayed bound
\[
\int\mathfrak D_i\le119Q_i(T)
\]
uses \(q_i=k_i-A_i/3\ge0\). The theorem statement in A01 assumes only \(k_i/A_i\to1/3\), so this sign is not explicit.

For the terminal sign class with
\[
(a_i^+)^2-A_i\ge0,
\]
the exact formula gives
\[
D_{a_i}
\le J_i+(-q_i)_+,
\qquad
(-q_i)_+=\max\{-q_i,0\}.
\]
Since
\[
\int\mathfrak D_i
\le5Q_i(T)+912\pi^2D_{a_i},
\qquad
J_i\le\frac{Q_i(T)}{8\pi^2},
\]
the general estimate is
\[
\boxed{
\int\mathfrak D_i
\le119Q_i(T)+912\pi^2(-q_i)_+.}
\tag{4.1}
\]
The near-critical assumption gives \(q_i/A_i\to0\), so (4.1) still yields
\[
A_i^{-1}\int\mathfrak D_i\to0.
\]
A bound purely by \(Q_i(T)\) requires \(q_i\ge0\).

Finally, the supplied files state
\[
\int G_i\le48\pi^2D_{a_i}
\]
but do not reproduce its full Seiberg–Witten algebra. The pointwise properties and the passage to the smooth limit are verified above; the integrated estimate remains a substantive imported lemma. Together with the transported-coefficient start/restart theorem, this is mathematical content not proved in the displayed files.