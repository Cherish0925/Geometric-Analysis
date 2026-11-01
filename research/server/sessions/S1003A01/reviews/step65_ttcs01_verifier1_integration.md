# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 65,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step65_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step65_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematical derivation in Spirit Step 64's homogeneous zero identity for Einstein almost-Kähler four-manifolds. Check the exact scalar Delta-q formula (G), all constants/sign conventions relative to the established Step-62 normalization, the passage to the leading polynomial identity H_m for a finite-order torsion zero f_m=z h(bar z)+g(bar z), and the claimed all-orders classification f_m=kappa (bar z_2)^m e_1 for m>=2. Pay particular attention to the bidegree separation, the argument forcing h=0, the Hermitian form tr(conjugate(M)M), maximal totally isotropic dimension, integration/mixed-partial argument, and whether any exceptional polynomial cases were missed. State exactly what is proved and what still depends on unproved formal/gauge assumptions.

## Integrated Scientific Memo

# Verification memo: Step-64 homogeneous zero identity

## Conclusion

**The exact scalar identity (G) is correct in the Step-62 normalization.** Its leading polynomial identity \((H_m)\), including the coefficient \(-6\), follows from the stated leading coframe dictionary. **The polynomial classification from \((H_m)\) is complete:** for every \(m\ge2\), every nonzero homogeneous solution of the prescribed half-twistor form is
\[
f_m(z)=\kappa(\bar z_2)^m e_1,\qquad \kappa\ne0,
\]
up to the compatible unitary frame and gauge action.

The remaining qualification is geometric, not algebraic: the supplied files give the exact dictionary at a zero and its second-order linearization, but do not fully write out the smooth adapted-gauge remainder lemma for arbitrary \(m\). The degree argument below explains the required extension. No formal or analytic realization, classification of higher Taylor terms, actual zero-surface theorem, or winding restriction follows merely from this leading classification.

## 1. Exact verification of (G)

Use precisely
\[
\Delta=\operatorname{tr}\nabla^2=-\nabla^*\nabla,\qquad
u=\Omega/\sqrt2,\qquad q=|\nabla\Omega|^2,
\]
and
\[
W=W^+=
\begin{pmatrix}r&\eta^T\\ \eta&-\frac r2I+V\end{pmatrix},
\qquad \operatorname{tr}V=0.
\]
Here all Weyl norms are endomorphism Hilbert–Schmidt norms, as in Step 62. The supplied equations are
\[
\Delta u=-2Wu+\frac s3u,\qquad
\Delta W=\frac s2W-6W^2+2\operatorname{tr}(W^2)I.
\]
Since \(|u|=1\),
\[
|\nabla u|^2=2r-\frac s3,\qquad
r=\frac s6+\frac q4.
\]

Set
\[
T=\sum_i\langle(\nabla_iW)\nabla_i u,u\rangle.
\]
The full product rule is
\[
\Delta r
=\langle(\Delta W)u,u\rangle
+2\langle W\Delta u,u\rangle
+2\sum_i\langle W\nabla_i u,\nabla_i u\rangle+4T.
\]
The block algebra gives
\[
\operatorname{tr}(W^2)=\frac32r^2+2|\eta|^2+\operatorname{tr}(V^2),
\qquad
\langle W^2u,u\rangle=r^2+|\eta|^2.
\]
Consequently, the first two terms are respectively
\[
\frac s2r-3r^2-2|\eta|^2+2\operatorname{tr}(V^2),
\qquad
-4r^2-4|\eta|^2+\frac{2s}{3}r.
\]

The AAD expression
\[
\nabla u=a\otimes\widehat\phi-Ja\otimes\widehat\psi,
\qquad \widehat\phi=\phi/\sqrt2,\quad \widehat\psi=\psi/\sqrt2,
\]
implies \(q=4|a|^2\) and
\[
\sum_i(\nabla_i u)\otimes(\nabla_i u)=\frac q4I_{u^\perp}.
\]
Thus the third term is \(-qr/2\). Altogether,
\[
\Delta r=\frac{7s}{6}r-7r^2-\frac q2r
-6|\eta|^2+2\operatorname{tr}(V^2)+4T.
\]
Substitution of \(r=s/6+q/4\) gives
\[
\frac{7s}{6}r-7r^2-\frac q2r
=-\frac{3s}{8}q-\frac9{16}q^2.
\]
Since \(s\) is constant and \(\Delta q=4\Delta r\),
\[
\boxed{\Delta q
=8\operatorname{tr}(V^2)-24|\eta|^2
-\frac{3s}{2}q-\frac94q^2+16T.}\tag{G}
\]

