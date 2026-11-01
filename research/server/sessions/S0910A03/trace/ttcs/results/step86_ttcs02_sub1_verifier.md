# TTCS Independent Branch Record

```json
{
  "step_id": 86,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step86_forced_bochner_superlevel_and_localization.md",
    "Sessions/S0910A03/workspace/scripts/step86_combined_orbit_area_energy.py",
    "Sessions/S0910A03/workspace/data/step86_combined_orbit_area_energy.json",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md"
  ]
}
```

## Task

Verify the new coupled orbit-area energy derivation in Step 86, section 9. Use the conventions dmu=e^sigma dvol, L=Delta+grad sigma dot grad, E=Ric+3g, T=tr_orbit E, e=|dU|^2, X=|grad sigma|^2, W=e+cX, F=tau_sigma(U), V=<dU,F>. Check: (i) whether the forced area trace equation is exactly L sigma=6-T and the sign; (ii) the weighted scalar Bochner formula for X and the rewrite -<grad sigma,grad T>=-div_sigma(T grad sigma)+T(6-T); (iii) after adding orbit Bochner, whether 1/2 L W >= div_sigma(V-cT grad sigma)+W^2/[2(1+c)]-(3+delta)W-D_c(delta)+P with P>=0 and D_c=12c delta+4(c+1)delta^2 really follows under operator |E|<=delta; track every cross/stress/error coefficient and correct it if needed; (iv) the norm bound on J; (v) c=1/2 reaction root series; and (vi) the conditional Cheeger inequality from W<=B and L sigma>=6-2delta, including orientation/absolute-value and domain/boundary caveats. Then assess whether this combined W identity creates a plausible noncircular bootstrap to a length-independent pointwise ceiling, or whether an explicit coupled scalar model still defeats it. Give a direct mathematical memo, preserving the restricted free-OT scope.

## Output

# Mathematical verification memo: coupled orbit–area energy

Let
\[
s=\nabla\sigma,\qquad A=U^*h_{\mathbb H^2},\qquad
e=\operatorname{tr}A,\qquad X=|s|^2,\qquad W=e+cX,
\]
and write
\[
\operatorname{div}_{\sigma}Y
=e^{-\sigma}\operatorname{div}_{\gamma_B}(e^\sigma Y),
\qquad L=\operatorname{div}_{\sigma}\nabla.
\]
Here \(c>0\), \(E_B\) is the horizontal block of \(E\), and
\[
\widehat E=G^{-1}E|_{T^2},\qquad T=\operatorname{tr}\widehat E.
\]

## 1. Orbit-area trace equation

For an OT metric \(g=\gamma_B+G\) with \(G=e^\sigma M\), \(\det M=1\), the vertical Ricci trace is
\[
\operatorname{tr}_{G}\!\left(\operatorname{Ric}_g|_{T^2}\right)
=-\Delta_{\gamma_B}\sigma-|\nabla\sigma|^2=-L\sigma.
\]
Since the vertical trace of \(3g\) is \(6\),
\[
T=\operatorname{tr}_{G}(E|_{T^2})=-L\sigma+6.
\]
Thus
\[
\boxed{L\sigma=6-T.}
\]
The sign in Step 86 is correct. On the round cusp,
\[
\gamma_B=dr^2+e^{2r}dz^2,\qquad \sigma=2r,
\]
one has \(L=\partial_{rr}+3\partial_r+e^{-2r}\partial_{zz}\), hence \(L\sigma=6\), agreeing with \(T=0\).

## 2. Weighted scalar Bochner identity

For the drift \(L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle\),
\[
\frac12LX
=|\operatorname{Hess}\sigma|^2
+\langle s,\nabla L\sigma\rangle
+(\operatorname{Ric}_B-\operatorname{Hess}\sigma)(s,s).
\]
The horizontal Ricci equation is
\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=-3\gamma_B+\frac12\,d\sigma\otimes d\sigma+\frac12A+E_B.
\]
Substitution of \(L\sigma=6-T\) gives
\[
\boxed{
\begin{aligned}
\frac12LX
={}&|\operatorname{Hess}\sigma|^2-3X
+\frac12X^2+\frac12A(s,s)+E_B(s,s)\\
&-\langle s,\nabla T\rangle .
\end{aligned}}
\]
Moreover,
\[
\operatorname{div}_{\sigma}(T\nabla\sigma)
=\langle\nabla T,s\rangle+T L\sigma,
\]
so
\[
\boxed{
-\langle s,\nabla T\rangle
=-\operatorname{div}_{\sigma}(T\nabla\sigma)+T(6-T).}
\]
Both the sign and coefficient are correct.

