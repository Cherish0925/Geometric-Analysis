# TTCS Independent Branch Record

```json
{
  "step_id": 90,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step89_twist_bochner_and_resolvent.md",
    "Sessions/S0910A03/trace/ttcs/results/step89_ttcs01_verifier1_integration.md",
    "Sessions/S0910A03/workspace/scripts/step89_symbolic_twist_ricci.py",
    "Sessions/S0910A03/workspace/data/step89_symbolic_twist_ricci.json",
    "Sessions/S0910A03/workspace/scripts/step90_charge_potential_verify.py",
    "Sessions/S0910A03/workspace/data/step90_charge_potential_verify.json",
    "Sessions/S0910A03/workspace/scripts/step90_exchange_inequality_verify.py",
    "Sessions/S0910A03/workspace/data/step90_exchange_inequality_verify.json",
    "Sessions/S0910A03/workspace/notes/step86_forced_bochner_superlevel_and_localization.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md"
  ]
}
```

## Task

Independently verify and strengthen the Step 90 structured forced free-T^2 reduction. Read the Step 89 derivation, its verifier, and the two new symbolic outputs/scripts. Check in the established H^2 normalization whether Q=(1/2)e^{-3σ}q^T M^{-1}q satisfies Hess_H Q=Qh and |grad_H Q|^2=Q^2; whether the fixed-charge twist source is S_F=-grad_H Q; and whether <dU,D S_F>=-Qe+3<dσ,<grad Q,dU>> plus a term linear in dq. Verify the exact invariant coefficient/norm relating dq to mixed Ricci defect and the round-cusp physical law w'+3w=forcing. Then derive the strongest valid Bochner or combined-energy inequality available without treating variable Q as constant. Keep inf Q (curvature), sup/source norms, and separator average distinct. State plainly whether the +Qe base term cancels, whether any further cancellation with the area equation is available, and what remains unresolved for a complete forced-twist obstruction. Do not extrapolate beyond the free-T^2 class.

## Output

# Scientific memo: structured forced free-\(T^2\) reduction

## 1. Charge potential on \(\mathbb H^2\)

With
\[
M=
\begin{pmatrix}
e^\alpha+\beta^2e^{-\alpha}&\beta e^{-\alpha}\\
\beta e^{-\alpha}&e^{-\alpha}
\end{pmatrix},
\qquad
h=d\alpha^2+e^{-2\alpha}d\beta^2,
\]
one has
\[
M^{-1}=
\begin{pmatrix}
e^{-\alpha}&-\beta e^{-\alpha}\\
-\beta e^{-\alpha}&\beta^2e^{-\alpha}+e^\alpha
\end{pmatrix}
\]
and therefore
\[
Q=\frac12e^{-3\sigma}
\left[e^{-\alpha}(q_1-\beta q_2)^2+e^\alpha q_2^2\right].
\tag{1.1}
\]

The only nonzero Christoffel symbols of \(h\) are
\[
\Gamma^\alpha_{\beta\beta}=e^{-2\alpha},
\qquad
\Gamma^\beta_{\alpha\beta}
=\Gamma^\beta_{\beta\alpha}=-1.
\]
Direct differentiation of (1.1) gives
\[
\boxed{\operatorname{Hess}_{\mathbb H^2}Q=Qh},
\qquad
\boxed{|\nabla_{\mathbb H^2}Q|^2=Q^2}.
\tag{1.2}
\]
These are exactly the zero residuals recorded in
`step90_charge_potential_verify.json`.

At a canonical point \(M=I\), after an \(SO(2)\) rotation taking
\(q\) to \((q_0,0)\),
\[
Q=\frac12e^{-3\sigma}q_0^2e^{-\alpha},
\qquad
\nabla Q=-Q\,\partial_\alpha.
\]
Hence
\[
\boxed{S_F=-\nabla Q}.
\tag{1.3}
\]
In particular, \(S_F=Q\partial_\alpha\) at the canonical point, agreeing with the reduced equation \(L\alpha=Q\). Equivariance under the simultaneous \(SL(2,\mathbb R)\) action on \(M\) and \(q\) extends this identity to every point.

