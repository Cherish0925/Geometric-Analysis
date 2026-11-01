# TTCS Independent Branch Record

```json
{
  "step_id": 46,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step46_o10_finite_marked_block_and_spinor_matching.md",
    "Sessions/S1003A01/workspace/scripts/step46_o10_block_matching.py",
    "Sessions/S1003A01/workspace/data/step46/o10_block_matching.json",
    "Sessions/S1003A01/workspace/notes/step45_o10_cell_tiling_tidal_radius_charge.md",
    "Sessions/S1003A01/workspace/data/step45/tnads_cartan.json",
    "Sessions/S1003A02/workspace/scripts/verify_gh_tangent.py",
    "Sessions/S1003A02/trace/ttcs/results/step2_ttcs01_generator2_integration.md",
    "Skills/geometric-analysis/research/sources/archive/sources/20261001-web-increment/Line1_Web_Increment_20260929_30/research/B/O10_Resolvent_Prolongation.md",
    "Skills/geometric-analysis/research/sources/continuation/20260926_actual_topological_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_actual_torsion_prolongation.md"
  ]
}
```

## Task

Read the Step-46 note and its computation against the inherited O10 equations and the exact TN/TNAdS sources. Check especially: (i) why a periodic one-compatible-nut block is topologically inadmissible; (ii) the distinction among circle Chern degree, scalar mass flux, and determinant/torsion boundary data; (iii) the half-order expansion Phi=Phi0+L chi1+..., the coefficient a=sqrt(2)/3, and the exact parent Hessian-energy calculation; (iv) the Hermite jet interpolation identity and its four-dimensional collapsed-cell scaling; (v) the correction that the raw TN field requires a leading q-pairing rather than solving the normalized resolvent equation at the flux-balance radius; and (vi) whether the finite marked-block problem states the correct residual and Cauchy scales. Identify any mathematical error, convention ambiguity, missing hypothesis, or stronger consequence. Give corrected formulas where needed.

## Output

# Verification Memo: Step 46 — Finite Marked Block and Spinor Matching

## Summary

The mathematical content of Step 46 is correct in all six areas examined. Every formula, scaling law, and numerical value I checked reproduces from the stated definitions and the exact TN/TNAdS geometry. Below are the detailed verifications and two observations that strengthen the note.

---

## (i) Topological inadmissibility of periodic one-nut cells

The argument is a direct application of the Bianchi identity for a principal $U(1)$-bundle. For a $U(1)$-bundle with connection over a compact oriented 3-manifold $Y$ with boundary $\partial Y$, the curvature $F$ satisfies $dF = 0$, so Stokes gives $\int_{\partial Y} F/(2\pi) = 0$. If opposite faces of a one-nut Wigner–Seitz cell are periodically identified, the orbit space of the free circle action becomes a punctured 3-torus $T^3 \setminus B$, whose boundary is the small 2-sphere $\partial B$ around the nut projection. The Hopf fibration restricted to $\partial B$ has Chern number $+1 \neq 0$, contradicting Stokes. The argument is correct and does not require any PDE input. ✓

---

## (ii) Three-flux distinction

The identity (1.1) is verified by direct computation. Starting from $m = |v|^2$ and $q = (\nabla^*\nabla - 2)v$ with $\nabla^*\nabla$ the positive connection Laplacian:
$$
\Delta_{\rm dg}\, m = 2\operatorname{Re}\langle -\nabla^*\nabla\, v,\, v\rangle + 2|\nabla v|^2 = 2|\nabla v|^2 - 4m - 2\operatorname{Re}\langle q, v\rangle.
$$
Integration over a domain gives (1.1). On a closed manifold, this becomes $\int|\nabla v|^2 = 2\int m + \operatorname{Re}\int\langle q,v\rangle$, which is identically satisfied by definition of $q$. On a domain the boundary flux $\Phi_m$ is nontrivial.

The note correctly observes that the scalar mass flux can be made $o(\ell^2)$ by choosing the balance radius, while the geometric circle degree remains $+1$ — these are independent. The determinant/torsion boundary data constitute yet a third layer of information. ✓

