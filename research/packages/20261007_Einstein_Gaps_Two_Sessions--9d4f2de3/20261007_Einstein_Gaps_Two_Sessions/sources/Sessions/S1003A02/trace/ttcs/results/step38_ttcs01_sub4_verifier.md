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

## Verification memo: SU(2)-invariant Seiberg–Witten reduction on the perpendicular cell

### Summary of what checks out and what does not

The symbolic reduction in `bianchi_sw_reduction.py` is correct: the Levi-Civita forms, the spin-connection sign, the Lichnerowicz self-consistency, the exact $S^+$ Dirac matrix $M$, and the self-dual curvature equation are all internally consistent, and the stated $\mathbb{CH}^2$ monopole solves the reduced ODE **exactly**. I found no sign or factor mistake in the derived ODE or in the bolt-end Frobenius data used by the forward shooter `sw_perp_cell_pair.py`. The trouble with the solvers has two distinct origins, both independent of the derivation:

1. `sw_perp_cell_pair_v2.py` imposes the wrong set of bolt-end conditions (one condition is automatically satisfied and therefore inert; a genuine regularity condition is absent).
2. The exact-$\mathbb{CH}$ trajectory is a hyperbolic saddle of the reduced flow with large positive growth exponents toward the collar, so forward integration is exponentially sensitive. This is a conditioning fact, not a coding mistake.

A third, conceptual point: matching the *full* canonical $\mathbb{CH}$ datum at a finite collar together with bolt regularity is over-determined for the 4-dimensional reduced system; the well-posed problem is bolt regularity plus stable-manifold decay at infinity.

I give the arithmetic below so each statement is checkable.

---

### 1. The exact reduced system (verified)

With coframe $e^0=dt,\ e^i=a_i\sigma_i$, $d\sigma_i=2\sigma_j\wedge\sigma_k$, the recorded $S^+$ Dirac matrix is

$$
M=\begin{pmatrix}M_{11}&M_{12}\\M_{21}&M_{22}\end{pmatrix}
= c\,I+\tfrac12\,(v_1\tau_1+v_2\tau_2+v_3\tau_3),\qquad
c=\frac{a_1^2+a_2^2+a_3^2}{2a_1a_2a_3}-\tfrac12\sum_i\frac{a_i'}{a_i},\quad v_j=\frac{\alpha_j}{a_j}.
$$

I re-expanded the JSON entries and confirmed this (e.g. $M_{11}=c+\tfrac12 v_3$, $M_{12}=\tfrac12(v_1-i v_2)$). The Dirac flow is $\phi'=M\phi$. Writing $\rho=|\phi|^2$, $n_j=\phi^\dagger\tau_j\phi$ and using $\{\tau_a,\tau_j\}=2\delta_{aj}$:

$$
\rho'=\phi^\dagger(M+M^\dagger)\phi=2c\rho+v\!\cdot\!n,\qquad
n_j'=\phi^\dagger(M^\dagger\tau_j+\tau_jM)\phi=2c\,n_j+v_j\rho .
$$

Restricting to the invariant locus $n_2=\alpha_2=0$ with $n=(\rho\cos\theta,0,\rho\sin\theta)$ gives exactly the solver's two equations
$$(\log\rho)'=2c+v_1\cos\theta+v_3\sin\theta,\qquad \theta'=v_3\cos\theta-v_1\sin\theta,$$
which I obtained independently from $n_1'=2c n_1+v_1\rho$. The curvature equation $\phi_j=\tfrac12(\alpha_j'/a_j+2\alpha_j/(a_ka_l))=n_j/2$ gives $\alpha_j'=a_j n_j-2a_j\alpha_j/(a_ka_l)$, matching `d1,d3`. The Clifford identity $(\vec n\!\cdot\!\vec\tau)\phi=\rho\phi$ is correct, so $c(F_A^+)\phi=\rho\phi$ and the Weitzenböck pairing gives $\tfrac{s}{4}+\tfrac12\rho\le0$ at an interior maximum, i.e. $\rho\le -s/2=12$ for $s=-24$. The amplitude density $\rho(12-\rho)/2\ge0$ used in the diagnostics is consistent with this.

