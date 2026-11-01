# TTCS Independent Branch Record

```json
{
  "step_id": 41,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step41_symplectic_closure_bolt_layer_and_new_inputs.md",
    "Knowledge/materials/openai-math-20261007/archive/sources/ricci-extension.txt",
    "Knowledge/materials/openai-math-20261007/archive/sources/ishida-0807.2169.txt",
    "Knowledge/materials/openai-math-20261007/continuation/20261007_openai_math_connections/connections.md"
  ]
}
```

## Task

Check the Ricci-flow proposition in Step 41 against the supplied primary sources and the note. Verify the normalized-to-unnormalized scaling/time conversion, Yamabe-minimum estimate, scalar evolution/minimum argument, mean-scalar identity including volume-form terms, and the inference that Y(M)<0 plus inf_g P(g)>0 forces scalar curvature to be unbounded on every maximal normalized Ricci flow, using family 351 for finite time and Ishida for the immortal branch. Also assess exactly how this adds to the Einstein-gap programme and whether any current inherited gap actually supplies inf P>0. Return mathematical corrections and scope.

## Output

# Verification memo: Step 41 §6, the Ricci-flow proposition

## Summary

The proposition is correct as stated, conditional on Theorem 1.1 of family 351. The proof steps check out:

- the scaling and time conversion,
- the Yamabe-minimum bound,
- the minimum principle,
- the mean-scalar identity.

Four points correct or sharpen the note:

1. The finite-time branch uses neither \(Y(M)<0\) nor any \(P\)-gap. It holds for every closed four-manifold, given family 351.
2. The hypotheses can be weakened in two places. An upper scalar bound alone is enough. The \(P\)-gap can be replaced by a gap for the numerator of \(\mathcal E\). The conclusion also improves to \(\limsup_{t\to T_{\max}}\max_M s=+\infty\).
3. Ishida's Proposition 3 drops the \(\partial_t d\mu\) term. The exact identity used in Step 41 repairs this slip, and the conclusion of Proposition 3 is unaffected.
4. Every all-metric \(P\)-gap currently available comes from Chern–Weil combined with a Yamabe, Seiberg–Witten or simplicial-volume bound. With these inputs the immortal branch is exactly Ishida's Theorems 6, 21 and 25. No inherited result supplies \(\inf P>0\) on manifolds where those classical bounds give nothing.

## 1. Normalization and volume form

Take \(\partial_tg=-2\operatorname{Ric}+\tfrac12\bar s\,g\) in dimension four. Then
\[
\partial_t d\mu=\tfrac12\operatorname{tr}(\partial_tg)\,d\mu=(\bar s-s)\,d\mu ,
\]
so \(V\) is constant. This normalization agrees with Ishida's general formula \(2\bar s/n\) at \(n=4\).

## 2. Finite-time branch

