# Einstein spectral pinching: automatic amplitude and a monopole consequence

23 September 2026. Conventions: nonnegative scalar Laplacian,
Hilbert--Schmidt norm on the Weyl endomorphism, and exterior norm on forms.
This note supplies two applications of the harmonic-Weyl selection theorem.
The maximum-principle calculation is elementary; no independent priority is
claimed for that calculation. The quantitative topological consequence uses
the accompanying selection estimate, with its complete hypotheses.

## 1. An upper amplitude supplied by the equation

Let \((M,g)\) be a closed oriented Einstein four-manifold with
\(\operatorname{Ric}=-g\). Write the ordered eigenvalues of \(W^+\) as
\(\lambda_1<\lambda_2\le\lambda_3\), and put
\[
 t=-\frac34\lambda_1>0,\qquad b=\lambda_3-\lambda_2,\qquad
 \theta=\frac{b}{4t}.
\tag{1}
\]
The lowest eigenvalue is assumed simple everywhere. The function \(t\)
is smooth, while \(b\) need only be continuous at an upper-eigenvalue
collision. Its square is smooth. Trace-freeness gives
\[
 (\lambda_1,\lambda_2,\lambda_3)
 =\left(-\frac{4t}{3},\frac{2t}{3}-\frac b2,
                         \frac{2t}{3}+\frac b2\right),
 \quad |W^+|^2=\frac83t^2+\frac12b^2.
\tag{2}
\]
In particular, simplicity of the lowest eigenvalue is equivalent to
\(\theta<1\).

**Lemma 1.** If \(\theta\le\theta_0<1/\sqrt3\), then
\[
 \boxed{t\le M_{\theta_0}:=\frac{1}{2(1-3\theta_0^2)}.}
\tag{3}
\]
There is no separate upper Weyl-curvature hypothesis.

To prove this, use the Einstein Weyl equation
\[
 \nabla^*\nabla W^+=2W^++6(W^+)^2-2|W^+|^2I.
\tag{4}
\]
For a smooth simple eigenvalue of a self-adjoint bundle section, the
second derivative formula, with the nonnegative Laplacian convention, is
\[
 \Delta\lambda_1
 =\langle(\nabla^*\nabla W^+)e_1,e_1\rangle
 -2\sum_{j=2}^3\frac{|\langle\nabla W^+e_1,e_j\rangle|^2}
                          {\lambda_1-\lambda_j}.
\tag{5}
\]
An orthonormal eigenbasis at the point suffices; the two upper eigenvalues
need not be locally simple. Since each denominator is negative, (2)--(5)
imply
\[
 \Delta t\le 2t-4t^2+\frac34b^2
            \le2t-4(1-3\theta_0^2)t^2.
\tag{6}
\]
At a maximum of \(t\), one has \(\Delta t\ge0\). Equation (3) follows.
The conclusion is only an upper bound: this argument does not provide a
uniform positive lower bound for \(t\) over a family of manifolds.

## 2. A derivative-free structure estimate

Assume in addition \(t\ge m>0\), with a prescribed lower bound.
Let \(\omega\) be the normalized lowest eigenform, \(|\omega|^2=2\),
on the orientation cover of its real eigenline. The cover has degree at
most two. Normalized integrals are unchanged under this cover. The
[harmonic-Weyl selection theorem](line1_signed_harmonic_weyl.md),
applied using (3), gives
\[
 \boxed{\fint\left(|dt|^2+(t-\tfrac12)^2+|\nabla\omega|^2\right)
       \le C_{m,\theta_0}\fint b^2.}
\tag{7}
\]
Here the Einstein equation supplies harmonicity of \(W^+\) and \(s=-4\).
No assumed Hessian budget, Ricci derivative estimate, Sobolev constant,
injectivity radius, scalar spectral gap, diameter, or \(W^-\) bound is
present. The lower amplitude and relative spectral pinching are genuine
assumptions. This is an integral structure estimate, not a theorem
constructing a nearby Kähler metric.

## 3. Topology forces a definite upper-eigenvalue splitting

Suppose that the given metric admits an actual polarized monopole class
with \(p=(a_g^+)^2\ge A>0\). This can be the metricwise class on the
blow-up/handle families of the main integral theorem; no globally fixed
class working for all polarizations is being presumed. Put
\[
 T=2\chi(M)+3\tau(M),\qquad h=1-T/A,
 \quad 0<h<1.
\tag{8}
\]

**Corollary 2.** Under the hypotheses of Section 2 and (8),
\[
 \boxed{\fint_M(\lambda_3-\lambda_2)^2\ge c_{m,\theta_0}h^2.}
\tag{9}
\]
It applies to every normalized negative Einstein metric meeting these
spectral assumptions, not merely to a selected construction.

Indeed, the scalar monopole estimate and \(s=-4\) give
\[
 16V\ge32\pi^2p\ge32\pi^2A.
\tag{10}
\]
For an Einstein metric, Chern--Weil gives
\[
 2\pi^2T/V=\frac13+\fint|W^+|^2.
\tag{11}
\]
Since \(T=A(1-h)>0\), (10)--(11) imply
\[
 \fint|W^+|^2\le\frac23-h.
\tag{12}
\]
Combining (2) and (12), and discarding only nonpositive terms, yields
\[
 h\le\frac83\left(\frac14-\fint t^2\right)-\frac12\fint b^2
   \le\frac83(M_{\theta_0}+\tfrac12)
                  \left(\fint(t-\tfrac12)^2\right)^{1/2}.
\tag{13}
\]
Use (7) and square this inequality. This proves (9), with, for example,
\(c_{m,\theta_0}=[\frac83(M_{\theta_0}+\frac12)]^{-2}
C_{m,\theta_0}^{-1}\), where the latter constant is the one in (7).

On
\(M=X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3)\),
\(A=c_1^2(X)>0\), the parameter is \(h=(k+4\ell)/A\).
Thus the inequality detects a required spectral departure from the
negative Kähler--Einstein curvature pattern on this actual family.
It does not exclude metrics with a lowest-eigenvalue collision, very
small lower amplitude, or failure of the displayed pinching. Consequently
this corollary alone is not an unconditional Einstein nonexistence result.
The separate two-chirality theorem supplies the new unconditional
topological application in this research package.

## 4. Sources and what is being added

The Einstein Weyl equation is classical; see Derdziński,
[Self-dual Kähler manifolds and Einstein manifolds of dimension four](https://www.numdam.org/article/CM_1983__49_3_405_0.pdf),
and the formulas recalled in Catino--Dameno,
[Conformal Kähler rigidity of Einstein four-manifolds](https://arxiv.org/abs/2607.21538).
The latter paper's largest-simple-eigenvalue classification must not be
replaced by a lowest-simple-eigenvalue classification: the negative
Kähler--Einstein model has a simple lowest eigenvalue and a double largest
one. The accompanying harmonic-Weyl proof derives the signed balance for
this different branch.

The scalar monopole estimate is the classical input of
[LeBrun, Ricci curvature, minimal volumes, and Seiberg--Witten theory](https://arxiv.org/abs/math/0003068).
Equations (10)--(12) are classical consequences. The present quantitative
application is their composition with (7); it is not a new proof of the
classical inequalities or a complete spectral classification of Einstein
four-manifolds.
