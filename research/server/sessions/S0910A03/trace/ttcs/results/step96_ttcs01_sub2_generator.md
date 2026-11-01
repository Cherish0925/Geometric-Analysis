# TTCS Independent Branch Record

```json
{
  "step_id": 96,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/notes/step95_KX_and_bochner_cancellation.md",
    "Sessions/S0910A03/workspace/notes/step92_tubular_collar_equations_seed.md",
    "Sessions/S0910A03/workspace/scripts/step94_charged_koiso_separator.py",
    "Sessions/S0910A03/workspace/data/step96_initial_taylor_invariants.json",
    "Sessions/S0910A03/workspace/data/step96_koiso_einstein_cauchy_evolution_N96_short.json",
    "Sessions/S0910A03/workspace/data/step96_relative_KX_diagnostic.json",
    "Sessions/S0910A02/workspace/notes/step83_near_pinched_construction_and_frontier_reduction.md"
  ]
}
```

## Task

Develop a high-value next mathematical construction from the exact charged Koiso center and the verified horizontal Noether/K_X pairing. The goal is a genuinely two-variable, shared-parameter joint matching formulation that can decide whether local Ricci flexibility extends to two expanded ends. Use the provided exact Cauchy data, quotient equations, and short Taylor/numerical evidence. Propose an explicit gauge-fixed unknown space, boundary data, residual/matching map including all Ricci blocks and two ends, and independent adjoint projections (not rearrangements of the area equation). Seek either a low-cost near-kernel analogous to log-Weyl slow interpolation or a finite projection that cannot vanish. Keep flat radial T3 models excluded; do not assume transition length or an interface. Derive as much of the linearized principal operator and dimension/index structure as possible, and specify a decisive computation/proof that could be done next.

## Output

## Reframing the target: what the exact charged center is really a piece of

Your reduced fields on the two-dimensional orbit space $B=(n,s)$, $s\in S^1$, with $T^2$ fiber $x^a$, are exactly the data of a **2D dilaton–gravity coupled to a sigma model into a solvable homogeneous target with a $\lambda$-potential.** Collecting the verified pieces, the natural target is

$$
\mathcal N=\mathbb R_\sigma\times\mathbb H^2_{(\alpha,\zeta)}\times\mathbb R^2_{q},
\qquad
ds^2_{\mathcal N}=d\sigma^2+\tfrac14|M^{-1}dM|^2+e^{-3\sigma}M^{-1}_{ab}\,dq_a\,dq_b ,
$$

whose twist block is precisely your $A=e^{-3\sigma}M^{-1}$ (so $Q=\tfrac12 q^TA q$ is the twist kinetic density), with base measure $d\mu_\sigma=\rho\,dV_B=e^\sigma dV_B$ and the potential fixed by $\lambda=-3$. This is the correct gauge-fixed unknown space: conformal base $\gamma_B=e^{2\phi}(dn^2+ds^2)$ with $\phi$ determined by the Hamiltonian/momentum constraints (2D dilaton–gravity: $\phi$ is not an independent elliptic wave), fiber gauge $\det M=1$, and the twist represented by the two scalars $q_a$ obtained by dualizing the connection one-forms. The OT locus $\{q=0\}$ is a **totally geodesic wall** $\mathcal N_0=\mathbb R_\sigma\times\mathbb H^2$ (fixed by $q\to-q$), because $q$ enters purely quadratically. Your exact charged Koiso center is a single interior map point lying off this wall; the two OT ends are required to lie on it. The whole matching problem is: *does a coupled harmonic-map-with-potential $U:B\to\mathcal N$, solving all Ricci blocks, leave the wall in the interior while both ends return to it, on a closed base?* Shared-parameter matching data are the two end moduli (points of $\mathbb H^2$ and the Koiso circle speed $12+2S$) plus the collapse-flux data below; the residual map is $\mathcal E=(H,T,Z,dq_{\mathrm{src}})$.

## Possibility A — the drift-integral balance forbids a free two-end cylinder and forces collapse caps

