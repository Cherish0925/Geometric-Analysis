# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md",
    "Sessions/S1003A01/workspace/scripts/step28_ak_gap_identity.py",
    "Sessions/S1003A01/workspace/scripts/step28_ak_nu_structure.py",
    "Sessions/S1003A01/workspace/data/step28/gap_lm3_x00.038_X128_d24.json",
    "Sessions/S1003A02/workspace/notes/step34_characteristic_constraint_calculus_and_N_probe.md"
  ]
}
```

## Task

Independently read the peer's canonical almost-Kähler gap identity for diagonal perpendicular exact-CH O(-1) cells. Check the conformal factor and almost-Kähler construction, the exact coefficients and signs in P_hat-1=12H+6G+(3/2)Qdelta+(1/2)QA-(3/2)N+Sigma, the transport lambda=nu_T/2+beta nu and bolt charge law, and the far-field Hardy conclusion. Use the supplied scripts/data as supporting records, but reason through the derivation. State the exact hypotheses, identify any hidden boundary or integrability assumption, and judge whether this identity genuinely supplies a stronger route to the non-round lower bound than b_++phi(q,eta). Develop the most plausible compact near-zone inequality coupling nu, lambda, and log u, or identify a structural countermechanism if the desired >=1 lower bound is implausible.

## Output

# Scientific verification memo

## 1. Exact geometric setting

The identity is valid under a fairly specific collection of hypotheses:

1. On the deleted cell \(0<t<t_+\),
   \[
   g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2,
   \qquad d\sigma_i=2\sigma_j\wedge\sigma_k,
   \]
   with the orientation for which \(e^{0f}+e^{gh}\) is self-dual.

2. The \(h\)-slot collapses at a smooth perpendicular \(O(-1)\) bolt. In the normalization used in the note,
   \[
   a_h=t+O(t^3),\qquad a_f=b+O(t^2),\qquad a_g=b+O(t^2).
   \]

3. The metric equals complex hyperbolic geometry on an open outer collar, with \(f\) the CH circle direction and \(a_g=a_h\) there. Matching only the induced metric at one hypersurface is insufficient for several endpoint cancellations below.

4. The invariant form \(d(\phi\sigma_f)\) descends through the \(O(-1)\) action. Its potential vanishes to second order at the bolt, which is what makes the form smooth there.

5. The relative Chern–Weil identity from Step 27 is used with the blow-up orientation and the stated \(8\pi^2\) normalization.

6. The assertion \(\Sigma=0\) requires the pointwise equation \(s\equiv-24\). An average scalar normalization does not suffice.

The conformally related metric is smooth only on the deleted cell. Near the bolt,
\[
u\sim c\,t^{1/2},\qquad T\sim c'T^{0}t^{3/2},
\]
and more explicitly
\[
A_f,A_g\asymp T^{1/3},\qquad A_h\asymp T.
\]
Thus \(\hat g\) has an anisotropic singular end, not an ordinary smooth almost-Kähler bolt or a standard metric cone. All Chern and integration-by-parts formulas must therefore be interpreted on \([\varepsilon,t_+]\) followed by \(\varepsilon\downarrow0\). The smooth original bolt expansions make the relevant endpoint expressions converge.

## 2. Conformal factor and almost-Kähler construction

In the orthonormal coframe of \(g\),
\[
d(\phi\sigma_f)
 =\frac{\phi'}{a_f}e^{0f}
  +\frac{2\phi}{a_ga_h}e^{gh}.
\]
It is self-dual precisely when
\[
\frac{\phi'}{\phi}=\frac{2a_f}{a_ga_h}.
\]
Normalize \(\phi=a_ga_h\) on the exact CH collar, and put
\[
u^2=\frac{\phi}{a_ga_h},\qquad
dT=u\,dt,\qquad A_i=ua_i.
\]
Then
\[
d(\phi\sigma_f)=2(\hat e^{0f}+\hat e^{gh}).
\]
Consequently \(\Omega=\frac12d(\phi\sigma_f)\) is the standard normalized almost-Kähler form on the deleted cell.

Writing
\[
\mathcal P=A_gA_h,
\]
one has
\[
\mathcal P=u^2a_ga_h=\phi,\qquad
\mathcal P_T=\frac{\phi'}u=2ua_f=2A_f.
\]
Hence
\[
A_f=\frac12\mathcal P_T.
\]
This verifies the AK constraint exactly.

There is a textual inconsistency in `step28_ak_nu_structure.py`: its header says
\[
P_m=A_gA_h=2\phi.
\]
The actual construction gives \(P_m=\phi\), and the code uses \(A_f=P_m'/2\), so the executable algebra follows the correct normalization. Reading \(P_m=2\phi\) literally would instead give the wrong factor \(A_f=P_m'/4\).

At the bolt,
\[
\phi\sim c t^2,\qquad u^2\sim(c/b)t,
\]
which also establishes all needed local integrability:
\[
\nu^2\,d\hat V,\quad \lambda^2\,d\hat V,\quad u'^2W\,dt
\]
are finite even though their pointwise coefficients diverge.

## 3. Nijenhuis scalar and transport law

Set
\[
A_g=\sqrt{\mathcal P}\,e^{q/2},\qquad
A_h=\sqrt{\mathcal P}\,e^{-q/2}.
\]
For
\[
v_i=(A_i)_T-\gamma_i,\qquad
\gamma_i=\frac{A_j^2+A_k^2-A_i^2}{A_jA_k},
\]
the AK relation gives directly
\[
\frac{v_h}{A_h}
 =-\frac12q_T-\frac{2\sinh q}{A_f},\qquad
\frac{v_g}{A_g}
 =\frac12q_T+\frac{2\sinh q}{A_f}.
\]
Thus
\[
\nu:=\frac{v_h}{A_h}=-\frac{v_g}{A_g}
   =-\frac12\left(q_T+\frac{4\sinh q}{A_f}\right).
\]

Using
\[
R^+_{ii}
 =-\frac{(v_i)_T}{2A_i}
  +\frac{-v_i-v_jv_k/2}{A_jA_k},
\]
and subtracting the \(g\) and \(h\) entries, the scalar-curvature subtraction cancels. A direct simplification gives
\[
\lambda:=\frac{\widehat W^+_{gg}-\widehat W^+_{hh}}2
 =\frac12\nu_T+\beta\nu,
\]
where
\[
\beta=-\frac{(A_f)_T}{2A_f}+\frac{2\cosh q}{A_f}.
\]
The coefficient can be seen explicitly from
\[
\frac14\left(\frac{(A_g)_T}{A_g}+
             \frac{(A_h)_T}{A_h}\right)
+\frac{A_g/A_h+A_h/A_g}{2A_f}
-\frac{v_f}{2A_f},
\]
using \((A_gA_h)_T=2A_f\) and
\[
\gamma_f=2\cosh q-\frac{A_f^2}{A_gA_h}.
\]
This independently confirms both the factor \(1/2\) in front of \(\nu_T\) and the signs in \(\beta\).

If
\[
\frac{\mu_T}{\mu}=2\beta,
\]
then
\[
(\mu\nu)_T=2\mu\lambda.
\]
In original variables,
\[
\mu=C\,(ua_f)^{-1}
 \exp\!\left(\int\frac{4\cosh q}{a_f}\,dt\right).
\]

Near the perpendicular bolt,
\[
q=\log(b/t)+O(t^2),\qquad
q_T+\frac{4\sinh q}{A_f}\sim\frac1{ut},
\]
so
\[
\nu\sim-\frac1{2ut}\asymp-t^{-3/2},\qquad
\mu\asymp t^{3/2}.
\]
Therefore
\[
K:=\lim_{t\downarrow0}\mu\nu
\]
exists and is nonzero. Its numerical value depends on the multiplicative normalization of \(\mu\), though nonvanishing does not.

Because the outer collar is exactly CH, \(\nu=0\) there. Integration yields
\[
0-K=2\int_{\rm cell}\mu\lambda\,dT,
\qquad
K=-2\int_{\rm cell}\mu\lambda\,dT.
\]
The sign in the note is correct.

The supplied record strongly supports this integrated law:
\[
K=-0.0174759482,\qquad
2\int\mu\lambda\,dT=0.01747594819,
\]
with reported mismatch \(1.3\times10^{-12}\).

The field `transport_rel_residual_max` in the same JSON is \(2.0\times10^7\), so it does not numerically support the pointwise transport formula. The reason is visible in the script: `tt=np.cumsum(dtdx*wxs)` uses cumulative Gaussian quadrature weights as though they were the physical node coordinates, and then applies `np.gradient` to a quantity behaving like \(t^{-3/2}\). The symbolic derivation above is exact, while that finite-difference evaluator is ill-conditioned and uses an unsuitable coordinate reconstruction.

## 4. Chern identity and the integral of \(\delta\)

Let
\[
w=A_fA_gA_h,\qquad d\hat V=w\,dT=u^4W\,dt.
\]
Direct substitution in the diagonal curvature formulas gives
\[
\kappa-\hat s=6\nu^2,\qquad
\hat s^*=\hat s+2\nu^2,
\]
and hence
\[
\kappa=\hat s^*+4\nu^2.
\]

The exact Stokes primitive is
\[
\hat s^*w
 =\frac d{dT}
 \left(4\mathcal P\cosh q
       -\mathcal P\mathcal P_{TT}
       -\frac12\mathcal P_T^2\right).
\]
At the bolt, \(\mathcal P\sim t^2\), \(q\sim\log(b/t)\), and every term in the bracket tends to zero.

On CH, with \(x=\mathcal P=\sinh^2R\),
\[
q=0,\quad
\mathcal P_T=2\sqrt{x(1+x)},\quad
\mathcal P_{TT}=2(1+2x),
\]
so the bracket is
\[
4x-2x(1+2x)-2x(1+x)=-6x^2.
\]
At the outer endpoint \(x=X\),
\[
\int\hat s^*\,d\hat V=-6X^2.
\]

Also,
\[
w=A_f\mathcal P=\frac12\mathcal P\mathcal P_T
 =\frac14(\mathcal P^2)_T,
\]
hence
\[
\int d\hat V=\frac{X^2}{4}=V_{\rm CH}.
\]
Therefore
\[
\int\hat s^*\,d\hat V=-24V_{\rm CH}.
\]

With
\[
N=4\int\nu^2\,d\hat V,\qquad
\delta=\widehat W^+_{\omega\omega}+4=\frac{\kappa}{6}+4,
\]
one obtains
\[
\begin{aligned}
\int\delta\,d\hat V
&=\frac16\int\hat s^*\,d\hat V
  +\frac23\int\nu^2\,d\hat V
  +4V_{\rm CH}\\
&=-4V_{\rm CH}+\frac N6+4V_{\rm CH}
 =\frac N6.
\end{aligned}
\]
This is the essential coefficient producing the final \(-3N/2\).

## 5. Verification of every coefficient in the gap identity

Let
\[
x=\widehat W^+_{\omega\omega}=\delta-4,\qquad
\lambda=\frac{\widehat W^+_{gg}-\widehat W^+_{hh}}2.
\]
Trace-freeness gives the other two eigenvalues as
\[
-\frac x2+\lambda,\qquad -\frac x2-\lambda.
\]
Thus
\[
|\widehat W^+|^2
 =\frac32x^2+2\lambda^2.
\]
Conformal invariance of \(|W^+|^2dV\) and \(\int d\hat V=V_{\rm CH}\) give
\[
D_+
=24V_{\rm exc}
 +12\int\delta\,d\hat V
 -\frac32Q_\delta-\frac12Q_A,
\]
where
\[
Q_\delta=\int\delta^2d\hat V,\qquad
Q_A=4\int\lambda^2d\hat V.
\]
Since \(\int\delta=N/6\),
\[
D_+=24V_{\rm exc}+2N-\frac32Q_\delta-\frac12Q_A.
\]

For the volume term, conformal scalar curvature gives
\[
\int\hat s\,d\hat V
 =6G+\int su^2W\,dt,
\qquad
G=\int u'^2W\,dt.
\]
The bolt contribution vanishes because
\[
uu'W=O(t),
\]
and the CH collar gives \(u'=0\) at the other endpoint. Since
\[
\int\hat s\,d\hat V
 =-24V_{\rm CH}-\frac N2,
\]
and
\[
H=\int(u^2-1)^2W\,dt,
\]
elementary algebra yields
\[
V_{\rm exc}
 =H+\frac G2+\frac N{24}
  +\frac1{12}\int(s+24)u^2W\,dt.
\]

Inserting these expressions into
\[
1-\widehat P=D_+-36V_{\rm exc}-S_{\rm exc},
\qquad
S_{\rm exc}=\int\left(\frac{s^2}{48}-12\right)W\,dt,
\]
gives exactly
\[
\boxed{
\widehat P-1
 =12H+6G+\frac32Q_\delta+\frac12Q_A-\frac32N+\Sigma
}
\]
with
\[
\Sigma
 =\int(s+24)(u^2-1)W\,dt
  +\int\frac{(s+24)^2}{48}W\,dt.
\]

A useful stronger presentation is
\[
\boxed{
12H+\Sigma
 =\frac1{48}\int(s+24u^2)^2W\,dt.
}
\]
Hence the identity can also be written
\[
\boxed{
\widehat P-1
 =6G+\frac32Q_\delta+\frac12Q_A-\frac32N
  +\frac1{48}\int(s+24u^2)^2W\,dt.
}
\]
This form makes the sign structure transparent for arbitrary scalar curvature. When \(s\equiv-24\), the final square is \(12H\).

The \(x_0=0.038\) record gives an identity mismatch \(2.1\times10^{-10}\), a curvature relation mismatch \(3.6\times10^{-14}\), and agreement in
\[
6G-\frac32N
 =6\int u^2a_fv_gv_h\,dt
\]
to displayed machine precision. These are strong numerical confirmations of the coefficients and signs.

## 6. Far-field Hardy estimate

From the transport equation,
\[
\nu_T=2\lambda-2\beta\nu.
\]
Therefore
\[
(\nu^2w)_T
 =4\nu\lambda w+\Lambda\nu^2w,
\qquad
\Lambda=\frac{w_T}{w}-4\beta.
\]
On a terminal interval \([T_0,T_+]\) ending in the exact CH collar, \(\nu(T_+)=0\). Put
\[
A=\int_{T_0}^{T_+}\nu^2w\,dT,\qquad
L=\int_{T_0}^{T_+}\lambda^2w\,dT.
\]
Integration gives
\[
\int\Lambda\nu^2w\,dT+\nu(T_0)^2w(T_0)
 =-4\int\nu\lambda w\,dT.
\]
If \(\Lambda\ge c>0\) throughout that terminal interval, then
\[
cA+\nu(T_0)^2w(T_0)\le4\sqrt{AL},
\]
and hence
\[
A\le\frac{16}{c^2}L.
\]
For \(c\ge4\sqrt3\),
\[
2L-6A\ge0.
\]

This conclusion applies to a terminal interval reaching a point where \(\nu=0\); it is not a purely local statement on an arbitrary subset where \(\Lambda\ge4\sqrt3\).

On exact CH,
\[
\Lambda=\frac{8x-3}{\sqrt{x(1+x)}}.
\]
Solving \(\Lambda=4\sqrt3\) with positive numerator gives
\[
x=3+\frac34\sqrt{15}\approx5.9047.
\]
The threshold and the limiting value \(\Lambda\to8\) are correct.

For the supplied \(x_0=0.038\) cell, the sampled last crossing is \(x_*\approx5.9488\), and
\[
2\int_{\rm tail}\lambda^2d\hat V
 -6\int_{\rm tail}\nu^2d\hat V
 =0.0058777.
\]
This verifies the expected positive tail contribution for that record. The location \(x_*\) is numerical and is not uniform over all admissible cells without further geometric control.

## 7. The compact near-zone action

For the exact scalar equation \(s=-24\), introduce
\[
v=u^{-1},\qquad
\rho=(\log v)_T,\qquad
m=(\log w)_T.
\]
Changing from \(t\) to \(T\) gives
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
give the exact radial relation
\[
\boxed{
\delta
 =\rho_T+\rho^2+m\rho+\nu^2+4(1-v^2).
}
\]
Consequently the whole exact-scalar gap is the one-dimensional action
\[
\boxed{
\begin{aligned}
\widehat P-1
=\int w\Big[
&6\rho^2
 +\frac12(\nu_T+2\beta\nu)^2
 -6\nu^2\\
&+\frac32\bigl(
 \rho_T+\rho^2+m\rho+\nu^2+4(1-v^2)
 \bigr)^2
 +12(v^2-1)^2
\Big]\,dT .
\end{aligned}
}
\]
This is the most useful compact near-zone formulation: it couples the Nijenhuis field, the transport curvature, the conformal logarithmic derivative, and the scalar equation without discarding any coefficient.

There is also a sharp weighted Sturm–Liouville form. Put
\[
z=\mu\nu,\qquad r_0=\frac{w}{\mu^2}.
\]
Then
\[
\boxed{
2\int\lambda^2w\,dT-6\int\nu^2w\,dT
 =\int r_0\left(\frac12z_T^2-6z^2\right)dT.
}
\]
For any \(C^1\) multiplier \(p\),
\[
\begin{aligned}
\int_I r_0\left(\frac12z_T^2-6z^2\right)dT
={}&\frac12\int_Ir_0(z_T+pz)^2\,dT
-\frac12[r_0pz^2]_{\partial I}\\
&+\frac12\int_Ir_0
\left(
p_T+\frac{(r_0)_T}{r_0}p-p^2-12
\right)z^2\,dT.
\end{aligned}
\]
Here
\[
\frac{(r_0)_T}{r_0}=\Lambda.
\]
The optimal multiplier solves the associated Riccati equation
\[
p_T+\Lambda p-p^2-12=0.
\]
This identifies the exact compact near-zone problem as a weighted ground-state problem coupled to the \((v,\rho,\delta)\) equation above.

## 8. Structural mechanism permitting \(\widehat P<1\)

A universal near-zone estimate with right side zero is not supported by the supplied cell. For \(x_0=0.038\), the decomposition at the last Hardy crossing is
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
Thus the compact region contributes approximately
\[
-0.0105865,
\]
while the terminal region returns only
\[
0.0058786.
\]
Together with \(\Sigma=-4.75\times10^{-6}\), this gives
\[
\widehat P-1=-0.00471263.
\]

The mechanism is coherent with the equations:

* At the bolt, \(\rho\sim\nu\), so \(6G\) cancels \(3N/2\) to leading order. The forced bolt charge therefore creates no strict positive surplus locally.
* The transformed charge \(z=\mu\nu\) can remain nearly constant through part of the compact region. Then \(\lambda=z_T/(2\mu)\) is modest while the \(-6\nu^2\) term continues to accumulate.
* Meanwhile \(u\) approaches \(1\), so \(\rho\) becomes small before \(\nu\) has fully unwound.
* The vanishing volume weight near the singular AK end permits this transition with modest \(H\) and \(Q_\delta\) payments.
* Once \(\Lambda\) becomes sufficiently large, the Hardy estimate forces a positive return, but the recorded return is smaller than the earlier decrease.

This is a genuine structural countermechanism to a direct proof of \(\widehat P\ge1\) from transport plus bolt charge alone.

The numerical cell does not have \(s\equiv-24\), so it is not a rigorous counterexample to the exact-scalar subclass. Still,
\[
12H+\Sigma=0.00332701,\qquad
12H=0.00333176,
\]
so the scalar-square contribution already differs from the exact-scalar expression by only \(4.75\times10^{-6}\), far below the observed \(4.7\times10^{-3}\) deficit. An exact-scalar positivity theorem, if true, would therefore have to use the full differential relation for \(\delta\) and \(\rho\), not merely the integrated scalar correction.

A mathematically plausible quantitative near estimate has the form
\[
\mathcal E_{\rm near}
 \ge -C\,K^2+\text{terminal trace terms},
\]
with \(C\) determined by the lowest weighted mode of
\[
-(r_0z_T)_T-12r_0z.
\]
The data indicate that the sharper zero-right-side version is incompatible with the ambient smooth diagonal class.

## 9. Scientific assessment relative to \(b_++\phi(q,\eta)\)

The almost-Kähler identity is substantially stronger in information content than \(b_++\phi(q,\eta)\):

* \(b_+\) is already an exact pointwise Hamilton–Jacobi calibration, so a correction depending only on \((q,\eta)\) has no unused pointwise margin.
* The AK construction introduces a nonlocal geometric state \(u\), the forced bolt charge \(K\), the Nijenhuis field \(\nu\), and the curvature transport field \(\lambda\).
* It gives a complete square decomposition of every contribution except the single \(-3N/2\) term.
* It proves positivity of the entire terminal Nijenhuis sector past an explicit CH scale.
* It reduces the remaining issue to a compact weighted variational problem with an exact scalar-coupling equation.

It therefore gives a stronger route to a sharp non-round estimate or to the true subunit optimum. It does not presently supply \(\widehat P\ge1\): the compact action possesses a real charge-storage mechanism, and the supplied metric realizes it numerically. For the exact \(s=-24\) subclass, the unresolved mathematical substance is whether the coupled \((v,\rho,\delta)\) equation removes that mode; transport and bolt asymptotics alone do not.