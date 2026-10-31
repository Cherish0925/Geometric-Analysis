# Step 27 consolidated status

## Advance

The normalized local-flow continuation problem has been repaired at the
highest-derivative level.  The Step 26 specification was incomplete because
splitting the velocity into Ricci and normalization pieces exposes
\(-(\nabla^2a)\owedge g\), whose \(m\)-th derivative reaches
\(\nabla^{m+2}a\).  Metric comparison and \(|a\operatorname{Rm}|\) do not
control these cutoff jets directly.

The repair is the parallel shifted curvature

\[
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\operatorname{Rm}+G,\qquad U=aT,
\]

in the convention \(\operatorname{Ric}(G)=g\).  Then

\[
\operatorname{Ric}(T)=E=\operatorname{Ric}+g,
\quad \operatorname{Ric}(U)=aE,
\quad \nabla G=0,
\]

and \(\partial_tG\) is algebraic in \(aE\) and \(g\).  The shifted evolution
has Wang's source structure:

\[
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T).
\]

The weighted equation for \(U\) has the same highest term
\(\chi\nabla^{m+2}\chi*U\) as Wang's local Ricci flow.  One integration by
parts absorbs its derivative-on-\(\nabla^mU\) component into the weighted
diffusion and lowers the remaining cutoff order to \(m+1\).  The cutoff-jet
evolution is driven exactly by derivatives of
\(aE=\operatorname{Ric}(U)\).  The current-order Volterra pair is therefore

\[
\nabla^mU\longleftrightarrow\nabla^{m+1}\chi,
\]

while \(\nabla^{m-1}T\) needs only \(\nabla^m\chi\) and is prior-level data.
The \(G\)-terms are bounded linear reactions or lower-order products and do
not create a pure highest-cutoff source.  Exact stationarity at \(T=0\) also
shows that the shifted algebraic reaction has no true constant term.

A theorem-level note at
`workspace/notes/step27_normalized_local_flow_extension_theorem.md` carries
the base unweighted \(L^p\) estimate, the Wang 4.11 coupled base step, the
high-order induction, the smooth terminal reconstruction, the transported
normalized DeTurck restart, and the interface with the \(C/t\) Moser bound.
Two independent TTCS branches found no uncancelled highest-order term and
identified the derivative-index correction above.  The algebraic bookkeeping
script `workspace/scripts/verify_step27_shifted_curvature_algebra.py` exits 0.

## Qualification

The detailed proof inherits Wang's finite staggered-exponent Hölder scheme;
all new terms were classified, including commutators such as
\(\operatorname{Ric}(\nabla^mU)*T\), which use high finite \(L^p\) norms rather
than unweighted \(L^\infty\) curvature.  An independently launched Codex run is
still deriving the transfer and must be inspected before the whole
four-dimensional chain receives an Agent4 review.  The old Step 26
continuation specification is superseded at this point.

## Consequence for the active route

If the independent derivation confirms the theorem note, the Step 26
whole-support estimate

\[
\|a\operatorname{Rm}(t)\|_\infty\le C\bar\beta/t
\]

rules out any positive maximal time below the target: it is bounded near that
positive terminal time, and the normalized extension theorem restarts the
flow.  Uniform higher derivatives across the pinching sequence are then
obtained only on a strict \(a=1\) plateau at positive time, followed by the
calibrated exponential-chart limit and the Step 6 projector/Einstein--Weyl
contradiction.

This remains a route for a critical four-dimensional negative
Ishida--LeBrun family.  It does not settle the unrestricted negative branch,
the positive branch, dimensions at least five, dimension-only quantifiers, or
Lean formalization of Yau 26.
