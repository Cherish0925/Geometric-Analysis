# Step 34: restored weighted-flow state and exact remaining estimates

## 0. Purpose

Step 33 changed the research direction for two incorrect reasons. This note restores the last supported state of the normalized cutoff-flow program, fixes the Sobolev notation, tests the proposed fixed-topology compactness inference against an explicit countermodel, and writes the energy-to-drift and cutoff-jet obligations in a notation that keeps every time and volume power visible.

The flow and basic variables are
\[
\partial_t g=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\qquad F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]
On one macro-support, with an auxiliary cutoff equal to one on \(\operatorname{supp}a\), set
\[
H_p(f,t)=\int a^{p-2}f^p\,d\mu_t,
\qquad z_p=a^{(p-1)/2}f^{p/2}.
\]
For curvature write \(K_p=H_p(F)\), and for defect write \(J_p=H_p(|E|)\).

## 1. Step 33 corrections

### 1.1 One Sobolev coefficient, not two

Use exactly the convention
\[
\boxed{\ \|u\|_4^2\le \mathcal S
 \bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),\qquad
 \mathcal S=C(4,Kr^2)\frac{r^2}{\sqrt V}.\ }
\tag{1.1}
\]
Here \(V\) is the relevant ball volume. Maheux--Saloff-Coste gives the unsquared norm estimate
\(
\|u\|_4\lesssim rV^{-1/4}\|\nabla u\|_2
\), and squaring it gives (1.1). If one instead writes \(\|u\|_4\le S\,\mathcal E(u)^{1/2}\), then \(S^2=\mathcal S\). These symbols may not be interchanged.

At \(p=2\),
\[
K_3\le K_2^{1/2}\|z_2\|_4^2
\le C\mathcal S K_2^{1/2}(D_2+r^{-2}K_2).
\tag{1.2}
\]
Thus the actual absorption number is
\[
\boxed{\gamma=\mathcal S K_2^{1/2}.}
\tag{1.3}
\]
At a good center, \(K_2\le K_0V\), so
\[
\gamma\le C\frac{r^2}{\sqrt V}\sqrt{K_0V}
      =Cr^2\sqrt{K_0}.
\tag{1.4}
\]
The ball volume cancels. Step 33's quantity \(S^2K_2^{1/2}\) arose by taking \(S\) to have the scaling of \(\mathcal S\) and then squaring it again. There is no new collapse obstruction at this step.

The same convention also converts the reaction coefficient. The three-factor curvature estimate has coefficient \(\mathcal S^2Y\), not an independently meaningful symbol \(S^4Y\):
\[
K_p'+cD_p\le Cp^N(r^{-2}+\mathcal S^2Y)K_p,
\qquad Y=K_3.
\tag{1.5}
\]
Since \(\mathcal S^2K_2=\gamma^2\), a bound \(Y(t)\lesssim \gamma K_2/t\) gives
\[
\mathcal S^2Y(t)\lesssim \gamma^3/t.
\tag{1.6}
\]

### 1.2 Fixed topology does not rescue the argument

The inference
\[
\operatorname{Ric}\ge-Kg,\quad \operatorname{Vol}(M)\le C
\quad\Longrightarrow\quad \operatorname{diam}(M)\le C'
\]
is false, even on one fixed smooth manifold. Let \(\Sigma\) be a closed surface of genus at least two and let \(q_i\) be hyperbolic metrics degenerating by pinching a simple closed geodesic. On
\[
M=\Sigma\times\Sigma,
\qquad g_i=q_i\oplus q_0,
\]
we have \(\operatorname{Ric}_{g_i}=-g_i\), fixed volume by Gauss--Bonnet, fixed topology, and \(\operatorname{diam}(g_i)\to\infty\); fixed-radius balls in the thin collar have volume tending to zero. Therefore Step 33's Bishop--Gromov diameter and ball-volume conclusions do not follow. This countermodel concerns the proposed compactness inference, not the Ishida--LeBrun topology or the calibrated-spectrum obstruction.

No fixed-manifold pinching gap follows from Step 33.

