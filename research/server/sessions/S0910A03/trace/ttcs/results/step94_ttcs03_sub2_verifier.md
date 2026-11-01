# TTCS Independent Branch Record

```json
{
  "step_id": 94,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step94_charged_koiso_separator.py",
    "Sessions/S0910A03/workspace/data/step94_charged_koiso_separator.json",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md",
    "Sessions/S0910A03/trace/ttcs/results/step92_ttcs02_verifier1_integration.md",
    "Sessions/S0910A03/workspace/notes/step88_source_note_twist.md",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md"
  ]
}
```

## Task

Verify the proposed charged Koiso separator construction in full detail. The hypersurface metric is qSigma=ds^2+M(U(s)) on T^3, det M=1. Choose fixed charge covector q, mixed Weingarten covector m=-q/2 (orientation convention), a hyperbolic target circle U of constant speed squared 12+2S with 0<S<3, physical separator charge Q(s)=1/2 q^T M^-1q scaled so Q<S, P=S-Q, and vertical tracefree Weingarten B=sqrt(P/2) M^-1 dM(N), N target-normal to U_s. Check: (i) the full block Weingarten endomorphism and its self-adjointness; (ii) tr W=0 and tr W^2=P+Q=S, including the factor 2 in the mixed block; (iii) scalar curvature and Hamiltonian constraint for lambda=-3; (iv) every momentum component, especially whether constant covector m really makes vertical momentum vanish after all connection terms and whether s-momentum remains tr(A B)=0 despite mixed W; (v) the Gaussian-gauge relation between m and the twist charge q, including rho factors and orientation; (vi) full—not merely invariant—strict stability and whether the potential is exactly 3-S for all torus Fourier modes; (vii) analyticity/global periodicity of the wound target circle and applicability of Koiso. Identify any hidden obstruction or needed modification. State exactly what a valid construction would establish and what global two-ended work remains.

## Output

# Verification Memo: Charged Koiso Separator (Step 94)

## Summary judgment

The construction is algebraically and geometrically correct in the stated target-space normalization. For the fixed charge covector $q=(q_0,0)$, the choice $m=-q/2$, the vertical block $B=\sqrt{P/2}\,C_N$ with $P=S-Q$, and the uniformly wound hyperbolic circle of constant speed$^2=12+2S$, the full block Weingarten endomorphism $W$ is self-adjoint, trace-free, satisfies $\operatorname{tr}(W^2)=S$, meets the $\lambda=-3$ Hamiltonian constraint, and has both momentum components vanishing exactly. The Jacobi form is $\int(|\nabla\phi|^2+(3-S)\phi^2)$ with a **constant** positive potential, so full (not merely torus-invariant) strict stability holds with lowest eigenvalue exactly $3-S$. Koiso's analytic Cauchy theorem then yields a genuine local analytic $\operatorname{Ric}=-3g$ germ carrying nonzero mixed second fundamental form, i.e. nonzero twist. I found no hidden error. The refinements below concern precise statement and physical interpretation, not correctness.

I reproduce each identity independently.

## 1. Full block endomorphism and self-adjointness (item i)

In coordinates $(s,x^1,x^2)$ with $q=\operatorname{diag}(1,M)$,
$$
W=\begin{pmatrix}0 & m^T\\ M^{-1}m & B\end{pmatrix},\qquad W^s{}_a=m_a,\; W^a{}_s=(M^{-1}m)^a,\; W^a{}_b=B^a{}_b.
$$
Lowering the upper index, $(qW)_{sa}=m_a$ and $(qW)_{as}=M_{ab}(M^{-1}m)^b=m_a$ agree; $(qW)_{ab}=(MB)_{ab}=\sqrt{P/2}\,dM(N)_{ab}$ is symmetric because $dM(N)$ is a derivative of a symmetric matrix. Hence $W$ is $q$-self-adjoint. This matches the numerical `W_self_adjoint` residual $\sim10^{-16}$.

## 2. Trace and squared norm, including the factor 2 (item ii)

