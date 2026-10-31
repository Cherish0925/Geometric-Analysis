# Step 27: Normalized cutoff-flow continuation theorem


**Step 32 superseding note.**  The positive-time endpoints displayed below
\(\|a\operatorname{Rm}\|_\infty\lesssim\beta/t\) and
\(\|aE\|_\infty\lesssim\delta(r^2/t)^{1/3}\) are again the active conditional
forms, but only via the corrected nested spacetime recurrence in
`workspace/notes/step32_nested_moser_and_tensor_audit.md`.  They are not proved
by the older theorem text below, and the continuation part remains incomplete
until the shifted-\(U\) derivative induction or a direct degenerate-flow extension
is written term by term.
Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose

**Step 28 correction.**  This note should be read through the A03 shifted-curvature
artifact and the Step 28 TTCS verification.  The generic-lower-order treatment
below is superseded by the `U=a(Rm+G)` induction; the transfer is strong at the
schematic/Wang-mechanism level but still needs a fully expanded Wang
Proposition 4.14 grouping, staggered Hölder exponents, and Yang degenerate
restart details before being treated as an independently written proof.

This note formulates the last open analytic obstacle in the four-dimensional
negative-branch conditional gap chain.  Both A01 (Step 27) and A03 (Step 26)
independently derived the three weighted estimates:

\[
  \|a\operatorname{Rm}(t)\|_\infty\le C\beta/t,\qquad
  \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3},\qquad
  Q(t)\le e^{C\theta}Q(0),
\]

conditional on smooth existence and the first-exit conditions.  The single
remaining piece is to prove that the normalized cutoff flow

\[
  \partial_tg=-2\chi^2(\operatorname{Ric}_g+g)=-2a(\operatorname{Ric}_g+g),
  \qquad a=\chi^2,
\tag{0.1}
\]

on a closed smooth four-manifold has a smooth solution lasting to the required
time \(\theta r^2\) under the energy bootstrap.

The argument adapts Yang (Section 8, Theorem 8.2) for short-time existence
and Wang (Theorem 4.1) for extension, both from the retrieved sources.

## 1. Short-time existence

**Theorem 1.1 (Short-time existence).** *Let \((M^4,g_0)\) be a closed smooth
Riemannian manifold and \(\chi\in C_0^\infty(M)\).  Then equation (0.1) has a
unique smooth solution \(g(t)\) for \(t\in[0,T_0)\) with \(T_0>0\).*

**Proof (following Yang Section 8, Approach 1 — direct degenerate construction).**

The equation (0.1) has the form \(\partial_tg=-2\chi^2\operatorname{Ric}_g+L(g)\)
where \(L(g)=-2\chi^2 g\) is a smooth zero-order mapping of \(g\).  Yang's
Approach 1 (lines 792--818) constructs a solution to the degenerate cutoff Ricci
flow by solving a coupled system for \((\hat g,\varphi_t)\) in DeTurck gauge:

\[
  \partial_t\hat g=-2(\chi\circ\varphi_t^{-1})^2\operatorname{Ric}(\hat g)
  -2(\chi\circ\varphi_t^{-1})^2\hat g
  +\text{DeTurck correction},
  \qquad \hat g(0)=g_0,
\tag{1.1}
\]
\[
  \partial_t\varphi_t=-\chi^2(\varphi_t)_*[\text{gauge vector}],
  \qquad\varphi_0=\operatorname{Id}.
\tag{1.2}
\]

The normalization term \(-2(\chi\circ\varphi^{-1})^2\hat g\) is algebraic (no
second derivatives of \(\hat g\)).  The linearized system gains the additional
term \(-2\chi^2h\), which is a tame zero-order operator in the Sobolev scale.
Yang's proof uses either a Banach fixed-point argument in
\(C^0([0,T],H^k(M))\) or Nash--Moser tame estimates; both extend to include a
tame zero-order perturbation without structural changes.

The energy estimate for the normalization-generated source gives
\[
  \frac{d}{dt}\mathcal E
  \le C\mathcal E+C_0\operatorname{Vol}(M),
\]
where the \(O(\operatorname{Vol})\) term is absorbed by Gronwall for short time.
This yields a common existence interval \([0,T_0)\) independent of any
regularization parameter.  Pulling back gives
\(g=\varphi_t^*\hat g\) satisfying (0.1).

**Step 27 correction (TTCS):** The earlier \(\varepsilon\)-regularization argument
is withdrawn because uniform-in-\(\varepsilon\) \(L^{n/2}\) curvature bounds do
not imply uniform \(C^k\) bounds (the elliptic constants degenerate as
\(\varepsilon\to0\)).  Yang's direct degenerate construction avoids this.
\(\square\)

**Remark 1.2.** Approach 1 in Yang Section 8 also works: the linearized
equation for (0.1) gains an additional lower-order term
\(-2\chi^2 h\) (where \(h\) is the metric perturbation), which does not change
the parabolic structure or the Nash--Moser tame estimates.

