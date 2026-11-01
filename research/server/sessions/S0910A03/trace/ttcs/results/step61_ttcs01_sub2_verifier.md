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

# Verification Memo: shifted-curvature base equations and Step 60's all-order tower (dimension 4)

Session S0910A03, exact fixed-cutoff flow. Objects: $a=\chi^2$ (fixed scalar), $G=\tfrac{g\owedge g}{2(n-1)}$, $T=\operatorname{Rm}+G$, $U=aT$, and $\partial_t g=-2a(\operatorname{Ric}_g+g)=-2\operatorname{Ric}(U)$.

I reconstructed the base evolution from the variation formula independently of the notes, enforced $T=U=0$ stationarity, and then traced the consequences through Step 60's induction. Findings below are stated as mathematics with the concrete terms attached.

---

## 1. Two algebraic facts that control everything

With the Kulkarni–Nomizu convention $(g\owedge g)_{ijkl}=2(g_{ik}g_{jl}-g_{il}g_{jk})$, the Ricci contraction is
$$
\operatorname{Ric}(g\owedge g)=2(n-1)g \;\Longrightarrow\; \operatorname{Ric}(G)=g,\qquad \operatorname{Ric}(T)=\operatorname{Ric}_g+g=E .
$$
So **$E$ is exactly the Ricci contraction of $T$, with no additive constant**, and $\operatorname{Rm}=T-G$. These two identities are the reason every surviving term in the base equations carries a factor of $T$ (or $U$), and they are what the stationarity test exposes.

Also $\operatorname{Ric}(U)=aE=V$, so $\partial_t g=-2V$ with $|V|\le C_n|U|$, and $V=\operatorname{Ric}(U)$ is a pure contraction of $U$ (this is used repeatedly in the commutator work).

---

## 2. Corrected base equations (independent derivation)

Write $v=\partial_tg=-2aE$, $B_1=\nabla a=2\chi C_1$, $B_2=\nabla^2a$, $C_j=\nabla^j\chi$. The second-order variation of $\operatorname{Rm}$ is
$$
\partial_tR_{ijkl}=\tfrac12(\nabla_i\nabla_kv_{jl}+\nabla_j\nabla_lv_{ik}-\nabla_i\nabla_lv_{jk}-\nabla_j\nabla_kv_{il})-\tfrac12(\operatorname{Rm}*v).
$$
Insert $v=-2aE$ and use $\nabla g=0$ (so $\nabla^2E=\nabla^2\operatorname{Ric}$, $\nabla E=\nabla\operatorname{Ric}$):

- $a\nabla^2E$ terms $\to a\Delta\operatorname{Rm}+a\,\operatorname{Rm}*\operatorname{Rm}$ via the contracted second Bianchi identity; since $\Delta G=0$ this is $a\Delta T$ plus quadratic curvature.
- $(\nabla a)(\nabla E)$ terms $\to B_1*\nabla\operatorname{Ric}=B_1*\nabla T$ (Bianchi turns $\nabla\operatorname{Ric}$ into a contraction of $\nabla T$).
- $(\nabla^2a)E$ terms $\to B_2*E=B_2*\operatorname{Ric}(T)=B_2*T$ — **and this is where the shift matters**: because $E=\operatorname{Ric}(T)$ with no constant, there is **no $B_2*g$, i.e. no bare $B_2$ term**.
- reaction $\operatorname{Rm}*v=a\,\operatorname{Rm}*E=a(T-G)*\operatorname{Ric}(T)=a(T*T+T)$; the $-G*\operatorname{Ric}(T)$ piece is $a$-linear in $T$, not a constant.
- $\partial_tG=\tfrac1{n-1}v\owedge g=-\tfrac2{n-1}(aE)\owedge g$, algebraic in $V$, hence of $aT$-linear type.

