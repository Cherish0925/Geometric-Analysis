# Step 18: simultaneous first-exit bootstrap, fixed-supercritical defect propagation, and Noether uniformity

## 1. Corrections to the Step 17 flow statement

The cutoff-flow conclusions in `step17_normalized_cutoff_flow_theorem.md` are not unconditional.  They must be read as implications on a first-exit interval on which the evolving metric, relative Sobolev inequalities, finite-neighbor cover, cutoff derivatives, and local critical energies are provisionally controlled.

Two specific statements from Step 17 fail.

1. A weighted curvature estimate
   \[
   \|a\operatorname{Rm}(t)\|_\infty\le C/t,
   \qquad a=\chi^2,
   \]
   does not by itself preserve the initial Einstein defect through the displayed maximum principle.  Its coefficient is not integrable at zero:
   \[
   \int_0^T\frac{dt}{t}=\infty.
   \]
   Starting at \(t_0=\varepsilon^2\) gives a factor \((T/\varepsilon^2)^C\), which diverges as the auxiliary initial time tends to zero.  Smoothness of each initial metric gives no sequence-uniform substitute.
2. The coupled curvature--defect \(L^2\) inequalities are a bootstrap lemma.  Their derivation uses the provisional evolving Sobolev geometry, volume comparison, overlap constants, cutoff control, and small neighboring energies.  They can improve those energy bounds inside a simultaneous continuation argument, but do not establish all their own inputs.

The earlier transition shortcut based on small metric velocity is also invalid: curvature evolution differentiates \(aE\) twice, and small amplitude gives no derivative bound.

## 2. Simultaneous first-exit framework

Run, for each smooth initial metric, the normalized cutoff flow
\[
\partial_tg=-2aE,\qquad E=\operatorname{Ric}+g,
\qquad a=\chi^2.
\]
Let \(T_*\) be the first time at which one of the following provisional bounds is saturated:

- \(e^{-\zeta}g_0\le g(t)\le e^\zeta g_0\);
- the relative Sobolev constants, ball-volume comparisons, and cover multiplicity exceed fixed multiples of their initial values;
- a local normalized curvature or defect energy exceeds twice its initial bootstrap threshold;
- the connection/cutoff quantities required for continuation leave their assigned norms.

On \([0,T_*)\), the coupled \(L^2\) calculation may be used to improve the energy threshold.  Metric comparability, however, must be improved using an integrable bound for the actual velocity \(aE\), not by integrating \(a\operatorname{Rm}\).

The natural target is, in four dimensions and for one fixed \(p>2\),
\[
 \boxed{\|aE(t)\|_\infty
 \le C_p\delta\left(\frac{r^2}{t}\right)^{2/p}}.
 \tag{M_p}
\]
It yields
\[
 \int_0^{\theta r^2}\|aE(t)\|_\infty dt
 \le \frac{p}{p-2}C_p\delta\,
       \theta^{1-2/p}r^2,
 \tag{1}
\]
which improves metric comparability for small \(\delta\).  The endpoint \(p=2\) is logarithmically divergent.

## 3. Weighted tensor equation

