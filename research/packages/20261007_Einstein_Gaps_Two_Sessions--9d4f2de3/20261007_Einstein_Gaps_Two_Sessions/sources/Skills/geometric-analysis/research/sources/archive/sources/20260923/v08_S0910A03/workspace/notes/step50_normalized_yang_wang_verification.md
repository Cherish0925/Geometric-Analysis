# Step 50: normalized start attempt and coupled Wang continuation

> **Start superseded by Step 52.** The transported lower-order variation in §2
> is algebraically correct, but the full neighborhood-uniform tame inverse was
> not established here, and Step 51 did not repair it.  The per-datum start is
> now supplied instead by the normalized extension of Guoyi Xu's detailed
> fixed-point construction in `step52_normalized_local_flow_start_repair.md`.
> The shifted-curvature/cutoff-jet continuation in §3 remains a separate
> positive-time construction and is not superseded by this notice.

Session: S0910A03. Agent4 / Preceptor. Phase: Execute.

## 0. Mathematical outcome

Consider the exact normalized cutoff flow on a closed smooth manifold

\[
 \partial_t g=-2a(\operatorname{Ric}_g+g),\qquad a=\chi^2,
 \qquad g(0)=g_0. \tag{0.1}
\]

The Step 49 construction mixed two different arguments. Its direct appeal to
Yang can be made precise and is the correct short-time construction. Its
coefficient-regularized nonlinear argument cannot be used: metric equivalence
does not bound the evolving connection, an unweighted critical curvature
energy does not bound curvature pointwise, and covariant derivatives of the
fixed scalar \(a\) are evolving tensors. The statements in Step 49 that
\(\nabla_g^{m+2}a\) is a prescribed bounded source are therefore removed.

There is a clean separation.

1. **Start and restart.**  Add the normalization directly to Yang's transported-
   coefficient DeTurck system. Its linearization changes exactly the lower-order
   \(Dh+E\psi\) slots displayed in Yang's proof. Sobolev multiplication and
   composition estimates show that the smooth-tame inverse has the same fixed
   derivative loss and neighborhood-uniform constants. This gives a smooth
   per-datum exact flow without passing through nonlinear
   \(a+\varepsilon^2\) flows.
2. **Positive-time continuation.**  Higher cutoff jets remain coupled unknowns.
   Introduce the shifted curvature
   \[
   G={g\owedge g\over2(n-1)},\qquad T=\operatorname{Rm}+G,
   \qquad U=aT.
   \]
   Then \(\operatorname{Ric}(T)=\operatorname{Ric}+g\) and
   \(\partial_tg=-2\operatorname{Ric}(U)\).  The Wang hierarchy must propagate
   \((U_m,C_{m+1})\) together, followed by \(T_m\), where
   \(U_m=\nabla^mU\) and \(C_j=\nabla^j\chi\).  This is precisely the coupling
   suppressed by Step 49.

The arguments below establish the source-level normalized Yang perturbation and
state the continuation proof through the coupled energy inequalities already
derived in Steps 40, 44, and 45. They do not use nonlinear coefficient
regularization to start the exact flow.

---

## 1. Why the Step 49 nonlinear regularization argument fails

### 1.1 Metric equivalence does not control cutoff jets

For a fixed scalar \(a\),

\[
 (\nabla_g^2a)_{ij}=\partial_i\partial_ja-\Gamma(g)^k{}_{ij}\partial_ka.
 \tag{1.1}
\]

A bilipschitz comparison \(\Lambda^{-1}g_0\le g\le\Lambda g_0\) controls
neither \(\Gamma(g)\) nor any positive derivative of \(g\). Consequently it
does not control \(\nabla_g^2a\), much less \(\nabla_g^ka\). Step 49
§1.3(c), §2.3, §3.2, and §5.2 cannot treat these tensors as prescribed bounded
coefficients.

### 1.2 Critical curvature energy is not a pointwise curvature estimate

In dimension four,

\[
 \|\operatorname{Rm}\|_{L^2}
\]

is scale-critical. Metric equivalence and an \(L^2\) curvature bound do not
imply an \(L^\infty\) bound on \(\operatorname{Ric}\). More generally, an
\(L^p\) bound with \(p>n/2\) and no derivative information still does not by
itself bound a function pointwise. Thus Step 49 §4.2 does not establish metric
drift from its displayed curvature energy.

### 1.3 The nonlinear \(a+\varepsilon^2\) route is unnecessary for the start

