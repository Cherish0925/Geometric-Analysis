# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 23,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step23_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step23_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematical synthesis joining the exact-CH conformal infimum equality, the corrected mu>2 normalized class, the peer CR-pinning identity/Lemma P, and the exact CH exterior response. Determine exactly what is proved, what still depends on decay/noncollapse/shadowing, and whether CR pinning and the exterior null-line response can be interpreted as components of one terminal map without conflating variables or normalizations. Also read the Arb diagnosis and assess the proposed local-basis certification repair.

## Integrated Scientific Memo

# Verification memo

## 1. Correct theorem obtained from the exact-CH conformal reduction

Let
\[
m_*:=2+2\sqrt3\approx 5.4641.
\]
For a smooth complete four-dimensional cell with one marked exact normalized \(\mathbf{CH}^2\) end and compact complement, the supplied argument proves:

1. There is a unique positive \(u\to1\) satisfying
   \[
   -6\Delta_gu+s_gu+24u^3=0.
   \]
   Hence \(\widehat g=u^2g\) is complete and \(s_{\widehat g}=-24\).

2. For every \(m<m_*\),
   \[
   |\nabla^k(u-1)|=O(e^{-mr})
   \]
   for every fixed \(k\).

3. Choosing \(4<m<m_*\) removes all linear end terms and gives
   \[
   P(g)-P(\widehat g)
   =24\int|\nabla u|^2+3\int\left(\frac{\Delta u}{u}\right)^2,
   \]
   and
   \[
   J_6(g)-J_6(\widehat g)
   =
   24\int|\nabla u|^2
   +3\int\left(\frac{\Delta u}{u}\right)^2
   +\frac14\int(s_g+24)^2.
   \]
   The final quadratic integrals require only decay \(>2\); the stronger \(>4\) rate is needed specifically for the integration-by-parts flux and the linear Chern–Gauss–Bonnet transgression.

The barrier signs, uniqueness argument, indicial root, and coefficients in these identities check out. The scalar-square comparison must be understood on common truncations before taking the limit, since the separate \(\int s^2\) terms need not be finite.

In particular, \(\widehat g\) is the unique end-normalized minimizer of \(P\) in its conformal class whenever the comparison conformal factor has enough decay to remove the boundary terms.

---

## 2. Correction to the normalized decay class

Define
\[
a=\inf_{{\cal C}_{\mathrm{exact}}}P,\qquad
b=\inf_{{\cal C}_{\mathrm{exact}}}J_6,\qquad
c_\mu=\inf_{{\cal C}^{\mathrm{aCH},\mu}_{-24}}P.
\]

The source proves unconditionally
\[
\boxed{a=b.}
\]

Indeed, \(P\le J_6\) gives \(a\le b\). Conversely, normalize any exact-ended \(g\) to \(\widehat g\), then truncate its conformal factor to one. The resulting exact-ended metrics satisfy
\[
J_6(g_R)\to P(\widehat g)\le P(g),
\]
so \(b\le a\).

For an \(s=-24\) metric with
\[
h-g_{\mathrm{CH}}=O(e^{-\mu r})
\]
in sufficiently many derivatives, fixed-width splicing to exact CH produces squared residual
\[
O(e^{(4-2\mu)R}).
\]
Thus, for every \(\mu>2\),
\[
a=b\le c_\mu.
\]

The reverse inequality supplied by conformal normalization is available only when the normalized image belongs to the chosen class. The established decay is \(m<m_*\), so for
\[
2<\mu<m_*
\]
one can choose \(\mu<m<m_*\), obtaining \(c_\mu\le a\). Therefore the exact result supported by the material is
\[
\boxed{
\inf_{{\cal C}_{\mathrm{exact}}}P
=
\inf_{{\cal C}_{\mathrm{exact}}}J_6
=
\inf_{{\cal C}^{\mathrm{aCH},\mu}_{-24}}P,
\qquad 2<\mu<2+2\sqrt3 .
}
\]

The claim “for every fixed \(\mu>2\)” is not proved. Class inclusion does not repair the argument: if \(\mu_2>\mu_1\), then
\[
{\cal C}^{\mu_2}\subset{\cal C}^{\mu_1},
\qquad c_{\mu_2}\ge c_{\mu_1},
\]
which is the already-known direction.

