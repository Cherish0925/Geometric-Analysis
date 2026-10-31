# Quantitative product-boundary calibration and its surviving source

## 1. Result and geometric setting

The scalar-energy boundary of the closed shear examples is different from
the forbidden Weyl boundary used in the integral gap theorem. At this
boundary the correct model is realizable: a product of two hyperbolic
surfaces. The result below gives quantitative control of departure from
that model on the original metric, without compactness or smoothing.
It also identifies the term that survives in the weak-Bianchi argument.

Let \(g\) be a smooth metric on a closed oriented four-manifold, with

\[
 s_g=-4\kappa,\qquad \kappa>0,\qquad
 A=2\chi+3\tau>0.
\]

Assume a specified spin-c structure has \(a^2=A\) and an actual
unperturbed Seiberg--Witten solution \((\Phi,\mathfrak A)\) for this
metric. An actual monopole class of this square supplies the hypothesis;
an arbitrary cohomology class does not. Set

\[
 \rho=|\Phi|^2,\quad \psi=2\sqrt2\sigma(\Phi),\quad
 |\psi|=\rho,\quad K=\int|\nabla_{\mathfrak A}\Phi|^2,
\]
\[
 P=\int|\operatorname{Ric}^{\circ}|^2,\qquad
 D=\kappa^2\operatorname{Vol}(g)-2\pi^2 A,\qquad
 w=4\kappa-\rho.
 \tag{1}
\]

All two-form norms are exterior-algebra norms; Weyl and curvature
operators use Hilbert--Schmidt norms on two-forms. Define the smooth,
globally defined Weyl surrogate

\[
 \mathsf A_\psi=\frac{\rho^2}{48\kappa}I
                       -\frac{\psi\otimes\psi}{16\kappa},
 \qquad \mathsf R=W^+-\mathsf A_\psi.
 \tag{2}
\]

It is a polynomial in the spinor and is smooth even where the spinor
vanishes. Its eigenvalues are

\[
 -\frac{\rho^2}{24\kappa},\quad
 \frac{\rho^2}{48\kappa},\quad
 \frac{\rho^2}{48\kappa}.
\]

**Theorem 1.** One has \(0\leq\rho\leq4\kappa\), \(D\geq0\), and
the exact identities

\[
 \boxed{4D=K+\kappa\int w+2\|F_{\mathfrak A}^-\|_2^2,}
 \tag{3}
\]
\[
 \boxed{
 \|\mathsf R\|_2^2+D+\frac1{8\kappa}\|d\psi\|_2^2
 =\frac P4+
   \frac1{384\kappa^2}\int(16\kappa^2-\rho^2)^2
   +\frac1{16\kappa}\|\nabla\psi\|_2^2.}
 \tag{4}
\]

In particular,

\[
 \boxed{
 \|\mathsf R\|_2^2+\frac1{8\kappa}\|d\psi\|_2^2
      +\frac\kappa3\int w+2\|F_{\mathfrak A}^-\|_2^2
 \leq \frac P4+3D.}
 \tag{5}
\]

No Einstein hypothesis, diameter bound, Sobolev constant, injectivity
radius, or full-curvature bound is assumed. Constant negative scalar
curvature is an actual hypothesis, not inferred from small Ricci error.

The closed shear manifolds have \(\tau=0\), \(A=2\chi>0\), and
actual canonical monopoles of square \(A\) in both orientations by
[Round 12](round12_global.md). Their scalar-calibrated Round-14 metrics
therefore satisfy the theorem twice. The opposite-orientation class is
not incorrectly treated as a positive-square class in the original
orientation.

## 2. Exact scalar loss decomposition

The standard unweighted equations, in the conventions of
[the monopole input](round3_monopole_input.md), give

\[
 4\nabla_{\mathfrak A}^*\nabla_{\mathfrak A}\Phi
                  +(\rho-4\kappa)\Phi=0,
 \qquad |F_{\mathfrak A}^+|^2=\rho^2/8.
 \tag{6}
\]

