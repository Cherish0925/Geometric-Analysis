# TTCS Independent Branch Record

```json
{
  "step_id": 99,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step99_geometric_mode_bridge_check.md",
    "Sessions/S0910A01/workspace/notes/step98_trace_obstruction_theorem.md",
    "Sessions/S0910A01/workspace/scripts/step99_tensor_partial_jets.py",
    "Sessions/S0910A01/workspace/scripts/step99_partial_jet_exact_contract.py",
    "Sessions/S0910A01/workspace/scripts/step99_chirality_cancellation_structure.py",
    "Sessions/S0910A01/workspace/scripts/step99_exact_degree_pair_cancellation.py",
    "Sessions/S0910A01/workspace/data/step99_partial_jet_exact_contract.json",
    "Sessions/S0910A01/workspace/data/step99_exact_degree_pair_cancellation.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 99 product-orbifold bridge check. The scientific question is whether the Step 98 raw chirality calculation should be treated as a restricted implemented spectral-model mechanism and whether Step 99 legitimately strengthens it by (i) showing omitted same-factor partial tensor jets for actual electric/full-Lie magnetic m=2 tensor families contract exactly to zero with the Step96 source/receiver functionals, and (ii) showing same-chirality zeros in the implemented AA/BB tensor model arise from signed fixed-degree polarization cancellation rather than support-level absence. Read the notes/scripts/data and identify any mathematical or coding errors, normalization risks, false interpretations, or useful next proof targets. Do not decide final Yau26 status; focus on correctness of this bridge evidence and its limits.

## Output

# Scientific verification memo: Step 99 product-orbifold bridge

## Overall assessment

The corrected Step 98 description is mathematically appropriate: the scripts compute a particular heat-regularized inter-node spectral response built from the Step96 source/receiver arrays and selected AB/AA/BB mode families. They do not yet compute the complete Ozuch gluing coefficient.

Step 99 supplies two genuine strengthenings:

1. For the four implemented \(m=2\) electric/full-Lie magnetic tensor seeds, the omitted same-factor **coordinate partial jets** contract to zero with both Step96 chiral source and receiver maps.
2. The implemented AA/BB same-chirality zero is produced by cancellation among signed polarization terms, not because every individual mode pairing vanishes.

Several exactness and completeness points remain unresolved. The most important coding issue is that both “exact” scripts first reconstruct rational arrays from floating-point Step96 coefficients; their exact arithmetic therefore certifies a rational surrogate unless the Step96 coefficient arrays are independently generated symbolically.

---

## 1. Same-factor tensor-jet calculation

### 1.1 Local geometry used by the script is correct to the required order

The normal-coordinate metric in `step99_tensor_partial_jets.py`,
\[
g_{ij}
=\delta_{ij}-\frac13\bigl(r^2\delta_{ij}-x_i x_j\bigr)+O(r^3),
\]
is the correct unit-sphere expansion. Its displayed inverse and
\[
\sqrt{\det g}=1-\frac16r^2+O(r^4)
\]
are also correct to quadratic order.

The scalar expansion
\[
\psi=b\,q_2\left(1+\frac{2-\mu}{12}r^2\right)+O(r^6),
\qquad q_2=x^2-y^2\ \text{or}\ 2xy,
\]
has the correct coefficient. Indeed, using
\[
\Delta_{S^2}
=\partial_r^2+\cot r\,\partial_r+\csc^2r\,\partial_\theta^2,
\]
the degree-two term contributes \(-2q_2\), while
\(\Delta_{\mathbb R^2}(r^2q_2)=12q_2\). Thus
\[
12\alpha-2=-\mu,\qquad \alpha=\frac{2-\mu}{12}.
\]

The electric tensor
\[
E=\operatorname{Hess}\psi+\frac{\mu}{2}\psi g
\]
and magnetic tensor
\[
M=\mathcal L_{J\nabla\psi}g
\]
are implemented with enough Taylor order to recover their componentwise second derivatives at the pole. The magnetic routine includes all coordinate terms in the Lie derivative, rather than retaining only a symmetrized Euclidean derivative.

### 1.2 What the output actually establishes

For
\[
E_{c2},E_{s2},M_{c2},M_{s2},
\]
the script computes
\[
\partial_p\partial_qT_{ab}(0)
\]
as expressions in \(\mu\) and \(b\), embeds them in AA and BB, and contracts them with both chiral Step96 maps. The numerical residual
\[
1.11\times10^{-16}
\]
is fully consistent with algebraic cancellation.

The file `step99_partial_jet_exact_contract.json` reports zero in every component for:

- both AA and BB embeddings;
- both chirality choices;
- both receiver and source functionals;
- all four electric/magnetic seeds.

Because the symbolic tensor jets retain \(\mu\) and \(b\), this is stronger than testing only the degrees \(\ell=2,3,4,5,8\). Common factors such as \(f(p)\), the Taylor coefficient \(1/2\), quotient volume factors, and tensor normalization do not affect a zero contraction.

### 1.3 The “exact” certificate is conditional on rational reconstruction

`step99_partial_jet_exact_contract.py` does not import exact Step96 formulas. It applies
```python
sp.Rational(str(float(x))).limit_denominator(10**6)
```
to floating-point coefficient arrays and sets entries below \(10^{-15}\) to zero. Consequently:

- the SymPy contraction is exact for the reconstructed rational arrays;
- it is not yet an exact derivation from the geometric definitions of `RCOEFF` and `SCOEFF`;
- shared floating-point approximations can reconstruct equal surrogate coefficients and preserve a cancellation that still needs derivation from the original formulas.

A fully geometric certificate would consist of exact SymPy definitions of the chiral two-form bases, curvature variation, \(H^4\) source pairing, and receiver pairing, followed by direct generation of `RCOEFF` and `SCOEFF`. Recording the entrywise difference between those exact arrays and the current NumPy arrays would also settle the normalization correspondence.

### 1.4 Coordinate partial jet versus covariant jet

The script deliberately computes \(\partial^2T\), not \(\nabla^2T\). At a normal-coordinate origin,
\[
\nabla_p\nabla_qT_{ab}
=
\partial_p\partial_qT_{ab}
-(\partial_p\Gamma^r_{qa})T_{rb}
-(\partial_p\Gamma^r_{qb})T_{ar}
+\cdots .
\]
Thus the result applies directly only if the Step96 functional receives the quadratic coefficient of tensor **components in the same normal/Bianchi chart**. If Step96 instead expects an intrinsic covariant Hessian, the \(\partial\Gamma\cdot T\) terms must be included. Ozuch’s local expansions are coordinate expansions in a selected gauge, so use of partial jets is plausible, but that identification is not derived in the supplied Step99 files.

### 1.5 Mode completeness around a pole

Only the \(m=2\) tensor seeds are examined. This is natural because a spin-two tensor has a nonzero value at a pole only in the \(m=\pm2\) sector. The following conditional argument would make the reduction complete for the pure AA/BB sector:

- the receiver functional annihilates every same-factor tensor jet;
- it also annihilates every mixed derivative jet;
- therefore receiver response comes only from \(T(p)\operatorname{Hess}f(p)\);
- hence only tensor modes with \(T(p)\ne0\), namely the \(m=2\) plane, can enter;
- for those modes, Step99 verifies the only remaining omitted same-factor source term.

The first item is visible in `step99_tensor_partial_jets.py`. The mixed-support implementation and its data were referenced but not supplied here, so that part cannot be independently reconstructed from the present excerpt.

The arbitrary-support test also inserts one unsymmetrized component \(H_{ac,pq}=1\). A geometric metric jet is symmetric in \(a,c\) and in \(p,q\). Receiver vanishing entry by entry is stronger than needed. The interpretation that the source sees arbitrary geometric same-factor jets would be cleaner with a basis explicitly symmetrized in both index pairs.

---

## 2. Fixed-degree chirality cancellation

### 2.1 Numerical grouping supports the stated mechanism

`step99_chirality_cancellation_structure.py` computes the signed Green contribution before successively grouping by

\[
(\ell_t,\ell_s,\text{kind},\text{tensor seed},\text{scalar mode}).
\]

It uses the same tensor kind, seed, and scalar mode at source and receiver, as expected for the diagonal spectral resolution in an orthogonal real polarization basis. At fixed \((\ell_t,\ell_s)\), the heat factor and eigenvalue denominator are common to all polarizations, so they cannot create the cancellation.

The reported AA–NS example has 1800 individual same-chirality contributions above the numerical threshold, while the complete same-chirality block is zero. This directly refutes a mode-support explanation. The cancellation is among electric/magnetic and scalar polarization terms with signs coming from the chiral contractions and north/south evaluations.

### 2.2 Finite exact algebra agrees with the numerical grouping

`step99_exact_degree_pair_cancellation.py` tests 36 combinations:
\[
6\ \text{degree pairs}\times 3\ \text{node pairs}\times 2\ \text{sectors}.
\]
For every tested combination, all 16 entries of both \(++\) and \(--\) response tensors simplify to zero. The `nonzero_counts` field is computed from the full \(2^4\)-entry tensor, so this conclusion does not rely on the smaller nine-entry `compact` display.

Representative cross blocks are nonzero exactly in the expected sectors:

- AA for NS;
- BB for SN;
- no AA/BB response for SS in the displayed cases.

The scalar weight
\[
w_{m0}=\frac{2\mu}{\mu-2}
\]
is correct. With normalized scalar harmonics, the pole Hessian amplitudes obey
\[
\frac{|H_{m0}|^2}{|H_{m2}|^2}
=\frac{2\mu}{\mu-2}.
\]

The assumption that electric and full-Lie magnetic modes have equal amplitude-squared divided by global norm is also mathematically plausible. Their pole amplitudes differ by a factor two, while
\[
\|M\|_{L^2}^2=4\|E\|_{L^2}^2,
\]
so the normalized spectral weights agree.

### 2.3 What the fixed-degree file does not prove

The degree file tests selected values rather than a symbolic \((\ell_t,\ell_s)\) identity. In particular:

- no odd–odd degree pair is present;
- scalar degree \(\ell_s=1\) is omitted;
- \(\ell_s=0\) is absent from both this certificate and the displayed Step98 loop structure;
- north/south signs are encoded by `node_sign` rather than derived from explicit frame transport.

The comment that \(\ell_s=1\) “belongs to a separate AB/one-form family” needs mathematical justification. A pure AA product tensor \(T_Af_B\) with an \(\ell_s=1\) scalar factor is still a tensor-scalar mode. At a pole its \(m=0\) scalar Hessian is nonzero, while the \(m=2\) polarization does not exist. It therefore requires a separate one-polarization computation, not division by the \(m=2\) normalization.

A universal algebraic proof could treat
\[
w_0=\frac{2\mu}{\mu-2},\qquad w_c=w_s=1
\]
symbolically and replace degree parities by signs
\(\varepsilon_t,\varepsilon_s\in\{\pm1\}\). This would cover every \(\ell_t\ge2,\ell_s\ge2\) at once, with \(\ell_s=0,1\) handled separately.

As with the jet certificate, the fixed-degree script rationalizes floating-point Step96 arrays. Its exact zero is therefore exact for that reconstructed algebra. Exact generation of the source/receiver arrays remains important.

### 2.4 Cross-chirality magnitude remains numerical

The stored compact blocks change sign with scalar-degree parity: for example the AA–NS block is \(+\frac12\) for even \(\ell_s\) and \(-\frac12\) for odd \(\ell_s\), up to the displayed spin-two basis conventions. Thus the final \(0.008\)-scale tensor response is an alternating spectral sum.

At heat parameter \(\tau>0\), the implemented operator is
\[
R\,e^{-\tau P}P^{-1}S^*,
\]
not yet \(RP^{-1}S^*\). Distinct-node smoothness suggests an Abel-type \(\tau\downarrow0\) value, but derivative evaluation of the Green kernel and its tail require an estimate. Step99 strengthens the zero blocks but does not strengthen the numerical positivity margin or the \(0.008\) normalization.

---

## 3. Relation to the complete geometric interaction

Ozuch’s Proposition 2.10 identifies the orbifold-side coefficient, after the first local terms vanish, through
\[
\nu_l
=
3\int_{S^3/\mathbb Z_2}
\langle H^4,V_{l,2}\rangle .
\]
The same paper then includes deformation terms, approximate cokernel projection, ALE kernel terms, and quantitative remainders. The Step96 arrays may represent the local bilinear pairing in this formula, but Step99 does not derive that identification.

A further completeness issue is visible from the sector list. Pointwise,
\[
\operatorname{Sym}^2_0(T_A\oplus T_B)
\cong
\operatorname{Sym}^2_0T_A
\oplus
\operatorname{Sym}^2_0T_B
\oplus
(T_A\otimes T_B)
\oplus
\mathbb R(g_A-g_B).
\]
The implemented tracefree AA, BB, and AB sectors account for the first three summands. The supplied notes do not exhibit the relative-trace scalar-scalar family
\[
f_Af_B\,(g_A-g_B).
\]
Unless the Step96 maps annihilate this family, or the Step98 code includes it under another name, the model is not the full traceless symmetric-tensor Green kernel.

Other unresolved identifications are:

- exact invariant-mode projection on the \(\mathbb Z_2\) quotient;
- pole-frame transport and chirality-basis transport;
- orthogonality and normalization of electric/magnetic modes in every degree;
- subtraction of global kernel and Einstein-deformation components;
- self, complement, and moving-projector contributions;
- the \(\tau\downarrow0\) Green-kernel value and spectral tail;
- consistency with self-adjoint reciprocity after transporting node frames.

Self-adjointness gives a particularly useful normalization test: after quotient factors and frame transport, the pair map from node \(j\) to node \(i\) should be the transpose of the reversed pair map in the corresponding \(L^2\) bases.

---

## 4. Strong structural proof target

The proposed Kähler explanation is mathematically sound as a target. On a Kähler–Einstein four-manifold in complex orientation,
\[
\mathcal R^+
=
\lambda\,\Pi_{\mathbb R\omega},
\]
so its kernel is
\[
K=\Lambda^{2,0}_{\mathbb R}.
\]
For a differentiable Kähler–Einstein family,
\[
\Pi_K\,\dot{\mathcal R}^{+}\,\Pi_K=0.
\]
Movement of \(K\) contributes no \(K\)-to-\(K\) block because the background curvature operator annihilates \(K\); equivalently, the derivative of an orthogonal rank-one projector has zero block on its kernel.

This identity would explain the same-chirality cancellation at operator level if the same-chirality singular Green field, including its gauge correction and global deformation component, is tangent to such a Kähler–Einstein family. Step99’s fixed-degree zeros are strong evidence for that representation-theoretic mechanism, but membership in that tangent space is not established by the mode sums.

---

## Final scientific reading

The revised Step 98/99 notes now describe the evidence accurately. The same-factor jet computation and polarization grouping are useful and reproducible within the implemented model. The principal textual adjustment still warranted is to describe the SymPy results as exact arithmetic **after rational reconstruction of Step96 arrays**, rather than exact derivation from the geometric source/receiver formulas. The strongest mathematical advances would come from exact Step96 coefficient generation, an all-degree polarization identity including \(\ell_s=0,1\), the relative-trace sector, frame-equivariant reciprocity, and the Kähler kernel-plane identity applied to the actual singular Green solution.