# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 80,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step80_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step80_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the Step-79 second-tier system and the Step-80 use of it as a geometric analyst. Verify or challenge E1/E2, the gradient decomposition, the identification D=24|eta|²-8 trV²+32 Im<alpha,K∂Dv>, and the scope of the complete-model negative conclusion. Pay special attention to conventions (complex form norms, trV²=2|v|², Laplacian sign) and to the fact that the Bianchi-VIII check has real eta and v only. Then assess whether common-denominator regularization reveals a plausible stronger combination with the weighted Kodaira currents, or whether a specific free jet/cross term blocks pointwise coercivity. Give a mathematical memo, not general advice.

## Integrated Scientific Memo

# Mathematical memo: the second-tier equations are consistent; the Step-80 model budget requires correction

The general complex system E1/E2, the gradient decomposition, and the identification of \(D\) are correct with the stated conventions. However, the supplied Step-80 rational model formulas do **not** match the Step-79 geometric calculation. In particular, the claimed adverse leading cancellation by the \(\partial v\) coupling is false on this model.

There is also a useful strengthening not explicit in the source notes: the derivative coupling is exactly a divergence plus algebraic terms. After regularization, it combines with the torsion gradient into the first square of the gradient decomposition. This removes that particular indefinite term, but does not close coercivity with the weighted Kodaira identities.

## 1. General verification, independent of the real-valued model

Use the Hermitian pairing linear in its first argument:
\[
\langle\xi,\zeta\rangle=\sum_a\xi(e_a)\overline{\zeta(e_a)}.
\]
With the full complex-form norm,
\[
|df|^2=2|\partial f|^2\quad(f\ \text{real}),\qquad
|\Re\xi|^2=\frac12|\xi|^2\quad(\xi\in\Lambda^{1,0}).
\]
Consequently,
\[
|\alpha|^2=q/2,\qquad
|W^+|^2=\frac32r^2+2|\eta|^2+2|v|^2,\qquad
\operatorname{tr}V^2=2|v|^2.
\]

### Moving-frame differentiation and E1/E2

Define the one-forms
\[
H=(\nabla W^+)_{11},\quad
Z=(\nabla W^+)_{12}+i(\nabla W^+)_{13},\quad
U=\frac{(\nabla W^+)_{22}-(\nabla W^+)_{33}}2
       +i(\nabla W^+)_{23}.
\]
Differentiating in the stated \((u_1,u_2,u_3)\)-frame gives
\[
\begin{aligned}
H&=dr-2\Re(\eta\alpha),\\
Z&=D\eta+\frac{3r}{2}\bar\alpha-v\alpha,\\
U&=Dv+\eta\bar\alpha.
\end{aligned}                                                    \tag{1}
\]
The algebraic harmonic-Weyl symbol, resolved using
\(\zeta\wedge\psi=2i\hat J(\zeta)\wedge u_1\), is
\[
Z^{1,0}=iK(H^{1,0}),\qquad
\overline{Z^{0,1}}=-2iK(U^{1,0}).                                \tag{2}
\]
Since \(K\) is antilinear, (1)–(2) give precisely
\[
\boxed{\partial_D\eta
=v\alpha-i\bar\eta K\alpha+iK(\partial r),}
\]
\[
\boxed{\overline{\bar\partial_D\eta}
=-\frac{3r}{2}\alpha-2iK(\partial_Dv).}
\]
These are eight independent real equations. At the harmonic-Weyl first-order symbol level, the free variables are
\[
\partial r,\quad \partial_Dv,\quad\bar\partial_Dv,
\]
of total real dimension \(12\). This count should not be interpreted as a realization theorem for arbitrary full almost-Kähler Einstein jets: the remaining structure and higher-order equations still matter.

### Gradient decomposition

For the trace-free symmetric matrix represented by \(H,Z,U\),
\[
|\nabla W^+|^2=\frac32|H|^2+2|Z|^2+2|U|^2.
\]
Put
\[
Y=\partial r-\eta\alpha,\qquad A=\partial_Dv,\qquad
B=\bar\partial_Dv.
\]
Equations (1)–(2) imply
\[
H=Y+\bar Y,\quad |Z^{1,0}|^2=|Y|^2,\quad
|Z^{0,1}|^2=4|A|^2,
\]
and \(U^{1,0}=A,\ U^{0,1}=B+\eta\bar\alpha\). Hence
\[
\boxed{
|\nabla W^+|^2
=5|Y|^2+10|A|^2+2|B+\eta\bar\alpha|^2.}                         \tag{3}
\]
The coefficients \(5,10,2\) depend on using the full complex-form norm, not a half-normalized Hermitian norm.

