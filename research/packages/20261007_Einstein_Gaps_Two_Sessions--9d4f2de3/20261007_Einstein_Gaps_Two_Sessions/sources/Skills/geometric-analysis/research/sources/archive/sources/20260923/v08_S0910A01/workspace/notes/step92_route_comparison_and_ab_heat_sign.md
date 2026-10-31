# Step 92: route comparison and AB adjacent heat sign

Session `S0910A01`. Agent1 / Orchestrator. Phase Explore.

## 1. Continuity of the hyperbolic connected-sum route

The hyperbolic connected-sum idea is not new in Step 91.  Step 47 already built the degree-two BCG/Chern--Gauss--Bonnet mechanism for
\[
M=X\#X,
\]
where `X` is a closed oriented real-hyperbolic four-manifold.  The essential points from `workspace/plans/route_assessment_step47_entropy_degree_theorem.md` §4 are:

1. There is a degree-two map `X#X -> X`.
2. For metrics scaled to satisfy `Ric >= -3g`, Besson--Courtois--Gallot gives
   \[
   \operatorname{Vol}(X\#X,g)\ge 2\operatorname{Vol}(X,g_{hyp}).
   \]
3. For a negative Einstein metric on `X#X`, Chern--Gauss--Bonnet gives the strict upper volume
   \[
   \operatorname{Vol}(X\#X,g)
   \le {4\pi^2\over3}\chi(X\#X)
   =2\operatorname{Vol}(X,g_{hyp})-{8\pi^2\over3},
   \]
   impossible against BCG.  Positive Einstein is excluded by infinite fundamental group and Myers, and Ricci-flat by the virtually abelian fundamental group structure of compact Ricci-flat manifolds.  Thus `X#X` is a clean four-dimensional no-Einstein stress family.
4. Under two-sided negative pinching, Step 47 already found a fixed-target lower margin degenerating as
   \[
   \delta_*(\chi(X))={1\over4\chi(X)}+O(\chi(X)^{-2})
   \]
   in its `Ric≈-g` normalization.

Step 91 improved the Ricci-eigenvalue algebra in the `Ric≈-3g` normalization.  It gives the sharper box computation
\[
{ s^2\over24}-{ |E|^2\over2}
={s^2\over6}-{|\operatorname{Ric}|^2\over2}
\ge 6(1-\varepsilon)^2
\]
for `-3(1+eps)g <= Ric <= -3(1-eps)g`, `eps <= 1/3`, hence
\[
\operatorname{Vol}(M,g)
\le {2\operatorname{Vol}(X)(1-1/\chi(X))\over (1-\varepsilon)^2}.
\]
Together with BCG, using Bishop only to bound the entropy after scaling,
\[
\operatorname{Vol}(M,g)\ge {2\operatorname{Vol}(X)\over (1+\varepsilon)^2},
\]
this is incompatible when
\[
\varepsilon< {1-\sqrt{1-1/\chi(X)}\over 1+\sqrt{1-1/\chi(X)}}
={1\over4\chi(X)}+O(\chi(X)^{-2}).
\]
This is the same structural obstruction as Step 47, now with corrected Ricci-box constants.

The decisive missing object is therefore not Sambusetti attribution and not a special rate `C/chi`.  The mathematical need is a family `X_i#X_i` with maximum negative Einstein defect tending to zero, or a stronger theorem preventing such decay.  A construction at any rate `delta_i -> 0` would defeat the normalized negative branch; a construction below the BCG--CGB lower margin cannot exist.  Large volume does not dilute a pointwise maximum-norm neck error by itself, so the connector would need a real geometric mechanism that makes the local Ricci tensor close to a scalar multiple everywhere.

The renewed Lohkamp shortcut must also be read narrowly.  A metric with `Ric<0` is not the same as a metric in an arbitrary tight negative interval.  If
\[
-b g\le \operatorname{Ric}_g\le -a g,
\qquad 0<a<b,
\]
constant scaling preserves the ratio `b/a`.  To fit a prescribed interval `[c,C]` with `c<C<0`, the metric must already have `b/a <= |c|/|C|` after normalization.  Thus two-sided pinching remains a substantive geometric problem.

## 2. Product-orbifold route after Step 91

The product branch is local, but it has gained a concrete analytic object rather than only finite algebra.  The reliable Step 91 outputs are:

- K-reflection reduces the linear pairwise background problem to K-odd/odd adjacent node interactions.
- For the checkerboard chirality vector `(+,−,−,+)`, the per-receiver equations retain only adjacent ordered source nodes.
- The product-background odd radial receiver is exactly
  \[
  R_{odd}(H)={1\over2}(H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01}),
  \]
  with no hidden `V0`, frame, or background-curvature correction in this pointwise product-linear layer.
- The corrected spectrum uses azimuthal `m` parity, independent degrees in the AB one-form sector, and `P>=1` on the relevant K-odd quotient linear sector.

The AB one-form calculation has a simplification beyond the Step 91 numerical ladder.  The exact cancellation of the adjacent `m=2` polarizations can be seen directly in the two-dimensional Hessian algebra.  With
\[
C=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
the pole Hessians of real `m=2` scalar modes are proportional to `C` and `S`.  Exact one-forms have derivative matrix `H`; coexact one-forms have derivative matrix `JH`, so
\[
JC=S,
\qquad
JS=-C.
\]
The sparse odd receiver for `h=alpha_A sym beta_B` is
\[
R_{odd}(A,B)=-{1\over2}(A_{01}B_{10}+A_{10}B_{01}),
\]
so it is nonzero only when both derivative matrices are off-diagonal `S`-type.  Thus, for every degree pair `(ell,k)`, the four `m=2` contributions with nonzero receiver are
\[
(c,c;\,coex,coex),\quad(c,s;\,coex,ex),\quad(s,c;\,ex,coex),\quad(s,s;\,ex,ex).
\]
At an adjacent source `NS`, the south-pole oriented frame signs are `c -> (-1)^k c` and `s -> -(-1)^k s`.  The four source signs therefore have common factor `(-1)^k` and relative pattern
\[
+1,-1,+1,-1.
\]
Their amplitudes, denominators, heat factors, and quotient norms agree mode by mode, so the `m=2` block cancels exactly before taking any heat limit.  This is stronger than the numerical table in `workspace/data/step92_ab_heat_sign_formula.json`.

After this cancellation, the residual AB adjacent polarization class is the `m=0` coexact--coexact double series
\[
K_{\tau}^{AB}={1\over512}\sum_{\ell,k\ge1}(-1)^k
{(2\ell+1)(2k+1)\mu_\ell\mu_k\over {1\over2}(\mu_\ell+\mu_k)-1}
\exp\{-\tau[ {1\over2}(\mu_\ell+\mu_k)-1]\},
\qquad \mu_\ell=\ell(\ell+1).
\]
The factors `(2ell+1)` and `(2k+1)` are the normalized zonal-shell amplitudes at a pole; this is not a literal single-degeneracy count.
Using
\[
{e^{-\tau p}\over p}=\int_\tau^\infty e^{-sp}\,ds,
\]
this becomes
\[
K_{\tau}^{AB}= {1\over512}\int_\tau^\infty e^s A(s)B(s)\,ds,
\]
where
\[
A(s)=\sum_{\ell\ge1}(2\ell+1)\mu_\ell e^{-s\mu_\ell/2},
\quad
B(s)=\sum_{\ell\ge1}(-1)^\ell(2\ell+1)\mu_\ell e^{-s\mu_\ell/2}.
\]
Here `A(s)>0` termwise.  Let `p_t^{(2)}(x)` be the scalar heat kernel on the unit `S^2`, from the north pole, written as a function of `x=cos r`.  At the antipode,
\[
p_t^{(2)}(-1)= {1\over4\pi}\sum_{\ell\ge0}(2\ell+1)(-1)^\ell e^{-t\mu_\ell},
\]
so
\[
B(s)=-4\pi\,\partial_t p_t^{(2)}(-1)\big|_{t=s/2}.
\]
The earlier monotonicity wording was too weak by itself.  A direct proof uses the dimension-raising identity
\[
\partial_xp_t^{(2)}(x)=2\pi e^{-2t}p_t^{(4)}(x),
\]
where `p_t^{(4)}` is the zonal heat kernel on `S^4`.  Since for a zonal function on `S^2`,
\[
\Delta=(1-x^2)\partial_x^2-2x\partial_x,
\]
at `x=-1` one has
\[
\partial_t p_t^{(2)}(-1)=\Delta p_t^{(2)}(-1)=2\partial_xp_t^{(2)}(-1)
=4\pi e^{-2t}p_t^{(4)}(-1)>0.
\]
The strict positivity is the positivity of the heat kernel on connected `S^4` for `t>0`.  Therefore
\[
B(s)=-16\pi^2 e^{-s}p_{s/2}^{(4)}(-1)<0.
\]
Consequently
\[
K_{\tau}^{AB}=-{\pi^2\over32}\int_\tau^\infty A(s)p_{s/2}^{(4)}(-1)\,ds<0.
\]
Near `s=0`, the off-diagonal heat kernel is exponentially small while `A(s)=O(s^{-2})`; as `s->infty`, `A(s)=6e^{-s}+O(e^{-3s})` and the `S^4` heat kernel tends to its positive average.  The improper integral is finite and strictly negative as `tau downarrow 0`.

Thus the AB adjacent sector has a strict analytic sign in the Step 89/91 principal normalization:
\[
K_{adj}^{AB}<0.
\]
The Step 91/92 numerical value
\[
K_{adj}^{AB}\approx -0.03144249732
\]
is consistent with this sign and with the Abel-limit double series.  The support calculation is recorded in `workspace/scripts/step92_ab_heat_sign_formula.py` and `workspace/data/step92_ab_heat_sign_formula.json`.  Direct floating summation of `B(s)` at very small `s` is ill-conditioned because the true antipodal signal is exponentially small; the sign statement rests on the dimension-raising heat-kernel argument, not on those finite-precision samples.

This is still only a sector theorem.  The complete Ozuch coefficient also needs the actual singular ALE source normalization, Bianchi/gauge projection, AA/BB tensor sectors, equality of adjacent ordered coefficients in the transported node frames, heat-tail bounds for the differentiated kernels, and matching of the result to the `t_i lambda_i + t_i^2 mu_i` radial expansion with an error smaller than the cubic layer.  A nonzero local adjacent coefficient would constrain only the selected symmetric desingularization branch; it would not rule out unrelated Einstein metrics on the resulting smooth manifold.

## 3. Route comparison after the correction

The current frontier has three serious but different mathematical roles.

### Restricted Ishida--LeBrun negative theorem

This remains the most mature result directly involving near-negative Ricci pinching and no-Einstein topology.  It is already a multi-module proof architecture with topological curvature budgets, selected supports, cutoff flow, terminal compactness, and the Derdzinski local contradiction.  Its limitation is scope: a special four-dimensional geography and substantial analytic work still needing independent proof-level tightening and eventual Lean formalization.  It is valuable to keep repairing, but it is not a route to the full all-dimensional statement by itself.

### Hyperbolic `X#X`

This route has the cleanest all-sign no-Einstein manifolds.  Its hard part is entirely metric construction or a stronger nonconstruction theorem for two-sided pinching.  Existing BCG/CGB work supplies a lower margin of order `1/chi(X)`; it does not create near-pinched metrics.  A02 Step 88 added a sharp local calculation for warped-product connectors: at a waist of `dr^2+f(r)^2 g_F` with `Ric_F=2k g_F`, `k>=0`, writing `alpha=f''/f>=0` and `beta=2k/f^2>=0`, the defect from `Ric=-3g` is `max(3|1-alpha|, |3-alpha+beta|)` and has minimum `3/2+3 beta/4`, hence at least `3/2` for flat or spherical waists.  I independently checked this algebra in `workspace/scripts/step92_warped_waist_barrier_check.py` and `workspace/data/step92_warped_waist_barrier_check.json`.  This explains why simple cusp-to-cusp warped turnarounds cannot make `delta->0`, but it is not a general non-warped waist theorem; the traced Gauss equation for a minimal separating hypersurface gives negative scalar curvature rather than a contradiction.  The hyperbolic route should be pursued when a concrete non-warped connector mechanism appears, or when the pointwise waist obstruction is generalized beyond warped products.  Without such a mechanism, repeating the global obstruction does not advance the construction side.

### Product-orbifold mixed chirality

This route is not global enough to decide Yau--26, but it is currently the most executable source of new mathematical information.  The K-reflection, receiver simplification, checkerboard adjacent reduction, corrected spectrum, and AB heat sign convert one part of the gluing problem into an analytic object with a provable sign.  Its value is not that it solves the full problem; its value is that it can now focus the remaining unknowns: source normalization and the AA/BB/gauge sectors.  If those sectors share the same sign, cancel for symmetry reasons, or can be bounded below the AB contribution, the product branch would yield a precise desingularization theorem.  If they cancel it, the calculation will still reveal a real structural balance in the orbifold Einstein problem.

## 4. Best next work

The strongest immediate action is to turn the AB sign into a clean, source-compatible theorem and then add the missing sectors.  The next Constructor/Actuator work should:

1. Convert the Step 92 written `m=2` polarization cancellation and dimension-raising heat-kernel sign argument into a polished lemma, with exact assumptions on symmetric-product normalization and pole frames.
2. Match the principal source normalization to Ozuch's actual `H^4` singular tensor, including the quotient isotropy factor and the no-averaging convention for symmetric products.
4. Build the AA/BB tensor-sector analogue with the corrected electric/magnetic harmonic decomposition and the same K-odd receiver.
5. Only after those pieces are stable, compare the complete adjacent coefficient with the all-same calibrated path and the cubic radial expansion.

In parallel, peer work should keep the hyperbolic connector problem concrete: find or rule out a geometric smoothing mechanism on `X_i#X_i` with maximum defect tending to zero.  The route should not be redirected to `X#X` merely because its no-Einstein obstruction is familiar; it needs new metric geometry, while the product branch currently has a newly tractable calculation.