Collecting, the correct star-contraction base equation is
$$
\boxed{\;\partial_tT=a\Delta T+B_1*\nabla T+B_2*T+a\,(T*T+T)\;}
$$
with **no $+a\cdot1$ forcing**. Multiplying by $a$ and using $\Delta U=a\Delta T+2B_1\!\cdot\!\nabla T+(\Delta a)T$, $\nabla U=a\nabla T+B_1*T$, $aB_2*T=B_2*U$, $a^2(T*T+T)=U*U+aU$, and $B_1*B_1=4a\,C_1*C_1$ so $(B_1*B_1)*T=4(C_1*C_1)*U$, gives
$$
\boxed{\;\partial_tU=a\Delta U+B_1*\nabla U+B_2*U+4(C_1*C_1)*U+U*U+aU\;}
$$
with **no $+a^2$ forcing**.

**Stationarity test.** For hyperbolic data $\operatorname{Rm}=-G$ (constant curvature $-\tfrac1{n-1}$, $\operatorname{Ric}=-g$, $E=0$), one has $T\equiv0$, $U\equiv0$; the metric is stationary, so $\partial_tT=\partial_tU=0$ must hold. In the corrected equations every term contains $T$, $\nabla T$, $\Delta T$, or $U$, so both right sides vanish identically. In Step 60's printed (1.5)–(1.6) the terms $a(T*T+T+\mathbf1)$ and $\dots+\mathbf{a^2}$ do **not** vanish at $T=U=0$; those two additive pieces are fictitious and must be removed. This confirms the correction already flagged in A01 Step 57 §3.1, now derived from the variation formula. (Step 60 §1 already prefers the identity (1.8) over "a fictitious bare $T$ coefficient," so the intent is present, but the displayed equations still carry the spurious constants.)

---

## 3. Which families survive, and whether any is missing

Applying $\nabla^m$ to the corrected base equations by Leibniz, the spatial commutator $[\nabla^m,\Delta]A=\sum\nabla^r\operatorname{Rm}*\nabla^sA$, and the time commutator (§6 below):

- Deleting $a\cdot1$ removes exactly the isolated $B_m$ summand inside Step 60 family (T6).
- Deleting $a^2$ removes exactly $\nabla^m(a^2)$ inside family (U7).

**No needed family disappears and no new family appears.** The derivation now produces strictly fewer terms than the printed list, all still of types (T1)–(T5) and (U1)–(U6) plus the harmless $B_r*U_{m-r}$/$B_r*T_{m-r}$ of (U7)/(T6). The removed pieces $B_m=\nabla^m(\chi^2)$ and $\nabla^m(a^2)$ were derivatives of a fixed smooth function, hence in $L^\infty\subset L^q$; had they been kept they would have contributed only a bounded "$+1$" forcing to the energy inequality. So their deletion does **not** alter energy closure — its significance is that with them present the written object is not the evolution of $T,U$ at all (it contradicts the stationary solution). The finite enumeration script tests integer allocations and exponent arithmetic; it passes with or without the spurious constants and therefore certifies none of the tensor identities in §1–§2. This is consistent with the notes' own statement that the script "checks the classification consequences … not the tensor identities."

---

## 4. The induction must start at $m=2$

The general current-pair estimate closes the residual (Step 60 (3.3)–(3.6))
$$
I_m=\int\chi\,|C_{m+1}|\,|U_1|\,|U_m|^{p-1}
$$
by treating $\|U_1\|_4$ as a **fixed prior-level constant**. At $m=1$ the current variable is $U_1$ itself, so $\|U_1\|_4$ is a norm of the unknown, multiplied by $\|f\|_4=\|\chi|U_1|^{p/2}\|_4$ (also the unknown). The product is quadratic in the highest available norm and cannot be linearly absorbed by one dissipation term; the estimate is circular at $m=1$. Hence the tower must run from $m=2$, taking the base layer $\{T_0,T_1,U_1,C_2\}\subset\bigcap_{q<\infty}L^q$ as separately established input. Step 56 supplement supplies exactly this: the signed-Hessian seed $T_0\in\bigcap_qL^q$ (its (1.1)), then the dedicated $(U_1,C_2)$ pair (its §3), then $T_1$ (its §4). So the chain is $T_0\to(U_1,C_2)\to T_1\to\big[(U_2,C_3)\to T_2\to\cdots\big]$, with the bracketed part being the $m\ge2$ induction. Applying the general residual at $m=1$ would be circular, matching A01 Step 57 §3.1.

