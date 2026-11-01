# TTCS Independent Branch Record

```json
{
  "step_id": 72,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/step72_vary_H2_free.py",
    "Sessions/S1003A01/workspace/scripts/step71_fibre_split.py",
    "Sessions/S1003A01/workspace/scripts/step71_fibre_test.py",
    "Sessions/S1003A01/workspace/data/step72/vary_H2_free_K6.json",
    "Sessions/S1003A01/workspace/data/step72/vary_H2_free_K8.json",
    "Sessions/S1003A01/workspace/data/step71/fibre_split_K8.json"
  ]
}
```

## Task

Independently examine the computational linear algebra in the Step-72 scripts and outputs for hidden subspace/projection mistakes. Focus on the anti-J degree-2 coefficient space (dimension 60), the rank-20 (dE0,dN1) constraints, degree-2 Hamiltonian gauge rank 35, the five-dimensional quotient, the construction of Wphys=(I-GG^T)Z2, and the least-squares lower corrections. Determine whether the output values support a genuine rank-five map to P6/P8 and nonzero radial row, or whether basis normalization, inconsistent constraints, or coordinate gauge could create it. State concrete additional checks that would distinguish these possibilities without requiring a full new formal theory.

## Output

## Scientific memo

### 1. The degree-2 quotient calculation is algebraically coherent

Let
\[
V_2\simeq \mathbb R^{6}\otimes \operatorname{Sym}^2(\mathbb R^4)^*,
\qquad \dim V_2=6\binom{5}{3}=60,
\]
and let
\[
A_2=\begin{bmatrix}dE_0\\ dN_1\end{bmatrix}\bigg|_{V_2}.
\]
The reported rank \(20\) gives
\[
Z_2=\ker A_2,\qquad \dim Z_2=40.
\]
The quartic Hamiltonians have dimension \(\binom{7}{3}=35\), and `gauge_basis(T,2)` reports rank \(35\). Its SVD output has orthonormal columns in the raw coefficient Euclidean metric, so
\[
P_G=G_2G_2^T
\]
is indeed the orthogonal projector onto the computed gauge span.

The numerical inclusions are very strong:
\[
\|A_2G_2\|\simeq 8.0\times10^{-15},\qquad
\|A_2W_{\rm phys}\|\simeq 5\text{--}8\times10^{-15}.
\]
Thus, to double precision, \(G_2\subset Z_2\). Under exact containment,
\[
\operatorname{im}\bigl((I-P_G)Z_2\bigr)=Z_2\cap G_2^\perp,
\]
and therefore
\[
\dim(Z_2/G_2)=40-35=5.
\]
So the construction
```python
W = (I-G2@G2.T)@Z2
Wphys = left_singular_vectors(W)[:,:5]
```
contains no evident projection error. An arbitrary orthogonal rotation of the five columns of `Wphys` also cannot create either the rank or `radial_norm`: the output matrix merely changes by right multiplication with an orthogonal \(5\times5\) matrix.

The field named `gauge_projection_residual` measures reconstruction of the Hamiltonian metric variations in the anti-\(J\) basis; it is not a principal-angle measurement between \(G_2\) and \(Z_2\). The latter still deserves explicit output.

### 2. What the least-squares stage actually defines

Write the lower linearized equations and the projected next equation as
\[
A=[A_p\;A_h],\qquad J=[J_p\;J_h],
\]
where \(A_p,J_p\) act on \(H_2\), while \(A_h,J_h\) act on \(H_4,\ldots,H_K\). For \(X=W_{\rm phys}\), the script chooses
\[
H_0=-A_h^+A_pX
\]
using the Moore–Penrose inverse in the unweighted raw monomial coefficient norm, and reports
\[
Y=J_pX+J_hH_0.
\]

