# Step 60: Base-pair continuation at tensor-index level

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Mathematical purpose

This note constructs the self-contained base-pair continuation proof that
Step 59 identified as the nearest decisive mathematical work.  The target is
the non-circular derivation of the base derivative estimates
`(U_1,C_2)\in L^q` from the imported zero-order inputs
`U_0\in L^\infty` and `T_0\in L^q_{\rm fin}`, followed by `T_1\in L^q`
and `T_0\in L^\infty`.

The m=1 case is excluded from the general current-pair induction because the
critical residual at m=1 would read
\[
I_1=\int\chi|C_2|\,|U_1|\,|U_1|^{p-1}=\int\chi|C_2||U_1|^p,
\]
in which the factor `U_1` is the current unknown, not base data.  The general
`m\ge2` Hölder argument cannot be applied.  The m=1 case must instead close by
a different mechanism: the signed-Hessian integration lemma, applied to the
actual tensor contractions in the differentiated U-equation.

The main result of this note is that **every coefficient-derivative term at
m=1 has total cutoff derivative `\le 3`**.  The `C_3` that arises from
`B_3*U_0` reduces to signed `C_2`-Hessian terms via integration by parts,
so no top-cutoff integration beyond one step is needed.  All m=1 Hessian
terms have the signed form required by the A03 Step 38 lemma.  The base
pair closes in a coupled estimate with the `C_2` evolution, which
produces only `C_1*U_1` and lower terms.

---

## 1. Setup and imported inputs

Work on a positive-time slab `[\tau,T_*)` with `\tau>0` of a smooth solution of
\[
\partial_tg=-2aE,\qquad E=\operatorname{Ric}_g+g,\qquad a=\chi^2,
\tag{1.1}
\]
on a fixed support with auxiliary cutoff `\eta` and the structural property
\[
\operatorname{supp}\chi\Subset\{\eta=1\},\qquad
\operatorname{supp}\nabla\eta\subset\{\chi=0\}.
\tag{1.2}
\]

Write
\[
T=\operatorname{Rm}+G,\qquad G=\frac{g\owedge g}{2(n-1)},\qquad U=aT,
\tag{1.3}
\]
so `\operatorname{Ric}(U)=aE`.  Use
\[
U_j=\nabla^jU,\quad T_j=\nabla^jT,\quad C_j=\nabla^j\chi,\quad B_j=\nabla^ja.
\tag{1.4}
\]

**Imported inputs on `[\tau,T_*)`:**

(I1) Zero-order weighted curvature:
\[
\|U(t)\|_{L^\infty}\le K_\tau<\infty.
\tag{1.5}
\]
This is the curvature Moser endpoint `\|aF_T(t)\|_\infty\le C\Gamma/t`
at positive time.

(I2) Zero-order unweighted curvature at finite exponent:
\[
\|T(t)\|_{L^q}\le K_{T,q}<\infty\quad\text{for all finite }q.
\tag{1.6}
\]
This follows from the H₂ first-exit estimate
`\int\eta^2(1+|\operatorname{Rm}|^2)` plus Sobolev interpolation on the
per-datum smooth interval.

(I3) Metric equivalence and Sobolev constants:
\[
e^{-2V(t)}g(0)\le g(t)\le e^{2V(t)}g(0),\qquad
\mathcal S(t)\le e^{8V(t)}\mathcal S(0),
\tag{1.7}
\]
with `V(t)` and `\mathcal S(t)` from the joint bootstrap.

(I4) Cutoff regularity:
\[
\|C_1\|_{L^\infty}\le C_{\rm cut}<\infty,\qquad
\chi\in[0,1],\qquad a=\chi^2\in[0,1].
\tag{1.8}
\]

**Key algebraic identity** (Step 58, (2.4)):
\[
(B_1*B_1)*T=4\chi^2(C_1*C_1)*T=4(C_1*C_1)*U.
\tag{1.9}
\]
No division by `a` is performed; the identity is algebraic.

---

## 2. The zero-order U-equation and its first spatial derivative

