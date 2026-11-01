# TTCS Independent Branch Record

```json
{
  "step_id": 73,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step73_preissmann_koiso_anisotropy.md",
    "Sessions/S0910A01/workspace/data/step73_preissmann_koiso_verify.json",
    "Sessions/S0910A01/workspace/data/step73_koiso_center_analysis.json",
    "Sessions/S0910A03/workspace/notes/step70_critical_identity_and_corrections.md"
  ]
}
```

## Task

Verify the mathematical correctness and completeness of three structural results for the graph-neck construction on T^3 graph manifolds.

Result 1 — Preissmann obstruction: For every Riemannian metric h on T^3, max |Ric_h + 2h|_op >= 2/3. The argument uses the 3D identity K_{ij} = (r_i + r_j - r_k)/2 to show that if all Ricci eigenvalues satisfy |r_i + 2| < c with c < 2/3, then all sectional curvatures are strictly negative, contradicting Preissmann's theorem for T^3 (which has Z^3 fundamental group containing Z^2). At c = 2/3, the flat torus theorem forces flatness but R_h = -16/3 ≠ 0.

Result 2 — Koiso center: At a totally geodesic center S(0) = 0 in a Gaussian collar, the Einstein equations force S'(0) = Ric_h + 3I and R_h = -6. Isotropic S' = I requires Ric_h = -2h (constant negative curvature), impossible on T^3 by Preissmann. For the T^2-invariant diagonal ansatz with a_0 = 0, the constraint R_h = -6 becomes u^2 + v^2 + uv + u' + v' = 3 where u = b_{0,theta}, v = c_{0,theta}. The Koiso accelerations are a_tt = uv, b_tt = v^2 + v', c_tt = u^2 + u'.

Result 3 — ODE anisotropy decay: For the diagonal ODE f_i'' + f_i' H = 3, the difference delta_ij = f_i' - f_j' satisfies delta_ij' + H delta_ij = 0, giving exponential decay delta_ij(t) = delta_ij(0) sech(sqrt(3) t). The claim that higher Fourier modes in the full PDE decay faster rests on the additional n^2 e^{-2a} term in the linearized operator.

Check: (a) Is the Preissmann argument correct at the boundary c = 2/3? (b) Are the Koiso formulas (3.3) correct from the T^2-inv Einstein equations? (c) Is the difference equation (4.2) correct? (d) Does the a=0 gauge really force b_t c_t = 0? (e) Is the claim about higher Fourier mode stability justified?

## Output

# Verification Memo — Three Structural Results for the T³ Graph-Neck Construction

I re-derived each result from the metric ansatz independently rather than reading the check counts. Overall: the two algebraic results (Preissmann bound, Koiso accelerations) are correct and I confirm them line by line; the difference equation is correct; the $a=0$ rank statement is correct in the ODE reduction; the higher-mode statement is a plausible expectation but is not yet established by the argument given. One paragraph in the Preissmann proof (the $c=2/3$ endpoint) is logically muddled and should be replaced, though the conclusion it supports is true and in fact strengthenable. There is also an internal inconsistency in the decay-rate constant of Result 3.

## (a) Preissmann obstruction — correct, with one paragraph to rewrite

**Strict part (fully verified).** The 3D identity $K_{ij}=(r_i+r_j-r_k)/2$ is the inversion of $r_i=\sum_{j\ne i}K_{ij}$ and is correct. More is true and is what the argument actually needs: for *any* orthonormal frame $u,v,w$ in three dimensions,
$$
K(u,v)=\tfrac12\big(\operatorname{Ric}(u,u)+\operatorname{Ric}(v,v)-\operatorname{Ric}(w,w)\big).
$$
Since $|\operatorname{Ric}_h+2h|_{\mathrm{op}}<c$ means $\operatorname{Ric}(x,x)\in(-2-c,-2+c)$ for *every* unit $x$, this gives $K(u,v)<\tfrac12((-2+c)+(-2+c)-(-2-c))=(3c-2)/2$ for **every** plane, not only eigenplanes. For $c<2/3$ this is $<0$ everywhere, so $K<0$ on a closed manifold; Preissmann forbids a $\mathbb Z^2$ in $\pi_1$, contradicting $\pi_1(T^3)=\mathbb Z^3$. If $\max|\operatorname{Ric}_h+2h|_{\mathrm{op}}<2/3$ one picks $c$ in between and reaches this contradiction, so $\max\ge 2/3$. This is airtight and needs nothing about the threshold value.

