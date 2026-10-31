# Step 20: weighted Wang hierarchy, defect-moment compatibility, and Whitney correction

## 1. Scope

This note advances the cutoff-flow route for the four-dimensional negative critical Ishida–LeBrun laboratory. It does not prove a Ricci-pinching gap and does not settle Yau Problem 26. All PDE statements below are on a provisional first-exit interval on which the evolving metric is comparable to the initial metric, relative Sobolev inequalities persist on a finite-neighbor family, and the nested supports remain in buffered local-energy regions.

Let
\[
 \partial_t g=-2aE,\qquad E=\operatorname{Ric}+g,\qquad a=\chi^2,\quad 0\le a\le1,
\]
and regularize curvature by
\[
 F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]
The decisive correction to Step 19 is that Wang's cutoff powers must be preserved throughout the local iteration. The weighted cubic potential \(\int aF^3\) is not an unweighted Li potential in the transition region.

## 2. Curvature hierarchy

For a nested localization cutoff \(\eta_k\), define
\[
 H_{q,k}(t)=\int \eta_k^2 a^{q-2}F^q\,d\mu_t,\qquad q\ge2,
\]
and
\[
 v_{q,k}=\eta_k a^{(q-1)/2}F^{q/2}.
\]
The powers are exact:
\[
 v_{q,k}^4=\eta_k^4a^{2q-2}F^{2q},\qquad
 Fv_{q,k}^2=\eta_k^2a^{q-1}F^{q+1}.
\]
Thus the fourth-power Sobolev output is the next weighted spatial moment \(H_{2q}\), after replacing \(\eta_k^4\) by an inner cutoff \(\eta_{k+1}^2\). At \(q=2\), the reaction is \(H_3=\int\eta^2aF^3\); at \(q=3\), the Sobolev variable is \(\eta aF^{3/2}\), precisely Wang's next fixed moment.

The full velocity must be retained as \(-2aE\). The curvature variation has structure
\[
 \partial_t\operatorname{Rm}
 =a\Delta\operatorname{Rm}+a(\operatorname{Rm}*\operatorname{Rm}+\operatorname{Rm})
 +da*\nabla E+(\nabla^2a)*E+aE*\operatorname{Rm}.
\]
Since
\[
 E=\operatorname{contr}(\operatorname{Rm})+g,
 \qquad \nabla E=\operatorname{contr}(\nabla\operatorname{Rm}),
\]
we have \(|E|\le CF\) and \(|\nabla E|\le C|\nabla\operatorname{Rm}|\) at every smooth time. Consequently, after integrating the Hessian-\(a\) term once by parts, the curvature power estimate closes with the curvature dissipation itself; no separate high-power defect-gradient energy is needed for this zero-order curvature layer.

For every fixed \(q\), tensor testing gives the local inequality
\[
\begin{aligned}
 \frac d{dt}H_{q,k}+c_q\int|\nabla v_{q,k}|^2
 \le Cq^2\bigg[&\int a^{q-1}|d\eta_k|^2F^q\\
 &+\int\eta_k^2\frac{|da|^2}{a}a^{q-2}F^q\\
 &+\int\eta_k^2a^{q-1}F^{q+1}\bigg],
\end{aligned}
\tag{2.1}
\]
up to finite-neighbor enlargement. The key regular identity is
\[
 \frac{|da|^2}{a}=4|d\chi|^2.
\]
The evolving measure \(\partial_td\mu=-\operatorname{tr}(aE)d\mu\) and inverse-metric variation enter the final reaction in (2.1), not an independent source.

