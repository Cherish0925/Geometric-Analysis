# TTCS Independent Branch Record

```json
{
  "step_id": 47,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/plans/route_assessment_step47_entropy_degree_theorem.md",
    "Knowledge/objects/papers/Differentiable-rigidity-under-Ricci-curvature-lower-bound--cfb4c9cdd3c7--65a5a48bd00c/object.md",
    "Knowledge/objects/papers/Farrell-Jones-spheres-and-inertia-groups-of-complex-projective-spaces--acfe469446a9--8fe24450b510/object.md",
    "Sessions/S0910A01/staging/acquired/Volume_entropy_and_rigidity_for_𝖱𝖢𝖣-spaces_97042f61708bf34d/part_001.md",
    "Sessions/S0910A01/staging/acquired/Extended_graph_4-manifolds__and_Einstein_metrics_36ca3f274012faba/content.md"
  ]
}
```

## Task

Using the Step 47 note and the actual sources, develop the strongest scientifically useful next formulations for the entropy/global-volume and exotic-smooth-structure directions toward the full Yau 26 proposition. In particular: (i) determine what normalized topology/entropy margin would be required for a uniform varying-target negative pinching theorem beyond fixed X; (ii) analyze whether Farrell--Jones real-hyperbolic exotic smoothings could become a strict counterexample route, separating what topology rules out for positive/zero/negative Einstein constants and what remains unknown; (iii) propose a few load-bearing theorem statements or calculations that would materially decide these routes. Do not invent literature or assert a no-Einstein theorem absent from the files.

## Output

## Framing: what the global-volume machinery can and cannot see

The single most important structural fact behind Step 47 is that every quantity the entropy/volume route controls is an invariant of homotopy type, while the counterexample candidates differ from their models only in smooth structure. Make this explicit, because it decides items (i) and (ii) simultaneously.

For a Farrell–Jones smoothing $Y=X\#\Sigma$ of a closed real-hyperbolic $X^n$ with $\Sigma$ a homotopy sphere ($n\ge3$): $Y$ is homeomorphic to $X$, hence $\pi_1(Y)\cong\pi_1(X)$, $H_*(Y)\cong H_*(X)$, $\chi(Y)=\chi(X)$, simplicial volume $\|Y\|=\|X\|$, and the minimal volume entropy $\mathrm{MinEnt}(Y)=\inf_g h(\tilde g)^n\mathrm{Vol}_g=\mathrm{MinEnt}(X)$ (all homotopy invariants). The BCG bound, the BBCG rigidity theorem, the Di Cerbo $\mathrm{Vol}_{\mathrm{Ric}}$ identity, and the RCD generalization $h(\bar X)^N\mathcal H^N \ge \mathrm{ind}_H(f)\,h(\tilde Y)^N\mathcal H^N(Y)$ are all functions of these invariants. Therefore **none of them separates $Y$ from $X$**, and none can either obstruct or manufacture an Einstein metric on the exotic $Y$ in a way that differs from $X$. The only Yau-26-relevant question is about the smooth structure, on which the entropy machinery is silent by construction. This is the mechanism, not a defect of Step 47's particular estimate.

## (i) The normalized margin a uniform varying-target theorem would demand

Write the pinching in scale-free form. After rescaling $g$ (which leaves $\mathrm{Ric}$ as a $(0,2)$-tensor fixed), assume the eigenvalues of $g^{-1}\mathrm{Ric}_g$ lie in $[-(n-1)(1+\delta),\,-(n-1)(1-\delta)]$, i.e. $\|g^{-1}\mathrm{Ric}_g+(n-1)I\|_{\mathrm{op}}\le (n-1)\delta$. Bishop gives $h(\tilde g)\le n-1$, so with a degree/index-$k$ domination $f:Y\to X$ of a hyperbolic target,
$$
(n-1)^n\mathrm{Vol}_g(Y)\ \ge\ h(\tilde g)^n\mathrm{Vol}_g(Y)\ \ge\ \mathrm{ind}\cdot(n-1)^n\mathrm{Vol}_{-1}(X),
$$
so the normalized excess
$$
\rho(Y,g):=\frac{h(\tilde g)^n\mathrm{Vol}_g(Y)}{\mathrm{ind}\cdot(n-1)^n\mathrm{Vol}_{-1}(X)}\ \ge\ 1 .
$$
A uniform (dimension-only) existence statement would need a fixed $\varepsilon_n>0$ with "$\rho<1+\varepsilon_n\Rightarrow$ Einstein." Two exact facts show why this specific inequality cannot carry the load:

- Because $\mathrm{MinEnt}$ is a homotopy invariant, $\inf_g\rho(Y,g)=\inf_g\rho(X,g)$; the exotic member attains the same infimal $\rho$, so $\rho<1+\varepsilon_n$ is satisfiable on $Y=X\#\Sigma$ for every $\varepsilon_n$ while $Y$ is not diffeomorphic to the model. Any theorem of the displayed form that concluded "diffeomorphic to $X$" would contradict the existence of these smoothings — which is precisely the BBCG diameter-dependence argument (their intro paragraph: arbitrarily sharp pinching on large-degree covers drives $\mathrm{Vol}_g(Y)/\mathrm{Vol}_{-1}(\bar X)\to1$).

- In dimension $4$ the CGB refinement of Step 47 replaces $\rho$ by a genuinely smooth-sensitive functional, but the elementary margin degenerates: the $X\#X$ threshold is $\delta_{\max}(X)\sim 1/(4\chi(X))\to0$. A uniform version would require a stability inequality
$$
2\chi(Y)-3|\tau(Y)|-\tfrac{3}{2\pi^2}\mathrm{Vol}_{\mathrm{Ric}}(Y)\ \ge\ \kappa_n\cdot \mathcal Q(Y),\qquad \mathcal Q>0\ \text{on exotic smoothings},
$$
with $\kappa_n$ dimension-only and $\mathcal Q$ a *smooth* invariant that is bounded away from $0$ on the exotic members. No such $\mathcal Q$ exists in $n=4$ (there $\chi,\tau$ do not detect $\Sigma$, and Seiberg–Witten is the only smooth-sensitive input, orthogonal to pinched geometry), and in $n\ge5$ there is no Gauss–Bonnet/Seiberg–Witten replacement at all.

Net content of (i): the required uniform margin is not a number one is missing but a *type* one is missing — a coercive lower bound whose right-hand side is sensitive to smooth structure. The entropy/volume family is homotopy-invariant and therefore cannot supply it. This reorients effort away from sharpening the entropy constant and toward a mechanism that is pointwise/curvature-sensitive (item iii).

## (ii) Exotic smoothings as a candidate refutation, resolved by sign

The decisive simplification: for $Y=X\#\Sigma$ homeomorphic to a closed real-hyperbolic $X^n$, an Einstein metric on $Y$ is forced into one sign of $\lambda$.