For each fixed \(\varepsilon>0\), the DeTurck equation is strictly parabolic.
Uniform passage as \(\varepsilon\downarrow0\), however, requires the very
cutoff-jet, weighted-curvature, unweighted-curvature, and fixed-coordinate
estimates whose propagation was left incomplete. Interior estimates on
\(\{\chi>0\}\) do not control jets across
\(\partial\operatorname{supp}\chi\). Yang's direct degenerate construction
avoids this circularity.

---

## 2. Exact normalized perturbation of Yang's transported system

### 2.1 Nonlinear hatted equations

Use Yang's background invertible symmetric tensor \(S\), and put

\[
 \widehat\chi=\chi\circ\varphi^{-1},\qquad
 \widehat a=\widehat\chi^2.
\]

Replace Yang's metric equation by

\[
 \partial_t\widehat g
 =-2\left[\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
 -\widehat\delta^*\!\left(
 \widehat aS^{-1}\delta G(S)\right)\right], \tag{2.1}
\]

and retain Yang's diffeomorphism equation. The gauge cancellation is unchanged.
For \(g=\varphi^*\widehat g\),

\[
 {d\over dt}(\varphi^*\widehat g)
 =-2\varphi^*\left[\widehat a
 (\operatorname{Ric}_{\widehat g}+\widehat g)\right]
 =-2a(\operatorname{Ric}_g+g). \tag{2.2}
\]

Thus a smooth solution of (2.1) and Yang's transport equation gives the exact
geometric equation (0.1), with no coefficient limit.

### 2.2 Exact linearization of the added term

Let \(h=\delta\widehat g\). For the diffeomorphism variation use the Eulerian
field

\[
 \zeta=\delta\varphi\circ\varphi^{-1}.
\]

The transported scalar satisfies

\[
 \delta\widehat\chi=-d\widehat\chi(\zeta),\qquad
 \delta\widehat a=-2\widehat\chi\,d\widehat\chi(\zeta). \tag{2.3}
\]

Therefore the variation of the added evolution term is exactly

\[
 \boxed{
 \delta(-2\widehat a\widehat g)
 =-2\widehat a h
 +4\widehat\chi\,d\widehat\chi(\zeta)\widehat g.} \tag{2.4}
\]

There is no derivative of \(h\) or \(\zeta\). Yang writes the unnormalized
linearized system as

\[
 \begin{aligned}
 \partial_th&=2\widehat\chi^2\Delta h
 +\widehat\chi(B\nabla h+C\nabla\psi)+Dh+E\psi+f,\\
 \partial_t\psi&=-\widehat\chi^2(P\nabla\psi+Q\nabla h+Rh)+\eta.
 \end{aligned} \tag{2.5}
\]

After identifying \(\zeta\) with \(\psi\) by right translation in the chosen
chart on the diffeomorphism group, (2.4) only replaces

\[
 D\mapsto D-2\widehat a\,\mathrm{Id},\qquad
 E\mapsto E+4\widehat\chi\,d\widehat\chi(\,\cdot\,)\widehat g. \tag{2.6}
\]

This is stronger than a principal-symbol observation: the new terms occupy the
same two lower-order coefficient slots explicitly allowed in Yang's displayed
system. The variation of the transported coefficient already appears in Yang's
unnormalized term \(\widehat a\operatorname{Ric}_{\widehat g}\), so (2.6)
introduces no new composition type.

### 2.3 Sobolev multiplication and composition in Yang's spaces

Let \(s_0>n/2+2\), and use the staggered Sobolev grading
\[
 \|u\|_s^*=\|\widehat g\|_{H^s}+\|\varphi\|_{H^{s+1}},
 \qquad u=(\widehat g,\varphi), \tag{2.7a}
\]
underlying Yang's stated \(C^0([0,T],H^s(M))\) construction. On a fixed
bounded neighborhood \(\mathcal U\) of smooth pairs, require uniform positive
definiteness of \(\widehat g\) and that \(\varphi\) remain in the
\(H^{s_0+1}\) diffeomorphism neighborhood of the identity. Standard Moser
multiplication gives, for \(s\ge s_0\),

\[
 \|uv\|_{H^s}
 \le C_{\mathcal U}\bigl(
 \|u\|_{H^{s_0}}\|v\|_{H^s}
 +\|u\|_{H^s}\|v\|_{H^{s_0}}\bigr). \tag{2.7}
\]

Sobolev composition and inversion on this neighborhood give

