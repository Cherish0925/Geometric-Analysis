# Step 90: structured forced twist, exact cancellation, and a radial discharge mechanism

Session `S0910A03`, Agent3 / Execute.

> **Corrects Step 89 §§2–8 wherever a spatially variable twist energy was treated as a constant.**
> The constant-
> \(Q\) arithmetic remains an algebraic specialization, but it is not a theorem for
> the forced connector. The forced free-\(T^2\) class remains open.
>
> **Partially superseded by Step 91:** The proposed radial cylindrical throat
> program (§8) is blocked by the flat-slice barrier: each r-level is a flat T³,
> so H² ≥ 9 − 6δ, requiring δ ≥ 3/2 for cylindrical interpolation. The
> separator stability inequality (Step 91 §3) gives Q_C ≤ 3 + δ. The resolvent-
> floor combination does NOT constrain Q_C beyond stability. Step 92 strengthens
> the full invariant stability form: after scalar conjugation and tangential
> Maxwell transport it gives a finite separator bound sup_C Q <= C_Q(delta),
> but not an interior Q_+ bound; normal orbit energy remains the tubular-collar
> obstruction. The toral BH coordinate equivalence shows the radial Q-redshift
> reflects rotated torus identification. Sections 1–7 (structured potential,
> cancellation, canonical energy, Maxwell transport, radial core, forced
> discharge) retain their verified structural content.

## 1. Reduction and normalization

For
\[
 g=\gamma_B+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\qquad
 G=e^\sigma M,\quad \det M=1,
\]
put \(\rho=e^\sigma\), \(F^a=dA^a=f^a\operatorname{vol}_{\gamma_B}\), and
\[
 q_a=\rho G_{ab}f^b,\qquad
 Q=\frac12G_{ab}f^af^b
   =\frac12e^{-3\sigma}q^TM^{-1}q.
\]
The weighted base operator is \(L=\Delta+\nabla\sigma\cdot\nabla\), and
\(U:B\to\mathbb H^2\) denotes the orbit-shape map. For
\(E=\operatorname{Ric}_g+3g\), write
\[
 T=\operatorname{tr}_{\rm orb}E,\qquad
 Z=-2\widehat E_0,
\]
where \(\widehat E_0\) is the traceless vertical block. The reduced system is
\[
 L\sigma=6+Q-T,
\tag{1.1}
\]
\[
 \tau_\sigma(U)=-\nabla_{\mathbb H^2}Q+Z,
\tag{1.2}
\]
\[
 \operatorname{Ric}_B-\operatorname{Hess}\sigma-\frac12d\sigma^2
 =(-3+Q)\gamma_B+\frac12U^*h_{\mathbb H^2}+E_B.
\tag{1.3}
\]
The direct base twist Ricci is \(-Q\gamma_B\), but solving (1.3) puts
\(+Q\gamma_B\) in the drift curvature. That sign observation alone does **not**
make twist favorable, because (1.2) contributes an exactly cancelling term.

The mixed Ricci formula in Liu's normalization translates to
\[
 dq_a=\pm2\rho\,*_\gamma E(\cdot,K_a).
\tag{1.4}
\]
With
\[
 |b|^2=e^{-3\sigma}\gamma^{ij}M^{ab}(\nabla_iq_a)(\nabla_jq_b),
\]
one gets
\[
 |b|^2=4|E_{\rm mix}|_{\rm HS}^2,
 \qquad |b|\le2\sqrt2\,\delta
 \quad\text{if }\|E\|_{\rm op}\le\delta.
\tag{1.5}
\]
This coefficient agrees with the explicit Step 89 mixed Ricci component and with
Liu's source formula \cite{liutoric}.

## 2. The charge is a horospherical target potential

