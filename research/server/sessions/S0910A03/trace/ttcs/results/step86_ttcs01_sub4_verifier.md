# TTCS Independent Branch Record

```json
{
  "step_id": 86,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/scripts/step85_bochner_comparison.py",
    "Sessions/S0910A03/trace/ttcs/results/step85_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Independently audit and derive the forced superlevel Caccioppoli inequality for e=|dU|^2 on the OT weighted base. Start with 1/2 Le=|DdU|^2+div_sigma V-|F|^2+Q-3e+(1/2)|dU(grad sigma)|^2+E_B:A, V(X)=<dU(X),F>, Q>=e^2/2. Test with eta^2 u, u=(e-k)_+, k>=6, and retain -int eta^2<V,grad u> as well as the cutoff term. Use Kato |grad e|<=2 sqrt(e)|DdU| and pointwise |F|,|E_B| controlled by the full operator Ricci defect to obtain the sharpest valid inequality without assuming u small. Then assess whether CD(-(3+delta),4), normalized doubling/Poincare/Sobolev on buffered balls, and this inequality genuinely imply any universal interior upper bound below 12 when exit e is small. Check locality, boundary, volume normalization, and whether Moser needs an independent local L2/L1 seed. If a proposed universal ceiling is false, construct the simplest scalar weak/PDE model exhibiting the failure mechanism while respecting the inequality's sign structure.

## Output

# Verification Memo: Forced Superlevel Caccioppoli Inequality for $e=|dU|^2$

## 0. What was checked and the one-line result

I re-derived the weak superlevel inequality from the forced weighted Bochner identity, kept every term the task asked to retain (the $-\int\eta^2\langle V,\nabla u\rangle$ piece and both cutoff cross terms), and tracked the sign of each contribution. The reaction structure is genuinely absorbing and shifts the natural threshold from $6$ to $6+O(\delta)$. **But the inequality as derived does not, on its own inputs, force an interior ceiling below $12$ from small exit data.** The reason is precise and reduces to a single missing analytic ingredient: the forcing term $F=\tau_\sigma$ is only controlled in $L^\infty$ ($|F|\le\delta$), whereas $\operatorname{div}_\sigma V$ carries $DF$, which is a distributional (i.e. $H^{-1}$-type) source. A superlinear absorbing reaction dominates a source that is bounded pointwise, but it does **not** dominate a divergence source built from a merely $L^\infty$ vector field. I make this quantitative below and exhibit the simplest scalar weak model that realizes it while respecting the exact sign structure.

---

## 1. The weak identity, term by term

Weighted integration by parts: since $Le\cdot\rho=\operatorname{div}(\rho\nabla e)$,
$$
\int_\Omega \phi\,Le\,d\mu=-\int_\Omega\langle\nabla\phi,\nabla e\rangle\,d\mu+\int_{\{r=R\}}\phi\,\partial_\nu e\,d\mu_\partial,\qquad d\mu=\rho\,dA .
$$
Take $\phi=\eta^2u$, $u=(e-k)_+$, $k\ge 6$. On $\{e>k\}$: $u=e-k$, $\nabla u=\nabla e$, $\nabla(\eta^2u)=\eta^2\nabla u+2\eta u\nabla\eta$. The reflected center is smooth-doubled, so it is interior and contributes no edge terms; the only edge locus is $r=R$.

Starting from
$$
\tfrac12Le=|DdU|^2+\operatorname{div}_\sigma V-|F|^2+Q-3e+\tfrac12|dU(\nabla\sigma)|^2+E_B{:}A,\quad V(X)=\langle dU(X),F\rangle,
$$
multiply by $\eta^2u$, integrate, use $\int\eta^2u\operatorname{div}_\sigma V\,d\mu=-\int\langle\nabla(\eta^2u),V\rangle d\mu+\int_{r=R}\eta^2u\,V(\nu)\,d\mu_\partial$, and collect. Every nonnegative quadratic goes to the left:

$$
\boxed{\;
\tfrac12\!\int\!\eta^2|\nabla u|^2
+\!\int\!\eta^2u|DdU|^2
+\!\int\!\eta^2u\,Q
+\tfrac12\!\int\!\eta^2u|dU(\nabla\sigma)|^2
\;}
$$
$$
=-\!\int\!\eta u\langle\nabla\eta,\nabla u\rangle
+\underbrace{\int\!\eta^2\langle\nabla u,V\rangle}_{T_2}
+\underbrace{2\!\int\!\eta u\langle\nabla\eta,V\rangle}_{T_3}
+\underbrace{\int\!\eta^2u|F|^2}_{T_4}
+\underbrace{3\!\int\!\eta^2u\,e}_{\text{reaction}}
-\!\int\!\eta^2u\,E_B{:}A
+B_\partial .
$$

All bulk integrals are $d\mu$; $B_\partial=\tfrac12\int_{r=R}\eta^2u\,\partial_\nu e\,d\mu_\partial-\int_{r=R}\eta^2u\,V(\nu)\,d\mu_\partial$. This is exact, no smallness assumed on $u$.

**Sign of the reaction is the whole game.** The $-3e$ of Bochner appears here as $+3\int\eta^2u\,e$ on the right (a source), while $Q\ge\tfrac12e^2$ sits on the left. Their difference is the coercive object:
$$
\int\eta^2u\,Q-3\int\eta^2u\,e\;\ge\;\tfrac12\int\eta^2u\,e(e-6)\;\ge 0\quad(\text{on }\{e\ge k\ge6}).
$$

---

## 2. Pointwise control of the small tensors and Young splits

Pointwise, with $|dU|=\sqrt e$:
$$
|V|\le\sqrt e\,|F|\le\delta\sqrt e,\qquad |E_B{:}A|\le\|E_B\|_{\mathrm{op}}\operatorname{tr}A\le\delta\,e,\qquad |\nabla u|\le 2\sqrt e\,|DdU|\ (\text{Kato}).
$$

- $-\!\int\eta u\langle\nabla\eta,\nabla u\rangle\le\tfrac18\!\int\eta^2|\nabla u|^2+2\!\int u^2|\nabla\eta|^2$.
- $T_2\le\tfrac18\!\int\eta^2|\nabla u|^2+2\!\int\eta^2|V|^2\le\tfrac18\!\int\eta^2|\nabla u|^2+2\delta^2\!\int\eta^2e$.
- $T_3\le 2\delta\!\int\eta u\sqrt e\,|\nabla\eta|\le\beta\!\int\eta^2u\,e+\tfrac{\delta^2}{\beta}\!\int u|\nabla\eta|^2$.
- $T_4\le\delta^2\!\int\eta^2u$.
- $-\!\int\eta^2u\,E_B{:}A\le\delta\!\int\eta^2u\,e$.

The two $ue$-type source contributions ($E_B{:}A$ and the $\beta$-piece of $T_3$) add to the reaction as an effective coefficient: comparing $\tfrac12ue^2$ against $(3+\delta+\beta)ue$ gives $\tfrac12ue\big(e-(6+2\delta+2\beta)\big)$. Choosing $k\ge 6+2\delta$ keeps this $\ge0$. Kato only makes the Hessian term and the Dirichlet term comparable ($\int\eta^2u|DdU|^2\ge\tfrac14\int\eta^2\tfrac{u}{e}|\nabla u|^2$, weaker than the direct $\tfrac12\int\eta^2|\nabla u|^2$ already present), so it does not add independent coercivity — it guarantees no double counting.

**Sharpest valid form.** Absorbing $\tfrac14$ of the Dirichlet energy and writing $e=u+k$ on $\{e>k\}$:
$$
\boxed{\;
\tfrac14\!\int\eta^2|\nabla u|^2
+\!\int\eta^2u|DdU|^2
+\tfrac12\!\int\eta^2u\,e\big(e-(6+2\delta)\big)
\le
C\!\int(u^2+\delta^2u)|\nabla\eta|^2
+C\delta^2\!\int_{\{e>k\}}\!\eta^2u
+C\delta^2 k\!\int_{\{e>k\}}\!\eta^2
+B_\partial .\;}
$$
Note $e(e-6-2\delta)\ge u^2$ on $\{e\ge k\}$, so the third left term is a genuine **cubic** sink $\ge\tfrac12\int\eta^2u^3$. The reaction is therefore not merely quadratic — it is Keller–Osserman-strong.

---

## 3. The one term that does not belong to the $u$-weighted family

The three source terms on the right are:
1. $C\delta^2\int_{\{e>k\}}\eta^2u$ — controllable, absorbed by the cubic sink and the reaction ($\delta^2 u\le \tfrac{1}{4}u^3+C\delta^3$).
2. $C\delta^2 k\int_{\{e>k\}}\eta^2$ — **the measure term.** It is proportional to $\mu(\{e>k\}\cap\operatorname{supp}\eta)$, weighted by $k\approx6$, and is **not** damped by $u$: as $e\downarrow k$, $u\to0$ and the sink $u^3\to0$, but this term stays $O(\delta^2)$ per unit measure.
3. $B_\partial$ — supported only on the exit locus $r=R$; it drops for interior cutoffs.

Term 2 is where the argument stops being self-closing. It is the source that survives arbitrarily close to the level set.

---

## 4. What Moser gives, and the seed it needs

On a buffered interior ball where $\rho=e^\sigma$ is bounded above and below (orbit area not collapsing), the drift base has $\operatorname{Ric}_\sigma=\operatorname{Ric}_B-\nabla^2\sigma\ge-(3+\delta)$, effective dimension $N=4$, so $\mathrm{CD}(-(3+\delta),4)$ holds. This gives scale-normalized volume doubling and an $(2,2)$-Poincaré/Sobolev on balls of radius $\lesssim(3+\delta)^{-1/2}$ with constants depending only on $N$ and $\delta$. Feeding the Caccioppoli into Sobolev and iterating yields the standard local $L^2\!\to\!L^\infty$ gain:
$$
\sup_{B_{r/2}}u\ \lesssim\ \Big(\fint_{B_r}u^2\Big)^{1/2}\;+\;\delta\sqrt{k}\,.
$$
Read off the two ingredients:

- The additive $\delta\sqrt{k}\approx2.4\,\delta$ is harmless: it contributes only $O(\delta)$ to any ceiling.
- The multiplicative term is a **seed**: $\big(\fint_{B_r}(e-k)_+^2\big)^{1/2}$. Moser is a conditional local regularity statement — it converts a local $L^2$ smallness of $(e-k)_+$ into a local $L^\infty$ smallness. **It does not manufacture an absolute numerical ceiling.** Nothing in the supplied inputs bounds this $L^2$ seed a priori.

Locality and the edge are clean: interior cutoffs kill $B_\partial$, and the reaction and divergence terms are local after the integration by parts. Volume normalization holds only on the non-collapsed collar; near collapsing $T^2$ orbits (the $N\#N$ neck axis) $\rho\to0$ and the normalized Poincaré/Sobolev constants degrade, so even the local Moser step is not uniform there.

---

## 5. Does a universal ceiling below $12$ follow? — The decisive point

There are two very different regimes, separated entirely by **which norm controls the forcing**, and this is where the honest answer to the task lives.

**(a) If the forcing enters only through $\|F\|_{L^\infty},\|E_B\|_{L^\infty}\le\delta$** (the stated input): the source $\operatorname{div}_\sigma V$ is a derivative of an $L^\infty$ field, hence lives in $H^{-1}$/$W^{-1,\infty}$, not in any $L^q$. A superlinear (even cubic) absorbing reaction dominates a **pointwise-bounded** potential but does **not** dominate an $H^{-1}$ source. Concretely, the integrated inequality above is fully consistent with thin, tall interior spikes of $e$ (see §6), whose $L^2$ seed is small yet whose $\sup$ is large; Moser then only reports the small seed, and there is no contradiction. **No universal interior ceiling below $12$ follows from $C^0$ control alone.** This is precisely why the center average $\langle e(0,\cdot)\rangle_\mu\ge12-8\delta$ cannot yet be contradicted for the forced connector — the interior is not pinned to $6+O(\delta)$.

**(b) If additionally $DF\in L^q$, $q>N/2=2$, with small norm** — equivalently the Ricci defect is controlled in $C^1$ (or $W^{1,q}$, $q>2$), not merely $C^0$ — then $\operatorname{div}_\sigma V$ becomes a genuine $L^q$ potential of size $\lesssim\delta'$. The cubic sink is Keller–Osserman-strong ($p=3>1$, subcritical against an $L^{q>2}$ source in $N=4$), giving an interior bound
$$
e(x)\ \le\ 6+C\big(\delta+\delta'^{1/2}\big)+\frac{C}{\operatorname{dist}(x,\{r=R\})^{2}}
$$
**independent of the connector length $R$ and of exit data.** In the interior of a long collar this drives $e\le6+O(\delta+\sqrt{\delta'})$, which contradicts $\langle e(0,\cdot)\rangle_\mu\ge12-8\delta$ for small defect. This is the version that closes the nonexistence direction.

So the sharp statement is: **the closing ingredient is $L^q$ ($q>2$) / $C^1$ smallness of $D\tau_\sigma$ (equivalently of the derivative of the operator Ricci defect), not merely $C^0$ smallness of the defect itself.** The material establishes the latter, not the former.

---

## 6. Simplest scalar weak model realizing the mechanism

Work on $(-R,R)$ with unit weight (drift and $\rho$ only change constants). Let $w\ge0$ solve, weakly against nonnegative test functions,
$$
\tfrac12\,w''\ \ge\ \tfrac12\,w(w-6)\;-\;b'(x),\qquad |b(x)|\le\delta\sqrt{w},
$$
with small exit data $w(\pm R)=\varepsilon$. This has exactly the derived sign structure: absorbing reaction $\tfrac12 w(w-6)$ on the left, divergence source $-b'$ (the scalar avatar of $\operatorname{div}_\sigma V$ with $V\sim\delta\sqrt e$) on the right, and $b$ obeying the same $L^\infty$ bound that $V$ obeys.

**Contrast of the two source regimes:**

- *Bounded source.* If instead the source were a genuine function $S(x)\le C\delta$, the peak obeys $w''\le0\Rightarrow\tfrac12 w(w-6)\le C\delta\Rightarrow w\le 3+\sqrt{9+2C\delta}=6+O(\delta)$. Ceiling holds, independent of exit data (Keller–Osserman). Regime (b).

- *Divergence source, $L^\infty$-only $b$.* Choose $b$ that drops rapidly across $x=0$: $b$ swings from $+\delta\sqrt{w}$ to $-\delta\sqrt{w}$ over a length $\ell$, so $b'\approx-2\delta\sqrt{w}/\ell$. A localized $-b'\ge 36$ near the peak requires only $\ell\lesssim \delta\sqrt{12}/18\sim\delta$. At such a spike the peak condition becomes $\tfrac12 w(w-6)\le -b'$, permitting $w(0)=12$ (indeed $w\le 3+\sqrt{9+2|b'|}$, unbounded as $|b'|$ grows). The excursion above $6$ occupies a set of length $O(\delta)$, so the $L^2$ seed $\int(w-6)_+^2\sim\delta$ is small — Moser only certifies this smallness and never sees the spike; the integrated inequality is satisfied because the reaction cost $\int (w-6)_+^3\sim\delta$ is likewise small. Regime (a).

The scalar model isolates the mechanism cleanly: **a pointwise bound on $b$ ($\Leftrightarrow$ on $F$) does not bound $b'$ ($\Leftrightarrow DF$); the reaction cannot beat an oscillatory divergence source; and Moser's $L^2$ seed cannot detect a thin tall spike.** It also shows the mechanism is defeated the moment $b\in W^{1,q}$, $q>2$ with small norm (then $b'$ is a bona fide small $L^q$ potential and the peak returns to $6+O(\delta)$).

---

## 7. What is settled and what must be supplied

Settled by the derivation:
- The forced superlevel inequality is correct with the sign structure boxed in §2; the effective threshold is $6+2\delta$; the reaction is cubic-strong.
- On non-collapsed buffered collar balls, $\mathrm{CD}(-(3+\delta),4)$ furnishes the normalized doubling/Poincaré/Sobolev needed for Moser, and interior cutoffs remove the exit-locus flux.

Not delivered by the present inputs:
- A universal interior ceiling below $12$. Moser gives a conditional $L^2\!\to\!L^\infty$ statement and requires an independent local $L^2$ seed on $(e-k)_+$; that seed is not established. Propagating a small-exit value inward along a length-$R$ chain accumulates the additive $O(\delta)$ per step unless the reaction is genuinely Keller–Osserman-active, which needs a pointwise (or $L^{q>2}$) source.
- The single ingredient that would close it: $\|D\tau_\sigma\|_{L^q}$, $q>2$ (equivalently $C^1$/$W^{1,q}$ smallness of the operator Ricci defect), replacing the $C^0$ bound $\|F\|_{L^\infty}\le\delta$. With that, the cubic reaction dominates the now-$L^q$ potential, the interior bound $e\le6+O(\delta+\|D\tau_\sigma\|^{1/2})$ holds $R$-independently, and it contradicts $\langle e(0,\cdot)\rangle_\mu\ge12-8\delta$.
- Uniformity fails to reach collapsing-orbit regions ($\rho\to0$), so any argument through this inequality covers the free-$T^2$ collar interior, not the $N\#N$ neck axis.

The precise open question is therefore narrower and sharper than "does Moser close": it is whether the geometry forces $D\tau_\sigma$ (second derivatives of the Ricci defect) to be small in $L^{q>2}$ whenever the defect itself is $C^0$-small on a near-Einstein connector. That is an elliptic-regularity / bootstrap statement about the defect tensor, and it is the object on which the forced nonexistence direction now rests.