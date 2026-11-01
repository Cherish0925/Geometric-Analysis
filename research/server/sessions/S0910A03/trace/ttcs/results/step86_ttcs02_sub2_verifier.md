# TTCS Independent Branch Record

```json
{
  "step_id": 86,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step86_forced_bochner_superlevel_and_localization.md",
    "Sessions/S0910A03/workspace/scripts/step86_combined_orbit_area_energy.py",
    "Sessions/S0910A03/workspace/data/step86_combined_orbit_area_energy.json",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md"
  ]
}
```

## Task

Verify the new coupled orbit-area energy derivation in Step 86, section 9. Use the conventions dmu=e^sigma dvol, L=Delta+grad sigma dot grad, E=Ric+3g, T=tr_orbit E, e=|dU|^2, X=|grad sigma|^2, W=e+cX, F=tau_sigma(U), V=<dU,F>. Check: (i) whether the forced area trace equation is exactly L sigma=6-T and the sign; (ii) the weighted scalar Bochner formula for X and the rewrite -<grad sigma,grad T>=-div_sigma(T grad sigma)+T(6-T); (iii) after adding orbit Bochner, whether 1/2 L W >= div_sigma(V-cT grad sigma)+W^2/[2(1+c)]-(3+delta)W-D_c(delta)+P with P>=0 and D_c=12c delta+4(c+1)delta^2 really follows under operator |E|<=delta; track every cross/stress/error coefficient and correct it if needed; (iv) the norm bound on J; (v) c=1/2 reaction root series; and (vi) the conditional Cheeger inequality from W<=B and L sigma>=6-2delta, including orientation/absolute-value and domain/boundary caveats. Then assess whether this combined W identity creates a plausible noncircular bootstrap to a length-independent pointwise ceiling, or whether an explicit coupled scalar model still defeats it. Give a direct mathematical memo, preserving the restricted free-OT scope.

## Output

## Verification memo — Step 86 §9 coupled orbit–area energy $W=e+cX$

Restricted throughout to the free, orthogonally transitive $T^2$ setting of §1–§4, target $\mathbb H^2$ with $K=-1$, drift operator $L=\Delta+\nabla\sigma\cdot\nabla$ self-adjoint for $d\mu=e^\sigma d\mathrm{vol}_{\gamma_B}$, and $E=\mathrm{Ric}_g+3g$, $\|E\|_{\rm op}\le\delta$.

**Overall:** every algebraic and differential step in §9 is correct as written; I reproduced each coefficient independently and they match the note and the three JSON files. The one point that needs explicit statement is that the conditional Cheeger inequality (9.11) is intrinsically a statement on a domain whose frontier carries the $\sigma$-flux (a cusp/connector end), not on a closed manifold, and that the bootstrap it feeds is not yet a closed loop. Details below.

---

### (i) Area trace equation $L\sigma=6-T$ and its sign — correct

From the exact reduction, $\rho=e^\sigma$ obeys $\Delta_B\rho=6\rho$ (Step 79 (4.2)), i.e. $\Delta_B\sigma+|\nabla_B\sigma|^2=6$, which is exactly $L\sigma=6$ when $E=0$. Writing $\mathrm{tr}_{\rm orb}\mathrm{Ric}=T-6$ (since $\mathrm{Ric}=E-3g$ and the flat $T^2$ orbit contributes no intrinsic curvature term), the generic area relation $L\sigma=-\mathrm{tr}_{\rm orb}\mathrm{Ric}=6-T$ follows, reducing to $6$ at $E=0$ with the correct sign. The estimate $|T|\le2\delta$ is right: $T=G^{ab}E_{ab}$ is a sum over the two orbit eigenvalues of $E$, each in $[-\delta,\delta]$. Consistency: on the round cusp $\sigma=2r$ gives $L\sigma=\partial_{rr}(2r)+3\partial_r(2r)=6$, $T=0$. ✓

### (ii) Weighted scalar Bochner (9.2) and the $T$-rewrite (9.3) — correct

