# Step 40: the actual m=2 coupled continuation mechanism

Session: S0910A03. Agent3 / Actuator. Phase: Execute.

## 0. Role of this note

The Step 39 defect power inequality is preserved: for p>=6 the homogeneous
s=|E|^2 calculation gives the defect Moser ladder without losing the initial
small defect factor.  The continuation theorem written in Step 39 is not yet a
proved theorem.  The remaining point is not only the order of the highest cutoff
jet.  It is the multiplication of the current cutoff jet by lower-order
curvature derivatives, especially at m=2.

This note treats the first nontrivial case directly.  It shows that the m=2
pair

\[
  V=\nabla^2U,\qquad Z=\nabla^3\chi,
\]

can be closed at a fixed finite exponent p, provided the m=1 base pair and the
first unweighted curvature-derivative estimate have already supplied finite
L^q bounds for

\[
  W=\nabla U,
  \quad \Theta=\nabla^2\chi,
  \quad T=\operatorname{Rm}+G,
  \quad \nabla T
\]

for the finite exponents used below.  The new mechanism is an additional signed
integration by parts on the term

\[
  \int \chi\,Z\,W\,|V|^{p-2}V,
\]

rather than the invalid estimate
\(\|W\|_{2p}\|Z\|_{2p}\|V\|_p^{p-1}\).  The latter asks for the current unknown
Z at a higher exponent.  The signed integration lowers Z to Theta and produces
only the weighted dissipation of V plus products of already available base-pair
norms.

This is a finite-exponent m=2 lemma, not a complete all-order continuation
theorem.  The all-order theorem still needs the same treatment written for every
possible high-cutoff/lower-curvature product, and the unweighted T-derivative
module must be proved by its own integrated equation rather than by dividing U
by a.

## 1. Standing smooth-interval hypotheses

Work on a smooth interval [tau,T) with tau>0 for the normalized cutoff flow

\[
  \partial_tg=-2aE,
  \qquad a=\chi^2,
  \qquad E=\operatorname{Ric}+g,
  \qquad U=aT,
  \qquad T=\operatorname{Rm}+G .
\]

Assume

\[
  \sup_{M\times[tau,T)}|U|\le K .
\]

Then the metrics are uniformly equivalent on [tau,T), |d chi| is bounded, and
finite Sobolev constants exist for this single smooth datum.  The zero-order
unweighted curvature estimate gives \(T\in L^q\) for all finite q.  The repaired
m=1 base pair gives

\[
  W=\nabla U\in L^q,
  \qquad \Theta=\nabla^2\chi\in L^q
\]

for every finite q.  Before the m=2 pair is used, one also needs the normalized
Wang Proposition 4.13 analogue at order one:

\[
  \nabla T\in L^q\quad\text{for all finite q}.        \tag{1.1}
\]

This is an independent integrated estimate.  It is not obtained by the false
claim that every derivative of a=chi^2 carries a chi factor.  In fact

\[
  \nabla^2a=2\chi\nabla^2\chi+2d\chi\otimes d\chi,      \tag{1.2}
\]

so a missing chi cannot be inserted in the transition region.  The unweighted
T estimate must instead use Wang's signed integration by parts in the actual
T equation.  For m=1 it requires only the already available \(\Theta\) and T,
not Z.  Section 4A below supplies this order-one integrated lemma.

## 2. The m=2 U energy and where the false higher-exponent demand appears

The high-cutoff part of the differentiated U equation at m=2 has schematic
terms

\[
\begin{array}{ll}
  \Gamma_1=\chi\nabla^4\chi*U, &
  \Gamma_2=d\chi*Z*U,\\[2mm]
  \Gamma_3=\chi Z*W, &
  \Gamma_4=\chi d\chi*\nabla V .
\end{array}                                      \tag{2.1}
\]

The precise numerical coefficients are irrelevant for this estimate; what is
load-bearing is the tensor placement and the displayed cutoff factors.  Testing
against

\[
  P(V)=|V|^{p-2}V,
  \qquad
  D_{2,p}=\int \chi^2|\nabla V|^2|V|^{p-2},
\]

the \(\Gamma_4\) term is standard:

\[
  \left|\int P(V)*(\chi d\chi*\nabla V)\right|
  \le \varepsilon D_{2,p}+C_{p,\varepsilon}r^{-2}\|V\|_p^p .   \tag{2.2}
\]

Integrating \(\Gamma_1\) once gives terms of the same three types:

\[
\begin{split}
 \int P(V)*(\chi\nabla^4\chi*U)
 ={}&-\int \nabla P(V)*\chi Z*U \\
 &-\int P(V)*d\chi*Z*U
   -\int P(V)*\chi Z*W .                                      \tag{2.3}
\end{split}
\]

