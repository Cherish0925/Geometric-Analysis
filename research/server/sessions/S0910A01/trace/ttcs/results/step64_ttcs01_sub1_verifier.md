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

## Verifier memo: Kulkarni–Nomizu sign reflection

### Overall finding

Assertions (a)–(d) are substantially correct **after a global reflection of the legacy auxiliary tensor**, but they are not correct as statements about the literal legacy formulas under one fixed standard Kulkarni–Nomizu product.

The main conclusions are:

- The reflection \(G_{\mathrm{old}}=-G\) does make the legacy and canonical \(T\) identical.
- The listed energies, dissipations, absorption parameters, and the \(U=aT\) conversion are unchanged.
- The sweep nevertheless missed:
  1. a sign inconsistency in its own norm-expansion display, Step 64 (2.6);
  2. a second \( \operatorname{Rm}=-G \) occurrence in Step 58 §2.2;
  3. a factor-two error in Step 63’s pure-scaling treatment of \(\partial_tG\), \(\partial_tT\), and \(\partial_t|T|^2\);
  4. an unresolved factor-four normalization question for \(|G|^2\);
  5. the need to recompute the exact zero-order \(Q(\operatorname{Rm})\) and \(\partial_tG\) collection under the canonical relation \(\operatorname{Rm}=T+G\).

None of items 1–5 changes the sign of diffusion or dissipation, the form of the Moser inequalities, or the convention-independence of the listed energies. They do affect exact tensor identities and scaling tests cited in support of the continuation equations.

---

## 1. Canonical tensor identities

With Step 63’s convention

\[
(\varphi\owedge\psi)_{ijkl}
=\varphi_{ik}\psi_{jl}+\varphi_{jl}\psi_{ik}
-\varphi_{il}\psi_{jk}-\varphi_{jk}\psi_{il},
\]

one has

\[
(g\owedge g)_{ijkl}
=2(g_{ik}g_{jl}-g_{il}g_{jk})
\]

and

\[
G_{ijkl}
=\frac1{2(n-1)}(g\owedge g)_{ijkl}
=\frac1{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}).
\]

Using Step 63’s Ricci contraction \(R_{jk}=g^{il}R_{ijkl}\),

\[
g^{il}G_{ijkl}
=\frac1{n-1}(g_{jk}-ng_{jk})
=-g_{jk}.
\]

Thus

\[
\operatorname{Ric}(G)=-g,\qquad
\nabla G=0,\qquad
\operatorname{Ric}(\operatorname{Rm}-G)
=\operatorname{Ric}+g=E.
\]

The canonical tensor is therefore

\[
\boxed{T=\operatorname{Rm}-G.}
\]

### Legacy reflection

Write the legacy auxiliary tensor as \(\widetilde G\). The legacy definition and Ricci identity are

\[
T_{\mathrm{old}}=\operatorname{Rm}+\widetilde G,
\qquad
\operatorname{Ric}(T_{\mathrm{old}})=\operatorname{Ric}+g.
\]

Consequently

\[
\operatorname{Ric}(\widetilde G)=+g.
\]

The reflection

\[
\boxed{\widetilde G=-G}
\]

gives

\[
T_{\mathrm{old}}
=\operatorname{Rm}+\widetilde G
=\operatorname{Rm}-G
=T.
\]

This is the coherent cross-note identification.

---

## 2. Do \(\operatorname{Ric}(T)=E\) and \(\nabla T=\nabla\operatorname{Rm}\) alone force the same \(T\)?

Not by themselves.

The two identities imply

\[
\operatorname{Ric}(\widetilde G)=+g,
\qquad
\nabla\widetilde G=0.
\]

The canonical choice \(\widetilde G=-G\) satisfies both, but uniqueness does not follow from these two conditions alone. For example, on a flat four-torus, let \(K\) be a nonzero constant Weyl tensor. Then

\[
\nabla K=0,\qquad \operatorname{Ric}(K)=0,
\]

so

\[
\widetilde G=-G+K
\]

also has \(\operatorname{Ric}(\widetilde G)=+g\) and \(\nabla\widetilde G=0\), while

\[
T_{\mathrm{old}}=\operatorname{Rm}-G+K
\]

differs from \(T\).

The full legacy package stated in the task is stronger: it also gives the same pointwise norm \(|G|^2\). If \(\widetilde G\) is an algebraic curvature tensor, then

\[
\widetilde G=-G+W,
\]

