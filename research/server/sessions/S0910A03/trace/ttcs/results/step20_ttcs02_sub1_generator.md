# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md",
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A03/workspace/notes/step19_p4_threshold_and_degenerate_moser.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Develop or refute a derivative-free first-exit theorem for the normalized cutoff flow based solely on weak weighted moments. Use H_q=∫eta²a^(q-2)F^q to obtain H_3 and then |aRm|, J_m=∫eta²a^(m-2)|E|^m to obtain |aE|, and triangular local Q energies. Ask whether one can choose the provisional quantities so no evolving Hess(a) or connection norm is ever assumed: only metric equivalence, local Sobolev, local energy, cutoff-gradient bounds, fixed-domain containment, and weighted pointwise curvature/velocity. If possible, formulate the exact first-exit closure and identify what remains to prove (especially smooth continuation for dg/dt=-2a(Ric+g)); if impossible, exhibit the precise term that cannot be controlled weakly. Include finite-neighbor and buffered-good-ball dependencies and preserve the distinction between local averages and support-global averages.

## Output

### Main conclusion

At the zero-order level, a derivative-free first-exit argument is structurally viable. Neither an evolving \(\nabla^2 a\) bound nor a connection bound is needed to propagate the weighted curvature moments, weighted defect moments, metric equivalence, local Sobolev inequalities, local critical energy, or the unweighted defect integral. Every appearance of \(\nabla^2a\) in the tensor equations can be integrated by parts, after which only
\[
\frac{|da|^2}{a}=4|d\chi|^2
\]
appears. The identity
\[
\nabla E=\operatorname{contr}(\nabla\operatorname{Rm})
\]
closes the curvature dissipation.

The resulting first-exit theorem is conditional on two substantial analytic results:

1. a complete nested weighted Moser theorem deriving \(|a\operatorname{Rm}|\) and \(|aE|\) from \(H_3\) and \(J_6\);
2. smooth continuation for
   \[
   \partial_tg=-2a(\operatorname{Ric}+g)
   \]
   under a bound for \(|a\operatorname{Rm}|\), extending Wang’s continuation theorem for local Ricci flow.

No zero-order term presently forces a pointwise curvature derivative. The term
\[
a\nabla\operatorname{Rm}*U,\qquad U=aE,
\]
appears only after differentiating the \(U\)-equation. It is therefore absent from the proposed first-exit system. It remains relevant only if a later argument requires a quantitative connection drift or a pointwise estimate for \(\chi\nabla U\).

---

## 1. Geometric data and finite-neighbor formulation

Work in dimension four. Fix \(0\leq\chi\leq1\), \(a=\chi^2\), and a finite family of fixed nested domains
\[
U_\alpha^-\Subset U_\alpha\Subset U_\alpha^+
\]
whose separations are comparable to \(r\). Assume:

- \(\{U_\alpha^-\}\) covers \(\{a>0\}\);
- every \(U_\alpha^+\) lies in the union of at most \(N\) centered buffered good balls;
- each point belongs to at most \(N\) outer domains;
- localization functions \(\eta_{\alpha,k}\) satisfy
  \[
  \eta_{\alpha,k+1}\equiv1
  \quad\text{on }\operatorname{supp}\eta_{\alpha,k+2},
  \qquad
  |d\eta_{\alpha,k}|_{g_0}\leq C2^k r^{-1};
  \]
- on every outer domain,
  \[
  \|u\|_{L^4(g_0)}^2
  \leq A_\alpha^2\left(\|\nabla u\|_{L^2(g_0)}^2
  +r^{-2}\|u\|_{L^2(g_0)}^2\right),
  \]
  with
  \[
  A_\alpha\leq C_S r\,V_\alpha^{-1/4},
  \qquad
  V_\alpha=\operatorname{Vol}_{g_0}B_{g_0}(x_\alpha,r).
  \]

