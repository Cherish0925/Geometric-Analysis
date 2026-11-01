# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step7_orbit_volume_negative_einstein_collapse.tex",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step6_collapsed_unwrapping_route.md"
  ]
}
```

## Task

Verify the orbit-volume obstruction argument for negative Einstein regular collapse:

1. Check that Lott's equation (2.9) Δv = (|F|²/4 - λN)v correctly specializes to Δv = (|F|²/4 + N)v for λ = -1, and that this makes v strictly subharmonic.

2. Verify the parabolicity argument: complement of finitely many points in a compact space of dim ≥ 2 is parabolic (Grigoryan), bounded-above subharmonic → constant → contradiction with positive RHS.

3. Check the circle base case: ∫v'' = 0 vs ∫Nv > 0.

4. Verify the near-Einstein error term: for Ric = -g + E with ||E||∞ ≤ δ, the coefficient becomes N(1-δ) > 0 for δ < 1.

5. Check the capacity estimate: from Δv ≥ cv with test function η²/v, one gets c∫η² ≤ ∫|∇η|².

6. Verify that the conclusion is correctly scoped: excludes free abelian collapse only (not nil³), and only on parabolic bases with bounded orbit volume. Identify any gaps or additional hypotheses needed.

7. Check whether the Cheeger-Tian framework legitimately applies to near-Einstein (not exactly Einstein) 4-manifolds to produce a groupoid limit with Ric = -g.

## Output

# Verification memo: orbit-volume argument for the \(\lambda=-1\) branch

## Overall assessment

The exact orbit-volume equation and its sign specialization are correct. They give a valid qualitative obstruction on a connected parabolic regular base when the orbit-volume function is globally bounded above. The closed-circle argument is also correct.

Three major derivational issues remain:

1. finite total space volume does **not** imply a pointwise upper bound for the orbit-volume function;
2. the proposed capacity estimate has the wrong sign and is false;
3. the cited Cheeger–Tian decomposition does not automatically extend from Einstein metrics to metrics satisfying only \(\|\operatorname{Ric}+g\|_{L^\infty}\to0\).

Thus the local PDE obstruction is sound under its stated analytic hypotheses, but the application to the whole regular part of the collapsed sequence requires more geometric input.

---

## 1. Lott equation and specialization to \(\lambda=-1\)

For an adapted metric with a free isometric \(\mathbb R^N\)-action, the orbit-volume identity can be written as

\[
\frac{\Delta_B v}{v}
=
\frac14|F|^2-\operatorname{tr}_{V}\operatorname{Ric}_{\bar g},
\qquad
v=\sqrt{\det G}.
\]

When \(\operatorname{Ric}_{\bar g}=\lambda\bar g\),

\[
\operatorname{tr}_{V}\operatorname{Ric}_{\bar g}=\lambda N,
\]

and hence

\[
\Delta_Bv
=
\left(\frac14|F|^2-\lambda N\right)v.
\]

At \(\lambda=-1\),

\[
\boxed{\Delta_Bv
=
\left(\frac14|F|^2+N\right)v.}
\]

Since \(G\) is positive definite, \(v>0\); since \(|F|^2\ge0\) and \(N\ge1\),

\[
\Delta_Bv\ge Nv>0.
\]

Therefore \(v\) is strictly subharmonic on every regular free-abelian stratum. The sign calculation is correct.

The equation is local and only uses the regular locus where the action is free and the adapted decomposition is defined. It does not directly cross rank-drop or singular-fiber points.

---

## 2. Parabolicity and the bounded-above argument

### Abstract parabolic argument

On a connected parabolic Riemannian manifold, the standard Liouville property says that every bounded-above subharmonic function is constant. Consequently, if

\[
v>0,\qquad \sup_Bv<\infty,\qquad \Delta v\ge cv,\quad c>0,
\]

then parabolicity makes \(v\) constant, while the differential inequality gives

\[
0=\Delta v\ge cv>0,
\]

which is impossible.

Thus the proposition in Section 2 is mathematically correct when:

- \(B\) is parabolic in the potential-theoretic sense relevant to the Liouville theorem;
- \(v\) has a global upper bound;
- the free abelian structure and the orbit-volume equation hold throughout \(B\).

The same reasoning works for orbifolds by passing to local finite covers.

### Compact smooth orbifold with finitely many points removed

If \(K^m\) is a compact smooth Riemannian orbifold, \(m\ge2\), and

\[
B=K\setminus\{p_1,\dots,p_q\},
\]

then each removed point has zero \(W^{1,2}\)-capacity. Explicitly:

- for \(m>2\), an annular cutoff around a point has energy \(O(\varepsilon^{m-2})\);
- for \(m=2\), a logarithmic cutoff has energy \(O(1/\log(1/\varepsilon))\).

Both tend to zero. This gives the usual parabolic Dirichlet form on the punctured compact orbifold and supports the bounded-above Liouville argument.

However, the phrase “a compact space of dimension at least two with finitely many points removed” is too broad. Topological dimension and compact metric completion alone do not imply parabolicity. For example, a warped end

\[
dr^2+r^{2\alpha}g_{S^{m-1}}
\]

can complete by adding one point, while the capacity of that point depends on

\[
\int_0 \frac{dr}{r^{\alpha(m-1)}}.
\]

Extra local orbifold, conical, or comparable metric control near the added points is needed.

The precise Grigoryan theorem and corollary numbering cannot be confirmed from the supplied files because the source passage itself was not included.

### Finite total volume does not imply bounded \(v\)

The application states that \(v\) is bounded because the four-dimensional volume is finite. This inference is incorrect. Volume pushdown only gives an integral such as

\[
\int_B v\,d\mu_B<\infty
\]

(up to lattice factors), not \(\sup_Bv<\infty\).

There is a direct PDE model showing that integrability cannot replace boundedness. On a compact manifold \(K\), let \(q_c\) be the positive Green kernel of \(c-\Delta\):

\[
(c-\Delta)q_c=\delta_p.
\]

On \(K\setminus\{p\}\),

\[
\Delta q_c=cq_c,
\]

while \(q_c\) is unbounded near \(p\) but integrable, with

\[
c\int_Kq_c\,d\mu=1.
\]

Thus a positive integrable function can satisfy exactly the same strict subharmonic equation by concentrating at a puncture. Geometrically, this is the analytic behavior that singular fibers or curvature concentration could support.

Accordingly, the application requires an independent pointwise upper bound for \(v\), or a geometric extension theorem forcing \(v\) to remain bounded near the deleted points.

---

## 3. Closed circle base

On a closed one-dimensional base, use arclength \(s\). Since a two-form on a one-dimensional base vanishes, \(F=0\), and the exact equation is

\[
v''=Nv.
\]

Periodicity gives

\[
\int_0^L v''\,ds=v'(L)-v'(0)=0,
\]

whereas

\[
N\int_0^L v\,ds>0.
\]

Hence no positive periodic solution exists. The same argument works for the near-Einstein inequality

\[
v''\ge N(1-\delta)v,\qquad \delta<1.
\]

For a one-dimensional interval, the conclusion depends on endpoint behavior. If \(v\to0\) at both finite endpoints, convexity indeed contradicts \(v>0\). If \(v\) does not tend to zero, the statement that the endpoint is not a genuine concentration point requires separate geometric analysis.

---

## 4. Near-Einstein term

For an exactly adapted metric with a free isometric abelian action, write

\[
\operatorname{Ric}_{\bar g}=-\bar g+E.
\]

The general vertical-trace identity gives

\[
\Delta_Bv
=
\left(\frac14|F|^2-\operatorname{tr}_{V}\operatorname{Ric}_{\bar g}\right)v
=
\left(\frac14|F|^2+N-\operatorname{tr}_{V}E\right)v.
\]

If

\[
\|g^{-1}E\|_{\mathrm{op}}\le\delta,
\]

then

\[
|\operatorname{tr}_{V}E|\le N\delta,
\]

so

\[
\boxed{
\Delta_Bv
\ge
\left(\frac14|F|^2+N(1-\delta)\right)v
\ge N(1-\delta)v.}
\]

This is correct for \(\delta<1\).

The exact symmetry assumption is essential. A Cheeger–Fukaya–Gromov invariant approximation to \(g_i\) does not automatically satisfy this estimate: Ricci curvature involves second derivatives, so small metric difference in a weak topology does not control the corresponding error in the orbit-volume equation. The inequality is valid either for the original metric with an exact local isometric action, or for a sufficiently regular limit groupoid after the Einstein equation has been passed to the limit.

---

## 5. The capacity estimate has the wrong sign

Let \(\eta\) be compactly supported and put

\[
\psi=\frac{\eta^2}{v}.
\]

Using the stated convention \(\Delta=\operatorname{tr}\nabla^2\),

\[
\begin{aligned}
\int \psi\,\Delta v
&=
-\int\left\langle \nabla\!\left(\frac{\eta^2}{v}\right),\nabla v\right\rangle\\
&=
\int \eta^2|\nabla\log v|^2
-2\int \eta\langle\nabla\eta,\nabla\log v\rangle\\
&=
\int|\eta\nabla\log v-\nabla\eta|^2
-\int|\nabla\eta|^2.
\end{aligned}
\]

From \(\Delta v\ge cv\), one gets

\[
c\int\eta^2
\le
\int|\eta\nabla\log v-\nabla\eta|^2
-\int|\nabla\eta|^2.
\]

The right side has no upper estimate by \(\int|\nabla\eta|^2\). Completing the square gives a lower estimate instead.

A concrete counterexample is

\[
v(x)=e^{\sqrt c\,x}\quad\text{on }\mathbb R,
\qquad v''=cv.
\]

Choose \(\eta_R=1\) on \([-R,R]\), supported in \([-R-1,R+1]\), with uniformly bounded transition derivatives. Then

\[
c\int\eta_R^2\asymp R,
\qquad
\int|\eta_R'|^2=O(1),
\]

contradicting the proposed estimate.

The estimate

\[
c\int\eta^2\le\int|\nabla\eta|^2
\]

would follow from the opposite differential sign,

\[
\Delta v\le-cv.
\]

Therefore the quantitative capacity discussion, the asserted transition cost, and the ensuing volume estimate are not supported by the displayed computation. Even independently, a pointwise estimate \(|\nabla\eta|\le L\) gives

\[
\int|\nabla\eta|^2
\le
L^2\operatorname{Vol}(\operatorname{supp}\nabla\eta),
\]

not merely \(L^2\).

The qualitative parabolic Liouville proof remains valid when \(v\) is bounded above.

---

## 6. Precise domain of validity

The verified result is:

> Let \(B\) be connected and parabolic, and suppose an adapted metric with an exact free isometric \(\mathbb R^N\)-action satisfies either \(\operatorname{Ric}=-g\), or \(\operatorname{Ric}=-g+E\) with \(\|g^{-1}E\|_{\mathrm{op}}<1\). If \(v=\sqrt{\det G}\) is globally bounded above, then such a regular abelian structure cannot exist.

A closed circle base needs no upper bound because direct integration suffices.

This result does not address:

- \(\mathrm{nil}^3\) or other nonabelian fibers;
- rank drop and singular fibers;
- interval bases without established endpoint asymptotics;
- regular bases with hyperbolic potential theory;
- point-deleted bases where \(v\) can diverge;
- approximately invariant metrics without second-derivative control.

In addition, because the Step 6 sequence has diameter tending to infinity, a pointed groupoid limit need not have compact metric completion. Its base therefore need not be a compact orbifold with finitely many points removed. Parabolicity of each resulting regular component must be established geometrically rather than inferred from the compactness of the original manifolds.

---

## 7. Cheeger–Tian and near-Einstein sequences

The Cheeger–Tian 2006 curvature theory cited in the note is built for Einstein four-manifolds. The exact Einstein equation supplies an elliptic curvature equation schematically of the form

\[
\nabla^*\nabla\operatorname{Rm}
=
\operatorname{Rm}*\operatorname{Rm}
+\lambda\operatorname{Rm}.
\]

For

\[
\operatorname{Ric}_{g_i}=-g_i+E_i,
\qquad
\|E_i\|_{L^\infty}\to0,
\]

the corresponding curvature equation contains

\[
\nabla^2E_i,
\]

which is not controlled by an \(L^\infty\) estimate on \(E_i\). Chern–Gauss–Bonnet, fixed topology, bounded Ricci, and bounded volume do provide an \(L^2\) curvature budget, but they do not by themselves provide:

- pointwise curvature estimates away from finitely many balls;
- uniform curvature radius on the regular part;
- the bounded-sectional-curvature hypotheses used in classical collapsed groupoid compactness.

Thus the stated Cheeger–Tian decomposition for the \(g_i\) is not presently justified from \(\|\operatorname{Ric}+g\|_{L^\infty}\to0\) alone.

If local covers with uniform harmonic radius and strong \(W^{2,p}\) compactness are independently available, then passing to

\[
\operatorname{Ric}_{g_\infty}=-g_\infty
\]

is legitimate through the harmonic-coordinate Ricci equation, followed by elliptic regularity. The unresolved part is producing those regular cover charts and the groupoid convergence from the given near-Einstein assumptions. Sufficient replacements would include scale-compatible derivative estimates for \(E_i\), an almost-Einstein epsilon-regularity theorem, or separately established curvature-radius control on the regular regions.

In summary, the exact local orbit-volume obstruction is correct; its global use in the critical collapsed sequence still depends on an upper bound for \(v\), verified parabolic geometry of the base, and a regular-collapse compactness theorem applicable to the near-Einstein metrics.