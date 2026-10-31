# Step 12: Taub--NUT--AdS accessibility calibration and repaired chart mechanism

Session: S0910A01. Phase: Execute.

## 1. Purpose

Step 11 correctly separated the local Derdziński obstruction from the source of harmonic charts, and it correctly identified the Pontryagin density of the calibrated bulk as structurally important.  Two later corrections change the execution target.

First, the Taub--NUT--AdS example does not close the fixed-scale cover question.  The universal cover of a large ball containing the NUT does not unwrap the short Hopf circle, but the accessibility question is existential in the buffered domain: one may first choose a smaller annular neighborhood avoiding the NUT and then take its cover.  On that smaller domain the circle survives and unwraps.

Second, the Pontryagin density in an actual near-critical LeBrun sequence is not hidden in tiny NUT cores.  The near-equality estimates force it to be close in mean to a positive constant on the whole volume.  The topological charge is therefore distributed over the calibrated bulk; any local Chern--Simons description is a boundary-flux representation of diffuse connection curvature, not an integer count of small cores.

This note records an independent coordinate computation of the Taub--NUT--AdS curvature, the multiscale consequences, and the repairs needed in the chart-accessible proof mechanism.

## 2. Coordinate curvature computation

The metric is
\[
 g_\nu={dr^2\over F_\nu}+(r^2-\nu^2)(d\theta^2+\sin^2\theta\,d\phi^2)
 +4\nu^2F_\nu(d\psi+\cos\theta\,d\phi)^2,
\]
\[
 F_\nu={r-\nu\over r+\nu}\left(1+{(r-\nu)(r+3\nu)\over3}\right),\qquad r\ge\nu.
\]
I wrote `workspace/scripts/step12_taub_nut_ads_coordinate_curvature.py`, which computes Christoffels, Riemann, Ricci, scalar curvature, the curvature-operator blocks on \(\Lambda^2_\pm\), and the calibrated defect directly from the coordinate metric.  This avoids the incomplete Bianchi IX formulas used in Step 11.

At \(\nu=0.01,r=0.5,\theta=\pi/2\), the run

```text
PYTHONDONTWRITEBYTECODE=1 python workspace/scripts/step12_taub_nut_ads_coordinate_curvature.py --nu 0.01 --r 0.5 --table
```

returned
\[
\operatorname{Ric}_{\mathrm{ON}}=-I+O(10^{-15}),\qquad s=-4,
\]
\[
W^+=0+O(10^{-15}),
\]
while the opposite half has eigenvalues
\[
(-0.150751470651,-0.150751470651,0.301502941302).
\]
The Hilbert--Schmidt norm squared of that nonzero half is \(0.136356035421\), agreeing with one quarter of the four-index Weyl norm squared
\[
 |W|^2_{(0,4)}={32\nu^2(4\nu^2-3)^2\over3(r+\nu)^6}.
\]
For \(\nu=0.01,r=0.5\), this formula gives \(0.545424141683\), and \(0.545424141683/4=0.136356035421\).  As an independent symbolic check I also ran S0910A03's exact script `Sessions/S0910A03/workspace/scripts/compute_taub_nut_ads_curvature.py`; it returned `Ric+g=0`,
\[
 |W|^2_{(0,4)}={32\nu^2(4\nu^2-3)^2\over3(r+\nu)^6},
\]
\[
W^+=0,
\qquad
\operatorname{Spec}(W^-)=\left({2\nu(4\nu^2-3)\over3(r+\nu)^3},{2\nu(4\nu^2-3)\over3(r+\nu)^3},{-4\nu(4\nu^2-3)\over3(r+\nu)^3}\right),
\]
and
\[
E^W_\nu(R)={32\pi^2(R-\nu)^2(4\nu^2-3)^2(R^2+6R\nu+17\nu^2)\over9(R+\nu)^4}.
\]

Thus, in the coordinate orientation used by the script and by S0910A03,
\[
 W^+\equiv0,
\]
and the LeBrun calibrated density built from that \(W^+\) is exactly
\[
(s+8\sqrt6|W^+|)^2=16,
\]
with \(E=0\) and \(G=0\).  This exact value is not a small positive core cost; it is a macroscopic scalar--Weyl defect on every annular region in that orientation.

