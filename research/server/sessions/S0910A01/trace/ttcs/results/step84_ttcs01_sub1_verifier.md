# TTCS Independent Branch Record

```json
{
  "step_id": 84,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step84_corrections_and_matched_control.md",
    "Sessions/S0910A01/workspace/data/step84_chirality_angular_difference.json",
    "Sessions/S0910A01/workspace/data/step84_chirality_obstruction_projection.json",
    "Sessions/S0910A01/workspace/scripts/step84_chirality_obstruction_projection.py",
    "Sessions/S0910A01/workspace/notes/step79_angular_rho_and_tilt_repair.md",
    "Sessions/S0910A01/workspace/notes/step81_L_exchange_and_radial_ledger.md"
  ]
}
```

## Task

Verify the chirality H^4 angular difference finding for the (S²×S²)/Z₂ product-orbifold Einstein desingularization.

The computation claims:
1. For Ozuch's angular map rho_x(zeta)_j = x^T(zeta^+ ∘ omega_j^-)x/|x|², using insertion direction zeta = omega_2:
   - H⁴(zeta⁺) = -Σ_j rho_j · (omega_2⁺ · omega_j⁻) / (2r⁴)
   - H⁴(zeta⁻) = -Σ_j rho_j · (omega_j⁺ · omega_2⁻) / (2r⁴)

2. The cross-compositions C[j,k] = omega_j⁺ · omega_k⁻ satisfy C[j,k] ≠ C[k,j] for j≠k, making H⁴_+ ≠ H⁴_- as symmetric 2-tensors.

3. The Gram matrices for the radial obstruction O_1 coupling are:
   - Same chirality: tr(C[1,j]·C[1,k]) = 4·delta_{jk}
   - Cross chirality: tr(C[j,1]·C[1,k]) = 4·delta_{j,1}·delta_{k,1}
   So same-chirality couples to all rho components equally, while cross-chirality couples only to rho_2.

4. The pointwise chirality difference in the obstruction overlap is 4(rho_1² + rho_3²) = 4(1 - rho_2²), with S³ mean exactly 8/3.

5. This means c_opp ≠ c_same at the H⁴ angular level: the inter-node Green response is genuinely chirality-dependent.

Please verify:
(a) The Ozuch source formulas for H⁴ in both chiralities (Prop 1.16 vs Section 1.2.3)
(b) Whether C[j,k] = C[k,j] or not (the key algebraic question)
(c) The Gram matrix computation and its interpretation
(d) Whether any cancellation in the Green-projected integral could restore chirality independence
(e) The mathematical significance: does nonzero 8/3 mean the mixed-chirality nearby-orbifold Einstein construction is genuinely obstructed?

## Output

# Scientific verification memo

## Main findings

1. **Ozuch’s two \(H^4\) formulas are consistent with the supplied source excerpts**, but the two chiralities use two different angular coefficient vectors in a fixed oriented frame.
2. **\(C[j,k]\neq C[k,j]\) for \(j\neq k\)**. Self-dual and anti-self-dual endomorphisms commute, but exchanging their basis labels is a different operation.
3. **The two Gram matrices and the raw mean \(8/3\) are exact** in the quaternion-normalized basis used by the scripts.
4. The script reuses the \(+\)-chirality angular vector for the \(-\)-chirality tensor. This makes its displayed pointwise formula for \(H^4_+-H^4_-\) source-inaccurate, although the radial Gram result and its \(8/3\) mean survive because only the common second component contributes.
5. **The raw \(8/3\) does not establish \(c_{\rm opp}\neq c_{\rm same}\)**. Those coefficients contain the global Lichnerowicz Green transfer, projections, frame transport, and receiver extraction.
6. Consequently, the mixed-chirality desingularization has **not** yet been shown to be obstructed.

---

## 1. Ozuch formulas and the two angular maps

Write
\[
P_a=\omega_a^+,\qquad M_b=\omega_b^-,
\qquad C_{ab}=P_aM_b,
\]
with \(a,b\in\{1,2,3\}\), and choose insertion direction \(P_2\) or \(M_2\).

The supplied excerpts from Ozuch, recorded in `step79_angular_rho_and_tilt_repair.md` and `step84_corrections_and_matched_control.md`, give
\[
H^4(P_2)
=-\frac{\rho_x(P_2)^-\circ P_2}{2r^4},
\qquad
H^4(M_2)
=-\frac{M_2\circ\rho_x(M_2)^+}{2r^4}.
\]

