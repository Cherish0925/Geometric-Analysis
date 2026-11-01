# Step 55 — Darboux-gauge Ricci compatibility for negative-scalar Goldberg

Session S1003A01, Agent3. This note replaces the Step-54 interpretation that a negative formal-dimension count by degree 15 by itself predicts a new Goldberg obstruction. It records a universal Ricci-symbol relation, derives its geometric form, and places it inside the existing almost-Kähler identities.

## 1. Set-up and the symbol relation

Work at a point of an almost-Kähler four-manifold in Darboux coordinates, so the symplectic form is fixed and the compatible metric varies through symmetric tensors satisfying
\[
hJ+Jh=0.
\]
In particular, \(\operatorname{tr}h=0\). For a real covector \(\xi\), the flat Ricci symbol is, up to the common sign convention,
\[
\sigma_{\mathrm{Ric}}(\xi)h
=\frac12\{\xi\otimes h\xi+h\xi\otimes\xi-|\xi|^2h\}.
\]
Since \(h(J\xi,J\xi)=-h(\xi,\xi)\), direct contraction gives
\[
\boxed{
(\sigma_{\mathrm{Ric}}(\xi)h)(J\xi,J\xi)
-\frac12|\xi|^2\operatorname{tr}(\sigma_{\mathrm{Ric}}(\xi)h)=0.}
\tag{1.1}
\]
This is independent of the contracted-Bianchi symbol. Its polynomial prolongations contribute \(n_{N-4}\) relations at Taylor degree \(N\), which changes the Step-54 free count to
\[
f_{\mathrm{corr}}(N)=N^2+8N-5\qquad(N\ge4).
\]
Hence the earlier negative count at \(N=15\) is explained by an omitted universal symbol relation. It gave no evidence of a negative-scalar-specific condition and no finite bound for nonlinear completion.

## 2. Coordinate-free fourth-order operator

For a symmetric two-tensor \(S\), define the fourth-order principal contraction
\[
\mathcal C_J(S)
:=J_i{}^aJ_j{}^b\nabla^i\nabla^jS_{ab}
-\frac12L(\operatorname{tr}S),
\qquad L:=\nabla^i\nabla_i.
\tag{2.1}
\]
Freezing \(J\) and replacing \(\nabla\) by \(\xi\), its symbol is exactly the scalar in (1.1). In AAD's nonnegative convention \(\Delta=-L\), the second term is \(+\frac12\Delta\operatorname{tr}S\). Thus for a compatible metric the fourth derivatives cancel in \(\mathcal C_J(\operatorname{Ric})\); what remains is a lower-jet relation involving derivatives of \(J\), curvature, and the lower-order nonlinearities of Ricci.

The first term has a useful exact divergence expansion. Put
\[
D^a:=J_i{}^a\nabla^i=-J^a{}_i\nabla^i,
\qquad \nabla^iJ_i{}^a=0,
\tag{2.2}
\]
where the last equality is the almost-Kähler identity \(\delta\omega=0\). Then
\[
\begin{aligned}
J_i{}^aJ_j{}^b\nabla^i\nabla^jS_{ab}
={}&\nabla^i\!\left(J_i{}^aJ_j{}^b\nabla^jS_{ab}\right)
-J_i{}^a(\nabla^iJ_j{}^b)\nabla^jS_{ab} \\
={}&\nabla^i\!\left(J_i{}^aJ_j{}^b\nabla^jS_{ab}\right)
-\langle\nabla J,\nabla S\rangle_{J},
\end{aligned}
\tag{2.3}
\]
with the displayed contraction defining the final shorthand. Therefore on a closed manifold
\[
\int_M J_i{}^aJ_j{}^b\nabla^i\nabla^jS_{ab}\,d\mu
=-\int_M J_i{}^a(\nabla^iJ_j{}^b)\nabla^jS_{ab}\,d\mu.
\tag{2.4}
\]
For an Einstein tensor \(S=\operatorname{Ric}=\lambda g\), both sides vanish identically because \(\nabla S=0\) and \(\operatorname{tr}S=4\lambda\) is constant. Consequently the unreduced contraction (2.1), evaluated only after imposing Einstein, is a differential consequence of \(\nabla\operatorname{Ric}=0\) and by itself cannot distinguish \(\lambda<0\) from the Kähler-Einstein and Ricci-flat Tod controls. This does **not** prove that the lower-order equation obtained after eliminating fourth derivatives is redundant among a truncated lower-jet system; such a resolved differential consequence can still be an integrability relation and may contain sign-sensitive terms.