The first two descendants are harmless current-exponent couplings:

\[
\begin{split}
 \left|\int \nabla P(V)*\chi Z*U\right|
 &\le \varepsilon D_{2,p}
      +C_{p,\varepsilon}K^2\int |Z|^2|V|^{p-2}                 \\
 &\le \varepsilon D_{2,p}
      +C_{p,\varepsilon,K}\bigl(\|Z\|_p^p+\|V\|_p^p\bigr),      \tag{2.4}
\end{split}
\]

and

\[
 \left|\int P(V)*d\chi*Z*U\right|
 \le C_{p,K,r}\bigl(\|Z\|_p^p+\|V\|_p^p\bigr).                 \tag{2.5}
\]

The direct treatment of the third descendant is the false step:

\[
  \left|\int P(V)*\chi Z*W\right|
  \le C\|W\|_{2p}\|Z\|_{2p}\|V\|_p^{p-1}.                     \tag{2.6}
\]

It asks for \(Z\) at exponent 2p while the current pair only controls \(Z\) at
exponent p.  Replacing \(\|Z\|_{2p}\) by \(\|Z\|_p\) is not a valid functional
step.  Passing to an ever larger exponent would not close a finite system.

## 3. The signed resolution of the residual \(\chi ZW\) term

Keep the tensor sign and write \(Z=\nabla\Theta\).  For any contraction of the
form

\[
  I_{ZW}=\int \chi\,Z*W*P(V),                                  \tag{3.1}
\]

one covariant integration by parts gives

\[
\begin{split}
 I_{ZW}={}&-\int d\chi*\Theta*W*P(V)
          -\int \chi\Theta*\nabla W*P(V)                         \\
         &-\int \chi\Theta*W*\nabla P(V).                       \tag{3.2}
\end{split}
\]

No boundary term appears on the closed manifold or with the stationary collar
localization.  Since \(\nabla W=V\), the middle term is a signed Hessian-cutoff
contraction in the current variable:

\[
  \int \chi\Theta*V*P(V)=\int\chi\nabla_i\nabla_j\chi\,B^{ij}(V),
\]

with

\[
  |B(V)|\le C_p|V|^p,
  \qquad |\nabla B(V)|\le C_p|V|^{p-1}|\nabla V| .              \tag{3.3}
\]

The Step 38 signed Hessian lemma gives

\[
  \left|\int \chi\Theta*V*P(V)\right|
  \le \varepsilon D_{2,p}+C_{p,\varepsilon}r^{-2}\|V\|_p^p .    \tag{3.4}
\]

The first term in (3.2) uses only base-pair norms:

\[
\begin{split}
 \int |d\chi|\,|\Theta|\,|W|\,|V|^{p-1}
 &\le Cr^{-1}\|\Theta\|_{2p}\|W\|_{2p}\|V\|_p^{p-1}             \\
 &\le C_{p,r}\bigl(1+\|V\|_p^p\bigr),                           \tag{3.5}
\end{split}
\]

where the coefficient depends on the already known finite norms of W and
Theta.

For the last term, use
\(|\nabla P(V)|\le C_p|V|^{p-2}|\nabla V|\).  Young's inequality with the
weighted dissipation gives

\[
\begin{split}
 \int\chi|\Theta||W||V|^{p-2}|\nabla V|
 &\le \varepsilon D_{2,p}
   +C_{p,\varepsilon}\int |\Theta|^2|W|^2|V|^{p-2}.              \tag{3.6}
\end{split}
\]

The remaining product contains no current cutoff jet.  In dimension four, or on
any finite-volume closed manifold with metric equivalence, Hölder with one
unused finite-volume factor gives

\[
\begin{split}
 \int |\Theta|^2|W|^2|V|^{p-2}
 &\le C(M,g(t))\,\|\Theta\|_{4p}^2\|W\|_{4p}^2\|V\|_p^{p-2}       \\
 &\le C_{p,W,\Theta}\bigl(1+\|V\|_p^p\bigr).                    \tag{3.7}
\end{split}
\]

Thus

\[
  |I_{ZW}|
  \le \varepsilon D_{2,p}+C_{p,W,\Theta,r}\bigl(1+\|V\|_p^p\bigr).  \tag{3.8}
\]

This is the missing m=2 mechanism.  It uses \(W,\Theta\) at higher finite
exponents, supplied by the m=1 base pair, but it never uses \(Z\) above the
current exponent p and never uses \(W\in L^\infty\).

