# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 41,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step41_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step41_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the Ricci-flow proposition in Step 41 against the supplied primary sources and the note. Verify the normalized-to-unnormalized scaling/time conversion, Yamabe-minimum estimate, scalar evolution/minimum argument, mean-scalar identity including volume-form terms, and the inference that Y(M)<0 plus inf_g P(g)>0 forces scalar curvature to be unbounded on every maximal normalized Ricci flow, using family 351 for finite time and Ishida for the immortal branch. Also assess exactly how this adds to the Einstein-gap programme and whether any current inherited gap actually supplies inf P>0. Return mathematical corrections and scope.

## Integrated Scientific Memo

# Step 41 Ricci-flow proposition: verification and corrections

Let
\[
P(g):=\int_M |\Ric_g^\circ|^2\,d\mu_g,
\qquad
\partial_tg=-2\Ric+\frac12\bar s\,g,
\qquad
\bar s=\frac1V\int_Ms\,d\mu .
\]

Conditional on family 351, Theorem 1.1, the principal proposition is correct:

> If \(M^4\) is closed, \(Y(M)<0\), and
> \[
> p_0:=\inf_{g\in\Met(M)}P(g)>0,
> \]
> then every maximal volume-normalized Ricci flow on \(M\) has unbounded scalar curvature on its maximal interval.

In fact, the conclusion can be sharpened to
\[
\limsup_{t\uparrow T_{\max}}\max_M s_{g(t)}=+\infty.
\]

The proof and its precise scope are as follows.

---

## 1. Normalized/unnormalized conversion

