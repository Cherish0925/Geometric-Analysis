# Step 16 — Joint diagonal dual calibration and exact ACH-bolt chirality

Normalization throughout the cell calculation is \(\operatorname{Ric}_{CH}=-6g\), and
\(P/(8\pi^2)=\frac14\int W|\operatorname{Ric}^{\circ}|^2dt\) for diagonal Bianchi IX,
where \(W=a_1a_2a_3\).

## 1. The full diagonal Ricci variable

For the spin variables
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\qquad
H_i=u_i+\frac12u_ju_k,
\]
put
\[
z_i=\frac{\dot u_i}{a_i}-\frac{2H_i}{a_ja_k}.
\]
The Cartan calculation of Steps 6--7 says
\[
|\operatorname{Ric}^{\circ}|^2=|z|^2.
\]
If \(e_0,e_1,e_2,e_3\) are the diagonal entries of \(\operatorname{Ric}^{\circ}\), then
\[
z_i=-(e_0+e_i).
\]
Thus the three-vector \(z\), not a single Ricci difference, is the complete trace-free diagonal
Ricci variable.  For every test field \(\beta(t)\in\mathbb R^3\),
\[
\boxed{\quad \frac{P}{8\pi^2}\ge
 \frac12\int Wz\cdot\beta\,dt-\frac14\int W|\beta|^2dt.\quad} \tag{1}
\]
For a finite family \(B_A\), the optimized right side is
\[
\frac14m^TG^{-1}m,\qquad
m_A=\int Wz\cdot B_A,
\quad G_{AB}=\int WB_A\cdot B_B.
\]
The full Gram matrix is used once, so correlated Green and spin directions are not added as
independent energy contributions.  `proofs/JointDualGram.lean` checks the scalar/eigenchannel
square completion, and `proofs/joint-dual-gram-check.json` dependency-checks the named theorem.

`scripts/check_joint_dual_identities.py` checks, in the Cartan algebra, the spin boundary
identity for
\[
\Phi=C-u_2^2,
\qquad \nabla_u\Phi=(2H_1,u_1u_3,2H_3):
\]
\[
\int Wz\cdot\frac{\nabla_u\Phi}{a}\,dt
 =\Phi(T)-\Phi(0)-2\int\sum_i\frac{(\partial_i\Phi)H_i}{\lambda_i}\,dt. \tag{2}
\]
For an \(O(-1)\) cell, \(\Phi(0)=1\), \(\Phi(T)=0\).  The correct test field in (1) is
\[
 B_i^\Phi=\frac{a_i}{W}\,\partial_{u_i}\Phi
          =\frac{\partial_{u_i}\Phi}{a_ja_k},
\]
because then \(Wz\cdot B^\Phi=\sum_i(\partial_i\Phi)a_iz_i\).  This field is weighted-\(L^2\)
regular at the collapsing bolt.  The first implementation incorrectly used
\((\partial_i\Phi)/a_i\) and then removed the fixed boundary term from the Gram moment.  TTCS
caught both errors; the script and all data below were regenerated with the correct field and the
full raw moment.  The two orbit-shape equations provide the constant and radial Green fields in
the two independent traceless diagonal directions.  Their fixed bolt fluxes and potential terms
are what must eventually make the moments in (1) competitor-independent.

## 2. Joint Gram experiment on the certified area branch

`scripts/joint_dual_calibration.py` evaluates the finite basis
\[
\{1,G\}\otimes\{(-1,0,1),(1,-1,0)\}
\quad\text{together with}\quad a^{-1}\nabla_u\Phi.
\]
The tensor directions are converted to the sign convention of the shape equations before
forming the Gram matrix.  The resulting numbers are numerical dual lower bounds for the
**fixed witnesses**.  They are not yet uniform lower bounds over all cells, because the
potential moments and Gram entries still depend on the metric.

Canonical table: `data/joint_dual/summary.csv`.

| \(x_0\) | \(P/(8\pi^2)\) | two Green shape fields | joint Green+spin | joint share of \(P\) |
|---:|---:|---:|---:|---:|
| .003 | .999795 | .506490 | .999523 | .99973 |
| .01 | .998700 | .581363 | .996023 | .99732 |
| .015 | .997766 | .606897 | .992008 | .99423 |
| .02 | .996937 | .623521 | .987480 | .99051 |
| .03 | .995848 | .643403 | .977335 | .98141 |
| .05 | .996753 | .658934 | .956338 | .95945 |
| .10 | 1.016431 | .666364 | .918929 | .90407 |

The corrected result is much stronger than the preliminary implementation.  At the inexpensive
\(x_0=.03\) cell the two shape Green fields see \(64.6\%\), while the single correct spin field
already sees \(97.2\%\); optimizing all five fields together sees \(98.14\%\) of \(P\).  As
\(x_0\to0\), the spin projection approaches the complete cost (joint share \(99.97\%\) at
\(.003\)), exactly as expected from the whole-AE/Chern--Weil calibration.  Its share decreases
for large bolts, while the two Green channels grow relatively more important.  This is the sought
complementarity rather than double counting.

A representation test in `scripts/full_diagonal_projection.py` multiplied the corrected geometric
directions by cubic polynomials in normalized geodesic radius.  It spans \(99.969\%\) of \(P\)
at \(x_0=.03\), but the Gram matrix is poorly conditioned and its localized moments are not fixed
by the two elementary Green identities.  The remaining difficulty is therefore no longer finding
a tensor direction that represents the core energy: it is converting the nearly complete spin
projection into a competitor-independent moment estimate and controlling localized corrections.

## 3. Scalar-channel cancellation is an escape only at enormous full cost

