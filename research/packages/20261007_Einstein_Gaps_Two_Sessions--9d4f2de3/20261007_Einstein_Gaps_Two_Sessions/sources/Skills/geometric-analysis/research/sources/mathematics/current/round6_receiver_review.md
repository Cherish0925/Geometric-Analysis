# Independent review of the receiver-weighted inverse and closed transfer

20 September 2026. Reviewed round6_weighted_inverse.md and
round6_construction.md, including their full tensor blocks, weighted
domains, gauge removal, marked collar comparison, and final error ledger.
The balanced construction and global TT estimates were checked against the
actual construction derivations, not inferred from the previous summary.

**Conclusion.** I found no blocking mathematical error in the claimed
fixed-small-multiple \(c_*\varepsilon\) exclusion, or in the sharp
coefficient under the smaller hypothesis \(a=o(\varepsilon)\). The
functional-space change is substantive: the receiver-weighted inverse
does not imply a maximum-norm inverse, and does not need one. A reference
problem and its self-contained replacement are recorded below.

## 1. Weighted domains and the horizontal factorization

In \(L^2(w\,dt)\), \(w=\operatorname{sech}t\), the derivative adjoint is
\(\partial_t^*=-\partial_t+\tanh t\). Writing \(k=\tanh t\) and \(f=w^2\),
direct calculation gives

\[
\begin{aligned}
(-\partial_t+k)(\partial_t+2k)&=-P+2-4f,\\
(\partial_t+2k)(-\partial_t+k)&=-P+2-f,\\
(\partial_t+2k)(-\partial_t+3k)
 &=\partial_t^*\partial_t+6-3f\ge3.
\end{aligned}
\]

Thus the first-order closed-range estimate is legitimate on the weighted
\(H^1\) domain; its one-dimensional kernel is exactly \(\mathbb R f\).
The constant function is the weighted adjoint kernel of \(-P+2-4f\).
In particular the coefficient equation
\(\lambda\int wz=\int wF\) is correct. It is not an unweighted
self-adjoint orthogonality assertion.

