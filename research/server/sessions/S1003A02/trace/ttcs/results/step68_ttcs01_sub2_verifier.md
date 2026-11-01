# TTCS Independent Branch Record

```json
{
  "step_id": 68,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/trace/ttcs/results/step67_ttcs01_sub1_generator.md",
    "Sessions/S1003A02/workspace/notes/step67_cK_local_coercivity_at_cscK.md",
    "Sessions/S1003A02/workspace/notes/step66_rank_one_exceptional_ricci_rigidity.md",
    "Sessions/S1003A02/workspace/scripts/step68_product_saddle_direct.py",
    "Sessions/S1003A02/workspace/data/step68_product_saddle_direct_n0.json",
    "Sessions/S1003A02/workspace/data/step68_product_saddle_direct_n1.json",
    "Sessions/S1003A02/workspace/data/step68_product_saddle_direct_n2.json",
    "Sessions/S1003A02/workspace/scripts/step68_product_saddle_global_exact.py"
  ]
}
```

## Task

Independently verify or refute the Step-67 product cscK saddle formula using the actual fixed-symplectic family. Setting: M=Sigma_1(K1) x Sigma_2(K2), K1,K2<0; Q is the real part of a holomorphic quadratic differential on Sigma_1; Delta_2 f=mu f; g_t|_1=g_1(exp(t f g_1^{-1}Q)·,·), g_t|_2=g_2, with fixed omega. The claimed Taylor t^2 coefficient is 8pi^2(p-|c1^-|^2)_2 = [mu/4][mu+2(K1-K2)]||fQ||^2. Derive this from actual connection/curvature variation or an exact integrated identity, checking all factors and the claims Ric''_1=(mu/2)k, rho0'_1=0, int u_2=(mu/4)||k||^2, and (rho0,t_2^-)=-[(K1-K2)mu/8]||k||^2. Resolve the apparent conflict in the supplied direct-coordinate scripts: they use local q=z^n on H^2 and produce n-dependent extra terms, suggesting that a pointwise local density is not the global integrated Hessian. Explain precisely whether those extras are divergences/Bochner terms and whether the global saddle formula is valid. Also check that an O(t^2) conformal correction to exact constant scalar curvature leaves the coefficient unchanged by Lemma 67.1. Give a proof-quality memo, not a procedural checklist.

## Output

# Verification memo: second variation of $P-8\pi^2|c_1^-|^2$ along the twisted Teichmüller mode on $\Sigma_1(K_1)\times\Sigma_2(K_2)$

## 0. Result

The saddle mechanism is real, but the twist coefficient in the Step-67 formula is too large by a factor of 2. For $k=fQ$, the correct $t^2$ Taylor coefficient is

$$
\boxed{\;8\pi^2\big(p-|c_1^-|^2\big)_2(fQ)=\frac{\mu}{4}\,\big[\mu+(K_1-K_2)\big]\,\|fQ\|_2^2\;}
\qquad\text{not}\qquad \frac{\mu}{4}\big[\mu+2(K_1-K_2)\big]\|fQ\|_2^2 .
$$

Status of the four inputs:

- $\mathrm{Ric}''_1=\tfrac{\mu}{2}k$ is correct.
- $\rho'_{0,1}=0$ is correct. In fact the whole $J_t$-invariant Ricci form is stationary.
- $\int u_2=\tfrac{\mu}{4}\|k\|^2$ is wrong in the normalization the twist identity requires. The torsion data are $\int|\nabla\omega|^2_2=\mu\|k\|^2$ (tensor norm) and $\int|a_1|^2=\tfrac{\mu}{8}\|k\|^2$.
- $(\rho_0,t_2^-)=-\tfrac{(K_1-K_2)\mu}{8}\|k\|^2$ is wrong. The correct value is $-\tfrac{(K_1-K_2)\mu}{16}\|k\|^2$.

The coordinate scripts contain two kinds of extra terms relative to the generator:

- The $n$-dependent terms are a pointwise Gauss–Bonnet divergence. They integrate to zero.
- The $n$-independent term $-(K_1-K_2)\mu/4$ in their `difference` field is a genuine integrated discrepancy. The scripts therefore independently confirm the corrected coefficient.

## 1. Exact structure of the family

