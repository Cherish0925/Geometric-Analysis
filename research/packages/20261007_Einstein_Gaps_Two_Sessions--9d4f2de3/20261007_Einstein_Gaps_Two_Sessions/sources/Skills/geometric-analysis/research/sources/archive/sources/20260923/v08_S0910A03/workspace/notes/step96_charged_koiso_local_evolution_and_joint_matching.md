# Step 96: charged Koiso local evolution and the genuine joint matching object

Session `S0910A03`, Agent3 / Execute.

## 1. Route correction

The radial curved-base BVP proposed at the end of Step 95 was not run.  If every
coefficient depends only on the normal variable, each induced `r=const` three-torus
still has constant coefficients and is intrinsically flat, even when the two-dimensional
quotient metric is written as `dr^2+phi(r)^2 dz^2` and a radial connection is present.
The established flat-slice identity then forces
\[
\mathcal H^2\ge 9-6\delta,
\]
so a cylindrical change of the sign of mean curvature costs at least
\(\delta=3/2\).  The charged Koiso center is not radial: its orbit matrix winds
nontrivially with the separator coordinate.  Replacing it by radial data would erase
the very curvature mechanism that evades the flat-slice theorem.

The two other premises in the Step 95 route map were also not used.  A general
minimal invariant separator need not have \(\nabla\sigma=0\), and
\(L\sigma\ge6\) is an elliptic trace equation, not a bound on transition length.
An exterior resolvent has entrance data and cannot inherit the complete-base ceiling.

## 2. Full spatially varying Einstein Cauchy system

Write a four-metric in Gaussian normal form around the charged separator,
\[
 g=dn^2+q_{ij}(n,s)dy^i dy^j,
 \qquad y=(s,x^1,x^2),
\]
where all coefficients are `T^2`-invariant but retain their full periodic `s`
dependence.  Put
\[
 K=\frac12\partial_nq,
 \qquad W=q^{-1}K,
 \qquad H=\operatorname{tr}W.
\]
The tangential Einstein equations for \(\operatorname{Ric}_g=-3g\) are
\[
 \boxed{\partial_nq=2K},
 \qquad
 \boxed{\partial_nK=\operatorname{Ric}(q)+3q-HK+2Kq^{-1}K}.
 \tag{2.1}
\]
The constraints are
\[
 \boxed{R(q)-H^2+|W|^2=-6},
 \qquad
 \boxed{\operatorname{div}_qK-dH=0}.
 \tag{2.2}
\]
These signs and the momentum index order were independently checked.  The original
implementation briefly used the wrong derivative index in the momentum evaluator;
it was corrected before interpreting evolution output.  A symbolic general-matrix
calculation in
`workspace/scripts/step96_symbolic_initial_constraints.py` verifies
\[
 (\operatorname{div}W)_s=-\operatorname{tr}(AB),
 \qquad
 (\operatorname{div}W)_a=(\operatorname{tr}A)m_a
\]
after the two vertical connection terms cancel.  With `det M=1`, constant mixed
covector \(m\), and target-normal vertical block \(B\), all momentum components
vanish.  The exact expressions and zero residuals are in
`workspace/data/step96_symbolic_initial_constraints.json`.

Equation (2.1) is elliptically ill-posed as normal evolution.  It is used only to
probe the analytic Koiso germ at very short distance; local existence itself follows
from the analytic Cauchy theorem and constraints, not from the numerics.

## 3. Quotient reconstruction in Gaussian gauge

