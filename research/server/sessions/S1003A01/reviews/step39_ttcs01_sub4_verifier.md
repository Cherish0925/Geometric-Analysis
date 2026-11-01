# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step39_actual_harmonic_zero_test_and_route_comparison.md",
    "Sessions/S1003A01/workspace/scripts/step39_harmonic_zero_profile.py",
    "Sessions/S1003A01/workspace/data/step39/harmonic_zero_certifiedprofile_x003_X128.json",
    "Sessions/S1003A01/workspace/data/step39/harmonic_zero_x0038_X128.json",
    "Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md",
    "Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md",
    "Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md",
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md"
  ]
}
```

## Task

Independently check the Step-39 actual harmonic-zero test object and its computed/scaled quantities. Verify the differential-geometric assertions: collar gluing gives a smooth closed self-dual harmonic form on the closed replicated metric; zero exceptional period and bolt vanishing are consistent; the sixfold scaling of q, amplitude defect, one-derivative form energy, Weyl-model error, and Ricci cost is correct; the negative-Kähler target used in the script has the stated original-scale eigenvalues; eta=1 is justified for the fixed pullback Kähler cohomology class but not arbitrary directions; and the singular hatted AK s* calculation cannot directly invoke closed AKGamma. Read the script and JSONs rather than trusting the note. Identify any normalization or logical error and give corrected formulas/numbers. Then assess only what the evidence establishes about localized O(k) form cost versus a diffuse construction.

## Output

# Verification memo: Step-39 harmonic-zero test object

The script and both JSON files were read directly. The geometric statements about the form all hold. Three normalization or interpretation defects need correction:

1. The "Ricci defect" entered in \(d_{1/2}\) is \(P=\int|\mathrm{Ric}^\circ|^2\), not \(\int|\mathrm{Ric}+g|^2\). The scalar part of the latter is missing.
2. The torsion number is quoted in the \(\mathrm{Ric}=-6g\) scale, beside quantities quoted in the \(\mathrm{Ric}=-g\) scale.
3. The reason AKΓ cannot be used on \((\widehat g,\Omega)\) is sharper than the note says: \(\int\widehat s^{\,2}d\widehat V=+\infty\).

There is also one structural identity worth recording. The only sign-indefinite term of Step-28 Theorem A equals, per cell, exactly the linear torsion allowance \(2A\theta\) of a formal AKΓ.

## 1. The form \(\Omega\): closed, self-dual, smooth, harmonic

**Self-duality.** With \(e^0=dt\) and \(e^i=a_i\sigma_i\),
\[
\tfrac12d(\phi\sigma_f)=\tfrac{\phi'}{2a_f}e^{0f}+\tfrac{\phi}{a_ga_h}e^{gh}.
\]
This is a multiple of \(e^{0f}+e^{gh}\) iff \(\phi'/\phi=2a_f/(a_ga_h)\). Then \(\Omega=u^2(e^{0f}+e^{gh})\), \(u^2=\phi/(a_ga_h)\), and \(|\Omega|^2=2u^4\).

**Collar.** On the collar \(a_f=\sinh t\cosh t\) and \(a_g=a_h=\sinh t\). Hence \((a_ga_h)'=2a_f\), so \(\phi=a_ga_h\) is consistent and \(\Omega=d(\tfrac12\sinh^2t\,\sigma_f)=\omega_{CH}\). The script fixes \(\phi(X)=X=a_ga_h(X)\) through `Ld -= Ld[-1]`, which is correct.

**Bolt.** \(a_h\sim t\) and \(a_f,a_g\to b\), so \(\phi'/\phi=2/t+O(1)\). This gives \(\phi\sim Ct^2\), \(u^2\sim ct\) and \(|\Omega|\sim\sqrt2\,ct\). The form vanishes to first order on the bolt. The bolt is tangent to \(f,g\) and \(\Omega\) has no \(e^{fg}\) component, so \(\int_E\Omega=0\). Vanishing on the bolt and zero period are therefore consistent. Zero period does not force vanishing in general, but here both hold.

**Smoothness.** This follows without any parity analysis of \(\phi\). \(\Omega\) is bounded and closed on the complement of a codimension-2 surface. The surface term over a tube of radius \(\varepsilon\) is \(O(\varepsilon)\sup|\Omega|\to0\). Hence \(d\Omega=0\) distributionally. Since \(\Omega=*\Omega\), also \(d^*\Omega=0\), and elliptic regularity makes \(\Omega\) smooth and harmonic.

**Gluing.** The covering map \(B\to X_\Gamma\) is holomorphic, and the cell's \(f\)-slot is the Hopf fibre of the host \(J\) (perpendicular class). So \(\Omega\) extends by the host Kähler form. Replication gives a smooth harmonic form on \(X\#k\overline{\mathbb{CP}}^2\) whose class lies in \(\mathcal H^+_g\).

**Genericity of the zero set.** The zero set (a 2-sphere) is non-generic and is produced by the \(SU(2)\) symmetry. For generic metrics, zero sets of self-dual harmonic forms are circles. Any perturbative or diffuse deformation changes the zero-set geometry qualitatively.

**Consistency with Taubes.** This agrees with Corollary T1: a zero \(E\)-period forces a zero of a harmonic self-dual form.

## 2. Class and period angle

\([\Omega]=\pi^*[\omega_X]\), because the collar matches and the \(E\)-periods are zero. On a KE host with \(\mathrm{Ric}=-g\), \(K=[\omega]/2\pi\). Therefore
\[
\eta=\frac{|K\cdot\omega|}{\sqrt{A[\omega]^2}}=1,
\]
independent of the metric and of \(\widehat V\). Pinning \(\widehat V=[\Omega]^2/2\) is automatic.

The note's "\([\Omega]^2=A\), \(|K\cdot[\Omega]|=A\)" holds only for the class normalized to \(K_X\) itself. In the script's \(\psi\)-normalization, \([\psi]^2=4\pi^2A\). Since \(\eta\) is scale invariant, the conclusion is unaffected.

For \(b^+\ge2\), the A02 example \(\omega_0+t\,\mathrm{Re}\,\Omega\) shows that other directions in \(\mathcal H^+\) can have \(\eta<1\). The note's distinction is correct.

## 3. Scalings and recomputed numbers

All scaling rules check, with \(\bar g=6g\):

| Quantity | Scaling | Check |
|---|---|---|
| \(\psi=6\Omega\) | \(\lvert\psi\rvert^2_{\bar g}=36\cdot6^{-2}\lvert\Omega\rvert_g^2=q\) | — |
| \(dV\) | ×36 | amplitude: \(0.0021273\times36=0.076584\) |
| \(\nabla\psi\) | \(\lvert\nabla\psi\rvert^2_{\bar g}=36\cdot6^{-3}\lvert\nabla\Omega\rvert^2_g\); with \(dV\), total ×6 | gradient: \(0.0754120\times6=0.452472\) |
| \(W^+\) (as \(\mathrm{End}\,\Lambda^+\)) | eigenvalues ×\(1/6\), norm² ×\(1/36\) | \(\int\lvert W^+-A\rvert^2dV\) scale invariant |

**Weitzenböck gradient.** The script's integrand \(q(2W_{ff}-s/3)\) is \(\langle(-2W^++s/3)\Omega,\Omega\rangle\), using \(\Delta=\nabla^*\nabla-2W^++s/3\) on \(\Lambda^+\). It vanishes identically on CH (\(W_{ff}=-4\), \(s=-24\)), as it must for a parallel form. There is no surface term, because \(\nabla\Omega=0\) on the collar and on the host.

**Kähler target.** In \(\bar g\) with \(\bar s=-4\), the Kähler \(W^+\) is \(\mathrm{diag}(-\tfrac23,\tfrac13,\tfrac13)\). This equals \(-\tfrac12(\psi\otimes\psi)_0\) at \(q=2\). The linear-in-\(q\) model \(-\tfrac12(\psi\otimes\psi)_0=\mathrm{diag}(-q/3,q/6,q/6)\) pulls back to \(\mathrm{diag}(-2q,q,q)\) in the original scale. This is the script's target, and it reduces to CH \(W^+=(-4,2,2)\) at \(q=2\). Here `Wplus = Rp - s/12` with KE \(R^+=\mathrm{diag}(\lambda,0,0)\), \(\lambda=-6\), which is consistent.

The norm used is the \(\mathrm{End}\,\Lambda^+\) Frobenius norm. This is the convention of \(C_+\) and of Step 28 (\(|W^+_{CH}|^2=24\)). If \(d_{1/2}\) was defined with the tensor norm, the Weyl term changes by a factor 4.

The identity \(\kappa-\widehat s-6\nu^2=0\) holds to \(3\times10^{-14}\) in the JSON. This is an independent sign check on \(W_{ff}\).

### Correction 1: the Ricci term

`ricci_defect = 4*J` with \(J=\widehat P=\int|\mathrm{Ric}^\circ|^2/8\pi^2\) (Step 28 channels \(C,E,D\) are trace-free). However, \(|\mathrm{Ric}+\bar g|^2=|\mathrm{Ric}^\circ|^2+(\bar s+4)^2/4\). The cell scalar is not constant: \(s\in[-24.458,-23.9997]\) for the certified profile and \([-24.027,-23.954]\) for the floating one. The missing term, in \(2\pi^2\) units on the profile scale, is
\[
\Delta_{\rm scal}=\tfrac14\int W\,(s+24)^2\,dt \qquad(\texttt{0.25*integ\_dt(W*(scal+24)**2)}).
\]

The certified profile shows this deviation is not idle. Its JSON has \(\int(2-q)W=-0.006784\), so \(V_g-V_{CH}=-0.00339\): the volume excess is below zero. Step-28's volume formula is
\[
V_{\rm exc}=H+G/2+N/24+\tfrac1{12}\int(s+24)u^2W,
\]
with \(H,G\ge0\) and \(N/24=0.04886/24\). It then forces
\[
\int(s+24)u^2W\,dt\le-12(0.00339+0.00204)=-0.065 .
\]
Hence \(\Delta_{\rm scal}\gtrsim0.065^2/(4V_s)\), where \(V_s\) is the volume carrying the scalar deviation. This term is the same order as the Weyl and amplitude entries and must be computed before quoting \(4.08167\) to six digits.

Either the numerator must be written with \(|\mathrm{Ric}^\circ|^2\), or this term must be added. Alternatively, the form statistics can be recomputed on the \(\bar s=-4\) Yamabe representative, which changes \(q\) as well.

The floating \(J\) (\(0.9956702\)) sits just below the Arb enclosure \(0.9956711\). Using the certified upper value gives \(3.982684\) instead of \(3.982681\), which is negligible.

### Correction 2: torsion scale

`torsion_per_cell_over_2pi2` (\(0.04886\)) is in the \(\mathrm{Ric}=-6g\) scale. Here \(\int|\nabla\omega|^2dV\) with \(|\omega|=\sqrt2\) scales by \(c\). In \(\mathrm{Ric}=-g\) it is \(0.2932\), and \(0.3906\) for the floating profile. The JSON places it beside \(\mathrm{Ric}=-g\) coefficients without conversion. The scale-invariant quantity is \(\theta\); see §4.

### Packing

Each cell occupies a CH ball of volume \(X^2/4=4096\) (\(2\pi^2\) units, \(g\)-scale), while the host has \(A/36\). Disjointness forces \(k/A\le1/147456\approx6.8\times10^{-6}\) at \(X=128\), unless the exact collar can be truncated at smaller \(x\). The coefficient \(4.08\,k/A\) is a per-cell price and is realized only in this ultra-sparse regime. This fits the pure-blow-up tower (\(\theta=1\) is density-free), but it should be stated.

## 4. The hatted structure and AKΓ

**Formulas.** The script's formulas match Step 28:
- \(\widehat s=u^{-3}(6\Delta u+su)\);
- \(\nu=-(q_t+4\sinh q/a_f)/(2u)\);
- \(|\nabla\Omega|^2_{\widehat g}=4\nu^2\);
- \(s^*=\widehat s+4\nu^2\), which is A02's \(s^*=s+|\nabla\omega|^2\), not Step-28's Chern scalar \(\widehat s+2\nu^2\).

**Independent numerical check.** Chern–Stokes predicts \(\int s^*d\widehat V=-24V_{CH}+\tfrac12\int4\nu^2d\widehat V\). The predictions are \(-98304+0.024429=-98303.97557\) (certified) and \(-98303.96745\) (floating). Both match the JSON to all printed digits. The bolt therefore contributes no Chern flux, and Blair's integral is finite and topological:
\[
\int(\widehat s+s^*)\,d\widehat V=-48V_{CH}\ \text{per cell},
\]
which is consistent with \(\alpha=0\).

**No \(s^*>0\) pocket.** \(\max s^*=-23.50\) against the CH value \(-24\), a margin of about 23 units. The statement that no pocket exists is robust, not marginal.

### Correction 3: AKΓ is meaningless on \((\widehat g,\Omega)\), not merely unproved

Near the bolt, \(u^2\sim ct\), \(\nu\sim-1/(2ut)\sim t^{-3/2}\), \(\widehat s\approx-6\nu^2\sim t^{-3}\) and \(d\widehat V\sim t^3dt\). Consequently:
- \(\int\nu^2d\widehat V\) is finite, matching \(N=0.0489\).
- \(\int\widehat s^{\,2}d\widehat V\sim\int t^{-3}dt=\infty\).

The sample \(s^*_{\min}=-1.2\times10^{18}\) at \(u_{\min}=0.002\) fits this power. So \(C_+(\widehat g)=+\infty\). AKΓ for \(\widehat g\) holds trivially and has no relation to \(P(g)\), because \(\int s^2\) is not conformally invariant. Only the linear quantities (Blair, \(\theta\)) survive.

**Scale-invariant torsion fraction.** \(\ell=48\widehat V\), so \(\ell/2\pi^2=4A/3\) on the \(g\)-scale. Then
\[
\theta=\frac{0.04886\,k}{4A/3}=0.0366\,k/A .
\]

**Structural match.** The formal AKΓ allowance is \(2A\theta=\tfrac32(0.04886)k=0.0733k\). This is exactly Step-28 Theorem A's term \(-\tfrac32N\) per cell. The correct localization of AKΓ on this object therefore already exists: it is Theorem A together with the interface flux \(B\) (Step 29), with \(B=1\) at the bolt and \(B=2\) on CH.

Two features distinguish it from a closed-manifold AKΓ:
- The "1" per cell comes from the bolt value of \(B\), not from a Chern flux.
- The divergent \(\widehat s^{\,2}\) is replaced by the finite \(12H_s+6G\).

The actual saving is \(1-0.99567=0.00433\) per cell, about 6% of the \(0.0733\) torsion allowance. Most of the Nijenhuis gain is spent on \(G\), \(Q_A\) and \(Q_\delta\), as in Step 28 §4.

So the note's request that localization "retain the bolt/interface flux" is correct. The flux to retain is \(B\), and on this object it supplies the full threshold unit.

## 5. What the evidence establishes about localized \(O(k)\) cost versus a diffuse construction

**Established, upper side only.** An explicit closed metric/form pair exists. Its cost is exactly additive per cell and confined to the cores: outside them \(u\equiv1\), \(\nabla\Omega=0\), and the metric is KE.

The per-cell defect in \(2\pi^2\) units, \(\mathrm{Ric}=-g\), is:

| Term | Value |
|---|---|
| Trace-free Ricci, \(\int\lvert\mathrm{Ric}^\circ\rvert^2\) | \(3.98268\) (Arb upper \(3.98268\)) |
| Weyl-model error | \(0.0224\) |
| Amplitude | \(0.0766\) |
| Scalar term \(\Delta_{\rm scal}\) | not computed |
| Gradient (separate) | \(0.4525\) |

The form-specific terms are about 2.4% of the numerator. The dominant cost is \(P\approx8\pi^2\cdot0.9957\) per blow-up, and its near-unit size is the bolt value of \(B\). Any diffuse competitor must therefore beat the threshold unit in \(P\) itself. Lowering \(q\)-depletion or Weyl misalignment alone cannot change the coefficient materially.

The object places all almost-complex rotation in non-host-like cores. This is the alternative allowed by A02 Theorem A; the bulk KE region has zero Nijenhuis energy.

**Not established.**
- **No lower bound.** No statement shows that the cost must be linear in \(k\) for pure blow-ups (\(\sigma=18\)), where the inherited bounds vanish.
- **No diffuse mode tested.** The object has zero bulk deviation, so it carries no information on the compliance of a host-scale bulk–core exchange mode.
- **Proxy, not the field.** \(\Omega\) is a harmonic form in the pullback class, not the Seiberg–Witten monopole direction of the glued metric. Relations to \(R\), \(\mathcal N\), or Theorem N require that field.
- **Only one family point.** Two profiles at fixed \(X\) and fixed bolt geometry are one point in the family. The symmetric zero sphere is non-generic, so any interpolating family must handle its change to zero circles.

**Usable benchmark numbers for a localized-to-diffuse theory.** Per cell:

| Quantity | Value |
|---|---|
| \(\theta/(k/A)\) | \(0.0366\) |
| \(\tfrac32N\) | \(0.0733\) |
| Realized saving | \(0.00433\) |
| \(\lVert\nabla\psi\rVert^2\) | \(0.4525\) |
| Weyl-model error | \(0.0224\) |
| Amplitude defect | \(0.0766\) |
| \(\eta\) | \(1\) |
| Exceptional period | \(0\) |

A domain-decomposition estimate should reproduce \(P_{\rm cell}=8\pi^2(1+\int L_{AK})\) on this object, with \(\int L_{AK}=-0.00433\). The bulk contributes zero.