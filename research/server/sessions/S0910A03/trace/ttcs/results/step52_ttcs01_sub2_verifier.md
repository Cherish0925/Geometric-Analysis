# TTCS Independent Branch Record

```json
{
  "step_id": 52,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step52_normalized_local_flow_start_repair.md",
    "Sessions/S0910A03/workspace/scripts/step52_flat_cutoff_forcing_test.py",
    "Sessions/S0910A03/workspace/data/step52_flat_cutoff_forcing_test.json",
    "Sessions/S0910A03/staging/processing/xu_local_ricci_flow.txt",
    "Sessions/S0910A03/workspace/notes/step50_normalized_yang_wang_verification.md",
    "Sessions/S0910A03/workspace/notes/step51_normalized_yang_precise_estimate.md"
  ]
}
```

## Task

Independently check the new Step 52 normalized local-flow start. The scientific question is whether Guoyi Xu's detailed fixed-point proof for the degenerate local Ricci-DeTurck equation remains valid after adding the algebraic metric reaction -2 chi^2 g. Reconstruct the exact changes to Xu's frozen strictly parabolic map, positivity/eigenvalue estimates, high-Sobolev invariant ball, contraction estimate, epsilon-uniform compactness, and DeTurck pullback. Look specifically for hidden derivative loss, epsilon dependence, boundary/interface mismatch, wrong sign, or a failure to recover the exact geometric normalized flow. Also verify that the flat-torus test really falsifies Step 51's homogeneous critical-energy closure. Give a direct mathematical judgment and any exact repairs needed.

## Output

## Verifier Memo — Step 52 normalized local-flow start

### Overall mathematical judgment

The construction in Step 52 is sound. Adding the algebraic reaction $-2\chi^2 V$ to Xu's frozen strictly parabolic map is a genuine zeroth-order perturbation: it introduces no derivative of the unknown, no inverse power of the regularization parameter, and no new composition type. Each of Xu's four structural estimates (eigenvalue positivity, high-Sobolev invariant ball, lower-order contraction, $\epsilon$-uniform compactness) closes after shrinking the per-datum time, and the DeTurck pullback recovers the exact geometric normalized flow. The flat-torus computation is arithmetically correct and does establish that spatial normalization produces curvature from flat data. Below I reconstruct each piece and mark the two places where the written justification is thinner than the mathematics it stands on.

### 1. Frozen map and the sign of the reaction

The target geometric flow $\partial_t g=-2\chi^2(\operatorname{Ric}_g+g)$ carries the localizing factor $\chi^2$ on the normalization, not a bare $-2g$. This is essential and Step 52 uses it correctly. In Xu's Eulerian equation (2.3) every term already carries a power of $\chi$; the reaction $-2\chi^2 g$ carries $\chi^2$ too, so all terms vanish together on the interior of $\{\chi=0\}$ and the two-region structure (moving on $\{\chi>0\}$, stationary on $\{\chi=0\}$) is preserved. A reaction $-2g$ would not vanish on $\{\chi=0\}$ and would destroy this structure; the chosen $-2\chi^2 g$ does not. In the solved-for variable the reaction is $-2\chi^2 V$ (3.5), which is the correct object to add, and being $\epsilon$-independent it needs no regularization.

### 2. Eigenvalue/positivity estimates (Prop 2.5, first part)

