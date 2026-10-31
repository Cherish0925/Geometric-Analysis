# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 34,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step34_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step34_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently read the peer's canonical almost-Kähler gap identity for diagonal perpendicular exact-CH O(-1) cells. Check the conformal factor and almost-Kähler construction, the exact coefficients and signs in P_hat-1=12H+6G+(3/2)Qdelta+(1/2)QA-(3/2)N+Sigma, the transport lambda=nu_T/2+beta nu and bolt charge law, and the far-field Hardy conclusion. Use the supplied scripts/data as supporting records, but reason through the derivation. State the exact hypotheses, identify any hidden boundary or integrability assumption, and judge whether this identity genuinely supplies a stronger route to the non-round lower bound than b_++phi(q,eta). Develop the most plausible compact near-zone inequality coupling nu, lambda, and log u, or identify a structural countermechanism if the desired >=1 lower bound is implausible.

## Integrated Scientific Memo

# Verification memo

## 1. Precise scope and hypotheses

The identity is valid for a **smooth diagonal \(SU(2)\)-invariant perpendicular \(O(-1)\) cell**
\[
g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2,
\qquad d\sigma_i=2\sigma_j\wedge\sigma_k,
\]
with the following assumptions.

1. **Perpendicular smooth bolt.** The \(h\)-slot collapses while \(f\) is the CH fibre:
   \[
   a_h=t+O(t^3),\qquad a_f=b+O(t^2),\qquad a_g=b+O(t^2),
   \]
   including the usual evenness and isotropy compatibility needed for a smooth \(O(-1)\) bolt.

