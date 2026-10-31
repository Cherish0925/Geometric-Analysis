# Tensor-energy derivation for the Step 24 buffered cutoff flow

## 1. Scope and conclusion

Consider a smooth solution on a closed four-manifold of

\[
\partial_t g=h=-2aE,\qquad E=\operatorname{Ric}+g,\qquad a=\chi^2,
\]

where \(\chi,\eta\) are fixed (time-independent) smooth scalar functions.  Assume

\[
0\leq \chi,\eta\leq 1,\qquad
\eta\equiv1\ \text{on a neighbourhood of }\operatorname{supp}\chi,
\qquad \operatorname{supp}d\eta\subset\{a=0\}^{\circ}.
\tag{1.1}
\]

Thus \(a=d a=0\) on a neighbourhood of \(\operatorname{supp}d\eta\).  All
norms, covariant derivatives, contractions, and measures below are those of
\(g(t)\).  Put

\[
F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

At every time at which the flow is smooth, the three proposed differential
inequalities are correct, with constants uniform on an interval provided the
current-metric bounds

\[
|d\chi|_{g(t)}\le C_\chi r^{-1},\qquad 0<r\le1
\tag{1.2}
\]

hold there.  No pointwise curvature bound is used in their derivation.  In
particular,

\[
\begin{aligned}
H_2'+cD_2&\le C\int\eta^2aF^3+Cr^{-2}H_2,\\
Y'+cD_3&\le Cr^{-2}Y+C\int\eta^2a^2F^4,\\
Q'+cX&\le Cr^{-2}Q+C\int\eta^2aF|E|^2,
\end{aligned}
\tag{1.3}
\]

with

\[
\begin{gathered}
H_2=\int\eta^2F^2,\quad
D_2=\int\eta^2a|\nabla\operatorname{Rm}|^2,\\
Y=\int\eta^2aF^3,\quad
D_3=\int\eta^2a^2F|\nabla\operatorname{Rm}|^2,\\
Q=\int\eta^2|E|^2,\quad
X=\int\eta^2a|\nabla E|^2.
\end{gathered}
\]

The constants depend only on the dimension and the cutoff-gradient constant in
(1.2) (and on a fixed metric-equivalence factor if (1.2) is transferred from
time zero).  A bound for \(\nabla^2\chi\) is not needed for these weak energy
inequalities: all Hessian-\(a\) terms are integrated by parts once.

The separate Sobolev absorptions proposed in Step 24 also have the correct
weights.  What is *not* supplied by (1.3) is uniform existence, metric
comparability, or persistence of the Sobolev inequality.  Those require a
bootstrap or an independent local-flow theorem, as recorded in Section 8.

## 2. Exact curvature variation with the cutoff terms exposed

### 2.1 A convention-independent starting point

Fix the convention

\[
(\nabla_i\nabla_j-\nabla_j\nabla_i)X^\ell
=R^\ell{}_{kij}X^k.
\]

For an arbitrary variation \(h=\partial_tg\), define

\[
C^\ell{}_{jk}:=\partial_t\Gamma^\ell{}_{jk}
=\frac12g^{\ell m}
(\nabla_jh_{km}+\nabla_kh_{jm}-\nabla_mh_{jk}).
\tag{2.1}
\]

Then the exact tensor identity is

\[
\partial_tR^\ell{}_{kij}=\nabla_iC^\ell{}_{jk}-\nabla_jC^\ell{}_{ik}.
\tag{2.2}
\]

This mixed-index form avoids all ambiguity about the extra algebraic term that
appears when an index is lowered by an evolving metric.

For \(h=-2aE\), set

\[
S_{jkm}:=\nabla_jE_{km}+\nabla_kE_{jm}-\nabla_mE_{jk}.
\]

Equation (2.1) becomes

\[
C^\ell{}_{jk}=-g^{\ell m}
\{aS_{jkm}+a_jE_{km}+a_kE_{jm}-a_mE_{jk}\}.
\tag{2.3}
\]

Expanding (2.2), using \(\nabla E=\nabla\operatorname{Ric}\), and applying the
twice-contracted Bianchi/commutator identity to the constant-\(a\) part gives

\[
\boxed{
\partial_tR^\ell{}_{kij}
=a(\Delta R^\ell{}_{kij}+\mathcal Q^\ell{}_{kij}(\operatorname{Rm}))
+\mathcal G^\ell{}_{kij}+\mathcal H^\ell{}_{kij}.}
\tag{2.4}
\]

Here \(\mathcal Q\) is the usual quadratic Ricci-flow curvature polynomial,
\(|\mathcal Q|\le C_n|\operatorname{Rm}|^2\), and the cutoff terms are exactly

\[
\begin{aligned}
\mathcal G^\ell{}_{kij}=-g^{\ell m}\{\,&
a_i(\nabla_kE_{jm}-\nabla_mE_{jk})
-a_j(\nabla_kE_{im}-\nabla_mE_{ik})\\
&+a_k(\nabla_iE_{jm}-\nabla_jE_{im})
-a_m(\nabla_iE_{jk}-\nabla_jE_{ik})\},
\end{aligned}
\tag{2.5}
\]

and

\[
\boxed{
\mathcal H^\ell{}_{kij}
=-g^{\ell m}
(a_{ik}E_{jm}-a_{im}E_{jk}-a_{jk}E_{im}+a_{jm}E_{ik}).}
\tag{2.6}
\]

Thus

\[
|\mathcal G|\le C_n|da|\,|\nabla E|,
\qquad
|\mathcal H|\le C_n|\nabla^2a|\,|E|.
\tag{2.7}
\]

The normalization term does not appear separately in (2.4): a constant
variation \(-2g\) does not change the Levi-Civita connection or the mixed
curvature tensor.  On lowering the first index,

\[
\partial_tR_{\ell kij}
=h_{\ell p}R^p{}_{kij}+g_{\ell p}\partial_tR^p{}_{kij},
\tag{2.8}
\]

so an additional algebraic term \(-2aE_{\ell p}R^p{}_{kij}\) appears.  It is
bounded by \(CaF^2\).

For comparison, in the standard all-covariant Hamilton convention, define

\[
B_{ijkl}=g^{pr}g^{qs}R_{pijq}R_{rkls}.
\]

The constant-coefficient normalized part in (2.8) can be written

\[
\begin{aligned}
\mathcal N_{ijkl}={}&\Delta R_{ijkl}
+2(B_{ijkl}-B_{ijlk}-B_{iljk}+B_{ikjl})\\
&-g^{pq}(R_{pjkl}R_{qi}+R_{ipkl}R_{qj}
+R_{ijpl}R_{qk}+R_{ijkp}R_{ql})-2R_{ijkl}.
\end{aligned}
\tag{2.9}
\]

Changing the sign convention for \(R\) changes the corresponding displayed
signs but not (2.1)--(2.3), once the convention is changed consistently, nor any
energy estimate below.  Equations (2.4)--(2.8) show the required separation

\[
\partial_t\operatorname{Rm}
=a\Delta\operatorname{Rm}+a\,\mathcal A(\operatorname{Rm})
+(da)*\nabla E+(\nabla^2a)*E,
\quad |\mathcal A|\le C(F^2+F).
\tag{2.10}
\]

Most importantly, before commuting derivatives the whole right side is the
linearization applied to \(aE\).  Hence no bare \((\nabla^2a)*g\) source exists.
Splitting \(-2aE=-2a\operatorname{Ric}-2ag\) produces two Hessian terms that
must be recombined into \((\nabla^2a)*E\).

### 2.2 Contraction identities used in curvature energy

At every smooth time,

\[
E_{ij}=g^{k\ell}R_{kilj}+g_{ij},\qquad
\nabla_pE_{ij}=g^{k\ell}\nabla_pR_{kilj}.
\tag{2.11}
\]

Consequently

\[
|E|\le C_nF,\qquad |\nabla E|\le C_n|\nabla\operatorname{Rm}|,
\qquad |\nabla F|\le|\nabla\operatorname{Rm}|.
\tag{2.12}
\]

These are algebraic contractions, not propagated pointwise-curvature or
pointwise-defect hypotheses.

## 3. Common energy bookkeeping

The remaining exact variation identities are

\[
\partial_td\mu=\frac12\operatorname{tr}_g(h)d\mu
=-a\tau\,d\mu,\qquad \tau=\operatorname{tr}E,
\tag{3.1}
\]

and, for an all-covariant four-tensor \(R\),

\[
\partial_t|R|^2
=2\langle\partial_tR,R\rangle
+2a\sum_{\alpha=1}^{4}(E\text{ contracted into the }\alpha
\text{th slot of }R)\cdot R.
\tag{3.2}
\]

The last sum is bounded by \(Ca|E||R|^2\le CaF^3\).  For \(F^q\), it
therefore contributes at most \(CaF^{q+1}\).  The measure term has the same
bound because \(|\tau|\le\sqrt n|E|\le CF\).

The principal term has a favourable tensor-gradient part.  If \(w\ge0\) is a
fixed scalar weight, then

\[
\begin{aligned}
q\int waF^{q-2}\langle R,\Delta R\rangle
={}&-q\int waF^{q-2}|\nabla R|^2\\
&-q(q-2)\int waF^{q-2}|\nabla F|^2\\
&-q\int \langle d(wa),F^{q-2}\langle R,\nabla R\rangle\rangle.
\end{aligned}
\tag{3.3}
\]

Here \(F\nabla F=\langle R,\nabla R\rangle\).  The last line is estimated by
Young's inequality against the first line.

For a representative Hessian-cutoff term, one integration by parts gives

\[
\begin{aligned}
\int wF^{q-2}R*(\nabla^2a)*E
=-\int da*\nabla(wF^{q-2}R*E).
\end{aligned}
\tag{3.4}
\]

By (2.12), all terms where the derivative hits \(F,R,E\) are bounded by

\[
C_q\int w|da|F^{q-1}|\nabla R|
\le \varepsilon\int waF^{q-2}|\nabla R|^2
+C_{q,\varepsilon}\int w\frac{|da|^2}{a}F^q.
\tag{3.5}
\]

The quotient is interpreted as zero on \(\{a=0\}\).  This is legitimate for
\(a=\chi^2\), since

\[
da=2\chi\,d\chi,\qquad
\frac{|da|^2}{a}=4|d\chi|^2
\quad\text{on }\{a>0\},
\tag{3.6}
\]

with a continuous bounded extension for the purposes of the estimate.  Terms
where the derivative in (3.4) hits \(w\) are treated separately below.  The
direct \((da)*\nabla E\) term satisfies precisely (3.5).

## 4. The \(q=2\) curvature energy

Take \(q=2\) and \(w=\eta^2\).  In (3.3), derivatives of \(\eta\) occur only
multiplied by \(a\), and in (3.4) only multiplied by \(da\).  Both vanish by
(1.1).  Thus, after absorbing (3.5), the diffusion and cutoff terms give

\[
-c\int\eta^2a|\nabla R|^2
+C\int\eta^2\frac{|da|^2}{a}F^2.
\tag{4.1}
\]

All algebraic curvature, metric-norm, and measure variations are bounded by

\[
C\int\eta^2aF^3,
\tag{4.2}
\]

using \(F\ge1\).  Notice that differentiating the constant \(1\) in
\(F^2=1+|R|^2\) produces nothing, while its measure variation is already
covered by (4.2).  Equations (3.6) and (1.2) now yield

\[
\boxed{
H_2'+cD_2
\le C\int\eta^2aF^3+Cr^{-2}H_2.}
\tag{4.3}
\]

There is no missing \(\nabla^2a\) term and no \(d\eta\) localization term.
Without the strict buffer (1.1), the usual extra term
\(C\int a|d\eta|^2F^2\) would be present.

The proposed critical absorption is also correctly weighted.  Since
\(\eta=1\) on \(\operatorname{supp}\chi\),

\[
\int\eta^2aF^3=\int F(\chi F)^2
\le \|F\|_{L^2(\operatorname{supp}\chi)}\|\chi F\|_4^2,
\tag{4.4}
\]

and

\[
\int|\nabla(\chi F)|^2
\le 2D_2+Cr^{-2}H_2.
\tag{4.5}
\]

Thus a current-time Sobolev inequality gives

\[
\int\eta^2aF^3
\le C\beta_a(t)(D_2+r^{-2}H_2),
\quad
\beta_a(t)=A(t)^2\|F\|_{L^2(\operatorname{supp}\chi,g(t))}.
\tag{4.6}
\]

Smallness of \(\beta_a(t)\), not a pointwise curvature bound, absorbs the
reaction.

## 5. The weighted \(q=3\) curvature energy

Now take \(q=3\) and \(w=\eta^2a\).  The principal coefficient in (3.3) is
\(wa=\eta^2a^2\), so the dissipation is exactly

\[
D_3=\int\eta^2a^2F|\nabla R|^2.
\tag{5.1}
\]

Differentiating \(wa=\eta^2a^2\) gives \(2\eta^2a\,da\); the \(d\eta\) part
again vanishes.  Young's inequality leaves \(|da|^2F^3\).  In (3.4), the
derivative of the testing weight \(w=\eta^2a\) also leaves
\(\eta^2|da|^2F^3\).  All other Hessian and gradient-cutoff terms satisfy

\[
\begin{aligned}
C\int\eta^2a|da|F^2|\nabla R|
&\le \varepsilon D_3+C_\varepsilon\int\eta^2|da|^2F^3.
\end{aligned}
\tag{5.2}
\]

Because \(|da|^2=4a|d\chi|^2\), every cutoff remainder is bounded by
\(Cr^{-2}Y\).  Every algebraic, norm, and volume reaction has both the testing
factor \(a\) and the equation factor \(a\), and is bounded by

\[
C\int\eta^2a^2F^4.
\tag{5.3}
\]

Therefore

\[
\boxed{
Y'+cD_3\le Cr^{-2}Y+C I_4,
\qquad I_4=\int\eta^2a^2F^4.}
\tag{5.4}
\]

Thus \(I_4\), rather than \(\int aF^4\), is the correct reaction.  Its proposed
Sobolev absorption uses

\[
u=aF^{3/2},\qquad I_4=\int F u^2,
\tag{5.5}
\]

and

\[
\int|\nabla u|^2
\le CD_3+C\int|da|^2F^3
\le C(D_3+r^{-2}Y).
\tag{5.6}
\]

Consequently

\[
I_4\le C\beta_a(t)(D_3+r^{-2}Y).
\tag{5.7}
\]

This confirms both the dissipation weight \(a^2F\) and the reaction weight
\(a^2F^4\).

## 6. Exact evolution of the Einstein defect

Use the Lichnerowicz Laplacian convention

\[
(\Delta_LE)_{ij}=\Delta E_{ij}+2R_{ikjl}E_{kl}
-R_i{}^kE_{kj}-R_j{}^kE_{ki}.
\tag{6.1}
\]

Let \(\tau=\operatorname{tr}E\).  Direct expansion of the Ricci variation,
followed by \(\operatorname{div}E=\tfrac12d\tau\), gives the exact equation

\[
\boxed{
\partial_tE_{ij}=a(\Delta_LE_{ij}-2E_{ij})+\mathcal C_a(E)_{ij},}
\tag{6.2}
\]

where

\[
\begin{aligned}
\mathcal C_a(E)_{ij}={}&(\Delta a)E_{ij}
+2a^k\nabla_kE_{ij}+\tau a_{ij}\\
&+\frac12(a_i\tau_j+a_j\tau_i)
-a_i{}^kE_{kj}-a_j{}^kE_{ki}\\
&-a^k(\nabla_iE_{kj}+\nabla_jE_{ki}).
\end{aligned}
\tag{6.3}
\]

Every term in (6.2)--(6.3) contains \(E\), \(\nabla E\), or a trace thereof.
In particular, there is no independent \((\nabla^2a)*g\) source.  This is also
forced by the geometric fixed-point check: if \(E=0\), then \(h=0\) and the
metric and every tensor constructed from it are stationary.

Including the variation of the norm, the constant-\(a\) cubic terms cancel and
one obtains the exact pointwise identity

\[
(\partial_t-a\Delta)|E|^2
=-2a|\nabla E|^2+4aR_{ikjl}E_{ij}E_{kl}
+2\langle E,\mathcal C_a(E)\rangle.
\tag{6.4}
\]

There is no separate \(-4a|E|^2\) in (6.4): it cancels against the Ricci terms
in \(\Delta_L\) after \(\operatorname{Ric}=E-g\), together with the inverse
metric variation.  This cancellation is harmless for the desired estimate but
is important in any claim of strict damping.

The Hessian-\(a\) cancellation can be displayed exactly.  For an arbitrary
fixed scalar test function \(q\), integrate the Hessian terms in
\(2q\langle E,\mathcal C_a(E)\rangle\) once and use
\(\nabla^iE_{ij}=\tfrac12\tau_j\).  The result is

\[
\begin{aligned}
\int2q\langle E,\mathcal C_a(E)\rangle
=\int\{&-2|E|^2\langle da,dq\rangle
-2\tau E(dq,da)+4E^2(dq,da)\\
&+q[-\tau\langle da,d\tau\rangle+2E(da,d\tau)]\}.
\end{aligned}
\tag{6.5}
\]

This identity has no Hessian of \(a\) and is manifestly at least quadratic
under \(E\mapsto\varepsilon E\), \(\nabla E\mapsto\varepsilon\nabla E\).

## 7. Testing the defect equation

Set \(q=\eta^2\).  Integrating the \(a\Delta|E|^2\) term in (6.4) produces

\[
-\int a\langle dq,d|E|^2\rangle
-\int q\langle da,d|E|^2\rangle.
\tag{7.1}
\]

The first term vanishes by (1.1).  All terms containing \(dq\) in (6.5) also
vanish because \(da=0\) on \(\operatorname{supp}dq\).  The remaining terms in
(7.1) and (6.5) obey

\[
C\int q|da|\,|E|\,|\nabla E|
\le \varepsilon X+C_\varepsilon
\int q\frac{|da|^2}{a}|E|^2.
\tag{7.2}
\]

The curvature term in (6.4) is bounded by \(Ca|\operatorname{Rm}||E|^2\),
and the volume variation from (3.1) is bounded by
\(Ca|E|^3\le CaF|E|^2\).  Therefore (3.6), (1.2), and absorption of
\(\varepsilon X\) give

\[
\boxed{
Q'+cX\le Cr^{-2}Q+C\int\eta^2aF|E|^2.}
\tag{7.3}
\]

This is genuinely triangular: its right side vanishes with \(E\).  The
curvature occurs only as a potential multiplying \(|E|^2\).

The proposed critical absorption is

\[
\begin{aligned}
\int\eta^2aF|E|^2
&=\int F|\chi E|^2\\
&\le\|F\|_{L^2(\operatorname{supp}\chi)}\|\chi E\|_4^2\\
&\le C\beta_a(t)(X+r^{-2}Q),
\end{aligned}
\tag{7.4}
\]

where (1.1) was used in the equality.  Thus small current-time \(\beta_a\)
absorbs the potential without any additive curvature dissipation.

## 8. Assumptions needed beyond formal tensor calculus

The inequalities (4.3), (5.4), and (7.3) are slice-wise weak energy estimates
for an already smooth solution.  Turning them into a uniform theorem on
\([0,\theta r^2]\) requires the following additional inputs.

1. **Existence.** One needs a smooth solution of the degenerate compactly
   supported cutoff flow on the claimed interval, or an approximation theorem
   whose estimates survive the limit.  The energy calculation does not prove
   this.

2. **Fixed cutoffs and present-metric derivative bounds.** The scalar functions
   \(\chi,\eta\) are fixed in time.  If their gradient bounds are known only for
   \(g_0\), a uniform bilipschitz comparison
   \(\Lambda^{-1}g_0\le g(t)\le\Lambda g_0\) gives the corresponding bounds for
   \(g(t)\).  No Hessian bound is needed after weak integration by parts, though
   smooth approximation requires enough regularity to justify that step.

3. **Sobolev persistence.** If

   \[
   \|u\|_{L^4(g_0)}^2\le A_0^2
   (\|\nabla u\|_{L^2(g_0)}^2+r^{-2}\|u\|_{L^2(g_0)}^2)
   \tag{8.1}
   \]

   on the fixed auxiliary support, the same inequality for \(g(t)\), with a
   constant depending only on \(\Lambda\) and dimension, follows from
   bilipschitz metric and measure comparison.  A Ricci lower bound at time zero
   alone does not propagate this Sobolev constant under the cutoff flow.

4. **How metric comparison is obtained.** From the evolution equation,

   \[
   e^{-2\int_0^t\|aE(s)\|_\infty ds}g_0
   \le g(t)\le
   e^{2\int_0^t\|aE(s)\|_\infty ds}g_0.
   \tag{8.2}
   \]

   Therefore an integrable weighted pointwise defect bound, or an independent
   local-flow metric-equivalence estimate, is needed.  The three energy
   inequalities alone do not imply (8.2) with a uniform constant.  A rigorous
   closure should use a first-exit bootstrap carrying metric equivalence,
   Sobolev control, cutoff-gradient control, and small \(\beta_a(t)\)
   simultaneously.

5. **Critical smallness is current-time smallness.** The absorptions
   (4.6), (5.7), and (7.4) use
   \(A(t)^2\|F(t)\|_{L^2(\operatorname{supp}\chi)}\ll1\).  Initial maximal-
   function smallness starts the bootstrap, while (4.3)--(4.6) can propagate it
   if the Sobolev and metric constants are already in the first-exit package.
   The stationary collar should be included explicitly when comparing the
   full auxiliary-support \(L^2\) norm with \(H_2\).

6. **No pointwise curvature assumption.** None is required for (1.3) or the
   three critical Sobolev absorptions.  A later \(|a\operatorname{Rm}|\lesssim
   t^{-1}\) estimate is an output of a further finite-exponent/mean-value
   argument, not an admissible input here.

7. **Scale convention.** Writing all harmless lower-order terms as
   \(Cr^{-2}\) assumes \(r\le1\).  Otherwise the displayed coefficient should
   be \(C(1+r^{-2})\).

## 9. Exact verdict and next tasks

The Step 24 tensor weights are supported without repair:

* the \(q=2\) reaction is \(aF^3\) and its dissipation is
  \(a|\nabla\operatorname{Rm}|^2\);
* the weighted \(q=3\) reaction is \(a^2F^4\) and its dissipation is
  \(a^2F|\nabla\operatorname{Rm}|^2\);
* the defect equation has no curvature-only or \((\nabla^2a)*g\) source, and
  the only curvature contribution to its energy is the triangular potential
  \(aF|E|^2\).

The only repairs to the surrounding narrative are logical rather than tensorial:
the constants \(A(t)\), \(|d\chi|_{g(t)}\), and metric comparison cannot be
declared persistent from the initial assumptions alone.  They must be included
in, and then improved by, a first-exit/local-existence argument.  The next
mathematical tasks are therefore:

1. formulate the cutoff-flow existence/approximation theorem on the fixed
   support with a quantitative first-exit interval;
2. close the simultaneous bootstrap for metric equivalence, the Sobolev
   constant, and \(\beta_a(t)\);
3. use the verified weighted \(q=3\) estimate to start the positive-time
   supercritical mean-value/Moser stage, without assuming pointwise curvature;
4. prove the integrable weighted pointwise defect estimate needed to improve
   the metric-equivalence part of the bootstrap.

The symbolic contraction and monomial checks used in this memo are in
`Sessions/S0910A01/workspace/codex_loop/work/verify_tensor_energy_ledger.py`.
