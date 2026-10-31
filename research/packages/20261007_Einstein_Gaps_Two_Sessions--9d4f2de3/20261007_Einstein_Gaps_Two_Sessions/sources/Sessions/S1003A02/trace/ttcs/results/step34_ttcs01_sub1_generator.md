# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/saturation_optimal_control.py",
    "Sessions/S1003A02/workspace/data/saturation_control/nonround_opening_profile.json",
    "Sessions/S1003A02/workspace/data/saturation_control/eps0p0625_N60_ch_bpmax_m1.json",
    "Sessions/S1003A02/workspace/data/static_charge/path_K10_t0.7-1.6_detour.json",
    "Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md",
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md"
  ]
}
```

## Task

For the non-round collapsed-to-CH opening problem, derive a practical Hamilton–Jacobi subsolution test for V=b_+ + phi(q,eta) in the exact scale-free state/control system. Minimize analytically over controls (Hbar,Ebar,Dbar), state the resulting pointwise inequality, and assess low-degree choices of phi that could add at least the missing ~0.18 beyond the endpoint charge at tau≈0.70. Use the optimizer profile only to identify the compact swap band; do not mistake trajectory fitting for a proof. Explain which other variables need interval enclosures, what endpoint values phi must have, and what region would resist if phi(q,eta) cannot work.

## Output

### Exact HJ reduction

Use \(q=-3\log z\), so \(z=e^{-q/3}\) and \(q'=\eta\). Write
\[
\xi=\chi+\frac{\eta}{2},
\]
and define
\[
\begin{aligned}
A_p&=p^2-\frac{\xi^2}{3}-\frac{\eta^2}{4}+\frac12V_H(x,q),\\
A_\chi&=-2p\chi+V_x(x,q),\\
A_\eta&=-2p\eta+V_D(x,q).
\end{aligned}
\]
The controlled system becomes
\[
\begin{aligned}
x'&=\chi,\qquad q'=\eta,\\
p'&=A_p-\frac12\bar H,\\
\chi'&=A_\chi-\bar E+\frac12\bar D,\\
\eta'&=A_\eta-\bar D,
\end{aligned}
\]
with running density
\[
L(\bar H,\bar E,\bar D)
=\frac{3}{16}\bar H^2+\frac16\bar E^2+\frac18\bar D^2.
\]

Let \(b=b_+(x,q,p,\chi,\eta)\), and set
\[
V=b+\phi(q,\eta).
\]
A subsolution inequality is
\[
\frac{d}{d\tau}V\le L
\]
for every state and every control. Integration then gives
\[
\int_{\tau_0}^{\tau_1}L\,d\tau
\ge V(\tau_1)-V(\tau_0).
\]

---

### Derivatives of \(b_+\)

Introduce
\[
\begin{aligned}
a_f&=e^{2\beta/3},&
a_g&=e^{-\beta/3+q/2},&
a_h&=e^{-\beta/3-q/2},\\
\beta&=x+\frac q2,
\end{aligned}
\]
and
\[
\begin{aligned}
v_f&=p+\frac23\chi+\frac13\eta,\\
v_g&=p-\frac13\chi+\frac13\eta,\\
v_h&=p-\frac13\chi-\frac23\eta.
\end{aligned}
\]
The normalized first-jet variables are
\[
u_i=a_i v_i-\gamma_i(x,q),
\]
where
\[
\begin{aligned}
\gamma_f&=\frac{a_g^2+a_h^2-a_f^2}{a_ga_h},\\
\gamma_g&=\frac{a_h^2+a_f^2-a_g^2}{a_ha_f},\\
\gamma_h&=\frac{a_f^2+a_g^2-a_h^2}{a_fa_g}.
\end{aligned}
\]
Then
\[
b=2-u_f^2-u_g^2-u_h^2-u_fu_gu_h.
\]
Set
\[
c_f=-2u_f-u_gu_h,\qquad
c_g=-2u_g-u_fu_h,\qquad
c_h=-2u_h-u_fu_g.
\]
Since \(b_{u_i}=c_i\), the derivatives in the velocity variables are especially simple:
\[
\begin{aligned}
b_p&=c_fa_f+c_ga_g+c_ha_h,\\
b_\chi&=\frac13(2c_fa_f-c_ga_g-c_ha_h),\\
b_\eta&=\frac13(c_fa_f+c_ga_g-2c_ha_h).
\end{aligned}
\]
For the shape derivatives,
\[
b_x=c_f(u_f)_x+c_g(u_g)_x+c_h(u_h)_x,
\]
\[
b_q=c_f(u_f)_q+c_g(u_g)_q+c_h(u_h)_q.
\]
This is convenient for interval evaluation because the \(u_i\) and their derivatives can be enclosed directly. For example,
\[
(a_f)_x=\frac23a_f,\quad (a_f)_q=\frac13a_f,
\]
\[
(a_g)_x=-\frac13a_g,\quad (a_g)_q=\frac13a_g,
\]
\[
(a_h)_x=-\frac13a_h,\quad (a_h)_q=-\frac23a_h,
\]
and the derivatives of \(\gamma_i\) follow by differentiating their explicit rational expressions in \(a_f,a_g,a_h\).

---

### Exact minimization over \((\bar H,\bar E,\bar D)\)

The drift of \(V\) is
\[
\begin{aligned}
\dot V={}&b_x\chi+(b_q+\phi_q)\eta
+b_p\left(A_p-\frac12\bar H\right)\\
&+b_\chi\left(A_\chi-\bar E+\frac12\bar D\right)
+(b_\eta+\phi_\eta)(A_\eta-\bar D).
\end{aligned}
\]
Thus the control-linear coefficients in \(\dot V\) are
\[
k_H=-\frac12b_p,\qquad
k_E=-b_\chi,\qquad
k_D=\frac12b_\chi-b_\eta-\phi_\eta.
\]

The supremum of \(\dot V-L\) over unrestricted controls is attained at
\[
\boxed{
\bar H_*=-\frac43b_p,\qquad
\bar E_*=-3b_\chi,\qquad
\bar D_*=2b_\chi-4(b_\eta+\phi_\eta).
}
\]
The resulting maximized Hamiltonian is
\[
\boxed{
\begin{aligned}
\mathscr H_\phi={}&b_x\chi+(b_q+\phi_q)\eta
+b_pA_p+b_\chi A_\chi+(b_\eta+\phi_\eta)A_\eta\\
&+\frac13b_p^2+\frac32b_\chi^2
+2\left(\frac12b_\chi-b_\eta-\phi_\eta\right)^2.
\end{aligned}}
\tag{HJ}
\]
Therefore a pointwise HJ subsolution test is simply
\[
\boxed{\mathscr H_\phi(x,q,p,\chi,\eta)\le0.}
\]

It is useful to separate the known \(b_+\) part. Define
\[
\begin{aligned}
\mathscr H_0={}&b_x\chi+b_q\eta+b_pA_p+b_\chi A_\chi+b_\eta A_\eta\\
&+\frac13b_p^2+\frac32b_\chi^2
+2\left(\frac12b_\chi-b_\eta\right)^2,
\end{aligned}
\]
and
\[
K=A_\eta-2b_\chi+4b_\eta.
\]
Then the entire effect of \(\phi\) is
\[
\boxed{
\mathscr H_\phi
=\mathscr H_0+\eta\phi_q+K\phi_\eta+2\phi_\eta^2.
}
\tag{1}
\]
The chiral charge identity gives \(\mathscr H_0\le0\). Put
\[
m(X)=-\mathscr H_0(X)\ge0.
\]
The extra potential must therefore satisfy
\[
\boxed{
\eta\phi_q+K\phi_\eta+2\phi_\eta^2\le m(X).
}
\tag{2}
\]
This is the practical form of the test.

For fixed \(X\), \(q\), \(\eta\), and \(r=\phi_q\), the allowed values \(s=\phi_\eta\) lie between
\[
\boxed{
s_\pm=
\frac{-K\pm\sqrt{K^2-8(\mathscr H_0+\eta r)}}{4},
}
\tag{3}
\]
provided the square root is real. Since \(\phi\) only sees \((q,\eta)\), the same pair \((r,s)\) must satisfy (3) simultaneously for every admissible \((x,p,\chi)\) above that \((q,\eta)\).

---

### Endpoint amount required from \(\phi\)

On the CH orbit at radius \(\tau\),
\[
q=0,\qquad \eta=0,
\]
and
\[
b_{\mathrm{CH}}(\tau)=2-9\sinh^4\tau.
\]
At \(\tau=0.70\),
\[
\sinh^2(0.70)\simeq0.57545,\qquad
b_{\mathrm{CH}}(0.70)\simeq-0.980.
\]

For the finite collapsed section used in the static charge comparison, \(b_0\simeq-1.79\), so the endpoint charge increase is approximately
\[
b_{\mathrm{CH}}(0.70)-b_0\simeq0.81.
\]
To reach \(p_*\simeq0.99585\), one needs
\[
\phi(0,0)-\phi(Q,N)\gtrsim0.18,
\tag{4}
\]
where
\[
Q=q_{\rm in},\qquad N=\eta_{\rm in}.
\]
The collapsed entry ray has \(N=O(e^{-Q/3})\), so the leading requirement is
\[
\phi(0,0)-\phi(Q,0)\gtrsim0.18.
\]
Normalize \(\phi(0,0)=0\). Then
\[
\boxed{\phi(Q,0)\lesssim-0.18.}
\]

For the exact asymptotic Taub–NUT state, \(b_0\to-2\), and the same CH radius gives
\[
b_{\mathrm{CH}}(0.70)-(-2)\simeq1.02.
\]
Thus the extra \(\phi\)-gain is mainly needed for the finite collapsed section used in the \(b_+\)-only comparison, not for the idealized \(Q\to\infty\) value itself.

---

### Low-degree choices

#### 1. Affine \(q\)-potential

Take
\[
\phi(q,\eta)=-a q.
\]
Then
\[
\phi_q=-a,\qquad \phi_\eta=0,
\]
and
\[
\mathscr H_\phi=\mathscr H_0-a\eta.
\]
The endpoint gain is
\[
\Delta\phi=aQ.
\]
Hence
\[
a\gtrsim\frac{0.18}{Q}.
\]
For \(Q=3.5\)–\(4.2\),
\[
a\simeq0.043\text{--}0.051.
\]
For the smaller \(Q\simeq2.8\) section,
\[
a\simeq0.064.
\]

The HJ condition becomes
\[
\boxed{a(-\eta)\le m(X)\qquad\text{whenever }\eta<0.}
\tag{5}
\]
The optimizer profile suggests \(\eta\) down to approximately \(-1.3\) in the compact swap band. Thus an affine potential with \(a\approx0.05\) needs approximately
\[
m\gtrsim0.065
\]
throughout the part of the band where \(\eta\approx-1.3\). If the interval lower value of \(m\) drops below this, the affine potential cannot be certified there.

A useful one-dimensional capacity test is obtained by writing
\[
\phi_q=-s(q),\qquad s(q)\ge0.
\]
Then (5) gives
\[
s(q)\le
S(q):=
\inf_{\substack{(x,p,\chi)\ {\rm admissible}\\ \eta<0}}
\frac{m(x,q,p,\chi,\eta)}{-\eta}.
\]
The maximum endpoint gain available to any \(q\)-only potential is bounded by
\[
\boxed{
\phi(0)-\phi(Q)
=\int_0^Q s(q)\,dq
\le\int_0^Q S(q)\,dq.
}
\tag{6}
\]
If the right-hand side is below \(0.18\), no choice of \(q\)-only polynomial, affine or otherwise, can supply the required amount.

#### 2. Quadratic \(q\)-potential

Take
\[
\phi(q)=-a q+bq^2.
\]
With \(\phi(0)=0\), the endpoint requirement is
\[
aQ-bQ^2\gtrsim0.18.
\tag{7}
\]
The HJ contribution is
\[
\eta(-a+2bq).
\]
Choosing \(b>0\) makes the slope smaller at larger \(q\), which can reduce the cost near the collapsed end, but it increases the magnitude of the slope near \(q=0\). The interval profile of
\[
\frac{m(X)}{-\eta}
\]
decides whether this redistribution helps.

A particularly useful endpoint-flat version is obtained by imposing \(\phi_q(Q)=0\):
\[
\phi(q)=-a q+\frac{a}{2Q}q^2.
\]
Then
\[
\phi(Q)=-\frac{aQ}{2},
\]
so \(a=2\delta/Q\) gives endpoint gain \(\delta\). For \(\delta=0.18\) and \(Q=4\), this gives \(a=0.09\). The derivative is
\[
\phi_q=-a\left(1-\frac qQ\right),
\]
which vanishes at the large-\(q\) endpoint and can be extended as a constant for \(q\ge Q\). Its maximum slope is larger than the affine choice, so it helps only if the available slack is concentrated away from the collapsed end.

A cubic interpolation can vanish at both ends:
\[
\boxed{
\phi(q)=-\delta\left[3\left(\frac qQ\right)^2
-2\left(\frac qQ\right)^3\right].
}
\tag{8}
\]
It satisfies
\[
\phi(0)=0,\qquad \phi(Q)=-\delta,\qquad
\phi_q(0)=\phi_q(Q)=0,
\]
and
\[
\phi_q(q)=-\frac{6\delta}{Q^3}q(Q-q).
\]
For \(Q=4\), \(\delta=0.18\), the largest slope magnitude is about \(0.0675\). This is larger than the affine slope \(0.045\), but the derivative disappears at both endpoint regimes. Such an endpoint-flat polynomial is the most natural low-degree candidate if the large-\(q\) region and the CH neighborhood each have small \(|\eta|\).

#### 3. Adding \(\eta\)-dependence

Take
\[
\phi(q,\eta)=-a q+bq^2+cq\eta+d\eta^2.
\]
Then
\[
\phi_q=-a+2bq+c\eta,\qquad
\phi_\eta=cq+2d\eta,
\]
and the exact extra HJ term is
\[
\boxed{
\eta(-a+2bq+c\eta)
+K(cq+2d\eta)
+2(cq+2d\eta)^2.
}
\tag{9}
\]
The \(cq\eta\) and \(d\eta^2\) terms contribute very little to the endpoint value because \(N=\eta_{\rm in}\) is small, so they cannot themselves provide the missing \(0.18\). Their role is to exploit the \(K\phi_\eta\) term and enlarge the available HJ slack.

For an affine potential
\[
\phi=Aq+C\eta,
\]
the two requirements become
\[
-AQ-CN\gtrsim0.18,
\tag{10}
\]
and
\[
\boxed{
A\eta+CK+2C^2\le m(X).
}
\tag{11}
\]
At a fixed state, the best local choice of \(C\) is \(C=-K/4\), which gains \(K^2/8\) in the HJ inequality. A single constant \(C\) is useful only when \(K\) has a fairly stable sign and size across all hidden states sharing the same \((q,\eta)\). If \(K\) changes sign over that set, the \(C K\) term helps one part and raises the Hamiltonian in another.

At the CH point \((q,\eta)=(0,0)\), a nonzero \(s=\phi_\eta(0,0)\) must satisfy
\[
\mathscr H_0+K s+2s^2\le0
\]
for every CH state being used. Setting
\[
\phi_\eta(0,0)=0
\]
avoids introducing a new endpoint restriction and is naturally compatible with the \(q\)-only and endpoint-flat cubic choices.

---

### Compact swap band and the required interval data

The supplied optimizer profiles indicate a compact kinematic band roughly of the form
\[
0\le q\lesssim4.2,\qquad
-1.3\lesssim\eta\lesssim0.3.
\]
For the displayed runs, the associated variables reach approximately
\[
0\lesssim x\lesssim1.7,\qquad
0.5\lesssim p\lesssim12,\qquad
0\lesssim\chi\lesssim9,
\]
with substantially narrower correlations along the actual path. These numbers identify where the swap occurs; they do not provide the HJ verification.

For a pointwise certificate, one needs interval enclosures for

\[
(q,\eta,x,p,\chi),
\]
together with derived enclosures for

\[
a_f,a_g,a_h,\quad
u_i,\quad
b_x,b_q,b_p,b_\chi,b_\eta,\quad
A_\eta,\quad
m=-\mathscr H_0,\quad
K.
\]

The variable \(z\) is fixed by \(q\), but the terms \(z^{-4}\) in \(V_D,V_x,V_H\) require cancellation-stable interval formulas near the collapsed end. A single Cartesian box such as
\[
[0,4.2]\times[-1.3,0.3]\times[0,1.7]\times[0.5,12]\times[0,9]
\]
will almost certainly be too broad: it combines \(p,\chi\) values that do not coexist at fixed \(q,\eta\), and it can erase the available slack \(m\). The useful enclosure must preserve correlations, especially

- \(p,\chi\) versus \(q\) near the CH endpoint;
- \(p,\eta\) versus \(q\) near the collapsed entry;
- the triaxial shape variable \(x\) during the middle of the swap.

The optimizer profile indicates that the largest \(D\)-channel cost occurs while \(q\) descends through approximately \(q\in[0.5,2]\). This is the first interval region in which \(m\), \(K\), and the admissible hidden-state set should be examined. The profile itself supplies no pointwise HJ inequality.

---

### Where a two-variable \(\phi(q,\eta)\) would be resisted

The decisive obstruction is a hidden-state one. Suppose two admissible states have the same \((q,\eta)\) but different \((x,p,\chi)\). Then they have the same \(\phi_q,\phi_\eta\), while their values of \(m\) and \(K\) may differ. A two-variable potential exists only if one pair
\[
(\phi_q(q,\eta),\phi_\eta(q,\eta))
\]
satisfies
\[
\eta\phi_q+K\phi_\eta+2\phi_\eta^2\le m
\]
for the entire hidden-state fiber.

The most resistant set is characterized by
\[
\eta<0,\qquad m\approx0,\qquad K\approx0.
\]
There,
\[
\eta\phi_q+2\phi_\eta^2\le0.
\]
A potential that supplies endpoint gain must have \(\phi_q<0\) over part of the \(q\)-interval. Since \(\eta<0\), the first term is then strictly positive, and no choice of \(\phi_\eta\) can compensate when \(K\) and \(m\) are both small. Geometrically, this is a near-Einstein, \(q\)-decreasing channel carrying shape motion with little available chiral slack.

In the present problem this set is most likely to appear in the triaxial swap portion of the descent, especially around \(q\in[0.5,2]\), where the optimizer shows large \(D\)-channel activity while the chiral charge itself changes little. The collapsed Taub–NUT-like face at larger \(q\) is another possible resistant set if \(m\) approaches zero there and \(\phi_q\) is kept nonzero.

Thus the decisive numerical object is not a fitted potential along one optimizer path, but the hidden-state envelope
\[
\sup_{(x,p,\chi)\in\mathcal I(q,\eta)}
\left[
\mathscr H_0+\eta\phi_q+K\phi_\eta+2\phi_\eta^2
\right].
\]
If this envelope stays at most zero on the swap band and the endpoint values satisfy (4), then \(b_++\phi\) supplies the missing action. If the envelope becomes positive on a set with \(m\) near zero and \(\eta<0\), then no potential depending only on \((q,\eta)\) can price that part of the opening; the representation must then include at least one of the hidden variables \(x,p,\chi\), or use a separate Green-type estimate for the \(D\)-channel.