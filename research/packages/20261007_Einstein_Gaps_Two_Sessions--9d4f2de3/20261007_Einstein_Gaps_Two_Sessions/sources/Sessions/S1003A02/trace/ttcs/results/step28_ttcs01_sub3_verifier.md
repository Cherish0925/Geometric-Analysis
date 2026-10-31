# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/scripts/chiral_flux_identity.py",
    "Sessions/S1003A02/workspace/data/chiral_flux.json",
    "Sessions/S1003A02/workspace/scripts/chiral_flux_models.py",
    "Sessions/S1003A02/workspace/data/chiral_flux_models.json",
    "Sessions/S1003A01/workspace/scripts/perp_cartan_verify.py"
  ]
}
```

## Task

Independently verify Theorem X in the supplied Step-27 note. Check the orientation and normalization of the two chiral curvature blocks, the derivation of the signature transgression from the displayed exact formula/data/script, both localized identities, and every entry of the charge table (smooth centre, O(-1) bolt, Berger collapse, CH, Burns, Taub-bolt). Look especially for constant shifts, sign reversals, or a false identification of block A with W+ in the blow-up orientation. Give a direct mathematical verification rather than accepting the zero symbolic residual.

## Output

# Scientific verification memo

## 1. Result

The chiral assignment, additive normalization, localized identities, and all requested charges are mutually consistent. In particular:

- block \(A\) is \(W^+\) for the orientation \(e^{0123}>0\);
- this is the complex orientation of the CH and Burns metrics and the orientation in which the bolt has self-intersection \(-1\);
- the normalized signature transgression is
  \[
  \mathfrak s=S_0-6,
  \]
  where the large rational expression in `chiral_flux.json` has the compact form
  \[
  \boxed{
  S_0=\sum_i p_i^2-\sum_{\rm cyc}\gamma_i p_jp_k
       +2\sum_i\gamma_i^2;
  }
  \]
- directly from the Cartan connection,
  \[
  S_0'=\frac W2(B_A-B_B);
  \]
- consequently \(\mathfrak b_+=\mathfrak b-\mathfrak s\) is the \(W^+\) flux and \(\mathfrak b_-=\mathfrak b+\mathfrak s\) is the \(W^-\) flux;
- all entries in the charge table, as well as the Burns and Taub-bolt balances, follow with the displayed signs.

There is one factor-of-two error in the prose immediately after Theorem X: the integrated Hitchin–Thorpe identity has \(4\pi^2(2\chi\pm3\tau)\), not \(8\pi^2(2\chi\pm3\tau)\). The subsequent closed-manifold formula for \(\widehat P\) is nevertheless the correct one.

---

## 2. Chiral blocks, norm convention, and orientation

Let
\[
e^0=dt,\qquad e^1=a\sigma_1,\qquad e^2=b\sigma_2,\qquad e^3=c\sigma_3
\]
with orientation \(e^{0123}>0\). Then
\[
*e^{01}=e^{23},\qquad *e^{02}=e^{31},\qquad *e^{03}=e^{12}.
\]
Hence the rows of `LA` are exactly the orthonormal self-dual basis
\[
\omega_1^+=\frac{e^{01}+e^{23}}{\sqrt2},\quad
\omega_2^+=\frac{e^{02}+e^{31}}{\sqrt2},\quad
\omega_3^+=\frac{e^{03}+e^{12}}{\sqrt2},
\]
while `LB` gives the anti-self-dual basis. Therefore
\[
W_A=W|_{\Lambda^+},\qquad W_B=W|_{\Lambda^-}.
\]

The block norm convention is
\[
B_A=\operatorname{tr}(W_A^2)=|W^+|^2,\qquad
B_B=\operatorname{tr}(W_B^2)=|W^-|^2,
\]
where the Weyl norm is the Hilbert–Schmidt norm of the curvature operator on \(\Lambda^2\). With
\[
dV=2\pi^2W\,dt,
\]
this gives
\[
\frac1{2\pi^2}\int_C|W^\pm|^2\,dV
 =\int_{t_0}^{t_1}W B_{A/B}\,dt.
\]
Equivalently,
\[
\frac1{4\pi^2}\int_C|W|^2\,dV
 =\frac12\int_{t_0}^{t_1}W(B_A+B_B)\,dt,
\]
exactly as stated in the note. If one instead uses the raw four-index contraction \(\sum W_{ijkl}^2\), it is four times this operator norm.

### CH orientation

For the CH profiles
\[
a=\sinh t\cosh t,\qquad b=c=\sinh t,
\]
the two-form
\[
\omega=e^{01}+e^{23}
\]
is self-dual. Moreover,
\[
d\omega
 =\left(\frac{b'}b+\frac{c'}c-\frac{2a}{bc}\right)e^{023}=0.
\]
Thus this is the Kähler form and the frame orientation is the CH complex orientation.

Since \(s=-24\), the Kähler \(W^+\)-eigenvalues are
\[
\frac s6,\ -\frac{s}{12},\ -\frac{s}{12}=(-4,2,2),
\]
so
\[
B_A=16+4+4=24.
\]
Complex hyperbolic space is a complex space form, hence \(W^-=0\), giving
\[
B_B=0.
\]
This independently fixes \(A=W^+\); exchanging the blocks would contradict the Kähler curvature decomposition.

### Blow-up orientation

For Burns, with fibre in the \(c\)-slot,
\[
a=b=r,\qquad c=r\sqrt{1-r^{-2}},
\]
the Kähler form is
\[
\omega_{\rm B}=e^{03}+e^{12}.
\]
It is self-dual and
\[
d\omega_{\rm B}
 =\left(\frac{a'}a+\frac{b'}b-\frac{2c}{ab}\right)e^{012}=0.
\]
Burns is the scalar-flat Kähler metric on the complex blow-up of \(\mathbb C^2\), whose exceptional sphere has self-intersection \(-1\). Therefore \(e^{0123}\) is precisely the blow-up orientation. A cyclic permutation moving the fibre from \(c\) to \(a\) preserves the orbit orientation, so the bolt computation in `chiral_flux_identity.py` uses the same orientation.

---

## 3. Direct derivation of the signature transgression

Write \(a_1=a,a_2=b,a_3=c\), with cyclic \((i,j,k)\), and
\[
p_i=a_i',\qquad
\gamma_i=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k}.
\]

### 3.1 Compact form of the JSON expression

Grouping the velocity terms in the displayed numerator from `chiral_flux.json` gives
\[
p_1^2+p_2^2+p_3^2
-\gamma_1p_2p_3-\gamma_2p_3p_1-\gamma_3p_1p_2.
\]
For example, the coefficient of \(p_2p_3\) is
\[
\frac{a^2}{bc}-\frac bc-\frac cb
=-\frac{b^2+c^2-a^2}{bc}
=-\gamma_1.
\]
The velocity-free terms are exactly
\[
2(\gamma_1^2+\gamma_2^2+\gamma_3^2).
\]
Thus the field `S` is
\[
S_0=\sum_i p_i^2-\sum_{\rm cyc}\gamma_i p_jp_k
       +2\sum_i\gamma_i^2.
\]

The \(\gamma_i\) obey the algebraic identity
\[
\boxed{
\gamma_1^2+\gamma_2^2+\gamma_3^2+\gamma_1\gamma_2\gamma_3=4.
}
\tag{3.1}
\]
This is the usual identity for \(\gamma_i=2\cos A_i\), or it follows directly after clearing the denominator \(a^2b^2c^2\).

### 3.2 Connection and curvature coefficients

Cartan’s first equation gives
\[
\omega_{0i}=-p_i\sigma_i,\qquad
\omega_{jk}=\gamma_i\sigma_i.
\]
Consequently
\[
\Omega_{0i}
=-p_i'\,dt\wedge\sigma_i
+\bigl(-2p_i+\gamma_jp_k+\gamma_kp_j\bigr)\sigma_j\wedge\sigma_k,
\]
and
\[
\Omega_{jk}
=\gamma_i'\,dt\wedge\sigma_i
+\bigl(2\gamma_i-p_jp_k-\gamma_j\gamma_k\bigr)
 \sigma_j\wedge\sigma_k.
\]
Pair symmetry gives the useful differential identity
\[
\boxed{
\frac{\gamma_i'}{a_i}
=\frac{-2p_i+\gamma_jp_k+\gamma_kp_j}{a_ja_k}.
}
\tag{3.2}
\]

Set
\[
X_i=R_{0i0i}=-\frac{p_i'}{a_i},\qquad
Y_i=R_{jkjk}
 =\frac{2\gamma_i-p_jp_k-\gamma_j\gamma_k}{a_ja_k},
\]
and
\[
Q_i=R_{0ijk}=\frac{\gamma_i'}{a_i}.
\]
The first Bianchi identity gives
\[
Q_1+Q_2+Q_3=0.
\]

In the self-dual and anti-self-dual bases, the diagonal Weyl entries are
\[
(W_A)_{ii}=\frac{X_i+Y_i}{2}+Q_i-\frac{s}{12},
\qquad
(W_B)_{ii}=\frac{X_i+Y_i}{2}-Q_i-\frac{s}{12}.
\]
It follows that
\[
\frac12(B_A-B_B)
=\sum_i(X_i+Y_i)Q_i,
\tag{3.3}
\]
because the scalar contribution vanishes after summing \(\sum_iQ_i=0\).

Multiplying (3.3) by \(W=a_1a_2a_3\),
\[
\frac W2(B_A-B_B)
=\sum_i\left[
-\frac{a_ja_k}{a_i}p_i'\gamma_i'
+\bigl(2\gamma_i-p_jp_k-\gamma_j\gamma_k\bigr)\gamma_i'
\right].
\tag{3.4}
\]

### 3.3 Differentiating \(S_0\)

Differentiation gives
\[
S_0'
=\sum_i
\bigl(2p_i-\gamma_jp_k-\gamma_kp_j\bigr)p_i'
+\sum_i(-p_jp_k+4\gamma_i)\gamma_i'.
\]
Using (3.2),
\[
2p_i-\gamma_jp_k-\gamma_kp_j
=-\frac{a_ja_k}{a_i}\gamma_i'.
\]
Hence
\[
S_0'
=\sum_i\left[
-\frac{a_ja_k}{a_i}p_i'\gamma_i'
+(-p_jp_k+4\gamma_i)\gamma_i'
\right].
\]
The difference between this and (3.4) is
\[
\sum_i(2\gamma_i+\gamma_j\gamma_k)\gamma_i'
=\frac d{dt}
 \left(\sum_i\gamma_i^2+\gamma_1\gamma_2\gamma_3\right)=0
\]
by (3.1). Therefore
\[
\boxed{
S_0'=\frac W2(B_A-B_B).
}
\]

Since an additive constant does not affect the derivative, the normalized transgression
\[
\boxed{\mathfrak s=S_0-6}
\]
has the same derivative.

---

## 4. Derivation and normalization of the localized identities

Let \(\mathfrak b\) be the Euler transgression
\[
\mathfrak b
=W\left(\sum_i\frac{p_i}{a_i}K_i
-\frac{p_1p_2p_3}{a_1a_2a_3}\right),
\]
where
\[
K_i=
\frac{(a_j^2-a_k^2)^2
+2a_i^2(a_j^2+a_k^2)-3a_i^4}
 {a_i^2a_j^2a_k^2}.
\]
The Cartan Euler form gives
\[
B_A+B_B-\frac12|\operatorname{Ric}^\circ|^2+\frac{s^2}{24}
=-\frac{2}{W}\mathfrak b'.
\]
Equivalently,
\[
\frac W4|\operatorname{Ric}^\circ|^2
=\mathfrak b'
+\frac W2(B_A+B_B)+\frac W{48}s^2.
\tag{4.1}
\]

Define
\[
\mathfrak b_+=\mathfrak b-\mathfrak s,\qquad
\mathfrak b_-=\mathfrak b+\mathfrak s.
\]
Using \(\mathfrak s'=W(B_A-B_B)/2\), equation (4.1) becomes
\[
\frac W4|\operatorname{Ric}^\circ|^2
=\mathfrak b_+'+WB_A+\frac W{48}s^2,
\]
and
\[
\frac W4|\operatorname{Ric}^\circ|^2
=\mathfrak b_-'+WB_B+\frac W{48}s^2.
\]

Since
\[
\widehat P(C)=\int_{t_0}^{t_1}\frac W4|\operatorname{Ric}^\circ|^2\,dt,
\]
and \(dV=2\pi^2W\,dt\), integration gives
\[
\boxed{
\widehat P(C)
=\Delta\mathfrak b_+
+\frac1{2\pi^2}\int_C|W^+|^2\,dV
+\frac1{96\pi^2}\int_Cs^2\,dV,
}
\]
and
\[
\boxed{
\widehat P(C)
=\Delta\mathfrak b_-
+\frac1{2\pi^2}\int_C|W^-|^2\,dV
+\frac1{96\pi^2}\int_Cs^2\,dV.
}
\]

Thus the signs in Theorem X are correct.

---

## 5. Charge table

### 5.1 Smooth centre

Smoothness gives
\[
a_i=t+O(t^3),\qquad p_i\to1,\qquad \gamma_i\to1.
\]
Therefore
\[
S_0\to3-3+6=6,\qquad \mathfrak s\to0.
\]
For the exact Euclidean cone,
\[
K_i=t^{-2},\qquad W=t^3,\qquad p_i/a_i=t^{-1},
\]
so
\[
\mathfrak b=t^3\left(\frac3{t^3}-\frac1{t^3}\right)=2.
\]
Hence
\[
\boxed{\mathfrak b=2,\qquad \mathfrak b_+=2,\qquad\mathfrak b_-=2.}
\]

### 5.2 Regular \(O(-1)\) bolt

With fibre in the \(a\)-slot,
\[
a=t+O(t^3),\qquad
b=\beta+Bt^2+O(t^4),\qquad
c=\beta+Ct^2+O(t^4).
\]
Then
\[
(p_1,p_2,p_3)\to(1,0,0),\qquad
(\gamma_1,\gamma_2,\gamma_3)\to(2,0,0),
\]
independently of \(B-C\). Thus
\[
S_0\to1+2(2^2)=9,\qquad \mathfrak s\to3.
\]
In the Euler flux, only the fibre term survives at zeroth order:
\[
K_1\to\frac4{\beta^2},\qquad
W\frac{p_1}{a}K_1\to
(t\beta^2)\frac1t\frac4{\beta^2}=4.
\]
All other terms are \(O(t^2)\). Therefore
\[
\boxed{\mathfrak b=4,\qquad
       \mathfrak b_+=1,\qquad
       \mathfrak b_-=7.}
\]

For a compact radial truncation of the disc bundle,
\[
\chi=2,\qquad \tau=-1,
\]
and indeed
\[
2\chi+3\tau=1,\qquad 2\chi-3\tau=7.
\]

### 5.3 Hopf-collapsed Berger orbit

Take
\[
a=\varepsilon,\qquad b=c=R,\qquad
p_a=\frac{\varepsilon V}{R},\qquad p_b=p_c=U.
\]
Writing \(x=\varepsilon/R\),
\[
\gamma_a=2-x^2,\qquad \gamma_b=\gamma_c=x.
\]
Substitution into the compact formula gives
\[
S_0
=8+x^2(U^2-2UV+V^2-4)+2x^4.
\]
Therefore
\[
\mathfrak s
=2+x^2(U^2-2UV+V^2-4)+2x^4.
\]
The Euler flux is
\[
\mathfrak b
=-x(U^2V-4V)+x^3(2U-3V).
\]
For bounded \(U,V\),
\[
\mathfrak s\to2,\qquad \mathfrak b\to0.
\]
Thus
\[
\boxed{\mathfrak b=0,\qquad
       \mathfrak b_+=-2,\qquad
       \mathfrak b_-=2.}
\]

### 5.4 Complex hyperbolic orbit

Put \(u=\sinh^2t\). Then
\[
a=\sinh t\cosh t,\qquad b=c=\sinh t,
\]
and
\[
p_a=1+2u,\qquad p_b=p_c=\cosh t,
\]
\[
\gamma_a=1-u,\qquad \gamma_b=\gamma_c=\cosh t.
\]
Direct substitution gives
\[
S_0=6+3u^2,\qquad \mathfrak s=3u^2=3\sinh^4t.
\]
The Euler flux evaluates to
\[
\mathfrak b=2-6u^2=2-6\sinh^4t.
\]
Hence
\[
\boxed{
\mathfrak b_+=2-9\sinh^4t,\qquad
\mathfrak b_-=2-3\sinh^4t.
}
\]

This also gives a direct sign test:
\[
\mathfrak s'=12\sinh^3t\cosh t,
\]
while \(W=\sinh^3t\cosh t\) and \(B_A-B_B=24\), so
\[
\mathfrak s'=\frac W2(B_A-B_B).
\]
Interchanging \(A\) and \(B\) would reverse this equality.

### 5.5 Isotropic real-hyperbolic profiles

For \(a=b=c=f(t)\),
\[
\gamma_i=1,\qquad p_i=f'.
\]
Thus
\[
S_0=3(f')^2-3(f')^2+6=6,
\]
so \(\mathfrak s=0\) for every isotropic normalization. Consequently
\[
\mathfrak b_+=\mathfrak b_-=\mathfrak b_H.
\]

---

## 6. Burns model

Set
\[
f=1-r^{-2},\qquad
a=b=r,\qquad c=r\sqrt f,\qquad dt=\frac{dr}{\sqrt f}.
\]
Then
\[
p_a=p_b=\sqrt f,\qquad p_c=1,
\]
and
\[
\gamma_a=\gamma_b=\sqrt f,\qquad
\gamma_c=1+r^{-2}.
\]
The compact transgression gives
\[
\mathfrak s=\frac3{r^4}.
\]
Direct evaluation of the Euler flux gives
\[
\mathfrak b=2+\frac2{r^4}.
\]
Therefore
\[
\mathfrak b_+=2-\frac1{r^4},\qquad
\mathfrak b_-=2+\frac5{r^4}.
\]
At \(r=1\),
\[
(\mathfrak b_+,\mathfrak b_-)=(1,7),
\]
and at infinity,
\[
(\mathfrak b_+,\mathfrak b_-)=(2,2).
\]

The self-dual Kähler argument gives \(B_A=0\), and direct curvature substitution gives
\[
s=0,\qquad
|\operatorname{Ric}^\circ|^2=\frac{16}{r^8},\qquad
B_B=\frac{24}{r^8}.
\]
The radial volume factor is
\[
W\,dt=abc\,dt=r^3\,dr.
\]
Hence
\[
\widehat P
=\int_1^\infty \frac{r^3}{4}\frac{16}{r^8}\,dr
=4\int_1^\infty r^{-5}\,dr=1,
\]
and
\[
\int_1^\infty W B_A\,dt=0,
\]
\[
\int_1^\infty W B_B\,dt
=24\int_1^\infty r^{-5}\,dr=6.
\]
The two chiral balances are therefore
\[
1=(2-1)+0,
\]
and
\[
1=(2-7)+6.
\]
Thus the Burns row, its chirality, and the sharp value \(\widehat P=1\) are correct.

---

## 7. Taub-bolt model

For \(n=1\),
\[
a=b=2\sqrt{r^2-1},\qquad
c=4\sqrt V,\qquad
V=\frac{r^2-\frac52r+1}{r^2-1},\qquad
dt=\frac{dr}{\sqrt V}.
\]

At \(r=2\),
\[
V(2)=0,\qquad V'(2)=\frac12.
\]
Thus \(p_c=2V'\to1\), while \(p_a,p_b\to0\). Consequently
\[
(p_a,p_b,p_c)\to(0,0,1),\qquad
(\gamma_a,\gamma_b,\gamma_c)\to(0,0,2),
\]
so
\[
\mathfrak s\to3,\qquad \mathfrak b\to4,
\]
and
\[
(\mathfrak b_+,\mathfrak b_-)\to(1,7).
\]

At infinity,
\[
p_a,p_b\to2,\qquad p_c\to0,\qquad
\gamma_a,\gamma_b\to0,\qquad\gamma_c\to2.
\]
Hence
\[
S_0\to8,\qquad \mathfrak s\to2,\qquad \mathfrak b\to0,
\]
and
\[
(\mathfrak b_+,\mathfrak b_-)\to(-2,2).
\]

Direct substitution in the curvature formulas gives
\[
\operatorname{Ric}=0,
\]
\[
B_A=\frac{243}{8(r+1)^6},\qquad
B_B=\frac{3}{8(r-1)^6}.
\]
The radial volume factor is
\[
W\,dt
=abc\,\frac{dr}{\sqrt V}
=16(r^2-1)\,dr.
\]
Therefore
\[
\int_2^\infty WB_A\,dt
=486\int_2^\infty\frac{r-1}{(r+1)^5}\,dr
=3,
\]
and
\[
\int_2^\infty WB_B\,dt
=6\int_2^\infty\frac{r+1}{(r-1)^5}\,dr
=5.
\]
Since \(\widehat P=0\),
\[
0=(-2-1)+3,
\qquad
0=(2-7)+5.
\]
Thus the block assignment and the Taub-bolt charge balance are exact.

---

## 8. Additive shift in the stored data

`chiral_flux.json` stores the unshifted \(S_0\). Its fields `bA` and `bB` are therefore
\[
bA_{\rm JSON}=\mathfrak b-S_0,\qquad
bB_{\rm JSON}=\mathfrak b+S_0.
\]
The theorem’s normalized fluxes are
\[
\boxed{
\mathfrak b_+=bA_{\rm JSON}+6,\qquad
\mathfrak b_-=bB_{\rm JSON}-6.
}
\]
For example, the JSON CH values
\[
bA_{\rm JSON}=-4-9\sinh^4t,\qquad
bB_{\rm JSON}=8-3\sinh^4t
\]
become
\[
\mathfrak b_+=2-9\sinh^4t,\qquad
\mathfrak b_-=2-3\sinh^4t.
\]
`chiral_flux_models.py` applies exactly this shift through `Sn = S_sol - 6`.

---

## 9. Hitchin–Thorpe coefficient

With the norm convention used here, the correct formula is
\[
\boxed{
4\pi^2(2\chi\pm3\tau)
=\int_M\left(
2|W^\pm|^2+\frac{s^2}{24}
-\frac{|\operatorname{Ric}^\circ|^2}{2}
\right)dV.
}
\]
Solving for
\[
\widehat P=\frac1{8\pi^2}\int_M|\operatorname{Ric}^\circ|^2\,dV
\]
gives
\[
\boxed{
\widehat P
=\frac1{2\pi^2}\int_M|W^\pm|^2\,dV
+\frac1{96\pi^2}\int_Ms^2\,dV
-(2\chi\pm3\tau),
}
\]
which agrees with the closed-manifold formula in the note. Thus only the preceding \(8\pi^2(2\chi\pm3\tau)\) text needs replacement by \(4\pi^2(2\chi\pm3\tau)\).

Overall, there is no block interchange or sign reversal in Theorem X. The sole substantive textual correction is this Hitchin–Thorpe prefactor; the theorem, charge table, Burns computation, and Taub-bolt computation retain their stated constants.