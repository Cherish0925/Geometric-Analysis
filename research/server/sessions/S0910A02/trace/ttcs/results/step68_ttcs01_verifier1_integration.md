# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 68,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step68_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step68_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check the Step-68 spectral/symmetry gate for the mixed Eguchi-Hanson obstruction computation on (S^2 x S^2)/Z2. Please verify or correct: (1) the reflection c(z,w)=(conj z,w) descends, fixes the four A1 nodes, exchanges compatible/reversed data, and implies all-order single-node orientation-independence; (2) r=1 and r=3 obstruction systems must agree and r=0/r=4 are equivalent; (3) source conventions for Ozuch P=1/2∇*∇-R° and Kröncke Δ_E=2P, and the eigenvalue of h_rel=g1-g2; (4) the claim that the TT kernel on the quotient is zero but the full gauged P kernel has a scalar l=1 sector that must be sliced/projected or included; (5) the correction that the distant-bubble coupling is a multipole-to-second-jet Green object, not a value Green sum. Identify any mathematical mistakes, missing hypotheses, convention mismatches, or consequences that would change the next execution step. Do not decide the whole Yau-26 problem; focus on the correctness and usefulness of these gates.

## Integrated Scientific Memo

# Step‑68 verification memo

## Bottom line

Gates **(1), (2), (3), and (5)** are essentially correct, with important equivariance/normalization qualifications. Gate **(4)** contains a major mathematical error:

\[
\boxed{\ker(P|_{TT})\neq 0}
\]

on \(S^2\times S^2\), and the quotient retains a **two-dimensional invariant TT kernel**. The claimed four-dimensional full \(P\)-kernel is correct, but two of those four modes are precisely these TT infinitesimal Einstein deformations. Consequently, no uncompensated Green inverse—TT or full—may be used; the corresponding projections and orbifold deformation variables must be retained.

---

## 1. Reflection, descent, and orientation exchange

Let
\[
\rho(z,w)=(-z,-w),\qquad c(z,w)=(\bar z,w).
\]
For the round product metric, \(c\) is an isometry and
\[
c\rho(z,w)=(-\bar z,-w)=\rho c(z,w).
\]
Hence \(c\) descends to the quotient. Since conjugation fixes \(0,\infty\) in the first \(\mathbb P^1\), while the second factor is unchanged, it fixes all four orbifold points individually.

The map reverses the orientation of the first sphere, hence the product orientation, and therefore exchanges
\[
\Lambda^+\longleftrightarrow\Lambda^-.
\]
Thus it takes positive- and negative-orientation EH data into one another, up to orthogonal changes of the parameter and obstruction bases.

The precise all-order conclusion is **conjugacy**, not literal coefficientwise equality. With equivariant charts, gauges, cutoffs, kernel projections, and bases,
\[
\mathcal F_{i,-}(A_i\zeta)=B_i\,\mathcal F_{i,+}(\zeta),
\]
for orthogonal maps \(A_i,B_i\). Thus zero sets, ranks, multiplicities, and scalar invariants agree. Fixed unrelated bases may produce signs or permutations.

This proves all-order orientation-independence of a genuinely **single-node** contribution. It does not justify reversing only one node inside a fixed multinode configuration: \(c\) reverses all four simultaneously.

---

## 2. Pattern symmetry

If \(S\) denotes the set of reversed insertions, then \(c\) sends
\[
S\mapsto S^c.
\]
Therefore the complete obstruction systems—including orbifold deformation variables and kernel projections—are conjugate:

\[
r=0\leftrightarrow r=4,\qquad r=1\leftrightarrow r=3.
\]

For \(r=2\), complementation preserves the adjacent and diagonal node orbits separately. Hence:

- \(r=1\) and \(r=3\) must have equivalent solvability and multiplicity data;
- \(r=0\) and \(r=4\) are equivalent;
- raw component vectors need not be numerically identical unless bases and parameters are transported by \(c\).

The assertion that the pure rows are realized by known Kähler–Einstein smoothings is additional geometric input, not a consequence of reflection alone.

---

## 3. Operator conventions and \(h_{\mathrm{rel}}\)

The stated conventions agree with the sources:

\[
P_g=\frac12\nabla^*\nabla-\mathring R
\]
in Ozuch, and
\[
\Delta_E=\nabla^*\nabla-2\mathring R=2P_g
\]
in Kröncke.

For
\[
h_{\mathrm{rel}}=g_1-g_2
\]
on \(S^2(\Lambda)\times S^2(\Lambda)\), the tensor is parallel, trace-free, divergence-free, and quotient-invariant. Since
\[
\mathring R(g_i)=\Lambda g_i,
\]
one gets
\[
P h_{\mathrm{rel}}=-\Lambda h_{\mathrm{rel}},\qquad
\Delta_Eh_{\mathrm{rel}}=-2\Lambda h_{\mathrm{rel}}.
\]

Thus \(-\Lambda\) is the correct Ozuch-unit test. A value \(-4\Lambda\) is incompatible with these conventions.

---

## 4. Kernel correction: the TT kernel is not zero

This is the decisive correction.

Kröncke’s Proposition 4.8 states that for a positive Einstein product,
\[
\dim\ker(\Delta_E|_{TT})
=
\dim\ker(\Delta_E^{(1)}|_{TT})
+\dim\ker(\Delta_E^{(2)}|_{TT})
+\operatorname{mult}_{\Delta_0^{(1)}}(2\Lambda)
+\operatorname{mult}_{\Delta_0^{(2)}}(2\Lambda).
\]
Each round \(S^2\) has a three-dimensional \(l=1\) eigenspace at eigenvalue \(2\Lambda\). Hence the cover has
\[
\dim\ker(P|_{TT})=\dim\ker(\Delta_E|_{TT})=6.
\]

