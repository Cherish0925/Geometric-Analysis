# TTCS Independent Branch Record

```json
{
  "step_id": 45,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step45_consolidated_IL_negative_gap_proof.md",
    "Sessions/S0910A01/workspace/notes/step44_preceptor_reading_first_exit_terminal_chain.md",
    "Sessions/S0910A01/workspace/notes/step43_H_WU_resolution_weighted_evolution.md"
  ]
}
```

## Task

Independently verify the mathematical correctness of the consolidated restricted negative Ishida-LeBrun gap theorem proof. Focus on three load-bearing points:

1. **Proposition 3.2 (quantitative local Φ lower bound from compactness).** The proof argues: on Riemannian 4-balls with |Rm| ≤ K and Vol(B_{ρ/2}) ≥ v₀, the density Φ = |E|² + (s+4)² + (s+8√6|W⁺|)² + G has fint Φ ≥ η(K,ρ,v₀) > 0. Otherwise a minimizing sequence converges smoothly (Cheeger-Gromov) to a germ with Φ ≡ 0, which is Einstein with the calibrated W⁺ spectrum, contradicting Derdziński. Is this compactness argument valid? Are the hypotheses sufficient for smooth subsequential convergence on B_{ρ/2}? Does Φ = 0 really force all four calibrated conditions, or could a density vanishing in the mean have a nontrivial limit? Does the passage from mean-zero Φ to pointwise Φ=0 on the limit require strong L¹ convergence (which Cheeger-Gromov does supply) or something else?

2. **Terminal averaging and support-count independence.** The Liouville average integral over P_i^in is claimed to be bounded by C(K,ρ)∫_M Φ without a factor depending on the number of supports. Check whether the Liouville-Rauch double integral over P_i^in can indeed be controlled by a single global integral of Φ over M, given bounded curvature and the fact that different centers' pullback images may overlap in M.

3. **Coefficient regularization order of operations.** The proof constructs regularized flows b_ε = χ² + ε² for each ε > 0, obtains ε-uniform bounds from the geometric energies (NOT from the ε-dependent PDE constants), passes to a smooth limit solving the exact a = χ² equation, and only THEN applies stationary-complement and disjoint-support identities. Check whether the ε-uniform geometric bounds (§5.2 properties) are indeed sufficient for a common existence time and smooth compactness, or whether additional information is needed.

## Output

# Verification memo: consolidated restricted Ishida–LeBrun gap proof

Session S0910A01, Step 45 consolidation. I worked through the three load-bearing points you named, and along the way checked the algebraic backbone that they rest on (the calibration density, the Chern–Weil identity, and the connected-sum topology), because Points 1–3 are only meaningful if that backbone is internally consistent. It is. I report the backbone check first in compressed form, then the three points.

## Backbone checks (all consistent)