## 2. Covariant derivative of the twist source

Let
\[
u_i=dU(e_i),\qquad
e=\sum_i|u_i|^2,\qquad
\zeta_i=\langle\nabla Q,u_i\rangle,
\qquad
X=\sum_i\sigma_i\zeta_i.
\]
Because \(Q\) scales as \(e^{-3\sigma}\),
\[
D_\sigma S_F[d\sigma]=3\,d\sigma\otimes\nabla Q.
\]
Using \(\operatorname{Hess}Q=Qh\),
\[
D_US_F[u_i]=-Q\,u_i.
\]
Thus, when \(q\) varies,
\[
\boxed{
\langle dU,DS_F\rangle
=-Qe+3X+R_q,
}
\tag{2.1}
\]
where
\[
R_q:=\sum_i\left\langle
u_i,D_qS_F[\nabla_iq]\right\rangle
\tag{2.2}
\]
is linear in \(dq\). This verifies the main structured identity in the Step 90 charge-potential script.

Define the invariant normalized charge derivative
\[
|b|^2:=
e^{-3\sigma}\gamma^{ij}M^{ab}
(\nabla_iq_a)(\nabla_jq_b).
\tag{2.3}
\]
At the canonical point the symbolic output gives
\[
D_qS_F[dq]
=q_0e^{-3\sigma/2}b
\]
in orthonormal target coordinates. Since \(2Q=q_0^2e^{-3\sigma}\),
\[
\boxed{
\sum_i|D_qS_F[\nabla_iq]|^2=2Q|b|^2,
}
\qquad
\boxed{|R_q|\le\sqrt{2Qe}\,|b|.}
\tag{2.4}
\]
Again, equivariance makes this canonical-point calculation invariant.

## 3. Mixed Ricci equation and its exact coefficient

Let \(K_a\) be the fundamental vertical fields and define the mixed block
\[
\mathcal E_{ia}=E(e_i^H,K_a),\qquad E=\operatorname{Ric}_g+3g.
\]
The Maxwell equation is, up to the orientation convention for the base Hodge star,
\[
\boxed{dq_a=2\rho\,*_\gamma\mathcal E_a}.
\tag{3.1}
\]
The factor \(2\rho\) is confirmed directly by
`step89_symbolic_twist_ricci.json`: for the supplied ansatz,
\[
\partial_zq_1=2\rho\,\operatorname{Ric}(e_r,K_1).
\]

If
\[
|\mathcal E|^2
=\gamma^{ij}G^{ab}\mathcal E_{ia}\mathcal E_{jb}
\]
denotes the Hilbert–Schmidt norm of the single horizontal-to-vertical block, then \(G^{-1}=\rho^{-1}M^{-1}\) and (3.1) imply the exact identity
\[
\boxed{|b|^2=4|\mathcal E|^2.}
\tag{3.2}
\]
The full symmetric tensor norm counts both off-diagonal blocks and therefore contributes \(2|\mathcal E|^2\).

Under \(\|E\|_{\mathrm{op}}\le\delta\), the \(2\times2\) mixed block has
\[
|\mathcal E|\le\sqrt2\,\delta,
\]
so
\[
\boxed{|b|\le2\sqrt2\,\delta.}
\tag{3.3}
\]

## 4. Round-cusp physical law

