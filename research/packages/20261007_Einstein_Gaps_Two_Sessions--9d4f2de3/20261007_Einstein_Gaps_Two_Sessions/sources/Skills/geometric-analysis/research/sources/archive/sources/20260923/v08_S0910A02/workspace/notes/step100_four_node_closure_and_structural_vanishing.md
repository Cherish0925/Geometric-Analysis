# Step 100: Four-node exchange-closure theorem and structural diagonal vanishing

Session `S0910A02`. Agent2 / Constructor. Execute.

## 1. Summary

Two results close the positive mirror at leading inter-node order:

1. **Four-node exchange-closure theorem**: Imposing all four receiver equations simultaneously closes the adjacent-balanced scale-ratio window from Step 99. The exchange symmetry between nodes within each chirality class makes their single-node feasibility windows reciprocal in the scale ratio, so they can overlap only if `r = 1` is feasible.

2. **Structural diagonal tensor vanishing**: The tensor-sector (AA+BB) cross-chirality coefficient for diagonal source pairs is identically zero. This is not a numerical coincidence but a structural identity: the cos(2φ) and sin(2φ) tensor modes at antipodal S² poles have opposite relative signs, and the SO(2) rotational symmetry of the kernel plane ensures equal contribution magnitudes, giving exact pairwise cancellation at every spectral level.

**Combined consequence**: ALL mixed chirality patterns on the positive mirror are obstructed at leading inter-node order.

## 2. Four-node exchange-closure theorem

### 2.1 Setup and adjacency

The product orbifold \((S^2\times S^2)/\mathbb Z_2\) has four \(A_1\) nodes:
\[
1 = \mathrm{NN},\quad 2 = \mathrm{NS},\quad 3 = \mathrm{SN},\quad 4 = \mathrm{SS}.
\]
Adjacent pairs (share one pole): \(\{1\text-2, 1\text-3, 2\text-4, 3\text-4\}\).
Diagonal pairs: \(\{1\text-4, 2\text-3\}\).

### 2.2 Inter-node equation at each receiver

At receiver node \(j\) with EH parameter \(\xi_j\in K_j\), the leading equation is:
\[
\sum_{i\;\text{opposite}} t_i^2\,\bigl(P_{ji}\,\xi_j + Q_{ji}\,\bar\xi_j\bigr) = 0,
\]
where \(P_{ji}\) is the isotropic (AB-sector) coefficient and \(Q_{ji}\) is the traceless (tensor-sector) coefficient, both evaluated at source scale \(u_i = |\zeta_i|^2\).

Same-chirality contributions vanish (Step 99 cross-verified). The isotropic coefficients are:
\[
c_{\rm adj} = +0.06288499464,\qquad c_{\rm diag} = -0.035453521442.
\]
The tensor traceless coefficients are:
\[
q_{\rm adj} = 0.0080049973185,\qquad q_{\rm diag} = 0\ \text{(structural identity, §3 below)}.
\]

### 2.3 Pattern-by-pattern analysis

**r = 0 (all compatible)**: No opposite pairs. \(f_4 \equiv 0\) on the compatible open locus by Tian–Yau/OSS.

**r = 1 and r = 3**: At least one node has only adjacent opposite sources.
Need \(|c_{\rm adj}| \le q_{\rm adj}\), i.e., \(0.06288 \le 0.00800\). **False**. Obstructed with margin \(0.05488\).

**Diagonal balanced \(\varepsilon = (+,-,-,+)\)**: Each node sees only adjacent opposite sources.
Same condition: \(|c_{\rm adj}| \le q_{\rm adj}\). **Obstructed** with margin \(0.05488\).

**Adjacent balanced \(\varepsilon = (+,+,-,-)\)**: Each node sees one adjacent and one diagonal opposite source. Specifically:
\[
P_1 = c_{\rm adj}\,u_3 + c_{\rm diag}\,u_4,\qquad
P_2 = c_{\rm diag}\,u_3 + c_{\rm adj}\,u_4.
\]
The feasibility condition \(|P_j| \le |Q_j|\) for node 1 at ratio \(r = u_4/u_3\) is equivalent to the condition for node 2 at ratio \(1/r\) (exchange symmetry). The intersection of feasibility sets \(S_1 \cap S_2\) is nonempty if and only if \(r = 1\) is feasible:
\[
|c_{\rm adj} + c_{\rm diag}| \le q_{\rm adj} + q_{\rm diag}.
\]
Numerically: \(0.027431 \le 0.008005 + q_{\rm diag}\), requiring \(q_{\rm diag} \ge 0.019426\).