The zero-order U-equation from Step 58, (2.5), after applying (1.9), is
\[
\partial_tU=\operatorname{div}(a\nabla U)+B_1*\nabla U+B_2*U
+4(C_1*C_1)*U+U*U+aU.
\tag{2.1}
\]

Apply `\nabla` to (2.1).  Set `V=U_1=\nabla U`.  For each source term, we
compute the first derivative and classify the result by total cutoff
derivative.

### 2.1 Differentiating the principal operator

The principal operator is `\operatorname{div}(a\nabla U)`.  In coordinates,
\[
\operatorname{div}(a\nabla U)^I
=\nabla_j(a\nabla^jU^I).
\]
Apply `\nabla_k`:
\[
\nabla_k\nabla_j(a\nabla^jU^I)
=\nabla_j\nabla_k(a\nabla^jU^I)
+[\nabla_k,\nabla_j](a\nabla^jU^I).
\]

The commutator produces curvature terms:
\[
[\nabla_k,\nabla_j](a\nabla^jU^I)
=\operatorname{Rm}*(a\nabla U)
=aT*V.
\tag{2.2}
\]

For the main part:
\[
\nabla_j\nabla_k(a\nabla^jU^I)
=\nabla_j(B_{1,k}\nabla^jU^I+a\nabla_k\nabla^jU^I).
\]
Expanding the product:
\[
=\nabla_j(B_{1,k}\nabla^jU^I)
+\nabla_j(a\nabla_k\nabla^jU^I).
\]
The second term is `\operatorname{div}(a\nabla V)` plus connection corrections
of type `aT*V` (from commuting `\nabla_k` and `\nabla^j`).  The first term:
\[
\nabla_j(B_{1,k}\nabla^jU^I)
=B_{2,jk}\nabla^jU^I+B_{1,k}\nabla_j\nabla^jU^I
=B_2*V+B_1*\nabla V.
\tag{2.3}
\]

Therefore, from the principal operator:
\[
\nabla(\operatorname{div}(a\nabla U))
=\operatorname{div}(a\nabla V)+B_2*V+B_1*\nabla V+aT*V+aT_1*U_0.
\tag{2.4}
\]

The last term `aT_1*U_0` comes from the divergence-form descendant
`\nabla_j(a[\nabla_k,\nabla^j]U^I)`: the curvature commutator produces
`a\operatorname{Rm}*V`, and differentiating the connection correction gives
`aT_1*U_0`.  Using `aT_1=V-B_1*T_0` (from §5.2, eq (5.3) below), this is
controlled by the base inputs.

**Classification:** `B_2*V` has total cutoff derivative 2.  This is the
m=1 Hessian term.

A time commutator also arises: `\partial_t(\nabla U) = \nabla(\partial_t U)
+ (\partial_t\Gamma)*U`.  The commutator term is `(\partial_t\Gamma)*U_0
= g^{-1}*U_1*U_0`, which is bounded by `\|U_0\|_\infty\|V\|_p`.

### 2.2 Differentiating the drift

\[
\nabla(B_1*\nabla U)=B_2*\nabla U+B_1*\nabla^2U
=B_2*V+B_1*\nabla V.
\tag{2.5}
\]

**Classification:** `B_2*V` again (cutoff derivative 2), plus `B_1*\nabla V`
which is diffusion-absorbable.

### 2.3 Differentiating the Hessian-cutoff term

\[
\nabla(B_2*U)=B_3*U+B_2*V.
\tag{2.6}
\]

**Classification:** `B_3*U_0` has cutoff derivative 3.  However,
\[
B_3=\nabla^3(\chi^2)=2\chi C_3+6C_1*C_2.
\]
So
\[
B_3*U_0=2\chi C_3*U_0+6C_1*C_2*U_0.
\tag{2.7}
\]
The first term involves `C_3` paired with `U_0`.  The second involves `C_2`
paired with `U_0`.

**Wait — this introduces C₃!**  The `B_3*U_0` term from differentiating
`B_2*U` contains `\chi C_3*U_0`, which has cutoff derivative 3 paired with
the zero-order `U_0`.  This is the `\chi C_{m+2}*U_0` structure at m=1.

