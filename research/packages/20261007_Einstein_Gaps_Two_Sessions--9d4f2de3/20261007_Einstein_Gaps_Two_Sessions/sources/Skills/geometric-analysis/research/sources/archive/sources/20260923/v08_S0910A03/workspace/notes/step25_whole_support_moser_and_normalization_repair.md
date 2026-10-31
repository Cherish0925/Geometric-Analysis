# Step 25: normalization-corrected energy and whole-support Wang iteration

## 1. Scope

This note repairs two breaks in the normalized cutoff-flow program for the
critical four-dimensional negative Ishida--LeBrun family.

1. The term \(-2a\operatorname{Rm}\) is present in the evolution of the fully
   covariant curvature tensor, but it is not a net coercive term in the
   four-dimensional curvature energy.  Tensor, inverse-metric, and measure
   variations must be combined.
2. Positive-time estimates only on the plateau \(a=1\) do not preserve the
   geometry of the transition collar.  The first-exit argument needs
   whole-support estimates for \(a\operatorname{Rm}\) and \(aE\), where
   \(E=\operatorname{Ric}+g\).

The buffered single-support construction is retained.  Let

\[
 \partial_tg=-2aE,\qquad a=\chi^2,
\]

and choose a fixed auxiliary cutoff \(\eta\) such that \(\eta=1\) on a
neighborhood of \(\operatorname{supp}\chi\) and
\(\operatorname{supp}d\eta\subset\{a=0\}^{\circ}\).  On a provisional smooth
bilipschitz interval assume the relative four-dimensional Sobolev inequality

\[
 \|u\|_4^2\le \mathsf S\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right)
 \tag{1.1}
\]

on the fixed auxiliary support.  Set

\[
 F=(1+|\operatorname{Rm}|^2)^{1/2},\qquad
 \beta(t)=\mathsf S\|F(t)\|_{L^2(\operatorname{supp}\chi)}.
 \tag{1.2}
\]

At a selected maximal-function good support,
\(\beta(0)\le C r^2\sqrt{1+K_0}\), independently of collapsed volume.

The exact tensor derivation produced by the A01 Codex worker is in
`Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md`.
Its symbolic ledger was rerun in this step and returned `All symbolic ledger
checks: PASS`.

## 2. Pure normalization has no curvature-energy gain in dimension four

For spatially constant \(a\), isolate the homothetic velocity
\(\partial_tg=-2ag\).  The mixed tensor \(R^l{}_{ijk}\) is unchanged, whereas

\[
 \partial_tR_{ijkl}=-2aR_{ijkl}.
 \tag{2.1}
\]

For \(x=|\operatorname{Rm}|^2\), the two curvature tensors in the contraction
contribute \(-4ax\).  The four inverse metrics contribute \(+8ax\).  Hence

\[
 \partial_tx=4ax.
 \tag{2.2}
\]

In dimension four, \(\partial_td\mu=-4a\,d\mu\), so

\[
 \partial_t(x\,d\mu)=0.
 \tag{2.3}
\]

This is the scale invariance of the critical curvature energy.  For
\(F=(1+x)^{1/2}\), the corresponding exact density variation is

\[
 \left.\partial_t(F^p d\mu)\right|_{-2ag}
 =2a\left[(p-2)F^p-pF^{p-2}\right]d\mu.
 \tag{2.4}
\]

Thus at \(p=2\) the pure-normalization contribution is \(-4a\,d\mu\), coming
only from the added constant in \(F^2\).  For \(p>2\), (2.4) is bounded in
absolute value by \(C_paF^p\), hence by the ordinary lower-order term in the
weak energy estimate.  There is no uniform negative \(-4aF^2\) contribution
left after norm and measure variation.  Spatial variation of \(a\) creates the
usual \(da\) and \(\nabla^2a\) terms; these are handled by one integration by
parts and \(|da|^2/a=4|d\chi|^2\).

Consequently the useful curvature inequality is the coarse, scale-consistent
one

\[
 H_2'+cD_2\le C\int\eta^2aF^3+Cr^{-2}H_2,
 \tag{2.5}
\]

not an inequality relying on normalization damping.

## 3. Tensor input on one buffered support

The index-level calculation gives, for an already smooth solution,

