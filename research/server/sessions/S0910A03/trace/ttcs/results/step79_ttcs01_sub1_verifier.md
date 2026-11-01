# TTCS Independent Branch Record

```json
{
  "step_id": 79,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/data/step79_ot_reduction.json",
    "Sessions/S0910A03/workspace/data/step79_verifications.json",
    "Sessions/S0910A03/workspace/notes/step78_rotating_eigenframe_barrier.md",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md"
  ]
}
```

## Task

Verify the following structural reduction for orthogonally transitive T²-invariant 4D Einstein metrics with Ric = -3g.

Metric: g = e^{2λ}(dr²+dz²) + G_{ab}(r,z)dξ^a dξ^b with G = e^σ M, det M = 1.

1. AREA EQUATION: σ_rr + σ_zz + σ_r² + σ_z² = 6 e^{2λ}. Check the coefficient 6.

2. ORBIT MAP EQUATION: div(e^σ M^{-1}dM) = 0 (weighted harmonic map to H² = SL(2)/SO(2)).
  In H² polar coords: d-eq: (e^σ d_r)_r + (e^σ d_z)_z = e^σ sinh(d)cosh(d)|∇ψ|²
  Conservation: div(e^σ sinh²(d) ∇ψ) = 0

3. BASE CONFORMAL: Δλ = (|∇σ|² - e_{H²})/4 where e_{H²} = H²-energy of orbit map.

4. TWIST VANISHING: For commuting Killing fields on Ric=-3g, twist scalars are constant. Reflection reverses orientation ⟹ twist = 0 on exact reflected cores.