This is a well-defined map for that particular Euclidean least-norm section. It is not automatically a map determined only by the five-dimensional quotient. If
\[
N_h=\ker A_h,
\]
then every other admissible correction has the form
\[
H=H_0+N_hC,
\]
and its projected next coefficient is
\[
Y_C=Y+BC,\qquad B:=J_hN_h.
\]
Consequently, the section-independent content is the image of \(Y\) in
\[
P_K/\operatorname{im}B.
\]
Equivalently, the number of target directions contributed beyond the fixed-\(H_2\) fibre is
\[
\operatorname{rank}[B\;Y]-\operatorname{rank}B.
\]
The Step-72 script does not compute this quantity.

### 3. The supplied \(K=8\) fibre data settle this ambiguity

For \(K=8\), the Step-71 and Step-72 variables and lower equations match:

- Step 72: \(h=(H_4,H_6,H_8)\), lower equations \(E_0,E_2,E_4,E_6\);
- Step 71: \(h=(H_4,H_6,H_8)\), lower equations \(E_2,E_4,E_6\).

By jet order, \(E_0\) has zero derivative with respect to \(H_4,H_6,H_8\), so the Step-71 tangent space is precisely \(\ker A_h\). The \(P_8\) target has
\[
\dim P_8=\dim\{\text{degree-6 polynomials in four variables}\}
=\binom{9}{3}=84.
\]
The supplied fibre output gives
\[
\dim\ker A_h=736,\qquad
\operatorname{rank}(J_hN_h)=84.
\]
This full row rank is numerically well separated from the stated threshold: the largest singular value is \(361.98\), the smallest displayed tail value is \(0.00504\), while the script threshold is about \(3.62\times10^{-6}\).

Therefore, at \(K=8\),
\[
\operatorname{im}B=P_8.
\]
For every Step-72 response \(Y\), including all five columns simultaneously, there is a fixed-\(H_2\) lower-jet variation \(N_hC\) such that
\[
B C=-Y.
\]
The altered responses keep the same five \(H_2\) directions and satisfy the same lower linearized equations, but have
\[
J(\,X,H_0+N_hC\,)=0.
\]

Thus the singular values
\[
206078.6,\ 113047.9,\ 80698.9,\ 55702.3,\ 42087.3
\]
show a robust rank-five matrix for the chosen Moore–Penrose section, but they do not define a nonzero map from the five-dimensional \(H_2\) quotient into \(P_8\). In the quotient \(P_8/\operatorname{im}B\), the induced image is zero.

The same conclusion is especially transparent for the radial row. Step 71 gives
\[
\|\ell^T B\|=0.925981\neq0,
\]
while Step 72 gives
\[
\|\ell^T Y\|=522.637.
\]
Hence the radial value can be changed while \(H_2\) and all lower equations remain fixed. The minimum Euclidean fibre adjustment needed merely to cancel this row has Frobenius norm
\[
\frac{522.637}{0.925981}\approx564.4,
\]
whereas the reported Step-72 \(K=8\) correction already has total higher-block norm about
\[
\sqrt{37.3^2+6327.5^2+6906.9^2}\approx 9.37\times10^3.
\]
So radial cancellation is not only algebraically available; its coefficient size is moderate relative to the selected correction.

For \(K=6\), no corresponding fixed-\(H_2\) fibre rank is supplied. The five singular values \(2304\)–\(5792\) and radial norm \(165.6\) establish a robust matrix for the selected least-norm section, but they do not determine
\[
\operatorname{rank}[B_6\;Y_6]-\operatorname{rank}B_6
\quad\text{or}\quad
\ell^TB_6.
\]
The \(P_6\) target has dimension \(\binom{7}{3}=35\), so this computation is small compared with the existing \(K=8\) calculation.

### 4. Basis normalization and conditioning

The five-dimensional quotient itself is invariant under invertible coefficient changes. The reported amplitudes and the least-norm lift are not.