\[
 \begin{aligned}
 H_2'+cD_2&\le C\int\eta^2aF^3+Cr^{-2}H_2,\\
 H_3'+cD_3&\le Cr^{-2}H_3+C\int\eta^2a^2F^4,\\
 Q'+cX&\le Cr^{-2}Q+C\int\eta^2aF|E|^2,
 \end{aligned}
 \tag{3.1}
\]

where

\[
 \begin{gathered}
 H_2=\int\eta^2F^2,\quad
 D_2=\int\eta^2a|\nabla\operatorname{Rm}|^2,\\
 H_3=\int\eta^2aF^3,\quad
 D_3=\int\eta^2a^2F|\nabla\operatorname{Rm}|^2,\\
 Q=\int\eta^2|E|^2,\quad
 X=\int\eta^2a|\nabla E|^2.
 \end{gathered}
\]

The strict buffer makes all terms containing \(a\,d\eta\) or
\(da\,d\eta\) vanish.  The three matched Sobolev variables are

\[
 \chi F,\qquad aF^{3/2},\qquad \chi E.
\]

For sufficiently small current \(\beta(t)\), (3.1) yields

\[
 H_2(t)\le e^{Ct/r^2}H_2(0),\qquad
 \mathsf S^2H_3(t)\le \frac{C\beta_*^3}{t},
 \tag{3.2}
\]

where \(\beta_*=\sup_{s\le t}\beta(s)\).  The second estimate uses the
spacetime \(H_3\) bound from the \(q=2\) equation and forward propagation by
the separate \(q=3\) equation.  It is not inferred from a time integral alone.
The same homogeneous defect calculation propagates

\[
 J_6(t):=\int\eta^2a^4|E|^6\le e^{Ct/r^2}J_6(0).
 \tag{3.3}
\]

Initial pointwise pinching gives \(J_6(0)\le C\delta^6V\), where \(V\) is the
volume of the auxiliary support.

## 4. General weighted power inequality

For \(p\ge3\), let \(\Phi=F\) (curvature) or a smooth regularization of
\(|E|\) (defect), and define

\[
 K_p[\Phi]=\int\eta^2a^{p-2}\Phi^p,
 \qquad
 Z_p[\Phi]=\eta a^{(p-1)/2}\Phi^{p/2}.
 \tag{4.1}
\]

Testing the tensor equation before scalarization, differentiating all inverse
metrics and the measure, and integrating each Hessian-\(a\) term once gives

\[
 \boxed{
 \frac d{dt}K_p+c\|\nabla Z_p\|_2^2
 \le Cp^2r^{-2}K_p
   +Cp\int\eta^2a^{p-1}F\Phi^p.}
 \tag{4.2}
\]

Here \(c>0\) is uniform for \(p\ge3\); increasing the polynomial power of
\(p\) on the right is harmless.  The curvature case uses
\(|E|\le CF\), \(|\nabla E|\le C|\nabla\operatorname{Rm}|\).  The defect case
uses the exact homogeneous identity

\[
 (\partial_t-a\Delta)|E|^2
 =-2a|\nabla E|^2+4a\operatorname{Rm}(E,E)
   +2\langle E,\mathcal C_a(E)\rangle.
 \tag{4.3}
\]

The measure term is also homogeneous and is bounded by
\(CaF|E|^p\).  There is no curvature-only source.

The potential in (4.2) is controlled by the fixed cubic moment.  The exact
weight identity is

\[
 a^{p-1}F\Phi^p
 =(aF^3)^{1/3}
  \left(a^{3p/2-2}\Phi^{3p/2}\right)^{2/3}.
 \tag{4.4}
\]

Together with

\[
 K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2},\qquad
 K_{2p}^{1/2}=\|Z_p\|_4^2
 \le\mathsf S(\|\nabla Z_p\|_2^2+r^{-2}K_p),
 \tag{4.5}
\]

Young's inequality gives

\[
 Cp\int\eta^2a^{p-1}F\Phi^p
 \le \frac c2\|\nabla Z_p\|_2^2
 +C p^3\left(r^{-2}+\mathsf S^2H_3\right)K_p.
 \tag{4.6}
\]

Therefore, on any positive-time slab \([t/2,t]\), (3.2) implies

