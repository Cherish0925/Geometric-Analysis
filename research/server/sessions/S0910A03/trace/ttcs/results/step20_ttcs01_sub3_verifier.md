# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step18_simultaneous_bootstrap_and_fixed_p_defect.md",
    "Sessions/S0910A03/workspace/notes/step19_p4_threshold_and_degenerate_moser.md",
    "Sessions/S0910A01/workspace/notes/step19_whitney_tensor_estimate.md",
    "Sessions/S0910A03/workspace/scripts/verify_step20_weighted_moment_hierarchy.py",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Verify and strengthen the proposed weighted-moment bridge for the normalized cutoff flow in dimension four. The active goal is Yau Problem 26, but this task concerns the four-dimensional negative critical Ishida–LeBrun laboratory. Read the supplied Step 18–20 notes, Wang source excerpt/object, and exponent-check script. Assess these exact points by derivation rather than analogy: (1) for curvature F=(1+|Rm|^2)^{1/2}, whether moments H_q=∫η² a^{q-2}F^q, a=χ², naturally have dissipation/sobolev variable η a^{(q-1)/2}F^{q/2}, and what local differential inequality—including η, da, evolving measure, full velocity aE, and normalized source—can rigorously be asserted; (2) whether H_2 small and the q=3 interpolation can yield A^4 H_3(t)≤C beta^3/t (or the correct beta/r source variant) without dividing by a; (3) for the Einstein defect, whether J_m=∫η²a^{m-2}|E|^m propagates from initial |E|≤δ under the known tensor cancellation, and whether weighted cubic H_3 controls its curvature reaction through the exact J_m–J_{3m/2}–J_{2m} interpolation; (4) whether this hierarchy can start at a fixed p=6 and iterate to a pointwise a|E| estimate, thereby genuinely replacing the weaker I_p=∫|aE|^p, or identify the exact term that prevents it; (5) assess the A01 Whitney-ball argument, especially whether its use of a physical time θr² on every Whitney level is compatible with obtaining pointwise information at arbitrary t near zero and whether global support energy alone really gives the required local smallness. Give a mathematical memo distinguishing derived identities, conditional estimates, and any fatal mismatch. Do not infer that the full Yau problem is solved.

## Output

# Scientific memo: weighted moments for the normalized cutoff flow

Let
\[
\partial_tg=-2aE,\qquad E=\Ric+g,\qquad a=\chi^2,\qquad
F=(1+|\Rm|^2)^{1/2}.
\]
All calculations below are in dimension four. The localization functions are fixed in time unless stated otherwise.

## 1. Curvature hierarchy

### 1.1 Evolution structure and the natural weight

For the full velocity \(-2aE\), the curvature equation has the tensor structure
\[
\partial_t\Rm
=a\Delta\Rm+a(\Rm*\Rm+\Rm)
+da*\nabla E+\nabla^2a*E+aE*\Rm.
\tag{1}
\]
Here \(\nabla E=\nabla\Ric\) is a contraction of \(\nabla\Rm\), while
\[
|E|\le C(1+|\Rm|)\le CF,\qquad |\nabla E|\le C|\nabla\Rm|.
\tag{2}
\]
Writing the velocity as one tensor \(aE\) is useful: the Hessian term is
\(\nabla^2a*E\), hence the entire equation vanishes when \(E=0\). If one instead splits the Ricci and normalization parts, the latter contributes
\(\nabla^2a\owedge g+a\Rm\); these lower powers are still dominated by \(F\).

For
\[
H_q=\int \eta^2a^{q-2}F^q\,d\mu,\qquad q\ge2,
\]
the principal diffusion term is tested against
\(\eta^2a^{q-2}F^{q-2}\Rm\). Its tensor dissipation is
\[
\mathcal T_q
=\int\eta^2a^{q-1}F^{q-2}|\nabla\Rm|^2.
\tag{3}
\]
Completing the cutoff-weight square gives the Sobolev variable
\[
v_q=\eta\,a^{(q-1)/2}F^{q/2}.
\tag{4}
\]
Indeed, the derivative of the \(a\)-factor produces
\[
a^{q-3}|da|^2F^q
=\frac{|da|^2}{a}\,a^{q-2}F^q,
\qquad
\frac{|da|^2}{a}=4|d\chi|^2.
\tag{5}
\]
Thus no singular quantity occurs at \(\chi=0\), including when \(q=2\).

