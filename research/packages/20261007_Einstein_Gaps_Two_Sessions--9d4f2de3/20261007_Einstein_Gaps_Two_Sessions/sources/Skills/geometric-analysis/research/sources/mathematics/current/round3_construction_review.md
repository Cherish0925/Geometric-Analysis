# Independent review of the complete double-cylinder Einstein family

19 September 2026. Reviewed `round3_construction.md`, concentrating on the
nonlinear source, weighted inverse, moving gauge, parameter space and
boundary terms. This is a mathematical review of the stated invariant
complete model, not of a closed-manifold gluing theorem.

**Finding.** The proof supports the stated small real-analytic family of
complete Einstein metrics. I found no missing analytic hypothesis in the
passage from the approximate eight-parameter family to the exact family.
The source's qualifications about gauge uniqueness, marked parameters,
nonlinear charges, and closed gluing are necessary and correctly retained.

## 1. The nonlinear residual is in the inverse's target space

The compactified frame is appropriate: radial differentiation is
\(p\partial_\xi\) or \(q\partial_\eta\), and all frame brackets extend
smoothly to the closed square. The inverse metric is uniformly regular
there for small parameters. Thus the exact curvature residual, not only
its Taylor polynomial, has smooth compactified components.

At a q-face all u-derivatives of the parameter functions a,b vanish, and
the second metric block becomes the identity with vanishing derivatives.
The bracket coefficient \(\sin\eta=\pm1\) supplies the usual limiting
hyperbolic radial geometry. Consequently the remaining first block is the
exact curvature-minus-one cylinder with constant parameters. The face
Ricci residual is zero, including mixed components. The same reasoning
holds at each p-face.

Division by p is valid because its zeros at the two endpoints are simple.
After that division the quotient still vanishes on each q-face: this is
first true for interior xi and then at the corners by continuity. A second
Hadamard division gives \(E=pqR\), with a smooth quotient. The division
commutes with differentiation in the finite-dimensional parameters.
Hence the verified Jacobi property of the first variations implies
\(R=O(|z|^2)\) with each fixed number of derivatives.

For the proposed norm the resulting integrand is
\(O(|z|^4)W^{-1+2\delta}\). Its integral is finite for
\(\delta<1/2\). This also holds for parameter derivatives. The rational
metric formulas have uniformly nonvanishing denominators in a common
small complex parameter neighborhood, so their analytic dependence is
compatible with the weighted Banach target. The fact that the parameter
deformation itself is not L2 causes no problem here.

## 2. The weighted inverse is established, rather than assumed

The displayed conjugation formula is consistent with the sign of
\(L=\frac12(-P_t-P_u+V)\). Relative to the measure W, the first-order
term and its linear zeroth-order correction are skew-adjoint together.
At \(\delta=1/4\),

\[
 \operatorname{Re}\langle L_\delta v,v\rangle
 \ge\langle Lv,v\rangle-\frac1{16}\|v\|_2^2
 \ge\frac12\langle Lv,v\rangle.
\]

Combining the given gap \(L\ge1/8\) with
\(\langle Lv,v\rangle\ge\frac12\|\partial v\|_2^2-\|v\|_2^2\)
does give coercivity of the full radial H1 norm. For example use the
second estimate with a coefficient strictly smaller than 1/9, and the
gap for the remaining convex weight. Lax--Milgram consequently supplies
a weak inverse for the nonself-adjoint conjugated operator as claimed.

All principal radial coefficients are uniformly elliptic, and the lower
coefficients and every fixed number of their derivatives are bounded.
The ratio of W at any two points of a unit radial box is uniformly
bounded. Local elliptic estimates can therefore be multiplied by the
box weight and summed with bounded overlap. This yields the stated
global weighted Hm-to-H(m+2) inverse. Angular covariance introduces
bounded matrix coefficients for invariant tensors, not additional
uncontrolled angular derivatives. The argument is specifically for
the invariant sector.

## 3. The moving reference handles the non-L2 parameters correctly

