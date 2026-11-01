# TTCS Independent Branch Record

```json
{
  "step_id": 76,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md",
    "Sessions/S0910A03/workspace/scripts/step76_center_energy_flux_verify.py",
    "Sessions/S0910A03/workspace/data/step76_center_energy_flux.json"
  ]
}
```

## Task

For the Yau-26 negative graph-manifold route, verify and sharpen the new center-energy/transport synthesis from first principles. In the diagonal orthogonally-transitive class, derive with correct physical measures: (i) the periodic center identity for q=ds^2+G(s), rho=sqrt(det G), h=rho'/rho, A0=A-(h/2)I, including the approximate scalar error e=R_q+6; (ii) the diagonal d=b-c specialization and its normalization under lattice quotients; (iii) the invariant exact and forced equations div_gamma(rho grad d)=-rho(E_x-E_y), total signed flux, boundary covariance pairing with arbitrary constant c, and all signs; (iv) the slice evolution F'(r) in Gaussian distance; and (v) for one Fourier mode on an expanding flat-cusp background, the reflection-normalized solution, asymptotic derivative, weighted pairing, and normalized decay. State exactly whether these identities imply a positive Ricci-defect cost or instead exhibit a feasible energy-dilution mechanism, and identify assumptions needed for either conclusion.

## Output

# Verification memo: center-energy / transport synthesis for the negative graph-manifold route

Session S0910A03. I reconstructed every identity in Steps 73–76 and the `step76_center_energy_flux_verify.py` bookkeeping from first principles, with attention to the physical measures. The algebra is correct throughout; the substantive question is what the chain does and does not force, and I address that explicitly at the end.

## Setup and measure conventions

The center slice is $q=ds^2+G(s)_{ab}dx^adx^b$ on $T^3$, $G$ a periodic positive-definite $2\times2$ matrix, orbits flat $T^2$. Shape operator $A=\tfrac12 G^{-1}G'$, $h=\operatorname{tr}A=(\log\sqrt{\det G})'=\rho'/\rho$ with $\rho=\sqrt{\det G}$. I confirmed $A=\tfrac12 G^{-1}G'$ from $\Gamma^s_{ab}=-\tfrac12 G'_{ab}$; the sign convention is the expanding-orbit one used consistently in the notes. The correct weight for $s$-integrals of fiber-integrated quantities is $\rho\,ds$, i.e. the 3-volume density up to the (lattice-dependent) coordinate torus area, which cancels in every normalized statement below.

## (i) Periodic center scalar identity

For flat leaves the foliation scalar formula gives $R_q=R_{\rm leaf}-h^2-|A|^2-2h'=-2h'-h^2-|A|^2$; I checked the general form against round $S^n$ (recovers $n(n-1)$), so the flat-leaf specialization is reliable. With $A_0=A-\tfrac h2 I$ and $|A|^2=|A_0|^2+\tfrac{h^2}{2}$ in dimension two,
$$R_q=-2h'-\tfrac32 h^2-|A_0|^2,$$
matching `pointwise_R_formula = -A0sq - 3*h**2/2 - 2*hp`. Set $e=R_q+6$ (the totally-geodesic reflection center of a 4-D $\operatorname{Ric}=-3g$ core forces $R_q=-6$; I verified $R_q=R_g-2\operatorname{Ric}_g(n,n)=-12+6=-6$).

