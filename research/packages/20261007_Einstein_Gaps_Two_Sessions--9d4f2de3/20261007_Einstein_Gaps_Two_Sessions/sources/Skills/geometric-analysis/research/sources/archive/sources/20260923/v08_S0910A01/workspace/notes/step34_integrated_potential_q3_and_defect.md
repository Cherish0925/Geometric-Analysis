# Step 34: fixed-exponent integrated potential, q=3 propagation, and two-factor J6 persistence

Session: S0910A01. Agent3 / Actuator. Phase: Execute.

## 0. Purpose and status

This note repairs the fixed-exponent analytic layer for the selected-support
normalized cutoff flow
\[
\partial_t g=-2aE,
\qquad a=\chi^2,
\qquad E=\operatorname{Ric}+g
\tag{0.1}
\]
on one buffered macro-support in the restricted four-dimensional negative
Ishida--LeBrun route.  It is a fixed-exponent module, not a full smoothing theorem.
It establishes two conditional consequences once the q=2 curvature energy and the
fixed-p tensor inequalities have been proved on a provisional smooth first-exit
interval:

1. an integrated curvature potential
\[
B(t)=\int_0^t {\mathcal S}(s)^2Y(s)\,ds\le C\gamma^3,
\tag{0.2}
\]
which makes q=3 same-support propagation a good-slice/Gronwall consequence;
2. a simpler unregularized \(J_6\) persistence estimate using A03 Step 35's
two-factor defect absorption, independent of \(Y=\int aF^3\):
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).
\tag{0.3}
\]

Throughout use the squared Sobolev convention
\[
\|u\|_4^2\le {\mathcal S}(t)
\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),
\qquad {\mathcal S}\simeq r^2V^{-1/2},
\tag{0.4}
\]
where \(V\) is the relevant support-scale ball volume.  During first-exit
arguments we assume provisionally
\({\mathcal S}(t)\le2{\mathcal S}(0)\) and the corresponding metric/support
comparability; this moving-geometry premise must later be closed by the defect
drift and continuation argument.

The note deliberately distinguishes three levels:

- algebra/scaling consequences checked by `workspace/scripts/step34_integrated_potential_q3_verify.py`;
- tensor PDE premises, still needing a complete index-level derivation;
- later moving-Sobolev, cutoff-jet, existence, and terminal geometry obligations.

## 1. Localized variables and the p=2 notation correction

Let
\[
F=(1+|\operatorname{Rm}|^2)^{1/2},
\qquad
Y=K_3=\int \eta^2 aF^3\,d\mu_t.
\tag{1.1}
\]
For \(p\ge3\), write
\[
K_p=\int \eta^2a^{p-2}F^p\,d\mu_t;
\tag{1.2}
\]
since \(\eta=1\) on \(\operatorname{supp}a\) and \(a=0\) on
\(\operatorname{supp}d\eta\), the auxiliary cutoff creates no active derivative
terms.  The special \(p=2\) seed must **not** be read as
\(K_2=\int F^2\).  The q=2 local energy from Step 25 is instead
\[
K_2^\eta=\int \eta^2F^2\,d\mu_t,
\qquad
D_2^\eta=\int \eta^2a|\nabla\operatorname{Rm}|^2\,d\mu_t.
\tag{1.3}
\]
This correction was highlighted by Step 34 TTCS: without \(\eta\), the p=2
quantity is not localized to the selected good support and is not controlled by
\(K_0V\).

The absorption parameter is therefore
\[
\gamma={\mathcal S}(0)(K_2^\eta(0))^{1/2}.
\tag{1.4}
\]
At a maximal-function good support with \(K_2^\eta(0)\le K_0V\),
\[
\gamma\le C{r^2\over\sqrt V}\sqrt{K_0V}=Cr^2\sqrt{K_0},
\tag{1.5}
\]
so the collapse-dependent volume in \({\mathcal S}\) cancels against the q=2
seed.  This is the corrected convention after the A03 #330/#332 episode.

## 2. Curvature evolution convention and fixed-p premise

