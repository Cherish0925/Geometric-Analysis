# TTCS Independent Branch Record

```json
{
  "step_id": 61,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 3,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A01/workspace/notes/step60_base_pair_proof.md",
    "Sessions/S0910A01/workspace/notes/step59_induction_ledger_repair.md"
  ]
}
```

## Task

Audit the per-datum existence construction (A03 Step 56, tame_direct_flow_repair) for the transported-cutoff DeTurck system ∂_t G = β²[G^{-1}D²G+R+Q-2G]+2sym(d(β²)⊗W), ∂_t β = β²W·Dβ, with regularization (β²+ε) and νΔβ. The claim is: a smooth per-datum solution exists on [0,T₀] with T₀ depending on high Sobolev norms of the initial data. Test for gaps: (1) The tame energy estimate (Prop 3.1, eq 3.2): d/dt E_m + cD_m ≤ C_{m,R}(1+E_m). Is the constant C_{m,R} really independent of ε,ν? Check the absorption in §3.3 (Lie cross term, eq 3.9-3.10): the top term ∫D^mG*βD^{m+1}β*W is integrated by parts to get -∫βD^{m+1}G*D^mβ*W. This works only if W=O(1) in L∞, which requires the low norm bound (2.2). Is the low bound (2.2) maintained for the whole construction, or is it a bootstrap that could fail? (2) The maximum principle for β (eq 1.3): at a spatial extremum of β, the transport term β²W·Dβ vanishes (Dβ=0), and νΔ̄β has the right sign at a max/min. Verify this is correct and gives 0≤β≤1. (3) The smooth limit (§5): from uniform E_m bounds for all m and ∂_t bounds, extract a diagonal sequence converging in every C^k. Verify the regularized terms ε[G^{-1}D²G+R+Q] and νΔ̄β vanish in C^k. (4) The pullback (5.3-5.4): verify that φ solving ∂_tφ=-β²W(G) gives β(t,φ(t,x))=χ(x) and g=φ*G solves the geometric equation ∂_t g = -2χ²(Ric_g+g). (5) The continuation/restart argument (§6.3): the claim is that if T_i*<θr², the first-exit estimate ‖aF_T‖_∞≤CΓ/t is finite on [T_i*/2,T_i*), and then the staggered continuation hierarchy (T₀→(U₁,C₂)→T₁→...) gives a smooth endpoint, allowing restart. Check: (a) is the staggered hierarchy actually at proof level (referencing Step 60 base pair and Step 59 induction ledger), and (b) does the restart produce a flow that agrees with the original on the overlap? The latter is the uniqueness question that Step 57 showed fails for ungauged Ricci — is it resolved here by the autonomous splice, or is it still open? (6) TTCS's original review flagged 'standard fixed-parameter parabolic details' as the remaining content. Has that been supplied, or is it still cited as 'standard strongly parabolic theory'? Be explicit about what is at proof level, what is cited-standard, and what is open.

## Output

## Verification memo: per-datum transported-cutoff DeTurck construction in Step 56

The Step 56 note gives a coherent per-datum local existence construction for the regularized transported-cutoff DeTurck system. Its analytical division of labor is appropriate: low-order tame energy gives a common time interval for one datum; arbitrary-order tame propagation gives smoothness; scalar viscosity gives a maximum-principle-controlled cutoff; pullback removes the DeTurck vector field. The main mathematical structure is sound. At the level of a self-contained proof, several components remain schematic, cited-standard, or conditional on other notes.

Below is a point-by-point examination of the six requested items.

---

### 1. Tame energy estimate and independence from \(\varepsilon,\nu\)

The asserted hierarchy

\[
\frac d{dt}\mathcal E_m+c_{m,\lambda}\mathcal D_m^G+c_m\mathcal D_m^\beta
\le C_{m,R}(1+\mathcal E_m)
\tag{3.2}
\]

can have constants independent of \(0<\varepsilon,\nu\le 1\), provided the low bootstrap condition

\[
\lambda \bar g\le G\le \lambda^{-1}\bar g,
\qquad
\|G\|_{H^{s_0}}+\|\beta\|_{H^{s_0}}\le R
\tag{2.2}
\]

is in force.

The reasons are explicit in the note:

1. **No inverse powers of \(\varepsilon\) or \(\nu\).**  
   The metric principal coefficient is

   \[
   A=(\beta^2+\varepsilon)G^{-1}.
   \]

   Its derivative is

   \[
   DA=2\beta D\beta\,G^{-1}+(\beta^2+\varepsilon)D(G^{-1}),
   \]

   and no term contains \(\varepsilon^{-1}\). Weighted Young inequalities use only

   \[
   \frac{\beta^2}{\beta^2+\varepsilon}\le 1,
   \qquad
   \frac{\beta^4}{\beta^2+\varepsilon}\le 1,
   \]

   because \(0\le\beta\le1\). Thus the absorption of mixed terms such as

   \[
   \int D^mG*\beta D^{m+1}\beta*W
   \]

   or

   \[
   \int D^m\beta\,\beta^2 A(G)D^{m+1}G*D\beta
   \]

   does not introduce \(\varepsilon^{-1}\).

2. **The scalar viscosity contributes uniformly.**  
   The \(\nu\bar\Delta\beta\) term gives

   \[
   -\nu\|D^{m+1}\beta\|_2^2+C_m\nu\|\beta\|_{H^m}^2,
   \]

   and since \(0<\nu\le1\), the lower-order part is controlled by a constant independent of \(\nu\).

3. **The extra \(\varepsilon(R+Q)\) terms are lower order.**  
   They are multiplied by \(\varepsilon\le1\) and involve only smooth functions of \(G^{\pm1}\), \(DG\), and \(D^2G\) in tame products. They do not require division by \(\varepsilon\).

4. **The tame product estimate is linear in the current high norm.**  
   The interpolation count in Step 56 is the standard Moser–Hamilton tame structure: after removing one top derivative \(D^{m+1}G\) or \(D^{m+1}\beta\), all remaining products with total derivative order at most \(m+2\) obey

   \[
   \|D^{q_1}u_1*\cdots*D^{q_N}u_N\|_2
   \le C_{m,R}(1+\|G\|_{H^m}+\|\beta\|_{H^m}).
   \]

   The exponent calculation

   \[
   \theta_i=\frac{q_i-4}{m-4},
   \qquad
   \sum\theta_i<1
   \]

   for two or more high factors, and \(\theta_i\le1\) for one high factor, is correct under \(s_0>n/2+4\). The allocation script checks the finite combinatorial partitions, but it does not replace the tensor-index identities or the PDE argument.

The Lie cross-term absorption in §3.3 is also structurally correct. The term

\[
\int D^mG*\beta D^{m+1}\beta*W(G)
\]

is integrated by parts as

\[
-\int \beta D^{m+1}G*D^m\beta*W
-\int D^mG*D\beta*D^m\beta*W
-\int D^mG*\beta D^m\beta*DW.
\]

The first term is absorbed by the weighted metric dissipation because

\[
\frac{\beta^2}{\beta^2+\varepsilon}\le1.
\]

The second and third terms are lower-order provided \(W\), \(D\beta\), and \(DW\) are in \(L^\infty\). Since

\[
W(G)=G^{ab}(\Gamma(G)^k_{ab}-\Gamma(\bar g)^k_{ab})
\]

contains one derivative of \(G\), and \(DW\) contains two derivatives of \(G\), the condition \(s_0>n/2+4\) plus the low \(H^{s_0}\) bound gives the needed \(L^\infty\) control. Thus the absorption works under the low bootstrap condition.

The important point is that (2.2) is not a permanent consequence of the curvature-to-volume budget; it is a local bootstrap. Step 56 states the correct mechanism:

- at level \(m=s_0\), obtain a polynomial ODE inequality for \(\mathcal E_{s_0}\);
- choose \(R\) larger than the initial \(H^{s_0}\) size;
- choose \(T_0\) small enough that the ODE comparison keeps \(\mathcal E_{s_0}\le R^2\);
- use \(\partial_tG\in H^{s_0-2}\) and Sobolev embedding to keep \(G\) \(C^0\)-close to its initial value, hence preserve the metric equivalence \(\lambda\bar g\le G\le\lambda^{-1}\bar g\).