### Torsion Laplacian and \(D\)

With the analyst sign \(\Delta=\operatorname{div}\operatorname{grad}\), the relevant tensor equations are
\[
\Delta W^+=\frac{s}{2}W^+-6(W^+)^2+2|W^+|^2I,\qquad
\Delta u_1=-2W^+u_1+\frac{s}{3}u_1.
\]
Apply the product rule to \(r=\langle W^+u_1,u_1\rangle\). Writing
\[
I=\Im\langle\alpha,KA\rangle,
\]
the result is
\[
\Delta r=\frac{7s}{6}r-7r^2-6|\eta|^2+4|v|^2-\frac{rq}{2}-8I.
                                                                    \tag{4}
\]
Here E2 evaluates the derivative contribution:
\[
4\sum_a\big\langle(\nabla_aW^+)(\nabla_au_1),u_1\big\rangle=-8I.
\]
Using \(q=4(r-s/6)\) in (4),
\[
\boxed{
\Delta q=8\operatorname{tr}V^2-24|\eta|^2
-\frac{3s}{2}q-\frac94q^2-32I.}                                  \tag{5}
\]
Thus Step 80 correctly defines
\[
\boxed{D=24|\eta|^2-8\operatorname{tr}V^2+32I.}
\]

The radial Laplacian in the script,
\[
\Delta q=\frac1{\sqrt G\,\mathrm{vol}}
 \frac{d}{dp}\left(\frac{\mathrm{vol}}{\sqrt G}\frac{dq}{dp}\right),
\]
has exactly this sign. For example, `logq_check.json` at \(p=0.5\) gives
\[
(\Delta q-\mathrm{base})/16=-2.13775722700575=-2I.
\]

### Scope of the real-model verification

The residuals near \(10^{-40}\) in `dW_check.json` are excellent checks of the implemented geometry, but \(\eta,v\) are real there. Gauge covariance helps identify admissible terms; it does not make the example a general phase test. A frame rotation preserves the invariant phase of \(\bar v\eta^2\), and the model has
\[
\Re\langle\alpha,KA\rangle=0.
\]
Terms involving this real part or \(\Im(\bar v\eta^2)\) would therefore be invisible to that check.

The general moving-frame and tensor derivations above resolve this limitation for E1/E2, (3), and (5). Weight counting and real-model residuals alone would not do so.

## 2. A stronger exact identity: the coupling is a divergence

Let
\[
X=\Re(\eta\alpha),
\]
a gauge-invariant real one-form, identified with a vector field when taking divergence.

The sign in its divergence identity can be derived directly, rather than selected from model integrals. Because \(\alpha\circ J=i\alpha\) and \(\delta\omega=0\),
\[
\langle d_b\alpha,\omega\rangle=i\,\operatorname{div}_b\alpha,
\qquad d_b\alpha=d\alpha-ib\wedge\alpha.
\]
The trace of the supplied torsion structure equation is
\[
\langle d_b\alpha,\omega\rangle=-2i\bar\eta.
\]
Therefore
\[
\boxed{\operatorname{div}_b\alpha=-2\bar\eta.}                    \tag{6}
\]
The gauge-invariant product rule gives
\[
\operatorname{div}(\eta\alpha)=\alpha\cdot D\eta-2|\eta|^2.
\]
Pairing E2 with \(\alpha\), taking real parts, and using its type,
\[
\Re(\alpha\cdot D\eta)
=-\frac{3r}{2}|\alpha|^2-2I.
\]
Combining these identities yields
\[
\boxed{
32I=-32|\eta|^2-12rq-16\operatorname{div}X.}                      \tag{7}
\]
In particular,
\[
D=-8|\eta|^2-8\operatorname{tr}V^2
+2|s|q-3q^2-16\operatorname{div}X,
\]
and (5) becomes
\[
\boxed{
\Delta q-16\operatorname{div}X
=8|\eta|^2+8\operatorname{tr}V^2
-\frac{|s|}{2}q+\frac34q^2.}                                    \tag{8}
\]
Its closed integral is exactly the existing torsion balance
\[
|s|Q=16\int|\eta|^2+16\int\operatorname{tr}V^2+\frac32\int q^2.
                                                                    \tag{9}
\]
Thus the unweighted integrated derivative coupling adds no independent budget beyond that balance.

