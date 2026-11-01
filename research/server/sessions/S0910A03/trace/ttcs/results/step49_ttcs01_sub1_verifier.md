# TTCS Independent Branch Record

```json
{
  "step_id": 49,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step49_normalized_flow_existence_and_extension.md",
    "Sessions/S0910A03/workspace/notes/step49_corrected_restricted_theorem_statement.md",
    "Sessions/S0910A03/workspace/notes/step47_consolidated_negative_IL_gap_theorem.md"
  ]
}
```

## Task

Verify the mathematical correctness of the normalized cutoff Ricci flow existence and extension theorem in step49_normalized_flow_existence_and_extension.md. The flow equation is ∂_t g = -2χ²(Ric(g) + g), which differs from Yang's equation ∂_t g = -2χ²Ric by the zeroth-order term -2χ²g. The note claims:

1. The extra Christoffel variation from h = -2bg is -(δ^k_j ∂_i b + δ^k_i ∂_j b - g_ij ∇^k b) using ∇g=0. The curvature variation is -2bRm - g∧∇²b (Kulkarni-Nomizu product). Verify these formulas.

2. In the L^p energy evolution, the extra terms contribute: a dissipative -2p∫b|Rm|^p (favorable) and a source bounded by Cp·||∇²a||_∞·(∫|Rm|^p + Vol). The Grönwall coefficient is therefore ε-independent since ∇^k b_ε = ∇^k a for k≥1. Verify this is correct.

3. The coefficient-regularized existence (b_ε = χ²+ε² with ε>0) gives uniformly parabolic equations, and the ε-independent energy bounds give a common existence time T₀. The ε→0 passage uses interior C^k estimates on {χ>0}, vanishing drift on {χ=0}, and weighted estimates for regularity at ∂supp(χ). Verify this argument.

4. The extension criterion: bounded |χ²Rm| on [0,T*) implies smooth extension past T*, by adapting Wang's staggered induction. The normalization adds bounded lower-order terms at each level. Verify compatibility with Wang's framework.

5. The positive-time slab argument: if T* is a finite maximal time, the Moser endpoint |χ²Rm| ≤ Cγ/t is finite on [T*/2,T*), giving bounded |χ²Rm| there, so the extension criterion applies — contradiction. This resolves the issue that γ/t diverges at t=0 without needing a uniform bound on [0,T]. Verify this argument is sound.

Check for hidden assumptions, circular reasoning, or gaps. The note explicitly does NOT claim uniqueness, sequence-uniform estimates, or any result about Yau Problem 26.

## Output

# Scientific verification memo

## Overall assessment

The Christoffel variation is correct. With the curvature convention explicitly written in the note, the Hessian term in the covariant curvature variation has the opposite sign from (1.2)–(1.3). This sign does not affect the subsequent absolute-value energy estimate.

The normalization is indeed zeroth order in fixed coordinates and should be compatible with Yang’s and Wang’s methods. However, the supplied argument does not yet prove either the \(\varepsilon\to0\) existence theorem or the all-order extension theorem. The main mathematical issue is that covariant derivatives of the fixed cutoff are not fixed bounded tensors when the metric evolves. Several passages treat \(\nabla_g^k a\) as uniformly bounded solely because \(a\) is a fixed smooth function. The regularization passage also contains a nonintegrable \(t^{-1}\) estimate and an invalid inference from weighted regularity to smoothness across the zero-set interface.

The positive-time slab argument itself is correct once the extension theorem and the Moser estimate up to \(T^*\) are available.

---

## 1. Christoffel and curvature variations

Let \(h_{ij}=-2b g_{ij}\). The standard connection variation gives

\[
\dot\Gamma^k_{ij}
=\frac12g^{k\ell}
 \left(\nabla_i h_{j\ell}+\nabla_jh_{i\ell}-\nabla_\ell h_{ij}\right)
=-\left(\delta^k_j b_i+\delta^k_i b_j-g_{ij}b^k\right),
\]

so (1.1) is correct.

Using the convention stated in the note,

