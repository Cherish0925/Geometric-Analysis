# Step 23: single-support Wang bridge for the normalized cutoff flow

## 1. Main correction and simplification

The Step 22 formulation compressed too much into one “critical lemma.”  It used
an outer dissipation that could not be absorbed by the inner energy, converted a
spacetime cubic estimate into a terminal estimate without the required
fixed-q evolution, and treated the homogeneous defect estimates as automatic.
Those points are separated here.

There is also a useful simplification.  The good-set construction already
provides, after Vitali selection and a further bounded-loss thinning, a family of
**disjoint good macro-supports**.  It is therefore unnecessary to cover the
whole manifold by a maximal micro-net and evolve a graph of curvature energies.
The latter introduces components centered in the uncontrolled bad region and
obscures the original source theorem.

For each selected good center \(p_j\), choose fixed domains and cutoffs at one
Li scale \(r\):

\[
 B_{4r}(p_j)\subset\{\chi_j=1\},\qquad
 \operatorname{supp}\chi_j\Subset B_{5r}(p_j),
\]

and choose \(\eta_j\) with

\[
 \eta_j=1\quad\hbox{on a neighborhood of }\operatorname{supp}\chi_j,
 \qquad \operatorname{supp}\eta_j\Subset U_j\subset B_{6r}(p_j).
\]

The thinning can be made so that the \(U_j\) are disjoint while the union of
the inner balls still has a fixed positive volume proportion.  Put

\[
 a=\sum_j\chi_j^2.
\]

On \(U_j\), \(a=\chi_j^2\).  Where \(d\eta_j\ne0\), one has \(a=da=0\), so
the auxiliary cutoff introduces no parabolic localization term.  The initial
maximal-function bound at \(p_j\) controls the whole \(U_j\):

\[
 \fint_{U_j}F(0)^2\le C K_0,
 \qquad F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

This is the exact geometry needed by Yang's one-support argument.  The
unweighted Hölder factor is controlled by the same component energy, while the
Sobolev test function retains \(\chi_j\) and hence the same component
dissipation.  There is neither outer dissipation nor neighbor dissipation.

## 2. Weak tensor inequality with no cutoff Hessian assumption

Consider

\[
 \partial_tg=-2aE,\qquad E=\operatorname{Ric}+g.
\tag{2.1}
\]

For a metric variation \(h=-2aE\), the curvature variation has the universal
contraction structure

\[
 \partial_t\operatorname{Rm}
 =a\Delta\operatorname{Rm}
  +a(\operatorname{Rm}*\operatorname{Rm}+\operatorname{Rm})
  +da*\nabla E+(\nabla^2a)*E.
\tag{2.2}
\]

Here and below \(*\) denotes a fixed dimension-dependent linear combination of
complete contractions.  Formula (2.2) follows either directly from the general
curvature variation or by adding the conformal variation \(-2ag\) to Wang's
formula for \(-2a\operatorname{Ric}\).  It is important to keep the full
velocity \(-2aE\): then

\[
 |E|\le C F,\qquad |\nabla E|\le C|\nabla\operatorname{Rm}|,
\tag{2.3}
\]

and every Hessian-\(a\) term contains \(E\).  In particular, \(E=0\) makes the
whole variation vanish, including in the transition annulus.

For \(q=2,3\), define on one component

\[
 H_{q,j}=\int\eta_j^2a^{q-2}F^q\,d\mu,
\qquad
 D_{q,j}=\int\eta_j^2a^{q-1}F^{q-2}
                |\nabla\operatorname{Rm}|^2\,d\mu.
\tag{2.4}
\]

Differentiate \(H_{q,j}\), including inverse-metric and volume variation.  The
principal term supplies \(D_{q,j}\).  A representative Hessian term is

\[
 I_q=\int\eta_j^2a^{q-2}F^{q-2}
       \operatorname{Rm}*(\nabla^2a)*E.
\]

Integrating it once by parts, using (2.3), and retaining the full tensor
dissipation gives

\[
 |I_q|\le \varepsilon D_{q,j}
 +C_{q,\varepsilon}\int\eta_j^2a^{q-3}|da|^2F^q.
\tag{2.5}
\]

No derivative lands on \(\eta_j\) in the active region, because
\(\eta_j\equiv1\) near \(\operatorname{supp}a\).  The direct
\(da*\nabla E\) terms obey the same estimate.  Since \(a=\chi_j^2\),

\[
 a^{q-3}|da|^2F^q
 =\frac{|da|^2}{a}\,a^{q-2}F^q
 =4|d\chi_j|^2a^{q-2}F^q,
\tag{2.6}
\]

with the continuous extension at \(a=0\).  Thus no negative cutoff power and
no pointwise bound on \(\nabla^2\chi_j\) is used.

The inverse-metric and measure terms satisfy

\[
 |\partial_tg^{-1}|\,|\operatorname{Rm}|^2
 +|\partial_t d\mu|F^2
 \le C aF^3,
\]

and, with the weight in (2.4), contribute at most
\(Ca^{q-1}F^{q+1}\).  After choosing \(\varepsilon\) small, the complete weak
inequality is

\[
 \boxed{
 H_{q,j}'+c_qD_{q,j}
 \le C_qr^{-2}H_{q,j}
   +C_qR_{q,j},
 \qquad
 R_{q,j}=\int\eta_j^2a^{q-1}F^{q+1}.}
\tag{2.7}
\]

This is the integrated statement the smoothing argument needs.  It is a
standard universal-constant tensor estimate, not a pointwise curvature
inequality.  The derivation deliberately avoids evolving cutoff Hessians.

## 3. Matched \(q=2\) absorption on one good support

Let \(\mathsf S_j\) denote the coefficient in the relative Sobolev inequality

\[
 \|u\|_4^2\le \mathsf S_j
 \left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right),
 \qquad u\in C_c^\infty(U_j).
\tag{3.1}
\]

