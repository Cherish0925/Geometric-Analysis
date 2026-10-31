# Step 30: weighted Moser repair, shifted-curvature scope, and Ishida--LeBrun family bookkeeping

Session: S0910A01. Agent3 / Actuator. Phase: Execute.

## 0. Purpose

This note corrects the Step 29 simultaneous-support theorem before it is used
as a guide for later proof work.  The corrections are not cosmetic:

1. the half-power weight gap in the direct comparison
   \(\|z_p\|_3^3\) versus \(H_{3p/2}\) does **not** kill the weighted hierarchy;
   it is repaired by a mixed Hölder--Sobolev time-slice estimate;
2. the proposed ordinary unweighted Moser iteration on
   \(U=a(\operatorname{Rm}+G)\) is not justified as a first weighted-curvature
   bound because the operator is still \(a\Delta\);
3. the family bookkeeping needs only an \(O(A)\) Euler bound and a positive
   lower bound for \(\operatorname{Vol}/A\), not the false claim
   \(\chi(M)=A+O(1)\) or the numerical constant \(K_0\to9\);
4. the difficult regime is \(\sigma_i/A_i\to0\), including sequences with all
   \(\sigma_i>0\), not just the exact hypersurface \(\sigma=0\);
5. support selection must be stated with macro-disjoint buffers and zero-extended
   terminal eigenline densities.

The verification script is
`workspace/scripts/step30_weighted_moser_family_repair.py`.

---

## 1. Corrected weighted Moser bridge

On one buffered active support let

\[
H_p(f,t)=\int \eta^2 a^{p-2}f^p\,d\mu_t,
\qquad
z_p=\eta a^{(p-1)/2}f^{p/2},
\qquad \kappa=\frac32.
\]

The Step 29 objection compared

\[
\|z_p\|_3^3=\int \eta^3 a^{3(p-1)/2}f^{3p/2}
\]

directly to

\[
H_{3p/2}=\int \eta^2 a^{3p/2-2}f^{3p/2}.
\]

The first integrand contains an extra factor \(a^{1/2}\).  Since \(a\le1\),
this gives the wrong direction and direct Sobolev embedding alone cannot bound
\(H_{3p/2}\).  The correct step is to use the time-slice energy \(H_p\) already
available from the power inequality:

\[
\boxed{
H_{3p/2}
 = \int_{\{\eta=1\text{ on the active region}\}}
      (a^{p-2}f^p)^{1/2}\, z_p^2
 \le H_p^{1/2}\,\|z_p\|_4^2 .}
\tag{1.1}
\]

The exponent identity is exact:

\[
\frac{p-2}{2}+(p-1)=\frac{3p}{2}-2.
\]

The auxiliary cutoff \(\eta\) is one on \(\operatorname{supp}\chi\), while
\(a=0\) on \(\operatorname{supp}\nabla\eta\); hence no active transition term is
lost in (1.1).  If a formula is written on the larger \(\eta\)-support, insert a
slightly nested energy cutoff equal to one on the support used for
\(H_{3p/2}\).  The macro-disjoint support construction below is designed so all
such cutoffs fit inside the stationary collar.

By the local Sobolev inequality and the gradient identity for \(z_p\),

\[
\|z_p\|_4^2\le S\left(\|\nabla z_p\|_2^2+r^{-2}\|z_p\|_2^2\right)
\le C p^N S\left(D_p+r^{-2}H_p\right),
\tag{1.2}
\]

where

\[
D_p=\int \eta^2 a^{p-1}f^{p-2}|\nabla f|^2.
\]

Thus on a time interval \(I\),

\[
\boxed{
\int_I H_{3p/2}(s)\,ds
\le C p^N S\,\bigl(\sup_I H_p\bigr)^{1/2}
\int_I \left(D_p+r^{-2}H_p\right)ds .}
\tag{1.3}
\]

This is the missing embedding implication.  It uses the actual power-energy
control of \(H_p\) and \(D_p\), not a standalone comparison between
\(\|z_p\|_3^3\) and the next energy.

---

## 2. Time-cutoff recurrence with polynomial losses

After the three-factor absorption (Step 27), the power inequality has the form