This is a standard continuation/bootstrap argument, but Step 56 does not write the full closed-open argument, the exact choice of \(R\), or the precise dependence of \(T_0\). Therefore:

- the tame estimate is uniform in \(\varepsilon,\nu\) once (2.2) holds;
- the preservation of (2.2) is plausible and standard, but currently remains a sketched bootstrap rather than a fully written proof component;
- the resulting \(T_0\) is per-datum. More precisely, it depends on the initial \(H^{s_0}\) norm, the cutoff geometry, and the background metric. The higher-order estimates do not shrink this interval, but they also do not make it sequence-uniform.

---

### 2. Maximum principle for \(\beta\)

The scalar equation is

\[
\partial_t\beta=\beta^2W(G)\cdot D\beta+\nu\bar\Delta\beta.
\]

For a smooth solution on a closed manifold, the maximum-principle argument is correct.

At a spatial maximum of \(\beta\),

\[
D\beta=0,
\qquad
\bar\Delta\beta\le0.
\]

Therefore

\[
\partial_t\beta=\nu\bar\Delta\beta\le0.
\]

At a spatial minimum,

\[
D\beta=0,
\qquad
\bar\Delta\beta\ge0,
\]

so

\[
\partial_t\beta\ge0.
\]

Thus if \(0\le\beta(0)=\chi\le1\), the interval \([0,1]\) is invariant. The transport coefficient \(\beta^2W\) does not create a zero-order source, and the diffusion sign is favorable. The argument does not require smallness of \(W\), only smoothness of the solution.

For \(\nu=0\), the limiting equation is a transport equation along the vector field \(\beta^2W\), and \(\beta\) is constant along its characteristics. The uniform \(\nu\to0\) limit preserves \(0\le\beta\le1\).

So the assertion

\[
0\le\beta(t)\le1
\]

is mathematically sound.

---

### 3. Smooth limit as \((\varepsilon,\nu)\to(0,0)\)

The compactness argument in §5 is structurally correct.

For each fixed datum, Step 56 obtains, for every \(m\ge s_0\),

\[
\sup_{t\in[0,T_0]}\mathcal E_m(t)
+\int_0^{T_0}(\mathcal D_m^G+\mathcal D_m^\beta)\,dt
\le C_m(g_0,\chi,T_0),
\]

uniformly in \(0<\varepsilon,\nu\le1\). The equations then give

\[
\|\partial_tG\|_{H^{m-2}}+\|\partial_t\beta\|_{H^{m-2}}\le C_m.
\]

From these bounds one can extract a diagonal subsequence converging in every space-time \(C^k\) norm. The ingredients are standard:

- boundedness in \(L^\infty_tH^m_x\) for all \(m\);
- boundedness of \(\partial_tG,\partial_t\beta\) in \(L^\infty_tH^{m-2}_x\);
- Sobolev embedding and Aubin–Lions-type compactness;
- diagonalization over a countable family of \(C^k\) norms.

The regularized terms vanish in the limit because they are multiplied by \(\varepsilon_j\) or \(\nu_j\), while the corresponding high norms remain uniformly bounded. For example,

\[
\varepsilon_j G_j^{-1}D^2G_j
\]

is bounded in \(C^k\) once \(G_j\) is bounded in a sufficiently high \(C^{k+2}\) norm and remains uniformly positive. Since \(G_j\) stays in a fixed metric neighborhood, \(G_j^{-1}\) is uniformly bounded in every \(C^k\) norm. Hence

\[
\varepsilon_j G_j^{-1}D^2G_j\to0
\]

in \(C^k\). The same applies to

\[
\varepsilon_j R(G_j,G_j),\qquad
\varepsilon_j Q(G_j,DG_j),\qquad
\nu_j\bar\Delta\beta_j.
\]

The nonlinear terms converge because \(G_j\to G\) and \(\beta_j\to\beta\) in sufficiently high \(C^k\) norms.

One part is not fully written in Step 56: the repeated time-differentiation argument. The note states that time derivatives are controlled by spatial estimates and that no division by \(\varepsilon,\nu\) occurs. This is the expected structure, but a complete proof would inductively bound all time derivatives needed for space-time \(C^k\) convergence. This is a standard parabolic regularity step, not a new obstruction.

