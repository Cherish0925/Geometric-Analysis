# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/bianchi_sw_reduction.py",
    "Sessions/S1003A02/workspace/data/bianchi_sw_reduction.json",
    "Sessions/S1003A02/workspace/scripts/sw_perp_cell_pair.py",
    "Sessions/S1003A02/workspace/scripts/sw_perp_cell_pair_v2.py",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py",
    "Sessions/S1003A01/workspace/scripts/perp_dual_cost.py",
    "Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json"
  ]
}
```

## Task

Independently inspect the SU(2)-invariant Seiberg-Witten reduction and the failed cell solvers. Determine from the exact Dirac matrix and curvature equation the correct real reduced ODE, bolt regularity/Frobenius data, and exact CH boundary solution for the perpendicular cell. Identify any sign, factor, or boundary-condition errors that explain why forward shooting blows up and solve_bvp fails. Give a corrected BVP/shooting formulation precise enough to implement; distinguish mathematical existence of the monopoles on a compact closed host from existence on the isolated exact-CH-ended cell with fixed asymptotic datum.

## Output

# Scientific memo

## 1. Exact real reduction from the supplied Dirac matrix

The matrix stored in `bianchi_sw_reduction.json` simplifies exactly to
\[
\dot\Phi=
\left(cI+\frac12\sum_{i=1}^3v_i\tau_i\right)\Phi,
\qquad
v_i=\frac{\alpha_i}{a_i},
\]
where a dot denotes \(d/dt\) and
\[
c=
\frac{a_1^2+a_2^2+a_3^2}{2a_1a_2a_3}
-\frac12\left(
\frac{\dot a_1}{a_1}
+\frac{\dot a_2}{a_2}
+\frac{\dot a_3}{a_3}
\right).
\]
Indeed, the two diagonal entries in the JSON are \(c\pm v_3/2\), while the off-diagonal entries are
\[
\frac12(v_1-iv_2),\qquad \frac12(v_1+iv_2).
\]

For the real invariant sector \(\alpha_2=0\), write
\[
\Phi=\binom{u}{v}\in\mathbb R^2,\qquad
\rho=u^2+v^2,\qquad
n_1=2uv,\qquad n_3=u^2-v^2.
\]
Then the exact component equations are
\[
\begin{aligned}
\dot u&=\left(c+\frac{v_3}{2}\right)u+\frac{v_1}{2}v,\\
\dot v&=\frac{v_1}{2}u+\left(c-\frac{v_3}{2}\right)v,\\
\dot\alpha_1&=a_1(2uv)-\frac{2a_1\alpha_1}{a_2a_3},\\
\dot\alpha_3&=a_3(u^2-v^2)-\frac{2a_3\alpha_3}{a_1a_2}.
\end{aligned} \tag{1}
\]

The curvature factor is also fixed by the symbolic output
`cF_plus_minus_2phitau = 0`:
\[
\phi_i=\frac12\left(\frac{\dot\alpha_i}{a_i}
+\frac{2\alpha_i}{a_ja_k}\right)=\frac{n_i}{2}.
\]
Consequently
\[
\frac{\dot\alpha_i}{a_i}+\frac{2\alpha_i}{a_ja_k}=n_i,
\]
which is exactly the last two equations in (1). There is no missing factor of \(2\) in `sw_perp_cell_pair.py`.

Using
\[
n=(\rho\cos\theta,0,\rho\sin\theta)
\]
gives
\[
\boxed{
\begin{aligned}
\dot{\log\rho}
   &=2c+v_1\cos\theta+v_3\sin\theta,\\
\dot\theta
   &=v_3\cos\theta-v_1\sin\theta,\\
\dot\alpha_1
   &=a_1\rho\cos\theta-\frac{2a_1\alpha_1}{a_2a_3},\\
\dot\alpha_3
   &=a_3\rho\sin\theta-\frac{2a_3\alpha_3}{a_1a_2}.
\end{aligned}} \tag{2}
\]
Thus the signs in the real ODE used by the first program agree with the exact Dirac matrix.

The conversion to the cell coordinate \(x\),
\[
\frac{dx}{dt}=2\sqrt G,\qquad
\frac{d}{dx}=\frac1{2\sqrt G}\frac{d}{dt},
\]
is also correct in the supplied scripts.

---

## 2. Exact complex-hyperbolic solution

On the exact CH part, with
\[
x=\sinh^2r,\qquad
a_1=a_2=\sinh r=:s,\qquad
a_3=\sinh r\cosh r=:sc,
\]
one has \(t=r+\text{constant}\) and
\[
c=-\frac32\tanh r.
\]

The canonical solution in the conventions of the symbolic reduction is
\[
\boxed{
\rho=12,\qquad
\theta=\frac{\pi}{2},\qquad
\alpha_1=0,\qquad
\alpha_3=3\sinh^2r=3x.} \tag{3}
\]
Equivalently,
\[
\Phi=\binom{\sqrt{12}}0,\qquad
A=3i\sinh^2r\,\sigma_3.
\]

Direct substitution fixes all signs and factors:

* \(v_3=3\tanh r\), so
  \[
  2c+v_3=-3\tanh r+3\tanh r=0.
  \]
* \(\dot\theta=0\) because \(v_1=0\) and \(\cos\theta=0\).
* For the curvature equation,
  \[
  \frac{\dot\alpha_3}{a_3}=6,\qquad
  \frac{2\alpha_3}{a_1a_2}=6,
  \]
  hence their sum is \(12=n_3\).
* The scalar curvature is \(s_g=-24\), so the Lichnerowicz terms on this spinor satisfy
  \[
  \frac{s_g}{4}+\frac{\rho}{2}=-6+6=0.
  \]

At the exact CH joining section \(x=X\), equality with this solution therefore means all four data
\[
\boxed{
\rho(X)=12,\quad
\theta(X)=\frac{\pi}{2},\quad
\alpha_1(X)=0,\quad
\alpha_3(X)=3X.} \tag{4}
\]

Only prescribing the first two entries of (4) does not prescribe the canonical CH solution.

### Exact obstruction for charged bolt data

For any diagonal metric, the set
\[
\theta=\frac{\pi}{2},\qquad \alpha_1=0
\]
is invariant under (2), since both \(\dot\theta\) and \(\dot\alpha_1\) then vanish identically.

It follows from uniqueness of the ODE that backward evolution from the complete data (4) satisfies
\[
\theta\equiv\frac{\pi}{2},\qquad \alpha_1\equiv0
\]
throughout the cell. It therefore reaches bolt charge \(0\), not
\(\alpha_1(0)=\sigma=\pm1\).

Hence, within this real SU(2)-invariant reduction, a monopole with bolt charge \(\sigma=\pm1\) cannot coincide exactly with the canonical CH solution from the joining section onward. A charged solution may still converge to (3) as \(r\to\infty\); that is a different two-ended ODE problem.

---

## 3. Bolt Frobenius expansion

Let the bolt be \(t=0\), with the first slot collapsing. Write the smooth metric expansion as
\[
\begin{aligned}
a_1(t)&=t+\kappa t^3+O(t^5),\\
a_2(t)&=b+\mu t^2+O(t^4),\\
a_3(t)&=b+\nu t^2+O(t^4).
\end{aligned} \tag{5}
\]
For the supplied perpendicular cell, \(b=\sqrt{x_0}\). Its smooth `wpow=2` construction also gives \(\mu=\nu\), although that equality is not needed below.

From (5),
\[
c=
\frac1{2t}
+\left(
\frac1{2b^2}-2\kappa-\frac{\mu+\nu}{b}
\right)t
+O(t^3). \tag{6}
\]

Fix the bolt degree
\[
\alpha_1(0)=\sigma,\qquad \sigma\in\{1,-1\},
\]
and define
\[
\theta_\sigma=\frac{1+\sigma}{2}\pi.
\]
Thus \(\theta_1=\pi\) and \(\theta_{-1}=0\). The regular nonzero-spinor branch has two real parameters \((\rho_0,\beta)\) and
\[
\boxed{
\begin{aligned}
\rho(t)&=\rho_0\bigl(1+R\,t^2+O(t^4)\bigr),\\
\theta(t)&=\theta_\sigma-\sigma\beta t+D\,t^3+O(t^5),\\
\alpha_1(t)&=
\sigma\left[
1-\left(\frac{\rho_0}{2}+\frac1{b^2}\right)t^2
\right]+O(t^4),\\
\alpha_3(t)&=\frac{b\rho_0\beta}{4}\,t^2+O(t^4),
\end{aligned}} \tag{7}
\]
where
\[
R=
\frac1{b^2}
-\frac32\kappa
-\frac{\mu+\nu}{b}
+\frac{\rho_0+\beta^2}{4}, \tag{8}
\]
and
\[
D=
\sigma\left[
\frac{\beta^3}{12}
+\beta\left(
\frac{\rho_0}{8}
+\frac1{2b^2}
+\frac{\kappa}{2}
\right)
\right]. \tag{9}
\]

In particular,
\[
n_1\longrightarrow-\sigma\rho_0,\qquad
n_3=\rho_0\beta t+O(t^3).
\]
This confirms the leading bolt formulas used by `sw_perp_cell_pair.py`, including the sign of \(\alpha_1\) and the factor \(1/4\) in \(\alpha_3\).

### Spinor variables regular at the bolt

The angular representation is singular whenever \(\rho=0\). A numerically cleaner form uses
\[
P=\frac{u-\sigma v}{\sqrt2},\qquad
Q=\frac{u+\sigma v}{\sqrt2}.
\]
Here \(P\) and \(Q\) are the \(\tau_1\)-eigencomponents with eigenvalues
\(-\sigma\) and \(+\sigma\). Regularity gives
\[
P(t)=P_0+O(t^2),\qquad
Q(t)=\frac{\beta P_0}{2}t+O(t^3),\qquad
P_0^2=\rho_0. \tag{10}
\]

The quantities
\[
P,\qquad \frac Qt,\qquad
\frac{\alpha_1-\sigma}{t^2},\qquad
\frac{\alpha_3}{t^2}
\]
are smooth even functions of \(t\) near the bolt. They are preferable to
\((\log\rho,\theta,\alpha_1,\alpha_3)\) for collocation, and they also retain the branch with \(P_0=0\), which the logarithmic variable omits.

---

## 4. What goes wrong in the two cell programs

### 4.1 `sw_perp_cell_pair.py`

Its differential equations and leading bolt series are correct. The principal issues are at the CH end and in conditioning.

1. **The terminal residual uses only**
   \[
   \log(\rho/12)=0,\qquad \theta-\pi/2=0
   \]
   at \(r=6.5\). It does not constrain \(\alpha_1\) and \(\alpha_3\).

   At a finite CH section, these two equalities allow a trajectory merely to cross the plane \(\rho=12,\theta=\pi/2\). It generally leaves that plane immediately because
   \[
   \dot{\log\rho}
   =\frac{\alpha_3-3\sinh^2r}{\sinh r\cosh r},
   \qquad
   \dot\theta=-\frac{\alpha_1}{\sinh r}
   \]
   there.

2. **Forward shooting is exponentially ill-conditioned.** Linearization around the canonical CH solution has two growing modes, with asymptotic exponents
   \[
   2,\qquad -2+\sqrt{13}\approx1.606.
   \]
   Tiny errors in \((\rho_0,\beta)\) therefore become large along the CH segment. Direct terminal values of \(\rho\) and \(\theta\) are poor coordinates for the required stable manifold.

3. At \(r=6.5\), the two decaying modes have sizes comparable to
   \[
   e^{-6r},\qquad e^{(-2-\sqrt{13})r},
   \]
   which are already around double-precision resolution. Asking finite-difference least squares to tune growing coefficients while the desired decaying traces are this small is numerically severe.

4. `least_squares` is given \(\rho_0\) itself rather than \(\log\rho_0\). Trial values can cross zero, where `math.log(rho0)` is undefined. Large positive \(\log\rho\) also makes `math.exp(lr)` overflow inside the ODE.

These numerical observations do not determine whether the bolt-regular and CH-stable manifolds intersect.

### 4.2 `sw_perp_cell_pair_v2.py`

The four endpoint equations in `bc` select the wrong local manifolds at both ends.

At the lower endpoint \(u=10^{-7}\), the code sets
\[
\theta=\theta_\sigma,\qquad \alpha_1=\sigma
\]
exactly. At a positive distance from the bolt, the regular series instead has
\[
\theta-\theta_\sigma=-\sigma\beta t+O(t^3),
\qquad
\alpha_1-\sigma
=-\sigma\left(\frac{\rho_0}{2}+\frac1{x_0}\right)t^2+O(t^4).
\]
Setting both corrections to zero effectively suppresses the free \(\beta\)-mode unless a thin numerical layer is created.

More importantly, no regularity equation is imposed on \(\alpha_3\). The local equation contains
\[
\dot\alpha_3+\frac2t\alpha_3=\text{regular forcing},
\]
whose general solution includes a \(t^{-2}\) term. The missing lower-end relation allows this nonsmooth mode to supply an artificial degree of freedom.

At the upper endpoint \(x=X\), the code imposes only
\[
\rho=12,\qquad \theta=\frac{\pi}{2}.
\]
This is neither the complete canonical data (4) nor the stable-manifold relation for convergence at infinity. The code also ends at \(X\), so it never represents the CH segment on which the asymptotic modes are selected.

There are two further numerical complications:

* \(a_1\sim\sqrt{u}\) near the bolt, but `CubicSpline` interpolates \(a_1\) directly as a function of \(u\) on a grid that omits \(u=0\). Its \(u\)-derivative is singular there. Interpolating \(a_1/t\) as a function of \(t^2\) is smooth.
* `np.exp(np.clip(y[0],-50,50))` changes the differential equation whenever the clip is active.

---

## 5. Correct CH stable data

On the exact CH end define
\[
L=\log\frac{\rho}{12},\qquad
\delta=\theta-\frac{\pi}{2},
\]
and
\[
\mathcal A=\frac{\alpha_1}{\sinh r},\qquad
\mathcal B=
\frac{\alpha_3-3\sinh^2r}{\sinh r\cosh r}.
\]
The exact CH equations become
\[
\begin{aligned}
L'&=-3\tanh r+\mathcal A\cos\theta
 +(3\tanh r+\mathcal B)\sin\theta,\\
\delta'&=(3\tanh r+\mathcal B)\cos\theta
 -\mathcal A\sin\theta,\\
\mathcal A'&=\rho\cos\theta
 -\left(\coth r+\frac{2}{\sinh r\cosh r}\right)\mathcal A,\\
\mathcal B'&=\rho\sin\theta-12
 -(3\coth r+\tanh r)\mathcal B.
\end{aligned} \tag{11}
\]

Linearization at \(L=\delta=\mathcal A=\mathcal B=0\) gives
\[
\begin{aligned}
L'&=\mathcal B,\\
\mathcal B'&=12L-(3\coth r+\tanh r)\mathcal B,\\
\delta'&=-3\tanh r\,\delta-\mathcal A,\\
\mathcal A'&=-12\delta
-\left(\coth r+\frac{2}{\sinh r\cosh r}\right)\mathcal A.
\end{aligned} \tag{12}
\]

As \(r\to\infty\), the decaying relations are
\[
\boxed{
\mathcal B=-6L+o(L),\qquad
\mathcal A=(\sqrt{13}-1)\delta+o(\delta).} \tag{13}
\]
Thus practical finite-\(R\) terminal equations are
\[
\mathcal B(R)+6L(R)=0,\qquad
\mathcal A(R)-(\sqrt{13}-1)\delta(R)=0, \tag{14}
\]
provided \(R\) is already in the small-perturbation region.

A more accurate finite-\(R\) version is
\[
\mathcal B=m(r)L,\qquad
\mathcal A=k(r)\delta,
\]
where
\[
\begin{aligned}
m'&=12-(3\coth r+\tanh r)m-m^2,
& m(\infty)&=-6,\\
k'&=k^2+
\left(3\tanh r-\coth r-\frac{2}{\sinh r\cosh r}\right)k-12,
& k(\infty)&=\sqrt{13}-1.
\end{aligned} \tag{15}
\]
Integrating these scalar Riccati equations backward supplies the tangent stable subspace at \(X\). For larger deviations, the full nonlinear CH stable manifold is obtained by integrating (11) backward from small decaying-mode amplitudes.

---

## 6. An implementable corrected formulation

### Asymptotically canonical CH end

A well-posed collocation formulation has two bolt parameters
\[
p=(\lambda,\beta),\qquad \rho_0=e^\lambda,
\]
and four ODE variables. At a small \(t=\varepsilon\), the four lower-end equations set the state equal to the Frobenius data (7), including the \(R\varepsilon^2\) correction if high accuracy is wanted. At a CH endpoint \(r=R\), two further equations impose (14), or the refined version from (15).

With four differential equations and two free parameters, these six endpoint equations have the correct count for `solve_bvp`.

An equivalent and often better-conditioned multiple-shooting representation is:

* a two-parameter bolt-regular family, propagated outward;
* a two-parameter CH-decaying family, propagated inward;
* equality of all four state variables at \(x=X\).

The exact mirror
\[
(\rho,\theta,\alpha_1,\alpha_3)
\longmapsto
(\rho,\pi-\theta,-\alpha_1,\alpha_3)
\]
maps the \(\sigma=1\) problem to the \(\sigma=-1\) problem, so only one charge needs an independent computation.

### Exact canonical equality at \(x=X\)

If equality with the canonical solution is intended from \(X\) onward, the endpoint data are the four equations (4). Backward evolution is then an ordinary initial-value problem, and the invariant-plane argument proves that it reaches \(\alpha_1(0)=0\). It therefore cannot realize either charged bolt sector in this ansatz.

---

## 7. Compact host versus isolated CH-ended cell

These are mathematically distinct existence questions.

* On a compact closed four-manifold, a relevant monopole class supplies global Seiberg–Witten solutions under the usual metric, chamber, and perturbation hypotheses. The trace of such a solution on the edge of a chosen cell is determined by the rest of the closed manifold.
* That global trace is not forced to equal the canonical CH data (4), or even to lie in the real SU(2)-invariant sector. Nonlinearity also prevents obtaining an invariant monopole by averaging an arbitrary global solution.
* On the isolated CH-ended cell, an invariant solution converging to (3) exists precisely when the two-dimensional bolt-regular family intersects the two-dimensional CH stable manifold in the four-dimensional reduced phase space.
* The supplied runs do not establish that intersection or its absence. They impose different endpoint subspaces from the two geometrically relevant ones.

Finally, the optimized record has nonzero scalar-deviation cost
\[
7.297586930245193\times10^{-6}.
\]
Thus the cell interior is not exactly scalar \(-24\), even though the exterior CH part is. The reported identity
\[
\int |\nabla\Phi|^2
=\int \frac{\rho(12-\rho)}2
\]
is exact only where \(s_g=-24\). On the complete cell the Weitzenböck expression is instead
\[
\int |\nabla\Phi|^2
=
\int\left(-\frac{s_g\rho}{4}-\frac{\rho^2}{2}\right).
\]
This scalar term does not alter the reduced ODE, but it does affect the integral comparisons in the two scripts.