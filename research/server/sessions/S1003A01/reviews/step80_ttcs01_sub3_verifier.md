# TTCS Independent Branch Record

```json
{
  "step_id": 80,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step79_second_tier_dWplus_kodaira_and_log_torsion_identity.md",
    "Sessions/S1003A01/workspace/notes/step80_regularized_torsion_transport.md",
    "Sessions/S1003A01/workspace/scripts/step79_dW_components_bianchiVIII.py",
    "Sessions/S1003A01/workspace/data/step79/dW_check.json",
    "Sessions/S1003A01/workspace/data/step79/kodaira_flux.json",
    "Sessions/S1003A01/workspace/data/step79/model_integrals_n40.json",
    "Sessions/S1003A01/workspace/data/step79/logq_check.json"
  ]
}
```

## Task

Check the Step-79 second-tier system and the Step-80 use of it as a geometric analyst. Verify or challenge E1/E2, the gradient decomposition, the identification D=24|eta|²-8 trV²+32 Im<alpha,K∂Dv>, and the scope of the complete-model negative conclusion. Pay special attention to conventions (complex form norms, trV²=2|v|², Laplacian sign) and to the fact that the Bianchi-VIII check has real eta and v only. Then assess whether common-denominator regularization reveals a plausible stronger combination with the weighted Kodaira currents, or whether a specific free jet/cross term blocks pointwise coercivity. Give a mathematical memo, not general advice.

## Output

# Mathematical verification memo

## 1. Complex conventions and the \(\delta W^+=0\) system

The conventions in Step 79 are internally consistent provided complex one-forms use
\[
|\xi|^2=\sum_a |\xi(e_a)|^2.
\]
In particular, if \(\xi\in\Lambda^{1,0}\), then
\[
|\xi+\bar\xi|^2=2|\xi|^2.
\]
Also, writing
\[
V=\begin{pmatrix}\Re v&\Im v\\ \Im v&-\Re v\end{pmatrix}
\]
for the trace-free part of \(W^+|_{\langle u_2,u_3\rangle}\), one indeed has
\[
\operatorname{tr}V^2=2|v|^2.
\]

Set
\[
H=(\nabla W^+)_{11},\qquad
Z=(\nabla W^+)_{12}+i(\nabla W^+)_{13},\qquad
U=\frac{(\nabla W^+)_{22}-(\nabla W^+)_{33}}2+i(\nabla W^+)_{23}.
\]
A direct differentiation in the moving \((u_1,u_2,u_3)\)-frame gives
\[
\begin{aligned}
H&=dr-2\Re(\eta\alpha),\\
Z&=D\eta+\frac{3r}{2}\bar\alpha-v\alpha,\\
U&=Dv+\eta\bar\alpha.
\end{aligned} \tag{1}
\]

The algebraic Bianchi symbol can be derived independently of the Bianchi-VIII example. If
\[
R_i\xi=*(\xi\wedge \sqrt2\,u_i),
\]
then \(d^\nabla W^+=0\) is equivalent to
\[
\sum_iR_i(\nabla W^+)_{ij}=0.
\]
Resolving these equations by type, with the Step-79 definition of \(K\), gives
\[
Z^{1,0}=iK(H^{1,0}),\qquad
\overline{Z^{0,1}}=-2iK(U^{1,0}). \tag{2}
\]
Since
\[
H^{1,0}=\partial r-\eta\alpha,\qquad U^{1,0}=\partial_Dv,
\]
equations (2) become exactly
\[
\partial_D\eta
=v\alpha-i\bar\eta K(\alpha)+iK(\partial r),
\]
and
\[
\overline{\bar\partial_D\eta}
=-\frac{3r}{2}\alpha-2iK(\partial_Dv).
\]
Thus E1 and E2, including their conjugations, factors \(3/2,2\), and signs of \(i\), are correct for the stated definition of \(K\).

This derivation is important because the model computation has \(\eta,v\in\mathbb R\). The numerical test by itself cannot distinguish every conjugation or any term proportional to \(\operatorname{Im}(\bar v\eta^2)\). A constant rotation \(\psi\mapsto e^{i\theta}\psi\) produces
\[
\alpha\mapsto e^{-i\theta}\alpha,\qquad
\eta\mapsto e^{i\theta}\eta,\qquad
v\mapsto e^{2i\theta}v,
\]
but it preserves the invariant phase of \(\bar v\eta^2\). Equations (1)–(2) supply the genuinely general verification that the real-model test cannot provide.

## 2. Gradient decomposition

