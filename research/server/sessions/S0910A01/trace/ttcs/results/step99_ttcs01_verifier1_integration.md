# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 99,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step99_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step99_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 99 product-orbifold bridge check. The scientific question is whether the Step 98 raw chirality calculation should be treated as a restricted implemented spectral-model mechanism and whether Step 99 legitimately strengthens it by (i) showing omitted same-factor partial tensor jets for actual electric/full-Lie magnetic m=2 tensor families contract exactly to zero with the Step96 source/receiver functionals, and (ii) showing same-chirality zeros in the implemented AA/BB tensor model arise from signed fixed-degree polarization cancellation rather than support-level absence. Read the notes/scripts/data and identify any mathematical or coding errors, normalization risks, false interpretations, or useful next proof targets. Do not decide final Yau26 status; focus on correctness of this bridge evidence and its limits.

## Integrated Scientific Memo

# Step 99 bridge verification

## Verdict

The corrected interpretation is justified:

- **Step 98 must remain a restricted implemented spectral-model calculation**, not a complete Ozuch interaction or obstruction theorem.
- **Step 99 genuinely strengthens that model** in two ways:
  1. for the four implemented \(m=2\) electric/full-Lie magnetic tensor seeds, the omitted same-factor **coordinate partial jets** have zero contraction with the Step96 source and receiver arrays;
  2. the AA/BB same-chirality zeros are caused by signed polarization cancellation, not by absence of individual same-chirality mode couplings.

Neither strengthening yet proves that the implemented map equals the complete geometric gluing coefficient.

## 1. Same-factor partial jets

The local formulas used in `step99_tensor_partial_jets.py` are consistent to the required Taylor order:

\[
g_{ij}=\delta_{ij}-\frac13(r^2\delta_{ij}-x_ix_j)+O(r^3),
\qquad
\sqrt{\det g}=1-\frac16r^2+O(r^4),
\]

and, for \(q_2=x^2-y^2\) or \(2xy\),

\[
\psi=bq_2(1+\alpha r^2),\qquad
\alpha=\frac{2-\mu}{12}.
\]

Indeed \(\Delta_{S^2}\psi=b(12\alpha-2)q_2+O(r^4)\), so \(\Delta\psi=-\mu\psi\) gives exactly this \(\alpha\). Consequently

\[
E=\operatorname{Hess}\psi+\frac{\mu}{2}\psi g,
\qquad
M=\mathcal L_{J\nabla\psi}g
\]

are implemented correctly through the order needed to compute \(\partial_p\partial_qT_{ab}(0)\). The magnetic routine includes the metric-derivative terms of the full Lie derivative.

The resulting statement is nontrivial:

- arbitrary same-factor support is annihilated by the receiver but **not** by the source;
- nevertheless, for
  \[
  E_{c2},E_{s2},M_{c2},M_{s2},
  \]
  in both AA and BB embeddings,
  \[
  R_\pm(\partial^2T)=S_\pm(\partial^2T)=0
  \]
  in every reported component.

Thus the omitted \((\partial^2T)f(p)\) contribution vanishes for these selected families; this is not a consequence of receiver sparsity alone. Scalar pole values, Taylor \(1/2\) factors, and common mode normalizations cannot change this zero.

### Important qualifications

1. **“Exact” is presently exact only after rational reconstruction.**  
   Both exact scripts convert floating Step96 arrays using
   ```python
   Rational(str(float(x))).limit_denominator(10**6)
   ```
   and threshold values below \(10^{-15}\). Therefore the certificate is exact for a rational surrogate of the Step96 arrays, not yet an exact derivation from the geometric source/receiver definitions. Exact symbolic generation of `RCOEFF` and `SCOEFF` is needed before calling this a geometric exact certificate.

2. **The script computes coordinate partial jets, not intrinsic covariant Hessians.**  
   At the normal-coordinate origin,
   \[
   \nabla_p\nabla_qT_{ab}
   =
   \partial_p\partial_qT_{ab}
   -(\partial_p\Gamma^r_{qa})T_{rb}
   -(\partial_p\Gamma^r_{qb})T_{ar}
   +\cdots .
   \]
   The present result is appropriate if Step96 pairs with the quadratic coefficient of tensor components in the same normal/Bianchi chart, as Ozuch-style local expansions suggest. That chart-level identification has not been derived here. If the intended functional uses \(\nabla^2T\), the \(\partial\Gamma\cdot T\) terms must be checked.

3. **Mixed first-derivative invisibility is not reproducible from the supplied scripts.**  
   The claim concerning \((\partial T)(\partial f)\) is attributed to an omitted support-check script. `step99_tensor_partial_jets.py` tests only all-indices-in-one-factor support. Hence item (i) is verified for the same-factor term, but the mixed-term claim remains conditional on absent material.

4. **Mode completeness remains conditional.**  
   Restricting tensor values at a pole to the \(m=\pm2\) plane is natural for spin-two modes, but the supplied files do not prove that these electric/magnetic families exhaust every relevant geometric AA/BB eigentensor after gauge and quotient projection.

## 2. Origin of the same-chirality zeros

`step99_chirality_cancellation_structure.py` establishes that individual same-chirality terms are generally nonzero. In the reported AA–NS run there are 1800 such individual terms, while the complete blocks satisfy

\[
B_{++}=B_{--}=0.
\]

Because the grouping is diagonal in tensor kind, seed, and scalar polarization, and because the heat/eigenvalue prefactor is common and positive at fixed \((\ell_t,\ell_s)\), the cancellation is finite-dimensional signed polarization algebra rather than support selection or a heat-tail accident.

The fixed-degree script confirms this with rationalized Step96 coefficients for all tested cases:

\[
B_{++}^{(\ell_t,\ell_s)}
=
B_{--}^{(\ell_t,\ell_s)}
=0,
\]

while the expected mixed blocks survive—AA for NS and BB for SN. The full 16-entry tensors are tested, not merely the compact display. The relative scalar weight

\[
w_{m0}=\frac{2\mu}{\mu-2},\qquad w_{c2}=w_{s2}=1
\]

is consistent with the pole Hessian amplitude ratio for normalized sphere harmonics.

### Coverage and interpretation limits

- This is not yet an all-degree proof: only six degree pairs were tested, and no odd–odd pair appears. A symbolic proof with parity signs \(\varepsilon_t,\varepsilon_s\in\{\pm1\}\) would cover all \(\ell_t,\ell_s\ge2\).
- The script’s conclusion should say **“exact for the tested rationalized fixed-degree algebra”**, not “proved structurally for every degree.”
- The statement that \(\ell_s=1\) belongs to a separate AB family is not sufficient. A pure AA mode \(T_Af_B\) with \(\ell_s=1\) still exists; its zonal scalar has nonzero isotropic pole Hessian but no \(m=2\) partners. Since the numerical heat sum includes \(\ell_s=1\), this slice needs a separate exact, absolute-normalization calculation. It cannot use \(2\mu/(\mu-2)\).
- The \(\ell_s=0\) scalar-constant slice should likewise be classified explicitly: either excluded by the operator/gauge decomposition or evaluated separately.
- The node rule encoded by `node_sign`, particularly the extra sign for the \(s2\) seed, has not been derived from explicit pole-frame and quotient transport. It controls which NS/SN mixed block survives and is therefore geometrically load-bearing.

Accordingly, item (ii) is valid in the following precise form: **within the implemented model, and exactly for the tested rationalized degree-pair algebra with \(\ell_s\ge2\), the zero is a signed complete-polarization cancellation, not modewise support absence.**

## 3. Remaining spectral-model completeness risks

The implemented AA, BB, and AB sectors do not visibly include the fourth summand in

\[
\operatorname{Sym}^2_0(T_A\oplus T_B)
\cong
\operatorname{Sym}^2_0T_A
\oplus
\operatorname{Sym}^2_0T_B
\oplus
(T_A\otimes T_B)
\oplus
\mathbb R(g_A-g_B).
\]

Thus the relative-trace scalar-scalar family
\[
f_Af_B(g_A-g_B)
\]
must either be added or proved annihilated by the relevant source/receiver pairing. Without this, AA/BB/AB are not demonstrably the full traceless symmetric-tensor Green kernel.

The final tensor magnitude is also still heat-regularized:

\[
R\,e^{-\tau P}P^{-1}S^*,
\]

not yet the unregularized \(RP^{-1}S^*\). The displayed fixed-degree cross blocks alternate with degree parity, so the numerical \(0.008\) response and its sign require a genuine \(\tau\downarrow0\) or spectral-tail estimate. Step99 strengthens the exact zero channels, not the numerical positivity margin.

A useful normalization audit follows from self-adjointness: after quotient factors and frame transport, the \(j\to i\) pair map should be the transpose of the reversed \(i\to j\) map in corresponding \(L^2\) bases.

## 4. Relation to Ozuch’s geometric coefficient

Ozuch’s orbifold-side coefficient, after lower obstructions vanish, is represented by a boundary pairing of the form

\[
\nu_l
=
3\int_{S^3/\mathbb Z_2}\langle H^4,V_{l,2}\rangle .
\]

Step96 may encode this pairing, but Step99 does not derive the identification. The following remain outside the verified bridge:

- exact quotient/invariant-mode normalization;
- node-frame and chirality-basis transport;
- full geometric eigentensor and gauge decomposition;
- subtraction of global kernel and Einstein-deformation components;
- self, deformation, complement, and moving-projector terms;
- the gluing remainder estimates.

The Kähler explanation is a strong structural target. On a Kähler–Einstein four-manifold in complex orientation,

\[
\mathcal R^+=\lambda\,\Pi_{\mathbb R\omega},
\qquad
K=\ker\mathcal R^+=\Lambda_{\mathbb R}^{2,0},
\]

and along a Kähler–Einstein variation,

\[
\Pi_K\,\dot{\mathcal R}^{+}\,\Pi_K=0.
\]

Motion of \(K\) contributes no \(K\)-to-\(K\) block because the background operator annihilates \(K\). This would explain the same-chirality cancellation if the complete singular Green field, including gauge and global correction terms, were proved tangent to the appropriate Kähler–Einstein sector. That membership is presently unproved.

## Most useful next checks

1. Generate Step96 coefficient arrays directly in exact symbolic arithmetic.
2. Prove the polarization identity symbolically for arbitrary \(\ell_t,\ell_s\ge2\), with parity variables.
3. Evaluate the isolated \(\ell_s=1\) \(m0\)-only contribution and classify \(\ell_s=0\).
4. Supply an exact mixed-support contraction for \((\partial T)(\partial f)\).
5. Check coordinate-partial versus covariant-jet conventions, including \(\partial\Gamma\cdot T\).
6. Add or eliminate the relative-trace scalar-scalar sector.
7. Derive frame transport, quotient factors, and reversed-pair transpose reciprocity.
8. Identify the surviving mixed block with Ozuch’s
   \[
   \pi_{\mathrm{tr}}(\rho(\zeta)\otimes\rho(\zeta))
   \]
   curvature response and control the heat tail.

In summary, the Step98/99 notes now state the scientific status substantially correctly. The bridge evidence is real, but its exactness is conditional on rationalized Step96 arrays, its fixed-degree coverage omits low scalar degrees, and it remains a model-level rather than geometric Ozuch identity.