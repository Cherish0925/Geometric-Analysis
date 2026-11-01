# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 60,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step60_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step60_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify Part B of the Step-59 note (zero-gap structure) with Part C.4. Check: (1) Prop 59.N: the O(lambda^2) estimate for gluing Ricci-flat ALE trees into Einstein orbifolds of any sign (decay rates, curvature on the annulus, tree induction, orientation compatibility). (2) Prop 59.C: alpha <= 36 Vol_{|r|} with LeBrun's normalization, and the claims that MinVol=0 forces chi=tau=0 and that alpha is never attained on S^1xY (Y hyperbolic/spherical), S^2xT^2, Kodaira surfaces. (3) Prop 59.D: the explicit warped-product interpolations: the real-hyperbolic double (curvatures -(f'^2-f''), -f'^2, volume O(e^{-3T})), the complex-hyperbolic Heisenberg-cusp double (is curvature really bounded when base scales e^{-f} and fibre e^{-2f}, including the mixed terms with f', f''?), and the T^3-cusp Dehn filling for every slope (flattening path of flat metrics on T^3 at scale e^{-T}, turnaround, exponential growth of the gamma-circle while the T^2 stays at size e^{-T}, round cap; volume O(e^{-2T})). Also whether the fillings and doubles are smooth closed manifolds with the claimed topology, and whether 'no Einstein warped T^3 x I neck' supports the stated openness for doubles. (4) Theorem 59.Z: whether Anderson's Theorem 4.10 (read the Knowledge object provided; note his case labels and hypotheses) plus lower semicontinuity of P on compact subsets of the regular set really yields the trichotomy (I) Einstein orbifold, (III) finite-volume complete Einstein domain with s<0 and F-structure complement, (II) total collapse, as stated; whether the minimizers of Z_eps = P + eps int (1+|Ric|^2)^p have P -> alpha; the arguments excluding Ricci-flat and positive Omega in (III); what extra hypotheses are silently used (e.g. local minimality, convergence class); and whether 'attainment iff Einstein' is correctly scoped. Return a direct scientific memo with corrected statements.

## Integrated Scientific Memo

# Scientific memo: Step 59, Part B and C.4

Write
\[
P(g)=\int_M|\operatorname{Ric}^{\circ}_g|^2\,d\mu_g,
\qquad \alpha(M)=\inf_g P(g).
\]
The three upper-bound constructions are valid after making their decay, interpolation, and topology hypotheses explicit. Anderson’s theorem gives an **existential decomposition for specially selected minimizing sequences**, not a classification of arbitrary zero-defect sequences. In the zero-gap case, completeness can be recovered componentwise from the Einstein equation and Anderson’s Remark 4.12; negativity follows for every **noncompact** component, but the supplied theorem does not explicitly exclude compact components in a proper-domain configuration.

## 1. Proposition 59.N: ALE-tree gluing

### Local estimate

Suppose the orbifold metric and ALE metric, in matched cone coordinates, satisfy
\[
|\partial^j(g_V-\delta)|\le Cr^{2-j},
\qquad
|\partial^j(g_N-\delta)|\le CR^{-\tau-j},
\quad j=0,1,2,
\]
for some \(\tau>0\). Under scaling by \(\lambda^2\), with \(x=\lambda y\), the ALE metric becomes
\[
g_{N,\lambda}(x)=\delta+q(x/\lambda),
\qquad
|\partial^j q(x/\lambda)|\le C\lambda^\tau r^{-\tau-j}.
\]
In particular, order-four decay gives a metric error \(O(\lambda^4r^{-4})\), **not** \(O(\lambda^6r^{-4})\).

Interpolate on \(t\le r\le2t\) using a cutoff with \(j\)-th derivatives \(O(t^{-j})\). Provided \(t\to0\) and \(\lambda/t\to0\), the interpolation remains uniformly comparable to the cone metric, and
\[
|\operatorname{Rm}|\le C\bigl(1+\lambda^\tau t^{-\tau-2}\bigr).
\]
Its volume is \(O(t^4)\), hence
\[
P_{\rm ann}
\le Ct^4\bigl(1+\lambda^\tau t^{-\tau-2}\bigr)^2
\le C\left(t^4+(\lambda/t)^{2\tau}\right).                 \tag{1}
\]
Outside these annuli, \(\operatorname{Ric}^{\circ}=0\) exactly. The sign of the Einstein constant of \(g_V\) is irrelevant.

