# TTCS Independent Branch Record

```json
{
  "step_id": 72,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/data/step72_conformal_gauge_system.json",
    "Sessions/S0910A03/workspace/data/step72_structural_analysis.json",
    "Sessions/S0910A03/workspace/notes/step70_critical_identity_and_corrections.md",
    "Sessions/S0910A03/workspace/notes/step69_anisotropic_cusp_compensation.md"
  ]
}
```

## Task

Verify the following structural properties of the T²-invariant Einstein system in conformal gauge on [0,R]×S¹.

Metric: g = e^{2φ}(dt²+dz²) + e^{2b}dx² + e^{2c}dy², where (t,z) is the base 2D plane (z periodic), and x,y are T² quotient directions.

Claim 1 (Anisotropy drift-Laplacian): For exact Ric+3g=0, the difference δ=b-c satisfies Δδ + ∇σ·∇δ = 0 where σ=b+c and Δ,∇ are the flat 2D operators on (t,z). This follows from subtracting the xx and yy Einstein equations.

Claim 2 (Maximum principle): On the domain [0,R]×S¹ with reflection conditions δ_t(0,z)=0, the strong maximum principle and Hopf lemma force: either δ is constant, or max_z δ(R,z) ≥ max_z δ(0,z) and min_z δ(R,z) ≤ min_z δ(0,z). The oscillation of the T² anisotropy at the outer boundary is at least as large as at the center.

Claim 3 (Orbit-area equation): Setting ρ=e^{b+c}, the orbit area satisfies Δ_flat(ρ) = (6e^{2φ} - |∇δ|²)·ρ. For isotropic solutions (δ=0), ρ is strictly subharmonic.

Claim 4 (Isotropic impossibility): For isotropic g=dt²+f²h on T³ (3D fiber), the normal Einstein equation gives s'+s²=1 while the tangential gives s'+3s²=3, where s=f'/f. These are algebraically inconsistent with s(0)=0.

Claim 5 (Forced compatibility): For approximate Einstein with |Ric+3g|_op ≤ δ on T³ outer boundary in flat conformal class, the Gauss equation forces δ ≥ (9-H²)/6 where H is mean curvature. Combined with the interior weighted identity (δ ≥ Ce^{-2R} from the normal balance), the constraints are compatible: take H=3-ε, δ~ε, R~(1/2)log(6/ε).

For each claim: (a) verify the derivation, (b) check whether the maximum principle argument is correct for the Neumann boundary at t=0, (c) identify whether the anisotropy preservation BLOCKS cusp matching or merely CONSTRAINS it.

Key question: Does the drift-Laplacian δ equation prevent the construction of approximate Einstein metrics on graph manifolds with Koiso centers? Or does the anisotropy propagation to the boundary merely require matching to an anisotropic cusp (which is what the lattice quotient construction provides)?

## Output

## Verifier Memo — T²-invariant Einstein system in conformal gauge on [0,R]×S¹

I recomputed each derivation from the raw component data in `step72_conformal_gauge_system.json` and cross-checked the reduction algebra. The dimension bookkeeping first: the metric $g=e^{2\phi}(dt^2+dz^2)+e^{2b}dx^2+e^{2c}dy^2$ is a **4-manifold** with $T^2$ orbit $(x,y)$, 2-plane base $(t,z)$, $z$ periodic. The slice $\{t=\text{const}\}$ is $S^1_z\times T^2_{xy}=T^3$, which is why Items 4–5 speak of a $T^3$ core. Target $\operatorname{Ric}=-3g=-(n-1)g$ with $n=4$ is consistent. The JSON entries "xx", "yy", etc. are the **mixed** components $E^i_i=\operatorname{Ric}^i_i+3$ (the additive $3$ is $-\lambda$), which is the correct object to combine.

### Item 1 (anisotropy drift-Laplacian) — derivation correct

