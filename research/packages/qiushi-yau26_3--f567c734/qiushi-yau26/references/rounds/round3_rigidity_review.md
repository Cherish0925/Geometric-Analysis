# Independent review of the intrinsic monopole calibration gap

19 September 2026. Reviewed `round3_rigidity.md` in full against the
round-two spinor identities and the live manuscript's rescaled-monopole,
Chern--Weil, and blow-up budget derivations. This review found no gap in
the stated intrinsic theorem. The conclusion concerns the actual monopole
class hypotheses, not arbitrary approximately Einstein metrics.

## 1. The bundle Hessian estimate

The norm interpolation follows directly by integration by parts:

\[
 \|\nabla u\|_4^2\le(2+\sqrt n)\|u\|_\infty\|\nabla^2u\|_2.
\]

It is valid for complex sections after taking real Hermitian pairings.
There is no Sobolev or injectivity input. Converting both sides to
volume-normalized norms multiplies both by `V^{-1/2}`. Thus no hidden
volume factor appears, including when volumes tend to zero or infinity.

For the Hessian identity, the exact antisymmetric relation
`H_ij-H_ji=F_ij u` first gives

\[
 \int|H|^2-\sum_{ij}\int\langle H_{ij},H_{ji}\rangle
        =\frac12\sum_{ij}\int|F_{ij}u|^2.
\]

Integration by parts on the crossed term then produces the rough
Laplacian, a Ricci contraction, and the displayed bundle curvature term.
The covector slot of `nabla u` contributes only Ricci after contraction;
the section slot contributes the bundle curvature. This verifies equation
(3), including why neither a full Riemann bound nor `nabla F` is needed.
The factor `17` in (2) is consistent with the ordered component norm:
the curvature-gradient term is at most `4 K ||F||_2 ||H||_2`; absorbing
half the Hessian energy leaves `16 K^2||F||_2^2`, and the antisymmetric
term contributes the remaining `K^2||F||_2^2` after multiplication by two.

## 2. Spinor curvature and smooth-weight quantifiers

The positive-spinor curvature projection removes the W-minus block of
the Riemann curvature operator. It retains W-plus, scalar curvature,
trace-free Ricci, and determinant curvature. Equation (8) is therefore
the appropriate bound. It is not a bound for the full tensor connection
on arbitrary curvature tensors.

The determinant identity

\[
 \int|F_A|^2=2\int|F_A^+|^2-4\pi^2a^2
\]

justifies precisely the factor involving `(-a^2)_+/V` in the theorem.
The self-dual projection `(a^+)^2` must not replace `a^2` here; the note
does not make that substitution.

The optimal weight need not have a uniform pointwise upper bound across
the sequence. None is used: the maximum principle needs only the uniform
lower bound for `f`, while the spinor rough Laplacian and determinant
curvature estimates need `f` in normalized L2. The calibration bound
controls `q` in normalized L2 and hence controls `f^2` in normalized L1.
This closes that possible source of a hidden curvature assumption.

For each fixed smooth metric on a compact manifold, `q` is continuous and
bounded; a smooth positive approximation to `sqrt(q)` can be uniformly
accurate enough to make all the scalar coefficient and integrated defect
errors smaller than any prescribed `eta`. The monopole solutions may
change with the approximation. The uniform maximum bound ensures the
error estimates hold for those solutions. No convergence of the spinors,
no uniform approximation derivative bounds, and no common choice of
approximation index across metrics is required. Sending the errors to
zero separately on each metric makes the universal theorem legitimate.

## 3. Strong divergence closure

The map from the spinor to `A_psi` is a parallel polynomial of degree four.
Its second derivative has only the two types
`Phi^3 nabla_A^2 Phi` and `Phi^2 (nabla_A Phi)^2`. Lemma 1 and the bounded
spinor therefore prove (14). The phase of the determinant line cancels.

The operator-to-four-index-Weyl identification is parallel, so
`||nabla J_psi||_2 <= C ||nabla^2 A_psi||_2`. Contracted Bianchi writes the
actual Weyl divergence as a fixed parallel contraction of `nabla E` and
`nabla tr E`; one integration by parts verifies (16). Testing it against
the smooth tensor `J_psi` is justified by (14). This is the extra regularity
absent from the prior functional endpoint counterexample.

I independently eliminated the weighted-Hodge terms from the round-two
identities. The resulting coefficients are exactly those in (19):
`-1/64` on `rho^2 B_psi`, `1/16` on `rho^2|dpsi|^2`, `-5/96` on
`rho^2|drho|^2`, and `1/8` on the mixed term. At `s=-4,rho=sqrt(2),R=0`,
the zeroth-order term is `1/16`. The amplitude and derivative deficits
control every remaining term with universal constants. Hence (20) and
the product gap (21) follow. The theorem's constant is existential;
this review does not supply a numerical value.

## 4. The blow-up specialization and its constants

Let `X` be a minimal complex surface of general type with `b_+(X)>1`,
`A=c_1^2(X)>0`, and `M=X#k CPbar^2`. Use the actual monopole classes from
the standard blow-up input. Sign averaging their self-dual projections
selects one with `p=(a^+)^2>=A`, while every such sign choice has the same
topological square

