# Step 67: corrections and reopening of the curved-neck problem

Session: S0910A03. Phase: Explore.

This note supersedes the affected conclusions of Steps 65–66 without deleting their scripts, numerical data, or valid flat-slice calculation. Group correction: message #478.

## 1. Corrections to the active mathematical record

### 1.1 Negative Ricci on the three-torus

The Step 66 assertion that Preissmann forbids a metric
\(\operatorname{Ric}_\gamma<-(4/3)\gamma\) on \(T^3\) is false. Preissmann concerns strictly negative **sectional** curvature. In dimension three,
\[
K_{ij}=\frac{\rho_i+\rho_j-\rho_k}{2}
\]
for Ricci eigenvalues \(\rho_1,\rho_2,\rho_3\); e.g. \((-2,-2,-10)\) gives \(K_{12}=3\). Lohkamp's negative-Ricci theorem applies to every closed manifold of dimension at least three, hence to \(T^3\); after a constant rescaling a compact negative-Ricci metric can satisfy any prescribed one-sided negative upper bound. This supplies no two-sided near-Einstein pinching.

The valid statement retained from Step 63 is
\[
\|\operatorname{Ric}_\gamma+2\gamma\|_{\rm op}<\frac23
\quad\Longrightarrow\quad K_\gamma<0,
\]
which Preissmann excludes on \(T^3\). This is a two-sided Ricci-neighborhood statement, not a one-sided negative-Ricci statement.

### 1.2 Scope of the Step 66 computation

The four fine-grid residuals
\[
4.4035,\quad1.5164,\quad4.8857,\quad2.6805
\]
are outcomes of four finite-dimensional ansätze, initializations, grids, and optimizers. They neither compute the infimum in that ansatz nor certify any continuum lower bound. The validated full-Ricci implementation and exact-cusp checks remain useful. Withdrawn: the curved-slice “Prong B,” closure of the curved-slice/model collar territory, closure of the graph-manifold route, and all dimension restrictions inferred from that closure.

### 1.3 What the flat-slice theorem actually covers

For
\[
g=dr^2+G(r)
\]
with \(G(r)\) a coordinate-independent positive-definite matrix on \(T^3\), every slice is intrinsically flat even when \(G\) is off-diagonal or matrices at distinct \(r\) do not commute. The shape operator is self-adjoint with respect to \(G(r)\). Thus the valid Step 63 estimate
\[
H^2\ge 9-6\delta
\]
under \(\|\operatorname{Ric}+3g\|_{\rm op}\le\delta\) covers this entire flat-slice class. A no-neck conclusion additionally needs end/global data forcing \(H\) to change sign or pass through zero; an exact hyperbolic cusp is not excluded.

A general Gaussian collar
\[
g=dr^2+\gamma_r(x)
\]
has curved, tangentially inhomogeneous slices and is not covered by this theorem. Off-diagonal terms do not break self-adjointness, but genuine \(x\)-dependence activates intrinsic Ricci, Codazzi divergence, and normal-evolution terms.

### 1.4 Four-dimensional Chern–Weil statements

The Step 65 assertion
\[
\operatorname{Vol}\ge1,\quad |s|\le1
\quad\Longrightarrow\quad \int|\operatorname{Ric}|^2\ge\frac13
\]
on \(T^4\) is false; a unit-volume flat torus is an immediate counterexample. It and its consequences are withdrawn.

The valid nonzero-normalization statement is only
\[
\mu_4:=\inf_\gamma\|\operatorname{Ric}_\gamma+3\gamma\|_{\rm op}
\ge \frac{3(\sqrt3-1)}2.
\]
This is a lower bound, not a determination of \(\mu_4\). Moreover an isolated-slice lower bound does not automatically become an ambient defect bound because intrinsic curvature, the second fundamental form, and normal evolution compensate in the ambient equations.

The examples in the cheap Chern–Weil class must also be corrected: \(\Sigma_g\times\Sigma_h\), \(g,h\ge2\), has \(\chi=4(g-1)(h-1)>0\), \(\tau=0\), satisfies Hitchin–Thorpe strictly, and the product of equally normalized hyperbolic factors is Einstein. It is not in the class \(2\chi\le3|\tau|\).

### 1.5 Dimension conclusions

Low-dimensional slice inequalities are filters, not ambient no-neck theorems. The earlier conclusion that ambient dimension six is the first open territory is withdrawn. In particular, the \(\mu_4\) lower bound alone does not close a five-dimensional construction; the full ambient equations may compensate slice defect.

## 2. Full Gaussian Einstein system

Let
\[
g^Z=dt^2+g_t,
\]
and use the Weingarten convention of Ammann–Moroianu–Moroianu/Koiso,
\[
g_t(W_tX,Y)=-\frac12\dot g_t(X,Y).
\]
Then
\[
\begin{aligned}
\operatorname{Ric}^Z(\nu,\nu)
 &=\operatorname{tr}(W^2)-\frac12\operatorname{tr}_{g_t}\ddot g_t,\\
\operatorname{Ric}^Z(\nu,X)
 &=d\operatorname{tr}W(X)+\delta^{g_t}W(X),\\
\operatorname{Ric}^Z(X,Y)
 &=\operatorname{Ric}^{g_t}(X,Y)+2g_t(WX,WY)
 +\frac12\operatorname{tr}(W)\dot g_t(X,Y)-\frac12\ddot g_t(X,Y).
\end{aligned}
\]
For \(\operatorname{Ric}^Z=\lambda g^Z\), the hypersurface constraints are
\[
 d\operatorname{tr}W+\delta W=0,
\qquad
\operatorname{Scal}^{g_0}+\operatorname{tr}(W^2)-(\operatorname{tr}W)^2=(n-1)\lambda,
\]
and the tangential equation is the second-order normal evolution
\[
\ddot g_t=2\operatorname{Ric}^{g_t}
+\dot g_t(g_t^{-1}\dot g_t\,\cdot,\cdot)
-\frac12\operatorname{tr}(g_t^{-1}\dot g_t)\dot g_t
-2\lambda g_t.
\tag{E}
\]
These formulas expose the missing Step 66 mechanism: intrinsic Ricci need not itself approximate the ambient tangential Einstein tensor; it is balanced by \(\dot g_t\) and \(\ddot g_t\).

