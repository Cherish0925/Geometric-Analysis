# A finite-measure Jacobi argument for the closed-collar receiver

20 September 2026. This is an independent derivation of the limiting
classification and sign used in `round5_construction.md`. The limit contains
the entire finite-area fibre, not only its thin cylinder. The passage from a
closed degenerating metric to this limit remains a separate argument in that
note.

## 1. Object, operator, and boundedness

Let

\[
 C=(\mathbb R_t\times\mathbb R_y,dt^2+\cosh^2t\,dy^2),\qquad
 X=C\times F,
\]

where \(F\) is a connected complete finite-area hyperbolic surface with
finitely many cusp ends. Work with tensors independent of \(y\), and integrate
over one unit of \(y\). All boundedness is in the product orthonormal frame.
Put \(\Delta=\nabla^*\nabla\) on functions, with nonnegative sign, and

\[
 2L=\nabla^*\nabla-2\mathring R,\quad
 P_t=\partial_t^2+\tanh t\,\partial_t,\quad
 f=\operatorname{sech}^2t,\quad J=\arctan(\sinh t).
\]

The following concerns bounded smooth solutions of \(LV=0\) in Bianchi
gauge. The block equations can also be interpreted weakly; interior
regularity on local covers then gives the derivatives used below. Write
\(T=dt^2-\cosh^2t\,dy^2\), and let \(S\) be the other unit-frame trace-free
symmetric polarization, with off-diagonal entries equal to one.

The product connection splits the tensor operator into:

* scalar trace blocks: \(-P_t+\Delta_F+2\);
* horizontal trace-free coefficients: \(-P_t+\Delta_F+2-4f\);
* mixed coefficients valued in one-forms on \(F\):
  \(-P_t+\Delta_{H,F}+2-f\);
* fibre trace-free block: \(-P_t+A_F\), where
  \(A_F=\Delta_{E,F}=2P_F\delta_F\), and \(P_F\) is the trace-free
  symmetrized gradient, the adjoint of \(\delta_F\).

These are equations for all tensor blocks, not an ansatz restricting the
unknown tensor to diagonal or fibrewise constant form.

## 2. Horizontal modes: finite measure rules out hidden resonances

Let a bounded scalar \(z(t,p)\) solve the horizontal equation. Direct
differentiation gives

\[
 (-P_t+2-4f)f=0.
\]

For sufficiently large fixed \(T_0\), the zeroth-order coefficient is at
least one on either half-region \(|t|\ge T_0\). Compare \(z\) and \(-z\)
with \(Cf\), choosing \(C\) to dominate the data at \(t=\pm T_0\).
The bounded maximum principle on each complete half-region gives
\(|z|\le Cf\). It applies here without a compactness assumption on \(F\):
the product has a Ricci lower bound, bounded drift, and a strictly positive
zeroth-order term. Equivalently, use complete distance exhaustions to
penalize a positive supremum away from the boundary.

Thus \(v=z/f\) is bounded, and its equation is

\[
 -v_{tt}+3\tanh t\,v_t+\Delta_Fv=0.
\]

This is a divergence-form equation with the **finite** measure

\[
 d\nu=\operatorname{sech}^3t\,dt\,dV_F,
 \qquad \nu(\mathbb R\times F)=\frac\pi2\operatorname{Area}(F).
\]

Testing with \(\chi_R^2v\), where \(\chi_R\) is a complete distance cutoff
with \(|d\chi_R|\le C/R\), gives

\[
 \int\chi_R^2|dv|^2d\nu
 \le4\|v\|_\infty^2\int|d\chi_R|^2d\nu\longrightarrow0.
\]

Consequently \(v\) is constant. The horizontal block is exactly
\(f(aT+bS)\). This proof includes continuous-spectrum fibre components;
no discrete eigenfunction expansion or uniform injectivity radius is needed.

## 3. Other blocks and the full bounded kernel

Bounded coefficients on \(F\) are square integrable, since its area is
finite. For a solution \(Z(t)\) in such a Hilbert-valued block, set
\(w(t)=\|Z(t)\|_{L^2(F)}^2\). Integrating by parts in the cusp ends is
justified by bounded local-cover derivatives and finite-volume cutoffs.
The trace and mixed equations imply respectively

