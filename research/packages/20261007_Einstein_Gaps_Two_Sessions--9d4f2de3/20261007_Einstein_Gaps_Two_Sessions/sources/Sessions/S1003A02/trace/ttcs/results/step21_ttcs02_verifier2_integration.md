# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 21,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step21_ttcs02_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step21_ttcs02_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the hyperbolic-cell channel identities and numerical interpretation. The normalization is Ric=-6, scalar -24, sectional curvature -2. Verify algebraically that for an exact-H4-collar one-blow-up cell, P/(8pi^2)-1 = 4 int W+^2/(8pi^2) + [int s^2/12 - 48 Vol(B)]/(8pi^2), and J/(8pi^2)-1 = that Weyl term + int(s+18)^2/3/(8pi^2) + [36 Vol(U)-48 Vol(B)]/(8pi^2). Read the script/data and assess whether the reported X=64 cells support the claim that no volume-saving/scalar-near--18 mechanism appears in the tested diagonal family. Identify any normalization or volume-factor error.

## Integrated Scientific Memo

## Verification memo

### 1. Relative channel identities

Use the orientation in which the exceptional sphere has self-intersection \(-1\), so for a one-blow-up cell \(U\) relative to the ball \(B\),
\[
(\Delta\chi,\Delta\tau)=(1,-1).
\]
With the stated endomorphism norms,
\[
8\pi^2\chi=\int\left(|W^+|^2+|W^-|^2-\frac12|\Ric^\circ|^2+\frac{s^2}{24}\right)dV,
\]
\[
12\pi^2\tau=\int\left(|W^+|^2-|W^-|^2\right)dV.
\]
The combination \(2\chi+3\tau\) gives
\[
8\pi^2(2\chi+3\tau)
=\int\left(4|W^+|^2-|\Ric^\circ|^2+\frac{s^2}{12}\right)dV.
\]
Subtracting the ball formula is legitimate because the boundary metric and required curvature jet match, so the relative transgression terms cancel. Since
\[
2\Delta\chi+3\Delta\tau=-1,
\]
and the curvature-\(-2\) ball satisfies
\[
W^\pm_B=0,\qquad \Ric^\circ_B=0,\qquad s_B=-24,
\qquad \frac{s_B^2}{12}=48,
\]
one obtains
\[
P(U)=8\pi^2+4\int_U|W^+|^2dV
+\int_U\frac{s^2}{12}dV-48\Vol(B).
\]
Therefore
\[
\boxed{\frac{P}{8\pi^2}-1
=
4\frac{\int_U|W^+|^2\,dV}{8\pi^2}
+
\frac{\int_U s^2/12\,dV-48\Vol(B)}{8\pi^2}.}
\]

For
\[
J=\int_U|\Ric+6g|^2dV
=P+\frac14\int_U(s+24)^2dV,
\]
the pointwise completion of the square is
\[
\frac{s^2}{12}+\frac{(s+24)^2}{4}
=\frac{(s+18)^2}{3}+36.
\]
Consequently,
\[
\boxed{\frac{J}{8\pi^2}-1
=
4\frac{\int_U|W^+|^2\,dV}{8\pi^2}
+
\frac{\int_U(s+18)^2/3\,dV}{8\pi^2}
+
\frac{36\Vol(U)-48\Vol(B)}{8\pi^2}.}
\]

Thus both requested identities are algebraically correct. The value \(-18\) is only the completed-square center for the combined \(J\) scalar terms; the Einstein target remains \(s=-24\).

### 2. Chirality correction

The analysis-script statement

> “The chirality is fixed by demanding \(W^+=0\) on the real-hyperbolic collar”

is incorrect: real hyperbolic space is conformally flat, hence both \(W^+=0\) and \(W^-=0\). The relevant chirality is fixed by choosing the orientation for which the exceptional class has square \(-1\), equivalently \(\Delta\tau=-1\).

The script also does not directly evaluate \(W^+\). It defines
\[
4W^+_{\rm rel}:=P-1-\left(\int s^2/12-48\Vol(B)\right)/(8\pi^2),
\]
so `four_Wplus_rel_norm` is an inferred Chern–Weil residual, not an independent Weyl computation.

### 3. Volume normalization

For
\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
\qquad \int_{S^3}\sigma_1\sigma_2\sigma_3=2\pi^2,
\]
the radial factor is \(dx/(2\sqrt G)\), while
\[
abc=\sqrt F\,\sqrt x\,\sqrt{xe^w}
=\sqrt F\,x\,e^{w/2}.
\]
Hence
\[
dV=\pi^2\frac{\sqrt F\,x\,e^{w/2}}{\sqrt G}\,dx,
\qquad
\boxed{\frac{dV}{8\pi^2}
=\frac{\sqrt F\,x\,e^{w/2}}{8\sqrt G}\,dx.}
\]
This agrees with the active code
```python
v8 = sqrt(F)*xx*exp(w/2)/(8*sqrt(G))
```
and the quadrature weight `dx` already contains the coordinate differential.

On the exact \(H^4\) collar,
\[
F=x,\qquad G=x+2x^2=x(1+2x),\qquad w=0,
\]
so
\[
\frac{dV_B}{8\pi^2}=\frac{x}{8\sqrt{1+2x}}\,dx.
\]
Writing \(Y=\sqrt{1+2X}\),
\[
\boxed{\frac{\Vol(B_X)}{8\pi^2}
=\frac{Y^3}{48}-\frac{Y}{16}+\frac1{24},}
\]
exactly as implemented. At \(X=64\), this gives \(29.8559354821\), agreeing with the data.