\[
 \|\chi\circ\varphi^{-1}\|_{H^{s+1}}
 \le C_{s,\mathcal U}\bigl(1+\|\varphi\|_{H^{s+1}}\bigr), \tag{2.8}
\]

because \(\chi\) is fixed and smooth. Right translation between \(\psi\) and
\(\zeta\) obeys the corresponding tame estimate. Combining (2.7)--(2.8), the
new linear operator

\[
 K_u(h,\psi)=
 \left(-2\widehat a h
 +4\widehat\chi d\widehat\chi(\zeta)\widehat g,0\right) \tag{2.9}
\]

satisfies, for a fixed finite loss \(r\) already sufficient for Yang's
coefficients,

\[
 \|K_u(h,\psi)\|_{H^s}
 \le C_{\mathcal U}\|(h,\psi)\|_{H^s}
 +C_{s,\mathcal U}
 (1+\|u\|_{s+r}^*)\|(h,\psi)\|_{H^{s_0}}. \tag{2.10}
\]

The same estimate holds in Yang's time-dependent norm and for differences of
reference pairs. No spatial derivative of the unknown is introduced by \(K_u\),
so the loss \(r\) is unchanged.

### 2.4 Stability of Yang's linear inverse

Yang constructs the inverse by adding \(\varepsilon^2\Delta h\) to the first
line of (2.5), proving energy estimates independent of \(\varepsilon\), and
letting \(\varepsilon\downarrow0\). One must solve the perturbed regularized
system directly; no small-operator assertion for \(L_u^{-1}K_u\) is being made.
At Sobolev order \(s\), the contribution of (2.9) to the differentiated energy
has the high--low form

\[
 |\langle\nabla^sh,\nabla^sK_u(h,\psi)\rangle|
 \le C_{\mathcal U}\mathcal E_s
 +C_{s,\mathcal U}(1+\|u\|_{s+r}^*)
 \mathcal E_{s_0}^{1/2}\mathcal E_s^{1/2}. \tag{2.11}
\]

It contains no term competing with the weighted dissipation
\(\|\widehat\chi\nabla^{s+1}h\|_2^2\), and its constants are independent of
the linear regularizer. At order \(s_0\), Gronwall closes the estimate. At
higher order, (2.11) is exactly a smooth-tame high--low term. Hence the
regularized linear solve, removal of the linear regularizer, uniqueness, and
smooth-tame dependence proceed with the same derivative loss as in Yang.

This argument uses Yang's published smooth-tame inverse for the original
coefficients \(B,C,D,E,P,Q,R\); it does not reconstruct that published theorem.
In particular, Yang's excerpt compresses the symmetrizer for the \(\psi\)-transport,
the inhomogeneous time-dependent inverse, reference-pair difference estimates,
and higher Fréchet-parameter estimates into “standard arguments.” What is proved
here is the incremental statement: the normalization lies in the displayed
lower-order class, its directly regularized linear equation has the same
energy allocation, and it introduces neither a new composition type nor a
larger finite derivative loss.

### 2.5 Normalized Yang theorem

**Proposition 2.1 (normalized start as a strict reduction to Yang's tame
inverse).** Let \(M\) be closed, \(g_0\) smooth, and \(\chi\) smooth. Import
Yang's neighborhood-uniform smooth-tame inverse, including its transport
symmetrizer and time norms. Then there is \(T=T(g_0,\chi)>0\) and a smooth
solution of (0.1) on \([0,T]\). The metric is stationary on the interior of
\(\{\chi=0\}\). The same construction starts from any smooth positive-definite
terminal metric.

**Reason.** Yang's nonlinear fixed-point or Nash--Moser construction reduces to
the neighborhood-uniform inverse for (2.5). Equations (2.4) and (2.7)--(2.11)
show, by directly solving the perturbed regularized linear system, that the
normalized operator has the same tame estimates on a possibly smaller
neighborhood and time interval. Pullback gives (0.1) by (2.2). This is a direct
perturbation of Yang's Approach 1; no assertion about nonlinear
\(a+\varepsilon^2\) flows is used. A completely self-contained reconstruction
would still have to write Yang's compressed transport symmetrization,
inhomogeneous inverse, neighborhood-difference hierarchy, and higher parameter
derivatives.

---

## 3. Continuation requires the evolving cutoff jets

### 3.1 Shifted variables and metric control

Set

