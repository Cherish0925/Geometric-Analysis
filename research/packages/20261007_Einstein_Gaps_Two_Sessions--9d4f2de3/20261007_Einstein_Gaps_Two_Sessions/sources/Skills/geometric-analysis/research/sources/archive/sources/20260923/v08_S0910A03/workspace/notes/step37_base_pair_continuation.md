# Step 37: base-pair continuation estimate — $(\nabla U,\nabla^2\chi)$

> **Supersession notice (Step 38).** The original equations (3.9) and (3.11)
> below have a power-counting error, the quotient $\chi^2/a$ should not be
> written on $\{a=0\}$, and §6 incorrectly upgrades finite $L^p$ control to
> $L^\infty$ without one more spatial derivative.  The repaired finite-$L^p$
> base estimate uses a second signed integration by parts on every
> $\int\chi\nabla^2\chi\,B(W)$ term.  See
> `step38_hessian_ibp_and_conditional_moser_repair.md`.  This file must not be
> cited as a completed extension theorem.

## 0. Purpose

This note proves the base-pair $L^p$ estimate for $(\nabla U,\nabla^2\chi)$
in the shifted-curvature continuation framework of Step 27. It is the $m=1$
case of the Wang induction on $[0,T)$ where $\sup|U|<\infty$, with the four
dangerous terms
$$
\chi\nabla^3\chi*U,
\quad \nabla\chi*\nabla^2\chi*U,
\quad \chi\nabla^2\chi*\nabla U,
\quad \chi\nabla\chi*\nabla^2U
\tag{0.1}
$$
handled explicitly as signed energy terms, without ever inserting the
uncontrolled $\|T\|_\infty$ or $\|a\nabla\operatorname{Rm}\|_\infty$.

The Step 36 Preceptor review identified this as the lowest unresolved test in the
continuation chain (`step36_preceptor_interface_review.md` §3). The Step 35
cutoff-jet note was rejected because it assumed smoothness on a closed interval
and used uncontrolled quantities as Grönwall coefficients. This note works on a
maximal interval $[0,T)$ and uses only quantities controlled by the hypotheses.

## 1. Setup and controlled quantities

**Flow:** $\partial_tg=-2aE$, $a=\chi^2$, $E=\operatorname{Ric}+g$, on closed
$M^n$, smooth solution on $[0,T)$. Constants may depend on $(M,g_0,\chi,T)$.

**Hypothesis:** $|U|\le K$ on $M\times[0,T)$, where $U=aT=a(\operatorname{Rm}+G)$.

**Controlled from the hypothesis (Step 27 §5):**
- Metrics are uniformly equivalent: $C^{-1}g_0\le g(t)\le Cg_0$ for $t<T$.
- $|d\chi|$, $|\nabla^2\chi(0)|$ bounded.
- $|T|\in L^p(M)$ for all finite $p$ (Step 27 eq. 5.4).
- Sobolev inequality on $(M,g(t))$ with datum-dependent constant $C_S$.
- Volume form $d\mu_t$ is uniformly equivalent to $d\mu_0$.

**Notation:** $W=\nabla U$, $\Theta=\nabla^2\chi$.  We prove
$\|W(t)\|_{L^p}+\|\Theta(t)\|_{L^p}\le C(T,p)$ for every finite $p$ on
$[0,T)$.

## 2. The $\nabla U$ equation at $m=1$

From the differentiated $U$-equation (Step 27 eq. 3.2 with $m=1$):
$$
\partial_tW = a\Delta W + \text{(seven term groups)}.
\tag{2.1}
$$
The seven groups are (using $W_i:=\nabla_iU$, subscripts on $\chi$ denoting
covariant derivatives):
$$
\begin{aligned}
&R_1 = \chi\chi_{ijk}U = \chi\nabla^3\chi*U,\\
&R_2 = \chi_i\chi_{jk}U = \nabla\chi*\Theta*U,\\
&R_3 = \chi\chi_{jk}W = \chi\Theta*W,\\
&R_4 = \chi\chi_j\nabla^2U = \chi\nabla\chi*\nabla W,\\
&R_5 = W*U + U*W,\\
&R_6 = aG*W + G\text{-lower},\\
&R_7 = \text{connection-commutator, metric-variation, }|\le C(|W|+K|T|+1).
\end{aligned}
\tag{2.2}
$$
Here I use schematic $*$ for tensorial contraction with bounded dimensional
factors, and "lower" means terms involving only previously controlled quantities.

