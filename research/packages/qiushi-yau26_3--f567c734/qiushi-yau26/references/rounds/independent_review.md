# Independent review: Ricci-box optimization and the base-TT correction lemma

Date: 2026-09-19. Reviewer: independent global-analysis subagent.

Reviewed `curvature_box.md`, `curvature_box.py`, `construction.md`, and `construction_checks.py`, and compared the construction's input estimates with `20260916_construction.tex:815–943` and `20260912.tex:3666–3759` in the live read-only Skill. Both scripts were executed successfully with local Python. This review checks mathematical implications as well as script output; the scripts do not certify a global metric or a nonlinear inverse.

## Findings

No fatal error was found in the exact Ricci-box bound or in the stated conditional base-TT proposition. Two presentational qualifications should be retained:

1. The Ricci-box *value* is correct on the entire stated interval, but the sentence classifying minimizers omits endpoint ties. At `d=0` all sixteen vertex labels coincide at the same point. At `d=1`, both `m=2` and `m=3` minimize. For `0<d<1/3` the minimizing count is `m=4`; at `d=1/3`, it is `m=3,4`; for `1/3<d<1`, it is `m=3`. This does not change any inequality or consequence.
2. The explicit coefficient `1/[16 pi^4(p-1)]` follows from the stated projection and test-mass asymptotics. Neither the new note nor these checks prove that this is the optimal *attainable* leading coefficient among all allowed perturbations. Call it an explicit leading-coefficient lower bound, or specify this limited meaning of “sharp.” The order `epsilon^3` is matched by the known upper construction; equality in its numerical constant is not established.

## 1. Ricci-box calculation and its implications

Independently start with eigenvalues `lambda_i=-1+a_i`. Then

\[
 F=\frac{(\sum\lambda_i)^2}{6}-\frac12\sum\lambda_i^2
   =\frac23-\frac t3+\frac{t^2}{6}-\frac12\sum a_i^2.
\]

The second derivative in any single `a_i` is `-2/3`. Separate concavity therefore reduces the minimum on the full box to vertices, not merely to a sampled subset. The minimizing counts and formulas in the note agree with direct evaluation of all five count-polynomials. In particular, comparison of the two competing branches gives

\[
 F_4-F_3=\frac23d(3d-1).
\]

The sign change occurs at `d=1/3`, as stated. The second branch vanishes precisely at `d=1/2` in the relevant interval. Hence Chern--Weil gives `2chi>3|tau|` for `d<1/2`. Applying the same inequality with each orientation is legitimate; it does not require both Weyl halves to minimize at the same algebraic tensor. Simultaneous minimization is unnecessary for the lower bounds.

The negative normalization change is correct: for `Ric≈-3g`, write `epsilon=3d`; the Ricci CGB density is multiplied by nine. Integrating the first branch gives

\[
 \operatorname{Vol}\le\frac{12\pi^2\chi}{(3-\epsilon)^2}
 \quad(0\le\epsilon\le1).
\]

Combining this with the retained AH segment volume produces exactly the exponential Euler-characteristic cost in `curvature_box.md`. It is a necessary condition with physical covolume and Ricci normalization fixed. It neither forbids all varying-cover constructions nor legitimizes matching by a coordinate shift.

The claim of algebraic sharpness is appropriate: prescribed Ricci eigenvalues can occur in algebraic curvature tensors, whereas a closed metric attaining this pattern everywhere is not asserted.

## 2. The sheared background does not leave a linear pure-base-TT term

This was the principal potential failure tested. In local product coordinates the original metric is block diagonal,

\[
 G=b_{ij}(x)dx^idx^j+h_{ab}(x,y)dy^ady^b,
\]

and the common pointwise fibre area gives

\[
 S_i=\tfrac12h^{-1}\partial_i h,\qquad\operatorname{tr}S_i=0.
\]

For every perturbed base metric `b'`, leaving `h` fixed, direct block-Christoffel contraction yields

