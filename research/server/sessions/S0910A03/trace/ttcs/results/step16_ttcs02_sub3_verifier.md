# TTCS Independent Branch Record

```json
{
  "step_id": 16,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md",
    "Sessions/S0910A03/workspace/notes/step15_L2_chain_and_separated_demands.md",
    "Sessions/S0910A03/workspace/scripts/verify_cutoff_defect_energy.py",
    "Sessions/S0910A01/workspace/notes/step16_preceptor_review_smoothing_architecture.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Independently scrutinize the proposed coupled transition-inclusive cutoff-flow estimate for a=chi^2: can one plausibly prove persistence of local normalized L2 curvature energy and global L2 Einstein defect using only initial |Ric+g|<=delta, local normalized ∫|Rm|² small at all centers on a support of fixed multiple of r, a relative Sobolev inequality, and controlled cutoff derivatives? Derive or inspect the full curvature evolution under ∂_t g=-2a(Ric+g), especially terms involving derivatives of a and E. Determine whether terms like ∇²a*E*Rm and ∇a*∇E*Rm close with available dissipation, whether higher cutoff derivatives or unweighted ∇E outside a>0 cause singular losses near chi=0, and what exact coupled inequalities would suffice for continuation and metric equivalence. Do not merely repeat the schematic system; identify a valid energy architecture or a specific mathematical obstruction/new assumption.

## Output

## Scientific memo: transition-inclusive \(a=\chi^2\) cutoff flow

### 1. Curvature evolution under \(\partial_t g=-2a(\operatorname{Ric}+g)\)

Let  
\[
E_{ij}=\operatorname{Ric}_{ij}+g_{ij},\qquad a=\chi^2 .
\]
Wang’s supplied local Ricci-flow formula for \(\partial_tg=-2a\operatorname{Ric}\) gives the correct starting point. Adding the pure local scaling term \(-2ag\) contributes \(-2aR_{ijkl}\) in the constant-\(a\) part and Hessian-\(a\) terms with \(g\). These combine with the Ricci Hessian terms into Hessian-\(a\) times \(E=\operatorname{Ric}+g\). Thus, schematically and with the derivative-\(a\) terms explicitly,

\[
\partial_t R_{ijkl}
=
a\,\mathcal N_{ijkl}(\mathrm{Rm})
+\mathcal D_a(E)_{ijkl},
\]

where

\[
\begin{aligned}
\mathcal N_{ijkl}={}&
\Delta R_{ijkl}
+R_{ijpq}R_{pqkl}
+2R_{ipkq}R_{jplq}
-2R_{iplq}R_{jpkq} \\
&-\bigl(
R_{ip}R_{pjkl}
+R_{jp}R_{ipkl}
+R_{kp}R_{ijpl}
+R_{lp}R_{ijkp}
\bigr)
-2R_{ijkl},
\end{aligned}
\]

and

\[
\begin{aligned}
\mathcal D_a(E)_{ijkl}={}&
-\bigl[
a_{ik}E_{jl}
+a_{jl}E_{ik}
-a_{il}E_{jk}
-a_{jk}E_{il}
\bigr] \\
&-\bigl[
a_i\nabla_kE_{jl}
+a_k\nabla_iE_{jl}
+a_j\nabla_lE_{ik}
+a_l\nabla_jE_{ik} \\
&\qquad
-a_j\nabla_kE_{il}
-a_k\nabla_jE_{il}
-a_l\nabla_iE_{jk}
-a_i\nabla_lE_{jk}
\bigr],
\end{aligned}
\]
with \(a_i=\nabla_i a\), \(a_{ik}=\nabla_i\nabla_k a\).

This is the key structural point: the transition terms contain \(E\) or \(\nabla E\), not a bare \(g\)-source. Hence an exact metric with \(\operatorname{Ric}+g=0\) is stationary even where \(\chi\) varies.

For \(a=\chi^2\),

\[
\nabla a=2\chi\nabla\chi,\qquad
\nabla^2a=2\chi\nabla^2\chi+2\nabla\chi\otimes\nabla\chi,
\]
and
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2
\quad\text{on }\{\chi>0\}.
\]
So the dangerous-looking \(\nabla a\cdot\nabla E\) term carries exactly one factor of \(\chi\), matching the weighted defect dissipation \(a|\nabla E|^2=\chi^2|\nabla E|^2\). There is no \(1/\chi\) singularity at the support rim.

---

### 2. Curvature \(L^2\) energy with transition terms included

Let \(\eta\) be an independent localization cutoff. Accounting also for norm and volume variation under \(\partial_tg=-2aE\), one obtains an estimate of the form

\[
\begin{aligned}
\frac{d}{dt}\int \eta^2 |\mathrm{Rm}|^2
+c\int \eta^2 a|\nabla\mathrm{Rm}|^2
\le{}&
C\int
\bigl(
a|\nabla\eta|^2+\eta^2|\nabla\chi|^2+\eta^2a
\bigr)|\mathrm{Rm}|^2 \\
&+C\int \eta^2a|\mathrm{Rm}|^3 \\
&+C\int \eta^2|\nabla^2a|\,|E|\,|\mathrm{Rm}| \\
&+C\int \eta^2|\nabla a|\,|\nabla E|\,|\mathrm{Rm}|.
\end{aligned}
\]

The two transition terms behave as follows.

#### The \(\nabla a\cdot\nabla E\cdot\mathrm{Rm}\) term

Using \(\nabla a=2\chi\nabla\chi\),

\[
\begin{aligned}
\int \eta^2|\nabla a|\,|\nabla E|\,|\mathrm{Rm}|
&\le
C\int \eta^2 \chi|\nabla\chi|\,|\nabla E|\,|\mathrm{Rm}| \\
&\le
\varepsilon\int \eta^2\chi^2|\nabla E|^2
+C_\varepsilon\int \eta^2|\nabla\chi|^2|\mathrm{Rm}|^2 .
\end{aligned}
\]

Thus this term closes only after coupling the curvature energy to the defect energy. It should not be placed in a standalone curvature inequality.

#### The \(\nabla^2a\cdot E\cdot\mathrm{Rm}\) term

If the transition width is comparable to \(r\), with

\[
|\nabla\chi|\le Cr^{-1},\qquad
|\nabla^2\chi|\le Cr^{-2},
\]
then

\[
|\nabla^2a|
\le C r^{-2},
\]
and therefore

\[
\int \eta^2|\nabla^2a|\,|E|\,|\mathrm{Rm}|
\le
Cr^{-2}\int \eta^2\bigl(|E|^2+|\mathrm{Rm}|^2\bigr).
\]

This is a lower-order \(r^{-2}\)-term. Over time \(t\le \theta r^2\), it contributes only a Gronwall factor \(e^{C\theta}\).

So the transition terms are not the main obstruction at the \(L^2\) level. The square choice \(a=\chi^2\) is exactly what makes the first-derivative term compatible with weighted defect dissipation.

---

### 3. Defect energy estimate

Step 14’s formula for

\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)
\]

has the needed homogeneity. After integration by parts, the Hessian-\(a\) terms cancel into first-derivative cutoff terms. The resulting estimate is

\[
\begin{aligned}
\frac{d}{dt}\int \eta^2 |E|^2
+c\int \eta^2a|\nabla E|^2
\le{}&
C\int
\bigl(
a|\nabla\eta|^2+\eta^2|\nabla\chi|^2+\eta^2a
\bigr)|E|^2 \\
&+C\int \eta^2a|\mathrm{Rm}|\,|E|^2 .
\end{aligned}
\]

The Python script `verify_cutoff_defect_energy.py` verifies the algebraic homogeneity of the displayed integrated expression and the identity \(|d(\chi^2)|^2/\chi^2=4|d\chi|^2\). It is a useful sanity computation, though the geometric integration by parts still rests on the tensor derivation.

---

### 4. Sobolev absorption and the correct coupled inequality

On a ball \(B\) of radius \(r\), assume a relative Sobolev inequality

\[
\|v\|_{L^4(B)}^2
\le
A_B\left(
\|\nabla v\|_{L^2(B)}^2+r^{-2}\|v\|_{L^2(B)}^2
\right),
\]
with

\[
A_B\lesssim \frac{r^2}{\operatorname{Vol}(B)^{1/2}}.
\]

If the normalized local curvature energy is small,

\[
\frac{r^4}{\operatorname{Vol}(B)}
\int_B |\mathrm{Rm}|^2
\le \varepsilon,
\]
then

\[
A_B\|\mathrm{Rm}\|_{L^2(B)}
\lesssim
\left(
\frac{r^4}{\operatorname{Vol}(B)}
\int_B|\mathrm{Rm}|^2
\right)^{1/2}
\le C\varepsilon^{1/2}.
\]

This is the four-dimensional volume cancellation.

For \(v=\eta\chi|\mathrm{Rm}|\),

\[
\int \eta^2a|\mathrm{Rm}|^3
\le
\|\mathrm{Rm}\|_2\|\eta\chi|\mathrm{Rm}|\|_4^2
\]
is absorbed into

\[
\int \eta^2a|\nabla\mathrm{Rm}|^2
\]
plus \(Cr^{-2}\int|\mathrm{Rm}|^2\), provided \(\varepsilon\) is small.

Similarly, with \(v=\eta\chi|E|\),

\[
\int \eta^2a|\mathrm{Rm}|\,|E|^2
\]
is absorbed into

\[
\int \eta^2a|\nabla E|^2
\]
plus \(Cr^{-2}\int|E|^2\).

The precise local coupled architecture should therefore be

\[
\boxed{
\frac{d}{dt}R_\alpha
+cX_\alpha
\le
Cr^{-2}\sum_{\beta\sim\alpha}(R_\beta+P_\beta)
+\varepsilon_1Y_\alpha ,
}
\]

\[
\boxed{
\frac{d}{dt}P_\alpha
+cY_\alpha
\le
Cr^{-2}\sum_{\beta\sim\alpha}P_\beta .
}
\]

Here

\[
R_\alpha
=
\frac{r^4}{V_\alpha}
\int \eta_\alpha^2|\mathrm{Rm}|^2,
\qquad
P_\alpha
=
\frac{r^4}{V_\alpha}
\int \eta_\alpha^2|E|^2,
\]

\[
X_\alpha
=
\frac{r^4}{V_\alpha}
\int \eta_\alpha^2a|\nabla\mathrm{Rm}|^2,
\qquad
Y_\alpha
=
\frac{r^4}{V_\alpha}
\int \eta_\alpha^2a|\nabla E|^2,
\]
and \(\beta\sim\alpha\) denotes the bounded set of neighboring balls arising from cutoff derivatives and Sobolev supports.

Choosing \(\kappa>0\) large enough, the combined quantity

\[
H_\alpha=R_\alpha+\kappa P_\alpha
\]
satisfies

\[
\frac{d}{dt}H_\alpha
+cX_\alpha+cY_\alpha
\le
Cr^{-2}\sum_{\beta\sim\alpha}H_\beta .
\]

Taking the supremum over the covering gives

\[
D^+H(t)\le Cr^{-2}H(t),
\qquad
H(t)=\sup_\alpha H_\alpha(t).
\]

Thus, over \(0\le t\le\theta r^2\),

\[
H(t)\le e^{C\theta}H(0).
\]

This is the clean transition-inclusive replacement for the earlier inner/outer propagation argument. It uses no finite-propagation principle.

---

### 5. Global \(L^2\) Einstein defect

For \(\eta\equiv1\), the defect energy inequality gives

\[
\frac{d}{dt}Q(t)
+c\int a|\nabla E|^2
\le
C\int (|\nabla\chi|^2+a)|E|^2
+C\int a|\mathrm{Rm}|\,|E|^2,
\]
where

\[
Q(t)=\int_M |E(t)|^2\,d\mu_t .
\]

Using the same local Sobolev absorption on the active region,

\[
\frac{d}{dt}Q(t)
\le
Cr^{-2}Q(t),
\]
so

\[
Q(t)\le e^{C\theta}Q(0)
\qquad
\text{for }0\le t\le\theta r^2.
\]

This preserves the global \(L^2\) defect up to a uniform factor. It does not create smallness from nothing: one still needs \(Q(0)\) small in the normalization relevant to the topological argument, for example \(Q(0)/A_i\to0\) in the LeBrun/Ishida-LeBrun setting.

---

### 6. What is supplied by the energy architecture, and what is not

At the \(L^2\) level, the transition terms are compatible with the available dissipations:

- \(\nabla a\cdot\nabla E\cdot\mathrm{Rm}\) closes by borrowing weighted defect dissipation.
- \(\nabla^2a\cdot E\cdot\mathrm{Rm}\) is a lower-order \(r^{-2}(R+P)\) contribution.
- No unweighted \(\nabla E\) term survives near \(\chi=0\), because \(\nabla a=2\chi\nabla\chi\).
- Higher cutoff derivatives do not enter the basic \(L^2\) curvature/defect inequalities.

The real extra analytic input is geometric rather than algebraic. The absorption above must be performed at time \(t\), so one needs along-flow control of:

\[
A_B(t)\lesssim A_B(0),
\qquad
|\nabla\chi|_{g(t)}\le Cr^{-1},
\qquad
|\nabla^2\chi|_{g(t)}\le Cr^{-2}.
\]

Metric equivalence controls \(|\nabla\chi|\), but it does not by itself control \(\nabla^2\chi\), since the connection changes. For a fixed scalar cutoff,

\[
\partial_t(\nabla^2\chi)
\sim
\nabla(aE)*d\chi
=
a\nabla E*d\chi+\chi\nabla\chi*E*d\chi .
\]

The available energy gives \(a^{1/2}\nabla E\in L^2\), not an \(L^\infty\) Hessian bound for \(\chi\). Wang’s Section 4 smooth-extension discussion shows precisely that higher derivatives of \(\chi\) and derivatives of \(\chi^2\mathrm{Rm}\) interact in local Ricci flow. Thus “controlled cutoff derivatives” must either be assumed along the flow or furnished by a local-flow theorem.

Metric equivalence also requires more than \(L^2\) defect preservation. Since

\[
\partial_tg=-2aE,
\]
one needs

\[
\int_0^{\theta r^2}\sup_M a|E(t)|\,dt
\]
to be bounded, and for closeness to the initial metric one wants it to be \(o(1)\). A sufficient estimate would be

\[
\sup_M a|E(t)|
\le
C\delta\left(\frac{r^2}{t}\right)^\gamma,
\qquad \gamma<1,
\]
which yields

\[
\left|
\log\frac{g(t)(v,v)}{g(0)(v,v)}
\right|
\le
C\delta r^2 .
\]

Li’s Corollary 3.5 gives such an integrable estimate on a plateau where \(a=1\) and the equation is ordinary normalized Ricci flow. A transition-inclusive weighted version for \(a|E|\), or an equivalent local-flow theorem, is still needed to make the whole-support Sobolev and cutoff-derivative assumptions self-contained.

---

### 7. Overall scientific assessment

The proposed transition-inclusive \(L^2\) energy architecture is plausible and mathematically well aligned with Wang’s local Ricci-flow curvature formula and the Step 14 defect homogeneity calculation. The terms

\[
\nabla^2a*E*\mathrm{Rm},
\qquad
\nabla a*\nabla E*\mathrm{Rm}
\]
do not present an intrinsic \(L^2\) obstruction when \(a=\chi^2\) and the transition width is comparable to \(r\). The correct object is a combined curvature–defect energy \(R+\kappa P\), not a curvature-only estimate.

What is not supplied by the listed initial data alone is the along-flow geometric control needed to run the absorption at later times: Sobolev constants, cutoff Hessians, and metric equivalence. These would follow from a transition-inclusive weighted pointwise defect estimate together with a \(\chi^2|\mathrm{Rm}|\le C/t\) local-flow regularity theorem, or they can be inserted as explicit hypotheses in the analytic proposition.

So the precise mathematical situation is:

\[
\text{local normalized }L^2\mathrm{Rm}\text{ persistence}
+
\text{global }L^2E\text{ preservation}
\]
can be closed by the displayed coupled inequalities, provided the flow already comes with controlled Sobolev/cutoff geometry on the active region. The remaining scientific substance is an along-flow theorem producing that geometry from the initial relative Sobolev data and the same small local normalized curvature energy.