At a torsion zero, \(T=q=0\) and
\[
\Delta q=2|\nabla^2\Omega|^2.
\]
Hence (G) recovers exactly
\[
|\nabla^2\Omega|^2=4\operatorname{tr}(V^2)-12|\eta|^2,
\]
the established Step-62 identity. No sign or factor discrepancy occurs.

## 2. Leading-order passage and its geometric prerequisite

Suppose \(a\) has first nonzero Taylor term \(f_m\), homogeneous of degree \(m\). The required principal equation is
\[
\partial_{z_j}(f_m)_i=h\,\delta_{ij}.
\]
Commuting \(z\)-derivatives in complex dimension two forces \(\partial_z h=0\). Therefore, writing \(w=\bar z\),
\[
f_m(z,w)=z\,h(w)+g(w),
\]
where \(h\) has degree \(m-1\) and \(g\) has degree \(m\). Set
\[
B=z\otimes D_wh+D_wg,\qquad
A=\frac{B-B^T}{2},\qquad S=\frac{B+B^T}{2}.
\]

### The all-order dictionary needed

In one smooth adapted gauge, the needed expansions are
\[
\begin{aligned}
a&=f_m+O(|x|^{m+1}),\\
\eta&=(-2\Re h,-2\Im h)+O(|x|^m),\\
V&=\mathcal V(A)+O(|x|^m),
\qquad |\mathcal V(A)|^2=4\|A\|^2.
\end{aligned}\tag{2.1}
\]
The errors must be Taylor remainders with their corresponding differentiated orders, not merely pointwise bounds.

The supplied Step-62 coframe calculation proves the constants and signs at first order; Step 64 states their second-order extension. The general degree argument is sound **provided the exact adapted Ricci identities have the asserted principal part**: frame-connection terms multiplying \(a\) are \(O(|x|^m)\), quadratic torsion terms are \(O(|x|^{2m})\), whereas \(da\) starts in degree \(m-1\). Einstein removes the anti-self-dual curvature part, and the scalar action on \(\Omega^\perp\) is proportional to \(q\), hence cannot contribute in degree \(m-1\). The same linear dictionary therefore applies to \(Df_m(x)\).

This supplies the mechanism for the extension, but the bounded source does not display the full general adapted identities and their remainder estimates. A self-contained geometric theorem for all \(m\) should include that lemma explicitly. It is not a formal-realization assumption.

### Laplacian and derivative-source calculation

In normal coordinates,
\[
q=4|f_m|^2+O(|x|^{2m+1}),\qquad
(\Delta_gq)_{2m-2}=\Delta_{\rm flat}(4|f_m|^2).
\]
Also
\[
\Delta_{\rm flat}f_m=4D_wh,\qquad
\|Df_m\|_{\mathbb R}^2
=4|h|^2+2\|A\|^2+2\|S\|^2.
\]
Writing
\[
C=\Re\sum_j\overline{f_{m,j}}\,\partial_{w_j}h,
\]
the left side of (G), in degree \(2m-2\), is
\[
8\|Df_m\|_{\mathbb R}^2+32C.
\]

The sign-sensitive source is
\[
T=a\cdot d\eta_1-Ja\cdot d\eta_2
+\text{higher-degree terms}.
\]
With the Step-62 convention \(Ja\leftrightarrow if_m\) and \(\eta_1+i\eta_2=-2h\), antiholomorphicity gives
\[
D_a h=\sum_j\bar f_{m,j}h_j,\qquad
D_{Ja}h=-i\sum_j\bar f_{m,j}h_j.
\]
Therefore
\[
T_{2m-2}=-4C.
\]
Connection corrections in differentiating the moving block components do not enter this degree: the \(u\)-mixing connection is \(O(a)\), giving \(O(a^2)\) after contraction, and the \(u^\perp\)-connection multiplies \(\eta\).

The algebraic curvature terms contribute
\[
32\|A\|^2-96|h|^2.
\]
The \(sq\) and \(q^2\) terms start in degrees \(2m\) and \(4m\). Equating the leading terms yields
\[
32|h|^2+16\|A\|^2+16\|S\|^2+32C
=32\|A\|^2-96|h|^2-64C,
\]
or
\[
\boxed{\|A\|^2-\|S\|^2-8|h|^2-6C=0.}\tag{H_m}
\]

For \(m=1\), \(D_wh=0\), so this is precisely the Step-62 cone
\[
\|A\|^2=8|h|^2+\|S\|^2.
\]