**The $c=2/3$ paragraph is inconsistent as written.** It posits saturating eigenvalues $(-4/3,-4/3,-8/3)$ giving $R_h=-16/3\ne0$ "contradicting flatness," while simultaneously invoking the flat torus theorem to force flatness. A flat metric has $\operatorname{Ric}\equiv0$, so one cannot hold fixed a Ricci spectrum that saturates the threshold *and* conclude flatness from the same metric — the two premises describe different metrics. The intended conclusion is nonetheless true and cleaner: $\max\le 2/3\Rightarrow\operatorname{Ric}(x,x)\in[-8/3,-4/3]\Rightarrow K\le0$ at every plane $\Rightarrow T^3$ flat (flat torus theorem, full-rank $\mathbb Z^3=\pi_1$, so the invariant flat $T^3$ is all of $M$) $\Rightarrow\operatorname{Ric}\equiv0\Rightarrow|\operatorname{Ric}_h+2h|_{\mathrm{op}}=2$, contradicting $\max\le2/3$. This shows the sharper $\max>2/3$ (strict). I recommend replacing the eigenvalue sentence with this chain.

I also confirmed the warped-product inputs feeding Corollary 2.2: for $g=dt^2+f^2h$ with fiber dimension 3, $(\operatorname{Ric}+3g)_{00}=-3f''/f+3$ and tangential coefficient $3f^2-ff''-2(f')^2$; with $f=\cosh t$ these give $0$ and $2$, so the center defect operator norm is $\cosh^{-2}(t)\,|\operatorname{Ric}_h+2h|_{\mathrm{op}}\ge2/3$ at $t=0$. Correct.

## (b) Koiso accelerations (3.3) — fully verified from scratch

Fiber $h=d\theta^2+e^{2b_0}dx^2+e^{2c_0}dy^2$, $u=b_0',v=c_0'$. Using $K_{\theta x}=-(u'+u^2)$, $K_{\theta y}=-(v'+v^2)$, $K_{xy}=-uv$:
$$
R^{(3)}_h=2(K_{\theta x}+K_{\theta y}+K_{xy})=-2(u^2+v^2+uv+u'+v'),
$$
matching (3.2); $R_h=-6$ gives the Riccati constraint $u^2+v^2+uv+u'+v'=3$.

Fiber Ricci eigenvalues: $r_\theta=-(u'+u^2)-(v'+v^2)$, $r_x=-(u'+u^2)-uv$, $r_y=-(v'+v^2)-uv$ (sum $=R_h$, checked). With $S'(0)=\operatorname{Ric}_h^\sharp+3I$ and the constraint,
$$
a_{tt}=r_\theta+3=3-[u'+v'+u^2+v^2]=uv,
$$
$$
b_{tt}=r_x+3=3-u'-u^2-uv=v^2+v',\qquad c_{tt}=u^2+u'.
$$
All three reproduce (3.3) exactly. Trace $=u^2+v^2+uv+u'+v'=3$ ✓. The Gauss/Hamiltonian relation (3.1) $|S|^2=H^2-6-R_h^{(3)}$ is the scalar Gauss equation for $\operatorname{Ric}_g=-3g$ in dimension 4 ($R_g=-12$, $\operatorname{Ric}(\nu,\nu)=-3$), and at $S=0$ it forces $R_h=-6$. Correct. The isotropic impossibility (§3.2) is also correct: $S'(0)=I$ needs $\operatorname{Ric}_h=-2h$, a space form of $K<0$ on $T^3$, excluded by Preissmann.

## (c) Difference equation (4.2) — correct; rate constant inconsistent

Subtracting two copies of (4.1) $f_i''+f_i'H=3$ gives $\delta_{ij}'+H\delta_{ij}=0$, hence $\delta_{ij}(t)=\delta_{ij}(0)\exp(-\int_0^tH)$. Algebraically exact.

The qualitative statement (anisotropy dies exponentially) holds because $H$ tends to a positive limit. But the specific constant is not consistent across the note. The full three-direction cusp has $H\to3$ (this is precisely the step70 identity $e^{2t}(H-3)=-3-\int_0^te^{2s}|B|^2ds$, which I re-derived and confirm: $\dot b+2b+|B|^2=0$ with $b=H-3$, $b(0)=-3$). With $H\to3$, $\exp(-\int H)\sim e^{-3t}$: rate $\approx3$. Yet (4.3)–(4.4) use $H\approx\sqrt3\tanh(\sqrt3 t)$ and report rate $\sqrt3$ with decay factor $0.34=\operatorname{sech}(\sqrt3)$ at $t=1$. The value $\sqrt3$ is the *two-direction* asymptotic of the $a=0$ gauge ($V_0'\to\sqrt3$), not the three-direction cusp. The §4.3 tables simultaneously report $H=3.000$. So the tables (three-direction, $H\to3$) and the decay formula (two-direction, $H\to\sqrt3$) belong to different scenarios. The exponential-decay conclusion survives either way, but the quoted rate $\sqrt3$ under-reports the true rate ($\sim3$) for the three-conformal-factor collar the construction actually needs. Pin the decay statement to one consistent profile.

I checked the shear budget scaling: $2(3+\int_0^Re^{2t}|S-I|^2dt)/(e^{2R}-1)$ is dominated by the universal term $6/(e^{2R}-1)$ ($=0.112$ at $R=2$, $0.00201$ at $R=4$ vs tabulated $0.130,\,0.00234$). This is why the $B=0.5$ and $B=1.0$ rows agree to 5+ digits despite different initial shear $S'(0)=(0,0.5,2.5)$ vs $(0,1,2)$: the shear integral is a subleading correction and the decay is essentially driven by the same $6/(e^{2R}-1)$ deficit that appears in the step70 $R\ge\tfrac12\log(1+6/\delta)$ length relation. This is a good cross-session consistency signal, but it also means the tables do **not** demonstrate anisotropy-specific decay — they mostly display the universal $-3$ initial deficit. To exhibit genuinely anisotropic decay one should tabulate $\int_0^Re^{2t}|S-I|^2dt$ or $\delta_{ij}(t)$ directly, isolated from the dominant constant.

## (d) $a=0$ gauge forces $b_tc_t=0$ — correct in the ODE reduction

Two independent facts collide. The normal equation carries no fiber-curvature term: $\dot H+|S|^2=3$, and with $a_t=0$, $|S|^2=b_t^2+c_t^2$, so $\dot H=3-b_t^2-c_t^2$. The summed tangential equations give $V_0''=3-V_0'^2$ with $H=V_0'=b_t+c_t$ (this uses $R_h=-6$ and $\operatorname{Ric}_\theta=-3$, so $\operatorname{Ric}_x+\operatorname{Ric}_y=-3$ cancels the excess; it is *not* a flat-slice statement). Then $\dot H=3-H^2=3-b_t^2-c_t^2-2b_tc_t$. Equating the two expressions for $\dot H$ yields $b_tc_t=0$. Verified. The rank-$\le1$ consequence (cannot reach $S=I$) is then immediate, and it reinforces the already-obvious point that $a_t\equiv0\ne1$ blocks the $\theta$-direction from expanding to the cusp. Note this is an ODE-reduction result; the full elliptic system adds $\theta$-derivative terms to the normal equation, so "$b_tc_t=0$ everywhere" is a statement about the homogeneous reduction, not the PDE.

## (e) Higher Fourier modes decay faster — plausible, not established

The principal part $\partial_{tt}+n^2e^{-2a}\partial_{\theta\theta}$ around $g_\infty=dt^2+e^{2t}h_\infty$ is correct in form: with $g_{\theta\theta}\sim e^{2t}$, the mode-$n$ potential enters as $n^2e^{-2t}$. But this potential *decays to zero* as $t\to\infty$, so the leading indicial decay rate at the cusp end is set by the $n$-independent part; the $n^2e^{-2t}$ term suppresses higher modes only transiently at moderate $t$ and does not change the asymptotic rate. The statement "$\theta$-dependent modes decay faster than $n=0$" is therefore true in a finite-$t$/transient sense but is stated as if it improved the asymptotic rate, which it does not. To make "the PDE is more stable than the ODE for higher modes" a result rather than an expectation, one needs the indicial roots of the actual linearized (DeTurck) operator at $t\to\infty$ for each $n$, together with the signs of the zeroth-order coefficients — none of which is in the supplied material. Treat this as a motivated expectation pending that indicial computation.

## What remains unresolved for the construction (scientific substance)

- The exact anisotropic Koiso extension is only shown to *approach* $H=3$ (step70 identity), never reaching it at finite $t$. Whether a genuine exact core exists to $t=\infty$ for a given $R_h=-6$ fiber, or whether an approximate core of defect $\delta$ can be built at length $R\sim\tfrac12\log(6/\delta)$ with the defect systematically arranged (not sign-random), is open. The identity fixes the necessary scaling but does not produce the object.
- The full five-component defect (normal, mixed, tangential) with maximum-norm control has not been solved; only the tangential shape operator is tracked in these ODE reductions.
- Even a complete $\lambda<0$ graph-manifold construction addresses only the $\lambda<0$ direction; the sign-unrestricted problem also requires the $\lambda>0$ direction on the same or a companion topology. This is correctly acknowledged in §5.2/§6 and I confirm it is genuinely outstanding.

## Bottom line for the three results

Result 1 (bound $\ge2/3$): correct; strengthen to $>2/3$ and replace the $c=2/3$ paragraph with the flat-torus chain above. Result 2 (Koiso accelerations, constraint, Hamiltonian relation, isotropic impossibility): all correct, verified independently. Result 3: difference equation correct and exponential decay qualitatively correct; the rate constant $\sqrt3$ conflicts with the three-direction $H\to3$ used in the same tables and should be pinned to one scenario; the $a=0\Rightarrow b_tc_t=0$ sub-result is correct in the ODE reduction; the higher-mode enhancement is transient, not asymptotic, and remains an expectation until an indicial computation of the linearized operator is supplied.