In Iwasawa coordinates
\[
 M=\begin{pmatrix}
 e^\alpha+\beta^2e^{-\alpha}&\beta e^{-\alpha}\\
 \beta e^{-\alpha}&e^{-\alpha}
 \end{pmatrix},\qquad
 h_{\mathbb H^2}=d\alpha^2+e^{-2\alpha}d\beta^2,
\]
\[
 Q=\frac12e^{-3\sigma}
 \left[e^{-\alpha}(q_1-\beta q_2)^2+e^\alpha q_2^2\right].
\]
Direct symbolic differentiation gives
\[
 \boxed{\operatorname{Hess}_{\mathbb H^2}Q=Qh_{\mathbb H^2}},
 \qquad
 \boxed{|\nabla_{\mathbb H^2}Q|^2=Q^2}.
\tag{2.1}
\]
At \(M=I,q=(q_0,0)\), \(-\nabla Q=Q\partial_\alpha\), agreeing with the
verified diagonal equation \(L\alpha=Q\). Equivariance gives
\[
 \boxed{S_F=-\nabla_{\mathbb H^2}Q}
\tag{2.2}
\]
for general \(M,q\).

Let \(u_i=dU(e_i)\), \(e=|dU|^2\), and
\[
 X=\sum_i\sigma_i\langle\nabla Q,u_i\rangle.
\]
Allowing \(q\) to vary,
\[
 \boxed{
 \langle dU,DS_F\rangle=-Qe+3X+R_q,
 }
\tag{2.3}
\]
where \(R_q\) is linear in \(dq\). In invariant norm,
\[
 \sum_i|D_qS_F[\nabla_iq]|^2=2Q|b|^2,
 \qquad |R_q|\le\sqrt{2Qe}\,|b|.
\tag{2.4}
\]
The sharp exchange size is
\[
 |X|\le |\nabla\sigma|\,Q\sqrt e,
\tag{2.5}
\]
not \(|\nabla\sigma|\sqrt{Qe}\). An initial version of
`step90_exchange_inequality_verify.py` inserted the latter magnitude; after TTCS
caught it, the script and JSON were repaired to give the correct \(Q^2/(2\eta)\)
Young remainder.

Reproducible calculation:
`workspace/scripts/step90_charge_potential_verify.py` and
`workspace/data/step90_charge_potential_verify.json`.

## 3. Exact cancellation in the orbit-energy Bochner equation

Let \(A=U^*h\), \(y=dU(\nabla\sigma)\), and
\(V_Z(X)=\langle dU(X),Z\rangle\). The weighted Bochner identity becomes
\[
\begin{aligned}
 \frac12Le={}&|DdU|^2+\frac12\operatorname{tr}(A^2)+2\det A-3e
 +E_B{:}A\\
 &+\frac12|y|^2+3\langle y,\nabla Q\rangle+R_q
 +\operatorname{div}_\sigma V_Z
 +\langle\nabla Q,Z\rangle-|Z|^2.
\end{aligned}
\tag{3.1}
\]
The \(+Qe\) from the drift curvature cancels pointwise with \(-Qe\) from
\(DS_F\), even when \(Q\) varies. Hence Step 89's net favorable
\(e-6+2Q\) interpretation is only an alternative full-divergence bookkeeping;
it does not leave a positive \(Qe\) term once the charge potential is expanded.

Completing the square,
\[
 \frac12|y|^2+3\langle y,\nabla Q\rangle
 =\frac12|y+3\nabla Q|^2-\frac92Q^2.
\tag{3.2}
\]
Thus a valid lower bound is
\[
\begin{aligned}
 \frac12Le\ge{}&|DdU|^2+\det A+\frac12e^2-(3+\delta)e
 +\operatorname{div}_\sigma V_Z\\
 &-\frac92Q^2-\sqrt{2Qe}|b|-2\delta Q-4\delta^2.
\end{aligned}
\tag{3.3}
\]
It is structured, but it does not control a large twist core.

The equivalent full-divergence form requires three distinct numbers:
\[
 Q_-:=\inf_BQ,\qquad Q_+:=\sup_BQ,\qquad
 Q_C:=\frac{\int_CQ\rho\,ds}{\int_C\rho\,ds}.
\]
The curvature bound uses \(Q_-\), source size uses \(Q_+\), and the minimal
separator floor uses \(Q_C\). With exact OT open ends, \(Q_-=0\), so the global
curvature parameter remains \(3+\delta\). No one of these can be replaced by a
single `Q_max`, and no spatially varying mass can be inserted into the Step 87
Fisher/Beta computation without a new variable-potential theorem.