This does not make the Darboux symbol relation useless. It identifies a real Spencer compatibility that must be included before any symbol count, and it shows exactly where information can enter after the Einstein equation: through the *resolved lower-order expression* for the same identity in the variables \(J,\nabla J\), not through a bare Ricci projection. Such a resolved expression is one component of the Ricci identities for \(\nabla\omega\) and the differential Bianchi identities.

## 3. Identification inside the AAD curvature system

Apostolov–Armstrong–Drăghici use
\[
\nabla\Omega=a\otimes\phi-Ja\otimes J\phi,
\qquad |\nabla\Omega|^2=4|a|^2,
\tag{3.1}
\]
and derive the Ricci identities
\[
da-Ja\wedge b=-R(J\phi),\qquad
d(Ja)+a\wedge b=-R(\phi),
\tag{3.2}
\]
together with
\[
db=a\wedge Ja-R(\Omega).
\tag{3.3}
\]
These equations determine the self-dual curvature and Ricci tensor from the lower jets of \(J\). Their differentiated system is the intrinsic form of the Darboux-gauge compatibility mechanism.

For a general almost-Kähler metric their differential Bianchi equation is (AAD Lemma 4, equation (33))
\[
\begin{aligned}
0={}&-\tfrac14(d^J(\kappa-s))_Z\Omega
+\tfrac16(d(\kappa-s)\wedge Z^\flat)^+
+(\delta\rho_*'')_Z\Omega \\
&+\tfrac\kappa4\nabla_{JZ}\Omega
-\nabla_{\rho_0(Z)}\Omega
+\nabla_{\rho_*''(Z)}\Omega
+\nabla_{JZ}\rho_*''
+2(\delta W_3^+)_Z+A_Z^+.
\end{aligned}
\tag{3.4}
\]
On an Einstein almost-Kähler metric, \(s\) is constant, \(\rho_0=0\), \(A=0\), while
\[
\kappa-s=\frac32q,
\qquad q=|\nabla\Omega|^2,
\qquad \rho_*''\equiv\eta .
\tag{3.5}
\]
Thus the surviving equation is
\[
\boxed{
0=-\frac38(d^Jq)_Z\Omega
+\frac14(dq\wedge Z^\flat)^+
+(\delta\eta)_Z\Omega
+\frac\kappa4\nabla_{JZ}\Omega
+\nabla_{\eta(Z)}\Omega
+\nabla_{JZ}\eta
+2(\delta W_3^+)_Z .}
\tag{3.6}
\]
This is the substantive lower-jet compatibility absent from the scalar symbol projection. It retains the transverse canonical curvature \(\eta\), the derivative of \(W_3^+\), and their coupling to torsion. It is not a Yang–Mills equation for the canonical connection and does not permit treating \(\eta\) as freely prescribed forcing.

