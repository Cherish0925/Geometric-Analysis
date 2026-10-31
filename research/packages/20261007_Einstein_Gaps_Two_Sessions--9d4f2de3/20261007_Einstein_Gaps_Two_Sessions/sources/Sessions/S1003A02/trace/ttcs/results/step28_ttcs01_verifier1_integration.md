# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 28,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step28_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step28_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify Theorem X in the supplied Step-27 note. Check the orientation and normalization of the two chiral curvature blocks, the derivation of the signature transgression from the displayed exact formula/data/script, both localized identities, and every entry of the charge table (smooth centre, O(-1) bolt, Berger collapse, CH, Burns, Taub-bolt). Look especially for constant shifts, sign reversals, or a false identification of block A with W+ in the blow-up orientation. Give a direct mathematical verification rather than accepting the zero symbolic residual.

## Integrated Scientific Memo

# Verification of Theorem X

## Verdict

The chiral transgression identities, their signs, and the smooth-centre, \(O(-1)\)-bolt, CH, Burns, and Taub-bolt charges are correct after one keeps track of the additive normalization
\[
\mathfrak s=S_0-6.
\]
Block \(A\) is indeed \(W^+\) in the orientation
\[
e^{0123}=dt\wedge a\sigma_1\wedge b\sigma_2\wedge c\sigma_3>0,
\]
and this is both the CH complex orientation and the Burns blow-up orientation, in which the exceptional sphere has self-intersection \(-1\). There is no hidden interchange \(A\leftrightarrow W^-\).

Three qualifications/corrections are required:

1. The prose Hitchin–Thorpe formula has a factor-of-two error: its left side must be \(4\pi^2(2\chi\pm3\tau)\), not \(8\pi^2(2\chi\pm3\tau)\). The following formula for \(\widehat P\) is correct.
2. `chiral_flux.json` stores the unshifted \(S_0\), so its `bA,bB` entries are not the normalized \(\mathfrak b_\pm\): one must add \(6\) to `bA` and subtract \(6\) from `bB`.
3. The Berger row \((-2,2)\) is valid only under the stated biaxial/near-biaxial bounded-normalized-jet collapse. It is not a universal charge for arbitrary anisotropic collapsed orbits without additional control such as \(|b-c|=O(\varepsilon)\).

There is also a false sentence outside Theorem X in Corollary X2: subthreshold cells are not compatible with CH-shaped orbits at *every* positive CH radius; sufficiently small CH radii are excluded.

---

## 1. Orientation and normalization of the curvature blocks

Use the orthonormal coframe
\[
e^0=dt,\qquad e^1=a\sigma_1,\qquad e^2=b\sigma_2,\qquad e^3=c\sigma_3
\]
and orientation \(e^{0123}>0\). Then
\[
*e^{01}=e^{23},\qquad *e^{02}=e^{31},\qquad *e^{03}=e^{12}.
\]
Thus the rows of `LA` in `chiral_flux_identity.py`,
\[
\frac{e^{01}+e^{23}}{\sqrt2},\quad
\frac{e^{02}+e^{31}}{\sqrt2},\quad
\frac{e^{03}+e^{12}}{\sqrt2},
\]
are an orthonormal basis of \(\Lambda^+\); the rows of `LB`, with minus signs, form a basis of \(\Lambda^-\). Therefore
\[
W_A=W|_{\Lambda^+},\qquad W_B=W|_{\Lambda^-}.
\]

The quantities
\[
B_A=\operatorname{tr}(W_A^2),\qquad B_B=\operatorname{tr}(W_B^2)
\]
are the Hilbert–Schmidt curvature-operator norms \(|W^+|^2\), \(|W^-|^2\). Since
\[
dV=2\pi^2abc\,dt=2\pi^2W\,dt,
\]
one has
\[
\frac1{2\pi^2}\int_C|W^\pm|^2\,dV
=\int_{t_0}^{t_1}W B_{A/B}\,dt,
\]
and hence
\[
\frac1{4\pi^2}\int_C|W|^2\,dV
=\frac12\int_{t_0}^{t_1}W(B_A+B_B)\,dt.
\]
This agrees with the normalization used by the scripts.

### CH fixes the chirality independently

