# TTCS Independent Branch Record

```json
{
  "step_id": 73,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step73_global_positive_proof_allocation.md",
    "Sessions/S0910A02/workspace/plans/step73_general_higher_flux_necessity_plan.md",
    "Skills/qiushi-yau26/references/research/20260912.tex",
    "Sessions/S0910A02/workspace/notes/step70_necessity_flux_dichotomy.md",
    "Sessions/S0910A02/workspace/data/step53_crepant_wall_and_stratum_probe.json"
  ]
}
```

## Task

Read the Step 73 allocation note and the higher-mode flux plan. Check the mathematical plausibility and risks of the proposed general cone higher-obstruction flux identity: the homogeneous degree-l tensor K_l, dual o_l=r^{-(d+2l-2)}K_l, expected Wronskian coefficient -(d+2l-2)/2, TT/radial-gauge cancellation of linearized Ricci gauge terms, operator-norm lower bound, nonlinear/weighted extension cautions, and the decision to prove an isolated cone lemma first while only stating a stratified obstruction-bundle extension. Identify any sign/scaling mistakes or hidden assumptions that Agent2 must fix before treating it as a theorem. Do not decide the whole Yau26 problem; focus on making the next theorem statement correct and useful.

## Output

# Scientific memo: general cone higher-mode flux

## 1. Main conclusion

The proposed dual tensor and exact Wronskian identity are mathematically consistent:

\[
o_\ell=r^{-(d+2\ell-2)}K_\ell,\qquad
\int_A\langle D\operatorname{Ric}_e u,o_\ell\rangle
=-\frac{d+2\ell-2}{2}I_{K_\ell},
\]

provided homogeneity and Laplacian conventions are stated precisely.

The main scaling error is the proposed unweighted estimate

\[
\|D\operatorname{Ric}_e u\|_{\mathrm{op},\infty}
\ge \frac{(d+2\ell-2)I_{K_\ell}}{2LJ_{K_\ell}}.
\]

This is valid only for \(\ell=2\). For \(\ell>2\), the \(L^1\) norm of \(o_\ell\) is power-like rather than logarithmic. The logarithmic estimate survives only in the weighted norm

\[
\sup_A r^{2-\ell}\|D\operatorname{Ric}_e u\|_{\mathrm{op}}.
\]

Thus the dimension-general result in `FND:flux` is general in \(d\), but remains specifically a quadratic-mode result. Higher polynomial degree changes the analytic scaling substantially.

---

## 2. Exact linear calculation

Use Cartesian-component homogeneity:

\[
\nabla_{\partial_r}K_\ell=\frac{\ell}{r}K_\ell,
\]

rather than tensor homogeneity under dilation pullback, which differs by the two covariant indices. Let

\[
a=d+2\ell-2,\qquad o_\ell=r^{-a}K_\ell.
\]

From

\[
\operatorname{tr}K_\ell=0,\quad
\operatorname{div}K_\ell=0,\quad
\Delta K_\ell=0,\quad
K_\ell(x,\cdot)=0,
\]

one obtains

\[
\operatorname{tr}o_\ell=0,\qquad
\operatorname{div}o_\ell=0,\qquad
o_\ell(x,\cdot)=0.
\]

Indeed,

\[
\operatorname{div}(r^{-a}K_\ell)
=r^{-a}\operatorname{div}K_\ell
-a r^{-a-2}K_\ell(x,\cdot)=0.
\]

Also, for any radial scalar \(f\),