The actual critical input should be defined on the complete outer star:
\[
\Gamma_0
=
\sup_\alpha A_\alpha^2
\left(
\sum_{\beta\in\mathcal N(\alpha)}
\int_{U_\beta^+}F_0^2\,d\mu_0
\right)^{1/2},
\qquad
F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]
The smallness assumption is \(\Gamma_0\leq\bar\gamma\), where \(\bar\gamma\) depends on \(C_S,N\), volume comparison constants, and the fixed buffer geometry.

A centered local budget such as
\[
\fint_{B_{g_0}(x_\alpha,10r)}F_0^2\leq K_0
\]
gives
\[
\Gamma_0\leq
C(C_S,C_V,N)\,r^2\sqrt{K_0}.
\]
An average over a large disconnected support union does not imply this estimate on each outer star: one component can contain nearly all the curvature energy. The curvature assumptions must therefore remain centered and local.

By contrast, the unweighted defect is propagated through total unnormalized integrals. Bounded overlap relates \(\sum_\alpha Q_\alpha\) to the integral over the full support; division by the individual ball volumes would destroy that relation in a collapsed family.

---

## 2. Weak curvature hierarchy and creation of \(H_3\)

Set
\[
H_{q,\alpha,k}
=
\int\eta_{\alpha,k}^2a^{q-2}F^q\,d\mu_t,
\qquad
v_{q,\alpha,k}
=
\eta_{\alpha,k}a^{(q-1)/2}F^{q/2},
\]
and
\[
X_{q,\alpha,k}=\int|\nabla v_{q,\alpha,k}|^2\,d\mu_t.
\]

On any interval where the metric and local Sobolev constants remain comparable to their initial values, tensor testing gives
\[
\frac d{dt}H_{q,\alpha,k}
+c_qX_{q,\alpha,k}
\leq
Cq^2\left[
r^{-2}\sum_{\beta\in\mathcal N(\alpha)}
H_{q,\beta,k-1}
+
\int\eta_{\alpha,k}^2a^{q-1}F^{q+1}
\right].
\tag{2.1}
\]
The \(\nabla^2a*E\) term has already been integrated by parts here. Its derivatives landing on \(E\) are absorbed using
\[
|\nabla E|\leq C|\nabla\operatorname{Rm}|,
\qquad |E|\leq CF.
\]
All remaining cutoff coefficients are bounded by \(Cr^{-2}\) through
\[
\frac{|da|^2}{a}=4|d\chi|^2.
\]

At \(q=2\),
\[
H_3=\int Fv_2^2
\leq \|F\|_2\|v_2\|_4^2
\leq C\Gamma(t)\bigl(X_2+r^{-2}H_2\bigr).
\]
For \(\Gamma(t)\) sufficiently small, this is absorbed into (2.1), yielding local \(H_2\) persistence and
\[
\int_0^tH_{3,\alpha}(s)\,ds
\leq
C\Gamma_0
\sum_{\beta\in\mathcal N(\alpha)}H_{2,\beta}(0).
\tag{2.2}
\]

At \(q=3\), the reaction is again controlled directly by the critical \(L^2\) curvature input. Backward averaging of the resulting \(H_3\) inequality gives
\[
A_\alpha^4H_{3,\alpha}(t)
\leq
\frac{C\Gamma_0^3}{t},
\qquad 0<t\leq\theta r^2.
\tag{2.3}
\]

### High powers from the cubic potential

For \(q\geq3\), write
\[
\mathcal R_q
=
\int\eta^2a^{q-1}F^{q+1}
=
\int Fv_q^2.
\]
The exact factorization
\[
Fv_q^2=(aF^3)^{1/3}(a^{-1/3}v_q^2)
\]
gives, after localization,
\[
\mathcal R_q
\leq
H_3^{1/3}H_{3q/2}^{2/3}.
\]
Interpolation and Sobolev yield
\[
H_{3q/2}
\leq H_q^{1/2}H_{2q}^{1/2},
\qquad
H_{2q}^{1/2}\leq
CA_\alpha^2(X_q+r^{-2}H_q),
\]
and consequently
\[
\mathcal R_q
\leq
\varepsilon X_q+
C\left(r^{-2}+\varepsilon^{-2}A_\alpha^4H_3\right)H_q.
\tag{2.4}
\]
On a slab \([t/2,t]\), (2.3) makes the last coefficient
\[
Cq^\sigma\left(r^{-2}+\frac{\Gamma_0^3}{t}\right).
\]
It is finite on that slab and polynomial in \(q\). Combined with the parabolic Sobolev recurrence
\[
q\longmapsto\frac{3q}{2},
\]
this has the expected endpoint
\[
\sup_{U_\alpha^-}aF(\cdot,t)
\leq
\frac{C_R\Gamma_0}{t}
\left(1+\frac t{r^2}\right)^\nu.
\tag{2.5}
\]
Indeed,
\[
H_q=\int a^{-2}(aF)^q,
\]
so the \(q\to\infty\) endpoint is precisely \(aF\), not \(a^{1/2}F\) or an unweighted curvature norm.

