# TTCS Independent Branch Record

```json
{
  "step_id": 89,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/notes/step87_resolvent_obstruction_theorem.md",
    "Sessions/S0910A03/workspace/data/step89_symbolic_twist_ricci.json",
    "Sessions/S0910A03/workspace/data/step89_corrected_twist_resolvent.json"
  ]
}
```

## Task

Verify the following corrected twist-Bochner computation for a free T²-invariant Einstein metric on a 4D manifold with base B², orbit metric G=ρM (detM=1), connection A, twist F=dA, and orbit-map U: B→H².

A symbolic Ricci computation for g=e^{2λ}(dr²+dz²)+e^{σ+α}(dξ₁+Pdz)²+e^{σ-α}dξ₂² gives:

1. Orbit twist Ricci: Ric_twist(ξ₁,ξ₁)/(G₁₁²f₁²) = 1/2, i.e., Ric^{twist}_{ab} = (1/2)G_{ac}G_{bd}f^cf^d. Here f^a = e^{-2λ}(∂_r A^a_z) is the twist scalar.

2. Base twist Ricci: Ric_twist(r,r)/(e^{2λ}Q) = -1, i.e., the base Ricci twist is -Qγ_B (NEGATIVE sign). Q = (1/2)G_{ab}f^af^b.

3. Area equation (orbit trace): G^{ab}Ric^{twist}_{ab} = Q, giving Lσ = 6+Q for exact Einstein with twist.

4. Orbit traceless equation (Einstein, diagonal M, f₂=0): Lα = Q, giving H² tension |S_F|² = Q².

5. Modified Bochner: Using Ric^σ = Ric_B - Hessσ = -(3+Q)γ + ½A + E_B and the standard weighted Bochner formula for maps to H² (target curvature gives +2detA):
  ½Le = |DdU|² + ½|dU(∇σ)|² + Q(A) - (3+Q)e + divσV - |S_F|²
where Q(A) = ½tr(A²)+2detA ≥ ½e², giving the subsolution:
  ½Le ≥ ½e(e - 6 - 2Q) + divσV - Q²

6. The separator floor from Step 88 is STRENGTHENED by twist: ⟨e_s⟩ ≥ 12+2⟨Q⟩-8δ, because |II|² includes a term ≥Q from the connection's normal derivative.

A previous TTCS generator (Step 88) incorrectly claimed base twist = +Qγ (favorable). The correct sign -Qγ makes the Bochner reaction WEAKER with twist. Combined with the separator floor strengthening, the threshold for exact connectors is Q*≈0.77.

Verify: (a) the 1/2 factor in orbit twist Ricci, (b) the NEGATIVE sign in base twist Ricci, (c) the area equation Lσ=6+Q, (d) the Bochner subsolution ½e(e-6-2Q)-Q², (e) the massive resolvent with κ=6+2Q giving a ceiling that exceeds the floor 12+2Q at Q≈0.77.

## Output

# Scientific verification memo

## Main finding

Items (a)–(c) and the separator estimate are correct. The direct base twist contribution is indeed \(-\mathcal Q\gamma_B\), where
\[
\mathcal Q:=\frac12G_{ab}f^af^b.
\]
However, moving this term through the horizontal Einstein equation changes its sign. Consequently,
\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=(-3+\mathcal Q)\gamma_B
+\frac12d\sigma^2+\frac12U^*h_{\mathbb H^2},
\]
not \(-(3+\mathcal Q)\gamma_B+\cdots\). The proposed Bochner reaction and the mass \(\kappa=6+2\mathcal Q\) therefore do not follow from the symbolic Ricci computation.

The corrected exact Bochner inequality is
\[
\boxed{
\frac12Le\ge
\frac12e(e-6+2\mathcal Q)
+\operatorname{div}_\sigma V-\mathcal Q^2.}
\]

---

## 1. Direct verification of the twist Ricci terms

Write
\[
F^a=f^a\,\mathrm{vol}_{\gamma_B}.
\]
The standard horizontal and vertical connection-curvature contributions are
\[
(\operatorname{Ric}_g^H)_F(X,Y)
=-\frac12G_{ab}
 \langle\iota_XF^a,\iota_YF^b\rangle,
\]
and
\[
(\operatorname{Ric}_g^V)_{ab,F}
=\frac14G_{ac}G_{bd}F^c_{ij}F^{d\,ij}.
\]

