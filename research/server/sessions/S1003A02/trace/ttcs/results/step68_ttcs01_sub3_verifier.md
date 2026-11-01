# TTCS Independent Branch Record

```json
{
  "step_id": 68,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/trace/ttcs/results/step67_ttcs01_verifier1_integration.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step67_cK_local_coercivity_at_cscK.md",
    "Sessions/S1003A02/trace/ttcs/results/step67_ttcs01_sub1_generator.md"
  ]
}
```

## Task

Read the Step-67 verifier and current §21.11, and state exact replacement mathematics for Theorem 67.K and the product model. Preserve only what is established: Lemma 67.1; moving-line null structure; obstruction P_omega and Xi; corrected Blair-Ianus constants; gauge-reduced ellipticity; finite kernel; conditional c_K>0; cubic metric-displacement remainder and T-N spectral interpretation. Check the proposed product mode independently enough to say whether it bypasses Xi (it is not an ell_2-null direction) and what it establishes about c_K versus 2. Identify any remaining false unconditional wording in §21.11 and give concise corrected statements suitable for insertion.

## Output

# Scientific memo: corrected Step 67 package

## 1. Replacement statement for Lemma 67.1

Let
\[
q=\|h_a^-\|_2>0,\qquad \widehat h=h_a^-/q,\qquad
\delta=1-\frac{\mathfrak F}{2\pi q},\qquad
L=\frac{P/2-\mathfrak F^2}{4\pi^2},
\]
where \(\mathfrak F=\sqrt2\int|B^*\widehat h|\). At a non-KE cscK metric,
\[
B_0=\pi q\,\omega\otimes\widehat h,\qquad
v_0:=B_0^*\widehat h=\pi q|\widehat h|^2\omega.
\]

For every **\(g\)-orthogonal**, orientation-compatible \(J\) with \(c_1(J)=a\),
\[
\boxed{2\pi q\,\delta\le (t_J^-,\widehat h).}
\]
Indeed,
\[
(t_J^-,\widehat h)
=2\pi q-\int\langle\Omega_J,B^*\widehat h\rangle
\ge 2\pi q-\sqrt2\int|B^*\widehat h|.
\]

The zero set of a nonzero harmonic form has measure zero. Consequently the integral norm \(v\mapsto\int|v|\) is Fréchet differentiable at \(v_0\) in the \(C^0\) topology even when \(Z(\widehat h)\ne\varnothing\). Together with smooth Hodge dependence, this proves differentiability of \(\mathfrak F,\delta,L\) at \(g_0\).

Orthogonalizing \(J_0\) along any two-sided metric curve \(g_t\) gives intrinsic torsion \(O(t)\), hence
\[
(t_{\widehat J_t}^-,\widehat h_t)=O(t^2).
\]
The preceding inequality and differentiability give \(D\delta(g_0)=0\). Since \(L\ge0\) and \(L(g_0)=0\), also \(DL(g_0)=0\). Therefore
\[
D(p-q^2)(g_0)=0.
\]
The topological identities give
\[
\boxed{p-q^2=C_+(g)-|a^+|_g^2,}
\]
so every cscK metric is stationary for \(C_+-|c_1^+|^2\) on the full metric space. The KE case \(q=0\), where \(\delta\) is not defined, follows separately because both \(P\) and \(|a^-|^2\) vanish to first order.

This agrees with the direct formulas, writing \(E=\Ric^\circ\),
\[
D\!\int s^2=-2s\int\langle E,k\rangle,\qquad
D\!\int|W^+|^2=-\frac{s}{12}\int\langle E,k\rangle,
\]
and
\[
D|a^+|^2=-\frac{s}{16\pi^2}\int\langle E,k\rangle=DC_+(k).
\]
The conformal verification uses only constant scalar curvature, not Yamabe attainment.

---

## 2. Correct replacement for Theorem 67.K(A)

