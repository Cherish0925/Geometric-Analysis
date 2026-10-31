# Step 89: correction of Step 88 positivity and finite relative Green formulation

Session `S0910A01`. Agent3 / Actuator. Phase Execute.

## 1. What was corrected

Step 88 correctly found a low-mode mechanism in the product orbifold
\[
\mathcal O=(S^2\times S^2)/\langle(r_\pi,r_\pi)\rangle:
\]
for the axial Killing--Killing mode
\[
h=(*dZ_A)\otimes(*dZ_B)+(*dZ_B)\otimes(*dZ_A),\qquad Ph=h,
\]
the node sign vector in node order `(NN,NS,SN,SS)` is
\[
s=(+1,-1,-1,+1),
\]
and this equals the diagonal mixed chirality pattern.  Thus the axial $V_2$ boundary source reinforces for mixed chirality and cancels for the equal-scale all-same comparison.

The Step 88 inference that the complete chirality-odd Green interaction is unconditionally positive is withdrawn.  The two mathematical reasons are decisive:

1. The product operator is not positive on all TT tensors.  The parallel shape tensor
\[
q=g_A-g_B
\]
is trace-free, divergence-free, descends to the quotient, and satisfies
\[
Pq=-q
\]
for unit product spheres.

2. The relevant sources are point-supported quadrupoles.  Their self-pairing through a Green kernel is singular.  A heat-regularized matrix before diagonal subtraction can be nonnegative, but subtracting or omitting the singular self terms does not preserve positivity.  A finite off-diagonal comparison must be derived; its sign is not inherited from an unregularized sum of squares.

The files corrected in this step are:

- `workspace/notes/step88_four_node_structural_theorem.md` (front correction and replacement of §§7--10),
- `workspace/plans/route_assessment_step88.md` (overwritten with corrected route status),
- warnings inserted into `workspace/scripts/step88_four_node_chirality_assembly.py`, `step88_source_receiver_proportionality.py`, and `step88_proportionality_random_test.py`.

## 2. Ozuch anchors and order bookkeeping

The source-level anchors in Ozuch's *Higher order obstructions* local Knowledge file remain:

- Lines 625--638: the boundary formula for zero-mode projections; the limit contains
  \[
  3\int_{S^3/\mathbb Z_2}\langle H^4,V_{l,2}\rangle
  +\int_{S^3/\mathbb Z_2}\langle H_2^4,V_{l,0}\rangle .
  \]
  When the first obstructions $\lambda_k$ vanish, Ozuch sets $H_2^4=0$.
- Lines 640--647: in the multi-node setting, $\bar h^4=\sum_j\bar h_j^4$ is orthogonal to the orbifold kernel and has the prescribed $H^4+H_2^4$ asymptotics at each node.
- Lines 770--795: Proposition 2.19 is necessary for an existing nearby Einstein metric.  In the scale notation $\zeta_j=t_j\phi_j$ it gives
  \[
  t_j\lambda_k^j(\phi_j,v)+t_j^2\mu_k^j(\phi_j,v)=O(t_{\max}^{5/2}),
  \qquad \nu_l(t\phi,v)=O(t_{\max}^{5/2}).
  \]

An inter-node response from a source $H^4(t_j\phi_j)=t_j^2H^4(\phi_j)$ enters the radial variables as
\[
t_i\,\delta\lambda_i=t_it_j^2\mathcal I_{ij}+\cdots,
\]
so for comparable scales it is $O(t^3)$.  Since $t^3=o(t^{5/2})$, Ozuch's displayed necessary estimate is too coarse to decide this layer.  Any mixed-row obstruction or existence argument requires a sharper projected expansion after the $t^2$ terms have been cancelled.

## 3. Exact flat source--receiver identity with corrected normalization

Let $H_{ijpq}=\partial_p\partial_q h_{ij}(0)$ be symmetric in $(i,j)$ and $(p,q)$, and write the homogeneous quadratic term as
\[
V_2(x)=\frac12 H_{ijpq}x_px_q.
\]
Use Ozuch's trace-free involution convention
\[
C_{ab}=\omega_a^+\circ\omega_b^-,\qquad
\operatorname{tr}(C_{ab}C_{cd})=4\delta_{ac}\delta_{bd},
\]
and define
\[
D_{ijpq}=\sum_{k=1}^3(C_{2k})_{ij}(C_{2k})_{pq}
        -\sum_{k=1}^3(C_{k2})_{ij}(C_{k2})_{pq},
\]
where the index $2$ denotes the chosen insertion direction $\zeta=\omega_2$.