For m=1, the top-cutoff integration by parts gives:
\[
\int|V|^{p-2}V*\chi C_3*U_0
=-\int\nabla(|V|^{p-2}V)*\chi C_2*U_0
-\int|V|^{p-2}V*C_1*C_2*U_0
-\int|V|^{p-2}V*\chi C_2*V.
\tag{2.8}
\]
The first term is absorbed by diffusion.  The second is bounded by Young
with bounded `C_1,U_0`.  The third is
\[
\int\chi|C_2||U_1|^p=\int\chi|C_2||V|^p.
\tag{2.9}
\]

**This is the m=1 circular term!**  The third term in (2.8) has the same
structure as the m=1 Hessian residual.  It couples `C_2` (current) to
`|V|^p` (current).  The signed-Hessian lemma cannot be applied because
`C_2` is not the Hessian factor here; it is paired with `|V|^p`, not with
`\nabla^2\chi` acting on a bilinear form of `V`.

### 2.4 Resolution: the C₃ term can be avoided

The term `B_3*U_0` from `\nabla(B_2*U)` is avoidable because the original
`B_2*U` in (2.1) can be rewritten before differentiating.  Specifically,
\[
B_2*U=(2\chi C_2+2C_1*C_1)*U.
\]
The first part `2\chi C_2*U` can be integrated by parts in the energy
estimate of the zero-order U-equation.  But for the continuation we
differentiate the equation, not the energy.

**Alternative:** Instead of differentiating (2.1) directly, use the
divergence form for the full differentiated equation.  The key is that
`B_2*U` in (2.1) can be written as
\[
B_2*U=\operatorname{div}(B_1*U)-B_1*\nabla U.
\]
Substituting into (2.1):
\[
\partial_tU=\operatorname{div}(a\nabla U)+B_1*\nabla U
+\operatorname{div}(B_1*U)-B_1*\nabla U
+4(C_1*C_1)*U+U*U+aU.
\]
The `B_1*\nabla U` terms cancel:
\[
\partial_tU=\operatorname{div}(a\nabla U+B_1*U)
+4(C_1*C_1)*U+U*U+aU.
\tag{2.10}
\]

Now differentiate (2.10):
\[
\partial_tV=\nabla\operatorname{div}(a\nabla U+B_1*U)
+\nabla(4(C_1*C_1)*U)+\nabla(U*U)+\nabla(aU).
\tag{2.11}
\]

The first term:
\[
\nabla\operatorname{div}(a\nabla U+B_1*U)
=\nabla\operatorname{div}(a\nabla U)+\nabla\operatorname{div}(B_1*U).
\]
From §2.1:
\[
\nabla\operatorname{div}(a\nabla U)
=\operatorname{div}(a\nabla V)+B_2*V+B_1*\nabla V+aT*V.
\tag{2.12}
\]

For the new part:
\[
\nabla\operatorname{div}(B_1*U)
=\nabla(B_2*U+B_1*\nabla U)
=B_3*U+B_2*V+B_2*V+B_1*\nabla V.
\]
Wait, this brings back `B_3*U`.  Let me redo:
\[
\operatorname{div}(B_1*U)
=\nabla_j(B_1^jU^I)
=B_2,j^j U^I+B_1^j\nabla_jU^I
=(\Delta a)U+B_1*\nabla U.
\]
Then
\[
\nabla\operatorname{div}(B_1*U)
=\nabla((\Delta a)U)+\nabla(B_1*\nabla U)
=(\nabla\Delta a)U+(\Delta a)V+B_2*V+B_1*\nabla V.
\]
The first term `(\nabla\Delta a)U=B_3*U_0` still appears.  So rewriting
`B_2*U` in divergence form before differentiating does not remove the
`B_3*U_0` term.

### 2.5 Correct resolution: absorb C₃ via the pair energy

The `B_3*U_0` term produces `\chi C_3*U_0` in the differentiated equation.
In the energy, after testing against `|V|^{p-2}V` and integrating by parts
once, the problematic remnant is
\[
I_{\rm top}=\int\chi|C_2||V|^p.
\tag{2.13}
\]

