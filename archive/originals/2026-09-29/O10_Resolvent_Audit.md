# O10 resolvent audit and separation of diffuse from concentrated Weyl energy

2026-09-29. This note reads the new `O10_Resolvent_Chern_Concentration(1).md` against the previous continuation's `O10_Strengthened_Endpoint.md` and `O10_Strong_Current_Prerequisite.md`. It preserves the original actual-field and class-square hypotheses. It does not claim unrestricted O10 or O11 has been solved.

**Same-continuation status update.** The later `O10_Abelian_Spectral_Independent_Audit.md` verifies a new line-bundle spectral-selection argument which excludes every zero sequence with uniformly bounded opposite-Weyl energy density. The finite-b escape discussed in Section 7 below describes the limitation of the rank-two resolvent/Chern route audited here; it is not the final status after the Abelian argument. The diffuse/tail inequalities remain valid conditional necessities, but are superseded as the final bounded-density obstruction by that stronger contradiction.

## 1. Audit conclusion

The new direct resolvent construction is valid and can replace the previous proof's high-mass gradient truncation followed by a second resolvent. The weighted Hessian argument and Chern localization also survive the audit: the former needs neither a Sobolev inequality nor a derivative of bundle curvature, and the latter retains the zero-set contribution through a smooth amplitude cutoff.

The uploaded threshold `3/8 + delta` is weaker than the previous continuation's `39/4 + delta`. It should not replace that stronger theorem or be registered as a new improvement of its density range. Its useful contribution is a shorter analytic construction, plus a clean statement of the universal curvature-tail obstruction without a density hypothesis.

There is an additional consequence of combining the two proofs: the Weyl energy responsible for the sharp Hopf pairing cannot be supplied by curvature concentration. Any finite-energy-density zero sequence must have at least `50/3` of diffuse opposite-Weyl energy, in addition to a positive concentrated part. Sections 5–6 prove this precisely.

## 2. Direct resolvent: complete energy estimate

Use normalized volume throughout. Let `t` be the actual cubic negative spinor, `L = nabla* nabla`, and `D` its twisted Dirac operator. The inherited endpoint conclusions are

\[
 \|Dt\|_2\to0,\qquad |t|^2\to m_* =128/81\text{ in }L^2,
 \qquad (L-2)t=D^*Dt+(\gamma-1)t-et,
\]

where `gamma` is uniformly bounded and converges to 1 in measure, while `e -> 0` in normalized `L2`. Thus `gamma-1 -> 0` in every finite normalized `Lp`, and `t` is bounded in normalized `L4`.

Choose a smooth radial bundle map `T` equal to the identity for `|t| <= 2` and bounded in norm by 4. Set `z=T(t)`. Since `m_*<4` and `|t|² -> m_*` strongly in `L2`,

\[
 \|z-t\|_2\to0.
\]

No derivative of this cutoff is required. Define

\[
 (4+L)u=6z.
\tag{2.1}
\]

The connection-Laplacian maximum principle gives

\[
 |u|\le6,\qquad |Lu|\le48.
\tag{2.2}
\]

Put `w=u-t` and `d=Dt`. Then

\[
 (4+L)w=6(z-t)-D^*d-(\gamma-1)t+et.
\]

Pairing with `w` gives

\[
 4\|w\|_2^2+\|\nabla w\|_2^2
 =6\langle z-t,w\rangle-\langle d,Dw\rangle
 -\langle(\gamma-1)t,w\rangle+\langle et,w\rangle.
\]

The first two terms are absorbed by Young's inequality, using `|Dw| <= 2|nabla w|`. The remaining two terms satisfy

\[
 |\langle(\gamma-1)t,w\rangle|
 \le\|\gamma-1\|_2\|t\|_4\|w\|_4=o(1),
\]

\[
 |\langle et,w\rangle|
 \le\|e\|_2\|t\|_4\|w\|_4=o(1).
\]

Here `||w||4 <= ||u||infinity + ||t||4` follows directly on the normalized probability space. It is not inferred from a Sobolev estimate. Therefore

\[
 \boxed{\|u-t\|_{H^1_{\rm av}}\to0.}
\tag{2.3}
\]

The same direct resolvent also supplies the residual needed in the stronger `39/4` argument:

\[
 \boxed{(L-2)u=6(z-u)\to0\text{ in }L^2_{\rm av},\qquad Du\to0\text{ in }L^2_{\rm av}.}
\tag{2.4}
\]

Thus all uses of the old bounded resolvent section remain valid after this substitution. In particular `|u|² -> m_*` in normalized `L2`, because `u` is bounded and converges in measure to the same amplitude as `t`.

