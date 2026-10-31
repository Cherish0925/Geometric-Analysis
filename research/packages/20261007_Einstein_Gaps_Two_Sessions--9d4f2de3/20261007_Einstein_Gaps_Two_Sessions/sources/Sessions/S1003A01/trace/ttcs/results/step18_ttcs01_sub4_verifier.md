# TTCS Independent Branch Record

```json
{
  "step_id": 18,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step18_corrected_riccati_and_H4_comparison.md",
    "Sessions/S1003A01/workspace/scripts/h4_perp_cell.py",
    "Sessions/S1003A01/workspace/scripts/u2_general_cell.py",
    "Sessions/S1003A01/workspace/data/h4_cells/corrected_perp_x0.003_X64_P_d16.json",
    "Sessions/S1003A01/workspace/data/h4_cells/corrected_perp_x0.01_X64_P_d16.json",
    "Sessions/S1003A01/workspace/data/h4_cells/corrected_perp_x0.03_X64_P_d16.json",
    "Sessions/S1003A01/workspace/data/h4_cells/corrected_perp_x0.01_X8_P_d12.json"
  ]
}
```

## Task

Independently read and check the real-hyperbolic cell comparison. Verify the normalization Ric=-6, the coordinate collar F=x, G=x+2x^2, w=0, bolt smoothness conditions and energy normalizations in h4_perp_cell.py, and assess what the floating results at X up to 64 establish scientifically about the absence or presence of a finite-scale subthreshold mechanism compared with complex hyperbolic cells. Look for implementation inconsistencies, especially the repaired G base, exact-collar contact, and whether the small anisotropy is meaningful. Do not turn numerical evidence into a theorem.

## Output

# Verification memo: real-hyperbolic $O(-1)$ cell comparison (`h4_perp_cell.py`, Step 18 §3)

**Summary.** The geometry, normalizations and bolt/collar matching in `h4_perp_cell.py` are correct. The floating results show that this ansatz yields $P/(8\pi^2)\approx 1+2.0\,x_0$ for $x_0\le 0.03$. They are upper bounds on the class infimum and say nothing about $P\ge 1$ in general. The near-zero anisotropy has a structural explanation: a symmetry fixes the biaxial family. It is not a dynamical contrast with the complex-hyperbolic (CH) cells.

## 1. Normalization and exact collar: correct

