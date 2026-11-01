# TTCS Independent Branch Record

```json
{
  "step_id": 71,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/Poincaré-Einstein-4-manifolds-with-cusps--d36d062e94d0--09d8ca1fbe38/object.md",
    "Sessions/S0910A03/workspace/notes/step69_anisotropic_cusp_compensation.md",
    "Sessions/S0910A03/workspace/notes/step70_critical_identity_and_corrections.md",
    "Sessions/S0910A01/workspace/notes/step72_graph_neck_weighted_shear_budget.md"
  ]
}
```

## Task

Analyze the Li–Liu Type-I equation relevant to T^2-compatible anisotropic quotients. The source equation is (e^v)_{xi xi}+Delta_{T^2}v=0, with W=1-(xi/2)v_xi. For a one-angular-variable reduction v(xi,theta), derive the correct nonlinear PDE, its linearization around a constant bounded AH-cusp solution, Fourier radial branches, the slice-average conservation law, and the reflection/totally-geodesic condition translated into the Li–Liu metric variables if possible. Decide whether their BVP1 family can contain a totally geodesic T^3 level or whether Proposition 6.6/global geometry rules it out. Identify a mathematically meaningful finite-cylinder approximate matching experiment that preserves the nonlinear equation and quotient symmetry, without claiming it solves the full graph gluing.

## Output

# Verification Memo — Li–Liu Type I reduction, anisotropic $T^2$ quotients, and the totally geodesic $T^3$ question

Session S0910A03, task on the Type I Toda reduction. I worked the requested derivations independently and cross-checked against the paper's Section 3–5 and against the A03/A01 step-notes. The central finding is clean and I believe decisive for the reflection-doubling idea: **no $\xi$-level of a BVP1 Einstein metric can be totally geodesic**, and this follows by an elementary computation directly in the reduction variables, independent of the anti-self-dual argument. I also give the linearization, radial modes, slice-average identity, the correct reading of Proposition 6.6, and a finite-cylinder experiment that preserves the exact reduction.

---

## 1. The one-angular-variable nonlinear PDE

Take flat $g_{T^2}=d\theta^2+d\psi^2$ (volume one) and $v=v(\xi,\theta)$, so $\Delta_{T^2}v=v_{\theta\theta}$. Since $(e^v)_{\xi\xi}=e^v(v_{\xi\xi}+v_\xi^2)$, the Type I equation $(e^v)_{\xi\xi}+\Delta_{T^2}v=0$ becomes

$$
e^{v}\bigl(v_{\xi\xi}+v_\xi^{2}\bigr)+v_{\theta\theta}=0 .
\tag{1}
$$

Both second-derivative terms enter with the same sign ($e^v>0$), so (1) is a **nonlinear elliptic** equation on the half-cylinder $(0,\infty)\times S^1_\theta$. This is an independent confirmation of the ellipticity that A03 Step 70 §1 reached from the $E_{22}$ Einstein component and that A01 relied on: the $\xi$-direction is not an evolution time, and the Cauchy blow-ups seen in the Step 69 Galerkin runs are the expected Hadamard instability of an elliptic Cauchy problem, not geometry. The well-posed problem is Dirichlet in $\xi$, exactly what Li–Liu solve (their Proposition 5.3 solves precisely the finite-cylinder Dirichlet problem on $[0,k_0]\times\Sigma$).

## 2. Slice-average conservation law

Integrate (1) over $T^2$ (or over $S^1_\theta$ in the reduced picture); the Laplacian term integrates to zero:

$$
\frac{d^{2}}{d\xi^{2}}\int_{T^2}e^{v}\,d\mathrm{vol}=0
\quad\Longrightarrow\quad
\int_{T^2}e^{v}\,d\mathrm{vol}=a\,\xi+b .
\tag{2}
$$

