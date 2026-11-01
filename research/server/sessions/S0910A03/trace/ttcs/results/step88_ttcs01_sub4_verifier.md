# TTCS Independent Branch Record

```json
{
  "step_id": 88,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step87_resolvent_obstruction_theorem.md",
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/workspace/scripts/step88_minimal_separator_verify.py",
    "Sessions/S0910A03/workspace/data/step88_minimal_separator_verify.json"
  ]
}
```

## Task

Independently verify and strengthen the proposed removal of reflection from the Step 87 forced OT obstruction. Work in a complete 4-manifold with a free orthogonally transitive T^2 action, quotient base B diffeomorphic to a cylinder, exact outward expanding cusp ends, and E=Ric+3g with ||E||op<=delta. (i) For any invariant minimal hypersurface Sigma=pi^{-1}(C) over an essential closed base curve C, derive with explicit normal and induced-measure conventions the contracted Gauss formula and the periodic intrinsic T^3 scalar identity for q=ds^2+G(s), G=e^sigma M. Check whether <e_s>=12-2<D>+2<|II|^2>+<h^2> and hence >=12-8delta is exactly correct, where D=tr E-2E(nu,nu), h=sigma_s, e_s=|U_s|^2, averages use rho ds, and full base e dominates e_s. (ii) Prove or find the precise missing hypotheses in obtaining an interior smooth essential-loop minimizer for length in the auxiliary metric rho^2 gamma_B, using the two expanding ends. Check equivalence between geodesicity of C for rho^2 gamma_B and minimality of pi^{-1}(C) in g, and analyze boundary barriers/properness rather than assuming reflection or a global Gaussian foliation. (iii) Check that Step 87's complete-base massive-resolvent ceiling applies unchanged, and state the strongest mathematically justified theorem. Identify any subtle failure involving completeness, end orientation, homotopy-class minimization, self-intersection, weighted averages, or attachment regularity.

## Output

## Verifier memo — removal of reflection from the Step 87 forced OT obstruction

Session `S0910A03`, independent check in clean context. I re-derived parts (i)–(iii) from scratch with explicit conventions, cross-checked against `step88_minimal_separator_verify.py`/`.json`, and re-examined the Step 87 ceiling for hidden reflection dependence. The short statement: the floor identity and its $\ge 12-8\delta$ consequence are exactly correct, the minimal-loop existence argument is sound provided a small number of stated hypotheses are added, and the ceiling transfers with no reflection input. The obstruction at small $\delta$ is robust; the numerical threshold $\delta_*\approx0.246$ inherits whatever precision the Step 85–87 Bochner/resolvent constants carry.

---

### Part (i): the two Gauss reductions and the floor

**Conventions I fixed.** $M^4$ carries a free OT $T^2$ action, $g=\gamma_B+G_{ab}\,d\xi^a d\xi^b$, $G=e^\sigma M$, $\det M=1$, so orbit area $\rho=\sqrt{\det G}=e^\sigma$ and $h:=\sigma_s=(\log\rho)_s$. For an essential closed base curve $C$, take $s$ = $\gamma_B$-arclength, $\nu$ = $\gamma_B$-unit normal to $C$ in $B$ (this is automatically the unit normal of $\Sigma=\pi^{-1}(C)$ in $M$, since OT makes base and orbit directions orthogonal). The induced metric on $\Sigma$ is exactly $q=ds^2+G(s)$ with $s$ periodic — no cross terms, precisely because of orthogonal transitivity. Averages use $d\mu=\rho\,ds$, which is the reduced $\Sigma$-volume measure.

**Contracted Gauss, $\Sigma^3\subset M^4$.** With the Riemannian contracted Gauss equation $R_\Sigma=R_M-2\operatorname{Ric}_M(\nu,\nu)+H^2-|II|^2$ (I verified the sign on $S^{n-1}(r)\subset\mathbb R^n$), $R_M=\operatorname{tr}E-12$, $\operatorname{Ric}_M(\nu,\nu)=E(\nu,\nu)-3$, and minimality $H=0$:
$$R_\Sigma=-6+D-|II|^2,\qquad D=\operatorname{tr}E-2E(\nu,\nu).$$
This is the script's `gauss_expected`.

