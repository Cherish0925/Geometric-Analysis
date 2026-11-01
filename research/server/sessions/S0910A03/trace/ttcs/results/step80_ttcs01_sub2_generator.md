# TTCS Independent Branch Record

```json
{
  "step_id": 80,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/data/step80_base_identity.json",
    "Sessions/S0910A03/workspace/data/step80_joint_base_response_summary.json",
    "Sessions/S0910A03/workspace/data/step80_residual_atlas.json",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step76_center_energy_transport_and_scattering.md",
    "Sessions/S0910A03/workspace/notes/step78_rotating_eigenframe_barrier.md"
  ]
}
```

## Task

Using the invariant orthogonally-transitive equations and the Step 80 numerical evidence, develop a mathematically concrete construction or obstruction focused on the first O(1) physical layer after a reflected scalar-minus-six T^3 center. The central issue is whether the base metric and orbit area can compensate the positive-semidefinite H^2 orbit-map stress while the full Ricci defect tends to zero and the shape reverses from forced contraction toward expansion. Propose a minimal but genuinely coupled ansatz or rescaling that is not a frozen cusp and not merely Step 73's tail; derive its equations or leading asymptotics, specify boundary/jet data consistent with reflection and R(q0)=-6, and identify a decisive calculation that could distinguish a real vanishing-defect mechanism from a surviving sign obstruction. Respect that common lattice scaling leaves U unchanged and that physical forcing uses rho dvol(gamma_B), e^{3r} on the cusp.

## Output

## Framing

The material below treats the first O(1) radial layer after a reflected, totally geodesic T³ center as an **exact** coupled elliptic problem in the orthogonally‑transitive (OT) variables, rather than as a fixed orbit‑map placed on a frozen cusp. The single most useful move I can offer is to show that the object the Step 80 runs were probing (entry operator sup ≈ 15 that refuses to fall near r≈0.2 even as the far end improves) is largely an artifact of holding σ, λ fixed while fitting only the orbit map; the exact coupled diagonal system has zero Ricci defect by construction, so the real question is not "can the defect be made small" but "does the coupled elliptic end‑to‑end problem admit a reflection‑symmetric member with a Yamabe‑sign‑minus Poincaré–Einstein (PE) far end." I then give a clean identity forced by R(q₀)=−6, isolate exactly where a sign feedback could survive, and name a decisive linear computation.

## 1. A minimal genuinely coupled ansatz that is neither a frozen cusp nor the Step 73 tail

Work in the invariant conformal base gauge with a **diagonal** orbit metric (this is the minimal choice that already breaks the Bianchi VII₀ feedback, see §4):

$$
g=e^{2\lambda(r,z)}(dr^2+dz^2)+e^{\sigma(r,z)}\big(e^{d(r,z)}dx^2+e^{-d(r,z)}dy^2\big),
$$

so $M=\mathrm{diag}(e^{d},e^{-d})\in \mathrm{SL}(2,\mathbb R)$, $\rho=e^{\sigma}$, and the point in $H^2$ moves on the diagonal geodesic $\psi\equiv0$. The three unknowns $(\sigma,\lambda,d)$ each depend on both base variables — this is the essential difference from the frozen cusp (which fixes $\sigma=2r,\lambda=r$) and from Step 73's tail (which fixes $\sigma=2r-2\log N,\ \lambda=r$ and solves only for $d$). The exact $\mathrm{Ric}=-3g$ system is

$$
\sigma_{rr}+\sigma_{zz}+\sigma_r^2+\sigma_z^2=6\,e^{2\lambda},\tag{A, area}
$$
$$
(e^{\sigma}d_r)_r+(e^{\sigma}d_z)_z=0,\tag{O, orbit}
$$
$$
\Delta\lambda=\tfrac14\big(|\nabla\sigma|^2-|\nabla d|^2\big),\tag{C, conformal}
$$

together with the two first‑order relations from $\mathrm{Ric}_{rz}=0$ and $\mathrm{Ric}_{rr}-\mathrm{Ric}_{zz}=0$,

$$
\sigma_{rz}=\sigma_r\lambda_z+\sigma_z\lambda_r-\tfrac12\sigma_r\sigma_z-\tfrac12 d_r d_z,\qquad
\sigma_{rr}-\sigma_{zz}=2(\sigma_r\lambda_r-\sigma_z\lambda_z)-\tfrac12(\sigma_r^2-\sigma_z^2)-\tfrac12(d_r^2-d_z^2).\tag{K}
$$

