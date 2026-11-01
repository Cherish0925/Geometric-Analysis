# TTCS Independent Branch Record

```json
{
  "step_id": 72,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/data/step72_conformal_gauge_system.json",
    "Sessions/S0910A03/workspace/data/step72_structural_analysis.json",
    "Sessions/S0910A03/workspace/notes/step70_critical_identity_and_corrections.md",
    "Sessions/S0910A03/workspace/notes/step69_anisotropic_cusp_compensation.md"
  ]
}
```

## Task

Verify the following structural properties of the T²-invariant Einstein system in conformal gauge on [0,R]×S¹.

Metric: g = e^{2φ}(dt²+dz²) + e^{2b}dx² + e^{2c}dy², where (t,z) is the base 2D plane (z periodic), and x,y are T² quotient directions.

Claim 1 (Anisotropy drift-Laplacian): For exact Ric+3g=0, the difference δ=b-c satisfies Δδ + ∇σ·∇δ = 0 where σ=b+c and Δ,∇ are the flat 2D operators on (t,z). This follows from subtracting the xx and yy Einstein equations.

Claim 2 (Maximum principle): On the domain [0,R]×S¹ with reflection conditions δ_t(0,z)=0, the strong maximum principle and Hopf lemma force: either δ is constant, or max_z δ(R,z) ≥ max_z δ(0,z) and min_z δ(R,z) ≤ min_z δ(0,z). The oscillation of the T² anisotropy at the outer boundary is at least as large as at the center.

Claim 3 (Orbit-area equation): Setting ρ=e^{b+c}, the orbit area satisfies Δ_flat(ρ) = (6e^{2φ} - |∇δ|²)·ρ. For isotropic solutions (δ=0), ρ is strictly subharmonic.

Claim 4 (Isotropic impossibility): For isotropic g=dt²+f²h on T³ (3D fiber), the normal Einstein equation gives s'+s²=1 while the tangential gives s'+3s²=3, where s=f'/f. These are algebraically inconsistent with s(0)=0.

Claim 5 (Forced compatibility): For approximate Einstein with |Ric+3g|_op ≤ δ on T³ outer boundary in flat conformal class, the Gauss equation forces δ ≥ (9-H²)/6 where H is mean curvature. Combined with the interior weighted identity (δ ≥ Ce^{-2R} from the normal balance), the constraints are compatible: take H=3-ε, δ~ε, R~(1/2)log(6/ε).

For each claim: (a) verify the derivation, (b) check whether the maximum principle argument is correct for the Neumann boundary at t=0, (c) identify whether the anisotropy preservation BLOCKS cusp matching or merely CONSTRAINS it.

Key question: Does the drift-Laplacian δ equation prevent the construction of approximate Einstein metrics on graph manifolds with Koiso centers? Or does the anisotropy propagation to the boundary merely require matching to an anisotropic cusp (which is what the lattice quotient construction provides)?

## Output

# Scientific verification memo

Write
\[
d=b-c,\qquad \sigma=b+c,\qquad \rho=e^\sigma,
\]
and reserve \(\eta\) for the approximate-Einstein error
\[
\mathcal E=\operatorname{Ric}_g+3g,\qquad \|\mathcal E\|_{\mathrm{op}}\le \eta.
\]
This avoids using the same symbol for anisotropy and curvature error.

For unit vectors in the \(x,y\) directions, the fiber equations are
\[
\mathcal E_x
 =3-e^{-2\phi}\bigl(\Delta b+\nabla \sigma\!\cdot\!\nabla b\bigr),
\qquad
\mathcal E_y
 =3-e^{-2\phi}\bigl(\Delta c+\nabla \sigma\!\cdot\!\nabla c\bigr).
\]
These agree with the `xx` and `yy` expressions in `step72_conformal_gauge_system.json`.

## 1. Anisotropy equation

