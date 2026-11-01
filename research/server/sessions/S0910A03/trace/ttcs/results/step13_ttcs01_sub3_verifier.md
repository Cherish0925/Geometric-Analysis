# TTCS Independent Branch Record

```json
{
  "step_id": 13,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/verify_einstein_defect_evolution.py",
    "Sessions/S0910A03/workspace/notes/step12_reduced_equations_accessibility.md"
  ]
}
```

## Task

Verify the following claim about the Einstein defect evolution under normalized Ricci flow. For the flow d/dt g = -2(Ric + g), define E = Ric(g) + g. The claim is: d/dt E = Delta_L E - 2E, where Delta_L is the Lichnerowicz Laplacian. Furthermore, the squared norm satisfies (d/dt - Delta)|E|^2 = -2|nabla E|^2 + 4 R_{ikjl} E_{ij} E_{kl}. The derivation uses: (1) contracted Bianchi identity div(E) = (1/2) d(tr E) to cancel the Hessian-of-trace terms in the variation formula; (2) substitution R_{ik} = E_{ik} - g_{ik} to cancel tr(E^3) and |E|^2 terms in the |E|^2 evolution. Check each step for correctness. Then assess the consequence: under Ye Li's smoothing (which gives |Rm(g(t))| <= C/t for t in (0, T)), the Gronwall estimate for sup|E(t)|^2 gives a growth factor exp(int_0^{t_0} 4C/t dt) = exp(4C log(t_0/0)) = infinity, so the Einstein defect is NOT controlled pointwise through the flow. Is this analysis correct? Are there alternative estimates (using integral norms, parabolic regularity, or the -2E damping term) that could circumvent this gap?

## Output

## Scientific memo

### 1. Tensor evolution

Use the conventions
\[
\Delta=\nabla^k\nabla_k,\qquad
(\Delta_L h)_{ij}
=\Delta h_{ij}+2R_{ikjl}h_{kl}
-R_i{}^k h_{kj}-R_j{}^k h_{ki}.
\]
For \(v=\partial_tg\), the Ricci variation formula is
\[
2\partial_tR_{ij}
=-(\Delta_Lv)_{ij}
-\nabla_i\nabla_j\operatorname{tr}v
+\nabla_i(\operatorname{div}v)_j
+\nabla_j(\operatorname{div}v)_i .
\]

Here \(v=-2E\), where \(E=\operatorname{Ric}+g\). Since
\[
\operatorname{tr}E=R+n,\qquad
\operatorname{div}E=\operatorname{div}\operatorname{Ric}
=\frac12\,dR
=\frac12\,d(\operatorname{tr}E),
\]
one has
\[
\operatorname{tr}v=-2\operatorname{tr}E,\qquad
\operatorname{div}v=-d(\operatorname{tr}E).
\]
Consequently,
\[
-\nabla_i\nabla_j\operatorname{tr}v
=2\nabla_i\nabla_j\operatorname{tr}E,
\]
while
\[
\nabla_i(\operatorname{div}v)_j+
\nabla_j(\operatorname{div}v)_i
=-2\nabla_i\nabla_j\operatorname{tr}E.
\]
These terms cancel exactly, leaving
\[
\partial_t\operatorname{Ric}=\Delta_LE.
\]
Also \(\Delta_Lg=0\), consistently with
\(\Delta_LE=\Delta_L\operatorname{Ric}\). Therefore
\[
\boxed{\partial_tE=\Delta_LE-2E.}
\]

Thus Part 1 of `verify_einstein_defect_evolution.py` is correct, provided the displayed curvature and Laplacian conventions are used together.

---

### 2. Squared-norm evolution

Let
\[
f=|E|^2,\qquad
\operatorname{tr}(E^3)=E_i{}^jE_j{}^kE_k{}^i.
\]
Since
\[
\partial_tg^{ij}=2E^{ij},
\]
differentiating the two inverse metrics in \(|E|^2\) contributes
\[
4\operatorname{tr}(E^3).
\]
Hence
\[
\partial_tf
=2\langle \Delta_LE-2E,E\rangle
+4\operatorname{tr}(E^3).
\]

