# TTCS Independent Branch Record

```json
{
  "step_id": 51,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step51_normalized_yang_precise_estimate.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Independently verify the precise L^p curvature energy estimate for the normalized cutoff flow ∂_tg = -2χ²(Ric+g). The note claims three specific things: (1) The conformal variation of |Rm|²_g under h₂ = -2ag gives +4a|Rm|² - 2⟨Rm, g∧∇²a⟩, where the +4a comes from the metric-inverse variation (4 factors of g^{-1}, each contributing +2a, minus 4a from the tensor inner product -2a|Rm|²). (2) Combined with the volume evolution ∂_t dμ = -a(s+n)dμ, the net normalization addition to d/dt ∫|Rm|^p is (2p-n)∫a|Rm|^p + bounded source. (3) At the critical exponent p=n/2, the reaction coefficient (2·n/2 - n) = 0 vanishes exactly. Check the sign conventions, count the g^{-1} factors, verify the Kulkarni-Nomizu trace, and confirm that Yang's Theorem A.7 Moser iteration is structurally compatible with the modified inequality (bounded Grönwall coefficient at supercritical p, bounded source from g∧∇²a). Read Yang's Theorem A.7 display and the conformal variation formula.

## Output

# Scientific verification memo

## 1. Conformal variation and inverse-metric count

Put \(a=\chi^{2}\) and consider only

\[
\dot g=h_{2}=-2ag.
\]

Write \(h_{2}=2\dot u\,g\), so \(\dot u=-a\). With the Hamilton/Yang curvature convention, the infinitesimal conformal formula for the fully covariant tensor is

\[
\dot R_{ijkl}
=
2\dot u\,R_{ijkl}
-(g\owedge\nabla^{2}\dot u)_{ijkl}.
\]

Consequently,

\[
\boxed{\dot R_{ijkl}\big|_{h_2}
=-2aR_{ijkl}+(g\owedge\nabla^{2}a)_{ijkl}.}
\]

Thus the source sign in equations (1.2) and (1.4) of the note is reversed. A flat two-dimensional test fixes the sign: for

\[
g(t)=e^{-2ta}(dx^{2}+dy^{2}),
\]

one has \(\dot R_{1212}=\Delta a\), while

\[
(g\owedge\nabla^{2}a)_{1212}=a_{11}+a_{22}=\Delta a.
\]

The algebraic reaction coefficient is nevertheless exactly as stated. Since

\[
|{\rm Rm}|^{2}
=g^{ia}g^{jb}g^{kc}g^{ld}R_{ijkl}R_{abcd},
\qquad
\dot g^{ij}=2ag^{ij},
\]

the four inverse metrics contribute

\[
4(2a)|{\rm Rm}|^{2}=8a|{\rm Rm}|^{2}.
\]

The two curvature tensors contribute

\[
2\langle {\rm Rm},-2a{\rm Rm}\rangle=-4a|{\rm Rm}|^{2}.
\]

Therefore

\[
\boxed{
\partial_t|{\rm Rm}|^{2}\big|_{h_2}
=
4a|{\rm Rm}|^{2}
+
2\langle {\rm Rm},g\owedge\nabla^{2}a\rangle .
}
\]

The \(+4a|{\rm Rm}|^{2}\) coefficient is fully verified; only the sign of the Hessian source differs from the note.

## 2. Kulkarni–Nomizu contraction

For the displayed convention

\[
(g\owedge H)_{ijkl}
=g_{ik}H_{jl}-g_{il}H_{jk}-g_{jk}H_{il}+g_{jl}H_{ik},
\]

direct contraction gives

\[
g^{ik}(g\owedge H)_{ijkl}
=(n-2)H_{jl}+(\operatorname{tr}H)g_{jl},
\]

and

\[
\boxed{\langle {\rm Rm},g\owedge H\rangle
=4\langle {\rm Ric},H\rangle.}
\]

Hence the exact source in the norm-square evolution is

\[
2\langle {\rm Rm},g\owedge\nabla^{2}a\rangle
=8\langle {\rm Ric},\nabla^{2}a\rangle.
\]

Its absolute-value estimate is

\[
\big|\langle {\rm Rm},g\owedge\nabla^{2}a\rangle\big|
\le C_{n}|{\rm Rm}|\,|\nabla^{2}a|.
\]

The source sign has no effect on this estimate.

The same contraction also gives

\[
\dot{\rm Ric}\big|_{h_2}
=(n-2)\nabla^{2}a+(\Delta a)g.
\]

For spatially constant \(a\), the covariant Ricci tensor is unchanged, while its norm grows according to \(\partial_t|{\rm Ric}|=2a|{\rm Ric}|\). Thus the statement in §4.1 that normalization contributes a dissipative \(-2a|{\rm Ric}|\) is inconsistent with constant metric scaling.

## 3. Volume and \(L^{p}\) energy

The general volume formula is

\[
\partial_t d\mu=\frac12\operatorname{tr}_{g}(\dot g)\,d\mu.
\]

For the full normalized cutoff flow,

\[
\operatorname{tr}_{g}\dot g=-2a(s+n),
\]

so

\[
\boxed{\partial_t d\mu=-a(s+n)d\mu.}
\]

Relative to Yang’s unnormalized flow, the normalization adds exactly

\[
-na\,d\mu.
\]

Equation (1.5) and the final table in the note display the opposite volume sign, whereas the recalculation in §2.3 uses the correct one.

Let \(F=|{\rm Rm}|\) and \(E_p=\int F^{p}d\mu\). The normalization-only addition is

\[
\begin{aligned}
\dot E_p\big|_{\rm norm}
&=
\frac p2\int F^{p-2}
\left(4aF^{2}
+2\langle {\rm Rm},g\owedge\nabla^{2}a\rangle\right)d\mu
-n\int aF^{p}d\mu\\
&=
\boxed{
(2p-n)\int aF^{p}d\mu
+
p\int F^{p-2}
\langle {\rm Rm},g\owedge\nabla^{2}a\rangle d\mu .
}
\end{aligned}
\]

With the alternative curvature-tensor convention, the last integral changes sign, but the coefficient \(2p-n\) is unchanged.

A useful independent test is constant \(a\). Then \(g(t)=e^{-2at}g(0)\),

\[
F(t)^{p}d\mu_{g(t)}
=e^{(2p-n)at}F(0)^{p}d\mu_{g(0)},
\]

which reproduces the coefficient exactly.

Therefore, at \(p=n/2\),

\[
\boxed{2p-n=0.}
\]

The reaction cancellation is exact and expresses the conformal scaling invariance of the critical curvature energy under spatially constant rescaling.

## 4. Size of the Hessian source

Using the preceding contraction,

\[
\left|
p\int F^{p-2}
\langle {\rm Rm},g\owedge\nabla^{2}a\rangle
\right|
\le C_{n,p}\int |\nabla^{2}a|F^{p-1}.
\]

Young’s inequality gives the more precise form

\[
C_{n,p}|\nabla^{2}a|F^{p-1}
\le
\varepsilon F^{p}
+
C_{n,p,\varepsilon}|\nabla^{2}a|^{p}.
\]

Thus at the critical exponent,

\[
\dot E_{n/2}
\le
C E_{n/2}
+
C_{\varepsilon}
\int |\nabla^{2}a|^{n/2}d\mu,
\]

and consequently

\[
E_{n/2}(t)
\le
e^{Ct}
\left[
E_{n/2}(0)
+
C_{\varepsilon}
\int_{0}^{t}\!\!\int
|\nabla^{2}a|^{n/2}\,d\mu\,ds
\right].
\]

Replacing the last integral by \(C_{\varepsilon}\operatorname{Vol}\,t\) requires a uniform \(L^\infty\) bound for \(\nabla^{2}a\). Bilipschitz control alone controls \(|\nabla a|\) and the measure, but not the evolving Hessian, since \(\nabla^{2}_{g(t)}a\) contains the evolving connection.

## 5. Comparison with Yang’s Theorem A.7

Yang’s printed Theorem A.7 assumes the homogeneous scalar inequality

\[
\partial_t f
\le
\chi^{2}(\Delta f+c_{0}f^{2})
+2A\chi|\nabla\chi||\nabla f|
+B\bigl(|\nabla\chi|^{2}-\chi\Delta\chi\bigr)f,
\]

together with

\[
\partial_t d\mu\le c\chi^{2}f\,d\mu.
\]

For the normalized flow:

1. **Volume term.** Since
   \[
   -a(s+n)\le a|s|\le C_n aF,
   \]
   Yang’s volume upper inequality remains available.

2. **Reaction term.** At supercritical levels,
   \[
   (2p-n)\int aF^{p}\le (2p-n)\int F^{p}.
   \]
   This is a bounded zeroth-order coefficient growing linearly in \(p\). Such polynomial growth is compatible with Lemmas A.5–A.6 because \(p_k\) grows geometrically and the \(p_k\)-th roots produce convergent exponent sums.

3. **Hessian source.** The term
   \[
   C|\nabla^{2}a|
   \]
   in the scalar curvature inequality is additive rather than proportional to \(F\). It is not present in Theorem A.7 as printed. At the energy levels it produces
   \[
   C_{\varepsilon}\int|\nabla^{2}a|^{p_k},
   \]
   in addition to the homogeneous Moser recurrence.

A quantity such as \(C^{p_k}\operatorname{Vol}\), after taking the \(p_k\)-th root, tends to \(C\), not to zero. In particular, when the preceding curvature energy is small, a fixed additive term dominates rather than becoming subordinate to its \(1+2/n\) power. An inhomogeneous Moser argument can still converge, but its pointwise estimate contains an additive forcing contribution, and the critical bootstrap requires a spacetime bound for

\[
\int |\nabla^{2}a|^{n/2}.
\]

Merely replacing Yang’s dimensional smallness constant by a slightly smaller dimensional constant does not control this source for arbitrary cutoff geometry and volume.

A homogeneous alternative is suggested by the shifted curvature tensor

\[
T={\rm Rm}+\mathcal G,
\qquad
\mathcal G=\frac{1}{2(n-1)}\,g\owedge g,
\]

for which \({\rm Ric}(\mathcal G)=g\) and hence

\[
\partial_tg=-2a\,{\rm Ric}(T).
\]

This formulation removes a curvature source independent of \(T\), though its critical hypothesis naturally concerns \(\int|T|^{n/2}\), not \(\int|{\rm Rm}|^{n/2}\).

Finally, Yang’s Appendix A uses the \(2n/(n-2)\) Sobolev inequality and Lemma A.3 with exponent \(p>1\). The supplied citation therefore supports \(n\ge3\); dimension \(n=2\) requires a separate two-dimensional Moser formulation.

## Summary

- The four inverse metrics contribute \(+8aF^{2}\), the two tensor copies contribute \(-4aF^{2}\), and the resulting \(+4aF^{2}\) reaction is correct.
- The normalization-only energy coefficient is exactly \(2p-n\).
- Its value at \(p=n/2\) is exactly zero.
- Under Yang’s curvature convention, the Hessian source signs in (1.2) and (1.4) should be plus rather than minus.
- The source contracts as \(4\langle{\rm Ric},\nabla^{2}a\rangle\).
- Yang’s iteration readily accommodates the supercritical linear reaction, but Theorem A.7 as printed does not contain the additive Hessian forcing. The asserted normalized existence theorem therefore needs an inhomogeneous source estimate with explicit cutoff-dependent spacetime control, or a homogeneous shifted-curvature formulation.