# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 72,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step72_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step72_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently examine the computational linear algebra in the Step-72 scripts and outputs for hidden subspace/projection mistakes. Focus on the anti-J degree-2 coefficient space (dimension 60), the rank-20 (dE0,dN1) constraints, degree-2 Hamiltonian gauge rank 35, the five-dimensional quotient, the construction of Wphys=(I-GG^T)Z2, and the least-squares lower corrections. Determine whether the output values support a genuine rank-five map to P6/P8 and nonzero radial row, or whether basis normalization, inconsistent constraints, or coordinate gauge could create it. State concrete additional checks that would distinguish these possibilities without requiring a full new formal theory.

## Integrated Scientific Memo

## Verification memo: Step-72 degree-2 quotient and corrected compatibility map

**Finding.** The supplied code and outputs support a five-dimensional degree-2 quotient and a numerically robust rank-five matrix for the **particular minimum-coefficient-norm lifts selected by Step 72**. They do **not** establish a section-independent rank-five map from that quotient into \(P_6/P_8\), nor an intrinsic nonzero radial response.

At \(K=8\), the supplied Step-71 data give a stronger, decisive conclusion: higher-jet variations with \(H_2\) fixed and all lower linearized Einstein equations preserved already map onto the entire \(84\)-dimensional \(P_8\) target. Consequently, all five Step-72 output columns—including their radial components—can be canceled by alternative admissible lower corrections. This is a freedom-of-lift issue, not evidence that the five-dimensional degree-2 quotient itself is spurious.

### 1. The degree-2 projection is internally sound

Write
\[
V_2=\mathbb R^6\otimes \operatorname{Sym}^2(\mathbb R^4)^*,
\qquad \dim V_2=6\binom53=60,
\]
and
\[
A_2=
\begin{bmatrix}dE_0\\dN_1\end{bmatrix}\Big|_{V_2}.
\]
Both outputs report
\[
\operatorname{rank}A_2=20,\qquad \dim\ker A_2=40.
\]

`gauge_basis(T,2)` constructs metric variations from quartic Hamiltonians. There are \(\binom73=35\) such monomials, and its reported rank is \(35\). Importantly, it returns **left singular vectors**, not raw Hamiltonian columns. Thus \(G_2\) has orthonormal columns in the script’s Euclidean coefficient norm, and
\[
P_\perp=I-G_2G_2^T
\]
is the appropriate orthogonal projector.

The containment needed for the construction is strongly supported:
\[
\|A_2G_2\|_F\simeq 8.0\times10^{-15},\qquad
\|A_2W_{\rm phys}\|_F\simeq 5\text{--}8\times10^{-15}.
\]
If \(G_2\subset\ker A_2\) exactly, and \(Z_2\) is an orthonormal basis of that kernel, then
\[
\operatorname{im}\bigl((I-G_2G_2^T)Z_2\bigr)
=\ker A_2\cap G_2^\perp,
\]
which has dimension \(40-35=5\). Its nonzero singular values are exactly five ones; the remaining 35 are zero. This gives a particularly simple missing spectral certificate.

The reported \(H_2\)-block Frobenius norm \(\sqrt5\simeq2.23607\) also agrees with five orthonormal columns. Rotating those columns cannot create rank or radial norm: it right-multiplies the output matrix by an orthogonal matrix.

Two qualifications:

* `gauge_projection_residual` measures reconstruction of the flat Hamiltonian metric variations in the anti-\(J\) basis. It does **not** directly measure gauge–kernel containment or projector accuracy.
* Dimension five alone does not identify this quotient with \(W^-(0)\). A direct curvature extraction would establish that identification.

There is no visible degree-2 projection mistake in the supplied evidence.

### 2. The decisive ambiguity is the choice of higher corrections

Use notation distinct from \(A_2\):
\[
A=[A_p\;\;A_h]
=\begin{bmatrix}dE_0\\dE_2\\ \vdots\\dE_{K-2}\end{bmatrix},
\qquad
J=[J_p\;\;J_h]=P_KdE_K,
\]
where \(p\) denotes the \(H_2\) block and \(h\) denotes \(H_4,\ldots,H_K\). Set \(X=W_{\rm phys}\).

The script selects
\[
H_0=-A_h^+A_pX,\qquad
Y=J_pX+J_hH_0.
\]
Here \(A_h^+\) is the pseudoinverse with `rcond=1e-12`, using the unweighted Euclidean norm of raw coefficients. Although the docstring says corrections are found “successively,” the implementation solves **one globally stacked least-squares problem**.

The residuals support approximate consistency:
\[
\|A[X;H_0]\|_F=
\begin{cases}
3.10\times10^{-11},&K=6,\\
1.11\times10^{-8},&K=8,
\end{cases}
\]
with relative residuals \(3.04\times10^{-15}\) and \(4.14\times10^{-14}\).

