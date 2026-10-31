# Step 91: receiver simplification and adjacent odd Green calculation

Session `S0910A01`.  Agent3 / Actuator.  Phase Execute.

## 1. Exact mathematical setting of the K-reflection result

The background is the product Einstein orbifold
\[
\mathcal O=(S^2\times S^2)/\langle (r_\pi,r_\pi)\rangle
\]
with four \(A_1\) points in node order \(NN,NS,SN,SS\).  At each node the two Eguchi--Hanson insertion models use \(\zeta=\omega_2^+\) and \(\zeta=\omega_2^-\) in a fixed oriented product frame.  The single-factor reflection
\[
K(z,w)=(\bar z,w)
\]
fixes each node and exchanges \(\omega_2^+\leftrightarrow \omega_2^-\).

For a **K-equivariant linear pairwise construction** of the source and receiver on the background orbifold, define
\[
S_j^0=\frac{S_j^++S_j^-}{2},\qquad S_j^1=\frac{S_j^+-S_j^-}{2},
\]
and similarly \(L_i^0,L_i^1\) for the receiving radial functional.  If the regularized pseudo-inverse \(G_\tau\) is a K-equivariant heat or spectral inverse of
\[
P=\frac12\nabla^*\nabla-\mathring R
\]
on the K-invariant background slice, then
\[
L_i^0G_\tau S_j^1=L_i^1G_\tau S_j^0=0.
\]
The result controls the linear pairwise \(O(t_i t_j^2)\) K-odd Green transfer.  It does **not** imply existence or nonexistence of an Einstein metric on the desingularized smooth four-manifold, and it says nothing by itself about other possible Einstein metrics on \(\#_3(S^2\times S^2)\).  It is a local desingularization coefficient calculation on the chosen orbifold branch, not a proof of any complete normalized positive branch of Yau--26.

The negative and zero modes are also separated only in this linear background sense.  Since \(q=g_A-g_B\) and the scalar Ozuch zero modes are K-even, a K-odd source is orthogonal to them whenever the source construction is actually K-equivariant.  A particular Ozuch/Biquard chart, Bianchi normalization, cutoff, and nonlinear multi-source expansion still have to be checked for compatibility before one can use the coefficient in a full gluing theorem.

## 2. Checkerboard radial equations: only adjacent sources survive

For the mixed checkerboard assignment
\[
\varepsilon=(+1,-1,-1,+1)
\]
in node order \(NN,NS,SN,SS\), the relative mixed-minus-all-same linear pairwise radial equation is
\[
\Delta_i=t_i\sum_j t_j^2(\varepsilon_i\varepsilon_j-1)K_{ij}^{11}.
\]
The factor \(\varepsilon_i\varepsilon_j-1\) vanishes for self terms and for the two-factor diagonal companions \((NN,SS)\) and \((NS,SN)\).  These are not identified by the orbifold quotient; their cancellation is only the algebraic fact \(\varepsilon_i\varepsilon_j=1\).  The surviving ordered pairs are exactly adjacent pairs, i.e. pairs differing in one factor:
\[
NN\leftrightarrow NS,\quad NN\leftrightarrow SN,
\quad NS\leftrightarrow SS,
\quad SN\leftrightarrow SS.
\]
Thus, before using exchange symmetries,
\[
\begin{aligned}
\Delta_{NN}&=-2t_{NN}(t_{NS}^2K_{NN,NS}+t_{SN}^2K_{NN,SN}),\\
\Delta_{NS}&=-2t_{NS}(t_{NN}^2K_{NS,NN}+t_{SS}^2K_{NS,SS}),\\
\Delta_{SN}&=-2t_{SN}(t_{NN}^2K_{SN,NN}+t_{SS}^2K_{SN,SS}),\\
\Delta_{SS}&=-2t_{SS}(t_{NS}^2K_{SS,NS}+t_{SN}^2K_{SS,SN}).
\end{aligned}
\]
Only after the established node-frame-normalized exchange symmetries identify these adjacent coefficients can this be reduced to one number \(K_{\rm adj}\).  A total sum over receivers is not a substitute for the radial system.

Script/data: `workspace/scripts/step91_checkerboard_radial_reduction.py`, `workspace/data/step91_checkerboard_radial_reduction.json`.

## 3. Receiver simplification at the product background

The radial receiver is the chirality-odd curvature-operator entry in the \(\omega_2\) direction:
\[
R_{\rm odd}(h)=\frac{1}{2}\left(\delta R^+_{22}(h)-\delta R^-_{22}(h)\right).
\]
At the product background, the curvature operator has only the factor-supported entries \(R_{0101}=R_{2323}=1\).  Therefore
\[
R_0\omega_2^+=R_0\omega_2^-=0.
\]
Consequently, first-order changes of the insertion frame, Hodge splitting, or length normalization contribute terms of the form \(\langle \delta\omega,R_0\omega_2^\pm\rangle\), hence vanish.  The odd component selected by \(\omega_2^+-\omega_2^-\) has four distinct product indices, while every background curvature-times-\(h_0\) correction requires a factor-supported curvature component.  Those corrections vanish in this component.

Using the standard fixed-frame variation formula
\[
(\delta R)_{abcd}=\frac12\left(h_{ad,bc}+h_{bc,ad}-h_{ac,bd}-h_{bd,ac}\right),
\]
with \(H_{ij,pq}=\partial_p\partial_q h_{ij}(0)\), the full linear odd receiver in product normal coordinates is exactly
\[
\boxed{
R_{\rm odd}(H)=\frac12\left(H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01}\right).
}
\]
This is the sparse Step-89 second-jet functional; it has no extra dependence on \(V_0\) or \(V_1\).  The script `workspace/scripts/step91_receiver_simplification.py` verified the identity on the full 100-dimensional symmetric-Hessian basis, checked \(R_0\omega_2^\pm=0\), and checked that all possible one-index product-curvature support terms in the odd component vanish.

