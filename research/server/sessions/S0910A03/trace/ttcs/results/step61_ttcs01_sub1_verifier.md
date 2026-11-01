# TTCS Independent Branch Record

```json
{
  "step_id": 61,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step60_all_order_continuation_and_terminal_chart.md",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A01/workspace/notes/step57_preceptor_deTurck_uniqueness_and_scope_review.md",
    "Sessions/S0910A03/workspace/codex_loop/Research_Report.md"
  ]
}
```

## Task

Independently reconstruct the shifted-curvature evolution for the exact fixed-cutoff flow in dimension four, with a=chi^2, G=g\owedge g/[2(n-1)], T=Rm+G, U=aT, and g_t=-2a(Ric+g)=-2 Ric(U). Read the listed notes. Determine the correct star-contraction base equations, enforcing the exact stationarity test T=U=0 (hyperbolic Einstein data) for arbitrary chi. Then assess Step 60's all-order induction after deleting any fictitious a·1 or a^2 forcing: which derivative families remain, whether any missing family appears, and whether the proof must start at m=2 from the separately established T0,T1,U1,C2 base rather than at m=1. Check the same-exponent residual estimate, time/spatial commutator derivative ordering, fixed-background C-infinity endpoint, and autonomous time-jet splice. Identify any further load-bearing flaw with an explicit term or explain why the corrected hierarchy closes. Produce a direct mathematical memo, not procedural commentary.

## Output

# Mathematical verification memo

## 1. Exact shifted-curvature equations

In dimension four,
\[
G=\frac{g\owedge g}{6},\qquad T=\operatorname{Rm}+G,\qquad
U=aT,\qquad a=\chi^2.
\]
With the stated contraction convention,
\[
\operatorname{Ric}(G)=g,\qquad
E:=\operatorname{Ric}+g=\operatorname{Ric}(T),
\]
and hence
\[
\operatorname{Ric}(U)=aE,\qquad
\partial_tg=-2\operatorname{Ric}(U).
\]

For the all-covariant Riemann tensor, the variation under
\(g_t=-2aE\), followed by the second Bianchi rearrangement and addition of
\(\partial_tG\), gives the star-contraction identity
\[
\boxed{
(\partial_t-a\Delta)T
=(\nabla a)*\nabla T+(\nabla^2a)*T
+a\bigl(T*T+G*T\bigr).}
\tag{1.1}
\]
Here and below each star denotes a finite universal linear combination of
contractions and slot permutations. The important algebraic fact is that every
term on the right contains \(T\). In particular, the constant \(G*G\) terms
that arise if \(\operatorname{Rm}=T-G\) is expanded prematurely cancel against
the corresponding terms from \(\partial_tG\) and the normalization.

Since \(a\) is fixed in coordinate time,
\(\partial_tU=a\,\partial_tT\). Applying
\[
\Delta(aT)=a\Delta T+2\nabla a*\nabla T+(\Delta a)T,
\qquad
\nabla U=a\nabla T+(\nabla a)*T,
\]
to (1.1) yields
\[
\boxed{
(\partial_t-a\Delta)U
=(\nabla a)*\nabla U+(\nabla^2a)*U
+\bigl((\nabla a)*(\nabla a)\bigr)*T
+U*U+aG*U.}
\tag{1.2}
\]
Writing \(B_j=\nabla^ja\) and \(C_j=\nabla^j\chi\), every occurrence of the
apparently unweighted term has the exact scalar-factor identity
\[
(B_1*B_1)*T
=4(C_1*C_1)*U,
\tag{1.3}
\]
with the same tensor contraction on both sides. Thus (1.2) is polynomial in
\(U\), cutoff jets, and \(aG\), without division by \(a\).

Equations (1.1)–(1.2) pass the exact stationarity test. If \(T=0\), then
\(\operatorname{Rm}=-G\), \(E=0\), \(U=0\), and \(g_t=0\) for every smooth
\(\chi\). Every term in both equations vanishes. Therefore the terms
\[
a\cdot1,\qquad a^2
\]
in Step 60 equations (1.5)–(1.6) are not actual evolution terms. Correspondingly:

- the standalone \(B_m\) in family (T6) must be deleted;
- \(\nabla^m(a^2)\) in family (U7) must be deleted.

