# TTCS Independent Branch Record

```json
{
  "step_id": 31,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step31_weighted_moser_interpolation_and_first_exit.md",
    "Sessions/S0910A03/workspace/notes/step31_coupled_continuation_theorem.md",
    "Sessions/S0910A03/workspace/notes/step31_corrected_support_and_terminal_density.md",
    "Sessions/S0910A03/workspace/scripts/verify_step31_weighted_interpolation.py",
    "Sessions/S0910A03/workspace/scripts/verify_step31_coupled_continuation.py"
  ]
}
```

## Task

Verify the complete analytic chain for the four-dimensional negative-branch Ricci-pinching gap, focusing on three specific claims:

1. WEIGHTED MOSER INTERPOLATION: The parabolic step combines sup_t K_p (energy) with K_{2p} = ||Z_p||_4^4 (Sobolev on Z_p = a^{(p-1)/2}Φ^{p/2}), then K_{3p/2} ≤ K_p^{1/2} K_{2p}^{1/2} (Cauchy-Schwarz). This supposedly resolves the half-power gap by noting ||Z_p||_3^3 is never used. Critically check: does the gradient ||∇Z_p||_2^2 genuinely decompose into D_p (a-weighted curvature dissipation) plus r^{-2}K_p (cutoff gradient) without any remaining gap? Does the 4D Sobolev step for ||Z_p||_4^2 ≤ S²(||∇Z_p||_2² + r^{-2}||Z_p||_2²) truly close the Moser iteration with polynomial p-loss? Does the L^∞ limit K_p^{1/p} → ||aΦ||_∞ give the correct weighted supremum?

2. COUPLED CONTINUATION: The induction claims d/dt(X_p+Z_p)+cD ≤ C(1+X_p+Z_p) where X_p=||∇^mU||_p^p and Z_p=||∇^{m+1}χ||_p^p, closing by Grönwall without dividing by χ. Check: is the connection-change formula ∂_t(∇^{m+1}χ) = U*∇^{m+1}χ + ∇^mU*∇χ + lower correct? Does the coupling genuinely avoid circular dependence? Does the {p,2p,4p} Hölder schedule work for all products?

3. TERMINAL BRIDGE: The terminal density ∫D^loc ≤ CQ with ε=Q/Vol regularization, exponential-pullback averaging, and the projector contradiction. Check: does the eigenline density restriction to the bounded-curvature region L_i create a gap when chart geodesics extend outside L_i? Does the Q/A normalization correctly account for varying topology?

## Output

# Scientific verification memo

## Overall assessment

The algebraic core of the weighted interpolation is correct:

\[
K_{2p}=\|Z_p\|_4^4,\qquad
K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2},
\]

and the gradient of \(Z_p\) is controlled by the weighted dissipation plus the cutoff term. Thus the previously noted half-power mismatch involving \(\|Z_p\|_3^3\) is not an obstruction to this interpolation route.

The supplied notes, however, do not yet derive the full parabolic recurrence or the coupled continuation theorem. Several displayed steps use the wrong Sobolev power, an incorrect reaction weight, or an unavailable time supremum. The terminal localization is structurally plausible after radius and regularity repairs, while its \(Q/A\) calculation currently uses an inequality in the wrong direction.

---

## 1. Weighted Moser interpolation

### 1.1 Gradient computation: valid for \(F\)

For

\[
Z_p=a^{(p-1)/2}F^{p/2},\qquad
K_p=\int a^{p-2}F^p,
\]

one has

\[
\nabla Z_p
=\frac{p-1}{2}a^{(p-3)/2}\nabla a\,F^{p/2}
+\frac p2a^{(p-1)/2}F^{p/2-1}\nabla F .
\]

Consequently,

\[
|\nabla Z_p|^2
\le Cp^2\left(
a^{p-3}|\nabla a|^2F^p
+a^{p-1}F^{p-2}|\nabla F|^2
\right).
\]

Since \(a=\chi^2\),

\[
a^{p-3}|\nabla a|^2
=4a^{p-2}|\nabla\chi|^2
\le Cr^{-2}a^{p-2}.
\]

For \(F=(1+|\mathrm{Rm}|^2)^{1/2}\),