This also settles the formerly uncertain sign in the second branch’s divergence calculation.

## 3. Correction of the Step-80 model formulas

The metric coefficients in the supplied script imply
\[
\sqrt G\,\mathrm{vol}
=\frac{64p(1+3p^2)}{3(1-p^2)^3},\qquad
\frac{\mathrm{vol}}{\sqrt G}
=\frac{16p(9p^2-1)}{3(1-p^2)}.                                  \tag{10}
\]
Together with the stated \(q\), these give
\[
\Delta q=
-\frac{432(1-p^2)^3(27p^6-87p^4+29p^2-1)}
 {(1+3p^2)^6}.
\]
The corrected quantities, consistent with the Step-79 data, are
\[
\boxed{
|\eta|^2=
\frac{9(1-p^2)^3(9p^2-1)}{(1+3p^2)^4},}                         \tag{11}
\]
\[
\boxed{
D=
\frac{108(1-p^2)^3(297p^6-267p^4+251p^2-25)}
 {(1+3p^2)^6},}                                                 \tag{12}
\]
\[
\boxed{
32I=
\frac{432(1-p^2)^4(9p^2-1)(3p^2+5)}
 {(1+3p^2)^6}.}                                                 \tag{13}
\]
The Step-80 \(\operatorname{tr}V^2\) formula is consistent; its \(|\eta|^2\) is twice (11), its \(D\) has incorrect middle coefficients, and (80.2) is incorrect.

These discrepancies are visible without delicate asymptotics:

- At \(p=0.4\), (11) gives \(0.489199700559344\), as recorded in `dW_check.json`; Step 80 gives twice this value.
- The actual \(D\) there is approximately \(58.116\), not the approximately \(38.47\) obtained from Step 80.
- At \(p=0.9\), \(32I=0.01615745256\ldots>0\), whereas (80.2) gives a negative value.

In fact, \(I\ge0\) throughout \(1/3\le p<1\). Direct rational integration gives
\[
\int32I=512.
\]
This agrees with the supplied budgets:
\[
\int D=18(64)-\frac94\frac{512}{3}=768,\qquad
\int(24|\eta|^2-8\operatorname{tr}V^2)=256.
\]

### Correct end behavior

For \(t=1-p\),
\[
\begin{aligned}
q&=\frac92t^3+O(t^4),&
dV&=\left(\frac{32}{3}t^{-3}+O(t^{-2})\right)dt,\\
|\eta|^2&=\frac94t^3+O(t^4),&
32I&=108t^4+O(t^5),\\
D&=54t^3+O(t^4),&
|dq|^2&=\frac{729}{2}t^6+O(t^7).
\end{aligned}                                                    \tag{14}
\]
Therefore
\[
\frac{24|\eta|^2}{q}\longrightarrow12,\qquad
\frac{32I}{q}=24t+O(t^2)\longrightarrow0.
\]
**There is no leading cancellation of half the \(\eta\) mass.** The derivative coupling is positive and one order smaller at this end.

The transition scale \(t\asymp\varepsilon^{1/3}\) and growth exponent \(\varepsilon^{-2/3}\) remain valid, but the Step-80 numerical table and its component split cannot be used as geometric-model evidence. For reference, the corrected leading scalar asymptotics are
\[
\begin{aligned}
\mathrm{RHS}&\sim C\varepsilon^{-2/3},\\
\int\frac{|dq|^2}{(q+\varepsilon)^2}
&\sim\frac C3\varepsilon^{-2/3},\\
\int\frac D{q+\varepsilon}
&\sim\frac{2C}{3}\varepsilon^{-2/3},
\end{aligned}
\quad
C=\frac{128\pi}{\sqrt3}\left(\frac92\right)^{2/3}.                 \tag{15}
\]
These follow from (14) and
\(\int_0^\infty(1+u^3)^{-1}du=2\pi/(3\sqrt3)\).
The coupling and \(V\)-terms are lower-order, of scale
\(\varepsilon^{-1/3}\).