From the JSON, with $\Delta=\partial_t^2+\partial_z^2$, $\delta=b-c$, $\sigma=b+c$:
$$E^x_x-E^y_y=-e^{-2\phi}\big[\Delta\delta+(b_t^2-c_t^2)+(b_z^2-c_z^2)\big]=-e^{-2\phi}\big[\Delta\delta+\nabla\sigma\!\cdot\!\nabla\delta\big].$$
The cross terms $b_tc_t,\,b_zc_z$ are identical in both mixed components and cancel; $b_t^2-c_t^2=\delta_t\sigma_t$ etc. Setting the two fiber equations to zero gives exactly $\Delta\delta+\nabla\sigma\cdot\nabla\delta=0$. Verified. The drift field is $\nabla\sigma=\nabla\log\rho$, a genuine bounded field for smooth data on the compact 2-plane region.

### Item 3 (orbit-area equation) — coefficient discrepancy; the true source is stronger

The JSON's own `Exx_plus_Eyy` is
$$E^x_x+E^y_y=6-e^{-2\phi}\big[\Delta\sigma+|\nabla\sigma|^2\big],$$
and their `lap_flat_rho_over_rho` equals $\Delta\sigma+|\nabla\sigma|^2=\Delta\rho/\rho$ (calculus identity for $\rho=e^\sigma$). Setting $E^x_x+E^y_y=0$ therefore gives
$$\boxed{\Delta\rho=6e^{2\phi}\,\rho.}$$
There is **no** $-|\nabla\delta|^2$ term. Item 3's formula $\Delta\rho=(6e^{2\phi}-|\nabla\delta|^2)\rho$ — repeated in `step72_structural_analysis.json` under `orbit_area` — contradicts the sum they themselves computed. The origin is likely a mis-substitution of $|\nabla\sigma|^2$ into $|\nabla b|^2+|\nabla c|^2$-type bookkeeping; note $|\nabla\sigma|^2+|\nabla\delta|^2=2(|\nabla b|^2+|\nabla c|^2)$, which is where a spurious $\delta$-gradient can slip in.

Consequence, and it works in the construction's favor: with the correct source $6e^{2\phi}\rho>0$, $\rho$ is **strictly subharmonic for all $\delta$**, not only for the isotropic case. The conditional statement "subharmonic when $6e^{2\phi}>|\nabla\delta|^2$" (structural JSON, `anisotropic_case`) should be replaced by the unconditional fact. The $\rho$ no-interior-maximum conclusion used downstream survives and is in fact unconditional.

### Item 2 (maximum principle with reflection condition at t=0) — correct, including the Neumann handling

$L\delta:=\Delta\delta+\nabla\sigma\cdot\nabla\delta=0$ is a linear elliptic operator with no zeroth-order term, so the strong maximum principle and Hopf lemma apply. The perimeter of $[0,R]\times S^1$ is the two circles $\{t=0\}$ and $\{t=R\}$ ($z$ periodic, no edge). At $\{t=0\}$ the outward conormal is $-\partial_t$. If a non-constant $\delta$ attained its maximum only on $\{t=0\}$ at $(0,z_0)$, Hopf forces $-\delta_t(0,z_0)>0$, i.e. $\delta_t(0,z_0)<0$, contradicting the reflection condition $\delta_t(0,z)\equiv0$. Hence the maximum is attained on $\{t=R\}$; symmetrically for the minimum. So
$$\max_z\delta(R,z)\ge\max_z\delta(0,z),\qquad \min_z\delta(R,z)\le\min_z\delta(0,z),$$
and the oscillation of the fiber shape at $t=R$ dominates that at the center. The Neumann/reflection condition is exactly what closes the Hopf step; part (b) is handled correctly. (Requires bounded $\nabla\sigma$ and interior sphere condition — both hold for smooth data on the compact region.)

