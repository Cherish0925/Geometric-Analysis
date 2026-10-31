# Full tensor reduction on degenerating hyperbolic products

## 1. Scope, normalization, and relation to existing theory

Let \((B,g_B)\) and \((F,g_F)\) be arbitrary connected closed oriented
surfaces of genera \(b,f\ge2\), both of constant curvature \(-3\).
Put \(M=B\times F\), \(g_0=g_B+g_F\). Thus
\(\operatorname{Ric}_{g_0}=-3g_0\), but mixed sectional curvatures are
zero. Either factor may degenerate, and their genera need not be bounded.

Use nonnegative scalar and Hodge Laplacians. With
\(\delta h=-\nabla^ih_{ij}\), \(\delta^*\alpha=\frac12\mathcal L_{
\alpha^\sharp}g\), and \(\mathcal B h=\delta h+\frac12d\operatorname{tr}h\),
the full gauged operator is
\[
 P_0=D(\operatorname{Ric}+3g)_{g_0}+\delta^*\mathcal B
     =\tfrac12\Delta_L+3
     =\tfrac12\nabla^*\nabla-\mathring R.                    \tag{1}
\]
It acts on all symmetric two-tensors, not merely TT tensors. Our
curvature convention is \(\mathring Rg=\operatorname{Ric}\).