---

## (iii) The coefficient $a = \sqrt{2}/3$ and the parent Hessian energy

**Coefficient derivation.** The torsion formula from the prolongation source gives $\tau = \rho(k_1+ik_2,\, -k_3-ik_4)$ in spinor components. For $\Phi_0 = \sqrt{\rho_*}\,e_1$ (parallel) and $\chi = a\bar{f}\,e_2$ (with $e_2$ parallel), the perturbation has $(h_j, k_j) = (0,\, a\cdot e_j\bar{f})$. In the orthonormal frame of the Gibbons–Hawking metric $g = H\,dx\cdot dx + H^{-1}(d\psi+\omega)^2$:
$$
e_a = H^{-1/2}\partial_{x_a}\quad(a=1,2,3),\qquad e_1(\bar{f}) = H^{-1/2},\qquad e_2(\bar{f}) = -iH^{-1/2},\qquad e_3(\bar{f}) = e_4(\bar{f}) = 0.
$$
The type-$(1,0)$ projection $k_1 + ik_2 = a(e_1(\bar f)+ie_2(\bar f)) = 2aH^{-1/2}$ doubles the magnitude relative to $|d\bar{f}|^2 = 2/H$. Thus $|\tau_{\rm lin}|^2 = \rho_*^2 a^2 \cdot 4/H$ while $|v|^2 = (m_*/2)(2/H) = m_*/H$. Matching $|\tau_{\rm lin}| = |v|$ gives
$$
4a^2\rho_*^2 = m_*,\qquad a = \frac{\sqrt{m_*}}{2\rho_*} = \frac{8\sqrt{2}/9}{8/3} = \frac{\sqrt{2}}{3}.
$$
The factor-of-$\sqrt{2}$ difference from the naïve estimate $a\rho_* = \sqrt{m_*/2}$ arises because the torsion formula uses the $(1,0)$-projection $k_1+ik_2$, which has squared norm $4|k|_{\rm base}^2$, not $2|k|_{\rm base}^2$. ✓

**Hessian energy.** With $e_2$ parallel, $\nabla^2\chi = a\nabla(d\bar{f})\otimes e_2$ and $\nabla v = \sqrt{m_*/2}\nabla(d\bar{f})$, so $|\nabla^2\chi|^2 = (2a^2/m_*)|\nabla v|^2 = (9/32)|\nabla v|^2$. Cross-check: $2a^2/m_* = 2(2/9)/(128/81) = (4/9)(81/128) = 324/1152 = 9/32$. ✓

Integrated energy:
$$
\int_{B_R}|\nabla^2\chi|^2 = \frac{9}{32}\cdot 8\pi^2\cdot\frac{128}{81}\cdot\ell^2\Bigl(\frac{R}{R+\ell}\Bigr)^2 = \frac{32\pi^2}{9}\,\ell^2\Bigl(\frac{R}{R+\ell}\Bigr)^2.\quad\checkmark
$$

Density per normalization volume $4\pi^2\ell^2$: $(32\pi^2/9)/(4\pi^2) = 8/9$. ✓

**Half-order scaling.** In cell coordinates $X = x/L$, $\bar{f} = L\bar{F}(X)$, so $\chi = aL\bar{F}\,e_2 = L\chi_1(X)$. This is order $L$, not $L^2$. The physical first derivative $|\nabla\chi| = a|d\bar{f}| = a\sqrt{2/H} = O(1)$ at the cell boundary. ✓

---

## (iv) Hermite jet interpolation and collapsed-cell scaling

**Identity verification.** The unique minimizer of $\int_0^L|u''|^2$ among $H^2$ functions with prescribed endpoint jets $(u_0, p_0, u_1, p_1)$ is the cubic Hermite polynomial. Solving the boundary conditions for the cubic $u = aR^3+bR^2+cR+d$, substituting, and collecting gives:
$$
\int_0^L|u''|^2 = \frac{12}{L^3}\alpha^2 + \frac{\beta^2}{L},\quad \alpha = u_1-u_0-\tfrac{L}{2}(p_0+p_1),\quad \beta = p_1-p_0.
$$
I reproduced this by explicit computation of $12a^2L^3+12abL^2+4b^2L$, with the cross terms cancelling. ✓

