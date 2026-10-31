# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 29,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step29_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step29_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the Step-29 mathematical bridge between the canonical almost-Kähler action and the already solved antisymmetric complex-hyperbolic exterior response. Read the theory note and all three scripts/data. Check: (i) the nonlinear local formula Phat[t0,t1]=int L_AK+B(t1)-B(t0), including B=b_+-3F-9P^2-6Wuu', endpoint values and normalization; (ii) the exact linear formulas q=theta, v_-=f_-w, nu=-v_-/(2sqrt x), lambda, and L_AK=mu w'^2+(Aw^2)' with every coefficient/sign; (iii) that the Einstein mass mode has zero raw action and nonzero AK tail canceled by the interface, so the Step-19 mass null line is preserved and no tail action may be counted twice; (iv) that the numerical profile evaluations actually test those equations and that the reported raw/AK/flux numbers follow from the supplied artifacts; (v) the contact identity/capacity computation, especially whether the linear two-constraint minimizer and its interpretation (26-39% of observed QA/2, frozen-profile only) are correct. Identify any mathematical or code error and state the strongest corrected result and implications for the all-metric Einstein-gap programme. Do not propose a separate tail cost unless the bridge is false.

## Integrated Scientific Memo

# Step-29 verification memo

## Verdict

The Step-29 bridge is valid, with two corrections/clarifications:

1. **Displayed coefficient error in the note.** The correct linear formula is
   \[
   \boxed{\lambda
   =-\frac{x(1+x)w'+(2-3x)w}{2(1+x)^3}},
   \qquad w'=\frac{dw}{dx}.
   \]
   The note incorrectly prints \(x^2(1+x)w'\). The script and JSON use the correct \(x(1+x)w'\), so the computations are unaffected.

2. **Numerical labeling issue.** The values produced by `step29_ak_exterior_bridge.py` are evaluations of the **CH quadratic bridge reconstructed from the nonlinear profile**, not the exact nonlinear raw and AK tail actions. The latter are computed by `step29_local_AK_flux.py`. This distinction changes no conclusion, but it should be stated explicitly.

Subject to these corrections, the nonlinear boundary identity, the linear CH bridge, preservation of the Einstein mass null line, and the frozen-profile two-constraint capacity calculation are correct. In particular, **no separate positive tail cost should be added**.

---

## 1. Nonlinear local identity

With
\[
\mathcal F
=4\mathcal P\cosh q-\mathcal P\mathcal P_{TT}
-\frac12\mathcal P_T^2,
\]
the asserted density is
\[
L_{AK}
=
12W\left(u^2+\frac{s}{24}\right)^2
+6Wu'^2
+\frac32\delta^2\frac{d\widehat V}{dt}
+2\lambda^2\frac{d\widehat V}{dt}
-6\nu^2\frac{d\widehat V}{dt}.
\]
The exact local identity is
\[
\boxed{
\widehat P[t_0,t_1]
=\int_{t_0}^{t_1}L_{AK}\,dt+B(t_1)-B(t_0),
}
\]
where
\[
\boxed{
B=b_+-3\mathcal F-9\mathcal P^2-6Wuu'.
}
\]

The coefficients and signs follow from combining:

\[
|W^+|^2W\,dt
=
\left[\frac32(\delta-4)^2+2\lambda^2\right]d\widehat V,
\]
\[
d\mathcal F=(\widehat s+2\nu^2)d\widehat V,
\]
\[
\widehat s\,d\widehat V
=
(su^2W+6Wu'^2)\,dt-6\,d(Wuu'),
\]
and
\[
d\!\left(\frac{\mathcal P^2}{4}\right)=d\widehat V.
\]
After completing the scalar square, the remaining exact derivative is precisely \(dB\).

### Endpoint normalization

On exact CH,
\[
u=1,\quad q=0,\quad \mathcal P=x,\quad Wuu'=0,
\]
and direct substitution gives
\[
\mathcal F=-6x^2,\qquad b_+=2-9x^2.
\]
Therefore
\[
B=(2-9x^2)-3(-6x^2)-9x^2=2.
\]

At the smooth perpendicular bolt,
\[
\mathcal P,\mathcal F,Wuu'\longrightarrow0,\qquad b_+\longrightarrow1,
\]
so
\[
B_{\rm bolt}=1,\qquad B_{\rm CH}=2.
\]
Hence, in the normalization \(\widehat P=P/(8\pi^2)\),
\[
\boxed{\widehat P=1+\int L_{AK}\,dt}
\]
for a complete smooth cell, while on a terminal interval ending in CH,
\[
\boxed{
\int_{\rm tail}L_{AK}
=\widehat P_{\rm tail}+B(\mathrm{entry})-2.
}
\]

Thus the local AK integral is not itself the raw Ricci action.

---

## 2. Exact linear CH bridge

Use the Step-19 variables
\[
q=\theta,\qquad v_-=f_-w,\qquad
f_-=\frac{x}{(1+x)^{5/2}},\qquad
k=\left(\frac{x}{1+x}\right)^2,
\]
with
\[
(k\theta)'=\frac12f_-^2w.
\]

On CH,
\[
\frac{dT}{dx}=\frac1{2\sqrt{x(1+x)}},
\qquad
\frac{d\widehat V}{dx}=\frac x2.
\]

From
\[
\nu=-\frac12\left(q_T+\frac{4\sinh q}{A_f}\right)
\]
at linear order, the torsion relation gives
\[
\boxed{
\nu=-\frac{v_-}{2\sqrt x}
=-\frac{\sqrt x}{2(1+x)^{5/2}}\,w.
}
\]

Also
\[
\beta=-\frac{(A_f)_T}{2A_f}+\frac2{A_f}
=\frac{3-2x}{2\sqrt{x(1+x)}}.
\]
Using \(\lambda=\frac12\nu_T+\beta\nu\), one obtains
\[
\boxed{
\lambda
=-\frac{x(1+x)w'+(2-3x)w}{2(1+x)^3}.
}
\]

This is the formula implemented by SymPy:
\[
-\frac{(x^2+x)w'+(2-3x)w}{2(1+x)^3}.
\]
The note’s \(x^2(1+x)w'\) is therefore a typographical error. It cannot be correct because it would give the wrong coefficient of \((w')^2\).

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
\mu(w')^2+\frac d{dx}\bigl(A(x)w^2\bigr).
}
\]
The supplied symbolic residual is exactly zero.

---

## 3. Einstein mass mode and null-line preservation

For the decaying antisymmetric Einstein mass mode,
\[
w\equiv c,\qquad v_-=cf_-,
\]
so its raw quadratic action vanishes:
\[
\int_\rho^\infty\mu(w')^2\,dx=0.
\]

Its corresponding \(\theta\) satisfies
\[
k\theta=-\frac c2G(x),\qquad
G(x)=\frac{6x^2+4x+1}{12(1+x)^4}.
\]
Therefore the Step-19 mismatch
\[
\delta=-2k(\rho)\Theta-w_0G(\rho)
\]
vanishes exactly. The Einstein mass mode remains the null line of
\[
E_{\rm ext}=\frac{\delta^2}{I(\rho)}.
\]

Nevertheless, its AK tail integral is nonzero:
\[
\int_\rho^\infty L_{AK}^{(2)}\,dx
=[Aw^2]_\rho^\infty=-A(\rho)c^2.
\]
This is canceled by the entrance primitive \(A(\rho)c^2\). At \(\rho=10\), \(c=1\),
\[
-A(10)=0.004346449261414086,
\]
and the artifact records
\[
\text{AK tail}+\text{entry interface}=0.
\]

For general entrance data,
\[
\boxed{
\int_\rho^\infty L_{AK}^{(2)}\,dx
=
\frac{\delta^2}{I(\rho)}-A(\rho)w_0^2.
}
\]
Thus the AK terminal integral and the Step-19 raw response are the same exterior functional in different transgression conventions. Counting both as independent positive costs would double-count the exterior and would falsely charge the Einstein mass mode.

---

## 4. Numerical verification and the exact meaning of the reported numbers

### Exact nonlinear evaluation

`step29_local_AK_flux.py` evaluates the full nonlinear trace-free Ricci density, all terms of \(L_{AK}\), and the full boundary observable \(B\).

At \(X=128\),
\[
B=1.9999999999417923,
\]
despite the individually large values
\[
b_+=-147453.99999999948,\quad
\mathcal F=-98303.9999999997,\quad
\mathcal P\simeq128.
\]
This confirms the exact CH cancellation to \(5.8\times10^{-11}\).

At \(x=10\), the exact nonlinear values are
\[
\widehat P_{\rm tail}
=1.5309026957\times10^{-4},
\]
\[
\int L_{AK}
=4.5086520671\times10^{-3},
\]
\[
B(\mathrm{entry})-B(\mathrm{end})
=4.3555618555\times10^{-3}.
\]
They obey
\[
\widehat P_{\rm tail}
=
\int L_{AK}+B_{\rm end}-B_{\rm entry}
\]
with residual \(5.80\times10^{-11}\).

The interface accounts for
\[
\frac{0.00435556186}{0.00450865207}\approx0.9660,
\]
or \(96.6\%\), of the positive AK tail integral at \(x=10\). All nine reported sections reproduce the local identity with residuals \(5.4\times10^{-11}\)–\(6.3\times10^{-11}\).

### CH quadratic reconstruction

`step29_ak_exterior_bridge.py` reconstructs \(w\) from the nonlinear profile and inserts it into the exact CH quadratic formulas. It obtains
\[
E_{\rm raw,CH}^{(2)}
=1.4749720965\times10^{-4},
\]
\[
E_{\rm AK,CH}^{(2)}
=4.5689479301\times10^{-3},
\]
\[
[Aw^2]_{10}^{128}
=4.4214505711\times10^{-3},
\]
with bridge residual \(1.49\times10^{-10}\).

These are not identical to the exact nonlinear numbers above. Their differences are finite nonlinear/off-CH corrections:
\[
E_{\rm raw,nonlinear}-E_{\rm raw,CH}^{(2)}
\approx5.59\times10^{-6},
\]
\[
E_{\rm AK,CH}^{(2)}-E_{\rm AK,nonlinear}
\approx6.03\times10^{-5}.
\]
Accordingly, the script comment that the hatted metric equals the original only “to numerical precision” must be understood as a far-tail approximation, not an exact statement about the optimized profile.

For the same entrance trace, the exact finite-\(X\) Step-19 quadratic minimizer has raw cost
\[
1.4357009992\times10^{-4}.
\]
After the same interface conversion its AK value is
\[
4.5650206710\times10^{-3},
\]
only \(3.93\times10^{-6}\) below the reconstructed profile’s quadratic AK value. This verifies closeness to the frozen-trace quadratic minimizer; it is not evidence of missing action.

---

## 5. Contact identity and frozen-profile capacity

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
the definition of \(\nu\) gives exactly
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
and this reduces to
\[
(k\theta)'=\frac12f_-v_-.
\]
It is therefore the Step-19 torsion/reconstruction equation in AK variables, not an independent exterior terminal condition.

### Capacity variational problem

Set
\[
h=\mu\nu,\qquad
\rho=\frac{\widehat W}{\mu^2}.
\]
Since \(\mu_T/\mu=2\beta\) and \(\nu_T+2\beta\nu=2\lambda\),
\[
h_T=2\mu\lambda,
\]
hence
\[
\boxed{
\frac{Q_A}{2}
=\frac12\int\rho h_T^2\,dT.
}
\]

For fixed endpoints \(h(T_0),h(T_1)\), writing
\[
R=\int_{T_0}^{T_1}\rho^{-1}\,dT,
\qquad
\Delta h=h(T_1)-h(T_0),
\]
the minimum is
\[
E_1=\frac{(\Delta h)^2}{2R}.
\]

Now impose the frozen contact moment
\[
\int c(T)h(T)\,dT=M,
\qquad
c=\frac{\eta(1-y^2)}{\mu}.
\]
Let \(h_{\rm lin}\) be the endpoint minimizer and let \(z\) solve
\[
-(\rho z_T)_T=c,\qquad z(T_0)=z(T_1)=0.
\]
Then
\[
\Gamma=\int cz\,dT=\int\rho z_T^2\,dT>0,
\]
and the two-constraint minimum is
\[
\boxed{
E_2
=
E_1+
\frac{\left(M-\int ch_{\rm lin}\,dT\right)^2}{2\Gamma}.
}
\]
This is exactly the formula implemented in the capacity script; its sign and factor \(1/2\) are correct.

The supplied results are:

| \(x_0\) | observed \(Q_A/2\) | endpoint capacity | endpoint + contact | fractions |
|---:|---:|---:|---:|---:|
| .015 | .00704682 | .00102980 | .00185791 | .1461, .2637 |
| .038 | .03285659 | .00585492 | .01066191 | .1782, .3245 |
| .07 | .08011336 | .01675474 | .03112443 | .2091, .3885 |

The reconstructed \(\frac12\int\rho h_T^2\) agrees with direct \(Q_A/2\) to \(10^{-8}\)–\(10^{-7}\). Contact residuals are \(6.1\times10^{-7}\)–\(1.2\times10^{-6}\), and all three profiles exhibit a sign change of \(\nu\).

Thus the claim that the two constraints account for only \(26\%\)–\(39\%\) of the observed transport energy is correct. It means only that, **after freezing the profile-dependent coefficients \(\rho,c\)**, endpoints plus one moment force that fraction. It does not yield a uniform lower bound over diagonal cells, because \(\rho,c,M\) vary with the metric. Nor does it show that the remaining percentage is an independent “tail cost”; it measures unresolved profile-dependent transport energy in this frozen variational comparison.

---

## Strongest corrected conclusion

For every smooth diagonal perpendicular exact-CH cell covered by the construction,
\[
\boxed{
\widehat P[t_0,t_1]
=\int_{t_0}^{t_1}L_{AK}\,dt+B(t_1)-B(t_0).
}
\]
In the antisymmetric linear CH sector,
\[
\boxed{
L_{AK}^{(2)}
=\mu(w')^2+(Aw^2)',
}
\]
with
\[
\boxed{
\lambda
=-\frac{x(1+x)w'+(2-3x)w}{2(1+x)^3}.
}
\]

Consequently:

- the Step-19 terminal response \(\delta^2/I(\rho)\) is the correct raw exterior value;
- the AK tail is that same response shifted by an explicit interface primitive;
- the Einstein mass direction remains exactly null;
- adding a separate AK tail price would double-count the exterior response;
- the displayed \(\lambda\) formula in the note must be corrected;
- the Section-3 profile values should be labeled CH quadratic reconstructions, while Section-2 values are the exact nonlinear evaluations.

For the all-metric Einstein-gap programme, this closes the representation ambiguity only in the diagonal near-CH exterior. It does not provide an unrestricted lower bound: the missing objects remain a uniform nonlinear exterior estimate for traces not quantitatively close to CH, a coercive near-zone estimate coupling the negative Nijenhuis term to conformal and transport evolution, and—outside symmetry—a justified relative self-dual form theory including its zero set and the additional \(W_2^+\) sector. The certified upper construction and its coefficient are unchanged by this verification.