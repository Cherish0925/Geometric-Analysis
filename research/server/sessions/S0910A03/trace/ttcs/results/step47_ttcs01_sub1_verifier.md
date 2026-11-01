# TTCS Independent Branch Record

```json
{
  "step_id": 47,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step47_consolidated_negative_IL_gap_theorem.md",
    "Sessions/S0910A03/workspace/notes/step43_terminal_density_G_lemma.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Verify the logical chain of the consolidated restricted negative IL gap theorem in the provided file. Focus on these five load-bearing points:

1. COLLAPSE CANCELLATION (§3d): The claim is that on a good ball where the volume-averaging maximal function satisfies M_vol(|Rm|²)(x) ≤ κ², the initial curvature energy satisfies K₂ ≤ (1+κ²)Vol(B), and the Sobolev constant S ≤ Cr²/√Vol(B). Therefore γ = S·K₂^{1/2} ≤ Cr²√(1+κ²), independent of Vol. Check: is this computation correct? Does the volume-averaging Hardy-Littlewood maximal inequality hold under Ric ≥ -3g with the stated constants? Is the Maheux-Saloff-Coste Sobolev inequality correctly stated?

2. TERMINAL POINT SELECTION (§7b-7c): The claim is that min_{x∈Π} D(x,T) ≤ (119C₁/α)δ² → 0, and then a subsequence of pullback metrics on B_R(0) ⊂ R⁴ converges C^∞ to an Einstein limit with D_h(0) = 0. Check: is the minimum-of-average-gives-small-minimum argument correct? Does the pullback chart have noncollapsed volume (Rauch comparison under bounded curvature)? Does C^k convergence pass D to the limit?

3. SPECTRAL DETERMINATION (§7d): From D_h(0)=0 on the Einstein limit with s=-4, the claim is |W⁺|² = 1/24 and G = 0, forcing Spec(W⁺) = (-1/6,1/12,1/12). Check the algebra: G = 4ξ(3-ξ) where ξ = w + √(2/3)|W⁺|, so G=0 forces ξ=0, hence w=-1/6.

4. PROJECTOR-BOCHNER (§7e): The claim is that on any connected Einstein 4-manifold with Ric=-g and W⁺ spectrum (-1/6,1/12,1/12) at one point, the simple eigenform is parallel (from δW⁺=0 + constant eigenvalue), so ∇W⁺=0 and |W⁺|²=const, and then the Bochner identity gives 0 = -1/8, a pointwise contradiction. Check: is the projector argument correct for a LOCAL domain (not just closed manifolds)?

5. SELF-IMPROVING FIRST-EXIT (§5h): The drift estimate d(T) ≤ Cδθ^{2/3}r² is used to keep Sobolev constants comparable. Check: does the bilipschitz comparison from small drift transport the local Sobolev constant correctly? Is the self-improving closure non-circular?

## Output

## Scientific verification memo

### Overall finding

With the flow estimates in §§4–6 taken as supplied:

- The collapse-cancellation computation in §3d is correct after adding the scale condition \(6r\le 1\) and stating the Sobolev inequality for compactly supported functions.
- The spectral algebra in §7d is correct.
- The local projector lemma and the Bochner arithmetic are correct when the calibrated spectrum holds throughout an open set.
- The present §7b–§7e passage only produces the calibrated spectrum at one point. Continuity does not make its eigenvalues constant nearby, so the projector lemma cannot be applied as written.
- The stated terminal curvature derivative bounds and the disjoint core balls provide a concrete way to strengthen pointwise smallness to open-ball vanishing.
- Small metric drift does transport the Sobolev inequalities correctly. The displayed \(K_2\) estimate, however, does not by itself improve the first-exit threshold \(2K_2(0)\); a time-sensitive Grönwall estimate is absent from the consolidated note.

Thus the exact proof text does not establish Theorem A, although the terminal spectral transition appears repairable using ingredients already stated in §7b.

---

## 1. Collapse cancellation

Let \(V_\alpha=\operatorname{Vol}B_{6r}(x_\alpha)\). If \(6r\le1\) and
\[
\mathcal M_{\mathrm{vol}}(|\mathrm{Rm}|^2)(x_\alpha)\le\kappa_0^2,
\]
then directly from the definition,
\[
\int_{B_{6r}(x_\alpha)}|\mathrm{Rm}|^2
 \le \kappa_0^2V_\alpha .
\]
For \(0\le\eta_\alpha\le1\), supported in this ball,
\[
K_{2,\alpha}(0)
 =\int\eta_\alpha^2(1+|\mathrm{Rm}|^2)
 \le (1+\kappa_0^2)V_\alpha .
\]

The local Sobolev estimate needed here is the standard Ricci-lower-bound form
\[
\|u\|_{L^4(B_R)}^2
 \le C e^{CR}\frac{R^2}{\operatorname{Vol}(B_R)^{1/2}}
 \left(\|\nabla u\|_2^2+R^{-2}\|u\|_2^2\right),
 \qquad u\in C_c^\infty(B_R),
\]
under \(\operatorname{Ric}\ge-3g\). Taking \(R=6r\) and absorbing the numerical factors gives (3.3). The cut-off quantities used later are compactly supported, so this is the appropriate version.

Consequently,
\[
\begin{aligned}
\gamma_\alpha
 &=\mathcal S_\alpha K_{2,\alpha}(0)^{1/2}\\
 &\le
 \frac{Cr^2}{V_\alpha^{1/2}}
 \bigl((1+\kappa_0^2)V_\alpha\bigr)^{1/2}\\
 &=Cr^2\sqrt{1+\kappa_0^2}.
\end{aligned}
\]
The cancellation of \(V_\alpha\) is exact and does not involve injectivity radius.

For the maximal estimate, Bishop–Gromov under
\(\operatorname{Ric}\ge-3g\) supplies uniform local doubling on every fixed radius interval. A Vitali argument for the maximal operator truncated at radius \(1\) uses enlarged balls of radius at most a fixed number such as \(5\); Bishop–Gromov still gives a constant depending only on dimension because the Ricci scale and truncation scale are fixed. Hence
\[
\operatorname{Vol}\{\mathcal M_{\mathrm{vol}}f>\lambda\}
 \le \frac{C_{\mathrm{HL}}}{\lambda}\int |f|
\]
is valid with no dependence on collapse or topology. The parameter list should explicitly include \(r\le1/6\), or a slightly smaller fixed value accommodating all ball enlargements.

---

## 2. Terminal point selection and local compactness

### 2.1 Averaging

Since \(\mathfrak D\ge0\), for every measurable set \(\Pi\) of positive terminal volume,
\[
\operatorname*{ess\,inf}_{\Pi}\mathfrak D
 \le \frac{1}{\operatorname{Vol}_{g(T)}(\Pi)}
       \int_\Pi\mathfrak D\,d\mu_{g(T)}.
\]
Thus the minimum-of-average calculation is correct, up to replacing “minimum” by “infimum” when \(\Pi\) is a union of open balls.

The volume fraction from §3b is initially measured using \(g(0)\). From
\[
\partial_tg=-2aE,\qquad
d(t)=\int_0^t\|aE\|_{\infty,g(s)}\,ds,
\]
one has
\[
e^{-2d(t)}g(0)\le g(t)\le e^{2d(t)}g(0).
\]
In dimension four this gives
\[
e^{-4d(t)}d\mu_{g(0)}
 \le d\mu_{g(t)}
 \le e^{4d(t)}d\mu_{g(0)}.
\]
Hence an initial volume fraction \(\alpha_0\) becomes at least
\(e^{-8d_0}\alpha_0\) at time \(T\). The constant in (7.3) therefore changes by a fixed factor, but the \(O(\delta^2)\) conclusion remains valid.

### 2.2 The plateau-edge problem

The selected point in the current text may lie arbitrarily close to the edge of
\[
\Pi=\bigcup_\alpha B_{4r}(x_\alpha).
\]
Although \(a=1\) at that point, there need not be a fixed-radius neighborhood on which \(a=1\). Thus
\[
\|aE(T)\|_\infty\longrightarrow0
\]
does not imply \(E\to0\) on a common neighborhood of that point.

The core
\[
\Omega=\bigcup_{\alpha\in\mathcal C}B_r(x_\alpha)
\]
already has the required volume fraction, because the selected \(B_r\)'s are disjoint and (3.2) gives
\[
\operatorname{Vol}\Omega
 =\sum_\alpha\operatorname{Vol}B_r(x_\alpha)
 \ge\alpha_0\operatorname{Vol}M.
\]
Every point of \(\Omega\) has a fixed buffer inside \(B_{4r}(x_\alpha)\). Selecting from \(\Omega\), rather than all of \(\Pi\), makes the Einstein-limit statement valid on a common ball.

### 2.3 Exponential pullbacks

Assume a uniform curvature bound \(|\mathrm{Rm}|\le K\) and uniform curvature derivative bounds on a buffered neighborhood. For
\[
R<\min\{c r,\pi/(2\sqrt K)\},
\]
the exponential differential has no conjugate degeneration. Rauch comparison gives
\[
c(K,R)^{-1}g_{\mathrm{Euc}}
 \le \exp_{x_i}^{*}g_i(T_i)
 \le c(K,R)g_{\mathrm{Euc}}
\]
on \(B_R(0)\subset T_{x_i}M_i\), and consequently
\[
\operatorname{Vol}_{\exp^*g_i}B_R(0)\ge c(K,R)R^4.
\]

The exponential map need not be injective under collapse, so this is not necessarily a coordinate chart onto a subset of \(M_i\). It is nevertheless a smooth local pullback metric on the tangent ball, sufficient for local tensor equations and \(C^\infty\) compactness.

Curvature derivative bounds and normal-coordinate Jacobi estimates give uniform coordinate derivatives of the pullback metrics. After identifying the oriented tangent spaces with \(\mathbb R^4\), a subsequence converges smoothly. The quantities
\[
E,\quad s,\quad |W^+|,\quad w=\lambda_{\min}(W^+),\quad G,\quad\mathfrak D
\]
are continuous under this convergence; ordered eigenvalues of a symmetric endomorphism are continuous. Therefore \(\mathfrak D_i(0)\to0\) implies \(\mathfrak D_h(0)=0\).

Smooth metric convergence plus \(E_i\to0\) uniformly on a fixed ball is enough to obtain \(\operatorname{Ric}_h=-h\); convergence of derivatives of \(E_i\) to zero is not needed.

---

## 3. Spectral determination

At a point where \(\mathfrak D=0\), each summand in (7.1) vanishes. In particular,
\[
E=0,\qquad s=-4,
\]
and
\[
s+8\sqrt6\,|W^+|=0.
\]
Thus
\[
|W^+|=\frac1{2\sqrt6},
\qquad |W^+|^2=\frac1{24}.
\]

Set \(u=|W^+|\) and \(\alpha=\sqrt{2/3}\). Then
\[
\alpha u=\frac16,\qquad
f=\frac23s-2\alpha u=-\frac83-\frac13=-3.
\]
Writing
\[
\xi=w+\alpha u=w+\frac16,
\]
one has \(0\le\xi\le1/6\): the lower inequality is the sharp algebraic estimate
\(w\ge-\sqrt{2/3}\,u\), while \(w\le0\) because \(w\) is the smallest eigenvalue of a trace-free \(3\times3\) endomorphism.

Since
\[
b=f+2\xi=-3+2\xi<0,
\]
the signed quantity \(b_-=\min(b,0)\) equals \(b\), and
\[
G=f^2-b^2
 =9-(-3+2\xi)^2
 =4\xi(3-\xi).
\]
Therefore \(G=0\) gives \(\xi=0\), hence
\[
w=-\frac16.
\]
If the other eigenvalues are \(\lambda_1,\lambda_2\), then
\[
\lambda_1+\lambda_2=\frac16,
\qquad
\lambda_1^2+\lambda_2^2
 =\frac1{24}-\frac1{36}
 =\frac1{72}.
\]
It follows that \((\lambda_1-\lambda_2)^2=0\), so
\[
\operatorname{Spec}(W^+)
 =\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
This part is correct.

---

## 4. Projector–Bochner argument

### 4.1 The local projector lemma itself

The lemma in `step6_local_projector_obstruction_and_collapse_reduction.tex` is local and does not require compactness.

On an open set where
\[
W^+=\mu I+(\lambda-\mu)P_\omega
\]
with two distinct constant eigenvalues, the Einstein equation gives
\(\delta W^+=0\). Differentiating and taking divergence yields
\[
(\nabla^a\omega_{ab})\omega_{cd}
 +\omega_{ab}\nabla^a\omega_{cd}=0.
\]
Contraction with \(\omega^{cd}\), using constant norm, gives
\[
\nabla^a\omega_{ab}=0.
\]
Substitution then gives
\[
\omega_{ab}\nabla^a\omega_{cd}=0.
\]
A nonzero self-dual two-form is nondegenerate, and under the normalization in the note,
\[
\omega_a{}^c\omega_c{}^b=-\delta_a{}^b.
\]
Hence \(\nabla\omega=0\), so \(P_\omega\) and \(W^+\) are parallel. This argument works on any sufficiently small open neighborhood supporting a local eigenform.

The Bochner arithmetic is also correct:
\[
-\frac4{24}-36\left(-\frac1{864}\right)
 =-\frac16+\frac1{24}
 =-\frac18.
\]

### 4.2 The application in §7e

The compactness argument in §7c gives the calibrated spectrum only at the origin. Continuity implies that the lowest eigenvalue remains simple nearby and remains close to \(-1/6\). It does not imply that it equals \(-1/6\) nearby. The upper double eigenvalue may also split immediately away from the origin.

Without open-set constancy, the Bochner identity at the origin reads
\[
\Delta|W^+|^2(0)
 =2|\nabla W^+|^2(0)-\frac18,
\]
not \(0=-1/8\). Both the Laplacian and gradient terms are undetermined. Connectedness does not turn one-point algebraic data into constant eigenvalue functions.

This is the central break in the written §7b–§7e chain.

### 4.3 Open-ball vanishing obtainable from the stated data

The stated disjoint core balls and terminal \(C^1\) curvature control yield a stronger selection argument.

Let
\[
\Omega_\alpha=B_r^{g(0)}(x_\alpha).
\]
These sets are pairwise disjoint, and their terminal volumes have total size at least a fixed fraction of \(\operatorname{Vol}_{g(T)}M\). Therefore
\[
\sum_\alpha\int_{\Omega_\alpha}\mathfrak D
 \le C\delta^2\operatorname{Vol}_{g(T)}M,
\qquad
\sum_\alpha\operatorname{Vol}_{g(T)}\Omega_\alpha
 \ge c\operatorname{Vol}_{g(T)}M.
\]
For at least one \(\alpha\),
\[
\fint_{\Omega_\alpha}\mathfrak D\,d\mu_{g(T)}
 \le C\delta^2. \tag{4.1}
\]

The terminal Shi estimates on the buffered core give a uniform Lipschitz constant
\[
|\nabla\mathfrak D|\le L.
\]
The smallest eigenvalue \(w\) is Lipschitz with constant controlled by
\(|\nabla W^+|\), and \(b\mapsto(\min\{b,0\})^2\) is \(C^1\), so this estimate is compatible with the definition of \(G\).

For \(y\) in an inner half-ball, put \(m=\mathfrak D(y)\) and
\[
\rho=\min\{cr,m/(2L)\}.
\]
Then \(\mathfrak D\ge m/2\) on \(B_\rho(y)\). Ricci lower comparison at time \(T\), together with the fixed buffer, gives
\[
\frac{\operatorname{Vol}B_\rho(y)}
     {\operatorname{Vol}\Omega_\alpha}
 \ge c\left(\frac{\rho}{r}\right)^4.
\]
Combining this with (4.1),
\[
C\delta^2
 \ge c\,m\min\left\{1,\left(\frac{m}{Lr}\right)^4\right\}.
\]
Thus
\[
\sup_{\Omega_\alpha^{\mathrm{inner}}}\mathfrak D
 \longrightarrow0;
\]
quantitatively, in the small-\(m\) regime,
\[
\sup\mathfrak D\le C\delta^{2/5}.
\]

Exponential pullbacks based at the center of this ball then converge to a metric satisfying
\[
\mathfrak D_h\equiv0
\]
on an open tangent ball. The spectral computation of §7d applies at every point there, so the spectrum is constant on that open set and the local projector–Bochner argument applies. This supplies the open-set information absent from the current minimum-at-one-point argument.

---

## 5. First-exit bootstrap

### 5.1 Sobolev transport

The metric drift does transport the local Sobolev inequality correctly. From
\[
e^{-2d_0}g(0)\le g(t)\le e^{2d_0}g(0),
\]
the \(L^4\), \(L^2\), and gradient norms on each fixed cut-off domain are comparable by factors depending only on \(d_0\). Thus
\[
\mathcal S_\alpha(t)\le e^{Cd_0}\mathcal S_\alpha(0).
\]
The same comparison controls cut-off gradients and the volume-normalized energy. Using the fixed domains defined by \(\eta_\alpha\) avoids any need to compare moving geodesic balls.

This part of the bootstrap is not circular: before the first-exit time, \(d(t)<d_0\) by definition, so the transported Sobolev inequality is available while deriving the pointwise estimate. Integrating (5.5) up to any \(\tau\le T\) gives
\[
d(\tau)
 \le C\delta r^{2/3}\tau^{2/3}
 \le C\delta\theta^{2/3}r^2.
\]
Choosing \(\delta\) with a strict margin rules out exit through \(d=d_0\).

### 5.2 The \(K_2\) threshold

Equation (5.1), as displayed,
\[
\sup_{t\le\tau}K_2(t)\le C K_2(0),
\]
does not imply
\[
K_2(\tau)<2K_2(0)
\]
unless \(C<2\). The line in §5h
\[
CK_2(0)<2K_2(0)
\]
cannot be achieved by making \(\delta\) smaller because \(C\) is independent of \(\delta\).

A time-sensitive estimate of the form
\[
K_2(t)+c\int_0^tD_2
 \le K_2(0)
   +C\int_0^t(1+r^{-2})K_2(s)\,ds
\]
would give
\[
K_2(t)\le
e^{C(1+r^{-2})t}K_2(0)
 \le e^{C(\theta+r^2\theta)}K_2(0).
\]
Taking \(\theta\) sufficiently small would then give, for example,
\[
K_2(t)\le\frac32K_2(0),
\]
which is the strict improvement required at the first-exit time. The consolidated file does not display this retained-initial-value estimate, so §5h is incomplete on its present equations.

---

## Final assessment of the five points

1. **Collapse cancellation:** correct, with \(6r\le1\) and the compact-support Sobolev formulation made explicit.

2. **Terminal selection and extraction:** the averaging inequality, exponential pullback noncollapse, and passage of \(\mathfrak D\) under smooth convergence are correct. Selection from all of \(B_{4r}\) does not ensure an Einstein neighborhood; the disjoint \(B_r\) cores do.

3. **Spectral determination:** fully correct.

4. **Projector–Bochner:** the local lemma and arithmetic are correct for constant spectrum on an open set. One-point spectral data do not meet that hypothesis. The ball-average plus Lipschitz argument above supplies a plausible rigorous bridge using the stated terminal estimates.

5. **First exit:** Sobolev transport and the drift bootstrap are valid. The strict \(K_2<2K_2(0)\) improvement is not contained in (5.1); it requires a Grönwall estimate retaining the initial coefficient and a sufficiently small \(\theta\).