The count is three second‑order elliptic equations for three fields on the $(r,z)$ half‑cylinder; (K) are the compatibility relations that a conformal‑gauge solution satisfies automatically once the gauge is fixed. **Any smooth solution of (A,O,C,K) has identically zero Ricci defect.** This is the correct object to solve numerically, in place of an orbit map fitted on a fixed $(\sigma,\lambda)$: the residual you were watching in Step 80 is the residual of the *reduced* fit, not of the Einstein system.

## 2. Reflection‑face jet

At a totally geodesic reflection face $r=0$ all first $r$‑derivatives of the even fields vanish: $\sigma_r=\lambda_r=d_r=0$. The Einstein equations then fix the second $r$‑jet pointwise in $z$:

$$
\sigma_{rr}(0,z)=6e^{2\lambda}-\sigma_{zz}-\sigma_z^2,\qquad
d_{rr}(0,z)=-d_{zz}-\sigma_z d_z,\qquad
\lambda_{rr}(0,z)=\tfrac14(\sigma_z^2-d_z^2)-\lambda_{zz}.
$$

Both first‑order relations (K) hold at $r=0$ by reflection evenness. The center data are therefore a free choice of the T³ metric $q_0=e^{2\lambda(0,z)}dz^2+e^{\sigma(0,z)}(e^{d(0,z)}dx^2+e^{-d(0,z)}dy^2)$, and the outward layer is completely determined to second order by that choice. The two physically important shape quantities are the second $r$‑derivatives above: the orbit area wants to expand because $\sigma_{rr}(0)\approx 6e^{2\lambda}>0$ (the $\Lambda=-3$ push), while $\lambda_{rr}$ (the z‑direction shape) is **suppressed** by the orbit z‑stress $d_z^2$. This sign asymmetry is the germ of the tension the task is pointing at.

## 3. The center anisotropy identity forced by R(q₀)=−6

For $q_0$ written in proper length $d\tau=e^{\lambda}dz$ along the z‑circle,

$$
R(q_0)=-2\sigma_{\tau\tau}-\tfrac32\sigma_\tau^2-\tfrac12 d_\tau^2 .
$$

Since $q_0$ is a totally geodesic slice of a $\mathrm{Ric}=-3g$ four‑manifold, the Gauss relation gives $R(q_0)=R(g)-2\mathrm{Ric}(n,n)=-12+6=-6$ automatically. Multiplying $2\sigma_{\tau\tau}+\tfrac32\sigma_\tau^2+\tfrac12 d_\tau^2=6$ by $\rho=e^{\sigma}$ and integrating around the circle (using $\oint\sigma_{\tau\tau}e^\sigma=-\oint\sigma_\tau^2 e^\sigma$) yields the sharp, lattice‑invariant identity

$$
\boxed{\ \big\langle d_\tau^2\big\rangle_\rho=12+\big\langle\sigma_\tau^2\big\rangle_\rho\ \ge 12,\qquad \langle f\rangle_\rho:=\frac{\oint f e^\sigma d\tau}{\oint e^\sigma d\tau}.}
$$

Because the common lattice rescaling $G\to N^{-2}G$ shifts $\sigma$ by a constant and leaves $M$ (hence $d$) untouched, the ratio is invariant; the floor survives the rank‑two lattice collapse, exactly as Step 76 reported, but now with the extra $\langle\sigma_\tau^2\rangle$ term made explicit. **The center is forced to carry order‑one z‑varying orbit anisotropy $d$.** In particular $d_z\not\equiv0$: a homogeneous (z‑independent) reflected center is impossible, which is why the whole construction must live in the genuinely two‑variable base and not in any cohomogeneity‑one ODE reduction.

A useful corollary for the shape jet: requiring the outgoing shape operator to be umbilic already at $O(r)$ needs $d_{rr}(0,z)\equiv0$, i.e. $d_{zz}+\sigma_z d_z=0\Rightarrow e^\sigma d_z=\mathrm{const}\Rightarrow d_z\equiv0$, which the floor forbids. So the center shape is necessarily anisotropic; the real question is whether that anisotropy **decays** outward, not whether it can be absent.

## 4. Why the diagonal orbit map removes the VII₀ sign feedback

