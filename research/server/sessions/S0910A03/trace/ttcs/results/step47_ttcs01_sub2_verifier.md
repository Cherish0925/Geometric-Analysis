# TTCS Independent Branch Record

```json
{
  "step_id": 47,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step47_consolidated_negative_IL_gap_theorem.md",
    "Sessions/S0910A03/workspace/notes/step43_terminal_density_G_lemma.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Verify the logical chain of the consolidated restricted negative IL gap theorem in the provided file. Focus on these five load-bearing points:

1. COLLAPSE CANCELLATION (§3d): The claim is that on a good ball where the volume-averaging maximal function satisfies M_vol(|Rm|²)(x) ≤ κ², the initial curvature energy satisfies K₂ ≤ (1+κ²)Vol(B), and the Sobolev constant S ≤ Cr²/√Vol(B). Therefore γ = S·K₂^{1/2} ≤ Cr²√(1+κ²), independent of Vol. Check: is this computation correct? Does the volume-averaging Hardy-Littlewood maximal inequality hold under Ric ≥ -3g with the stated constants? Is the Maheux-Saloff-Coste Sobolev inequality correctly stated?

2. TERMINAL POINT SELECTION (§7b-7c): The claim is that min_{x∈Π} D(x,T) ≤ (119C₁/α)δ² → 0, and then a subsequence of pullback metrics on B_R(0) ⊂ R⁴ converges C^∞ to an Einstein limit with D_h(0) = 0. Check: is the minimum-of-average-gives-small-minimum argument correct? Does the pullback chart have noncollapsed volume (Rauch comparison under bounded curvature)? Does C^k convergence pass D to the limit?

3. SPECTRAL DETERMINATION (§7d): From D_h(0)=0 on the Einstein limit with s=-4, the claim is |W⁺|² = 1/24 and G = 0, forcing Spec(W⁺) = (-1/6,1/12,1/12). Check the algebra: G = 4ξ(3-ξ) where ξ = w + √(2/3)|W⁺|, so G=0 forces ξ=0, hence w=-1/6.

4. PROJECTOR-BOCHNER (§7e): The claim is that on any connected Einstein 4-manifold with Ric=-g and W⁺ spectrum (-1/6,1/12,1/12) at one point, the simple eigenform is parallel (from δW⁺=0 + constant eigenvalue), so ∇W⁺=0 and |W⁺|²=const, and then the Bochner identity gives 0 = -1/8, a pointwise contradiction. Check: is the projector argument correct for a LOCAL domain (not just closed manifolds)?

5. SELF-IMPROVING FIRST-EXIT (§5h): The drift estimate d(T) ≤ Cδθ^{2/3}r² is used to keep Sobolev constants comparable. Check: does the bilipschitz comparison from small drift transport the local Sobolev constant correctly? Is the self-improving closure non-circular?

## Output

## Verification memo — consolidated restricted −g‑normalized IL gap theorem (Step 47)

I checked the five load‑bearing points against the algebra, the analytic inputs, and the internal cross‑references (Steps 6, 43). Four of the five are correct as stated or need only a presentational strengthening. The terminal spectral contradiction (Point 4) contains a genuine unclosed step that sits exactly on top of the collapsed geometry that Step 6 shows is unavoidable for a fixed $M$. I give the substance point by point, then the consolidated statement.

---

### Point 1 — Collapse cancellation (§3d): correct, and the mechanism is genuine

The arithmetic $\gamma_\alpha=\mathcal S_\alpha K_{2,\alpha}(0)^{1/2}\le \frac{Cr^2}{\sqrt{\operatorname{Vol}B_{6r}}}\cdot\sqrt{(1+\kappa_0^2)\operatorname{Vol}B_{6r}}=Cr^2\sqrt{1+\kappa_0^2}$ is right, and the two analytic ingredients are correctly stated for $n=4$:

- **Curvature energy.** Since the maximal function takes its supremum over all $\rho\le1$, membership $x_\alpha\in G$ controls the single scale $\rho=6r$ (this needs $6r\le1$, a mild constraint on $r$). Hence $\int_{B_{6r}}|\mathrm{Rm}|^2\le\kappa_0^2\operatorname{Vol}B_{6r}$ and $K_{2,\alpha}(0)\le(1+\kappa_0^2)\operatorname{Vol}B_{6r}$. Correct.
- **Sobolev constant.** The Maheux–Saloff‑Coste local inequality under $\operatorname{Ric}\ge-3g$ carries the factor $R^2/\operatorname{Vol}(B_R)^{2/n}$, and $2/n=1/2$ in dimension four. So $\mathcal S_\alpha\le Cr^2/\sqrt{\operatorname{Vol}B_{6r}}$ is the correct form. This $\operatorname{Vol}^{-1/2}$ is exactly what cancels the $\operatorname{Vol}^{1/2}$ from $K_2^{1/2}$. The cancellation is a real feature of the critical dimension where $\int|\mathrm{Rm}|^2$ is the scale‑invariant $L^{n/2}$ energy.
- **Doubling / weak type.** Bishop–Gromov under $\operatorname{Ric}\ge-3g$ gives uniform doubling for $\rho\le1$ (dimension‑only ratio), and the Coifman–Weiss weak‑type inequality on the doubling space gives (3.1) with $C_{\rm HL}$ depending only on the doubling constant. Consistent.

One thing to record for downstream use: $\gamma\le C'r^2$ suffices for the low‑moment absorption (5.1)–(5.2), but §5e itself notes that this two‑factor absorption does not survive the high‑$p$ ladder (it would need $\gamma\lesssim1/p$), which is why (5.4)–(5.5) switch to a three‑factor Hölder+Young argument. That internal switch is acknowledged and self‑consistent.

**Verdict: sound.**

---

### Point 2 — Terminal point selection and pullback (§7b–7c): correct, with one clarification that turns out to be decisive downstream

- **Minimum vs. average.** $\min_\Pi\mathfrak D\le\frac{1}{\operatorname{Vol}\Pi}\int_\Pi\mathfrak D\le\frac{119C_1}{\alpha}\delta^2\to0$ is elementary and correct, using $\operatorname{Vol}\Pi\ge\alpha\operatorname{Vol}M$ and $\int_M\mathfrak D\le119Q(T)$, $Q(T)\le C_1\delta^2\operatorname{Vol}M$.
- **Noncollapsed pullback.** The statement $\operatorname{Vol}_{\tilde g_i}(B_R)\ge c_1R^4$ is correct **because $\tilde g_i=\exp_{x_i}^*g_i$ lives on the tangent ball $B_R(0)\subset T_{x_i}M$.** Under $|\sec|\le\Lambda$ the conjugate radius is $\ge\pi/\sqrt\Lambda$, so for $R<\pi/\sqrt\Lambda$ the map $\exp_{x_i}$ is an immersion and Günther's Jacobian lower bound makes the pullback density bounded below. This is not a statement about volumes of balls in $M$ (which do collapse — see below); it is intrinsic to the tangent‑space pullback and is valid.
- **Passage of the Einstein condition.** The pointwise bound (5.5) $\|aE(T)\|_\infty\le C\delta\theta^{-1/3}$ holds *uniformly on the plateau* (where $a=1$), so $|E(T)|\to0$ in $L^\infty(\Pi)$. Together with the Shi‑derived $C^k$ bounds this yields $\operatorname{Ric}_h=-h$ (hence $s_h\equiv-4$, $E_h\equiv0$) on the **whole** limit ball $B_R(0)$. Correct.
- **Passage of $\mathfrak D$.** By $C^k$ convergence $\mathfrak D(\tilde g_i)\to\mathfrak D_h$ uniformly, and at the origin $\mathfrak D(\tilde g_i)(0)=\mathfrak D(g_i)(x_i)\to0$, so $\mathfrak D_h(0)=0$. Correct — **but only at the origin.**

The important distinction to flag: on the limit, only $\operatorname{Ric}_h=-h$ (from the *uniform pointwise* defect bound) and the *single‑point* value $\mathfrak D_h(0)=0$ (from the min‑of‑average) are established. The Weyl part of $\mathfrak D$, namely $(s+8\sqrt6|W^+|)^2$ and $G$, is controlled only in $L^1$ by the gauge‑theoretic bound $\int\mathfrak D\le119Q$; it does **not** come with a pointwise or uniform bound on the plateau. This is what breaks Point 4.

**Verdict: the pullback and the Einstein/origin conclusions are sound; the Weyl spectrum of $h$ is pinned only at the single origin point.**

---

### Point 3 — Spectral determination (§7d): correct, verified line by line

With $s=-4$, $|W^+|^2=1/24$, $u=|W^+|=1/(2\sqrt6)$, $\alpha=\sqrt{2/3}$:

- $2\alpha u=2\sqrt{2/3}\cdot\frac{1}{2\sqrt6}=\sqrt{2/3}/\sqrt6=1/3$, so $f=\tfrac23s-2\alpha u=-\tfrac83-\tfrac13=-3$. ✓
- $\alpha u=\sqrt{2/3}\cdot\frac{1}{2\sqrt6}=1/6$, so $\xi=w+1/6$. For a trace‑free symmetric $3\times3$ with $\sum\lambda_i^2=1/24$, the smallest eigenvalue is $\ge-\sqrt{2/3}\,|W^+|=-1/6$, so $\xi\ge0$; and $w\le0$ gives $\xi\le1/6$. ✓
- $b=f+2\xi=-3+2\xi\in[-3,-8/3]<0$, so $b_-=b$ and $G=f^2-b^2=9-(-3+2\xi)^2=12\xi-4\xi^2=4\xi(3-\xi)$. ✓
- $3-\xi>0\Rightarrow G=0\iff\xi=0\iff w=-1/6$; then $\lambda_1+\lambda_2=1/6$, $\lambda_1^2+\lambda_2^2=1/24-1/36=1/72$, so $(\lambda_1-\lambda_2)^2=0$, $\lambda_1=\lambda_2=1/12$. ✓

$\operatorname{Spec}(W^+)(0)=(-1/6,1/12,1/12)$ at the origin is forced. Lemma 1.1/1.2 in Step 43 are also internally consistent.

**Verdict: sound.**

---

### Point 4 — Projector–Bochner contradiction (§7e): the projector lemma is valid locally and the Bochner numerics are correct, but the application rests on an unproved constancy step

Two sub‑parts are fine:

- **Local projector lemma (Step 6).** The computation is purely pointwise/local: from $\delta W^+=0$ and a *constant* simple eigenvalue $\lambda\ne\mu$ (double), write $W^+=\mu I+(\lambda-\mu)P_\omega$; contracting $(\nabla^a\omega_{ab})\omega_{cd}+\omega_{ab}\nabla^a\omega_{cd}=0$ with $\omega^{cd}$ (constant length) gives $\delta\omega=0$, then $\omega_{ab}\nabla^a\omega_{cd}=0$, and nondegeneracy $\omega_a{}^c\omega_c{}^b=-\delta_a{}^b$ gives $\nabla\omega=0$. Nothing here needs global compactness; it holds on any open $(B_R,h)$ where the simple eigenline is defined. This agrees with Derdziński 1983 Prop. 5. **Valid on a local domain.**
- **Bochner numerics.** With $\det W^+=(-1/6)(1/12)^2=-1/864$: $s|W^+|^2=-\tfrac16$, $-36\det W^+=+\tfrac1{24}$, so $\nabla W^+=0$ forces $0=-\tfrac16+\tfrac1{24}=-\tfrac18\ne0$. ✓ Consistent with Step 6 eq. (4) ($|\nabla W^+|^2=1/16$). The $|W^+|^2=\sum\lambda_i^2$ convention is used consistently.

The problem is the hinge between them. §7e step 1 asserts that the simple eigenvalue $-1/6$ is **constant** in a neighbourhood of the origin "by continuity and $|W^+|^2=1/24\ne0$." Continuity gives that the smallest eigenvalue is *near* $-1/6$ and *simple* (an open condition) near the origin — it does **not** give that it equals the constant $-1/6$. The projector lemma's hypothesis is exactly *constant* eigenvalues; without constancy the lemma does not apply, and $\nabla W^+=0$ is not obtained. The Bochner identity evaluated only at the origin reads $\Delta|W_h^+|^2(0)=2|\nabla W_h^+|^2(0)-\tfrac18$: one equation in two unknowns, no contradiction.

The correct route to constancy is $\mathfrak D_h\equiv0$ on $B_R$, which by Lemma 1.2 pointwise gives $|W_h^+|^2\equiv1/24$, $G_h\equiv0$, hence $\operatorname{Spec}(W_h^+)\equiv(-1/6,1/12,1/12)$ everywhere, and then the projector lemma does apply. But $\mathfrak D_h\equiv0$ is not what §7c delivers. To get it one needs $\int_{B_R(0)}\mathfrak D(\tilde g_i)\,d\mathrm{vol}_{\tilde g_i}\to0$, and here the multiplicity of the tangent pullback intervenes:
$$
\int_{B_R(0)}\mathfrak D(\tilde g_i)\,d\mathrm{vol}_{\tilde g_i}=\int_M \mathfrak D(g_i)\,N_i(x)\,d\mathrm{vol},\qquad N_i(x)=\#\{y\in B_R(0):\exp_{x_i}(y)=x\}.
$$
When $\exp_{x_i}$ is injective (unit‑scale noncollapsing), $N_i\equiv1$ and $\int_{B_R(0)}\mathfrak D(\tilde g_i)\le\int_M\mathfrak D\le119C_1\delta_i^2\operatorname{Vol}\to0$ (for fixed $A$), so $\mathfrak D_h\equiv0$ and the whole chain closes. But Step 6 eq. (10) shows precisely that for a fixed critical $M$ any escaping sequence must collapse at unit scale everywhere while $\operatorname{Vol}\to32\pi^2A/9$ stays fixed (so the diameter diverges). A short‑time flow of duration $T=\theta r^2$ preserves collapse (volume element evolves by $-a(s+4)$ with $|s+4|\le2\delta$; injectivity radius changes by a bounded factor). Under collapse the sheet number $N_i$ of the tangent‑ball pullback is unbounded, and $N_i\!\int_M\mathfrak D$ need not vanish. Since the Weyl part of $\mathfrak D$ is only $L^1$‑controlled (by $\int\mathfrak D\le119Q$), there is no pointwise route either.

Consequently a limit $h$ that is Einstein ($\operatorname{Ric}_h=-h$) on $B_R(0)$ with $\mathfrak D_h(0)=0$ at a single point but $\mathfrak D_h>0$ elsewhere is not excluded by anything in the note. The projector lemma only forbids the calibrated spectrum from being *constant*; it says nothing about an isolated point value. This is exactly the "unwrapping preserves the small LeBrun deficit" question that Step 6 §"what changes and what remains" states as unresolved, together with its warning that the fixed‑$A$ absolute vanishing must not be assumed in the collapsed regime.

**Verdict: the projector lemma and the Bochner numbers are correct; the terminal contradiction is rigorous in the unit‑scale noncollapsed regime (there $N_i\equiv1$ gives $\mathfrak D_h\equiv0$, constant spectrum, and $\nabla W^+=0$ vs. $-1/8$). In the collapsed regime — which Step 6 shows is the operative one for a fixed critical $M$ — the step from "$\mathfrak D_h(0)=0$ at one point" to "constant Weyl spectrum in a neighbourhood" is not established, and the justification "by continuity" is not a proof of constancy.** This is the single unclosed link in the assembly.

---

### Point 5 — Self‑improving first‑exit (§5h): transport and non‑circularity are fine; one constant needs its $\theta$‑dependence displayed

- **Bilipschitz transport.** If the drift keeps $|g(t)/g(0)-\mathrm{Id}|\le\psi(d_0)$, i.e. $(1-\epsilon)g(0)\le g(t)\le(1+\epsilon)g(0)$, then volumes, gradient norms, and $L^p$ norms all change by factors bounded in $\epsilon$, so the local Sobolev constant of $g(t)$ is comparable to that of $g(0)$. Correct and standard.
- **Non‑circularity.** The parameter chain $\kappa_0\to r\to\theta\to\delta_0$ is a valid dependency order: $\kappa_0^2=4C_{\rm HL}\Lambda$ (from $\Lambda$), $r\le(\gamma_0/C')^{1/2}$ (from the Moser threshold, independent of $\delta,\theta$), $\theta$ from the curvature Moser time scale, $\delta_0$ last from $C'\delta_0\theta^{2/3}r^2<d_0$. The first‑exit closure assumes $K_2\le2K_2(0)$ and $d\le d_0$ on $[0,\tau)$, derives (5.1)–(5.7) using only those hypotheses (plus the transported Sobolev constants), and concludes strict improvement, hence $\tau=T$. No conclusion is used in its own derivation.
- **One point to make explicit.** The strict improvement $K_2(T)<2K_2(0)$ requires the constant in (5.1) to be of the form $e^{C\theta}$ (so $\to1$ as $\theta\to0$), matching (5.7) $Q(T)\le e^{C\theta}Q(0)$. As written, (5.1) reads "$\le CK_2(0)$" with a generic $C$; the closure sentence "$K_2(T)\le CK_2(0)<2K_2(0)$" is legitimate only once this $\theta$‑dependence is shown. This is a presentational fix, not a structural one.
- **Load‑bearing import.** The drift being $O(\delta)$ hinges on (5.5) $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$ being *linear in $\delta$* (defect stays small proportionally to its initial size). This is plausible from the near‑homogeneous parabolic evolution of $E$, and the $(r^2/t)^{1/3}$ smoothing exponent is dimensionally the right parabolic $L^\infty\!\leftarrow\!L^p$ gain, but the derivation lives in Step 39 and cannot be re‑checked from this note alone.

**Verdict: mechanism sound; display the $\theta$‑dependence in (5.1), and note that (5.5)'s linear‑in‑$\delta$ propagation is the imported input carrying the $O(\delta)$ drift.**

---

### Consolidated statement

The chain is internally consistent and the calibration is arithmetically exact — I re‑derived the profile independently: with $|W^+|\to1/(2\sqrt6)$, Chern–Weil $\frac{\operatorname{Vol}}{6\pi^2}+\frac{\int|W^+|^2}{2\pi^2}=\frac{2A}{3}$ forces $\operatorname{Vol}\to\frac{32\pi^2A}{9}$ and $\int|W^+|^2\to\frac{4\pi^2A}{27}$, matching §2. Points 1, 3, and 5 are correct (Point 5 needs the $\theta$‑dependence of (5.1) written out). Point 2 is correct, with the clarification that only $\operatorname{Ric}_h=-h$ on all of $B_R$ and $\mathfrak D_h(0)=0$ at the single origin point pass to the limit.

The decisive item is Point 4. The terminal spectral contradiction is complete **only when the tangent‑ball pullback has bounded sheet number**, i.e. when the sequence does not collapse at unit scale — because then the $L^1$ gauge deficit $\int_M\mathfrak D\to0$ localizes to $\mathfrak D_h\equiv0$, the Weyl spectrum is genuinely constant, and the local projector lemma delivers $\nabla W^+=0$ against the Bochner value $-1/8$. Step 6 eq. (10) shows that for a fixed critical $M$ every escaping sequence must collapse at unit scale everywhere, so the collapsed regime is not a corner case but the operative one. The smoothing module produces bounded (indeed small) curvature on the plateau, but it does not produce unit‑scale noncollapsing, so the multiplicity of $\exp_{x_i}$ on $B_R(0)$ is not controlled, and the passage from the single‑point value $\mathfrak D_h(0)=0$ to a constant neighbourhood spectrum — the exact hypothesis the projector lemma needs — is not supplied. The §7e phrase "constant … by continuity" states the needed conclusion without proving it.

What would close it, stated as concrete mathematical substance: either (i) a pointwise or uniform bound on the Weyl part $(s+8\sqrt6|W^+|)^2+G$ on the plateau (not merely the $L^1$ bound from $\int\mathfrak D\le119Q$), so that $\mathfrak D_h\equiv0$ on $B_R$; or (ii) an elliptic propagation on the Einstein limit showing that a nonneg $\mathfrak D_h$ with an interior zero (a global minimum $=0$) satisfying a differential inequality of the form $\Delta\mathfrak D_h\le C\mathfrak D_h$ must vanish identically — which would require exhibiting such an inequality for $\mathfrak D_h=(8\sqrt6|W_h^+|-4)^2+G_h$ on $\operatorname{Ric}=-h$ manifolds using the Weitzenböck $\Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+$; or (iii) a controlled local unwrapping of collapsed plateau balls to noncollapsed charts preserving the small pulled‑back deficit, which is precisely the question Step 6 records as open. Until one of these is in hand, the assembled result stands rigorously for the unit‑scale noncollapsed situation, with the collapsed situation — the one forced on a fixed critical $M$ — carrying the unclosed constancy step.

The §9 statement that this covers "every Riemannian metric on every manifold in the $q\ge0$ IL geography" is therefore stronger than what the terminal module presently supports; the supported content is the $-g$‑normalized IL gap on the noncollapsed branch, which coincides with Step 6's regular‑patch contradiction. The above‑critical corollary ($q/A\ge c>0\Rightarrow\delta_0\ge\min(1/4,\sqrt{3c/16})$) is independent of the smoothing/terminal module and, per §2, uses only the calibration algebra and the SW monopole bound; it is not touched by the Point 4 issue.