\[
|\nabla F|
=\frac{|\langle \mathrm{Rm},\nabla\mathrm{Rm}\rangle|}{F}
\le |\nabla\mathrm{Rm}|.
\]

Therefore

\[
\boxed{\|\nabla Z_p\|_2^2
\le Cp^2\left(D_p+r^{-2}K_p\right)}
\]

with

\[
D_p=\int a^{p-1}F^{p-2}|\nabla\mathrm{Rm}|^2.
\]

No lower bound for \(a\) is used. At \(p=2\), \(Z_2=\chi F\), so the apparently singular expression \(a^{-1}|\nabla a|^2\) is interpreted directly as \(4|\nabla\chi|^2\).

For \(\Phi=|E|\), the same calculation requires the corresponding dissipation

\[
\int a^{p-1}|E|^{p-2}|\nabla E|^2.
\]

The sentence in the note using \(|\nabla\Phi|\le|\nabla\mathrm{Rm}|/\Phi\) does not apply to \(\Phi=|E|\). One instead uses the weak Kato inequality and \(|\nabla E|\le C|\nabla\mathrm{Rm}|\), with a regularization near \(E=0\).

### 1.2 Interpolation identity: valid

The exponent calculation is exact:

\[
\begin{aligned}
K_{3p/2}
&=\int
\left(a^{(p-2)/2}F^{p/2}\right)
\left(a^{(2p-2)/2}F^p\right)\\
&\le K_p^{1/2}K_{2p}^{1/2}.
\end{aligned}
\]

Thus \(\|Z_p\|_3^3\) is genuinely irrelevant if the iteration is organized through this fixed-time Cauchy–Schwarz inequality.

### 1.3 Correct four-dimensional Sobolev coefficient

On a radius-\(r\) ball, the collapse-adapted inequality should be written

\[
\|u\|_4^2
\le C_S\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right),
\]

where

\[
C_S=C(4,\kappa r^2)\frac{r^2}{\operatorname{Vol}(B_r)^{1/2}}.
\]

The note alternates between \(S\) and \(S^2\). Its stated

\[
S^2=C\,\frac{r^4}{\operatorname{Vol}(B_r)}
\]

is the square of the actual coefficient. With \(S_j=Cr^2/\operatorname{Vol}^{1/2}\), the usable estimate is

\[
K_{2p}^{1/2}=\|Z_p\|_4^2
\le C S_jp^2(D_p+r^{-2}K_p),
\]

not \(CS_j^2p^2(\cdots)\).

The asserted four-dimensional product inequality

\[
\int u^4\lesssim
\left(\int|\nabla u|^2\right)\left(\int u^2\right)
\]

is not the four-dimensional Sobolev inequality; that product form is associated with dimension two. In four dimensions, squaring the Sobolev estimate gives a square of the energy term.

What is available after time integration is

\[
\int_I K_{2p}^{1/2}\,dt
\le CS_jp^2\int_I(D_p+r^{-2}K_p)\,dt,
\]

not a bound for \(\int_IK_{2p}\,dt\).

Combining this with the valid interpolation gives

\[
\boxed{
\int_I K_{3p/2}\,dt
\le
\left(\sup_IK_p\right)^{1/2}
CS_jp^2
\int_I(D_p+r^{-2}K_p)\,dt .
}
\]

This is the mathematically consistent parabolic step. It yields a spacetime \(K_{3p/2}\) estimate and hence a good time slice at exponent \(3p/2\). It does not yield the \(\sup K_{2p}\) used in §§3 and 7.5.

### 1.4 The \(p=2\) absorption has a wrong square root

The note writes

\[
K_3\le H_2^{1/2}S_j(D_2+r^{-2}H_2)^{1/2}.
\]

The correct chain is

\[
K_3\le K_2^{1/2}K_4^{1/2}
\le C S_jH_2^{1/2}(D_2+r^{-2}H_2).
\]

Thus, with

\[
\gamma_j=S_jH_{2,j}^{1/2},
\]

one obtains

\[
K_3\le C\gamma_j(D_2+r^{-2}H_2).
\]

