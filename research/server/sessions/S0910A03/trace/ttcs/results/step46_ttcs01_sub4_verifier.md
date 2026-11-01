# TTCS Independent Branch Record

```json
{
  "step_id": 46,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step42_uniform_gap_weight_terminal_repairs.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md",
    "Sessions/S0910A01/workspace/notes/step16_exponential_pullback_averaging_review.md",
    "Sessions/S0910A03/workspace/notes/step43_terminal_density_G_lemma.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step45_preceptor_verdict_and_next_interface.md"
  ]
}
```

## Task

Independently verify the theorem statement, topological normalization, and terminal geometric passage in the assembled restricted Ishida–LeBrun negative-gap argument. Check the family-uniform contradiction split for bounded/unbounded A and q>=0; the O(A) curvature/volume input needed for support selection; terminal density constants and use of monopole classes at the flowed metric; retention of A-proportional inner-center volume; conversion of the normalized plateau flow to ordinary Ricci flow; local Shi estimates with a real spacetime buffer; exponential-pullback Liouville–Rauch averaging without base injectivity; strong convergence sufficient to pass G and Weyl eigenvalues; and the Derdzinski/projector contradiction. Attack any hidden assumption such as base noncollapse, unsupported smooth cutoffs, weak-to-strong curvature passage, or a mismatch between the density average and the pulled-back chart. Give exact repairs and state the strongest theorem actually supported, without treating it as a solution of full Yau Problem 26.

## Output

# Verification Memo: Restricted Ishida–LeBrun Negative-Gap Argument

## Summary judgment

The argument separates cleanly into a **topological/algebraic core** (deficit accounting, calibration, terminal density constants, exponential-pullback averaging, Derdziński germ) that I find correct and independently reproducible, and an **analytic flow package** (weighted degenerate cutoff flow producing the terminal metric) that is explicitly incomplete. The downstream geometry is a genuine conditional module: *given* a terminal metric on the same smooth manifold with two quantitative outputs, the contradiction runs. The flow that must supply those outputs under collapse is not established. What is unconditionally supported is a reduction theorem, not the restricted gap itself, and in no reading a resolution of Yau 26.

I checked the requested items in order.

---

## 1. Topological normalization and deficit algebra — correct

For a minimal surface of general type, $(2\chi+3\tau)(X_j)=c_1^2(X_j)$ (Hirzebruch). With $\chi$ additive minus $2$ per connected-sum neck ($\chi(S^4)=2$) and $\tau$ additive,
$$(2\chi+3\tau)(M)=\sum_j c_1^2(X_j)+(2\chi+3\tau)(N)-4m=A-D=\tfrac{2A}{3}-q.$$
This reproduces Step 42 (2.1), $I-J=\tfrac{2A}{3}-q$, and confirms that the Step 41 line "$I-J=A-k=-q$" was wrong (it would need $A-k=A/3-k$). The repaired averaged deficit
$$D_{\mathrm{av}}=J-q-\tfrac23\sum(E_\ell^+)^2\ge0,\qquad q+\tfrac23\sum(E_\ell^+)^2\le J,$$
is algebraically forced by sign-averaging the mixed inequality $I\ge\tfrac23(\kappa_\varepsilon^+)^2$: the cross terms average to zero, $(\sum c_1)^{+2}\ge(\sum c_1)^2=A$ because $(\alpha^+)^2=\alpha^2+|\alpha^-|^2$, and the summands are mutually orthogonal. Since $J\le Q/8\pi^2$ and (below) $\mathrm{Vol}/A\to 32\pi^2/9$, one gets $q/A\to0$, $\sum(E_\ell^+)^2/A\to0$, $D_{\mathrm{av}}/A\to0$. All consistent.

The calibration identity
$$27\big(\tfrac{s^2}{24}+2|W^+|^2\big)-(s-\sqrt6|W^+|)^2=\tfrac18(s+8\sqrt6|W^+|)^2$$
I verified directly (both sides $=\tfrac{s^2}{8}+2\sqrt6\,su+48u^2$). It gives $K=E/72\pi^2\le\tfrac32 I$ and hence $I\ge\tfrac23(a^+)^2$, consistent with the SW inputs. The calibrated volume follows: mean $s^2/24\to2/3$, $2|W^+|^2\to1/12$, integrand mean $\to3/4$, $I\to2A/3$ gives $\mathrm{Vol}/A\to32\pi^2/9$.

---

