# Step 67 — Q4: nondegenerate torsion zeros survive the order-six compatibility

Agent3, Execute. This note supersedes the universal-obstruction interpretation in `step66_order6_obstruction.md`. It does not supersede the first-jet cone/index theorem, the higher-order GH leading classification, or the compact zero-surface results.

## 1. Corrected mathematical conclusion

Let 
\[
E(g)=\operatorname{Ric}(g)-\lambda g,
\]
and work in Darboux coordinates with fixed standard symplectic form, 
\[
g=e^H,\qquad H^T=H,\qquad HJ_0+J_0H=0,\qquad H=\sum_{d\ge2}H_d.
\]
This parametrization satisfies compatibility and closure identically. A torsion zero occurs at the origin because $H=O(|x|^2)$. Its first torsion derivative is
\[
f(z,\bar z)=cz+(S+A)\bar z,
\]
subject to the established cone
\[
\|A\|^2=\|S\|^2+8|c|^2.
\]
Every nondegenerate cone point has
\[
\det_{\mathbb R}Df=9|c|^4+|\det(S+A)|^2>0,
\]
so its local Brouwer index is $+1$.

A02's revised Step-80 calculation constructs explicit real coefficient arrays $H_2,\dots,H_8$ for which $E_0,\dots,E_6$ are small, including two negative-Einstein cases with $\lambda=-5$ and nondegenerate $Df$. A01 independently re-evaluated those arrays, then pulled them into its separate general $(g,\omega)$ equation engine. The best example, `recon_F012_gen5_lam-5`, gives
\[
\det Df=0.02337291736636084,
\qquad \Phi_6=-0.41612425938887987,
\]
with Darboux-gauge degree-six Einstein residual $7.69\times10^{-9}$ and independent pulled-back-system norm $8.44\times10^{-9}$. Thus there is no universal real obstruction at $E_6$ to a nondegenerate torsion zero. The earlier conjecture that all AKE torsion zeros must be degenerate is unsupported and is withdrawn.

This is a floating finite-jet result. It does not prove an exact finite jet, all-orders formal integrability, convergence to an analytic germ, or a closed strictly almost-Kähler Einstein manifold.

## 2. Order-six reduction and reconstruction

The degree count is
\[
E_k=L_kH_{k+2}+\mathcal N_k(H_2,\dots,H_{k+1}).
\]
With $H_2,H_3$ fixed, solve $E_1,\dots,E_5=0$ affinely:
\[
u=u_0+Ny,\qquad u=(H_4,H_5,H_6,H_7).
\]
Modulo the image of $L_6$ acting on $H_8$, the remaining equations are exactly quadratic:
\[
\Psi(y)=c+Jy+\frac12H[y,y].
\]
For generic strict-cone data in the computed even branch, there are 35 nontrivial rows. The joint quadratic range has dimension 12 and 34 rows are absorbed linearly; one scalar remains. Writing $y=Pz+Kw$ gives
\[
\phi(z)=c_\pi+j^Tz+\frac12 z^TH_\pi z.
\]
When $H_\pi>0$,
\[
\Phi_6=c_\pi-\frac12j^TH_\pi^{-1}j.
\]
A real root exists exactly when $\Phi_6\le0$ within this reduced stratum. For $\Phi_6<0$ the scalar root is transverse, so finite-order solvability is numerically robust under small perturbations of the reduced data. Equality is a singular case.

The order dictionary must not be shifted incorrectly:

| Einstein coefficient | highest metric jet | scalar-compatibility Taylor degree | number of scalar coefficients |
|---|---:|---:|---:|
| $E_2$ | $H_4$ | 0 | 1 |
| $E_4$ | $H_6$ | 2 | 10 |
| $E_6$ | $H_8$ | 4 | 35 |
| $E_8$ | $H_{10}$ | 6 | 84 |

Thus differentiating the Step-65 scalar identity twice pertains to the already studied $E_4$ level. The new $E_6$ quantity comes from the quartic Taylor coefficient after eliminating 34 adjustable directions. The numerically universal functional on degree-six Ricci coefficients is plausibly the $U(2)$-invariant radial double trace of that quartic scalar compatibility, not a bare $|\nabla^3\Omega|^2$ term.

