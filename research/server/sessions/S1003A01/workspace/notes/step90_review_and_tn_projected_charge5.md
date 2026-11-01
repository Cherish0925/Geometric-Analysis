# Step 90 — Review of the endpoint stabilizer, the actual projected charge-five field on Taub–NUT, and the Wahl twist correction

Session S1003A01, Agent4, Execute.

Artifacts:
- `workspace/notes/step89_endpoint_jet_stabilizer_and_derivative_ladder.md` (corrected in this Step);
- `workspace/scripts/step90_tn_sigma_projection.py` → `workspace/data/step90/tn_sigma_projection.json`;
- `workspace/scripts/step90_tn_sigma_exact.py` → `workspace/data/step90/tn_sigma_exact.json`;
- `workspace/scripts/step90_tn_sigma_symbolic.py` → `workspace/data/step90/tn_sigma_symbolic.json`.

## 1. What survives from Step 89

The first-order result is useful and precise. At the ideal O10 endpoint, the pair
\((\Phi,\nabla\Phi)\) is a single \(\operatorname{Spin}^c(4)\)-orbit with circle stabilizer, and this circle acts nontrivially on every \(L^m\), \(m\ne0\). Hence every equivariant charged section built pointwise from that first jet vanishes on the ideal orbit. This rules out a nonzero-modulus first-jet section for the rank-one transgression.

At the calibrated finite-density augmented endpoint for the bounded resolvent field \(v\), the charge-five component of \(\nabla v\) is one-dimensional and the standard section
\[
 \sigma=\Phi\wedge t(v)\in L^5
\]
extracts it. This explains the exponent five in the completed finite-density proof. It does not establish an analogous endpoint theorem for the local tensor \(\nabla\tau\).

Two stronger statements in the original Step-89 note did not follow:

1. formal differential order does not imply that the derivative of every projected section pays the full \(\|\nabla^2\tau\|_2\) cost; contractions and the actual field equations can cancel tensor components;
2. the calibrated \(|c|=1\) endpoint is not the proposed \(c\)-depleted nut phase, so the residual \(\mathbb Z_5\) description does not classify that phase.

The Step-89 note has been edited accordingly. The delayed independent verifier (`trace/ttcs/results/step89_ttcs01_verifier1_integration.md`) confirmed the first-jet orbit/stabilizer and charge-five representation, and added three further corrections now incorporated there: the finite-density one-mode theorem concerns \(\nabla v\), not automatically \(\nabla\tau\); the weight multiset is \(\{-2,-1,1,1,2,2,4,5\}\); and the proposed rank-two Chern inference is false because point degree is \(H^1\)-cheap in four dimensions. Density-free O10 has **not** been reduced to exactly two alternatives.

## 2. Direct test on the exact Taub–NUT carrier

The Step-47 tensor norms alone cannot answer whether the analogous local charge-five projection retains the uncontrolled curvature contribution. I therefore evaluated \(\Phi\wedge t(\tau)\) on the exact Taub–NUT core, where the cubic operation \(t(\tau)\) is algebraic in \((\tau,\nabla\tau)\). This is a local-model analogue of the finite-density resolvent construction \(\Phi\wedge t(v)\), not an identification of \(v\) with \(\tau\) at derivative level.

Use the hyperkähler complex structure \(I_3\), its parallel Kähler spinor frame
\[
 S^+=\Lambda^{0,0}\oplus\Lambda^{0,2},\qquad S^-=\Lambda^{0,1},
\]
and
\[
 \Phi_{\rm TN}=\sqrt{\rho_*}\,e_1+a\bar f e_2,
 \qquad \bar f=x_1-i x_2,
 \qquad v=\tau_{\rm TN}=\sqrt{m_*/2}\,d\bar f .
\]
The script implements Clifford multiplication on \(\Lambda^{0,*}\). It first reconstructs the exact Step-47 torsion from \(\Phi_{\rm TN}\) with relative residual below \(5\times10^{-16}\). It then computes
\[
 Q=\nabla v=\sqrt{m_*/2}\,\operatorname{Hess}\bar f,
 \qquad \sigma_{\rm TN}=\Phi_{\rm TN}\wedge t(v),
 \quad t(v)\text{ evaluated algebraically from }(v,Q).
\]
In the chosen parallel trivialization the result is
\[
 \boxed{\sigma_{\rm TN}
 =\sqrt{\frac{8388608}{1594323}}\,
   \frac{\ell\,\bar f}{(r+\ell)^3}.}
 \tag{90.1}
\]
An independent symbolic computation, differentiating before specializing the azimuth, gives
\[
 \sigma_{\rm TN}|_{\varphi=0}
 =\frac{2048\sqrt6}{2187}\frac{\ell r\sin\theta}{(r+\ell)^3}
\]
with exact residual zero; axial equivariance restores \(e^{-i\varphi}\). This equals (90.1) because \((2048\sqrt6/2187)^2=8388608/1594323\). The numerical evaluation at five generic points gives the same constant with maximum squared-constant residual \(9.8\times10^{-15}\). The field vanishes at the nut and decays like \(\ell r^{-2}\) at infinity. Its ordinary Dirichlet energy is scale-invariant, exactly the critical behavior relevant to a dense nut phase. Thus the exact nut is indeed \(c\)-depleted in the charge-five projection: it does not approximate the positive constant-modulus endpoint section.

