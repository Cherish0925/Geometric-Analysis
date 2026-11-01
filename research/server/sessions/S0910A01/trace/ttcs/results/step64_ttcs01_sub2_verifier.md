# TTCS Independent Branch Record

```json
{
  "step_id": 64,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step64_convention_consistency_sweep.md",
    "Sessions/S0910A01/workspace/notes/step63_curvature_variation_index_proof.md",
    "Sessions/S0910A01/workspace/notes/step54_first_exit_continuation_derivation.md",
    "Sessions/S0910A01/workspace/notes/step58_all_order_continuation_proof.md"
  ]
}
```

## Task

Cross-note sign-convention consistency audit for a Riemannian flow proof. The shifted curvature used in an Ishida-LeBrun cutoff-flow proof was redefined in the newest note (Step 63) as T = Rm - G with G = (g KN g)/(2(n-1)) under the standard Kulkarni-Nomizu product, giving Ric(G) = -g, Ric(T) = E, nabla T = nabla Rm. All earlier notes (Steps 34,43,54,55,58,59,60) wrote T = Rm + G with the SAME auxiliary properties Ric(T)=E, nabla T = nabla Rm, |G|^2 = n/(2(n-1)). The sweep note claims: (a) the two conventions define the SAME tensor T (legacy G_old = -G); (b) |G|^2 and F_T=(1+|T|^2)^{1/2} asymptotic F=(1+|Rm|^2)^{1/2} are sign-invariant; (c) all energies H_2, K_p, Y, Gamma and dissipations built from F_T or |Rm| are numerically unchanged; (d) the U=aT evolution conversion uses only the sign-free cancellation d_t U = a d_t T, so the continuation equations are unaffected. Read the sweep note plus the Step 63 anchor and the legacy Step 54/58 notes. Verify or refute claims (a)-(d) rigorously at the tensor level. Specifically: is it TRUE that requiring Ric(T)=E and nabla T = nabla Rm forces the same T regardless of the G sign? Are there any displayed equations in the legacy notes whose SIGN genuinely flips (not just relabels) under one consistent convention? Identify any compensating-error risk the sweep missed.

## Output

## Verification memo: shifted-curvature sign convention in the IL cutoff-flow notes

### 1. Fixed algebra under the Step 63 convention

Use the Step 63 Kulkarni–Nomizu convention

\[
(\varphi\owedge\psi)_{ijkl}
=\varphi_{ik}\psi_{jl}+\varphi_{jl}\psi_{ik}
-\varphi_{il}\psi_{jk}-\varphi_{jk}\psi_{il},
\]

and the Ricci contraction

\[
\operatorname{Ric}_{jk}(A)=g^{il}A_{ijkl}.
\]

For the metric tensor,

\[
(g\owedge g)_{ijkl}=2(g_{ik}g_{jl}-g_{il}g_{jk}).
\]

Let

\[
G=\frac{1}{2(n-1)}(g\owedge g)
=\frac{1}{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}).
\]

Then

\[
g^{il}G_{ijkl}
=\frac{1}{2(n-1)}g^{il}(g\owedge g)_{ijkl}
=\frac{1}{2(n-1)}\bigl(2g_{jk}-2n g_{jk}\bigr)
=-g_{jk}.
\]

Thus

\[
\operatorname{Ric}(G)=-g.
\]

With

\[
T=\operatorname{Rm}-G,
\]

one obtains

\[
\operatorname{Ric}(T)=\operatorname{Ric}(\operatorname{Rm})-\operatorname{Ric}(G)
=\operatorname{Ric}+g=E,
\]

and, since \(\nabla g=0\),

\[
\nabla G=0,\qquad \nabla T=\nabla\operatorname{Rm}.
\]

This is the canonical convention.

---

## 2. Item-by-item tensor verification

### (a) Do the two conventions define the same tensor \(T\)?

**Answer: yes, but only after the legacy auxiliary tensor is identified as \(G_{\rm old}=-G\). The two properties \(\operatorname{Ric}(T)=E\) and \(\nabla T=\nabla\operatorname{Rm}\) alone do not force this without the algebraic restriction on \(G\).**

Suppose the legacy convention writes

\[
T_{\rm old}=\operatorname{Rm}+G_{\rm old}
\]

and still requires

\[
\operatorname{Ric}(T_{\rm old})=E=\operatorname{Ric}+g,
\qquad
\nabla T_{\rm old}=\nabla\operatorname{Rm}.
\]

Then

\[
\operatorname{Ric}(G_{\rm old})=+g,
\qquad
\nabla G_{\rm old}=0.
\]

If \(G_{\rm old}\) is required to be a universal multiple of \(g\owedge g\) with the Step 63 KN product, say

\[
G_{\rm old}=c\,(g\owedge g),
\]

then

