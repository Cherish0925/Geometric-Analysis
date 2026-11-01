# TTCS Independent Branch Record

```json
{
  "step_id": 77,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step77_internode_kernel_block_framework.md",
    "Sessions/S0910A02/workspace/data/step77_scalar_decoupling_and_mu_vanishing.json",
    "Sessions/S0910A01/workspace/notes/step78_equivariant_diagonal_reduction.md",
    "Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md"
  ]
}
```

## Task

Verify the following structural theorem about the Ozuch desingularization obstruction on the product orbifold (S²×S²)/Z₂ with Ric=Λg, Λ>0.

CLAIM: All local Ozuch second obstruction coefficients μ_k(ζ^ε) = 0 (k=1,2,3) at every A₁ node, for both chiralities ε, in every chirality pattern.

PROOF SKETCH:
1. The degree-4 del Pezzo Bl₄CP² admits KE metrics (Tian 1990). These approach the product orbifold along comparable-scale nondegenerate sequences with compatible (Kähler) EH insertions. Ozuch's necessary conditions t²μ_k = O(t^{5/2}) at comparable scales force μ_k = 0 (since μ_k is t-independent).
2. The reflection c(z,w)=(z̄,w) is an isometry fixing every A₁ node and exchanging chiralities. Since R⁺=R⁻ and ∇Rm≡0, local μ_k are c-equivariant, giving μ_k(ζ⁻) = μ_k(ζ⁺) = 0.
3. D₈ symmetry and ∇Rm≡0 give node independence.

POTENTIAL ISSUES TO CHECK:
(a) Does the del Pezzo KE desingularization truly approach the product orbifold at comparable scales? The four A₁ points have Z₂-permutation symmetry; does the family preserve this?
(b) Is μ_k truly t-independent in Ozuch's framework? The h₂ and h₄ equations (eqs (22)-(23)) define μ_k from the source Λ·eh - Q^(2)(h₂,h₂), which depends on the orbifold geometry and EH direction but not the scale t. Verify.
(c) Does the c-equivariance argument correctly identify μ_k(ζ⁻) with μ_k(ζ⁺)? The key point is that c maps the SD kernel basis to the ASD kernel basis while preserving the local curvature structure (since R⁺=R⁻).
(d) Is there any gap between 'existence of KE desingularization' and 'Ozuch's necessary conditions vanish'? Ozuch's equations are necessary for any nearby Einstein metric; the KE metrics exist; so the equations must be satisfied. But check whether the KE metrics are nondegenerate in Ozuch's sense (Definition 1.26).

## Output

# Scientific verification memo

## Overall assessment

The supplied material rigorously supports

\[
\mu_1(\phi^\epsilon)=0
\]

for every unit \(\phi^\epsilon\in\ker R^\epsilon\), through Ozuch’s determinant formula and

\[
R^\pm=\operatorname{diag}(\Lambda,0,0).
\]

It also supports chirality covariance and node equivalence for the local coefficient vector. The proposed vanishing of \(\mu_2,\mu_3\), however, is not yet established by the KE-control argument as written. Two ingredients are absent:

1. a sourced construction of a comparable-scale, equivariant KE degeneration to the specified product orbifold satisfying Ozuch’s Definition 1.26;
2. control of order-\(t\) drift in the normalized EH directions and orbifold parameter \(v\), which could cancel the bare \(\mu\)-term.

This agrees with `step78_equivariant_diagonal_reduction.md`, §5.3, which explicitly states that the complete Biq16 expression is still needed because \(dR^-\) has nonzero kernel-block components.

---

## 1. What the Ozuch estimate actually implies

The supplied notes give the finite-dimensional equation

\[
t_j\lambda^j_k(\phi_j,v)+t_j^2\mu^j_k(\phi_j,v)
   =O(t_{\max}^{5/2}).
\]

If

\[
t_j\asymp t_{\max},\qquad
\lambda^j_k(\phi_j,v)=0
\]

for every member of the degenerating family, then division by \(t_j^2\) gives

\[
\mu^j_k(\phi_j,v)=O(t_{\max}^{1/2}),
\]

