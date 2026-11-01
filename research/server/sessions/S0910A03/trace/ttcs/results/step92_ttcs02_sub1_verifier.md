# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step92_constrained_spike_koiso.py",
    "Sessions/S0910A03/workspace/data/step92_constrained_spike_koiso.json",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md",
    "Knowledge/objects/papers/1106.2066-The-Cauchy-problems-for-Einstein-metrics-and-parallel-spinors--e588543ba837--cf493e3a7afe/object.md"
  ]
}
```

## Task

Verify a proposed exact family of analytic stable minimal T^3 Cauchy data for local Ric=-3g germs. Let P(s)>0 be analytic periodic on a circle. Choose a closed immersed curve U:S^1->H^2 with |U_s|^2=12+2P(s), and set q=ds^2+M(U(s))_{ab}dx^a dx^b with det M=1. Let A=(1/2)M^{-1}M_s. Choose a target unit normal N(s) perpendicular to U_s, let C_N=M^{-1}dM(N), and define a vertical tracefree Weingarten endomorphism B=sqrt(P/2) C_N, with W(T)=0 and W|vertical=B. Check carefully, in the normalization e_s=(1/2)tr[(M^{-1}M_s)^2], that: Scal_q=-e_s/2; tr W=0; tr W^2=P; the momentum constraint d tr W+delta W=0 is exactly tr(A B)=0 (and all other components vanish by T^2 invariance); the Hamiltonian constraint Scal_q+tr W^2-(tr W)^2=-6 holds; |II|^2=P and e_nu=2P; invariant stability is equivalent to -d_s^2+3-P>=0. If P is a sufficiently narrow analytic von Mises bump of fixed mass m<2sqrt(3)tanh(sqrt(3)L/2), does the stability hold for large concentration, and does Koiso's analytic theorem then yield a genuine local analytic Einstein germ with arbitrarily large e_nu on the center? Identify any hidden error: target-to-matrix normalization, momentum divergence connection terms, global closed curve/normal, analyticity, sign of W, or distinction between invariant and full stability. Explain exactly what this would establish for the connector route and what it would not.

## Output

# Scientific verification memo

## Summary

With the target metric normalized by  
\[
\langle X,Y\rangle_{\mathbb H^2}
=\frac12\operatorname{tr}(C_XC_Y),
\qquad C_X=M^{-1}dM(X),
\]
the proposed Cauchy data satisfy the Einstein constraints exactly. Koiso’s analytic theorem therefore produces, for every fixed analytic \(P>0\), a genuine local analytic metric with
\[
\operatorname{Ric}_{g^{(4)}}=-3g^{(4)}
\]
and central hypersurface \((T^3,q,W)\).

There are three important refinements:

1. Under Koiso’s sign convention, \(U_\nu=-\sqrt{2P}\,N\), rather than \(+\sqrt{2P}\,N\); its energy is still \(e_\nu=2P\).
2. For this particular block metric, positivity of \(-\partial_s^2+3-P\) implies stability against all normal variations, not merely \(T^2\)-invariant ones.
3. The spike in \(e_\nu\) is accompanied by a spike in \(e_s\) and by
   \(\operatorname{Scal}_q=-6-P\to-\infty\) at the peak.

## 1. Target-to-matrix normalization and closed curve

Let
\[
\mathcal P=\{M=M^T>0:\det M=1\}.
\]
For example,
\[
M(\alpha,\beta)=
\begin{pmatrix}
e^\alpha+\beta^2e^{-\alpha}&\beta e^{-\alpha}\\
\beta e^{-\alpha}&e^{-\alpha}
\end{pmatrix}.
\]
Direct computation gives
\[
\frac12\operatorname{tr}\!\left[(M^{-1}dM)^2\right]
=d\alpha^2+e^{-2\alpha}d\beta^2,
\]
the hyperbolic metric of curvature \(-1\). Thus
\[
e_s=|U_s|^2
=\frac12\operatorname{tr}\!\left[(M^{-1}M_s)^2\right]
\]
has exactly the normalization used in the proposal.

A closed analytic immersed curve of any prescribed analytic speed
\[
v(s)=\sqrt{12+2P(s)}
\]
exists explicitly. Put
\[
\mathcal L=\int_0^L v(s)\,ds,\qquad
R=\operatorname{arsinh}\frac{\mathcal L}{2\pi},
\qquad
\theta(s)=\frac1{\sinh R}\int_0^s v(u)\,du.
\]
Then \(\theta(L)=2\pi\). Parameterizing a hyperbolic circle of radius \(R\) by \(\theta(s)\) gives a closed analytic \(U\) with \(|U_s|=v\). Since \(\mathbb H^2\) is oriented,
\[
N=J\frac{U_s}{|U_s|}
\]
is a global analytic periodic unit normal. There is therefore no normal-holonomy or closing obstruction.

Strict positivity of \(P\) ensures that \(\sqrt P\) is analytic globally on the circle.

## 2. Intrinsic scalar curvature

Write
\[
A=\frac12M^{-1}M_s.
\]
Because \(\det M=1\),
\[
\operatorname{tr}A=\frac12\partial_s\log\det M=0.
\]
For a metric \(q=ds^2+M(s)\) with flat torus fibers,
\[
\operatorname{Scal}_q
=-2(\operatorname{tr}A)_s-(\operatorname{tr}A)^2-\operatorname{tr}(A^2).
\]
Hence
\[
\operatorname{Scal}_q=-\operatorname{tr}(A^2).
\]
On the other hand,
\[
e_s=\frac12\operatorname{tr}[(2A)^2]
=2\operatorname{tr}(A^2),
\]
so
\[
\boxed{\operatorname{Scal}_q=-\frac12e_s.}
\]
With \(e_s=12+2P\),
\[
\operatorname{Scal}_q=-6-P.
\]

## 3. Algebra of \(W\)

For target unit \(N\),
\[
\operatorname{tr}C_N=0,
\qquad
\frac12\operatorname{tr}(C_N^2)=1.
\]
Thus, for
\[
B=\sqrt{\frac P2}\,C_N,
\]
one has
\[
\operatorname{tr}B=0,\qquad
\operatorname{tr}(B^2)
=\frac P2\operatorname{tr}(C_N^2)=P.
\]
Moreover,
\[
MB=\sqrt{\frac P2}\,dM(N)
\]
is symmetric, so \(B\) is self-adjoint for the vertical metric \(M\). Extending by \(W(\partial_s)=0\),
\[
\boxed{\operatorname{tr}W=0,\qquad |{\rm II}|^2=\operatorname{tr}(W^2)=P.}
\]

## 4. Momentum constraint and connection terms

The only Christoffel symbols involving the \(s\)-direction that enter are
\[
\Gamma^a_{sb}=A^a{}_b,\qquad
\Gamma^s_{ab}=-(MA)_{ab}.
\]
Using the supplied convention
\[
(\delta W)_j=-\nabla_iW^i{}_j,
\]
the \(s\)-component is
\[
\nabla_iW^i{}_s
=-\Gamma^k_{is}W^i{}_k
=-\operatorname{tr}(AB),
\]
and therefore
\[
(\delta W)(\partial_s)=\operatorname{tr}(AB).
\]
For vertical \(X\), all terms vanish because the coefficients are independent of \(x^a\) and \(W\) has no mixed components:
\[
(\delta W)(X)=0.
\]
No \(B_s\) term occurs: divergence differentiates the first tensor index, while \(W^s{}_j=0\).

Finally,
\[
\operatorname{tr}(AB)
=\sqrt{\frac P2}\,
\frac12\operatorname{tr}(C_{U_s}C_N)
=\sqrt{\frac P2}\,\langle U_s,N\rangle_{\mathbb H^2}=0.
\]
Since \(\operatorname{tr}W\equiv0\),
\[
\boxed{d\operatorname{tr}W+\delta W=0.}
\]

## 5. Hamiltonian constraint and normal orbit energy

For a three-dimensional hypersurface in a four-dimensional Einstein metric with Einstein constant \(\lambda=-3\), Koiso’s Hamiltonian equation is
\[
\operatorname{Scal}_q+\operatorname{tr}(W^2)-(\operatorname{tr}W)^2
=(3-1)\lambda=-6.
\]
Here,
\[
(-6-P)+P-0=-6,
\]
so it holds identically.

The supplied source uses
\[
g_t(WX,Y)=-\frac12\dot g_t(X,Y).
\]
Consequently the vertical matrix derivative at the center obeys
\[
M_\nu=-2MB,\qquad
C_{U_\nu}=M^{-1}M_\nu=-2B.
\]
Therefore
\[
C_{U_\nu}=-\sqrt{2P}\,C_N,
\qquad U_\nu=-\sqrt{2P}\,N,
\]
and
\[
\boxed{
e_\nu=\frac12\operatorname{tr}(C_{U_\nu}^2)
=2\operatorname{tr}(B^2)=2P.}
\]
Changing the convention for the Weingarten tensor reverses the direction of \(U_\nu\) but leaves \(e_\nu\) unchanged.

## 6. Stability

For a minimal hypersurface in \(\operatorname{Ric}=-3g\), the second-variation form is
\[
Q[f]
=\int_{T^3}\left(
|\nabla f|_q^2-
(\operatorname{Ric}(\nu,\nu)+|{\rm II}|^2)f^2
\right)d\mu_q.
\]
Since \(\operatorname{Ric}(\nu,\nu)=-3\), \(|{\rm II}|^2=P\), and
\(\det M=1\),
\[
Q[f]=\int_{T^3}\bigl(|\nabla f|^2+(3-P)f^2\bigr)\,ds\,dx.
\]
For \(T^2\)-invariant \(f=\phi(s)\),
\[
Q[\phi]\ge0
\quad\Longleftrightarrow\quad
-\partial_s^2+3-P\ge0
\]
on periodic functions.

In fact this is also equivalent to full stability. Expanding
\[
f(s,x)=\sum_{k\in\mathbb Z^2}y_k(s)e^{ik\cdot x}
\]
gives
\[
Q[f]
=\sum_k\int_0^L
\left(
|y_k'|^2+
\bigl[3-P+k^TM(s)^{-1}k\bigr]|y_k|^2
\right)ds.
\]
The additional term \(k^TM^{-1}k\) is \(\ge0\). Hence the \(k=0\) mode has the lowest quadratic form, and
\[
\boxed{\text{full stability}\iff
\text{\(T^2\)-invariant stability}\iff
-\partial_s^2+3-P\ge0.}
\]

## 7. Von Mises concentration

On a circle of length \(L\), set
\[
P_\kappa(s)=
\frac{m\,e^{\kappa\cos(2\pi s/L)}}{L I_0(\kappa)}.
\]
Then \(\int_0^LP_\kappa\,ds=m\), and \(P_\kappa ds\) converges to
\(m\delta_0\).

For
\[
H=-\partial_s^2+3,
\qquad
\mathfrak h[y]=\int_0^L(|y'|^2+3|y|^2)\,ds,
\]
the periodic Green kernel has
\[
G(0,0)=\frac1{2\sqrt3}
\coth\!\left(\frac{\sqrt3L}{2}\right).
\]
Thus the sharp evaluation inequality is
\[
|y(0)|^2\le G(0,0)\,\mathfrak h[y].
\]
The point-interaction form
\[
\mathfrak h[y]-m|y(0)|^2
\]
is \(>0\) whenever
\[
m<m_*:=\frac1{G(0,0)}
=2\sqrt3\tanh\!\left(\frac{\sqrt3L}{2}\right).
\]

The one-dimensional Sobolev modulus estimate yields, uniformly in \(y\),
\[
\int P_\kappa|y|^2
\le \bigl(mG(0,0)+\varepsilon_\kappa\bigr)\mathfrak h[y],
\qquad \varepsilon_\kappa\to0.
\]
Therefore, for every fixed \(m<m_*\),
\[
\int\left(|y'|^2+(3-P_\kappa)|y|^2\right)ds
\ge
\bigl(1-mG(0,0)-\varepsilon_\kappa\bigr)\mathfrak h[y]>0
\]
for all sufficiently large \(\kappa\).

At the same time,
\[
P_\kappa(0)
=\frac{m e^\kappa}{LI_0(\kappa)}
\sim\frac{m\sqrt{2\pi\kappa}}L,
\]
so
\[
\sup e_\nu=2\sup P_\kappa\longrightarrow\infty.
\]

For the supplied computation, \(L=2\pi\), \(m=1\), while
\[
m_*\approx3.464.
\]
The finite-difference value
\[
\lambda_0=2.7218156
\]
is consistent with the strict analytic estimate.

## 8. Koiso application

The supplied Ammann–Moroianu–Moroianu source, Theorem 2.1, states that analytic \(q\) and analytic symmetric \(W\) satisfying exactly the two equations above determine a unique analytic Einstein germ in Gaussian form. All hypotheses are met on the standard analytic \(T^3\). Hence for each \(\kappa\) there is some \(\varepsilon_\kappa>0\) and an analytic metric
\[
g^{(4)}=dt^2+q_t
\quad\text{on}\quad
(-\varepsilon_\kappa,\varepsilon_\kappa)\times T^3
\]
such that
\[
\operatorname{Ric}_{g^{(4)}}=-3g^{(4)},\qquad
q_0=q,\qquad W_0=W.
\]

Torus translations preserve the initial data; uniqueness makes the germ \(T^2\)-invariant. Simultaneous inversion \(x\mapsto-x\) also preserves the data and rules out base-orbit mixed terms, so the local germ remains block orthogonal.

No common positive lower value for \(\varepsilon_\kappa\) follows as \(\kappa\to\infty\).

## 9. Numerical artifact

The JSON residuals, including
\[
|\operatorname{tr}(AB)|<5\times10^{-14},\qquad
|\operatorname{tr}(B^2)-P|<8\times10^{-14},
\]
and Hamiltonian residual \(<3\times10^{-14}\), correctly support the matrix factors.

One small discretization inconsistency is visible: the script rescales the sampled `theta` but not `theta_prime`. Thus the sampled curve and declared derivative are not exactly related by finite differences, and `theta_total` differs from \(2\pi\) by about \(1.6\times10^{-10}\). The exact integral definition of \(\theta\) above removes this discrepancy; none of the analytic conclusions depends on that discretization.

## 10. Meaning for the connector construction

This family establishes that:

- exact Einstein hypersurface constraints, even together with full strict stability and ambient \(\operatorname{Ric}=-3g\), permit
  \[
  \sup_{T^3}e_\nu\to\infty;
  \]
- there is no universal separator-only pointwise estimate for \(e_\nu\) based solely on those equations;
- the concentration is compatible with all local Einstein equations, not merely with formal separator jets.

It does not produce:

- a complete two-ended connector or matching to prescribed end geometries;
- a concentration-independent collar width;
- a separator known to minimize globally in a primitive class, rather than merely being strictly stable;
- a closed ambient manifold relevant by itself to the full Yau 26 statement.

Also,
\[
e_s=12+2P,\qquad \operatorname{Scal}_q=-6-P
\]
spike simultaneously with \(e_\nu\). Thus the family does not address estimates that additionally assume pointwise control of the intrinsic separator geometry or of \(e_s\). The remaining mathematical distinction is therefore between separator-level stability and information propagated across a collar into the two prescribed ends.