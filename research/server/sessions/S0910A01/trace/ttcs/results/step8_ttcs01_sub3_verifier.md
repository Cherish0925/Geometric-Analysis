# TTCS Independent Branch Record

```json
{
  "step_id": 8,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/notes/sources/derdzinski_1983_self_dual_kahler_einstein_four.txt",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md"
  ]
}
```

## Task

Verify the Step 8 measure-local rigidity theorem for the four-dimensional LeBrun near-boundary negative-pinching route. Check (i) the primary-source Derdziński conformal factor and orientation/eigenvalue normalization used in the local contradiction, (ii) the local averaging lemma with local means under Ricci lower/doubling, (iii) the harmonic-coordinate passage through finite W^{2,p} convergence and smoothness of the limiting Einstein metric without derivative-Ricci assumptions on the approximating metrics, and (iv) the exact strength of the conclusion Vol{p: Vol(B_1(p))>=v}/Vol(M)->0 rather than pointwise collapse. Identify any mathematical gaps, missing hypotheses, or normalization errors that could invalidate the theorem.

## Output

## Scientific verification memo

### Overall assessment

The measure-local theorem is mathematically valid provided the global LeBrun bookkeeping quoted in Step 8 is available:

\[
\frac{D_i}{A_i}\to0,\qquad
\frac{\operatorname{Vol}(M_i,g_i)}{A_i}\to\frac{32\pi^2}{9},
\qquad
\frac1{\operatorname{Vol}M_i}\int_{M_i}F_i\,d\mu_i\to0.
\]

The Derdziński normalization is correct, the local averaging argument is correct, and finite-\(p\) harmonic-coordinate compactness suffices without bounds on derivatives of \(\operatorname{Ric}_{g_i}\). The resulting conclusion is exactly convergence to zero of the relative volume of the unit-scale noncollapsed set; it does not imply uniform collapse at every point.

### 1. Derdziński factor, orientation, and eigenvalues

Derdziński Proposition 5(i), on extracted pages corresponding to pp. 420–421, states that under

\[
\delta W^+=0,\qquad \#\operatorname{spec}(W^+)\le2,
\]

the metric

\[
\widehat g=(24\,g(W^+,W^+))^{1/3}g
          =(24|W^+|_g^2)^{1/3}g
\]

is locally Kähler on \(\{W^+\ne0\}\), compatibly with the prescribed orientation. Proposition 5(ii) gives essential uniqueness, and Proposition 5(iii) states that constant \(|W^+|^2\) is equivalent to \(\nabla W^+=0\) under these hypotheses. Remark 4 gives the Einstein-to-locally-conformally-Kähler formulation used in Step 8.

The tensor normalization agrees with LeBrun’s convention. Both sources use the Kähler identity

\[
s^2=24|W^+|^2,
\]

and, for the Kähler orientation,

\[
\operatorname{spec}(W^+)
 =\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right).
\]

Thus, if \(\operatorname{Ric}=-g\), then \(s=-4\) and a Kähler–Einstein metric has

\[
\operatorname{spec}(W^+)
 =\left(-\frac23,\frac13,\frac13\right),
 \qquad |W^+|^2=\frac23.
\]

The calibrated LeBrun profile is instead