\[
\Delta(fK_\ell)
=\left(f''+\frac{d-1+2\ell}{r}f'\right)K_\ell.
\]

Taking \(f=r^{-a}\) gives

\[
\Delta o_\ell
=a(a-d-2\ell+2)r^{-a-2}K_\ell=0.
\]

Thus \(o_\ell\) is the decaying componentwise harmonic partner, with coefficient degree

\[
-(d+\ell-2).
\]

### Gauge terms

With \(\Delta=\sum_i\partial_i^2\),

\[
(D\operatorname{Ric}_e u)_{ij}
=-\frac12\Delta u_{ij}
+\frac12(\partial_i\beta_j+\partial_j\beta_i),
\]

where

\[
\beta_j=\partial^ku_{kj}-\frac12\partial_j\operatorname{tr}u.
\]

Because \(o_\ell\) is divergence-free and \(o_\ell(\nu,\cdot)=0\) on every sphere \(r=\mathrm{const}\),

\[
\int_A\langle \operatorname{sym}D\beta,o_\ell\rangle=0.
\]

This cancellation depends on the dual tensor \(o_\ell\), not on \(u\) itself being TT.

Green’s identity then gives, since \(u=0\) near \(r=b\) and \(u=K_\ell\) near \(r=R\),

\[
\begin{aligned}
\int_A\langle D\operatorname{Ric}_e u,o_\ell\rangle
&=-\frac12\int_A\langle\Delta u,o_\ell\rangle\\
&=-\frac12\int_{r=R}
\left(
\langle\nabla_{\partial_r}K_\ell,o_\ell\rangle
-\langle K_\ell,\nabla_{\partial_r}o_\ell\rangle
\right).
\end{aligned}
\]

Since

\[
\nabla_{\partial_r}o_\ell
=-\frac{d+\ell-2}{r}o_\ell,
\]

the Wronskian coefficient is

\[
\frac{\ell+d+\ell-2}{r}
=\frac{d+2\ell-2}{r}.
\]

The powers of \(R\) cancel against the sphere measure, yielding

\[
\boxed{
\int_A\langle D\operatorname{Ric}_e u,o_\ell\rangle
=-\frac{d+2\ell-2}{2}I_{K_\ell}.
}
\]

This agrees with `FND:flux` at \(\ell=2\). The minus sign is correct for the displayed convention. If the rough Laplacian is instead written as \(\nabla^*\nabla=-\Delta\), the formula must be translated accordingly.

---

## 3. Correct operator-norm estimates

On \(r=\rho\),

\[
\|o_\ell\|_*=\rho^{-(d+\ell-2)}
\|K_\ell\|_{*,r=1}.
\]

Consequently,

\[
\int_A\|o_\ell\|_*\,dV
=J_{K_\ell}\int_b^R r^{1-\ell}\,dr.
\]

Define

\[
H_\ell(b,R)=
\begin{cases}
\log(R/b),&\ell=2,\\[1mm]
\dfrac{b^{2-\ell}-R^{2-\ell}}{\ell-2},&\ell>2.
\end{cases}
\]

Operator/nuclear norm duality therefore gives the correct unweighted estimate

\[
\boxed{
\|D\operatorname{Ric}_e u\|_{\mathrm{op},\infty}
\ge
\frac{(d+2\ell-2)I_{K_\ell}}
{2J_{K_\ell}H_\ell(b,R)}.
}
\]

For \(\ell>2\) and \(b/R\to0\),

\[
H_\ell(b,R)\sim \frac{b^{2-\ell}}{\ell-2},
\]

so the lower bound has size \(b^{\ell-2}\), not \(L^{-1}\).

There is a valid logarithmic weighted form:

\[
\int_A r^{\ell-2}\|o_\ell\|_*\,dV
=LJ_{K_\ell},
\]

hence

\[
\boxed{
\sup_A r^{2-\ell}
\|D\operatorname{Ric}_e u\|_{\mathrm{op}}
\ge
\frac{(d+2\ell-2)I_{K_\ell}}
{2LJ_{K_\ell}}.
}
\]

At \(\ell=2\), weighted and unweighted norms coincide.

### Explicit scale test

Let \(\chi(r/b)\) vanish near \(r=b\) and equal \(1\) for \(r\ge2b\), and set

\[
u_b=\chi(r/b)K_\ell.
\]

The radial multiplier preserves trace, divergence, and radial gauge. Moreover,

\[
\Delta u_b
=
\left(
\chi_b''+\frac{d-1+2\ell}{r}\chi_b'
\right)K_\ell,
\]

so on its support

\[
\|D\operatorname{Ric}_e u_b\|_\infty
\le C b^{\ell-2}.
\]

For \(\ell>2\), this is much smaller than \(1/\log(R/b)\). It also matches the power in the corrected unweighted estimate. Thus the quadratic mode is the unique logarithmically critical polynomial mode.

As a result, a nonzero \(\ell>2\) endpoint mismatch does not by itself imply

\[
\delta\,L\gtrsim 1
\]

for the ordinary Ricci operator norm. If \(b\asymp t^\gamma\), the direct estimate instead has the scale

\[
\delta\gtrsim t^{\gamma(\ell-2)},
\]

up to endpoint and nonlinear terms. An exponential relation is therefore special to \(\ell=2\), unless an additional persistence hypothesis prevents the transition from being concentrated near \(r=b\).

---

## 4. Hidden geometric assumptions behind “higher obstruction”

The clean cone identity applies to any \(K_\ell\) satisfying the four displayed tensor equations. Identifying such a tensor with an actual higher Einstein obstruction requires more structure.

1. **Bianchi and radial gauges are distinct.**  
   The condition \(K_\ell(x,\cdot)=0\) is natural in geodesic normal coordinates, while \(\operatorname{div}K_\ell=0\) is a Bianchi-type condition. They coincide for the quadratic pure-Weyl tensor used in `FND:flux`. For higher jets, a general normal-coordinate coefficient need not satisfy both after lower jets and nonlinear forcing are included.

2. **Higher jets are coordinate-sensitive.**  
   The quadratic Weyl tensor represents curvature and is geometrically intrinsic after fixing the frame. Higher Taylor coefficients can change under higher-order coordinate transformations. A mode used as an obstruction datum needs a fixed slice and fixed endpoint markings, or a proof that its projection is invariant modulo pure gauge terms.

3. **Formal tower subtraction is essential.**  
   For \(\ell>2\), the order-\(\ell\) Einstein equation is generally forced by products of lower jets. The object paired with \(o_\ell\) should be the residual after subtracting the full lower formal tower, not simply the raw degree-\(\ell\) Taylor coefficient.

4. **Endpoint errors require first radial derivatives.**  
   The Wronskian contains both \(u\) and \(\nabla_{\partial_r}u\). Approximate endpoint matching therefore needs projected \(C^1\) control, not only tensor \(C^0\) control.

5. **Logarithmic resonances need separate formulas.**  
   If the formal expansion contains \(r^\ell\log r\), its radial derivative changes the end-sphere flux. The coefficient is no longer obtained by inserting \(K_\ell\) into the pure homogeneous formula.

6. **The integer \(\ell\) need not equal obstruction order.**  
   Biquard–Ozuch obstruction order, ALE Jacobi-field decay, and polynomial angular degree are related through the relevant indicial decomposition, but are not interchangeable without a mode-identification theorem.

---

## 5. Nonlinear and weighted extensions

The proposed energy

\[
\mathcal E_\ell(v)
=\int_A r^{-d-2\ell+4}|Dv|^2
\]

has plausible scaling for an isolated degree-\(\ell\) component: if \(v\sim r^\ell\), then

\[
\mathcal E_\ell(v)\sim R^2.
\]

However, the nonlinear pairing does not enter merely as \(C\mathcal E_\ell\). Since

\[
o_\ell\sim r^{-d-\ell+2},
\]

the pure-mode quadratic terms satisfy schematically

\[
\int_A
\bigl(|Dv|^2+|v||D^2v|\bigr)|o_\ell|
=O(R^\ell).
\]

In energy notation this naturally carries a factor comparable to

\[
R^{\ell-2}\mathcal E_\ell(v),
\]

together with Hardy and endpoint terms.

There are two further distinctions:

- The total metric perturbation normally begins at order \(r^2\), so it cannot satisfy an \(O(r^\ell)\) estimate when \(\ell>2\). The degree-\(\ell\) component must be separated from the common quadratic and intermediate jets.
- Cross terms between a quadratic background and \(v_\ell\) pair with \(o_\ell\) at size \(O(R^2)\), while the pure \(v_\ell^2\) contribution is \(O(R^\ell)\). These terms belong explicitly in the remainder formula.

The normalized Einstein term also matters:

\[
D(\operatorname{Ric}-\lambda g)_e v
=D\operatorname{Ric}_e v-\lambda v.
\]

For \(v\sim r^\ell\),

\[
\int_A|\langle \lambda v,o_\ell\rangle|=O(R^2).
\]

The weighted energy estimate therefore needs exact radius factors, formal lower-jet terms, and \(C^1\) endpoint errors before it becomes a theorem.

Finally, the coordinate-pullback example in `20260912.tex` shows that weighted derivative energy is not geometrically controlled by the Ricci operator norm alone. Harmonic or Bianchi coordinates with quantified control are part of the mathematical hypotheses, not merely a presentation choice.

---

## 6. Stratified obstruction bundles

Separating the isolated transverse cone calculation from the stratum problem is mathematically well founded. The stratum version is not a direct corollary.

For an exact product \(S^m\times A^d\) with a parallel obstruction tensor \(K_\ell\), the isolated identity integrates over \(S\) and is multiplied by \(\operatorname{Vol}(S)\). This is a genuine intermediate result.

If \(K_\ell=K_\ell(y)\) varies along \(S\), the full rough Laplacian contains

\[
\Delta_{\mathrm{full}}u
=\Delta_{\mathrm{normal}}u+\Delta_Su,
\]

and the flux pairing gains a tangential term such as

\[
-\frac12\int_{S\times A}
\langle\Delta_Su,o_\ell\rangle.
\]

Normal connection curvature, second fundamental form terms, mixed tensor components, and derivatives of the obstruction section add further contributions. The effective equation is therefore a bundle-valued elliptic equation along the stratum, not merely the algebraic condition

\[
R_{\mathrm{normal},\pm}(y)\zeta(y)=0.
\]

A nonzero normal coefficient at one point can be offset by tangential derivative terms unless parallelism or quantitative slow variation is assumed. Pointwise Ricci pinching controls the total bundle equation, not its normal algebraic part separately.

A rigorous stratum formulation also needs:

- a smooth fixed-isotropy stratum;
- an obstruction orbibundle with specified normal connection;
- uniform transverse ALE charts and markings;
- control of covariant derivatives of the obstruction section;
- fiberwise tower subtraction;
- an elliptic estimate along the stratum strong enough to convert integrated information into local control.

The Step 53 warning about parameter variation is therefore correct, but the resulting object is an elliptic obstruction-bundle equation rather than a simple stratum integral.

---

## 7. Theorem-ready form

The isolated linear result can be stated cleanly for every \(d\ge4\) and \(\ell\ge2\) with:

\[
\int_A\langle D\operatorname{Ric}_e u,o_\ell\rangle
=-\frac{d+2\ell-2}{2}I_{K_\ell},
\]

\[
\|D\operatorname{Ric}_e u\|_{\infty}
\ge
\frac{(d+2\ell-2)I_{K_\ell}}
{2J_{K_\ell}H_\ell(b,R)},
\]

and

\[
\sup_A r^{2-\ell}
\|D\operatorname{Ric}_e u\|_{\infty}
\ge
\frac{(d+2\ell-2)I_{K_\ell}}
{2LJ_{K_\ell}}.
\]

Its scientific interpretation should distinguish:

- \(\ell=2\): unweighted logarithmic flux, yielding the familiar \(\delta L\) mechanism;
- \(\ell>2\): power-scaled unweighted flux, with logarithmic control only in a weighted Ricci norm.

The exact Wronskian generalization is sound. The proposed all-mode unweighted \(1/L\) consequence and the associated exponential-neck statement are not supported for \(\ell>2\) without substantial extra hypotheses.