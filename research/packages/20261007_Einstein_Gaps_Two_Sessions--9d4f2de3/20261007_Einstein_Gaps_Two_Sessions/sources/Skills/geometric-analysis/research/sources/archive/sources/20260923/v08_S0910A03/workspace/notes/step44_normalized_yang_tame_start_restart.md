# Step 44: normalized Yang start, uniqueness, and restart

## 0. Scope

Let \((M,g_0)\) be a closed smooth manifold and let
\(\chi\in C^\infty(M)\), \(0\le\chi\le1\).  The equation is

\[
 \partial_tg=-2a(\operatorname{Ric}_g+g),
 \qquad a=\chi^2,
 \qquad g(0)=g_0.                                                \tag{0.1}
\]

The required short-time theorem is per datum: its time and constants may depend
on all smooth norms of \((g_0,\chi)\).  No uniformity over a collapsing sequence
is sought here.  Sequence-uniform estimates begin only after a smooth solution
has started.

The appropriate construction is Yang's transported-coefficient DeTurck system,
not coefficient regularization plus a small-cutoff Schauder argument.  Yang's
Theorem 8.2 proves smooth short-time existence for
\(\partial_tg=-2\chi^2\operatorname{Ric}_g\).  The source gives the exact
coupled metric/diffeomorphism equations and reduces nonlinear existence to a
smooth tame inverse for the linearized system.  The present task is to show
that the added term \(-2a g\) preserves that inverse and its uniqueness.

Source: `Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md`, lines 785--823.

## 1. Exact transported system and pullback

Fix Yang's invertible background symmetric tensor \(S\) (one may take
\(S=g_0\)).  For a hatted metric, use Yang's operators
\(\widehat G(S)\), \(\widehat\delta\), and \(\widehat\delta^*\).  Let

\[
 \widehat\chi=\chi\circ\varphi_t^{-1},
 \qquad \widehat a=\widehat\chi^2.
\]

The normalized coupled equations are

\[
 \partial_t\widehat g
 =-2\left[
    \widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
    -\widehat\delta^*\!\left(
       \widehat a\,S^{-1}\delta G(S)
     \right)
   \right],                                                     \tag{1.1}
\]

with Yang's diffeomorphism equation

\[
 \partial_t\varphi
 =-\chi^2\,\varphi_{t*}
   \left[S^{-1}\delta G(S)\right]^\sharp,
 \qquad \varphi_0=\mathrm{id}.                                  \tag{1.2}
\]

Here all hatted divergences, adjoints, sharps, and the gauge one-form are read
exactly as in Yang's equations (8.5)--(8.6).  The coefficient is transported;
it is not held fixed in (1.1).

Yang's gauge cancellation gives, for \(g=\varphi_t^*\widehat g\),

\[
 \frac d{dt}(\varphi_t^*\widehat g)
 =-2\varphi_t^*\left[
    \widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
   \right]
 =-2a(\operatorname{Ric}_g+g),                                  \tag{1.3}
\]

because \(\varphi_t^*\widehat a=a\).  The normalization does not alter the
gauge vector or the cancellation.

Two exact consistency tests follow immediately.

* If \(\operatorname{Ric}_{g_0}=-g_0\) and \(S=g_0\), then
  \((\widehat g,\varphi)=(g_0,\mathrm{id})\) is stationary.
* The vector field that enters the geometric pullback is the weighted generator
  encoded by Yang's system.  The unweighted DeTurck vector need not vanish where
  \(a=0\); only its weighted contribution does.

## 2. Linearization of the normalization

Work in a local chart on the diffeomorphism group and write the variations as
\((h,\psi)\).  Yang's unnormalized linearization has the schematic form

\[
 \partial_th
 =2\widehat\chi^2\Delta h
  +\widehat\chi(B\nabla h+C\nabla\psi)
  +Dh+E\psi+f,                                                   \tag{2.1}
\]

\[
 \partial_t\psi
 =-\widehat\chi^2(P\nabla\psi+Q\nabla h+Rh)+\eta.              \tag{2.2}
\]

All coefficients are smooth functions of the reference pair and finitely many
of its derivatives.  The new term is