The supplied Step-80 fast-script/data files are absent from this bounded input, so the precise implementation error cannot be localized here. Agreement within an erroneous scalar model would not validate (11)–(13).

## 4. Regularization is valid, and admits an exact square formulation

Set \(h=q+\varepsilon\). On a closed manifold,
\[
\Delta\log h=\frac{\Delta q}{h}-\frac{|dq|^2}{h^2}
\]
proves (80.R), with its displayed signs. Likewise,
\[
\operatorname{div}(j_f/h)=F_f/h-\langle dq,j_f\rangle/h^2
\]
proves (80.K). Both are valid for every \(\varepsilon>0\), with no zero-set assumption.

Substitute (7) into (80.R). Integration by parts gives
\[
\int\frac{\operatorname{div}X}{h}
=\int\frac{\langle dq,X\rangle}{h^2}.
\]
Now
\[
|dq|^2-16\langle dq,X\rangle
=|dq-8X|^2-64|X|^2,
\]
where
\[
|dq-8X|^2=32|Y|^2,\qquad 64|X|^2=16q|\eta|^2.
\]
Hence the stronger regularized presentation is
\[
\boxed{
32\int\frac{|Y|^2}{h^2}
+\frac{|s|}{2}\int\frac qh
=
8\int\frac{|\eta|^2+\operatorname{tr}V^2}{h}
+16\int\frac{q|\eta|^2}{h^2}
+\frac34\int\frac{q^2}{h}.}                                    \tag{16}
\]
It contains no indefinite derivative coupling. Its derivative is exactly the \(Y\)-square in (3). Multiplication by \(\varepsilon\) followed by \(\varepsilon\to\infty\) recovers (9).

This is a genuine structural improvement over interpreting the cross term solely as an uncontrolled Young-inequality error. It is not a contradiction: both sides of (16) have positive terms.

### End limit and nonuniform escape

The frame formulas in the script determine the previously unresolved end limit. Since
\[
\alpha(E_0)=\frac{x_1x_2'-x_2x_1'}{\sqrt G},
\quad x_i=\sqrt{X_i},
\]
they give
\[
\alpha(E_0)\sim\frac{3\sqrt2}{4}t^{3/2},\quad
\eta\sim-\frac32t^{3/2},\quad
\partial r(E_0)\sim-\frac{27\sqrt2}{16}t^3.
\]
At leading order the forms lie in the same complex radial line, so
\[
|Y|^2\sim\frac{81}{64}t^6,\qquad
\boxed{\frac{32|Y|^2}{q^2}\longrightarrow2.}                    \tag{17}
\]
The unregularized end densities in (16) therefore approach \(8\) on the left and \(12\) on the right. The missing balance is supplied by the transition layer when \(\varepsilon>0\); setting \(\varepsilon=0\) before integrating loses it.

The zero-stratum repairs in Step 80 are sound for their stated normal forms:

- \(q=c\rho^{2m}\) at an isolated four-dimensional zero has no point logarithmic mass.
- A smooth codimension-two stratum with that normal behavior contributes \(4\pi m\) times surface measure.
- A leading polynomial alone does not determine the actual degenerate zero set.

Neither absence of point mass nor analyticity justifies separate singular-term convergence. Formula (16), like (80.R), must be used as a common-denominator family unless those limits are independently controlled.

## 5. Weighted Kodaira combinations: plausible structure, specific obstruction

E1/E2 imply
\[
F_v=|B|^2-|A|^2-\left(|s|-\frac q2\right)|v|^2,
\]
\[
F_\eta
=4|A|^2+6rI+\frac98r^2q
-|v\alpha+iKY|^2
-\left(\frac{|s|}{2}-\frac q4\right)|\eta|^2.                    \tag{18}
\]
Thus the \(\eta\)-Kodaira identity supplies the missing \(4|A|^2\) that the raw scalar identity lacks.

Indeed, at \(P=\partial r=0,\ B=0\), the raw scalar density contains \(32I/h\), with no \(|A|^2\). Taking \(KA=it\alpha\) makes \(I=-tq/2\), of either sign and arbitrarily large at the second-tier symbol level. The scalar density is therefore not pointwise coercive. Adding positive multiples of the Kodaira identities can stabilize this particular direction: the \(|A|^2,|B|^2\) coefficients become
\[
4c_\eta-c_v,\qquad c_v.
\]
They are positive for \(0<c_v<4c_\eta\). Thus the free \(A\)-direction does **not** by itself exclude every stronger combination.

