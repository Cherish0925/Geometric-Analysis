# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 38,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step38_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step38_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the conditional K2–Y–Moser smoothing layer in the Step 38 note against A01's fixed-exponent and index-level notes and A03's restored state. Check exact Sobolev convention, weights, q=2 absorption, q=3 good-slice propagation, the coefficient S^2Y on dyadic slabs, the p→3p/2 spacetime recurrence, and endpoint scalings ||aF||∞≲γ/t and ||aE||∞≲δ(r²/t)^(1/3). Determine which estimates are genuinely established conditional PDE lemmas and which still depend on unproved moving first-exit, regularized defect general-p, or continuation inputs. Pay special attention to whether the defect high-p inequality follows from the fixed unregularized J6 lemma, and whether any additive regularization source would destroy the δ scaling.

## Integrated Scientific Memo

## Verification memo: Step 38 conditional \(K_2\)–\(Y\)–Moser smoothing layer

The Step 38 smoothing layer is substantially correct as a **conditional PDE module on a smooth first-exit interval**, with the important qualification that the defect \(L^\infty\) endpoint still depends on an unproved **general-\(p\)** defect power inequality. The curvature chain is now supported at fixed and high exponent by A01 Step 34–35 and A03 Step 34/38. The fixed \(J_6\) defect seed is supported by A03 Step 35 and A01 Step 35, but it does not by itself imply the full defect Moser ladder.

Below is the precise status of each requested point.

---

### 1. Sobolev convention and collapse scaling

The correct four-dimensional Sobolev convention is the squared one:
\[
\|u\|_4^2\le \mathcal S(t)\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),
\qquad 
\mathcal S\simeq \frac{r^2}{\sqrt V}.
\]
Thus the critical absorption parameter is
\[
\gamma(t)=\mathcal S(t)\,K_2(t)^{1/2},
\qquad 
K_2(t)=\int_{U}\eta^2 F^2\,d\mu_t.
\]
At a good support,
\[
K_2(0)\le K_0V
\quad\Longrightarrow\quad
\gamma(0)\lesssim \frac{r^2}{\sqrt V}\sqrt{K_0V}
=Cr^2\sqrt{K_0},
\]
so the collapsed volume cancels. This agrees with A03 Step 34, A01 Step 32, and A01 Step 34. The high-exponent curvature potential coefficient is
\[
\boxed{\mathcal S^2Y},\qquad Y=\int\eta^2aF^3,
\]
not an additional Sobolev square. If an unsquared embedding constant \(S\) is used, then \(S^2=\mathcal S\), so the same coefficient would be \(S^4Y\). Step 38 uses the correct convention.

One localization nuance: the \(K_2\) used for \(\gamma\) must be the localized auxiliary-support quantity
\[
K_2^\eta=\int_U\eta^2F^2,
\]
not a global \(\int F^2\). Step 38’s component notation \(K_{2,j}=\int_{U_j}\eta_j^2F^2\) is consistent with this.

---

### 2. \(q=2\) absorption: established conditional lemma

The supported \(q=2\) curvature energy inequality is
\[
K_2'+cD_2\le CY+C(r^{-2}+1)K_2,
\]
with
\[
D_2=\int\eta^2a|\nabla\operatorname{Rm}|^2,
\qquad
Y=\int\eta^2aF^3.
\]
For \(v=\chi F\),
\[
Y=\int Fv^2
\le \|F\|_{L^2(\operatorname{supp}a)}\|v\|_4^2
\le C\gamma(D_2+r^{-2}K_2).
\]
Here \(\eta=1\) on \(\operatorname{supp}a\), and
\[
|\nabla(\chi F)|^2\le C a|\nabla F|^2+C|\nabla\chi|^2F^2
\le C a|\nabla\operatorname{Rm}|^2+Cr^{-2}F^2.
\]
If \(C\gamma\le c/2\), then
\[
K_2'+\frac c2D_2\le C(r^{-2}+1)K_2.
\]
For \(t\lesssim \min\{r^2,1\}\), or with the factor \(e^{C(r^{-2}+1)t}\) retained,
\[
\sup_{s\le t}K_2(s)+\int_0^tD_2(s)\,ds
\le CK_2(0),
\]
and hence
\[
\boxed{\int_0^tY(s)\,ds\le C\gamma K_2(0).}
\]

