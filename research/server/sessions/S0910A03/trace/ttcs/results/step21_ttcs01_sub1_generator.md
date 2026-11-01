# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step21_derivative_free_first_exit_and_plateau_regularity.md",
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md",
    "Sessions/S0910A03/workspace/notes/step19_p4_threshold_and_degenerate_moser.md"
  ]
}
```

## Task

The derivative-free first-exit framework reduces the 4D negative-branch cutoff-flow program to one PDE task: the localized zero-order Moser iteration for the degenerate normalized cutoff flow. Consider what alternative approaches or structural insights could bypass or simplify this remaining PDE localization.

Specifically: (A) Wang's proof is for the unnormalized cutoff Ricci flow on a complete manifold with global Sobolev and energy bounds. The needed adaptation is to finite-neighbor domains with normalized flow. What is the simplest way to extract the needed local estimates? Could the completed-manifold trick (extend the closed manifold trivially and apply Wang's global theorem) work? Could a time-layer argument avoid the nested-cutoff/evolving-measure complexity?

(B) Is there a more direct route to the calibrated contradiction that avoids the full Moser iteration? For example: if one only needs |Rm| bounded at some positive time on the plateau (not the sharp C/t rate), could a softer estimate suffice? The downstream needs are: (i) smooth compactness at fixed time T_0, (ii) defect → 0 on the limit, (iii) |W+| = 1/(2sqrt6) on the limit.

(C) A02's CZ spike audit shows that the weighted estimate is not broken by singular-kernel transplants. Could this stability property be used constructively to prove the estimate, e.g., by showing that the heat kernel of the degenerate operator dt - chi^2 Delta smooths faster than it generates curvature?

## Output

The strongest simplification is to recognize that Wang’s weighted moments are ordinary moments after a conformal/ground-state transformation. This opens a Nash–semigroup route that packages the entire infinite-exponent iteration into one \(L^2\!\to L^\infty\) estimate.

## A. Local extraction: literal completion versus conformal completion

A literal application of Wang’s global theorem to the original closed \(M\) does not remove the localization issue. Wang’s global critical quantity sees all of
\[
A_{\mathrm{glob}}^2\|\operatorname{Rm}\|_{L^2(M)},
\]
whereas the available small quantity is componentwise or ballwise. Attaching a cap to a local domain also does not automatically help: in four dimensions \(\int|\operatorname{Rm}|^2\) is invariant under scaling, so enlarging or shrinking the cap does not make its curvature energy small. Stationary curvature outside \(\operatorname{supp}\chi\) is harmless for the equation but is still counted by the stated global hypothesis.

There is, however, a different completion that exactly matches the cutoff powers. Put
\[
a=\chi^2,\qquad \Omega=\{a>0\},\qquad
\widehat g(t)=a^{-1}g(t),\qquad
d\nu_t=a^{-2}d\mu_{g(t)}.
\]
In dimension four, \(d\nu_t=d\mu_{\widehat g(t)}\). Since a smooth nonzero cutoff vanishes at most linearly in distance, \(\widehat g=\chi^{-2}g\) is complete toward the zero set of \(\chi\).

Define
\[
\mathcal K=aF,\qquad F=(1+|\operatorname{Rm}|^2)^{1/2},
\qquad
\mathcal U=a|E|,\qquad E=\operatorname{Ric}+g.
\]
Then the weighted quantities become exactly
\[
H_q=\int_\Omega a^{q-2}F^q\,d\mu
    =\int_\Omega \mathcal K^q\,d\nu,
\]
and
\[
J_m=\int_\Omega a^{m-2}|E|^m\,d\mu
    =\int_\Omega \mathcal U^m\,d\nu.
\]
Even the Wang Sobolev variables acquire a transparent interpretation:
\[
v_q=a^{(q-1)/2}F^{q/2}
    =a^{-1/2}\mathcal K^{q/2},
\]
\[
z_m=a^{(m-1)/2}|E|^{m/2}
    =a^{-1/2}\mathcal U^{m/2}.
\]
Thus the mysterious “two fewer powers of \(a\)” are simply the four-dimensional conformal volume factor \(a^{-2}\).

For \(\phi\in C_c^\infty(\Omega)\), the local Sobolev inequality for \(g(t)\) becomes
\[
\begin{aligned}
\|\phi\|_{L^4(\nu_t)}^2
&=\|a^{-1/2}\phi\|_{L^4(\mu_t)}^2\\
&\le C A^2\left[
 \int_\Omega\left|\nabla\!\left(a^{-1/2}\phi\right)\right|^2d\mu_t
 +r^{-2}\|\phi\|_{L^2(\nu_t)}^2
 \right].
\end{aligned}
\tag{A.1}
\]
Introduce the quadratic form
\[
\mathfrak e_t[\phi]
=
\int_\Omega\left|\nabla\!\left(a^{-1/2}\phi\right)\right|^2d\mu_t
+r^{-2}\|\phi\|_{L^2(\nu_t)}^2.
\tag{A.2}
\]
The critical curvature reaction is now an ordinary form perturbation:
\[
\int_\Omega \mathcal K\,\phi^2\,d\nu_t
\le
\|\mathcal K\|_{L^2(\nu_t)}
\|\phi\|_{L^4(\nu_t)}^2
\le
C A^2\|\mathcal K\|_{L^2(\nu_t)}\,\mathfrak e_t[\phi].
\tag{A.3}
\]
But
\[
\|\mathcal K\|_{L^2(\nu_t)}^2
=\int_\Omega F^2\,d\mu_t,
\]
so the coefficient in (A.3) is exactly the volume-independent parameter \(\gamma\). Once \(C\gamma<1\), curvature generation is a strictly form-subordinate perturbation of diffusion.

This reformulation suggests replacing the \(q\mapsto3q/2\) recurrence by the standard Nash argument for the nonautonomous form \(\mathfrak e_t\). The Sobolev inequality (A.1) implies a four-dimensional Nash inequality, and hence an evolution-family estimate of the form
\[
\|P(t,s)\|_{L^2(\nu_s)\to L^\infty(\nu_t)}
\le
C A^2(t-s)^{-1}
e^{C(t-s)(1+r^{-2})}.
\tag{A.4}
\]
The first-order cutoff terms are sector-form perturbations because
\[
\frac{|da|^2}{a}=4|d\chi|^2\le Cr^{-2}.
\]
The changing measure also fits the same form calculus:
\[
\frac{\partial_t d\nu_t}{d\nu_t}
=-\operatorname{tr}_g(aE),
\qquad
|\operatorname{tr}_g(aE)|\le C\mathcal K.
\tag{A.5}
\]
Thus evolving measure, inverse-metric variation, curvature reaction, and cutoff drift all enter either through the small form term (A.3) or through \(Cr^{-2}\|\phi\|_2^2\). The normalization contributes only zeroth-order terms of this latter type.

Geometrically, if \(u=\log\chi\), then on \(\Omega\)
\[
g=e^{2u}\widehat g
\]
and
\[
\partial_t\widehat g
=
-2\operatorname{Ric}_{\widehat g}
+\mathcal L_{2\widehat\nabla u}\widehat g
-4\,du\otimes du
+\bigl(2\widehat\Delta u+4|du|_{\widehat g}^2-2a\bigr)\widehat g.
\tag{A.6}
\]
After removing the Lie derivative, this is a uniformly parabolic Ricci-type equation on the complete conformal manifold, with fixed conformal-source terms. Formula (A.6) is useful geometrically; the weak form (A.2) is preferable analytically because it only uses \(|d\chi|\), while second cutoff derivatives are integrated by parts.

### Removing finite-neighbor coupling

There is also a combinatorial simplification. An equal-radius covering under the Ricci lower bound has uniformly bounded intersection degree. Its enlarged balls can be colored with \(N=N(n)\) colors so that the enlarged supports in each color are pairwise disjoint. For one color, choose \(\chi\) as the sum of the component cutoffs. Then
\[
\Omega=\bigsqcup_\alpha\Omega_\alpha
\]
is a disjoint union, and the flow on each component is analytically independent.

Componentwise smallness gives the global direct-sum form estimate
\[
\sum_\alpha\int_{\Omega_\alpha}\mathcal K\phi^2\,d\nu
\le
\varepsilon\sum_\alpha\mathfrak e_\alpha[\phi],
\]
even when the sum of all component curvature energies is large. The direct-sum heat operator has operator norm equal to the supremum of its component norms. This replaces the finite-neighbor matrix recurrence by a componentwise estimate. Since only finitely many colors occur, volume averaging and calibration can select a color after passage to a subsequence.

This is the useful version of the completed-manifold idea: not a trivial extension of \(M\), but a conformal completion of disjoint cutoff components.

## B. The downstream argument needs much less than the full pointwise hierarchy

At a fixed \(T_0>0\), smooth compactness only requires a curvature estimate on a slab such as
\[
P_{\mathrm{inner}}\times[T_0/2,T_0],
\]
not a carefully optimized estimate from time zero. Applying (A.4) to the scalar curvature subsolution with potential \(C\mathcal K\) gives
\[
\|\mathcal K(t)\|_\infty
\le
\frac{C A^2}{t}\|\mathcal K(0)\|_{L^2(\nu_0)}
+Cr^{-2}+C.
\tag{B.1}
\]
On the plateau this supplies
\[
\sup_{P\times[T_0/2,T_0]}|\operatorname{Rm}|
\le C(T_0,r,\gamma).
\]
Shi estimates then give all curvature derivatives on the inner plateau at \(T_0\).

The metric drift still needs an integrable estimate for \(aE\), but the exponent \(m=6\) is not essential once the heat evolution is available. Set
\[
w=|\mathcal U|^2=|aE|^2.
\]
The homogeneous defect equation makes \(w\) a scalar subsolution for the same form operator with potential \(C\mathcal K\). Applying the single \(L^2\!\to L^\infty\) estimate to \(w\) gives
\[
\|\mathcal U(t)\|_\infty
\le
C A\,t^{-1/2}\|\mathcal U(0)\|_{L^4(\nu_0)}.
\tag{B.2}
\]
Initial pointwise pinching yields
\[
\|\mathcal U(0)\|_{L^4(\nu_0)}^4
=
\int_\Omega a^2|E(0)|^4\,d\mu_0
\le \delta^4 V.
\]
Using \(A\le CrV^{-1/4}\),
\[
\boxed{\;
\|\mathcal U(t)\|_\infty
\le C\delta\,r\,t^{-1/2}
=C\delta\left(\frac{r^2}{t}\right)^{1/2}.
\;}
\tag{B.3}
\]
This is weaker near zero than the \(m=6\) rate, but still integrable:
\[
\int_0^{\theta r^2}\|\mathcal U(t)\|_\infty\,dt
\le C\delta r^2\sqrt{\theta}.
\tag{B.4}
\]
Hence \(J_4\), rather than \(J_6\), already closes metric comparability. No derivative estimate is involved.

Once curvature is bounded on the final slab, defect convergence can be obtained in either of two ways:

1. Directly from (B.3), since \(\delta_i\to0\) at fixed \(T_0\).
2. From triangular preservation of
   \[
   Q_i(t)=\int|E_i(t)|^2\,d\mu_{g_i(t)}
   \]
   followed by ordinary interior \(L^2\!\to L^\infty\) smoothing for the defect equation on \([T_0/2,T_0]\).

For calibration, only integral convergence is needed:
\[
\int\left(|W_i^+|-\frac1{2\sqrt6}\right)^2d\mu_{g_i(T_0)}
\longrightarrow0.
\]
Smooth convergence on a pulled-back ball then gives
\[
|W_\infty^+|\equiv\frac1{2\sqrt6}.
\]
Thus the analytic target can be reduced to:

- componentwise persistence of \(H_2\);
- one Nash ultracontractivity estimate for the curvature scalar;
- the same estimate applied to \(w=|aE|^2\);
- triangular preservation of the unweighted defect energy.

The entire high-exponent curvature and defect recurrences become unnecessary.

A flow-free alternative would require a collapse-independent harmonic-radius theorem of the following shape:
\[
A^2\|\operatorname{Rm}\|_{L^2(B_{2r})}\ll1,\qquad
\|\operatorname{Ric}+g\|_\infty\to0
\]
implies, after an appropriate local covering or pullback, uniform harmonic coordinates on \(B_r\). In such coordinates,
\[
-\frac12g^{ab}\partial_a\partial_b g_{\alpha\beta}
=
-g_{\alpha\beta}+E_{\alpha\beta}
+Q_{\alpha\beta}(\partial g),
\]
so \(E\to0\) would yield an Einstein weak limit and elliptic regularity would make it smooth. This would bypass Ricci flow altogether. The unresolved content is the harmonic-radius lower estimate at the critical \(L^2\) exponent in collapsed geometry. Relevant source families are Anderson harmonic-radius compactness, local-cover compactness under Ricci bounds, and critical-curvature compactness for four-manifolds. An integrated Derdziński argument alone introduces Cotton terms involving \(\nabla E\), so \(C^0\) pinching does not presently close that route.

## C. Constructive meaning of the CZ spike stability

The CZ spike calculation points directly to the form inequality (A.3). A curvature spike may be pointwise large, but its effect on every heat-energy mode satisfies
\[
\int \mathcal K\phi^2\,d\nu
\le C\gamma\,\mathfrak e[\phi].
\tag{C.1}
\]
For \(C\gamma<1\), the reaction absorbs only a fixed fraction of the diffusion form. This is the precise sense in which the heat operator smooths faster than curvature is produced.

A naive Duhamel estimate is less suitable. In four dimensions,
\[
\|P_t\|_{L^2\to L^\infty}\sim t^{-1},
\]
so inserting an \(L^2\) curvature potential into
\[
\int_0^tP_{t-s}(\mathcal K^2(s))\,ds
\]
encounters the critical logarithmic endpoint. The quadratic-form method avoids this endpoint convolution by treating \(C\mathcal K\) as part of the time-dependent Schrödinger operator.

The heat-kernel theorem naturally associated with the present problem is therefore:

> A nonautonomous, vector-valued evolution generated by \(\mathfrak e_t\), with first-order sector terms of size \(Cr^{-1}\), zeroth-order terms of size \(Cr^{-2}+C\), and a potential \(V_t\) satisfying
> \[
> \int V_t\phi^2\,d\nu_t\le\varepsilon\mathfrak e_t[\phi]
> +Cr^{-2}\|\phi\|_2^2,\qquad \varepsilon<1,
> \]
> obeys the four-dimensional Nash estimate
> \[
> \|P(t,s)\|_{2\to\infty}
> \le CA^2(t-s)^{-1}e^{C(t-s)(1+r^{-2})}.
> \]

The exact source families are nonautonomous sectorial forms with uniform Nash inequalities, Gaussian estimates for time-dependent Schrödinger forms with small \(L^{n/2}\) potentials, and vector-valued semigroup domination. Proving this lemma directly from the Nash differential inequality is also short: it uses one \(L^2\)-energy identity for the forward evolution, one for the adjoint evolution, and duality. It has no nested spatial cutoffs, no nested time intervals, and no exponent product.

In summary, the weighted Wang construction already contains a hidden global heat problem. The conformal measure \(a^{-2}d\mu\), the ground-state factor \(a^{-1/2}\), and the small form perturbation (C.1) provide a route from local critical energy directly to the two estimates actually needed:
\[
|a\operatorname{Rm}(t)|\lesssim t^{-1},
\qquad
|aE(t)|\lesssim \delta\,t^{-1/2}.
\]
Combined with disjoint-color localization, this can remove both the finite-neighbor recurrence and the full Moser hierarchy.