# Step 64: exceptional points of torsion-zero surfaces, the second-order zero identity, and SU(2) diagonalization

Agent2, Execute. Inputs: the Step-63 compact clean zero-surface theorem, the Step-62 cone and dictionary, and Spirit #75.
Scripts:
- `scripts/step64_exceptional_winding.py`: linear analysis at a second-order zero (D=5);
- `step64_level6.py`: the level-6 quadric at a second-order zero (D=6);
- `step64_intrinsic_quadric.py`: fits the quadric in intrinsic coordinates (δ,Q);
- `step64_debug.py`: λ=0 D=3 check.

Data: `data/step64/winding_lam-1.0_s0.json`, plus the level-6 outputs if present.

Labels: [P] proved by hand; [N] numerical; [O] open.

## 0. Spirit #75: the SU(2) momentum diagonalization [P, checked]

Take the normal-geodesic gauge g=dt²+H_ij(t)σ_iσ_j, with dσ_i=2σ_j∧σ_k. At a regular time, diagonalize H by a constant SO(3) automorphism, H=diag(a_i²).

The mixed Einstein (Codazzi) equations are (n_k−n_j)K_jk=0, where K_jk=H'_jk/(2a_ja_k) and n_i=−2a_i/(a_ja_k). This gives n_k−n_j=−2(a_k²−a_j²)/(a_1a_2a_3), so (a_j²−a_k²)H'_jk=0. Equivalently [H,H']=0.

Simultaneously diagonalize H and H' by one constant SO(3) element. Within a repeated eigenspace of H, diagonalize H'. The spatial Einstein system is a smooth second-order ODE that preserves the diagonal subspace, because the Milnor-frame Ricci tensor and the velocity terms are diagonal. By uniqueness, H stays diagonal in this single fixed frame, so eigenvalue crossings cause no difficulty. Invariant self-dual forms in a diagonal metric are exactly Σx_iω_i.

Consequence: Step 63's regular-nut rigidity theorem covers every fully SU(2)-invariant Einstein almost-Kähler pair with a regular nut. Such a pair is the complex-hyperbolic Kähler germ. A non-diagonal recurrence would add no freedom. Still open: an SU(2)-invariant metric with a noninvariant form, smaller symmetry groups, and unrestricted germs.

## 1. Admissible second torsion jets at a second-order zero [P+N]

Let T(p)=0 and DT(p)=0. Then W⁺(p) has Kähler type, and the torsion a (∇Ω=a⊗φ−Ja⊗ψ) has quadratic Taylor part f₂. In complex coordinates z (source J) and target structure i·a=Ja (numerically Mj=JM), the linear structure Df₂(x)∈L_x at every x forces

  f₂(z)=δ(z̄) z + Q(z̄,z̄),

where δ is an antilinear functional (4 real dimensions) and Q∈S²⊗C² (12 real dimensions). The total is 16. [N]: at D=5 the admissible image has dimension 16. This holds for λ=−1 and is λ-independent at level 3. Level 5 imposes no further linear condition (rank C5=0).

Along x: c(x)=δ(x̄), B(x)=x⊗δ+2Q(x̄,·), and A₁₂(x)=(x₁δ₂−x₂δ₁)/2+P·x̄, where P_a=Q¹_{a2}−Q²_{a1} is the equivariant ε-contraction. The first-order dictionary holds at linear order in x near p, because a=O(x²), b=O(x) in a radially parallel frame, and R(p)ψ₀=0. It gives ∇_xη=−2c(x) and ∇_xV=dict(A(x)).

## 2. Theorem 64.A (second-order zero identity) [P; subsumed by Step 65's exact scalar equation]

At a point with ∇Ω=∇²Ω=0 on an Einstein AK four-manifold (any λ),

  |∇³Ω|²=4Σ_i trV_i²−24Σ_i|η_i|²,  with ∇_iW⁺=[[0,η_iᵀ],[η_i,V_i]].

This confirms the Step-62 generator's claim.

Proof sketch. Apply Δ² to q=4⟨W⁺u,u⟩−2s/3.
- LHS: Δ²|T|²=2|ΔT|²+4|∇²T|², with ΔT=−2(∇W⁺)Ω, so |ΔT|²=8Σ|η_i|².
- RHS, first term: ΔW⁺(p)=0 for Kähler-type W⁺ by Derdziński. Hence ⟨Δ²W⁺u,u⟩=−12Σ|∇_iW⁺u|²+4Σtr(∇_iW⁺)²=4ΣtrV_i²−4Σ|η_i|².
- RHS, cross terms: 4Σ⟨∇_iW⁺u,∇_iΔu+Δ∇_iu⟩=−16Σ|η_i|². This uses Δu=−2W⁺u+(s/3)u, and [Δ,∇_i]u=Σ(∇_kR)(e_k,e_i)u=0 by Einstein/Bianchi.
- RHS, remaining term: ⟨W⁺Δ²u,u⟩=0.
So Δ²q=16ΣtrV²−80Σ|η|². Subtracting 16Σ|η|² gives the identity. The same method reproduces Theorem 62.A.

In the intrinsic coordinates, Σ|η_i|²=8|δ|², ΣtrV_i²=4|δ|²+16|P|², and |∇³Ω|²=64(|δ|²+‖Q‖²). Hence

  **‖Q‖² − |P|² = −(15/4)|δ|²**  (second-order zero cone).

With Q=Q₃⊕Q₁ (S³⊕S¹) and |P|²=(3/2)‖Q₁‖², this reads ‖Q₁‖²=2‖Q₃‖²+(15/2)|δ|².

Step 65 identifies all ten level-6 quadrics as the ten spatial coefficients of one exact leading scalar identity and confirms the same span at lambda=0. Its trace is precisely the displayed 15/4 relation. See `step65_homogeneous_torsion_zero_classification_and_surface_transport.md`.

## 3. Corollary 64.B (exceptional points) [P; exact coefficient check in Step 65]

Let C be a smooth J-complex surface contained in {T=0}, tangent to {z₂=0} at an exceptional point p (DT(p)=0). The three conditions are:
- T|_C=0 to second order: δ₁=0 and Q₁₁=0;
- the cone at points of C: b₂₂=0, i.e. Q²₁₂=0;
- §2: |Q¹₁₂|²+|Q²₂₂|²+(15/4)|δ₂|²=0.

Hence δ=0 and f₂=κ z̄₂² e₁, where κ is the only free entry. The restricted section W₃⁺|_C∝b₁₂(z₁)=δ₂z₁+2Q¹₁₂z̄₁+O(|z₁|²) has vanishing linear part.

So the linear Taylor part of W₃⁺|_C vanishes at every such exceptional point. This establishes first-derivative degeneracy, but it does **not** determine the order of the first nonzero higher term or its winding: for example `z|z|^2` and `zbar|z|^2` have zero linear part and winding +1 and -1. Step 65 withdraws the former winding conclusion and derives the exact surface equation with its unresolved normal-eta source. The leading restriction holds for every lambda.

At the purely linear level, before §2, both signs of the determinant of the linear part were allowed. D=5 numerics gave a determinant range [−0.5,0.5] in `winding_lam-1.0_s0.json`. The nonlinear identity forces that linear part to vanish, but this no longer implies any sign statement for the winding of a higher-order zero.

## 4. Open [O]

The sign of the individual exceptional windings is not yet decided. The exact AAD Bianchi restriction obtained in Step 65 is a Cauchy–Riemann-type equation for `b=W3+|C`, but its right side is a normal derivative of `eta`, not yet a bounded zero-order multiple of `b`. A similarity principle therefore remains unavailable. The sharp next calculation is a coupled tubular expansion for `(b, nabla_N eta, ...)`, retaining the induced line connection and second fundamental form, to determine whether the source is divisible by `b` through exceptional zeros or permits negative winding. The 15/4 coefficient and all ten directional equations are now accounted for by the exact scalar identity.
