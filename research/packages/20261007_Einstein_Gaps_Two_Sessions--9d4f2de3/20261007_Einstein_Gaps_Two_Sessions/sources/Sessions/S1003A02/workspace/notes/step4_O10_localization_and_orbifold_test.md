# Step 4 — Where density can matter: an elementary density-free endpoint, the 3/4 window, Kähler closure of O10, and the orbifold-limit test

Conventions are those of `Skills/geometric-analysis/references/conventions-and-literature.md`
(operator Hilbert–Schmidt Weyl norms, $S=\int s^2$, $P=\int|\mathrm{Ric}^\circ|^2$,
$W=\int|W^+|^2$, $T_+=2\chi+3\tau$, $p=(a_g^+)^2$). The endpoint quantity is
the one of `thm:finite-density-endpoint`
(`Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex`, l.13–43):
$$
\kappa_\beta(g)=\fint|\mathrm{Ric}+g|^2+\frac{D_\beta}{V},\qquad
D_\beta=(1+\beta^{-1})S+6(\beta+1)W-72\pi^2p ,
$$
for **every** metric $g$ of the conformal class (it is not scale invariant; the factor $g$ fixes the scale).
Symbolic checks: `workspace/scripts/o10_localization.py` → `workspace/data/o10_localization.json`.

## 1. Exact rewriting

Since $|\mathrm{Ric}+g|^2=|\mathrm{Ric}^\circ|^2+(s+4)^2/4$ and
$4\pi^2T_+=S/24+2W-P/2$, i.e. $P=S/12+4W-8\pi^2T_+$,
$$
V\kappa_\beta=\Bigl(\tfrac{13}{12}+\tfrac1\beta\Bigr)S+(6\beta+10)W+\int\frac{(s+4)^2}{4}-8\pi^2T_+-72\pi^2p. \tag{1.1}
$$
LeBrun's estimate $\int(s-\sqrt6|W^+|)^2\ge72\pi^2p$ (valid for every metric when the
actual monopole exists) and the pointwise inequality $(x+y)^2\le(1+\gamma^{-1})x^2+(1+\gamma)y^2$ give,
for every $\gamma>0$,
$$
72\pi^2p\le(1+\gamma^{-1})S+6(1+\gamma)W. \tag{1.2}
$$
(With $\gamma=\beta$ this is $D_\beta\ge0$.)

## 2. Theorem L (density-free endpoint below the 3/4 ratio)

**Hypotheses.** Actual conformal monopole supply as in `thm:finite-density-endpoint`,
$p\ge A>0$, $a^2\ge T_+$, and $T_+\le\theta A$ for a number $\theta<3/4$.
**No Euler-density bound.**

**Conclusion.** There is $c(\theta)>0$, independent of the manifold, structure, $A$, metric and $\beta$, with
$$
\kappa_\beta(g)\ge c(\theta)\frac{(\beta-2)^2}{\beta^2}\qquad(\beta\ge2).
$$

**Proof.** If $T_+<0$ put $\theta=0$ below (drop $-8\pi^2T_+\ge0$). Otherwise
$T_+\le\theta A\le\theta p$, so $-8\pi^2T_+-72\pi^2p\ge-72\pi^2\lambda p$ with $\lambda=1+\theta/9$.
Insert (1.2) with $\gamma=\gamma_{\max}=(9\beta-\theta+6)/(\theta+9)$, the value that cancels the $W$
coefficient $(6\beta+10)-6\lambda(1+\gamma)$. Then
$$
V\kappa_\beta\ge\int\Bigl(a\,s^2+\frac{(s+4)^2}{4}\Bigr),\qquad
a(\theta,\beta)=\frac{(\tfrac34-\theta)\beta^2+(\tfrac12-\tfrac{11}{4}\theta)\beta+6-\theta}{\beta(9\beta-\theta+6)} .
$$
For $a>0$ the pointwise minimum of $as^2+(s+4)^2/4$ is $16a/(4a+1)$, so
$\kappa_\beta\ge16a/(4a+1)$. The numerator $N(\beta)$ of $a$ is quadratic in $\beta$ with leading
coefficient $3/4-\theta>0$ and discriminant
$$
\mathrm{disc}(\theta)=\tfrac{57}{16}\theta^2+\tfrac{97}{4}\theta-\tfrac{71}{4}
=\tfrac{57}{16}\bigl(\theta-\tfrac23\bigr)\bigl(\theta+\tfrac{142}{19}\bigr).
$$
* $\theta<2/3$: $N>0$ for all $\beta$, and $a(\theta,\beta)\to a_\infty=1/12-\theta/9$; hence
  $\inf_{\beta\ge2}a>0$ and the bound holds for every $\beta\ge2$ from (1.1)–(1.2) alone.
