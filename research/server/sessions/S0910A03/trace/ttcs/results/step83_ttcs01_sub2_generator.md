# TTCS Independent Branch Record

```json
{
  "step_id": 83,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step81_collapse_and_contraction.md"
  ]
}
```

## Task

Given the K-production framework for the OT graph-manifold connector, where K'=-2⟨τ,b⟩+2⟨vc⟩+Cov(v-u,k)-2xK with K(0)=12, K''(0)≥72, and a successful connector requires K≤6+2δ: investigate whether any known monotone or convex functional excludes the K-drop in the full coupled (γ_B, σ, M) OT system. Consider: (a) The total orbit energy E=∫ρ e_{H²} dz — does the full area/base evolution preserve E monotonicity? (b) The orbit-volume-weighted squared distance F=∫ρ d²_{H²}(U,P) dz for an appropriate reference P — does the coupled base response preserve its monotonicity? (c) The matrix Noether current Q=∫ρ M⁻¹M_r dz — can its vanishing be used in combination with other quantities? (d) Is there an energy/entropy functional combining K, x, y, ⟨|b|²⟩, ⟨h²⟩ that is monotone along the coupled Einstein evolution? Look for a differential inequality of the form d/dr(F)≥c·F or a Lyapunov argument. If no monotone quantity exists, identify which coupled mechanism breaks each candidate's monotonicity and what the resulting freedom is.

## Output

## Memo to the core research agent — monotone/convex control of the K-drop in the coupled OT system

A single geometric restatement organizes everything below. Identity (5.1) says
$$\langle R(q_r)\rangle_\rho=-\tfrac12 K,$$
so $K$ is (minus twice) the orbit-volume-weighted mean intrinsic scalar curvature of the $T^2$-invariant slice. The connector question is therefore literally: *can the Einstein-forced radial evolution raise the mean slice scalar curvature from $-6$ to $-3$?* This reframing is what lets the convex-function machinery of maps into a curvature-$(-1)$ target bite, because $U$ is exactly a weighted harmonic map into $\mathbb H^2$ and $K$ is a curvature moment of that map plus the area shear $\langle h^2\rangle$.

I give four genuinely different control attempts, each answering one of (a)–(d), then the object that ties them together and decides the matter.

---

### Possibility A — the convex-distance flux is monotone and survives the base coupling; it does not exclude the drop but forces a large orbit excursion (answers (b))

Work in the conformal base gauge (3.1). Put $P\in\mathbb H^2$ fixed, $\varphi=\tfrac12 d_{\mathbb H^2}^2(U,P)$. Because $\mathbb H^2$ has curvature $-1$, $\operatorname{Hess}(\tfrac12 d^2)\ge g_{\mathbb H^2}$ (radial eigenvalue $1$, transverse eigenvalue $d\coth d\ge1$). For a weighted harmonic map with weighted tension $\tau_\rho=\rho^{-1}\operatorname{div}(\rho\nabla U)$,
$$
\operatorname{div}(\rho\nabla\varphi)=\rho\,\langle\nabla U\otimes\nabla U,\operatorname{Hess}\varphi\rangle+\rho\,\langle\nabla\varphi,\tau_\rho\rangle\ \ge\ \rho|\nabla U|^2-\rho\,d\,|\tau_\rho|.
$$
The Hessian inequality holds for **any** positive background $\rho$, so the joint area/conformal response ($\gamma_B,\sigma,\lambda$) does not spoil this — the coupled base response cannot break the monotonicity of the flux
$$
\Psi(r)=\int_{S^1}\rho\,\varphi_r\,dz,\qquad \Psi(0)=0\ \text{(reflected end)},\qquad
\Psi'(r)=\int_{S^1}\operatorname{div}(\rho\nabla\varphi)\,dz .
$$
Only the defect term $\int\rho\,d\,|\tau_\rho|$ can. This is the exact analytic statement behind the Step 79 rigidity, and it shows the rigidity is destroyed solely by defect forcing, not by anything in the base sector.