The four displayed top-jet types are not the entire high-cutoff line.  The
remaining allocations are
\[
 \Theta*\Theta*U,
 \quad d\chi*\Theta*W,
 \quad \chi\Theta*V,
 \quad d\chi*d\chi*V .                                           \tag{3.9}
\]
The first two use \(\Theta,W\in L^{2p}\), the third is another signed
Hessian term, and the fourth is a bounded first-cutoff coefficient.  Therefore,
after including these allocations as well as (2.2)--(2.5) and (3.8), the complete
high-cutoff line in the m=2 U energy satisfies

\[
  \left|\int P(V)*\mathcal H_2\right|
  \le \varepsilon D_{2,p}
  +C_p\bigl(1+\|V\|_p^p+\|Z\|_p^p\bigr),                       \tag{3.10}
\]

with per-datum coefficients depending on finite base-pair norms.

## 4. Lower curvature products and the role of the unweighted T module

The remaining terms in the m=2 U equation contain products of the following
schematic types:

\[
  U*V,
  \quad W*W,
  \quad \nabla^ia*\nabla^jU*\nabla^kT\ (i+j+k=2,\ k\le1),
  \quad G\text{-linear terms}.                                  \tag{4.1}
\]

The first is linear in V with bounded coefficient K; the second is controlled by
\(W\in L^{2p}\); the G-linear terms contain no new high derivative.  The mixed
T-products require (1.1).  For example,

\[
 \int |\nabla T|\,|W|\,|V|^{p-1}
 \le \|\nabla T\|_{2p}\|W\|_{2p}\|V\|_p^{p-1}
 \le C(1+\|V\|_p^p).                                           \tag{4.2}
\]

Terms containing \(\nabla^2a\) are expanded using (1.2).  The
\(\chi\nabla^2\chi\) part is handled by signed integration by parts when it is
current-order; the \(d\chi\otimes d\chi\) part is a bounded first-cutoff
coefficient.  No estimate in this note uses an artificial chi factor in
\(\nabla^2a\).

Therefore the V-energy has the form

\[
  {d\over dt}\|V\|_p^p+cD_{2,p}
  \le C_p\bigl(1+\|V\|_p^p+\|Z\|_p^p\bigr).                    \tag{4.3}
\]

## 4A. The missing order-one unweighted T derivative lemma

The required input \(\nabla T\in L^p\) follows from its own whole-manifold
energy estimate.  It does not follow from Leibniz inversion or from small metric
drift near \(\{\chi=0\}\).

Set \(X=\nabla T\).  Differentiating
\[
 (\partial_t-a\Delta)T
 =a(T*T+G*T)+\nabla a*\nabla T+\nabla^2a*T
\]
and including connection variation gives the safe schematic equation
\[
\begin{split}
 \partial_tX={}&a\Delta X+\nabla a*\nabla X+\nabla^2a*X+\nabla^3a*T\\
 &+aT*X+aG*X+\nabla a*T*T+\nabla a*G*T+\nabla U*T .              \tag{4A.1}
\end{split}
\]
Test against \(P(X)=|X|^{p-2}X\), with
\(D_p^T=\int a|\nabla X|^2|X|^{p-2}\).  The diffusion and first-cutoff terms
are controlled using \(|\nabla a|^2/a=4|d\chi|^2\).  Expand rather than
factor the higher cutoff derivatives:
\[
 \nabla^2a=2\chi\Theta+2d\chi\otimes d\chi,
 \qquad
 \nabla^3a=2\chi\nabla\Theta+C\,d\chi*\Theta .                    \tag{4A.2}
\]
The \(d\chi\otimes d\chi*X\) term is zeroth order.  The
\(\chi\Theta*X\) term is a signed Hessian contraction and obeys the Step 38
lemma.  For the only third-cutoff term, integrate only the derivative in
\(\chi\nabla\Theta\):
\[
\begin{split}
 \int \chi\nabla\Theta*T*P(X)
 ={}&-\int d\chi*\Theta*T*P(X)
     -\int\chi\Theta*X*P(X)\\
    &-\int\chi\Theta*T*\nabla P(X).                              \tag{4A.3}
\end{split}
\]
The first term uses \(T,\Theta\in L^{2p}\); the second is again signed
Hessian; and the last gives
\[
\begin{split}
 \int\chi|\Theta||T||X|^{p-2}|\nabla X|
 &\le\varepsilon D_p^T
  +C_{p,\varepsilon}\int|\Theta|^2|T|^2|X|^{p-2}\\
 &\le\varepsilon D_p^T+C_p(1+\|X\|_p^p),                         \tag{4A.4}
\end{split}
\]
using \(T,\Theta\in L^{2p}\).  It is important not to integrate the whole
\(\nabla(\nabla^2a)\) blindly: doing so can leave a
\(d\chi\otimes d\chi*T*\nabla P(X)\) term without a chi factor for the
degenerate dissipation.

