# Full connector budgets and a sharp nonpositive-curvature obstruction

20 September 2026. This note concerns the complete free twisted T² cylinder
with two exact outward expanding hyperbolic T³ ends. The unconditional
small-Ricci-defect question remains open: no escaping family is constructed
here.

There are two new conclusions. First, the full quotient equations and
four-dimensional characteristic forms give an exact Weyl–twist energy
balance, including both physical end volumes. Second, a connector with
nonpositive sectional curvature has Ricci defect at least 3/2; this constant
is sharp as an infimum among smooth metrics with the prescribed exact ends.
The second conclusion needs no torus symmetry. The separate note
`round5_rank_obstruction.md` gives the general-dimensional flat-torus
argument and its sharpness construction.

## 1. The full metric, normalization and exact ends

Let B be a cylinder and let the principal T² bundle over B be marked by a
fixed integral lattice. Such a bundle is trivial, since H²(B;Z²)=0. Write

\[
 g=\gamma+G_{ab}(d\xi^a+\mathcal A^a)(d\xi^b+\mathcal A^b),
 \qquad G=\rho M,\quad \rho=e^\sigma,\quad\det M=1.
 \tag{1.1}
\]

The quotient metric, positive matrix M and connection may depend on both
base variables. No diagonal, orthogonal-transitivity, radial or reflection
assumption is imposed. Let U denote the shape map into H² with normalization

\[
 e=|dU|^2=\tfrac12\operatorname{tr}(M^{-1}dM\,M^{-1}dM).
\]

Put dA=f dμ_γ and define

\[
 q=\rho^2Mf,\qquad Q=\tfrac12f^TGf
       =\tfrac12\rho^{-3}q^TM^{-1}q\ge0.
 \tag{1.2}
\]

The Ricci error and its horizontal and vertical restrictions are

\[
 E=\operatorname{Ric}+3g,\quad E_B,E_V,\qquad
 \epsilon=\|g^{-1}E\|_{\infty,\mathrm{op}}.
\]

For reference, all reduced Ricci blocks retained in the argument are

\[
 \begin{aligned}
 E_B&=\operatorname{Ric}_\gamma-\nabla^2\sigma
      -\tfrac12d\sigma^2-\tfrac12U^*h-Q\gamma+3\gamma,\\
 (\Delta+\nabla\sigma\cdot\nabla)\sigma
      &=6+Q-\operatorname{tr}E_V,\\
 \tau_\sigma U+\nabla_UQ&=\mathscr Z,\qquad |\mathscr Z|\le2\epsilon,\\
 \mathscr B&=\rho^{-3/2}M^{-1/2}dq,\qquad
       |\mathscr B|^2=4|E_{\rm mix}|_{\rm HS}^2.
 \end{aligned}
 \tag{1.3}
\]

Here the last line uses the Hilbert–Schmidt norm of one rectangular mixed
block, not twice that norm in the full symmetric tensor. The bounds on
the shape residual are those of round 2. The identities below do not set
any of these blocks to zero.

On each end, in its own outward coordinate t, assume exactly

\[
 g=dt^2+e^{2t}h_\pm,
 \tag{1.4}
\]

where h_± is a flat metric on the actual marked T³. Thus in quotient
coordinates γ=dt²+b_±²e^{2t}ds², ρ=c_±e^{2t}, M is constant and F=0.
Flat connection holonomy is allowed. Coordinates have fixed periods;
their period cell has area C_Λ, so dV_g=C_Λ ρ dμ_γ after fibre integration.
Changing a coordinate origin does not change a physical boundary volume.

Let D⊂B be a compact cylinder bounded by sections in these exact ends and
let Ω=π^{-1}(D). Write

\[
 V_D=\operatorname{Vol}_g(\Omega),\qquad
 A_D=\operatorname{Vol}_g(\partial\Omega).
\]

Each component of the boundary has outward shape operator +I. Increasing
an end cutoff by a adds volume (e^{3a}−1) times its previous boundary
volume divided by three.

## 2. Exact physical volume and twist balance

**Proposition 2.1.** The quantity

\[
 V_{\rm ren}=V_D-A_D/3
 \tag{2.1}
\]

is independent of the cutoffs once they lie in the exact ends, and

\[
 \boxed{\quad 6V_{\rm ren}
       =\int_\Omega(\operatorname{tr}E_V-Q)\,dV_g.\quad}
 \tag{2.2}
\]

In particular, for ε<3,