A complete proof still requires the temporal cutoffs, all nested spatial supports, polynomial \(q\)-dependence, and passage through \(a=0\). One convenient regularization is \(a_\varepsilon=a+\varepsilon\), using
\[
\frac{|da|^2}{a+\varepsilon}
=\frac{4a}{a+\varepsilon}|d\chi|^2
\leq4|d\chi|^2,
\]
followed by \(\varepsilon\downarrow0\).

---

## 3. Defect hierarchy and the velocity estimate

Define
\[
J_{m,\alpha,k}
=
\int\eta_{\alpha,k}^2a^{m-2}|E|^m\,d\mu_t,
\qquad
z_{m,\alpha,k}
=
\eta_{\alpha,k}a^{(m-1)/2}|E|^{m/2}.
\]
The \(E\)-equation is homogeneous in \(E\):
\[
\partial_tE
=
a\Delta_LE
+(\nabla a)*\nabla E
+(\nabla^2a)*E
+a\operatorname{Rm}*E
+aE*E
-2aE.
\]
After integrating the Hessian term by parts,
\[
\frac d{dt}J_{m,\alpha,k}
+c_m\int|\nabla z_{m,\alpha,k}|^2
\leq
Cm^2\left[
r^{-2}\sum_{\beta\in\mathcal N(\alpha)}J_{m,\beta,k-1}
+
\int\eta_{\alpha,k}^2a^{m-1}F|E|^m
\right].
\tag{3.1}
\]

The base exponent \(m=6\) is propagated directly by the critical \(L^2\) curvature input:
\[
\int Fz_6^2
\leq
\|F\|_2\|z_6\|_4^2
\leq
C\Gamma(t)\left(\int|\nabla z_6|^2+r^{-2}J_6\right).
\]
Thus
\[
J_{6,\alpha}(t)
\leq
C\sum_{\beta\in\mathcal N(\alpha)}J_{6,\beta}(0).
\tag{3.2}
\]
Initial pointwise pinching gives
\[
J_{6,\alpha}(0)\leq
\delta^6\operatorname{Vol}_{g_0}(U_\alpha^+).
\]

For higher exponents, the same cubic factorization as in (2.4) gives
\[
\int\eta^2a^{m-1}F|E|^m
\leq
\varepsilon\int|\nabla z_m|^2
+
C\left(r^{-2}+\varepsilon^{-2}A_\alpha^4H_3\right)J_m.
\tag{3.3}
\]
The nested recurrence \(m\mapsto3m/2\), started from (3.2), then has the endpoint
\[
\sup_{\{a>0\}}a|E|(\cdot,t)
\leq
C_E\delta
\left(1+\frac{r^2}{t}\right)^{1/3}.
\tag{3.4}
\]
The relative-Sobolev factor \(A_\alpha\sim rV_\alpha^{-1/4}\) cancels the factor
\[
J_6(0)^{1/6}\leq\delta V_\alpha^{1/6},
\]
so the constant is independent of collapsed volume.

Equation (3.4) controls the full flow velocity. Hence
\[
\left|\log\frac{g(t)(v,v)}{g_0(v,v)}\right|
\leq
2\int_0^t|aE|\,ds
\leq
C_E\delta r^2
\left[
\left(\frac t{r^2}\right)
+
\left(\frac t{r^2}\right)^{2/3}
\right].
\tag{3.5}
\]
No connection estimate enters.