Multiply $|A_0|^2=-2h'-\tfrac32h^2+6-e$ by $\rho$ and integrate over the $s$-circle. Using $\rho'=\rho h$, integration by parts gives $\int\rho(-2h')=2\int\rho h^2$, so
$$\boxed{\int\rho|A_0|^2\,ds=6\!\int\!\rho\,ds+\tfrac12\!\int\!\rho h^2\,ds-\!\int\!\rho e\,ds.}$$
This matches the script exactly. The substitution `hp -> -h^2` in the code is a valid density encoding of the by-parts identity $\int\rho h'=-\int\rho h^2$, not a false pointwise relation; the resulting `A0_energy_density_identity = -e + h**2/2 + 6` and its integrated `meaning` are correct.

## (ii) Diagonal $d=b-c$ and lattice normalization

$G=\operatorname{diag}(e^{2b},e^{2c})$: $\rho=e^{\sigma}$, $\sigma=b+c$; $A=\operatorname{diag}(b',c')$; $A_0=\tfrac{d'}{2}\operatorname{diag}(1,-1)$, so $|A_0|^2=\tfrac12(d')^2$ (matches `A0_sq = d_s**2/2`). Hence
$$\int\rho(d')^2\,ds=12\!\int\!\rho+\!\int\!\rho h^2-2\!\int\!\rho e,$$
matching `d_energy_density_identity`. Dividing by $\int\rho$ gives the invariant per-volume anisotropy energy. Under a lattice/constant fiber rescaling $b,c\mapsto b+{\rm const},c+{\rm const}$: $d=b-c$ and $s$ are unchanged, $\rho$ picks up a constant that cancels in the ratio; so the normalized energy is a genuine lattice-quotient invariant. When $e=0$ it is $\ge12$ (since $\int\rho h^2\ge0$).

For the ambient bound I re-derived $e=R_q+6=\operatorname{tr}_TE-E_{nn}$ from $R_q=R_g-2\operatorname{Ric}_g(n,n)$ with $E=\operatorname{Ric}_g+3g$, $R_g=\operatorname{tr}_gE-12$: $R_q=\operatorname{tr}_TE-E_{nn}-6$, so $e=\operatorname{tr}_TE-E_{nn}$ and $|e|\le4\delta$ under $|E|_{\rm op}\le\delta$. Then normalized energy $\ge12-8\delta$, matching `ambient_defect_floor`. All correct.

## (iii) Invariant transport equation, flux, covariance, signs

For the orthogonally-transitive block $g=\gamma_{\mu\nu}dx^\mu dx^\nu+e^{2b}dx^2+e^{2c}dy^2$, the fiber Ricci mixed components are $R^x_x=-\tfrac1\rho\operatorname{div}_\gamma(\rho\nabla b)$, $R^y_y=-\tfrac1\rho\operatorname{div}_\gamma(\rho\nabla c)$, $\rho=e^{b+c}$. With $E_x=R^x_x+3$, $E_y=R^y_y+3$,
$$\boxed{\operatorname{div}_\gamma(\rho\nabla d)=-\rho\,(E_x-E_y),\qquad d=b-c.}$$
The vacuum case gives (2.2). I also checked the coordinate form: for $\gamma=e^{2\phi}\delta$ in 2-D, $\operatorname{div}_\gamma(\rho\nabla_\gamma d)=e^{-2\phi}\operatorname{div}_\delta(\rho\nabla_\delta d)$, so the Step 73 form $\operatorname{div}_\delta(\rho\nabla_\delta d)=-e^{2\phi+\sigma}(E_x-E_y)$ is the same identity; the extra $e^{2\phi}$ is only the conformal factor, not a discrepancy.

**Net signed flux.** $Q(r)=\int_{S^1}\rho\,d_r\,dz$ satisfies $Q'(r)=-\int_{S^1}\rho(E_x-E_y)$; in vacuum $Q$ is $r$-constant, and reflection gives $Q(0)=0$, hence $Q(R)=0$ (matches `net_signed_flux`). In the forced case $Q$ is not constant and $Q(R)=-\int_0^R\!\int_{S^1}\rho(E_x-E_y)$; the notes correctly restrict the zero-flux statement to $E=0$.

**Boundary covariance with arbitrary $c$.** Multiplying by $(d-c)$ and integrating by parts, the center face contributes nothing ($d_n=0$) and in vacuum
$$\int_D\rho|\nabla d|^2=\oint_{\partial_{\rm out}D}(d-c)\rho\,d_n\,d\ell,\quad\text{any constant }c,$$
because $-c\oint\rho d_n=-cQ(R)=0$. This is exactly (2.5). The point is sharp: even when the pointwise flux density $\rho d_n$ is small in sup norm, its covariance against $(d-c)$ (choose $c=$ boundary mean of $d$) can be order one. Signs: $\int_D\rho|\nabla d|^2\ge0$, so the boundary covariance and $F(R)$ below are nonnegative. All correct.

**Umbilic-exit rigidity.** Exact umbilic in orbit directions means $b_n=c_n$, i.e. $d_n=0$; with $d_n=0$ on both faces the energy identity forces $d\equiv{\rm const}$. Then the center metric (2.6) is conformal to a flat $T^2\times S^1$, and $R_q=-6$ requires $-8\Delta_{\rm flat}u=-6u^5$, impossible on $T^3$ ($\int$ LHS $=0<\int$ RHS). I confirmed this excludes only the *finite equal-orbit-derivative* exit, not exact cores in general: the reciprocal-warp family in §4 solves $u''=\tfrac34u^5-\tfrac14(f')^2u$ with $h_f$ *non*-conformally-flat, so no contradiction with existence of scalar-$-6$ center metrics.

## (iv) Slice evolution $F'(r)$ in Gaussian distance

Define $F(r)=\int_{D_r}\rho|\nabla d|^2$ over $D_r=[0,r]\times S^1$. Differentiating,
$$F'(r)=\int_{S^1}\rho\big(d_r^2+\gamma^{zz}d_z^2\big)\sqrt{\gamma_{zz}}\,dz=N(r)+Z(r),\quad N,Z\ge0,$$
matching `F'(r)=N(r)+Z(r)`. At the center $d_r=0$ (reflection parity), so $N(0)=0$ and, with $z=s$ arclength,
$$F'(0)=Z(0)=\int_{S^1}\rho(d')^2\,ds\ \overset{(\rm ii),\,e=0}{\ge}\ 12\int\rho\,ds,$$
matching `center_slope`. This uses (ii) directly; the $\delta$-perturbed version is $\ge(12-8\delta)\int\rho$.

## (v) Single Fourier mode on the expanding flat cusp

The reduced equation $\psi''+3\psi'-k^2e^{-2t}\psi=0$ with $x=ke^{-t}$ ($\tfrac{d}{dt}=-x\tfrac{d}{dx}$) becomes $\psi_{xx}-\tfrac2x\psi_x-\psi=0$, with independent solutions $e^x(x-1)$ and $e^{-x}(x+1)$ (I verified both). The reflection-normalized combination
$$\psi(x)=\frac{e^{x-k}(x-1)+e^{k-x}(x+1)}{2k}$$
satisfies $\psi(x{=}k)=1$ and $\psi_x(k)=\tfrac{x}{2k}(e^{x-k}-e^{k-x})|_{x=k}=0$, i.e. $\psi(t{=}0)=1,\ \psi'(0)=0$. Both checks pass. Its limit is
$$\psi(x\to0)=\frac{e^k-e^{-k}}{2k}=\frac{\sinh k}{k},$$
and I reproduced the tabulated factors ($1.17520,1.81343,3.33929,14.84064,186.30985$ for $k=1,2,3,5,8$). The identity $(e^{3t}\psi')'=k^2e^t\psi$ follows from the equation and is the reduction of $\operatorname{div}_\gamma(\rho\nabla d)=0$ with base $\gamma=dt^2+e^{2t}dz^2$, orbit weight $\rho=e^{2t}$ (the $e^{3t}=e^{2t}\cdot\sqrt\gamma$ combines orbit weight and base measure — the measures are correctly assembled).

**Asymptotic derivative.** Expanding near $x=0$: $\psi_x\approx-\tfrac{\sinh k}{k}x$, so $\psi'=-x\psi_x\approx k\sinh k\,e^{-2t}\to0$. The unweighted radial derivative decays like $e^{-2t}$.

**Weighted pairing and normalized decay.** The mode’s energy density is $e^{3t}\psi'^2+k^2e^t\psi^2$; the second term dominates, growing like $\sinh^2k\,e^{T}$, and equals the boundary covariance $F(T)=e^{3t}\psi'\psi\sim k\sinh k\,e^{T}$ (both grow as $e^{T}$, consistent). The cusp volume $\int_0^T e^{3t}dt\sim\tfrac13e^{3T}$ grows faster, so the **normalized** (per-volume) anisotropy energy decays as
$$\frac{\text{energy}}{\text{volume}}\sim 3\sinh^2k\;e^{-2T}\to0.$$

**Frequency behavior.** The transfer $\psi(0)=1\mapsto\psi(\infty)=\sinh k/k$ grows exponentially in $k$. A single reflection-normalized mode cannot be simultaneously reflection-even at the center and flat at infinity (that would need $\psi(\infty)=0$, impossible for the reflected solution). Hence Neumann–Dirichlet uniqueness at one fixed $k$ carries no inverse bound uniform in $k$; the mode-transfer map is not bounded below across frequencies in the unweighted norm.

## Sharp center-acceleration identity (cross-check of §3.12)

I re-derived $\langle S'(0)v,v\rangle\le(e-3)-E_{vv}=E_{11}+E_{22}-E_{nn}-3\le-3+3\delta$ using $e=E_{vv}+E_{11}+E_{22}-E_{nn}$; the $E_{vv}$ cancels exactly, giving $\lambda_{\min}(S'(0))\le-3+3\delta$. The steps `K_orb\ge3-e/2`, `(Ric_q+3q)(v,v)=e/2-K_orb\le e-3`, and $-\det A=\tfrac12|A_0|^2$ at a downward zero all check. The §4 numerics approaching max sectional curvature $3.033$ from above are consistent with the sharp floor $3$ (illustration, not attainment proof, as stated).

## What the chain forces — and what it does not

**The synthesis does not establish a positive lower bound on the maximum Ricci defect $\|E\|_{\rm op,\infty}$.** What it rigorously establishes is:

1. an integral center-energy floor — normalized center anisotropy energy $\ge 12-8\delta$ (part ii), an unavoidable order-one quantity at an exact or near-exact reflection center;
2. a zero-net-signed-flux transport structure (part iii) that channels this energy into a boundary covariance pairing (exact case) or a bulk source $-\rho(E_x-E_y)$ (forced case);
3. a nonnegative, order-one initial accumulation rate $F'(0)\ge(12-8\delta)\operatorname{Vol}$ (part iv).

**These are consistent with a feasible energy-dilution mechanism, not with a defect cost.** The exact single mode (part v) shows one can carry the full center anisotropy to infinity with $E\equiv0$, the per-volume energy decaying like $e^{-2T}$, terminating in a nonzero-anisotropy conformal-infinity profile $(\sinh k/k)\cos kz$. The Step 73 adiabatic tail then removes that residual boundary anisotropy at cost $\|E\|_{\rm op,\infty}\le C(K^{-1}+K^{-2}+e^{-2r_0})\to0$ (I confirmed its leading fiber eigenvalue $\tfrac32\max|\chi'|=45/16=2.8125$ against the tabulated $K\sup|E|\to2.8125$). So on present evidence the center-energy floor is an integral statement whose energy can be diluted; it is not converted into any pointwise defect lower bound.

**Assumptions that would turn this into a defect cost.** One would need an inverse/coercivity estimate for the transport operator (and the full nonlinear five-component system with Hamilton/momentum constraints) that is uniform in the physical radius $R$ and in the cusp degeneration, relating $F'(r)$ or the bulk source to $\|E\|_{\rm op,\infty}$ at a fixed physical scale. Part (v) shows the linearized mode-transfer is not bounded below uniformly in frequency in the unweighted norm ($\sinh k/k$ amplification), so any such estimate must be posed in the correct weighted ($\rho$) measure and cannot descend from a single fixed mode. No such uniform estimate is present, and the normal balance $e^{2R}\eta+\tfrac\delta2(e^{2R}-1)\ge3$ only forces the physical length to grow as $\delta\to0$; it supplies no upper length bound and hence no positive-thickness statement for a defect region.

**Assumptions that would turn this into a construction.** One would need: (a) nonlinear existence of the core-entry interface from the totally-geodesic center to a large expanding almost-umbilic slice with $\|E\|_{\rm op,\infty}\to0$ — the §5 searches stalled near $\|E\|_{\rm op}\sim16$–$24$ with no decay in $R$, which the elliptic-unstable Cauchy character renders inconclusive either way; (b) control of $e^{-2a}\|\operatorname{Ric}(q_r)\|$ during expansion (the source damping in the traceless equation $P'+3a'P=e^{-2a}\operatorname{Ric}(q_r)^\circ$), which expansion alone does not guarantee; (c) full jet matching at the tail attachment; and (d) resolution of the constraint-propagation issue flagged in Step 73 §5 — the three-equation elliptic block $2(\tau^2+\xi^2)^3$ does not by itself close $E_{tt}-E_{zz}=0$ and $E_{tz}=0$, so any BVP must solve full Einstein–DeTurck and remove the DeTurck field or prove propagation of the Hamilton/momentum components.

**Net reading.** The center-energy/transport identities are internally correct and physically well-measured, and they sharpen the picture considerably: the order-one center anisotropy is real and lattice-invariant, its transport is flux-neutral and covariance-carried, and the single mode plus the tail exhibit an explicit dilution channel. But the chain as it stands demonstrates feasibility of dilution rather than a Ricci-defect cost; the decisive missing element on the cost side is a weighted, degeneration-uniform inverse estimate, and on the construction side the nonlinear core-entry existence with constraint propagation. Both remain open, and (per the notes) even a completed negative construction settles only the normalized negative branch in dimension four, leaving the positive branch and the higher-dimensional quantifiers of Yau 26 outstanding.