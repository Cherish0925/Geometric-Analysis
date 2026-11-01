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

## Scientific verification memo

### 1. Product curvature computation

The Step 93 curvature correction is exact.

Let each surface factor have constant Gaussian curvature \(\Lambda\), so that the product metric satisfies \(\operatorname{Ric}=\Lambda g\). In the orthonormal frame adapted to the two factors,
\[
\mathcal R(e^{12})=\Lambda e^{12},\qquad
\mathcal R(e^{34})=\Lambda e^{34},
\]
while \(\mathcal R\) vanishes on the four mixed two-forms. With normalized chiral bases beginning with
\[
\kappa^\pm=\frac{e^{12}\pm e^{34}}{\sqrt2},
\]
one obtains
\[
\mathcal R^\pm=\operatorname{diag}(\Lambda,0,0).
\]
Since \(s=4\Lambda\) and
\[
\mathcal R^\pm=W^\pm+\frac{s}{12}I,
\]
it follows that
\[
W^\pm=\operatorname{diag}\!\left(\frac{2\Lambda}{3},
-\frac{\Lambda}{3},-\frac{\Lambda}{3}\right).
\]
Thus the round product is not conformally flat. The Step 93 JSON matrices reproduce this calculation numerically.

The quotient does not change this local tensor calculation: at an orbifold point the curvature is computed on the smooth local cover.

A notation refinement is useful. For the standard complex orientation, only \(\kappa^+\) is the Kähler form of the standard product complex structure. The vector \(\kappa^-\) is the parallel form associated with reversing the complex structure on one factor. Calling both first basis vectors “the Kähler direction” can obscure chirality bookkeeping; “rank-one parallel-form direction” is unambiguous.

### 2. Consequence for the old \(I/3\) and \(e_1\) construction

Ozuch’s first obstruction is, up to a nonzero universal factor,
\[
\lambda_k(\zeta^\pm)
 =\big\langle \mathcal R^\pm\zeta^\pm,\zeta_{(k)}^\pm\big\rangle
\]
(Equation (24) in the supplied Ozuch paper). Vanishing for every \(k\) is therefore equivalent to
\[
\mathcal R^\pm\zeta^\pm=0.
\]
For the product,
\[
K^\pm:=\ker \mathcal R^\pm
=(\kappa^\pm)^\perp,
\qquad \dim K^\pm=2.
\]

Consequently:

* the old background matrix \((\Lambda/3)I\) is wrong;
* an \(e_1=\kappa^\pm\) parameter produces a nonzero order-\(t\) obstruction;
* an order-\(t^3\) interaction cannot cancel that term in a family with \(t\to0\);
* the equation \(1/3+t^2K=0\) and its finite \(t_*\) do not describe a nearby orbifold desingularization branch.

One could formally write \(\Lambda+t^2K=0\) along \(e_1\), but any root has scale of order one and lies outside the small-scale expansion. It has no standing as an Ozuch gluing equation near this degeneration.

The toy matrices in the Step 93 JSON are algebraically correct for unit separation:
\[
12uu^T-4I
\]
has eigenvalues \(8,-4,-4\). They do not supply the product-orbifold coefficient. In particular, the old \(e_1\) evaluation concerns the excluded image direction, and the flat lattice factor \(|x|^{-6}\) has been suppressed only because the displayed toy separations have unit norm.

### 3. Correct kernel reduction

Write the leading parameter at node \(j\) as
\[
\zeta_j=t_j\xi_j,\qquad
\xi_j\in K_j,\qquad |\xi_j|=1.
\]
If the effective chiral curvature is
\[
\mathcal R_j^{\epsilon_j}
=\Lambda\,\kappa_j\otimes\kappa_j+\delta\mathcal R_j,
\]
then an image component of the corrected direction can be solved from
\[
\Lambda a_j+
\langle\kappa_j,\delta\mathcal R_j\,\xi_j\rangle=0.
\]
The remaining equation is precisely
\[
\Pi_{K_j}\delta\mathcal R_j\,\Pi_{K_j}\xi_j=0.
\]
Thus the response relevant to a nearby branch is a symmetric \(2\times2\) form on \(K_j\), not a scalar evaluated on \(e_1\).

For a source \(i\), the Eguchi–Hanson term satisfies
\[
H_i^4(t_i\xi_i)=t_i^2H_i^4(\xi_i),
\]
by Proposition 1.16. Let \(\bar h_i^4(\xi_i)\) be the globally projected solution with this singular asymptotic, fixed by Bianchi gauge and orthogonality to \(\ker P_{g_o}\). At another node,
\[
\bar h_i^4=A_{ji,0}+A_{ji,2}+O(r_j^4).
\]
The invariant definition of the physical response is
\[
Q_{ji}^{\epsilon_j,\epsilon_i}(\xi_i)
 :=
 \left.\frac{d}{ds}\right|_{s=0}
 \mathcal R_{g_o+s\bar h_i^4(\xi_i)}^{\epsilon_j}(p_j),
\]
where the chiral block is expressed in an orthonormal frame for the perturbed metric. This definition automatically includes the constant jet \(A_{ji,0}\), chart renormalization, the quadratic jet, and gauge choices. The desired local object is then
\[
B_{ji}(\xi_i)
=\Pi_{K_j}Q_{ji}^{\epsilon_j,\epsilon_i}(\xi_i)\Pi_{K_j}
\in\operatorname{Sym}(K_j).
\]