Extending equality to arbitrary \(\mu>2\) would require additional input, such as a scalar-curvature-preserving annular gluing theorem or a proof that near-minimizers can be made scalar \(-24\) and exact CH outside a compact set with negligible change in \(P\).

The observed tail \(r e^{-4r}\) belongs to \(O(e^{-\mu r})\) precisely for every \(\mu<4\), not for \(\mu=4\). Thus a natural class explicitly containing that tail has
\[
2<\mu<4.
\]

---

## 3. CR-pinning identity and Lemma P

For a diagonal Bianchi-IX metric, write
\[
\widetilde\Phi
=q+\frac14(y_g-y_h)-\zeta\sinh q,
\qquad e_i=\operatorname{Ric}_{ii}+6.
\]
The supplied dynamical equations and curvature potentials give exactly
\[
\boxed{
\widetilde\Phi'
=
\zeta^2G_{\mathrm{drift}}
-\frac14(e_g-e_h)
=
\zeta^2G_{\mathrm{drift}}
-\frac14(\operatorname{Ric}^{\circ}_{gg}-\operatorname{Ric}^{\circ}_{hh}).
}
\]
The potentials in `cr_pinning_check.py` agree with the standard diagonal Bianchi-IX Ricci formula, so this is not merely a check on CH and real hyperbolic examples.

The norm estimate is also correct:
\[
P=2\pi^2\int W|\operatorname{Ric}^{\circ}|^2dt
\ge \pi^2\int W(e_g-e_h)^2dt.
\]
Since \(P=8\pi^2\widehat P\), weighted Cauchy–Schwarz yields
\[
\boxed{
\left|
\widetilde\Phi(T_1)-\widetilde\Phi(T_0)
-\int_{T_0}^{T_1}\zeta^2G_{\mathrm{drift}}\,dt
\right|
\le
\left(\frac{\widehat P_{[T_0,T_1]}}2\right)^{1/2}
\left(\int_{T_0}^{T_1}\frac{dt}{W}\right)^{1/2}.
}
\]

If
\[
W\ge \frac c{16}e^{4t}
\]
and the full tail remains in a validated ACH block in which the drift integral is bounded by \(\varepsilon_{\rm drift}(T)\), then
\[
\boxed{
\widehat P_{[T,\infty)}
\ge
\frac c2 e^{4T}
\bigl(|\widetilde\Phi(T)|-\varepsilon_{\rm drift}(T)\bigr)_+^2.
}
\]

This corollary is conditional on both:

- a lower bound on orbit volume;
- retention of the trajectory in a block controlling all variables entering \(G_{\mathrm{drift}}\).

Small \(\zeta\) or bounded \(q\) alone is insufficient. The script verifies the identity, but the numerical bounds such as \(\sup|G_{\mathrm{drift}}|\le7.354\) depend on the separate block certification.

---

## 4. Relation to the exact CH exterior response

To avoid the multiple incompatible uses of \(G\), write the Step-19 quantities as
\[
\omega=\frac{v_-}{f_-},\qquad
\Gamma(x)=\int_x^\infty f_-^2\,ds,\qquad
\varpi(x)=\frac{x^3}{4(1+x)^4},
\]
with
\[
x=\sinh^2t,\qquad
k(x)=\left(\frac{x}{1+x}\right)^2.
\]

The torsion relation is
\[
(k\theta)'=\frac12 f_-^2\omega.
\]
For entrance data
\[
\theta(\rho)=\Theta,\qquad \omega(\rho)=\omega_0
\]
and terminal condition \(\theta(\infty)=0\), define
\[
\delta=-2k(\rho)\Theta-\omega_0\Gamma(\rho).
\]
Then
\[
\int_\rho^\infty \Gamma\,\omega'\,dx=\delta,
\]
and weighted Cauchy–Schwarz gives the exact linear value function
\[
\boxed{
E_{\mathrm{ext}}(\rho;\omega_0,\Theta)
=
\frac{\delta^2}{I(\rho)},\qquad
I(\rho)=\int_\rho^\infty\frac{\Gamma^2}{\varpi}\,dx.
}
\]
The null line \(\delta=0\) is the Einstein mass mode.

