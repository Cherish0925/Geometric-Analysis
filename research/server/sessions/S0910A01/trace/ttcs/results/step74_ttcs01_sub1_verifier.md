# TTCS Independent Branch Record

```json
{
  "step_id": 74,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step74_graph_center_and_positive_flux_rebalance.md",
    "Sessions/S0910A01/workspace/data/step74_torus_yamabe_center.json",
    "Sessions/S0910A01/workspace/scripts/step74_torus_yamabe_center.py",
    "Sessions/S0910A02/workspace/notes/step73_global_positive_proof_allocation.md",
    "Skills/qiushi-yau26/references/research/20260912.tex",
    "Sessions/S0910A01/workspace/notes/step73_preissmann_koiso_anisotropy.md"
  ]
}
```

## Task

Verify the Step 74 route correction for the Yau--26 research. Read the Step74 note and supporting data, together with A02's positive-branch allocation and the 20260912 manuscript source. Check two load-bearing mathematical points: (1) the graph-neck repair: does the construction h0=dtheta^2+e^{2f}dx^2+e^{-2f}dy^2 with negative Yamabe normalization really give analytic T^2-invariant scalar -6 torus metrics suitable as Koiso center data S(0)=0, S'(0)=Ric_h^#+3I, and what assumptions or caveats remain? (2) the positive flux scale critique: does FND:flux / constant-scalar refinement only give a c/L lower bound, so that nonzero obstruction coefficient is compatible with delta->0 along L->infty unless an additional sequence-scale mechanism is proved? Compare with the manuscript's |log a| delta_+ -> 1/6 construction. Please identify any mathematical errors, missing hypotheses, or sharper next theorem statement that would materially improve the research direction.

## Output

# Scientific verification memo

## 1. Yamabe–Koiso graph-neck repair

### 1.1 Scalar curvature and Yamabe normalization