Proposition 2.10 supplies the sphere integral governing the global \(\nu_l\) components and constructs \(\bar h_i^4\); it does not directly equal \(B_{ji}\). The receiver coefficient is obtained by extracting the regular two-jet at \(p_j\) and then applying Equation (24).

### 4. What remains unproved in the proposed angular reduction

The kernel-plane target is correct, but “one angular equation” needs additional representation theory.

For
\[
\xi_j(\theta)=\cos\theta\,e_{2,j}+\sin\theta\,e_{3,j},
\]
a general projected response
\[
F_j(\theta)\in K_j
\]
gives two scalar equations:
\[
f_{j,\mathrm{rad}}(\theta)
 =\langle F_j(\theta),\xi_j(\theta)\rangle=0,
\]
\[
f_{j,\mathrm{ang}}(\theta)
 =\langle F_j(\theta),J\xi_j(\theta)\rangle=0.
\]
A single angular equation results only if the stated dihedral/reflection symmetry makes one component vanish identically or relates the two. The supplied notes do not give the generators, their actions on each \(K_j\), or the ordered transport maps between nodes. Therefore the \(D_8\)-invariant reduction is plausible but not yet derived.

The notation “\(D_8\times K\)” should also be changed because \(K\) is already used for \(\ker\mathcal R^\pm\). A group such as \(G_{\mathrm{sym}}\) can be defined by explicit generators, node permutations, and matrices
\[
U_{\gamma,j}:K_j\longrightarrow K_{\gamma j}.
\]
The equivariant ansatz is then
\[
\xi_{\gamma j}=U_{\gamma,j}\xi_j,\qquad
t_{\gamma j}=t_j.
\]
Computing the fixed subspaces of the node stabilizers determines whether the reduced equation is vector-valued or scalar-valued. Since \(H^4(\xi)=H^4(-\xi)\), the angular parameter naturally lies in
\[
S(K_j)/\{\pm1\}\cong\mathbb{RP}^1,
\]
which also belongs in the symmetry calculation.

### 5. Order bookkeeping

The order comparison in Step 93 is correct. With \(t_j=|\zeta_j|\), Ozuch’s necessary equation is
\[
t_j\lambda_k^j(\phi_j,v)
+t_j^2\mu_k^j(\phi_j,v)
=O(t_{\max}^{5/2}).
\]
A source at \(i\) produces a regular curvature response of size \(t_i^2\) at \(j\), so its contribution to the receiver equation is
\[
t_jt_i^2
\big\langle Q_{ji}(\xi_i)\xi_j,\zeta_{j,(k)}\big\rangle.
\]
At comparable equal scales this is \(O(t^3)\), whereas
\[
t^{5/2}\gg t^3\qquad (t\to0).
\]
Hence the existing estimate cannot distinguish a nonzero cubic response.

The symmetry alternative must be stated precisely: symmetry would need to make the projection of the entire uncomputed residual vanish identically through every order below three. It is not enough to observe that the estimated remainder transforms equivariantly. Otherwise one needs a refined construction giving
\[
\Pi_{K_j}\mathfrak F_j(t)
=t^3\mathcal C_j+o(t^3),
\]
preferably with an estimate \(O(t^{3+\alpha})\). Remark 2.11 of Ozuch allows logarithmic radial terms, so a refined expansion must also determine whether terms such as \(t^3\log t\) occur.

### 6. Additional mathematical issues before the cubic coefficient becomes leading

1. **The local \(t^2\) coefficient is not fully settled.**  
   Lemma 2.14 proves the radial component
   \[
   \mu_1=C\det(\mathcal R^\pm|_{\xi^\perp})
   \]
   vanishes for the rank-one product block. It does not give all transverse \(\mu_k\). After splitting
   \[
   \xi^\perp=\mathbb R\,J\xi\oplus\mathbb R\,\kappa,
   \]
   the \(\kappa\)-component can be absorbed by an order-\(t\) image correction to \(\xi\), but the \(J\xi\) component lies in the kernel plane and cannot be removed that way. Thus the precise prerequisite for a cubic kernel equation is
   \[
   \Pi_{K_j}\boldsymbol\mu_j(\xi_j)=0,
   \]
   not merely \(\mu_1=0\). Step 77 itself records that the corresponding transverse formula has not been supplied.