AAD's general Weitzenböck formula (their equation (47)) specializes under Einstein to
\[
\begin{aligned}
(\nabla^*\nabla(\nabla\Omega))_X={}&-\frac{3s}{4}\nabla_X\Omega
+\left[\frac13d(\kappa-s)_X
-2\langle(\delta W_3^+)_{JX},\Omega\rangle\right]\Omega \\
&+2(\nabla_X\eta)''+2\nabla_{J\eta(X)}\Omega,
\end{aligned}
\tag{3.7}
\]
where the other terms vanish because \(\operatorname{Ric}_0=0\) and \(A=0\). Using (3.5),
\[
\boxed{
(\nabla^*\nabla(\nabla\Omega))_X
+\frac{3s}{4}\nabla_X\Omega
=\left[\frac12dq_X
-2\langle(\delta W_3^+)_{JX},\Omega\rangle\right]\Omega
+2(\nabla_X\eta)''+2\nabla_{J\eta(X)}\Omega .}
\tag{3.8}
\]
The sign \(3s/4<0\) explains why a naive integration does not force torsion to vanish, but it is not evidence for local freedom. Equations (3.6) and (3.8) constrain \(dq,\nabla\eta,\delta W_3^+\), and \(\nabla\Omega\) together. The \(\Omega\)-component of (3.6) removes the explicit \(dq\) and \(\delta W_3^+\) forcing in (3.8):
\[
\frac12dq_X-2\langle(\delta W_3^+)_{JX},\Omega\rangle
=2(\delta\eta)_{JX}+\langle\eta,\nabla_X\Omega\rangle,
\tag{3.9}
\]
so the Helmholtz equation can be written with \(\eta,\nabla\eta\) as its only explicit sources. For Einstein metrics, the third Gray condition is \(\eta=0\) alone; \(W_3^+=0\) is not additionally required. Then AAD's closed Helmholtz equation follows, and their local classification—not the rough-Laplacian equation alone—forces any strict solution in this branch into the Ricci-flat NPT/Tod class. Hence it supplies no strictly almost-Kähler negative-Einstein germ.

## 4. Consequences for the jet computation

1. The original all-at-once degree-5 computations are usable only as existence of independently optimized truncated jets. They do **not** form compatible formal germs. The preserved D5 runs have residual squares between \(1.1\times10^{-27}\) and \(5.7\times10^{-27}\); the full Jacobian ranks are 1035 for KE and 1036 for RF/NEG. As at degree 4, the KE one-row difference is expected from the singular linearization of the imposed scalar condition \(q(0)=0\). Moreover the D5 `KE` jets are not the exact Kähler-Einstein control: their computed \(q\) is numerical zero, but their reported \(|\eta|=0.156,0.298\) and generic \(W^+\) show that imposing only the pointwise scalar equation \(q(0)=0\) does not impose a Kähler germ. Only the explicit exact \(H^2\times H^2\) jet is a KE control.
2. D6/D7 empty or incomplete outputs resulted from resource termination and carry no mathematical content.
3. The first fixed-lower-jet test (files `data/step54_prolong/prolong_D4_*_z0_to_D5.json`) produced nonzero projection norms for every branch: \(1.567\) for the mislabeled `KE` D4 jet, \(0.669\) for a generic RF jet, and \(0.741\) for a NEG jet, with exact affine-linearity errors \(4.4\)--\(5.8\times10^{-14}\). Because even the controls fail and the source jets were independently optimized truncations rather than exact extendible germs, these numbers are **not** obstructions. They demonstrate that the present least-squares jets do not lie on a degree-five extendible branch and that sector-by-sector residual norms are basis-dependent (the total cokernel vector mixes E1/E2/E3 rows). The fixed-lower-jet method becomes meaningful only with an exact KE and exact Tod source and with its cokernel quotiented by (1.1), contracted Bianchi, closure, and algebraic compatibility identities.
4. A projection along (1.1) should vanish as a consequence of (3.2)–(3.4); it is a control on the implementation, not a negative-scalar obstruction.
5. The next local computation should use an intrinsic first-order prolongation of (3.2)–(3.3), (3.6), and (3.8), or Darboux variables with the universal identities explicitly removed. It should seek a residual relation not generated by these equations and compare an exact KE germ and an exact Tod germ against negative jets at several \(q/|\lambda|\). Re-running the unconstrained degree ladder is not justified.

## 5. Global implication

