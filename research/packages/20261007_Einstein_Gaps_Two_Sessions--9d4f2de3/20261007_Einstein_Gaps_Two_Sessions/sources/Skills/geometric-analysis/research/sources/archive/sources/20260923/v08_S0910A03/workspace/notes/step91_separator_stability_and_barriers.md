# Step 91: Separator stability, flat-slice barrier, and toral BH equivalence

Session `S0910A03`, Agent2 / Execute.

> **Corrects Step 90 §8:** the proposed radial cylindrical throat is blocked by the
> flat-slice barrier (δ ≥ 3/2 required). The resolvent-floor combination does NOT
> independently constrain Q_C; the ceiling rises faster than the floor with Q.
>
> **Step 92 sign correction:** §8 below originally reversed the contracted Gauss
> sign and confused a minimal slice \(\mathcal H=0\) with a stationary value
> \(\partial_r\mathcal H=0\). The correct identity is
> \(R(q)=-6+D+\mathcal H^2-|\mathrm{II}|^2\). Thus at a minimal slice
> \(R(q)\le-6+4\delta\), and tangential orbit energy helps furnish the required
> negative intrinsic curvature. The supposed positive-curvature conflict is
> withdrawn. Sections 1--7 remain valid; Step 92 replaces §8 with the full
> weighted Jacobi-form analysis.

## 1. Flat-slice barrier kills the radial cylindrical throat

For the cohomogeneity-one charged metric
\[
 g=dr^2+\psi(r)^2d\theta^2+e^{\sigma+\alpha}(d\xi_1+Pd\theta)^2+e^{\sigma-\alpha}d\xi_2^2,
\]
each constant-\(r\) slice is a flat \(T^3\): all coefficients are independent of
\((\theta,\xi_1,\xi_2)\), giving a left-invariant metric on an abelian group.
Hence
\[
 R(q_r)=0.
\tag{1.1}
\]
The contracted Gauss equation gives
\[
 H^2-\operatorname{tr}(S^2)=6-D,\qquad |D|\le4\delta,
\tag{1.2}
\]
and Cauchy–Schwarz for the 3 eigenvalues of \(S\) gives
\(\operatorname{tr}(S^2)\ge H^2/3\), hence
\[
 \boxed{H^2\ge9-6\delta.}
\tag{1.3}
\]
A cylindrical base with two outward-expanding ends has \(H\to\pm3\) at the
respective ends, so smooth interpolation requires \(H=0\) somewhere. But
(1.3) prevents this for \(\delta<3/2\). The connection charge, orbit
anisotropy, discharge control, and sign-changing forcing are all irrelevant:
the barrier is topological (slice flatness) and applies to any radial metric
whose level sets are flat tori.

**The Step 90 radial cylindrical throat program is therefore unnecessary.** The
disk cap avoids the barrier because \(\psi(0)=0\); the angular circle collapses,
allowing \(H\to+\infty\) near the polar center without passing through \(H=0\).

Verified: `workspace/scripts/step91_flat_slice_and_stability.py`,
`workspace/data/step91_flat_slice_and_stability.json`.

## 2. Twist enters the second fundamental form

For the free \(T^2\)-invariant metric
\[
 g=\gamma_B+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),
\]
the O'Neill A-tensor for horizontal lifts \(\bar T,\bar\nu\) is
\[
 2g(\nabla_{\bar T}\bar\nu,K_a)
 =g(K_a,[\bar T,\bar\nu])
 =-\varepsilon G_{ab}f^b,
\]
where \(\varepsilon=\operatorname{vol}_{\gamma_B}(T,\nu)\). Hence
\[
 \operatorname{II}(\bar T,K_a)=-\frac\varepsilon2G_{ab}f^b.
\tag{2.1}
\]
In the orbit-orthonormal frame \(e_\alpha=K_\alpha/\sqrt{G_{\alpha\alpha}}\),
\[
 \operatorname{II}(\bar T,e_\alpha)
 =-\frac\varepsilon2\sqrt{G_{\alpha\alpha}}f^\alpha.
\]
The symmetric tensor norm counts both orderings, so
\[
 \boxed{
 |\mathrm{II}|^2_{\rm twist}
 :=2\sum_\alpha\mathrm{II}(\bar T,e_\alpha)^2
 =\frac12G_{ab}f^af^b=Q.}
\tag{2.2}
\]
The other components are twist-independent:
\(\mathrm{II}(T,T)=\pm\kappa\) and the orbit block is
\(|S_\nu|^2=\frac12h_\nu^2+\frac12e_\nu\). Thus
\[
 \boxed{
 |\mathrm{II}|^2
 =\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q.}
\tag{2.3}
\]
Twist does not enter the mean curvature \(H=-\kappa+h_\nu\).

TTCS-verified derivation: Koszul formula and full O'Neill computation in
`trace/ttcs/results/step91_ttcs01_verifier1_integration.md`.