The coefficient \(-6\) is fixed once these conventions are fixed. It should not be described as freely gauge-dependent: compatible gauge changes transform all entries together and preserve the equation.

## 3. Euler reduction and bidegree separation

For any complex matrix \(B\),
\[
\|A\|^2-\|S\|^2=-\operatorname{tr}(\bar B B),
\]
with **entrywise conjugation**, not adjoint.

Put \(G=D_wg\) and \(X=\sum_i\bar g_i h_i\). Euler homogeneity gives
\[
\begin{aligned}
\operatorname{tr}(\bar B B)
&=\operatorname{tr}(\bar G G)+(m-1)^2|h|^2+2m\Re X,\\
C&=(m-1)|h|^2+\Re X.
\end{aligned}
\]
Thus \((H_m)\) is equivalent to
\[
\boxed{
\operatorname{tr}(\overline{Dg}Dg)
+(m+1)(m+3)|h|^2+2(m+3)\Re X=0.
}\tag{I_m}
\]

In \((w,\bar w)\), the first two terms have bidegree \((m-1,m-1)\); \(X\) and \(\bar X\) have bidegrees \((m-2,m)\) and \((m,m-2)\). These are distinct for every \(m\ge2\), including \(m=2\).

There is no hidden restriction from \(w=\bar z\): the substitution
\[
z=x+iy,\qquad w=x-iy
\]
is invertible over \(\mathbb C\), so a polynomial vanishing for all real \(x,y\) vanishes in the independent complexified variables. Hence
\[
\boxed{\sum_i\bar g_i h_i=0,}\tag{J_m}
\]
and
\[
\boxed{\operatorname{tr}(\overline{Dg}Dg)
+(m+1)(m+3)|h|^2=0.}\tag{K_m}
\]

## 4. Why \(h=0\): an exhaustive argument without a gauge choice

If \(g_1,g_2\) are complex-linearly independent polynomials, \((J_m)\), as an identity in independent \(w,\bar w\), forces
\[
h_1=h_2=0.
\]
Since \(h\) has positive degree, \(h=0\).

Otherwise \(g=vG\) for a constant vector \(v\) and scalar polynomial \(G\). Directly,
\[
\operatorname{tr}(\overline{Dg}Dg)
=\left|\sum_i\bar v_i\,\partial_{w_i}G\right|^2\ge0.
\]
Equation \((K_m)\) then forces \(h=0\). This also covers \(g=0\).

This coordinate-free proof repairs the only potentially delicate point in the source’s line-valued argument: **an independent target rotation need not preserve the transpose split**. No rotation is needed to prove \(h=0\).

## 5. Hermitian isotropy and integration: complete classification

Define
\[
\mathcal H(M,N)=\operatorname{tr}(\bar M N).
\]
Despite the absence of an adjoint, this is Hermitian:
\(\mathcal H(M,N)=\overline{\mathcal H(N,M)}\). For
\(M=\begin{pmatrix}a&b\\c&d\end{pmatrix}\),
\[
\mathcal H(M,M)
=|a|^2+|d|^2+2\Re(\bar b c)
=|a|^2+|d|^2+
\left|\frac{b+c}{\sqrt2}\right|^2-
\left|\frac{b-c}{\sqrt2}\right|^2.
\]
Its signature is therefore \((3,1)\).

Expand
\[
Dg(w)=\sum_{|\alpha|=m-1}M_\alpha w^\alpha.
\]
With \(h=0\), \((K_m)\) says
\[
\sum_{\alpha,\beta}\mathcal H(M_\alpha,M_\beta)
\bar w^\alpha w^\beta=0.
\]
Independence of mixed monomials forces **every pairing**, not only the diagonal ones, to vanish. The coefficient span is totally isotropic. Its complex dimension is at most one: projection onto the one-dimensional negative factor is injective on any totally isotropic subspace. Hence, for a nonzero \(g\),
\[
Dg=M p(w)
\]
with constant nonzero \(M\) and nonzero homogeneous \(p\) of degree \(m-1\).

Equality of mixed partials gives
\[
M_{i1}p_2=M_{i2}p_1,\qquad i=1,2.
\]
If \(M\) were invertible, then \(Dp=0\), impossible for a nonzero polynomial of positive degree. Thus \(M=v\otimes\ell\) has rank one. The same equations become
\[
\ell_1p_2-\ell_2p_1=0.
\]
Choose linear coordinates \(L=\ell\cdot w\) and a complementary coordinate. This equation says \(p\) is independent of the complementary coordinate. Homogeneity then gives
\[
p=cL^{m-1}.
\]
Integration and degree-\(m\) homogeneity yield
\[
g(w)=\kappa v(\ell\cdot w)^m;
\]
there is no integration constant. Finally,
\[
0=\mathcal H(v\otimes\ell,v\otimes\ell)
=|\ell\cdot\bar v|^2.
\]
Thus \(\ell\cdot\bar v=0\).

