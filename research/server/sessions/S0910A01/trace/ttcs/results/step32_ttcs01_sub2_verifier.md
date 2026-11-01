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

# Verifier Memo — Step 32 nested weighted Moser recurrence and tensor-derivation review

I independently reworked the two mathematical points requested. Point 1 (recurrence, exponents, endpoints, cancellations, collapse counterexample) reproduces exactly under my own computation. Point 2 (tensor ledger, defect derivation, m=2 replacement) is substantively correct, with one genuine adjudication between A01-Step32 and A03-Step32 on the pointwise endpoint, a subdominant term in the m=2 estimate to record, and two notational collisions that will cross-contaminate other notes if left implicit.

## Point 1 — the corrected recurrence

**Interpolation identity (3.3).** With $z_p^2=a^{p-1}f^p$ and $(a^{p-2}f^p)^{1/2}=a^{(p-2)/2}f^{p/2}$, the product has $a$-exponent $(p-2)/2+(p-1)=3p/2-2$ and $f$-exponent $3p/2$, so $\int(a^{p-2}f^p)^{1/2}z_p^2=H_{3p/2}$, and Cauchy–Schwarz gives $H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2$. Correct.

**Sobolev/gradient feed.** $\|z_p\|_2^2=\int a^{p-1}f^p\le\int a^{p-2}f^p=H_p$ (since $a\le1$), so applying (1.1) to $z_p$ with (2.4) yields $\|z_p\|_4^2\le Cp^2C_S(D_p+r^{-2}H_p)$. Correct.

**Recurrence power is $L_k^{3/2}$, not $L_k$.** The two energy outputs on the slab are $\sup_{I_{k+1}}H_{p_k}\le L_kA_k$ and $\int_{I_{k+1}}(D_{p_k}+r^{-2}H_{p_k})\le L_kA_k$, with $A_k=\int_{I_k}H_{p_k}$. Then
$$\int_{I_{k+1}}H_{p_{k+1}}\le(\sup_{I_{k+1}}H_{p_k})^{1/2}\,Cp_k^2C_S\!\int_{I_{k+1}}\!(D_{p_k}+r^{-2}H_{p_k})\le Cp_k^2C_S(L_kA_k)^{1/2}(L_kA_k)=Cp_k^2C_S\,L_k^{3/2}A_k^{3/2}.$$
The half-power sits with the supremum factor and the full power with the integral factor; there is no $L_k^{1/2}$ in a denominator. The Step 31 recurrence (its 5.4, via the intermediate line "$[L_k\int K_{p_k}]^{3/2}/L_k^{1/2}$") divided the two, effectively replacing $L_k^{3/2}$ by $L_k$; that is the error, and Step 32's $L_k^{3/2}$ is the correct one.

**Exponent sums.** $U_k:=A_k^{1/p_k}$ satisfies $U_{k+1}\le B_k^{1/p_{k+1}}U_k$ because $(3/2)/p_{k+1}=1/p_k$. With $p_k=p_0(3/2)^k$, $\sum_{k\ge0}1/p_{k+1}=\frac1{p_0}\sum_{k\ge0}(2/3)^{k+1}=2/p_0$, so the $C_S$ exponent is $2/p_0$; the $t^{-1}$ inside $L_j$ enters at power $3/2$, giving time exponent $\tfrac32\cdot\tfrac2{p_0}=3/p_0$. The $\log p_j$ and dyadic $4^j$ losses sum finitely by geometric growth of $p_j$. Endpoint
$$\|af(t)\|_\infty\le C\,C_S^{2/p_0}t^{-3/p_0}\Big(\!\int_{t/2}^tH_{p_0}\Big)^{1/p_0}$$
is exactly what the recurrence delivers. Correct; the script's `recurrence_exponents` reproduces $2/p_0$ and $3/p_0$.