Reversing orientation places the nonzero half into \(W^+\).  For small \(\nu\), its spectrum has two negative eigenvalues and one positive eigenvalue:
\[
\left(a,a,-2a\right),\qquad
 a={2\nu(4\nu^2-3)\over3(r+\nu)^3}<0.
\]
At the shell where its norm equals the calibrated magnitude \(|W^+|^2=1/24\), the sign pattern is not the calibrated LeBrun pattern \((-1/6,1/12,1/12)\).  The completed tensor density remains positive; the script gives \(F=35/36\) up to numerical roundoff at that shell.

## 3. Multiscale behavior of the NUT model

I wrote `workspace/scripts/step12_taub_nut_ads_multiscale_calibration.py`, which saves:

- `workspace/data/step12_taub_nut_ads_multiscale.csv`
- `workspace/data/step12_taub_nut_ads_multiscale_summary.json`
- `workspace/figures/step12_taub_nut_ads_multiscale.png`

The exact complete-orbit radial volume density is
\[
 {dV\over dr}=32\pi^2\nu(r^2-\nu^2),
\]
and the cumulative full four-index Weyl energy from the NUT to radius \(R\) is
\[
E^W_\nu(R)={32\pi^2(4\nu^2-3)^2\over9}
 { (R-\nu)^2(R^2+6R\nu+17\nu^2)\over(R+\nu)^4}.
\]
Consequently
\[
E^W_\nu(\infty)\to32\pi^2.
\]
For fixed \(R>0\),
\[
\operatorname{Vol}\{\nu\le r\le R\}\sim {32\pi^2\over3}\nu R^3,
\]
so
\[
\fint_{\nu\le r\le R}|W|^2_{(0,4)}\sim {3\over\nu R^3}.
\]
The core-containing fixed-radius mean therefore diverges like \(\nu^{-1}\).  A large ball containing the NUT is not a good ball for any assumption controlling centered curvature means at all radii up to a fixed scale.

At a point at fixed distance from the NUT, an annular ball of radius below the distance to the NUT has \(|W|^2=O(\nu^2)\) and volume \(\Theta(\nu)\).  In the coordinate \(z=2\nu\psi\), the unwrapped annular geometry tends to
\[
 {dr^2\over1+r^2/3}+r^2d\Omega_2^2+(1+r^2/3)dz^2,
\]
real hyperbolic four-space with sectional curvature \(-1/3\).  It has \(W=0\), hence in the Step 12 coordinate orientation the calibrated defect is \(16\).  Such annular regions are actually accessible after choosing the smaller buffered domain; they fail to be calibrated, not accessible.

The radius where the opposite orientation has \(|W^+|^2=1/24\) satisfies
\[
 r_\nu\sim 576^{1/6}\nu^{1/3}=2\,3^{1/3}\nu^{1/3}.
\]
This tends to zero.  The cumulative Weyl energy from the NUT to \(r_\nu\) tends to \(32\pi^2\), while the volume is \(\Theta(\nu^2)\); the mean energy to that shell diverges like \(\nu^{-2}\).  It is not a fixed physical scale carrying the near-critical calibrated profile.

## 4. What the Taub--NUT model establishes

The correct conclusions are:

1. A large domain can kill the short Hopf fiber by including the NUT.  This shows that the cover of a prescribed large ball is not the same object as a cover chosen after selecting a smaller buffered annular domain.

2. Taub--NUT--AdS does not disprove adjustable-buffer cover accessibility.  Away from the NUT, the smaller annular domain unwraps the circle and has a smooth hyperbolic limit.

3. The standard NUT geometry is not a model for the calibrated good bulk.  Core-containing balls have divergent mean curvature energy; fixed annular unwrapped balls have macroscopic defect \(16\) in the coordinate orientation; the opposite-orientation magnitude shell collapses to scale \(\nu^{1/3}\) and has the wrong Weyl sign pattern.

4. A local integer-residue count is not the right first formulation for the global near-critical sequence.  The Chern--Weil density in the actual sequence is forced to follow volume.

## 5. Diffuse Pontryagin density in a near-critical LeBrun sequence

