# Step 70: critical identity, elliptic correction, and peripheral algebra

Session: S0910A03. Agent2/Constructor, Explore.
**Supersedes** the elliptic/hyperbolic claim in step70_mixed_boundary_formulation.md.

## 1. CORRECTION: the T²-invariant system is ELLIPTIC

From the SymPy computation of E_{22}/g_{22} = 0:
$$
b_{tt} + e^{-2a} b_{\theta\theta} = 3 - (a_t+c_t)b_t - b_t^2
  + e^{-2a}(a_\theta b_\theta - b_\theta^2 - b_\theta c_\theta)
$$

Both second derivatives have the **same sign** on the left: this is a
**Laplacian**, not a wave operator. The T²-invariant Gaussian-gauge system
is **elliptic**, not hyperbolic.

**Consequences:**
- The IVP (Cauchy problem from t=0 with S=0) is Hadamard ill-posed:
  this explains the finite-time Fourier blow-up in the Step 69 Galerkin runs,
  which are elliptic Cauchy instability artifacts, not geometric singularities.
- The BVP with Dirichlet at t=0 and t=R is well-posed for the elliptic system.
- The DeTurck formulation makes the FULL 5-component system elliptic,
  with a properly posed Dirichlet BVP.

## 2. CRITICAL IDENTITY: H < 3 at all finite times

**Theorem.** For any exact Einstein metric $\operatorname{Ric}=-3g$ on
$[0,R]\times T^3$ with totally geodesic center ($S(0)=0$), the mean
curvature satisfies $H(t,\theta) < 3$ for all $t \in (0,R]$.

**Proof.** Set $B = S - I$, $b = H - 3 = \operatorname{tr}B$.
The normal-normal Einstein equation $E_{00}=0$ gives
$$
H' + |S|^2 = 3.
$$
Expanding $|S|^2 = |I+B|^2 = 3 + 2b + |B|^2$:
$$
\dot b + 2b + |B|^2 = 0. \tag{$*$}
$$
This is a first-order linear ODE for $b$ with forcing $-|B|^2 \le 0$.
Multiplying by $e^{2t}$:
$$
\frac{d}{dt}\bigl(e^{2t}b\bigr) = -e^{2t}|B|^2.
$$
Integrating from 0 to $t$, with $b(0) = H(0)-3 = -3$:
$$
\boxed{
e^{2t}b(t,\theta) = -3 - \int_0^t e^{2s}|B(s,\theta)|^2\,ds
}
$$

Since the integral is nonnegative: $e^{2t}b(t) \le -3 < 0$, so $b(t) < 0$,
i.e., **$H(t) < 3$ for all $t > 0$**.

More precisely: $H(t) \le 3 - 3e^{-2t}$.