For
\[
h_0=d\theta^2+e^{2f(\theta)}dx^2+e^{-2f(\theta)}dy^2,
\]
the general formula for
\[
ds^2+e^{2b(s)}dx^2+e^{2c(s)}dy^2
\]
is
\[
R=-2(b''+c'')-2\bigl((b')^2+(c')^2+b'c'\bigr).
\]
Taking \(b=f,\ c=-f\) gives
\[
R(h_0)=-2(f')^2.
\]
Also \(d\mu_{h_0}=d\theta\,dx\,dy\). Hence, for nonconstant periodic \(f\),
\[
\int_{T^3}R(h_0)\,d\mu_{h_0}<0.
\]
Testing the Yamabe functional with the constant function shows \(Y([h_0])<0\). The Yamabe theorem therefore gives a positive conformal factor, and a constant rescaling fixes the scalar curvature to \(-6\).

For \(h=\psi^4h_0\), the three-dimensional conformal formula is
\[
R_h=\psi^{-5}\bigl(-8\Delta_{h_0}\psi+R(h_0)\psi\bigr).
\]
The \(T^2\)-translations in \(x,y\) preserve \(h_0\). A conformal metric of fixed scalar curvature \(-6\) is unique in a conformal class with Yamabe constant \(<0\): if \(u^4h\) also has scalar \(-6\), then
\[
-8\Delta_hu=6u(1-u^4),
\]
and the maximum principle gives \(u\equiv1\). Translation invariance therefore forces \(\psi=\psi(\theta)\), yielding
\[
-8\psi''-2(f')^2\psi=-6\psi^5,\qquad \psi>0.
\]
For analytic \(f\), this analytic ODE makes \(\psi\) analytic.

Thus the main Yamabe construction is correct. It also directly repairs the earlier zero-mean problem: with
\[
ds=\psi^2d\theta,\qquad
b=2\log\psi+f,\qquad c=2\log\psi-f,
\]
both \(b\) and \(c\) are periodic functions of the arclength coordinate on a circle of circumference
\[
\ell=\int\psi^2\,d\theta.
\]

This construction is already supported by the 20260912 manuscript’s analytic-collar section. There the \(f=\sin\theta\) model is normalized to scalar \(-2\) and produces a local metric with \(\operatorname{Ric}=-g\). Multiplying that four-metric by \(1/3\) gives \(\operatorname{Ric}=-3g\) and center scalar \(-6\), exactly the Step 74 normalization.

### 1.2 Koiso constraints

Using
\[
S=\frac12h_t^{-1}\partial_th_t,\qquad H=\operatorname{tr}S,
\]
the Gaussian formulas are
\[
\operatorname{Ric}_{00}=-\operatorname{tr}S'-|S|^2,
\]
and
\[
(\operatorname{Ric}_{\tan})^\sharp
=\operatorname{Ric}_{h_t}^{\sharp}-S'-HS.
\]
At a totally geodesic center \(S(0)=0\), the equation
\(\operatorname{Ric}_g=-3g\) gives
\[
\operatorname{tr}S'(0)=3,\qquad
S'(0)=\operatorname{Ric}_h^\sharp+3I.
\]
Taking the trace gives
\[
\operatorname{tr}S'(0)=R_h+9,
\]
so consistency is exactly \(R_h=-6\). The momentum constraint
\[
\operatorname{div}S-dH=0
\]
is automatic when \(S=0\).

Hence \((h,S=0)\) is valid analytic Einstein Cauchy data. Strictly speaking, \(S'(0)\) is not an independently prescribed datum; it is the second-order quantity determined by the tangential Einstein equation. The analytic Koiso theorem cited in the manuscript supplies a local even Einstein collar.

### 1.3 What remains unproved on the graph side

The center construction provides local exact geometry, but not:

- continuation to arbitrarily large \(t\);
- convergence of \(S(t)\) to \(I\);
- convergence of \(e^{-2t}h_t\) to a flat marked torus;
- decay of the fiber Ricci differences at rate \(e^{-2t}\);
- a compact graph-manifold assembly with small full operator Ricci residual.

The torus circumference \(\ell\) is also a genuine geometric modulus when matching to a marked cusp lattice. Rewriting the circle with coordinate period \(2\pi\) changes the \(ds^2\) coefficient to \((\ell/2\pi)^2\); a coordinate relabeling does not erase relative lattice scales.

For an Einstein–DeTurck computation, solving
\[
\operatorname{Ric}+3g+\mathcal L_Wg=0
\]
is not by itself an Einstein solution. Endpoint conditions and the equation satisfied by \(W\) must force \(W=0\), or the actual tensor \(\operatorname{Ric}+3g\) must be measured directly. Mixed \(t\theta\) components are essential.

### 1.4 Numerical artifact

The numerical values are plausible and agree with the analytic formulas, but two code details need correction.

1. In `step74_torus_yamabe_center.py`,
   ```python
   ddpsi_ode = 0.75*psi**5 - 0.25*fp(theta)**2*psi
   residual = -8*ddpsi_ode - 2*fp(theta)**2*psi + 6*psi**5
   ```
   makes `ode_residual_sup_using_rhs` algebraically zero. The reported \(1.1\times10^{-16}\) is therefore not an independent numerical residual. The FFT residual \(1.5\times10^{-5}\) and the scalar spread near \(-6\) are the meaningful cross-discretization comparisons.

2. `np.trapezoid(psi**2, theta)` is applied to an endpoint-free periodic grid, omitting the last periodic interval. The periodic trapezoidal sum should be
   \[
   \frac{2\pi}{n}\sum_j\psi_j^2.
   \]
   From the recorded extrema, the discrete circumference should increase by approximately \(1.19\)–\(1.33\times10^{-3}\), giving about \(2.5788\), rather than \(2.57753\). This has no effect on the analytic construction.

A mesh-refinement table and a collocation residual computed from the spline derivative would strengthen the numerical record, though existence already follows analytically.

---

## 2. Annular flux scaling

The Step 74 scale critique is correct.

If the endpoint jump is \(\kappa K\), Proposition `FND:flux` gives
\[
\int_A\langle D\operatorname{Ric}_e u,o\rangle
=-\kappa\,\frac{d+2}{2}I_K,
\qquad
\int_A\|o\|_*\,dV=LJ_K.
\]
Therefore
\[
\|D\operatorname{Ric}_eu\|_{\mathrm{op},\infty}
\ge
\frac{(d+2)I_K}{2J_K}\frac{|\kappa|}{L}.
\]
The nonlinear formulas `FND:nonlinearflux` and `FND:energyflux` preserve the same leading \(1/L\) behavior after endpoint and weighted-energy terms are included.

For the constant-scalar spherical \(A_1\) model, the manuscript strengthens the coefficient to
\[
\delta_+\ge \frac{1}{6L}+o(L^{-1}).
\]
Its explicit family satisfies
\[
s_{\widehat g_a}=4,\qquad
|\log a|\,\delta_+(\widehat g_a)\longrightarrow\frac16.
\]
With the stated choices
\[
T=|\log a|,\qquad b=aT,\qquad R=T^{-1},
\]
the logarithmic length is
\[
L=\log\frac{R}{b}=T-2\log T,
\]
so \(L/T\to1\) and consequently
\[
L\,\delta_+(\widehat g_a)\longrightarrow\frac16.
\]
Thus the local flux estimate is asymptotically sharp. A fixed nonzero quadratic coefficient is fully compatible with \(\delta_+\to0\) when the transition is spread across \(L\to\infty\).

These examples do not settle \(P_n^+\), because the manuscript supplies no theorem excluding every Einstein metric on their underlying smooth manifolds. They do settle the analytic scale question: local flux alone cannot produce a dimension-only positive lower bound for \(\delta_+\).

### Fixed-rescaled annuli need an additional tightness hypothesis

The Step 74 phrase about taking \(\delta_i\to0\) on each fixed rescaled annulus and then \(R\to\infty\) is not sufficient by itself. The model
\[
\eta_i(t)=\frac{t}{L_i},\qquad 0\le t\le L_i,
\]
has total coefficient jump one and residual size \(O(L_i^{-1})\), while its variation on every fixed-length \(t\)-interval tends to zero. Taking the sequence limit first loses the transition, which escapes across diverging logarithmic scales.

Such an extraction becomes effective only if it also retains one of the following:

- the full coefficient transition inside a uniformly bounded logarithmic interval;
- weighted residual mass tending to zero over the entire neck;
- \(\delta_iL_i\to0\);
- a global transport, monotonicity, or coercive identity that forbids slow drift across scale.

A controlled-length annulus is useful only when it carries a fixed portion of the endpoint coefficient jump.

---

## 3. Sharper theorem formulations

### 3.1 Sequence-level flux theorem

The natural quantity is the weighted residual mass
\[
\mathfrak R_i
=\int_{A_i}
\|\operatorname{Ric}_{g_i}-\sigma g_i\|_{\mathrm{op}}
\,\|o_i\|_*\,dV_{g_i}.
\]
After harmonic/Bianchi gauge, endpoint expansion, and nonlinear remainder control, the desired statement has the form
\[
\frac{d+2}{2}I_K|\kappa_i|
\le
\mathfrak R_i
+C_K\bigl(\epsilon_i+\mathcal E_i+R_i\sqrt{\mathcal E_i}+R_i^2\bigr).
\]
The supremum estimate only gives
\[
\mathfrak R_i\le J_K\,\delta_iL_i+o(1).
\]
Thus coefficient disappearance follows from \(\mathfrak R_i\to0\), not merely from \(\delta_i\to0\). In the constant-scalar \(A_1\) normalization this reduces asymptotically to
\[
|\kappa_i|\le 6\,\delta_iL_i+o(1),
\]
and the manuscript family saturates it with \(\kappa_i=1\).

For higher homogeneous degree \(\ell\), the proposed dual
\[
o_\ell=r^{-(d-2)-2\ell}K_\ell
\]
does give the expected Wronskian coefficient
\((d+2\ell-2)/2\). Its weighted \(L^1\) mass, however, scales as
\[
\int_b^R r^{1-\ell}\,dr,
\]
so only \(\ell=2\) is logarithmically critical. Higher-mode statements require an explicit normalization of the coefficient at a chosen scale; they do not resolve the quadratic slow-drift phenomenon.

### 3.2 Graph continuation statement

A graph-side result that would connect the valid center data to the intended construction would assert the existence of \(R_j\to\infty\) and \(T^2\)-invariant metrics
\[
g_j=dt^2+h_{j,t}\quad\text{on }[0,R_j]\times T^3
\]
such that

\[
S_j(0)=0,\qquad R_{h_{j,0}}=-6,
\]
\[
\|\operatorname{Ric}_{g_j}+3g_j\|_{\mathrm{op},\infty}\to0,
\]
and, at the outer endpoint,
\[
\|S_j(R_j)-I\|_{C^1}
+\|e^{-2R_j}h_{j,R_j}-h_{\mathrm{flat},j}\|_{C^2}\to0,
\]
with compatible marked flat lattices. All normal, tangential, and mixed Ricci components must enter the estimate. Such a result would turn the Yamabe center from valid local data into a usable graph half-core.

## Overall finding

The two principal Step 74 corrections are mathematically sound:

1. the Yamabe construction genuinely supplies analytic diagonal \(T^2\)-invariant scalar-\(-6\) torus data satisfying the Koiso constraints and giving a local exact \(\operatorname{Ric}=-3g\) collar;
2. the annular flux mechanism is intrinsically inverse-logarithmic in the quadratic mode, and the manuscript’s constant-scalar family realizes the sharp product \(L\delta_+\to1/6\).

The principal refinement is that fixed-scale extraction alone does not remove logarithmic drift. The missing positive-side substance is a global sequence theorem controlling weighted residual mass or concentrating the coefficient transition into bounded logarithmic length.