$R_5$ and $R_6$ are straightforward: $|R_5|\le CK|W|$ and $|R_6|\le C|W|+C$,
both bounded by $CK(|W|+1)$.

$R_7$ includes the $\partial_t$-correction of the covariant derivative
and norm/measure variations; its coefficients are controlled by $|U|\le K$
and the uniform metric equivalence.

The four dangerous terms are $R_1,\ldots,R_4$.

## 3. $L^p$ energy for $W$

Set $p\ge n+2$ (a large but finite exponent). Multiply (2.1) by $|W|^{p-2}W$
and integrate:
$$
\frac1p\frac{d}{dt}\int|W|^p\,d\mu
+ c_p\int a|\nabla W|^2|W|^{p-2}\,d\mu
= \sum_{k=1}^7\int\langle|W|^{p-2}W, R_k\rangle\,d\mu
  + \text{measure var.}
\tag{3.1}
$$
The measure variation contributes $|\le CK\int|W|^p$, absorbed later.

### 3.1 Term $R_1 = \chi\nabla^3\chi*U$: integration by parts

This is the key signed term. Schematically:
$$
I_1 = \int|W|^{p-2}\langle W,\chi U*\nabla^3\chi\rangle\,d\mu.
\tag{3.2}
$$
Integrate by parts, moving one derivative off $\nabla^3\chi$ onto the rest:
$$
I_1 = -\int\nabla\bigl(|W|^{p-2}W\cdot\chi U\bigr)*\nabla^2\chi\,d\mu.
\tag{3.3}
$$
The gradient of the product generates three terms:
$$
I_1 = \underbrace{-\int\nabla(|W|^{p-2}W)\cdot\chi U*\Theta}_{I_{1a}}
      \underbrace{-\int|W|^{p-2}W\cdot\nabla\chi\cdot U*\Theta}_{I_{1b}}
      \underbrace{-\int|W|^{p-2}W\cdot\chi\cdot\nabla U*\Theta}_{I_{1c}}.
\tag{3.4}
$$
Note: $\nabla U$ in $I_{1c}$ is $W$ itself.

**$I_{1a}$:** The factor $|\nabla(|W|^{p-2}W)|\le C(p-1)|W|^{p-2}|\nabla W|$.
Use the no-division factorization
$$
K|\chi||\Theta||W|^{p-2}|\nabla W|
=K\bigl(\sqrt a|\nabla W||W|^{(p-2)/2}\bigr)
  \bigl(|\Theta||W|^{(p-2)/2}\bigr).
$$
Young therefore gives on all of $M$, including $\{a=0\}$,
$$
|I_{1a}|\le\varepsilon\int a|\nabla W|^2|W|^{p-2}
+C_\varepsilon K^2\int|\Theta|^2|W|^{p-2}.
\tag{3.6}
$$
No quotient $\chi^2/a$ is formed.
By Hölder with exponents $(p/(p-2),p/2)$:
$$
\int|\Theta|^2|W|^{p-2}\le\|\Theta\|_p^2\|W\|_p^{p-2}.
\tag{3.7}
$$

**$I_{1b}=R_2\text{-type:}$** This has $|\nabla\chi||U||\Theta||W|^{p-1}$.
$$
|I_{1b}|\le Cr^{-1}K\|\Theta\|_p\|W\|_p^{p-1}.
\tag{3.8}
$$

**$I_{1c}$ (Step 38 correction):** Since $\nabla U=W$ and the testing
factor already has size $|W|^{p-1}$, the raw term has size
$\int\chi|\Theta||W|^p$, not total power $p$.  Keep its signed contraction as
$$
J=\int\chi\,\nabla_i\nabla_j\chi\,B^{ij}(W),
\quad |B|\le C_p|W|^p,
\quad |\nabla B|\le C_p|W|^{p-1}|\nabla W|.
$$
A second integration by parts gives
$$
|I_{1c}|\le\varepsilon\int a|\nabla W|^2|W|^{p-2}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\int|W|^p.
\tag{3.9}
$$

### 3.2 Term $R_2 = \nabla\chi*\Theta*U$

