# Step 61: Preceptor review of the restricted negative-flow module and route reset

Session: S0910A03. Agent4 / Preceptor. Phase: Execute.

## 0. Mathematical judgment

The Step 60 continuation idea survives independent reconstruction, but two
corrections were necessary before it could be retained:

1. The exact shifted-curvature equations have no independent constant forcing.
   For
   \[
   a=\chi^2,\qquad G=\frac{g\owedge g}{2(n-1)},\qquad
   T=\operatorname{Rm}+G,\qquad U=aT,
   \]
   the flow is \(g_t=-2\operatorname{Ric}(U)\), and \(T=U=0\) is stationary for
   every cutoff.  Thus the true reaction terms are
   \[
   (\partial_t-a\Delta)T=da*\nabla T+\nabla^2a*T+a(T*T+G*T),
   \]
   \[
   (\partial_t-a\Delta)U=da*\nabla U+\nabla^2a*U+(da*da)*T
      +U*U+aG*U.
   \]
   The former \(a\cdot1\) and \(a^2\) entries, and their isolated derivative
   families \(B_m\) and \(\nabla^m(a^2)\), were artifacts of a rough upper
   envelope rather than tensor identities.

2. The uniform same-exponent residual argument is not a proof of the first
   weighted level.  At \(m=1\), the residual contains \(U_1\), which is the
   current unknown.  The hierarchy must use the separately established base
   \[
   T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
   \]
   and apply the universal \((U_m,C_{m+1})\to T_m\) step only for \(m\ge2\).

Both corrections are now incorporated into
`workspace/notes/step60_all_order_continuation_and_terminal_chart.md` and its
allocation script.  The corrected script again checks 252,256 allocations
through order 64 with zero failures.  Independent TTCS reconstruction is in
`trace/ttcs/results/step61_ttcs01_verifier1_integration.md`.

## 1. What the corrected all-order argument establishes

On a positive-time slab with bounded \(U\), bilipschitz metrics, finite
per-datum Sobolev constants, and the established base layer, the exact identities
\[
(da*da)*T=4(d\chi*d\chi)*U,
\qquad
aT_m=U_m-\sum_{q=1}^mB_q*T_{m-q}
\]
prevent an unweighted current \(T_m\) from entering the \(U_m\) equation.
Spatial commutators with at least one derivative on \(a\) are prior-level;
reordering time commutators introduces only \(T_q\) with \(q\le m-2\).
Because \(\chi\) is a fixed scalar, \(\partial_t(d\chi)=0\), and therefore
\[
\partial_tC_{m+1}=U_m*C_1+\text{prior-level terms},
\]
with neither \(U_{m+1}\) nor \(C_{m+2}\).

The sole new cutoff jet in the \(U_m\) equation is the
\(2\chi C_{m+2}*U_0\) part of \(B_{m+2}*U_0\).  Integrating only this part once
leaves
\[
I_m=\int\chi|C_{m+1}|\,|U_1|\,|U_m|^{p-1}.
\]
For \(m\ge2\), \(U_1\) is prior-level, and in dimension four Sobolev applied to
\(\chi|U_m|^{p/2}\) keeps \(C_{m+1}\) and \(U_m\) at the same exponent \(p\).
Together with signed integration of the current Hessian, this gives the
triangular all-order bounds.  Fixed-background conversion then controls every
spatial derivative of \(g\) and \(g_t\), yielding a positive-definite
\(C^\infty\) terminal metric.  A restart there has the same recursively
specified autonomous-PDE time jets, so the direct splice is smooth and does not
need overlap uniqueness.

This is a substantive analytic module, but its proof remains at the universal
star-contraction level rather than a formal coordinate-index expansion.  The
independent reconstruction found no missing derivative family after the two
corrections above.

## 2. Terminal pullback module