and hence \(\mu^j_k(\phi_j,0)=0\) after passage to the orbifold limit. This part of the proposed reasoning is correct.

The important issue is that leading-order kernel membership alone is insufficient. If the exact family has

\[
\phi_j(t)=\phi_{j,0}+t_j\dot\phi_j+o(t_j),
\qquad
v(t)=t_jv_1+o(t_j),
\]

with \(\lambda(\phi_{j,0},0)=0\), then

\[
\frac{\lambda(\phi_j(t),v(t))}{t_j}
 \longrightarrow
D_\phi\lambda(\dot\phi_j)+D_v\lambda(v_1).
\]

The divided equation becomes

\[
D_\phi\lambda(\dot\phi_j)+D_v\lambda(v_1)
+\mu(\phi_{j,0},0)=0,
\]

rather than \(\mu(\phi_{j,0},0)=0\). Thus the KE family must be matched to Ozuch’s parameters in a way that gives

\[
\lambda(\phi_j(t),v(t))=o(t_j),
\]

or, more strongly, keeps \(\phi_j(t)\) exactly in \(\ker R^\epsilon\) and removes \(v(t)\). The statement that the insertions are Kähler-compatible may provide this, but no local matching theorem establishing it is included in the supplied files.

The \(A\)-symmetry from `step78_equivariant_diagonal_reduction.md`, Theorem 2.1, would eliminate the four scalar zero modes \(u_i g_j\) if the complete smoothing family and its KE metrics were \(A\)-invariant. That invariance has not been constructed here.

---

## 2. Scale independence of \(\mu_k\)

For a normalized EH direction \(\phi\), the formal coefficient

\[
\mu_k(\phi,0)
\]

is independent of the gluing magnitude \(t\). The orbifold tensors \(H_2,H_4\), the operator used to determine the local correction, and the source

\[
\Lambda\,\mathrm{eh}-Q^{(2)}(h_2,h_2)
\]

are computed at fixed \(g_o,\Lambda,\phi\); the gluing magnitude appears through the explicit factor \(t^2\) in the reduced equation.

The notation \(\mu_k(\zeta)\) should therefore be interpreted with care when \(\zeta=t\phi\). The scale-independent object is \(\mu_k(\phi)\) for a normalized direction. Since the intended result is vanishing, homogeneity then extends it to nonzero multiples.

The numerical JSON file does not independently evaluate these coefficients. Its `r0_control_vanishing_theorem` entry is prose encoding the same KE argument. The actual computations in that file establish factor-tracelessness and symmetry parities, not the Biq16 values of \(\mu_2,\mu_3\).

---

## 3. Comparable-scale KE degeneration

Tian’s existence theorem for smooth degree-four del Pezzo surfaces does not by itself produce the required degeneration. The following geometric data are still needed:

- an explicit \(D_8\)-equivariant smoothing
  \[
  \mathcal X\to\Delta,\qquad \mathcal X_0=(S^2\times S^2)/\mathbb Z_2,
  \]
  whose four local \(A_1\) smoothing parameters satisfy
  \[
  a_j(s)=\kappa_j s+O(s^2),\qquad \kappa_j\ne0;
  \]
- convergence of the normalized KE metrics on \(\mathcal X_s\) to the product orbifold metric;
- identification of the four bubbles as EH spaces, with
  \[
  t_j(s)\asymp t_\ell(s)
  \]
  for all \(j,\ell\);
- the weighted estimates and parameter matching required by Ozuch’s Definition 1.26.

A transitive symmetry of the central fiber does not automatically imply that an arbitrary smoothing path preserves it. If the group action extends to the total family and the KE metrics are chosen invariantly, then invariantly defined bubble scales at nodes in one orbit are equal. No explicit family or source passage proving these facts appears in `step77_internode_kernel_block_framework.md`; its source-pinning section cites Ozuch’s local obstruction equations but not a del Pezzo degeneration theorem.

Consequently, potential issue (a), together with the Definition 1.26 part of (d), remains unresolved from the supplied evidence.

---

## 4. Reflection and chirality