**Curvature and defect cancellations.** For $p_0=3$, seed $\int_{t/2}^tY\le C\beta^3/C_S^2$ gives $C_S^{2/3}t^{-1}(\beta^3/C_S^2)^{1/3}=\beta/t$ — the $C_S^{2/3}$ and $C_S^{-2/3}$ cancel. For $p_0=6$ (defect $f=|E|$, $H_6=\int a^4|E|^6=J_6$), seed $J_6\le C\delta^6V$ gives $C_S^{1/3}t^{-1/2}(\delta^6Vt)^{1/6}$; with $C_S\asymp r^2V^{-1/2}$ one has $C_S^{1/3}V^{1/6}=r^{2/3}$ and $t^{-1/2}t^{1/6}=t^{-1/3}$, hence $\delta(r^2/t)^{1/3}$, with $V$ cancelled. Drift: $\int_0^T\delta(r^2/t)^{1/3}dt=\tfrac32\delta r^{2/3}T^{2/3}=\tfrac32\delta\theta^{2/3}r^2$, and $t^{-1/3}$ is integrable at $0$. All correct.

**Collapse counterexample.** On $B^3(1)\times S^1(\varepsilon)$ with $u$ supported in $B^3$ and constant along $S^1$: $\|u\|_4^4\sim\varepsilon$ so $\|u\|_4^2\sim\varepsilon^{1/2}$, while $\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\sim\varepsilon$; the required coefficient is $\gtrsim\varepsilon^{-1/2}$. Taking $u$ compactly supported in the interior of the $B^3$ factor keeps it Dirichlet-admissible on $\partial\operatorname{supp}\chi$, so vanishing boundary values do not remove the $\varepsilon^{-1/2}$ collapse factor. Consistent with $\operatorname{Vol}(M)\sim\varepsilon$ and $C_S\sim r^2/\sqrt V\sim\varepsilon^{-1/2}$. Correct; the coefficient scaling in the script ($10,10^2,10^4$ for $\varepsilon=10^{-2},10^{-4},10^{-8}$) matches.

**Reaction potential $C_S^2Y$.** Three-factor identity $a^{p-1}Ff^p=(aF^3)^{1/3}(a^{p-2}f^p)^{1/3}z_p^{4/3}$ balances both exponents; Hölder$(3,3,3)$ gives $R_p\le Y^{1/3}H_p^{1/3}\|z_p\|_4^{4/3}$, and Young cubes the $C_S^{2/3}Y^{1/3}$ prefactor to $C_S^2Y$. My absorption gives the polynomial power $N=4$; any finite $N$ is acceptable for the Moser product. Correct.

**Two items to carry forward on Point 1.**

1. *The pointwise endpoints are genuinely $t$-singular, and this resolves the A01-Step32 / A03-Step32 disagreement.* The factor $t^{-3/p_0}$ is intrinsic to the temporally localized recurrence; a uniform-in-$t$ pointwise bound would require $\int_{t/2}^tH_{p_0}\sim t^3$ (i.e. $H_{p_0}\sim t^2$), which the seeds do not give. Step 31 §8's flattening to "$\|aF\|_\infty\le C(\gamma,\theta)$ uniform" came from replacing $\tfrac1t\int_0^tK_3$ by $\int_0^TK_3$ without retaining the temporal prefactor; that replacement is not valid, and moreover $\int_0^tK_3$ diverges at $0$ under the $Y(s)\sim\beta^3/(C_S^2s)$ propagation the seed rests on. Step 32's $\beta/t$ (curvature) and $\delta(r^2/t)^{1/3}$ (defect) are the supported raw outputs. A03's remark that "uniform terminal bounds may be sufficient" is a downstream-sufficiency statement, not a statement that the recurrence produces uniform bounds; it should not be read as contradicting the $t$-singular endpoint. The two are compatible only if one keeps track that (i) the curvature $\beta/t$ is not itself time-integrable, but enters $J_6$'s equation as a coefficient producing the mild power $(t/s)^{C\beta}$ (log-integrable, controllable for small $\beta$), and (ii) the defect $t^{-1/3}$ is time-integrable and is what supplies the metric drift $\int_0^T\|aE\|_\infty$.