- **Line element.** With $dt=dx/(2\sqrt G)$ and $a=\sqrt x$, one has $a'=\sqrt{G/x}$.
- **Round profile.** For $a=\sinh(\sqrt2t)/\sqrt2$ we get $a'^2=\cosh^2=1+2a^2$, so $G=x+2x^2$, $F=x$, $w=0$.
- **Ricci tensor.** The Ricci formula in `symbolic()` is the standard diagonal Bianchi IX one, rescaled for $d\sigma_i=2\sigma_j\wedge\sigma_k$. Its curvature term $2(a_i^4-(a_j^2-a_k^2)^2)/(a_i^2a_j^2a_k^2)$ gives $2/a^2$ on round orbits, consistent with unit $S^3=\sum\sigma_i^2$ and $\int\sigma_{123}=2\pi^2$.
- **Direct check on the profile.** $a''/a=2$ and $(a'/a)^2=(1+2a^2)/a^2$. Hence $\mathrm{Ric}_{00}=-6$ and $\mathrm{Ric}_{ii}=-2-2(1+2a^2)/a^2+2/a^2=-6$.
- So $\mathrm{Ric}=-6g$, $s=-24$ and $\mathrm{Ric}_0=0$, matching the CH normalization $a_2^2=x(1+x)$.

## 2. Bolt regularity: all required conditions are met

**Slope condition.**
- Near $x_0$, $a_1'\to F'(x_0)\sqrt{G'(x_0)/F'(x_0)}=\sqrt{F'G'}$.
- Unit-speed Hopf fibres have period $2\pi$ on unit $S^3$, so an $O(-1)$ bolt needs $a_1'=1$, i.e. $F'G'=1$.
- **Code check:** $T_0=\mathrm{cheb}(d,-1)$ and $T_0[0]=1$. The shift therefore makes $\sum c_G T_0=-\sum c_F T_0$, i.e. $q_F(0)+q_G(0)=0$.
- The bases $(x-x_0)+x_0S$ and $(x-x_0)+(2x^2+x_0)S$ both have derivative exactly 1 at $x_0$, because $S'(0)=0$. So $F'(x_0)G'(x_0)=1$ holds exactly.
- The repaired $G$ base is correct. The stored $z[d]=0$ in every file is expected: that coefficient is overwritten by the shift and has zero gradient.

**Anisotropy order.**
- The isotropy circle acts with weight 1 on the normal plane and weight 2 on $\mathrm{span}(e_2,e_3)$. Trace-free symmetric tensors there therefore carry weight 4.
- Smoothness then requires $a_2^2-a_3^2=s^4\phi(s^2)$, i.e. $O((x-x_0)^2)$.
- The factor $u^2$ in $w=u^2(1-u)^3\sum c_W T$ supplies exactly this, with $u\sim(x-x_0)/(x_0\ell)$. A factor $u^1$ would have produced a conical defect on the bolt.
- $w(x_0)=0$ gives a round bolt. $F$ and $G$ are smooth with simple zeros, so $x$ is smooth in $s^2$ and $a_1$ is odd with $a_1'(0)=1$.

**Collar contact at $x=X$.**
- $q_F,q_G,w$ vanish to second order because of the $(1-u)^3$ factors, and $S(1)=1$, $S'(1)=S''(1)=0$.
- This gives $F=X$, $F'=1$, $F''=0$; $G=X+2X^2$, $G'=1+4X$, $G''=4$; and $w=w'=w''=0$.
- The glued metric is $C^2$ and the energy densities are continuous: there is no junction contribution, and mollification converges in $C^2$.
- The older `u2_general_cell.py` is only $C^1$ in $F$ at $X$. That is still adequate, since $F''$ only jumps and produces no delta term.

## 3. Energy normalization: correct, and the threshold is the Burns energy

- With $dV=abc\,dt\wedge\sigma_{123}$, the code's normalization is $P/(8\pi^2)=\frac14\int abc\,|\mathrm{Ric}_0|^2dt$, so `PD=vol*ric0/4` is right.
- The scalar part $\frac1{16}\int abc(s+24)^2dt$ matches `SD`.
- $|\mathrm{Ric}_0|^2=\sum(\mathrm{Ric}_{ii}-s/4)^2$ is the full tensor norm.
- **Independent check of the threshold value 1.** For Burns on $O(-1)$, which is ALE with trivial group, $\chi=2$ and $\tau=-1$. Scalar-flat Kähler implies $W^+=0$, and the signature formula then gives $\int|W^-|^2=12\pi^2$.
- Gauss–Bonnet then reads $2=(12\pi^2-\frac12\int|\mathrm{Ric}_0|^2)/8\pi^2+1$, so $\int|\mathrm{Ric}_0|^2=8\pi^2$.
- The threshold 1 is therefore exactly the Burns energy, consistent with $P\to1$ as $x_0\to0$.

## 4. Implementation observations

**`minF` / `minG` carry no information.** $F,G>0$ by construction. The recorded minima are just $F'(x_0)$ times $(x-x_0)$ at the first Gauss node. For $x_0=0.003$: $u_1\approx1.4\times10^{-6}$, so $x_0\ell u_1\approx4\times10^{-8}$, which matches.

**"Continuation from X=8 to X=64" is not supported by the stored data.**
- The output dict does not record `--seed`.
- The $X=64$ file has $P_0=1.1429$, far above the $X=8$ optimum $1.0206$.
- Coefficients in $u=\log(x/x_0)/\ell$ also change meaning when $\ell$ changes. A seed is therefore a warm start, not a homotopy.
- The two runs also differ in degree (12 vs 16) and quadrature nodes (800 vs 1000). The $9\times10^{-5}$ change cannot be attributed to $X$.

**Optimizer convergence.**
- Termination came from `ftol`, with $\|\nabla\|_\infty\approx5\times10^{-5}$ against `gtol=1e-12`.
- There is no degree or `nq` refinement table.
- Near the bolt, $F\sim10^{-8}$ in the simplified densities implies large cancellations. A same-parameter `nq` doubling would bound this.

**The two codes parametrize the same class.** At $w=0$, `h4_perp_cell` is the same biaxial $O(-1)$ class as `u2_general_cell RSF` (slot 3 there, slot 1 here). Their values, $1.06479$ at $(.03, X{=}4)$ and $1.06307$ at $(.03, X{=}64)$, differ by about 3% of $P-1$. This measures ansatz dependence of the slope ($2.16$ vs $2.10$); it is not an independent confirmation.

`SC` is computed but unused.

## 5. The small anisotropy is structurally expected

**Symmetry argument.**
- The swap $(\sigma_1,\sigma_2,\sigma_3)\mapsto(-\sigma_1,\sigma_3,\sigma_2)$ preserves $d\sigma_i=2\sigma_j\wedge\sigma_k$ and is induced by an $SO(3)$ rotation.
- It maps $(a_1,a_2,a_3)\mapsto(a_1,a_3,a_2)$. For H$^4$ it also preserves the collar and the bolt data, so the biaxial metrics are its fixed set.
- By symmetric criticality, a biaxial critical point is critical in all anisotropic directions.

**Gauge effect of $w$.**
- In the gauge $a_2^2=x$, a pure $\delta w$ is not purely odd. It equals an odd part plus a biaxial reparametrization $(\delta F,\delta G)=-\tfrac12(xF_x,xG_x)\delta w$.
- A nonzero optimized $w$ can therefore simply enlarge the truncated biaxial basis.
- $\max|w|\sim4$–$7\times10^{-5}$ is consistent with this. It sits at the gradient level and varies irregularly with $x_0$.

**What the runs do not test.** All runs start from $c_W=0$. A small symmetry-breaking odd mode would not be probed. A test would need odd-direction second variation at the biaxial optimum, or random-$w$ starts.

**Why the contrast with CH is structural.** In the CH perpendicular cell, the collar has $a_2^2=x(1+x)\ne a_3^2=x$ while the bolt needs $a_2=a_3$. Anisotropy is therefore forced. "Essentially biaxial for H$^4$, anisotropic for CH" follows from the backgrounds and is not an optimization finding.

## 6. Quantitative content and a testable link to $R^+$

| $x_0$ | $(P-1)/x_0$ |
|---|---|
| 0.003 | 2.0188 |
| 0.01 | 2.0467 |
| 0.03 | 2.1023 |

- The fit $(P-1)/x_0\approx2.002-0.975\,x_0\log x_0$, determined by the first two points, predicts $2.104$ at $x_0=.03$ against the observed $2.102$.
- Truncation of about $10^{-4}$ in $P$ allows roughly $\pm0.03$ in the leading coefficient at $x_0=.003$. The leading slope is about $2.0$, as an ansatz upper value.
- Interpretation: H$^4$ has $R^+=(s/12)I=-2I$, so every unit self-dual gluing direction $J$ has $\langle R^+J,J\rangle=-2$. CH with $\mathrm{Ric}=-6$ has $R^+=\mathrm{diag}(-6,0,0)$; the trace $-6$ is the same, but the direction structure differs.
- **Testable consequence.** If the first-order cell energy is $1+\kappa\,(-\langle R^+J,J\rangle)\,x_0$ with $\kappa\approx1$ in this $x_0$ normalization, then:
  - the CH perpendicular slope should be about 0;
  - the CH Kähler-aligned slope should be about 6, provided the bolt-area normalizations $\pi x_0$ agree.
- Existing `CSF` `P_slope` and perpendicular-cell data can confirm or refute this directly. That would turn the Step 18 picture into a measured first-order law. The formula itself is heuristic; I have not derived it.

## 7. What the runs establish

**Established.** Within one diagonal Bianchi IX family, at $x_0\le0.03$ and $X\le64$, the best cells found have $P/(8\pi^2)\approx1+2x_0$. These are upper bounds on the class infimum.

**Not established.**
- **No lower bound.** "No subthreshold H$^4$ cell" would need a lower bound; optimizer output cannot supply one. By contrast, a CH value below 1 is a construction, certifiable by interval arithmetic. The two sides have different evidential status.
- **No finite-scale data.** Nothing is learned about $x_0\gtrsim0.1$, the regime of the CH finite-scale effects in Step 18. $X$ already reaches curvature scale, but $x_0$ does not.
- **No matched comparison.** No run compares CH-perpendicular and H$^4$ cells at equal $(x_0,X,\deg)$ with a common base family. Differing base positivity factors make the ansatz expressivity unequal.

**What would turn the H$^4$ branch into mathematics.**
- An analytic first-order expansion around Burns giving coefficient $2$ for H$^4$ and $0$ for the CH kernel directions.
- A same-code H$^4$/CH table at matched parameters with degree and `nq` convergence.
- An odd-mode Hessian check at the biaxial optimum.