where \(W=\widetilde G+G\) is Ricci-free and hence purely Weyl. The curvature decomposition is orthogonal, so

\[
|\widetilde G|^2
=
|-G+W|^2
=
|G|^2+|W|^2.
\]

Requiring \(|\widetilde G|^2=|G|^2\) forces \(W=0\). Thus:

\[
\boxed{
\text{Ric identity}+\text{parallel identity alone do not force uniqueness,}
}
\]

but

\[
\boxed{
\text{those identities plus the algebraic curvature structure and the same pointwise norm do.}
}
\]

Equivalently, the explicit legacy KN formula—read with the reflected product—already fixes \(\widetilde G=-G\).

---

## 3. Assessment of assertions (a)–(d)

### (a) Same tensor

Correct, under the reflection \(\widetilde G=-G\).

There is, however, a literal-text issue. Step 58 (1.2) writes

\[
T=\operatorname{Rm}+G,\qquad G=(g\owedge g)/6
\]

without defining an opposite KN product. If that \(G\) is read using Step 63’s standard product, then

\[
\operatorname{Ric}(\operatorname{Rm}+G)
=\operatorname{Ric}-g
=E-2g,
\]

not \(E\). Therefore one of the following two readings is required:

1. the legacy KN product was the negative of Step 63’s product; or
2. the legacy \(T=\operatorname{Rm}+G\) display contained an actual sign error.

The sweep adopts the first reading retroactively. That makes the analysis coherent, but it is not accurate to describe the original displays as already convention-consistent without that reinterpretation.

### (b) Norm and \(F_T\asymp F\)

The equality

\[
|-G|^2=|G|^2
\]

is immediate. Also, for either sign,

\[
|\operatorname{Rm}\pm G|^2
=
|\operatorname{Rm}|^2
\pm2\langle\operatorname{Rm},G\rangle
+|G|^2.
\]

Since \(|G|=C_n\),

\[
c_n(1+|\operatorname{Rm}|^2)
\le
1+|\operatorname{Rm}\pm G|^2
\le
C_n(1+|\operatorname{Rm}|^2).
\]

Hence

\[
\boxed{F_T\asymp_nF}
\]

in either convention.

A precision matters here: \(F_T\) is exactly unchanged only under the simultaneous map

\[
(\widetilde G,\operatorname{Rm}+\widetilde G)
\longmapsto
(G,\operatorname{Rm}-G).
\]

It is not pointwise unchanged if one flips \(G\) while keeping \(T=\operatorname{Rm}-G\) fixed. The equivalence \(F_T\asymp F\) survives either way, but the equality of energies relies on the simultaneous reflection.

### (c) Energies and dissipations

Correct under the simultaneous reflection. The tensors entering the energies are identical:

\[
H_2=\int\eta^2F_T^2\,d\mu,\qquad
K_p=\int\eta^2a^{p-2}F_T^p\,d\mu,
\]

\[
Y=\int\eta^2aF_T^3\,d\mu,\qquad
\Gamma=\sup\mathcal S H_2^{1/2}.
\]

Likewise,

\[
\nabla T=\nabla\operatorname{Rm}
\]

in both conventions, so the Bochner and radial dissipations built from \(|\nabla T|\), \(|\nabla\operatorname{Rm}|\), or \(|\nabla F_T|\) are numerically unchanged. The defect energies \(J_p,Q_p\) contain no \(G\) at all.

No Moser absorption sign or \(\gamma=\mathcal S H_2^{1/2}\) parameter changes.

### (d) The \(U=aT\) conversion

Correct as a calculus identity. Since \(a=\chi^2\) is time-independent,

\[
\partial_tU=\partial_t(aT)=a\,\partial_tT.
\]

The conversion formulas

\[
\nabla U=a\nabla T+\nabla a*T,
\]

\[
\Delta U=a\Delta T+2\nabla a\cdot\nabla T+(\Delta a)T
\]

also contain no sign of \(G\).

What this identity does not establish is the exact algebraic collection of the \(\partial_tT\) equation. In particular, conversion of

\[
Q(\operatorname{Rm}),\qquad
\operatorname{Rm}*E,\qquad
\partial_tG
\]

to a \(T\)-equation uses the canonical relation

\[
\operatorname{Rm}=T+G
\]

rather than the legacy relation

\[
\operatorname{Rm}=T-\widetilde G.
\]

The zero-order cross terms are exactly where a compensating sign can enter without affecting coarse \(CaF_T^3\) bounds.

---

## 4. A stale sign inside Step 64 itself

