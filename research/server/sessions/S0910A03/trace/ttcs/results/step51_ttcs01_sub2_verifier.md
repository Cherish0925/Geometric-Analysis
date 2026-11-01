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

## Verification Memo — Normalized cutoff flow $L^p$ curvature energy estimate (Step 51)

I reconstructed the three computations independently from the conformal variation formulas and from Yang's Theorem A.7 display. The central identity is correct; several displayed signs are off in ways that do not affect the headline identity but should be repaired; and one analytic step (the additive volume source through the Moser levels) is asserted rather than derived and is the piece that actually needs work.

### 1. Metric-inverse count and the $+4a|\mathrm{Rm}|^2$ reaction — confirmed

From $\partial_t g_{ij} = -2a\,g_{ij}$ (the $h_2$ part), differentiating $g^{ik}g_{kj}=\delta^i_j$ gives
$$\partial_t g^{ik} = -g^{im}(\partial_t g_{ml})g^{lk} = 2a\,g^{ik},$$
so each inverse metric factor contributes $+2a$. This sign is what the note uses, and it is right.

$|\mathrm{Rm}|^2 = R_{ijkl}R_{pqrs}g^{ip}g^{jq}g^{kr}g^{ls}$ carries **four** inverse-metric factors, hence the metric-derivative part is $4\cdot 2a\,|\mathrm{Rm}|^2 = 8a|\mathrm{Rm}|^2$. The tensor part uses the conformal variation of the fully lowered Riemann tensor. Writing $\partial_t g = 2\dot u\, g$ with $\dot u=-a$, the first-order variation is
$$\partial_t R_{ijkl} = 2\dot u\,R_{ijkl} - (g\owedge\nabla^2\dot u)_{ijkl} = -2a\,R_{ijkl} + (g\owedge\nabla^2 a)_{ijkl},$$
(the $du\otimes du$ and $|du|^2 g$ pieces of the conformal law are quadratic in $u$ and drop at first order). Then $2\langle\mathrm{Rm},\partial_t\mathrm{Rm}\rangle = -4a|\mathrm{Rm}|^2 + 2\langle\mathrm{Rm},g\owedge\nabla^2 a\rangle$, and
$$\partial_t|\mathrm{Rm}|^2\big|_{h_2} = 8a|\mathrm{Rm}|^2 - 4a|\mathrm{Rm}|^2 + 2\langle\mathrm{Rm},g\owedge\nabla^2 a\rangle = 4a|\mathrm{Rm}|^2 + 2\langle\mathrm{Rm},g\owedge\nabla^2 a\rangle.$$
The magnitude $+4a$ (i.e. $8a-4a$) is exactly the note's, so the reaction coefficient is verified.

**Sign notice (immaterial for the estimate, but the display is off):** my computation gives $+(g\owedge\nabla^2 a)$ in the tensor variation and $+2\langle\mathrm{Rm},g\owedge\nabla^2 a\rangle$ in $\partial_t|\mathrm{Rm}|^2$; the note (1.2) and (1.4) write these with a minus sign. Because only $|\langle\mathrm{Rm},g\owedge\nabla^2 a\rangle|$ is used downstream, the estimate is untouched, but (1.2)/(1.4) should be corrected for internal correctness.

The Kulkarni–Nomizu bound $|\langle\mathrm{Rm},g\owedge H\rangle|\le C_n|\mathrm{Rm}|\,|H|$ with $H=\nabla^2 a$ is correct ($g\owedge H$ is linear in $H$ with dimensional constants), and with $\nabla^2 a = 2\chi\nabla^2\chi + 2\nabla\chi\otimes\nabla\chi$ the source is bounded by $C_n\|\nabla^2\chi\|_\infty$. Confirmed.

### 2. Net $L^p$ coefficient $(2p-n)$ — confirmed, with a stated volume-sign error in (1.5)

The energy identity $\frac{d}{dt}\int F^p d\mu = \frac p2\int F^{p-2}\partial_t(F^2)\,d\mu + \int F^p\,\partial_t d\mu$ is standard. The reaction part contributes $\frac p2\int F^{p-2}(4aF^2) = 2p\int aF^p$.

