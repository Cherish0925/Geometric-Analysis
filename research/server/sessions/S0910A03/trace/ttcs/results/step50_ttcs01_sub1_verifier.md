# TTCS Independent Branch Record

```json
{
  "step_id": 50,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step50_normalized_yang_wang_verification.md",
    "Sessions/S0910A03/workspace/notes/step44_normalized_yang_tame_start_restart.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Independently verify the source-based short-time existence argument in the Step 50 note for the degenerate normalized cutoff flow ∂t g=-2χ²(Ric+g). Read Yang's actual Theorem 8.2 lines 785–823 and the Step 44/Step 50 notes. Check the exact Eulerian variation δ[-2(χ∘φ^{-1})² ĝ], its placement in Yang's displayed D h+E ψ slots, and whether the stated Sobolev product/composition estimates genuinely preserve Yang's neighborhood-uniform smooth-tame inverse and unchanged finite derivative loss. Identify any missing term, regularity index, circularity, or unjustified passage. This should be a direct mathematical verification, not a generic review.

## Output

# Scientific verification memo

## 1. What Yang’s Theorem 8.2 actually supplies

The cited passage of Yang’s Theorem 8.2 contains the relevant structural ingredients:

- the transported coefficient
  \[
  \widehat\chi=\chi\circ\varphi^{-1};
  \]
- a coupled hatted metric/diffeomorphism system whose pullback solves
  \(\partial_tg=-2\chi^2\operatorname{Ric}_g\);
- the schematic linearization
  \[
  \begin{aligned}
  \partial_th&=2\widehat\chi^2\Delta h
   +\widehat\chi(B\nabla h+C\nabla\psi)+Dh+E\psi,\\
  \partial_t\psi&=-\widehat\chi^2(P\nabla\psi+Q\nabla h+Rh);
  \end{aligned}
  \]
- linear regularization by \(\varepsilon^2\Delta h\), with energy estimates used to pass to \(\varepsilon\to0\);
- the statement that the linear solution obeys smooth-tame estimates.

The published passage is highly compressed. It does not display inhomogeneous forcing, the time-dependent Sobolev spaces, a numerical derivative loss, uniformity with respect to a neighborhood of reference pairs, or higher parameter derivatives of the inverse. Thus “Yang’s published smooth-tame inverse” should be understood as the inverse asserted and used in Yang’s proof, not as a separately formulated theorem with all constants and indices written out.

## 2. Exact Eulerian variation

Let \(\varphi_r\) be a variation of \(\varphi\), and write
\[
\psi=\left.\frac{d}{dr}\right|_{0}\varphi_r,
\qquad
\zeta=\psi\circ\varphi^{-1}.
\]
Differentiating \(\varphi_r\circ\varphi_r^{-1}=\mathrm{id}\) gives
\[
\delta\varphi^{-1}=-d\varphi^{-1}(\zeta).
\]
Consequently, at a target point \(y\),
\[
\begin{aligned}
\delta(\chi\circ\varphi^{-1})(y)
 &=d\chi_{\varphi^{-1}(y)}\bigl(\delta\varphi^{-1}(y)\bigr)\\
 &=-d(\chi\circ\varphi^{-1})_y(\zeta_y).
\end{aligned}
\]
Therefore
\[
\delta\widehat\chi=-d\widehat\chi(\zeta),
\qquad
\delta\widehat a
=2\widehat\chi\,\delta\widehat\chi
=-2\widehat\chi\,d\widehat\chi(\zeta).
\]

For
\[
N(\widehat g,\varphi)=-2\widehat a\,\widehat g
\]
and \(h=\delta\widehat g\),
\[
\boxed{
DN_{(\widehat g,\varphi)}(h,\psi)
=-2\widehat a\,h
+4\widehat\chi\,d\widehat\chi(\zeta)\,\widehat g.}
\]

The sign and factor \(4\) in Step 50 are correct. There is no further \(h\)-term hidden in \(\delta\widehat a\), since \(\widehat a\) depends on \(\varphi\) but not on \(\widehat g\). In particular, \(d\widehat\chi\) is the ordinary differential of a scalar, so no metric variation enters through it.

If Yang’s \(\psi\) is represented in Lagrangian rather than Eulerian coordinates, the second term is
\[
4\widehat\chi\,d\widehat\chi(R_\varphi\psi)\,\widehat g,
\qquad
R_\varphi\psi=\psi\circ\varphi^{-1}.
\]
Right translation is a zeroth-order operation on the unknown \(\psi\); its Sobolev constants depend tamely on \(\varphi\).

No new term appears in the diffeomorphism equation. That nonlinear equation is unchanged; only its coefficients are evaluated along the normalized reference pair.

## 3. Placement in Yang’s \(Dh+E\psi\) slots

The added derivative has exactly the form
\[
D_Nh+E_N\psi,
\]
where
\[
D_N=-2\widehat a\,\mathrm{Id},
\qquad
E_N\psi=
4\widehat\chi\,d\widehat\chi(R_\varphi\psi)\,\widehat g.
\]
Neither component contains \(\nabla h\) or \(\nabla\psi\). It therefore belongs in Yang’s displayed zeroth-order \(Dh+E\psi\) terms, exactly as stated in Step 50.

There is also a direct comparison with a term already present in Yang’s unnormalized linearization. Varying the transported coefficient in
\(-2\widehat a\,\operatorname{Ric}_{\widehat g}\) produces
\[
4\widehat\chi\,d\widehat\chi(\zeta)\,
\operatorname{Ric}_{\widehat g}.
\]
The normalized addition replaces \(\operatorname{Ric}_{\widehat g}\) by the much simpler coefficient \(\widehat g\). Thus its dependence on \((\widehat g,\varphi)\) has no greater differential order than a coefficient already occurring in Yang’s system.

The pullback calculation is also exact:
\[
\varphi^*(\widehat a\,\widehat g)
=(\varphi^*\widehat a)(\varphi^*\widehat g)
=\chi^2g.
\]
Yang’s original gauge cancellation therefore gives
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g)
\]
without modifying the gauge vector.

## 4. Sobolev regularity and tame order

A precise grading should record one extra derivative on the diffeomorphism:
\[
\|u\|_s^*
=\|\widehat g\|_{H^s}
+\|\varphi\|_{H^{s+1}}.
\]
Indeed,
\[
\|d(\chi\circ\varphi^{-1})\|_{H^s}
\lesssim
C_{s,\mathcal U}\bigl(1+\|\varphi\|_{H^{s+1}}\bigr).
\]
Thus Step 50’s ungraded notation \(\|u\|_{H^{s+r}}\) is valid only with either:

- \(r\ge1\), or
- a staggered grading in which the \(\varphi\)-component already carries one extra derivative.

With \(s_0>n/2+2\), standard multiplication and composition estimates give
\[
\begin{aligned}
\|\widehat a h\|_{H^s}
&\le C_{\mathcal U}\|h\|_{H^s}
 +C_{s,\mathcal U}(1+\|u\|_s^*)\|h\|_{H^{s_0}},\\
\|\widehat\chi\,d\widehat\chi(R_\varphi\psi)\widehat g\|_{H^s}
&\le C_{\mathcal U}\|\psi\|_{H^s}
 +C_{s,\mathcal U}(1+\|u\|_s^*)\|\psi\|_{H^{s_0}}.
\end{aligned}
\]
Hence
\[
\|K_u(h,\psi)\|_{H^s}
\le C_{\mathcal U}\|(h,\psi)\|_{H^s}
 +C_{s,\mathcal U}(1+\|u\|_s^*)
   \|(h,\psi)\|_{H^{s_0}}.
\]

This verifies the high–low estimate in Step 50 after making the grading explicit. Since Yang’s original coefficients already involve the transported cutoff together with \(\operatorname{Ric}_{\widehat g}\), his differential loss must already accommodate at least one derivative of \(\varphi\) and two derivatives of \(\widehat g\). The normalized addition uses one derivative of \(\varphi\) and no derivative of \(h\) or \(\psi\). It therefore does not enlarge whatever finite loss is used in Yang’s construction. The numerical value of that loss cannot be extracted from the cited passage because Yang does not state it.

At energy order \(s\),
\[
\left|
\langle\nabla^sh,\nabla^sK_u(h,\psi)\rangle
\right|
\le C_{\mathcal U}\mathcal E_s
+C_{s,\mathcal U}(1+\|u\|_s^*)
  \mathcal E_{s_0}^{1/2}\mathcal E_s^{1/2}.
\]
No \(s+1\) derivative of either unknown occurs, so this term does not interact with the weighted dissipation
\(\|\widehat\chi\nabla^{s+1}h\|_2^2\), and its constants are independent of the linear regularizer \(\varepsilon\).

## 5. The remaining unstated passage

The product estimate alone does not algebraically turn Yang’s inverse \(L_u^{-1}\) into an inverse for \(L_u+K_u\); no small operator norm for \(L_u^{-1}K_u\) has been established. The mathematically appropriate argument is the one sketched in Step 50 §2.4:

1. solve the directly regularized system
   \[
   (L_u+K_u+\varepsilon^2\Delta_h)v=f;
   \]
2. use Yang’s energy allocation plus the displayed zeroth-order estimate;
3. pass to \(\varepsilon\to0\) using uniform estimates at every Sobolev order;
4. derive parameter-difference and higher parameter-derivative estimates by differentiating the perturbed equation.

Step 44 gives the same-order energy estimate, and Step 50 gives the high–low contribution. What remains unwritten is the full induction for differences and higher Fréchet derivatives in Yang’s time norms. Standard tame composition/inversion results supply it, and the original transported coefficient already requires the same machinery. Still, lines 785–823 themselves do not contain those formulas.

Likewise, Yang’s displayed linearized equations have zero forcing and zero initial variation. Step 50 inserts \(f,\eta\), as required for an inverse. The inhomogeneous version follows from the same regularized energy proof, but it is not literally displayed in the source.

## 6. Overall mathematical assessment

The normalization calculation, the \(Dh+E\psi\) placement, the gauge pullback, and the differential-order comparison are all correct. No normalization term has been omitted. The direct Yang construction also avoids the circular use of nonlinear \(\widehat a+\varepsilon^2\) flows.

The short-time theorem is rigorous as an incremental extension of Yang’s intended smooth-tame linear theory. It is not a self-contained reconstruction from the cited lines alone: the Sobolev grading for \(\varphi\), inhomogeneous inverse, neighborhood-uniform time norms, and higher parameter estimates remain imported from Yang’s compressed “standard arguments.” The phrase “unchanged derivative loss” is mathematically supported by the order comparison above, although Yang’s source does not provide a numerical loss to quote.