In a fixed frame, define
\[
p_j(x)=\frac{x^TC_{2j}x}{|x|^2},
\qquad
q_j(x)=\frac{x^TC_{j2}x}{|x|^2}.
\]
Then the source-correct expansions are
\[
H^4_+(x)=-\frac1{2r^4}\sum_jp_j(x)C_{2j},
\qquad
H^4_-(x)=-\frac1{2r^4}\sum_jq_j(x)C_{j2}.
\]

Thus the symbol \(\rho_j\) in the two displayed formulas must denote different orientation-swapped angular maps. It cannot denote the same three functions in both formulas.

For the basis used in `step84_chirality_obstruction_projection.py`,
\[
\begin{aligned}
p_1&=-2(x_1x_4+x_2x_3),\\
p_2&=-(x_1^2-x_2^2+x_3^2-x_4^2),\\
p_3&=2(x_1x_2-x_3x_4),
\end{aligned}
\]
whereas
\[
\begin{aligned}
q_1&=2(x_1x_4-x_2x_3),\\
q_2&=p_2,\\
q_3&=-2(x_1x_2+x_3x_4).
\end{aligned}
\]
For example, at \(x=2^{-1/2}(1,1,0,0)\),
\[
p=(0,0,1),\qquad q=(0,0,-1).
\]
Therefore the script’s use of one `rho_vec` for both chiralities does not give the literal fixed-frame tensor difference.

Nevertheless, \(H^4_+\neq H^4_-\) generically remains true. Also, `step81_L_exchange_and_radial_ledger.md` establishes
\[
L^*H^4_-(Lx)=H^4_+(x)
\]
for the orientation-reversing single-factor antipodal map. Hence their inequality under the identity frame identification is not an intrinsic scalar chirality invariant; frame transport matters.

---

## 2. Exact cross-composition algebra

Self-dual and anti-self-dual skew endomorphisms commute:
\[
P_aM_b=M_bP_a.
\]
It follows that \(C_{ab}\) is symmetric:
\[
C_{ab}^T=M_b^TP_a^T=M_bP_a=P_aM_b.
\]

Quaternionic multiplication gives the exact orthogonality relation
\[
\boxed{\operatorname{tr}(C_{ab}C_{cd})
      =4\,\delta_{ac}\delta_{bd}.}
\]
Thus the nine \(C_{ab}\) form an orthogonal basis of \(S^2_0(\mathbb R^4)\), agreeing with `cross_basis_rank = 9` in the JSON artifact.

For \(a\neq b\), \(C_{ab}\) and \(C_{ba}\) are distinct orthogonal tensors. In the script’s zero-based indexing,
\[
C[0,1]-C[1,0]
=
\begin{pmatrix}
0&0&0&2\\
0&0&0&0\\
0&0&0&0\\
2&0&0&0
\end{pmatrix},
\]
so the asymmetry is exact.

The distinction is:

- \(P_aM_b=M_bP_a\): reverse the **order of composition**;
- \(C_{ab}\) versus \(C_{ba}\): exchange the **self-dual and anti-self-dual basis labels**.

Only the first equality follows from the commuting \(\Lambda^+\) and \(\Lambda^-\) actions.

---

## 3. Gram matrices and the exact \(8/3\)

Strip off the common factor \(-1/(2r^4)\) and set
\[
A_+(x)=\sum_jp_jC_{2j},\qquad
A_-(x)=\sum_jq_jC_{j2}.
\]
The leading radial tensor at a \(+\)-receiver is proportional to \(A_+\).

The same-chirality Gram matrix is
\[
\operatorname{tr}(C_{2j}C_{2k})=4\delta_{jk}.
\]
The cross-chirality matrix is
\[
\operatorname{tr}(C_{j2}C_{2k})
=4\delta_{j2}\delta_{k2}.
\]
Therefore
\[
\langle A_+,A_+\rangle=4\sum_jp_j^2=4,
\]
while
\[
\langle A_-,A_+\rangle
=4q_2p_2=4p_2^2.
\]
Here \(|p|=|q|=1\) and \(q_2=p_2\). Consequently,
\[
\boxed{
\langle A_+,A_+\rangle-\langle A_-,A_+\rangle
=4(1-p_2^2)=4(p_1^2+p_3^2).
}
\]