Small \(\gamma_j\) directly absorbs the \(D_2\) term. The Young inequality involving
\(\gamma_j(D_2+r^{-2}H_2)^{1/2}\) is based on the wrong Sobolev power.

The integrated consequence also contains the dissipation contribution:

\[
\int_0^T K_3
\le C\gamma_j
\left(\int_0^TD_2+r^{-2}\int_0^TH_2\right),
\]

rather than only \(C\gamma_jT\sup H_2\).

### 1.5 Reaction weight mismatch

The energy equation initially contains

\[
\int a^{p-1}F^{p+1}.
\]

This weight is compatible with Hölder:

\[
\int a^{p-1}F^{p+1}
\le K_p^{(p-1)/p}K_{2p}^{1/p}.
\]

The note then replaces it by the larger quantity

\[
\int a^{p-2}F^{p+1}
\]

and applies the same Hölder formula. That formula no longer holds: its right-hand side has \(a\)-exponent \(p-1\), not \(p-2\). On a region where \(a=\varepsilon\), the ratio between the two weights is \(\varepsilon^{-1}\), so no uniform constant repairs this substitution.

The original \(a^{p-1}\) reaction should be retained.

### 1.6 High-exponent recurrence is not yet derived

At \(p=3\),

\[
K_4\le K_2^{1/2}K_6^{1/2}
\le C\gamma_j(D_3+r^{-2}K_3),
\]

so fixed small \(\gamma_j\) can indeed give linear propagation of \(K_3\).

For general \(p\), the useful subcritical identity is

\[
\int a^{p-1}F^{p+1}
\le K_3^{1/3}K_{3p/2}^{2/3}.
\]

This connects the spacetime \(K_3\) control to the \(p\mapsto3p/2\) recurrence. A complete argument still requires nested time intervals, time cutoffs, and an explicit recurrence whose constants remain polynomial after taking \(p\)-th roots. The current text instead invokes an unavailable \(\sup K_{2p}\) and leaves the reaction term inside “propagation.” The Python script verifies exponent identities but does not derive this parabolic recurrence.

### 1.7 Weighted \(L^\infty\) endpoint: correct

Since

\[
K_p^{1/p}=\|a^{1-2/p}F\|_{L^p},
\]

the endpoint is \(aF\), not \(a^{1/2}F\). More directly, a uniform bound for \(K_p^{1/p}\) along \(p\to\infty\) implies \(a(x)F(x)\le C\) at every point with \(a(x)>0\), by integrating over a small neighborhood of that point. At \(a=0\), the weighted quantity is zero.

Thus the intended endpoint

\[
\|aF\|_\infty
\]

is the correct one.

---

## 2. Coupled continuation

### 2.1 Highest-order connection variation: correct in order

Let

\[
h=\partial_tg=-2\operatorname{Ric}(U).
\]

Then

\[
\partial_t\Gamma=g^{-1}*\nabla h
=g^{-1}*\nabla\operatorname{Ric}(U),
\]

so its highest derivative is \(\nabla U\). For \(H=\nabla^{m+1}\chi\),

\[
\partial_tH
=
\nabla^mU*\nabla\chi
+\sum_{j<m}\nabla^jU*\nabla^{m+1-j}\chi.
\]

When differentiating \(|H|^p\,d\mu\), metric and volume variation add a term of the form \(U*H\). Hence the schematic highest-order expression

\[
U*H+\nabla^mU*\nabla\chi+\text{lower terms}
\]

has the correct derivative orders.

### 2.2 Linear coupled Grönwall is not established

The \(\Gamma_1\) integration by parts does reduce \(\nabla^{m+2}\chi\) to \(\nabla^{m+1}\chi\), and one resulting term has the valid estimate

\[
\int |U|^2|H|^2|V|^{p-2}
\le
\|U\|_\infty^2\|H\|_p^2\|V\|_p^{p-2}
\le C(X_p+Z_p).
\]

Other resulting terms contain products such as

\[
H*\nabla U*|V|^{p-1}
\]

or their partially integrated versions. Merely knowing \(H,V\in L^p\) does not place \(H|V|^p\) in \(L^1\). Such terms require either:

- a precise integration-by-parts cancellation,
- pointwise control of the lower factor,
- or a simultaneous interpolation estimate with absorbable weighted gradients.