This is structurally identical to the m=1 Hessian residual
`J_1=\int\chi C_2*V*|V|^{p-2}V`.  Both couple `C_2` to `|V|^p` with a
single `\chi` factor.  The signed-Hessian lemma treats `J_1` by integrating
`C_2=\nabla C_1` off the product, yielding terms with only `C_1` and `\nabla V`.

But for `I_{\rm top}`, the `C_2` came from integrating `C_3` once; we cannot
integrate `C_2` again because `C_2=\nabla C_1` and integrating again would
create a boundary term with `C_1*V` inside, which is bounded.  Let me check:
\[
I_{\rm top}=\int\chi|C_2||V|^p
\]
is not a signed tensor contraction of the form (1.1) from A03 Step 38.
The A03 lemma requires the form
\[
J=\int\chi\nabla_i\nabla_j\chi B^{ij}(V),
\]
where `B^{ij}(V)` is a bilinear form of `V` (the current unknown).  In
`I_{\rm top}`, the integrand is `\chi|C_2||V|^p`, which is the absolute
value, not a signed contraction.

**Key question:** Is the actual tensor contraction from `B_3*U_0` of the
signed form?  The term is
\[
|V|^{p-2}V*(B_3*U_0).
\]
Expanding `B_3=2\chi C_3+6C_1*C_2`:
\[
|V|^{p-2}V*(2\chi C_3*U_0)+|V|^{p-2}V*(6C_1*C_2*U_0).
\]
The first term: `2\chi |V|^{p-2}V*C_3*U_0`.  Since `C_3=\nabla C_2`,
integrating once:
\[
2\int\chi|V|^{p-2}V*C_3*U_0
=-2\int\nabla(\chi|V|^{p-2}V*U_0)*C_2.
\]
Expanding the derivative:
\[
-2\int C_1*|V|^{p-2}V*U_0*C_2
-2\int\chi\nabla(|V|^{p-2}V)*U_0*C_2
-2\int\chi|V|^{p-2}V*\nabla U_0*C_2.
\]
The first is bounded.  The second is absorbed by diffusion.  The third:
\[
-2\int\chi|V|^{p-2}V*V*C_2=-2\int\chi|V|^p*C_2.
\tag{2.14}
\]

This is a signed contraction!  The `*` in `|V|^p*C_2` means a specific
tensor contraction of the `(p+2)`-tensor `|V|^{p-2}V\otimes V\otimes C_2`.
Writing `C_2=\nabla^2\chi`, this is
\[
-2\int\chi\nabla_i\nabla_j\chi\,\mathcal B^{ij}(V),
\tag{2.15}
\]
where `\mathcal B^{ij}(V)` is the specific contraction of
`|V|^{p-2}V\otimes V` determined by the original `*` contractions.

**This IS of the signed form (1.1).**  The A03 Step 38 lemma applies:
\[
|I_{\rm top}|\le\varepsilon D_{1,p}^U
+C_{p,\varepsilon}\|C_1\|_\infty^2\|V\|_p^p.
\tag{2.16}
\]

**Resolution:** The apparent m=1 circular term `I_{\rm top}` from the
`B_3*U_0` source is, after integration by parts and before taking absolute
values, of the signed-Hessian form.  The signed-Hessian lemma closes it.

### 2.6 The m=1 Hessian term from §2.1–2.2

The `B_2*V` terms from §2.1 and §2.2:
\[
|V|^{p-2}V*(B_2*V).
\]
Expanding `B_2=2\chi C_2+2C_1*C_1`:
\[
2\chi|V|^{p-2}V*C_2*V+2|V|^{p-2}V*C_1*C_1*V.
\]
The second is bounded.  The first:
\[
2\int\chi\nabla_i\nabla_j\chi\,\widetilde{\mathcal B}^{ij}(V),
\tag{2.17}
\]
where `\widetilde{\mathcal B}^{ij}(V)` is the contraction of
`|V|^{p-2}V\otimes V`.  This is also of the signed form (1.1) and is
controlled by the A03 lemma.

### 2.7 Remaining sources

The remaining differentiated terms from (2.11) are:

1. `\nabla(4(C_1*C_1)*U)=4(C_2*C_1)*U+4(C_1*C_1)*V`.
   First: `C_2*C_1*U_0` — paired with `|V|^{p-2}V`, gives
   `\int C_1*C_2*U_0*|V|^{p-2}V`.  **Direct Young bound** (no integration
   by parts): with exponents `(p,p/(p-1))`,
   \[
   \int|C_1||C_2||U_0||V|^{p-1}
   \le\|C_1\|_\infty\|U_0\|_\infty\bigl(\|C_2\|_p^p+\|V\|_p^p\bigr).
   \tag{2.18}
   \]
   This is immediately controlled by the coupled norms.  Integration by
   parts on `C_2=\nabla C_1` is **not** used here because it produces an
   unweighted `\nabla V` factor that cannot be absorbed by the
   `\chi^2`-weighted diffusion.

2. `\nabla(U*U)=V*U_0`.  Bounded coefficient `U_0\in L^\infty`.

3. `\nabla(aU)=B_1*U_0+aV`.  Both bounded.

4. The curvature commutator `aT*V` from §2.1.  This is
   `aT*V=U_0*T_0` up to the `aT=U` identity.  Actually `aT=U`, so
   `aT*V=U_0*V`, bounded.

   Wait — the curvature commutator in (2.4) is `aT*V` where `T` is the
   full shifted curvature.  Using `aT=U`:
   \[
   aT*V=U*V=U_0*V.
   \]
   This has bounded coefficient `U_0`.  No problem.

### 2.8 Summary of m=1 energy terms

Testing the differentiated equation against `|V|^{p-2}V`, the complete
list of non-trivial integrals is:

| Source | Term | Mechanism |
|--------|------|-----------|
| Principal (§2.1) | `B_2*V` → `\chi C_2*V*V` | Signed-Hessian lemma |
| Drift (§2.2) | `B_2*V` → `\chi C_2*V*V` | Signed-Hessian lemma |
| Hessian (§2.3) | `B_3*U_0` → `\chi C_3*U_0` → IBP → `\chi C_2*V*V` | Signed-Hessian lemma |
| Hessian (§2.3) | `C_1*C_2*U_0` | Young, bounded `C_1,U_0` |
| (C₁C₁)U (§2.7.1) | `C_2*C_1*U_0` | Direct Young (2.18), no IBP |
| Reaction (§2.7.2) | `V*U_0` | Bounded coefficient |
| Linear (§2.7.3) | `B_1*U_0+aV` | Bounded |
| Curv. comm. (§2.7.4) | `aT*V=U_0*V` | Bounded coefficient |
| Principal (§2.1) | `B_1*\nabla V` | Diffusion absorption |
| Drift (§2.2) | `B_1*\nabla V` | Diffusion absorption |

Every signed-Hessian contraction is of the form
\[
\int\chi\nabla_i\nabla_j\chi\,\mathcal B^{ij}(V),
\quad|\mathcal B|\le C|V|^p,\quad|\nabla\mathcal B|\le Cp|V|^{p-1}|\nabla V|,
\]
and the A03 lemma gives
\[
\le\varepsilon D_{1,p}^U+C_{p,\varepsilon}\|C_1\|_\infty^2\|V\|_p^p.
\]

**Conclusion:** No genuinely circular term survives at m=1.  All apparent
obstructions resolve through the signed-Hessian lemma applied to the
actual tensor contractions.

---

## 3. The C₂ evolution equation

### 3.1 Derivation from the connection evolution

The Christoffel symbols evolve by
\[
\partial_t\Gamma^k_{ij}
=\frac12g^{kl}(\nabla_i\partial_tg_{jl}+\nabla_j\partial_tg_{il}
-\nabla_l\partial_tg_{ij}).
\]
With `\partial_tg=-2aE`:
\[
\partial_t\Gamma=g^{-1}*\nabla(aE).
\]
Now `aE=\operatorname{Ric}(U)` is a contraction of `U`:
\[
\nabla(aE)=\nabla\operatorname{Ric}(U)=g^{-1}*\nabla U=g^{-1}*U_1.
\tag{3.1}
\]
Therefore
\[
\partial_t\Gamma=g^{-1}*U_1.
\tag{3.2}
\]

