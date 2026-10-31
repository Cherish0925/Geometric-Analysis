# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 30,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step30_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step30_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the new Step-30 mathematics. In particular: (i) starting from the chiral transgression, check Lemma Q'' and the exact controlled-collapse limit b_+^{end}=-2-(C+4X)^2 under x=X z^3+o(z^3), p=Pz+o(z), chi=Cz+o(z), eta=Nz+o(z); determine whether the asymptotic assumptions really represent finite-curvature/F-structure control and whether any missing first-jet term changes the formula; (ii) check the fibre/base observable B~=log(kappa/sqrt(1+zeta))+(v-kappa^{-1})/4, its CH vanishing, the derivative B~'=F_beta-E/4, tensor coefficient P_hat >= (1/6)∫WE^2, the Cauchy-Schwarz constant, CH tail integral, and mismatch threshold 0.3702 at T=.70; (iii) interpret the raw anisotropic numerical runs without treating them as regular-bolt constructions. Give explicit corrections if needed and explain what is rigorously established for the diagonal Einstein-gap programme.

## Integrated Scientific Memo

# Step-30 verification memo

## 1. Chiral transgression and Lemma Q″

For every diagonal annulus \(C=[t_0,t_1]\), the established identity is
\[
\widehat P(C)
=\mathfrak b_+(t_1)-\mathfrak b_+(t_0)
+\frac1{2\pi^2}\int_C |W^+|^2
+\frac1{96\pi^2}\int_C s^2 .
\]
Hence, whenever the endpoint data determining \(\mathfrak b_+\) converge,
\[
\liminf_j\widehat P(C_j)\ge b_+^{\rm out}-b_+^{\rm in}.
\]
Thus Lemma Q″ is correct. At a collapsed endpoint, “first-jet convergence” should be stated more precisely as convergence of the normalized self-dual connection coefficients
\[
u_i=p_i-\gamma_i,\qquad
\gamma_i=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},
\]
or any equivalent data guaranteeing convergence of \(\mathfrak b_+\). Merely having
\((x,z,p,\chi,\eta)\to(0,0,0,0,0)\) is insufficient, since the charge depends on ratios such as \(x/z^3\) and \(\chi/z\).

A useful pathwise form, not requiring a round terminal orbit, is
\[
\widehat P[t_0,t_1]\ge
\sup_{t_0\le t\le t_1}\mathfrak b_+(t)-\mathfrak b_+(t_0).
\]

If the outer endpoint is round, \(b_+^{\rm out}=2\), then
\[
\liminf\widehat P\ge 2-b_+^{\rm in}.
\]
For a CH endpoint of radius \(\tau\),
\[
b_+^{\rm out}=2-9\sinh^4\tau.
\]

Equality in the transgression bound forces the nonnegative integrals to vanish. For a convergent sequence this initially means
\[
\int |W^+|^2\to0,\qquad \int s^2\to0;
\]
identifying a smooth ASD scalar-flat limiting metric additionally requires geometric compactness. Burns realizes exact equality.

---

## 2. Controlled-collapse charge: algebra correct, geometric label too strong

Write
\[
q=-3\log z,\qquad \beta=x+\frac q2,
\]
and impose
\[
x=Xz^3+o(z^3),\quad
p=Pz+o(z),\quad
\chi=Cz+o(z),\quad
\eta=Nz+o(z).
\]
The volume-normalized orbit coefficients satisfy
\[
\begin{aligned}
a_f&=e^{2x/3}z^{-1},&
a_g&=e^{-x/3}z^{-1},&
a_h&=e^{-x/3}z^2,\\
p_f&=a_f\!\left(p+\frac23\chi+\frac13\eta\right),&
p_g&=a_g\!\left(p-\frac13\chi+\frac13\eta\right),&
p_h&=a_h\!\left(p-\frac13\chi-\frac23\eta\right).
\end{aligned}
\]
Consequently,
\[
\begin{aligned}
p_f&\to P+\frac23C+\frac13N,\\
p_g&\to P-\frac13C+\frac13N,\\
p_h&\to0,
\end{aligned}
\qquad
(\gamma_f,\gamma_g,\gamma_h)\to(-2X,2X,2).
\]
Therefore
\[
\begin{aligned}
u_f&\to P+\frac23C+\frac13N+2X,\\
u_g&\to P-\frac13C+\frac13N-2X,\\
u_h&\to-2.
\end{aligned}
\]
Using
\[
\mathfrak b_+=2-\sum_i u_i^2-u_fu_gu_h
\]
gives
\[
\boxed{\mathfrak b_+^{\rm end}=-2-(C+4X)^2.}
\]
This is exact. The disappearance of \(P,N\) is not a missing term: when \(u_h=-2\),
\[
\mathfrak b_+=-2-(u_f-u_g)^2,
\]
and \(P,N\) shift \(u_f,u_g\) equally.

