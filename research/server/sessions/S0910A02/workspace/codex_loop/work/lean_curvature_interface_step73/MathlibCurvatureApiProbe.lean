import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Metric
import Mathlib.Geometry.Manifold.VectorBundle.CovariantDerivative.Torsion
import Mathlib.Geometry.Manifold.Instances.Real
import Mathlib.Geometry.Manifold.Riemannian.Basic
import Mathlib.LinearAlgebra.BilinearForm.Properties
import Mathlib.LinearAlgebra.Trace
import Mathlib.Topology.Connected.Basic

/-!
Declaration-level probe for the locked Mathlib curvature stack.

This file is not a Yau--26 statement.  It records the real pieces available in
Mathlib v4.33.1 and is compiled by the Qiushi Lean checker.
-/

#check ModelWithCorners
#check ModelWithCorners.Boundaryless
#check BoundarylessManifold
#check IsManifold
#check TangentSpace
#check ContMDiffSection
#check Bundle.ContMDiffRiemannianMetric
#check Bundle.ContMDiffRiemannianMetric.toRiemannianMetric
#check Bundle.RiemannianBundle
#check Bundle.RiemannianMetric.inner
#check IsContMDiffRiemannianBundle
#check IsRiemannianManifold
#check EMetricSpace.ofRiemannianMetric
#check CovariantDerivative
#check CovariantDerivative.ContMDiffCovariantDerivative
#check CovariantDerivative.IsMetricCompatible
#check CovariantDerivative.derivMetricTensor
#check CovariantDerivative.torsion
#check CovariantDerivative.torsion_eq_zero_iff
#check LinearMap.trace
#check LinearMap.BilinForm
#check LinearMap.BilinForm.IsNonneg
#check LinearMap.BilinForm.IsPosSemidef
#check Module.finrank
#check CompactSpace
#check ConnectedSpace
#check T2Space
#check SecondCountableTopology

-- These assertions distinguish true API availability from name-search output.
example : CompactSpace PUnit := inferInstance
example : ConnectedSpace PUnit := inferInstance

-- `𝓡 n` is the real n-dimensional boundaryless model with corners.
open scoped Manifold
#check 𝓡 4