Step 64 (2.6) displays, using the canonical symbol \(G\),

\[
1+|T|^2
=
1+|\operatorname{Rm}|^2
+2\langle\operatorname{Rm},G\rangle
+|G|^2.
\]

Under the canonical \(T=\operatorname{Rm}-G\), the correct expansion is

\[
\boxed{
|T|^2
=
|\operatorname{Rm}|^2
-2\langle\operatorname{Rm},G\rangle
+|G|^2.
}
\]

Under the legacy \(T=\operatorname{Rm}+\widetilde G\), the expansion is

\[
|T|^2
=
|\operatorname{Rm}|^2
+2\langle\operatorname{Rm},\widetilde G\rangle
+|\widetilde G|^2.
\]

These two displays are equal because \(\widetilde G=-G\). Step 64 (2.6) therefore appears to mix the canonical \(G\) with the legacy plus sign. The surrounding equivalence \(F_T\asymp F\) remains true in either sign convention, but the equality has a genuine sign error under the note’s own anchor convention.

This is precisely the kind of display that cannot be copied into the final writeup without repair.

---

## 5. Step 58 contains a second unpatched \(\operatorname{Rm}=-G\)

Step 64 repairs the Step 58 §2.1 sentence

\[
T=0\implies\operatorname{Rm}=-G.
\]

The same geometric relation occurs again in Step 58 §2.2, in the sentence describing the constant-curvature reference:

\[
\operatorname{Rm}=-G.
\]

Under the canonical convention this must be

\[
\boxed{\operatorname{Rm}=+G.}
\]

Indeed,

\[
T=\operatorname{Rm}-G=0
\iff
\operatorname{Rm}=G
\implies
\operatorname{Ric}=-g
\implies
E=\operatorname{Ric}+g=0.
\]

Under the legacy symbol, \(\operatorname{Rm}=-\widetilde G\) is equivalent to \(\operatorname{Rm}=+G\). Thus the underlying geometry is coherent after reflection, but the Step 58 §2.2 occurrence is still a canonical-sign repair that the sweep did not list.

A related display is Step 58 §4.1:

\[
a\nabla^m\operatorname{Rm}
=
a(T_m-\nabla^mG).
\]

With the canonical \(T=\operatorname{Rm}-G\), the algebraic relation is

\[
\nabla^m\operatorname{Rm}=T_m+\nabla^mG.
\]

For \(m\ge1\), \(\nabla^mG=0\), so both reduce to \(aT_m\); there is no numerical effect in the use made there. At \(m=0\), the relation is \(\operatorname{Rm}=T+G\), and the sign matters.

---

## 6. The Step 63 pure-scaling test contains a factor-two error

This is independent of the legacy sign reflection.

Step 63 correctly derives

\[
\partial_t(g\owedge g)=2(h\owedge g)
\]

and

\[
\partial_tG
=
\frac{h\owedge g}{n-1}
=
-\frac{2a}{n-1}(E\owedge g).
\tag{A}
\]

For the scaling test \(a\equiv1\), \(E=g\), equation (A) gives

\[
\partial_tG
=
-\frac2{n-1}(g\owedge g).
\]

But from the definition of \(G\),

\[
g\owedge g=2(n-1)G.
\]

Therefore

\[
\boxed{\partial_tG=-4G,}
\]

not \(-2G\) as written in Step 63 §3.6.

This is also immediate from homothetic scaling. If

\[
g(t)=e^{-2t}g_0,
\]

then \(G\) is quadratic in the metric, so

\[
G(t)=e^{-4t}G_0.
\]

The same scaling gives

\[
\operatorname{Rm}(t)=e^{-2t}\operatorname{Rm}_0,
\qquad
\partial_t\operatorname{Rm}=-2\operatorname{Rm},
\]

and hence

\[
\boxed{
\partial_tT
=
-2\operatorname{Rm}+4G
=
-2T+2G.
}
\]

Step 63 instead writes

\[
\partial_tT=-2T.
\]

### Concrete counterexample: flat torus

Take \((T^4,g_{\mathrm{flat}})\), \(a\equiv1\). Then

\[
E=g,\qquad \operatorname{Rm}=0,\qquad T=-G.
\]

Under \(g(t)=e^{-2t}g_0\),

\[
T(t)=-G(t)=e^{-4t}T_0.
\]

Thus

\[
\boxed{\partial_tT=-4T,}
\]

