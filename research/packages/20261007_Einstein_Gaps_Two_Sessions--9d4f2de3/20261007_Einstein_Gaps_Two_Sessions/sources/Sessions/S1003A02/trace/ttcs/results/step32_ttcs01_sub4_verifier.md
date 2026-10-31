# TTCS Independent Branch Record

```json
{
  "step_id": 32,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md"
  ]
}
```

## Task

Analyze the proposed identification of the diagonal collapsed Berger signature charge with an APS/Dai adiabatic eta invariant. Starting from the exact diagonal signature transgression and the Hopf Berger family, determine the needed eta formula, sign, factor, and endpoint convention. Check whether an explicit odd-signature eta formula eta=-(2/3)(1-lambda^2)^2 would imply s=-3 eta and collapsed jump 2; explain kernel/reduced-eta and orientation issues. Then state the strongest justified symmetry-free collapsed-end pricing formulation, separating established APS/Dai consequences from conjectural extension to arbitrary critical-L2 near-minimizers.

## Output

# Memo: the collapsed Berger signature charge as an APS/Dai eta invariant

## Summary

The identification holds exactly. The normalized signature transgression of Theorem X is
\[
\mathfrak s=3\big(\eta_{\rm out}+\Pi\big),
\]
where \(\eta_{\rm out}\) is the APS eta invariant of the even odd-signature operator on the orbit, oriented as the outward-cooriented edge of the inner region in the frame orientation, and \(\Pi\) is the Gilkey/Chern–Simons second-fundamental-form correction.

- With the outward orientation, the exact Step-27 Berger formula gives \(\eta_{\rm out}=+\tfrac23(1-\lambda^2)^2\).
- The proposed formula \(\eta=-\tfrac23(1-\lambda^2)^2\) is the same object with the orbit orientation reversed. In that convention \(\mathfrak s=-3\eta\) holds exactly at \(\mathrm{II}^\circ=0\).
- The collapsed jump of \(\mathfrak s\) is 2. The collapsed price 4 splits as Euler part 2 plus signature part 2.

What follows rigorously, without symmetry, is an exact single-hypersurface pricing identity together with Dai's adiabatic evaluation under bounded collapsed-frame geometry. What does not yet follow is its use on arbitrary near-minimizers.

## 1. Derivation, sign, factor and endpoint convention

### General identity

For compact oriented \(U\), any metric, and outward coorientation \(n\) on \(\partial U\), two classical identities hold:

- Chern–Gauss–Bonnet with transgression term \(Q_{GB}\), valid for any metric.
- APS with Gilkey's correction for non-product metrics:
\[
\tau(U)=\frac1{12\pi^2}\int_U(|W^+|^2-|W^-|^2)-\eta(\partial U)-\Pi_G(\partial U).
\]

In the session normalization these combine to
\[
\widehat P(U)=\frac1{2\pi^2}\int_U|W^\pm|^2+\frac1{96\pi^2}\int_Us^2+\mathfrak b_\pm(\partial U)-\big(2\chi(U)\pm3\tau(U)\big),
\]
\[
\mathfrak b_\pm=\mathfrak b\mp\mathfrak s,\qquad \mathfrak b=\frac1{4\pi^2}\int Q_{GB},\qquad \mathfrak s=3(\eta+\Pi_G).
\tag{A}
\]

Two convention checks:

- **Factor 3.** It comes from \(\frac1{4\pi^2}(|W^+|^2-|W^-|^2)=3\times\) the L-density. This is the "\(\pm3\tau\)" of Hitchin–Thorpe.
- **Operator.** \(\eta\) is for \(B_{\rm ev}=\pm(*d-d*)\) on \(\Omega^0\oplus\Omega^2\). If the operator on all forms is used, \(\eta\) doubles and the relation becomes \(\mathfrak s=\tfrac32(\eta_{\rm all}+\dots)\).

### Endpoint convention

- \(\eta\), \(\Pi_G\) and \(Q_{GB}\) are all odd under simultaneous reversal of coorientation and orientation.
- The inner orbit of an annulus therefore enters as \(-\mathfrak b_\pm\) of its outward-cooriented version. This is exactly the \(\Delta\mathfrak b_\pm\) of Theorem X.
- The raw JSON field is \(S_0=\mathfrak s+6\). The eta identification uses the normalized \(\mathfrak s\).

### Why this is a theorem and not a fit