\[
\dot R^k{}_{\ell ij}
=\nabla_i\dot\Gamma^k_{j\ell}-\nabla_j\dot\Gamma^k_{i\ell},
\]

one obtains

\[
\dot R^k{}_{\ell ij}
=-\delta^k_jH_{i\ell}
 +g_{j\ell}H_i{}^k
 +\delta^k_iH_{j\ell}
 -g_{i\ell}H_j{}^k,
\qquad H=\nabla^2b.
\]

Lowering the first index also differentiates the metric:

\[
\boxed{
\dot R_{k\ell ij}
=-2bR_{k\ell ij}
+g_{ki}H_{j\ell}+g_{j\ell}H_{ik}
-g_{kj}H_{i\ell}-g_{i\ell}H_{jk}.
}
\]

Thus, with the standard Kulkarni–Nomizu convention,

\[
\boxed{\dot{\operatorname{Rm}}\big|_N
=-2b\,\operatorname{Rm}+g\owedge\nabla^2b.}
\]

Equations (1.2)–(1.3) have a minus sign in front of \(g\owedge\nabla^2b\), opposite to the result dictated by the convention written immediately before them. Since later estimates take the absolute value of this source, the sign error does not alter those inequalities.

There is also a derivative-order typo in (2.1): product expansion of the cutoff Ricci term produces a contribution of the form

\[
\nabla^2b * \operatorname{Ric},
\]

not \(\nabla^2b * \nabla\operatorname{Ric}\). The other first-derivative term is \(\nabla b*\nabla\operatorname{Ric}\).

---

## 2. Exact normalization contribution to the \(L^p\) energy

For the covariant \((0,4)\) curvature tensor, the term \(-2b\operatorname{Rm}\) alone contributes

\[
-2p\int b|\operatorname{Rm}|^p\,d\mu.
\]

That calculation in §2.2 is correct as an isolated tensor-variation contribution. It is not the net scaling contribution, because the four inverse metrics entering \(|\operatorname{Rm}|^2\) also vary.

Indeed, under \(h=-2bg\),

\[
\dot g^{-1}=2b g^{-1}.
\]

The four inverse factors contribute \(8b|\operatorname{Rm}|^2\), while
\(2\langle\operatorname{Rm},-2b\operatorname{Rm}\rangle\) contributes
\(-4b|\operatorname{Rm}|^2\). Hence

\[
\partial_t|\operatorname{Rm}|^p\big|_N
=2pb|\operatorname{Rm}|^p
+p|\operatorname{Rm}|^{p-2}
 \langle\operatorname{Rm},g\owedge\nabla^2b\rangle.
\]

Together with \(\dot d\mu=-nb\,d\mu\),

\[
\boxed{
\frac{d}{dt}E_p\Big|_N
=(2p-n)\int b|\operatorname{Rm}|^p\,d\mu
+p\int |\operatorname{Rm}|^{p-2}
 \langle\operatorname{Rm},g\owedge\nabla^2b\rangle\,d\mu .
}
\]

Thus the complete reaction is generally positive when \(p>n/2\), rather than dissipative. It is nevertheless harmless for an upper estimate because \(0\le b_\varepsilon\le2\).

If one already knows

\[
\sup_{\varepsilon,t}\|\nabla^2_{g_\varepsilon}a\|_\infty<\infty,
\]

then

\[
\left|
p\int |\operatorname{Rm}|^{p-2}
 \langle\operatorname{Rm},g\owedge\nabla^2a\rangle
\right|
\le C(n)p\|\nabla^2a\|_\infty
\left(E_p+\operatorname{Vol}\right).
\]

Consequently, the final upper-bound form in (2.2) is structurally correct.

The missing point is that

\[
\nabla^2_ga=\partial^2a-\Gamma(g)*\partial a
\]

depends on the evolving connection. Although

\[
\nabla^k_{g_\varepsilon}b_\varepsilon
=\nabla^k_{g_\varepsilon}a,\qquad k\ge1,
\]

