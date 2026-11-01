# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step14_smoothing_vs_reduction_route.md",
    "Sessions/S0910A01/workspace/notes/step13_normalized_accessibility_theorem.md",
    "Sessions/S0910A01/trace/ttcs/results/step13_ttcs01_generator1_integration.md",
    "Knowledge/objects/papers/Ricci-flow-smoothing-for-locally-collapsing-manifolds-arXiv--fd31dbed4f1f--11306ef80968/object.md"
  ]
}
```

## Task

Develop concrete mathematical bridges from localized Ricci-flow smoothing to the existing calibrated-Einstein-germ obstruction in the LeBrun negative branch. Assume a sequence with Ric+g -> 0, global calibrated W+ defect o(Vol), and a maximal-function set with bounded local |Rm|^2 mean. Explore two possibilities: (A) use local smoothing only to obtain bounded-curvature collapsed structure or cover charts and then transfer that chart/control back to the original metric where defects are small; (B) run a normalized/local Ricci flow and prove the Einstein error and calibrated W+ residual remain small at a fixed small time. Derive the relevant evolution/compactness estimates at a level sufficient to identify a plausible theorem or a decisive obstruction. Keep the rank-one reduced equations as context but do not assume exact symmetry.

## Output

### 1. Fixed-scale local input

Write
\[
E_i=\operatorname{Ric}_{g_i}+g_i,\qquad \|E_i\|_{L^\infty}\to0,
\]
and let \(\mathcal C(W_i^+)\) denote the calibrated spectral remainder. A convenient invariant representative for the target spectrum
\[
\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
is
\[
P(A)=A^2+\frac1{12}A-\frac1{72}I.
\]
For a trace-free symmetric endomorphism of \(\Lambda^+\), \(P(A)=0\) is equivalent to that spectrum.

If
\[
\fint_{B_{4r}(p_i)}|\operatorname{Rm}|^2\le K_0
\]
and \(q\in B_r(p_i)\), relative Bishop–Gromov comparison gives
\[
\fint_{B_r(q)}|\operatorname{Rm}|^2\le C_4K_0.
\]
Thus
\[
r^4\fint_{B_r(q)}|\operatorname{Rm}|^2\le C_4K_0r^4.
\]
Choosing one fixed \(r>0\) with \(C_4K_0r^4<\varepsilon_{\mathrm{Li}}\) supplies Ye Li’s dimensionless hypothesis at every center in a buffered region. What is still needed from the smoothing theory is an interior version of the all-centers theorem.

It is natural to convert Li’s unnormalized flow \(\bar g(s)\) to the normalization in which \(\operatorname{Ric}=-g\) is stationary:
\[
g(t)=e^{-2t}\bar g\!\left(\frac{e^{2t}-1}{2}\right),
\qquad
\partial_tg=-2(\operatorname{Ric}_g+g)=-2E.
\]

---

## 2. Exact evolution of the Einstein tensor

For the normalized flow,
\[
\boxed{
(\partial_t-\Delta)E_{ij}
=
2R_{ikjl}E^{kl}-2E_i{}^kE_{kj}.
}
\]
The variation of the metric in the norm cancels the cubic term, giving
\[
\boxed{
(\partial_t-\Delta)|E|^2
=
-2|\nabla E|^2
+
4R_{ikjl}E^{ij}E^{kl}.
}
\]
Hence
\[
(\partial_t-\Delta)|E|^2\le C|\operatorname{Rm}|\,|E|^2.
\]

The estimate \(|\operatorname{Rm}(t)|\le C/t\) alone is not enough to propagate \(\|E(0)\|_\infty=o(1)\) uniformly through a sequence. The scalar model
\[
y_i'(t)=\frac{C}{t+\kappa_i^{-1}}y_i(t),\qquad y_i(0)=\delta_i
\]
has
\[
y_i(t)=\delta_i(1+\kappa_it)^C,
\]
which can be order one at fixed \(t\) when \(\kappa_i\) grows rapidly relative to \(\delta_i^{-1}\). Thus a \(C/t\) curvature estimate must be supplemented by either an integrated Ricci estimate or a critical form estimate.

The critical form estimate has the correct four-dimensional scaling. A normalized local Sobolev inequality
\[
\left(\fint |\phi|^4\right)^{1/2}
\le
S\left(r^2\fint|\nabla\phi|^2+\fint\phi^2\right)
\]
and
\[
r^4\fint|\operatorname{Rm}|^2\le\varepsilon
\]
imply
\[
\boxed{
\int |\operatorname{Rm}|\,\phi^2
\le
S\varepsilon^{1/2}\int|\nabla\phi|^2
+
S\varepsilon^{1/2}r^{-2}\int\phi^2.
}
\tag{2.1}
\]
This remains meaningful in collapse because both hypotheses use volume-normalized quantities.

If (2.1) persists along the local flow with \(S\varepsilon^{1/2}\) small enough to absorb the gradient term, a cutoff energy computation gives
\[
\sup_{0<t\le\theta r^2}
\fint_{B_{2r}}|E(t)|^2
+
\fint_0^{\theta r^2}\!\!\int_{B_{2r}}|\nabla E|^2
\le
C\|E(0)\|_\infty^2.
\tag{2.2}
\]
On \([\theta r^2/2,\theta r^2]\), Li’s curvature estimate and parabolic mean-value estimates then yield
\[
\boxed{
\sup_{B_r}|E(\theta r^2)|
+
\sum_{m=1}^k(\theta r^2)^{m/2}
\sup_{B_r}|\nabla^mE(\theta r^2)|
\le C_{k,\theta}\|E(0)\|_\infty.
}
\tag{2.3}
\]

This suggests the following precise local smoothing theorem shape:

> **Local critical Einstein-stability theorem.**  
> Under two-sided Ricci control and the all-centers Li smallness condition on a buffered four-ball, the normalized interior flow exists for \(0<t\le cr^2\), satisfies \(|\operatorname{Rm}|\le C/t\), preserves a curvature form estimate of type (2.1), and obeys (2.2)–(2.3).

The new ingredient beyond the quoted statement of Li’s theorem is preservation of the form estimate. It is closely aligned with the small-critical-energy absorption already used in four-dimensional smoothing arguments.

---

# A. Smooth first, construct covers, then return to \(g_i(0)\)

This route does not require calibrated Weyl data to survive the flow.

## A.1 The exact metric-transfer quantity

For any normalized flow,
\[
\partial_t\log g(t)(v,v)
=
-2\frac{E(t)(v,v)}{g(t)(v,v)}.
\]
Define
\[
L_i(t_*)=\int_0^{t_*}\|E_i(t)\|_{\mathrm{op},\infty}\,dt.
\]
Then
\[
e^{-2L_i}g_i(0)\le g_i(t_*)\le e^{2L_i}g_i(0),
\tag{A.1}
\]
and
\[
e^{-4L_i}dV_{g_i(0)}
\le dV_{g_i(t_*)}
\le e^{4L_i}dV_{g_i(0)}.
\tag{A.2}
\]
Uniform boundedness of \(L_i\) is enough to transfer a fixed local volume anchor. The stronger estimate \(L_i\to0\), supplied by (2.3), makes the two metrics asymptotically identical in \(C^0\).

Neither \(|\operatorname{Rm}|\le C/t\) nor the Hölder distance estimate in the Huang–Wang appendix implies (A.1). An additive \(O(\sqrt t)\) distortion is comparable to the natural harmonic scale \(\sqrt t\). The relevant smoothing output for this route is therefore
\[
\int_0^{t_*}\|E(t)\|_\infty\,dt<\infty
\]
or, in unnormalized variables, an analogous integrated Ricci bound.

## A.2 Producing a topological cover at positive time

At \(t_*=\theta r^2\), the metric has bounded sectional curvature. On a region that is collapsed with full local nilpotent rank, bounded-curvature collapse theory produces an infranil structure and a normal cover
\[
\pi_i:\widetilde U_i\longrightarrow U_i
\]
on which the collapsing directions are unwrapped. Full rank gives
\[
\operatorname{Vol}_{\pi_i^*g_i(t_*)}
B_{\pi_i^*g_i(t_*)}(\tilde p_i,\rho)
\ge v_*\rho^4
\tag{A.3}
\]
for fixed \(v_*,\rho>0\).

This is exactly the mechanism appearing in Huang–Wang: their maximal nilpotency-rank assumption is what turns the local normal cover into an almost Euclidean cover. Energy smoothing by itself does not supply the rank equality.

The cover is topological, so it also carries \(\pi_i^*g_i(0)\). From (A.1)–(A.3),
\[
\operatorname{Vol}_{\pi_i^*g_i(0)}
B_{\pi_i^*g_i(0)}(\tilde p_i,C(L)\rho)
\ge c(L,v_*)\rho^4.
\tag{A.4}
\]

For rank one, the deck-counting interpretation is especially transparent. A cover ball spans roughly \(\rho/\ell_i\) fundamental circle tiles. Numerator and denominator in
\[
\fint_{\widetilde B}|\operatorname{Rm}(g_i(0))|^2
\]
acquire the same tile multiplicity. Bounded distortion of the tile geometry then gives
\[
\fint_{\widetilde B}
|\operatorname{Rm}(\pi_i^*g_i(0))|^2
\le C(L)\,K_0.
\tag{A.5}
\]
No exact circle action for \(g_i(0)\) is involved. The circle appearing after smoothing is used only to identify the covering subgroup and control deck multiplicities.

## A.3 Harmonic coordinates for the original metric

From (A.4), the original lifted metrics are noncollapsed at a fixed scale. From (A.5), at a smaller fixed radius \(s\),
\[
s^4\fint_{B_{2s}}|\operatorname{Rm}|^2
\le C K_0s^4
\]
can be made below the standard four-dimensional harmonic-radius threshold. Together with \(|\operatorname{Ric}|\le K\), this gives a uniform \(W^{2,p}\) harmonic radius for every finite \(p>4\).

The original tensors then pass directly to a limit:
\[
\pi_i^*g_i(0)\longrightarrow h
\quad\text{strongly in }W^{2,p}_{\mathrm{loc}}
\]
after harmonic gauge and a subsequence. Since
\[
\operatorname{Ric}_{g_i(0)}+g_i(0)\to0,
\]
the limit satisfies
\[
\operatorname{Ric}_h=-h,
\]
and elliptic bootstrapping makes \(h\) smooth. Strong \(W^{2,p}\) convergence gives strong local convergence of curvature in \(L^p\). Therefore any local average of the original calibrated remainder tending to zero implies
\[
P(W_h^+)=0.
\]
The limit has the forbidden calibrated Einstein germ. Derdziński’s repeated-eigenvalue mechanism makes it locally Kähler in the relevant orientation, whereas a Kähler–Einstein surface with scalar curvature \(-4\) has
\[
\operatorname{Spec}(W^+)=\left(-\frac23,\frac13,\frac13\right),
\]
not the calibrated profile.

Thus route A reduces to two quantitative statements:

1. the smoothed collapse has full local nilpotent rank on a positive-volume part of the calibrated bulk;
2. the normalized flow has uniformly bounded integrated Einstein tensor, preferably \(L_i(t_*)\to0\).

The first is topological; the second is parabolic.

---

# B. Use the smoothed metrics themselves

Under the local stability theorem above, (2.3) gives
\[
E_i(t_*)\to0
\quad\text{in }C^k
\]
on interior subballs for every fixed \(k\). On any full-rank normal cover furnished by the smoothed geometry, curvature and injectivity estimates give smooth compactness:
\[
\pi_i^*g_i(t_*)\longrightarrow h,
\qquad
\operatorname{Ric}_h=-h.
\]
The remaining issue is calibration at time \(t_*\).

## B.1 Direct Weyl transport requires more than \(E=o(1)\)

For a metric variation \(\dot g=-2E\),
\[
\partial_tW^+
=
\Pi_+\bigl(\nabla^2E\bigr)
+
\operatorname{Rm}*E,
\tag{B.1}
\]
where changes of the Hodge splitting are included in the algebraic term. Consequently,
\[
|\partial_tP(W^+)|
\le
C(1+|W^+|)
\left(|\nabla^2E|+|\operatorname{Rm}|\,|E|\right).
\tag{B.2}
\]
The derivative estimate \(|\nabla^2E(t)|\le C\delta_i/t\) leads to a logarithm near \(t=0\). Therefore \(\|E_i(0)\|_\infty\to0\) and \(|\operatorname{Rm}|\le C/t\) do not by themselves give a uniform modulus for \(P(W_i^+(t_*))\).

A direct propagation theorem would follow from the stronger spacetime estimate
\[
\int_0^{t_*}\!\!\int
(1+|W^+|)
\left(|\nabla^2E|+|\operatorname{Rm}|\,|E|\right)
=o(\operatorname{Vol}).
\tag{B.3}
\]
Critical \(L^2\) energy estimates provide control of \(\nabla E\), but not immediately the \(L^1_tL^2_x\) control of \(\nabla^2E\) needed in (B.3). Parabolic maximal regularity adapted to the volume-normalized collapsed Sobolev inequality would be the relevant analytic result.

## B.2 Topological recalibration avoids Weyl transport

In the LeBrun setting, a better mechanism may be to reconstruct calibration at every time from topology and the monopole curvature inequality.

The exact Chern–Weil identity is
\[
4\pi^2(2\chi+3\tau)
=
\int_M
\left(
2|W^+|^2+\frac{s^2}{24}
-\frac12|\operatorname{Ric}_0|^2
\right)dV.
\tag{B.4}
\]
If \(E_i(t_*)\to0\), then
\[
s_i(t_*)=-4+o(1),\qquad
\operatorname{Ric}_{0,i}(t_*)=o(1),
\]
and (A.2) with \(L_i\to0\) gives
\[
\operatorname{Vol}(g_i(t_*))
=
\operatorname{Vol}(g_i(0))+o(\operatorname{Vol}).
\]
Since the initial calibrated profile has
\[
\fint |W_i^+(0)|^2=\frac1{24}+o(1),
\]
identity (B.4) determines the same norm at time \(t_*\):
\[
\boxed{
\fint |W_i^+(t_*)|^2
=
\frac1{24}+o(1).
}
\tag{B.5}
\]

The remaining spectral information is the repeated-eigenvalue saturation. If \(w(A)\) denotes the smallest eigenvalue of a trace-free symmetric \(3\times3\) matrix, then
\[
w(A)+\sqrt{\frac23}|A|\ge0,
\tag{B.6}
\]
with equality exactly for eigenvalues \((-2a,a,a)\). Combining (B.5), \(s=-4+o(1)\), and a metric-uniform LeBrun inequality involving \(s\) and \(w(W^+)\) would reproduce
\[
\int
\left[
w(W_i^+)+\sqrt{\frac23}|W_i^+|
\right]
=o(\operatorname{Vol}),
\]
together with concentration of \(|W_i^+|\) near \(1/\sqrt{24}\). This yields the calibrated spectrum at time \(t_*\) without estimating \(\partial_tW^+\).

The exact constants and equality remainder must come from the LeBrun/Seiberg–Witten curvature estimate used in `20260910.tex`. The relevant source family is: **LeBrun curvature inequalities expressed through the smallest eigenvalue of \(W^+\), monopole classes, and their equality decomposition**. If that inequality applies to every metric on the same smooth manifold, normalized Ricci flow preserves all topological inputs automatically.

---

## 4. Combined theorem shape

A theorem sufficient for the germ argument can be formulated as follows.

> Let \(g_i\) be four-dimensional metrics with \(\|{\rm Ric}_{g_i}+g_i\|_\infty\to0\), calibrated remainder \(o(\operatorname{Vol})\), and a positive-volume buffered set satisfying the all-centers Li energy condition at one fixed radius. Suppose the localized normalized flow:
>
> 1. preserves the curvature form estimate (2.1);
> 2. satisfies the Einstein stability estimates (2.2)–(2.3);
> 3. has, on a positive-volume part of that set, full-rank local nilpotent covers at time \(t_*=\theta r^2\).
>
> Then either:
>
> * the covers transfer to \(g_i(0)\), where critical-energy harmonic regularity produces the forbidden calibrated Einstein germ; or
> * the LeBrun topological remainder recalibrates \(W_i^+(t_*)\), and smooth cover compactness produces the same germ directly from \(g_i(t_*)\).

The rank-one reduced equations remain useful for interpreting what happens when item 3 is absent. Large derivative twist, represented by \(W^-\), can coexist with calibrated \(W^+\) and can drive complicated collapse. Smoothing converts that analytic behavior into a geometric alternative: either the short loop survives in the pseudo-local fundamental group and can be unwrapped, or the drop in metric dimension exceeds the nilpotent rank. The latter is a genuine topological obstruction to both transfer and direct smooth compactness; no exact circle symmetry assumption resolves it.

The two most informative missing source statements are therefore:

* an interior Ye Li theorem carrying the curvature form estimate and Einstein-tensor stability;
* the exact metric-uniform LeBrun remainder that upgrades (B.5) from Weyl norm control to the repeated calibrated spectrum.