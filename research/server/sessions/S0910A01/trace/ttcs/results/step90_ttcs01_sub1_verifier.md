# TTCS Independent Branch Record

```json
{
  "step_id": 90,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step90_K_symmetry_cross_parity_elimination.md",
    "Sessions/S0910A01/workspace/data/step90_K_symmetry_chirality_exchange.json",
    "Sessions/S0910A01/workspace/data/step90_K_symmetry_H4_transport_fix.json",
    "Sessions/S0910A01/workspace/notes/step89_correction_and_relative_green.md",
    "Sessions/S0910A01/workspace/notes/step88_four_node_structural_theorem.md"
  ]
}
```

## Task

Verify the K-symmetry argument for the product orbifold (S^2 x S^2)/Z_2 desingularization. K(z,w) = (bar(z), w) is complex conjugation on the first sphere, identity on the second. The central claims to verify are:

1. K fixes all four A_1 nodes (NN, NS, SN, SS), has tangent DK = diag(1,-1,1,1), det = -1, and commutes with sigma, A, J.

2. K^* maps omega_2^+ to omega_2^- with sign +1, hence exchanges the positive and negative Eguchi-Hanson models at each node.

3. Cross-parity vanishing: if S_j^1 = (S_j^+ - S_j^-)/2 is K-odd and L_i^0 is K-even, then L_i^0 G_tau S_j^1 = 0 for ALL node pairs (i,j), including diagonal. This eliminates all even-odd and odd-even interactions.

4. Geometric annihilation: q = g_A - g_B is K-even (because K preserves both metrics), hence K-parity orthogonality gives <S_j^1, q> = 0 at the full geometric level, not just the flat V_2 level. Similarly for the four scalar Ozuch zero modes.

5. The relative mixed-minus-all-same interaction reduces to off-diagonal odd-odd terms only. Diagonal odd-odd terms vanish by epsilon_i^2 - 1 = 0. No singular self-subtraction is needed.

Critically examine: (a) whether the Bianchi correction and gauge terms in the Ozuch construction respect K-equivariance, (b) whether there could be additional negative TT modes in the K-odd sector beyond the known K-even mode q, (c) the exact mechanism by which K acts on the linearized curvature functional (receiver).

## Output

# Scientific verification memo

## 1. Geometry of \(K\)

Write
\[
\sigma(z,w)=(-z,-w),\qquad
J(z,w)=(\bar z,\bar w),
\]
and let \(A\) be the diagonal antipodal map
\[
A(z,w)=\left(-\frac1{\bar z},-\frac1{\bar w}\right),
\]
as indicated by the node-orbit structure in the supplied notes. Then
\[
K(z,w)=(\bar z,w)
\]
satisfies
\[
K\sigma=\sigma K,\qquad KJ=JK,\qquad KA=AK.
\]
For example,
\[
KA(z,w)=\left(-\frac1z,-\frac1{\bar w}\right)=AK(z,w).
\]

Complex conjugation fixes \(0,\infty\in\mathbb {CP}^1\), hence \(K\) fixes every point
\[
NN,\ NS,\ SN,\ SS.
\]
In a \(K\)-adapted orthonormal tangent frame, with the first two directions tangent to the first sphere,
\[
DK=\operatorname{diag}(1,-1,1,1),\qquad \det DK=-1.
\]
Thus \(K\) descends through the \(\sigma\)-quotient and reverses the product orientation. The displayed matrix depends on the chosen normal frames, but the determinant and exchange of \(\Lambda^2_+\) with \(\Lambda^2_-\) are intrinsic.

## 2. Action on self-dual and anti-self-dual forms

Let \(e^0,e^1\) be a coframe on the first sphere and \(e^2,e^3\) one on the second, chosen so that
\[
K^*e^0=e^0,\quad K^*e^1=-e^1,\quad
K^*e^2=e^2,\quad K^*e^3=e^3.
\]
With the convention
\[
\begin{aligned}
\omega_1^\pm&=e^{01}\pm e^{23},\\
\omega_2^\pm&=e^{02}\mp e^{13},\\
\omega_3^\pm&=e^{03}\pm e^{12},
\end{aligned}
\]
one obtains
\[
K^*\omega_1^+=-\omega_1^-,
\qquad
K^*\omega_2^+=\omega_2^-,
\qquad
K^*\omega_3^+=\omega_3^-.
\]
Thus the transport matrix from \(\Lambda^2_+\) to \(\Lambda^2_-\) is
\[
\operatorname{diag}(-1,1,1),
\]
and the chosen insertion direction \(\omega_2\) is exchanged with sign \(+1\).