\[
 (6-2\epsilon)V_D+\int_\Omega Q\,dV_g\le2A_D,
 \qquad V_D\le\frac{A_D}{3-\epsilon}.
 \tag{2.3}
\]

**Proof.** The vertical trace equation is equivalently

\[
 \Delta_\gamma\rho=(6+Q-\operatorname{tr}E_V)\rho.
\]

Its boundary flux is 2ρ on either exact end. Multiply by C_Λ and integrate.
This gives 6V_D+∫Q−∫tr E_V=2A_D, hence (2.2) and (2.3).
The cutoff independence is also immediate from the explicit end volumes.
Every factor here is a physical volume; no lower torus covolume is assumed.

The upper bound on V_D is relative to the chosen physical end sections.
It is not a uniform volume bound when those sections or their lattices vary.
In particular, it is not legitimate to let a cutoff run outward and then
regard A_D as fixed.

## 3. Weyl–twist balance and chirality

Weyl norms in this section are Hilbert–Schmidt norms as operators on Λ².
Thus the Euler density is
`|W|²−|Ric°|²/2+s²/24`, and a Kähler W+ has norm squared s²/24.

**Theorem 3.1.** With the preceding hypotheses,

\[
 \boxed{\quad
 \int_\Omega (|W|^2-Q)\,dV_g
 =\int_\Omega\left[
       \operatorname{tr}E_B+\tfrac12|E|^2
                       -\tfrac16(\operatorname{tr}E)^2
                    \right]dV_g.\quad}
 \tag{3.1}
\]

Moreover,

\[
 \int_\Omega|W^+|^2\,dV_g
       =\int_\Omega|W^-|^2\,dV_g
       =\tfrac12\int_\Omega |W|^2\,dV_g.
 \tag{3.2}
\]

All integrands in these formulas vanish on the exact ends except the
displayed volume terms before cancellation. If K is any compact region
containing the nonhyperbolic region, then

\[
 \left|\int|W|^2-\int Q\right|
       \le(2\epsilon+2\epsilon^2)\operatorname{Vol}(K).
 \tag{3.3}
\]

**Proof.** The Euler characteristic of Ω≅T³×[0,1] is zero. The
Gauss–Bonnet boundary transgression for a flat boundary with outward shape
operator I is −2 times its volume. Consequently,

\[
 0=\int_\Omega\left(|W|^2-\tfrac12|E^\circ|^2
              +\tfrac1{24}(-12+\operatorname{tr}E)^2\right)dV_g
              -2A_D.
 \tag{3.4}
\]

One can verify the boundary coefficient without an asymptotic expansion:
the intrinsic curvature is zero and the transgression is a universal
multiple of det(I); applying it to a hyperbolic torus slab, with shape
operators I and −I, gives precisely −2A_D with oriented boundary signs.
Substitute (2.2) in (3.4). The remaining quadratic expression is

\[
 \tfrac12|E^\circ|^2-\tfrac1{24}(\operatorname{tr}E)^2
       =\tfrac12|E|^2-\tfrac16(\operatorname{tr}E)^2,
\]

which proves (3.1). This calculation is the exact-end specialization of
the Chern–Gauss–Bonnet/renormalized-volume relation; no Einstein assumption
has been inserted into the interior.

For (3.2), conformally compactify with x=e^{−t} near each end. The resulting
metric is dx²+h_± near its boundary and is flat there. The tangent bundle
of T³×[0,1] has a global frame. Choose the quotient angular coordinate
affine on each boundary and extend it over the annulus; in the global
principal-bundle trivialization, remove the periodic exact parts of the
flat end connections by gauges supported in disjoint end collars.
The remaining connection holonomies and all end metric coefficients are
constant in this one global angular framing; any required integral affine
basis change is constant and introduces no framing winding.
Apply Gram–Schmidt to the resulting global coordinate frame;
near either flat product boundary its connection form is zero, since the
flat metric coefficients there are constant. The Pontryagin form is the
exterior derivative of the Chern–Simons form of this global frame, so its
integral is zero. The four-dimensional Pontryagin density is a universal
multiple of (|W+|²−|W−|²)dV, and this density is conformally invariant.
This proves (3.2) without a boundary-eta convention.

Finally, if λ_i are the four eigenvalues of E, |λ_i|≤ε. The quadratic
term R_E in (3.1) obeys

\[
 -\tfrac23\epsilon^2\le
 R_E=\tfrac12\sum_i\lambda_i^2-\tfrac16(\sum_i\lambda_i)^2
 \le2\epsilon^2.
 \tag{3.5}
\]

