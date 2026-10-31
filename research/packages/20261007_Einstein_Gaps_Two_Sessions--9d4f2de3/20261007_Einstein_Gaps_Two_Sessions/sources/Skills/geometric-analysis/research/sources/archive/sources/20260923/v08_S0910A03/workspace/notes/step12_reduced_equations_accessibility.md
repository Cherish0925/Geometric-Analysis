# Step 12: full rank-one reduction and the fixed-scale accessibility problem

## 1. Repairs to the Step 11 picture

The negative-branch collapse problem should **not** be divided into an established fiber-survival case and an established high-twist fiber-death case. Three implications used for that division are unavailable.

1. Orthogonal transitivity of a full `T^2` action does not make either chosen circle action hypersurface-orthogonal. Taub–NUT–AdS is already a counterexample in the exact Einstein setting: its `(psi,phi)` torus is polar over `(r,theta)`, while the Hopf circle has connection `A=cos(theta)dphi` and nonzero curvature. The rank-two twist quantities are scalars on a two-dimensional quotient; a rank-one twist is a closed one-form on a three-dimensional quotient. The degeneration-edge argument for the former does not annihilate the latter.
2. Small `ell^2|F|^2` does not imply a static limit. The four-dimensional curvature contains `ell nabla F` and `(nabla ell)F`, equivalently first derivatives of the scaled field `Z=ell F`; these terms can remain order one when `Z` is small. A Harnack argument for `ell` also presupposes controlled quotient geometry, which the good-point assumptions do not give.
3. The static calculation in Step 11 proves only a spherical cohomogeneity-one exclusion. It does not classify static Einstein circle metrics. The exact product `H^2 x H^2`, with the circle written in polar coordinates on the first factor,
   
   `g = dr^2+sinh^2(r)dpsi^2+g_H2`,
   
   is static with `Ric=-g`, `Spec(Hess ell/ell)=(1,0,0)`, and constant `Spec(W+) = (-2/3,1/3,1/3)` up to orientation. Thus “constant static spectrum implies W+=0” is false outside the special ansatz. The general calibrated constant-spectrum exclusion remains the projector/Derdzinski Einstein-germ result of Step 6.

Accordingly, the governing question remains:

> Does a positive-volume set with bounded centered four-dimensional curvature means and vanishing calibrated deficit necessarily contain a fixed-scale buffered covering chart, or can quotient degeneration and derivative twisting destroy every such chart?

## 2. Exact rank-one variables

On a regular invariant region write

`g = q + ell^2 theta^2`,  `theta=dpsi+A`,  `F=dA`,

and use a `q`-orthonormal horizontal frame and the unit vertical vector `V`. Define

`u=d log ell`,  `Z=ell F`,  `z=*q Z`,  `H=Hess_q(ell)/ell=nabla u+u tensor u`.

For an exact Einstein metric `Ric_g=-kappa g`, `kappa>0`, standard Kaluza–Klein curvature formulas give

`R_{aVbV} = -H_ab + (1/4) Z_ac Z_b^c`,

`R_{abcV} = -(1/2)[(nabla_a Z)_bc + 2u_a Z_bc-u_b Z_ac+u_c Z_ab]`

up to the simultaneous sign induced by the choice of `V` or `A`. In three dimensions this yields the electric and magnetic Weyl matrices

`E_ab := W_{aVbV} = (kappa/3)q_ab-H_ab+(1/4)(|z|^2 q_ab-z_a z_b)`,

`B_ab := (1/2)[(nabla_a z)_b+u_a z_b+u_b z_a-<u,z>q_ab]`.

The reduced vertical and mixed Einstein equations are

`tr H = kappa+|z|^2/2`,

`d z = -2u wedge z`,  `div z = <u,z>`.

The first identity makes `E` trace-free; the latter two make `B` symmetric and trace-free. Up to orientation and the sign convention for `B`,

`W+ = E+B`,  `W- = E-B`.

These formulas have two decisive consequences.

* The scaled twist amplitude `|Z|=|z|` controls only the algebraic quadratic term in `E`.
* The derivative term `nabla z` lies in `B` and hence directly in a chiral Weyl block. It is not lower order as `ell -> 0`.

The exact source formulation uses the Killing norm and twist potential. If `xi` is the circle Killing field, `lambda=|xi|^2=ell^2` and the twist one-form is locally `d omega`. The Geroch quotient equations express `Ric_q`, `Delta lambda`, and `Delta omega` through `lambda,omega` and their first/second derivatives (with signature-dependent signs). They confirm structurally that the complete system is elliptic on every regular set where `lambda>0`, but becomes singular as `lambda->0`; cosmological constant does not remove the derivative twist field. See `Knowledge/objects/papers/Geroch-group-for-Einstein-spaces-and-holographic-integrability--97a50a94c55d--463361159051/object.md`, lines 98–156, with care because its displayed conventions begin in Lorentzian signature.