For the \(\ell=1\) coexact-coexact AB modes at NN, the receiver census is especially sharp: only
\[
(*dZ_A)\odot(*dZ_B)
\]
has nonzero odd receiver, equal to \(1\) in the Step-89 normalization.  The V0-nonzero equatorial coexact modes have zero odd receiver in this functional; they do not require a separate frame/background-curvature receiver correction at this linear product layer.

Data: `workspace/data/step91_receiver_simplification.json`.

## 4. Corrected spectral input

The Step-90 script had the right qualitative lower bound but an incorrect low-mode enumeration.  The corrected rules are:

1. The quotient generator is a simultaneous \(\pi\)-rotation.  Spherical harmonics transform by azimuthal parity \((-1)^m\), not by \((-1)^\ell\).  Descent uses \(m_A+m_B\) parity.
2. Factor trace-free tensor harmonics have rough eigenvalue \(\ell(\ell+1)-4\), and \(\mathring R=-1\) on that block, so
   \[
   P=\frac{\ell_F(\ell_F+1)+\ell_O(\ell_O+1)}2-1.
   \]
   The first K-odd quotient factor-TF modes occur at \(P=2\), not \(4\).  The executable ledger records the \(m=2\) electric-type example; TTCS pointed out that the \(m=0\) magnetic tensor harmonic \(\operatorname{sym}_0\nabla(*dY_{\ell0})\) is also K-odd at \(\ell=2\) and descends.  This does not change the lower bound, but it means the current low-mode ledger is not a complete tensor-harmonic decomposition.
3. In the mixed AB one-form block, \(\ell_A\) and \(\ell_B\) are independent and
   \[
   P=\frac{\ell_A(\ell_A+1)+\ell_B(\ell_B+1)}2-1,
   \]
   with minimum \(P=1\) at \((1,1)\).

The lower bound \(P\ge1\) in the K-odd quotient tensor sector survives these repairs: nonpositive scalar/shape modes are K-even or do not descend in their K-odd real component; AB one-form modes start at \(1\); factor-TF modes start at \(2\).  This is still only a spectral lower bound on the linear sector and does not assign a sign to off-diagonal Green values.  Also, the fixed reflection here is \(K_A\); a tensor supported in the second factor with first factor constant is K-even, and factor exchange changes the chosen reflection rather than preserving the same K-parity label.

