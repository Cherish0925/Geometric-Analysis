# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step6_perpendicular_dual_cost_and_relative_calibration.md",
    "Sessions/S1003A01/workspace/scripts/perp_dual_cost.py",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py",
    "Sessions/S1003A01/workspace/scripts/perp_cartan_verify.py",
    "Sessions/S1003A01/workspace/data/perp_dual/summary.csv",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md"
  ]
}
```

## Task

Critically read the perpendicular P/J computations and the exact-CH factorization as a geometric analyst. Verify the smooth bolt assumptions and the assertion that C2-matched numerical profiles can be approximated by smooth exact-CH-collar cells with vanishing P and J change. If true, supply a precise cutoff lemma with a scaling estimate; if not, state the required jet matching and why the current polynomial envelope is inadequate. Also determine whether the exact Cartan identities plus CH endpoint map suggest a rigorous fixed-slot P≥8π² or J≥8π² proof, a plausible counterprofile, or neither. Keep the result limited to the diagonal perpendicular branch and distinguish P from J.

## Output

# Scientific verification memo — diagonal perpendicular branch

## 1. Main conclusions

1. The `wpow=2` profiles in `perp_dual_cost.py` have the correct smooth ordinary-blowup bolt behavior for the fixed diagonal metric
   \[
   g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2.
   \]
   The slope relation imposed on \(F,G\) removes the conical singularity, while \(w=O((x-x_0)^2)=O(t^4)\) is exactly the required weight-four tangential anisotropy. The `wpow=1` profiles are generally not smooth at the bolt.

2. The terminal polynomial envelope matches the complex-hyperbolic profile through its second \(x\)-jet. A smooth cutoff produces an exact CH collar and changes both \(P\) and \(J_6\) by a quantity tending to zero. For the actual cubic terminal vanishing in the scripts, the change is
   \[
   |P(g_\varepsilon)-P(g)|+|J_6(g_\varepsilon)-J_6(g)|
   \le C_g\varepsilon^3.
   \]
   Thus the recorded numerical values are genuine limiting costs of smooth exact-collar cells in this diagonal branch.

3. The Cartan identities are algebraically consistent, and the CH Sturm forms admit an additional exact ground-state factorization. In particular, the sign-changing potential in \(\mathcal Q_-\) does not by itself produce a compactly supported descent inside an exact CH segment.

4. The supplied material contains neither an all-profile proof of \(P\ge8\pi^2\) or \(J_6\ge8\pi^2\), nor an actual subthreshold counterprofile. It does isolate a credible coercivity mechanism, stronger for \(J_6\), but the nonlinear transition from the bolt to the CH channel still contains the signed cubic interaction. Smooth bolt asymptotics generically place that cubic on the adverse side near \(t=0\).

Everything below applies only to the fixed diagonal perpendicular branch, without rotating frames or general four-metrics.

---

## 2. Smoothness at the ordinary-blowup bolt

Put
\[
\rho=x-x_0,\qquad dt=\frac{d\rho}{2\sqrt{G}},
\]
and suppose near \(\rho=0\)
\[
F=f_1\rho+O(\rho^2),\qquad
G=g_1\rho+O(\rho^2),\qquad f_1,g_1>0.
\]
Then
\[
t=\sqrt{\rho/g_1}+O(\rho^{3/2}),\qquad
\rho=g_1t^2+O(t^4),
\]
and therefore
\[
F=f_1g_1t^2+O(t^4).
\]
With the Hopf circle normalized to have period \(2\pi\), smooth polar collapse requires
\[
\boxed{f_1g_1=1.}
\]

For an ordinary \(O(-1)\) bolt, the isotropy circle acts with weight two on the tangent plane spanned by \(\sigma_2,\sigma_3\). Its trace-free symmetric square has weight four. Consequently the difference between the two tangential metric coefficients must begin at order \(t^4\):
\[
xe^w-x=O(t^4).
\]
Since \(\rho=O(t^2)\), this is equivalent to
\[
\boxed{w=O(\rho^2).}
\]

More explicitly, the adapted axes satisfy
\[
a^2=x,\qquad b^2=xe^w,\qquad c^2=F,
\]
and smoothness has the form
\[
a(t)=A+\alpha t^2+O(t^4),\qquad
b(t)=A+\alpha t^2+O(t^4),\qquad
c(t)=t+O(t^3),\qquad A=\sqrt{x_0}.
\]
These are precisely the even/odd expansions required for a smooth diagonal invariant metric at the bolt.

### Verification for the implemented profiles

Let \(u=\log(x/x_0)/\ell\). At \(u=0\),
\[
\operatorname{smooth}(u)=10u^3-15u^4+6u^5=O(u^3)=O(\rho^3).
\]
Hence
\[
F=\rho e^{q_F}+O(\rho^3),\qquad
G=\rho e^{q_G}+O(\rho^3).
\]
The coefficient shift in `prof_factory` gives
\[
q_F(0)+q_G(0)=0,
\]
so
\[
F'(x_0)G'(x_0)=e^{q_F(0)+q_G(0)}=1.
\]
This is the conical regularity relation.

For `wpow=2`,
\[
w=\log(1+x)\operatorname{smooth}(u)
   +u^2(1-u)^3\sum c_jT_j(2u-1)
   =O(\rho^2),
\]
so the tangential split is \(O(t^4)\). Thus all main records with `wpow=2` extend smoothly across the ordinary bolt.

For `wpow=1`, the free term is generally \(O(\rho)=O(t^2)\). A weight-four tensor cannot begin at radial degree two, so such a profile does not generally define a smooth metric at the bolt. Accidental cancellation of its leading coefficient would be a separate special case.

---

## 3. Exact-collar cutoff lemma

Let the CH profile be
\[
F_0=x,\qquad G_0=x(1+x),\qquad w_0=\log(1+x),
\]
on a neighborhood of the outer endpoint \(X\), and write
\[
q=(F-F_0,\;G-G_0,\;w-w_0).
\]

### Lemma

Assume \(F,G,w\) are smooth from the interior side, \(F,G>0\), and
\[
q(X)=q'(X)=q''(X)=0.
\]
Then there are smooth diagonal profiles \(g_\varepsilon\) such that

- \(g_\varepsilon=g\) for \(x\le X-2\varepsilon\);
- \(g_\varepsilon=g_{CH}\) for \(x\ge X-\varepsilon\);
- \(g_\varepsilon\) has the same bolt as \(g\);
- as \(\varepsilon\to0\),
  \[
  P(g_\varepsilon)\to P(g),\qquad
  J_6(g_\varepsilon)\to J_6(g).
  \]

If, more quantitatively,
\[
|\partial_x^jq(x)|\le A(X-x)^{3-j},
\qquad j=0,1,2,3,
\]
then
\[
\boxed{
|P(g_\varepsilon)-P(g)|
+|J_6(g_\varepsilon)-J_6(g)|
\le C A^2\varepsilon^3,
}
\]
where \(C\) depends on a uniformly elliptic collar neighborhood and on fixed upper bounds for the profile there.

### Construction and estimate

Choose \(\chi\in C^\infty([0,\infty))\) with
\[
\chi=0\quad\text{on }[0,1],\qquad
\chi=1\quad\text{on }[2,\infty),
\]
and put \(r=X-x\). Define
\[
F_\varepsilon=F_0+\chi(r/\varepsilon)(F-F_0),
\]
\[
G_\varepsilon=G_0+\chi(r/\varepsilon)(G-G_0),
\]
\[
w_\varepsilon=w_0+\chi(r/\varepsilon)(w-w_0).
\]
For sufficiently small \(\varepsilon\), positivity of \(F_\varepsilon,G_\varepsilon\) follows from their closeness to the positive CH coefficients. The cutoff is constant near both ends of its transition interval, so the resulting profile is smooth.

On \(0\le r\le2\varepsilon\),
\[
|\partial_x^j(q_\varepsilon)|\le C A\varepsilon^{3-j},
\qquad j=0,1,2.
\]
In particular, the full metric two-jet differs from the CH two-jet by \(O(A\varepsilon)\). Since curvature is a smooth function of the metric, its inverse, and the first two metric derivatives on this uniformly elliptic collar,
\[
|\operatorname{Ric}^{\circ}_{g_\varepsilon}|
+|\operatorname{Ric}_{g_\varepsilon}+6g_\varepsilon|
\le CA\varepsilon.
\]
The collar volume density is uniformly bounded and the transition has \(x\)-length \(O(\varepsilon)\). Therefore
\[
\int_{X-2\varepsilon}^{X}
|\operatorname{Ric}^{\circ}_{g_\varepsilon}|^2\,dV
+
\int_{X-2\varepsilon}^{X}
|\operatorname{Ric}_{g_\varepsilon}+6g_\varepsilon|^2\,dV
\le CA^2\varepsilon^3.
\]
The original profile has the same estimate on the removed terminal layer, proving the displayed cost estimate.

For a merely \(C^2\)-matched profile, define
\[
\omega_2(\varepsilon)=
\sup_{X-2\varepsilon\le x\le X}
\left(
|q''|+\varepsilon^{-1}|q'|+\varepsilon^{-2}|q|
\right).
\]
The matching of the second jet implies \(\omega_2(\varepsilon)\to0\), and the same argument gives
\[
|P(g_\varepsilon)-P(g)|
+|J_6(g_\varepsilon)-J_6(g)|
\le C\varepsilon\,\omega_2(\varepsilon)^2=o(\varepsilon).
\]

### Application to the polynomial envelope

Writing \(v=1-u\),
\[
\operatorname{smooth}(u)=1-10v^3+15v^4-6v^5,
\]
while
\[
q_F,\ q_G,\ w_{\mathrm{free}}=O(v^3).
\]
Because \(u\mapsto x=x_0e^{\ell u}\) is a smooth local diffeomorphism at \(u=1\),
\[
F-x=O((X-x)^3),\quad
G-x(1+x)=O((X-x)^3),\quad
w-\log(1+x)=O((X-x)^3).
\]
Thus the stronger \(O(\varepsilon^3)\) estimate applies to every fixed stored profile.

The exact CH portion inside the original interval has thickness comparable to \(\varepsilon\). If a collar of prescribed macroscopic thickness is desired, an additional exact CH annulus can be attached outside \(X\); it contributes zero to both \(P\) and \(J_6\).

The constants can depend on \(x_0\) and the polynomial coefficients. For a sequence \(x_0\to0\), a diagonal choice of \(\varepsilon=\varepsilon(x_0)\) still makes the cutoff contribution arbitrarily small for each member.

---

## 4. Cartan identities and endpoint data

The cyclic relabeling
\[
(a,b,c)=(\sqrt{x},\sqrt{xe^w},\sqrt F)
\]
is orientation preserving, so the same structure equations
\[
d\sigma_i=2\sigma_j\wedge\sigma_k
\]
apply without an additional sign.

The symbolic calculation in `perp_cartan_verify.py` establishes
\[
|\operatorname{Ric}^{\circ}|^2
=\sum_i(r_i-v_i)^2,
\qquad
s=-2\sum_i(r_i+v_i),
\]
with
\[
r_i=\frac{\dot u_i}{a_i},\qquad
v_i=\frac{2H_i}{a_ja_k},
\qquad
H_i=u_i+\frac12u_ju_k,
\]
and
\[
\dot C=abc\sum_i r_iv_i,
\qquad
C=\sum_i u_i^2+u_1u_2u_3.
\]
The orbit-volume normalization then gives
\[
\frac{P}{8\pi^2}
=\int\sum_i\frac{\lambda_i}{4}
\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt,
\qquad
\lambda_i=\frac{a_ja_k}{a_i}.
\]
These identities hold on \(t>0\), and the smooth bolt expansions make every term integrable as \(t\downarrow0\).

At the bolt,
\[
u=(0,0,-1),\qquad C=1.
\]
On the exact CH profile,
\[
a=c=\sqrt x,\qquad b=\sqrt{x(1+x)},
\]
and direct differentiation gives
\[
u=(0,3x,0),\qquad C=9x^2.
\]
Thus
\[
\Phi=C-u_2^2
\]
has endpoint values \(1\) at the bolt and \(0\) on the CH channel. This validates the relative completion leading to equation (4.8).

---

## 5. An exact Hardy factorization on the CH segment

For
\[
p(x)=\frac{x(1+x)}4,
\]
the two quadratic forms in the note are
\[
\mathcal Q_\pm[v]
=\int\left(p(v')^2+V_\pm v^2\right)dx,
\]
where
\[
V_+=\frac{4+18x+15x^2}{16x(1+x)},\qquad
V_-=\frac{4-18x+3x^2}{16x(1+x)}.
\]

They have explicit positive zero modes:
\[
\phi_+(x)=x(1+x)^{1/2},\qquad
\phi_-(x)=x(1+x)^{-5/2},
\]
because
\[
V_\pm=\frac{(p\phi_\pm')'}{\phi_\pm}.
\]
Consequently, on any CH interval \([\xi,1]\),
\[
\boxed{
\mathcal Q_\pm[v]
=
\int_\xi^1 p\phi_\pm^2
\left(\frac{v}{\phi_\pm}\right)'^{\!2}dx
+\left[b_\pm(x)v(x)^2\right]_\xi^1,
}
\]
with
\[
b_+(x)=\frac{2+3x}{8},\qquad
b_-(x)=\frac{2-3x}{8}.
\]

In particular, if \(v(\xi)=v(1)=0\), then
\[
\mathcal Q_\pm[v]\ge0.
\]
Therefore the sign-changing coefficient in \(V_-\) does not create a compactly supported below-zero direction inside an exact CH collar.

If only the outer endpoint is fixed, \(v(1)=0\), the lower endpoint contribution is
\[
-b_\pm(\xi)v(\xi)^2.
\]
Its interaction with the preceding transition region remains essential. This is the precise trace term that a global matrix Hardy or Riccati estimate would have to absorb. The CH factorization alone does not control it.

---

## 6. Why the relative completion is not yet a theorem

Smooth bolt behavior generically puts the cubic interaction on the adverse side. Indeed, write
\[
a=A+\alpha t^2+O(t^4),\qquad
b=A+\alpha t^2+O(t^4),\qquad
c=t+\gamma t^3+O(t^5).
\]
Then
\[
u_1=\kappa t+O(t^3),\qquad
u_2=\kappa t+O(t^3),\qquad
u_3=-1+O(t^2),
\]
where
\[
\kappa=2\alpha-\frac1A,
\]
and
\[
\lambda_2=t+O(t^3).
\]
Hence
\[
u_1u_2u_3=-\kappa^2t^2+O(t^4),
\]
and the cubic term in (4.8) begins as
\[
\frac{2u_1u_2u_3}{\lambda_2}
=-2\kappa^2t+O(t^3).
\]
Thus the pointwise hypothesis \(u_1u_2u_3\ge0\) is not inherited from smooth bolt geometry; generically it is violated immediately next to the bolt.

For \(P\), the missing mathematical object is therefore a global inequality coupling:

- the three relative-flow squares in (4.8);
- the signed cubic interaction;
- the reconstruction equations
  \[
  \dot a_i=u_i+\frac{a_j^2+a_k^2-a_i^2}{a_ja_k};
  \]
- the smooth bolt data;
- the CH endpoint and its explicit trace terms.

The CH ground-state factorization is favorable evidence for such an estimate, but it handles only the exact outgoing segment and the quadratic transverse part.

For \(J_6\),
\[
J_6-P
=\frac14\int(s+24)^2dV
\]
adds the exact square in (4.12). This can compensate a possible drop in \(P\), so a direct \(J_6\) theorem is analytically weaker than a \(P\) theorem. No supplied estimate yet relates this scalar square quantitatively to the adverse cubic over the complete transition.

---

## 7. Interpretation of the numerical evidence

All stored smooth competitors satisfy
\[
P>8\pi^2,\qquad J_6>8\pi^2,
\]
and the smallest \(x_0\) values approach the threshold from above. This is consistent with a sharp infimum \(8\pi^2\), but finite polynomial degree and local optimization do not determine the all-profile infimum.

There is direct evidence that the optimizations reach distinct local points. At \(x_0=0.01\), degree eight,
\[
P_{\text{P-target}}=1.001936966,
\]
while the independently obtained J-target profile has
\[
P_{\text{J-target}}=1.001855826,
\]
which is smaller even though \(P\) was not its optimization target. The degree-10/12 J-target record lowers \(P\) further to \(1.001831515\). Together with gradients of size \(10^{-4}\)–\(10^{-3}\), this prevents interpreting the table as a resolved polynomial minimum.

The recorded decomposition
\[
S_1+S_2+S_3=0.003428047,\qquad
C_{\mathrm{cubic}}=-0.00143166
\]
shows that the signed cubic removes about \(42\%\) of the positive square contribution. It is therefore structurally important, not a numerical perturbation. At the same time, it does not nearly reverse the total sign in the stored profile.

The exact CH Hardy factorization also shows that the sign-changing \(V_-\) potential is not, by itself, a counterprofile mechanism. An actual counterprofile would require smooth positive \(F,G\), weight-four bolt behavior, an exact CH collar, and a verified value below one after integrating the full nonlinear curvature defect. No such profile appears in the supplied data.

---

## 8. P versus \(J_6\), and normalization

The logical relations are:

- a proof of \(P\ge8\pi^2\) immediately gives \(J_6\ge8\pi^2\);
- a proof of \(J_6\ge8\pi^2\) need not imply the same for \(P\);
- a P-counterprofile with \(P<8\pi^2\) need not be a J-counterprofile, because the scalar square may restore the threshold.

One textual statement in `perp_dual_cost.py` needs mathematical correction: \(P\) is scale invariant in dimension four, but \(J_6\) is not scale invariant when the number \(6\) is held fixed. The correct covariance is
\[
J_{\lambda/c}(cg)=J_\lambda(g).
\]
In particular,
\[
J_1(6g)=J_6(g),
\]
which is the rescaling relevant to the \(\operatorname{Ric}=-g\) cell normalization.

## Final assessment

The bolt and exact-collar aspects are mathematically sound for the `wpow=2` profiles, and the cutoff lemma makes the numerical competitors geometrically usable as smooth exact-CH-collar approximants. The Cartan identities and the explicit CH ground states provide substantial analytic structure.

For the complete diagonal perpendicular family, the present evidence yields neither a rigorous \(P\) or \(J_6\) threshold theorem nor an actual subthreshold cell. The strongest rigorous new information is that the exact CH transverse operators factor through positive ground states, while the unresolved part is concentrated in the nonlinear bolt-to-collar transition and its signed cubic interaction.