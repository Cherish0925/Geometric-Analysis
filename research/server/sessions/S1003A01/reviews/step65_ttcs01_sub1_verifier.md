# TTCS Independent Branch Record

```json
{
  "step_id": 65,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step64_homogeneous_zero_identity.md",
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md",
    "Sessions/S1003A01/workspace/notes/step64_exceptional_points_second_order_zero.md",
    "Sessions/S1003A01/workspace/scripts/spirit_step64_homogeneous_quadric_check.py",
    "Sessions/S1003A01/workspace/data/spirit_step64/homogeneous_quadric_comparison.json"
  ]
}
```

## Task

Independently verify the mathematical derivation in Spirit Step 64's homogeneous zero identity for Einstein almost-Kähler four-manifolds. Check the exact scalar Delta-q formula (G), all constants/sign conventions relative to the established Step-62 normalization, the passage to the leading polynomial identity H_m for a finite-order torsion zero f_m=z h(bar z)+g(bar z), and the claimed all-orders classification f_m=kappa (bar z_2)^m e_1 for m>=2. Pay particular attention to the bidegree separation, the argument forcing h=0, the Hermitian form tr(conjugate(M)M), maximal totally isotropic dimension, integration/mixed-partial argument, and whether any exceptional polynomial cases were missed. State exactly what is proved and what still depends on unproved formal/gauge assumptions.

## Output

# Verification memo

## 1. Main result

With the Step-62 conventions
\[
\Delta=\operatorname{tr}\nabla^2,\qquad
u=\Omega/\sqrt2,\qquad
q=|\nabla\Omega|^2,
\]
and
\[
W^+=
\begin{pmatrix}
r&\eta^T\\
\eta&-\frac r2I+V
\end{pmatrix},
\qquad r=\frac s6+\frac q4,
\]
the scalar identity
\[
\boxed{
\Delta q
=
8\operatorname{tr}(V^2)-24|\eta|^2
-\frac{3s}{2}q-\frac94q^2
+16\sum_i\left\langle(\nabla_iW^+)\nabla_i u,u\right\rangle
}
\tag{G}
\]
is correct, including every coefficient and sign.

Assuming the established principal half-twistor equation and the leading coframe dictionary extend to a finite-order zero with the indicated remainder orders, its degree \(2m-2\) part is exactly
\[
\boxed{
\|A\|^2-\|S\|^2-8|h|^2
-6\operatorname{Re}\sum_j\overline{f_j}\,\partial_{w_j}h=0.
}
\tag{H_m}
\]

For \(m\ge2\), the algebraic consequences of \((H_m)\) are complete: every nonzero leading polynomial is, after a unitary frame change,
\[
\boxed{f_m(z)=\kappa\,(\bar z_2)^m e_1,\qquad \kappa\ne0.}
\tag{L_m}
\]
No exceptional polynomial family is omitted in this algebraic classification.

---

## 2. Exact derivation of \((G)\)

Set
\[
T:=\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle .
\]
The supplied equations are
\[
\Delta u=-2W^+u+\frac s3u,
\qquad
\Delta W^+=\frac s2W^+-6(W^+)^2+2|W^+|^2I.
\]

For the block decomposition,
\[
|W^+|^2=\frac32r^2+2|\eta|^2+\operatorname{tr}(V^2),
\qquad
\langle(W^+)^2u,u\rangle=r^2+|\eta|^2.
\]
Consequently,
\[
\begin{aligned}
\langle(\Delta W^+)u,u\rangle
&=\frac s2r-6(r^2+|\eta|^2)+2|W^+|^2\\
&=\frac s2r-3r^2-2|\eta|^2+2\operatorname{tr}(V^2).
\end{aligned}
\]