\[
 \delta(-2\widehat a\,\widehat g)
 =-2\widehat a\,h-2(\delta\widehat a)\widehat g.                 \tag{2.3}
\]

If \(\zeta=\delta\varphi\circ\varphi^{-1}\), then

\[
 \delta\widehat\chi=-d\widehat\chi(\zeta),
 \qquad
 \delta\widehat a=-2\widehat\chi\,d\widehat\chi(\zeta).        \tag{2.4}
\]

Thus (2.3) adds only

\[
 \widehat\chi^2*h
 \quad\text{and}\quad
 \widehat\chi\,d\widehat\chi*\psi                              \tag{2.5}
\]

with no derivative of \(h\) or \(\psi\).  In particular, it preserves the one-
cutoff-factor structure of (2.1) and changes only Yang's lower-order coefficient
matrices.

## 3. Regularized linear inverse with uniform Sobolev estimates

Following Yang Approach 1, regularize only the linearized metric equation:

\[
 \partial_th
 =2\widehat\chi^2\Delta h+\varepsilon^2\Delta h
  +\widehat\chi(B\nabla h+C\nabla\psi)
  +\widetilde D h+\widetilde E\psi+f,                            \tag{3.1}
\]

while keeping (2.2).  For each \(\varepsilon>0\), this is a strictly parabolic--
transport system with a unique smooth solution.  The useful point is that the
energy constants below do not depend on \(\varepsilon\).

Choose a fixed smooth reference connection and volume form; all changing
coefficients are then absorbed into the smooth matrices in (3.1)--(2.2).
For integer \(k\ge0\), set

\[
 \mathcal E_k(t)=\|h(t)\|_{H^k}^2+A_k\|\psi(t)\|_{H^k}^2.        \tag{3.2}
\]

The constant \(A_k>0\) is fixed large enough to absorb the coupled terms.
Differentiating up to order \(k\) gives the following top-order allocations.

### 3.1 Metric diffusion

Integration by parts gives

\[
 2\langle\nabla^kh,\nabla^k(\widehat\chi^2\Delta h)\rangle
 \le-c\|\widehat\chi\nabla^{k+1}h\|_2^2
    +C_k\|h\|_{H^k}^2.                                         \tag{3.3}
\]

The only top cutoff derivative created in this integration is
\(\nabla(\widehat\chi^2)=2\widehat\chi\,d\widehat\chi\); it is absorbed by
weighted dissipation.  Terms in which two or more derivatives hit a smooth
coefficient contain at most \(k\) derivatives of the unknown and are lower
order.  The regularizer contributes

\[
 -c\varepsilon^2\|\nabla^{k+1}h\|_2^2+C_k\varepsilon^2\|h\|_{H^k}^2. \tag{3.4}
\]

### 3.2 First-order metric terms and the metric--transport coupling

The \(\widehat\chi B\nabla h\) term is absorbed exactly as in (3.3).  For the
apparently derivative-losing term, retain its contraction and integrate once:

\[
 \int\nabla^kh*\widehat\chi C\nabla^{k+1}\psi
 =-\int\widehat\chi C\nabla^{k+1}h*\nabla^k\psi
  -\int\nabla(\widehat\chi C)\nabla^kh*\nabla^k\psi.             \tag{3.5}
\]

Consequently,

\[
 |(3.5)|\le\rho\|\widehat\chi\nabla^{k+1}h\|_2^2
           +C_{k,\rho}(\|h\|_{H^k}^2+\|\psi\|_{H^k}^2).         \tag{3.6}
\]

No \(H^{k+1}\) norm of \(\psi\) remains.

### 3.3 Transport equation

Here Yang's symbol $P\nabla\psi$ must be read with its actual transport
structure, not as an arbitrary matrix first-order system.  At top order it is
covariant differentiation along a smooth vector field (equivalently, it has a
smooth symmetrizer), so

\[
 \int\langle\nabla^k\psi,
       \widehat a V^i\nabla_i\nabla^k\psi\rangle
 =-\frac12\int\operatorname{div}(\widehat aV)|\nabla^k\psi|^2
   +\text{lower-order commutators}
 \le C_k\|\psi\|_{H^k}^2.                                      \tag{3.7}
\]

