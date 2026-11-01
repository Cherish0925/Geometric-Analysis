# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 32,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step32_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step32_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

For the four-dimensional normalized cutoff flow route toward the Ishida-LeBrun negative Ricci-pinching gap, critically verify the two remaining analytic points, using the supplied files rather than assuming the previous synthesis. (1) Moser: keep the valid mixed-weight identity H_{3p/2} <= H_p^{1/2}||z_p||_4^2, but check that the correct nested-time recurrence follows only from the direct spacetime interpolation int_I H_{3p/2} <= (sup_I H_p)^{1/2} S int_I(|nabla z_p|^2+r^{-2}H_p); identify exactly what upstream estimates (H3/Y, J6, Q, same-support bootstrap) are still needed. (2) Continuation: inspect the m=2 version of Codex equations (6.11)-(6.13), where a term schematically looks like int chi |nabla^2 chi| |nabla^2 U|^p. Decide whether the exact Wang grouped integrations cancel/replace this single-chi term, whether an available weighted Sobolev estimate controls it, or whether the induction must be changed. Also comment on why replacing a by a+epsilon is not automatically harmless when outside supports have uncontrolled curvature. Return a direct mathematical memo naming valid pieces, invalid steps, and the sharp next proof obligation; do not decide final writing readiness.

## Integrated Scientific Memo

# Direct verification memo: 4D normalized cutoff flow, weighted Moser and continuation gaps

## 1. Weighted Moser: what is valid, what must be corrected

Use the notation
\[
H_p(f)=\int \eta^2 a^{p-2}f^p,\qquad 
z_p=\eta\,a^{(p-1)/2}f^{p/2},\qquad a=\chi^2 ,
\]
with \(\eta\) an auxiliary spatial cutoff supported in the same macro-component/nested collar. Ignore \(\eta\)-gradient terms below; they add the same \(r^{-2}H_p\)-type errors if \(\operatorname{supp}\nabla\eta\) is placed in the controlled collar.

### 1.1 The mixed-weight identity is correct

The relevant identity is not \(\|z_p\|_3^3\). One has
\[
z_p^2=a^{p-1}f^p,\qquad
(a^{p-2}f^p)^{1/2}=a^{(p-2)/2}f^{p/2},
\]
and hence
\[
(a^{p-2}f^p)^{1/2}z_p^2
=a^{(p-2)/2+p-1}f^{3p/2}
=a^{3p/2-2}f^{3p/2}.
\]
Therefore
\[
\boxed{\;
H_{3p/2}(f)
\le H_p(f)^{1/2}\,\|z_p\|_4^2 .
\;}
\]
This resolves the half-power objection: \(\|z_p\|_3^3\) has \(a\)-exponent \(3(p-1)/2=3p/2-3/2\), which is too large by \(1/2\), and is the wrong quantity.

### 1.2 The gradient estimate is valid for curvature, but must be restated for defect

For \(f=F=(1+|\mathrm{Rm}|^2)^{1/2}\),
\[
\nabla z_p
=\frac{p-1}{2}a^{(p-3)/2}\nabla a\,F^{p/2}
+\frac p2 a^{(p-1)/2}F^{p/2-1}\nabla F .
\]
Since \(a=\chi^2\),
\[
a^{p-3}|\nabla a|^2
=4a^{p-2}|\nabla\chi|^2
\le Cr^{-2}a^{p-2},
\]
and \(|\nabla F|\le |\nabla\mathrm{Rm}|\). Thus
\[
\boxed{\;
\|\nabla z_p\|_2^2
\le Cp^2\bigl(D_p+r^{-2}H_p\bigr),
\qquad
D_p=\int \eta^2 a^{p-1}F^{p-2}|\nabla\mathrm{Rm}|^2 .
\;}
\]
No lower bound for \(a\) is used.