The product rule gives
\[
\begin{aligned}
\Delta r
={}&\langle(\Delta W^+)u,u\rangle
+4T
+2\langle W^+\Delta u,u\rangle\\
&\quad+2\sum_i\langle W^+\nabla_i u,\nabla_i u\rangle .
\end{aligned}
\]
The third term is
\[
2\langle W^+\Delta u,u\rangle
=-4(r^2+|\eta|^2)+\frac{2s}{3}r.
\]

The AAD algebra implies
\[
\sum_i(\nabla_i u)\otimes(\nabla_i u)
=\frac q4I_{u^\perp}.
\]
Since \(\operatorname{tr}_{u^\perp}W^+=-r\),
\[
2\sum_i\langle W^+\nabla_i u,\nabla_i u\rangle
=-\frac q2r.
\]
Combining the four contributions,
\[
\Delta r
=\frac{7s}{6}r-7r^2-\frac q2r
-6|\eta|^2+2\operatorname{tr}(V^2)+4T.
\tag{2.1}
\]

Because \(s\) is constant and \(r=s/6+q/4\),
\[
\Delta r=\frac14\Delta q.
\]
Direct substitution gives
\[
\frac{7s}{6}r-7r^2-\frac q2r
=-\frac{3s}{8}q-\frac{9}{16}q^2.
\]
Multiplying (2.1) by four proves \((G)\).

This also recovers the Step-62 identity at a first-order zero: there \(q=0\), \(\nabla u=0\), and
\[
\Delta q=8\operatorname{tr}(V^2)-24|\eta|^2
=2|\nabla^2\Omega|^2.
\]

---

## 3. Passage to the leading identity

Let \(a\) vanish to finite order \(m\ge1\), with leading polynomial \(f_m\). The principal complex equation says that the complex-linear derivative of \(f_m\) is scalar:
\[
\partial_{z_j}(f_m)_i=h\,\delta_{ij}.
\]
Commuting the \(z\)-derivatives shows \(\partial_{z_1}h=\partial_{z_2}h=0\). Hence \(h\) is a homogeneous polynomial of degree \(m-1\) in \(w=\bar z\), and integration gives
\[
f_m(z,w)=z\,h(w)+g(w),
\]
where \(g\) is \(\mathbb C^2\)-valued and homogeneous of degree \(m\).

Write
\[
B=D_wf_m=z\otimes D_wh+D_wg,\qquad
A=\frac{B-B^T}{2},\qquad
S=\frac{B+B^T}{2}.
\]

### 3.1 Left side of \((G)\)

The Step-62 normalization gives
\[
q=4|f_m|^2+O(|x|^{2m+1}).
\]
Using
\[
\Delta_{\mathbb R}=4\sum_j\partial_{z_j}\partial_{w_j},
\qquad
\Delta_{\mathbb R}f_m=4D_wh,
\]
one obtains
\[
\big(\Delta q\big)_{2m-2}
=
8\|Df_m\|_{\mathbb R}^2
+32\operatorname{Re}\sum_j\overline{f_{m,j}}\,\partial_{w_j}h.
\tag{3.1}
\]
Furthermore,
\[
\|Df_m\|_{\mathbb R}^2
=4|h|^2+2\|A\|^2+2\|S\|^2.
\tag{3.2}
\]

### 3.2 Algebraic curvature terms

The leading Step-62 dictionary is
\[
|\eta|^2=4|h|^2,\qquad
\operatorname{tr}(V^2)=4\|A\|^2.
\tag{3.3}
\]
Thus
\[
\big(8\operatorname{tr}(V^2)-24|\eta|^2\big)_{2m-2}
=32\|A\|^2-96|h|^2.
\tag{3.4}
\]

Since \(q=O(|x|^{2m})\), the terms \(sq\) and \(q^2\) begin at degrees \(2m\) and \(4m\), respectively, and do not enter degree \(2m-2\).

### 3.3 Derivative source

