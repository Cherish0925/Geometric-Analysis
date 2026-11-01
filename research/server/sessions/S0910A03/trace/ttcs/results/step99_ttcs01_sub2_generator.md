# TTCS Independent Branch Record

```json
{
  "step_id": 99,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step96_charged_koiso_local_evolution_and_joint_matching.md",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md",
    "Sessions/S0910A03/workspace/plans/step98_route_map.md"
  ]
}
```

## Task

Given the cost structure of the free-T² connector for Yau Problem 26:

1. Normal cost: bounded below by Raychaudhuri floor δ_min(R) ~ 12e^{-2R}
2. Tangential cost: conformal expansion gives 9.94·sech²(r) for the charged separator orbit shape
3. The exact Einstein germ (Koiso) has zero cost but is only defined locally

The critical unknown is the continuation domain of the exact Einstein germ from the charged Koiso center. If it extends to r = r₁, the best trial metric could achieve operator norm ~ max(δ_min(R), 9.94·sech²(r₁)) for a total cylinder of length R.

PROPOSE concrete mathematical strategies for either:
(A) Establishing that the Koiso germ has finite maximal continuation radius r_max, and estimating r_max from the data (S=1, Qmax=0.5, scalar curvature -7, orbit energy concentrated with von Mises parameter 800).
(B) Proving that the tangential cost cannot be made arbitrarily small by any trial (i.e., a genuine tangential obstruction).
(C) A completely different construction strategy that bypasses the Koiso center + expanding exterior framework.

The context includes the full development history of the free-T² connector problem over 96+ steps, including the Bochner/resolvent obstruction for exact OT connectors, the flat-slice barrier, and the charged Koiso separator construction.

## Output

## The central reframing: the operator-norm floor is a Chern–Gauss–Bonnet identity, not a continuation artifact

Before separating (A)/(B)/(C), there is one structural fact that reorganizes all three and, in the free‑T² class, essentially resolves (B) in closed form. A free T²-action with 2‑dimensional orbit space makes M⁴ a T²-bundle over a surface, so

$$
\chi(M)=\chi(T^2)\,\chi(\Sigma)=0 .
$$

For any smooth metric on a closed oriented 4‑manifold,

$$
\chi(M)=\frac{1}{8\pi^2}\int_M\Big(|W|^2+\tfrac{1}{24}s^2-\tfrac12|\mathring{\mathrm{Ric}}|^2\Big)\,dV .
$$

With $\chi=0$ this is an exact identity, not an inequality:

$$
\boxed{\ \int_M|\mathring{\mathrm{Ric}}|^2\,dV \;=\; 2\int_M|W|^2\,dV+\tfrac{1}{12}\int_M s^2\,dV\ }\tag{$\star$}
$$

Now feed in a pinching band. If the Ricci eigenvalues lie pointwise in $[c,C]$, then $s\in[4c,4C]$ and the trace‑free part obeys $|\mathring{\mathrm{Ric}}|^2\le 4(C-c)^2$ (four eigenvalues, mean zero, each of size $\le C-c$; the value $4(C-c)^2$ is attained by $(+w,+w,-w,-w)$). If the band avoids zero, say $C<0$, then $s^2\ge 16C^2$. Substituting into $(\star)$,

$$
4(C-c)^2\,\mathrm{Vol}\;\ge\;\int|\mathring{\mathrm{Ric}}|^2\;\ge\;\tfrac{1}{12}\int s^2\;\ge\;\tfrac{4C^2}{3}\,\mathrm{Vol},
$$

so

$$
\boxed{\ C-c\ \ge\ \frac{|C|}{\sqrt3}\ }\qquad\text{(free-}T^2,\ \text{non-flat, band below }0).
$$

This is a rigorous, construction-independent lower bound on the pinching width. Around $C\approx-3$ it forces $c\lesssim-4.73$, i.e. a width $\gtrsim\sqrt3\approx1.73$ in Ricci eigenvalues; converted to the generalized operator norm of $\mathrm{Ric}+3g$ this is an order‑unity floor, and the $\int|W|^2$ term of the *specific* T²-bundle geometry only raises it. Computing $\int|W|^2$ for the actual H²×T²-type asymptotic model (a short calculation on the warped orbit metric) will pin the constant and should reproduce the numerically observed several-unit floor. In other words: **the "operator norm $\sim5$" the connector keeps hitting is the Euler-characteristic identity $(\star)$ speaking, not a weakness of any one trial.**

