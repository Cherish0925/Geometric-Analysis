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

# Scientific verification memo

## Overall assessment

| Item | Mathematical status |
|---|---|
| Preissmann estimate | Correct; in fact the argument gives a strict \(>2/3\) inequality. The scalar-curvature sentence at \(c=2/3\) is not justified as written. |
| Koiso center identities | Correct with the stated shape-operator convention. The proposed Riccati data do not yet establish metrics on \(T^3\), because one additional period condition is absent. |
| ODE difference identity | Correct algebraically. The \(\operatorname{sech}(\sqrt3\,t)\) profile does not follow from the displayed ODE and is incompatible with its trace equation. |
| \(a\equiv0\) reduction | It does not imply \(b_t c_t=0\) in the full \(T^2\)-invariant Einstein system. The actual algebraic relation is \(b_t c_t+b_\theta c_\theta=0\). |
| Higher Fourier modes | The principal term alone does not establish faster asymptotic decay. After Fourier decomposition it produces both increasing and decreasing branches, while its coefficient tends to zero toward the cusp. |

---

## 1. Preissmann estimate

Set
\[
D(h)=\max_{T^3}\lvert \operatorname{Ric}_h+2h\rvert_{\mathrm{op}}.
\]
If \(D(h)\le 2/3\), every Ricci eigenvalue satisfies
\[
-\frac83\le r_i\le-\frac43.
\]
In a Ricci eigenframe,
\[
K_{ij}=\frac{r_i+r_j-r_k}{2}
\le \frac{-4/3-4/3+8/3}{2}=0.
\]
In dimension three the curvature operator on \(\Lambda^2\) has these three eigenvalues, so every sectional curvature is \(\le0\).

The flat torus theorem then makes \(h\) flat. But for a flat metric,
\[
D(h)=\lvert 0+2I\rvert_{\mathrm{op}}=2,
\]
contradicting \(D(h)\le2/3\). Consequently,
\[
\boxed{D(h)>\frac23}
\]
for every metric on \(T^3\). Thus the stated weaker inequality \(D(h)\ge2/3\) is valid.

The sentence assigning the eigenvalue triple
\[
\left(-\frac43,-\frac43,-\frac83\right)
\]
and hence \(R_h=-16/3\) at \(c=2/3\) does not follow. That triple is only one equality configuration for one sectional plane. The clean contradiction is instead “\(K\le0\) implies flat, while flatness is incompatible with the Ricci interval.” Equivalently, the interval itself gives \(R_h\le-4\), contradicting flatness.

Preissmann alone already proves \(D(h)\ge2/3\) by excluding \(D(h)<2/3\). The flat torus theorem excludes equality. The supplied material does not show that \(2/3\) is the infimum over all metrics on \(T^3\); it is the sharp algebraic threshold for this Ricci-eigenvalue argument.

---

## 2. Koiso center formulas