## 3. Exact combined identity and all coefficients

The orbit-map Bochner identity is
\[
\frac12Le
=|DdU|^2+\operatorname{div}_{\sigma}V-|F|^2
+\frac12e^2+\det A-3e
+\frac12A(s,s)+E_B:A.
\]
Adding \(c/2\) times the scalar identity yields, with
\[
J=V-cT\nabla\sigma,
\]
the exact expression
\[
\boxed{
\begin{aligned}
\frac12LW={}&\operatorname{div}_{\sigma}J
+\frac12e^2+\frac c2X^2-3W\\
&+|DdU|^2+c|\operatorname{Hess}\sigma|^2+\det A
+\frac{1+c}{2}A(s,s)\\
&+E_B:A+cE_B(s,s)-|F|^2+cT(6-T).
\end{aligned}}
\tag{3.1}
\]
Thus:

* the stress coefficient is exactly \((1+c)/2\);
* there is no omitted \(eX\) term;
* \(\det A\ge0\) because \(A\) is a positive-semidefinite \(2\times2\) tensor;
* all derivative terms shown in the second line of (3.1) have the favorable sign.

The quadratic decomposition is stronger than the displayed lower estimate:
\[
\frac12e^2+\frac c2X^2
=
\frac{W^2}{2(1+c)}
+\frac{c}{2(1+c)}(e-X)^2.
\]
Consequently one may take
\[
\boxed{
\begin{aligned}
\mathcal P={}&|DdU|^2+c|\operatorname{Hess}\sigma|^2+\det A
+\frac{1+c}{2}A(s,s)\\
&+\frac{c}{2(1+c)}(e-X)^2,
\end{aligned}}
\qquad \mathcal P\ge0.
\tag{3.2}
\]

Under \(\|E^\sharp\|_{\mathrm{op}}\le\delta\),
\[
E_B:A\ge-\delta e,\qquad E_B(s,s)\ge-\delta X,
\]
hence these terms combine with \(-3W\) to give
\[
-3W+E_B:A+cE_B(s,s)\ge-(3+\delta)W.
\]

Also,
\[
|F|\le2\delta,\qquad |T|\le2\delta,
\]
so
\[
-|F|^2+cT(6-T)
\ge-4\delta^2-c(12\delta+4\delta^2).
\]
Therefore Step 86’s inequality does follow:
\[
\boxed{
\frac12LW\ge
\operatorname{div}_{\sigma}J
+\frac{W^2}{2(1+c)}
-(3+\delta)W
-D_c(\delta)+\mathcal P,
}
\]
with
\[
\boxed{D_c(\delta)=12c\delta+4(c+1)\delta^2.}
\]

### Stronger use of the common vertical defect tensor

The displayed \(D_c\) treats \(F\) and \(T\) independently, although both arise from \(\widehat E\). If \(\lambda_1,\lambda_2\in[-\delta,\delta]\) are the vertical eigenvalues, then
\[
T=\lambda_1+\lambda_2,\qquad |F|=|\lambda_1-\lambda_2|,
\]
and hence
\[
|T|+|F|=2\max(|\lambda_1|,|\lambda_2|)\le2\delta.
\]
Using this relation,
\[
\boxed{
-|F|^2+cT(6-T)
\ge
-\max\{4\delta^2,\;12c\delta+4c\delta^2\}.}
\tag{3.3}
\]
Thus \(D_c\) in Step 86 is valid but not optimal. The stronger constant furnished solely by the vertical operator estimate is
\[
D_c^{\rm vert}(\delta)
=\max\{4\delta^2,\;12c\delta+4c\delta^2\}.
\]