The same identity converts the "how far does the exact germ continue?" question into global accounting. Split $M$ into the exactly-Einstein germ region $G$ (where $\mathring{\mathrm{Ric}}=0$) and the rest $N$. Then $\int_G(|W|^2+s^2/24)+\int_N(|W|^2+s^2/24-|\mathring{\mathrm{Ric}}|^2/2)=0$ gives

$$
\int_N|\mathring{\mathrm{Ric}}|^2 \;\ge\; \tfrac{1}{12}\!\int_G s^2 \;\approx\; \tfrac{144}{12}\,\mathrm{Vol}(G)=12\,\mathrm{Vol}(G).
$$

A *larger* zero-defect germ forces a *larger* defect integral on the transition. The exact-germ region does not buy small defect; it pushes the deficit into the collar. This is the clean reason $\max(\delta_{\min}(R),\,9.94\,\mathrm{sech}^2 r_1)$ cannot be driven to zero on a $\chi=0$ manifold regardless of $r_{\max}$.

## (A) Finite $r_{\max}$ via directional focusing, with the charge accelerating rather than resisting collapse

The exact analytic germ terminates when a slice geometry degenerates. Track the base-circle scale $a(n,s)$ in $q=a^2ds^2+G_{ab}(\dots)$. The shape operator $W=q^{-1}K$ satisfies the matrix Riccati coming from Ric $=-3g$,

$$
\partial_n W + W^2 = -R_\nu,\qquad (R_\nu)^i{}_j:=R^i{}_{\ \nu j\nu},
$$

whose trace is the Raychaudhuri equation $\partial_n H=3-|W|^2$ (consistent with the center value $H_n=3-S=2$). Projecting on the $s$-direction and writing $\theta_s=\partial_n\log a$,

$$
\partial_n\theta_s+\theta_s^2+(\text{off-diagonal }W^2\ge0)=-R(\nu,e_s,\nu,e_s).
$$

The center data already fix the sign: $a_{nn}=-3-S-Q$ gives $\partial_n\theta_s|_0=-(3+S+Q)<0$, i.e.

$$
R(\nu,e_s,\nu,e_s)\big|_0=3+S+Q>0.
$$

So the plane spanned by the normal and the base circle carries **positive** sectional curvature even though $g$ is Einstein with $\lambda=-3$ (the orbit planes are strongly curved below zero, $\sigma_{nn}=6+Q$, to compensate). Positive sectional curvature focuses: $a\to0$ in finite normal distance, an $s$-circle pinch. Crucially the charge enters the focusing term with a $+Q$ sign — it does **not** act as a centrifugal barrier; it hastens the pinch. There is no rotational escape here, contrary to the intuition that a magnetic twist should hold the circle open.

Quantitatively, since $W^2\succeq\theta_s^2$ (off-diagonal squares are $\ge0$) and $R(\nu,e_s,\nu,e_s)\ge k_\ast>0$ along the germ,

$$
\partial_n\theta_s\le-\theta_s^2-k_\ast\ \Rightarrow\ \theta_s\le-\sqrt{k_\ast}\tan(\sqrt{k_\ast}\,n),\qquad a\to0\ \text{at}\ n_\ast\le\frac{\pi}{2\sqrt{k_\ast}} .
$$

With $k_\ast\gtrsim 3+S\approx4$ this gives $r_{\max}\lesssim \pi/4\approx0.78$ for spread data. The one analytic input needed to make this a theorem is a uniform lower bound $R(\nu,e_s,\nu,e_s)\ge k_\ast>0$ along the germ; it can be produced by integrating the reduced $(\sigma,U,A)$ sigma-model equations (which are numerically well-behaved, unlike the ill-posed Cauchy form) and verifying the sign, then closing with a Sturm comparison. The existing short evolution already shows $\lambda_{\min}(q)$ falling from $O(1)$ to $0.127$ by $n=0.02$, which is exactly the rapid slice-collapse signature and independently suggests $r_{\max}$ is short for the concentrated data.

For the highly concentrated data (von Mises $\kappa=800$, spike width $\ell\sim\kappa^{-1/2}\approx0.035$), the analytic continuation radius is controlled by the data length scale through a Cauchy–Kovalevskaya majorant, giving $r_{\max}=O(\ell)\approx0.03$–$0.1$. Then $\mathrm{sech}^2(r_{\max})\approx1$ and the tangential cost stays $\approx9.9$. So concentration is self-defeating: it makes the germ die almost immediately. The clean statement to prove and report: $r_{\max}=O(\min(1,\ell_{\text{data}}))$, hence $9.94\,\mathrm{sech}^2(r_{\max})$ never falls below $\sim5$.

