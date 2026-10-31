# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 38,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step38_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step38_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently inspect the SU(2)-invariant Seiberg-Witten reduction and the failed cell solvers. Determine from the exact Dirac matrix and curvature equation the correct real reduced ODE, bolt regularity/Frobenius data, and exact CH boundary solution for the perpendicular cell. Identify any sign, factor, or boundary-condition errors that explain why forward shooting blows up and solve_bvp fails. Give a corrected BVP/shooting formulation precise enough to implement; distinguish mathematical existence of the monopoles on a compact closed host from existence on the isolated exact-CH-ended cell with fixed asymptotic datum.

## Integrated Scientific Memo

# Verification memo

## 1. Exact reduced equations

The symbolic output is internally consistent. With
\[
v_i=\frac{\alpha_i}{a_i},\qquad
c=\frac{a_1^2+a_2^2+a_3^2}{2a_1a_2a_3}
-\frac12\sum_{i=1}^3\frac{\dot a_i}{a_i},
\]
the stored Dirac matrix is exactly
\[
M=cI+\frac12(v_1\tau_1+v_2\tau_2+v_3\tau_3).
\]
Thus \(\dot\Phi=M\Phi\). In the real invariant sector \(\alpha _2=0\), write
\[
\Phi=\binom uv,\qquad
\rho=u^2+v^2,\qquad
n_1=2uv,\qquad n_3=u^2-v^2.
\]
Then
\[
\begin{aligned}
\dot u&=\left(c+\frac{v_3}{2}\right)u+\frac{v_1}{2}v,\\
\dot v&=\frac{v_1}{2}u+\left(c-\frac{v_3}{2}\right)v.
\end{aligned}
\]

The symbolic identity
\[
c(F_A^+)|_{S^+}=2\sum_i\phi_i\tau_i,\qquad
\phi_i=\frac12\left(\frac{\dot\alpha_i}{a_i}
+\frac{2\alpha_i}{a_ja_k}\right)
\]
and the normalization \(\phi_i=n_i/2\) give
\[
\dot\alpha_i=a_i n_i-\frac{2a_i\alpha_i}{a_ja_k}.
\]
There is no missing factor \(2\) or curvature-sign error in the scripts.

Using
\[
n=(\rho\cos\theta,0,\rho\sin\theta)
\]
therefore gives the exact real system
\[
\boxed{
\begin{aligned}
\dot{\log\rho}
 &=2c+\frac{\alpha_1}{a_1}\cos\theta
      +\frac{\alpha_3}{a_3}\sin\theta,\\
\dot\theta
 &=\frac{\alpha_3}{a_3}\cos\theta
      -\frac{\alpha_1}{a_1}\sin\theta,\\
\dot\alpha_1
 &=a_1\rho\cos\theta-\frac{2a_1\alpha_1}{a_2a_3},\\
\dot\alpha_3
 &=a_3\rho\sin\theta-\frac{2a_3\alpha_3}{a_1a_2}.
\end{aligned}}
\tag{1}
\]
For the cell coordinate,
\[
\frac{dx}{dt}=2\sqrt G,\qquad
\frac{dy}{dx}=\frac1{2\sqrt G}\frac{dy}{dt},
\]
so the coordinate conversion in both solvers is also correct.

---

## 2. Exact complex-hyperbolic solution

On the CH region let
\[
x=\sinh^2r,\qquad
a_1=a_2=\sinh r,\qquad
a_3=\sinh r\cosh r,\qquad t=r+\text{const}.
\]
Then
\[
c=-\frac32\tanh r.
\]
The canonical solution in the conventions of the symbolic reduction is
\[
\boxed{
\rho=12,\qquad
\theta=\frac{\pi}{2},\qquad
\alpha_1=0,\qquad
\alpha_3=3\sinh^2r=3x.}
\tag{2}
\]
Indeed \(v_3=3\tanh r\), so \(2c+v_3=0\), while
\[
\frac{\dot\alpha_3}{a_3}=6,\qquad
\frac{2\alpha_3}{a_1a_2}=6,
\]
giving \(n_3=12\).

