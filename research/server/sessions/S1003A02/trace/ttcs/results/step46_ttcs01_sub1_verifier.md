# TTCS Independent Branch Record

```json
{
  "step_id": 46,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step46_lemmaM_elementary_and_AC.md",
    "Sessions/S1003A02/workspace/scripts/step46_lemmaM_elementary.py",
    "Sessions/S1003A02/workspace/data/step46_lemmaM_elementary.json",
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md",
    "Sessions/S1003A02/workspace/notes/step45_lemmaM_and_weyl_departure.md",
    "Sessions/S1003A02/trace/ttcs/results/step45_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Verify Step 46 of the Einstein-gap programme: `workspace/notes/step46_lemmaM_elementary_and_AC.md` (S1003A02). Work in the normalization CH^2 with holomorphic sectional curvature -4, Ric=-6g. Part 1, Lemma M by elementary means. (a) Check the block decomposition N = B_1 ⊕ (Δ0+12) ⊕ (Δ0+6) ⊕ ∇*∇ on K^{-1}, and that B_1 = dd* + ½d*d + 6 is the Hodge form of the one-form block, where the Step-44 'potential 1/2 at s=-4' is the Bochner form after dropping ½||d*a||². Then judge the strategist's worry that the coclosed sector has operator ½Δ_H + 3 with bottom 3.5 < 4 and so breaks L^1. (b) For the K^{-1} radial reduction, check the radial gauge A=6iη with η=½sinh²r σ3, V=9tanh²r, the claim that the Green kernel is radial f(r)e⊗e_o*, the Landau state cosh^{-3}r with eigenvalue 12, the zero-energy decay 2+√13, positivity, and the identity ∫tanh² G = 1/9. (c) Check formula (2.2) for B_1^{-1}, the Kato bound on 2(∇*∇+6)^{-1}, the mixed Hessian of distance on CH^2 (0, -2/sinh 2r, -1/sinh r), local cancellation, and the resulting L^∞ bound. (d) Check periodization, invertibility on quotients, derivative kernels, and the Schauder step (2.3), including surjectivity of L from index 0 plus injectivity. Part 2, Theorem A_C proof steps 1–6. Check: the Yamabe linearization 6(Δ+8); the DeTurck harmonic-map gauge with no loss of derivatives and Jacobi operator ∇*∇+6; the exact identity Ric°=Ric-λg when s=4λ; the Bianchi-gauge expansion with pointwise Q bound; and the York-decomposition coercivity argument. In that argument check the linearized scalar constraint 3Δf+24f, the relation ½(∇*∇+6)X=-df (signs and constants), that the linearized Einstein operator kills δ*X, the upgrade to H² on the locally symmetric quotient, and whether ||h||_{H²} ≤ 2||k||_{H²} really follows. Then check the canonical-branch IFT and the L² torsion bound ∫|∇n|² ≤ C||h||²_{H¹}. Identify any genuine gap, wrong constant or circularity, and state the exact corrected statement. Also check whether an absolute H^s (s≥5) neighbourhood with an injectivity-radius bound implies the C^{2,α}_b hypothesis, given that Step 44's A_H used the false H²⊂L^∞ in dimension 4. Do not infer any blow-up tariff.

## Output

# Scientific verification memo: Step 46

## Overall assessment

The elementary proof of Lemma M is mathematically sound at the qualitative level: all four normal blocks possess quotient-uniform \(L^\infty\) inverses, their first derivatives have integrable kernels, and the connection sector does not create the proposed \(L^1\) obstruction. The radial \(K^{-1}\) calculation correctly derives the exponent \(2+\sqrt{13}\) without external spectral calibration.

Theorem \(A_C\) also follows after two repairs to the written gauge/coercivity argument:

1. harmonic-map gauge gives  
   \[
   \beta_{g_\Gamma}h=O(h\nabla h),
   \]
   rather than \(\beta_{g_\Gamma}h=0\) exactly;
2. the gauge-fixed Einstein operator \(L_E=\nabla^*\nabla-2\mathring R\) does not annihilate \(\delta^*X\) by itself. The natural linearization of \(\operatorname{Ric}-\lambda g\) annihilates pure Lie derivatives. In the proof, the required estimate instead follows because \(\delta^*X+fg_\Gamma=O(\varepsilon h)\) in \(H^2\).

Both repairs fit the displayed quadratic remainder and give the stated coercivity. There is no circular use of \(P\) in obtaining \(\|h\|_{H^2}\le2\|k\|_{H^2}\).

The decimal inverse norms \(0.21490\) and \(0.6790\) are numerical estimates, not rigorous upper constants from the present script. The exact qualitative constants and the formulas involving the finite integral \(I_{dd}\) are rigorous.

---

## 1. Normal operator and the connection-sector concern

### 1.1 Block decomposition

Using the Step-44 Clifford computation, with \(|\Phi_0|^2=24\), the \(a\)-only part of the squared linearization is
\[
\|d^*a\|^2+\|d^+a\|^2+\left\|\frac12a\cdot\Phi_0\right\|^2.
\]
Since
\[
(d^+)^*d^+=\frac12d^*d
\]
on one-forms and
\[
\left|\frac12a\cdot\Phi_0\right|^2
=\frac14|\Phi_0|^2|a|^2=6|a|^2,
\]
the one-form block is exactly
\[
\boxed{B_1=dd^*+\frac12d^*d+6.}
\]

The remaining Step-44 potentials scale from \((2,1,0)\) at scalar curvature \(-4\) to \((12,6,0)\) at scalar curvature \(-24\). Thus
\[
\boxed{
N=B_1\oplus(\Delta_0+12)\oplus(\Delta_0+6)
\oplus\nabla^*\nabla_{K^{-1}}.
}
\]

This agrees with the supplied normalization.

### 1.2 Hodge and Bochner forms

For one-forms on \(\mathbb{CH}^2\),
\[
\Delta_1=\nabla^*\nabla+\operatorname{Ric}
=\nabla^*\nabla-6.
\]
Also
\[
\|d^*a\|^2+\frac12\|da\|^2
=\frac12\langle\Delta_1a,a\rangle+\frac12\|d^*a\|^2.
\]
Consequently
\[
B_1
=\frac12\Delta_1+6+\frac12dd^*
=\frac12\nabla^*\nabla+3+\frac12dd^*.
\]
After dropping the last nonnegative term, the Bochner expression is
\[
\frac12\nabla^*\nabla+3
\]
in holomorphic-curvature-\(-4\) units, corresponding to
\[
\frac12\nabla^*\nabla+\frac12
\]
after rescaling to scalar curvature \(-4\). This reconciles the Step-44 potential.

On coclosed forms the actual operator is
\[
B_1=\frac12\Delta_1+6
=\frac12(\Delta_1+12),
\]
not \(\frac12\Delta_1+3\). The latter results from replacing the rough Laplacian by the Hodge Laplacian without the Ricci correction.

Even that undercounted operator would not obstruct integrability. Since the coexact one-form threshold is \(\alpha_1=1\),
\[
\frac12(\Delta_1+6)
\]
has zero-resolvent decay parameter
\[
s=\sqrt{\alpha_1+6}=\sqrt7,
\]
and hence decay
\[
e^{-(2+\sqrt7)r}.
\]
This is integrable against shell growth \(e^{4r}\), because \(\sqrt7>2\). Comparing the spectral number \(3.5\) directly with \(\rho_0^2=4\) ignores both the leading factor \(1/2\) and the one-form spectral threshold. The connection-sector concern therefore does not materialize.

---

## 2. The \(K^{-1}\) radial calculation

Let
\[
J(r)=\sinh^3r\cosh r,
\qquad
\Delta_r=-\partial_r^2-(3\coth r+\tanh r)\partial_r.
\]

### 2.1 Connection and potential

In the synchronous radial frame,
\[
A=\pm6i\eta,\qquad
\eta=\frac12\sinh^2r\,\sigma_3,
\]
and
\[
|\eta|^2=\frac14\tanh^2r.
\]
Therefore
\[
\boxed{|A|^2=36|\eta|^2=9\tanh^2r.}
\]

There is a sign inconsistency between the prose and the script. With the explicit Maurer–Cartan forms used in the script,
\[
d\sigma_3=-2\sigma_1\wedge\sigma_2,
\]
and the exact symbolic output is
\[
d\eta=e^0\wedge e^3-e^1\wedge e^2,
\]
not the displayed plus sign. This only changes the orientation convention for the Kähler form. It does not change \(|d\eta|^2=2\), \(|\eta|^2\), the potential, or any spectral conclusion.

### 2.2 Why the Green kernel is radial

Parallel transport from \(o\) along the unique geodesic to \(x\) defines a synchronous unitary frame \(e(x)\). The \(U(2)\) isotropy is transitive on geodesic spheres, and connection parallel transport is equivariant under this isotropy. Hence the invariant kernel from \(L_o\) to \(L_x\) has the form
\[
G(x,o)=f(r)e(x)\otimes e_o^*.
\]
In this frame \(A(\partial_r)=0\), \(\langle A,df\rangle=0\), and \(d^*A=0\). Therefore
\[
\nabla^*\nabla(fe)
=
\left[-f''-(3\coth r+\tanh r)f'
+9\tanh^2r\,f\right]e.
\]

### 2.3 Landau state

For \(f_0=\cosh^{-3}r\),
\[
\frac{f_0'}{f_0}=-3\tanh r,
\qquad
\frac{f_0''}{f_0}=9\tanh^2r-3\operatorname{sech}^2r.
\]
Substitution gives
\[
\boxed{\nabla^*\nabla(f_0e)=12f_0e.}
\]
Moreover,
\[
f_0^2J(r)\asymp e^{-6r}e^{4r}=e^{-2r},
\]
so this section is in \(L^2\). Combined with the supplied Kodaira estimate
\[
\nabla^*\nabla_{K^{-1}}\ge12,
\]
it realizes the spectral bottom.

### 2.4 Zero-energy decay and positivity

At infinity the equation becomes
\[
-f''-4f'+9f=0.
\]
For \(f\sim e^{-\mu r}\),
\[
\mu^2-4\mu-9=0,
\]
so the decaying exponent is
\[
\boxed{\mu=2+\sqrt{13}.}
\]
Thus
\[
|G|\,d\mu
=O\!\left(e^{-(2+\sqrt{13})r}e^{4r}\right)dr
=O\!\left(e^{-(\sqrt{13}-2)r}\right)dr,
\]
which is integrable.

Positivity should be understood for the scalar radial coefficient \(f\). The radial Sturm equation has \(V=9\tanh^2r\ge0\), the decaying solution is unique up to scale, and the Green flux chooses its positive scale. Once positive, writing \(p=Jf'\) gives
\[
p'=9J\tanh^2r\,f.
\]
Since \(p(\infty)=0\), one obtains \(p(r)<0\), so \(f\) is decreasing.

### 2.5 Flux identity

Near the pole,
\[
G(r)\sim\frac1{4\pi^2r^2},
\qquad
2\pi^2J(r)G'(r)\longrightarrow-1.
\]
Integrating the homogeneous equation on \(r>\varepsilon\), then sending \(\varepsilon\to0\), gives
\[
-1+9\int_{\mathbb{CH}^2}\tanh^2r\,G\,d\mu=0.
\]
Therefore
\[
\boxed{\int_{\mathbb{CH}^2}\tanh^2r\,G\,d\mu=\frac19.}
\]

The script reproduces this as \(0.111111111014\).

### 2.6 Numerical status

The values
\[
\|G_{K^{-1}}\|_1\approx0.2148993934,
\qquad
\int|\partial_rG|\approx1.4522016
\]
are consistent with the ODE and asymptotics. The second number includes only the radial derivative; the full covariant derivative also contains the connection contribution \(|A|G\), which is integrable because \(A\) is bounded and \(G\in L^1\).

The script integrates only to \(r=14\) and uses floating-point ODE data. It therefore provides numerical approximations rather than certified inequalities with the final decimal digits.

---

## 3. One-form inverse and its kernel

### 3.1 Formula (2.2)

On exact one-forms,
\[
B_1=\Delta_1+6,
\]
whereas on coexact one-forms,
\[
B_1=\frac12(\Delta_1+12).
\]
Using
\[
\Delta_1+12=\nabla^*\nabla+6,
\]
the proposed inverse is
\[
\boxed{
B_1^{-1}
=
2(\nabla^*\nabla+6)^{-1}
-\frac16\,d\left[(\Delta_0+6)^{-1}-(\Delta_0+12)^{-1}\right]d^*.
}
\]
For an exact eigenmode with \(\Delta_1\)-eigenvalue \(x\), its multiplier is
\[
\frac2{x+12}
-\frac{x}{(x+6)(x+12)}
=\frac1{x+6}.
\]
On a coexact mode the second term vanishes and the multiplier is \(2/(x+12)\). On harmonic one-forms it is \(1/6\), as required. Formula (2.2) is therefore exact.

### 3.2 Kato part

Semigroup domination gives
\[
\left|(\nabla^*\nabla+6)^{-1}F\right|
\le(\Delta_0+6)^{-1}|F|,
\]
and
\[
(\Delta_0+6)^{-1}1=\frac16.
\]
Hence
\[
\boxed{
\left\|2(\nabla^*\nabla+6)^{-1}\right\|_{\infty\to\infty}
\le\frac13.
}
\]

### 3.3 Mixed Hessian

For \(h(r)=G_6(r)-G_{12}(r)\),
\[
\nabla_x\nabla_yh
=h''\,dr_x\otimes dr_y+h'\nabla_x\nabla_yr.
\]
Along the geodesic and the three transverse directions, the singular values of the mixed Hessian of distance are
\[
0,\qquad
\frac{2}{\sinh2r},\qquad
\frac1{\sinh r},\qquad
\frac1{\sinh r}.
\]
The signs depend on the choice of radial frames; the note’s signs are consistent with the usual mixed-Hessian convention. Since
\[
\frac{2}{\sinh2r}
=\frac1{\sinh r\cosh r}
\le\frac1{\sinh r},
\]
the operator norm is
\[
\boxed{
\left|\nabla_x\nabla_yh\right|_{\mathrm{op}}
=
\max\left\{|h''|,\frac{|h'|}{\sinh r}\right\}.
}
\]

### 3.4 Local cancellation and far decay

In four dimensions,
\[
G_\mu(r)
=
\frac1{4\pi^2r^2}
+\frac{\mu}{8\pi^2}\log r+O(1).
\]
Therefore the \(r^{-2}\) terms cancel in \(G_6-G_{12}\), and
\[
h'(r)\sim\frac{6-12}{8\pi^2r}
=-\frac6{8\pi^2r}.
\]
Thus
\[
h''=O(r^{-2}),\qquad
\frac{h'}{\sinh r}=O(r^{-2}),
\]
which is locally integrable against \(r^3dr\).

At infinity the \(G_6\) term is slowest:
\[
h,\ h',\ h''
=O\!\left(e^{-(2+\sqrt{10})r}\right).
\]
After multiplication by shell growth \(e^{4r}\), the remaining exponent is \(-(\sqrt{10}-2)r\), so the kernel is integrable.

Defining exactly
\[
I_{dd}
=
\int_{\mathbb{CH}^2}
\max\left\{|h''|,\frac{|h'|}{\sinh r}\right\}\,d\mu,
\]
one obtains the rigorous estimate
\[
\boxed{
\|B_1^{-1}\|_{\infty\to\infty}
\le\frac13+\frac{I_{dd}}6,
\qquad I_{dd}<\infty.
}
\]
The script estimates \(I_{dd}\approx2.07381238\), giving approximately \(0.67896873\). Because the numerical tail and floating-point errors are not enclosed, \(0.6790\) should be labeled an approximation rather than a proved upper constant.

---

## 4. Quotients, derivative kernels, and Schauder estimates

For any universal kernel \(K\in L^1(\mathbb{CH}^2)\), its twisted periodization satisfies
\[
\sup_x\int_{X_\Gamma}|K_\Gamma(x,y)|\,dy
\le
\sup_{\tilde x}
\int_{\mathbb{CH}^2}|K(\tilde x,z)|\,dz.
\]
Thus its \(L^\infty\) operator norm is independent of the quotient.

Invertibility on a compact quotient follows from
\[
B_1\ge6,\qquad
\Delta_0+12\ge12,\qquad
\Delta_0+6\ge6,\qquad
\nabla^*\nabla_{K^{-1}}\ge12.
\]
The periodized Green operator is consequently the actual inverse.

Near the pole, inverse kernels of these second-order elliptic operators behave as \(r^{-2}\), and their first derivatives behave as \(r^{-3}\), which is integrable in real dimension four. Away from the pole, homogeneous interior estimates preserve the established exponential decay. The same reasoning applies to the strongly elliptic, non-Laplace-type block \(B_1\).

It follows that both \(N^{-1}\) and \(N^{-1}\nabla^*\) have quotient-uniform \(L^\infty\) estimates. Local Schauder estimates on fixed balls in the universal cover then give
\[
\boxed{
\|u\|_{C_b^{2,\alpha}}
\le C\|Nu\|_{C_b^{0,\alpha}}.
}
\]

For the first-order operator \(\mathcal L\), positivity of \(N=\mathcal L^*\mathcal L\) gives \(\ker\mathcal L=0\). Its real Fredholm index is the canonical Seiberg–Witten expected dimension,
\[
\frac{c_1(K^{-1})^2-(2\chi+3\tau)}4=0.
\]
Hence its cokernel is zero and
\[
\mathcal L^{-1}=N^{-1}\mathcal L^*.
\]
The derivative-kernel estimate therefore yields
\[
\boxed{
\|v\|_{C_b^{1,\alpha}}
\le C\|\mathcal Lv\|_{C_b^{0,\alpha}}.
}
\]

This completes the analytic content of Lemma M.

---

## 5. Theorem \(A_C\)

### 5.1 Yamabe normalization

For \(\hat g=u^2g\) with \(s_{\hat g}=-24\),
\[
6\Delta_gu+s_gu+24u^3=0.
\]
At \((g_\Gamma,u=1)\),
\[
D_uF=6\Delta_0-24+72
=\boxed{6(\Delta_0+8)}.
\]
Its \(L^\infty\) inverse norm is at most \(1/48\), and universal-cover Schauder estimates give a quotient-independent implicit-function theorem. Thus
\[
\|u-1\|_{C_b^{2,\alpha}}\le C\varepsilon.
\]

Since the conformal Yamabe constant is below zero near \(g_\Gamma\), the scalar-\(-24\) representative is unique. In dimension four,
\[
P(g)=2\int|W_g|^2+\frac1{12}\int s_g^2-16\pi^2\chi,
\]
and \(\int|W|^2\) is conformally invariant. The Yamabe representative minimizes \(\int s^2\) in such a conformal class, giving
\[
P(\hat g)\le P(g).
\]

### 5.2 Harmonic-map gauge

The tension map uses second derivatives of \(\Psi\) and first derivatives of the source metric, so
\[
(g,\Psi)\mapsto\tau_g(\Psi)
\]
is a \(C^1\) map
\[
C_b^{2,\alpha}\times C_b^{2,\alpha}\longrightarrow C_b^{0,\alpha}.
\]
At the identity its Jacobi operator is
\[
\nabla^*\nabla-\operatorname{Ric}
=\boxed{\nabla^*\nabla+6}.
\]
Kato domination gives a quotient-uniform inverse. The resulting map is \(C^1\)-close to the identity and hence a diffeomorphism.

The exact gauge equation is the nonlinear harmonic-map condition
\[
g'^{ij}\bigl(\Gamma(g')-\Gamma(g_\Gamma)\bigr)^k_{ij}=0.
\]
Its expansion is
\[
\boxed{\beta_{g_\Gamma}h=O(h\nabla h),}
\]
not \(\beta_{g_\Gamma}h=0\) exactly. This is the main textual correction in Step 46.

The correction has precisely the same form as the displayed quadratic terms. Differentiating it gives
\[
\nabla\beta h
=O(h\nabla^2h)+O(|\nabla h|^2).
\]
Thus the Ricci expansion remains
\[
\operatorname{Ric}(g')+6g'
=
\frac12L_Eh+Q(h),
\]
with
\[
|Q(h)|
\le
C\bigl(|h||\nabla^2h|+|\nabla h|^2+|h|^2\bigr).
\]
Alternatively, one may construct an exact Bianchi slice after obtaining \(C^{2,\alpha}\) regularity.

### 5.3 Trace-free identity

Because
\[
s(g')=-24=4(-6),
\]
\[
\operatorname{tr}_{g'}\bigl(\operatorname{Ric}(g')+6g'\bigr)=0.
\]
Hence
\[
\boxed{
\operatorname{Ric}^\circ(g')
=\operatorname{Ric}(g')+6g'
}
\]
exactly.

### 5.4 York decomposition and scalar equation

Use
\[
h=k+\delta^*X+fg_\Gamma,
\qquad
\delta k=0,\quad \operatorname{tr}k=0,
\]
with
\[
(\delta^*X)_{ij}
=\frac12(\nabla_iX_j+\nabla_jX_i).
\]
The conformal-Killing operator has a quotient-uniform inverse because \(\operatorname{Ric}=-6g\), so this decomposition is uniformly bounded in \(H^2\).

The scalar variation satisfies
\[
D s(k)=0,\qquad
D s(\delta^*X)=0,
\]
and
\[
D s(fg_\Gamma)=3\Delta f+24f.
\]
Therefore constant scalar curvature gives
\[
(3\Delta+24)f
=
O\!\left(\varepsilon
  (|h|+|\nabla h|+|\nabla^2h|)\right),
\]
so
\[
\boxed{
\|f\|_{H^2}
\le C\varepsilon\|h\|_{H^2}.
}
\]

With
\[
\beta=\delta+\frac12d\,\operatorname{tr},
\]
one has
\[
\beta(fg_\Gamma)=df,
\qquad
\beta(\delta^*X)
=
\frac12(\nabla^*\nabla-\operatorname{Ric})X
=
\frac12(\nabla^*\nabla+6)X.
\]
Thus in exact Bianchi gauge,
\[
\boxed{
\frac12(\nabla^*\nabla+6)X=-df.
}
\]
In harmonic-map gauge the right side acquires \(O(h\nabla h)\):
\[
\frac12(\nabla^*\nabla+6)X
=
-df+O(h\nabla h).
\]
Consequently,
\[
\boxed{
\|X\|_{H^3}
\le C\varepsilon\|h\|_{H^2}.
}
\]

It follows that
\[
\|h-k\|_{H^2}
\le
C\bigl(\|X\|_{H^3}+\|f\|_{H^2}\bigr)
\le C\varepsilon\|h\|_{H^2}.
\]
For \(C\varepsilon\le1/2\),
\[
\|h\|_{H^2}
\le\|k\|_{H^2}+\frac12\|h\|_{H^2},
\]
and hence
\[
\boxed{
\|h\|_{H^2}\le2\|k\|_{H^2}.
}
\]
This deduction is valid and is not circular.

### 5.5 Einstein operator on the gauge component

The sentence that \(L_E\) annihilates \(\delta^*X\) is not correct. Diffeomorphism invariance gives
\[
D(\operatorname{Ric}+6g)(\delta^*X)=0,
\]
whereas
\[
D(\operatorname{Ric}+6g)(h)
=
\frac12L_Eh-\delta^*\beta h
\]
up to convention-dependent simultaneous signs. Thus \(L_E\delta^*X\) generally does not vanish.

The required estimate follows instead from the estimates above:
\[
\|L_E(h-k)\|_{L^2}
\le C\|h-k\|_{H^2}
\le C\varepsilon\|h\|_{H^2}.
\]
Koiso’s estimate gives
\[
\langle L_Ek,k\rangle\ge2\|k\|^2.
\]
Elliptic estimates on the locally symmetric quotient, together with this \(L^2\) gap, give
\[
\|L_Ek\|_{L^2}\ge\kappa\|k\|_{H^2}
\]
with model-dependent \(\kappa>0\). Therefore
\[
\begin{aligned}
P(\hat g)^{1/2}
&=\|\operatorname{Ric}(g')+6g'\|_{L^2}\\
&\ge\frac12\|L_Ek\|_{L^2}
-C\varepsilon\|h\|_{H^2}\\
&\ge c\|h\|_{H^2}
\end{aligned}
\]
for sufficiently small \(\varepsilon\). Hence
\[
\boxed{
\|h\|_{H^2}^2\le C P(\hat g).
}
\]

### 5.6 Canonical branch and torsion

Under the Bourguignon–Gauduchon identification,
\[
\|F(0)\|_{C_b^{0,\alpha}}
\le C\|h\|_{C_b^{1,\alpha}},
\]
because the curvature equation changes algebraically in \(h\), while the Dirac operator contributes first derivatives of \(h\). Also
\[
\|DF(0)-\mathcal L\|_{C_b^{1,\alpha}\to C_b^{0,\alpha}}
\le C\varepsilon,
\]
and the nonlinear terms are bilinear. Lemma M therefore gives a quotient-uniform contraction argument in \(C_b^{1,\alpha}\), producing a unique gauge class in a fixed small neighborhood and
\[
\|v\|_{C_b^{1,\alpha}}\le C\varepsilon.
\]

In \(L^2\),
\[
\mathcal Lv
=
-F(0)-(DF(0)-\mathcal L)v-q(v).
\]
The Step-44 estimate
\[
\|\mathcal Lv\|^2
\ge
\frac12\|\nabla v\|^2+3\|v\|^2
\]
and the pointwise smallness of \(h,v\) give
\[
\boxed{
\|v\|_{H^1}\le C\|h\|_{H^1}.
}
\]

Since \(\Phi_0\) is parallel and \(|\Phi|\) stays uniformly away from zero,
\[
|\nabla n|
\le
C\bigl(|\nabla v|+|v|+|\nabla h|\bigr).
\]
Therefore
\[
\int|\nabla n|^2
\le C\|h\|_{H^1}^2
\le C\|h\|_{H^2}^2
\le C P(\hat g)
\le C P(g).
\]
At scalar curvature \(-4\), the spinor amplitude is uniformly bounded, and the \(W_2\) component is bounded by the full derivative, so
\[
\boxed{R_{\mathrm{can}}(\hat g)\le C'P(g).}
\]

---

## 6. Corrected theorem statement

A precise version supported by the calculations is:

> There are \(\varepsilon_0,C>0\), depending only on the complex-hyperbolic model, such that for every compact quotient \(X_\Gamma\), if one global diffeomorphism \(\phi\) and one constant \(c>0\) satisfy
> \[
> \|c\,\phi^*g-g_\Gamma\|_{C_b^{2,\alpha}}\le\varepsilon_0,
> \]
> then the scalar-\(-24\) Yamabe representative has a unique Seiberg–Witten solution in a fixed \(C_b^{1,\alpha}\) neighborhood of the canonical Kähler solution. For this branch,
> \[
> \int|\nabla n|^2\le C P(\hat g)\le C P(g),
> \qquad
> R_{\mathrm{can}}(\hat g)\le C P(g).
> \]
> The constants are independent of the quotient. In the proof, harmonic-map gauge is used through
> \(\beta h=O(h\nabla h)\), and the gauge and conformal York components are absorbed as \(O(\varepsilon h)\) in \(H^2\).

The result concerns the nearby canonical branch on closed ball quotients. It supplies no estimate for other monopoles on a blow-up and no core or collar price.

---

## 7. Absolute \(H^s\) neighborhoods

On a four-manifold of bounded complex-hyperbolic geometry with injectivity radius at least \(i_0>0\),
\[
H^s\hookrightarrow C^{2,\alpha}
\quad\text{whenever}\quad
s>4+\alpha.
\]
Thus for every \(0<\alpha<1\),
\[
\boxed{
\|h\|_{C_b^{2,\alpha}}
\le C(i_0,\alpha)\|h\|_{H^5}.
}
\]
The constant is uniform along finite covers of a fixed compact quotient because curvature and all of its derivatives are fixed and the injectivity radius does not decrease.

Accordingly, an absolute global \(H^s\) neighborhood with \(s\ge5\), measured after the same global diffeomorphism and scale, does imply the hypothesis of \(A_C\). A volume-normalized or per-unit-volume \(H^s\) smallness statement would not imply it. The earlier \(H^2\) argument remains invalid in dimension four because
\[
H^2\not\hookrightarrow L^\infty.
\]

---

## 8. Artifact consistency

- The script exactly verifies \(V=9\tanh^2r\) and the eigenvalue \(12\).
- Its exact exterior-form output uses \(d\eta=e^{03}-e^{12}\), whereas the note writes a plus sign.
- `Ric_plus_6g_max_abs_at_samples` evaluates three sample points; it is not an exact symbolic identity test in the saved output.
- The scalar norms \(1/6\) and \(1/12\) are exact.
- The values \(0.21489939\), \(2.07381238\), and \(0.67896873\) are high-accuracy numerical estimates but are not interval-certified upper values in the present computation.