* $2/3\le\theta<3/4$: $N<0$ exactly on an interval $(\beta_-(\theta),\beta_+(\theta))$ containing $\beta=8$
  ($\theta=2/3$ gives the double root $\beta=8$); $\beta_+(\theta)\to\infty$ as $\theta\uparrow3/4$
  (e.g. $\theta=0.74$: roots $\approx3.5,150$). For $\beta\ge2\beta_+(\theta)$ the elementary bound applies with
  $a\ge a_0(\theta)>0$. For $2\le\beta\le2\beta_+(\theta)$ use the density-free single-solution parameter estimate
  (results-and-questions §2): since $a^2\ge T_+\ge0$, $b=(-a^2)_+/V=0$ and
  $\kappa_\beta\ge(P+D_\beta/\beta)/V\ge c_{\rm par}(\beta-2)^2/\beta^4\ge c_{\rm par}(2\beta_+)^{-2}(\beta-2)^2/\beta^2$.
  When $T_+<0$ the case $\theta=0$ of the first bullet applies for every $\beta$ ($a(0,\beta)=\frac{\beta^2/4+\beta/6+2}{\beta(3\beta+2)}\ge1/12$). $\square$

*Scope check still owed.* The elementary branch holds for every metric of the class. The bounded-$\beta$ branch
quotes the single-solution parameter estimate, which results-and-questions §2 states on the $s=-4$ Yamabe
representative; for arbitrary metrics of the class one must use the same conformal transfer the corpus uses in
`thm:finite-density-endpoint` (read its proof for the transfer before citing Theorem L for non-Yamabe metrics).
For $\theta<2/3$ no such issue arises.

Values of the $\beta\to\infty$ constant $16a_\infty/(4a_\infty+1)$: $\theta=0$: $1$; $\theta=1/2$: $0.4$;
$\theta=2/3$: $1/7$; $\theta=0.74$: $0.0177$ (table in the JSON).

**What the proof shows structurally.** The *same quadratic* produces two classical thresholds:
uniformity in $\beta$ fails first at $\theta=2/3$ with the double root at $\beta=8$ — exactly LeBrun's
Einstein-obstruction ratio and the corpus' Chern–Weil-aligned parameter
($D_8=108\pi^2(T_+-2p/3)+27P/2$, in which $S$ and $W$ cancel). The large-$\beta$ endpoint fails only at
$\theta=3/4$. Thus Chern–Weil + LeBrun see everything except the window $T_+/A\ge3/4$ at large $\beta$.

## 3. The $\beta=\infty$ saturation configuration

Suppose $\kappa_{\beta_j}(g_j)\to0$ with $\beta_j\to\infty$ (the only regime the finite-density
theorem needs density for). From (1.1)–(1.2): $P/V\to0$, $\fint(s+4)^2\to0$, $\beta_jW/V\to0$, and
$S-72\pi^2p=o(V)$. Hence, asymptotically,
$$
p/V\to\frac{2}{9\pi^2},\qquad T_+/V\to\frac1{6\pi^2},\qquad \frac{T_+}{p}\to\frac34 ,
$$
the numerology of a negative Einstein metric with $W^+=0$ (e.g. real hyperbolic, or a complex-hyperbolic
quotient with reversed orientation) carrying a monopole that **saturates LeBrun's estimate at $W^+=0$**,
$S=72\pi^2p$. Such saturation is impossible on a smooth closed manifold (equality in LeBrun's improved
estimate forces Kähler–Einstein, whose $|W^+|=|s|/(2\sqrt6)\ne0$). So:

> **O10 in its exact form** = uniform-in-density quantitative strictness of LeBrun's $W^+$-improved
> estimate on almost-$W^+$-flat, almost-negative-Einstein geometries, in the window $T_+\ge\frac34A$.

The Euler number is invisible in all of these limits: $W^-$ enters none of $P,S,W,T_+$. Indeed
$8\pi^2\chi/V\to2/3+\fint|W^-|^2$, so $\chi/A\to\infty$ means $\fint|W^-|^2\to\infty$, i.e. $W^-$-bubbles.
For symplectic minimal $M$ with $a=c_1(K)$ one has $a^2=T_+$, so saturation needs
$p=(a^+)^2\to\frac43a^2$, i.e. $(a^-_g)^2\to-\frac13a^2$: the harmonic ASD part of the canonical class must be
macroscopic — the opposite of Kähler geometry, where $a^-=0$.

## 4. Kähler surfaces: O10 holds (Corollary K)