**Intrinsic $T^3$ scalar of $q=ds^2+G(s)$.** For a metric over a line with flat orbit fibers, $R_q=-2\operatorname{tr}\dot k-(\operatorname{tr}k)^2-\operatorname{tr}(k^2)$ where $k=\tfrac12G^{-1}\dot G$ is the orbit shape operator. I benchmarked this on $\mathbb H^3$ ($G=e^{2s}I\Rightarrow k=I,R_q=-6$), which fixes the signs. Writing $P=M^{-1}M_s$ ($\operatorname{tr}P=0$): $\operatorname{tr}k=h$, $\operatorname{tr}\dot k=h_s$, $\operatorname{tr}(k^2)=\tfrac12h^2+\tfrac14\operatorname{tr}(P^2)$. With the shape-map normalization $e_s=|U_s|^2=\tfrac12\operatorname{tr}(P^2)$ (this is the normalization that reproduces the $\mathbb H^2$-curvature $-1$ target and matches Steps 82/85/88),
$$R_q=-2h_s-\tfrac32h^2-\tfrac12e_s.$$
Periodic integration against $\rho\,ds$ with $\rho_s=h\rho$ moves the $h_s$ term: $\int(-2h_s)\rho\,ds=+2\int h^2\rho\,ds$, giving
$$\langle R_q\rangle=\tfrac12\langle h^2\rangle-\tfrac12\langle e_s\rangle.$$
This is the script's `weighted_scalar_after_periodic_ibp`, and it agrees with Step 82 eq. (5.1).

**The floor.** Since $R_\Sigma=R_q$ (both are the intrinsic scalar of $\Sigma$), equating the two averaged expressions and solving:
$$\boxed{\ \langle e_s\rangle=12-2\langle D\rangle+2\langle|II|^2\rangle+\langle h^2\rangle\ }$$
matching `separator_energy_expected`. Dropping $|II|^2\ge0,\ h^2\ge0$, and using that in a $g$-orthonormal frame $\{e_1,e_2,e_3,\nu\}$ one has $D=E_{11}+E_{22}+E_{33}-E_{\nu\nu}$ with each diagonal entry in $[-\delta,\delta]$, hence $|D|\le4\delta$:
$$\langle e_s\rangle\ge 12-8\delta.$$
Because $e=|U_s|^2+|U_\nu|^2\ge e_s$ pointwise on $C$, this gives $\sup_B e\ge\langle e\rangle_C\ge\langle e_s\rangle_C\ge12-8\delta$, i.e. a floor on the *same* $\sup_B e$ that the ceiling bounds. **Part (i) is exactly correct.** The $4\delta$ coefficient is the frame bound (sharper than the naive $6\delta$ from $|\operatorname{tr}E|+2|E_{\nu\nu}|$); it is attained by a diagonal $E$, so $12-8\delta$ is the true content of the identity, not slack.

Two facts this rests on that are worth keeping visible: the shape-map normalization $e_s=\tfrac12\operatorname{tr}(P^2)$ (any other constant rescales the "12"), and the exact-Einstein value $R_M=4\lambda=-12$ from the $\lambda=-3$ normalization. Both are internally consistent with Steps 82/85/87.

---

### Part (ii): interior minimal essential loop

**Minimal $\iff$ geodesic in $\rho^2\gamma_B$.** The mean curvature of $\Sigma=\pi^{-1}(C)$ is $H=\kappa_g(C)+\partial_\nu\log\rho$, where $\kappa_g$ is the $\gamma_B$-geodesic curvature of $C$ and the orbit-block of $II$ contributes $\tfrac12 G^{ab}\partial_\nu G_{ab}=\partial_\nu\log\rho$. Under the conformal change $\tilde\gamma=e^{2\sigma}\gamma_B=\rho^2\gamma_B$, geodesic curvature transforms as $\tilde\kappa=e^{-\sigma}(\kappa_g+\partial_\nu\sigma)$, so $\tilde\kappa=0\iff\kappa_g+\partial_\nu\log\rho=0\iff H=0$. Equivalently, the $\tilde\gamma$-length element is $\rho\,ds_{\gamma_B}$, so $\tilde\gamma$-length of $C$ equals $\operatorname{Area}_g(\Sigma)/\operatorname{vol}(T^2)$: minimizing $\Sigma$-area = minimizing $\tilde\gamma$-length of $C$. The equivalence is **correct**.