Let
\[
 \gamma=A^2\|F\|_{L^2(\widetilde U)}.
\]
At \(q=2\), Sobolev gives
\[
 H_3\le C\gamma\left(\int|\nabla v_2|^2+r^{-2}H_2\right).
\]
For sufficiently small \(\gamma\), this reaction is absorbed and
\[
 \int_0^tH_3(s)\,ds\le C\gamma H_2(0).
\tag{2.2}
\]
At \(q=3\), the same fixed-exponent absorption yields \(H_3'\le Cr^{-2}H_3\). Averaging backward with (2.2) gives
\[
 H_3(t)\le \frac{C\gamma H_2(0)}t,
 \qquad
 \boxed{A^4H_3(t)\le \frac{C\gamma^3}{t}}.
\tag{2.3}
\]
This is the transition-compatible curvature potential sought in Steps 18–19. It is obtained without dividing by \(a\), and without first assuming a pointwise curvature bound.

Because \(F\) includes the constant 1, generally
\[
 \gamma\le\beta+Cr^2,
 \qquad \beta=A^2\|\operatorname{Rm}\|_2.
\]
In the original initial near-negative-Einstein metric, \(|E|\le\delta\ll1\) forces \(|\operatorname{Ric}|\ge c>0\), so \(F\le C|\operatorname{Rm}|\) at the initial slice and \(\gamma\lesssim\beta\). More robustly, use \(\gamma\) as the actual parameter. The four-dimensional relative-Sobolev scaling gives
\[
 \gamma\lesssim r^2\sqrt{1+K_0},
\]
independent of collapsed volume.

## 3. Defect hierarchy and the transfer missing in Step 19

The previously propagated moment
\[
 I_p=\int|aE|^p=\int a^p|E|^p
\]
is too weak near \(a=0\) for the same Wang hierarchy. Replace it by
\[
 J_{m,k}=\int\eta_k^2a^{m-2}|E|^m,
 \qquad
 z_{m,k}=\eta_k a^{(m-1)/2}|E|^{m/2}.
\]
For \(0\le a\le1\), \(J_p\ge I_p\), with two fewer powers of \(a\). Initial pointwise pinching still supplies
\[
 J_p(0)\le\delta^p\operatorname{Vol}(\widetilde U).
\]
Tensor testing before scalarization and integrating Hessian-\(a\) terms by parts gives, for fixed \(m\),
\[
\begin{aligned}
 \frac d{dt}J_{m,k}+c_m\int|\nabla z_{m,k}|^2
 \le Cm^2\bigg[&\int a^{m-1}|d\eta_k|^2|E|^m\\
 &+\int\eta_k^2\frac{|da|^2}{a}a^{m-2}|E|^m\\
 &+\int\eta_k^2a^{m-1}F|E|^m\bigg].
\end{aligned}
\tag{3.1}
\]
Thus one prescribed base exponent, in particular \(m=6\), propagates by the same small critical parameter. This resolves the compatibility issue raised by the Strategist: the stronger starting moment is available directly from initial pointwise smallness and is stable under the weighted tensor calculation; it does not have to be recovered from \(I_6\).

The weighted cubic potential closes the high-exponent reaction exactly. Algebraically,
\[
 Fz_m^2=(aF^3)^{1/3}(a^{-1/3}z_m^2),
\]
and the second factor raised to \(3/2\) has density
\[
 a^{3m/2-2}|E|^{3m/2}=J_{3m/2}.
\]
Moreover,
\[
 J_{3m/2}\le J_m^{1/2}J_{2m}^{1/2},
\]
while Sobolev controls \(J_{2m}^{1/2}\) by
\[
 CA^2\left(\int|\nabla z_m|^2+r^{-2}J_m\right).
\]
Therefore
\[
 \int\eta^2a^{m-1}F|E|^m
 \le\varepsilon X_m+C\varepsilon^{-2}A^4H_3J_m.
\tag{3.2}
\]
On a positive-time cylinder \([t/2,t]\), (2.3) turns the coefficient into \(C_m\gamma^3/t\). A nested parabolic iteration with \(m\mapsto3m/2\), starting from propagated \(J_6\), is compatible with
\[
 \boxed{|aE(x,t)|\le C\delta\left(1+\frac{r^2}{t}\right)^{1/3}}.
\tag{3.3}
\]
The volume factors cancel because \(A\lesssim rV^{-1/4}\) and \(J_6(0)^{1/6}\le\delta V^{1/6}\). In the limit \(m\to\infty\), \((a^{m-2}|E|^m)^{1/m}\to a|E|\), so this hierarchy outputs the correct flow velocity. Equation (3.3) is still conditional on writing the nested finite-neighbor recurrence with the evolving geometry; the exponent and norm transfer themselves now match exactly.

## 4. Unweighted defect energy is triangular

Global calibration later needs
\[
 Q(t)=\int_M|E|^2.
\]
A bound with an additive \(\varepsilon\int a|\nabla\operatorname{Rm}|^2\) is inadequate: the integrated curvature dissipation can be order \(A\), creating an order \(\varepsilon A\) term at a fixed smoothing scale.

The exact defect equation is homogeneous in \(E\). Testing locally by \(\eta^2E\), integrating the Hessian cutoff term by parts, and absorbing the curvature potential by critical Sobolev gives
\[
 \frac d{dt}Q_\alpha
 \le Cr^{-2}\sum_{\beta\sim\alpha}Q_\beta,
\tag{4.1}
\]
provided the full-support neighboring curvature parameter is small. Summing unnormalized local energies over bounded overlap yields
\[
 Q_{\mathrm{support}}(T)\le e^{CT/r^2}Q_{\mathrm{support}}(0).
\tag{4.2}
\]
Outside the support, the metric is stationary. Thus (4.2) preserves \(Q(T)/A\to0\) from \(Q(0)/A\to0\). This replaces the overstrong Step 19 assertion that the integrated cancellation alone sufficed.

## 5. Whitney balls: useful local interpretation, not a completed reduction

At a point with \(\chi(y)=\chi_0>0\), set
\[
 a_0=\chi_0^2,\qquad \ell=cr\chi_0.
\]
On \(B_\ell(y)\),
\[
 a/a_0\in[(1-Lc)^2,(1+Lc)^2],
\]
and after effective-time rescaling \(\tau=a_0t\),
\[
 \tau/\ell^2=t/(c^2r^2).
\]
Hence one physical interval \(t\le\theta r^2\), \(\theta<c^2\), is compatible with all cutoff levels, including arbitrarily small positive times. This part of A01's proposal is sound.

Two corrections are essential:

1. \(|a-a_0|/a_0=O(c)\), not \(O(c^2)\).
2. A single energy bound on a large disconnected support union does not imply local Whitney-ball smallness. One needs a centered local budget such as
   \[
   \int_{B_{10r}(y)}F^2\le K_0\operatorname{Vol}(B_{10r}(y)),
   \]
   or a per-component/finite-neighbor equivalent. Bishop–Gromov then yields
   \[
   \ell^4\fint_{B_\ell(y)}F^2\le CK_0r^4
   \]
   uniformly in \(\chi_0\). Bounded overlap controls sums of unnormalized integrals, not sums of normalized averages.

The direct \(H_q,J_m\) hierarchy and Whitney balls encode the same cutoff scaling. The direct hierarchy is currently the cleaner zero-order route; Whitney balls remain promising for the derivative estimate because they make the operator uniformly parabolic after rescaling.

## 6. Remaining derivative obstruction

The zero-order hierarchy gives a Caccioppoli control of \(\chi\nabla(aE)\), but not the pointwise bound
\[
 |\chi\nabla(aE)|\le C\delta t^{-1/2}(r^2/t)^{1/3}.
\tag{6.1}
\]
Differentiating the \(U=aE\) equation produces the term
\[
 \chi a\,\nabla\operatorname{Rm}*U.
\]
Neither (2.3) nor a zero-order \(|a\operatorname{Rm}|\lesssim t^{-1}\) bound controls it. A weighted curvature-derivative estimate on Whitney cylinders, or a coupled derivative energy argument, is still required. If (6.1) is established, its time integral is finite because the base exponent is \(p=6>4\), giving the Step 19 connection and cutoff-Hessian drift bounds.

## 7. What changed

The analytic bridge is sharper than at Step 19:

- The transition-compatible cubic curvature potential follows from the fixed \(q=2,3\) Wang hierarchy rather than from an unweighted Li hypothesis.
- The stronger defect moments \(J_m\), not \(I_m=\int|aE|^m\), are the norms that feed the high-exponent iteration; initial pinching and tensor cancellation make \(J_6\) available.
- The curvature power layer closes through \(\nabla E=\operatorname{contr}(\nabla\operatorname{Rm})\).
- Global unweighted defect preservation must be triangular, with no additive curvature-only dissipation.
- The unresolved first-exit quantity is now concentrated in the weighted derivative/Bernstein estimate and the full finite-neighbor implementation of the zero-order recurrences.

Evidence:

- `workspace/scripts/verify_step20_weighted_moment_hierarchy.py`
- `trace/ttcs/results/step20_ttcs01_generator1_integration.md`
- `trace/ttcs/results/step20_ttcs01_verifier1_integration.md`
- A01 `workspace/notes/step20_closed_tensor_estimate.md`
- Wang source, especially the fixed \(q=2,3\) calculations in lines 672–703.

## 8. Whitney derivative weight audit

A direct scale calculation gives useful information about the remaining term. On a Whitney ball with \(a_0=\chi_0^2\), radius \(\ell=cr\chi_0\), and effective time \(\tau=a_0t\), standard positive-time parabolic scaling predicts
\[
 |\nabla\operatorname{Rm}|\lesssim \tau^{-3/2},
 \qquad a_0^{3/2}|\nabla\operatorname{Rm}|\lesssim t^{-3/2}.
\]
The ordinary interior gradient estimate for \(U\) gives
\[
 \chi_0|\nabla U|\lesssim
 \chi_0(a_0t)^{-1/2}\sup|U|
 =t^{-1/2}\sup|U|,
\]
with no negative power of \(\chi_0\). Moreover,
\[
 \chi_0a_0|\nabla\operatorname{Rm}|\,|U|
 \sim t^{-3/2}|U|
 \sim \frac1t\,|\chi_0\nabla U|.
\]
Thus the dangerous differentiated-curvature term is scale-critical but not cutoff-singular. This is encouraging for a Whitney-cylinder Bernstein argument: the cutoff level cancels exactly. It also shows why a bare Gronwall treatment is insufficient—the resulting \(1/t\) coefficient is nonintegrable from zero. One must work on \([t/2,t]\) and use a coupled positive-time estimate, or exploit a Bernstein combination in which this term is absorbed rather than integrated from the initial slice. The weight calculation is verified by `workspace/scripts/verify_step20_whitney_bernstein_weights.py`.

## 9. Derivative-free first-exit refinement

A further review changes the role of the Step 19 Bernstein target. For the zero-order first-exit, quantitative pointwise control of \(\chi\nabla(aE)\), the connection, or \(\nabla^2a\) need not be assumed at all:

- every Hessian-\(a\) term in the weak \(H_q\), \(J_m\), and triangular \(Q\) estimates is integrated by parts;
- fixed scalar cutoffs satisfy \(|d\chi|_{g(t)}\) and \(|d\eta|_{g(t)}\) bounds from metric equivalence alone, since these are covector norms and use no connection;
- relative Sobolev constants on fixed domains, volume comparison between fixed domains, and buffered containment transfer under bilipschitz metric equivalence;
- the integrable pointwise velocity (3.3) directly improves metric equivalence.

Thus the provisional first-exit quantities can be limited to metric equivalence, fixed-domain relative Sobolev constants, full-neighbor-star critical \(F\)-energy, fixed cutoff-gradient norms, buffered domain containment, weighted pointwise curvature/velocity, and triangular unweighted defect energy. The derivative term in Section 6 obstructs a quantitative Bernstein theorem, but not this weaker zero-order closure.

Two mathematical tasks replace the former derivative target:

1. complete the nested positive-time recurrence from (2.3) to \(|a\operatorname{Rm}|\lesssim\gamma/t\), and from propagated \(J_6\) to (3.3), including time cutoffs, finite-neighbor leakage, and summable exponent dependence;
2. adapt Wang's qualitative smooth-extension proof from \(\partial_tg=-2a\operatorname{Ric}\) to \(\partial_tg=-2a(\operatorname{Ric}+g)\). A terminal \(|a\operatorname{Rm}|\) bound is expected to generate cutoff and weighted-curvature derivatives internally through Wang's triangular \(L^p\) induction; the normalized term is lower order, but this adaptation is not a direct consequence of Wang's stated theorem and must be written.

The formal curvature high-exponent reaction has the same cubic factorization as the defect:
\[
 \int\eta^2a^{q-1}F^{q+1}
 \le \varepsilon X_q+C\bigl(r^{-2}+\varepsilon^{-2}A^4H_3\bigr)H_q.
\]
On \([t/2,t]\), (2.3) makes this a \(C_q(r^{-2}+\gamma^3/t)\) potential. The expected \(q\mapsto3q/2\) recurrence has endpoint \(aF\), since \((a^{q-2}F^q)^{1/q}\to aF\), and the scale is \(C\gamma/t\). This is a well-posed remaining derivation, not yet a proved pointwise estimate.

Independent support: `trace/ttcs/results/step20_ttcs02_generator1_integration.md` and `step20_ttcs02_verifier1_integration.md`.

## 10. Infinite-product and endpoint scaling check

For the abstract positive-time recurrence with \(q_{j+1}=3q_j/2\), the sums are
\[
 \sum_{j\ge0}\frac1{q_j}=\frac3{q_0}.
\]
If one step contributes \((CA^2)^{2/(3q_j)}\Lambda_j^{1/q_j}\), then the accumulated Sobolev and parabolic exponents are
\[
 A^{4/q_0},\qquad \Lambda^{3/q_0}.
\]
Polynomial factors in \(q_j\) and nested-cutoff factors \(4^j\) have convergent products because \(\sum j/q_j<\infty\).

For curvature with \(q_0=2\), the endpoint factor is
\[
 A^2t^{-3/2}(tH_2)^{1/2}.
\]
Using \(H_2\le\gamma^2/A^4\) gives exactly \(\gamma/t\). For the defect with \(q_0=6\), the endpoint factor is
\[
 A^{2/3}t^{-1/2}(tJ_6)^{1/6}.
\]
Using \(J_6\le\delta^6V\) and \(A\lesssim rV^{-1/4}\) gives exactly
\[
 \delta(r^2/t)^{1/3}.
\]
This verifies that the proposed recurrence, once its time-space energy step is written rigorously, has the correct outputs and finite exponent product. It does not by itself supply that energy recurrence. See `workspace/scripts/verify_step20_moser_recurrence_products.py`.

## 11. Abstract parabolic recurrence (proved from the weak moment inequality)

The infinite-exponent passage can be separated cleanly from the geometric derivation. Let \(f=aF\) (curvature) or \(f=a|E|\) (defect), and write
\[
 M_q(Q)=\iint_Q a^{-2}f^q=\iint_Q a^{q-2}\Phi^q,
\]
where \(\Phi=F\) or \(|E|\). Interpret the density directly as \(a^{q-2}\Phi^q\), so no division by \(a\) is performed at its zero set.

Let \(Q_{j+1}\Subset Q_j\) be nested space-time cylinders ending at a fixed time \(t>0\), and set \(q_{j+1}=3q_j/2\). Suppose the weak tensor estimate and the weighted cubic-potential bound imply, for every \(j\),
\[
 \sup_{s\in I_{j+1}}H_{q_j,j+1}(s)
 +\int_{I_{j+1}}D_{q_j,j+1}(s)\,ds
 \le Cq_j^\sigma4^j(t^{-1}+r^{-2})
 M_{q_j}(Q_j).
\tag{11.1}
\]
Here the \(q_j^\sigma\) factor includes the Young loss from
\[
 A^4H_3(s)\le C\gamma^3/t,\qquad s\in[t/2,t],
\]
and \(D_q\) is the squared gradient norm of the corresponding Sobolev variable. Spatial Sobolev and
\[
 H_{3q/2}\le H_q^{1/2}H_{2q}^{1/2}
\]
then give
\[
 M_{3q_j/2}(Q_{j+1})
 \le CA^2\left[Cq_j^\sigma4^j(t^{-1}+r^{-2})
 M_{q_j}(Q_j)\right]^{3/2}.
\tag{11.2}
\]
Taking the \(2/(3q_j)\) power yields the explicit recurrence
\[
 \boxed{
 M_{q_{j+1}}(Q_{j+1})^{1/q_{j+1}}
 \le (CA^2)^{2/(3q_j)}
 \left[Cq_j^\sigma4^j(t^{-1}+r^{-2})\right]^{1/q_j}
 M_{q_j}(Q_j)^{1/q_j}.}
\tag{11.3}
\]
Because
\[
 \sum_{j\ge0}\frac1{q_j}=\frac3{q_0},
 \qquad
 \sum_{j\ge0}\frac{j+\log q_j}{q_j}<\infty,
\]
all polynomial-in-\(q_j\), \(4^j\), and fixed localization factors have convergent products. Hence
\[
 \|f\|_{L^\infty(Q_\infty)}
 \le C A^{4/q_0}(t^{-1}+r^{-2})^{3/q_0}
 M_{q_0}(Q_0)^{1/q_0}.
\tag{11.4}
\]
For \(t\le r^2\), the two relevant substitutions are:

- curvature, \(q_0=2\): \(M_2(Q_0)\le tH_2\le t\gamma^2/A^4\), so
  \[
  \|aF(t)\|_\infty\le C\gamma/t;
  \]
- defect, \(q_0=6\): \(M_6(Q_0)\le t\delta^6V\) and \(A\lesssim rV^{-1/4}\), so
  \[
  \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}.
  \]

