# Step 90: K-symmetry eliminates cross-parity sectors and gives geometric mode annihilation

Session `S0910A01`.  Agent2 / Constructor.  Phase Execute.

## 1. Definition and basic properties

Define the **single-factor meridian reflection**
$$
K(z,w)=(\bar z,w)
$$
on $S^2\times S^2$, where $\bar z$ denotes complex conjugation on $S^2\cong\mathbb{CP}^1$.
In real coordinates $(x_0,x_1,x_2)$ on the first sphere, $K$ sends $x_1\mapsto-x_1$ and fixes $x_0,x_2$.
On the product, $K$ acts as an orientation-reversing isometry: it preserves the round product metric and has $\det(DK)=-1$ in the tangent frame.

**Key properties** (all verified computationally with exact zero error):

| Property | K | L (for comparison) | J (for comparison) |
|---|---|---|---|
| Definition | $(\bar z,w)$ | $(-x,y)$ | $(\bar z,\bar w)$ |
| Tangent at node | $\mathrm{diag}(1,-1,1,1)$ | same in compatible frames | $\mathrm{diag}(1,-1,1,-1)$ |
| Determinant | $-1$ | $-1$ | $+1$ |
| Nodes | fixes all four | exchanges A-orbits | fixes all four |
| SD/ASD | exchanges: $\omega_2^+\leftrightarrow\omega_2^-$ | exchanges | preserves |
| Commutes with $\sigma,A,J$ | yes, yes, yes | yes, yes, yes | yes, yes, — |

The relation $K=K_A$ (conjugation on first factor), $K_B=KJ$ (conjugation on second), $J=K_AK_B$.

## 2. Chirality exchange at each node

Since $K$ fixes every node and maps $\omega_2^+\mapsto\omega_2^-$ with positive sign, the Eguchi–Hanson model at any node transforms as
$$
K^*(\mathrm{eh}_{\zeta^+})=\mathrm{eh}_{K^*\zeta^+}
=\mathrm{eh}_{t\omega_2^-}.
$$
The Ozuch $H^4$ multipole satisfies $K^*(H^4_+)(x)=H^4_-(x)$ **exactly** for all $x\in S^3$ (20,000 samples, max error $0$).
The algebraic mechanism is:
$$
K\,C_{2j}\,K=T_{K,j}\,C_{j2},\qquad T_K=\mathrm{diag}(-1,1,1),
$$
and since $T_{K,j}^2=1$ for all $j$, the bilinear $H^4$ formula is invariant:
$$
K\left(\sum_j(x^TC_{2j}x)\,C_{2j}\right)K
=\sum_j(x^TC_{j2}x)\,C_{j2}.
$$
The kernel mode $O_1$ also transports exactly: $K^*(O_1^+)=O_1^-$ (20,000 samples, max error $0$).

## 3. Even/odd parity decomposition

For any source, receiver, or tensor quantity $\phi$ defined at a node with chirality label $\varepsilon$, define
$$
\phi^0=\frac{\phi^++\phi^-}{2}\quad(\text{K-even}),
\qquad
\phi^1=\frac{\phi^+-\phi^-}{2}\quad(\text{K-odd}).
$$
Since $K^*(\phi^+)=\phi^-$ and $K^*(\phi^-)=\phi^+$, these have definite K-parity:
$$
K^*\phi^0=\phi^0,\qquad K^*\phi^1=-\phi^1.
$$

## 4. Cross-parity vanishing theorem

**Theorem.**  For any K-equivariant regularization parameter $\tau>0$ and any node pair $(i,j)$,
$$
K_{ij}^{01}(\tau)=L_i^0\,G_\tau\,S_j^1=0,
\qquad
K_{ij}^{10}(\tau)=L_i^1\,G_\tau\,S_j^0=0.
$$

**Proof.**  The Lichnerowicz operator $P$ commutes with $K^*$ because $K$ is an isometry of the background orbifold metric.  Any K-equivariant heat or spectral regularization $G_\tau$ therefore also commutes with $K^*$.  Since $S_j^1$ is K-odd, $G_\tau S_j^1$ is K-odd.  The receiver $L_i^0$ is K-even: this follows from the naturality of the linearized curvature operator under isometries.  Specifically, $L_i^\pm(h)=\langle\omega_2^\pm,D\mathcal R_{\bar g}[h]\omega_2^\pm\rangle/|\omega_2^\pm|^2$, and since $K^*\omega_2^+=\omega_2^-$, the K-pullback exchanges $L_i^+$ and $L_i^-$, making $L_i^0$ K-even and $L_i^1$ K-odd.  The $L^2$ inner product of a K-even functional with a K-odd field vanishes.  $\square$