The upper bound follows by dropping the negative term. For the lower
bound use (∑λ_i)²≤4∑λ_i². Since |tr E_B|≤2ε, (3.3) follows.

The upper and lower quadratic constants in (3.5) are attained by
(ε,ε,−ε,−ε) and (ε,ε,ε,ε), respectively.

## 4. The unweighted base Gauss–Bonnet identity

Let L_D be the sum of the γ-lengths of the two boundary circles. Direct
tracing of (1.3) gives

\[
 K_\gamma=\tfrac14(e-|d\sigma|^2)+\tfrac32Q
             +\tfrac12(\operatorname{tr}E_B-\operatorname{tr}E_V).
 \tag{4.1}
\]

The outward boundary geodesic curvatures are +1. Gauss–Bonnet and the
integrated area equation therefore imply

\[
 \boxed{\quad
 \int_D(e+5Q)\,d\mu_\gamma
  =6(\operatorname{Area}_\gamma(D)-L_D)
       -2\int_D\operatorname{tr}E_B\,d\mu_\gamma
       +\int_D\operatorname{tr}E_V\,d\mu_\gamma.\quad}
 \tag{4.2}
\]

Both sides are again cutoff independent. Notice that this is an
unweighted two-dimensional identity, whereas (2.2) and (3.1) use the full
physical four-volume. Replacing one measure by the other would amount to
an unjustified orbit-covolume bound. The sign of the renormalized base
area in (4.2) is not controlled by the cylinder topology alone.

## 5. A sharp obstruction with no torus symmetry

**Theorem 5.1.** Let g be any smooth complete metric on R×T³, equal to
dt²+e^{2t}h_± outside a compact set at its two ends, with both t coordinates
pointing outward. If all sectional curvatures are nonpositive, then

\[
 \|g^{-1}(\operatorname{Ric}+3g)\|_{\infty,\mathrm{op}}\ge\tfrac32.
 \tag{5.1}
\]

The infimum 3/2 is sharp among such smooth nonpositively curved exact-end
metrics. Neither a torus action nor a lower injectivity radius is required.

**Proof of the lower bound.** Every nontrivial free homotopy class contains
a closed length-minimizing geodesic. Here is the necessary compactness
argument, since the manifold is not compact. A noncontractible loop entirely
past t=R in an exact end has length at least e^R sys(h_±), by projection
to its marked flat torus. Thus a sequence of loops of bounded length in a
fixed nontrivial class has points in one fixed compact set. Every remaining
point of those loops lies in a fixed metric neighborhood of that set. This
neighborhood is compact by completeness. The usual direct-method argument,
including the positive injectivity radius on this compact set, supplies
a positive-length geodesic in the class.

If K≤0, the universal cover is a complete Hadamard manifold. Each element
of its deck group Z³ has translation length attained, by the preceding
closed geodesic. Hence the action is proper and semisimple. The flat torus
theorem gives an invariant, totally geodesic isometric R³. Its hypotheses
require properness and semisimplicity, not cocompactness of the whole
four-manifold action.

At a point of this flat, take an orthonormal tangent basis e_1,e_2,e_3 and
unit normal n. All K(e_i,e_j)=0. Therefore

\[
 \sum_{i=1}^3\operatorname{Ric}(e_i,e_i)
       =\sum_{i=1}^3K(e_i,n)=\operatorname{Ric}(n,n).
\]

Writing Ric=−3g+E gives

\[
 6=\sum_{i=1}^3E(e_i,e_i)-E(n,n)\le4\epsilon,
\]

as claimed. The relevant primary statement is Bridson–Haefliger,
*Metric Spaces of Non-Positive Curvature*, II.7, Theorem 7.1.

**Sharpness as an infimum.** Fix any actual flat torus (T³,h_0) and c>0.
Put k²=3/2 and

\[
 a_0(t)=\operatorname{clip}(k\tanh(kt),-1,1).
\]

This function is odd, nondecreasing, Lipschitz with constant 3/2, and is
exactly ±1 outside a finite interval. Let φ_η be a nonnegative even smooth
mollifier supported on [−η,η], of integral one, and put

\[
 a_\eta=\phi_\eta*a_0,\quad
 F_\eta(t)=c\exp\!\left(\int_0^ta_\eta(s)\,ds\right),\quad
 g_\eta=dt^2+F_\eta(t)^2h_0.
 \tag{5.2}
\]

