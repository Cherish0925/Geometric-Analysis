# TTCS Independent Branch Record

```json
{
  "step_id": 79,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step79_angular_rho_and_tilt_repair.md",
    "Sessions/S0910A01/workspace/data/step79_angular_rho_verify.json",
    "Sessions/S0910A01/workspace/data/step79_tilt_linearization.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md"
  ]
}
```

## Task

Verify the Step 79 mathematical repair of the positive mixed-row product-orbifold obstruction problem. Read the repair note plus the two data files and the relevant Ozuch source excerpts. Check: (1) whether Ozuch's rho_x dependence invalidates the Step 78 fixed-rho rank-one/block-diagonal conclusions; (2) whether the factor-traceless bare scalar-decoupling theorem survives for zeta in span{omega2,omega3}; (3) whether the tilt linearization D_phi lambda=(0,c Lambda a,0) at phi0=omega2 is correctly interpreted as making mu2 adjustable and leaving the cokernel component as the actual second-order local condition; (4) whether the response to A02's r=0 KE-control argument is mathematically sound or too strong. Give a direct scientific memo with corrections and next computation priorities.

## Output

## Scientific memo: Step 79 repair

### Overall assessment

The angular correction is mathematically necessary, the factor-trace identity is exact, and the tilt calculation has the right finite-dimensional interpretation. Two refinements are important:

1. For \(R=\operatorname{diag}(\Lambda,0,0)\), \(\operatorname{coker}D_\phi\lambda\) is two-dimensional, spanned by components \(k=1,3\). Ozuch’s determinant formula removes the \(k=1\) component at this product rank-one block, leaving \(k=3\) as the undetermined local scalar.
2. If orbifold deformation variables satisfy \(v(t)=t\,w+o(t)\), the relevant quotient uses the image of the full derivative \(D_{(\phi,v,\ldots)}\lambda\), not only \(D_\phi\lambda\).

The assertion that a Kähler–Einstein control family forces all three \(\mu_k\) to vanish does not follow without information on the first jet of that family in Ozuch’s gluing coordinates.

---

## 1. Angular \(\rho_x\) dependence

Ozuch Definition 1.14 and Remark 1.15 give
\[
\rho_x(\zeta)_j=\frac{x^T(\zeta^+\circ\omega_j^-)x}{|x|^2},
\]
with \(\rho_x\) given by quaternionic conjugation. Hence, for fixed \(\zeta\neq0\),
\[
|\rho_x(\zeta)|=|\zeta|,
\]
and the map \(S^3\to S^2\), \(x\mapsto \rho_x(\zeta)/|\zeta|\), is surjective.

For the product curvature block
\[
R^-=\operatorname{diag}(\Lambda,0,0),
\]
one therefore has
\[
R^-\rho_x(\zeta)=\Lambda\,\rho_1(x,\zeta)\,e_1,
\]
which is generically nonzero even when \(\zeta\in\ker R^-\).

Likewise, Proposition 1.16 gives
\[
d_eR^-(H^4)
=\frac{12}{r^6}\left(\rho_x(\zeta)\rho_x(\zeta)^T
-\frac{|\zeta|^2}{3}I\right).
\]
Thus
\[
(d_eR^-)_{12}=\frac{12\rho_1\rho_2}{r^6},
\qquad
(d_eR^-)_{13}=\frac{12\rho_1\rho_3}{r^6},
\]
which are generically nonzero.

The exact sample in `step79_angular_rho_verify.json`,
\[
x=(0.4,0.8,-0.4,0.2),\qquad
\rho_x(\omega_2)=(0.48,0.36,0.8),
\]
gives
\[
R^-\rho_x=(0.48\Lambda,0,0),
\]
and, at \(r=1\),
\[
(d_eR^-)_{12}=12(0.48)(0.36)=2.0736,\qquad
(d_eR^-)_{13}=12(0.48)(0.8)=4.608.
\]

Therefore the Step 78 fixed-\(\rho\) conclusions concerning pointwise kernel membership and block-diagonal curvature variation are invalid. The numerical sample supports this, but the quaternionic rotation property already proves it.

A source-transcription detail is worth recording. The `object.md` sentence displaying
\[
\rho_{-x}=\rho_x^T=\rho_x^{-1}=\rho_x
\]
cannot hold literally for a generic rotation. Quaternionic conjugation gives
\[
\rho_{-x}=\rho_x,\qquad
\rho_{\bar x}=\rho_x^{-1}=\rho_x^T
\]
for unit \(x\). The displayed source line likely lost a bar during conversion. This distinction matters when later swapping interaction points.

---

## 2. Factor-traceless scalar decoupling