Under the provisional bilipschitz interval, the same inequality holds with a
fixed multiple of its initial coefficient.  Define

\[
 \gamma_j(t)=\mathsf S_j\|F(t)\|_{L^2(U_j)}.
\tag{3.2}
\]

At \(q=2\), \(H_{2,j}=\int\eta_j^2F^2\),
\(R_{2,j}=H_{3,j}=\int aF^3\), and the matched Sobolev variable is

\[
 v_2=\chi_jF.
\]

Because \(\eta_j=1\) on \(\operatorname{supp}\chi_j\),

\[
 \begin{aligned}
 H_{3,j}
 &=\int_{U_j}Fv_2^2
 \le\|F\|_{L^2(U_j)}\|v_2\|_4^2\\
 &\le C\gamma_j(t)
 \left(D_{2,j}+r^{-2}H_{2,j}\right).
 \end{aligned}
\tag{3.3}
\]

The gradient term in (3.3) is exactly \(D_{2,j}\):

\[
 |\nabla(\chi_jF)|^2
 \le2a|\nabla F|^2+2|d\chi_j|^2F^2.
\]

If \(C\gamma_j(t)<c_2/2\), (2.7) gives

\[
 H_{2,j}'+\frac{c_2}{2}D_{2,j}
 \le Cr^{-2}H_{2,j}.
\tag{3.4}
\]

Consequently, for \(0<t\le\theta r^2\),

\[
 H_{2,j}(t)\le e^{C\theta}H_{2,j}(0),
\qquad
 \int_0^tD_{2,j}(s)\,ds\le C H_{2,j}(0),
\tag{3.5}
\]

and (3.3) yields the spacetime cubic estimate

\[
 \int_0^tH_{3,j}(s)\,ds
 \le C\gamma_{j,*}H_{2,j}(0).
\tag{3.6}
\]

At the initial slice, relative Sobolev and the centered maximal bound give

\[
 \mathsf S_j\lesssim r^2\operatorname{Vol}(U_j)^{-1/2},
\qquad
 \|F(0)\|_{2,U_j}\lesssim\sqrt{K_0\operatorname{Vol}(U_j)},
\]