For \(f=|E|\), this must not be justified by the displayed \(F\)-argument. The defect iteration needs its own regularized norm, weak Kato inequality, and dissipation
\[
D_p^E=\int \eta^2a^{p-1}|E|^{p-2}|\nabla E|^2 .
\]
The scalar statement is plausible in the homogeneous \(E\)-equation, but it is a separate upstream estimate, not supplied by the curvature gradient calculation.

### 1.3 The correct Sobolev-to-recurrence step is spacetime interpolation, not \(\int H_{2p}\) or \(\sup H_{2p}\)

In dimension four the usable Sobolev form is
\[
\|u\|_4^2
\le S\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),
\]
with \(S\) the local/collapse-adapted constant in whatever normalization is fixed. The Step 31 note’s Ladyzhenskaya-style product
\[
\int u^4\lesssim \left(\int|\nabla u|^2\right)\left(\int u^2\right)+\cdots
\]
is not the right four-dimensional Sobolev input for this recurrence.

Since \(\|z_p\|_2^2\le H_p\),
\[
\|z_p\|_4^2
\le S\bigl(\|\nabla z_p\|_2^2+r^{-2}H_p\bigr).
\]
Combining with the mixed identity gives the direct spacetime estimate
\[
\boxed{\;
\int_I H_{3p/2}
\le
(\sup_I H_p)^{1/2}\,
S\int_I\bigl(\|\nabla z_p\|_2^2+r^{-2}H_p\bigr)
\;}
\]
and hence, for curvature,
\[
\boxed{\;
\int_I H_{3p/2}
\le
Cp^2S(\sup_IH_p)^{1/2}
\int_I(D_p+r^{-2}H_p).
\;}
\]

This is the sharp correction. The recurrence does **not** follow from first bounding \(\int_I H_{2p}\), \(\int_IK_{2p}\), or \(\sup_IK_{2p}\) by the displayed Sobolev inequality. The valid iteration advances through \(\int_I H_{3p/2}\).

A correct nested-time version must have the form
\[
\sup_{I_{k+1}}H_{p_k}
+\int_{I_{k+1}}\bigl(D_{p_k}+r^{-2}H_{p_k}\bigr)
\le
C p_k^N L_k\int_{I_k}H_{p_k},
\]
with \(p_{k+1}=3p_k/2\), \(I_{k+1}\Subset I_k\), and \(L_k\) containing only dyadic time-cutoff losses, \(r^{-2}\), and already-controlled reaction coefficients. Then
\[
\int_{I_{k+1}}H_{p_{k+1}}
\le
C p_k^N S\,L_k^{3/2}
\left(\int_{I_k}H_{p_k}\right)^{3/2},
\]
up to harmless changes in the polynomial \(p_k\)-loss depending on how the energy inequality is normalized. Since \(p_k\sim(3/2)^k\), polynomial \(p_k\)-loss and dyadic \(2^k\)-loss are compatible with the usual Moser product.

### 1.4 Reaction weights: the \(a^{p-1}\) weight is essential

For curvature the reaction must be retained as
\[
R_p=\int \eta^2 a^{p-1}F^{p+1}.
\]
Replacing it by the larger
\[
\int \eta^2a^{p-2}F^{p+1}
\]
is not harmless: the later Hölder factorization produces the \(a^{p-1}\) weight and does not control the lighter \(a^{p-2}\) integrand near \(\{a=0\}\).

A usable decomposition, appearing in the Codex memo, is
\[
\eta^2a^{p-1}Ff^p
=(aF^3)^{1/3}(\eta^2a^{p-2}f^p)^{1/3}z_p^{4/3},
\]
which leads, after Hölder, Sobolev, and Young, to
\[
R_p
\le
\varepsilon\bigl(D_p+r^{-2}H_p\bigr)
+
C_\varepsilon p^N S^2Y\,H_p,
\qquad
Y=\int_{\operatorname{same\ support}}aF^3 .
\]
Thus high-\(p\) energy becomes
\[
H_p'+cD_p
\le
Cp^N(r^{-2}+S^2Y)H_p,
\]
provided \(S^2Y\) is controlled on the same support and time interval.