This is the paper's affine invariant. For BVP1 the $L^\infty$ requirement forces $a=0$, $b=\overline{e^{\varphi}}$, and the substitution $u=v-\log b$ gives the normalized invariant $\fint_{T^2}e^{u}\equiv1$ used throughout Section 5. On a finite cylinder with data at $\xi_0,\xi_1$, (2) fixes $a=(\overline{e^{\varphi_1}}-\overline{e^{\varphi_0}})/(\xi_1-\xi_0)$; the bounded/AH-compatible branch is selected exactly by imposing equal $\theta$-averages $\overline{e^{\varphi_0}}=\overline{e^{\varphi_1}}$.

## 3. Linearization around a constant AH-cusp state and radial modes

Theorem 3.13(1) gives $v_{\mathrm{mod}}=\bar\varphi$ **constant** for BVP1, so linearize about $v_0\equiv c$. Writing $v=c+\epsilon w$, the quadratic $v_\xi^2$ drops and (1) linearizes to

$$
e^{c}\,w_{\xi\xi}+w_{\theta\theta}=0 .
\tag{3}
$$

With $w=\sum_k \hat w_k(\xi)\phi_k(\theta)$, $-\Delta_{T^2}\phi_k=\mu_k\phi_k$ ($\mu_k\ge0$):

$$
e^{c}\hat w_k''=\mu_k\hat w_k,
\qquad
\hat w_k(\xi)=A_k e^{+\sqrt{\mu_k}\,e^{-c/2}\xi}+B_k e^{-\sqrt{\mu_k}\,e^{-c/2}\xi}.
\tag{4}
$$

The $L^\infty$ condition kills the growing branch $A_k$ for $k\neq0$; the $k=0$ mode is forced constant by (2) with $a=0$. Thus the bounded linearized solution decays at rate

$$
\delta_k=\sqrt{\mu_k}\,e^{-c/2},
$$

reproducing $|v-v_{\mathrm{mod}}|=O(e^{-\delta\xi})$ of Theorem 3.13(1) at linear order, and displaying the uniqueness mechanism of Theorem 3.12 concretely (boundedness = suppression of the growing radial branch). For an anisotropic quotient of type $(N,1)$ — $\theta$-period rescaled by $1/N$ — the eigenvalues scale as $\mu_k\propto N^2$, so $\delta_k\propto N$: **finer angular quotients relax the anisotropic modes faster in $\xi$.** This is the exact linear content of the "anisotropic mode dies quickly" heuristic in Step 69 §4.

## 4. The totally geodesic $T^3$ condition in Li–Liu variables — and its impossibility

Write $h=N^2d\xi^2+h_{\rm slice}$ with $N^2=\xi^{-2}W$, unit normal $n=\xi W^{-1/2}\partial_\xi$. The induced metric on a $\xi$-level $T^3$ is block-orthogonal,

$$
h_{\rm slice}= \underbrace{\xi^{-2}W^{-1}}_{p}\,\eta^{2}
\;+\;\underbrace{\xi^{-2}We^{v}}_{q}\,g_{T^2},
$$

($\eta$ has no $d\xi$ component). The two diagonal principal curvatures are $\tfrac12\,\partial_n\log(\text{coeff})=\tfrac12\,\xi W^{-1/2}\partial_\xi\log(\text{coeff})$:

$$
\lambda_\eta=\tfrac12\xi W^{-1/2}\!\left(-\tfrac2\xi-\tfrac{W_\xi}{W}\right),
\qquad
\lambda_T=\tfrac12\xi W^{-1/2}\!\left(-\tfrac2\xi+\tfrac{W_\xi}{W}+v_\xi\right).
$$

Totally geodesic ($\mathrm{II}\equiv0$) requires at least these two to vanish:

$$
\lambda_\eta=0:\ \ \xi W_\xi=-2W,
\qquad
\lambda_T=0:\ \ -2+\xi\tfrac{W_\xi}{W}+\xi v_\xi=0.
$$

Substituting the first into the second gives $-2-2+\xi v_\xi=0$, i.e. $\boxed{\xi v_\xi=4}$, and since $W=1-\tfrac12\xi v_\xi$,

$$
W=1-2=-1<0 .
$$