holds for each \(\varepsilon\), it does not by itself give a uniform bound as \(\varepsilon\to0\). Such a bound must come from the coupled cutoff-jet estimates.

A related formula in §2.3 is incomplete:

\[
\partial_t(\nabla^m\operatorname{Rm})
\ne \nabla^m(\partial_t\operatorname{Rm})
\]

without connection commutators. The omitted normalization terms have the form

\[
\sum_{r=0}^{m-1}
\nabla^r(\dot\Gamma_N)*
\nabla^{m-1-r}\operatorname{Rm},
\qquad
\dot\Gamma_N\sim\nabla a.
\]

These remain lower order, but they must appear in the induction.

---

## 3. Coefficient regularization and the \(\varepsilon\to0\) passage

### 3.1 Per-\(\varepsilon\) parabolicity

For every fixed \(\varepsilon>0\),

\[
b_\varepsilon=a+\varepsilon^2\ge\varepsilon^2
\]

makes the DeTurck-gauged principal operator strictly parabolic. The term
\(-2b_\varepsilon g\) has no second derivatives of \(g\), so it does not alter the principal symbol. This part is correct.

Because the coefficient is an external scalar field, the DeTurck construction must transport it consistently under the gauge diffeomorphisms. The note mentions this but does not display the coupled system. Yang’s transported-coefficient construction is the relevant mechanism.

### 3.2 A common existence time does not follow from (2.2) alone

An \(L^p\) curvature Grönwall inequality by itself does not provide uniform fixed-coordinate \(C^{2,\alpha}\) control for a family whose ellipticity constants tend to zero. A complete argument needs Yang’s full regularization estimates, including uniform metric equivalence, cutoff jets, weighted curvature derivatives, and coordinate or DeTurck control.

