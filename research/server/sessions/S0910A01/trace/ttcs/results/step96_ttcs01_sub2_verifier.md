# TTCS Independent Branch Record

```json
{
  "step_id": 96,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step96_source_compatible_kernel_map.md",
    "Sessions/S0910A01/workspace/data/step96_source_receiver_decomposition.json",
    "Sessions/S0910A01/workspace/data/step96_kernel_plane_ab_map.json",
    "Sessions/S0910A01/workspace/scripts/step96_source_receiver_decomposition.py",
    "Sessions/S0910A01/workspace/scripts/step96_kernel_plane_ab_map.py",
    "Sessions/S0910A01/workspace/notes/step95_gauge_obstruction_and_kernel_plane.md",
    "Sessions/S0910A01/workspace/notes/step89_correction_and_relative_green.md",
    "Sessions/S0910A02/workspace/notes/step93_ttcs_audit_of_kernel_plane_and_A01_step95.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 96 product-orbifold source-compatible kernel-plane reconstruction. Please read the files and give a mathematical memo on: (i) whether the Ozuch H^4 boundary source is correctly treated as a quadratic Sym^2(K) source rather than a scalar receiver adjoint; (ii) whether the scripts' conclusion that the Step89 odd adjoint identity holds for diagonal entries but fails for the off-diagonal/double-angle entry is consistent with the formulas; (iii) whether the AB-sector propagated map is a valid restricted sample and recovers the old K_adj only as one entry; (iv) what assumptions or missing components still prevent an obstruction/existence theorem. Do not decide the whole session; focus on correctness, source compatibility, and mathematical limitations of this Step 96 artifact.

## Output

# Verification Memo — Step 96 product-orbifold source-compatible kernel-plane reconstruction

Session S0910A01. Prepared in a clean context after reading the two notes (Step 95, Step 96), the two data files, both scripts, the Step 89 correction note, the A02 Step 93 integration note, and the relevant passages of Ozuch (Prop. 1.16, Rem. 1.18, §2.1, Prop. 2.10, Prop. 2.19, §3.3).

## Summary judgment

The Step 96 artifact is mathematically coherent and represents a genuine structural correction of Step 95, not a cosmetic one. The three positive assertions requested — quadratic source, diagonal-versus-off-diagonal identity, restricted AB sample — are internally consistent with the stated formulas and reproduce the earlier exact anchors to machine precision. The artifact does not by itself yield an obstruction or existence statement, and the note is accurate about why. Below I give the substance for each item and the two places where independent recomputation, not internal consistency, would be needed to fully certify the construction.

## (i) The H⁴ source is correctly a quadratic Sym²(K) object

This is correct and is the mathematically right object.

Ozuch's asymptotic term is $H^4(\zeta^+) = -\rho(\zeta)^-\circ\zeta^+/(2r^4)$ (Prop. 1.16(1)). By Definition 1.14, $\rho_x(\zeta)$ is **linear** in $\zeta$ and $\zeta^+$ is linear in $\zeta$, so $H^4(\zeta^+)$ is genuinely **quadratic** in the insertion direction $\zeta$. Rem. 1.18 makes this explicit: $d_{\mathbf e}\mathbf R^-(H^4(\zeta^+)) = 12\,\pi_{\rm tr}(\rho(\zeta)^-\otimes\rho(\zeta)^-)/r^6$, manifestly quadratic.

On the receiving side, the first-obstruction functional (Prop. 2.10, §2.1.4) reads the $2\times2$ curvature block $\{R_{22},R_{33},R_{23}\}$ in the plane orthogonal to the receiver insertion direction, i.e. it is quadratic in the receiver direction $\zeta_j$. The inter-node coefficient is therefore (quadratic in $\zeta_i$) $\times$ (quadratic in $\zeta_j$), i.e. a map
$$\operatorname{Sym}^2(K_i)\longrightarrow \operatorname{Sym}^2(K_j),\qquad K_j=\ker R^{\epsilon_j}=\operatorname{span}\{e_2,e_3\}.$$
Step 96 §4 states exactly this. The Step 95 reduction to a single scalar $K_{\rm adj}$ (a bilinear form in one direction) collapsed a $3\times3$ finite-dimensional map to one entry. Restoring the full $\operatorname{Sym}^2$ structure is the correct move, and it is what makes the residual double-angle information visible. The withdrawal of the Step 95 "$K_{\rm even}+K_{\rm adj}=0 \Rightarrow -2K_{\rm adj}\neq0$" argument follows correctly, because that argument presumed a scalar response and a signwise transfer from the all-compatible Kähler–Einstein row to the mixed row that the map structure does not support.

## (ii) Diagonal identity holds, off-diagonal/double-angle departs — consistent with the formulas

This is internally consistent and does not contradict Step 89; it sharpens it.

Note first that Step 89 defined its receiver as a **single matrix entry**, $R_{\rm odd}(H)=\tfrac12[(\delta R^+)_{22}-(\delta R^-)_{22}]$, with insertion $\zeta=\omega_2$. Its exact identity $S_{\rm odd}=\tfrac{\pi^2}{2}R_{\rm odd}$, verified on the 100-dimensional symmetric-Hessian basis, was therefore always a **22-entry** statement. Step 96 extends the receiver to the full $2\times2$ block (entries 22, 33, 23) and finds:

- $S_{\rm odd,22}=\tfrac12 R_{\rm odd,22}$ and $S_{\rm odd,33}=\tfrac12 R_{\rm odd,33}$ to residual $\sim5.3\times10^{-17}$ (machine zero). The 33 case follows from 22 by the $e_2\leftrightarrow e_3$ symmetry of the construction, so this is a real internal cross-check, not an independent input.
- $S_{\rm odd,23}$ has a nonzero residual against $R_{\rm odd,23}$: least-squares coefficient exactly $0.5$ (same as the diagonal), residual $\ell_2 = 0.35355 = 0.5/\sqrt2$, relative residual $1/\sqrt2$, worst component $0.125$ at Hessian entry $((0,0),(0,1))$.

The factor bookkeeping is consistent: the scripts work with $S/\pi^2$, so "$S_{\rm odd}/\pi^2=\tfrac12 R_{\rm odd}$" matches Step 89's "$S_{\rm odd}=\tfrac{\pi^2}{2}R_{\rm odd}$." The source coefficient $-1/16$ per chirality reconstructs Step 89's $-1/32$ for the half-difference $S_{\rm odd}=(S^+-S^-)/2$, and reduces to Step 89's four-term sparse form $D:H=-8H_{01,23}+8H_{03,12}+8H_{12,03}-8H_{23,01}$. So the diagonal identity is reproduced, and the off-diagonal departure is a genuinely new observation about the double-angle ($\zeta_2\zeta_3$) part of the quadratic source that lives outside the simple curvature-receiver span. This is exactly what "the source is a full $\operatorname{Sym}^2$ form, the receiver only captures its trace-like part" predicts. The even-chirality residuals (relative $0.7528$ against the odd receiver span, with rational fit coefficients $1/12,-5/12$) are also consistent: the even source is not adjoint to the odd receiver, so a large residual is expected.

One recheck worth naming: the identity rests on the index conventions encoded in `curvature_block_coeff` (the receiver, using $\delta R_{abcd}=\tfrac12(H_{ad,bc}+H_{bc,ad}-H_{ac,bd}-H_{bd,ac})$) and in `SCOEFF` (the source, $-\tfrac1{16}\sum_b C_{ab}\otimes C_{cb}$ with the $S^3/\mathbb Z_2$ factor). The machine-precision reproduction of the Step 89 22-entry identity strongly supports these conventions, and the code's own integrality check on $C_{ab}$ guards the trace-free involution algebra. What internal consistency cannot certify is whether the overall constant (the "3∫" of Prop. 2.10 and the $\pi^2$/RP³ factor) is placed correctly relative to the true first-obstruction normalization; that was debugged once in Step 89 (the $H$-versus-$V_2$ factor of $\tfrac12$), so it is plausible but is the single arithmetic input I could not derive from first principles here.

## (iii) The AB-sector map is a valid restricted sample and recovers K_adj as one entry

This is sound, and the note draws the right line around it.

The propagation uses matched one-form jets on the two $S^2$ factors, cross-factor (AB) Hessians $h=\alpha_A\odot\beta_B$, and a heat-regularized product Green weight $\text{pref}=e^{-\tau P}/(P\,\mu_A\mu_B)$ with $P=\tfrac12(\mu_A+\mu_B)-1$. For all AB modes $\ell_A,\ell_B\ge1$, $P\ge1>0$, so the regularized inverse is well defined and the mode $q=g_A-g_B$ with $Pq=-1\cdot q$ (Step 89 §4) does not enter this sector — that mode is a same-factor tensor mode, not an AB cross mode, which is exactly why the note excludes it from this sample.

Checks that hold up:
- The heat ladder $(\tau,L)=(0.1,80),(0.05,120),(0.02,180),(0.01,260)$ stabilizes every compact-map entry to $\pm0.03144249732$ with tail indicators $10^{-107}$ to $10^{-131}$, so the displayed numbers are converged in the modes summed.
- $K_{\rm adj}^{AB}=-0.03144249732$ is recovered as the single odd/odd $R_{22}\leftarrow\zeta_2^2$ entry (`old_scalar_checks.odd_odd_R22_source22` = `expected_step91_AB_adjacent`). It is one of several equal diagonal entries in a rank-one $\begin{psmallmatrix}1&1&0\\1&1&0\\0&0&0\end{psmallmatrix}$ block, with the $R_{23}$ row/column and the $\zeta_2\zeta_3$ column identically zero.
- The independent axial $\ell=1$ check drifts monotonically ($-0.0636,-0.0669,-0.0689,-0.0696$) toward $-9/128=-0.0703125$, matching Step 89's $K^{11,\rm axial}\propto 9/128$. This is a cross-check between the exact asymptotic-value computation and the spectral propagation; the residual $\sim1\%$ gap is finite-$\tau$, and the trend is the right consistency signal. Note this axial coefficient and the AB-sector $-0.03144$ are different channels; the note keeps them separate and does not conflate them.

The structurally important point, correctly stated: the AB block responds only to the source **trace** $\zeta_2^2+\zeta_3^2$ and produces only the trace-like $R_{22}+R_{33}$ — it is blind to the anisotropic double-angle piece. That is precisely the residual $T$ isolated in (ii). Hence the AB sample cannot carry the very component that distinguishes the full map, and the note's warning that it "should not be extrapolated to the complete map" is not caution for its own sake but a direct consequence of the rank-one structure. This coherence between §2 (the local double-angle residual) and §3 (its invisibility in AB) is a real insight: the anisotropic response must be carried by the AA/BB tensor sectors.

One bookkeeping place to watch on cross-comparison: the compact-map $\zeta_2\zeta_3$ column is the matrix off-diagonal coefficient and must be evaluated with the factor $2\zeta_2\zeta_3$ (the code comments this). When comparing the AB `R23` column to the local-algebra $S_{\rm odd,23}$, this factor of 2 must be tracked to avoid a spurious mismatch.

## (iv) What still prevents an obstruction or existence statement

The enumeration in Step 96 §5 and A02 Step 93 §3 is accurate and matches the structure of Ozuch's own construction. The genuine missing pieces:

1. **AA/BB tensor sectors with the full jet.** The anisotropic residual $T$ established in (ii) is invisible to AB (iii) and must propagate through the electric/magnetic tensor-harmonic sectors, using complete node Hessians including same-factor components. The AB sample computes one restricted channel only.

2. **The receiver block is global, not local.** Ozuch Prop. 2.10 produces $\bar h^4$ by solving $P_{g_o}\bar h^4=\sum\nu_l\mathbf v_l+\sum\lambda_k\overline{\mathbf o}^4_k$ globally and then extracting the regular second jet at the receiving node. Identifying the true node-to-node block $\Pi_K Q_{ji}\Pi_K$ with the local algebraic adjoint or with the spectral $1/P$ propagation is not established; the $S^3/\mathbb Z_2$ pairing integral is one ingredient, not the block itself (A02 §3.1). The spectral map models this but does not realize it.

3. **Frame/projector motion at the same order as the target.** $K_j=(e_1^{\epsilon_j})^\perp$ and the rank-one image line move under the regular jet at order $t_i^2$ — the same order as the coefficient being computed. This projector correction is not yet in the reduced equation.

4. **Lower-order obstruction data.** Only $\mu_1=0$ (the rank-one determinant, Lemma 2.14) is in hand. $\mu_2,\mu_3$, the global $\nu_l$, and any orbifold deformation variable $v_2$ must be solved or shown to vanish in the residual symmetry sector before the projected equation is complete.

5. **Remainder ordering is the decisive bottleneck.** The inter-node term is $O(t_j t_i^2)=O(t^3)$ at comparable scales, while the estimate in the current record (Prop. 2.19) controls the residual only to $O(t^{5/2})$, and $t^3=o(t^{5/2})$. A nonzero $t^3$ coefficient therefore does not decide existence or nonexistence. Ozuch §3.3 (Prop. 3.14, Cor. 3.25) shows how a higher-jet expansion pushes the residual below the crude estimate — in the $T^4/\mathbb Z_2$ mixed-scale setting Cor. 3.25 reaches $\lambda_k^j+\mu_k^j=O(|\zeta^\pm|^2|\zeta^\mp|^5+|\zeta^\pm|^{3+\beta/12}|\zeta^\mp|^{4-3\beta/4})$. Transporting that template to $(S^2\times S^2)/\mathbb Z_2$ requires rebuilding the background, the kernel-plane projection, and the scale conventions; it is not importable verbatim, and it is the item that would convert a computed $t^3$ coefficient into a decisive statement.

Additionally, the whole product branch is a local desingularization model of one mixed-checkerboard configuration; even a complete resolution of items 1–5 would speak to Einstein metrics arising from that specific desingularization of one 4-dimensional orbifold, not to the $n\ge2$, all-signs Yau-26 proposition. The note states this in §5 and does not overreach.

## Net

Items (i)–(iii) are correct as stated and mutually reinforcing; the artifact reproduces the Step 89 diagonal identity and the Step 91 scalar as strict special cases, and it exposes a real anisotropic residual that the earlier scalar picture hid. The construction remains a reduction, not a theorem: the two things I could not certify from the material alone are the overall source normalization constant (plausible via the Step 89 reconciliation) and the identification of the spectral/local receiver with the true global node-to-node block. The decisive open analytic content is the sub-$t^3$ remainder expansion adapted from Ozuch §3.3, without which no obstruction or existence conclusion about the product-orbifold branch is supported by this Step 96 artifact.