**Forward conversion.** Put \(\tilde g(\tau)=a(t)g(t)\) with \(d\tau/dt=a\). Then
\[
\partial_\tau\tilde g=\frac{a'}{a}\,g-2\operatorname{Ric}(g)+\tfrac12\bar s\,g .
\]
Ricci curvature is invariant under constant rescaling, so this equals \(-2\operatorname{Ric}(\tilde g)\) exactly when \(a'/a=-\tfrac12\bar s\). This gives \(a=\exp(-\tfrac12\int_0^t\bar s)\) and \(s_{\tilde g}=a^{-1}s_g\), as Step 41 states. On \([0,T_{\max})\) with \(|s|\le C\), we have \(a\in[e^{-CT_{\max}/2},e^{CT_{\max}/2}]\). Hence \(\tau(T_{\max})<\infty\) and \(s_{\tilde g}\) is bounded.

Family 351, Theorem 1.1 then applies: closed four-manifold, \(0<T<\infty\), smooth initial metric \(\tilde g(0)=g(0)\), and \(\sup|R|<\infty\).

**Return to fixed volume.** This step deserves one explicit line. On the extended interval, the unnormalized volume \(\tilde V(\tau)\) is smooth and positive. Set \(c=(V/\tilde V)^{1/2}\), \(dt/d\tau=c\), and \(g=c\,\tilde g\). This is a normalized flow, and \(t(\tau)\) is strictly increasing past \(T_{\max}\). On the original interval \(\tilde V=a^2V\), so \(c=1/a\) and the reconstruction reproduces the given \(g\). This contradicts maximality.

**What this branch depends on.** The branch rests entirely on family 351. That is an OpenAI release preprint whose proof has not been re-established here. The classical alternative in its introduction, Bamler–Zhang Corollary 1.10, needs \(H^2(M;F)=0\) for every field \(F\). It therefore does not cover \(b^+\ge2\) manifolds.

**Sharper form of this branch.** Along the normalized flow, \(m=\min s\) satisfies \(m'\ge\tfrac12 m(m-\bar s)\). Whenever \(m<0\), this gives \(m'\ge0\). Then \(s\ge\min(m(0),0)\), so \(|s|\) is bounded if and only if \(s\) is bounded above.

Family 351 Corollary 1.2 carries over to the normalized flow as follows. Either \(\bar s\) is unbounded above, so \(\max s\ge\bar s\to\infty\). Or \(a\) is bounded below, so \(\max s=a\max s_{\tilde g}\to\infty\) along a sequence. In both cases \(\limsup_{t\to T}\max_M s=+\infty\).

## 3. Yamabe-minimum estimate

Ishida Prop. 5 at \(n=4\) gives \(m(t)\le Y(M)V^{-1/2}=:-c\).

- Dropping the gradient term and using Hölder, \(\int u^2\le(\int u^4)^{1/2}V^{1/2}\), gives \(Y[g]\ge mV^{1/2}\) when \(m<0\).
- If \(m\ge0\), then \(Y[g]\ge0\), which contradicts \(Y(M)<0\).
- Since \(V\) is fixed, \(c\) is constant in time.
- Orientation plays no role.

The estimate in Step 41 (11.3) is correct.

## 4. Scalar evolution and minimum argument

Under the normalized flow,
\[
\partial_ts=\Delta s+2|\operatorname{Ric}^\circ|^2+\tfrac{2}{n}\,s(s-\bar s).
\]
The extra term \(-\rho s\), coming from \(\rho g\) with \(\rho\) spatially constant, accounts for the \(\bar s\) contribution. This matches Ishida (6).

At a spatial minimum, in the barrier or a.e. sense since \(m\) is locally Lipschitz:
\[
m'\ge\tfrac12\,m(m-\bar s)=\tfrac12\,|m|(\bar s-m)\ge\tfrac c2(\bar s-m).
\]
This is Step 41's (11.4).

**Correction.** The integral
\[
\int_0^T(\bar s-m)\,dt\le\frac2c\,\bigl(m(T)-m(0)\bigr)\le\frac2c\,(-c-m(0))
\]
holds for every \(T\) without any scalar bound. Only the next step needs one.

**Variance step.** The exact identity is
\[
\fint(s-m)^2=\operatorname{Var}(s)+(\bar s-m)^2 .
\]
Hence \(\operatorname{Var}\le(\max s-m)(\bar s-m)\). An upper bound \(s\le C\) suffices, since \(\max s-m\le C-m(0)\).

## 5. Mean-scalar identity

Differentiate \(\int s\,d\mu\):
\[
\frac{d}{dt}\int s\,d\mu=\int\partial_ts\,d\mu+\int s(\bar s-s)\,d\mu .
\]
The first term equals \(2P+\tfrac12\int s(s-\bar s)\). The volume-form term equals \(-\int s(s-\bar s)=-\int(s-\bar s)^2\). Dividing by \(V\):
\[
\bar s'=\frac{2P}{V}-\frac12\operatorname{Var}(s).
\]
This confirms (11.5). The general-\(n\) coefficient is \((2/n-1)\).

**Slip in the primary source.** Ishida's proof of Prop. 3 writes \(\int\partial_ts\,d\mu=\partial_t\int s\,d\mu\). This omits \(\int(s-\bar s)^2\ge0\). Under \(|s|\le C\), that term is at most \(2C\int|s-\bar s|\), which is time-integrable by his (5). So Proposition 3 still holds, but the displayed chain of equalities is incorrect. Step 41's exact identity supplies the correct derivation.

**Bounded \(\bar s\) is not needed.** Since \(\int(\bar s-m)<\infty\), there are \(T_k\to\infty\) with \(\bar s(T_k)\le -c+o(1)\). Integrating up to \(T_k\) already gives \(\int_0^\infty P<\infty\).

## 6. Sharpened statement

Assume \(Y(M)<0\). Let \(Q(g)=4P+\bigl(S-(\textstyle\int s)^2/V\bigr)\), which is scale invariant. Note that \(Q\) is the numerator of the programme's \(\mathcal E\), since
\[
\mathcal E=\frac{4P+V\operatorname{Var}}{R}.
\]

**Proposition (sharpened).** If \(\inf_gQ(g)>0\), then every maximal normalized flow has
\[
\limsup_{t\to T_{\max}}\max_M s=+\infty ,
\]
assuming family 351 for finite \(T_{\max}\).

**Proof of the immortal branch.** Under \(s\le C\), both \(\int P\) and \(\int V\operatorname{Var}\) are finite. This contradicts \(Q\ge q_0>0\).

**Where the hypothesis comes from.**

- A \(P\)-gap implies a \(Q\)-gap, since \(Q\ge4P\).
- An \(\mathcal E\)-gap \(e_0\) implies \(Q\ge e_0R\ge e_0Y(M)^2/4\). This uses \(S\ge Y(M)^2\), which is Ishida (10) at \(n=4\).
- A \(\mathcal J\)-gap implies both of the above, because \(\mathcal E\ge\mathcal J\).
- The \(P\)-gap and \(\mathcal E\)-gap are not comparable with each other.
- Step 41's remark that \(P+D_2\) does not suffice remains correct.
- The scalar budget \(S_0\) in note (11.6) is automatic: \(S_0=Y(M)^2\).

**Quantitative rate for immortal flows.** Put \(K(T)=\sup_{M\times[0,T]}s\). Integrating (11.5) and using §4 gives
\[
K(T)-m(0)\ \ge\ \frac{2c}{V\,|m(0)|}\int_0^TP\,dt\ \ge\ \frac{2c\,p_0}{V|m(0)|}\,T .
\]
So under a \(P\)-gap the scalar maximum grows at least linearly. This is a growth rate for the time-supremum of \(\max s\), not for \(\max s\) at each time. The finite-time branch has no rate.

## 7. Which inherited gaps supply \(\inf P>0\)

Chern–Weil, note (1.1), gives \(P=S/12+4W_\pm-8\pi^2T_\pm\). The available all-metric lower bounds are:

| Input | Lower bound on \(\inf P\) | Status |
|---|---|---|
| Yamabe | \(\inf P\ge Y^2/12-8\pi^2\min(T_+,T_-)\) | Positive exactly when Ishida Thm 6 is violated |
| LeBrun, Cor. 15 | \(\inf P\ge8\pi^2\bigl(\tfrac23\beta^2-T_+\bigr)\) | On \(X\#k\overline{\mathbb{CP}}^2\): \(\ge8\pi^2(k-c_1^2/3)\) |
| Theorem 14 with \(W_-\) | \(\inf P\ge8\pi^2\bigl(\tfrac13\beta^2-T_-\bigr)\) | Classical |
| Family 335 | \(\inf P\ge a_4\|M\|/12-8\pi^2T\) | Conditional on family 335; gives \(Y\le-\sqrt H\) on the \(M_j\) of note §8.2 |

In the note's window \(T_+=A(1-h)\), the LeBrun row gives \(8\pi^2A(h-\tfrac13)\). This is positive only for \(h>1/3\).

**Consequence.** With any of these inputs, the immortal branch is equivalent to Ishida's Theorems 6, 21 and 25. No new manifold is reached.

**Gaps that do not help here.** The finite-density and N1/I40/I41 results bound \(\kappa_\beta=r+D_\beta/V\). They do not bound \(P\) or \(Q\). Step 41 §7.4 itself records that lower theory still lacks an all-metric mechanism.

**Equality case in Ishida.** Ishida Cor. 22 at \(k=c_1^2/3\), and Thm 23 at equality, derive strictness from a per-metric strict inequality. A per-metric strict inequality only gives "\(\ge\)" after the \(\liminf\) over time windows. The written argument therefore reaches only \(k>c_1^2/3\), unless one adds a compactness argument that is not in the source. This equality integer, together with the window \(h\le1/3\), is exactly where a uniform \(P\)- or \(Q\)-gap from the Einstein-gap programme would feed the proposition with new content.

## 8. What the proposition adds to the programme

**What it is.** It is an application, not a strengthening of \(\alpha(M)\). It turns any all-metric \(Q\)-gap into the dynamical conclusion that scalar curvature blows up upward on every maximal normalized flow, with linear growth in the immortal case.

**Contrapositive use.** Suppose a flow on \(M\) with \(Y(M)<0\) is immortal and has \(s\) bounded above. Then real metrics \(g(t_k)\) exist with \(P\to0\) and \(\mathcal E\to0\), so \(\inf\mathcal E=\inf\mathcal J=0\). Such flows are therefore a possible source of approximating sequences. They give no information about attainment.

**What it does not address.** It says nothing about finite-time blow-up versus immortality, blow-up rates in finite time, singularity models, attainment, or O10/O11.