### 3.2 Evolution of C₂

Since `C_2=\nabla^2\chi` and `\chi` is a fixed spatial function:
\[
\partial_tC_2=\partial_t\nabla^2\chi.
\]
The covariant derivative `\nabla` depends on `g(t)`, so
\[
\partial_t(\nabla^2\chi)=\nabla^2(\partial_t\chi)+[\partial_t,\nabla^2]\chi.
\]
Since `\chi` is fixed, `\partial_t\chi=0`.  The commutator:
\[
[\partial_t,\nabla^2]\chi=(\partial_t\Gamma)*\nabla\chi
=g^{-1}*U_1*C_1.
\tag{3.3}
\]

Therefore
\[
\boxed{\partial_tC_2=g^{-1}*U_1*C_1.}
\tag{3.4}
\]

**No U₂ appears.**  The C₂ evolution involves only `U_1` (the base-pair
partner) and `C_1` (bounded).  Testing against `|C_2|^{p-2}C_2`, including the time variation of the
metric norm and volume form:
\[
\frac{d}{dt}\|C_2\|_p^p
\le C\|U_1\|_p\|C_1\|_\infty\|C_2\|_p^{p-1}
+C\|U_0\|_\infty\|C_2\|_p^p.
\tag{3.5}
\]

The second term comes from `\partial_t g=-2\operatorname{Ric}(U)` and
`U_0\in L^\infty` (I1).  By Young:
\[
\le C(\|V\|_p^p+\|C_2\|_p^p).
\tag{3.6}
\]

---

## 4. Coupled base-pair energy inequality

Combining §2.8 and §3.2, the coupled system for `(V,Z)=(U_1,C_2)` is:
\[
\begin{aligned}
\frac{d}{dt}\|V\|_p^p+cD_{1,p}^U
&\le C_{p,\tau}(1+\|V\|_p^p)+C_{p,\tau}\|C_2\|_p^p,\\
\frac{d}{dt}\|Z\|_p^p&\le C(\|V\|_p^p+\|Z\|_p^p).
\end{aligned}
\tag{4.1}
\]

Adding:
\[
\frac{d}{dt}(\|V\|_p^p+\|Z\|_p^p)+cD_{1,p}^U
\le C_{p,\tau}(1+\|V\|_p^p+\|Z\|_p^p).
\tag{4.2}
\]

By Grönwall on `[\tau,t]`:
\[
\boxed{
\|U_1(t)\|_p^p+\|C_2(t)\|_p^p
\le e^{C_{p,\tau}(t-\tau)}
\bigl(\|U_1(\tau)\|_p^p+\|C_2(\tau)\|_p^p+C_{p,\tau}(t-\tau)\bigr).}
\tag{4.3}
\]

**Initial data:** At `t=\tau`, the solution is smooth, so
`\|U_1(\tau)\|_p` and `\|C_2(\tau)\|_p` are finite per-datum constants.
The estimate (4.3) propagates these bounds to all `t\in[\tau,T_*)`.

---

## 5. T₁ derivation from the base pair

### 5.1 The T-equation

The unweighted shifted curvature satisfies
\[
\partial_tT=a\Delta T+B_1*\nabla T+aT*T+aT.
\tag{5.1}
\]
Differentiating once and setting `W=T_1=\nabla T`:
\[
\partial_tW
=a\Delta W+B_1*\nabla W+B_2*T_0+B_1*W
+\nabla(aT*T)+\nabla(aT)+[\nabla,a\Delta]T.
\tag{5.2}
\]

The commutator `[\nabla,a\Delta]T=aT*W+B_1*T_0*T_0+\cdots` produces
`aT*W` and lower terms.

### 5.2 Conversion of aT₁

The key term is `aW=aT_1`.  Using
\[
aT_1=U_1-B_1*T_0,
\tag{5.3}
\]
which follows from `\nabla U=\nabla(aT)=B_1*T+a\nabla T`, we get
\[
aW=V-B_1*T_0.
\tag{5.4}
\]