The Banach map must be read as

\[
 F(z,k)=E[z]+\bigl(F(z,k)-F(z,0)\bigr).
\]

The first term belongs to Y by Section 1. Every term in the second
contains k or a derivative of k, with uniformly smooth bounded
coefficients depending analytically on z. Weighted multiplication follows
from two-dimensional local Sobolev estimates and the same uniformly
comparable box weights. At m=4 there is ample regularity both for the
quasilinear second derivatives and for global C2 smallness.

Thus the derivative \(D_kF(0,0)=L\) acts between exactly the invertible
spaces. The parameter derivative need not belong to X: it changes the
bounded background coefficient field and the integrable source. This
is a legitimate finite-dimensional-parameter implicit-function theorem.

The order estimates follow from \(E[0]=dE[0]=0\), and the local inverse
gives \(k=O(|z|^2)\). Fixing the background gauge instead would add the
displayed nonintegrable quadratic term; the moving reference is therefore
a substantive part of the proof.

## 4. Gauge removal does not assume the conclusion

The initial correction lies in weighted H6. Its Bianchi one-form is
therefore in H1 and L2 for g0, and also for G because G is uniformly
equivalent to g0 and its connection differs by uniformly bounded
coefficients. Uniform C2 closeness to g0 already implies
\(\operatorname{Ric}_G\le-cG\), before imposing the Einstein equation.

The contracted Bianchi identity for G applied to the gauged equation
gives
\((\nabla_G^*\nabla_G-\operatorname{Ric}_G)\omega=0\).
Testing with compact distance cutoffs times omega is justified on the
complete G. The cutoff term tends to zero because omega is L2; no
boundary condition at a compactification face is inserted. Coercivity
then gives omega=0. This establishes the actual Einstein equation and
the claimed moving Bianchi condition simultaneously.

Completeness follows from uniform equivalence to the complete product.
Higher derivative decay follows by local elliptic bootstrapping on the
same fixed radial boxes: the initial weighted H6 norm bounds their local
norms by \(O(|z|^2)W^{-3/4}\), the source has faster W-minus-one decay,
and background coefficients have bounded derivatives. The statement
allows the parameter neighborhood to shrink for any fixed finite list
of higher derivative estimates, which is sufficient.

## 5. End and flux assertions have the correct scope

The displayed face estimates follow from the endpoint expansion of J,
the \(p^2,q^2\) factors in the metric blocks, and the correction's
weighted pointwise bound. The end metrics are genuine limits of the
exact family. These are four radial faces of one model; they need not
be four topological ends or exact product regions outside a compact set.

For the second variation, projection against Q1 is integrable in t:
K and its derivatives contribute \(\cosh(t)^{-3/4}\), Q1 contributes
\(\cosh(t)^{-2}\), and the measure contributes \(\cosh(t)\).
The projected function M1 is also L2 in the u measure. Transverse
integration by parts and uniqueness of the projected scalar solution
are therefore justified.

The claim that expanding-square fluxes agree with the iterated limits is
consistent with these rates. On a t-face at |t|=R, the integrated error
is bounded by a constant times

\[
 e^{-7R/4}\int_{-R}^{R}e^{|u|/4}\,du=O(e^{-3R/2}).
\]

The omitted tails on the u-faces satisfy the same estimate. Thus the
second-order receiver coefficients have legitimate boundary limits.

The warning about fixed nonzero parameter flux is essential. The
W-minus-three-quarters bound by itself does not justify passing the
infinite boundary limit through the parameter Taylor expansion against
non-L2 detectors. The note makes no such claim.

## Review boundary

This review supports the exact invariant noncompact existence theorem,
given the round-two diagonal-operator and first-variation calculations
that it explicitly cites. It does not prove that the eight parameters
remain distinct modulo arbitrary diffeomorphisms. It does not give a
closed-model inverse, match physical angular periods to a closed bundle,
or remove the closed global kernel. Those remain separate mathematical
tasks, and the construction note states them as such.