Both \(\mathfrak s\) and \(3(\eta+\Pi_G)\) are functions of the orbit 1-jet \((a_i,p_i)\), and both have \(t\)-derivative \(\tfrac12W(B_A-B_B)\) on every 2-jet. Their difference \(D\) therefore satisfies
\[
\partial_pD\cdot a''+\partial_aD\cdot p=0\quad\text{for all }a'',p,
\]
so \(D\) is constant. The constant is fixed at the round orbit of flat space: \(\eta(S^3_{\rm round})=0\) because of the orientation-reversing isometry, \(\Pi_G=0\) because the orbit is umbilic in a conformally flat germ, and \(\mathfrak s=0\) there.

A corollary is an exact eta formula for every diagonal left-invariant metric on \(SU(2)\):
\[
\eta_{\rm out}(a_1,a_2,a_3)=\tfrac13\,\mathfrak s\big|_{p=0}=\tfrac13\big(S_0|_{p=0}-6\big),
\]
which can be read directly from `chiral_flux.json`.

## 2. Check of \(\eta=-\tfrac23(1-\lambda^2)^2\)

### Product jets

Step 27 gives an exact Berger expression with \(a=\varepsilon\) (fibre), \(b=c=R\), \(\lambda=\varepsilon/R\):
\[
\mathfrak s=2+\lambda^2(U^2-2UV+V^2-4)+2\lambda^4=2(1-\lambda^2)^2+\lambda^2(U-V)^2 .
\]

At \(U=V=0\) (totally geodesic orbit, \(\Pi_G=0\)) this is \(\mathfrak s=2(1-\lambda^2)^2=-3\cdot[-\tfrac23(1-\lambda^2)^2]\). So:

- \(\mathfrak s=-3\eta\) holds exactly for all \(\lambda\), with \(\eta\) the eta invariant of the orbit carrying the reversed orientation. Equivalently, \(\mathfrak s=3\eta_{\rm out}\) with \(\eta_{\rm out}=+\tfrac23(1-\lambda^2)^2\).
- The value at \(\lambda=1\) is 0 and the limit as \(\lambda\to0\) is 2. The collapsed jump is 2, matching \(\int_{\rm Taub\text{-}NUT}L=+\tfrac23\) in the frame orientation.

### Correction term

\(U-V=R(k_{\rm base}-k_{\rm fibre})\) is a difference of principal curvatures. Hence, in the biaxial case,
\[
3\Pi_G=a_f^2(k_b-k_f)^2,
\]
which depends only on the traceless second fundamental form \(\mathrm{II}^\circ\).

This is the expected structure. The L-density is pointwise conformally invariant, and the Chern–Simons/eta invariant of a 3-manifold is conformally invariant, so \(\mathfrak s\) is a conformal invariant of the hypersurface germ. A symbolic test on the general triaxial \(S\) field is \(\mathfrak s(a,p+\mu a)=\mathfrak s(a,p)\).

### CH test (\(\lambda=\cosh t>1\), non-umbilic)

Here \(U=\cosh t\), \(V=\cosh2t/\cosh t\), and \(U-V=-\sinh^2t/\cosh t\). Then
\[
\mathfrak s=2\sinh^4t+\sinh^4t=3\sinh^4t ,
\]
which equals the table value. This confirms both the \(\Pi\) term and the continuation of the polynomial \(\eta\) to all \(\lambda\), including \(\lambda>4\).

### Orientation

- Inversion \(g\mapsto g^{-1}\) is an orientation-reversing isometry from left-Berger to right-Berger spheres. The sign of \(\eta\) is therefore the sign of the fibration's Euler number relative to the orientation.
- In the frame orientation (CH Kähler with \(W^+\neq0\), bolt \(-1\)), the \(\sigma_1\)-fibre has \(e=-1\) outward and \(\eta_{\rm ad}=+\tfrac23\).
- Values of \(-\tfrac23(1-\lambda^2)^2\) quoted elsewhere correspond to the opposite orientation or to the opposite operator sign. The session's own exact formula fixes the sign independently of any source.

## 3. Kernel and reduced eta

