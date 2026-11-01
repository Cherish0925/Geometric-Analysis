# TTCS Independent Branch Record

```json
{
  "step_id": 6,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step5_regular_patch_and_derdzinski_boundary.tex",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/trace/ttcs/results/step5_ttcs01_verifier2_integration.md",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md"
  ]
}
```

## Task

Review the regular-patch and spectral-transfer chain needed to exploit any local algebraic contradiction. For a fixed critical Ishida–LeBrun manifold with ||Ric+g||∞→0 and absolute scalar–Weyl/SW deficits O(Aδ²), determine rigorously whether the existence of one unit ball with Vol B1≥v yields a fixed harmonic chart on which a smooth Einstein limit exists and the full spectrum (−1/6,1/12,1/12) holds. Check the use of Cheeger–Naber Theorem 1.13, the definition/propagation of harmonic radius, strong W^{2,p} convergence under only L∞ Ricci defect, and transfer of the selected regularized SW forms/eigenvalue defect. Pay special attention to whether a monopole solution can be chosen coherently across i and regularization, and whether local elliptic estimates give a nonzero limiting eigenform. State the strongest theorem actually justified, and exactly what conclusion about sup_p Vol B1 can follow if the local projector obstruction is valid.

## Output

# Verification memo: the regular-patch and spectral-transfer chain

## Summary of what the material actually establishes

The local chain in `step5_regular_patch_and_derdzinski_boundary.tex`, supported by `quantitative_deficit_analysis.md` and Cheeger–Naber Theorem 1.13, is essentially correct and, with two points that need one more line of estimate each, rigorously produces the following: from a **single** unit ball with $\mathrm{Vol}_{g_i}B_1(p_i)\ge v$ one extracts a positive-measure family of harmonic patches of a fixed scale $\rho(v)$, on which a subsequence converges to a **smooth pointed Einstein germ** $\mathrm{Ric}(g_\infty)=-g_\infty$ carrying the full calibrated data $s_\infty=-4$, $|W^+_\infty|=\tfrac1{2\sqrt6}$, a nonzero saturating self-dual form, and $\operatorname{Spec}(W^+_\infty)=(-\tfrac16,\tfrac1{12},\tfrac1{12})$. This is a genuine local structure theorem.

It does **not** produce any local contradiction, and therefore cannot by itself constrain $\sup_p\mathrm{Vol}\,B_1$. The germ is a (generally incomplete, noncompact) open piece, and the calibrated spectrum is realizable on such a piece. The decisive obstruction is global. Details follow.

## 1. Extraction step (Cheeger–Naber 1.13, harmonic radius, propagation) — correct

For large $i$, $\mathrm{Ric}_{g_i}=-g_i+E_i$ with $|E_i|\le\delta_i$, so the operator norm $|\mathrm{Ric}_{g_i}|\le 1+\delta_i<3=n-1$. Theorem 1.13 applies in its $|\mathrm{Ric}|\le 3$ form and gives the harmonic-radius measure estimate $\mathrm{Vol}(T_r\{r_h\le r\})\le C(v)r^4$ on $B_1(p_i)$. The note correctly uses the **harmonic radius** $r_h$, not the regularity scale $r_x$: the Einstein/$|\nabla\mathrm{Ric}|$ upgrade in Remark 1.11/1.16 is unavailable because only $\|E_i\|_{L^\infty}$ is controlled and $\nabla E_i$ is not.

The tube removal is valid. With $G_i:=B_{1/2}(p_i)\setminus T_{2\rho}\{r_h\le2\rho\}$ and $\rho$ chosen so $C(v)(2\rho)^4<\tfrac12 b(v)$ (Bishop–Gromov lower bound), $\mathrm{Vol}(G_i)\ge\tfrac12 b(v)>0$. Because a full $2\rho$-tube was removed, every $x_i\in G_i$ satisfies $d(x_i,\{r_h\le2\rho\})\ge2\rho$, so $r_h>2\rho$ on all of $B_{2\rho}(x_i)$, in particular on $B_\rho(x_i)$. (One should not read this off the mere $1$-Lipschitz property of $r_h$, which would only give $r_h>\rho$; the tube construction is what supplies the stronger uniform scale.) So a positive-measure family of patches with a **fixed** harmonic scale exists, extracted from one noncollapsed ball. Global noncollapse is not needed and is not obtained.