From $\dot V=-2\chi^2 V$ one gets $\dot{(V^{-1})}=2\chi^2 V^{-1}$, and for the power traces $\phi_m=\operatorname{tr}(V^{-m})$, $\psi_m=\operatorname{tr}(V^m)$,
$$(\partial_t\phi_m)_N=2m\chi^2\phi_m,\qquad (\partial_t\psi_m)_N=-2m\chi^2\psi_m,$$
which I confirm by differentiating $\sum\lambda_i^{\mp m}$ with $\dot\lambda_i=-2\chi^2\lambda_i$. Signs (3.6) are right. The reaction pushes eigenvalues downward, so the quantity at risk is the lower bound $\lambda_i\ge \tfrac12$; this is exactly the $\phi_m$ inequality, which acquires the positive term $+2m\chi^2\phi_m\le +2m\phi_m$. In Xu's maximum-principle argument this is a bounded additive contribution to the ODE comparison, so $t_{1,1}$ shrinks but stays positive. The $\psi_m$ inequality acquires the dissipative $-2m\chi^2\psi_m$, which only helps the upper bound. So $A_T$ invariance holds on a smaller time. No derivative and no $\epsilon^{-1}$ enters. Correct.

### 3. High-Sobolev invariant ball (Prop 2.5, 2.7)

The reaction contributes to $\tfrac{d}{dt}\|V\|_m^2$ the term $2\sum_{|\alpha|\le m}\langle\tilde\nabla^\alpha V,\tilde\nabla^\alpha(-2\chi^2 V)\rangle$. At top order $|\alpha|=m$ the leading piece is $-2\chi^2|\tilde\nabla^m V|^2$ (harmless sign), and all cross terms distribute $\tilde\nabla^\beta(\chi^2)$ with $|\beta|\ge1$ onto lower derivatives of $V$; Moser product estimates give the stated $C_m\|\chi\|_{C^m}^2\|V\|_m^2$ (3.7). Crucially the reaction produces nothing at order $\tilde\nabla^{m+1}V$, so it does not touch the principal weighted dissipation $\int(\chi^2+\epsilon)|\tilde\nabla^{\alpha+1}V|^2$. Xu's inequality (2.22) changes only by a bounded multiple of $\|V\|_m^2$. Correct.

### 4. Contraction (Prop 2.8)

For $W=V-\tilde V$, the two reaction terms $-2\chi^2 V$ and $-2\chi^2\tilde V$ subtract to $-2\chi^2 W$ (3.8). This is the one point worth stating explicitly: because the reaction depends only on the solved variable and not on the frozen coefficient $U$, it contributes **nothing** to Xu's inhomogeneity $H$ (which collects $U-\tilde U$ terms); it lands entirely on the $W$-side. Its energy contribution stays inside $|\cdot|_{\tilde p}$ with bound $C_{\tilde p}\|\chi\|_{C^{\tilde p}}^2\|W\|_{\tilde p}^2$ (3.9), so Xu's difference inequality (2.49) becomes (3.10), and $W(0)=0$ gives the coefficient $C_2 T e^{(C_1+C_N)T}$, driven below $1/4$ by taking $T$ small. The contraction constant $1/2$ is recovered with the same derivative loss. Correct — no loss, same norm.

### 5. The $\epsilon\to0$ limit and interface regularity

Every extra constant ($2m$, $C_m\|\chi\|_{C^m}^2$) is free of $\epsilon$, so Xu's uniform-in-$\epsilon$ high-Sobolev and time-derivative bounds persist, and Rellich–Kondrachov compactness passes to a limit solving (3.4). Smoothness on $\{\chi>0\}$ is interior parabolic regularity; on the interior of $\{\chi=0\}$ every term (including $-2\chi^2 V$) vanishes and the metric is stationary. This is precisely Xu's Theorem 2.9 conclusion, and the reaction respects it.

The most delicate transfer is smoothness **across** a non-flat zero set of $\chi$, e.g. the hypersurface $\{x_1=\pi\}$ in the test where $\chi\sim\tfrac14(x_1-\pi)^2$ and $\chi^2$ vanishes to fourth order rather than to infinite order. Xu handles this not by interior Schauder but by carrying global fixed-background Sobolev bounds at arbitrary finite order before the diagonal limit, then Sobolev embedding. Step 52 §3.4 invokes exactly this mechanism, and the reaction sits in the same global Sobolev norms, so the argument goes through. This is correct but is the piece leaning most heavily on Xu's specific smoothness route; it is where a reader should look hardest, and Step 52 does point to it.