Product spectra and stability are classical. Kröncke's
[*On infinitesimal Einstein deformations*, Proposition 4.1 and §4](https://arxiv.org/pdf/1508.00721)
give the tensor-product spectrum, the relevant commuting identities,
and the negative-Einstein product kernel. The calculations below
specialize this structure to two-dimensional hyperbolic factors, with
an explicit proof of the surface identity, precise degenerating channels,
and uniform perturbative estimates. No new general product-stability
theorem or literature priority is claimed.

Koiso's [1980 rigidity paper](https://ir.library.osaka-u.ac.jp/repo/ouka/all/26044/04842_Dissertation.pdf)
explicitly excludes two-dimensional factors from its noncompact-symmetric
rigidity assertion. Those factors have the genuine deformation spaces
retained below.

This is also outside [Jäckel's Theorem 1.1](https://arxiv.org/html/2502.16692v2):
that theorem assumes strictly negative sectional curvature bounded away
from zero, and sectional curvature exactly \(-1\) in the thin part.
The products here satisfy neither assumption. Its uniform inverse theorem
cannot be imported into this problem by replacing the word hyperbolic
with product-hyperbolic.

## 2. The complete surface calculation

For either surface \(\Sigma\), define the trace-free conformal-Killing
operator
\[
 D_\Sigma\alpha=\delta^*\alpha+\tfrac12(\delta\alpha)g_\Sigma.
\]
On trace-free tensors its adjoint is \(D_\Sigma^*=\delta\).
Let
\[
 \mathcal T_\Sigma
   =\{q:\operatorname{tr}q=0,\ \delta q=0\}.
\]
These are the real parts of holomorphic quadratic differentials, with
\(\dim\mathcal T_\Sigma=6\operatorname{genus}(\Sigma)-6\).

The exact surface identities are
\[
 \boxed{
 P_\Sigma|_{S^2_0}=D_\Sigma\delta,
 \qquad \delta D_\Sigma=\tfrac12\Delta_H+3,
 \qquad P_\Sigma(ug_\Sigma)
       =(\tfrac12\Delta u+3u)g_\Sigma.}                     \tag{2}
\]
Here \(\Delta_H=\nabla^*\nabla-3\) on one-forms, since
\(\operatorname{Ric}=-3g\). In particular this is the Hodge Laplacian,
not the unshifted rough Laplacian.

One can derive (2) by commuting two derivatives and inserting
\(\mathring Rq=3q\) for trace-free surface tensors. More explicitly,
\[
 D\delta q=\tfrac12\nabla^*\nabla q-3q,
 \qquad
 \delta D\alpha=\tfrac12\nabla^*\nabla\alpha+\tfrac32\alpha.
\]
These expressions also follow directly in the local metric
\((dx^2+dy^2)/(3y^2)\) for arbitrary tensor entries, as checked by the
accompanying coordinate program. They are tensorial identities and apply
on every closed quotient.

The orthogonal decomposition is
\[
 L^2(S^2\Sigma)
  =L^2(\Sigma)g_\Sigma
       \ \widehat\oplus\ \mathcal T_\Sigma
       \ \widehat\oplus\ \overline{D_\Sigma\Omega^1(\Sigma)}.
                                                               \tag{3}
\]
In fact \(D\) has closed range from \(H^1\) to \(L^2\), because
\[
 \|D\alpha\|_2^2
  =\tfrac12\langle\Delta_H\alpha,\alpha\rangle
       +3\|\alpha\|_2^2.
                                                               \tag{4}
\]
The orthogonal complement of its range among trace-free tensors is
exactly \(\ker\delta=\mathcal T_\Sigma\). Equation (2) shows
\(Pq=0\) for \(q\in\mathcal T_\Sigma\), while
\[
 P D\alpha=D(\tfrac12\Delta_H+3)\alpha.                    \tag{5}
\]
Thus every nonzero surface branch outside \(\mathcal T_\Sigma\)
has eigenvalue at least \(3\).

For completeness, an orthonormal basis of one-forms consists of harmonic
forms and \(\lambda_i^{-1/2}du_i\),
\(\lambda_i^{-1/2}*du_i\) for positive scalar eigenvalues
\(\Delta u_i=\lambda_i u_i\). Applying
\(D(\frac12\Delta_H+3)^{-1/2}\) is an isometry onto the last
summand of (3). This normalization avoids treating a differential map
as an unweighted unitary identification.

## 3. Every product tensor sector

Let \(u_i\), \(v_j\) be scalar eigenbases on \(B,F\), with
eigenvalues \(\lambda_i,\nu_j\), including the normalized constant
functions at index zero. Let \(\alpha_r,\gamma_s\) be Hodge one-form
eigenbases with eigenvalues \(\mu_r,\xi_s\), including all harmonic
one-forms. Let \(q_a\), \(r_d\) be bases of
\(\mathcal T_B,\mathcal T_F\).

The following is a complete orthogonal system after the normalizations
in (3)--(5). A displayed tensor may be rescaled to norm one without
changing its eigenvalue.

| Tensor | Eigenvalue of \(P_0\) |
| --- | --- |
| \(q_a\,v_j\) | \(\nu_j/2\) |
| \(u_i\,r_d\) | \(\lambda_i/2\) |
| \(u_i v_j g_B\), \(u_i v_j g_F\) | \(3+(\lambda_i+\nu_j)/2\) |
| \((D_B\alpha_r)v_j\) | \(3+(\mu_r+\nu_j)/2\) |
| \(u_i(D_F\gamma_s)\) | \(3+(\lambda_i+\xi_s)/2\) |
| \(\alpha_r\odot\gamma_s\) | \(3+(\mu_r+\xi_s)/2\) |

Here \(\alpha\odot\gamma=(\alpha\otimes\gamma+
\gamma\otimes\alpha)/\sqrt2\), so tensor products of unit
one-forms have unit norm.

To verify completeness, use the orthogonal bundle splitting
\[
 S^2(T^*M)=S^2(T^*B)\oplus S^2(T^*F)
                         \oplus(T^*B\odot T^*F)
\]
and apply (3) to the first two blocks. Product covariant derivatives
preserve all three blocks. On a pure \(B\) tensor, \(P_0\) is
\(P_B+\frac12\Delta_F\). On a mixed tensor the curvature action
vanishes, while each rough one-form Laplacian is \(\Delta_H+3\).
This gives the last row, including the positive shift for harmonic
one-forms. There is no omitted mixed zero mode. The relative scaling
tensor \(g_B-g_F\) also has eigenvalue \(3\), not zero.

Define the entire exceptional channel
\[
 \mathcal L=
 [\mathcal T_B\widehat\otimes L^2(F)]
       \widehat\oplus
 [L^2(B)\widehat\otimes\mathcal T_F],
 \qquad \mathcal H=\mathcal L^\perp.                         \tag{6}
\]
All of \(\mathcal L\) is TT on the four-dimensional product. Multiplying
a fiber TT tensor by a base function creates no divergence because
the nonzero tensor slots remain entirely in the fiber.

**Complete complement theorem.** Independently of injectivity radius,
diameter, volume, and genus,
\[
 \boxed{\langle P_0h,h\rangle\ge3\|h\|_2^2
            \quad(h\in\mathcal H\cap H^1),}               \tag{7}
\]
whereas on \(\mathcal L\) the operator is exactly
\[
 \boxed{P_0|_{\mathcal L}
      =\tfrac12\Delta_F\text{ on each }\mathcal T_B
       \ \oplus\ \tfrac12\Delta_B\text{ on each }\mathcal T_F.}
                                                               \tag{8}
\]
The true kernel is only
\[
 \ker P_0=\mathcal T_B\otimes\mathbb R
           \oplus\mathbb R\otimes\mathcal T_F,
 \qquad \dim\ker P_0=6b+6f-12.                              \tag{9}
\]
These are the genuine factor Teichmüller deformations, and they integrate
to hyperbolic product metrics. Removing (9) does **not** remove the rest
of (6).

## 4. Exact inverse channels and their unavoidable degeneration

For a forcing orthogonal to (9), the inverse in the first channel is
\[
 \sum_a q_a\,F_a(y)\longmapsto
      2\sum_a q_a\,\Delta_F^{-1}F_a(y),\qquad \int_F F_a=0,
                                                               \tag{10}
\]
and the second channel uses \(2\Delta_B^{-1}\) in precisely the same
way. These are vector-valued scalar equations, not a finite list of
constant parameters.

The remaining inverse is diagonal in the complete table above. After
Hodge decomposition and the normalized \(D\) identification, every
coefficient is obtained from a positive shifted scalar resolvent
\[
 \bigl(3+\tfrac12(\Delta_B+\Delta_F)\bigr)^{-1},            \tag{11}
\]
or its specialization with a harmonic one-form label fixed. This is an
exact \(L^2\) description; reconstruction involves normalized differential
maps and does not automatically preserve maximum norms.

The optimal \(L^2\) spectral gap after removing only the kernel is
\[
 \boxed{\min\{3,\lambda_1(B)/2,\lambda_1(F)/2\}.}         \tag{12}
\]
For a separating hyperbolic degeneration, \(\lambda_1\to0\).
This last fact can be seen without a compactness theorem: take constants
on the two thick pieces and join them harmonically across the collar.
For \(a=c\cosh(kt)\), the least radial transition energy is
\[
 \frac{2\pi}{\int_{-R}^{R}a^{-1}dt}=O(c),
\]
while the mean-zero \(L^2\) mass on the fixed-area thick pieces stays
positive. Min--max gives the claim. Tensoring those scalar functions with
any \(r_d\in\mathcal T_F\) yields actual four-dimensional TT near-zero
modes. They are not gauge artifacts.

The gauge operator itself has no corresponding degeneration:
\[
 \mathcal B\delta^*\alpha=\tfrac12\Delta_H\alpha+3\alpha
                                                               \tag{13}
\]
on the Einstein product. Thus its \(L^2\) gap is at least \(3\),
including harmonic one-forms. At the exact product, a Bianchi-compatible
forcing and the kernel-orthogonal solution retain Bianchi gauge by the
commuting identity \(\mathcal B P_0=(\frac12\Delta_H+3)\mathcal B\).

### Fixed genus still requires many retained modes above the cusp threshold

There is a stronger obstruction to keeping only a uniformly fixed number
of low modes. Pinch one simple geodesic on a **fixed** closed surface
\(B_c\), and keep \(F\) fixed. For every \(\sigma>3/8\),
\[
 \boxed{\#\{\text{positive eigenvalues of }P_0\text{ below }\sigma}
                   \longrightarrow\infty.}                 \tag{14}
\]

Indeed on one half of the embedded collar the radial scalar Laplacian is
\(-a^{-1}(a\partial_t)'\). The unitary substitution \(v=\sqrt a\,u\)
gives the **exact** Schrödinger operator
\[
 -\frac{d^2}{dt^2}+\frac34
               +\frac34\operatorname{sech}^2(\sqrt3t).     \tag{15}
\]
Choose \(3/4<\Lambda<2\sigma\) and a fixed \(T\) so large that
the potential on \([T,R_c]\) is at most \(3/4+\epsilon<\Lambda\).
The first \(N\) Dirichlet sine functions on this interval span a
space with Rayleigh quotient at most
\[
 \frac34+\epsilon+\frac{N^2\pi^2}{(R_c-T)^2}.
\]
Extend their corresponding radial functions by zero to \(B_c\);
these are legitimate \(H^1\) test functions. Taking
\(N\) proportional to \(R_c-T\asymp\log(1/c)\), min--max
gives at least \(N\) scalar eigenvalues below \(\Lambda\), counting
the constant mode at most once. The table then gives positive TT
eigenvalues below \(\sigma\), multiplied by \(6f-6\).

Thus no fixed-dimensional projection can preserve a uniform lower
bound greater than \(3/8\) on the remaining tensors throughout this
fixed-genus degeneration. This does not exclude a finite reduction at
a smaller positive threshold for fixed genus. If genus varies, even
the zero-mode dimension in (9) is unbounded. After removing those zero
modes, arbitrarily many additional eigenvalues can be made smaller than
any prescribed positive number by joining sufficiently many fixed
hyperbolic pieces with sufficiently short separating collars and using
the same capacity test on piecewise constants.

## 5. Uniform Sobolev control of the full complement

Let \(\Pi\) denote the orthogonal projection onto (6), and \(Q=I-\Pi\).
Use the geometric norm
\(\|h\|_{H^2}^2=\sum_{j=0}^2\|\nabla^jh\|_2^2\).
The complement inverse satisfies
\[
 \boxed{\|(P_0|_{\mathcal H})^{-1}F\|_{H^2}
                                  \le C\|F\|_2,}          \tag{16}
\]
with a universal constant. In particular the statement includes trace,
mixed, conformal-Killing, and all high-frequency sectors, not just one
TT projection.

Here is an injectivity-independent proof of the required global estimate.
The curvature action has operator norm at most \(3\), so
\[
 \|\nabla h\|_2^2\le2\langle P_0h,h\rangle+6\|h\|_2^2.
                                                               \tag{17}
\]
Since \(\nabla\operatorname{Rm}=0\), covariant integration by parts
and one derivative commutation give
\[
 \|\nabla^2h\|_2^2
 \le\|\nabla^*\nabla h\|_2^2+C\|\nabla h\|_2^2+C\|h\|_2^2.
                                                               \tag{18}
\]
The constant depends only on the dimension and the fixed curvature tensor.
Use \(\nabla^*\nabla h=2P_0h+2\mathring Rh\) in (18), and
use \(\langle P_0h,h\rangle\le\|P_0h\|_2\|h\|_2\) in (17).
This proves the uniform graph-norm equivalence
\[
 \|h\|_{H^2}\le C(\|P_0h\|_2+\|h\|_2).                 \tag{19}
\]
For \(h\in\mathcal H\), (7) supplies
\(\|h\|_2\le\frac13\|P_0h\|_2\), proving (16).
No coordinate ball or Sobolev embedding is used.

Because \(\Pi\) commutes with \(P_0\) and is an \(L^2\) projection,
(19) also proves that \(\Pi,Q\) are bounded on \(H^2\), with
universal constants. This remains true when the number of factor
deformation modes grows. Neither (16) nor (19) implies an
injectivity-independent \(C^{2,\alpha}\) inverse in dimension four.

## 6. The complement persists under actual small metric perturbations

This section concerns any smooth metric \(g\) on the **same product**
satisfying
\[
 \|g-g_0\|_{C^2(g_0)}\le\epsilon.
                                                               \tag{20}
\]
It need not be a product or Einstein and may have all tensor modes.
Define \(P_g=\frac12\Delta_{L,g}+3\); at a non-Einstein metric it
is still self-adjoint and equals the gauged first variation
\(D(\operatorname{Ric}+3g)_g+\delta_g^*\mathcal B_g\).

To compare Hilbert spaces exactly, write \(C=g_0^{-1}g\) and use the
\(L^2\)-unitary fiber identification
\[
 (Uh)(X,Y)=(\det C)^{-1/4}
                   h(C^{1/2}X,C^{1/2}Y).
                                                               \tag{21}
\]
It maps \(L^2(g_0)\) to \(L^2(g)\). Its coefficients and first two
derivatives differ from the identity by \(O(\epsilon)\).
Set \(\widetilde P=U^{-1}P_gU\).

Uniform tensor coefficient estimates give
\[
\begin{aligned}
 |\langle(\widetilde P-P_0)h,h\rangle_0|
   &\le C\epsilon(\|\nabla h\|_2^2+\|h\|_2^2),\\
 \|(\widetilde P-P_0)h\|_2
   &\le C\epsilon\|h\|_{H^2}.                              \tag{22}
\end{aligned}
\]
For the first estimate, compare the rough-gradient quadratic forms and
the algebraic Ricci/curvature terms in \(\Delta_L\). For the second,
compare the second-, first-, and zeroth-order covariant coefficients.
All needed changes are controlled by (20); no derivative of curvature
or noncollapse is required.

For \(h\in\mathcal H\), equations (7) and (17) show
\(\|\nabla h\|_2^2\le4\langle P_0h,h\rangle\).
For a universal \(\epsilon_0>0\), (22) therefore implies
\[
 \boxed{\langle\widetilde P h,h\rangle_0
       \ge\tfrac12\langle P_0h,h\rangle_0
       \ge\tfrac32\|h\|_2^2
       \quad(h\in\mathcal H,\ \epsilon\le\epsilon_0).}    \tag{23}
\]
This is a genuine uniform all-mode complement estimate on the transported
reference high space \(U\mathcal H\), not a claim about the moving
low eigenspaces of \(P_g\).

The compressed operator
\[
 A_{HH}=Q\widetilde P Q:
            H^2\cap\mathcal H\longrightarrow\mathcal H
\]
has a uniformly bounded inverse
\[
 \boxed{\|A_{HH}^{-1}F\|_{H^2}\le C\|F\|_2,
              \qquad \|A_{HH}^{-1}\|_{L^2\to L^2}\le2/3.} \tag{24}
\]
Indeed factor it by \(P_0|_{\mathcal H}\). Equations (16), (22),
and uniform \(H^2\) boundedness of \(Q\) show that the resulting
error on \(H^2\cap\mathcal H\) has norm \(O(\epsilon)\).
A Neumann series proves the first estimate and surjectivity; (23)
proves the second. This also identifies the operator-domain solution,
rather than stopping at a weak quadratic-form assertion.

## 7. The low equation is a full PDE with controlled high feedback

Let \(A_{LL},A_{LH},A_{HL},A_{HH}\) be the blocks of
\(\widetilde P\) under (6). For forcing \((F_L,F_H)\), the exact
linear elimination is
\[
\begin{aligned}
 h_H&=A_{HH}^{-1}(F_H-A_{HL}h_L),\\
 (A_{LL}-A_{LH}A_{HH}^{-1}A_{HL})h_L
      &=F_L-A_{LH}A_{HH}^{-1}F_H.                            \tag{25}
\end{aligned}
\]
The off-diagonal blocks vanish at the exact product and are
\(O(\epsilon):H^2\to L^2\). Consequently the Schur correction is
\(O(\epsilon^2):H^2\cap\mathcal L\to L^2\cap\mathcal L\),
whereas the direct low perturbation is \(O(\epsilon)\). The underlying
principal reference operator is (8), not a finite matrix.

Every mode eliminated in (25) feeds back into both the low operator and
the low forcing. Solving only its projection onto the constant
Teichmüller kernel is insufficient. Moreover, the uniform \(H^2\)
theory does not by itself supply a quadratic Einstein contraction:
four-dimensional \(H^2\) is not a uniform algebra controlling
\(C^2\), and the nonlinear equation and gauge have not been solved.

The global product hypothesis is also essential. A fixed integer-shear
manifold need not be diffeomorphic to \(B\times F\), and its collarwise
product appearances do not create the global projectors (6). The present
theorem supplies the complete model operator and a genuine neighborhood
complement theorem where a global product reference exists. To use it
on a sheared gluing one still needs compatible local projectors,
commutator estimates, actual transmission data, and the remaining low
PDE. Those are mathematical tasks, not assumed corollaries.

## 8. What this changes in the research problem

The product model has now been reduced without discarding tensor modes:

1. All scalar, gauge-generated, mixed, and complementary trace-free
   sectors have a uniform positive inverse, including small nonproduct
   perturbations in the stated geometric \(C^2\) neighborhood.
2. Every small denominator is carried by an explicit scalar Laplacian
   acting on factor Teichmüller coefficients. These are genuine TT
   fields, so gauge fixing does not remove the difficulty.
3. A uniform finite-dimensional replacement is not generally possible:
   long collars accumulate modes above the \(3/8\) tensor threshold,
   even with fixed topology; varying genus creates further arbitrarily
   small branches and unbounded exact kernel dimension.
4. The next equation is therefore an effective Teichmüller-valued PDE
   with the high Schur term retained, not another isolated waist
   coefficient or a blanket negative-curvature stability citation.

These conclusions specialize established product spectral geometry to
the precise degeneration relevant here. They do not settle the nonlinear
Einstein problem on the shear manifolds or a Yau26 sign branch.

`round17_product_operator_check.py` independently constructs the surface
connection and verifies (2), (5), the curvature block action, all spectral
shifts, the exact collar potential, and Schur algebra. Its ten groups
include rejection of omitted feedback. Global Hodge completeness,
min--max, and uniform perturbation bounds are analytic arguments above,
not consequences of finite program success.