**Existence, and the coercivity that replaces reflection.** On the exact outward-expanding end $\gamma_B=dt^2+e^{2t}dz^2,\ \rho=ce^{2t}$, the auxiliary metric is $\tilde\gamma=c^2e^{4t}dt^2+c^2e^{6t}dz^2$. Any essential loop in $\{t\ge T\}$ has $\tilde\gamma$-length $\ge c\int e^{3t}|z'|\,du\ge cL_z e^{3T}\to\infty$. Since *both* ends are outward-expanding, the essential-class length function is proper (coercive) and $\to\infty$ at both ends. The $\tilde\gamma$-radial distance $\int^\infty ce^{2t}dt$ also diverges, so $(B,\tilde\gamma)$ is complete. Coercivity + completeness + non-contractibility (positive infimum length) give, by the direct method / Birkhoff curve shortening, a smooth closed $\tilde\gamma$-geodesic realizing the minimal length of the primitive essential class, located in a compact interior core. **This is the honest replacement for reflection: the two expanding ends provide barriers at infinity, so no artificial totally-geodesic center slice or global Gaussian foliation is needed.** Regularity of $\Sigma$ is then automatic ($\Sigma=\pi^{-1}(\text{smooth geodesic})$), avoiding Almgren–Pitts min-max regularity entirely — a genuine simplification over the reflected construction.

**Precise hypotheses that must be added / stated (these are the true content of (ii)):**

1. **Both ends expanding.** Coercivity of the loop length *and* $e\to0$ at the ends (needed for the ceiling) both require every end to be an exact outward-expanding cusp. A single contracting or non-expanding end lets minimizing loops escape or drift, and the interior minimizer is lost. The two-expanding-end orientation is load-bearing and is simultaneously what the ceiling needs.

2. **Primitive class ⇒ embedded loop.** Minimize in the *primitive* generator of $\pi_1(S^1)$. A shortest loop in a primitive free-homotopy class on a surface is simple; on an orientable cylinder it is also two-sided, so $\nu$ is globally defined and $\Sigma$ is an embedded smooth $T^3$. If one minimized in a non-primitive class the geodesic could be a multiple cover, giving an immersed non-embedded $\Sigma$ and invalidating the single-normal Gauss computation of part (i). This is the one place self-intersection could intrude, and it is closed by "primitive ⇒ simple."

3. **Orthogonal transitivity is essential.** The induced metric $q=ds^2+G(s)$ has no cross terms only under OT. With approximate twist ($c_X,c_Y\neq0$) the induced metric acquires off-diagonal terms and the intrinsic identity of part (i) changes. So the theorem stays inside the free-OT class, as in Step 87 §10.

4. **Exactness at the ends, and smooth complete gluing.** Coercivity used the *exact* cusp form near each end; if the cusp is only asymptotic, one needs quantitative decay of $\rho$'s growth and of $e$ rather than the exact model. The interior/transition region must be $C^\infty$ and complete so that $\tilde\gamma$ is smooth and the minimizer is smooth; keeping the ends far out lets $C$ avoid any gluing seam.

No missing "barrier" beyond these; the properness argument is the correct mechanism and it is complete once (1)–(4) are fixed.

---

### Part (iii): ceiling transfer and the strongest theorem

**The Step 87 ceiling uses no reflection.** Its ingredients — forced Bochner (1.1), the massive comparison $(-L+\kappa)e\le\kappa^2+8\delta^2-2\operatorname{div}_\sigma V$ (3.1), the Li–Yau/Bakry–Émery Fisher-information Riccati bound $I(t)\le NK/(1-e^{-2Kt})$ (4.1), the resolvent gradient constant $C_\kappa=\sqrt{N/K}=2/\sqrt{3+\delta}$ (5.1), and the Duhamel comparison (6.1)–(7.2) giving $\sup e\le\mathcal B(\delta)$ — are all pointwise or global-analytic on the complete weighted base $(B,\gamma_B,d\mu=e^\sigma dA)$. Reflection appeared in Step 87 only in the *floor* (the reflected-center identity), now replaced by part (i). The ceiling requirements are all met by the two-expanding-end geometry:

- **Completeness:** the base has a compact core plus two infinite expanding ends; complete. (Note the terminology: these are expanding/flaring ends of infinite length, not finite-volume metric cusps — completeness holds because $\int^\infty dt=\infty$.)
- **$\mathrm{Ric}^4_f\ge-(3+\delta)\gamma_B$ globally:** from $\|E\|\le\delta$ via (2.1). The effective dimension $N=4=\dim B+\dim T^2$ is exactly the $T^2$-over-surface collapse dimension, and the $\tfrac12 d\sigma\otimes d\sigma$ term is precisely the $\tfrac1{N-n}$ Bakry–Émery correction with $N-n=2$; the dimensional bookkeeping is coherent.
- **Boundedness of $e$:** $e$ is continuous and $\to0$ at both ends, hence bounded with $\sup$ attained in the core — automatic here, so no a priori boundedness assumption is needed (cleaner than the reflected version).
- **$V\to0$ at ends and $|\nabla G_\kappa|\in L^1$** for the integration by parts: $|V|\le2\delta\sqrt e\to0$; the $L^1$ bound follows from the Fisher/resolvent estimate. 
- **Stochastic completeness** ($P_t1=1$) from $CD(-K,N)$ with finite $N$ on a complete manifold.