In the unit frame of \(u^\perp\),
\[
\eta=(-2\operatorname{Re}h,-2\operatorname{Im}h)
\]
at leading order. Also
\[
\nabla u
=a\otimes\frac{\phi}{\sqrt2}
-Ja\otimes\frac{\psi}{\sqrt2}.
\]
Therefore
\[
\begin{aligned}
\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle
&=a\cdot d\eta_1-Ja\cdot d\eta_2+O(|x|^{2m-1})\\
&=-4\operatorname{Re}\sum_j
\overline{f_{m,j}}\partial_{w_j}h
+O(|x|^{2m-1}).
\end{aligned}
\tag{3.5}
\]
The factor \(-4\) agrees with the complex convention \(w_j=x_j-iy_j\) and the Step-62 relation between \(\eta\) and the scalar complex-linear mode.

Substituting (3.1)–(3.5) into \((G)\) gives
\[
\begin{aligned}
32|h|^2+16\|A\|^2+16\|S\|^2+32C
=32\|A\|^2-96|h|^2-64C,
\end{aligned}
\]
where
\[
C=\operatorname{Re}\sum_j\overline{f_{m,j}}\partial_{w_j}h.
\]
Division by \(16\) yields \((H_m)\).

For \(m=1\), \(D_wh=0\), so this becomes
\[
\|A\|^2=\|S\|^2+8|h|^2,
\]
exactly the Step-62 cone.

---

## 4. Reduction of \((H_m)\) to the bidegree identity

For a complex \(2\times2\) matrix \(B\),
\[
\|A\|^2-\|S\|^2
=-\operatorname{tr}(\overline B\,B),
\]
where the bar is entrywise and the multiplication is ordinary matrix multiplication.

Let \(G=D_wg\). Euler homogeneity gives
\[
\sum_iw_i\partial_{w_i}h=(m-1)h,\qquad
\sum_iw_i\partial_{w_i}g_j=mg_j.
\]
Expanding \(\operatorname{tr}(\overline B B)\) gives
\[
\operatorname{tr}(\overline B B)
=
\operatorname{tr}(\overline G G)
+(m-1)^2|h|^2
+2m\operatorname{Re}\sum_i\overline{g_i}\,\partial_{w_i}h.
\]
Also,
\[
\operatorname{Re}\sum_i\overline{f_i}\partial_{w_i}h
=(m-1)|h|^2+
\operatorname{Re}\sum_i\overline{g_i}\partial_{w_i}h.
\]
Thus \((H_m)\) is equivalent to
\[
\boxed{
\operatorname{tr}(\overline{Dg}\,Dg)
+(m+1)(m+3)|h|^2
+2(m+3)\operatorname{Re}
\sum_i\overline{g_i}\,\partial_{w_i}h=0.
}
\tag{I_m}
\]

The first two terms have bidegree
\[
(m-1,m-1)
\]
in \((w,z)\). The final complex term and its conjugate have bidegrees
\[
(m-2,m),\qquad (m,m-2).
\]
For \(m\ge2\), these three bidegrees are pairwise distinct. A polynomial identity in \(z,\bar z\) is equivalently a polynomial identity after treating \(z,w\) as independent variables, since \(z=x+iy\), \(w=x-iy\) is an invertible complex-linear change of variables. Hence
\[
\sum_i\overline{g_i}\,\partial_{w_i}h=0
\tag{J_m}
\]
and
\[
\operatorname{tr}(\overline{Dg}\,Dg)
+(m+1)(m+3)|h|^2=0.
\tag{K_m}
\]

The bidegree argument is therefore valid for every \(m\ge2\), including \(m=2\). It is not available at \(m=1\), which is consistent with the larger Step-62 cone.

---

## 5. Why \(h=0\)

There are two exhaustive cases.

### 5.1 The components \(g_1,g_2\) are linearly independent as polynomials

