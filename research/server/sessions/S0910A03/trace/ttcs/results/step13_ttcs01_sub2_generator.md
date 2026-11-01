# TTCS Independent Branch Record

```json
{
  "step_id": 13,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step12_reduced_equations_accessibility.md",
    "Sessions/S0910A01/workspace/notes/step13_normalized_accessibility_theorem.md"
  ]
}
```

## Task

For a four-dimensional negative Einstein metric Ric = -g with a local free circle action g = q + ell^2 theta^2, define H = Hess_q(ell)/ell. In the chiral variables a_+ = u - z/2 and a_- = u + z/2 where u = d log(ell) and z = *_q(ell F), we have W+ = -[sym nabla a_+ + a_+ otimes a_+]_0 and the electric Weyl E = (1/3)I - H + (|z|^2 I - z otimes z)/4, magnetic Weyl B = (1/2)(sym nabla z + u otimes z + z otimes u - <u,z>I). The trace constraint is tr(H) = 1 + |z|^2/2. The question: if the calibrated W+ spectrum is (-1/6, 1/12, 1/12), and the full curvature average is bounded (fint |Rm|^2 <= K_0), investigate whether H has nonnegative eigenvalues. In the static case (B=0, z=0), calibrated E has eigenvalues (-1/6, 1/12, 1/12), giving H = (1/2, 1/4, 1/4) > 0. For the general twisted case, express H = (1/3)I + Q - E where Q = (|z|^2 I - z otimes z)/4, and E = W+ - B. Determine: (A) Can large B (twist gradient) push an eigenvalue of H below zero while maintaining |W+|^2 = 1/24? (B) Does the L^2 smallness of |B| (from integral calibrated deficit) suffice to control H in L^p for p > 3/2? (C) Explore whether the chiral Riccati structure W+ = -[sym nabla a_+ + a_+ otimes a_+]_0 with |W+|^2 = 1/24 provides a direct estimate relating |B|^2 to |nabla z|^2 + |u|^2|z|^2 that would bound H from below. Seek a precise inequality or a counterexample (an explicit 1-jet model).

## Output

## Memo: positivity of the fiber Hessian $H$ under calibrated $W^+$

I take the reduction as stated: for $\mathrm{Ric}_g=-g$ on $M^4$ with a local free circle action, $H=\mathrm{Hess}_q(\ell)/\ell$, $u=d\log\ell$, $z=*_q(\ell F)$,
$$
E=\tfrac13 I-H+Q,\quad Q=\tfrac14(|z|^2 I-z\otimes z)\succeq0,\quad B=\tfrac12(\mathrm{sym}\,\nabla z+u\otimes z+z\otimes u-\langle u,z\rangle I),
$$
$W^+=E+B$, $W^-=E-B$, and the trace identity $\operatorname{tr}H=1+|z|^2/2$. Everything below is exact algebra on this data plus the divergence structure of Einstein 4‑manifolds.

### 1. The exact relation and a sharp lower bound for $\lambda_{\min}(H)$

Solve for $H$:
$$
\boxed{\,H=\tfrac13 I+Q+B-W^+\,},\qquad Q\succeq0.
$$
Because $Q$ is positive semidefinite it can only raise eigenvalues of $H$; the only tensor able to drive an eigenvalue of $H$ below zero is the magnetic block $B$. For any unit $e$,
$$
\langle He,e\rangle=\tfrac13+\langle Qe,e\rangle+\langle Be,e\rangle-\langle W^+e,e\rangle\ \ge\ \tfrac13+0+\lambda_{\min}(B)-\lambda_{\max}(W^+).
$$
The calibrated spectrum $(-\tfrac16,\tfrac1{12},\tfrac1{12})$ gives $\lambda_{\max}(W^+)=\tfrac1{12}$, and for a trace‑free symmetric $3\times3$ tensor $\lambda_{\min}(B)\ge-\sqrt{2/3}\,|B|$. Hence
$$
\boxed{\ \lambda_{\min}(H)\ \ge\ \tfrac14-\sqrt{\tfrac23}\,|B|\ }\qquad\Longrightarrow\qquad H\succeq0\ \text{ wherever }\ |B|\le \tfrac{\sqrt6}{8}\approx0.306\ \ (|B|^2\le \tfrac{3}{32}).
$$
This is sharp and independent of $z$: the worst case is $z=0$, $Q=0$, with $B$'s most‑downward eigendirection lying in the $+\tfrac1{12}$ plane of $W^+$. Note the calibrated $W^+=\tfrac1{12}(I-3\,n\otimes n)$ has a single distinguished eigenline $n$; the dangerous configuration puts the extreme direction of $B$ orthogonal to $n$, and nothing in the calibration forbids that alignment.