**Chern–Weil / signature identity (2.3)–(2.4).** With $I=\frac1{4\pi^2}\int(\frac{s^2}{24}+2|W^+|^2)$ and $J=\frac1{4\pi^2}\int\frac{|\mathring{\mathrm{Ric}}|^2}{2}$, the identity $I-J=(2\chi+3\tau)(M)$ is the standard Gauss–Bonnet/signature combination and is correct. For the connected sum $M=(\#_j X_j)\#N$ with $X_j$ of general type ($c_1^2=2\chi+3\tau$) I get $(2\chi+3\tau)(M)=\sum_j c_1^2(X_j)+(2\chi+3\tau)(N)-4m=A-D$, and $\frac{2A}{3}-q=A-D$ exactly when $q=D-\frac A3$. So (2.3), the definition of $q$, and $D_{\rm av}=J-q-\frac23\sum(e_\ell^+)^2$ with $0\le D_{\rm av}\le J$ under $q\ge0$ all cohere.

**Density $\Phi\ge0$ and the calibrated germ.** I verified the assertion $\mathcal G=f^2-(a_{*,-})^2\ge0$ pointwise. For a traceless symmetric $W^+$ with eigenvalues summing to zero, the smallest eigenvalue satisfies $w\ge-\sqrt{2/3}\,|W^+|$, hence $a_*=\frac23 s+2w\ge\frac23 s-2\sqrt{2/3}|W^+|=f$; combined with $f<0$ on the relevant regime this gives $|f|\ge a_{*,-}$, so $\mathcal G\ge0$, with equality forcing $w=-\sqrt{2/3}|W^+|$, i.e. the two-equal-eigenvalue pattern. Solving $\Phi=0$ pointwise: $s=-4$, $s+8\sqrt6|W^+|=0\Rightarrow|W^+|^2=1/24$, and $\mathcal G=0\Rightarrow\operatorname{spec}(W^+)=(-1/6,1/12,1/12)$. I checked these three numbers are mutually consistent ($|W^+|^2=1/36+2/144=1/24$) and that a Kähler–Einstein metric with $s=-4$ has $|W^+|^2=s^2/24=2/3\ne1/24$. So **if pointwise $\Phi_\infty=0$ is secured, the Derdziński contradiction is airtight** — including that $W^+_\infty\ne0$, which Derdziński requires. This last fact is exactly where Point 1 turns.

## Point 1 — Proposition 3.2 (local $\Phi$ lower bound)

The conclusion is correct, but the proof as written in §3.2 rests on a convergence statement that is not available from the stated hypotheses, and the correct mechanism is elliptic, not the bare Cheeger–Gromov compactness cited.

**Where the written argument is incomplete.** The hypotheses $|\mathrm{Rm}_{g_k}|\le K$ and $\mathrm{Vol}(B_{\rho/2})\ge v_0$ give (Anderson harmonic radius + Cheeger–Gromov–Taylor injectivity control) only $C^{1,\alpha}\cap W^{2,p}$ convergence of metrics in harmonic coordinates. A $C^0$ bound on curvature does **not** yield smooth convergence; curvature ($\sim\partial^2 g$) converges only weakly in $L^p$. Under weak curvature convergence the three Weyl-calibration terms of $\Phi$ transfer to the limit as one-sided inequalities. Concretely, $\int(s_k+8\sqrt6|W^+_k|)^2\to0$ together with weak convergence gives only
$$
s_\infty+8\sqrt6|W^+_\infty|\le0\ \Longrightarrow\ |W^+_\infty|^2\le\tfrac1{24},
$$
which permits $W^+_\infty=0$. A limit with $W^+_\infty=0$ (a constant-curvature germ, $\mathrm{Ric}=-g_\infty$, $s=-4$) is Einstein and produces **no** Derdziński contradiction, because Derdziński needs $W^+\ne0$. So mean-vanishing plus weak convergence is genuinely insufficient: it cannot exclude the flat-Weyl Einstein germ, and it does not pin the nonvanishing calibrated spectrum the contradiction consumes.

**Why the conclusion is nonetheless correct — the missing step.** Strong $L^2$ curvature convergence is in fact available, and it comes precisely from the $|E|^2$ term, matching the note's own remark that $|E|^2$ is essential. In harmonic coordinates,
$$
-\tfrac12 g_k^{ab}\partial_a\partial_b(g_k)_{ij}=\mathrm{Ric}(g_k)_{ij}-Q_{ij}(g_k,\partial g_k)
=-(g_k)_{ij}+(E_k)_{ij}-Q_{ij}.
$$
The mean-vanishing of $\Phi$ gives $\int_{B_{\rho/2}}|E_k|^2\to0$, i.e. $E_k\to0$ strongly in $L^2$. The elliptic coefficients $g_k^{ab}$ and the quadratic remainder $Q(g_k,\partial g_k)$ converge strongly (from $C^{1,\alpha}$ convergence of $g_k$ and $\partial g_k$). Hence the right side converges strongly in $L^2$, and the interior elliptic $L^2$ estimate makes $g_k$ Cauchy in $W^{2,2}_{\rm loc}$: **strong $W^{2,2}$ metric convergence, therefore strong $L^2$ convergence of the full curvature tensor.** Since every term of $\Phi$ is a continuous quadratic function of curvature dominated by the $L^\infty$ bound $K^2$, $\Phi_{g_k}\to\Phi_{g_\infty}$ in $L^1$, so $\fint\Phi_\infty=0$ and $\Phi_\infty\equiv0$ a.e. Weak lower semicontinuity of the $L^2$ norm already gives $E_\infty=0$, so $g_\infty$ is Einstein and (Einstein + harmonic coordinates) smooth; the strong $L^2$ curvature convergence then delivers the exact calibrated $W^+$ spectrum pointwise, and §0's algebra closes the Derdziński contradiction.

So Proposition 3.2 holds, but §3.2 should replace "converges smoothly (Cheeger–Gromov)" with the elliptic upgrade above. Note that §7.2 already states the correct strong $W^{2,p}$/strong-$L^p$-curvature convergence; §3.2 is simply written at a weaker level than §7.2 and must import the same mechanism. The only inputs needed are the ones present: $L^2$-smallness of $E$ (from $\Phi$), the $L^\infty$ curvature bound (for harmonic radius and for dominating $\Phi$), and noncollapse. The $L^\infty$ bound does double duty; the strong $L^2$ statement for $E$ is enough and does not even require interpolation to higher $L^p$.

**One item to confirm.** The passage from $\Phi=0$ pointwise to "at most two distinct eigenvalues of $W^+$" runs through $\mathcal G=0$; I verified this above. Nothing further is needed there.

## Point 2 — terminal averaging and support-count independence

This is valid; the support-count independence is genuine and comes from a Fubini exchange, not from any packing miracle.

Writing the Liouville average as $A_\rho\Phi(p)=\frac1{V_p}\int_{B_\rho(p)}\Phi$ with $V_p=\mathrm{Vol}(B_\rho(p))$, and using symmetry $p\in B_\rho(y)\iff y\in B_\rho(p)$,
$$
\int_{P_i^{\rm in}}A_\rho\Phi\,d\mu
\le\frac1{v_0}\int_M\Phi(y)\,\mu\!\left(P_i^{\rm in}\cap B_\rho(y)\right)d\mu(y)
\le\frac{V(K,\rho)}{v_0}\int_M\Phi\,d\mu.
$$
Each point $y$ is weighted by the measure of centers lying within $\rho$ of it, which is at most the volume of a single $\rho$-ball — independent of how many supports exist and independent of overlaps. Two comparison constants enter: the lower bound $V_p\ge v_0(K,\rho)$ (needs bounded curvature and the §6.4 geodesic buffer, both supplied on $P_i^{\rm in}$), and the upper bound $\mathrm{Vol}(B_\rho(y))\le V(K,\rho)$ (needs a lower Ricci bound near $y$). The upper bound is the mild ingredient; the only thing to confirm is that the **terminal** metric $g_i(T)$ carries a fixed global lower Ricci bound (e.g. $\mathrm{Ric}\ge-2g$) so the comparison holds for every $y\in M$, not only on the plateau. Off the plateau the flow forcing is $-2aE$ with $a$ small or zero, so the input bound drifts by $O(\theta r^2)$; that persistence should be stated. There is also a purely combinatorial route that avoids the global upper bound entirely: since the centers are $r$-separated and $\rho\le r/2$, $B_\rho(y)$ meets a bounded number of the disjoint $B_r(x_\alpha)$, so $\mu(P_i^{\rm in}\cap B_\rho(y))\le C\,\mathrm{Vol}(B_\rho)$ directly. Either way, the estimate (7.3) is correct and the constant depends only on $(K,\rho)$.

## Point 3 — coefficient regularization order of operations

The order of operations is the right one, and the §5.2 properties are the correct *structural* $\varepsilon$-uniform inputs. They are not, by themselves, a literally complete list; the substantive additional input is a propagated $\varepsilon$-uniform zeroth-order bound, which the notes import rather than re-derive.

**What §5.2 gives.** $0<b_\varepsilon\le2$, $\nabla^r b_\varepsilon=\nabla^r(\chi^2)$ ($\varepsilon$-independent), $|\nabla b_\varepsilon|^2/b_\varepsilon\le4|d\chi|^2$, $\chi^2/b_\varepsilon\le1$, and no derivative of $b_\varepsilon^{-1}$. These are exactly the quantities that keep the weighted energies for $U_m=b_\varepsilon T$ from degenerating as $b_\varepsilon\to0$ on $\{\chi=0\}$: the degeneracy ratios stay bounded and every top cutoff jet $C_{m+2}$ carries a $\chi$ that pairs with the weighted dissipation $\int\chi^2|\nabla U_m|^2|U_m|^{p-2}$ (Step 43 §§5–7). The two-step structure — start each $\varepsilon>0$ flow with the $\varepsilon$-dependent parabolicity $b_\varepsilon\ge\varepsilon^2$, then control it on a common interval by $\varepsilon$-uniform energies — is a sound vanishing-regularization strategy.

**What must be added for a common time and smooth compactness.**
1. **$\varepsilon$-uniform initial energies.** Since $b_\varepsilon(0)\le2$ and $g_0,\chi$ are fixed smooth, $\|U_m(0)\|_p\le2\|\nabla^m T_0\|_p$ uniformly. Immediate, but should be stated as the base of the induction.
2. **The propagated $\varepsilon$-uniform zeroth-order bound $\sup|b_\varepsilon T|\le K$.** This is the genuinely load-bearing input; the entire staggered $(U_m,C_{m+1})$ induction is conditional on it (the seed $|aT|\le K$ in §5.3, and the first-exit $K_2^\eta$ mechanism of §6). It is asserted from A03 Step 44 and the first-exit branches, not re-derived in these two notes. Its $\varepsilon$-uniform propagation on $[0,T_*]$ is the one place where the whole coefficient-regularization platform stands or fails, so it deserves an explicit self-contained statement here rather than a cross-reference.
3. **$\varepsilon$-uniform control of the DeTurck gauge.** The transported coefficient $\widehat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1}$ drives the gauge diffeomorphism $\varphi_t$; because $b_\varepsilon\le2$ with $\varepsilon$-independent derivatives, the gauge is plausibly $\varepsilon$-uniformly regular, but this is used implicitly and is worth one line.