The VII₀ barrier (Step 78) is entirely a **frozen‑angular‑source** phenomenon: with $\psi_z=k$ held constant, the geodesic‑distance equation carries a strictly positive source $e^\sigma\sinh d\cosh d\,k^2>0$, forcing $d$ (hence $K=2k^2a^{-2}\sinh^2 d$) monotonically up. In the diagonal ansatz $\psi\equiv0$ and equation (O) is source‑free:

$$
(e^\sigma d_r)_r+(e^\sigma d_z)_z=0 .
$$

This is a weighted‑harmonic (weighted‑Laplace) equation for $d$ with the **growing** weight $e^\sigma$. It has no definite‑sign forcing, so nothing prevents the anisotropy energy from radiating outward and decaying: high z‑frequency components of $d$ are damped by the growing weight, and the orbit intrinsic curvature $K\sim e^{-2r}\sinh^2 d\to 0$ as $d$ homogenizes and the area grows. This is precisely the mechanism Step 79 named (2‑variable base transport, item 1) made concrete in the simplest closed system. The sign feedback that produces the barrier is a property of the *frozen angular* geodesic, not of the orbit map space.

The decisive structural point for the task: in the diagonal system the positive‑semidefinite $H^2$ orbit stress $|\nabla d|^2$ enters (C) and the shape jet with a fixed sign, but it enters (O) — the equation that governs its own evolution — **with no source at all**. There is therefore no self‑amplification. Whether it is *compensated* is then a linear question about the coupled (A,C) response, not a nonlinear runaway.

## 5. The convex‑distance rigidity dissolves at an infinite PE end

The apparent exact‑connector rigidity (Step 79 §8, the $F=\tfrac12 d^2_{H^2}(U,P)$ maximum principle) is real but its reach must be stated precisely. For an exact weighted‑harmonic map $U$ into $H^2$ (curvature $-1$, so $\mathrm{Hess}\,F\ge g_{H^2}$),

$$
\mathrm{div}\!\big(e^\sigma\nabla(F\circ U)\big)\ge e^\sigma|dU|^2\ge0 .
$$

