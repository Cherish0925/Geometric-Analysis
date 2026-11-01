# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step10_multiscale_cover_and_diffuse_pontryagin.tex",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex"
  ]
}
```

## Task

Consider a closed oriented Einstein 4-manifold (M, g) with Ric = -g that is collapsing with circle fibers of length function ℓ. The self-dual Weyl operator in the static circle reduction is W+ = 2J(h - I/3) where h = Hess(ℓ)/ℓ, plus twist corrections that are O(ℓ²|F|²) where F = dA is the connection curvature. The calibrated spectrum (-1/6, 1/12, 1/12) requires h eigenvalues (3/8, 3/8, 1/4) in the static case, but the ONLY constant-eigenvalue static Einstein circle metric has h = I/3 (i.e., W+ = 0). This is the static incompatibility.

Near a smooth NUT (ℓ → 0), twist corrections vanish as O(ℓ²), so the static formula dominates: W+ → 2J(h - I/3) with h constrained to the isotropic value by Einstein. This means the calibrated anisotropy cannot persist into the NUT core.

Develop a rigorous argument connecting this anisotropy constraint to fiber survival at a fixed buffer scale on the calibrated good set. Specifically:

1. For a good point p (bounded curvature mean at all scales ≤ 1, small calibrated deficit), can the fiber length ℓ(p) be arbitrarily small? The Riemann tensor in the e_a ∧ e_4 directions contains h_{ab} = Hess(ℓ)_{ab}/ℓ, which diverges if ℓ → 0 with |∇ℓ| bounded. Use the curvature mean bound to derive a lower bound on ℓ(p) at good points.

2. If ℓ(p) ≥ ℓ₀ > 0, then the fiber survives in a ball B_R(p) of fixed radius (from the slow variation of ℓ implied by the curvature bound). This gives a buffer-scale covering chart, which transports the calibrated deficit and produces the forbidden Einstein germ.

3. Alternatively, if ℓ(p) can be small at a good point, show that the static incompatibility forces a positive calibrated deficit or excessive curvature on B_R(p), using the fact that calibrated W+ requires substantial twist energy (O(ℓ²|F|²) ≥ c), while the total twist energy is controlled by the topology.

The scientific product should be a clear mechanism connecting the W+ anisotropy, the circle-reduction Hessian, and fiber survival, leading to a conditional or unconditional exclusion of circle-collapse on the calibrated good set.

## Output

A rigorous circle-collapse argument should be phrased in terms of **fiber survival radius**, not absolute fiber length.  The length \(\ell(p)\) can be arbitrarily small in a regular free circle-collapse region with bounded curvature; what matters is whether the circle contracts inside the chosen buffer.  The anisotropy mechanism separates three cases: surviving fiber, low-twist contraction, and high-twist contraction.

## 1. Reduction variables and what curvature actually controls

On a regular circle region write
\[
g=q+\ell^2\theta^2,\qquad \theta=d\psi+A,\qquad F=dA,
\]
with horizontal indices \(a,b=1,2,3\), unit vertical one-form \(\eta=\ell\theta\), and
\[
h_{ab}=\ell^{-1}\nabla_a\nabla_b\ell,\qquad
Z_{ab}=\ell F_{ab},\qquad \tau=|Z|^2=\ell^2|F|^2 .
\]
For the usual Kaluza–Klein convention,
\[
R_{a4b4}=-h_{ab}+\frac14 Z_{ac}Z_b{}^c,
\]
and the Einstein equation \(\operatorname{Ric}_g=-g\) gives
\[
\operatorname{tr}h=1+\frac14\tau,\qquad
\nabla^b(\ell^3F_{ab})=0,
\]
with horizontal Ricci determined by \(h\) and \(Z\).  The self-dual Weyl operator has the schematic form
\[
W^+=2J\Bigl(h-\frac13I\Bigr)+Q(Z),
\qquad |Q(Z)|\le C\tau,
\]
where \(J\) is the trace-free symmetric \(3\times3\) to \(\Lambda^2_+\) identification, up to the chosen norm convention.

Let
\[
\mathcal W_*=\operatorname{SO}(3)\cdot
\operatorname{diag}\Bigl(-\frac16,\frac1{12},\frac1{12}\Bigr),
\]
and
\[
\mathcal H_*=\operatorname{SO}(3)\cdot
\operatorname{diag}\Bigl(\frac38,\frac38,\frac14\Bigr).
\]
In the static case \(Z=0\), calibration means \(h\in\mathcal H_*\).  The distance from the isotropic value is definite:
\[
\left|
\operatorname{diag}\Bigl(\frac38,\frac38,\frac14\Bigr)-\frac13I
\right|
=
\left|
\operatorname{diag}\Bigl(\frac1{24},\frac1{24},-\frac1{12}\Bigr)
\right|
=\frac1{4\sqrt6}.
\]
Thus, pointwise,
\[
\operatorname{dist}(W^+,\mathcal W_*)\le \varepsilon
\quad\Longrightarrow\quad
\operatorname{dist}(h,\mathcal H_*)\le C(\varepsilon+\tau).
\]
So a calibrated small-twist region must carry the static anisotropy
\[
|h-I/3|\ge c_*>0.
\]

## 2. Curvature mean does not by itself bound \(\ell(p)\) below

The implication
\[
\fint_{B_r(p)}|\operatorname{Rm}|^2\le K
\quad\Rightarrow\quad
\ell(p)\ge \ell_0(K)
\]
is not a valid geometric inference.

A local model is hyperbolic space of sectional curvature \(-1/3\),
\[
g_\varepsilon
=
dt^2+e^{2t/\sqrt3}(dx^2+dy^2+\varepsilon^2d\psi^2).
\]
Then \(\operatorname{Ric}=-g_\varepsilon\), the circle length is
\[
\ell_\varepsilon=\varepsilon e^{t/\sqrt3}\to0,
\]
while all curvature components stay fixed.  In the circle reduction,
\[
F=0,\qquad h=\frac13I,\qquad W^+=0.
\]
So bounded curvature controls the scale-invariant quantities \(h\), \(Z=\ell F\), and their derivatives, not the multiplicative size of \(\ell\).

What the Einstein reduction gives instead is Harnack-type control on a regular free circle region.  Since
\[
\Delta_q\ell=\Bigl(1+\frac14\tau\Bigr)\ell,
\]
bounded \(\tau\) and controlled base geometry imply
\[
\sup_{B_{R/2}^q}\ell\le C_H\inf_{B_{R/2}^q}\ell,
\qquad
|\nabla\log\ell|\le C_H/R
\]
under the standard smoothed collapse estimates.  Thus if \(\ell(p)\) is tiny in a regular low-twist free region, it remains tiny nearby; it does not contract to zero inside the buffer.  That is precisely the situation where the circle generator survives and can be unwrapped.

## 3. Fiber survival gives the forbidden calibrated Einstein germ

Let \(a(p)\) denote the largest radius on which the circle fibration over the projected base ball is regular and the fiber loop remains nontrivial in the buffered fundamental group.

If
\[
a(p)\ge R_0>0,
\]
then after choosing the buffer first, the normal cover unwraps the short circle.  Even if \(\ell(p)\to0\), the lifted ball has four-dimensional volume:
\[
\operatorname{Vol}_{\tilde g}B_{cR_0}(\tilde p)\ge v_0R_0^4,
\]
because the base contributes \(R_0^3\) and the unwrapped vertical coordinate contributes a physical interval of length comparable to \(R_0\).

The maximal-function good point hypotheses transport to this cover:
\[
\fint_{B_r(\tilde p)}|\widetilde{\operatorname{Rm}}|^2\le C K,
\qquad
\fint_{B_r(\tilde p)}\widetilde D_{\rm cal}\le C\varepsilon_i\to0,
\qquad r\le cR_0.
\]
Together with \(|\operatorname{Ric}+g|\to0\), harmonic-coordinate compactness gives a smooth Einstein limit on a noncollapsed chart.  The calibrated deficit then forces
\[
\operatorname{Ric}=-g,\qquad
\operatorname{Spec}(W^+)=\Bigl(-\frac16,\frac1{12},\frac1{12}\Bigr).
\]
But the constant-spectrum harmonic-Weyl argument gives \(\nabla W^+=0\), while the Einstein Weyl identity gives
\[
|\nabla W^+|^2=\frac1{16}.
\]
Hence a calibrated good point cannot have a fixed surviving circle buffer.

This proves the key low-cost alternative:

\[
\boxed{
\text{A calibrated circle-collapsed good point must either have no fixed survival buffer,}
\text{ or it produces the forbidden germ.}
}
\]

## 4. What if the fiber contracts inside every fixed buffer?

If the fiber contracts in \(B_{R_0}(p)\), the relevant quantity is not \(\ell(p)\) but the mechanism by which the loop dies.

### Low-twist contraction is incompatible with good-point bounds

Assume \(F\) remains bounded in the quotient metric, so \(\tau=\ell^2|F|^2\to0\).  If \(\ell\) approaches zero at a smooth contraction point, then in the quotient picture \(\ell\sim r\).  Consequently
\[
h=\frac{\nabla^2\ell}{\ell}\sim \frac1{r^2}
\]
in angular base directions.  Since
\[
R_{a4b4}=-h_{ab}+O(\tau),
\]
a low-twist contraction core creates
\[
|R_{a4b4}|^2\sim r^{-4}.
\]
With four-dimensional volume density \(\ell\,d\mu_q\sim r^3dr\), this gives a logarithmic curvature-energy cost:
\[
\int |R_{a4b4}|^2\,d\mu_g\sim\int\frac{dr}{r}.
\]
Thus a regular low-twist contraction core cannot sit inside the centered balls of a maximal-function good point.

Equivalently, in a regular free region with bounded \(\tau\), the equation
\[
\Delta_q\ell=\Bigl(1+\frac14\tau\Bigr)\ell
\]
and Harnack control prevent a positive \(\ell\) from dropping to zero inside a controlled base ball.  Contraction requires either quotient singularity, large \(Z=\ell F\), or curvature concentration.

### Static calibrated anisotropy gives a stronger exclusion

Suppose a sequence of regular circle reductions on fixed base balls satisfies
\[
\tau_i\to0,\qquad
\fint D_{{\rm cal},i}\to0,
\]
with controlled base harmonic radius.  Normalize the fiber length by
\[
\hat\ell_i=\ell_i/\ell_i(x_i).
\]
The static equations are invariant under this multiplication, since \(h=\nabla^2\ell/\ell\).  Elliptic compactness gives a static Einstein limit
\[
g_\infty=q_\infty+\hat\ell_\infty^2d\psi^2,
\qquad F_\infty=0.
\]
The calibrated deficit forces
\[
\operatorname{Spec}(h_\infty)=\Bigl(\frac38,\frac38,\frac14\Bigr)
\]
throughout the limiting ball.  But the static constant-eigenvalue theorem gives only
\[
h_\infty=\frac13I,
\qquad W^+_\infty=0.
\]
Therefore, for every fixed regular reduced geometry class, there are constants \(R,c>0\) such that
\[
\fint_{B_R}\bigl(D_{\rm cal}+\tau^2\bigr)\,d\mu_g\ge c.
\]
So a calibrated good point cannot lie in a low-twist static contraction region.

## 5. High-twist contraction is the only remaining circle mechanism

If \(h\) is forced toward the isotropic static value near a contraction core, but \(W^+\) remains calibrated, then the twist term must supply the anisotropy:
\[
|Q(Z)|\ge \frac1{2\sqrt6}-o(1).
\]
Since \(|Q(Z)|\le C\tau\),
\[
\tau=\ell^2|F|^2\ge c_Q>0
\]
on a definite portion of the region.

This is the precise meaning of “calibrated anisotropy forces twist energy.”  The fiber can contract inside a fixed buffer only if the reduction leaves the static regime through order-one \(Z=\ell F\), quotient singularity, or mixed O’Neill curvature.

A smooth NUT illustrates the point.  The statement “twist corrections vanish like \(O(\ell^2)\)” is accurate only when \(F\) stays bounded in the quotient metric.  At a NUT, the quotient connection curvature typically blows up in the quotient norm; otherwise the singular \(h\sim r^{-2}\) term would remain visible in \(R_{a4b4}\).  Smoothness comes from cancellation between the Hessian term and the twist/O’Neill terms, not from a purely static core.

Thus the calibrated good set has the following structure:

\[
\boxed{
\begin{array}{c}
\text{regular surviving fiber at fixed buffer}
\\
\Downarrow
\\
\text{unwrapped noncollapsed cover}
\\
\Downarrow
\\
\text{forbidden calibrated Einstein germ}
\end{array}}
\]

and

\[
\boxed{
\begin{array}{c}
\text{no fixed survival buffer}
\\
\Downarrow
\\
\text{contraction core inside every fixed buffer}
\\
\Downarrow
\\
\text{either low-twist static singularity, giving curvature/deficit cost,}
\\
\text{or order-one twist/mixed curvature } \tau=\ell^2|F|^2 .
\end{array}}
\]

## 6. Resulting exclusion statement

The anisotropy mechanism gives an unconditional exclusion of **static or low-twist circle collapse** on the calibrated good set:

\[
\boxed{
\text{No calibrated good point can be modeled on a fixed-buffer regular circle reduction}
\text{ with }\tau=\ell^2|F|^2\to0.
}
\]

More quantitatively, on any regular reduced ball with controlled base geometry,
\[
\fint_{B_R}D_{\rm cal}\to0
\quad\text{and}\quad
\fint_{B_R}\tau^2\to0
\]
force a static calibrated Einstein limit, contradicting \(h=I/3\).

The fully general circle-collapse case reduces to a sharper mixed-curvature problem:

\[
\boxed{
\text{Every calibrated good point with no fixed surviving fiber must carry}
\quad
\fint_{B_R}\tau^2\ge c>0
\quad
\text{or comparable mixed O'Neill/Chern--Simons flux.}
}
\]

This high-twist alternative is not a finite-NUT picture.  Because the calibrated Pontryagin density satisfies
\[
\rho_+\approx \frac{3}{16\pi^2}
\]
in \(L^1\), the characteristic mass follows volume.  If circle collapse persists on a positive-volume good set, the twist/mixed curvature must be diffuse through the collapsed bulk, not stored only at isolated contraction cores.

So the clean conclusion is:

- \(\ell(p)\) itself need not have a fixed lower bound.
- If the fiber survives on a fixed buffer, the normal cover produces the forbidden Einstein germ.
- If the fiber does not survive, then low-twist/static contraction is excluded by the Hessian anisotropy and static theorem.
- The only remaining circle-collapse model is diffuse high-twist collapse with order-one \(\ell^2|F|^2\) or equivalent mixed curvature throughout the calibrated good set.