Script/data: `workspace/scripts/step91_corrected_spectral_ledger.py`, `workspace/data/step91_corrected_spectral_ledger.json`.

## 5. First adjacent heat computation: AB one-form sector

Using the simplified receiver and the Step-89 principal adjoint normalization
\[
S_{\rm odd}=\frac{\pi^2}{2}R_{\rm odd},
\]
I computed the heat-regularized adjacent transfer in the mixed AB one-form sector:
\[
K^{AB}_{\tau}(NN,NS)=\frac{\pi^2}{2}\sum_{\psi\in AB}
\frac{e^{-\tau\lambda_\psi}R_{NN}(\psi)R_{NS}(\psi)}{
\lambda_\psi\|\psi\|^2_{\mathcal O}}.
\]
The instrument uses independent \((\ell_A,\ell_B)\), m-parity quotient descent, and heat regularization; it does not use the erroneous \(\ell_A=\ell_B\) restriction or the old factor-TF minimum.  Since the points are distinct but share one factor coordinate, the heat representation is preferable to an ordinary cutoff; individual polarization subseries can have strong short-time behavior, while the complete AB block has cancellations.

Numerical ladder for the adjacent pair \((NN,NS)\):

| \(\tau\) | cutoff | \(K^{AB}_\tau(NN,NS)\) | axial \((1,1,m=0)\) part |
|---:|---:|---:|---:|
| 0.2 | 80 | -0.031442495530455 | -0.057567006075796 |
| 0.1 | 100 | -0.031442497319956 | -0.063621380955653 |
| 0.05 | 140 | -0.031442497319962 | -0.066883318910206 |
| 0.02 | 220 | -0.031442497320011 | -0.068920219216881 |
| 0.01 | 320 | -0.031442497319961 | -0.069612878935488 |
| 0.005 | 480 | -0.031442497320561 | -0.069961814943235 |
| 0.003 | 650 | -0.031442497323991 | -0.070101878590081 |

The axial part tends to \(-9/128\), while the complete AB one-form sector in this normalization stabilizes near
\[
K^{AB}_{\rm adj}\approx -0.03144249732.
\]
The symmetry-related adjacent pair \((NN,SN)\) gives the same value to the displayed precision.  The opposite-corner pair \((NN,SS)\) gives about \(+0.01772676072\), but checkerboard relative factors kill this two-factor companion in the radial equation.

The self heat samples diverge rapidly, as expected for point-supported quadrupole self-pairings; they are not part of the finite adjacent coefficient.

Script/data: `workspace/scripts/step91_adjacent_ab_heat_spectral.py`, `workspace/data/step91_adjacent_ab_heat_spectral.json`.

## 6. Interpretation and remaining mathematical work

This step gives two reliable pieces and one experimental coefficient:

- Reliable: the linear odd receiver at the product background is exactly the sparse second-jet expression, with no hidden V0/frame/background correction.
- Reliable: the checkerboard relative radial equation retains only adjacent sources; two-factor diagonal companions vanish by \(\varepsilon_i\varepsilon_j=1\) before any summation over receivers.
- Experimental: the corrected AB one-form heat instrument gives a stable adjacent value near \(-3.14425\times10^{-2}\) in the principal normalization.

The experimental coefficient is **not** the full Ozuch coefficient.  The next mathematical work must still derive the singular source normalization from the actual ALE boundary duality, include the AA/BB tensor sectors and any Bianchi/gauge projection induced by the full source, prove heat-kernel convergence and tail estimates for the differentiated pairings, and match the coefficient to the \(t_i\lambda_i+t_i^2\mu_i\) radial expansion at order \(t_i t_j^2\).  Even if the adjacent coefficient is nonzero, it controls only the local symmetric desingularization branch of the product orbifold; it does not by itself obstruct all Einstein metrics on the underlying smooth manifold and does not solve the full Yau--26 proposition.