Use
\[
S=\frac12h_t^{-1}\partial_t h_t,\qquad H=\operatorname{tr}S.
\]
For \(g=dt^2+h_t\),
\[
\operatorname{Ric}_{00}=-H'-|S|^2,
\]
and, as tangential endomorphisms,
\[
\operatorname{Ric}_g^\sharp
=\operatorname{Ric}_{h_t}^\sharp-S'-HS.
\]
At a reflection center \(S(0)=0\), imposing \(\operatorname{Ric}_g=-3g\) gives
\[
\operatorname{tr}S'(0)=3,
\qquad
S'(0)=\operatorname{Ric}_h^\sharp+3I.
\]
Taking the trace of the second equation yields
\[
3=R_h+9,
\qquad
\boxed{R_h=-6}.
\]
These identities are correct. If \(S'=I\), then
\[
\operatorname{Ric}_h=-2h.
\]
In dimension three this gives sectional curvature \(-1\), which is impossible on \(T^3\) by Preissmann.

### The \(T^2\)-invariant acceleration formulas

For
\[
h=d\theta^2+e^{2b_0(\theta)}dx^2+e^{2c_0(\theta)}dy^2,
\qquad
u=b_0',\quad v=c_0',
\]
the Ricci eigenvalues are
\[
\begin{aligned}
r_\theta&=-(u'+v'+u^2+v^2),\\
r_x&=-(u'+u^2+uv),\\
r_y&=-(v'+v^2+uv).
\end{aligned}
\]
Hence
\[
R_h=-2(u^2+v^2+uv+u'+v').
\]
Under \(R_h=-6\),
\[
u^2+v^2+uv+u'+v'=3.
\]
Since the shape eigenvalues are \(a_t,b_t,c_t\), their derivatives at the center are \(a_{tt},b_{tt},c_{tt}\). Therefore
\[
\begin{aligned}
a_{tt}(0)&=r_\theta+3=uv,\\
b_{tt}(0)&=r_x+3=v^2+v',\\
c_{tt}(0)&=r_y+3=u^2+u'.
\end{aligned}
\]
Thus formula (3.3) is correct.

### Missing period condition in the numerical fibers

For these functions to define a metric on \(T^3\), one needs
\[
\int_0^{2\pi}u(\theta)\,d\theta=0,
\qquad
\int_0^{2\pi}v(\theta)\,d\theta=0.
\]
The choice \(v=B\sin\theta\) satisfies the second equation. A periodic solution \(u\) of the Riccati equation does **not** automatically satisfy the first: periodicity of \(u=b_0'\) is weaker than periodicity of \(b_0\).

`step73_koiso_center_analysis.json` records \(u(0)\), curvature residuals, and acceleration traces, but not \(\int u\,d\theta\). Therefore the artifact verifies the local curvature algebra but does not yet verify that the listed \(b_0\) descends to \(S^1\). A nonzero shift in \(b_0\) after one turn cannot be absorbed into the product \(T^3\) coordinates.

The center calculation also controls only the second jet of \(h_t\) and the Einstein tensor on the center slice. The supplied material contains no smooth elliptic extension result from these data.

---

## 3. ODE anisotropy equation and decay rate

For
\[
s_i=f_i',\qquad s_i'+Hs_i=3,\qquad H=s_1+s_2+s_3,
\]
subtraction gives exactly
\[
\delta_{ij}'+H\delta_{ij}=0,
\qquad
\delta_{ij}(t)=\delta_{ij}(0)
\exp\!\left(-\int_0^tH(\tau)\,d\tau\right).
\]
So equation (4.2) is correct.

The subsequent \(\operatorname{sech}(\sqrt3\,t)\) formula is not a consequence of this system. Summing the three equations gives
\[
H'+H^2=9.
\]
With \(H(0)=0\),
\[
H(t)=3\tanh(3t),
\]
and hence
\[
\exp\!\left(-\int_0^tH\right)=\operatorname{sech}(3t).
\]
Thus the homogeneous decay associated with the displayed ODE is
\[
\boxed{\delta_{ij}(t)=\delta_{ij}(0)\operatorname{sech}(3t)},
\]
not \(\operatorname{sech}(\sqrt3\,t)\).

There is a deeper incompatibility with the Koiso center. At a reflection center,
\[
s_i(0)=0,
\]
so \(\delta_{ij}(0)=0\), and this homogeneous ODE remains isotropic. Moreover, it forces
\[
s_i'(0)=3
\]
for every \(i\), whereas the Koiso values are \(s_i'(0)=r_i(h)+3\), generally unequal.

The full tangential Einstein equation is
\[
s_i'+Hs_i=3+r_i(h_t),
\]
so the correct difference equation is
\[
\boxed{\delta_{ij}'+H\delta_{ij}=r_i(h_t)-r_j(h_t)}.
\]
Its Duhamel formula is
\[
\delta_{ij}(t)=e^{-\int_0^tH}
\left[
\delta_{ij}(0)+
\int_0^t e^{\int_0^\tau H}
\bigl(r_i(h_\tau)-r_j(h_\tau)\bigr)\,d\tau
\right].
\]
The intrinsic Ricci anisotropy creates the Koiso acceleration and also determines the eventual decay rate. Dropping it removes precisely the mechanism under study.

The \(\sqrt3\tanh(\sqrt3 t)\) profile solves \(H'=3-H^2\), which belongs to the rank-one \(a\equiv0\) reduction, not the three-direction ODE above. For an exact isotropic solution of the normal equation,
\[
H'+|S|^2=3,\qquad S=\frac H3I,
\]
one instead obtains \(H=3\tanh t\). These three profiles should not be interchanged.

---

## 4. The \(a\equiv0\) ansatz

Let
\[
p=b_t,\quad q=c_t,\quad u=b_\theta,\quad v=c_\theta.
\]
For
\[
g=dt^2+d\theta^2+e^{2b(t,\theta)}dx^2+e^{2c(t,\theta)}dy^2,
\]
the equations \(\operatorname{Ric}=-3g\) include
\[
\begin{aligned}
p_t+q_t+p^2+q^2&=3,\\
u_\theta+v_\theta+u^2+v^2&=3,\\
p_\theta+q_\theta+pu+qv&=0,\\
p_t+u_\theta+p^2+u^2+pq+uv&=3,\\
q_t+v_\theta+q^2+v^2+pq+uv&=3.
\end{aligned}
\]
Adding the last two and subtracting the first two yields
\[
\boxed{pq+uv=0},
\]
or
\[
\boxed{b_t c_t=-b_\theta c_\theta}.
\]
There is no general implication \(b_t c_t=0\).

A local exact example makes this explicit. Choose constants \(p,q\) with
\[
p^2+q^2=3
\]
and set
\[
b=pt-q\theta,\qquad c=qt+p\theta.
\]
Then all five equations above hold and \(\operatorname{Ric}=-3g\), while \(b_tc_t=pq\) can be nonzero. This example is not periodic in \(\theta\), but it proves that the asserted product identity is not a local consequence of the Einstein equations. No global periodic argument establishing it appears in the supplied note.

Also, \(a\equiv0\) throughout the collar is a restrictive metric ansatz, not merely a coordinate choice compatible with Gaussian coordinates. At the center it forces \(a_{tt}=0\), while the Koiso formula gives \(a_{tt}=uv\). Thus Koiso fibers with \(uv\ne0\) necessarily leave the \(a\equiv0\) ansatz.

---

## 5. Higher Fourier modes

The scalar principal part is
\[
\partial_{tt}+e^{-2a}\partial_{\theta\theta}.
\]
For a mode \(y_n(t)e^{in\theta}\), it becomes
\[
y_n''-n^2e^{-2a(t)}y_n.
\]
Two points prevent the proposed inference:

1. Near a region where \(a\) is approximately constant, the toy equation
   \[
   y_n''-n^2y_n=0
   \]
   has both \(e^{|n|t}\) and \(e^{-|n|t}\) branches. Treating \(t\) as evolution therefore produces stronger elliptic Cauchy instability at high frequency, not automatic decay.

2. If \(a(t)\sim t\), then
   \[
   n^2e^{-2a(t)}\sim n^2e^{-2t}\longrightarrow0.
   \]
   Consequently fixed Fourier modes have the same leading indicial exponents at the cusp; \(n\) enters only in lower-order asymptotic corrections. For example,
   \[
   y_n''+\alpha y_n'-n^2e^{-2t}y_n=0
   \]
   has leading exponents \(0\) and \(-\alpha\), independent of \(n\).

On a finite interval with two-ended Dirichlet data, the \(n^2e^{-2a}\) term may improve a scalar coercive energy estimate. That is distinct from faster asymptotic \(t\)-decay, and the coupled Einstein–DeTurck tensor operator requires its full linearization, gauge terms, end conditions, and indicial spectrum.

## Direct answers

- **(a)** Yes, the Preissmann estimate is correct; the endpoint argument should use flatness versus the Ricci interval, not the fixed triple with scalar \(-16/3\).
- **(b)** Yes, formulas (3.3) are correct. The numerical Riccati data still need \(\int u=0\) to define metrics on \(T^3\).
- **(c)** The difference identity is correct. The stated \(\sqrt3\) rate is not; the displayed ODE gives a \(3\)-rate, and the full equation contains intrinsic-Ricci forcing.
- **(d)** No. The full equations give \(b_tc_t+b_\theta c_\theta=0\), not \(b_tc_t=0\).
- **(e)** No. The Fourier principal term alone does not establish faster decay; its coefficient vanishes toward the cusp and it produces both elliptic branches.