2. **Global \(O(t^2)\) components must be included.**  
   Proposition 2.10 gives
   \[
   \nu_l
   =3\int_{S^3/\mathbb Z_2}
     \langle H^4,V_{l,2}\rangle .
   \]
   These terms must vanish in the chosen symmetric sector or be solved jointly through an orbifold deformation \(v_2\). The scalar-decoupling statements in Step 77 are not established in the Ozuch passages reproduced here for every chirality pattern.

3. **Same-chirality pair terms have not been eliminated.**  
   The Euclidean formula
   \[
   d_{\mathbf e}\mathcal R^-(H^4(\zeta^+))
   =12\pi_{\mathrm{tr}}(\rho(\zeta)^-\otimes\rho(\zeta)^-)/r^6
   \]
   gives a local chirality split. It does not by itself show that propagation by the curved product operator produces zero \(K\)-block at every same-chirality receiver. The all-compatible Kähler–Einstein family yields identities for the full sum, including parameter relations and orbifold deformations; it does not imply pairwise vanishing. Until a preservation theorem or explicit computation is given, the cubic sum should run over all \(i\ne j\).

4. **The Step 77 commutator display has a sign/transposition error.**  
   For \(A^T=-A\) and \(R=\operatorname{diag}(\Lambda,0,0)\),
   \[
   [A,R]=AR-RA
   \]
   is symmetric, while the displayed matrix in Step 77 appears skew in its \(1a/a1\) entries. Its \(K\)-to-\(K\) block is still zero, so the stated kernel-block consequence survives.

5. **The torus and sphere Green kernels are only analogues.**  
   Ozuch’s explicit \(B_x^L\) formula belongs to the flat \(\mathbb T^4/\mathbb Z_2\) problem. A spectral sum on \(S^2\times S^2\) is not a decomposition of that lattice kernel. Moreover,
   \[
   P_{rq}=\frac{\mu_r+\mu_q}{2}-1
   \]
   is a sector-specific denominator, not a universal formula for every tensor channel. The Step 94 number
   \[
   K_{\mathrm{adj}}^{\mathrm{principal}}\approx-0.03544499598
   \]
   is therefore a round-product spectral component, not the physical \(K_j\)-restricted Ozuch coefficient.

6. **The full cubic term may contain more than pair interactions.**  
   A third-order construction can also contain self-node contributions, chart corrections, orbifold-deformation terms, and nonlinear terms generated while solving the complement. Calibration against the all-compatible family should be performed at the level of the complete cubic map, not by setting each same-chirality pair response to zero.

### 7. Sharp formulation of the coefficient and remainder problem

For each node \(p_j\), fix:

* a chiral sign \(\epsilon_j\);
* the rank-one vector \(\kappa_j^{\epsilon_j}\);
* \(K_j=(\kappa_j^{\epsilon_j})^\perp\);
* explicit orthonormal orbifold charts and transport maps;
* the projected inverse of \(P_{g_o}\) orthogonal to \(\ker P_{g_o}\).

Then establish an expansion of the projected obstruction map
\[
\Pi_{K_j}\mathfrak F_j
=
t_j^2\,\Pi_{K_j}\boldsymbol\mu_j(\xi_j)
+t_j\Pi_{K_j}
\left[
D\mathcal R_j(v_2)
+\sum_{i\ne j}t_i^2Q_{ji}(\xi_i)
+\mathcal S_j^{(2)}
\right]\xi_j
+o(t_{\max}^3).
\]
Here \(\mathcal S_j^{(2)}\) denotes every cubic-order self and chart contribution not contained in the pair fields.

The concrete mathematical target is therefore:

1. prove or compute
   \[
   \Pi_{K_j}\boldsymbol\mu_j(\xi_j)=0
   \]
   in the selected equivariant sector;

2. solve the order-\(t^2\) global equations for \(\nu_l\) and determine \(v_2\);

3. compute the complete symmetric forms
   \[
   B_{ji}(\xi_i)=\Pi_{K_j}Q_{ji}(\xi_i)\Pi_{K_j};
   \]

4. derive the explicit action of the symmetry group on nodes and \(K_j\);

5. reduce the cubic map to
   \[
   f_{\mathrm{rad}}(\theta,\mathbf r)=0,\qquad
   f_{\mathrm{ang}}(\theta,\mathbf r)=0,
   \]
   showing algebraically if one component vanishes;

6. prove an \(o(t^3)\) projected remainder estimate, including any logarithmic terms.

This formulation preserves the valid Step 93 insight—rank-one curvature forces a kernel-plane problem—while preventing the old \(e_1\) scalar response, an unproved one-variable reduction, or the coarse \(O(t^{5/2})\) estimate from being used as the physical desingularization equation.