hence

\[
 \gamma_j(0)\lesssim r^2\sqrt{K_0},
\tag{3.7}
\]

independently of collapse.  Choosing the physical radius once so that (3.7)
is below the absorption threshold, (3.5) self-improves \(\gamma_j(t)\) on the
provisional bilipschitz interval.

## 4. The fixed \(q=3\) equation prevents terminal spikes

A spacetime estimate alone gives only a good time slice.  The endpoint follows
from the separate \(q=3\) inequality.

Now

\[
 H_{3,j}=\int aF^3,
 \qquad R_{3,j}=\int a^2F^4,
 \qquad v_3=aF^{3/2}.
\]

The same unweighted coefficient \(\|F\|_{L^2(U_j)}\) gives

\[
 R_{3,j}=\int Fv_3^2
 \le C\gamma_j(t)
 \left(D_{3,j}+r^{-2}H_{3,j}\right),
\tag{4.1}
\]

because

\[
 |\nabla(aF^{3/2})|^2
 \le C a^2F|\nabla F|^2+C|da|^2F^3
 \le C D_{3,j}+Cr^{-2}H_{3,j}.
\]

After absorption,

\[
 H_{3,j}'\le Cr^{-2}H_{3,j}.
\tag{4.2}
\]

Fix \(0<t\le\theta r^2\).  By (3.6), some
\(s\in[t/4,t/2]\) satisfies

\[
 H_{3,j}(s)\le\frac4t\int_0^{t/2}H_{3,j}(\tau)\,d\tau.
\]

Propagating this slice to \(t\) with (4.2) gives

\[
 \boxed{
 H_{3,j}(t)
 \le \frac{C\gamma_{j,*}H_{2,j}(0)}{t}.}
\tag{4.3}
\]

Since \(H_{2,j}(0)\le\gamma_j(0)^2/\mathsf S_j^2\), this is equivalently

\[
 \boxed{
 \mathsf S_j^2H_{3,j}(t)
 \le\frac{C\gamma_{j,*}^3}{t}.}
\tag{4.4}
\]

Thus (4.4) is not a mean-value assertion: it is the combination of a genuine
good slice with the fixed-\(q=3\) differential inequality.  Narrow terminal
time spikes are excluded by (4.2).

## 5. The homogeneous defect estimates remain separate—and simplify too

### 5.1 Global unweighted \(Q\)

Let

\[
 Q(t)=\int_M|E|^2\,d\mu_t.
\]

The exact integrated identity from Step 14, now with no localization cutoff,
gives

\[
 Q'+c\int_Ma|\nabla E|^2
 \le C\int_M\left(\frac{|da|^2}{a}+a\right)|E|^2
    +C\int_Ma|\operatorname{Rm}|\,|E|^2.
\tag{5.1}
\]

There is no curvature-only source.  Because the active supports are disjoint,
the last term is absorbed component by component:

\[
 \begin{aligned}
 \int_{U_j}\chi_j^2|\operatorname{Rm}|\,|E|^2
 &\le\|\operatorname{Rm}\|_{2,U_j}\|\chi_jE\|_4^2\\
 &\le C\gamma_j(t)
 \left(\int_{U_j}a|\nabla E|^2+r^{-2}\int_{U_j}|E|^2\right).
 \end{aligned}
\tag{5.2}
\]

Summing (5.2), absorbing the gradient terms, and using
\(|da|^2/a\le Cr^{-2}\) yields

\[
 \boxed{Q'(t)\le Cr^{-2}Q(t),\qquad
 Q(t)\le e^{C\theta}Q(0).}
\tag{5.3}
\]

This directly supplies the unweighted defect amplification required by the
\(7/24\) calibration inequality.  A graph of local \(Q_\alpha\) is not needed
for the disjoint-support flow.

### 5.2 Fixed \(J_6\) from time zero

For \(m\ge2\), set on one support

\[
 J_{m,j}=\int\eta_j^2a^{m-2}|E|^m,
 \qquad z_m=a^{(m-1)/2}|E|^{m/2}.
\]