**Verification with the isotropic case:** $a=b=c=f(t)$, $S=f'I$, $H=3f'$.
$f'' = 3(1-f'^2)$ with $f'(0)=0$ gives $f'=\tanh(\sqrt{3}\,t)$,
$H = 3\tanh(\sqrt{3}\,t) \to 3$ as $t\to\infty$, but $H < 3$ always. ✓

## 3. Consequences for PE conformal infinity

If the extension exists to $t=\infty$ with Poincaré–Einstein expansion
$h_t = e^{-2t}\gamma_t \to h_0$ (conformal infinity), then taking $t\to\infty$
in the boxed identity:
$$
\frac14 R_{h_0}(\theta) = -3 - \int_0^\infty e^{2s}|B(s,\theta)|^2\,ds < -3.
$$
Therefore $R_{h_0} < -12$ pointwise. In particular:
- **Flat conformal infinity ($R_{h_0}=0$) is impossible** for reflection cores.
- The standard AH cusp has flat conformal boundary → cannot arise from
  a reflection center.

Li–Liu solutions have NO totally geodesic $T^3$ slice and are not
reflection-symmetric, so they do not contradict this.

## 4. Necessary logarithmic length for approximate cores

For $\|E\|_{\mathrm{op}} \le \delta$ (approximate Einstein):
$$
\dot b + 2b + |B|^2 = -E_{00}, \qquad |E_{00}| \le \delta.
$$
Integrating:
$$
e^{2R}b(R) = -3 - \int_0^R e^{2s}|B|^2\,ds + \int_0^R e^{2s}E_{00}\,ds.
$$
For $b(R) = 0$ (exact cusp data at $t=R$):
$$
3 + \int_0^R e^{2s}|B|^2\,ds \le \frac{\delta}{2}(e^{2R}-1).
$$
Therefore:
$$
\boxed{R \ge \frac12\log\!\left(1+\frac{6}{\delta}\right)
\sim \frac12\log\frac{6}{\delta}.}
$$

This is **necessary** for ANY approximate construction, regardless of ansatz.
It matches the manuscript's finite-boundary second variation bound in scaling.

**The gap:** this bound is necessary but **existence of such approximate cores
is not yet established**. The defect $E_{00}$ must be systematically negative
(compensating the initial $-3$ and shear energy), not random.

## 5. Peripheral algebraic reduction (TTCS-verified)

**Theorem (peripheral covers).** Let $P$ be a one-cusped orientable
hyperbolic 4-manifold piece with cusp lattice $\Lambda \cong \mathbb{Z}^3$.
Let $\phi:\pi_1(P)\to\mathbb{Z}$ be a primitive character with
$\phi|_\Lambda = d\ell$ ($\ell$ primitive, $d \ge 1$).

For every $N$ with $(d,N) = 1$: the cyclic mod-$N$ cover $P_N$ has
**exactly one cusp**, with peripheral lattice
$$
\Lambda_N = \ker(\ell \bmod N) = \langle Nf_1, e_2, e_3 \rangle
$$
of type $(N,1,1)$ in the basis $\{f_1, e_2, e_3\}$ adapted to $\ell$.

**Proof sketch:** $(d,N)=1$ makes $q_N|_\Lambda$ surjective onto $\mathbb{Z}/N$,
so the cusp inverse image is connected (one cusp). The sublattice is
$\{v \in \Lambda : d\ell(v) \equiv 0 \pmod{N}\}$, and since $d$ is invertible
mod $N$, this equals $\ker(\ell \bmod N)$. ✓

**When does such $\phi$ exist?** The necessary and sufficient condition is:
$$
\boxed{\operatorname{rank}_\mathbb{Q}\operatorname{im}
\bigl(H_1(T^3;\mathbb{Q})\to H_1(\bar M;\mathbb{Q})\bigr) > 0
\quad\Longleftrightarrow\quad b_1(\bar M) > b_3(\bar M).}
$$

This follows from the long exact sequence and Poincaré–Lefschetz duality
$H_1(\bar M, T^3) \cong H^3(\bar M) \cong H_3(\bar M)$, giving
$\operatorname{rank}\operatorname{im}(i_*) = b_1 - b_3$.

**For Slavich's manifold** with $H_1 \cong \mathbb{Z}\oplus\mathbb{Z}_3$:
$b_1 = 1$, so the criterion reduces to $b_3 = 0$. This needs explicit
verification from the manifold's presentation (Euler characteristic $\chi$
or the abelianized peripheral generators in $\mathbb{Z}\oplus\mathbb{Z}_3$).

## 6. Li–Liu coordinate slices are far from totally geodesic

For Li–Liu Type-I metrics with $S^1$-invariant Toda data, TTCS showed:
$$
|S|^2 \ge \frac{8}{3}
$$
on every coordinate-level hypersurface. Therefore:
- Small metric perturbations cannot produce a nearly-geodesic $T^3$
- Near-geodesic $T^3$ requires **finite-amplitude ASD breaking**
  or **strongly tilted graph slices**

The deformation problem is: find a non-ASD Einstein metric near the Li–Liu
family with a nearly-geodesic slice. This requires solving the mixed-end
Lichnerowicz equation and checking whether the kernel/cokernel admits
$DW^+(k) \ne 0$ modes.

## 7. Updated route assessment

**What the critical identity establishes:**
- Exact reflection cores approach the cusp exponentially: $3-H \sim 3e^{-2t}$
- They NEVER reach the cusp at finite distance
- Matching at finite $R$ with a cusp piece always has defect $\ge 3e^{-2R}$
- For defect $\delta$: the core needs length $R \ge (1/2)\log(6/\delta)$

**What remains open:**
- Does the exact Koiso extension survive to $t=\infty$ for ANY scalar-minus-six
  $T^3$ metric? (The numerical blow-up is elliptic Cauchy artifact, not proof
  of geometric singularity.)
- Is the $R \sim (1/2)\log(1/\delta)$ bound achievable by an approximate
  construction?
- Does the Slavich manifold satisfy $b_3 = 0$?
- Can the Li–Liu family be deformed to acquire a nearly-geodesic slice?

**The graph manifold counterexample requires ALL of:**
1. An Einstein core (exact or approximate) reaching expanding cusp state
2. Peripheral covers of type $(N,1,1)$ in an Einstein-free graph class
3. Compatible affine gluing
4. The same construction for the POSITIVE branch (or a different obstruction)

The critical identity is a sharp structural result, not a no-go: it shows
the exact scaling and the asymptotic rate, and reveals that the construction
must use the exponential approach rather than finite-time arrival.