Suppose first that the normalized flow exists on \([0,T)\), \(T<\infty\), and scalar curvature is bounded. Define
\[
a(t)=\exp\!\left(-\frac12\int_0^t\bar s(u)\,du\right),\qquad
\tau(t)=\int_0^t a(u)\,du,\qquad
\widetilde g(\tau(t))=a(t)g(t).
\]
Constant metric rescaling satisfies
\[
\Ric_{ag}=\Ric_g
\quad\text{as a \((0,2)\)-tensor},\qquad
s_{ag}=a^{-1}s_g.
\]
Since \(a'/a=-\bar s/2\),
\[
\frac d{dt}(ag)
=a'g+a\left(-2\Ric+\frac12\bar s\,g\right)
=-2a\Ric,
\]
and \(d\tau/dt=a\), so
\[
\partial_\tau\widetilde g=-2\Ric_{\widetilde g}.
\]

If \(|s_g|\le C\), then \(|\bar s|\le C\), and on the finite interval
\[
e^{-CT/2}\le a(t)\le e^{CT/2}.
\]
Consequently \(\tau(T)<\infty\) and
\[
|s_{\widetilde g}|=a^{-1}|s_g|
\]
remains uniformly bounded. Family 351, Theorem 1.1 therefore extends \(\widetilde g\) smoothly beyond \(\tau(T)\).

To return explicitly to fixed volume, let \(\widetilde V(\tau)=\Vol_{\widetilde g(\tau)}M\) and set
\[
c(\tau)=\left(\frac{V}{\widetilde V(\tau)}\right)^{1/2},\qquad
\frac{dt}{d\tau}=c(\tau),\qquad
g(t(\tau))=c(\tau)\widetilde g(\tau).
\]
Because \(\widetilde V>0\) is smooth, this reconstructs a smooth normalized flow beyond \(T\), agreeing with the original one before \(T\). Thus finite maximal time and bounded scalar curvature are incompatible.

This finite-time branch uses neither \(Y(M)<0\) nor a \(P\)-gap; it follows solely from family 351. Its Corollary 1.2 also shows that, at finite maximal time,
\[
\limsup_{t\uparrow T}\max_M s=+\infty.
\]

---

## 2. Volume form and scalar evolution

For the four-dimensional normalized flow,
\[
\partial_t d\mu
=\frac12\tr_g(\partial_tg)\,d\mu
=(\bar s-s)\,d\mu,
\]
hence \(V'=0\).

The scalar evolution is
\[
\partial_ts
=\Delta s+2|\Ric|^2-\frac12\bar s\,s.
\]
Using
\[
|\Ric|^2=|\Ric^\circ|^2+\frac{s^2}{4},
\]
this becomes
\[
\boxed{\;
\partial_ts
=\Delta s+2|\Ric^\circ|^2+\frac12s(s-\bar s).
\;}
\]

---

## 3. Yamabe minimum estimate

Let
\[
m(t)=\min_M s_{g(t)}.
\]
For the current conformal class, its Yamabe constant satisfies
\[
Y_{[g(t)]}\le Y(M)<0.
\]
If \(m(t)\ge0\), the Yamabe quotient is nonnegative for every test function, contradicting \(Y_{[g(t)]}<0\). Thus \(m(t)<0\).

In dimension four,
\[
Q_g(u)=
\frac{\int_M(6|\nabla u|^2+su^2)\,d\mu}
{\left(\int_Mu^4\,d\mu\right)^{1/2}}.
\]
Dropping the nonnegative gradient term and using
\[
\int u^2\,d\mu\le V^{1/2}\left(\int u^4\,d\mu\right)^{1/2},
\]
with the sign reversal caused by \(m<0\), gives
\[
Q_g(u)\ge mV^{1/2}.
\]
Therefore
\[
mV^{1/2}\le Y_{[g]}\le Y(M),
\]
and hence
\[
\boxed{\;
m(t)\le Y(M)V^{-1/2}=:-c<0.
\;}
\]
This is Ishida Proposition 5 specialized to \(n=4\).

---

## 4. Minimum principle and scalar variance

At a spatial scalar minimum, in the barrier or almost-everywhere sense,
\[
m'\ge\frac12m(m-\bar s).
\]
Since \(m\le-c<0\) and \(\bar s-m\ge0\),
\[
\boxed{\;
m'\ge\frac c2(\bar s-m)\ge0.
\;}
\]
Thus \(m\) is nondecreasing and bounded above by \(-c\). Integrating,
\[
\int_0^\infty(\bar s-m)\,dt<\infty.
\]

Now assume the immortal flow has scalar curvature bounded above; a two-sided bound is stronger than necessary. Since \(m(t)\ge m(0)\),
\[
0\le s-m\le \sup s-m(0)=:C_1.
\]
Moreover,
\[
\fint(s-m)^2
=\fint(s-\bar s)^2+(\bar s-m)^2.
\]
Hence
\[
\Var(s):=\fint(s-\bar s)^2
\le \fint(s-m)^2
\le C_1(\bar s-m),
\]
so
\[
\boxed{\;
\int_0^\infty\Var(s)\,dt<\infty.
\;}
\]

Thus the immortal argument requires only a uniform upper scalar bound. A lower scalar bound follows from the minimum evolution independently.

---

## 5. Exact mean-scalar identity

The volume-form contribution must be included:
\[
\begin{aligned}
\frac d{dt}\int_Ms\,d\mu
&=\int_M\partial_ts\,d\mu+\int_Ms(\bar s-s)\,d\mu\\
&=\int_M\left(
2|\Ric|^2-\frac12\bar s\,s+s\bar s-s^2
\right)d\mu\\
&=2P-\frac12\left(\int_Ms^2\,d\mu-V\bar s^2\right).
\end{aligned}
\]
Since \(V\) is constant,
\[
\boxed{\;
\bar s'
=\frac{2P}{V}
-\frac12\fint_M(s-\bar s)^2\,d\mu.
\;}
\]

Integrating and using bounded \(\bar s\) and time-integrable variance gives
\[
\int_0^\infty P(g(t))\,dt<\infty.
\]
It is also possible to avoid assuming a separate bound on \(\bar s\): the integrability of \(\bar s-m\) provides times \(T_j\to\infty\) with \(\bar s(T_j)-m(T_j)\to0\), and integration up to \(T_j\) yields the same conclusion.

### Source correction

Ishida Proposition 3 reaches the correct conclusion
\[
\int_0^\infty\!\int_M|\Ric^\circ|^2\,d\mu\,dt<\infty,
\]
but its displayed proof identifies \(\int\partial_ts\,d\mu\) with \(\partial_t\int s\,d\mu\), omitting the evolving-volume term. That omission is not fatal: the missing term is controlled by Ishida’s time-integrable scalar oscillation. The exact identity above is the clean correction.

---

## 6. Contradiction from a positive \(P\)-gap

If
\[
P(g)\ge p_0>0
\]
for every smooth metric on \(M\), then an immortal flow satisfies
\[
\int_0^\infty P(g(t))\,dt\ge\int_0^\infty p_0\,dt=\infty,
\]
contradicting the previous section. Thus an immortal normalized flow cannot have bounded-above scalar curvature.

Together with the finite-time branch:
\[
\boxed{\;
\limsup_{t\uparrow T_{\max}}\max_Ms_{g(t)}=+\infty.
\;}
\]

---

## 7. Correction concerning \(P+D_2\)

Step 41 says: “A bound only for \(P+D_2\) does not suffice.” This is false if
\[
D_2(g):=\int_M(s-\bar s)^2\,d\mu.
\]
Under the hypothetical bounded-scalar immortal flow, both
\[
\int_0^\infty P\,dt<\infty,
\qquad
\int_0^\infty D_2\,dt
=V\int_0^\infty\Var(s)\,dt<\infty.
\]
Therefore any all-metric bound
\[
\inf_g\bigl(P(g)+D_2(g)\bigr)>0
\]
already gives the same contradiction. More generally, a positive lower bound for \(aP+bD_2\), \(a,b>0\), suffices.

For the programme’s normalized defect,
\[
\mathcal E
=\frac{4P+D_2}{R},
\qquad
R=P+\frac S4,\qquad S=\int s^2\,d\mu,
\]
an all-metric gap \(\mathcal E\ge e_0>0\) also suffices. Since \(Y(M)<0\),
\[
S\ge |Y(M)|^2,
\]
and therefore
\[
4P+D_2=\mathcal ER
\ge \frac{e_0}{4}S
\ge\frac{e_0}{4}|Y(M)|^2>0.
\]

Thus the proper distinction is:

- a \(P+D_2\) or \(\mathcal E\) gap need not imply \(\inf P>0\);
- nevertheless, if it holds for **all** metrics, it is already enough for the same Ricci-flow blow-up conclusion.

If Step 41 intended a different \(D_2\), its definition must be stated.

---

## 8. Do current inherited results supply \(\inf P>0\)?

### 8.1 The Step 41 cell work does not

The subthreshold cell construction is an upper-bound construction for the Einstein-defect problem. It does not yield an all-metric lower bound on \(P\). Nor do the current O10/O11 finite-density or collar arguments close such a lower bound. Thus, for the main unresolved target family, \(p_0>0\) remains an additional hypothesis.

Negative Yamabe invariant alone is also insufficient: a negative Einstein metric has \(Y(M)<0\) but \(P=0\).

### 8.2 A genuine all-metric \(\mathcal J\)-gap would supply it

If
\[
\mathcal J(g)=\frac{4P}{P+S/4}\ge c_0>0
\]
for every metric, then
\[
(4-c_0)P\ge\frac{c_0}{4}S.
\]
Using \(S\ge |Y(M)|^2\),
\[
\boxed{\;
\inf_gP(g)\ge
\frac{c_0|Y(M)|^2}{4(4-c_0)}>0.
\;}
\]
The scalar budget needed here is automatic from \(Y(M)<0\).

### 8.3 Ishida–LeBrun supplies \(P\)-gaps in strict classical regions

Chern–Weil gives
\[
4\pi^2T_+
=\frac S{24}+2W_+-\frac P2,
\qquad T_+=2\chi+3\tau.
\]
LeBrun’s estimate quoted by Ishida gives
\[
\frac1{4\pi^2}\left(2W_++\frac S{24}\right)
\ge\frac23\beta^2(M).
\]
Subtracting yields
\[
\boxed{\;
P(g)\ge8\pi^2\left(\frac23\beta^2(M)-T_+(M)\right).
\;}
\]

For
\[
M=X\#N,\qquad b^+(N)=0,
\]
with the monopole input \(\beta^2(M)\ge c_1^2(X)=:C\), and
\[
B:=4b_1(N)+b^-(N),\qquad T_+(M)=C-B,
\]
one gets
\[
\boxed{\;
P(g)\ge8\pi^2\left(B-\frac C3\right).
\;}
\]
Hence this is a positive uniform \(P\)-gap whenever
\[
4b_1(N)+b^-(N)>\frac13c_1^2(X).
\]

For pure blow-ups,
\[
M=X\#k\,\overline{\CP}^{\,2},
\]
this becomes
\[
P(g)\ge8\pi^2\left(k-\frac13c_1^2(X)\right),
\]
positive for \(k>c_1^2(X)/3\).

At equality, a per-metric strict inequality does not imply a uniform positive infimum. Ishida’s equality-case arguments exclude equality for individual metrics in certain settings, but the supplied proof does not furnish compactness preventing a sequence with \(P\to0\). Therefore the Ricci-flow proposition cannot be fed a \(P\)-gap at the equality threshold without an additional uniform argument.

The simplicial-volume estimate in the supplied connections note can likewise produce a \(P\)-gap only in the range where its explicit Chern–Weil lower bound is positive; it does not resolve the principal balanced window.

---

## 9. Exact contribution to the Einstein-gap programme

The proposition is a valid **static-to-dynamic transfer principle**:

- an all-metric \(P\)-gap—or, more generally, an all-metric positive gap for \(4P+D_2\)—forces upward scalar-curvature blow-up on every maximal normalized Ricci flow;
- family 351 closes the finite-time branch;
- Ishida Propositions 3 and 5 supply the classical immortal-flow mechanism, with the mean-scalar computation corrected as above.

It does **not** establish a new Einstein gap, improve the value of \(\alpha(M)\), prove finite-time singularity, classify singularity models, give a finite-time blow-up rate, or address attainment. In the strict Ishida–LeBrun topological region, it mainly repackages known quasi-non-singular-flow obstructions and combines them with family 351 to cover all maximal intervals uniformly.

Its genuinely new relevance would occur exactly where the Einstein-gap programme proves an all-metric \(P\)-, \(\mathcal J\)-, or \(\mathcal E\)-gap not already supplied by classical Yamabe/Seiberg–Witten/Chern–Weil estimates. No such new all-metric gap is presently supplied by the inherited Step 41 cell construction or the unresolved O10/O11 lower theory.