\[
 a^2=A-k=T(M).
\]

The distinction between these two squares is preserved. Moreover any
candidate with `delta<=1/64` automatically has `A-k>0`: Chern--Weil gives

\[
 4\pi^2(A-k)=\int\left(s^2/24+2|W^+|^2
                                  -|\operatorname{Ric}^{\circ}|^2/2\right),
\]

and its integrand is at least
`(2/3)(1-delta)^2-2delta^2>0` after discarding Weyl. Thus the factor
`1+(-a^2)_+/V` in (21) equals one in this application, even if `k<A`
was not initially imposed.

Put `d=(1/3-k/A)_+`, and use the manuscript's quantities

\[
 I=(4\pi^2)^{-1}\int(s^2/24+2|W^+|^2),\quad
 J=(8\pi^2)^{-1}\int|\operatorname{Ric}^{\circ}|^2,\quad
 D_a=I-2p/3\le J+Ad.
\]

The exact completed square gives

\[
 \Delta\le108\pi^2D_a
       \le\frac{27}{2}\int|\operatorname{Ric}^{\circ}|^2
                                      +108\pi^2Ad.
\]

Using `V>=2pi^2 A/(1+delta)^2` and `delta<=1/4` yields

\[
 \frac\Delta V\le54\delta^2+\frac{675}{8}d.
\]

Combining this independently derived estimate with the retained joint
calibration budget gives

\[
 \frac{d_{\rm cal}}V\le436\delta^2+675d,
\qquad
 \varepsilon\le491\delta^2+\frac{6075}{8}d
                      \le760(\delta^2+d).
\]

Therefore Theorem 2 proves a universal positive lower bound for
`delta^2+(1/3-k/A)_+` in this family, with no full-curvature assumption.
To state it for all smooth metrics, the range `delta>1/64` is automatic
after reducing the final constant to at most `1/4096`. No relative Euler
bound or lower covolume has entered this proof.

The critical connected-sum application likewise has positive actual
class square `2A/3+4m-4+4b_1(N)`. Its monopole sign-cube existence remains
an explicit family hypothesis; topological numbers by themselves do not
provide it.

## Review conclusion

The prior curvature-bound hypothesis can be removed for the stated
monopole applications by this intrinsic estimate. This does not remove
the monopole hypothesis, prove an arbitrary-metric calibration gap, or
settle either unrestricted Yau26 branch. All review work stayed in the
isolated local workspace.

## Follow-up: the complete all-metrics blow-up theorem

I subsequently read `round3_joint_gap.md` in full, with special attention
to its independently supplied lowest-eigenvalue inequality (4). That
derivation is valid for the same selected actual monopole class; it does
not introduce an extra spectral or scalar-curvature hypothesis.

Here is the complete Holder step behind its concise argument. Replace
the Weyl-norm eigendefect in the spinor proof by

\[
 2\int\bigl(\langle W^+\psi,\psi\rangle-w\rho^2\bigr)\ge0,
 \qquad q_w=-s-3w>0.
\]

The two Weitzenbock formulas and the quadratic-map differential inequality
then give, for `v=|varphi|` and the optimal weight `f=sqrt(q_w)`,

\[
 Z:=\int fv^3\le\int q_wv^2.
\]

Put `Q=integral f^4=integral q_w^2`. Holder gives

\[
 Z\le\int f^2v^2\le Q^{1/3}Z^{2/3},
\]

so `Z<=Q` and `integral f^2v^2<=Q`. Meanwhile the curvature equation
and harmonic projection give

\[
 \int f^2v^2=18\int|F_A^+|^2\ge72\pi^2p.
\]

The selected `p>=A>0` excludes the zero denominator case in the division
by `Z^{2/3}`. Smooth approximation of `sqrt(q_w)` is valid on each compact
metric for the same reason as in the main proof. Finally
`(2s/3+2w)^2=(4/9)q_w^2` proves the coefficient `32pi^2` in equation (4).

An additional exact symbolic check verified both pointwise identities in
equation (5), this `4/9` conversion, and the final coefficient additions.
The density estimate uses `G>=0` and
`Q_E+Z_s+108P=5Q_E+104P<=109Q_E`, where
`Q_E=integral |Ric+g|^2=P+Z_s/4`. Thus its factor `436` and the volume
conversion factors `675` and `675/8` are consistent. The coarse volume
bound `V>=32pi^2 A/25` is valid throughout the smaller range
`delta<=1/64` actually used.

The last proof step has the correct quantifiers. Small-delta candidates
automatically have `a^2=A-k>0`, as verified above, so the intrinsic
constant is universal. The complementary range `delta>1/64` is covered
by `delta^2>1/4096`. Therefore

\[
 c_* = \min\{c/760,1/4096\}>0
\]

works simultaneously for every allowed `X`, every nonnegative integer
`k`, and every smooth metric `g`. Only `T=2chi+3tau=A-k`, the actual
monopole classes, and the scalar volume lower bound are used. No
`chi/A`, full-energy, full-curvature, diameter, or noncollapse bound has
been smuggled into the specialization. The stated Einstein forbidden-band
consequence follows by rescaling any hypothetical negative Einstein
metric and using monopoles to exclude the other signs.