## 2. Family-uniform split (bounded/unbounded $A$, $q\ge0$) — logically coherent, reducing both branches to the same flow

The pointwise scalar estimate forcing $q_i/A_i\to0$ rests on operator-norm pinching giving $|s+4|\le4\delta$ pointwise together with $\int s^2\ge32\pi^2(a^+)^2\ge32\pi^2A$; this is reasonable but is the one place the exact inequality $\delta/(1-\delta)\ge\sqrt{q/(2A)}$ should be reconstructed from the session's own derivation, since it is quoted rather than reproved here.

The bounded-$A$ branch is sound: $q_i\in\tfrac13\mathbb Z$, $q_i\ge0$, $q_i/A_0\to0$ forces $q_i=0$ eventually. **But note both branches then depend on the *same* analytic flow package**: the bounded-$A$ case is not closed by the fixed-$A$ Cheeger–Naber reduction (S0910A03 Step 6), which only yields everywhere unit-scale collapse and $\mathrm{diam}\to\infty$, not a contradiction. So the split does not create an independently-closed branch; it is a clean case division feeding one common downstream module.

---

## 3. $O(A)$ curvature/volume input for support selection — correct

$\int|\mathrm{Rm}|^2=O(A)$ holds: $\int|W^+|^2\sim4\pi^2A/27$ from calibration, $\int|W^-|^2$ controlled by $\int|W^+|^2$ and $\tau(M)=O(A)$, $\int|\mathrm{Ric}^\circ|^2\le Q=o(A)$, $\int s^2\sim16\,\mathrm{Vol}=O(A)$. The Chern–Weil bound $\int|\mathrm{Rm}|^2\le C_0A$ is legitimate.

The maximal-function selection is valid: under $\mathrm{Ric}\ge-2g$ the doubling/weak-type $(1,1)$ inequality holds, giving bad-set volume $\le C r^4A/\gamma_0^2$, hence good-set volume $\ge\alpha_0A$. The conversion of the *averaged* threshold $r^4\fint|\mathrm{Rm}|^2\le\gamma_0^2$ to the *unnormalized* $\int_{B_{7r}}|\mathrm{Rm}|^2\lesssim\gamma_0^2$ via the Bishop–Gromov upper volume $V_{-2}(7r)\sim(7r)^4\omega_4$ is correct, and collapse only shrinks $\mathrm{Vol}\,B_{7r}$, which helps. This piece survives collapse as claimed.

---

## 4. Terminal density constant chain — arithmetic correct; one imported inequality is the true dependency; one internal definition clash

The constant chain reproduces exactly:
- $\int|E|^2=Q$ (coeff 1);
- $(s+4)^2=(\mathrm{tr}_gE)^2\le4|E|^2$ in dimension 4 (coeff 4);
- $\int(s+8\sqrt6|W^+|)^2=864\pi^2I-8E\le864\pi^2(R-q_{\rm top})\le108Q+864\pi^2(-q_{\rm top})_+$ (coeff 108, 864), where $R=(1/8\pi^2)\int|E^\circ|^2\le Q/8\pi^2$ using $\mathrm{Ric}^\circ=E^\circ$;
- $\int G\le6Q+48\pi^2(-q_{\rm top})_+$ (coeff 6, 48).

Total $119=1+4+108+6$, $912=864+48$. Under $q\ge0$ this is $\int\mathfrak D\le119Q$, and $\mathfrak D/A\to0$ follows from $Q(T)/A\to0$, independent of the exact constant. The monopole classes and SW invariants are topological, so they apply at the flowed metric $g_i(T)$; this use is correct.

**The load-bearing external input is Step 43 Step C**, i.e. the claim
$$\int(b_-)^2\ge32\pi^2(a^+)^2,\qquad b=\tfrac23 s+2w,$$
equivalently the nonnegativity of $D_{\rm Yam}$ and $D_{\rm mono}$ in the generalized-Yamabe decomposition $(4/9)\Delta_a=D_{\rm spec}+D_{\rm Yam}+D_{\rm mono}$. This is invoked as "LeBrun Theorem 2.3 + generalized-Yamabe extension" but is not reproduced; the note itself gives only the decomposition schematically from "Codex eq. 24." **Exact repair:** extract from the two cited LeBrun papers the precise statement, its hypotheses (whether the lowest-eigenvalue quantity $\tfrac23 s+2w$ and the conformal minimization apply to an *arbitrary* smooth metric, not only Yamabe minimizers), and confirm the two deficit terms are genuinely nonnegative pointwise/after minimization. Until this is pinned to the source, the terminal $\int G$ constant rests on an imported inequality, and everything else in the density chain is elementary.

