# TTCS Independent Branch Record

```json
{
  "step_id": 67,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step67_corrections_and_analytic_neck_reopening.md",
    "Knowledge/objects/papers/1106.2066-The-Cauchy-problems-for-Einstein-metrics-and-parallel-spinors--e588543ba837--cf493e3a7afe/object.md",
    "Sessions/S0910A03/workspace/notes/step63_graph_manifold_counterexample_analysis.md"
  ]
}
```

## Task

Verify the new Step 67 local curved-neck result in full mathematical detail. Check sign conventions, Koiso/Theorem 2.1 hypotheses, existence of an analytic constant-scalar-curvature -6 metric on T^3, the W=0 constraint for a four-dimensional Ric=-3g extension, the formula for g''(0), time-reflection symmetry, and H'(0)=3 under the opposite S convention. Identify any hidden issue that would invalidate the conclusion that an exact local negative-Einstein germ reverses mean curvature through a curved totally geodesic T^3. Also distinguish exactly what this refutes and what remains global. Ground every conclusion in the supplied source and note; do not assume a global extension.

## Output

I will verify each formula against the supplied source, including the dimension convention in the constraint equation and the existence/analyticity argument on \(T^3\).# Scientific verification memo

## 1. Sign conventions and Gaussian formulas

The supplied source, §2, uses
\[
g^Z=dt^2+g_t,\qquad \nu=\partial_t,
\]
and defines the Weingarten endomorphism by
\[
\nabla_X^Z\nu=-W_tX,\qquad
g_t(W_tX,Y)=-\frac12\dot g_t(X,Y).
\]
Thus, as an endomorphism,
\[
W_t=-\frac12g_t^{-1}\dot g_t.
\]

The Ricci formulas reproduced in Step 67 agree with source equations (2.3)–(2.5):
\[
\begin{aligned}
\operatorname{Ric}^Z(\nu,\nu)
 &=\operatorname{tr}(W_t^2)-\frac12\operatorname{tr}_{g_t}\ddot g_t,\\
\operatorname{Ric}^Z(\nu,X)
 &=d\operatorname{tr}W_t(X)+\delta^{g_t}W_t(X),\\
\operatorname{Ric}^Z(X,Y)
 &=\operatorname{Ric}^{g_t}(X,Y)+2g_t(W_tX,W_tY)\\
 &\quad+\frac12\operatorname{tr}(W_t)\dot g_t(X,Y)
 -\frac12\ddot g_t(X,Y).
\end{aligned}
\]

For a hypersurface of dimension \(m\) in an \((m+1)\)-manifold satisfying
\[
\operatorname{Ric}^Z=\lambda g^Z,
\]
the source constraints are
\[
d\operatorname{tr}W+\delta W=0,
\]
and
\[
\operatorname{Scal}^{g_0}
+\operatorname{tr}(W^2)-(\operatorname{tr}W)^2
=(m-1)\lambda.
\tag{1}
\]
Step 67 uses \(m=3\), so there is no dimension mismatch.

The normal evolution equation in Step 67 is also exactly source equation (2.11):
\[
\ddot g_t
=2\operatorname{Ric}^{g_t}
+\dot g_t\bigl(g_t^{-1}\dot g_t\,\cdot,\cdot\bigr)
-\operatorname{tr}(g_t^{-1}\dot g_t)\dot g_t
-2\lambda g_t.
\tag{2}
\]

---

## 2. An analytic metric on \(T^3\) with scalar curvature \(-6\)

The existence required by Step 67 can be made explicit before applying the Yamabe theorem.