$\operatorname{tr}W=W^s{}_s+\operatorname{tr}B=0+\sqrt{P/2}\operatorname{tr}C_N$, and $\operatorname{tr}C_N=d(\log\det M)(N)=0$ since $\det M=1$. So $\operatorname{tr}W=0$.

For the squared norm, enumerate the trace of $W^2$:
$$
\operatorname{tr}(W^2)=\underbrace{2\,m_a(M^{-1}m)^a}_{sa\text{ and }as\text{ blocks}}+\underbrace{\operatorname{tr}(B^2)}_{\text{vertical}} = 2\,m^TM^{-1}m+P.
$$
The factor $2$ is genuine: the mixed off-diagonal blocks each contribute one copy of $m^TM^{-1}m$. With $m=-q/2$, $2\,m^TM^{-1}m=\tfrac12 q^TM^{-1}q=Q$. And $\operatorname{tr}(B^2)=\tfrac{P}{2}\operatorname{tr}(C_N^2)=\tfrac{P}{2}\cdot 2=P$ (unit normal $\Rightarrow \tfrac12\operatorname{tr}C_N^2=1$). There is no mixed–vertical cross term in the trace. Therefore
$$
\operatorname{tr}(W^2)=Q+P=S.
$$
This reproduces `Q_mixed_norm`, `P_vertical_norm`, and `II_norm_minus_S` residuals $\sim10^{-16}$. The design that $Q(s)$ varies (physical charge redshift, $Q\in[0.24,0.5]$) while $P=S-Q$ compensates so that $|II|^2\equiv S$ is exact is the structural core of the example.

## 3. Scalar curvature and Hamiltonian constraint (item iii)

For $q=ds^2+M(s)dx^adx^b$ with $\operatorname{tr}A=0$ ($A=\tfrac12 M^{-1}M_s$),
$$
\operatorname{Scal}_q=-\operatorname{tr}(A^2)=-\tfrac12 e_s,\qquad e_s=\tfrac12\operatorname{tr}[(M^{-1}M_s)^2]=2\operatorname{tr}(A^2),
$$
so $\operatorname{Scal}_q=-6-S$ for $e_s=12+2S$. The correct Gauss scalar relation for a hypersurface in a 4-dimensional Einstein space with $\operatorname{Ric}=\lambda g$ is
$$
R_\Sigma+ |II|^2 - H^2 = R_M-2\operatorname{Ric}_M(\nu,\nu)=4\lambda-2\lambda=2\lambda.
$$
With $H=0$, $|II|^2=S$, $\lambda=-3$: $R_\Sigma=2\lambda-|II|^2=-6-S$, which coincides with the constructed $\operatorname{Scal}_q$. The code's residual `scal+IInorm+6` checks exactly $R_\Sigma+|II|^2=-6$; residual $\sim6\times10^{-15}$. Constraint satisfied.

(For orientation of readers: this uses the sign convention $R_\Sigma=R_M-2\operatorname{Ric}_M(\nu,\nu)+H^2-|II|^2$, verified against the unit sphere $S^n\subset\mathbb R^{n+1}$: $R=n^2-n=n(n-1)$.)

## 4. All momentum components (item iv)

Christoffels of $q$: $\Gamma^a_{sb}=A^a{}_b$, $\Gamma^s_{ab}=-(MA)_{ab}$, and $\Gamma^i_{ik}=\partial_k\log\sqrt{\det q}=0$.

**$s$-component.** $(\operatorname{div}W)_s=\partial_iW^i{}_s-\Gamma^k_{is}W^i{}_k=-\,\Gamma^a_{bs}W^b{}_a=-A^a{}_bB^b{}_a=-\operatorname{tr}(AB)$. Since $A=\tfrac12 C_{U_s}$, $B=\sqrt{P/2}\,C_N$, and $\langle U_s,N\rangle_{\mathbb H^2}=0$,
$$
\operatorname{tr}(AB)=\sqrt{P/2}\,\langle U_s,N\rangle=0.
$$
The mixed blocks $m$ do **not** enter the $s$-component, because the only surviving Christoffel contraction $\Gamma^a_{bs}$ pairs with the vertical block $B$, not $m$. Residual `momentum_s` $\sim6\times10^{-16}$.