This is a genuine conditional PDE lemma once the \(q=2\) tensor energy inequality is available. A01 Step 35 supplies the needed index-level curvature Hessian-\(a\) tensor
\[
B_{\rm curv}^{pq}=R^p{}_j{}^q{}_lE^{jl},
\]
with
\[
|B_{\rm curv}|\le CF^2,
\qquad
|\nabla B_{\rm curv}|\le CF|\nabla\operatorname{Rm}|.
\]
The signed tensor IBP, rather than a pointwise evolving Hessian bound for \(a\), controls the Hessian-\(a\) terms.

---

### 3. \(q=3\) good-slice propagation and dyadic coefficient \(\mathcal S^2Y\)

The fixed \(q=3\) inequality is
\[
Y'+cD_3\le C(r^{-2}+1)Y+C\int\eta^2a^2F^4,
\]
where
\[
D_3=\int\eta^2a^2F|\nabla\operatorname{Rm}|^2.
\]
With \(u=aF^{3/2}\),
\[
\int a^2F^4=\int Fu^2
\le \|F\|_{L^2(\operatorname{supp}a)}\|u\|_4^2
\le C\gamma(D_3+r^{-2}Y).
\]
Indeed,
\[
|\nabla(aF^{3/2})|^2
\le C a^2F|\nabla F|^2+C|da|^2F^3
\le C D_3+Cr^{-2}Y.
\]
For \(C\gamma\) small,
\[
Y'\le C(r^{-2}+1)Y.
\]

Combining this with the spacetime estimate \(\int_0^tY\le C\gamma K_2(0)\), choose a good slice \(\tau\in[t/4,t/2]\) such that
\[
Y(\tau)\le \frac{C\gamma K_2(0)}{t}.
\]
Forward propagation gives
\[
\boxed{
Y(t)\le \frac{C\gamma K_2(0)}{t}.}
\]
Therefore, under first-exit comparability of \(\mathcal S(t)\) and \(K_2(t)\),
\[
\boxed{
\mathcal S(t)^2Y(t)\le \frac{C\gamma^3}{t}.}
\]

This is the correct **pointwise dyadic slab coefficient** for high-\(p\) Moser. The time average
\[
\int_{t/2}^t\mathcal S^2Y
\]
is not by itself enough to control \(\int(\mathcal S^2Y)K_p\), because \(\mathcal S^2Y\) could correlate with \(K_p\). Step 38 correctly uses the pointwise dyadic bound.

A01 Step 34 also records an equivalent route through
\[
Y'\le C(r^{-2}+1+\mathcal S^2Y)Y
\]
and
\[
\int_0^t\mathcal S^2Y\le C\gamma^3.
\]
This is compatible with the direct \(q=3\) absorption formulation.

---

### 4. General curvature power inequality: established conditional lemma

A01 Step 35 resolves the earlier A01 Step 33 defects and establishes the index-level curvature power inequality
\[
\boxed{
K_p'
+c\{pD_p^{\rm Rm}+p(p-2)D_p^F\}
\le Cp^N(r^{-2}+1+\mathcal S^2Y)K_p,
\qquad p\ge3.
}
\]
Here
\[
D_p^{\rm Rm}=\int\eta^2a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2,
\]
\[
D_p^F=\int\eta^2a^{p-1}F^{p-2}|\nabla F|^2.
\]
The coefficient \(p(p-2)\), not the older \(p(p-3)\), is the corrected one. Keeping both dissipations is essential:

- \(\nabla B_{\rm curv}\) is paid by \(D_p^{\rm Rm}\);
- derivatives of \(F^{p-2}\) are paid by \(D_p^F\).

The Hessian-\(a\) term is controlled by signed tensor IBP:
\[
\int a^{p-2}F^{p-2}(\nabla_i\nabla_ja)B_{\rm curv}^{ij}
=
-\int \nabla_ja\,\nabla_i(a^{p-2}F^{p-2}B_{\rm curv}^{ij}),
\]
and the derivative-structure bound \(|\nabla B_{\rm curv}|\le CF|\nabla\operatorname{Rm}|\) is exactly what prevents loss.

Thus Step 38’s curvature high-\(p\) input is genuinely established, conditional on the smooth first-exit geometry.