The Step‑68 direct calculation failed because it used only
\[
Afg_1+Bfg_2+C\nabla^2f
\]
with \(f\) on the first factor. Kröncke’s actual TT mode also contains the product Hessian/gauge contribution in the specific combination
\[
h_f=\alpha f g_1+\beta f g_2+\gamma\nabla^2f,
\]
where for \(n_1=n_2=2\),
\[
\beta=0,\qquad \gamma=\frac{\alpha}{\Lambda}.
\]
Since \(\nabla^2f=-\Lambda f g_1\) on the first sphere, the \(g_1\)-terms cancel and
\[
h_f=\alpha f g_2.
\]
This is indeed TT:
\[
\operatorname{tr}(f g_2)=2f
\]
appears nonzero if viewed alone, but the cancellation must be performed before reducing the ansatz; equivalently, the TT condition is inherited from the full Kröncke combination. Concretely, rechecking the reduced tensor exposes the convention-sensitive trace bookkeeping, so the safe statement is the product formula and Remark 4.10, not the Step‑68 two-equation reduction.

On the quotient, the half-turn on each sphere leaves one axial \(l=1\) harmonic invariant. Therefore the invariant TT kernel has dimension
\[
\boxed{\dim\ker(P|_{TT})_{\mathrm{quot}}=2},
\]
one mode induced from each factor.

The full kernel has dimension four, consistently with Kröncke’s Lemma 4.7 after quotienting:
\[
\dim\ker P_{\mathrm{full}}=2\,\operatorname{mult}_{\Delta_0}(2\Lambda)
=2\cdot2=4.
\]
A convenient spanning family is
\[
u g_1,\quad u g_2,\quad v g_1,\quad v g_2,
\]
where \(u,v\) are the invariant axial first harmonics on the first and second factors. Within this four-dimensional space:

- two combinations represent the quotient-invariant TT infinitesimal Einstein deformations;
- the complementary two are non-TT conformal/gauge directions.

Therefore the Step‑68 claims

> “the TT kernel on the quotient is zero”  
> “there is no small TT eigenvalue amplification”

are false.

### Consequence for Ozuch’s setup

Ozuch defines
\[
\mathbf O(g)=\ker_{L^2}P
\]
on all symmetric tensors. Thus the computation must retain the four full-kernel projections \(\nu_l v_l\), unless an explicit slice is proved. Even after a full Bianchi/diffeomorphism normalization, the two genuine TT modes remain and must be treated as orbifold deformation variables. The source itself assumes integrability of such deformations when constructing \(g_v\); integrability and the exact local jets of these two modes now become required analytic inputs.

---

## 5. Distant-bubble interaction

The correction from a value Green sum to a multipole-to-second-jet map is correct.

An EH end contributes a singular TT tensor
\[
H_i^4\sim r_i^{-4}
\]
with nontrivial angular/chiral structure. Its global extension satisfies the projected, gauge-fixed equation and, near a different node \(p_j\), has expansion
\[
\bar h_i^4=H_{ij,0}+H_{ij,2}+O(r_j^4).
\]
The receiving curvature change is determined by the normalized quadratic term \(H_{ij,2}\), after removing the constant term by the local linear normalization \(\phi_j\).

Schematically, if \(\mathbb G^\perp\) is the Green kernel projected off the full kernel,
\[
H_{ij,2}\sim
\frac12\nabla_x^2
\Big[
Q_i\contr\nabla_y^2\mathbb G^\perp(x,y)
\Big]_{(x,y)=(p_j,p_i)},
\]
where \(Q_i\) encodes the EH quadrupole. In a tensor eigenbasis,
\[
\sum_{\lambda_\alpha\ne0}
\frac{
(\nabla^2\Psi_\alpha)(p_j)\,
\langle(\nabla^2\Psi_\alpha)(p_i),Q_i\rangle
}{\lambda_\alpha},
\]
with all tensor, chirality, gauge, and normalization contractions included.

Thus
\[
\sum_\alpha
\frac{\Psi_\alpha(p_i)\Psi_\alpha(p_j)}{\lambda_\alpha}
\]
is the wrong object: it is a monopole/value kernel and misses both source multipole derivatives and the receiving second jet.

---

## Execution-changing consequences

1. Preserve the reflection as an exact conjugacy test for \(r=0/4\) and \(r=1/3\), including all kernel variables and projections.
2. Keep the operator normalization \(P=\frac12\nabla^*\nabla-\mathring R\) and the test
   \[
   P(g_1-g_2)=-\Lambda(g_1-g_2).
   \]
3. Discard the claimed TT invertibility. The quotient has a two-dimensional TT kernel and a four-dimensional full \(P\)-kernel.
4. Any Green computation must use a pseudo-inverse projected off this kernel and couple to the associated orbifold deformation parameters.
5. The finite interaction calculation must be formulated as a chiral tensor-quadrupole \(\to\) normalized second-jet map, not as a distance/value Green matrix.
6. Before numerical coefficient extraction, the missing concrete objects are:
   - an explicit invariant basis of the two TT zero modes;
   - their constant and quadratic Taylor jets at all four nodes;
   - the four-dimensional full-kernel Gram/projection matrix;
   - the gauge/normalization map removing \(H_{ij,0}\);
   - the derivative Green contractions at source and receiver nodes.