### 1.5 Endpoint is \(\|af\|_\infty\)

If the recurrence closes,
\[
H_p^{1/p}
=
\|\eta^{2/p}a^{1-2/p}f\|_{L^p}
\longrightarrow
\|af\|_\infty
\]
on the active region. The endpoint is \(\|aF\|_\infty\), not \(\|a^{1/2}F\|_\infty\). This is exactly the weighted pointwise curvature quantity needed on the plateau \(a=1\).

## 2. Upstream estimates still required for the Moser route

The interpolation engine is valid, but it consumes several inputs not proved by the interpolation identity itself.

1. **Same-support critical \(H_2\to H_3/Y\) seed.**  
   The \(p=2\) absorption should read
   \[
   H_3
   \le H_2^{1/2}H_4^{1/2}
   \le CSH_2^{1/2}(D_2+r^{-2}H_2).
   \]
   The small parameter is
   \[
   \gamma=SH_2^{1/2}.
   \]
   One needs the good-center/maximal-function estimate and the collapse-adapted Sobolev constant on the same component to make \(\gamma\) small or bounded in the required way. The later recurrence also needs a positive-time same-support bound such as
   \[
   S^2Y(s)\lesssim \beta^3/s
   \]
   or an equivalent integrable coefficient estimate.

2. **Propagated \(p_0=3\) curvature seed.**  
   Starting the recurrence at \(p_0=3\) requires a same-support \(\int_{t/2}^tH_3\) or pointwise-in-time \(H_3\) bound after the good-slice/propagation argument. This must be written using the corrected spacetime recurrence, not a false \(\sup H_{2p}\) step.

3. **Defect \(J_6\) persistence.**  
   For \(f=|E|\), the endpoint starts at \(p_0=6\):
   \[
   J_6=H_6(|E|)=\int \eta^2a^4|E|^6.
   \]
   The route needs same-support persistence of \(J_6\), with the homogeneous defect equation and curvature coefficient controlled by \(|aF|\). The \(E=0\) regularization/Kato step must be included.

4. **Global \(Q\) evolution.**  
   The scalar Moser recurrence does not itself need
   \[
   Q=\int_M|E|^2,
   \]
   but the later terminal density/defect bridge does. The needed input is a homogeneous estimate
   \[
   Q(t)\le e^{C\theta}Q(0)
   \]
   compatible with the metric-comparison bootstrap.

5. **Same-support bootstrap and moving Sobolev constants.**  
   \(H_2\), \(Y\), \(J_6\), the local Sobolev constant, volume comparison, and the auxiliary cutoffs must all refer to the same macro-support/nested collars. Metric drift from the eventual \(|aE|\) bound must preserve the Sobolev and volume constants up to the first-exit time. Without this support alignment, the volume cancellations in the curvature and defect endpoints are not justified.

Thus: the half-weight Moser objection is repaired, but the complete Moser closure still requires these upstream estimates in corrected nested-time form.

## 3. Continuation: the \(m=2\) single-\(\chi\) term

Let
\[
U=a(\mathrm{Rm}+G),\qquad W_m=\nabla^mU,\qquad P_p(W_m)=|W_m|^{p-2}W_m,
\]
and consider the differentiated \(U\)-equation. The high cutoff terms have schematic form
\[
\Gamma_1=\chi\nabla^{m+2}\chi*U,\quad
\Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,
\]
\[
\Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,\quad
\Gamma_4=\chi\nabla\chi*\nabla W_m .
\]
The source paper’s local Ricci flow Proposition 4.14 indeed groups \(\Gamma_1,\Gamma_2,\Gamma_3\) and, after integration by parts, leaves an exceptional term of type
\[
\int |\nabla^m(\chi^2\mathrm{Rm})|^{p-2}
\left\langle
\nabla^m(\chi^2\mathrm{Rm}),
\nabla^2\chi*\nabla^m\chi*\chi^2\mathrm{Rm}
\right\rangle,
\]
which is soft because \(\chi^2\mathrm{Rm}\) is the bounded weighted curvature factor.