**Exact $\mathbb{CH}$ check (decisive).** With $x=\sinh^2 r$, $t=r$, $a_1=a_2=\sinh r$, $a_3=\sinh r\cosh r$, I verified by hand that $\theta=\pi/2,\ \rho=12,\ \alpha_1=0,\ \alpha_3=3\sinh^2 r$ solves all four equations:
- $\alpha_3'=6\sinh r\cosh r$ vs $a_3\cdot12-2a_3\cdot3\sinh^2r/\sinh^2r=12\sinh r\cosh r-6\sinh r\cosh r$. ✓
- $c=-\tfrac32\tanh r$, $v_3=3\tanh r$, so $(\log\rho)'=2c+v_3=0$. ✓
- $\theta'=-v_1=0$, $n_2$ stays zero. ✓

This confirms every sign and factor in the reduced ODE and the collar datum simultaneously.

---

### 2. Bolt Frobenius data (verified) and the exact regularity conditions

Near the bolt $a_1=\sqrt F\to0$, $a_2=a_3=b=\sqrt{x_0}$, with $F'G'=1$ one has $a_1=\tau$ (so $\kappa=1$) and $t_0=\sqrt{\delta x/G'}$. I reproduced each starting value in `sw_perp_cell_pair.py`:

- $2c\to +1/\tau$ (leading), from $(2b^2)/(2\tau b^2)-\tfrac12(1/\tau)$ doubled.
- $v_1\cos\theta=(\alpha_1(0)/\tau)\cos\theta$. For $\rho$ to stay finite the $1/\tau$ pieces must cancel: $(1-\alpha_1(0))/\tau$ finite $\Rightarrow \alpha_1(0)=+1$ when $\theta\to\pi$, and $\alpha_1(0)=-1$ when $\theta\to0$. **Flux quantization $\alpha_1(\text{bolt})=\sigma=\pm1$ is forced by smoothness**, with the sign tied to the $\theta$-branch.
- The $\theta$ equation near the bolt, $\theta'\approx-(\sigma/\tau)\sin\theta$, integrates to $\tan(\theta/2)=C'/\tau$; for $\sigma=+1$ **every** trajectory has $\theta\to\pi$ with slope $\beta=-2/C'$ free. So $\theta(\text{bolt})=\pi$ is automatic, not a selecting condition.
- $\alpha_1=\sigma\big(1-(\rho_0/2+1/x_0)\tau^2\big)$ and $\alpha_3=\tfrac{b\rho_0\beta}{4}\tau^2$ follow from the two $\alpha$ equations; I verified the $\tau^2$ coefficients ($C=b\rho_0\beta/4$ from $4C=b\rho_0\beta$). The homogeneous mode of $\alpha_3'=-2\alpha_3/\tau+\dots$ is $\tau^{-2}$, so **regularity requires $\alpha_3(\text{bolt})=0$**.

Hence the regular bolt family is 2-parameter $(\rho_0,\beta)$, cut out of the 4-dimensional phase space by the two conditions
$$\boxed{\ \alpha_1(\text{bolt})=\sigma,\qquad \alpha_3(\text{bolt})=0.\ }$$
$\theta(\text{bolt})=\pi$ and $\rho$-finiteness are consequences, not independent conditions. The mirror map $(\rho,\theta,\alpha_1,\alpha_3)\mapsto(\rho,\pi-\theta,-\alpha_1,\alpha_3)$ for $\sigma\mapsto-\sigma$ leaves all four equations invariant (I checked each), so the $\sigma=-1$ monopole is the exact reflection.

---

### 3. Why forward shooting diverges: the collar is a saddle

Linearizing the reduced flow about the exact $\mathbb{CH}$ solution as $r\to\infty$ separates into two $2\times2$ blocks.

**Slot-1 block** $(\psi=\theta-\pi/2,\ \delta_1=\alpha_1)$, after the natural rescaling $\delta_1=e^{r}\tilde\delta_1$:
$$
\begin{pmatrix}\psi\\\tilde\delta_1\end{pmatrix}'=\begin{pmatrix}-3&-2\\-6&-1\end{pmatrix}\begin{pmatrix}\psi\\\tilde\delta_1\end{pmatrix},\qquad \lambda=-2\pm\sqrt{13}=\{+1.606,\,-5.606\}.
$$
**$(\log\rho,\alpha_3)$ block** $(\mu=\log(\rho/12),\ \delta_3=\alpha_3-3\sinh^2r=e^{2r}\tilde\delta_3)$:
$$
\begin{pmatrix}\mu\\\tilde\delta_3\end{pmatrix}'=\begin{pmatrix}0&4\\3&-4\end{pmatrix}\begin{pmatrix}\mu\\\tilde\delta_3\end{pmatrix},\qquad \lambda=\{+2,\,-6\}.
$$

So the collar carries a **two-dimensional unstable manifold** with growth $e^{1.6r}$ (in $\theta$) and $e^{2r}$ (in $\log\rho$). Integrating to `XFAR = sinh²(6.5)`, i.e. $r=6.5$, amplifies bolt errors by $e^{1.6\cdot6.5}\approx3\times10^4$ and $e^{2\cdot6.5}\approx4\times10^5$. The `rhs` then overflows ($\rho=e^{\log\rho}$ runs away), LSODA reports non-success, and `resid` returns the fallback $[10^3,10^3]$. The `np.clip(y[0],-50,50)` in v2 is a visible symptom of the same divergence. This is pure conditioning: the parameter count is right (2 bolt parameters $(\rho_0,\beta)$ ↔ 2 unstable modes to suppress), but the Jacobian condition number $\sim10^5$ leaves essentially no margin in double precision.

---

### 4. The endpoint-condition mistake in `sw_perp_cell_pair_v2.py`

`bc` returns $\{\theta(\text{bolt})=\pi,\ \alpha_1(\text{bolt})=\sigma,\ \log\rho(X)=\log12,\ \theta(X)=\pi/2\}$. Two problems:

- $\theta(\text{bolt})=\pi$ is **inert**: as shown, all regular trajectories satisfy it automatically, so this row of the endpoint Jacobian is nearly degenerate and controls nothing in the 2-parameter family.
- $\alpha_3(\text{bolt})=0$ is **missing**, so the singular $\tau^{-2}$ mode of $\alpha_3$ is not suppressed. On the stiff near-bolt mesh (coefficients $\sim1/\tau$, `fac`$\to\infty$), the collocation residual cannot be driven down with a nonzero $\tau^{-2}$ tail present, producing the large `rms_residuals`/non-convergence.

Replacing the inert condition by the missing one, i.e. imposing $\alpha_1(\text{bolt})=\sigma$ and $\alpha_3(\text{bolt})=0$, fixes the bolt side.

Separately, the collar conditions $\{\rho(X)=12,\theta(X)=\pi/2\}$ at the **finite** node $X$ leave $\alpha_1(X)$ free. The returned solution would then generically have $\alpha_1(X)\ne0$, so it would not continue as the exact canonical $\mathbb{CH}$ monopole beyond $X$; the two endpoint rows pin $(\rho,\theta)$ but do not enforce the stable-manifold decay. This conflates the finite-collar matching with the asymptotic problem.

---

### 5. A corrected formulation precise enough to implement

Variables $y=(\log\rho,\theta,\alpha_1,\alpha_3)$ on $u\in[0,1]$, $x=x_0 e^{\ell u}$, $\ell=\log(X/x_0)$, with the geometry $(G,a_i,\dot a_i)$ already tabulated. The right-hand side is the verified system of §1 times $dt/du=\ell x/(2\sqrt G)$.

**Bolt end (start mesh at $x_0+\delta$ using the Frobenius expansion, parameters $\rho_0,\beta$):**
$$
\log\rho=\log\rho_0,\quad \theta=\pi-\beta\tau,\quad \alpha_1=\sigma\!\left(1-(\tfrac{\rho_0}{2}+\tfrac1{x_0})\tau^2\right),\quad \alpha_3=\tfrac{\sqrt{x_0}\,\rho_0\beta}{4}\tau^2,\quad \tau=\sqrt{\delta/G'(x_0)} .
$$
Equivalently, as pure endpoint conditions for collocation: $\alpha_1=\sigma$ and $\alpha_3=0$ at $x_0^+$.

**Collar end.** Choose one of two mathematically different problems and keep them distinct:

(a) *Asymptotic problem (the one the shooter intends).* Integrate on the actual cell-plus-exact-$\mathbb{CH}$ geometry out to $r=R$. The correct far condition is projection onto the stable eigenspace: with $P_u$ the projector onto the two unstable eigenvectors (eigenvalues $+1.606,+2$ computed above, in the rescaled variables $\delta_1 e^{-r},\ \delta_3 e^{-2r}$),
$$
P_u\big(y(R)-y_{\mathbb{CH}}(R)\big)=0 \quad(\text{2 conditions}).
$$
This is well-posed against the 2 bolt parameters. Because the collar is a saddle, pure forward (or backward) single shooting is ill-conditioned either way ($|\lambda|$ up to $6$); use `solve_bvp` collocation (global Newton handles the saddle) or multiple shooting with a few knots, seeded by the exact $\mathbb{CH}$ solution on the outer part and the bolt Frobenius expansion on the inner part. The stable-eigenspace projection replaces the naive $\{\rho=12,\theta=\pi/2\}$ and removes the exponential sensitivity from the far condition.

(b) *Finite exact-$\mathbb{CH}$-ended cell with fixed datum.* If instead the full canonical datum is pinned at the finite collar, impose all four: $\rho(X)=12,\ \theta(X)=\pi/2,\ \alpha_1(X)=0,\ \alpha_3(X)=3X$. Together with the two bolt regularity conditions this is **six conditions on a four-dimensional system** — over-determined by two. Do not pose it as a determined `solve_bvp`.

A workable collocation setup for (a): 4 ODEs, endpoint conditions $\{\alpha_1(x_0^+)=\sigma,\ \alpha_3(x_0^+)=0,\ P_u(y(R)-y_{\mathbb{CH}})=0\}$ (two scalar rows), mesh clustered logarithmically near $x_0$, initial guess = bolt Frobenius glued to exact $\mathbb{CH}$. The redundant `theta if sigma==1 else 0` row should be dropped.

---

### 6. Existence: closed host versus isolated exact-$\mathbb{CH}$-ended cell

- **Closed host.** On a compact closed four-manifold the Seiberg–Witten system is elliptic with the a priori bound $\rho\le-s$ (here $\le-s/2$ in the recorded normalization); existence of an irreducible monopole is governed by the topology of the spin$^c$ structure (nonvanishing SW invariant / nonzero index), with no asymptotic datum to match. The SU(2)-invariant reduction then produces a genuine solution of the ODE on the closed orbit space, with regular bolt data at each end.

- **Isolated cell with fixed collar datum.** The cell is not closed; one end is the bolt (2 regularity conditions, verified above) and the other is prescribed. If the *entire* canonical $\mathbb{CH}$ datum is fixed at the collar, the matching is over-determined (§5b): generically there is no solution, and this over-determination — not any coding mistake — is the structural reason a four-condition `solve_bvp` with full collar data cannot be expected to converge. The mathematically natural cell problem replaces the fixed finite datum by *decay onto the collar's stable manifold* (§5a): bolt regularity (2) plus unstable-mode suppression (2) is a determined, well-posed intersection problem. Its solvability is a genuine question — whether the 2-dimensional regular bolt family meets the 2-dimensional stable manifold of the $\mathbb{CH}$ end — governed by a relative index / spectral-flow count for the cell, and is **not** automatic from the closed-host existence. The forward shooter targets exactly this intersection with the right dimension counts; only its numerical conditioning (the $e^{1.6r},e^{2r}$ saddle growth) prevents it from resolving the intersection, which is why collocation or multiple shooting with the stable-eigenspace projection is the appropriate instrument.

---

### What remains to be settled

The verification above establishes the ODE, the bolt data, and the $\mathbb{CH}$ datum, and explains the divergence. It does not by itself decide whether the regular bolt family actually intersects the collar's stable manifold for the certified cell — i.e. whether the invariant monopole pair exists on this specific exact-$\mathbb{CH}$-ended cell. Resolving that needs the corrected determined problem of §5a solved numerically (collocation with the projection condition), and ideally the relative-index count for the cell to confirm the intersection is expected. The kinetic/`rotation` density formulas used downstream were not re-derived here; they feed the diagnostics (the $K$, $\zeta^2$, rotation integrals) rather than the monopole equations themselves, and should be checked separately before those orbit integrals are used quantitatively.