The volume evolution is where the note contains a genuine sign error. The correct standard formula is
$$\partial_t d\mu = +\tfrac12\,\mathrm{tr}_g(\partial_t g)\,d\mu = \tfrac12(-2a(s+n))\,d\mu = -a(s+n)\,d\mu.$$
The note's (1.5) writes the prefactor as $-\tfrac12\mathrm{tr}_g$ and reports $+a(s+n)\,d\mu$; both are the wrong sign. Section 2.3, however, uses the correct $-a(s+n)\,d\mu$. So (1.5) is inconsistent with §2.3, and (1.5) is the erroneous one.

With the correct $-a(s+n)$, the normalization-only volume addition relative to Yang's $-as$ is $-an$, giving $-n\int aF^p$. Net normalization addition:
$$2p\int aF^p - n\int aF^p = (2p-n)\int aF^p,$$
plus the source $-p\int F^{p-2}\langle\mathrm{Rm},g\owedge\nabla^2 a\rangle$. This matches (2.7). The final identity is correct despite the (1.5) error; the messy intermediate passages in §2.2 (which first produced $2p+n$) do not propagate into the boxed result.

### 3. Critical exponent — trivially confirmed

$(2\cdot\tfrac n2 - n)=0$. The pointwise reading is also consistent: from $\partial_t|\mathrm{Rm}|^2=4a|\mathrm{Rm}|^2$ one gets $\partial_t|\mathrm{Rm}|=2a|\mathrm{Rm}|$, so $\partial_t F^p = 2paF^p$, and the volume $-n$ cancels this at $p=n/2$. The vanishing is exact and dimension-independent.

### 4. Structural compatibility with Yang A.7 — base level solid, higher levels asserted

Yang's driving inequality (A.9), obtained after the $L^{n/2}$ smallness absorbs the nonlinear Sobolev coupling, is
$$\tfrac{\partial}{\partial t}\int f^p + \int|\nabla(\chi f^{p/2})|^2 \le p\|\nabla\chi\|_\infty^2\int f^p,$$
**homogeneous** in $f$, and the Moser recursion (Lemma A.6, Theorem A.7) is built on this homogeneity. The normalized inequality reads
$$\tfrac{\partial}{\partial t}\int F^p + \int|\nabla(\chi F^{p/2})|^2 \le \big[p\|\nabla\chi\|_\infty^2 + (2p-n)+\varepsilon\big]\int F^p + C_\varepsilon\,\mathrm{Vol}.$$
Two changes: a bounded additive Grönwall coefficient $(2p-n)$ (using $a=\chi^2\le1$), and an **inhomogeneous** term $C_\varepsilon\mathrm{Vol}$.

- **Base critical level ($p=n/2$):** here $p$ is fixed, so $C_\varepsilon$ is a fixed constant, and the reaction is zero. The Grönwall (2.10) then genuinely gives self-improvement provided $\int F_0^{n/2}+C_\varepsilon\mathrm{Vol}\cdot\|\nabla\chi\|^{-2}$ stays below Yang's threshold $[(\tfrac n2+1)ec_0A]^{-1}$, which does force $\int F_0^{n/2}$ below the threshold by a fixed margin, i.e. a strictly smaller $c(n)$. This step is correct as stated.

- **Higher Moser levels ($p_k=p_0v^k\to\infty$):** this is where the note asserts rather than derives. The Young separation of $F^{p_k-1}\cdot C_n$ produces a constant $C_\varepsilon\sim\varepsilon^{-(p_k-1)}\|\nabla^2\chi\|^{p_k}$, i.e. the note's own $C_\varepsilon^{p_k}\mathrm{Vol}$ — a coefficient that grows super-exponentially in the level $k$. The note's §3.2 declares this "sublinear compared to $H(p_k)^{1+2/n}$ … absorbed into the modified Moser constant," with no estimate. Yang's recursion $H(p_{k+1})\le [\,\cdots\,]^{1+2/n}H(p_k)^{1+2/n}$ is purely superlinear and homogeneous; an additive term with a level-dependent, super-exponentially growing constant does not automatically ride through it, and the conclusion of Theorem 5.1 retains Yang's **homogeneous** $L^\infty$ form $\|\chi^2\mathrm{Rm}\|_\infty\le C'(n)C_S(t\|\nabla\chi\|^2+1)^2t^{-1}$ with no additive piece — which is exactly what one would need to prove, not assume.

  What is genuinely available and should be used: $\nabla^2 a$ is supported only where $\nabla\chi\neq0$ (the cutoff transition annulus), since $a=\chi^2$ is locally constant on the interior. So the honest, pre-Young form is $pC_n\|\nabla^2\chi\|_\infty\int F^{p-1}$, a lower-order ($F^{p-1}$) term localized to the annulus, structurally analogous to Yang's own $\|\nabla\chi\|_\infty$ cutoff terms. The needed argument is to carry $\int F^{p_k-1}$ through Lemma A.5/A.6 by interpolation between $\int F^{p_k}$ and a base $L^1$-type quantity, and to show the resulting additive contribution to $\Phi_k=H(p_k,\ldots)^{1/p_k}$ stays bounded as $k\to\infty$ — without invoking a bare $C_\varepsilon^{p_k}$. Until that exponent bookkeeping is done, the passage from the modified $L^p$ inequality to the $L^\infty$ bound is not established at the level of the rest of the note.

