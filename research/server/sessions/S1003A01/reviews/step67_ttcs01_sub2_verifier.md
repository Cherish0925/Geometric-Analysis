# TTCS Independent Branch Record

```json
{
  "step_id": 67,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step65_homogeneous_torsion_zero_classification_and_surface_transport.md",
    "Sessions/S1003A01/workspace/notes/step66_order6_obstruction.md",
    "Sessions/S1003A02/workspace/notes/step80_Q4_universal_functional_and_lambda_quadratic.md",
    "Sessions/S1003A02/workspace/scripts/step80_reconstruct.py",
    "Sessions/S1003A01/workspace/scripts/step67_verify_A02_reconstruction.py",
    "Sessions/S1003A01/workspace/scripts/step67_convert_darboux_to_normal.py",
    "Sessions/S1003A01/workspace/data/step67/verify_A02_step80_reconstructions.json",
    "Sessions/S1003A01/workspace/data/step67/normal_coordinate_crosscheck.json",
    "Sessions/S1003A02/workspace/data/step80/recon_F012_gen5_lam-5.json",
    "Sessions/S1003A02/workspace/data/step80/recon_lsA_jet0_lam-1.json"
  ]
}
```

## Task

Independently assess the mathematical significance and correctness of the Step-67 finite-jet result for the closed negative-scalar Goldberg programme. Read the Step-65 leading-zero theorem, the superseded Step-66 note, A02's corrected Step-80 note/reconstruction method, and A01's independent Step-67 verification outputs and coordinate-conversion script. Determine precisely what is established by the explicit H2..H8 jets and two-gauge residuals, what is not (formal all-orders/analytic germ/global closed example), whether the normal-coordinate pullback cross-check is mathematically valid including the geodesic exponential-map recursion, and what the highest-value next computation or invariant derivation is. Pay special attention to the order dictionary (E2/E4/E6 versus Taylor coefficients of the scalar compatibility), scaling parameters, positive-index nondegenerate zeros, and whether attempting degree 8 is scientifically justified. Give a direct technical memo, not process advice.

## Output

# Memo: Step-67 finite-jet result at nondegenerate torsion zeros (Goldberg programme, s < 0)

## 0. Summary

**What the jets prove.** The H2…H8 jets show a finite-dimensional fact. In Darboux gauge there are real almost-Kähler metric jets, through Taylor degree 8, whose Einstein deviation vanishes through Taylor degree 6. Their torsion vanishes at the origin with nondegenerate differential of index +1. This holds at λ/tn² = 0 and at λ/tn² = −5.

**How robust it is.** Solvability at this order reduces exactly to one real quadratic equation with a positive-definite Hessian. Its discriminant Φ₆ is strictly below zero at the three jets, and the linearization is surjective at the constructed point. The result therefore survives perturbation, and it can be converted into an exact certificate.

**What it does not prove.** It says nothing beyond Ricci degree 6:
- it gives no formal power series;
- it gives no convergent germ;
- it gives no closed manifold.

**What it refutes.** It does refute every order-≤6 local argument for "no nondegenerate torsion zeros". That includes the conditional theorem of Step 66 and Conjecture 79.C at this order.

**Gauge cross-check.** The A01 two-gauge cross-check is mathematically valid as an independent evaluation of a diffeomorphic pullback. However, its coordinates are not geodesic normal coordinates: the exponential-map recursion has the wrong velocity factor (§3).

## 1. Order dictionary and what the jets contain

**Unknowns and equations.** The metric is g = e^H, with H symmetric and anticommuting with J₀, and ω = Ω₀ constant. With this parametrization, ω-compatibility and dω = 0 are identities. The only equations are E = Ric(g) − λg = 0. E_k denotes the degree-k Taylor coefficient of E.

