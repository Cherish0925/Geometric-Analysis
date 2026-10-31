# Step 89 correction notice

Step 89 retracts the Step 88 positivity conclusion in §§7--10 below.  The valid Step 88 result is the four-node axial $\lambda=1$ source structure: the node sign vector $s=(+1,-1,-1,+1)$ matches the diagonal mixed chirality pattern, so the axial $V_2$ boundary source reinforces for the mixed assignment and cancels for the equal-scale all-same assignment.  The later inference that this makes the full chirality-odd Green interaction positive or sign-determined is not established.  In fact the parallel shape tensor $q=g_A-g_B$ is TT and satisfies $Pq=-q$ on $S^2(1)\times S^2(1)$, so $P$ is not positive on all TT tensors.  Moreover point-supported quadrupole sources have singular self-pairings; a relative mixed--all-same comparison can cancel common diagonal singularities, but the resulting finite off-diagonal quantity does not inherit positivity from an unregularized sum of squares.

Step 89 also fixes a normalization issue in the source--receiver identity.  If $H_{ijpq}=\partial_p\partial_q h_{ij}(0)$ and $V_2=\frac12H_{ijpq}x_px_q$, then at the flat principal $V_2$ level
\[
S_{\rm odd}(V_2)=\frac{\pi^2}{2}R_{\rm odd}(H),
\qquad D:H=-16R_{\rm odd}(H),
\]
not $S_{\rm odd}=\pi^2R_{\rm odd}$.  See `workspace/scripts/step89_identity_and_spectral_support.py` and `workspace/data/step89_identity_and_spectral_support.json`.

# Step 88: Four-node assembled chirality source — structural theorem

Session `S0910A01`. Agent2 / Constructor. Phase Execute.

## 1. Statement

**Theorem (four-node chirality non-cancellation).** Let $\mathcal O = (S^2 \times S^2)/\langle (r_\pi, r_\pi) \rangle$ with four $A_1$ nodes $p_1=NN, p_2=NS, p_3=SN, p_4=SS$. Consider the axial Killing–Killing eigenmode
$$
h = (*dZ_A) \odot (*dZ_B),\qquad Ph = h
$$
on the upstairs product, where $P = \frac{1}{2}\nabla^*\nabla - \mathring{R}$ is the Lichnerowicz operator. Define the chirality-odd source functional at node $j$:
$$
S_{\mathrm{odd},j}(h) = \frac{B_j^+(h) - B_j^-(h)}{2}
$$
where $B_j^\varepsilon$ is the Ozuch boundary-pairing source for chirality $\varepsilon\in\{+,-\}$.

Then at the $V_2$ boundary-pairing level:

**(a)** The node-sign vector $s = (s_j)_{j=1}^4 = (+1,-1,-1,+1)$ satisfies
$$
B_j^\varepsilon(h) = \varepsilon\,s_j\,\frac{\pi^2}{2},\qquad
S_{\mathrm{odd},j}(h) = s_j\,\frac{\pi^2}{2},\qquad
S_{\mathrm{even},j}(h) = 0.
$$
(Convention: $h = \alpha\otimes\beta + \beta\otimes\alpha$ without the symmetrization $1/2$, matching Step 87. With $\odot = \frac{1}{2}(\otimes+\otimes^T)$, replace these $B$ and $S_{\rm odd}$ constants by $\pi^2/4$ throughout.)

**(b)** For the diagonal mixed-chirality assignment $\varepsilon_j = s_j$, the four-node assembled chirality-odd source is
$$
\sum_j w_j\,\varepsilon_j\,S_{\mathrm{odd},j}(h)
= \frac{\pi^2}{2}\sum_j w_j > 0
$$
for any positive bubble scales $w_j = t_j^2 > 0$. No scale choice can cancel this.

**(c)** For the all-same assignment $\varepsilon_j = +1$ with equal scales $w_j = w$,
$$
\sum_j w\,S_{\mathrm{odd},j}(h)
= \frac{w\pi^2}{2}(1 - 1 - 1 + 1) = 0.
$$

**(d)** Among quotient-descending TT modes at $\lambda = 1$, the chirality-odd $V_2$ source is one-dimensional, spanned by the axial mode $h$. The equatorial modes $(*dX_A\odot*dX_B, \ldots)$ have $V_0\neq 0$ at all nodes and zero $V_2$ chirality source difference.

## 2. Proof sketch

### Node-sign transport