### 2. (A) An explicit 1‑jet with $\lambda_{\min}(H)<0$ and calibrated $W^+$

Take a point where $z(p)=0$. Then the first‑order reduced equations force the antisymmetric part of $\nabla z$ to vanish ($dz=-2u\wedge z=0$) and its trace to vanish ($\operatorname{div}z=\langle u,z\rangle=0$), so $\nabla z$ is an arbitrary symmetric trace‑free tensor and $B=\tfrac12\,\mathrm{sym}\,\nabla z$ is arbitrary symmetric trace‑free. Choose, in an orthonormal base frame with $W^+=\operatorname{diag}(-\tfrac16,\tfrac1{12},\tfrac1{12})$,
$$
B=\operatorname{diag}(c,-2c,c),\qquad \nabla z=2B,\qquad z(p)=0,\qquad u(p)=0,\qquad \mathrm{Hess}_q(\log\ell)=H.
$$
Then $Q=0$, $E=\tfrac13 I-H=\operatorname{diag}(-\tfrac16-c,\ \tfrac1{12}+2c,\ \tfrac1{12}-c)$ is trace‑free, and
$$
W^+=E+B=\operatorname{diag}(-\tfrac16,\tfrac1{12},\tfrac1{12})\quad(\text{calibrated, }|W^+|^2=\tfrac1{24}),
$$
while
$$
H=\tfrac13 I+B-W^+=\operatorname{diag}\!\big(\tfrac12+c,\ \tfrac14-2c,\ \tfrac14+c\big),\qquad \lambda_{\min}(H)=\tfrac14-2c.
$$
For $c>\tfrac18$ the fiber Hessian is indefinite; e.g. $c=\tfrac14$ gives $H=\operatorname{diag}(\tfrac34,-\tfrac14,\tfrac34)$. Every first‑order reduced equation holds at $p$. So the calibrated $W^+$ spectrum together with the pointwise reduced relations does **not** force $H\succeq0$: derivative twisting ($\nabla z$ large while $z,u$ small) realizes the decoupling flagged in Step 12. This is a genuine 1‑jet obstruction to any purely algebraic pointwise positivity statement.

The cost is visible immediately: $W^-=E-B=\operatorname{diag}(-\tfrac16-2c,\tfrac1{12}+4c,\tfrac1{12}-2c)$, so at $c=\tfrac14$, $|W^-|^2\approx1.79\gg|W^+|^2=\tfrac1{24}$. Pushing $H$ below zero deposits $O(|B|^2)$ into the anti‑self‑dual Weyl energy, hence into $|Rm|^2$. This is the lever for part (B).

Whether this 1‑jet integrates to an actual $\mathrm{Ric}=-g$ metric is a separate matter — see §5, where the second‑order Einstein content (Derdziński) makes the calibrated germ itself impossible, so no integrated calibrated model exists at all. The 1‑jet is exactly the right object to show the first‑order proxy is too strong, not a claimed metric.

### 3. (B) $L^2$ control of the part of $H$ below zero, and where $p>3/2$ sits

Write $B=\tfrac12(W^+-W^-)$, so $|B|^2\le\tfrac12(|W^+|^2+|W^-|^2)$. For $\mathrm{Ric}=-g$ (so $s=-4$, $\mathrm{Ric}_0=0$),
$$
|Rm|^2=|W^+|^2+|W^-|^2+\tfrac{8}{3}=\tfrac1{24}+|W^-|^2+\tfrac83\quad\text{on the calibrated set.}
$$
Thus $\fint|W^-|^2\le K_0-\tfrac83-\tfrac1{24}$ and
$$
\fint|B|^2\ \le\ \tfrac12\big(\tfrac1{24}+\fint|W^-|^2\big)\ \le\ \tfrac12\big(K_0-\tfrac83\big).
$$
Setting $(H)_-:=\max(0,-\lambda_{\min}(H))\le\sqrt{2/3}\,|B|$ from §1,
$$
\boxed{\ \fint (H)_-^2\ \le\ \tfrac23\fint|B|^2\ \le\ \tfrac13\big(K_0-\tfrac83\big).\ }
$$
So the part of $H$ below zero — equivalently the part of $\mathrm{Ric}_B=-I+H+\tfrac12 C^2_{\mathrm{sym}}$ below $-I$, since $C^2_{\mathrm{sym}}\succeq0$ gives $\lambda_{\min}(\mathrm{Ric}_B)\ge-1+\lambda_{\min}(H)$ — is controlled in $L^2$. Because $2>\tfrac32=\tfrac n2$ in the 3‑dimensional base, this places $(\mathrm{Ric}_B)_-$ in the subcritical range of integral‑Ricci geometry (Petersen–Wei; Dai–Wei–Zhang), which is exactly the input for volume comparison, Sobolev, and harmonic‑radius bounds. So the answer to (B) is affirmative in the $L^2$ sense.