The exact derivative-cancellation combination is
\[
\begin{aligned}
F_\eta+4F_v={}&4|B|^2-|v\alpha+iKY|^2+\frac98r^2q+6rI\\
&-\left(\frac{|s|}{2}-\frac q4\right)|\eta|^2
-4\left(|s|-\frac q2\right)|v|^2.
\end{aligned}                                                    \tag{19}
\]
Equation (7) eliminates its remaining \(I\):
\[
6rI=-6r|\eta|^2-\frac94r^2q
-3\operatorname{div}(rX)+3\langle dr,X\rangle.                  \tag{20}
\]
Consequently, the combined weighted identity has transport current
\[
j_\eta+4j_v+3rX.
\]
This closes the unweighted algebra on \(Y,B,\eta,v,q\), but creates no automatic weighted sign.

The obstruction is explicit. With the volume-form current convention used in the script,
\[
j_f^\flat=\Re\bigl(\bar f(\bar\partial_Df-\partial_Df)\bigr).
\]
Its \(dq\)-pairing contains free \(P\)-\(A\) and \(P\)-\(B\) bilinear terms. In the derivative-cancellation combination, the positive \(|A|^2\) term has disappeared, while the current still generally depends linearly on \(A\). Converting \(I\) into (20) does not eliminate that current dependence.

More generally, Young’s inequality for weighted transport has the form
\[
\frac{|\langle dq,j_f\rangle|}{h^2}
\lesssim
\delta\frac{|Df|^2}{h}
+C_\delta\frac{|dq|^2|f|^2}{h^3}.                              \tag{21}
\]
Absorption into the available radial term \(|dq|^2/h^2\) requires a bound on \(|f|^2/h\). Such a bound is not supplied by the second-tier equations. At a torsion zero, \(\eta\) and \(v\) are components of the first derivative of \(\alpha\); the structure equation does not force them to vanish with \(\alpha\). This is exactly where the denominator mismatch becomes nonuniform.

Accordingly:

- The original cross term can be absorbed **exactly**, not merely estimated.
- A weighted Kodaira strengthening is algebraically plausible.
- The derivative-cancellation combination loses control of a free jet still present in its transport current.
- Combinations retaining positive jet squares face the coefficient/denominator mismatch in (21).

What remains unresolved is a **global, uniform-in-\(\varepsilon\)** estimate for these combined transports and curvature terms, compatible with actual torsion-zero geometry. No such estimate follows from the displayed pointwise system.

## 6. Precise scope of the complete-model negative conclusion

The model decisively refutes the proposed unweighted estimate:
\[
10\int|A|^2+2\int|B+\eta\bar\alpha|^2
=\frac{7136}{21}<384
=2|s|\int\operatorname{tr}V^2.
\]
The supplied integrals support these rational values numerically; their recognition is not itself symbolic integration.

The valid no-go statement concerns arguments transferable to the model by exhaustion: every density must be integrable, every relevant boundary flux must vanish, and no genuinely compact global input may be used. Flux vanishing alone is insufficient. It does not exclude finite-volume estimates, compact extrema, spectral data, zero-set topology, canonical cycles, or Seiberg–Witten information. Nor is the broad claim about all polynomial currents established merely by counting “two decaying factors.”

For every fixed \(\varepsilon>0\), (80.R), (80.K), and (16) have vanishing model end flux and finite relevant integrals. They therefore still share the complete-model obstruction. The distinction appears in uniform control and the \(\varepsilon\downarrow0\) limit.

**Bottom line:** retain E1/E2, the gradient decomposition, \(D\), and the regularized identities; replace the Step-80 model formulas and withdraw the adverse-cancellation interpretation. Formula (16) is the useful strengthened torsion budget. The remaining obstruction is weighted normalized-torsion transport coupled to free Weyl jets and uncontrolled \(|\eta|^2/(q+\varepsilon)\), \(|v|^2/(q+\varepsilon)\), not a leading negative coupling on the Bianchi-VIII end.