Under the compatible simultaneous unitary transformation
\[
z'=Uz,\qquad f'(z')=Uf(U^*z'),
\]
one has
\[
B'=UBU^T,\qquad v'=Uv,\qquad \ell'=\ell\bar U^T.
\]
This preserves \(\operatorname{tr}(\bar B B)\) and the orthogonality condition. It sends the two orthogonal directions to \(e_1,e_2\), with lengths and phases absorbed into \(\kappa\). Consequently,
\[
\boxed{f_m(z)=\kappa(\bar z_2)^m e_1,\quad m\ge2.}\tag{L_m}
\]

Conversely, this polynomial satisfies the principal equation and \((H_m)\): \(h=0\), and its derivative has only an upper-right entry, so \(\operatorname{tr}(\overline{Dg}Dg)=0\).

All exceptional algebraic cases are covered: zero \(g\), dependent components, zero derivative, zero \(p\), either vanishing component of \(\ell\), and rank-two \(M\). The restriction \(m\ge2\) is essential; at \(m=1\), \(p\) is constant and the rank-two exclusion fails.

## 6. Second-order trace and the comparison artifact

For \(m=2\), write \(h=\delta\cdot w\) and \(g=Q(w,w)\), with the source’s symmetric-tensor norm. Summing \((H_2)\) over the four real coordinate unit vectors gives
\[
\sum_{\nu=1}^4(H_2)(e_\nu)
=-8\left(\|Q\|^2-|P|^2+\frac{15}{4}|\delta|^2\right).
\]
Indeed, the \(g\)-part contributes \(-8(\|Q\|^2-|P|^2)\); the \(|h|^2\) sum is \(2|\delta|^2\), with coefficient \(-15\); and the unequal-bidegree cross terms cancel in this source trace. Thus the \(15/4\) coefficient and its sign are independently verified.

The supplied script correctly implements \((H_2)\). Its saved output reports rank ten, span agreement to approximately \(6.24\times10^{-9}\), and surface-restricted rank three. The original saved intrinsic matrices are not included here, so their span comparison is supported by the supplied output rather than a fresh reconstruction.

One artifact claim needs correction: **the script is not entirely exact dyadic arithmetic**. `abs(h)**2` can perform a rounded square root followed by squaring. The JSON itself contains nominally zero entries of size \(3.55\times10^{-15}\). The reported zero trace error is therefore a floating-point result, not an exact certificate. The analytic trace derivation above supplies the exact identity; an exact implementation would evaluate squared moduli by real and imaginary squares or rational arithmetic.

## 7. Exact scope and remaining objects

What is established:

- (G), with all constants and signs.
- \((H_m)\) from the stated all-order leading dictionary.
- A complete algebraic classification of its homogeneous half-twistor solutions for every \(m\ge2\).
- The exact second-order trace relation, explaining the \(15/4\) coefficient.
- The leading normal form without the extra zero-surface hypotheses used in Step-64 Corollary 64.B.

What remains unproved in this bounded material:

1. **The explicit all-\(m\) adapted-gauge lemma** giving (2.1), the principal equation, and differentiated remainder control from the full AAD Ricci identities.
2. **Realization:** whether a nonzero allowed polynomial extends to a full compatible formal jet or an actual Einstein almost-Kähler germ, particularly for \(s<0\).
3. **Higher-order geometry:** the actual torsion-zero set and the equation for \(W_3^+|_C\) through exceptional points.

The two branches’ algebraic conclusions agree. Their stronger ancillary claims should not be imported: finite-order automaticity via analyticity is not established by the supplied files, and changing the derivative-source sign is unnecessary and does not verify the fixed normalization.

Finally, Step 64’s claim that a vanishing linear part excludes winding \(\pm1\) is false. The real-analytic sections
\[
b(\zeta)=\zeta|\zeta|^2,\qquad
b(\zeta)=\bar\zeta|\zeta|^2
\]
have zero linear part and windings \(+1,-1\). The leading torsion polynomial vanishes on a complex plane, but this alone determines neither the actual zero locus nor a local index. A winding theorem requires an additional surface PDE with coefficient control through \(b=0\); it is not a consequence of \((L_m)\).