Two structural points determine whether this is enough for the accessibility construction rather than merely encouraging:

- The estimate delivers a **bound**, not scale‑invariant **smallness**. Integral‑Ricci harmonic‑radius theorems need $r^2\big(\fint_{B_r}(\mathrm{Ric}_-)^p\big)^{1/p}$ below a dimensional constant at the working scale. A global average $\le\tfrac13(K_0-\tfrac83)$ does not preclude concentration of $|W^-|^2=4|B|^2+\dots$ into small balls on a positive‑measure set. The crude volume estimate $\mathrm{Vol}\{H\not\succeq0\}\le\tfrac{32}{3}\int|B|^2$ is only informative when the $W^-$ energy is itself small, which is not supplied.
- The measure is the weighted quotient measure $\ell\,dV_q$ (the $\mathrm{RCD}(-1,4)$ measure of Step 12), so the needed theorem is a **weighted** integral‑Ricci statement, not the classical smooth one. The passage from the 4D energy to the weighted 3D $L^2$ energy carries the fiber weight $v$ that the bootstrap does not yet control independently.

So (B) reduces the whole positivity question to a single sharp issue: **small‑scale non‑concentration of the $W^-$ energy on the calibrated set.** That is where the next structural input must come.

### 4. (C) Why no pointwise inequality bounds $|B|$ by $|W^+|$ — and the divergence structure that could replace it

The chiral identities give $B$ cleanly:
$$
2B=\big[\mathrm{sym}\,\nabla z+u\otimes z+z\otimes u\big]_0,\qquad |B|\ \lesssim\ |\nabla z|+|u|\,|z|,
$$
which is the requested relation $|B|^2\lesssim|\nabla z|^2+|u|^2|z|^2$. The obstruction to a lower bound on $H$ from $|W^+|^2=\tfrac1{24}$ is structural: $W^+$ is the trace‑free symmetric Riccati tensor of $a_+=u-z/2$, while $B$ lives in the Riccati tensor of $a_-=u+z/2$. The two chiral 1‑forms are coupled **only** through the Maurer–Cartan relations $da_\pm=\pm\,a_+\wedge a_-$, i.e. through the *antisymmetric* derivative, whereas the Weyl blocks are the *symmetrized* Riccati tensors. Symmetric part and $d$‑part are independent data, so the calibration of $a_+$ leaves the symmetrized Riccati of $a_-$ — hence $B$ — pointwise free. The 1‑jet of §2 is the explicit realization. No pointwise coercive inequality of the requested form can exist.

The genuinely stronger structure is second‑order and comes from the Einstein Bianchi identity, which is not yet used in the $H$‑positivity question:

**Divergence‑free chiral Weyl.** For any Einstein 4‑manifold $\delta W^+=\delta W^-=0$ (the Cotton tensor vanishes since $\nabla\mathrm{Ric}=0$). Because $W^\pm=E\pm B$, this gives simultaneously
$$
\delta E=0,\qquad \delta B=0.
$$
Reduced along the Killing fiber, the electric/magnetic decomposition $E_{ab}=W_{aVbV}$, $B$ = mixed block, is exactly the Weyl "electric/magnetic" split relative to $V$, and $\mathcal L_V E=\mathcal L_V B=0$ kills every "time" derivative. The Bianchi system therefore collapses to a purely spatial first‑order **div–curl (Maxwell–Weyl) system on the base**:
$$
\operatorname{div}_{q,\ell}B=(\text{algebraic in }E,B,u,z),\qquad \operatorname{curl}_{q,\ell}B=(\text{algebraic}),\qquad \text{likewise for }E,
$$
with the calibration $|E+B|^2=\tfrac1{24}$ as an algebraic constraint. A transverse (weighted‑divergence‑free) trace‑free symmetric tensor with bounded $L^2$ has additional interior regularity; an elliptic div–curl estimate for this system would control $\nabla B$ by algebraic quantities and hence forbid the small‑scale concentration of $|B|^2$ that §3 left open. This is the coercive object Step 12 §7 sought, now with the correct source: not a raw Bochner on $a_\pm$ (whose trace mode $|z|^2,\langle u,z\rangle$ was the obstruction), but the Bianchi‑reduced Maxwell–Weyl system with the exact static simplification $\mathcal L_V(E,B)=0$.