\[
\operatorname{Ric}(G_{\rm old})
=-2c(n-1)g.
\]

The condition \(\operatorname{Ric}(G_{\rm old})=+g\) forces

\[
-2c(n-1)=1,
\qquad
c=-\frac{1}{2(n-1)}.
\]

Hence

\[
G_{\rm old}
=-\frac{1}{2(n-1)}(g\owedge g)
=-G.
\]

Therefore

\[
T_{\rm old}
=\operatorname{Rm}+G_{\rm old}
=\operatorname{Rm}-G
=T.
\]

So the tensor \(T\) is identical under the two conventions **provided** the legacy symbol \(G\) is interpreted as the opposite of the canonical \(G\).

However, the properties

\[
\operatorname{Ric}(T)=E,\qquad \nabla T=\nabla\operatorname{Rm}
\]

by themselves only force

\[
\operatorname{Ric}(G_{\rm old})=g,\qquad \nabla G_{\rm old}=0.
\]

Without assuming that \(G_{\rm old}\) is the universal metric KN tensor, those conditions do not uniquely determine \(G_{\rm old}\). The identification \(G_{\rm old}=-G\) relies on the algebraic form of \(G\).

There is also a literal-display issue: if a legacy note writes

\[
T=\operatorname{Rm}+G,
\qquad
G=\frac{1}{2(n-1)}(g\owedge g),
\]

and simultaneously uses the Step 63 KN product and Ricci contraction, then those displayed equations give

\[
\operatorname{Ric}(T)=\operatorname{Ric}-g,
\]

not \(E=\operatorname{Ric}+g\). Thus the legacy displays are mutually consistent only if the symbol \(G\) in those notes is understood as \(-G_{\rm canonical}\), or if the legacy notes used the opposite KN/Ricci convention. The tensor \(T\) can be made identical, but the literal \(G\)-formulae cannot all be copied unchanged into the canonical convention.

---

### (b) Is \(|G|^2\) and the equivalence \(F_T\asymp F\) sign-invariant?

**Answer: yes.**

Since

\[
G_{\rm old}=-G,
\]

one has

\[
|G_{\rm old}|^2=|G|^2.
\]

The numerical value

\[
|G|^2=\frac{n}{2(n-1)}
\]

is therefore unchanged by the sign reflection, assuming the same curvature-tensor norm is used throughout. The value itself depends on the norm convention; with the full \((0,4)\)-tensor norm one would get a different factor. The notes’ value corresponds to the curvature norm convention used in the bridge. That is a norm-convention point, not a sign point.

For the equivalence with

\[
F=(1+|\operatorname{Rm}|^2)^{1/2},
\qquad
F_T=(1+|T|^2)^{1/2},
\]

the sign of the shift is irrelevant. Since \(|G|\) is a dimension-only constant,

\[
\bigl||T|-|\operatorname{Rm}|\bigr|\le |G|.
\]

Thus there exist dimension-only constants \(c_n,C_n>0\) such that

\[
c_n(1+|\operatorname{Rm}|^2)
\le
1+|T|^2
\le
C_n(1+|\operatorname{Rm}|^2).
\]

Equivalently,

\[
c_n F^2\le F_T^2\le C_nF^2.
\]

If \(G_{\rm old}=-G\), then \(T_{\rm old}=T\), so \(F_T\) is not merely equivalent but exactly the same function. If one instead reads the legacy formula literally as \(T=\operatorname{Rm}+G_{\rm canonical}\), then \(T\) differs from the canonical \(T\) by \(2G\); the equivalence \(F_T\asymp F\) still holds, but the pointwise energy is not identical.

---

### (c) Are the energies \(H_2,K_p,Y,\Gamma\) and dissipations unchanged?

**Answer: exactly unchanged if the legacy \(G\) is interpreted as \(-G\); only comparable, not identical, if the legacy plus sign is read literally with canonical \(G\).**

Under \(G_{\rm old}=-G\),

\[
T_{\rm old}=T,
\qquad
\nabla T_{\rm old}=\nabla T=\nabla\operatorname{Rm}.
\]

Therefore every energy built from \(T\), \(F_T\), or \(|\nabla\operatorname{Rm}|\) is identical:

\[
H_2=\int\eta^2F_T^2\,d\mu,
\]

\[
K_p^\eta=\int\eta^2a^{p-2}F_T^p\,d\mu,
\]

\[
Y=\int\eta^2aF_T^3\,d\mu,
\]

\[
\Gamma=\max_\alpha\sup \mathcal S\,H_{2,\alpha}^{1/2},
\]

and the dissipations such as

\[
D_2=\int\eta^2a|\nabla\operatorname{Rm}|^2\,d\mu
\]

are unchanged.

If, however, a legacy display is read as

\[
T=\operatorname{Rm}+G_{\rm canonical},
\]