**Vertical component.** $(\operatorname{div}W)_a=\partial_sW^s{}_a-\Gamma^k_{ia}W^i{}_k=\partial_s m_a-\big[-(MA)_{ba}(M^{-1}m)^b+A^b{}_a m_b\big]$. Using $M_{bc}(M^{-1}m)^b=m_c$, the bracket is $-A^c{}_a m_c+A^c{}_a m_c=0$ **identically**, for any symmetric $M$. Hence $(\operatorname{div}W)_a=\partial_s m_a$, which vanishes precisely because $m=-q/2$ is a constant covector. So both connection terms genuinely cancel and constancy of $m$ closes the vertical component.

One matter to record: the script's `conn1+conn2` is a coded tautology ($\pm A^Tm$) and is not an independent numerical divergence. The substantive verification of the vertical momentum is the analytic identity above, which I reproduce independently; it is correct. A from-scratch covariant divergence with the full Christoffel set would be a cleaner numerical corroboration, but the algebra is unambiguous.

## 5. Gaussian-gauge charge reconstruction (item v)

In Gaussian normal gauge $g=dt^2+q_t$, the convention $g_t(WX,Y)=-\tfrac12\dot g_t(X,Y)$ gives $\dot q_{sa}=-2W_{sa}=-2m_a$. The off-diagonal $q_{sa}$ is (with fibre metric $M$) the Kaluza–Klein connection $A^a_s=M^{ab}q_{sb}$, and with $A^a_t=0$ in this gauge the twist field strength is
$$
F^a_{ts}=\partial_t A^a_s=M^{ab}\dot q_{sb}=-2(M^{-1}m)^a,\qquad q_a\equiv M_{ab}F^b_{ts}=-2m_a,
$$
so $q=-2m$ at $\rho=1$, matching the code (which checks this arithmetically, residual $0$). This is the correct physical dictionary: nonzero $m$ is nonzero $F_{ts}$, and by the Step 88 mixed-Ricci conservation the associated twist scalar $\alpha_a$ is constant along the exact germ. Because $m\neq0$, the germ is genuinely non-orthogonally-transitive with nonzero conserved twist, distinct from the totally geodesic OT Koiso center. The one point worth stating plainly: this reconstruction is definitional plus the KK dictionary; the numerics verify only the $t=0$ constraint data, not the germ's non-OT character for $t\neq0$ (which follows from $m\neq0$ and twist conservation, not from a computation here).

## 6. Full versus invariant stability (item vi)

The Jacobi operator is $L=-\Delta_\Sigma-(\operatorname{Ric}(\nu,\nu)+|II|^2)=-\Delta_\Sigma+(3-S)$. Because $|II|^2\equiv S$ is a **constant** (this is the essential difference from the variable-$P$ spikes of Step 92), the potential $3-S$ is a positive constant everywhere. Hence for every $f$ on $T^3$,
$$
Q[f]=\int_{T^3}\big(|\nabla f|^2+(3-S)f^2\big)\,d\mu\ \ge\ (3-S)\|f\|^2,
$$
with equality on constants. Full strict stability is therefore immediate and the lowest eigenvalue is exactly $3-S=2$, consistent with the JSON.