But minimum norm selects one lift; it does not make all admissible lifts equivalent under \(J\). If \(N_h\) is an orthonormal basis of \(\ker A_h\), every other exact lift is
\[
H_C=H_0+N_hC,\qquad
Y_C=Y+BC,\qquad B=J_hN_h.
\]
Thus the correction-independent output lies in
\[
P_K/\operatorname{im}B.
\]
Its rank is
\[
r_{\rm new}=\operatorname{rank}[B\;\;Y]-\operatorname{rank}B,
\]
not generally \(\operatorname{rank}Y\). The radial row is independent of the correction choice only if
\[
\ell^TB=0.
\]

To descend further from \(H_2\) representatives to the Hamiltonian quotient, one must also check the fully prolonged gauge variations. Removing a flat gauge block in \(H_2\) is not, by itself, that check.

### 3. The supplied \(K=8\) fibre calculation already resolves the unrestricted lift question

At \(K=8\), Step 71 and Step 72 use the same named base jet and the same higher variables
\[
h=(H_4,H_6,H_8).
\]
Step 71 imposes \(E_2,E_4,E_6\); Step 72 additionally includes \(E_0\). By jet order, \(dE_0\) has no higher-block contribution, so the Step-71 tangent space is precisely \(\ker A_h\), subject to verifying that expected zero block in the implementation.

The target uses degree-six scalar monomials, hence has dimension
\[
\dim P_8=\binom93=84.
\]
The supplied output gives
\[
\dim\ker A_h=736,\qquad \operatorname{rank}(J_hN_h)=84.
\]
This is not a marginal self-relative rank: the displayed smallest singular value is \(0.005041\), versus the rank threshold
\[
10^{-8}(361.976)\simeq3.62\times10^{-6}.
\]
Accordingly, within the reported numerical resolution,
\[
\operatorname{im}B=P_8,\qquad r_{\rm new}=0.
\]

In particular, one can solve \(BC=-Y\) and obtain
\[
A[X;H_0+N_hC]\simeq0,\qquad
J[X;H_0+N_hC]\simeq0
\]
without changing any of the five \(H_2\) directions.

The radial ambiguity is independently explicit:
\[
\|\ell^TB\|_2=0.925981,\qquad
\|\ell^TY\|_2=522.637.
\]
For radial cancellation alone, put \(b=\ell^TB\), \(r=\ell^TY\), and choose
\[
C_{\rm rad}=-\frac{b^Tr}{bb^T}.
\]
Because \(N_h\) is orthonormal, the minimum Frobenius norm of this higher-jet adjustment is
\[
\|N_hC_{\rm rad}\|_F
=\frac{\|r\|_2}{\|b\|_2}
\simeq564.4.
\]
The selected Step-72 higher correction has norm about \(9.37\times10^3\). Thus cancellation is algebraically available without an adjustment disproportionately large relative to the existing correction, although these are coefficient norms, not geometric norms.

No corresponding unrestricted \(K=6\) fibre output is supplied. Its correction-independent rank and radial response remain undetermined.

### 4. What the large singular values establish—and what they do not

The matrices \(Y\) have singular values

| Order | Largest | Smallest | Ratio |
|---|---:|---:|---:|
| \(K=6\) | \(5792.12\) | \(2304.01\) | \(0.398\) |
| \(K=8\) | \(206078.64\) | \(42087.25\) | \(0.204\) |

These support rank five for the computed sections, far from the script’s rank cutoff. They do not look like five singular values created merely by roundoff in the degree-2 projector.

Nevertheless:

* Changing the coefficient norm changes the minimum-norm section and can therefore change \(Y\) by \(BC\). An orthogonal basis rotation does not; a general coefficient reweighting can.
* The correction norms depend substantially on the order:
  \[
  \|H_4\|_F:\ 382.6\ (K=6)\quad\text{versus}\quad37.3\ (K=8).
  \]
  These are not a nested, order-consistent family of selected lifts.
* Nullspace decisions use relative cutoffs near \(10^{-9}\), while the correction solve uses \(10^{-12}\). Small modes may therefore be classified differently.
* A small lower residual alone does not bound the error in \(Y\). That requires conditioning information for \(A_h\) and error control for \(J\).

The large output values cannot be interpreted as invariant geometric sizes or “expected derivative growth” from the supplied material alone.

### 5. Torsion and coordinate-gauge interpretations require correction

Step 72 imposes
\[
\delta N_1=0,
\]
not \(N_1=0\), and not \(\delta N_3=\delta N_5=\cdots=0\). Its directions preserve the first Nijenhuis coefficient to first order; the phrase “torsion-free directions” is stronger than the actual constraints.

The Step-71 output distinguishes the issue:

| Fixed-\(H_2\) subspace | Target rank | Radial norm |
|---|---:|---:|
| Only \(H_8\) varies | 28 | \(7.55\times10^{-10}\) |
| Lower blocks in flat gauge spans | 28 | \(3.64\times10^{-9}\) |
| \(dN_3=dN_5=0\) | 69 | \(3.01\times10^{-9}\) |
| Unrestricted lower-equation tangent | 84 | \(0.925981\) |

Thus higher corrections **do** access the radial row when higher torsion is allowed to vary. The current radial value cannot be attributed uniquely to \(H_2\).

For a fixed-\(H_2\) vector, the Step-71 constraints \(dN_3=dN_5=0\) use the full Jacobians, including lower-jet contributions. They are not merely diagonal “principal-block” constraints. These results suggest that imposing additional torsion constraints could remove the radial ambiguity, but Step 72 has not tested solvability or the resulting response under those additional constraints.

Other assertions not justified by the sources:

* Hamiltonian symplectomorphisms need not be biholomorphisms of \(J_0\). Tensorial pullback covariance and jet order explain the relevant gauge behavior; preservation of \(J_0\) is not needed.
* `Tower.Evec` is imported but absent. It cannot be asserted to return only six anti-\(J\) components. The surrounding scripts explicitly anticipate ten symmetric-tensor components. Consequently, no separate constraint rank such as \(\operatorname{rank}dE_0=6\) is established.
* Testing `OM` and `OM.T` does not resolve a Darboux-convention mismatch: for a skew matrix they differ only by sign and generate the same span.

### 6. Concrete additional computations

The following checks resolve the outstanding questions without a new formal theory.

**A. Certify the degree-2 subspaces.** Record the spectra of \(A_2\), the raw Hamiltonian matrix, and \(W=(I-GG^T)Z_2\), together with
\[
\|G^TG-I\|,\quad
\|(I-Z_2Z_2^T)G\|,\quad
\|G^TW_{\rm phys}\|.
\]
Expect five singular values of \(W\) near one and 35 near zero. Record separate \(dE_0,dN_1\) ranks without presupposing their values. Verify higher-block derivatives of \(E_0,N_1\) vanish.

**B. Compute the correction-independent output directly.** For both orders form \(N_h,B,Y\), report
\[
\operatorname{rank}B,\quad r_{\rm new},\quad
\|(I-U_BU_B^T)Y\|,\quad \|\ell^TB\|,
\]
where \(U_B\) spans \(\operatorname{im}B\). Construct \(C=-B^+Y\) and report both
\[
\|A[X;H_0+N_hC]\|,\qquad
\|J[X;H_0+N_hC]\|.
\]
The supplied \(K=8\) results predict cancellation of all five columns.

**C. Check consistency and conditioning.** Report the retained singular spectrum of \(A_h\), order-by-order lower residuals, and the left-nullspace obstruction
\[
L^TA_pX,
\]
where \(L\) spans \(\ker A_h^T\). Repeat with a common cutoff and a short cutoff sweep. Weighted coefficient solves should be compared through the correction-independent output, not only through raw singular values.

**D. Test a torsion-preserving lift.** Augment the correction equations by
\[
(dN_q)_hH=-(dN_q)_pX
\]
for the desired higher odd degrees. These right-hand sides must include the \(H_2\) contributions. Determine first whether all five lifts exist. Then recompute the restricted fibre image and radial ambiguity. This directly tests whether a radial response survives after higher torsion is genuinely held fixed.

**E. Identify curvature and actual gauge.** Extract linearized curvature at the origin from the quadratic metric variation and project to the trace-free operator on \(\Lambda^-\). Check that the map annihilates \(G_2\) and has rank five on \(W_{\rm phys}\), with orientation conventions stated. Separately differentiate actual Hamiltonian pullbacks through degree \(K\), convert their metric variations into \(H=\log g\) coefficients, and evaluate the full constraints and compatibility derivative. Print base Einstein residuals, since a pullback derivative contains \(\mathcal L_XE\) when the base is only approximately solved.

A nonlinear test can subsequently check integrability of these tangent directions, but it does not by itself resolve the lift ambiguity. Even a direct finite-difference test must compare
\[
R(x_0+\varepsilon\,\mathrm{Resp})-R(x_0)
=\varepsilon Y+O(\varepsilon^2)
\]
for the **same chosen section**.

### Bottom line

The degree-2 arithmetic and projector are well supported. The rank-five \(P_6/P_8\) matrices are real numerical features of the selected least-norm lifts, not visibly projector leakage. **At \(K=8\), however, their entire output is removable by admissible fixed-\(H_2\) corrections; the supplied evidence rules out interpreting that matrix as an intrinsic unrestricted quotient-to-\(P_8\) map.** For \(K=6\), the missing object is \(J_h(\ker A_h)\). A stronger geometric claim requires specifying and testing additional constraints—most naturally higher-torsion preservation and fully prolonged coordinate gauge—rather than relying on minimum coefficient norm.