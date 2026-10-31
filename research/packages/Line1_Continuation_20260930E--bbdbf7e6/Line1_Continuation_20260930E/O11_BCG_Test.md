# O11: direct test of the blowdown–entropy candidate

2026-09-30. This note tests one proposed global route: apply the degree-one blowdown map to the complex-hyperbolic base, then use entropy/natural-map Jacobian defects to pay the missing blow-up cost. The direct route does not close. In fact a classical theorem identifies exactly why entropy alone cannot count these surgeries.

## 1. What the degree theorem actually gives

Let
\[
M=X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3),
\quad V_0=2\pi^2A,
\quad h_0=4/\sqrt6,
\]
where the complex-hyperbolic metric on \(X\) has \(\operatorname{Ric}=-g\). Write \(e(g)\) for volume entropy, reserving \(h=Q/A\) for the project's surgery density. The collapsing map \(f:M\to X\) has degree one. Besson–Courtois–Gallot's main theorem, printed p.734, gives for every smooth \(g\)
\[
e(g)^4V_g\ge h_0^4V_0.\tag{1}
\]
It places no source Ricci assumption on this entropy-product inequality.

If one additionally assumed \(\operatorname{Ric}_g\ge-(1+\delta)g\), Bishop comparison would give \(e(g)\le\sqrt{3(1+\delta)}\), hence
\[
V_g\ge \frac{64}{81(1+\delta)^2}V_0.\tag{2}
\]
At \(\delta=0\), this still has fixed fractional slack relative to \(V_0\). For the actual negative Yamabe representatives, SW already gives \(V\ge V_0\). Thus even granting the missing pointwise Ricci hypothesis, this particular BCG–Bishop calculation cannot see an order-\(Q\) improvement when \(Q=o(A)\). This precise constant comparison was already present in the integrated manuscript's entropy section; it is not a new estimate.

## 2. A stronger obstruction: the full minimal entropy is exactly unchanged

Set
\[
\lambda(N)=\inf_g e(g)V_g^{1/4}.
\]
Brunnbauer–Ishida–Suárez-Serrato, *An essential relation between Einstein metrics, volume entropy, and exotic smooth structures*, arXiv:0807.1187v2, Theorem 1.1, proves
\[
\lambda(N\#Y)=\lambda(N)
\]
whenever \(Y\) is closed, connected, orientable, and nonessential. Both kinds of added summands here satisfy this condition: \(\overline{\mathbb{CP}}^2\) is simply connected; the classifying map of \(S^1\times S^3\) factors through \(S^1\), which has dimension less than four. Applying the theorem successively and then BCG on \(X\) gives the exact formula
\[
\boxed{\lambda(M)^4=h_0^4V_0=\frac{128\pi^2}{9}A,}
\tag{3}
\]
independently of \(k\) and \(\ell\).

Consequently the nonnegative entropy defect
\[
\mathcal D_{\rm ent}(g)=e(g)^4V_g-h_0^4V_0
\]
satisfies
\[
\boxed{\inf_g\mathcal D_{\rm ent}(g)=0}
\tag{4}
on every one of these surgery manifolds. In particular no inequality \(\mathcal D_{\rm ent}(g)\ge c k\), or \(\ge cQ\), with \(c>0\) can hold for all metrics. Equality rigidity of an individual metric does not change this vanishing infimum.

This also prevents an argument that tries to assign a fixed positive surgery charge to an unweighted natural-map Jacobian deficit bounded by the entropy-product defect. Such a charge would contradict (4). Curvature-weighted Jacobian information is not ruled out; it would be a genuinely additional estimate and is not supplied by (1).

The minimizing metrics in (4) are **not** asserted to be \(P\)-near-minimizers, to have \(s=-4\), or to satisfy the project's derivative budgets. Thus (4) is not a counterexample to O11. It excludes the proposed unrestricted positive entropy-defect charge and identifies the extra coupling a useful proof would need.

## 3. Constant scalar curvature does not supply the missing entropy comparison

On a selected \(s=-4\) representative, \(\operatorname{Ric}=-g+Z\), \(\operatorname{tr}Z=0\). Let
\[
\rho_{-1/3}=(-1-\lambda_{\min}(\operatorname{Ric}))_+.
\]
For a traceless symmetric four-by-four matrix,
\( -\lambda_{\min}(Z)\le\sqrt3\,|Z|/2\). Therefore the actual budget only yields
\[
\|\rho_{-1/3}\|_{L^2_{\rm av}}
\le\frac{\sqrt3}{2}\sqrt{P/V}=O(\sqrt h).\tag{5}
\]
This is the critical exponent \(p=n/2=2\). It is neither a pointwise Ricci bound nor an \(L^p\) bound for any \(p>2\), nor a local ball-average bound on the universal cover. Constant trace does not upgrade an eigenvalue's integrability.

The improvement by Chen–Wei, *Improved relative volume comparison for integral Ricci curvature and applications to volume entropy*, Theorem 1.4, explicitly assumes \(p>n/2\), a diameter upper bound, and sufficiently small averaged negative Ricci error; its constants depend on these data. In four dimensions the hypotheses needed to apply it are absent here. Aubry, arXiv:0810.0149, §1.4, explicitly discusses failure of the general entropy comparison at \(p\le n/2\). Those general counterexamples are not claimed to satisfy all O11 field conditions.

The previously constructed near-stationary metrics satisfy a dual variation estimate. That estimate does not itself give the higher integrability or diameter control needed above; deriving such a conclusion would require a new regularity/coercivity theorem.

## 4. The exact missing connection and outcome

The desired target is
\[
\frac{S-32\pi^2A}{12}+4\int|W^-|^2
\ge48\pi^2k-o(Q).
\tag{6}
\]
With \(S=16V\), it is equivalently
\[
V-V_0+3\int|W^-|^2\ge36\pi^2k-o(Q).
\]
Neither the entropy product in (1), nor its optimal value in (3), supplies the right-hand exceptional count. The proposed route needs a new estimate linking the curvature carried by the topology collapsed by \(f\) to a curvature-weighted natural-map defect, uniformly for the actual \(P\)-near-minimizers. No such estimate has been derived here.

Therefore the standard BCG/entropy comparison does not settle O11, even after replacing a rough entropy lower bound by the exact minimal entropy. Its failure is structural, not a missing optimization of the constant in (2).

## Primary sources checked

1. Besson, Courtois, Gallot (1995), main theorem and Ricci-volume discussion, printed pp.734–735: https://www.aimath.org/WWN/entropyrigidity/papers/BessonCourtoisGallot.pdf .
2. Brunnbauer, Ishida, Suárez-Serrato, arXiv:0807.1187v2, Theorem 1.1 and §2: https://arxiv.org/pdf/0807.1187 .
3. Aubry, arXiv:0810.0149, §1.4: https://arxiv.org/pdf/0810.0149 .
4. Chen–Wei, Theorem 1.4: https://web.math.ucsb.edu/~wei/paper/Chen-Wei2021.pdf .