The exact $\infty$-Bakry–Émery Bochner identity for $L$ with $u=\sigma$ is
$$\tfrac12 LX=|\mathrm{Hess}\sigma|^2+\langle\nabla\sigma,\nabla(L\sigma)\rangle+(\mathrm{Ric}_B-\mathrm{Hess}\sigma)(\nabla\sigma,\nabla\sigma).$$
Two points worth recording. First, the correct tensor here is the $\infty$-tensor $\mathrm{Ric}_B-\mathrm{Hess}\sigma$, **not** the $N=4$ tensor of the top box; the note uses it correctly because it keeps $|\mathrm{Hess}\sigma|^2$ explicit. Second, (9.2) rests on the §2 reduction identity
$$\mathrm{Ric}_B-\mathrm{Hess}\sigma=-3\gamma_B+\tfrac12 d\sigma^2+\tfrac12U^\ast h_{\mathbb H^2}+E_B,$$
which is equivalent to $\mathrm{Ric}^4_f=-3\gamma_B+\tfrac12U^\ast h+E_B$ (add $\tfrac12 d\sigma^2$, use $\tfrac1{N-n}=\tfrac12$). Contracting on $(\nabla\sigma,\nabla\sigma)$ gives exactly $-3X+\tfrac12X^2+\tfrac12A(\nabla\sigma,\nabla\sigma)+E_B(\nabla\sigma,\nabla\sigma)$, matching (9.2) term by term. With $L\sigma=6-T$, $\langle\nabla\sigma,\nabla(6-T)\rangle=-\langle\nabla\sigma,\nabla T\rangle$. ✓

Rewrite (9.3): $\mathrm{div}_\sigma(T\nabla\sigma)=T\,L\sigma+\langle\nabla T,\nabla\sigma\rangle=T(6-T)+\langle\nabla\sigma,\nabla T\rangle$, so $-\langle\nabla\sigma,\nabla T\rangle=-\mathrm{div}_\sigma(T\nabla\sigma)+T(6-T)$. ✓

I also re-derived the orbit Bochner (3.1) as a cross-check on the $Q(A)$ and $-3e$ structure: the $\infty$-tensor contraction $\mathrm{Ric}^\infty_f:A$ produces $-3e$, $\tfrac12|dU(\nabla\sigma)|^2$, $\tfrac12\mathrm{tr}(A^2)$ and $E_B:A$; the $K=-1$ target term adds $+2\det A$; together $Q(A)=\tfrac12\mathrm{tr}(A^2)+2\det A=\tfrac12e^2+\det A$. All internally consistent, and the identity $\langle dU,DF\rangle=\mathrm{div}_\sigma V-|F|^2$ verifies directly.

### (iii) The combined inequality (9.5), (9.6) — correct, all coefficients tracked

Adding (3.1) $+\,c\times$(9.2) and placing every term:

| term | source | destination |
|---|---|---|
| $\tfrac12e^2$ (from $Q$) $+\ \tfrac c2X^2$ | orbit + scalar | quadratic |
| $\det A,\ |DdU|^2,\ c|\mathrm{Hess}\sigma|^2,\ \tfrac12|dU(\nabla\sigma)|^2,\ \tfrac c2A(\nabla\sigma,\nabla\sigma)$ | both | $\mathcal P\ge0$ |
| $-3e-3cX=-3W$ | both | exact linear |
| $E_B:A\ge-\delta e$ ; $cE_B(\nabla\sigma,\nabla\sigma)\ge-c\delta X$ | both | $-\delta W$ |
| $\mathrm{div}_\sigma V-c\,\mathrm{div}_\sigma(T\nabla\sigma)$ | both | $\mathrm{div}_\sigma J$ |
| $-|F|^2\ge-4\delta^2$ ; $cT(6-T)\ge -c(12\delta+4\delta^2)$ | both | $-D_c$ |

The single most important coefficient check: the two curvature-defect contractions combine as $E_B:A+cE_B(\nabla\sigma,\nabla\sigma)\ge-\delta e-c\delta X=-\delta(e+cX)=-\delta W$. This is why the linear term is $-(3+\delta)W$ and not $-(3+2\delta)W$ — the two $\delta$-sources pack into one $\delta W$ because $e$ and $cX$ are exactly the pieces of $W$. Correct.