The Hessian term illustrates the complete power count. After one integration by parts,
\[
\begin{aligned}
&\left|\int\eta^2a^{q-2}F^{q-2}
 \langle\Rm,\nabla^2a*E\rangle\right|\\
&\quad\le
\varepsilon\mathcal T_q
+C_{\varepsilon,q}\int\eta^2a^{q-3}|da|^2F^q
+C_{\varepsilon,q}\int a^{q-1}|d\eta|^2F^q .
\end{aligned}
\tag{6}
\]
Only \(da\), rather than a pointwise estimate for \(\nabla^2a\), remains.

The evolving volume contributes
\[
\partial_td\mu=-a\,\tr(E)\,d\mu,
\tag{7}
\]
hence
\[
\left|\int \eta^2a^{q-2}F^q\,\partial_td\mu\right|
\le C\int\eta^2a^{q-1}F^{q+1}\,d\mu.
\tag{8}
\]
The metric-inverse variation in \(\partial_t|\Rm|^2\) has the same upper estimate.

### 1.2 Differential inequality

For every fixed \(q\ge2\), smoothness and one integration by parts give
\[
\boxed{
\begin{aligned}
\frac d{dt}H_q+c\int|\nabla v_q|^2
\le Cq^2\bigg[&
\int a^{q-1}|d\eta|^2F^q\\
&+\int\eta^2\frac{|da|^2}{a}\,a^{q-2}F^q\\
&+\int\eta^2a^{q-1}F^{q+1}\bigg].
\end{aligned}}
\tag{9}
\]
Changing \(Cq^2\) to another polynomial in \(q\) accommodates tensor-convention constants. This does not affect the iteration.

If \(\eta=\eta(t)\), one additionally has
\[
2\int \eta\,\partial_t\eta\,a^{q-2}F^q.
\]
Formula (9) contains the localization terms, cutoff drift, evolving measure, metric-norm variation, and normalization source.

The exact algebra behind the hierarchy is
\[
Fv_q^2=\eta^2a^{q-1}F^{q+1},
\qquad
v_q^4=\eta^4a^{2q-2}F^{2q}.
\tag{10}
\]
The second expression is not literally \(H_{2q}\) with the same \(\eta\), because it has \(\eta^4\) rather than \(\eta^2\). Nested cutoffs repair this: take an outer cutoff in \(v_q\) which equals one on the support of the inner \(H_{2q}\).

These powers agree with Wang’s Section 5 formulas in dimension four: the \(q=2\) dissipation uses \(\nabla(\chi|\Rm|)\), while the \(q=3\) dissipation uses \(\nabla(\chi^2|\Rm|^{3/2})\). The normalized flow requires the additional \(F\)-regularization and the preceding treatment of \(\nabla^2a\).

---

## 2. The \(H_2\)-to-\(H_3\) bridge

Let an enlarged ball carry
\[
\|\phi\|_4\le A\bigl(\|\nabla\phi\|_2+r^{-1}\|\phi\|_2\bigr),
\]
and define
\[
\gamma=A^2\|F\|_{L^2(\widetilde B)}.
\tag{11}
\]
Assume \(\gamma\) is sufficiently small and remains comparable to its initial value on the provisional interval.

For \(q=2\),
\[
H_3=\int\eta^2aF^3=\int Fv_2^2
\le C\gamma\left(\int|\nabla v_2|^2+r^{-2}H_2\right).
\tag{12}
\]
Thus the curvature reaction in (9) is absorbed, giving
\[
\sup_{s\le t}H_2(s)+\int_0^t\!\!\int|\nabla v_2|^2
\le Ce^{Ct/r^2}H_2(0),
\tag{13}
\]
and, for \(t\le\theta r^2\),
\[
\int_0^tH_3(s)\,ds\le C\gamma H_2(0).
\tag{14}
\]

At \(q=3\),
\[
H_4=\int\eta^2a^2F^4=\int Fv_3^2
\le C\gamma\left(\int|\nabla v_3|^2+r^{-2}H_3\right).
\tag{15}
\]
After absorption, the \(q=3\) inequality gives
\[
\frac d{dt}H_3\le Cr^{-2}H_3.
\]
Averaging this inequality over earlier times and using (14) yields
\[
H_3(t)\le \frac{C\gamma H_2(0)}{t}.
\tag{16}
\]
Since \(H_2(0)\le\gamma^2/A^4\),
\[
\boxed{A^4H_3(t)\le \frac{C\gamma^3}{t}},
\qquad 0<t\le\theta r^2.
\tag{17}
\]