---

## 5. The same-exponent residual is correct

Checking the Hölder/Sobolev arithmetic of (3.4)–(3.6) with $f=\chi|U_m|^{p/2}$, $V=U_m$, $Z=C_{m+1}$:

- Hölder $\|f\|_4\,\|Z\|_p\,\|U_1\|_4\,\|V\|_p^{p/2-1}$ closes: $\tfrac14+\tfrac1p+\tfrac14+\tfrac{p-2}{2p}=1$, with $\||V|^{p/2-1}\|_{2p/(p-2)}=\|V\|_p^{p/2-1}$. Dimensionally exact.
- 4D critical Sobolev ($2^*=4$) on $f$: $\|f\|_4^2\le C_S(\|\nabla f\|_2^2+\|f\|_2^2)$, and $\|\nabla f\|_2^2\lesssim\|d\chi\|_\infty^2\|V\|_p^p+p^2\!\int\!\chi^2|V|^{p-2}|\nabla V|^2$. The weight $\chi^2=a$ is precisely the degenerate diffusion weight $D^U_{m,p}=\int a|\nabla V|^2|V|^{p-2}$. Hence $\|f\|_4^2\le C_S(p^2D^U_{m,p}+C_{p,r}\|V\|_p^p)$ — (3.5) is right, and it is exactly this $a=\chi^2$ matching that lets the degenerate operator control the critical norm.
- Young then gives $I_m\le\varepsilon D^U_{m,p}+C_{m,p,\tau}(1+\|Z\|_p^p+\|V\|_p^p)$: the current variables stay at exponent $p$ in both slots.
- The cutoff evolution (2.6) tested against $|Z|^{p-2}Z$ contributes the top coupling $U_m*C_1$ with $\|C_1\|_\infty=\|d\chi\|_\infty$ bounded, again same-exponent. So (3.7) closes the pair, and afterward (3.8) closes $T_m$. Verified.

---

## 6. Commutator ordering: the load-bearing subtlety in (2.6)

$\partial_t\Gamma=g^{-1}*\nabla V=g^{-1}*\operatorname{Ric}(\nabla U)=g^{-1}*U_1$, so $\nabla^r(\partial_t\Gamma)=g^{-1}*U_{r+1}$, and the time commutator at stage $m$ introduces $U_{r+1}$ with $r\le m-1$, i.e. at most the current $U_m$ — never $U_{m+1}$ in the $U$-equation. Good.

For the cutoff, a **direct** application of the generic time-commutator formula to $\nabla^{m+1}\chi$ would suggest a top term $\nabla^m(\partial_t\Gamma)*\chi=U_{m+1}*\chi$, one order above the current pair, which would break triangularity. This term does **not** occur. The reason is that $\nabla\chi=d\chi$ is metric-independent, so $\partial_t\nabla\chi=0$: the connection first acts at the second covariant derivative. Concretely
$$
\partial_tC_2=-\partial_t\Gamma*d\chi=U_1*C_1,\qquad
\partial_tC_3=U_2*C_1+U_1*C_2,
$$
and in general $C_{m+1}=\nabla^m\omega$ with $\omega=d\chi$ fixed, giving top term $\nabla^{m-1}(\partial_t\Gamma)*\omega=U_m*C_1$. So (2.6) — "$\partial_tC_{m+1}=U_m*C_1+\sum_{1\le j<m}U_j*C_{m+1-j}+\mathcal R_m$, no $U_{m+1}$, no $C_{m+2}$" — is correct, but its justification rests on the scalar-truncation $\partial_t\nabla\chi=0$, not on the generic commutator count. This should be stated explicitly, because the generic count applied to a scalar overcounts by one derivative and would falsely place $U_{m+1}$ in the cutoff equation.

