# Step 78: A-equivariant diagonal reduction and scalar decoupling for (S²×S²)/Z₂

> **Step 79 correction notice.** Read `workspace/notes/step79_angular_rho_and_tilt_repair.md` before using this note.  The antipodal symmetry and odd scalar-kernel elimination remain valid.  The frozen substitution `rho(zeta)^-=(0,cos alpha,sin alpha)` in a fixed product frame is false for boundary integrations: Ozuch's `rho_x` depends on `x\in S^3/Z_2` and rotates through `S^2`.  Consequently §5's pointwise `R^- rho=0`, fixed block-diagonal `dR^-`, and any inference that `mu_2,mu_3` must separately vanish are superseded.  The surviving algebra is that `eta^- circ zeta^+` is factor-traceless for arbitrary `eta^-` when `zeta^+` lies in the product kernel plane, and the second-order local problem must be reduced modulo `D_phi lambda` using scale-dependent tilts.

Session `S0910A01`. Agent2 / Constructor. Phase Execute.

## Purpose

This note constructs the A-equivariant diagonal reduction for Einstein desingularization of the positive product orbifold `(S²×S²)/Z₂`. It establishes three structural theorems that dramatically simplify the Ozuch obstruction problem and identifies the leading reduced equation.

## 1. The antipodal symmetry A

### 1.1 Definition and basic properties

Define `A: S²×S² → S²×S²` by `A(x,y) = (-x,-y)`, the simultaneous antipodal map on both factors. On the round `S²(Λ)`:
- The antipodal map reverses the 2D orientation (it is an orientation-reversing isometry of S²).
- On the product, `A` reverses both factor orientations, hence PRESERVES the 4D product orientation: `(-1)·(-1) = +1`.

The quotient half-turn `σ = (r_π, r_π)` acts by π-rotation around the z-axis on each factor. Since A sends `(θ,φ) → (π−θ, φ+π)` and `r_π` sends `(θ,φ) → (θ, φ+π)`, both act by multiplicative phases/signs on spherical harmonics, hence they commute:
\[
A\sigma = \sigma A.
\]
Therefore A descends to a well-defined orientation-preserving isometry of the orbifold `(S²×S²)/Z₂`.

### 1.2 Action on nodes

The four orbifold singular points are the σ-fixed points `(pole₁, pole₂)` where each pole is north (N) or south (S). A exchanges N↔S on each factor:
\[
A: (N,N) \leftrightarrow (S,S), \qquad (N,S) \leftrightarrow (S,N).
\]
Two node orbits: `{(N,N),(S,S)}` and `{(N,S),(S,N)}`.

### 1.3 Action on chirality patterns

For the diagonal k=2 opposite chirality assignment:
\[
\varepsilon(NN) = \varepsilon(SS) = +1, \qquad \varepsilon(NS) = \varepsilon(SN) = -1,
\]
A exchanges nodes within each orbit, preserving the chirality. **Verified computationally** (data: `step78_equivariant_construction.json`).

### 1.4 Action on self-dual/anti-self-dual 2-forms

Since A preserves the 4D orientation, it preserves the decomposition `Λ² = Λ⁺ ⊕ Λ⁻`. In the standard self-dual basis at any node, A acts by transport along the manifold; since the product metric is A-invariant, the curvature blocks are preserved:
\[
A^*R^± = R^±.
\]

### 1.5 Action on metrics and harmonics

The round metrics are A-invariant: `A*gᵢ = gᵢ`. The axial first harmonic `uᵢ = Y_{1,0}` on factor i satisfies `A*uᵢ = -uᵢ` (antipodal maps negate l=1 harmonics). More generally, on product harmonics:
\[
A^*(Y_{l₁,m₁} Y_{l₂,m₂}) = (-1)^{l₁+l₂} Y_{l₁,m₁} Y_{l₂,m₂}.
\]
A-even modes have `l₁+l₂` even; A-odd modes have `l₁+l₂` odd.

## 2. Scalar kernel elimination by symmetry

**Theorem 2.1 (Equivariant kernel removal).** The four scalar-sector modes `{u₁g₁, u₁g₂, u₂g₁, u₂g₂}` in `ker(P)` are A-odd. An A-invariant approximate metric has A-invariant residual, which is automatically orthogonal to all four kernel modes.