A concrete, low‑cost step: derive this reduced $\delta W^\pm=0$ system in the $(g_B,v,F_B)$ variables symbolically (in the style of the existing `verify_chiral_reduction_identity.py` / `verify_rank1_reduction.py`), confirm $\delta_{q,\ell}B=0$, and test whether it plus $|E+B|^2=\tfrac1{24}$ yields an interior $\int_{B_{r/2}}|\nabla B|^2\lesssim\int_{B_r}(|B|^2+1)$ Caccioppoli‑type inequality. On the two exact checks already in hand ($H^2\times H^2$: $E=\operatorname{diag}(-\tfrac23,\tfrac13,\tfrac13)$, $B=0$; Taub–NUT–AdS: $E+B=0$, $E-B\ne0$) the div–curl relations must close, so those give free correctness tests.

### 5. The reconciliation that reframes the whole question

Pointwise $H\succeq0$ is neither attainable (§2) nor necessary. The real force of the calibration is second order. On the calibrated set $|W^+|^2\equiv\tfrac1{24}$ is constant, so Derdziński's Einstein identity
$$
\nabla^*\nabla W^+=\tfrac{s}{2}W^+-6\,\overset{\circ}{(W^+)^2}
$$
forces, via $\tfrac12\Delta|W^+|^2=\langle W^+,\nabla^*\nabla W^+\rangle-|\nabla W^+|^2=0$, the exact value
$$
|\nabla W^+|^2=\tfrac{s}{2}|W^+|^2-6\operatorname{tr}\!\big((W^+)^3\big)=-2\cdot\tfrac1{24}-6\big(-\tfrac1{288}\big)=-\tfrac{1}{12}+\tfrac1{48}=-\tfrac1{16}<0,
$$
an impossibility. (Any convention shift only rescales; the sign statement is the germ obstruction of Step 6.) So a smooth calibrated Einstein germ cannot exist at all — the accessibility program's target is not "$H\succeq0$" but "produce a controlled chart on which the germ obstruction can act." In that light the correct role of §1–§4 is:

- $H\succeq0$ is a first‑order proxy for chart control; it holds pointwise only where $|B|\le\sqrt6/8$, holds in $L^2$ everywhere with constant $\tfrac13(K_0-\tfrac83)$, and can be replaced by the divergence‑free structure of $B$ (§4) as the mechanism that prevents $|B|$ concentration;
- the decisive missing input is a weighted interior regularity estimate for the Bianchi‑reduced Maxwell–Weyl system that converts the $L^2$ bound on $B$ into scale‑invariant smallness of $(\mathrm{Ric}_B)_-$ at a fixed working scale, feeding weighted integral‑Ricci harmonic‑radius control and then the germ obstruction.

### 6. Two objects that would settle the branch decisively

1. **A weighted div–curl (Caccioppoli/Moser) estimate** for the $\delta_{q,\ell}E=\delta_{q,\ell}B=0$ system with the algebraic calibration $|E+B|^2=\tfrac1{24}$, on an $\mathrm{RCD}(-1,4)$ base with fiber weight $\ell$, giving $\big(\fint_{B_{r/2}}|B|^p\big)^{1/p}\lesssim\big(\fint_{B_r}|B|^2\big)^{1/2}+1$ for some $p>3$. This would upgrade §3 from a bound to the scale‑invariant smallness needed, closing the twist branch through the germ obstruction rather than through pointwise positivity.

2. **An integrated (not 1‑jet) rank‑one model** in which $W^+$ stays calibrated, both Weyl energies stay $L^2$‑bounded per unit weighted volume, and $|B|^2$ concentrates so that the weighted quotient reconstruction radius tends to zero while $(\mathrm{Ric}_B)_-$ escapes any scale‑invariant smallness. Because Derdziński (§5) forbids an exact calibrated germ, such a model must be *approximately* calibrated with a defect $\delta\to0$; producing one would show the twist branch is not closable by curvature energy alone and would redirect the construction toward the metric‑measure reconstruction interface of Step 12 §6. Taub–NUT–AdS does not qualify (its core‑reaching means diverge and its accessible annuli carry $E+B=0$, i.e. are uncalibrated), so this remains genuinely open and is the sharpest test of the whole approach.

The precise deliverables requested are therefore: (A) yes, with the explicit sharp 1‑jet above and the threshold $|B|>\sqrt6/8$; (B) yes in $L^2$ ($p=2>3/2$) with the explicit constant $\fint(H)_-^2\le\tfrac13(K_0-\tfrac83)$, but this is boundedness, not the scale‑invariant smallness the construction needs; (C) no pointwise inequality can bound $|B|$ by $|W^+|$ because the chiral symmetric Riccati parts decouple, and the correct coercive replacement is the Einstein Bianchi identity $\delta W^\pm=0$ reduced along the Killing fiber to a static Maxwell–Weyl div–curl system, whose weighted interior estimate is the concrete next computation.