Write $A=g_1^{-1}Q$, which is $g_1$-self-adjoint, tracefree and anticommutes with $J_1$. Set $G_t=g_1e^{tf(y)A}$ on $T\Sigma_1$, with $g_2$ unchanged and $y\in\Sigma_2$. Then:

- $\det G_t=\det g_1$, so $d\mu$ is fixed.
- $\omega_1$ is the $G_t$-area form, so $\omega=\omega_1+\omega_2$ is fixed.
- $J_t=e^{-tfA}J_1$ is $G_t$-compatible.
- The splitting stays orthogonal, so $*_t\omega_1=\omega_2$ exactly. Hence $\omega_1$ and $\omega_2$ remain $g_t$-harmonic, and $\omega_1-\omega_2$ remains ASD with fixed norm.

Consequently $|c_1^-|^2_{g_t}$ is exactly constant in $t$. The Hessian of $F=P-8\pi^2|c_1^-|^2$ is the second variation of $P=\int|\mathrm{Ric}^\circ|^2d\mu$, by Chern–Gauss–Bonnet. No appeal to Lemma 67.1 is needed for this reduction.

Projection to $\Sigma_2$ is a Riemannian submersion with the following properties:

- The horizontal distribution is integrable, so the O'Neill tensor $A=0$.
- The horizontal leaves are totally geodesic, since $\Gamma^U_{XY}=0$.
- The fibres have second fundamental form $T_UV=-\tfrac12(\partial G)(U,V)$.
- The fibres are minimal, since $\operatorname{tr}G^{-1}\partial G=t\,df\operatorname{tr}A=0$.

The O'Neill / Kaluza–Klein formulas are verified on the warped case $g_2+e^{2\varphi}\delta$. Using $G^{-1}\partial_jG=t f_jA$ and $A^2=\tfrac12|Q|^2I$ in dimension 2, they give:

- **Vertical block.** $\mathrm{Ric}_{V}=K_sG-\tfrac12\Delta^{\rm tr}_yG+\tfrac12\partial^jG\,G^{-1}\partial_jG$, where $K_s$ is the curvature of $G_s=g_1e^{sA}$ at $s=tf(y)$. The two $|df|^2$ terms cancel exactly ($\mp\tfrac{t^2}{4}|df|^2|Q|^2G$), leaving
 $$\mathrm{Ric}_V=K_sG+\tfrac{t\mu f}{2}\,GA .$$
 The first-order part $t(K_1+\mu/2)k$ agrees with the Bianchi-gauge Lichnerowicz formula, using $\nabla^*\nabla Q=-2K_1Q$ and $\mathring RQ=-K_1Q$.
- **Horizontal block.** $\mathrm{Ric}_H=K_2g_2-N$, with $N=\tfrac{t^2}{4}|Q|^2\,df\otimes df$.
- **Mixed block.** $\mathrm{Ric}_{UX}=O(t^2)$. The $O(t)$ part is $\tfrac t2 f_X\,\mathrm{div}_{g_1}Q=0$. The mixed block therefore enters $|\mathrm{Ric}^\circ|^2$ only at $O(t^4)$.

**$J_t$-type of each piece.**

- $K_sG$ is $J_t$-invariant.
- $GA$ is $J_t$-anti-invariant, because $AJ_t=-J_tA$.
- Hence $\mathrm{Ric}''_1=\tfrac{\mu}{2}k$, and $\rho_t=K_1\omega_1+K_2\omega_2+O(t^2)$, so $\rho'_0=0$. Both statements are confirmed.

## 2. The integrated Hessian

With $s=2K_s+2K_2-\operatorname{tr}N$ and $\operatorname{tr}N=\tfrac{t^2}{4}|Q|^2|df|^2$,

$$
|\mathrm{Ric}^\circ|^2=\operatorname{tr}\mathrm{Ric}^2-\tfrac{s^2}{4}
=(K_s-K_2)^2+\tfrac{t^2\mu^2f^2}{4}|Q|^2+\tfrac{t^2}{4}(K_1-K_2)|Q|^2|df|^2+O(t^3).
$$

There is no $O(t)$ term, even pointwise. This is consistent with criticality.

The term $2(K_1-K_2)(K_s-K_1)$ integrates to zero fibrewise by Gauss–Bonnet, because $\int_{\Sigma_1}K_s\,dA_{G_s}=2\pi\chi$ and $dA_{G_s}=dA_{g_1}$. Using $\int_{\Sigma_2}|df|^2=\mu\int f^2$ then gives the boxed formula.