A constant \(1\) may still appear on the right of an energy inequality after
regularizing tensor norms or applying Young’s inequality; that is an estimate
artifact rather than a term in the tensor equation.

---

## 2. Corrected derivative families

After the two deletions above, the \(T_m=\nabla^mT\) families are
\[
\begin{array}{lll}
\mathrm{(T1)}&a\Delta T_m,\\[1mm]
\mathrm{(T2)}&B_r*T_{m+2-r},&1\le r\le m+2,\\
\mathrm{(T3)}&B_r*T_i*T_j,&r+i+j=m,\quad B_0=a,\\
\mathrm{(T4)}&B_\ell*\nabla^r\operatorname{Rm}*T_s,
&\ell+r+s=m,\\
\mathrm{(T5)}&U_{r+1}*T_s,&r+s=m-1,\\
\mathrm{(T6)}&B_r*T_{m-r},&0\le r\le m.
\end{array}
\tag{2.1}
\]
Family (T6) is exactly the differentiated \(aG*T\) term, using
\(\nabla G=0\).

The \(U_m=\nabla^mU\) families are
\[
\begin{array}{lll}
\mathrm{(U1)}&a\Delta U_m,\\[1mm]
\mathrm{(U2)}&B_r*U_{m+2-r},&1\le r\le m+2,\\
\mathrm{(U3)}&C_{r+1}*C_{s+1}*U_t,&r+s+t=m,\\
\mathrm{(U4)}&U_i*U_j,&i+j=m,\\
\mathrm{(U5)}&B_\ell*\nabla^r\operatorname{Rm}*U_s,
&\ell+r+s=m,\\
\mathrm{(U6)}&U_{r+1}*U_s,&r+s=m-1,\\
\mathrm{(U7)}&B_r*U_{m-r},&0\le r\le m.
\end{array}
\tag{2.2}
\]
Here (U3) comes from differentiating \(4(C_1*C_1)*U\), and (U7) comes from
\(aG*U\).

For a literal commutator enumeration, the row (T4)/(U5) has
\(0\le\ell\le m-1\), since the commutator with \(\Delta\) is zero when no
derivative remains on \(\Delta A\). Allowing \(\ell=m\) merely enlarges the
schematic family by a term with zero universal coefficient.

No additional current-order family appears. The two potentially dangerous
spatial allocations reduce as follows:
\[
aT_m
=U_m-\sum_{q=1}^m B_q*T_{m-q},
\tag{2.3}
\]
and hence
\[
aT_m*U_0
=U_m*U_0-\sum_{q=1}^mB_q*T_{m-q}*U_0.
\tag{2.4}
\]
The coefficient \(U_0\) is pointwise bounded on the slab. At the other
extreme,
\[
a\operatorname{Rm}*U_m=(U_0-aG)*U_m.
\tag{2.5}
\]
The analogous \(T_m\) commutator terms have bounded current coefficient:
\[
aT_m*T_0=U_0*T_m,\qquad
a\operatorname{Rm}*T_m=(U_0-aG)*T_m.
\tag{2.6}
\]

There is one precision point in the printed tables. If covariant derivatives
are reordered into a fixed canonical order, differentiation of
\(\partial_t\Gamma\) also produces lower products such as
\[
T_q*U_{r-q}*T_s
\quad\text{or}\quad
T_q*U_{r-q}*U_s,
\qquad q\le r-1,\quad r+s=m-1,
\tag{2.7}
\]
and possibly iterated versions under repeated reordering. These products are
not separate rows in (2.1)–(2.2). They contain only orders below \(m\):
\(q\le m-2\), \(r-q\le m-1\), and \(s\le m-1\). Thus they belong to the
previous-level forcing. Alternatively, retaining ordered covariant derivatives
avoids introducing them at all. The tables are therefore complete for
current-order analysis, though a literal every-monomial list should mention
(2.7).

---

## 3. Time and cutoff commutators

The connection variation is
\[
\partial_t\Gamma
=g^{-1}*\nabla\operatorname{Ric}(U)
=g^{-1}*U_1.
\tag{3.1}
\]
Consequently,
\[
[\partial_t,\nabla^m]A
=\sum_{r+s=m-1}\nabla^r(\partial_t\Gamma)*\nabla^sA.
\tag{3.2}
\]
The unreordered top contribution is \(U_{r+1}*A_s\), so the largest \(U\)
order is \(m\), never \(m+1\).

