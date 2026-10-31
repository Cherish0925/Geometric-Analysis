# Step 92: full separator Jacobi form, Maxwell control, and the remaining collar problem

Session `S0910A03`, Agent1 / Explore.

## 1. Correction of the Step 91 sign

Let \(\Sigma=\pi^{-1}(C)\) be the invariant separator, \(\nu\) its normal,
\(\mathcal H=\operatorname{tr}\mathrm{II}\), and
\[
E=\operatorname{Ric}_g+3g,
\qquad D=\operatorname{tr}_gE-2E(\nu,\nu).
\]
Contracted Gauss is
\[
\boxed{R_\Sigma=-6+D+\mathcal H^2-|\mathrm{II}|^2.}
\tag{1.1}
\]
At the minimal separator \(\mathcal H=0\),
\[
\boxed{R_\Sigma=-6+D-|\mathrm{II}|^2\le -6+4\delta.}
\tag{1.2}
\]
This agrees with a Koiso totally geodesic center, where \(D=0\),
\(\mathrm{II}=0\), and \(R_\Sigma=-6\). Thus the Step 91 interpretation that a
turning slice required positive scalar curvature was false. It also conflated
\(\mathcal H=0\) with \(\partial_r\mathcal H=0\). The flat-slice result remains
valid: when \(R_\Sigma=0\), (1.1) and
\(|\mathrm{II}|^2\ge\mathcal H^2/3\) give
\(\mathcal H^2\ge9-6\delta\), so a radial flat-torus cylinder cannot reverse
for \(\delta<3/2\).

The correction was made in
`workspace/notes/step91_separator_stability_and_barriers.md`,
`workspace/plans/step91_route_map.md`, and
`workspace/scripts/step91_slice_curvature_tradeoff.py`, and transmitted to the
session group as message #673.

## 2. Full invariant stability, not only the constant test

The curve \(C\) minimizes
\[
\int_C\rho\,ds=\operatorname{Length}_{\rho^2\gamma_B}(C)
\]
in its primitive essential class. Every small normal variation stays in that
class. Its lift gives an invariant variation of \(\Sigma\), so for every smooth
periodic speed \(\phi(s)\),
\[
\boxed{
\int_C\rho V\phi^2ds
\le
\int_C\rho\bigl[(\phi_s)^2+(3-E_{\nu\nu})\phi^2\bigr]ds,}
\tag{2.1}
\]
where
\[
V:=|\mathrm{II}|^2
=\kappa^2+\frac12h_\nu^2+\frac12e_\nu+Q.
\tag{2.2}
\]
This is stability only against invariant speeds; the minimizing-loop argument
does not establish stability against torus-dependent variations. The constant
test recovers \(\langle V\rangle_\rho\le3+\delta\), but (2.1) contains more
nonlocal information.

Along \(C\), use base arclength \(s\), write \(\rho=e^\sigma\),
\(h=\sigma_s\), and let \(e_s=|U_s|^2\). The intrinsic formula is
\[
R_\Sigma=-2h_s-\frac32h^2-\frac12e_s.
\tag{2.3}
\]
Combining (1.2) before taking inequalities gives the exact pointwise identity
\[
\boxed{
h_s=3-\frac D2+\frac V2-\frac34h^2-\frac14e_s.}
\tag{2.4}
\]
Tangential orbit energy helps supply the negative curvature of the separator;
it does not conflict with it.

A useful unweighted integrated consequence follows by integrating (2.4) around
\(C\):
\[
\int_C V\,ds=-6L_C+\int_C D\,ds
 +\frac32\int_Ch^2\,ds+\frac12\int_Ce_s\,ds.
\tag{2.5}
\]
Combining this with (3.1) below at \(y=1\) gives, after optimizing the two
nonnegative terms,
\[
\boxed{\int_CV\,ds\le
 \left(\frac{24}{5}+\frac85\delta\right)L_C.}
\tag{2.6}
\]
This removes the \(\rho\)-weight from the average estimate, although it still
scales with separator length and gives no height control by itself.

## 3. Unweighted Schrödinger form