This transport/symmetrizer property is inherited from Yang's exact
linearization; equation (3.7) would not follow for a general unsymmetrized
matrix $P$.  The coupling to \(h\) obeys

\[
 \left|\int\nabla^k\psi*\widehat\chi^2Q\nabla^{k+1}h\right|
 \le\rho\|\widehat\chi\nabla^{k+1}h\|_2^2+C_{k,\rho}\|\psi\|_{H^k}^2. \tag{3.8}
\]

The remaining differentiated commutators contain at most \(k\) derivatives of
\((h,\psi)\), with smooth per-datum coefficients.

### 3.4 New normalization terms

By (2.5), for every \(k\),

\[
 \left|\left\langle\nabla^kh,
   \nabla^k(\widehat\chi^2h+
             \widehat\chi d\widehat\chi*\psi)
 \right\rangle\right|
 \le C_k(\|h\|_{H^k}^2+\|\psi\|_{H^k}^2).                       \tag{3.9}
\]

They create neither derivative loss nor any inverse power of \(\widehat\chi\).

### 3.5 Uniform estimate and removal of the linear regularizer

After summing orders \(0,\ldots,k\), first fixing the energy weight $A_k$ and
then choosing each Young parameter small relative to that fixed weight (the
transport couplings are themselves multiplied by $A_k$),

\[
 \boxed{
 \frac d{dt}\mathcal E_k
 +c_k\|\widehat\chi\nabla^{k+1}h\|_2^2
 +c_k\varepsilon^2\|\nabla^{k+1}h\|_2^2
 \le C_k\mathcal E_k
   +C_k(\|f\|_{H^k}^2+\|\eta\|_{H^k}^2).}                       \tag{3.10}
\]

The constants depend on a bounded set of smooth reference pairs and on the full
smooth cutoff, but not on \(\varepsilon\).  Standard commutator interpolation
puts the dependence on the reference pair in the same smooth tame form used by
Yang.  Gronwall yields the tame inverse estimate.  Applying (3.10) at every
order, the regularized solutions have uniform spatial Sobolev bounds; the
equations give uniform time-derivative bounds two orders lower.  Compactness on
the closed manifold gives a smooth limit as \(\varepsilon\downarrow0\), solving
(2.1)--(2.2).  The \(\varepsilon^2\Delta h\) term vanishes in every fixed lower
Sobolev topology.

This is the relevant regularization-uniform statement.  It does not assert that
a coefficient-regularized nonlinear flow has uniform Schauder estimates near
\(\{a=0\}\).

### 3.6 What remains to make the inverse self-contained

The same-order estimate (3.10) proves the regularized linear solve and its
smooth limit, but a stand-alone Nash--Moser proof also needs the high--low tame
form, uniformly for reference pairs in a smooth neighborhood.  Schematically,
with $u=(\widehat g,\varphi)$ and fixed low index $k_0>n/2+2$,

\[
 \mathcal E_k'
 \le C(\|u\|_{H^{k_0+r}})\mathcal E_k
 +C_k(1+\|u\|_{H^{k+r}})\mathcal E_{k_0}
 +\text{high--low forcing terms},                               \tag{3.11}
\]

with a loss $r$ independent of $k$.  One also needs the corresponding time
norms and smooth-tame dependence of the inverse on $u$.  Yang's Theorem 8.2
asserts precisely that the unnormalized system has this smooth tame inverse,
but the published proof excerpt compresses it into “standard arguments.”  The
normalization preserves it because

\[
 \|\widehat a h\|_{H^k}
 \lesssim\|\widehat a\|_{H^{k_0}}\|h\|_{H^k}
          +\|\widehat a\|_{H^k}\|h\|_{H^{k_0}},                 \tag{3.12}
\]

and the composition term
$\widehat\chi d\widehat\chi*(\psi\circ\varphi^{-1})$ obeys the same standard
smooth-tame product/composition estimate already required for Yang's
transported coefficient.  Thus the incremental normalized adaptation is
proved; a completely self-contained reconstruction of Yang's neighborhood-
uniform tame inverse is still not contained in this note.

## 4. Nonlinear short-time theorem