\[
 G={g\owedge g\over2(n-1)},\qquad T=\operatorname{Rm}+G,
 \qquad U=aT. \tag{3.1}
\]

With the standard Ricci contraction, \(\operatorname{Ric}(G)=g\), hence

\[
 \operatorname{Ric}(T)=\operatorname{Ric}+g,
 \qquad \operatorname{Ric}(U)=a(\operatorname{Ric}+g),
 \qquad \partial_tg=-2\operatorname{Ric}(U). \tag{3.2}
\]

If \(\sup|a\operatorname{Rm}|\le K\) on \([0,T_*)\), then \(|U|\le K+C_n\).
Equation (3.2) yields

\[
 e^{-C_n(K+1)t}g_0\le g(t)\le e^{C_n(K+1)t}g_0, \tag{3.3}
\]

so the metrics, volumes, Sobolev constants, and \(|d\chi|\) are uniformly
controlled. No higher cutoff jet follows from (3.3).

### 3.2 Exact coupled hierarchy

Write

\[
 B_j=\nabla^ja,\qquad C_j=\nabla^j\chi,
 \qquad T_j=\nabla^jT,\qquad U_j=\nabla^jU.
\]

The coordinate-time equations have the division-free structure

\[
 \partial_tT=a\Delta T+B_1*\nabla T+B_2*T
 +a(T*T+T+1), \tag{3.4}
\]

\[
 \partial_tU=a\Delta U+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+aU+a^2. \tag{3.5}
\]

Moreover,

\[
 \partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U), \tag{3.6}
\]

and, because \(\chi\) is fixed only as a scalar function,

\[
 \partial_t C_{m+1}
 =\sum_{r+s=m-1}U_{r+1}*C_{s+1}\qquad(m\ge1), \tag{3.7}
\]

up to tensor-slot permutations and lower curvature commutators. Thus the current
term in (3.7) is \(U_m*C_1\). This is why \(C_{m+1}\) must be estimated with
\(U_m\), not declared bounded in advance.

The coefficient expansion is

\[
 B_j=2\chi C_j+
 \sum_{1\le q\le j-1}C_q*C_{j-q},\qquad
 {|B_1|^2\over a}=4|C_1|^2. \tag{3.8}
\]

Every highest single cutoff jet \(C_{m+2}\) in the \(U_m\) equation therefore
carries \(\chi\) and multiplies an algebraic contraction of \(U_0\). This is
the source of the signed integrations below.

### 3.3 Base unweighted curvature energy

For every finite \(p\ge2\), testing (3.4) against \(|T|^{p-2}T\), retaining
the \(B_2*T\) contraction with its sign, and integrating it once by parts gives

\[
 {d\over dt}\|T\|_p^p
 +c_p\int a|\nabla T|^2|T|^{p-2}
 \le C_p(K+1+\|d\chi\|_\infty^2)\|T\|_p^p+C_p\operatorname{Vol}. \tag{3.9}
\]

Here the quadratic term uses
\(a|T|^{p+1}=|U||T|^p\), and
\(|B_1|^2/a=4|d\chi|^2\). No Hessian cutoff bound is used. Gronwall supplies
\(T_0\in L^p\) uniformly up to \(T_*\) for every finite \(p\).

### 3.4 Staggered finite-exponent propagation

At stage \(m\ge1\), first test the differentiated \(U_m\) equation together
with (3.7). The only current first derivative is \(B_1*U_{m+1}\), absorbed by
weighted dissipation using (3.8). A current \(B_2*U_m\) term is integrated by
parts. A highest jet has the form

\[
 \chi C_{m+2}*\mathcal A(U_0)*|U_m|^{p-2}U_m. \tag{3.10}
\]

One integration lowers it to \(C_{m+1}\); the residual
\(\chi C_{m+1}*U_1*|U_m|^{p-2}U_m\) is integrated once more when \(m\ge2\).
At \(m=1\) it is the same signed-Hessian contraction. All larger finite
exponents fall on already completed spatial levels. This yields

\[
 {d\over dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
 +c_{m,p}\int a|\nabla U_m|^2|U_m|^{p-2}
 \le C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr). \tag{3.11}
\]

After (3.11), test the \(T_m\) equation. Its highest new cutoff jet is
\(2\chi C_{m+2}*T_0\); one signed integration lowers it to the now known
\(C_{m+1}\). Current quadratic curvature terms carry \(aT_0=U_0\), while time
commutators use \(U_m\) and previous \(T\)-levels in finite Hölder exponents.
Thus

