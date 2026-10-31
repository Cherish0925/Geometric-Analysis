# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/scripts/step40_nijenhuis_tariff_check.py",
    "Sessions/S1003A02/workspace/data/step40_nijenhuis_tariff_check.json",
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Skills/geometric-analysis/research/paper/sections/single_solution_coercivity.tex",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md"
  ]
}
```

## Task

Verify the new Step-40 theorems in workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md against the simultaneous signed-cost identity (Prop. 'Simultaneous signed cost identity', lines 319-447 of variational_selection_and_global_cost.tex) in its normalization s=-4, F^+=2i sigma(Phi), rho=|Phi|^2 in [0,2], psi=2sqrt2 sigma(Phi), W_0=(1/4)(rho^2 I/3 - psi psi). Check in detail: (1) Lemma 1: that the Clifford contraction of the u^perp-valued part of the first jet has kernel exactly the Gray-Hervella W_2 (almost-Kaehler / Nijenhuis) component, that cc*=2, hence rho|v_4|^2=|a+J'b|^2/2 under D_A Phi=0, and that this is correct in the presence of the U(1) connection; (2) the pointwise Weitzenboeck formula (1/2)Delta rho + |nabla Phi|^2 = rho(2-rho)/2 in this normalization (the integrated version K=(1/2)int rho(2-rho) follows from the paper's slack identities); (3) Theorem N as an exact equality, including the polynomial m-rho^2(2-rho) and the (a,b) quadratic form, and the Hermitian corollary P>=8pi^2 Q; (4) Theorem W: the self-dual Weitzenboeck convention (Delta_H = nabla*nabla - 2W^+ + s/3 with W_0 having Kaehler eigenvalue s/6), |d psi|^2 = 2 rho |b|^2 under the Dirac equation, and the collapse of the (a,b) form to -4|zeta|^2; (5) Theorem E: the pointwise envelope g_{t,lambda}, the use of |W^+|^2 = rho^4/24 - rho^2 x/2 + |M|^2 and |M|^2 >= (3/2) x^2, and the exact conclusion that the threshold is t=2/3 binding at rho=3/2. Report any sign, factor, convention, or quantifier error and its repair, and say precisely which statements are proved. Also assess whether Theorem E really shows that no pointwise/algebraic compensation inequality can give k-dependence, and what global terms remain.

## Output

## Verification memo — Step 40 (Theorems N, W, E) against the simultaneous signed-cost identity

**Headline.** I reproduced all five pieces by hand in the paper's $s=-4$, $F^+=2i\sigma(\Phi)$, $\rho\in[0,2]$, $\psi=2\sqrt2\sigma(\Phi)$, $W_0=\tfrac14(\tfrac{\rho^2}{3}I-\psi\otimes\psi)$ normalization. Theorems N and W are **exact equalities** with no sign, factor, or convention error; the Hermitian corollary $P\ge8\pi^2Q$ follows. Theorem E's envelope polynomial $g_{t,\lambda}$ is assembled correctly and the $t=2/3$ optimum binding at $\rho=3/2$ is right. The one place where the written statement is stronger than what is strictly derived is the universal "no pointwise/algebraic compensation" phrasing; I describe below exactly how much is proved and what the structural argument actually supports.

---

### 1. Lemma 1 (Clifford contraction, Nijenhuis identification)

With $\Phi=\sqrt\rho\,u$, $\nabla_{\mathcal A}\Phi=(a+ib)u+\sqrt\rho\,v\,u^\perp$, the three norm identities follow directly: $|\nabla\Phi|^2=|a+ib|^2+\rho|v|^2=|a|^2+|b|^2+\rho|v|^2$; $\zeta=\langle\Phi,\nabla\Phi\rangle=\sqrt\rho(a+ib)$ so $|\zeta|^2=\rho(|a|^2+|b|^2)$; and $d\rho=2\sqrt\rho\,a$ is consistent with $a=d\sqrt\rho$. The Hopf/Fubini–Study factor giving $|\nabla n|^2=4|v|^2$ is right (the $i\beta u$ phase does not move $n$), and this is where the $U(1)$ connection correctly drops out: $n$ is gauge invariant, so $\nabla n$ depends on $v$ only, not on $\beta$. The connection is absorbed into $b=\sqrt\rho\,\beta$, and the whole lemma is pointwise algebraic in $(a,b,v)$, independent of whether these arise from $d$ or $\nabla_{\mathcal A}$.

- **(i) $cc^*=2\,\mathrm{Id}_{S^-}$:** correct; realified $S^-$ is $4$-real-dimensional, $\operatorname{tr}cc^*=8$. The script's `CCt_minus_2I`$\approx10^{-16}$ confirms $cc^T=2I_4$.
- **(ii) $\ker c=\mathcal W_2$:** correct and conceptually sound. In real dimension four the Gray–Hervella content is exactly $\nabla\omega\in\mathcal W_2\oplus\mathcal W_4$ (both $4$-dimensional; $\mathcal W_1=\mathcal W_3=0$), $\mathcal W_2$ being $d\omega=0$ (almost-Kähler, Nijenhuis), $\mathcal W_4$ the Lee form. The dimension count ($\dim\mathcal W_2=4=\dim\ker c$) plus the Taubes canonical-spinor inclusion gives equality, and the script's coincident kernels (`kernel_cosines`$=1$, `rank_C`$=$`rank_dOmega`$=4$) confirm $\ker c=\ker(v\mapsto d\omega)$.
- **(iii)** Clifford linearity $(a+ib)\cdot u=(a+J'b)\cdot u$ with $J'$ orthogonal, $J'^2=-I$, verified (`Jprime_orthogonal`, `Jprime_squared_plus_I`, `complex_clifford_norm_residual` all $\sim10^{-15}$).

**Dirac consequence.** From $D_{\mathcal A}\Phi=(a+ib)\cdot u+\sqrt\rho\,c(v)=0$ with $v=v_2+v_4$, $c(v_2)=0$, and $|c(v_4)|^2=2|v_4|^2$ (nonzero singular values of $c$ are $\sqrt2$), one gets $|a+J'b|^2=|(a+ib)\cdot u|^2=\rho\cdot2|v_4|^2$, i.e. $\rho|v_4|^2=\tfrac12|a+J'b|^2$ with $v_2$ free. Verified. This is the single pointwise constraint the Dirac equation imposes on the first jet, and it is exactly what Theorems N and W use.

### 2. Pointwise Weitzenböck

$\tfrac12\Delta\rho+|\nabla\Phi|^2=\langle\nabla^*\nabla\Phi,\Phi\rangle=-\tfrac s4\rho-\tfrac12\langle F^+\!\cdot\Phi,\Phi\rangle$. With $s=-4$ and the moment-map identity $\langle i\sigma(\Phi)\cdot\Phi,\Phi\rangle=\tfrac12|\Phi|^4$, $\langle F^+\!\cdot\Phi,\Phi\rangle=2\cdot\tfrac12\rho^2=\rho^2$, giving $\tfrac12\Delta\rho+|\nabla\Phi|^2=\rho-\tfrac12\rho^2=\tfrac12\rho(2-\rho)$ (with $\Delta=d^*d\ge0$). The maximum principle then gives $0\le\rho\le2$, and the integral is $K=\int|\nabla\Phi|^2=\tfrac12\int\rho(2-\rho)$, matching the paper's slack identity. Correct.

### 3. Theorem N — exact equality confirmed

I reproduced the full chain. The paper's identity, after $K=\tfrac12\int\rho(2-\rho)$, gives the **amplitude form**
$$\mathfrak S=\int m(\rho)-8\|\zeta\|^2-4\|M\|^2-\mathcal W,\qquad m=\tfrac{(2-\rho)(-\rho^3+10\rho^2-2\rho-4)}6,$$
and I verified $2\rho(2-\rho)-b(\rho)(2-\rho)^2=m(\rho)$ by hand (expanding $(-\rho^2+8\rho+2)(2-\rho)=\rho^3-10\rho^2+14\rho+4$). Multiplying the pointwise Weitzenböck by $\psi=2\rho$ gives $\int2\rho|\nabla\Phi|^2+4\int\rho|a|^2=\int\rho^2(2-\rho)$. Substituting $|\nabla\Phi|^2=|a|^2+|b|^2+\rho|v_2|^2+\tfrac12|a+J'b|^2$ and $\int m=\int\rho^2(2-\rho)-\int\tfrac{(2-\rho)^2(2+2\rho-\rho^2)}6$ (the `m_identity_residual`$=0$ check), I obtained exactly
$$\int\rho^2(2-\rho)-8\!\int\!\rho(|a|^2+|b|^2)=\underbrace{\tfrac12\!\int\!\rho^2|\nabla n|^2_{\mathcal W_2}}_{=2\int\rho^2|v_2|^2}-\int\rho(|a|^2+5|b|^2-2\langle a,J'b\rangle),$$
which is Theorem N. The $(|a|^2,|b|^2,\langle a,J'b\rangle)$ quadratic form has matrix $\binom{\;1\;-1}{-1\;\;5}$, determinant $4>0$, positive definite, so the subtracted term is $\ge0$; and $2+2\rho-\rho^2>0$ on $[0,2]$ (roots $1\pm\sqrt3$). The only unsubtracted term is the Nijenhuis energy $\tfrac12\int\rho^2|\nabla n|^2_{\mathcal W_2}$. **Theorem N is an exact equality.**

**Corollary 1 (Hermitian tariff) is proved:** if every $J_\epsilon$ is integrable on $\{\Phi\ne0\}$ then $\mathcal W_2=0$ (dimension four: $N=0\Leftrightarrow\mathcal W_2=0$), the sole positive term vanishes, $\mathfrak S\le0$, $P\ge8\pi^2Q$. This genuinely contains and extends the Step-38 Kähler theorem (Kähler $\Rightarrow$ integrable). Corollary 2's quantitative lower bound $\mathbb E\int\rho^2|\nabla n|^2_{\mathcal W_2}\ge16\pi^2(1-c)k$ is the correct rearrangement, and $16\pi^2\times0.0043373\approx0.68488$ matches the cell enclosure. The Corollary 3 scale law ($\rho^2\le4$, diffuse rotation over diameter $r$ buys $O(r^2)$) is dimensionally correct.

### 4. Theorem W — exact equality confirmed

The self-dual Weitzenböck $\nabla^*\nabla\psi=\Delta_H\psi+2W^+\psi-\tfrac s3\psi$ is the standard sign ($\Delta_H=\nabla^*\nabla-2W^++\tfrac s3$). With $W_0\psi=-\tfrac{\rho^2}6\psi$ (I checked: $\tfrac14(\tfrac{\rho^2}3-\rho^2)\psi=-\tfrac{\rho^2}6\psi$, so $|W_0|^2$ has eigenvalues $(-\rho^2/6,\rho^2/12,\rho^2/12)$) and $\|d^*\psi\|=\|d\psi\|$ for a self-dual form, I confirmed
$$\int|\nabla\psi|^2=2\|d\psi\|^2+2\!\int\!(W^+-W_0)(\psi,\psi)+\int\tfrac{\rho^2}3(4-\rho^2).$$
Using $|\nabla\psi|^2=4\rho|a|^2+\rho^2|\nabla n|^2$ (the cross term dies since $\langle n,\nabla n\rangle=0$) with $\rho^2|\nabla n|^2=4\rho^2|v_2|^2+2\rho|a+J'b|^2$, and $|d\psi|^2=2\rho|b|^2$ (numerically confirmed: `Qd_eigs`$=\{0^4,2^4\}$), substitution into Theorem N gives — and I verified every term by hand — the exact
$$\mathfrak S=\mathbb E\!\int[\rho^2x-4|M|^2]+\mathbb E\!\int\tfrac{(2-\rho)(\rho-1)(3\rho+2)}3-4\mathbb E\|\zeta\|^2-\mathcal W,\quad x=M(n,n).$$
The $(a,b)$ cross terms cancel exactly: the combined form reduces to $-4\rho(|a|^2+|b|^2)=-4|\zeta|^2$ (the JSON `G_eigs` all $=-4$ confirm this), and the amplitude polynomial collapses via `weitzenboeck_identity_residual`$=0$. **Theorem W is an exact equality.** The interpretation $x>0\Leftrightarrow W^+(n,n)>-\rho^2/6$ is correct ($W^+(n,n)=-\rho^2/6+x$), and $4|M|^2\ge6x^2$ is right: minimizing $\|M\|^2$ over trace-free symmetric $M$ with $\langle Mn,n\rangle=x$ gives $M=\tfrac32x(n\otimes n-\tfrac13 I)$, $|M|^2=\tfrac32x^2$.

### 5. Theorem E — envelope construction correct

I reconstructed $g_{t,\lambda}$ from the three exact relations. Taking $(1-t)\times$(closed identity, with $|W^+|^2=\rho^4/24-\rho^2x/2+|M|^2$, volume density $4/3$) $+\,t\lambda\times$(Theorem W) $+\,t(1-\lambda)\times$(amplitude form), the $4|M|^2$ coefficients sum to $1$, the topological constants give $8\pi^2[k-(1-t)A]$, the $x$-coefficient is $-(t\lambda+2-2t)\rho^2$, and minimizing $4|M|^2-(t\lambda+2-2t)\rho^2x$ under the sharp $|M|^2\ge\tfrac32x^2$ (so $4|M|^2\ge6x^2$, optimum $x=(t\lambda+2-2t)\rho^2/12$) yields the penalty $-(t\lambda+2-2t)^2\rho^4/24$. The result matches the note exactly:
$$g_{t,\lambda}=(1-t)\!\left(\tfrac{\rho^4}6+\tfrac43\right)-t\!\left[\lambda\tfrac{(2-\rho)(\rho-1)(3\rho+2)}3+(1-\lambda)m\right]-\tfrac{(t\lambda+2-2t)^2\rho^4}{24}.$$
I confirmed the two closing facts: $g_{2/3,2/3}=-\tfrac2{243}(2\rho-3)^2(\rho^2-24\rho-18)\ge0$ on $[0,2]$ (second factor negative there), reproducing LeBrun's $C_+\ge2A/3$ (equivalently $P/8\pi^2\ge k-A/3$); $\max_\lambda g_{t,\lambda}(3/2)=-\tfrac34(3t-2)<0$ for $t>2/3$ with $\lambda_{\rm opt}=2-8/(9t)$; and $g_{2/3,2/3}(2)=124/243>0$, so the envelope binds only at $\rho=3/2$, strictly slack at the Kähler–Einstein amplitude $\rho=2$. All sign-correct.

---

### Assessment: does Theorem E really exclude pointwise $k$-dependence, and what global terms remain?

What is rigorously established: within the two-parameter family of convex combinations of the three exact pointwise identities (closed Chern–Weil/Gauss–Bonnet, Theorem W, amplitude form) together with the sharp Weyl inequality $|M|^2\ge\tfrac32x^2$, and discarding the nonnegative $\mathcal W$ and $\|\zeta\|^2$ reservoirs, the largest linear-in-$A$ coefficient obtainable is $t=2/3$, binding at the single amplitude $\rho=3/2$. For $0<k<A/3$ this family produces no positive lower bound (LeBrun's $k-A/3<0$ there). That is a precise and correct statement.

Two things to keep distinct. First, Theorem N is not an independent resource from the amplitude form — I showed above they are the *same* identity after the $\psi=2\rho$ kinetic reorganization — so the genuinely independent exact pointwise inputs are the cost identity, the two Weitzenböck identities, the closed topological identity, and $|M|^2\ge\tfrac32x^2$; the $(t,\lambda)$-envelope does use all of them. Second, the envelope fixed the Weitzenböck multiplier at $\psi=2\rho$; a different weight function would produce a different amplitude polynomial, so the written universal "no pointwise/algebraic combination" is one step beyond the two-parameter optimization. The feature that actually makes the broader statement robust is the scale law (Corollary 3) together with the pointwise saving-density bound ($\max_\rho F_{3/4}=0.8$): the per-point saving is bounded and can be realized at low $\rho$ spread over large volume with no pointwise penalty, so any density-level inequality caps the integrated saving by volume rather than by $k$. I would present Theorem E as: the natural envelope of all derived exact pointwise identities cannot beat LeBrun, binding at $\rho=3/2$ and slack at $\rho=2$, and the diffuse-spreading structure explains why no pointwise density bound can force $k$-scaling for $k<A/3$ — rather than as a closed proof over every conceivable pointwise scheme.

Remaining global reservoirs (what a $k$-dependent bound for $0<k<A/3$ must draw on), all consistent with Step 38: the Walsh self-dual energy $\mathcal W=2\|f_\varnothing^-\|^2+2\sum_{I\ne\varnothing}\|f_I^+\|^2$; the harmonic-projection terms $J_\epsilon$; the $\zeta$-energy pricing the Lee component and amplitude gradients; and elliptic/regularity structure of the actual solutions. The three candidate mechanisms in Section 5 (localization of Nijenhuis energy near the $E_i$-dual cycles via the fixed $4\pi^2$ singleton $h^-$ charge; a growth statement forcing $\sum_I\|f_I^+\|^2$ or $J_\epsilon$ up under diffuse rotation of all $2^k$ structures; or the converse construction with $\rho\approx1.6$, $x>0$ on volume $\gtrsim10\pi^2(1-c)k$) are the right places; none is a pointwise object, which is the correct lesson from Theorem E.

### Items still carried numerically

Two inputs feeding Theorem W are confirmed only in an explicit Clifford model, not yet derived in the paper's conventions: $|d\psi|^2=2\rho|b|^2$ (the $\mathcal W_2$ part of $\nabla n$ lying in $\ker d$) and the integrated self-dual Weitzenböck form. Both are internally consistent and numerically clean (`Qd_eigs`$=\{0^4,2^4\}$, residuals $\sim10^{-10}$), but since Theorem W's collapse to $-4\|\zeta\|^2$ depends on $|d\psi|^2=2\rho|b|^2$, a hand derivation in the fixed Clifford conventions would close the last analytic step. Lemma 1(ii)'s identification $\ker c=\mathcal W_2$ likewise rests on the dimension count plus Taubes' canonical-spinor inclusion plus the numerical kernel coincidence; a one-line conceptual argument (the Dirac contraction of the $u^\perp$-jet is the self-dual part of $d\omega$) would make it fully analytic. These do not affect the correctness of the exact equalities as checked, which hold once these two identities are granted.