Let $X$ be a minimal Kähler surface of general type with $p_g\ge1$ ($b_+\ge3$), $A=c_1^2(X)$, and
$M=X\#k\overline{\mathbb{CP}}^2$ for any $k\ge0$, with LeBrun's blow-up supply (for each conformal class a
basic class $\pm K_X\pm E_1\pm\cdots$ with $p\ge A$; $a^2=T_+=A-k$). Then
$\kappa_\beta\ge c_K(\beta-2)^2/\beta^2$ for all $\beta\ge2$, all metrics, all $k$, with a universal $c_K>0$.

*Proof.* If $k\ge0.3A$ then $T_+\le0.7A$: Theorem L with $\theta=0.7$. If $k<0.3A$, Noether's inequality
$c_2\le5c_1^2+36-12q$ for minimal surfaces of general type gives $\chi(M)/A\le5.3+36/A\le41.3$, and
`thm:finite-density-endpoint` applies with $B=41.3$. $\square$

So no counterexample to O10 can be Kähler (or a blow-up of Kähler); the window $T_+\ge\frac34A$ together
with $\chi/A\to\infty$ forces non-Kähler manifolds far below the Noether line, $b_-\approx5b_+$ — e.g.
minimal symplectic manifolds with $0<c_1^2\ll\chi$. **The window is nonempty:** Braungardt–Kotschick
(`Knowledge/objects/papers/Einstein-metrics-and-the-number-of-smooth-structures-on-a-four-manifold--937ef5235565--e616882f6ef1/object.md`,
Theorem 4) realise every first-quadrant lattice point $(\chi_h,c_1^2)$ with $c_1^2\le(9-\epsilon)\chi_h-c(\epsilon)$ by
infinitely many simply connected minimal symplectic manifolds. Fix $c_1^2=A\ge1$ and let $\chi_h\to\infty$: $b_+=2\chi_h-1\ge3$,
Taubes gives the canonical-class monopole for every metric, $p\ge a^2=c_1^2=A$, $a^2=T_+$, and
$\chi/A=(12\chi_h-A)/A\to\infty$. For those, $T_+=A$, $\theta=1$, squarely in the window. **These are the
manifolds on which O10 is genuinely open.**

**Quantitative Hitchin–Thorpe (no field input).** For every metric, $P\ge S/12-8\pi^2T_+$; hence if
$T_+\le0$ then $\mathcal J=4P/(P+S/4)\ge1$, and $\mathcal E\ge\mathcal J\ge1$ (the $R=0$ case has $\mathcal E=4$).
Same with $T_-$. So $\alpha(M)\ge1$ whenever $2\chi\le3|\tau|$; product metrics on $S^2\times\Sigma_g$
($g\ge2$) give $\mathcal E=4-2(K_1+K_2)^2/(K_1^2+K_2^2)\to2$, so $1\le\alpha(S^2\times\Sigma_g)\le2$. The sharp
value in this region is a separate (fieldless) question.

## 5. Orbifold-limit test (strategist's test), computed

Let $X_0$ be a Kähler–Einstein orbifold of general type ($s=-4$) whose singular points are of type
$A_{k_i-1}$ ($\mathbb C^2/\mathbb Z_{k_i}$, $SU(2)$ action), and $Y\to X_0$ its minimal (crepant) resolution: $Y$ is a
smooth minimal surface of general type with $(-2)$-curve chains, $K_Y=\pi^*K_{X_0}$ nef, not ample, so $Y$ has
no Kähler–Einstein metric.

*Glued metrics.* Insert Kronheimer's hyperkähler ALE $A_{k-1}$ metrics scaled by $\varepsilon^2$, cut off at
$r\sim\varepsilon^{1/2}$ (orbifold metric $=$ flat $+O(r^2)$, ALE metric $=$ flat $+O(\varepsilon^4r^{-4})$). The error is
supported on annuli of volume $O(\varepsilon^2)$ with bounded curvature error, and the cores have volume
$O(\varepsilon^4)$; hence $\fint|\mathrm{Ric}+g|^2=O(\varepsilon^2)$ and $\alpha(Y)=0$.

*Field terms.* The ALE cores are Ricci-flat Kähler for the same complex structure, so $s=0$ and $W^+=0$
there (complex orientation): they contribute nothing to $S$ or $W$. Their $L^2$ harmonic forms are ASD and
$K_Y\cdot E=0$ for every exceptional curve, so $p(g_\varepsilon)\to K_Y^2$. With the KE values
$|W^+|^2=2/3$, $p=V/2\pi^2$,
$$
\kappa_\beta(g_\varepsilon)\longrightarrow\frac{4(\beta-2)^2}{\beta}\qquad(\text{exactly the KE orbifold value}).
$$
So on this sequence the whole endpoint gap is carried by $D_\beta$ (bulk misalignment of $W^+$ from $|s|/(\beta\sqrt6)$),
the Ricci part tends to zero, and $\kappa_2\to0$. $Y$ lies in the bounded-density range (Noether) and in the
window ($T_+/A=1$), consistently with the theorem.

