# Step 23 — Scalar-relaxed angular construction, CR pinning, and long-cell certification

## 1. Exact-ended objective after conformal normalization

The sign-free exact-CH conformal theorem has the stronger consequence
\[
\inf_{{\cal C}_{\rm exact}}P
=\inf_{{\cal C}_{\rm exact}}J_6
=\inf_{{\cal C}^{\rm aCH,\mu}_{-24}}P\qquad(2<\mu<2+2\sqrt3).
\]
Indeed, \(P\le J_6\) on exact-ended metrics. Conversely, normalize any exact-ended \(P\)-competitor to \(\widehat g=u^2g\), so \(P(\widehat g)\le P(g)\) and \(J_6(\widehat g)=P(\widehat g)\), and splice \(\widehat g\) back to an exact collar. The squared residual on the splice is \(O(e^{(4-2\mu)R})\), so \(\mu>2\) suffices for this direction. The reverse comparison with the normalized decay class uses the proved normalization decay only below \(2+2\sqrt3\); equality for arbitrary larger \(\mu\) is not established. The stronger \(m>4\) in the conformal theorem is used to remove the linear Chern--Gauss--Bonnet transgression and integration-by-parts flux in the *selection identity*. In particular, the observed \(r e^{-4r}\) tail belongs to every normalized class with \(2<\mu<4\), but not to the endpoint \(O(e^{-4r})\). The theorem note `step22_exact_CH_conformal_reduction.md` has been corrected accordingly.

This changes the upper-construction standard: a rigorously controlled exact-ended \(P<8\pi^2\) cell is enough for the \(J_6\) transfer after the normalization-and-recovery construction. It does not establish attainment.

## 2. Scalar-relaxed \(j=1\) angular block

Script: `workspace/scripts/angular_isotype_conformal.py`.

The script extends the Step-22 globally smooth angular probe in two ways. Its higher-order runs use the single coefficient \(\sqrt3\,\mathrm{Ad}(q)_{00}\); because the anisotropic base is not right-SU(2)-invariant, that is a compression of the full fixed-left-row \(j=1\) tensor space, which also contains \(\mathrm{Ad}_{01}\) and \(\mathrm{Ad}_{02}\). A `--fullmult` option now includes all three and was run at radial order two.

1. The metric perturbation uses a radial Chebyshev basis multiplied by \(u^2(1-u)^3\), all six off-diagonal orthonormal-frame tensors, and three diagonal differences. The pure trace metric direction is deliberately omitted because it is first-order redundant with the conformal variable.
2. A simultaneous angular conformal field in the same single angular coefficient
   \[
   \phi=\sqrt3\,\mathrm{Ad}(q)_{00}\,u^2(1-u)^4\sum b_nT_n(2u-1)
   \]
   is included. The Schur complement in the \(b_n\) block approximates the optimal scalar response. The script also computes the kernel of the sampled scalar-coupling matrix \(H_{\phi h}\), which approximates tangency to \(Ds[h]=0\).

The Haar mean and Gram matrix are exact to approximately \(2\times10^{-16}\), and the base value at 192 radial nodes is
\[
J_6/(8\pi^2)=0.995178186608463,
\]
within \(5.7\times10^{-13}\) of the independently evaluated stored value.

Canonical data:

- `data/angular_isotype/j1_fullmult_tf_conformal_r2p8_q128.json` (all three fixed-left-row multiplicity components at radial order two)
- `data/angular_isotype/j1_tf_conformal_r2p10_q160.json`
- `data/angular_isotype/j1_tf_conformal_r4p12_q160.json`
- `data/angular_isotype/j1_tf_conformal_r6p16_q192.json`

The full-multiplicity order-two calculation has the expected threefold spectrum and the same minima as the single-coefficient calculation: raw \(0.8957496\), relaxed \(0.8750491\), with positive two-sided line tests. Thus the original single-coefficient pilot did not miss a lower order-two multiplicity direction. The lowest generalized values in the higher-order single-coefficient trace-free basis are:

| radial order | raw | scalar-relaxed | sampled scalar-kernel |
|---:|---:|---:|---:|
| 2 | 0.8957496 | 0.7499216 | 0.8957496 |
| 4 | 0.1782308 | 0.1782308 | 0.1782308 |
| 6 | 0.1209451 | 0.1209451 | 0.1209451 |

All are positive. Here “tested \(j=1\) space” means the full multiplicity only at radial order two and the single-coefficient compression at orders four and six. Two-sided actual-metric line tests at amplitudes \(10^{-3},5\cdot10^{-4},2.5\cdot10^{-4},1.25\cdot10^{-4}\) reproduce the Hessian values; for the order-six lowest direction, the even quotients are about \(0.12094\) and both signs raise \(J_6\). No negative construction direction appears in this tested \(j=1\) space.

In the single-coefficient order-two calculation with a larger conformal basis, scalar relaxation lowers a coupled branch enough that it becomes the new ground branch at \(0.74992\); it does **not** lower the original raw ground eigenvector from \(0.89575\). In the matched full-multiplicity \(n_\phi=8\) calculation the corresponding relaxed triplet is \(0.8750491\). The scalar-coupling matrix detects only orthogonality against the sampled conformal test space, not the pointwise equation \(Ds[h]=0\). At orders four and six the compressed global minimum is numerically in this sampled coupling kernel and has negligible optimal conformal coefficients, but other relaxed levels (notably \(0.28253\) and \(0.14447\)) descend strongly. Thus no negative direction is seen, while the coupled scalar-relaxed sector remains scientifically important.