Thus the high-exponent product itself is now resolved: no deteriorating critical-energy threshold is used after the fixed \(q=2,3\) construction of \(H_3\). What remains is to derive (11.1) with all nested time cutoffs and fixed outer-neighborhood terms from the exact evolving tensor equations, uniformly across the chosen local family. The exponent sums and endpoint scalings are checked in `workspace/scripts/verify_step20_moser_recurrence_products.py`.

## 12. Source update on normalization

The focused retrieval did not locate a published theorem stated exactly for the spatially cutoff normalized flow \(-2\chi^2(\operatorname{Ric}+g)\). It did recover Fei He's 2016 local-flow work, whose introduction explicitly states that parallel results hold for the normalized Ricci flow
\[
 \partial_tg=-2(\operatorname{Ric}-\lambda g),\qquad \lambda=\text{constant},
\]
with smallness imposed on \(\operatorname{Ric}-\lambda g\). This is supporting structural precedent for using \(E=\operatorname{Ric}+g\), not a direct smooth-extension theorem for a spatial cutoff. Wang's Theorem 4.1 and Lemmas 4.4–4.14 remain the exact extension template. Accordingly, the normalized cutoff adaptation remains a proof task rather than a citation. Source: `staging/acquired/Existence__Lifespan_and_Transfer_Rate_of_Ricci_Flows_on_Manifold_4f0e84ed47779027/part_001.md`, lines 95–97; Wang source lines 394–661.
