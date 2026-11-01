# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step58_all_order_continuation_proof.md",
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md",
    "Sessions/S0910A01/workspace/notes/step57_preceptor_deTurck_uniqueness_and_scope_review.md",
    "Sessions/S0910A01/trace/ttcs/results/step57_ttcs02_verifier1_integration.md"
  ]
}
```

## Task

Verify the proof-level all-order continuation note for the restricted four-dimensional negative IL cutoff flow. Focus on five specific mathematical points:

1. CORRECTED BASE EQUATIONS (§2): The T-equation is ∂_t T = aΔT + B₁*∇T + B₂*T + a(T*T + T). The U-equation after the (B₁*B₁)*T = 4(C₁*C₁)*U identity is ∂_t U = div(a∇U) + B₁*∇U + B₂*U + 4(C₁*C₁)*U + U*U + aU. Verify: (a) T=U=0 is stationary, (b) no independent constant forcing a·1 or a² appears, (c) the conversion from ∂_t U = a·∂_t T using the Laplacian product rule is correct.

2. INDUCTION BASE (§3, §5.2): The base layer T₀,T₁,U₁,C₂ ∈ L^q is established by the curvature/defect Moser endpoints and the W^{1,p} bridge. Verify that the general induction mechanism (§5) genuinely fails at m=1 — specifically that I₁ = ∫χ|C₂||U₁|^p cannot be closed by the same Hölder-Sobolev pattern because U₁ is the current unknown.

3. CRITICAL RESIDUAL ABSORPTION (§5.2): For m≥2, the residual I_m = ∫χ|C_{m+1}||U₁||U_m|^{p-1} is controlled using f=χ|U_m|^{p/2}, Hölder (4,p,4,2p/(p-2)), and U₁∈L⁴ as a base-layer quantity. Verify the exponent matching, the role of U₁ as known (not current), and whether Young yields the correct linear Grönwall structure.

4. SIGNED-HESSIAN INTEGRATION (§5.3): The term χC₂*U_m is not treated as a bounded coefficient. Integration by parts replaces C₂=∇C₁+... and produces ε D_{m,p}^U + C||C₁||_∞²||V||_p^p. Verify this uses only ||∇χ||_∞, not ||∇²χ||_∞.

5. AUTONOMOUS SPLICE (§8): The C^∞ convergence g(t)→g_* from §7, plus positive-definiteness from §8.1, plus the recursive jet identity F_ℓ(g*) = lim ∂_t^ℓ g(t) = ∂_s^ℓ ĝ(0), gives a smooth spliced solution across T*. Verify: (a) all one-sided jets genuinely match because the PDE is autonomous; (b) no uniqueness comparison is needed; (c) the positive-definiteness argument from the integrable defect endpoint is correct.

## Output

# Scientific verification memo

## Overall assessment

The five requested mechanisms are mathematically sound, assuming the imported base estimates and per-datum local existence theorem. Two textual points need precision:

1. The \(U\)-equation is correct as a schematic star-product equation, but §5.1 mixes the divergence term with an additional \(B_1*\nabla U_m\) drift. The latter requires its own weighted Young estimate.
2. The estimates establishing \(T_0,T_1,U_1,C_2\in L_t^\infty L_x^q\) are cited rather than reproduced in the supplied files. The supplied material does verify that these are exactly the inputs needed to begin at \(m=2\).

---

## 1. Corrected base equations

Let \(U=aT\), \(B_1=\nabla a\), and \(B_2=\nabla^2a\). Since \(a\) is time-independent,
\[
\partial_tU=a\,\partial_tT.
\]
The product identities give
\[
\Delta U=a\Delta T+2\nabla a*\nabla T+(\Delta a)T,
\qquad
a\nabla T=\nabla U-(\nabla a)*T.
\]
For example, the Laplacian contribution can be written
\[
a^2\Delta T
=\operatorname{div}(a\nabla U)
+B_1*\nabla U+B_2*U+(B_1*B_1)*T,
\]
where the star notation absorbs the universal numerical coefficients and tensor contractions. Similarly,
\[
a(B_1*\nabla T)=B_1*\nabla U+(B_1*B_1)*T,
\qquad
a(B_2*T)=B_2*U.
\]
The reaction terms satisfy
\[
a^2(T*T)=U*U,\qquad a^2T=aU.
\]
Thus the structural family
\[
\partial_tU
=\operatorname{div}(a\nabla U)+B_1*\nabla U+B_2*U
 +(B_1*B_1)*T+U*U+aU
\]
is correct.

Since
\[
B_1=2\chi C_1,\qquad a=\chi^2,
\]
each concrete contraction obeys
\[
(B_1*B_1)*T
=4\chi^2(C_1*C_1)*T
=4(C_1*C_1)*U.
\]
This is a global algebraic identity and uses no division by \(a\).

If \(T=0\), then \(\operatorname{Rm}=-G\), hence \(\operatorname{Ric}=-g\). Therefore
\[
\partial_tg=-2a(\operatorname{Ric}+g)=0,
\]
and consequently \(\partial_tT=\partial_tU=0\). Thus the normalized equations contain no independent \(a\cdot1\) or \(a^2\) forcing after all constant-curvature terms are combined.

### Drift bookkeeping

Equation (2.5) displays both
\[
\operatorname{div}(a\nabla U)
\quad\text{and}\quad
B_1*\nabla U.
\]
Testing the divergence term gives directly
\[
\int \langle |V|^{p-2}V,\operatorname{div}(a\nabla V)\rangle
\le -c_p\int a|\nabla V|^2|V|^{p-2}.
\]
There is no additional cross term from this divergence-form integration. The separately displayed drift is estimated by
\[
\begin{aligned}
\left|\int B_1*\nabla V*V|V|^{p-2}\right|
&\le \varepsilon D_{m,p}^U
 +C_\varepsilon\int \frac{|B_1|^2}{a}|V|^p\\
&=\varepsilon D_{m,p}^U
 +4C_\varepsilon\|C_1\|_\infty^2\|V\|_p^p.
\end{aligned}
\]
Thus the energy closes, but §5.1 should distinguish this drift estimate from the pure divergence computation.

---

## 2. Induction base and the \(m=1\) circularity

The present files cite A03 Step 57, A03 Step 58, and A01 Step 34 for
\[
T_0,T_1,U_1,C_2\in L_t^\infty L_x^q
\qquad\text{for every finite }q.
\]
Those derivations are not reproduced here; Step 55 also takes the same estimates as assumptions. Their logical use in the all-order induction is nevertheless correct.

For the general residual, write
\[
V=U_m,\qquad Z=C_{m+1}.
\]
At \(m=1\), \(V=U_1\), \(Z=C_2\), and
\[
I_1=\int\chi |C_2||U_1|^p.
\]
Applying the pattern from §5.2 would give
\[
I_1
\le
\|\chi|V|^{p/2}\|_4\,
\|Z\|_p\,
\underbrace{\|V\|_4}_{\text{same current variable}}\,
\|V\|_p^{p/2-1}.
\]
After Sobolev and Young, one obtains terms such as
\[
\|Z\|_p^2\|V\|_4^2\|V\|_p^{p-2},
\]
rather than a bound linear in
\[
1+\|Z\|_p^p+\|V\|_p^p.
\]
For instance, at \(p=4\) this includes a product proportional to
\[
\|C_2\|_4^2\|U_1\|_4^4.
\]
Hence the same argument does not independently establish the \(m=1\) pair. Once \(U_1\in L_t^\infty L_x^4\) has been obtained by the separate base module, the circular factor becomes a known coefficient. Starting the general induction at \(m=2\) is therefore mathematically necessary for the stated proof architecture.

---

## 3. Critical residual for \(m\ge2\)

For
\[
I_m=\int\chi |Z||U_1||V|^{p-1},
\qquad
f=\chi|V|^{p/2},
\]
write
\[
\chi|V|^{p-1}
=f\,|V|^{p/2-1}.
\]
For \(p>2\), the Hölder exponents satisfy
\[
\frac14+\frac1p+\frac14+\frac{p-2}{2p}=1,
\]
and
\[
\bigl\||V|^{p/2-1}\bigr\|_{2p/(p-2)}
=\|V\|_p^{p/2-1}.
\]
Thus
\[
I_m
\le
\|f\|_4\,\|Z\|_p\,\|U_1\|_4\,\|V\|_p^{p/2-1}.
\]
For \(p=2\), the exponents \((4,2,4)\) give the corresponding estimate.

The four-dimensional Sobolev estimate gives
\[
\|f\|_4
\le C\left(D_{m,p}^{U\,1/2}+\|V\|_p^{p/2}\right),
\]
with \(p\)- and cutoff-dependent constants. Set
\[
X=\|V\|_p,\qquad Y=\|Z\|_p,\qquad
K=\sup_{t\in[\tau,T_*)}\|U_1(t)\|_4.
\]
For \(m\ge2\), \(K<\infty\) comes from the base layer and is not part of the current pair. Hence
\[
I_m
\le CKYX^{p/2-1}D^{1/2}
   +CKYX^{p-1}.
\]
Young’s inequality gives
\[
I_m
\le\varepsilon D
 +C K^2Y^2X^{p-2}
 +CKYX^{p-1}.
\]
For \(p>2\),
\[
Y^2X^{p-2}\le C_p(Y^p+X^p),
\qquad
YX^{p-1}\le C_p(Y^p+X^p).
\]
The \(p=2\) case gives the same quadratic structure directly. Therefore
\[
I_m\le
\varepsilon D_{m,p}^U+
C_{m,p,\tau}\bigl(\|Z\|_p^p+\|V\|_p^p\bigr),
\]
which has precisely the linear Grönwall form used in (5.12).

---

## 4. Signed-Hessian integration

In covariant notation,
\[
C_2=\nabla C_1
\]
exactly; no coordinate connection remainder is needed. For
\[
J_m=\int\chi(C_2)_{ij}\mathcal B^{ij}(V),
\]
integration by parts on the closed manifold gives
\[
J_m
=-\int (C_1)_i(C_1)_j\mathcal B^{ij}(V)
 -\int\chi(C_1)_j\nabla_i\mathcal B^{ij}(V).
\]
Using
\[
|\mathcal B(V)|\le C|V|^p,
\qquad
|\nabla\mathcal B(V)|
\le Cp|V|^{p-1}|\nabla V|,
\]
one gets
\[
|J_m|
\le C\int |C_1|^2|V|^p
 +Cp\int\chi|C_1||V|^{p-1}|\nabla V|.
\]
Weighted Young gives
\[
|J_m|
\le
\varepsilon\int\chi^2|\nabla V|^2|V|^{p-2}
+C_{p,\varepsilon}\|C_1\|_\infty^2\|V\|_p^p.
\]
Thus this step uses only
\[
\|C_1\|_\infty=\|\nabla\chi\|_\infty,
\]
not an \(L^\infty\) estimate for \(C_2=\nabla^2\chi\).

---

## 5. Autonomous splice and positivity

Define
\[
\mathcal F(g)=-2\chi^2(\operatorname{Ric}_g+g),
\qquad
\mathcal F_1=\mathcal F,\qquad
\mathcal F_{\ell+1}(g)
=D\mathcal F_\ell(g)[\mathcal F(g)].
\]
Because \(\chi\) is fixed in time, this is an autonomous smooth differential operator on the open set of positive metrics. Every smooth solution satisfies
\[
\partial_t^\ell g(t)=\mathcal F_\ell(g(t)).
\]
The convergence \(g(t)\to g_*\) in \(C^\infty\) implies
\[
\partial_t^\ell g(t)
=\mathcal F_\ell(g(t))
\longrightarrow\mathcal F_\ell(g_*)
\quad\text{in }C^\infty.
\]
For any smooth local solution \(\hat g(s)\) with \(\hat g(0)=g_*\),
\[
\partial_s^\ell\hat g(0)=\mathcal F_\ell(g_*).
\]
Hence all pure time derivatives match. Since the matching occurs in \(C^\infty\) spatial topology, every mixed space-time derivative also matches. The piecewise metric is therefore smooth across \(T_*\). This uses no comparison between two branches on a common time interval.

For positive definiteness, set
\[
k(t)=\|aE(t)\|_{g(t),\mathrm{op}}.
\]
For every fixed tangent vector,
\[
-2k(t)g(t)\le\partial_tg(t)\le2k(t)g(t)
\]
as quadratic forms. The defect estimate gives
\[
k(t)\le C_E\delta r^{2/3}t^{-1/3},
\]
so
\[
V_*=\int_\tau^{T_*}k(t)\,dt
\le \frac32C_E\delta r^{2/3}
\left(T_*^{2/3}-\tau^{2/3}\right)<\infty.
\]
Integrating the quadratic-form inequality yields
\[
e^{-2V_*}g(\tau)\le g(t)\le e^{2V_*}g(\tau).
\]
Passing to the smooth limit gives the same lower estimate for \(g_*\), so \(g_*\) is a smooth positive Riemannian metric.

## Conclusion

The corrected base structure, the \(m=2\) starting point, the residual absorption, the signed-Hessian integration, and the autonomous splice are all valid under the cited base estimates and local existence input. The concrete internal correction is that the separately displayed \(B_1*\nabla U_m\) drift must be estimated by weighted Young rather than described as part of the pure divergence integration.