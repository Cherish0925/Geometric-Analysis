# Moving surgery centers and uniform first-order stability

28 September 2026. Continuation of 3409fe5. This is a local research
proof, not a web-review package.

The previous [I52 proof](20260927_endpoint_covariance_and_surgery_limits.md)
established first-order stability of selected shrinking-surgery metrics
inside explicit TT or Bianchi slices. The missing passage from arbitrary
nearby metrics to a fixed slice is not merely an unproved estimate.
The construction below shows that such a passage, with uniformly bounded
metric distortion, can fail on the actual recovery family.

The obstruction is a marked geometric variable. A harmonic map on the
smooth negatively curved limit is fixed by its homotopy class, whereas
an isotopy on the resolved manifold must preserve the exceptional class
and hence its concentration point. Moving that point relative to the
limiting harmonic map makes the two requirements incompatible.

The positive continuation keeps the centers as parameters. I52's
first-order inequality then holds uniformly on compact configuration
families, including their conformal and diffeomorphism saturations.
It does not assert that every nearby metric admits this parametrization.
Continuing past this obstruction, the companion
[matched-cap proof I53](20260928_intrinsic_caps_and_stability.md)
now removes the gauge and scalar assumptions from the lower first-order
bound near selected recovery bases. It does not solve a fixed exact slice.

## 1. Notation and actual recovery geometry

Let \(X\) be a closed complex-hyperbolic surface with
\(\operatorname{Ric}(g_X)=-g_X\), and let \(A=c_1^2(X)\). On
\[
 M=X\# k\overline{\mathbb {CP}}^{\,2}
       \#\ell(S^1\times S^3),\qquad k\ge1,
\]
put \(Q=k+4\ell\), \(h=Q/A\), and
\[
 P(g)=\int|\operatorname{Ric}^{\circ}_g|^2,\quad
 S(g)=\int s_g^2,\quad R(g)=\int|\operatorname{Ric}_g|^2.
\]
The relative Einstein defect is the same functional as in I40--I52.
For a scalar-minus-four metric it is
\[
 \mathcal E(g)=\frac{4P(g)}{R(g)}
             =\frac{4P(g)}{P(g)+4V(g)}.                 \tag{1.1}
\]
All classes and actual monopole suppliers are inherited from the same
smooth manifolds. No new local solution is substituted for a closed
conformal supplier.

We use the actual Burns blowup and two-ended scalar-flat Schwarzschild
handle constructions of LeBrun, Theorem 4.3, with negative Yamabe
normalization as justified in I52, Section 3. For a fixed \(X,k,\ell\),
their normalized shrinking limits satisfy
\[
 P(g_t)\longrightarrow8\pi^2Q,\qquad
 V(g_t)\longrightarrow2\pi^2A,\qquad
 \mathcal E(g_t)\longrightarrow\frac{4h}{1+h}.         \tag{1.2}
\]
The last limit is a recovery value, not an assertion about the
unrestricted infimum.

For the marked argument it is important to specify the handles.
We put the two mouths of each handle in one shrinking background
ball. If \(R_t\) is its outer radius, \(d_t\) the separation of the
mouths, \(r_t\) their cutoff radius and \(a_t\) the donor scale, choose
\[
 a_t\ll r_t^2,\qquad r_t\ll d_t\ll R_t\longrightarrow0. \tag{1.3}
\]
All clusters are disjoint, and the limiting cluster points are distinct.
First select the cluster sizes; then choose the inner scales sufficiently
small for the finitely many required energy and normalization errors.
This is a fixed-topology diagonal, before taking any large-cover limit.

The whole handle cluster has diameter tending to zero. The Schwarzschild
neck has diameter \(O(r_t)\), and the remaining cluster has diameter
\(O(R_t)\). The normalized Yamabe factors have a uniform upper bound
from the uniform negative lower bound for the raw scalar curvature.
These statements also hold for the Burns regions. The metrics converge
smoothly to the background off the finite set of limiting points.
Consequently the marked metric spaces converge to the smooth \(X\).

This choice is essential: handles joining two fixed distinct points
would instead identify those points in the metric limit. We do not
use that different limit here. Clustering does not change the smooth
topology, the actual supplier, or the costs in (1.2).