I re-checked the internal analytic pieces: the Riccati solution $y=NK/(1-e^{-2Kt})$ solves $y'=2Ky-\tfrac2N y^2$ with $y(0^+)=\infty$ (via $w=1/y$, $w'+2Kw=2/N$), and $C_\kappa=\tfrac{\sqrt{NK}}{2K}B(1,\tfrac12)=\sqrt{N/K}$ with $B(1,\tfrac12)=2$. These are self-consistent. **The ceiling applies unchanged**, with $\mathcal B(0)=6$.

**Strongest justified theorem.**

> Let $(M^4,g)$ be complete and smooth with a free, isometric, orthogonally transitive $T^2$ action whose quotient $B=M/T^2$ is a cylinder with two ends each equivariantly exactly isometric to an outward-expanding round cusp end ($\gamma_B=dt^2+e^{2t}dz^2,\ \rho=ce^{2t}$, orbit map constant), and suppose $\|\operatorname{Ric}_g+3g\|_{\mathrm{op}}\le\delta$ everywhere. Then, granting the forced Bochner inequality and the massive-resolvent ceiling of Steps 85–87, for $\delta<\delta_*\approx0.246$ no such $g$ exists.

Proof skeleton: the primitive essential class has an interior embedded $\tilde\gamma=\rho^2\gamma_B$-shortest geodesic $C$ (part ii); $\Sigma=\pi^{-1}(C)$ is a smooth minimal invariant $T^3$; part (i) gives $\sup_B e\ge\langle e_s\rangle_C\ge12-8\delta$; the ceiling gives $\sup_B e\le\mathcal B(\delta)$; since $\mathcal B(0)=6<12$ with margin, the two cross at $\delta_*\approx0.246$ (`unchanged_crossing_delta_star`$=0.24625$), and below it the floor exceeds the ceiling. The $\delta=0$ contradiction $12>6$ is robust.

**Subtle points the task asked me to name, with status:**

- **Completeness / end orientation:** both hold and are mutually reinforcing — expanding ends give coercivity (floor) *and* $e\to0$ (ceiling). This is the linchpin; a mixed-orientation cylinder breaks both simultaneously.
- **Homotopy-class minimization / self-intersection:** resolved by minimizing the primitive class (shortest ⇒ simple ⇒ embedded ⇒ single normal). Non-primitive minimization would give an immersed $\Sigma$ and void part (i).
- **Weighted averages:** the "$12$" depends on the $e_s=\tfrac12\operatorname{tr}(P^2)$ normalization and on $\rho\,ds$ being the reduced $\Sigma$-measure; both are consistent throughout.
- **Attachment regularity:** needs exact cusps on end-neighborhoods and $C^\infty$ complete gluing; keep $C$ in the core away from any seam.
- **OT dependence:** the induced diagonal metric and the whole identity require orthogonal transitivity; approximate twist is outside this reach.

**What the theorem inherits and does not itself establish.** This memo verifies the floor side (i)–(ii) rigorously and confirms the ceiling is reflection-free (iii). The load-bearing inputs I did *not* re-derive are the forced Bochner inequality (1.1) with its constants, the $\operatorname{div}_\sigma V$ handling and the self-consistent quadratic (7.1)–(7.2), and the Fisher-Riccati ceiling constant. The qualitative conclusion (obstruction for small $\delta$) is stable against perturbations of these constants because the $\delta=0$ gap $12$ vs $6$ is wide; the exact $\delta_*$ is only as sharp as those inputs. Finally, as noted in Step 87 §10, this addresses the $\operatorname{Ric}=-3g$ free-OT interpolation setting only; the positive-normalized branch, singular orbits, non-OT graph metrics, $N\#N$ ($S^3$-interface) necks, and the all-dimensional quantifier of Yau 26 remain untouched by this construction.

**Net:** the removal of reflection is legitimate and, if anything, cleaner than the reflected version (automatic boundedness, automatic $\Sigma$-regularity, natural coercivity). The three algebraic residuals in `step88_minimal_separator_verify.json` are genuine confirmations of the coefficient bookkeeping; my independent derivation reproduces every one, and the floor $\langle e_s\rangle\ge12-8\delta$ is exact under the stated conventions.