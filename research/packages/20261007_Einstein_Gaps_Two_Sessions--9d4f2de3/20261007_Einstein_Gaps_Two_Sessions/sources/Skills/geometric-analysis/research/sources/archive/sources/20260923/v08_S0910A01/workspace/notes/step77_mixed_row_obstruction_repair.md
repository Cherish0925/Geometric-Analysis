# Step 77: repair of the mixed-row product-orbifold obstruction problem

Session `S0910A01`. Agent3 / Actuator. Phase Execute.

## Purpose

This note repairs the Step 76 simplification of the Ozuch obstruction problem for
\[
\mathcal O=(S^2\times S^2)/\langle(r_\pi,r_\pi)\rangle,
\qquad \operatorname{Ric}(g_o)=\Lambda g_o>0.
\]
The useful rank-one curvature cancellation remains, but the global finite-dimensional system cannot be deleted.  Ozuch Definition 1.8 defines
\[
P_g=\frac12\nabla^*\nabla-\mathring R,
\qquad \mathbf O(g)=\ker_{L^2}P_g
\]
on all symmetric two-tensors, not only on TT tensors.  The product quotient has zero TT kernel but has a four-dimensional scalar-sector full kernel.  A rigorous reduced problem must either include these four projections/variables or replace Ozuch's setup by an explicitly derived slice with corresponding compatibility equations.

## 1. Correct kernel statement

Let `u_1` be the axial first spherical harmonic on the first sphere and `u_2` the axial first harmonic on the second sphere.  They are invariant under the half-turn and hence descend to the orbifold.  With the positive Laplacian convention used in Ozuch's displayed operator,
\[
\Delta u_i=2\Lambda u_i,
\qquad \nabla^2u_i=-\Lambda u_i g_i.
\]
Since each factor metric is parallel and
\[
\mathring R(u_i g_j)=\Lambda u_i g_j,
\]
we get
\[
P(u_i g_j)=\frac12(2\Lambda)u_i g_j-\Lambda u_i g_j=0,
\qquad i,j\in\{1,2\}.
\]
Thus
\[
\{u_1g_1,u_1g_2,u_2g_1,u_2g_2\}\subset \mathbf O(g_o),
\]
and the full Ozuch kernel has the four scalar-sector modes already identified by A02.  The Step 76 data file `workspace/data/step76_orbifold_kernel_verification.json` is superseded on this point.

This does **not** contradict the zero TT kernel.  For a scalar-sector tensor with `f=u_1`,
\[
h=a f g_1+b f g_2 + c\nabla^2 f=(a-c\Lambda)fg_1+bfg_2,
\]
trace-free gives `(a-cΛ)+b=0`, while divergence-free gives `a-cΛ=0`; hence `b=0`.  There is no nonzero TT tensor from these modes.  Also the parallel relative tensor `g_1-g_2` satisfies `P(g_1-g_2)=-\Lambda(g_1-g_2)`, so it is an unstable eigenvector, not a zero mode.  The correct distinction is:

- `ker(P|TT)=0` and the shape mode is bounded away from zero;
- `ker_{L^2}P` on all symmetric tensors contains four non-TT scalar/gauge/conformal modes;
- a Bianchi/diffeomorphism slice may remove their role, but that must be derived and then substituted into the obstruction equations.

The executable check `workspace/scripts/step77_slice_decomposition_verify.py` wrote `workspace/data/step77_slice_decomposition_verify.json` with the formulas:
\[
B(a u_1g_1+b u_1g_2)=b\,du_1,
\qquad
B(c u_2g_1+d u_2g_2)=c\,du_2,
\]
and
\[
\mathcal L_{\nabla u_1}g=-2\Lambda u_1g_1,
\qquad
\mathcal L_{\nabla u_2}g=-2\Lambda u_2g_2.
\]
This shows why the full kernel modes are not genuine Einstein moduli after a geometric slice, but it also shows why deleting Ozuch's `\nu_l` projections without changing the slice is invalid.

## 2. Correct finite-dimensional system

For EH parameters `\zeta_j=t_j\phi_j`, chirality `\epsilon_j`, and possible orbifold-kernel coordinate `v`, Ozuch's estimates give, for an exact nearby Einstein metric,
\[
t_j\lambda_k^j(\phi_j,v)+t_j^2\mu_k^j(\phi_j,v)=O(t_{\max}^{5/2}),
\qquad
\nu_l(t\phi,v)=O(t_{\max}^{5/2}).
\]
These are projected finite-dimensional equations.  They are not themselves a full weighted residual estimate for the approximate metric; the full perturbation also needs the projected residual bound, a chosen inverse estimate on the complement, and nonlinear remainder control.