Those estimates are not written in the note.

The stated \(\{p,2p,4p\}\) schedule only verifies one sample reciprocal-exponent sum. It does not enumerate all products in the differentiated \(U\)-equation and the \(H\)-equation. In particular, a current-order factor in \(L^p\) multiplied by a lower factor not yet known in \(L^\infty\) can create dependence on current \(L^{2p}\) or \(L^{4p}\) norms. The scripts print the assumed hierarchy rather than deriving it from the tensor equations.

### 2.3 Recovery of \(T\) off the plateau is incorrect

The statement

> on \(\{a<1/2\}\), the flow is not active

is false. The transition annulus has \(0<a<1/2\) and

\[
\partial_tg=-2aE\ne0.
\]

Moreover, curvature variation contains

\[
\partial_t\mathrm{Rm}
=\nabla^2(aE)+\mathrm{Rm}*(aE),
\]

so derivatives of \(a\) produce terms such as

\[
\nabla^2a*E,\qquad \nabla a*\nabla E,
\]

which are not \(O(a)\). Therefore

\[
|\nabla^m\mathrm{Rm}(t)-\nabla^m\mathrm{Rm}(0)|=O(a\,t)
\]

does not follow near the transition region.

A division-free route is conceivable through

\[
\partial_t\nabla^k\mathrm{Rm}
=
\nabla^{k+2}\operatorname{Ric}(U)+\text{lower terms},
\]

because bounds for sufficiently many derivatives of \(U\) would control metric-curvature evolution by time integration. That route requires a separate coupled hierarchy and is not contained in §2.5.

### 2.4 Regularization is substantive, not automatic

Replacing \(a\) by \(a+\varepsilon\) gives a uniformly parabolic Ricci–DeTurck system for each \(\varepsilon>0\), but passing to \(\varepsilon\to0\) requires estimates uniform in \(\varepsilon\) for:

- all derivatives of the evolving metric,
- time regularity,
- transition-region terms containing derivatives of \(a\),
- and the relation between \(U_\varepsilon=(a+\varepsilon)T\) and \(U=aT\).

The weighted dissipation alone does not supply unweighted derivative estimates near \(a=0\). Describing this as standard porous-medium theory does not provide the needed geometric argument.

Accordingly, the connection-order bookkeeping is sound, but the boxed inequality

\[
\frac d{dt}(X_p+Z_p)+cD_{m,p}
\le C(1+X_p+Z_p)
\]

has not been obtained from the displayed terms.

---

## 3. Terminal density bridge

### 3.1 Localization of the eigenline density

Localizing \(\mathfrak G_i\) to \(L_i\) is compatible with point selection if every exponential averaging ball lies strictly inside \(L_i\).

For \(p\in P_j=B_r(p_j)\) and vectors of length at most \(r\), the image lies in \(B_{2r}(p_j)\), well inside \(L_j=B_{4r}(p_j)\). Thus the averaging used to select \(p_i\) can access the full eigenline density.

The assertion that \(\exp_p(B_{3r}(0))\subset L_j\) has no radial slack: \(r+3r=4r\). Since the regions were defined with the initial metric while the exponential map uses the terminal metric, bilipschitz drift can move such geodesics outside \(L_j\). Using a smaller tangent ball, or a larger plateau, resolves this geometric issue.

Curvature control does not imply injectivity of \(\exp_p\); a collapsed flat torus is the standard example. Injectivity is not necessary for a germ argument. If \(r\sqrt K\) is sufficiently small, Rauch comparison excludes conjugate points and makes \(\exp_p^*g\) a smooth nondegenerate metric on the tangent ball, even when the exponential map wraps around the manifold.

The averaging estimate can then be based on:

1. Rauch control of the exponential Jacobian;
2. Liouville invariance of geodesic flow after integrating over base points and directions.

### 3.2 Uniform smooth convergence needs interior derivative estimates

A terminal curvature bound alone gives \(C^{1,\alpha}\)-type compactness after suitable coordinates, not smooth convergence. The continuation estimates in the note depend on initial high derivatives and therefore are not uniform along the varying family.

