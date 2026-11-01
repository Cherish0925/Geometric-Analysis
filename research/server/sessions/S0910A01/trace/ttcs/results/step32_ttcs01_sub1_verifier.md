# TTCS Independent Branch Record

```json
{
  "step_id": 32,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step32_nested_moser_and_tensor_audit.md",
    "Sessions/S0910A01/workspace/scripts/step32_nested_moser_repair.py",
    "Sessions/S0910A03/workspace/notes/step32_preceptor_analytic_review.md",
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step31_general_p_tensor_power_inequality.md",
    "Sessions/S0910A01/workspace/notes/step31_m2_continuation_analysis.md"
  ]
}
```

## Task

Verify the Step 32 corrected analytic calculations for the four-dimensional normalized cutoff-flow route toward the Ishida--LeBrun negative Ricci-pinching gap. Focus only on two mathematical points. (1) In the fixed convention ||z||_4^2 <= C_S(||grad z||_2^2+r^{-2}||z||_2^2), beta=C_S H_2(0)^{1/2}, check the nested-time recurrence derived from H_{3p/2}<=H_p^{1/2}||z_p||_4^2: integral recurrence, exponent sums, no division by L_k^{1/2}, endpoint ||af(t)||_inf <= C C_S^{2/p0} t^{-3/p0}(int_{t/2}^t H_{p0})^{1/p0}, and the curvature/defect cancellations giving beta/t and delta(r^2/t)^{1/3} under the stated conditional seeds. Also check the collapsed flat product counterexample to a volume-independent unnormalized Dirichlet constant. (2) Check the tensor audit: Step 31 general-p curvature derivation is not a completed proof because Hessian-a integration differentiates a^{p-2}F^{p-2} and requires retaining both full-tensor D_p^Rm and radial D_p^F, and the defect hierarchy still needs a regularized |E| derivation. Check whether the m=2 continuation replacement using Hölder (4,4,2), ||nabla^2 chi||_4, and weighted Sobolev is a valid current formulation, rather than the prior L^infty shortcut. Return direct mathematical corrections, any remaining exponent/normalization errors, and the sharp next proof obligation. Do not assess final writing readiness.

## Output

## Scientific verification memo

### 1. Nested weighted Moser calculation

Let
\[
H_p=\int a^{p-2}f^p,\qquad
D_p=\int a^{p-1}f^{p-2}|\nabla f|^2,\qquad
z_p=a^{(p-1)/2}f^{p/2}.
\]

#### Mixed interpolation and reaction normalization

The identity
\[
H_{3p/2}
=\int (a^{p-2}f^p)^{1/2}z_p^2
\le H_p^{1/2}\|z_p\|_4^2
\]
is exact, since
\[
\frac{p-2}{2}+(p-1)=\frac{3p}{2}-2.
\]

Writing \(B_p=D_p+r^{-2}H_p\), the Sobolev and gradient estimates give
\[
\|z_p\|_4^2\le Cp^2C_SB_p.
\]
For
\[
R_p=\int a^{p-1}Ff^p,
\]
the three-factor decomposition yields
\[
R_p\le Cp^{4/3}C_S^{2/3}Y^{1/3}H_p^{1/3}B_p^{2/3}.
\]
Direct Young gives, before accounting for any exterior factor \(p\) in the energy inequality,
\[
R_p\le \varepsilon B_p+
C\varepsilon^{-2}p^4C_S^2YH_p.
\]
Thus \(C_S^2Y\) is indeed the correct potential in the convention
\[
\|z\|_4^2\le C_S\bigl(\|\nabla z\|_2^2+r^{-2}\|z\|_2^2\bigr).
\]
The eventual power of \(p\) depends on the precise dissipation coefficient and on the exterior \(pR_p\), but remains polynomial.

#### Spacetime recurrence

Assume
\[
\sup_{I_{k+1}}H_{p_k}
+\int_{I_{k+1}}B_{p_k}
\le L_kA_k,
\qquad
A_k=\int_{I_k}H_{p_k},
\]
with
\[
L_k\lesssim Cp_k^N4^k(t^{-1}+r^{-2}).
\]
Then
\[
\begin{aligned}
A_{k+1}
&\le
C p_k^2 C_S
\bigl(\sup_{I_{k+1}}H_{p_k}\bigr)^{1/2}
\int_{I_{k+1}}B_{p_k}\\
&\le Cp_k^NC_SL_k^{3/2}A_k^{3/2}.
\end{aligned}
\]
There is no factor \(L_k^{-1/2}\): the supremum contributes
\((L_kA_k)^{1/2}\), while the spacetime energy contributes \(L_kA_k\).