The right side uses the controlled `V=U_1` and bounded `B_1=2\chi C_1`
with `T_0\in L^q`.  Therefore `aW\in L^p` after the base pair is
controlled.  The unweighted equation (5.2) then has all source terms
controlled:
- `a\Delta W` gives dissipation `D_{1,p}^T=\int a|\nabla W|^2|W|^{p-2}`.
- `B_1*\nabla W` is absorbed by diffusion.
- `B_2*W` from differentiating the drift: `B_2*W=2\chi C_2*W+2C_1*C_1*W`.
  The `\chi C_2*W` portion is the m=1 signed-Hessian term for the
  T-equation, closed by the A03 lemma against
  `D_{1,p}^T=\int a|\nabla W|^2|W|^{p-2}` using `\|C_1\|_\infty`.
  The `C_1*C_1*W` part is bounded by `C\|C_1\|_\infty^2\|W\|_p^p`.
- `aT*W` becomes `U_0*W` after `aT=U`, bounded coefficient.
- `\nabla(aT*T)` and `\nabla(aT)` are lower-order, controlled by
  `T_0,W` and `B_1,T_0`.

Therefore
\[
\frac{d}{dt}\|W\|_p^p+cD_{1,p}^T
\le C_{p,\tau}(1+\|W\|_p^p).
\tag{5.5}
\]

### 5.3 Pointwise curvature

With `T_0\in L^p` (imported, (I2)) and `T_1\in L^p` (from §5.2), for
`p>4` the Sobolev embedding `W^{1,p}\hookrightarrow L^\infty` in
dimension four gives
\[
\|T_0(t)\|_{L^\infty}\le C_{\rm Sob}(\|T_0\|_p+\|T_1\|_p)<\infty.
\tag{5.6}
\]

---

## 6. Complete base-layer output

The base layer is now established in the non-circular order:
\[
\boxed{
(U_0\in L^\infty,\;T_0\in L^q_{\rm fin})
\to(U_1,C_2)\in L^p_{\rm fin}
\to T_1\in L^p_{\rm fin}
\to T_0\in L^\infty.}
\tag{6.1}
\]

All constants depend on the per-datum initial data at `\tau`, the cutoff
geometry, and the bootstrap parameters `(\Gamma,V)`.  No constant depends
on the sequence index `i` of the IL family.

The base-layer output is:
\[
\|U_1\|_p,\;\|C_2\|_p,\;\|T_1\|_p\le K_{1,p,\tau}<\infty,
\qquad\|T_0\|_\infty\le K_{0,\tau}<\infty,
\tag{6.2}
\]
for all finite `p`, uniformly on `[\tau,T_*)`.

---

## 7. Derivative-reordering lemma for the general induction

For the general `m\ge2` induction, the differentiated U-equation contains
`B_{m+2}*U_0` from the coefficient-derivative source.  Expanding:
\[
B_{m+2}=\nabla^{m+2}(\chi^2)=2\chi C_{m+2}
+\sum_{i=1}^{m+1}c_{i,m+2}C_i*C_{m+2-i}.
\tag{7.1}
\]

The top term `2\chi C_{m+2}*U_0` requires integration by parts.  The
reordering lemma states that when `\nabla^m\nabla^2a` is written as
`\nabla C_{m+1}` (i.e., one derivative is moved from the curvature to the
cutoff), every curvature commutator produced has strictly lower cutoff
and curvature indices.

**Lemma (derivative reordering).**  Let `m\ge2`.  In the differentiated
U-equation at level `m`, every occurrence of the highest cutoff jet
`C_{m+2}` is paired only with `U_0` (never with `U_j` for `j\ge1`), and
every curvature commutator from reordering `\nabla^m\nabla^2a` into
`\nabla C_{m+1}` involves only `T_{\le m-1}` and `C_{\le m}`.

**Proof sketch.**  The coefficient-derivative source at level `m` is
`\nabla^m(B_2*U)` where `B_2*U` is the Hessian-cutoff term in the
zero-order equation.  Applying Leibniz:
\[
\nabla^m(B_2*U)=\sum_{k=0}^m\binom mk B_{k+2}*U_{m-k}.
\]
The case `k=m` gives `B_{m+2}*U_0` (top cutoff with zero-order curvature).
The case `k=m-1` gives `B_{m+1}*U_1` (next cutoff with first-order
curvature).  All cases with `k\le m-2` give `B_{\le m}*U_{\ge2}`.