### 5. A mischaracterization in §4.1 (Ricci) — conclusion survives, description does not

For $u=|\mathrm{Ric}|$: the (0,2) Ricci tensor has **no** first-order conformal rescaling term ($\tilde{\mathrm{Ric}}=\mathrm{Ric}-(n-2)(\ldots)-(\ldots)g$, the $\mathrm{Ric}$ enters with coefficient 1), so $\partial_t\mathrm{Ric}_{ij}|_{h_2}=(n-2)\nabla^2 a+(\Delta a)g$ (bounded source, no reaction term). The reaction on $|\mathrm{Ric}|^2$ comes only from the **two** inverse-metric factors: $+4a|\mathrm{Ric}|^2$, i.e. $\partial_t|\mathrm{Ric}|=+2a|\mathrm{Ric}|+\cdots$. This is anti-dissipative, the opposite of the note's "$-2au$ (dissipative), helps." Because Corollary A.10 only requires a **bounded** lower-order coefficient $b$, a $+2au$ term is admissible and the Corollary still applies with modified constants — so the outcome the note wants is intact, but the sign and the "helps" description in §4.1 are wrong and should be corrected. (§4.2 bilipschitz $|\tfrac{d}{dt}\log|v|^2|\le 2a(|\mathrm{Ric}|+1)$ is correct.)

### 6. Ancillary checks

- The $\varepsilon$-uniform bound in §4.5, $|db_\varepsilon|^2/b_\varepsilon = 4\chi^2|d\chi|^2/(\chi^2+\varepsilon^2)\le 4|d\chi|^2$ with $b_\varepsilon=\chi^2+\varepsilon^2$, is correct and is the right quantity to make the DeTurck/Arzelà–Ascoli passage uniform.
- Yang's Theorem A.7 hypotheses and conclusion in the retrieved source match how the note invokes them (smallness $(\int f_0^{n/2})^{2/n}\le[(\tfrac n2+1)ec_0A]^{-1}$; output $\le CA[t\|\nabla\chi\|^2+1]^2t^{-1}$ on $0<t<\min(T,\|\nabla\chi\|^{-2})$).

### Summary of what is established vs. what needs an actual estimate

Established by independent recomputation: the inverse-metric count ($8a$), the conformal tensor reaction ($-4a$), the net $+4a|\mathrm{Rm}|^2$, the net $L^p$ coefficient $(2p-n)$, the exact vanishing at $p=n/2$, the boundedness of the KN source, and the base-level $L^{n/2}$ self-improvement with a fixed shrink of $c(n)$. These constitute the note's headline identity and it holds.

Needs repair (does not affect the identity): the KN source sign in (1.2)/(1.4); the volume-sign error in (1.5); the "$-2au$ dissipative" description in §4.1.

Needs a genuine estimate (does affect whether Theorem 5.1 as stated is proved): the propagation of the additive source $\int F^{p_k-1}$ (equivalently the note's $C_\varepsilon^{p_k}\mathrm{Vol}$) through Yang's homogeneous Moser recursion to the $L^\infty$ bound. The route is to keep the localized $F^{p_k-1}$ form, interpolate, and track the exponent arithmetic in Lemma A.5/A.6 so the additive contribution to $\Phi_k$ remains finite as $k\to\infty$; the current §3.2 assertion does not do this. The note's §7 correctly lists Yang's tame inverse, the first-exit bootstrap, and the terminal contradiction as imported/conditional, so the identity here is a real, verifiable ingredient rather than a completed reduction.