The complementary point in the $U$-equation: the spatial commutator produces $a\nabla^m\operatorname{Rm}*U_0=a T_m*U_0$, i.e. the current unweighted $T_m$ appears **only weighted by $a$**. The identity $aT_m=U_m-\sum_{q=1}^mB_q*T_{m-q}$ (Step 60 (2.5)) converts it to the current pair variable $U_m$ plus prior levels. Thus no unweighted $T_m$ enters the $(U_m,C_{m+1})$ estimate, which is why the pair closes before $T_m$ is known. Verified. The coefficient bound uses $aT_0=U_0$ and $a\operatorname{Rm}=U_0-aG$, both bounded by $K$ on the slab.

---

## 7. Signed-Hessian handling of the cutoff-Hessian current term

The term $B_2*U_m$ (and $B_2*T_m$) has coefficient $B_2=2\chi C_2+2C_1\otimes C_1$; here $C_2=\nabla^2\chi$ is time-dependent through $\Gamma(t)$ and is only in $L^q$, not $L^\infty$. It is handled by one integration by parts (Step 56 (2.1), Step 60 (3.2)):
$$
\Big|\int(\nabla_i\nabla_ja)\,\mathcal B^{ij}(V)\Big|\le\varepsilon\!\int a|\nabla V|^2|V|^{p-2}+C_{p,\varepsilon}\|C_1\|_\infty^2\|V\|_p^p,
$$
using $|B_1|^2/a=4|C_1|^2$ and $|\nabla\mathcal B(V)|\le C|V|^{p-1}|\nabla V|$. This uses only $\|d\chi\|_\infty$; no $\|\nabla^2\chi\|_\infty$ is required. This is essential and correctly invoked. The same mechanism absorbs the raised-order gradient $B_1*U_{m+1}=2\chi C_1*\nabla V$: because it carries the single $\chi=a^{1/2}$, $\int\chi|V|^{p-1}|\nabla V|\le D^{1/2}\|V\|_p^{p/2}\le\varepsilon D+C\|V\|_p^p$. In fact the entire architecture rests on the observation that every derivative exceeding the diffusion-controllable order arrives with an explicit $\chi$ (from differentiating $a=\chi^2$), except the single cutoff jet $\chi C_{m+2}*U_0$, which carries one $\chi$ and is closed by the 4D critical Sobolev step of §5. One must integrate only the $\chi C_{m+2}$ piece of $B_{m+2}=\nabla^{m+2}(\chi^2)$ and retain the $C_1*C_{m+1}$ piece as a bounded-coefficient same-exponent current term; integrating the whole $B_{m+2}$ would generate an unweighted $C_1*C_1*T_0*\nabla(|X|^{p-2}X)$ term that does not close (Step 56 §5). This selective integration is correct.

---

## 8. $C^\infty$ endpoint and autonomous jet splice

The unweighted tower (3.8) gives $T_m\in\bigcap_qL^q$ for every fixed $m$, hence $\nabla^m\operatorname{Rm}\in L^q$; with bilipschitz metrics and finite Sobolev constants this yields $\sup_{[\tau,T_*)}\|g(t)\|_{H^s(\bar g)}<\infty$ for all $s$. Since $\partial_tg=-2V$, $V=\operatorname{Ric}(U)$, and $\|\partial_tg\|_{H^s}\lesssim\sum_{k\le s}\|U_k\|_2<\infty$, the map $t\mapsto g(t)$ is uniformly continuous into every $H^s$ on the finite interval, so $g(t)\to g_*$ in $C^\infty$ and $g_*$ is positive definite from the integrated $\|aE\|_\infty$ bound. This is sound.

The splice is valid and does not use uniqueness. With $\mathcal F(g)=-2\chi^2(\operatorname{Ric}_g+g)$ autonomous and $\mathcal F_{\ell+1}=D\mathcal F_\ell[\mathcal F]$, one has $\partial_t^\ell g(t)=\mathcal F_\ell(g(t))\to\mathcal F_\ell(g_*)$ in $C^\infty$ because $\mathcal F_\ell$ is continuous in the $C^\infty$ topology; any restart $\widehat g$ from $g_*$ solving the same autonomous equation satisfies $\partial_s^\ell\widehat g(0)=\mathcal F_\ell(g_*)$. All one-sided space-time jets match, and a one-variable function whose derivatives all extend continuously across $T_*$ is $C^\infty$ there. So the chosen branch extends smoothly past any finite $T_*$ at which $\|U\|_\infty$ stays finite, contradicting maximality if $T_*<\theta r^2$. This correctly replaces the invalid ungauged $L^2$ difference estimate (Step 60 §4, A01 §1): the ungauged Ricci symbol $\sigma_\xi(DF)(h)=a(-|\xi|^2h-\xi\!\otimes\!\xi\operatorname{tr}h+2\,\xi\odot(\xi\!\cdot\!h))$ is indefinite on the trace-adjusted directions (e.g. $h=\operatorname{diag}(1,-\varepsilon,0,0)$ gives $\langle\sigma_\xi(DF)h,h\rangle=\varepsilon-\varepsilon^2>0$), so no coercive raw-difference estimate exists, and the jet splice is the correct substitute.