## 2. Extension under weighted curvature control

**Theorem 2.1 (Extension).** *Let \(g(t)\), \(t\in[0,T)\), be a smooth solution
of (0.1) on a closed manifold.  If*
\[
  \sup_{[0,T)}|\chi^2\operatorname{Rm}|_{g(t)}\le K<\infty,
\tag{2.1}
\]
*then the solution extends smoothly beyond \(T\).*

**Proof (adapting Wang Theorem 4.1).**  The argument follows Wang's induction
scheme.  The curvature evolution for the normalized flow is
\[
  \partial_t R_{ijkl}
  =\chi^2[\Delta R_{ijkl}+P(Rm)]
  +(\nabla\chi^2)\ast\nabla Rm+(\nabla^2\chi^2)\ast Rm
  +\underbrace{(-2\chi^2g)\text{ contributions}}_{(\star)}.
\tag{2.2}
\]

The additional terms from the \(-2\chi^2 g\) part use a key simplification:
\(\nabla g=0\) (Levi-Civita compatibility), so
\[
  \nabla^m(\chi^2 g)=(\nabla^m(\chi^2))\otimes g.
\tag{2.3}
\]
This eliminates the concern that \(\nabla^m g\) might involve \(m\)-th order
Christoffel derivatives.  The normalization terms at order \(m\) are
\(\nabla^m(\chi^2)\ast g + \chi^2\ast\operatorname{Rm}\), both controlled if
lower-order quantities are known.

**Higher derivatives and joint induction.**  Wang's Lemma 4.4 gives the
evolution of \(\nabla^m\operatorname{Rm}\).  The normalization adds terms from
(2.3).  But a subtlety (Step 27 TTCS correction): the covariant derivatives
\(\nabla^q(\chi^2)\) for \(q\ge2\) depend on the evolving Levi-Civita
connection, since \(\chi\) is a fixed smooth function but \(\nabla^q\chi\)
involves the time-dependent Christoffel symbols.  Specifically,
\[
  \partial_t(\nabla^q\chi^2)
  =\sum_{r}(\partial_t\Gamma)\ast\nabla^{q-1}(\chi^2),
\]
and \(\partial_t\Gamma=g^{-1}\ast\nabla(aE)\) involves first derivatives of
curvature.  Therefore the correct induction must jointly estimate
\[
  \{\nabla^j(\chi^2\operatorname{Rm})\}_{j\le m},\qquad
  \{\nabla^q(\chi^2)\}_{q\le m+2},
\]
with the ordering: controlling \(\nabla^{j-1}(\chi^2\operatorname{Rm})\)
and \(\nabla^{q-1}(\chi^2)\) suffices for the next step, because the
Christoffel variation contributes derivatives of curvature one order lower.
Wang's original induction (Lemma 4.5, 4.6) already has exactly this triangular
structure for the unnormalized flow; the normalization terms fit into the same
induction because they contribute at most \(\nabla^m(\chi^2)\ast g\) plus
lower-order cross terms.

**Metric equivalence.** Under (2.1),
\[
  |\partial_tg|=2\chi^2|\operatorname{Ric}+g|
  \le C(|\chi^2\operatorname{Rm}|+\chi^2)
  \le C(K+1).
\]
Hence \(e^{-C(K+1)T}g_0\le g(t)\le e^{C(K+1)T}g_0\) on \([0,T)\).
Metric equivalence alone does not control \(\nabla^q(\chi^2)\) for \(q\ge2\);
this is why the joint induction above is necessary.

**Conclusion.**  Wang's proof (Proposition 4.3 \(\to\) Lemma 4.10 \(\to\)
induction on \(m\)) extends with the joint layer including \(\nabla^q(\chi^2)\)
evolution.  The normalization adds no new highest-order terms at any induction
step.  All weighted derivatives \(\nabla^m(\chi^2 Rm)\) are bounded on
\([0,T)\), and the metric has a smooth limit at \(T\). \(\square\)

## 3. Uniform continuation to \(\theta r^2\)

**Theorem 3.1 (Uniform time).** *Under the hypotheses of the four-dimensional
negative-branch gap theorem (initial Ricci pinching \(\delta\), selected good
support with \(\beta_0\le\varepsilon_0\)), equation (0.1) has a smooth
solution on \([0,\theta r^2]\) for a uniform \(\theta>0\), and the first-exit
conditions F1--F4 hold throughout.*

**Proof.** By Theorem 1.1, the solution exists on some \([0,T_1)\) with \(T_1>0\).

Define \(T_*\) as the supremum of times \(T\le\theta r^2\) such that the
first-exit conditions hold on \([0,T)\):

- **(F1)** \(e^{-1/10}g_0\le g(t)\le e^{1/10}g_0\);
- **(F2)** \(\mathsf S(t)\le 2\mathsf S(0)\);
- **(F3a)** \(\widehat H_2(t)\le 2\widehat H_2(0)\);
- **(F3b)** \(Q(t)\le 2Q(0)\);
- **(F4)** \(J_6(t)\le 2J_6(0)\).