On each unit sphere $S^2(1)$, the height function $Z = \cos\theta$ gives the Killing one-form $K_Z = *dZ$. In geodesic normal coordinates at a pole:
$$
K_Z|_N = x_1 dx_0 - x_0 dx_1 + O(r^3),\qquad
K_Z|_S = -(x_1'dx_0' - x_0'dx_1') + O(r^3).
$$
The sign reversal at $S$ gives factor signs $\sigma_N = +1$, $\sigma_S = -1$. The product mode has $V_2$ at node $(p,q)$ equal to $\sigma_p\sigma_q$ times $V_2$ at NN. Since the boundary pairing $B_j^\varepsilon$ is linear in $V_2$, this gives $B_j^\varepsilon = \sigma_p\sigma_q\,B_{NN}^\varepsilon$, hence $s_j = \sigma_p\sigma_q$ as claimed.

### Explicit source at NN

Using $H_+^4 = -\frac{1}{2}\sum_k(x^TC_{2k}x)C_{2k}$ and the $S^3$ quartic moment, the Step 87 calculation gives $B_{NN}^+ = \pi^2/2$ and $B_{NN}^- = -\pi^2/2$, hence $B_{NN}^+ - B_{NN}^- = \pi^2$. This was verified by direct computation against the bilinear defect tensor $D_{ij,pq}$ with $D:M = -8$.

### Coincidence of s and mixed-chirality pattern

The mixed-diagonal chirality assignment assigns $\varepsilon_j = +1$ to nodes where both factors are at the same pole (NN, SS) and $\varepsilon_j = -1$ where they are at opposite poles (NS, SN). This is exactly $\varepsilon_j = \sigma_p\sigma_q = s_j$, because the chirality of the Eguchi–Hanson insertion follows the orientation of the resolved node, and the orientation depends on the product of the two factor orientations.

### Assembly

$\sum_j w_j \varepsilon_j s_j = \sum_j w_j s_j^2 = \sum_j w_j$ for mixed-diagonal, and $\sum_j w_j s_j = w_1 - w_2 - w_3 + w_4$ for all-same. Under the $A+L$ equal-scale condition, $w_j = w$ and the latter vanishes.

### Eigenspace isolation

On $S^2(1)$, the three Killing forms $K_X, K_Y, K_Z$ satisfy $\nabla^*\nabla K_U = K_U$. The equatorial forms $K_X, K_Y$ have nonzero constant jets at the poles: $K_X|_N = -dx_1 + O(r)$, $K_Y|_N = dx_0 + O(r)$. The axial form $K_Z|_N = O(r)$ has zero constant jet. For the mixed products $K_U^A \odot K_V^B$, the quadratic jet $V_2$ at NN is:

- **Equatorial ($U,V \in \{X,Y\}$)**: $V_2$ arises from $K_U^{(0)}\odot K_V^{(2)} + K_U^{(2)}\odot K_V^{(0)}$, where each term has both derivative indices within a single factor. The derivative-index/tensor-index quartets therefore have repeated factor labels, and contracting with the fully-mixed defect tensor $D$ gives zero.

- **Axial ($U=V=Z$)**: $V_2 = K_Z^{(1),A}\odot K_Z^{(1),B}$, with one derivative index per factor, creating the fully-mixed quartets $(0,3,1,2)$ and $(1,2,0,3)$. These pair nontrivially with $D$.

## 3. Physical interpretation

Since $Ph = h$ with $\lambda = 1 > 0$, this mode is **not** a Fredholm obstruction. It is a definite **correction field**: the chirality-odd source $S_{\mathrm{odd}}$ can be inverted by $P$ to produce a smooth tensor field
$$
u = P^{-1}S_{\mathrm{odd}}
$$
whose $\lambda = 1$ projection is proportional to $h$. This field propagates the local chirality information to all other nodes and modifies the local curvature there.

The receiver linearized curvature (Step 87) is:
$$
\delta R^+ = \operatorname{diag}(-2,1,1),\quad \delta R^- = \operatorname{diag}(2,-1,-1)
$$
for $\zeta = \omega_2$, giving a nonzero local radial response with opposite signs for opposite chiralities. This feeds back into the radial obstruction equations at the next matching order.

## 4. Self-adjointness direction

The operator $P$ is formally self-adjoint on the orbifold. Therefore $G_P^\perp = (P|_{(\ker P)^\perp})^{-1}$ is also self-adjoint on $(\ker P)^\perp$. Consider the chirality-odd source functional:
$$
S_j^{\mathrm{odd}} = \frac{S_j^+ - S_j^-}{2}.
$$

If the receiver functional $L_i$ at node $i$ can be identified (up to normalization) with the source functional $S_i$ through the boundary duality, then:
$$
c_{ij}^{\mathrm{odd}} = L_i\,G_P^\perp\,S_j^{\mathrm{odd}} = \kappa\,\langle S_i, G_P^\perp S_j^{\mathrm{odd}} \rangle
$$
for some constant $\kappa$. In particular, the diagonal $c_{ii}^{\mathrm{odd}}$ would be:
$$
c_{ii}^{\mathrm{odd}} = \kappa \sum_{\lambda_k > 0} \frac{|S_i^{\mathrm{odd}}(h_k)|^2}{\lambda_k \|h_k\|^2} \geq 0,
$$
which is non-negative by self-adjointness. The $\lambda = 1$ term is strictly positive.