Since the base is two-dimensional,
\[
\langle\iota_XF^a,\iota_YF^b\rangle
=f^af^b\gamma_B(X,Y),
\qquad
F^c_{ij}F^{d\,ij}=2f^cf^d.
\]
Hence
\[
\boxed{(\operatorname{Ric}_g^H)_F=-\mathcal Q\gamma_B}
\]
and
\[
\boxed{
(\operatorname{Ric}_g^V)_{ab,F}
=\frac12G_{ac}G_{bd}f^cf^d.}
\]

For the supplied ansatz,
\[
f^1=e^{-2\lambda}P_r,\qquad
\mathcal Q=\frac12e^{\sigma+\alpha-4\lambda}P_r^2.
\]
Therefore
\[
-\mathcal Q\,\gamma_{rr}
=-\frac12P_r^2e^{\sigma+\alpha-2\lambda},
\]
and
\[
\frac12G_{11}^2(f^1)^2
=\frac12P_r^2e^{2\sigma+2\alpha-4\lambda}.
\]
These are exactly the two expressions recorded in
`step89_symbolic_twist_ricci.json`. Thus:

- **(a)** the orbit coefficient \(1/2\) is correct;
- **(b)** the direct base contribution is \(-\mathcal Q\gamma_B\).

Taking the vertical trace gives
\[
G^{ab}(\operatorname{Ric}_g^V)_{ab,F}
=\frac12G_{cd}f^cf^d=\mathcal Q.
\]

---

## 2. Area and orbit-shape equations

In the stated normalization, the vertical Ricci trace without twist is
\[
G^{ab}\operatorname{Ric}_{ab}=-L\sigma,
\qquad
L=\Delta_{\gamma_B}+\langle\nabla\sigma,\nabla\cdot\rangle.
\]
Including twist and imposing \(\operatorname{Ric}_g=-3g\) gives
\[
-L\sigma+\mathcal Q=-6,
\]
hence
\[
\boxed{L\sigma=6+\mathcal Q.}
\]

For \(M=\operatorname{diag}(e^\alpha,e^{-\alpha})\) and \(f^2=0\),
\[
\frac{\operatorname{Ric}_{11}}{G_{11}}
-\frac{\operatorname{Ric}_{22}}{G_{22}}
=-L\alpha+\mathcal Q.
\]
The Einstein equation therefore gives
\[
\boxed{L\alpha=\mathcal Q.}
\]
With the Step 85 normalization \(e=|d\alpha|^2\), the induced target source obeys
\[
\boxed{|S_F|^2=\mathcal Q^2.}
\]
Thus **(c)** and the diagonal one-charge tension calculation are correct.

---

## 3. The horizontal Einstein equation and the sign propagation

The complete horizontal Ricci decomposition is
\[
\operatorname{Ric}_g^H
=
\operatorname{Ric}_B-\operatorname{Hess}\sigma
-\frac12d\sigma\otimes d\sigma
-\frac12U^*h_{\mathbb H^2}
-\mathcal Q\gamma_B.
\]
Setting this equal to \(-3\gamma_B\) yields
\[
\boxed{
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=(-3+\mathcal Q)\gamma_B
+\frac12d\sigma^2
+\frac12U^*h_{\mathbb H^2}.}
\]
Equivalently, the finite-dimensional Bakry–Émery tensor is
\[
\boxed{
\operatorname{Ric}^4_\sigma
:=\operatorname{Ric}_B-\operatorname{Hess}\sigma
-\frac12d\sigma^2
=(-3+\mathcal Q)\gamma_B
+\frac12U^*h_{\mathbb H^2}.}
\]

Thus the direct term \(-\mathcal Q\gamma_B\) in \(\operatorname{Ric}_g^H\) becomes
\(+\mathcal Q\gamma_B\) after solving the Einstein equation for the base drift curvature. This is the sign error in item (5).

---

## 4. Corrected Bochner equation