---

### 5. \(p\mapsto3p/2\) spacetime recurrence: algebraically correct

For either \(f=F\) or \(f=|E|\), define
\[
H_p(f)=\int\eta^2a^{p-2}f^p,
\qquad
z_p=\eta a^{(p-1)/2}f^{p/2}.
\]
The mixed interpolation is
\[
\boxed{
H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2.
}
\]
The weight identity is
\[
\frac{p-2}{2}+(p-1)=\frac{3p}{2}-2,
\]
and the \(f\)-power is
\[
\frac p2+p=\frac{3p}{2}.
\]

On nested dyadic time slabs \(I_{k+1}\Subset I_k\subset[t/2,t]\), with
\[
p_{k+1}=\frac32p_k,
\]
the energy recurrence has the form
\[
\int_{I_{k+1}}H_{p_{k+1}}
\le C p_k^N\mathcal S
\bigl(L_k\int_{I_k}H_{p_k}\bigr)^{3/2},
\]
where
\[
L_k\lesssim p_k^N\left(\frac{4^k}{t}+r^{-2}+1+\operatorname*{ess\,sup}_{I_k}\mathcal S^2Y\right).
\]
Using
\[
\operatorname*{ess\,sup}_{I_k}\mathcal S^2Y\lesssim \frac{\gamma^3}{t},
\]
and \(\gamma\) small, one obtains for \(t\lesssim\min\{r^2,1\}\)
\[
L_k\lesssim p_k^N4^kt^{-1}.
\]
The Moser product converges because
\[
p_k=p_0(3/2)^k,
\qquad
\sum_k\frac1{p_k}<\infty,
\qquad
\sum_k\frac{k+\log p_k}{p_k}<\infty.
\]
The endpoint is
\[
\boxed{
\|af(t)\|_\infty
\le C\mathcal S^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^tH_{p_0}(f,s)\,ds\right)^{1/p_0}.
}
\]
Without the short-time simplification, replace \(t^{-3/p_0}\) by
\[
(t^{-1}+r^{-2}+1)^{3/p_0}.
\]

This recurrence is established algebraically and matches A01 Step 32, A03 Step 34, A03 Step 25, and Step 38.

---

### 6. Curvature endpoint \(\|aF\|_\infty\lesssim \gamma/t\): conditional PDE consequence

For curvature, take \(p_0=3\). Since
\[
\int_{t/2}^tY(s)\,ds\le C\gamma K_2(0),
\]
the recurrence gives
\[
\|aF(t)\|_\infty
\le C\mathcal S^{2/3}t^{-1}(\gamma K_2(0))^{1/3}.
\]
Using \(\gamma=\mathcal S K_2(0)^{1/2}\), equivalently \(K_2(0)=\gamma^2/\mathcal S^2\) up to first-exit comparability,
\[
\mathcal S^{2/3}(\gamma K_2(0))^{1/3}
\sim
\mathcal S^{2/3}\gamma^{1/3}(\gamma^2\mathcal S^{-2})^{1/3}
=\gamma.
\]
Therefore
\[
\boxed{
\|aF(t)\|_\infty\le \frac{C\gamma}{t}.
}
\]
This is a genuine conditional curvature smoothing estimate, assuming the smooth first-exit interval and the already-established curvature tensor inequalities.

It is singular like \(t^{-1}\) near \(0\), so it is **not** the metric-drift control. Metric drift must come from the defect estimate.

---

### 7. Fixed \(J_6\) persistence: established conditional lemma

A03 Step 35 and A01 Step 35 support the unregularized defect \(J_6\) estimate. Let
\[
s=|E|^2,
\qquad
J_6=\int\eta^2a^4s^3,
\qquad
X_6=\int\eta^2a^5s^2|\nabla E|^2,
\]
and
\[
P_6=\int\eta^2a^5Fs^3.
\]
The defect Hessian-\(a\) contraction tensor is
\[
B_{\rm def}^{pq}=s g^{pq}+(\operatorname{tr}E)E^{pq}-2(E^2)^{pq},
\]
with
\[
B_{\rm def}|_{E=0}=0,
\qquad
|B_{\rm def}|\le Cs,
\qquad
|\nabla B_{\rm def}|\le Cs^{1/2}|\nabla E|.
\]
Thus the Hessian-\(a\) contribution is homogeneous in \(E\) and is controlled by signed IBP:
\[
|T_H^E|\le \varepsilon X_6+C_\varepsilon r^{-2}J_6.
\]
The chain rule for \(s^3\) gives
\[
(\partial_t-a\Delta)s^3
=
3s^2(\partial_t-a\Delta)s
-6as|\nabla s|^2,
\]
and the last term is nonpositive. The resulting differential inequality is
\[
\boxed{
J_6'+cX_6\le C(1+r^{-2})J_6+CP_6.
}
\]