## 2. Convergence and smoothness — correct, and the two-step order matters

In harmonic coordinates with $r_h\ge\rho$, bounded Ricci gives a priori $C^{1,\beta}\cap W^{2,p}$ metric bounds for all $\beta<1$, $p<\infty$ (Definition 2.9 discussion). Hence $g_i\to g_\infty$ in $C^{1,\beta}$ strongly, $g_i\rightharpoonup g_\infty$ in $W^{2,p}$.

Passing (6) to the limit is legitimate: $Q(g_i,\partial g_i)\to Q(g_\infty,\partial g_\infty)$ uniformly, and $g_i^{kl}\partial_k\partial_l g_{i,ab}\rightharpoonup g_\infty^{kl}\partial_k\partial_l g_{\infty,ab}$ (uniform coefficient $\times$ weak-$L^p$ second derivatives), while $E_i\to0$ in $L^\infty$. This gives $\mathrm{Ric}(g_\infty)=-g_\infty$ distributionally; elliptic Schauder bootstrap on the defect-free quasilinear system makes $g_\infty$ smooth.

The note's insistence on the **order** is right and necessary: $E_i\to0$ in $L^\infty$ does not give $C^\alpha$ convergence of $E_i$, so $C^{2,\alpha}$ metric convergence is not available. The correct upgrade — strong $W^{2,p}_{\rm loc}$ — follows only *after* smoothness of $g_\infty$: interior $L^p$ estimate for $L_i=g_i^{kl}\partial_k\partial_l$ applied to $g_i-g_\infty$ gives
$$
\|g_i-g_\infty\|_{W^{2,p}(B')}\le C\big(\|-2(RHS_i-RHS_\infty)+(L_\infty-L_i)g_\infty\|_{L^p(B)}+\|g_i-g_\infty\|_{L^p(B)}\big)\to0,
$$
using $RHS_i=-g_i-Q(g_i,\partial g_i)+E_i\to RHS_\infty$ strongly in $L^p$, $g_i^{kl}\to g_\infty^{kl}$ uniformly, and $\partial^2 g_\infty$ bounded. Consequently $\mathrm{Rm}(g_i)\to\mathrm{Rm}(g_\infty)$ strongly in $L^p_{\rm loc}$. This is enough to pass algebraic curvature expressions, and it does **not** give sequence-level $C^{2,\alpha}$ convergence — consistent with the absence of any $\nabla\mathrm{Ric}$ control.

## 3. Transfer of the $O(A\delta^2)$ deficits — correct because $A$ is fixed

On the fixed critical manifold $A$ is a constant, so each nonnegative deficit density integrates to $\int_M \mathfrak d_i=O(A\delta_i^2)\to0$; restriction to any patch $U_i\subset M$ is automatic, $\int_{U_i}\mathfrak d_i\to0$. This is the cleanest of the three cases in `step5_ttcs01_verifier2_integration.md` §3 (total global integral controls every subset), and it is exactly the situation here. The normalized-average case, where a single ball would be insufficient, arises only when the topology (hence $A$, cube dimension) varies; that reservation is correctly recorded but does not bear on the fixed-manifold statement.

For the algebraic curvature deficit, strong $L^p_{\rm loc}$ convergence then gives $(s_\infty+8\sqrt6|W^+_\infty|)=0$ a.e., and with $s_\infty=-4$ (from $\mathrm{Ric}=-g$), $|W^+_\infty|=\tfrac1{2\sqrt6}$, hence $q_\infty=-s_\infty+\sqrt6 w_\infty=4+\tfrac12=\tfrac92$ on the patch. This is a purely local consequence and matches (8).

## 4. Nonzero limiting eigenform and the double eigenvalue — justified, with one estimate to spell out

The nonvanishing is genuinely earned and does not rest on the monopole selection:

- $H_i$ is the $g_i$-harmonic self-dual representative of the fixed class $a^+$; it is canonical (not a chosen monopole). Uniform local mass $\int_{B_\rho}|H_i|^2\le(a_i^+)^2=p_i\le K\to A$ holds. With $\Delta_{g_i}H_i=0$ and $g_i\to g_\infty$ in $C^{1,\beta}$, interior elliptic estimates give $H_i\to H_\infty$ in $C^{1,\alpha}(B_{\rho/2})$ (subsequence), $H_\infty$ harmonic self-dual for $g_\infty$.
- The $L^2$ identity (17), together with $q_i\to\tfrac92$ in $L^p_{\rm loc}$, gives $|2\pi H_i|\to \tfrac{q_\infty}{3\sqrt2}=\tfrac{3}{2\sqrt2}$ in $L^2(B_\rho)$. This forces a strictly positive $L^2$ mass lower bound on the patch, so $H_\infty\ne0$ and in fact $|H_\infty|\equiv\tfrac{3}{4\sqrt2\pi}=c_0$ there. This is (9), and it is correct.

On the double-eigenvalue point there is an apparent tension with `verifier2` §3 ("fixing $|W^+_\infty|$ does not imply a double eigenvalue"). The two statements are compatible and both correct: $|W^+|$ alone indeed does not, but the input used in (10) is $D_{\rm eig}=0$, not $|W^+|$. The pointwise integrand $W^+(\psi,\psi)+\sqrt{\tfrac23}w|\psi|^2\ge0$ (since $\lambda_{\min}(W^+)\ge-\sqrt{\tfrac23}|W^+|$ for trace-free symmetric $3\times3$), so $D_{\rm eig}=0$ forces, where $\psi\ne0$, both $\psi/|\psi|$ in the lowest eigenline **and** $\lambda_{\min}=-\sqrt{\tfrac23}|W^+|$. Saturation of that sharp bound is attained exactly when the two larger eigenvalues coincide ($a=b$, $c=-2a$, $2a^2+c^2=1\Rightarrow c=-\sqrt{2/3}$). Hence the double eigenvalue does follow from $D_{\rm eig}=0$, and with $|W^+_\infty|^2=\tfrac1{24}$ one gets $(-\tfrac16,\tfrac1{12},\tfrac1{12})$ uniquely. The note is right; the `verifier2` remark is a correct warning against the weaker $|W^+|$-only route.

Transfer of $D_{\rm eig}=0$ to the patch is valid because its density is nonnegative, so $\int_{B_\rho}[\cdot]\le\tfrac12 D_{\rm eig}=O(A\delta_i^2)\to0$. Passing to the limit needs $\psi_i\to\psi_\infty$ in $L^2(B_{\rho/2})$: from (16) $f_i\varphi_i\to-6\sqrt2\pi H_\infty$ in $L^2$, $f_i\to f_\infty=\sqrt{9/2}>0$, so $\varphi_i\to\varphi_\infty=-6\sqrt2\pi H_\infty/f_\infty\ne0$ in $L^2$; with $W^+_i\to W^+_\infty$ in $L^p$ the nonnegative quadratic form passes and vanishes on the patch, giving pointwise saturation, hence the spectrum a.e. and then everywhere by smoothness.

Two points still want an explicit line:

1. **Coherent selection across $i$ and regularization.** Because $w=|W^+|$ is only Lipschitz at the zero set of $W^+$, the optimal weight $f=\sqrt q$ is regularized by smooth $f_k\to\sqrt q$, and (13)–(17) hold with $\Delta_a+o_k(1)$. This does not require a canonical convergent monopole sequence: for each $i$ choose $k(i)$ so the regularization remainder is $\le A\delta_i^2$ (possible since $o_k(1)\to0$ at fixed $i$). Then $\psi_i:=\psi_i^{(k(i))}$ has total deficit $O(A\delta_i^2)\to0$, and the limiting eigenform is anchored to the canonical $H_\infty$, so the selection ambiguity does not affect $\psi_\infty$. This diagonal argument closes the "coherent monopole" concern and should be written explicitly.

2. **Local $L^\infty$ control of $\psi_i$.** To pass $W^+_i(\psi_i,\psi_i)$ in $L^1$ (given $W^+_i\to W^+_\infty$ only in $L^p$) one uses a uniform local sup bound on the rescaled spinor: the Weitzenböck maximum-principle bound $|\Phi|^2\le \sup(-s)/f\le C$ (with $f\ge\sqrt{q}\ge\sqrt{9/2-o(1)}>0$), then interpolation with $L^2$ convergence gives $\psi_i\to\psi_\infty$ in every $L^q$. This rescaled-equation bound is used implicitly and deserves one explicit sentence; it is very likely fine but is currently unstated.

## 5. Internal consistency of the calibrated model — confirmed

At $(-\tfrac16,\tfrac1{12},\tfrac1{12})$: $|W^+|^2=\tfrac1{36}+\tfrac2{144}=\tfrac1{24}$, $\det W^+=-\tfrac1{864}$, $s=-4$. Since $|W^+|$ is constant, $\Delta|W^+|^2=0$, so (15) gives $2|\nabla W^+|^2=-s|W^+|^2+36\det W^+=\tfrac16-\tfrac1{24}=\tfrac18$, i.e. $|\nabla W^+|^2=\tfrac1{16}$. This matches (16) and shows the model is nonparallel with constant norm — a bona fide, non-flat solution of the Bochner identity. This is a strong positive check that the calibrated germ is an actual local object, not an artifact.

## 6. No local contradiction; the mechanism is global

Step5 §3 is the load-bearing point and it is correct. Derdzinski's two-eigenvalue structure makes $\widetilde g=f^2 g_\infty$ Kähler with $s<0$, $f^2\widetilde s=-1$, and $\Delta_{g_\infty}f=-\tfrac12 f$. On a ball this positive-$f$ equation is solvable (it is a Helmholtz-type equation below the first Dirichlet value), so the calibrated germ is locally conformally Kähler and not contradictory. Only on a **closed** $M$ does integrating $\Delta f=-\tfrac12 f$ give $0=-\tfrac12\int_M f<0$; equivalently the exact saturation yields a global almost-Kähler form and, being Einstein, a Kähler–Einstein metric contradicting the connected-sum topology (the "bounded-geometry exclusion theorem," `quantitative_deficit_analysis.md` §5). The obstruction lives in the compact Stokes step, which a single patch or a noncompact pointed germ cannot perform.

The weak-Bianchi remark (17) is also correct and relevant: $\|E_i\|_\infty\le\delta$ controls $\mathrm{Ric}^\circ$ pointwise but not its derivatives, so no strong Cotton or $\nabla W^+$ estimate is available; consistent with $|\nabla W^+_\infty|^2=\tfrac1{16}\ne0$, i.e. one cannot force a parallel $W^+$.

## 7. Strongest theorem actually justified

> Let $M$ be a fixed critical Ishida–LeBrun manifold ($m=2,3$, $A>0$, $D=A/3$) with $\|g_i^{-1}(\mathrm{Ric}_{g_i}+g_i)\|_{L^\infty}=\delta_i\to0$ and $\mathrm{Vol}_{g_i}B_1(p_i)\ge v>0$ for one sequence of balls. Then there is $\rho(v)>0$ and points $x_i\in B_{1/2}(p_i)$ with $r_h(x_i)\ge2\rho$ such that, along a subsequence, in harmonic coordinates $g_i\to g_\infty$ in $C^{1,\beta}$ and strongly in $W^{2,p}_{\rm loc}$, with $g_\infty$ smooth and $\mathrm{Ric}(g_\infty)=-g_\infty$. On the germ, $s_\infty=-4$, $|W^+_\infty|=\tfrac1{2\sqrt6}$; the harmonic self-dual form $H_i\to H_\infty$ with $|H_\infty|\equiv\tfrac{3}{4\sqrt2\pi}>0$; and, using a diagonally selected regularized monopole so its deficit is $O(A\delta_i^2)$, the eigenvalue defect transfers to force $\operatorname{Spec}(W^+_\infty)=(-\tfrac16,\tfrac1{12},\tfrac1{12})$, $|\nabla W^+_\infty|^2=\tfrac1{16}$, and $g_\infty$ locally conformally Kähler ($\Delta_{g_\infty}f=-\tfrac12 f$, $f>0$).

This is the maximal justified statement. It is a rigidity/structure result on an open Einstein germ; it contains no contradiction. It does not recover global topology, a global Einstein metric, a diameter, or completeness, and it does not remove orbifold points or ALE bubbling (Antonelli–Székelyhidi removable-singularity input presupposes an $L^\infty$ extension across a closed smooth manifold and does not cover generic $\mathbb R^4/\Gamma$ cone points).

## 8. What can follow about $\sup_p\mathrm{Vol}\,B_1$

Precisely: **nothing** follows from the local analysis as it stands, because the local projector obstruction is not valid (§6 shows the calibrated spectrum is locally realizable).

If, hypothetically, one *did* have a valid local obstruction — a theorem that no smooth open Einstein germ can carry $(-\tfrac16,\tfrac1{12},\tfrac1{12})$ with the saturating self-dual form — then the contrapositive of the extraction above would give only
$$
\sup_p \mathrm{Vol}_{g_i}B_1(p)\longrightarrow0,
$$
i.e. every unit ball collapses (uniform/total collapse of the sequence). It would **not** produce a contradiction to the sequence's existence: total volume collapse is permitted (e.g. round lens-space quotients carry exact $s<0$ Einstein metrics with normalized volume $\to0$; and Anderson's $T^3$-collapsing family in Cheeger–Naber Example 2.16 shows collapse with $|\mathrm{Ric}|\to0$ and $b_2\to\infty$). So even a valid local obstruction would leave the counterexample-compatible mechanism intact (anisotropic collapse / cusp escape / $W^-$-carrying concentration away from the noncollapsed part).

Therefore any decisive advance toward a pinching gap must be global, in one of two forms:

- **Restore the closed manifold**: uniform unit-ball noncollapse on all of $M_i$ *plus* a diameter bound *plus* removal of curvature concentration (orbifold points, ALE bubble trees). Then Cheeger compactness yields a genuine Kähler–Einstein limit and the compact integration of $\Delta f=-\tfrac12 f$ (or the almost-Kähler/Armstrong route) closes it. This is exactly the "bounded-geometry exclusion theorem," whose hypotheses (42) are the missing global inputs.
- **Classify complete conformally-Kähler ends** of the profile (7)–(14) with end behavior strong enough to reinstate a global identity (e.g. an integrated Stokes relation on a complete noncompact germ). Absent such control, the germ analysis is consistent with a non-existent global contradiction.

## 9. Items to make fully airtight

1. Write the diagonal $k(i)$ selection so the regularized-monopole deficit is provably $O(A\delta_i^2)$ (§4 point 1).
2. State the rescaled-SW $L^\infty$ bound $|\Phi_i|^2\le \sup(-s)/f\le C$ used to upgrade $\psi_i\to\psi_\infty$ from $L^2$ to $L^q$ (§4 point 2), so the $L^1$ passage of $W^+_i(\psi_i,\psi_i)$ is unconditional.
3. Note explicitly that $H_\infty\ne0$ uses only harmonic-form compactness plus (17) and $q_\infty=\tfrac92$, hence is independent of the monopole-selection ambiguity — this is the cleanest way to present the nonvanishing and forestalls the natural worry.

With these three lines added, the local structure theorem in §7 is rigorous. The reach of the conclusion is exactly local; the sought contradiction, and any statement about $\sup_p\mathrm{Vol}\,B_1$, requires the global step, which remains the open scientific substance.