Let
\[
P_i=2|W_i^+|^2+{s_i^2\over24}-{1\over2}|E_i|^2.
\]
In the near-critical negative branch, \(\|g_i^{-1}\operatorname{Ric}_{g_i}+I\|_\infty\to0\), hence
\[
s_i\to-4\quad\text{in }L^\infty,
\qquad |E_i|\to0\quad\text{in }L^\infty.
\]
The completed-square remainder gives
\[
\fint_{M_i}\left(s_i+8\sqrt6|W_i^+|\right)^2\,d\mu_i\to0.
\]
Therefore
\[
|W_i^+|\to {1\over2\sqrt6}\quad\text{in mean square},
\]
and Cauchy--Schwarz gives
\[
|W_i^+|^2\to {1\over24}\quad\text{in }L^1\text{ mean}.
\]
Thus
\[
\fint_{M_i}\left|P_i-{3\over4}\right|\,d\mu_i\to0.
\]
With the normalized Chern--Weil representative
\[
\rho_{+,i}={1\over4\pi^2}P_i,
\]
we get
\[
\left\|\rho_{+,i}-{3\over16\pi^2}\right\|_{L^1\text{ mean}}\to0.
\]
For every measurable \(U_i\subset M_i\),
\[
\int_{U_i}\rho_{+,i}\,d\mu_i={3\over16\pi^2}\operatorname{Vol}(U_i)+o(A_i),
\]
where the error is bounded by the global \(L^1\) error, i.e. by \(o(\operatorname{Vol}M_i)=o(A_i)\).  This is a uniform absolute error for all measurable subsets, not a relative estimate on every small subset.  In particular, if \(\operatorname{Vol}(U_i)=o(A_i)\), then \(U_i\) carries only \(o(A_i)\) physical Pontryagin charge.  The order-\(A_i\) charge is already spread through the calibrated bulk.

This does not make the collapse basic.  On a regular collapsed region, if a comparison connection \(B\) on \(\Lambda^2_+\) is pulled back from a base of dimension at most three, then \(P(F_B)=0\) as a four-form and
\[
P(F_A)-P(F_B)=dT_P(A,B).
\]
For invariant rank-one circle collapse, writing
\[
F_A=F_H+\eta\wedge\Xi,\qquad \Xi=\iota_VF_A,
\]
one has
\[
P(F_A)=2\eta\wedge P(\Xi,F_H).
\]
If the horizontal curvature has bounded mean, the nonzero density above forces persistent mean \(|\Xi|^2\).  The surviving mechanism is diffuse non-basic mixed connection curvature: scaled holonomy, O'Neill tensors, nil commutators, or vertical frame twisting can in principle distribute the Chern--Simons flux through the bulk.

## 6. Repairs to the chart-accessible theorem

The Step 11 theorem remains valuable, but its proof should be read in the following repaired form.

### Controlled-chart forbidden germ

Fix a radius \(h>0\), an interior shrink factor \(0<\sigma<1\), and a harmonic-coordinate control package \(Q\) including \(Q^{-1}\delta\le(g_{ij})\le Q\delta\) and \(\|g_{ij}\|_{C^{1,\alpha}(B_h)}\le Q\).  There is \(\varepsilon_0(h,\sigma,Q)>0\) such that no sequence of smooth four-metrics on buffered domains can simultaneously satisfy:

- a harmonic coordinate chart of radius \(h\) with the fixed \(Q\) control and a compact interior ball \(B_{\sigma h}\Subset B_h\);
- \(\|g^{-1}\operatorname{Ric}+I\|_{L^\infty}\to0\);
- mean calibrated defect \(\fint F\to0\) on a smaller concentric ball.