Equations (4.2)–(4.3) are labeled “adapted,” but no derivation or source passage establishes the precise normalized versions. In particular, the extra \(C'(\chi)t\) term presupposes uniform control of \(\nabla^2_{g_\varepsilon}a\).

### 3.3 The metric-drift integral in (4.4) is invalid

The estimate written there contains

\[
\int_0^t \frac{C}{s}\,ds,
\]

which diverges. It therefore cannot imply metric equivalence for small \(t\), nor the later estimate \(C\sqrt t\). An integrable estimate such as \(Cs^{-\alpha}\) with \(\alpha<1\), or a uniform short-time bound beginning at \(t=0\), is needed.

### 3.4 The zero-set estimate loses the asserted \(\varepsilon^2\)

From (4.3), on \(\{\chi=0\}\),

\[
\varepsilon^2|\operatorname{Rm}_\varepsilon|
=|b_\varepsilon\operatorname{Rm}_\varepsilon|
\le \frac Ct.
\]

Hence

\[
|\operatorname{Rm}_\varepsilon|
\le \frac{C}{\varepsilon^2t},
\]

and therefore

\[
\varepsilon^2|\operatorname{Ric}_\varepsilon|
\le \frac{C}{t},
\]

not \(C\varepsilon^2/t\). The displayed estimate in §4.4 does not follow from the weighted Moser bound and gives no vanishing drift as \(\varepsilon\to0\).

### 3.5 Weighted regularity does not imply smooth gluing

The implication

\[
\nabla^m(a\operatorname{Rm})\in L^p\ \text{for all }m,p,
\quad
g=g_0\ \text{on }\{a=0\}
\quad\Longrightarrow\quad
g\in C^\infty
\]

is not valid without additional jet-matching information.

A scalar model is

\[
a(x)=
\begin{cases}
e^{-1/x^2},&x>0,\\
0,&x\le0,
\end{cases}
\qquad
u(x)=x_+.
\]

Then \(au\) extends smoothly and is flat at \(x=0\), while \(u\) is not \(C^1\). Thus a flat coefficient can hide a mismatch of unweighted derivatives. Uniform fixed-coordinate estimates for \(g_\varepsilon\), or direct control of all connection jets across the zero-set frontier, are needed.

The diagonal convergence on compact subsets of \(\{\chi>0\}\) is valid once (4.5) is established, but it gives no such matching by itself. Similarly, \(C^0\) convergence to \(g_0\) at \(t=0\) would not establish a smooth family on \(M\times[0,T_0]\).

Therefore §4, as written, does not prove Theorem 4.1. The theorem remains mathematically plausible through a complete adaptation of Yang’s direct degenerate DeTurck construction, since the added term is semilinear, but that adaptation is not present here.

---

## 4. Extension under bounded weighted curvature

Assume an exact smooth solution exists on \([0,T^*)\) and

\[
\sup_{M\times[0,T^*)}|a\operatorname{Rm}|\le K.
\]

The metric-equivalence step is sound and can be written directly as

\[
|\partial_tg|_g
\le 2|a\operatorname{Ric}|_g+2|ag|_g
\le C_nK+2\sqrt n.
\]

Consequently,

\[
e^{-C(K+1)t}g_0\le g(t)\le e^{C(K+1)t}g_0.
\]

No division by a positive lower bound for \(\chi\) is needed.

At the structural level, the normalization is compatible with Wang’s method:

* \(\dot\Gamma_N\sim\nabla a\);
* \(\dot{\operatorname{Rm}}_N=-2a\operatorname{Rm}+g\owedge\nabla^2a\);
* differentiated terms are linear in current or lower curvature derivatives and in cutoff jets.

However, they are not simply fixed bounded sources. For example,

\[
\nabla^m\!\left[a(g\owedge\nabla^2a)\right]
\supset a\,g\owedge\nabla^{m+2}a.
\]

This must be coupled to the cutoff-jet part of Wang’s staggered induction. The omitted time-connection commutators must also be included. The companion `step49_corrected_restricted_theorem_statement.md`, §6 item 1, explicitly records that the arbitrary-order tensor induction has not been fully carried through.

Finally, uniform covariant curvature bounds and Sobolev embedding do not immediately yield fixed-coordinate \(C^k\) bounds for the metric. Wang’s endpoint construction, or corresponding DeTurck/connection-difference estimates, is needed to produce a smooth metric \(g(T^*)\).

Thus the added normalization is analytically compatible with Wang’s framework, but Theorem 5.1 is not fully derived in this note.

---

## 5. Positive-time slab continuation

This argument is correct under two premises:

1. the Moser estimate
   \[
   |a\operatorname{Rm}(t)|\le C\gamma/t
   \]
   holds for every \(0<t<T^*\) with the same constants;
2. the extension theorem from §5 is available.

Smoothness on the compact early slab gives

\[
K_{\mathrm{early}}
=\sup_{M\times[0,T^*/2]}|a\operatorname{Rm}|<\infty.
\]

On the late slab,

\[
\sup_{M\times[T^*/2,T^*)}|a\operatorname{Rm}|
\le \frac{2C\gamma}{T^*}<\infty.
\]

Combining them produces a finite bound on all of \([0,T^*)\). Dependence on \(T^*\) is immaterial; the extension theorem only needs finiteness for this particular solution. Hence the divergence of \(C\gamma/t\) at \(t=0\) creates no problem.

When the Moser estimate is obtained inside a first-exit bootstrap, its hypotheses must remain valid for every \(t<T^*\). Subject to that standard local-in-time use, there is no circularity in the slab reasoning.

## Final scientific status

* Christoffel formula: correct.
* Curvature formula: Hessian sign reversed under the convention stated in the note.
* \(L^p\) upper-bound structure: compatible after cutoff-jet control, but the full normalization reaction is \((2p-n)b|\operatorname{Rm}|^p\), not dissipative in general.
* Regularized \(\varepsilon\to0\) construction: not established by the supplied estimates; (4.4), the zero-set drift, and the smooth-gluing inference are invalid.
* Wang-type extension: normalization is structurally lower order, but the all-order coupled induction and fixed-coordinate endpoint control are absent.
* Positive-time slab: mathematically sound once the preceding extension theorem and the Moser estimate up to \(T^*\) are available.