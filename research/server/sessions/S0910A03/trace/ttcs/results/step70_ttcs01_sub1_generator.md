# TTCS Independent Branch Record

```json
{
  "step_id": 70,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step70_mixed_boundary_formulation.md",
    "Sessions/S0910A03/workspace/notes/step69_anisotropic_cusp_compensation.md",
    "Sessions/S0910A03/workspace/notes/step67_corrections_and_analytic_neck_reopening.md"
  ]
}
```

## Task

The research asks whether a T²-invariant Einstein half-core exists: a Riemannian 4-metric on [0,R]×T³ with Ric=-3g, totally geodesic at t=0 (shape operator S=0) with prescribed Koiso center metric q on T³ (scalar curvature -6), and approaching an expanding cusp state at t=R. The T²-invariant Gaussian-gauge system is b_tt - e^{-2a}b_θθ = lower order, which is WAVE-like (hyperbolic), not elliptic. The central obstruction is: every scalar-minus-six T³ metric has S'(0) = Ric_q♯+3I with a negative eigenvalue (from Preissmann/sectional curvature). Numerical Cauchy evolution for all tested conformal seeds shows H reversal before reaching the expanding regime. Li-Liu's exact PE-to-AH-cusp Einstein metrics on (0,∞)×T³ demonstrate global compensation exists without reflection symmetry, using the Toda equation. QUESTION: (1) Characterize when a T²-invariant reflection-symmetric Einstein half-core exists: what conditions on the center metric q guarantee that the exact analytic continuation reaches an expanding cusp state rather than developing a singularity? (2) For the approximate problem, if we allow Einstein defect ||Ric+3g||≤δ, can a smooth core be constructed over a domain of length R~log(1/δ) connecting Koiso center to cusp? (3) Is there a deformation of the Li-Liu ASD Toda solution that breaks W⁺=0 while acquiring a nearly-geodesic T³ slice?

## Output

### 1. The reduced equations have elliptic Cauchy behavior, not wave behavior

The displayed formula for \(\hat E_{22}\) has principal part
\[
-b_{tt}-e^{-2a}b_{\theta\theta}.
\]
Thus \(\hat E_{22}=0\) gives
\[
b_{tt}+e^{-2a}b_{\theta\theta}=\text{lower-order terms}.
\]
For a Fourier mode \(e^{ik\theta}\), this becomes
\[
\widehat b_k''-k^2e^{-2a}\widehat b_k=\cdots,
\]
which has exponentially growing and decaying solutions. The same applies to \(c\). The missing \(a_{\theta\theta}\) term reflects residual coordinate freedom in Gaussian gauge; the full Einstein–DeTurck system is elliptic.

Consequently:

* The Koiso data \((q,S=0)\) form an elliptic Cauchy problem: analytic uniqueness holds, but high Fourier modes can grow exponentially.
* Prescribing values at both \(t=0\) and \(t=R\) is an elliptic endpoint problem, not a fixed-endpoint string problem.
* Doubling a Dirichlet solution does not automatically produce reflection symmetry. Smooth doubling requires \(S(0)=0\), equivalently the normal derivative of the tangential metric must vanish.
* The observed Fourier stiffness near \(t\approx0.45\) is consistent with elliptic Cauchy amplification.

There is also a small strengthening of the initial-acceleration observation. Preissmann alone gives a plane with \(K\ge0\), hence an eigenvalue of \(\operatorname{Ric}_q^\sharp+3I\) that is \(\le0\). Strict inequality somewhere follows from the flat torus theorem: if \(K\le0\) everywhere on \(T^3\), the cocompact \(\mathbb Z^3\)-action forces flatness, contradicting \(R_q=-6\). Hence some plane has \(K>0\), and the complementary acceleration eigenvalue is \(<0\).

---

## 2. Exact normalized evolution gives a sharp characterization at an expanding end