**Check at $K_1=K_2$.** At a Kähler–Einstein product $P\ge0$ and $P=0$, so $P_2=\|(\mathrm{Ric}^\circ)'\|^2=\tfrac{\mu^2}{4}\|k\|^2$. The formula reproduces this.

## 3. Torsion computed directly: where the factor 2 enters

The only nonzero components of $\nabla\omega$ are $(\nabla_U\omega)(V,X)$. In an orthonormal frame with $A=\mathrm{diag}(\alpha,-\alpha)$, $|Q|^2=2\alpha^2$ and $\nabla f=|df|e_3$:

$$
\nabla_{e_1}\omega=\tfrac{t\alpha|df|}{2}(e^{14}+e^{23}),\qquad
\nabla_{e_2}\omega=\tfrac{t\alpha|df|}{2}(e^{13}-e^{24}).
$$

Three facts follow.

1. **Tensor norm.** $|\nabla\omega|^2_{\rm tensor}=t^2|Q|^2|df|^2$. This matches the generator's $|(\nabla\omega)_1|^2$. It also matches Blair–Ianus: directly, $\int s_t=\text{const}-\tfrac{t^2}{4}\mu\|k\|^2$, which equals $-\tfrac14E_2$.
2. **Torsion one-form.** In the form $\nabla\omega=a\otimes\phi+Ja\otimes J\phi$ with $|\phi|^2=2$ (form norm), one has $|a|=\tfrac{t\alpha|df|}{2}$. So $|a|^2=\tfrac{t^2}{8}|Q|^2|df|^2$ and $a\in T^*\Sigma_1$.
3. **Twist pairing.** $a\wedge Ja=|a|^2\omega_1$, so $(a\wedge Ja)^-=\tfrac{|a|^2}{2}(\omega_1-\omega_2)$. Hence
 $$(\rho_0,t^-_2)=-r\!\int|a_1|^2=-\tfrac{(K_1-K_2)\mu}{16}\|k\|^2,\qquad r=\tfrac{K_1-K_2}{2}.$$

**Normalization mismatch.** The Step-66 identity $2\|t^-\|^2=\int u^2$ with $t^-=-(a\wedge Ja)^-$ forces $u=|a|^2=|\nabla\omega|^2_{\rm tensor}/8$. That is $|\nabla\omega|^2/4$ only if the 2-form slot carries the form norm. Generator eq. (5) combined $u=|\nabla\omega|^2/4$ with the tensor-norm value, which doubles $\int u_2$ and hence the twist term.

**Corrected inputs reproduce the direct result.** Substituting into $\mathfrak Q=\|\mathrm{Ric}''_1\|^2-4(\rho_0,t_2^-)+2\|\rho'^{\perp}\|^2$ gives $\tfrac{\mu^2}{4}+\tfrac{(K_1-K_2)\mu}{4}$, exactly the direct value.

**Residual check on the AK formula.** The same normalization fixes the remaining squares: $2\|\rho^{*\prime\prime}_1\|^2+4\|W_{3,1}\|^2=\tfrac{\mu^2}{4}-\tfrac{K_2\mu}{2}\ge0$. An independent evaluation of $W_3$ and $\rho^{*\prime\prime}$ for this mode would test Prop. 63.AK's coefficients. The same $u$-normalization question applies to the $s\int u_2$ term written in Step 67 §3. Neither of these is checked here.

The file `step68_product_saddle_global_exact.py` hardcodes `rho_t=-(K1-K2)mu/8`. It therefore reproduces the error and is not independent evidence.

## 4. Reconciling the coordinate scripts

After substituting $f''=-\mu f/(B^2v^2)$ and integrating $f'^2$ by parts, all three jets give

$$
\text{ratio}=\tfrac{\mu^2}{4}+\tfrac{(K_1-K_2)\mu}{4}+\tfrac{c_n}{4}K_1(K_1-K_2),\qquad c_n=6,16,30 .
$$

**The $\mu$-dependent part is jet-independent.** It is exactly the corrected integrated coefficient.

**The $c_n$ term is $2(K_1-K_2)(K_s-K_1)/(t^2f^2|Q|^2)$, a pointwise Gauss–Bonnet density.**