The parent cell code is also consistent:
\[
\texttt{vol}=\frac{abc}{2\sqrt G}=4\,\frac{dV/(8\pi^2)}{dx},
\]
so `vol*ric0/4` integrates to \(P/(8\pi^2)\), and `vol*(s+24)^2/16` integrates to
\[
\frac1{8\pi^2}\frac14\int(s+24)^2dV.
\]

**No normalization, factor-of-two, \(8\pi^2\), or ball-volume error is present.** The unused zero-valued `vol_density` line is harmless dead code.

### 4. Interpretation of the \(X=64\) cells

For the three degree-16, \(P\)-optimized cells:

| \(x_0\) | \(V/V_B-1\) | mean \(s\) | RMS\((s+18)\) | scalar-volume channel in \(P\) | inferred \(4W^+\) | \(P-1\) |
|---:|---:|---:|---:|---:|---:|---:|
| .003 | \(1.6774\!\times10^{-5}\) | \(-23.999849\) | \(5.999850\) | .00601156 | .00004482 | .00605638 |
| .01 | \(4.7988\!\times10^{-5}\) | \(-23.999589\) | \(5.999602\) | .02003813 | .00042875 | .02046688 |
| .03 | \(1.1856\!\times10^{-4}\) | \(-23.999053\) | \(5.999155\) | .05986267 | .00320689 | .06306957 |

The evidence supports the following restricted conclusion:

1. **No volume saving occurs in these cells.**  
   All three have \(\Vol(U)>\Vol(B)\), albeit slightly.

2. **Their scalar curvature remains overwhelmingly near \(-24\), not \(-18\).**  
   RMS\((s+18)\approx6\), precisely the \(H^4\) value. The volume fractions with \(|s+18|\le3\) are only
   \[
   1.28\times10^{-7},\quad 1.44\times10^{-6},\quad 1.20\times10^{-5}.
   \]

3. **The apparently huge negative \(J\) “volume channel” is not a saving mechanism.**  
   For \(x_0=.003\),
   \[
   \frac1{8\pi^2}\int\frac{(s+18)^2}{3}=358.259337,
   \qquad
   \frac{36V-48V_B}{8\pi^2}=-358.253197.
   \]
   This is the ordinary \(s\approx-24\) background cancellation. The meaningful combined non-Weyl channel is
   \[
   C_J=\frac{\int(s+18)^2/3+36V-48V_B}{8\pi^2},
   \]
   whose values are
   \[
   0.00614040,\qquad 0.02122358,\qquad 0.06894252,
   \]
   all positive.

4. **Both channels in the \(P\) identity are positive.**  
   The scalar-volume terms are \(0.00601,0.02004,0.05986\), and the inferred Weyl terms are also positive. Thus no tested cell is subthreshold.

A clearer expansion around the actual hyperbolic scalar value is
\[
\frac{s^2}{12}-48
=\frac{(s+24)^2}{12}-4(s+24).
\]
Therefore
\[
\frac{P}{8\pi^2}-1
=
4W^+_{\rm rel}
+48(V-V_B)-4\int_U(s+24)\frac{dV}{8\pi^2}
+\int_U\frac{(s+24)^2}{12}\frac{dV}{8\pi^2}.
\]
The separate volume and linear-scalar pieces partially cancel, leaving approximately the predicted first-order Burns response:
\[
\frac{\text{scalar-volume channel}}{x_0}
=2.004,\ 2.004,\ 1.995.
\]
The inferred Weyl channel is smaller and approximately second order in \(x_0\).

### 5. Scope of the numerical claim

The data justify:

> Within the sampled degree-16 diagonal family, for \(X=64\) and \(x_0=.003,.01,.03\), the \(P\)-optimized cells exhibit neither a volume deficit nor a substantial scalar region near \(-18\); their combined scalar-volume and inferred \(W^+\) channels remain positive.

They do **not** establish the corresponding statement for the entire diagonal family:

- only three small-\(x_0\), \(P\)-targeted profiles were tested;
- \(x_0\le .03\) is perturbative, where the first-order law \(P/(8\pi^2)-1\sim2x_0\) already predicts a positive cost;
- there was no systematic \(X=64\) degree sweep, random-restart study, or interval certification;
- the recorded cells were optimized for \(P\), not directly for \(J\);
- direct coordinate integration of \(|W^\pm|^2\) was not performed.

Also, because
\[
J=P+\frac14\int(s+24)^2dV\ge P,
\]
a \(J\)-specific scalar-near-\(-18\) mechanism cannot produce \(J<8\pi^2\) without simultaneously producing \(P<8\pi^2\). Nevertheless, a separate \(J\)-optimization would be needed to characterize \(J\)-minimizing geometry rather than merely rule out a mechanism in these \(P\)-optimized samples.

Finally, the parametrization has exact \(H^4\) two-jet contact at \(x=X\), not an open exact-collar interval inside the numerical integration domain. That suffices for the relative transgression calculation; a globally smooth literal exterior attachment would require an additional flat-to-all-orders taper or smoothing segment.