The script minimizes the ordinary Euclidean norm of raw coefficients across different polynomial degrees and monomials. Rescaling from ordinary monomial coefficients to derivative-normalized Taylor coefficients, or assigning separate weights to \(H_4,H_6,H_8\), changes the Moore–Penrose section by an element of \(\ker A_h\). At \(K=8\), where \(J_h(\ker A_h)=P_8\), such a change can alter the target by an arbitrary element of \(P_8\).

There is already visible section dependence in the output:

- \(K=6\): \(\|H_4\|=382.6\), \(\|H_6\|=674.8\);
- \(K=8\): \(\|H_4\|=37.3\), \(\|H_6\|=6327.5\), \(\|H_8\|=6906.9\).

The same degree-2 quotient is being lifted, but adding the \(E_6\) equation and \(H_8\) variables changes the global least-norm representative drastically.

There is also a threshold mismatch:

- nullspaces and reported ranks use relative thresholds near \(10^{-9}\);
- `np.linalg.lstsq` uses `rcond=1e-12`.

Modes between \(10^{-9}\sigma_{\max}\) and \(10^{-12}\sigma_{\max}\) are treated as null in one place and invertible in another. The relative residuals are excellent, but the inferred right-hand-side norms are large:
\[
\|A_pX\|\approx1.02\times10^4 \quad(K=6),
\qquad
\|A_pX\|\approx2.68\times10^5 \quad(K=8).
\]
Together with the large correction norms, this calls for the singular spectrum of \(A_h\), order-by-order residuals, and an `rcond` sweep before attaching meaning to the numerical magnitudes. It does not explain the computed rank-five matrix as floating-point noise: the five output singular values have ratios \(s_{\min}/s_{\max}\approx0.40\) and \(0.20\), far from the rank threshold.

### 5. Coordinate gauge and torsion

The degree-2 Hamiltonian gauge itself is effectively removed: its rank is \(35\), its anti-\(J\) reconstruction residual is \(10^{-13}\), and \(A_2G_2\) is \(10^{-14}\). Therefore the five-dimensional complement is not produced by simple leakage of those 35 directions.

Higher-order coordinate freedom remains among the lower-correction nullspace. A geometrically prolonged Hamiltonian pullback should be tested as a full jet vector \((\delta H_2,\delta H_4,\ldots)\), not by projecting only its \(H_2\) block and then applying a raw least-norm completion.

The Step-71 decomposition gives useful evidence about the radial component:

- `S_gauge` radial norm: \(3.64\times10^{-9}\);
- `S_Nfixed_principal` radial norm: \(3.01\times10^{-9}\);
- full fixed-\(H_2\) tangent radial norm: \(0.925981\).

Thus the large radial variability is not seen in the listed Hamiltonian-gauge subspace or when the higher principal Nijenhuis coefficients are held fixed. It enters through fixed-\(H_2\) directions that vary higher torsion data. This is scientifically important because Step 72 imposes only
\[
\delta N_1=0.
\]
That condition preserves the degree-1 Nijenhuis coefficient; it is not the same equation as \(N_1=0\), nor does it preserve \(N_3,N_5,\ldots\). The current five directions are therefore torsion-preserving at the first jet, not a full torsion-free deformation through order \(K\).

### 6. Concrete computations that distinguish the possibilities

1. **Spectral certificate for the degree-2 quotient.** Record:
   \[
   s_{20}(A_2),\ s_{21}(A_2),\qquad
   s_{35}(G_{\rm raw}),\qquad
   s_1,\ldots,s_{40}\bigl((I-GG^T)Z_2\bigr),
   \]
   together with
   \[
   \|(I-Z_2Z_2^T)G_2\|,\qquad \|G_2^TG_2-I\|.
   \]
   Exact containment predicts five singular values near \(1\) and the remaining 35 near machine precision.