The Step 60 terminal argument is mathematically coherent under its stated
inputs.  If the same buffered center set satisfies
\[
\operatorname{Vol}_{g(T)}P\ge c_0A,
\qquad
\int_M\mathfrak D\le C_0\delta^2A,
\]
and all radial geodesics of a fixed length \(\rho\) remain inside a plateau
with \(|\operatorname{Rm}|\le K\), Liouville invariance selects an exponential
pullback ball with mean density \(O(\delta^2)\).  The topology scale \(A\)
cancels.  Center injectivity in the pullback domain plus Rauch comparison gives
a fixed harmonic chart.  The harmonic-coordinate Ricci equation yields a
smooth negative-Einstein limit and strong \(W^{2,q}_{\rm loc}\) convergence.
The latter gives strong \(L^q\) curvature and \(L^1\) convergence of the
nonnegative spectral density; it does not give pointwise convergence of the
approximating curvatures.  Zero integral plus continuity of the smooth limit
forces the density to vanish on an open ball, hence
\[
\operatorname{Spec}(W^+)=(-1/6,1/12,1/12).
\]
The verified projector lemma gives \(\nabla W^+=0\), while the Einstein--Weyl
identity gives \(|\nabla W^+|^2=1/16\), a contradiction.

The spectral gap density is denoted \(\mathcal G\) in the corrected note, to
avoid collision with the shifted-curvature background tensor \(G\).

## 3. Source-level topology check

The original Ishida--LeBrun source confirms the output obstruction being used.
Its Theorem D states that, for the specified almost-complex summands with the
mod-2 Seiberg--Witten/Bauer--Furuta hypotheses and \(N\) with \(b_+(N)=0\),
\[
4m-(2\chi+3\tau)(N)\ge\frac13\sum_jc_1^2(X_j)
\]
excludes every Einstein metric on the connected sum for \(m=2,3,4\).  Thus the
restricted route really concerns smooth manifolds already known to have no
Einstein metric, rather than only excluding Einstein constant \(-1\).  The
full monopole-family and geography hypotheses must remain explicit.

## 4. Remaining mathematical dependence of the restricted result

The restricted negative mechanism is much stronger than a local model, but it
is not yet a theorem that should be used as a solved component without further
work.  Its remaining dependence is the connected proof, on the same exact
flow, of:

- the Step 56 doubly regularized transported-cutoff construction and smooth
  zero-regularization limit;
- the exact tensor-level \(H_2\), curvature all-\(p\), \(Q\), \(J_6\), and
  defect all-\(p\) inequalities, including moving norms and measure terms;
- the simultaneous first-exit bootstrap with evolving local Sobolev constants;
- construction and persistence of the same proportional-volume buffered center
  set used by the terminal Liouville argument.

Several of these pieces have detailed derivations and independent checks, but
they have not been compressed into one proof in which every tensor identity,
support convention, and constant is traced on a single realized flow.  The
allocation scripts verify derivative arithmetic, not tensor coefficients or
signs.  Therefore the correct present result is a highly developed candidate
proof of a restricted four-dimensional negative input-metric gap.

## 5. Relation to the full Yau problem and next research direction

Even if the entire restricted module is completed, it does not decide the
original quantifiers.  It excludes only sufficiently tight negative normalized
pinching on selected four-dimensional no-Einstein geographies.  It does not
construct any no-Einstein manifold carrying a metric in a fixed dimension-only
interval, nor prove that some interval forces Einstein existence.  Positive
pinching in dimension four and all dimensions \(n\ge5\) remain without a
comparable mechanism, and no Lean formalization is appropriate before the
mathematics is complete.

After many consecutive execution steps, further local refinement of the same
PDE hierarchy has sharply diminishing value for the highest goal unless it is
used to complete the connected restricted theorem.  The next main inquiry
should therefore return to the quantifier-level problem: compare routes that
could convert a restricted gap into a genuine dimension-only statement, or
produce explicit fixed-width pinched metrics on manifolds with an obstruction
to every Einstein metric.  Promising independent evidence includes A02's
orbifold/ALE matching and toric-cone Bianchi-flux work, but it presently remains
local and cannot yet decide the same-manifold output quantifier.  The restricted
flow module should be preserved as a tested four-dimensional component while
Agent1 reopens the positive branch, higher-dimensional constructions, and
possible global compactness/contradiction principles.