For
\[
a=\sinh t\cosh t,\qquad b=c=\sinh t,
\]
the two-form
\[
\omega=e^{01}+e^{23}
\]
is self-dual and closed:
\[
d\omega=
\left(\frac{b'}b+\frac{c'}c-\frac{2a}{bc}\right)e^{023}=0.
\]
It is the CH Kähler form. Hence the chosen orientation is the complex orientation. Since \(s=-24\), the Kähler block has eigenvalues
\[
\frac{s}{6},-\frac{s}{12},-\frac{s}{12}=(-4,2,2),
\]
so
\[
B_A=24,\qquad B_B=0.
\]
Thus \(A=W^+\); reversing the assignment would contradict the Kähler decomposition.

### Burns fixes the blow-up orientation

For Burns,
\[
a=b=r,\qquad c=r\sqrt{1-r^{-2}},\qquad dt=\frac{dr}{\sqrt{1-r^{-2}}},
\]
the Kähler form is
\[
\omega_{\mathrm B}=e^{03}+e^{12},
\]
which is self-dual and closed. This is the complex orientation of the blow-up of \(\mathbb C^2\), in which the exceptional curve has square \(-1\). Consequently the frame orientation used by the computation is precisely the blow-up orientation, and \(A=W^+\) there as claimed.

---

## 2. Direct derivation of the signature transgression

Write \(a_i=(a,b,c)\), \(p_i=a_i'\), and cyclically
\[
\gamma_i=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k}.
\]

The long expression stored as `S` in `chiral_flux.json` simplifies to
\[
\boxed{
S_0=\sum_i p_i^2-\sum_{\rm cyc}\gamma_i p_jp_k
       +2\sum_i\gamma_i^2.
}
\tag{2.1}
\]
For example, the coefficient of \(p_2p_3\) is
\[
\frac{a_1^2}{a_2a_3}-\frac{a_2}{a_3}-\frac{a_3}{a_2}
=-\gamma_1.
\]
The velocity-free part is exactly \(2\sum\gamma_i^2\).

The \(\gamma_i\) satisfy
\[
\boxed{\sum_i\gamma_i^2+\gamma_1\gamma_2\gamma_3=4.}
\tag{2.2}
\]