Decompose each slice as
\[
 q=a^2ds^2+G_{ab}(dx^a+\mathcal A_s^a ds)
                    (dx^b+\mathcal A_s^b ds).
 \tag{3.1}
\]
If \(v_a=q_{as}\), then
\[
 G=q|_{\rm vert},\qquad
 \mathcal A_s=G^{-1}v,\qquad
 a^2=q_{ss}-v^TG^{-1}v.
\]
In temporal connection gauge \(\mathcal A_n=0\),
\[
 F_{ns}=\partial_n\mathcal A_s,
 \qquad f=\frac{\partial_n\mathcal A_s}{a}
\]
is its coefficient in the orthonormal base frame.  With
\[
 \rho=\sqrt{\det G}=e^\sigma,
 \qquad M=\rho^{-1}G,
\]
the conserved coordinate charge and physical twist energy are
\[
 c=\rho Gf,
 \qquad Q=\frac12f^TGf
 =\frac12c^T(e^{-3\sigma}M^{-1})c,
 \tag{3.2}
\]
and
\[
 e^{-3\sigma}M^{-1}=\rho^{-2}G^{-1},
 \qquad d\mu_\sigma=\rho a\,dn\,ds.
\]
The connection potential itself is gauge dependent; curvature, `dc=0`, and the
outer holonomy are the invariant data relevant to matching.

## 4. Exact center Taylor geometry

For the charged Koiso family of Step 94,
\[
 H=0,\qquad |W|^2=S,\qquad
 R(q_\Sigma)=-6-S,
\]
with \(0<S<3\), fixed nonzero charge \(c\), and
\[
 Q(s)=\frac12c^TM(s)^{-1}c<S.
\]
The first nontrivial normal coefficients can be derived directly, without numerical
marching.

The normal Einstein equation gives
\[
 \boxed{H_n=3-S}.
 \tag{4.1}
\]
For the sample \(S=1\), \(H_n=2\).  Reversing the normal reverses \(K\), but at
the minimal slice both sides have the same positive derivative in their respective
outward directions: the exact germ initially expands away from the separator on both
sides.

The tangential `ss` equation and Schur complement give
\[
 \boxed{a_n=0,\qquad a_{nn}=-3-S-Q(s)}.
 \tag{4.2}
\]
Since the slice volume density is \(a\rho\),
\[
 H=\partial_n\log(a\rho)=a_n/a+\sigma_n.
\]
Thus
\[
 \boxed{\sigma_n=0,\qquad \sigma_{nn}=6+Q(s)}.
 \tag{4.3}
\]
The center therefore immediately separates base-circle contraction from orbit-area
expansion:
\[
 a=1-\frac12(3+S+Q)n^2+O(n^3),
 \qquad
 \rho=1+\frac12(6+Q)n^2+O(n^3).
\]
This is a genuine two-variable escape from the flat-slice model: \(Q\) and the
orbit shape vary with `s`, and the intrinsic separator scalar curvature supplies the
missing negative curvature.

The complete computation in
`workspace/scripts/step96_initial_taylor_invariants.py` gives, for \(S=1\),
\[
 H_n=2\quad(10^{-10}\text{ residual}),
\]
\[
 a_{nn}\in[-4.5,-4.0086233],
 \qquad
 \sigma_{nn}\in[6.0086233,6.5].
\]
It also reconstructs constant coordinate charge with standard deviation
\(1.1\times10^{-15}\) and \(\max|c_n|<9.8\times10^{-14}\).  Physical \(Q\)
varies because the area and orbit matrix vary; charge conservation does not make
\(Q\) constant.

## 5. Short spectral evolution

`workspace/scripts/step96_koiso_einstein_cauchy_evolution.py` implements (2.1)
with Fourier differentiation in `s` and optional 2/3 filtering.  It evolves the full
symmetric `3 x 3` tensors, including the mixed connection block; it is not the
excluded radial cylindrical model.