Let
\[
C_{ij}=h_{\mathbb H^2}(U_i,U_j),\qquad e=\operatorname{tr}C,
\]
and
\[
\Phi(C)=\frac12\operatorname{tr}(C^2)+2\det C
       \ge\frac12e^2.
\]
For \(\tau_\sigma(U)=S_F\), set
\[
V(X)=\langle dU(X),S_F\rangle.
\]
The weighted tension identity gives
\[
\langle dU,DS_F\rangle
=\operatorname{div}_\sigma V-|S_F|^2.
\]

Substitution of the corrected base equation into the weighted Bochner formula gives
\[
\frac12Le
=
|DdU|^2
+\frac12|dU(\nabla\sigma)|^2
+\Phi(C)
-(3-\mathcal Q)e
+\operatorname{div}_\sigma V
-\mathcal Q^2.
\]
Therefore
\[
\boxed{
\frac12Le\ge
\frac12e(e-6+2\mathcal Q)
+\operatorname{div}_\sigma V-\mathcal Q^2.}
\]
So **(d)** as written, with \(e-6-2\mathcal Q\), is incorrect.

---

## 5. Separator contribution

For an invariant hypersurface over a base curve, let \(T,\nu\) be the horizontal tangent and normal and \(E_a\) a vertical orthonormal frame. The mixed second-fundamental-form entries satisfy
\[
\mathrm{II}(T,E_a)
=\pm\frac12\langle F(T,\nu)^\#,E_a\rangle.
\]
Since both symmetric mixed entries contribute to the tensor norm,
\[
2\sum_a|\mathrm{II}(T,E_a)|^2
=\frac12G_{ab}f^af^b
=\mathcal Q.
\]
Thus
\[
|\mathrm{II}|^2\ge\mathcal Q.
\]
Inserting this into Step 88 equation (2.5) gives
\[
\boxed{
\langle e_s\rangle
\ge12+2\langle\mathcal Q\rangle-8\delta.}
\]
The separator strengthening is therefore correct.

---

## 6. Resolvent arithmetic

If one assumes the proposed but incorrect drift tensor
\[
\operatorname{Ric}^4_\sigma
=-(3+\mathcal Q)\gamma_B+\frac12U^*h
\]
and also treats \(\mathcal Q=q\) as a constant, then \(K=3+q\), \(\kappa=2K\), and the Step 87 calculation gives
\[
B\le
\left[
\frac{2q}{\sqrt{3+q}}
+\sqrt{2(3+q)+\frac{5q^2}{3+q}}
\right]^2.
\]
Its first crossing with \(12+2q\) is indeed
\[
q=0.7707543822\ldots.
\]
Thus the numerical arithmetic in `step89_corrected_twist_resolvent.json` is internally consistent after taking the erroneous drift equation as input.

With the corrected geometry and constant \(0\le q<3\),
\[
K=3-q,\qquad \kappa=6-2q,
\]
and the analogous ceiling is
\[
\boxed{
B\le
\left[
\frac{2q}{\sqrt{3-q}}
+\sqrt{2(3-q)+\frac{5q^2}{3-q}}
\right]^2.}
\]
Its first crossing with \(12+2q\) is approximately
\[
\boxed{q=0.8985974.}
\]
Hence **(e)** with \(\kappa=6+2q\) and crossing \(q\simeq0.77\) is only the arithmetic consequence of the sign-reversed base equation, not of the supplied symbolic Ricci tensor.

Finally, \(\mathcal Q\) is generally a function on \(B\), not a constant. Exact mixed Einstein equations give
\[
d\!\left(\rho G_{ab}*F^b\right)=0,
\]
so the charge components \(\rho G_{ab}f^b\) are constant, while
\[
\mathcal Q(x)
=\frac1{2\rho(x)^2}c_aG^{ab}(x)c_b
\]
usually varies. A single resolvent mass involving \(\mathcal Q\) therefore requires an explicit constant-\(\mathcal Q\) assumption or uniform estimates. Moreover, if an exact cusp open set has \(F=0\), the conserved charges vanish and \(F\equiv0\) throughout the connected region. For the exact cusp-ended geometry of Step 88, nonzero twist is therefore excluded by the mixed Einstein equation itself.