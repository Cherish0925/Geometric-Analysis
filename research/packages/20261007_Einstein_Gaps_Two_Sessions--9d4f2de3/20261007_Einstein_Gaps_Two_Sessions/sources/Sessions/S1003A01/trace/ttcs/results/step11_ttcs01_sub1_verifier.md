# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/perp_rigorous_enclosure.py",
    "Sessions/S1003A01/workspace/scripts/check_bianchi_ricci_closed_form.py",
    "Sessions/S1003A01/workspace/scripts/perp_cartan_verify.py",
    "Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json",
    "Sessions/S1003A01/workspace/data/perp_collar/rigorous_x0.01_X8_J_d8.json",
    "Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py",
    "Sessions/S1003A02/workspace/scripts/o11_collar_independent_verify.py",
    "Sessions/S1003A02/workspace/data/o11_peer_rigorous_replication_256.json"
  ]
}
```

## Task

Independently verify the computer-assisted theorem that the frozen perpendicular Bianchi-IX cell has J_6<8π². Read the actual enclosure code, frozen JSON profile, symbolic Ricci checker, Step-10 theorem note, and peer independent reconstruction. Focus on the acb.integral holomorphy contract (including the piecewise phi_derivs series/quotient, complex-ball tail bound, analytic flags for log/sqrt), the desingularized Ricci algebra, exact interpretation of coefficients, volume/energy normalization, and faithful transcription of the profile. Identify any mathematically load-bearing flaw; if sound, state precisely what the certificate proves and its trust base. Do not merely summarize the files.

## Output

# Scientific verification memo

## 1. Verified mathematical statement

No mathematically load-bearing flaw was found in the enclosure argument for the explicitly defined frozen profile.

Interpreting each JSON coefficient by

```python
arb(float(v))
```

means that the witness uses the dyadic rational represented by the parsed IEEE-754 binary64 value, not the decimal numeral viewed as an exact rational. With \(x_0=1/100\), \(X=8\), the exact derived \(c_G\)-shift stated in the Step-10 note, and the metric
\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
\]
the supplied 256-bit Arb result
\[
[0.999116243135324311\mathbin{+/-}2.25\times10^{-19}]
\]
implies the safe enclosure
\[
0.9991162431353240
<
\frac{J_6(g)}{8\pi^2}
<
0.9991162431353246.
\]
In particular,
\[
\frac{J_6(g)}{8\pi^2}
<
1-8.8375686\times10^{-4}<1.
\]

This enclosure is for the \(C^2\) metric obtained by attaching the exact complex-hyperbolic exterior at \(x=X\). The analytic cutoff argument separately gives smooth exact-collar metrics whose energies converge to this value, and hence a smooth metric with, for example,
\[
J_6<8\pi^2(1-\eta/2),\qquad \eta=8.8375686\times10^{-4}.
\]
The interval computation itself does not supply a numerical cutoff width \(\delta\); the existence of such a \(\delta\) follows from the \(O(\delta^3)\) estimate in the note.

## 2. Faithful reconstruction of the frozen metric

Let
\[
\ell=\log(X/x_0),\qquad x=x_0e^{\ell u},\qquad
y=x-x_0=x_0\ell u\,\phi(\ell u),
\quad
\phi(z)=\frac{e^z-1}{z}.
\]
Writing \(p(u)=10-15u+6u^2\) and \(S(u)=u^3p(u)\), the code defines
\[
\widehat F=e^{(1-u)^3C_F(u)}
       +\frac{u^2p(u)}{\ell\phi(\ell u)}
\]
and therefore
\[
y\widehat F
=(x-x_0)e^{q_F}+x_0u^3p(u)
=(x-x_0)e^{q_F}+x_0S(u)=F.
\]
Likewise,
\[
\widehat G=
\left(
1+\frac{(x^2+x_0)u^2p(u)}
{x_0\ell\phi(\ell u)}
\right)e^{(1-u)^3C_G(u)}
\]
gives
\[
y\widehat G
=\bigl(x-x_0+(x^2+x_0)S(u)\bigr)e^{q_G}=G.
\]
Finally, the jet expression
\[
w=\log(1+x)\,u^3p(u)+u^2(1-u)^3C_w(u)
\]
is exactly the frozen profile in the theorem note. Its auxiliary quotient satisfies
\[
w=y^2\widehat w,\qquad
\widehat w=
\frac{\log(1+x)\,u\,p(u)+(1-u)^3C_w(u)}
     {(x_0\ell\phi(\ell u))^2}.
\]

The Chebyshev arguments and indexing agree in all relevant files. The shift
\[
c_{G,0}\longmapsto c_{G,0}
-\sum_{k=0}^7(-1)^k(c_{F,k}+c_{G,k})
\]
gives \(q_F(0)+q_G(0)=0\). Thus
\[
F'(x_0)G'(x_0)=\widehat F(0)\widehat G(0)=1.
\]
The original JAX optimizer forms this shift in binary64 arithmetic, whereas the Arb code encloses the exact sum of the dyadic inputs at high precision. The certified metric is therefore precisely the exact-sum profile written in the theorem note; the difference from the optimization execution is only the rounding of this derived shift.

For real \(0\le u\le1\),
\[
p(u)>0,\qquad \phi(\ell u)>0,
\]
so \(\widehat F>0\) and \(\widehat G>0\). At \(u=0\),
\[
F=G=0,\qquad w=O(y^2),
\]
and the radial coordinate satisfies \(y=\widehat G(0)t^2+O(t^4)\). Hence
\[
a_1^2=F=t^2+O(t^4),\qquad
a_2^2-a_3^2=x(1-e^w)=O(t^4),
\]
which is the required smooth Hopf-bolt behavior.

At \(u=1\), \(S=1\), \(q_F=q_G=0\), and the residual \(w-\log(1+x)\) vanishes. Since \(1-S\) and every \(q\)-term have a factor \((1-u)^3\), the metric agrees through its second \(x\)-jet with
\[
F=x,\qquad G=x+x^2,\qquad e^w=1+x.
\]
Thus the attached metric is \(C^2\), and its exterior has \(\operatorname{Ric}=-6g\).

One textual inconsistency should be removed from future presentations: the header of `o11_perp_cell.py` writes an ansatz containing \(xe^{-w}\sigma_2^2\), but its executable `prof_factory`, the frozen theorem, the enclosure code, and the independent reconstruction all use
\[
F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2.
\]
The certificate applies to this latter metric.

## 3. Desingularized Ricci algebra

For
\[
g=dt^2+\sum_{i=1}^3a_i^2\sigma_i^2,\qquad
\frac d{dt}=2\sqrt G\,\frac d{dx},
\]
put \(h_i=a_i^2\). Direct differentiation gives
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

For \(h_1=y\widehat F\) and \(G=y\widehat G\), the singular-looking terms combine exactly:
\[
\frac{\ddot a_1}{a_1}
=
2\frac{\widehat G}{\widehat F}h_1''
+h_1'
\frac{\widehat G'\widehat F-\widehat G\widehat F'}
     {\widehat F^2}.
\]
Indeed,
\[
G'h_1-Gh_1'
=
y^2(\widehat G'\widehat F-\widehat G\widehat F'),
\]
which cancels the \(y^2\) in \(h_1^2\). Similarly,
\[
\frac{\dot a_1\dot a_j}{a_1a_j}
=
\frac{\widehat G}{\widehat F}
\frac{h_1'h_j'}{h_j}.
\]
These are exactly the expressions `D1`, `L12`, and `L13` in the enclosure code.

For \(h_2=x\), \(h_3=xe^w\), and \(w=y^2\widehat w\),
\[
e^w-1=w\phi(w)=y^2\widehat w\phi(w),
\]
so
\[
\frac{(e^w-1)^2}{h_1e^w}
=
\frac{y^3\widehat w^2\phi(w)^2}{\widehat F e^w}.
\]
Also,
\[
\frac{\sinh w}{h_1}
=
\frac{y\widehat w\,\operatorname{shc}(w)}{\widehat F},
\qquad
\operatorname{shc}(w)=\frac{\sinh w}{w}.
\]
Substitution into
\[
A_i=
\frac{2\bigl(h_i^2-(h_j-h_k)^2\bigr)}
     {h_ih_jh_k}
\]
gives precisely
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
Thus every apparent division by the collapsing \(h_1\) has been removed at \(u=0\).

The Ricci entries used by the code,
\[
R_{00}=-\sum_i\frac{\ddot a_i}{a_i},
\]
\[
R_{ii}
=
-\frac{\ddot a_i}{a_i}
-\frac{\dot a_i}{a_i}
 \left(\frac{\dot a_j}{a_j}+\frac{\dot a_k}{a_k}\right)
+\frac{2(a_i^4-(a_j^2-a_k^2)^2)}
       {a_i^2a_j^2a_k^2},
\]
have the correct factor \(2\) for \(d\sigma_i=2\sigma_j\wedge\sigma_k\). The symbolic scripts derive the connection and curvature from Cartan’s equations and reduce all four differences between this formula and the Cartan Ricci tensor to zero. The separate symbolic reductions of `D1`, `A1`, `A2`, and `A3` also vanish identically. The algebra above independently reproduces the portions that matter at the bolt.

## 4. Volume and energy normalization

With
\[
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2,
\]
the volume element is
\[
dV
=
\frac{\sqrt{F\cdot x\cdot xe^w}}{2\sqrt G}\,
dx\int_{S^3}\sigma_{123}
=
\pi^2x e^{w/2}\sqrt{\frac{F}{G}}\,dx.
\]
Since \(F/G=\widehat F/\widehat G\) and \(dx=\ell x\,du\),
\[
\frac{dV}{8\pi^2\,du}
=
\frac18\,x e^{w/2}
\sqrt{\frac{\widehat F}{\widehat G}}\,
\ell x,
\]
which is exactly `vol` in the code.

The Ricci tensor is diagonal in the orthonormal frame, hence
\[
|\operatorname{Ric}+6g|^2
=
\sum_{a=0}^3(R_{aa}+6)^2.
\]
Therefore the implemented `J` integrand is exactly \(J_6/(8\pi^2)\).

Likewise,
\[
|\operatorname{Ric}^{\circ}|^2
=
\sum_a\left(R_{aa}-\frac s4\right)^2,
\]
and in four dimensions
\[
|\operatorname{Ric}+6g|^2
=
|\operatorname{Ric}^{\circ}|^2+\frac14(s+24)^2.
\]
The 256-bit centers satisfy
\[
0.999108702733592648
+
0.000007540401731663
=
0.999116243135324311,
\]
matching \(J=P+S\) through every displayed digit.

## 5. The `acb.integral` analyticity contract

### The \(\phi\) implementation

The Taylor expansions used in the series branch are
\[
\phi(z)=\sum_{k\ge0}\frac{z^k}{(k+1)!},
\]
\[
\phi'(z)=\sum_{k\ge0}
\frac{k+1}{(k+2)!}z^k,
\qquad
\phi''(z)=\sum_{k\ge0}
\frac{(k+1)(k+2)}{(k+3)!}z^k.
\]
For each of these three series, the absolute value of the coefficient of \(z^k\) is at most \(1/k!\). Thus, when \(|z|\le r\le1\),
\[
\sum_{k=N}^{\infty}\frac{r^k}{k!}
\le
\frac{r^N/N!}{1-r/(N+1)}.
\]
This is exactly the tail radius used with \(N=48\). Adding the complex rectangle
\[
[-t,t]+i[-t,t]
\]
certainly contains every complex remainder of modulus at most \(t\).

For \(r>1\), the code uses the exact formulas
\[
\phi=\frac{e^z-1}{z},\quad
\phi'=\frac{ze^z-e^z+1}{z^2},\quad
\phi''=\frac{z^2e^z-2ze^z+2e^z-2}{z^3}.
\]
If a broad complex ball also contains \(z=0\), the division produces a nonfinite enclosure and Arb subdivides. Near \(z=0\), the Taylor branch is selected. The switch at \(r=1\) is therefore only a switch between two enclosures of the same entire functions; it does not define a piecewise mathematical integrand.

The upper radius estimate passes through Python binary64:
```python
(float(m.mid()) + float(m.rad()))*(1 + 2**-30) + 1e-300
```
This remains valid here. For magnitudes at least \(10^{-300}\), the \(2^{-30}\) inflation is vastly larger than the binary64 conversion and addition errors, which are of relative order \(2^{-52}\). For smaller magnitudes the added \(10^{-300}\) dominates. Consequently the Taylor branch is entered only with a genuine upper estimate \(r\le1\). A pure-Arb upper endpoint would remove this external floating-point step, but the present expression does not invalidate this computation.

### Logarithm, square root, and divisions

On the real integration interval,
\[
x>0,\quad 1+x>0,\quad
\widehat F>0,\quad \widehat G>0,\quad
\phi(\ell u)>0.
\]
Hence there is a complex neighborhood of the compact interval in which all required denominators remain nonzero and the selected logarithm and square root extend holomorphically.

The only multivalued operations are handled as
```python
log(analytic=analytic)
sqrt(analytic=analytic)
```
when Arb requests an analyticity proof on a complex ellipse. If an enclosure intersects the logarithm or square-root branch ray \((-\infty,0]\), the analytic call does not return an unjustified finite value. Ordinary division likewise requires the denominator ball to exclude zero. Exponentials and Chebyshev polynomials are entire.

The auxiliary representations contain poles away from the real interval, for example at complex zeros of \(\phi(\ell u)\). This is harmless: the real interval has a smaller complex neighborhood free of those zeros, and `acb_calc_integrate` can subdivide until its ellipses lie inside such neighborhoods. The finite returned ball records that this process succeeded.

Although the computed integral has a tiny imaginary radius, the exact profile and integrand are real on \(0\le u\le1\). Taking the real component therefore retains the exact real integral.

## 6. Independent reconstruction and artifact consistency

The JAX reconstruction uses the cyclic permutation
\[
(a_1,a_2,a_3)
=
(\sqrt{x},\sqrt{xe^w},\sqrt F),
\]
which preserves the cyclic Bianchi-IX structure. With
\[
r_i=\frac{\dot u_i}{a_i},\qquad
v_i=\frac{2H_i}{a_ja_k},\qquad
\lambda_i=\frac{a_ja_k}{a_i},
\]
its direct expression
\[
\sum_i\frac{\lambda_i}{4}
\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2
\frac{dx}{2\sqrt G}
\]
is exactly
\[
\frac{abc}{4}\sum_i(r_i-v_i)^2\,dt
=
\frac{1}{8\pi^2}|\operatorname{Ric}^{\circ}|^2dV.
\]
Its scalar expression is also correct because the Cartan identity gives
\[
s=-2\sum_i(r_i+v_i).
\]
Thus `P_positive + scalar` is a genuinely separate floating evaluation of \(J/(8\pi^2)\). The named `J` field in that script additionally uses the relative transgression decomposition, but the direct positive formula is already present.

Two artifact distinctions matter:

1. `o11_peer_rigorous_replication_256.json` has exactly the output schema of `perp_rigorous_enclosure.py`, not that of `o11_collar_independent_verify.py`. It is a high-precision rerun of the same Arb implementation, not an output from the independent JAX reconstruction. The supplied material contains the reconstruction source but not its resulting JSON.

2. The optimizer metadata in the frozen record,
   \[
   J=0.9991162428177064,\qquad
   P=0.9991087024169157,
   \]
   lie outside the much narrower Arb balls. Their differences from the certified centers are approximately
   \[
   3.17618\times10^{-10},\qquad
   3.16677\times10^{-10}.
   \]
   Those fields are preliminary quadrature values and are not part of the enclosure proof. The Step-10 sentence saying independent floating values lie inside the ball cannot refer to these two stored metadata values.

Neither point changes the strict inequality, but both should be stated accurately when presenting computational corroboration.

## 7. Trust base

The strict inequality rests on the following concrete components:

1. Correctness of Arb/python-flint ball arithmetic, its elementary complex functions, and `acb_calc_integrate`.
2. Faithful execution of the shown enclosure source against the shown JSON record.
3. Python’s JSON-to-binary64 conversion and python-flint’s enclosure of those dyadic values.
4. The proved Taylor remainder formula and the binary64 inflation used to obtain \(r\).
5. The Cartan-derived Bianchi-IX Ricci formula and the desingularized identities reproduced above.
6. The orbit normalization \(\int_{S^3}\sigma_{123}=2\pi^2\).
7. The analytic branch handling for `log` and `sqrt`, plus interval exclusion of zero for every division.

The JSON `lower`, `upper`, and `eta_certified` fields are converted to ordinary Python floats; at 256 bits the displayed lower and upper even collapse to the same binary64 number. The rigorous object is the Arb ball string itself. The boolean comparison remains correct here because the gap to \(1\) is about \(8.8\times10^{-4}\), many orders of magnitude larger than binary64 rounding.

Subject to this standard trust base, the frozen exact-sum perpendicular cell satisfies
\[
\boxed{J_6(g)<8\pi^2}
\]
with a certified normalized deficit exceeding \(8.8375686\times10^{-4}\).