**Internal clash to fix:** Step 41 (7.4) defines $\mathfrak D=\tfrac1{4\pi^2}\big[(s+4)^2+\tfrac1{16}(s+8\sqrt6|W^+|)^2+G\big]$, which is *not* the density $\mathfrak D=|E|^2+(s+4)^2+(s+8\sqrt6|W^+|)^2+G$ used in Step 28/Step 43 to derive $119$. The two normalizations are inconsistent (extra $1/4\pi^2$, $1/16$, and no $|E|^2$ term). Adopt the Step 43 definition uniformly; the conclusion is unaffected because only $\int\mathfrak D/A\to0$ is used, but the discrepancy will trip any reader reconstructing the constant.

**Notation collision to fix:** Step 43 §1 uses $q=\sqrt6|W^+|-s$ (pointwise) while $q_{\rm top}=D-A/3$. Both usages are internally consistent as I checked, but the same symbol for a pointwise scalar and a topological integer invites a hidden sign error. Rename one.

---

## 5. Retention of $A$-proportional inner-center volume — correct

Coloring into $N_0\le C(n,r)$ classes gives one disjoint $B_{7r}$ class of volume $\ge\alpha_0A/N_0$; Bishop–Gromov $\mathrm{Vol}\,B_r\ge\frac{V_{-2}(r)}{V_{-2}(5r)}\mathrm{Vol}\,B_{5r}$ (fixed ratio, $r$ fixed) gives inner-center volume $\ge c\alpha_0A$. The terminal $C^0$-comparison $\|g_i(T)-g_i(0)\|_{C^0}\le2\int_0^T\|aE\|_\infty\,dt\le C\delta\theta^{2/3}r^2\to0$ (from the drift endpoint (5.7)) keeps the terminal inner volume $\ge c'\alpha_0A$. Bilipschitz-to-$1$ is genuine, **conditional on the Moser endpoint (5.7) holding**.

---

## 6. Normalized plateau flow $\to$ ordinary Ricci flow, and local Shi with a real spacetime buffer — correct, and this is a solid point

The decisive structural fact is that $\chi_\alpha$ (hence $a=\sum\chi_\alpha^2$) is **time-independent** (§4.3: the gradient of a scalar does not involve $\Gamma$, so $C_1$ and the plateau set are frozen). Therefore $\{a=1\}=\bigcup B_{5r}^{g(0)}(x_\alpha)$ is a *fixed* open set, and on $\{a=1\}\times[0,T]$ the flow is exactly $\partial_tg=-2(\mathrm{Ric}+g)$ — normalized Ricci flow, which differs from unnormalized by a time reparametrization/rescaling that leaves the derivative structure untouched. This gives a genuine spacetime parabolic plateau, so interior Shi estimates on $B_r\times[\tau,T]$ apply once $|\mathrm{Rm}|\le K$ is known there. The curvature bound comes from the Moser endpoint $\|aF\|_\infty\le C\gamma/t$ (with $a=1$ on plateau), so $|\mathrm{Rm}|\le C\gamma/t+C\le K$ for $t\ge\tau$. This module is correct and the spacetime buffer is real, **conditional on the Moser plateau curvature bound**.

---

## 7. Exponential-pullback Liouville–Rauch averaging — fully rigorous, no base injectivity

Step 16's lemma is correct and I reproduce its two inputs: under $\sec\le K$, $J_p\ge s_K^{n-1}>0$ for $t<\pi/\sqrt K$ (no conjugate points below first, and $r<\pi/(2\sqrt K)$ keeps $\exp_p$ an immersion), and $\sec\ge-K$ gives $J_p\le s_{-K}^{n-1}$. The Fubini step uses Liouville invariance of the geodesic flow on $SM$ (natural measure $d\mu(p)\,d\xi$), giving $\int_M\!\int_{S_pM}F(\exp_p(t\xi))\,d\xi\,d\mu=|S^{n-1}|\int_MF\,d\mu$ for each fixed $t$; multiplying by $s_{-K}^{n-1}(t)\,dt$ yields the estimate. $F\ge0$ makes multiplicity harmless. No cut locus, no injectivity radius, no deck group. This is the strongest, cleanest piece of the whole assembly.