## 3. Why the weighted Hessian estimate does not hide extra regularity

Write `P_i=nabla_i u`, `H_ij=nabla_i P_j`, `q=|P|²`, and `h=Lu`. The exact antisymmetry identity is

\[
 \int w|H|^2
 =\int w\operatorname{Re}\langle H_{ij},H_{ji}\rangle
 +\frac12\int w\sum_{i,j}|F_{ij}u|^2.
\]

In the first term, integrate the derivative with index `j`, then commute `nabla_j nabla_i P_j`. The contracted covector curvature is Ricci; the other curvature acts on the bundle slot. The only derivative of a traced quantity is `nabla h`. Integrating that term back once gives

\[
 \int w\operatorname{Re}\langle P,\nabla h\rangle
 =\int w|h|^2-\int\operatorname{Re}\langle dw\otimes P,h\rangle.
\]

No `nabla F`, `nabla Ric`, or estimate on `nabla h` is introduced. For

\[
 w=\left(\frac{q+\delta}{L_0^2+q+\delta}\right)^\epsilon,
 \qquad |dw|\sqrt q\le2\epsilon w|H|,
\]

the weight terms are absorbed for a fixed sufficiently small epsilon. The bounded-section interpolation from `div(wq Re<u,nabla u>)` gives

\[
 J=\int wq^2\le C_1\left(I+\int wq\right),
 \qquad I=\int w|H|^2.
\]

Split the bundle curvature at an arbitrary amplitude `T`. Its low part contributes `C_T int w(1+q)`. Young's inequality treats the tail-curvature times `q` term with a small multiple of `J`; choose that small coefficient after fixing `C1`. The coefficient multiplying the tail's squared norm is then independent of `T` and of the total curvature-energy bound. Consequently

\[
 \fint w(|H|^2+q^2)
 \le C_TL_0^{-2\epsilon}
 +C\fint_{|F|>T}|F|^2+C\fint|\operatorname{Ric}+g|^2.
\tag{3.1}
\]

The unweighted calculation first supplies the finite `L2` Hessian and `L4` gradient budgets. Their constants can depend on the total curvature-energy bound; this dependence is permitted in `C_T` and disappears when `L0 -> infinity` with `T` fixed.

For any sets `Z_j` of vanishing relative volume, let

\[
 \Gamma_F=\lim_{T\to\infty}\limsup_j\fint_{|F_j|>T}|F_j|^2.
\]

First take `j -> infinity`, then `L0 -> infinity`, then `T -> infinity` in (3.1). This proves

\[
 \limsup_j\fint_{Z_j}|\nabla u_j|^4\le C\Gamma_F.
\tag{3.2}
\]

This is a tail estimate, not an assertion that the Hessian squares are uniformly integrable on arbitrary small sets.

## 4. Chern localization and the no-density tail obstruction

The unit-section transgression on `u != 0` has

\[
 d\mathcal T_u=c_2(F^E),\qquad
 |\mathcal T_u|\le C\left(|F^E||\nabla(u/|u|)|
 +|\nabla(u/|u|)|^3\right).
\]

A smooth amplitude cutoff below `m_*` turns this into a global Stokes identity. It yields

\[
 \frac{|c_2(E)[M]|}{V}
 \le C\fint_{\{|u|^2\le b_0\}}
       \left(|F^E|^2+|\nabla u|^4\right),
 \qquad 0<b_0<m_*.
\]

The displayed set has relative volume tending to zero. Combining with (3.2) and

\[
 F^E=F_0+\mathscr L(W^-)+o_{L^2}(1),\qquad |F_0|\le C,
\]

gives one universal constant `C_*` such that

\[
 \limsup_j\frac{|c_2(E_j)[M_j]|}{V_j}\le C_*\Gamma_-,
 \qquad
 \Gamma_-:=\lim_{T\to\infty}\limsup_j\fint_{|W_j^-|>T}|W_j^-|^2.
\tag{4.1}
\]

If `Gamma_-` is finite, some fixed-amplitude tail has finite limsup, and hence `avg |W^-|²` is bounded after omitting finitely many indices. This justifies the unweighted curvature budget used above. If `Gamma_-` is infinite, the necessary positive lower bound is automatic. There is no missing density assumption in this dichotomy.

The actual Chern identity gives at least

\[
 \liminf_j c_2(E_j)[M_j]/V_j\ge 5/(12\pi^2).
\]

Therefore every hypothetical endpoint zero sequence, including sequences with unbounded Euler density, must have `Gamma_- >= c > 0`. This is a necessary obstruction. It does not prove that such concentration is impossible.

## 5. New combination: the sharp Hopf budget is diffuse