With \(p_{k+1}=\frac32p_k\),
\[
A_{k+1}^{1/p_{k+1}}
\le
\bigl(Cp_k^NC_SL_k^{3/2}\bigr)^{1/p_{k+1}}
A_k^{1/p_k}.
\]
The relevant sums are exactly
\[
\sum_{k=0}^{\infty}\frac1{p_{k+1}}=\frac2{p_0},
\qquad
\frac32\sum_{k=0}^{\infty}\frac1{p_{k+1}}=\frac3{p_0}.
\]
The sums involving \(\log p_k\) and \(k\) also converge. Therefore
\[
\|af\|_{L^\infty(\text{terminal slab})}
\le
C C_S^{2/p_0}(t^{-1}+r^{-2})^{3/p_0}
\left(\int_{t/2}^tH_{p_0}(s)\,ds\right)^{1/p_0}.
\]
For \(t\le cr^2\), this becomes
\[
\boxed{\;
\|af(t)\|_\infty
\le C C_S^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^tH_{p_0}(s)\,ds\right)^{1/p_0}.
\;}
\]
Obtaining the value at \(t\) requires the nested slabs to retain \(t\) in their closure; smoothness then supplies the pointwise endpoint. The limiting weight is \(af\), since
\[
(a^{p-2}f^p)^{1/p}=a^{1-2/p}f\longrightarrow af.
\]

#### Curvature and defect cancellations

For curvature, \(p_0=3\) and \(H_3=Y\). Under
\[
\int_{t/2}^tY(s)\,ds\le C\frac{\beta^3}{C_S^2},
\qquad
\beta=C_SH_2(0)^{1/2},
\]
the endpoint is
\[
C C_S^{2/3}t^{-1}
\left(\frac{\beta^3}{C_S^2}\right)^{1/3}
=
\boxed{\;C\beta/t.\;}
\]

For the defect, \(p_0=6\) and
\[
J_6(s)\le C\delta^6V
\]
give
\[
\begin{aligned}
\|aE(t)\|_\infty
&\le C C_S^{1/3}t^{-1/2}
(\delta^6Vt)^{1/6}\\
&=C\delta C_S^{1/3}V^{1/6}t^{-1/3}.
\end{aligned}
\]
Using the same-support upper estimate
\[
C_S\le Cr^2V^{-1/2}
\]
gives
\[
\boxed{\;
\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3}.
\;}
\]
Consequently,
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta\theta^{2/3}r^2.
\]

One textual correction is needed in §4.1: the spacetime seed
\[
\int_{t/2}^tY\le C\beta^3/C_S^2
\]
and the pointwise dyadic estimate
\[
C_S^2Y(s)\lesssim \beta^3/s
\]
are not equivalent by themselves. The pointwise estimate implies the integral estimate. The converse needs the stated good-slice argument together with a \(q=3\) forward propagation inequality. The integral estimate supplies the initial Moser quantity \(A_0\), while the pointwise estimate supplies the coefficient control used in \(L_k\).

When \(C_S\) and \(V\) evolve, these formulas require a uniform upper bound for \(C_S(s)\) on the whole slab and a compatible reference volume on the same support.

#### Collapsed flat product

On \(B^3(1)\times S^1(\varepsilon)\), take
\[
u(x,\theta)=\phi(x),\qquad \phi\in C_c^\infty(B^3(1)),\quad \phi\ne0.
\]
Then
\[
\|u\|_4^2
=\left(\int|u|^4\right)^{1/2}
\asymp \varepsilon^{1/2},
\]
whereas
\[
\int\bigl(|\nabla u|^2+r^{-2}u^2\bigr)\asymp\varepsilon
\]
for fixed \(r\). Hence every coefficient in the unnormalized Dirichlet Sobolev inequality satisfies
\[
C_S\ge c_\phi\varepsilon^{-1/2}.
\]
The function has compact support in the interior, so the zero-trace condition does not alter this scaling. Since \(V\asymp\varepsilon\), this matches \(C_S\asymp r^2V^{-1/2}\). The Python script verifies these exponents; it does not verify any PDE estimate.

---

### 2. Tensor derivation and the \(m=2\) continuation term

#### Curvature power inequality

The Step 31 treatment of the Hessian-\(a\) term is incomplete. A representative integral is
\[
I_C=p\int a^{p-2}F^{p-2}\nabla^2a*T,
\qquad |T|\lesssim F^2.
\]
After one integration by parts,
\[
I_C=-p\int\nabla a*
\nabla\!\left(a^{p-2}F^{p-2}T\right).
\]
The three derivative targets require distinct estimates:

1. Differentiating \(a^{p-2}\) produces
   \[
   p(p-2)a^{p-3}|\nabla a|^2F^p
   \lesssim p^2r^{-2}H_p.
   \]