Since \(q_{\rm diag} = 0\) (§3), this fails with margin \(0.019426\). **Obstructed**.

## 3. Structural diagonal tensor vanishing

### 3.1 Computation

The diagonal tensor coefficient was computed by running A01's validated step98/step96 spectral framework with source pair "SS" at all four convergence-ladder rungs \((\tau, L_{\max}) = (0.08, 80), (0.04, 120), (0.02, 180), (0.01, 260)\). All chirality maps (++, +−, −+, −−) in both AA and BB sectors give identically zero at every rung.

### 3.2 Cancellation mechanism

For the tensor-sector spectral sum on \(S^2\times S^2\), each angular order \(\ell_t \ge 2\) produces four tensor modes: two "seeds" (c2 and s2) in two families (electric and magnetic). The c2 and s2 modes within each family are related by a \(\pi/4\) rotation in the kernel plane \(K = \omega^\perp\).

At a node pole, the mode signs are:
- North pole: \(\mathrm{sign}_{c2} = 1\), \(\mathrm{sign}_{s2} = 1\)
- South pole: \(\mathrm{sign}_{c2} = (-1)^{\ell_t}\), \(\mathrm{sign}_{s2} = -(-1)^{\ell_t}\)

At antipodal source (South vs North receiver), these signs are **always opposite**: \((-1)^{\ell_t}\) and \(-(-1)^{\ell_t}\). The SO(2) rotational symmetry of the kernel plane ensures equal contribution magnitudes for c2 and s2 seeds. Therefore each spectral level contributes:
\[
(-1)^{\ell_t} f + \bigl(-(-1)^{\ell_t}\bigr) f = 0.
\]
This cancellation applies to all (electric, magnetic) × (m0, c2, s2 scalar) mode combinations. The vanishing is structural and exact, not numerical.

### 3.3 Why adjacent pairs survive

For adjacent pairs (e.g., NN→NS), the tensor factor's source is at the **same** pole as the receiver. Both seeds have ratio +1, so contributions reinforce rather than cancel. The scalar factor's source is at the opposite pole, providing the coupling through \((-1)^{\ell_s}\) oscillation.

## 4. Complete positive mirror status

| Pattern | Status | Margin |
|---------|--------|--------|
| r = 0 (compatible) | Undecided (f₄ = 0, KE exists) | — |
| r = 1 (one reversed) | Obstructed | 0.05488 |
| r = 2 (diagonal balanced) | Obstructed | 0.05488 |
| r = 2 (adjacent balanced) | Obstructed | 0.01943 |
| r = 3 (three reversed) | Obstructed | 0.05488 |

**ALL mixed rows are obstructed at leading inter-node order.**

The weakest link is the adjacent-balanced row at margin 0.01943.

### 4.1 Calibration cross-check

The coefficient table reproduces the known KE/non-KE dichotomy:
- Compatible pattern: all same-chirality → \(B_{\rm same} = 0\) → \(f_4 = 0\) → consistent with KE existence by Tian–Yau/OSS ✓
- Mixed patterns: cross-chirality nonzero → \(f_4 \ne 0\) → obstruction → consistent with non-Kähler/non-symplectic structure ✓

## 5. Caveats

1. **Leading order only**: Self-interaction, complement Schur, frame/projector motion, global deformation, and \(o(t^3)\) remainder (including possible \(t^3\log t\) terms) are not yet controlled.
2. **Local obstruction only**: Even a complete local theorem obstructs only the product-orbifold degeneration, not global Einstein nonexistence on \(\#_3(S^2\times S^2)\).
3. **Positive mirror only**: The negative mirror \((\Sigma_2\times\Sigma_2)/\mathbb Z_2\) with 36 nodes needs a separate coefficient computation.
4. **Dimension four only**: Higher dimensions need different obstruction mechanisms.

## 6. Files

- Data: `workspace/data/step100_four_node_closure_and_q_diag.json`
- Script: `workspace/scripts/step100_four_node_closure_and_q_diag.py`
- This note: `workspace/notes/step100_four_node_closure_and_structural_vanishing.md`