For \(\tau\ge2\), \(t=\sqrt\lambda\) yields
\[
|\operatorname{Rm}|\le C,\qquad P_{\rm ann}=O(\lambda^2).
\]
For \(\tau=4\), this is precisely the note’s displayed estimate
\[
|\operatorname{Rm}|\le C(1+\lambda^4t^{-6}).
\]
Positive decay alone suffices for zero gap: choosing
\[
t=\lambda^{\tau/(\tau+2)}
\]
gives
\[
P_{\rm ann}=O\!\left(\lambda^{4\tau/(\tau+2)}\right)\to0.
\]

Thus the \(O(\lambda^2)\) assertion needs derivative-controlled decay of order at least two, not necessarily order four. The supplied Anderson object cites Bando–Kasue–Nakajima but does not reproduce its precise asymptotic theorem. The proposition should either state the decay hypothesis explicitly or supply the precise result giving it for the ALE class used.

### Trees and orientation

For a **finite** ALE orbifold tree, perform each insertion in the parent’s native scale, in disjoint neighborhoods of its singular points. Because \(P\) is scale invariant, the total defect is bounded by the sum of the relative-scale annular errors. With order \(\ge2\) at every end, a common relative parameter \(\lambda\) gives \(O(\lambda^2)\) for the finite tree; nested parameters also give a diagonal sequence with defect tending to zero. All terminal pieces must be smooth.

“Compatible orientation” requires a cone-end identification, not merely an abstract isomorphism of groups: the end action must match the local \(\Gamma\)-action through an orthogonal conjugacy, and the boundary identification must reverse induced boundary orientations. An orientation mismatch can be repaired by reversing the ALE space’s orientation; Ricci-flatness and \(P\) are orientation independent.

**Corrected proposition.** A smooth closed manifold obtained from a compact Einstein orbifold with isolated irreducible cone points by compatible finite Ricci-flat ALE-tree replacements has \(\alpha=0\). The stated rate holds with derivative-controlled ALE order \(\ge2\).

This construction does not automatically treat a reducible vertex with several cone branches: that requires an appropriate replacement matching all branches.

### Attainment in the examples

The sentence concerning canonical models should distinguish two claims:

- the minimal resolution has \(\alpha=0\);
- its given complex structure admits a negative Kähler–Einstein metric iff \(K_X\) is ample.

The supplied argument does **not** prove that existence of an unrestricted Einstein metric is equivalent to ampleness. For unrestricted attainment, retain only “attained iff the underlying smooth manifold admits an Einstein metric.”

## 2. Proposition 59.C: normalization, collapse, and nonattainment

### The constant \(36\)

With the spectral Ricci normalization intended by \(\operatorname{Vol}_{|r|}\),
\[
-3g\le\operatorname{Ric}\le3g.
\]
If \(\rho_1,\ldots,\rho_4\) are the Ricci eigenvalues,
\[
|\operatorname{Ric}^{\circ}|^2
=\sum_i\rho_i^2-\frac14\left(\sum_i\rho_i\right)^2
\le36.
\]
Consequently,
\[
\boxed{\alpha(M)\le36\,\operatorname{Vol}_{|r|}(M)
                  \le36\,\operatorname{MinVol}(M).}       \tag{2}
\]
The second inequality follows because \(|K|\le1\) implies every Ricci eigenvalue lies in \([-3,3]\). The pointwise constant \(36\) is algebraically sharp, with equality for eigenvalues \(3,3,-3,-3\); this does not assert sharpness of the global invariant comparison.

The note’s proof mixes two norms: under the spectral bound, the tensor norm satisfies \(|\operatorname{Ric}|^2\le36\), not \(|\operatorname{Ric}|\le3\). If a different invariant were defined using the tensor-norm bound \(|\operatorname{Ric}|_{\rm HS}\le3\), its coefficient would be \(9\), and the second comparison in (2) would not follow with that same normalization.

