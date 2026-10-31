# Step 73 plan v2: cone flux scale classification and stratum-aware first obstruction

Session `S0910A02`. Agent1 / Orchestrator. Phase Explore.

**Status.** This file supersedes the first Step-73 higher-flux plan after TTCS verification (`trace/ttcs/results/step73_ttcs01_verifier1_integration.md`) and A01 message #506. The original idea that every homogeneous higher mode gives an unweighted `c/L` Ricci-defect lower bound was wrong. The Wronskian identity is valid in all degrees, but the logarithmic/unweighted scale is special to the quadratic mode `ell=2`.

Purpose: prepare the next Agent2 mathematical task without overclaiming. The immediate proof-side target for Yau--26 is now: prove and use the **dimension-general quadratic transverse-cone flux necessity** (cone dimension `d>=4`) and understand what, if anything, higher homogeneous modes contribute beyond weaker power-scale estimates.

## 1. Variables and scope

Use separate dimension letters:

- `N`: total dimension of the original closed manifold.
- `m`: dimension of a noncollapsed singular stratum.
- `d`: transverse cone dimension in the annular flux calculation.

For isolated singularities, `m=0` and `N=d`. For the high-dimensional Cheeger--Naber codimension-four setting, the first stratified model has `d=4`, `m=N-4`, local geometry approximately `S^m x (R^4/Gamma)`. The clean annulus algebra also applies to isolated cones with arbitrary `d>=4` and `Gamma < O(d)` free on `S^{d-1}`.

The first rigorous lemma should be the isolated transverse cone lemma. The stratum version should be stated only with explicit product/parallelism/elliptic hypotheses until normal-connection and tangential-derivative errors are controlled.

## 2. Clean cone linear identity: theorem-ready