`scripts/test_Ezero_reconstruction.py` freezes \(F,G\) of the \(x_0=.03,X=64\) witness and
varies only \(w\), trying to suppress one Ricci-difference energy.  Unregularized optimization
reduces that channel from \(0.13210\) to \(0.00632\), but drives the coefficients to size
hundreds and raises \(P/(8\pi^2)\) to \(2.46\times10^5\).  With quadratic coefficient penalties
\(\mu=10^{-1},10^{-2},10^{-3},10^{-4}\), the outcomes are:
\[
(E\text{-cost},P)=(.13198,.99586),(.13094,.99721),(.12218,1.10475),(.08775,4.77986).
\]
Files: `data/joint_dual/Ezero_mu*.json` and `Ezero_x003_X64.json`.

So a single shape channel can be nearly cancelled as an underdetermined scalar equation, but in
this controlled slice doing so transfers large cost to the other shape/radial components.  This
supports the Strategist's warning: failure of one scalar observable does not identify a genuine
low-energy escape.  A lower argument must control the full three-vector \(z\).

## 4. What the joint experiment changes for a lower theorem

The finite Gram representation suggests a concrete middle-scale theorem target.  On
\(b\in[b_-,b_+]\) and for a controlled class of diagonal cells, seek transport identities for
both shape Green fields and one corrected spin field such that:

1. their moment vector is separated from zero by bolt flux plus the relative charge;
2. the potential terms can be bounded in terms of the same moment vector and geometric state,
   without assuming the desired Ricci estimate;
3. the Gram matrix has a uniform upper spectral bound;
4. localized residual directions are absorbed by a positive spin/Hamilton--Jacobi remainder.

The corrected five-field basis is already numerically near-sharp on the observed interior cell:
\(0.977335\) against \(P=0.995848\), and the spin direction alone gives \(0.967757\).  Thus a
competitor-independent control of the full spin moment and norm could produce a quantitatively
serious diagonal lower bound.  Near equality is not automatic: the moment contains the nonlinear
potential integral in (2), and the test norm is metric-dependent.  The remaining \(1.86\%\) at
\(x_0=.03\) can be represented by localized corrections, but deriving their moments from geometry
without assuming the desired estimate is the actual problem.

For \(b\to0\), the data are consistent with a two-scale dichotomy rather than an automatic AE
limit: either the marked rescaled core has controlled end transgression and the whole-AE identity
pays the charge, or a fixed CH-scale outer transition retains the missing charge/energy.  The
large-b side likewise still needs a genuine penalty estimate; numerical growth alone is not one.

## 5. Exact bolt chirality for the peer's validated ACH Einstein filling

Peer S1003A02 proved a complete real-analytic \(\operatorname{Ric}=-6g\) ACH filling at
\(b=4/5\).  Its validated Fuchsian series gives, in their bolt-slot-3 convention,
\[
a_1=a_2=\frac45+\frac{49}{20}t^2+O(t^4),\qquad
 a_3=t-\frac{25}{24}t^3+O(t^5).
\]
`scripts/ach_bolt_weyl_exact.py` inserts this exact two-jet into the Cartan curvature operator and
projects to the two chiral \(\Lambda^2\) blocks used by `o11_rotated_cell.py`.  At the bolt,
\[
s=-24,
\]
\[
W_A=\operatorname{diag}\!\left(-\frac{41}{16},-\frac{41}{16},\frac{41}{8}\right),
\quad |W_A|_{op}^2=\frac{5043}{128},
\]
\[
W_B=\operatorname{diag}\!\left(-\frac{91}{16},-\frac{91}{16},\frac{91}{8}\right),
\quad |W_B|_{op}^2=\frac{24843}{128}.
\]
Both halves are nonzero exactly.  Therefore the validated ACH Einstein metric is neither
self-dual nor anti-self-dual.  The first exact script version accidentally reused the symbol `b`
for the bolt radius and Cartan radius variable, causing sequential SymPy substitution to corrupt
the inserted two-jet; TTCS identified the inconsistency.  The repaired script uses a `Dummy` bolt
radius and now agrees with `scripts/ach_bolt_weyl_coordinate_check.py`, which gives chiral operator
norms tending to \(39.3985\) and \(194.083\).  In the four-index tensor convention these norms are
four times larger.  Each block has the Kähler-type eigenvalue multiplicity \((2,1)\), so the
peer's proposed exclusion by "three distinct eigenvalues" does not apply to the corrected blocks.
(Correction, Step 17.)  A Kähler structure is nevertheless excluded for either orientation by the
norm: the metric is Einstein, so a compatible Kähler structure would make it Kähler--Einstein,
and then the Kähler-side Weyl block is \(\operatorname{diag}(s/6,-s/12,-s/12)=(-4,2,2)\) with
\(|W|^2_{op}=s^2/24=24\).  The two blocks have norms \(5043/128\approx39.40\) and
\(24843/128\approx194.08\), and neither spectrum is \(\pm(-4,2,2)\).  Correction sent to the peer
as message 771.  The labels \(A,B\) must be
mapped to \(W^+,W^-\) according to orientation before assigning a sign.

## 6. Status

The certified cell upper theorem remains the current global construction result; this step did
not treat another decimal as the main goal.  The new substance is a complete three-component
diagonal Ricci representation, a non-double-counted finite Gram combination of the two shape
transports with the spin charge direction, an explicit demonstration of what remains invisible,
and an exact chirality conclusion for the independently validated ACH Einstein filling.
The diagonal lower theory, small-b outer-transition alternative, large-b penalty, unrestricted
cell infimum, and mixed blow-up--handle costs remain open.
