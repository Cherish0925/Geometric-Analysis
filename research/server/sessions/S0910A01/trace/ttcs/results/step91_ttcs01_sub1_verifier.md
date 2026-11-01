# TTCS Independent Branch Record

```json
{
  "step_id": 91,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step91_receiver_and_adjacent_green.md",
    "Sessions/S0910A01/workspace/scripts/step91_receiver_simplification.py",
    "Sessions/S0910A01/workspace/data/step91_receiver_simplification.json",
    "Sessions/S0910A01/workspace/scripts/step91_checkerboard_radial_reduction.py",
    "Sessions/S0910A01/workspace/data/step91_checkerboard_radial_reduction.json",
    "Sessions/S0910A01/workspace/scripts/step91_corrected_spectral_ledger.py",
    "Sessions/S0910A01/workspace/data/step91_corrected_spectral_ledger.json",
    "Sessions/S0910A01/workspace/scripts/step91_adjacent_ab_heat_spectral.py",
    "Sessions/S0910A01/workspace/data/step91_adjacent_ab_heat_spectral.json",
    "Sessions/S0910A01/workspace/notes/step90_K_symmetry_cross_parity_elimination.md",
    "Sessions/S0910A01/workspace/notes/step89_correction_and_relative_green.md"
  ]
}
```

## Task

Verify the Step 91 product-orbifold calculation. Read the Step 91 note and supporting scripts/data. Check: (1) whether the product-background odd receiver really reduces to the sparse second-jet formula with no V0/frame/background-curvature correction; (2) whether the checkerboard radial reduction correctly leaves only adjacent ordered pairs in the per-receiver equations; (3) whether the corrected spectral ledger repairs the Step 90 mistakes (m-parity quotient descent, factor trace-free minimum P=2, independent degrees) while preserving P>=1 on the K-odd quotient linear sector; and (4) whether the AB one-form heat computation and its normalization are mathematically plausible as a sector calculation, including any norm/factor/sign/tail caveats. State precisely what is verified and what remains unsupported for the full Ozuch coefficient and Yau-26.

## Output

# Scientific verification memo

## Summary

The Step 91 receiver formula and checkerboard algebra are correct under the stated product-frame conventions. The spectral corrections restore the right eigenvalue lower bound \(P\ge 1\), although the trace-free tensor parity ledger still omits an \(m=0\) magnetic family and conflates first-factor and second-factor tensor modes under the fixed reflection \(K\). The AB heat computation is internally consistent as a principal-source sector calculation: its receiver, quotient norm, eigenvalue, axial normalization, and pole signs agree independently. The decimal value
\[
K_{\mathrm{adj}}^{AB}\approx-0.03144249732
\]
is numerically persuasive but is not supplied with a rigorous remainder enclosure. It is not the full Ozuch interaction coefficient.

## 1. Product-background odd receiver

Let
\[
\omega_2^+=e^{02}-e^{13},\qquad
\omega_2^-=e^{02}+e^{13}.
\]
For the unit product metric, the curvature operator is supported on \(e^{01}\) and \(e^{23}\). Hence
\[
\mathcal R_0\omega_2^\pm=0.
\]
This immediately removes the linear terms arising from variation of the orthonormal frame, Hodge decomposition, two-form length, and curvature-operator inner product: every such term contains either
\[
\langle \delta\omega,\mathcal R_0\omega_2^\pm\rangle
\quad\text{or}\quad
\langle \mathcal R_0\omega_2^\pm,\delta\omega\rangle.
\]

In fixed product normal coordinates, the lower-index Riemann variation has the second-jet part
\[
(\delta R)_{abcd}
=\frac12\left(
H_{ad,bc}+H_{bc,ad}-H_{ac,bd}-H_{bd,ac}
\right).
\]
Contracting this formula with \(\omega_2^\pm\), using the script’s normalized `/8` raw contraction and then taking half the chirality difference, gives exactly
\[
R_{\mathrm{odd}}(H)
=\frac12\left(
H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01}
\right).
\]
The exact `Fraction` calculation on the \(10\times10=100\) symmetric Hessian basis confirms every coefficient and finds only the four displayed entries.

The remaining zeroth-jet curvature terms also vanish. Linear variation of index raising or of the tensor basis replaces one index in a product-curvature component. For the mixed components selected by \((e^{02},e^{13})\), no one-index replacement produces either a \(0101\) or \(2323\) component. The support calculation in `step91_receiver_simplification.py` verifies this directly. First jets do not enter the fixed-coordinate Riemann variation at a background normal-coordinate origin; converting partial second derivatives to covariant ones only introduces curvature times \(h(0)\), already removed by the preceding support argument.

Thus the sparse formula is valid for the fixed-node linear odd curvature receiver at the product background. The JSON field `depends_on_V0_or_V1: false` is metadata rather than a symbolic computation over general \(V_0,V_1\), but the geometric argument above supplies the missing justification.

The \(\ell=1\) census is also consistent: for the nine tensors
\[
(*dX_A),(*dY_A),(*dZ_A)
\quad\odot\quad
(*dX_B),(*dY_B),(*dZ_B),
\]
only \((*dZ_A)\odot(*dZ_B)\) has the required mixed first derivatives, giving \(R_{\mathrm{odd}}=1\) in the Step 89 convention.