For
\[
w_6=\eta a^{5/2}s^{3/2}=\eta\chi^5|E|^3,
\]
one has
\[
P_6=\int Fw_6^2
\le \|F\|_2\|w_6\|_4^2
\le C\gamma(X_6+r^{-2}J_6).
\]
If \(C\gamma<c/2\), then
\[
\boxed{
J_6'+c'X_6\le C(1+r^{-2})J_6,
}
\]
so
\[
\boxed{
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).
}
\]
With initial \(\|E(0)\|_\infty\le\delta\) on the support,
\[
J_6(0)\le C\delta^6V,
\]
and for \(t\le \theta r^2\),
\[
\boxed{
J_6(t)\le C\delta^6V.
}
\]

This is a solid conditional fixed-exponent lemma. It does not use \(Y\), does not use the curvature \(L^\infty\) endpoint, and avoids any Kato regularization source.

Minor correction: A03 Step 35 §3.6a displays \(s^{3/2}\) in one first-derivative cutoff term, but the surrounding calculation and A01 Step 34 identify the correct power as
\[
a^4|da|s^{5/2}|\nabla E|.
\]
The final estimate is unaffected.

---

### 8. Defect high-\(p\) inequality: not yet established

This is the main unresolved point.

Step 38 assumes, for \(f=|E|\),
\[
\boxed{
H_p'(f)+c\|\nabla z_p\|_2^2
\le Cp^N(r^{-2}+1+\mathcal S^2Y)H_p(f),
}
\]
with no curvature-only additive source. This is exactly the right input for the defect Moser iteration, but it is **not proved** by the fixed \(J_6\) lemma.

The Moser ladder from \(p_0=6\) uses
\[
p_k=6(3/2)^k=6,9,13.5,\dots.
\]
The fixed \(J_6\) persistence only supplies the initial spacetime seed
\[
\int_{t/2}^tJ_6(s)\,ds\le Ct\delta^6V.
\]
It does not supply the differential inequalities at \(p=9,13.5,\ldots\).

The most plausible way to prove the missing general-\(p\) inequality is to avoid norm regularization and work with
\[
s=|E|^2,
\qquad
H_p^E=\int\eta^2a^{p-2}s^{p/2},
\qquad
z_p^E=\eta a^{(p-1)/2}s^{p/4}.
\]
For the Moser ladder, \(p\ge6\), so \(q=p/2\ge3\). The chain rule
\[
(\partial_t-a\Delta)s^q
=
q s^{q-1}(\partial_t-a\Delta)s
-aq(q-1)s^{q-2}|\nabla s|^2
\]
has no singularity at \(s=0\), and the last term is favorable. The already-derived tensor
\[
B_{\rm def}^{pq}=s g^{pq}+(\operatorname{tr}E)E^{pq}-2(E^2)^{pq}
\]
has the right homogeneous bounds for every such \(q\):
\[
|B_{\rm def}|\le Cs,
\qquad
|\nabla B_{\rm def}|\le Cs^{1/2}|\nabla E|.
\]
The reaction term should be estimated by
\[
a^{p-1}F|E|^p
=
(aF^3)^{1/3}
(a^{p-2}|E|^p)^{1/3}
(z_p^E)^{4/3},
\]
which yields the same \(\mathcal S^2Y\) coefficient after Hölder, Sobolev, and Young.

However, the supplied notes do not yet write this general-\(p\) defect derivation term-by-term, including first cutoff derivatives, Hessian-\(a\) IBP, measure variation, and moving tensor norms. Therefore Step 38’s defect high-\(p\) inequality remains an **assumption**, albeit a structurally well-motivated one.

---

