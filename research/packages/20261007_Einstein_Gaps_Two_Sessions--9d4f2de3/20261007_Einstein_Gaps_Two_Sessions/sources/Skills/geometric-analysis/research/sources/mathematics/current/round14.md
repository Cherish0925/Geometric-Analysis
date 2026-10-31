# Round 14: twisted integral rigidity and an all-mode Einstein repair barrier

## Outcome

This round advances all three research lines, with the strongest connection
between the construction and global lines. The fixed closed pure-shear
family now has pointwise Einstein defect of order \(\ell^2\), while **every
Einstein metric, without a symmetry or gauge restriction, is excluded from
a geometric \(C^2\) ball of radius \(b\ell\)** around it. The radius
still tends to zero; no global Einstein nonexistence is deduced.

Separately, the integral rigidity mechanism extends to genuine
\(\mathrm{Pin}^-(2)\) inputs. This supplies a uniform integral gap on an
explicit infinite critical family where ordinary Seiberg--Witten
invariants vanish. The local linear analysis also identifies both radial
collar modes and proves a uniform bound on their full Dirichlet complement.

These are additions to the twelve-round results and Round 13, not a new
proof or independent certification of every inherited theorem. Complete
Yau26 remains unresolved.

## 1. Rigidity: the required equations need not live downstairs

The previous integral theorem used actual weighted-solvable monopoles.
This round checks its precise analytic dependency: on a finite isometric
cover, it only needs the deck-invariant weights built from the tested
metric's scalar and self-dual Weyl curvature. Positive smooth majorants
can be averaged over the deck group. All subsequent spinor and weak
Bianchi estimates run on the ordinary bundles upstairs.

Consequently actual \(\mathrm{Pin}^-(2)\) solutions downstairs provide
the required input after lifting. This does **not** assert ordinary
all-metric monopole nonvanishing on the cover. The equations are used
only on lifted metrics and with the necessary invariant weights.

Let \(M\) have \(b_+(M)\ge2\) and an odd ordinary SW invariant in a
spin-c structure with square
\(A=2\chi(M)+3\tau(M)>0\). Let \(b_+(N)=0\), and set
\[
 X=M\#N\#\Bigl(\mathop{\#}_j S^2\times\Sigma_{r_j}\Bigr)
       \#\Bigl(\mathop{\#}_{i=1}^m S^1\times Y_i\Bigr),
 \quad r_j\ge1,
\]
with at least one of the displayed latter summands. Write
\[
 D=b_2(N)+4b_1(N)+\sum_j(8r_j-4)+4m.
\]
Using the genuine classes of Ishida--Matsuo--Nakamura, their square
\(A-b_2(N)\), and the invariant-weight argument, the inherited integral
theorem gives
\[
 \boxed{\mathcal E_X(g)+\left(\frac13-\frac DA\right)_+\ge c_*}
 \quad\text{for every smooth metric on }X.                 \tag{1}
\]
The constant is independent of these topologies. Here
\[
 \mathcal E_X(g)=\inf_{\lambda\ne0}
   \frac{\int_X|\operatorname{Ric}_g-\lambda g|^2\,d\mu_g}
        {\lambda^2\operatorname{Vol}_g(X)}.
\]