At \(n=0.02\), \(S=1\), `wind=1`, and \(Q_{\max}(0)=1/2\), the `N=96` run gives
\[
 \lambda_{\min}(q)=0.127455,
 \quad H\in[0.03545,0.03668],
\]
\[
 a\in[0.9990785,0.9991693],
 \quad \rho\in[1.0012022,1.0013013],
 \quad Q_{\max}=0.5095580.
\]
The second-order predictions from (4.2)--(4.3) agree at the displayed scale.  The
Hamiltonian and momentum residuals at `N=48,64,96` are respectively
\[
 (8.32\times10^{-2},5.79\times10^{-2}),
\quad(9.96\times10^{-3},1.01\times10^{-2}),
\quad(1.32\times10^{-4},2.29\times10^{-4}).
\]
The rapid resolution improvement and convergence of \(Q_{\max}\) between `N=64`
and `N=96` support the Taylor implementation on this extremely short collar.  They
do not support order-one continuation, completeness, an expanded end, or a two-end
connector.  Longer runs are dominated by the expected ill-posed high-frequency
growth and are not used as geometric evidence.

Canonical data:
`workspace/data/step96_koiso_einstein_cauchy_evolution_N96_short.json`.

## 6. Relative `K_X` diagnostic: what it does and does not test

For a compactly supported quotient vector field \(X\), define
\[
 \mathcal R_X=
 \frac{\left|\frac12\int c^TK_Xc\,d\mu_\sigma\right|}
 {\int(2|\operatorname{sym}\nabla X|+\sqrt2|\operatorname{div}_\sigma X|
       +|\operatorname{div}X|+|dU(X)|)\,d\mu_\sigma},
\]
\[
 K_X=X(A)+(\operatorname{div}_\sigma X)A,
 \qquad A=e^{-3\sigma}M^{-1}.
 \tag{6.1}
\]
The coefficients in the denominator are the direct operator-norm-to-Hilbert--Schmidt
conversion for the verified horizontal pairing.

On the short exact fixed-charge germ, however, this is deliberately a null control,
not an obstruction.  Pointwise,
\[
 \frac12c^TK_Xc=\operatorname{div}_\sigma(QX)-m_c(X).
\]
Because `dc=0`, \(m_c=0\), so the integrated numerator vanishes by ordinary
integration by parts for every compactly supported \(X\), independently of the
Einstein or horizontal Noether equations.  For
\(X=\sin^4(\pi n/L)\partial_n\), \(L=0.02\), the implementation gives
\(\mathcal R_X\sim 4.8\times10^{-11}\) at `N=96`; large positive and negative
slice integrands cancel.  This checks the `K_X` implementation and numerical charge
conservation only.  It is not an independent Noether validation and cannot create a
local obstruction.  The corrected script/data are
`workspace/scripts/step96_relative_KX_diagnostic.py` and
`workspace/data/step96_relative_KX_diagnostic.json`.

This result sharpens the strategist's relative-source lesson: a useful \(X\) must
come from a global adjoint problem spanning the center and both ends.  A compactly
supported local choice has identically zero numerator on the exact charged germ, and
a favorable pointwise sign of `K_X` is offset by the boundary/divergence structure.

## 7. The joint two-end matching map

The next consequential object is a gauge-fixed mixed-order elliptic problem on the
whole quotient cylinder
\[
 \Omega=\mathbb R_\tau\times S^1_s,
 \qquad
 \gamma=e^{2\varphi}(d\tau^2+ds^2),
 \qquad
 G=e^\sigma M(U).
\]
The unknowns retain all `s` modes:
\[
 V=(\varphi,\sigma,U,q,A; p),
\]
where `A` is in Coulomb gauge with fixed end holonomies and `p` contains parameters
shared by both halves: the center \(S\), charge vector, target phase/frame, plus the
two end scales and asymptotic orbit shapes.  The same center parameters must satisfy
both end problems.

