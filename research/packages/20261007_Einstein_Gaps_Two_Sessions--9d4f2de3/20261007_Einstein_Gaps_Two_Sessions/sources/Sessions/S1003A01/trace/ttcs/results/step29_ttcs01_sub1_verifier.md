# TTCS Independent Branch Record

```json
{
  "step_id": 29,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md",
    "Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md",
    "Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md",
    "Sessions/S1003A01/workspace/scripts/step29_ak_exterior_bridge.py",
    "Sessions/S1003A01/workspace/scripts/step29_local_AK_flux.py",
    "Sessions/S1003A01/workspace/scripts/step29_capacity_contact.py",
    "Sessions/S1003A01/workspace/scripts/exterior_null_line.py",
    "Sessions/S1003A01/workspace/data/step29/ak_exterior_bridge_x0038_X128_rho10.json",
    "Sessions/S1003A01/workspace/data/step29/local_AK_flux_x0038_X128.json",
    "Sessions/S1003A01/workspace/data/step29/capacity_x0015_X256.json",
    "Sessions/S1003A01/workspace/data/step29/capacity_x0038_X128.json",
    "Sessions/S1003A01/workspace/data/step29/capacity_x007_X256.json"
  ]
}
```

## Task

Independently verify the Step-29 mathematical bridge between the canonical almost-Kähler action and the already solved antisymmetric complex-hyperbolic exterior response. Read the theory note and all three scripts/data. Check: (i) the nonlinear local formula Phat[t0,t1]=int L_AK+B(t1)-B(t0), including B=b_+-3F-9P^2-6Wuu', endpoint values and normalization; (ii) the exact linear formulas q=theta, v_-=f_-w, nu=-v_-/(2sqrt x), lambda, and L_AK=mu w'^2+(Aw^2)' with every coefficient/sign; (iii) that the Einstein mass mode has zero raw action and nonzero AK tail canceled by the interface, so the Step-19 mass null line is preserved and no tail action may be counted twice; (iv) that the numerical profile evaluations actually test those equations and that the reported raw/AK/flux numbers follow from the supplied artifacts; (v) the contact identity/capacity computation, especially whether the linear two-constraint minimizer and its interpretation (26-39% of observed QA/2, frozen-profile only) are correct. Identify any mathematical or code error and state the strongest corrected result and implications for the all-metric Einstein-gap programme. Do not propose a separate tail cost unless the bridge is false.

## Output

# Independent verification memo

## Main result

The Step-29 bridge is mathematically sound, with one important typographical correction:

\[
\boxed{\lambda
=-\frac{x(1+x)w'+(2-3x)w}{2(1+x)^3}}
\]

when \(w'=dw/dx\). The note displays \(x^2(1+x)w'\), which is incorrect. The symbolic script and JSON artifact use the corrected \(x(1+x)w'\) coefficient, and the stated identity with \(\mu\) and \(A\) requires this corrected formula.

Apart from that typo, the nonlinear local identity, the CH quadratic bridge, preservation of the Einstein mass null line, and the frozen-profile capacity calculation are correct. One numerical-description issue remains: the quantities in `step29_ak_exterior_bridge.py` are CH quadratic reconstructions from the nonlinear profile, not the exact nonlinear raw and AK tail integrals. The exact nonlinear quantities are instead those produced by `step29_local_AK_flux.py`.

---

## 1. Nonlinear local AK identity

Use
\[
d\widehat V=u^4W\,dt,\qquad
\delta=\widehat W^+_{\omega\omega}+4,\qquad
\lambda=\frac{\widehat W^+_{gg}-\widehat W^+_{hh}}2.
\]

In the diagonal orbit normalization, the Cartan transgression is
\[
d\widehat P
=db_++\left(|W^+|^2+\frac{s^2}{48}\right)W\,dt.
\]

The diagonal Weyl decomposition gives
\[
|W^+|^2W\,dt
=
\left[\frac32(\delta-4)^2+2\lambda^2\right]d\widehat V.
\]

The Chern–Stokes and conformal scalar relations are
\[
d\mathcal F=(\widehat s+2\nu^2)d\widehat V,
\]
\[
\widehat s\,d\widehat V
=
\left(su^2W+6Wu'^2\right)dt-6\,d(Wuu'),
\]
while the conformal scalar/Weyl relation gives
\[
\delta\,d\widehat V
=
\frac16\,d\mathcal F+\frac23\nu^2d\widehat V+4d\widehat V.
\]

Finally,
\[
d\!\left(\frac{\mathcal P^2}{4}\right)=d\widehat V.
\]

Substituting these four identities yields
\[
d\widehat P=L_{AK}\,dt+dB,
\]
where
\[
L_{AK}
=
12W\left(u^2+\frac{s}{24}\right)^2
+6Wu'^2
+\frac32\delta^2\frac{d\widehat V}{dt}
+2\lambda^2\frac{d\widehat V}{dt}
-6\nu^2\frac{d\widehat V}{dt},
\]
and
\[
\boxed{
B=b_+-3\mathcal F-9\mathcal P^2-6Wuu'.
}
\]

Thus
\[
\boxed{
\widehat P[t_0,t_1]
=
\int_{t_0}^{t_1}L_{AK}\,dt+B(t_1)-B(t_0).
}
\]

All coefficients and signs in this nonlinear formula are correct.

### Endpoint values

On exact CH,
\[
A_f=\sqrt{x(1+x)},\qquad A_g=A_h=\sqrt x,\qquad
\mathcal P=x,\qquad q=0,\qquad u=1.
\]
A direct calculation gives
\[
\mathcal F=-6x^2,\qquad b_+=2-9x^2,\qquad Wuu'=0,
\]
hence
\[
B=(2-9x^2)-3(-6x^2)-9x^2=2.
\]

At a smooth perpendicular bolt,
\[
\mathcal P\to0,\qquad \mathcal F\to0,\qquad Wuu'\to0,
\]
and the smooth-bolt spin data give \(b_+\to1\). Therefore
\[
B_{\rm bolt}=1,\qquad B_{\rm CH}=2,
\]
so the whole-cell relation is
\[
\widehat P=1+\int L_{AK}\,dt.
\]

This also confirms the normalization \(\widehat P=P/(8\pi^2)\), with threshold value \(1\).

---

## 2. Exact linear CH bridge

On CH,
\[
\frac{dT}{dx}=\frac1{2\sqrt{x(1+x)}},
\qquad
\frac{d\widehat V}{dx}=\frac x2.
\]

With
\[
q=\theta,\qquad
v_-=f_-w,\qquad
f_-=\frac{x}{(1+x)^{5/2}},\qquad
k=\left(\frac{x}{1+x}\right)^2,
\]
and
\[
(k\theta)'=\frac12f_-^2w,
\]
the AK Nijenhuis scalar satisfies
\[
\nu
=-\frac12\left(q_T+\frac{4q}{A_f}\right)
=-\sqrt{x(1+x)}
\left(\theta'+\frac{2\theta}{x(1+x)}\right).
\]
Using the torsion equation,
\[
\boxed{
\nu=-\frac{\sqrt x}{2(1+x)^{5/2}}w
=-\frac{v_-}{2\sqrt x}.
}
\]

On CH,
\[
\beta=-\frac{(A_f)_T}{2A_f}+\frac2{A_f}
=\frac{3-2x}{2\sqrt{x(1+x)}}.
\]
Consequently
\[
\lambda=\frac12\nu_T+\beta\nu
\]
becomes
\[
\boxed{
\lambda
=-\frac{x(1+x)w'+(2-3x)w}{2(1+x)^3}.
}
\]

The extra factor \(x\) in the displayed Step-29 note is a typo. This is decisively seen from the \((w')^2\) coefficient: with the corrected formula,
\[
x\lambda^2\big|_{(w')^2}
=
\frac{x^3}{4(1+x)^4}(w')^2
=\mu(w')^2,
\]
whereas the displayed \(x^2(1+x)w'\) would produce the wrong power of \(x\).

With
\[
\mu=\frac{x^3}{4(1+x)^4},
\qquad
A(x)=-\frac{x^2(3x-2)}{4(1+x)^5},
\]
direct expansion gives
\[
\boxed{
\frac x2(2\lambda^2-6\nu^2)
=
\mu(w')^2+\frac d{dx}\bigl(Aw^2\bigr).
}
\]

The SymPy residual in `ak_exterior_bridge_x0038_X128_rho10.json` is exactly zero, and its printed \(\lambda\) is the corrected one:
\[
-\frac{x^2w'+xw'+(2-3x)w}{2(1+x)^3}
=
-\frac{x(1+x)w'+(2-3x)w}{2(1+x)^3}.
\]

---

## 3. Einstein mass mode and the Step-19 null line

For the decaying antisymmetric Einstein mass mode,
\[
w\equiv c,\qquad v_-=cf_-,
\]
so
\[
\int_\rho^\infty\mu(w')^2dx=0.
\]

Its \(\theta\) is
\[
\theta
=-c\,\frac{6x^2+4x+1}{24x^2(1+x)^2}.
\]
Since
\[
k\theta=-\frac c2G(x),\qquad
G(x)=\frac{6x^2+4x+1}{12(1+x)^4},
\]
the Step-19 mismatch is
\[
\delta=-2k(\rho)\Theta-w_0G(\rho)=0.
\]
Thus the mass mode lies exactly on the Step-19 null line.

For constant \(w=c\),
\[
\int_\rho^\infty L_{AK}^{(2)}dx
=
[A(x)c^2]_\rho^\infty
=-A(\rho)c^2,
\]
because \(A(x)\to0\). The interface contribution is \(A(\rho)c^2\), so
\[
\int_\rho^\infty L_{AK}^{(2)}dx+A(\rho)c^2=0.
\]

At \(\rho=10\), \(c=1\),
\[
-A(10)=0.004346449261414086,
\]
exactly matching the JSON artifact. The nonzero AK tail is therefore a transgression contribution, not a second Ricci cost.

More generally, after minimizing the raw CH functional,
\[
E_{\rm ext}=\frac{\delta^2}{I(\rho)},
\]
the equivalent AK representation is
\[
\boxed{
\int_\rho^\infty L_{AK}^{(2)}dx
=
\frac{\delta^2}{I(\rho)}-A(\rho)w_0^2.
}
\]
Adding both this AK integral and \(E_{\rm ext}\) as independent prices would count the same exterior response twice and would incorrectly assign a positive price to the Einstein mass mode.

---

## 4. Numerical artifacts

### Exact nonlinear local evaluation

`step29_local_AK_flux.py` computes:

* the full trace-free Ricci density \(W|\operatorname{Ric}^{\circ}|^2/4\);
* every term in the all-scalar \(L_{AK}\);
* \(\mathcal P,u,\mathcal F,b_+\), and \(B\);
* the local identity on multiple terminal intervals.

At \(X=128\),
\[
b_+=-147453.99999999948,\quad
\mathcal F=-98303.9999999997,\quad
\mathcal P=127.99999999999984,
\]
and
\[
B=1.9999999999417923.
\]
This is the exact CH cancellation
\[
(2-9x^2)-3(-6x^2)-9x^2=2
\]
resolved to approximately \(6\times10^{-11}\).

At entry \(x=10\), the exact nonlinear values are
\[
\widehat P_{\rm tail}
=1.5309026957446828\times10^{-4},
\]
\[
\int L_{AK}
=4.508652067061618\times10^{-3},
\]
\[
B_{\rm entry}-B_{\rm end}
=4.355561855533542\times10^{-3}.
\]
They satisfy
\[
\widehat P_{\rm tail}
=
\int L_{AK}+B_{\rm end}-B_{\rm entry}
\]
with residual
\[
5.80\times10^{-11}.
\]

The interface conversion is
\[
\frac{0.00435556186}{0.00450865207}=0.9660,
\]
so it accounts for \(96.60\%\) of the positive AK tail integral at this section.

All listed sections \(x=0.1,\ldots,50\) reproduce the note’s table, with residuals between approximately \(5.4\times10^{-11}\) and \(6.3\times10^{-11}\).

### Linear CH reconstruction on the nonlinear profile

`step29_ak_exterior_bridge.py` instead reconstructs \(w\) from the actual \(q\) and inserts it into the exact CH quadratic formulas. At \(x=10\), it reports
\[
E_{\rm CH,quad}=1.474972096527144\times10^{-4},
\]
\[
\int L_{AK,\rm CH}^{(2)}
=4.568947930143581\times10^{-3},
\]
\[
-A(10)w(10)^2
=4.421450571117447\times10^{-3}.
\]

These are not the exact nonlinear tail quantities above. Their differences are

\[
E_{\rm exact}-E_{\rm CH,quad}
=5.59306\times10^{-6},
\]
\[
L_{AK,\rm CH}^{(2)}-L_{AK,\rm exact}
=6.02959\times10^{-5},
\]
\[
(-Aw^2)-\bigl(B_{\rm entry}-B_{\rm end}\bigr)
=6.58887\times10^{-5}.
\]

The \(1.49\times10^{-10}\) bridge residual verifies quadrature and automatic differentiation for the CH quadratic identity. It does not measure the discrepancy between the nonlinear metric and its CH quadratic reconstruction.

The finite-\(X\) minimizer calculation is nevertheless correct within that quadratic model:
\[
E_{\rm ext}^{X}
=1.4357009992111612\times10^{-4},
\]
and
\[
E_{\rm ext}^{X}-A(10)w_0^2
=4.565020671038563\times10^{-3},
\]
which differs from the reconstructed profile’s quadratic AK value by
\[
3.92726\times10^{-6}.
\]

Thus the code is mathematically consistent; the note should label the Section-3 quantities as CH quadratic reconstructions rather than exact raw and exact AK tail integrals.

---

## 5. Contact identity and frozen-profile capacities

Let
\[
y=\tanh(q/2).
\]
Since
\[
q_T=\frac{2y_T}{1-y^2},
\qquad
\sinh q=\frac{2y}{1-y^2},
\]
the definition
\[
\nu=-\frac12\left(q_T+\frac{4\sinh q}{A_f}\right)
\]
is exactly equivalent to
\[
\boxed{
y_T+\frac4{A_f}y=-\nu(1-y^2).
}
\]

For \(\eta_T=4\eta/A_f\),
\[
\boxed{
(\eta y)_T=-\eta\nu(1-y^2).
}
\]
On linear CH, \(\eta\) is proportional to
\[
k=\left(\frac{x}{1+x}\right)^2,
\]
and this equation reduces exactly to
\[
(k\theta)'=\frac12f_-v_-.
\]
It is therefore the existing torsion/reconstruction equation in AK variables, not an additional independent exterior equation.

### Transport energy

With
\[
h=\mu\nu,\qquad
\rho=\frac{\widehat W}{\mu^2},
\qquad
\frac{\mu_T}{\mu}=2\beta,
\]
the transport equation gives
\[
h_T=\mu(\nu_T+2\beta\nu)=2\mu\lambda.
\]
Hence
\[
\boxed{
\frac{Q_A}{2}
=
\frac12\int\rho h_T^2\,dT.
}
\]

For fixed endpoint values, put
\[
R=\int\frac{dT}{\rho},\qquad
\Delta h=h_1-h_0.
\]
The endpoint minimizer has energy
\[
E_1=\frac{(\Delta h)^2}{2R}.
\]

For the additional frozen moment
\[
\int c(T)h(T)\,dT=M,
\qquad
c=\frac{\eta(1-y^2)}{\mu},
\]
let \(h_{\rm lin}\) be the endpoint minimizer and let \(z\) solve
\[
-(\rho z_T)_T=c,\qquad z(T_0)=z(T_1)=0.
\]
Then
\[
\Gamma=\int cz\,dT=\int\rho z_T^2\,dT,
\]
and the constrained minimum is
\[
\boxed{
E_2
=
E_1+
\frac{\left(M-\int ch_{\rm lin}\,dT\right)^2}{2\Gamma}.
}
\]
This is exactly the formula implemented by `step29_capacity_contact.py`; the signs and the factor \(1/2\) are correct.

The supplied values are:

| \(x_0\) | observed \(Q_A/2\) | endpoints | endpoints + contact | fractions |
|---:|---:|---:|---:|---:|
| .015 | .00704682 | .00102980 | .00185791 | .1461, .2637 |
| .038 | .03285659 | .00585492 | .01066191 | .1782, .3245 |
| .07 | .08011336 | .01675474 | .03112443 | .2091, .3885 |

The independent reconstruction
\[
\frac12\int\rho h_T^2dT
\]
agrees with direct \(Q_A/2\) to about \(1.2\times10^{-8}\), \(4.0\times10^{-8}\), and \(1.0\times10^{-7}\), respectively. The contact residuals are \(6.1\times10^{-7}\)–\(1.2\times10^{-6}\), and the recorded maxima of \(\nu\) are far larger than these residuals, supporting the reported sign changes.

The \(26\%\)–\(39\%\) interpretation is correct: after freezing \(\rho,c\), the endpoint data plus one scalar contact moment force only that fraction of the observed transport energy. Since \(\rho,c,M\) are all generated by the same metric and change when the metric changes, these percentages do not furnish a uniform estimate over diagonal competitors.

---

## 6. Strongest corrected conclusion

For smooth diagonal perpendicular exact-CH cells, the two exterior descriptions are the same functional written with different interface primitives:

\[
\boxed{
\widehat P[t_0,t_1]
=
\int_{t_0}^{t_1}L_{AK}\,dt
+B(t_1)-B(t_0).
}
\]

In the linear antisymmetric CH sector,

\[
\boxed{
L_{AK}^{(2)}
=
\mu(w')^2+(Aw^2)',
\qquad
\lambda
=-\frac{x(1+x)w'+(2-3x)w}{2(1+x)^3}.
}
\]

Therefore the solved Step-19 response
\[
E_{\rm ext}=\delta^2/I(\rho)
\]
is the raw terminal value, while the AK terminal integral is that same value shifted by the explicit interface primitive. The Einstein mass direction remains exactly null.

This resolves the representation issue but does not determine an unrestricted all-metric lower value for \(\alpha(M)\). The supplied identity is established for the diagonal perpendicular family; the explicit response is a CH quadratic result; and the capacity coefficients are endogenous to each profile. For the unrestricted problem, the supplied material still lacks a uniform nonlinear exterior estimate for traces not close to CH and a nonsymmetric treatment of the relative self-dual form, its zero set, and the additional \(W_2^+\) sector. The cited certified upper construction is unaffected by the bridge.