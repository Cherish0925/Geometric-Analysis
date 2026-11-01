# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step60_resonant_h4_neck_drift_and_alf_flux.md",
    "Sessions/S0910A02/workspace/data/step60_resonant_flux_neck_alf.json",
    "Sessions/S0910A02/workspace/data/step60_neck_drift_schedules.json",
    "Sessions/S0910A02/workspace/data/step60_warp_neck_drift_model.json",
    "Sessions/S0910A02/workspace/notes/step59_h4dual_two_scale_matching_analysis.md",
    "Sessions/S0910A02/workspace/notes/step34_indicial_modediag_resonance_and_collapse.md",
    "Sessions/S0910A02/workspace/notes/step42_mode_projection_bridge_resolution.md",
    "Sessions/S0910A02/workspace/notes/step11_cz_spike_and_proposition_A.md"
  ]
}
```

## Task

Verify the mathematical substance of the Step-60 correction for Yau-26. Read the Step-60 note and supporting data, with the Step-59 and Step-34/42 context. Check scale conventions, the l=2 Wronskian/log resonance, the claim that H4 necessity is only rate-limited by delta_i log(1/t_i)->0 (conditional on annular gauge/projection), the local opposite-warping neck-drift model, and the first ALF scalar flux model. Identify any serious mathematical error, hidden assumption, or overstatement; also state which parts look sound and what the next decisive computation/proof should be. Do not decide the whole Yau-26 problem; focus on this correction and its consequences.

## Output

# Verification Memo: Step-60 Correction (Yau-26, S0910A02)

## Bottom line

The Step-60 computations I can check are arithmetically correct, and the central structural move — replacing a nonresonant weighted estimate by the resonant $l=2$ Wronskian/flux identity at the indicial root $\beta=2$, and thereby reinstating the $\delta_i\log(1/t_i)$ dependence — is coherent and, I believe, mathematically right. It is a genuine self-correction of Steps 35–36/42, not a regression. The rate-limited necessity statement and the exponential drift channel form a clean dichotomy at the model level. Two things deserve emphasis: (i) the necessity statement rests on unproven annular gauge/projection infrastructure that Step 60 correctly does not pretend to have; (ii) the neck-drift construction has an $O(1)$-amplitude nonlinear obstruction at the outer scale that the linear Laplacian model does not touch, and this is the make-or-break issue for the counterexample side.

## What checks out

**l=2 radial ODE, homogeneous solutions, Wronskian.** Indicial equation $\alpha^2+2\alpha-8=(\alpha-2)(\alpha+4)$ gives roots $2,-4$; $W(r^2,r^{-4})=-6r^{-3}$, so $r^3W=-6$ is scale-independent. Correct.

**Particular solution and its verification.** For constant $S$,
$$f_p=\tfrac{S}{6}r^2\log(r/r_0)-\tfrac{S}{36}(r^2-r_0^6r^{-4}).$$
I applied $L$ by hand: $L[r^2\log r]=6$ (since $g''+3g'/r-8g/r^2$ with $g=r^2\log r$ gives $2\log r+3+6\log r+3-8\log r=6$), so $Lf_p=S$; and $f_p(r_0)=f_p'(r_0)=0$. Both confirmed. The growing-coefficient drift $\tfrac{S}{6}\log(R/r_0)$ with $R=t^{-1/2}$, $r_0=O(1)$ gives $\tfrac{S}{12}\log(1/t)$, i.e. relative drift $\tfrac{\delta}{12}\log(1/t)$. The `1/12` constant in the JSON is consistent (the $1/6$ from the ODE times $1/2$ from $\log t^{-1/2}$).

**Weighted-exponent scaling.** $\|E_i\|_{C^0_{\beta-2}}\sim t_i\delta_i R_i^{2-\beta}=\delta_i t_i^{\beta/2}$ at $R_i=t_i^{-1/2}$ is the correct scaling, and $\beta=2$ being the $l=2$ indicial root is correct. The exponential thresholds in `step60_neck_drift_schedules.json` ($\log(1/t)=a/\delta$, $\log_{10}=a/(\delta\ln10)$) reproduce exactly, e.g. $\delta=0.2,a=1\Rightarrow\log_{10}(1/t)=2.171$.

**Neck-drift Laplacian.** I recomputed the polar Laplacian of $u=tr^2A(\log r)\cos2\theta$: radial part $\phi''+\phi'/r=4A+4A'+A''$, angular part $-4A$, total $t(A''+4A')\cos2\theta$. Confirmed. The schedule arithmetic (cubic $q=3z^2-2z^3$, $\max q'=1.5$ at $z=1/2$, $\max|q''|=6$ at endpoints, giving $\max|\Delta u|/(t\delta)=6.12$ for $\delta=0.02,\Delta A=1,L=50$) checks out.

**ALF scalar indicial data.** $\mathbb R^3$ harmonics $r^\ell,r^{-\ell-1}$ give $\alpha_+=\ell,\alpha_-=-\ell-1$; $r^2(f_+f_-'-f_-f_+')=-(2\ell+1)$. Correct, and the mass mode $\ell=0$ pair $(0,-1)$ is genuinely different from the ALE $(2,-4)$ pair, so the ALE degeneracy condition $R_\pm\zeta=0$ is indeed not the ALF obstruction. The source-accumulation integral $\int_1^R r^{2-q}dr$ (polynomial $q<3$, log $q=3$, bounded $q>3$) is elementary and correct.

**Chern–Weil energy quantization.** With $\mathrm{Ric}\to g$ (so traceless-Ricci $E\to0$, $\int|E|^2\le\delta^2\mathrm{Vol}\to0$) and $s\to4$ with $\mathrm{Vol}\to0$ (so $\int s^2/24\to0$), Gauss–Bonnet gives $\int|W|^2\to8\pi^2\chi$ and the signature split $\int|W^\pm|^2\to2\pi^2(2\chi\pm3\tau)$. Verified: $\int|W^+|^2=(8\pi^2\chi+12\pi^2\tau)/2=2\pi^2(2\chi+3\tau)$. The $\chi>0$ blow-up conclusion ($\int|W|^2\le\sup|W|^2\,\mathrm{Vol}\to0$ contradiction) is correct, and the principal-$S^1$-bundle $\chi=0$ (versus $\chi(S^2\times S^2)=4$) fact is correct.

## The one subtle point: Step-60 versus Steps 35–36/42

The heart of the correction is the assertion that Steps 35–36 wrongly removed the resonance by using fixed annuli plus an iterated $i\to\infty,R\to\infty$ limit. I checked this and Step 60 is right.

For an exact homogeneous $r^2$ mode the coefficient is scale-independent, so fixed-annulus extraction at radius $R$ reads a well-defined number. But the Ozuch identification $\lambda_k=c\langle R_\pm(p)\zeta,\zeta\rangle$ requires the $f\sim H_2+O(\rho^{-2})$ matching *at the orbifold transition* $\rho\sim t^{-1/2}$ (Step 59 §3). The coefficient at a fixed bubble-frame radius $R$ and the coefficient at $\rho\sim t^{-1/2}$ differ by the source accumulated between them, which for a coherent constant-in-$\rho$ $l=2$ source of size $\delta$ is $\delta\log(t^{-1/2}/R)=\delta(\tfrac12\log(1/t)-\log R)$. Holding $R$ fixed while $t\to0$ this is unbounded unless $\delta\log(1/t)\to0$. The iterated-limit language in Steps 35–36/42 concealed that the extraction radius must be pushed toward $t^{-1/2}$, which couples $R$ to the sequence. So the resonance is real, Step 34's original $\delta\log(1/t)$ was structurally correct, and the retraction was the error. This is a valuable catch.

One reconciliation worth stating precisely, because it looks like a contradiction but is not. Step 59's Open Lemma targets $\|w_i\|_{C^{2,\alpha}_\beta}\le C(t_i+\delta_i)$ (after subtracting $t_i\underline h_2$), while Step 60's "factor over target $\delta_it_i^{\beta/2-1}$" measures against the compact-set signal $O(t_i)$. The apparent divergence in Step 60 is because $\delta$ and $t$ are independent, and the necessity conclusion must resolve the $O(t_i)$ signal against an error whose bare size is $O(\delta_i)$. The value of the resonant flux identity is exactly that the scale-invariant Wronskian pairing reads the $t$-order signal with *relative* error $\delta\log(1/t)$, avoiding the $\delta/t$ catastrophe that naive nonresonant inversion targeting $O(t)$ on compact sets would incur. So Step 60's preference for the $\beta=2$ flux object over a $\beta\in(0,2)$ Fredholm inversion is internally consistent and is the correct reading of which analytic object carries the obstruction. The two notes are compatible once "target" is read as the $O(t)$ compact-set signal.

## What the necessity statement still rests on

The rate-limited theorem is genuinely conditional, and the note says so, but the reader should keep the full list in view because none of it is a one-dimensional computation:

- existence of compatible gauges across the whole neck (not just on fixed annuli);
- a rigorous $l=2$ projection on annular regions of a Cheeger–Naber limit under merely bounded Ricci (Step 42 imports Cheeger–Naber $C^{1,\alpha}\cap W^{2,q}$ regularity for this, which is legitimate, but the projection of the *defect* onto tensor harmonics on a singular limit is not yet a proven operation);
- control of nonlinear and gauge commutators, i.e. that the $Q(h,h)$ and gauge terms do not themselves feed a coherent $l=2$ source of size comparable to $\delta$;
- subtraction of the ambient $H_2/H_4$ tower without introducing new resonant sources.

The Wronskian-plus-flux reduction is correct *given* these; the one-dimensional ODE is not a substitute for them. The det $R_+$ table in Step 42 §7 is also relevant here and remains valid: for every positive Kähler–Einstein orbifold $\det R_+=0$, so even a fully rigorous first-order necessity theorem does not touch the $\#_k(S^2\times S^2)$ stress family. The rate-limited necessity theorem, even if all four analytic pieces were supplied, would constrain only the near-round/non-KE limits — it is one first-order obstruction among several needed.

## The decisive weak point on the construction side

The neck-drift model's linear source estimate is where I would concentrate suspicion. The ansatz $u=tr^2A(\log r)\cos2\theta$ has, near the outer radius $R=t^{-1/2}$, amplitude $u\sim tR^2=O(1)$. That is not a small perturbation. The reported Ricci source $O(t\delta)$ is the *linear* (Laplacian) part only; the true Ricci defect contains quadratic gradient terms $|\nabla u|^2$, $\nabla u\cdot\nabla F$, and the doubly-warped cross terms, none of which are perturbative when the warping amplitude is $O(1)$. The note flags this ("$O(tR^2)=O(1)$ only after correct subtraction/gauge normalization; this needs a real nonlinear estimate"), but the numerical schedules report only $\max|\Delta u|/(t\delta)$, which is the linear quantity. So the tables do not yet demonstrate an $O(\delta)$ *Ricci-operator* defect — they demonstrate an $O(\delta)$ *Laplacian* defect. The gap between these is precisely the mechanism that Step 11 exploited in the opposite direction (there the quadratic terms were controlled by small amplitude; here the amplitude is not small at the scale that matters). Any statement that the drift channel is "credible enough to deserve construction pressure" is defensible, but the channel is not yet shown compatible with an $O(\delta)$ Ricci defect once the nonlinear terms at the outer scale are included.

## ALF model status

The scalar model is a correct first orientation but is a $\mathbb R^3$-scalar surrogate. The real content — whether a forced flux or an energy defect appears under positive Einstein normalization — lives in the tensor Lichnerowicz system on the actual ALF metric with circle-fibration gauge and cosmological normalization, where the indicial roots and boundary Wronskian differ from both the scalar $\mathbb R^3$ roots and the ALE tensor roots. The observation that ALF collapse can be more sensitive to slowly decaying sources ($R^{3-q}$ growth for $q<3$ versus ALE's log at the indicial root) is a correct and useful pointer, but it is derived from the scalar mass mode, not the tensor system. Nothing here is overstated; it is explicitly a "first cheap computation."

## Where the next decisive step lies

I agree with the note's own two targets and would sharpen the order of decisiveness:

1. **Full doubly-warped curvature for the neck-drift ansatz, including all quadratic/gradient and cap terms, at the outer scale $r\sim t^{-1/2}$ where $u=O(1)$.** This single computation decides whether the exponential drift channel survives as a real Ricci-pinched object or collapses because the nonlinear terms exceed $O(\delta)$. It is the lowest-cost computation that can change the judgment on the counterexample side, and it directly attacks the weak point above. If the nonlinear Ricci defect at the outer scale is forced above $O(\delta)$, the channel is answered in the direction of necessity; if it stays $O(\delta)$ after gauge normalization, the channel becomes a serious counterexample candidate and the caps/EH-matching tasks become the frontier.

2. **Tensor ALF indicial roots and boundary Wronskian for Euclidean Schwarzschild / Taub–NUT in the actual Lichnerowicz/Ricci system with positive-Einstein normalization**, to determine whether the leading mass/bolt mode carries a forced nonzero flux or a forced energy defect in $\chi>0$ collapse — the natural continuation of the correct Chern–Weil quantization.

A secondary but load-bearing item for the necessity side is turning the "standard annular gauge/projection setup" into an actual construction on a Cheeger–Naber limit, since that, not the Wronskian, is what stands between the rate-limited statement and a theorem.

## One convention note for the record

Step 34 uses "ALE coefficient $t^4$, balance radius $r=t^{2/3}$"; Steps 42/59/60 use "metric scale $t$, outer radius $R=t^{-1/2}$." The symbol $t$ does not mean the same thing across these steps. Both conventions produce the same $\delta\log(1/t)$ relative drift, so the physics is consistent, but the two $t$'s should not be identified in any future write-up.