### Minimal volume and topology

If \(|K_{g_i}|\le1\) and \(\operatorname{Vol}(g_i)\to0\), full curvature is uniformly bounded. Euler and signature densities are quadratic curvature polynomials, so
\[
|\chi(M)|+|\tau(M)|\le C\operatorname{Vol}(g_i)\to0.
\]
Therefore
\[
\boxed{\operatorname{MinVol}(M)=0\Longrightarrow
       \chi(M)=\tau(M)=0.}
\]
This is a necessary condition for bounded-sectional-curvature total collapse, not a converse.

For the general \(F\)-structure assertion, use the standard sufficient hypothesis of a **polarized positive-rank \(F\)-structure**, or an explicit bounded-curvature collapsing sequence. A bare \(F\)-structure should not silently be identified with \(\operatorname{MinVol}=0\).

### The nonattainment examples

An Einstein metric on a closed four-manifold with \(\chi=0\) satisfies
\[
0=8\pi^2\chi
 =\int_M\left(|W|^2+\frac{s^2}{24}\right)d\mu,
\]
so it is flat. Here \(\tau=0\) is redundant.

The listed examples admit bounded-curvature collapse and do not admit flat metrics:

- \(S^1\times Y\), \(Y\) closed hyperbolic: \(\pi_1\) is not virtually abelian.
- \(S^1\times Y\), \(Y\) spherical: \(\pi_1\) is virtually \(\mathbb Z\), whereas a closed flat four-manifold has fundamental group virtually \(\mathbb Z^4\).
- \(S^2\times T^2\): it is not aspherical.
- Primary Kodaira surfaces, and secondary Kodaira surfaces through their finite primary cover: their fundamental groups are not virtually abelian.

Thus these manifolds have \(\alpha=0\) and no smooth attaining metric. This conclusion is sound.

## 3. Proposition 59.D: explicit partial-collapse constructions

### 3.1 Real-hyperbolic doubles