Now suppose the hypothetical zero sequence has bounded opposite-Weyl energy, and pass to a subsequence with

\[
 b_j=\fint|W_j^-|^2\longrightarrow b<\infty.
\]

The previous strong-current theorem and (2.3) transfer the complete first-torsion projection to `u`. The unweighted Hessian bound then gives the amplitude and phase controls used in the previous continuation. For the bounded ordinary ASD Hopf form `Q_j=-i q_-(u_j)`, the established identities imply

\[
 \fint\langle W_j^-Q_j,Q_j\rangle\to a_*:=5m_*^2/12,
 \qquad\fint|Q_j|^4\to d_*:=m_*^4/64.
\tag{5.1}
\]

The tails do not contribute to the first limit. Indeed, because `Q_j` is bounded,

\[
 \left|\fint_{|W_j^-|>T}\langle W_j^-Q_j,Q_j\rangle\right|
 \le\frac{C}{T}\fint|W_j^-|^2\le C_b/T.
\tag{5.2}
\]

Write `Gamma(T)=limsup_j avg_{|W_j^-|>T}|W_j^-|²`. The sharp trace-free three-dimensional inequality and Cauchy–Schwarz, restricted to the complementary set, give

\[
 (a_*-C_b/T)_+^2
 \le\frac23\bigl(b-\Gamma(T)\bigr)d_*.
\tag{5.3}
\]

To justify the liminf appearing here, apply the finite-j inequality and then take the liminf of the low-amplitude energy; it equals `b-Gamma(T)` because the total energies converge. The fourth moments are bounded by the full moments in (5.1).

Letting `T -> infinity` proves

\[
 \boxed{b-\Gamma_-\ge\frac{3a_*^2}{2d_*}=\frac{50}{3}.}
\tag{5.4}
\]

Thus the `50/3` lower bound and the curvature-tail obstruction require separate portions of the energy. Counting the same concentrated energy as satisfying both would lose information.

## 6. A positive fraction of the Weyl energy must concentrate

For a finite-b zero sequence, the exact actual-field curvature limits in the previous continuation give

\[
 \frac{c_2(E_j)[M_j]}{V_j}
 \longrightarrow\frac{b+10/3}{8\pi^2}.
\tag{6.1}
\]

Equation (4.1) therefore implies

\[
 \Gamma_-\ge\lambda(b+10/3),
 \qquad
 \lambda:=\min\left\{\frac12,\frac1{8\pi^2C_*}\right\}>0.
\tag{6.2}
\]

The constant is universal and does not depend on `b`. Combine (5.4) with (6.2):

\[
 b\ge\frac{50}{3}+\lambda(b+10/3),
\]

and hence

\[
 \boxed{b\ge\frac{50}{3}+\frac{20\lambda}{1-\lambda}.}
\tag{6.3}
\]

This gives a quantitative expression for a positive margin above `50/3` in terms of the universal Chern-tail estimate. It is compatible with, and refines the description of, the earlier existential excess gap. It is not a computed numerical optimum because `C_*` has not been optimized.

For example, with

\[
 \Delta_b=20\lambda/(1-\lambda),\qquad
 \delta_{\rm top}=9\Delta_b/32,
\]

the actual Euler budget `b <= 16B/9-2/3` at `B=39/4+delta_top` gives `b <= 50/3+Delta_b/2`, contradicting (6.3). The finite-parameter exclusion and the manuscript's exact conformal comparison then recover the all-parameter, original-metric O10 gap in this density range. This is a more informative proof of a positive extension; the earlier stronger theorem remains the correct status baseline.

## 7. Exact remaining obstruction

The direct resolvent construction requires no bounded opposite-Weyl energy. Its `H1` approximation and bounded rough Laplacian hold even when that energy diverges. However, the amplitude-gradient and Hopf-pairing step uses the unweighted Hessian budget, whose constant depends on a bound for the opposite-Weyl energy. Finite total density and finite tail are enough for the stated results; neither is silently available in a general zero sequence.

Even for bounded density, (5.4) and (6.2) are consistent when `b` is sufficiently large. They identify the permitted escape quantitatively: a diffuse component costing at least `50/3`, plus a concentrated component carrying a universal positive fraction of the total topological curvature budget. Ruling out that combination requires another actual geometric constraint or a construction showing that it occurs. No additional choice of cutoff or Young parameter in the present argument removes it.

The uniform-integrability hypothesis is therefore not a dispensable convenience in this argument: it is precisely what destroys the concentrated component. The research target remains to control that component using its Levi-Civita/actual-field origin, beyond the information of an arbitrary unitary bundle with a bounded approximate eigensection.