The maximum principle yields \(\rho\leq4\kappa\). Pairing with the
spinor and integrating gives

\[
 4K=4\kappa\int w-\int w^2.
 \tag{7}
\]

The determinant connection represents \(2\pi a\), so its full
Chern--Weil identity, not merely a harmonic projection bound, gives

\[
 \int\rho^2=8\|F_{\mathfrak A}^+\|_2^2
          =32\pi^2 A+8\|F_{\mathfrak A}^-\|_2^2.
 \tag{8}
\]

Expanding \(\rho=4\kappa-w\) in (8) and using (7) proves (3).
Every term on its right is nonnegative. In particular

\[
 K\leq4D,\qquad \kappa\int w\leq4D,\qquad
 \int w^2\leq16D,\qquad \|F_{\mathfrak A}^-\|_2^2\leq2D.
 \tag{9}
\]

These statements concern the actual connection of an actual solution.
No derivative of a merely chosen harmonic cohomology representative
has been substituted for a spinor derivative.

The foundational spinor identities and equality characterization are
classical: see LeBrun, [*Ricci Curvature, Minimal Volumes, and
Seiberg--Witten Theory*, Section 2](https://arxiv.org/pdf/math/0003068),
and [*Four-Manifolds, Curvature Bounds, and Convex Geometry*,
Proposition 3.2](https://arxiv.org/pdf/math/0611450).
Here the full nonnegative decomposition is retained quantitatively.

## 3. Weyl calibration from the actual spinor

The exact two-form Hodge identity is

\[
 2\|d\psi\|_2^2
 =\|\nabla\psi\|_2^2-\frac{4\kappa}{3}\int\rho^2
                         -2\int\langle W^+\psi,\psi\rangle.
 \tag{10}
\]

Self-duality gives \(\|d^*\psi\|_2=\|d\psi\|_2\). The quadratic
spinor map satisfies the pointwise differential bound

\[
 |\nabla\psi|^2\leq4\rho|\nabla_{\mathfrak A}\Phi|^2
                     \leq16\kappa|\nabla_{\mathfrak A}\Phi|^2.
 \tag{11}
\]

The operator (2) has squared norm \(\rho^4/(384\kappa^2)\), and
trace-freeness of \(W^+\) gives

\[
 \|\mathsf R\|_2^2
 =\|W^+\|_2^2+\frac1{384\kappa^2}\int\rho^4
                  +\frac1{8\kappa}\int\langle W^+\psi,\psi\rangle.
 \tag{12}
\]

Chern--Weil with \(A=2\chi+3\tau\) reads

\[
 \|W^+\|_2^2
 =2\pi^2A-\frac{\kappa^2}{3}V+\frac P4
 =\frac23\kappa^2V-D+\frac P4.
 \tag{13}
\]

Substitute (10) and (13) into (12). The remaining scalar polynomial
is exactly

\[
 \frac23\kappa^2-\frac{\rho^2}{12}
                         +\frac{\rho^4}{384\kappa^2}
 =\frac{(16\kappa^2-\rho^2)^2}{384\kappa^2}.
\]

This proves (4). Since \(0\leq w\leq4\kappa\),

\[
 \frac{(16\kappa^2-\rho^2)^2}{384\kappa^2}
 \leq \frac{w^2}{6}\leq\frac{2\kappa}{3}w.
 \tag{14}
\]

Equations (11), (14), and (3) yield

\[
 \|\mathsf R\|_2^2+D+\frac1{8\kappa}\|d\psi\|_2^2
 \leq\frac P4+K+\frac{2\kappa}{3}\int w
 =\frac P4+4D-\frac\kappa3\int w-2\|F_{\mathfrak A}^-\|_2^2,
\]

which is (5). All estimates are integral identities or pointwise
polynomial bounds on the original metric.

## 4. Two orientations give a full product-curvature estimate

Let \(\mathscr K_\kappa\) be the Weyl-operator orbit with eigenvalues

\[
 (-2\kappa/3,\kappa/3,\kappa/3).
\]

Choose the distinguished eigenline to be the line of \(\psi\) where
it is nonzero; at its zeros choose any measurable line. There is no
derivative of this choice. The squared distance between (2) and the
chosen orbit element is exactly the polynomial in (14). Consequently

\[
 \int\operatorname{dist}(W^+,\mathscr K_\kappa)^2
 \leq2\|\mathsf R\|_2^2+
       2\int\frac{(16\kappa^2-\rho^2)^2}{384\kappa^2}
 \leq\frac P2+\frac{34}{3}D.
 \tag{15}
\]

Now assume \(\tau=0\) and both orientations have actual monopoles
of square \(A=2\chi>0\). Let \(\mathcal R_g:\Lambda^2\to\Lambda^2\)
be the curvature operator and \(\mathscr P_\kappa\) the oriented
orthogonal orbit of the curvature operator of

\[
 \mathbb H^2_{-\kappa}\times\mathbb H^2_{-\kappa}.
\]

**Corollary 2.** For every constant-scalar metric as above,

\[
 \boxed{
 \int\operatorname{dist}_{\rm HS}(\mathcal R_g,\mathscr P_\kappa)^2
 \leq\frac32 P+\frac{68}{3}D.}
 \tag{16}
\]

**Proof.** The two Weyl blocks independently satisfy (15).
The off-diagonal Ricci blocks of the curvature operator have total
squared norm (P/2). Adding \(s/12=-\kappa/3\) to the diagonal
blocks makes their model spectra \((-\kappa,0,0)\) in both
orientations. Any pair of distinguished unit lines in \(\Lambda^+\)
and \(\Lambda^-\) determines two complementary simple two-planes;
equivalently, \(SO(4)\to SO(3)\times SO(3)\) is onto. Thus the
two independent orbit choices assemble into one product-curvature
operator, rather than two incompatible model choices. Summing proves
(16). The full four-index curvature-norm bound is four times (16).

For an Einstein metric \(P=0\), (16) bounds average deviation from
the local product model by its normalized volume excess. It does not
produce a global splitting or an identification of the fundamental
group. In particular it does not erase the shear topology.

The product metric itself has \(D=P=0\), parallel canonical spinors,
and both model Weyl blocks exactly. Thus it passes the equality test.

## 5. The full surviving weak-Bianchi source

The surrogate in (2) is \(1/(2\kappa)\) times the polynomial model
used at the forbidden \(2/3\) boundary. Retaining that old model
unchanged would impose the wrong curvature scale.

Let \(W(\mathsf A)\) denote its four-index tensor, in the conventions
of [the original first-jet computation](round3_monopole_input.md), and
put

\[
 J=\operatorname{div}W(\mathsf A_\psi),\qquad
 C_\psi=\langle\iota_{\nabla\rho}\psi,*d\psi\rangle.
\]

The exact weighted Hodge/first-jet identity gives

\[
\begin{split}
 \int|J|^2={}&
 \int\frac{\rho^4(16\kappa^2-\rho^2)}{3072\kappa^3}
 +\frac1{128\kappa^2}\int\rho^2\langle\mathsf R\psi,\psi\rangle\\
 &+\frac1{64\kappa^2}\int\rho^2|d\psi|^2
 -\frac5{384\kappa^2}\int\rho^2|d\rho|^2
 +\frac1{32\kappa^2}\int\rho C_\psi.
\end{split}
 \tag{17}
\]

This identity includes the remainder/source term, the amplitude term,
and all differential terms. In particular the algebraic term is

\[
 \frac{\rho^4(4\kappa-\rho)(4\kappa+\rho)}{3072\kappa^3},
 \qquad 0\leq\int\text{this term}\leq\frac83\kappa D.
 \tag{18}
\]

It vanishes at the product calibration \(\rho=4\kappa\). There is
no residual positive constant analogous to \(1/16\) in the forbidden
model. This is the precise cancellation, not just a numerical difference
between \(T/A=1\) and \(2/3\).

The pointwise polynomial derivative gives

\[
 |\nabla\mathsf A_\psi|^2
 =\frac{\rho^2}{128\kappa^2}|\nabla\psi|^2
  +\frac{\rho^2}{384\kappa^2}|d\rho|^2.
 \tag{19}
\]

Equations (9), (11), and the fixed-dimensional divergence contraction
give \(\int|J|^2\leq C\kappa D\). The differential terms in
(17) have the same bound, so the *integrated* remainder contraction
also satisfies

\[
 \left|\frac1{128\kappa^2}
       \int\rho^2\langle\mathsf R\psi,\psi\rangle\right|
 \leq C\kappa D.
 \tag{20}
\]

This does not make that contraction pointwise nonnegative or remove it
from the equation. For Einstein \(g\), weak Bianchi says

\[
 J=-\operatorname{div}W(\mathsf R),\qquad
 \int\langle J,T\rangle
   =\int\langle W(\mathsf R),\nabla T\rangle
 \tag{21}
\]

for smooth tests, with the stated divergence convention. Both sides of
the self-test may now tend to zero with \(D\). The actual equations
therefore retain the possibility of product-like Einstein degeneration;
the earlier forbidden-spectrum contradiction cannot be transplanted by
discarding this source.

## 6. A quantitative necessary condition for exact output

Let

\[
 \mu_\pm(g)=\inf_{0\ne\omega\in C^\infty(\Lambda^\pm)}
                    \frac{\|\nabla\omega\|_2^2}{\|\omega\|_2^2}
 \tag{22}
\]

be the lowest connection-Laplacian eigenvalues, not Hodge-Laplacian
eigenvalues. Taking the two spinor forms as tests, (8), (9), and (11)
prove

\[
 \boxed{
 \mu_\pm(g)\leq\frac{2\kappa D}{\pi^2 A}
        =4\kappa\left(\frac{V}{V_*}-1\right),
 \qquad V_*:=\frac{2\pi^2A}{\kappa^2}.}
 \tag{23}
\]

The same metric supplies both estimates. For a non-Kähler smooth type
in both orientations, each \(\mu_\pm(g)>0\): on a fixed compact
metric a zero eigenvalue would give a nonzero parallel self-dual or
anti-self-dual form, hence a compatible Kähler structure. Thus every
putative Einstein output obeys

\[
 \frac{V}{V_*}-1
 \geq\frac{\max\{\mu_+(g),\mu_-(g)\}}{4\kappa}>0.
 \tag{24}
\]

This is a metric-dependent quantitative necessary condition. Positivity
for every metric is not a uniform lower bound over a degenerating
Einstein family. The two explicit collapsing eigenvalue tests below
show why that distinction is necessary.

## 7. The actual shear supplies the source at cubic order

For the pure-shear family of [Round 14](round14_global.md), use
\(\kappa=3\), \(k=\sqrt3\), and

\[
 G_\ell=dt^2+a^2\theta^2+h_F,\quad
 a=c\cosh(kt),\quad \theta=d\phi+z(t)\beta,\quad
 c=\ell/(2\pi),\quad Q=\tfrac12a^2z'^2|\beta|^2.
\]

The global symplectic forms already constructed in Round 11 are

\[
 \Omega_\pm=a\,dt\wedge\theta\ \pm\ \omega_F.
\]

They are closed, of norm \(\sqrt2\), and respectively self-dual and
anti-self-dual. For the pure-shear metric their covariant derivatives
satisfy the **exact pointwise identity**

\[
 \boxed{|\nabla\Omega_+|^2=|\nabla\Omega_-|^2=2Q.}
 \tag{25}
\]

To see this, choose an orthonormal frame \(T,U,X,Y\) with

\[
 T=\partial_t,\quad U=a^{-1}\partial_\phi,\quad
 \beta=|\beta|X^*,\quad q=az'|\beta|/2.
\]

At the point, eliminate the fiber Levi-Civita connection by a normal
frame. The electric terms are

\[
 \nabla_TU=qX,\quad \nabla_TX=-qU,\quad
 \nabla_UT=(a'/a)U+qX,\quad \nabla_UX=-qT,
 \quad \nabla_XT=qU,\quad\nabla_XU=-qT.
\]

The ordinary \(T,U\) hyperbolic rotation preserves their area form.
The \(T\)- and \(U\)-derivatives of either \(\Omega_\pm\) each have
squared norm \(2q^2\); the \(X,Y\) derivatives vanish. Their sum is

\[
 4q^2=a^2z'^2|\beta|^2=2Q.
\]

The formula extends through zeros of \(\beta\) and through profile
cutoffs; outside the shear, the forms are parallel. Thus it holds on
the actual closed manifold, not only the infinite model cylinder.

Writing \(B_\beta=\int_F|\beta|^2\), the optimized profile yields

\[
 \int Q=\frac{kB_\beta}{4\pi^3}\ell^3+O(\ell^6),\qquad
 \frac{\|\nabla\Omega_\pm\|_2^2}{\|\Omega_\pm\|_2^2}
 =\frac1{V_*}\int Q.
 \tag{26}
\]

Here \(V_*=4\pi^2\chi/9\) in the normalization \(\kappa=3\).
Scalar calibration gives \(\widehat G_\ell=v_\ell^2G_\ell\).
Self-duality, closedness, and the \(L^2\) norm of two-forms are
conformally unchanged. Round 14 gives

\[
 \|v_\ell-1\|_\infty=O(\ell^2),\qquad
 \|dv_\ell\|_2=O(\ell^{5/2}).
\]

The difference of the two Levi-Civita connections acting on a two-form
is bounded by \(C|d\log v|\,|\Omega_\pm|\). Thus Cauchy--Schwarz
and (25) show

\[
 \|\widehat\nabla\Omega_\pm\|_{2,\widehat G_\ell}^2
 =2\int Q+O(\ell^4),\qquad
 \mu_\pm(\widehat G_\ell)
 \leq\frac{kB_\beta}{4\pi^3V_*}\ell^3+O(\ell^4).
 \tag{27}
\]

For these scalar-calibrated metrics, simultaneously,

\[
 D_\ell=9(\operatorname{Vol}(\widehat G_\ell)-V_*)
     =\frac{3kB_\beta}{8\pi^3}\ell^3+O(\ell^5),
 \qquad P_\ell=O(\ell^5).
 \tag{28}
\]

Equation (16) therefore gives an \(O(\ell^3)\) full product-curvature
calibration even though the integral Einstein defect is \(O(\ell^5)\).
The scalar-energy surplus and the failure of the canonical plane forms
to be parallel record the shear at a different scale from tracefree
Ricci. They cannot be silently replaced by the smaller Ricci error.

## 8. Einstein outputs approaching the sharp volume cannot form curvature bubbles

There is a stronger consequence when the metric is exactly Einstein.
Fix the normalization \(\operatorname{Ric}=-3g\), and suppose
\(\tau=0\), \(A=2\chi>0\), with the actual canonical monopole
input in both orientations. The constants in the next statement do not
depend on \(A\).

**Theorem 3.** There are universal \(D_0>0\) and \(C_m<\infty\)
such that every such exact Einstein metric with

\[
 0\leq D=9\operatorname{Vol}(g)-2\pi^2A\leq D_0
\]

satisfies

\[
 \sup_M|\nabla^m\operatorname{Rm}_g|\leq C_m
 \quad(m=0,1,2,\ldots).
 \tag{29}
\]

In particular a sequence of exact Einstein metrics on a fixed closed
shear manifold whose volumes approach the sharp scalar-volume bound
\(V_*=2\pi^2A/9\), if it exists, cannot develop unbounded curvature,
even in collapsing regions. This does not address a sequence minimizing
Einstein volume when its infimum lies strictly above this bound.

**Proof.** For exact Einstein metrics \(P=0\), (16) bounds the total
curvature-operator model error by \(68D/3\). The product model has
four-index squared norm \(8\kappa^2=72\). Therefore every ball satisfies

\[
 \int_{B_r(p)}|\operatorname{Rm}|^2
 \leq8\int_M\operatorname{dist}_{\rm HS}
                     (\mathcal R_g,\mathscr P_3)^2
       +144\operatorname{Vol}B_r(p)
 \leq\frac{544}{3}D+144C_{\rm BG}r^4,
 \quad 0<r\leq1.
 \tag{30}
\]

The volume upper bound is Bishop--Gromov with \(\operatorname{Ric}=-3g\);
it does not assume a volume lower bound. The four-dimensional
Cheeger--Tian theorem gives universal \(\epsilon_{\rm CT},C_{\rm CT}\)
such that, for an exact Einstein metric with Einstein constant of
absolute value at most three,

\[
 \int_{B_r(p)}|\operatorname{Rm}|^2\leq\epsilon_{\rm CT},
 \quad r\leq1
 \quad\Longrightarrow\quad
 \sup_{B_{r/2}(p)}|\operatorname{Rm}|\leq C_{\rm CT}r^{-2}.
 \tag{31}
\]

There is no noncollapse condition in this theorem. It is stated directly
by Cheeger in his [2018 lecture, slides 2--3](https://sites.duke.edu/scshgap/files/2016/08/dim4dukebeamer.pdf),
explicitly with an integral not normalized by volume. Its precise statement
is also reproduced as Theorem 1.1 in Ge--Jiang,
[*Epsilon-regularity for shrinking Ricci solitons and Ricci flows*](https://arxiv.org/pdf/1707.05511),
which attributes it to Cheeger--Tian, *JAMS* 19 (2006), 487--525.
Choose once and for all \(r_0\leq1\) so that
\(144C_{\rm BG}r_0^4\leq\epsilon_{\rm CT}/2\), then choose
\(D_0\leq3\epsilon_{\rm CT}/1088\).
Equations (30)--(31) now apply at every point, proving the global
curvature bound. Fixed-order derivative bounds follow from bounded-
curvature Einstein regularity. Equivalently apply the standard complete
bounded-curvature Ricci-flow derivative estimates to the explicit
self-similar flow \(g(t)=(1+6t)g\) on a fixed positive time interval,
and scale back. This route also needs no injectivity-radius hypothesis.

The absolute integral in (30) is intentional. The argument does not
divide by the volume of a collapsing ball, and does not assert that
small absolute model error implies pointwise closeness to the product
at every collapsed point.

**Corollary 4 (the remaining degeneration).** Fix a closed shear manifold
with the non-Kähler conclusion in both orientations proved in Round 11.
If exact metrics \(g_j\) with \(\operatorname{Ric}_{g_j}=-3g_j\)
satisfy \(\operatorname{Vol}(g_j)\to V_*\), then

\[
 \operatorname{diam}(M,g_j)\longrightarrow\infty.
 \tag{32}
\]

Every smooth pointed noncollapsed limit of such a sequence is locally
isometric to \(\mathbb H^2_{-3}\times\mathbb H^2_{-3}\).

**Proof.** A bounded-diameter subsequence would, by the lower total
volume \(V_*>0\) and relative Bishop--Gromov comparison, have uniform
lower volumes for fixed-radius balls. The curvature bound (29) then
gives a uniform injectivity radius and smooth Einstein compactness on
the original smooth type. Pull back the actual quadratic spinor forms
\(\psi_j^+\), not their determinant connections or spin-c structures,
by the same compactness diffeomorphisms. Equations (9) and (11) make
their covariant gradient energies tend to zero and their lengths tend
to \(12\) in \(L^2\). Rellich compactness on the fixed compact limit
then gives a global nonzero parallel two-form, hence a Kähler structure
in one of the two orientations. This contradicts the topology and
proves (32). No identification of the pulled-back spin-c structures is
needed.

For the pointed assertion it is enough to consider any smooth
noncollapsed limit charts. Choose actual spinor solutions in both
orientations on \(g_j\). Equations (9) and (11) give
\(\int|\nabla\psi_j^\pm|^2\to0\) and
\(\int(|\psi_j^\pm|-12)^2\to0\).
After transport to a fixed smooth limit chart, local Rellich compactness
and the uniform amplitude bound give nonzero parallel self-dual and
anti-self-dual limiting forms. A diagonal subsequence works on every
compact subset. The two associated parallel complex structures commute
and give complementary parallel two-plane distributions. Local product
splitting and \(\operatorname{Ric}=-3g\) make both surface factors
have curvature \(-3\). This proves the claimed local geometry without
assuming that the original smooth shear splitting is respected.

The corollary neither asserts noncollapse everywhere nor transfers
absolute error to local covers of unbounded multiplicity. Its conclusion
is precise: any remaining exact sequence with \(V\to V_*\) must have
bounded-curvature long geometry, with product geometry in its smooth
noncollapsed limits, rather than curvature bubbles.

In fact at least one such pointed limit exists. A second classical
Cheeger--Tian estimate, stated in [Cheeger's lecture, slides 8--9](https://sites.duke.edu/scshgap/files/2016/08/dim4dukebeamer.pdf),
says that a complete Einstein four-manifold with
\(\operatorname{Ric}=\pm3g\) and total curvature energy bounded by \(C\)
has some point \(p\) for which
\(\operatorname{Vol}B_1(p)/\operatorname{Vol}M\geq w(C)>0\).
On the fixed closed \(M\), exact Einstein Chern--Gauss--Bonnet gives
\(\int|\operatorname{Rm}|^2=32\pi^2\chi(M)\) in our full four-index
norm; the slides use the curvature-operator convention, with energy
\(8\pi^2\chi(M)\). Rescaling the fixed constant converts between them.
Since \(\operatorname{Vol}(g_j)\geq V_*>0\), choose basepoints \(p_j\)
with a uniform unit-ball volume lower bound. Together with (29),
pointed smooth compactness produces a complete limit after a subsequence.
The preceding proof makes this limit locally
\(\mathbb H^2_{-3}\times\mathbb H^2_{-3}\), and exhaustion by compact
sets gives total volume at most \(V_*\). The noncollapse estimate is a
classical input, not a new theorem of this round.

This complete limit is noncompact. Otherwise smooth pointed convergence
would eventually embed the entire compact limit into the connected
\(M\). The embedding is a local diffeomorphism with compact, hence
closed, image; its image is also open, so it is onto. The limiting
global parallel two-form would then give a Kähler structure on \(M\),
contrary to the assumed topology. The two parallel plane distributions
lift to the complete simply connected cover. The de Rham theorem gives
that cover as \(\mathbb H^2_{-3}\times\mathbb H^2_{-3}\). No identification
of the limit's ends with the original shear collars follows from this
argument.

## 9. Consequence for the next exact-equation step

At \(T/A=1\), actual gauge equations do yield a quantitative theorem:
small scalar-volume excess and small tracefree Ricci energy force both
canonical curvature blocks toward a genuine product model, with explicit
control on the original metric. For an exact output approaching the
sharp volume, its two connection-Laplacian gaps must also vanish.

For the current shear topology the equality \(D=0\) is excluded by
the established non-Kähler theorem. But the actual constructed sequence
has \(D\to0\), collapsing parallel-form gaps, and the source (25).
Thus topology cannot be converted into a uniform \(D\)-gap solely by
claiming that a nonparallel canonical form costs a fixed amount of
energy. Any such claim needs new control of the global matching or of
the exact Einstein equation; it is not supplied by (3)--(21).

This result is a quantitative stability statement at a *realizable*
calibration, complementary to the earlier integral obstruction at the
unrealizable \(2/3\) calibration. It neither creates a Yau26 counterexample
nor limits future arguments to monopole-budget refinements.

`round15_rigidity_check.py` independently checks the scalar and Weyl
identities, the two-orientation curvature normalization, the corrected
Weyl-source contraction, and the electric-shear parallel-form energy.
The classical gauge-existence input is not certified by these algebra
checks; it is the stated actual-monopole hypothesis.