A sharper rigidity worth recording: if the terminal circle carries a **fixed** fiber shape ($\delta\equiv D$ constant on $\{t=R\}$, as an exact match to a single flat cusp lattice demands), then global max $=$ global min $=D$ and $\delta\equiv D$ **throughout**. So exact matching to a fixed-shape flat cusp forces a uniformly anisotropic (rectangular) fiber shape everywhere; all inhomogeneity must live in $\sigma$ (orbit area) and $\phi$ (conformal factor), not in $\delta$.

### Item 4 (isotropic impossibility) — correct, and it extends to all z-homogeneous diagonal cores

For $g=dt^2+f^2h$ over $T^3$, $s=f'/f$, $f''/f=s'+s^2$: normal $s'+s^2=1$, tangential $s'+3s^2=3$; subtracting gives $2s^2=2$, $s=\pm1$, $s'=0$, incompatible with $s(0)=0$. Verified. The unique isotropic solution is the exact cusp $f=e^{\pm t}$, which has no geodesic center.

I extended this to the **anisotropic $z$-homogeneous** case, because that is what Item 2's rigidity pushes toward. For a diagonal $t$-only metric $g=dt^2+\sum_i e^{2\psi_i}dx_i^2$ (three flat fiber directions $z,x,y$), $\tau=\sum_i\psi_i'$:
$$\text{tangential: }\ \psi_i''+\psi_i'\tau=3\ (i=1,2,3),\qquad \text{normal: }\ \textstyle\sum_i(\psi_i''+\psi_i'^2)=3.$$
At a geodesic center $\psi_i'(0)=0\Rightarrow\tau(0)=0$, so each $\psi_i''(0)=3$, giving $\sum\psi_i''(0)=9\neq3$. **No diagonal $z$-homogeneous core with a totally geodesic center exists**, isotropic or anisotropic. This strengthens Item 4 into a clean dimension-count obstruction: three tangential focusing equations each force sectional-scale $3$, but the Hamiltonian constraint permits only total $3$. The immediate structural conclusion: any admissible core must be **genuinely $z$-inhomogeneous** — the 2-plane elliptic system is mandatory, a 1-variable reduction cannot carry the construction. (The exact cusp $\psi_i=t$ satisfies the $z$-homogeneous equations but has $\psi'(0)=1$, no center — consistent.)

### Item 5 (forced compatibility) — arithmetic correct; it establishes consistency of necessary conditions, not existence

Gauss on the flat $T^3$ cross-section, ambient $\operatorname{Ric}=-3g$ in 4D ($R_{amb}=-12$, $\operatorname{Ric}(n,n)=-3$): $0=R_\Sigma=-12+6+H^2-|A|^2$, so $|A|^2=H^2-6$. With $|A|^2\ge H^2/3$ (Cauchy–Schwarz in 3 fiber dimensions), $H^2\ge9$ exactly, relaxed to $H\ge3-O(\delta)$ under defect $\delta$. Writing $H=3-\epsilon$: $(9-H^2)/6=\epsilon-\epsilon^2/6$, which reproduces the `forced_design` `delta_gauss` column to all listed digits ($\epsilon=0.1\to0.09833$, $\epsilon=0.01\to0.009983$). The length relation $R\ge\tfrac12\log(1+6/\delta)$ reproduces `R_min` ($\epsilon=0.1\to2.0637$). The two conditions — Gauss lower bound $\delta\gtrsim\epsilon$ from the terminal circle, and the interior weighted normal balance $\delta\gtrsim e^{-2R}$ from the Step-70 identity $e^{2t}b(t)=-3-\int_0^t e^{2s}|B|^2\,ds$ — are jointly satisfiable by $H=3-\epsilon,\ \delta\sim\epsilon,\ R\sim\tfrac12\log(6/\epsilon)$. Verified as a compatibility statement. It is necessary and consistent; it does not by itself produce a core, matching the note's own remark that existence of approximate cores is not established.