2. *Notational collisions across the notes.* Step 32 uses $C_S$ with $\|z\|_4^2\le C_S(\ldots)$, whereas Step 31 uses $S$ with $\|Z_p\|_4^2\le S^2(\ldots)$; hence $C_S=S^2$ and Step 31's potential $S^4Y$ equals Step 32's $C_S^2Y$ (no discrepancy, but easy to misread). Likewise Step 32's $\beta=C_SH_2(0)^{1/2}$ equals Step 31's $\gamma=S^2H_2^{1/2}$, and is a different quantity from Step 31's own $\beta=SH_2^{1/2}$. Any cross-note use of "$\beta/t$" must fix which $\beta$; the endpoint $\beta/t$ is correct only with the Step 32 definition.

## Point 2 — tensor ledger, defect derivation, m=2 replacement

**The premature dissipation collapse is a real error, and the repair ordering is correct.** In Step 31 the Bochner pair $-pD_p^{\operatorname{Rm}}-p(p-2)D_p^F$ is immediately compressed to $-p(p-1)D_p^F$ using $D_p^{\operatorname{Rm}}\ge D_p^F$, leaving only a $D_p^F$ reservoir (its 2.5, then $\varepsilon=1/8$). But the Type-B and Hessian-of-$a$ terms, once $\nabla$ hits $T=\operatorname{Rm}+G$, produce $\nabla\operatorname{Rm}$ and (via $|\nabla E|\le C|\nabla\operatorname{Rm}|$) $\nabla E$ contributions that can only be absorbed into $+\varepsilon pD_p^{\operatorname{Rm}}$. Absorbing $+\varepsilon pD_p^{\operatorname{Rm}}$ into $-cp^2D_p^F$ is not permitted, because $D_p^{\operatorname{Rm}}\ge D_p^F$ makes the reservoir potentially far smaller than the term. Step 32's requirement — retain $-pD_p^{\operatorname{Rm}}-p(p-2)D_p^F$, absorb all full-tensor derivative terms into $D_p^{\operatorname{Rm}}$ first, and only then compress the residual to $c\,p^2D_p^F$ for the interpolation — is the correct order. It is also internally consistent with the Moser step, since $\nabla z_p$ ($z_p=a^{(p-1)/2}f^{p/2}$) only produces $\nabla F$, so $D_p^F$ is exactly what the interpolation consumes. So Step 31's boxed (3.1)/(4.5) is a schematic estimate, not a proved power inequality, and Step 32's statement to that effect is right. The Hessian-cutoff derivative bookkeeping I checked term by term: $\nabla(a^{p-2})$ gives $\lesssim p^2r^{-2}K_p$ (using $a^{p-3}|\nabla a|^2=4a^{p-2}|\nabla\chi|^2$), $\nabla(F^{p-2})$ pays $p(p-2)D_p^F+p^2r^{-2}K_p$, and $\nabla T$ pays $pD_p^{\operatorname{Rm}}+pr^{-2}K_p$. The ledger is sound.