Thus the smooth-limit argument is mathematically plausible and likely fillable, but currently it is presented at the level of a standard compactness sketch rather than a fully detailed proof.

---

### 4. Pullback and recovery of the geometric cutoff Ricci flow

Let \(\varphi\) solve

\[
\partial_t\varphi(t,x)
=
-\beta(t,\varphi(t,x))^2W(G)(t,\varphi(t,x)),
\qquad
\varphi(0,x)=x.
\]

Because the vector field is smooth on a closed manifold, \(\varphi(t)\) is a diffeomorphism on the existence interval.

For the unregularized limit, the \(\beta\)-equation is

\[
\partial_t\beta=\beta^2W(G)\cdot D\beta.
\]

Then along \(\varphi\),

\[
\frac{d}{dt}\beta(t,\varphi(t,x))
=
\partial_t\beta
+
d\beta(\partial_t\varphi)
=
\beta^2W\cdot D\beta
-
\beta^2W\cdot D\beta
=0.
\]

Therefore

\[
\beta(t,\varphi(t,x))=\beta(0,x)=\chi(x).
\]

Now set

\[
g(t)=\varphi(t)^*G(t).
\]

Using

\[
\partial_t(\varphi^*G)
=
\varphi^*\bigl(\partial_tG+L_{\partial_t\varphi}G\bigr),
\]

and \(\partial_t\varphi=-\beta^2W\), one obtains cancellation of the DeTurck Lie term if the \(G\)-equation has the geometric form

\[
\partial_tG
=
-2\beta^2(\operatorname{Ric}_G+G)
+
L_{\beta^2W(G)}G.
\]

Then

\[
\partial_tg
=
\varphi^*\bigl(
-2\beta^2(\operatorname{Ric}_G+G)
+
L_{\beta^2W}G
-
L_{\beta^2W}G
\bigr)
=
-2\varphi^*(\beta^2)(\operatorname{Ric}_g+g).
\]

Since \(\beta(t,\varphi(t,x))=\chi(x)\),

\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]

This is the desired geometric equation.

The one point that needs an explicit tensor-index verification is the identity between the schematic DeTurck system

\[
\partial_tG
=
\beta^2\bigl[G^{-1}D^2G+R(G,G)+Q(G,DG)-2G\bigr]
+
2\operatorname{sym}(d(\beta^2)\otimes W^\flat_G)
\]

and the geometric DeTurck form

\[
\partial_tG
=
-2\beta^2(\operatorname{Ric}_G+G)
+
L_{\beta^2W(G)}G.
\]

Step 56 uses this equivalence, but it does not display the full index computation. It is the standard Ricci–DeTurck relation, but for a self-contained proof one should write the precise definitions of \(R\), \(Q\), and \(W\), and verify that the extra cutoff-gradient term

\[
2\operatorname{sym}(d(\beta^2)\otimes W^\flat_G)
\]

is exactly the part of \(L_{\beta^2W}G\) produced by differentiating the scalar factor \(\beta^2\).

So the pullback argument is correct conditional on that standard DeTurck identity being fully recorded.

---

### 5. Continuation/restart and the staggered hierarchy

This is the most consequential place where the construction is not self-contained.

#### 5.1 Status of the staggered continuation hierarchy

Step 56 §6.3 uses the following logic:

1. For each datum, start the exact flow and form a maximal extendible smooth branch with right endpoint \(T_i^*\).
2. If \(T_i^*<\theta r^2\), run first-exit estimates on \((0,\min\{T_i^*,\theta r^2\})\).
3. Use the positive-time continuation hierarchy

   \[
   T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
   \longrightarrow(U_2,C_3)\longrightarrow T_2\longrightarrow\cdots
   \]

   to obtain a smooth terminal metric at \(T_i^*\).
4. Restart the local theorem from that terminal metric, extending the branch beyond \(T_i^*\).
5. Conclude that every datum reaches \(\theta r^2\).

The logical shape is reasonable. However, the ingredients needed for step 3 are not fully proved inside Step 56.

The base-pair note, Step 60, gives a substantial derivation of the \(m=1\) pair \((U_1,C_2)\) from the imported inputs

\[
U_0\in L^\infty,
\qquad
T_0\in L^q_{\mathrm{fin}}.
\]