The cutoffs and the exterior estimates of I52 remain available. One
uses an enclosing cutoff for each whole cluster and much smaller
cutoffs at the two mouths for construction. There is bounded curvature
energy per cluster, and the transition errors are chosen arbitrarily
small. Thus these clustered bases can satisfy all the selections in
I52, Theorem 9, simultaneously with (1.3).

## 2. Comparing normalization without resolving the cores again

The following elementary observation is useful when the raw metrics
agree near the entire singular region.

**Lemma 1 (relative Yamabe normalization).** Suppose \(b_{0,t}\) and
\(b_{1,t}\) are smooth raw metrics on the same closed manifold, equal
outside a fixed regular region \(K\). Let
\(g_{0,t}=u_t^2b_{0,t}\) have scalar curvature \(-4\). Assume on a
neighborhood of \(K\) that
\[
 u_t\longrightarrow1\text{ in }C^2,\qquad
 b_{i,t}\longrightarrow b_i\text{ smoothly},\qquad s_{b_i}=-4.
                                                               \tag{2.1}
\]
If \(\|b_{1,t}-b_{0,t}\|_{L^\infty(b_{0,t})}\le a\), then their
scalar-minus-four Yamabe representatives satisfy
\[
 \|g_{1,t}-g_{0,t}\|_{L^\infty(g_{0,t})}\le a+o_t(1)(1+a).       \tag{2.2}
\]
No lower bound for the size of the cores is needed.

**Proof.** Put \(\widetilde g_t=u_t^2b_{1,t}\).
It equals \(g_{0,t}\) off \(K\). The conformal scalar formula and
(2.1) show
\[
 \delta_t:=\|s_{\widetilde g_t}+4\|_\infty\longrightarrow0.
\]
For sufficiently small \(t\), this metric has negative scalar
curvature. Write its normalized representative as
\(g_{1,t}=v_t^2\widetilde g_t\). At the maximum and minimum of \(v_t\),
the scalar equation gives
\[
 1-\delta_t/4\le v_t^2\le1+\delta_t/4.                         \tag{2.3}
\]
The common \(u_t^2\) cancels in the relative pointwise tensor norm,
which proves (2.2). QED.

This proof requires only the already established exterior convergence.
It does not infer uniform convergence of \(u_t\) on every rescaled
donor from exterior convergence.

## 3. A fixed-base Bianchi slice can have unbounded distortion

Our divergence convention is
\[
 \beta_g q=\delta_gq+\tfrac12d\,\operatorname{tr}_gq,\qquad
 (\delta_gq)_j=-\nabla^i q_{ij}.
\]
For a diffeomorphism \(\varphi\), set \(q=\varphi^*g_1\). Direct
contraction of the connection difference gives
\[
 \tau(\operatorname{id}:(M,g_0)\to(M,q))^k
       =-q^{k\ell}(\beta_{g_0}q)_\ell.                         \tag{3.1}
\]
Thus
\(\beta_{g_0}(\varphi^*g_1-g_0)=0\) is exactly the harmonic-map
equation for \(\varphi:(M,g_0)\to(M,g_1)\), not only its linearization.

**Theorem 2 (marked obstruction to a uniform fixed slice).**
For the balanced actual family used in I40--I52, with \(h_j\to0\)
and at least one blowup, there exist scalar-minus-four recovery
metrics \(g_j^0,g_j^1\) on the same \(M_j\) such that
\[
 \|g_j^1-g_j^0\|_{L^\infty(g_j^0)}\longrightarrow0,\qquad
 \frac{\mathcal E(g_j^0)}{h_j}\longrightarrow4,\qquad
 \frac{\mathcal E(g_j^1)}{h_j}\longrightarrow4,                 \tag{3.2}
\]
and every \(\varphi\in\operatorname{Diff}_0(M_j)\) satisfying
\[
 \beta_{g_j^0}(\varphi^*g_j^1-g_j^0)=0                         \tag{3.3}
\]
has bilipschitz constant greater than \(j\), measured from \(g_j^0\)
to \(g_j^1\). If no such diffeomorphism exists, the statement has
the usual empty-set meaning.
The same examples can also be chosen with
\[
 \|\delta_{g_j^0}^*\beta_{g_j^0}(g_j^1-g_j^0)\|_2=o(\sqrt{Q_j}).
                                                               \tag{3.3a}
\]
Thus even a small actual gauge residual does not imply a uniformly
controlled exact gauge at the fixed marked base.