Equation \((J_m)\) reads
\[
\overline{g_1}(z)h_1(w)+\overline{g_2}(z)h_2(w)=0,
\qquad h_i=\partial_{w_i}h.
\]
Linear independence over \(\mathbb C\) remains valid after extending scalars to \(\mathbb C(w)\). Hence
\[
h_1=h_2=0.
\]
Since \(h\) is homogeneous of degree \(m-1\ge1\), this gives \(h=0\).

### 5.2 The components are linearly dependent

Then
\[
g(w)=v\,G(w)
\]
for a fixed \(v\in\mathbb C^2\) and a scalar homogeneous polynomial \(G\). Its derivative is
\[
Dg=v\otimes DG.
\]
A direct calculation gives
\[
\operatorname{tr}(\overline{Dg}\,Dg)
=
\left|\sum_i\overline{v_i}\,\partial_{w_i}G\right|^2.
\]
Therefore \((K_m)\) is a sum of two terms each \(\ge0\):
\[
\left|DG\cdot\overline v\right|^2
+(m+1)(m+3)|h|^2=0.
\]
Thus \(h=0\). The subcase \(g=0\) gives the same conclusion immediately.

This coordinate-free argument avoids any uncertainty about whether an independent target rotation preserves the transpose decomposition.

---

## 6. Classification after \(h=0\)

With \(h=0\),
\[
\operatorname{tr}(\overline{Dg(w)}\,Dg(w))=0.
\tag{6.1}
\]

Define the Hermitian form on \(M_2(\mathbb C)\)
\[
\mathcal H(M,N)=\operatorname{tr}(\overline M\,N).
\]
For
\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
\[
\mathcal H(M,M)=|a|^2+|d|^2+2\operatorname{Re}(\bar b c).
\]
Putting
\[
u=\frac{b+c}{\sqrt2},\qquad v=\frac{b-c}{\sqrt2},
\]
gives
\[
\mathcal H(M,M)=|a|^2+|d|^2+|u|^2-|v|^2.
\]
Thus \(\mathcal H\) has Hermitian signature \((3,1)\).

Expand
\[
Dg(w)=\sum_{|\alpha|=m-1}M_\alpha w^\alpha.
\]
Equation (6.1) becomes
\[
\sum_{\alpha,\beta}
\mathcal H(M_\alpha,M_\beta)\,
\bar w^\alpha w^\beta=0.
\]
The mixed monomials \(\bar w^\alpha w^\beta\) are independent, so
\[
\mathcal H(M_\alpha,M_\beta)=0
\quad\text{for all }\alpha,\beta.
\]
The coefficient matrices therefore span a totally isotropic complex subspace.

For a Hermitian form of signature \((3,1)\), such a subspace has complex dimension at most one. One direct proof is that projection to the one-dimensional minus-sign factor is injective on a totally isotropic subspace: a vector whose minus-sign component vanishes must have all three plus-sign components zero. Hence
\[
Dg(w)=M\,p(w)
\tag{6.2}
\]
for one constant matrix \(M\) and a scalar homogeneous polynomial \(p\) of degree \(m-1\).

### 6.1 Mixed partials

Writing \(\partial_jg_i=M_{ij}p\), equality of mixed partials gives
\[
M_{i1}\partial_2p=M_{i2}\partial_1p,\qquad i=1,2.
\tag{6.3}
\]
If \(M\) has rank two, (6.3) forces
\[
\partial_1p=\partial_2p=0.
\]
But \(p\) has degree \(m-1\ge1\), so \(p=0\), contrary to a nonzero leading term. Thus \(M\) has rank one:
\[
M=v\otimes\ell.
\]

Equation (6.3) becomes
\[
\ell_1\partial_2p-\ell_2\partial_1p=0.
\]
Hence \(p\) is constant along the vector field
\[
-\ell_2\partial_{w_1}+\ell_1\partial_{w_2},
\]
and therefore depends only on
\[
L(w)=\ell_1w_1+\ell_2w_2.
\]
Homogeneity gives
\[
p(w)=c\,L(w)^{m-1}.
\]
Integrating (6.2),
\[
g(w)=\kappa\,v\,L(w)^m.
\]

