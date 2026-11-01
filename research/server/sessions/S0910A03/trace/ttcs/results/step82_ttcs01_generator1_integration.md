# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 82,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step82_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step82_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop the strongest mathematically plausible next step from the slice balances for the finite small-defect graph connector. Focus on the actual reversal problem: starting at a reflected scalar-minus-six center with I(0)=J(0)=0 and I'(0)=-3V, J'(0)=6V, can the coupled OT Einstein or small-defect equations dynamically create the covariance/orbit-expansion term needed for I to return to zero before singularity? Seek either (a) a coercive evolution identity controlling the turning expression 2Cov(u,v)+<v^2>/2-<|B0|^2> using the orbit H^2 energy, Codazzi/base constraints, and J' balance, or (b) a constraint-compatible perturbative center family whose exact early radial jets make the expression grow toward 3. Work in physical measures and retain all Einstein components. Do not return to constant-exit maximum principles or Noether current alone. Provide explicit equations/calculations and a decisive low-cost computation or theorem target, while clearly separating a mechanism from an established connector.

## Integrated Scientific Memo

## Reversal is exactly an intrinsic-energy drop

Use physical Gaussian gauge
\[
g=dr^2+q_r,\qquad
q_r=ds^2+e^\sigma M_{ab}d\xi^a d\xi^b,\qquad \det M=1,
\]
where \(s\) is slice arclength, \(\rho=e^\sigma\), and averages are with respect to
\[
d\mu=\rho\,ds\,d\xi^1d\xi^2,\qquad \langle f\rangle=V^{-1}\int f\,d\mu.
\]
Split
\[
S^s{}_s=u,\qquad S_{\rm orb}=\frac v2I+B_0,\qquad H=u+v,
\]
and put
\[
x=\langle u\rangle=I/V,\qquad y=\langle v\rangle=J/V.
\]

Let \(U=[M]\in\mathbb H^2\), \(h=\sigma_s\), and
\[
e=|U_s|_{\mathbb H^2}^2,\qquad
K:=\langle e-h^2\rangle.
\]
With the normalization used in Steps 79–81,
\[
R(q)=-2h_s-\frac32h^2-\frac12e.
\]
Since \(\rho_s=h\rho\),
\[
\boxed{\langle R(q)\rangle=-\frac12K.}
\]