The bases \(g_j^0\) may in addition satisfy the selections of I52.
In particular there is no automatic uniformly bounded, let alone
vanishing-amplitude, exact Bianchi representative relative to those
fixed bases under just constant scalar curvature, competitive energy,
and \(C^0\) closeness.

**Proof: move the smooth background while retaining the marked core.**
First keep \(X,k,\ell\) fixed. Choose one exceptional point \(p\).
In a CH chart about \(p\), choose a local Killing field moving \(p\),
multiply it by a cutoff, and let \(\psi_\epsilon\) be its small-time
flow. It is isotopic to the identity, is a genuine local CH isometry
on a smaller neighborhood of \(p\), and is the identity near all
other surgery clusters and outside a larger chart. Set
\[
 b_\epsilon=\psi_\epsilon^*g_X .
\]
Then \(b_\epsilon=g_X\) near every donor and outside a fixed regular
annulus \(K\), while
\[
 \|b_\epsilon-g_X\|_{C^m}\le C_m|\epsilon|,\qquad
 \psi_\epsilon^{-1}(p)\ne p\quad(\epsilon\ne0).                 \tag{3.4}
\]
Perform exactly the same marked surgeries at exactly the same
points in \(g_X\) and \(b_\epsilon\). The two raw metrics are identical
near all donors, and differ only on \(K\). Normalize them to obtain
\(g_{0,t}\) and \(g_{\epsilon,t}\).
Lemma 1 and the recovery limits give, for fixed \(\epsilon\),
\[
 \|g_{\epsilon,t}-g_{0,t}\|_{L^\infty(g_{0,t})}
       \le C|\epsilon|+o_t(1),                               \tag{3.5}
\]
and (1.2) for both families.

**Proof: compactness of a hypothetical bounded-distortion gauge.**
Suppose for this fixed nonzero \(\epsilon\) there are \(t_n\to0\)
and \(L\)-bilipschitz maps
\(\varphi_n\in\operatorname{Diff}_0(M)\) satisfying (3.3).
The collapsing regions described in Section 1 have diameter tending
to zero. Uniform convergence on the smooth exterior, or equivalently
the elementary compactness of bilipschitz maps between the resulting
compact metric spaces, produces a bilipschitz homeomorphism
\[
 F:(X,g_X)\longrightarrow(X,b_\epsilon).                     \tag{3.6}
\]
The inverse maps converge as well, so this is not merely a continuous
map onto a quotient.

The exceptional class at \(p\) forces
\[
 F(p)=p.                                                     \tag{3.7}
\]
Indeed the exceptional sphere \(E_p\) in the source has diameter
tending to zero. Its image also does, and
\([\varphi_n(E_p)]=[E_p]\ne0\) in \(H_2(M;\mathbb Z)\).
If its limit were a regular point of the target \(X\), it would
eventually lie in a contractible coordinate ball and have zero class.
If its limit were another exceptional point \(q\), it would lie in
one fixed small enclosing topological neighborhood of that cluster,
whose image in \(H_2(M)\) is
\(\mathbb Z[E_q]\), not \(\mathbb Z[E_p]\).
A whole handle cluster has \(H_2=0\).
These exhaust the points other than \(p\), proving (3.7).
We use the entire neighborhoods and their marked homology, not just
terminal bubbles.

**Proof: the limit is in the identity homotopy class.**
Collapse maps \(\pi_n:M\to X\) induce the usual quotient
\[
 \pi_1(M)=\pi_1(X)*F_\ell\longrightarrow\pi_1(X).
\]
Isotopy of \(\varphi_n\) gives
\(\pi_n\circ\varphi_n\simeq\pi_n\).
Choose generators on loops avoiding the finite source cluster set
and \(F^{-1}\) of the target cluster set. On these loops the convergence
is in the ordinary smooth regions, so the induced outer homomorphism
of \(F\) on \(\pi_1(X)\) is the identity. The CH manifold \(X\) is
aspherical. Hence \(F\) is homotopic to the identity.
This argument explicitly kills the free handle generators; it does
not identify \(\pi_1(M)\) with \(\pi_1(X)\).