**Defect derivation genuinely remains open.** Homogeneity of the $V=aE$ equation (A03's 2.11, reaction $U*V+V*V+aG*V$, $|\mathcal R_V|\le C_n(|U|+a)|V|$) fixes the reaction weight but does not substitute for the regularized derivation. The power inequality (5.3), $J_p'+c_pD_p^E\le Cp^N(r^{-2}+C_S^2Y)J_p+\text{absorbable}$, with no curvature-only source, still needs the $|E|_\varepsilon=(|E|^2+\varepsilon)^{1/2}$ equation written explicitly, the Kato chain-rule dissipation at the zero set of $E$, and the moving-norm/moving-measure terms tracked. Step 32 states this correctly as an unfinished estimate.

**The m=2 weighted-Sobolev replacement is a valid current formulation; the $L^\infty$ shortcut is not.** I verified the Hölder$(4,4,2)$ estimate. Writing $I=\int|B|\,u\,|W|^{p/2}$ with $B=\nabla^2\chi$, $u=\chi|W|^{p/2}$, Hölder gives $I\le\|B\|_4\|u\|_4X_p^{1/2}$; Sobolev gives $\|u\|_4^2\le CC_S(p^2D_p+(1+r^{-2})X_p)$; Young on the $D_p$ part gives $\varepsilon D_p+C_\varepsilon p^2C_S\|\nabla^2\chi\|_4^2X_p$. This dominant term matches the boxed (6.1). One point to record: the $(1+r^{-2})X_p$ piece of $\|u\|_4^2$ produces a *subdominant* term $\sim C_S^{1/2}(1+r^{-2})^{1/2}\|\nabla^2\chi\|_4X_p$, which is linear in $\|B\|_4$ and $C_S^{1/2}$, not the quadratic $C_S\|B\|_4^2$ shown. It is bounded by $\tfrac12(C_S\|B\|_4^2+1)(1+r^{-2})X_p$, so it folds into the same $X_p$ coefficient family plus a bare $(1+r^{-2})X_p$ term that enters the Gronwall right side harmlessly; but (6.1)/(3.2) as boxed should carry that additive $(1+r^{-2})X_p$ contribution explicitly rather than absorbing it silently into $C_S\|\nabla^2\chi\|_4^2$.

The reason the $L^\infty$ shortcut is not a base-level estimate: the term uses $\nabla^2\chi$ in the evolving metric $g(t)$, and $\nabla^2_{g(t)}\chi=\nabla^2_{g_0}\chi-(\Gamma(t)-\Gamma_0)*\nabla\chi$ with $\Gamma(t)-\Gamma_0=\int_0^t\partial_t\Gamma$, $\partial_t\Gamma\sim g^{-1}*\nabla(aE)$. So $\|\nabla^2\chi\|_{\infty,g(t)}\lesssim C/r^2$ holds only in the fixed $g_0$; in $g(t)$ it needs the connection $\Gamma(t)$, i.e. $\nabla g$-control, which is built up through the coupled ladder, not delivered by the terminal hypothesis $\|U\|_\infty\le K$ alone. The order-count is coherent: the term carries $\nabla^m\chi$ ($m=2$), a *previous*-level cutoff derivative supplied by the $(\nabla^1U,\nabla^2\chi)$ coupled step, so inserting $\|\nabla^2\chi\|_4$ from that step is consistent with the corrected induction order $(\nabla^mU,\nabla^{m+1}\chi)$-first-then-$\nabla^mT$. Step 32 is right that the shortcut assumes an intermediate-level conclusion; the weighted-Sobolev estimate is the correct current form.

**Coefficient regularization $a\mapsto a+\varepsilon$.** The two notes agree and are correct: it evolves the stationary exterior $\{a=0\}$ by $\partial_tg_\varepsilon=-2\varepsilon(\operatorname{Ric}+g)$ and destroys the identity $|\nabla a|^2/a=4|\nabla\chi|^2$ that the estimates use throughout; Kato regularization of $|E|$ or $|\operatorname{Rm}|$ is different and admissible because it does not touch the flow coefficient. No correction needed.

## Sharp next proof object

The endpoint forms (4.2)/(4.4) and the drift (4.5) are empty until their inputs exist, so the decisive next object is the trio of genuine estimates the recurrence consumes, produced in one convention:

1. the completed curvature general-$p$ power inequality with the $D_p^{\operatorname{Rm}}$/$D_p^F$ ledger executed term-by-term — retaining $-pD_p^{\operatorname{Rm}}$ until every $\nabla\operatorname{Rm}$/$\nabla E$ Hessian-$a$ and Type-B term is absorbed, then compressing the residue to $c\,p^2D_p^F$;
2. the regularized $|E|_\varepsilon$ defect power inequality (5.3) with Kato dissipation, moving-norm and moving-measure terms, and no curvature-only source;
3. the same-support $H_2\to H_3$ spacetime seed and the $q=3$ propagation giving $\int_{t/2}^tY\le C\beta^3/C_S^2$ (equivalently $C_S^2Y(s)\lesssim\beta^3/s$) plus fixed $J_6$ persistence from time zero.

Only after (1)–(3) does the recurrence output stop being a statement about algebra of weights and become a statement about the flow. The m=2 continuation lemma (weighted-Sobolev version with the additive $X_p$ term made explicit, or the exact Wang grouped replacement) is a parallel required piece, and both remain inside the four-dimensional negative Ishida–LeBrun setting — the positive branch, arbitrary 4-manifold topology, $n\ge5$, and the Lean formalization are untouched by these calculations.