\[
 \operatorname{Ric}(b'+h)_{ij}
 =\operatorname{Ric}(b')_{ij}
  -\nabla^{b'}_j\operatorname{tr}S_i
  -\operatorname{tr}(S_iS_j)
 =\operatorname{Ric}(b')_{ij}-\operatorname{tr}(S_iS_j).
\]

The trace term vanishes identically before differentiation, so it cannot reappear when the base connection changes. The last tensor is independent of `b'`. Thus

\[
 \Phi(b'+h)_{HH}=(K(b')+1)b'-T.
\tag{R1}
\]

For a TT tensor `k` on the hyperbolic surface,

\[
 DK_b(k)=\tfrac12\bigl(\operatorname{div}\operatorname{div}k
 -\Delta\operatorname{tr}k-\langle\operatorname{Ric}_b,k\rangle\bigr)=0.
\]

Since `K(b)+1=0`, the first derivative of (R1) is zero as a horizontal tensor, not merely after integration. The polarized second derivative is `D²K_b(k1,k2)b`, whose pairing with the fixed trace-free `q_beta` vanishes pointwise. Vertical and mixed blocks cannot pair with the horizontal test tensor because the *fixed* `G` has no horizontal-vertical inverse components.

Therefore arbitrary global base-TT directions really do have zero first and second fixed-test projection. No assertion that `J_G Q=0` is needed or valid. Moving the contraction metric or measure to `G+sB` would change the argument, but `construction.md` explicitly keeps both fixed. This distinction is essential and correctly observed.

The global perturbation `B=pi^*k` is legitimate because it changes the base metric while preserving the original bundle splitting and fibre path. The argument would not cover an arbitrary horizontal tensor depending on fibre position, a base tensor that is only approximately TT, or a changed horizontal distribution.

## 3. Uniform nonlinear remainders despite degenerating injectivity radius

The proposed use of uniform Taylor bounds is valid in the stated *geometric* `C²(G)` norm, and can be justified more directly than through coordinate charts. Let `g=G+h`, with `|h|_G<1/2`. Relative to the fixed connection `nabla=nabla^G`, the exact connection difference is

\[
 C^k{}_{ij}=\tfrac12(G+h)^{k\ell}
 (\nabla_i h_{j\ell}+\nabla_j h_{i\ell}-\nabla_\ell h_{ij}).
\]

The Ricci difference is a sum of `nabla C` terms and quadratic `C*C` terms. The inverse metric is uniformly bounded and analytic in `h` on this neighbourhood. Consequently the Ricci map has uniform multilinear bounds, including its third derivative with respect to the *metric variable*, as a map from `C²(G)` to `C⁰(G)`. These pointwise tensor estimates depend on dimension and the positivity radius; they introduce no inverse injectivity-radius factor. Spatial `C³` bounds on the perturbation are not required.

For the pure base perturbation one can avoid a third-order expansion altogether. TT gives `K(b+k)+1=O(a²)`, while fixed trace-freeness gives `<b+k,q>_b=<k,q>_b`. Equation (R1) therefore implies

\[
 |\langle\Phi(G+B)-\Phi(G),Q\rangle_G|
 \le Ca^3|Q|_*.
\]

The horizontal covariant derivatives of the horizontal-horizontal components of `B` agree with base covariant derivatives because the original horizontal leaves are totally geodesic. Thus the assumed `C²(G)` bound controls the base norm used here uniformly.

Finally,

\[
 \Phi(G+B+r)-\Phi(G+B)-D\Phi_G(r)
 =O_{C^0}(az+z^2)
\]

by the uniform derivative estimate above. Closed-manifold integration against the globally TT `Q` moves the remaining linear `r` term to `J_GQ`. Hence the exact-cancellation argument and the assumed adjoint estimate give precisely

\[
 |\langle\Phi(G+B+r),Q\rangle_{L^2(G)}-I_\epsilon|
 \le C\beta(\epsilon^2z+a^3+az+z^2).
\tag{R2}
\]

This also identifies the proof's nonnegotiable assumptions: the norm is the original geometric `C²(G)`, positivity is uniform relative to `G`, the test tensor is genuinely global TT, and the stated `L¹` adjoint estimate holds. A coordinate `C²` bound in the shrinking angular coordinates would not be a substitute.

## 4. Independent normalization and leading coefficient

The nuclear norm of the leading base tensor is `2f`, with `f=sech²t`. The base volume weight is `beta cosh(t)dt dtheta`, with unit normalized angular period, and the fibre area is `4pi(p-1)`. Thus

\[
 \int|Q|_* =4\pi(p-1)\,2\beta\int\operatorname{sech}t\,dt
 =8\pi^2(p-1)\beta
\]

to leading order. For the balanced collar `v=c0 epsilon sech(t)sech²(u)`, `c0=2/pi²`, the horizontal source paired with `q0` is `-v²f/2`. Including both short angular factors, the leading source integral is

\[
 -\frac12c_0^2\epsilon^3\beta
 \left(\int\operatorname{sech}^3t\,dt\right)
 \left(\int\operatorname{sech}^3u\,du\right)
 =-\frac{\epsilon^3\beta}{2\pi^2}.
\]

The manuscript's global quadratic differential and cutoff estimates supply the stated lower-order terms. With `beta=epsilon²`, the global `O(beta²)` normalization errors are consistent with these leading scales.

For `a=O(epsilon^(3/2)), z=o(epsilon^(3/2))`, every term in (R2) is `o(epsilon³ beta)`. The same holds for `a=o(epsilon), z=O(epsilon²)`. Pointwise operator/nuclear-norm duality and `G+h=(1+o(1))G` yield

\[
 |\langle\Phi(G+h),Q\rangle_{L^2(G)}|
 \le(1+o(1))\delta_-(G+h)\int|Q|_*dV_G.
\]

Dividing the preceding leading source coefficient by the nuclear-mass coefficient gives exactly

\[
 \liminf\frac{\delta_-(G+B+r)}{\epsilon^3}
 \ge\frac1{16\pi^4(p-1)}.
\]

No missing `sqrt(2)`, extra angular period, or lost `beta` factor was found. Again, this proves the lower bound, not optimal attainability of its constant.

## 5. Counterexample attempts and remaining scope

An exact hyperbolic base path cannot refute the projection lemma: (R1) keeps its whole fixed-test projection equal to `I_epsilon`. Its nonlinear acceleration precisely explains why the straight-path cubic sign is not an integrability obstruction. A conformal perturbation of order `epsilon^(3/2)` can cancel this single projection, but it has a remainder of that same order and lies outside `z=o(epsilon^(3/2))`; the note records this existing counterexample correctly.

The cylinder checks verify one concrete model and the restricted vertical response. They do not independently verify the global holomorphic-quadratic-differential theorem or the complete adjoint defect estimate; these remain explicit manuscript inputs. The general base-TT cancellation, however, follows from the dimension-two identity (R1), and does not depend on extrapolating the cylinder computation.

The final Schur-complement formula retains the complement's effect on the projected nonlinear term and is algebraically correct conditional on the declared inverse and bounded projections. It supplies no evidence that all leading corrections lie in base-TT directions. The strongest supported conclusion is exactly the restricted necessary estimate (R2) and its two asymptotic corollaries. There is no all-metric Einstein obstruction or complete small-spectrum theorem here.