**Which H_d enter E_k.** Ricci has two derivatives, so E_k involves H up to degree k+2. Quadratic terms H_aH_b enter at Ricci degree a+b−2. Hence:
- E₀…E₅ are exactly linear in u = (H₄,…,H₇) once H₂ is fixed and H₃ = 0.
- The first nonlinearity in u is H₄H₄, at E₆.
- H₈ enters E₆ only through the flat operator L₆. H₂H₈ first appears at degree 8.

So "order 6" in A02's usage means Ricci degree 6, which is jet degree 8. A01's "D = 8" denotes the same level.

**Cokernel count at E₆.** The flat cokernel has dimension 259 = 224 + 35.
- 224 = 4·C(8,3) is the degree-5 part of the contracted Bianchi identity δ_gE + ½d tr_gE = 0. This holds for any metric and any constant λ, so these rows are identically satisfied. That explains why the Gram reduction drops them.
- 35 = C(7,3) is the number of degree-4 coefficients of a scalar function on ℝ⁴.

**The scalar compatibility pattern.** The same count C(k+1,3) gives:
- 1 condition at Ricci degree 2, which is the cone (76.Z);
- 10 conditions at Ricci degree 4, which are the Step-64/65 "ten quadrics" (jet level 6);
- 35 conditions at Ricci degree 6.

So the excess at Ricci degree k is the set of degree-(k−2) Taylor coefficients of one scalar compatibility function Ψ_sc.

**Heuristic source of that scalar.** A count is consistent with this. There are 6 metric unknowns, minus 1 Hamiltonian (symplectic) gauge function, giving 5. Against this stand 10 Einstein equations minus 4 Bianchi identities, giving 6. This is a heuristic count, not a verified symbol computation.

**Link to Step 65.** Step 65 §4 already identified the ten Ricci-degree-4 conditions, at degenerate zeros, as the ten coefficients of the scalar identity (65.2). The fit gave principal-angle cosines of 1, at λ = −1 and λ = 0. The natural reading at a nondegenerate zero is:
- the cone is the degree-0 coefficient of the (65.1)-type scalar identity;
- the ten degree-2 coefficients are linearly solvable (D = 6 converged);
- of the 35 degree-4 coefficients, exactly one combination survives the elimination.

This identification is a testable prediction (§6), not yet a proved statement.

**The positive-index fact.** The torsion vanishes automatically at 0, because ∂g(0) = 0. Its differential is fixed by H₂. Both evaluators reproduce `det_formula_9c4+|detB|^2` = detD to 10⁻¹⁶. Because 9|c|⁴ + |det B|² ≥ 0, every nondegenerate zero on the cone has index +1. The jets realize this case.

## 2. Why order-6 solvability is exact algebra, and how robust the numbers are

**Structure of the reduced map.** Inside the affine solution space u = u₀ + Ny of E₀…E₅, the 35 excess rows form

  Ψ(y) = c + Jy + ½ yᵀH y,

and this form is exact, not a truncation: it is linear in y except for H₄H₄. The `construct` routine splits y = Pz + Kw, where P is the joint range of the 35 quadratic forms. Then:
- H(Kw, ·) = 0 exactly.
- J K has rank 34, so 34 rows are solved linearly in w.
- The remaining row π satisfies πᵀJK = 0. Its equation is φ(z) = c_π + j·z + ½ zᵀH_π z, which does not involve w.

**The solvability statement.** With H_π positive definite, a real solution exists if and only if Φ₆ = c_π − ½ jᵀH_π⁻¹ j ≤ 0. This is a statement about real quadrics, not a numerical artifact.

**Margins at the three jets.**

| jet | Φ₆ | min eig H_π |
|---|---|---|
| gen2, λ=0 | −0.165 | 0.068 |
| gen2, λ=−5 | −0.237 | 0.0054 |
| gen5, λ=−5 | −0.416 | 0.0047 |

Recomputed φ(z) is about 10⁻¹⁶ in the A01 file. At the root z = z* + t v, the gradient of φ is t·h·v ≠ 0; for gen5 it is about 0.06. With rank JK = 34, DΨ has full rank 35 at y. A Newton–Kantorovich estimate gives an exact root near the floating root once two numbers are certified in ball arithmetic: the observed ‖Ψ‖ ≈ 2×10⁻⁹ and a bound on ‖H‖.