The spherical average is exact. For \(x\) uniform on \(S^3\),
\[
\mathbb E[(x^TAx)^2]
=\frac{2\operatorname{tr}(A^2)+(\operatorname{tr}A)^2}{4(4+2)}.
\]
Taking \(A=C_{22}\), with \(\operatorname{tr}A=0\) and
\(\operatorname{tr}(A^2)=4\), gives
\[
\mathbb E[p_2^2]=\frac13.
\]
Hence
\[
\boxed{
\mathbb E_{S^3}\bigl[4(1-p_2^2)\bigr]=\frac83.
}
\]
The JSON value `2.668056634...` is the Monte Carlo approximation to \(8/3\).

### Normalization point

The number \(8/3\) is the average after removing the factors in \(H^4\) and in the radial mode. From the asymptotic formula quoted in Step 81,
\[
\mathbf o_1^+(x)=\frac{A_+(x)}{r^4},
\qquad
H^4_+(x)=-\frac{A_+(x)}{2r^4}.
\]
Thus the corresponding literal overlap difference is, up to the chosen sign of the radial functional,
\[
-\frac{2(1-p_2^2)}{r^8},
\]
whose mean is
\[
-\frac{4}{3r^8}.
\]
Other normalizations multiply this by a common constant. Therefore \(8/3\) is a useful dimensionless Gram numerator, not the actual coefficient \(c_{\rm opp}-c_{\rm same}\).

The JSON entry `mean_Delta_sq_analytic = 5.3361...` is also based on the sampled correlation matrix. Its exact stripped value is
\[
\mathbb E\|A_+-A_-\|^2
=8\left(1-\frac13\right)=\frac{16}{3}.
\]

---

## 4. Green projection can erase or cancel this local distinction

An inter-node coefficient has the schematic form
\[
c_{\epsilon_i\epsilon_j}
=
\ell_{i,\epsilon_i}
\Bigl(
G_P\,\Pi\,S_{j,\epsilon_j}
\Bigr),
\]
where:

- \(S_{j,\epsilon_j}\) is the complete Bianchi-corrected source near node \(j\);
- \(\Pi\) removes the full kernel components in the selected slice;
- \(G_P\) is the pseudo-inverse of Ozuch’s operator on the quotient;
- \(\ell_{i,\epsilon_i}\) extracts the normalized radial coefficient at node \(i\).

The calculation producing \(8/3\) instead uses an identity tensor pairing at the same angular point. For distinct nodes, the Green kernel has separate source and receiver angular variables:
\[
\iint_{S^3\times S^3}
p_j(x)\,K_{jk}(x,y)\,p_k(y)\,d x\,d y.
\]
The local \(8/3\) corresponds only to a very special identity-type transfer.

Several supplied facts show why global equality remains possible:

- Step 81 gives exact orientation-reversing transport between \(H^4_+\) and \(H^4_-\).
- `step84_chirality_angular_difference.json` records zero tensor difference along all three listed node directions.
- The product Green operator includes the surviving shape mode with eigenvalue \(<0\), even scalar responses, gauge terms, and matching terms; no positivity property forces the raw pointwise sign to survive.
- The angular source itself is an \(\ell=2\) field. The scalar \(8/3\) appears only after multiplying source and receiver fields at the same angular variable.

Thus the local algebra proves that some linear functionals can distinguish the two tensors. It does not prove that the specific global Green-transfer functional does so.

A decisive mathematical object would be the \(9\times9\) source-to-receiver matrix obtained by expanding the Bianchi-corrected source in the \(C_{ab}\) basis, applying the product \(S^2\times S^2\) spectral pseudo-inverse, and extracting the receiver curvature block with the transported radial normalization.

---

## 5. Consequence for the mixed Einstein branch

The nonzero \(8/3\) alone does **not** show
\[
c_{\rm opp}-c_{\rm same}\neq0,
\]
and therefore does not yet show an obstruction to the mixed filling.

Conditionally, if the full projected calculation establishes
\[
F_{\rm mixed}(t)
=2(c_{\rm opp}-c_{\rm same})t^3+o(t^3),
\qquad c_{\rm opp}-c_{\rm same}\neq0,
\]
after all tilts, deformation variables, gauge corrections, and possible logarithmic terms are included, then there is no sufficiently small positive zero along that equal-scale \(G\)-equivariant branch. Even that result would concern this nearby-orbifold branch, not every Einstein metric on \(\#_3(S^2\times S^2)\).

The verified scientific content is therefore:

\[
\boxed{\text{Local chirality tensors and their identity-pairing Gram forms differ.}}
\]

The still unresolved statement is:

\[
\boxed{\text{Whether the global projected coefficients }c_{\rm opp}
\text{ and }c_{\rm same}\text{ differ.}}
\]