**A convergence-notion point that affects support locations.** §5.2 states the limit solves the exact flow "in the Cheeger–Gromov sense on fixed coordinate patches." For the later identities (stationary complement, frozen outer metric, disjoint-support summation) the limit must be a flow on the *same* $M$ with the *same* fixed $\chi$; convergence only up to diffeomorphism could move supports and invalidate those identities. The $\varepsilon$-uniform energies give control of the actual coefficient functions where $\chi>0$ (there $b_\varepsilon\ge\chi^2>0$ recovers $T$ from $U$), and near-stationarity gives fixed-coordinate control on $\{\chi=0\}$. So fixed-coordinate (not diffeomorphism-quotient) convergence is available on all of $M$, but the note should say "fixed-coordinate" explicitly rather than "Cheeger–Gromov sense," to make clear the supports do not drift.

**Correct ordering, explicitly right.** The note is correct and careful that stationary-complement, disjoint-support summation, and global-$Q$ propagation are used only on the exact $a=\chi^2$ limit. For $\varepsilon>0$ the complement evolves by $-2\varepsilon^2(\mathrm{Ric}+g)\ne0$, so applying those identities at finite $\varepsilon$ would be an error; §1 of Step 44 and §5.2 of Step 45 avoid it correctly. Where $\chi=0$ the weighted energies give no $\varepsilon$-uniform curvature control (there $U=\varepsilon^2 T$), but the limit metric is stationary there and equal to the fixed smooth $g_0$, so no uniform curvature bound is needed off the supports — this is consistent.

## What remains to be written out

- In §3.2, the strong-$L^2$-curvature step (harmonic-coordinate elliptic upgrade from $E_k\to0$ in $L^2$) should be stated explicitly; the current "smooth Cheeger–Gromov convergence" phrasing understates and mis-states the mechanism, and weak convergence alone permits $W^+_\infty=0$, which would remove the Derdziński contradiction.
- In §7.1/§4.1, the persistence of a fixed global lower Ricci bound for the terminal metric $g_i(T)$ (or a statement of the combinatorial $r$-separation route) makes the constant $C(K,\rho)$ in the Fubini estimate rigorous.
- In §5, the $\varepsilon$-uniform zeroth-order bound $\sup|b_\varepsilon T|\le K$ on $[0,T_*]$ should be a self-contained proposition rather than a cross-reference, and the convergence should be stated as fixed-coordinate.

The topological backbone, the density positivity, and the calibrated-germ algebra I re-derived are correct and internally consistent, and the three load-bearing points are each valid after the specific derivational additions above — none of which points to a structural obstruction in the $\mathrm{Ric}\to-g$ Ishida–LeBrun argument. The additions in Points 1 and 3 are the ones that most change whether the written note is a complete proof of the restricted statement it targets.