The local scalar candidate has collapsed to a known compatibility identity rather than an integrability theorem. Therefore the highest-value Goldberg route is the coupled canonical-connection system:
\[
\eta=-\tfrac12\operatorname{div}^1(A),
\quad\text{AAD (3.6),}
\quad\text{AAD (3.8),}
\quad
\beta=iF_{\mathcal A}-\tfrac s4\omega,
\quad
\int q^2/16\ge8\pi^2\|c_1^{-,h}\|^2.
\]
A successful rigidity proof must obtain a global coercive relation that controls the transverse terms in (3.6)–(3.8), possibly from the actual canonical/Seiberg–Witten field, rather than discarding them. Conversely, a local counterexample construction must solve this coupled system with \(\eta\ne0\) for \(s<0\), not merely the scalar Ricci compatibility.

## 6. Evidence status

- Equations (1.1), (2.3), (3.6), and (3.8) are direct algebraic/specialization derivations from the displayed definitions and the cited AAD equations.
- The identification of the entire nonlinear Darboux remainder with the AAD system is structural; a component-by-component coordinate expansion has not been performed.
- No negative-scalar strictly almost-Kähler Einstein germ, compact example, or integrability proof is obtained here.

## 7. Global identities extracted from the coupled equations

An independent coefficient check (`trace/ttcs/results/step55_ttcs01_verifier1_integration.md`) confirms (3.6), (3.8), the identification \(\eta=\rho_*''=W^+(\Omega)_{\Omega^\perp}\), and the form of (3.9). Pairing (3.8) with \(T=\nabla\Omega\) and integrating gives
\[
\boxed{
\int_M|\nabla^2\Omega|^2+\frac{3s}{4}\int_Mq
=4\int_M|\eta|^2.}
\tag{7.1}
\]
The \(\Omega\)-valued forcing is orthogonal to \(T\), and the \(J\eta\)-directional term contracts a skew tensor with the symmetric tensor \(\langle T_X,T_Y\rangle\), hence vanishes. AAD's identity
\[
\nabla^*\nabla\Omega=2\eta+\frac q2\Omega
\]
then supplies the right-hand side. For \(s<0\), (7.1) reads
\[
\int|\nabla^2\Omega|^2=\frac{3|s|}{4}\int q+4\int|\eta|^2,
\tag{7.2}
\]
so the Helmholtz equation measures, but does not suppress, torsion.

The canonical closed form \(\beta=iF_{\mathcal A}-(s/4)\Omega\) satisfies \(\beta\wedge\beta=|\eta|^2d\mu\), so (7.1) also gives the topological identity
\[
\boxed{
\int|\nabla^2\Omega|^2+\frac{3s}{4}\int q
=4[\beta]^2,
\qquad [\beta]=2\pi c_1-\frac{s}{4}[\Omega].}
\tag{7.3}
\]
This connects the full second derivative of the almost-Kähler field to the same canonical class appearing in the Hodge inequality; it remains non-coercive in the negative-scalar regime.

The transverse Bianchi component provides the additional exact equation
\[
0=\frac14(dq\wedge Z^\flat)''+\frac\kappa4T_{JZ}
+2(\delta W_3^+)_Z''+\nabla_{\eta(Z)}\Omega+(\nabla_{JZ}\eta)'',
\tag{7.4}
\]
which is the correct place to seek coercivity. It retains the derivative of \(W_3^+\), rather than replacing it by a scalar norm. In particular, pairing (7.4) with \(T_{JZ}\), integrating, and using the established almost-Kähler balance yields
\[
\boxed{
\int_M\sum_i\langle(\delta W_3^+)_{e_i},T_{Je_i}\rangle
=2\int_M|W_3^+|^2.}
\tag{7.5}
\]
Thus the transverse Weyl component has a signed global cross-pairing with the Nijenhuis derivative. The missing step for Goldberg is a canonical-connection estimate controlling the left side of (7.5), together with the \(\eta\) terms in (7.4), strongly enough to contradict the negative-scalar balance unless \(T=0\). A pointwise or \(L^2\) bound that discards these coupled derivatives will reproduce the already non-coercive identities.