Consequently, exact equality to the canonical solution at a finite join \(x=X\) means all four conditions
\[
\boxed{
\rho(X)=12,\quad \theta(X)=\frac{\pi}{2},\quad
\alpha_1(X)=0,\quad \alpha_3(X)=3X.}
\tag{3}
\]
The two conditions used in the scripts,
\(\rho=12\) and \(\theta=\pi/2\), do **not** impose canonical CH continuation.

There is also an exact obstruction to finite matching for charged bolt sectors. The plane
\[
\theta=\frac{\pi}{2},\qquad \alpha_1=0
\]
is invariant under (1). By uniqueness, backward evolution from the complete datum (3) remains in that plane and therefore reaches bolt charge \(\alpha_1(0)=0\), not \(\pm1\). Hence no real invariant charged solution can agree exactly with (2) from a finite join onward.

This does not rule out convergence to (2) only as \(r\to\infty\).

---

## 3. Bolt regularity and Frobenius data

Let the first orbit direction collapse at \(t=0\), with
\[
a_1=t+\kappa t^3+O(t^5),\qquad
a_2=b+\mu t^2+O(t^4),\qquad
a_3=b+\nu t^2+O(t^4),
\tag{4}
\]
where \(b=\sqrt{x_0}\) for the supplied cell. Then
\[
c=\frac1{2t}
+\left(\frac1{2b^2}-2\kappa-\frac{\mu+\nu}{b}\right)t
+O(t^3).
\]

For bolt charge
\[
\alpha_1(0)=\sigma,\qquad \sigma=\pm1,
\]
define
\[
\theta_\sigma=\frac{1+\sigma}{2}\pi
\quad(\theta_+=\pi,\ \theta_-=0).
\]
The regular nonzero-spinor family has two free real parameters
\((\rho_0,\beta)\), and
\[
\boxed{
\begin{aligned}
\rho(t)&=\rho_0\left(1+R t^2+O(t^4)\right),\\
\theta(t)&=\theta_\sigma-\sigma\beta t+D t^3+O(t^5),\\
\alpha_1(t)&=
\sigma\left[1-\left(\frac{\rho_0}{2}+\frac1{b^2}\right)t^2\right]
+O(t^4),\\
\alpha_3(t)&=\frac{b\rho_0\beta}{4}t^2+O(t^4),
\end{aligned}}
\tag{5}
\]
where
\[
R=\frac1{b^2}-\frac32\kappa-\frac{\mu+\nu}{b}
+\frac{\rho_0+\beta^2}{4},
\]
and
\[
D=\sigma\left[
\frac{\beta^3}{12}
+\beta\left(\frac{\rho_0}{8}+\frac1{2b^2}+\frac{\kappa}{2}\right)
\right].
\]

Thus
\[
n_1\to-\sigma\rho_0,\qquad
n_3=\rho_0\beta t+O(t^3).
\]
The leading data in `sw_perp_cell_pair.py`, including the sign of \(\alpha_1\) and the coefficient \(1/4\) in \(\alpha_3\), are correct.

A subtle point relevant to collocation is that the limiting statements
\[
\alpha_1(0)=\sigma,\qquad \alpha_3(0)=0
\]
alone are not safe boundary equations when the computation begins at \(t=\varepsilon>0\). One must impose the Frobenius values (5), or use desingularized variables. Otherwise one either suppresses legitimate regular modes or permits the singular homogeneous mode
\[
\alpha_3\sim Ct^{-2}.
\]

A robust spinor parametrization is
\[
P=\frac{u-\sigma v}{\sqrt2},\qquad
Q=\frac{u+\sigma v}{\sqrt2},
\]
for which
\[
P=P_0+O(t^2),\qquad
Q=\frac{\beta P_0}{2}t+O(t^3),\qquad P_0^2=\rho_0.
\]
The regular quantities are
\[
P,\qquad Q/t,\qquad
(\alpha_1-\sigma)/t^2,\qquad \alpha_3/t^2.
\]
These avoid both the angular singularity at \(\rho=0\) and the logarithmic exclusion of the zero-spinor branch.

The mirror symmetry is exact:
\[
(\rho,\theta,\alpha_1,\alpha_3;\sigma)
\mapsto
(\rho,\pi-\theta,-\alpha_1,\alpha_3;-\sigma).
\tag{6}
\]