In particular, the valid coarse necessary comparison is
\[
12+2Q_C-8\delta\le
\left[
 \frac{2(Q_++2\delta)}{\sqrt{3-Q_-+\delta}}
 +\sqrt{2(3-Q_-+\delta)+
 \frac{5(Q_++2\delta)^2}{3-Q_-+\delta}}
\right]^2,
\tag{3.4}
\]
not the Step 89 one-parameter curve. The number \(0.8986\ldots\) belongs only to
the extra specialization \(Q(x)\equiv q\).

## 4. Coupling to area: the canonical energy

Keeping second derivatives of \(q\) inside a weighted divergence gives an exact
structured identity for
\[
 \boxed{W=e+2Q+3|\nabla\sigma|^2.}
\tag{4.1}
\]
The coefficients are forced: they simultaneously cancel the area-shape exchange,
the term \(R_q\), and the corresponding \(dq\)-area term. One obtains
\[
\begin{aligned}
 \frac12LW={}&\operatorname{div}_\sigma\mathcal J
 +|DdU|^2+3|\operatorname{Hess}\sigma|^2
 +2|dU(\nabla\sigma)|^2+\Phi(A)\\
 &+\frac32|\nabla\sigma|^4+3Q|\nabla\sigma|^2+Qe
 -3e-9|\nabla\sigma|^2-18Q-4Q^2\\
 &+E_B{:}A+3E_B(\nabla\sigma,\nabla\sigma)
 +2\langle\nabla Q,Z\rangle-|Z|^2\\
 &+18T+6QT-3T^2,
\end{aligned}
\tag{4.2}
\]
with
\[
 \mathcal J=V_Z+Z_Q-3T\nabla\sigma,
 \qquad |\mathcal J|\le
 (2+2\sqrt2+2\sqrt3)\delta\sqrt W.
\tag{4.3}
\]
At a common critical point with \(e=|\nabla\sigma|=0\), \(Q=Q_0\), and exact
second jets, the nonflux right side is \(54-2Q_0^2\). Therefore no universal
positive-quadratic reaction in \(W\) follows from \((e,Q,|\nabla\sigma|^2)\)
alone. The canonical energy organizes the equations but does not yet obstruct
large \(Q\).

The derivation and two independent readings are in
`trace/ttcs/results/step90_ttcs01_generator1_integration.md` and
`step90_ttcs01_verifier1_integration.md`. One generator branch proposed an average
\(Q=O(\delta^2)\) closure, but that argument first assumes an \(e\)-ceiling that is
precisely unavailable here and does not turn a global average into the kernel-
weighted control required by a resolvent. It is retained only as a conditional
integral identity, not as closure.

## 5. Physical Maxwell transport