The algebra in `step90_K_symmetry_H4_transport_fix.json` is sufficient to prove the \(H^4\) transport, independently of the random samples. If
\[
K C_{2j}K=t_jC_{j2},\qquad (t_1,t_2,t_3)=(-1,1,1),
\]
then pullback includes both evaluation at \(Kx\) and conjugation of the tensor:
\[
\begin{aligned}
(K^*H^4_+)(x)
&=K H^4_+(Kx)K\\
&=-\frac12\sum_j
\bigl(x^TKC_{2j}Kx\bigr)\,KC_{2j}K\\
&=-\frac12\sum_jt_j^2
\bigl(x^TC_{j2}x\bigr)C_{j2}
=H^4_-(x).
\end{aligned}
\]
The same covariance is reported for \(O_1\).

This proves exchange of the leading ALE coefficient and radial kernel mode. Exchange of the complete Eguchi–Hanson metrics additionally uses the marked-ALE covariance identity
\[
\widetilde K^{\,*}\operatorname{eh}_{\omega_2^+}
=\operatorname{eh}_{\omega_2^-},
\]
for a lift \(\widetilde K\) compatible with the two asymptotic markings. The supplied artifacts do not contain the explicit lift or the full metric formula; they establish \(H^4\) and \(O_1\), not every ALE coefficient. If the EH family is defined through the standard \(O(4)\)-equivariant marked construction, the identity follows directly.

## 3. Exact source and receiver parity

Let \(U=K^*\). On orbifold tensors and tensor distributions, \(U\) is a unitary involution. Since the product metric is \(K\)-invariant,
\[
UP=PU.
\]
Any spectral or heat regularization of the form
\[
G_\tau=f_\tau(P)(I-\Pi_{\ker P})
\]
also commutes with \(U\), because the orthogonal kernel projection is \(K\)-invariant.

For the Ozuch sphere-pairing source, the \(H^4\) covariance and invariance of the Riemannian surface density give
\[
S_j^+(Uh)=S_j^-(h),\qquad
S_j^-(Uh)=S_j^+(h).
\]
There is no extra orientation sign: the pairing uses the Riemannian density rather than an oriented volume form. Consequently
\[
US_j^0=S_j^0,\qquad US_j^1=-S_j^1.
\]

The receiver transformation follows from naturality of linearized curvature. At a fixed node \(p_i\), let
\[
A_2=\Lambda^2(DK_{p_i}).
\]
Then
\[
D\mathcal R_{\bar g}[Uh]
=A_2^{-1}\,D\mathcal R_{\bar g}[h]\,A_2.
\]
For
\[
L_i^\pm(h)
=\frac{\langle\omega_2^\pm,
D\mathcal R_{\bar g}[h]\omega_2^\pm\rangle}
{|\omega_2^\pm|^2},
\]
the relation \(A_2\omega_2^+=\omega_2^-\) yields
\[
L_i^+(Uh)=L_i^-(h),\qquad
L_i^-(Uh)=L_i^+(h).
\]
Hence
\[
L_i^0U=L_i^0,\qquad L_i^1U=-L_i^1.
\]
The sign of \(A_2\omega_2^+\) would disappear in this quadratic curvature contraction even under another compatible frame convention.

It now follows algebraically that
\[
\begin{aligned}
L_i^0G_\tau S_j^1
&=L_i^0UG_\tau S_j^1
=L_i^0G_\tau US_j^1\\
&=-L_i^0G_\tau S_j^1=0,
\end{aligned}
\]
and similarly
\[
L_i^1G_\tau S_j^0=0.
\]
This applies to every ordered pair \((i,j)\), because \(K\) fixes both nodes rather than permuting them. For \(i=j\), the identities hold for every \(\tau>0\), before any singular limit is considered.

## 4. Bianchi correction, cutoffs, and gauge

The standard geometric ingredients can preserve this equivariance:

\[
\mathcal B_{\bar g}(Uh)=U\mathcal B_{\bar g}(h),
\qquad
\delta_{\bar g}^*(U\alpha)=U\delta_{\bar g}^*\alpha,
\]
and therefore
\[
(\mathcal B_{\bar g}\delta_{\bar g}^*)U
=U(\mathcal B_{\bar g}\delta_{\bar g}^*).
\]
Radial cutoffs \(\chi(d_{\bar g}(p_i,\cdot))\) are \(K\)-invariant because every \(p_i\) is fixed. Spectral inverses, orthogonal projections, and uniquely normalized Bianchi solutions commute with \(K\). The same is true for a DeTurck construction relative to the \(K\)-invariant product metric.

Three concrete pieces must match for the full Ozuch construction:

1. local charts satisfying a relation of the form
   \[
   K\circ\Phi_i^+=\Phi_i^-\circ\widetilde K;
   \]
2. \(K\)-invariant kernel complements and center-fixing normalizations;
3. equivariant treatment of \(H_2^4\), frame corrections, and every gauge vector field.

The supplied scripts verify the flat \(H^4/O_1\) transport but do not exhibit these chart and gauge identities. Thus the full-geometric parity statement is mathematically available with standard natural choices, while its implementation in the specific Ozuch/Biquard chart remains undocumented here.