## 3. Independent verification

### 3.1 Direct coefficient evaluation

`workspace/scripts/step67_verify_A02_reconstruction.py` loads only the saved arrays and conventions, rebuilds the truncated Einstein operator, and checks the cone and scalar quadratic. Its output is `workspace/data/step67/verify_A02_step80_reconstructions.json`.

| case | $\lambda$ | $\det Df$ | $\Phi_6$ | $\|E_6\|$ | status at $E_6$ |
|---|---:|---:|---:|---:|---|
| gen2 | 0 | 0.0166186352 | -0.165278514 | $6.16\times10^{-8}$ | reconstructed |
| gen2 | -5 | 0.0166186352 | -0.236911608 | $1.25\times10^{-7}$ | reconstructed |
| gen5 | -5 | 0.0233729174 | -0.416124259 | $7.69\times10^{-9}$ | reconstructed |
| lsA jet0 | -1 | 0.0501890418 | +0.841909980 | 4.64 | positive control fails |

For all three reconstructed examples, the cone residual is below $3\times10^{-16}$ and the saved scalar root has $|\phi(z)|<10^{-15}$. The metric coefficients are large (for gen5, $\|H_8\|\approx5.85\times10^5$), so this is not a validated exact result; cancellation and conditioning must be retained in its interpretation.

### 3.2 Cross-representation evaluation

`workspace/scripts/step67_convert_darboux_to_normal.py` applies a polynomial coordinate pullback and evaluates the resulting $(g,\omega)$ jet with A01's independent `step62_zero_prolong` equations, which separately impose
\[
\omega^Tg^{-1}\omega=g,\qquad d\omega=0,\qquad \operatorname{Ric}=\lambda g.
\]
The pullback residuals reproduce the sign distinction:

* gen2, $\lambda=0$: total norm $6.73\times10^{-8}$;
* gen2, $\lambda=-5$: $1.41\times10^{-7}$;
* gen5, $\lambda=-5$: $8.44\times10^{-9}$;
* positive control: $4.78$.

The converted torsion convention satisfies
\[
\det(\mathrm{Mvec})=16\det Df,
\]
and each negative example again satisfies the Step-62 cone to about $2\times10^{-14}$ in the independent sector basis. This is the strongest current cross-check.

Correction: the map constructed by the current script is an invertible point-normal polynomial germ but not a proved geodesic exponential map. Its recursion uses $\Gamma(X)y y$ instead of $\Gamma(X)(\mathcal RX)(\mathcal RX)$ and therefore omits velocity corrections beginning generically at coordinate degree five. The coordinate pullback and tensor evaluation remain valid; only the stronger “geodesic-normal” description is withdrawn.

## 4. The order-six law is sign-changing

The earlier Step-80 prose initially asserted $F_0>0$ and $F_2<0$. The completed `F012` scan disproves both. On the computed regular slice,
\[
\Phi_6=F_0+\lambda F_1+\lambda^2F_2,
\]
and all $F_i$ take both signs on sampled strict-cone jets. In particular, gen2 has $F_0=-0.16528$ and $F_2>0$, while many other jets have $F_0>0$ and $F_2<0$.

Let
\[
N=4|c|^2+2\|S\|^2+2\|A\|^2.
\]
Under jet dilation, $(c,S,A,\lambda)\mapsto\mu^2(c,S,A,\lambda)$, hence $N\mapsto\mu^4N$ and $\Phi_6\mapsto\mu^8\Phi_6$. The scale-invariant curvature/torsion ratio is therefore
\[
\Lambda=\frac{\lambda}{\sqrt N},
\]
not $\lambda/N$. The invariant law has the form
\[
\Phi_6=N^2\bigl[\phi_0(X)+\Lambda\phi_1(X)+\Lambda^2\phi_2(X)\bigr],
\]
where $X$ denotes angular data on the normalized cone. A single torsion magnitude or $|c|^2$ fraction cannot determine the sign; relative phases and the singular values of $S$ matter.