2. **Exact CH outer collar, not merely matched boundary data.** On an open collar the metric is exactly complex hyperbolic, with \(a_g=a_h\). This is used to fix the normalization of the canonical form, to obtain \(u=1\), \(u'=0\), and \(\nu=0\) at the outer endpoint, to evaluate the Chern primitive, and in the relative Chern–Weil formula.

3. **Orientation and normalization.** The orientation makes \(e^{0f}+e^{gh}\) self-dual; \(\widehat P=P/(8\pi^2)\), \(dV=2\pi^2W\,dt\), \(W=a_fa_ga_h\).

4. **Diagonal symmetry.** This makes \(W_2^+=0\) and reduces \(W^+\) to the three diagonal eigenvalues used below.

5. The simplification \(\Sigma=0\) requires the **pointwise** equation \(s\equiv-24\), not merely an average scalar-curvature condition.

The conformal almost-Kähler metric is singular at the bolt. Every Stokes or integration-by-parts calculation must therefore first be made on \([\varepsilon,t_+]\) and then passed to \(\varepsilon\downarrow0\) using the smooth original bolt expansions. This is the principal hidden boundary assumption.

---

## 2. Conformal factor and almost-Kähler structure

For
\[
\omega=d(\phi\sigma_f),
\]
one has
\[
\omega=\frac{\phi'}{a_f}e^{0f}+\frac{2\phi}{a_ga_h}e^{gh}.
\]
Thus \(\omega\) is self-dual exactly when
\[
\frac{\phi'}{\phi}=\frac{2a_f}{a_ga_h}.
\]
Normalize \(\phi=a_ga_h\) on the exact CH collar and define
\[
u^2=\frac{\phi}{a_ga_h},\qquad dT=u\,dt,\qquad A_i=ua_i.
\]
Then
\[
\omega=2(\hat e^{0f}+\hat e^{gh}),\qquad \hat g=u^2g,
\]
so \(\omega/2\) has constant norm and defines the almost-Kähler structure on the deleted cell.

Writing
\[
\mathcal P=A_gA_h,
\]
gives
\[
\mathcal P=u^2a_ga_h=\phi,\qquad
\mathcal P_T=\frac{\phi'}u=2ua_f=2A_f,
\]
hence the exact AK constraint
\[
\boxed{A_f=\frac12\mathcal P_T.}
\]

There is a typo in the header of `step28_ak_nu_structure.py`: it says \(P_m=A_gA_h=2\phi\). The correct relation is
\[
P_m=A_gA_h=\phi.
\]
The executable formulas use \(A_f=P_m'/2\), so the computation itself follows the correct normalization.

At the bolt,
\[
\phi\sim ct^2,\qquad u^2\sim \frac cb\,t,\qquad T\asymp t^{3/2},
\]
and therefore
\[
A_f,A_g\asymp T^{1/3},\qquad A_h\asymp T.
\]
Thus \(\hat g\) is incomplete and anisotropically singular; it is not a smooth AK metric across the bolt. Nevertheless,
\[
u'^2W\,dt,\qquad \nu^2\,d\hat V,\qquad \lambda^2\,d\hat V,
\qquad \delta^2\,d\hat V
\]
are locally integrable under the stated bolt expansions.

---

## 3. Nijenhuis scalar, transport, and bolt charge

Put
\[
A_g=\sqrt{\mathcal P}\,e^{q/2},\qquad
A_h=\sqrt{\mathcal P}\,e^{-q/2},
\]
and
\[
v_i=(A_i)_T-\gamma_i,\qquad
\gamma_i=\frac{A_j^2+A_k^2-A_i^2}{A_jA_k}.
\]
Using \(\mathcal P_T=2A_f\),
\[
\frac{v_h}{A_h}
=-\frac12q_T-\frac{2\sinh q}{A_f},
\qquad
\frac{v_g}{A_g}
=\frac12q_T+\frac{2\sinh q}{A_f}.
\]
Therefore
\[
\boxed{
\nu:=\frac{v_h}{A_h}=-\frac{v_g}{A_g}
=-\frac12\left(q_T+\frac{4\sinh q}{A_f}\right).
}
\]

The diagonal self-dual curvature formula
\[
R^+_{ii}
=-\frac{(v_i)_T}{2A_i}
+\frac{-v_i-v_jv_k/2}{A_jA_k}
\]
then gives, after subtracting the \(g,h\) components,
\[
\boxed{
\lambda:=\frac{\widehat W^+_{gg}-\widehat W^+_{hh}}2
=\frac12\nu_T+\beta\nu,
\qquad
\beta=-\frac{(A_f)_T}{2A_f}+\frac{2\cosh q}{A_f}.
}
\]
Both the factor \(1/2\) and the signs are correct.

If
\[
\frac{\mu_T}{\mu}=2\beta,
\]
then
\[
\boxed{(\mu\nu)_T=2\mu\lambda,}
\]
with
\[
\mu=C(ua_f)^{-1}
\exp\!\left(\int\frac{4\cosh q}{a_f}\,dt\right).
\]
The multiplicative constant \(C\) changes the numerical bolt charge but not its nonvanishing or the charge law.

Near the perpendicular bolt,
\[
q=\log(b/t)+O(t^2),\qquad
\nu\sim-\frac1{2ut}\asymp-t^{-3/2},
\qquad
\mu\asymp t^{3/2}.
\]
Hence
\[
K:=\lim_{t\downarrow0}\mu\nu
\]
exists and is nonzero. Since \(\nu=0\) on the exact CH collar,
\[
\boxed{K=-2\int_{\rm cell}\mu\lambda\,dT.}
\]

For the supplied \(x_0=.038\) record,
\[
K=-0.0174759482,\qquad
2\int\mu\lambda\,dT=0.01747594819,
\]
with genuine cumulative mismatch about \(1.3\times10^{-12}\).

Two numerical caveats are important:

- `transport_rel_residual_max = 2.0\times10^7` does **not** validate the pointwise transport formula. The script differentiates \(\nu\sim T^{-1}\) on reconstructed cumulative quadrature coordinates, where large terms cancel to produce the much smaller \(\lambda\); this test is ill-conditioned and geometrically misparameterized.
- The JSON field `law_residual` is hard-coded to zero by dead code. The meaningful check is `law_residual_from_i30`, together with the endpoint integral above.

The transport law itself is supported by the exact symbolic curvature derivation, not by that failed finite-difference field.

---

## 4. Chern–Stokes identity and coefficients in the gap formula

Let
\[
w=A_fA_gA_h,\qquad d\hat V=w\,dT=u^4W\,dt.
\]
The curvature identities are
\[
\kappa-\hat s=6\nu^2,\qquad
\hat s^*=\hat s+2\nu^2,
\]
so
\[
\kappa=\hat s^*+4\nu^2.
\]

The exact primitive is
\[
\hat s^*w
=\frac d{dT}
\left(
4\mathcal P\cosh q
-\mathcal P\mathcal P_{TT}
-\frac12\mathcal P_T^2
\right).
\]
The bracket tends to zero at the bolt. On CH, with \(\mathcal P=x=\sinh^2R\),
\[
q=0,\qquad
\mathcal P_T=2\sqrt{x(1+x)},\qquad
\mathcal P_{TT}=2(1+2x),
\]
and the bracket equals \(-6x^2\). Hence
\[
\int\hat s^*\,d\hat V=-6X^2=-24V_{\rm CH}.
\]
Also,
\[
w=\frac12\mathcal P\mathcal P_T=\frac14(\mathcal P^2)_T,
\qquad
\int d\hat V=\frac{X^2}{4}=V_{\rm CH}.
\]

Define
\[
N=4\int\nu^2d\hat V,\qquad
\delta=\widehat W^+_{\omega\omega}+4=\frac{\kappa}{6}+4.
\]
Then
\[
\int\delta\,d\hat V
=\frac16\int\hat s^*d\hat V
+\frac23\int\nu^2d\hat V+4V_{\rm CH}
=\boxed{\frac N6}.
\]

Now write \(x=\widehat W^+_{\omega\omega}=\delta-4\). Trace-freeness gives the other eigenvalues
\[
-\frac x2+\lambda,\qquad -\frac x2-\lambda,
\]
and therefore
\[
|\widehat W^+|^2=\frac32x^2+2\lambda^2.
\]
With
\[
Q_\delta=\int\delta^2d\hat V,\qquad
Q_A=4\int\lambda^2d\hat V,
\]
conformal invariance yields
\[
D_+
=24V_{\rm exc}+2N-\frac32Q_\delta-\frac12Q_A.
\]

The conformal scalar formula gives
\[
\int\hat s\,d\hat V
=6G+\int su^2W\,dt,\qquad
G=\int u'^2W\,dt.
\]
The boundary term vanishes because
\[
uu'W=O(t)\quad\text{at the bolt},\qquad u'=0\quad\text{on the CH collar}.
\]
Since
\[
\int\hat s\,d\hat V=-24V_{\rm CH}-\frac N2,
\]
one obtains
\[
V_{\rm exc}
=H+\frac G2+\frac N{24}
+\frac1{12}\int(s+24)u^2W\,dt,
\]
where
\[
H=\int(u^2-1)^2W\,dt.
\]

Substitution into
\[
1-\widehat P=D_+-36V_{\rm exc}-S_{\rm exc}
\]
gives exactly
\[
\boxed{
\widehat P-1
=12H+6G+\frac32Q_\delta+\frac12Q_A-\frac32N+\Sigma,
}
\]
with
\[
\boxed{
\Sigma
=\int(s+24)(u^2-1)W\,dt
+\int\frac{(s+24)^2}{48}W\,dt.
}
\]
Thus every coefficient and sign in the claimed identity is correct.

There is a useful stronger algebraic form:
\[
12H+\Sigma
=\frac1{48}\int(s+24u^2)^2W\,dt.
\]
Consequently
\[
\boxed{
\widehat P-1
=6G+\frac32Q_\delta+\frac12Q_A-\frac32N
+\frac1{48}\int(s+24u^2)^2W\,dt.
}
\]
This shows that, without assuming \(s=-24\), the only negative term is still \(-3N/2\). If \(s=-24\), the last square is \(12H\).

The supplied record verifies the identity to \(2.1\times10^{-10}\):
\[
\begin{aligned}
\widehat P-1&=-0.0047126289,\\
12H&=0.0033317627,\quad
6G=0.0556282430,\quad
\tfrac32Q_\delta=0.0011324989,\\
\tfrac12Q_A&=0.0328568573,\quad
-\tfrac32N=-0.0976572403,\quad
\Sigma=-4.7502\times10^{-6}.
\end{aligned}
\]

---

## 5. Far-field Hardy conclusion

From
\[
\nu_T=2\lambda-2\beta\nu
\]
one gets
\[
(\nu^2w)_T
=4\nu\lambda w+\Lambda\nu^2w,
\qquad
\Lambda=\frac{w_T}{w}-4\beta.
\]
On a **terminal interval** \([T_0,T_+]\) ending where \(\nu(T_+)=0\), suppose
\[
\Lambda\ge c>0.
\]
Writing
\[
A=\int_{T_0}^{T_+}\nu^2w\,dT,\qquad
L=\int_{T_0}^{T_+}\lambda^2w\,dT,
\]
integration gives
\[
cA+\nu(T_0)^2w(T_0)\le4\sqrt{AL},
\]
hence
\[
A\le\frac{16}{c^2}L.
\]
Therefore
\[
2L-6A\ge0
\]
whenever
\[
\boxed{c\ge4\sqrt3.}
\]

This is not a local conclusion on an arbitrary disconnected subset where \(\Lambda\ge4\sqrt3\); the interval must reach an endpoint at which \(\nu=0\), or retain the corresponding endpoint term.

On CH,
\[
\Lambda=\frac{8x-3}{\sqrt{x(1+x)}},
\]
and the relevant positive solution of \(\Lambda=4\sqrt3\) is
\[
\boxed{x_H=3+\frac34\sqrt{15}\approx5.9047.}
\]
The constant \(4\sqrt3\) is sharp for constant/exponential weights.

A sharper endpoint-exporting version follows by setting
\[
z=\mu\nu,\qquad m=\frac{w}{\mu^2},
\qquad \Lambda=(\log m)_T.
\]
Then
\[
\frac12Q_A-\frac32N
=\int m\left(\frac12z_T^2-6z^2\right)dT.
\]
For any \(C^1\) multiplier \(\kappa\),
\[
\begin{aligned}
\int_a^b m\left(\frac12z_T^2-6z^2\right)dT
\ge {}&
[\kappa mz^2]_a^b\\
&+\int_a^b mz^2
\left(\kappa_T+\Lambda\kappa-2\kappa^2-6\right)dT .
\end{aligned}
\]
On a tail with \(\Lambda\ge c\ge4\sqrt3\), a constant root of
\[
2\kappa^2-c\kappa+6=0
\]
gives positivity plus a nonnegative trace contribution at the near/far interface. At threshold, \(\kappa=\sqrt3\).

For the record, the last crossing is \(x_*\approx5.9488\), and
\[
2\int_{\rm tail}\lambda^2d\hat V
-6\int_{\rm tail}\nu^2d\hat V
=0.0058777>0.
\]
The location \(x_*\approx6\) is empirical for these competitors, not a uniform theorem for all admissible cells.

---

## 6. Natural compact near-zone formulation

For \(s=-24\), set
\[
v=u^{-1},\qquad
\rho=(\log v)_T=-(\log u)_T,\qquad
m_0=(\log w)_T.
\]
Then
\[
G=\int\rho^2w\,dT,\qquad
H=\int(v^2-1)^2w\,dT.
\]
The conformal scalar equation
\[
-6\hat\Delta v+\hat s\,v+24v^3=0
\]
and
\[
\delta=\frac{\hat s}{6}+\nu^2+4
\]
give the exact coupling
\[
\boxed{
\delta
=\rho_T+\rho^2+m_0\rho+\nu^2+4(1-v^2).
}
\]
Using \(2\lambda=\nu_T+2\beta\nu\), the complete exact-scalar gap becomes
\[
\boxed{
\begin{aligned}
\widehat P-1=\int w\Big[
&6\rho^2-6\nu^2
+\frac12(\nu_T+2\beta\nu)^2\\
&+\frac32\big(
\rho_T+\rho^2+m_0\rho+\nu^2+4(1-v^2)
\big)^2
+12(v^2-1)^2
\Big]dT .
\end{aligned}
}
\]
This is the most direct compact near-zone functional coupling \(\nu\), \(\lambda\), and \(\log u\).

Equivalently, with \(z=\mu\nu\) and \(m=w/\mu^2\),
\[
\frac12Q_A-\frac32N
=\int m\left(\frac12z_T^2-6z^2\right)dT,
\qquad z(0)=K,\quad z(T_+)=0.
\]
The associated Jacobi operator is
\[
-\frac1m(mz_T)_T-12z,
\]
or
\[
z_{TT}+\Lambda z_T+12z=0
\]
at stationarity. The exact near-zone question is therefore a weighted ground-state/Riccati problem coupled to the conformal equation for \(v\).

A sufficient condition for a zero-deficit estimate can be written as follows. If a multiplier \(\kappa\), with a bolt behavior strong enough that \(\kappa mz^2\to0\), satisfies
\[
\boxed{
\kappa_T+\Lambda\kappa-2\kappa^2
\ge 6\left(1-\frac{\rho^2}{\nu^2}\right)
}
\]
where \(\nu\neq0\), then the \(6G\) term compensates the negative Nijenhuis sector; the nonnegative scalar and \(Q_\delta\) terms only improve the estimate. Near zeros of \(\nu\), this quotient formulation should be replaced by the undivided inequality
\[
6\rho^2+\nu^2(\kappa_T+\Lambda\kappa-2\kappa^2-6)\ge0.
\]

Near the bolt \(\rho/\nu\to1\), explaining the leading cancellation between \(6G\) and \(3N/2\). On the far tail, \(\Lambda\to8\), and the Hardy/Riccati condition is favorable. The only difficult region is the compact middle zone where \(\rho\) has relaxed but \(\nu\) remains appreciable and \(\Lambda<4\sqrt3\).

---

## 7. Structural obstruction to a universal \(\widehat P\ge1\) estimate

The supplied cell exhibits precisely the mechanism that defeats a zero-right-side near-zone inequality:
\[
\begin{aligned}
12H_{\rm near}+6G_{\rm near}
+\frac32Q_{\delta,\rm near}
&=0.0600916,\\
2\int_{\rm near}\lambda^2d\hat V
-6\int_{\rm near}\nu^2d\hat V
&=-0.0706781.
\end{aligned}
\]
Thus the near region contributes about \(-0.0105865\), while the tail recovers only \(+0.0058777\), leaving
\[
\widehat P-1=-0.0047126.
\]

The mechanism is structural:

1. At the bolt, \(\rho\sim\nu\), so the singular leading terms cancel and there is no strict positive bolt surplus.
2. The transformed charge \(z=\mu\nu\) can vary slowly, keeping \(\lambda=z_T/(2\mu)\) modest while \(-6\nu^2\) accumulates.
3. The conformal factor \(u\) can become close to \(1\), hence \(\rho\) small, before \(\nu\) has unwound.
4. In the middle zone \(\Lambda^2<48\), the Jacobi equation is underdamped/oscillatory; the recorded \(z=\mu\nu\) changes sign there.
5. Hardy positivity begins only after that negative action has accumulated.

The numerical competitors are not exactly \(s=-24\), so they are not rigorous counterexamples within the exact-scalar subclass. However,
\[
12H+\Sigma=0.00332701
\]
differs from \(12H\) by only \(4.75\times10^{-6}\), whereas the observed deficit is \(4.7\times10^{-3}\). Thus any exact-scalar theorem proving \(\widehat P\ge1\) would have to exploit a strong differential restriction from the full \((v,\rho,\delta)\) coupling, not the integrated scalar correction, transport law, or bolt charge alone.

The plausible output of the AK method is therefore either:

- a sharp subunit lower bound determined by the lowest coupled weighted mode, or
- a conditional \(\widehat P\ge1\) theorem under an additional coercive condition controlling the middle-zone duration and the ratio \(\rho/\nu\).

A natural quantitative form is
\[
\mathcal E_{\rm near}\ge -C_{\rm geom}K^2
+\text{interface trace},
\]
where \(C_{\rm geom}\) is the inverse spectral scale of
\[
-(mz_T)_T-12mz
\]
subject to the bolt charge and far-tail boundary condition.

---

## 8. Comparison with \(\mathfrak b_++\phi(q,\eta)\)

The canonical AK identity is genuinely stronger than the attempted correction \(\mathfrak b_++\phi(q,\eta)\).

The latter starts from an exact Hamilton–Jacobi calibration:
\[
\sup(\dot{\mathfrak b}_+-L)=0,
\]
so it has no pointwise slack. Its correction must satisfy
\[
\eta\phi_q+K_{\rm HJ}\phi_\eta+2\phi_\eta^2\le0,
\]
but the hidden-state dependence makes \(K_{\rm HJ}\) change sign, obstructing a universal gain from \((q,\eta)\) alone.

The AK construction escapes this obstruction by adding a genuinely new, nonlocal state: the potential \(\phi\) of the closed self-dual form, equivalently \(u\). It then supplies:

- an exact decomposition with only one negative sector;
- a forced bolt charge;
- exact transport of that charge by \(\lambda\);
- sharp positivity on a terminal CH-scale tail;
- and a compact weighted Sturm–Liouville problem for the remaining region.

Thus it is the stronger route to determining the **actual perpendicular-cell lower bound and near-minimizer geometry**. It does not, on present evidence, provide a route to a universal bound \(\widehat P\ge1\). The unresolved mathematical object is the lowest value of the coupled compact action in §6 under the smooth-bolt and exact-CH boundary conditions—particularly whether the scalar/Yamabe relation removes the negative weighted Nijenhuis mode in the exact \(s=-24\) subclass.