Finally,
\[
0=\mathcal H(M,M)
=\mathcal H(v\otimes\ell,v\otimes\ell)
=|\ell\cdot\overline v|^2,
\]
so
\[
\ell\cdot\overline v=0.
\]
Thus \(v\) and \(\ell\) are Hermitian-orthogonal. A simultaneous unitary frame change sends them, up to lengths and phases absorbed into \(\kappa\), to \(e_1\) and \(e_2\). This yields
\[
f_m(z)=g(\bar z)=\kappa(\bar z_2)^m e_1.
\]

The cases \(g=0\), \(Dg=0\), rank-two \(M\), vanishing \(p\), and one-component \(g\) are all included in the preceding alternatives. For a genuine first nonzero Taylor term, \(\kappa\ne0\).

---

## 7. Relation with the saved second-order computation

For \(m=2\), \((H_2)\) is a real homogeneous quadratic polynomial in four source coordinates. It therefore has ten scalar coefficients. The supplied script constructs precisely these ten coefficient quadrics.

The saved comparison reports:

- predicted rank \(10\);
- saved rank \(10\);
- all principal-angle cosines equal to \(1\) to floating precision;
- largest relative projection discrepancy \(6.24\times10^{-9}\), consistent with the saved eight-decimal matrices;
- surface-restricted rank \(3\);
- exact dyadic evaluation of
  \[
  \operatorname{tr}_{\text{source}}(H_2)
  =
  -8\left(
  \|Q\|^2-|P|^2+\frac{15}{4}|\delta|^2
  \right).
  \]

Thus the sign and coefficient \(15/4\) agree with the Step-64 scalar relation
\[
\|Q\|^2-|P|^2=-\frac{15}{4}|\delta|^2.
\]
The numerical span comparison supports identification of the stored ten quadrics with the ten coefficients of \((H_2)\). It does not by itself establish that no other nonlinear jet equations occur at that level.

---

## 8. Precisely established versus still requiring a written geometric lemma

The following parts are complete from the displayed equations and algebra:

1. the exact scalar equation \((G)\);
2. all numerical constants and signs in its block expansion;
3. the derivation of \((H_m)\) from the stated leading expansions;
4. the Euler and bidegree reduction from \((H_m)\) to \((J_m)\) and \((K_m)\);
5. the proof that \(h=0\);
6. the signature \((3,1)\), one-dimensional maximal totally isotropic subspaces, mixed-partial integration, and normal form \((L_m)\).

For a fully self-contained geometric theorem at every \(m\), the supplied notes still need one explicit all-order local lemma proving, in one smooth adapted gauge,
\[
\begin{aligned}
a&=f_m+O(|x|^{m+1}),\\
\eta&=(-2\Re h,-2\Im h)+O(|x|^m),\\
\operatorname{tr}(V^2)&=4\|A\|^2+O(|x|^{2m-1}),\\
\sum_i\langle(\nabla_iW^+)\nabla_i u,u\rangle
&=-4\Re\sum_j\overline{f_{m,j}}\,\partial_{w_j}h
+O(|x|^{2m-1}).
\end{aligned}
\]
The Step-62 coframe calculation proves the constants at first order, and Step 64 supplies the corresponding second-order linearization. The general remainder estimates follow naturally from the exact soldered equation, \(a=O(|x|^m)\), and the Ricci identities, but that all-\(m\) lemma is not written in the supplied files.

Even after that lemma is recorded, the result is a necessary classification of the first nonzero torsion polynomial. It gives no formal-jet realization, analytic germ realization, existence of an Einstein almost-Kähler metric carrying such a zero, classification of higher Taylor terms, or determination of the actual local zero set. In particular, the plane \(\{\bar z_2=0\}\) is the zero set of the leading polynomial only, and no winding conclusion follows solely from this leading normal form.