The chirality-odd boundary source is
\[
S_{\rm odd}=\frac{B^+-B^-}{2},
\qquad
\frac{S_{\rm odd}}{\pi^2}=-\frac1{32}D_{ijpq}H_{ijpq}.
\]
The receiver principal part is
\[
R_{\rm odd}(H)=\frac{(\delta R^+)_{22}-(\delta R^-)_{22}}2,
\]
where $(\delta R^\pm)_{22}$ denotes the curvature-operator matrix entry in the normalized SD/ASD basis, equivalently
\[
(\delta R^\pm)_{22}=\frac{\langle\omega_2^\pm,\delta\mathcal R\,\omega_2^\pm\rangle}{|\omega_2^\pm|^2},
\qquad |\omega_2^\pm|^2=2.
\]
If one instead uses an unnormalized raw contraction, the displayed proportionality gains the corresponding factor.  The Riemann variation convention is
\[
\delta R_{abcd}=\frac12\left(H_{adbc}+H_{bcad}-H_{acbd}-H_{bdac}\right).
\]
The exact identity is
\[
\boxed{\quad S_{\rm odd}(V_2)=\frac{\pi^2}{2}R_{\rm odd}(H).\quad}
\]
Equivalently,
\[
D_{ijpq}H_{ijpq}=-16R_{\rm odd}(H).
\]

This identity was checked exactly on the full 100-dimensional basis of independent symmetric Hessians by `workspace/scripts/step89_identity_and_spectral_support.py`, with output `workspace/data/step89_identity_and_spectral_support.json`.  The sparse coefficient script `workspace/scripts/step89_identity_sparse_components.py` records that only four independent components occur:
\[
\begin{aligned}
D:H={}&-8H_{01,23}+8H_{03,12}+8H_{12,03}-8H_{23,01},\\
R_{\rm odd}={}&\frac12H_{01,23}-\frac12H_{03,12}-\frac12H_{12,03}+\frac12H_{23,01}.
\end{aligned}
\]
The Step 88 `\pi^2` factor was doubled because the script put Hessian coefficients into the source formula for polynomial $V_2$ coefficients; the missing $1/2$ is exactly the difference between $H$ and $V_2$.

For the axial mode, the corrected identity gives
\[
S_{\rm odd}/\pi^2=\frac12,
\qquad R_{\rm odd}=1,
\]
matching Step 87's exact boundary values
\[
B^+=\frac{\pi^2}{2},
\qquad B^-=-\frac{\pi^2}{2}
\]
in the unaveraged symmetric product convention.

## 4. Negative and zero mode support at the principal level

The shape tensor $q=g_A-g_B$ is TT and satisfies $Pq=-q$, so it must remain in any inverse/slice formulation.  The Step 89 exact computation gives
\[
S_{\rm odd}(q)=0,
\qquad R_{\rm odd}(q)=0
\]
at the flat principal $V_2$ level.  The reason is structural: the Taylor expansion of $q$ has tensor and derivative indices inside one $S^2$ factor, while $D$ is supported on the fully mixed orientation-sensitive index sector.

The same exact computation gives zero principal odd source for the four scalar Ozuch zero modes
\[
u_Ag_A,
\quad u_Ag_B,
\quad u_Bg_A,
\quad u_Bg_B.
\]
For the same-factor modes this is because the Taylor support stays inside one factor.  For the crossed scalar modes $u_Ag_B$ and $u_Bg_A$ the support can be of type $BB;AA$ or $AA;BB$, but the tensor factor is diagonal; the defect tensor $D$ uses only the four fully mixed non-diagonal components $H_{01,23},H_{03,12},H_{12,03},H_{23,01}$.  Equivalently, their relevant component is in the $C_{11}$ shape direction, orthogonal to the chirality-odd $C_{2k}/C_{k2}$ sector.