Write
\[
g=dt^2+\gamma_t,\qquad
S=\frac12\gamma_t^{-1}\dot\gamma_t,\qquad H=\operatorname{tr}S,
\]
and normalize by the expanding cusp scale:
\[
h_t=e^{-2t}\gamma_t,\qquad
B=S-I=\frac12h_t^{-1}\dot h_t,\qquad b=\operatorname{tr}B=H-3.
\]
For \(\operatorname{Ric}_g=-3g\), the equations become
\[
\dot h=2hB,
\]
\[
\dot b+2b+|B|^2=0,
\tag{2.1}
\]
\[
\operatorname{div}_{h}B-db=0,
\tag{2.2}
\]
\[
\dot B=e^{-2t}\operatorname{Ric}_{h}^{\sharp}
-bI-3B-bB,
\tag{2.3}
\]
and
\[
e^{-2t}R_h-4b-b^2+|B|^2=0.
\tag{2.4}
\]
At a totally geodesic center,
\[
B(0)=-I,\qquad b(0)=-3.
\]
Equation (2.1) integrates pointwise to
\[
e^{2t}b(t,\theta)
=
-3-\int_0^t e^{2s}|B(s,\theta)|^2\,ds.
\tag{2.5}
\]

This identity supplies several strong conclusions.

### 2.1 An exact flat cusp jet cannot occur at finite \(R\)

A flat expanding cusp has \(B=0\), hence \(b=0\). But (2.5) gives
\[
b(t,\theta)<0
\]
for every finite \(t\). More quantitatively,
\[
3-H=-b\ge 3e^{-2t},
\qquad
|B|\ge \frac{|b|}{\sqrt3}\ge \sqrt3\,e^{-2t}.
\tag{2.6}
\]
Thus no scalar-minus-six center metric \(q\) reaches exact flat-cusp Cauchy data at finite distance. This also follows from analytic uniqueness: exact \((\gamma,S)=(e^{2R}h_{\rm flat},I)\) would continue backward as the pure cusp and could not have \(S(0)=0\).

### 2.2 A smooth flat conformal infinity is also impossible

Suppose the continuation exists for all \(t\) and is smoothly conformally compact:
\[
h_t=h_0+e^{-2t}h_2+e^{-3t}h_3+\cdots .
\]
For a four-dimensional Poincaré–Einstein metric,
\[
h_2=-P_{h_0},\qquad
\operatorname{tr}_{h_0}P_{h_0}=\frac14R_{h_0},
\]
so
\[
b=e^{-2t}\frac14R_{h_0}+O(e^{-3t}).
\]
Taking \(t\to\infty\) in (2.5) yields the pointwise scattering identity
\[
\boxed{
\frac14R_{h_0}(\theta)
=
-3-\int_0^\infty e^{2s}|B(s,\theta)|^2\,ds .
}
\tag{2.7}
\]
Hence
\[
R_{h_0}(\theta)<-12
\]
at every point, since \(B(0)=-I\). In particular, a flat conformal infinity cannot arise.

The signs can be tested on the Fuchsian model
\[
g=dt^2+\cosh^2t\,q,\qquad K_q=-1.
\]
Here \(h_0=q/4\), so \(R_{h_0}=-24\), exactly consistent with (2.7).

Therefore, for the flat expanding state posed in the question, the exact reflection-symmetric stable set is empty. Reflection-symmetric Einstein ends with a general conformal infinity remain conceivable only when the center-normalized representative at infinity has scalar curvature strictly below \(-12\) pointwise and satisfies the full tensor equations (2.2)–(2.4).

### 2.3 General characterization of successful center metrics

For an analytic \(T^2\)-invariant \(q\) with \(R_q=-6\), let \((h_q(t),B_q(t))\) be its unique maximal Koiso continuation with
\[
(h_q(0),B_q(0))=(q,-I).
\]
A continuation to a general expanding Poincaré–Einstein end is equivalent to:

1. positive definiteness and regular curvature on every finite interval;
2. convergence \(h_q(t)\to h_0\) in the smooth conformal compactification topology;
3. the Fefferman–Graham decay of \(B_q\);
4. equations (2.2)–(2.4), including the pointwise identity (2.7).

This represents the desired metrics as the intersection of the Koiso initial-data manifold
\[
\{(q,-I):R_q=-6\}
\]
with the stable manifold of the Poincaré–Einstein end system. It is intrinsically nonlocal; the sign pattern of \(S'(0)\) alone cannot determine membership. For flat \(h_0\), the intersection is empty by (2.7).

---

## 3. The approximate equation forces the logarithmic length scale

Let
\[
E=\operatorname{Ric}_g+3g,\qquad \|E\|_{\mathrm{op}}\le\delta.
\]
The normal equation becomes
\[
\dot b+2b+|B|^2=-E_{00},
\]
hence
\[
e^{2R}b(R)
=
-3-\int_0^R e^{2s}|B|^2\,ds
-\int_0^R e^{2s}E_{00}\,ds.
\tag{3.1}
\]
If the terminal shape is exactly cuspidal, \(b(R)=0\), then
\[
3+\int_0^R e^{2s}|B|^2\,ds
=
-\int_0^R e^{2s}E_{00}\,ds
\le \frac{\delta}{2}(e^{2R}-1).
\tag{3.2}
\]
Therefore
\[
\boxed{
R\ge \frac12\log\!\left(1+\frac6\delta\right).
}
\tag{3.3}
\]
The weighted shear gives the stronger relation
\[
R\ge
\frac12\log\!\left(
1+\frac{2}{\delta}
\left[
3+\int_0^R e^{2s}|B|^2\,ds
\right]\right).
\tag{3.4}
\]

Thus \(R\asymp\log(1/\delta)\) is the correct scale, with leading coefficient at least \(1/2\). The defect must also have a coherent sign in the normal channel:
\[
-E_{00}
\]
must compensate both the initial value \(b(0)=-3\) and the entire weighted shear energy.

For an approximately cuspidal endpoint with \(|B(R)|\le\eta\), (3.1) yields
\[
3+\int_0^R e^{2s}|B|^2\,ds
\le
\sqrt3\,\eta e^{2R}
+\frac{\delta}{2}(e^{2R}-1).
\tag{3.5}
\]
When \(\eta=O(\delta)\), the same logarithmic scale persists.

### 3.1 The terminal flat warped layer is feasible

On a flat-slice tail
\[
g=dt^2+f(t)^2h_{\rm flat},\qquad
\frac{f'}f=1+\beta,
\]
the two independent residuals are
\[
E_{00}=-3\beta'-6\beta-3\beta^2,
\]
\[
E_{\mathrm{tan}}=-\beta'-6\beta-3\beta^2.
\]
If \(\beta=O(\delta)\) and \(\beta'=O(\delta)\), then the full defect is \(O(\delta)\), and \(\beta\) can be brought to zero over an interval of fixed length. Hence the final smoothing layer is not the main analytic difficulty.

The missing object is a trajectory from the prescribed Koiso center into a state satisfying
\[
\|h_T-h_{\rm flat}\|_{C^{2,\alpha}}
+\|B_T\|_{C^{1,\alpha}}
=O(\delta),
\qquad
T=\frac12\log(1/\delta)+O(1).
\tag{3.6}
\]

### 3.2 What elliptic amplification can and cannot supply

Linearization of the Gaussian equations gives Fourier equations of the form
\[
u_k''-k^2e^{-2a(t,\theta)}u_k+\cdots=F_k.
\tag{3.7}
\]
A source of size \(\delta\) can create an order-one endpoint response only when
\[
\int_0^R |k|e^{-a(t)}\,dt
\]
is comparable to \(\log(1/\delta)\). In an ordinary expanding cusp, \(a\sim t\), so this integral stays bounded for fixed \(k\). Therefore a long cusp tail does not itself amplify fixed spatial modes enough to repair an order-one tensor mismatch.

Three mathematically distinct mechanisms remain:

* a family of center metrics whose exact continuations shadow the cusp stable manifold for increasingly long times;
* a long region in which the physical \(\theta\)-wavenumber \(ke^{-a}\) remains bounded away from zero, allowing elliptic Cauchy amplification;
* Fourier frequencies depending on \(\delta\), accompanied by uniform control of curvature and nonlinear mode coupling.

The endpoint response is encoded by the smallest singular values of the linearized Einstein–DeTurck end-to-interior map. Exponential decay
\[
\sigma_{\min}(R)\sim e^{-\kappa R}
\]
together with a transverse projection of the Koiso-to-cusp mismatch would produce the logarithmic steering mechanism. Near the standard cusp, the trace and shear modes instead decay forward at rates \(2\) and \(3\), so a small source there changes \(B\) only by \(O(\delta)\).

The normal identity therefore validates the logarithmic scale but does not alone construct the core. A smooth \(O(\delta)\) core requires a genuine tensor steering mechanism before the final warped tail.

---

## 4. Li–Liu deformation: infinitesimal ASD breaking is too small

There is first an algebraic issue in the supplied notes. The two equations
\[
(e^v)_{\xi\xi}+\Delta v=0
\quad\text{and}\quad
(e^v)_{\xi\xi}+\Delta(e^v)=0
\]
are not equivalent. Under \(v=v(\xi,\theta)\), the first becomes
\[
(e^v)_{\xi\xi}+v_{\theta\theta}=0,
\]
which remains nonlinear. The exact Li–Liu convention and the \(\xi\)-dependence of \(\eta\) are needed before harmonic-function methods can be used.

### 4.1 Coordinate \(\xi\)-levels are uniformly far from geodesic

For
\[
g=\xi^{-2}\bigl(W\,d\xi^2+W^{-1}\eta^2+We^v g_{T^2}\bigr),
\qquad W>0,
\]
set
\[
p=\frac{\xi W_\xi}{2W},
\qquad
\frac{\xi v_\xi}{2}=1-W.
\]
Ignoring off-diagonal terms from \(\partial_\xi\eta\), which only increase the norm, the principal shape eigenvalues of a \(\xi\)-level are
\[
s_\eta=-\frac{1+p}{\sqrt W},
\qquad
s_1=s_2=\frac{p-W}{\sqrt W}.
\]
Thus
\[
|S|^2
\ge
\frac{(1+p)^2+2(p-W)^2}{W}.
\]
Minimizing first in \(p\) and then in \(W>0\) gives
\[
\boxed{|S|^2\ge \frac83.}
\tag{4.1}
\]
Hence no coordinate level is even close to totally geodesic in Einstein units. A sufficiently small \(C^1\) perturbation of the Li–Liu metric cannot change this.

A tilted graph \(\xi=\phi(x)\) can contribute a Hessian term to its shape tensor, so it is the only local possibility within a small metric perturbation. Its linearized shape equation has the form
\[
D S(k,\phi)
=
D_gS[k]
-\nabla^2\phi
-\phi\bigl(R_{\nu i\nu j}+S_i{}^mS_{mj}\bigr).
\tag{4.2}
\]
The components of \(S\) orthogonal to the image of this Hessian-plus-potential operator cannot be removed by tilting. In \(T^2\)-invariant Fourier variables this becomes a concrete modewise projection problem.

### 4.2 Gauss–Codazzi forces order-one breaking of \(W^+=0\)

For any hypersurface \(\Sigma^3\subset(M^4,g)\) with \(\operatorname{Ric}_g=-3g\),
\[
W_{\nu ijk}
=
\nabla_jS_{ik}-\nabla_kS_{ij},
\tag{4.3}
\]
and
\[
K_\Sigma(e_i,e_j)
=
-1+W_{ijij}
+\det\bigl(S|_{\operatorname{span}(e_i,e_j)}\bigr).
\tag{4.4}
\]
When \(W^+=0\), four-dimensional Hodge algebra determines the tangential Weyl components from the mixed components in (4.3). More generally,
\[
|W_{\mathrm{tan}}|
\le C\bigl(|W^+|+|\nabla S|\bigr).
\]
If \(\Sigma=T^3\), Preissmann gives a point and plane with \(K_\Sigma\ge0\). Equation (4.4) then implies
\[
\boxed{
1\le
C\left(
|W^+|+|\nabla S|+|S|^2
\right)
}
\tag{4.5}
\]
somewhere on \(\Sigma\).

Consequences:

* An ASD Einstein metric cannot contain a totally geodesic \(T^3\).
* Any exact totally geodesic \(T^3\) in an Einstein deformation must have \(\sup_\Sigma|W^+|\ge c_0>0\).
* A family with \(W^+\to0\) and \(S\to0\) in \(C^1\), while retaining bounded geometry, cannot exist.
* A deformation with only \(C^0\)-small \(S\) could evade (4.5) through order-one tangential derivatives of \(S\), but such oscillation would enter any reflection smoothing estimate.

Thus the required Li–Liu deformation is not infinitesimal in the ASD-breaking direction. It must either move a finite distance in Einstein moduli, produce a strongly tilted slice, or develop rapid variation/collapse on the slice.

### 4.3 The appropriate deformation representation

In Bianchi gauge, an infinitesimal Einstein deformation \(k\) solves
\[
D\!\left(\operatorname{Ric}+3g+\delta^*\beta\right)_g k=0
\tag{4.6}
\]
in weighted spaces adapted simultaneously to the PE end and the AH cusp end. The slice problem couples (4.6) to
\[
S+D_gS[k]
-\nabla^2\phi
-\phi(R_{\nu i\nu j}+S_i{}^mS_{mj})
\approx0.
\tag{4.7}
\]
The substantive questions are:

* the kernel and cokernel of (4.6) for the mixed PE–cusp geometry;
* whether conformal-infinity variations generate modes with \(DW^+(k)\ne0\);
* whether the resulting end-to-slice map reaches the tensor components in (4.7);
* whether continuation to finite amplitude preserves completeness and the cusp asymptotics.

The relevant source families are the exact Li–Liu Type-I equation, weighted Lichnerowicz theory on PE metrics with cusp ends, Graham–Lee/Biquard deformation theory, and Witten–Yau–Cai–Galloway conformal-infinity connectedness.

---

## Main mathematical conclusions

1. The supplied \(T^2\)-invariant equations have elliptic Cauchy behavior. The wave interpretation and fixed-endpoint string analogy do not apply.
2. For every exact reflection center,
   \[
   e^{2t}(H-3)
   =
   -3-\int_0^t e^{2s}|S-I|^2\,ds.
   \]
   Hence exact flat cusp data cannot occur at finite distance.
3. If the exact continuation has a smooth conformal infinity \(h_0\), then
   \[
   R_{h_0}
   =
   -12-4\int_0^\infty e^{2s}|S-I|^2\,ds<-12.
   \]
   A flat expanding end is therefore impossible for every center metric \(q\).
4. With defect at most \(\delta\), exact cusp shape at \(R\) requires
   \[
   R\ge \frac12\log(1+6/\delta),
   \]
   with a stronger constant determined by weighted shear. This explains precisely why a logarithmic collar is the minimal plausible scale.
5. Li–Liu coordinate levels satisfy \(|S|^2\ge8/3\). Moreover a \(T^3\) slice obeys the order-one relation
   \[
   1\lesssim |W^+|+|\nabla S|+|S|^2.
   \]
   Acquiring a \(C^1\)-nearly-geodesic torus therefore requires finite, not infinitesimal, departure from the ASD sector.