Put \(\phi=\rho^{-1/2}y\). Direct conjugation gives
\[
e^{\sigma/2}\left[-\rho^{-1}(\rho\phi_s)_s+
 (3-E_{\nu\nu}-V)\phi\right]
=-y_{ss}+\left(3-E_{\nu\nu}-V+\frac12h_s+\frac14h^2\right)y.
\]
Using (2.4), define
\[
\mathcal W:=\frac34V+\frac18(h^2+e_s),
\qquad
c_E:=\frac92-E_{\nu\nu}-\frac D4.
\]
Then (2.1) is exactly
\[
\boxed{
\int_C\mathcal W y^2ds
\le\int_C\bigl(y_s^2+c_Ey^2\bigr)ds.}
\tag{3.1}
\]
In an adapted orthonormal frame,
\[
c_E=\frac92-\frac14\sum_{i=1}^3E(e_i,e_i)-\frac34E_{\nu\nu},
\]
so
\[
\frac92-\frac32\delta\le c_E\le
 a_\delta:=\frac92+\frac32\delta.
\tag{3.2}
\]
Hence
\[
\boxed{
\int_C\mathcal W y^2ds
\le\int_C(y_s^2+a_\delta y^2)ds.}
\tag{3.3}
\]
The symbolic conjugation has zero residual in
`workspace/scripts/step92_weighted_jacobi_transform.py` and
`workspace/data/step92_weighted_jacobi_transform.json`.

Equation (3.3) is independent of oscillation of \(\rho\). It yields a
Birman--Schwinger/capacity constraint. With
\(H_\delta=-\partial_s^2+a_\delta\) and its periodic Green kernel \(G_\delta\),
\[
\|\mathcal W^{1/2}H_\delta^{-1}\mathcal W^{1/2}\|\le1,
\tag{3.4}
\]
and therefore
\[
\iint G_\delta(s,t)\mathcal W(s)\mathcal W(t)\,dsdt
\le\int_C\mathcal W\,ds.
\tag{3.5}
\]
Because \(\mathcal W\ge3Q/4\) and
\(\mathcal W\ge3e_\nu/8\), this controls concentrated mass of both quantities.
It is stronger than the weighted average, but it is not a pointwise estimate.

For constant coefficients on a circle of length \(L\), the exact capacity of
an interval of length \(\ell\) is
\[
\operatorname{Cap}_{a}(I_\ell)
=a\ell+2\sqrt a\tanh\left(\frac{\sqrt a(L-\ell)}2\right).
\tag{3.6}
\]
The square-well computation confirms that
\(-\partial_s^2+a-A\mathbf1_{I_\ell}\ge0\) can hold with
\[
A\to\infty,
\qquad
A\ell\to2\sqrt a\tanh\left(\frac{\sqrt aL}{2}\right).
\tag{3.7}
\]
For \(a=3,L=2\pi\), numerical critical values have
\(A\ell=5.6595,4.5170,3.9778,3.7175,3.5899,3.5267\) as
\(\ell=1,1/2,\ldots,1/32\), tending to
\(2\sqrt3\tanh(\sqrt3\pi)\approx3.464\). Thus stability alone permits
arbitrarily tall narrow spikes with bounded mass. Reproducible file:
`workspace/data/step92_jacobi_concentration_models.json`.

## 4. Maxwell transport removes separator charge-height concentration

Let \(w=\sqrt{2Q}\). The invariant physical Maxwell inequality restricted to
\(C\) is
\[
\boxed{
\left|w_s+\frac32hw\right|
\le\frac12w\sqrt{e_s}+2\sqrt2\,\delta.}
\tag{4.1}
\]
Consequently
\[
|w_s|\le c(s)w+B_\delta,
\quad
c=\frac32|h|+\frac12\sqrt{e_s},
\quad B_\delta=2\sqrt2\delta,
\tag{4.2}
\]
and
\[
c^2\le\frac52(h^2+e_s)\le20\mathcal W.
\tag{4.3}
\]
This is the crucial coupling. The same local Schrödinger capacity that controls
\(Q\)-mass controls the exponential cost for changing \(w\).

