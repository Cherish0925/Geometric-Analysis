# TTCS Independent Branch Record

```json
{
  "step_id": 81,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step81_L_exchange_and_radial_ledger.md",
    "Sessions/S0910A01/workspace/data/step81_L_symmetry_scale_ledger.json",
    "Sessions/S0910A01/workspace/data/step81_L_H4_transport.json",
    "Sessions/S0910A01/workspace/notes/step80_J_equivariant_all_order_reduction.md",
    "Sessions/S0910A01/trace/ttcs/results/step80_ttcs01_verifier1_integration.md",
    "Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 81 refinement of the positive mixed-row product-orbifold construction. User goal is Yau Problem 26; this is only a local positive-Einstein desingularization test. Read the notes/data and check: (1) the single-factor antipodal L(x,y)=(-x,y) really descends to the quotient, exchanges the two A-orbits, reverses 4D orientation, and swaps the plus/minus EH chiralities compatibly with the diagonal mixed assignment; (2) L transports the J-fixed radial direction omega2 with the stated sign and is compatible with the full angular H^4/rho_x formula, not a frozen-rho shortcut; (3) the surviving radial finite-dimensional response should be recorded as F_i=t_i sum_j B_ij t_j^2+R_i rather than sum_j B_ij t_j^3; (4) L symmetry constrains the candidate B matrix to [[a,b],[b,a]] only after fixing transported radial normalizations and does not force positive-scale balance; (5) identify any missing sign, normalization, order, self/cross-response, logarithmic, gauge, or shape-mode issue that must be handled before a real coefficient calculation can support or obstruct an Einstein desingularization.

## Output

# Verification memo — Step 81 single-factor exchange L and the radial scale ledger

## Summary judgment

The linear-algebra and symmetry content of Step 81 is correct and internally consistent, and it corrects two earlier errors soundly: the missing receiver factor `t_i` in the surviving radial response, and the mistaken idea that node-orbit exchange follows from `A`. The map `L` genuinely descends, exchanges the two `A`-orbits, reverses the 4-manifold orientation, and swaps `Λ^+↔Λ^-` compatibly with the diagonal mixed chirality. The transport sign on `ω_2` is `+1` and is consistent with the full `x`-dependent Ozuch `ρ_x`/`H^4` structure, not a frozen-`ρ` shortcut. The matrix form `[[a,b],[b,a]]` is correct once the two orbit radial normalizations are pinned by `L`-transport, and `a+b=0` is a genuine coefficient condition that symmetry does not supply.

What Step 81 delivers is a representation-theoretic reduction of one specific comparable-scale `A`,`J`,`L`-equivariant degeneration to a single decisive real number (the equal-scale cubic coefficient `a+b`). It does not produce an Einstein metric, and the analytical substance needed to define `a+b` rigorously — a remainder sharper than the current `O(t^{5/2})`, control of logarithms, and inversion against the indefinite `g_1-g_2` direction — is not yet in place. The full Yau‑26 statement is untouched by this local test.

---

## 1. `L` descends, exchanges orbits, reverses orientation, swaps chirality

**Descent.** Write `L=(ℓ_1,\mathrm{id})` with `ℓ_1` an orientation-reversing involution of the first round sphere sending `N↔S`. Both natural representatives — the reflection `\mathrm{diag}(1,1,-1)` and the sphere antipode `-I_3` — satisfy `ℓ_1 r_π = r_π ℓ_1` (check: `\mathrm{diag}(1,1,-1)\,\mathrm{diag}(-1,-1,1)=\mathrm{diag}(-1,-1,-1)=\mathrm{diag}(-1,-1,1)\,\mathrm{diag}(1,1,-1)`, and `-I_3` commutes with everything). Hence `L` commutes with `σ=(r_π,r_π)` and descends to an isometry of `(S^2\times S^2)/⟨σ⟩`. Because `ℓ_1` and `\mathrm{id}` are round-sphere isometries, `L` is an isometry of the product; this is required for every later step.

**Orbit exchange.** `L` fixes `N,S` on the second sphere and swaps `N↔S` on the first, so `NN↦SN`, `SS↦NS`, `NS↦SS`, `SN↦NN`. This maps orbit `1=\{NN,SS\}` onto orbit `2=\{NS,SN\}`, matching the node table exactly.

**Orientation and chirality.** The tangent representative `DL=\mathrm{diag}(1,-1,1,1)` has `\det=-1`. There is a genuine bookkeeping point worth stating: the ambient antipode restricts to `-I_2` on a sphere tangent plane (raw determinant `+1`), but it also reverses the outward normal, so relative to the intrinsic sphere orientations at `N` and `S` the map reverses orientation; the oriented-frame representative therefore carries `\det=-1`, and `\mathrm{diag}(1,-1,1,1)` is a valid such representative. With this matrix I reproduce the stated action on standard bases (`ω_2^{\pm}=e^{13}\mp e^{24}`, etc.):
$$
ω_1^+\mapsto -ω_1^-,\quad ω_2^+\mapsto +ω_2^-,\quad ω_3^+\mapsto +ω_3^-,
$$
so `Λ^+` maps to `Λ^-`. Since the diagonal orbit carries positive (SD) EH and the off-diagonal orbit carries negative (ASD) EH, an orientation-reversing isometry that exchanges the orbits and swaps `Λ^+↔Λ^-` is geometrically matched to the chirality assignment `ε(s_1,s_2)=s_1s_2`. This is a genuine geometric identification, not relabelling.

I also confirmed `DL`, `DJ=\mathrm{diag}(1,-1,1,-1)`, and `L∘A` are mutually consistent (`ℓ_1 α_1=r_π`, so `L∘A=(r_π,α_2)`; all commute), and that `J` acts as `\mathrm{diag}(-1,+1,-1)` on the SD basis, consistent with Step 80.

---

## 2. `ω_2` transport sign and full angular `H^4`

The insertion direction `ω_2` is the `+1` eigenline of `J` in each `Λ^{\pm}`, and `L` sends `ω_2^+\mapsto +ω_2^-`. Both statements are exact linear algebra, independent of sampling.

The `H^4`/`ρ_x` conventions used match Ozuch Definition 1.14 and Proposition 1.16(1): `ρ(ζ)^-_j=x^T(ζ^+\circ ω_j^-)x/|x|^2` and `H^4(ζ^+)=-\rho(ζ)^-\circ ζ^+/(2r^4)`. The angular repair from Step 79 is respected — the tested identity uses the true `x`-dependence, not a fixed vector. The reported exact-zero transport error over 20,000 `S^3` samples is what one expects for a genuine linear isometry intertwining the two EH structures (the identities are algebraic), and the sampled data are internally consistent: `\mathrm{diag}(-1,1,1)\,ρ^+(x)=ρ^-(Lx)` holds term by term. The induced `\mathrm{diag}(-1,1,1)` on `ρ`-components is exactly the `ω_1^+\mapsto -ω_1^-` sign, so nothing is contradictory. This part is sound.

---

## 3. The receiver factor: `F_i=t_i\sum_j B_{ij}t_j^2+R_i`

This scaling is correct and traceable to the paper. Two facts fix it:

- The Ozuch necessary condition (eq. 51) is `t_j\lambda_k^j+t_j^2\mu_k^j=O(t_{\max}^{5/2})`; the local first obstruction at a node enters with an explicit prefactor `t_j` (the "receiver" scale).
- A source bubble scales as `H^4(t_j\phi_j)=t_j^2H^4(\phi_j)` (Proposition 1.16(1): the leading term is quadratic in `ζ`). Its regular product-resolvent response reaching node `i` is `O(t_j^2)`, and it perturbs the receiver's first obstruction, which itself carries `t_i`. Thus the cross contribution is `t_i\,t_j^2` and the self contribution is `t_i^3` — exactly `F_i=t_i(B_{i1}t_1^2+B_{i2}t_2^2)`. The scale-blind `\sum_j B_{ij}t_j^3` drops the receiver factor and is wrong.

This is consistent with the Step 77 ledger `t_i\,\delta\lambda_{i,k}=t_i t_j^2\,\mathcal I_{ij,k}+\cdots`, and with `\mu_1=0` (rank-one determinant) removing the `t_i^2` term so that the first surviving radial order is cubic.

One quantitative tension must be foregrounded, and the note does state it: the current remainder `O(t_{\max}^{5/2})` is **larger** than the `t^3` signal for small `t` (`5/2<3`). The cubic coefficient is therefore below the present resolution. To make `B` meaningful one needs a refined approximate metric pushing the remainder to `o(t^3)`, i.e. the product-orbifold analogue of Ozuch §3.3 (the `\bar h^4,\bar h^8` and `\mathring H_{j,2m}` towers with obstruction-cancellation Lemmas 3.15/3.18). This is the dominant piece of unfinished analysis; it is not a minor refinement.

---

## 4. `[[a,b],[b,a]]` and the status of `a+b`

The relation `F_2(t_1,t_2)=F_1(t_2,t_1)` follows from `L`-equivariance and orbit exchange. Explicitly: `L` sends a configuration with `(orbit1,orbit2)` scales `(s_1,s_2)` to one with `(s_2,s_1)`, and `L`-invariance of the residual with the isometry-invariant `L^2` pairing gives `F_2(s_2,s_1)=F_1(s_1,s_2)`; renaming yields the stated identity. Feeding `F_i=t_i(B_{i1}t_1^2+B_{i2}t_2^2)` gives `B_{21}=B_{12}`, `B_{22}=B_{11}`, i.e. `[[a,b],[b,a]]`. The algebra is correct.

The equal-scale analysis is also correct: on `t_1=t_2=t>0`, `F_1=t^3(a+b)`, so vanishing needs `a+b=0`, which symmetry does not impose. For two positive scales, `B\,(t_1^2,t_2^2)^T=0` with `B=[[a,b],[b,a]]` (eigenvalues `a+b` on `(1,1)`, `a-b` on `(1,-1)`): a positive kernel vector requires the `(1,1)` eigenvector, hence `a+b=0` and `t_1=t_2`. So the decisive object is the single real number `a+b` (the equal-scale cubic coefficient). A nonzero value obstructs this comparable-scale `A`,`J`,`L`-equivariant degeneration at cubic order; a zero opens the next radial order along `t_1=t_2`, which then becomes the object.

**Normalization sign.** The `[[a,b],[b,a]]` form (as opposed to `[[a,b],[-b,-a]]`) depends on transporting the orbit-2 radial obstruction basis from orbit-1 by `L`. Because `L` swaps SD↔ASD, the orbit-1 obstruction tensor `o_1\sim -\theta_1^-\circ\theta_1^+/r^4` maps to an ASD-type tensor at orbit 2, and the pairing normalization (`\int\langle\cdot,o_k\rangle`) carries a definite factor. The note's `+1` is stated from `ω_2^+\mapsto+ω_2^-`, but that fixes only the insertion direction; the transport sign of the **full** `o_1` tensor and of the flux pairing has not been checked. The equal-scale condition `a+b=0` is insensitive to a global sign, but the two-scale kernel structure is not, so this sign controls the off-diagonal solution branch and should be pinned from the tensor `o_1` and the `L^2` flux pairing rather than from the `ω_2` line alone.

---

## 5. Scientific substance still required before a coefficient calculation is decisive

1. **Sharp remainder.** As above: without an `o(t^3)` remainder (product-orbifold higher-order approximate metric), `a+b` is not yet an isolable quantity. This is the principal outstanding analysis.

2. **Logarithms.** The Ozuch expansion carries logarithmic terms (Remark 2.11: `H_4^4` is typically `\log r`-order; Remark 3.12: `r^k\log^l r\propto r^k`). The first surviving radial response may be `t_i t_j^2\log t` rather than clean `t_i t_j^2`. Whether the leading equal-scale term is pure cubic or cubic×log must be settled; if a log is present, "the `B` matrix" is not the right object and `a+b` must be replaced by a coefficient attached to `t^3\log t`.

3. **The indefinite shape mode `g_1-g_2`.** It satisfies `P(g_1-g_2)=-\Lambda(g_1-g_2)`. It is `A`-even, `J`-even, and — importantly — also `L`-even (since `L^*g_1=g_1`, `L^*g_2=g_2`), so it survives all three symmetries. It is not a kernel element and does not add an obstruction equation, but it makes the operator on the invariant complement indefinite. The inverse estimate needed for the reduction therefore cannot rest on positivity; uniform invertibility with control of the neck small-eigenvalues and the `-\Lambda` direction is required, and the shape-mode-mediated even response feeds back into the effective `a,b`. This coupling means the "finite-dimensional" reduction is entangled with the indefinite inverse problem.

4. **Scalar kernel modes `u_i g_j` at cubic order.** Step 77 established the full `L^2` kernel of `P` contains four non-TT scalar modes (superseding the zero-kernel statement of Step 76), producing `\nu_l` obstructions; Step 78's `A`-parity removes them and Step 77's Bianchi-coordinate correction cancels the raw `-\pi^2/18` quadratic pairing. For the present purpose these cancellations must be verified to hold at the cubic order where `a,b` live, not only at leading quadratic order, and inside the actual Bianchi/DeTurck slice rather than imposed afterward.

5. **Global equivariant gluing and gauge.** The all-order `J`-elimination and the `L`-orbit relation require the full construction — approximate metric, cutoff radii, DeTurck reference, Lyapunov–Schmidt splitting, mode normalizations — to be simultaneously invariant under the finite group generated by `A`, `J`, `L`, `σ`. Since `L` swaps the two EH orientations, this equivariance mixes positive and negative bubbles; realizing one invariant approximate metric with compatibly transported obstruction bases across chirality is asserted but not constructed. Finite-group averaging makes the linear choices invariant, but the nonlinear gluing across opposite orientations at the shared neck geometry needs to be exhibited.

6. **Inter-node interaction map.** The coefficient `b` is a projected `t_i t_j^2` interaction, not a point value: it is the sliced multipole-to-curvature map `\mathcal C_{ij}` of Step 77, built from the full product resolvent with additive spectral denominators `1/(\lambda_1+\lambda_2+\kappa)`, with singular subtraction only at the source. It is not the product of two single-factor `S^2` Green functions and not the local `\mu` coefficient. Computing `a,b` requires this object explicitly.

7. **Existence beyond equation-counting.** A balanced `2\times2` system carries no existence content by itself. Even with `a+b=0` and a next-order equation, a small positive solution `(t_1,t_2)` requires a transversality/degree or implicit-function argument together with the uniform inverse estimate and nonlinear remainder control (weighted Schauder/Hölder and contraction). This remains entirely open.

8. **Relation to the top goal.** Even a complete positive outcome here would furnish one Einstein metric on one smooth 4-manifold (the `#_3(S^2\times S^2)` "opposite" `k=2` filling of the Step 77 table). It would not address the sign-unrestricted, all-dimensional pinching-to-Einstein statement of Yau‑26, nor even settle the mixed-row family. The value of the calculation is that it tests whether a tight positive near-Einstein orbifold degeneration is completed by an exact Einstein metric or meets a robust even radial obstruction, reducing that question to one refined scalar with explicit power/log accounting.