The exact defect equation is
\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E),
\]
with
\[
\begin{aligned}
(\mathcal C_a(E))_{ij}={}&(\Delta a)E_{ij}+2a^k\nabla_kE_{ij}
 +(\operatorname{tr}E)a_{ij}
 +\tfrac12(a_i\nabla_j\operatorname{tr}E+a_j\nabla_i\operatorname{tr}E)\\
&-a_i{}^kE_{kj}-a_j{}^kE_{ki}
-a^k(\nabla_iE_{kj}+\nabla_jE_{ki}).
\end{aligned}
\tag{2}
\]
Set
\[
 U=aE,\qquad \sigma=\operatorname{tr}U.
\]
The terms \(a(\Delta a)E+2a\nabla a\cdot\nabla E\) cancel exactly against the commutator in \(a\Delta(aE)\).  Thus
\[
 \partial_tU=a(\Delta_LU-2U)+\mathcal B_a(U),
\tag{3}
\]
where
\[
\begin{aligned}
(\mathcal B_a(U))_{ij}={}&
 \sigma a_{ij}-a_i{}^kU_{kj}-a_j{}^kU_{ki}
 +\tfrac12(a_i\nabla_j\sigma+a_j\nabla_i\sigma)\\
&-a^k(\nabla_iU_{kj}+\nabla_jU_{ki})
-\sigma\frac{a_i a_j}{a}
+\frac{a^k}{a}(a_iU_{kj}+a_jU_{ki}).
\end{aligned}
\tag{4}
\]
The apparent quotients are regular for \(a=\chi^2\):
\[
\frac{da\otimes da}{a}=4d\chi\otimes d\chi,
\qquad \frac{|da|^2}{a}=4|d\chi|^2.
\tag{5}
\]
As for \(E\), inverse-metric variation cancels the cubic tensor reaction.  Hence
\[
(\partial_t-a\Delta)|U|^2
=-2a|\nabla U|^2+4a\operatorname{Rm}(U,U)
 +2\langle U,\mathcal B_a(U)\rangle.
\tag{6}
\]
The evolving volume satisfies \(\partial_td\mu=-\sigma d\mu\), so higher-power integral energies still contain a term controlled by \(|E||U|^p\).

## 4. Fixed-supercritical tensor energy estimate

Let \(w=|U|\), let \(\eta\) be an independent localization function, and set
\[
 I_p=\int\eta^2w^p,\qquad
 D_p=\int\eta^2a|\nabla w^{p/2}|^2.
\]
Testing the tensor equation before scalarizing is important: terms of the form \(da*U*\nabla U\) require the full tensor dissipation, since \(|\nabla|U||\) does not see rotations of \(U\).  Young's inequality gives
\[
 C_p\eta^2|da|w^{p-1}|\nabla U|
 \le \epsilon\eta^2a w^{p-2}|\nabla U|^2
 +C_{p,\epsilon}\eta^2\frac{|da|^2}{a}w^p.
\tag{7}
\]
The \(\nabla^2a\) terms can be integrated by parts once; they become the same first-derivative terms plus \(da*d\eta*w^p\).  Therefore the defect-side higher-power estimate does not need a pointwise Hessian bound:
\[
\boxed{
\begin{aligned}
\frac d{dt}I_p+c_pD_p\le{}&
 C_p\int\left(a|d\eta|^2+
 \eta^2\frac{|da|^2}{a}\right)w^p\\
&+C_p\int\eta^2a|\operatorname{Rm}|w^p
 +C_p\int\eta^2w^{p+1}.
\end{aligned}}
\tag{8}
\]
This formula is conditional on the provisional smooth first-exit geometry, but it retains all transition commutators.

On a relative-Sobolev ball \(U_\alpha\), use norm form
\[
 \|\varphi\|_4\le A_\alpha
 (\|\nabla\varphi\|_2+r^{-1}\|\varphi\|_2),
 \qquad A_\alpha\lesssim rV_\alpha^{-1/4}.
\tag{9}
\]
For \(z=w^{p/2}\), both reactions have the form
\[
 \int |\operatorname{Rm}|(\chi\eta z)^2,
 \qquad
 \int |E|(\chi\eta z)^2,
\]
because \(w=a|E|\).  Thus
\[
\begin{aligned}
&\int\eta^2a|\operatorname{Rm}|w^p+
 \int\eta^2w^{p+1}\\
&\quad\le C A_\alpha^2
 (\|\operatorname{Rm}\|_{L^2(\widetilde U_\alpha)}+
  \|E\|_{L^2(\widetilde U_\alpha)})
 \left(D_p+r^{-2}\sum_{\beta\sim\alpha}I_{p,\beta}\right).
\end{aligned}
\tag{10}
\]
In dimension four,
\[
 A_\alpha^2\|\operatorname{Rm}\|_2
 \lesssim
 \left(\frac{r^4}{V_\alpha}
 \int_{\widetilde U_\alpha}|\operatorname{Rm}|^2\right)^{1/2},
\tag{11}
\]
so collapsed volume cancels.  For any one fixed \(p>2\), choose the critical energy threshold small depending on \(p\); (10) absorbs into the tensor dissipation and the finite-neighbor inequality gives
\[
 \sup_{0\le s\le\theta r^2}
 \fint_{U_\alpha}|aE(s)|^p\le C_p\delta^p.
\tag{12}
\]
This is a substantive but limited improvement over the Step 17 formulation: a fixed supercritical spatial `L^p` bound can be propagated before pointwise curvature, within the simultaneous first-exit hypotheses. It is not yet the pointwise estimate `(M_p)`; the latter still needs a supercritical time-dependent curvature potential.