### 6. DeTurck pullback — substance correct, justification thin

Equation (3.3) is stated with the fixed cutoff $\chi^2$, whereas a literal pullback of $-2\chi^2(\operatorname{Ric}_g+g)$ by $\varphi_t$ produces the composed factor $\chi^2\circ\varphi_t$ in front of $\operatorname{Ric}_{\varphi^*g}+\varphi^*g$. The one-line reason given ("$\chi$ is fixed in Xu's Eulerian formulation, so no transported-cutoff composition is needed") glosses this. The mathematically load-bearing reason is stronger and should be written out: the added term $-2\chi^2 g$ and Xu's term $-2\chi^2\operatorname{Ric}_g$ are **both** $\chi^2$ times a natural symmetric 2-tensor, so they transform identically under the DeTurck diffeomorphism, the added term contributes no Lie derivative and no new composition type, and the diffeomorphism equation (3.2) and the vector field $W_j=g^{jk}g^{pq}(\Gamma^k_{pq}-\tilde\Gamma^k_{pq})$ are unchanged by normalization. Xu's published pullback already converts the fixed-$\chi$ DeTurck system into the fixed-$\chi$ local Ricci flow (1.2) (this is what his Theorem 5.14 asserts); the normalization rides on that identical mechanism verbatim. So the recovery of the exact fixed-$\chi$ normalized geometric flow is correct; only the written argument is terser than warranted.

### 7. Two conditions on the statement of Proposition 3.1

- Xu's local Ricci flow is defined for $n\ge3$ (his (1.2) and abstract). Proposition 3.1 is written for a general closed $M$ with no dimension restriction. For $n=4$, the program's focus and the test dimension, this is immaterial. For $n=2$ the §2 construction would need a separate reading. Worth a marginal note.
- Xu's §2 lives on a bounded domain $\Omega$ with the condition $g=\tilde g$ on $\partial\Omega$ (with $\chi$ compactly supported inside). On a closed $M$ there is no $\partial\Omega$; the analogous facts are the global Sobolev constant $C_s(M,g_0)<\infty$ and stationarity on $\{\chi=0\}$. This transfer is fine and arguably cleaner, but the statement "based on Xu's detailed fixed-point construction" implicitly performs this domain-to-closed passage; it is legitimate and rests on the same estimates.

### 8. The flat-torus test versus Step 51

I reproduced the symbolic content. With $\chi=(1+\cos x_1)/2$, $a=\chi^2=\tfrac38+\tfrac12\cos x_1+\tfrac18\cos 2x_1$, so $a''=-\tfrac12(\cos x_1+\cos 2x_1)$, matching the script. At $t=0$ on the flat torus $\operatorname{Ric}=0$, so $\dot g=-2ag$ and $\dot{\operatorname{Rm}}=g\owedge\operatorname{Hess}a$. For $H=\operatorname{diag}(a'',0,0,0)$ the tensor norm $|g\owedge H|^2=4(n-2)|H|^2+4(\operatorname{tr}H)^2=8(a'')^2+4(a'')^2=12(a'')^2$, matching the script's ratio $12$. With $\int_0^{2\pi}(a'')^2\,dx_1=\pi/2$ and three transverse circles of length $2\pi$,
$$\int_{T^4}|\operatorname{Rm}(g(t))|^2\,d\mu = 12\cdot\tfrac{\pi}{2}\cdot(2\pi)^3\,t^2+O(t^3)=48\pi^4 t^2+O(t^3).$$
All four assertions in the script (`ratio==12`, `int==π/2`, `leading==48π^4`, `E'/E==2/t`) are correct, and this is a leading-order infinitesimal computation that uses only the flow equation at $t=0$, so it is independent of PDE existence. The conclusion $E'/E=2/t$ genuinely precludes any source-free inequality $E'(t)\le C\,E(t)$ near zero.

