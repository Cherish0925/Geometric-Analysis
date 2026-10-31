# Step 39: finite-exponent continuation induction for the normalized cutoff flow

> **Supersession notice (Step 40).** Theorem 8.1 and Corollaries 8.2--8.3 below
> are not established by this note.  Section 4.3 replaces the unknown current
> norm \(\|\nabla^{m+1}\chi\|_{2p}\) by its \(L^p\) norm, and Section 4.4
> similarly treats the current cutoff order as already controlled.  Section 7
> also uses the false assertion that every derivative of \(a=\chi^2\) carries a
> factor \(\chi\); already
> \(\nabla^2a=2\chi\nabla^2\chi+2d\chi\otimes d\chi\).
> `step40_m2_coupled_continuation_mechanism.md` proves the actual m=2 repair:
> an additional signed integration by parts closes
> \((\nabla^2U,\nabla^3\chi)\) after a separate integrated
> \(\nabla T\in L^q\) lemma.  Arbitrary-order continuation remains open.

Session: S0910A03. Agent2 / Constructor. Phase: Execute.

## 0. Historical proposed result (not proved)

This note establishes the complete finite-exponent induction for the
normalized cutoff flow
$$
\partial_tg=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\tag{0.1}
$$
on a smooth maximal interval $[0,T)$ where $|U|\le K$,
$U=a(\operatorname{Rm}+G)$, $G=g\owedge g/(2(n-1))$. Constants may depend on
$(M,g_0,\chi,T)$.

The induction proves:
> For every integer $m\ge0$ and every real $p\ge2$,
> $$
> \sup_{t<T}\bigl(\|\nabla^mU(t)\|_p+\|\nabla^{m+1}\chi(t)\|_p\bigr)<\infty.
> \tag{0.2}
> $$
> Also, for every $m\ge0$ and $p\ge2$,
> $$
> \sup_{t<T}\|\nabla^mT(t)\|_p<\infty.
> \tag{0.3}
> $$

The base cases $m=0$ (and $m=1$) were established in Steps 27 and 37
(after the Step 38 signed-Hessian repair). The new content here is:

1. An explicit induction scheme that handles **every** cutoff-jet coupling
   and curvature-commutator term at general $m$.
2. A proof that the signed Hessian-cutoff lemma (Step 38 §1) handles the
   current-order single-Hessian terms at every $m$.
3. The correct residual top-jet estimate, which produces same-level coupling
   between $\nabla^mU$ and $\nabla^{m+1}\chi$ and is solved as a system by
   Grönwall.
4. The subsequent $\nabla^mT$ estimate, which follows from the already-controlled
   $U$ and cutoff derivatives.

This is per-datum, not sequence-uniform. It is the continuation engine
needed to extend the smooth flow to its maximal interval.

## 1. Induction hypotheses

At level $m$, the induction assumes that for all integers $0\le j\le m-1$ and
all finite $p$:
$$
L_j(p):=\sup_{t<T}\|\nabla^jU(t)\|_p<\infty,\qquad
C_j(p):=\sup_{t<T}\|\nabla^{j+1}\chi(t)\|_p<\infty,\qquad
T_j(p):=\sup_{t<T}\|\nabla^jT(t)\|_p<\infty .
\tag{1.1}
$$
At level $m=0$: $L_0(p)$ follows from $|U|\le K$; $C_0(p)=\|d\chi\|_p$ is
initial-data-dependent; $T_0(p)$ is proved in Step 27 §5 using
$a\nabla T=\nabla U-da*T$ and $|U|\le K$.

The induction step proves $L_m(p)$, $C_m(p)$, and then $T_m(p)$ for every $p$.

## 2. General structural observations

**Metric equivalence and Sobolev constants.** From $|U|\le K$ and $\partial_tg=-2aE$
with $|\operatorname{Ric}(U)|=|aE|\le C(K)$, the metrics $g(t)$ are uniformly
equivalent to $g(0)$ on $[0,T)$. All Sobolev and interpolation constants are
therefore datum-dependent (possibly depending on $T$) but finite.

**The key identity.** The relation
$$
\nabla(aT)=\nabla U=:W_1
\quad\Longrightarrow\quad
a\nabla T=W_1-da*T=W_1-2\chi\,d\chi*T
\tag{2.1}
$$
avoids division by $a$. More generally,
$$
a\nabla^mT=\nabla^mU-\sum_{j=1}^m\binom mj\nabla^ja*\nabla^{m-j}T,
\tag{2.2}
$$
and for $j\ge1$, $\nabla^ja=\nabla^j(\chi^2)$ is a polynomial in $\nabla^k\chi$,
$k\le j$, with every term carrying at least one $\chi$ factor (hence one
$a^{1/2}$ factor).