Let
\[
 w=\sqrt{2Q}=e^{-3\sigma/2}|M^{-1/2}q|.
\]
Invariantly,
\[
 \left|dw+\frac32w\,d\sigma\right|
 \le\frac12w|dU|+|b|.
\tag{5.1}
\]
For diagonal \(M=\operatorname{diag}(e^\alpha,e^{-\alpha})\),
\(q=(q(r),0)\),
\[
 \boxed{w'+\frac12(3\sigma'+\alpha')w=b},
 \qquad b=e^{-(3\sigma+\alpha)/2}q'.
\tag{5.2}
\]
On the round expanding cusp, \(\sigma'=2,\alpha'=0\), so
\[
 w'+3w=b.
\tag{5.3}
\]
Thus coordinate charge can change at order \(\delta e^{3r}\), while physical
forcing remains \(O(\delta)\). Sustained forcing permits \(w=O(\delta)\); it does
not force extra decay. Exact Einstein conservation kills twist from an exact OT
open end, but this propagation fails for an approximately Einstein interior.

## 6. An exact charged radial core

To test whether the missing \(Q_+\) estimate is plausible, use a polar base and a
diagonal charge:
\[
 \gamma=dr^2+\psi(r)^2d\theta^2,
 \quad M=\operatorname{diag}(e^\alpha,e^{-\alpha}),
 \quad q=(q_0,0).
\]
Set
\[
 u=\sigma',\quad v=\alpha',\quad H=\psi'/\psi,
 \quad Q=\tfrac12q_0^2e^{-3\sigma-\alpha},
 \quad K=-\psi''/\psi.
\]
The exact reduced Einstein system is
\[
 u'=6+Q-u^2-Hu,
\quad v'=Q-Hv-uv,
\tag{6.1}
\]
\[
 K=-3+Q+Hu,
\quad H'=-K-H^2.
\tag{6.2}
\]
Smooth-center jets are
\[
 u=\frac{6+Q_0}{2}r+O(r^3),\qquad
 v=\frac{Q_0}{2}r+O(r^3),
\]
\[
 H=r^{-1}-\frac{Q_0}{2}r+O(r^3),\qquad
 K(0)=\frac32Q_0.
\tag{6.3}
\]
The unused horizontal \(rr\) equation was monitored independently. Writing its
residual as \(C=E_{rr}\), direct differentiation gives the exact propagation law
\[
 C'=-2(u+H)C
\tag{6.4a}
\]
in the constant-charge core. Thus a regular center with \(C(0)=0\) satisfies the
full horizontal system; the observed relative residual below
\(1.8\times10^{-9}\) comes from truncating the center series at leading order,
not an accidental cancellation.

For \(Q_0=0.1,1,3,10,30,100\), every integration reached \(r=4\) and numerically approached
\[
 u\to2,\qquad v\to0,\qquad H\to1,\qquad K\to-1,\qquad Q\to0.
\tag{6.4}
\]
Even \(Q_0=100\) fell below \(10^{-2}\) by \(r=0.982\) and below
\(10^{-4}\) by \(r=1.720\). Thus the exact local regular family permits every
finite \(Q_0\), and the sampled solutions through \(Q_0=100\) rapidly redshift to
an almost-OT expanding end. This does
not contradict exact charge conservation: coordinate \(q_0\) remains nonzero,
while physical \(Q\) decays.

Files:
`workspace/scripts/step90_radial_twist_core.py` and
`workspace/data/step90_radial_twist_core.json`.

## 7. Forced discharge into an exact OT end

Starting from the exact core at the first radius where \(w=\delta\), prescribe
\[
 b(s)=-A\sin^2(\pi s/L),\qquad 0\le s\le L,
\tag{7.1}
\]
and choose \(A\) by a nonlinear scalar shooting solve so that \(w(L)=0\). During the taper, equations
(6.1) and the \(\theta\theta\) horizontal equation were imposed exactly
(so \(T=0\), \(Z=0\), and that horizontal component vanishes), while the remaining
\(rr\) defect was measured.

For \(Q_0=1,10,100\), \(\delta=0.1,0.03,0.01\), and
\(L=0.5,1,2\), all 27 shots reached \(w(L)=0\). The main scaling is
\[
 \max|b|=C(L)\delta,
\tag{7.2}
\]
with ranges across \(Q_0,\delta\)
\[
\begin{array}{c|ccc}
 L&0.5&1&2\\ \hline
 C(L)&1.752\text{--}1.850&0.365\text{--}0.395&0.0266\text{--}0.0293.
\end{array}
\]
The round-cusp linear predictions are \(1.8215,0.3860,0.02851\), respectively.
The remaining horizontal \(rr\) residual obeys the exact forced constraint law
\[
 C'=-2(u+H)C-wb,
\tag{7.3a}
\]
so \(w,b=O(\delta)\) explain its observed \(O(\delta^2)\) scaling:
\[
 \max|E_{rr}|/\delta^2\in
 [0.0665,0.0729],\ [0.0114,0.0131],\
 [4.12,4.90]\times10^{-4}
\tag{7.3}
\]
for \(L=0.5,1,2\).

In this rank-one radial reduction the mixed orthonormal Ricci component is
\(|b|/2\), and the only other nonzero reduced block is \(C\). Hence
\[
 \|E\|_{\rm op}=\max\{|C|,|b|/2\};
\]
all 27 sampled collars have \(\|E\|_{\rm op}<0.925\delta\).

This is not a completed two-ended connector or a counterexample to Yau 26: the
base disk has polar topology rather than the free cylindrical topology of the
minimal-separator theorem (the fibre \(T^2\) itself remains free), the chosen
\(b=-A\sin^2(\pi s/L)\) and its first derivative vanish at each endpoint but not
all derivatives, and the terminal \(C=O(\delta^2)\) must be further removed or
allowed to decay in a nonexact exterior. A flat bump forcing can repair endpoint
smoothness without changing the \(O(\delta)\) scale, but it does not by itself
remove \(C(L)\). Because
\[
 C(L)=-e^{-2I(L)}\int_0^Le^{2I(s)}w(s)b(s)\,ds,
 \qquad I'=u+H,
\]
a monotone discharge with \(w\ge0,b\le0\) necessarily leaves \(C(L)>0\). An exact
exterior splice therefore needs a sign-changing control or an additional
horizontal source; this is a genuine next matching equation, not merely a choice
of smoother cutoff. A pilot two-mode sign-changing solve did satisfy both
\(w(L)=C(L)=0\), but only with \(\max|b|\approx26\delta\) for
\((Q_0,\delta,L)=(10,0.03,1)\). This shows algebraic controllability in one poor
basis, not small-defect feasibility or a lower bound. See
`step90_two_moment_taper_pilot.json` and `step90_constraint_moment_no_go.json`. It is nevertheless decisive against any attempted theorem
that derives \(Q_+=O(\delta)\) solely from mixed Ricci control and one exact OT
end. The local regular exact reduced equations allow any finite center parameter
\(Q_0\); the computed global redshift has been verified for \(Q_0\le100\). After
area redshift, these sampled cores can be discharged to \(q=0\) with
\(O(\delta)\) mixed forcing and only \(O(\delta^2)\) residual in the remaining
horizontal equation.

Files:
`workspace/scripts/step90_radial_twist_taper.py`,
`workspace/data/step90_radial_twist_taper.json`,
`workspace/scripts/step90_taper_scaling_summary.py`,
`workspace/data/step90_taper_scaling_summary.json`,
`workspace/scripts/step90_constraint_moment_no_go.py`, and the exploratory
`workspace/scripts/step90_two_moment_taper.py`.

## 8. Consequence for the route

The reflection-free OT theorem of Steps 87–88 remains intact for genuinely OT
metrics. The forced twist extension is not closed. The structured potential
calculation changes the mechanism:

1. twist's apparent positive drift term is exactly exchanged with its target
   potential source;
2. no current pointwise or resolvent estimate controls a large, localized \(Q\);
3. the radial computation exhibits a concrete redshift-and-discharge mechanism
   consistent with every reduced block to the recorded accuracy;
4. the next mathematical question is global: can such a charged region occur on a
   **free cylindrical base with two outward ends and a minimal separator**, or do
   topology and the two-end area/shape constraints forbid it?

A serious next construction should replace the polar center by a cylindrical
high-twist throat or splice two charged radial halves while keeping the free action,
then solve the full boundary-value problem with a flat-endpoint, sign-changing
control that simultaneously imposes \(w(L)=0\) and \(C(L)=0\). A closely related
exact benchmark already exists in generalized Einstein Dehn filling: the toral
black-hole metric
\[
 h_{BH}=\frac{ds^2}{s^2-a/s}+(s^2-a/s)d\theta^2+s^2g_{\mathbb R^2}
\]
is Einstein on \(D^2\times T^2\), asymptotic to the hyperbolic cusp, and is
patched to cusp ends with a small interpolation error in the cited construction
\cite{li2026poincar}. This does not solve the graph connector—its topology caps a
single cusp and the final Einstein filling may lie on a manifold that does carry
an Einstein metric—but it confirms that the radial redshift geometry is not a
numerical artifact and supplies an exact cap/matching benchmark. A serious next
obstruction should use both ends and the separator, not a purported local
\(Q_+\) estimate. None of this reaches non-free general graph metrics, diffuse
\(S^3\)-neck connected sums, the independent positive branch, or the full
all-dimensional statement.