With Neumann data at the reflection face and $U\to P$ **at a finite exit**, $F$ is a weighted‑subharmonic function that is zero on the outer edge and Neumann at $r=0$; then $F\equiv0$, $U\equiv P$, and the anisotropy floor is contradicted. But at an **infinite** PE end the relevant weighted line operator $(w\,h')'$ with $w\sim e^\sigma\sim e^{cr}$ ($c>0$) is transient, $\int^\infty w^{-1}dr<\infty$, so bounded nonconstant weighted‑harmonic functions exist (e.g. $1-e^{-\int^r w^{-1}}$) and bounded weighted‑subharmonic functions need not be constant. **The convex‑distance rigidity pins $U$ to a point only when the far end is reached at finite radius.** Consequently the correct target is not $U\to P$ at finite $r$ but $U\to U_\infty\neq P$ at an infinite PE end that retains anisotropy — exactly what the pure cusp already shows, where $d\to \mathrm{const}\neq0$ ($\psi_k(\infty)=\sinh k/k$). This removes the perceived exact‑connector no‑go and moves the entire question to existence of a reflection‑symmetric solution with an infinite PE end.

## 6. Shape reversal is compatible with the area equation

The z‑independent Hamiltonian‑type relation in the coordinates of §2 gives, along the radial direction, $u'\approx 3-K$ where $u$ is the mean shape eigenvalue and $K$ the orbit intrinsic curvature. At the center $K\approx6$ forces $u'(0)\approx-3$ (forced contraction). As $d$ homogenizes and $\sigma$ grows, $K\to0$, so $u'\to3>0$ and the shape reverses toward the umbilic expanding value. This is self‑consistent with the source‑free decay of §4: the same area growth that damps $d$ also lowers $K$, and both push the shape from contraction to expansion. The reversal is therefore not fought by a sign in (O); the only place a surviving sign could live is the coupled response of $\lambda$ (the z‑direction shape) to the orbit stress in (C).

## 7. Decisive calculations

**(i) Solve the exact coupled diagonal elliptic system, not the reduced fit.** On $[0,R]\times S^1_z$ solve (A,O,C) with reflection Neumann data at $r=0$ (a chosen anisotropic $q_0$ meeting the §3 floor) and PE‑model matching at $r=R$, then let $R\to\infty$. Because solutions of (A,O,C) have zero defect identically, a converging family is direct evidence of existence; a genuine cokernel that blocks the elliptic solve is the surviving sign obstruction. This replaces the Step 80 protocol, whose fixed‑$(\sigma,\lambda)$ orbit map necessarily leaves an O(1) entry residual near the center regardless of $R$ — that residual is the price of freezing the area/conformal fields, not a property of the Einstein problem. The quantity to watch is the traceless shape at the exit, $e^{2R}(S-I)^\circ$, and whether it tends to a finite PE stress functional of the conformal‑infinity datum.

**(ii) Linearize the end‑to‑end map at an explicit background and test its response.** Take the hyperbolic cusp (or a Li–Liu Toda member) as background and compute the linearized map from reflection (Neumann) data at $r=0$ to conformal‑infinity data at the PE end for the coupled triple $(\sigma,\lambda,d)$. Anderson's PE theory makes this map Fredholm of index zero and permits cusp degeneration. The decisive question is whether the forced anisotropy of §3 lies in the image: if the linearization is onto the reflection data with $R(q_0)=-6$, the implicit function theorem produces a family of exact reflected connectors near the background (existence on the $\Lambda=-3$, Yamabe‑sign‑$-$ branch); if there is a one‑dimensional cokernel with a definite sign, that sign is the real obstruction, and it can be exhibited as a single number — the pairing of the cokernel element with the orbit stress $|\nabla d|^2$ generated by the center.

**(iii) Non‑horizontal totally geodesic slice inside the integrable (Toda) family.** A level $\xi=\mathrm{const}$ of Li–Liu cannot be totally geodesic (it forces $W=-1$). Test instead a slice $\{f(\xi,z)=\mathrm{const}\}$ preserving the T² action: the totally geodesic condition $S\equiv0$ becomes a first‑order PDE for $f$ against the Toda potential $v$ with $W=1-\tfrac12\xi v_\xi$. Solvability with T³ topology would produce an exact reflected Einstein metric with a PE end by reflection, settling the $\Lambda=-3$ branch construction; unsolvability across the whole Toda family would show the reflected connector must be non‑anti‑self‑dual, focusing the search. This is a clean elliptic test grounded in the one exact source available.

## 8. What separates a real mechanism from a surviving sign

The three calculations converge on one scalar test. The center injects a fixed‑sign orbit stress $|\nabla d|^2$ with the floor $\langle d_\tau^2\rangle_\rho\ge12$. Equation (O) does not amplify it (no source, §4), and the maximum‑principle rigidity does not forbid its outward radiation once the end is infinite (§5). The only remaining place a sign can persist is the coupled response of the z‑direction conformal factor: $\lambda_{rr}(0)$ is lowered by $d_z^2$, and if the linearized (C)+(A) response to the forced $|\nabla d|^2$ produces a cokernel element whose pairing with $|\nabla d|^2$ has a fixed sign, the exit traceless shape $e^{2R}(S-I)^\circ$ cannot be driven to zero and the umbilic PE far end is unreachable — a genuine obstruction. If instead that pairing is unconstrained in sign (the area growth $6e^{2\lambda}$ in (A) supplies enough freedom to move $\lambda$ and $\sigma$ so that the traceless shape decays), the mechanism is real and the reflected connector exists near the tested background. The single decisive number is therefore the sign of

$$
\int_{[0,\infty)\times S^1} \Xi\cdot|\nabla d|^2\, e^{2\lambda}\,dr\,dz,
$$

where $\Xi$ is the cokernel field of the linearized coupled end‑to‑end map at the chosen background. Producing $\Xi$ explicitly and evaluating this pairing on the §3 center data is the calculation that would change the judgement, and it uses only linear elliptic theory plus the exact background, so it is inexpensive relative to a full nonlinear solve. The nonlinear solve (i) is the confirming step once the linear sign is known.

Two things to keep in view while doing this: the lattice invariance means the constant part of $\sigma$ is free, so the pairing must be evaluated on $M$ and the $\sigma$‑gradients only; and the physical measure is $\rho\,d\mathrm{vol}(\gamma_B)$ with the $e^{3r}$ growth on the cusp side, so the pairing weight $e^{2\lambda}$ above is the correct one and the transience $\int e^{-\sigma}dr<\infty$ (§5) is what makes the far‑end response finite. Success here would still leave the positive branch and the higher‑dimensional quantifier of the full problem untouched, but it would replace a finite‑tolerance fit by a sharply defined linear sign whose outcome genuinely decides the $\Lambda=-3$ reflected route.