On
\[
T^3=(\mathbb R/2\pi\mathbb Z)^3
\]
take a nonconstant analytic periodic function \(f(x)\), for example \(f(x)=a\sin x\), and set
\[
\bar g=dx^2+e^{2f(x)}dy^2+e^{-2f(x)}dz^2.
\]
For a doubly warped metric
\[
dx^2+A(x)^2dy^2+B(x)^2dz^2,
\]
the sectional curvatures of the three coordinate planes are
\[
K_{xy}=-\frac{A''}{A},\qquad
K_{xz}=-\frac{B''}{B},\qquad
K_{yz}=-\frac{A'B'}{AB}.
\]
With \(A=e^f\) and \(B=e^{-f}\), these become
\[
\begin{aligned}
K_{xy}&=-f''-(f')^2,\\
K_{xz}&=f''-(f')^2,\\
K_{yz}&=(f')^2.
\end{aligned}
\]
Hence
\[
\operatorname{Scal}_{\bar g}
=2(K_{xy}+K_{xz}+K_{yz})
=-2(f')^2.
\]
Moreover \(dv_{\bar g}=dx\,dy\,dz\), so
\[
\int_{T^3}\operatorname{Scal}_{\bar g}\,dv_{\bar g}
=-2\int_{T^3}(f')^2\,dx\,dy\,dz<0.
\]
Testing the three-dimensional Yamabe quotient with \(u\equiv1\),
\[
Q_{\bar g}(u)=
\frac{\int_{T^3}\bigl(8|\nabla u|^2+\operatorname{Scal}_{\bar g}u^2\bigr)\,dv_{\bar g}}
{\left(\int_{T^3}|u|^6\,dv_{\bar g}\right)^{1/3}},
\]
therefore gives
\[
Y(T^3,[\bar g])<0.
\]

The Yamabe existence result invoked in source Corollary 2.3 supplies a unit-volume metric
\[
\widehat g=u^4\bar g
\]
with constant scalar curvature
\[
\operatorname{Scal}_{\widehat g}=Y(T^3,[\bar g])=:Y<0.
\]
Because \(\bar g\) is analytic and \(u>0\) solves the analytic semilinear equation
\[
-8\Delta_{\bar g}u+\operatorname{Scal}_{\bar g}u=Yu^5,
\]
analytic elliptic regularity gives analytic \(u\) and \(\widehat g\). The source’s Corollary 2.3 describes this equation as linear; it is semilinear, but the stated analyticity conclusion remains valid.

Finally, with
\[
g_0=\frac{-Y}{6}\,\widehat g,
\]
constant rescaling gives
\[
\operatorname{Scal}_{g_0}
=\frac{6}{-Y}Y=-6.
\]
Thus the required analytic \(g_0\) exists on the standard analytic torus.

This also resolves a possible ambiguity: the manifold Yamabe invariant of \(T^3\) being \(0\) does not prevent individual conformal classes from having Yamabe constant \(<0\).

---

## 3. Koiso hypotheses for \(W_0=0\) and \(\lambda=-3\)

Take
\[
W_0=0,\qquad \lambda=-3.
\]
The first constraint in (1) is immediate:
\[
d\operatorname{tr}W_0+\delta W_0=0.
\]
The second becomes
\[
\operatorname{Scal}_{g_0}
=(3-1)(-3)=-6,
\]
which is exactly how \(g_0\) was normalized.

All hypotheses of source Theorem 2.1 are therefore satisfied:

- \(T^3\) is an analytic manifold;
- \(g_0\) is analytic;
- \(W_0=0\) is analytic and symmetric;
- both Einstein hypersurface constraints hold.

The theorem gives a unique analytic germ, in Gaussian gauge,
\[
g^Z=dt^2+g_t,\qquad \operatorname{Ric}_{g^Z}=-3g^Z,
\]
with
\[
g_{t=0}=g_0,\qquad
\dot g_0=-2g_0(W_0\cdot,\cdot)=0.
\]
Since \(T^3\) is compact, the local pieces furnished by the theorem patch over a two-sided collar
\[
(-\varepsilon,\varepsilon)\times T^3
\]
after decreasing \(\varepsilon\). Positivity of \(g_t\) persists for sufficiently small \(|t|\).

Source Corollary 2.2 gives the same existence result directly: for \(m=3\),
\[
\frac{\operatorname{Scal}_{g_0}}{m-1}=-3=\lambda,
\]
and its umbilicity parameter is
\[
\alpha^2=
\frac{-6}{3\cdot2}-\frac{-3}{3}=0,
\]
so the hypersurface is totally geodesic.

---

## 4. The formula for \(\ddot g_0\) and componentwise consistency

Substituting \(\lambda=-3\) and \(\dot g_0=0\) into (2) gives
\[
\boxed{\ddot g_0=2\operatorname{Ric}_{g_0}+6g_0.}
\tag{3}
\]

Its trace is
\[
\operatorname{tr}_{g_0}\ddot g_0
=2\operatorname{Scal}_{g_0}+18
=2(-6)+18=6.
\tag{4}
\]
Consequently \(\ddot g_0\) is nonzero at every point.

Writing
\[
\operatorname{Ric}_{g_0}
=\operatorname{Ric}_{g_0}^{\circ}-2g_0
\]
gives the more informative decomposition
\[
\ddot g_0=2g_0+2\operatorname{Ric}_{g_0}^{\circ}.
\tag{5}
\]
Thus the trace-free part of \(\ddot g_0\) is
\[
(\ddot g_0)^\circ=2\operatorname{Ric}_{g_0}^{\circ}.
\]

If \(\operatorname{Ric}_{g_0}^{\circ}\) vanished identically, then
\[
\operatorname{Ric}_{g_0}=-2g_0.
\]
In dimension three this implies sectional curvature \(K=-1\). Preissmann’s theorem would then force every abelian subgroup of \(\pi_1(T^3)\) to be cyclic, contrary to
\[
\pi_1(T^3)=\mathbb Z^3.
\]
Therefore \((\ddot g_0)^\circ\) is not identically zero. The word “anisotropic” in Step 67 is correct in this global tensorial sense. It is not established that the trace-free part is nonzero at every individual point; that stronger pointwise statement is unnecessary.

Equation (3) also makes all ambient Einstein components agree at \(t=0\). From (4),
\[
\operatorname{Ric}^Z(\nu,\nu)
=-\frac12\operatorname{tr}_{g_0}\ddot g_0=-3.
\]
The mixed component is zero because \(W_0=0\). Tangentially,
\[
\begin{aligned}
\operatorname{Ric}^Z(X,Y)
&=\operatorname{Ric}_{g_0}(X,Y)-\frac12\ddot g_0(X,Y)\\
&=\operatorname{Ric}_{g_0}(X,Y)
-\operatorname{Ric}_{g_0}(X,Y)-3g_0(X,Y)\\
&=-3g_0(X,Y).
\end{aligned}
\]
This explicitly exhibits the mechanism absent from a slice-only argument: arbitrary trace-free intrinsic Ricci at the central slice is canceled by the trace-free part of \(\ddot g_0\).

---

## 5. Time-reflection symmetry

Define the reflected family
\[
\widetilde g_t=g_{-t}.
\]
Then
\[
dt^2+\widetilde g_t
\]
is the pullback of \(dt^2+g_t\) by \((t,x)\mapsto(-t,x)\), so it is again Einstein with constant \(-3\). At \(t=0\),
\[
\widetilde g_0=g_0,\qquad
\dot{\widetilde g}_0=-\dot g_0=0.
\]
It therefore has the same Koiso Cauchy data \((g_0,W_0)\). Uniqueness in source Theorem 2.1 yields
\[
\boxed{g_t=g_{-t}}
\]
as analytic germs.

Equivalently, equation (2) is invariant under \(t\mapsto-t\): its first-derivative terms are quadratic in \(\dot g_t\). Hence \(g_t\) is even, while \(\dot g_t\) is odd.

In particular,
\[
g_t
=g_0+\frac12\ddot g_0\,t^2+O(t^4)
=g_0+\bigl(\operatorname{Ric}_{g_0}+3g_0\bigr)t^2+O(t^4).
\]

---

## 6. Mean-curvature derivative under \(S=-W\)

Set
\[
S_t=-W_t=\frac12g_t^{-1}\dot g_t.
\]
Then
\[
\nabla_X\nu=S_tX,
\]
and with the unnormalized convention used in Step 67,
\[
H(t)=\operatorname{tr}S_t
=\frac12\operatorname{tr}(g_t^{-1}\dot g_t).
\]
Differentiating,
\[
\begin{aligned}
H'
&=\frac12\operatorname{tr}(g_t^{-1}\ddot g_t)
-\frac12\operatorname{tr}\bigl((g_t^{-1}\dot g_t)^2\bigr)\\
&=\frac12\operatorname{tr}_{g_t}\ddot g_t-2|S_t|^2.
\end{aligned}
\]
Since the source formula gives
\[
\operatorname{Ric}^Z(\nu,\nu)
=|S_t|^2-\frac12\operatorname{tr}_{g_t}\ddot g_t,
\]
one obtains
\[
\boxed{H'=-\operatorname{Ric}^Z(\nu,\nu)-|S_t|^2.}
\tag{6}
\]
For \(\operatorname{Ric}^Z=-3g^Z\),
\[
H'=3-|S_t|^2.
\]
At the central slice,
\[
S_0=0,\qquad H(0)=0,\qquad
\boxed{H'(0)=3.}
\]
The same follows immediately from (4):
\[
H'(0)=\frac12\operatorname{tr}_{g_0}\ddot g_0=3.
\]

Time symmetry makes \(H\) odd, so
\[
H(t)=3t+O(t^3).
\]
Consequently, relative to the fixed continuous normal \(\nu=\partial_t\),
\[
H(t)<0\quad (t<0\text{ small}),\qquad
H(t)>0\quad (t>0\text{ small}).
\]
Thus the mean curvature genuinely changes sign through the totally geodesic central torus.

Two convention details are worth recording:

1. If mean curvature is normalized as \(\bar H=\frac13\operatorname{tr}S\), then
   \[
   \bar H'(0)=1,
   \]
   with the same sign change.

2. If one uses \(\operatorname{tr}W\) instead, its derivative at zero is \(-3\).

At the two end slices of a finite collar, using each outward normal instead of the fixed normal \(\partial_t\) reverses the sign at the left end. Both outward traces are then positive for a sufficiently short symmetric collar. Any cusp-matching comparison must therefore state its normal orientations explicitly.

---

## 7. Exact local consequence

The central slice has
\[
\operatorname{Scal}_{g_0}=-6,
\]
so it is intrinsically curved at every point, and \(W_0=S_0=0\), so it is totally geodesic. The ambient metric has zero Einstein residual:
\[
\operatorname{Ric}_{g^Z}+3g^Z=0.
\]
Together with \(H'(0)=3\), this establishes an exact local \(\operatorname{Ric}=-3g\) germ in which a curved \(T^3\) slice is totally geodesic and the fixed-normal mean curvature changes from one sign to the other.

No inconsistency in the supplied source invalidates this conclusion.

This refutes any universal local assertion that torus topology, self-adjointness of the shape operator, scalar curvature information alone, or arbitrarily small ambient Einstein residual prevents such a sign change. It also shows why the flat-slice estimate from Step 63 cannot be extended to general \(x\)-dependent slice metrics: at the central slice,
\[
\operatorname{Ric}_{g_0}-\frac12\ddot g_0=-3g_0,
\]
so normal acceleration cancels the intrinsic Ricci tensor.

It does not contradict the valid flat-slice theorem. The present \(g_0\) has scalar curvature \(-6\), hence is not flat. Nor does it contradict the supplied estimate
\[
\|\operatorname{Ric}_{g_0}+2g_0\|_{\mathrm{op}}<\frac23
\Longrightarrow K_{g_0}<0,
\]
because a torus metric cannot satisfy that strict pinching.

## 8. What remains global

The Koiso theorem supplies only a germ for \(|t|<\varepsilon\). It does not provide:

- continuation for arbitrarily large \(|t|\);
- completeness;
- flat torus slices at distant ends;
- matching of the metric and its required jets to hyperbolic cusp data;
- a uniformly small-residual transition layer;
- a compact metric obtained by graph-manifold gluing;
- a metric sequence on an extended graph manifold with residual tending to zero.

Time reflection gives two locally isometric sides, but it gives no asymptotic cusp behavior. Accordingly, the local result settles the existence of exact mean-curvature reversal near a curved totally geodesic torus, while the two-ended cusp-matching problem and its relation to Yau’s problem remain unresolved.