## 2. Checkerboard radial reduction

For
\[
\varepsilon=(1,-1,-1,1),
\qquad
\Delta_i=t_i\sum_jt_j^2(\varepsilon_i\varepsilon_j-1)K_{ij}^{11},
\]
the multiplier is

- \(0\) when \(i=j\);
- \(0\) for \(NN\leftrightarrow SS\) and \(NS\leftrightarrow SN\);
- \(-2\) precisely when the nodes differ in one factor.

Therefore the eight surviving ordered pairs are exactly
\[
NN\leftrightarrow NS,\quad NN\leftrightarrow SN,\quad
NS\leftrightarrow SS,\quad SN\leftrightarrow SS.
\]
The four displayed per-receiver equations in the note follow directly and are correct.

Reduction to one scalar \(K_{\mathrm{adj}}\) is conditional on consistent source frames, receiver frames, orientation conventions, and the relevant node/factor symmetries. The checkerboard script records that identification as a hypothesis; it does not itself prove it. The per-receiver system remains the primary object. Summing over receivers would discard information when the \(t_i\) are unequal.

## 3. Corrected spectral ledger

The three principal repairs are correct.

### Quotient descent

The orbifold generator is the simultaneous rotation
\[
(\phi_A,\phi_B)\mapsto(\phi_A+\pi,\phi_B+\pi),
\]
so a product harmonic transforms by
\[
(-1)^{m_A+m_B}.
\]
Descent is therefore controlled by azimuthal \(m\)-parity, not by \(\ell\)-parity.

### Mixed AB block

For exact or coexact one-forms generated by degree-\(\ell\) scalar harmonics,
\[
\nabla^*\nabla\alpha=(\ell(\ell+1)-1)\alpha.
\]
The product mixed tensor has \(\mathring R=0\), hence
\[
P=\frac{\ell_A(\ell_A+1)+\ell_B(\ell_B+1)}2-1.
\]
Since \(\ell_A,\ell_B\ge1\), its minimum is \(P=1\) at \((1,1)\). Treating the two degrees independently is essential and Step 91 does so.

### Factor trace-free block

A degree-\(\ell_F\) trace-free tensor harmonic has rough eigenvalue
\[
\ell_F(\ell_F+1)-4,
\]
while \(\mathring R=-1\) on that block. Therefore
\[
P=\frac{\ell_F(\ell_F+1)+\ell_O(\ell_O+1)}2-1.
\]
With \(\ell_F\ge2\), the minimum is \(P=2\).

There are, however, two residual parity-bookkeeping defects in the executable ledger:

1. For \(m=0\), the magnetic tensor harmonic
   \[
   T_{\ell0}^{B}
   =\operatorname{sym}_0\nabla(*dY_{\ell0})
   \]
   is nonzero for \(\ell\ge2\). Since \(K\) reverses orientation on the first sphere,
   \[
   K^*(*dY_{\ell0})=-*dY_{\ell0},
   \]
   so \(T_{\ell0}^{B}\) is \(K\)-odd and descends. Thus a first-factor trace-free \(K\)-odd mode already occurs at \(\ell=2,m=0\), not only at \(m=2\). Its eigenvalue is still \(P=2\).

2. A trace-free tensor supported on the second sphere and multiplied by a constant on the first is \(K\)-even, because the fixed \(K\) acts only on the first factor. The ledger label `AA_or_BB_factor_tracefree` therefore merges two different \(K\)-parity situations. Factor interchange converts \(K_A\) into the analogous \(K_B\); it does not preserve the same fixed reflection operator.

Neither defect changes the lower bound. Indeed, values below \(1\) can arise only in the scalar/parallel block: constants have \(P=-1\) and are \(K\)-even, while \(P=0\) requires one \(\ell=1\) scalar factor. A \(K\)-odd \(\ell=1\) harmonic on the first sphere has odd \(m_A\) and does not descend when the other factor is constant; modes supported only on the second sphere are \(K\)-even. Consequently,
\[
\boxed{P\ge1}
\]
on the \(K\)-odd quotient-descending linear tensor sector. A complete electric/magnetic tensor-harmonic decomposition is not encoded in the script, but the blockwise eigenvalue argument establishes the bound.

## 4. AB heat calculation

### Receiver and norm

For
\[
h=\alpha_A\otimes\beta_B+\beta_B\otimes\alpha_A
\]
without a factor \(1/2\), write
\[
A_{ab}=\partial_b\alpha_a,\qquad
B_{\mu\nu}=\partial_\nu\beta_\mu.
\]
Substitution into the sparse receiver gives
\[
R_{\mathrm{odd}}(h)
=-\frac12\left(A_{01}B_{10}+A_{10}B_{01}\right),
\]
exactly as implemented.