For \(E=\operatorname{Ric}_g+3g\), the integrated \(s\)-block equation gives
\[
\boxed{
x'=3-\frac12K-\langle E_{ss}\rangle-x(x+y).
}
\]
Thus at a differentiable first return \(x=0,\ x'\ge0\),
\[
\boxed{K\le 6-2\langle E_{ss}\rangle.}
\]
At an exact reflected scalar-minus-six center,
\[
K(0)=12,\qquad x(0)=y(0)=0,\qquad x'(0)=-3,\qquad y'(0)=6.
\]
Hence reversal requires the coupled equations to drive the physical spatial energy excess
\[
\boxed{\langle |U_s|^2-h^2\rangle}
\]
from \(12\), after its initial evolution, down to approximately \(6\).

The Hamilton identity also yields, at \(x=0\),
\[
\boxed{
T:=2\operatorname{Cov}(u,v)+\frac12\langle v^2\rangle-\langle|B_0|^2\rangle
=6-\frac12K-2\langle E_{rr}\rangle .
}
\]
Together with
\[
x'=T-3+2\langle E_{rr}\rangle-\langle E_{ss}\rangle
\quad (x=0),
\]
this recovers the Step-82 necessary bound \(T\ge3-3\delta\) when
\(\|E\|_{\rm op}\le\delta\). This uses the corrected defect combination
\(2E_{rr}-E_{ss}\), not \(E_{\rm orb}-E_{rr}\).

---

## Exact production identity for \(K\)

Set
\[
a=U_s,\qquad b=U_r,\qquad
\tau=\nabla_s a+h\,a.
\]
With the above normalization,
\[
|b|_{\mathbb H^2}^2=2|B_0|^2.
\]
The traceless orbit equation and the commutation formula are
\[
\nabla_r b+Hb+\tau=\mathcal E_0,
\qquad
\nabla_r a=\nabla_s b-u\,a,
\]
where \(\mathcal E_0\) represents the traceless orbit defect.

Define
\[
c=h_s+h^2,\qquad k=e-h^2.
\]
Direct differentiation in the moving physical measure gives
\[
\boxed{
K'=
-2\langle\langle\tau,b\rangle\rangle
+2\langle vc\rangle
+\operatorname{Cov}(v-u,k)
-2xK
+2\langle\langle\mathcal E_0,b\rangle\rangle .
}
\]
The mixed Einstein equation supplies the missing constraint:
\[
\boxed{
v_s=h\left(u-\frac v2\right)
-\frac12\langle a,b\rangle_{\mathbb H^2}
-E_{rs}.
}
\]
Consequently,
\[
\boxed{
\langle vc\rangle
=-\left\langle h^2\left(u-\frac v2\right)\right\rangle
+\frac12\langle h\langle a,b\rangle\rangle
+\langle hE_{rs}\rangle .
}
\]

This identifies the only available routes to a later \(K\)-drop:

1. \(b\) must become aligned with \(+\tau\), so that
   \(-2\langle\tau,b\rangle<0\);
2. the Codazzi area terms must become favorable;
3. \(\operatorname{Cov}(v-u,k)\) must become negative enough.

Before return \(x<0\), so \(-2xK>0\) actively opposes the required decrease. Thus angular redistribution is only a kinematic possibility; it must overcome a definite expanding-measure penalty.

---

## Universal center jets: no favorable early reversal

At a scalar-minus-six reflected center,
\[
e=12-4h_s-3h^2,\qquad
k=e-h^2=12-4(h_s+h^2),
\]
so
\[
c=\frac{12-k}{4}.
\]
The exact first radial jets are
\[
\boxed{
u_r(0)=-\frac14k,\qquad
v_r(0)=3+\frac14k,\qquad
B_{0,r}(0)=-\frac12\tau_0,
}
\]
and \(\langle k\rangle=12\). It follows that
\[
\boxed{K'(0)=0}
\]
and
\[
\boxed{
K''(0)=
2\langle|\tau_0|^2\rangle
+18+\frac38\langle k^2\rangle
\ge72+2\langle|\tau_0|^2\rangle .
}
\]
Therefore \(K\) universally rises at the center. In particular,
\[
x(r)
=-3r+\frac13\left(9-\frac14K''(0)\right)r^3+O(r^5)
\le -3r-3r^3+O(r^5).
\]

This rules out option (b) in the strong sense requested: **no exact reflected scalar-minus-six OT center family can make the true reversal variable \(K\) initially move toward the required threshold \(6\)**. Any reversal must be an intermediate-radius nonlinear transfer occurring only after an initial worsening.

There is a useful reconciliation concerning the turning expression. Writing
\[
\widetilde T
=2\operatorname{Cov}(u,v)
+\frac12\operatorname{Var}(v)-\langle|B_0|^2\rangle,
\]
one obtains
\[
\widetilde T(r)
=-r^2\left[
\frac32\operatorname{Var}(c)
+\frac14\langle|\tau_0|^2\rangle
\right]+O(r^4)\le0.
\]
For the Step-82 expression, which contains \(\langle v^2\rangle\) rather than
\(\operatorname{Var}(v)\),
\[
T=\widetilde T+\frac12y^2,
\qquad y=6r+O(r^3),
\]
and hence
\[
\boxed{
T(r)=r^2\left[
18-\frac32\operatorname{Var}(c)
-\frac14\langle|\tau_0|^2\rangle
\right]+O(r^4).
}
\]
Thus \(T\) may have a positive quadratic coefficient merely because its mean contribution is \(\frac12y^2=18r^2+O(r^4)\); this does **not** signal movement toward reversal, because simultaneously \(K''(0)>0\) and \(x\) bends further downward.

For constant area \(h=0\), \(k=12\), so
\[
T(r)=r^2\left(18-\frac14\langle|\tau_0|^2\rangle\right)+O(r^4).
\]
Under the alternative convention in which the orbit tension norm is scaled by a factor \(2\), this appears as \(18-\frac12\langle|\tau_0|^2\rangle\). Any numerical elastica test must fix this normalization explicitly. Such a test can optimize the superficial \(T_2\) coefficient, but cannot evade the universal \(K''(0)>0\) obstruction.

---

## Coercive estimate and its precise limitation

The Codazzi identity gives
\[
v_s=h\left(u-\frac v2\right)
-\frac12\langle a,b\rangle-E_{rs}.
\]
A weighted Poincaré inequality therefore implies
\[
\operatorname{Var}_\rho(v)
\le C_P(\rho)\left\langle
\left[
h\left(u-\frac v2\right)
-\frac12\langle a,b\rangle-E_{rs}
\right]^2
\right\rangle .
\]
Consequently,
\[
\widetilde T
\le
2\sqrt{\operatorname{Var}(u)\operatorname{Var}(v)}
+\frac12\operatorname{Var}(v)-\langle|B_0|^2\rangle .
\]
This is not yet coercive enough to exclude turning: neither
\(\operatorname{Var}(u)\) nor the weighted Poincaré constant is controlled by the currently available balances. The missing theorem is a physical-measure estimate coupling them to
\[
\langle e+h^2+|b|^2\rangle
\]
and preventing that energy from producing \(T\ge3\) before curvature concentration.

A sharper target is therefore:

> Prove on the pre-return interval \(x\le0\) an estimate of the form
> \[
> -2\langle\tau,b\rangle
> +2\langle vc\rangle
> +\operatorname{Cov}(v-u,k)
> +2\langle\mathcal E_0,b\rangle
> \ge 2xK-\mathcal R,
> \]
> with an integrable remainder \(\mathcal R\) controlled by the full defect and a non-collapsing weighted Poincaré geometry.

If its integral is too small to lower \(K\) from its post-center value to \(6+O(\delta)\), reversal is excluded. Conversely, a computed interval where the left side is decisively negative identifies the genuine OT escape mechanism.

---

## Decisive low-cost computation

The most informative inexpensive experiment is not an algebraic moment search or a prescribed carrier optimization. March the **exact reflected OT Cauchy germ** in \(r\), spectrally in \(z\), retaining
\[
(\gamma_B,\sigma,U),\quad E_{rr},E_{rs},E_{ss},E_{\rm orb}^{\rm tr},
E_{\rm orb}^{0},
\]
and all base constraints.

Center data must satisfy pointwise
\[
R(q_0)=-6,\qquad
\partial_r(\gamma_B,\sigma,U)|_{0}=0,
\]
with exact Einstein jets generated at least through order six before numerical marching. Record
\[
x,\ y,\ K,\ K',
\]
and the separate ledger
\[
-2\langle\tau,b\rangle,\quad
2\langle vc\rangle,\quad
\operatorname{Cov}(v-u,k),\quad
-2xK,\quad
2\langle\mathcal E_0,b\rangle,
\]
together with
\[
T,\quad \widetilde T,\quad
\max_z|S|^2,\quad C_P(\rho),\quad \min_z\rho.
\]

The decisive event is not merely \(T=3\), but
\[
\boxed{x=0,\quad x'\ge0,\quad K\le6+O(\delta)}
\]
before loss of regularity or collapse of the weighted circle geometry. If it occurs, the ledger reveals which coupled term reverses the universal initial rise of \(K\). If every resolved center family instead has \(K\) increasing until singularity, the numerical evidence points directly toward the coercive inequality above.

The established conclusion is therefore negative only at the germ level: early-jet engineering cannot produce reversal. A finite connector remains unestablished; its exact unresolved object is a later nonlinear drop of \(K=\langle|U_s|^2-h^2\rangle\) by roughly six units against the positive \(-2xK\) term, while all Einstein components remain uniformly small.