Use all-lower curvature
\(R_{ijkl}=g_{l\alpha}R_{ijk}{}^\alpha\), with norm computed using four inverse
metrics.  For the pure scaling test \(\partial_tg=-2g\), the connection and
\(R_{ijk}{}^\ell\) are fixed, while
\[
\partial_tR_{ijkl}=-2R_{ijkl}.
\tag{2.1}
\]
Thus
\[
2\langle R,\partial_tR\rangle=-4|R|^2,
\qquad
\partial_t|R|^2=4|R|^2
\tag{2.2}
\]
after adding the four inverse-metric variations.  In dimension four,
\(\partial_td\mu=-4d\mu\), so \(\int|R|^2d\mu\) is invariant.  For
\(F^2=1+|R|^2\), only the constant part contributes a lower-order source.  Hence
normalization/conformal terms must not be treated as pointwise curvature damping.

For (0.1), the pointwise upper input has the schematic form
\[
\partial_tF^2\le a\Delta F^2-2a|\nabla\operatorname{Rm}|^2
+C|\nabla a|F|\nabla\operatorname{Rm}|+
\Sigma_H+CaF^3,
\tag{2.3}
\]
where \(\Sigma_H\) denotes signed Hessian-cutoff contractions
\[
\Sigma_H=(\nabla^2a)*(\operatorname{Rm}+g)*\operatorname{Rm}
\tag{2.4}
\]
inside the subsequent integral.  The term \(CaF^3\) absorbs Hamilton reaction,
metric variation, and volume terms because \(|E|\le CF\) and
\(|s+4|=|\operatorname{tr}E|\le CF\).  No pointwise persistence of
\(|E|\ll1\) is used.

Testing (2.3) by \((p/2)a^{p-2}F^{p-2}\) for \(p\ge3\), the volume-form term is
controlled as
\[
\left|\int a^{p-2}F^p\partial_td\mu\right|
=\left|\int a^{p-1}(s+4)F^p\right|
\le C\int a^{p-1}F^{p+1}.
\tag{2.5}
\]
Thus it belongs to the reaction; the Step 33 bound \(C\delta K_p\) is not
available before defect persistence is proved.

The diffusion and explicit tensor dissipation give, before cutoff absorption,
\[
\boxed{-pD_p^{\rm Rm}-p(p-2)D_p^F,}
\tag{2.6}
\]
where
\[
D_p^{\rm Rm}=\int a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2,
\qquad
D_p^F=\int a^{p-1}F^{p-2}|\nabla F|^2.
\tag{2.7}
\]
This fixes the Step 33 inconsistency that had effectively added back a spurious
\(+pD_p^F\) and changed the radial coefficient to \(-p(p-3)D_p^F\).  At \(p=3\),
the corrected formula retains the radial dissipation.

The cutoff cross terms use
\(|\nabla a|^2/a=4|\nabla\chi|^2\le Cr^{-2}\), giving
\[
\text{first-derivative cutoff terms}
\le\varepsilon pD_p^{\rm Rm}+\varepsilon p(p-2)D_p^F
+C_\varepsilon p^Nr^{-2}K_p.
\tag{2.8}
\]
For the first smoothing bound, use the signed Hessian route rather than assuming
an evolving pointwise Hessian bound.  A typical term is
\[
T_H=p\int a^{p-2}F^{p-2}(\nabla_i\nabla_ja)B^{ij}(\operatorname{Rm},g).
\tag{2.9}
\]
It is not enough to know \(|B|\le CF^2\); the tensor variation must supply
\[
|\nabla B|\le CF|\nabla\operatorname{Rm}|.
\tag{2.10}
\]
This derivative structure is expected because \(B\) is algebraic in
\(\operatorname{Rm}\), \(E=\operatorname{Ric}+g\), and \(g\), with
\(|\nabla E|\le C|\nabla\operatorname{Rm}|\), but it remains part of the
index-level PDE premise.  Under (2.10), signed tensor IBP gives
\[
|T_H|\le \varepsilon pD_p^{\rm Rm}
+
\varepsilon p(p-2)D_p^F
+C_\varepsilon p^Nr^{-2}K_p.
\tag{2.11}
\]
This route uses only the fixed cutoff gradient and the already available tensor
dissipation.  The alternative pointwise bound
\(|\nabla^2_{g(t)}a|\le Cr^{-2}\) is a stronger later continuation input, not an
interchangeable premise for the initial smoothing estimate.