Integrate from the reflected center to the exit interface at $r=R$ where $U$ is near $P$ ($\varphi,\varphi_r$ small):
$$
\underbrace{\int_0^R\!\!\int_{S^1}\rho|\nabla U|^2\,dz\,dr}_{\text{transported Dirichlet energy}}\ \le\ \int_0^R\!\!\int_{S^1}\rho\,d\,|\tau_\rho|\,dz\,dr\ +\ |\Psi(R)|.
$$
Now use the definitions to turn this into a statement about $K$. Since $|\nabla U|^2\ge|U_z|^2=e$ and $\int_{S^1}\rho e\,dz=V(K+\langle h^2\rangle)$, the left side is $\ge\int_0^R V(r)\,(K(r)+\langle h^2\rangle)\,dr\ge 6\int_0^R V\,dr$ over the part of the connector where $K\ge6$ (which, by $K(0)=12$ and $K''(0)\ge72$, is essentially the whole run up to the drop). With $|\tau_\rho|$ controlled by the orbit part of $E$ (so $\lesssim\delta$ in the physical norm) and $d\le d_{\max}$,
$$
\boxed{\,d_{\max}\ \gtrsim\ \frac{c}{\delta}\,}\qquad (c=O(1)).
$$
So a low-defect connector is *not excluded*, but it is forced to drive the orbit-shape map an $\mathbb H^2$-distance $\gtrsim1/\delta$ away from $P$ — the $T^2$ orbits must become anisotropic with aspect ratio $\sim e^{1/\delta}$ — and then return. This is the precise, quantitative form of the "expanding weight absorbs the anisotropy" mechanism: the growing orbit volume $\int V\,dr$ enters *only* through the forcing budget, so expansion loosens the exclusion by exactly the factor by which $V$ grows. **Gauge note:** the clean invariant form is (physical Dirichlet energy of $U$) $\le C\delta\int d\,dV_{\rm phys}+$ edge term; your verified slice-balance scripts can pin the constant $c$ by carrying the $e^{2\lambda}$ factors, which I have only tracked schematically here. The decisive follow-on is whether an excursion of size $1/\delta$ is dynamically compatible with $\|E\|\le\delta$ everywhere — a bootstrap, since a large excursion tends to source defect elsewhere.

---

### Possibility B — the Bakry–Émery energy Bochner formula is the object that actually decides A (sharpest line)

Treat $\rho=e^\sigma$ as a Bakry–Émery weight on the $2$D base. The energy density $e_U=|\nabla U|^2$ of the weighted harmonic map obeys
$$
\tfrac12\operatorname{div}(\rho\nabla e_U)=\rho|\nabla dU|^2+\rho\big\langle \mathrm{Ric}^\sigma_{\rm base}\,\nabla U,\nabla U\big\rangle+\rho\,|\nabla U\wedge\nabla U|^2+\rho\langle\cdots,\nabla\tau_\rho\rangle,
$$
where $\mathrm{Ric}^\sigma_{\rm base}=\mathrm{Ric}_{\rm base}+\operatorname{Hess}\sigma$ and the target term $+\rho|\nabla U\wedge\nabla U|^2\ge0$ because $\mathbb H^2$ has curvature $-1$ (the target sign *helps*). The base is flat in conformal gauge, so the only sign-indefinite term is $\operatorname{Hess}\sigma$.

This is the pivot. If $\operatorname{Hess}\sigma\ge0$ along the connector, then $e_U$ is weighted-subharmonic (up to defect) and attains its maximum on the region's rim — i.e. $e_U$ interior is controlled by the center and exit data, which **caps** $d_{\max}$ and would collide head-on with $d_{\max}\gtrsim c/\delta$ from Possibility A, excluding low-defect connectors and closing the hyperbolic-type barrier. If $\operatorname{Hess}\sigma$ can be sign-indefinite, energy can concentrate and the excursion is available — the escape.