## 3. A source-backed local curved-neck mechanism

Koiso's analytic Cauchy theorem, as reviewed in Ammann–Moroianu–Moroianu, says that analytic \((g_0,W_0)\) satisfying the two constraints determine a unique local analytic Einstein germ \(dt^2+g_t\) (source: `Knowledge/objects/papers/1106.2066-The-Cauchy-problems-for-Einstein-metrics-and-parallel-spinors--e588543ba837--cf493e3a7afe/object.md`, Theorem 2.1, lines 94–140; citation \cite{ammann2018cauchy}).

Take \(n=3\), \(\lambda=-3\), and \(W_0=0\). The constraints reduce exactly to
\[
\operatorname{Scal}_{g_0}=-6.
\]
Analytic constant-negative-scalar metrics on \(T^3\) exist. One route is to start with any analytic conformal class of negative Yamabe constant and use the Yamabe minimizer; elliptic analytic regularity makes the minimizer analytic. Corollaries 2.2–2.3 of the same source state this consequence directly. Therefore:

> **Local Einstein reversal germ.** There exists an analytic metric \(g_0\) on \(T^3\) with \(\operatorname{Scal}_{g_0}=-6\) and a unique local analytic four-metric
> \[
> g^Z=dt^2+g_t,\qquad \operatorname{Ric}_{g^Z}=-3g^Z,
> \]
> for which \(T^3\times\{0\}\) is totally geodesic.

At \(t=0\), equation (E) gives
\[
\ddot g_0=2\operatorname{Ric}_{g_0}+6g_0,
\tag{E0}
\]
which is nonzero and anisotropic unless \(g_0\) were three-dimensional Einstein (impossible on \(T^3\) at negative scale). In the opposite sign convention \(S=-W\), the mean-curvature identity is
\[
H'=-\operatorname{Ric}^Z(\nu,\nu)-|S|^2=3-|S|^2,
\]
so at the totally geodesic slice \(H(0)=0\), \(H'(0)=3\). Thus the local exact Einstein geometry reverses mean curvature through a curved torus slice. This is a rigorous counterexample to any proposed *local* no-reversal implication based only on torus topology, scalar curvature, self-adjointness, or small ambient Einstein defect.

This does not give a compact graph-manifold metric. Analytic uniqueness makes the local germ rigid once \((g_0,W_0)\) is chosen, and Riemannian Einstein evolution is elliptic/ill-posed for generic smooth data. The unresolved problem is global: can such a germ be continued far enough and matched, exactly or with uniformly small defect, to two flat hyperbolic cusp ends with the required opposite orientations?

## 4. Reformulated neck problem

The correct curved-neck target is a two-ended boundary/matching problem, not a pointwise slice obstruction.

Given \(L>0\), seek \(g_t\) on \([-L,L]\times T^3\) such that:

1. near \(\pm L\), \(g_t\) agrees with or is close in sufficient jets to flat-cusp data;
2. the induced mean curvatures have opposite signs dictated by the graph gluing;
3. \(\|\operatorname{Ric}(dt^2+g_t)+3(dt^2+g_t)\|_{L^\infty}\) is small;
4. the mixed constraint \(dH+\delta W\) and Hamiltonian constraint are controlled, not merely the tangential equation.

The local Koiso germ proves that the central reversal can have zero defect. Hence any lower bound must use the distance/jets needed to reach flat cusp ends, an integrated conserved quantity, entropy/volume information, or a global topological input. Conversely, a counterexample construction should concentrate its residual only in the two matching layers and make their sup norm tend to zero by a genuine multiscale or elliptic gluing mechanism; making the layers smaller only controls integral norms and is insufficient for the target.

## 5. Next mathematical tests

1. Linearize (E) about the totally geodesic Koiso germ and about a hyperbolic cusp, identify stable/unstable boundary modes and the finite-dimensional mismatch between the two phase spaces.
2. Use the time-reflection symmetry forced by \(W_0=0\): uniqueness gives \(g_t=g_{-t}\). Determine whether any analytic initial \(g_0\) can generate asymptotically flat-cusp ends, or whether an invariant obstructs this.
3. Test prospective integrated monotonicities on this exact Einstein germ and on exact cusps; any quantity that forbids the germ is wrong.
4. Preserve the Step 66 JAX code as a verified evaluator, but redesign any computation around equation (E), constraint residuals, boundary jets, variable collar length, and continuation from a constant-scalar central slice rather than increasing the old Fourier basis blindly.

## 6. Relation to Yau 26

This local theorem does not prove or disprove Yau 26. It reopens the strongest concrete negative-branch candidate correctly: an extended graph four-manifold excludes every Einstein metric, while local exact Einstein reversal through a torus is possible. The decisive missing object is a global small-defect matching construction or a global theorem excluding it. A full disproof still needs both normalized signs to fail in the same dimension on all-Einstein-excluding manifolds; a proof needs one sign branch in every dimension. The output metric remains unrestricted and unrelated to the input metric.