**Scope.**  This is a geometric statement, not restricted to flat $V_2$ jets.  It holds after Bianchi correction, cutoff, curved-parametrix terms, and all Ozuch radial corrections, as long as the construction respects K-equivariance (which the node-fixed insertion does).

**Consequence for self-singularities.**  The even–odd diagonal terms $K_{ii}^{01}$ and $K_{ii}^{10}$ vanish by K-symmetry alone, without any matched subtraction or regularization limit.  This eliminates the problematic mixed-sector self-singularities identified in Step 89.

## 5. Geometric annihilation of negative and zero modes

**Theorem.**  The chirality-odd source $S_j^1$ is geometrically orthogonal to the negative shape mode $q=g_A-g_B$ and to all four scalar Ozuch zero modes $u_Ag_A,\,u_Ag_B,\,u_Bg_A,\,u_Bg_B$.

**Proof.**  All five modes are K-even:

- $q=g_A-g_B$: $K$ preserves both metrics ($K$ is an isometry of each factor), so $K^*q=q$.
- $u_Ag_A=Z_Ag_A$: $Z_A=\cos\theta_A=x_2$ is invariant under $x_1\mapsto-x_1$, and $g_A$ is preserved by the isometry, so $K^*(u_Ag_A)=u_Ag_A$.
- Similarly for $u_Ag_B$, $u_Bg_A$, $u_Bg_B$, since $Z_B=y_2$ is unchanged by K (identity on second sphere).

The source $S_j^1$ is K-odd.  The P-eigenspace decomposition respects K-parity.  Therefore $\langle S_j^1,\psi\rangle=0$ for every K-even eigenfunction $\psi$, including $q$ and the scalar zero modes.  $\square$

For the K-equivariant linear pairwise background problem this upgrades the Step 89 flat principal calculation for these modes: the negative shape mode $q$ with $Pq=-q$ lives in the K-even sector and does not pair with the K-odd source.  A particular Ozuch/Biquard chart and nonlinear multi-source terms still require separate compatibility checks.

## 6. Simplified relative interaction

With cross-parity terms eliminated, the relative mixed-minus-all-same response reduces to
$$
\Delta_\varepsilon(\tau)
=\sum_{i,j}a_ib_j(\varepsilon_i\varepsilon_j-1)\,K_{ij}^{11}(\tau),
$$
where $a_i=t_i$ (receiver weight), $b_j=t_j^2$ (source weight), and $K_{ij}^{11}$ is the pure chirality-odd interaction.

The diagonal odd–odd terms vanish algebraically: $\varepsilon_i^2-1=0$.  Therefore
$$
\Delta_\varepsilon(\tau)
=\sum_{i\ne j}a_ib_j(\varepsilon_i\varepsilon_j-1)\,K_{ij}^{11}(\tau).
$$
This is an **off-diagonal sum of smooth Green kernel values** at distinct nodes (separated by a definite distance on the orbifold), requiring no singular self-subtraction.

## 7. Step 91 correction to the spectral input

Step 91 repairs the enumeration in the first version of this section.  The useful lower-bound conclusion survives, but the bookkeeping must be stated with the correct quotient and product-spectrum rules.

**Corrected product rules.**
- The quotient generator is the simultaneous \(\pi\)-rotation \(r_\pi\) on the two spheres.  Spherical modes transform by azimuthal parity \((-1)^m\), not by \((-1)^\ell\).  Descent is therefore controlled by \(m_A+m_B\) parity.  The simultaneous antipodal map \(A\) is a different symmetry.
- Factor trace-free tensor harmonics on one \(S^2\) have rough eigenvalue \(\ell(\ell+1)-4\), and \(\mathring R=-1\) on the factor trace-free block.  Thus the product eigenvalue is
  \[
  P=\frac{\ell_F(\ell_F+1)+\ell_O(\ell_O+1)}2-1,
  \]
  with the first K-odd quotient factor-TF modes giving \(P=2\), not \(4\).  One such electric-type example has \(\ell_F=2,m_F=2,\ell_O=0\); Step 91 TTCS notes that an \(m=0\) magnetic tensor harmonic is also K-odd at the same eigenvalue, so a complete tensor-harmonic proof must include both electric and magnetic families.
- In the mixed AB one-form block, \(\ell_A\) and \(\ell_B\) are independent and
  \[
  P=\frac{\ell_A(\ell_A+1)+\ell_B(\ell_B+1)}2-1,
  \]
  with minimum \(P=1\) at \((\ell_A,\ell_B)=(1,1)\).  Factor interchange relates symmetry-conjugate coefficients; it is not a restriction \(\ell_A=\ell_B\).