For a diagonal charge orientation,
\[
w=e^{-(3\sigma+\alpha)/2}q_1,
\qquad
b_r=e^{-(3\sigma+\alpha)/2}q_1',
\]
and differentiation gives
\[
\boxed{
w'
+\left(\frac32\sigma'+\frac12\alpha'\right)w=b_r.
}
\tag{4.1}
\]
On the round expanding cusp \(\sigma=2r,\ \alpha=0\),
\[
\boxed{w'+3w=b_r.}
\tag{4.2}
\]
Thus, if \(|b_r|\le B\),
\[
|w(r)|
\le e^{-3(r-r_0)}|w(r_0)|
+\frac B3\bigl(1-e^{-3(r-r_0)}\bigr).
\tag{4.3}
\]
Sustained mixed Ricci forcing permits an \(O(B)\) physical twist amplitude; it does not by itself give decay to zero. On an exact end where \(b=0\), the decay is \(e^{-3r}\).

## 5. Exact structured Bochner identity

Write
\[
Z:=-2\widehat E_0,\qquad
T:=\operatorname{tr}_G E_{VV}.
\]
Then
\[
\tau_\sigma(U)=S_F+Z=-\nabla Q+Z,
\qquad |Z|\le2\delta,\qquad |T|\le2\delta.
\tag{5.1}
\]
If the vertical eigenvalues of \(E\) are \(\varepsilon_1,\varepsilon_2\), then
\[
T^2+|Z|^2
=2(\varepsilon_1^2+\varepsilon_2^2)\le4\delta^2.
\tag{5.2}
\]

The horizontal equation is
\[
\operatorname{Ric}^4_\sigma
=(-3+Q)\gamma_B+\frac12U^*h+E_B.
\tag{5.3}
\]
Let \(A=U^*h\), \(y=dU(\nabla\sigma)\), and
\[
\Phi(A)=\frac12\operatorname{tr}(A^2)+2\det A
       =\frac12e^2+\det A.
\]
For \(V_Z(X)=\langle dU(X),Z\rangle\), substituting (2.1) into Bochner gives the exact identity
\[
\boxed{
\begin{aligned}
\frac12Le={}&|DdU|^2+\Phi(A)-3e+E_B{:}A\\
&+\frac12|y|^2+3\langle y,\nabla Q\rangle+R_q\\
&+\operatorname{div}_\sigma V_Z
+\langle\nabla Q,Z\rangle-|Z|^2 .
\end{aligned}}
\tag{5.4}
\]

### The \(+Qe\) term does cancel

The \(+Qe\) contribution from (5.3) cancels exactly against
\[
-Qe
\]
from \(D_US_F=-Q\,dU\). Thus there is no residual \(+Qe\) reaction in the expanded structured identity.

The retained \(y\)-term yields a substantially better estimate than the one encoded in `step90_exchange_inequality_verify.py`:
\[
\frac12|y|^2+3\langle y,\nabla Q\rangle
=\frac12|y+3\nabla Q|^2-\frac92Q^2
\ge-\frac92Q^2.
\tag{5.5}
\]
Consequently,
\[
\boxed{
\begin{aligned}
\frac12Le\ge{}&
|DdU|^2+\det A+\frac12e^2-(3+\delta)e
+\operatorname{div}_\sigma V_Z\\
&-\frac92Q^2-\sqrt{2Qe}\,|b|
-2\delta Q-4\delta^2 .
\end{aligned}}
\tag{5.6}
\]
Here
\[
|V_Z|\le2\delta\sqrt e.
\tag{5.7}
\]

For any \(\eta>0\),
\[
\sqrt{2Qe}\,|b|
\le \eta e+\frac{Q|b|^2}{2\eta}
\le\eta e+\frac{4Q\delta^2}{\eta}.
\tag{5.8}
\]

### Correction to the exchange script

The script inserts
\[
|X|\le|\nabla\sigma|\sqrt{Qe}.
\]
That does not follow from the verified potential geometry. Since
\[
|\nabla Q|=Q,
\]
the direct estimate is
\[
\boxed{|X|\le|\nabla\sigma|\,Q\sqrt e.}
\tag{5.9}
\]
Accordingly, the associated scalar Young estimate contains \(Q^2/(2\eta)\), not \(Q/(2\eta)\):
\[
3X\ge-\frac92\eta|\nabla\sigma|^2e-\frac{Q^2}{2\eta}.
\tag{5.10}
\]
The zero symbolic residual in the exchange JSON verifies the Young square after the magnitude \(\sqrt{Qe}\) was inserted; it does not establish that geometric magnitude. Formula (5.5) is both valid and stronger.

## 6. Full-divergence form and a variable-\(Q\) resolvent estimate

Instead of expanding \(DS_F\), let
\[
V(X)=\langle dU(X),\tau_\sigma(U)\rangle.
\]
Then
\[
\boxed{
\frac12Le
=
|DdU|^2+\frac12|y|^2+\Phi(A)
-(3-Q)e+E_B{:}A
+\operatorname{div}_\sigma V-|\tau_\sigma(U)|^2.
}
\tag{6.1}
\]
This is equivalent to (5.4), but it retains \(+Qe\) at the price of putting the twist source into the divergence field.

Set the three distinct quantities
\[
Q_-:=\inf_BQ,\qquad
Q_+:=\sup_BQ,\qquad
Q_C:=\langle Q\rangle_C
\tag{6.2}
\]
for a separator \(C\). Define
\[
K:=3-Q_-+\delta,\qquad f:=Q_++2\delta.
\tag{6.3}
\]
Then
\[
\boxed{
\frac12Le\ge
\frac12e^2-Ke+\operatorname{div}_\sigma V-f^2,
\qquad |V|\le f\sqrt e.
}
\tag{6.4}
\]
No spatially varying resolvent mass has been introduced.

Under the same complete weighted-base Green-kernel assumptions used in Step 87, with \(K>0\) and vanishing end flux, take \(\kappa=2K\). The resolvent calculation gives
\[
\boxed{
\sup_Be\le
\left[
\frac{2f}{\sqrt K}
+\sqrt{2K+\frac{5f^2}{K}}
\right]^2.
}
\tag{6.5}
\]
This is the proper variable-\(Q\) replacement for Step 89 equation (4.3). If \(Q\) is spatially constant, it reduces to that formula. Constancy of the charge vector \(q\) does not imply constancy of \(Q\), because
\[
Q=\frac12\rho^{-3}q^TM^{-1}q.
\]
Thus the number \(0.8986\ldots\) belongs only to the additional spatially constant-\(Q\) specialization.

For exact OT open ends, \(Q=0\) there and hence
\[
Q_-=0,\qquad K=3+\delta.
\]
In that geometry twist gives no improvement in the uniform curvature parameter; its contribution instead enters through \(Q_+\) and through the separator average.

## 7. Area equation and combined energy

The vertical trace equation is
\[
\boxed{L\sigma=6+Q-T.}
\tag{7.1}
\]
Put
\[
x=|\nabla\sigma|^2,\qquad W=e+cx,\quad c>0.
\]
Weighted scalar Bochner gives the exact divergence form
\[
\begin{aligned}
\frac12Lx={}&|\operatorname{Hess}\sigma|^2
+(-3+Q)x+\frac12x^2+\frac12|y|^2
+E_B(\nabla\sigma,\nabla\sigma)\\
&+\operatorname{div}_\sigma((Q-T)\nabla\sigma)
-(Q-T)(6+Q-T).
\end{aligned}
\tag{7.2}
\]
Combining this with the full-divergence map identity yields
\[
\boxed{
\begin{aligned}
\frac12LW={}&|DdU|^2+c|\operatorname{Hess}\sigma|^2
+\Phi(A)+\frac c2x^2+\frac{1+c}{2}|y|^2\\
&+(-3+Q)W
+E_B{:}A+cE_B(\nabla\sigma,\nabla\sigma)\\
&+\operatorname{div}_\sigma\!\left[V+c(Q-T)\nabla\sigma\right]\\
&-|\tau_\sigma(U)|^2-c(Q-T)(6+Q-T).
\end{aligned}}
\tag{7.3}
\]
Since
\[
\frac12e^2+\frac c2x^2\ge\frac{W^2}{2(1+c)},
\]
equation (7.3) implies
\[
\boxed{
\frac12LW\ge
\frac{W^2}{2(1+c)}-KW
+\operatorname{div}_\sigma\mathcal J_c
-f^2-cf(6+f),
}
\tag{7.4}
\]
where
\[
\mathcal J_c=V+c(Q-T)\nabla\sigma,
\qquad
|\mathcal J_c|\le f\sqrt{1+c}\,\sqrt W.
\tag{7.5}
\]

There is no second reaction cancellation analogous to the \(+Qe-Qe\) cancellation. If (7.2) is instead expanded using
\[
dQ=\langle\nabla Q,dU\rangle-3Q\,d\sigma+D_qQ[dq],
\]
its exchange contribution is \(+X\); adding \(cLx/2\) changes the coefficient in (5.4) from \(3X\) to \((3+c)X\), rather than removing it. Formula (7.2) transfers that exchange into the flux \((Q-T)\nabla\sigma\).

For fixed \(q\), a formal combination involving \(LQ\) can remove the \(X\)-term. When \(dq\neq0\), expanding \(LQ\) introduces second derivatives of \(q\), while the mixed Ricci estimate (3.1) controls only \(dq\). The supplied assumptions therefore do not support that extra cancellation in the forced case.

## 8. Separator coefficient and the three \(Q\)-quantities

For an invariant minimal separator,
\[
\mathrm{II}(T,K_a)=\frac12G_{ab}f^b
\]
up to orientation. With a vertical orthonormal index counted once,
\[
\sum_A|\mathrm{II}(T,E_A)|^2
=\frac14G_{ab}f^af^b=\frac Q2.
\]
The full tensor norm counts both symmetric mixed entries, so its mixed contribution is \(Q\):
\[
|\mathrm{II}|^2\ge Q.
\tag{8.1}
\]
Thus
\[
\boxed{
\langle e_s\rangle_C
\ge12+2Q_C-8\delta.
}
\tag{8.2}
\]
Step 89 equation (7.1) has a factor-of-two notational mismatch if its sum is read as a single vertical sum; the resulting floor (7.2) is nevertheless correct.

Combining (6.5) and (8.2), every connector satisfying the global resolvent assumptions must obey
\[
12+2Q_C-8\delta
\le
\left[
\frac{2(Q_++2\delta)}{\sqrt{3-Q_-+\delta}}
+\sqrt{
2(3-Q_-+\delta)
+\frac{5(Q_++2\delta)^2}{3-Q_-+\delta}}
\right]^2.
\tag{8.3}
\]
The curvature uses \(Q_-\), the source uses \(Q_+\), and the geometric floor uses \(Q_C\). Replacing these by one symbol is not justified.

## 9. Mathematical substance still unresolved

For a complete forced-twist obstruction in the free-\(T^2\) class, the missing input is a dimension-only relation controlling \(Q_+\) and \(Q_C\) from \(\delta\) and the prescribed ends.

The mixed equation supplies only
\[
|b|\le2\sqrt2\,\delta.
\]
The round-cusp law controls physical twist along an exact radial cusp, but a long or geometrically complicated compact core can accumulate charge variation. Neither (3.3) nor the area equation presently gives a universal upper estimate for \(Q_+\). The structured formula (5.6) replaces the large twist flux by terms involving \(Q^2\), but it still requires control of \(Q\). The full-divergence formula (6.4) requires \(Q_+\) directly.

For exact Einstein metrics, \(dq=0\); an exact OT open end has \(q=0\), hence \(q\equiv0\) on the connected free region. For forced metrics, \(dq\) is small rather than zero, and this propagation argument no longer removes twist.

All formulas above concern free \(T^2\)-invariant metrics only. They do not provide an implication for general four-dimensional metrics without that symmetry.