The quadratic step (9.7) is a genuine pointwise algebraic inequality, not a constrained minimum: $2(1+c)\big(\tfrac12e^2+\tfrac c2X^2\big)-(e+cX)^2=c(e-X)^2\ge0$ for $c\ge0$. So $\tfrac12e^2+\tfrac c2X^2\ge \tfrac{W^2}{2(1+c)}$ holds everywhere. ✓

The forcing constant: $-|F|^2+cT(6-T)\ge-4\delta^2-c(12\delta+4\delta^2)=-12c\delta-4(c+1)\delta^2$, i.e. $D_c(\delta)=12c\delta+4(c+1)\delta^2$. ✓ (script's $4\delta^2+2c\delta(6+2\delta)$ is the same). $\mathcal P\ge0$ because each listed piece is a square or a Gram-form contraction ($A\succeq0\Rightarrow\det A\ge0,\ A(\nabla\sigma,\nabla\sigma)\ge0$). ✓

### (iv) $|J|\le2(1+\sqrt c)\delta\sqrt W$ — correct

$|V|\le\sqrt e\,|F|\le2\delta\sqrt e\le2\delta\sqrt W$; $|cT\nabla\sigma|\le2c\delta\sqrt X\le2c\delta\sqrt{W/c}=2\sqrt c\,\delta\sqrt W$; triangle sum $2(1+\sqrt c)\delta\sqrt W$. For $c=\tfrac12$ this is $(2+\sqrt2)\delta\sqrt W$, matching the JSON. ✓

### (v) $c=\tfrac12$ reaction root — correct

Positive root of $\tfrac{W^2}{2(1+c)}-(3+\delta)W-D_c=0$ is $W=(1+c)\big[(3+\delta)+\sqrt{(3+\delta)^2+\tfrac{2D_c}{1+c}}\big]$. At $c=\tfrac12$, $D_{1/2}=6\delta+6\delta^2$, and this equals $\tfrac{9+3\delta}2+\tfrac32\sqrt{9+14\delta+9\delta^2}$, with series $9+5\delta+\tfrac89\delta^2+O(\delta^3)$. ✓ At $\delta=0$ the threshold is $9$, so with the reflected-center mean floor $\langle W\rangle\ge\langle e\rangle\ge12$ the mean sits an order-three amount above the pointwise zero-defect root.

Interpretation to keep in view: adding $X$ **raises** the root from $6$ (the $c=0$ orbit ceiling) to $6(1+c)=9$, while the $W$-mean floor stays $\ge12$; hence the floor-minus-root margin **shrinks** from $6$ (pure $e$) to $3$. The reason to accept the smaller margin is not the margin size but that $c>0$ is exactly what converts a bound on $W$ into a bound on $|\nabla\sigma|=\sqrt{X}$, which is the only route to the spectral estimate in (vi). With $c=0$ there is no control on $X$ and no Cheeger step. This trade-off is sound and correctly motivated.

### (vi) Conditional Cheeger (9.10)–(9.11) — correct, with one structural fact to state explicitly

Given $W\le B$: $cX\le B\Rightarrow|\nabla\sigma|\le\sqrt{B/c}$, and $L\sigma=6-T\ge6-2\delta$. Weighted divergence over relatively compact $\Omega$ gives
$$(6-2\delta)\mu(\Omega)\le\int_\Omega L\sigma\,d\mu=\int_{\partial\Omega}\langle\nabla\sigma,\nu\rangle\,d\mu_\partial\le\sqrt{B/c}\,\mu_\partial(\partial\Omega),$$
hence $h_\mu\ge(6-2\delta)\sqrt{c/B}$ and $\lambda_1(-L)\ge h_\mu^2/4=\tfrac{c(6-2\delta)^2}{4B}$. The orientation issue is harmless: the left side is positive, and the step $\langle\nabla\sigma,\nu\rangle\le|\nabla\sigma|$ is orientation-free, so no absolute-value error enters.

Two facts the memo should carry:

1. **This cannot hold on a closed manifold, and that is not an error — it identifies the required geometry.** On a closed base $\int_M L\sigma\,d\mu=0$, so $L\sigma\ge6-2\delta>0$ everywhere is impossible ($\int T\,d\mu=6\mu(M)$ contradicts $|T|\le2\delta$). The inequality is therefore intrinsically a statement on a domain whose frontier $\partial\Omega$ carries nonzero $\sigma$-flux — an expanding cusp/connector end where $\sigma$ increases outward. The estimate is valid there provided $\partial\Omega$ (including the exit end) is included in $\mu_\partial$. This matches the §8 setup and the physical connector geometry, so it is consistent, but the conditional statement is about the connector, not about a compact reflected core in isolation.

2. **Strong positive consistency: (9.11) reproduces the exact cusp gap.** On the round cusp $e=0$, $X=4$, so $W=4c$; taking $B=W=4c$, $\delta=0$ gives $\lambda_1\ge\tfrac{c\cdot36}{16c}=\tfrac{9}{4}$, exactly the §8 benchmark $\lambda_1\to9/4$. This is independent evidence that the normalization of the drift Laplacian, the $6-T$ trace, and the Cheeger constant are all self-consistent.

---

### Assessment of the bootstrap and whether a coupled model can defeat it

**As presently written the loop is circular, and the note says so.** (9.11) produces the length-independent gap $\lambda_1\ge\tfrac{c(6-2\delta)^2}{4B}$ **only under the hypothesis $W\le B$**, which is the very conclusion one wants. To be noncircular the bound $W\le B$ must come from an independent input. The candidate local regularity (6.1), $\sup_{B_r}e\le C(1+\delta+r^{-2})$, does not supply it: it carries the $r^{-2}$ scale and the scalar weak-model (6.3) shows arbitrarily high constant energy is admissible on a ball of radius $\sim H^{-1/2}$, so no location-independent $B$ follows on a long connector.

**What is genuinely new here** is the mechanism direction: a global $W\le B$ would give a spectral gap that does **not** decay with connector length, unlike the §8 gap which relied on the exact exponential area growth. If one could produce even a weak a priori $B$ from the coupled equations, (9.11) would upgrade it to a gap, and the gap could then be tested against the divergence forcing $\mathrm{div}_\sigma J$ with $|J|\le2(1+\sqrt c)\delta\sqrt W$ in (9.5). That is a coherent target.

**Whether a coupled scalar model still defeats it.** The pure-$e$ countermodel (6.3) treats $\sigma$ as an arbitrary background and $V$ as free; §9's value is that $J$ and the background are now tied to the same $\sigma$ through $L\sigma=6-T$. However, this added relation constrains only the trace/$\sigma$ sector. The orbit energy $e$ can still concentrate on a thin layer in a region where $\sigma$ is nearly $L$-harmonic ($T\approx0$, $L\sigma\approx6$ satisfied by e.g. $\sigma\approx2r$), while the §7 jet ($e=A^2$, $\nabla e=0$, $F=0$, $\langle dU,DF\rangle=-\tfrac12e^2$) shows the quartic reaction can be cancelled by a $C^1$-large, $C^0$-small tension derivative in a layer of thickness $\sim\delta A^{-3}$. Nothing in §9 forbids such a layer from carrying a $W$-spike (with $X$ moderate and $e$ spiking), because the area equation does not control $e$. So a coupled thin-layer countermodel is **not excluded** by §9 alone, though none has been constructed. The decisive missing input is exactly the one the note isolates: a length-independent Green/resolvent or Cheeger estimate that does not presuppose $W\le B$, or a weighted-inradius/volume-density lower bound on the components of $\{W>k\}$ that rules out thin layers, or additional regularity for $F=-2\widehat E_0$ from the full coupled OT system beyond Bianchi.

**Net:** §9 is a correct and structurally elegant coupling — it folds the area equation into a single nonlinear differential inequality for $W$, keeps the forcing in divergence form, and its conditional gap matches the exact cusp. It is not yet a proof of a length-independent pointwise ceiling, and the thin-layer freedom in the $e$-sector means a coupled countermodel remains a live possibility until one of the four localization inputs is supplied.

**Setting reminder.** Everything above is confined to free, orthogonally transitive $T^2$-regions with the reflection twist-vanishing of §2. Approximate twist, general graph-manifold pieces without OT symmetry, the positive branch, and higher dimensions are outside what §9 addresses; even a full small-defect exclusion in this class would not by itself resolve Yau 26.