Subtracting the two fiber equations gives
\[
\mathcal E_x-\mathcal E_y
=-e^{-2\phi}\bigl(\Delta d+\nabla\sigma\cdot\nabla d\bigr).
\]
Hence, for an exact solution,
\[
\boxed{\Delta d+\nabla\sigma\cdot\nabla d=0.}
\]
Equivalently,
\[
\boxed{\operatorname{div}\!\left(e^\sigma\nabla d\right)=0.}
\]

Thus Item 1 is correct. The disappearance of derivatives of \(\phi\) uses the fact that the base is two-dimensional: the scalar Laplacian of \(e^{2\phi}(dt^2+dz^2)\) is \(e^{-2\phi}\Delta_{\rm flat}\).

For an approximate solution, the sourced equation is
\[
\boxed{
\Delta d+\nabla\sigma\cdot\nabla d
=-e^{2\phi}(\mathcal E_x-\mathcal E_y),
}
\qquad
\left|\Delta d+\nabla\sigma\cdot\nabla d\right|
\le 2\eta e^{2\phi}.
\]
Only the \(x\)-versus-\(y\) component of the Einstein error can alter this mode.

## 2. Maximum principle at the reflected face

The operator
\[
L_\sigma=\Delta+\nabla\sigma\cdot\nabla
=e^{-\sigma}\operatorname{div}(e^\sigma\nabla\,\cdot)
\]
is uniformly elliptic on the compact cylinder when \(\sigma\) is smooth.

Suppose \(d\) is not constant. The strong maximum principle excludes a global extremum in the interior. At \(t=0\), the outward Euclidean normal is \(-\partial_t\). The Hopf lemma says that a nonconstant solution attaining its global maximum there must have a nonzero outward normal derivative. Reflection gives
\[
d_t(0,z)=0,
\]
which contradicts that conclusion. The same argument applied to \(-d\) excludes a global minimum there. Consequently,
\[
\boxed{
\max_z d(R,z)>\max_z d(0,z),\qquad
\min_z d(R,z)<\min_z d(0,z)
}
\]
for every nonconstant exact solution. In particular,
\[
\operatorname{osc}_{t=R}d>\operatorname{osc}_{t=0}d.
\]

So Item 2 is correct and can be strengthened from weak to strict inequalities.

There is also a useful energy proof when the outer trace is constant. If \(d(R,z)=K\), set \(u=d-K\). Then
\[
u(R,z)=0,\qquad u_t(0,z)=0,
\]
and integration by parts gives
\[
0=\int u\,\operatorname{div}(e^\sigma\nabla u)
=-\int e^\sigma|\nabla u|^2.
\]
Therefore \(d\equiv K\). Thus an exact reflected solution with constant outer \(x/y\) aspect ratio must have that same constant aspect ratio throughout.

## 3. Orbit-area equation

Adding the fiber equations gives
\[
\mathcal E_x+\mathcal E_y
=6-e^{-2\phi}
 \left(\Delta\sigma+|\nabla\sigma|^2\right).
\]
Since
\[
\frac{\Delta\rho}{\rho}
=\Delta\sigma+|\nabla\sigma|^2,
\]
the exact equation is
\[
\boxed{\Delta_{\rm flat}\rho=6e^{2\phi}\rho.}
\]

The proposed term \(-|\nabla d|^2\rho\) is absent. Indeed, the cross terms from the two fiber equations combine as
\[
|\nabla b|^2+2\nabla b\cdot\nabla c+|\nabla c|^2
=|\nabla(b+c)|^2.
\]
The formula in `step72_structural_analysis.json` should therefore be replaced by the boxed identity above. The proposed identity differs from the true one by \( |\nabla d|^2\rho\).

A stronger conclusion follows:
\[
\boxed{\Delta\rho>0}
\]
for every exact solution, not only when \(d=0\). With reflection,
\[
\rho_t(0,z)=0,
\]
and integration over the cylinder yields
\[
\int_{S^1}\rho_t(R,z)\,dz
=6\int_0^R\int_{S^1}e^{2\phi}\rho\,dz\,dt>0.
\]