### 1.3 Status of the Step 33 script

`workspace/scripts/verify_step33_uniform_bootstrap.py` encoded the diameter bound, ball-volume bound, endpoint estimates, and gap statement as `check(..., True)`. Those lines are assertions, not computational verification. The script remains useful only for elementary exponent manipulations after its mathematical inputs are separately established. Its conclusion must not be used.

## 2. Volume-normalized formulation

Write normalized ball averages
\[
\langle h\rangle_V=V^{-1}\int h\,d\mu,
\qquad
k_p=V^{-1}K_p,
\qquad d_p=V^{-1}D_p.
\]
Then (1.1), divided by \(V^{1/2}\), becomes
\[
\langle |u|^4\rangle_V^{1/2}
\le Cr^2\bigl(\langle|\nabla u|^2\rangle_V+r^{-2}\langle u^2\rangle_V\bigr).
\tag{2.1}
\]
For \(u=z_p\),
\[
k_{3p/2}\le k_p^{1/2}\langle z_p^4\rangle_V^{1/2}
\le Cp^2r^2k_p^{1/2}(d_p+r^{-2}k_p).
\tag{2.2}
\]
At \(p=2\), the absorption number is transparently
\[
\gamma\asymp r^2\sqrt{k_2}\le Cr^2\sqrt{K_0},
\tag{2.3}
\]
with no volume symbol present. This notation should be used in the next derivation. During the provisional metric-comparison interval, either use a fixed reference measure/ball or retain the controlled factor relating \(V(t)\) to \(V(0)\); do not silently differentiate a normalized average as though \(V\) were constant.

## 3. Supported curvature seed

The already-derived \(q=2\) estimate and (1.2), under \(C\gamma<c_2/2\), give
\[
\sup_{0<s<t}K_2(s)+\int_0^tD_2(s)\,ds\le CK_2(0),
\tag{3.1}
\]
\[
\int_0^tY(s)\,ds\le C\gamma K_2(0).
\tag{3.2}
\]
The separate \(q=3\) inequality prevents terminal spikes and yields for every \(t>0\)
\[
Y(t)\le {C\gamma K_2(0)\over t},
\qquad
\mathcal S^2Y(t)\le {C\gamma^3\over t}.
\tag{3.3}
\]
This is a positive-time seed. It does not imply a time-uniform bound for \(Y\), and the \(t^{-1}\) coefficient is not integrable from zero.

## 4. Correct spacetime recurrence and time powers