It follows rigorously, for this normalized first-jet family, that
\[
\widehat P_{\rm round}\ge4+(C+4X)^2
\]
and, for a CH endpoint,
\[
\widehat P_{\rm CH(\tau)}
\ge4+(C+4X)^2-9\sinh^4\tau.
\]

### The opposite chirality in the supplied script is wrong

The JSON computes a purported \(\mathfrak b_-\) from the \(u_i\), but the opposite chirality uses
\[
w_i=p_i+\gamma_i,\qquad
\mathfrak b_-=\sum_iw_i^2-w_fw_gw_h-2.
\]
Here
\[
(w_f,w_g,w_h)\to
\left(P+\frac23C+\frac13N-2X,\,
P-\frac13C+\frac13N+2X,\,
2\right),
\]
so
\[
\boxed{\mathfrak b_-^{\rm end}=2+(C-4X)^2.}
\]
In particular, at \(C=X=0\) it equals \(2\), as required by the Step-27 Berger row, rather than the JSON value \(-2\). Thus the Step-30 statement that \(N\) enters the opposite chiral charge must also be deleted: \(N\) cancels from both limiting chiral charges.

The corresponding Euler/signature combinations are
\[
\mathfrak b=\frac{\mathfrak b_++\mathfrak b_-}{2}=-8CX,
\qquad
\mathfrak s=\frac{\mathfrak b_- -\mathfrak b_+}{2}
=2+C^2+16X^2.
\]

---

## 3. Missing first-jet term and what the ansatz excludes

Let
\[
\delta=u_h+2.
\]
Without forcing \(u_h\to-2\), there is the exact identity
\[
\boxed{
\mathfrak b_+
=-2-(u_f-u_g)^2+\delta(4-u_fu_g)-\delta^2.}
\]
Thus an opening-rate term \(\delta\) can raise \(\mathfrak b_+\) above \(-2\). The Step-30 ansatz forces \(\delta\to0\), so it does not omit such a term within its stated assumptions; rather, it excludes the raw opening/shear jets for which \(\delta\) remains nonzero. This is precisely the mechanism visible in the raw \(\eta\) runs.

---

## 4. The assumptions are not, by themselves, finite-curvature F-structure control

The phrase “finite-curvature F-structure end” is too strong for
\[
x=Xz^3,\quad \chi=Cz,\quad p=Pz,\quad\eta=Nz.
\]

Put
\[
R=A_g,\qquad
\delta_c=\frac{A_h}{A_g}=z^3,\qquad
A_f=Re^x,\quad A_h=R\delta_c.
\]
At fixed base scale \(R\), the intrinsic orbit-curvature anisotropy has leading size
\[
\operatorname{Ric}^{(3)}_{ff}-\operatorname{Ric}^{(3)}_{gg}
\sim \frac{16x}{R^2\delta_c^2}.
\]
Thus \(x=X\delta_c+o(\delta_c)\) with \(X\ne0\) produces curvature of order
\[
\frac{X}{R^2\delta_c},
\]
which diverges. Uniformly bounded orbit curvature at fixed base scale instead requires
\[
x=O(\delta_c^2)=O(z^6).
\]