The curvature reaction is absorbed with the four-dimensional identity
\[
a^{p-1}F^{p+1}
=(aF^3)^{1/3}(a^{p-2}F^p)^{1/3}
\left(a^{(p-1)/2}F^{p/2}\right)^{4/3}.
\tag{2.12}
\]
Hölder, Sobolev, and Young give
\[
Cp\int a^{p-1}F^{p+1}
\le \varepsilon\bigl[pD_p^{\rm Rm}+p(p-2)D_p^F\bigr]
+C_\varepsilon p^N{\mathcal S}^2YK_p
+C_\varepsilon p^Nr^{-2}K_p.
\tag{2.13}
\]
The fixed-p curvature premise is therefore
\[
\boxed{
K_p'+c\bigl[pD_p^{\rm Rm}+p(p-2)D_p^F\bigr]
\le Cp^N(r^{-2}+1+{\mathcal S}^2Y)K_p,
\qquad p\ge3.}
\tag{2.14}
\]
All lower-order contributions from the \(1\) in \(F\) carry an active weight and
are bounded by \(C(r^{-2}+1)K_p\), not by a separate unweighted volume constant.
For \(p=3\), (2.14) implies
\[
\boxed{Y'\le C(r^{-2}+1+{\mathcal S}^2Y)Y.}
\tag{2.15}
\]

## 3. Integrated potential from q=2

The q=2 estimate from Step 25, on the same buffered support, is
\[
(K_2^\eta)'+cD_2^\eta\le CY+Cr^{-2}K_2^\eta.
\tag{3.1}
\]
The p=2 interpolation uses the localized variables:
\[
Y=\int \eta^2aF^3
=\int (\eta F)(\chi F)^2
\le (K_2^\eta)^{1/2}\|\chi F\|_4^2.
\tag{3.2}
\]
Sobolev gives
\[
\|\chi F\|_4^2
\le C{\mathcal S}(D_2^\eta+r^{-2}K_2^\eta),
\tag{3.3}
\]
and hence, in the first-exit interval,
\[
Y\le C\gamma(D_2^\eta+r^{-2}K_2^\eta).
\tag{3.4}
\]
For \(C\gamma\) small, the \(D_2^\eta\) contribution is absorbed into (3.1), and
for \(t\le T=\theta r^2\), with \(\theta\) fixed small,
\[
\sup_{s\le t}K_2^\eta(s)+\int_0^tD_2^\eta(s)\,ds\le C K_2^\eta(0).
\tag{3.5}
\]
Therefore
\[
\boxed{
\int_0^tY(s)\,ds\le C\gamma K_2^\eta(0).}
\tag{3.6}
\]
Using \({\mathcal S}(s)\le2{\mathcal S}(0)\),
\[
\boxed{
B(t):=\int_0^t{\mathcal S}(s)^2Y(s)\,ds
\le C{\mathcal S}(0)^2\gamma K_2^\eta(0)=C\gamma^3.}
\tag{3.7}
\]
This bound uses only q=2 energy plus Sobolev interpolation; it does not use a
pointwise q=3 estimate.

## 4. q=3 same-support propagation by good slice and Gronwall

For any \(t\in(0,T]\), (3.6) gives a slice
\(\tau\in[t/4,t/2]\) such that
\[
Y(\tau)
\le {4\over t}\int_{t/4}^{t/2}Y(s)\,ds
\le {C\gamma K_2^\eta(0)\over t}.
\tag{4.1}
\]
Integrating the fixed-p q=3 inequality (2.15) from \(\tau\) to \(t\),
\[
Y(t)
\le Y(\tau)
\exp\left(C\int_\tau^t(r^{-2}+1)\,ds
+C\int_\tau^t{\mathcal S}^2Y\,ds\right).
\tag{4.2}
\]
Because \(t\le\theta r^2\) and (3.7) holds,
\[
\int_\tau^t(r^{-2}+1)\,ds\le C(\theta+	heta r^2),
\qquad
\int_\tau^t{\mathcal S}^2Y\,ds\le C\gamma^3.
\tag{4.3}
\]
Thus
\[
\boxed{
Y(t)\le {C\gamma K_2^\eta(0)\over t},
\qquad
{\mathcal S}(t)^2Y(t)\le {C\gamma^3\over t}.}
\tag{4.4}
\]
The appearance of \(Y\) in its own coefficient is not circular, because its time
integral was already controlled by q=2.  The \(t^{-1}\) estimate is a positive-time
input for dyadic high-p Moser; it is not integrated from zero.

## 5. Unregularized J6 persistence by two-factor defect absorption

A03 Step 35 supplies a sharper fixed-exponent defect estimate than the three-factor
regularized route considered earlier in this session.  Set
\[
s=|E|^2,
\qquad
J_6=\int \eta^2a^4s^3,
\qquad
X_6=\int \eta^2a^5s^2|\nabla E|^2,
\tag{5.1}
\]
and
\[
P_6=\int \eta^2a^5Fs^3.
\tag{5.2}
\]
Since \(s^3=|E|^6\) is smooth, the energy derivative can be taken without a norm
regularization.  The Sobolev variable
\[
w_6=\eta a^{5/2}s^{3/2}=\eta\chi^5|E|^3
\tag{5.3}
\]
is \(C^1\) at \(E=0\), and this is enough for the Sobolev step.

The defect equation follows from
\[
\partial_tE=D\operatorname{Ric}_g[-2aE]-2aE,
\tag{5.4}
\]
using the contracted Bianchi identity to combine the coefficient-\(a\) second
derivatives into a Lichnerowicz-type principal operator.  All terms are homogeneous
in \(E\): the remaining cutoff terms are \((\nabla a)*\nabla E\) and
\((\nabla^2a)*E\), and algebraic terms are bounded by \(CaF|E|\) after testing.
For \(s=|E|^2\),
\[
(\partial_t-a\Delta)s=-2a|\nabla E|^2+\Sigma_s,
\tag{5.5}
\]
where non-cutoff reaction terms are bounded by \(CaFs+Cas\), and cutoff terms are
handled by signed IBP.

The exact chain rule for \(s^3\) gives the favorable additional term
\[
(\partial_t-a\Delta)s^3=3s^2(\partial_t-a\Delta)s-6as|\nabla s|^2.
\tag{5.6}
\]
After integrating by parts against \(\eta^2a^4\), the principal dissipation is
\(-6X_6\), and the chain-rule \(-6as|\nabla s|^2\) term is nonpositive.
First-derivative cutoff terms have the structure
\[
\int \eta^2a^4|da|s^{5/2}|\nabla E|
\le \varepsilon X_6+C_\varepsilon r^{-2}J_6.
\tag{5.7}
\]
(A03's displayed line 3.6a has \(s^{3/2}\); the surrounding text and verifier show
the intended power is \(s^{5/2}\), matching (5.7).)

For the Hessian-a part one must again keep the signed tensor.  In the defect case
the contraction is quadratic in \(E\):
\[
B^{ij}=2g^{ij}|E|^2+2(\operatorname{tr}E)E^{ij}-4E^{ik}E_k{}^j,
\tag{5.8}
\]
so \(|B|\le Cs\) and \(|\nabla B|\le Cs^{1/2}|\nabla E|\).  Tensor IBP on
\(\nabla_i\nabla_ja\), with derivatives falling on \(a^4\), \(s^2\), and
\(B\), gives
\[
|T_H^E|\le \varepsilon X_6+C_\varepsilon r^{-2}J_6.
\tag{5.9}
\]
Thus the unabsorbed differential inequality is
\[
\boxed{J_6'+cX_6\le C(1+r^{-2})J_6+CP_6.}
\tag{5.10}
\]

The potential is linear in \(F\), so it does **not** need the curvature cubic
moment \(Y\).  Since
\[
P_6=\int Fw_6^2,
\tag{5.11}
\]
Hölder and Sobolev give
\[
P_6\le \|F\|_{2,\operatorname{supp}w_6}\|w_6\|_4^2
\le C(K_2^\eta)^{1/2}{\mathcal S}(X_6+r^{-2}J_6)
=C\gamma(X_6+r^{-2}J_6).
\tag{5.12}
\]
Here
\[
\|\nabla w_6\|_2^2\le C(X_6+r^{-2}J_6),
\qquad
\|w_6\|_2^2\le J_6,
\tag{5.13}
\]
because \(a=0\) on \(\operatorname{supp}d\eta\), the \(d\chi\) term is bounded by
\(r^{-2}J_6\), and \(|\nabla s|^2\le4s|\nabla E|^2\).
For \(C\gamma<c/2\), (5.10)--(5.12) yield
\[
\boxed{J_6'+c'X_6\le C(1+r^{-2})J_6.}
\tag{5.14}
\]
Consequently,
\[
\boxed{J_6(t)\le e^{C(1+r^{-2})t}J_6(0).}
\tag{5.15}
\]
For \(T=\theta r^2\) and \(r\le r_0\), the exponent is bounded by
\(C(\theta+	heta r^2)\), so if the initial Ricci defect is
\(\|E(0)\|_\infty\le\delta\) on the selected support, then
\[
J_6(T)\le C\delta^6V.
\tag{5.16}
\]
This is strictly simpler than the earlier three-factor defect route: q=3 and
\(B(t)\) are not needed for \(J_6\) persistence.  The integrated-potential
estimate remains essential for q=3 curvature propagation and the curvature Moser
coefficient on positive dyadic slabs.

## 6. Connection with the high-p weighted Moser step

Once (4.4) and (5.15) are available, the existing nested-time Moser recurrence from
Step 32/A03 Step 34 applies on positive slabs:
\[
\|af(t)\|_\infty
\le C{\mathcal S}^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^tH_{p_0}(f,s)\,ds\right)^{1/p_0}.
\tag{6.1}
\]
For curvature, \(p_0=3\) and (3.6) give
\[
\|aF(t)\|_\infty\lesssim {\gamma\over t}.
\tag{6.2}
\]
For defect, \(p_0=6\) and (5.16) give
\[
\|aE(t)\|_\infty\lesssim \delta(r^2/t)^{1/3},
\tag{6.3}
\]
and hence
\[
\int_0^T\|aE(t)\|_\infty\,dt
\lesssim \delta r^{2/3}T^{2/3}
=\delta\theta^{2/3}r^2.
\tag{6.4}
\]
This is the metric-drift input for the simultaneous first-exit closure.

## 7. What remains unproved

This step strengthens the fixed-exponent analytic bridge but does not prove the
restricted negative-family theorem, much less Yau Problem 26.  The exact remaining
mathematical obligations are:

1. complete the index-level all-lower curvature variation for (2.3), including the
normalization coefficients and the derivative-structure bound (2.10);
2. complete the defect variation from Ricci variation and contracted Bianchi at the
level needed for (5.5), including the signed Hessian contraction (5.8);
3. close the simultaneous first-exit interval carrying \({\mathcal S}(t)\),
\(K_2^\eta(t)\), \(J_6(t)\), support/buffer geometry, and metric comparison;
4. prove degenerate-flow existence and continuation with coupled cutoff jets, then
obtain terminal bounded-curvature plateaux;
5. combine terminal calibration and exponential-pullback selection with the
Derdziński forbidden-germ argument.

Even a complete solution of these obligations would address only the near-critical
Ishida--LeBrun negative four-dimensional laboratory.  The positive branch,
arbitrary four-manifold topology, dimensions \(n\ge5\), dimension-only interval
constants for the original proposition, and Lean formalization remain open.