The proof uses the supplied harmonic chart, not a new Cheeger--Naber conclusion.  The harmonic-radius control gives compactness in \(C^{1,\alpha'}\).  In harmonic coordinates,
\[
g^{ab}\partial_a\partial_b g_{ij}=-2\operatorname{Ric}_{ij}+Q(g^{-1},\partial g).
\]
Because \(\operatorname{Ric}=-g+e_i\) with \(e_i\to0\) in \(L^\infty\), and because the chart control makes the coefficients and the quadratic term compact in lower Hölder norms, interior elliptic estimates give strong finite-\(p\) \(W^{2,p}\) convergence on smaller balls.  The limit is a smooth Einstein metric with \(\operatorname{Ric}=-g\).  Since \(F_i\to0\) in \(L^1\), the limit has the calibrated constant spectrum.  Derdziński's local theorem then forces the limit metric itself to be locally Kähler, while \(\operatorname{Ric}=-g\) Kähler geometry gives \(|W^+|^2=2/3\), contradicting the calibrated value \(1/24\).

### Diameter-free selection of small defect balls

The negative branch has no Myers diameter bound.  Basepoint selection should use local doubling under Ricci lower bounds.  For fixed \(h\), the local Hardy--Littlewood maximal function
\[
M_hF(p)=\sup_{0<r\le h}\fint_{B_r(p)}F
\]
satisfies a weak estimate with constant depending only on dimension, the Ricci lower bound, and \(h\):
\[
\operatorname{Vol}\{M_hF>\lambda\}
\le {C(h)\over\lambda}\int_MF.
\]
Writing \(\bar F_i=\operatorname{Vol}(M_i)^{-1}\int F_i\to0\) and choosing, for instance, \(\lambda_i=\sqrt{\bar F_i}\), the bad set \(\{M_hF_i>\lambda_i\}\) has vanishing volume fraction while \(\lambda_i\to0\).  Thus any fixed-positive-volume family of accessible points contains points whose relevant base balls have defect mean tending to zero.  This replaces the Step 11 reference to a diameter radius.

### Cover transport and accessibility

Once a buffered normal cover is chosen and the base ball has small defect mean, the Step 9 normal-cover transport lemma gives
\[
\fint_{B_h(\hat p)}\pi^*F
\le {V_{-1}(3h)\over V_{-1}(h)}\fint_{B_h(p)}F.
\]
If the lifted ball also carries the supplied controlled harmonic chart, the controlled-chart forbidden germ applies.  Therefore the chart-accessible exclusion remains a good conditional mechanism, but it must be stated with the chart as part of the hypothesis rather than derived from bounded Ricci and cover noncollapse alone.

## 7. Interaction with A02's Calderón--Zygmund spike

The S0910A02 spike rules out a route from \(C^0\) Ricci control to pointwise curvature control.  It does not rule out the finite-\(p\) harmonic-coordinate passage above, which starts only after a chart has been supplied.  The surviving row is:
\[
\text{controlled chart} + C^0\text{ Ricci error}
\Rightarrow W^{2,p}_{\mathrm{loc}}\text{ convergence for finite }p
\Rightarrow \text{Chern--Weil and Derdziński passage on that chart.}
\]
The open problem is not pointwise curvature regularity; it is whether the closed near-critical sequence must have a positive volume proportion of fixed-scale accessible charts, or whether diffuse non-basic mixed connection curvature can prevent accessibility at every fixed scale while keeping \(F\) small.

## 8. Current mathematical target

The strongest next object is a multiscale rank-recovery or mixed-curvature estimate.  Persistent failure of fixed-scale accessibility should be related to one of the following quantities:

- contraction fillings for short fibers in buffered domains;
- scaled holonomy or vertical--horizontal curvature \(\Xi=\iota_VF_A\) in the \(\Lambda^2_+\) connection;
- O'Neill or nilpotent twisting terms in collapsed regions;
- localized regions where maximal curvature means are not controlled.

The exact Taub--NUT--AdS calculation now functions as a calibration: a single NUT has a threshold scale, below which the annular cover unwraps and the limit is hyperbolic; above which the NUT is included but the centered curvature mean is large.  A real near-critical countergeometry would need a diffuse or nested mechanism preventing all fixed-scale chart access on most volume while preserving the near-calibrated \(W^+\) density.

## 9. Rank-one Kaluza--Klein toy: what the mixed curvature may look like

To begin the next mixed-curvature calculation I wrote two local algebra scripts:

- `workspace/scripts/step12_rank1_sd_connection_toy.py`, an initial guessed-connection computation now marked as superseded;
- `workspace/scripts/step12_rank1_sd_connection_cartan.py`, which solves Cartan's first structural equations for the flat-base, constant-fiber rank-one model before forming the induced connection on \(\Lambda^2_+\).

The toy coframe is
\[
de^0=de^1=de^2=0,
\qquad
 de^3=C_{01}e^{01}+C_{02}e^{02}+C_{12}e^{12}.
\]
Cartan gives
\[
\omega_{01}=-{C_{01}\over2}e^3,
\quad \omega_{02}=-{C_{02}\over2}e^3,
\quad \omega_{12}=-{C_{12}\over2}e^3,
\]
\[
\omega_{03}=-{C_{01}\over2}e^1-{C_{02}\over2}e^2,
\quad
\omega_{13}={C_{01}\over2}e^0-{C_{12}\over2}e^2,
\quad
\omega_{23}={C_{02}\over2}e^0+{C_{12}\over2}e^1.
\]
In the self-dual basis \((e^{01}+e^{23},e^{02}+e^{31},e^{03}+e^{12})\), the script computes the induced \(SO(3)\) connection and \(\sum_iF_i\wedge F_i\).  For constant \(C_{ab}\), the four-form coefficient is zero.  Thus a flat-base constant-length circle bundle with constant twist is still too basic to carry diffuse \(\rho_+\).  Nonzero density arises only through horizontal variation of the scaled twist components and/or through base curvature, changing fiber length, O'Neill/nil terms, or non-invariant error terms absent from this toy.

After imposing the closure condition \(d(de^3)=0\), the plus-sign convention used in the toy yields a coefficient
\[
 C_{01,0}C_{12,2}-C_{01,1}C_{02,2}+C_{01,2}^2-C_{01,2}C_{02,1}
 -C_{02,0}C_{12,1}+C_{02,1}^2.
\]
This expression is not the simple \(H\cdot\operatorname{curl}H\) guessed at first, and the rotating unit example tested in the script gives zero.  Therefore the next serious calculation should not rely on a naive magnetic-helicity analogy.  It should derive the \(\Lambda^2_+\) connection for a general rank-one Kaluza--Klein metric with variable fiber length and curved base, then identify which terms can supply the forced bulk density \(P\to3/4\) while the Ricci equation remains close to \(-g\).

## 10. Variable-length rank-one toy: diffuse density can arise from closed one-jets

I then extended the toy to a variable fiber length, still suppressing horizontal base curvature:
\[
de^0=de^1=de^2=0,
\]
\[
de^3=u_0e^{03}+u_1e^{13}+u_2e^{23}
     +C_{01}e^{01}+C_{02}e^{02}+C_{12}e^{12},
\]
where \(u=d\log\ell\) and \(C=\ell F_A\) are scaled local variables.  The script is `workspace/scripts/step12_rank1_variable_length_cartan.py`.  Cartan gives
\[
\omega_{01}=-{C_{01}\over2}e^3,
\quad \omega_{02}=-{C_{02}\over2}e^3,
\quad \omega_{12}=-{C_{12}\over2}e^3,
\]
\[
\omega_{03}=-{C_{01}\over2}e^1-{C_{02}\over2}e^2-u_0e^3,
\]
\[
\omega_{13}={C_{01}\over2}e^0-{C_{12}\over2}e^2-u_1e^3,
\qquad
\omega_{23}={C_{02}\over2}e^0+{C_{12}\over2}e^1-u_2e^3.
\]
The closure condition \(d(de^3)=0\) is already nontrivial:
\[
-C_{01}u_2+C_{01,2}+C_{02}u_1-C_{02,1}-C_{12}u_0+C_{12,0}=0,
\]
\[
-u_{0,1}+u_{1,0}=0,
\quad -u_{0,2}+u_{2,0}=0,
\quad -u_{1,2}+u_{2,1}=0.
\]
For constant \(u,C\), closure forces \(C_{01}u_2-C_{02}u_1+C_{12}u_0=0\).  The derivative-free \(\sum_iF_i\wedge F_i\) coefficient in the plus-sign convention is
\[
{(C_{01}u_2-C_{02}u_1+C_{12}u_0)
(C_{01}^2+6C_{01}u_2+C_{02}^2-6C_{02}u_1+C_{12}^2+6C_{12}u_0+8|u|^2)\over4},
\]
so closed constant coefficients still have zero four-form.  However, closed one-jets can carry nonzero density.  For example, with
\[
u=(u,0,0),\qquad C_{12}=C,\qquad C_{12,0}=uC,
\]
and all other first derivatives zero, the closure equations hold at the point, while the computed coefficient is
\[
{C u^2(3C+4u)\over2}
\]
in one \(SO(3)\) sign convention and
\[
{C u(4C^2+9Cu+4u^2)\over2}
\]
in the opposite convention.  The precise normalization/sign must be matched to the Chern--Weil convention before use, and base-curvature terms are missing.  Nevertheless the calculation is important: a diffuse \(\rho_+\) density need not come from isolated NUT residues.  It can already appear in the local algebra through the coupling of fiber-length gradient and scaled twist gradient.  The next theorem/calculation should insert these expressions into the rank-one Einstein/Ricci-pinching equations and test whether the calibrated conditions force or forbid such closed one-jets.

## 11. Link to S0910A02 toric determinant equations

S0910A02's Step 12 toric calculation gives the corresponding exact reduced equations for a local \(T^2\)-invariant metric
\[
g=g_B+h_{IJ}(d\phi^I+A^I)(d\phi^J+A^J),\qquad w=\sqrt{\det h}.
\]
The vertical trace is
\[
\operatorname{tr}_h\operatorname{Ric}^V=-{\Delta_Bw\over w}+{1\over2}|F|_h^2,
\]
so exact Einstein scale \(\operatorname{Ric}=\lambda g\) gives
\[
\Delta_Bw=\left({1\over2}|F|_h^2-2\lambda\right)w.
\]
The mixed equation is the twist conservation law
\[
d\left(w h_{IJ}*_BF^J\right)=0.
\]
This is the rank-two analogue of the rank-one lesson above.  Constant or conserved twist does not automatically create calibrated bulk density; boundary degeneration, fiber length variation, and scaled twist gradients decide whether the collapse is orthogonally transitive/basic or carries persistent mixed \(\Lambda^2_+\) curvature.  For the negative LeBrun branch, the next useful calculation is the rank-one negative-Einstein analogue of these determinant/twist equations coupled to the \(\Lambda^2_+\) Pontryagin density \(P\to3/4\).  For the positive branch, A02's determinant equation explains why degeneration boundary conditions and simple connectivity/fixed points may create a volume scale, whereas free quotient collapse can evade that mechanism.

## 12. Concrete exponential-twist metric: simplest closed one-jet is not negative Einstein

To test whether the closed one-jet mechanism can already approximate the negative Einstein equations in the simplest geometry, I wrote
`workspace/scripts/step12_rank1_exp_twist_metric.py` for
\[
g=dx^2+dy^2+dz^2+e^{2ux}(dt+C y\,dz)^2.
\]
At the origin this has
\[
de^3=u e^{03}+C e^{12},
\]
with the closure-compatible derivative pattern from the variable-length toy.  The coordinate curvature computation gives exactly
\[
\operatorname{Ric}=
\operatorname{diag}\left(-u^2,-{C^2\over2},-{C^2\over2},{C^2\over2}-u^2\right),
\]
\[
s=-{C^2+4u^2\over2}.
\]
Thus there is no solution of \(\operatorname{Ric}=-\kappa g\) with \(\kappa>0\) in this flat-base constant-gradient model: the first three diagonal equations require \(u^2=C^2/2=\kappa\), while the vertical equation then gives \(0=-\kappa\).  A coarse grid search over \(u\in[-3,3]\), \(C\in[-4,4]\) also found no point close to both \(\operatorname{Ric}=-g\) and the calibrated \(P=3/4\); the best rows stayed at Ricci Frobenius error about \(1.87\).

The Weyl and Pontryagin formulas at the origin are also explicit:
\[
W^+=\operatorname{diag}\left(
{-C^2-6Cu+2u^2\over12},
{-C^2-6Cu+2u^2\over12},
{5C^2+12Cu+8u^2\over12}
\right),
\]
\[
|E|^2={11C^4-24C^2u^2+16u^4\over16},
\]
\[
P_+=2|W^+|^2+{s^2\over24}-{1\over2}|E|^2
={C^4+48C^3u+116C^2u^2+48Cu^3+16u^4\over24}.
\]
This does not rule out diffuse mixed-curvature collapse; it shows that the missing ingredient is not merely a nonzero closed one-jet of \(u\) and scaled twist over a flat base.  Any serious rank-one reduced model must include base curvature, variable gradients, nil/O'Neill terms, or a more constrained solution of the reduced Einstein equations.  This aligns with A02's toric determinant finding: the reduced Ricci equations, not Chern--Weil algebra alone, decide which mixed-connection densities are compatible with near-Einstein pinching.