**What is needed to complete this direction:**
1. Identify the receiver radial curvature functional with the adjoint source (boundary duality between the singular parametrix and test eigentensors)
2. Control the negative modes ($P = -1$ shape mode) through the kernel/slice projection
3. Verify that the common normalization gives $\kappa > 0$
4. Show that the four-node assembly preserves the positivity structure

**Warning (TTCS-verified):** Source and receiver are not the same functional in general. The source acts through $B_j^\varepsilon = 3\int_{S^3/Z_2} \langle H^4_\varepsilon, V_2 \rangle$, while the receiver extracts $\delta R^\varepsilon$ curvature components. These are related but not identical; the identification requires the Green boundary-duality argument.

## 5. What this resolves and what remains

### Resolved:
- The mixed-chirality construction activates a global response at $\lambda = 1$ that the equal-scale all-same construction does not
- This mechanism is structural (sign-vector coincidence), not a numerical accident
- The chirality-odd source at $\lambda = 1$ is one-dimensional and isolated from intra-eigenspace cancellation
- The result is consistent with the known KE degeneration for the all-same filling

### Remaining:
- Higher eigenspaces $\lambda > 1$ can in principle contribute to the full coefficient; their decay $1/\lambda$ is offset by growing jet coefficients and eigenspace dimensions
- The full $c_{\mathrm{opp}} - c_{\mathrm{same}}$ requires the complete source/receiver identification, all eigenspace projections, negative/zero mode handling, and regularized spectral sum
- $V_0$-dependent receiver corrections for equatorial modes are not included
- The self-adjointness/positivity direction is promising but requires the boundary duality identification
- This remains a local constructive test, not a solution of Yau-26

## 6. Data and verification

- Computation: `workspace/scripts/step88_four_node_chirality_assembly.py`
- Output: `workspace/data/step88_four_node_chirality_assembly.json`
- TTCS verification: `trace/ttcs/results/step88_ttcs01_verifier1_integration.md`
- Step 87 source data: `workspace/data/step87_missed_killing_mode_boundary.json`
- Step 87 receiver data: `workspace/data/step87_missed_killing_mode_receiver.json`
- Step 87 l=1 source matrix: `workspace/data/step87_l1_oneform_source_matrix.json`


## 7. Source--receiver identity corrected by Step 89

The Step 88 proportionality calculation was useful but used two incompatible versions of the quadratic coefficient.  The boundary pairing is naturally written for the homogeneous quadratic term
\[
V_2(x)=\frac12H_{ijpq}x_px_q,\qquad H_{ijpq}=\partial_p\partial_qh_{ij}(0),
\]
whereas `step88_source_receiver_proportionality.py` fed the Hessian-like tensor directly into the source formula.  The corrected exact identity is
\[
S_{\rm odd}(V_2)=\frac{\pi^2}{2}R_{\rm odd}(H),
\]
with
\[
S_{\rm odd}/\pi^2=-\frac1{32}D_{ijpq}H_{ijpq},
\qquad
R_{\rm odd}=\frac{(\delta R^+)_{22}-(\delta R^-)_{22}}2,
\]
where $(\delta R^\pm)_{22}$ is the curvature-operator matrix entry in the normalized SD/ASD basis (equivalently $\langle\omega_2^\pm,\delta\mathcal R\omega_2^\pm\rangle/|\omega_2^\pm|^2$ with $|\omega_2^\pm|^2=2$),

and equivalently
\[
D_{ijpq}H_{ijpq}=-16R_{\rm odd}(H)
\]
for every symmetric Hessian $H$.

This is an exact finite-dimensional algebra statement in a fixed oriented orthonormal frame.  The script `workspace/scripts/step89_identity_and_spectral_support.py` verifies the tensor equality on the full 100-dimensional basis of tensors symmetric in $(i,j)$ and $(p,q)$ with zero failures, not merely on random samples.  For the axial Killing--Killing mode it gives
\[
S_{\rm odd}/\pi^2=\frac12,
\qquad R_{\rm odd}=1,
\]
matching the Step 87 boundary result $B_+=\pi^2/2$, $B_-=-\pi^2/2$ under the unaveraged symmetric product convention.  This flat identity is strong evidence that the leading singular source is adjoint to the leading radial curvature receiver, but it does not yet include curved-parametrix corrections, $V_0$ frame terms, gauge choices, or the Ozuch radial normalization.

## 8. Spectral support and negative/zero modes