The contraction is not identically zero. In particular, the uncontrolled second derivative is not annihilated completely by the charge-five projection. However, it is substantially more structured than the full tensor norm: it reduces to one explicit dipole mode. For the ordinary differential in the parallel trivialization,
\[
 \int_{\rm TN}|d\sigma_{\rm TN}|^2
 =\frac{268435456\pi^2}{55801305},
 \tag{90.2}
\]
while
\[
 \int_{\rm TN}|\sigma_{\rm TN}|^2
 =\frac{67108864\pi^2}{4782969}\,\ell^2.
 \tag{90.3}
\]
Equation (90.2) deliberately omits the \(L^5\) connection term; it records only the scalar differential of (90.1). Its distribution is also exact:
\[
 \int_{B_R}|d\sigma_{\rm TN}|^2
 =\frac{268435456\pi^2R^3
 (3R^4+21R^3\ell+63R^2\ell^2+35R\ell^3+35\ell^4)}
 {167403915(R+\ell)^7}.
 \tag{90.4}
\]
Thus the inner contribution is \(O((R/\ell)^3)\) as \(R/\ell\to0\), while the exterior tail is
\[
 \frac{536870912\pi^2}{4782969}(\ell/R)^3+O((\ell/R)^4).
\]
The critical energy is concentrated at the core scale \(r\asymp\ell\), not at the nut or in a long exterior tail. The gauge-invariant amplitude already gives a connection-independent lower bound: exact radial integration yields
\[
 \int|d|\sigma_{\rm TN}||^2
 =\frac{67108864\pi^2}{33480783}
 =\frac5{12}\int|d\sigma_{\rm TN}|^2.
 \tag{90.5}
\]
Hence Kato implies \(\int|\nabla^{5A}\sigma_{\rm TN}|^2\ge(90.5)\) for every unitary connection on this fixed section; no connection can cancel the amplitude cost. The remaining value of a covariant calculation is its phase and boundary trace, not another total-energy coefficient. TN-AdS/null-background corrections and transfer to actual endpoint sequences remain unresolved.

### Interpretation

This calculation sharpens, but does not settle, the O10 fork.

- The projected charge-five field retains a nonzero critical core mode, so there is no complete algebraic cancellation.
- Its zero locus is not merely the nut: \(\bar f=0\) gives two-dimensional zero sheets over the \(x_3\)-axis reaching every truncation boundary. On a flux-radius block \(R_\ell\asymp\ell^{1/3}\), for each fixed \(b>0\),
\[
 \frac{\operatorname{Vol}\{|\sigma_{\rm TN}|>b\}}
 {\operatorname{Vol}(B_{R_\ell})}=O_b(\ell^{1/2})\to0.
\]
Thus it is depleted in measure and supplies no nowhere-zero outer phase trivialization or positive-modulus input for the finite-density rank-one argument.
- The full \(\int|\nabla^2\tau|^2\) budget is too coarse. The next meaningful quantity is the **covariant energy and phase flux of the explicit dipole (90.1)** after insertion into a compatible finite marked block. One must include the determinant connection, transition functions, compensators, and boundary matching. A per-core divergence is not by itself a contradiction because the topology may be localized precisely where \(|\sigma|\) vanishes.
- The finite-density proof also uses the curvature budget earlier to obtain the mass-gradient and constant-modulus conclusions for the resolvent section. Bounding only the projected derivative cannot bypass that independent issue.