*Proof.* Each kernel mode `uᵢgⱼ` has `l₁+l₂ = 1` (odd), so `A*(uᵢgⱼ) = -(uᵢgⱼ)`. For any A-invariant symmetric 2-tensor h:
\[
\langle h, uᵢgⱼ\rangle_{L²} = \langle A^*h, A^*(uᵢgⱼ)\rangle_{L²} = \langle h, -uᵢgⱼ\rangle = -\langle h, uᵢgⱼ\rangle,
\]
hence `⟨h, uᵢgⱼ⟩ = 0`. The Ozuch projections `νₗ` against these modes vanish by this orthogonality, not by the (incorrect) claim that the full kernel is empty. □

**Remark.** The shape mode `g₁−g₂` has `l₁=l₂=0`, so `l₁+l₂=0` (even), and is A-even. It survives the equivariant reduction. It has `P(g₁−g₂) = −Λ(g₁−g₂)` (negative eigenvalue, bounded away from zero).

## 3. Scalar decoupling theorem

**Theorem 3.1 (Factor-tracelessness of in-kernel H⁴).** For any `ζ ∈ ker(R⁺) = span{ω₂,ω₃}`, the Eguchi–Hanson quadrupole tensor
\[
H^4(\zeta^+) = -\frac{\rho(\zeta)^-\circ\zeta^+}{2r^4}
\]
has zero trace on each S² factor separately. Consequently, `H⁴(ζ)` has zero coupling to ALL scalar-sector eigenmodes `f·gₖ`, regardless of the function f.

*Proof.* Write `ζ = c\,ω₂+s\,ω₃` with `c=\cos\alpha, s=\sin\alpha`. Then `ρ(ζ)^- = c\,ω₂^-+s\,ω₃^-` and
\[
H^4 = -\tfrac12\bigl[c^2(\omega_2^-\circ\omega_2^+)+cs(\omega_2^-\circ\omega_3^++\omega_3^-\circ\omega_2^+)+s^2(\omega_3^-\circ\omega_3^+)\bigr]/r^4.
\]
Direct computation in the orthonormal product frame `(e₁,e₂,e₃,e₄)` gives:
\[
\omega_2^+\circ\omega_2^- = \operatorname{diag}(-1,1,-1,1), \qquad
\omega_3^+\circ\omega_3^- = \operatorname{diag}(-1,1,1,-1),
\]
both with `tr₁ = tr₂ = 0`. The cross compositions `ω₂^±\circ ω₃^∓` have identically zero diagonal. Therefore every term in H⁴ is factor-traceless. **Verified numerically at 37 angles** (max factor trace: `5.5×10⁻¹⁷`).

For the boundary integral coupling to a scalar eigenmode `f·gₖ`:
\[
\langle f\,g_k, H^4\rangle_{\partial B_\varepsilon} \propto
\int_{S^3/\mathbb Z_2} (g_k)_{ab} H^4_{ab}(\theta)\,d\Omega = 0,
\]
since the angular integral of `H⁴` against a constant tensor on either factor vanishes by factor-tracelessness. The coupling vanishes identically, regardless of the eigenfunction f. □
**Corollary 3.2.** The inter-node Green response for in-kernel EH desingularization lives entirely in the vector and TT sectors of `P`, where the operator is positive definite. The TT×scalar sector has spectral gap `3Λ/2`, but the mixed 1-form sector (αᵢ⊙βⱼ from factor Killing fields) has eigenvalue `Λ`. Hence the full non-scalar spectral gap is `Λ`, not `3Λ/2`. (TTCS correction.)
**Contrast.** The OUT-of-kernel direction `ω₁` gives `ω₁^+\circ\omega₁^- = -(g₁-g₂)`, which IS in the scalar sector. The scalar decoupling is specific to in-kernel EH directions.

**Corollary 3.2.** The inter-node Green response for in-kernel EH desingularization lives entirely in the vector and TT sectors of `P`, where the operator is positive definite with spectral gap ≥ `3Λ/2` (from the `(l₁,l₂)=(2,0)` TT×scalar eigenvalue in the A-even sector).

## 4. Order analysis and leading reduced equation

### 4.1 Ozuch necessary conditions

From Ozuch Theorem 0.2, for an exact nearby Einstein metric:
\[
t_j\lambda_k^j(\phi_j,v)+t_j^2\mu_k^j(\phi_j,v)=O(t_{\max}^{5/2}),\qquad
\nu_l(t\phi,v)=O(t_{\max}^{5/2}).
\]
For in-kernel `φⱼ`: `λₖʲ = 0`, so `t²μₖ = O(t^{5/2})`.