The Step 88 statement that all TT eigenvalues are positive is false.  On the unit product,
\[
q=g_A-g_B
\]
is parallel, trace-free, divergence-free, descends to the quotient, and satisfies
\[
Pq=-q.
\]
Thus any inverse or Green calculation must specify the slice and the treatment of this negative shape direction.

The principal chirality-odd $V_2$ source nevertheless annihilates this mode: the local expansion of $q$ has tensor and derivative indices within a single $S^2$ factor, while the defect tensor $D$ lives in the fully mixed orientation-sensitive sector.  The Step 89 exact script records
\[
S_{\rm odd}(q)=0,
\qquad R_{\rm odd}(q)=0
\]
at this flat principal level.  The same computation gives zero principal odd source for the four scalar Ozuch zero modes
\[
u_Ag_A,
u_Ag_B,
u_Bg_A,
u_Bg_B.
\]
This supports the possibility that the chirality-odd principal source lies in a favorable spectral sector, but it is not a complete geometric projection theorem: the full source includes cutoff, curvature, Bianchi, frame, and radial-normalization terms that must be matched to the chosen finite-dimensional slice.

## 9. Relative mixed--all-same interaction as the correct finite object

Point-supported quadrupole sources are not ordinary $L^2$ sources.  A formal diagonal expression
\[
\sum_k \frac{|S_i(h_k)|^2}{\lambda_k\|h_k\|^2}
\]
has a singular high-frequency self-pairing.  A heat-regularized full matrix may be nonnegative before subtracting singular diagonal terms, but deleting or renormalizing the diagonal does not preserve such positivity; an off-diagonal matrix with zero diagonal cannot itself be positive unless it is zero.

A more meaningful quantity is the relative comparison between two chirality assignments using the same local construction, scales, slice, and regularization.  If $K_{ij}^{11}(\tau)$ denotes the regularized odd-source/odd-receiver pairing, then the odd--odd part of the mixed-minus-all-same comparison in Ozuch radial weights is
\[
\Delta^{11}(\tau)
=\sum_{i,j}a_i b_j(\epsilon_i\epsilon_j-1)K_{ij}^{11}(\tau),
\qquad a_i=t_i,
\quad b_j=t_j^2.
\]
A purely energy-like quadratic comparison may use symmetric weights, but it is not the radial $O(t^3)$ object.  The odd--odd diagonal terms vanish identically because $\epsilon_i^2-1=0$, so common odd--odd self singularities cancel before taking $\tau\downarrow0$.  Even--odd and odd--even diagonal terms need separate symmetry or matched subtraction.  The finite inter-node limit, if it exists, must be computed from the smooth off-diagonal Green kernel and its matched local normalizations; its sign is not inherited from positivity of an unrenormalized self-pairing.

The complete response can also contain even--odd and odd--even pieces.  Writing
\[
S_j^{\epsilon_j}=S_j^0+\epsilon_jS_j^1,
\qquad
L_i^{\epsilon_i}=L_i^0+\epsilon_iL_i^1,
\]
one gets terms with factors $(\epsilon_j-1)$, $(\epsilon_i-1)$, and $(\epsilon_i\epsilon_j-1)$.  These cross terms should remain in the calculation unless an actual $A,J,L$ or chart symmetry eliminates them.

The axial mode now has a precise role.  In the provisional principal normalization it contributes a nonzero odd--odd off-diagonal relative signal for the checkerboard mixed assignment, while the equal-scale all-same source has no axial component.  This establishes a robust low-mode mechanism distinguishing the two fillings, not a sign theorem for the full radial equation.

## 10. Order bookkeeping and status after Step 89

For comparable scales the inter-node response enters the radial variables as
\[
t_i t_j^2\mathcal I_{ij}=O(t^3).
\]
Ozuch Proposition 2.19 gives only the necessary estimate
\[
t_i\lambda_i+t_i^2\mu_i=O(t_{\max}^{5/2}),
\]
and $t^3=o(t^{5/2})$.  Therefore the published necessary estimate is too coarse to determine this layer; deciding the mixed row requires a sharper projected expansion after the $t^2$ terms are killed.

Current established content:

- the four-node axial $\lambda=1$ source sign pattern and source isolation remain valid;
- the flat principal source--receiver identity is exact with the corrected factor $\pi^2/2$;
- the negative shape mode and scalar zero modes have zero principal chirality-odd source in the fixed local model;
- the finite object to derive is a matched, regularized relative mixed--all-same interaction with all surviving even/odd sectors and the Ozuch radial normalization.

This remains a local product-orbifold desingularization calculation.  It does not prove an obstruction to Einstein metrics on $\#_3(S^2\times S^2)$ and does not decide the full Yau--26 proposition.