*Meaning for the human question.* $Y$ gives $\alpha(Y)=0$ (arbitrarily good integral approximation) on a
manifold with no Kähler–Einstein metric. **Correction to the expected obstruction:** the leading
Biquard/Ozuch obstruction to Einstein desingularization is $\det\mathbf R^+(x)=0$ with
$\mathbf R^+=W^++\tfrac s{12}$ on $\Lambda^+$ (Ozuch I, `Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md`, l.89–130),
not $\det W^+=0$. At a KE point $W^+=\mathrm{diag}(s/6,-s/12,-s/12)$, so $\mathbf R^+=\mathrm{diag}(s/4,0,0)$ has rank one and
$\det\mathbf R^+=0$: **the leading obstruction is satisfied** and does not exclude Einstein metrics near the limit.
The Kähler route is obstructed cohomologically ($K_Y\cdot E=0$, $K_Y$ not ample). The LeBrun–Ozuch rigidity
(admissible Einstein sequences converging to conformally Kähler orbifolds are eventually Kähler–Einstein;
`Knowledge/objects/papers/Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8--5b19d560b771/object.md`)
is proved for $\lambda>0$ through Wu's criterion $\det W^+>0$; for negative KE, $\det W^+=s^3/864<0$, so that
mechanism is unavailable. Whether non-Kähler Einstein metrics exist on $Y$ near the orbifold limit is therefore
decided only by higher-order (second-order / tree) obstructions — undecided in the material read so far.
This makes $Y$ the cleanest test of "gap zero vs. existence": a concrete degenerating family with
$\mathcal E\to0$ where both outcomes (a non-KE Einstein metric, or non-attainment) are live. It also shows **$\kappa_\beta$ for $\beta\ne2$ is not an Einstein gap**:
it is a field-alignment gap that stays $\ge4(\beta-2)^2/\beta$ on metrics with $\mathcal E\to0$. The passage from
$\kappa$ to $\alpha$ is the N1 combination with the topological summand $(T_+/A-2/3)_+$, which is $1/3$ on $Y$.

## 6. Consequence for the O10 programme (re-aiming Steps 2–3)

* **Local payments vanish.** $W^+$-flat hyperkähler cores (ALE, or the multi–Taub–NUT tangent of Step 3)
  contribute zero to every term of $\kappa_\beta$ ($P$, $S$-defect $O(\text{vol})$, $W$, and $p$ when $a\cdot E=0$).
  The "positive transition payment per Euler unit" alternative of Step 3 is false locally — the $Y$ sequence
  realises zero local cost per Euler unit. A density-free theorem must be global, as the strategist anticipated.
* **Orbifold bulks are excluded.** If a would-be counterexample had $W^+$-flat bubbles and a bulk converging to
  an orbifold of bounded Euler density, an orbifold version of the finite-density theorem (with the saturation
  of §3 impossible on orbifolds as well) would contradict it. So any O10 counterexample needs essential
  non-orbifold degeneration at the bulk scale: collapse, accumulation of orbifold points, or a shift of the
  harmonic period point $a^-_g$ carried by the degeneration (§3 requires $(a^-)^2\approx-T_+/3$).
* **The live mechanism.** ALF multi–Taub–NUT carries $L^2$ harmonic ASD forms not dual to compact spheres (the
  Taub–NUT form); unlike ALE $(-2)$-classes, they are not killed by $a\cdot E=0$. Whether degenerating ALF cores can
  move the period point so as to give $p\approx\frac43a^2$ while the bulk is $W^+$-flat is the precise question
  that replaces the order-$r^2$ "transition cost" programme. A counterexample would have to realise it on a
  non-Kähler manifold with $T_+\ge\frac34A$, $\chi/A\to\infty$; a theorem would prove quantitative strictness of
  LeBrun's improved estimate uniformly in $\fint|W^-|^2$.

## 7. O11 (kept in view)

Unchanged this Step: the decisive objects are a fixed-scale non-symmetric cell with $4\Delta W_++\Delta S/12<0$
or a lower-bound theorem $P(U)\ge8\pi^2$ for every $\mathbb{CH}^2$-asymptotic cell. Note the analogy now visible:
in O11 the Burns cell has $P(U)=8\pi^2=-8\pi^2T_+(\text{cell})$ exactly by (1.1)-type bookkeeping
($s=0$, $W^+=0$), i.e. the scalar-flat Kähler cell is the $T_+$-saturating object, just as the $W^+$-flat
bubble is the $\chi$-carrying, $T_+$-neutral object in O10.