These are smooth complete metrics on the fixed R×T³ with two exactly
hyperbolic outward ends. The physical torus lattice and c remain fixed.
Let v(t)=φ_η*a_0²−a_η². Then 0≤v≤(9/4)η². Almost everywhere,

\[
 1\le a_0'+a_0^2\le\tfrac32,
 \qquad a_0'+3a_0^2\ge\tfrac32.
\]

Consequently,

\[
 \begin{aligned}
 1-\tfrac94\eta^2&\le a_\eta'+a_\eta^2\le\tfrac32,\\
 \tfrac32-\tfrac{27}4\eta^2
    &\le a_\eta'+3a_\eta^2\le\tfrac72.
 \end{aligned}
 \tag{5.3}
\]

The upper first inequality is Jensen's inequality; the upper second one
uses |a_η|≤1. Since a_η'≥0, all sectional curvatures of g_η are
nonpositive: K_rad=−(a_η'+a_η²) and K_tan=−a_η². Its Ricci eigenvalues are
−3(a_η'+a_η²) and −(a_η'+3a_η²), the latter with multiplicity three.
For sufficiently small η, (5.3) gives

\[
 \|g_\eta^{-1}(\operatorname{Ric}+3g_\eta)\|_\infty
       \le\tfrac32+\tfrac{27}4\eta^2.
 \tag{5.4}
\]

Together with the lower bound this proves sharpness of the infimum. It
does not assert attainment by an exact-end metric with defect exactly 3/2.

## 6. A forced Weyl peak and the remaining escape

For ε<3/2, Theorem 5.1 forces strictly positive sectional curvature at
some point of every connector. For ε<1 this has the quantitative consequence

\[
 \boxed{\qquad \sup|W|>\sqrt3(1-\epsilon).\qquad}
 \tag{6.1}
\]

Indeed, for a plane spanned by e_1,e_2,

\[
 K_{12}=-1+W_{1212}
       +\tfrac13(E_{11}+E_{22})-\tfrac16(E_{33}+E_{44}),
\]

and the last two terms are at most ε. The trace-free 3×3 matrices W± obey
|λ_max(W±)|≤sqrt(2/3)|W±|. A unit decomposable two-form has squared norm
1/2 in each chirality, so |W_{1212}|≤|W|/sqrt(3). A positive K_{12} gives
(6.1). No torus symmetry enters this argument either.

The exact balances constrain a putative ε_j→0 sequence as follows:

* a Weyl peak of order one is unavoidable;
* the two chiral Weyl energies are equal, exactly;
* their sum differs from total physical twist energy by at most
  (2ε_j+2ε_j²) times the physical volume of the active region;
* V_ren differs from minus one sixth of the twist energy by at most
  ε_j/3 times that same volume;
* the order-one twist peak and diverging weighted charge-transport cost of
  round 2 remain necessary, and every purely radial model is already
  excluded by round 4.

These statements still allow the order-one curvature and twist peaks to
occupy a collapsing physical volume. Neither (3.3) nor (6.1) supplies a
lower bound on the volume of their supports. The sharp NPC theorem proves
that merely non-radial negative sectional geometry cannot realize the
escape: a successful construction must develop positive sectional curvature
as well as nontrivial charge transport. It does not rule out that possibility.

Thus the new results are an exact full-class energy constraint and a sharp
full-class obstruction under K≤0. The general two-variable small-Ricci-gap
problem is not solved here. In particular, no inequality-compatible profile
has been represented as an actual solution of all blocks in (1.3).

## Sources and reproducibility

The elementary coefficient and extremal calculations are checked by
`round5_global_check.py`. The checker does not prove the flat torus theorem
or replace the geometric compactness argument above.

* M. T. Anderson, *L² curvature and volume renormalization of AHE metrics
  on 4-manifolds*, Mathematical Research Letters 8 (2001), 171–188,
  [primary article](https://archive.intlpress.com/site/pub/files/_fulltext/journals/mrl/2001/0008/0002/MRL-2001-0008-0002-a006.pdf).
  Used to verify characteristic-form normalization; the non-Einstein
  identity (3.1) is derived above rather than imported from an Einstein theorem.
* M. Bridson and A. Haefliger, *Metric Spaces of Non-Positive Curvature*,
  Chapter II.7, Theorem 7.1,
  [primary book text](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bridsonhaefligerx.pdf).
  The action need not be cocompact: properness and semisimplicity suffice.