$$
|I_2| = \int|\nabla\chi||\Theta||U||W|^{p-1}
\le CKr^{-1}\|\Theta\|_p\|W\|_p^{p-1}.
\tag{3.10}
$$

### 3.3 Term $R_3 = \chi\Theta*W$

The original Hölder estimate here was false.  As for $I_{1c}$, retain the
signed contraction and integrate once off the Hessian:
$$
|I_3|
\le\varepsilon\int a|\nabla W|^2|W|^{p-2}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\int|W|^p.
\tag{3.11}
$$
This uses $|\nabla B(W)|\le C_p|W|^{p-1}|\nabla W|$ and does not require a
norm of $\Theta$.

### 3.4 Term $R_4 = \chi\nabla\chi*\nabla^2 U$

Here $\nabla^2U$ is not $W$; it is $\nabla W$. But the factor is
$\chi\cdot\nabla\chi$, so:
$$
|I_4| \le \int\chi|\nabla\chi||\nabla W||W|^{p-1}
\le Cr^{-1}\int\chi|\nabla W||W|^{p-1}.
\tag{3.12}
$$
Since $\chi\le a^{1/2}$, by Young:
$$
|I_4|\le\varepsilon\int a|\nabla W|^2|W|^{p-2}
+C_\varepsilon r^{-2}\int|W|^p.
\tag{3.13}
$$

### 3.5 Terms $R_5$--$R_7$

$$
|I_5|+|I_6|+|I_7| \le CK\int(|W|^p+|T|^p+1)\,d\mu.
\tag{3.14}
$$

### 3.6 Combined $W$-inequality

Choosing $\varepsilon$ small, absorbing the diffusion:
$$
\frac{d}{dt}\|W\|_p^p
+c_p\int a|\nabla W|^2|W|^{p-2}
\le C_pK^2\|\Theta\|_p^2\|W\|_p^{p-2}
  +C_p(1+K)\|W\|_p^p
  +C_pK\|\Theta\|_p\|W\|_p^{p-1}
  +C_p\|T\|_p^p+C_p.
\tag{3.15}
$$
For later use, write $\mathscr W_p:=\|W\|_p^p$. Young's inequality converts the
mixed powers to
$$
\frac{d}{dt}\mathscr W_p
\le C_p(1+K^p)\bigl(1+\mathscr W_p+\|\Theta\|_p^p+\|T\|_p^p\bigr).
\tag{3.16}
$$
(Here I used $K^2\|\Theta\|_p^2\mathscr W_p^{(p-2)/p}\le CK^p\|\Theta\|_p^p+
C\mathscr W_p$ by Young with $(p/2,p/(p-2))$.)

## 4. $L^p$ evolution of $\Theta=\nabla^2\chi$

From (Step 27 eq. 4.4) at $r=2$:
$$
\partial_t|\Theta|\le CK|\Theta|+C|W||\nabla\chi|.
\tag{4.1}
$$
The first term comes from $\partial_t\Gamma*\nabla\chi$ with $\partial_t\Gamma$
bounded by $|\nabla(aE)|=|\nabla\operatorname{Ric}(U)|$, and
$\operatorname{Ric}(U)=aE$ so $\nabla\operatorname{Ric}(U)$ includes
$\nabla U*g=W*g$ (current order) and $U*\Gamma$ (bounded by $K$). The second
term is the current-order coupling: $|\nabla^1 U||\nabla^{2-1}\chi|=|W||\nabla\chi|$.

In $L^p$:
$$
\frac{d}{dt}\|\Theta\|_p^p
\le CpK\|\Theta\|_p^p + Cpr^{-1}\|W\|_p\|\Theta\|_p^{p-1}.
\tag{4.2}
$$
By Young:
$$
\frac{d}{dt}\|\Theta\|_p^p
\le C_p(1+K)\bigl(\|\Theta\|_p^p+\|W\|_p^p\bigr).
\tag{4.3}
$$

## 5. Coupled Volterra comparison