The normalized residual map is
\[
 \mathscr E(V)=(H,T,Z,\mathcal B),
 \tag{7.1}
\]
where
\[
\begin{aligned}
 H={}&\operatorname{Ric}_\gamma-\operatorname{Hess}\sigma
 -\frac12d\sigma^2-\frac12U^*h-Q\gamma+3\gamma,\\
 T={}&L\sigma-6-Q,\\
 Z={}&\tau_\sigma(U)+\nabla_UQ,\\
 \mathcal B={}&e^{-3\sigma/2}M^{-1/2}dq.
\end{aligned}
\tag{7.2}
\]
The last block has \(|\mathcal B|=2|E_{\rm mix}|_{\rm HS}\).  `q` is a first-order
charge variable, not a fictitious second-order sigma-model field.

The second-order principal block in conformal base coordinates is
\[
 DT_2=e^{-2\varphi}\Delta_0\dot\sigma,
 \quad DZ_2=e^{-2\varphi}\Delta_0\dot U,
\]
\[
 D(\operatorname{tr}H)_2=e^{-2\varphi}
 (-2\Delta_0\dot\varphi-\Delta_0\dot\sigma),
 \quad D\mathcal B_1=e^{-3\sigma/2}M^{-1/2}d\dot q+\cdots .
\tag{7.3}
\]
After Coulomb/conformal gauge fixing and removal of the true Bianchi redundancy this
is a Douglis--Nirenberg elliptic system.  The principal-symbol audit in
`workspace/scripts/step96_linear_matching_symbol.py` gives
\[
 \det P_{(\varphi,\sigma,U)}=-2|\xi|^8,
 \qquad \det(P^*P)=4|\xi|^{20}
\]
for the scalar/map block together with the two first-order `dq` blocks; the generic
symbol rank is all six unknown directions.  This establishes principal injectivity,
not the Fredholm index.  Its indicial modes and finite cokernel have not yet been
computed (`workspace/data/step96_linear_matching_symbol.json`).

A two-half Dirichlet-to-Neumann form makes the shared-parameter condition explicit:
solve from each expanded end toward the exact Koiso collar and require both returned
Cauchy data to equal the same
\(W(S,c,\text{target phase})\).  The finite matching map must simultaneously contain:

1. two-component charge flux from center `c` to zero in each exact OT end;
2. flat-connection holonomy at both ends;
3. all center Dirichlet--Neumann shape and horizontal conditions;
4. projections onto genuine adjoint modes of the full operator.

Independent projection families are:

* weighted TT/Hopf tensors paired with \(\mathring H\), detecting relative end length
  and phase;
* global Noether fields `X_j` solving the adjoint boundary problem, not
  \(X=\nabla\sigma\) (which only rearranges the area equation at fixed charge);
* the three target-Killing currents of `H^2`, detecting whether orbit shape, target
  phase, and charge direction match simultaneously.

An exact fixed-charge bridge, if it reached expanding ends, would exhibit a cheap
redshift direction: a charge taper placed at distance `R` has
\[
 \|\mathcal B\|_\infty=O(e^{-3R}/\ell),
 \qquad \|Q\|_\infty=O(e^{-6R}).
\]
This does not construct the bridge; it says why the full linearized matching map must
be studied as `R` grows.  A decisive computation is the smallest singular value and
left singular field of the compactified Fourier--Chebyshev linearization including
all blocks in (7.2).  Exponential decay of the singular value with a left field
escaping to infinity identifies a redshift near-kernel.  Convergence to a positive
value or a bounded left zero mode with nonzero center pairing identifies the finite
obstruction that the local `K_X` test cannot see.

## 8. Scope relative to Yau 26

The exact charged center has now been advanced from a constraint-only local example
to a quantitatively checked two-variable local evolution and a precise all-block,
shared-parameter global matching formulation.  The center immediately expands on
both sides, so local geometry does not supply a no-neck theorem; the unresolved
issue is global matching and charge removal.  No two-ended small-defect connector
has been constructed or excluded, and no closed no-Einstein manifold has been
connected to this local family.  This remains a restricted free-`T^2` negative-side
program; it does not decide the positive sign branch, nonsymmetric metrics, higher
dimensions, or the original Yau-26 quantifiers, and it is not ready for Lean
formalization.