If
\[
\beta=A^2\|\Rm\|_2,
\]
then generally
\[
\gamma\le \beta+C A^2\Vol(\widetilde B)^{1/2}
\le \beta+Cr^2.
\tag{18}
\]
Therefore the unconditional form in terms of Wang’s \(\beta\) is
\[
A^4H_3(t)\le \frac{C(\beta+Cr^2)^3}{t}.
\tag{19}
\]
In the near-Einstein setting \(|E|\le\delta\ll1\), one has
\(|\Ric|\ge c>0\), hence \(F\le C|\Rm|\) in \(L^2\), and then
\(\gamma\le C\beta\). Under that additional input, (17) becomes
\[
A^4H_3(t)\le \frac{C\beta^3}{t}.
\tag{20}
\]

Thus the proposed \(\beta^3/t\) scaling is derivable, but either the near-Einstein lower curvature scale or the replacement \(\beta\mapsto\beta+Cr^2\) is required. The use of \(F\) prevents an additive normalized-flow source from escaping the hierarchy.

---

## 3. Einstein-defect moments

Set \(G=|E|\) and
\[
J_m=\int\eta^2a^{m-2}G^m,\qquad
z_m=\eta a^{(m-1)/2}G^{m/2}.
\tag{21}
\]
Testing the exact tensor equation for \(E\), before scalarizing, retains
\[
\int\eta^2a^{m-1}G^{m-2}|\nabla E|^2.
\]
The inverse-metric variation cancels the cubic tensor reaction described in Step 18. The volume term remains, but
\[
a|\tr E|G^m\le CaG^{m+1}\le CaFG^m,
\tag{22}
\]
because \(G\le CF\).

The same integration-by-parts calculation as for curvature gives
\[
\boxed{
\begin{aligned}
\frac d{dt}J_m+c\int|\nabla z_m|^2
\le C m^2\bigg[&
\int a^{m-1}|d\eta|^2G^m\\
&+\int\eta^2\frac{|da|^2}{a}a^{m-2}G^m\\
&+\int\eta^2a^{m-1}FG^m\bigg].
\end{aligned}}
\tag{23}
\]
All cutoff commutators close at the \(J_m\) weight. In particular,
\[
a^{m-3}|da|^2G^m
=\frac{|da|^2}{a}a^{m-2}G^m.
\tag{24}
\]

For one fixed \(m\), the curvature reaction can be absorbed directly:
\[
\int Fz_m^2
\le C\gamma\left(\int|\nabla z_m|^2+r^{-2}J_m\right).
\tag{25}
\]
Consequently \(J_6\) propagates when the critical curvature size is chosen small depending on \(m=6\). Initial pointwise control gives
\[
J_6(0)\le \delta^6\Vol(\widetilde B).
\tag{26}
\]

### Exact weighted-cubic interpolation

With an outer cutoff equal to one on the support of \(\eta\),
\[
\begin{aligned}
\int \eta^2a^{m-1}FG^m
&\le H_3^{1/3}J_{3m/2}^{2/3},\\
J_{3m/2}
&\le J_m^{1/2}J_{2m}^{1/2}.
\end{aligned}
\tag{27}
\]
The first line follows from
\[
Fz_m^2=(aF^3)^{1/3}\bigl(a^{-1/3}z_m^2\bigr),
\]
since
\[
\bigl(a^{-1/3}z_m^2\bigr)^{3/2}
=\eta^3a^{3m/2-2}G^{3m/2}.
\]
The second line is the exact geometric interpolation of the two weighted densities.

Sobolev gives, on the inner localization region,
\[
J_{2m}^{1/2}\le
C A^2\left(\int|\nabla z_m|^2+r^{-2}J_m\right).
\tag{28}
\]
Combining (27)–(28) and Young’s inequality produces
\[
\int \eta^2a^{m-1}FG^m
\le \varepsilon X_m+
C\varepsilon^{-2}A^4H_3J_m,
\tag{29}
\]
where \(X_m=\int|\nabla z_m|^2+r^{-2}J_m\). This verifies the script’s weighted-cubic identity at the integral level.

---

## 4. Starting at \(p=6\) and reaching \(a|E|\)

The hierarchy is strong enough in its powers:

* \(J_6\) uses \(a^4|E|^6\), whereas \(I_6=\int a^6|E|^6\). Thus \(J_6\) carries more information near the cutoff edge.
* Pointwise,
  \[
  \bigl(a^{m-2}G^m\bigr)^{1/m}
  =a^{1-2/m}G\longrightarrow aG.
  \]