A concrete coarse bound follows. If the separator length
\(L_C\ge2/\sqrt{a_\delta}\), center a tent cutoff at a maximum of \(Q\) and use
\(r=a_\delta^{-1/2}\). Equation (3.3) yields
\[
\int_{|s-s_*|\le r/2}\mathcal W\,ds
\le M:=\frac8r+\frac83a_\delta r
=\frac{32}{3}\sqrt{a_\delta}.
\]
There is a point in this arc with
\(Q\le(4/3)M/r=(128/9)a_\delta\), and along a connecting subarc
\[
\int c\,ds\le\sqrt{20M(r/2)}=\sqrt{320/3}.
\]
Gronwall applied directly to \(w\), without dividing by it, gives
\[
\sup_CQ\le
\frac12e^{2\sqrt{320/3}}
\left(\frac{16}{3}\sqrt{a_\delta}
      +\frac{\sqrt2\delta}{\sqrt{a_\delta}}\right)^2.
\tag{4.4}
\]
For \(L_C<2/\sqrt{a_\delta}\), the global constant test and the shorter arc
give another dimensionless bound. Taking the larger yields
\[
\boxed{\sup_CQ\le C_Q(\delta),}
\tag{4.5}
\]
independent of separator length and \(\rho\)-oscillation. The displayed constant
is enormous (about \(6\times10^{10}\) even at \(\delta=0\)); it proves finite
height, not smallness. Constants were recomputed in
`workspace/scripts/step92_jacobi_maxwell_bound.py` and
`workspace/data/step92_jacobi_maxwell_bound.json`.

This is a real improvement over the constant stability test: the separator
charge cannot form arbitrary-height spikes. It does not bound
\(Q_+=\sup_BQ\), which is what a global twisted resolvent comparison would need.

## 5. Why normal orbit energy remains uncontrolled at separator-jet level

There is no corresponding first-order transport law for
\(e_\nu=|U_\nu|^2\). The orbit equation
\[
\tau_\sigma(U)=-\nabla Q+Z
\tag{5.1}
\]
controls a trace of second derivatives. On one curve, an arbitrarily large
first normal jet can be balanced by choosing the second normal jet. Thus
bounded \(Q\) and bounded tension do not imply bounded \(e_\nu\) without a
collar geometry, boundary data, and a regularity scale.

The reduced relations themselves admit a formal spike family. Let
\(P_\ell=(m/\ell)\chi(s/\ell)\) with
\(m<2\sqrt3\tanh(\sqrt3L/2)\), and prescribe along \(C\)
\[
\rho=1,\ h=D=E_{\nu\nu}=Q=\kappa=h_\nu=0,
\quad
e_\nu=2P_\ell,
\quad V=P_\ell,
\quad e_s=12+2P_\ell.
\tag{5.2}
\]
Then the intrinsic and Gauss scalar formulas agree,
\(R=-6-P_\ell\), and the Jacobi form is
\(-\partial_s^2+3-P_\ell\ge0\) for sufficiently narrow smooth spikes. The
Maxwell equation is trivial. At the level of target-map jets, choose the second
normal jet to satisfy the trace equation (5.1). This gives
\(\sup e_\nu\sim\ell^{-1}\to\infty\) with bounded mass.

The preceding abstract jets can in fact be upgraded to exact local Einstein
germs. For any positive analytic periodic \(P(s)\), choose a closed immersed
curve \(U:S^1\to\mathbb H^2\) of prescribed speed
\[
|U_s|^2=12+2P.
\]
Such a curve is obtained by traversing a hyperbolic geodesic circle with a
nonuniform analytic parameter. Put
\[
q=ds^2+M(U(s))_{ab}dx^adx^b,
\qquad A=\tfrac12M^{-1}M_s.
\]
Let \(N\) be the target unit normal to \(U_s\),
\(C_N=M^{-1}dM(N)\), and define the vertical trace-free Weingarten block
\[
B=\sqrt{P/2}\,C_N,
\qquad W(\partial_s)=0.
\]
Then
\[
\operatorname{Scal}_q=-\frac12|U_s|^2=-6-P,
\quad \operatorname{tr}W=0,
\quad \operatorname{tr}(W^2)=P.
\]
Moreover, the only nontrivial momentum component is
\(\operatorname{tr}(AB)=0\), because \(N\perp U_s\). Hence the complete
Einstein Cauchy constraints for \(\lambda=-3\) hold:
\[
d\operatorname{tr}W+\delta W=0,
\qquad
\operatorname{Scal}_q+\operatorname{tr}(W^2)
-(\operatorname{tr}W)^2=-6.
\tag{5.3}
\]
With the source convention \(g_t(WX,Y)=-\dot g_t(X,Y)/2\), the orbit normal
velocity is \(U_\nu=-\sqrt{2P}\,N\), so
\[
\boxed{e_\nu=2P.}
\tag{5.4}
\]