If the entrance data are instead continued outward by the zero-cost linear Einstein solution, its conformal-infinity contact-plane squashing is
\[
C_{\mathrm{CR}}^{\mathrm{int}}
=
k(\rho)\Theta+\frac12\omega_0\Gamma(\rho)
=
-\frac{\delta}{2}.
\]
Thus
\[
E_{\mathrm{ext}}
=
\frac{4(C_{\mathrm{CR}}^{\mathrm{int}})^2}{I(\rho)}.
\]
Since
\[
\Gamma(x)\sim\frac1{2x^2},\qquad
I(x)\sim\frac1{2x^2},\qquad
x\sim\frac14e^{2T},
\]
one obtains
\[
E_{\mathrm{ext}}
\sim \frac12 e^{4T}(C_{\mathrm{CR}}^{\mathrm{int}})^2.
\]
This is exactly the sharp asymptotic constant in Lemma P.

### Correct terminal-map interpretation

CR pinning and the exterior null-line response can be organized as parts of one terminal formalism, but they are not independent penalized coordinates.

A suitable terminal port is the finite-radius state and first jet,
\[
{\cal T}_T(g)=\bigl(g|_{S_T},\nabla_\nu g|_{S_T}\bigr).
\]
In the linear diagonal antisymmetric sector this reduces to \((\Theta,\omega_0)\). From that port one forms:

- the mass-mode coordinate, tangent to the null line and carrying zero quadratic exterior cost;
- the Rossi/CR mismatch
  \[
  C_{\mathrm{CR}}^{\mathrm{int}}=-\delta/2,
  \]
  which is the penalized coordinate.

The corrected nonlinear observable is
\[
\widetilde\Phi(T)+\int_T^\infty\zeta^2G_{\mathrm{drift}}\,dt.
\]
Its linearization at CH is the same \(C_{\mathrm{CR}}^{\mathrm{int}}\). Therefore:

- Step 19 gives the exact quadratic Dirichlet-to-Neumann value function near CH;
- Lemma P gives a nonlinear lower estimate for the same CR mismatch while the tail remains in a controlled ACH block.

One must not add \(\delta^2/I\) and the CR-pinning lower bound as separate terminal penalties; that would double-count the same antisymmetric channel. It is nevertheless legitimate to retain both the full port \((\Theta,\omega_0)\) and its derived CR projection in a terminal map, provided the latter is identified as a function of the former rather than a new independent variable.

The exterior costate
\[
\lambda=-\delta/I
\]
is conjugate to the penalized CR coordinate. It is not the Rossi parameter, not the mass amplitude, and not the Einstein constant.

This synthesis is currently restricted to the diagonal antisymmetric sector. No supplied analogue of \(\widetilde\Phi\) controls general nondiagonal angular CR deformation.

---

## 5. Exact status of compactness and attainment claims

### Established from the supplied material

- Exact-CH conformal normalization, uniqueness, and decay \(m<m_*\).
- The two conformal energy identities.
- Equality \(\inf_{\mathrm{exact}}P=\inf_{\mathrm{exact}}J_6\).
- Equality with the scalar-\(-24\) class for \(2<\mu<m_*\).
- CR-pinning identity and Lemma P.
- Corollary P1 under its volume and block hypotheses.
- Exact linear exterior value function and null line.
- Identification \(\delta=-2C_{\mathrm{CR}}^{\mathrm{int}}\).

### Still dependent on decay or truncation

A complete finite-\(P\), scalar-\(-24\) tail does not automatically have pointwise \(C^2\) decay \(O(e^{-\mu r})\). The proposed truncation lemma still needs:

- precise removal/matching of the rate-\(2\) radial-origin or CH-scale mode;
- pointwise control of the forced stable modes from weighted \(L^2\) curvature control;
- enough decay to show cutoff cost tends to zero.

This is distinct from the proved truncation of the specific normalized images of exact-ended metrics.

### Still dependent on noncollapse

Attainment of the diagonal infimum requires compactness assumptions excluding:

- collapsed connectors;
- large bolts;
- non-Euclidean interior necks or orbit collapse.

CR pinning alone does not rule these out because its strength comes from large orbit volume.

### Still dependent on shadowing and a validated face portrait

