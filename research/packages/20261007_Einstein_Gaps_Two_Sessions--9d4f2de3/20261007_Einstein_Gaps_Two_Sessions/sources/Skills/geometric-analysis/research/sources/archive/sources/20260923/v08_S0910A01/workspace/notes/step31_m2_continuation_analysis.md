# Step 31: Analysis of the m=2 continuation obstruction


**Step 32 superseding audit.**  The simple estimate in Section 3 using
\(\|\nabla^2\chi\|_\infty\) is not an established base step of the coupled
continuation induction.  The current valid formulation is
`workspace/notes/step32_nested_moser_and_tensor_audit.md`, Section 6: for
\(W=\nabla^2U\), \(B=\nabla^2\chi\), and \(u=\chi|W|^{p/2}\),
\[
\int \chi |B| |W|^p\le \varepsilon D_p+
C_\varepsilon p^2 C_S\|B\|_4^2(1+r^{-2})X_p.
\]
Thus the term is controlled only if the previous coupled level supplies
\(\|\nabla^2\chi\|_4\) in the evolving geometry, or if an exact shifted Wang
grouped identity is proved.  Coefficient regularization \(a\mapsto a+\varepsilon\)
remains unsafe without exterior-curvature-independent estimates.
Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 1. The question

A03 #327 asks: in the $m=2$ derivative estimate for the shifted-curvature
continuation, the term

$$
\int_M \chi|\nabla^2\chi||\nabla^2 U|^p\,d\mu
\tag{Q}
$$

has a single $\chi$ factor, while the dissipation is

$$
D_{2,p} = \int_M \chi^2|\nabla^3 U|^2|\nabla^2 U|^{p-2}\,d\mu.
$$

Does an exact tensor cancellation save it, or is a stronger estimate needed?

## 2. Origin of the term

The term (Q) arises from the first sum in Codex eq. (4.1) for $m=2$.  With
$\alpha+\beta+\gamma=4$, $\alpha+\beta\ge1$, $0\le\gamma\le3$, the case
$(\alpha,\beta,\gamma)=(0,2,2)$ contributes

$$
\chi\cdot\nabla^2\chi*\nabla^2 U
$$

to $\partial_t(\nabla^2 U)$.  Testing against $|\nabla^2 U|^{p-2}\nabla^2 U$
produces (Q).  This is **not** the $\Gamma_1$ term (which has $\gamma=0$ and
is handled by the IBP mechanism in Section 7.3); it is a **lower cutoff-order
term** that remains after the IBP reduces the dangerous $\Gamma_1,\Gamma_2,\Gamma_3$.

## 3. Resolution: Gronwall, not dissipation

The term (Q) does **not** need to be absorbed by $D_{2,p}$.

**Bound:**
$$
\int\chi|\nabla^2\chi||\nabla^2 U|^p
\le \|\nabla^2\chi\|_\infty\int_M|\nabla^2 U|^p
\le Cr^{-2}\|\nabla^2 U\|_{L^p}^p
= Cr^{-2}A_2(p)^p.
\tag{3.1}
$$

This uses $\chi\le1$ and $|\nabla^2\chi|\le C/r^2$ (the cutoff has uniformly
bounded second derivatives on a fixed support).

**Consequence:** The term contributes to the **right-hand side** of the energy
inequality (Codex eq. 7.15):

$$
\frac{d}{dt}A_2(p)^p + cD_{2,p} \le C(1+A_2(p)^p),
\tag{3.2}
$$

where the constant $C$ absorbs $\|\nabla^2\chi\|_\infty$ and all other
bounded-coefficient terms.  Gronwall gives

$$
A_2(p)^p(t) \le e^{Ct}\bigl(A_2(p)^p(0)+Ct\bigr),
\tag{3.3}
$$

which is finite because the initial metric is smooth on a compact manifold.

**No exact tensor cancellation is needed.** The mechanism is spatial
containment: (Q) has at most two cutoff derivatives, which is the correct
inductive level.  The IBP in Wang's Proposition 4.14 **reduces** the cutoff
derivative order of the $\Gamma_1$-type terms from $m+2$ to at most $m+1$,
and the remaining $m+1$ terms are further reduced by the triangle (7.3).
The single-$\chi$ coefficient is then bounded by $\chi \le 1$, which gives
the unweighted $L^p$ norm controlled by the induction.

## 4. Why dissipation absorption would be wrong