**Reset cost.** For $u_0 = u_1 = 0$, $p_0 = p_1 = p$: $\alpha = -Lp$, $\beta = 0$, energy $= 12p^2/L$. Per four-dimensional cell of volume $L^6$ with transverse face volume $L^5$, the density is $12p^2L^5/(L\cdot L^6) = 12p^2/L^2$. JSON confirms `reset_times_L2` $= 12$ for all tested $n$. ✓

**Coherent jet.** With $\alpha = O(L^2)$ and $\beta = O(L)$: energy per fiber $= O(L)+O(L) = O(L)$; density per cell $= O(L)\cdot L^5/L^6 = O(1)$. ✓

**Convergence test.** For $u = \sin(2\pi x)$: $\int_0^1|u''|^2 = (2\pi)^4/2 = 779.2727\ldots$. JSON at $n=256$: `smooth_sine_energy` $= 779.27272788$, relative error $5\times 10^{-10}$. ✓

**One point to make explicit.** The extension from the one-dimensional scalar argument to four-dimensional spinor sections uses parallel transport in the normal direction to reduce each fiber to a scalar problem. In a parallel-transport gauge along the normal, $\nabla_\nu$ becomes $\partial_\nu$ component-wise, and the scalar Hermite estimate applies to each spinor component. Non-negative contributions from tangential second derivatives and connection curvature only strengthen the bound. This step is implicit in the note and is valid.

---

## (v) Mass equation mismatch of the raw TN field

The raw TN field satisfies $\nabla^*_{\rm TN}\nabla_{\rm TN}v = 0$, so $q = -2v$ and $\operatorname{Re}\langle q,v\rangle = -2m$. The mass flux on TN is then:
$$
\Phi_m = 2E - 4M + 4M = 2E.
$$
At the balance radius $R_* = (3/4)^{1/3}L$ where $2E = 4M$:
$$
\operatorname{Re}\int\langle q,v\rangle = \tfrac{1}{2}(2E-4M-2E) = -2M = -E.
$$
The numerical coefficient: $E/\ell^2 \to 8\pi^2 m_* = 1024\pi^2/81 = 124.771\ldots$, and $M/\ell^2 = (16\pi^2/3)m_*(3/4) = 512\pi^2/81 = 62.386\ldots$. JSON: `tangent_energy_over_ell2` → 124.728 at $L = 0.0125$ (converging to 124.771), `tangent_mass_over_ell2` $= 62.386$ exactly (independent of $L$ because $R^3/\ell = c^3 = 3/4$ at $R = cL$, $\ell = L^3$), and `raw_profile_required_q_pairing_over_ell2` $= -124.771$ exactly. ✓

The independence of the last quantity from $L$ is a consequence of $-2M/\ell^2 = -1024\pi^2/81$ being an exact expression when $R = cL$. ✓

The note's conclusion is correct: $q = -2v$ is far from zero. The pairing $\operatorname{Re}\int\langle q,v\rangle = -E \sim -124.77\,\ell^2$ is of the same order as the block volume $\sim 4\pi^2\ell^2$. The O10 requirement $\|q\|_{L^2} = o(\ell)$ (i.e., $\operatorname{Re}\int\langle q,v\rangle = o(\ell^2)$) is violated at leading order. ✓

---

## (vi) Residual and Cauchy scales in the finite marked-block problem

**Interior residual scales.** The conditions $\|q_L\|_{L^2} = o(L^3)$ and $\|t_{\Phi_L}-v_L\|_{H^1} = o(L^3)$ correspond to squared errors $o(L^6)$ per block of volume $\sim L^6$. These are the correct normalized-$L^2$ conditions for a phase with $O(V/L^6)$ blocks. ✓

