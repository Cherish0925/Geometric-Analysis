# TTCS Independent Branch Record

```json
{
  "step_id": 80,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step80_J_equivariant_all_order_reduction.md",
    "Sessions/S0910A01/workspace/data/step80_J_symmetry_verification.json",
    "Sessions/S0910A01/workspace/notes/step79_angular_rho_and_tilt_repair.md",
    "Sessions/S0910A01/workspace/notes/step78_equivariant_diagonal_reduction.md"
  ]
}
```

## Task

Verify the J-symmetry all-order obstruction elimination theorem for the product orbifold (S²×S²)/⟨(r_π,r_π)⟩ with EH insertion direction ω₂. The claim is: simultaneous complex conjugation J(z,w)=(z̄,w̄) acts on the SD/ASD basis at each node as diag(-1,+1,-1), fixes ω₂ (the insertion direction), and therefore a J-equivariant Eguchi-Hanson construction has zero obstruction projections onto the J-odd directions (ω₁ and ω₃) at EVERY order of the Ozuch expansion. Combined with A-symmetry (killing scalar kernel ν_l) and the rank-one determinant (μ₁=0), this eliminates all finite-dimensional Ozuch obstructions. Check: (1) Is the J-parity argument mathematically rigorous? (2) Does J genuinely extend as an isometry of the EH metric when the insertion direction is ω₂? (3) Is the 'every order' claim correct, or could higher-order gauge/normalization issues break J-invariance? (4) Is the surviving system really balanced (2 equations in 2 unknowns)? (5) What is the strongest statement about existence that this structural result supports, and what analytical gaps remain?

## Output

# Scientific verification memo

## Overall finding

The \(J\)-parity mechanism is mathematically sound once the gluing data and gauge are chosen \(J\)-equivariantly. It gives an exact vanishing of the two \(J\)-odd bubble projections, not merely cancellation of their second-order coefficients. The EH metric does admit the required \(J\)-isometry for insertion direction \(\omega _2\).

The combination with \(A\)-symmetry and the determinant formula removes every coefficient appearing in the supplied Ozuch expansion through the \((\lambda,\mu,\nu)\) level. It does **not** remove the \(J\)-even radial bubble projection at subsequent orders. Thus Step 80 §6 is too strong if “all finite-dimensional equations” means the complete nonlinear reduced map; Step 80 §7 correctly retains radial equations.

## 1. Exact action of \(J\) on \(\Lambda^\pm\)

At any singular point choose an oriented orthonormal product coframe
\[
(e^1,e^2,e^3,e^4),
\]
with the first two covectors from the first sphere. The derivative of simultaneous conjugation is
\[
D=dJ=\operatorname{diag}(1,-1,1,-1).
\]
For the usual bases
\[
\begin{aligned}
\omega _1^\pm&=\tfrac1{\sqrt2}(e^{12}\pm e^{34}),\\
\omega _2^\pm&=\tfrac1{\sqrt2}(e^{13}\mp e^{24}),\\
\omega _3^\pm&=\tfrac1{\sqrt2}(e^{14}\pm e^{23}),
\end{aligned}
\]
one has
\[
D^*e^{12}=-e^{12},\quad D^*e^{34}=-e^{34},\quad
D^*e^{13}=e^{13},\quad D^*e^{24}=e^{24},
\]
and \(D^*e^{14}=-e^{14}\), \(D^*e^{23}=-e^{23}\). Hence
\[
J^*|_{\Lambda^+}=J^*|_{\Lambda^-}
=\operatorname{diag}(-1,+1,-1).
\]

This is an exact calculation and does not rely on the numerical samples in `step80_J_symmetry_verification.json`. At different nodes the frame labels must be transported coherently; intrinsically, the \(+1\)-eigenspace in each \(\Lambda^\pm\) is one-dimensional, and the insertion called \(\omega _2\) must be chosen in that line.

The matrices defining \(J\) and the orbifold involution \(\sigma=-I_4\) commute. Therefore \(J\) descends to the local quotient and globally to
\[
(S^2\times S^2)/\langle(r_\pi,r_\pi)\rangle.
\]

## 2. Extension of \(J\) to the Eguchi–Hanson space

The extension is genuine, but the relevant complex structure is the EH complex structure selected by \(\omega _2\), not the original product complex structure on the two spheres.

