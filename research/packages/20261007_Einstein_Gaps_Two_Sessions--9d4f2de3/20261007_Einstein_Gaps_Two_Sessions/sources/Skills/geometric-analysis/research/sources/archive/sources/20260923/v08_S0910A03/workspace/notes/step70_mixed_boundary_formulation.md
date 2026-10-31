# Step 70: T²-invariant Einstein mixed-boundary formulation

Session: S0910A03. Agent2/Constructor, Explore.

## 1. The T²-invariant Einstein equations

For the metric
$$
g = dt^2 + e^{2a(t,\theta)}\,d\theta^2 + e^{2b(t,\theta)}\,dx^2 + e^{2c(t,\theta)}\,dy^2
$$
on $[0,R]\times T^3$ (with $\theta,x,y$ periodic), the exact Ricci components
(verified by SymPy, `scripts/step70_ricci_T2inv.py`) are:

**Normal–normal:**
$$E_{00} = 3 - \ddot a - \ddot b - \ddot c - \dot a^2 - \dot b^2 - \dot c^2$$

**Normal–tangential:**
$$E_{01} = \dot a(b'+c') - \dot b\,b' - \dot c\,c' - \dot b' - \dot c'$$

**Tangential (orthonormal):** writing $\alpha = e^{-2a}$:
$$\hat E_{11} = 3 - \ddot a - \dot a\dot H + \alpha(a'b'+a'c'-{b'}^2-b''-{c'}^2-c'')$$
$$\hat E_{22} = 3 - \ddot b - \dot b\dot H + \alpha(a'b'-{b'}^2-b'c'-b'')$$
$$\hat E_{33} = 3 - \ddot c - \dot c\dot H + \alpha(a'c'-b'c'-{c'}^2-c'')$$

where $H = \dot a+\dot b+\dot c$, dots are $\partial_t$, primes are $\partial_\theta$.

**Structure of the principal part:**
The highest derivatives in each equation involve
$\ddot a - \alpha a''$, $\ddot b - \alpha b''$, $\ddot c - \alpha c''$.
Since $\alpha = e^{-2a} > 0$, each is a **wave operator** $\Box_{(t,\theta)}$, not
a Laplacian. The Gaussian-gauge system is **hyperbolic** in $(t,\theta)$, not elliptic.

**Consequence:** A boundary value problem with Dirichlet data at $t=0$ and $t=R$
is well-posed (analogous to the fixed-endpoint string problem), but it is NOT
an elliptic BVP. To make the full Einstein system elliptic, we need the DeTurck
gauge, which uses all 5 independent metric components.

## 2. Verification checks

1. **Round cusp** $a=b=c=t$: all five $E_{\mu\nu}=0$ exactly. ✓
2. **Anisotropic cusp** $a=0, b=t, c=t$: $E_{00}=1\ne0$. Not Einstein. ✓
   (A cusp with one bounded direction is not Einstein in dimension 4.)
3. **Koiso center** at $t=0$: $\dot a=\dot b=\dot c=0$,
   $(a,b,c)$ from the Yamabe solve. $E_{00} = 3 - \ddot a - \ddot b - \ddot c$,
   and by the Hamiltonian constraint $\ddot a + \ddot b + \ddot c = 3$
   (trace of the initial acceleration). ✓

## 3. BVP formulations

### 3a. Exact Einstein BVP (Gaussian gauge, hyperbolic)

Use the 3 evolution equations $\hat E_{11}=\hat E_{22}=\hat E_{33}=0$ as the
PDEs. Specify Dirichlet data:
- At $t=0$: $(a,b,c) = (a_0,b_0,c_0)$ from the Koiso center $q_N$
- At $t=R$: $(a,b,c) = (a_R,b_R,c_R)$ target expanding state

This is a well-posed BVP for 3 coupled wave equations on $[0,R]\times S^1$.
The constraint equations $E_{00}=E_{01}=0$ are propagated by the contracted
Bianchi identity, provided the boundary data satisfy the constraints.

**Compatibility:** the initial data $(q_N, S=0)$ automatically satisfy the
constraints at $t=0$. The target data at $t=R$ must also satisfy the constraints
there. This reduces the target parameter space.

**Reflection condition:** for a totally geodesic center, $\dot a(0)=\dot b(0)=\dot c(0)=0$.
The BVP determines the initial velocity; the reflection condition is an additional
3-parameter constraint. Whether it is satisfiable is the central existence question.

### 3b. Exact Einstein BVP (DeTurck gauge, elliptic)

Write the general T²-invariant metric as
$$
g = g_{tt}\,dt^2 + 2g_{t\theta}\,dt\,d\theta + g_{\theta\theta}\,d\theta^2
  + g_{xx}\,dx^2 + g_{yy}\,dy^2
$$
with 5 unknowns $(g_{tt}, g_{t\theta}, g_{\theta\theta}, g_{xx}, g_{yy})$
depending on $(t,\theta)$.

Choose a reference metric $\bar g$ (smooth interpolation between Koiso and cusp).
The Einstein-DeTurck system $\operatorname{Ric}(g)+3g+\mathcal L_V g = 0$ has
principal symbol $-\frac12 g^{\alpha\beta}\xi_\alpha\xi_\beta \cdot \mathrm{Id}$.
Since $g$ is Riemannian, this is **strictly elliptic**.

BVP: Dirichlet at both ends for all 5 components.
- $t=0$: from Koiso center (using the gauge determined by $\bar g$)
- $t=R$: from target cusp (using the gauge determined by $\bar g$)

This is a well-posed elliptic BVP. Solutions satisfy $\operatorname{Ric}(g)+3g=0$
provided the DeTurck vector field vanishes (which requires checking).

### 3c. Approximate core (optimization)

For any smooth T²-invariant diagonal metric on $[0,R]\times T^3$ with given
boundary data, define:
$$
\delta_* = \inf_{g} \sup_{(t,\theta)} \sqrt{E_{00}^2 + E_{01}^2 + \hat E_{11}^2
  + \hat E_{22}^2 + \hat E_{33}^2}
$$

For the graph manifold counterexample, we need $\delta_*\to0$ as some parameter
$\to\infty$. The approximate core problem asks: what is $\delta_*$ for given
boundary data and domain length $R$?

**Key Strategist insight:** exact continuation failure does not exclude approximate
cores. The exact Koiso solution may blow up at finite $t$, but a controlled
defect $\delta>0$ could extend the valid domain significantly.

## 4. The central obstruction: anisotropic initial acceleration

For EVERY scalar-minus-six metric $q$ on $T^3$:
$$
S'(0) = \operatorname{Ric}_q^\sharp + 3I
$$
has a negative eigenvalue. This is because $P_k = -K_{ij}$ for the complementary
sectional plane, and $T^3$ cannot have all-negative sectional curvature
(Preissmann's theorem applies to sectional, not Ricci).

Numerical verification (step69_center_amplitude_sweep.py): for all tested
amplitudes $A = 0.03, \ldots, 4.0$, $P_{\min} < 0$.

This means: the reflection core always starts with mixed expansion/contraction.
A successful core must use **nonlinear spatial redistribution** to overcome
the initially contracting direction.

## 5. The Li-Liu parallel: exact non-reflection compensation

Li-Liu Theorem 1.3 constructs complete $\operatorname{Ric}=-3h$ metrics on
$(0,\infty)\times T^3$ with one PE end and one AH cusp, for each quotient
metric on $T^2$. Their Type-I form:
$$
h = \xi^{-2}(W\,d\xi^2 + W^{-1}\eta^2 + We^v g_{T^2}),\qquad
W = 1-\tfrac12\xi v_\xi,
$$
with Toda equation $(e^v)_{\xi\xi}+\Delta_{T^2}v=0$.

For T²-invariant ($v=v(\xi,\theta)$), this reduces to a 2D elliptic equation!
The Toda equation with $v=v(\xi,\theta)$ is:
$$
(e^v)_{\xi\xi} + (e^v)_{\theta\theta} = 0
$$
which is the Laplace equation for $e^v$ on the $(\xi,\theta)$ half-plane.

**Connection to our problem:** the Li-Liu solution demonstrates exact global
compensation from anisotropic initial data. It does NOT have a totally geodesic
T³ (being ASD), but its equations and asymptotics provide the correct variables
and endpoint matching for a deformation analysis.

## 6. Quotient compatibility (Strategist point)

The $q_N$ anisotropic quotient preserves T² symmetry: the collapsing $x,y$
directions are flat and translation-invariant. The core equations are therefore
N-independent in the T²-invariant class.

**If we break T² symmetry** (allow $x,y$-dependent perturbations of the core),
then:
- $\partial_x^2$ acts on functions with period $1/N$, picking up a factor $N^2$
- The Ricci tensor gets N-dependent terms
- The construction becomes N-dependent, potentially invalidating the quotient

**Conclusion:** the core search should remain within the T²-invariant class
unless the N-dependence can be quantitatively controlled. Seek compensation
within the quotient-compatible T²-invariant Einstein equations.

## 7. Gaussian-gauge BVP in Fourier space

Fourier-expand in $\theta$: $a(t,\theta) = \sum_k \hat a_k(t) e^{ik\theta}$ etc.
With $M$ modes kept, the system becomes $3(2M+1)$ coupled second-order ODEs in $t$.

BVP: specify $\hat a_k(0), \hat b_k(0), \hat c_k(0)$ and
$\hat a_k(R), \hat b_k(R), \hat c_k(R)$ for all $|k|\le M$.

This is $6(2M+1)$ conditions for $3(2M+1)$ second-order equations → correct count.
Solvable by standard BVP algorithms (scipy.solve_bvp or collocation).

For the reflection condition: additionally require $\dot a_k(0)=\dot b_k(0)=\dot c_k(0)=0$.
This is $3(2M+1)$ additional conditions → overdetermined. The reflection condition
should be enforced by symmetry: solve on $[0,R]$ with Dirichlet at both ends,
then double to $[-R,R]$ by reflection.

**Numerical plan:** Solve the BVP with target data at $t=R$ equal to the round
cusp $(a,b,c) = (R,R,R)$, starting from Koiso center at $t=0$. Vary $R$ and
measure the resulting Einstein defect (especially the constraint equations which
are not imposed as PDEs).

## 8. Comparison with Chapter 6 mechanism

The surface bundle construction (20260912.tex, Ch. 6) keeps the fiber metric
exactly hyperbolic while collapsing a base circle. The shape operator is:
$$
S = \frac12\begin{pmatrix}0&v\\v&0\end{pmatrix},\qquad v = Qz'
$$
The Ricci defect comes entirely from the time-dependent shape operator, not
from intrinsic fiber curvature. The fiber stays at exact Einstein scale throughout.

For our torus construction:
- The Koiso center has curvature at Einstein scale (scalar = -6)
- But no obvious split into "exactly Einstein fiber" + "collapsing direction"
- The intrinsic torus curvature contributes to the Ricci defect during transition

**Transferable principle:** instead of interpolating the curvature itself,
interpolate the *extrinsic* geometry (shape operator) while keeping the intrinsic
geometry at a controlled Einstein scale. In our case: hold the $\theta$-metric
(the curved direction) at the Koiso scale while the $x,y$ directions enter
the expanding regime.

This suggests a different ansatz for the transition: not $a\to t, b\to t, c\to t$
(all expanding), but $a\to\text{bounded}, b\to t, c\to t$ (only the flat
directions expand). But the SymPy computation shows this is NOT Einstein!
(The verification $a=0,b=t,c=t$ has nonzero defect.)

The resolution: the bounded direction $a$ must slowly decrease to compensate.
This is a specific prediction for the BVP target data.

## Summary of concrete remaining work

1. **Peripheral algebra**: verify that specific one-cusped hyperbolic 4-manifold
   pieces have nonzero peripheral image in $H_1$. If so, the $(N,1,1)$ covers
   exist by the Strategist's reduction.

2. **BVP solver**: implement the Gaussian-gauge Fourier BVP with target data
   at $t=R$, varying $R$ and the target. Measure constraint violation and
   determine the shape operator at $t=0$.

3. **Approximate core optimization**: minimize the Einstein defect over smooth
   metrics with given boundary conditions, allowing small defect.

4. **Li-Liu deformation**: analyze whether a non-ASD deformation of the
   Li-Liu solution can accommodate a nearly-geodesic T³ slice.
