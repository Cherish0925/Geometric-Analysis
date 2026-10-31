# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 34,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step34_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step34_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

For the non-round collapsed-to-CH opening problem, derive a practical Hamilton–Jacobi subsolution test for V=b_+ + phi(q,eta) in the exact scale-free state/control system. Minimize analytically over controls (Hbar,Ebar,Dbar), state the resulting pointwise inequality, and assess low-degree choices of phi that could add at least the missing ~0.18 beyond the endpoint charge at tau≈0.70. Use the optimizer profile only to identify the compact swap band; do not mistake trajectory fitting for a proof. Explain which other variables need interval enclosures, what endpoint values phi must have, and what region would resist if phi(q,eta) cannot work.

## Integrated Scientific Memo

## Hamilton–Jacobi certificate for the non-round opening

Use the exact scale-free state
\[
X=(x,q,p,\chi,\eta),\qquad q=-3\log z,\qquad \xi=\chi+\frac{\eta}{2},
\]
so that \(q'=\eta\). Define the uncontrolled drifts
\[
\begin{aligned}
A_p&=p^2-\frac{\xi^2}{3}-\frac{\eta^2}{4}+\frac12V_H(x,e^{-q/3}),\\
A_\chi&=-2p\chi+V_x(x,e^{-q/3}),\\
A_\eta&=-2p\eta+V_D(x,e^{-q/3}).
\end{aligned}
\]
Then the exact controlled system in the source script is
\[
\begin{aligned}
x'&=\chi,& q'&=\eta,\\
p'&=A_p-\frac12\bar H,&
\chi'&=A_\chi-\bar E+\frac12\bar D,&
\eta'&=A_\eta-\bar D,
\end{aligned}
\]
with action density
\[
L(\bar H,\bar E,\bar D)
=\frac3{16}\bar H^2+\frac16\bar E^2+\frac18\bar D^2.
\]

Let
\[
V(X)=b_+(X)+\phi(q,\eta),
\]
where \(b_+\) is exactly the chiral flux implemented in `bplus_ca`.

### 1. Analytical minimization over the controls

Writing derivatives of \(b=b_+\) as \(b_x,b_q,b_p,b_\chi,b_\eta\),
\[
\begin{aligned}
\dot V={}&b_x\chi+(b_q+\phi_q)\eta+b_pA_p+b_\chi A_\chi
 +(b_\eta+\phi_\eta)A_\eta\\
&-\frac12b_p\bar H-b_\chi\bar E
 +\left(\frac12b_\chi-b_\eta-\phi_\eta\right)\bar D .
\end{aligned}
\]
The desired inequality \(\dot V\le L\) for every control is equivalent to
\[
\sup_{\bar H,\bar E,\bar D}(\dot V-L)\le0.
\]
The maximizers are
\[
\boxed{
\bar H_*=-\frac43b_p,\qquad
\bar E_*=-3b_\chi,\qquad
\bar D_*=2b_\chi-4(b_\eta+\phi_\eta).
}
\]
Equivalently, these minimize \(L-\dot V\). Substitution gives the exact pointwise test
\[
\boxed{
\begin{aligned}
\mathcal H_\phi={}&b_x\chi+(b_q+\phi_q)\eta
+b_pA_p+b_\chi A_\chi+(b_\eta+\phi_\eta)A_\eta\\
&+\frac13b_p^2+\frac32b_\chi^2
+2\left(\frac12b_\chi-b_\eta-\phi_\eta\right)^2\le0 .
\end{aligned}}
\tag{HJ}
\]

Separate the already known charge part:
\[
\begin{aligned}
\mathcal H_0={}&b_x\chi+b_q\eta+b_pA_p+b_\chi A_\chi+b_\eta A_\eta\\
&+\frac13b_p^2+\frac32b_\chi^2
+2\left(\frac12b_\chi-b_\eta\right)^2,
\end{aligned}
\]
and put
\[
m=-\mathcal H_0,\qquad
K=A_\eta-2b_\chi+4b_\eta.
\]
The chiral charge inequality implies \(m\ge0\) on the exact admissible system. The practical test becomes
\[
\boxed{\eta\phi_q+K\phi_\eta+2\phi_\eta^2\le m.}
\tag{1}
\]
Thus, at fixed state and \(r=\phi_q\), the permissible \(s=\phi_\eta\) form
\[
s\in
\left[
\frac{-K-\sqrt{K^2+8(m-\eta r)}}4,\,
\frac{-K+\sqrt{K^2+8(m-\eta r)}}4
\right],
\tag{2}
\]
provided \(m-\eta r+K^2/8\ge0\). Because \(\phi\) sees only \((q,\eta)\), one common pair \((r,s)\) must obey (1) for every admissible hidden state \((x,p,\chi)\) above that same \((q,\eta)\).

For interval computation, stable derivatives of \(b\) can be obtained from
\[
b=2-\sum_i u_i^2-u_fu_gu_h,\qquad
c_f=-2u_f-u_gu_h
\]
and cyclically. If
\[
\begin{aligned}
v_f&=p+\frac23\chi+\frac13\eta,&
v_g&=p-\frac13\chi+\frac13\eta,&
v_h&=p-\frac13\chi-\frac23\eta,
\end{aligned}
\]
and \(u_i=a_iv_i-\gamma_i\), then
\[
\begin{aligned}
b_p&=c_fa_f+c_ga_g+c_ha_h,\\
b_\chi&=\frac{2c_fa_f-c_ga_g-c_ha_h}{3},\\
b_\eta&=\frac{c_fa_f+c_ga_g-2c_ha_h}{3}.
\end{aligned}
\]
Shape derivatives follow by differentiating the explicit \(a_i,\gamma_i\), avoiding numerical differentiation.

### 2. Endpoint normalization and required gain

Integration of (HJ) yields
\[
\int L\,d\tau\ge
b_+(X_1)-b_+(X_0)+\phi(q_1,\eta_1)-\phi(q_0,\eta_0).
\]
At an exact CH endpoint,
\[
(q_1,\eta_1)=(0,0),\qquad
b_+^{\rm CH}(\tau)=2-9\sinh^4\tau.
\]
At \(\tau=0.70\),
\[
b_+^{\rm CH}\approx-0.980.
\]
For the finite collapsed section used in the static comparison, \(b_+(X_0)\approx-1.79\), so the charge alone contributes about \(0.81\). To reach \(p_*\approx0.99585\), require approximately
\[
\boxed{\phi(0,0)-\phi(Q,N)\gtrsim0.18,}
\tag{3}
\]
with \(Q=q_0\) and \(N=\eta_0\). Normalize
\[
\phi(0,0)=0;
\]
then \(\phi(Q,N)\lesssim-0.18\). On the collapsed entry ray \(N=O(e^{-Q/3})\), so the leading condition is \(\phi(Q,0)\lesssim-0.18\).

This \(0.18\) requirement pertains to the finite collapsed link. In the ideal \(Q\to\infty\) limit, \(b_+\to-2\), whose endpoint increment at \(\tau=0.70\) is already about \(1.02\).

### 3. Low-degree candidates

#### Affine \(q\)-only potential

Take
\[
\phi=-aq.
\]
Then
\[
\Delta\phi=aQ,\qquad
\mathcal H_\phi=\mathcal H_0-a\eta,
\]
and therefore
\[
\boxed{a(-\eta)\le m\quad\text{where }\eta<0.}
\tag{4}
\]
The required slope is
\[
a\gtrsim\frac{0.18}{Q}.
\]
This is \(a\approx0.043\!-\!0.051\) for \(Q=3.5\!-\!4.2\), and \(a\approx0.064\) for \(Q\approx2.8\). Since the optimizer reaches roughly \(\eta\approx-1.25\), \(a=0.05\) needs a certified margin \(m\gtrsim0.063\) there.

More generally, if \(\phi_q=-s(q)\), define the hidden-state envelope
\[
S(q)=
\inf_{\substack{\text{admissible }(x,p,\chi,\eta)\\ \eta<0}}
\frac{m(x,q,p,\chi,\eta)}{-\eta}.
\]
Every \(q\)-only certificate obeys
\[
\boxed{\phi(0)-\phi(Q)\le\int_0^Q S(q)\,dq.}
\tag{5}
\]
Hence an interval upper bound below \(0.18\) for this integral rules out all \(q\)-only choices, not merely affine ones.

#### Endpoint-flat cubic

A useful low-degree redistribution is
\[
\boxed{
\phi(q)=-\delta\left[3(q/Q)^2-2(q/Q)^3\right],
\qquad \delta=0.18.
}
\tag{6}
\]
It has
\[
\phi(0)=0,\quad \phi(Q)=-\delta,\quad
\phi_q(0)=\phi_q(Q)=0.
\]
Its maximum slope is \(3\delta/(2Q)\), about \(0.0675\) for \(Q=4\), larger than the affine slope \(0.045\). It is advantageous only if the certified slack is concentrated in the interior while the collapsed and CH endpoint neighborhoods have little slack.

A quadratic such as
\[
\phi=-aq+\frac{a}{2Q}q^2
\]
can flatten the collapsed endpoint, but doubles the required small-\(q\) slope for a fixed total gain and is therefore less attractive if the CH-side band is restrictive.

#### Quadratic in \((q,\eta)\)

For
\[
\phi=-aq+bq^2+cq\eta+d\eta^2,
\]
equation (1) becomes
\[
\boxed{
\eta(-a+2bq+c\eta)
+K(cq+2d\eta)+2(cq+2d\eta)^2\le m.
}
\tag{7}
\]
The \(\eta\)-terms contribute negligibly to the endpoint gain because \(\eta=0\) at CH and \(N\) is small at collapse. Their sole useful role is local Hamiltonian shaping through \(K\phi_\eta\). Pointwise the best unconstrained value is
\[
\phi_\eta=-K/4,
\]
which lowers the left side by \(K^2/8\); a genuine \(\phi(q,\eta)\) can approximate this only if \(K\) is sufficiently coherent over each hidden-state fiber. If \(K\) changes sign across states with the same \((q,\eta)\), a single \(\phi_\eta\) may worsen the worst case. It is prudent to impose
\[
\phi_\eta(0,0)=0
\]
unless the CH endpoint inequality is separately enclosed.

### 4. What the optimizer does—and does not—establish

The optimizer may only locate the compact swap band. Across the supplied collapsed runs, the relevant approximate ranges are
\[
0\le q\lesssim4.2,\qquad -1.25\lesssim\eta\lesssim0.26,
\]
and, along the sampled trajectories,
\[
0\lesssim x\lesssim1.60,\qquad
0.5\lesssim p\lesssim11.2,\qquad
0\lesssim\chi\lesssim8.2.
\]
The main \(D\)-cost is accumulated during the descent, especially through the middle/late swap: broadly \(q\sim0.5\!-\!2\), with the precise location moving as collapse deepens. This identifies where to refine enclosures; it is not a proof domain and must not be used as one-dimensional trajectory fitting.

A certificate requires interval enclosures of the full admissible set in
\[
(x,q,p,\chi,\eta),
\]
and of the derived quantities
\[
V_D,V_x,V_H,\quad a_i,\gamma_i,u_i,\quad
b_x,b_q,b_p,b_\chi,b_\eta,\quad
A_\eta,\quad m,\quad K.
\]
The \(z^{-4}=e^{4q/3}\) terms demand cancellation-controlled formulas, as already used in the source script. A single Cartesian box over all displayed ranges will combine incompatible values of \(p,\chi,x\) and likely destroy the margin. The enclosure must retain at least the correlations

- \(p,\chi\) against \(q\) near CH;
- \(p,\eta\) against \(q\) near collapse;
- \(x\) against \((q,\eta)\) through the triaxial swap.

The region enclosed must come from independent geometric/dynamical barriers, not merely a tube around an optimal trajectory.

### 5. Precise obstruction to a \(\phi(q,\eta)\) certificate

For each \((q,\eta)\), let \(\mathcal I(q,\eta)\) denote its admissible hidden-state fiber in \((x,p,\chi)\). The actual verification object is
\[
\boxed{
\sup_{(x,p,\chi)\in\mathcal I(q,\eta)}
\left[
-m+\eta\phi_q+K\phi_\eta+2\phi_\eta^2
\right]\le0.
}
\tag{8}
\]
The resistant region is a \(q\)-decreasing fiber with
\[
\eta<0,\qquad m\approx0,\qquad K\approx0.
\]
There, (1) reduces approximately to
\[
\eta\phi_q+2\phi_\eta^2\le0.
\]
But producing the required endpoint gain forces \(\phi_q<0\) somewhere, hence \(\eta\phi_q>0\); the nonnegative quadratic term cannot compensate. More generally, incompatible values or signs of \(K\) over a single hidden-state fiber can make the intersection of the allowable intervals (2) empty.

The optimizer suggests searching first for this obstruction in the triaxial middle/late swap, roughly \(q\in[0.5,2]\), and second on the near-collapsed face if \(m\to0\) there. If such a fiber is rigorously present, no function of \((q,\eta)\) alone can close the missing \(0.18\). A successful extension must then include at least one hidden variable—most naturally \(x\), \(p\), or \(\chi\)—or combine the charge with the exact \(D\)-channel Green estimate, which retains incoming anisotropy momentum and Einstein drift that \((q,\eta)\) alone cannot distinguish.