One must not repeat this absorption as \(p\to\infty\).  Its coefficient generally scales like \(p\sqrt{\varepsilon_*}\), so fixed \(\varepsilon_*\) cannot absorb every iteration exponent.

## 5. Correct second stage: curvature as a time-dependent potential

After (12), the remaining Moser iteration should treat curvature as a potential rather than repeatedly absorb it by critical \(L^2\) smallness.  A sufficient supercritical curvature input is
\[
 K_{3,\alpha}(t):=
 \int_{\widetilde U_\alpha}a|\operatorname{Rm}|^3
 \le \frac{C}{A_\alpha^4t}.
\tag{13}
\]
Indeed, for \(z=\eta w^{m/2}\), interpolation and Sobolev give
\[
 \int a|\operatorname{Rm}|z^2
 \le \epsilon\|\nabla(\chi z)\|_2^2
 +C_\epsilon A_\alpha^4K_{3,\alpha}(t)\|z\|_2^2
 +Cr^{-2}\|z\|_2^2.
\tag{14}
\]
The stronger estimate \(|a\operatorname{Rm}|\le C/t\), together with local \(L^2\) curvature energy, implies (13).  A Li-type time-cylinder iteration from the fixed \(L^p\) bound then gives conditionally
\[
 |aE(x,t)|
 \le C_p A_\alpha^{4/p}(t^{-1}+r^{-2})^{2/p}
 \|E(0)\|_{L^p(\widetilde U_\alpha)}.
\tag{15}
\]
Since \(A_\alpha\lesssim rV_\alpha^{-1/4}\) and
\(\|E(0)\|_p\le\delta V_\alpha^{1/p}\), volume cancels and (15) becomes \((M_p)\).

The proof is not complete at this point. In particular, the pointwise estimate is downstream of weighted curvature smoothing even though the fixed spatial `L^p` propagation is not. The remaining transition-inclusive inputs are:

- derivation of (13), or an equivalent weighted curvature-potential estimate, from the local critical energy under the degenerate operator \(\partial_t-a\Delta\);
- simultaneous control of the connection and of \(\nabla^2a\), whose evolution contains \(\nabla(aE)*\nabla a\); a pointwise bound on \(aE\) alone does not control this derivative;
- a finite-neighbor version of the Li iteration with evolving measure and weighted dissipation;
- improvement of the unweighted global defect energy \(Q(t)=\int|E|^2\), which does not follow from a weighted pointwise estimate where \(a\to0\).

Thus the difficult center is now narrower: the defect-side fixed-supercritical propagation is available inside the bootstrap, while weighted curvature-potential regularization and connection/cutoff continuation remain coupled.

## 6. Source comparison

Ye Li's Theorem 2.5 explicitly begins with a fixed \(p_0>2\), assumes a time-dependent potential \(u\) with \(\|u\|_{L^3}\lesssim t^{-1/3}\), and then performs the high-exponent iteration.  Corollary 3.5 takes \(p_0=3\).  This is the correct model for the two-stage strategy above.

