# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step91_separator_stability_and_barriers.md",
    "Sessions/S0910A03/workspace/scripts/step92_jacobi_concentration_models.py",
    "Sessions/S0910A03/workspace/data/step92_jacobi_concentration_models.json",
    "Sessions/S0910A03/workspace/scripts/step92_weighted_jacobi_transform.py",
    "Sessions/S0910A03/workspace/data/step92_weighted_jacobi_transform.json",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md"
  ]
}
```

## Task

Independently verify and sharpen the Step 92 separator analysis. Check the corrected contracted-Gauss sign; derive the full invariant second-variation inequality from the rho^2 gamma minimizing loop; conjugate the weighted Jacobi operator and verify the stated potential after substituting R_q=-2h_s-(3/2)h^2-e_s/2 and R_q=-6+D-|II|^2. Then assess the square-spike calculation: does stable J=-d^2+a-A 1_I on a periodic circle permit A→∞ with width ell→0 and A ell approaching 2 sqrt(a)tanh(sqrt(a)L/2)? State precisely what this proves and does not prove for geometric Q, including the role of variable rho and Maxwell/orbit equations. Seek any immediate rigorous concentration consequence stronger than the constant test, but reject unsupported regularity or scale assumptions.

## Output

# Verification memo — Step 92 separator Jacobi analysis

Session S0910A03. I re-derived each stated identity independently and ran the algebra by hand where the scripts use `sympy`/`scipy`. The central conclusions hold. Details, one concrete sharpening, and the genuinely open mechanism follow.

## 1. Contracted-Gauss sign — confirmed

For a hypersurface $\Sigma^3\subset(X^4,g)$ the trace Gauss equation is
$$R_\Sigma = R_g - 2\operatorname{Ric}_g(\nu,\nu) + H^2 - |\mathrm{II}|^2 .$$
With $E=\operatorname{Ric}_g+3g$, so $R_g=\operatorname{tr}E-12$ and $\operatorname{Ric}_g(\nu,\nu)=E(\nu,\nu)-3$,
$$R_g-2\operatorname{Ric}_g(\nu,\nu)=\operatorname{tr}E-2E(\nu,\nu)-6=-6+D,\qquad D=\operatorname{tr}E-2E(\nu,\nu).$$
At $H=0$ this gives $R_q=-6+D-|\mathrm{II}|^2$, i.e. exactly (8.2)/(2.1). In an orthonormal frame $D=E(T,T)+E(V_1,V_1)+E(V_2,V_2)-E(\nu,\nu)$, four terms each in $[-\delta,\delta]$, so $|D|\le4\delta$ and $R_q\le-6+4\delta$. The Step 91 correction is right: at a minimal separator the intrinsic scalar curvature sits below zero for $\delta<3/2$, and the $-\tfrac12 e_s$ term in $R_q=-2h_s-\tfrac32h^2-\tfrac12 e_s$ supplies rather than opposes it. The withdrawn "positive-turning" reading was the error; the present sign is internally consistent with the Koiso totally geodesic value $R_q=-6$ at $\delta=0$.

The §1 flat-slice statement is also correct: $R(q_r)=0$ plus the general Gauss form gives $H^2-\operatorname{tr}(S^2)=6-D$, and $\operatorname{tr}(S^2)\ge H^2/3$ yields $\tfrac23H^2\ge6-4\delta$, i.e. $H^2\ge9-6\delta$. This forbids $H=0$ on a flat-torus level set for $\delta<3/2$, so a radial cylindrical throat cannot pass through a minimal flat slice. That obstruction stands.

## 2. Reduction to the one-dimensional weighted form (8.4) — confirmed

For $\Sigma=\pi^{-1}(C)$ with induced $q=ds^2+G_{ab}d\xi^a d\xi^b$ and $d\mu=\rho\,ds\,d\xi$, an invariant test $\phi=\phi(s)$ has $|\nabla_\Sigma\phi|^2=(\partial_s\phi)^2$ and the fiber integrates to the constant torus volume. The two-sided stable second variation restricted to invariant $\phi$ is therefore
$$\int_C\rho\big[(\partial_s\phi)^2+(3-E(\nu,\nu))\phi^2\big]ds\ \ge\ \int_C\rho\big(\kappa^2+\tfrac12 h_\nu^2+\tfrac12 e_\nu+Q\big)\phi^2\,ds,$$
which is (8.4) with $a=3-E(\nu,\nu)$ and $V=|\mathrm{II}|^2=\kappa^2+\tfrac12h_\nu^2+\tfrac12e_\nu+Q$. One point worth stating explicitly for the record: the stability used here is stability **only against invariant normal variations**, and it is exactly the second variation of $\rho^2\gamma_B$-length of the minimizing loop $C$. The area functional restricted to invariant hypersurfaces *is* the $\widehat\gamma$-length functional, so the two second variations coincide identically on this class; the weighted-length minimizer supplies (8.4) with no appeal to full homological area minimization. The constant test $\phi\equiv1$ recovers $\langle V\rangle_C\le 3+\delta$, hence $\langle Q\rangle_C\le3+\delta$ since $V\ge Q$ pointwise. Consistent with (3.4).

## 3. Weighted-Jacobi conjugation and the $-\tfrac34$ coefficient — reproduced by hand

With $\rho=e^\sigma$, $J\phi=-\rho^{-1}(\rho\phi')'+(a-V)\phi$, and $\phi=e^{-\sigma/2}y$:
$$e^{\sigma/2}J\phi=-y''+\Big(a-V+\tfrac12\sigma''+\tfrac14\sigma'^2\Big)y,$$
matching the `sympy` residual-zero result. Using $h=\sigma'$ and $R_q=-2h_s-\tfrac32h^2-\tfrac12e_s\Rightarrow\sigma''=-\tfrac12R_q-\tfrac34h^2-\tfrac14e_s$, the weight potential is
$$W=\tfrac12\sigma''+\tfrac14\sigma'^2=-\tfrac14R_q-\tfrac18e_s-\tfrac18h^2.$$
Substituting the minimal-separator value $R_q=-6+D-V$ (valid pointwise on $C$ because $H\equiv0$ there),
$$W=\tfrac32-\tfrac14D+\tfrac14V-\tfrac18e_s-\tfrac18h^2,$$
and the full Schrödinger potential is
$$a-V+W=\tfrac92-E(\nu,\nu)-\tfrac34V-\tfrac14D-\tfrac18e_s-\tfrac18h^2.$$
I confirm all three JSON expressions and the key structural fact: after the intrinsic-curvature substitution the coefficient on $V=|\mathrm{II}|^2$ is $-\tfrac34$, not $-1$, while $e_s$ and $h^2$ enter with minus sign. The conjugation does not manufacture a definite-sign potential; the operator remains a Schrödinger form whose potential can be driven far below zero by a large $V$. So the conjugated form yields no pointwise or supremum control of $V$ (hence none of $Q$). This is the correct reading, and it is a genuine addition over the naive expectation that the $\rho$-weight might tame the $-V$ term.

## 4. Square-spike model — independently confirmed, with the limit derived cleanly

The monodromy method is sound: both inside ($y''+(A-a)y=0$) and outside ($y''-ay=0$) transfer matrices have unit determinant (Wronskian), and a periodic zero mode is $\operatorname{tr}M=2$. The threshold $A_{\rm crit}(\ell)$ marks where the lowest periodic eigenvalue of $J=-d^2+a-A\mathbf 1_{[0,\ell]}$ reaches zero; below it $J\ge0$ (stable), above it $J$ acquires a mode below zero.

I reproduced the small-width limit exactly by the $\delta$-well reduction. As $\ell\to0$ with $\beta=A\ell$ fixed, the well acts as $-\beta\delta$; the symmetric periodic zero mode $y=\cosh(\mu(|s|-L/2))$, $\mu=\sqrt a$, with jump condition $y'(0^+)-y'(0^-)=-\beta y(0)$ gives $-2\mu\sinh(\mu L/2)=-\beta\cosh(\mu L/2)$, hence
$$\boxed{A_{\rm crit}\,\ell\ \longrightarrow\ 2\sqrt a\,\tanh(\sqrt a\,L/2).}$$
For $a=3,\ L=2\pi$ this is $2\sqrt3\tanh(\sqrt3\,\pi)\approx3.4638$ (since $\tanh(5.44)\approx1$). The JSON rows descend $5.66\to4.52\to\cdots\to3.53$ toward $3.464$, and `Aell_over_2sqrt_a`$\to1$. The numerics agree with the closed form to the digits shown; the trace residuals ($\sim10^{-10}$) confirm the root solves are converged. So the model conclusion is correct: stability permits $A\to\infty$ as $\ell\to0$, with the retained invariant being the mass $A\ell\lesssim2\sqrt a$, and $A\ell^2\to0$. There is no supremum ceiling and no universal width.

**What this proves.** In a decoupled one-dimensional weighted stability form with the geometric potential treated as free, stability alone permits arbitrarily tall, sufficiently narrow spikes of $V$ (hence of $Q$) at the separator, subject only to an integrated (capacity) mass constraint. This makes precise, and rigorously supports, the Step 91 §5 statement that separator stability bounds the average $Q_C\le3+\delta$ but does not bound the interior maximum $Q_+$.

**What it does not prove.** (i) It does not show spikes actually occur — only that stability does not forbid them. (ii) The model fixes $\rho\equiv1$ and $a\equiv3$; the true problem has variable $a\in[3-\delta,3+\delta]$ and, more importantly, a non-constant weight $\rho=e^\sigma$ whose conjugation potential $W$ (§3) reweights everything. (iii) The model treats $V$ as an external potential, but geometrically $V$ is tied to $\sigma$ through the Gauss identity; that coupling is exactly what the decoupled well omits (see §6). So the model is a permissive one-sided statement about the isolated stability form, not about the coupled system.

## 5. Strongest rigorous concentration consequence available from stability

Two statements can be made rigorously, and neither exceeds capacity/average control.

**(a) Optimized local-mass bound (a concrete sharpening of the tent test).** With $\phi=\max(1-|s-s_0|/r,0)$, constant $\rho$: $\int(\phi')^2=2/r$, $\int\phi^2=2r/3$, and $\phi^2\ge\tfrac14$ on $|s-s_0|\le r/2$, so stability gives
$$\int_{|s-s_0|\le r/2}V\,ds\ \le\ \frac8r+\frac83\,a\,r.$$
Minimizing the right side over $r$ at $r=\sqrt{3/a}$ yields the clean closed statement
$$\int_{I}V\,ds\ \le\ \frac{16}{\sqrt3}\sqrt a\ \le\ \frac{16}{\sqrt3}\sqrt{3+\delta}\ \approx\ 9.24\sqrt{3+\delta}$$
over an interval $I$ of width $\sqrt{3/a}\approx1$. This is a genuine local refinement of the constant test $\langle V\rangle\le a$; it is quotable and slightly stronger than the note's scaling form. It bounds an *integral* of $V$ over an $O(1)$ window and diverges as the window shrinks, so it gives no pointwise ceiling.

**(b) Positive-solution structure (why no supremum bound can be extracted).** $J\ge0$ on the circle is equivalent (Allegretto–Piepenbrink) to existence of $u>0$ with $Ju=0$. Writing $w=u'/u$ (with $\rho\equiv1$, $a$ const) gives the Riccati relation $V-a=-w'-w^2$. Integrating, $\oint(V-a)=-\oint w^2\le0$ recovers $\langle V\rangle\le a$; but $\sup V=a+\sup(-w'-w^2)$ is unbounded wherever $w'$ dips sharply. This shows structurally that stability determines $V$ only up to the average and permits unbounded pointwise peaks — consistent with §4 and not improvable by a cleverer test function. So the accurate assessment is: the full Jacobi form strengthens the average test to a capacity/local-mass statement, and nothing beyond that follows from stability alone.

## 6. The coupling that the decoupled model omits — a concrete avenue

The one place where the present analysis could still yield something stronger is the back-reaction the square well ignores. On $C$ the Gauss identity is a pointwise constraint linking the potential to the weight:
$$h_s=\sigma''=3-\tfrac12 D+\tfrac12 V-\tfrac34 h^2-\tfrac14 e_s .$$
A tall spike in $V$ therefore forces a large positive $h_s$ (through $+\tfrac12V$), i.e. a sharp upward bend of $\log\rho$; the spike cannot be inserted as a free potential without a matching feature in the orbit-volume profile. Integrating over the closed curve (using $\oint h_s\,ds=0$) gives the exact unweighted identity
$$\oint_C V\,ds=\oint_C\Big(-6+D+\tfrac32 h^2+\tfrac12 e_s\Big)ds .$$
This ties $\oint V$ to $\oint h^2$ and $\oint e_s$, which the decoupled model treats as unconstrained. It does not by itself close (the right side is not controlled by $\delta$), but it is the correct object on which to test whether the coupled system — Gauss constraint plus the Maxwell/orbit-shape (harmonic-map $|dU|^2$) equations plus stability — still admits a periodic stable $Q$-spike. This is where a stronger consequence, if any, must come from, and it requires the transport/regularity content of the orbit equations, not stability.

## 7. Assessment relative to the research goal

Within the near-hyperbolic ($E=\operatorname{Ric}+3g$, $\|E\|\le\delta$) free-$T^2$ obstruction program, Step 92 correctly establishes that separator stability, even in its full weighted-Jacobi form and after intrinsic-curvature conjugation, controls only the separator average and local mass of the twist energy $Q$, never its interior supremum $Q_+$. This is exactly the quantity the resolvent ceiling of Step 87/88 needs as a supremum input, and Step 91 §5 already recorded that the ceiling rises with $Q_+$ faster (slope $\approx8.86$) than the floor with $Q_C$ (slope $2$). So the orthogonally-transitive obstruction ($Q=0$, $\delta<\delta_*=0.24625$) is unaffected and stands, while the twist generalization remains genuinely open, and Step 92 rigorously identifies stability as insufficient to close it.

The missing scientific ingredient is a mechanism relating the interior maximum of the orbit energy to separator data — either an elliptic/transport estimate from the weighted Abelian Maxwell law (the constant charge scalars $\alpha_a$ of the Liu formula cited in Step 88 §5) giving $\sup e$ from integrated quantities, or a direct supremum estimate for the harmonic-map energy $|dU|^2$ under the $CD(-(3+\delta),4)$ structure. Nothing in the present material supplies it, and the concentration models correctly refrain from assuming a regularity length or pointwise ceiling that is not derived. No mathematical error was found in the derivations, the conjugation algebra, the monodromy computation, or the asymptotic; all check out independently.