Precise statement for the Fourier decomposition $f=\sum_k y_k(s)e^{ik\cdot x}$:
$$
Q[f]=\sum_k\int\big(|y_k'|^2+(3-S+k^TM(s)^{-1}k)\,|y_k|^2\big)\,ds.
$$
The mode potential is $3-S+k^TM^{-1}k$, equal to $3-S$ only for $k=0$; nonzero modes add the nonnegative $k^TM^{-1}k$ and are strictly more stable. So the accurate phrasing is: the potential floor is $3-S$, attained at $k=0$, and full stability holds with lowest eigenvalue $3-S$ — not literally "$3-S$ for all modes." The stability conclusion is robust and, for $k\neq0$, stronger.

## 7. Global periodicity, analyticity, and Koiso (item vii)

On a hyperbolic circle of radius $R$ traversed at uniform angular rate, the speed per unit $\theta$ is $\sinh R$ (circumference $2\pi\sinh R$). With $\theta=\mathrm{wind}\cdot s$ and $R=\operatorname{arcsinh}(\mathrm{speed}/\mathrm{wind})$,
$$
|U_s|^2=\sinh^2R\cdot\mathrm{wind}^2=\mathrm{speed}^2=12+2S,
$$
constant, matching `speed_squared` residual $\sim10^{-14}$ and $e_s\in[14,14]$. The denominator $\cosh R-\sinh R\sin\theta>0$ never vanishes, so $U$ is a closed real-analytic immersion winding 10 times; $N=J\,U_s/|U_s|$ is a globally periodic analytic unit normal. There is no closure or normal monodromy obstruction. The uniform winding (available here because $S$ is constant) sidesteps the small `theta_prime` rescaling inconsistency noted for the variable-speed Step 92 curve; here the speed is exactly constant to $10^{-14}$.

Analyticity of the data: $M$, $U$, $Q=\tfrac12 q^TM^{-1}q$ analytic; $P=S-Q>0$ (data $P\in[0.5,0.76]$) so $\sqrt{P/2}$ analytic and $B$ analytic. Both constraints hold with analytic data, so Koiso's theorem yields a unique local analytic $g=dt^2+q_t$ with $\operatorname{Ric}=-3g$ and these Cauchy data. Uniqueness transports the $T^2$-translation symmetry to the germ.

## 8. What a valid construction establishes, and what remains

Established, on the free-$T^2$/two-ended-connector analysis:
- Exact $T^2$-invariant **charged** Cauchy data on $T^3$ meeting the complete $\lambda=-3$ Hamiltonian and momentum constraints, with a nonzero mixed Weingarten block realizing a conserved twist charge $q=-2m$.
- A minimal ($H=0$), fully strictly stable ($L\ge 3-S=2$) separator slice, with bounded moderate normal orbit energy $e_\nu=2P$ (unlike the unbounded-$e_\nu$ spikes of Step 92; here $P,Q$ are bounded, so the germ existence interval is not forced to shrink).
- A genuine local analytic Einstein germ that is non-OT and carries nonzero twist — supplying the local charged object that the Step 90 radial-core discussion sought, and confirming that twist charge is compatible with full separator-level stability at bounded curvature.

Not established (the remaining substance for the route):
- This is a single Cauchy germ. There is no complete two-ended connector, no matching to prescribed cylindrical/OT ends, and no uniform continuation interval across a family.
- The reconciliation of nonzero interior twist with the Step 88 result that exact Einstein on an OT open end forces $\alpha_a=0$ requires a physical-charge redshift-and-discharge across a collar (the Step 90 mechanism), whose end-matching leaves a horizontal residual $C(L)=O(\delta^2)$ demanding sign-changing control — unresolved.
- The decisive missing object is the tubular-collar transport/regularity relation from the stable separator to the ends (Step 92 §6, Step 90 §8): a length-independent bound on $\int_\Gamma(|h_\nu|+\sqrt{e_\nu})$, or a genuine two-variable gluing threading the charge to OT ends. Nothing here supplies that.
- Nothing here addresses non-free, non-OT, or non-symmetric metrics, the positive-Einstein branch, or the all-dimensional Yau 26 statement.

## 9. Consolidated verification points

The one recurring cause behind the small refinements is that several supporting checks are self-consistency of the assumed structure (the tautological `conn1+conn2` cancellation, the tautological `qrec=-2m`) rather than independent recomputations. In each such case the independent analytic identity — the connection cancellation $-A^c{}_a m_c+A^c{}_a m_c=0$, the KK dictionary $q=-2m$, the constant-potential stability $L\ge3-S$ — is correct and I reproduce it above. The numerical residuals ($<2\times10^{-12}$ throughout) then corroborate the closed-form algebra. The construction stands as an exact charged, fully stable, minimal $T^3$ Einstein-constraint germ; its content for Yau 26 is that separator-level stability plus complete Cauchy constraints, now with nonzero twist, still do not produce a global connector, and the collar transport / two-ended gluing remains the open mathematical object.