Yang's proof of Theorem 8.2 states that the nonlinear fixed-point or Nash--Moser
construction reduces to a unique smooth solution of the linearized system with
smooth tame estimates.  Equations (2.3)--(3.12) show that, **on importing
Yang's asserted neighborhood-uniform smooth tame inverse**, the normalized
operator has the same principal coupled system and preserves that inverse: its
new term is a zeroth-order smooth-tame perturbation.  Applying Yang's
construction therefore gives:

**Normalized local-flow theorem.**  There exists
\(T=T(g_0,\chi)>0\) and a smooth solution \((\widehat g,\varphi)\) of
(1.1)--(1.2) on \([0,T]\).  Its pullback \(g=\varphi^*\widehat g\) is a smooth
solution of (0.1).

The theorem is global on the closed manifold but per datum.  In particular, it
allows arbitrary smooth geometry in \(\{a\ll1\}\); no small-displacement
argument is used there.  This conclusion is a rigorous reduction to Yang's
published Theorem 8.2 plus the explicit lower-order perturbation check, rather
than a self-contained reproof of every high--low tame estimate hidden in
Yang's compressed exposition.

## 5. Coupled uniqueness

Two nearby solutions \((\widehat g_1,\varphi_1)\) and
\((\widehat g_2,\varphi_2)\) with the same initial pair are compared in a common
local chart on metrics and diffeomorphisms.  Integrating the differential of the
nonlinear operator along the segment between the two pairs produces a linear
system of the form (2.1)--(2.2), including

\[
 \widehat a_1-\widehat a_2
 =-2\widehat\chi\,d\widehat\chi*(\varphi_1-\varphi_2)
  +\text{smooth quadratic remainder}.                            \tag{5.1}
\]

Thus metric and transport differences must be estimated together.  Applying
(3.10) with zero forcing and zero initial data yields
\(\mathcal E_k(t)=0\), hence both differences vanish.  Equivalently, use the
exact mean-value identity
$\Phi(u_1)-\Phi(u_2)=\int_0^1D\Phi(u_s)(u_1-u_2)\,ds$ in a common local chart,
rather than truncating the coefficient difference at linear order.  This
argument does not assume that the ordinary DeTurck vector vanishes on
\(\{a=0\}\).

The corresponding geometric solution is locally unique: gauge two geometric
solutions with the same initial metric into the same Yang system, apply coupled
uniqueness, and pull back.

## 6. Restart and interaction with continuation

Suppose a solution on \([0,T_*)\) has a positive-definite smooth limit
\(g_*\) as \(t\uparrow T_*\).  Apply the normalized local-flow theorem to the
smooth datum \((g_*,\chi)\), with a newly chosen background tensor
\(S=g_*\).  There need not be a temporal overlap.  Because the equation is autonomous and
$g(t)\to g_*$ in $C^\infty$, the left time derivatives satisfy
$\partial_t^jg(t)\to\mathcal F_j(g_*)$ recursively; the restarted solution has
the same right time jets.  Hence the two pieces glue smoothly at $T_*$.  Local
geometric uniqueness then makes the extension unique.

Together with `step44_zero_order_T_seed_repair.md` and the Step 40 staggered
finite-exponent induction, this supplies the start/restart interface for the
restricted four-dimensional smoothing construction.

## 7. What is and is not supplied

The argument above establishes the mathematical adaptation actually needed
from Yang, conditional only on importing the smooth-tame inverse asserted in
Yang's theorem:

* the transported coefficient and weighted gauge are retained exactly;
* the normalization has a one-cutoff-factor variation and is lower order;
* the coupled \((h,\psi)\) same-order estimate is uniform in Yang's linear regularizer;
* the normalization obeys the high--low product/composition bounds and therefore
  preserves Yang's smooth-tame inverse, although that inverse is not reconstructed
  fully from the compressed source proof here;
* uniqueness treats metric and transport differences together;
* restart is per datum and follows from the same theorem.

It does not obtain the sequence-uniform observation time.  That time comes from
the separate weighted curvature/defect estimates and first-exit improvement.
Nor does this restricted smoothing construction address the positive branch,
arbitrary four-manifold topology, dimensions \(n\ge5\), dimension-only
constants, or Lean formalization required by the full Yau Problem 26.