However, the Codex equations (6.11)–(6.13) for the shifted \(U\)-calculation contain, after integrating one derivative off \(\nabla^{m+1}\chi\), the descendant
\[
-\int P_p(W_m)*\chi\nabla^m\chi*\nabla^2U .
\]
For \(m=2\), this is schematically
\[
\boxed{\;
I=\int \chi\,|\nabla^2\chi|\,|\nabla^2U|^p .
\;}
\]
This is not controlled by plain Hölder from \(\nabla^2\chi\in L^q\) and \(W_2=\nabla^2U\in L^p\); plain Hölder would require \(\nabla^2\chi\in L^\infty\), which is not available in the coupled induction at that point.

### 3.1 Does Wang’s grouped integration cancel or replace it?

From the supplied Wang source alone, the grouped local-Ricci-flow identity replaces the dangerous group by the softer residual above. But the normalized shifted \(U\)-Codex file does **not** provide the coefficient-level grouped identity showing that the same replacement occurs after passing to \(U=a(\mathrm{Rm}+G)\). The displayed Codex expansion instead leaves the single-\(\chi\) term.

Therefore, for the supplied material, one should **not** claim that Wang’s grouped integrations automatically cancel this term in the shifted normalized equation. There are two possible proof paths:

1. write the exact grouped identity for the shifted \(U\)-equation and prove that the Wang residual is indeed the only survivor; or  
2. keep the single-\(\chi\) term and estimate it directly.

The second path is available in dimension four.

### 3.2 The \(m=2\) term is controlled by weighted Sobolev

Set
\[
W=\nabla^2U,\qquad B=\nabla^2\chi,\qquad
X_p=\int |W|^p,
\]
\[
D_p=\int \chi^2|\nabla W|^2|W|^{p-2}.
\]
Let
\[
u=\chi |W|^{p/2}.
\]
Then
\[
\|\nabla u\|_2^2
\le
C\|\nabla\chi\|_\infty^2X_p+Cp^2D_p,
\]
and the four-dimensional Sobolev estimate gives
\[
\|u\|_4^2
\le
CS\bigl(p^2D_p+(1+r^{-2})X_p\bigr).
\]
Now use Hölder with exponents \((4,4,2)\):
\[
\begin{aligned}
I
&=\int |B|\,u\,|W|^{p/2} \\
&\le \|B\|_4\,\|u\|_4\,\|W\|_p^{p/2} \\
&\le
CS^{1/2}\|B\|_4 X_p^{1/2}
\bigl(p^2D_p+(1+r^{-2})X_p\bigr)^{1/2}.
\end{aligned}
\]
Young’s inequality yields
\[
\boxed{\;
I
\le
\varepsilon D_p
+
C_\varepsilon p^2S\,\| \nabla^2\chi\|_4^2(1+r^{-2})X_p .
\;}
\]
This has the desired Grönwall form because \(\|\nabla^2\chi\|_4\) is supplied by the previous base coupled level \((\nabla U,\nabla^2\chi)\). No \(\|\nabla^2\chi\|_\infty\) is needed.

For \(m\ge3\), the analogous \(\nabla^2U\) factor is lower order and can be treated using earlier higher-integrability/Sobolev bounds; \(m=2\) is the uniquely delicate case.

### 3.3 Consequence for the induction

The induction need not be redesigned solely because of this \(m=2\) term. But the written Codex justification “for \(m=2\), it is a coefficient times \(\chi|W_2|^p\)” is insufficient unless it is replaced by the weighted Sobolev estimate above or by a fully written shifted Wang grouped identity.