## 3. A chiral Riccati factorization

Define the two one-forms

`a_+ = u-z/2`,  `a_- = u+z/2`.

A direct tensor calculation using the scalar reduced equations gives

`W+ = -[sym nabla a_+ + a_+ tensor a_+]_0`,

`W- = -[sym nabla a_- + a_- tensor a_-]_0`

up to exchanging `+` and `-` with orientation. Here the subscript `0` denotes the trace-free part. The antisymmetric reduced equation becomes

`d a_+ = a_+ wedge a_-`,  `d a_- = -a_+ wedge a_-`.

The trace modes are

`tr(sym nabla a_+ + a_+ tensor a_+) = kappa + 3|z|^2/4 - 3<u,z>/2`,

`tr(sym nabla a_- + a_- tensor a_-)= kappa + 3|z|^2/4 + 3<u,z>/2`.

These identities are checked exactly by `workspace/scripts/verify_chiral_reduction_identity.py`.

This factorization is more discriminating than the proposed “high scaled twist” division. The calibrated condition constrains a nonlinear first-order Riccati tensor for one chiral combination `a_+`; bounded full-curvature means constrain the corresponding tensor for both `a_+` and `a_-`. But neither controls `u` and `z` separately unless one also controls a trace mode, a gauge, or quotient geometry. In particular, large `u` and `z` can nearly cancel in `a_+` while surviving in `a_-`, and conformal/quotient degeneration can hide the coefficient geometry in which these equations are elliptic.

## 4. Exact checks

`workspace/scripts/verify_rank1_reduction.py` performs two independent tests.

### Static product

For `H^2 x H^2`, `z=0` and `Spec(H)=(1,0,0)`, so the formula gives

`Spec(W+) = (-2/3,1/3,1/3)`.

This exactly supplies the counterexample to the Step 11 general static-rigidity wording.

### Taub–NUT–AdS

For

`V=(r-nu)/(r+nu) [1+(r-nu)(r+3nu)/3]`,

`q=dr^2/V+(r^2-nu^2)g_S2`,  `ell=2nu sqrt(V)`,  `F=-sin(theta)dtheta wedge dphi`,

the script obtains

`tr H-1-|z|^2/2=0`,  `tr B=0`,

and

`E = diag(-2c,c,c)`,  `B=diag(2c,-c,-c)`,

where `c=nu(4nu^2-3)/(3(r+nu)^3)`. Therefore `E+B=0`, while

`Spec(E-B)=(-4c,2c,2c)`,

which exactly matches the nonzero chiral spectrum from the independent coordinate-curvature script. This check simultaneously confirms that derivative twisting cancels an order-one electric anisotropy even though a toric action is polar.

## 5. What the quotient curvature bound actually gives

A separate robust structure comes from quotient metric-measure geometry. If a genuine compact circle acts isometrically on a four-manifold with `Ric >= K g`, the quotient with the pushforward volume measure is `RCD*(K,4)`. On a smooth regular quotient the measure is proportional to `ell dvol_q`, and the finite-dimensional weighted tensor is

`Ric^4_{q,ell} = Ric_q-Hess_q(ell)/ell >= K q`.

This is exactly the weighted combination naturally inherited from the four-dimensional horizontal Ricci equation. It explains why ordinary `Ric_q`, base harmonic radius, and ordinary Harnack estimates were not available: they can degenerate while the weighted four-dimensional structure remains controlled. The source is Galaz-Garcia–Kell–Mondino–Sosa, `On quotients of spaces with Ricci curvature bounded below`, Corollary 1.2 and the smooth formula near lines 70–80, citation key `galazgarca2018quotients`.

The weighted `RCD(-,4)` structure supplies doubling, Poincare inequalities, heat-flow regularity, and measured compactness on the quotient. It does **not** by itself lift a three-dimensional regular quotient point to a four-dimensional noncollapsed covering chart, nor does it keep `ell` away from zero. Indeed a collapsed hyperbolic cusp has excellent weighted quotient geometry and arbitrarily short but surviving fibers. The missing datum is topological survival of the fiber in a buffered domain together with quantitative reconstruction from the weighted quotient.

## 6. Refined obstruction architecture

The available reasoning now separates three genuinely different failures instead of calling all of them high twist.

1. **Buffered fiber survival.** If a fixed-scale buffered normal cover unwraps a rank-one fiber and has a controlled harmonic chart, the mean-transport lemma carries the calibrated deficit and the Step 6 forbidden Einstein germ gives a contradiction. This conditional implication remains valid.
2. **Derivative twisting.** Even when `|Z|` is small, `nabla Z+u tensor Z` can be order one. In chiral variables this is the freedom to keep the Riccati tensor of `a_+` calibrated while `u,z` or `a_-` oscillate/degenerate. A useful estimate must control a derivative quantity such as `nabla z` or the full `W-` mean, not merely `|Z|^2`.
3. **Quotient degeneration / rank loss.** The smooth quotient equations become singular at `ell=0`, and weighted `RCD(-,4)` regularity does not imply ordinary three-dimensional harmonic radius. Fiber death inside every buffer can occur through a singular set whose effect is encoded in the metric-measure quotient rather than a pointwise lower bound for `|Z|`.