Let \(g_t\) be a first-order constant-scalar deformation and \(h_t\) the moving harmonic ASD representative. If \(\ell_2(k)=0\), the correct moving-line equation is
\[
\boxed{
B'_0=\dot\Phi\otimes h_0+\Phi_0\otimes\dot h,
}
\]
including the bundle-motion terms. It is not correct to require raw \(B'_0\in\Lambda^+\otimes\mathbb Rh_0\).

Under the zero-free or transverse-zero hypothesis, division is applied to the residual after subtracting the moving aligned comparison. At a transverse zero, taking the three components of \(h\) as normal coordinates \(x_i\), the relations
\[
S_i x_j-S_jx_i=0
\]
imply \(S_i=f x_i\) with one smooth coefficient \(f\). Thus one obtains
\[
\Ric^\circ_t=\Phi_t\circ h_t+O(t^2)
\]
smoothly across \(Z(h)\).

Lemma 66.D and contracted Bianchi then give
\[
h_t(\delta_t\Phi_t)=O(t^2).
\]
Since \(h_0\) is invertible away from its zero set, the first coefficient of \(\delta\Phi_t\) vanishes there and hence everywhere by smoothness. The amplitude equation makes \(|\Phi_t|\) spatially constant through first order. After normalization,
\[
d\Omega_t=O(t^2),\qquad (\Ric''_t)'=0.
\]

Thus the unconditional infinitesimal conclusion is:

\[
\boxed{\text{Every }\ell_2\text{-null direction induces a first-order almost-Kähler aligned pair with }(\Ric'')'=0.}
\]

It does **not** follow in general that this pair is first-order Kähler. The missing cohomological object is
\[
\mathcal P_\omega:
H^{0,1}(T^{1,0}M)\longrightarrow H^{0,2}(M),
\qquad
[\mu]\longmapsto[\mu\lrcorner\omega].
\]
A prescribed \((0,2)\) class variation is realizable by a first-order Kähler pair precisely when it belongs to \(\operatorname{im}\mathcal P_\omega\). The proposed formula \(\mu=\omega^{-1}\bar\theta\) does not generally satisfy \(\bar\partial\mu=0\).

Define
\[
\boxed{
\Xi:K\longrightarrow H^{0,2}(M)/\operatorname{im}\mathcal P_\omega,
\qquad
k\longmapsto[\dot\Omega_k]^{0,2},
}
\]
where \(K=\ker\ell_2\cap\mathcal S\). Then the corrected rigidity statement is:

\[
\boxed{
\Xi(k)=0\quad\Longrightarrow\quad k\text{ is first-order Kähler and belongs to the radical of }d_2.
}
\]

This includes \(p_g=0\), surjectivity of \(\mathcal P_\omega\), and individual modes with no \((0,2)\) class variation.

The Blair–Ianus constants used here are
\[
s^*-s=|\nabla\omega|^2,
\qquad
\int\frac{s+s^*}{2}=4\pi c_1\cdot[\omega].
\]
Hence, for \(E(J)=\int|\nabla\omega|^2\),
\[
\boxed{
\int s=4\pi c_1\cdot[\omega]-\frac12E(J),
}
\]
and on the fixed-\(\omega\) compatible space,
\[
D\!\int s(k)=-\int\langle\Ric'',k\rangle,\qquad
DE(k)=2\int\langle\Ric'',k\rangle,
\]
\[
\boxed{\operatorname{Hess}E=2\int|(\nabla\omega)'|^2.}
\]
The factors \(1/4\) and \(4\) in the original Step 67 text must be replaced by \(1/2\) and \(2\).

For \(M=C_g\times C_h\), \(g,h\ge2\),
\[
H^{0,1}(TM)
=H^{0,1}(TC_g)\oplus H^{0,1}(TC_h),
\]
because \(H^0(TC_g)=H^0(TC_h)=0\). Contraction with the product Kähler form vanishes by type and factor dimension, so
\[
\boxed{\mathcal P_\omega=0,\qquad H^{0,2}(M)\ne0.}
\]
Thus zero-freeness of \(\widehat h\) alone does not settle \(\Xi\) on products.

---

## 3. Correct replacement for Theorem 67.K(B)

Let
\[
\mathcal S=\{k:\beta_{g_0}k=0,\ s'_0(k)\text{ is spatially constant}\}.
\]
The metric dependence of the harmonic representative contributes order-zero pseudodifferential and finite-rank terms. These do not alter the second-order principal symbol.

The Ricci row used in the numerical matrix is the gauge-reduced symbol. Before imposing Bianchi gauge, the symbol is
\[
\sigma_\xi(\Ric')(k)
=\frac12\Bigl(
|\xi|^2k+\xi\otimes\xi\,\tr k
-\xi\otimes k(\xi)-k(\xi)\otimes\xi
\Bigr),
\]
up to the common Fourier sign. On the Bianchi-symbol kernel it reduces to \(\frac12|\xi|^2k\).

Vanishing of the augmented symbol gives
\[
k^\circ=\sigma\circ\widehat h,\qquad \sigma\perp\omega.
\]
The gauge and scalar rows imply \(\tr k=0\) and
\[
(\sigma\circ\widehat h)\xi=0.
\]
Since
\[
(\sigma\circ\widehat h)^2
=\frac14|\sigma|^2|\widehat h|^2\operatorname{Id},
\]
one obtains \(\sigma=0\) and \(k=0\). Thus, when \(\widehat h\) is zero-free,
\[
\|k\|_{H^2}\le
C\bigl(\sqrt{\ell_2(k)}+\|k\|_{L^2}\bigr),
\]
and Rellich compactness gives a finite-dimensional smooth kernel \(K\) and
\[
\boxed{
\ell_2(k)\ge c_1\|k-\pi_Kk\|_{H^2}^2.
}
\]

This finite-kernel result is unconditional under zero-freeness. Positivity of \(c_K\) additionally follows when
\[
\boxed{\Xi|_K=0.}
\]
Under that assumption, first-order Kähler companions can be chosen linearly on \(K\), using a local chart on the space of almost-complex structures rather than the literal expression \(J_0+\dot J\). For \(\eta=k-\pi_Kk\),
\[
d_2(k)\le\frac{\tau_{\mathrm{ref},2}(k)}{2\pi q}
\le C\|\eta\|_{H^1}^2,
\]
and therefore
\[
\boxed{d_2(k)\le C\ell_2(k),\qquad c_K>0.}
\]

The exact second-order identity is
\[
\boxed{
2\pi q\,d_2
=\tau_{\mathrm{ref},2}
-\frac1{\sqrt2}\int\frac{|w_1|^2}{|v_0|},
}
\]
where
\[
w_1=P_{e_0^\perp}v'_0-|v_0|e'_0,\qquad
v_t=B_t^*\widehat h_t,\qquad
e_t=\Omega_t^{\mathrm{ref}}/\sqrt2.
\]
The derivative of the moving reference direction is essential. At transverse zeros \(w_1=O(|h_0|)\), so the quotient is locally bounded, but the zero-free elliptic estimate above does not automatically extend across such zeros.

The full quadratic form \(d_2\) is not compact relative to \(\ell_2\). Under \(\Xi|_K=0\), on the \(\ell_2\)-Hilbert completion of \(K^\perp\), the operator representing \(q^2d_2\) has the form
\[
\boxed{A=T-N,}
\]
where \(T\) is compact self-adjoint and \(N\ge0\) is bounded. Hence the essential spectrum of \(A\) lies in \((-\infty,0]\). If \(d_2\) is positive on some vector, its largest positive eigenvalue is attained and
\[
\boxed{c_K=\lambda_{\max}(A)^{-1}.}
\]

Because \(\widehat h\) is zero-free, \(\delta\) and \(L\) are smooth functionals on a \(C^{2,\alpha}\) metric neighborhood, although their harmonic-form dependence is global rather than pointwise in the metric 2-jet. On the linear space \(\mathcal S\),
\[
\delta(g_0+k)=d_2(k)+O(\|k\|_{C^{2,\alpha}}^3),
\qquad
L(g_0+k)=\ell_2(k)+O(\|k\|_{C^{2,\alpha}}^3).
\]
Thus, assuming \(\Xi|_K=0\), for every \(0<c<c_K\),
\[
\boxed{
L(g_0+k)\ge c q_0^2\delta(g_0+k)
-C\|k\|_{C^{2,\alpha}}^3.
}
\]
Replacing \(q_0^2\) by \(q(g_0+k)^2\) changes only the cubic term. This is a statement on the linear constant-scalar/Bianchi space; a statement for nearby exact constant-scalar metrics also requires a genuine slice and an \(O(\|k\|^2)\) projection onto the linear constraint space.

---

## 4. Product mode: independent calculation and corrected coefficient

Let
\[
M=\Sigma_1\times\Sigma_2,\qquad
K_1,K_2<0,\qquad K_1\ne K_2,
\]
with
\[
\omega=\omega_1+\omega_2,\qquad
\eta=\omega_1-\omega_2,\qquad
\rho_0=r\eta,\qquad r=\frac{K_1-K_2}{2}.
\]
Take a real holomorphic quadratic differential
\[
Q\in\Gamma(S^2_0T^*\Sigma_1),\qquad
\delta Q=0,\qquad \nabla^*\nabla Q=-2K_1Q,
\]
and an eigenfunction on \(\Sigma_2\),
\[
\Delta f=\mu f,\qquad \mu>0.
\]
Set
\[
k=fQ
\]
on the first-factor block. Then
\[
\tr k=0,\qquad \delta k=0,\qquad s'(k)=0,
\]
so \(k\in\mathcal S\). It is realized by a fixed-\(\omega\) compatible variation.

The TT Ricci linearization gives
\[
\Ric'(k)=\left(K_1+\frac{\mu}{2}\right)k.
\]
The \(K_1k\) term is the variation of the \(J_t\)-invariant tensor \(K_1g_{1,t}\), hence
\[
\boxed{(\Ric'')_1=\frac{\mu}{2}k.}
\]
The moving \(J\)-invariant primitive Ricci form is stationary, so
\[
(\rho'_{0,1})^{\perp\mathcal H}=0.
\]

There is a factor-two correction to the generator calculation. At a point with
\[
Q=\operatorname{diag}(a,-a),\qquad df=v\,e^3,
\]
one obtains
\[
(\nabla\omega)'_{e_1}
=\frac{av}{2}(e^{14}+e^{23}),\qquad
(\nabla\omega)'_{e_2}
=\frac{av}{2}(e^{13}-e^{24}),
\]
with the other two derivative directions zero. Therefore
\[
|(\nabla\omega)'|^2
=\frac12|Q|^2|df|^2,
\qquad
\int u_2=\frac{\mu}{8}\|fQ\|_2^2.
\]
For the corresponding connection forms,
\[
\langle\eta,t_2^-\rangle=-u_2,
\]
and consequently
\[
(\rho_0,t_2^-)
=-\frac{r\mu}{8}\|fQ\|_2^2.
\]

Using
\[
8\pi^2(p-q^2)_2
=\|(\Ric'')_1\|_2^2
-4(\rho_0,t_2^-)
+2\|(\rho'_{0,1})^{\perp\mathcal H}\|_2^2,
\]
gives
\[
\boxed{
8\pi^2(p-q^2)_2(fQ)
=\frac{\mu}{4}\bigl[\mu+K_1-K_2\bigr]\|fQ\|_2^2.
}
\]
Thus the earlier factor \(\mu+2(K_1-K_2)\) is twice too large in its curvature-difference term.

If \(K_1<K_2\), this mode descends precisely when
\[
\boxed{0<\mu<K_2-K_1.}
\]
Interchanging the factors gives
\[
8\pi^2(p-q^2)_2(hQ_2)
=\frac{\lambda}{4}\bigl[\lambda+K_2-K_1\bigr]\|hQ_2\|_2^2,
\]
which descends when \(K_2<K_1\) and \(0<\lambda<K_1-K_2\).

For example, take \(K_1=-2\), \(K_2=-1\), and choose \(\Sigma_2\) with \(\lambda_1(\Sigma_2)<1\). Such constant-curvature surfaces exist by degeneration in moduli. Then this mode has
\[
(p-q^2)_2<0.
\]

This mode does not interact with \(\Xi\):

* \(\mu>0\) gives \((\Ric'')_1\ne0\), hence \(\ell_2(k)>0\), so \(k\notin K\) and \(\Xi\) is not evaluated on it.
* The variation keeps \(\omega\) fixed, so its class variation is zero in any event.

Since
\[
\ell_2(k)-2q^2d_2(k)<0
\]
and \(\ell_2(k)\ge0\), necessarily \(d_2(k)>0\), and therefore
\[
\boxed{c_K<2}
\]
for these product examples. This conclusion does not require \(\Xi|_K=0\). It does not produce an aligned \(L=0\) branch; it produces a non-Kähler direction with \(\ell_2>0\) along which \(p-q^2\) decreases.

The necessary spectral condition supplied by this family for \(c_K\ge2\) is
\[
\lambda_1(\Sigma_2)\ge K_2-K_1\quad(K_1<K_2),
\]
or the factor-swapped analogue. Satisfying this inequality does not settle all remaining separated tensor blocks.

An \(O(t^2)\) conformal correction makes the scalar curvature exactly constant because, for \(s<0\), the operator \(6\Delta-2s\) is invertible. Stationarity from Lemma 67.1 ensures that this correction does not alter the displayed quadratic coefficient.

---

## 5. Unconditional wording in §21.11 that requires replacement

The following sentences should not remain as written:

1. **“Every \(\ell_2\)-null direction is first-order Kähler.”**  
   Replace by first-order almost-Kähler alignment, followed by first-order Kählerness only when its \((0,2)\) class lies in \(\operatorname{im}\mathcal P_\omega\).

2. **“The \(H^{2,0}\) directions are realized by \(\omega^{-1}\bar\theta\).”**  
   Replace by the map \(\mathcal P_\omega\); \(\bar\partial(\omega^{-1}\bar\theta)\) need not vanish.

3. **“\(\ker\ell_2\) lies in the radical of \(d_2\).”**  
   Replace by this conclusion for the subspace \(\ker\Xi\subset K\).

4. **“Zero-free \(\widehat h\) implies \(c_K>0\).”**  
   Zero-freeness gives ellipticity, finite-dimensional \(K\), and complement coercivity. Positivity of \(c_K\) follows from the additional condition \(\Xi|_K=0\), or from a separate estimate on the remaining finite-dimensional modes.

5. **“The theorem covers \(\Sigma_g\times\Sigma_h\).”**  
   For products, \(\mathcal P_\omega=0\) and \(H^{0,2}\ne0\); \(\Xi|_K=0\) has not been established. The explicit mode above instead proves \(c_K<2\) for products with a sufficiently small first scalar eigenvalue.

6. **“The infinitesimal aligned non-Kähler seed does not occur.”**  
   Replace by: it does not occur among class-realizable null modes. Modes with \(\Xi\ne0\) remain unresolved.

7. **“\(d_2\) is compact relative to \(\ell_2\).”**  
   Replace by the decomposition \(A=T-N\), with \(T\) compact self-adjoint and \(N\ge0\) bounded.

8. **“\(\delta,L\) are functions of the metric 2-jet.”**  
   They are smooth on a zero-free \(C^{2,\alpha}\) neighborhood, but depend globally on harmonic representatives.

Accordingly, the remaining objects in §21.11 are the finite-dimensional map \(\Xi\), the weighted elliptic estimate across transverse zeros, and the other low separated tensor blocks on a fixed product. The comparison \(c_K\ge2\) is already disproved for the product family described above.