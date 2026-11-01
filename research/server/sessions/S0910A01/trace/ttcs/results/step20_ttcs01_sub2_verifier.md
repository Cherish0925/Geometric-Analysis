# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A01/workspace/scripts/step20_tensor_closed_curvature_energy.py",
    "Sessions/S0910A01/workspace/scripts/step20_triangular_defect_energy.py",
    "Sessions/S0910A01/workspace/notes/step19_whitney_tensor_estimate.md",
    "Sessions/S0910A01/trace/ttcs/results/step19_ttcs01_verifier1_integration.md",
    "Sessions/S0910A03/workspace/notes/step19_p4_threshold_and_degenerate_moser.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md"
  ]
}
```

## Task

Verify the Step 20 analytic change in the Yau 26 four-dimensional negative-route cutoff-flow work. Read the Step 20 closed tensor estimate, Step 20 scripts, and Step 19 Whitney/TTCS context. Check scientifically: (1) whether E=Ric+g and nabla E=contraction(nabla Rm) legitimately allow the Hess(a) and nabla a*nabla E terms in the curvature-power energy to be absorbed into full curvature dissipation without a separate high-power defect-gradient energy; (2) whether the schematic curvature variation under h=-2aE correctly has no Einstein-independent Hess(a) source; (3) whether the q-dependent inequality and the warning about all-exponent critical absorption are mathematically sound; (4) whether the triangular unweighted defect estimate avoids the invalid +epsilon X inference and can preserve Q/A->0 under small beta; and (5) what exact gaps remain before this becomes a theorem. Be strict about hidden assumptions: evolving metric, volume form, covariant derivative convention, cutoff Hessian, finite-neighbor summation, Sobolev constants, and collapse-uniform constants.

## Output

# Verification Memo: Step 20 closed-curvature and triangular-defect change (S0910A01, four-dimensional Ricci=−g cutoff-flow laboratory)

## What Step 20 actually changes, and why it is the right structural move

The load-bearing new idea is that under $\partial_t g=-2aE$, $a=\chi^2$, $E=\operatorname{Ric}+g$, the defect tensor $E$ and its gradient are *algebraic functions* of the curvature and its gradient, not independent fields. Because $g$ is parallel,
$$
E_{ij}=R_{kikj}+g_{ij},\qquad \nabla_pE_{ij}=\nabla_pR_{kikj}=\nabla_p\operatorname{Ric}_{ij},
$$
so $|E|\le C_n(1+|\operatorname{Rm}|^2)^{1/2}=C_nF$ and $|\nabla E|\le C_n|\nabla\operatorname{Rm}|$ are exact pointwise contractions on every smooth slice, requiring no persistence of the initial near-Einstein pointwise bound. This is correct and is a genuine conceptual gain over the Step 19 two-field energy $H=R+\kappa P$: the curvature-power energy becomes self-contained, and the defect-gradient contributions fold into the same curvature dissipation $\int\eta^2 aF^{q-2}|\nabla\operatorname{Rm}|^2$. I confirm each of the five points below, with the exponent balances I re-derived, and then state precisely what remains before this is a theorem.

## Point 1 — absorbing Hess(a) and ∇a·∇E into curvature dissipation

Legitimate. The IBP in (4.2) and the Young step (4.3) balance correctly. Tracking weights for the representative term $\int\eta^2|\nabla a|F^{q-1}|\nabla H|$: split as $\big(\sqrt a\,F^{(q-2)/2}|\nabla H|\big)\cdot\big(F^{q/2}|\nabla a|/\sqrt a\big)$; the second factor squared is $F^{q}|\nabla a|^2/a$, giving exactly $\epsilon\int\eta^2 aF^{q-2}|\nabla H|^2+C_\epsilon\int\eta^2(|\nabla a|^2/a)F^q$. Since $|\nabla a|^2/a=4|\nabla\chi|^2\le 4L^2r^{-2}$, no inverse power of $\chi$ survives. The higher-power mixed remainders that the Step 19 verification memo raised — $\frac{|\nabla a|^2}{a}|E|^2|H|^{q-2}$ — collapse to $\frac{|\nabla a|^2}{a}F^q$ under $|E|\le C_nF$, $|H|\le F$, so they are absorbed by the same regular cutoff potential, at the price of the larger $q$-power in (5.1). This is the correct resolution of the earlier coupling concern: no separate defect-gradient energy is needed at any exponent. The cost — the $q^3$ coefficient on $(|\nabla a|^2/a+a)F^q$ — is real and matters for Point 3.

## Point 2 — no Einstein-independent Hess(a) source

Correct, and it resolves a genuine disagreement with the A03 Step 19 note. Keeping the full velocity $h=-2aE$ together, every term of $\partial_t R_{ijkl}$ is linear in $E$: $\nabla_i\nabla_k(aE_{jl})=a\nabla_i\nabla_k E_{jl}+(\nabla a)*\nabla E+(\nabla^2 a)E_{jl}$, and the reaction $h*R=-2a\,E*R$. Every term carries $E$, $\nabla E$, or $\nabla^2E$; at an exact $\operatorname{Ric}=-g$ metric ($E\equiv0$) the flow is stationary regardless of $\nabla a,\nabla^2a$. The A03 Step 19 note (§4) wrote the normalized-flow correction as $D\operatorname{Rm}(h_2)\sim(\nabla^2a)\owedge g+a\operatorname{Rm}$, which suggests a $\nabla^2a\owedge g$ source surviving at $E=0$. That form comes from splitting $-2aE=-2a\operatorname{Ric}-2ag$; the metric-part Hessians recombine with the Ricci-part Hessians into $\nabla^2a\owedge E$. Step 20 uses A03's own second listed option (merge the full velocity), and it is the correct one. The two sessions are now consistent on this.

One item is asserted rather than derived: (2.2), $a\nabla\nabla E=a\Delta\operatorname{Rm}+a(\operatorname{Rm}*\operatorname{Rm})+a\operatorname{Rm}$, is the standard DeTurck/Uhlenbeck reduction via twice-contracted Bianchi, but it is only schematic here. The precise reaction coefficients and the linear normalization term need the explicit computation (see Gaps).

## Point 3 — the q-inequality (5.1) and the all-exponent warning

The warning is mathematically sound and, in fact, aligns the argument with the actual structure of the source. In 0911.3104 the critical smallness enters *once* at the base exponent (Theorem 3.4: $e_0\le(3C_0A)^{-1}$), and the Moser climb (Theorem 2.5, requiring $p_0>2$) then propagates via the potential $u$ with its $\mu t^{-1/3}$ decay — it does **not** re-impose critical absorption at every level. The Step 20 statement that direct all-exponent absorption needs $C(q)\beta_\ell<c$ with $C(q)$ growing is therefore correct: attempting to absorb $\int aF^{q+1}$ into dissipation at every $q$ via the fixed critical product $\beta_\ell=S_\ell\|\operatorname{Rm}\|_2\le C\sqrt{K_0}\,r^2$ does not work uniformly. The proposed route — reach one fixed $q_0>2$, then run a positive-time mean-value argument with $F$ as a supercritical potential — is precisely Li's Theorem 2.5 architecture, and is the right target. I did not fully re-derive the exact $q$-powers in (5.1); the note states they are improvable, and the qualitative $q$-monotonicity of the absorption threshold (the script's $\beta_{\max}=c/(Cq)$ table) is what carries the argument, which is legitimate.

The regularized norm $F=(1+|\operatorname{Rm}|^2)^{1/2}$ is used correctly to swallow the linear $a\operatorname{Rm}$ normalization term into $aF^q$; with the $\operatorname{Ric}=-g$ baseline $|\operatorname{Rm}|\ge c>0$ this does not alter the critical scaling. Consistent with A03.

## Point 4 — the triangular unweighted defect estimate

The structural core is correct and is the essential fix. The additive form $Q'\le Cr^{-2}Q+\epsilon X$, $X=\int a|\nabla\operatorname{Rm}|^2$, indeed cannot preserve $Q/A\to0$: Gronwall gives $Q(T)\lesssim e^{cT}(Q(0)+\int_0^T X)$, and since $\int_0^T X$ is comparable to the dissipated total curvature energy $\sim\int|\operatorname{Rm}|^2=O(A)$ in the LeBrun/Ishida–LeBrun sequence, a fixed $\epsilon$ leaves $O(\epsilon A)$, i.e. $O(\epsilon)$ after dividing by $A$ — not $o(1)$. The numerical illustration ($\int X/A=10$, additive $Q(T)/A\approx0.11$ versus triangular $\approx10^{-4}$) correctly encodes this. The remedy is exactly right in principle: since $\partial_t E$ has no curvature-only forcing (same fact as Point 2), testing by $\eta^2E$ makes curvature appear only as a potential on $|E|^2$, and the support-summed unnormalized $Q$ satisfies $Q_{\text{support}}(T)\le\exp(C_N T/r^2)Q_{\text{support}}(0)$, which preserves $Q/A\to0$ over $T=\theta r^2$.

There is one point in (7.1)–(7.3) that must be pinned down exactly, because the whole absorption depends on it. The written $E$-equation (7.1) includes a term $(\nabla a)*\operatorname{Rm}*E$. From the actual linearization $\partial_tE=D\operatorname{Ric}_g(-2aE)-2aE$ with
$$
D\operatorname{Ric}(k)=-\tfrac12\Delta_L k-\tfrac12\nabla^2(\operatorname{tr}k)+\operatorname{sym}\nabla(\operatorname{div}k),\quad k=-2aE,
$$
the terms produced are $a\Delta_L E$ (whose curvature piece is $a\operatorname{Rm}*E$), $\nabla a*\nabla E$, $(\nabla^2a\ \text{or}\ \Delta a)*E$, and the gauge pieces $a\nabla\operatorname{div}E$, $a\nabla^2\operatorname{tr}E$ (which combine through the contracted Bianchi identity $\operatorname{div}E=\tfrac12\nabla\operatorname{tr}E$). I do **not** find a $\nabla a*\operatorname{Rm}*E$ term arising from this computation — the only curvature$\times E$ coupling is $a\operatorname{Rm}*E$, with weight $a$. This matters decisively:

- If the potential is genuinely $a|\operatorname{Rm}|$, then (7.3) is valid using only critical $L^2$: $\int a|\operatorname{Rm}||E|^2=\int|\operatorname{Rm}|\,|\chi\eta E|^2\le\|\operatorname{Rm}\|_2\|\chi\eta E\|_4^2\le\beta_\ell(\int\eta^2 a|\nabla E|^2+\ell^{-2}\int a\eta^2|E|^2)$, and (7.4)–(7.5) close for small $\beta_\ell$.
- If a $(\nabla a)*\operatorname{Rm}*E$ term were truly present, then $|\nabla a|=2\sqrt a|\nabla\chi|$ turns it into a $\sqrt a|\operatorname{Rm}|=\chi|\operatorname{Rm}|$ potential (times $r^{-1}$), which near $\chi\to0$ is larger than $a|\operatorname{Rm}|=\chi^2|\operatorname{Rm}|$ by a factor $\chi^{-1}$, or after Young produces an $a|\operatorname{Rm}|^2$ potential whose absorption needs $\||\operatorname{Rm}|\|_{L^4}$ — i.e. the output of the Point-1/Point-3 curvature $\varepsilon$-regularity, not the input critical $L^2$.

So the triangular estimate is correct **provided** the mixed term in (7.1) is confirmed absent (which the standard linearization indicates) and the curvature potential is exactly $a|\operatorname{Rm}|$. I flag the written $(\nabla a)*\operatorname{Rm}*E$ as the one item to verify by explicit computation; on the standard reduction it does not appear and (7.2)–(7.5) close on critical $L^2$ alone.

A quantitative correction inherited from the Step 19 verification also applies here: the $\ell^{-2}\int a\eta^2|E|^2$ term is $\ell^{-2}a\sim(c^2r^2)^{-1}$, so the $r^{-2}$ in (7.3)/(7.5) is really $c^{-2}r^{-2}$, and the exponential factor is $\exp(C_N\theta/c^2)$. Over $T=\theta r^2$ with $\theta\lesssim c^2$ this stays $O(1)$, so the conclusion is unaffected, but the constant should be written with the $c^{-2}$.

## Exact remaining substance before this is a theorem

1. **Explicit tensor evolution.** Write $\partial_t\operatorname{Rm}$ under $\partial_t g=-2aE$ with every $a,\nabla a,\nabla^2 a$ term, verifying (2.2) and the reaction/normalization coefficients of (5.1), including the volume-form variation $\partial_t d\mu=-\operatorname{tr}(aE)\,d\mu=-a(\operatorname{scal}+n)\,d\mu$ inside $\tfrac{d}{dt}\int\eta^2 F^q$ (this adds an $\int\eta^2 F^q\,a|E|\lesssim\int\eta^2 aF^{q+1}$ term — controllable but currently only "schematic"). The exact $q$-powers should be produced rather than asserted.

2. **Precise E-equation and its potential.** Confirm the exact form of (7.1); in particular settle whether $(\nabla a)*\operatorname{Rm}*E$ is present. The standard $D\operatorname{Ric}(-2aE)$ reduction gives only an $a\operatorname{Rm}*E$ coupling, which is what (7.2)/(7.3) need; this should be verified in index form so that the potential in (7.2) is provably $a|\operatorname{Rm}|$ and (7.3) uses critical $L^2$ only.

3. **The localized parabolic theorem itself.** From (5.1) plus critical smallness, prove either $|a\operatorname{Rm}|\le C/t$ or a fixed $L^{q_0}$, $q_0>2$, bound followed by a positive-time mean-value argument, for the degenerate operator $\partial_t-a\Delta$ with the cutoff-perturbed, tensor, finite-neighbor structure. This is the same object A03 lists as its Step-3 target and the Step 19 verification identifies as unproved; it is a genuine new PDE result, not a corollary of Li Theorem 2.5/3.4 or Wang Theorem 6.3, whose hypotheses are global. The scripts are exponent ledgers and explicitly do not prove it.

4. **Finite-neighbor summation.** Make (7.4)→(7.5) rigorous as a differential inequality on the bounded-overlap Whitney graph of *unnormalized* $Q_\alpha$, with the overlap multiplicity $N(n,L,c)$ entering multiplicatively. Step 20 correctly uses unnormalized support-summed energy, avoiding the normalized-energy summation issue flagged for Step 19; the summation lemma still needs to be stated and proved.

5. **Bootstrap inputs that the estimates presuppose.** Metric comparability $e^{-\zeta}g_0\le g(t)\le e^{\zeta}g_0$ (H1) and the persistence of the Whitney Sobolev constant $S_\ell$ under the evolving metric are used to make $\beta_\ell$ small and $\chi_0$-independent; these are closed only by the metric-drift integration $\int_0^{\theta r^2}|aE|\,dt=O(\delta r^2)$ (A03's $p>2$ integration), which itself rests on the weighted defect estimate. The first-exit closure joining (b)–(e) is standard in form but circular-looking until items 2–3 are in hand; the dependency graph should be written so that each provisional bound is strictly improved.

6. **Collapse-uniform constants through the completed iteration.** The $\chi_0$- and volume-independence is proved for the geometric inputs (BG transfer, squared-Sobolev product $S_\ell\|\operatorname{Rm}\|_2\le C\sqrt{K_0}r^2$, ellipticity ratio, overlap). Independence of the *final* constants can only be asserted once the iteration (item 3) is complete.

7. **Distance to Yau 26.** This is one conditional link (the localized parabolic input) inside the conditional 10-step chain of Step 19 §13, for the four-dimensional $\operatorname{Ric}=-g$ LeBrun/Ishida–LeBrun family only. The general statement — all $n\ge2$, both signs of $\lambda$, all closed manifolds — is untouched, as the notes state.

## Overall

Step 20 is a correct and valuable structural simplification. The algebraic identities $|E|\le C_nF$, $|\nabla E|\le C_n|\nabla\operatorname{Rm}|$ genuinely make the curvature-power energy self-contained (Point 1), the merged-velocity variation removes the spurious $\nabla^2a\owedge g$ source and reconciles A01 with A03 (Point 2), the all-exponent warning correctly steers toward Li's fixed-$q_0$-plus-mean-value structure (Point 3), and the triangular defect estimate is the right mechanism to preserve $Q/A\to0$ against an $\int X=O(A)$ dissipation (Point 4). The exponent bookkeeping I re-checked is consistent; the scripts state their function accurately as ledgers. The two things that most affect whether (7.2)–(7.5) close as written are the exact form of the $E$-equation potential (item 2) and the localized degenerate parabolic theorem (item 3); the latter is the single unproved analytic result on which both the curvature and defect layers still depend.