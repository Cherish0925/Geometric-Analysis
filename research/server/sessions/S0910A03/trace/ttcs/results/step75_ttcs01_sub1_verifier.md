# TTCS Independent Branch Record

```json
{
  "step_id": 75,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/data/step75_structural_identities.json",
    "Sessions/S0910A03/workspace/scripts/step75_structural_identities_verify.py",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md",
    "Sessions/S0910A03/workspace/data/step70_ricci_T2inv.json"
  ]
}
```

## Task

For the Yau-26 negative graph-neck program, independently check the mathematical results in the Step-75 note. Verify from first principles: (i) for q=ds^2+G(s) on T^3 with flat T^2 orbits and R_q=-6, the formula R_q=-2h'-|A|^2-h^2 and the downward-zero argument forcing an orbit-plane sectional curvature >=3; (ii) the equivalence to an eigenvalue <=-3 of Ric_q+3I and to reflected Einstein shape acceleration; (iii) under |Ric_4+3g|_op<=delta at a reflected center, the stated quantitative constant lambda_min S'(0)<=-3+5delta, including every trace and sign; (iv) the finite-cylinder anisotropy integration showing reflection plus exact equal orbit normal derivatives at the exit forces d=b-c constant and makes the scalar-minus-six center impossible; (v) the normal weighted identity and physical-length inequality. Report corrected formulas if anything is wrong, and distinguish exact results from statements requiring extra regularity, orientation, coordinates, or boundary assumptions.

## Output

# Scientific memo: Step-75 structural identities

## Summary

The orbit-scalar formula, downward-zero argument, finite-cylinder anisotropy argument, and weighted normal identity are correct in the stated geometric settings.

Two refinements matter:

1. At the point selected by the downward-zero argument, the orbit-normal vector is a Ricci eigenvector with eigenvalue
   \[
   (\operatorname{Ric}_q+3I)(v,v)=-K_{\rm orb}\le -3.
   \]
   Thus orbit curvature \(K_{\rm orb}\ge3\) is equivalent to this particular normal eigenvalue being at most \(-3\). Merely saying that some eigenvalue is at most \(-3\) is a weaker statement and is not logically reversible by itself.