The area equation controls only the **trace**:
$$
\operatorname{tr}\operatorname{Hess}\sigma=\Delta\sigma=6e^{2\lambda}-|\nabla\sigma|^2\quad(\text{sign-indefinite}),
$$
while the traceless part of $\operatorname{Hess}\sigma$ is set by the base constraints (4.8),(4.10) and is free. Therefore the entire connector question concentrates on **the sign structure of the traceless Bakry–Émery Hessian $\operatorname{Hess}_0\sigma$ of the log-orbit-area**, driven by the Liouville forcing. I recommend computing $\operatorname{Hess}\sigma$ explicitly on the exact reflected germ (you have the jets) and along the expanding tail, and testing whether the constraints (4.8),(4.10) force a lower bound $\operatorname{Hess}_0\sigma\ge -\kappa\,g$ with $\kappa$ small enough that the target term $+|\nabla U\wedge\nabla U|^2$ dominates. That inequality, if it holds, is a genuine monotone/maximum-principle exclusion; if the constraints permit $\operatorname{Hess}_0\sigma$ arbitrarily negative under bounded defect, that is the exact mechanism of the escape, and Possibility A's $d_{\max}$ excursion is then realizable.

---

### Possibility C — the $\langle\tau,b\rangle$ cancellation gives a moment functional free of the least-controlled term (answers (d))