then the tensor is shifted by \(2G\) relative to the canonical \(T\). Because \(G\) is bounded, the energies remain dimensionally comparable, but they are not numerically identical. The sweep’s “numerically unchanged” conclusion is therefore correct under the reinterpretation \(G_{\rm old}=-G\), but not under a literal copy of the plus-sign formula with the canonical \(G\).

---

### (d) Is the conversion to \(U=aT\) sign-free?

**Answer: the conversion identity itself is sign-free; explicit \(G\)-evolution displays are not.**

Since \(a=\chi^2\) is a fixed spatial function,

\[
\partial_t U=\partial_t(aT)=a\,\partial_t T.
\]

This identity does not involve \(G\) and is unaffected by the sign convention.

But the evolution of \(T\) itself does involve \(\partial_t G\). Under the canonical convention,

\[
\partial_t T=\partial_t\operatorname{Rm}-\partial_t G.
\]

Under the legacy convention with \(G_{\rm old}=-G\),

\[
\partial_t T=\partial_t\operatorname{Rm}+\partial_t G_{\rm old}.
\]

These are the same identity after substituting \(G_{\rm old}=-G\), but the explicit sign in any displayed formula for \(\partial_t G\) changes.

From Step 63,

\[
\partial_t(g\owedge g)=2(h\owedge g),
\]

and for \(h=-2aE\),

\[
\partial_t G
=
-\frac{2a}{n-1}(E\owedge g).
\]

For the legacy tensor \(G_{\rm old}=-G\),

\[
\partial_t G_{\rm old}
=
+\frac{2a}{n-1}(E\owedge g).
\]

Thus any legacy display of \(\partial_t G\) must acquire the opposite sign when rewritten in canonical \(G\). The \(U\)-equation itself, if written purely in terms of \(U\), \(T\), \(a\), and star-products, can be convention-independent. But any derivation step that refers explicitly to \(G\), or to the stationary condition \(T=0\), must be rewritten.

---

## 3. Displays whose sign genuinely changes under the canonical convention

The following are not mere cosmetic relabelings if the canonical \(G\) is used.

1. **Definition of \(T\).**  
   Legacy:

   \[
   T=\operatorname{Rm}+G_{\rm old}.
   \]

   Canonical:

   \[
   T=\operatorname{Rm}-G.
   \]

   If one keeps the canonical formula

   \[
   G=\frac{1}{2(n-1)}(g\owedge g),
   \]

   then the plus sign in the legacy definition must become a minus sign.

2. **Stationarity display.**  
   Legacy Step 58 says, in effect,

   \[
   T=0\implies \operatorname{Rm}=-G.
   \]

   With canonical \(G\),

   \[
   T=0\implies \operatorname{Rm}=+G.
   \]

   The consequence

   \[
   \operatorname{Ric}=-g,\qquad E=0
   \]

   remains correct, because \(\operatorname{Ric}(G)=-g\).

3. **Cross term in \(|T|^2\).**  
   Canonical:

   \[
   |T|^2
   =
   |\operatorname{Rm}|^2
   -2\langle \operatorname{Rm},G\rangle
   +|G|^2.
   \]

   Legacy, with \(G_{\rm old}\):

   \[
   |T|^2
   =
   |\operatorname{Rm}|^2
   +2\langle \operatorname{Rm},G_{\rm old}\rangle
   +|G_{\rm old}|^2.
   \]

   The two agree after \(G_{\rm old}=-G\), but the sign written in front of the inner product changes.

4. **Evolution of \(G\).**  
   Canonical:

   \[
   \partial_t G
   =
   -\frac{2a}{n-1}(E\owedge g).
   \]

   Legacy:

   \[
   \partial_t G_{\rm old}
   =
   +\frac{2a}{n-1}(E\owedge g).
   \]

5. **Any formula saying \(T=\operatorname{Rm}+G\) while also defining \(G=(g\owedge g)/(2(n-1))\) under the Step 63 KN product.**  
   Those two displays together are incompatible with \(\operatorname{Ric}(T)=E\). One must either replace \(G\) by \(-G\) or change the KN/Ricci convention.

---

## 4. Compensating-error risks not removed by the sign sweep

### 4.1 The sweep’s “same tensor” conclusion depends on a silent reflection of \(G\)

The tensor \(T\) is the same only if the legacy symbol \(G\) is interpreted as \(-G_{\rm canonical}\). If a later writeup copies a legacy formula such as

\[
G=\frac{1}{2(n-1)}(g\owedge g),
\qquad
T=\operatorname{Rm}+G
\]

while also using the Step 63 KN product and Ricci contraction, then the resulting \(T\) is not the canonical one and does not satisfy \(\operatorname{Ric}(T)=E\). The final theorem writeup must define \(G\) once, canonically, and then rewrite every legacy occurrence of \(G\) with the opposite sign.