The Lichnerowicz term satisfies
\[
\begin{aligned}
2\langle\Delta_LE,E\rangle
={}&\Delta f-2|\nabla E|^2
+4R_{ikjl}E_{ij}E_{kl}\\
&-4R_{ik}E_{ij}E_{kj}.
\end{aligned}
\]
As endomorphisms,
\[
\operatorname{Ric}=E-I,
\]
so
\[
R_{ik}E_{ij}E_{kj}
=\operatorname{tr}(\operatorname{Ric}E^2)
=\operatorname{tr}(E^3)-|E|^2.
\]
The complete zeroth-order contribution is therefore
\[
\begin{aligned}
&[-4\operatorname{tr}(E^3)+4|E|^2]
+[4\operatorname{tr}(E^3)]
+[-4|E|^2]\\
&\hspace{3cm}=0.
\end{aligned}
\]
Thus
\[
\boxed{
(\partial_t-\Delta)|E|^2
=-2|\nabla E|^2
+4R_{ikjl}E_{ij}E_{kl}.
}
\]
Cauchy–Schwarz gives
\[
(\partial_t-\Delta)f\le 4|\operatorname{Rm}|f.
\]

The algebra in Part 2 of the script is correct.

---

### 3. Consequence of the \(C/t\) curvature estimate

On the closed manifold let
\[
F(t)=\sup_M |E(t)|^2.
\]
The maximum principle gives, in the upper-Dini-derivative sense,
\[
D^+F(t)\le \frac{4C}{t}F(t).
\]
Therefore, for \(0<s<t_0\),
\[
\boxed{
F(t_0)\le F(s)\left(\frac{t_0}{s}\right)^{4C}.
}
\]
Letting \(s\downarrow0\) makes this upper estimate vacuous whenever one only knows a fixed nonzero bound for \(F(s)\). The precise interpretation is:

* Every individual smooth initial metric has finite curvature at \(t=0\), so its actual \(F(t_0)\) is finite.
* The estimate \(|\operatorname{Rm}|\le C/t\) alone does not provide a uniform propagation estimate from \(F(0)\) to \(F(t_0)\) across a family whose initial full curvature can diverge.
* This computation does not establish that \(E(t_0)\) itself becomes large; it establishes that the displayed maximum-principle argument cannot retain quantitative smallness from time zero.
* If \(E(0)=0\) exactly, uniqueness gives \(E(t)\equiv0\), despite the vacuous upper estimate.

Thus the pointwise \(C/t\) issue identified in the script is mathematically real at the level of this Gronwall argument.

---

### 4. The proposed damping ODE needs correction

For \(f=|E|^2\), the tensor term \(-2E\) initially contributes \(-4f\), not \(-2f\). More importantly, that contribution is canceled exactly by the Ricci terms in \(\Delta_L\) together with the evolving metric used to form the norm. The resulting scalar equation has no universal damping term:
\[
(\partial_t-\Delta)f
=-2|\nabla E|^2+4\operatorname{Rm}(E,E).
\]

Accordingly, the Part 3 model
\[
f'=(-2+4C/t)f
\]
is not the ODE supplied by the exact squared-norm evolution. Even if a constant damping term had survived, it would only add a finite factor such as
\[
e^{-4(t_0-s)}\left(\frac{t_0}{s}\right)^{4C},
\]
which still diverges as \(s\downarrow0\).

At an Einstein fixed metric with \(\operatorname{Ric}=-g\),
\[
\Delta_LE-2E=\Delta E+2\operatorname{Rm}(E).
\]
This also makes the cancellation transparent. A uniform curvature bound yields finite-time dependence,
\[
F(t)\le e^{4Kt}F(0),
\]
but decay requires a favorable spectral property of the operator
\(\Delta+2\operatorname{Rm}\); bounded curvature alone does not supply it.

---

### 5. Integral estimates that can potentially retain smallness

The exact global \(L^2\) identity includes the evolving volume form
\[
\partial_td\mu=-\operatorname{tr}E\,d\mu:
\]
\[
\boxed{
\frac{d}{dt}\int_M |E|^2\,d\mu
=-2\int_M|\nabla E|^2\,d\mu
+4\int_M\operatorname{Rm}(E,E)\,d\mu
-\int_M(\operatorname{tr}E)|E|^2\,d\mu.
}
\]
The trace obeys the useful scalar equation
\[
\boxed{
(\partial_t-\Delta)\operatorname{tr}E
=2|E|^2-2\operatorname{tr}E.
}
\]
In particular, the downward part of \(\operatorname{tr}E\) is controlled from its initial value by the scalar maximum principle. The main analytic term is therefore
\[
\int |\operatorname{Rm}|\,|E|^2.
\]