---

## 4. Why the existing solvers fail

### Forward shooter

Its ODE and bolt seed are essentially correct. Its difficulties are:

1. **Wrong finite terminal interpretation.** It enforces only
   \[
   \rho(R)=12,\qquad \theta(R)=\pi/2.
   \]
   At such a crossing,
   \[
   (\log\rho)'=
   \frac{\alpha_3-3\sinh^2R}{\sinh R\cosh R},
   \qquad
   \theta'=-\frac{\alpha_1}{\sinh R},
   \]
   so the trajectory is canonical only if the missing gauge variables also have their canonical values.

2. **Exponential saddle conditioning.** Define
   \[
   L=\log(\rho/12),\qquad \delta=\theta-\pi/2,
   \]
   \[
   \mathcal A=\frac{\alpha_1}{\sinh r},\qquad
   \mathcal B=\frac{\alpha_3-3\sinh^2r}{\sinh r\cosh r}.
   \]
   The exact CH equations are
   \[
   \begin{aligned}
   L'&=-3\tanh r+\mathcal A\cos\theta
        +(3\tanh r+\mathcal B)\sin\theta,\\
   \delta'&=(3\tanh r+\mathcal B)\cos\theta
        -\mathcal A\sin\theta,\\
   \mathcal A'&=\rho\cos\theta-
     \left(\coth r+\frac{2}{\sinh r\cosh r}\right)\mathcal A,\\
   \mathcal B'&=\rho\sin\theta-12
     -(3\coth r+\tanh r)\mathcal B.
   \end{aligned}
   \tag{7}
   \]
   Linearization at the canonical solution has asymptotic exponents
   \[
   2,\ -6,\qquad -2+\sqrt{13},\ -2-\sqrt{13}.
   \]
   Hence two modes grow outward like \(e^{2r}\) and
   \(e^{(\sqrt{13}-2)r}\). At \(r=6.5\), small bolt-parameter errors are amplified by roughly \(4\times10^5\) and \(3\times10^4\). This explains runaway \(\rho=e^{\log\rho}\), LSODA failure, and the flat fallback residual \([10^3,10^3]\).

3. The optimizer should use \(\lambda=\log\rho_0\), not \(\rho_0\), to prevent trial values \(\rho_0\le0\).

### `solve_bvp` version

Its endpoint rows do not select the correct local manifolds.

* At \(u=10^{-7}>0\), it imposes exactly
  \[
  \theta=\theta_\sigma,\qquad \alpha_1=\sigma.
  \]
  But a regular solution there has the nonzero corrections from (5):
  \[
  \theta-\theta_\sigma=-\sigma\beta t+O(t^3),\qquad
  \alpha_1-\sigma=
  -\sigma\left(\frac{\rho_0}{2}+\frac1{x_0}\right)t^2+O(t^4).
  \]
  Exact limiting values at a positive cutoff suppress the \(\beta\)-mode or force a numerical boundary layer.

* No Frobenius condition is imposed on \(\alpha_3\), so the nonsmooth \(t^{-2}\) homogeneous mode is not excluded.

* At \(X\), only \((\rho,\theta)\) are constrained. These are neither the four exact finite CH data nor the two stable-manifold conditions for asymptotic convergence.

* Interpolating \(a_1\sim t\sim\sqrt{x-x_0}\) directly by a cubic spline in \(u\) is poorly conditioned. Tabulate smooth bolt variables such as \(a_1/t\), \(a_2\), and \(a_3\) against \(s=t^2\).

* `exp(clip(logrho))` changes the ODE once clipping activates and cannot be used in a verification computation.

---

## 5. Correct asymptotic boundary conditions

Linearizing (7) gives
\[
L'=\mathcal B,\qquad
\mathcal B'=12L-(3\coth r+\tanh r)\mathcal B,
\]
\[
\delta'=-3\tanh r\,\delta-\mathcal A,\qquad
\mathcal A'=-12\delta-
\left(\coth r+\frac{2}{\sinh r\cosh r}\right)\mathcal A.
\]
The decaying eigendirections satisfy asymptotically
\[
\boxed{
\mathcal B=-6L+o(L),\qquad
\mathcal A=(\sqrt{13}-1)\delta+o(\delta).}
\tag{8}
\]
Thus a practical far-boundary condition at \(r=R\) is
\[
\boxed{
\mathcal B(R)+6L(R)=0,\qquad
\mathcal A(R)-(\sqrt{13}-1)\delta(R)=0.}
\tag{9}
\]

