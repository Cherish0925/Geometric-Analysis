# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 11,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step11_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step11_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the computer-assisted theorem that the frozen perpendicular Bianchi-IX cell has J_6<8π². Read the actual enclosure code, frozen JSON profile, symbolic Ricci checker, Step-10 theorem note, and peer independent reconstruction. Focus on the acb.integral holomorphy contract (including the piecewise phi_derivs series/quotient, complex-ball tail bound, analytic flags for log/sqrt), the desingularized Ricci algebra, exact interpretation of coefficients, volume/energy normalization, and faithful transcription of the profile. Identify any mathematically load-bearing flaw; if sound, state precisely what the certificate proves and its trust base. Do not merely summarize the files.

## Integrated Scientific Memo

# Verification memo: frozen perpendicular Bianchi–IX cell

## Verdict

No mathematically load-bearing flaw is visible in the supplied \(X=8\) certificate. Subject to the stated Arb/python-flint trust base, the explicit frozen profile satisfies
\[
\boxed{\frac{J_6(g)}{8\pi^2}<1},
\qquad
J_6(g)=\int |\operatorname{Ric}_g+6g|_g^2\,dV_g .
\]

The strongest supplied Arb output is
\[
\frac{J_6(g)}{8\pi^2}
=
[\,0.999116243135324311\pm 2.25\times10^{-19}\,],
\]
so, conservatively,
\[
\frac{J_6(g)}{8\pi^2}<0.9991162431353246
<1-8.8375686\times10^{-4}.
\]

This is a certificate for the explicitly defined frozen \(C^2\) cell obtained by attaching the exact complex-hyperbolic exterior at \(X=8\). The separate cutoff argument implies existence of smooth exact-collar metrics with energy converging to this value, hence, for example,
\[
J_6(g_\delta)<8\pi^2(1-\eta/2),
\qquad
\eta=8.8375686\times10^{-4},
\]
for some sufficiently small \(\delta\). The interval computation does not provide an explicit admissible \(\delta\).

---

## 1. Exact object certified

The coefficient interpretation must be stated carefully. Each JSON decimal is parsed to an IEEE-754 binary64 value and then passed as `arb(float(v))`. Thus the certified coefficients are the exact dyadic rationals represented by those binary64 values, not the displayed decimal strings interpreted as exact decimal rationals.

The remaining exact data are
\[
x_0=\frac1{100},\qquad X=8,\qquad
\ell=\log(X/x_0),\qquad
u=\frac{\log(x/x_0)}{\ell}.
\]
Let
\[
p(u)=10-15u+6u^2,\qquad S(u)=u^3p(u),
\]
and let \(C_F,C_G,C_w\) be the degree-seven Chebyshev expansions using the three consecutive blocks of eight stored coefficients. The \(C_G\) constant coefficient is shifted by
\[
c_{G,0}\mapsto c_{G,0}
-\sum_{k=0}^{7}(-1)^k(c_{F,k}+c_{G,k}),
\]
so that \(q_F(0)+q_G(0)=0\) exactly for the certified dyadic inputs.

The metric is
\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
\]
where
\[
F=(x-x_0)e^{q_F}+x_0S,
\]
\[
G=\bigl(x-x_0+(x^2+x_0)S\bigr)e^{q_G},
\]
\[
w=\log(1+x)S+u^2(1-u)^3C_w,
\]
with \(q_F=(1-u)^3C_F\) and \(q_G=(1-u)^3C_G\).

This transcription agrees with:

- the executable `PerpCell.prof_factory` in its perpendicular, \(\beta_0=0\), `wpow=2` specialization;
- the theorem note;
- the Arb enclosure code;
- the independent reconstruction source.

There is one harmless but real documentation error: the header of `o11_perp_cell.py` displays an ansatz with \(xe^{-w}\sigma_2^2\), whereas its executable code and every certified artifact use
\[
F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2.
\]
The certificate concerns the latter metric.

The frozen record does not itself store `wpow`; nevertheless the theorem is self-contained because it explicitly defines the \(u^2(1-u)^3C_w\) profile. The close floating agreement also strongly corroborates that the optimizer run used `wpow=2`.

---

## 2. Faithfulness of the cancellation-free profile