\[
 \frac d{ds}K_p+\frac c2\|\nabla Z_p\|_2^2
 \le Cp^3\left(r^{-2}+\frac{\beta_*^3}{t}\right)K_p.
 \tag{4.7}
\]

This is the subcritical stage.  Only the fixed exponents \(2\) and \(3\) used
critical smallness; the later powers incur a polynomial \(p^3\) factor but no
shrinking smallness threshold.

## 5. Exact match with Yang's fixed-cutoff iteration

Yang's Appendix A uses moments \(\chi^{2p'}\Phi^p\) and updates, in dimension
four,

\[
 p_{j+1}=\frac32p_j,\qquad
 p'_{j+1}=\frac32p'_j+1.
 \tag{5.1}
\]

If \(p'_0=p_0-2\), then induction gives

\[
 p'_j=p_j-2.
 \tag{5.2}
\]

Hence Yang's moment is exactly

\[
 \chi^{2p'_j}\Phi^{p_j}=a^{p_j-2}\Phi^{p_j}=K_{p_j}[\Phi],
 \tag{5.3}
\]

and the endpoint is

\[
 \lim_{j\to\infty}\chi^{2p'_j/p_j}\Phi=a\Phi.
 \tag{5.4}
\]

Yang's potential exponent can be chosen as \(q=6>4\).  Its required weighted
potential is then

\[
 \int\chi^{q-4}F^{q/2}=\int aF^3=H_3.
 \tag{5.5}
\]

Moreover, (3.2) gives

\[
 H_3(s)^{1/3}
 \le C\beta_*\mathsf S^{-2/3}s^{-1/3}.
 \tag{5.6}
\]

The dimensionless combination in Yang's iteration is
\(\mathsf S^{2/3}\mu=C\beta_*\); after the Young step it enters as
\(C p^3\beta_*^3/s\), exactly as in (4.7).  Thus the fixed-cutoff powers in the
source are not merely analogous to the present weights: in dimension four they
are identical.

For completeness, choose times \(\tau_j\uparrow3t/4\), put
\(p_{j+1}=3p_j/2\), and let

\[
 \mathcal M_{p,j}=\int_{\tau_j}^{t}K_p(s)\,ds.
\]

A time cutoff in (4.7), followed by the four-dimensional parabolic Sobolev
inequality, gives

\[
 \begin{aligned}
 &\sup_{[\tau_{j+1},t]}K_{p_j}
  +\int_{\tau_{j+1}}^t\|\nabla Z_{p_j}\|_2^2
 \le L_j\mathcal M_{p_j,j},\\
 &\mathcal M_{p_{j+1},j+1}
 \le C\mathsf S\left(L_j\mathcal M_{p_j,j}\right)^{3/2},\\
 &L_j=Cp_j^3 4^j(t^{-1}+r^{-2}).
 \end{aligned}
 \tag{5.7}
\]

Equivalently,

\[
 \mathcal M_{p_{j+1},j+1}^{1/p_{j+1}}
 \le(C\mathsf S)^{2/(3p_j)}L_j^{1/p_j}
   \mathcal M_{p_j,j}^{1/p_j}.
 \tag{5.8}
\]

Because

\[
 \sum_j\frac1{p_j}=\frac3{p_0},\qquad
 \sum_j\frac{j+\log p_j}{p_j}<\infty,
 \tag{5.9}
\]

all constants in (5.8) have a finite product.  The resulting whole-support
estimate is

\[
 \boxed{
 \|a\Phi\|_{L^\infty(\operatorname{supp}\chi\times[3t/4,t])}
 \le C\mathsf S^{2/p_0}(t^{-1}+r^{-2})^{3/p_0}
 \mathcal M_{p_0,0}^{1/p_0}.}
 \tag{5.10}
\]

This is the precise transition-inclusive estimate that plateau regularity
cannot replace.

## 6. Curvature and defect outputs

### 6.1 Curvature

Use \(\Phi=F\) and start the subcritical iteration at \(p_0=3\).  From (3.2),

\[
 \mathcal M_{3,0}=\int_{t/2}^tH_3(s)\,ds
 \le C\frac{\beta_*^3}{\mathsf S^2}.
 \tag{6.1}
\]

Substitution into (5.10) gives, for \(0<t\le r^2\),

\[
 \boxed{\|aF(t)\|_\infty\le C\frac{\beta_*}{t},\qquad
        \|a\operatorname{Rm}(t)\|_\infty\le C\frac{\beta_*}{t}.}
 \tag{6.2}
\]

The base exponent is \(3\), not \(2\): the fixed \(q=2,3\) argument first
creates the subcritical potential and supplies its positive-time spacetime
norm.

### 6.2 Einstein defect

Use \(\Phi=|E|\) and \(p_0=6\).  From (3.3),

\[
 \mathcal M_{6,0}\le Ct\,\delta^6V.
 \tag{6.3}
\]

The relative Sobolev scaling on the auxiliary support is

\[
 \mathsf S\le Cr^2V^{-1/2}.
 \tag{6.4}
\]

Equations (5.10), (6.3), and (6.4) give

\[
 \boxed{
 \|aE(t)\|_\infty
 \le C\delta\left(\frac{r^2}{t}\right)^{1/3},
 \qquad0<t\le r^2.}
 \tag{6.5}
\]

This is valid on the entire active support, including the transition collar.
Consequently

\[
 \int_0^{\theta r^2}\|aE(s)\|_\infty ds
 \le \frac32C\delta\,\theta^{2/3}r^2.
 \tag{6.6}
\]

For sufficiently small \(\delta\), (6.6) strictly improves the provisional
bilipschitz bound.  Fixed-domain volume comparison, the relative Sobolev
constant, \(|d\chi|\), buffered containment, and the critical product
\(\beta(t)\) then improve simultaneously.  The \(q=2\) energy estimate supplies
the improvement of \(\beta(t)\); no transition curvature bound without the
factor \(a\) is required.

## 7. Consequences and remaining proof

The corrected single-support chain is now

\[
 \begin{gathered}
 \text{buffered good support}
 \longrightarrow H_2\text{ persistence}
 \longrightarrow H_3\text{ at positive time}
 \longrightarrow |a\operatorname{Rm}|,\ |aE|\\
 \longrightarrow \text{metric/Sobolev/cutoff comparison on the whole support}
 \longrightarrow \text{positive-time plateau regularity}.
 \end{gathered}
\]

The remaining analytic issue is smooth continuation of the degenerate
normalized cutoff flow.  Wang proves that bounded \(|\chi^2\operatorname{Rm}|\)
extends the unnormalized local Ricci flow.  His induction couples derivatives
of \(\chi^2\operatorname{Rm}\), unweighted \(L^p\) curvature, and derivatives
of \(\chi\).  The added term \(-2ag\) changes this system only by lower-order
expressions involving the same fixed cutoff and weighted curvature, but the
normalized adaptation still has to be written.  Short-time existence follows
by the same DeTurck/strictly parabolic approximation used by Yang; uniform
existence to \(\theta r^2\) follows once the normalized extension induction is
completed.

After continuation, (6.2) gives ordinary curvature bounds on a smaller
\(a=1\) plateau.  Standard interior normalized Ricci-flow estimates then give
all curvature derivatives there.  The geometric terminal step must remain the
Step 6 argument:

\[
 \operatorname{Spec}(W^+)=(-1/6,1/12,1/12),\quad \delta W^+=0
 \Longrightarrow \nabla W^+=0,
\]

whereas the Einstein--Weyl scalar identity forces
\(|\nabla W^+|^2=1/16\).  Parallel \(W^+\) alone does not imply that the full
curvature is parallel, so no local-symmetry classification is used.

This advances only the critical four-dimensional negative branch.  It does
not establish the unrestricted dimension-dependent interval statement.

## 8. Reproducible verification

`workspace/scripts/verify_step25_normalization_and_moser_exponents.py` checks:

- cancellation of the homothetic contribution in
  \(|\operatorname{Rm}|^2d\mu\) in dimension four;
- formula (2.4) for every power \(p\);
- the exact invariant relation \(p'_j=p_j-2\) in Yang's iteration;
- the potential-weight identity (4.4);
- convergence of the exponent products;
- the endpoint scales \(\beta/t\) and
  \(\delta(r^2/t)^{1/3}\).

The script ran with exit code zero.