The rank-one local curvature block is still important:
\[
R^+=R^- = \operatorname{diag}(\Lambda,0,0),
\qquad \ker R^\pm=\operatorname{span}\{\omega_2^\pm,\omega_3^\pm\}.
\]
For `\phi_j\in\ker R^{\epsilon_j}`,
\[
\lambda_k^j(\phi_j,0)=0\quad(k=1,2,3).
\]
The displayed determinant formula in Ozuch §2.1.4 / Lemma 2.14 proves only
\[
\mu_1^j=C\det\begin{pmatrix}R_{22}&R_{23}\\ R_{32}&R_{33}\end{pmatrix}=0
\]
for the bare rank-one product block in the adapted basis.  It does **not** prove `\mu_2^j=\mu_3^j=0` until the Biq16 formulas for those components are derived in this basis and the corrections from `v`, the singular-subtracted Green response, and local coordinate normalization are included.  Nonzero transverse terms may be balanced by admissible changes of scales and angles rather than required to vanish identically.

## 3. The interacting object: singular-subtracted Green response

A useful construction problem remains.  When first obstructions are killed, Ozuch constructs a tensor `\bar h_j^4` satisfying, schematically,
\[
P_o\bar h_j^4=\sum_l \nu_l\mathbf v_l+
\sum_{m,k}\lambda_k^m\overline{\mathbf o}_{m,k}^4,
\qquad
\bar h_j^4\sim H^4(\zeta_j^{\epsilon_j})
\]
near node `j`, with singular part subtraction and orthogonality to `\mathbf O(g_o)`.  At a different node `i`,
\[
\bar h_j^4=H_{ij,0}+H_{ij,2}+O(r_i^4).
\]
The second jet `H_{ij,2}` changes the effective curvature block entering the local first obstruction at node `i`.  Its scale order is not the same as the local Ozuch `\mu_i` term.  Since
\[
H^4(t_j\phi_j)=t_j^2H^4(\phi_j),
\]
the regular response from source `j` at receiver `i` has size `O(t_j^2)` and enters the receiver finite equation as
\[
t_i\,\delta\lambda_{i,k}
= t_i t_j^2\,\mathcal I_{ij,k}+\cdots .
\]
For comparable scales this is order `t^3`, lower than the order currently resolved by Ozuch's `O(t_{\max}^{5/2})` necessary estimate and distinct from the bare local coefficient `t_i^2\mu_{i,k}`.  Thus the decisive object for a construction beyond Ozuch's displayed estimates is a **sliced multipole-to-curvature interaction map**
\[
\mathcal C_{ij}^{\epsilon}(\phi_j)
=D R^{\epsilon}_{p_i}\left[G_P^{\perp}(I-\Pi_{\mathbf O})\mathcal S_{j,\phi_j}\right],
\]
where `\mathcal S_{j,\phi}` is the boundary quadrupole source normalized by the Ozuch flux pairing.  It is not a point-value Green function, not a product of static one-factor Green functions, and not the local Ozuch `\mu` coefficient.  The full product resolvent has additive separated denominators `1/(\lambda_1+\lambda_2+\kappa_{tensor})`; receiver evaluations are regular for `i\ne j`, while singular subtraction is a source/self-node issue.

The earlier statement that “all second-order obstructions vanish and only convergence remains” is therefore withdrawn.  The correct opportunity is to compute or derive the sliced interacting obstruction map with precise order bookkeeping.

## 4. Executable local prototype

I wrote and ran `workspace/scripts/step77_scalar_kernel_and_pairing.py`, which produced `workspace/data/step77_scalar_kernel_and_pairing.json`.  The script verifies the self-dual/anti-self-dual tensor basis algebra and the full scalar kernel, then computes a **local raw normal-coordinate prototype** of the projections
\[
\int_{S^3/\mathbb Z_2}\langle H^4(\phi), V_{l,2}\rangle.
\]
Using the unsliced product-coordinate scalar modes `u_1g_1,u_1g_2,u_2g_1,u_2g_2`, the raw local coefficient at a north-north node is
\[
-\frac{1}{18}\pi^2
\]
for each of the four modes in the normalization of the script, independent of the in-kernel angle.  At the other nodes, the signs are the axial harmonic signs:
\[
\begin{array}{c|cc}
&u_1&u_2\\\hline
p_1=(N,N)&+&+\\
p_2=(N,S)&+&-\\
p_3=(S,N)&-&+\\
p_4=(S,S)&-&-
\end{array}
\]
TTCS then found, and the new scripts `workspace/scripts/step77_bianchi_defect_verify.py` and `workspace/scripts/step77_bianchi_cancellation_check.py` verified, that this raw coefficient is a Riemann-normal-coordinate artifact at quadratic Bianchi order.  In the convention `B_j=-\partial_i h_{ij}+\frac12\partial_j\operatorname{tr}h`, the raw product quadratic tensor has `B(H_2)=-\frac23x^\flat`.  The vector field
\[
X^a=-\frac{1}{18}r^2x^a
\]
(in `\Lambda=1` units and in the same flat tensor conventions) gives a Lie correction whose pairing is `+\pi^2/18`; hence the Bianchi-corrected local quadratic pairing with each of these four scalar modes is zero.  Therefore the `-\pi^2/18` value should be kept only as an algebraic unit test for the unsliced prototype.  It must not be used to infer that unequal scales produce a genuine scalar projection at this order.  Higher-order terms, a different complete slice, or the Green-transport problem can still produce finite-dimensional equations, but the local quadratic scalar projection itself cancels after the Bianchi coordinate correction.

