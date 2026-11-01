import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Metric
import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Torsion
import Mathlib.Geometry.Manifold.Instances.Real
import Mathlib.LinearAlgebra.Trace

/-!
# Constant metric scaling and Ricci-pinching normalization

This file is a checked interface step, not a formalization or proof of Yau Problem 26.
It uses Mathlib's genuine smooth Riemannian metrics, covariant derivatives, torsion,
metric compatibility, smooth vector fields, and linear trace.  Mathlib v4.33.1 does
not yet construct the Levi--Civita connection or curvature, so those missing data
and their laws are exposed in `GeometryFor`.

The checked normalization also corrects a reciprocal typo in the Step 85 prose:
if `h = α g`, then interval coefficients divide by `α`, so the centering scale is
`α = (c+C)/2` in the positive branch and `α = -(c+C)/2` in the negative branch.
-/

noncomputable section

open Bundle Bornology
open scoped Manifold ContDiff Topology

namespace Yau26MetricScaling

universe u

set_option synthInstance.maxHeartbeats 200000
set_option maxHeartbeats 1000000
set_option linter.style.haveILetI false

abbrev ModelSpace (n : ℕ) := EuclideanSpace ℝ (Fin n)

variable {n : ℕ} {M : Type u}
variable [TopologicalSpace M] [ChartedSpace (ModelSpace n) M]
variable [IsManifold (𝓡 n) ∞ M]

abbrev SmoothMetric (n : ℕ) (M : Type u) [TopologicalSpace M]
    [ChartedSpace (ModelSpace n) M] [IsManifold (𝓡 n) ∞ M] :=
  Bundle.ContMDiffRiemannianMetric (𝓡 n) ∞ (ModelSpace n)
    (TangentSpace (𝓡 n) : M → Type _)

abbrev TangentConnection (n : ℕ) (M : Type u) [TopologicalSpace M]
    [ChartedSpace (ModelSpace n) M] [IsManifold (𝓡 n) ∞ M] :=
  CovariantDerivative (𝓡 n) (ModelSpace n) (TangentSpace (𝓡 n) : M → Type _)

abbrev SmoothVectorField (n : ℕ) (M : Type u) [TopologicalSpace M]
    [ChartedSpace (ModelSpace n) M] [IsManifold (𝓡 n) ∞ M] :=
  ContMDiffSection (𝓡 n) (ModelSpace n) ∞
    (TangentSpace (𝓡 n) : M → Type _)

/-- Explicit smoothness-at-a-point predicate, avoiding model-inference ambiguity for `T% X`. -/
def IsSmoothVectorFieldAt (X : (x : M) → TangentSpace (𝓡 n) x) (x : M) : Prop :=
  MDifferentiableAt (𝓡 n) ((𝓡 n).prod 𝓘(ℝ, ModelSpace n)) (T% X) x

abbrev RiemannTensor (n : ℕ) (M : Type u) [TopologicalSpace M]
    [ChartedSpace (ModelSpace n) M] [IsManifold (𝓡 n) ∞ M] :=
  (x : M) → TangentSpace (𝓡 n) x →L[ℝ]
    TangentSpace (𝓡 n) x →L[ℝ]
      TangentSpace (𝓡 n) x →L[ℝ] TangentSpace (𝓡 n) x