Take analytic von Mises spikes \(P_k\,ds\rightharpoonup m\delta_0\), with
\[
m<2\sqrt3\tanh(\sqrt3L/2).
\]
For sufficiently large concentration parameter,
\(-\partial_s^2+3-P_k>0\). In this special translation-invariant block metric,
Fourier modes in the torus directions add the nonnegative potential
\(k^TM^{-1}k\), so invariant strict stability is actually full strict
stability. Nevertheless \(\sup e_\nu=2\sup P_k\to\infty\).

Koiso's analytic Cauchy theorem (as stated in \cite{ammann2018cauchy}) now gives,
for every fixed \(k\), a genuine local analytic metric with
\(\operatorname{Ric}=-3g\) and these stable minimal central data. This closes a
local question decisively: even full stability, full Cauchy constraints, and
exact Einstein equations in a neighborhood do not bound normal orbit energy.
The germ radius may shrink with concentration, and the construction supplies
neither complete ends nor a two-ended connector. Symbolic/numerical
normalization checks are in
`workspace/scripts/step92_constrained_spike_koiso.py` and
`workspace/data/step92_constrained_spike_koiso.json`; TTCS independently
verified all factors, the momentum connection terms, global target normal,
analyticity, full Fourier-mode stability, and the Koiso conclusion.

## 6. The decisive remaining free-\(T^2\) question

Normal Maxwell transport has the form
\[
\left|\partial_\nu w+\frac32h_\nu w\right|
\le\frac12w\sqrt{e_\nu}+2\sqrt2\delta.
\tag{6.1}
\]
To carry (4.5) into the base requires control of
\[
\int_\Gamma\bigl(|h_\nu|+\sqrt{e_\nu}\bigr)\,dn
\tag{6.2}
\]
along normal arcs through a collar. The separator Jacobi form controls only the
single slice \(n=0\) and only in tangential capacity. The orbit equation is a
second-order trace relation, and \(|b|\le2\sqrt2\delta\) supplies no derivative
of the defect. Therefore the exact missing bridge is a tubular-collar
transport/regularity estimate using the remaining horizontal equations and
Codazzi--Bianchi structure. Any of the following would materially advance the
route:

1. a length-independent bound for (6.2) from the stable separator to the exact
   ends;
2. a collar \(L^2\) estimate for \(DdU\) plus a trace/transport theorem;
3. a new normal monotonicity combining the horizontal constraint with Maxwell
   transport;
4. a two-variable continuation/gluing construction extending the exact
   concentrated Koiso germs to the prescribed cylindrical ends.

Without such a result, (4.5) cannot replace \(Q_+\) in the resolvent theorem,
and the free-\(T^2\) symmetry class remains open.

## 7. Position within Yau 26

This Step strengthens only the negative, free-\(T^2\), two-ended connector
analysis. It does not construct a graph metric, exclude all free-\(T^2\)
connectors, cover non-free/non-OT/nonsymmetric metrics, address the positive
branch, or settle the full statement.

Peer positive-side messages #675--#676 independently reproduce A01's restricted
inter-node spectral numbers and clarify their scope. Same-chirality vanishing
holds in the implemented raw model by cancellations, not support alone;
diagonal balanced data have a positive inter-node margin, whereas another
balanced row may retain a kernel. Full Lyapunov--Schmidt self, complement,
frame, deformation, and remainder terms are not yet assembled, and even a
perturbative obstruction would not exclude unrelated Einstein metrics on the
smooth manifold.
