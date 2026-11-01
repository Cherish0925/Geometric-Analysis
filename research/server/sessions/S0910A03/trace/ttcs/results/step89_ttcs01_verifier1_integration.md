# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 89,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step89_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step89_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

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

## Integrated Scientific Memo

## Verification result

The symbolic Ricci data verify **(a), (b), and (c)**. They do **not** imply the proposed drift-curvature sign in Step 5. After inserting the negative horizontal twist term into the Einstein equation, its sign reverses when solving for \(\operatorname{Ric}_B-\operatorname{Hess}\sigma\). Therefore **(d)** and **(e)**, as stated, are incorrect.

Write
\[
Q:=\frac12G_{ab}f^af^b,\qquad F^a=f^a\,\mathrm{vol}_{\gamma_B}.
\]

### 1. Twist Ricci coefficients

In two base dimensions,
\[
\langle\iota_XF^a,\iota_YF^b\rangle=f^af^b\gamma_B(X,Y),
\qquad
F^a_{ij}F^{b\,ij}=2f^af^b.
\]
Hence the connection-curvature contributions are
\[
\boxed{\operatorname{Ric}^{\rm twist}_{ij}=-Q\,(\gamma_B)_{ij}},
\]
and
\[
\boxed{\operatorname{Ric}^{\rm twist}_{ab}
=\frac12G_{ac}G_{bd}f^cf^d}.
\]

For the supplied ansatz, \(f^1=e^{-2\lambda}P_r\), so
\[
Q=\frac12e^{\sigma+\alpha-4\lambda}P_r^2.
\]
Thus
\[
\operatorname{Ric}^{\rm twist}_{rr}
=-Qe^{2\lambda}
=-\frac12P_r^2e^{\sigma+\alpha-2\lambda},
\]
and
\[
\operatorname{Ric}^{\rm twist}_{11}
=\frac12G_{11}^2(f^1)^2
=\frac12P_r^2e^{2\sigma+2\alpha-4\lambda},
\]
exactly matching `step89_symbolic_twist_ricci.json`.

Therefore:

- **(a) verified:** the vertical coefficient is \(1/2\);
- **(b) verified:** the direct horizontal twist Ricci is \(-Q\gamma_B\).

### 2. Area and traceless orbit equations

Taking the vertical trace gives
\[
G^{ab}\operatorname{Ric}^{\rm twist}_{ab}=Q.
\]
Using the untwisted trace identity \(G^{ab}\operatorname{Ric}_{ab}=-L\sigma\) and
\(\operatorname{Ric}_g=-3g\),
\[
-L\sigma+Q=-6,
\]
so
\[
\boxed{L\sigma=6+Q}.
\]
Thus **(c) is verified**.

For \(M=\operatorname{diag}(e^\alpha,e^{-\alpha})\) and \(f^2=0\), the traceless vertical equation similarly gives
\[
\boxed{L\alpha=Q}.
\]
With the normalization \(e=|d\alpha|^2\) along this target geodesic,
\[
\boxed{|S_F|^2=Q^2}.
\]

### 3. Crucial sign propagation into the base equation

The full horizontal decomposition is
\[
\operatorname{Ric}^H_g
=
\operatorname{Ric}_B-\operatorname{Hess}\sigma
-\frac12d\sigma^2-\frac12U^*h_{\mathbb H^2}
-Q\gamma_B.
\]
Imposing \(\operatorname{Ric}^H_g=-3\gamma_B\) yields
\[
\boxed{
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=(-3+Q)\gamma_B
+\frac12d\sigma^2+\frac12U^*h_{\mathbb H^2}.}
\]
Equivalently,
\[
\boxed{
\operatorname{Ric}^4_\sigma
=(-3+Q)\gamma_B+\frac12U^*h_{\mathbb H^2}.}
\]

Thus the direct term \(-Q\gamma_B\) becomes \(+Q\gamma_B\) after it is moved to the other side of the Einstein equation. The claimed
\[
-(3+Q)\gamma_B+\cdots
\]
does not follow from the symbolic Ricci computation.

### 4. Correct Bochner inequality