Likewise,
\[
y_f-y_g=x'=\frac{\chi}{r}\sim\frac C R
\]
under \(\chi=Cz\) and \(r\sim Rz\). Codazzi-type curvature components contain the collapsing-circle amplification
\[
R_{0fgh}\sim -\frac{2}{R\delta_c}(y_f-y_g),
\]
so fixed-scale collar curvature generally diverges when \(C\ne0\). Bounded-curvature collar control forces the stronger behavior
\[
\chi=O(z^4),
\]
and hence \(C\to0\).

Moreover, the displayed assumptions contain no second-radial-derivative bounds and therefore cannot by themselves control all ambient curvature components.

There is also a compatibility issue if these are interpreted as differentiable asymptotic expansions along one end rather than independent jets on selected sections. Since
\[
\eta=rq'=-3r\frac{z'}z,
\qquad rz'=-\frac{\eta z}{3},
\]
differentiating \(x=Xz^3+o(z^3)\), with corresponding derivative control on the remainder, gives
\[
\chi=rx'=-X\eta z^3+o(z^4),
\]
so \(\eta=Nz+o(z)\) forces \(\chi=o(z)\), i.e. \(C=0\). Nonzero \(C\) therefore describes an independently prescribed section jet or a rapidly varying transition layer, not a smooth slow asymptotic expansion with those leading coefficients.

The correct description of (4) is:

> a finite-\(\mathfrak b_+\), normalized first-jet Berger family,

not automatically a bounded-curvature F-structure end.

This correction strengthens the genuinely bounded-geometry conclusion. Under fixed-base-scale bounded geometry, the problematic \(X,C\) modes vanish and
\[
\mathfrak b_+^{\rm end}\to-2.
\]
More generally, if the collapsed orbit satisfies bounded normalized intrinsic curvature and bounded shape operator, then
\[
\mathfrak b_+
=-2-\bigl(R(k_f-k_g)\bigr)^2+o(1)\le-2+o(1);
\]
with collar regularity the horizontal shear also tends to zero and equality is recovered. Thus a later round decollapse costs at least \(4-o(1)\).

The kernel condition \(C+4X=0\) preserves the plus charge, but does **not** imply bounded curvature.

---

## 5. Fibre/base observable and pinning identity

For
\[
\widetilde B
=\log\frac{\kappa}{\sqrt{1+\zeta}}
+\frac14(v-\kappa^{-1}),
\qquad
v=y_f-\frac{y_g+y_h}{2},
\]
CH has
\[
\kappa=\coth t,\qquad
\zeta=\csch^2t,\qquad
v=\tanh t=\kappa^{-1}.
\]
Since
\[
\sqrt{1+\csch^2t}=\coth t,
\]
one has exactly
\[
\widetilde B|_{\rm CH}=0.
\]