This is the strongest and cheapest decisive object, and it does not use any transition length, interface, or radial reduction. Using **only** your verified area equation $L\sigma=6+Q$ with $L=\rho^{-1}\operatorname{div}(\rho\nabla\cdot)$ (which is an identity because $\log\rho=\sigma$), integrate against $d\mu_\sigma$ over the orbit space:

$$
\int_B(6+Q)\,d\mu_\sigma=\int_B L\sigma\,\rho\,dV_B=\int_B\operatorname{div}(\rho\nabla\sigma)\,dV_B
=\oint_{\text{edge}}\rho\,\partial_\nu\sigma\,d\ell .
$$

If the $T^2$ action is free (the genuinely free cylindrical two-end target of Step 95 §6), then $B$ is a *closed* surface with no edge, $\rho>0$ everywhere, and the right side is $0$. But $6+Q\ge 6>0$, so the left side is $\ge 6\,\mathrm{vol}_\sigma(B)>0$: **contradiction.** Hence:

- No closed 4-manifold with a *free* $T^2$ action carries an exactly $\lambda=-3$, $T^2$-invariant Einstein metric of this reduced type. (This is the metric-level shadow of Bochner's theorem: a closed $\lambda<0$ Einstein manifold has finite isometry group, so cannot admit the continuous $T^2$ symmetry at all.)
- For a near-Einstein input, $T=L\sigma-6-Q$ is a trace component of the defect, $|T|\le c\,\|E\|_{\mathrm{op}}\le c\delta$ pointwise. On a free (edgeless) closed base, $\int_B(6+Q)\,d\mu_\sigma=\int_B T\,d\mu_\sigma\le c\delta\,\mathrm{vol}_\sigma$, forcing $\delta\ge 6/c$. A genuinely small-defect free-cylinder connector **does not exist**.

The consequence is structural: any closed $\lambda=-3$ $T^2$-symmetric near-Einstein connector must have **collapse strata** (nuts/bolts where a fiber circle degenerates), which supply the edge flux. These are exactly the disk-cap models you have treated as adverse benchmarks. So the two "expanded ends" are not free cusps to be joined; they must terminate in collapse, and the free-cylinder target is empty. Note the sign branch dependence: the constant is $-2\lambda$, so this obstruction is special to $\lambda<0$; for $\lambda>0$ the constant flips sign, $Q\ge0$ can balance it, and free $T^2$ symmetry is consistent (Page-type geometries). This cleanly separates the two normalized branches and removes flat/nil $T^3$ free-action models from contention at $\lambda=-3$.

The same identity used as a finite projection cannot be defeated by redshift, because it is an equality tied to the fixed-point data rather than a pointwise transport estimate. Evaluated at a bolt of orbit-space length $L_{\rm bolt}$ with $\rho\sim r$, $\sigma\sim\log r$, the edge flux is $\sim L_{\rm bolt}$, giving the exact bound

$$
\int_B Q\,d\mu_\sigma \;=\;\Phi_{\rm total}-6\,\mathrm{vol}_\sigma-\int_B T\,d\mu_\sigma
\;\le\;\Phi_{\rm total}+c\delta\,\mathrm{vol}_\sigma,
\qquad \Phi_{\rm total}\sim\textstyle\sum L_{\rm bolt}.
$$

Because $Q\,d\mu_\sigma=e^{-2\sigma}\cdot\tfrac12 q^TM^{-1}q\,dV_B$ weights the *collapse* regions (small $\sigma$) heavily, finiteness of the left side forces a definite decay rate of $Q$ toward each bolt; near a bolt the integrand is $\sim q_{\rm phys}\,r^{-1}dr$, so $Q$ must vanish at collapse at a controlled rate. This is a real, redshift-proof control on charge exactly where $\sup Q$ lives. **Decisive computation:** compute $\Phi_{\rm total}$ from the nut/bolt data for each candidate closed topology (equivariant localization of the $T^2$ action determines the flux from fixed-point weights), then test whether $\Phi_{\rm total}$ combined with the separator floor $\langle e_s\rangle_\Sigma\ge 12-8\delta+2Q_C$ leaves room for an order-one $Q_C$ at the separator.

## Possibility B — the transverse twist operator: charge is intrinsically nonlinear, and one number decides everything

Linearize $\mathcal E$ about an exact OT reference on the wall $\{q=0\}$. Because $q$ enters every block quadratically, the transverse (twist) equation decouples at linear order to the pure divergence-form operator with **no zeroth-order term**:

$$
\mathcal L_q\,q\;:=\;\rho^{-1}\operatorname{div}(\rho\,A_0\nabla q)=\text{(source)},\qquad
A_0=e^{-3\sigma_0}M_0^{-1}>0 .
$$

With $q=0$ on both ends, the homogeneous operator has trivial kernel by the energy identity $\int\rho\,A_0\nabla q\!\cdot\!\nabla q=0\Rightarrow q\equiv0$. So charge cannot be switched on at linear order — it is genuinely nonlinear, sourced only through the mixed-Ricci defect $\operatorname{div}_\sigma(A_0\nabla q)=2\rho\,E_{\rm mix}$ at order $\delta$. Everything then turns on the **operator norm of the solution map** $G:\ \text{source}\mapsto q$ with zero end data:

$$
\|q\|\le \|G\|\cdot\|E_{\rm mix}\|,\qquad Q_+\lesssim \|G\|^2\delta^2 .
$$

If $\|G\|$ is bounded independent of the connector geometry, then $Q_+=O(\delta^2)$, the OT resolvent obstruction ($\delta<0.246$, $q=0$) applies to leading order, and the charged connector is obstructed — closing this refutation route at $\lambda=-3$. If $\|G\|$ grows without bound, order-one charge is reachable and the construction side is open.

Your redshift-taper (Step 94 §6) is exactly the Rayleigh quotient of $\mathcal L_q$ in the *area-only truncation*: $\int w^2\rho/\int b^2\rho\sim e^{2\sqrt6 R}$ shows the truncated $\|G\|$ grows exponentially in plateau size. But that truncation froze $M=I$, violating the orbit equation $Z=0$, and used a noncompact geometry. The decisive object is the **full coupled** transverse operator with the orbit and base blocks restored and the area balance of Possibility A enforced. The full linearized principal operator, modulo the 2D diffeomorphism gauge (two functions) and the constrained $\phi$, is block-elliptic:

$$
D\mathcal E=\begin{pmatrix}
\Delta_\sigma+\cdots & \ast & 0\\
\ast & \Delta_U^{\mathbb H^2}+\cdots & 0\\
0 & 0 & \mathcal L_q
\end{pmatrix}
$$

on $(\dot\sigma,\dot U,\dot q)$, the top-left $3\times3$ block second-order elliptic with drift $\sigma$, the twist block $\mathcal L_q$ a $2\times2$ system of the divergence type above. Because $q$ couples back only at second order, the twist eigenproblem $\mathcal L_q\psi=\mu\,\rho\,A_0\psi$ (Dirichlet on the ends) is self-contained; its lowest eigenvalue $\mu_1$ on the closed collapse-strata orbit space, as a function of the geometry, is the number that decides the dichotomy. **Decisive computation:** solve this 2D generalized eigenproblem on the actual orbit surface (two local $\sigma$-maxima separated by the stable separator, terminating in bolts), with the area balance imposed, and determine whether $\mu_1$ is bounded below or decays as the separator/plateau lengthens. The redshift growth is the enemy; the orbit equation and the collapse-forced weighting $e^{-2\sigma}$ are the sources of a possible floor. This is the genuinely two-variable version of the constant-$Q$ Step 89 analysis and supersedes the 1D transport picture.

## Possibility C — independent adjoint moments that are not the area equation

The horizontal Noether identity (8.6) is the right two-dimensional pairing, but Step 95 §3 shows testing it against $\nabla\sigma$ reproduces the area equation. Genuinely independent projections come from adjoint fields tied to the closed orbit-space symmetry and the $s$-direction, not to $\sigma$:

1. **$s$-momentum adjoint $X=f(n)\,\partial_s$.** On an $s$-symmetric reference $\partial_s$ is Killing, so $\operatorname{sym}\nabla(\partial_s)=0$ and the $H$-term drops; the identity reduces to a pairing of the $s$-flux of the charge-work against the $Z$-block along the orbit map. This isolates the *second* charge moment (the $s$-variation) that total-flux conditions (4.4)–(4.5) miss, and it is precisely the object the redshift-taper cannot address because that benchmark is $s$-independent.
2. **Conformal adjoint $X=\Xi$, the conformal Killing field of the cylinder.** This probes the scale invariance broken by the $\lambda$-potential; its moment couples $\operatorname{tr}H$ and $T$ to the charge-work and, unlike $\nabla\sigma$, is not proportional to the area equation.
3. **Collapse-anchored adjoint.** Choose $X$ vanishing at both ends but with prescribed unit flux linking the two bolts; its moment is a capacity between the collapse strata, which the closed topology bounds from below independent of connector length — the ingredient the noncompact interval model lacked.

The program: exhibit a finite family $\{X_j\}$ for which the moments $\int m_q(X_j)\,d\mu_\sigma$ are simultaneously (i) bounded below by a positive function of $Q_+$ (charge must do work against these adjoints), and (ii) bounded above by $C\delta$ through the right sides of (8.6). Incompatibility for order-one $Q_+$ and small $\delta$ is the finite projection that cannot vanish. A single adjoint is defeatable by redshift (Step 94 §6); the closed topology and the $s$-momentum moment are what a defeating construction must also cancel, and satisfying all of (4.4), the $s$-momentum moment, and the capacity moment simultaneously with every Ricci block $\to0$ is the concrete construction target if the obstruction does not close.

## What to compute next, in order of decisiveness

The cheapest decisive step is Possibility A made quantitative: compute $\Phi_{\rm total}$ from the fixed-point weights for the specific candidate closed $T^2$-manifolds you are targeting, and check the balance $\int Q\,d\mu_\sigma\le\Phi_{\rm total}+c\delta\,\mathrm{vol}_\sigma$ against the separator floor and the near-collapse decay rate it forces on $Q$. This alone may show the free-cylinder target is empty and that only collapse-cap configurations survive, redirecting the entire refutation attempt onto the disk-cap regime you already know is adverse.

The single number that then settles the surviving regime is $\mu_1(\mathcal L_q)$ of Possibility B on the actual 2D orbit surface with the area balance imposed. A bounded-below $\mu_1$ gives $Q_+=O(\delta^2)$ and restores the OT obstruction with charge; a decaying $\mu_1$ localizes a slow transverse twist mode (the exact analog of the log-Weyl slow interpolation in the 4D orbifold construction) and hands you an explicit construction direction. I would build the reference from your exact charged Koiso center pushed to the wall ($q\to0$) as the interior seed and the exact OT cusp as the end data, solve the generalized eigenproblem numerically on the surface for a family of separator lengths, and fit $\mu_1$ against length; the redshift exponent $2\sqrt6$ is the value to beat, and whether the orbit block lifts $\mu_1$ above the truncated value is the whole question.

Two things to keep clearly separated in this: the source $2\rho E_{\rm mix}$ is $O(\delta)$ only pointwise, so the eigenproblem must be run with the true $A_0$ from a genuine two-max/one-saddle $\sigma$-profile, not a plateau; and the closed-topology weighting $e^{-2\sigma}$ near bolts should be included, since it is the mechanism that could convert the exponential redshift advantage into a finite floor. If both A and B leave order-one charge alive, the adjoint family of C is the finite projection to attack; if that too admits a distributed sign-changing charge satisfying every moment, you have a concrete blueprint for the near-Einstein charged connector and the refutation shifts entirely to proving the underlying closed manifold carries no Einstein metric of any sign.