**Unreduced residuals in A02's evaluator.**

| jet | max E₀–E₅ | E₆ after H₈ | E₆ before H₈ |
|---|---|---|---|
| gen2, λ=0 | ≤ 5×10⁻¹¹ | 6.2×10⁻⁸ | — |
| gen2, λ=−5 | ≤ 4×10⁻¹⁰ | 1.2×10⁻⁷ | 3.4×10⁷ |
| gen5, λ=−5 | ≤ 1.2×10⁻¹⁰ | 7.7×10⁻⁹ | 2×10⁶ |

Relative to the coefficient sizes, these residuals are at roundoff level. The positive control behaves as the reduction predicts: the irreducible residual equals Φ₆ = 0.842, and E₆ stays at 4.64.

**Numerical points that matter for any continuation.**

1. *H₈ is inflated by the least-squares solver.* H₈ is obtained with `torch.linalg.lstsq`; the CUDA driver assumes full rank. But L₆ is rank-deficient: 840 rows, 259-dimensional cokernel. The H₈ norms jump relative to H₄ and H₆:

   | jet | ‖H₄‖ | ‖H₆‖ | ‖H₈‖ |
   |---|---|---|---|
   | gen2, λ=0 | ≈ 2×10³ | 7.5×10² | 5×10⁶ |
   | gen2, λ=−5 | — | — | 10⁷ |
   | control | — | — | 3.5×10¹⁴ |

   This is the signature of near-null directions absorbing residual, not of genuine jet growth. Any order-8 computation must use the minimum-norm solution on the numerical range of L₆ (gelsd or truncated pinv). It must also parametrize null(L₆) explicitly, otherwise E₈ inherits spurious 10⁷–10¹⁴ data through H₂H₈.

2. *The jets are not exactly even.* H₅ and H₇ are 10⁻⁸–10⁻⁶, not 0, and E₃ and E₅ are about 10⁻¹¹, not 0. In the even branch parity decouples exactly. An exact certificate should set the odd jets to zero.

3. *Coefficient sizes carry no convergence information.* The free data at each order are non-unique, and the weighted rescaling x → μx changes H_k by μ^k.

## 3. The normal-coordinate cross-check

**The recursion is not the geodesic equation.** `exp_map_coeffs` iterates

  m(m−1)X_m = [−Γ(X(y))(y, y)]_m.

Write the geodesic as x(t) = X(ty). The geodesic equation, after Euler's identity, is

  m(m−1)X_m = [−Γ(X(y))(DX(y)y, DX(y)y)]_m,  with DX(y)y = y + Σ m X_m(y).

The two agree through X₃ = −Γ₁(y)(y,y)/6, because Γ(0) = 0 and X₂ = 0. They first differ in X₅, through the term Γ₁·y·3X₃. The pulled-back metric therefore fails the Gauss lemma g_ij(y)yʲ = y_i from degree 4 on.

The reported check `normal_metric_linear_norm = 0` holds for any X = y + O(y³). It does not test normality.

**The pullback is still an exact isometric representation.** X is a polynomial of degree 8 with X = y + O(y³), so it is a genuine diffeomorphism germ. With X₉ = 0, the pullback J^T g(X) J and J^T Ω J is exact through degree 8, and Ricci degree 6 needs nothing more. Pullback commutes with Ric − λg, and ω stays closed and compatible. The cross-check is therefore a valid independent evaluation by A01's gauge-free (g, ω) system:
- E1 is the algebraic compatibility;
- E2 is dω = 0;
- E3 is Einstein.

It tests A02's Ricci and torsion code on non-Darboux input. It does not test A02's reduction logic, because it evaluates the same jet.

**Consistency checks that pass.**