\[
 {d\over dt}\|T_m\|_p^p
 +c_{m,p}\int a|\nabla T_m|^2|T_m|^{p-2}
 \le C_{m,p}(1+\|T_m\|_p^p). \tag{3.12}
\]

The order is

\[
 T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
 \longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots. \tag{3.13}
\]

Equations (3.9), (3.11), and (3.12) are the required correction to Step 49:
higher cutoff jets are produced by the flow and controlled as members of the
coupled hierarchy.

### 3.5 Fixed-coordinate endpoint

Choose \(\bar\nabla=\nabla^{g(0)}\) and set
\(A=\nabla^g-\bar\nabla\). From (3.2),

\[
 \partial_tA=g^{-1}*\nabla\operatorname{Ric}(U). \tag{3.14}
\]

Taking \(p>n\) and one extra spatial level in (3.11)--(3.12), uniform Sobolev
embedding gives pointwise bounds for all \(U_m,C_m,T_m\). Choose \(p>\max\{n,100\}\) and use one or two additional spatial levels from
the all-order induction; scalar Sobolev embedding and Kato then give pointwise
bounds for every covariant derivative. Equation (3.14), together with
\(\bar\nabla=\nabla+A*\), gives inductively

\[
 \sup_{t<T_*}\|\bar\nabla^kA(t)\|_\infty<\infty,
 \qquad
 \sup_{t<T_*}\|\partial_t\bar\nabla^kg(t)\|_\infty<\infty
 \quad(k\ge0). \tag{3.15}
\]

Hence \(g(t)\) is Cauchy in every fixed-background \(C^k\) norm as
\(t\uparrow T_*\). Its limit is smooth and positive definite by (3.3). Proposition 2.1 restarts the equation once Yang's tame inverse is imported.
Autonomy recursively matches all time jets at the joining time.

**Theorem 3.1 (normalized Wang terminal regularity and conditional restart).**
A smooth solution of (0.1) on \([0,T_*)\), \(T_*<\infty\), which satisfies
\(\sup_{M\times[\tau,T_*)}|a\operatorname{Rm}|<\infty\) for some
\(0<\tau<T_*\), converges in every fixed-background \(C^k\) norm to a smooth
positive-definite terminal metric. Upon importing Proposition 2.1's Yang tame
inverse, it extends smoothly past \(T_*\).

The proof uses (3.9)--(3.15), not a bound on prescribed cutoff derivatives.
It is a shifted-curvature adaptation of Wang's Theorem 4.1. In particular, the
normalization is absorbed into the identity \(\partial_tg=-2\operatorname{Ric}(U)\).

---

## 4. Consequence for the current negative route

If the exact-flow Moser estimate

\[
 \|a\operatorname{Rm}(t)\|_\infty\le {C\gamma\over t}
 \qquad(0<t<T)
\]

holds throughout a first-exit interval, it is bounded on every terminal slab
\([T_*/2,T_*)\). Theorem 3.1 then gives a smooth terminal metric, and Proposition 2.1 supplies
the restart after importing Yang's tame inverse. This use does not integrate
\(1/t\) at zero.

The transported-coefficient calculation alone did not remove the per-datum
start obstacle.  Step 52 subsequently supplies that start through a different
route: Xu's detailed fixed-point construction with the explicit algebraic
reaction \(-2\chi^2V\).  The restricted Ishida--LeBrun gap still should not be
promoted here: its sequence-uniform first-exit estimates and terminal attachment
must be re-read on the corrected start and the coupled continuation above. Nothing here addresses the positive
branch, arbitrary four-manifold topology, dimensions at least five,
dimension-only forcing constants, or Lean formalization.

## 5. Source and artifact dependencies

- Yang, Theorem 8.2 and its displayed linearized system: Knowledge object
  `Convergence-of-riemannian-manifolds-with-integral-bounds`, lines 785--823.
- Wang, Theorem 4.1 and Lemmas 4.4--4.14: Knowledge object
  `Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature`, lines
  392--661.
- Direct normalized tame perturbation developed in
  `workspace/notes/step44_normalized_yang_tame_start_restart.md`.
- Zero-order shifted-curvature estimate in
  `workspace/notes/step44_zero_order_T_seed_repair.md`.
- Coordinate-time tensor families and fixed-coordinate connection mechanism in
  `workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md`.
- Arbitrary-order signed integrations in
  `workspace/notes/step40_staggered_all_order_continuation_candidate.md`.