For \(v=(\partial_t+2k)z\), the partner equation is an
\(H^{-1}_w\)-forcing equation. Its energy is
\[
\int w\bigl(|v'|^2+(1+\lambda+f)|v|^2\bigr),
\]
and pairing \(D_1F\) with \(v\) differentiates \(v\), not \(F\).
Consequently no missing derivative of the original residual is needed.
For \(z\in H^2_w\), \(v\in H^1_w\), so exhaustion of this weak pairing
is justified in the declared domain. The rank-one change from projection
orthogonal to \(f\) to \(\int w(z-cf)=0\) is uniformly bounded because
\(\int wf>0\) is fixed.

At large fibre eigenvalue the elementary energy estimates yield, in order,
\(\lambda\|z\|_2\le C\|F\|_2\),
\(\sqrt\lambda\|z'\|_2\le C\|F\|_2\), then
\(\|z''\|_2\le C\|F\|_2\) from the equation. Thus the parameter estimates
needed for the full tensor \(H^2_w\) norm are present.

## 2. The TT transfer block and full covariant derivatives

The vertical TT right inverse is also valid. On the positive half-line
its undifferentiated Volterra kernel is bounded by a fixed constant.
After multiplication by \(\sqrt{w(t)/w(s)}\), it is bounded by
\(Ce^{-(t-s)/2}\) for \(t\ge s\); the differentiated kernel is bounded by
\(Ce^{-3(t-s)/2}\). Young's inequality therefore controls \(r,r'\);
the equation controls \(r''\). The zero initial value and derivative at
zero match the two half-line solutions in \(H^2_w\). The two-dimensional
scalar kernel is exactly \(\operatorname{span}\{1,J\}\), so the
TT-valued kernel is \(A+JB\), and must not be reduced to \(A\).

There is no loss of fibre derivatives hidden in these scalar estimates.
On every closed curvature-\(-1\) fibre,
\[
2\delta_FP_F=\Delta_{H,F}+2,\qquad
A_F=2P_F\delta_F=\nabla_F^*\nabla_F-2
\]
on trace-free two-tensors. The positive \(A_F\)-spectrum is at least two.
For a TT tensor \(B\), \(\|\nabla_FB\|_2^2=2\|B\|_2^2\), and commuting
one derivative gives \(\|\nabla_F^2B\|_2\le C\|B\|_2\).
The curvature and its derivatives are uniformly controlled, indeed
parallel. Analogous integrated identities on the other fibre blocks
give the required first and second derivative estimates. None is a
collapsing Sobolev embedding.

## 3. Scalar gap: correct hypothesis and resolved reference issue

Only one nonseparating fibre geodesic degenerates; the complementary
marked data stay in a fixed compact family. This is sufficient for the
uniform positive scalar gap used in the horizontal sector. It would be
false for a separating degeneration. The first draft's International Press
PDF link pointed to a commentary preview by Yau, not the original theorem
statement, and the full fetch returned 403 in this review. This issue has
been resolved in the reviewed revision by inserting a direct proof.
The relevant fact is also
explicitly recorded in [Ji--Wentworth, *Spectral convergence on
degenerating surfaces*, p. 493](https://math.umd.edu/~raw/papers/spectrum.pdf).

The inserted proof establishes the needed fact without this reference.
On a hyperbolic collar, conjugation of its radial
Dirichlet operator by \(\sqrt{\cosh u}\) gives
\[
-(\partial_u^2+\tanh u\,\partial_u)
\ \longleftrightarrow\
-\partial_u^2+\tfrac14+\tfrac14\operatorname{sech}^2u.
\]
The angular term is nonnegative, so the full collar Dirichlet gap is at
least \(1/4\), uniformly in its length and waist.

If normalized mean-zero eigenfunctions had eigenvalues tending to zero,
they would converge on the connected thick complement to one constant
\(c\). The two outer collar strips have uniform geometry and the same
limit \(c\). Cut off \(u_\varepsilon-c\) only on those fixed-width outer
strips. Its Dirichlet energy tends to zero, so the preceding collar
estimate prevents any \(L^2\) mass from escaping into the long collar.
Together with convergence on the complement this gives
\(\|u_\varepsilon-c\|_2\to0\). Mean zero and fixed area force \(c=0\),
contradicting normalization. Nonseparation is used exactly in requiring
the same constant at the two collar faces. This argument repairs the
citation weakness without adding a new geometric hypothesis.

## 4. The actual closed collar and angular error

The annular trivialization is compatible with the specified bundle:
the Dehn twist is at a transverse collar face, not around the short
angular loop. Hence the components are genuinely beta-periodic, and
angular averaging commutes with the product operator.

The comparison with a single closed fibre is uniformly valid on the
whole collar. In the product orthonormal frame, the shear is
\[
\frac{\varepsilon\,\tau(t)\chi_R(u)\operatorname{sech}^2u}{I_R}.
\]
Every fixed covariant derivative is \(O(\varepsilon)\): angular frame
derivatives of the coefficients vanish and the remaining connection
coefficients are uniformly bounded. This verifies the claimed
\(C^k\) comparison, including the ends where the metric is
\(D^*h_F\) in the chosen marking. The comparison does not assert that
the Dehn twist is isotopic to the identity.

The cutoff commutator is \(O(a)\) on a set of weighted measure
\(O(e^{-L})=O(\beta)\), giving precisely \(O(a\sqrt\beta)\) in
weighted \(L^2\). Since \(\sqrt\beta=\varepsilon\), this is included in
the existing \(\varepsilon a\) forcing budget.

For the angularly oscillatory part, Poincaré applied to components and
first covariant derivatives gives a factor
\((\beta\cosh t)^2\). After multiplication by \(w\) and integration,
\[
\beta^2\int_{-L}^L\cosh t\,dt=O(\beta).
\]
The mixed bilinear terms vanish by angular averaging. Integrating the
quadratic Ricci form once by parts therefore costs \(O(\beta a^2)\),
without assuming small second angular derivatives. The actual detector
error \(O(\beta^2)\), after division by \(\beta\) over bounded physical
volume, has the same order. The background comparison costs
\(O(\varepsilon a^2)\). These are the terms in (4.5), with no omitted
exterior response.

## 5. Gauge covariance and the error ledger

The gauge equation \((\nabla^*\nabla+1)X=bH\) has the advertised coercive
weighted blocks. Pointwise \(C^2\) control of \(X\) needs only the
Lipschitz bound on \(bH\), supplied by the \(C^2\) hypothesis on \(H\).
Weighted \(H^3\) control follows from \(bH\in H^1_w\).
A uniform pointwise third derivative of \(X\), or of \(H\), is not
required: the gauged tensor is estimated in \(H^2_w\).

For \(V=H-\mathcal L_Xg_*\) and \(F=DE\,H=DE\,V\), differentiating
the pulled-back metric path gives exactly
\[
D^2E[H,H]-D^2E[V,V]
 =2\mathcal L_XF-DE[\mathcal L_X(H+V)].
\]
In particular the \(2\mathcal L_XF\) term cannot be dropped; it has
correctly been retained. Its pairing is \(O(a\|F\|_{L^2_w})\) after
moving the Lie derivative onto the integrable detector. The linear term
vanishes distributionally: its argument is weighted \(L^2\), and the
cutoff derivatives of the TT adjoint kernel decay with the same weight.

The signed kernel pairing is
\(-\pi\|B\|_2^2/8\), with no pointwise bound on the TT projection needed.
The bilinear \(H^2_w\times H^2_w\) bound follows directly from
Cauchy--Schwarz against \(|Q|dV\). Thus the complete positive error is
\[
C\{\varepsilon^2a+a\eta+\eta^2
       +(\varepsilon+\beta)a^2+a^3\},\qquad
\eta=\delta+\varepsilon^2+\varepsilon a+a^2.
\]
For \(a=o(\varepsilon)\), \(\delta=O(\varepsilon^3)\), every term is
\(o(\varepsilon^3)\). For \(a\le c_*\varepsilon\) the normalized error
is \(O(c_*+c_*^2+c_*^3)+O(\varepsilon)\), so choosing one small
\(c_*\) gives a uniform positive lower bound. The coefficient in the
little-o case is correctly
\[
\frac{1/(2\pi^2)}{8\pi^2(p-1)}
 =\frac1{16\pi^4(p-1)}.
\]
Finally an exact metric in this ball has
\(\lambda=-1+O(a+\varepsilon^2)\); constant rescaling changes its
distance by at most \(C(a+\varepsilon^2)\). The all-sign local exclusion
therefore follows after shrinking the radius, but not for arbitrary
large multiples of \(\varepsilon\), all \(o(1)\) corrections, or distant
Einstein metrics.

The independent rerun of round6_construction_check.py passed all six
finite-collar, gauge-variation, asymptotic-order and coefficient checks.
Those algebra checks complement, but do not replace, the analytic domain
and geometric-comparison arguments reviewed above.