### 9. Additive regularization sources and \(\delta\)-scaling

An additive source independent of \(E\) would destroy the desired \(\delta\)-linear defect endpoint.

If a regularized defect inequality had the form
\[
J_{p,\varepsilon}'\le L_pJ_{p,\varepsilon}+A_{p,\varepsilon},
\]
and \(A_{p,\varepsilon}\) left a nonzero \(\delta\)-independent limit as \(\varepsilon\to0\), then even at \(p=6\)
\[
J_6(t)\lesssim \delta^6V+\int_0^tA_6(s)\,ds.
\]
The Moser endpoint would then contain a term not proportional to \(\delta\), so
\[
\|aE(t)\|_\infty\lesssim \delta(r^2/t)^{1/3}
\]
would fail.

The exact defect equation strongly suggests no such source should exist: \(E=0\) is preserved by the flow, and the Hessian tensor satisfies \(B_{\rm def}|_{E=0}=0\). Every source term in the \(s=|E|^2\) equation carries either \(s\), \(|E||\nabla E|\), or \(|\nabla E|^2\). Thus any regularization source should vanish as \(\varepsilon\to0\). But unless this is proved uniformly through the full Moser ladder, the regularized route is unsafe.

The cleanest resolution is the unregularized \(s^{p/2}\) derivation for all \(p_k\ge6\), avoiding additive regularization sources entirely.

---

### 10. Defect endpoint scaling: correct but conditional on missing high-\(p\) input

Assuming the general-\(p\) defect inequality, take \(p_0=6\). From \(J_6(s)\le C\delta^6V\),
\[
\int_{t/2}^tH_6^E(s)\,ds
\le Ct\delta^6V.
\]
The Moser endpoint gives
\[
\|aE(t)\|_\infty
\le C\mathcal S^{1/3}t^{-1/2}(t\delta^6V)^{1/6}.
\]
Using \(\mathcal S\lesssim r^2V^{-1/2}\),
\[
\mathcal S^{1/3}V^{1/6}
\lesssim (r^2V^{-1/2})^{1/3}V^{1/6}
=r^{2/3}.
\]
Therefore
\[
\boxed{
\|aE(t)\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^{1/3}.
}
\]
Its time integral is
\[
\boxed{
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta\theta^{2/3}r^2.
}
\]
This is the desired integrable metric-drift scale for \(\partial_tg=-2aE\), but it remains conditional on the unproved general-\(p\) defect inequality and the first-exit geometry.

---

### 11. Signed Hessian-cutoff repair and continuation status

Step 38’s signed Hessian lemma is correct:
\[
J=\int \chi\,\nabla_i\nabla_j\chi\,B^{ij}(V)
\]
with
\[
|B(V)|\le C_p|V|^p,
\qquad
|\nabla B(V)|\le C_p|V|^{p-1}|\nabla V|
\]
gives
\[
J
=
-\int\nabla_i\chi\nabla_j\chi B^{ij}
-\int\chi\nabla_j\chi\nabla_iB^{ij},
\]
and hence
\[
|J|
\le \varepsilon\int\chi^2|\nabla V|^2|V|^{p-2}
+C_{p,\varepsilon}\|\nabla\chi\|_\infty^2\int |V|^p.
\]
This uses no division by \(a\), no \(\chi^2/a\), and no pointwise evolving \(\nabla^2\chi\) bound.

For \(m=2\), Step 38 correctly applies this to the signed term
\[
\chi\nabla^2\chi*\nabla^2U
\]
tested against \(|\nabla^2U|^{p-2}\nabla^2U\). Thus the previous apparent obstruction
\[
\int\chi|\nabla^2\chi||\nabla^2U|^p
\]
was an artifact of taking absolute values before exploiting tensor placement.

But this does not prove full smooth continuation. Step 38 correctly identifies the remaining higher-order issue: for general \(m\), top cutoff jets couple to lower differentiated curvature factors, e.g.
\[
\chi\nabla^{m+1}\chi*\nabla U*|\nabla^mU|^{p-2}\nabla^mU,
\]
and after IBP derivatives may fall on \(\nabla U\), metric contractions, or commutators. A complete continuation theorem still needs a finite-exponent induction for \((\nabla^mU,\nabla^{m+1}\chi)\) and lower unweighted \(T\)-moments. That induction is not present in the supplied materials.