not \(-2T\). Moreover, because \(T\) scales like a \((0,4)\)-tensor with factor \(e^{-4t}\), while each of the four inverse metrics contributes \(e^{2t}\),

\[
|T(t)|_{g(t)}^2=|T_0|_{g_0}^2,
\]

so on the flat torus

\[
\boxed{\partial_t|T|^2=0,}
\]

not \(+4|T|^2\).

For a general Ricci-flat initial metric, which is precisely the condition \(E=g\), the correct pointwise identity is

\[
\boxed{
\partial_t|T|^2
=
4\langle\operatorname{Rm},T\rangle.
}
\]

Step 63’s +8 metric-variation contribution is correct; the tensor derivative used before it is not.

### Consequence

The error does not disturb the large inequality

\[
\partial_tF_T^2
\le
a\Delta F_T^2-2a|\nabla\operatorname{Rm}|^2+\cdots+CaF_T^3,
\]

because the corrected zero-order terms are still bounded by \(CaF_T^3\). It does invalidate the following exact statements in Step 63:

- \(\partial_tG=-2G\) in §3.6;
- \(\partial_tT=-2T\) in §3.6;
- the tensor part \(\partial_t|T|^2=-4|T|^2\) in §5.3;
- the conclusion \(\partial_t|T|^2=+4|T|^2\) in §5.3;
- the corresponding rows of the §9 scaling table.

This also removes the cited independent verification of the zero-order collection in the continuation \(T\)-equation.

---

## 7. Norm normalization is not reconciled

Step 64 and the earlier notes quote

\[
|G|^2=\frac{n}{2(n-1)}=\frac23\quad(n=4).
\]

Step 63 §5.1, however, defines the norm as the full tensor contraction

\[
|T|^2
=
g^{ip}g^{jq}g^{kr}g^{ls}
T_{ijkl}T_{pqrs}.
\]

With that full contraction,

\[
\left|g_{ik}g_{jl}-g_{il}g_{jk}\right|^2
=
2n(n-1),
\]

so

\[
\boxed{
|G|^2=\frac{2n}{n-1},
}
\]

which is \(8/3\) in dimension four. The quoted \(n/[2(n-1)]\) is exactly one quarter of the full contraction.

Thus one of the following conventions must be made explicit:

- use the full contraction and replace \(|G|^2=n/[2(n-1)]\) by \(2n/(n-1)\);
- or define the curvature norm with a factor \(1/4\) on the antisymmetric index pairs, in which case Step 63 §5.1 needs that prefactor.

Changing the coefficient in \(G\) is not a possible repair, since the coefficient is already fixed by \(\operatorname{Ric}(G)=-g\). This normalization issue changes numerical constants in \(F_T\), \(H_2\), and related displays, but not the dimension-only equivalence \(F_T\asymp F\) or any sign.

---

## 8. Signed-Hessian structure is consistent

The Hessian terms displayed in Step 63 (4.2)–(4.3) combine as

\[
-(\nabla^2a\owedge\operatorname{Ric})
-(\nabla^2a\owedge g)
=
-(\nabla^2a\owedge E).
\]

That sign agrees with the connection variation and the stated KN product. Since \(B\) is contracted with the same physical tensor \(T\) under the reflection, the structural bound

\[
|\nabla B|\le CF_T|\nabla\operatorname{Rm}|
\]

is unaffected by the sign repair.

---

## 9. Remaining compensating-error channel

The sweep’s three-channel description omits the exact zero-order conversion

\[
\boxed{\operatorname{Rm}=T+G}
\]

inside:

- \(Q(\operatorname{Rm})\);
- Lichnerowicz reaction terms;
- metric-variation contractions;
- the \(E\owedge g\) term from \(\partial_tG\);
- the explicit linear term in Step 58’s structural \(T\)-equation.

Under the legacy notation the same geometric relation is \(\operatorname{Rm}=T-\widetilde G\). The coarse estimates absorb every resulting term into \(CaF_T^3\), so the energy inequalities are stable. Exact coefficients, stationarity statements, and pure-scaling identities are not.

Accordingly, the scientifically supported conclusion is:

\[
\boxed{
\text{The KN sign reflection leaves the estimate stack unchanged.}
}
\]

But the stronger textual conclusion of “zero cross-note contradictions” is not supported. The concrete items requiring canonical repair are Step 64 (2.6), Step 58 §§2.1–2.2, the \(m=0\) form of the \(\operatorname{Rm}=T\pm G\) conversion, Step 63’s factor-two scaling equations, and the global curvature-norm normalization.