\[
H_p' + c p^{-m}D_p
\le C p^N(r^{-2}+S^2Y(t))H_p + \operatorname{source}_p,
\tag{2.1}
\]

where the exact polynomial powers depend on the tensor-power calculation and
Kato regularization.  On a slab \([t/2,t]\) the q=3 layer is intended to provide

\[
S^2Y(s)\le C\beta^3/s\le C\beta^3/t.
\tag{2.2}
\]

With nested time cutoffs
\(\zeta_k\) supported in \([\tau_k,t]\), equal to one on
\([\tau_{k+1},t]\), and satisfying \(|\zeta_k'|\le C4^k/t\), the energy estimate
has the standard schematic form

\[
\sup_{[\tau_{k+1},t]}H_{p_k}
+\int_{\tau_{k+1}}^tD_{p_k}
\le L_k\int_{\tau_k}^t H_{p_k}(s)\,ds + \text{source},
\tag{2.3}
\]

with

\[
L_k=Cp_k^N4^k(t^{-1}+r^{-2}).
\tag{2.4}
\]

Combining (1.3) and (2.3) gives a valid recurrence

\[
\int_{\tau_{k+1}}^t H_{p_{k+1}}(s)\,ds
\le C p_k^N S\,
       \left(L_k\int_{\tau_k}^tH_{p_k}\right)^{3/2}
\tag{2.5}
\]

(up to the same source terms and harmless changes in \(N\)).  Therefore, for
\(m_k=(\int_{\tau_k}^tH_{p_k})^{1/p_k}\),

\[
m_{k+1}\le (CS)^{1/(\kappa p_k)}L_k^{1/p_k}m_k,
\qquad p_{k+1}=\kappa p_k,
\tag{2.6}
\]

exactly as desired.  The polynomial and \(4^k\) factors are compatible with
Moser because

\[
\sum_k\frac{\log p_k}{p_k}<\infty,
\qquad
\sum_k\frac{k}{p_k}<\infty.
\]

For \(n=4\),

\[
\sum_{k\ge0}\frac1{p_k}=\frac{3}{p_0}=\frac{n+2}{2p_0},
\qquad
\sum_{k\ge0}\frac{1}{\kappa p_k}=\frac{2}{p_0}=\frac{n}{2p_0}.
\tag{2.7}
\]

Thus the time power is \(t^{-3/p_0}\) and the Sobolev power is \(S^{2/p_0}\):

- curvature seed \(p_0=3\): time power \(t^{-1}\), Sobolev power \(S^{2/3}\);
- defect seed \(p_0=6\): time power \(t^{-1/2}\), Sobolev power \(S^{1/3}\).

The expected endpoints remain

\[
\|aF(t)\|_\infty\lesssim \beta/t,
\qquad
\|aE(t)\|_\infty\lesssim \delta(r^2/t)^{1/3},
\tag{2.8}
\]

provided the tensor power inequalities, q=3 potential estimate, and fixed
\(J_6\) propagation are all proved on the same evolving supports.  Equation
(2.8) is therefore a repaired analytic route, not a completed theorem.

---

## 3. True role of shifted curvature \(U=a(\operatorname{Rm}+G)\)

The shifted curvature remains important.  With

\[
G=\frac{g\owedge g}{2(n-1)},\qquad T=\operatorname{Rm}+G,
\qquad U=aT,
\]

we have

\[
\operatorname{Ric}(T)=E,\qquad \operatorname{Ric}(U)=aE,
\qquad \partial_tg=-2\operatorname{Ric}(U).
\]

This identity is valuable for the connection evolution and Wang-type derivative
induction.  It should be retained for smooth continuation **after** a weighted
curvature bound has been obtained.

However, Step 29's ordinary unweighted Moser shortcut is not justified:

1. the operator in the \(U\)-equation is still \(a\Delta\), so testing
   \(|U|^p\) controls only
   \[
   \int a\,|\nabla(|U|^{p/2})|^2,
   \]
   not the unweighted gradient needed by a standard uniformly parabolic Moser
   iteration;
2. if the shifted \(T\)-equation has the quadratic reaction \(aT*T\), then
   multiplying by \(a\) gives
   \[
   a^2T*T=(aT)*(aT)=U*U,
   \]
   not \(aU*U\).  The unweighted reaction is therefore not softened by a spare
   factor of \(a\);
3. continuation estimates that assume \(\sup |a\operatorname{Rm}|<\infty\)
   cannot be used to produce the first such bound.

Thus the current route is: use the repaired weighted hierarchy to try to obtain
\(\|aF\|_\infty\); then use \(U\) to organize connection/derivative estimates and
restart.  Renaming the variable cannot remove the degeneracy of the first
Moser step.

---

## 4. Ishida--LeBrun topology and the mean curvature-energy budget

For the Ishida--LeBrun family

\[
M=(\#_{j=1}^m X_j)\#N,
\qquad m=2\text{ or }3,
\qquad A=\sum_jc_1^2(X_j),
\]

with

\[
D=4m-(2\chi+3\tau)(N),
\qquad \sigma=D-A/3\ge0,
\]

Ishida--LeBrun gives no Einstein metric when \(\sigma\ge0\).  The connected-sum
identity is

\[
(2\chi+3\tau)(M)=A-D=\frac{2A}{3}-\sigma.
\tag{4.1}
\]

For minimal complex surfaces of general type, Noether's formula and inequality
imply

\[
c_2(X_j)\le 5c_1^2(X_j)+36.
\tag{4.2}
\]

Connected sum gives

\[
\chi(M)=\sum_jc_2(X_j)+\chi(N)-2m.
\tag{4.3}
\]

Writing Betti numbers for \(N\), and using the standard Ishida--LeBrun input
\(b_+(N)=0\),

\[
D=4m-(2\chi+3\tau)(N)
=A/3+\sigma
\]

is equivalent to

\[
\chi(N)=A/3+\sigma+6-4m-6b_1(N)
\le A/3+\sigma+6-4m.
\tag{4.4}
\]

Hence

\[
\boxed{\chi(M)\le \frac{16}{3}A+\sigma+30m+6.}
\tag{4.5}
\]

At exact criticality this recovers the Step 18 bound
\(\chi(M)/A\le65/6\) for \(m=2\), \(\le28/3\) for \(m=3\), using
\(A\ge12(m-1)\).  The important point is that this is an \(O(A)\) bound, not
\(\chi(M)=A+O(1)\).  Therefore Step 29's numerical constant \(K_0\to9\) is not
supported and is unnecessary.

With a fixed curvature-norm convention, Chern--Gauss--Bonnet gives a bound of
form

\[
\int_M |\operatorname{Rm}|^2
\le C_1\chi(M)+C_2\operatorname{Vol}+C_3\delta^2\operatorname{Vol},
\tag{4.6}
\]

where the constants depend only on the convention for the full curvature norm.
The route only uses existence of such universal constants.  In a near-pinched
negative sequence, the scalar/Chern--Weil volume estimates give

\[
0<v_-\le \operatorname{Vol}(M,g)/A\le v_+<\infty
\tag{4.7}
\]

in the near-critical regime.  Combining (4.5)--(4.7), and using
\(\sigma/A\to0\) when \(\delta\to0\) (Section 5), gives a uniform mean
curvature-energy budget

\[
K_0=\operatorname{Vol}^{-1}\int |\operatorname{Rm}|^2\le C.
\tag{4.8}
\]

This is sufficient to keep the physical work radius
\(r=cK_0^{-1/4}\) bounded below after choosing a fixed small \(c>0\), while
also making the critical product

\[
\beta=S\|F\|_2\lesssim r^2\sqrt{1+K_0}
\]

small enough for absorption by taking \(c\) small.

The plateau mass also needs the lower volume bound in (4.7).  If coloring and
support selection retain a fixed fraction \(\theta>0\) of the total volume, then

\[
\operatorname{Vol}(P_i)\ge \theta\operatorname{Vol}(M_i,g_i)
\ge \theta v_- A_i.
\tag{4.9}
\]

An upper bound for volume alone would not supply the \(A_i\)-proportional
center-set volume required by the exponential-pullback selection.

---

## 5. Above-critical algebra and the true near-critical regime

The mixed estimate and CGB identity yield, for

\[
R=\frac1{4\pi^2}\int\frac{|\operatorname{Ric}^\circ|^2}{2},
\]

\[
R\ge\sigma.
\tag{5.1}
\]

If \(\|g^{-1}(\operatorname{Ric}+g)\|_{\infty,op}\le\delta\), then
\(|\operatorname{Ric}^\circ|^2\le4\delta^2\), so

\[
\sigma\le R\le \frac{\delta^2}{2\pi^2}\operatorname{Vol}(M,g).
\tag{5.2}
\]

Together with \(\operatorname{Vol}/A\le v_+\), this gives

\[
\frac{\sigma}{A}\le C\delta^2.
\tag{5.3}
\]

Therefore any sequence with \(\delta_i\to0\) necessarily satisfies
\(\sigma_i/A_i\to0\).  The purely topological lower bound gives a fixed margin
only when \(\sigma/A\) is bounded below by a positive constant.  The smoothing
argument must cover the full near-critical regime \(\sigma_i/A_i\to0\), including
sequences with every \(\sigma_i>0\).  It is not enough to prove the exact
\(\sigma=0\) case.

Terminal recalibration survives in this regime: the topological excess tightens
rather than weakens the calibration because the exact deficit identity gives
\(D_a\le R-\sigma\le R\).  Since both \(R/A\) and \(\sigma/A\) tend to zero in a
near-pinched sequence, the normalized terminal density remains \(o(A)\) if the
flow preserves \(Q/A\to0\).

---

## 6. Support geometry corrections

Later uses of the selected-support theorem should use the following spatial
organization.

1. Choose maximal-function good centers with a macro-separation such as an
   \(r\)-separated net.  Build a graph with an edge whenever the corresponding
   macro buffers interact, for example at distance \(\le12r\).
2. Color this bounded-degree graph and keep a color class of maximal volume.
   Then the enlarged buffers (e.g. \(B_{6r}\) in the initial metric) are
   pairwise disjoint for the retained class.  This is stronger than merely
   having small physical supports; it is what makes the global defect sum exact.
3. Use an inner center set \(P_j\) such as \(B_r(x_j)\), a larger active plateau
   on which \(a=1\) such as \(B_{4r}(x_j)\), and a still larger stationary
   collar/support contained in the controlled energy domain.  The terminal
   exponential geodesics used in the pullback argument must remain inside the
   bounded-curvature \(a=1\) plateau buffer after metric comparison.
4. Terminal eigenline/harmonic-form densities whose estimates are proved only
   on bounded-curvature regions should be zero-extended outside those regions
   before applying the global pullback averaging inequality.
5. For the positive-part rescaled monopole at terminal time in varying families,
   the regularization parameter should scale with the terminal mean defect, e.g.
   \(\varepsilon=Q/\operatorname{Vol}\), and all final density estimates should
   be normalized by \(A\).

These support refinements are compatible with the Step 28 exponential-pullback
bridge, but they are not all written into Step 29's theorem statement.

---

## 7. Current state of the restricted negative route

After this repair, the best analytic route is still alive and sharper:

\[
H_2\ \longrightarrow\ Y\ \longrightarrow\text{weighted mixed Moser}\
\longrightarrow\|aF\|_\infty\ \longrightarrow\ J_6\ \longrightarrow
\|aE\|_\infty\ \longrightarrow\text{velocity/continuation}.
\]

The repaired mixed Hölder--Sobolev estimate removes the specific Step 29
embedding error.  The unweighted-\(U\) first-bound shortcut is withdrawn.  What
still needs proof is the tensor-level power inequality with correct polynomial
\(p\)-dependence, the q=3 positive-time potential, fixed \(J_6\) persistence,
common-time continuation via shifted curvature, and macro-disjoint support
selection producing fixed \(A\)-normalized plateau mass and bounded-curvature
buffers.

Even if completed, this would exclude a restricted four-dimensional negative
Ishida--LeBrun near-critical laboratory.  It does not settle the positive branch,
arbitrary four-manifolds, dimensions \(n\ge5\), the full Yau 26 interval
proposition, or Lean formalization.