Let
\[
E=\operatorname{span}\{e_1,e_2\},\qquad
F=\operatorname{span}\{e_3,e_4\},
\]
be the tangent planes to the two \(S^2\) factors.

The six exact matrices in `step79_angular_rho_verify.json` prove that
\[
\operatorname{tr}_{E}(\eta^-\circ\zeta^+)
=
\operatorname{tr}_{F}(\eta^-\circ\zeta^+)=0
\]
for
\[
\zeta^+\in\operatorname{span}\{\omega_2^+,\omega_3^+\},
\qquad \eta^-\in\Lambda^-.
\]
Indeed, the only diagonal basis products are proportional to
\[
\operatorname{diag}(-1,1,-1,1)
\quad\text{or}\quad
\operatorname{diag}(-1,1,1,-1),
\]
and all other basis products have zero diagonal. Each factor trace is therefore zero; bilinearity gives the general statement.

Taking \(\eta^-=\rho_x(\zeta)^-\) yields, pointwise,
\[
\operatorname{tr}_{g_1}H^4
=
\operatorname{tr}_{g_2}H^4=0,
\qquad
H^4=-\frac{\rho_x(\zeta)^-\circ\zeta^+}{2r^4}.
\]
Consequently,
\[
\langle H^4,f\,g_1\rangle
=
\langle H^4,f\,g_2\rangle=0
\]
for every scalar function \(f\).

This is an exact algebraic theorem, not a numerical observation. It concerns the bare \(H^4\) tensor. It does not by itself determine the scalar projection of:

- cutoff and gauge-correction terms;
- \(Q^{(2)}(H^4,H_2)\) or later nonlinear sources;
- the global Green response;
- the invariant \(P\)-pseudo-inverse near the \(g_1-g_2\) mode.

A stronger global decoupling statement would require invariance of the relevant tensor subspace under the full gauge-fixed operator and an explicit projection of every source term.

---

## 3. Tilt linearization and the local second-order equation

Write
\[
R=\operatorname{diag}(\Lambda,0,0),\qquad
\phi_0=\omega_2,
\]
and use the adapted frame
\[
(\phi_{(1)},\phi_{(2)},\phi_{(3)})
=(\omega_2,\omega_1,\omega_3).
\]
For
\[
\phi(\varepsilon)
=
\frac{\omega_2+\varepsilon(a\omega_1+b\omega_3)}
{\sqrt{1+\varepsilon^2(a^2+b^2)}},
\]
one has
\[
R\phi(\varepsilon)
=
\frac{\Lambda a\varepsilon}
{\sqrt{1+\varepsilon^2(a^2+b^2)}}\,\omega_1.
\]
Using Ozuch’s formula
\[
\lambda_k=c\langle R\phi,\phi_{(k)}\rangle,
\]
the JSON series follows:
\[
\lambda_1=c\Lambda a^2\varepsilon^2+O(\varepsilon^4),
\]
\[
\lambda_2
=c\Lambda a\varepsilon
-c\Lambda\left(a^3+\frac12ab^2\right)\varepsilon^3
+O(\varepsilon^4),
\]
and, for the displayed smooth frame convention,
\[
\lambda_3=0.
\]
In particular,
\[
D_\phi\lambda_{\phi_0}(a,b)
=(0,c\Lambda a,0).
\]

Thus
\[
\operatorname{im}D_\phi\lambda
=\operatorname{span}\{e_{(2)}\},
\]
while the \(b\)-direction, tangent to the kernel circle of \(R\), is invisible at first order.

For a common small parameter \(t\),
\[
\phi(t)=\phi_0+t\psi+o(t),
\]
Ozuch’s equation becomes
\[
t\lambda(\phi(t))+t^2\mu(\phi(t))
=
t^2\bigl(D_\phi\lambda(\psi)+\mu(\phi_0)\bigr)+o(t^2).
\]
Hence the \(k=2\) equation is solved by
\[
a=-\frac{\mu_2}{c\Lambda}.
\]

The full cokernel is
\[
\operatorname{coker}D_\phi\lambda
\simeq \operatorname{span}\{e_{(1)},e_{(3)}\}.
\]
At \(\phi_0\), the restriction of \(R\) to \(\phi_0^\perp\) is
\[
\begin{pmatrix}\Lambda&0\\0&0\end{pmatrix},
\]
so the exact determinant formula in Ozuch Section 2.1.4 gives
\[
\mu_1=C\det
\begin{pmatrix}\Lambda&0\\0&0\end{pmatrix}=0.
\]
Therefore, after using this structural identity, the remaining local second-order scalar is \(\mu_3\).

Two assumptions should accompany this interpretation:

- Ozuch’s remainder \(O(t_{\max}^{5/2})\) is \(o(t_j^2)\) when the relevant scales are comparable. For highly disparate scales, that estimate alone does not isolate the coefficient of \(t_j^2\).
- At antipodally paired nodes, the required \(a\)-tilts must transform with the same signs as the transported obstruction frames. Equivariance should make this compatible, but the sign transport belongs in the paired reduced map.

Ozuch’s proof after equation (53) supports the general mechanism by allowing \(\phi_n-\phi_\infty=O(t+\|v\|)\). Its invertibility argument there assumes both transverse curvature eigenvalues are nonzero. The present rank-one case is different: only one transverse component is adjustable, exactly as the explicit derivative shows.

---

## 4. The Kähler–Einstein control family

Suppose an exact Kähler–Einstein family, when expressed in Ozuch coordinates, has
\[
\phi(t)=\phi_0+t\psi+o(t),\qquad
v(t)=t\,w+o(t).
\]
Then its order-\(t^2\) equation is
\[
D_\phi\lambda(\psi)
+D_v\lambda(w)
+\mu(\phi_0)=0.
\]
More generally, all parameters with order-\(t\) motion contribute through the full derivative of \(\lambda\).

Thus existence of the exact family implies
\[
[\mu]=0
\quad\text{in}\quad
\mathbb R^3/
\operatorname{im}D_{(\phi,v,\ldots)}\lambda.
\]
It does not imply \(\mu_1=\mu_2=\mu_3=0\) componentwise.

In the rank-one product model, with no order-\(t\) contribution from \(v\),

- the family can force the reduced \(k=1,3\) components to vanish;
- it can absorb \(\mu_2\) through an out-of-kernel tilt;
- it determines \(\mu_2=0\) only if its extracted coordinate satisfies
  \(\phi(t)=\phi_0+o(t)\), or if Kähler symmetry independently forces \(a=0\).

If \(D_v\lambda(w)\) has a \(k=3\) component, even the inference \(\mu_3=0\) requires incorporating \(v\) into the reduced derivative. Consequently, the Step 79 response to the stronger \(r=0\) assertion is mathematically sound, with the refinement that “quotient by \(D\lambda\)” should mean the derivative in all admissible order-\(t\) variables.

The useful missing object from the Kähler–Einstein family is its coordinate jet
\[
\bigl(\phi'(0),v'(0)\bigr)
\]
in Ozuch’s normalization. Kähler class periods, the local complex structure, and the normalized ALE chart may determine this jet.

---

## Computation priorities

1. **Exact angular local projection.**  
   Compute the \(\mathbf o_k\)-projections defining \(\mu_2(\phi_0)\) and \(\mu_3(\phi_0)\) using the full Hopf-angular field \(\rho_x\). Haar identities provide exact replacements for sampling:
   \[
   \int_{S^3}\rho_i\rho_j\,d\sigma
   =\frac{|\zeta|^2}{3}\delta_{ij},
   \]
   \[
   \int_{S^3}\rho_i\rho_j\rho_k\rho_l\,d\sigma
   =\frac{|\zeta|^4}{15}
   (\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}
   +\delta_{il}\delta_{jk}).
   \]

2. **Kähler-family coordinate jet.**  
   Determine whether the exact \(r=0\) family has \(a=0\), or instead realizes
   \[
   a=-\mu_2/(c\Lambda).
   \]
   This separates genuine coefficient vanishing from compensation by coordinate motion.

3. **Invariant product pseudo-inverse.**  
   Project the complete gauge-fixed source onto the even scalar sectors and the \(g_1-g_2\) mode. Bare factor-tracelessness removes direct \(H^4\) pairings but does not evaluate these later source projections.

4. **Third-order sliced map.**  
   After choosing \(a\), the order-\(t^3\) expression contains
   \[
   D_\phi\lambda(\psi^{(2)})
   +\frac12D_\phi^2\lambda(\psi^{(1)},\psi^{(1)})
   +D_\phi\mu(\psi^{(1)})
   +\sum_i\mathcal I_{ji}
   +\text{local third-order response}.
   \]
   In particular, the data already show a \(k=1\) contribution
   \[
   c\Lambda a^2
   \]
   from the quadratic tilt. Resolving this order requires a reduced expansion sharper than Ozuch’s current \(O(t^{5/2})\) remainder.

The repair therefore restores the correct angular geometry and the correct quotient interpretation of the second-order equation. It does not yet establish an Einstein metric on the mixed-row resolution; the decisive unresolved scalar is the projected \(\mu_3\), enlarged by any order-\(t\) orbifold deformation contribution.