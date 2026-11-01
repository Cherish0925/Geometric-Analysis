# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md",
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A03/workspace/notes/step19_p4_threshold_and_degenerate_moser.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Sessions/S0910A03/workspace/scripts/verify_step20_weighted_moment_hierarchy.py"
  ]
}
```

## Task

Test a potentially decisive simplification of the Step-20 cutoff-flow first-exit. Given the weighted curvature moments H_q and defect moments J_m in the supplied note, determine whether any pointwise connection or Hessian-a control is actually needed for the zero-order smoothing theorem and metric comparability. Specifically: all Hess(a) terms in the q=2,3 and high-exponent weak estimates are integrated by parts to leave only |da|^2/a and localization gradients; relative Sobolev and fixed-domain overlap then depend only on metric comparability, while metric comparability follows from the integrable pointwise aE estimate. If this is sound, the prior target |chi nabla(aE)| may be unnecessary for the first-exit itself. Check every place it could re-enter: local critical-energy persistence, H_2-to-H_3, curvature and defect Moser recurrences, triangular unweighted Q, preservation of cutoff-gradient bounds, moving volume/balls, and smooth continuation of the normalized cutoff flow. Read Wang Theorem 4.1/Proposition 4.9 and decide whether a terminal bound on |a Rm| (plus fixed smooth cutoff) extends to the normalized flow with -2ag, or what extra qualitative—not dimension-uniform quantitative—derivative input is actually needed. Also derive the curvature high-exponent recurrence from H_3 to |aRm| and verify its scaling C gamma/t. Give a rigorous mathematical memo; do not assume full finite-neighbor implementation or conclude Yau 26.

## Output

# Scientific memo: Step-20 zero-order first-exit simplification

## 1. Main mathematical reading

For the zero-order smoothing theorem and metric comparability, the supplied Step-20 weighted formulation does **not** use pointwise control of  
\[
\chi\nabla(aE),\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\]
nor pointwise control of \(\nabla^2 a\), provided all estimates are kept in weak localized form with fixed spatial cutoffs.

The reason is structural: every \(\nabla^2 a\) term in the curvature, defect, and unweighted \(Q\)-energy identities can be integrated by parts once. The resulting terms contain only
\[
\frac{|da|^2}{a}=4|d\chi|^2
\]
and localization-gradient terms such as \(a|d\eta|^2\). These are controlled from metric comparability because \(\chi,\eta\) are fixed functions. No pointwise connection estimate is needed for those zero-order inequalities.

The weighted derivative estimate
\[
|\chi\nabla(aE)|\le C\delta\,t^{-1/2}(r^2/t)^{1/3}
\]
is therefore not an ingredient for the zero-order first-exit closure described in the task. It is only needed for the older connection/Hessian-drift route, or for a separate quantitative \(C^1\)-type statement.

Smooth continuation is a distinct issue: Wang’s Theorem 4.1 shows for local Ricci flow that a terminal bound on \(|\chi^2\operatorname{Rm}|\) generates the needed qualitative higher derivative bounds. For the normalized flow \(\partial_tg=-2a(\operatorname{Ric}+g)\), the same continuation mechanism should extend after adding lower-order \(ag\) terms, but this adaptation is not literally stated in Wang. If that adaptation is not supplied, the extra terminal input is qualitative boundedness of weighted curvature derivatives, not the dimension-uniform estimate for \(\chi\nabla(aE)\).

---

## 2. Why \(\nabla^2a\) leaves the zero-order estimates

For the normalized cutoff flow
\[
\partial_tg=-2aE,\qquad E=\operatorname{Ric}+g,
\]
the curvature equation has schematic form
\[
\partial_t\operatorname{Rm}
=a\Delta\operatorname{Rm}
+a(\operatorname{Rm}*\operatorname{Rm}+\operatorname{Rm})
+da*\nabla E+(\nabla^2a)*E+aE*\operatorname{Rm}.
\]

The identities
\[
E=\operatorname{contr}(\operatorname{Rm})+g,\qquad 
\nabla E=\operatorname{contr}(\nabla\operatorname{Rm})
\]
give
\[
|E|\le C F,\qquad |\nabla E|\le C|\nabla\operatorname{Rm}|,\qquad
F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

For
\[
H_{q,k}=\int \eta_k^2a^{q-2}F^q,\qquad
v_{q,k}=\eta_k a^{(q-1)/2}F^{q/2},
\]
a representative Hessian-cutoff term is
\[
I=\int \eta^2a^{q-2}F^{q-2}\operatorname{Rm}*(\nabla^2a)*E.
\]
Integrating by parts once gives terms of the form
\[
\nabla a*\nabla\operatorname{Rm}*E,\qquad
\nabla a*\operatorname{Rm}*\nabla E,\qquad
\nabla a*d\eta*\operatorname{Rm}*E,
\]
plus the derivative of \(a^{q-2}F^{q-2}\). Using \(|E|\le CF\), \(|\nabla E|\le C|\nabla\operatorname{Rm}|\), and Young’s inequality,
\[
|I|
\le \varepsilon\int |\nabla v_q|^2
+C_{\varepsilon,q}\int \eta^2\frac{|da|^2}{a}a^{q-2}F^q
+C_q\int a|d\eta|^2a^{q-2}F^q.
\]
Thus the weak curvature estimate contains no pointwise \(\nabla^2a\) term.

The same mechanism applies to the defect moments
\[
J_{m,k}=\int \eta_k^2a^{m-2}|E|^m,\qquad
z_{m,k}=\eta_k a^{(m-1)/2}|E|^{m/2}.
\]
Testing the \(E\)-equation against \(\eta^2a^{m-2}|E|^{m-2}E\), the \((\nabla^2a)*E\) contribution again becomes
\[
\varepsilon\int |\nabla z_m|^2
+C_{\varepsilon,m}\int \eta^2\frac{|da|^2}{a}a^{m-2}|E|^m
+C_m\int a|d\eta|^2a^{m-2}|E|^m.
\]

The key regular identity
\[
\frac{|da|^2}{a}=4|d\chi|^2
\]
is exact for \(a=\chi^2\). Since \(\chi\) is fixed, \(|d\chi|_{g(t)}\) is controlled by metric comparability alone.

---

## 3. Entry points where pointwise connection control could have appeared

### Local critical-energy persistence

For \(q=2\),
\[
H_2' + cX_2
\le C\bigl(r^{-2}H_2+H_3\bigr),
\qquad
X_2=\int|\nabla v_2|^2.
\]
The Hessian-\(a\) terms have already become \((|da|^2/a)H_2\). Metric and volume variations contribute only algebraic potentials bounded by \(aF^3\) and lower-order \(aF^2\). No \(\nabla(aE)\) term appears.

### \(H_2\to H_3\)

For \(q=2,3\),
\[
R_q:=\int \eta^2a^{q-1}F^{q+1}
=\int Fv_q^2
\le \|F\|_{L^2(\widetilde U)}\|v_q\|_{L^4}^2.
\]
The relative Sobolev inequality gives
\[
R_q\le C\gamma\bigl(X_q+r^{-2}H_q\bigr),
\qquad
\gamma=A^2\|F\|_{L^2(\widetilde U)}.
\]
For \(\gamma\) small, this absorbs the reaction for fixed \(q=2,3\). Hence
\[
\int_0^t H_3(s)\,ds\le C\gamma H_2(0),
\]
and the \(q=3\) inequality gives, by backward averaging,
\[
H_3(t)\le \frac{C\gamma H_2(0)}{t}.
\]
Since \(A^4H_2(0)\le \gamma^2\),
\[
\boxed{A^4H_3(t)\le \frac{C\gamma^3}{t}}.
\]
This derivation uses only metric comparability, relative Sobolev, fixed cutoffs, and the weak integration-by-parts treatment of \(\nabla^2a\).

### Curvature and defect Moser recurrences

The high-exponent reaction is controlled by the weighted cubic potential \(H_3\), not by pointwise derivatives.

For curvature,
\[
R_q=\int \eta^2a^{q-1}F^{q+1}
=\int (aF^3)^{1/3}\,\eta^2a^{q-4/3}F^q.
\]
Hölder gives
\[
R_q\le H_3^{1/3}H_{3q/2}^{2/3}.
\]
The exact weighted interpolation is
\[
H_{3q/2}\le H_q^{1/2}H_{2q}^{1/2},
\]
and Sobolev gives
\[
H_{2q}^{1/2}\le CA^2(X_q+r^{-2}H_q).
\]
Therefore
\[
R_q
\le C A^{4/3}H_3^{1/3}H_q^{1/3}(X_q+r^{-2}H_q)^{2/3},
\]
hence
\[
R_q
\le \varepsilon X_q
+C\bigl(\varepsilon^{-2}A^4H_3+r^{-2}\bigr)H_q.
\]
No pointwise \(\nabla(aE)\) estimate is used.

For defect moments,
\[
\int \eta^2a^{m-1}F|E|^m
=\int Fz_m^2
\le H_3^{1/3}J_{3m/2}^{2/3},
\]
with exact interpolation
\[
J_{3m/2}\le J_m^{1/2}J_{2m}^{1/2},
\]
and Sobolev control of \(J_{2m}^{1/2}\). This is the same weighted mechanism.

### Triangular unweighted \(Q\)

For
\[
Q_\alpha(t)=\int \eta_\alpha^2|E|^2,
\]
the \(E\)-equation is homogeneous in \(E\):
\[
\partial_tE
=a\Delta_LE-2aE+da*\nabla E+(\nabla^2a)*E
+a\operatorname{Rm}*E+aE*E.
\]
Testing by \(\eta^2E\), the Hessian-\(a\) term is integrated by parts:
\[
\int \eta^2E*(\nabla^2a)*E
\leadsto
\int \eta^2\nabla a*E*\nabla E
+\int \eta\,d\eta*\nabla a*E*E.
\]
Young gives
\[
\frac{d}{dt}Q_\alpha+c\int\eta^2a|\nabla E|^2
\le
C\int \eta^2\left(\frac{|da|^2}{a}+a+a|\operatorname{Rm}|\right)|E|^2
+C\int a|d\eta|^2|E|^2.
\]
The curvature potential is absorbed by
\[
\int a|\operatorname{Rm}|\,|\eta E|^2
=\int |\operatorname{Rm}|\,|\chi\eta E|^2
\le \|\operatorname{Rm}\|_2\|\chi\eta E\|_4^2,
\]
using the local critical \(L^2\) budget and Sobolev. Again no pointwise connection term appears.

### Cutoff-gradient bounds

For fixed \(\chi,\eta\),
\[
|d\chi|_{g(t)}^2,\quad |d\eta|_{g(t)}^2
\]
are controlled by metric comparability:
\[
e^{-\kappa}g(0)\le g(t)\le e^\kappa g(0)
\quad\Longrightarrow\quad
|d\chi|_{g(t)}^2\le e^\kappa |d\chi|_{g(0)}^2.
\]
No control of \(\nabla^2a\) is needed in the zero-order estimates.

### Moving volume and balls

The volume form satisfies
\[
\partial_t d\mu=-\operatorname{tr}(aE)\,d\mu,
\]
so integrable pointwise control of \(|aE|\) gives volume comparability on fixed domains.

Distance comparability follows from metric comparability:
\[
e^{-\kappa/2}d_{g(0)}(x,y)
\le d_{g(t)}(x,y)
\le e^{\kappa/2}d_{g(0)}(x,y).
\]
Thus fixed-domain overlap and relative Sobolev constants can be transported using bilipschitz control. No pointwise connection estimate is required if the finite-neighbor system is formulated with fixed spatial cutoffs.

---

## 4. Curvature high-exponent recurrence and the \(C\gamma/t\) scaling

Let
\[
X_q=\int|\nabla v_q|^2,\qquad
v_q=\eta a^{(q-1)/2}F^{q/2}.
\]
After using the \(H_3\) reaction estimate above, the curvature energy inequality has the form
\[
\frac{d}{dt}H_q+cX_q
\le Cq^\sigma\bigl(r^{-2}+A^4H_3(t)\bigr)H_q,
\tag{4.1}
\]
for some fixed polynomial power \(\sigma\). On a positive-time cylinder \(s\in[t/2,t]\),
\[
A^4H_3(s)\le \frac{C\gamma^3}{s}\le \frac{C\gamma^3}{t}.
\]

Use nested time intervals \(I_j\subset[t/2,t]\), nested spatial cutoffs, and exponents
\[
q_{j+1}=\frac32q_j,\qquad q_0=2.
\]
With a time cutoff supported in \(I_j\), equal to \(1\) on \(I_{j+1}\), (4.1) gives
\[
\sup_{I_{j+1}}H_{q_j}
+\int_{I_{j+1}}X_{q_j}
\le
Cq_j^\sigma\Theta_j
\int_{I_j}H_{q_j},
\tag{4.2}
\]
where
\[
\Theta_j=(\Delta t_j)^{-1}+r^{-2}+\gamma^3t^{-1}.
\]
Choosing the time gaps so that \(\Delta t_j\asymp tq_j^{-N}\) for a fixed large \(N\), and using \(t\le \theta r^2\), gives
\[
\Theta_j\le Cq_j^N t^{-1}
\]
for small fixed \(\gamma\).

Now Sobolev and exact weighted interpolation give
\[
H_{2q}^{1/2}
\le CA^2(X_q+r^{-2}H_q),
\]
and
\[
H_{3q/2}\le H_q^{1/2}H_{2q}^{1/2}.
\]
Thus
\[
\int_{I_{j+1}}H_{q_{j+1}}
\le
CA^2
\left(\sup_{I_{j+1}}H_{q_j}\right)^{1/2}
\int_{I_{j+1}}(X_{q_j}+r^{-2}H_{q_j}).
\]
Using (4.2),
\[
\int_{I_{j+1}}H_{q_{j+1}}
\le
CA^2
\bigl(q_j^\sigma\Theta_j\bigr)^{3/2}
\left(\int_{I_j}H_{q_j}\right)^{3/2}.
\]

Define
\[
Y_j=\left(\int_{I_j}H_{q_j}\right)^{1/q_j}.
\]
Since \(q_{j+1}=\frac32q_j\),
\[
Y_{j+1}
\le
C^{1/q_{j+1}}
A^{2/q_{j+1}}
\bigl(q_j^\sigma\Theta_j\bigr)^{1/q_j}
Y_j.
\]
The products converge because
\[
\sum_{j\ge0}\frac1{q_j}=\frac32,\qquad
\sum_{j\ge0}\frac1{q_{j+1}}=1,\qquad
\sum_{j\ge0}\frac{\log q_j}{q_j}<\infty.
\]
Therefore
\[
\|aF\|_{L^\infty(U_\infty\times I_\infty)}
\le
C A^2 t^{-3/2}
\left(\int_{t/2}^{t}H_2(s)\,ds\right)^{1/2}.
\]
Using \(H_2(s)\le C H_2(0)\),
\[
\left(\int_{t/2}^{t}H_2(s)\,ds\right)^{1/2}
\le Ct^{1/2}H_2(0)^{1/2}.
\]
Since
\[
A^2H_2(0)^{1/2}\le \gamma,
\]
one obtains
\[
\boxed{\|aF(t)\|_{L^\infty(U_\infty)}
\le \frac{C\gamma}{t}.}
\]
In particular,
\[
\boxed{\|a\,\operatorname{Rm}(t)\|_{L^\infty}
\le \frac{C\gamma}{t}.}
\]

This verifies the expected \(C\gamma/t\) scaling. The derivation uses the weighted \(H_3\) potential and the exact \(q\mapsto 3q/2\) parabolic recurrence. The finite-neighbor implementation still has to carry the enlarged supports, overlap constants, and evolving Sobolev constants through this recurrence.

---

## 5. Defect smoothing and metric comparability

The defect recurrence is parallel. From
\[
J_m=\int\eta^2a^{m-2}|E|^m,
\qquad
z_m=\eta a^{(m-1)/2}|E|^{m/2},
\]
the reaction satisfies
\[
\int \eta^2a^{m-1}F|E|^m
=\int Fz_m^2
\le
\varepsilon X_m+
C\bigl(\varepsilon^{-2}A^4H_3+r^{-2}\bigr)J_m.
\]
Starting from \(m=6\), the parabolic smoothing exponent in dimension four is
\[
\frac{n}{2m}=\frac{4}{12}=\frac13.
\]
Thus the supplied Step-20 scaling
\[
\boxed{|aE(x,t)|
\le C\delta\left(1+\frac{r^2}{t}\right)^{1/3}}
\]
is consistent with the weighted hierarchy.

Metric comparability then follows directly:
\[
\left|\partial_t\log g_t(v,v)\right|
\le 2|aE|_{g(t)}.
\]
Hence
\[
\int_0^{\theta r^2}|aE(s)|\,ds
\le
C\delta\int_0^{\theta r^2}
\left(1+\frac{r^2}{s}\right)^{1/3}ds
<\infty.
\]
The singularity \(s^{-1/3}\) is integrable. Therefore the zero-order defect estimate supplies metric comparability without any pointwise connection estimate.

Once metric comparability is available, fixed-domain Sobolev constants, cutoff-gradient bounds, volume comparability, and finite overlap constants are transported by bilipschitz comparison.

---

## 6. Reading Wang Theorem 4.1 and Proposition 4.9

In Wang’s Section 4:

- Theorem 4.1 states that for local Ricci flow
  \[
  \partial_tg=-2\chi^2\operatorname{Ric},
  \]
  a uniform bound on
  \[
  |\chi^2\operatorname{Rm}|_\infty
  \]
  up to a finite terminal time yields smooth extension.

- Proposition 4.9 states that \(|\chi^2\operatorname{Rm}|_\infty\) gives uniform metric equivalence, hence uniform \(|\nabla\chi|_\infty\) and Sobolev constants.

- Proposition 4.3 and Lemmas 4.10–4.14 then generate the qualitative higher derivative bounds
  \[
  |\nabla^m(\chi^2\operatorname{Rm})|_\infty<\infty
  \]
  needed for Hamilton-style continuation.

For the normalized cutoff flow
\[
\partial_tg=-2a(\operatorname{Ric}+g),
\]
the extra \(-2ag\) part contributes lower-order curvature variation terms of the schematic types
\[
a\operatorname{Rm},\qquad (\nabla^2a)*g,
\]
or, when combined with the Ricci part,
\[
(\nabla^2a)*E,\qquad da*\nabla E,\qquad aE*\operatorname{Rm}.
\]
Because
\[
E=\operatorname{contr}(\operatorname{Rm})+g,\qquad
\nabla^jE=\operatorname{contr}(\nabla^j\operatorname{Rm})\quad(j\ge1),
\]
these terms have the same top-order structure as Wang’s local Ricci flow estimates, with additional lower-order \(g\)-terms. The velocity is also bounded by
\[
|aE|\le C(|a\operatorname{Rm}|+a)\le C(|a\operatorname{Rm}|+1).
\]

Thus the tensor algebra supports the following continuation principle for the normalized flow: a terminal bound on \(|a\operatorname{Rm}|\), together with fixed smooth \(a=\chi^2\), should generate the same qualitative weighted derivative bounds as in Wang’s proof. The published theorem, however, is written for \(-2\chi^2\operatorname{Ric}\), not explicitly for \(-2a(\operatorname{Ric}+g)\).

If one does not write out that normalized adaptation, the extra terminal input needed is qualitative:
\[
\sup_{[T-\varepsilon,T)}|\nabla^m(a\operatorname{Rm})|<\infty
\quad\text{for all }m,
\]
together with the corresponding evolving-metric bounds for derivatives of the fixed cutoff generated in Wang’s induction. These constants may depend on the particular flow, terminal time, cutoff, and initial high derivatives. They do **not** need the quantitative, volume-independent, \(\delta\)-linear estimate for \(\chi\nabla(aE)\).

---

## 7. Scientific consequence for the Step-20 first-exit architecture

The simplification is mathematically sound at the zero-order level:

\[
\text{weighted }H_q,J_m\text{ estimates}
\quad\Longrightarrow\quad
|a\operatorname{Rm}|\lesssim \gamma/t,\quad
|aE|\lesssim \delta(1+r^2/t)^{1/3}
\quad\Longrightarrow\quad
\text{metric comparability}.
\]

Pointwise connection control and pointwise Hessian-\(a\) control do not re-enter the zero-order smoothing theorem, local critical-energy persistence, \(H_2\to H_3\), curvature/defect Moser recurrences, triangular unweighted \(Q\), cutoff-gradient preservation, or fixed-domain Sobolev transport.

The remaining mathematical substance is the complete finite-neighbor parabolic implementation and the normalized analogue of Wang’s qualitative continuation theorem. Neither requires the earlier quantitative target for \(|\chi\nabla(aE)|\) as part of the zero-order first-exit mechanism.