The reaction terms satisfy, for example,
\[
 \int a|T||X|^p=\int|U||X|^p\le K\|X\|_p^p,
\]
\[
 \int|\nabla a||T|^2|X|^{p-1}
 \le C\|T\|_{2p}^2\|X\|_p^{p-1},
 \qquad
 \int|\nabla U||T||X|^{p-1}
 \le\|W\|_{2p}\|T\|_{2p}\|X\|_p^{p-1}.                         \tag{4A.5}
\]
Thus
\[
 {d\over dt}\|\nabla T\|_p^p+cD_p^T
 \le C_p(1+\|\nabla T\|_p^p),                                  \tag{4A.6}
\]
and Gronwall proves (1.1) for every finite p.  The precise input at target p is
finite \(T,W,\Theta\) norms at exponents no larger than \(2p\), together with
\(|U|\le K\), metric equivalence, \(|d\chi|\), and smooth data at time tau.
No \(Z\) norm, division by a, or unweighted pointwise curvature is used.

This also disproves the proposed alternative split
\(\{\chi\ge\delta\}\cup\{\chi<\delta\}\): \(|aE|=|\operatorname{Ric}(U)|\le
C|U|\) has no additional \(\chi^2\) smallness on \(\{\chi<\delta\}\), and even
small \(C^0\) metric drift would not control curvature derivatives.

## 5. The Z equation closes at the same exponent

For the fixed scalar chi, variation of covariant derivatives gives, at the
third derivative level,

\[
  \partial_t Z
  = \nabla(\partial_t\Gamma)*d\chi+\partial_t\Gamma*\Theta+\text{lower metric contractions}.  \tag{5.1}
\]

Because

\[
  \partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
\]

the current terms in (5.1) are

\[
  V*d\chi,
  \qquad W*\Theta,                                             \tag{5.2}
\]

plus lower products controlled by the already bounded base norms.  Testing
against \(|Z|^{p-2}Z\) gives

\[
\begin{split}
 {d\over dt}\|Z\|_p^p
 &\le C_p\|V\|_p\|Z\|_p^{p-1}
      +C_p\|W\|_{2p}\|\Theta\|_{2p}\|Z\|_p^{p-1}                 \\
 &\qquad +C_p(1+\|Z\|_p^p)                                      \\
 &\le C_p\bigl(1+\|V\|_p^p+\|Z\|_p^p\bigr).                    \tag{5.3}
\end{split}
\]

Thus the pair

\[
  Y_{2,p}(t)=\|\nabla^2U(t)\|_p^p+\|\nabla^3\chi(t)\|_p^p
\]

satisfies

\[
  Y_{2,p}'(t)
  \le C_p(1+Y_{2,p}(t)),                                      \tag{5.4}
\]

and Gronwall gives finite \(L^p\) control of the m=2 pair on [tau,T).  The
constant is per-datum and depends on finite norms of W, Theta, T and nabla T at
specified exponents.

## 6. Consequences and remaining work

This m=2 calculation repairs the specific multiplication problem identified in
the Step 40 strategist note.  The problematic residual
\(\chi Z\nabla U|V|^{p-1}\) is not estimated by the invalid
\(\|Z\|_{2p}\) route; it is integrated by parts once more and becomes a mixture
of:

1. a current signed Hessian term \(\chi\Theta B(V)\), paid by the Step 38 lemma;
2. a diffusion term with coefficient \(\Theta W\), paid using finite base-pair
   exponents;
3. lower products containing only W and Theta.

This supports a plausible all-order pattern: when the top current cutoff jet is
multiplied by a lower derivative of U, integrate off that cutoff jet until the
derivative either lands on the lower U-factor or on P(\nabla^mU).  The former
raises the lower U derivative by one; at m=2 this reaches V and becomes a signed
current Hessian term.  The latter is paid by weighted diffusion with lower-level
finite-exponent coefficients.  But the all-order pattern has not yet been
written for arbitrary distributions, so Step 39's all-order continuation theorem
must remain superseded.

A complete continuation theorem still requires:

- the normalized Wang Proposition 4.13 analogue for unweighted
  \(\nabla^jT\) at every higher order; Section 4A proves only the first-derivative
  case needed before the m=2 pair;
- the arbitrary-m version of the extra integration used in Section 3, with a
  finite exponent schedule for every lower-derivative product;
- the shifted terminal extension proof using bounded derivatives of the compactly
  supported velocity \(aE=\operatorname{Ric}(U)\);
- transported-coefficient short-time existence for the normalized equation.

Until these are written, the smoothing principle remains a strong developing
analytic mechanism rather than an established flow theorem.  The full Yau 26
problem remains much broader: positive branch, arbitrary four-dimensional
topology, dimensions n>=5, dimension-only constants, and Lean formalization are
not settled by this restricted negative-branch analysis.