Li–Liu prove $W>0$ everywhere on $[0,\infty)\times T^2$ (Proposition 5.8, via the Bochner formula for the Killing field norm $|\mathcal K|^2=\xi^{-2}W^{-1}$). **Hence no $\xi$-level of any BVP1 solution is totally geodesic** — the two diagonal principal curvatures cannot simultaneously vanish while the metric stays Riemannian. Off-diagonal II components (from $\partial_\xi\eta$) can only add to the defect. This is an independent confirmation of the paper's ASD-based remark and of A03 Step 70 §6 ("Li–Liu coordinate slices are far from totally geodesic"); moreover it is sharper, because it does not use $W^+_h=0$ and it holds pointwise in $\theta$ for the full anisotropic family.

Note also that the $\mathbb S^1\times T^2$-invariant totally geodesic hypersurfaces are exactly the $\xi$-levels (principal orbits), and the two ends of $M$ are geometrically distinct (PE end $E_0$ versus AH cusp $E_\infty$), so there is no isometric involution swapping ends whose fixed set could give a non-invariant totally geodesic $T^3$. The reflection-doubling wall simply does not exist inside a BVP1 metric.

## 5. What Proposition 6.6 does and does not decide

Proposition 6.6 constrains complete $\operatorname{Ric}=-nh$ manifolds **with a PE end whose conformal infinity has Yamabe constant $\ge 0$**. It is a statement about ends, not about interior totally geodesic hypersurfaces, so it does not by itself address the $T^3$ question. Its interaction with BVP1 is:

- By **Lemma 6.8**, the PE-end conformal infinity $[g^\flat]$ of the BVP1 family (an aspherical circle bundle over $T^2$) has Yamabe constant $<0$ for all non-flat data. Proposition 6.6 has no hypothesis to apply, so it places no constraint and does **not** exclude these genuine two-ended metrics.
- The single exception is the flat $T^3$ case (constant $\varphi$), where the Yamabe constant is $0$; there Proposition 6.6 case (3) forces the rigid warped product $ds^2+e^{-2s}g_{T^3}$ — precisely the exact hyperbolic cusp (Table 1, case $a=0$). So in the flat case the metric is rigid and one-ended-modeled, consistent with everything.

Thus Proposition 6.6 does **not** rule out the family; the impossibility of a totally geodesic $T^3$ is a separate fact established in §4. It is also consistent with A03 Step 70 §3: a reflection center ($S(0)=0$) extended to a PE end forces $\tfrac14 R_{h_0}=-3-\int_0^\infty e^{2s}|B|^2\,ds<-3$, i.e. conformal infinity scalar curvature $<-12$, whereas the AH cusp of BVP1 has flat conformal infinity. A reflection core and a Li–Liu AH cusp are therefore two structurally different objects, and the §4 computation is the direct reason the Li–Liu piece cannot host the reflection wall.

## 6. A finite-cylinder matching experiment that preserves the exact nonlinear equation

The value of the reduction is that **any** solution of (1) with $W>0$, together with $\eta$ from $d\eta=(We^v)_\xi\,e^f dx\wedge dy+W_x\,dy\wedge d\xi+W_y\,d\xi\wedge dx$, is an **exact** $\operatorname{Ric}=-3h$ metric on the region where $W>0$. This is the property the Step 69 diagonal Galerkin runs lacked (they carried an $O(1)$ interior $E_{00}$ residual). A meaningful experiment therefore solves (1) itself.

Proposed setup, preserving the nonlinear equation and the $(N,1)$ quotient symmetry:

1. **Domain and symmetry.** $[\xi_0,\xi_1]\times S^1_\theta$ with $\theta$-period $P/N$ (the anisotropic quotient of type $(N,1)$ matching the $(N,1,1)$ cusp lattice of Step 69/70). Solve the exact equation (1) — this is literally the finite-cylinder Dirichlet problem of Proposition 5.3, so existence and the continuity-method solve are grounded in the paper.
2. **End data.** Prescribe $v(\xi_0,\cdot)=\varphi_0$, $v(\xi_1,\cdot)=\varphi_1$ with $\overline{e^{\varphi_0}}=\overline{e^{\varphi_1}}$ so that (2) gives $a=0$ (the AH-compatible branch).
3. **Quantities to record.**
 - $\min W$ over the cylinder (Proposition 5.8 is a half-line statement; on a finite piece $W>0$ must be checked, not assumed).
 - The full induced $\|\operatorname{Ric}_h+3h\|_{\rm op}$ in the interior — this should be at machine level, certifying that the interior is exactly Einstein and that any defect lives only at the two cross-sections. This is the clean separation the earlier stand-in models could not provide.
 - At each end cross-section, the two principal curvatures $\lambda_\eta,\lambda_T$ of §4, and $\min_\theta(|\lambda_\eta|+|\lambda_T|)$. By §4 this cannot be driven to zero while $W>0$; measuring it quantifies exactly how far a $T^2$-quotient Li–Liu piece is from admitting a totally geodesic gluing wall.
 - The A01 Step 72 weighted normal functional $\dfrac{2\bigl(3+\int e^{2t}|S-I|^2dt\bigr)}{e^{2R}-1}$, now computed from the **exact** induced metric in the Gaussian coordinate $dt=\xi^{-1}W^{1/2}d\xi$, rather than from a one-dimensional profile.
4. **Sweep.** Vary $N$ and confirm the §3 prediction $\delta_k\propto N$ for the angular relaxation rate; vary $\xi_1-\xi_0$ to see whether $\min W$ ever approaches $0$ (the geometry's own signal that a finite piece is leaving the Riemannian regime).

Interpretation and honest limits of what this measures: the experiment produces exact interior Einstein pieces and isolates the interface second-fundamental-form defect predicted by the $W=-1$ obstruction; it does **not** assemble the graph manifold, does not solve the constraint-compatible gluing, and does not address the sign-$(+)$ branch of the Yau statement. A companion computation worth running is the reflection double of two such pieces across a common $\xi$-level: away from the wall it is exactly Einstein, and the distributional Ricci concentrated on the wall is proportional to the jump $2\,\mathrm{II}$. Since §4 forbids $\mathrm{II}=0$, this doubled object always carries genuine curvature concentration on $T^3$, which is the precise, measurable form of the obstruction to reflection-doubling a BVP1 metric.

## 7. Points needing care before any of this is used downstream

- The §4 impossibility is for exact BVP1 metrics. It says nothing about *approximate* Einstein cores with a nearly-geodesic $T^3$; A03 Step 70 §4 already gives the necessary length $R\ge\tfrac12\log(1+6/\delta)$ for those, and A01 Step 72 shows the weighted shear functional is necessary but not sufficient. The existence of a systematically signed defect $E_{00}$ producing such approximate cores remains unestablished by the retrieved material.
- The frequency normalization $\mu_k$ (hence $\delta_k$) depends on the chosen flat metric on $T^2$ and its volume-one convention; the $N$-scaling in §3 assumes the quotient acts purely on the $\theta$-circle. If the anisotropic quotient also rescales $\psi$, the eigenvalue set changes and the decay-rate sweep must use the actual lattice.
- On a finite cylinder, $W>0$ and the circle-bundle degree condition $\tfrac1{\mathfrak p}\int_\Sigma(We^v)_\xi=\ell$ are extra compatibility relations between the two end-data averages; the experiment must record whether they can be met simultaneously with the equal-average condition of step 2, otherwise the piece does not close up over the quotient base.

Net assessment: the requested derivations are internally consistent and consistent with the paper (Theorems 3.12–3.13, Proposition 5.8, Lemma 6.8) and with the A03/A01 notes. The strongest new item is §4 — a two-line, sign-based proof that BVP1 admits no totally geodesic $T^3$, valid for the whole anisotropic family and independent of the ASD hypothesis — which converts the "cannot be doubled directly" remark into a quantitative, measurable interface defect.