\[
|W^+|^2=\frac1{24},\qquad
\operatorname{spec}(W^+)
 =\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

At this profile,

\[
(24|W^+|^2)^{1/3}=1,
\]

so Derdziński’s Kähler metric is exactly \(g\), not merely an unspecified conformal representative. This yields the stated contradiction with the Kähler–Einstein spectrum. The orientation is also correct: Derdziński’s Kähler form lies in \(\Lambda^+\), and the simple eigenvalue is \(s/6\); for the calibrated tensor it is \(-1/6\).

The alternative Weitzenböck computation is consistent. With

\[
\frac12\Delta |W^+|^2
 =|\nabla W^+|^2+\frac{s}{2}|W^+|^2-18\det W^+,
\]

the calibrated values \(s=-4\), \(|W^+|^2=1/24\), and
\(\det W^+=-1/864\) give

\[
|\nabla W^+|^2=\frac1{16},
\]

whereas Proposition 5(iii) gives \(\nabla W^+=0\).

### 2. The algebraic LeBrun gap can be written without \(Q_i,P_i\)

The undefined factors \(Q_i,P_i\) are the main presentation issue in the note. The necessary algebra can be expressed canonically.

Set

\[
\alpha=\sqrt{\frac23},\qquad
f=\frac23s-2\alpha|W^+|,\qquad
a=\frac23s+2w,
\]

where \(w\) is the least eigenvalue of \(W^+\), and define

\[
\xi=w+\alpha|W^+|\ge0.
\]

Then \(a=f+2\xi\), and

\[
\mathcal G:=f^2-(a_-)^2\ge0,
\qquad a_-:=\min(a,0).
\]

Indeed, if \(a<0\),

\[
\mathcal G=f^2-a^2=-4\xi(f+\xi),
\]

while if \(a\ge0\), \(\mathcal G=f^2\).

At the limiting values \(s=-4\) and \(|W^+|=1/(2\sqrt6)\),

\[
f=-3,\qquad -\frac16\le w\le0.
\]

Consequently \(a=-8/3+2w<0\), and

\[
\mathcal G=4\xi(3-\xi).
\]

Thus \(\mathcal G=0\) forces \(\xi=0\), hence

\[
w=-\sqrt{\frac23}|W^+|=-\frac16.
\]

Equality in the trace-free eigenvalue estimate then forces the other two eigenvalues to coincide at \(1/12\).

This also connects directly to the global LeBrun excess. The identity

\[
\frac{s^2}{24}+2|W^+|^2
 =\frac1{12}f^2
  +\frac1{216}(s+8\sqrt6|W^+|)^2
\]

shows that, if

\[
D=L-\frac23A,\qquad
L=\frac1{4\pi^2}\int
  \left(\frac{s^2}{24}+2|W^+|^2\right)d\mu,
\]

then LeBrun’s estimate gives

\[
\int\mathcal G\,d\mu\le48\pi^2D,
\qquad
\int(s+8\sqrt6|W^+|)^2\,d\mu\le864\pi^2D.
\]

The coefficient \(24\pi^2\) in Step 8 is consistent if
\(\xi(Q+P)=\mathcal G/2\). Since \(Q,P\) are not displayed, that exact numerical coefficient cannot be recovered from the supplied note, but the weaker coefficient above is sufficient for the theorem.

### 3. Local averaging with local means

Let

\[
H(p)=\frac1{\operatorname{Vol}B_R(p)}
      \int_{B_R(p)}F\,d\mu.
\]

Fubini gives

\[
\frac1{\operatorname{Vol}M}\int_M H(p)\,d\mu(p)
=
\frac1{\operatorname{Vol}M}\int_M F(x)
 \left[
 \int_{B_R(x)}
 \frac{d\mu(p)}{\operatorname{Vol}B_R(p)}
 \right]d\mu(x).
\]

If \(d(p,x)\le R\), then

\[
B_R(x)\subset B_{2R}(p).
\]

Under \(\operatorname{Ric}\ge-(n-1)Kg\), Bishop–Gromov gives

\[
\operatorname{Vol}B_{2R}(p)
 \le D(n,K,R)\operatorname{Vol}B_R(p),
\]

and therefore

\[
\frac1{\operatorname{Vol}B_R(p)}
 \le
\frac{D(n,K,R)}{\operatorname{Vol}B_R(x)}.
\]

The inner bracket is at most \(D(n,K,R)\), proving

\[
\frac1{\operatorname{Vol}M}\int_M H
\le
D(n,K,R)
\frac1{\operatorname{Vol}M}\int_M F.
\]

If \(\operatorname{Vol}E_i(v)\ge\eta\operatorname{Vol}M_i\), then

\[
\frac1{\operatorname{Vol}E_i(v)}
\int_{E_i(v)}H_i
\le
\frac{D}{\eta}
\frac1{\operatorname{Vol}M_i}\int_{M_i}F_i\to0.
\]

Hence points \(p_i\in E_i(v)\) with \(H_i(p_i)\to0\) exist. This restricted-set step is implicit in the note and is valid.

The near-Einstein assumption supplies all uniform geometric constants:

\[
\operatorname{Ric}_{g_i}\ge-(1+\delta_i)g_i,
\qquad
|\operatorname{Ric}_{g_i}|_{g_i}\le2(1+\delta_i)<3
\]

for large \(i\). Bishop–Gromov also gives

\[
\operatorname{Vol}B_{1/2}(p_i)\ge c(v)>0
\]

and a uniform upper bound for \(\operatorname{Vol}B_1(p_i)\). Therefore

\[
\int_{B_1(p_i)}F_i\,d\mu_i\to0.
\]

### 4. Harmonic-coordinate convergence

Cheeger–Naber Theorem 1.13 supplies

\[
\operatorname{Vol}\!\left(
T_r\{x\in B_1(p_i):r_h(x)\le r\}
\right)\le C(v)r^4.
\]

Choosing \(r_0(v)>0\) so that \(C(v)r_0^4<c(v)\) shows that some

\[
q_i\in B_{1/2}(p_i)
\]

has \(r_h(q_i)\ge r_0\). After shrinking the harmonic coordinate domain, its image lies inside \(B_1(p_i)\).

On a fixed smaller Euclidean coordinate ball, the pulled-back metrics have uniform

\[
C^{1,\alpha}\cap W^{2,p}
\]

bounds for every finite \(p\). After subsequence extraction,

\[
g_i\to g_\infty\quad\text{strongly in }C^{1,\beta},
\qquad
g_i\rightharpoonup g_\infty\quad\text{in }W^{2,p}.
\]

In harmonic coordinates,

\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
 =-2(\operatorname{Ric}_{g_i})_{jk}
  +Q_{jk}(g_i^{-1},\partial g_i).
\]

