# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step63_matching_problem_formulation.md",
    "Sessions/S0910A03/workspace/scripts/step63_torus_transition_analysis.py",
    "Sessions/S0910A03/workspace/data/step63_torus_transition_analysis.json"
  ]
}
```

## Task

Verify the following mathematical claims from Step 63 of the Yau 26 research project. Focus on correctness of the differential geometry, not literature.

CLAIM 1 (Flat-slice barrier): For g = dr^2 + G(r) on T^3 x [a,b] with intrinsically flat T^3 slices and ||Ric+3g||_op <= delta, the traced Gauss equation gives H^2 - |S|^2 = 2Ric(dr,dr) - R_M, which lies in [6-4delta, 6+4delta]. Since |S|^2 >= H^2/3 (Cauchy-Schwarz for self-adjoint 3x3), we get H^2 >= 9-6*delta > 0 for delta < 3/2.

CLAIM 2 (Exact Einstein funnel): The warped product g = dr^2 + cosh^2(r)*g_N on R x T^3, where (T^3, g_N) has Ric_{g_N} = -2*g_N (possible by Lohkamp), satisfies Ric_g = -3g exactly. Check using the standard warped product formulas: Ric(dr,dr) = -k*f''/f with k=3, and Ric(X,Y) = Ric_N(X,Y) - [f''/f + (k-1)(f'/f)^2]*f^2*g_N(X,Y) for X,Y tangent to N.

CLAIM 3 (Scaling argument): In the transition annulus [L,L+ell] x T^3 where the slice metric deforms from flat to Ric=-2, the Ricci defect scales as O(1/ell^2 + exp(-2L)). For a sequence of graph manifolds with increasingly large hyperbolic pieces, both ell and L can grow, giving delta -> 0.

CLAIM 4 (Gluing compatibility): The affine diffeomorphism gluing of extended graph manifolds requires FLAT boundary tori. The non-flat Einstein collar cannot be directly glued, but a flat-to-non-flat transition annulus solves this: gluing happens at the flat boundary of the transition annulus.

For each claim, verify the algebra, identify any sign errors or missing terms, and assess whether the conclusion follows from the computation. If any claim is wrong, give the correct statement.

## Output

## Verification memo

Let \(\nu=\partial_r\), \(S=\tfrac12 G^{-1}G'\), and \(H=\operatorname{tr}_G S\). The operator norm condition  
\[
\|\operatorname{Ric}_g+3g\|_{\mathrm{op}}\le \delta
\]
means pointwise that the four eigenvalues of \(\operatorname{Ric}_g\) lie in \([-3-\delta,-3+\delta]\).

---

## 1. Flat-slice barrier

The traced Gauss equation for a hypersurface \(\Sigma_r\subset (M^4,g)\) is
\[
R_{\Sigma_r}=R_M-2\operatorname{Ric}_M(\nu,\nu)+H^2-|S|^2 .
\]
If each \(\Sigma_r\cong T^3\) is intrinsically flat, then \(R_{\Sigma_r}=0\), hence
\[
H^2-|S|^2=2\operatorname{Ric}_M(\nu,\nu)-R_M .
\]

Write the Ricci eigenvalues as \(\lambda_0\) in the normal direction and \(\lambda_1,\lambda_2,\lambda_3\) in tangential directions. Then
\[
2\operatorname{Ric}(\nu,\nu)-R_M
=2\lambda_0-(\lambda_0+\lambda_1+\lambda_2+\lambda_3)
=\lambda_0-(\lambda_1+\lambda_2+\lambda_3).
\]
Since each \(\lambda_i\in[-3-\delta,-3+\delta]\),
\[
\lambda_0-(\lambda_1+\lambda_2+\lambda_3)
\in [6-4\delta,\,6+4\delta].
\]
Thus
\[
H^2-|S|^2\in[6-4\delta,6+4\delta].
\]

For a self-adjoint operator \(S\) on a 3-dimensional slice,
\[
|S|^2\ge \frac{H^2}{3}.
\]
Therefore
\[
H^2-|S|^2\le H^2-\frac{H^2}{3}=\frac{2}{3}H^2.
\]
If \(\delta<\tfrac32\), the lower endpoint \(6-4\delta\) is positive, so
\[
\frac{2}{3}H^2\ge 6-4\delta,
\]
hence
\[
H^2\ge 9-6\delta>0.
\]

So the algebra is correct. There is no sign mistake in this part. A direct consequence is that on a connected region whose \(T^3\)-slices are flat, \(H\) cannot vanish and therefore cannot change sign when \(\delta<3/2\).

---

## 2. Exact Einstein funnel

For a warped product
\[
g=dr^2+f(r)^2 g_N,\qquad \dim N=3,
\]
the standard Ricci formulas are
\[
\operatorname{Ric}(\partial_r,\partial_r)=-3\frac{f''}{f},
\]
\[
\operatorname{Ric}(\partial_r,X)=0,
\]
and for \(X,Y\) tangent to \(N\),
\[
\operatorname{Ric}(X,Y)
=
\operatorname{Ric}_N(X,Y)
-
\left[
\frac{f''}{f}
+2\left(\frac{f'}{f}\right)^2
\right] f^2 g_N(X,Y).
\]

Take \(f(r)=\cosh r\). Then
\[
\frac{f''}{f}=1,\qquad \frac{f'}{f}=\tanh r.
\]
If
\[
\operatorname{Ric}_N=-2g_N,
\]
then
\[
\operatorname{Ric}(\partial_r,\partial_r)=-3.
\]
For tangential directions,
\[
\begin{aligned}
\operatorname{Ric}(X,Y)
&=
-2g_N(X,Y)
-
\left[1+2\tanh^2 r\right]\cosh^2 r\, g_N(X,Y)\\
&=
\left[-2-\cosh^2 r-2\sinh^2 r\right]g_N(X,Y)\\
&=
\left[-2-\cosh^2 r-2(\cosh^2 r-1)\right]g_N(X,Y)\\
&=
-3\cosh^2 r\, g_N(X,Y)\\
&=
-3g(X,Y).
\end{aligned}
\]
Thus, conditionally on the existence of a fixed 3-metric \(g_N\) with
\[
\operatorname{Ric}_{g_N}=-2g_N,
\]
the warped product
\[
g=dr^2+\cosh^2(r)g_N
\]
is exactly Einstein with Einstein constant \(-3\).

The problematic part is the assertion that such a \(g_N\) exists on \(T^3\) by Lohkamp’s theorem. Lohkamp’s theorem gives metrics with \(\operatorname{Ric}<0\) on manifolds of dimension at least \(3\). It does not give Einstein metrics, and it does not give \(\operatorname{Ric}=-2g\).

In dimension \(3\), the condition
\[
\operatorname{Ric}_{g_N}=-2g_N
\]
is much stronger than \(\operatorname{Ric}<0\). It forces constant sectional curvature \(-1\). Indeed, in dimension \(3\) the full curvature tensor is determined by the Ricci tensor; if \(\operatorname{Ric}=-2g\), then
\[
R_{ijkl}=-(g_{ik}g_{jl}-g_{il}g_{jk}),
\]
so every sectional curvature equals \(-1\). A closed \(3\)-torus cannot carry a metric of constant sectional curvature \(-1\); equivalently, a closed hyperbolic \(3\)-manifold cannot have fundamental group \(\mathbb Z^3\).

Therefore the correct statement is:

- The warped-product computation is algebraically correct.
- If \(N^3\) is a closed hyperbolic \(3\)-manifold with \(\operatorname{Ric}_N=-2g_N\), then \(dr^2+\cosh^2(r)g_N\) is exactly Einstein with \(\operatorname{Ric}=-3g\).
- For \(N=T^3\), this exact warped-product model is unavailable because \(T^3\) carries no metric with \(\operatorname{Ric}=-2g\).

If one only has
\[
\operatorname{Ric}_{g_N}=-2g_N+E
\]
for some error tensor \(E\), then for \(f=\cosh r\) the tangential part of \(\operatorname{Ric}_g+3g\) is exactly \(E\) as a bilinear form on \(N\), and has size \(|E|/\cosh^2 r\) in a \(g\)-orthonormal frame. Exactness requires \(E=0\).

---

## 3. Scaling argument for the transition annulus

The proposed estimate
\[
\delta \sim O\!\left(\frac1{\ell^2}+e^{-2L}\right)
\]
does not follow from the Ricci equations as stated. Stretching the \(r\)-coordinate reduces only those terms containing \(r\)-derivatives of the interpolating slice metric. It does not remove the algebraic terms involving the intrinsic Ricci tensor of the slices and the quadratic terms in the shape operator.

The radial Ricci equation for a general foliation \(g=dr^2+G(r)\) is
\[
\operatorname{Ric}(\nu,\nu)=-\operatorname{tr}(S')-|S|^2.
\]
Thus the condition \(\operatorname{Ric}(\nu,\nu)=-3+O(\delta)\) is
\[
\operatorname{tr}(S')+|S|^2=3+O(\delta).
\]

At a slice where \(H=0\), this equation still has to hold. There are two possibilities:

1. **Isotropic-type behavior.** If \(S\) is small at \(H=0\), then one needs \(\operatorname{tr}(S')\approx 3\). That is an \(O(1)\) derivative, so the transition cannot be made arbitrarily long while keeping the radial equation close to the Einstein value.

2. **Shear-dominated behavior.** If the transition is stretched so that \(S'=O(1/\ell)\), then at \(H=0\) the radial equation forces
   \[
   |S|^2=3+O(\delta)+O(1/\ell).
   \]
   This is again an \(O(1)\) condition, not a term of size \(O(1/\ell^2)\).

A simple stretched cosh illustrates the issue. Take
\[
f_\ell(r)=\cosh(r/\ell)
\]
and first take flat \(T^3\)-slices. At \(r=0\),
\[
\frac{f_\ell''}{f_\ell}=\frac1{\ell^2},\qquad \frac{f_\ell'}{f_\ell}=0.
\]
Then
\[
\operatorname{Ric}(\partial_r,\partial_r)=-\frac{3}{\ell^2},
\]
whereas the target value is \(-3\). The radial defect is
\[
\left|-\frac{3}{\ell^2}+3\right|=3\left(1-\frac1{\ell^2}\right),
\]
which is \(O(1)\), not \(O(1/\ell^2)\). The tangential defect is also \(O(1)\). Thus simply stretching the transition does not preserve the near-Einstein condition.

The term \(e^{-2L}\) also does not control the crucial part of the reversal. Suppose one uses a fixed fiber with \(\operatorname{Ric}_N=-2g_N\) and takes
\[
f(r)=A\cosh r.
\]
The radial equation still gives \(\operatorname{Ric}(\nu,\nu)=-3\), but the tangential Ricci eigenvalue at the \(H=0\) slice is
\[
-\frac{2}{A^2}-1.
\]
The target value is \(-3\), so the defect at that slice is
\[
\left|-\frac{2}{A^2}-1+3\right|
=
2-\frac{2}{A^2}.
\]
For large \(A\), this tends to \(2\), not to \(0\). Hence placing the transition at large warping factor does not by itself remove the \(O(1)\) tangential defect at the place where \(H=0\).

More conceptually: the \(H\)-reversal must pass through a slice with \(H=0\). Near such a slice, the radial and tangential equations force either an \(O(1)\) derivative of \(S\), an \(O(1)\) shear \(|S|^2\), or an \(O(1)\) intrinsic Ricci contribution from the slice. These are algebraic/zeroth-order constraints. They are not suppressed merely by making the annulus longer.

There is also a further geometric point. If the long-scaling argument made \(S'\) uniformly small, then at \(H=0\) the tangential equation would force the intrinsic slice Ricci to be close to a pure-trace tensor of the form \(-3G\) or \(-2G\), depending on the precise shear behavior. In dimension \(3\), being sufficiently close to such a pure-trace Ricci tensor forces all sectional curvatures of the slice to be \(<0\). A \(3\)-torus cannot carry a metric with all sectional curvatures strictly below \(0\). Quantitatively, if a \(3\)-metric satisfies
\[
\|\operatorname{Ric}+2g\|_{\mathrm{op}}<\frac23,
\]
then its sectional curvatures are all \(<0\). Thus a fixed \(T^3\)-slice cannot be made arbitrarily close to the Einstein fiber needed by the simple funnel model.

So the correct statement is weaker:

- Making the annulus long can reduce defects coming purely from \(r\)-derivatives of a prescribed interpolation.
- It does not control the intrinsic Ricci of the slices, the quadratic shear terms, or the mixed Codazzi-type terms.
- The estimate \(O(1/\ell^2+e^{-2L})\) is not valid as a general consequence of the setup.
- The conclusion \(\delta\to0\) for a sequence of graph manifolds does not follow from this scaling argument alone.

---

## 4. Gluing compatibility

The standard affine gluing of cusp pieces uses flat affine structures on the torus interfaces. An affine diffeomorphism between flat tori preserves the flat affine structure. It cannot identify a non-flat induced metric with a flat one, because intrinsic curvature is preserved by isometry and affine equivalence.

Thus a non-flat Einstein collar cannot be directly affinely glued to a flat cusp interface. This part is correct.

However, saying that a flat-to-non-flat transition annulus “solves” the issue is incomplete. To obtain a smooth Riemannian metric after gluing, one must match more than the topological affine structure. At the joining surface one needs at least:

1. matching of the induced metric;
2. matching of the second fundamental form, equivalently matching \(G\) and \(G'\) in Gaussian coordinates;
3. enough differentiability to avoid distributional contributions to \(\operatorname{Ric}\).

For a hyperbolic cusp truncated at a flat torus, the induced metric is flat and the shape operator is \(\pm \mathrm{Id}\), depending on orientation. A transition annulus ending in a flat torus can be glued affinely only if its induced flat metric and its second fundamental form agree with those of the cusp truncation. If only the metric matches but the second fundamental form jumps, the resulting metric is not \(C^2\), and the Ricci tensor acquires singular or large smoothing errors.

Therefore:

- A flat interface is necessary for affine gluing to a cusp.
- A transition annulus can move the gluing location to a flat interface.
- But the transition annulus still has to perform the flat-to-non-flat deformation while keeping the full \(4\)-dimensional Ricci tensor close to \(-3g\).
- The gluing observation does not itself construct such a transition.

---

## Overall assessment

1. **Flat-slice barrier:** Correct. The traced Gauss equation and Cauchy–Schwarz step give \(H^2\ge 9-6\delta\), so for \(\delta<3/2\) a flat \(T^3\)-slice cannot have \(H=0\).

2. **Exact Einstein funnel:** The warped-product algebra is correct conditional on a fixed fiber with \(\operatorname{Ric}_N=-2g_N\). But such a fiber cannot exist on \(T^3\). Lohkamp’s theorem does not supply it. The exact model exists over a closed hyperbolic \(3\)-manifold, not over \(T^3\).

3. **Scaling argument:** Not valid as stated. Stretching the annulus reduces derivative terms but does not remove the \(O(1)\) radial and tangential algebraic constraints at the \(H=0\) slice. The estimate \(O(1/\ell^2+e^{-2L})\) omits the intrinsic slice Ricci, the shear magnitude, and the mixed components. The conclusion \(\delta\to0\) does not follow.

4. **Gluing compatibility:** Direct affine gluing requires flat interfaces, so a non-flat collar cannot be glued directly. A transition annulus with a flat outer interface can restore affine compatibility, but one must also match the second fundamental form, and the interior transition still has to satisfy the near-Einstein equations.