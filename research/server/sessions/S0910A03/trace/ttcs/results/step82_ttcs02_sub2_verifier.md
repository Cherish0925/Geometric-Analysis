# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/workspace/scripts/step82_center_jet_invariants.py",
    "Sessions/S0910A03/workspace/data/step82_center_jet_invariants.json",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step81_collapse_and_contraction.md"
  ]
}
```

## Task

Resolve a possible error in the proposed radial production law for K in the Step-82 note. Work in fixed periodic z coordinates with physical arclength derivative D_s=e^{-a}∂_z, measure dμ=e^aρ dz=ρ ds, σ=logρ, h=D_sσ, U:S^1→H^2, A=D_sU, b=∂_rU, e=|A|^2, k=e-h^2, K=<k>, u=a_r, v=σ_r, H=u+v, x=<u>, y=<v>. Use only target covariant derivatives, [∂_r,D_s]=-uD_s, and normalized moving averages. Independently derive K'. Check whether the exact kinematic identity is K'=-2<τ,b>+2<vc>+Cov(v-u,k)-2xK with τ=∇_sA+hA and c=h_s+h^2, or whether an additional explicit traceless-orbit defect term belongs while τ is retained. Then derive the Codazzi relation with E=Ric+3g and all normalization factors. For exact reflected scalar-minus-six center, verify u_r=-k/4, v_r=3+k/4, b_r=-τ (under the chosen target normalization), K'(0)=0, and K''(0)=72+2<|τ|^2>+(3/8)Var(k). State precisely how orbit defect enters if one substitutes the orbit evolution for τ, and flag double counting. Also check the x cubic coefficient. Ground the answer in the actual Step-82 files, but recompute rather than trusting the prior generator.

## Output

## Verification memo — Step-82 radial production law for K, center jet, and Codazzi relation

I recomputed everything from the stated definitions (fixed periodic $z$, $D_s=e^{-a}\partial_z$, $d\mu=\rho\,ds$, $\tau=\nabla_sA+hA$, $c=h_s+h^2$), using only $[\partial_r,D_s]=-uD_s$, target metric compatibility, and periodic integration by parts. I did not reuse the prior generator algebra. The headline outcome:

**The exact kinematic production law is**
$$
K'=-2\langle\tau,b\rangle+2\langle vc\rangle+\operatorname{Cov}(v-u,k)-2xK,
$$
**with no additional orbit-defect term.** The extra $+2\langle\mathcal E_0,b\rangle$ printed in draft (8.1) does not belong while $\tau$ is retained, and its sign is opposite to the term that actually appears if $\tau$ is eliminated. Everything else in §7 (the center jet, $K'(0)$, $K''(0)$, the $x$ cubic coefficient) reproduces exactly, and the §8 Codazzi relation reproduces exactly with its normalization factors.

---

### 1. Two tools that control the whole computation

Moving-measure rule. Since the density $w=e^a\rho$ obeys $w_r=Hw$,
$$
\tfrac{d}{dr}\!\int f\,d\mu=\int(f_r+Hf)\,d\mu,\qquad
\langle f\rangle'=\langle f_r\rangle+\operatorname{Cov}(H,f).
$$

Slice integration by parts. With $\partial_z\rho=\rho e^a h$,
$$
\int (D_sF)\,d\mu=-\int Fh\,d\mu,\qquad\text{i.e. }\langle D_sF\rangle=-\langle Fh\rangle.
$$
Check: $F=1$ gives $\langle h\rangle$-type identity $\int h\,d\mu=\int\partial_z\rho\,dz=0$. ✓

Applied to $v$: $\langle h\,D_sv\rangle=-\langle v(D_sh+h^2)\rangle=-\langle vc\rangle$, which is where $c=h_s+h^2$ enters.

---

### 2. Independent derivation of $K'$

Kinematic pieces (all off-shell):
- $h_r=\partial_r(D_s\sigma)=D_sv-uh$ (commutator plus $\sigma_r=v$);
- $\nabla_rA=\nabla_sb-uA$ (commutator on the map, $A=D_sU$, $b=\partial_rU$);
- $e_r=2\langle\nabla_rA,A\rangle=2\langle\nabla_sb,A\rangle-2ue$;
- $\langle\nabla_sb,A\rangle=D_s\langle b,A\rangle-\langle b,\nabla_sA\rangle=D_s\langle b,A\rangle-\langle b,\tau\rangle+h\langle b,A\rangle$.

Hence
$$
k_r=e_r-2hh_r
=2D_s\langle b,A\rangle+2h\langle b,A\rangle-2\langle b,\tau\rangle-2h\,D_sv-2uk .
$$

Averaging with the two tools:
- $\langle 2D_s\langle b,A\rangle\rangle=-2\langle h\langle b,A\rangle\rangle$ **cancels** $+2\langle h\langle b,A\rangle\rangle$;
- $-2\langle h\,D_sv\rangle=+2\langle vc\rangle$;
- $-2\langle uk\rangle=-2\operatorname{Cov}(u,k)-2xK$.

So $\langle k_r\rangle=-2\langle\tau,b\rangle+2\langle vc\rangle-2\langle uk\rangle$, and with $K'=\langle k_r\rangle+\operatorname{Cov}(H,k)$, $H=u+v$,
$$
\boxed{\,K'=-2\langle\tau,b\rangle+2\langle vc\rangle+\operatorname{Cov}(v-u,k)-2xK\,}.
$$
This uses **no Einstein equation**. $\tau=\nabla_sA+hA$ is exactly the weighted slice tension (it equals $\rho^{-1}\nabla_s(\rho A)$), a geometric quantity present even for exact Einstein. The two cancellations above are the substantive content; they are what removes any would-be defect contribution.

---

### 3. How the orbit defect really enters — the double counting

The exact-Einstein orbit-map equation, rederived in Gaussian gauge, is
$$
\nabla_rb+Hb+\tau=\mathcal E_0 ,
$$
where the full 2-D weighted tension splits into a radial part $\nabla_rb+Hb$ and the slice part $\tau$, and $\mathcal E_0$ is the traceless orbit component of $E=\operatorname{Ric}+3g$. (I verified the coefficients: $\tfrac1{e^a\rho}\nabla_r(e^a\rho\,b)=\nabla_rb+Hb$, and $\tfrac1{e^a\rho}\nabla_z(\rho A)=\nabla_sA+hA=\tau$.)

If one eliminates $\tau$ in the boxed identity via $\tau=\mathcal E_0-\nabla_rb-Hb$,
$$
-2\langle\tau,b\rangle=-2\langle\mathcal E_0,b\rangle+2\langle\nabla_rb,b\rangle+2\langle Hb,b\rangle .
$$
Therefore:
- the defect enters with coefficient $-2\langle\mathcal E_0,b\rangle$ (not $+2$), and
- when it enters, $\tau$ is **gone**, replaced by $2\langle\nabla_rb+Hb,\,b\rangle$.

Draft (8.1) keeps $-2\langle\tau,b\rangle$ *and* adds $+2\langle\mathcal E_0,b\rangle$. That is a genuine double counting (both the kinematic tension and its Einstein value are summed) and additionally carries the wrong sign for the defect. The corrected object is the boxed identity; the note's §7 hedge that (8.1) “has not yet been independently tensor-verified” is now resolved: four terms are correct, the fifth must be removed.

---

### 4. Codazzi relation (§8) with all normalizations

Contracted Codazzi in the orthonormal slice frame, $\operatorname{Ric}_{rs}=(\operatorname{div}_\Sigma S)(e_s)-D_sH$, with block-diagonal shape operator ($S e_s=u e_s$, $S|_{\rm orbit}=B$, $\operatorname{tr}B=v$), geodesic $z$-lines ($\nabla_{e_s}e_s=0$), and slice orbit shape $\mathcal W=\tfrac12G^{-1}G_s=\tfrac h2 I+\mathcal W_0$:
$$
(\operatorname{div}_\Sigma S)(e_s)=D_su+uh-\operatorname{tr}(\mathcal W B),\qquad
\operatorname{Ric}_{rs}=-D_sv+uh-\operatorname{tr}(\mathcal W B).
$$
Splitting $B=\tfrac v2I+B_0$, $\mathcal W_0=\tfrac12M^{-1}M_s$, $B_0=\tfrac12M^{-1}M_r$:
$$
\operatorname{tr}(\mathcal W B)=\tfrac{hv}{2}+\operatorname{tr}(\mathcal W_0B_0),\qquad
\operatorname{tr}(\mathcal W_0B_0)=\tfrac14\operatorname{tr}(M^{-1}M_sM^{-1}M_r)=\tfrac12\langle U_s,b\rangle .
$$
With $E_{rs}=\operatorname{Ric}_{rs}$,
$$
\boxed{\,D_sv=h\!\left(u-\tfrac v2\right)-\tfrac12\langle U_s,b\rangle-E_{rs}\,},
$$
matching the note verbatim, including the $\tfrac12$ on the map cross-term and the sign of $E_{rs}$. The normalization used throughout is the $H^2$ metric $\tfrac12\operatorname{tr}((M^{-1}dM)^2)$, giving $|\mathcal W_0|^2=\tfrac12e$, $|B_0|^2=\tfrac12|b|^2$, consistent with the script's stated $|U_r|^2=2|B_0|^2$.

---

### 5. Center jet at an exact reflected $R(q_0)=-6$ center

Reflection makes $a,\sigma,G,U$ even in $r$, so $u(0)=v(0)=0$, $b(0)=0$, $H(0)=0$ pointwise. Intrinsic slice curvatures (cohomogeneity-one, flat $T^2$ orbits, arclength coordinate valid on the 1-D base):
$$
R^q_{zz}=-h_s-\tfrac12h^2-\tfrac12e=-c-\tfrac12k,\qquad
R^q_{\rm orb}=-h_s-h^2=-c,
$$
so $\int R^q_{\rm orb}\,d\mu=-\int c\,d\mu=0$ (matches §3). The pointwise Gauss constraint at the totally geodesic center gives $R(q_0)=-6$, i.e. $-2h_s-\tfrac32h^2-\tfrac12e=-6$, hence
$$
c=3-\tfrac14k=\tfrac{12-k}{4},\qquad \langle k\rangle=K(0)=12 .
$$
Tangential evolution at $H=0,\;E=0$:
$$
v_r(0)=R^q_{\rm orb}+6=-c+6=3+\tfrac14k,\qquad
u_r(0)=R^q_{zz}+3=-c-\tfrac12k+3=-\tfrac14k,
$$
and from the orbit evolution with $\mathcal E_0=0$, $\nabla_rb(0)=-\tau$, i.e. $b_r(0)=-\tau$. All three reproduce §7 exactly. Note $K'(0)=0$ follows both from the boxed identity (every term carries a factor that vanishes at the center) and, independently, from $K$ being even in $r$.

---

### 6. $K''(0)$ and the $x$ cubic coefficient

Differentiating the boxed identity at the center (where $\operatorname{Cov}(H,\cdot)=0$ since $H(0)\equiv0$), term by term:
- $-2\langle\tau,b\rangle$: $\to 2\langle|\tau|^2\rangle$ (using $b(0)=0$, $\nabla_rb(0)=-\tau$);
- $2\langle vc\rangle$: $\to 2\langle v_r(0)c(0)\rangle=2\langle(3+\tfrac14k)(3-\tfrac14k)\rangle=18-\tfrac18\langle k^2\rangle$;
- $\operatorname{Cov}(v-u,k)$: $\to \langle(v_r-u_r)k\rangle-\langle v_r-u_r\rangle\langle k\rangle=(36+\tfrac12\langle k^2\rangle)-108=-72+\tfrac12\langle k^2\rangle$;
- $-2xK$: $\to -2x'(0)K(0)=-2(-3)(12)=+72$.

Sum:
$$
K''(0)=18+2\langle|\tau|^2\rangle+\tfrac38\langle k^2\rangle
=72+2\langle|\tau|^2\rangle+\tfrac38\operatorname{Var}(k)\ \ge\ 72 ,
$$
using $\langle k^2\rangle=\operatorname{Var}(k)+144$. This matches (7.3) exactly.

$x$ cubic: from $x'=3-\tfrac12K-x(x+y)$ (exact), with $x'(0)=-3$, $y'(0)=6$, $x+y=3r+O(r^3)$, $K=12+\tfrac12K''(0)r^2+O(r^4)$,
$$
x'=-3+\big(9-\tfrac14K''(0)\big)r^2+O(r^4)\ \Rightarrow\
x=-3r+\big(3-\tfrac1{12}K''(0)\big)r^3+O(r^5),
$$
matching (7.4) and the script's $A=3-K''(0)/12$. Since $K''(0)\ge72$, the cubic coefficient $\le-3$, so $x(r)\le-3r-3r^3+O(r^5)$. ✓ The auxiliary $T,\widetilde T$ quadratic coefficients in `step82_center_jet_invariants.py` also reproduce ($T=r^2[18-\tfrac12\langle|\tau|^2\rangle-\tfrac3{32}\operatorname{Var}(k)]$, $\widetilde T=-r^2[\tfrac12\langle|\tau|^2\rangle+\tfrac3{32}\operatorname{Var}(k)]$), and the positive $T$ coefficient is entirely the $y^2/2=18r^2$ mean-area piece, not a spatial-fluctuation contribution.

---

### 7. What this settles and what to do with it

- The exact production law for $K$ is the four-term boxed identity; it holds off-shell. Correcting the note means deleting `$+2\langle\mathcal E_0,b\rangle$` from (8.1) and, wherever the defect is wanted explicitly for approximate connectors, substituting $\tau=\mathcal E_0-\nabla_rb-Hb$ so that the defect appears once as $-2\langle\mathcal E_0,b\rangle$ with $\tau$ removed.
- With this correction, the whole §7 center-jet package (including $K'(0)=0$ and the universal $K''(0)\ge72$ initial rise) and the §8 Codazzi relation are confirmed by independent recomputation. The “universal early worsening” statement — $K$ has a strict local minimum $12$ at any exact reflected center — is therefore on firm ground: it follows from $K'(0)=0$ together with $K''(0)\ge72$.
- The genuinely unresolved quantity is the pre-return sign of the *corrected* identity's non-mean terms. On the interval before the first return $x<0$, so $-2xK>0$ opposes the required decrease of $K$ from $12$ toward $6+2\delta$; whether $-2\langle\tau,b\rangle+2\langle vc\rangle+\operatorname{Cov}(v-u,k)$ can drive $K'<0$ before curvature concentration is the substantive dynamical question, and it is unchanged by removing the spurious defect term (the removal only affects the exact/approximate bookkeeping, not the exact-core sign analysis). A coercive lower estimate on $K'$ over the pre-return interval, or an explicit interval with $K'<0$ and controlled $E$, is what would either extend the VII$_0$ exclusion to general OT connectors or exhibit the first escape.

One consistency point worth recording for the next write-up: the two independent ways of getting $K'(0)=0$ (parity of $K$, and the four-term identity) and the two independent ways of getting the $b_r(0)=-\tau$ input (orbit evolution with $\mathcal E_0=0$; Codazzi cross-check on $D_sv$) all agree, which is why the $K''(0)$ value is robust even though it mixes on-shell jet data into an off-shell identity.