The decreasing sequence \(0.8957,0.1782,0.1209\) is important: these are finite compression values, not a proof of a positive spectral lower bound. They do not yet cover the full \(j=1\) multiplicity, and the conformal space vanishes at the finite collar rather than carrying the exact decaying exterior solution of \((-6\Delta+48)v=-Ds[h]\). More radial order with all three \(\mathrm{Ad}_{0b}\) coefficients for tensors and scalars, a direct scalar residual solve with transparent exterior response, a better-conditioned localized basis, exact Lie-derivative modes, and geometric gauge quotient are still required. In particular, positive finite blocks do not establish unrestricted local minimality. The two-sided paths are finite first-order conformal responses, not exactly scalar-normalized nonlinear paths; a genuine construction must solve the Yamabe equation for each amplitude and evaluate \(P=J_6\).

A false near-zero branch appeared when the pure trace tensor was allowed simultaneously with the conformal factor. Its metric coefficients were equal in all four diagonal slots and the conformal coefficient cancelled them pointwise. This was parameter redundancy, not a geometric mode; omitting pure trace repaired it. This illustrates why scalar elimination must be formulated geometrically rather than by stacking redundant fields.

## 3. CR-pinning identity checked independently

The peer identity in `S1003A02/workspace/scripts/cr_pinning_check.py` was rerun. With
\[
\widetilde\Phi=q+\frac14(y_g-y_h)-\zeta\sinh q,
\]
the symbolic controlled system gives exactly
\[
\widetilde\Phi'=\zeta^2G-\frac14(e_g-e_h)
=\zeta^2G-\frac14(\mathrm{Ric}^\circ_{gg}-\mathrm{Ric}^\circ_{hh}).
\]
The CH and real-hyperbolic substitutions have zero residual, and a randomly forced numerical solution satisfies the integrated identity to \(6.97\times10^{-16}\). The CH volume factor check gives \(We^{-4t}\to1/16\), so \(\int_T^\infty dt/W\sim4e^{-4T}\). Combining these facts with Cauchy--Schwarz reproduces the peer's sharp pinning scale \(\widehat P\gtrsim\frac12e^{4T}(\Delta\widetilde\Phi)^2\) when the drift is controlled.

This observable is the nonlinear counterpart of the same antisymmetric channel controlled by the Step-19 exterior response. In the linearized CH variables, the interior Rossi mismatch is \(C_{\rm CR}^{\rm int}=k\Theta+\tfrac12w_0G=-\delta/2\), so \(E_{\rm ext}=4(C_{\rm CR}^{\rm int})^2/I\) has the same asymptotic constant \(\tfrac12e^{4T}\) as sharp CR pinning. A unified terminal map should retain the finite-radius canonical port (metric/first jet or \((w_0,\Theta)\)) and may record its derived CR projection, with the nonlinear drift integral accounting for departure from the ACH curve. The two bounds must not be added as independent penalties, since that would count the same antisymmetric mismatch twice. This identification is currently diagonal and antisymmetric; it does not yet control general angular CR deformations.

## 4. Why the corrected long-cell Arb integrations fail

Script: `workspace/scripts/arb_piece_diagnose.py`. Data:

- `data/perp_tail/arb_diag_x0038_X256_p32.json`
- `data/perp_tail/arb_diag_x003_X64_p32.json`

The failure is not a single isolated physical subinterval. Direct complex-box evaluation with equal real and imaginary half-width \(1/64\) makes the Chebyshev exponentials in the spectral representation explode. For the corrected degree-24 \(x_0=.038,X=256\) profile every one of 32 boxes loses denominator separation; \(GH\) and \(G\) enclosures become infinite or cross zero. Even the previously certifiable degree-16 \(x_0=.03,X=64\) profile fails this crude box test at the same width, showing that the test is deliberately much harsher than Arb's adaptive ellipses. Nevertheless it explains why merely splitting the integration interval while retaining global high-degree Chebyshev profiles does not cure the long-cell enclosure: complex growth of the global basis, not loss of positivity on the real metric, dominates the interval dependency.

The constructive repair should change representation rather than increase precision or repeat equal pieces. The profile should be converted into physical-radius subdomains with local low-degree Chebyshev/Taylor expansions, each accompanied by interval remainders and real positivity bounds for \(F,G,e^w\). The already certified \(x_0=.03,X=128\) value remains the transfer input until this local representation is implemented.

## 5. Mathematical interpretation

Scalar elimination is now structurally incorporated into the angular construction search. Within the tested fixed-row \(j=1\) block, it finds no lowering direction after pure-trace redundancy is removed, but the finite Ritz values are still falling with radial order. The next informative angular computation is therefore not another single bump; it is a higher-order full-multiplicity, localized and better-conditioned radial basis plus the exact scalar solve/exterior response, exact Lie-derivative projection, and Ward identities. Independently, CR pinning narrows the diagonal degeneration problem to standard-CR noncollapse, collapsed connectors, large bolts, and other non-Euclidean necks. The unrestricted Einstein-gap problem remains much broader than this cell branch, but these calculations sharpen which local and degeneration mechanisms remain viable.