The reflection

\[
c(z,w)=(\bar z,w)
\]

has the required local properties:

- it is an isometry of the product metric;
- it commutes with the quotient half-turn because
  \(c r_\pi c^{-1}=r_{-\pi}=r_\pi\);
- it fixes all four pole pairs;
- it reverses the four-dimensional orientation and therefore exchanges
  \(\Lambda^+\) and \(\Lambda^-\).

The natural covariance statement is vector-valued:

\[
\boldsymbol\mu^{-}(c_*\phi)
   =U_c\,\boldsymbol\mu^{+}(\phi),
\]

where \(U_c\) is the orthogonal change-of-basis matrix between the transported obstruction bases. Componentwise equality is valid only when the ASD basis is defined by transporting the SD basis through \(c\). For vanishing, the distinction is immaterial.

The equations defining \(h_2,h_4\), the quadratic Einstein term, and the \(L^2\)-orthogonality normalization are preserved by isometries, so this covariance is mathematically sound. The identities \(R^+=R^-\) and \(\nabla\mathrm{Rm}=0\) make the two local curvature models identical, although naturality under \(c\) is the central argument.

Thus potential issue (c) is resolved after replacing literal componentwise equality by the transported-basis formula.

---

## 5. Coverage of all kernel directions and nodes

A single symmetric KE sequence may realize only one limiting EH direction. There is nevertheless a local symmetry argument that extends one zero to the full kernel circle.

Rotations of the two sphere factors by angles \((\alpha,\beta)\) commute with the quotient action and fix every pole. On the standard two-form bases, they rotate

\[
\operatorname{span}\{\omega_2^+,\omega_3^+\}
\quad\text{and}\quad
\operatorname{span}\{\omega_2^-,\omega_3^-\}
\]

by the combinations \(\alpha+\beta\) and \(\alpha-\beta\), respectively. Each action is transitive on the corresponding unit circle. Hence, by isometry covariance,

\[
\boldsymbol\mu^\epsilon(\phi_0)=0
\quad\Longrightarrow\quad
\boldsymbol\mu^\epsilon(\phi)=0
\]

for every unit \(\phi\in\ker R^\epsilon\).

Node-moving product isometries normalize the half-turn and carry any pole pair to any other pole pair. Together with local symmetry and \(\nabla\mathrm{Rm}=0\), this establishes node equivalence for the bare local coefficient. No additional use of a KE family at each separate direction is required.

---

## 6. Present evidentiary status of \(\mu_2,\mu_3\)

The executable calculations supplied establish:

- the SD/ASD algebra;
- the rank-two kernel of \(R^\pm\);
- vanishing of the same-chirality kernel commutator block;
- factor-tracelessness of in-kernel \(H^4\);
- \(\mu_1=0\) through the rank-one determinant.

They do not evaluate the complete source defining \(\mu_2,\mu_3\). In particular, `step78_equivariant_diagonal_reduction.md`, §5.3 records that

\[
dR^-\cdot v\ne0,\qquad R^-\cdot dR^-\ne0,
\]

so the relation \(R^-\rho(\phi)^-=0\) alone does not annihilate every term in the Biq16 formula.

Therefore the currently justified statement is:

\[
\boxed{\mu_1(\phi^\epsilon)=0}
\]

for all nodes, chiralities, and in-kernel directions, together with the conditional implication

\[
\boxed{
\text{an Ozuch-admissible comparable KE family with }
\lambda=o(t)
\ \Longrightarrow\
\mu_2=\mu_3=0.
}
\]

A direct substitution into the complete Biq16 formulas would establish or refute the remaining two coefficients without relying on the global KE degeneration.

Finally, even if all three bare local coefficients vanish, the mixed-chirality inter-node term

\[
t_i t_j^2\,\mathcal I_{ij,k}
\]

remains at order \(t^3\). It lies beneath Ozuch’s \(O(t^{5/2})\) resolution but can still enter the higher-order finite-dimensional equation. Vanishing of the local \(\mu_k\) therefore does not by itself reduce the construction to a uniform inverse estimate and nonlinear contraction.