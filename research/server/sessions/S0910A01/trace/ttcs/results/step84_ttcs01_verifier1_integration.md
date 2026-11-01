# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 84,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step84_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step84_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

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

## Integrated Scientific Memo

# Verification result

## Verdict

Claims (1)–(4) are correct **after one essential convention repair**: the two chiralities use different angular maps in a fixed oriented frame. The exact Gram difference and its normalized \(S^3\)-mean \(8/3\) survive this repair.

Claim (5) is not established. The computation proves a nonzero **local identity-pairing angular difference**, not
\[
c_{\mathrm{opp}}\ne c_{\mathrm{same}}
\]
for the globally Green-projected inter-node coefficient. Accordingly, it does not yet prove that the mixed-chirality Einstein desingularization is obstructed.

---

## (a) Ozuch \(H^4\) formulas and the angular-map correction

The supplied notes reproduce Proposition 1.16 and the orientation-reversed formula as
\[
H^4(\zeta^+)
=-\frac{\rho_x(\zeta)^-\circ\zeta^+}{2r^4},
\qquad
H^4(\zeta^-)
=-\frac{\zeta^-\circ\rho_x(\zeta)^+}{2r^4}.
\]
These are internally consistent with the asymptotic obstruction formula quoted in Steps 79 and 81. Direct primary-text verification is impossible from the bounded input because the Ozuch paper itself is not included.

Set
\[
P_a=\omega_a^+,\qquad M_b=\omega_b^-,
\qquad C_{ab}=P_aM_b,
\]
and choose insertion index \(2\). In a fixed oriented frame, the correct coefficient vectors are
\[
p_j(x)=\frac{x^TC_{2j}x}{|x|^2},
\qquad
q_j(x)=\frac{x^TC_{j2}x}{|x|^2}.
\]
Thus
\[
H^4_+(x)=-\frac1{2r^4}\sum_jp_j(x)C_{2j},
\qquad
H^4_-(x)=-\frac1{2r^4}\sum_jq_j(x)C_{j2}.
\]

The Step 84 script incorrectly inserts the same `rho_vec` into both formulas. Generally \(p\ne q\); for its basis,
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
Consequently, the script’s explicit formula for \(H^4_+-H^4_-\), its sampled difference matrices, and its \(\|\Delta\|^2\) calculation are not literal fixed-frame computations of the source formulas. The separate conclusion that the two tensors are generically unequal remains true.

Step 81 supplies an important geometric qualification:
\[
L^*H^4_-(Lx)=H^4_+(x)
\]
under the orientation-reversing single-factor antipodal map. Hence fixed-frame inequality is not itself an invariant scalar measure of chirality; source-to-receiver frame transport must be included.

---

## (b) Exact \(C_{ab}\) algebra

Self-dual and anti-self-dual skew endomorphisms commute:
\[
P_aM_b=M_bP_a.
\]
This implies each \(C_{ab}\) is symmetric:
\[
C_{ab}^{T}=M_b^{T}P_a^{T}=M_bP_a=P_aM_b.
\]

It does **not** imply \(C_{ab}=C_{ba}\). The latter exchanges the SD and ASD basis labels rather than merely reversing composition order. Indeed,
\[
\boxed{\operatorname{tr}(C_{ab}C_{cd})
=4\delta_{ac}\delta_{bd}},
\]
so the nine \(C_{ab}\) form an orthogonal basis of \(S^2_0(\mathbb R^4)\). In particular, \(C_{ab}\ne C_{ba}\) when \(a\ne b\).

For example, in the script’s zero-based notation,
\[
C[0,1]-C[1,0]
=
\begin{pmatrix}
0&0&0&2\\
0&0&0&0\\
0&0&0&0\\
2&0&0&0
\end{pmatrix}.
\]
Thus the key algebraic assertion is exactly correct.

---

## (c) Gram matrices and the exact \(8/3\)

Suppress the common \(r^{-4}\) and normalization factors and define
\[
A_+(x)=\sum_jp_j(x)C_{2j},
\qquad
A_-(x)=\sum_jq_j(x)C_{j2}.
\]
The leading \(+\)-receiver radial tensor is proportional to \(A_+\).

The orthogonality identity gives
\[
\boxed{\operatorname{tr}(C_{2j}C_{2k})=4\delta_{jk}}
\]
and
\[
\boxed{\operatorname{tr}(C_{j2}C_{2k})
=4\delta_{j2}\delta_{k2}}.
\]
Therefore the same- and cross-chirality matrices are respectively
\[
4I_3,\qquad \operatorname{diag}(0,4,0).
\]

Their correct interpretation is:

* same chirality:
  \[
  \langle A_+,A_+\rangle=4|p|^2=4;
  \]
* opposite chirality:
  \[
  \langle A_-,A_+\rangle=4q_2p_2=4p_2^2,
  \]
  because \(q_2=p_2\).