Lemma P controls one CR projection, not the entire dynamical state. Excluding a large-volume excursion away from the ACH curve and back to the exact CH end requires:

- weighted control of all relevant state equations;
- a quantitative shadowing or pseudo-orbit theorem;
- a rigorous no-return statement for the conformal-infinity face flow.

The cited unstable-face fates are numerical, not yet a validated global phase portrait. Consequently, the conditional structure/attainment theorem remains conditional.

Likewise, \(\delta^2/I\) is a global terminal cost only for traces already in the CH linear regime. A lower theorem for arbitrary exterior traces still needs a nonlinear mechanism bringing them into that regime or a nonlinear exterior value function.

---

## 6. Arb diagnosis and certification repair

The supplied JSON establishes that the chosen equal complex boxes fail completely:

- all 32 boxes have nonfinite volume and Ricci enclosures;
- the lapse-related \(G\) and \(GH\) channels fail denominator separation throughout;
- failure occurs across the interval, not at one isolated physical subinterval.

It does **not** establish a genuine complex singularity of the metric profile. The diagnostic uses a comparatively large square complex enlargement and evaluates globally parameterized high-degree expressions directly. Moreover, different channels behave very differently: \(FH\) is often reasonably narrow while \(G\) and \(GH\) are enormous. Thus “generic Chebyshev complex growth” is only part of the diagnosis; the lapse/bolt-adapted representation and cancellation structure are specifically implicated.

The proposed local-basis repair is mathematically appropriate, provided it contains the following elements.

1. **Preserve the same profile.**  
   Re-expand the existing global polynomial exactly, or with a rigorous local remainder. Independently fitting each cell would define a new metric unless matching conditions are certified.

2. **Use geometry-adapted subdomains.**  
   Partition in physical radius, logarithmic \(x\), or \(t=\operatorname{arsinh}\sqrt{x}\), rather than uniform global spectral coordinates over the entire scale range.

3. **Factor bolt behavior analytically.**  
   Remove known zeros and removable singular factors before interval evaluation. Near-bolt wrapping will not necessarily be cured by subdivision alone.

4. **Certify derivatives through second order.**  
   Ricci depends on first and second derivatives, so local Taylor/Chebyshev enclosures must propagate rigorous derivative bounds.

5. **Separate real positivity from complex analyticity.**  
   Metric validity needs real-axis lower bounds for \(F,G,e^w\). Complex zero exclusion is additionally necessary only if using a complex-ellipse quadrature theorem. A real Taylor-model quadrature can avoid that requirement.

6. **Subtract the CH background in the far field.**  
   Evaluate curvature residuals as linear and quadratic expressions in small perturbations, rather than by subtracting large \(O(1)\) curvature terms. This is essential where the physical residual is tiny.

7. **Propagate remainder bounds to the integrated energy.**  
   The certificate must enclose the complete squared residual times volume, including transcendental compositions and all local remainder terms.

8. **Optionally replace the far tail by the transparent boundary form.**  
   Once a rigorously verified trace lies in a controlled linear neighborhood, the explicit \(\delta^2/I\) tail can replace direct long-range quadrature, with a separately bounded nonlinear remainder. It cannot be used without such a linear-regime certificate.

Hence the local low-degree Chebyshev/Taylor strategy is a valid repair direction, but no rigorous \(X=256\) energy bound follows from the current diagnostic. The previously certified shorter-cell value remains the rigorous transfer input; the improved long-cell numbers remain floating-point evidence.

---

## Final corrected synthesis

The conformal theorem rigorously removes the scalar channel and identifies the exact-ended \(P\)- and \(J_6\)-infima. Its presently justified scalar-\(-24\) reformulation uses
\[
2<\mu<2+2\sqrt3,
\]
not arbitrary \(\mu>2\). CR pinning and the exact CH exterior response describe the same asymptotic Rossi/CR mismatch at nonlinear-inequality and linear-exact levels, respectively; the mass direction is the exterior null coordinate. They can therefore be components of one terminal-state formalism, but their penalties must not be added independently.

What prevents a full diagonal compactness or gap theorem is not this terminal-coordinate identification. The remaining obstacles are the truncation/decay theorem for general finite-energy tails, quantitative shadowing and rigorous no-return dynamics, and the unresolved collapse and large-bolt regimes.