The scalar \(|E|^2\) equation is homogeneous and contains the curvature
potential but no cubic defect source.  Tensor testing before scalarization,
together with the same Hessian-\(a\) integration, gives

\[
 J_{m,j}'+c_mX_{m,j}
 \le Cr^{-2}J_{m,j}
 +C\int_{U_j}Fz_m^2,
\tag{5.4}
\]

where \(X_{m,j}\) is the gradient dissipation generated by \(z_m\).  The
critical absorption is again matched:

\[
 \int Fz_m^2
 \le C\gamma_j(t)(X_{m,j}+r^{-2}J_{m,j}).
\tag{5.5}
\]

For the fixed base exponent \(m=6\), (5.4)--(5.5) imply

\[
 \boxed{J_{6,j}(t)\le e^{C\theta}J_{6,j}(0).}
\tag{5.6}
\]

Since the initial pointwise pinching gives
\(J_{6,j}(0)\le\delta^6\operatorname{Vol}(U_j)\), the \(\delta^6\) factor is
preserved before any positive-time iteration.  The nonintegrable
\(H_3(t)\sim t^{-1}\) coefficient is never integrated from zero.

## 6. Exact-model and scaling checks

An exact negative Einstein metric has \(E=0\), so the total velocity in (2.1)
vanishes.  Therefore every \(H_{q,j}\) is time-independent.  In general,
however,

\[
 H_{3,j}=\int aF^3>0
\]

and \(F\) need not be spatially constant (Taub--NUT--AdS is a nonconstant
Einstein example).  Stationarity checks cancellation of the full tensor
variation; it does not make the curvature potential disappear.

For \(a=1\), constant-curvature homothetic solutions give an independent sign
check.  If \(g(t)=c(t)g_0\), \(\sec(g_0)=k_0\), and \(n=4\), then

\[
 c'=-2(c+3k_0),\qquad
 \frac d{dt}\log|\operatorname{Rm}|^2=4\left(1+\frac{3k_0}{c}\right),
 \qquad
 \frac d{dt}\log d\mu=-4\left(1+\frac{3k_0}{c}\right).
\]

The Einstein case \(k_0=-1/3,c=1\) is stationary.  These signs agree with the
inverse-metric and measure terms used above.

The reproducible algebra and scale checks are in
`workspace/scripts/verify_step23_component_wang_bridge.py`; the script ran with
exit code 0.

## 7. What this step establishes and what still requires development

The following analytic pieces now have a coherent proof on the provisional
bilipschitz/Sobolev interval:

1. the integrated \(q=2,3\) curvature inequality (2.7), with Hessian-\(a\)
   removed by integration by parts and full tensor dissipation retained;
2. componentwise critical-energy persistence and spacetime \(H_3\);
3. the terminal estimate (4.4) from a good slice plus the fixed \(q=3\)
   evolution;
4. global unweighted \(Q\) amplification (5.3), with no curvature-only source;
5. fixed \(J_6\) persistence (5.6), preserving the initial \(\delta^6\) factor.

The remaining smoothing work is no longer a single tensor calculation.  It
consists of:

- implementing the positive-time subcritical iteration from (4.4) to a uniform
  \(|a\operatorname{Rm}|\) bound on each support;
- implementing the parallel defect iteration from (5.6) and (4.4) to an
  integrable \(|aE|\) bound, thereby improving metric and Sobolev comparability;
- adapting Yang--Wang smooth continuation to the normalized lower-order term;
- checking the support/plateau thinning and relative Sobolev constants with the
  enlarged \(U_j\) radii in the actual first-exit construction.

Once those are supplied, positive-time interior normalized Ricci-flow estimates
on \(B_{4r}(p_j)\) give uniform derivatives on smaller plateaux, and the
exponential-pullback/joint-monopole argument can reach the forbidden calibrated
Einstein germ.  This remains a result for the critical four-dimensional
negative Ishida--LeBrun laboratory, not the full dimension-by-dimension Yau 26
statement.