Let
\[
E=\operatorname{Ric}_{ff}
-\frac{\operatorname{Ric}_{gg}+\operatorname{Ric}_{hh}}2.
\]
The control-dependent part of \(v'\) is \(-E\), so direct differentiation gives
\[
\boxed{\widetilde B'=F_\beta-\frac14E.}
\]
The supplied symbolic residual and CH checks support this identity exactly.

The coefficient \(1/4\) is not uniquely forced by CH vanishing: every
\[
B_\lambda=
\log\frac{\kappa}{\sqrt{1+\zeta}}
+\lambda(v-\kappa^{-1})
\]
vanishes on CH and satisfies
\[
B_\lambda'=F_\lambda-\lambda E.
\]
The choice \(\lambda=1/4\) is analytically useful because it cancels a fibre-velocity term in the ACH linearized drift.

The tensor decomposition
\[
|\operatorname{Ric}^{\circ}|^2
=\frac34H^2+\frac23E^2+\frac12D^2
\]
is correct. Since
\[
\widehat P=\frac14\int W|\operatorname{Ric}^{\circ}|^2dt,
\]
it follows that
\[
\boxed{\widehat P\ge\frac16\int WE^2dt.}
\]
Combining this with
\[
\Delta\widetilde B-\int F_\beta\,dt
=-\frac14\int E\,dt
\]
and weighted Cauchy–Schwarz gives
\[
\boxed{
\left|\Delta\widetilde B-\int F_\beta dt\right|
\le
\sqrt{\frac{3\widehat P}{8}}
\left(\int\frac{dt}{W}\right)^{1/2}.}
\]
The coefficient is correct.

---

## 6. CH tail integral and the precise threshold

On exact CH,
\[
W_{\rm CH}=\sinh^3t\cosh t,
\]
and
\[
I(T)=\int_T^\infty\frac{dt}{W_{\rm CH}}
=\frac1{2\sinh^2T}
-\frac12\log\!\left(1+\sinh^{-2}T\right).
\]
Thus, if the correction interval is itself exact CH, or if one has proved
\[
\int_J\frac{dt}{W_g}\le I(T),
\]
then an effective mismatch
\[
C=\left|\Delta\widetilde B-\int_JF_\beta\,dt\right|
\]
implies
\[
\widehat P_J\ge\frac{8C^2}{3I(T)}.
\]

For a general connector, however, the rigorous denominator is
\[
J_g=\int_J\frac{dt}{W_g},
\]
so the unconditional estimate is
\[
\boxed{\widehat P_J\ge\frac{8C^2}{3J_g}.}
\]
Replacing \(J_g\) by the CH value \(I(T)\) requires a volume comparison not supplied in Step 30. A CH terminal first jet alone does not imply that comparison.

At \(T=0.70\),
\[
I(0.70)=0.36531401499170657,
\]
hence
\[
C_*=\sqrt{\frac{3I(0.70)}8}
=0.370125\ldots .
\]
Therefore the usual four-decimal rounding is \(0.3701\). The value \(0.3702\) is a slightly stronger sufficient threshold, not the nearest rounded value.

At the exact Corollary-X3 unit-cost junction,
\[
\sinh^4T=\frac13,\qquad T\approx0.70103,
\]
the corresponding threshold is approximately \(0.3692\).

The ACH expansion of the free drift is also correctly reported:
\[
F_\beta
=z\left(-\frac15s_2+\frac25u-\cosh q+1\right)+O(z^2).
\]
Its constant term vanishes, but the linear term is not sign-definite. Moreover, “small because of the factor \(z\)” requires control of \(q\), since \(z\cosh q\) need not be small outside the standard ACH block.

One may combine the chiral and pinning costs additively when they genuinely apply on disjoint subintervals, potentially reducing a sufficient uniform mismatch threshold below \(0.3701\). Such an optimization is conditional on locating the correction on a CH-sized interval and proving the required \(W\)-comparison; it is not presently a theorem for arbitrary saturation trajectories.

---

## 7. Interpretation of the anisotropic numerical runs

The raw runs are connector computations from freely prescribed collapsed first jets. They are **not** regular-bolt constructions because they omit the preceding cost of producing those jets from smooth bolt data.

### Raw \(\Delta\eta=-8\)

At \(\varepsilon=1/16\),
\[
\mathfrak b_+(0)=1.4519368402,
\]
so the endpoint charge gap to \(2\) is only
\[
2-\mathfrak b_+(0)=0.5480631598.
\]
The collocation value \(0.54541\) lies slightly below this rigorous gap, indicating discretization/transcription error. The independently reconstructed metric has cost \(0.57446\), which is above the gap and is consistent with transgression.

Thus the cheap run does not defeat the chiral law: its initial raw jet has already raised \(\mathfrak b_+\) close to the round value through the omitted \(\delta=u_h+2\) opening-rate mechanism.

At \(\varepsilon=1/32\),
\[
2-\mathfrak b_+(0)=2.9421976,
\]
while the collocation and reconstructed costs are \(2.94250\) and \(2.94303\). Again the cost is essentially the endpoint charge difference. This run also lies on the imposed bounds \(A=5\), \(t_{\rm ch}=0.701\), so it is a constrained numerical value, not evidence for an unconstrained asymptotic minimum.

For an actual \(O(-1)\)-bolt cell, the omitted prefix obeys
\[
\widehat P_{\rm bolt\to entry}\ge \mathfrak b_+(\text{entry})-1.
\]
For the cheapest raw run this contributes at least \(0.45194\). Adding the reconstructed connector cost gives
\[
\widehat P_{\rm total}\ge 0.45194+0.57446\approx1.0264.
\]
Even combining with the underestimated collocation value gives approximately \(0.9973\). Therefore this particular raw run cannot undercut the certified \(0.99585\) cell once its chiral prefix cost is included. This does not replace a construction or lower bound for all possible bolt-to-entry paths, but it correctly explains the reported run.

### Controlled \(N=-8\)

When \(\eta=Nz\) with fixed \(N=-8\), the family lies in the normalized first-jet regime and
\[
\mathfrak b_+^{\rm end}\to-2.
\]
The low finite-\(\varepsilon\) cost \(2.2668\) is therefore a finite-scale entry/matching effect; it cannot change the limiting plus-charge gap to a round orbit.

### Kernel and \(X,C\) runs

The direction \(C+4X=0\) has limiting plus charge \(-2\), and the observed costs \(3.58,3.78\) moving toward \(4\) are consistent with the transgression prediction. They do not prove convergence to \(4\), and the kernel direction is not automatically bounded-curvature geometry.

The large \(X\) and raw \(x=\pm0.25\) runs probe highly curvature-amplified jets. Their large charges and costs are warnings about enlarged initial-data spaces, not regular collapsed competitors.

The run with \(\eta=+0.25\) is marked unsuccessful and should not be used quantitatively.

---

## 8. What is rigorously established for the diagonal Einstein-gap programme

The following statements are rigorous within the supplied diagonal framework:

1. **Relative chiral pricing**
   \[
   \widehat P(C)\ge \mathfrak b_+^{\rm out}-\mathfrak b_+^{\rm in},
   \]
   with endpoint convergence formulated through the normalized chiral connection coefficients.

2. **Exact normalized-jet charge**
   \[
   \mathfrak b_+^{\rm end}=-2-(C+4X)^2.
   \]

3. **Correct opposite charge**
   \[
   \mathfrak b_-^{\rm end}=2+(C-4X)^2,
   \]
   correcting the supplied script and the claim about \(N\).

4. **Conditional round/CH prices**
   \[
   \widehat P_{\rm round}\ge4+(C+4X)^2,
   \]
   \[
   \widehat P_{\rm CH(\tau)}
   \ge4+(C+4X)^2-9\sinh^4\tau.
   \]

5. **Bounded-geometry adiabatic conclusion:** genuine controlled Berger collapse has
   \[
   \mathfrak b_+\le-2+o(1),
   \]
   and under regular collar control \(\mathfrak b_+\to-2\). Hence a subsequent round decollapse costs at least \(4-o(1)\).

6. **Exact fibre/base pinning**
   \[
   \widetilde B'=F_\beta-\frac14E,
   \qquad
   \widehat P\ge\frac16\int WE^2dt,
   \]
   and
   \[
   \left|\Delta\widetilde B-\int F_\beta dt\right|
   \le\sqrt{\frac{3\widehat P}{8}}
   \left(\int W^{-1}dt\right)^{1/2}.
   \]

What remains unproved is precisely:

- that regular small-bolt data reach the selected collapsed section with the required bounded-geometry/first-jet control;
- a comparison of the actual connector integral \(\int W_g^{-1}dt\) with the CH tail \(I(T)\);
- a uniform lower bound for the drift-corrected mismatch;
- the global saturation theorem \(\inf\widehat P_{\rm sat}=4\);
- exclusion or pricing of trajectories that alter the mismatch before entering a CH-sized region;
- construction and functoriality of the analogous adiabatic chiral charge on nonsymmetric F-structure necks.

Accordingly, Step 30 supplies a valid diagonal transgression barrier and an exact pinning identity, but not yet a proof that every regular small-bolt branch pays \(4\), nor a general finite-curvature F-structure theorem.