The buffer hypothesis is met: a radial geodesic of length $\rho\le r$ from an inner center $x_\alpha\in B_r$ reaches distance $\le2r$, staying in $B_{2r}\subset B_{5r}$ where $a=1$ and $|\sec|\le K$ (Moser). Choose $\rho\le\min(r,\pi/(2\sqrt K))$. The constant $C(n,K,\rho)$ is $i$-independent **iff $K$ is sequence-uniform**, which again returns to the Moser output.

---

## 8. Density-average $\to$ pulled-back chart, strong convergence, passing $G$ and Weyl eigenvalues — coherent, no hidden mismatch

I checked the potential mismatch and it is clean. $\mathfrak D$ is a pointwise Riemannian invariant, so $\mathfrak D_{\hat g_i}(x)=\mathfrak D_{g_i(T)}(\exp_{p_i}x)$ ($\hat g_i=\exp^*g_i(T)$ is an isometric immersion). In polar coordinates the $\hat g_i$-volume form is $J_p\,dt\,d\xi$, so $A_\rho\mathfrak D(p_i)=\frac1{\mathrm{Vol}_{\hat g_i}(B_\rho)}\int_{B_\rho(0)}\mathfrak D_{\hat g_i}\,d\mu_{\hat g_i}$. Thus selection $A_\rho\mathfrak D(p_i)\to0$ is exactly vanishing mean of the *chart* density over the metric ball, with $\mathrm{Vol}_{\hat g_i}(B_\rho)$ bounded above/below by Rauch. No mismatch between the averaged quantity and the compactness object.

The weak-to-strong passage is repaired correctly in Step 42 §5: uniform $|\sec|\le K$ + Rauch lower volume $\Rightarrow$ harmonic radius $\Rightarrow$ $C^{1,\alpha}\cap W^{2,p}$ bounds; $|E|\le|\mathrm{Rm}|+C\le K$ on the plateau with $\int|E|^2\to0$ upgrades to $\int|E|^p\le K^{p-2}\int|E|^2\to0$ by interpolation; elliptic stability of $g^{ab}\partial_a\partial_b g_{jk}=-2\mathrm{Ric}+Q(\partial g)$ gives $\hat g_i\to g_\infty$ in $W^{2,p}_{\rm loc}$, hence $\mathrm{Rm}(\hat g_i)\to\mathrm{Rm}(g_\infty)$ in $L^p_{\rm loc}$. This kills the earlier unsupported $W^{4,p}$ inference. Since the densities are continuous functions of $\mathrm{Rm}$ (and $w$ is Lipschitz in $W^+$), $\int_{B_\rho}\mathfrak D_{g_\infty}=\lim\int\mathfrak D_{\hat g_i}=0$, so $\mathfrak D_{g_\infty}=0$ a.e.: $s_\infty=-4$, $|W^+_\infty|^2=1/24$, $G_\infty=0$, $\mathrm{Ric}_{g_\infty}=-g_\infty$ a.e.; elliptic bootstrap makes $g_\infty$ smooth and the equalities hold everywhere. A local (multiply-covered) Einstein germ is all Derdziński needs.

---

## 9. Derdziński/projector germ contradiction — fully correct, doubly confirmed

I verified the arithmetic. $G_\infty=0$ with $s_\infty=-4$, $|W^+_\infty|^2=1/24$: $f=-3$, $G=4\xi(3-\xi)$, so $\xi=0$, $w=-1/6$, then $\lambda_1+\lambda_2=1/6$, $\lambda_1^2+\lambda_2^2=1/24-1/36=1/72$, $(\lambda_1-\lambda_2)^2=0$, giving $\mathrm{Spec}(W^+_\infty)=(-\tfrac16,\tfrac1{12},\tfrac1{12})$. Einstein $\Rightarrow\delta W^+=0$; two distinct constant eigenvalues $\Rightarrow(24|W^+|^2)^{1/3}g$ locally Kähler (Derdziński Prop 5), and $24|W^+|^2=1$ makes $g_\infty$ itself locally Kähler. A Kähler surface has $|W^+|^2=s^2/24=2/3\ne1/24$. Contradiction.

The independent Step 6 route also checks: $\det W^+=-1/864$, and the scalar Weitzenböck $\Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+$ forces $|\nabla W^+|^2=1/16$ (since $2|\nabla W^+|^2=1/6-1/24=1/8$), while the projector lemma from $\delta W^+=0$ + two constant eigenvalues gives $\nabla W^+=0$. Two eigenforms, one contradiction. Both correct.