The obstruction to a closed Lyapunov function on $(x,y,K)$ is that $K'$ contains $-2\langle\tau,b\rangle$, an inner product of the spatial tension with the radial orbit velocity that is not a function of the moments. Pair $K$ with the radial orbit energy $P=\langle|b|^2\rangle=\langle|U_r|^2\rangle$. Using the radial orbit equation $\nabla_r b+Hb+\tau=\mathcal E_0$ (§8) and $\tfrac{d}{dr}\langle f\rangle=\langle f_r\rangle+\operatorname{Cov}(H,f)$,
$$
P'=-2\langle H|b|^2\rangle-2\langle\tau,b\rangle+2\langle\mathcal E_0,b\rangle+\operatorname{Cov}(H,|b|^2).
$$
Both $K'$ and $P'$ carry the identical $-2\langle\tau,b\rangle$, so
$$
\boxed{\,(K-P)'=2\langle vc\rangle+\operatorname{Cov}(v-u,k)-2xK+2\langle H|b|^2\rangle-2\langle\mathcal E_0,b\rangle+\operatorname{Cov}(H,|b|^2)\,}
$$
is **free of the uncontrolled $\langle\tau,b\rangle$**. This is the correct combined variable to test as a Lyapunov candidate. Its remaining terms are far more structured: $2\langle vc\rangle$ is computed from (8.3); $2\langle H|b|^2\rangle$ is an energy–expansion correlation that is positive on the expanding tail and pushes $K-P$ up; the covariances are sign-indefinite. The mechanism most likely to prevent monotonicity of $W=K-\langle|b|^2\rangle$ is precisely the positivity of $\langle H|b|^2\rangle$ on expansion together with a favorable $\operatorname{Cov}(v-u,k)$ — the freedom is the correlation between mean curvature $H$ and radial orbit velocity, i.e. the connector can pour radial-orbit energy into regions of positive expansion. I recommend computing $W'$ on the exact reflected germ to second order (you have the $\tau,c,k$ jets) to see whether $W$ starts monotone and where it can reverse; the $\langle\tau,b\rangle$-free form makes this a finite, decidable computation rather than an estimate on an uncontrolled cross-term.

---

### Possibility D — the exactly conserved quantities are one-sided or mean-zero, and the freedom is $z$-concentration (answers (a) and (c))

Two exact conservation/one-sidedness facts survive the coupling, and both fall short for a structural reason worth naming.

The **Iwasawa height** obeys (4.6): $\operatorname{div}(e^\sigma\nabla\alpha)=-e^{\sigma-2\alpha}|\nabla\beta|^2\le0$, so $\alpha$ is weighted-superharmonic and the height flux $\int e^\sigma\alpha_r\,dz$ is nonincreasing, vanishing at the reflected center. This is a genuine one-sided monotone quantity, but it controls the *mean* anisotropy, not the gradient energy $e$ that defines $K$; the center stores its $|U_z|^2=12$ in $\alpha_z,\beta_z$, not in $\alpha$ itself. The companion (4.7) gives a conserved $\beta$-current $\int e^{\sigma-2\alpha}\beta_r\,dz\equiv0$. The natural upgrade is the Busemann function $B_\xi$ toward the ideal point that the tail approaches: $\operatorname{Hess}B_\xi=g_{\mathbb H^2}-dB\otimes dB$, so $B\circ U$ is weighted-subharmonic with the horocyclic energy $|\nabla U|^2-|\nabla(B\circ U)|^2\ge0$ as its source, and its flux grows *linearly* in $B$ rather than quadratically in $d$ — a tighter version of Possibility A that separately controls the horocyclic (i.e. $\beta$) energy. Pursuing the point-distance flux and the Busemann flux together pins both the total transported energy and its split into the height/horocycle sectors adapted to the tail's ideal point.

The **matrix Noether current** $Q=\int_{S^1}\rho\,M^{-1}M_r\,dz$ is conserved in $r$ (from $\operatorname{div}(\rho M^{-1}\nabla M)=0$) and vanishes by reflection, giving two scalar mean-zero conditions on the radial orbit velocity. It cannot be combined with the energy to force a bound because the orbit energy is quadratic while $Q=0$ is a first-moment condition: converting it into an energy inequality needs a weighted Poincaré inequality on $S^1_z$ with weight $\rho$. The coupled area equation permits $\rho$ to concentrate sharply in $z$, and a concentrating weight degenerates the weighted Poincaré constant. **That $z$-concentration of the orbit area is the precise freedom that defeats candidate (c).**

For candidate (a), the total spatial energy $E=\int\rho\,e_{H^2}\,dz$ is not monotone: $\tfrac{d}{dr}E$ contains the weight-growth term $\langle 2h\,e\rangle$ with $h=(\log\rho)_s$ sign-indefinite (area locally contracts or expands), plus the base-conformal coupling that injects the $\Lambda=-3$ source. The freedom this exposes is redistribution — the growing weight and area shear let energy move between the $r$- and $z$-sectors and spread over growing orbit volume, which is exactly why $E$ carries no exclusion.

---

### The unifying picture and what to consult

All four candidates reduce to the same fork already isolated in Possibility B: the exact-Einstein structure makes the convex functionals (A), the height/Busemann one-sidedness (D), and the matrix current (C) rigid, and the *only* things that can break each are (i) the defect forcing $\rho\,d\,|\tau_\rho|$, and (ii) the sign-indefiniteness of $\operatorname{Hess}\sigma$ and the $z$-concentration of $\rho$ that the Liouville area equation leaves free. The single decisive computation is the sign of the Bakry–Émery Hessian $\mathrm{Ric}_{\rm base}+\operatorname{Hess}\sigma$ (in $2$D, $=\operatorname{Hess}\sigma$) subject to the base constraints; that sign either caps $d_{\max}$ (colliding with the $d_{\max}\gtrsim c/\delta$ excursion and excluding low-defect connectors) or permits energy concentration (the escape).

Two source families are directly relevant and worth naming as reading targets, not for citation manufacture: the reduction of stationary axisymmetric Einstein gravity to an $SL(2,\mathbb R)/SO(2)$ ($\mathbb H^2$) harmonic map coupled to a $2$D dilaton (Ernst/Weyl–Papapetrou; Geroch group and its infinitely many conserved currents), and the modification of that integrable structure by a cosmological constant (Belinski–Zakharov / inverse-scattering with $\Lambda$, and Liouville-forced area). In the $\Lambda=0$ vacuum case the whole tower of Geroch currents is conserved and none obstruct a connector because they are symmetries; the $\Lambda=-3$ term is precisely the forcing that enters every current balance with a definite geometric source. Reading the $\Lambda$-modified integrability tells you which of your candidate functionals inherit an exact conservation and which acquire a one-signed $\Lambda$-source — the latter are the true monotone candidates. The second family is weighted/drift harmonic maps and Bakry–Émery $\Gamma_2$ calculus into NPC targets, which is the exact technical home of Possibility B's energy Bochner formula.

One concrete numerical test that would move the key judgment at low cost: integrate the exact reflected OT germ outward with your verified slice-balance solver, track $d_{\rm H^2}(U,P)$, the physical Dirichlet energy, and $\operatorname{Hess}\sigma$ simultaneously, and check whether the observed excursion is consistent with $d_{\max}\gtrsim c/\delta$ and whether $\operatorname{Hess}_0\sigma$ is driven to the sign that would cap the energy. That single run distinguishes "excluded low-defect connector" from "excursion-based escape" and tells you which of A/B is the operative mechanism.