A concrete critical family is
\[
 X_j=(\Sigma_2\times\Sigma_{3j+1})
           \#\mathop{\#}_{2j}(S^2\times T^2),\qquad j\ge1.
\]
It has \(A_j=24j\), \(D_j=8j\), so (1) yields
\[
                         \mathcal E_{X_j}(g)\ge c_* .      \tag{2}
\]
The ordinary SW and ordinary stable-cohomotopy SW invariants vanish in
this class. The twisted nonvanishing and the exact Einstein obstruction
are classical inputs; the present addition is the **uniform integral
stability at this critical boundary**, conditional only on the previously
proved integral mechanism. See
[the full twisted proof](round14_twisted_rigidity.md) and
[Ishida--Matsuo--Nakamura, Propositions 8--9 and Theorem 16](https://arxiv.org/pdf/1505.05948).

A separate [finite-cover proof](round14_rigidity.md) gives an explicit
quotient application with all ordinary SW invariants zero on the base.
It also shows why covers alone do not solve the closed-shear problem:
every finite cover of that family still has monopole budget
\(\alpha^2=\beta^2=2\chi\), and critical ratio one, not two-thirds.

## 2. Construction: solve the mixed equation, then retain its geometric forces

On a hyperbolic product throat let
\[
 a=c\cosh(kt),\quad k=\sqrt3,\quad
 g=dt^2+a^2(d\phi+z(t)\beta)^2+h_F,
 \quad K(h_F)=-3.
\]
The fixed nonzero integral shear has harmonic representative \(\beta\).
The actual mixed Ricci equation is
\[
 (a^3z')'=0,
 \qquad
 z'=\frac{\operatorname{sech}^3(kt)}{J_3(R)},\quad
 J_m(R)=\int_{-R}^R\operatorname{sech}^m(kt)dt.             \tag{3}
\]
Its connection energy is minimal even among general circle-invariant
connections with these endpoint cohomology classes:
\[
 \min\mathscr C=\frac{c^3}{J_3(R)}\|\beta\|_2^2.          \tag{4}
\]
Solving (3) leaves a signed waist projection
\[
 \int\langle\operatorname{Ric}+3g,H_{\rm waist}\rangle
 =-2\pi c^3\|\beta\|_2^2\frac{J_5(R)}{J_3(R)^2}
 \sim-3\sqrt3c^3\|\beta\|_2^2.                           \tag{5}
\]
It also leaves a fiber TT force in the genuine Teichmuller direction
\[
 T_\beta=\beta\otimes\beta-\tfrac12|\beta|^2h_F.
\]
For the harmonic energy of the fixed class,
\[
 D\|\beta_h\|_2^2[T_\beta]
                 =-\tfrac12\int_F|\beta|^4<0.             \tag{6}
\]
The corresponding linear shape correction satisfies
\((av')'=-a^3z'^2\) and exports a nonzero flux to the two ends.
Thus the remaining problem involves actual geometry and boundary response,
not another arbitrary choice of connection cutoff. These forces belong
to a fixed-background reduced problem; nonlinear feedback must still be
controlled before a full obstruction follows.

Proofs, the exact complete-throat response, and the distinction between
Maxwell energy and receiver minimization are in
[round14_shear.md](round14_shear.md).

### Fixed closed metrics with three explicit scales

For the identity mapping-class subfamily, use nearly the full available
hyperbolic collar and smoothly truncate (3) where the radius is bounded
away from zero. All gluing maps and the closed smooth manifold remain
fixed. The resulting metrics satisfy
\[
 \|g_\ell^{-1}\operatorname{Ric}_{g_\ell}+3I\|_\infty
       \le C\ell^2,
 \qquad\operatorname{Vol}(g_\ell)=V_*=rac{4\pi^2\chi(M)}9.
\]
A conformal correction of size \(O(\ell^2)\) produces \(\widehat g_\ell\)
with **exact** scalar curvature \(-12\). For a single nonzero shear,
\[
 \begin{split}
 \operatorname{Vol}(\widehat g_\ell)-V_*
     &=\frac{\sqrt3\|\beta\|_2^2}{24\pi^3}\ell^3+O(\ell^5),\\
 \int_M|\operatorname{Ric}^{\circ}_{\widehat g_\ell}|^2
     &=\Theta(\ell^5) .
 \end{split}                                               \tag{7}
\]
The complete Ricci defect remains \(O(\ell^2)\), and full curvature
and all fixed-order derivatives stay bounded. The remaining defect is
trace-free and divergence-free.
The lower bound in (7) follows from the receiver in the next section:
its pairing is of order \(\ell^3\) and its \(L^2\) norm is of order
\(\ell^{1/2}\). Cauchy--Schwarz gives the matching fifth-order energy
lower bound. In the exact scalar normalization,
\[
 \mathcal E(\widehat g_\ell)
 =\frac{4J_\ell}{36\operatorname{Vol}(\widehat g_\ell)+J_\ell}
 =\Theta(\ell^5),\quad
 J_\ell=\int|\operatorname{Ric}^{\circ}_{\widehat g_\ell}|^2.
\]

This is an improved family on the existing pure-shear smooth types, not
another claim of new topology. It does not improve the slow mapping-class
transition in the general closed family. The proof includes uniform local
cover estimates, the scalar PDE, and the exact positive volume identity:
[round14_global.md](round14_global.md).

## 3. Full tensor analysis: a controlled collar complement and a genuine repair barrier

### The collar's complete Dirichlet low-energy sector

On a collapsing fixed-fiber subcollar, there are **two**, not one, radial
kernel polarizations:
\[
 H_1=f(dt^2-a^2d\phi^2),\qquad
 H_2=f\{dt\otimes(ad\phi)+(ad\phi)\otimes dt\},\quad
 f=\operatorname{sech}^2(kt).
\]
After removing their two \(L^2\) projections, the full Dirichlet
Einstein operator satisfies
\[
 \langle Pq,q\rangle\ge\mu\|q\|_2^2,
 \quad\mu=\min\{k^2/8,\lambda_1(F)/2\}>0                 \tag{8}
\]
on the exact product, and \(\mu/2\) on the actual sheared plateau
for small enough maximal radius. This includes all nonzero angular modes,
mixed tensors, traces, and fiber TT tensors. The proof uses an explicit
radial factorization and the surface Weitzenbock identity, with min--max
showing exactly two small Dirichlet eigenvalues.

This fills the local complement estimate left open in Round 13. The
twist's global gauge status and the adjacent blocks' low modes remain in
the closed matching problem; they are not removed by Dirichlet boundary
conditions. See [round14_collar_complement.md](round14_collar_complement.md).

### A nonlinear exclusion allowing every perturbation mode

For the optimized closed family, cut off the actual waist tensor in
the exact-product outer bands. Direct computation gives
\[
 \|H_c\|_1\le Cc,\qquad
 \|P_{G_c}H_c\|_1+\|\delta H_c\|_1\le Cc^2,
 \quad c=\ell/(2\pi).
\]
Its residual pairing has the nonzero order \(c^3\) in (5). For any
global smooth symmetric tensor \(h\), put \(\eta=\|h\|_{C^2(G_c)}\).
Closed-manifold integration by parts and the full nonlinear Taylor
formula bound the change in this pairing by
\[
                         C(c^2\eta+c\eta^2).              \tag{9}
\]
This estimate imposes no symmetry, gauge, support, or mode restriction.
It proves that constants \(b,b_0>0\) exist with
\[
 \boxed{
 \|h\|_{C^2(G_c)}\le bc
 \quad\Longrightarrow\quad
 \|(G_c+h)^{-1}\operatorname{Ric}_{G_c+h}+3I\|_\infty
       \ge b_0c^2.}                                       \tag{10}
\]
The same ball contains no Einstein metric of **any** Einstein constant:
the test tensor is trace-free and the possible change of constant is
absorbed in (9). Diffeomorphism pullbacks are included among the tested
metrics. The \(O(c^2)\) scalar correction in (7) lies inside this ball,
so a comparable exclusion radius holds about \(\widehat g_\ell\).

This proves, in particular, that the constructed pointwise residual is
\(\Theta(\ell^2)\), while the excluded \(C^2\) repair radius is of
order \(\ell\). The entire conformal class also contains no Einstein
metric, by the separate argument in the global note.
The full all-mode proof is [round14_repair_radius.md](round14_repair_radius.md).

For this fixed-topology family there can therefore be no uniform correction
estimate \(d_{C^2}(g,\mathrm{Ein})\le C\delta_{-3}(g)^p\) with
\(p>1/2\), nor one of the form \(C\mathcal E(g)^p\) with \(p>1/5\).
All Einstein constants and diffeomorphism pullbacks are allowed in this
distance. The endpoint exponents are not excluded, and Yau26 itself asks
for existence rather than proximity.

## 4. What has changed, and what still decides Yau26

The progress is not a count of local formulas:

- The integral mechanism now applies to twisted gauge inputs, giving a
  concrete critical family beyond the ordinary-SW application class.
- A complete mixed equation is solved, and its remaining low-mode forces
  and end fluxes are computed rather than hidden in an error term.
- The collar complement is controlled on all tensor modes, and a
  nonlinear test excludes genuinely nonsymmetric small repairs.

The last point strengthens the prior statement that exact output would
have to break local symmetry. It gives an actual size constraint on
such a repair. It still leaves larger nonconformal, nonsymmetric
Einstein deformations and distant Einstein metrics possible.

The immediate closed problem is now the low-mode and boundary-response
system: couple the proven Dirichlet collar inverse to the actual exterior
blocks, keep their shape modes, and decide whether the signed throat forces
can balance after full nonlinear feedback. Neither a local kernel nor a
local Dirichlet inverse decides that system by itself.

The new twisted-obstructed manifolds and the near-Einstein shear manifolds
are different smooth objects. Connecting them by a surgery does not
preserve the constructed metrics; (1) actually forbids such preservation
in the critical cases. A Yau26 branch counterexample still requires a
near-Einstein sequence and absence of **all** Einstein metrics on the same
allowed object(s). Complete negation of the project's interval statement
requires both sign branches to fail in one fixed dimension. No such
complete negation, nor the unrestricted affirmative theorem, is obtained
in this round.

## 5. Proof and verification entry points

| File | Mathematical content |
| --- | --- |
| [round14_twisted_rigidity.md](round14_twisted_rigidity.md) | Invariant weights, genuine twisted classes, critical surgery family |
| [round14_rigidity.md](round14_rigidity.md) | Finite covers, explicit quotients, SW vanishing, shear budget saturation |
| [round14_shear.md](round14_shear.md) | Capacity, exact mixed equation, waist/shape forces and exported flux |
| [round14_collar_complement.md](round14_collar_complement.md) | Two radial modes and the full Dirichlet complement |
| [round14_global.md](round14_global.md) | Full-collar closed metrics, scalar calibration, volume and conformal classes |
| [round14_repair_radius.md](round14_repair_radius.md) | Nonlinear all-mode, all-Einstein-constant exclusion radius |
| [round14_verification.md](round14_verification.md) | Actual program runs, primary-source inputs, and mathematical cross-checks |

The five accompanying programs check exact finite identities. The weighted
gauge solvability, integral estimates, global scalar PDE, and nonlinear
exclusion arguments are supplied in the proofs and are not certified merely
by a program returning zero.