- $\lambda>0$: $\mathrm{Ric}=\lambda g>0$ forces $\pi_1(Y)$ finite (Bonnet–Myers). But $\pi_1(Y)\cong\pi_1(X)$ is infinite. Excluded.
- $\lambda=0$: a compact Ricci-flat manifold has, by the Cheeger–Gromoll splitting theorem plus Bieberbach, a finite-index $\mathbb Z^k$ in $\pi_1$; $\pi_1$ is virtually abelian. The hyperbolic group $\pi_1(X)$ is not (it contains a free group of rank $2$). Excluded.
- $\lambda<0$: the only sign compatible with the topology; existence in $n\ge5$ is open (Di Cerbo's Question 4 records exactly this gap).

So the exotic route is a *strict* counterexample to Yau 26 for every window whose lower constant $c_n<0$ **iff** some such $Y$ admits no Einstein metric with $\lambda<0$; otherwise those $Y$ support Yau 26.

The scaling bookkeeping that makes this bite on *every* $c_n<0$ window: given $c_n<C_n$ with $c_n<0$, choose $\mu\in(c_n,\min(C_n,0))$, take a Farrell–Jones metric $g_\varepsilon$ with $\mathrm{sect}\in[-1-\varepsilon,-1+\varepsilon]$ (hence, summing $n-1$ sectional terms, $\mathrm{Ric}_{g_\varepsilon}\in[-(n-1)(1+\varepsilon),-(n-1)(1-\varepsilon)]$), and rescale by $t=(n-1)/|\mu|$. The eigenvalues of $g^{-1}\mathrm{Ric}$ then sit in $[\mu(1+\varepsilon),\mu(1-\varepsilon)]\subset(c_n,C_n)$ once $\varepsilon<\varepsilon(\mu,c_n,C_n)$. Farrell–Jones supplies arbitrarily small $\varepsilon$ (via cover degree $\to\infty$, per BBCG's own statement), so *every* window with $c_n<0$ is populated on $Y$. Consequently a *true* window must have $c_n\ge0$, throwing the entire proposition onto positively-Ricci-pinched manifolds — the same front as the $\#_k(S^2\times S^2)$ analysis. Real-hyperbolic Farrell–Jones examples (dimensions $\ge6$ in the acquired Kasilingam remark) are the sharp attack because their pinching is arbitrarily tight; the complex-hyperbolic smoothings (real dimensions $14,16$) only give a fixed wide window $\mathrm{sect}\in[-4-\varepsilon,-1+\varepsilon]$, hence $\mathrm{Ric}$ in a fixed ratio-$4$ band, and do not defeat narrow windows.

The status of the whole route therefore *flips* on one analytic fact — whether these sectionally-pinched exotics carry an Einstein metric with $\lambda<0$ — which is exactly item (iii).

## (iii) Load-bearing statements and the one decisive computation

**Lemma S (sign restriction — provable now, natural Lean target).** If $Y^n$ ($n\ge3$) is homotopy equivalent to a closed real-hyperbolic manifold, then any Einstein metric on $Y$ has $\lambda<0$. Proof: Bonnet–Myers excludes $\lambda>0$; Cheeger–Gromoll + Bieberbach exclude $\lambda=0$. This is elementary, self-contained, and it converts Yau 26's exotic branch into a single existence question. Worth formalizing early because it is short and it structures everything downstream.

**Theorem R (reduction — conditional).** Fix $n\ge6$. If there exists a closed real-hyperbolic $X^n$ and a Farrell–Jones smoothing $Y=X\#\Sigma$ carrying no Einstein metric (equivalently, by Lemma S, none with $\lambda<0$), then Yau 26's implication is void for every $c_n<C_n$ with $c_n<0$; any surviving window has $c_n\ge0$. Conversely, if all such $Y$ carry an Einstein metric, the $c_n<0$ family is consistent with Yau 26 and the exotic route is closed.

**Theorem A (the decisive existence target).** There is $\varepsilon_n>0$, depending only on $n$, such that any closed $M^n$ with $\mathrm{sect}\in[-1-\varepsilon,-1+\varepsilon]$, $\varepsilon<\varepsilon_n$, carries an Einstein metric with $\lambda<0$ obtained by perturbing $M$'s own metric. The reason to expect this, and the reason it is *target-independent* where the entropy route is not: the mechanism is pointwise. The linearized Einstein operator in Bianchi gauge on transverse-traceless symmetric $2$-tensors is
$$
\mathcal L_g=\tfrac12\Delta_L-\lambda,\qquad \Delta_L h=\nabla^*\nabla h+\mathrm{Ric}\!\cdot\!h+h\!\cdot\!\mathrm{Ric}-2\mathring R h,\quad (\mathring R h)_{ij}=R_{ikjl}h^{kl}.
$$
For constant curvature $-1$, $\mathring R h=-h$ on TT tensors and $\mathcal L_g$ is strictly positive (Koiso rigidity of hyperbolic Einstein metrics, $n\ge3$, modulo the finitely many exceptional situations tied to small eigenvalues of the Hodge Laplacian). The curvature term $-2\mathring R$ is controlled *pointwise* by the sectional curvatures, so under $\mathrm{sect}\in[-1-\varepsilon,-1+\varepsilon]$ one gets a coercivity constant $c(n,\varepsilon)>0$ that is bounded below independent of the target. Bounded geometry — a lower injectivity-radius bound uniform across all hyperbolic covers by the Margulis lemma (BBCG cite this) plus the two-sided curvature bound — gives uniform elliptic Schauder constants, and the Ricci defect $\|\mathrm{Ric}_g+(n-1)g\|\lesssim(n-1)\varepsilon$ is small. An inverse-function-theorem step then produces a genuine Einstein metric on the *same* smooth $M$. If Theorem A holds, Farrell–Jones exotics all carry $\lambda<0$ Einstein metrics, closing the refutation route and even yielding a dimension-only Yau-26 statement for the sectionally-pinched sub-family.

**The single computation that adjudicates the route.** Estimate, for TT tensors under $\mathrm{sect}\in[-1-\varepsilon,-1+\varepsilon]$,
$$
\langle(\Delta_L-2\lambda)h,\,h\rangle\ \ge\ c(n)\,\|h\|^2\quad\text{with }c(n)>0\text{ for }\varepsilon<\varepsilon_n,
$$
via the Weitzenböck term $-2\mathring R$ compared to $\nabla^*\nabla$, and pair it with the uniform injectivity-radius lower bound to bound the inverse operator. Whether $c(n)$ stays positive uniformly is exactly what flips Theorem R. This is a bounded, curvature-algebra computation (sign and size of $R_{ikjl}h^{kl}$ against $|h|^2$ for pinched sectional curvature) followed by an elliptic-estimate accounting — far cheaper and more decisive than any further sharpening of the entropy constant.

**The frontier that neither route touches — and the correct next object.** Theorem A, even if true, needs *sectional* pinching; Yau 26 hypothesizes only *Ricci* pinching, which does not control $\mathring R$ and hence does not deliver Weitzenböck coercivity. So the genuine difficulty of Yau 26 is exactly the wedge between $c_ng\le\mathrm{Ric}\le C_ng$ (weak, no full-curvature control) and sectional pinching. The productive counterexample search is therefore *not* exotic smoothings of hyperbolic manifolds (whose sectional pinching probably lends them Einstein metrics, per Theorem A) and *not* the entropy invariants (homotopy-blind to smooth structure). It is: closed manifolds carrying a Ricci-pinched metric with uncontrolled sectional curvature and no Einstein metric of any sign. Two concrete places to manufacture such candidates:

1. Sphere bundles / warped products where one can prescribe $\mathrm{Ric}$ in a narrow band while letting some sectional curvatures diverge, then test Einstein existence against $\pi_1$/χ/τ (dimension $4$) or against the sign trichotomy (higher dimensions, where only $\lambda<0$ or the positive front can host an obstruction). 
2. The positively-Ricci-pinched front forced by (ii): once $c_n\ge0$ is mandatory, the test manifolds are those with $0\le c_ng\le\mathrm{Ric}\le C_ng$, finite $\pi_1$, and the open Einstein-existence question — the same territory as the $\#_k(S^2\times S^2)$ bubbling analysis. A quantitative statement worth targeting here is whether $\mathrm{Ric}\ge0$ pinching plus a fixed upper Ricci bound forces a bounded number of "necks," which would connect the two fronts through a common non-collapsing count.

In short: the two routes in Step 47 resolve cleanly but oppositely — entropy is structurally homotopy-invariant and cannot decide smooth Einstein existence, while the exotic-smoothing candidates are governed by a pointwise Weitzenböck coercivity computation whose outcome determines whether they refute or support the $c_n<0$ window. Both push the real content of Yau 26 onto the same object: Ricci-pinched metrics *without* sectional control, on the positively-pinched side once the $c_n<0$ windows are settled.