If the generating scalar harmonics have full-sphere \(L^2\)-norm one, then
\[
\|\alpha\|^2=\ell_A(\ell_A+1),\qquad
\|\beta\|^2=\ell_B(\ell_B+1).
\]
The unaveraged symmetric product has full-cover norm
\[
2\ell_A(\ell_A+1)\ell_B(\ell_B+1).
\]
Orbifold integration halves this for an invariant mode, giving
\[
\|h\|_{\mathcal O}^2
=\ell_A(\ell_A+1)\ell_B(\ell_B+1),
\]
which is the code’s denominator. Using a symmetrization convention with an extra \(1/2\) would change this factor, so the unaveraged convention must remain explicit.

### Pole harmonics and parity

Only scalar modes with \(m=0\) or \(m=2\) have a nonzero Hessian at a pole. Modes with \(m=1\) have a linear leading term and zero Hessian there; modes with \(m>2\) vanish to higher order. Thus the mode selection is complete for this receiver.

The south-pole frame \((X,-Y)\) is positively oriented. In that frame the script’s signs
\[
m=0,c2:\quad (-1)^\ell,\qquad
s2:\quad-(-1)^\ell
\]
are correct. They follow from antipodal parity together with the reversal of the second local coordinate.

### Axial normalization

For the unnormalized axial tensor
\[
h=(*dZ_A)\odot(*dZ_B),
\]
one has
\[
P h=h,\qquad
\|h\|_{\mathcal O}^2=\frac{64\pi^2}{9},\qquad
R_{NN}=1,\quad R_{NS}=-1.
\]
Using
\[
S_{\mathrm{odd}}=\frac{\pi^2}{2}R_{\mathrm{odd}}
\]
therefore gives
\[
\frac{\pi^2}{2}\frac{R_{NN}R_{NS}}{\|h\|_{\mathcal O}^2}
=-\frac9{128}.
\]
With heat regularization this becomes \(-9e^{-\tau}/128\), exactly matching every table entry. This independently verifies the source factor, quotient norm, eigenvalue, and adjacent sign within the Step 89 principal convention.

### Structure of the full AB sum

The four \(m=2\) polarization contributions cancel degree by degree for the adjacent pair under the chosen pole frames. Thus the total AB result reduces to the \(m=0\), coexact–coexact series
\[
K_\tau^{AB}
=\frac1{512}
\sum_{\ell,k\ge1}
(-1)^k
\frac{(2\ell+1)(2k+1)\lambda_\ell\lambda_k}
{\frac12(\lambda_\ell+\lambda_k)-1}
e^{-\tau[\frac12(\lambda_\ell+\lambda_k)-1]},
\qquad
\lambda_\ell=\ell(\ell+1).
\]
This formula reproduces the axial term at \(\ell=k=1\).

Using
\[
\frac{e^{-\tau p}}p=\int_\tau^\infty e^{-sp}\,ds,
\]
the series becomes
\[
K_\tau^{AB}
=\frac1{512}\int_\tau^\infty e^s A(s)B(s)\,ds,
\]
where
\[
A(s)=\sum_{\ell\ge1}(2\ell+1)\lambda_\ell e^{-s\lambda_\ell/2},
\]
\[
B(s)=\sum_{k\ge1}(-1)^k(2k+1)\lambda_k e^{-s\lambda_k/2}.
\]
Here \(B(s)\) is an antipodal differentiated heat kernel and has exponential small-time decay, while \(A(s)\) has only polynomial growth. This gives a direct mathematical reason for existence of the \(\tau\downarrow0\) Abel value and explains why the ladder is already nearly constant at \(\tau=0.2\).

The reported value
\[
K_{\mathrm{adj}}^{AB}\approx-0.03144249732
\]
is therefore mathematically plausible and strongly supported by the data. The `last_10_ellA_shell_abs_sum` is not a rigorous two-variable remainder estimate: the summation over \(\ell_B\) occurs before taking the absolute value, and it does not quantify the \(\tau\downarrow0\) error. No interval enclosure or analytic numerical bound accompanies the decimal. The very large thermal cutoffs make fixed-\(\tau\) truncation error plausibly tiny, but that precision is empirical.

## 5. What remains unsupported

The files do not determine the full Ozuch coefficient. Missing mathematical identifications include:

- the actual ALE sphere-flux source and its sign relative to the equation \(Ph=S\);
- isotropy normalization at the orbifold nodes;
- cutoff and Bianchi corrections;
- projection associated with the chosen pseudo-inverse and zero modes;
- AA and BB tensor contributions, together with any scalar-sector completion induced by gauge correction;
- possible \(H_2^4\)-type terms when lower-order obstructions are present;
- frame-normalized proof that every ordered adjacent coefficient is the same \(K_{\mathrm{adj}}\);
- a projected nonlinear radial expansion with remainder \(o(t^3)\), needed to isolate the \(t_i t_j^2\) interaction from the existing \(O(t_{\max}^{5/2})\) estimate.

Other sectors may alter or cancel the AB value, so neither its sign nor its nonzero size transfers yet to the complete radial coefficient. These calculations concern one local, symmetric desingularization construction near the product orbifold. They provide no existence or nonexistence result for Einstein metrics on \(\#_3(S^2\times S^2)\), and they do not establish or refute the stated Yau–26 proposition.