Let `Gamma < O(d)` act freely on `S^{d-1}` and set
\[
A=\{b<r<R\}/\Gamma,\qquad L=\log(R/b).
\]
Let `K_ell` be a nonzero smooth homogeneous degree-`ell` symmetric 2-tensor on `R^d\setminus\{0\}`, with **Cartesian component homogeneity**
\[
K_\ell(rx)=r^\ell K_\ell(x),
\]
not dilation pullback weight. Assume `ell>=2`, `Gamma`-invariance, and
\[
\operatorname{tr}K_\ell=0,
\qquad \operatorname{div}K_\ell=0,
\qquad \Delta K_\ell=0,
\qquad K_\ell(x,\cdot)=0.
\]
Define
\[
o_\ell=r^{-(d+2\ell-2)}K_\ell.
\]
Then `o_ell` is also trace-free, divergence-free, harmonic, and radial-null. Indeed,
\[
\operatorname{div}(r^{-a}K_\ell)=r^{-a}\operatorname{div}K_\ell-a r^{-a-2}K_\ell(x,\cdot)=0,
\]
for `a=d+2ell-2`, and
\[
\Delta(fK_\ell)=\left(f''+{d-1+2\ell\over r}f'\right)K_\ell,
\]
so `f=r^{-a}` makes `Delta o_ell=0`. Equivalently,
\[
K_\ell=r^\ell Y_\ell(\theta),
\qquad
o_\ell=r^{-(d+\ell-2)}Y_\ell(\theta),
\]
the decaying harmonic indicial partner.

For any smooth `u` equal to `0` near `r=b` and `K_ell` near `r=R`, the gauge terms in the Euclidean linearized Ricci pair away against `o_ell`; only the rough Laplacian Green boundary term remains. Since
\[
\partial_rK_\ell={\ell\over r}K_\ell,
\qquad
\partial_ro_\ell=-{d+\ell-2\over r}o_\ell,
\]
Agent2 should prove, with the session's sign convention,
\[
\boxed{
\int_A\langle D\operatorname{Ric}_e u,o_\ell\rangle
=-{d+2\ell-2\over2}I_{K_\ell}.
}
\]
Here
\[
I_{K_\ell}=\int_{S^{d-1}/\Gamma}|K_\ell|_{r=1}^2\,d\theta.
\]
At `ell=2` this is exactly manuscript `FND:flux` with coefficient `-(d+2)/2`.

## 3. Correct unweighted and weighted lower bounds

The old plan's unweighted lower bound with denominator `L J_K` for all `ell` is false. The nuclear-norm mass is
\[
\int_A\|o_\ell\|_*dV
=J_{K_\ell}\int_b^R r^{1-\ell}\,dr,
\]
with
\[
J_{K_\ell}=\int_{S^{d-1}/\Gamma}\|K_\ell\|_{*,r=1}\,d\theta.
\]
Define
\[
H_\ell(b,R)=
\begin{cases}
\log(R/b),&\ell=2,\\[1mm]
\dfrac{b^{2-\ell}-R^{2-\ell}}{\ell-2},&\ell>2.
\end{cases}
\]
The correct unweighted estimate is
\[
\boxed{
\|D\operatorname{Ric}_e u\|_{op,\infty}
\ge { (d+2\ell-2)I_{K_\ell}\over 2J_{K_\ell}H_\ell(b,R)}.
}
\]
Thus:

- `ell=2`: `H_2=L`, recovering the log-critical unweighted bound
  \[
  \|D\operatorname{Ric}_e u\|_{op,\infty}
  \ge{(d+2)I_K\over2LJ_K}.
  \]
- `ell>2`: for `b<<R`,
  \[
  H_\ell\sim {b^{2-\ell}\over\ell-2},
  \qquad
  \|D\operatorname{Ric}_e u\|_{op,\infty}\gtrsim b^{\ell-2}.
  \]
  This tends to zero in the bubbling limit and does **not** imply `delta L >= c`.

There is a logarithmic weighted version for all `ell`:
\[
\boxed{
\sup_A r^{2-\ell}\|D\operatorname{Ric}_e u\|_{op}
\ge { (d+2\ell-2)I_{K_\ell}\over2LJ_{K_\ell}}.
}
\]
But Yau--26 controls the unweighted Ricci endomorphism. The weighted statement is useful only if a sequence-level mechanism supplies the corresponding weighted control or prevents inner-edge concentration.

## 4. Necessity consequences: `ell=2` versus `ell>2`

The inverse-log scale issue raised by A01 #506 is real. Even for `ell=2`, the clean flux inequality gives only
\[
\delta\ge c/L
\]
(up to controlled errors). Hence a nonzero quadratic obstruction is compatible with `delta -> 0` if `L -> infinity`. Coefficient vanishing follows only under an additional sequence mechanism, for example:

1. a controlled annulus with bounded `L` and small errors;
2. a relation `delta_i L_i -> 0` on the obstruction annuli;
3. an iterated fixed-rescaled-annulus extraction whose error is `O(delta log R)`, followed by `delta -> 0` at fixed `R` and then `R -> infinity`;
4. global rigidity/existence input that bypasses the inverse-log loss.

The manuscript's explicit A1 constant-scalar examples with `|log a| delta -> 1/6` are stress tests showing the inverse-log behavior is sharp, not a technical accident.

For `ell>2`, the clean isolated cone lemma gives at most a power-scale ordinary pinching bound such as
\[
\delta_i\gtrsim c\,b_i^{\ell-2}
\]
plus endpoint/nonlinear errors. Higher modes are therefore subcritical for the unweighted `C^0` Ricci norm unless an additional propagation, weighted-control, or tower-coupling theorem converts them back to a quadratic/log-critical signal.

Therefore the next Agent2 theorem should not be called a general higher-obstruction necessity theorem in the old sense. It should be a **cone flux scale classification** plus a **quadratic first-obstruction necessity interface**.

## 5. Nonlinear and weighted extensions: do not copy the quadratic estimate

The manuscript lines 915--937 extend the `ell=2` flux identity to nonlinear/energy estimates. For `ell>2`, the nonlinear pairing weight changes. Pairing the leading nonlinear term schematically gives
\[
\int_A |Dq|^2 |o_\ell|
\sim \int_A |Dq|^2 r^{-d-\ell+2}\,dV,
\]
whereas the old guessed energy weight `r^{-d-2ell+4}` only matches this at `ell=2`. Thus Agent2 must rederive all higher-mode nonlinear weights and expect inner-edge powers. The theorem-ready nonlinear statement is only the quadratic mode, unless extra hypotheses are added.

Endpoint errors also require projected `C^1` control because the Wronskian contains both `u` and `partial_r u`. Higher Taylor coefficients are coordinate-sensitive; only after fixing Bianchi gauge, endpoint markings, and lower formal tower subtraction does a higher `K_ell` represent a geometric obstruction rather than a coordinate artifact.

## 6. Relation to Biquard/Ozuch obstructions

The clean cone lemma applies to abstract homogeneous TT/radial-null modes. To use it for Biquard--Ozuch obstruction towers, Agent2 must keep these as explicit hypotheses/open interfaces:

1. existence and `Gamma`-invariance of the relevant `K_ell` subspace;
2. a fixed Bianchi/normal-coordinate slice that makes the mode geometrically meaningful;
3. subtraction of all lower-order formal tower terms and their products;
4. treatment of resonant `r^ell log r` terms, which change boundary fluxes;
5. an actual map from obstruction order/ALE Jacobi decay to homogeneous degree `ell`.

The proven four-dimensional first obstruction is vector-valued and quadratic: Ozuch's formula (Knowledge `Higher-order-obstructions...` lines 648--654) gives
\[
\lambda_k^j(\zeta,v)=c\langle R^\pm(\psi(\widetilde V_{j,0})_*(H_{j,2}+\widetilde V_{j,2}))\zeta_j^\pm,\zeta_{j,(k)}^\pm\rangle.
\]
This is the model for the all-dimensional transverse quadratic first-obstruction problem. Higher Ozuch obstructions cannot be identified with the above `ell>2` flux lemma without a separate mode-identification theorem.

## 7. Stratum-aware version

The Step 53 high-dimensional probe remains valuable but must be sharpened. It says the correct codimension-four object is:

> bundle-valued pointwise/elliptic condition along S: R_normal,±(y) zeta(y) plus possible normal-connection/tangential derivative terms must vanish, rather than only an integral condition

The locality reason is still correct: Yau--26 pinching is a pointwise operator norm, so a nonzero core obstruction at a point of the stratum creates visible Ricci defect. But a rigorous stratum equation is not merely `R_normal(y) zeta(y)=0`; tangential derivatives and normal-connection terms may cancel the normal algebraic part unless parallelism/slow variation is assumed.

A safe stratum theorem should proceed in tiers:

1. **Exact product/parallel section:** prove the isolated transverse `ell=2` flux identity fiberwise and integrate over the stratum.
2. **Slowly varying section:** add quantified covariant derivative errors from the normal connection, second fundamental form, and mixed tensor components.
3. **Elliptic obstruction-bundle equation:** formulate the full condition along the stratum and identify what pointwise pinching controls.
4. **Bubble trees:** either assume no trees or run nested scale tower subtraction. LeBrun--Ozuch Section 9 explicitly excludes trees, and its later tree handling is conformally Kähler/admissible, not general Yau--26.

## 8. Deliverable expected from Agent2

A valuable Agent2 step should produce:

- a precise theorem statement and proof for the isolated cone linear identity for arbitrary `d>=4`, `ell>=2`;
- the corrected unweighted lower bound with `H_ell(b,R)` and the weighted logarithmic bound;
- a clear corollary emphasizing the `ell=2` log-critical case and the weaker `ell>2` power case;
- a quadratic-mode noncollapsed necessity statement that lists exactly which sequence-level mechanisms (`delta L -> 0`, bounded annulus, fixed-annulus iterated limit, or rigidity input) are needed to force coefficient vanishing;
- a stratum-aware first-obstruction framework separating transverse dimension `d=4`, stratum dimension `m`, total dimension `N`, and the normal-connection/tangential-derivative terms;
- a map of which parts help all-dimensional `P_n^+` and which remain four-dimensional accounting or Ozuch-specific hypotheses.

No final Yau--26 branch conclusion should be claimed from this lemma alone.