2. **Direct \(W^-\) identification.** Construct the linearized curvature at the origin from the quadratic metric coefficient,
   \[
   \delta R_{ijkl}
   =\frac12\bigl(
   \partial_{jk}h_{il}+\partial_{il}h_{jk}
   -\partial_{jl}h_{ik}-\partial_{ik}h_{jl}
   \bigr),
   \]
   and project to the trace-free operator on \(\Lambda^-\), which has dimension five. Numerically,
   \[
   W^-(G_2)\simeq0,\qquad
   \operatorname{rank}\bigl(W^-(W_{\rm phys})\bigr)=5
   \]
   would identify the quotient with actual anti-self-dual Weyl curvature, rather than only by matching dimensions.

3. **Fibre-quotient computation for both orders.** With \(N_h\) an orthonormal basis of \(\ker A_h\), form
   \[
   B=J_hN_h,\qquad Y=J\,\mathrm{Resp},
   \]
   and report
   \[
   \operatorname{rank}B,\quad
   \operatorname{rank}[B\;Y]-\operatorname{rank}B,\quad
   \|\ell^TB\|.
   \]
   A direct numerical construction is:
   ```python
   Nh, sAh, rAh = null(Ah, rtol)
   B = JR[:, sl(4).start:] @ Nh
   Y = JR @ Resp
   C = torch.linalg.lstsq(B, -Y).solution
   Resp0 = Resp + torch.cat([
       torch.zeros(T.size[2], Y.shape[1], dtype=dt, device=dev),
       Nh @ C
   ], dim=0)
   ```
   The residuals `A@Resp0` and `JR@Resp0` directly exhibit whether the five outputs can be removed. The supplied \(K=8\) data predict `JR@Resp0` near zero.

4. **Consistency through the left nullspace.** If \(L\) spans the left nullspace of \(A_h\), exact solvability is equivalent to
   \[
   L^TA_pW_{\rm phys}=0.
   \]
   This is more informative than the aggregate least-squares residual and should be evaluated order by order for \(E_0,E_2,\ldots,E_{K-2}\).

5. **Coefficient-metric and cutoff sweep.** Repeating the solve with derivative-normalized monomials, separate positive weights on each \(H_d\), and `rcond` values \(10^{-8},\ldots,10^{-13}\) would show how much \(Y\), its radial row, and the correction norms depend on the selected horizontal section. The target functional \(\ell\) must transform contragrediently under any target-basis rescaling.

6. **Higher-torsion-fixed lift.** Augment the lower equations by the full linearized conditions
   \[
   \delta N_3=\delta N_5=\cdots=0,
   \]
   including their \(H_2\)-dependent right-hand sides. The Step-71 values suggest that this removes the fixed-\(H_2\) radial variability. Whether the five \(H_2\) directions still admit such lifts, and whether their radial response persists, directly separates \(W^-\) input from higher-torsion input.

7. **Full Hamiltonian prolongation.** Generate the metric-jet variation by differentiating the actual polynomial pullback under each Hamiltonian vector field, through degrees \(K\). Evaluating \(A\) and \(J\) on those full jet vectors tests coordinate invariance without relying on the Moore–Penrose completion.

8. **Base residuals.** Print
   \[
   \|E_0\|,\|E_2\|,\ldots,\|E_K\|
   \]
   at the polished jet. Gauge covariance of a linearized residual is contaminated by the underlying residual through terms of the form \(\mathcal L_XE\), so these values should be well below the effects being interpreted.

### Conclusion

The rank-\(20\), rank-\(35\), five-dimensional degree-2 quotient and the projector construction are internally well supported. The reported \(P_6/P_8\) matrices also have genuine numerical rank five for the particular unweighted Moore–Penrose lifts; they are not near-roundoff artifacts.

They do not yet define a geometric rank-five map from the five-dimensional \(H_2\) quotient. At \(K=8\), the supplied Step-71 data show that the fixed-\(H_2\) lower-correction fibre already maps onto all of \(P_8\), including the radial row. Hence the entire Step-72 \(P_8\) image, and its radial component, can be altered or canceled without changing the five \(H_2\) classes or the lower linearized equations. For \(K=6\), the corresponding fibre calculation is absent, so the section-independent rank and radial content remain undetermined.