- *Torsion determinant.* Mvec_det equals 16 × detD in each case:

  | jet | Mvec_det | 16 × detD |
  |---|---|---|
  | gen2 | 0.26590 | 16 × 0.016619 |
  | gen5 | 0.37397 | 16 × 0.023373 |
  | control | 0.80302 | 16 × 0.050189 |

  This matches Nphi = 2·Mmat, i.e. det scales by 2⁴. The torsion zero and its index are gauge-consistent.

- *Einstein residuals.* E3_d6 is about 10⁻⁸–10⁻⁷ for the three Φ₆ < 0 jets. For the control it is 4.78.

- *E1_d8 is roundoff.* The control's E1_d8 = 0.178 is exactly compatible by construction. The value is roundoff on coefficients of size 3.5×10¹⁴ (relative ~10⁻¹⁵), which confirms item 1 of §2.

**A sharper check left open.** E₀…E₅ vanish, X = y + O(y³), and DX = I + O(y²). Hence

  Φ*E = E₆(y) + O(y⁸).

The degree-6 Ricci coefficient must coincide componentwise in the two gauges. The control norms differ: 4.640 versus 4.778, a ratio of 1.030. This must be a normalization difference in how the two codes vectorize Ricci coefficients, for example off-diagonal multiplicity or monomial weights. Comparing the two E₆ tensors componentwise, after matching normalizations, turns the cross-check into an exact identity test. As it stands, the Φ₆ < 0 cases agree only to "both at roundoff".

## 4. What is established and what is not

**Established (floating point, cross-validated, certifiable):**
- Prop 80.R. Real AK jets through degree 8 satisfy Ric − λg = O(|x|⁷) and have a nondegenerate index +1 torsion zero, at λ/tn² ∈ {0, −5}.
- Order ≤ 6 cannot exclude nondegenerate torsion zeros for λ ≤ 0.
- The Step-66 premise "Φ₆ > 0 at every strict cone point" is refuted by gen2 and gen5.
- Its conditional theorem, and the corollary "all zeros are degenerate", are withdrawn at this order.
- Φ₆ ≤ 0 is a necessary condition at order 6 in the even branch, H₃ = 0.

**Not established:**

1. *The order-6 region is mapped only for H₃ = 0.* H₃ is free data constrained only by E₁, which is linear in H₃ given H₂. H₃H₃ enters E₄ and H₃H₅ enters E₆. A jet with Φ₆ > 0 in the even branch, such as the lsA control, may extend once H₃ ≠ 0. "{Φ₆ > 0} is obstructed" is a statement about even jets only.

2. *No all-orders formal series.* Order 7 is automatic only for exactly even jets. Order 8 (H through degree 10) carries 84 = C(9,3) excess conditions.

3. *No convergent germ.* The system is overdetermined: Einstein metric plus a self-dual harmonic 2-form of constant length √2, which is one extra scalar equation. Analyticity of Einstein metrics does not turn a formal solution into a convergent one. Artin-type approximation does not apply to PDE systems.

4. *No closed example, and no decision on Goldberg for s < 0.*