For a symmetric trace-free \(3\times3\) matrix written through \(H,Z,U\),
\[
|\nabla W^+|^2=\frac32|H|^2+2|Z|^2+2|U|^2. \tag{3}
\]
Let
\[
z=\partial r-\eta\alpha,\qquad A=\partial_Dv,\qquad B=\bar\partial_Dv.
\]
Because \(H=z+\bar z\), E1–E2 yield
\[
|H|^2=2|z|^2,\qquad
|Z^{1,0}|^2=|z|^2,\qquad
|Z^{0,1}|^2=4|A|^2,
\]
while
\[
U^{1,0}=A,\qquad U^{0,1}=B+\eta\bar\alpha.
\]
Substitution in (3) gives
\[
\boxed{
|\nabla W^+|^2
=5|\partial r-\eta\alpha|^2
+10|\partial_Dv|^2
+2|\bar\partial_Dv+\eta\bar\alpha|^2.}
\]
The coefficients \(5,10,2\) therefore follow exactly from the full complex-form norm. They would change if one used a half-normalized Hermitian norm.

The numerical value at \(p=0.4\),
\[
23.76707446411,
\]
agrees in `dW_check.json`, but the preceding calculation gives the phase-independent proof.

## 3. The torsion Laplacian and the definition of \(D\)

Let
\[
A=\partial_Dv,\qquad
x=\operatorname{Im}\langle\alpha,KA\rangle,
\]
where the Hermitian product is linear in its first argument, as in the script.

With the analyst tensor Laplacian, the Einstein harmonic-Weyl equation is
\[
\Delta W^+
=\frac{s}{2}W^+-6(W^+)^2+2|W^+|^2I,
\]
and harmonicity of \(\omega\) gives
\[
\Delta u_1=-2W^+u_1+\frac{s}{3}u_1.
\]
Applying these identities to
\[
r=\langle W^+u_1,u_1\rangle
\]
and using \(|\alpha|^2=q/2\), one obtains
\[
\Delta r
=\frac{7s}{6}r-7r^2-6|\eta|^2+4|v|^2-\frac{rq}{2}-8x. \tag{4}
\]
The derivative term in (4) follows from E2:
\[
4\sum_a\left\langle
(\nabla_aW^+)(\nabla_au_1),u_1
\right\rangle=-8x.
\]
Since \(q=4(r-s/6)\), multiplying (4) by four and substituting \(r=s/6+q/4\) gives
\[
\Delta q
=16|v|^2-24|\eta|^2-\frac{3s}{2}q-\frac94q^2-32x.
\]
Using \(\operatorname{tr}V^2=2|v|^2\) and \(s<0\),
\[
\boxed{
\Delta q=-D+\frac{3|s|}{2}q-\frac94q^2,
\quad
D=24|\eta|^2-8\operatorname{tr}V^2
+32\operatorname{Im}\langle\alpha,K\partial_Dv\rangle.}
\]
Thus the Step-80 definition of \(D\), including the sign of the derivative coupling, is correct.

The pointwise model data verify the same sign independently: at \(p=0.5\),
\[
\frac{\Delta q-\text{base}}{16}=-2.13775722700575,
\qquad
\operatorname{Im}\langle\alpha,K\partial_Dv\rangle
=1.06887861350288,
\]
so the omitted contribution is precisely \(-32x\).

The radial expression used by the script,
\[
\Delta q=\frac1{\sqrt G\,\mathrm{vol}}\,
\partial_p\!\left(\frac{\mathrm{vol}}{\sqrt G}\,\partial_pq\right),
\]
is the analyst sign: on a closed manifold,
\[
\int f\Delta f=-\int|df|^2.
\]

## 4. What the complete model establishes

The supplied data strongly support the normalization and all displayed coefficients:

- E1, E2, the torsion equation, and the gradient formula have residuals of order \(10^{-40}\).
- The integrated decomposition gives
  \[
  5\frac{736}{105}+10\frac{1528}{105}
  +2\frac{680}{7}=\frac{2624}{7}.
  \]
- The two Kodaira budgets agree with
  \[
  \int\operatorname{tr}V^2=16,\qquad
  \int|v|^2=8,\qquad
  \int|\eta|^2=16.
  \]
- The proposed \(v\)-gradient estimate is contradicted by the strict numerical separation
  \[
  10\int|\partial_Dv|^2
  +2\int|\bar\partial_Dv+\eta\bar\alpha|^2
  =\frac{7136}{21}\approx339.81<384
  =2|s|\int\operatorname{tr}V^2.
  \]

The rational values are numerically recognized rather than symbolically integrated in the supplied artifacts, although the 24- and 40-node agreement makes the strict inequality far larger than the numerical uncertainty.

Proposition 79.1 has a precise mathematical reading for integrated expressions whose densities are integrable on the model, whose end surface terms vanish, and which use no global datum absent from that model. Any coercive inequality assembled only in this way must also hold on the strict complete example and therefore cannot force \(q\equiv0\).