\[
 P_tw\ge4w,\qquad P_tw\ge2(2-f)w\ge2w.
\]

Both bounded nonnegative functions vanish by the one-dimensional bounded
maximum principle. Thus there are no trace or mixed modes.

For completeness, the gap for \(A_F\) on the orthogonal complement of the
\(L^2\) TT tensors is at least two. Indeed, on one-forms

\[
 \delta_FP_F=\frac12(\Delta_{H,F}+2)\ge1.
\]

The closed operators \(2P_F\delta_F\) and
\(2\delta_FP_F=\Delta_{H,F}+2\) have the same nonzero spectrum; the latter
is bounded below by two. These identities first hold on compactly supported
smooth sections and extend by the complete-manifold closures. Projection
of the fibre block onto the orthogonal complement of its TT kernel
therefore gives \(P_tw\ge4w\), so that component vanishes.

The remaining TT-valued equation is \(P_tZ=0\). Hence

\[
 \boxed{V=f(aT+bS)+A+J(t)B,}
\]

where \(A,B\) are bounded \(L^2\) TT tensors on \(F\). In particular the
entire finite-area fibre contributes only its genuine hyperbolic
deformation directions, not an arbitrary exterior response.

## 4. Receiver sign without a coordinate Ricci expansion

Set \(Q=fT\). It is a TT Jacobi tensor; it and its covariant derivatives
are integrable on \(X\) per unit \(y\)-period. The fibre part of \(V\) can
be realized by the determinant-preserving path

\[
 H_s(t)=h_F\exp\{s\,h_F^{-1}(A+J(t)B)\}.
\]

The endomorphism in the exponential is self-adjoint and trace free, so
\(H_s\) is positive for small \(s\) and has exactly the original fibre
area form. In the metric \(g_C+H_s(t)\), its fibre shape operator is
\(\mathcal S_s=\frac12H_s^{-1}\partial_tH_s\), with zero trace. The base
Ricci equations give

\[
 (\operatorname{Ric}+g)_{tt}=-\operatorname{tr}\mathcal S_s^2
 =-\frac{s^2}4(J')^2|B|^2+O(s^3),\qquad
 (\operatorname{Ric}+g)_{yy}=0.
\]

Only these two blocks enter the \(Q\)-pairing. The second derivative of
the metric path contributes \(DE[H''_0]\); its pairing with \(Q\) is zero
by the adjoint equation and integrable-tail cutoffs. The horizontal
\(f(aT+bS)\) term can independently be realized by an exact hyperbolic
cylinder path. It has zero receiver and no quadratic cross term with the
fibre variation: the fibre contribution starts at the square of its
first-order shape operator.

Since \(J'=\operatorname{sech}t\),

\[
 \boxed{
 \frac12\int_X\langle D^2(\operatorname{Ric}+g)[V,V],Q\rangle dV
 =-\frac14\|B\|_{L^2(F)}^2\int_{\mathbb R}\operatorname{sech}^3t\,dt
 =-\frac\pi8\|B\|_{L^2(F)}^2\le0.}
\]

This is a sign theorem for every bounded Bianchi Jacobi field in the
declared limit, not just a calculation for one balanced profile. A pure
gauge addition has zero effect on the receiver whenever its first three
weak covariant derivatives have the bounds needed for the same cutoff
integration: diffeomorphism covariance expresses its change as \(DE[Z]\)
for a bounded tensor \(Z\).

## 5. Exactly what this adds to the closed problem

The closed detector in `round3_matching_next.md`, Section 6, requires a
positive limit \(1/(2\pi^2)\) if an exact correction has size
\(O(\varepsilon^{3/2})\). The sign above supplies the previously missing
contradiction **provided** the actual beta-normalized closed receiver
converges to this whole-fibre receiver after bounded gauge fixing. Those
compactness, tail and gauge arguments are provided separately in
`round5_construction.md`; they cannot be replaced by thin-core convergence.

The zero set \(B=0\) also identifies the next obstruction to a larger
claim. Constant fibre deformations, cylinder parameters and gauge changes
survive. A conclusion excluding every correction tending to zero would
require quantitative modulation of those directions and uniform remainder
estimates, not just the nonpositive limiting quadratic form. This note
does not assert Einstein nonexistence on \(E_D\).