---

## 4. Triangular unweighted defect system

Let \(\zeta_\alpha\) be fixed cutoffs such that
\[
c\leq\sum_\alpha\zeta_\alpha^2\leq C
\quad\text{on }\operatorname{supp}a,
\]
and define
\[
Q_\alpha(t)=\int\zeta_\alpha^2|E|^2\,d\mu_t.
\]
Testing the homogeneous \(E\)-equation gives
\[
\frac d{dt}Q_\alpha
+c\int\zeta_\alpha^2a|\nabla E|^2
\leq
Cr^{-2}\sum_{\beta\in\mathcal N(\alpha)}Q_\beta
+
C\int a|\operatorname{Rm}|\,|\zeta_\alpha E|^2.
\]
The curvature potential satisfies
\[
\begin{aligned}
\int a|\operatorname{Rm}|\,|\zeta_\alpha E|^2
&=
\int|\operatorname{Rm}|\,|\chi\zeta_\alpha E|^2\\
&\leq
\|\operatorname{Rm}\|_{L^2(U_\alpha^+)}
\|\chi\zeta_\alpha E\|_{L^4}^2,
\end{aligned}
\]
and is absorbed by the local critical smallness. Therefore
\[
\frac d{dt}Q_\alpha(t)
\leq
Cr^{-2}
\sum_{\beta\in\mathcal N(\alpha)}Q_\beta(t).
\tag{4.1}
\]
Summing and using the neighbor degree \(N\),
\[
\sum_\alpha Q_\alpha(t)
\leq
e^{CNt/r^2}
\sum_\alpha Q_\alpha(0).
\tag{4.2}
\]
Outside \(\operatorname{supp}a\), the metric is stationary. Hence
\[
\int_M|E(t)|^2\,d\mu_t
\leq
C e^{CNt/r^2}
\int_M|E(0)|^2\,d\mu_0.
\tag{4.3}
\]
This is an unnormalized support-total estimate. In particular, if a sequence has
\[
\frac{\int_M|E(0)|^2}{\mathcal A}\longrightarrow0
\]
for a topological scale \(\mathcal A\), then the same relation holds at every fixed \(t\leq\theta r^2\).

---

## 5. Exact first-exit closure

Fix a small metric tolerance \(\kappa_0\). Let \(T_*\) be the supremum of times \(T\leq\min\{T_{\max},\theta r^2\}\) on which:

1. **Metric equivalence**
   \[
   e^{-\kappa_0}g_0\leq g(t)\leq e^{\kappa_0}g_0.
   \]

2. **Local Sobolev control**
   \[
   A_\alpha(t)\leq2A_\alpha.
   \]

3. **Outer-star critical energy**
   \[
   \Gamma(t)\leq2\bar\gamma.
   \]

4. **Fixed-cutoff gradients**
   \[
   |d\chi|_{g(t)}\leq2L_\chi r^{-1},
   \qquad
   |d\eta_{\alpha,k}|_{g(t)}
   \leq2C2^kr^{-1}.
   \]

5. **Fixed-domain containment**, whenever moving balls are used:
   all inner moving balls remain inside their prescribed fixed outer domains.

6. **Weighted curvature**
   \[
   t\,\sup_{\{a>0\}}aF(t)\leq2C_R\bar\gamma.
   \]

7. **Weighted velocity**
   \[
   \sup_{\{a>0\}}
   \frac{a|E|(t)}
   {\delta(1+r^2/t)^{1/3}}
   \leq2C_E.
   \]

8. **Unweighted defect**
   \[
   \sum_\alpha Q_\alpha(t)
   \leq
   2e^{CNt/r^2}\sum_\alpha Q_\alpha(0).
   \]

Choose the parameters so that
\[
C(6)\bar\gamma<\frac18,
\qquad
e^{CN\theta}<\frac32,
\qquad
C_E\delta r^2(\theta+\theta^{2/3})
<\frac{\kappa_0}{4}.
\tag{5.1}
\]
Then the weak hierarchies give the same eight estimates with the factors \(2\) replaced by strictly smaller constants:

- \(H_2\) persistence improves the critical-energy bound;
- (2.3) and the high-\(q\) recurrence improve weighted curvature;
- (3.2)–(3.4) improve weighted velocity;
- (3.5) improves metric equivalence;
- metric equivalence transfers Sobolev inequalities and cutoff-gradient bounds;
- bilipschitz distance comparison improves fixed-domain containment;
- (4.2) improves the unweighted defect estimate.

Thus \(T_*\) can stop before \(\theta r^2\) only if the maximal smooth flow interval ends there. This reduces the final issue to smooth continuation.

---

## 6. Normalized smooth continuation

The needed extension statement is:

> **Normalized local-flow extension proposition.**  
> Let \(g(t)\), \(0\leq t<T<\infty\), solve
> \[
> \partial_tg=-2\chi^2(\operatorname{Ric}+g)
> \]
> smoothly on a closed manifold. If
> \[
> \sup_{M\times[0,T)}|\chi^2\operatorname{Rm}|<\infty,
> \]
> then \(g(t)\) extends smoothly beyond \(T\).

For a hypothetical \(T=T_{\max}>0\), estimate (2.5) gives a uniform bound on \([T/2,T)\); smoothness of the initial segment gives a bound on \([0,T/2]\). Hence the proposition applies.

Wang’s Theorem 4.1 proves the corresponding statement for
\[
\partial_tg=-2\chi^2\operatorname{Ric}.
\]
The normalized adaptation should use
\[
aE=\operatorname{contr}(a\operatorname{Rm})+ag
\]
and, for every \(m\),
\[
\nabla^m(aE)
=
\operatorname{contr}\bigl(\nabla^m(a\operatorname{Rm})\bigr)
+\nabla^m a*g
+\text{lower tensor contractions}.
\]
The coupled induction is then the same triangular structure used by Wang:

- \(L^p\) estimates for unweighted \(\nabla^m\operatorname{Rm}\);
- \(L^p\) estimates for \(\nabla^m(a\operatorname{Rm})\);
- evolution estimates for \(\nabla^{m+1}\chi\);
- Sobolev embedding to obtain all weighted curvature derivatives;
- integration of \(\partial_t\nabla^mg\) to a smooth time-\(T\) metric;
- restart through local Ricci–DeTurck theory.

The additional \(ag\) terms contribute fixed-cutoff derivatives and lower-order tensors. They do not alter the highest derivative structure. Importantly, evolving derivatives of \(a\) and the connection are derived inside this continuation proof; they are not assumed as first-exit quantities. Constants in this extension argument may depend on the individual initial smooth metric, since only extendibility—not a family-uniform derivative estimate—is required.

The exact source comparison is Wang, Section 4, especially Theorem 4.1 and Proposition 4.14, together with Deane Yang’s local Ricci-flow extension argument. The specific missing source-level computation is the same induction with \(aE\) replacing \(a\operatorname{Ric}\).

---

## 7. Remaining mathematical substance

The derivative-free route is therefore reduced to four precise pieces:

1. The tensor derivation of (2.1) and (3.1), including evolving measure, inverse-metric variation, finite-neighbor localization, and \(a\downarrow0\).

2. The complete parabolic recurrence based on (2.3)–(2.4), proving
   \[
   |a\operatorname{Rm}|\leq C\Gamma_0/t
   \]
   with constants independent of cutoff level and collapsed volume.

3. The corresponding recurrence from \(J_6\), proving the \(\delta\)-linear velocity estimate (3.4).

4. The normalized extension proposition above.

No pointwise \(\nabla\operatorname{Rm}\) term enters items 1–3. If one later asks for
\[
|\chi\nabla(aE)|,
\]
then differentiating produces
\[
\chi a\nabla\operatorname{Rm}*(aE),
\]
which is not controlled pointwise by \(H_3\), \(J_6\), \(|a\operatorname{Rm}|\), and \(Q\) alone. That is a separate derivative theorem, not part of this first-exit closure.