Hence the Step 84 reuse of a common angular vector is harmless for this particular radial overlap:
\[
\boxed{
\langle A_+,A_+\rangle-\langle A_-,A_+\rangle
=4(1-p_2^2)
=4(p_1^2+p_3^2).
}
\]

Quaternionic conjugation gives \(|p|=1\). Moreover,
\[
\mathbb E_{S^3}[p_jp_k]=\frac13\delta_{jk}.
\]
Equivalently, using the quadratic-form moment formula with
\(\operatorname{tr}C_{22}=0\) and \(\operatorname{tr}(C_{22}^2)=4\),
\[
\mathbb E[p_2^2]=\frac13.
\]
Thus
\[
\boxed{\mathbb E_{S^3}\!\left[4(1-p_2^2)\right]=\frac83}.
\]

This is a dimensionless Gram numerator after stripping the \(H^4\) and obstruction normalizations. Since
\[
H^4_+=-\frac{A_+}{2r^4},
\qquad
\mathbf o_1^+=\frac{A_+}{r^4}
\]
in the quoted convention, the literal normalized overlap difference has additional sign, factor, and \(r^{-8}\) terms; \(8/3\) is not itself \(c_{\mathrm{opp}}-c_{\mathrm{same}}\).

---

## (d) The Green projection can restore equality

The actual inter-node coefficient is schematically
\[
c_{\epsilon_i\epsilon_j}
=
\ell_{i,\epsilon_i}
\!\left(
G_P\,\Pi\,S_{j,\epsilon_j}
\right),
\]
where:

* \(S_{j,\epsilon_j}\) is the complete Bianchi-corrected source;
* \(\Pi\) is the gauge/kernel projection;
* \(G_P\) is the global pseudo-inverse of the product-orbifold linearized Einstein operator;
* \(\ell_{i,\epsilon_i}\) is the transported, normalized radial extraction functional.

The \(8/3\) calculation instead replaces this transfer by a same-angular-point identity pairing. For different nodes, the relevant object has two angular variables:
\[
\iint p_j(x)\,K_{jk}(x,y)\,p_k(y)\,dx\,dy.
\]
Nothing supplied proves that this kernel acts as a positive scalar multiple of the identity on the relevant angular sector.

In particular:

1. Each \(p_j\) has zero \(S^3\)-mean and lies in a degree-two angular sector. The \(8/3\) is the constant component of a **product** of angular profiles, not a monopole of \(H^4\).
2. The global operator includes tensor, even-scalar, negative shape, gauge, and matching responses.
3. The orientation-reversing symmetry transports the full \(H^4\) tensor between chiralities.
4. A Lichnerowicz resolvent is not a positive angular measure, so the pointwise nonnegativity of \(4(1-p_2^2)\) does not preclude cancellation.
5. Steps 81 and 84 have not established that the first exposed radial term is a pure \(t_i t_j^2\) coefficient rather than one involving logarithms or intervening terms.

Therefore cancellation is mathematically possible on the supplied evidence. It is neither proved nor disproved.

The decisive object is the source-to-receiver transfer matrix on the nine-dimensional basis \(\{C_{ab}\}\), including Bianchi correction, kernel projection, product spectral pseudo-inverse, node-frame transport, and radial extraction. Computing only the local Gram matrix corresponds to replacing this transfer matrix by an identity-type model.

---

## (e) Significance for mixed-chirality desingularization

The rigorous conclusion is
\[
\boxed{\text{The local }H^4\text{ angular tensors and their radial identity pairings distinguish chirality.}}
\]

The computation does **not** establish
\[
\boxed{c_{\mathrm{opp}}\ne c_{\mathrm{same}}}.
\]
Thus the nonzero \(8/3\) does not prove that the mixed-chirality nearby-orbifold Einstein construction is obstructed.

To obtain such an obstruction one would need, after all movable parameters and projections are included, a sharp expansion such as
\[
F_{\mathrm{mixed}}(t)
=
2(c_{\mathrm{opp}}-c_{\mathrm{same}})t^3+o(t^3),
\qquad
c_{\mathrm{opp}}-c_{\mathrm{same}}\ne0,
\]
or the corresponding rigorously derived logarithmic expansion. One must also justify the claimed same-chirality KE control relation in the identical Ozuch chart, including insertion directions, scale ratios, gauge, and normalization.

Even then, a nonzero leading coefficient would obstruct only the specified small, equivariant, comparable/equal-scale mixed-chirality degeneration. It would not rule out other gluing branches or an unrelated Einstein metric on \(\#_3(S^2\times S^2)\).

## Required artifact correction

The Step 84 code should use separate functions
\[
p_j=x^TC_{2j}x/|x|^2,\qquad
q_j=x^TC_{j2}x/|x|^2
\]
for the two chiralities. Its Gram matrices and \(8/3\) result remain valid, but the reported pointwise tensor difference and \(\Delta\)-norm outputs should be regenerated with this correction.