On a strict plateau, however, \(a=1\), so the equation is the ordinary normalized Ricci flow. A curvature bound on a parabolic neighborhood separated from the transition region would give uniform interior Shi estimates at positive time. This is the natural source of the derivative bounds needed for smooth convergence of \(\exp_{p_i}^*g_i(T)\). That step is not presently included.

### 3.3 The \(Q/A\) line uses the wrong inequality direction

The note writes

\[
\operatorname{Vol}_i\ge cA_i,
\qquad
Q_i\le C\delta_i^2\operatorname{Vol}_i
\le C\delta_i^2A_i.
\]

The last implication requires \(\operatorname{Vol}_i\le CA_i\), not the displayed lower bound.

The desired upper volume estimate can instead be derived from Chern–Gauss–Bonnet. Writing \(z\) for traceless Ricci,

\[
8\pi^2\chi(M)
=
\int\left(|W|^2-\frac12|z|^2+\frac{s^2}{24}\right).
\]

Since

\[
\int(s+4)^2\le4Q,\qquad \int|z|^2\le Q,
\]

and \(Q=o(\operatorname{Vol})\), one obtains

\[
\int s^2\ge c\,\operatorname{Vol}
\]

for sufficiently small defect, hence

\[
\operatorname{Vol}\le C\chi(M).
\]

Together with \(\chi(M_i)/A_i\le C(\kappa)\),

\[
\frac{Q_i}{A_i}
\le
C\delta_i^2\frac{\operatorname{Vol}_i}{A_i}
\le
C\delta_i^2\frac{\chi(M_i)}{A_i}
\longrightarrow0.
\]

Thus the normalization can be repaired, but not by the inequality currently cited.

The regularization estimate itself is arithmetically correct:

\[
\varepsilon_i=\frac{Q_i}{\operatorname{Vol}_i}
\quad\Longrightarrow\quad
\varepsilon_i^2\operatorname{Vol}_i
=\frac{Q_i^2}{\operatorname{Vol}_i}
\le \delta_i^2Q_i.
\]

### 3.4 Projector contradiction

For the limiting spectrum

\[
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right),
\]

write \(P\) for the rank-one projector onto the simple eigenspace. Then

\[
W^+=\frac1{12}I-\frac14P,
\qquad
\nabla W^+=-\frac14\nabla P.
\]

The spectrum by itself does not imply \(\nabla P=0\). The localized density
\(\mathfrak G_\infty=0\) must supply precisely this parallel-projector conclusion. Its definition and the passage from vanishing integral to \(\nabla P=0\) are not included in the supplied files, so that part cannot be independently reconstructed here.

Assuming \(\nabla P=0\), the final contradiction is correct. Indeed,

\[
|W^+|^2=\frac1{24},
\qquad
\det W^+=-\frac1{864},
\qquad s=-4.
\]

The Einstein–Weyl formula

\[
\frac12\Delta|W^+|^2
=
|\nabla W^+|^2+\frac s2|W^+|^2-18\det W^+
\]

then gives

\[
|\nabla W^+|^2
=\frac1{16},
\]

incompatible with \(\nabla W^+=0\).

---

## Final scientific status

- The weighted Cauchy–Schwarz interpolation, cutoff-gradient calculation, and endpoint \(\|aF\|_\infty\) are valid.
- The complete Moser recurrence is still absent: the current text uses a dimension-two product inequality, the wrong \(p=2\) square root, an incompatible reaction weight, and an unavailable \(\sup K_{2p}\).
- The leading derivative order in the connection-change formula is correct, but the linear coupled Grönwall estimate, finite exponent schedule, transition-region curvature recovery, and uniform \(\varepsilon\)-regularization have not been derived.
- The terminal localization can work on strictly smaller exponential balls with interior Ricci-flow derivative estimates.
- The \(Q/A\) conclusion follows from \(\operatorname{Vol}\le C\chi\) and \(\chi/A\le C\), not from the displayed lower volume bound.
- The final Weyl calculation is correct once the localized eigenline density is shown to force a parallel rank-one projector.

These materials concern a controlled four-dimensional Ishida–LeBrun family; they do not by themselves prove or refute the dimension-wide proposition for all closed manifolds.