---

## 10. The genuinely unresolved inputs (the argument is conditional here)

Three items are not established, and the assembly correctly records the first two:

**(i) Collapse-robust weighted Moser/first-exit package.** The endpoints (5.6)–(5.7), the $K_2/J_6/Q$ propagation, and the plateau curvature bound are the sole source of every "conditional on Moser" caveat above. The $L^2\to L^\infty$ Moser iteration needs a moving Sobolev/entropy control. Step 6 shows a fixed-critical sequence must collapse at unit scale everywhere with $\mathrm{diam}\to\infty$; a diverging diameter degrades the global Sobolev constant (Saloff-Coste), which is exactly the pressure the weighted energies must absorb through the $r^{-2}$ and $\chi$-weight bookkeeping. Step 45 item 1 explicitly names "simultaneous preservation of moving Sobolev constants, support geometry, homogeneous $K_2$, $Y$, $J_6$, the all-$p$ defect ladder, and global $Q$" as the outstanding work. This is not established. **Exact requirement:** a single degenerate-flow first-exit estimate on one regularization-limit flow in which the Sobolev-type inequality used in the Moser recurrence is uniform in $i$ under the forced diameter divergence, with the weight carrying the collapse.

**(ii) H-WU and H-DT.** H-WU (the exact weighted all-order $U_m$ equation whose top cutoff term is $\chi C_{m+2}U_0$, verified so that no commutator, normalization, or $G$-variation term produces a bare $C_{m+2}U_0$) is the mechanism that routes around the *unbounded* higher cutoff jets $\nabla^m\chi_\alpha$ (Lemma 2.1(f) asserts no sequence-uniform bound on $m\ge2$). Step 45's coefficient identity $B_{r+1}*B_{s+1}*T_t$ with $B_1B_1T_m=4(\chi^2/b)C_1C_1(U_m-\sum B_qT_{m-q})$ is a promising re-derivation, and the scalar partition script passes, but the note itself states the tensor provenance and PDE existence are not settled by that script. H-DT (transported-coefficient DeTurck start/restart with tame estimates and uniqueness) remains a separate input read against Yang's compressed statement. Both open.

**(iii) The LeBrun spectral lower bound** (§4 above) — the one imported inequality inside the otherwise-elementary terminal density chain.

---

## Strongest theorem actually supported

Unconditionally, the assembly establishes a **conditional reduction**, and the downstream geometry as a self-contained module:

> *Suppose the degenerate normalized cutoff flow $\partial_tg=-2a(\mathrm{Ric}+g)$ with time-independent weight $a$ exists on $[0,\theta r^2]$ and produces, for the pinched Ishida–LeBrun sequence, a terminal metric $g_i(T)$ on the same smooth manifold with (a) $Q_i(T)/A_i\to0$, and (b) a plateau center set $P_i$ of volume $\ge\alpha A_i$ carrying $|\mathrm{Rm}_{g_i(T)}|\le K$ and a radius-$\rho$ bounded-curvature buffer, uniformly in $i$. Then, using the terminal density constant $\int\mathfrak D\le119Q$ (with the LeBrun spectral lower bound as an external input), the exponential-pullback Liouville–Rauch averaging lemma, strong $W^{2,p}$ chart convergence, and the Derdziński germ, there is $\varepsilon_{\rm IL}>0$ independent of $A,D,q,N$ and of the metric such that no manifold in the $q\ge0$ Ishida–LeBrun geography carries $\|g^{-1}(\mathrm{Ric}_g+g)\|_{\infty,\mathrm{op}}<\varepsilon_{\rm IL}$.*

The two components verified as **unconditionally correct** and reusable are: (1) the exponential-pullback averaging lemma (Step 16), which is a clean, injectivity-radius-free selection principle of independent value; and (2) the terminal recalibration $\to$ pullback $\to$ Derdziński contradiction chain (Step 28 §§1–4, Step 6, Step 8), which is a correct conditional module taking exactly outputs (a),(b) as input.

Even the fully completed restricted result would be a dimension-four, negative-sign, single-geography statement. It does not touch the positive branch, arbitrary four-manifold topology, dimensions $n\ge5$, a dimension-only forcing interval for the full proposition, or the Lean formalization. The full Yau 26 statement requires forcing in some dimension on *both* normalized sign branches (or a dimension-only interval), which this route does not attempt.