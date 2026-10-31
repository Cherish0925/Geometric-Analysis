# Step 63 (cont.): The flat-to-non-flat matching problem

Session: S0910A03. Agent2 / Constructor. Phase: Explore.

## 1. Precise formulation

**Goal.** Construct a smooth Riemannian metric on $T^3 \times [-1, 1]$ with:
- At $r = -1$: the metric restricts to a flat torus (matching a hyperbolic cusp).
- At $r = +1$: the metric restricts to the same flat torus (matching another cusp).
- Everywhere: $\|\operatorname{Ric}_g + 3g\|_{\mathrm{op}} \le \delta$ for small $\delta$.
- The mean curvature $H(r)$ transitions from $-3$ to $+3$ (contracting to expanding).

If such a metric exists for arbitrarily small $\delta$, extended graph manifolds
carry approximate Einstein metrics, giving a Yau 26 counterexample.

## 2. Reduction to slice geometry

Write $g = dr^2 + G(r)$ where $G(r)$ is a $r$-dependent metric on $T^3$.
The Ricci tensor has three blocks:

**Radial-radial:**
$$\operatorname{Ric}(\partial_r, \partial_r) = -\frac{1}{2}\operatorname{tr}(S') - \frac{1}{2}|S|^2$$
where $S = \frac{1}{2}G^{-1}G'$ is the shape operator.

**Radial-tangential:**
$$\operatorname{Ric}(\partial_r, X) = \frac{1}{2}\left[\nabla^i S_{iX} - \partial_X H\right]$$
(divergence of shape operator minus gradient of mean curvature).

**Tangential-tangential:**
$$\operatorname{Ric}(X, Y) = \operatorname{Ric}_{G(r)}(X, Y) - S'_{XY} - H S_{XY} + 2(S^2)_{XY}$$

### 2.1 Target conditions

For $\operatorname{Ric} = -3g$:
- Radial: $\operatorname{tr}(S') + |S|^2 = 6$.
- Mixed: $\nabla^i S_{iX} = \partial_X H$ (Codazzi equation for the slice).
- Tangential: $\operatorname{Ric}_{G(r)} - S' - HS + 2S^2 = -3G$.

The Codazzi equation is automatically satisfied if $G(r)$ is a family of
homogeneous metrics on $T^3$ (all components constant in $X$). For
non-homogeneous metrics, the Codazzi equation is a constraint.

## 3. The simplest model: isotropic non-flat slices

Let $G(r) = f(r)^2 g_N(r)$ where $g_N(r)$ is a family of metrics on $T^3$
with $\operatorname{Ric}_{g_N(r)} = -\alpha(r) g_N(r)$.

Then $S = (f'/f)\operatorname{Id} + \frac{1}{2}g_N^{-1}g_N'$.

**Case A: $g_N$ fixed (independent of $r$).**
Then $S = (f'/f)\operatorname{Id}$, isotropic, $H = 3f'/f$.

Radial: $3(f'/f)' + 3(f'/f)^2 = 3f''/f = 6 \Rightarrow f'' = 2f$.
Solution: $f = A\cosh(\sqrt{2}r) + B\sinh(\sqrt{2}r)$.

Wait — this gives $f''/f = 2$, not 1 as in the cosh model. Let me recheck.

Actually, the radial Ricci is:
$\operatorname{Ric}(\partial_r,\partial_r) = -3f''/f$.
For this to equal $-3$: $f''/f = 1$, so $f'' = f$, giving $f = \cosh$ (as before).

But then the tangential Ricci is:
$\operatorname{Ric}_{tang} = \operatorname{Ric}_N/f^2 - (f''/f + 2(f'/f)^2) = -\alpha/f^2 - 1 - 2\tanh^2(r)$.

For $\operatorname{Ric}_{tang} = -3$: $\alpha/f^2 = 2 - 2\tanh^2(r) = 2\operatorname{sech}^2(r)$.
So $\alpha = 2f^2\operatorname{sech}^2(r) = 2\cosh^2(r)/\cosh^2(r) = 2$.

So with FIXED $\alpha = 2$ (i.e., $\operatorname{Ric}_N = -2g_N$ fixed), the metric
$g = dr^2 + \cosh^2(r) g_N$ has **exactly** $\operatorname{Ric} = -3g$.

**The issue is only the boundary matching**: at $r = \pm L$, the slice metric
is $\cosh^2(L) g_N$, not flat.

### 3.1 Boundary transition

At the cusp boundary $r = L$, we need to match:
- Einstein side: slice metric $\cosh^2(L) g_N$, shape $S = \tanh(L) \operatorname{Id}$.
- Cusp side: slice metric $e^{-2L} g_0$ (flat), shape $S = -\operatorname{Id}$.

These don't match in two ways:
1. **Metric**: $\cosh^2(L) g_N \ne e^{-2L} g_0$ (different conformal factor AND different base).
2. **Shape**: $\tanh(L) \approx 1$ vs $-1$ (opposite signs).

The shape mismatch is expected: the Einstein collar has $H > 0$ (expanding),
the cusp has $H < 0$ (contracting). The transition region is where $H$ changes sign.

The metric mismatch requires $g_N \to g_0$ as we approach the boundary. This means
$g_N$ must **deform from Ric = -2 to flat** within the collar. This deformation itself
contributes to the Ricci tensor.

## 4. The deformation problem

**Question.** Can a smooth family $g_N(r)$ of metrics on $T^3$ interpolate between:
- $g_N(-L) = g_0$ (flat, $\operatorname{Ric} = 0$),
- $g_N(0) = g_N^*$ (with $\operatorname{Ric} = -2g_N^*$),
- $g_N(L) = g_0$ (flat again),
while maintaining $\|\operatorname{Ric}_g + 3g\|_{\mathrm{op}} \le \delta$?

The key constraint is the tangential Ricci:
$$\operatorname{Ric}_{tang} = \operatorname{Ric}_{G(r)} - S' - HS + 2S^2$$

If $G(r) = f(r)^2 g_N(r)$ with $g_N$ deforming, then $S$ has both an isotropic part
($f'/f$) and an anisotropic part ($g_N^{-1}g_N'/2$). The anisotropic part contributes
to $|S|^2$ and hence to the radial Ricci.

### 4.1 Lohkamp interpolation

By Lohkamp's theorem, there exist smooth paths of metrics on $T^3$ from flat to
$\operatorname{Ric} = -2$. The path can be chosen with bounded derivatives (since $T^3$
is compact and the space of metrics is open).

**Crude estimate.** If the path has length $\ell$ in the $C^2$ topology, then
$|g_N'| \sim |g_N|/\ell$ and $|g_N''| \sim |g_N|/\ell^2$. The anisotropic shape
operator contributes $O(1/\ell)$ to $S$ and $O(1/\ell^2)$ to $S'$. For the radial
Ricci to remain near $-3$, we need $\ell$ large enough that these are $O(\delta)$.

But $\ell$ large means the collar is long, which is fine — the collar length is a
free parameter. The question is whether the defect can be made arbitrarily small.

**Scaling.** If we scale the $r$ coordinate by $r \to \lambda r$, then $S \to S/\lambda$
and $S' \to S'/\lambda^2$. The defect from the $g_N$ deformation scales as $1/\lambda^2$.
By taking $\lambda$ large (long collar), the deformation defect can be made arbitrarily small.

**However**, the isotropic part also changes: the cosh function now has a longer
transition region, and its own defect profile changes. The total defect is:
$$\delta \sim \max\left(\delta_{\mathrm{isotropic}}, \frac{C}{\lambda^2}\right)$$
where $\delta_{\mathrm{isotropic}}$ is the defect from the pure cosh model with
$\operatorname{Ric}_N = -2$ (which is **zero** — the cosh model is exact Einstein).

So the total defect is $\delta \sim C/\lambda^2 \to 0$ as $\lambda \to \infty$.

**This suggests that arbitrarily tight pinching IS possible!**

## 5. The critical subtlety: the isotropic-defect interaction

The above scaling argument is too naive. The issue is that when $g_N$ is deforming,
the pure cosh solution no longer gives exact Einstein. The isotropic and anisotropic
parts interact.

More precisely, the full system is:
- Radial: $\operatorname{tr}(S') + |S|^2 = 6 + O(\delta)$.
- Tangential: $\operatorname{Ric}_N/f^2 - S'_{tang} - H S_{tang} + 2(S^2)_{tang} = -3G + O(\delta)$.

With $S = u\operatorname{Id} + \Sigma$ where $u = f'/f$ (isotropic) and
$\Sigma = \frac{1}{2}g_N^{-1}g_N'$ (traceless anisotropic):

Radial: $3u' + 3u^2 + \operatorname{tr}(\Sigma') + 2u\operatorname{tr}(\Sigma) + |\Sigma|^2 = 6$.
Since $\operatorname{tr}(\Sigma) = 0$: $3u' + 3u^2 + |\Sigma|^2 = 6$.

This is the key equation. The anisotropic shear $|\Sigma|^2 \ge 0$ **increases** the
radial acceleration. In the pure isotropic case ($\Sigma = 0$): $u' + u^2 = 2$, giving
$u = \sqrt{2}\tanh(\sqrt{2}r)$. Wait, let me redo this.

For the Einstein target $\operatorname{Ric}(\partial_r,\partial_r) = -3$:
$3u' + 3u^2 = 6$ (isotropic, $\Sigma=0$).
$u' = 2 - u^2$.
Equilibria at $u = \pm\sqrt{2}$.

Hmm, this doesn't match the cosh model where $u = \tanh(r)$ and the equilibria are at
$\pm 1$. Let me recheck.

For $g = dr^2 + f^2 g_N$ with FIXED $g_N$ ($\operatorname{Ric}_N = -2g_N$):
$\operatorname{Ric}(\partial_r,\partial_r) = -3f''/f$.
For Ric = $-3$: $f''/f = 1$, $f = \cosh(r)$, $u = f'/f = \tanh(r)$.
Equilibria at $u = \pm 1$.

But from the formula: $3u' + 3u^2 = 6 \Rightarrow u' = 2 - u^2$.
For $u = \tanh(r)$: $u' = \operatorname{sech}^2(r) = 1 - \tanh^2(r) = 1 - u^2$.
So $u' = 1 - u^2$, not $2 - u^2$.

The discrepancy: the radial Ricci formula gives $-3f''/f$, and for $f = \cosh$:
$f''/f = 1$, so $\operatorname{Ric} = -3$. ✓

But $u = f'/f$, so $u' = f''/f - (f'/f)^2 = 1 - u^2$.
Then $3u' + 3u^2 = 3(1-u^2) + 3u^2 = 3 \ne 6$.

I made an error. The correct radial Ricci formula for $g = dr^2 + G(r)$ is:
$$\operatorname{Ric}(\partial_r,\partial_r) = -\operatorname{tr}(S') - |S|^2$$
where $S = \frac{1}{2}G^{-1}G'$.

For $G = f^2 g_N$ (fixed $g_N$): $S = (f'/f)\operatorname{Id}$ (on the 3-dim slice).
$\operatorname{tr}(S') = 3(f'/f)' = 3u'$.
$|S|^2 = 3u^2$.
$\operatorname{Ric}(\partial_r,\partial_r) = -3u' - 3u^2 = -3(u' + u^2)$.

For Ric = $-3$: $u' + u^2 = 1$. With $u = \tanh(r)$: $u' = 1-u^2$, so $u'+u^2 = 1$. ✓

So the correct equation is $u' + u^2 = 1$, equilibria at $u = \pm 1$. Good.

**With anisotropic shear:**
$\operatorname{Ric}(\partial_r,\partial_r) = -3u' - 3u^2 - |\Sigma|^2 - \operatorname{tr}(\Sigma')$.

Wait, actually $\operatorname{tr}(S') = 3u' + \operatorname{tr}(\Sigma')$, and
$\operatorname{tr}(\Sigma') = (\operatorname{tr}\Sigma)' = 0$ (since $\Sigma$ is traceless).
$|S|^2 = 3u^2 + |\Sigma|^2$ (cross term vanishes since $\Sigma$ is traceless).

So: $\operatorname{Ric}(\partial_r,\partial_r) = -3u' - 3u^2 - |\Sigma|^2$.

For Ric = $-3 + O(\delta)$:
$$3u' + 3u^2 + |\Sigma|^2 = 3 + O(\delta)$$
$$u' = 1 - u^2 - \frac{|\Sigma|^2}{3} + O(\delta)$$

The shear $|\Sigma|^2$ **slows down** the transition. If $|\Sigma|^2$ is small
(long collar), the effect is small. But $|\Sigma|^2$ is determined by the rate of
deformation of $g_N$, which is $O(1/\lambda^2)$ for a collar of length $\lambda$.

**The key question is the tangential equation.** The tangential Ricci is:
$$\operatorname{Ric}_{tang} = \operatorname{Ric}_{G(r)} - S' - HS + 2S^2$$

For $G = f^2 g_N(r)$ with deforming $g_N$:
- $\operatorname{Ric}_{G(r)} = \operatorname{Ric}_{g_N(r)}/f^2$ (not exactly, because the
  3D Ricci of $f^2 g_N$ is $\operatorname{Ric}_{g_N}/f^2$ only if $g_N$ is fixed;
  for deforming $g_N$ there are correction terms from the $r$-dependence).

Actually, the intrinsic Ricci of the slice $\{r\} \times T^3$ with metric $G(r) = f(r)^2 g_N(r)$
is just the Ricci of the 3D metric $f(r)^2 g_N(r)$, which is
$\operatorname{Ric}_{f^2 g_N} = \operatorname{Ric}_{g_N}$ (since Ricci is invariant under constant
conformal rescaling in dimension 3... wait, no: $\operatorname{Ric}_{cg} = \operatorname{Ric}_g$
for constant $c > 0$ in any dimension).

So $\operatorname{Ric}_{G(r)} = \operatorname{Ric}_{g_N(r)}$ as a tensor on $T^3$.
If $\operatorname{Ric}_{g_N(r)} = -\alpha(r) g_N(r)$, then
$\operatorname{Ric}_{G(r)} = -\alpha(r) g_N(r) = -\alpha(r)/f(r)^2 \cdot G(r)$.

The tangential equation becomes:
$$-\frac{\alpha(r)}{f^2} G - S' - HS + 2S^2 = -3G + O(\delta)$$

For the isotropic part ($S = u\operatorname{Id}$):
$$-\frac{\alpha}{f^2} - u' - 3u \cdot u + 2u^2 = -3$$
$$-\frac{\alpha}{f^2} - u' - u^2 = -3$$
$$u' = 3 - u^2 - \frac{\alpha}{f^2}$$

Combined with the radial equation $u' = 1 - u^2 - |\Sigma|^2/3$:
$$3 - u^2 - \frac{\alpha}{f^2} = 1 - u^2 - \frac{|\Sigma|^2}{3}$$
$$\frac{\alpha}{f^2} = 2 + \frac{|\Sigma|^2}{3}$$

This is the **consistency condition**. For $\Sigma = 0$: $\alpha = 2f^2$.
With $f = \cosh$: $\alpha = 2\cosh^2(r)$, which varies with $r$.

But we wanted $\alpha = 2$ (fixed). The resolution: in the exact Einstein model,
$G(r) = \cosh^2(r) g_N$ with FIXED $g_N$ ($\alpha = 2$ fixed). The intrinsic
metric on the slice at $r$ is $\cosh^2(r) g_N$, and its Ricci (as a tensor on $T^3$)
is $\operatorname{Ric}_{g_N} = -2g_N$. But as a tensor with respect to $G(r)$:
$\operatorname{Ric}_{G(r)} = -2g_N = -\frac{2}{\cosh^2(r)} G(r)$.
So the effective $\alpha(r) = \frac{2}{\cosh^2(r)}$ in the $G(r)$ frame.

OK so I need to be more careful. Let me redefine.

**Setup.** $g = dr^2 + G(r)$ on $\mathbb{R} \times T^3$.
$S = \frac{1}{2}G^{-1}G'$, $H = \operatorname{tr}S$.

**Radial Ricci:** $\operatorname{Ric}_{rr} = -\operatorname{tr}(S') - |S|^2$.
(Note: $S' = \frac{dS}{dr}$, not the covariant derivative.)

**Tangential Ricci:** $\operatorname{Ric}_{XY} = \operatorname{Ric}^{T^3}_{G(r)}(X,Y)
- S'_{XY} - HS_{XY} + 2(S^2)_{XY}$ for $X, Y$ tangent to $T^3$.

Here $\operatorname{Ric}^{T^3}_{G(r)}$ is the intrinsic Ricci tensor of the 3D metric
$G(r)$ on $T^3$.

**For the exact Einstein model $G(r) = \cosh^2(r) g_N$:**

$S = \tanh(r) \operatorname{Id}$ (isotropic).
$H = 3\tanh(r)$.
$S' = \operatorname{sech}^2(r) \operatorname{Id}$.
$\operatorname{tr}(S') = 3\operatorname{sech}^2(r)$.
$|S|^2 = 3\tanh^2(r)$.

Radial: $-3\operatorname{sech}^2 - 3\tanh^2 = -3(\operatorname{sech}^2+\tanh^2) = -3 \cdot 1 = -3$. ✓

Tangential: $\operatorname{Ric}^{T^3}_{G(r)} = \operatorname{Ric}_{g_N} = -2g_N$
(since $\operatorname{Ric}$ is invariant under constant conformal rescaling).

Wait, is that right? For a 3D metric $G = c^2 g_N$ (constant $c$):
$\operatorname{Ric}_G = \operatorname{Ric}_{g_N}$? Yes — Ricci is scale-invariant as a
(0,2)-tensor under constant conformal rescaling in any dimension.

So $\operatorname{Ric}^{T^3}_{G(r)} = -2g_N = -\frac{2}{\cosh^2(r)}G(r)$.

Tangential Ricci:
$$-\frac{2}{\cosh^2}G - \operatorname{sech}^2 \operatorname{Id} - 3\tanh \cdot \tanh \operatorname{Id}
+ 2\tanh^2 \operatorname{Id}$$
$$= \left[-\frac{2}{\cosh^2} - \operatorname{sech}^2 - 3\tanh^2 + 2\tanh^2\right]G$$
$$= \left[-2\operatorname{sech}^2 - \operatorname{sech}^2 - \tanh^2\right]G$$
$$= \left[-3\operatorname{sech}^2 - \tanh^2\right]G$$

For this to equal $-3G$: $-3\operatorname{sech}^2 - \tanh^2 = -3$.
$3\operatorname{sech}^2 + \tanh^2 = 3$.
$3(1-\tanh^2) + \tanh^2 = 3$.
$3 - 3\tanh^2 + \tanh^2 = 3$.
$3 - 2\tanh^2 = 3$.
$\tanh^2 = 0$.

This is only true at $r = 0$! **The cosh model with FIXED $g_N$ is NOT exact Einstein!**

I made an error earlier. Let me recalculate.

Actually, I think the error is in the formula for tangential Ricci. The standard formula
for $g = dr^2 + f(r)^2 g_N$ (warped product with FIXED fiber metric $g_N$) is:

$\operatorname{Ric}(X,Y) = \operatorname{Ric}_N(X,Y) - \left[\frac{f''}{f} + (n-1)\frac{(f')^2}{f^2}\right] g(X,Y)$

where $n = 3$ is the fiber dimension, and $X,Y$ are lifts of tangent vectors to $N$.

Wait, this formula has $(n-1)$ where $n$ is the fiber dimension. Let me double-check.

For $g = dr^2 + f(r)^2 g_N$ on $\mathbb{R} \times N$ with $\dim N = k$:

$\operatorname{Ric}(\partial_r, \partial_r) = -k \frac{f''}{f}$

$\operatorname{Ric}(X,Y) = \operatorname{Ric}_N(X,Y) - \left[\frac{f''}{f} + (k-1)\frac{(f')^2}{f^2}\right] g(X,Y)$

For $k = 3$, $N = T^3$:

$\operatorname{Ric}(\partial_r,\partial_r) = -3f''/f$.

$\operatorname{Ric}(X,Y) = \operatorname{Ric}_N(X,Y) - [f''/f + 2(f'/f)^2] f^2 g_N(X,Y)$.

For $f = \cosh$, $g_N$ with $\operatorname{Ric}_N = -2g_N$:

$\operatorname{Ric}(X,Y) = -2g_N(X,Y) - [1 + 2\tanh^2] \cosh^2 g_N(X,Y)$
$= [-2 - \cosh^2 - 2\sinh^2] g_N(X,Y)$
$= [-2 - \cosh^2 - 2(\cosh^2-1)] g_N(X,Y)$
$= [-2 - \cosh^2 - 2\cosh^2 + 2] g_N(X,Y)$
$= -3\cosh^2 g_N(X,Y)$
$= -3 g(X,Y)$ ✓

So the warped product formula gives the correct answer: the metric IS exact Einstein.

My earlier computation using the $S$ formalism was wrong because I conflated
the intrinsic Ricci $\operatorname{Ric}^{T^3}_{G(r)}$ (which is a tensor on $T^3$
in the $G(r)$ metric) with the warped product formula. The correct relation is:

$\operatorname{Ric}^{T^3}_{G(r)}(X,Y) = \operatorname{Ric}_{g_N}(X,Y) = -2g_N(X,Y)$
$= -\frac{2}{\cosh^2(r)}G(r)(X,Y)$.

And the warped product formula gives:
$\operatorname{Ric}(X,Y) = \operatorname{Ric}^{T^3}_{G(r)}(X,Y) - [f''/f + 2(f'/f)^2] G(r)(X,Y)$
$= [-2/\cosh^2 - 1 - 2\tanh^2]G(X,Y)$
$= [-2\operatorname{sech}^2 - 1 - 2\tanh^2]G(X,Y)$.

Now: $2\operatorname{sech}^2 + 1 + 2\tanh^2 = 2(1-\tanh^2) + 1 + 2\tanh^2 = 3$. ✓

So $\operatorname{Ric}(X,Y) = -3G(X,Y)$. The model IS exact Einstein. Good.

**The error in my $S$-formalism computation** was using the wrong tangential Ricci formula.
The correct formula in terms of $S$ is:

$\operatorname{Ric}(X,Y) = \operatorname{Ric}^{slice}(X,Y) - S'_{XY} - HS_{XY} + 2(S^2)_{XY}$

where $\operatorname{Ric}^{slice}$ is the intrinsic Ricci of the slice.

For the cosh model: $\operatorname{Ric}^{slice} = -2g_N = -(2/\cosh^2)G$.
$S = \tanh \operatorname{Id}$, $H = 3\tanh$, $S' = \operatorname{sech}^2 \operatorname{Id}$.

$\operatorname{Ric}(X,Y) = [-2\operatorname{sech}^2 - \operatorname{sech}^2 - 3\tanh^2 + 2\tanh^2]G$
$= [-3\operatorname{sech}^2 - \tanh^2]G$.

For this to be $-3G$: $3\operatorname{sech}^2 + \tanh^2 = 3$.
$3(1-\tanh^2) + \tanh^2 = 3 - 2\tanh^2 = 3$ iff $\tanh = 0$.

But the warped product formula says it's exact Einstein everywhere. **Contradiction!**

Let me recheck the $S$-formalism tangential formula. The Gauss equation for a
hypersurface is:

$R_M(X,Y,Z,W) = R_N(X,Y,Z,W) + \langle SX, Z\rangle\langle SY, W\rangle - \langle SX, W\rangle\langle SY, Z\rangle$

The Ricci tensor of $M$ restricted to tangent vectors:
$\operatorname{Ric}_M(X,Y) = \operatorname{Ric}_N(X,Y) + \langle R(\partial_r, X)Y, \partial_r\rangle
+ H\langle SX, Y\rangle - \langle S^2X, Y\rangle$

Hmm, this is getting complicated. The term $\langle R(\partial_r,X)Y,\partial_r\rangle$
is related to $S'$ by the "radial curvature equation":
$\langle R(\partial_r,X)Y,\partial_r\rangle = -(S')_{XY} + (S^2)_{XY}$.

So: $\operatorname{Ric}_M(X,Y) = \operatorname{Ric}_N(X,Y) - (S')_{XY} + (S^2)_{XY}
+ H S_{XY} - (S^2)_{XY}$
$= \operatorname{Ric}_N(X,Y) - (S')_{XY} + H S_{XY}$.

Let me redo with this: $\operatorname{Ric}_M(X,Y) = \operatorname{Ric}_N(X,Y) - S'_{XY} + HS_{XY}$.

For cosh: $\operatorname{Ric}_M = -2\operatorname{sech}^2 G - \operatorname{sech}^2 G + 3\tanh^2 G$
$= [-3\operatorname{sech}^2 + 3\tanh^2]G = -3[\operatorname{sech}^2 - \tanh^2]G = -3[1-2\tanh^2]G$.

For this to be $-3G$: $1 - 2\tanh^2 = 1$ iff $\tanh = 0$. Still wrong.

Hmm, I think the sign of the $HS$ term might be wrong. Let me look up the standard formula.

For $g = dr^2 + G(r)$, the second fundamental form is $II(X,Y) = \langle SX, Y\rangle$
where $S = \frac{1}{2}G^{-1}G'$. The Ricci tensor is:

$\operatorname{Ric}_M(X,Y) = \operatorname{Ric}_N(X,Y) - \mathcal{L}_{\partial_r}(II)(X,Y)
+ 2(II \circ II)(X,Y) - H \cdot II(X,Y)$

where $\mathcal{L}_{\partial_r}(II) = S' + $ correction terms.

Actually, I think the issue is that $S'$ should be the Lie derivative, not the
ordinary derivative. For $S = \frac{1}{2}G^{-1}G'$:

$\mathcal{L}_{\partial_r}S = \frac{dS}{dr}$ (since $\partial_r$ is a coordinate vector field).

And $\mathcal{L}_{\partial_r}(II)(X,Y) = \partial_r(II(X,Y)) - II([\partial_r,X],Y) - II(X,[\partial_r,Y])$.

For $X, Y$ tangent to the slice and $[\partial_r, X] = 0$ (if $X$ is a coordinate field
on the slice extended constantly in $r$): $\mathcal{L}_{\partial_r}(II) = \partial_r(II)$.

But $II_{XY} = \langle SX, Y\rangle_G = G(SX, Y)$. So
$\partial_r(II_{XY}) = \partial_r(G(SX,Y)) = G'(SX,Y) + G(S'X,Y) + G(SX',Y)$.

This is getting messy. Let me just use the standard warped product formula, which I
already verified gives the correct answer.

**Standard warped product formulas** for $g = dr^2 + f(r)^2 g_N$, $\dim N = k$:

(1) $\operatorname{Ric}(\partial_r,\partial_r) = -k\frac{f''}{f}$.

(2) $\operatorname{Ric}(\partial_r,X) = 0$.

(3) $\operatorname{Ric}(X,Y) = \operatorname{Ric}_N(X,Y) - \left[\frac{f''}{f} + (k-1)\frac{(f')^2}{f^2}\right] f^2 g_N(X,Y)$.

These are well-known and correct. The cosh model with $\operatorname{Ric}_N = -2g_N$ gives
exact Einstein.

## 6. The actual matching problem

Now that the exact Einstein model is confirmed, the matching problem is:

**Input.** A hyperbolic cusp end $[0,\infty) \times T^3$ with metric
$g_{cusp} = dr^2 + e^{-2r} g_0$ ($g_0$ flat on $T^3$).

**Output.** An Einstein collar $[-L,L] \times T^3$ with metric
$g_{collar} = dr^2 + \cosh^2(r) g_N$ ($\operatorname{Ric}_{g_N} = -2g_N$).

**Interface.** At $r = L$ (collar) matches $r = 0$ (cusp):
- Collar slice: $\cosh^2(L) g_N$ (non-flat).
- Cusp slice: $g_0$ (flat).

**Gap.** The metrics don't match. A transition region is needed.

### 6.1 Transition region

In the transition region $[L, L+\ell] \times T^3$, the metric $G(r)$ must deform from
$\cosh^2(L)g_N$ to $e^{-2(L+\ell)}g_0$... wait, the cusp metric at $r=0$ has slice
metric $g_0$ (not scaled). So the matching is:

At $r = L$: collar has $G(L) = \cosh^2(L) g_N$.
At $r = L + \ell$: cusp has $G(L+\ell) = e^{-2\ell'} g_0$ for some $\ell'$.

Actually, the cusp coordinate and collar coordinate are independent. Let me use a single
coordinate $r$ for the whole collar + transition + cusp.

At the cusp end ($r \to \infty$): $G(r) \approx e^{-2r}g_0$ (contracting).
At the collar end ($r \to -\infty$): $G(r) \approx \cosh^2(r) g_N$ (expanding as $r \to -\infty$,
i.e., $H \to +3$).

Wait, for a compact manifold, we don't have infinite ends. Let me reconsider.

### 6.2 Compact graph manifold structure

An extended graph 4-manifold $M$ is assembled from:
- **Pure pieces** $V_i$: finite-volume hyperbolic 4-manifolds with toral cusps,
  truncated at some horospherical level.
- **Product pieces**: $T^2 \times V_j$ where $V_j$ is a finite-volume hyperbolic surface.
- **Gluing**: torus boundary components glued by affine diffeomorphisms.

The metric on each pure piece is exactly hyperbolic (Ric = $-3g$) in the interior.
The cusp metric is $dr^2 + e^{-2r}g_0$ for $r \ge 0$.

**The transition from one pure piece to another** goes through a collar $T^3 \times [-1,1]$.
On each side, the metric is hyperbolic with flat torus cross-sections.
The collar must transition from one flat torus to another (possibly different shape).

**Key insight**: Within a single pure piece, the cusp metric already has flat slices.
The collar between two pieces also starts and ends with flat slices. The question is
whether the interior of the collar can deviate from flat to achieve the transition.

### 6.3 The naive approach fails

If we try to use only flat slices ($G(r) = f(r)^2 g_0$ with fixed flat $g_0$),
the flat-slice barrier prevents $H$ from changing sign for $\delta < 3/2$.

### 6.4 The non-flat approach

If we allow non-flat slices, the transition can go through $g_N$ with
$\operatorname{Ric}_{g_N} = -2g_N$. The exact Einstein funnel $dr^2 + \cosh^2(r)g_N$
provides the interior, but the boundary slices are non-flat.

**The matching at each boundary requires** a local deformation from flat to non-flat.
This deformation is on the slice metric only (not the 4D metric), and can be done
in a thin annulus $[L, L+\epsilon] \times T^3$.

In this annulus, the 4D metric is $dr^2 + G(r)$ where $G(r)$ interpolates from
$\cosh^2(L)g_N$ to (say) $e^{2L}g_0$ (some flat metric at a comparable scale).

The Ricci defect in this annulus comes from:
1. The anisotropic shear $\Sigma = \frac{1}{2}g_N^{-1}g_N' \ne 0$.
2. The deviation of the intrinsic slice Ricci from $-2g_N$.

By Lohkamp's path, the deformation can be done with $|g_N'| = O(1/\epsilon)$
and $|g_N''| = O(1/\epsilon^2)$. The defect is $O(1/\epsilon^2)$.

But $\epsilon$ can be large! We can take a long transition annulus. The only
constraint is the total length of the collar, which is bounded by the diameter
of the manifold. Since the manifold is compact, the diameter is finite, but we
can make the collar as long as we want by choosing the graph manifold with
large enough pieces.

**This is the key**: for a fixed graph manifold, the collar length is bounded,
so the defect has a floor $\delta_0 > 0$. But by taking a sequence of graph
manifolds with increasingly large pieces (or increasingly many pieces), the
collar length can grow, and $\delta_0 \to 0$.

**Wait, but the Yau 26 question is about a fixed dimension, not a fixed manifold.**
For each $n$, we need a sequence of manifolds with $\delta_i \to 0$. The graph
manifolds with increasingly large hyperbolic pieces provide exactly this!

### 6.5 The Lohkamp defect more carefully

Actually, the Lohkamp deformation from flat to $\operatorname{Ric} = -2$ on $T^3$
is a global deformation. The defect is not just from the $r$-derivative but from
the intrinsic 3D geometry of the deforming slices.

More precisely: in the transition annulus $[L, L+\ell] \times T^3$, the slice
metric $G(r) = f(r)^2 g_N(r)$ has intrinsic Ricci
$\operatorname{Ric}^{slice} = \operatorname{Ric}_{g_N(r)}$
(invariant under constant rescaling).

If $g_N(r)$ goes from $\operatorname{Ric} = 0$ (flat) to $\operatorname{Ric} = -2g_N$,
then at intermediate values, $\operatorname{Ric}_{g_N(r)} = -\alpha(r) g_N(r)$
with $\alpha(r)$ going from $0$ to $2$.

The tangential Ricci defect is:
$\operatorname{Ric}_{tang} + 3G = \operatorname{Ric}^{slice} - [f''/f + 2(f'/f)^2]G + 3G$
$= [-\alpha/f^2 + 3 - f''/f - 2(f'/f)^2]G$.

For the radial: $\operatorname{Ric}_{rr} + 3 = -3f''/f + 3 + (\text{shear terms})$.

The shear terms come from the $r$-dependence of $g_N$. If $g_N$ changes slowly
($|g_N'|/|g_N| = O(1/\ell)$), the shear is $O(1/\ell)$ and its contribution to
the radial Ricci is $O(1/\ell^2)$.

The intrinsic term $-\alpha/f^2$ contributes $O(1/f^2)$ to the tangential defect.
Since $f = \cosh(r) \approx e^r/2$ for large $r$, this decays exponentially.
At $r = L$: $-\alpha/f^2 \approx -8\alpha e^{-2L}$.

So the total defect in the transition annulus is:
$$\delta \sim \max\left(\frac{C}{\ell^2}, 8\alpha_{\max}e^{-2L}\right)$$

where $\alpha_{\max} = 2$ is the maximum of $\alpha(r)$ (at the Einstein end).

By taking $L$ large (deep into the collar) and $\ell$ large (long transition),
both terms can be made small. The constraint is that $L + \ell$ is bounded by
the collar length, which for a fixed graph manifold is bounded.

**For a sequence of graph manifolds** with increasingly large hyperbolic pieces
(e.g., higher-degree covers), $L$ and $\ell$ can both grow, giving $\delta \to 0$.

## 7. The critical question: does the collar actually work?

The above analysis suggests that the collar defect can be made arbitrarily small
by scaling. But there is a **crucial topological constraint**: the collar must be
glued to the hyperbolic pieces by affine diffeomorphisms of the boundary tori.

The boundary torus at the collar end is $(T^3, \cosh^2(L)g_N)$. This must be
**affinely diffeomorphic** to the boundary torus of the hyperbolic piece, which
is a flat torus $(T^3, g_0)$.

**Affine diffeomorphisms preserve the flat structure.** A non-flat torus
$(T^3, g_N)$ is NOT affinely diffeomorphic to a flat torus $(T^3, g_0)$.

**This is the fundamental obstruction.** The gluing in an extended graph manifold
uses affine diffeomorphisms of flat tori. The Einstein collar has non-flat boundary
tori. These are incompatible.

**But**: the transition annulus solves this. The collar boundary at the transition
side is non-flat, but the transition annulus deforms it to flat before the gluing.
The gluing happens at the flat boundary of the transition annulus, not at the
Einstein collar boundary.

So the structure is:
$$\text{hyperbolic piece} \to \text{flat cusp} \to \text{flat-to-non-flat transition}
\to \text{Einstein collar} \to \text{non-flat-to-flat transition} \to \text{flat cusp}
\to \text{hyperbolic piece}$$

Each transition annulus contributes defect $O(1/\ell^2 + e^{-2L})$.
For large $\ell$ and $L$, the defect is small.

**The remaining question** is whether the flat-to-non-flat transition can actually
be done with the stated defect bounds. This requires:
1. A smooth path $g_N(r)$ from flat to $\operatorname{Ric} = -2$ on $T^3$.
2. Control of the 4D Ricci tensor in terms of the 3D path and its derivatives.
3. The path must respect the $T^3$ topology throughout.

Lohkamp's theorem gives (1) and (3). The warped product formulas give (2).
The defect estimate is the scaling argument above.

**This is a concrete, potentially solvable problem.**

## 8. TTCS Correction and Revised Assessment

**The analysis above contains a critical error.** $T^3$ cannot carry
$\operatorname{Ric}_{g_N} = -2g_N$: in dimension 3, this forces constant
sectional curvature $-1$, impossible for $\pi_1 = \mathbb{Z}^3$.
Lohkamp's theorem gives $\operatorname{Ric} < 0$, not Einstein.

**Corrected mechanism.** The $T^3$ topology provides a **quantitative floor**
for the slice Ricci defect. Any metric on $T^3$ sufficiently close to
$\operatorname{Ric} = -2g$ has some sectional curvatures $\ge 0$
(quantitatively: $\|\operatorname{Ric}+2g\|_{\mathrm{op}} < 2/3$ forces all
sectional curvatures $< 0$, impossible on $T^3$).

**The scaling argument (Section 6) is also invalid.** Stretching the transition
annulus reduces $r$-derivative terms but does not remove the $O(1)$ algebraic
constraints at the $H=0$ slice:
- Radial: $\operatorname{tr}(S') + |S|^2 = 3$ requires $O(1)$ shear or $O(1)$
  shape derivative at $H=0$.
- Tangential: requires slice Ricci $\approx -2G$, violating the $T^3$ constraint.

**Revised conclusion.** The graph manifold counterexample route (Route A)
faces a fundamental obstruction from the $T^3$ slice topology. The flat-slice
barrier and the $T^3$ Einstein impossibility together suggest a **gap theorem**
(Route B) rather than a counterexample. The remaining question is whether
the transition can avoid $T^3$ foliation altogether.

## 9. Implications (corrected)

The original implication analysis was premature. The corrected picture:

1. **Flat-slice barrier** (verified): prevents $H$ reversal with flat slices.
2. **$T^3$ Einstein impossibility** (verified): prevents approximate Einstein
   slices needed for non-flat escape.
3. **Scaling argument** (invalid): does not give $\delta \to 0$.
4. **Counterexample route** (blocked): unless a non-torus-sliced transition exists.
5. **Gap theorem route** (strengthened): the combined barriers provide a new
   quantitative obstruction mechanism, complementary to the IL route.