Let \(A=U^*h_{\mathbb H^2}\), \(e=\operatorname{tr}A\), and
\[
\Phi(A)=\frac12\operatorname{tr}(A^2)+2\det A
       =\frac12e^2+\det A\ge\frac12e^2.
\]
For \(\tau_\sigma(U)=S_F\), with
\[
V(X)=\langle dU(X),S_F\rangle,
\]
the tension identity is
\[
\langle dU,DS_F\rangle
=\operatorname{div}_\sigma V-|S_F|^2.
\]
Consequently,
\[
\frac12Le
=
|DdU|^2+\frac12|dU(\nabla\sigma)|^2
+\Phi(A)-(3-Q)e
+\operatorname{div}_\sigma V-Q^2.
\]
Dropping nonnegative terms gives
\[
\boxed{
\frac12Le\ge
\frac12e(e-6+2Q)+\operatorname{div}_\sigma V-Q^2.}
\]

Therefore **(d) is false as written**: the correct reaction contains
\[
e-6+2Q,
\]
not \(e-6-2Q\). Direct base twist is negative, but after enforcing Einstein it strengthens, rather than weakens, the linear Bochner reaction.

### 5. Separator floor

For an invariant hypersurface over a base curve, the mixed components satisfy, up to orientation,
\[
\mathrm{II}(T,E_a)
=\frac12\langle F(T,\nu)^\#,E_a\rangle.
\]
Since both symmetric mixed entries contribute to \(|\mathrm{II}|^2\),
\[
2\sum_a|\mathrm{II}(T,E_a)|^2
=\frac12G_{ab}f^af^b=Q.
\]
Hence
\[
|\mathrm{II}|^2\ge Q.
\]
Step 88’s identity therefore gives, allowing variable \(Q\),
\[
\boxed{
\langle e_s\rangle
\ge 12+2\langle Q\rangle-8\delta.}
\]
This strengthening is correct.

### 6. Resolvent consequence

The proposed mass
\[
\kappa=6+2Q
\]
and crossing \(Q_*\simeq0.770754\) are algebraically consistent only if one assumes the incorrect drift tensor \(-(3+Q)\gamma_B+\cdots\).

If \(Q=q\) is additionally assumed constant and \(0\le q<3\), the corrected curvature parameter and mass are
\[
K=3-q,\qquad \kappa=2K=6-2q.
\]
Repeating the Step 87 estimate gives
\[
\boxed{
B:=\sup e\le
\left[
\frac{2q}{\sqrt{3-q}}
+\sqrt{\,2(3-q)+\frac{5q^2}{3-q}}
\right]^2.}
\]
Comparison with the floor \(12+2q\) gives its first crossing at approximately
\[
\boxed{q_*\approx0.8986},
\]
not \(0.77075\).

This constant-\(q\) arithmetic is not yet a theorem for general twisted Einstein connectors because \(Q\) is normally a function:
\[
d\!\left(\rho G_{ab}*F^b\right)=0,\qquad
Q(x)=\frac1{2\rho(x)^2}c_aG^{ab}(x)c_b.
\]
A constant resolvent mass therefore requires either constant \(Q\) or suitable uniform bounds. Moreover, if an exact cusp open set has \(F=0\), charge conservation forces \(c_a=0\), hence \(F\equiv0\) on the connected region. Thus nonzero exact twist is incompatible with the exact-cusp-open-set extensions used in Steps 87–88.

## Final disposition

| Item | Verdict |
|---|---|
| (a) orbit factor \(1/2\) | Verified |
| (b) direct base twist \(-Q\gamma_B\) | Verified |
| (c) \(L\sigma=6+Q\) | Verified |
| (d) proposed \(e-6-2Q\) reaction | Incorrect; correct sign is \(e-6+2Q\) |
| (e) \(\kappa=6+2Q,\ Q_*\approx0.77\) | Not geometrically valid; follows from the sign-error premise |

The central correction is the distinction between the **direct Ricci contribution** \(-Q\gamma_B\) and the resulting **Einstein-solved drift curvature**, where the same term appears as \(+Q\gamma_B\).