The mixed interpolation is
\[
K_{3p/2}\le K_p^{1/2}\|z_p\|_4^2.
\tag{4.1}
\]
Let \(I=(\tau,t)\), \(I'=(\tau',t)\), \(\tau<\tau'<t\), and let a time cutoff satisfy \(|\zeta'|\lesssim(\tau'-\tau)^{-1}\). Combining the power energy with (1.1) gives the actual one-step estimate
\[
\boxed{
\int_{I'}K_{3p/2}
\le Cp^N\mathcal S
\left[L_p(I)\int_IK_p\right]^{3/2},}
\tag{4.2}
\]
where the direct time-cutoff energy estimate requires
\[
L_p(I)= (\tau'-\tau)^{-1}+r^{-2}+1
       +\operatorname*{ess\,sup}_{s\in I}\mathcal S^2Y(s)
\tag{4.3}
\]
up to universal polynomial factors in \(p\). A mere time average of \(\mathcal S^2Y\) does not control \(\int_I(\mathcal S^2Y)K_p\), because the coefficient can correlate with \(K_p\). This corrects the first version of this note.

On a dyadic slab \(I_t=[t/2,t]\), (3.3) gives both
\[
\operatorname*{ess\,sup}_{I_t}\mathcal S^2Y\le C\gamma^3/t,
\qquad
\int_{I_t}\mathcal S^2Y(s)\,ds\le C\gamma^3\log2.
\tag{4.4}
\]
The first bound is what closes the displayed energy recurrence; the second only records scale-critical integrability on one dyadic slab. Every nested temporal cutoff costs \(C4^k/t\). Iterating (4.2), for \(t\lesssim\min\{r^2,1\}\), therefore yields an endpoint of the scaling form
\[
\boxed{
\|af(t)\|_\infty
\le C(\gamma,\theta)\,\mathcal S^{2/p_0}
 t^{-3/p_0}
 \left(\int_{t/2}^{t}H_{p_0}(f,s)\,ds\right)^{1/p_0}.}
\tag{4.5}
\]
This is the supported formula from the Codex reconstruction. The factor \(t^{-3/p_0}\) may not be dropped merely because (4.4) is bounded.

For curvature, \(p_0=3\). Using only the spacetime seed (3.2) on a comparable slab gives
\[
\|aF(t)\|_\infty
\lesssim \mathcal S^{2/3}t^{-1}
          (\gamma K_2(0))^{1/3}
\asymp {C\gamma\over t}.
\tag{4.6}
\]
The last equivalence uses \(\gamma=\mathcal S K_2(0)^{1/2}\). Thus the currently justified curvature endpoint has a \(t^{-1}\) cost. A time-uniform endpoint near zero has not been derived.

For the defect, assume first that the base energy gives
\[
\sup_{0<s<T}J_6(s)\le C\delta^6V.
\tag{4.7}
\]
Applying (4.5) with \(p_0=6\) gives
\[
\|aE(t)\|_\infty
\le C\mathcal S^{1/3}t^{-1/2}(\delta^6Vt)^{1/6}
\le C\delta(r^2/t)^{1/3}.
\tag{4.8}
\]
Here the powers of \(V\) cancel exactly. Consequently
\[
\int_0^T\|aE(t)\|_\infty\,dt
\le C\delta r^{2/3}T^{2/3}
=C\delta\theta^{2/3}r^2
\tag{4.9}
\]
for \(T=\theta r^2\). This is the desired sequence-uniform, collapse-independent metric drift, if (4.7), the recurrence, and the provisional moving-Sobolev interval are all valid.

The route is therefore not blocked by collapse at the Sobolev step. Its central open loop is more precise: prove (4.7) without first assuming a pointwise curvature bound that is only available after the curvature iteration, and carry (4.2)--(4.9) through a simultaneous first-exit argument. The earlier direct estimate
\[
\int Fz_6^2\le C\gamma(X_6+r^{-2}J_6)
\tag{4.10}
\]
The functional estimate (4.10) follows from Sobolev--Hölder once the regularized defect energy has the expected dissipation. What remains to be checked is the exact tensor/Kato inequality
\[
J_{m,\varepsilon}'+c_mX_{m,\varepsilon}
\le C_m(r^{-2}+1)J_{m,\varepsilon}
 +C_m\int a^{m-1}F\Phi_\varepsilon^m,
\]
uniformly as \(\varepsilon\downarrow0\). It is not enough to replace the last term by \(\|aF\|_\infty J_6\), whose \(t^{-1}\) coefficient is nonintegrable at zero.

## 5. Moving geometry and first exit

The appropriate provisional interval is the maximal interval on which:

1. the local Sobolev coefficient satisfies \(\mathcal S(t)\le2\mathcal S(0)\);
2. \(K_2(t)\le2K_2(0)\), hence \(\gamma(t)\le C\gamma(0)\);
3. the metric drift is below a fixed bilipschitz threshold;
4. the fixed support/buffer geometry remains comparable.

If (4.7)--(4.9) are proved using only these provisional bounds, then small \(\delta\) improves the metric factor, which improves the Sobolev and support comparisons. Curvature need not be time-uniform at \(t=0\); the \(t^{-1}\) estimate is sufficient for positive-time plateau regularity. The defect estimate must retain the integrable \(t^{-1/3}\) behavior.

This is a coupled argument, not the triangular uniform-endpoint argument stated in Step 33.

## 6. Evolving cutoff jets

Bilipschitz equivalence controls norms of a fixed covariant tensor only after that tensor is specified independently of the metric. Although \(d\chi\) is fixed, \(\nabla^2_{g(t)}\chi\) is not:
\[
\partial_t(\nabla_i\nabla_j\chi)=-(\partial_t\Gamma^k_{ij})\nabla_k\chi.
\tag{6.1}
\]
For \(h=\partial_tg=-2\operatorname{Ric}(U)\),
\[
\partial_t\Gamma=g^{-1}*\nabla h=g^{-1}*\nabla\operatorname{Ric}(U),
\tag{6.2}
\]
so
\[
\partial_t\nabla^2\chi=\nabla U*\nabla\chi
\tag{6.3}
\]
schematically. Therefore \(\|\nabla^2\chi\|_4\) must be produced together with the first derivative of \(U\); it does not follow from metric equivalence alone.

The continuation induction should start with the coupled base pair
\[
W_1=\nabla U,\qquad C_2=\nabla^2\chi.
\tag{6.4}
\]
At the next order, \(W_2=\nabla^2U\) is coupled to \(C_3=\nabla^3\chi\). The residual single-\(\chi\) term is
\[
I=\int\chi|C_2||W_2|^p.
\tag{6.5}
\]
Set \(u=\chi|W_2|^{p/2}\). In four dimensions,
\[
I\le\|C_2\|_4\|u\|_4\|W_2\|_p^{p/2}
\le\varepsilon D_{2,p}
 +C_{\varepsilon,p}\bigl[1+\mathcal S\|C_2\|_4^2(1+r^{-2})\bigr]\|W_2\|_p^p.
\tag{6.6}
\]
\]
This closes only after the base pair has supplied a finite evolving \(L^4\) bound for \(C_2\). Initial smoothness gives finite initial data; it does not itself show that the evolving quantity stays finite to the candidate terminal time.

The next constructor should explicitly derive:
\[
{d\over dt}\bigl(\|W_1\|_p^2+\|C_2\|_p^2\bigr)
\le C_i(t)\bigl(1+\|W_1\|_p^2+\|C_2\|_p^2\bigr),
\tag{6.7}
\]
then the \((W_2,C_3)\) estimate with (6.6), and identify which coefficients are controlled by \(\|U\|_\infty\), finite unweighted \(T\)-moments, and previous levels. Constants here may depend on the individual initial metric and cutoff. No coefficient regularization \(a\mapsto a+\varepsilon\) may be used unless exterior-independent estimates are separately proved.

## 7. Restored scientific status

The following survive:

- collapse-independent critical absorption \(\gamma\lesssim r^2\sqrt{K_0}\);
- spacetime mixed interpolation and exponent map \(p\mapsto3p/2\);
- the positive-time \(H_3\) seed \(Y(t)\lesssim\gamma K_2/t\);
- the predicted defect endpoint \(\|aE(t)\|_\infty\lesssim\delta(r^2/t)^{1/3}\), whose time integral is finite;
- the shifted-curvature/cutoff-jet pairing as the right continuation architecture;
- the calibrated terminal Einstein-germ contradiction, conditional on reaching regular plateaux.

The following do not survive:

- Step 33's extra Sobolev factor and collapse obstruction;
- its fixed-topology diameter and ball-volume inference;
- its time-uniform curvature and defect endpoints;
- its fixed-manifold gap conclusion;
- automatic evolving Hessian control from bilipschitz equivalence;
- any theorem-status conclusion for the Ishida--LeBrun negative branch.

The immediate mathematical target is now sharply localized: establish the exact regularized defect energy inequality underlying (4.10) and hence \(J_6\) persistence; derive the nested-time recurrence (4.2) with the pointwise dyadic potential bound (4.3)--(4.4), moving geometry, and all time powers; obtain (4.8)--(4.9) inside a simultaneous first-exit argument; and close the evolving cutoff-jet base pair (6.7) before attempting higher-order continuation. TTCS Step 34 independently confirmed that the base pair \((\nabla U,\nabla^2\chi)\), followed by finite unweighted \(\nabla T\) moments and then \((\nabla^2U,\nabla^3\chi)\), is a viable datum-dependent order for that proof, but its term-level shifted equations still need core derivation.