2. Differentiating \(F^{p-2}\) produces
   \[
   p(p-2)a^{p-2}|\nabla a|F^{p-1}|\nabla F|,
   \]
   which is paid by the radial term
   \[
   p(p-2)D_p^F
   \]
   plus a polynomial \(p\)-multiple of \(r^{-2}H_p\).

3. Differentiating \(T\) produces terms involving
   \[
   \nabla\operatorname{Rm}*E,\qquad
   \operatorname{Rm}*\nabla E.
   \]
   Since
   \[
   |\nabla E|\le C|\nabla\operatorname{Rm}|,
   \]
   these require
   \[
   pD_p^{\operatorname{Rm}},
   \]
   not merely \(D_p^F\).

Thus the Bochner pair must remain in the form
\[
pD_p^{\operatorname{Rm}}+p(p-2)D_p^F
\]
until every differentiated Hessian-\(a\) term has been treated. The inequality
\(|\nabla F|\le|\nabla\operatorname{Rm}|\) only goes in one direction and does not permit full tensor derivatives to be paid by the radial norm. Step 31 equation (2.7) suppresses precisely these derivative targets.

For the defect, homogeneity of the tensor equation in \(E\) is useful but does not replace the calculation with
\[
f_\varepsilon=(|E|^2+\varepsilon)^{1/2}.
\]
That calculation must retain the full \(\nabla E\) dissipation, the radial \(\nabla f_\varepsilon\) term, Hessian-\(a\) integrations, moving tensor norms, and moving measure. Any \(\varepsilon\)-terms must vanish uniformly as \(\varepsilon\to0\). Only then does the absence of a curvature-only source pass to the \(J_p\) inequality.

#### The \(m=2\) term

Set
\[
W=\nabla^2U,\qquad B=\nabla^2\chi,\qquad
X_p=\int|W|^p,\qquad
D_p=\int\chi^2|\nabla W|^2|W|^{p-2},
\]
and
\[
u=\chi|W|^{p/2}.
\]
Then
\[
\int\chi|B||W|^p
\le \|B\|_4\|u\|_4X_p^{1/2}
\]
by Hölder \((4,4,2)\). Moreover,
\[
\|u\|_4^2
\le CC_S\bigl(p^2D_p+r^{-2}X_p\bigr).
\]
This mechanism is valid and uses only a spatial \(L^4\) estimate for the evolving Hessian of \(\chi\).

The boxed Step 32 formula (6.1), however, omits a harmless zero-order term. A direct Young calculation gives
\[
\boxed{\;
\int\chi|B||W|^p
\le
\varepsilon D_p+
C_\varepsilon\bigl(r^{-2}+p^2C_S\|B\|_4^2\bigr)X_p.
\;}
\]
If normalized zeroth-order contributions are included, one may write
\[
\varepsilon D_p+
C_\varepsilon\bigl(1+r^{-2}+p^2C_S\|B\|_4^2\bigr)X_p.
\]
Equivalently, a coarser form is
\[
\varepsilon D_p+
C_\varepsilon(1+r^{-2})
\bigl(1+p^2C_S\|B\|_4^2\bigr)X_p.
\]
The displayed Step 32 expression containing only
\[
p^2C_S\|B\|_4^2(1+r^{-2})X_p
\]
does not follow directly from Hölder, Sobolev, and Young without an additional relation among the cutoff norms. The restored zero-order term is already compatible with Gronwall.

This \(L^4\) formulation is preferable to the earlier pointwise shortcut. Uniform control of \(\|\nabla^2_{g(t)}\chi\|_\infty\) is not supplied by metric comparability alone, because the evolving connection enters \(\nabla^2_{g(t)}\chi\). A preceding coupled level can instead supply a uniform \(\|\nabla^2\chi\|_4\), which is exactly what the corrected estimate consumes.

### Sharp proof obligation

The remaining analytic lemma must derive, term by term,
\[
K_p'
+c\,pD_p^{\operatorname{Rm}}
+c\,p(p-2)D_p^F
\le
Cp^N(1+r^{-2}+C_S^2Y)K_p
\]
and an \(\varepsilon\)-uniform defect analogue with both full and radial defect dissipations, followed by \(J_6\) persistence from time zero. The same lemma package also needs the \(H_2\to H_3\) spacetime seed and the \(q=3\) forward estimate that converts a good slice into the dyadic bound for \(C_S^2Y\). For continuation, the corrected \(m=2\) estimate above handles the single-\(\chi\) term, but every remaining product in the coupled \((\nabla^2U,\nabla^3\chi)\) energy still needs an explicit estimate.