A distinct outcome deserves separate treatment. If at $a\to0$ the $s$-circle degenerates *smoothly* (a bolt/nut of the T²-action), the germ caps off into a closed piece — but then the T²-action is no longer free, $\chi$ picks up contributions from the fixed set, and the object may simply be (part of) a genuine Einstein metric rather than a connector. The distinguishing computation is the holonomy/period condition at $a=0$: a smooth cap requires the collapsing circle's length to close at rate $a\sim(\text{const})\,(n_\ast-n)$ with the correct $2\pi$ normalization of the residual angle; a mismatch gives a cone/curvature blow-up and no continuation. Either way the germ does not reach an infinite expanding end.

## (B) The genuine tangential obstruction, and why the integral form is not enough by itself

$(\star)$ already gives the strongest form of (B) for the free-T² class: a positive, closed-form lower bound on the defect that no trial can beat. I want to add the second, softer mechanism because it clarifies what the sech²-profile really encodes and where the sup-norm floor (as opposed to an integral floor) comes from.

Consider the reduced harmonic-map-with-potential system on the cylinder $\Omega=\mathbb R_r\times S^1_s$: $\tau_\sigma(U)=-\nabla_U Q+E$, with $U:\Omega\to\mathbb H^2$ and potential $Q=\tfrac12 c^\top e^{-3\sigma}M^{-1}c$. Pair the tension with the translation field $\partial_r$ to form the stress component $T_{rr}=|U_r|^2-|U_s|^2-2Q$. If $E\equiv0$, $\partial_r\!\int_{S^1}T_{rr}\,ds=0$, so the flux is constant. At a symmetric center $U_r=0$: $T_{rr}=-|U_s|^2-2Q<0$. At a charge-free expanding end: $U_r,U_s,Q\to0$, so $T_{rr}\to0$. These cannot both hold with constant flux, hence

$$
\int_\Omega\big\langle E,\ \text{(dilation field)}\big\rangle \;\ge\; |U_s|^2_{\text{center}}+2Q_{\text{center}}\;>\;0 .
$$

This is a Pohozaev/virial reincarnation of the earlier Bochner–resolvent statement that no exact charged connector exists. But it is only an *integral* lower bound: spread over a cylinder of length $R$ it permits $\sup|E|\sim(\text{const})/R\to0$. Therefore the pointwise floor cannot come from Pohozaev alone — it must come from the fact that the relaxation of orbit shape and charge cannot be spread adiabatically. That rigidity is the indicial/mass-gap structure at the ends: the linearized operator about the charge-free expanding end has indicial roots pinned by the $e^{-3\sigma},e^{-6\sigma}$ decays of $q$ and $Q$, so the transition is confined to an $O(1)$ region and produces the fixed-width $9.94\,\mathrm{sech}^2 r$ profile rather than a spreadable ramp. The decisive computation, still open per Step 96 §7, is exactly the indicial exponents and the smallest singular value of the compactified linearization as $R\to\infty$: convergence to a positive value with a bounded left field of nonzero center pairing is the sup-norm floor; exponential decay with a left field escaping to infinity would be the redshift channel that $(\star)$ says cannot exist in the $\chi=0$ class. The two analyses should agree, and that agreement is itself a strong cross-check.

## (C) Constructions that leave the Koiso-center-plus-expanding-exterior frame

**(C-main) Target the topology directly; make the Einstein deficit the object of study.** $(\star)$ says $\chi=0$ manifolds carry a hard width floor, so they can only ever defeat *wide* pinching bands, never narrow ones. This is a ceiling on the entire free-T² program: even a perfect connector would refute Yau 26 only for bands of width $\gtrsim|C|/\sqrt3$, leaving every narrow band untouched. The manifolds that could defeat narrow bands must have $\chi\neq0$ and must be non-Einstein for a *finer* reason than Hitchin–Thorpe. Note the parallel Chern–Gauss–Bonnet computation shows narrow pinching near a nonzero $\lambda$ forces $2\chi\ge3|\tau|$ (the $s^2/24-|\mathring{\mathrm{Ric}}|^2/2$ integrand becomes positive), so Hitchin–Thorpe violators cannot even carry narrowly-pinched metrics — they are the wrong target. The right targets are LeBrun's Seiberg–Witten–obstructed 4-manifolds: they satisfy Hitchin–Thorpe yet admit no Einstein metric. For these, LeBrun's sharp curvature inequalities (of the form $\int(s-\sqrt6\,|W^+|)^2\ge 72\pi^2(c_1^+)^2$ and the Weyl/scalar refinements of $2\chi\pm3\tau$) give a *positive* lower bound on $\int|\mathring{\mathrm{Ric}}|^2$, i.e. a per-manifold Einstein deficit