It explains how the apparent circular \(m=1\) terms are converted into signed-Hessian forms and controlled by the signed-Hessian integration lemma. The key mechanism is plausible:

\[
\int |V|^{p-2}V*\chi C_3*U_0
\]

is integrated by parts, producing a signed contraction of the form

\[
\int \chi \nabla_i\nabla_j\chi\,\mathcal B^{ij}(V),
\]

which can be estimated using only \(\|C_1\|_\infty\).

But Step 60 itself lists remaining proof obligations:

- exact tensor-index evolution formulas for the general \(U_m\) and \(T_m\) equations;
- complete energy estimates for all remainder families;
- fixed-background Sobolev product estimates;
- verification of the imported Moser endpoints and local existence module.

Step 59 repairs the induction ledger and clarifies the extraction of current-order terms:

\[
\chi C_{m+2}*U_0,
\qquad
\chi C_{m+1}*U_1,
\qquad
C_1*C_{m+1}*U_0,
\qquad
\chi C_2*U_m,
\qquad
C_1*C_1*U_m.
\]

It also states a derivative-reordering lemma asserting that the highest cutoff jet \(C_{m+2}\) appears only with zero-order curvature. This is exactly the kind of structural fact needed, but Step 59 presents it as a proof sketch, not as a completed tensor-index lemma.

Moreover, the first-exit estimates used in Step 56,

\[
\|aF_T(t)\|_\infty\le C\gamma/t,
\qquad
\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3},
\]

are not reproved in Step 56. Their use is explicitly conditional on the unweighted \(H_2\), \(Y\), \(J_6\), and local \(Q_\alpha\) inequalities having only first-cutoff-derivative constants after signed Hessian integration by parts.

Therefore, the staggered continuation hierarchy is not currently at complete proof level inside the supplied material. It is a detailed analytic program with several crucial components identified and partially developed, but it still requires:

- a complete tensor-index derivation of the differentiated \(U_m\) and \(T_m\) hierarchies;
- a complete proof of the derivative-reordering lemma;
- complete energy estimates for all levels \(m\ge2\);
- proof that all constants in the collapse-uniform estimates use only permitted inputs;
- independent derivation of the imported zero-order endpoints.

Until those are supplied, the statement that every datum reaches \(\theta r^2\) is conditional on the Step 59/Step 60 continuation machinery and the first-exit estimates.

#### 5.2 Restart, overlap, and uniqueness

For the specific purpose of contradicting maximality of \(T_i^*\), one does not need uniqueness on an open overlap if the restart is performed exactly at a smooth terminal time. If the terminal metric and its relevant jets are smooth, then any smooth solution starting from that terminal data gives an extension beyond \(T_i^*\). That is enough to show that the previous branch was not maximal.

However, several subtleties remain.

First, the smooth terminal metric itself is produced by the staggered hierarchy. As just noted, that hierarchy is not yet complete.

Second, if one wants the restarted solution to be the same branch in a canonical sense, or if one needs to compare two continuations on an overlapping interval, then uniqueness is required. Step 56 explicitly states that the restricted Ishida–LeBrun argument uses existence and restart, not canonical uniqueness. It also states that a full uniqueness statement requires the branch-oriented difference ledger.

Third, the autonomous splice mentioned in Step 59 is intended to avoid an overlap-uniqueness argument by matching terminal time-jets. But the splice is not developed in Step 56, and its proof status is not established in the supplied material. To use it safely, one would need to verify that:

- the spliced object is a smooth solution of the same geometric equation;
- the splice preserves the stationary region where \(a=0\);
- the global defect quantity used in the Ishida–LeBrun interface is preserved or controlled through the splice;
- the time-jet matching does not introduce additional curvature or cutoff constants.

Thus:

- extension beyond a smooth terminal endpoint can be argued without overlap uniqueness;
- canonical branch agreement remains unresolved;
- the autonomous splice is a proposed mechanism, not a completed proof component in Step 56;
- the uniqueness/difference-ledger part remains open.

---

### 6. Status of the fixed-parameter parabolic details

Step 56 still relies on “standard quasilinear strongly parabolic theory” for the fixed-\((\varepsilon,\nu)\) system. Specifically, it uses standard theory for:

- local existence of smooth solutions for fixed positive \(\varepsilon,\nu\);
- continuation as long as the solution remains smooth and the metric stays positive;
- strong parabolicity of the diagonal block system

  \[
  (\beta^2+\varepsilon)G^{ab}\xi_a\xi_b I_{\mathrm{Sym}^2},
  \qquad
  \nu\bar g^{ab}\xi_a\xi_b.
  \]

These are reasonable citations. For fixed \(\varepsilon>0\) and \(\nu>0\), the system is strongly parabolic because the metric block has coefficient at least \(\varepsilon\) and the scalar block has coefficient \(\nu\).

But the note does not supply the fixed-parameter parabolic construction itself. It does not write:

- the function-space setup;
- the linearization and invertibility argument;
- the contraction or Galerkin construction;
- the precise continuation theorem;
- the dependence of the fixed-parameter local time on \(\varepsilon,\nu\);
- the proof that the energy/continuation argument prevents the fixed-parameter solution from stopping before the common \(T_0\).

The last point is the important one: even if the fixed-parameter local existence time shrinks as \(\varepsilon,\nu\to0\), the uniform tame energy and continuation argument is intended to show that every regularized solution reaches the same per-datum \(T_0\). That argument is outlined, but the fixed-parameter continuation theorem is still cited rather than proved.

Thus the TTCS-flagged “standard fixed-parameter parabolic details” have not been fully supplied inside Step 56. They remain cited-standard.

---

## Summary by component

| Component | Status |
|---|---|
| Tame product estimate | Structurally correct; interpolation count is explicit; allocation script supports the combinatorics but does not prove tensor identities. |
| Uniformity of \(C_{m,R}\) in \(\varepsilon,\nu\) | Correct under the low bootstrap condition (2.2); no inverse powers of \(\varepsilon,\nu\) appear. |
| Maintenance of low bootstrap | Standard continuation argument sketched; not fully written. |
| Maximum principle for \(\beta\) | Correct. |
| Uniform high-order bounds | Structurally correct; time-derivative induction not fully detailed. |
| Smooth limit and vanishing of regularization terms | Correct in outline; standard compactness details not fully written. |
| Pullback to geometric flow | Correct conditional on explicit Ricci–DeTurck identity. |
| Fixed-\((\varepsilon,\nu)\) local existence | Cited as standard strongly parabolic theory; not constructed in detail. |
| First-exit estimates | Not reproved in Step 56; used conditionally. |
| Staggered continuation hierarchy | Depends on Step 59/Step 60; not complete proof level in supplied material. |
| Base pair \((U_1,C_2)\) | Substantial progress in Step 60, but exact tensor-index formulas and remainder estimates remain to be completed. |
| General \(m\ge2\) induction | Ledger repaired structurally; derivative-reordering lemma remains proof sketch. |
| Restart without overlap uniqueness | Possible for mere extension from a smooth terminal endpoint. |
| Canonical branch agreement/uniqueness | Unresolved; autonomous splice not proved in Step 56. |

---

## Overall assessment

The Step 56 construction gives the right analytic architecture for a per-datum smooth solution of the transported-cutoff flow. The tame estimates are designed so that regularization parameters do not enter destructively, the scalar viscosity gives a clean maximum principle, and the limit and pullback mechanisms are mathematically natural.

The strongest parts are:

- the tame high-order energy structure;
- the explicit avoidance of divisions by \(a\), \(\varepsilon\), or \(\nu\);
- the correct use of low-order control to absorb top mixed terms;
- the clear separation between per-datum local existence and sequence-uniform first-exit time.

The parts that are not yet self-contained are:

- the full bootstrap proof that (2.2) persists on \([0,T_0]\);
- the fixed-parameter parabolic existence/continuation details;
- the tensor-index verification of the DeTurck-to-geometric identity;
- the complete first-exit and staggered continuation hierarchy;
- the general induction beyond the base pair;
- the uniqueness/splice issue.

As it stands, Step 56 establishes a credible per-datum existence skeleton. It does not yet provide a fully self-contained proof of the continuation machinery needed to reach the common observation time \(\theta r^2\) uniformly across an Ishida–LeBrun sequence, and it does not settle uniqueness or the full Yau Problem 26 statement.