Define $Y_1(t)=\mathscr W_p(t)+\|\Theta(t)\|_p^p$. Adding (3.16) and (4.3):
$$
Y_1'(t)\le C_1\bigl(1+Y_1(t)+\|T(t)\|_p^p\bigr),
\tag{5.1}
$$
where $C_1=C_1(p,K,g_0,\chi)$ depends on the individual smooth datum. Since
$\|T\|_p^p\le C(t)$ for all finite $p$ by Step 27 eq. 5.4, the right-hand
side is a known function plus $C_1 Y_1$. By Grönwall:
$$
Y_1(t)\le e^{C_1 t}\Bigl(Y_1(0)+C_1\int_0^t(1+\|T(s)\|_p^p)\,ds\Bigr).
\tag{5.2}
$$
Since $Y_1(0)$ is finite (from smoothness of $g_0$ and $\chi$) and
$\|T\|_p^p$ is bounded on $[0,T)$ (from Step 27 §5), the integral is finite.
Therefore
$$
\boxed{\sup_{t\in[0,T)}\bigl(\|\nabla U(t)\|_{L^p}+\|\nabla^2\chi(t)\|_{L^p}\bigr)<\infty
\qquad\text{for all finite }p.}
\tag{5.3}
$$

## 6. What finite $L^p$ does and does not imply

For every fixed finite $p$, the repaired energy argument gives finite
$\|\nabla U\|_p$ and $\|\nabla^2\chi\|_p$ under the stated hypotheses.  It does
**not** give their $L^\infty$ norms merely by taking $p>n$: Sobolev embedding
requires a full $W^{1,p}$ bound, whereas the energy provides only a degenerate
weighted spatial derivative integral.  Pointwise bounds can follow only after a
separate higher derivative induction supplies the next unweighted spatial
level.

Step 38 shows that the apparent $m=2$ term
$\int\chi|\nabla^2\chi||\nabla^2U|^p$ should first be restored to its signed
contraction and integrated off the Hessian; it then costs diffusion plus
$\|d\chi\|_\infty^2\|\nabla^2U\|_p^p$, without requiring an evolving Hessian
coefficient.  The remaining higher induction, especially top cutoff jets
coupled to differentiated lower-order curvature factors, is not proved in this
file.  Consequently no smooth terminal extension conclusion follows from this
base estimate alone.

## 7. What this proves

**Finite-$L^p$ base-pair lemma.** Let
$\partial_tg=-2a(\operatorname{Ric}+g)$ on closed $M^n$, $a=\chi^2$, smooth on
$[0,T)$. If $\sup_{M\times[0,T)}|U|<\infty$ with
$U=a(\operatorname{Rm}+G)$, and if the unweighted finite-$L^p$ bound for $T$
used in §5 is independently available, then for every finite $p$,
$$
\sup_{t\in[0,T)}\bigl(\|\nabla U(t)\|_{L^p}+\|\nabla^2\chi(t)\|_{L^p}\bigr)<\infty.
$$
This is a base estimate, not an extension theorem.  A complete higher
shifted-curvature/cutoff-jet induction and terminal restart remain separate
work.

**What it does NOT use:**
- $\|T\|_\infty$ (only finite $L^p$ norms, which are available from Step 27 §5);
- $\|a\nabla\operatorname{Rm}\|_\infty$ (never appears as a coefficient);
- Unweighted $\|T\|_\infty$ division near $a=0$ (the shift avoids this by working
  with $U$ rather than $T$);
- Sequence-uniform constants (all bounds depend on $(g_0,\chi,T)$).

**What it DOES use as controlled coefficients in $R_1$--$R_7$:**
- $|U|\le K$ (the hypothesis);
- $|d\chi|\le Cr^{-1}$ (fixed cutoff geometry);
- $\|T\|_{L^p}<\infty$ (from Step 27 eq. 5.4);
- Uniform metric equivalence and Sobolev constants (from $|U|\le K$);
- The diffusion weight $a=\chi^2$ matching the $\chi$ in the dangerous $R_1$ term.

## 8. Remark on the $m=2$ term identified by the Preceptor

The Step 32 absolute-value estimate treated
$\int\chi|\nabla^2\chi||\nabla^2U|^p$ through
$\|\nabla^2\chi\|_4$.  Step 38 improves this: for the actual signed contraction
$\int\chi\nabla_i\nabla_j\chi\,B^{ij}(\nabla^2U)$, a second integration by
parts yields diffusion plus
$C\|d\chi\|_\infty^2\|\nabla^2U\|_p^p$.  Thus an evolving Hessian norm is not
intrinsic to this term.  This does not by itself settle other higher-order
couplings involving the highest cutoff jet and differentiated lower-order
curvature factors.