5. VII_0 SPECIALIZATION: Setting ψ=kz, d=d(r), the d-equation becomes (e^σ d')' = e^σ sinh(d)cosh(d)k², whose RHS is always positive. This is the VII_0 barrier mechanism.

6. STEP 73 RECOVERY: On the cusp background with diagonal orbit (α=v, β=0), the orbit equation gives v_rr + 3v_r + e^{-2r}v_zz = 0, recovering Step 73.

Verify each component. Check whether the coefficient in the area equation is 6 (not 3). Check whether the orbit equation is exactly a weighted harmonic map. Check the conservation law. Does the mechanism analysis correctly identify that general 2-variable H² maps can break the VII_0 barrier through angular momentum absorption by the growing weight e^σ? Are there additional conservation laws or monotonicity constraints in the coupled system that could prevent this?

## Output

## Scientific verification memo

Let
\[
\rho=e^\sigma=\sqrt{\det G},\qquad
A_i=G^{-1}\partial_iG=\sigma_i I+B_i,\qquad
B_i=M^{-1}\partial_iM,
\]
where \(i\in\{r,z\}\) and \(\operatorname{tr}B_i=0\).

For the block metric
\[
g=e^{2\lambda}(dr^2+dz^2)+G_{ab}\,d\xi^a d\xi^b,
\]
the orbit-orbit Ricci endomorphism is
\[
(\operatorname{Ric}_g)^a{}_b
=-\frac{e^{-2\lambda}}{2\rho}
\partial_i\!\left(\rho A_i\right)^a{}_b.
\tag{1}
\]
Thus \(\operatorname{Ric}=-3g\) is equivalent in the orbit block to
\[
\partial_i(\rho A_i)=6e^{2\lambda}\rho I.
\tag{2}
\]

### 1. Area equation and the coefficient \(6\)

Taking the matrix trace of (2), using
\[
\operatorname{tr}A_i=2\sigma_i,\qquad
\partial_i(\rho\sigma_i)=\Delta\rho,
\]
gives
\[
2\Delta\rho=12e^{2\lambda}\rho.
\]
Hence
\[
\boxed{\Delta\rho=6e^{2\lambda}\rho}
\]
and, since \(\rho=e^\sigma\),
\[
\boxed{\Delta\sigma+|\nabla\sigma|^2=6e^{2\lambda}}.
\]

The coefficient is therefore **\(6\), not \(3\)**. In general it is \(-2\Lambda\) when \(\operatorname{Ric}=\Lambda g\).

The round cusp confirms it directly: with \(t=-e^{-r}\),
\[
\lambda=-\log(-t),\qquad \sigma=-2\log(-t),
\]
so
\[
\sigma_{tt}+\sigma_t^2=\frac{2}{t^2}+\frac{4}{t^2}
=\frac6{t^2}=6e^{2\lambda}.
\]

### 2. Orbit map equation

Subtracting the scalar part of (2) leaves
\[
\boxed{\partial_i\!\left(\rho M^{-1}\partial_iM\right)=0.}
\tag{3}
\]
Because the base has dimension two and is in conformal gauge, this flat divergence is equivalent to the divergence formed using \(e^{2\lambda}(dr^2+dz^2)\).

Equip the symmetric-space model with
\[
\langle V,W\rangle_M
=\frac12\operatorname{tr}(M^{-1}VM^{-1}W).
\tag{4}
\]
Then
\[
q_{ij}:=\langle\partial_iM,\partial_jM\rangle
=\frac12\operatorname{tr}(B_iB_j),
\]
and (3) is precisely the Euler–Lagrange equation of
\[
\frac12\int \rho\,|dM|_{H^2}^2\,dr\,dz.
\]
It is therefore the weighted harmonic-map equation into
\[
H^2=SL(2,\mathbb R)/SO(2).
\]

In geodesic polar coordinates
\[
ds_{H^2}^2=dd^2+\sinh^2d\,d\psi^2,
\]
the equations are
\[
\boxed{
\partial_r(\rho d_r)+\partial_z(\rho d_z)
=\rho\sinh d\cosh d\,
(\psi_r^2+\psi_z^2)
}
\tag{5}
\]
and
\[
\boxed{
\partial_r(\rho\sinh^2d\,\psi_r)
+\partial_z(\rho\sinh^2d\,\psi_z)=0.
}
\tag{6}
\]
Thus the polar equations and angular conservation law are correct.

There is one sign error in the supplied Iwasawa formula. For
\[
ds_{H^2}^2=d\alpha^2+e^{-2\alpha}d\beta^2,
\]
the correct equations are
\[
\boxed{
\operatorname{div}(\rho\nabla\alpha)
=-\rho e^{-2\alpha}|\nabla\beta|^2,
}
\tag{7}
\]
\[
\boxed{
\operatorname{div}(\rho e^{-2\alpha}\nabla\beta)=0.
}
\tag{8}
\]
The right side of Step 79 equation (4.6) should have a minus sign. This does not affect the diagonal specialization \(\beta=0\).

### 3. Base conformal factor

The base-base Ricci tensor is
\[
\operatorname{Ric}_{ij}
=-\Delta\lambda\,\delta_{ij}
-\nabla_i^h\nabla_j^h\sigma
-\frac14\operatorname{tr}(A_iA_j).
\tag{9}
\]
Since
\[
\frac14\operatorname{tr}(A_iA_j)
=\frac12\sigma_i\sigma_j+\frac12q_{ij},
\]
taking the flat trace of (9) gives
\[
-2\Delta\lambda-\Delta\sigma
-\frac12\bigl(|\nabla\sigma|^2+e_{H^2}\bigr)
=-6e^{2\lambda},
\tag{10}
\]
where
\[
e_{H^2}=q_{rr}+q_{zz}
=\frac12\operatorname{tr}(B_r^2+B_z^2).
\]
Substitution of the area equation yields
\[
\boxed{
\Delta\lambda
=\frac{|\nabla\sigma|^2-e_{H^2}}4.
}
\tag{11}
\]
Thus item 3 is correct with the normalization
\[
e_{H^2}=|dM|_{H^2}^2,
\]
rather than one half of that quantity.

For completeness, the two traceless base equations are
\[
\begin{aligned}
\sigma_{rr}-\sigma_{zz}
={}&2(\lambda_r\sigma_r-\lambda_z\sigma_z)
-\frac12(\sigma_r^2-\sigma_z^2)
-\frac12(q_{rr}-q_{zz}),
\\
\sigma_{rz}
={}&\lambda_z\sigma_r+\lambda_r\sigma_z
-\frac12\sigma_r\sigma_z-\frac12q_{rz}.
\end{aligned}
\tag{12}
\]
The displayed cross equation in Step 79 agrees with the second equation when its notation \(e_{H^2,rz}\) means \(q_{rz}\).

### 4. Twist vanishing

For a Killing field \(X\), define its twist one-form
\[
\omega_X=*(X^\flat\wedge dX^\flat).
\]
The Killing identity gives
\[
d\omega_X=2*\bigl(X^\flat\wedge\operatorname{Ric}(X)^\flat\bigr).
\]
If \(\operatorname{Ric}=-3g\), then \(\operatorname{Ric}(X)^\flat=-3X^\flat\), so
\[
d\omega_X=0.
\]
For a commuting Killing field \(Y\),
\[
c_X=\iota_Y\omega_X
=*(X^\flat\wedge Y^\flat\wedge dX^\flat)
\]
satisfies
\[
dc_X=\mathcal L_Y\omega_X-\iota_Yd\omega_X=0.
\]
Similarly \(dc_Y=0\).

An isometric reflection fixing a hypersurface pointwise reverses orientation and preserves the tangent \(T^2\) generators. Therefore it changes the sign of the Hodge star while leaving the remaining factors unchanged:
\[
c_X\circ\mathcal R=-c_X,\qquad c_Y\circ\mathcal R=-c_Y.
\]
At the fixed hypersurface this gives \(c_X=c_Y=0\), and constancy extends this throughout the connected core. Where the two Killing fields are independent, these two equalities give orthogonal transitivity.

Item 4 is therefore correct under the stated reflection symmetry preserving the \(T^2\) action.

### 5. VII\(_0\) specialization

For the abstract polar ansatz
\[
d=d(r),\qquad \psi=kz,\qquad \sigma=\sigma(r),
\]
equation (5) becomes
\[
\boxed{
(e^\sigma d')'
=e^\sigma\sinh d\cosh d\,k^2.
}
\tag{13}
\]
For \(k\ne0\) and \(d>0\), the right side is strictly positive. With reflected data \(d'(0)=0\), this implies
\[
e^\sigma d'>0,\qquad d'>0
\]
for \(r>0\). This is exactly the one-way radial mechanism used in the VII\(_0\) argument.

There is a factor-of-two convention when comparing (13) with the Step 78 coframe. If
\[
M=R(kz)\begin{pmatrix}e^d&0\\0&e^{-d}\end{pmatrix}R(kz)^T,
\]
then
\[
\frac12\operatorname{tr}(B_z^2)=4k^2\sinh^2d.
\]
The standard polar angle is therefore
\[
\psi=2kz.
\]
Consequently, using the same \(k\) as Step 78, the right side of (13) is
\[
4e^\sigma k^2\sinh d\cosh d.
\]
The qualitative mechanism is unchanged, but “\(\psi=kz\)” implicitly redefines the VII\(_0\) frequency by a factor of two.

### 6. Recovery of Step 73

Set
\[
t=-e^{-r},\qquad
\lambda=-\log(-t),\qquad
\rho=e^\sigma=N^{-2}e^{2r}=N^{-2}t^{-2},
\]
and take
\[
M=\operatorname{diag}(e^v,e^{-v}),
\qquad \alpha=v,\quad \beta=0.
\]
The orbit equation is
\[
\partial_t(\rho v_t)+\partial_z(\rho v_z)=0.
\]
Using
\[
\partial_t=e^r\partial_r
\]
gives
\[
e^{4r}(v_{rr}+3v_r)+e^{2r}v_{zz}=0,
\]
hence
\[
\boxed{
v_{rr}+3v_r+e^{-2r}v_{zz}=0.
}
\tag{14}
\]
For \(v=f(r)\cos(kz)\), this becomes
\[
f''+3f'-k^2e^{-2r}f=0.
\]
Item 6 is correct.

## The proposed angular-relaxation mechanism

The full two-variable system certainly escapes the specific Step 78 invariant-region proof: \(\psi\) need not equal a fixed linear function of \(z\), and \(d_r\) need not have one sign at every point. However, the stronger statement that growth of \(e^\sigma\) forces \(\psi_z\) to decay does **not** follow from (6).

Write
\[
J_r=\rho\sinh^2d\,\psi_r,\qquad
J_z=\rho\sinh^2d\,\psi_z.
\]
Equation (6) says only
\[
\partial_rJ_r+\partial_zJ_z=0.
\]
On a periodic \(z\)-circle,
\[
\frac d{dr}\int J_r\,dz=0.
\tag{15}
\]
It gives no conservation equation for \(\int J_z\,dz\). In particular, the Step 79 formula
\[
\frac d{dr}\int J_z\,dz
=-\int(\partial_zJ_z)\psi_z\,dz
\]
does not follow from the harmonic-map equation.

The helicoidal example itself demonstrates the point:
\[
J_r=0,\qquad
J_z=\rho\sinh^2d\,k.
\]
This satisfies \(\partial_rJ_r+\partial_zJ_z=0\) for arbitrary \(r\)-dependence of \(J_z\). Thus current conservation does not require the growing weight to reduce \(\psi_z\).

There are three further exact structures relevant to a reflected connector.

### A. All \(SL(2,\mathbb R)\) radial currents vanish in mean

The matrix equation gives
\[
\mathcal Q(r):=\int_{S^1}\rho M^{-1}M_r\,dz,
\qquad
\mathcal Q'(r)=0.
\tag{16}
\]
Reflection gives \(M_r(0,z)=0\), hence
\[
\boxed{\mathcal Q(r)\equiv0.}
\tag{17}
\]
The angular current is only one component of this matrix-valued conservation law.

### B. Convex-distance maximum principle

Fix \(P\in H^2\), and let
\[
F(U)=\frac12\operatorname{dist}_{H^2}(U,P)^2,
\qquad U=(d,\psi).
\]
For a weighted harmonic map,
\[
\rho^{-1}\operatorname{div}(\rho\nabla(F\circ U))
=\operatorname{Hess}_{H^2}F(dU,dU).
\]
Since \(H^2\) has curvature \(-1\),
\[
\operatorname{Hess}F\ge g_{H^2},
\]
and therefore
\[
\boxed{
\operatorname{div}(\rho\nabla(F\circ U))
\ge \rho |dU|^2.
}
\tag{18}
\]

On a finite periodic cylinder with reflected inner face \(U_r=0\), this implies
\[
\sup_{\text{cylinder}}F
\le \sup_{\text{outer face}}F.
\tag{19}
\]
In particular, if the outer map is exactly the constant \(P\), then
\[
\boxed{U\equiv P.}
\tag{20}
\]
If the outer map approaches \(P\) uniformly, then the whole exact reflected cylinder approaches \(P\) uniformly. Thus an exact order-one orbit displacement at the reflected center cannot relax to a uniformly constant orbit map at the outer face.

This does not rule out large orbit-map derivatives with small amplitude, nor does it directly treat approximate Einstein sequences.

For
\[
E=\operatorname{Ric}+3g,
\]
the orbit equation becomes
\[
\partial_i(\rho B_i)
=-2e^{2\lambda}\rho\,E^\circ_{\rm orbit}.
\tag{21}
\]
On a long expanding connector, the geometric multiplier \(e^{2\lambda}\rho\) can make the accumulated forcing substantial even when \(\|E\|_\infty\) is small. A quantitative estimate therefore requires weighted control of this source, not merely its pointwise norm.

### C. Area and stress balances

Reflection gives \(\rho_r(0,z)=0\). Integrating the area equation around the circle yields
\[
\frac d{dr}\int_{S^1}\rho_r\,dz
=6\int_{S^1}e^{2\lambda}\rho\,dz>0.
\tag{22}
\]
Thus the mean outward area flux increases, although this does not imply \(\rho_r>0\) pointwise.

The harmonic-map stress tensor
\[
T_{ij}=q_{ij}-\frac12\delta_{ij}e_{H^2}
\]
obeys
\[
\boxed{
\partial_i(\rho T_{ij})
=-\frac12e_{H^2}\,\partial_j\rho.
}
\tag{23}
\]
If \(\rho_r\ge0\) pointwise, then
\[
\frac d{dr}\int\rho T_{rr}\,dz
=-\frac12\int \rho_r e_{H^2}\,dz\le0.
\tag{24}
\]
The area equation supplies mean growth, not the pointwise sign needed for this monotonicity.

## Overall assessment

Items 1–4 and 6 are correct. Item 5 is correct after distinguishing the abstract polar frequency from the Step 78 coframe frequency. The Iwasawa \(\alpha\)-equation in Step 79 has the wrong sign.

General two-variable maps remove the fixed-helicoid ODE structure, so the Step 78 pointwise invariant-region argument does not extend automatically. Yet “angular momentum absorption by \(e^\sigma\)” is not established by the conservation law. The exact system retains matrix-valued radial currents, convex-distance subharmonicity, area-flux growth, and the weighted stress balance. In particular, exact reflected data together with a constant outer orbit map force the orbit map to be constant. The remaining mathematical possibility is an approximate, long, geometrically weighted connector for which the forcing in (21) accumulates while the pointwise Ricci defect tends to zero; the supplied material contains no construction or quantitative weighted estimate resolving that possibility.