For `k=m`: `B_{m+2}=2\chi C_{m+2}+\cdots`, so the top term is
`2\chi C_{m+2}*U_0`.  No `U_j` with `j\ge1` appears paired with `C_{m+2}`.

For `k=m-1`: `B_{m+1}=2\chi C_{m+1}+\cdots`, so the next term is
`2\chi C_{m+1}*U_1`.  This is the `\chi C_{m+1}*U_1` current term from
the Step 59 ledger.

When integrating `2\chi C_{m+2}*U_0` by parts as `C_{m+2}=\nabla C_{m+1}`,
the derivative falls on the test function `|U_m|^{p-2}U_m` or on `\chi`
or on `U_0`.  The curvature commutators from reordering `\nabla^m\nabla^2`
involve `\operatorname{Rm}*\nabla^{\le m}` acting on `a` or `U`, producing
only `T_{\le m-1}` and `C_{\le m}` factors.

This completes the structural verification that the Step 59 ledger
correctly extracts all current-order terms.

---

## 8. Interface with the general induction

With the base layer (6.1)–(6.2) established, the general `m\ge2`
current-pair induction from Step 59 applies:

1. At each level `m\ge2`, the pair `(U_m,C_{m+1})` satisfies the coupled
   energy inequality (3.15) from the Step 59 note.
2. The critical residual `I_m=\int\chi|C_{m+1}||U_1||U_m|^{p-1}` is
   absorbed by Hölder `(4,p,4,2p/(p-2))` with `U_1` as base data (now
   established by this note).
3. The signed-Hessian term `\chi C_2*U_m` is controlled by the A03 lemma
   with `\|C_1\|_\infty` (no evolving `C_2` in `L^\infty`).
4. The unweighted `T_m` equation is then controlled using `aT_m=U_m-\sum B_q*T_{m-q}`.

The fixed-background conversion and autonomous splice from Steps 58–59
then give per-datum `C^\infty` continuation to the observation time
`T=\theta r^2`.

---

## 9. Relation to the full IL chain and Yau 26

This note closes the base-pair gap identified in Step 59.  The IL
analytic bridge now has the following status:

- **Base pair (this note):** proved at tensor-index level.  The signed-
  Hessian lemma closes all m=1 Hessian terms.  No circular residual
  survives.  The C₂ evolution produces only `U_1`, not `U_2`.
- **General induction (Step 59):** structurally verified with the
  corrected ledger.  The derivative-reordering lemma (§7 above) confirms
  that the highest cutoff jet `C_{m+2}` is paired only with `U_0/T_0`.
- **Remaining proof obligations:** (a) exact tensor-index evolution
  formulas for the general `U_m` and `T_m` equations including time
  variation of norms and volume forms; (b) complete energy estimates for
  all remainder families; (c) fixed-background Sobolev product estimates;
  (d) audit of the imported Moser endpoints and local existence module.

The restricted IL theorem remains conditional on these items.  It does
not address the positive branch, general four-manifold topology,
dimensions `n\ge5`, dimension-only constants, or Lean formalization.

### Normal-form reconciliation with Step 59

The zero-order T-equation (5.1) in this note uses the normal form
`\partial_tT=a\Delta T+B_1*\nabla T+aT*T+aT`, which does not display a
separate `B_2*T` term.  Step 59's normal form (4.1) includes `B_2*T`
explicitly.  These are consistent: the `B_2*T` in Step 59's form is
absorbed into the `a\Delta T` term here via the product rule
`a\Delta T=\Delta(aT)-2\nabla a\cdot\nabla T-(\Delta a)T`, where
`(\Delta a)T=B_2*T`.  If `B_2*T` is displayed explicitly, its m=1
descendant `\chi C_3*T_0` closes by the same IBP + signed-Hessian
mechanism as the U-side, since `\nabla T_0=W=T_1` gives the required
`|W|^{p-2}W\otimes W` bilinear form.