2. The Step-75 estimate
   \[
   \lambda_{\min}S'(0)\le -3+5\delta
   \]
   is valid, with all signs correct. Under the same operator-norm hypothesis, retaining the dependence among the error components improves it to
   \[
   \boxed{\lambda_{\min}S'(0)\le -3+3\delta.}
   \]
   The \(5\delta\) in the JSON file results from separately estimating two quantities whose \(E_{vv}\) terms actually cancel.

---

## 1. Scalar curvature of \(q=ds^2+G(s)_{ab}dx^a dx^b\)

Let
\[
K_{ab}=\frac12G'_{ab},\qquad
A^a{}_b=G^{ac}K_{cb}=\frac12(G^{-1}G')^a{}_b,\qquad
h=\operatorname{tr}A.
\]
Here \(s\) is arclength on the quotient circle, and
\[
|A|^2=\operatorname{tr}(A^2)
\]
because \(A\) is self-adjoint with respect to \(G\).

The nonzero mixed Christoffel symbols are
\[
\Gamma^s_{ab}=-K_{ab},\qquad
\Gamma^a_{sb}=A^a{}_b.
\]
Since the coefficients of \(G(s)\) are independent of \(x^1,x^2\), each orbit is intrinsically flat. The normal Ricci curvature is
\[
\operatorname{Ric}_q(\partial_s,\partial_s)
=-h'-|A|^2.
\]
The Gauss equation for the orbit plane gives
\[
K_{\rm orb}=-\det A.
\]
In dimension three,
\[
R_q=2\bigl(\operatorname{Ric}_q(\partial_s,\partial_s)+K_{\rm orb}\bigr),
\]
so
\[
R_q=-2h'-2|A|^2-2\det A.
\]
For a \(2\times2\) endomorphism,
\[
h^2=(\operatorname{tr}A)^2=|A|^2+2\det A.
\]
Consequently,
\[
\boxed{R_q=-2h'-|A|^2-h^2.}
\]

This derivation allows non-diagonal \(G(s)\). It uses the global orthogonal product form \(ds^2+G(s)\), not an arbitrary metric with additional orbit-connection terms.

### The downward zero

Because \(G\) is periodic,
\[
\int_0^Lh\,ds
=\log\sqrt{\det G(L)}-\log\sqrt{\det G(0)}=0.
\]
If \(h\not\equiv0\), it has both signs. At the end of a component where \(h>0\), there is a point \(s_0\) with
\[
h(s_0)=0,\qquad h'(s_0)\le0.
\]
At this point \(A\) is trace-free. Its eigenvalues are \(\alpha,-\alpha\), and hence
\[
-\det A=\alpha^2=\frac12|A|^2.
\]
If \(R_q=-6\), the scalar formula at \(s_0\) becomes
\[
-6=-2h'-|A|^2,
\]
or
\[
\frac12|A|^2=3-h'.
\]
Therefore
\[
\boxed{K_{\rm orb}=-\det A=\frac12|A|^2=3-h'\ge3.}
\]
If \(h\equiv0\), then \(h'=0\) and the same calculation gives
\[
|A|^2=6,\qquad K_{\rm orb}=3
\]
at every point. Thus Step 75 correctly covers both cases.

The minimum regularity needed here is \(G\in C^2\), positive definite and periodic; the supplied setting is smooth.

---

## 2. Ricci eigenvalue and reflected Einstein acceleration

Let \(v=\partial_s\), and let \(e_1,e_2\) be an orthonormal basis of the orbit plane. In dimension three,
\[
\operatorname{Ric}_q(v,v)
=K(v,e_1)+K(v,e_2)
=\frac{R_q}{2}-K_{\rm orb}.
\]
For \(R_q=-6\),
\[
\operatorname{Ric}_q(v,v)=-3-K_{\rm orb},
\]
and hence
\[
\boxed{(\operatorname{Ric}_q+3q)(v,v)=-K_{\rm orb}.}
\]

Moreover, for \(q=ds^2+G(s)\),
\[
\operatorname{Ric}_q(v,e_a)=0.
\]
This follows either directly from the Christoffel symbols or from the Codazzi expression
\[
\operatorname{Ric}_q(v,\cdot)|_{T^2}
=\operatorname{div}A-dh,
\]
whose orbit derivatives vanish. Thus \(v\) is an actual eigenvector, not merely a test vector. At the selected point,
\[
K_{\rm orb}\ge3
\quad\Longleftrightarrow\quad
v\text{ has eigenvalue }-K_{\rm orb}\le-3
\]
for \(\operatorname{Ric}_q+3I\). This in turn implies
\[
\lambda_{\min}(\operatorname{Ric}_q+3I)\le-3.
\]

The reverse implication from “some eigenvalue is at most \(-3\)” to \(K_{\rm orb}\ge3\) need not identify the orbit-normal eigenvalue. The precise equivalent formulation is the one involving \(v\).

### Four-dimensional shape acceleration

Write a Gaussian four-metric as
\[
\bar g=dr^2+q_r,
\qquad
S=\frac12q_r^{-1}\partial_rq_r,
\qquad H=\operatorname{tr}S.
\]
This convention makes an expanding hyperbolic cusp satisfy \(S=I\). The Gaussian Ricci equations are
\[
\operatorname{Ric}_{\bar g,rr}=-H'-|S|^2,
\]
and
\[
(\operatorname{Ric}_{\bar g})_T^\sharp
=\operatorname{Ric}_{q_r}^\sharp-S'-HS.
\]
At a reflected center, \(q_r\) is even and therefore
\[
S(0)=0.
\]
If \(\operatorname{Ric}_{\bar g}=-3\bar g\), the tangential equation at \(r=0\) gives
\[
-3I=\operatorname{Ric}_{q_0}^\sharp-S'(0),
\]
so
\[
\boxed{S'(0)=\operatorname{Ric}_{q_0}^\sharp+3I.}
\]
Consequently the orbit-normal eigenvalue satisfies
\[
S'(0)v=-K_{\rm orb}v,
\]
and at the selected point
\[
\lambda_{\min}S'(0)\le-3.
\]

Since
\[
q_r''(0)=2q_0S'(0),
\]
this is also the second-order contraction of the induced metric in that direction. Reversing the definition of the shape operator changes the displayed shape signs; the convention above is the convention used by the Step-75 normal identity.

---

## 3. Small four-dimensional defect at the reflected center

Set
\[
E=\operatorname{Ric}_{\bar g}+3\bar g,
\qquad \|E\|_{\mathrm{op}}\le\delta.
\]
At the reflected center \(S=0\). From the tangential Gaussian equation,
\[
E_T^\sharp
=\operatorname{Ric}_{q}^\sharp+3I-S'.
\]
Taking its tangential trace gives
\[
\operatorname{tr}_T E=R_q+9-\operatorname{tr}S'.
\]
The normal component is
\[
E_{nn}=3-H'=3-\operatorname{tr}S'.
\]
Subtracting,
\[
\boxed{e:=R_q+6=\operatorname{tr}_T E-E_{nn}.}
\]
Thus
\[
|e|\le |\operatorname{tr}_T E|+|E_{nn}|
\le3\delta+\delta=4\delta.
\]
This verifies the Step-75 trace identity and its \(4\delta\) estimate.

At a downward zero of \(h\),
\[
-6+e=-2h'-|A|^2.
\]
Since \(h'\le0\),
\[
K_{\rm orb}=\frac12|A|^2
=3-\frac e2-h'
\ge3-\frac e2.
\]
For the center orbit-normal \(v\),
\[
(\operatorname{Ric}_q+3q)(v,v)
=\frac e2-K_{\rm orb}
\le e-3.
\]
Using \(S'=\operatorname{Ric}_q^\sharp+3I-E_T^\sharp\),
\[
\langle S'v,v\rangle
\le e-3-E_{vv}.
\]
The Step-75 estimate treats \(e\le4\delta\) and \(-E_{vv}\le\delta\) separately, yielding
\[
\lambda_{\min}S'(0)
\le\langle S'v,v\rangle
\le-3+5\delta.
\]
Hence the stated constant is valid.

There is, however, an exact cancellation. In an orthonormal frame
\[
(v,e_1,e_2,n),
\]
where \(e_1,e_2\) are orbit tangent and \(n\) is the four-dimensional Gaussian normal,
\[
e=E_{vv}+E_{11}+E_{22}-E_{nn}.
\]
Therefore
\[
e-E_{vv}=E_{11}+E_{22}-E_{nn},
\]
and
\[
\begin{aligned}
\langle S'v,v\rangle
&\le -3+E_{11}+E_{22}-E_{nn}\\
&\le -3+3\delta.
\end{aligned}
\]
Thus the stronger result is
\[
\boxed{\lambda_{\min}S'(0)\le-3+3\delta.}
\]
This uses only the same full four-dimensional operator-norm estimate. The line \(5\delta-3\) in `step75_structural_identities.json` correctly reproduces the two-stage estimate but does not retain this cancellation.

If \(h\equiv0\), the same approximate calculation applies at any point, with \(h'=0\).

---

## 4. Finite-cylinder anisotropy integration

Consider
\[
g=e^{2\phi}(dt^2+dz^2)+e^{2b}dx^2+e^{2c}dy^2,
\qquad
d=b-c,\quad \sigma=b+c.
\]
Let
\[
\gamma=e^{2\phi}(dt^2+dz^2)
\]
be the base metric. The normalized fiber Ricci curvatures satisfy
\[
\operatorname{Ric}(e_x,e_x)-\operatorname{Ric}(e_y,e_y)
=-\left(\Delta_\gamma d+
\langle\nabla_\gamma\sigma,\nabla_\gamma d\rangle_\gamma\right).
\]
For an exact Einstein metric the left side vanishes, so
\[
\operatorname{div}_\gamma(e^\sigma\nabla_\gamma d)=0.
\]
Because the base is two-dimensional and conformal,
\[
\operatorname{div}_\gamma(e^\sigma\nabla_\gamma d)
=e^{-2\phi}\operatorname{div}_0(e^\sigma\nabla_0d).
\]
Hence
\[
\boxed{\operatorname{div}_{t,z}(e^\sigma\nabla d)=0.}
\]

On a finite periodic cylinder \(D=[0,T]\times S^1\), multiply by \(d\) and integrate:
\[
0
=\int_Dd\,\operatorname{div}(e^\sigma\nabla d)
=\text{face terms}-\int_De^\sigma|\nabla d|^2.
\]
Reflection at \(t=0\) gives
\[
d_n=0.
\]
Equality of the two orbit principal normal derivatives at \(t=T\) gives
\[
b_n=c_n,\qquad d_n=0.
\]
The \(z\)-face terms cancel by periodicity, and both \(t\)-face terms vanish. Therefore
\[
\int_De^\sigma|\nabla d|^2=0.
\]
Since \(e^\sigma>0\) and the cylinder is connected,
\[
\boxed{d\equiv d_0.}
\]

Full umbilicity of the outer face is more than is needed here: equality of the \(x\)- and \(y\)-orbit principal curvatures suffices.

For a nonzero Einstein defect, the equation becomes
\[
\operatorname{div}_{t,z}(e^\sigma\nabla d)
=-e^{\sigma+2\phi}(E_x-E_y),
\]
so the preceding energy identity no longer forces \(d\) to be constant.

### Center scalar curvature contradiction

At the reflected center,
\[
q=e^{2\phi(z)}dz^2
 +e^{\sigma(z)+d_0}dx^2
 +e^{\sigma(z)-d_0}dy^2.
\]
Define a new circle coordinate by
\[
d\tau=e^{\phi-\sigma/2}\,dz.
\]
The multiplier is smooth, positive and periodic, so this defines a circle coordinate with some period \(L>0\). Then
\[
q=e^\sigma\left(d\tau^2+e^{d_0}dx^2+e^{-d_0}dy^2\right)
=u^4q_{\rm flat},
\qquad u=e^{\sigma/4}>0.
\]

For an exact reflected metric with \(\operatorname{Ric}_g=-3g\), the center is totally geodesic and the scalar Gauss equation gives
\[
R_q=R_g-2\operatorname{Ric}_g(n,n)
=-12-2(-3)=-6.
\]
The three-dimensional conformal scalar formula is therefore
\[
-8\Delta_{q_{\rm flat}}u=-6u^5.
\]
Integration over the flat torus gives
\[
0=-6\int_{T^3}u^5\,d\mu_{q_{\rm flat}},
\]
which is impossible because \(u>0\). Thus no exact finite cylinder in this diagonal orthogonally-transitive class can simultaneously have:

- a reflected center,
- \(\operatorname{Ric}=-3g\),
- periodic \(z\),
- and equal \(x,y\) orbit normal derivatives at the outer face.

The argument uses the global product coordinates of the displayed ansatz. Smoothness is more than sufficient; \(C^2\) coefficients and well-defined \(C^1\) endpoint traces already support the calculation.

---

## 5. Weighted normal identity and physical length

For a Gaussian metric
\[
g=dr^2+h_r
\]
in four dimensions, set
\[
S=\frac12h_r^{-1}h_r',\qquad
H=\operatorname{tr}S,\qquad
B=S-I,\qquad b=H-3.
\]
The normal Ricci equation gives
\[
E_{rr}=-H'-|S|^2+3.
\]
Since
\[
|S|^2=|I+B|^2
=3+2\operatorname{tr}B+|B|^2
=3+2b+|B|^2,
\]
one obtains
\[
\boxed{b'+2b+|B|^2=-E_{rr}.}
\]
Equivalently,
\[
\boxed{(e^{2r}b)'=-e^{2r}(|B|^2+E_{rr}).}
\]

At a reflected center,
\[
S(0)=0,\qquad H(0)=0,\qquad b(0)=-3.
\]
Set
\[
\eta=3-H(R)=-b(R).
\]
Integration from \(0\) to \(R\) yields
\[
-e^{2R}\eta+3
=-\int_0^Re^{2r}(|B|^2+E_{rr})\,dr,
\]
hence
\[
\boxed{
e^{2R}\eta
=3+\int_0^Re^{2r}\bigl(|S-I|^2+E_{rr}\bigr)\,dr.
}
\]

If \(\|E\|_{\mathrm{op}}\le\delta\), then \(E_{rr}\ge-\delta\), so
\[
\boxed{
e^{2R}\eta+\frac{\delta}{2}(e^{2R}-1)
\ge
3+\int_0^Re^{2r}|S-I|^2\,dr
\ge3.
}
\]
All signs in Step 75 are correct.

The formula is pointwise along each Gaussian normal geodesic. If \(H\) varies across the exit slice, then \(\eta\) is likewise a function on that slice and the identity holds at each normal label.

For a signed \(\eta\), the displayed inequality implies
\[
3\le e^{2R}\left(|\eta|+\frac\delta2\right),
\]
and therefore, whenever the right-hand logarithm is positive,
\[
\boxed{
R\ge\frac12\log\frac{3}{|\eta|+\delta/2}.
}
\]
If \(\eta\ge0\), the slightly sharper expression is
\[
R\ge
\frac12\log\frac{3+\delta/2}{\eta+\delta/2}.
\]
Thus uniform convergence of both \(H(R)\) to \(3\) and \(E\) to zero requires the Gaussian distance \(R\) to diverge.

Here \(r\) must be unit-speed Gaussian distance and the exit must be a constant-\(r\) slice. In coordinates
\[
e^{2\phi(t,z)}(dt^2+dz^2),
\]
the coordinate interval in \(t\) is generally not this distance. When \(\phi_z\neq0\), the \(t\)-coordinate curves need not be normal geodesics, so a conformal-coordinate length cannot replace \(R\).

## Final assessment

The central Step-75 geometric results are mathematically sound in their stated ansätze. The precise refinements are:

\[
K_{\rm orb}\ge3
\iff
\text{the orbit-normal eigenvalue of }\operatorname{Ric}_q+3I\text{ is }\le-3,
\]
rather than an unrestricted converse involving any eigenvalue, and
\[
\boxed{\lambda_{\min}S'(0)\le-3+3\delta}
\]
is available under the same hypothesis that was used for the recorded \(-3+5\delta\) estimate.