## 3. Separator stability: \(Q_C\le3+\delta\)

For a compact two-sided stable minimal hypersurface \(\Sigma^3\subset(X^4,g)\),
the second variation with \(\phi\equiv1\) gives
\[
 \int_\Sigma\bigl(|\mathrm{II}|^2+\operatorname{Ric}(\nu,\nu)\bigr)\,d\mu\le0.
\tag{3.1}
\]
Since \(\operatorname{Ric}(\nu,\nu)=-3+E(\nu,\nu)\ge-3-\delta\),
\[
 \boxed{\langle|\mathrm{II}|^2\rangle_\Sigma\le3+\delta.}
\tag{3.2}
\]
Substituting (2.3):
\[
 \boxed{
 \left\langle\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q\right\rangle_C
 \le3+\delta.}
\tag{3.3}
\]
In particular, the separator-averaged twist energy is bounded:
\[
 \boxed{Q_C:=\langle Q\rangle_C\le3+\delta.}
\tag{3.4}
\]
And the normal orbit energy:
\[
 \boxed{\langle e_\nu\rangle_C\le6+2\delta-2Q_C.}
\tag{3.5}
\]

**Note on minimality:** The Step 88 separator is a \(\rho^2\gamma_B\)-geodesic
whose invariant lift minimizes \(\int_C\rho\,ds\) among essential curves. The
constant normal variation \(\phi=1\) is invariant, so the weighted-length
minimizer already suffices for (3.1). Full homological area minimization is not
required.

## 4. The raised separator floor

The separator identity from Step 88 is
\[
 \langle e_s\rangle_C
 =12-2\langle D\rangle_C+2\langle|\mathrm{II}|^2\rangle_C
  +\langle h_T^2\rangle_C,
\tag{4.1}
\]
where \(h_T=(\log\rho)_T\) and \(|D|\le4\delta\). With (2.3):
\[
 \langle e_s\rangle_C
 =12-2\langle D\rangle_C
 +2\langle\kappa^2\rangle+\langle h_\nu^2\rangle+\langle e_\nu\rangle
 +2Q_C+\langle h_T^2\rangle.
\tag{4.2}
\]
All non-\(D\) terms are nonnegative, hence
\[
 \boxed{\langle e_s\rangle_C\ge12-8\delta+2Q_C.}
\tag{4.3}
\]
Twist raises the energy floor by exactly \(2Q_C\). The coefficient \(2\) is exact.

## 5. The resolvent-floor combination does NOT constrain \(Q_C\)

An initial analysis (script output) suggested that combining (4.3) with the
Step 87 OT ceiling \(\mathcal B(\delta)\) would force \(Q_C\approx0\) near
\(\delta_*\). TTCS verification corrected this: the ceiling
\(\mathcal B(\delta)\) was derived under \(Q=0\), and with \(Q>0\) the modified
ceiling grows faster than the floor.

Specifically, the Step 90 three-parameter comparison reads
\[
 12+2Q_C-8\delta
 \le
 \left[
 \frac{2(Q_++2\delta)}{\sqrt{3-Q_-+\delta}}
 +\sqrt{2(3-Q_-+\delta)+\frac{5(Q_++2\delta)^2}{3-Q_-+\delta}}
 \right]^2.
\tag{5.1}
\]
With exact OT ends, \(Q_-=0\), but \(Q_+\ge Q_C\). Near
\((\delta_*,Q_+)=(\delta_*,0)\):
\[
 \frac{\partial\mathcal B_{\rm tw}}{\partial Q_+}\bigg|_{(\delta_*,0)}
 \approx8.86,
 \qquad
 \frac{\partial\text{floor}}{\partial Q_C}=2.
\tag{5.2}
\]
Even under the most favorable identification \(Q_+=Q_C\), the ceiling outpaces
the floor. The resolvent with variable twist therefore does not independently
bound \(Q_C\). The only established twist constraint at the separator is
stability:
\[
 \boxed{Q_C\le3+\delta.}
\]

A stronger relation would require either an upper \(e\)-estimate expressed
directly through \(Q_C\) (not \(Q_+\)), or a geometric transport theorem
connecting \(Q_+\) to \(Q_C\).

## 6. Toral black-hole coordinate equivalence

Starting from the diagonal metric
\[
 g=dr^2+f(r)^2d\varphi^2+a(r)^2(dx^2+dy^2)
\]
(for example, the toral black-hole metric with
\(f^2=s^2-a_0/s,\;a^2=s^2\)), the coordinate change
\(\varphi=\theta+kx\) gives
\[
\begin{aligned}
 &G_{xx}=k^2f^2+a^2,\quad G_{yy}=a^2,\\
 &A_\theta^x=\frac{kf^2}{k^2f^2+a^2},\quad
 \psi^2=\frac{f^2a^2}{k^2f^2+a^2}.
\end{aligned}
\tag{6.1}
\]
Verified: all residuals zero in symbolic computation.