One distinction the notes blur and that matters here: $|A|^2=H^2-6$ constrains the **extrinsic expansion anisotropy** (the shape operator $S$), while $\delta=b-c$ is the **intrinsic fiber-shape anisotropy**. At a standard cusp $S\to I$ (isotropic expansion, $|A|^2\to3=H^2/3$, Cauchy–Schwarz near-equality) **regardless** of the flat lattice's rectangularity; the lattice anisotropy sits in $\delta$, not in $S$. So a nonzero constant $\delta$ at the cusp is fully compatible with $H\to3$ and does not enter the Gauss balance. This is the reconciliation of Item 5 with the anisotropy of Items 1–2.

### Key question — does the drift-Laplacian block the graph-manifold construction?

It does not block; it constrains. Concretely:

1. $L\delta=0$ is homogeneous linear elliptic; $\delta\equiv\text{const}$ is a solution, and constant $\delta$ is exactly what an exact match to a single fixed anisotropic flat cusp lattice requires (Item 2 rigidity). The lattice-quotient $(N,1,1)$ construction supplies precisely such a fixed rectangular flat torus. So the anisotropy propagation *requires matching to an anisotropic cusp, which the quotient provides* — this is the correct reading of the mechanism, not an obstruction.

2. The subharmonic orbit-area equation $\Delta\rho=6e^{2\phi}\rho$ is consistent with the expanding end: with the reflection condition $\rho_t(0,z)=0$, the same Hopf argument puts the maximum of $\rho$ on $\{t=R\}$, i.e. orbit area is largest toward the cusp. No conflict.

3. The genuine analytic content is displaced onto the parts the $\delta$-equation cannot decide: (a) existence of a **$z$-inhomogeneous** core (mandatory by the extended Item-4 obstruction) with totally geodesic center whose mean curvature climbs to $H\to3^-$ with the right terminal asymptotics — this is a well-posed two-circle Dirichlet problem for the genuinely elliptic conformal-gauge system (symbol determinant $2(\tau^2+\xi^2)^3\ne0$, confirming the ellipticity entry and the reading of the Galerkin blow-up as an elliptic Cauchy artifact rather than geometry); and (b) the arithmetic realization of the required peripheral sublattice in a hyperbolic 4-piece ($b_3=0$ for Slavich's manifold, still to be extracted from its presentation).

So: the drift-Laplacian, the maximum principle, and the orbit-area subharmonicity are mutually consistent structural constraints that shape the target (uniformly-rectangular fiber, inhomogeneity carried by $\sigma,\phi$, $z$-dependence mandatory) but leave the construction open on the existence side, exactly as the Step-70 notes state.

### Items to correct or resolve

- **Fix the orbit-area coefficient** in Item 3 and in `step72_structural_analysis.json`: the correct identity is $\Delta\rho=6e^{2\phi}\rho$ (unconditional strict subharmonicity), not $(6e^{2\phi}-|\nabla\delta|^2)\rho$. Downstream conclusions improve, not weaken.
- **Record the extended Item-4 result**: no diagonal $z$-homogeneous core (isotropic or anisotropic) admits a geodesic center; the $9\ne3$ Hamiltonian count makes $z$-inhomogeneity mandatory. This sharpens the analytic target and rules out an entire class of ansätze in one line.
- **Separate the two anisotropies** ($\delta$ vs. $S$) wherever the Gauss balance and the fiber-shape propagation are used together, so the "$H\to3$ with anisotropic lattice" matching is not read as a tension.
- The `rho_identity_residual` string in the JSON does not reduce to $0$ as printed; if it is meant to certify $\Delta\rho=6e^{2\phi}\rho$, re-run the simplification, since the printed expression carries an uncancelled $e^{\pm2\phi}$ weighting.

Unresolved by the present material and needed to advance: an existence result for the $z$-inhomogeneous elliptic two-circle problem producing $H\to3^-$ with matched cusp asymptotics (the decisive analytic step), and the topological computation $b_3=0$ for the intended hyperbolic 4-piece. Neither is settled by the structural properties checked here, all of which are compatible with the construction proceeding.