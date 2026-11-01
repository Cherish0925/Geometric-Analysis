# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step92_route_comparison_and_ab_heat_sign.md",
    "Sessions/S0910A01/workspace/notes/step91_receiver_and_adjacent_green.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step47_entropy_degree_theorem.md",
    "Sessions/S0910A01/workspace/data/step92_ab_heat_sign_formula.json",
    "Sessions/S0910A01/workspace/data/step91_adjacent_ab_heat_spectral.json"
  ]
}
```

## Task

Verify the Step 92 route comparison and AB adjacent heat sign argument. Read the Step 92 note plus the Step 91 product note, Step 47 entropy/degree note, and Step 92 support data. Check especially: (1) whether the hyperbolic X#X continuity and corrected Lohkamp-ratio statement are mathematically accurate; (2) whether the AB-sector reduction after adjacent m=2 polarization cancellation to K_adj^AB=(1/512)∫ e^s A(s)B(s) ds is consistent with Step 91 normalization; (3) whether the claimed sign proof B(s)<0 via monotonicity of the scalar heat kernel at antipodal points on S^2 is actually valid for all s>0, or whether it needs an additional theorem/proof/correction; and (4) what remains before the result affects the full Ozuch coefficient or Yau-26. Give a direct scientific memo with any errors and repairs.

## Output

## Verification memo — Step 92 route comparison and the AB adjacent heat sign

I checked the four requested items by re-deriving the algebra, the series factorization, and the heat argument, and by cross-reading the Step 91 spectral form against the Step 92 integral form and the JSON numerics. Summary: items (1) and (2) are correct and internally consistent; item (3) is a true statement whose supporting result is asserted rather than proved and is genuinely load-bearing (I give the missing proof); item (4) is stated accurately and I sharpen the list. No arithmetic error found.

---

### (1) Hyperbolic X#X continuity and the Lohkamp-ratio statement — correct

I reproduced the Step 91/92 pinched-box algebra in the Ric≈−3g normalization. Writing Ricci eigenvalues as −3+r_i with |r_i|≤3ε, the Chern–Gauss–Bonnet Ricci integrand is

$$Q=\tfrac{s^2}{24}-\tfrac{|E|^2}{2}=\tfrac{s^2}{6}-\tfrac{|\mathrm{Ric}|^2}{2}=6-R+\tfrac{R^2}{6}-\tfrac12\textstyle\sum r_i^2,\quad R=\sum r_i.$$

The Hessian in the r_i is $\tfrac13 J-I$, indefinite (eigenvalues $\tfrac13$ once, $-1$ thrice), so the minimum over the box $[-3\varepsilon,3\varepsilon]^4$ sits at a vertex. Evaluating vertices with $j=k-2\in\{-2,\dots,2\}$ gives $Q=6-6\varepsilon j+6\varepsilon^2 j^2-18\varepsilon^2$; comparing $j=2$ and $j=1$ the difference is $6\varepsilon(3\varepsilon-1)\le0$ for $\varepsilon\le\tfrac13$, so the minimizer is all $r_i=+3\varepsilon$ (all Ricci eigenvalues $=-3(1-\varepsilon)$) with

$$Q_{\min}=6(1-\varepsilon)^2.$$

This confirms the Step 91/92 box bound. The volume chain then follows: with $\chi(X\#X)=2\chi(X)-2$ and $\mathrm{Vol}(X)=\tfrac{4\pi^2}{3}\chi(X)$,
$$\mathrm{Vol}(M,g)\le \frac{8\pi^2\chi(X\#X)}{6(1-\varepsilon)^2}=\frac{2\mathrm{Vol}(X)\,(1-1/\chi(X))}{(1-\varepsilon)^2},$$
and BCG after the scale $g\mapsto(1+\varepsilon)g$ (Ric unchanged as a (0,2)-tensor, so $\mathrm{Ric}\ge-3(1+\varepsilon)g\Rightarrow\mathrm{Ric}_{\tilde g}\ge-3\tilde g$) gives $\mathrm{Vol}(M,g)\ge 2\mathrm{Vol}(X)/(1+\varepsilon)^2$. Incompatibility is exactly $(1-\varepsilon)/(1+\varepsilon)>\sqrt{1-1/\chi}$, i.e. $\varepsilon<\dfrac{1-\sqrt{1-1/\chi}}{1+\sqrt{1-1/\chi}}=\dfrac1{4\chi}+O(\chi^{-2})$. This matches the note and matches, to leading order, the Step 47 result $\delta_*=1/(4m)+O(m^{-2})$ in the Ric≈−g normalization. So the assertion that Step 91/92 is the same obstruction as Step 47 with corrected constants is accurate.

The no-Einstein argument for X#X is also correct: $\lambda>0$ excluded by infinite (free-product) $\pi_1$ and Bonnet–Myers; $\lambda=0$ excluded by virtual abelianity of compact Ricci-flat $\pi_1$; $\lambda<0$ excluded because CGB at $\mathrm{Ric}=-3g$ forces $\mathrm{Vol}\le\tfrac{4\pi^2}{3}\chi(X\#X)=2\mathrm{Vol}(X)-\tfrac{8\pi^2}{3}$, against BCG's $\ge 2\mathrm{Vol}(X)$.

The Lohkamp-ratio remark is correct and worth keeping. If $-bg\le\mathrm{Ric}\le-ag$ with $0<a<b$, fitting into a prescribed interval $[c,C]$ with $c<C<0$ by a constant scale $t$ needs $b/t\le|c|$ and $a/t\ge|C|$, jointly solvable iff $b/a\le|c|/|C|$. So a metric with $\mathrm{Ric}<0$ (Lohkamp) does not by scaling meet an arbitrary tight sub-zero interval; the intrinsic ratio $b/a$ is invariant and must already be small enough. The two-sided pinching problem is genuinely more than "$\mathrm{Ric}<0$." Also correct is the observation that a connected-sum neck injects an $O(1)$ pointwise operator-norm Ricci error that global volume growth does not dilute; this is precisely why the $X_i\#X_i$ minus-sign branch is not defeated by the existing global inequalities and needs an actual construction with per-point defect tending to zero.

---

### (2) Reduction to $K_{\rm adj}^{AB}=\tfrac{1}{512}\int e^{s}A(s)B(s)\,ds$ — consistent with Step 91

The factorization is exact. Starting from the residual $m$-collapsed double series with $p_{\ell k}=\tfrac12(\mu_\ell+\mu_k)-1$ and using $e^{-\tau p}/p=\int_\tau^\infty e^{-sp}\,ds$,
$$K_\tau=\frac1{512}\int_\tau^\infty e^{s}\Big(\sum_\ell(2\ell+1)\mu_\ell e^{-s\mu_\ell/2}\Big)\Big(\sum_k(-1)^k(2k+1)\mu_k e^{-s\mu_k/2}\Big)ds=\frac1{512}\int_\tau^\infty e^s A(s)B(s)\,ds,$$
where the $e^{+s}$ is exactly the $-1$ in $p_{\ell k}$. Absolute convergence of the double series holds for $\tau>0$ ($\sim\ell^3k^3 e^{-\tau(\mu_\ell+\mu_k)/2}$), so the interchange is legitimate; the $\int_0^\infty$ form is the $\tau\to0$ limit, integrable at $s\to0$ ($A\sim s^{-2}$, $B$ exponentially small) and at $s\to\infty$ ($\sim e^{-s}$).

Two independent consistency checks confirm the normalization matches Step 91:

- The $\ell=k=1$ term is $\tfrac1{512}(-1)(3)(3)(2)(2)=-9/128=-0.0703125$, which is exactly the "axial (1,1,m=0)" limit quoted in Step 91 ($-0.0701$ at $\tau=0.003$, rising to $-9/128$).
- The overall constant is consistent with the Step 91 spectral prefactor: $\tfrac{\pi^2}{2}\cdot\tfrac1{16\pi^2}\cdot\tfrac1{16}=\tfrac1{512}$, where $1/(16\pi^2)$ is two spherical addition theorems and $1/16$ collects the receiver $\tfrac12$ factors. So $\tfrac{\pi^2}{2}$ (source-adjoint) and $\tfrac1{512}$ (heat-integral) are the same normalization.

The addition-theorem picture also explains the asymmetry between $A$ (no sign) and $B$ ($(-1)^k$): receiver NN=(N,N) and source NS=(N,S) coincide on factor A (so $P_{\ell_A}(1)=1$, giving $A>0$ termwise) and are antipodal on factor B (so $P_{\ell_B}(-1)=(-1)^{\ell_B}$, giving the $(-1)^k$). The opposite-corner pair NN↔SS is antipodal in both factors, hence $\tfrac1{512}\int e^s B(s)^2\,ds>0$; the JSON value $+0.01772676$ and its $\ell=k=1$ term $+9/128$ match this. So the sign structure across pairs is coherent.

I also verified the $m=2$ cancellation in the numerics: the four one-form types carry $m=2$ parts $(+P,-P,+P,-P)$ with common magnitude $P$ (e.g. $P=1.297$ at $\tau=0.003$) that sum to zero, leaving the $m=0$ coexact–coexact residual $-0.0314$ in the total. The residual coexact–coexact entry $=P-0.0314$ reproduces the tabulated $1.265$. This confirms the reduction numerically, though a written proof of the $m=2$ cancellation from the $2\times2$ Hessian/star matrices is still an open piece (the note itself lists it).

---

### (3) The sign $B(s)<0$ — true, but rests on an asserted theorem that is genuinely load-bearing

The identity $B(s)=-4\pi\,\partial_t p_t(\pi)\big|_{t=s/2}$ is correct: the round-$S^2$ scalar heat kernel gives $p_t(\pi)=\tfrac1{4\pi}\sum_{\ell\ge0}(2\ell+1)(-1)^\ell e^{-t\mu_\ell}$, and the $\ell=0$ term drops since $\mu_0=0$. So $B(s)<0$ is equivalent to $\partial_t p_t(\pi)>0$ for all $s>0$.

The note obtains this from "the heat kernel strictly decreases with distance from the source for every $t>0$; hence the antipode is the spatial minimum," then applies the parabolic minimum principle so that the minimal value is nondecreasing in time. The minimum-value-nondecreasing step is standard. The strict-radial-monotonicity step is **not** self-evident and is essential, not decorative: without it the argument does not go through. By axial symmetry the south pole is always a critical point, so $\partial_t p_t(\pi)=\Delta u(\text{south})=$ trace of the Hessian there. If the radial profile $u(t,\theta)$ developed an interior critical latitude at some intermediate $t$, the south pole could be a local maximum and $\Delta u(\text{south})<0$, i.e. $B(s)>0$. So the sign hinges entirely on the south pole being the true spatial minimum, which is exactly radial monotonicity. Termwise reasoning does not deliver it: $P_\ell'(\cos\theta)$ changes sign (e.g. $P_2'=3x<0$ for $x<0$), so the Legendre expansion of $u_\theta$ is not sign-definite term by term.

The statement is nonetheless **true**, and the missing proof is short. Let $w:=u_\theta$ on $(0,\pi)$. From $\partial_t u=u_{\theta\theta}+\cot\theta\,u_\theta$ one gets
$$\partial_t w=w_{\theta\theta}+\cot\theta\,w_\theta-\csc^2\theta\,w,$$
with $w(t,0)=w(t,\pi)=0$ (smoothness of the radial kernel at the poles) and zeroth-order coefficient $-\csc^2\theta\le-1<0$. For small $t_0>0$ the kernel is in its Gaussian regime and $w<0$ strictly on $(0,\pi)$. The absorption term $-\csc^2\theta\,w$ prevents $w$ from crossing $0$ from below (at an interior would-be positive maximum $w_{\theta\theta}\le0$, $w_\theta=0$, $-\csc^2\theta\,w<0$, so $\partial_t w<0$), and the endpoints stay $0$; the strong maximum principle gives $w<0$ on $(0,\pi)$ for all $t>t_0$. Hence $u$ is strictly decreasing in $\theta$, the antipode is the strict spatial minimum, its value strictly increases in $t$, and $B(s)<0$ for all $s>0$. (The singular endpoint coefficient is handled by working on $[\varepsilon,\pi-\varepsilon]$ and using $w<0$ on the compact interior; alternatively one may cite the known result that heat kernels on rank-one symmetric spaces are strictly decreasing in distance.)

Once $A>0$ termwise (immediate) and $B<0$ are in hand, the integrand $e^sA(s)B(s)<0$ and $K_{\rm adj}^{AB}<0$, magnitude $\approx-0.0314$, consistent with the ladder.

Separately: the JSON's finite-precision $B(s)$ samples at small $s$ (values $\sim10^{-12}$ with fluctuating sign flagged `finite_precision_B_sign_reliable: false`) are correctly not used for the sign. Direct alternating summation of $\sum(-1)^\ell(2\ell+1)\mu_\ell e^{-s\mu_\ell/2}$ has terms growing like $\ell^3$ with a true value that is exponentially small — catastrophic cancellation. The reliance on the analytic argument rather than these samples is the right handling. The samples at $s\ge0.2$ are reliably minus-signed and consistent.

**Net on (3):** the conclusion $B(s)<0$ is valid, but the write-up should include the $w=u_\theta$ maximum-principle proof (or an explicit citation) of $S^2$ heat-kernel radial monotonicity, since the sign of the whole AB adjacent coefficient depends on it.

---

### (4) What must be added before this touches the full Ozuch coefficient or Yau-26

The note's own list is accurate. In order of what actually changes the coefficient:

1. **Written proof of the $m=2$ polarization cancellation** from the $2\times2$ Hessian/star matrices, replacing the executable table. The numerics show the four one-form types' $m=2$ parts sum to zero, but the divergent parts grow as $\tau\to0$, so the cancellation must be exact and proved, not observed.
2. **Radial-monotonicity proof for $B<0$** (item (3) above).
3. **Source normalization from the actual Ozuch $H^4$ singular ALE tensor**, including the quotient isotropy factor and the symmetric-product no-averaging convention. Presently $\tfrac{\pi^2}{2}$/$\tfrac1{512}$ is internally consistent between the two representations but is a working normalization, not one derived from the true singular source; the physical size of the coefficient depends on this.
4. **AA/BB trace-free tensor sectors** with the electric/magnetic harmonic decomposition and the same K-odd receiver. The AB one-form sector is one of three; its sign alone does not determine the total.
5. **Bianchi/gauge projection** induced by the full source.
6. **Equality of adjacent ordered coefficients** in the transported node frames, so the four surviving adjacent pairs genuinely reduce to one $K_{\rm adj}$.
7. **Heat-tail estimates** for the differentiated pairings and convergence of the $\int_0^\infty$ representation with the actual source.
8. **Matching to the $t_i\lambda_i+t_i^2\mu_i$ radial expansion at order $t_it_j^2$** with error below the cubic layer.

Beyond the coefficient itself, two structural points bound what a result here could mean. First, a nonzero adjacent coefficient obstructs only the chosen symmetric desingularization branch of the specific product orbifold $(S^2\times S^2)/\mathbb Z_2$ with four $A_1$ points; it does not exclude other Einstein metrics on the underlying smooth 4-manifold, so it is a statement about one gluing ansatz, not about the smooth manifold's Einstein moduli. Second, this route is four-dimensional and addresses only the $\lambda>0$ construction side, so even a complete coefficient theorem is one input to the $n=4$ picture, not the dimension-uniform statement Yau-26 asks for.

On the route comparison itself: the assessment that X#X supplies the cleanest all-sign no-Einstein manifolds but needs a construction of $X_i\#X_i$ metrics with maximal defect $\to0$ (or a theorem forbidding such decay), while the product-orbifold branch currently carries the one tractable new computation, is supported by the algebra above. The BCG–CGB margin is genuinely of order $1/(4\chi)$ and genuinely target-size dependent; nothing in the present material closes the varying-target uniform margin $\Gamma>1$ of Step 47 §5.

---

**One correction to wording, no correction to mathematics.** The phrase "only the $m=0$ coexact–coexact double series remains" is exact for the residual after $m=2$ cancellation, but the surviving $(2\ell+1)(2k+1)$ degeneracy is not an $m=0$-only artifact — it is the full $\ell$- and $k$-shell collapsed by the spherical addition theorem (coincident factor $\to P_\ell(1)=1$, antipodal factor $\to P_k(-1)=(-1)^k$). Stating it that way makes the origin of the degeneracy and of the $(-1)^k$ transparent and pre-empts a reader's worry about where the shell sums went.