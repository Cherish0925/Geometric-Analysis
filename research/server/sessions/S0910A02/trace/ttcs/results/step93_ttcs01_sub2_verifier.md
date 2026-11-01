# TTCS Independent Branch Record

```json
{
  "step_id": 93,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step93_curvature_correction_and_kernel_plane_target.md",
    "Sessions/S0910A02/workspace/data/step93_product_curvature_and_kernel_audit.json",
    "Sessions/S0910A02/workspace/notes/step92_ozuch_spectral_connection_and_transversality.md",
    "Sessions/S0910A02/workspace/notes/step77_internode_kernel_block_framework.md",
    "Sessions/S0910A01/workspace/notes/step94_corrected_aabb_and_route_reassessment.md",
    "Sessions/S0910A01/workspace/data/step94_corrected_aabb_principal_response.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 93 correction to the product-orbifold mixed-chirality desingularization target for Yau Problem 26. Check, using the supplied files, whether the curvature correction R^±=diag(Λ,0,0) for S^2×S^2 is correct; whether this invalidates the old Step 92 I/3 critical-scale/e1 ansatz; whether the corrected target should indeed be the Ozuch/Biquard response restricted to ker R^±=ω^⊥ with an angular D8+K invariant equation; and whether the O(t^3) pattern term versus O(t^(5/2)) remainder caveat is stated honestly. Identify any remaining mathematical or source-level errors that could mislead the next computation, and suggest the sharpest concrete formulation of the next coefficient/remainder problem. Do not decide the whole Yau-26 problem; focus on correctness and usefulness of this corrected local target.

## Output

# Verification Memo: Step 93 Product-Orbifold Curvature Correction

## 1. The curvature computation is correct

I reproduced the central algebraic fact independently. For a Riemannian product of two constant-curvature surfaces forming an Einstein 4-manifold with $\operatorname{Ric}=\Lambda g$, take the frame $(e_1,e_2)$ tangent to the first factor and $(e_3,e_4)$ to the second. The only nonvanishing sectional curvatures are $K(e_1,e_2)=K(e_3,e_4)=\Lambda$; mixed planes vanish because the metric is a product. The curvature operator on $\Lambda^2$ is therefore diagonal in $\{e^{12},e^{13},e^{14},e^{23},e^{24},e^{34}\}$ with entries $(\Lambda,0,0,0,0,\Lambda)$.

Passing to $\omega_1^\pm=e^{12}\pm e^{34}$, $\omega_2^\pm=e^{13}\pm e^{42}$, $\omega_3^\pm=e^{14}\pm e^{23}$:
$$
\mathcal R(\omega_1^\pm)=\Lambda\,\omega_1^\pm,\qquad \mathcal R(\omega_2^\pm)=\mathcal R(\omega_3^\pm)=0,
$$
so $R^+=R^-=\operatorname{diag}(\Lambda,0,0)$. With $s=2\operatorname{tr}\mathcal R=2(\Lambda+\Lambda)=4\Lambda$, hence $s/12=\Lambda/3$, the Weyl block is
$$
W^\pm=R^\pm-\tfrac{s}{12}I=\operatorname{diag}\!\big(\tfrac{2\Lambda}{3},-\tfrac{\Lambda}{3},-\tfrac{\Lambda}{3}\big)\neq0 .
$$
This matches `step93_product_curvature_and_kernel_audit.json` exactly (eigenvalues $\{1,0,0\}$ for $R^\pm$, $\{\tfrac23,-\tfrac13,-\tfrac13\}$ for $W^\pm$ at $\Lambda=1$). The earlier $R^\pm=(\Lambda/3)I$ is definitively wrong: it would require $W^\pm=0$, i.e. conformal flatness, which for an Einstein 4-manifold forces constant sectional curvature, contradicted by the vanishing mixed sectional curvatures of $S^2\times S^2$. Both consistency arguments in the note are valid.

The second consistency argument is also sound and worth stating precisely: Ozuch's Theorem 0.2 permits a desingularization only where $\det R^+=0$ or $\det R^-=0$. An invertible $(\Lambda/3)I$ would forbid *any* Einstein desingularization, including the same-orientation Kähler one. Since the all-compatible resolution of the four $A_1$ points is the degree-4 del Pezzo $\mathrm{Bl}_5\mathbb{CP}^2$ (I checked $\chi=4+4=8=3+5$, matching), a kernel must exist. The explicit computation sharpens "kernel exists" to "kernel is exactly two-dimensional," $\ker R^\pm=\operatorname{span}\{\omega_2^\pm,\omega_3^\pm\}=\omega^\perp$, with $\omega_1^\pm$ (the eigenvalue-$\Lambda$ Kähler direction) excluded.

## 2. The invalidation of the old $I/3$ critical-scale / $e_1$ ansatz is correct

The first Ozuch obstruction is $\lambda_k(\zeta^\pm)=c\langle R^\pm(H_2)\zeta^\pm,\zeta^\pm_{(k)}\rangle$ with $\zeta^\pm_{(1)}\propto\zeta$. Vanishing of all three $\lambda_k$ is equivalent to $R^\pm\zeta=0$, i.e. $\zeta\in\ker R^\pm$. Because $R^\pm=\operatorname{diag}(\Lambda,0,0)$ genuinely has a 2-plane kernel, the gluing direction is not forced to zero and is not free either — it must lie in $\omega^\perp$. There is consequently no invertible background form for an inserted $O(t^2)$ term to cancel, so the equation "$\tfrac13+t^2K=0$" and its critical scale $t_*^2=-1/(3K)$ have no referent; they were artifacts of the false $(\Lambda/3)I$ premise. The ansatz $\zeta_i=te_1$ sits on the eigenvalue-$\Lambda$ direction, giving $\lambda_1=c\Lambda|\zeta|\ne0$ at order $t$, so it is obstructed at zeroth order. Withdrawing it is correct. The demotion of the earlier "$e_1$ scalar sign" interpretation is likewise warranted, since that quantity was evaluated on the excluded direction.

## 3. The corrected target object is the right one

The corrected local problem — the Ozuch/Biquard Green response restricted to $\ker R^\pm=\omega^\perp$, giving an angular equation on the 2-plane rather than a scale selection — is the correct object, and the order structure supporting it is consistent with the source:

- Same-chirality response perturbs $R^{\epsilon_j}$ by an infinitesimal frame rotation $[A,R^{\epsilon_j}]$; with $R^{\epsilon_j}=\operatorname{diag}(\Lambda,0,0)$ its $\{2,3\}$-block is identically zero, so same-chirality interactions produce no in-kernel obstruction. This is verified in the Step 77 script and is algebraically forced.
- Opposite-chirality response shifts the *same* block as the receiver (the chirality split $d_eR^-(H^4(\zeta^+))\in\operatorname{End}(\Omega^-)$, Ozuch eq. (9)/(13)), producing the decisive in-kernel shift $R^{\epsilon_j}(H_{ij,2})=O(t_i^2)$.
- With $\zeta_j=t_j\xi_j$, $\xi_j\in K$, the shifted first obstruction is $\lambda^j_k=ct_j\sum_i t_i^2\langle Q_{ji}\xi_j,\zeta_{j,(k)}\rangle$, so the vanishing condition on $K$ is $\Pi_K(\sum_i t_i^2 Q_{ji})\Pi_K\,\xi_j=0$; at equal scales the common $t^2$ cancels and the residual object is a $2\times2$ symmetric form on $K$. This is exactly the note's statement.

I also independently checked A01's normalization repair that feeds $Q$: on the unit $S^2$, Bochner gives $\int|(\nabla^2f)^{TF}|^2=\int(\Delta f)^2-\int|\nabla f|^2-\tfrac12\int(\Delta f)^2=\tfrac12\mu(\mu-2)$, and for $M=L_{(*df)^\#}g$ the pointwise relation $M=2\big(\begin{smallmatrix}-c&a\\a&c\end{smallmatrix}\big)$ from $E=\big(\begin{smallmatrix}a&c\\c&-a\end{smallmatrix}\big)$ yields $\|M\|^2=8(a^2+c^2)=4\|E\|^2$. The factor-four repair, the mode-by-mode cancellation of separated-tensor sectors, and the surviving same-pole value $\approx-0.00400$ are internally consistent, and the note correctly treats $K^{\text{principal}}_{\text{adj}}\approx-0.03544$ as a product-background component of $Q$, not the physical coefficient. The single-image toy values $\operatorname{diag}(8,-4,-4)=12\,e_k\otimes e_k-4I$ are also correct and correctly flagged as flat algebra only.

## 4. The order/remainder statement is faithful but should be reframed

The reservation that the pattern term enters at $O(t_jt_i^2)=O(t^3)$ while the recorded necessary-equation remainder is $O(t^{5/2})$ is stated faithfully, and the conclusion — a computed $O(t^3)$ coefficient is not by itself decisive against the crude estimate — is correct: $t^3\ll t^{5/2}$, so Ozuch's Proposition 2.19 (which yields $\lambda^j_k+\mu^j_k=O(|\zeta_j|^{5/2})$, $\nu_l=O(|\zeta|^{5/2})$) is automatically satisfied by an $O(t^3)$ quantity and cannot see it.

What the note underplays is that $O(t^{5/2})$ is the accuracy of the *crude single-stage* approximate metric, not a fundamental floor. Ozuch Section 3.3 (Prop. 3.14, Cor. 3.25) constructs a higher-order approximate metric — the tower $\bar h^4,\bar h^8$, the jets $\underline h_{j,2},\underline h_{j,4},\mathring{\underline h}_{j,2m}$, with obstruction-cancellation lemmas 3.15/3.18 — precisely to push the remainder below a target obstruction. In the comparable-scale regime this drives the remainder to $O(|\zeta^\pm|^2|\zeta^\mp|^5+|\zeta^\pm|^{3+\beta/12}|\zeta^\mp|^{4-3\beta/4})$, well beneath the second-obstruction order it needs to resolve. The same method applies to the fixed curved product background: the systematically available route to make the $O(t^3)$ coefficient decisive is to build the analogous higher-jet approximate metric and drive the remainder below $t^3$, rather than to rely on a symmetry cancellation of the $O(t^{5/2})$ term. The note lists "sharpen the expansion" as one option but does not point at the ready template; the next computation should treat sharpening as the primary route and symmetry-parity killing as a secondary one.

## 5. Points that could still mislead the next computation

- **Isotropy-group order is inconsistently recorded.** Step 77 §5 writes "$D_8$ stabilizer (order 4)"; $D_8$ is not order 4 under either common convention. Since the reduction of the $2\times2$ angular form to a single function, and any parity cancellation of the remainder, both rest on the exact node stabilizer, its order and generators (factor-swap for equal radii, the reflection $c$, in-factor rotations) must be pinned down explicitly before those reductions are trusted.

- **The kernel plane is itself $\zeta$-dependent to the order being computed.** The far-field of node $i$ contributes a constant term $H_{ij,0}=O(t_i^2)$ that rotates the local frame at $j$, hence rotates $K_j=\ker R^{\epsilon_j}$ by $O(t_i^2)$. When defining $\Pi_{K_j}$ inside a computation that keeps $O(t_i^2)$ shifts, the projector must be taken in the transported frame; applying $\Pi_K$ in the unperturbed frame introduces an error of exactly the order of the quantity being computed. This is a concrete correctness point.

- **Calibration on the all-compatible row is mandatory, not optional.** The convention for the kernel plane, ordered N/S frame transport, and signs must reproduce the known unobstructed del Pezzo family in the $r=0$ (all-compatible) case. If the assembled $Q$ does not return an unobstructed response there, the sign/frame/kernel-plane convention is wrong and any mixed-row number is unreliable.

- **Sign reading.** The product-background principal response sits below zero, but with the physical $H^4$ source normalization (Prop. 1.16, $H^4(\zeta^+)=-\rho(\zeta)^-\!\circ\zeta^+/2r^4$), Bianchi/gauge projection, and isotropy normalization not yet included, its sign carries no structural meaning about whether the branch is obstructed. The note withdraws the old sign interpretation, which is correct; the residual "encouraging" phrasing elsewhere should not be read as evidence.

- **The reach of a possible outcome.** The note's statement that a nondegenerate/no-kernel result would exclude only Einstein metrics near this particular degeneration and this Ozuch branch — not a distant Einstein metric on the same smooth manifold — is correct and important: Ozuch's obstructions are local to the bubbling limit.

## 6. Sharpest concrete formulation of the next coefficient/remainder problem

At receiver node $j$ with chirality $\epsilon_j$ and kernel $K_j=\operatorname{span}\{\omega_2^{\epsilon_j},\omega_3^{\epsilon_j}\}$, define the $2\times2$ symmetric form
$$
\mathcal M_j(\xi)\;=\;\Pi_{K_j}\!\Big[\sum_{i:\,\epsilon_i\neq\epsilon_j} R^{\epsilon_j}\big(H_{ij,2}[\xi_i]\big)\Big]\Pi_{K_j},
\qquad
H_{ij,2}[\xi_i]=\text{2-jet at }j\text{ of }\bar h_i^4,
$$
where $\bar h_i^4$ solves $P_{g_o}\bar h_i^4=\sum_l\nu_l v_l+\sum_k\lambda_k\bar o^4_{i,k}$ on $(S^2\times S^2)/\mathbb Z_2$ with singular asymptotic $H^4(\zeta_i^{\epsilon_i})$ at $i$, in TT/Bianchi gauge, $L^2$-orthogonal to $\mathbf O(g_o)$. The leading pattern-dependent equation (equal scales) is $\mathcal M_j(\xi)\,\xi_j=0$ in $K_j$ for each $j$; its resolution reduces to the sign/kernel structure of $\mathcal M_j$ along the $D_{?}\times K$-invariant ray $\xi(\theta)=\cos\theta\,\omega_2^{\epsilon_j}+\sin\theta\,\omega_3^{\epsilon_j}$.

Two ingredients make it decidable:

1. **Physical kernel-restricted response.** Compute $\Pi_K Q_{ji}\Pi_K$ from the projected product-$P$ resolvent with additive spectral denominators $P_{rq}=\tfrac12(\mu_r+\mu_q)-1$ (this denominator itself should be re-derived, not imported, since it carries the $\Lambda$-dependent curvature term and the negative/zero-mode content noted in Step 77 §5), the EH source $H^4(\zeta^\pm)$ normalized as in Prop. 1.16, Bianchi/TT projection, node-isotropy averaging with the exact stabilizer, ordered N/S frame transport, and the $r=0$ del Pezzo calibration. Do the two geometry types separately (`M_adj` at distance $\pi/\sqrt\Lambda$; `M_diag` at $\pi\sqrt2/\sqrt\Lambda$, regular in each one-factor projection — the cleaner first target).

2. **Remainder below $t^3$.** Build the higher-jet approximate metric for the product orbifold following the Section 3.3 template (extend $\bar h^4,\bar h^8$ and the corresponding ALE jets; use the obstruction-cancellation structure of Lemmas 3.15/3.18) and determine the sharpened remainder order. Establishing a remainder $o(t^3)$ in the invariant kernel directions makes $\mathcal M_j$ decisive directly; failing that, determine whether the exact node parity annihilates the $O(t^{5/2})$ term along the invariant ray. Fix the isotropy group first, since both routes depend on it.

The Step 93 correction itself contains no residual mathematical error I can find; it repairs a genuine load-bearing mistake and points the computation at the correct object. The two substantive things to add before the next number is trusted are the exact isotropy structure and the explicit remainder-sharpening via the Section 3.3 method, together with the $r=0$ calibration and the frame in which $\Pi_K$ is taken.