- \(\ker B_{\rm ev}=\mathcal H^0\oplus\mathcal H^2\) has dimension \(b_0+b_2=1\) for every metric on \(S^3\) and on its lens quotients. No eigenvalue crosses zero, there is no spectral flow, and \(\eta_{\rm sign}\) is a smooth real-valued function rather than a quantity defined mod \(\mathbb Z\).
- The APS signature formula uses \(\eta\), not \(\xi=(h+\eta)/2\); the \(h\) terms cancel.
- This contrasts with Hitchin's Dirac eta on Berger spheres, where harmonic spinors appear at \(\lambda=4\) and \(\xi\) jumps. Such jumps are irrelevant to \(\mathfrak s\), which the CH check confirms is analytic through \(\lambda=4\).
- The only integer in the story is Dai's spectral-sequence term. It arises from eigenvalues of order \(\varepsilon\), not from kernel, so \(\mathfrak s\) varies continuously into its adiabatic value.

## 4. Endpoint decomposition, \((\mathfrak b,\ 3\eta,\ 3\Pi)\)

| end | \(\mathfrak b\) | \(3\eta_{\rm out}\) | \(3\Pi_G\) | \(\mathfrak b_+\) |
|---|---|---|---|---|
| smooth centre / round flat orbit | 2 | 0 | 0 | 2 |
| thin tube around \(O(-1)\) bolt (\(V=R/\varepsilon\), \(U=0\)) | 4 | 2 | 1 | 1 |
| controlled Hopf-collapsed end | 0 | 2 | 0 | −2 |

Model checks:

- **Taub-bolt.** \(\int L=(2-3)/3=-\tfrac13\) and APS gives \(-1=-\tfrac13-\tfrac23\). The bolt-to-ALF change in \(\mathfrak s\) is entirely the loss of the fibre second-fundamental-form term. The eta part is the same \(e=-1\) adiabatic value at both ends.
- **Burns.** \(\int L=-1=\tau\), with \(\eta(\text{round})=0\).
- **Q″ price.** The Berger-to-round price \(4\) splits as \(2\) from the Euler term (Cheeger–Gromov vanishing) plus \(2\) from \(3\eta_{\rm ad}\).

## 5. Dai value for general Euler number, and a testable prediction

Take the biaxial \(\mathbb Z_k\) fibre quotient \(L(k,1)\). Its local transgression is \(1/k\) of the cover's, so
\[
\eta_{\rm ad}=\eta(L(k,1)_{\rm round})+\tfrac{2}{3k}.
\]

- **Lens value.** The APS lens value is \(\pm\frac1k\sum\cot^2(\pi j/k)=\pm\frac{(k-1)(k-2)}{3k}\).
- **Sign forced by \(\widehat P\ge0\).** LeBrun's scalar-flat Kähler metrics on \(O(-k)\) are biaxial with \(V=1+\frac{k-2}{r^2}+\frac{1-k}{r^4}\); they give Burns at \(k=1\) and Eguchi–Hanson at \(k=2\), and they have \(W^+=0\) in the frame orientation. For them (A) gives
\[
\widehat P=\frac2k-3\eta-1\ \ge 0 .
\]
For \(k\ge3\) this forces the minus sign.
- **Result.** Algebraically,
\[
\eta_{\rm ad}=\frac{3-k}3=\frac e3-\operatorname{sign}(e),\qquad e=-k .
\]
This is the Dai form: the local \(\eta\)-form term \(e/3\) plus the spectral-sequence integer \(-\operatorname{sign}e\). It is odd in \(e\), as orientation reversal requires.
- **Independent check.** The two-centre ALF (Gibbons–Hawking) space in its hyperkähler orientation has \(e=+2\). It needs \(\mathfrak b_+(\text{end})=2\chi+3\tau=1\), and the formula gives \(-e+3\operatorname{sign}e=1\).

Predictions:

- **LeBrun metrics.** \(\widehat P(\text{LeBrun }O(-k))=(k-2)^2/k\). This gives \(1\) for Burns and \(0\) for Eguchi–Hanson. The value \(\tfrac13\) at \(k=3\) is an independent test of the orientation chain and of the lens eta. It is a one-line computation with the existing diagonal scripts on the cover, which predict \(\widehat P_{\rm cover}=(k-2)^2\).
- **Decollapse on the \(O(-k)\) fibre quotient.** The ALF-to-ALE price is
\[
\frac{k^2-3k+4}{k}-(k-3)=\frac4k .
\]
This is local, being \(1/k\) of the cover value 4. Lemma Q's ALE bound is attained by the LeBrun metrics.

