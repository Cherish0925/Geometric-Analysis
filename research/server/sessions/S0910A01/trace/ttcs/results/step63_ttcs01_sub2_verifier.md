# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step63_curvature_variation_index_proof.md",
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md"
  ]
}
```

## Task

Verify the index-level curvature variation and H_2 inequality derivation for the restricted 4D cutoff flow partial_t g = -2aE, a=chi^2, E=Ric+g, n=4, T=Rm+G, F_T=(1+|T|^2)^{1/2}, H=int eta^2 F_T^2 d mu.

The proof note claims to close Premise C1 from the Step 61 gate audit: the index-level tensor identities consumed by the curvature Moser endpoint. Check these items:

(1) PURE-SCALING CHECKSUM: For a=1, E=g (partial_t g = -2g), does the derivation give partial_t R_{ijkl} = -2R_{ijkl}? The connection contribution should vanish (nabla g = 0, nabla a = 0), and the metric-variation contribution h_{l alpha} R^alpha_{ijk} = -2g_{l alpha} R^alpha_{ijk} = -2R_{ijkl}. Check §3.4 and the checksum table in §9.

(2) CURVATURE VARIATION (3.11): partial_t R_{ijkl} = a Delta_L R + (nabla^2 a)*E + (nabla a)*(nabla E) + a Rm*E + a Q(Rm). Is this the correct general form? The Ricci part h_Ric = -2a Ric gives the Lichnerowicz Laplacian via Hamilton's formula; the conformal part h_conf = -2ag gives Hessian terms via (3.8). Check that every term carries at least one factor of a or a derivative of a (no a-free source).

(3) HESSIAN TENSOR B (Lemma 4.1): The Hessian terms from (4.2) and (4.3) contracted with 2T give 2(nabla^2 a) B where B is algebraic in E, g, T. The bound |nabla B| <= C F_T |nabla Rm| follows from nabla g = 0, nabla T = nabla Rm, and |nabla E| <= C|nabla Rm| (Bianchi). Is the Bianchi inequality |nabla Ric| <= C|nabla Rm| correct? Is the structural argument (B algebraic in E,g,T implies nabla B involves only nabla E, nabla T, nabla g) sound?

(4) H_2 INEQUALITY (8.2): H' + c_0 D_2 <= C_0 Y + C_H(1+r^{-2})H + C_V||aE||_inf H, where D_2 = int eta^2 a|nabla Rm|^2, Y = int eta^2 a F_T^3. The metric-drift term C_V||aE||_inf H is new (Premise C2). Check that it correctly accounts for the metric variation (5.2) and volume-form (6.3) contributions proportional to |E|.

(5) SIGNED IBP (§7): The Hessian term 2 int eta^2 (nabla^2 a) B is integrated by parts; the cutoff cross term vanishes (a=da=0 on supp d eta); the main term is absorbed by Young with |nabla a|^2/a <= Cr^{-2}. No higher cutoff jet appears. Is this consistent with Step 34 eq 2.8 and A03 Step 57 eq 5.4?

(6) NORMALIZATION BOOKKEEPING: For a=1, E=g: partial_t|T|^2 = -4|T|^2 + 8|T|^2 = +4|T|^2, partial_t(d mu) = -4 d mu, so partial_t int|Rm|^2 d mu = 0 in dim 4. The +4|T|^2 is absorbed into CaF_T^3. Is this consistent with the n=4 conformal invariance of int|Rm|^2 d mu?

Read the proof note at Sessions/S0910A01/workspace/notes/step63_curvature_variation_index_proof.md and the A03 Step 57 tensor calculation at Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md. Report any errors in the tensor calculations, sign errors, missing terms, or structural gaps.

## Output

## Scientific verification memo

I checked the Step 63 index-level derivation against A03 Step 57 and Step 34. The main analytic output,

\[
\frac{dH}{dt}+c_0D_2
\le C_0Y+C_H(1+r^{-2})H+C_V\|aE\|_\infty H,
\]

has the correct structure for the later Moser argument: the weighted dissipation is \(D_2=\int \eta^2a|\nabla\operatorname{Rm}|^2\), the cubic potential is \(Y=\int\eta^2aF_T^3\), the cutoff terms are controlled by \(|\nabla a|^2/a\le Cr^{-2}\), and the signed Hessian contribution is reduced to first cutoff derivatives by integration by parts. Those are the essential analytic ingredients.

At the same time, the note contains several concrete tensor-bookkeeping inaccuracies. They do not destroy the \(H_2\) inequality as an analytic estimate, because the omitted or mis-signed pieces remain algebraic Hessian terms of the same structural type. But they do prevent the note from being a finished index-level verification in the sense of “every tensor contraction written and sign-checked.”

---

### 1. Pure scaling of \(R_{ijkl}\)

For \(a\equiv1\), \(E=g\), i.e. \(\partial_t g=-2g\), the Riemann part is correct.

Because a constant rescaling does not change the Levi-Civita connection,

\[
\partial_t\Gamma^k_{ij}=0,
\qquad
\partial_t R^\alpha{}_{ijk}=0.
\]

Using

\[
R_{ijkl}=g_{l\alpha}R^\alpha{}_{ijk},
\]

one obtains

\[
\partial_t R_{ijkl}
=(\partial_t g_{l\alpha})R^\alpha{}_{ijk}
=-2g_{l\alpha}R^\alpha{}_{ijk}
=-2R_{ijkl}.
\]

Thus the \(R_{ijkl}\) entry in the checksum is correct.

However, the corresponding entries for \(T\), \(|T|^2\), and the shifted normalization are not consistent with the stated definition of \(G\).

The note defines

\[
G=\frac{1}{2(n-1)}(g\owedge g)
=\frac{1}{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}).
\]

For any symmetric \(h=\partial_t g\),

\[
\partial_t G=\frac{1}{n-1}(h\owedge g).
\]

If \(h=-2g\), then

\[
h\owedge g=-2(g\owedge g),
\]

so

\[
\partial_t G
=-\frac{2}{n-1}(g\owedge g)
=-4G,
\]

because \(G=\frac1{2(n-1)}g\owedge g\). The note writes \(\partial_tG=-2G\) in the pure-scaling checksum. That factor is off by two.

Consequently,

\[
\partial_t T=\partial_t\operatorname{Rm}+\partial_tG
=-2\operatorname{Rm}-4G,
\]

not \(-2T\). Therefore the table entry

\[
\partial_t T_{ijkl}=-2T_{ijkl}
\]

does not follow from the given definition of \(G\).

Likewise, the stated pure-scaling computation

\[
\partial_t|T|^2=-4|T|^2+8|T|^2=+4|T|^2
\]

assumes \(\partial_tT=-2T\). With the actual \(\partial_tG=-4G\), one obtains instead

\[
\partial_t|T|^2
=
4|\operatorname{Rm}|^2+4\langle \operatorname{Rm},G\rangle,
\]

not \(4|T|^2\). The difference is algebraic and can still be absorbed into the general \(CaF_T^3\) terms, but the displayed checksum for \(T\) is not correct as written.

The pure-scaling cancellation for \(\operatorname{Rm}\) alone,

\[
\partial_t|\operatorname{Rm}|^2=+4|\operatorname{Rm}|^2,
\qquad
\partial_t d\mu=-4d\mu,
\qquad
\frac d{dt}\int|\operatorname{Rm}|^2d\mu=0
\]

in dimension four, is correct.

---

### 2. Sign/contraction convention for \(\operatorname{Ric}(G)\)

The note states

\[
\operatorname{Ric}(G)=g.
\]

With the Ricci contraction as written,

\[
R_{jk}=g^{il}R_{ijkl},
\]

and

\[
G_{ijkl}=\frac{1}{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}),
\]

one computes

\[
g^{il}G_{ijkl}
=
\frac{1}{n-1}
\left(
g^{il}g_{ik}g_{jl}
-
g^{il}g_{il}g_{jk}
\right)
=
\frac{1}{n-1}
\left(
g_{jk}-ng_{jk}
\right)
=-g_{jk}.
\]

Thus, under the stated contraction, \(\operatorname{Ric}(G)=-g\), not \(+g\).

To obtain \(\operatorname{Ric}(G)=g\), one must either:

1. reverse the sign of \(G\), or  
2. use the other standard Ricci contraction, e.g. \(R_{jl}=g^{ik}R_{ijkl}\), or  
3. adjust the index ordering convention consistently.

This matters because the note uses \(\operatorname{Ric}(T)=E=\operatorname{Ric}+g\). If the sign or contraction is not corrected, that identity is not established as written. The analytic estimate can still be repaired because \(|E|\le C F_T\) remains true by algebraic comparison, but the tensor premise should be internally consistent.

---

### 3. General curvature variation formula

The schematic form

\[
\partial_t R_{ijkl}
=
a\Delta_L R_{ijkl}
+(\nabla^2 a)*E
+(\nabla a)*(\nabla E)
+a\,\operatorname{Rm}*E
+a\,Q(\operatorname{Rm})
\tag{3.11}
\]

is the right structural shape.

- The part \(h_{\rm Ric}=-2a\operatorname{Ric}\) gives the weighted Lichnerowicz principal term \(a\Delta_L\operatorname{Rm}\), first-derivative cutoff terms \((\nabla a)*\nabla\operatorname{Ric}\), Hessian cutoff terms \((\nabla^2a)*\operatorname{Ric}\), and algebraic curvature reactions.

- The conformal part \(h_{\rm conf}=-2ag\) gives Hessian terms of the form \((\nabla^2a)*g\) and the algebraic normalization term \(-2a\operatorname{Rm}\).

- The metric-variation contribution gives algebraic terms involving \(E*\operatorname{Rm}\).

- The shift \(G\) contributes only algebraic terms through \(\partial_tG=-\frac{2a}{n-1}(E\owedge g)\).

There is no \(a\)-free source term. Every term contains either \(a\), \(\nabla a\), or \(\nabla^2a\). That part is correct.

But several displayed index formulas need correction or completion.

#### 3.1 Conformal Hessian term

Under the convention stated in the note,

\[
\partial_t R^\ell{}_{ijk}
=
\nabla_i(\partial_t\Gamma^\ell{}_{jk})
-
\nabla_j(\partial_t\Gamma^\ell{}_{ik}),
\]

and for \(h_{\rm conf}=-2ag\),

\[
\partial_t\Gamma^\ell{}_{jk}
=
-(\nabla_j a)\delta^\ell_k
-(\nabla_k a)\delta^\ell_j
+(\nabla^\ell a)g_{jk}.
\]

Differentiating and antisymmetrizing gives, after lowering the \(\ell\)-index,

\[
\partial_t R^{\rm conf}_{ijkl}
=
-(\nabla_i\nabla_k a)g_{jl}
-(\nabla_j\nabla_l a)g_{ik}
+(\nabla_i\nabla_l a)g_{jk}
+(\nabla_j\nabla_k a)g_{il}.
\]

Equivalently, with the usual Kulkarni–Nomizu convention,

\[
\partial_t R^{\rm conf}_{ijkl}
=
-(\nabla^2a\owedge g)_{ijkl}.
\]

The note’s equation (3.8) writes

\[
-\frac12(\nabla^2a\owedge g)_{ijkl}.
\]

That coefficient is not consistent with the preceding formula and the standard Kulkarni–Nomizu normalization used in (1.1). Also, the intermediate display (3.7) omits the two terms containing \(g_{jk}\) and \(g_{ik}\). Those terms are needed for the \((k,l)\)-antisymmetry of the curvature tensor.

This discrepancy is not detected by the constant-\(a\) scaling checksum, because all Hessian terms vanish when \(a\) is constant. A variable-\(a\) test, for example a flat background metric with nonconstant \(a\), would test these signs and coefficients.

#### 3.2 Ricci-part Hessian terms

Using the same convention, the Hessian terms coming from \(h_{\rm Ric}=-2a\operatorname{Ric}\) are

\[
\partial_t R^{\rm Ric,hess}_{ijkl}
=
(\nabla_i\nabla_l a)R_{jk}
-
(\nabla_j\nabla_l a)R_{ik}
-
(\nabla_i\nabla_k a)R_{jl}
+
(\nabla_j\nabla_k a)R_{il}.
\]

The display (4.2) in the note has the opposite sign on the first two terms. If the curvature sign convention is reversed, then all such signs should be reversed consistently. As written, the signs in (4.2) are not the ones produced by (2.4).

Again, this does not change the analytic type of the term: it is still \((\nabla^2a)*\operatorname{Ric}\), and after contraction with \(T\) it contributes to a tensor \(B\) algebraic in curvature and metric. But for an index-level verification, the signs and coefficients must be exact.

#### 3.3 Quadratic \(\nabla a\) terms from the conformal part

The note says in §3.3 that there are “terms from \(\nabla\Gamma * \partial_t\Gamma\)” quadratic in \(\nabla a\). In the covariant variation formula

\[
\partial_t R^\ell{}_{ijk}
=
\nabla_i(\partial_t\Gamma^\ell{}_{jk})
-
\nabla_j(\partial_t\Gamma^\ell{}_{ik}),
\]

the conformal part \(h=-2ag\) produces only Hessian terms, because \(\nabla g=0\) and \(\nabla\delta=0\). There are no genuine \((\nabla a)^2\) terms in the linear variation of curvature under \(h=-2ag\). Such terms would be second order in the conformal factor in a finite conformal change, not part of the infinitesimal variation. This sentence should therefore be removed or clarified.

---

### 4. The Hessian tensor \(B\) and the bound \(|\nabla B|\le CF_T|\nabla\operatorname{Rm}|\)

The structural argument for \(B\) is sound, once \(B\) is indeed an algebraic contraction of \(E\), \(g\), and \(T\).

If

\[
B=B(E,g,T)
\]

algebraically, then

\[
\nabla B
=
(\nabla E)*T*E*g
+
E*(\nabla T)*g
+
E*T*(\nabla g).
\]

Since \(\nabla g=0\) and \(\nabla T=\nabla\operatorname{Rm}\) because \(\nabla G=0\), this becomes structurally

\[
|\nabla B|
\le
C\left(|\nabla E||T|+|E||\nabla\operatorname{Rm}|\right).
\]

The inequality

\[
|\nabla E|=|\nabla(\operatorname{Ric}+g)|
=
|\nabla\operatorname{Ric}|
\le
C|\nabla\operatorname{Rm}|
\]

is correct. It is essentially the fact that Ricci is a metric contraction of \(\operatorname{Rm}\); the contracted Bianchi identity is not needed for this pointwise inequality, though it is compatible with it.

Thus

\[
|\nabla B|
\le
C F_T|\nabla\operatorname{Rm}|
\]

is valid, and similarly

\[
|B|\le C|E||T|\le C F_T^2.
\]

This is the key input needed for the signed integration by parts.

However, the note does not display the full formula for \(B^{\alpha\beta}\). It gives the structural form and the bound. For the energy estimate that is enough. For the stated purpose of closing an index-level premise, an explicit symmetric tensor \(B^{\alpha\beta}\), including coefficients, should be written.

---

### 5. The \(H_2\) inequality and the metric-drift term

The passage from the pointwise inequality

\[
\partial_t F_T^2
\le
a\Delta F_T^2
-2a|\nabla\operatorname{Rm}|^2
+C|\nabla a||\nabla\operatorname{Rm}|F_T
+2(\nabla^2a)B
+CaF_T^3
\]

to the integrated inequality is analytically correct.

#### 5.1 Bochner and cutoff terms

Using

\[
\int \eta^2 a\Delta F_T^2
=
-\int \nabla(\eta^2a)\cdot\nabla F_T^2,
\]

the \(\nabla\eta\) piece vanishes on the buffered support because \(a=0\) on \(\operatorname{supp}(d\eta)\). The remaining \(\nabla a\) term is estimated by Young:

\[
|\nabla a\cdot \nabla F_T^2|
\le
\varepsilon a|\nabla T|^2
+
C_\varepsilon\frac{|\nabla a|^2}{a}F_T^2.
\]

Since

\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2\le Cr^{-2},
\]

this contributes

\[
\varepsilon D_2+C_\varepsilon r^{-2}H.
\]

The first-derivative curvature term

\[
C|\nabla a||\nabla\operatorname{Rm}|F_T
\]

is handled in the same way. This matches Step 34 and A03 Step 57.

#### 5.2 Signed Hessian integration by parts

The Hessian contribution is

\[
2\int \eta^2(\nabla_\alpha\nabla_\beta a)B^{\alpha\beta}\,d\mu.
\]

Integrating by parts once,

\[
2\int \eta^2(\nabla_\alpha\nabla_\beta a)B^{\alpha\beta}
=
-2\int (\nabla_\beta a)\nabla_\alpha(\eta^2B^{\alpha\beta}).
\]

The cutoff cross term is

\[
-4\int \eta(\nabla_\alpha\eta)(\nabla_\beta a)B^{\alpha\beta}.
\]

It vanishes because \(\nabla a=0\) on \(\operatorname{supp}(d\eta)\) in the buffered geometry.

The remaining term is bounded by

\[
C\int \eta^2|\nabla a||\nabla B|
\le
C\int \eta^2|\nabla a|F_T|\nabla\operatorname{Rm}|.
\]

Young gives

\[
C|\nabla a|F_T|\nabla\operatorname{Rm}|
\le
\varepsilon a|\nabla\operatorname{Rm}|^2
+
C_\varepsilon\frac{|\nabla a|^2}{a}F_T^2
\le
\varepsilon D_2
+
C_\varepsilon r^{-2}H.
\]

No \(\|\nabla^2\chi\|_\infty\) or higher cutoff jet enters the final estimate. This is consistent with Step 34 and A03 Step 57 equation (5.4).

#### 5.3 Metric-drift term

The metric-drift term

\[
C_V\|aE\|_\infty H
\]

correctly represents those zero-order metric and volume terms that contain a factor \(a|E|\).

The volume-form variation is

\[
\partial_t d\mu
=
-a\,\operatorname{tr}_g(E)\,d\mu.
\]

Since

\[
|\operatorname{tr}_g(E)|\le \sqrt n |E|,
\]

the volume contribution satisfies

\[
\left|
\int \eta^2F_T^2\partial_t d\mu
\right|
\le
C\int \eta^2 a|E|F_T^2
\le
C\|aE\|_\infty H.
\]

The metric variation of the norm gives terms of the form

\[
Ca|E||T|^2,
\]

and these also satisfy

\[
\int \eta^2 a|E||T|^2
\le
\|aE\|_\infty H.
\]

Thus the separate term \(C_V\|aE\|_\infty H\) is a valid refinement of the more schematic absorption into \(Y\). A03 Step 57 absorbs these terms into \(C\int\eta^2aF_T^3\) using \(|E|\le CF_T\). Both treatments are compatible; Step 63 simply keeps the \(L^\infty\) coefficient explicit, which is useful for coupling to the defect estimate.

One minor numerical point: in the pure-scaling table, for \(E=g\) one has \(|E|=\sqrt n\), not \(1\). This is harmless because the constant \(C_V\) absorbs it, but the table should either say “schematic unit size” or use \(\sqrt n\).

---

### 6. Normalization bookkeeping and four-dimensional cancellation

For \(\operatorname{Rm}\) alone, the four-dimensional scaling cancellation is correct:

\[
\partial_t|\operatorname{Rm}|^2=+4|\operatorname{Rm}|^2,
\qquad
\partial_t d\mu=-4d\mu,
\]

so

\[
\frac d{dt}\int|\operatorname{Rm}|^2d\mu=0.
\]

This is a constant-scaling cancellation. It should not be described as full local conformal invariance of \(\int|\operatorname{Rm}|^2d\mu\) under arbitrary nonconstant conformal changes. The nonconstant part produces precisely the Hessian cutoff terms. A03 Step 57 states this distinction correctly.

For the shifted tensor \(T=\operatorname{Rm}+G\), the same homogeneous cancellation does not hold, because \(G\) is quadratic in \(g\) and scales differently. With the given definition of \(G\),

\[
\partial_tG=-4G
\]

under \(\partial_tg=-2g\), not \(-2G\). Therefore the shifted pure-scaling checksum should be rewritten. The extra algebraic pieces are still controlled by the general reaction terms in the \(H_2\) inequality, but the current table gives the wrong normalization bookkeeping for \(T\).

---

### 7. Consistency with A03 Step 57 and Step 34

The energy inequality itself is consistent with the earlier analytic structure.

- Step 34 requires a pointwise inequality of the form

  \[
  \partial_tF^2
  \le
  a\Delta F^2
  -2a|\nabla\operatorname{Rm}|^2
  +C|\nabla a|F|\nabla\operatorname{Rm}|
  +\Sigma_H
  +CaF^3,
  \]

  with \(\Sigma_H\) a signed Hessian contraction. Step 63 supplies this structure for \(F_T\).

- A03 Step 57 derives the same \(H_2\) structure without the explicit drift term:

  \[
  H_2'+(2-\delta_0)D_2
  \le
  C_1\int\eta^2aF_T^3
  +
  C_2(1+r^{-2})H_2.
  \]

  Step 63’s additional \(C_V\|aE\|_\infty H\) term is compatible with this; it is a more explicit accounting of the same zero-order metric and volume contributions.

- The signed Hessian integration by parts in Step 63 agrees with A03 Step 57 equation (5.4): both reduce the Hessian term to

  \[
  \varepsilon D_2+C_\varepsilon r^{-2}H_2
  \]

  using only \(|\nabla\chi|\le Cr^{-1}\).

The main cross-note discrepancy is in the coefficient/sign of the Hessian term. A03 Step 57 writes Type (C) schematically as \((\nabla^2a)\owedge E\), while Step 63 writes the conformal piece as \(-\frac12(\nabla^2a)\owedge g\). Under the conventions as written in Step 63, the conformal piece should be \(-(\nabla^2a)\owedge g\), without the extra \(1/2\). If the opposite curvature sign convention is adopted, the sign should be reversed consistently throughout. Since the Hessian term is later estimated by absolute value, this does not change the \(H_2\) inequality, but it must be unified for an index-level proof.

---

### 8. Net scientific assessment

The analytic core is solid:

\[
\boxed{
\frac{dH}{dt}+c_0D_2
\le
C_0Y+C_H(1+r^{-2})H+C_V\|aE\|_\infty H
}
\]

is the right form for the curvature Moser input, and the signed Hessian mechanism is correctly implemented. The bound

\[
|\nabla B|\le CF_T|\nabla\operatorname{Rm}|
\]

is structurally sound. The metric-drift term correctly represents the zero-order metric and volume contributions proportional to \(aE\).

The tensor-bookkeeping items that need correction are:

1. **Ricci contraction/sign for \(G\).** As written, \(g^{il}G_{ijkl}=-g_{jk}\). To have \(\operatorname{Ric}(G)=g\), fix the sign of \(G\) or the Ricci contraction.

2. **Scaling of \(G\).** With \(G=\frac1{2(n-1)}g\owedge g\), pure scaling gives \(\partial_tG=-4G\), not \(-2G\). The \(T\)-scaling checksum and the \(|T|^2\) table entry should be rewritten.

3. **Conformal Hessian coefficient.** Under the stated curvature convention, the conformal Hessian variation is \(-(\nabla^2a)\owedge g\), not \(-\frac12(\nabla^2a)\owedge g\), and the intermediate display should include all four terms.

4. **Ricci-part Hessian signs.** The signs in (4.2) should be re-derived against the stated convention (2.4); as written, the first two signs appear reversed.

5. **Explicit \(B\).** The structural bound is enough for the estimate, but a complete index-level record should display \(B^{\alpha\beta}\) explicitly.

6. **Pure-scaling checksum coverage.** The constant-\(a\) checksum verifies the normalization of the \(\operatorname{Rm}\) part but does not verify Hessian signs or coefficients. A variable-\(a\) local test is needed for those terms.

After those corrections, the Step 63 derivation provides the analytic tensor input needed by the curvature Moser endpoint. The remaining mathematical substance not addressed by this tensor calculation includes existence and continuation of the degenerate cutoff flow and the downstream selection/common-time construction.