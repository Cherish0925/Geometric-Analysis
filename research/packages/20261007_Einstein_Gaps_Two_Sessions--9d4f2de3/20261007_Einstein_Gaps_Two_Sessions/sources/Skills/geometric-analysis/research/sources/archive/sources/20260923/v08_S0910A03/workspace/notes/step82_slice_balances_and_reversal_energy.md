# Step 82: physical slice balances and the nonlinear reversal variable

> **Step 83 correction.** The sign analysis in §8 overclaimed: Cov(H,|b|²)
> is indefinite (not part of the positive group), and ⟨h²(v-2u)⟩ is indefinite
> (pointwise u ≤ 0, v ≥ 0 not guaranteed). The budget is -6+2δ, not -18.
> The corrected analysis is in `workspace/notes/step83_corrected_K_production_and_bakry_emery.md`.
> TTCS also showed that no known monotone functional excludes the K-drop
> in the full OT system. The Bakry-Émery Ric^σ_B has a universal -1 eigenvalue.

Session `S0910A03`, Agent1 / Explore.

## 1. Why this is the right local question

The negative graph-manifold route already has an all-Einstein exclusion on the intended topology and an explicit expanding tail. Its unresolved geometric module is a finite connector from a reflected scalar-minus-six center to an expanding slice. Steps 78 and 81 exclude the fixed Bianchi VII\(_0\) evolution, but not the full two-variable orthogonally transitive (OT) system.

The useful question is therefore not whether an exact core can end at a constant orbit map—Step 79 already excludes that—but whether the coupled geometry can reverse the **mean horizontal contraction** forced at the reflected center. This note derives the exact physical-measure balances that isolate that event.

## 2. Variables and conventions

Use physical Gaussian radial gauge
\[
 g=dr^2+q_r,
 \qquad q_r=e^{2a(r,z)}dz^2+G_{ab}(r,z)dx^a dx^b,
\]
with periodic `z`, positive-definite orbit matrix `G`, and free flat \(T^2\) orbits. Let
\[
 \rho=\sqrt{\det G},\qquad
 u=a_r,\qquad
 B=\frac12G^{-1}G_r,\qquad
 v=\operatorname{tr}B,
\]
\[
 B_0=B-\frac v2I,\qquad H=u+v,
 \qquad d\mu=e^a\rho\,dz.
\]
Define
\[
 V=\int d\mu,\qquad I=\int u\,d\mu,\qquad J=\int v\,d\mu.
\]
All defect components below are orthonormal components of
\[
 E=\operatorname{Ric}_g+3g.
\]
Since \((d\mu)_r=H\,d\mu\),
\[
 V'=I+J,
 \quad I'=\int(u_r+Hu)d\mu,
 \quad J'=\int(v_r+Hv)d\mu.
\]

## 3. Exact integrated balances

