# TTCS Independent Branch Record

```json
{
  "step_id": 59,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step59_induction_ledger_repair.md",
    "Sessions/S0910A01/workspace/scripts/step59_induction_ledger_verify.py",
    "Sessions/S0910A01/workspace/data/step59_induction_ledger_verify.json",
    "Sessions/S0910A01/workspace/notes/step58_all_order_continuation_proof.md",
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md",
    "Sessions/S0910A03/workspace/notes/step37_base_pair_continuation.md"
  ]
}
```

## Task

Verify the new Step 59 induction-ledger repair for the restricted four-dimensional negative Ishida--LeBrun cutoff-flow route. Focus only on the consequential issues identified in the Strategist note: (i) whether the source-by-source classification correctly extracts current-order terms from B_{m+2}*U_0, B_{m+1}*U_1, and B_2*U_m rather than hiding them in a lower family; (ii) whether the unweighted T_m equation has the analogous extracted top-cutoff and signed-Hessian terms and uses aT_m=U_m+lower without division by a; (iii) whether the source order T0 -> (U1,C2) -> T1 -> pointwise T0 -> general m>=2 is logically sound and avoids using W^{1,p}->L^[?2004h∞ to prove its own base estimates; (iv) whether the fixed-background conversion really has the strict triangular form partial_t A_m = g^{-1}*U_{m+1}+P(A_{<m},U_{<=m}) without a current A_m coefficient; and (v) what precise mathematical details still remain unproved after this repair. Do not treat the old Step58 module count as evidence; read the actual notes.

## Output

# Verification memo — Step 59 current‑pair induction ledger

Session S0910A01. I re‑derived the load‑bearing algebra myself from the flow equations rather than reading the module tables, and I read `step59_induction_ledger_repair.md`, its script and JSON, `step58_all_order_continuation_proof.md`, and the two A03 notes (`step57_H2_evolution_and_continuation_bridge.md`, `step37_base_pair_continuation.md`) that the base layer is drawn from. Below, equation numbers refer to the note in question.

---

## 0. Independent re‑derivations that came out right

Before the itemized answers, the following pieces I checked by direct computation, not by trusting the notes:

**(a) The weighted base equation and the no‑division identity.** From $\partial_t g=-2aE$ and $\partial_tT=a\Delta T+B_1*\nabla T+B_2*T+a(T*T+T)$, multiplying by $a$ and using $a\nabla T=\nabla U-B_1*T$, $a\Delta T=\Delta U-2\nabla a\!\cdot\!\nabla T-(\Delta a)T$ gives
$$a^2\Delta T=a\Delta U-2B_1*\nabla U+2(B_1*B_1)*T-B_2*U,\qquad aB_1*\nabla T=B_1*\nabla U-(B_1*B_1)*T,$$
so Step 58 (2.3) has the right shape, and $(B_1*B_1)*T=4\chi^2(C_1*C_1)*T=4(C_1*C_1)*U$ is an identity of algebra with no quotient anywhere. Good.

**(b) No independent forcing.** The apparent danger in the normalization piece $h_{\rm conf}=-2ag$ is a term $(\nabla^2a)\owedge g$, which would not vanish at $T\equiv0$. It does not occur: the Hessian of the coefficient always lands on $h=-2aE$ as a whole, i.e. $(\nabla^2a)\owedge E$ with $E=\operatorname{Ric}(T)$. Step 58 §2's stationarity principle is therefore consistent with the actual Leibniz expansion, not just with a wish.

**(c) Hölder/Sobolev arithmetic of the critical residual.** $\tfrac14+\tfrac1p+\tfrac14+\tfrac{p-2}{2p}=1$, and $\bigl\||V|^{p/2-1}\bigr\|_{2p/(p-2)}=\|V\|_p^{p/2-1}$. So (3.8) is exact, and (3.9) follows by $A^{1/2}B\le\varepsilon A+\tfrac1{4\varepsilon}B^2$ together with $\|Z\|_p^2\|V\|_p^{p-2}\le\frac2p\|Z\|_p^p+\frac{p-2}{p}\|V\|_p^p$. The $p$‑dependence ($\varepsilon\sim (p^2C_S)^{-1}$ against $c_p\ge1$ in (3.2)) is harmless because only finitely many exponents are ever used.

**(d) Both commutator top indices.** For the scalar $\chi$, $\partial_t(\nabla^{m+1}\chi)=\sum_{i=0}^{m-1}\nabla^i(\partial_t\Gamma)*\nabla^{m-i}\chi$ — the recursion terminates at $i=m-1$ because $\partial_t(\nabla\chi)=0$ exactly. With $\partial_t\Gamma=g^{-1}*U_1$ and $\nabla g^{-1}=0$, this is precisely $\sum_{j=1}^{m}C_{m+1-j}*U_j$, i.e. (3.13) with top $C_1*U_m$ and no $U_{m+1}$, no $C_{m+2}$. Likewise $[\partial_t,\nabla^m]U=\sum_{r+s=m-1}g^{-1}*U_{r+1}*U_s$ has top $U_m*U_0$, confirming (2.11)–(2.12). These two order counts are what make the pair $(U_m,C_{m+1})$ a genuinely closed system, and they hold.

---

## 1. (i) Extraction from $B_{m+2}*U_0$, $B_{m+1}*U_1$, $B_2*U_m$

**Correct, and the current list (2.4) is complete.** I enumerated every source of a differentiated cutoff coefficient at level $m$:

| source | family | top index |
|---|---|---|
| $\nabla^m(a\Delta U)$ | $B_k*U_{m+2-k}$, $k=1..m$ | $B_m*U_2$ |
| $\nabla^m(B_1*\nabla U)$ | $B_{1+k}*U_{m+1-k}$, $k=0..m$ | $B_{m+1}*U_1$ |
| $\nabla^m(B_2*U)$ | $B_{2+k}*U_{m-k}$, $k=0..m$ | $B_{m+2}*U_0$ |
| $\nabla^m\bigl((C_1{*}C_1){*}U\bigr)$ | $C_{1+i}*C_{1+j}*U_l$, $i+j+l=m$ | $C_{m+1}*C_1*U_0$ |

Applying (1.4) to each and tracking indices: in $B_{m+2}*U_0$ the cross sum $\sum_{i=1}^{m+1}C_i*C_{m+2-i}$ has current pieces only at $i=1$ and $i=m+1$, both giving $C_1*C_{m+1}$; for $2\le i\le m$ both indices are $\le m$ and hence previous‑level. In $B_{m+1}*U_1$ the cross indices run over $1\le i\le m$, all $\le m$. In $B_2*U_m$ the split $B_2=2\chi C_2+2C_1\otimes C_1$ is exact. So (2.3a–c) and the extracted list (2.4) are right, and the previous‑level statement (2.5) with $3\le k\le m$, $U_{m+2-k}\le U_{m-1}$, $C_{j}$, $j\le k\le m$, is right. The $m=2$ remark (empty middle range) is right.

**The single structurally load‑bearing fact, which the note asserts but never states as a lemma:** $C_{m+2}$ occurs *only* against $U_0$, and only from the $k=m$ term of $\nabla^m(B_2*U)$. Everything in §3.2 depends on that pairing, because after one integration by parts the absorbed term carries the factor $\|U_0\|_\infty$ and the residual carries $U_1$. It is worth writing that count explicitly, since it is the reason a single integration by parts suffices at every order.

**Two families the wording of (2.2) omits, neither changing (2.4).**
1. The triple cutoff family from $(C_1*C_1)*U$ is not of the form $B_k*U_{m+2-k}$. Its current pieces are exactly $C_1*C_{m+1}*U_0$ and $C_1*C_1*U_m$, already listed; the interior pieces $C_{1+i}*C_{1+j}*U_l$, $1\le i\le m-1$, have all indices $\le m$. So the ledger is complete, but the sentence "all terms created by differentiating the cutoff coefficients have schematic form (2.2)" is narrower than the actual source set.
2. **Reordering of derivative blocks is not on the ledger at all.** $B_{m+2}$ as produced by the Leibniz rule is $\nabla^m(\nabla^2a)$, whereas (2.3a) and the integration by parts (3.4) use $C_{m+2}=\nabla C_{m+1}$ with the outer index first. Commuting the two costs $\sum_{i+j\le m}T_i*C_j$ with $i\le m-1$, $j\le m$ (from $[\nabla_a,\nabla_b]\nabla_c\chi=-R_{abc}{}^d\nabla_d\chi$ and its iterates), multiplied by the bounded $U_0$. Those are previous‑level *precisely because* the interleaved order (4.8) supplies $T_i$ for $i\le m-1$ before the pair at level $m$ — so the design absorbs them, but the reordering family should appear in the ledger and in the script, since it is the one place where the unweighted tower feeds back into the weighted pair estimate.

**Mechanism check on §3.4.** The signed‑Hessian estimate is valid: $\nabla^2\chi$ is symmetric, so $\nabla_i$ can be taken as the outer index; $\chi=\sqrt a$ exactly, so $\chi|C_1||V|^{p-1}|\nabla V|$ Young‑splits against $\int a|\nabla V|^2|V|^{p-2}$; and $|\nabla B|\le Cp|V|^{p-1}|\nabla V|$ holds for $B\sim|V|^{p-2}V*V$. Only $\|d\chi\|_\infty$ enters, as stated. Similarly (3.3) is legitimate globally: on $\{a=0\}$ one has $B_1=2\chi C_1=0$, so the integrand vanishes there and $|B_1|^2/a=4|C_1|^2$ is used only where $a>0$. Since $\{a=0\}$ has positive measure, that one‑line remark deserves to be in the text.

---

## 2. (ii) The unweighted $T_m$ equation

**The extracted five terms are the right ones.** From $\partial_tT=a\Delta T+B_1*\nabla T+B_2*T+a(T*T+T)$ the same three sources produce $B_{m+2}*T_0$, $B_{m+1}*T_1$, $B_2*T_m$, hence $\chi C_{m+2}*T_0$, $\chi C_{m+1}*T_1$, $C_1*C_{m+1}*T_0$, $\chi C_2*T_m$, $C_1*C_1*T_m$ — (4.1) is consistent with my own expansion. The residual (4.4) and its absorption (4.5) mirror (3.6)–(3.9) with $T_1\in L^4$ replacing $U_1\in L^4$; the exponent arithmetic is identical and correct.

**$aT_m=U_m-\sum\binom mq B_q*T_{m-q}$ is used correctly and without division.** (2.10)/(4.6) is just the Leibniz rule solved for the top term; every unweighted factor on the right has index $\le m-1$. Two refinements:

* The conversion is needed at *more* places than remark 4 lists. It applies not only to spatial commutators but also to the differentiated reaction $\nabla^m(aT*T)\ni aT_m*T_0$ and to the $k=0$ term of $\nabla^m(aT)$. As written, remark 4 covers only "spatial commutators with $aT_m$".
* Several places where the note invokes $T_0\in L^\infty$ do not need it, because $aT_0=U_0$ *identically*. The spatial‑commutator endpoint is $a\operatorname{Rm}*U_m=(U_0-aG)*U_m$ with $|aG|\le C$, so it is a bounded‑coefficient current term with no pointwise curvature input; likewise $a\operatorname{Rm}*T_m$. The only current place where $T_0$ appears with a $\chi$ rather than an $a$ is the absorbed piece of the top‑cutoff integration by parts, $\int\nabla(|T_m|^{p-2}T_m)*\chi Z*T_0$, and that closes with $T_0\in L^{2p}$ via $\|Z\|_{2p}^2\|T_0\|_{2p}^2\|T_m\|_p^{p-2}$ — the pair estimate is available at exponent $2p$. So the pointwise curvature step is a convenience, not a structural prerequisite; the JSON's sample string "bounded $T_0$ after base pointwise step" attributes to it more work than it does.

---

## 3. (iii) Source order and the Sobolev step

**The order is not circular, and the specific worry is answered.** The chain is: an unweighted $L^q$ estimate for $T_0$; then the pair $(U_1,C_2)$; then $T_1$; then $|T_0|\in L^\infty$ by Kato plus Sobolev; then $m\ge2$. The Sobolev step consumes $\|T_0\|_p+\|T_1\|_p$ with *unweighted* $L^p$ norms, and the unweighted tower (4.7) produces exactly unweighted norms (the weight $a$ sits only on the dissipation). This is precisely what A03 Step 37 §6 warned was missing in the earlier version ("the energy provides only a degenerate weighted spatial derivative integral"), and the interleaved order supplies it. So (0.1) is sound as a matter of logic.

**The $m=0$ layer is stronger than Step 58 §3 says it is.** Step 58 §3 justifies $T_0\in L^q$ by "bounded Riemann curvature everywhere on the controlled slab", which is not available on the collar where $0<a<1$. The correct argument is the $m=0$ instance of this note's own machinery: testing the $T$ equation against $|T|^{p-2}T$,
$$\tfrac{d}{dt}\|T\|_p^p+c\!\int\! a|\nabla T|^2|T|^{p-2}\le \varepsilon(\cdots)+C\bigl(\|C_1\|_\infty^2+\|U\|_\infty+1\bigr)\|T\|_p^p,$$
where $B_2*T=2\chi C_2*T+2C_1{*}C_1{*}T$ has its Hessian piece handled by §3.4 (no $\|C_2\|$ needed) and the reaction obeys $\int a|T|^{p+1}=\int(a|T|)|T|^p\le K\|T\|_p^p$. Every term is homogeneous in $T$, so no volume forcing is needed either. This makes the base $T_0$ layer internal, with inputs only $\|aF_T\|_\infty\le K_\tau$, $\|d\chi\|_\infty$, and slab metric equivalence.

**A more consequential point: the $m=1$ exception looks like an artifact of taking absolute values.** §3.3 and Step 58 §5.2 declare $m=1$ impossible because the residual becomes $\int\chi|C_2||U_1|^p$ with $U_1$ current. But at $m=1$ that residual *is* a signed Hessian term: $Z=C_{m+1}=\nabla^2\chi$ and the accompanying factor $U_1$ equals $V$, so the term is
$$\int\chi\,\nabla_i\nabla_j\chi\;B^{ij}(V),\qquad |B|\le C|V|^p,\quad|\nabla B|\le Cp|V|^{p-1}|\nabla V| ,$$
i.e. exactly the object handled by (3.10)–(3.12), and the derivative created by the second integration by parts is absorbed by the *level‑1* dissipation $D_{1,p}^U$, not by an unavailable level‑2 quantity. The other current terms at $m=1$ are $C_1*C_2*U_0$ (Young, $Z$ linear), the absorbed piece $\int\nabla(|V|^{p-2}V)*\chi Z*U_0$ ($Z$ linear), and $\chi C_2*U_1$ (same Hessian route); the cutoff‑jet equation degenerates to $\partial_tC_2=C_1*U_1$ exactly. This is essentially what A03 Step 37 §3.1/§3.3 as repaired by Step 38 does. If that index bookkeeping holds, the induction can begin at $m=1$ and the "base layer" ceases to be an import — which matters because the two files that currently carry it (`step37...`, `step57...`) both open with supersession notices covering the sections in question (Step 37 "must not be cited as a completed extension theorem"; Step 57 §§8.1–8.3 superseded and §9.2(a,c,d) marked not established). The precise thing to check is the contraction pattern: whether the residual's $C_2$ indices are both free for the second integration by parts once the specific contractions of $\nabla^m(B_2*U)$ are written out. The $m\ge2$ Hölder–Sobolev route and the $m=1$ Hessian route are complementary, not competing: for $m\ge2$, $C_{m+1}$ is no longer a Hessian and iterating the integration by parts would hit $U_1$ and $V$ with uncontrolled derivatives, so the base‑data route is the correct one there.

---

## 4. (iv) Strict triangularity of the background conversion

**Verified, including the two auxiliary identities.**

$\partial_t\Gamma^k_{ij}=-g^{kl}\bigl(\nabla_i(aE)_{jl}+\nabla_j(aE)_{il}-\nabla_l(aE)_{ij}\bigr)$ and $aE=\operatorname{Ric}(U)$, with $\nabla$ commuting with metric contraction, gives $\partial_tA=g^{-1}*U_1$ exactly — no derivative of $a$ is created, as (1.6)/(5.2) states.

$\bar\nabla g=-A*g$ (from $\nabla g=0$, $\nabla=\bar\nabla+A$) gives $\bar\nabla g^{-1}=g^{-1}*A$, hence (5.3) with top $A_{k-1}$. Writing $\bar\nabla=\nabla-A$ and inducting: $\bar\nabla U_1=U_2-A*U_1$, $\bar\nabla^2U_1=U_3-2A*U_2-A_1*U_1+A*A*U_1$, and in general each of the $m$ background derivatives either raises the $U$ order or differentiates an existing $A$, so the highest $A$ order is $A_{m-1}$ — (5.4) holds. Combining with the Leibniz sum over $\bar\nabla^jg^{-1}$ ($A$ order $\le j-1\le m-1$) yields exactly
$$\partial_tA_m=g^{-1}*U_{m+1}+P_m(A_{\le m-1},U_{\le m},g^{-1}),$$
with **no** current $A_m$ coefficient. The Step 58 §7.2 term $B_0^A*A_m$ is indeed superfluous. Two additions that strengthen the statement: at $m=0$ there is no lower term at all, and $A(\tau)=0$ since $\bar g=g(\tau)$, so $\|A(t)\|_p\le\int_\tau^t\|U_1\|_p$; and the Grönwall at each level needs the forcing measured in $\bar g$‑norms, which requires the uniform equivalence $e^{-2V_*}g(\tau)\le g(t)\le e^{2V_*}g(\tau)$ from $\int_\tau^{T_*}\|aE\|_\infty<\infty$ (Step 58 (8.2)) plus the index‑count constant relating $|\cdot|_{g(t)}$ and $|\cdot|_{\bar g}$ for a tensor of fixed rank. Given that, (5.6)–(5.8) and Cauchy convergence in each $H^s$ (Lipschitz in $t$ with values in $H^s$, finite terminal time) are sound, and the smooth limit follows by Sobolev embedding.

---

## 5. (v) What is still unproved after this repair

Ordered by how much each carries.

1. **Explicit contraction patterns.** Everything above is verified at the level of index counting with $*$‑products. Three places need the actual tensor contractions to be written, because the estimates use structure, not only size: (a) the top‑cutoff integration by parts (3.4)/(4.3) requires the outer index of $C_{m+2}$ to be the differentiated one, which needs the $\nabla^m\nabla^2a\to\nabla^{m+2}a$ reordering ledger described in §1 above; (b) the signed‑Hessian estimate (3.10)–(3.12) requires both Hessian indices to be free for the second integration by parts; (c) the $m=1$ residual identification in §3 above.

2. **The $m=1$ pair and $T_1$.** Either the base layer must be reproved in a non‑superseded file for $(U_1,C_2)$ and $T_1$ at every finite $p$ on a positive slab, or — preferably — the $m=1$ signed route above should be written so the ledger becomes self‑contained from $m=0$. As it stands, (3.1) of Step 58 is imported from sections that their own headers mark as superseded or not established, and Step 59 §3.3 uses $\|U_1\|_{L^4}$, $\|T_1\|_{L^4}$ as given data.

3. **The two Moser endpoints.** The whole tower runs on $\|aF_T(t)\|_\infty\le C\Gamma/t$ and $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$. A03 Step 57 §12 lists the term‑by‑term verification of the weighted curvature endpoint as not carried out there. $U_0\in L^\infty$, the slab metric equivalence, the Sobolev constant, and the positive‑definiteness of $g_*$ all rest on these.

4. **Smooth existence for the degenerate flow itself** (Step 58 module A). $a=\chi^2$ vanishes on an open set, so the system is degenerate parabolic; the transported‑cutoff DeTurck construction is the deepest analytic input and is the one item Step 58 §10 lists as conditional.

5. **Two distinct suprema in the continuation conclusion.** Step 58 §8.3 concludes $T_*\ge\theta r^2$ from the splice. The splice extends the *maximal smooth interval*; it does not by itself contradict an exit of the first‑exit inequalities. The conclusion needs the separate strict‑improvement/openness property of the bootstrap quantities (A01 Step 55) alongside the smooth continuation. Step 59 §5 inherits this wording.

6. **Routine but undisplayed terms.** The metric‑ and measure‑variation contributions to $\frac{d}{dt}\int|V|^p$ (from $\partial_tg^{-1}=2aE*g^{-1}g^{-1}$, one factor per index of $U_m$, and $\partial_t d\mu=-a\operatorname{tr}E\,d\mu$) are all bounded by $C(m)\|U\|_\infty$ and belong in $\mathcal B_m^U$; they are absent from (2.13) and from the script.

7. **The geometric inputs** that §6 correctly says are not supplied: a curvature budget mechanism and a terminal density with a locally impossible zero set. Two arithmetic checks on the interface in Step 58 §9 do hold: $\operatorname{Spec}(W^+_\infty)=(-\tfrac16,\tfrac1{12},\tfrac1{12})$ is trace‑free with $\sum\lambda_i^2=\tfrac6{144}=\tfrac1{24}$, so $24|W^+|^2=1$ and the Derdziński conformal factor is $1$, i.e. $g_\infty$ itself is locally Kähler; and $\operatorname{Ric}=-g$ in dimension four gives $s=-4$, so a Kähler–Einstein comparison forces $|W^+|^2=s^2/24=2/3\ne1/24$. The coefficient $119$ in (9.1) and the volume/selection constants in (9.2) are not checkable from the files supplied here.

---

## 6. On the script and JSON

The 10/10 result should not be read as verification of the mathematics, and it is worth knowing exactly what it covers, since the ledger is the object being tested:

* Eight of the ten are substring searches in the note. They confirm wording, not derivations.
* `base_order_preserved` compares a literal list to the same literal list; it is a tautology.
* The real content is `coefficient_classification`, which for each $m$ up to 64 asserts labels for $k=m+2,m+1,2$ and the range $3\le k\le m$. The index arithmetic that makes the classification true (that the cross sums $\sum_i C_i*C_{m+2-i}$ have all indices $\le m$ except at $i\in\{1,m+1\}$) is written into label strings, not computed. Since the arithmetic is uniform in $m$, running to $m=64$ adds nothing over $m=2,3$; the only distinguished case is $m=2$, where the middle range is empty.
* `reaction_classification`, `spatial_comm_classification`, `time_comm_classification` are run for $U$ only. The $T$‑side reaction $\nabla^m(aT*T)$, the $T$‑side commutators, and the $aT_m\to U_m$ conversion at each of their occurrences are not classified anywhere, although §4 makes assertions about them.

If the ledger is to carry machine content, the cheap upgrade is to enumerate rather than label: for each $m$, generate the multiset of monomials from the four sources of §1 (including the $C_1{*}C_1{*}U$ triple family and the curvature‑reordering family $T_i*C_j*U_0$, $i\le m-1$, $j\le m$), tag each monomial by (max cutoff order, max $U$/$T$ order), and assert that every monomial is either in the explicit current list or has all orders strictly below the level‑$m$ pair in the interleaved order (4.8). That version would have caught both omissions in (2.2) and would cover the $T$ side symmetrically.

---

## 7. Net reading

On the five questions: (i) yes, the extraction is correct and the current list is complete, with the exhaustiveness statement (2.2) needing two more source families and with the "$C_{m+2}$ occurs only against $U_0$" count deserving lemma status; (ii) yes, with the $aT_m$ conversion applying at more occurrences than remark 4 lists and with several $T_0\in L^\infty$ invocations replaceable by $aT_0=U_0$ or by finite exponents; (iii) the order is non‑circular and the Sobolev step is applied to genuinely unweighted norms, but the $m=0$ layer needs the energy argument rather than Step 58 §3's justification, and the $m=1$ exception appears to dissolve under the same signed‑Hessian mechanism the note already uses, which would make the base internal instead of imported from superseded sections; (iv) yes, strictly triangular, and I confirmed it by direct computation, with $A(\tau)=0$ and no lower term at $m=0$ as free strengthenings; (v) the items in §5, of which the contraction‑pattern write‑up, a non‑superseded $m=1$/$T_1$ derivation, the two Moser endpoints, and existence for the degenerate flow are the substantive ones — the ledger repair itself is a genuine improvement in the analytic hierarchy and does not touch the geometric inputs, exactly as §6 states.