- At $z=i$, $q=z^n$ gives $|d|Q||^2/|Q|^2=(n+2)^2A^2=4,9,16\,(\times A^2)$.
- The values $c_n$ fit $K_s-K_1=-\tfrac{s^2}{4}\big(|d|Q||^2+K_1|Q|^2\big)+O(s^3)$ exactly. Two parameters are fitted, and the third jet confirms the form.
- Using the Kato equality $|\nabla Q|^2=2|d|Q||^2$ for holomorphic quadratic differentials and the Bochner identity $\tfrac12\Delta^{\rm tr}|Q|^2=|\nabla Q|^2+2K_1|Q|^2$, this becomes a pure Laplacian:
 $$K_s-K_1=-\tfrac{s^2}{16}\Delta^{\rm tr}_{\Sigma_1}|Q|^2 .$$
 It is a divergence and integrates to zero.
- This pointwise formula is inferred from the jets. The global result does not depend on it, since Gauss–Bonnet alone kills the integral.

**Summary.** Pointwise density and integrated Hessian differ only by this divergence. The scripts' `difference` field, $(K_1-K_2)(c_nK_1-\mu)/4$, mixes the divergence (the $c_n$ part) with the genuine factor-2 discrepancy $-(K_1-K_2)\mu/4$.

## 5. Conformal correction to exact constant scalar curvature

The family has $s_t=s_0+O(t^2)$, but not constant: $K_s$ varies in $x$ and $\operatorname{tr}N\ne0$.

- Put $\tilde g_t=e^{2t^2w}g_t$, with $w$ solving $(6\Delta-2s_0)w=-(s_2-\bar s_2)$. The operator is invertible on all functions since $s_0<0$.
- Then $F(\tilde g_t)=F(g_t)+t^2DF(g_0)(2wg_0)+O(t^3)$.
- $DF(g_0)$ vanishes on conformal directions independently of Lemma 67.1: $\int|W|^2$ and $|c_1^-|^2$ are conformally invariant, and $\tfrac{d}{d\varepsilon}\int s^2d\mu=12s_0\int\Delta\varphi=0$ at constant $s_0$.
- Lemma 67.1 also gives full criticality, so the Hessian at $g_0$ depends only on the velocity $k$. The velocity has $\operatorname{tr}k=0$, $\delta k=0$ and $s'(k)=0$, so it lies in the slice.

The $t^2$ coefficient is therefore unchanged.

## 6. Consequences

**Thresholds.**

- For the mode $fQ$: $\mathfrak Q(fQ)<0\iff 0<\mu<K_2-K_1$.
- For the swapped mode: $\mathfrak Q(hQ_2)=\tfrac{\lambda}{4}(\lambda+K_2-K_1)\|hQ_2\|^2$.
- The necessary condition for local Kähler minimality is $\lambda_1(\Sigma_2)\ge K_2-K_1$ when $K_1<K_2$. This replaces the threshold $2(K_2-K_1)$.

**The stated example.**

- With $K_1=-2$, $K_2=-1$, $\mu=1$, the mode is now exactly marginal ($\mathfrak Q=0$), not negative.
- A negative direction needs $\lambda_1(\Sigma_2)<1$ for the curvature $-1$ surface. Pinching a separating geodesic still gives this.

**A stronger general statement.** Scale invariance lets the curvature ratio $|K_1|/|K_2|$ be chosen freely by adjusting areas. Cheng's bound gives $\lambda_1\le\tfrac14|K_2|+o(1)$ as $\operatorname{diam}\Sigma_2\to\infty$. Hence:

- if $|K_1|/|K_2|>5/4$ and $\Sigma_2$ has large genus, every such product is a saddle;
- for $1<|K_1|/|K_2|$ close to 1, the sign depends on $\lambda_1(\Sigma_2)$.

**Meaning for $c_K$.** Whenever the threshold is met, the mode has $\ell_2-2q^2d_2<0$, so $c_K<2$. The constant-scalar metrics $\tilde g_t$ satisfy $P<8\pi^2|c_1^-|^2$ and are non-Kähler and non-aligned. Theorem 67.K's $c_K>0$ is untouched.

**Effect on the rest of the Step-67 programme.**

- The structural conclusions of the generator's §§3–6 survive, with the halved twist coefficient.
- The block-matrix completion in §5 must use $\int|a|^2$, i.e. $|\nabla\omega|^2_{\rm tensor}/8$, in every twist entry.
- The competition is now $\mu^2/4$ against $|K_1-K_2|\mu/4$.