Cartan’s first equation gives
\[
\omega_{0i}=-p_i\sigma_i,\qquad \omega_{jk}=\gamma_i\sigma_i.
\]
The curvature forms are
\[
\Omega_{0i}
=-p_i'\,dt\wedge\sigma_i
+\bigl(-2p_i+\gamma_jp_k+\gamma_kp_j\bigr)\sigma_j\wedge\sigma_k,
\]
\[
\Omega_{jk}
=\gamma_i'\,dt\wedge\sigma_i
+\bigl(2\gamma_i-p_jp_k-\gamma_j\gamma_k\bigr)\sigma_j\wedge\sigma_k.
\]
Pair symmetry yields
\[
\boxed{
\frac{\gamma_i'}{a_i}
=\frac{-2p_i+\gamma_jp_k+\gamma_kp_j}{a_ja_k}.
}
\tag{2.3}
\]

Define
\[
X_i=-\frac{p_i'}{a_i},\qquad
Y_i=\frac{2\gamma_i-p_jp_k-\gamma_j\gamma_k}{a_ja_k},
\qquad
Q_i=\frac{\gamma_i'}{a_i}.
\]
The Bianchi identity gives \(\sum_iQ_i=0\). In the chiral bases,
\[
(W_A)_{ii}=\frac{X_i+Y_i}{2}+Q_i-\frac{s}{12},
\]
\[
(W_B)_{ii}=\frac{X_i+Y_i}{2}-Q_i-\frac{s}{12}.
\]
Therefore
\[
\frac12(B_A-B_B)=\sum_i(X_i+Y_i)Q_i,
\]
the scalar terms cancelling because \(\sum_iQ_i=0\). Multiplying by \(W=a_1a_2a_3\),
\[
\frac W2(B_A-B_B)
=\sum_i\left[
-\frac{a_ja_k}{a_i}p_i'\gamma_i'
+\bigl(2\gamma_i-p_jp_k-\gamma_j\gamma_k\bigr)\gamma_i'
\right].
\tag{2.4}
\]

Differentiating (2.1) and using (2.3) gives
\[
S_0'
=\sum_i\left[
-\frac{a_ja_k}{a_i}p_i'\gamma_i'
+(-p_jp_k+4\gamma_i)\gamma_i'
\right].
\]
The difference between this and (2.4) is
\[
\sum_i(2\gamma_i+\gamma_j\gamma_k)\gamma_i'
=\frac d{dt}\left(\sum_i\gamma_i^2+
\gamma_1\gamma_2\gamma_3\right)=0
\]
by (2.2). Hence
\[
\boxed{S_0'=\frac W2(B_A-B_B).}
\]

The normalized signature transgression is therefore
\[
\boxed{\mathfrak s=S_0-6,}
\]
where the constant is chosen so that \(\mathfrak s=0\) at a smooth round centre.

---

## 3. Verification of both localized identities

The Euler transgression satisfies
\[
\frac W4|\operatorname{Ric}^{\circ}|^2
=\mathfrak b'
+\frac W2(B_A+B_B)+\frac W{48}s^2.
\tag{3.1}
\]
Define
\[
\mathfrak b_+=\mathfrak b-\mathfrak s,\qquad
\mathfrak b_-=\mathfrak b+\mathfrak s.
\]
Using
\[
\mathfrak s'=\frac W2(B_A-B_B),
\]
equation (3.1) becomes
\[
\frac W4|\operatorname{Ric}^{\circ}|^2
=\mathfrak b_+'+WB_A+\frac W{48}s^2,
\tag{3.2}
\]
and
\[
\frac W4|\operatorname{Ric}^{\circ}|^2
=\mathfrak b_-'+WB_B+\frac W{48}s^2.
\tag{3.3}
\]
Integrating and using \(dV=2\pi^2W\,dt\) gives
\[
\boxed{
\widehat P(C)=\Delta\mathfrak b_+
+\frac1{2\pi^2}\int_C|W^+|^2\,dV
+\frac1{96\pi^2}\int_Cs^2\,dV,
}
\]
\[
\boxed{
\widehat P(C)=\Delta\mathfrak b_-
+\frac1{2\pi^2}\int_C|W^-|^2\,dV
+\frac1{96\pi^2}\int_Cs^2\,dV.
}
\]
Thus the signs in Theorem X are correct: subtracting \(\mathfrak s\) isolates block \(A=W^+\), while adding it isolates block \(B=W^-\).

A useful equivalent Chern–Simons representation is obtained from
\[
u_i=p_i-\gamma_i,\qquad
C(u)=\sum_i u_i^2+u_1u_2u_3.
\]
One finds
\[
\boxed{\mathfrak b_+=2-C(u),}
\]
which supplies an independent structural explanation of the \(+\)-identity using the exact identity
\[
C' = W\sum_i r_iv_i
\]
already established in `perp_cartan_verify.py`.

---

## 4. Exact charge computations

### Smooth centre

At a smooth round centre,
\[
a_i=t+O(t^3),\qquad p_i\to1,\qquad\gamma_i\to1.
\]
Thus
\[
S_0\to3-3+6=6,\qquad\mathfrak s\to0.
\]
For the Euclidean cone, \(\mathfrak b=2\), hence
\[
\boxed{(\mathfrak b,\mathfrak b_+,\mathfrak b_-)=(2,2,2).}
\]

### Regular \(O(-1)\) bolt

With fibre in the \(a\)-slot,
\[
a=t+O(t^3),\qquad
b=\beta+Bt^2+O(t^4),\qquad
c=\beta+Ct^2+O(t^4),
\]
so
\[
p\to(1,0,0),\qquad \gamma\to(2,0,0).
\]
Consequently
\[
S_0\to1+2\cdot4=9,\qquad\mathfrak s\to3.
\]
The Euler flux has limit \(\mathfrak b\to4\), independent of the triaxial second-order jet. Therefore
\[
\boxed{(\mathfrak b,\mathfrak b_+,\mathfrak b_-)=(4,1,7).}
\]
These equal
\[
2\chi+3\tau=1,\qquad 2\chi-3\tau=7
\]
for \(\chi=2,\tau=-1\), confirming the orientation.

### Berger collapse

For the biaxial ansatz
\[
a=\varepsilon,\qquad b=c=R,\qquad
a'=\frac{\varepsilon V}{R},\qquad b'=c'=U,
\]
write \(x=\varepsilon/R\). Then
\[
\gamma_a=2-x^2,\qquad \gamma_b=\gamma_c=x,
\]
and direct substitution gives
\[
\mathfrak s
=2+x^2(U^2-2UV+V^2-4)+2x^4,
\]
\[
\mathfrak b
=-x(U^2V-4V)+x^3(2U-3V).
\]
For bounded \(U,V\),
\[
\boxed{(\mathfrak b,\mathfrak b_+,\mathfrak b_-)\to(0,-2,2).}
\]

This row is exact for the displayed biaxial collapse and persists for suitably controlled near-biaxial collapse. It should not be stated for unrestricted anisotropic collapse. If
\[
b=Re^{q/2},\qquad c=Re^{-q/2},
\]
then \(\gamma_b,\gamma_c\) can be of order \(Rq/\varepsilon\), and the leading fluxes acquire shear terms:
\[
\mathfrak b_+\approx-2-R^2\left(q'+\frac{4q}{\varepsilon}\right)^2,
\qquad
\mathfrak b_-\approx2+R^2\left(q'-\frac{4q}{\varepsilon}\right)^2.
\]
Thus equality with \((-2,2)\) needs control of the anisotropic mode; the symmetric Berger formula alone does not prove slot-symmetric universality for arbitrary collapsed jets.

### Complex hyperbolic orbit

Let \(u=\sinh^2t\). For
\[
a=\sinh t\cosh t,\qquad b=c=\sinh t,
\]
one obtains
\[
S_0=6+3u^2,\qquad
\mathfrak s=3u^2,
\]
and
\[
\mathfrak b=2-6u^2.
\]
Hence
\[
\boxed{
\mathfrak b_+=2-9\sinh^4t,\qquad
\mathfrak b_-=2-3\sinh^4t.
}
\]
Moreover
\[
\mathfrak s'=12\sinh^3t\cosh t
=\frac W2(24-0),
\]
which directly confirms both the sign and the assignment \(A=W^+\).

### Isotropic real-hyperbolic orbit

For \(a=b=c=f(t)\),
\[
\gamma_i=1,\qquad p_i=f',
\]
so
\[
S_0=3(f')^2-3(f')^2+6=6,\qquad\mathfrak s=0.
\]
Therefore
\[
\boxed{\mathfrak b_+=\mathfrak b_-=\mathfrak b_H.}
\]

---

## 5. Burns verification

For
\[
a=b=r,\qquad c=r\sqrt{1-r^{-2}},
\qquad dt=\frac{dr}{\sqrt{1-r^{-2}}},
\]
direct substitution gives
\[
\mathfrak s=\frac3{r^4},\qquad
\mathfrak b=2+\frac2{r^4},
\]
hence
\[
\mathfrak b_+=2-\frac1{r^4},\qquad
\mathfrak b_-=2+\frac5{r^4}.
\]
Thus
\[
(\mathfrak b_+,\mathfrak b_-)_{\rm bolt}=(1,7),\qquad
(\mathfrak b_+,\mathfrak b_-)_{\infty}=(2,2).
\]

The curvature quantities are
\[
s=0,\qquad B_A=0,\qquad B_B=\frac{24}{r^8},
\qquad |\operatorname{Ric}^{\circ}|^2=\frac{16}{r^8}.
\]
Since
\[
W\,dt=r^3\,dr,
\]
\[
\widehat P
=\int_1^\infty\frac{r^3}{4}\frac{16}{r^8}\,dr=1,
\]
\[
\int WB_A\,dt=0,\qquad
\int WB_B\,dt
=24\int_1^\infty r^{-5}\,dr=6.
\]
The localized identities read
\[
1=(2-1)+0,
\qquad
1=(2-7)+6.
\]
Thus Burns is scalar-flat Kähler with \(W^+=0\) in the blow-up orientation, and the stated sharp cost is correct.

---

## 6. Taub-bolt verification

For \(n=1\),
\[
a=b=2\sqrt{r^2-1},\qquad
c=4\sqrt V,\qquad
V=\frac{r^2-\frac52r+1}{r^2-1},
\qquad dt=\frac{dr}{\sqrt V}.
\]
At \(r=2\), \(V=0\) and \(V'(2)=1/2\), so \(c'=2V'\to1\); this is a regular bolt. The limiting data give
\[
(\mathfrak b,\mathfrak b_+,\mathfrak b_-)=(4,1,7).
\]
At infinity,
\[
\mathfrak b\to0,\qquad\mathfrak s\to2,
\]
so
\[
(\mathfrak b_+,\mathfrak b_-)\to(-2,2).
\]

The metric is Ricci-flat, and
\[
B_A=\frac{243}{8(r+1)^6},\qquad
B_B=\frac3{8(r-1)^6}.
\]
Moreover
\[
W\,dt=16(r^2-1)\,dr.
\]
Therefore
\[
\int_2^\infty WB_A\,dt
=486\int_2^\infty\frac{r-1}{(r+1)^5}\,dr=3,
\]
\[
\int_2^\infty WB_B\,dt
=6\int_2^\infty\frac{r+1}{(r-1)^5}\,dr=5.
\]
Since \(\widehat P=0\),
\[
0=(-2-1)+3,\qquad
0=(2-7)+5.
\]
The Taub-bolt charge balance is therefore exact and has the stated chirality. There is no orientation obstruction to using it as an \(O(-1)\) core.

---

## 7. Constant shift in the data file

`chiral_flux.json` stores \(S_0\), not \(\mathfrak s=S_0-6\). Consequently its fields are
\[
bA_{\rm JSON}=\mathfrak b-S_0,\qquad
bB_{\rm JSON}=\mathfrak b+S_0,
\]
whereas Theorem X uses
\[
\boxed{
\mathfrak b_+=bA_{\rm JSON}+6,\qquad
\mathfrak b_-=bB_{\rm JSON}-6.
}
\]
For example, the JSON Euclidean values are \((-4,8)\), not \((2,2)\), and its CH fields are
\[
-4-9\sinh^4t,\qquad 8-3\sinh^4t.
\]
After the shifts they become the theorem’s
\[
2-9\sinh^4t,\qquad 2-3\sinh^4t.
\]
`chiral_flux_models.py` correctly applies this normalization through `Sn = S_sol - 6`.

The note should therefore not cite the raw `bA,bB` fields as already normalized charges without explicitly stating this \(\pm6\) conversion.

---

## 8. Hitchin–Thorpe coefficient

In the conventions used here,
\[
\boxed{
4\pi^2(2\chi\pm3\tau)
=\int_M\left(
2|W^\pm|^2+\frac{s^2}{24}
-\frac{|\operatorname{Ric}^{\circ}|^2}{2}
\right)dV.
}
\]
The factor \(8\pi^2\) appearing in the prose after Theorem X is wrong. Solving for
\[
\widehat P=\frac1{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2\,dV
\]
gives
\[
\widehat P
=\frac1{2\pi^2}\int|W^\pm|^2\,dV
+\frac1{96\pi^2}\int s^2\,dV
-(2\chi\pm3\tau),
\]
which is exactly the subsequent formula in the note. Thus the error is confined to that displayed prefactor.

---

## 9. Consequential correction to Corollary X2

From the bolt charge \(\mathfrak b_+(0)=1\),
\[
\widehat P[0,t]\ge \mathfrak b_+(t)-1.
\]
For a CH-shaped orbit of radius \(\tau\),
\[
\mathfrak b_+(\tau)=2-9\sinh^4\tau.
\]
Thus a cell with total defect \(P<1\) can contain such an orbit only if
\[
2-9\sinh^4\tau\le1+P,
\]
or
\[
\boxed{\sinh^4\tau\ge\frac{1-P}{9}.}
\]
Hence the sentence saying that X2 is compatible with CH-like orbits “at every positive radius” is false. For \(P\to0\), CH-shaped orbits with
\[
\tau<\operatorname{arsinh}(9^{-1/4})\approx0.549
\]
are excluded. This does not alter Theorem X or the charge table.

## Final assessment

Theorem X itself is mathematically verified:

- \(A=W^+\), \(B=W^-\) in the CH/blow-up orientation;
- \(\mathfrak s'=W(B_A-B_B)/2\);
- both localized identities have the stated signs and coefficients;
- the centre, bolt, CH, Burns, and Taub-bolt values and balances are exact;
- the biaxial Berger limit is \((-2,2)\).

The necessary amendments are the \(4\pi^2\) Hitchin–Thorpe prefactor, explicit correction of the raw JSON \(\pm6\) offsets, and a qualification of the Berger charge when anisotropic collapse is allowed.