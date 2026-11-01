# TTCS Independent Branch Record

```json
{
  "step_id": 89,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step89_correction_and_relative_green.md",
    "Sessions/S0910A01/workspace/data/step89_identity_and_spectral_support.json",
    "Sessions/S0910A01/workspace/data/step89_identity_sparse_components.json",
    "Sessions/S0910A01/workspace/notes/step88_four_node_structural_theorem.md",
    "Sessions/S0910A01/workspace/data/step87_missed_killing_mode_boundary.json",
    "Sessions/S0910A01/workspace/data/step87_missed_killing_mode_receiver.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 89 correction of the product-orbifold chirality calculation. Check the corrected flat principal identity S_odd(V2)=(pi^2/2) R_odd(H) and D:H=-16 R_odd under the stated conventions; check whether the shape tensor q=g_A-g_B is indeed TT with Pq=-q and whether the principal odd source/receiver annihilation of q and scalar zero modes follows from the displayed tensor support; check the finite relative mixed-minus-all-same formulation for point-supported quadrupoles, including diagonal self-term cancellation, lack of inherited positivity, possible even/odd cross terms, and order bookkeeping t^3=o(t^(5/2)) relative to Ozuch Proposition 2.19. Please identify any remaining normalization or conceptual errors and state what is actually established versus still needing geometric/Bianchi/Ozuch matching.

## Output

# Scientific verification memo — Step 89 correction

## 1. Flat quadratic-jet identity

The corrected factor is right, provided \((\delta R^\pm)_{22}\) denotes the curvature-operator matrix coefficient in the length-\(\sqrt2\) basis \(\omega_a^\pm\).

Set
\[
A^+_{ijpq}=\sum_{k=1}^3(C_{2k})_{ij}(C_{2k})_{pq},
\qquad
A^-_{ijpq}=\sum_{k=1}^3(C_{k2})_{ij}(C_{k2})_{pq},
\qquad D=A^+-A^- .
\]
On \(S^3/\mathbb Z_2\),
\[
\int x_ax_bx_px_q\,d\sigma
=\frac{\pi^2}{24}
\bigl(\delta_{ab}\delta_{pq}
+\delta_{ap}\delta_{bq}
+\delta_{aq}\delta_{bp}\bigr).
\]
Using
\[
H_\pm^4=-\frac12 A^\pm_{ijab}x_ax_b,
\qquad
V_{2,ij}=\frac12H_{ijpq}x_px_q,
\]
and \(\operatorname{tr}C_{ab}=0\), the Ozuch surface coefficient is
\[
B^\pm=3\int_{S^3/\mathbb Z_2}\langle H_\pm^4,V_2\rangle
=-\frac{\pi^2}{16}A^\pm_{ijpq}H_{ijpq}.
\]
Consequently,
\[
\boxed{\frac{S_{\rm odd}}{\pi^2}
=\frac{B^+-B^-}{2\pi^2}
=-\frac1{32}D_{ijpq}H_{ijpq}.}
\]

The supplied sparse tensor has
\[
D:H=-8H_{01,23}+8H_{03,12}+8H_{12,03}-8H_{23,01}.
\]
For the orientation in the files, take
\[
\omega_2^\pm=e^0\wedge e^2\pm e^3\wedge e^1.
\]
Since \(|\omega_2^\pm|^2=2\), the curvature-operator matrix entry is
\[
(\delta R^\pm)_{22}
=\frac{\langle\omega_2^\pm,\delta\mathcal R\,\omega_2^\pm\rangle}
       {|\omega_2^\pm|^2}.
\]
It follows that
\[
R_{\rm odd}
=\frac{(\delta R^+)_{22}-(\delta R^-)_{22}}2
=\delta R_{0231}.
\]
The displayed Riemann convention gives
\[
R_{\rm odd}
=\frac12\left(
H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01}
\right).
\]
Termwise comparison therefore yields
\[
\boxed{D:H=-16R_{\rm odd}},
\qquad
\boxed{S_{\rm odd}(V_2)=\frac{\pi^2}{2}R_{\rm odd}(H)}.
\]

This also explains why testing the 100-dimensional space
\(\operatorname{Sym}^2\mathbb R^4\otimes\operatorname{Sym}^2\mathbb R^4\)
is sufficient.

### Remaining curvature-block normalization ambiguity

The JSON sentence “2-form block \(=\langle\omega_a,R\omega_b\rangle\) with \(1/4\) contraction” needs one clarification. With the unnormalized forms used in
\[
C_{ab}=\omega_a^+\circ\omega_b^-,
\qquad \operatorname{tr}(C_{ab}C_{cd})=4\delta_{ac}\delta_{bd},
\]
the raw pairing is twice the matrix coefficient because \(|\omega_a^\pm|^2=2\). If \((\delta R^\pm)_{22}\) were literally the raw \(1/4\)-contraction, then
\[
S_{\rm odd}=\frac{\pi^2}{4}R_{\rm odd}^{\rm raw}.
\]
Thus the corrected \(\pi^2/2\) identity uses either normalized receiver forms \(\omega/\sqrt2\), or equivalently curvature-operator coefficients in the length-\(\sqrt2\) basis. This should be stated explicitly in the TeX notation.

For the axial mode,
\[
H_{03,12}=H_{12,03}=-1,
\]
with the other two sparse components zero. Hence
\[
D:H=-16,\qquad R_{\rm odd}=1,\qquad S_{\rm odd}=\frac{\pi^2}{2},
\]
exactly matching \(B^+=\pi^2/2\), \(B^-=-\pi^2/2\).

Its quotient norm is also consistent:
\[
\|h\|^2_{(S^2\times S^2)/\mathbb Z_2}
=\frac12\,2
\left(\int_{S^2}|dZ|^2\right)^2
=\left(\frac{8\pi}{3}\right)^2
=\frac{64\pi^2}{9}.
\]
Therefore its single-eigenmode kernel coefficient is
\[
\frac{(\pi^2/2)\cdot1}{1\cdot(64\pi^2/9)}
=\frac9{128}.
\]

## 2. Shape tensor and scalar kernel modes

Let
\[
q=g_A-g_B.
\]
Because both factor metrics are parallel,
\[
\nabla q=0,\qquad \delta q=0.
\]
Since each factor is two-dimensional,
\[
\operatorname{tr}_{g_A+g_B}q=2-2=0.
\]
Thus \(q\) is TT and descends through the simultaneous rotation quotient.

For unit spheres,
\[
\mathring R(g_A)=g_A,\qquad \mathring R(g_B)=g_B,
\]
so
\[
\mathring R(q)=q,\qquad
Pq=\frac12\nabla^*\nabla q-\mathring R(q)=-q.
\]
The eigenvalue \(-1\) is therefore correct in the stated normalization.

In product normal coordinates with
\[
A=\{0,1\},\qquad B=\{2,3\},
\]
the quadratic jet of \(q\) has only \(AA;AA\) and \(BB;BB\) components. By contrast, the four entries of \(D:H\) lie in
\[
AA;BB,\qquad BB;AA,\qquad AB;AB.
\]
Hence
\[
D:H(q)=0,\qquad
S_{\rm odd}^{\rm principal}(q)=0,\qquad
R_{\rm odd}^{\rm principal}(q)=0.
\]

For quotient-invariant first spherical harmonics \(u_A,u_B\),
\[
\nabla^*\nabla u_A=2u_A,\qquad
\nabla^*\nabla u_B=2u_B.
\]
Because \(\mathring R(g_A)=g_A\) and \(\mathring R(g_B)=g_B\),
\[
P(u_Ag_A)=P(u_Ag_B)=P(u_Bg_A)=P(u_Bg_B)=0.
\]
Their principal odd contractions vanish as well. For example, \(u_Ag_B\) can produce \(BB;AA\) components, but its tensor factor at the base point is proportional to the diagonal \(B\)-metric, whereas the sparse functional requires the off-diagonal component \(H_{23,01}\). The other three tensors vanish by the same product-index argument. The exact identity then gives zero principal receiver values too.

These statements concern the flat second-derivative part. The complete curvature variation also contains background-curvature contractions, changes of the orthonormal frame, and contributions from a nonzero constant jet \(V_0\). In addition, Ozuch’s zero-mode formula contains
\[
3\int\langle H^4,V_{l,2}\rangle
+\int\langle H_2^4,V_{l,0}\rangle.
\]
Lemma 2.3 removes \(H_2^4\) when the first \(\lambda_k\) vanish in Ozuch’s specified Eguchi–Hanson coordinates. That statement directly concerns orbifold kernel modes; it does not by itself give the complete projection onto \(q\), whose \(P\)-eigenvalue is \(-1\).

## 3. Relative Green interaction

It is clearer to allow distinct receiver and source weights:
\[
a_i\quad\text{and}\quad b_j.
\]
Then
\[
\mathcal R_\epsilon(\tau)
=\sum_{i,j}a_i b_j
\left(
K_{ij}^{00}
+\epsilon_jK_{ij}^{01}
+\epsilon_iK_{ij}^{10}
+\epsilon_i\epsilon_jK_{ij}^{11}
\right),
\]
and subtraction of the all-\(+\) assignment gives
\[
\Delta_\epsilon(\tau)
=\sum_{i,j}a_i b_j
\left[
(\epsilon_j-1)K_{ij}^{01}
+(\epsilon_i-1)K_{ij}^{10}
+(\epsilon_i\epsilon_j-1)K_{ij}^{11}
\right].
\]
This algebra is correct.

For \(i=j\),
\[
\epsilon_i^2-1=0.
\]
Thus the entire odd–odd self term cancels before the regulator is removed. This is important because in four dimensions a quadrupole–Green–quadrupole pairing has local behavior
\[
\partial^4(|x-y|^{-2})\sim |x-y|^{-6},
\]
so its coincident-point value is not an ordinary finite pairing.

For \(i\ne j\), the Green kernel is smooth and the corresponding derivatives are finite once the kernel projection and source tensors are fixed. Therefore the pure odd–odd relative expression reduces to a genuine off-diagonal quantity.

The complete relative response is not automatically finite from this cancellation alone. At \(i=j\),
\[
(\epsilon_i-1)K_{ii}^{01}
+(\epsilon_i-1)K_{ii}^{10}
\]
can remain. Their disappearance requires an actual local orientation symmetry, principal-symbol orthogonality, or a matched subtraction showing that these cross pairings vanish. The flat odd source–receiver identity does not establish any of these statements for the even–odd sectors.

No sign follows from the regulated full matrix. There are two independent reasons:

1. \(P^{-1}\) is not a positive operator on all symmetric tensors because \(Pq=-q\).
2. Even for an operator whose relevant spectral denominators are above zero, subtracting coincident terms leaves an off-diagonal matrix. A nonzero symmetric matrix with zero diagonal cannot be positive semidefinite; its spectrum necessarily occurs on both sides of zero.

The axial channel remains valid. With
\[
K_{ij}^{11,\mathrm{axial}}=\frac9{128}s_is_j,\qquad \epsilon_i=s_i,
\]
one obtains
\[
(\epsilon_i\epsilon_j-1)K_{ij}^{11,\mathrm{axial}}
=\frac9{128}(1-s_is_j).
\]
It is zero for equal node signs and \(18/128>0\) for opposite node signs. This is an exact contribution from one eigenmode, not a sign determination for the complete Green interaction.

## 4. Scale bookkeeping and a weight inconsistency

Ozuch writes \(\zeta_j=t_j\phi_j\), and
\[
H^4(t_j\phi_j)=t_j^2H^4(\phi_j).
\]
A field emitted by node \(j\) therefore changes the first obstruction at node \(i\) by
\[
\delta\lambda_i=O(t_j^2).
\]
Since the radial equation contains \(t_i\lambda_i\), the inter-node term is
\[
t_i\,\delta\lambda_i=t_it_j^2\mathcal I_{ij}.
\]
For comparable scales this is \(O(t^3)\), and
\[
\frac{t^3}{t^{5/2}}=t^{1/2}\longrightarrow0.
\]
Thus Ozuch Proposition 2.19,
\[
t_i\lambda_i+t_i^2\mu_i=O(t_{\max}^{5/2}),
\]
cannot detect a coefficient at order \(t^3\). An expansion with a remainder smaller than \(t^3\) is needed to identify that interaction.

There is one notational mismatch in Step 89: the response is written with \(w_iw_j\), while Step 88 used \(w_j=t_j^2\). Keeping that meaning would make \(w_iw_j=O(t^4)\), not the radial \(O(t^3)\) term. For the Ozuch radial equations, the natural weights are
\[
a_i=t_i,\qquad b_j=t_j^2.
\]
The chirality algebra and diagonal odd–odd cancellation remain unchanged with these unequal weights, but the current \(w_iw_j\) formula is not yet normalized to the radial variables.

## 5. Precisely established content

The supplied equations and data establish:

- the flat quadratic-jet identity
  \[
  S_{\rm odd}=\frac{\pi^2}{2}R_{\rm odd},\qquad D:H=-16R_{\rm odd},
  \]
  with curvature-operator matrix normalization;
- the axial values \(S_{\rm odd}/\pi^2=1/2\), \(R_{\rm odd}=1\), and coefficient \(9/128\);
- \(q\) is TT and satisfies \(Pq=-q\);
- the principal odd source and receiver vanish on \(q\) and the four displayed scalar kernel modes;
- pure odd–odd coincident terms cancel in the mixed-minus-all-same comparison;
- the isolated axial off-diagonal contribution has the stated checkerboard sign;
- the inter-node radial contribution occurs at \(t_it_j^2\), below the precision of Proposition 2.19.

A complete geometric coefficient still depends on:

- a Bianchi-compatible global source with cutoff and curved-parametrix terms;
- the precise pseudoinverse on the chosen slice and projection away from the full kernel;
- all \(P\)-eigenspaces with eigenvalues below zero, not only \(q\);
- the full receiver including \(V_0\), frame, background-curvature, and Ozuch radial normalizations;
- a global integration-by-parts identity relating that source to that receiver;
- the even–odd and odd–even coincident terms;
- an order-\(t^3\) projected expansion with a remainder \(o(t^3)\).

Accordingly, Step 89 correctly repairs the flat algebra and the Green-kernel formulation, but it does not yet produce a geometric obstruction to Einstein desingularization or an Einstein-existence result on the resolved manifold.