For the fixed scalar \(\chi\),
\[
\boxed{
\partial_tC_{m+1}
=U_m*C_1+
\sum_{1\le j<m}U_j*C_{m+1-j}
+\mathcal R_m,}
\tag{3.3}
\]
where every term in \(\mathcal R_m\) contains curvature and cutoff orders below
the current pair. In particular, neither \(U_{m+1}\) nor \(C_{m+2}\) occurs in
(3.3). This is the triangular relation needed to couple \(U_m\) with
\(C_{m+1}\).

The spatial commutator has
\[
[\nabla^k,\Delta]A
=\sum_{r+s=k}\nabla^r\operatorname{Rm}*\nabla^sA.
\tag{3.4}
\]
When a coefficient receives \(\ell\ge1\) derivatives before this commutation,
\(r+s=m-\ell\le m-1\). Only \(\ell=0\) reaches the current order, and those
terms are exactly the ones reduced in (2.3)–(2.6).

---

## 4. Same-exponent closure and the correct starting order

Let
\[
V=U_m,\qquad Z=C_{m+1},\qquad
D_{m,p}^U=\int a|\nabla V|^2|V|^{p-2}.
\]
The two principal coefficient terms have the required structure:

- \(B_1*U_{m+1}=2\chi C_1*\nabla V\) is absorbed into \(D_{m,p}^U\);
- every \(B_2*V\) contraction can be integrated by parts as
  \[
  \left|\int(\nabla_i\nabla_ja)\,\mathcal B^{ij}(V)\right|
  \le \varepsilon D_{m,p}^U
  +C_{p,\varepsilon}\|C_1\|_\infty^2\|V\|_p^p.
  \tag{4.1}
  \]

Using
\[
B_{m+2}
=2\chi C_{m+2}
+\sum_{i=1}^{m+1}C_i*C_{m+2-i},
\tag{4.2}
\]
the sole new cutoff jet is \(2\chi C_{m+2}*U_0\). Testing against
\(P_p(V)=|V|^{p-2}V\) and integrating once gives, schematically,
\[
\begin{aligned}
\int P_p(V)*\chi\nabla Z*U_0
={}&-\int\nabla P_p(V)*\chi Z*U_0\\
&-\int P_p(V)*C_1*Z*U_0
-\int P_p(V)*\chi Z*U_1.
\end{aligned}
\tag{4.3}
\]
The first term is absorbed by diffusion, the second uses same-exponent Young,
and the last is
\[
I_m=\int\chi|Z|\,|U_1|\,|V|^{p-1}.
\tag{4.4}
\]
In four dimensions, with \(f=\chi|V|^{p/2}\),
\[
I_m
\le \|f\|_4\|Z\|_p\|U_1\|_4
\|V\|_p^{p/2-1},
\tag{4.5}
\]
because the reciprocal exponents sum to
\[
\frac14+\frac1p+\frac14+\frac{p/2-1}{p}=1.
\]
Moreover,
\[
\|f\|_4^2
\le C_S\left(p^2D_{m,p}^U+C_p\|V\|_p^p\right).
\tag{4.6}
\]
Young’s inequality then gives
\[
I_m\le\varepsilon D_{m,p}^U+
C\left(1+\|Z\|_p^p+\|V\|_p^p\right),
\tag{4.7}
\]
provided \(U_1\in L^4\) is already available. Thus neither current variable is
requested at an exponent larger than \(p\).

This explains why the general induction must begin at \(m=2\), after the
separate base construction
\[
T_0,\quad U_1,\quad C_2,\quad T_1
\in L^q\qquad\text{for every finite }q.
\tag{4.8}
\]
At \(m=1\), the \(U_1\) in (4.4) is the current variable \(V\), so treating
\(\|U_1\|_4\) as previous data is circular. Step 56 resolves precisely this
case by recognizing the resulting \(\chi C_2*V\) term as a signed-Hessian
contraction and integrating it directly. Hence the rigorous order is
\[
T_0\longrightarrow(U_1,C_2)\longrightarrow T_1,
\]
followed, for \(m\ge2\), by
\[
(U_m,C_{m+1})\longrightarrow T_m.
\tag{4.9}
\]