Put
\[
y=x-x_0=x_0\ell u\,\phi(\ell u),
\qquad
\phi(z)=\frac{e^z-1}{z}.
\]
The code defines \(F=y\widehat F\), \(G=y\widehat G\), \(w=y^2\widehat w\), where
\[
\widehat F=e^{q_F}+\frac{u^2p(u)}{\ell\phi(\ell u)},
\]
\[
\widehat G=
\left(
1+\frac{(x^2+x_0)u^2p(u)}
{x_0\ell\phi(\ell u)}
\right)e^{q_G},
\]
and
\[
\widehat w=
\frac{\log(1+x)\,u\,p(u)+(1-u)^3C_w}
{(x_0\ell\phi(\ell u))^2}.
\]
Multiplication by \(y\) or \(y^2\) reproduces the displayed frozen profile exactly. In particular,
\[
y\widehat F=(x-x_0)e^{q_F}+x_0S,
\]
and similarly for \(G,w\). This is not an approximation or an alternate profile.

For \(0\le u\le1\), \(p(u)>0\) and \(\phi(\ell u)>0\), so
\[
\widehat F>0,\qquad \widehat G>0.
\]
Consequently the metric is positive definite away from the bolt, and all real-axis denominators used by the integrand are nonzero.

At \(u=0\),
\[
F=G=0,\qquad
F'(x_0)G'(x_0)=\widehat F(0)\widehat G(0)
=e^{q_F(0)+q_G(0)}=1,
\]
and \(w=O(y^2)\). Hence, in the geodesic coordinate \(t\),
\[
a_1^2=F=t^2+O(t^4),\qquad
a_2^2-a_3^2=x(1-e^w)=O(t^4),
\]
which gives the smooth Hopf-bolt behavior for the charge-four anisotropy mode.

At \(u=1\), \(S=1\), \(q_F=q_G=0\), and
\[
F=x,\qquad G=x+x^2,\qquad e^w=1+x.
\]
Because all deviations contain \((1-u)^3\), the metric agrees through its second \(x\)-jet with the complex-hyperbolic metric. Thus the direct attachment is \(C^2\), and the exterior contributes zero to \(J_6\).

---

## 3. Desingularized Ricci algebra