---

## Final classification

### Established conditional PDE lemmas

On a smooth first-exit interval with fixed buffered supports, moving Sobolev comparability, metric comparability, and \(\gamma\) small:

1. Correct Sobolev convention:
   \[
   \|u\|_4^2\le\mathcal S(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2),
   \qquad
   \gamma=\mathcal SK_2^{1/2}.
   \]

2. \(q=2\) curvature absorption:
   \[
   \sup K_2+\int D_2\le CK_2(0),
   \qquad
   \int_0^tY\le C\gamma K_2(0).
   \]

3. \(q=3\) good-slice propagation:
   \[
   Y(t)\le \frac{C\gamma K_2(0)}t,
   \qquad
   \mathcal S^2Y(t)\le \frac{C\gamma^3}{t}.
   \]

4. General-\(p\) curvature power inequality:
   \[
   K_p'+c\{pD_p^{\rm Rm}+p(p-2)D_p^F\}
   \le Cp^N(r^{-2}+1+\mathcal S^2Y)K_p.
   \]

5. Weighted Moser recurrence:
   \[
   \|af(t)\|_\infty
   \le C\mathcal S^{2/p_0}t^{-3/p_0}
   \left(\int_{t/2}^tH_{p_0}(f,s)\,ds\right)^{1/p_0},
   \]
   with \(t^{-3/p_0}\) replaced by \((t^{-1}+r^{-2}+1)^{3/p_0}\) outside the short-time simplification.

6. Curvature endpoint:
   \[
   \|aF(t)\|_\infty\le C\gamma/t.
   \]

7. Unregularized fixed \(J_6\) persistence:
   \[
   J_6(t)\le e^{C(1+r^{-2})t}J_6(0)\le C\delta^6V.
   \]

8. Signed Hessian-cutoff repair for the \(m=2\) shifted-curvature term.

### Correct but still conditional on unproved input

1. Defect endpoint:
   \[
   \|aE(t)\|_\infty
   \le C\delta(r^2/t)^{1/3}.
   \]
   The scaling algebra is correct, but it requires the general-\(p\) defect inequality for \(p=6(3/2)^k\), not merely fixed \(J_6\).

2. Metric drift:
   \[
   \int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
   \le C\delta\theta^{2/3}r^2.
   \]
   This depends on the previous defect endpoint.

### Still unproved inputs

1. General-\(p\) unregularized defect power inequality with no additive \(E\)-independent source:
   \[
   (H_p^E)'+c\|\nabla z_p^E\|_2^2
   \le Cp^N(r^{-2}+1+\mathcal S^2Y)H_p^E.
   \]

2. Simultaneous moving first-exit bootstrap controlling:
   \[
   \mathcal S(t),\quad K_2(t),\quad J_6(t),\quad \gamma(t),\quad
   \text{metric comparison},\quad \text{support/buffer geometry}.
   \]

3. Degenerate cutoff-flow existence and continuation to the target time.

4. Higher-order shifted-curvature/cutoff-jet induction beyond the repaired \(m=2\) single-Hessian term.

5. Terminal geometric passage and any connection to the full Yau Problem 26 statement.

---

### Bottom line

Step 38’s curvature \(K_2\to Y\to \|aF\|_\infty\) chain is a valid conditional PDE smoothing module. The coefficient \(\mathcal S^2Y\), the \(q=2\) absorption, the \(q=3\) good-slice propagation, the \(p\mapsto3p/2\) recurrence, and the curvature endpoint
\[
\|aF\|_\infty\lesssim \gamma/t
\]
are all consistent with the fixed-exponent and index-level notes.

The fixed unregularized \(J_6\) lemma is also established and preserves the \(\delta^6\) seed without regularization. But it does **not** imply the defect high-\(p\) Moser inequalities. Therefore the endpoint
\[
\|aE\|_\infty\lesssim \delta(r^2/t)^{1/3}
\]
is conditionally correct only after proving the missing general-\(p\) homogeneous defect inequality. Any additive regularization source surviving the \(\varepsilon\to0\) limit would break the \(\delta\)-scaling, so the safest completion is an unregularized \(s=|E|^2\), \(s^{p/2}\)-based derivation for the whole Moser ladder.