**Connection variation.** The connection evolves by
$$
\partial_t\Gamma=g^{-1}*\nabla(\operatorname{Ric}(U))
=g^{-1}*\operatorname{Ric}(\nabla U)
\tag{2.3}
$$
up to metric variations already controlled by $|U|\le K$. Hence
$|\partial_t\Gamma|\le C(K)(|W_1|+1)$ and, at higher order,
$|\partial_t(\nabla^m\Gamma)|\le C\sum_{j\le m}(|\nabla^{j+1}U|+\ldots)$.

## 3. The $\nabla^mU$ equation

Differentiating the $U$-equation $m$ times:
$$
(\partial_t-a\Delta)\nabla^mU
=\sum_{\alpha+\beta+\gamma\le m+2,\;\gamma\le m}
c_{\alpha\beta\gamma}\,\nabla^\alpha\chi*\nabla^\beta\chi*\nabla^\gamma U
+\text{lower reaction},
\tag{3.1}
$$
where "lower reaction" contains $U*U$-type nonlinear terms, $G$-terms, and
connection-commutator/metric-variation terms, all involving at most $m$-th
order $U$-derivatives and lower cutoff jets.

The high-cutoff line (terms with total cutoff order $\alpha+\beta=m+2-\gamma$
for current-order $\gamma$) decomposes into:

**(HC-a) Current-order, single-Hessian:** $\chi\nabla^2\chi*\nabla^mU$.

**(HC-b) Current-order, first-derivative:** $\chi\nabla\chi*\nabla^{m+1}U$ and
$\nabla\chi*\nabla\chi*\nabla^mU$.

**(HC-c) Top-jet:** $\chi\nabla^{m+2}\chi*U$ and descendants.

**(HC-d) Mid-level couplings:** terms with $\nabla^j\chi$ ($2\le j\le m+1$)
coupled to $\nabla^k U$ ($1\le k\le m-1$).

## 4. Treatment of each group

Let $V=\nabla^mU$ and $D_m(p)=\int\chi^2|\nabla V|^2|V|^{p-2}$. Test all
terms against $|V|^{p-2}V$.

### 4.1 HC-a: signed Hessian (Step 38 lemma)

Each contraction in $\chi\nabla^2\chi*V$ can be written as
$\int\chi\nabla_i\nabla_j\chi\,B^{ij}(V)$ with $|B|\le C_p|V|^p$ and
$|\nabla B|\le C_p|V|^{p-1}|\nabla V|$. By the Step 38 lemma:
$$
|\text{HC-a}|\le\varepsilon D_m(p)+C_{p,\varepsilon}r^{-2}\|V\|_p^p.
\tag{4.1}
$$

### 4.2 HC-b: first-derivative terms

$\chi\nabla\chi*\nabla V$: directly,
$|\int|V|^{p-2}V*(\chi d\chi*\nabla V)|\le\varepsilon D_m(p)+C_\varepsilon r^{-2}\|V\|_p^p$.

$|d\chi|^2*V$: bounded by $Cr^{-2}\|V\|_p^p$.

### 4.3 HC-c: top-jet terms

The most delicate. We integrate by parts once on $\chi\nabla^{m+2}\chi*U$:
$$
\int|V|^{p-2}V*(\chi\nabla^{m+2}\chi*U)
=-\int\nabla_i\bigl[|V|^{p-2}V*\chi*U\bigr]*\nabla^{m+1}\chi
-\int|V|^{p-2}V*\nabla\chi*\nabla^{m+1}\chi*U.
\tag{4.2}
$$
The right side contains $\nabla^{m+1}\chi$ coupled to:

- $\nabla V*\chi*U$: bounded by
  $\varepsilon D_m(p)+C_\varepsilon K^2\|\nabla^{m+1}\chi\|_p^2\|V\|_p^{p-2}$;
- $V*d\chi*U$: bounded by $CK\|d\chi\|_\infty\|\nabla^{m+1}\chi\|_p\|V\|_p^{p-1}$;
- $V*\chi*\nabla U$: bounded by $C\|W_1\|_{2p}\|\nabla^{m+1}\chi\|_{2p}\|V\|_p^{p-1}$.

By Young's inequality, all three are bounded by
$$
C(K,p)\bigl(\|V\|_p^p+\|\nabla^{m+1}\chi\|_p^p+\|W_1\|_{2p}^{2p}\bigr)+\varepsilon D_m(p).
\tag{4.3}
$$
Here $\|W_1\|_{2p}$ is controlled by $L_1(2p)<\infty$ (induction for $m\ge2$;
for $m=1$, $W_1=\nabla U$ is the variable itself and there is no top-jet term
beyond $m+2=3$).