For
\[
g=dt^2+\sum_{i=1}^3a_i^2\sigma_i^2,
\qquad h_i=a_i^2,\qquad
\frac d{dt}=2\sqrt G\,\frac d{dx},
\]
one has
\[
\frac{\ddot a_i}{a_i}
=
\frac{G'h_i'}{h_i}
+\frac{2Gh_i''}{h_i}
-\frac{G(h_i')^2}{h_i^2},
\]
and
\[
\frac{\dot a_i\dot a_j}{a_ia_j}
=
G\frac{h_i'h_j'}{h_ih_j}.
\]

For \(h_1=y\widehat F\), \(G=y\widehat G\), the apparently singular terms combine to
\[
\frac{\ddot a_1}{a_1}
=
2\frac{\widehat G}{\widehat F}h_1''
+h_1'
\frac{\widehat G'\widehat F-\widehat G\widehat F'}
{\widehat F^2},
\]
because
\[
G'h_1-Gh_1'
=
y^2(\widehat G'\widehat F-\widehat G\widehat F').
\]
Likewise,
\[
\frac{\dot a_1\dot a_j}{a_1a_j}
=
\frac{\widehat G}{\widehat F}\frac{h_1'h_j'}{h_j}.
\]
These are exactly the coded `D1`, `L12`, and `L13`.

For \(h_2=x\), \(h_3=xe^w\), \(w=y^2\widehat w\),
\[
e^w-1=w\phi(w)=y^2\widehat w\phi(w),
\]
and
\[
\frac{\sinh w}{h_1}
=
\frac{y\widehat w\,\operatorname{shc}(w)}{\widehat F},
\qquad
\operatorname{shc}(w)=\frac{\sinh w}{w}.
\]
Therefore the algebraic Bianchi–IX curvature terms become
\[
A_1=
\frac{2h_1}{x^2e^w}
-\frac{2y^3\widehat w^2\phi(w)^2}{\widehat F e^w},
\]
\[
A_2=
-\frac{4y\widehat w\,\operatorname{shc}(w)}{\widehat F}
+\frac4x-\frac{2h_1}{x^2e^w},
\]
\[
A_3=
\frac{4y\widehat w\,\operatorname{shc}(w)}{\widehat F}
+\frac{4}{xe^w}-\frac{2h_1}{x^2e^w}.
\]
These agree line-for-line with the enclosure code and remove every division by the collapsing factor \(h_1\).

The base Ricci formula
\[
R_{00}=-\sum_i\frac{\ddot a_i}{a_i},
\]
\[
R_{ii}=
-\frac{\ddot a_i}{a_i}
-\frac{\dot a_i}{a_i}
\left(\frac{\dot a_j}{a_j}+\frac{\dot a_k}{a_k}\right)
+
\frac{2(a_i^4-(a_j^2-a_k^2)^2)}
{a_i^2a_j^2a_k^2}
\]
has the correct structure constant for
\[
d\sigma_i=2\sigma_j\wedge\sigma_k.
\]
The supplied symbolic scripts derive the curvature from Cartan’s equations and are constructed to reduce the four Ricci differences and the \(D_1,A_1,A_2,A_3\) rewrite residuals to zero. The relevant identities are also directly verified by the calculations above, so the absent captured stdout is not essential to this review.

The second-order jet implementation is correct:
\[
f_x=\frac{f_u}{\ell x},\qquad
f_{xx}=\frac{f_{uu}-\ell f_u}{\ell^2x^2},
\]
and the jet for \(\phi(\ell u)\) is
\[
\bigl(\phi(\ell u),\ell\phi'(\ell u),\ell^2\phi''(\ell u)\bigr).
\]

---

## 4. Volume and energy normalization

With
\[
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2,
\]
the volume element is
\[
dV
=
\pi^2\sqrt{\frac{h_1h_2h_3}{G}}\,dx
=
\pi^2x e^{w/2}\sqrt{\frac{\widehat F}{\widehat G}}\,dx.
\]
Since \(dx=\ell x\,du\),
\[
\frac{dV}{8\pi^2\,du}
=
\frac18\,x e^{w/2}
\sqrt{\frac{\widehat F}{\widehat G}}\,
\ell x,
\]
exactly the coded `vol`.

The Ricci tensor is diagonal in the orthonormal frame, hence
\[
|\operatorname{Ric}+6g|^2
=
\sum_{a=0}^3(R_{aa}+6)^2.
\]
Thus the coded `J` integral is precisely \(J_6/(8\pi^2)\), not a proportional surrogate.

Similarly,
\[
|\operatorname{Ric}^{\circ}|^2
=
\sum_a\left(R_{aa}-\frac s4\right)^2,
\]
and in dimension four
\[
|\operatorname{Ric}+6g|^2
=
|\operatorname{Ric}^{\circ}|^2+\frac14(s+24)^2.
\]
The 256-bit centers obey
\[
0.999108702733592648
+
0.000007540401731663
=
0.999116243135324311,
\]
providing a strong internal normalization check.

---

## 5. Arb holomorphy contract

### 5.1 The \(\phi\) series and quotient branches

The Taylor branch evaluates
\[
\phi(z)=\sum_{k\ge0}\frac{z^k}{(k+1)!},
\]
\[
\phi'(z)=\sum_{k\ge0}\frac{k+1}{(k+2)!}z^k,
\qquad
\phi''(z)=\sum_{k\ge0}
\frac{(k+1)(k+2)}{(k+3)!}z^k.
\]
Each coefficient is bounded by \(1/k!\). For \(|z|\le r\le1\),
\[
\sum_{k=N}^\infty\frac{r^k}{k!}
\le
\frac{r^N/N!}{1-r/(N+1)}.
\]
This is the exact bound used with \(N=48\). The error box
\[
[-t,t]+i[-t,t]
\]
contains the disk of radius \(t\), so adding it encloses each complex remainder.

For \(r>1\), the code uses the exact identities
\[
\phi(z)=\frac{e^z-1}{z},
\]
\[
\phi'(z)=\frac{ze^z-e^z+1}{z^2},
\]
\[
\phi''(z)=
\frac{z^2e^z-2ze^z+2e^z-2}{z^3}.
\]
A complex ball containing zero can make this representation nonfinite; that does not silently produce a wrong value. It causes rejection/subdivision by the integrator. Near zero the Taylor branch is normally selected.

The branch choice depends on `abs(z)`, but it is only a choice between two valid enclosures of the same entire functions. It does not make the represented integrand piecewise nonholomorphic.

The tail radius uses
```python
(float(m.mid()) + float(m.rad()))*(1 + 2**-30) + 1e-300
```
rather than a pure-Arb upper endpoint. This is not ideal design, but it is safe for the present computation: the \(2^{-30}\) relative inflation dominates binary64 conversion and addition errors of order \(2^{-52}\), while \(10^{-300}\) covers the extreme near-zero regime. Replacing this with a rigorous Arb upper bound would reduce the trust base, but the current step is not a load-bearing defect here.

### 5.2 Logarithm, square root, and divisions

The multivalued functions are called as
```python
log(analytic=analytic)
sqrt(analytic=analytic)
```
during Arb’s analyticity tests. Thus a ball intersecting the relevant branch cut cannot be accepted as a valid holomorphic enclosure. Ordinary division is valid only when the denominator ball excludes zero; otherwise the result is nonfinite and subdivision is required.

On the real interval,
\[
1+x>0,\qquad
\widehat F>0,\qquad
\widehat G>0,\qquad
\phi(\ell u)>0.
\]
By compactness, these functions remain nonzero and off the cuts on some complex neighborhood of \([0,1]\). The auxiliary quotient representation has complex poles away from the interval, notably at zeros of \(\phi(\ell u)\), but this only limits admissible ellipse sizes. It does not obstruct subdivision to a sufficiently small holomorphic neighborhood.

The integrand uses \((R_{aa}+6)^2\), not \(|R_{aa}+6|^2\). That is exactly the required holomorphic extension of the real-axis energy density. The exact integral is real, so extracting the real part of an `acb` enclosure with a small imaginary radius is legitimate.

Accordingly, every finite callback value used by `acb_calc_integrate` encloses a holomorphic extension on the tested ball. No violation of the Petras-type integration contract was found.

---

## 6. Interpretation of the numerical artifacts

The rigorous object is the Arb ball string. The JSON `lower`, `upper`, `rad`, and `eta_certified` fields are ordinary Python floats. At 256-bit precision the printed binary64 lower and upper values collapse to the same number, so those fields should not be cited as the high-precision interval endpoints. This does not affect the boolean \(J<1\): the deficit is about \(8.8\times10^{-4}\), vastly larger than binary64 rounding.

Two claims in the note require qualification:

1. `o11_peer_rigorous_replication_256.json` has the output schema of the same Arb enclosure script. It is a higher-precision rerun, not output from the independent JAX reconstruction. It demonstrates reproducibility of that implementation, not code independence.

2. The preliminary record values
   \[
   J=0.9991162428177064,\qquad
   P=0.9991087024169157
   \]
   are outside the narrow final Arb balls by about \(3.2\times10^{-10}\). They are nonrigorous optimization quadrature metadata and play no role in the proof. Therefore the note’s statement that all floating implementations lie “inside the ball” cannot refer to these stored metadata.

The independent reconstruction source does use genuinely different formulas—cyclically reordered axes and the spin/Chern–Simons representation—and therefore is valuable corroboration of profile transcription and curvature normalization. However, its output JSON is not among the supplied files; numerical agreement attributed to it is not independently inspectable from this bounded bundle.

There is also a small distinction between the optimization and certified profiles: the optimizer computes the derived \(c_G\) shift in binary64 arithmetic, whereas the certificate forms the exact high-precision sum of the dyadic input coefficients. The theorem correctly concerns this exact-sum certified profile.

---

## 7. Scope of the result

What is established by the supplied certificate is:

\[
\boxed{
\frac1{8\pi^2}
\int_{x_0\le x\le8}
|\operatorname{Ric}+6g|^2\,dV
\in
[0.999116243135324311\pm2.25\times10^{-19}]
}
\]
for the exact frozen \(X=8\) profile described above. Since the exterior is exactly complex hyperbolic, the same value is the energy of the attached \(C^2\) cell.

Bolt smoothness, positivity, \(C^2\) collar matching, topology, and smoothing are analytic arguments rather than consequences of Arb. They are consistent with the formulas supplied and no defect was found. The cutoff proof yields smooth witnesses with energy arbitrarily close to, but not exactly equal to, the frozen \(C^2\) value.

The supplied materials do **not** independently verify:

- the claimed \(X=16\) certificate, because its profile and rigorous output are absent;
- the full global O11 coefficient calculation, which relies on the unsupplied I54 surgery accounting and normalization conventions.

Those limitations do not affect the local theorem \(J_6<8\pi^2\) for the \(X=8\) cell.

---

## Trust base

The strict inequality depends on:

1. correctness of Arb complex ball arithmetic, elementary functions, and `acb_calc_integrate`;
2. correctness of the python-flint wrapper’s analytic-callback semantics;
3. faithful execution of the displayed enclosure source on the displayed JSON;
4. Python JSON parsing to binary64 and exact Arb enclosure of those dyadic values;
5. the explicit \(\phi,\phi',\phi''\) tail estimate, including the small binary64 inflation used for \(r\);
6. the Bianchi–IX Ricci formula, desingularized identities, and jet rules checked above;
7. the orbit normalization
   \[
   \int_{S^3}\sigma_{123}=2\pi^2;
   \]
8. analytic handling of `log` and `sqrt`, and zero exclusion for divisions.

Within that standard computer-assisted-proof trust base, the frozen perpendicular cell theorem is sound:
\[
\boxed{J_6(g)<8\pi^2}
\]
with certified normalized deficit exceeding \(8.8375686\times10^{-4}\).