There is also an order distinction. For the linear pairwise inter-node layer, each \(S_j^\pm\) is constructed on the \(K\)-invariant orbifold background, so the parity theorem applies exactly. A complete multibubble approximate metric with chirality vector \(\epsilon\) instead obeys
\[
K^*\widetilde g_\epsilon=\widetilde g_{-\epsilon};
\]
a fixed mixed assignment is generally not itself \(K\)-invariant. Higher nonlinear terms can involve products such as \(\epsilon_j\epsilon_k\), so they require their own parity decomposition and are not all represented by a single-node expression \(S_j^0+\epsilon_jS_j^1\).

## 5. Geometric annihilation and the spectrum of \(P\)

The parity argument gives, for every \(K\)-even smooth mode \(\psi\),
\[
\langle S_j^1,\psi\rangle
=\langle US_j^1,U\psi\rangle
=-\langle S_j^1,\psi\rangle=0.
\]
In particular,
\[
K^*(g_A-g_B)=g_A-g_B.
\]
Also \(Z_A\), \(Z_B\), \(g_A\), and \(g_B\) are all \(K\)-invariant, so
\[
Z_Ag_A,\quad Z_Ag_B,\quad Z_Bg_A,\quad Z_Bg_B
\]
are \(K\)-even. Their full pairing with a genuinely \(K\)-odd source vanishes, not merely its flat \(V_2\) contribution.

The concern about other TT modes with eigenvalue below zero can in fact be resolved directly for the stated operator. Decompose any symmetric tensor upstairs as
\[
h=f g_A+k_A+m+\ell g_B+k_B,
\]
where \(k_A,k_B\) are traceless within their sphere blocks and \(m\) is mixed. On the unit product,
\[
\begin{aligned}
P(fg_A)&=\left(\frac12\Delta f-f\right)g_A,\\
Pk_A&=\frac12\nabla^*\nabla k_A+k_A,\\
Pm&=\frac12\nabla^*\nabla m,
\end{aligned}
\]
with identical formulas for the \(B\)-block. Therefore:

- eigenvalues below zero occur only for constant scalar coefficients;
- among trace-free divergence-free tensors, this gives only
  \[
  q=g_A-g_B,\qquad Pq=-q;
  \]
- the zero scalar-block modes come from product scalar eigenvalue \(2\).

On the \(\sigma\)-quotient, the scalar eigenvalue-\(2\) functions that descend are \(Z_A,Z_B\). Both are \(K\)-even, giving exactly the four displayed Ozuch zero modes after multiplication by \(g_A\) or \(g_B\).

More strongly, on the \(K\)-odd quotient sector:

- scalar block coefficients have scalar eigenvalue at least \(4\), hence \(P\)-eigenvalue at least \(1\);
- traceless block tensors satisfy \(P\ge1\);
- mixed tensors have rough-Laplacian eigenvalue at least \(2\), hence again \(P\ge1\).

Thus
\[
\boxed{\quad P\big|_{\text{\(K\)-odd quotient tensors}}\ge1.\quad}
\]
This includes the TT subspace. There are no additional modes with eigenvalue \(\le0\) in that sector, and the observed axial Killing–Killing mode at eigenvalue \(1\) realizes the lower endpoint. Positivity of this operator does not by itself fix the sign of individual off-diagonal Green-kernel entries.

## 6. Relative interaction and diagonal cancellation

After the cross sectors vanish, the common-regularized mixed-minus-all-plus response is
\[
\Delta_\epsilon(\tau)
=\sum_{i,j}a_i b_j
(\epsilon_i\epsilon_j-1)K_{ij}^{11}(\tau).
\]
For \(i=j\),
\[
\epsilon_i^2-1=0,
\]
so the odd–odd diagonal term is identically absent for every \(\tau>0\). The cross-sector diagonal terms are already zero by parity. Therefore
\[
\Delta_\epsilon(\tau)
=\sum_{i\ne j}a_i b_j
(\epsilon_i\epsilon_j-1)K_{ij}^{11}(\tau).
\]
For \(i\ne j\), a distributional source at \(p_j\) produces a solution smooth near \(p_i\); curvature-jet evaluation there is finite. The relative quantity should be defined with the common regularization before taking \(\tau\downarrow0\), rather than as a difference of two separately undefined diagonal expressions. In that formulation no local self-term subtraction is required for this pairwise odd–odd layer.

## Overall assessment

The node geometry, \(\omega_2^+\mapsto\omega_2^-\) transport, receiver exchange, cross-parity algebra, and geometric orthogonality are mathematically sound. The product spectral decomposition strengthens the note by proving \(P\ge1\) on the \(K\)-odd quotient sector. The remaining unsupported portion is the explicit equivariant realization of the complete marked EH chart, Bianchi correction, and higher nonlinear multibubble terms. The off-diagonal reduction is exact for the regularized linear pairwise interaction, but it does not determine the sign of the resulting finite Green-kernel sum.