/-- Genuine constant rescaling of a smooth Riemannian metric by `α > 0`. -/
def scaleMetric (g : SmoothMetric n M) (α : ℝ) (hα : 0 < α) : SmoothMetric n M where
  inner x := α • g.inner x
  symm x v w := by simp [g.symm x v w]
  pos x v hv := by
    simpa using mul_pos hα (g.pos x v hv)
  isVonNBounded x := by
    let β : ℝ := Real.sqrt α
    have hβ : 0 < β := Real.sqrt_pos.2 hα
    have hβsq : β * β = α := by
      dsimp [β]
      nlinarith [Real.sq_sqrt hα.le]
    apply Bornology.IsVonNBounded.subset _
      ((g.isVonNBounded x).image ((β⁻¹) • (1 : TangentSpace (𝓡 n) x →L[ℝ]
        TangentSpace (𝓡 n) x)))
    intro v hv
    refine ⟨β • v, ?_, ?_⟩
    · change g.inner x (β • v) (β • v) < 1
      rw [map_smul, map_smul]
      change β * (β * g.inner x v v) < 1
      rw [← mul_assoc, hβsq]
      simpa using hv
    · simp [smul_smul, hβ.ne']
  contMDiff := by
    simpa using g.contMDiff.const_smul_section (a := α)

@[simp]
theorem scaleMetric_inner (g : SmoothMetric n M) (α : ℝ) (hα : 0 < α)
    (x : M) (v w : TangentSpace (𝓡 n) x) :
    (scaleMetric g α hα).inner x v w = α * g.inner x v w := by
  rfl

/-- Mathlib's metric-compatibility predicate with a metric supplied as explicit data. -/
def IsMetricCompatibleWith (g : SmoothMetric n M) (cov : TangentConnection n M) : Prop :=
  letI : Bundle.RiemannianBundle (TangentSpace (𝓡 n) : M → Type _) :=
    ⟨g.toRiemannianMetric⟩
  cov.IsMetricCompatible

/-- The pointwise Leibniz formula corresponding to `IsMetricCompatibleWith`. -/
def MetricCompatibilityFormula (g : SmoothMetric n M) (cov : TangentConnection n M) : Prop :=
  ∀ {x : M} {X σ τ : (x : M) → TangentSpace (𝓡 n) x},
    IsSmoothVectorFieldAt X x → IsSmoothVectorFieldAt σ x →
      IsSmoothVectorFieldAt τ x →
      mvfderiv (𝓡 n) (fun y ↦ g.inner y (σ y) (τ y)) x (X x) =
        g.inner x (cov σ x (X x)) (τ x) +
          g.inner x (σ x) (cov τ x (X x))

theorem isMetricCompatibleWith_iff_formula
    (g : SmoothMetric n M) (cov : TangentConnection n M) :
    IsMetricCompatibleWith g cov ↔ MetricCompatibilityFormula g cov := by
  letI : Bundle.RiemannianBundle (TangentSpace (𝓡 n) : M → Type _) :=
    ⟨g.toRiemannianMetric⟩
  change cov.IsMetricCompatible ↔ _
  constructor
  · intro h x X σ τ hX hσ hτ
    have Hx := (CovariantDerivative.isMetricCompatible_iff (cov := cov)).1 h
      (x := x) (X := X) (σ := σ) (τ := τ) hX hσ hτ
    change mvfderiv (𝓡 n) (fun y ↦ g.inner y (σ y) (τ y)) x (X x) =
      g.inner x (cov σ x (X x)) (τ x) +
        g.inner x (σ x) (cov τ x (X x)) at Hx
    exact Hx
  · intro H
    rw [CovariantDerivative.isMetricCompatible_iff]
    intro x X σ τ hX hσ hτ
    have Hx := H (x := x) (X := X) (σ := σ) (τ := τ) hX hσ hτ
    change mvfderiv (𝓡 n) (fun y ↦ g.inner y (σ y) (τ y)) x (X x) =
      g.inner x (cov σ x (X x)) (τ x) +
        g.inner x (σ x) (cov τ x (X x)) at Hx
    exact Hx

/-- Constant positive rescaling preserves compatibility of the same connection. -/
theorem isMetricCompatibleWith_scaleMetric
    (g : SmoothMetric n M) (cov : TangentConnection n M)
    (α : ℝ) (hα : 0 < α) (hcov : IsMetricCompatibleWith g cov) :
    IsMetricCompatibleWith (scaleMetric g α hα) cov := by
  rw [isMetricCompatibleWith_iff_formula] at hcov ⊢
  intro x X σ τ hX hσ hτ
  have hold := hcov (x := x) (X := X) (σ := σ) (τ := τ) hX hσ hτ
  have hinner : MDifferentiableAt (𝓡 n) 𝓘(ℝ)
      (fun y ↦ g.inner y (σ y) (τ y)) x := by
    letI : Bundle.RiemannianBundle (TangentSpace (𝓡 n) : M → Type _) :=
      ⟨g.toRiemannianMetric⟩
    exact hσ.inner_bundle hτ
  rw [show (fun y ↦ (scaleMetric g α hα).inner y (σ y) (τ y)) =
      fun y ↦ α * g.inner y (σ y) (τ y) by
        funext y
        simp]
  have hderiv :
      mvfderiv (𝓡 n) (fun y ↦ α * g.inner y (σ y) (τ y)) x =
        α • mvfderiv (𝓡 n) (fun y ↦ g.inner y (σ y) (τ y)) x := by
    rw [show (fun y ↦ α * g.inner y (σ y) (τ y)) =
      (fun _ : M ↦ α) * (fun y ↦ g.inner y (σ y) (τ y)) by rfl]
    simpa [Pi.smul_apply, mvfderiv_const] using
      (mvfderiv_smul (I := 𝓡 n) (a := fun _ : M ↦ α)
        mdifferentiableAt_const hinner)
  rw [hderiv]
  simp only [smul_apply, smul_eq_mul]
  simp only [scaleMetric_inner]
  linear_combination α * hold

/-- The connection commutator on vector fields. -/
def curvatureOnFields (cov : TangentConnection n M)
    (X Y Z : (x : M) → TangentSpace (𝓡 n) x) (x : M) : TangentSpace (𝓡 n) x :=
  cov (fun y ↦ cov Z y (Y y)) x (X x)
    - cov (fun y ↦ cov Z y (X y)) x (Y x)
    - cov Z x (VectorField.mlieBracket (𝓡 n) X Y x)

/--
The exact geometry currently missing from Mathlib for a supplied smooth metric.
The connection and its torsion/compatibility predicates are genuine Mathlib objects;
the pointwise Riemann tensor is tied to that connection by `riemann_realizes`.
-/
structure GeometryFor (n : ℕ) (M : Type u) [TopologicalSpace M]
    [ChartedSpace (ModelSpace n) M] [IsManifold (𝓡 n) ∞ M]
    (g : SmoothMetric n M) where
  leviCivita : TangentConnection n M
  connection_smooth : CovariantDerivative.ContMDiffCovariantDerivative leviCivita ∞
  torsion_free : leviCivita.torsion = 0
  metric_compatible : IsMetricCompatibleWith g leviCivita
  riemann : RiemannTensor n M
  riemann_realizes :
    ∀ (X Y Z : SmoothVectorField n M) (x : M),
      riemann x (X x) (Y x) (Z x) =
        curvatureOnFields leviCivita (fun y ↦ X y) (fun y ↦ Y y) (fun y ↦ Z y) x

/-- The endomorphism `z ↦ R(z,v)w` whose trace is `Ric(v,w)`. -/
def curvatureEndomorphism {g : SmoothMetric n M} (G : GeometryFor n M g) (x : M)
    (v w : TangentSpace (𝓡 n) x) :
    TangentSpace (𝓡 n) x →ₗ[ℝ] TangentSpace (𝓡 n) x where
  toFun := fun z ↦ G.riemann x z v w
  map_add' := by simp
  map_smul' := by simp

/-- Basis-independent Ricci contraction `Ric(v,w) = tr(z ↦ R(z,v)w)`. -/
def ricciAt {g : SmoothMetric n M} (G : GeometryFor n M g) (x : M)
    (v w : TangentSpace (𝓡 n) x) : ℝ :=
  LinearMap.trace ℝ (TangentSpace (𝓡 n) x) (curvatureEndomorphism G x v w)

/-- The Ricci `(0,2)` tensor at a point, bundled as an actual bilinear form. -/
def ricciTensor {g : SmoothMetric n M} (G : GeometryFor n M g) (x : M) :
    LinearMap.BilinForm ℝ (TangentSpace (𝓡 n) x) where
  toFun v :=
    { toFun := fun w ↦ ricciAt G x v w
      map_add' := by
        intro w₁ w₂
        unfold ricciAt
        rw [show curvatureEndomorphism G x v (w₁ + w₂) =
          curvatureEndomorphism G x v w₁ + curvatureEndomorphism G x v w₂ by
            ext z
            simp [curvatureEndomorphism]]
        exact map_add _ _ _
      map_smul' := by
        intro a w
        unfold ricciAt
        rw [show curvatureEndomorphism G x v (a • w) =
          a • curvatureEndomorphism G x v w by
            ext z
            simp [curvatureEndomorphism]]
        exact map_smul _ _ _ }
  map_add' := by
    intro v₁ v₂
    apply LinearMap.ext
    intro w
    change ricciAt G x (v₁ + v₂) w = ricciAt G x v₁ w + ricciAt G x v₂ w
    unfold ricciAt
    rw [show curvatureEndomorphism G x (v₁ + v₂) w =
      curvatureEndomorphism G x v₁ w + curvatureEndomorphism G x v₂ w by
        ext z
        simp [curvatureEndomorphism]]
    exact map_add _ _ _
  map_smul' := by
    intro a v
    apply LinearMap.ext
    intro w
    change ricciAt G x (a • v) w = a • ricciAt G x v w
    unfold ricciAt
    rw [show curvatureEndomorphism G x (a • v) w =
      a • curvatureEndomorphism G x v w by
        ext z
        simp [curvatureEndomorphism]]
    exact map_smul _ _ _

/--
The geometry of `α g` obtained by reusing the connection and `(1,3)` curvature of `g`.
Metric compatibility is proved above; all other structure fields are literally unchanged.
-/
def scaleGeometry {g : SmoothMetric n M} (G : GeometryFor n M g)
    (α : ℝ) (hα : 0 < α) : GeometryFor n M (scaleMetric g α hα) where
  leviCivita := G.leviCivita
  connection_smooth := G.connection_smooth
  torsion_free := G.torsion_free
  metric_compatible := isMetricCompatibleWith_scaleMetric g G.leviCivita α hα G.metric_compatible
  riemann := G.riemann
  riemann_realizes := G.riemann_realizes

/-- Constant positive metric scaling leaves Ricci equal as a bundled `(0,2)` tensor. -/
@[simp] theorem ricciTensor_scale_const {g : SmoothMetric n M} (G : GeometryFor n M g)
    (α : ℝ) (hα : 0 < α) (x : M) :
    ricciTensor (scaleGeometry G α hα) x = ricciTensor G x := by
  rfl

/-- Constant positive scaling leaves the complete pointwise Ricci tensor field unchanged. -/
@[simp] theorem ricciTensorField_scale_const {g : SmoothMetric n M} (G : GeometryFor n M g)
    (α : ℝ) (hα : 0 < α) :
    (fun x ↦ ricciTensor (scaleGeometry G α hα) x) = fun x ↦ ricciTensor G x := by
  rfl

/-- Constant positive metric scaling leaves the Ricci `(0,2)` tensor unchanged. -/
@[simp] theorem ricci_scale_const {g : SmoothMetric n M} (G : GeometryFor n M g)
    (α : ℝ) (hα : 0 < α) (x : M) (v w : TangentSpace (𝓡 n) x) :
    ricciAt (scaleGeometry G α hα) x v w = ricciAt G x v w := by
  rfl

/-- Order on two forms in the diagonal, quadratic-form sense. -/
def QuadraticLE {V : Type*} (A B : V → V → ℝ) : Prop :=
  ∀ v, A v v ≤ B v v

/-- The literal pointwise pinching condition `c g ≤ Ric_g ≤ C g`. -/
def RicciPinched {g : SmoothMetric n M} (G : GeometryFor n M g) (c C : ℝ) : Prop :=
  ∀ x,
    QuadraticLE
      (fun v w ↦ c * g.inner x v w)
      (fun v w ↦ ricciTensor G x v w)
    ∧ QuadraticLE
      (fun v w ↦ ricciTensor G x v w)
      (fun v w ↦ C * g.inner x v w)

/-- Pair-of-order-inequalities form of `‖Ric - σ g‖op ≤ δ`. -/
def NormalizedPinched {g : SmoothMetric n M} (G : GeometryFor n M g)
    (σ δ : ℝ) : Prop :=
  RicciPinched G (σ - δ) (σ + δ)

/--
General transport lemma.  If `a α = c` and `b α = C`, then pinching by
`[c,C]` relative to `g` is exactly pinching by `[a,b]` relative to `α g`.
-/
theorem ricciPinched_scale_iff_of_endpoint_identities
    {g : SmoothMetric n M} (G : GeometryFor n M g)
    (α : ℝ) (hα : 0 < α) (c C a b : ℝ)
    (ha : a * α = c) (hb : b * α = C) :
    RicciPinched G c C ↔ RicciPinched (scaleGeometry G α hα) a b := by
  constructor
  · intro h x
    constructor
    · intro v
      calc
        a * (scaleMetric g α hα).inner x v v = c * g.inner x v v := by
          rw [scaleMetric_inner, ← mul_assoc, ha]
        _ ≤ ricciTensor G x v v := (h x).1 v
        _ = ricciTensor (scaleGeometry G α hα) x v v := by simp
    · intro v
      calc
        ricciTensor (scaleGeometry G α hα) x v v = ricciTensor G x v v := by simp
        _ ≤ C * g.inner x v v := (h x).2 v
        _ = b * (scaleMetric g α hα).inner x v v := by
          rw [scaleMetric_inner, ← mul_assoc, hb]
  · intro h x
    constructor
    · intro v
      calc
        c * g.inner x v v = a * (scaleMetric g α hα).inner x v v := by
          rw [scaleMetric_inner, ← mul_assoc, ha]
        _ ≤ ricciTensor (scaleGeometry G α hα) x v v := (h x).1 v
        _ = ricciTensor G x v v := by simp
    · intro v
      calc
        ricciTensor G x v v = ricciTensor (scaleGeometry G α hα) x v v := by simp
        _ ≤ b * (scaleMetric g α hα).inner x v v := (h x).2 v
        _ = C * g.inner x v v := by
          rw [scaleMetric_inner, ← mul_assoc, hb]

/-- Correct positive-interval scale: the arithmetic midpoint, not its reciprocal. -/
def positiveScale (c C : ℝ) : ℝ := (c + C) / 2

def positiveDelta (c C : ℝ) : ℝ := (C - c) / (C + c)

theorem positiveScale_pos {c C : ℝ} (hc : 0 < c) (hcC : c < C) :
    0 < positiveScale c C := by
  unfold positiveScale
  linarith

theorem positiveDelta_mem_Ioo {c C : ℝ} (hc : 0 < c) (hcC : c < C) :
    positiveDelta c C ∈ Set.Ioo (0 : ℝ) 1 := by
  have hden : 0 < C + c := by linarith
  constructor
  · exact div_pos (sub_pos.2 hcC) hden
  · exact (div_lt_one hden).2 (by linarith)

theorem positive_lower_endpoint {c C : ℝ} (hc : 0 < c) (hcC : c < C) :
    (1 - positiveDelta c C) * positiveScale c C = c := by
  have hden : C + c ≠ 0 := ne_of_gt (by linarith)
  unfold positiveDelta positiveScale
  field_simp [hden]
  ring

theorem positive_upper_endpoint {c C : ℝ} (hc : 0 < c) (hcC : c < C) :
    (1 + positiveDelta c C) * positiveScale c C = C := by
  have hden : C + c ≠ 0 := ne_of_gt (by linarith)
  unfold positiveDelta positiveScale
  field_simp [hden]
  ring

/-- Centering the rescaled endpoints at `1` forces the midpoint scale. -/
theorem positive_centering_scale_unique {c C α δ : ℝ}
    (hlower : (1 - δ) * α = c) (hupper : (1 + δ) * α = C) :
    α = positiveScale c C := by
  unfold positiveScale
  nlinarith

/--
A strict positive interval is equivalent, after scaling by `(c+C)/2`, to the
normalized pair `(1-δ) h ≤ Ric_h ≤ (1+δ) h`, with `0 < δ < 1`.
-/
theorem positive_interval_normalization
    {g : SmoothMetric n M} (G : GeometryFor n M g)
    {c C : ℝ} (hc : 0 < c) (hcC : c < C) :
    RicciPinched G c C ↔
      NormalizedPinched
        (scaleGeometry G (positiveScale c C) (positiveScale_pos hc hcC))
        1 (positiveDelta c C) := by
  unfold NormalizedPinched
  apply ricciPinched_scale_iff_of_endpoint_identities
  · exact positive_lower_endpoint hc hcC
  · exact positive_upper_endpoint hc hcC

/-- Positive normalization together with the certified strict range `0 < δ < 1`. -/
theorem positive_interval_normalization_package
    {g : SmoothMetric n M} (G : GeometryFor n M g)
    {c C : ℝ} (hc : 0 < c) (hcC : c < C) :
    positiveDelta c C ∈ Set.Ioo (0 : ℝ) 1 ∧
      (RicciPinched G c C ↔
        NormalizedPinched
          (scaleGeometry G (positiveScale c C) (positiveScale_pos hc hcC))
          1 (positiveDelta c C)) :=
  ⟨positiveDelta_mem_Ioo hc hcC, positive_interval_normalization G hc hcC⟩

/-- Correct negative-interval scale: the absolute value of the arithmetic midpoint. -/
def negativeScale (c C : ℝ) : ℝ := -(c + C) / 2

def negativeDelta (c C : ℝ) : ℝ := (C - c) / (-(C + c))

theorem negativeScale_pos {c C : ℝ} (hcC : c < C) (hC : C < 0) :
    0 < negativeScale c C := by
  unfold negativeScale
  linarith

theorem negativeDelta_mem_Ioo {c C : ℝ} (hcC : c < C) (hC : C < 0) :
    negativeDelta c C ∈ Set.Ioo (0 : ℝ) 1 := by
  have hden : 0 < -(C + c) := by linarith
  constructor
  · exact div_pos (sub_pos.2 hcC) hden
  · exact (div_lt_one hden).2 (by linarith)

theorem negative_lower_endpoint {c C : ℝ} (hcC : c < C) (hC : C < 0) :
    (-1 - negativeDelta c C) * negativeScale c C = c := by
  have hden : C + c ≠ 0 := ne_of_lt (by linarith)
  unfold negativeDelta negativeScale
  field_simp [hden]
  ring

theorem negative_upper_endpoint {c C : ℝ} (hcC : c < C) (hC : C < 0) :
    (-1 + negativeDelta c C) * negativeScale c C = C := by
  have hden : C + c ≠ 0 := ne_of_lt (by linarith)
  unfold negativeDelta negativeScale
  field_simp [hden]
  ring

/-- Centering the rescaled endpoints at `-1` forces the absolute midpoint scale. -/
theorem negative_centering_scale_unique {c C α δ : ℝ}
    (hlower : (-1 - δ) * α = c) (hupper : (-1 + δ) * α = C) :
    α = negativeScale c C := by
  unfold negativeScale
  nlinarith

/--
A strict negative interval is equivalent, after scaling by `-(c+C)/2`, to the
normalized pair `(-1-δ) h ≤ Ric_h ≤ (-1+δ) h`, with `0 < δ < 1`.
-/
theorem negative_interval_normalization
    {g : SmoothMetric n M} (G : GeometryFor n M g)
    {c C : ℝ} (hcC : c < C) (hC : C < 0) :
    RicciPinched G c C ↔
      NormalizedPinched
        (scaleGeometry G (negativeScale c C) (negativeScale_pos hcC hC))
        (-1) (negativeDelta c C) := by
  unfold NormalizedPinched
  apply ricciPinched_scale_iff_of_endpoint_identities
  · exact negative_lower_endpoint hcC hC
  · exact negative_upper_endpoint hcC hC

/-- Negative normalization together with the certified strict range `0 < δ < 1`. -/
theorem negative_interval_normalization_package
    {g : SmoothMetric n M} (G : GeometryFor n M g)
    {c C : ℝ} (hcC : c < C) (hC : C < 0) :
    negativeDelta c C ∈ Set.Ioo (0 : ℝ) 1 ∧
      (RicciPinched G c C ↔
        NormalizedPinched
          (scaleGeometry G (negativeScale c C) (negativeScale_pos hcC hC))
          (-1) (negativeDelta c C)) :=
  ⟨negativeDelta_mem_Ioo hcC hC, negative_interval_normalization G hcC hC⟩

end Yau26MetricScaling