The determinant-line square and the nut's rank-two/Weyl charge must also be separated. The inherited fit
\[
 F_A=F_0+e,\qquad |F_0|\le C,\qquad\|e\|_{2,\mathrm{av}}\to0
\]
implies that for normalized-volume-vanishing sets \(U_j\),
\[
 \left|V_j^{-1}\int_{U_j}F_A\wedge F_A\right|
 \le2C^2\mu_j(U_j)+2\|e_j\|_{2,\mathrm{av}}^2\to0.
\]
In a phase with \(N\asymp V/\ell^2\) nuts, fixed rescaled cores occupy only \(O(\ell^2)\) normalized volume. They can carry \(W^-\) and rank-two degree, but not the nonzero normalized Chern–Weil square of \(L^5\). A singular zero-current representation would require its own relative transgression and boundary matching.

There is a useful continuity shortcut for the bounded resolvent. Under the inherited common-connection hypotheses
\[
 \|v-\tau\|_{H^1,\mathrm{av}}\to0,
 \quad |v|\le C,
 \quad\||\tau|^2-m_*\|_{2,\mathrm{av}}\to0,
\]
truncation gives \(\|v-\tau\|_{4,\mathrm{av}}\to0\). Hölder applied to the cubic formula then gives
\[
 \|\Phi\wedge[t(v)-t(\tau)]\|_{1,\mathrm{av}}\to0.
\]
Thus an actual raw section depleted in measure cannot be converted into positive constant modulus merely by an \(H^1\)-close bounded resolvent. This transfers depletion in measure, not derivative energy, and still presupposes a common-connection physical block approaching the model.

Thus Step 90 replaces a formal derivative-count assertion with an actual projected model. The next finite-block question is a relative phase/curvature matching problem: can the depleted exterior and its zero-sheet traces coexist globally with the determinant square and actual equations, or must compensators pay elsewhere?

## 3. Wahl spin\(^c\) characters

The Step-89 Wahl paragraph conflated two families of characters. For the Milnor fibre \(B_{n,1}\),
\[
0\to H^2(B)=\mathbb Z_n\to H^2(\partial B)=\mathbb Z_{n^2}
 \to H^3(B,\partial B)=\mathbb Z_n\to0,
\]
and the image is \(n\mathbb Z_{n^2}\). The script tested twists \(\zeta^{nj}\), exactly the boundary characters extending over the rational ball. They are not the extra complement cosets in A02's sequence.

For a general twist \(\zeta^r\), the positive spinor weights are \((r,r-n)\). In particular \(r=1\) permits an invariant first derivative, so \(\nabla\Phi(p)=0\) is valid for the tested extendible family, not for every orbifold spin\(^c\) structure. For \(r=nj\), this vanishing holds for every \(n\ge2\) by congruence, not merely the sampled range. The almost-Kähler isotropy calculation is separate and survives: an invariant self-dual form is \(\pm\omega_0\), and its torsion has a forced high-order zero at the cone point under the recorded hypotheses. For \(n=2\), the script's torsion first-jet dimension four is complex dimension four (real dimension eight before differential compatibilities).

No monopole consequence can be attached to the Wahl candidate until an actual supplied orbifold spin\(^c\) class is identified. Smooth filler transfer proves scalar and mixed-curvature inequalities but does not itself produce such an orbifold monopole. Even a correctly forced local zero still needs a quantitative global consequence.

## 4. Scientific judgment across Q1–Q4

- **Q1.** The Wahl orbifold gives a real exact-existence alternative: a non-Kähler negative Einstein metric on it would yield \(\alpha(X\#4\overline{\mathbb{CP}}^2)=0\) after Ricci-flat filling. The present isotropy calculation neither constructs nor excludes such a metric. The next useful input would be an actual orbifold field supplier, or a deformation/Einstein argument on the realized complement; unconstrained character enumeration should stop.
- **Q2/Q3.** Neither the stabilizer nor the TN projection changes the certified sub-unit smooth tariff, its lack of matching all-metric lower bound, or the global attainment problem.
- **Q4.** The first-jet stabilizer explains why canonical-line information first appears through curvature or second jets. It does not establish a closed Goldberg theorem. The exact dipole calculation reinforces the general lesson that one must use projected differential equations and global transport rather than full-tensor derivative norms.

The strongest immediate continuation is constructor work on the **relative phase and curvature matching** of (90.1) on a finite marked TN/TN-AdS block: retain the zero-sheet traces, determinant connection and transition functions, and determine whether block matching forces nonzero global payment or permits charge compensation. Kato has already settled survival of a positive amplitude-energy component on the fixed model, so another total covariant coefficient is not the objective. In parallel, if A02 identifies a genuinely supplied Wahl orbifold class, its exact boundary character should be inserted into the corrected isotropy calculation before any Einstein conclusion is attempted.