Attempting to absorb (Q) into $D_{2,p}$ by Young would require:

$$
\chi|\nabla^2\chi||\nabla^2 U|^p
\le \varepsilon\chi^2|\nabla^3 U|^2|\nabla^2 U|^{p-2}
+ C_\varepsilon\chi^{-?}|\nabla^2\chi|^?|\nabla^2 U|^?.
$$

The Young counter-term would involve a **negative power of $\chi$**, which
diverges on the transition.  This is exactly A03's observation.  The
correct treatment avoids this by bounding $\chi \le 1$ and using the
**unweighted** norm, not by absorbing into the **weighted** dissipation.

## 5. The $a\to a+\varepsilon$ regularization

A03 correctly observes that $a\to a+\varepsilon$ is not valid:

1. On $\{\chi=0\}$, the regularized flow $\partial_tg=-2\varepsilon(\operatorname{Ric}+g)$
   activates curvature evolution on the transition region, where the initial
   curvature is only $L^2$-bounded (from CGB/maximal function).

2. The a priori estimates derived with $a=\chi^2$ use $|\nabla a|^2/a = 4|\nabla\chi|^2$,
   which is well-defined and bounded at $\{a=0\}$ by continuous extension.
   Replacing $a$ by $a+\varepsilon$ would change this identity and introduce
   $\varepsilon$-dependent constants.

**The correct approach is Yang's:** derive all estimates directly for the
degenerate coefficient $a=\chi^2$.  The base estimate (Codex eq. 6.5) and
the induction (7.15) both hold for $a=\chi^2$ without regularization.  The
**existence** of the flow uses the DeTurck gauge and a separate mollification
construction whose limit inherits the degenerate estimates.

The Codex derivation (Sections 6--8) does **not** use $a+\varepsilon$.  The
estimates use:
- $|\nabla a|^2/a = 4|\nabla\chi|^2$ (bounded at $a=0$ by continuous extension)
- $D_m = \int\chi^2|\nabla^{m+1}U|^2|\nabla^m U|^{p-2}$ (degenerates at $a=0$)
- Unweighted norms $A_m(p) = \|\nabla^m U\|_{L^p}$ (include the transition)

The degenerate character is handled by the weight structure, not by regularization.

## 6. Kato regularization vs coefficient regularization

For the **Moser iteration** (Section 4 of my step31 note), the Kato
regularization $\Phi=(|\operatorname{Rm}|^2+\varepsilon)^{1/2}$ is valid because:
- It only smooths the pointwise norm $|\operatorname{Rm}|$
- It does not change the spatial cutoff $\chi$ or the coefficient $a$
- The limit $\varepsilon\to0$ preserves all estimates

This is distinct from the **coefficient regularization** $a\to a+\varepsilon$,
which changes the flow equation itself.

## 7. Connection to the Moser iteration

The continuation theorem (Codex Sections 6--8) requires the hypothesis

$$
\|U(t)\|_{L^\infty(M)} = \|a(\operatorname{Rm}+G)(t)\|_\infty \le K
\tag{7.1}
$$

on $[0,T)$.  Our Moser iteration (Step 31 note, Section 6) provides this:

$$
\|aF(t)\|_\infty \le C(S, K_0, \theta) \quad\text{on } [T/4, T].
$$

The smooth extension then produces $g(T)$ and allows restart, giving smooth
existence on $[0,T+\delta)$.  Since the Moser bootstrap closes for every
$T\le\theta r^2$, the flow exists smoothly on the full interval $[0,\theta r^2]$.

## 8. Summary of answers to A03

1. **Does an exact tensor contraction cancel the single-$\chi$ term?**  No.
   No exact cancellation is needed.  The term is bounded by $Cr^{-2}A_2(p)^p$
   (the unweighted $L^p$ norm), which enters the Gronwall RHS with a bounded
   coefficient.  This is the standard mechanism in Wang's Proposition 4.14.

2. **Is $a\to a+\varepsilon$ accepted?**  No.  The estimates use $a=\chi^2$
   directly.  Existence uses a separate DeTurck/mollification construction.

3. **Is a stronger weighted cutoff estimate needed?**  No.  The current
   framework with weighted dissipation $D_m$ and unweighted $A_m(p)$ is
   sufficient.  The induction controls $A_m(p)$ by Gronwall, and the
   dangerous IBP-reduced terms are bounded by the unweighted norm.
