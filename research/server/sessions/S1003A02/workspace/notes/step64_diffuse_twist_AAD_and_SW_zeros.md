# Step 64 — The diffuse frame-twist target, what the AAD transport identity controls, and why the SW Bloch field is singular

Agent3, Execute.  The shell remained unavailable, so the exact local check was derived and staged rather than executed.  This note corrects the route judgment after Step 63: neither a positive per-class tariff nor a \(k^2/A\) law is presently favored by the proved inequalities.

## 1. The actual low-defect construction target supplied by Theorem 63.T

Let \(M=X\#k\overline{\mathbb {CP}}^{\,2}\), let \(a=a_\varepsilon\) be a sign class maximizing \((a^+)^2\), and let \(h_a^-\) denote the harmonic ASD representative normalized so that \([2\pi h_a^-]=2\pi a^-\).  For a smooth orthogonal almost-complex structure \(J\) with \(c_1(J)=a\), write
\[
 \gamma_J^-=\rho_0^J+t_J^-,\qquad t_J^-=(\alpha\wedge\beta)^-,
\]
with the sign understood as in (63.1); in the almost-Kähler convention \(t_J^-=-(a\wedge Ja)^-\).  If \(P=o(k)\), Theorem 63.T and Hodge orthogonality require
\[
 \|\rho_0^J\|_2=o(\sqrt{k}),\qquad
 \|t_J^-\|_2=2\pi\sqrt{k+\Pi}+o(\sqrt{k}),
\tag{64.1}
\]
and the efficient version is stronger:
\[
 t_J^-=-2\pi h_a^-+o_{L^2}(\sqrt{k}),
\tag{64.2}
\]
up to the convention sign.  Thus the exceptional classes should be nearly ASD (\(\Pi\simeq0\)), their harmonic representatives should be diffuse, and the rotation of the \((2,0)\)-plane should have an ASD quadratic twist nearly equal to the harmonic flux.

For an almost-Kähler structure put \(u=|\nabla\Omega|^2/4\).  Then
\[
 |t_J^-|^2=\frac{u^2}{2},
\]
so (64.1) forces
\[
 \frac12\int_Mu^2\ge4\pi^2(k+\Pi)-o(k).
\tag{64.3}
\]
At the negative-KE volume scale \(V\simeq2\pi^2A\), the smallest diffuse RMS size is
\[
 u_{\rm rms}\ge 2\sqrt{\frac{k+\Pi}{A}}+o(\sqrt{k/A}),
 \qquad |\nabla\Omega|_{\rm rms}\asymp (k/A)^{1/4}.
\tag{64.4}
\]
This corrects the old common mode: its torsion \(u=k/A\) is too small by a square root to carry the ASD Chern flux.  But (64.4) does **not** imply a tariff.  For \(k/A\ll1\), this torsion lies in the negative window of the exact identity
\[
 P=2\|\gamma_J^-\|^2+\int u(5u+s)+2\|\rho_*''\|^2+4\|W_3^+\|^2.
\tag{64.5}
\]
The positive \(W_2/W_3\) energy needed to balance the negative linear torsion term can be financed by the simultaneous deletion of the Kähler-type \(W_1\) component; (64.5) is exactly the negative Goldberg balance.  Hence neither 62.W nor 62.G follows from 63.T.

**Construction problem 64.C.**  Construct, or obstruct, a sequence \((g_j,J_j)\) with the following properties simultaneously:
1. \(g_j\) is the scalar \(-4\) Yamabe representative and \(P(g_j)=o(k)\) (or has a prescribed smaller scale);
2. \(c_1(J_j)=a_{\varepsilon_j}\), \(\Pi_j=o(k)\), and (64.2) holds;
3. \(u_j\) is diffuse with RMS size \(2\sqrt{k/A}\), while its unavoidable zeros/transition cores occupy vanishing volume;
4. the actual Levi-Civita Gauss/Ricci/Bianchi equations hold, not only the pointwise algebraic identities.

This is the precise cheap-state template to test.  It is more informative than a collection of nearly unit-cost local cells, which never enters the diffuse scale.

## 2. A quantitative weak form of the AAD transition identity

For every almost-Kähler four-manifold, AAD Corollary 1 gives, since \(\kappa-s=6u\),
\[
\boxed{
2d^Ju=
2\langle\delta W_3^+,\Omega\rangle
+2\delta\rho_*''
-\langle\rho_*'',\nabla_J\Omega\rangle
+\langle A^+,\Omega\rangle,
}
\tag{64.6}
\]
where
\[
 A_Z=(d^\nabla\operatorname{Ric}'')_Z+\iota_{JZ}d\rho,
 \qquad d\rho=*\bigl(J\delta\operatorname{Ric}''\bigr).
\]
The last identity is AAD (26), so the derivatives in \(A\) involve the anti-Hermitian Ricci tensor, not a new curvature component.

Integrate (64.6) against a smooth one-form \(\eta\).  Integrating each divergence term by parts and using \(|\nabla\Omega|=2\sqrt u\) gives a universal algebraic constant \(C\) such that
\[
\begin{split}
2|\langle d^Ju,\eta\rangle|
\le C\bigl(&\|W_3^+\|_2+\|\rho_*''\|_2+\|\operatorname{Ric}''\|_2\bigr)\\
&\times\bigl(\|\nabla\eta\|_2+\|\sqrt u\,\eta\|_2\bigr).
\end{split}
\tag{64.7}
\]
No derivative of curvature remains in (64.7).  Thus, for the weighted negative norm
\[
 \|\xi\|_{\mathcal H_u^{-1}}
 :=\sup_{\eta\ne0}\frac{|\langle\xi,\eta\rangle|}
 {\|\nabla\eta\|_2+\|\sqrt u\,\eta\|_2},
\]
one has
\[
 \|d^Ju\|_{\mathcal H_u^{-1}}
 \le C\bigl(\|W_3^+\|_2+\|\rho_*''\|_2+\sqrt P\bigr).
\tag{64.8}
\]
Using (64.5), a weaker closed estimate is
\[
 \|d^Ju\|_{\mathcal H_u^{-1}}^2
 \le C\left[P+\int u(|s|-5u)_+\right].
\tag{64.9}
\]
Equations (64.7)--(64.9) are the rigorous scale at which AAD transports torsion amplitude into curvature components.  They control only the nonconstant part of \(u\).  They do not control the mean diffuse mode, the orientation of \(t_J^-\), or its harmonic projection.

### Why (64.8) does not yet give a gap

A positive constant value of \(u\) is topologically impossible in the open range because the Nijenhuis section has
\[
 c_2(T^{1,0}\otimes K^{-1})=5\chi+6\tau=c_2(X)+2A-k\ne0.
\]
But topology does not impose a quantitative size on the zero cores.  A profile equal to \(u_0\) away from finitely many balls of radius \(\epsilon\), and vanishing inside them, has
\[
 \|u-u_0\|_2^2=O(u_0^2\epsilon^4)
\]
per isolated core.  Its derivative therefore tends to zero in the natural exact \(H^{-1}\) scale.  A degree-one phase of the Nijenhuis section on the linking \(S^3\) has critical boundary energy, but the bulk \(L^2\) energy of its first derivative scales like \(u_0\epsilon^2\) and can vanish.  The four-dimensional \(L^2\) curvature scale is therefore supercritical for pricing isolated zeros solely through their degree.

Consequently, the desired estimate
\[
 \|t_J^-\|_2\le C\bigl(\|W_3\|_2+\|\rho_*''\|_2+\sqrt P\bigr)
\tag{64.10}
\]
does not follow from (64.6): (64.6) annihilates the constant mode and sees no quantitative radius for the topologically required cores.  A theorem of the form (64.10) needs additional input that couples the **harmonic projection and orientation** of \(t_J^-\) to the second AAD Bianchi identity, or an elliptic/noncollapse statement that prevents the Nijenhuis zeros from concentrating.  This is exactly the global information missing from arbitrary near-minimizers.

The second AAD identity does contain the orientation information,
\[
0=(d u\wedge Z^\flat)''+\frac\kappa4\nabla_{JZ}\Omega-\nabla_{\rho_0(Z)}\Omega
+2(\delta W_3^+)_Z''+\nabla_{\rho_*''(Z)}\Omega
+(\nabla_{JZ}\rho_*'')''+(A_Z^+)''.
\tag{64.11}
\]
However, pairing it with \(\nabla\Omega\) is the negative-scalar Goldberg problem: the zeroth-order term has the noncoercive sign that allows strict almost-Kähler negative Einstein geometry.  Steps 43 and 63 already identified the resulting derivative loss.  Thus (64.11) is a genuine route only with a new spectral/noncollapse input, not by Cauchy--Schwarz alone.

## 3. The SW-selected Bloch field does not directly enter Theorem 63.T

Let \(\Phi\) be a positive spinor, \(\rho=|\Phi|^2\), and on \(\{\Phi\ne0\}\) let
\[
 n=\frac{q(\Phi)}{|q(\Phi)|}:M\setminus Z(\Phi)\to S(\Lambda^+)
\]
be its unit Bloch direction.  Theorem N controls the weighted quantity
\[
 \int\rho^2|\nabla n|_{\mathcal W_2}^2.
\]
Theorem 63.T instead requires a smooth nonvanishing orthogonal almost-complex form on all of \(M\), and controls the unweighted quadratic twist of its moving frame.  These are not the same object near a spinor zero.

### Proposition 64.H (the transverse-zero model)

Suppose \(\Phi:\mathbb R^4\to\mathbb C^2\) has a nondegenerate zero at the origin.  After bounded linear changes, its leading unit spinor is \(x/r:S^3\to S^3\), and its Bloch field is the radial Hopf map
\[
 n(x)=\frac1{r^2}
 \bigl(2(x_1x_3+x_2x_4),\ 2(x_2x_3-x_1x_4),\ x_1^2+x_2^2-x_3^2-x_4^2\bigr).
\tag{64.12}
\]
Then
\[
 |\nabla n|^2=\frac8{r^2},\qquad
 |n^*\omega_{S^2}|^2=\frac{16}{r^4}.
\tag{64.13}
\]
For \(\Omega=\sqrt2\,n\) and a moving orthonormal frame of \(\Omega^\perp\),
\[
 |(\alpha\wedge\beta)^-|^2=\frac8{r^4}.
\tag{64.14}
\]
Therefore on an annulus \(\epsilon<r<R\),
\[
 \int|\nabla n|^4=128\pi^2\log(R/\epsilon),\qquad
 \int|(\alpha\wedge\beta)^-|^2=16\pi^2\log(R/\epsilon).
\tag{64.15}
\]
By contrast, because \(\rho\asymp r^2\),
\[
 \int_{B_R}\rho^2|\nabla n|^2=O(R^6),
 \qquad \int_{B_R}\rho|\nabla n|^2=O(R^4).
\tag{64.16}
\]
The boundary map \(n|_{S^3}\) is the nontrivial Hopf class in \(\pi_3(S^2)\), so it cannot be filled by a smooth unit self-dual form inside the ball while it is kept fixed outside.

*Proof.*  The Hopf map on the unit \(S^3\) has two horizontal singular values equal to \(2\), giving (64.13).  In a tangent frame of \(S^2\), \(\alpha\) and \(\beta\) are orthogonal of squared norm \(4/r^2\); a decomposable two-form has equal SD and ASD norms, giving (64.14).  Since \(|S^3|=2\pi^2\), radial integration gives (64.15).  The weighted estimates are immediate.  The homotopy statement is the defining Hopf class.  The exact algebra has been staged in `workspace/scripts/step64_hopf_spinor_twist.py`.

**Consequences.**
1. The Bloch field of a generic isolated SW spinor zero is not a global orthogonal almost-complex structure.  It cannot be repaired only inside a small ball without altering the exterior homotopy data.
2. Even on the punctured ball its unweighted \(L^4\) rotation and \(L^2\) frame twist diverge logarithmically.  Thus no estimate of the 63.T twist by Theorem N's weighted rotation can hold without explicit zero-set boundary terms.
3. Theorem N is intentionally blind to this singularity: the amplitude weight makes the local contribution tend to zero as \(R^6\).
4. A usable canonical-field theorem must retain the determinant connection and the zero indices, rather than normalize the spinor and then invoke 63.T.  Equivalently, one needs a punctured Gauss formula with boundary Hopf/zero charges, or a different smooth field supplier.

This is a structural obstruction to Q3 of Step 63, not merely a missing estimate.  The external literature retrieved this step supplies frequency and weighted control for Dirac/SW zero sets, but no four-dimensional theorem controlling the unweighted normalized-spinor twist; this absence is consistent with the local logarithmic model.

## 4. What remains mathematically live

The two serious alternatives are now sharper.

### Lower-bound route
Prove a harmonic-projection estimate for a **smooth** best-class \(J\):
\[
 \|\mathsf H^-(t_J^-)\|_2^2
 \le C\,\mathcal E_{\rm geom}(g,J),
\tag{64.17}
\]
where \(\mathcal E_{\rm geom}\) is controlled by \(P\) together with already priced Weyl/Yamabe terms, and where the quantifiers exclude collapsed interfaces only through a proved global alternative.  AAD (64.6) controls amplitude variation, while (64.11) is the necessary orientation equation.  Neither alone proves (64.17).

### Construction route
Realize (64.2)--(64.4) with tiny topological zero cores.  The twist should be nearly harmonic and diffuse, while \(W_2/W_3\) implement the negative Goldberg balance.  A construction would refute every positive per-class tariff and determine whether the remaining scale is \(k^2/A\), smaller, or zero.  Local cells do not test this regime.

### Conditional theorem that is already available
If an Anderson-type selected near-minimizer decomposition supplies a noncollapsed smooth bulk and a uniform lower harmonic radius at every Nijenhuis/field-transition core, then the AAD identities and local trace estimates can price the finitely many cores.  Without such an entrance, shrinking cores and collapsed interfaces remain genuine escape mechanisms.  This is why the unrestricted lower bound still cannot be inferred from the local EH/Burns theory.

## 5. Status and route judgment

- The diffuse-twist scale (64.3)--(64.4) is a direct consequence of the verified Theorem 63.T.
- The weak transport estimate (64.7) is obtained directly from AAD Corollary 1 by integration by parts; it has no curvature-derivative assumption.
- Proposition 64.H is an elementary exact local calculation; its script is staged but not executed because the shell lease is still blocked.
- The conclusion about canonical SW normalization is exact for a transverse isolated zero.  General SW zero sets may be more singular, not better for the unweighted critical norm.
- No positive tariff, \(k^2/A\) bound, or cheap closed construction follows yet.  The proved work identifies the correct construction and the precise analytic obstruction: the harmonic projection of quadratic frame twist, including zero/core and collapse data.

## 6. Verification and strengthening (TTCS step64_ttcs01/02) — BINDING

Sources: `trace/ttcs/results/step64_ttcs01_verifier1_integration.md`, `step64_ttcs01_generator1_integration.md`, and the targeted independent check `step64_ttcs02_verifier1_integration.md`.

### 6.1 Corrections to §§1–4

1. **The harmonic projection, not the full twist, is fixed.**  With \(\mathsf H^-\) the harmonic ASD projection and \([h_a^-]=a^-\),
   \[
   \boxed{\mathsf H^-(t_J^-)=2\pi h_a^- -\mathsf H^-(\rho_0^J),\qquad
   \|\mathsf H^-(t_J^-)-2\pi h_a^-\|_2\le\sqrt{P/2}.}
   \tag{64.18}
   \]
   Thus \(P=o(k)\) gives only
   \(\|t_J^-\|_2\ge2\pi\sqrt{k+\Pi}-\sqrt{P/2}\).  Equality of its norm and the nearly-harmonic ansatz require the extra efficiency hypothesis
   \(\|(1-\mathsf H^-)t_J^-\|_2=o(\sqrt k)\).  Under it the sign is **positive**:
   \(t_J^-=2\pi h_a^-+o_{L^2}(\sqrt k)\).  The sign in (64.2) is withdrawn.

2. **Exact quartic torsion scale.**  In the AK case,
   \[
   \frac12\int u^2\ge(2\pi\sqrt{k+\Pi}-\sqrt{P/2})_+^2.
   \tag{64.19}
   \]
   At the additional volume hypothesis \(V=2\pi^2A(1+o(1))\),
   \[
   u_{\rm rms}\ge2\sqrt{(k+\Pi)/A}(1-o(1)),\quad
   \langle|\nabla\Omega|^4\rangle^{1/4}\ge2\sqrt2((k+\Pi)/A)^{1/4}(1-o(1)).
   \]
   The old phrase \(|\nabla\Omega|_{\rm rms}\) is replaced by normalized \(L^4\) size.  Diffuseness is a construction hypothesis, not a consequence.  For an arbitrary orthogonal \(J\),
   \[
   \int|\nabla\Omega|^4\ge32(2\pi\sqrt{k+\Pi}-\sqrt{P/2})_+^2.
   \tag{64.20}
   \]

3. **Nijenhuis cores.**  The scaling model shows only that isolated zero index plus the first AAD amplitude identity imposes no fixed per-core \(P\)-cost.  Four-dimensional \(L^2\) curvature is critical, not supercritical; the subcritical quantity is the bulk \(L^2\) first-derivative energy of the section.  No actual AK metric implant or Yamabe-normalized low-defect construction has been proved.  A lower harmonic radius does not by itself convert the core's second-jet/Weyl energy into Ricci defect.  The conditional assertion at the end of §4 is withdrawn.

4. **General transverse spinor zero.**  The exact coefficients \(128\pi^2\) and \(16\pi^2\) hold when the invertible leading derivative \(L:\mathbb R^4\to\mathbb C^2\) is conformal.  In general
   \[
   \int_{\epsilon<r<R}|\nabla n|^4=C_4(L)\log(R/\epsilon)+O(1),\quad
   \int|t_J^-|^2=C_t(L)\log(R/\epsilon)+O(1),
   \]
   with \(C_4(L),C_t(L)>0\).  The linking Hopf invariant is \(\operatorname{sign}\det_{\mathbb R}L\).  For best-sign bundles the total signed zero count is \(c_2(S^+)=0\), so charges can pair globally; this does not remove the local logarithms or supply a uniform repair.  The zero-free case still leaves the main \(L^2\)-to-\(L^4\) gap.

### 6.2 New exact AAD harmonic-flux identity

Let \((g,J,\Omega)\) be almost-Kähler with constant scalar curvature \(s\), put \(V_X=\nabla_X\Omega\), and let \(h\) be harmonic ASD.  Define \((\eta_h)_Z=V_{h(Z)}\).  The algebraic contraction is
\[
 \sum_i\langle V_{Je_i},V_{h(e_i)}\rangle=-4\langle t^-,h\rangle.
\tag{64.21}
\]
Pairing AAD Corollary 1's second equation with \(\eta_h\) gives
\[
 \boxed{s\langle\mathsf H^-(t^-),h\rangle
 =\mathcal F_h-6\int u\langle t^-,h\rangle,}
\tag{64.22}
\]
where \(\mathcal F_h\) is the integral of the remaining \(du,\rho_0,W_3,\rho_*''\), and \(A\) terms displayed in the step64 TTCS integration.  At \(s=-4\),
\[
4\langle\mathsf H^-(t^-),h\rangle
=6\int u\langle t^-,h\rangle-\mathcal F_h.
\]
Without constant \(s\), the exact left side is \(\langle\mathsf H^-(s t^-),h\rangle\).

For every closed AK four-manifold, with no Gray or constant-s assumption,
\[
 \boxed{\|\nabla^2\Omega\|_2+\|\nabla\Omega\|_4^2\le C\|\operatorname{Rm}\|_2.}
\tag{64.23}
\]
This follows from the harmonic-form Weitzenböck equation, \(|\nabla\Omega|^2\le C|\operatorname{Rm}|\), and the bundle-valued Weitzenböck formula for \(V=\nabla\Omega\).  It closes the unrestricted smooth-AK second-jet estimate, but only at total-curvature/host scale.

After integration by parts,
\[
 |\mathcal F_h|\le C E_{\rm AAD}B_h,
 \quad E_{\rm AAD}=\|W_3^+\|_2+\|\rho_*''\|_2+\sqrt P,
\tag{64.24}
\]
with
\[
 B_h=\|h\|_\infty\|\operatorname{Rm}\|_2+
 \|\nabla h\|_4\|\operatorname{Rm}\|_2^{1/2}.
\]
Let \(T=\mathsf H^-(t^-)\), \(h=T/\|T\|_2\), \(r=t^--T\), and \(U=\|u\|_\infty\).  Then
\[
 \boxed{(4-6U)\|T\|_2\le C E_{\rm AAD}B_h+6U\|r\|_2}
\tag{64.25}
\]
when \(U<2/3\); the exact weighted coefficient uses \(\int u|h|^2\).  This finally tests the harmonic orientation of the twist, rather than only \(du\).

It is not yet a gap.  The exact AK identity gives, with \(S=\int u^2\), \(I=\int u\), and \(Q=2\|\rho_*''\|^2+4\|W_3\|^2\),
\[
 Q\ge(4/U-6)S-2\sqrt{PS}.
\tag{64.26}
\]
Thus at small diffuse amplitude the full norms in \(E_{\rm AAD}\) are necessarily large enough to finance the flux estimate.  A lower bound must exploit cancellation or spectral separation in the **specific tested contraction** \(\mathcal F_h\), not its full norms.  The independent A01 equations (message #834, `S1003A01/workspace/notes/step55_darboux_ricci_compatibility.md`) are consistent: their AAD Bianchi/Weitzenböck system retains exactly \(\rho_*''\) and \(W_3\), and the scalar Ricci projection is not coercive.

### 6.3 Smooth regularized spinor flux ledger

Let \(L=\det S^+\), choose the real-curvature convention \(f_{\mathcal A}=iF_{\mathcal A}\), \([f_{\mathcal A}]=2\pi a\), and on \(\{\Phi\ne0\}\) put \(v=\Phi/|\Phi|\), \(\beta=i\langle v,\nabla_{\mathcal A}v\rangle\).  With the compatible Bloch orientation,
\[
 \boxed{\gamma_J=f_{\mathcal A}-2d\beta=R(\Omega)+t_J.}
\tag{64.27}
\]
The numerator \(\lambda=|\Phi|^2\beta\) is smooth through zeros.  For \(\rho=|\Phi|^2\),
\[
 \beta_\delta=\frac\lambda{\rho+\delta},\quad
 w_\delta=\frac\rho{\rho+\delta},\quad
 \gamma_\delta=f_{\mathcal A}-2d\beta_\delta
\]
is a smooth closed representative of \(2\pi a\), and
\[
\boxed{\gamma_\delta^-=
 w_\delta(R(\Omega)^-+t_J^-)+(1-w_\delta)f_{\mathcal A}^-
 -2(dw_\delta\wedge\beta)^-.}
\tag{64.28}
\]
Pairing (64.28) with harmonic ASD \(h\) is an exact finite ledger dividing the flux among weighted geometric twist, the low-amplitude ASD determinant-curvature reservoir, and an amplitude-transition term.  For finitely many fixed transverse zeros, the last term is \(O(\delta(1+|\log\delta|))\), yielding the finite \(L^1\) pairing
\[
 \int\langle t_J^-,h\rangle
 =2\pi\langle h_a^-,h\rangle-
 \int\langle R(\Omega)^-,h\rangle.
\tag{64.29}
\]
This does not recover the \(L^2\) bound of 63.T.

The degree-four zero ledger is
\[
 \gamma_J^2-f_{\mathcal A}^2
 =4d(\beta\wedge d\beta-\beta\wedge f_{\mathcal A}),
\tag{64.30}
\]
with local Hopf index \(q_z=(4\pi^2)^{-1}\int_{S_z^3}\beta\wedge d\beta\).  Using linking-sphere orientation,
\[
 \int_{M\setminus Z}\gamma_J^2
 =4\pi^2a^2-16\pi^2\sum_zq_z.
\tag{64.31}
\]
For best-sign classes \(\sum q_z=c_2(S^+)=0\).  The regularization is a smooth **connection-curvature ledger**, not a smooth unit Bloch field.  The open SW problem is now exact: jointly price the low-amplitude \(f_{\mathcal A}^-\) reservoir and transition term in (64.28) using the actual SW equations and Theorem N.  The self-dual SW equation alone does not control \(f_{\mathcal A}^-\).

### 6.4 Construction implications

TTCS supplied two useful models, neither a solution:
- an exact AK family \(\Omega_\epsilon=\Omega_0+\epsilon v\), \(g_\epsilon=(1+\epsilon^2|v|^2/2)^{1/2}g_0\), showing \(P=O(\epsilon^4)\) while torsion energy is \(O(\epsilon^2)\), but \(c_1(J_\epsilon)^-=0\), so it carries no exceptional harmonic twist;
- a negative Einstein Taub--Bolt--AdS \(O(-1)\) interior with \(P=0\), whose boundary first jets do not asymptotically match a CH sphere, leaving a genuine connector functional.

These models separate cheap torsion from exceptional flux, and zero-cost exceptional interiors from cheap joining.  No closed \(P=o(k)\) construction, positive tariff, or \(k^2/A\) theorem follows.


## 7. Step-64 execution record

The shell returned after the derivational work.

- `python workspace/scripts/step64_hopf_spinor_twist.py` ran with exit 0 and saved `workspace/data/step64_hopf_spinor_twist.json`. It verifies exactly
  \(|n|^2=1\), \(|dn|^2=8/r^2\), \(|n^*\omega_{S^2}|^2=16/r^4\), and the conformal Hopf-model annular coefficients \(128\pi^2\) and \(16\pi^2\).
- The old staged coordinate script `step61_EH_cokernel_norm.py` ran but failed its Ricci/duality booleans because its Euler-angle coframe did not satisfy the Maurer--Cartan conventions assumed by the metric. Its JSON is a failed run and is not evidence. The repaired moving-frame script `step61_EH_cokernel_norm_v2.py` ran with exit 0 and verified \(|\Omega|_{\rm endo}^2=4/r^8\), shell density \(\pi^2r^3\), and \(\|o_i\|_2^2=\pi^2/a^4\); see `workspace/data/step61_EH_cokernel_norm_v2.json` and the addendum to `step61_EH_quantitative_obstruction.md`.
- The two delayed research messages were sent to A01 as group messages #835 and #836; the EH execution correction was sent as #837.
- A01 message #834 supplied the missing structural Ric° Burns corrector. `theorem_package_v1.md` §19 now records that the logarithmic Burns coefficient is all-sector: both the W⁻ and Ric° corner contributions attain zero, while Theorem 59.R remains the needed P-critical remainder theorem.