This is not yet the complete geometric support theorem requested by the calculation.  What is established here is the full flat principal functional.  The full source includes cutoff, Bianchi correction, curved-parametrix terms, $H_2^4$ when first obstructions do not vanish, constant-jet/frame effects, and the Ozuch radial normalization.  In the in-kernel product setting $\lambda_k=0$, Ozuch's formula allows $H_2^4=0$ for the zero-mode boundary projection, but the nonzero negative shape mode still needs a full slice-level integration-by-parts derivation before one can say the complete geometric source has no negative component.

## 5. Relative mixed--all-same interaction

Decompose the source and receiver at each node into chirality-even and chirality-odd parts:
\[
S_j^{\epsilon_j}=S_j^0+\epsilon_jS_j^1,
\qquad
L_i^{\epsilon_i}=L_i^0+\epsilon_iL_i^1.
\]
For a common regularization parameter $\tau$ define sector kernels
\[
K_{ij}^{ab}(\tau)=L_i^aG_\tau S_j^b,
\qquad a,b\in\{0,1\}.
\]
To match the Ozuch radial variables, the receiver weight and source weight should be kept distinct:
\[
a_i=t_i,
\qquad b_j=t_j^2,
\]
because the response from node $j$ has size $t_j^2$ and enters the $i$th radial equation after multiplication by $t_i$.  The response for assignment $\epsilon=(\epsilon_j)$ is therefore
\[
\mathcal R_\epsilon(\tau)=\sum_{i,j}a_ib_j
\left(K_{ij}^{00}+\epsilon_jK_{ij}^{01}+\epsilon_iK_{ij}^{10}+\epsilon_i\epsilon_jK_{ij}^{11}\right).
\]
Compared with the all-same assignment $\epsilon_i=1$, the relative response is
\[
\Delta_\epsilon(\tau)=\sum_{i,j}a_ib_j
\left((\epsilon_j-1)K_{ij}^{01}
     +(\epsilon_i-1)K_{ij}^{10}
     +(\epsilon_i\epsilon_j-1)K_{ij}^{11}\right).
\]
For the pure odd--odd part, the diagonal coefficients vanish identically:
\[
\epsilon_i^2-1=0.
\]
Thus common odd--odd self singularities cancel before taking $\tau\downarrow0$, leaving a finite off-diagonal odd--odd object if the matched regularized limit exists.  This cancellation is algebraic; it does not imply a sign.  Even--odd and odd--even diagonal terms do not vanish from this formula unless a genuine symmetry, principal-symbol orthogonality, or local matched subtraction removes them, so their finiteness is a separate problem.

For the axial mode alone, in the provisional unaveraged normalization,
\[
K_{ij}^{11,{\rm axial}}=\frac{9}{128}s_is_j
\]
because $B_j^{\epsilon_j}=\epsilon_js_j\pi^2/2$, $L_i^{\epsilon_i}=\epsilon_is_i$, $\lambda=1$, and $\|h\|^2=64\pi^2/9$.  For the diagonal mixed assignment $\epsilon=s$, the odd--odd relative coefficient is
\[
(\epsilon_i\epsilon_j-1)K_{ij}^{11,{\rm axial}}
=\frac{9}{128}(1-s_is_j),
\]
so only opposite-sign node pairs contribute and they contribute positively in this isolated channel.  This recovers the useful axial mechanism while avoiding any claim about the sign of the full relative Green interaction.

## 6. Meaning for the Yau--26 program

This step does not prove or disprove Einstein existence on $\#_3(S^2\times S^2)$ and does not solve Yau Problem 26.  It improves the positive product-orbifold branch by replacing an unsupported positivity assertion with a sharper computable target:

1. an exact flat adjoint identity for the principal source/receiver;
2. principal annihilation of the known negative and zero modes;
3. a finite relative mixed--all-same Green quantity in which common self singularities cancel before the limit;
4. explicit order separation showing that the inter-node layer is below Ozuch Proposition 2.19's necessary estimate.

The next work should derive the full Bianchi-compatible geometric source and receiver, prove the complete negative/zero-mode support statement in the chosen slice, and compute the finite off-diagonal relative kernels rather than relying on positivity of a singular self-pairing.
