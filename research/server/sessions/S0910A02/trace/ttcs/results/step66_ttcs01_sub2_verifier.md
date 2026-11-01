# TTCS Independent Branch Record

```json
{
  "step_id": 66,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step66_kahler_reduction_and_operator_audit.md",
    "Sessions/S0910A02/workspace/notes/step65_metric_export_findings.md",
    "Sessions/S0910A02/workspace/data/step66_kahler_substitute_step65.json",
    "Sessions/S0910A02/workspace/data/step66_operator_audit_profiles.json",
    "Sessions/S0910A02/workspace/data/step66_nonlinear_radial_audit.json",
    "Sessions/S0910A02/workspace/data/step66_ode_matrix_extract.json",
    "Sessions/S0910A02/workspace/data/step66_ode_compatibility.json",
    "Sessions/S0910A02/workspace/data/step66_least_squares_h_profile.json",
    "Sessions/S0910A02/workspace/data/step66_ls_profile_nonlinear_audit.json",
    "Sessions/S0910A02/workspace/data/source_text/biquard_1105_4904_pdftotext.txt"
  ]
}
```

## Task

Verify the Step-66 mathematical/computational conclusions about the Eguchi-Hanson correction export for the Yau-26 positive-branch experiment. Read the supplied note/data. Check specifically: (1) whether the Kähler-potential identity and its limitation by the EH bolt cohomology/obstruction term are stated correctly in the session conventions; (2) whether the solver-agnostic operator-norm audit results justify decoupling the refined small-defect certificate from BVP convergence and from the naive-start flow experiment; (3) whether the ODE compatibility extraction (rank-two highest-derivative system plus lower-order constraint) is a legitimate correction to the Step-65 handoff; (4) whether the LS-profile and nonlinear audit should be interpreted only as diagnostic, not as a near-pinched metric certificate; and (5) what concrete mathematical/computational next step would most reduce uncertainty without overclaiming. Please identify any sign/factor/cohomology/gauge caveats that could materially change the next work.

## Output

## Verifier memo — Step-66 Eguchi–Hanson correction export

I recomputed the load-bearing algebra and cross-checked it against the supplied Biquard source text. The five requested points hold up, with several places where the prose is stronger than the mathematics literally supports. I show the checks so they are independently reproducible.

---

### 1. Kähler-potential identity: verified, with two wording items to fix

**Coframe/metric consistency.** With $W=1-r^{-4}$, $e_0=W^{-1/2}dr$, $e_1=\tfrac r2\sigma_1$, $e_2=\tfrac r2\sigma_2$, $e_3=\tfrac{r\sqrt W}2\sigma_3$, the sum $e_0^2+e_1^2+e_2^2+e_3^2$ reproduces $g_{EH}$ exactly. Good.