Since

\[
\operatorname{Ric}_{g_i}=-g_i+e_i,\qquad
\|e_i\|_{L^\infty}\to0,
\]

and \(g_i\to g_\infty\) in \(C^{1,\beta}\), the right-hand sides converge strongly in \(L^p\), in fact uniformly apart from the second derivatives hidden on the left. Interior estimates for the difference equation then give

\[
g_i\to g_\infty
\quad\text{strongly in }W^{2,p}
\]

on a further-shrunken chart.

The limiting metric satisfies

\[
\operatorname{Ric}_{g_\infty}=-g_\infty
\]

weakly. The harmonic-coordinate Einstein equation then bootstraps \(g_\infty\) to smoothness. No estimate for \(\nabla\operatorname{Ric}_{g_i}\) is used. The approximating metrics need not have uniform \(C^{2,\alpha}\) bounds.

For \(p>2\), strong \(W^{2,p}\) convergence yields strong \(L^p\) convergence of curvature; taking larger finite \(p\) handles all algebraic products. After an almost-everywhere subsequence,

\[
W_i^+\to W_\infty^+,\qquad
s_i\to s_\infty,\qquad
w_i\to w_\infty.
\]

The induced orientations on the charts should be chosen consistently, so that \(W_i^+\) converges to \(W_\infty^+\). Zero integral of the deficit densities gives the corresponding identities almost everywhere; smoothness of \(g_\infty\) makes them hold everywhere.

### 5. Exact conclusion

Assuming a fixed \(v>0\) and a positive lower relative volume for \(E_i(v)\) produces the smooth local Einstein limit above and hence the Derdziński contradiction. Therefore

\[
\frac{\operatorname{Vol}E_i(v)}
     {\operatorname{Vol}M_i}\to0
\qquad
\text{for every fixed }v>0.
\]

Equivalently, for a volume-random point \(p_i\),

\[
\operatorname{Vol}B_1(p_i)\to0
\]

in probability. This does not imply

\[
\sup_{p\in M_i}\operatorname{Vol}B_1(p)\to0
\]

or eventual emptiness of \(E_i(v)\). Regions of relative volume \(o(1)\) may remain noncollapsed and may contain topology or concentrated curvature.

The only substantive documentation gap is the absence of explicit formulas for \(Q_i,P_i\) and their relation to the LeBrun excess. Replacing that term by the canonical density \(\mathcal G_i\) above makes the local spectral passage independently verifiable. Subject to the quoted global deficit and volume asymptotics, no normalization or compactness issue invalidates the measure-local theorem.