At large cusp distance (\(f\sim s,a\sim s\)):
\[
 \alpha\to\frac12\log(1+k^2)=\text{const},
\]
so the orbit anisotropy is just the rotated torus identification — not new
curvature. Near the horizon (\(f\to0\)):
\(\alpha\to0,\;A_\theta\to0,\;Q\to0\).

**The "rapid \(Q\) redshift" observed in the Step 90 radial core is this
coordinate rotation:** a large initial \(Q_0\) reflects the angle between the
chosen torus subgroup and the natural flat torus of the cusp, not a genuine
curvature production mechanism.

## 7. Summary of established constraints at the separator

For a free \(T^2\)-invariant metric with two outward-expanding complete ends
and \(\|\operatorname{Ric}+3g\|_{\rm op}\le\delta\):

| Quantity | Bound | Source |
|----------|-------|--------|
| \(Q_C\) | \(\le3+\delta\) | Stability (§3) |
| \(\langle\kappa^2\rangle+\frac12\langle h_\nu^2\rangle+\frac12\langle e_\nu\rangle\) | \(\le3+\delta-Q_C\) | Stability (§3) |
| \(\langle e_s\rangle_C\) | \(\ge12-8\delta+2Q_C\) | Floor identity (§4) |
| \(\langle e_\nu\rangle_C\) | \(\le6+2\delta-2Q_C\) | Stability (§3) |
| \(\sup e\) | \(\ge12-8\delta+2Q_C\) | Floor + \(e\ge e_s\) |

Without twist (\(Q=0\)):
- The OT resolvent gives \(\sup e\le\mathcal B(\delta)\), contradicting the
  floor for \(\delta<\delta_*=0.2462\ldots\).

With twist (\(Q>0\)):
- Floor rises by \(2Q_C\), but ceiling rises faster with \(Q_+\). No
  contradiction from existing estimates.
- Q_C is bounded by stability but Q_+ (the interior maximum) is not.
- Step 90 radial core shows local exact solutions with arbitrary finite Q_0.
- The flat-slice barrier prevents radial cylindrical interpolation for δ < 3/2.

The next frontier is genuinely z-dependent geometry where R(q_r) ≠ 0 and the
Bochner identity, Maxwell conservation, stability, and slice geometry interact
in the full coupled system.

## 8. Correct intrinsic interpretation and the full stability form

Use arclength \(s\) along the separator curve \(C\subset(B,\gamma_B)\), and put
\(h=\partial_s\sigma\). The intrinsic scalar curvature is
\[
R(q)=-2\partial_sh-\frac32h^2-\frac12e_s.
\tag{8.1}
\]
For a general hypersurface with mean curvature \(\mathcal H\), contracted Gauss is
\[
R(q)=-6+D+\mathcal H^2-|\mathrm{II}|^2,
\qquad D=\operatorname{tr}E-2E(\nu,\nu).
\tag{8.2}
\]
At the minimal separator \(\mathcal H=0\), therefore
\[
R(q)=-6+D-|\mathrm{II}|^2\le-6+4\delta.
\tag{8.3}
\]
This sign agrees with the exact Koiso totally geodesic center
\(R(q)=-6\). The term \(-e_s/2\) in (8.1) supplies, rather than opposes, the
negative intrinsic curvature required by (8.3). The earlier discussion of a
positive-curvature turning requirement was false. Also,
\(\mathcal H=0\) is not the condition \(\partial_r\mathcal H=0\).

The stronger retained statement is stability for every smooth periodic
invariant normal speed \(\phi(s)\):
\[
\boxed{
\int_C\rho\left(\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q\right)\phi^2ds
\le
\int_C\rho\left[(\partial_s\phi)^2+(3-E(\nu,\nu))\phi^2\right]ds.}
\tag{8.4}
\]
The constant test gives only §3. Formula (8.4) is the nonnegativity of a
one-dimensional weighted Jacobi operator, so it controls localized
concentration through capacity rather than furnishing a pointwise bound or a
universal concentration length. Step 92 investigates its coupling to (8.1)
and to Maxwell charge transport.

## 9. Supersession

- Step 90 §8 and route map: remove the proposed cylindrical charged throat
  program; it is blocked by the flat-slice barrier.
- Step 91 JSON field `step87_ceiling: 12.0` is incorrect; the actual value at
  δ = 0.246 is ≈10.025.
- The script's "OBSTRUCTED" labels in the Q_C_max table are valid only for
  Q = 0 (already known from Step 87). They should NOT be read as constraints on
  Q_C when twist is present.
- The original §8 positive-curvature interpretation and the corresponding
  Step 91 handoff are superseded by (8.1)--(8.4): at a minimal separator the
  required scalar curvature is negative, not positive.
