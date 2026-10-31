# O11: direct descent tests at an exact critical metric

This attempt does not establish a new lower bound for \(\inf P\). It tests whether the additional exact criticality available in an ideal minimizing configuration supplies the missing descent direction. The calculations below are for a smooth **closed**, constant-negative-scalar, stable critical point of \(P=\int|\operatorname{Ric}^{\circ}|^2\). They must not be transferred to an incomplete regular orbifold domain without checking boundary terms and scalar constancy.

Write \(Z=\operatorname{Ric}^{\circ}\), \(q=|Z|^2\), \(s<0\), and \(L=-\Delta\ge0\), where \(\Delta=\operatorname{div}\nabla\). The curvature contraction convention is that the critical equation is

\[
\nabla^*\nabla Z-2\mathring R(Z)+\frac12qg=0.
\tag{1}
\]

This is Anderson's equation (4.35), with constant scalar curvature eliminating the divergence terms. Equation (1) is an exact critical equation, not a replacement for the manuscript's weak near-stationarity estimate.

## 1. An exact stability consequence without a geometric compactness hypothesis

Gauss–Bonnet gives

\[
P=2\int|W|^2+\frac1{12}\int s^2-16\pi^2\chi(M).
\]

For \(g_u=e^{2u}g\), conformal invariance of the Weyl integral and the scalar transformation formula give

\[
P(g_u)-P(g)
=-\int s\Delta u-\int s|du|^2
+3\int(\Delta u+|du|^2)^2.
\tag{2}
\]

Consequently the conformal Hessian at a constant-scalar metric is

\[
\operatorname{Hess}_P(2ug,2ug)
=\langle u,(6L^2-2sL)u\rangle.
\tag{3}
\]

Since \(\delta Z=0\) and \(\operatorname{tr}Z=0\), the scalar variation in direction \(h=Z\) is

\[
s'[Z]=-q.
\]

Differentiating the conformal first variation \(-\int u\Delta s\) gives the mixed Hessian

\[
\operatorname{Hess}_P(Z,2ug)=-\langle u,Lq\rangle.
\tag{4}
\]

At a critical metric this Hessian does not depend on the second-order choice of a two-parameter metric path. Stability applied to \(Z+2ug\), followed by minimization over \(u\), therefore yields

\[
\boxed{
\operatorname{Hess}_P(Z,Z)
\ge\langle q,L(6L-2s)^{-1}q\rangle.
}
\tag{5}
\]

The inverse \((6L-2s)^{-1}\) exists because \(s<0\); constants are annihilated by the preceding \(L\). No lower bound for the first nonzero Laplace eigenvalue, Sobolev constant, or injectivity radius was used.

Formula (5) is a real constraint on an exact stable critical metric. It has the wrong structure for the proposed contradiction: it is a lower bound for a nonnegative Hessian, not a forced negative direction. On a Laplace eigenfunction of eigenvalue \(\lambda\), its multiplier is \(\lambda/(6\lambda-2s)\), which can tend to zero as \(\lambda\to0\). Thus it neither bounds the value of \(P\) nor forces a uniform amount of instability from \(P/A\to0\).

## 2. The normalized Ricci direction has a stronger cancellation than global stationarity

Consider normalized Ricci flow at time zero, with

\[
\dot g=-2Z.
\]

At the constant-scalar initial metric, the scalar evolution is \(\dot s=2q\). In endomorphism notation, the trace-free Ricci evolution is

\[
\frac{d}{dt}Z^{\sharp}
=\Delta Z^{\sharp}+2\mathring R(Z)^{\sharp}-\frac12qI.
\tag{6}
\]

Equation (1) makes the right side of (6) vanish. Hence

\[
\boxed{\dot Z^{\sharp}=0,\qquad \dot q=0,\qquad \dot{dV}=0}
\tag{7}
\]

pointwise at time zero. Thus this natural candidate descent does not merely have a vanishing integrated first variation; the eigenvalues of the trace-free Ricci endomorphism themselves have zero first derivative. Lowering the scalar-square energy along this direction does not lower \(P\) at first order.

The exact scalar derivative is

\[
\frac d{dt}\int s^2=4sP<0.
\]

Consequently \(\int|\operatorname{Ric}|^2=P+\frac14\int s^2\) initially decreases. This does not contradict its known sharp infimum: the assumed \(P\)-minimizer may have a positive scalar-square excess, and no supplied estimate makes its Ricci-square value equal to the classical minimum.

## 3. The remaining term is concentration, not the background sign

Taking the pointwise norm in (1) yields

\[
\frac12\Delta q=|\nabla Z|^2-2\operatorname{Rm}(Z,Z).
\]

Multiplication by \(q\) and integration therefore gives

\[
\boxed{
\int q|\nabla Z|^2+\frac12\int|dq|^2
=2\int q\operatorname{Rm}(Z,Z).
}
\tag{8}
\]

The potentially uncontrolled part contains

\[
\int |Z|^2 W_{ikjl}Z^{ij}Z^{kl}.
\tag{9}
\]

Neither \(\int|Z|^2=O(Q)\) nor the total curvature budget \(\int|\operatorname{Rm}_{\rm op}|^2=O(A)\) controls (9). Direct Hölder would require an \(L^8\) bound on \(Z\). Even the unweighted critical identity requires \(L^4\) control of \(Z\) to estimate its Weyl pairing. These norms are not supplied by small average \(P/A\), and no uniform Sobolev estimate is available in the original hypotheses.

This is precisely where the attempted criticality/stability descent stops. Formula (5) does not remove (9): it places a positive constraint on the Hessian and allows that constraint to be paid by the same concentrated curvature. No sign of (9), no controlled \(L^8\) norm, and no quantitative transfer to the \(8\pi^2Q\) topological cost has been obtained here.

## 4. The literature does not supply the omitted implication

The relevant primary references are Anderson, *Canonical Metrics on 3-Manifolds and 4-Manifolds*, equation (4.35), <https://arxiv.org/pdf/math/0511034>, and Gursky–Viaclovsky, *Rigidity and Stability of Einstein Metrics for Quadratic Curvature Functionals*, <https://arxiv.org/pdf/1105.4648>. The latter develops local rigidity/stability at an Einstein background, with its stated spectral and neighborhood hypotheses. It does not turn \(P/A\ll1\) on an arbitrary varying topology into the required controlled neighborhood.

Also, the torsion-free group of the aspherical bulk does not make every ALE end Euclidean. A finite boundary group may be killed inside a resolving core, as occurs for Eguchi–Hanson. Therefore the attempted route “aspherical bulk implies trivial ALE groups, hence the AE tariff” has an invalid group-theoretic implication.

The calculations above retain both failures explicitly. They do not announce an O11 coefficient, a new competing closed metric, or a new global rigidity theorem.