The reduction is a critical value, so rational invariant dependence is natural:
\[
\Phi_6=c_\pi-\frac12j^TH_\pi^{-1}j.
\]
Polynomial sign guesses are therefore especially unreliable near rank-changing strata.

## 5. Candidate invariant multiplier

The observed universal row has a concrete flat-symbol candidate. For anti-$J$ symmetric metric variations $h$, the scalar symbol
\[
P_\xi(E)=E(J\xi,J\xi)-\frac12|\xi|^2\operatorname{tr}E
\]
annihilates the flat linearized Ricci image modulo contracted-Bianchi relations. Applying it to $E_6$ produces a homogeneous quartic scalar polynomial. Its unique radial $U(2)$-invariant coefficient is extracted by double trace:
\[
\ell(E_6)\stackrel{?}=C\,\Delta_0^2\left[J^i{}_aJ^j{}_b\partial_a\partial_bE_{ij}
-\frac12\Delta_0\operatorname{tr}E\right]_{0}.
\]
This formula has the correct weight and explains why one universal row can survive. `workspace/scripts/step67_multiplier_candidate.py` performed the first direct coefficient comparison. The raw candidate with trace coefficient $-1/2$ has cosine $0.97637$ with the saved 840-vector $\ell$; optimizing the two displayed invariant coefficients gives ratio $-0.52856$ and cosine $0.97730$ (`workspace/data/step67/multiplier_candidate.json`). This strong but nonexact agreement shows that the radial $U(2)$ scalar is close to the surviving row, while the remaining $21.3\%$ normalized component must be explained by contracted-Bianchi representatives, coefficient-pairing conventions, or an omitted invariant symbol. The candidate is not yet identified. The geometric counterpart remains the quartic coefficient of the Step-65 exact $\Delta q$ identity after lower equations are eliminated.

## 6. Consequences for the closed Goldberg problem

The local picture now has three distinct sectors:

1. nondegenerate first-order zeros, compatible through $E_6$ on an open sampled region and carrying index $+1$;
2. rank-deficient first-order zeros, including zero-surface models;
3. higher-order zeros $m\ge2$, whose leading term is $\kappa\bar z_2^m e_1$.

The topological charge $c_2(E)[M]=5\chi+6\tau>0$ can therefore still be carried naturally by nondegenerate positive-index zeros. It is false that finite-order compatibility has forced all charge into degenerate geometry. At an isolated degenerate zero the Brouwer degree remains defined through $f/|f|$ on a linking $S^3$; only the Jacobian-sign shortcut fails.

No current compact identity supplies a lower bound on $N$ at an isolated zero or forces $\Lambda$ and the cone-shape parameters into a prohibited subset. The first-jet cone is independent of $\lambda$, index has no magnitude information, and integral curvature control does not control isolated pointwise derivatives. Therefore the sign-changing order-six law is presently a local structural constraint, not a closed-manifold obstruction.

## 7. Next local and global work

The next new even local level is $E_8$, requiring coefficients through $H_{10}$. The gen5, $\lambda=-5$ jet is the best base point because it has the largest negative margin, smallest reconstructed coefficients, and best two-representation residual. One must vary the full lower-order family, especially the kernel part of $H_8$; failure of one minimum-norm representative would not be an obstruction. Conversely, a full-rank projected derivative without an actual root would not establish extension. Odd lower data must remain available before making a universal statement.

Before a large $E_8$ calculation, two smaller exact tasks have high value:

1. identify the saved universal multiplier exactly: resolve the observed cosine $0.97730$ by projecting modulo the explicit contracted-Bianchi row space and checking coefficient-pairing conventions, then use rational reconstruction;
2. use rank-revealing range/nullspace decompositions to certify the $E_6$ reconstruction and remove numerically inflated $H_8$ components.

The tubular AAD transport along a zero surface remains an independent global route. It is not replaced by the nondegenerate branch. The full closed Goldberg question still requires either all-orders/local realization plus compact assembly, or a genuinely global identity that prevents the locally admissible zeros from assembling on a closed negative-Einstein manifold.