### 4.2 Inter-node interaction order

A source `H⁴(t_jφ_j) = t_j²H⁴(φ_j)` at node j produces a regular response at node i through the Green operator. Its contribution to the receiver obstruction is:
\[
t_i\cdot\delta\lambda_{i,k} = t_it_j^2\mathcal I_{ij,k} + \cdots.
\]
At comparable scales `t₁ ≈ t₂ ≈ t`, this is `O(t³)`.

### 4.3 The critical comparison

Since `5/2 < 3`, we have `t^{5/2} \gg t^3` for small `t > 0`:
\[
\frac{t^3}{t^{5/2}} = t^{1/2} \to 0 \quad\text{as }t\to0.
\]
The inter-node interaction `O(t³)` is therefore SMALLER than the Ozuch remainder `O(t^{5/2})` and does not appear in the leading finite-dimensional equation.

**Theorem 4.1 (Leading reduced equation).** In the A-equivariant diagonal construction at comparable scales, the leading finite-dimensional equations are:
\[
\mu_k(\alpha_1) = 0 \quad\text{(at orbit 1 representative)},\qquad
\mu_k(\alpha_2) = 0 \quad\text{(at orbit 2 representative)},
\]
for `k=1,2,3`. These are decoupled: no inter-node interaction at this order.

**Remark.** At unequal scales `t₁ \gg t₂`, the equation at orbit 2 becomes `t₂²μ_k + t₂t₁²I_{21,k} = O(t₁^{5/2})`, so the interaction term can compete. But the self-obstruction still leads unless `μ_k = 0` identically.

## 5. Rank-one orthogonality and the second obstruction

### 5.1 The curvature modification structure

For in-kernel `ζ`, `ρ(ζ)^-` has components `(0, c, s)` in the `Λ^-` basis. The curvature modification (Ozuch eq.(16)) is:
\[
d_\mathbf{e}R^-(H^4) = 12\,\pi_{\mathrm{tr}}(\rho(\zeta)^-\otimes\rho(\zeta)^-)/r^6
= \begin{pmatrix}-4&0&0\\0&12c^2-4&12cs\\0&12cs&12s^2-4\end{pmatrix}/r^6.
\]
This is **block-diagonal**: the `(1,2)` and `(1,3)` entries are exactly zero for all `α`. The curvature modification does not couple `ω₁^-` to the kernel directions. **Verified at 13 angles** (exact zeros).

### 5.2 R⁻ · ρ(ζ)⁻ = 0

The product orbifold has `R^- = \operatorname{diag}(\Lambda, 0, 0)`. Since `ρ(\zeta)^-` has zero `ω₁^-` component for in-kernel `ζ`:
\[
R^-\cdot\rho(\zeta)^- = \begin{pmatrix}\Lambda&0&0\\0&0&0\\0&0&0\end{pmatrix}
\begin{pmatrix}0\\c\\s\end{pmatrix} = \begin{pmatrix}0\\0\\0\end{pmatrix}.
\]
The orbifold curvature annihilates the anti-self-dual direction of the EH bubble. **Verified at 5 angles** (exact zeros).

### 5.3 Consequences for μ₂ and μ₃

The second Ozuch obstruction involves curvature contractions of the form `R^±` acting on the components of `ρ(ζ)^±`. Since `ρ(ζ)^-` lies in `ker(R^-)` and `R` is parallel on the product orbifold (`∇R = 0`), the curvature provides no mechanism to produce a nonzero second obstruction.

**Proved:** `μ₁ = 0` (rank-one determinant, Step 76).

**Rank-one orthogonality evidence:** `R^-·ρ(ζ)^- = 0` and `∇R = 0` eliminate the leading curvature contraction. However, TTCS identified that `dR^-·v = 8v/r⁶ ≠ 0` (the curvature modification in the kernel direction is nonzero) and `R^-·dR^- ≠ 0`. These nonzero quantities can enter the full Biq16 formula for μ₂ and μ₃. Therefore the rank-one orthogonality is necessary but NOT sufficient to prove μ₂ = μ₃ = 0. The decisive computation is the actual Biq16 formula evaluation.

### 5.4 Additional structure

The curvature modification `dR^-` has:
- Entry (1,1) = −4: universal (independent of α)
- Kernel block determinant = −32: universal and nonzero
- No ω₁↔kernel coupling