There is also useful gradient coercivity inside \(\mathcal P\). Kato’s inequalities give
\[
|\nabla e|\le2\sqrt e\,|DdU|,
\qquad
|\nabla X|\le2\sqrt X\,|\operatorname{Hess}\sigma|,
\]
and therefore
\[
\boxed{
\mathcal P\ge
|DdU|^2+c|\operatorname{Hess}\sigma|^2
\ge\frac{|\nabla W|^2}{4W}}
\tag{3.4}
\]
where \(W>0\). This term is relevant for excluding abrupt transitions, even though it was left implicit in §9.

## 4. Norm of the combined current

The estimate written in Step 86 is valid:
\[
\begin{aligned}
|J|
&\le |F|\sqrt e+c|T|\sqrt X\\
&\le2\delta\sqrt e+2c\delta\sqrt X\\
&\le2(1+\sqrt c)\delta\sqrt W.
\end{aligned}
\]
The common-eigenvalue relation above yields the stronger estimate
\[
\boxed{
|J|
\le2\delta\max\{\sqrt e,c\sqrt X\}
\le2\delta\max\{1,\sqrt c\}\sqrt W.}
\tag{4.1}
\]
For \(c=\tfrac12\), Step 86 gives \((2+\sqrt2)\delta\sqrt W\), while (4.1) gives simply
\[
|J|\le2\delta\sqrt W.
\]

## 5. Reaction root for \(c=\tfrac12\)

For the Step 86 constant \(D_c\), the positive root of
\[
\frac{W^2}{2(1+c)}-(3+\delta)W-D_c=0
\]
is
\[
k_c=(1+c)\left((3+\delta)
+\sqrt{(3+\delta)^2+\frac{2D_c}{1+c}}\right).
\]
At \(c=\tfrac12\),
\[
D_{1/2}=6\delta+6\delta^2,
\]
and
\[
\boxed{
k_{1/2}
=\frac32\left(3+\delta+\sqrt{9+14\delta+9\delta^2}\right)
=9+5\delta+\frac89\delta^2+O(\delta^3).}
\]
The series in Step 86 and in the JSON file is correct.

If the stronger vertical constant (3.3) is used and \(0<\delta<3\), then
\[
D_{1/2}^{\rm vert}=6\delta+2\delta^2,
\]
giving
\[
k_{1/2}^{\rm vert}
=\frac32\left(3+\delta+
\sqrt{9+14\delta+\frac{11}{3}\delta^2}\right)
=9+5\delta-\frac49\delta^2+O(\delta^3).
\]

The supplied Python script correctly verifies the quadratic minimization and the root series for the coarser \(D_c\). It does not encode the tensor contractions in (3.1), the common vertical-eigenvalue refinement, or the weighted divergence argument.

## 6. Conditional Cheeger estimate

Assume \(W\le B\) on a smooth free-OT domain \(\mathcal D\). Then
\[
|\nabla\sigma|^2=X\le B/c.
\]
Also
\[
L\sigma=6-T\ge6-2\delta.
\]
A positive isoperimetric estimate therefore requires \(\delta<3\).

For every smooth \(\Omega\Subset\mathcal D\), with outward unit normal \(\nu\),
\[
\begin{aligned}
(6-2\delta)\mu(\Omega)
&\le\int_\Omega L\sigma\,d\mu\\
&=\int_{\partial\Omega}\langle\nabla\sigma,\nu\rangle e^\sigma\,dA\\
&\le\int_{\partial\Omega}
|\langle\nabla\sigma,\nu\rangle|e^\sigma\,dA\\
&\le\sqrt{B/c}\,P_\mu(\Omega).
\end{aligned}
\]
The orientation is correct: the signed flux is positive because it equals the integral of \(L\sigma\); absolute values enter only in the upper estimate. Thus the compact-support/Dirichlet Cheeger constant obeys
\[
\boxed{
h_{\mu,\mathcal D}
\ge(6-2\delta)\sqrt{\frac cB}.}
\]
Weighted Cheeger then gives
\[
\boxed{
\lambda_1^{\rm Dir}(-L)
\ge\frac{c(6-2\delta)^2}{4B}.}
\]