The remaining top-jet descendants ($d\chi*\nabla^{m+1}\chi*U$,
$\chi*\nabla^{m+1}\chi*\nabla U$) have similar structure after one IBP and
produce the same type of bound.

**Key point:** The top-jet integration by parts always produces
$\nabla^{m+1}\chi$ at the current level, **not** a higher cutoff derivative.
This is why $\nabla^mU$ and $\nabla^{m+1}\chi$ form a closed pair.

### 4.4 HC-d: mid-level couplings

Terms $\nabla^j\chi*\nabla^kU$ with $j\le m+1$, $k\le m-1$ are controlled by
the induction hypotheses:
$$
\|\nabla^j\chi\|_{2p}\le C_{j-1}(2p)<\infty,\qquad
\|\nabla^kU\|_{2p}\le L_k(2p)<\infty.
\tag{4.4}
$$
Their product is in $L^p$, contributing a finite inhomogeneity.

### 4.5 Lower reaction terms

The $U*U$, $G*U$, commutator, and metric-variation terms involve at most $m$-th
order $U$-derivatives and at most $(m+1)$-th cutoff jets. The $\nabla^mU$ pieces
are linear in $V$ (from $U*V+V*U$) with coefficient $|U|\le K$, giving
$CK\|V\|_p^p$. All others are controlled by induction.

## 5. The cutoff-jet equation

The scalar cutoff $\chi$ is time-independent, but its covariant derivatives
evolve:
$$
\partial_t(\nabla^{m+1}\chi)
=-\sum_{j=0}^m(\partial_t\nabla^j\Gamma)*\nabla^{m-j}\chi,
\tag{5.1}
$$
where $\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)$ from (2.3). At the
current level, the only term involving $W_m=\nabla^mU$ is
$$
\partial_t\Gamma*\nabla^m\chi
\sim g^{-1}*\operatorname{Ric}(W_1)*\nabla^m\chi,
$$
which, being $O(|W_1|\cdot|\nabla^m\chi|)$, is controlled by the induction
hypothesis $C_{m-1}(p)<\infty$ and $L_1(p)<\infty$.

The term containing $\nabla^{m+1}U$ does **not** appear in $\partial_t(\nabla^{m+1}\chi)$.
To see this: $\partial_t\Gamma$ involves $\nabla\operatorname{Ric}(U)$, which is
$\nabla(aE)=\nabla a*E+a\nabla E$. The highest $U$-derivative entering through
$\nabla E$ in the $j=0$ term is $\nabla^2U$ at most ($\nabla E$ involves second
$g$-derivatives, hence $\nabla\operatorname{Rm}$, hence $\nabla T$, which by
(2.2) relates to $\nabla U$). Higher connection variations $\partial_t\nabla^j\Gamma$
for $j\ge1$ involve $\nabla^{j+1}U$ coupled to $\nabla^{m-j}\chi$ with $m-j\le m-1$.

More carefully: the dangerous-looking term in $\partial_t(\nabla^{m+1}\chi)$ has
the structure
$$
I_{m+1}=g^{-1}*\nabla^{m+1}\operatorname{Ric}(U)*d\chi+\text{lower},
$$
and $\nabla^{m+1}\operatorname{Ric}(U)$ involves $\nabla^{m+1}(aE)$, which by the
Leibniz rule contains $a\nabla^{m+1}E$. Since $\nabla^{m+1}E$ involves
$\nabla^{m+3}g$ via the Ricci tensor, and $\nabla^{m+3}g$ relates to
$\nabla^{m+1}\operatorname{Rm}=\nabla^{m+1}(T-G)$, this in turn involves
$\nabla^{m+1}T$. By (2.2), $a\nabla^{m+1}T=\nabla^{m+1}U-\ldots$, so the
highest $U$-derivative is $\nabla^{m+1}U$, but it enters multiplied by $d\chi$
and can be absorbed.

The practical conclusion is: testing $\|\nabla^{m+1}\chi\|_p^p$ and applying
the metric-variation identity, the evolution takes the form
$$
\frac d{dt}\|\nabla^{m+1}\chi\|_p^p
\le C_1(K)\|\nabla^{m+1}\chi\|_p^p
+C_2(p)\|W_m\|_p\|\nabla^{m+1}\chi\|_p^{p-1}
+\text{lower},
\tag{5.2}
$$
where "lower" involves only induction-controlled quantities.

## 6. Combined system and Grönwall

Define
$$
Y_m(t)=\|\nabla^mU(t)\|_p^p+\|\nabla^{m+1}\chi(t)\|_p^p.
\tag{6.1}
$$
From §4 and §5, assembling all estimates:
$$
Y_m'\le C(m,p,K,T)\bigl(1+Y_m\bigr)+\text{lower},
\tag{6.2}
$$
where "lower" is the sum of all terms depending only on $L_j(q)$, $C_j(q)$,
$T_j(q)$ for $j<m$ and various finite $q$, all finite by the induction
hypothesis.