Two dependencies attach here and remain conditional, not reproved in these notes: (a) $\|U\|_\infty\le K$ on $[\tau,T_*)$, which is drawn from the first-exit output $\|aF_T(t)\|_\infty\le C\gamma/t$ (finite on a terminal slab $[T_*/2,T_*)$ but growing as $T_*\downarrow0$); (b) the whole tower runs with $\tau>0$ fixed, and the constants $C_{m,p,\tau}$ grow as $\tau\to0$ — acceptable because only terminal behavior near a fixed $T_*$ is used.

---

## 9. Assessment and further load-bearing points

The corrected hierarchy closes, given the base layer of §4 and the conditional inputs of §8. I did not find an additional term that breaks closure. The genuinely load-bearing facts, each of which the enumeration script does not certify and each of which I verified by hand, are:

1. $E=\operatorname{Ric}(T)$ exactly, so the base reaction is $a(T*T+T)$ with no additive constant; the fictitious $a\cdot1,\,a^2$ must be deleted (§2). This is not cosmetic: because the reaction is $a$-weighted, every current-order factor $T_m$ inside it appears as $aT_m=U_0*(\cdot)$-coefficient or converts to $U_m$; a bare (un-$a$-weighted) reaction would produce current $T_m$ with a coefficient uncontrolled on the $\chi\to0$ collar, and the energy would not close there.
2. $(B_1*B_1)*T=4(C_1*C_1)*U$ and $aT_m=U_m-\sum_qB_q*T_{m-q}$ (§2, §6), which keep the $U$-pair free of unweighted current $T_m$.
3. $\partial_t\nabla\chi=0$, truncating the cutoff-evolution top term from $U_{m+1}$ to $U_m*C_1$ (§6) — the single point where the generic commutator count would mislead.
4. Selective integration of only $\chi C_{m+2}$, closed by the 4D $L^4$ critical Sobolev estimate; the same-exponent residual is arithmetically exact (§5, §7).
5. The signed-Hessian device removing all dependence on $\|\nabla^2\chi\|_\infty$ (§7).

Points where the argument is real but rests on inputs proved elsewhere: the base layer $\{T_0,T_1,U_1,C_2\}\subset\bigcap_qL^q$ (Step 56 supplement), and the first-exit bound feeding $\|U\|_\infty\le K$. The 4D $L^4$ Sobolev step is specific to $n=4$; the same residual in dimension $n$ carries $2^*=2n/(n-2)$ and different Hölder exponents, so nothing here transfers to $n\ge5$ as written. All of this is internal to the four-dimensional $\operatorname{Ric}=-g$ (hyperbolic-sign) Ishida–LeBrun component and does not by itself address the $\lambda>0$ branch, general four-manifold topology, or the full Yau 26 statement.

Net: after deleting the fictitious $a\cdot1$ and $a^2$, the base equations are the ones derived in §2; the family list loses only the two isolated bounded-forcing pieces and gains nothing; the induction must begin at $m=2$; and the same-exponent residual, commutator ordering, $C^\infty$ endpoint, and autonomous jet splice are each correct with the identities and inputs named above. The one presentational correction that materially affects reading is that Step 60's displayed (1.5)–(1.6) still print the spurious constants, and the derivation of (2.6) should record the $\partial_t\nabla\chi=0$ truncation rather than the generic commutator formula.