This means the curvature modification lives in the same block structure as `R^-` itself: it changes the nonzero eigenvalue but does not create off-diagonal coupling to the kernel. This block-diagonal preservation is a consequence of the rank-1 structure and the in-kernel constraint. However, the kernel block itself has eigenvalues `8` (along v) and `−4` (perpendicular), both nonzero. These enter higher-order obstruction formulas.

## 6. The equivariant parameter space

The A-equivariant diagonal construction has four parameters:
\[
(t_1, \alpha_1, t_2, \alpha_2) \in \mathbb R_+^2 \times [0,\pi)^2.
\]

| Orbit | Nodes | Scale | Angle | Chirality |
|-------|-------|-------|-------|-----------|
| 1 | {(N,N),(S,S)} | t₁ | α₁ | + |
| 2 | {(N,S),(S,N)} | t₂ | α₂ | − |

**Eliminated by A-symmetry:** All four `νₗ` projections (scalar kernel equations).

**Leading equations:** `μ_k(αᵢ) = 0` at each orbit, decoupled.

**If μ₂ = μ₃ = 0 (unproved, supported by partial evidence):** The approximate metric satisfies all Ozuch necessary conditions at `O(t^{5/2})` for arbitrary equal-orbit scales and in-kernel angles. The remaining task is the inverse estimate and nonlinear contraction on the positive-definite non-scalar sector.

**SO(2) covariance in the kernel plane.** The curvature `R = diag(Λ,0,0)` is invariant under SO(2) rotations in span{ω₂,ω₃}. The adapted obstruction basis (ζ_{(k)}) transforms covariantly under this rotation. Therefore μ₂ and μ₃ are each INDEPENDENT of the in-kernel angle α. Either both vanish identically (for all α) or are nonzero constants. The angle α is a pure gauge degree of freedom at the obstruction level. It suffices to check μ₂ and μ₃ at one convenient angle (e.g., α=0, ζ=ω₂).

**Topology:** The diagonal k=2 opposite pattern gives `#3(S²×S²)` (even b₂, spin, χ=8, τ=0).

## 7. Non-scalar sector spectral structure

The P eigenvalue on the TT₁×scalar₂ sector (TT tensor on factor 1, scalar on factor 2):
\[
\mu_{l_1,l_2}^{TT\times\text{sc}} = \frac\Lambda2\bigl(l_1(l_1+1)+l_2(l_2+1)-3\bigr),\qquad l_1\ge2.
\]

Lowest A-even eigenvalues (l₁+l₂ even):
| (l₁,l₂) | Sector | P eigenvalue |
|----------|--------|-------------|
| (2,0) | TT₁×sc₂ | 3Λ/2 |
| (0,2) | sc₁×TT₂ | 3Λ/2 |
| (2,2) | TT₁×sc₂ | 9Λ/2 |
| (3,1) | TT₁×sc₂ | 11Λ/2 |

All positive. The spectral gap is `3Λ/2`, which provides the inverse bound for the linearized equation away from the kernel.

The H⁴ source at a node couples to `|m|=2` TT modes (the only modes with nonzero TT value at a pole), not `m=0` modes.

## 8. What remains

1. **Verify μ₂ = μ₃ = 0** from the complete Biq16 formulas (not just the leading R⁻ action). The rank-one orthogonality provides strong structural evidence, but the explicit coefficient check is needed.

2. **Weighted Schauder/Hölder inverse estimate** on the non-scalar sector. The positive spectral gap `3Λ/2` should give a bounded inverse in appropriate weighted spaces. The A-equivariance removes the kernel obstruction.

3. **Nonlinear contraction estimate.** The quadratic terms in the full Einstein equation must be controlled by the linear inverse.

4. **Convergence to exact Einstein metric.** If items 1–3 succeed, the implicit function theorem gives an exact positive Einstein metric on `#3(S²×S²)`, which would be the first known positive Einstein metric on this smooth type.

## Files

- Equivariant construction data: `workspace/data/step78_equivariant_construction.json`
- Spectral structure data: `workspace/data/step78_spectral_structure.json`
- Rank-one orthogonality data: `workspace/data/step78_rank_one_orthogonality.json`
- Scripts: `workspace/scripts/step78_equivariant_construction.py`, `step78_spectral_structure.py`, `step78_rank_one_orthogonality.py`
- Corrected Step 77 note: `workspace/notes/step77_mixed_row_obstruction_repair.md`
- Ozuch source: Knowledge lines 95–149 (Theorem 0.2), 315–369 (H⁴ and EH deformations), 618–714 (global construction), 730–799 (multi-node estimates)