With these corrections, the spectral lower bound in the K-odd quotient tensor sector remains \(P\ge1\): the nonpositive scalar/shape directions are K-even or fail to descend in their K-odd real component, AB one-form modes start at \(P=1\), and factor-TF modes start at \(P=2\).  The corrected executable ledger is `workspace/scripts/step91_corrected_spectral_ledger.py`, with data `workspace/data/step91_corrected_spectral_ledger.json`.

The positivity is only a bilinear-form fact on the K-odd linear sector.  It does not determine the sign of off-diagonal Green values, and it does not complete the nonlinear gluing comparison.

## 8. Step 91 receiver simplification

Step 91 also removes a spurious receiver uncertainty.  At the product background,
\[
R_0\omega_2^+=R_0\omega_2^-=0,
\]
so first-order variations of the insertion frame, Hodge splitting, or length normalization pair with zero curvature.  The odd receiver selects only the four-distinct product-index component.  Since product curvature is supported only in one factor at a time, all curvature-times-\(h_0\) corrections to this odd component vanish.

Consequently, in product normal coordinates the full linear odd receiver is exactly the sparse second-jet functional from Step 89:
\[
R_{\rm odd}(H)=\frac12\left(H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01}\right).
\]
This was verified on the full 100-dimensional symmetric-Hessian basis in `workspace/scripts/step91_receiver_simplification.py`, data `workspace/data/step91_receiver_simplification.json`.  For the \(\ell=1\) coexact-coexact AB modes at NN, only the axial mode \((*dZ_A)\odot(*dZ_B)\) has nonzero odd receiver in this functional; V0-nonzero equatorial modes do not acquire an extra odd receiver from frame/background curvature.

## 9. What remains after K-symmetry and Step 91

The K-reflection proves cross-parity vanishing and removes odd-sector self singularities for the K-equivariant **linear pairwise** background problem.  The language "at any order" in the first version should be read only for natural linear constructions respecting K; nonlinear multi-source terms and a particular Ozuch/Biquard chart still require explicit compatibility.

For the checkerboard assignment, \(\varepsilon_i\varepsilon_j-1\) vanishes for self terms and also for the two-factor diagonal companions \((NN,SS)\) and \((NS,SN)\).  These companions are not being identified by the quotient; they vanish only because \(\varepsilon_i\varepsilon_j=1\).  Thus each radial equation has only adjacent opposite-chirality sources:
\[
\Delta_i=t_i\sum_{j\sim i} t_j^2(\varepsilon_i\varepsilon_j-1)K_{ij}^{11},
\]
where \(j\sim i\) means the two nodes differ in exactly one factor.  L- and factor-exchange symmetries can then identify all adjacent coefficients after the source and receiver frames are normalized consistently.  A sum over receivers is not itself the radial system.

The remaining mathematical target is therefore the intrinsic adjacent coefficient \(K_{\rm adj}^{11}\): a finite off-diagonal Green transfer in the K-odd linear sector, with the singular source and Ozuch radial normalization matched to the same convention.  Its sign and full value remain unknown.

## 10. Files and verification

- Main computation: `workspace/scripts/step90_K_symmetry_chirality_exchange.py`
- H⁴ transport fix: `workspace/scripts/step90_K_H4_transport_fix.py`
- Main data: `workspace/data/step90_K_symmetry_chirality_exchange.json`
- Transport data: `workspace/data/step90_K_symmetry_H4_transport_fix.json`
- Step 89 corrected note: `workspace/notes/step89_correction_and_relative_green.md`
- Step 88 corrected note: `workspace/notes/step88_four_node_structural_theorem.md`

## 11. Meaning for Yau–26

The K-symmetry substantially simplifies the product-orbifold positive-branch calculation by reducing a multi-sector, self-singular problem to a single finite off-diagonal odd–odd sum.  Combined with the existing A, J, L symmetries:

- A eliminates odd scalar modes.
- J fixes insertion direction and eliminates transverse projections.
- L exchanges A-orbits and gives $B=\begin{pmatrix}a&b\\b&a\end{pmatrix}$.
- **K exchanges chirality at each node, eliminates all cross-parity sectors, and gives geometric annihilation of the negative shape mode.**

This does not prove or disprove Einstein existence on $\#_3(S^2\times S^2)$ and does not solve Yau Problem 26.  It concentrates the constructive positive-branch question into a well-defined finite spectral/Green problem.  The restricted IL negative-branch theorem remains the strongest direct Yau-26 asset.