In dimension four, on a ball \(B_r\), Hölder and a relative Sobolev inequality give schematically
\[
\int_{B_r}|\operatorname{Rm}|\,|\phi E|^2
\le
\|\operatorname{Rm}\|_{L^2(B_r)}
\|\phi E\|_{L^4(B_r)}^2.
\]
Writing
\[
\varepsilon_r=
\frac{r^4}{\operatorname{Vol}(B_r)}
\int_{B_r}|\operatorname{Rm}|^2,
\]
the volume-normalized Sobolev inequality yields
\[
\int |\operatorname{Rm}|\,|\phi E|^2
\lesssim
\varepsilon_r^{1/2}\int|\nabla(\phi E)|^2
+\varepsilon_r^{1/2}r^{-2}\int|\phi E|^2.
\]
For sufficiently small \(\varepsilon_r\), the gradient term can be absorbed into
\(-2\int|\nabla E|^2\). One then obtains a scaled estimate of the form
\[
Y'(t)\lesssim r^{-2}Y(t),
\qquad
Y(t)=\int |\phi E|^2,
\]
so over a time interval of length comparable to \(r^2\), the amplification remains finite and scale-independent.

This route would require more than the pointwise output \(|\operatorname{Rm}|\le C/t\). The needed geometric package consists of:

1. persistence, or a spacetime analogue, of the small normalized \(L^2\) curvature quantity during the early flow;
2. relative Sobolev and volume-doubling estimates uniform in time;
3. controlled cutoffs on a buffered ball;
4. control of the cutoff-annulus contributions.

The Ye Li hypothesis quoted in the supplied material has exactly the relevant initial four-dimensional normalized curvature quantity, but the stated \(C/t\) conclusion alone does not supply its persistence. That persistence would need to come from additional estimates in the smoothing argument.

If such an \(L^2\) propagation estimate is available, then at times \(t\ge \theta r^2\) the Type-I estimate becomes
\[
|\operatorname{Rm}(t)|\le C_\theta r^{-2}.
\]
Standard local parabolic mean-value estimates could then convert spacetime \(L^2\) control into an interior estimate
\[
\sup |E(t_0)|^2
\lesssim
\frac{1}{r^2\operatorname{Vol}(B_r)}
\int_{\theta r^2}^{t_0}\int_{B_r}|E|^2,
\]
potentially preserving an \(O(\delta^2)\) initial Einstein defect.

---

### 6. Other sufficient analytic inputs

The same early-time issue disappears under any of the following stronger inputs:

* \(\displaystyle \int_0^{t_0}\|\operatorname{Rm}(t)\|_\infty\,dt<\infty\);
* a bound \(|\operatorname{Rm}|\lesssim t^{-\alpha}\) with \(\alpha<1\);
* mixed spacetime control
  \[
  \operatorname{Rm}\in L_t^qL_x^p,
  \qquad
  \frac{n}{2p}+\frac1q<1;
  \]
* small critical form or heat-kernel/Kato control at equality;
* a sign estimate
  \[
  \operatorname{Rm}(E,E)\le \kappa(t)|E|^2
  \quad\text{with}\quad
  \kappa_+\in L^1_t.
  \]

The estimate \(C/t\) corresponds to the critical endpoint \(L_t^1L_x^\infty\) and provides none of these by itself. Standard parabolic regularity starting at a fixed time \(s>0\) is effective, but it still requires quantitative information about \(E(s)\); it does not bridge the interval from \(0\) to \(s\) solely from the Type-I curvature estimate.

### Bottom line

Both displayed evolution identities are correct. The divergent Gronwall factor correctly shows that \(|\operatorname{Rm}|\le C/t\) alone does not propagate initial pointwise smallness of \(E\) uniformly to positive time. The script’s separate damped ODE is inconsistent with the exact squared-norm equation. A viable replacement is a critical \(L^2\)-energy plus Sobolev/Moser argument, provided the smoothing construction also preserves suitable normalized curvature energy and local geometric inequalities during the initial parabolic layer.