### 4.2 If the legacy convention came from an opposite KN product, all KN signs must be checked

One way for the legacy notes to obtain \(\operatorname{Ric}(G_{\rm old})=+g\) while writing the same formal expression is to use the opposite KN product. If that happened, then not only \(G\) but every KN product display may have the opposite sign. This includes terms such as

\[
(\nabla^2 a)\owedge g,
\]

and algebraic curvature terms appearing in the variation formulae. The final estimates often use absolute values, so many such sign changes do not alter constants, but any signed cancellation or explicitly written structural identity must be recomputed under the Step 63 KN convention.

### 4.3 A coefficient mismatch in the Step 63 pure-scaling computation

There is a separate coefficient issue in Step 63, independent of the plus/minus convention.

Step 63 gives

\[
G=\frac{1}{2(n-1)}(g\owedge g),
\]

and

\[
\partial_t(g\owedge g)=2(h\owedge g).
\]

For the pure-scaling variation \(h=-2g\),

\[
\partial_t(g\owedge g)
=
2((-2g)\owedge g)
=
-4(g\owedge g).
\]

Therefore

\[
\partial_t G
=
\frac{1}{2(n-1)}(-4(g\owedge g))
=
-4G.
\]

But the normalization passage in Step 63 states, in effect,

\[
\partial_t G=-2G.
\]

With the displayed all-lower \(G\), the coefficient is \(-4\), not \(-2\). The statement \(\partial_t G=-2G\) would require either a different definition of \(G\), a different product rule, or a mixed-index version of \(G\). As written, the pure-scaling checksum for \(T\) does not verify the displayed all-lower formula.

This does not automatically change the Moser estimates, because algebraic reaction terms are absorbed into a term of the form \(CaF_T^3\). But it means the exact normalization check is not currently valid as written, and a coefficient in the algebraic part of \(\partial_t T\) may be different from the one recorded. This is precisely the kind of compensating possibility that a sign-only sweep can miss.

### 4.4 The linear term in the \(T\)-equation should be rechecked after the sign reflection

Step 58 records a structural equation of the form

\[
\partial_t T
=
a\Delta T
+B_1*\nabla T
+B_2*T
+a(T*T+T).
\]

The linear term \(aT\) is described using the stationary reference. In the legacy convention that reference was written as \(\operatorname{Rm}=-G\). In the canonical convention it is

\[
\operatorname{Rm}=+G.
\]

Because the tensor \(T\) is the same, the final \(T\)-only equation may still be correct, but the derivation of the coefficient of the linear term should be recomputed under the canonical convention. The sign sweep does not itself re-derive that coefficient.

### 4.5 Norm convention for \(|G|^2\)

The value

\[
|G|^2=\frac{n}{2(n-1)}
\]

matches a curvature norm convention with a factor \(1/4\) relative to the raw full \((0,4)\)-tensor norm. If any note uses the raw norm, the numerical constants in \(F_T\), \(H_2\), and the absorption parameters shift by a fixed dimension-only factor. This is not a sign issue, but it can combine with the sign reflection to hide a constant mismatch.

---

## 5. Net verdict

At the level of the tensor \(T\) and the analytic energies, the sweep’s main conclusion is correct **after** the identification

\[
G_{\rm old}=-G_{\rm canonical}.
\]

Under that identification:

\[
T_{\rm old}=T_{\rm canonical},
\]

\[
|G_{\rm old}|^2=|G_{\rm canonical}|^2,
\]

\[
F_T\asymp F
\]

is sign-independent, and the energies

\[
H_2,\ K_p,\ Y,\ \Gamma
\]

and dissipations are unchanged. The conversion

\[
\partial_t U=a\,\partial_t T
\]

is sign-free.

However, the literal legacy displays are not all invariant as written. Every formula containing \(G\) explicitly must be rewritten with the opposite sign if the canonical KN product is adopted. In particular:

\[
T=\operatorname{Rm}+G
\quad\longrightarrow\quad
T=\operatorname{Rm}-G,
\]

\[
T=0\implies \operatorname{Rm}=-G
\quad\longrightarrow\quad
T=0\implies \operatorname{Rm}=+G,
\]

and

\[
\partial_t G_{\rm old}=+\frac{2a}{n-1}(E\owedge g)
\quad\longrightarrow\quad
\partial_t G=-\frac{2a}{n-1}(E\owedge g).
\]

In addition, Step 63 contains a separate coefficient mismatch in the pure-scaling computation of \(\partial_t G\): with the displayed all-lower \(G\), the factor should be \(-4G\), not \(-2G\). That point should be corrected or explained by adopting a mixed-index version of \(G\). Until that is done, the normalization checksum does not fully verify the algebraic part of the \(T\)-evolution.