**Step-66 text that is wrong as written.**
- "Isolated degenerate zeros have ill-defined Brouwer index." The local degree on a small sphere is defined for any isolated zero; only the det formula is unavailable.
- "All zeros degenerate with GH-type structure" conflates two cases:
  - first-order rank-deficient zeros on the cone, with c = 0 and det B = 0 (e.g. Step 65's f₁ = κ z̄₂ e₁ along surfaces), which (65.5) does not cover;
  - zeros of order m ≥ 2, for which (65.5) gives κ z̄₂^m e₁.

## 5. Significance for the closed Goldberg programme with s < 0

**Zeros are forced.** Using the zero count 5χ+6τ from the Step-80 note, and c₁² = 2χ+3τ:

  5χ + 6τ = 2c₁² + c₂.

For an Einstein metric, Hitchin–Thorpe gives τ ≥ −2χ/3, so 5χ + 6τ ≥ χ > 0 for nonflat metrics. A strictly AKE closed manifold therefore has a nonempty torsion zero set of positive total index.

**No local contradiction through order 6.** Nondegenerate zeros contribute exactly +1 each. The Step-80 jets show that such a zero is locally consistent through Ricci degree 6 with λ < 0. So index counting plus order-6 local analysis produce no contradiction: a configuration of 5χ+6τ nondegenerate index +1 zeros is locally admissible at this order.

**Where the closed problem now stands.** Any proof must use one of:
- higher-order local information (order ≥ 8, or the odd branch);
- global integral information, e.g. the integrated form of (65.1), whose −(3s/2)q term has a definite sign for s < 0;
- the surface-transport problem of Step 65 §6 for rank-deficient zero sets.

The order-6 result moves the discriminating content out of the order-≤6 nondegenerate-zero analysis.

## 6. The two computations with the highest information content

**(a) Identify the excess and the functional ℓ invariantly.** This is cheap and has high leverage.

The method is the Step-65 §4 method one degree up:
1. Compute the degree-4 Taylor coefficients of the residual of the scalar identity (65.1), or of the scalar compatibility it represents, on Darboux jets at a nondegenerate zero.
2. Compare their span with the 35 excess rows C₆ by principal angles.
3. Then decompose the universal functional ℓ under SO(4) and U(2). It is jet-independent, with |cos| = 1 to 10⁻¹⁵ across four jets.

The natural candidate is an invariant trace of the degree-4 coefficient, such as Δ² of the scalar at 0. At degenerate zeros, the spatial trace of the ten quadrics was the decisive combination (65.6).

What success would give:
- a closed formula Φ₆ = F₀ + F₁λ + F₂λ² in U(2)-invariants of (c, S, A), with weights 8, 6, 4;
- the exact semialgebraic region, replacing the 8+7-jet sample;
- an identification of the order-6 condition with a pointwise Taylor coefficient of a global geometric identity, which is the form that can be integrated on a closed manifold.

**(b) Order 8 as a rank computation, not a full solve.**

*Mechanism for the expectation.* At order 6, the quadratic coupling was confined to H₄H₄ on a 12-dimensional block. At Ricci degree 8, in the even branch, the excess rows acquire the bilinear term H₄·H₆ (and H₂H₄H₄-type cubics). The order-6 solution has H₄ ≠ 0 and large. So the linearization in the free H₆ directions is J₈ + B(H₄, ·), which generically has more rank than the flat coupling. My expectation is surjectivity onto the 84 rows; this is a mechanism-based expectation, not a computed fact.

*The computation that decides it.* Compute the rank, on the 84 Ricci-degree-8 excess rows, of the Jacobian at a constructed order-6 solution. The variables must include:
- the tangent space of the order-6 solution variety (y-directions preserving Ψ = 0);
- the null(L₆) directions of H₈, computed with the minimum-norm fix of §2;
- H₁₀ through the flat L₈.

*How to read the outcome.*
- Rank 84 means order 8 is solvable near that point by the implicit function theorem. That would indicate the formal route does not close at nondegenerate zeros.
- A rank deficit would give a new surviving scalar. Its sign on the open region {Φ₆ < 0} is then the next question.

*What either outcome leaves open.*
- Order 8 is scientifically justified because both outcomes change the assessment of the local route.
- Only the rank deficit refines the semialgebraic region; neither outcome produces a germ.
- If a deficit appears, the odd branch H₃ ≠ 0 must be added before calling any region obstructed.

**Route to a genuine germ.** Formal consistency does not give an analytic germ. A route that could is a reduced-symmetry ansatz with an isolated fixed point, for example T²-equivariant almost-Kähler metrics in action-angle Darboux coordinates; Step 63 excludes full SU(2). The quick prerequisite is algebraic. Determine which components of f = cz + (S+A)z̄ are equivariant under the T² weights on ℂ². Then check whether the equivariant part can satisfy the cone with detD > 0. If not, no torus-symmetric germ has a nondegenerate zero, and the germ question must be answered by a non-symmetric existence argument.