The curvature maximal function from Step 9 does bound the mean of **both** chiral Weyl blocks on selected points, since it bounds `|Rm|^2`. Thus the sharper analytic target is not a pointwise curvature estimate. It is a compactness/reconstruction statement for solutions of the coupled chiral Riccati–Maurer–Cartan system on an `RCD(-,4)` quotient:

> bounded local means of both `|W+|^2` and `|W-|^2`, vanishing calibrated defect for `W+`, and the exact/approximate reduced equations should either yield a fixed-scale regular weighted quotient region whose buffered cover reconstructs noncollapsed four-dimensional geometry, or force concentration of the trace/gauge modes (`|u|`, `|z|`, or quotient singularity density) visible in a scale-invariant energy.

At present no source found supplies this theorem. The literature search found the exact Geroch equations and quotient `RCD` inheritance, but not the needed coercive Bochner identity or reconstruction theorem. This is a precise new mathematical interface rather than an established result.

## 7. Model-level coercive possibilities

Three calculations now look worthwhile.

* Derive a weighted Bochner identity for `a_+` and `a_-` using the `ell dvol_q` Laplacian. The trace-free Riccati tensors are the chiral Weyl blocks, while `d a_±` is algebraically `a_+ wedge a_-`. A successful identity would bound `|nabla a_±|^2+|a_+ wedge a_-|^2` by the two Weyl energies plus boundary terms. The obstruction is the trace mode, which contains `|z|^2` and `<u,z>` and may require a normalization or a weighted divergence identity.
* Work at the synthetic quotient level: quantify whether a positive-measure set of 3-regular points in an `RCD(-,4)` quotient has a definite reconstruction radius when both chiral curvature means are controlled. This must retain fiber homotopy information; quotient regularity alone is insufficient.
* Search for an exact or approximate rank-one countermodel in which `W+` stays calibrated, both Weyl means remain bounded, but the quotient reconstruction radius tends to zero through derivative twisting. Such a model would decisively redirect the negative branch. Taub–NUT–AdS does not qualify because core-reaching means diverge and accessible annuli are uncalibrated.

## 8. Scope relative to Yau 26

All of the reduction above assumes a genuine local circle action. A Ricci-pinched collapsed sequence does not automatically carry such an exact action. Passing from bounded-Ricci collapse to invariant reduced variables requires smoothing, local covers, nilpotent structures, or a limit-groupoid construction; the Calderon–Zygmund spike blocks naive pointwise curvature recovery. Thus the full bridge has two layers:

1. obtain a sufficiently exact rank-one reduced structure on a positive-volume good set;
2. establish coercive weighted compactness/reconstruction for the complete `u,z` system.

Neither layer is proved. The fixed critical Ishida–LeBrun negative branch remains a valuable test problem, but the positive branch, dimensions at least five, and Lean formalization remain open. The present advance is the identification and exact verification of the complete derivative-sensitive reduced structure, together with removal of two false simplifications that would have sent subsequent work toward the wrong theorem.

## 9. A stronger alternate interface: normalized energy concentration

Reading Ye Li's four-dimensional smoothing theorem reveals a more concrete route that should be compared with the rank-one reconstruction program. Theorem 3.6 in `Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md` assumes

`r^4/Vol(B_r(x)) * integral_{B_r(x)} |Rm|^2 <= epsilon`

and bounded Ricci, and then produces a Ricci flow for time comparable to `r^2` with `|Rm(t)| <= C/t`, without a noncollapse hypothesis. The same source explains that Cheeger–Tian/Li good chopping can shrink an absolute-small-energy ball by a comparable factor to obtain this volume-normalized smallness.

**Step 13 correction.** The claim that Li smoothing is inapplicable because the calibrated bulk has nonzero background curvature is **wrong**. The dimensionless energy `eps_r = r^4 fint|Rm|^2 <= K_0 r^4` becomes arbitrarily small by reducing the fixed radius `r_0`, while the Einstein scale remains nonzero. Furthermore, the pointwise `C/t` stability gap for the Einstein defect is circumvented by an `L^2` Sobolev absorption mechanism: in 4D, Hölder + relative Sobolev gives `int|Rm||E|^2 <= C_S eps_r^{1/2} (||nabla E||_2^2 + r^{-2}||E||_2^2)` where volumes cancel, and for `eps_r` small the gradient term is absorbed by `-2int|nabla E|^2`. This gives bounded `L^2` growth, then parabolic MVI at bounded-curvature time gives pointwise `|E(t_0)| = O(delta)`. See `step13_smoothing_bridge_and_L2_propagation.md`.