## 6. The finite-charge anisotropic class in these terms

From \(\mathfrak b_\pm^{\rm end}=\mp2-(C\pm4X)^2\) one gets
\[
\mathfrak s_{\rm end}=2+C^2+16X^2,\qquad \mathfrak b_{\rm end}=-8CX\neq0 .
\]

The Euler term does not vanish because this class has unbounded slice curvature. For a triaxial left-invariant metric, \(\mathrm{Ric}_{ff}\approx4(2x+\lambda^2)/(\lambda^2R^2)\), and with \(x=X\lambda\) this is of order \(X/(\lambda R^2)\). Hence the Step-30 requirement \(x=O(\lambda^2)\).

So the excess \(C^2+16X^2\) is a non-adiabatic eta-plus-\(\Pi\) shift. It is produced by perturbations that are of order one in the collapsed-frame \(C^2\) sense. The raw-opening identity
\[
\mathfrak b_+=-2-(u_f-u_g)^2+\delta(4-u_fu_g)-\delta^2
\]
shows that outside this class the shift can have either sign. The hypotheses for an adiabatic charge must therefore be stated in collapsed-frame norms, not in raw state variables.

## 7. Symmetry-free collapsed-end pricing

### Established

- **(i) Exact identity.** Identity (A) holds for every smooth metric on every compact oriented \(U\). Consequently
\[
\widehat P(U)\ge\mathfrak b_\pm(\partial U)-\big(2\chi(U)\pm3\tau(U)\big).
\]
Only one good hypersurface per neck is needed; no compactness is required.
- **(ii) Adiabatic evaluation.** Suppose the rescaled slice metrics \(R_j^{-2}g|_{Y_j}\) converge, in collapsed-frame \(C^1\) with bounded curvature, to an adiabatic circle-bundle family \(\varepsilon_j^2\theta^2+\pi^*g_B\) with Euler number \(e\), and \(\varepsilon_jR_j|\mathrm{II}^\circ_{\rm fibre/base}|\to0\) with bounded normalized \(\mathrm{II}\). Then three limits hold:
  - \(\mathfrak b\to0\) (Cheeger–Gromov type);
  - \(\Pi_G\to0\), since its integrand times the slice volume is \(O(\varepsilon)\);
  - \(\eta\to e/3-\operatorname{sign}e\) (Dai, plus the APS variation formula for the perturbation).
  Hence
\[
\mathfrak b_\pm\to\mp\big(e-3\operatorname{sign}e\big).
\]
- **(iii) Q″ without symmetry.** For an annulus from such a slice with \(e=-1\) to an almost-round flat slice,
\[
\liminf\widehat P\ge4 .
\]
More generally the price is the round charge minus the adiabatic charge plus the change in \(2\chi\pm3\tau\).

The bolt-tube row of §4 shows exactly which hypothesis in (ii) matters: \(\varepsilon R|\mathrm{II}^\circ|\sim1\) gives \(3\Pi=1\).

### Plausible but unproved

- Extension of (ii) to general nilpotent/F-structure collapse: torus and nil fibres, and Seifert ends with exceptional fibres. This needs Dai's formula for those fibrations and a path argument within bounded-curvature invariant metrics showing that \(\eta\) is \(o(1)\)-constant on each collapsed class.

### Conjectural: arbitrary critical-\(L^2\) near-minimizers

The conjecture is that every collapsed neck of a \(\widehat P\)-near-minimizing sequence is priced up to \(o(1)\) by the adiabatic charge difference. The missing input is a slice-selection theorem: some hypersurface in each neck has bounded normalized curvature and \(\varepsilon R|\mathrm{II}^\circ|\to0\).

- \(\widehat P\) and \(L^2\) curvature do not control \(\Pi_G\), which needs pointwise or \(L^\infty\)-type control of \(\mathrm{II}^\circ\) on the slice.
- Cheeger–Tian supplies such control only under \(|\mathrm{Ric}|\le3\).
- Ge–Jiang's critical-metric examples show that \(L^2\) smallness alone does not supply it in general.
- Possible substitutes are a selection principle (for example the \(P+\varepsilon R_1\) penalization of package §8) or a coarea estimate bounding \(\int_Y|\mathrm{II}^\circ||\mathrm{Rm}_Y|\) by local \(\widehat P\) plus curvature energy.
- The finite-charge class of §6 shows that without such control the charge genuinely moves.