What this refutes, precisely:

- It shows the forcing $g\owedge\operatorname{Hess}(a)$ is real and creates curvature from flat data. In Yang's unnormalized flow, flat torus data is stationary; under the normalization it is not. So the normalized critical-$L^{n/2}$ energy (in $n=4$, $\int|\operatorname{Rm}|^2$) does not reduce to Yang's source-free framework, contrary to Step 51 §7–§8 ("KN source eliminated by IBP … no non-homogeneous Moser extension is needed").
- The deeper structural point, Step 52 §1, is the correct one: the single integration by parts of $4p\int F^{p-2}\operatorname{Ric}_{ij}\nabla_i\nabla_j a$ leaves $|da|F^{p-2}|\nabla\operatorname{Ric}|$ and $|da|F^{p-2}|\operatorname{Ric}||\nabla F|$; absorbing the second into $\int aF^{p-2}|\nabla\operatorname{Rm}|^2$ leaves $\tfrac{|da|^2}{a}F^{p-2}=4|d\chi|^2F^{p-2}$, and a second integration by parts of the contracted-Bianchi piece restores $\Delta_g a$. That $\Delta_g a=g^{ij}(\partial_i\partial_j a-\Gamma(g)^k{}_{ij}\partial_k a)$ carries the connection of the **evolving** metric, which bilipschitz equivalence does not control (the same mechanism identified in Step 50 §1.1). Step 51 silently replaced this by the fixed-metric $\|\Delta\chi\|_\infty$ inside its (2.5). This substitution is the actual place the earlier argument does not close.

One nuance I want stated so the refutation is not overread. Step 51's literal displayed inequality (2.10), $\int F^{n/2}(t)\le e^{(\cdots)}(\int F_0^{n/2}+C_\epsilon\operatorname{Vol}\cdot t)$, carries an additive volume term. With $F_0=0$ it gives $O(t)$, and the measured $O(t^2)$ is numerically consistent with $O(t)$ near zero. So the flat number does not contradict inequality (2.10) as written; it contradicts the surrounding reading that the critical-exponent cancellation $(2p-n)|_{p=n/2}=0$ plus IBP removes the source and yields a per-datum existence argument. The correct separation, which Step 52 makes, is that per-datum existence comes from the fixed-point route (Xu §2 + reaction), while a critical-energy smallness estimate is a Yang-Theorem-9.2-type domain-uniform smoothing statement that presupposes the flow already exists. Step 52 explicitly does not assert domain-uniform time ("not asserted to be uniform across a collapsing sequence"), which is the position consistent with the test.

### 9. Net

Proposition 3.1 (normalized per-datum start and restart on closed $M$) is established by the reconstruction above, with the frozen-map, eigenvalue, Sobolev-ball, contraction, and compactness steps all closing under the zeroth-order reaction $-2\chi^2 V$ with no hidden derivative loss, no $\epsilon$ dependence, correct signs, and stationarity preserved on $\{\chi=0\}$. Two written justifications deserve expansion to match the mathematics they rely on: the DeTurck pullback should be argued from identical transformation type of the two $\chi^2\cdot$tensor terms rather than from "$\chi$ fixed"; and interface smoothness across a non-flat zero set of $\chi$ should be tied explicitly to Xu's global finite-order Sobolev route (as §3.4 does) rather than to any interior statement. The flat-torus test is correct and does what it says: it exhibits a genuine spatial forcing that a source-free critical-energy closure cannot absorb, so the Step 51 route is not a valid existence or homogeneous-closure argument, and the separate fixed-point start in Step 52 is the appropriate replacement.

Unresolved by this material, and needed before the surrounding program advances: the domain/sequence-uniform first-exit estimates that Step 52 deliberately leaves aside, and the reconnection of those to the coupled cutoff-jet continuation of Step 50 without reimporting the source-free critical-energy statement. These are stated as open in the note itself and are not settled by the start construction verified here.