For small enough \(\theta,\varepsilon_0,\delta_0\), the following hold on
\([0,T_*)\) (A03, Step 26, Section 6.2):

1. The three-factor Moser iteration (Section 5 of the unified iteration note)
   gives
   \[
     \|aF(t)\|_\infty\le C\beta/t,\qquad
     \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}.
   \]

2. The metric drift satisfies
   \(I(t)\le(3/2)C\delta\theta^{2/3}r^2<1/20\), strictly improving (F1).

3. Metric comparison (F1) implies Sobolev persistence (F2) and cutoff-gradient
   bounds.

4. The energy inequalities with three-factor absorption give strict improvement
   of (F3a), (F3b), (F4) for small \(\theta\).

5. The critical product satisfies
   \(\beta(t)\le C\beta_0 e^{C\theta}\le\varepsilon_0/2\), preserving smallness.

6. **Splicing bound (TTCS correction).** Fix any \(t_0\in(0,\min(T_1,T_*))\)
   from the initial smooth interval.  Then
   \[
     \sup_{0\le t<T_*}|\chi^2\operatorname{Rm}(t)|
     \le\max\!\left\{\sup_{[0,t_0]}|\operatorname{Rm}|,\;\frac{C\beta}{t_0}\right\}
     <\infty.
   \]
   The first term is finite because \(g(t)\) is smooth on \([0,t_0]\).
   The second uses the Moser bound for \(t\ge t_0\).  By Theorem 2.1, the
   uniform bound up to \(T_*\) implies the flow extends beyond \(T_*\).

If \(T_*<\theta r^2\), the first-exit conditions hold with strict improvement
on \([0,T_*)\) and the splicing bound gives finite weighted curvature up to
\(T_*\).  By Theorem 2.1, the flow extends, contradicting maximality.
Hence \(T_*\ge\theta r^2\). \(\square\)

## 4. Compatibility with the conditional gap chain

The three theorems above close the last obstacle in the negative four-dimensional
chain (A03, Section 7):

\[
\begin{aligned}
&\text{Ric pinching on critical Ishida--LeBrun }M\\
\longrightarrow{}&\text{Maheux--Saloff-Coste Sobolev (A03, \S1)}\\
\longrightarrow{}&\text{small }\beta\text{ at maximal-function good support}\\
\longrightarrow{}&\text{Theorems 1.1, 2.1, 3.1 (this note)}\\
\longrightarrow{}&\text{first-exit energy persistence (Steps 25--27, A03 \S3--4)}\\
\longrightarrow{}&\text{three-factor Moser: }\|aF\|\le C\beta/t,\;
  \|aE\|\le C\delta(r^2/t)^{1/3}\\
\longrightarrow{}&\text{global defect preservation: }Q_{\rm global}(t)\le e^{C\theta}Q_{\rm global}(0)\\
\longrightarrow{}&\text{terminal calibrated Weyl spectrum on plateaux (Steps 3--8)}\\
\longrightarrow{}&\text{harmonic-chart compactness + smooth Einstein limit}\\
\longrightarrow{}&\text{Derdziński forbidden germ}
\end{aligned}
\]

## 5. A03 shifted-curvature formulation (adopted)

A03's Step 27 introduces T = Rm + G with G = (g∧g)/(2(n-1)), giving
Ric(T) = E, ∇G = 0, and U = aT.  This shifted equation has exactly Wang's
structure, including the highest cutoff term χ∇^{m+2}χ*U that must be
integrated by parts once.  The joint induction (∇^mU, ∇^{m+1}χ) with
Move A / Move B / Move C structure rigorously transfers Wang's extension
without suppressing cutoff jets.  See
`Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md`.

This formulation is adopted over the generic-lower-order treatment in §2 above.
The corrections in §2 (∇g = 0, joint induction, TTCS fixes) remain valid as
constraints on any alternative argument.

## 6. What this does not settle

- The chain assumes A03's general-\(p\) inequality (Lemma, \S3.1) and
  Maheux--Saloff-Coste initial Sobolev are correct.  Both have been independently
  derived and script-verified.
- This closes only the critical four-dimensional LeBrun/Ishida--LeBrun negative
  laboratory.  It does not prove the full negative branch for arbitrary
  four-manifolds, the positive branch, dimensions \(n\ge5\), or the original
  all-dimensional Yau Problem 26.
- No Lean formalization.

## References

- Yang source: `Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md`,
  Section 8 (lines 787--823), Section 9 (lines 825--877)
- Wang source: `Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`,
  Theorem 4.1 (lines 396--412), Lemma 4.4--4.5 (lines 426--461)
- Unified three-factor iteration: `workspace/notes/step27_unified_weak_moser_iteration.md`
- A03 general-p and Sobolev: `Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md`