The full continuation theorem is still not closed by this one estimate alone. One must still provide term-by-term estimates for all products in the coupled pair
\[
(\nabla^mU,\nabla^{m+1}\chi),
\]
including products involving \(\nabla^{m+1}\chi*\nabla U*|W_m|^{p-1}\), commutators from the evolving connection, moving norms/measure, and \(G\)-linear normalization terms. The derivative-counting formula for the fixed scalar cutoff is correct:
\[
\partial_t\nabla^{m+1}\chi
=
\nabla^mU*\nabla\chi+\text{lower-order products},
\]
so there is no hidden \(\nabla^{m+1}U\) in the cutoff equation; the issue is estimates, not derivative count.

## 4. Why \(a\mapsto a+\varepsilon\) is not automatically harmless

Replacing \(a=\chi^2\) by
\[
a_\varepsilon=a+\varepsilon
\]
makes the equation strictly parabolic, but changes the geometric problem on \(\{a=0\}\). In the intended degenerate flow,
\[
\partial_tg=-2aE,
\]
the exterior where \(a=0\) is stationary. The weighted variable
\[
U=a(\mathrm{Rm}+G)
\]
vanishes there, so no exterior curvature bound is required.

For \(a_\varepsilon\),
\[
U_\varepsilon=(a+\varepsilon)(\mathrm{Rm}+G)
=\varepsilon(\mathrm{Rm}+G)
\quad\text{on }\{a=0\},
\]
and the metric evolves there by
\[
\partial_tg_\varepsilon=-2\varepsilon E.
\]
If the exterior curvature is uncontrolled—as it is meant to be in this cutoff route—then neither
\[
\varepsilon |\mathrm{Rm}|,\qquad
\varepsilon |\mathrm{Rm}|^2,\qquad
\varepsilon\nabla^k\mathrm{Rm}
\]
nor the corresponding reaction terms are uniformly bounded independently of \(\varepsilon\). For fixed \(\varepsilon>0\), the exterior is no longer frozen and can contribute curvature growth or singular behavior not seen by the weighted estimates on the macro-supports.

Thus strict parabolic regularization can be used only after proving uniform-in-\(\varepsilon\) estimates independent of exterior curvature, or after imposing exterior controls. The supplied files do not contain such an argument. The safer route is to invoke/prove Yang-type degenerate local Ricci flow existence directly for the fixed cutoff, with the normalization term \(-2\chi^2g\) treated as a zeroth-order addition, rather than relying on \(a+\varepsilon\) as automatically standard.

## 5. Sharp next proof obligations

### Moser side

Prove the corrected same-support nested recurrence:
\[
\sup_{I_{k+1}}H_{p_k}
+\int_{I_{k+1}}\bigl(D_{p_k}+r^{-2}H_{p_k}\bigr)
\le
C p_k^N L_k\int_{I_k}H_{p_k},
\]
where \(L_k\) uses only dyadic time losses, \(r^{-2}\), and established same-support \(Y\)-bounds. This must be coupled to:

- the \(H_2\to H_3\) absorption with \(\gamma=SH_2^{1/2}\);
- a propagated same-support curvature seed \(Y=H_3(F)\);
- the defect \(J_6\) persistence with correct \(E\)-dissipation/Kato regularization;
- global \(Q\) evolution for the later density bridge;
- preservation of the collapse-adapted Sobolev constant under the metric-comparison bootstrap.

### Continuation side

Either:

1. write the exact shifted normalized analogue of Wang’s grouped integration showing the single-\(\chi\) \(m=2\) term is replaced by the softer Wang residual; or  
2. retain that term and insert the four-dimensional weighted Sobolev estimate above.

Then complete the full coupled \((\nabla^mU,\nabla^{m+1}\chi)\) term-by-term Grönwall proof. Do not rely on \(a+\varepsilon\) unless a uniform exterior-curvature-independent approximation theorem is proved.