A more accurate finite-\(R\) linear stable projection uses
\[
\mathcal B=m(r)L,\qquad \mathcal A=k(r)\delta,
\]
where
\[
\begin{aligned}
m'&=12-(3\coth r+\tanh r)m-m^2,
& m(\infty)&=-6,\\
k'&=k^2+
\left(3\tanh r-\coth r-\frac{2}{\sinh r\cosh r}\right)k-12,
& k(\infty)&=\sqrt{13}-1.
\end{aligned}
\tag{10}
\]
Integrate these Riccati equations backward from a large radius. If the solution is not already in the linear neighborhood at \(R\), construct the full nonlinear two-dimensional CH stable manifold by backward integration of (7) from small amplitudes in its two decaying modes.

---

## 6. Implementable corrected formulations

### A. Collocation with asymptotic CH convergence

Use four ODE variables, preferably desingularized near the bolt. Introduce two unknown parameters
\[
p=(\lambda,\beta),\qquad \rho_0=e^\lambda.
\]
Start at \(t=\varepsilon\), not at the singular orbit, and impose the four Frobenius equations
\[
y(\varepsilon)=y_{\rm bolt}(\varepsilon;\lambda,\beta)
\]
from (5). At \(r=R\), impose the two stable-manifold equations (9), or their Riccati-refined form (10).

This is correctly counted for `solve_bvp`:

* four first-order equations;
* two unknown parameters;
* six scalar boundary equations.

Do not impose exact limiting values \(\theta=\theta_\sigma\) and \(\alpha_1=\sigma\) at a positive cutoff.

### B. Multiple shooting

This is likely better conditioned:

1. propagate the two-parameter bolt-regular family outward from \(t=\varepsilon\);
2. propagate a two-parameter family on the CH stable manifold inward from \(r=R\);
3. require equality of all four state variables at one or more intermediate knots.

Multiple shooting limits the amplification from the positive and negative CH exponents and avoids trying to resolve decaying traces of order \(e^{-6R}\) in one integration.

### C. Exact canonical datum at a finite join

If the requirement is exact equality to the canonical CH monopole from \(X\) onward, impose all four values (3). This is not the same BVP as asymptotic convergence. Together with charged bolt regularity it is overdetermined, and in fact the invariant-plane argument proves impossibility for \(\sigma=\pm1\) within this reduction.

---

## 7. What existence is and is not established

Existence of a Seiberg–Witten monopole on a compact closed host does not imply existence of the isolated invariant cell problem with prescribed CH asymptotics.

On the closed host:

* the global solution is selected by the closed elliptic problem and the relevant spin\(^c\), chamber, and perturbation data;
* its trace at the edge of this cell is determined by the complementary region;
* that trace need not be canonical CH data, real, or SU(2)-invariant;
* averaging a nonlinear monopole does not generally produce an invariant monopole.

On the isolated exact-CH-ended cell, the invariant asymptotic problem asks whether the two-dimensional bolt-regular manifold intersects the two-dimensional CH stable manifold in the four-dimensional reduced phase space. The supplied failed runs neither establish nor refute that intersection because they imposed the wrong terminal subspace and, in the BVP version, incorrect cutoff bolt conditions.

Finally, the optimized cell is not exactly scalar \(-24\): the record reports scalar-deviation cost \(7.2975869\times10^{-6}\). Therefore the diagnostic identity
\[
\int|\nabla\Phi|^2=\int\frac{\rho(12-\rho)}2
\]
is not exact on the whole cell. The correct integrated Weitzenböck term is
\[
\boxed{
\int|\nabla\Phi|^2
=\int\left(-\frac{s_g\rho}{4}-\frac{\rho^2}{2}\right).}
\]
This does not change the reduced ODE, but it does change the downstream kinetic-energy comparisons.