The Yang theorem quoted in Wang's paper gives, under a global Sobolev inequality, global critical curvature smallness, and a global \(L^p\) Ricci bound,
\[
 \|\chi^2\operatorname{Ric}(t)\|_\infty
 \le C(n,p)A_0^{n/p}t^{-n/(2p)}
 (1+t|\nabla\chi|_0^2)^{n/p+2/p}K.
\]
For \(n=4\) this has the desired \(t^{-2/p}\) exponent and is integrable for \(p>2\).  However, those global hypotheses are stronger than the finite-neighbor relative-Sobolev data here, and the cited theorem concerns \(\operatorname{Ric}\), not the homogeneous Einstein defect under the normalized cutoff flow.  It supplies a structural precedent, not the missing theorem.

## 7. Topological uniformity: Noether, not BMY

Step 17 incorrectly said that BMY automatically bounds \(\chi(M)/A\) above.  BMY gives
\(c_1^2\le3c_2\), hence a lower bound on \(c_2/c_1^2\), the wrong direction.

For a minimal complex surface of general type \(X\), Noether's formula and inequality give
\[
 c_1^2+c_2=12\chi_h,
 \qquad c_1^2\ge2p_g-4,
 \qquad \chi_h=1-q+p_g\le1+p_g.
\]
Consequently
\[
 \chi_h\le\frac{c_1^2+6}{2},
 \qquad
 \boxed{c_2\le5c_1^2+36}.
\tag{16}
\]
For
\[
 M=(\#_{j=1}^mX_j)\#N,
 \qquad m=2,3,
 \qquad A=\sum c_1^2(X_j),
\]
connected sum gives
\[
 \chi(M)=\sum c_2(X_j)+\chi(N)-2m.
\tag{17}
\]
Write Betti numbers of \(N\).  The critical relation
\[
 D=4m-(2\chi+3\tau)(N)=A/3
\]
is equivalent to
\[
 \chi(N)=A/3+6-4m+6(b_+(N)-b_1(N)).
\tag{18}
\]
Thus \(D=A/3\) alone does not bound \(\chi(N)\) above.  Under the actual Ishida--LeBrun hypothesis \(b_+(N)=0\), however,
\[
 \chi(N)=A/3+6-4m-6b_1(N)\le A/3,
\tag{19}
\]
and
\[
 A\ge12(m-1).
\tag{20}
\]
Combining (16)--(20),
\[
 \frac{\chi(M)}A
 \le\frac{16}{3}+\frac{30m+6}{A}
 \le
 \begin{cases}
 65/6,&m=2,\\
 28/3,&m=3.
 \end{cases}
\tag{21}
\]
Hence \(\chi(M)/A\le65/6\) uniformly for the subclass with minimal general-type summands and the standard \(b_+(N)=0\) input.  This does not automatically extend to arbitrary symplectic/almost-complex summands in the broader theorem.

For negative-definite \(N\) with \(b_1=0\), the convention is
\[
 D=4(m-1)+b_-(N),
\]
not \(D=b_-(N)\).  The omitted \(4(m-1)\) is the connected-sum correction.

## 8. Current consequence

The downstream \(7/24\) calibration inequality, exponential-pullback averaging, positive-part monopole density, and forbidden calibrated Einstein germ remain consequential if the simultaneous flow theorem is completed.  Step 18 has not completed that theorem.  It establishes a correct fixed-\(p>2\) defect propagation mechanism inside a first-exit bootstrap, identifies the exact curvature-potential and connection continuation still missing, and repairs the topology-uniformity argument for the minimal-general-type subclass.

Evidence:

- `workspace/scripts/verify_step18_weighted_defect_exponents.py` checks collapse cancellation, drift scaling, the \(p=2\) endpoint, \(C/t\) divergence, and failure of direct all-exponent absorption.
- `workspace/scripts/verify_step18_noether_topology_bound.py` checks the connected-sum/Noether algebra and records why \(D\) alone is insufficient.
- Independent derivations: `trace/ttcs/results/step18_ttcs01_verifier1_integration.md` and `step18_ttcs01_verifier2_integration.md`.