**Coefficient formulas.** For $\phi=r^2$ ($q=2r$, $q'=2$):
$$A_\phi=\frac{r(r^4-1)\cdot2+(r^4+3)\cdot2r}{r^5}=4+4r^{-4},\qquad B_\phi=\frac{2(r^4-1)\cdot2r}{r^5}=4-4r^{-4},$$
so $A-B=8r^{-4}$ — matches the stated anti-self-dual discrepancy. The "$i\partial\bar\partial(r^2)=2\omega$" proposal is indeed false; note that even asymptotically the constant is $4$, not $2$.

**Exact end potential.** For $q=2r^5/(r^4-1)$: $B_\phi=4$ directly; and $r(r^4-1)q'+(r^4+3)q=4r^5$ gives $A_\phi=4$. Integrating, $\phi'=2r+2r/(r^4-1)=2r^5/(r^4-1)$ confirms $\phi=r^2+\tfrac12\log\frac{r^2-1}{r^2+1}$, log-singular at $r=1$. All correct.

**The $-\tfrac12$ identity is genuine, not fitted.** In `step66_kahler_substitute_step65.json` the difference for factor $-1/2$ vanishes identically as a function of the *free* symbol $q(r)$ and its derivatives up to $q'''$ (`diff00=diff11=diff33="0"`, `holds:true`), while $\pm1,\pm2,+1/2$ leave nonzero rational expressions. Because $q$ is arbitrary, this establishes
$$d\operatorname{Ric}_{EH}(h_\phi)=-\tfrac12\,i\partial\bar\partial(A_\phi+B_\phi)$$
as an identity, not a coincidence among six trial constants. It is also the expected Kähler linearized-Ricci-form relation $\delta\rho=-\tfrac12 i\partial\bar\partial(\operatorname{tr}_\omega\delta\omega)$, and the frame output has the correct Kähler symmetry $\text{frame}_{00}=\text{frame}_{33}\ne\text{frame}_{11}$. Solid.

**Two items the memo should correct.**

- The cohomological reasoning ("smooth global scalar cannot represent $\Lambda\omega$") is correct because $[\omega]\ne0$ in $H^2(T^*S^2)$. But the identification with Biquard's obstruction tensors is not literal: the scalar-ansatz obstruction is the **self-dual Kähler class $[\omega]$**, whereas Biquard's $o_j=\Omega(I_j\cdot,\cdot)$ come from the **anti-self-dual $L^2$ harmonic form $\Omega$** (source eq. 5, "2-forme anti-autoduale"). Both reflect $H^2(EH)\ne0$, but they are different representatives in different bundles. The word "precisely" overstates a heuristic linkage; the operational conclusion (scalar ansatz insufficient globally) is unaffected.

- The note writes Biquard's obstructed equation with a factor $\tfrac13$: $d_{EH}\operatorname{Ric}(h)=\Lambda e_h+\tfrac13\sum_j\lambda_j o_j$. The source equations (23) and Prop. 2.2 carry coefficient $1$: $d_{eh}\operatorname{Ric}(h)=\Lambda\,eh+\sum_1^3\lambda_i o_i$. The $\lambda_j$ are unknowns, so a constant is absorbable, but the deviation from the source should be noted so the $\lambda_j$ normalization stays traceable when the ambient $H$ is finally inserted.

---

### 2. Solver-independent operator evaluation: internally consistent; separation is sound; near-pinching is not yet demonstrated

Every entry in `step66_operator_audit_profiles.json` is consistent with exact facts:

- **raw ($h=0$)**: defect $=1$ everywhere, frame dRic $=(0,0,0)$. Since $\operatorname{Ric}_{EH}=0$, the residual is $\|{-\Lambda g}\|_{op}=|\Lambda|=1$. This correctly shows the raw insert is *not* near-pinched.
- **kpot_parallel ($h=4g$)**: defect $=1$, frame $(0,0,0)$. This equals the $A_\phi=B_\phi=4$ potential ($h_\phi=4g$), and $d\operatorname{Ric}(cg)=0$ by scale invariance — matching $-\tfrac12 i\partial\bar\partial(8)=0$. A clean internal cross-check.
- **r2metric ($h=r^2g$)**: defect $\approx8.92$ — the isotropic $r^2g$ is distinct from the Kähler Hessian $i\partial\bar\partial(r^2)$ (which has $A\ne B$ and zero linearized Ricci because $A+B=8$ is constant). The distinction is handled correctly; this is the "$\Delta_L$ vs full linearized Ricci" trap.
- **scalar_cutoff**: far-region median $\sim3\times10^{-6}$, far/all maxima $O(1)$–$O(10)$ near the artificial truncation. Correct picture: the scalar potential removes the source away from the bolt but leaves a compact core/transition residual.

The methodological separation is legitimate: given any assembled $h$, one computes $d\operatorname{Ric}_{EH}(h)-\Lambda g$ pointwise regardless of how $h$ was produced, so BVP convergence is not the certificate. Two substantive points must stay attached to this:

- The pointwise computation as run is the **first-order (linearized)** residual at unit scale. The physical $O(t)$ core / $O(t^{1/2})$ transition pinching for the assembled $g_{t,\varphi}=t(e_h+th)$ is a **nonlinear, $t$-scaled** statement (Biquard Lemma 4.1). `step66_nonlinear_radial_audit.json` supplies the $t$-scaled version, and it confirms raw stays $\delta_{\text{far}}\approx1$ across $t\in[3\times10^{-4},10^{-2}]$; no reduction with $t$.
- No genuine Biquard $h$ has been fed into either routine. Consequently no branch is near-pinched by these numbers; the note's statement that the $O(1)$ compact residual cannot support the refutation direction is exactly right and is not overstated.

---

### 3. Rank-two + compatibility extraction: verified by hand, and legitimate

I recomputed the left-null vector of the highest-derivative matrix $M$ (columns $=(f_1',f_2'',f_3'')$). Simplifying `step66_ode_matrix_extract.json`:

column $f_1'$: $\big(\tfrac{3r^4-1}{2r^5},\ \tfrac{r^4-1}{2r^5},\ \tfrac{r^4+1}{2r^5}\big)$; column $f_2''$: $\big(-\tfrac{r^4-1}{r^4},\ -\tfrac{r^4-1}{2r^4},\ 0\big)$; column $f_3''$: $\big(-\tfrac{r^4-1}{2r^4},\ 0,\ -\tfrac{r^4-1}{2r^4}\big)$.

Testing $v=(-1,2,1)$:
- $f_1'$: $[-(3r^4-1)+2(r^4-1)+(r^4+1)]/(2r^5)=0$;
- $f_2''$: $(r^4-1)/r^4-(r^4-1)/r^4=0$;
- $f_3''$: $(r^4-1)/(2r^4)-(r^4-1)/(2r^4)=0$.

So $\operatorname{rank}M=2$ with left-null $(-1,2,1)$ is correct, and the compatibility numerator in `step66_ode_compatibility.json` reproduces the note's constraint term-for-term (with $a_0=f_1,b_0=f_2,b_1=f_2',c_0=f_3,c_1=f_3'$; it contains no $f_1'$, i.e. it is first-order). This is a proper sharpening of the Step-65 "2 second-order + 1 first-order" description: the rank deficiency is the contracted second Bianchi identity, which is expected for $d\operatorname{Ric}(h)=\Lambda g$ posed without gauge fixing.

Relevant point for the next work: Biquard does **not** solve this constrained singular system. He adds the gauge term $\delta_g^*B_{g_t}g$ (source §5, eqs. 43–48), so the operator becomes the elliptic $P=\tfrac12\nabla^*\nabla-\mathring R$ acting on Bianchi-gauge tensors, and the obstruction is isolated into the finite-dimensional $O_{eh}=\langle o_j\rangle$. Imposing $B_{eh}h=0$ within the $U(2)$ diagonal ansatz turns the rank-2 constraint manifold into a genuine elliptic ODE system and is the mathematically clean route; solving the constrained system directly is workable but is not the formulation the source uses. The singular denominators $r^2(r^4-1)$ at the bolt are correctly identified for proper-distance/Frobenius treatment.

---

### 4. LS profile and nonlinear evaluation: correctly read as measurement only

`step66_least_squares_h_profile.json` reports `lsqr.istop=7` (iteration limit reached at 20000), `cond_est≈1.0×10^7`, `resid_norm≈0.092`, with a max residual $\sim4.7\times10^3$ near the ends. The nonlinear evaluation is decisive: the interior ($r>1.2$) **maximum** residual plateaus at $\approx0.69,0.67,0.65,0.65$ across $t=10^{-2}\!\to\!3\times10^{-4}$, i.e. it does *not* shrink, while only the median shrinks roughly linearly. A genuine Biquard $h$ would drive the residual down uniformly on the controlled region. The plateau is strong evidence the LS profile is not near any solution; the warnings ("not bolt-regular, not ambient-$H$ matched, not a certificate") are, if anything, generous. Treating it strictly as a measurement of the operator infrastructure, not as a near-pinched metric, is the correct reading.

---

### 5. Lowest-uncertainty next step, and the item that most changes the plan

The variable that gates everything downstream is the **ambient quadratic jet $H$** and the associated curvature condition — currently the $(c_1,c_2,c_3)$ end data are the undetermined 2-dimensional gauge freedom that is causing `solve_bvp` not to converge. Concretely, before any further BVP work:

1. **Compute the 2-jet $H$ of the intended orbifold metric at the $A_1$ point** (the $(S^2\times S^2)/\mathbb Z_2$ or del Pezzo model) in geodesic coordinates, then evaluate Biquard's condition via the explicit matrix (source eq. 38):
$$R^+\!\Big(\textstyle\sum H_{ij}\alpha_i\alpha_j\Big)=\begin{pmatrix}-5H_{11}+H_{22}+H_{33}&-6H_{12}&-6H_{13}\\ \cdot&-5H_{22}+H_{33}+H_{11}&-6H_{23}\\ \cdot&\cdot&-5H_{33}+H_{11}+H_{22}\end{pmatrix},$$
and test $R^+(H)(dx^1\wedge dx^2+dx^3\wedge dx^4)=0$ (eq. 26). This single evaluation (i) fixes the 2-dimensional end data and removes the underdetermination, and (ii) decides whether $\lambda_2=\lambda_3=0$ (and, at the bi-Kähler locus, $\lambda_1=0$). It is upstream of, and far cheaper than, any refined $h$ solve. If the condition holds, the linear correction $h$ exists with vanishing first obstruction; if it does not, Biquard's Cor. 8.3 states the naive glued metric is provably not $C^{1,\alpha}$-close to any Einstein metric — a directly usable structural fact either way.

2. **Reformulate in Bianchi gauge and re-coordinatize the bolt** (proper distance $\ell=\int dr/\sqrt W$, Frobenius expansion at $\ell=0$), so the ODE system is elliptic rather than the rank-2 constrained form.

**The item that most changes the next work** is a reading of Biquard's setting that the notes do not make explicit. Biquard's construction of *actual Einstein metrics* (Th. 0.1, Th. 11.3, §9–14) is proven in the **asymptotically hyperbolic non-compact** setting, and it uses deformations of the conformal infinity of $M_0$ to kill the residual obstructions $\mu_j$ ("ce n'est donc qu'ici qu'on utilise la non compacité"). The source states plainly that the compact case carries additional known obstructions it does not resolve, and that only the construction **through Corollary 8.3** — the approximate metric and the necessity of $\det R^+(p_0)=0$ — remains valid when $M_0$ is compact. For a closed manifold (which is what Yau-26 requires), there is no conformal-infinity knob to remove the $\mu_j$ residual, so a small operator residual for the assembled $g_{t,\varphi}$ does **not** by itself yield a closed Einstein metric. This means:

- for the existence direction, the EH-desingularization gives a small-residual approximate metric on the closed model, but the last step to a genuine closed Einstein metric is exactly the open problem Biquard sets aside — the operator infrastructure being built does not bridge it;
- for the refutation direction, a small linearized residual on the EH piece is not a statement about non-existence of Einstein metrics on the closed manifold.

Sign/factor/cohomology/gauge points that could materially move the work: the $\tfrac13$ vs coefficient-$1$ in the obstructed equation (item 1); the self-dual-Kähler vs anti-self-dual-$L^2$ distinction underlying the obstruction (item 1); the ambient $H$ curvature evaluation that fixes the sign of $\det R^+$ and the vanishing of $\lambda_j$ (item 5.1); and the choice to impose Bianchi gauge rather than propagate the singular rank-2 constraint (item 3). None of the Step-66 computations I checked contain an arithmetic error; the reach of the conclusions is stated accurately in the workspace notes, and the one thing to keep in front of the plan is the AH-vs-compact gap in Biquard's existence theorem.