For an approximate solution,
\[
\Delta\rho=e^{2\phi}\bigl(6-\mathcal E_x-\mathcal E_y\bigr)\rho,
\]
so \(\rho\) remains strictly subharmonic whenever \(\eta<3\).

## 4. Fully isotropic warped product

For
\[
g=dt^2+f(t)^2h,\qquad s=\frac{f'}f,
\]
with three-dimensional fiber, the normal equation is
\[
\operatorname{Ric}_{tt}=-3\frac{f''}{f}=-3,
\]
hence
\[
\boxed{s'+s^2=1.}
\]

The tangential warped-product formula is
\[
\operatorname{Ric}_g|_{T^3}
=\operatorname{Ric}_h-\bigl(ff''+2(f')^2\bigr)h.
\]
If the four-metric is Einstein on an interval, this tensor equation forces \(h\) to be Einstein. A three-dimensional Einstein metric on \(T^3\) is flat. Therefore
\[
\frac{f''}{f}+2s^2=3,
\]
or
\[
\boxed{s'+3s^2=3.}
\]
Subtracting gives \(s^2=1\), incompatible with the reflection condition \(s(0)=0\). Equivalently, at \(t=0\) the two equations demand simultaneously \(s'(0)=1\) and \(s'(0)=3\).

Thus Item 4 is correct once the flatness of \(h\) is stated or derived as above. It is not independent of \(h\) before the tangential tensor equation is used.

There is also a concrete inconsistency in `step70_critical_identity_and_corrections.md`: the normal equation alone with \(s(0)=0\) gives
\[
s(t)=\tanh t,\qquad H=3\tanh t,
\]
not \(\tanh(\sqrt3\,t)\). This normal solution does not satisfy the tangential Einstein equation.

## 5. Gauss estimate and normal weighted identity

Let \(\Sigma^3\) be an intrinsically flat outer torus, with second fundamental form \(A\), mean curvature \(H\), and unit normal \(\nu\). The scalar Gauss equation gives
\[
0=R_\Sigma
=R_g-2\operatorname{Ric}_g(\nu,\nu)+H^2-|A|^2.
\]
Writing \(\operatorname{Ric}=-3g+\mathcal E\),
\[
0=-6+\operatorname{tr}_\Sigma\mathcal E-\mathcal E_{\nu\nu}
  +H^2-|A|^2.
\]
The operator estimate gives
\[
\left|\operatorname{tr}_\Sigma\mathcal E-\mathcal E_{\nu\nu}\right|
\le4\eta,
\]
while \(|A|^2\ge H^2/3\). Hence
\[
6\le4\eta+\frac23H^2,
\]
and therefore
\[
\boxed{\eta\ge\frac{9-H^2}{6}.}
\]
This is informative when \(|H|<3\).

Pointwise flatness is the precise hypothesis for this pointwise formula. If the induced metric is merely conformal to a flat metric, \(h=u^4h_0\), then
\[
\int_\Sigma R_h\,dV_h
=8\int_\Sigma|\nabla u|_{h_0}^2\,dV_{h_0}\ge0.
\]
An integrated version of the Gauss estimate still follows; for nonconstant \(H\), it involves the average of \(H^2\).

For the normal balance, use Gaussian distance \(r\), so
\[
g=dr^2+h_r,\qquad A=\tfrac12h_r',\qquad A(0)=0.
\]
Set
\[
B=A-I,\qquad \beta=H-3.
\]
With \(\mathcal E=\operatorname{Ric}+3g\),
\[
\mathcal E_{\nu\nu}
=-H'-|A|^2+3,
\]
and hence
\[
\beta'+2\beta+|B|^2=-\mathcal E_{\nu\nu}.
\]
Since \(\beta(0)=-3\),
\[
\boxed{
e^{2R}\beta(R)
=-3-\int_0^R e^{2r}|B|^2\,dr
   -\int_0^R e^{2r}\mathcal E_{\nu\nu}\,dr.
}
\]
The sign of the last integral differs from the displayed integrated line in the Step 70 note when \(\mathcal E=\operatorname{Ric}+3g\); the absolute-value estimate for \(H(R)=3\) is unchanged.

If \(H(R)=3\), this implies
\[
\eta\ge\frac{6}{e^{2R}-1}.
\]
If instead
\[
H(R)=3-\varepsilon,
\]
the correct necessary relation is
\[
\boxed{
3e^{-2R}
\le \varepsilon+\frac{\eta}{2}(1-e^{-2R}).
}
\]
Thus the normal identity alone does not give an error-only estimate of order \(e^{-2R}\) when \(\varepsilon>0\); the endpoint deficit can carry part of the initial discrepancy.

The Gauss estimate supplies
\[
\eta\ge \varepsilon-\frac{\varepsilon^2}{6}.
\]
These two relations are compatible. For small \(\varepsilon\),
\[
\eta\asymp\varepsilon,\qquad e^{-2R}\asymp\varepsilon
\]
is consistent. In particular,
\[
R\sim\frac12\log\frac6\varepsilon,\qquad \eta\sim\varepsilon
\]
satisfies both with room to spare. For \(0\le\varepsilon\le3\), the two inequalities also imply the explicit combined estimate
\[
\eta\ge \frac65e^{-2R}.
\]

The exponential formula uses Gaussian distance. The coordinate \(t\) in
\[
e^{2\phi}(dt^2+dz^2)
\]
is generally not Gaussian distance when \(\phi\) depends on \(z\). Consequently, the same symbol \(R\) cannot be identified in the two gauges without an arclength comparison or a coordinate conversion.

## Consequence for cusp matching and lattice quotients

A flat hyperbolic-cusp cross-section, written in affine coordinates adapted to the \(T^2\) action, has
\[
b-c=\text{constant}.
\]
Unequal \(x\)- and \(y\)-periods merely change this constant. They do not produce \(z\)-dependent oscillation.

For the explicit Koiso center from Step 69,
\[
q_N=u^4\left(dz^2+e^{2f(z)}\frac{dx^2}{N^2}
                   +e^{-2f(z)}\frac{dy^2}{N^2}\right),
\]
one has
\[
d_N=b_N-c_N=2f(z),
\]
independent of \(N\). The outer cusp type \((1,N^{-1},N^{-1})\) has \(d=0\). More generally, unequal quotients replace \(d\) by \(d+\text{constant}\), leaving its oscillation unchanged.

Therefore:

* For exact Einstein metrics in this diagonal \(T^2\)-invariant ansatz, a nonconstant Koiso-center anisotropy cannot attach at finite distance to any translational flat cusp, even one with unequal constant lattice lengths.
* The lattice quotient construction resolves the overall scale mismatch and the anisotropy between the \(z\) direction and the two quotient directions. By itself it does not resolve the oscillatory \(x/y\) mode \(d(z)\).
* For approximate Einstein metrics, the drift equation becomes sourced, so it does not furnish a universal impossibility theorem. The required change must be carried by
  \[
  \mathcal E_x-\mathcal E_y,
  \]
  with its effect weighted by \(e^{2\phi}\).

On a fixed cylinder with uniformly controlled \(\phi,\sigma\), constant outer data \(d=K\), and \(u=d-K\), one has
\[
\int e^\sigma|\nabla u|^2
=-\int e^\sigma u\,e^{2\phi}(\mathcal E_x-\mathcal E_y).
\]
Weighted Poincaré and elliptic estimates then force the center anisotropy to approach a constant as \(\eta\to0\). Thus the quotient parameter \(N\), which only adds constants to \(b,c\), does not alone make the required error small.

The final answer to the key question is therefore intermediate: the exact drift-Laplacian equation blocks direct exact cusp attachment for the nonconstant Koiso seed, while approximate graph-manifold constructions are not ruled out by this equation alone. An unequal flat lattice is insufficient; the oscillatory mode requires a quantitatively controlled sourced transition, a geometric degeneration that amplifies the source term, or a different reflected center with \(b-c\) constant.