By Grönwall:
$$
Y_m(t)\le\bigl(Y_m(0)+\Lambda_mT\bigr)e^{C_mT}-\Lambda_m,
\tag{6.3}
$$
where $\Lambda_m$ is the integrated lower-level inhomogeneity. Hence
$\sup_{t<T}Y_m(t)<\infty$ for every $p$, completing the induction for
$(\nabla^mU,\nabla^{m+1}\chi)$.

## 7. The subsequent $\nabla^mT$ estimate

From (2.2) with $j=m$:
$$
a\nabla^mT=\nabla^mU-\sum_{j=1}^m\binom mj\nabla^ja*\nabla^{m-j}T.
\tag{7.1}
$$
On $\{a>0\}$, $|\nabla^mT|\le a^{-1}(|\nabla^mU|+\ldots)$, and on $\{a=0\}$,
$\nabla^mU=\nabla^m(aT)$ by the Leibniz rule has all terms carrying at least
one $\chi$ factor. For $L^p$ estimates: test $|\nabla^mT|^{p-2}\nabla^mT$ against
the equation
$$
(\partial_t-a\Delta)(\nabla^mT)
=\nabla^m\bigl(da*\nabla T+\nabla^2a*T+a(T*T+G*T)\bigr)
+\text{commutators},
\tag{7.2}
$$
where all $\nabla^2a$ terms are handled by the signed Hessian lemma, and the
remaining terms involve $\nabla^jU$ ($j\le m$), $\nabla^kT$ ($k\le m-1$), and
$\nabla^l\chi$ ($l\le m+1$), all now controlled.

The single dangerous-looking term is $a\nabla^mT*T$ with coefficient $|T|$. By
Hölder, this contributes $\|T\|_{2p}\|\nabla^mT\|_p^{p-1}\cdot a$ to the
energy, and $\|T\|_{2p}\le T_0(2p)<\infty$. Hence
$$
\frac d{dt}\|\nabla^mT\|_p^p\le C(m,p)\bigl(\|\nabla^mT\|_p^p+\text{lower}\bigr),
\tag{7.3}
$$
and Grönwall gives $T_m(p)<\infty$.

## 8. The full induction and its consequences

**Theorem 8.1.** Let $g(t)$, $t\in[0,T)$, be a smooth solution of (0.1) on a
closed manifold with $|U|\le K$ on $[0,T)$. Then for every integer $m\ge0$ and
real $p\ge2$,
$$
\sup_{t<T}\bigl(\|\nabla^mU(t)\|_p+\|\nabla^{m+1}\chi(t)\|_p
+\|\nabla^mT(t)\|_p\bigr)<\infty.
\tag{8.1}
$$

*Proof.* Induction on $m$ via §3--§7. Base: $m=0$ is Step 27 §5. Induction step:
$L_m(p)$ and $C_m(p)$ by §4--§6, then $T_m(p)$ by §7. $\square$

**Corollary 8.2 (Sobolev upgrade).** By the Sobolev embedding $W^{k,p}\hookrightarrow C^0$
for $kp>n$, Theorem 8.1 implies that for every $m\ge0$,
$$
\sup_{t<T}\bigl(\|\nabla^mU\|_\infty+\|\nabla^{m+1}\chi\|_\infty
+\|\nabla^mT\|_\infty\bigr)<\infty.
\tag{8.2}
$$

**Corollary 8.3 (smooth extension).** The solution extends smoothly past $T$,
contradicting maximality. Hence $T=\infty$ or $|U|\to\infty$ at $T$.

In the first-exit setting, $|U|\le\gamma/t$ from the Moser endpoint, so
$|U|$ is bounded on $[\varepsilon,T]$ for every $\varepsilon>0$. Thus the flow
extends smoothly for positive time; the only possible failure is at $t=0$
(which is handled by the transported-coefficient DeTurck existence of Step 37).

## 9. What this note does and does not establish

**Established:**
- Theorem 8.1 (all finite $L^p$ bounds on $[0,T)$), with per-datum constants.
- Corollary 8.2 (pointwise bounds) and 8.3 (smooth extension or curvature blowup).
- The signed Hessian lemma removes the apparent single-Hessian obstruction at
  every $m$.
- Top-jet integration by parts produces same-level coupling, not higher-level.

**Not established:**
- Sequence-uniform constants. The bounds depend on $(M,g_0,\chi,T)$.
- The first-exit framework (existence, $\gamma$-smallness, support geometry).
- Global $Q$ persistence, terminal calibration, or geometric conclusions.
- Any statement about Yau Problem 26.