After Young’s inequality, the high-exponent energy equation contains
\[
C m^3A^4H_3(t)J_m
\lesssim \frac{Cm^3\gamma^3}{t}J_m.
\tag{30}
\]
This coefficient cannot be integrated from time zero. The correct two-stage procedure is:

1. propagate \(J_6\) from \(t=0\) using the fixed-exponent absorption (25);
2. for a requested time \(t>0\), perform the high-exponent iteration on a cylinder contained in \([t/2,t]\), where \(H_3(s)\le C\gamma^3/(A^4t)\).

The parabolic exponent is \(m\mapsto3m/2\). The required spacetime identity is
\[
J_{3m/2}\le J_m^{1/2}J_{2m}^{1/2},
\]
so the slight mismatch between \(\int z_m^2\) and \(J_m\) causes no loss. Nested spatial and temporal cutoffs then give
\[
\|aE(\cdot,t)\|_{L^\infty(B')}
\le
C A^{2/3}(t^{-1}+r^{-2})^{1/3}J_6(0)^{1/6}.
\tag{31}
\]
Using \(A\lesssim rV^{-1/4}\) and (26),
\[
\boxed{
\|aE(\cdot,t)\|_\infty
\le C\delta\left(1+\frac{r^2}{t}\right)^{1/3}},
\tag{32}
\]
which has the desired \(p=6\) behavior.

Thus no exponent incompatibility prevents the \(J_m\) bridge from replacing \(I_p\) for the pointwise estimate of \(aE\). What is not supplied by this hierarchy is
\[
|\chi\nabla(aE)|
\lesssim \delta\,t^{-1/2}(r^2/t)^{1/3}.
\]
The connection and cutoff-Hessian drift in Step 19 still require a separate weighted derivative estimate.

---

## 5. Whitney-ball argument

Let \(a_0=\chi(y)^2\) and
\[
\ell=cr\chi(y).
\]
Then
\[
\frac{a}{a_0}\in[(1-Lc)^2,(1+Lc)^2]
\]
on \(B_\ell(y)\). With effective time \(\tau=a_0t\),
\[
\frac{\tau}{\ell^2}
=\frac{t}{c^2r^2}.
\tag{33}
\]
Therefore one physical interval \(0<t\le\theta r^2\), with \(\theta<c^2\), is compatible with every Whitney level. For arbitrary small \(t\), the diffusion radius
\[
\sqrt{a_0t}=\chi(y)\sqrt t
\]
is still contained in \(B_\ell(y)\). The resulting \(1/t\) estimate becomes large as \(t\downarrow0\), exactly as expected. There is no time-scale mismatch here.

Two corrections are material:

1. The coefficient variation is
   \[
   \frac{|a-a_0|}{a_0}\le 2Lc+(Lc)^2,
   \]
   which is \(O(c)\), not \(O(c^2)\). It remains controllable by choosing \(c\) small, but it must be retained at first order.

2. A single energy estimate over a union of arbitrarily many support components does not imply uniform Whitney-scale smallness. The valid local transfer is
   \[
   \int_{B_{10r}(y)}F^2
   \le K_0\Vol(B_{10r}(y))
   \Longrightarrow
   \ell^4\fint_{B_\ell(y)}F^2
   \le C K_0r^4,
   \tag{34}
   \]
   by Bishop–Gromov comparison in the initial metric and provisional metric equivalence. An equivalent per-component or finite-neighbor energy budget also works. A lone number
   \(\int_\Omega F^2\le K_0\Vol(\Omega)\) for a large disconnected union permits concentration of the entire energy in one component and introduces the number of components into (34).

Bounded overlap controls sums of unnormalized integrals. It does not, by itself, control sums of volume-normalized energies.

## Overall mathematical assessment

The weighted powers in the Step 20 script are the correct ones. The curvature \(H_2\to H_3\) smoothing and the defect
\[
J_m\to J_{3m/2}\to J_{2m}
\]
interpolation can be derived without dividing by \(a\); every apparent quotient reduces to \(4|d\chi|^2\). With nested cutoffs, local Sobolev persistence, and local \(F\)-energy smallness, the bridge yields the \(p=6\) pointwise estimate for \(aE\).

The remaining analytic substance is the full localized implementation of (9) and (23) on the evolving finite-neighbor system, plus the separate weighted derivative estimate needed for connection and cutoff-Hessian control. Wang’s displayed \(q=2,3\) calculations strongly support the weights, but his global unnormalized local Ricci flow theorem does not itself supply these normalized, localized conclusions.