**Proof: the harmonic limit contradicts the mark.**
By (3.1), each \(\varphi_n\) is harmonic. Away from the finite set
consisting of source cluster points and inverse images of target
cluster points, both metrics converge smoothly and the differential
of \(\varphi_n\) is uniformly bounded. In coordinates the harmonic
equation has bounded right-hand side; interior elliptic estimates
and bootstrapping give smooth convergence there.

The limit (3.6) is Lipschitz on the smooth compact \(X\).
In the weak harmonic equation a cutoff at a missing point has an
error bounded by \(C r^3\): the derivative of the map is bounded
and the cutoff has derivative \(O(r^{-1})\) on a four-dimensional
annulus of volume \(O(r^4)\). The equation therefore extends weakly
across every missing point. Coordinate elliptic regularity makes
\(F\) a smooth harmonic map on all of \(X\).

The map \(\psi_\epsilon^{-1}:(X,g_X)\to(X,b_\epsilon)\) is an
isometry, hence harmonic, and is homotopic to the identity.
Strictly negative sectional curvature of \(b_\epsilon\) makes
this harmonic map unique in its homotopy class. One may apply
[Hartman, Section 1(H), rank-greater-than-one corollary, p.675](https://math.jhu.edu/~js/Math646/hartman.harmonic.pdf).
Equivalently, geodesic-homotopy energy convexity is strict against
the rank-four isometry unless the homotopy is stationary.
Thus \(F=\psi_\epsilon^{-1}\), contradicting (3.7) and (3.4).

We have proved that for each fixed nonzero \(\epsilon\) and each
finite \(L\), sufficiently small donor scales exclude every such
\(L\)-bilipschitz gauge.

**Proof: the balanced diagonal.**
Return to \(X_j,k_j,\ell_j\). Choose \(\epsilon_j\to0\), using
uniformly controlled lifted CH charts; if needed choose it even
smaller to absorb any chart constant. For each fixed \(j,\epsilon_j\),
choose the clustered donor scales so small that:

- the just-proved exclusion holds with \(L=j\);
- the relative error in (3.5) tends to zero;
- both errors in (1.2) are \(o(Q_j)\) in \(P\) and small enough
  in \(V\) to give (3.2);
- all the core, exterior, and near-stationarity errors required in
  I52 are at most a prescribed number tending to zero.

Each list is finite at fixed \(j\), so the same diagonal satisfies
all requirements. Since \(4/(1+h_j)\to4\), (3.2) follows.
No assertion about the rate at which the necessary bilipschitz
constant diverges is required. The remaining strengthening (3.3a)
is proved next and is included in the same diagonal. QED.

### 3.1 The counterexamples still satisfy the approximate-gauge criterion

This is a positive coverage statement as well as a distinction between
an approximate and an exact gauge. Write
\[
 r_t=u_t^2(b_{\epsilon,t}-b_{0,t}),\qquad
 \widetilde g_t=g_{0,t}+r_t,\qquad
 g_{\epsilon,t}=e^{2f_t}\widetilde g_t,\qquad w_t=e^{2f_t}-1.
\]
The tensor \(r_t\) is supported in the regular annulus \(K\), with
\(\|r_t\|_{C^2(g_{0,t},K)}\le C|\epsilon|\). Lemma 1 gives
\(\|f_t\|_\infty\le C\delta_t\), where
\(s_{\widetilde g_t}+4\) is supported in \(K\), has supremum
\(\delta_t\to0\), and has \(L^2\) norm \(O(\delta_t)\).
Also \(P(\widetilde g_t)\le C Q\), since outside \(K\) it is the
same metric as \(g_{0,t}\), while its curvature on \(K\) converges
smoothly to that of the CH background \(b_\epsilon\).

The derivative bounds proved in I52, Lemma 5, now apply on
\(\widetilde g_t\):
\[
 \|\nabla^2 f_t\|_2\le C\delta_t(1+\sqrt Q),\qquad
 \|df_t\|_2\le C\delta_t,\qquad
 \|df_t\|_4^2\le C\delta_t^2(1+\sqrt Q).               \tag{3.8}
\]
Changing the connection in these estimates back to \(g_{0,t}\)
only costs \(C|\epsilon|\|df_t\|_{2,K}\); the two metrics agree
off \(K\). Consequently the Hessian of \(w_t\) has the same first
bound in (3.8).

Put \(k_t=g_{\epsilon,t}-g_{0,t}
       =w_tg_{0,t}+(1+w_t)r_t\). The exact product rules are
\[
 \beta_0(wg_0)=dw,\qquad
 \beta_0(fr)=f\beta_0r+
       \bigl(\tfrac12\operatorname{tr}_0r\,I-r^\sharp\bigr)df .
\]
One further derivative therefore gives
\[
 \|\delta_0^*\beta_0 k_t\|_2
    \le C\{|\epsilon|+\delta_t(1+\sqrt Q)\}.           \tag{3.9}
\]
Choose the donor scales also to ensure
\(\delta_t(1+\sqrt Q)\le|\epsilon|\).
With \(\epsilon_j\to0\) and \(Q_j\ge1\), equations (3.5) and
(3.9) prove (3.3a) and
\[
 \|k_j\|_\infty\,
       \|\delta_0^*\beta_0 k_j\|_2=o(\sqrt{Q_j}).       \tag{3.10}
\]
Thus these actual examples are already covered by the approximate
criterion of I52, Corollary 11. They do not refute that criterion
or show that moving centers is the only way to retain coefficient
four. What fails is the attempted replacement of a small residual
by a uniformly controlled exact fixed-base harmonic slice.
If a chosen regular chart or cutoff has constants depending on \(j\),
choose the displacement first so that the resulting
\(C_j|\epsilon_j|\to0\), and then the donor scales so that
\(C_j\delta_j(1+\sqrt{Q_j})\le C_j|\epsilon_j|\).
This is permitted by the fixed-\(j\), fixed-displacement argument
and does not change the exact-gauge exclusion.

**What the theorem does not say.** These are not sub-four metrics,
not failures of actual monopole supply, and not counterexamples to
I52 or to Yau26. It also does not exclude other useful gauges,
changing the background centers, or approximate gauge equations.
It rules out a precise proposed reduction to a fixed exact Bianchi
slice, even on competitive actual recovery metrics.

## 4. Retaining the centers gives a positive uniform extension

The obstruction above disappears for its explicit family if the centers
are moved with the background. Let \(\mathbf p\) be the marked centers
and local frames in the first construction and
\(\mathbf q=\psi_\epsilon(\mathbf p)\). The local isometry at each
affected center extends over the corresponding Burns donor using the
transported frame; the other donors are unchanged. Thus there is a
marked diffeomorphism between the two surgery manifolds with the exact
raw identity
\[
 b_{\epsilon,t}
     =\Psi_\epsilon^*b_t(g_X,\mathbf q).                       \tag{4.1}
\]
Negative Yamabe normalization commutes with pullback, by uniqueness, so
\[
 g_{\epsilon,t}
     =\Psi_\epsilon^*g_t(g_X,\mathbf q).                       \tag{4.2}
\]
This is an exact equivalence, not an approximate gauge assertion.
The family defeated a fixed center, not the full family of centers.

We next record the uniform statement which follows from the actual
estimates of I52; keeping it uniform is important when the number
and positions of the cores vary.

**Theorem 3 (uniform moving-center stability).** For each \(j\), let
\(K_j\) be a compact set of marked, pairwise distinct cluster-center
configurations and frames in the CH cover \(X_j\), with the fixed
counts \(k_j,\ell_j\). The enclosing balls are disjoint and lie
in uniformly controlled CH charts. There are recovery families
\(g_j^0(\mathbf p)\), \(\mathbf p\in K_j\), whose diagonal errors
are uniform on \(K_j\), such that the conclusion of I52, Theorem 9
holds for every choice \(\mathbf p_j\in K_j\), with constants
independent of these choices.

In particular, if \(a_j=\|k_j^{\mathrm{met}}\|_\infty\to0\) and
\(k_j^{\mathrm{met}}\) is TT relative to
\(g_j^0(\mathbf p_j)\), then
\[
 \liminf_j
 \frac{\mathcal E\!\left(\widehat{g_j^0(\mathbf p_j)
                                    +k_j^{\mathrm{met}}}\right)}
      {h_j}\ge4.                                             \tag{4.3}
\]
The same holds in the constant-scalar Bianchi version of I52.
The exact-gauge quadratic lower bound and equality criterion are
uniform as well. The symbol \(k_j^{\mathrm{met}}\) is a tensor and
is distinct from the blowup count \(k_j\).

**Proof.** For each fixed \(j\), compactness of \(K_j\) supplies a
positive minimum separation of its distinct cluster centers, not
a separation independent of \(j\). Choose enclosing radii below
that separation and so small that their fourth powers sum to
at most \(\varepsilon_jQ_j\), with \(\varepsilon_j\to0\).
Within the handle clusters use the further hierarchy (1.3).
All local metric and cutoff estimates take place in CH charts.
The number of cutoffs is \(O(Q_j)\); each has uniformly bounded
scale-invariant second-derivative cost.

The donor costs, scalar lower bound, and exterior convergence are
uniform over a compact configuration set at fixed \(j\).
For completeness, nonuniform exterior convergence would give
a sequence of configurations converging in \(K_j\).
After moving their finitely many centers by smooth chart
identifications, the capacity and negative-Yamabe uniqueness
proof of I52, Lemma 3, applies to the limiting configuration,
contradicting that failure. Local elliptic estimates give the
required exterior \(C^2\) convergence. The raw and normalized
Bach and Ricci-gradient errors are treated in the same finite
compact family. A common sufficiently small scale therefore
makes their errors at most \(\varepsilon_jQ_j\).
In particular impose the actual stronger exterior selection
\(P_{\rm ext}\le\varepsilon_j^2Q_j^2/A_j\), as well as
\(\|\operatorname{grad}P(g_j^0)\|_1\le\varepsilon_jQ_j\).
An exterior bound of only \(o(Q_j)\) would not justify that
near-stationarity statement.

The constants in the remaining I52 argument use only the universal
CH tensor gap, the bounded energy per donor, the disjoint cutoff
estimates, and these selected errors. They do not use the minimum
separation itself. Hence its graph estimate and square completion
give, uniformly in \(\mathbf p\),
\[
 P_{\mathrm{final}}\ge8\pi^2Q_j+c x_j^2
                         -C a_j^2Q_j-\varepsilon_jQ_j,        \tag{4.4}
\]
where \(x_j\) is the appropriate norm-preserving identified
linearization from I52. The same opposite-chirality conversion
proves (4.3). The matching expansion in the competitive case
gives the inherited equality criterion \(x_j^2=o(Q_j)\).
QED.

There need not be a global trivialization of the entire configuration
bundle of smooth manifolds. The assertions are fiberwise and invariant
under the marked local identifications. For the one-parameter family
in Theorem 2 a contractible chart of configurations suffices.

**Corollary 4 (conformal and diffeomorphism saturation).**
The lower bound (4.3) is unchanged if one takes any orientation-preserving
pullback and any positive smooth conformal multiple of its output.
Neither the conformal factor nor the diffeomorphism needs a uniform
coordinate bound.

**Proof.** Diffeomorphism invariance is exact. If \(\widehat g\)
is the negative constant-scalar representative of a conformal class
and \(g\) is any other representative, put
\[
 \delta=S(g)-S(\widehat g)\ge0,\qquad
 L=S(g)-\frac{(\int s_g)^2}{V(g)}\ge0.
\]
The four-dimensional conformal curvature identities give
\[
 P(g)=P(\widehat g)+\delta/12,\qquad
 R(g)=R(\widehat g)+\delta/3.
\]
Consequently
\[
 \mathcal E(g)=
 \frac{\mathcal E(\widehat g)R(\widehat g)+\delta/3+L}
      {R(\widehat g)+\delta/3}
 \ge \min\{\mathcal E(\widehat g),1\}.                         \tag{4.5}
\]
Since \(h_j\to0\), this inequality transfers (4.3), including cases
of noncompetitive conformal representatives. QED.

Theorems 2--3 belong together: a configuration family is genuinely
needed for the proposed uniformly controlled exact-slice description
of these explicit \(C^0\)-nearby recovery metrics, and the first-order
estimate is uniform when that variable is kept. The approximate
criterion supplies a separate fixed-base route for this example.
We have not proved that this modulated family covers all nearby
metrics, nor that every unrestricted near-minimizer lies near it.

## 5. The intrinsic continuation: matched collars without a global slice

A second route avoids a global harmonic slice. The
[complete companion proof](20260928_intrinsic_caps_and_stability.md)
constructs a full-curvature cap of cost
\(C(\int|\operatorname{Rm}|^2+\|g-e\|_\infty^2)\), matching the
actual outer collar exactly. Localized DeTurck smoothing supplies
an interior smooth band; a fixed-input frozen-collar estimate and
critical energy control complete the two matches.

No scalar normalization is needed. Directly, for
\(\mathcal E<1/2\), Chern--Gauss--Bonnet gives total curvature
\(O(\chi)=O(A_j)\). In \(L_j\) disjoint fixed-ratio bands around
each marked blowup, minimum-energy selection gives
\[
 \sum_i\int_{\mathcal A_{i,j}}|\operatorname{Rm}|^2
        \le C A_j/L_j=o(Q_j)\quad\text{if }L_jh_j\to\infty.
                                                               \tag{5.1}
\]
The annuli enclose designated blowups, not handles. Leave any
energy-bad cores unremoved; their count is \(o(Q_j)\) when
\(L_jh_j\to\infty\). The partial signature identity charges these
retained blowups explicitly. It gives
\[
 \mathcal E(g_j)\ge\frac{4h_j}{1+h_j}
                      -C/L_j-C(k_j/A_j)a_j^2.        \tag{5.1a}
\]
This proves the coefficient-four lower bound for arbitrary
\(C^0\)-nearby smooth competitors on selected long-annulus bases,
and computes the infimum in every shrinking \(C^0\) neighborhood.
It also allows \(o(Q_j)\) wholly unstructured blowups and only
mean-square small annular amplitudes.

The remaining all-metric question is whether unrestricted
near-minimizers possess enough such marked annuli. The cap itself
is no longer the missing step. No global conformal normalization
is used to infer zeroth-order closeness.

There is no static curvature-supremum estimate for arbitrary metrics
from these inputs. For example, on a fixed local annulus consider
\[
 g=dx_1^2+e^{2u(x_1)}dx_2^2+e^{-2u(x_1)}dx_3^2
                  +v(x_1)^2dx_4^2,\qquad
 v''=(2r^2-(u')^2)v,\quad v(0)=1,\ v'(0)=0.
\]
Its scalar curvature is exactly \(-4r^2\). With a compactly supported
slab \(u=a\psi((x_1-c)/\ell)\), on a bounded interval,
\[
 \|g-g_{\mathrm{Eucl}}\|_\infty
       =O(a+r^2+a^2/\ell),\qquad
 \int|\operatorname{Rm}|^2=O(a^2/\ell^3+r^4),\qquad
 \|\operatorname{Rm}\|_\infty\gtrsim a/\ell^2 .
                                                               \tag{5.2}
\]
Choose \(a=\ell^p\), \(3/2<p<2\), and \(r\to0\). Then the first
two quantities vanish while the last diverges. The estimates follow
from the multiply warped curvature formulas and the displayed ODE;
\(v\) stays positive because \(r^2+a^2/\ell\to0\).
This local test does not disprove a low-energy cap.

Positive-time Ricci smoothing is a possible construction tool, but
matching the original collar remains an extra step. Even using an
actual Ricci flow rather than DeTurck coordinates, a variable-time
graph \(g_\theta(x)=g(x,\theta(x))\) creates connection terms
\[
 B^k{}_{ij}
 =-g^{k\ell}\{\operatorname{Ric}_{j\ell}\theta_i
             +\operatorname{Ric}_{i\ell}\theta_j
             -\operatorname{Ric}_{ij}\theta_\ell\}.            \tag{5.3}
\]
Its curvature includes \(d\theta\,\nabla\operatorname{Ric}\),
\(\nabla^2\theta\,\operatorname{Ric}\), and
\(|d\theta|^2(\partial_t\operatorname{Ric}
                       +\operatorname{Ric}*\operatorname{Ric})\).
Pointwise smoothing bounds of size \(a/t\) alone give a
nonintegrable majorant near the hypersurface where \(\theta=0\).
These terms explain why positive-time smoothing alone was insufficient.
I53 instead uses a spatially localized flow with the full
\(\mathcal L_{qW}\) term, controls its integrated energy, and
then restores the original collar. It does not use a variable-time
graph or assert that the original metric has bounded curvature.

## 6. Status and classical inputs

The new actual counterexample is registered as X09. The uniform
moving-center and conformal extensions are recorded with I52,
not counted as several separate breakthroughs.

O11, the all-metric coefficient on the balanced family, remains open.
O10, the unrestricted actual weak zero-Weyl endpoint, also remains
open. The present theorem neither supplies a closed endpoint escape
nor rules one out. The continued endpoint equations are maintained
separately in the research record.

Classical inputs used here are the Burns/Schwarzschild recovery
construction and negative Yamabe theory already made explicit in
I52, the elementary harmonic-map identity (3.1), and Hartman's
negative-curvature uniqueness theorem. The core-position obstruction
and its actual balanced diagonal are the conclusions proved here.
No worldwide priority claim follows from this local derivation.

## Appendix A. The exact Schwarzschild donor has no negative gauge mode

The marked obstruction should not be attributed to an unverified
negative mode on the handle donor. Its vector Jacobi quadratic form
can be evaluated directly.

Write the four-dimensional Riemannian scalar-flat Schwarzschild metric as
\[
 g_S=\rho^2(dt^2+\gamma_{S^3}),\qquad
 \rho=2a\cosh t,\quad v=\tanh t,\quad \sigma=\operatorname{sech}^2t .
\]
Its coordinate Ricci components are
\(\operatorname{Ric}_{tt}=-3\sigma\) and
\(\operatorname{Ric}_{ab}=\sigma\gamma_{ab}\).
For a compactly supported vector field set
\[
 \mathcal Q_S(X)=\int
       (|\nabla X|^2-\operatorname{Ric}(X,X))\,dV .
\]
Decompose angular components by scalar gradients and coclosed vector
harmonics on the round unit \(S^3\). For a scalar harmonic \(Y\) with
\(\int Y^2=1\), \(-\Delta_\gamma Y=\lambda Y\),
\(\lambda=l(l+2)\), take
\(X=u(t)Y\partial_t+f(t)\nabla Y\).
Integration by parts in the radial first-derivative terms gives
\[
 \mathcal Q_S(X)=\int\rho^4\{
 u'^2+\lambda f'^2+(\lambda+2\sigma)u^2
       +\lambda(\lambda-4)f^2-4\lambda vuf\}\,dt .
\]
After \(z=\rho^2u\), \(y=\sqrt{\lambda}\rho^2f\), this is
\[
 \int\left\{z'^2+y'^2+
 \left\langle
 \begin{pmatrix}
 \lambda+4&-2\sqrt{\lambda}\,v\\
 -2\sqrt{\lambda}\,v&\lambda-2\sigma
 \end{pmatrix}
 \binom zy,\binom zy\right\rangle\right\}\,dt .          \tag{A.1}
\]
For \(\lambda\ge3\) the matrix minus the identity has nonnegative
diagonal and determinant
\[
       (\lambda-3)(\lambda+3-2v^2)\ge0 .
\]
The radial \(\lambda=0\) block is \(z'^2+4z^2\).
For a coclosed vector harmonic with rough eigenvalue \(\mu\), the
corresponding potential is \(\mu+2-2\sigma\).
Here \(\mu\ge2\): the integrated symmetric-gradient identity on
\(S^3\), with divergence zero and Ricci \(2\gamma\), gives
\(\int|\nabla V|^2\ge2\int|V|^2\).
These blocks exhaust the vector fields. Hence
\[
 \mathcal Q_S(X)\ge\int\rho^{-2}|X|^2\,dV .             \tag{A.2}
\]
Since
\(\operatorname{Ric}(X,X)\le\rho^{-2}|X|^2\), also
\[
 \mathcal Q_S(X)\ge\frac13
       \int(|\nabla X|^2+\rho^{-2}|X|^2)\,dV .         \tag{A.3}
\]
The inequality extends by cutoff density to this finite-energy
space. It excludes a finite-energy kernel or negative mode on the
exact donor. It says nothing about a uniform supremum estimate for
the strain of a gauge through an entire degenerating marked manifold;
Theorem 2 shows why that stronger statement needs different data.