**Expansion.** $\Phi_L = \Phi_0 + L\chi_1 + L^2\chi_2 + \cdots$ is the half-order expansion established in (iii). The first correction is $O(L)$, not $O(L^2)$. ✓

**Cauchy data (6.4).** The five quantities $(\Phi_L,\, \nabla_\nu^{A_L}\Phi_L,\, A_L^{\rm tan},\, v_L,\, \nabla_\nu^{3A_L}v_L)|_{Y_L}$, together with the four invariants (degree, mass flux, determinant Chern–Simons, torsion index), constitute the complete boundary output. Prescribing fewer data would leave the block underdetermined. ✓

**Joining law (6.5).** The conditions $\nabla_A\Phi_j - G_{ij}\nabla_A\Phi_i = O(L)$ and $\Phi_j - G_{ij}\Phi_i - (L/2)(\nabla_\nu^A\Phi_j + G_{ij}\nabla_\nu^A\Phi_i) = O(L^2)$ ensure that the Hermite affine defect is $O(L^2)$ and the slope defect is $O(L)$, giving bounded Hessian density:
$$
\frac{12|O(L^2)|^2}{L^3}+\frac{|O(L)|^2}{L} = O(L) \quad\text{per fiber},\qquad \frac{O(L)\cdot L^5}{L^6} = O(1)\quad\text{density.}\quad\checkmark
$$

**Boundary scaling verification from JSON.** At $L = 0.0125$:

| Quantity | Formula | Computed | JSON |
|---|---|---|---|
| $(H-1)/L^2$ | $1/c = (4/3)^{1/3}$ | 1.10064 | 1.10064 |
| $(F-1)/L^2$ | $c^2/3 + O(L^2)$ | 0.27526 | 0.27526 |
| $(1-m/m_*)/L^2$ | $1/(c+L^2)$ | 1.10045 | 1.10045 |
| $(\partial_\nu m)/L$ | $m_*/c^2 + O(L^2)$ | 1.914 | 1.914 |
| $|\nabla v|^2/L^2$ | $m_*/c^4 + O(L^2)$ | 2.317 | 2.317 |

All entries match. ✓

---

## Additional observations

**Observation 1 (volume density cancellation).** The four-volume density $16\pi^2 R\ell(R+\ell)\,dR$ is the same for TN and TNAdS because the factors of $F$ cancel in $\sqrt{\det g}$:
$$
\sqrt{(H/F)(HR^2)^2(\ell^2 F/H)} = HR^2\ell = R\ell(R+\ell).
$$
This exact coincidence means that the normalization-cell volume $4\pi^2\ell^2$ and the balance-radius condition $2E = 4M$ are metric-independent within the TN/TNAdS family. The field extension problem on TNAdS therefore inherits the same volume bookkeeping as TN, even though the Laplacian and connection change.

**Observation 2 (the $W^-$ ratio).** The exact relation $|W^-_{\rm TNAdS}|^2/|W^-_{\rm TN}|^2 = (1-\ell^2/3)^2$ (Step 45, independent of $R$) means that the opposite-Weyl curvature at the cell boundary is essentially unchanged by the Einstein continuation. Since $\ell = L^3$ and $L \ll 1$, this ratio is $1 - O(L^6)$. The divergent Weyl density that drives the O10 concentration scenario therefore originates entirely from the TN core geometry, not from the Einstein correction. This strengthens the note's statement that "the Einstein continuation changes the Ricci part of the curvature by $O(1)$...while leaving $W^-$ essentially that of TN."

---

## No mathematical errors found

Every formula, coefficient, scaling argument, and numerical value in the Step 46 note and its associated computation is correct. The topological obstruction, the half-order expansion with $a = \sqrt{2}/3$, the Hermite identity, the mass-equation mismatch, and the finite-block formulation are all mathematically sound. The open problems (field extension on TNAdS, covariant joining compatibility, global degree cancellation) are correctly identified and sharply stated.