The phrase “any argument” is broader than what the example mathematically excludes. The complete metric has infinite volume and does not share compact topology, finite-volume averages, zero-set topology, Seiberg–Witten input, or compact extrema. An exhaustion also requires integrability of every term, not merely vanishing flux. Consequently, the model obstructs the unweighted second-tier budgets and similar finite polynomial-current combinations; it does not address arguments using genuinely compact input or estimates uniform as \(\varepsilon\downarrow0\).

For the same reason, the sentence that volume-sensitive or singular weights are the “only” alternatives is valid only inside the displayed polynomial-current algebra. Canonical cycles, compact zero-set geometry, and other topological information also distinguish a closed manifold from this model.

## 5. Common-denominator regularization and the free derivative

The regularized identity is correct:
\[
\int\left[
\frac{|dq|^2}{(q+\varepsilon)^2}
+\frac{D}{q+\varepsilon}
+\frac94\frac{q^2}{q+\varepsilon}
\right]
=\frac{3|s|}{2}\int\frac q{q+\varepsilon}.
\]
It follows directly by integrating \(\Delta\log(q+\varepsilon)\). Likewise,
\[
\int\frac{F_f}{q+\varepsilon}
=\int\frac{\langle dq,j_f\rangle}{(q+\varepsilon)^2}
\]
has the correct sign.

The scalar Step-80 sweep is principally a quadrature and asymptotic test: its rational \(D\) was reconstructed from the torsion equation itself. The independent geometric evidence for \(D\) is instead the Step-79 pointwise calculation and the derivation in Section 3 above. The weighted Kodaira-current sweep was not completed numerically, although its identity is exact algebraically.

The relevant free derivative is
\[
A=\partial_Dv.
\]
Write
\[
P=\partial r=\frac14\partial q,\qquad
B=\bar\partial_Dv,\qquad
x=\operatorname{Im}\langle\alpha,KA\rangle.
\]
E1–E2 give the useful exact formulas
\[
F_v=|B|^2-|A|^2-\left(|s|-\frac q2\right)|v|^2,
\]
and
\[
\begin{aligned}
F_\eta={}&4|A|^2+6rx+\frac94r^2|\alpha|^2\\
&-\left|v\alpha+iK(P-\eta\alpha)\right|^2
-\left(\frac{|s|}{2}-\frac q4\right)|\eta|^2.
\end{aligned} \tag{5}
\]
In contrast, the derivative part of the scalar regularized density is only
\[
\frac{32|P|^2}{(q+\varepsilon)^2}
+\frac{32x}{q+\varepsilon}. \tag{6}
\]
At a point with \(q>0\), set \(P=B=0\) and vary \(A\) so that \(KA=i\,t\alpha\). Then \(x\) has either sign and grows linearly in \(t\), while (6) contains no \(|A|^2\). Hence E1–E2 alone cannot give a pointwise lower bound for the scalar density.

Equation (5) shows why the \(\eta\)-Kodaira identity is nevertheless a plausible strengthening: it contributes \(4|A|^2\). If constants \(c_\eta,c_v\) multiply the two weighted Kodaira identities, then at \(P=0\) the derivative quadratic part becomes
\[
\frac1{q+\varepsilon}\left[
(4c_\eta-c_v)|A|^2+c_v|B|^2
+(32+6rc_\eta)x
\right]. \tag{7}
\]
It is bounded below in both \(A\) and \(B\) when
\[
c_\eta>0,\qquad 0<c_v<4c_\eta.
\]
Thus there is no purely symbolic obstruction to stabilizing \(A\) after the Kodaira terms are included.

Exact cancellation of \(x\) would require
\[
c_\eta=-\frac{16}{3r}.
\]
This is singular at \(r=0\) and has the wrong sign for controlling \(|A|^2\) where \(r>0\). The complete model itself crosses \(r=0\), since \(r=-2+q/4\) there and \(q\) decreases through \(8\). A \(q\)-dependent coefficient merely transfers the problem into an additional \(dq\)-current.

Finally, with the volume-form identification used in the script,
\[
j_f^\flat=\Re\!\left(\bar f\,
(\bar\partial_Df-\partial_Df)\right).
\]
Therefore the terms
\[
\frac{\langle dq,j_f\rangle}{(q+\varepsilon)^2}
\]
contain free \(P\)-\(A\) and \(P\)-\(B\) bilinear transport. Their sign is not fixed by E1 or E2. This is the remaining concrete analytic obstruction: the weighted \(\eta\)-identity supplies the missing \(|A|^2\), but simultaneously introduces normalized torsion transport that must be controlled globally and uniformly in \(\varepsilon\).

The common denominator therefore identifies a credible combined structure, rather than already producing a coercive estimate. Any successful combination must retain the transport terms, the \(4\pi m\) surface residues, and the \(\varepsilon^{-2/3}\) moving layer seen on the complete model. Pointwise absolute-value estimates that discard the derivative coupling lose the leading cancellation exhibited by the Step-80 decomposition.