$$
\mathfrak E(M)=\inf_g\ \frac{\sup_M|\mathring{\mathrm{Ric}}|_g}{\ |s|_g\ }\ >\ 0 .
$$

Yau 26 in dimension four is then equivalent to a single extremal question: **is $\inf_{M\ \text{non-Einstein}}\mathfrak E(M)>0$?** If the SW-based lower bounds on $\mathfrak E$ stay bounded away from zero along every family of SW-obstructed manifolds, Yau 26 holds in dim 4 (for a suitable band); if some family has $\mathfrak E(M_k)\to0$, it fails. This is a far more decisive formulation than germ continuation, and it points computation at concrete objects (blow-ups of surfaces of general type, connected sums with controlled SW basic classes) with explicit $c_1^2,\chi,\tau$.

**(C-alt) Cohomogeneity-one / Bianchi phase space instead of a two-ended sigma model.** Replace the T²-over-surface reduction by a cohomogeneity-one Ansatz (Böhm, Wang–Ziller): the Einstein condition becomes a finite-dimensional ODE flow on the space of principal-orbit shape parameters, and the pinching band $c_n g\le\mathrm{Ric}\le C_n g$ becomes an explicit region $\mathcal P$ in that phase space. The disproof question becomes: is there a bounded orbit of the reduced flow that stays in $\mathcal P$ for all time (or connects two smooth caps) without being a fixed point (=Einstein)? This is a concrete, low-cost dynamical-systems search with rigorous interval-arithmetic verification available, and it entirely sidesteps the ill-posed Cauchy continuation. It also tests the flexibility-versus-rigidity heart of the problem in a setting where the whole solution, not just a germ, is under control.

**(C-context) Flexibility-versus-rigidity is the real axis.** Lohkamp's theorem gives complete freedom for one-sided Ric<0; Yau 26 asks whether *two-sided narrow* pinching near a constant is rigid enough to force Einstein existence. $(\star)$ and the deficit functional show the answer is topology-dependent: it is rigid on $\chi=0$ (width floor) and on Hitchin–Thorpe violators (no narrow pinch at all), and the open question lives precisely on SW-obstructed manifolds. Framing the whole session this way — Lohkamp flexibility on one side, LeBrun deficit rigidity on the other, with Yau 26 as the extremal value of $\mathfrak E$ — is what turns the accumulated connector data into a statement about the actual problem.

## Sources to pull (named topics, not invented citations)

Chern–Gauss–Bonnet and signature integrands with the exact $\tfrac1{24}s^2-\tfrac12|\mathring{\mathrm{Ric}}|^2+|W|^2$ normalization (Besse, *Einstein Manifolds*, curvature-functional chapter); Hitchin–Thorpe inequality and its equality/rigidity case; LeBrun's Seiberg–Witten obstructions to Einstein metrics and his sharp $\int s^2$, $\int(s-\sqrt6|W^+|)^2$ curvature bounds (the "four-manifolds without Einstein metrics" and "Ricci curvature, minimal volumes, SW theory" families); Lohkamp's flexibility for Ric<0; Böhm and Wang–Ziller cohomogeneity-one Einstein ODE systems; Anderson's and Cheeger–Tian's $L^2$-curvature/ε-regularity theory for the deficit estimates; and the harmonic-map-with-potential Pohozaev/stress-energy identities on cylinders for the tangential virial statement.

The one calculation that would most change the picture immediately: evaluate $\int|W|^2$ and $c_1^2,\chi,\tau$ for the explicit T²-bundle model underlying the connector, insert into $(\star)$ and the LeBrun bounds, and compare the resulting closed-form defect floor against the numerical $5$ and $9.94$. If they match, the "operator norm floor" is proven topological and the free-T² route's ceiling is established analytically rather than empirically.