Let \(I_2\) be defined by
\[
g_{\mathrm e}(I_2X,Y)=\omega _2^+(X,Y).
\]
Since \(D\) is orthogonal and \(D^*\omega _2^+=\omega _2^+\), it follows that
\[
DI_2=I_2D.
\]
Thus \(D\) is complex linear and unitary relative to \(I_2\). Explicit \(I_2\)-complex coordinates can be taken as
\[
\xi _1=x_1+i x_3,\qquad \xi _2=x_2-i x_4,
\]
in which
\[
D(\xi _1,\xi _2)=(\xi _1,-\xi _2).
\]
This matrix lies in \(U(2,I_2)\), commutes with the central \(\{\pm1\}\), and acts on \(\mathbb C^2/\{\pm1\}\). The standard EH metric with Kähler form in the \(\omega _2\) direction is \(U(2)\)-invariant. The unitary action lifts to the minimal resolution and preserves the exceptional sphere and its size parameter. Consequently it is an exact EH isometry.

The same reasoning applies at nodes where the selected insertion belongs to \(\Lambda^-\): \(D\) fixes \(\omega _2^-\), and the EH complex structure is interpreted with the opposite ambient orientation.

Thus the sentence in Step 80 that \(J\) “acts as a Kähler isometry with respect to the \(\omega _2\) complex structure” is correct. It would be incorrect only if one used the original product complex structure, relative to which simultaneous conjugation is anti-holomorphic.

## 3. Rigorous parity of the obstruction projections

Let \(\mathcal E(g_t)\) denote either the Einstein residual
\[
\operatorname{Ric}(g_t)-\Lambda g_t
\]
or its DeTurck-gauge version formed using a \(J\)-invariant reference metric. Naturality gives
\[
J^*\mathcal E(g_t)=\mathcal E(J^*g_t).
\]
Hence an exactly \(J\)-invariant approximate metric satisfies
\[
J^*\mathcal E(g_t)=\mathcal E(g_t).
\]

The parity of the EH obstruction tensors needs one additional covariance statement, omitted from the short proof in Step 80. If \(\mathbf o_v\) denotes the infinitesimal EH mode associated with a variation \(v\) of the insertion data, then
\[
J^*\mathbf o_v=\mathbf o_{J^*v}.
\]
This follows either by differentiating
\[
J^*g_{\rm EH}(\phi)=g_{\rm EH}(J^*\phi)
\]
at \(\phi=\omega _2\), or from the standard expression of the EH kernel tensors using the \(U(2)\)-invariant \(L^2\) harmonic form and the parallel hyperkähler forms.

In the adapted ordering
\[
(\phi_{(1)},\phi_{(2)},\phi_{(3)})
=(\omega _2,\omega _1,\omega _3),
\]
the three parities are therefore
\[
(+1,-1,-1).
\]
For an obstruction pairing
\[
c_v(t)=\int \langle\mathcal E(g_t),\mathbf o_v\rangle\,dV,
\]
change of variables by \(J\) gives
\[
c_v(t)
=\int\langle J^*\mathcal E(g_t),J^*\mathbf o_v\rangle\,dV
=c_{J^*v}(t).
\]
If \(J^*v=-v\), then \(c_v(t)=-c_v(t)\), so
\[
c_{\omega _1}(t)=c_{\omega _3}(t)=0
\]
exactly.

### Higher orders and gauge choices

This reasoning is stronger than a coefficient computation: the full odd projection is identically zero as a function of the gluing parameters. Therefore every coefficient in any valid power or polyhomogeneous expansion of that projection vanishes.

Higher-order gauge choices do not force parity breaking provided that:

- the orbifold and EH charts intertwine \(J\);
- cutoffs are \(J\)-invariant;
- the DeTurck reference metric is \(J\)-invariant;
- linear corrections are chosen in the \(J\)-fixed subspace;
- kernel and cokernel normalizations respect the \(J\)-eigenspace decomposition.

The finite group \(\{1,J\}\) allows linear choices to be symmetrized by averaging. Even and odd modes are orthogonal, so Gram–Schmidt normalization can also be performed separately in the two parity spaces.

A non-equivariant coordinate or gauge selection can display odd intermediate coefficients, but those coefficients do not represent the invariant obstruction pairing above.

One qualification is textual rather than geometric: the supplied Ozuch source establishes only the finite expansion quoted in Step 79. Symmetry implies vanishing at every subsequently constructed order; it does not itself construct an infinite Ozuch expansion.

## 4. What the combined \(A+J+\det\) argument actually gives

For
\[
R^\pm=\operatorname{diag}(1,0,0),\qquad \phi_0=\omega _2,
\]
the first obstruction satisfies \(\lambda(\phi_0)=0\), since \(\omega _2\in\ker R^\pm\).

At the next displayed order:

- \(J\)-parity gives \(\mu _2=\mu _3=0\);
- the determinant formula cited from Step 76 gives \(\mu _1=0\), since \(\det R^\pm=0\);
- \(A\)-parity gives \(\nu_l=0\) for the four modes \(u_i g_j\).

Therefore every coefficient explicitly appearing in
\[
t_j\lambda_k^j+t_j^2\mu_k^j
=O(t_{\max}^{5/2}),\qquad
\nu_l=O(t_{\max}^{5/2})
\]
vanishes in the symmetric family.

The determinant argument concerns only the second-order radial coefficient \(\mu _1\). The radial obstruction tensor is \(J\)-even, so symmetry does not remove its later self-interaction, inter-node interaction, gauge response, or nonlinear response. Thus the entry in the JSON saying that all finite-dimensional obstructions vanish must be read as referring only to the displayed \((\lambda,\mu,\nu)\) coefficients. It cannot refer to the complete reduced map.

The note’s phrase “positive-definite operator with one removable mode” also needs adjustment: the \(A\)- and \(J\)-even tensor \(g_1-g_2\) has eigenvalue \(-\Lambda\). The relevant complement may still be uniformly invertible, but its spectrum has both signs; positivity of its quadratic form is unavailable.

## 5. Is the remaining problem genuinely \(2\times2\)?

There is a valid dimension count, subject to constructing the full Lyapunov–Schmidt reduction:

1. Four singular points initially give one \(J\)-even radial bubble projection each.
2. \(A\) pairs
   \[
   (N,N)\leftrightarrow(S,S),\qquad
   (N,S)\leftrightarrow(S,N),
   \]
   leaving two independent radial equations.
3. The \(A\)-invariant scales provide two variables \(t_1,t_2\).

After fixing the Einstein normalization, this produces a reduced map of the form
\[
(F_1,F_2):(t_1,t_2)\longmapsto\mathbb R^2.
\]

Three corrections are important:

- \(A\) does **not** exchange the two node orbits. Hence it does not imply that \(F_1\) and \(F_2\) have the same functional form, nor that \(t_1=t_2\).
- A separate orientation-reversing product isometry, such as the antipodal map on one sphere, exchanges the orbits and also exchanges \(\Lambda^+\) with \(\Lambda^-\). It might relate \(F_1\) and \(F_2\), but compatibility with the opposite-chirality EH lifts must be proved before using it.
- Equal numbers of equations and variables do not provide a small positive solution. For example, if the first radial terms are
  \[
  F_i=t_i\sum_j B_{ij}t_j^2+\cdots,
  \]
  then, for \(t_i>0\), the leading equation is
  \[
  B(t_1^2,t_2^2)^T=0.
  \]
  A nonzero branch approaching the orbifold requires suitable algebra and signs in \(B\); an invertible \(B\) leaves only \(t_1=t_2=0\).

The supplied \(O(t_{\max}^{5/2})\) remainder also does not by itself prove that the next radial term is exactly cubic. Inter-node terms are naturally expected at \(t_it_j^2\), but a refined expansion is needed to separate cubic, logarithmic, and other contributions.

## 6. Strongest existence consequence and remaining mathematics

The strongest established structural consequence is:

> In an exactly \(A\)- and \(J\)-equivariant EH gluing family with insertion direction \(\omega _2\), all \(J\)-odd bubble projections and all \(A\)-odd global kernel projections vanish identically, while every coefficient currently resolved through the local second-order Ozuch equations vanishes after applying the rank-one determinant formula.

This shows that the known local second-order equations do not exclude a positive Einstein desingularization of the stated product orbifold, potentially yielding the indicated smooth type \(\#_3(S^2\times S^2)\).

An existence theorem still requires:

- a global \(A,J\)-equivariant approximate metric with compatible lifts at all four EH pieces;
- a uniform inverse for the gauge-fixed linearized Einstein operator on the invariant complement, including the eigenvalue \(-\Lambda\), possible small neck eigenvalues, and diffeomorphism modes;
- a refined computation of the two radial reduced functions, including self-response, product Green interactions, the even scalar shape response, gauge terms, and Einstein normalization;
- positive scales solving the reduced equations, together with a nondegenerate derivative or another mechanism producing a branch approaching \(t_1=t_2=0\);
- weighted elliptic estimates and nonlinear contraction or implicit-function arguments yielding an exact smooth Einstein metric.

Thus the \(J\)-symmetry theorem is a strong and exact representation-theoretic reduction. Its content is transverse all-order vanishing, not complete all-order desingularization.