For
\[
g=dt^2+e^{-2f(t)}g_N,\qquad g_N\ \text{flat},
\]
put \(a=e^{-f}\). Then
\[
K(\partial_t,X)=-a''/a=f''-(f')^2,\qquad
K(X,Y)=-(a'/a)^2=-(f')^2.
\]
Choose a fixed-length smooth reflection collar matching \(f=t\) near one end and the reversed cusp coordinate near the other, with
\[
f\ge T-O(1),\qquad |f'|+|f''|\le C.
\]
The metric matches the cusp metrics to all orders and has uniformly bounded curvature. Its volume is \(O(e^{-3T})\).

There is also an exact defect formula. With \(u=f'\), \(q=f''\), the Ricci eigenvalues are
\[
3(q-u^2),\quad q-3u^2,\quad q-3u^2,\quad q-3u^2,
\]
so
\[
|\operatorname{Ric}^{\circ}|^2=3(f'')^2.
\]
Hence
\[
P_{\rm neck}
=3\operatorname{Vol}(N,g_N)
  \int (f'')^2e^{-3f}\,dt
=O(e^{-3T}).
\]
All other regions are hyperbolic and contribute zero defect.

Doubling **all** boundary components of a compact truncation gives a smooth closed oriented manifold. The identity identification of corresponding cusp sections is orientation reversing as a map between the induced boundaries of \(H_T\) and \(\overline{H_T}\). Its diffeomorphism type is independent of \(T\).

### 3.2 Complex-hyperbolic Heisenberg doubles: mixed curvature terms

Locally take Heisenberg forms
\[
d\eta_1=d\eta_2=0,\qquad d\theta=\kappa\,\eta_1\wedge\eta_2.
\]
For
\[
g=dt^2+e^{-2f}(\eta_1^2+\eta_2^2)+e^{-4f}\theta^2,
\]
the orthonormal coframe
\[
\omega^0=dt,\quad \omega^1=e^{-f}\eta_1,\quad
\omega^2=e^{-f}\eta_2,\quad \omega^3=e^{-2f}\theta
\]
satisfies
\[
d\omega^1=-f'\omega^0\wedge\omega^1,\quad
d\omega^2=-f'\omega^0\wedge\omega^2,
\]
\[
d\omega^3=-2f'\omega^0\wedge\omega^3
          +\kappa\,\omega^1\wedge\omega^2.                \tag{3}
\]
Thus connection coefficients are linear in \(f'\) and \(\kappa\); curvature coefficients are combinations of \(f''\), \((f')^2\), \(\kappa f'\), and \(\kappa^2\). No exponentially growing coefficient occurs.

For example, the coordinate-plane sectional curvatures are
\[
\begin{aligned}
K_{01}=K_{02}&=f''-(f')^2,\\
K_{03}&=2f''-4(f')^2,\\
K_{12}&=-\tfrac34\kappa^2-(f')^2,\\
K_{13}=K_{23}&=\tfrac14\kappa^2-2(f')^2.
\end{aligned}
\]
The additional Codazzi/off-diagonal curvature components have size \(O(|\kappa f'|)\). Equation (3) therefore verifies the **full curvature bound**, including the mixed terms omitted from the original proof.

The volume density is \(e^{-4f}\), giving
\[
\operatorname{Vol}(\text{neck})=O(e^{-4T}),
\qquad P_{\rm neck}=O(e^{-4T}).
\]
The construction descends to an infranil cusp quotient because it uses the invariant horizontal metric and vertical metric, rather than a globally chosen coframe. The double is smooth and closed.

### 3.3 Every primitive \(T^3\)-slope can be filled with zero gap

Fix a primitive \(\gamma\in H_1(T^3;\mathbb Z)\), extend it to an integral basis, and use the resulting identification
\[
T^3\cong S^1_\gamma\times T^2.
\]
Attach \(D^2\times T^2\) so that \(\partial D^2\) represents \(\gamma\). This is a smooth manifold attachment; primitivity ensures an embedded meridian rather than a multiple-cover core.

Two missing matching steps should be included explicitly.

**Flat-metric transition.** The original flat cusp metric need not split orthogonally in this basis. On a fixed interval choose a smooth positive-definite path \(G(s)\), and use
\[
ds^2+e^{-2T}G(s).
\]
Choose \(G(s)=e^{-2s}G_{\rm cusp}\) near the incoming endpoint, and a constant product metric adapted to \(\gamma\) near the outgoing endpoint. Every slice is flat, and its shape operator is
\[
L=\tfrac12G^{-1}G',
\]
independent of \(T\). Gauss–Codazzi gives bounded full curvature from fixed bounds on \(G,G^{-1},G',G''\). This collar has volume \(O(e^{-3T})\).

**Turnaround, growth, and cap.** Continue with
\[
ds^2+a(s)^2d\theta^2+e^{-2T}g_{T^2}.
\]
Writing \(a=e^q\), curvature is controlled by
\[
a''/a=q''+(q')^2.
\]
Fixed-length transitions can change \(q'\) from \(0\) to \(-1\), then to \(+1\), while \(a\asymp e^{-T}\). Their curvature is bounded and volume \(O(e^{-3T})\). On the long growth segment,
\[
a(s)=a_0e^s,\qquad a_0\asymp e^{-T},
\]
until \(a\) reaches a fixed positive size. Its length is \(T+O(1)\), but its volume is
\[
e^{-2T}\int_0^{T+O(1)}a_0e^s\,ds=O(e^{-2T}),
\]
without an extra factor \(T\).

An exponential segment does not directly match a round cap. Insert a fixed-size positive-radius transition, then an exact round cap. At the disk center, with \(\theta\) of period \(2\pi\), require
\[
a(\rho)=\rho+O(\rho^3)
\]
and the usual odd smooth expansion. This removes any cone singularity. The transition and cap have bounded curvature and volume \(O(e^{-2T})\).

Therefore, for each fixed primitive slope,
\[
\boxed{P(g_T)\le C_\gamma e^{-2T}\to0.}
\]
Constants may depend on the slope; no uniformity over slopes is needed. All remaining cusps must also be filled or paired for the result to be closed.

### 3.4 C.4: filling literature and the warped-neck assertion

The supplied material records, but does not supply the underlying Anderson–Bamler filling papers, that sufficiently long slopes admit negative Einstein fillings. Subject to the precise hypotheses of those results:

- every primitive filling has \(\alpha=0\) by the interpolation above;
- sufficiently long fillings attain zero by an Einstein metric;
- the construction does not decide attainment for the remaining slopes.

The “finite short-slope test family” is literally finite for one fixed cusp. With several cusps, finitely many excluded slopes **per cusp** do not imply finitely many excluded slope tuples.

For a fixed long-slope manifold, its Einstein metric gives a compact minimizing sequence, while the interpolation gives another minimizing sequence with a cusped limit. Einstein fillings as slopes tend to infinity generally vary the underlying manifold; this is not one Anderson sequence on a fixed \(M\).

For an isotropic flat neck,
\[
g=dt^2+\phi(t)^2g_{\rm flat},
\]
the Einstein equations give
\[
\phi\phi''=(\phi')^2,\qquad
\phi=Ce^{ct}.
\]
The constant solution is a flat product; nonconstant solutions are monotone cusp segments. Thus there is **no turning isotropic Einstein neck matching the two cusp derivatives**. Saying “no Einstein \(T^3\times I\) neck exists” is false: exponential Einstein segments exist.

This ansatz obstruction neither rules out arbitrary Einstein metrics on doubles nor establishes the literature status of their existence problem. The supplied sources give no Einstein construction or general obstruction for the doubles. Any claim of current openness needs separate source support.

The exact formula \(2\operatorname{Vol}(H)/v_4\) for the double’s simplicial volume belongs to the real-hyperbolic setting; it should not be carried over unchanged to complex hyperbolic surfaces.

## 4. Theorem 59.Z: what Anderson actually implies

### Regularized minimizing values

On unit-volume smooth metrics let
\[
Q_p(g)=\int(1+|\operatorname{Ric}|^2)^p\,d\mu,\qquad
m_\varepsilon=\inf(P+\varepsilon Q_p).
\]
For fixed \(p>1\), and every smooth competitor \(h_\delta\) with \(P(h_\delta)\le\alpha+\delta\),
\[
\alpha\le m_\varepsilon
\le\alpha+\delta+\varepsilon Q_p(h_\delta).
\]
Thus \(m_\varepsilon\to\alpha\). Smooth exact minimizers, if they exist, or smooth \(o(1)\)-minimizers satisfy
\[
\alpha\le P(g_\varepsilon)
\le m_\varepsilon+o(1),
\]
hence \(P(g_\varepsilon)\to\alpha\). The same argument works for \(p_\varepsilon\to1\), since \(Q_{p_\varepsilon}(h_\delta)\) remains bounded for each fixed smooth competitor.

Anderson’s Corollaries 4.4 and 4.8 produce **idealized minimizing pairs on orbifold domains**, not necessarily smooth global minimizers on \(M\). One cannot automatically apply \(P\ge\alpha(M)\) to such a domain pair. For the forward implication at \(\alpha=0\), this distinction is harmless:
\[
0\le P(\Omega_\varepsilon,g_\varepsilon)
\le Z_\varepsilon(\Omega_\varepsilon,g_\varepsilon)
\le m_\varepsilon\to0.
\]
Alternatively, use the smooth approximating sequences provided in Theorem 4.10.

The relation to \(\mathcal R^2\) is normalization-dependent. Anderson’s displayed equation (3.3) gives
\[
\mathcal R^2=8\pi^2\chi+P
\]
in his curvature norm; with the full four-index tensor norm this becomes \(32\pi^2\chi+4P\). Both give the same minimizing problem on a fixed manifold.

### Einstein regular limits and bubbles

For any compact regular subset \(K\), smooth convergence after pullback gives
\[
\int_K|\operatorname{Ric}^{\circ}_{g_0}|^2\,d\mu_{g_0}
\le\liminf_iP(g_i)=0.
\]
Thus the regular limit is Einstein, with scalar curvature constant on each connected regular component. Local smooth convergence is stronger than the lower semicontinuity needed here.

The same argument applies to smoothly convergent bubble rescalings because \(P\) is scale invariant. A zero-\(P\) ALE bubble is Einstein, and its decay at infinity forces its scalar curvature to vanish; it is therefore Ricci-flat. This conclusion needs bubble-scale convergence, not just convergence of the bulk.

Anderson’s theorem initially gives only a \(C^0\) extension at cone points. Calling the limit a smooth Einstein orbifold additionally uses Einstein removable-singularity regularity on each local branch.

### Completeness: recoverable in the zero-gap case

Theorem 4.10 does not assert completeness in general. However, Remark 4.12 explicitly states that a uniform Ricci lower bound yields completeness of the maximal domain, since finite-distance collapse is ruled out by Bishop–Gromov comparison.

Once a connected component is Einstein,
\[
\operatorname{Ric}=\frac{s}{4}g
\]
provides exactly such a lower bound on that component. Thus completeness is recovered **componentwise** in the zero-gap situation. It need not be imposed as an independent conjectural assumption here.

For every complete noncompact component:

- \(s>0\) is excluded by Myers;
- \(s=0\) is excluded by infinite volume of complete noncompact Ricci-flat spaces, as also used in Anderson’s Remark 4.3(i).

Therefore
\[
\boxed{s<0\quad\text{on every noncompact connected component}.}
\]
The supplied theorem allows reducibility and does not explicitly exclude compact components inside a proper-domain configuration. The stronger assertion “all of \(\Omega\) has \(s<0\)” needs that exclusion. There need not be one scalar constant shared by all components.

### Corrected structure statement

Assuming Anderson’s Theorem 4.10 and the regularity inputs above, if \(\alpha(M)=0\), **there exists a selected minimizing sequence** exhibiting one of:

1. **Compact configuration:** a compact, possibly reducible orbifold \(V\), associated to \(M\), of volume \(1\), Einstein on its regular branches; smooth Einstein-orbifold extension uses removability.
2. **Nonempty-domain configuration:** a nonempty maximal orbifold domain \(\Omega\), weakly embedded in \(M\), of total volume \(0<\operatorname{Vol}\Omega\le1\), Einstein and complete componentwise. Every noncompact component has negative scalar curvature. Outside sufficiently large compact subsets, the selected sequence collapses along \(F\)-structures with locally bounded curvature away from finitely many shrinking balls.
3. **Total collapse:** \(\Omega=\varnothing\), with the corresponding collapse and \(F\)-structures away from finitely many shrinking balls.

These are Theorem 1.1’s three labels. **Theorem 4.10 has only (I) and (II)**, its (II) including both nonempty domains and total collapse.

The alternatives describe possible selected degenerations, not mutually exclusive properties of \(M\). Proposition 59.D’s long-slope examples already show that one manifold can admit both a compact Einstein minimizing sequence and a cusped minimizing sequence.

### Hidden scope and topology

The smooth convergence machinery uses Anderson’s perturbed minimizing configurations, local minimality, and elliptic regularity. It does not apply automatically to an arbitrary sequence with \(P\to0\), or merely to arbitrary critical metrics. Remark 4.17 retains local minimality for the extension to critical-point moduli.

Anderson explicitly describes finite ALE-tree reconstruction in the discussion around (4.65), following Theorem 4.15. If that decomposition is invoked, it should be cited directly. Neither lower semicontinuity alone nor the Step-58 hypothesis \(\mathrm H_{\rm sm}\) proves reconstruction: \(\mathrm H_{\rm sm}\) means trivial cone groups, not a no-neck/topology theorem. In general, “associated orbifold” should not be simplified to “collapsing essential homology cycles”; trivial-group and reducible vertices are allowed.

Finally,
\[
\boxed{\alpha(M)=0\text{ is attained by a smooth metric on }M
\iff M\text{ admits an Einstein metric}.}
\]
This follows directly from \(P(g)=0\iff\operatorname{Ric}^{\circ}_g=0\), independently of Anderson. It does not assert that positive infima cannot be attained, or that orbifold/domain attainment is smooth attainment on \(M\).

The supported unifying principle is therefore a **sufficient construction principle**: Einstein pieces joined by transition regions of vanishing \(P\)-energy yield zero gap. Anderson supplies a selected limiting decomposition in the reverse direction, but not the stronger claim that every zero-gap sequence has exactly these controlled transitions.