## 5. Scope repairs

Ozuch Question 0.8 is a Ricci-flat question about whether Ricci-flat orbifold desingularizations by trees of Kähler Ricci-flat ALE metrics must be quotients of hyperkähler metrics.  It is not a positive-Einstein sufficiency conjecture for the product quotient.  A flat `T^4/Z_2` computation is therefore only a control calculation unless a transfer argument to the positive product orbifold is supplied.

The topology table for the four-node fillings has `b_2=6`, not a family `#_r(S^2\times S^2)` for `r=1,\ldots,4`.  For `k` positive EH kernels the rows from `20260912.tex` are:
\[
\begin{array}{c|c}
k&\text{oriented smooth type}\\\hline
0&\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2\\
1&2\mathbb{CP}^2\#4\overline{\mathbb{CP}}{}^2\\
2\text{ adjacent}&3\mathbb{CP}^2\#3\overline{\mathbb{CP}}{}^2\\
2\text{ opposite}&\#3(S^2\times S^2)\\
3&4\mathbb{CP}^2\#2\overline{\mathbb{CP}}{}^2\\
4&5\mathbb{CP}^2\#\overline{\mathbb{CP}}{}^2.
\end{array}
\]
The mixed rows of direct interest are `2CP^2#4CPbar^2`, the odd `3CP^2#3CPbar^2` row, and the even `#3(S^2\times S^2)` row.  These are positive-branch stress families for Yau--26; constructing or obstructing a nearby Einstein metric there does not resolve the full sign-unrestricted all-dimensional proposition.

## 6. Next mathematical work

The productive route is now precise:

1. Derive the scalar-kernel slice for the product quotient in the Ozuch gauge, specifying which of the four `u_i g_j` projections remain as equations and which are killed by Bianchi/diffeomorphism normalization.  The derivation must be reflected in the finite-dimensional map, not imposed afterwards.  The Step 77 Bianchi-cancellation script gives the first local check: quadratic scalar pairings vanish after the coordinate correction.
2. Compute the regular inter-node Green response from an EH `H^4(\zeta_j)` multipole at one node to the curvature response at another node.  Use the full product `P` pseudo-inverse with additive spectral denominators or a projected heat-kernel/massive-resolvent representation.  Do not multiply two static `S^2` Green functions.  For `i\ne j`, receiver evaluation is regular; subtract the singular part only at the source/self-node.
3. Keep the expansion ledger separate:
   \[
   F_{i,k}=t_i\lambda^{(0)}_{i,k}+t_i^2\mu^{(0)}_{i,k}
   +\sum_{j\ne i}t_it_j^2\mathcal I_{ij,k}+\cdots .
   \]
   Only after the effective local jets are derived should `\mu_{2,3}` be evaluated from the actual Biq16/Ozuch formulas.  The determinant formula already gives `\mu_1=0` for the bare product block, but no more.
4. Start with the diagonal `k=2` spin row because it is regular in both factors, has the larger `D_8` stabilizer, and corresponds to the even `#3(S^2\times S^2)` topology in the current working table.  Then compare adjacent `k=2` and `k=1\leftrightarrow k=3`.  A zero plus an inverse and nonlinear remainder estimate would be a genuine construction route; a nonzero map excluding all balances in a row would be a local degeneration obstruction only.

## Files

- Correction data: `workspace/data/step77_scalar_kernel_and_pairing.json`, `workspace/data/step77_slice_decomposition_verify.json`, `workspace/data/step77_bianchi_defect_verify.json`, `workspace/data/step77_bianchi_cancellation_check.json`.
- Scripts: `workspace/scripts/step77_scalar_kernel_and_pairing.py`, `workspace/scripts/step77_slice_decomposition_verify.py`, `workspace/scripts/step77_bianchi_defect_verify.py`, `workspace/scripts/step77_bianchi_cancellation_check.py`.
- Superseded Step 76 data: `workspace/data/step76_orbifold_kernel_verification.json` should not be used for the full Ozuch kernel dimension.
- Source lines: Ozuch Definition 1.8 at lines 243--250; global `\nu_l` construction at lines 625--666; estimates at lines 770--795 of the local Knowledge object.