This is a Dirichlet or compact-support statement. It does not apply to the Neumann spectral bottom, where constants give eigenvalue zero. On the reflected double there is no central face. On a half-connector, reflection gives \(\partial_\nu\sigma=0\) at the center face, leading to the corresponding mixed realization with Dirichlet data at the exit. Any set meeting a physical exit must include that face in the weighted perimeter and flux formula.

There is also a useful version that avoids assuming a global \(B\). For a regular value \(t\), suppose a component
\[
\Omega_t=\{W>t\}
\]
is compactly contained in the free-OT region and does not meet an exit where \(W\ge t\). On its level face, \(W=t\), so \(X\le t/c\). The same computation gives
\[
\boxed{
P_\mu(\Omega_t)
\ge(6-2\delta)\sqrt{\frac ct}\,\mu(\Omega_t).}
\tag{6.1}
\]
This level-set inequality is genuinely independent of a prior global ceiling.

## 7. Does the \(W\)-identity close the pointwise estimate?

The combined identity supplies two new pieces not present in the orbit-energy estimate alone:

1. the level-set area expansion (6.1);
2. the gradient term \(\mathcal P\ge|\nabla W|^2/(4W)\).

These make a truncation/coarea argument plausible. In particular, after writing \(W=y^2\), the gradient term cancels the usual chain-rule loss:
\[
\frac12L(y^2)=yLy+|\nabla y|^2,
\qquad
\frac{|\nabla W|^2}{4W}=|\nabla y|^2.
\]
The remaining current has size \(|J|/y=O(\delta)\) on high superlevels. This is a materially better structure than applying ordinary Moser iteration to \(e\) alone.

The global Cheeger estimate based on \(W\le B\), however, is conditional: its spectral constant decays like \(B^{-1}\). No estimate in the supplied material yet converts it into a strict improvement \(B\mapsto B'<B\).

A local area–\(W\) scalar layer illustrates why the conditional Cheeger line alone is insufficient. On the round cusp take
\[
\sigma=2r,\qquad X=4,\qquad L\sigma=6,\qquad T=0.
\]
Fix \(H>4c\), set \(W=H\), \(e=H-4c\) on \(|s|<\ell\), and let
\[
R_H=\frac{H^2}{2(1+c)}-(3+\delta)H-D_c+\mathcal P_H>0
\]
for some prescribed constant \(\mathcal P_H\ge0\). Define
\[
J=j(s)\partial_r,\qquad
j(s)=-\frac{R_H}{3}(1-e^{-3s}).
\]
Since \(\operatorname{div}_\sigma(j\partial_r)=j'+3j\),
\[
\operatorname{div}_\sigma J=-R_H,
\]
and hence
\[
\frac12LW=0
=\operatorname{div}_\sigma J
+\frac{H^2}{2(1+c)}-(3+\delta)H-D_c+\mathcal P_H.
\]
Moreover,
\[
|j(s)|\le R_H\ell e^{3\ell}.
\]
Choosing
\[
R_H\ell e^{3\ell}\le2\delta\sqrt{H-4c}
\]
makes the current obey even the stronger \(T=0\) amplitude estimate. For large \(H\), the layer thickness is of order \(\delta H^{-3/2}\). It also satisfies the conditional Cheeger lower estimate because its perimeter-to-volume ratio is much larger than \(H^{-1/2}\).

This scalar object specifies only \((\sigma,W,J)\). It does not furnish an orbit map \(U\), the tensor \(A\), the full horizontal Einstein equations, or a smooth connection from the high plateau to low exit data. In particular, the transition must pay the gradient cost (3.4). Thus it shows that the area equation, the coarse scalar \(W\)-inequality, and the current-amplitude estimate alone permit thin local layers; it does not produce a full OT connector.

The unresolved mathematical point is whether the gradient coercivity, level-set expansion, integrability \(A=U^*h_{\mathbb H^2}\), and horizontal equations together exclude such layers. No globally matched coupled scalar model satisfying all of those structures is present in the supplied files.

All conclusions above remain within smooth free, orthogonally transitive \(T^2\)-regions. Twist terms, singular-orbit regions, and general nonsymmetric metrics introduce equations not represented in this computation.