The tangential Gaussian evolution is
\[
 S_r+HS=\operatorname{Ric}(q_r)+3I-E_T.
\]
Taking the orbit trace and horizontal unit-vector component gives
\[
 v_r+Hv=R^q_{\rm orb}+6-E_{\rm orb},
\]
\[
 u_r+Hu=R^q_{zz}+3-E_{zz}.
\]
In physical slice arclength `s`, if \(\theta=\rho_s/\rho\), then
\[
 R^q_{\rm orb}=-\theta_s-\theta^2
 =-\rho^{-1}\partial_s(\rho\theta).
\]
Consequently periodicity gives
\[
 \int R^q_{\rm orb}\,d\mu=0.
\]
This uses only the orbit-area function, so it remains valid for the full, non-diagonal orbit matrix. Hence
\[
 \boxed{J'=6V-\int E_{\rm orb}\,d\mu,}
 \tag{3.1}
\]
\[
 \boxed{I'=3V+\int R(q_r)\,d\mu-\int E_{zz}\,d\mu.}
 \tag{3.2}
\]
The diagonal direct-Ricci script `workspace/scripts/step82_slice_balance_verify.py` checks both formulas symbolically and on a nontrivial periodic off-shell field. The finite-difference discrepancies are \(1.45\times10^{-12}\) for `I` and \(6.50\times10^{-12}\) for `J`; see `workspace/data/step82_slice_balance.json`.

### Contracted Gauss correction

The exact contracted Gauss identity is
\[
 R(q_r)=R(g)-2\operatorname{Ric}_{rr}+H^2-|S|^2.
\]
Because \(R(g)=\operatorname{tr}E-12\) and \(\operatorname{Ric}_{rr}=E_{rr}-3\),
\[
 \boxed{
 R(q_r)=-6+H^2-|S|^2+\operatorname{tr}E-2E_{rr}.}
 \tag{3.3}
\]
Furthermore
\[
 |S|^2=u^2+\frac12v^2+|B_0|^2.
\]
Substitution into (3.2) cancels `E_zz` and yields
\[
 \boxed{
 I'=\int\left[-3+2uv+\frac12v^2-|B_0|^2
 +E_{\rm orb}-E_{rr}\right]d\mu.}
 \tag{3.4}
\]
This is an important correction to an intermediate Step-82 draft: the exact defect is \(E_{\rm orb}-E_{rr}\), not \(2E_{rr}-E_{zz}\). Both TTCS verifier branches caught the error, and the direct symbolic/numerical check now gives zero contracted-Gauss residual and reproduces `I'` exactly. The coarse operator-norm consequence below happened to be unchanged because both three-component combinations are bounded by \(3\delta\).

## 4. The first-return condition

Suppose `I` is negative immediately before a first radius \(r_*\) at which \(I(r_*)=0\). Smoothness gives \(I'(r_*)\ge0\). Write weighted averages as \(\langle f\rangle=V^{-1}\int f\,d\mu\). At the return, \(\langle u\rangle=0\), so \(\langle uv\rangle=\operatorname{Cov}(u,v)\). Equation (3.4) gives
\[
 0\le\frac{I'}V=-3+2\operatorname{Cov}(u,v)
 +\frac12\langle v^2\rangle-\langle|B_0|^2\rangle
 +\langle E_{\rm orb}-E_{rr}\rangle.
\]
If \(\|E\|_{\rm op}\le\delta\), then \(|E_{\rm orb}-E_{rr}|\le3\delta\), hence every first return requires
\[
 \boxed{
 2\operatorname{Cov}(u,v)+\frac12\langle v^2\rangle
 -\langle|B_0|^2\rangle\ge3-3\delta.}
 \tag{4.1}
\]
Thus mean/inhomogeneous orbit expansion and positive correlation between horizontal and orbit expansion help reversal; radial orbit shear opposes it.

## 5. Equivalent intrinsic-energy threshold

Write
\[
 G=\rho M,\qquad \det M=1,
\]
and let \(U:S^1\to SL(2,\mathbb R)/SO(2)\cong\mathbb H^2\) denote the orbit-shape map. In physical slice arclength `s`, let
\[
 h=(\log\rho)_s,\qquad e=|U_s|_{\mathbb H^2}^2,
\]
with the Step 79 normalization. The intrinsic scalar identity is
\[
 R(q_r)=-2h_s-\frac32h^2-\frac12e.
\]
Since \(\rho_s=h\rho\), integration by parts gives
\[
 \boxed{\langle R(q_r)\rangle=-\frac12K,\qquad
 K:=\langle e-h^2\rangle.}
 \tag{5.1}
\]
Set \(x=I/V=\langle u\rangle\), \(y=J/V=\langle v\rangle\). Equation (3.2) becomes
\[
 \boxed{x'=3-\frac12K-\langle E_{zz}\rangle-x(x+y).}
 \tag{5.2}
\]
At a first return \(x=0,x'\ge0\),
\[
 \boxed{K\le6-2\langle E_{zz}\rangle\le6+2\delta.}
 \tag{5.3}
\]
At an exact reflected scalar-minus-six center,
\[
 K(0)=12,\qquad x(0)=y(0)=0,
 \qquad x'(0)=-3,
 \qquad y'(0)=6.
\]
The connector must therefore lower a geometrically invariant physical quantity from `12` to about `6`, after first moving away from the center. This is sharper than merely asking whether a convex-distance or orbit energy grows.

The normalized orbit-area mean obeys
\[
 \boxed{y'=6-\langle E_{\rm orb}\rangle-y(x+y).}
 \tag{5.4}
\]
This controls only the mean `y`; it does not control \(\operatorname{Var}(v)\), \(\operatorname{Cov}(u,v)\), or radial shear.

## 6. What the slice identities do and do not force

The balances alone do not prohibit reversal.

* The moment profile \(u=v=2\cos z\), \(B_0=0\) gives the left side of (4.1) equal to `5`. This is only an algebraically favorable slice, not a metric evolution.
* More strongly, a local exact Einstein reversal germ exists away from a reflected center. For
  \[
  g=dr^2+e^{2a(r)}dz^2+e^{2b(r)}(dx^2+dy^2),
  \]
  put \(u=a'\), \(p=b'\), \(v=2p\). Flat-slice Einstein evolution gives
  \[
  u'=3-u(u+2p),\qquad p'=3-p(u+2p).
  \]
  At a slice with \(u=0,p=\sqrt3\), the Hamilton relation holds, all mixed equations vanish, and \(u'=3\). Thus local exact equations permit a horizontal return. This does **not** show it is reachable from the reflected scalar-minus-six center.

The matrix Noether current also does not settle the problem: zero matrix average allows large oscillatory radial map velocity and gives no \(L^2\) bound on \(|B_0|\). The mixed equation is a sign-indefinite Codazzi relation. Therefore the remaining mathematics is dynamic reachability, not pointwise or moment compatibility.

`workspace/scripts/step82_turning_covariance_model.py` and `workspace/data/step82_turning_covariance_model.json` preserve this distinction. The former draft's homogeneous \(v=\sqrt6\) row was only a moment balance and violated the flat-slice Gauss relation; it is now explicitly marked as such. The compatible flat exact germ occurs at \(v=\sqrt{12}\).

## 7. Universal early behavior from the clean-context derivation

The TTCS generator derived a stronger germ result. Define
\[
 k=e-h^2,\qquad c=h_s+h^2=\frac{12-k}{4},
 \qquad \tau=\nabla_sU_s+hU_s.
\]
At an exact reflected scalar-minus-six OT center,
\[
 u_r(0)=-\frac14k,
 \qquad v_r(0)=3+\frac14k,
 \qquad (U_r)_r(0)=-\tau,
 \qquad \langle k\rangle=12.
 \tag{7.1}
\]
It obtained
\[
 \boxed{K'(0)=0,}
 \tag{7.2}
\]
\[
 \boxed{
 K''(0)=2\langle|\tau|^2\rangle+18+\frac38\langle k^2\rangle
 =72+2\langle|\tau|^2\rangle+\frac38\operatorname{Var}(k)\ge72.}
 \tag{7.3}
\]
Consequently
\[
 x(r)=-3r+\left(3-\frac1{12}K''(0)\right)r^3+O(r^5)
 \le-3r-3r^3+O(r^5).
 \tag{7.4}
\]
Thus no exact reflected center engineering can make `K` initially move toward the return threshold. Any successful connector must exhibit a later nonlinear turnover after universal initial worsening.

The algebraic consequences of (7.1)–(7.3) were independently reproduced in `workspace/scripts/step82_center_jet_invariants.py`. With
\[
 T=2\operatorname{Cov}(u,v)+\frac12\langle v^2\rangle-\langle|B_0|^2\rangle
\]
and \(\widetilde T=T-y^2/2\), its exact quadratic coefficients are
\[
 T=r^2\left[18-\frac12\langle|\tau|^2\rangle
 -\frac3{32}\operatorname{Var}(k)\right]+O(r^4),
 \tag{7.5}
\]
\[
 \widetilde T=-r^2\left[\frac12\langle|\tau|^2\rangle
 +\frac3{32}\operatorname{Var}(k)\right]+O(r^4).
 \tag{7.6}
\]
A positive coefficient in `T` can come entirely from mean orbit expansion \(y^2/2=18r^2+O(r^4)\); it does not contradict the universal increase of `K`.

The geometric derivation of (7.3), including normalization, was subsequently tensor-checked from (8.1), the orbit equation, and Codazzi in `trace/ttcs/results/step82_ttcs02_verifier1_integration.md`. It is established in the stated exact reflected OT setting; approximate germs acquire defect-jet terms.

## 8. Strongest next mathematical object

The full problem is now organized by
\[
 K=\langle|U_s|^2-h^2\rangle.
\]
The next useful derivation is its exact radial production law. The TTCS generator proposes, with \(b=U_r\),
\[
 \nabla_rb+Hb+\tau=\mathcal E_0,
 \qquad \nabla_rU_s=\nabla_sb-uU_s,
\]
and a Codazzi relation of the form
\[
 v_s=h\left(u-\frac v2\right)-\frac12\langle U_s,b\rangle-E_{rs}.
\]
A second independent clean-context verification derived the exact kinematic identity
\[
 \boxed{K'=-2\langle\tau,b\rangle+2\langle vc\rangle
 +\operatorname{Cov}(v-u,k)-2xK.}
 \tag{8.1}
\]
Here
\[
 [\partial_r,D_s]=-uD_s,\qquad
 \nabla_rU_s=\nabla_sb-uU_s,
\]
and moving normalized averages obey
\[
 \frac d{dr}\langle f\rangle=\langle f_r\rangle+\operatorname{Cov}(H,f).
\]
The Codazzi identity, in the same target normalization \(|b|^2=2|B_0|^2\), is
\[
 \boxed{D_sv=h\left(u-\frac v2\right)
 -\frac12\langle U_s,b\rangle_{\mathbb H^2}-E_{rs}.}
 \tag{8.2}
\]
Consequently
\[
 2\langle vc\rangle=-2\langle h^2u\rangle+\langle h^2v\rangle
 +\langle h\langle U_s,b\rangle\rangle+2\langle hE_{rs}\rangle.
 \tag{8.3}
\]

An earlier candidate (8.1) also added an explicit traceless-orbit defect term while retaining \(-2\langle\tau,b\rangle\). That double-counted the orbit equation and has been removed. If
\[
 \nabla_rb+Hb+\tau=\mathcal E_0,
\]
then one may instead eliminate `tau`; the explicit defect contribution is then \(-2\langle\mathcal E_0,b\rangle\), and it appears only once.

Before return, `x<0`, so \(-2xK>0\) opposes the required decrease. A connector must make the remaining terms sufficiently negative to reverse the universal rise and lower `K` by roughly six units. The next constructive/verification work should compute the separate production ledger along an exact reflected OT Cauchy germ, not a prescribed cosh carrier, and seek either a coercive estimate on (8.1) or a resolved interval where `K'<0` before curvature concentration. This is a theorem/construction fork; neither outcome has yet been obtained.

## 9. Scope relative to Yau 26

This work advances only the normalized negative graph-manifold laboratory. Even a complete connector would still need global attachment and would leave the positive normalized branch and all-dimensional quantifiers unresolved. Peer A02's positive near-pinched construction is complementary. A01 has corrected its mixed-chirality result: the unconditional positivity argument fails because the Einstein operator has a negative TT mode and singular self-pairings cannot be treated by a positive quadratic form; only the flat principal odd identity and a matched regularized relative-response target survive. Neither peer result changes the present negative-side equations.

## 10. Reproducible files

- `workspace/scripts/step82_slice_balance_verify.py`
- `workspace/data/step82_slice_balance.json`
- `workspace/scripts/step82_geometric_balance_check.py`
- `workspace/data/step82_geometric_balance.json`
- `workspace/scripts/step82_turning_covariance_model.py`
- `workspace/data/step82_turning_covariance_model.json`
- `workspace/scripts/step82_center_jet_invariants.py`
- `workspace/data/step82_center_jet_invariants.json`
- `trace/ttcs/results/step82_ttcs01_verifier1_integration.md`
- `trace/ttcs/results/step82_ttcs01_generator1_integration.md`
- `trace/ttcs/results/step82_ttcs02_verifier1_integration.md`