After \((U_m,C_{m+1})\) is completed, the \(T_m\) equation has the same weighted
principal terms. Its top-cutoff integration leaves \(C_{m+1}\), \(T_0\),
\(T_1\), and the current gradient. These quantities are already available at
arbitrarily large finite exponents. The time-commutator term
\(U_m*T_0\) is also forcing at this stage; for example,
\(U_m,T_0\in L^{2p}\) makes their product \(L^p\). Thus
\[
\frac d{dt}\|T_m\|_p^p+cD_{m,p}^T
\le C_{m,p,\tau}\bigl(1+\|T_m\|_p^p\bigr).
\tag{4.10}
\]

---

## 5. Fixed-background smooth endpoint

Fix \(\bar g=g(\tau)\) and let
\[
A=\nabla^{g(t)}-\bar\nabla.
\]
The connection variation is
\[
\partial_tA=g^{-1}*U_1.
\tag{5.1}
\]
Applying \(\bar\nabla^k\), converting between \(\bar\nabla\) and \(\nabla\),
and inducting on \(k\) gives an equation whose leading source is \(U_{k+1}\)
and whose remaining terms involve lower \(A\)-derivatives and already bounded
\(U\)-derivatives. Choosing finite \(p>4\) and using sufficiently many levels
of the intrinsic tower supplies the required pointwise coefficients. Grönwall
then yields bounds for every \(\bar\nabla^kA\).

Since \(\nabla g=0\),
\[
\bar\nabla g=A*g,
\]
so all fixed-background derivatives of \(g\) are bounded. Likewise,
\[
\partial_tg=-2\operatorname{Ric}(U)
\]
and the completed \(U\)-tower imply, for every integer \(s\),
\[
\sup_{\tau\le t<T_*}
\|\partial_tg(t)\|_{H^s(\bar g)}<\infty.
\tag{5.2}
\]
Therefore \(g(t)\) is Lipschitz in time with values in every
\(H^s(\bar g)\), hence
\[
g(t)\to g_*\quad\text{in }C^\infty(M)
\qquad(t\uparrow T_*).
\tag{5.3}
\]

Positive definiteness persists because
\[
|g_t|_g\le C_n|U|_g.
\]
A uniform \(\|U\|_\infty\) bound on the finite slab gives exponential
two-sided metric comparison with \(g(\tau)\), so the smooth tensor \(g_*\) is
a Riemannian metric.

---

## 6. Autonomous time-jet splice

Define
\[
\mathcal F(g)=-2\chi^2(\operatorname{Ric}_g+g),
\qquad
\mathcal F_1=\mathcal F,\qquad
\mathcal F_{\ell+1}(g)=D\mathcal F_\ell(g)[\mathcal F(g)].
\tag{6.1}
\]
Each \(\mathcal F_\ell\) is a smooth differential operator depending on a
finite spatial jet of \(g\) and the fixed function \(\chi\). Along the old
solution,
\[
\partial_t^\ell g(t)=\mathcal F_\ell(g(t)).
\]
The convergence (5.3) therefore gives
\[
\partial_t^\ell g(t)\to\mathcal F_\ell(g_*)
\quad\text{in }C^\infty(M).
\tag{6.2}
\]

Any smooth local restart \(\widehat g(s)\) with
\(\widehat g(0)=g_*\) satisfies the same autonomous equation and hence
\[
\partial_s^\ell\widehat g(0)=\mathcal F_\ell(g_*)
\quad\text{for every }\ell.
\tag{6.3}
\]
Thus the old solution, \(g_*\), and the restart have matching mixed
space-time derivatives of every order at \(T_*\). Their piecewise assembly is
a smooth solution across \(T_*\), without any overlap uniqueness statement.

## Result

After removing the spurious \(a\cdot1\), \(a^2\), standalone \(B_m\), and
\(\nabla^m(a^2)\) terms, the current-pair hierarchy closes. The induction must
use the separately proved \(m=1\) block and begin its uniform step at \(m=2\).
Canonical covariant reordering adds lower products of the form (2.7), but no
new current-order tensor or cutoff jet. Under the stated slab hypotheses and
the Step 56 base layer, the fixed-background smooth endpoint and autonomous
time-jet splice are mathematically supported.