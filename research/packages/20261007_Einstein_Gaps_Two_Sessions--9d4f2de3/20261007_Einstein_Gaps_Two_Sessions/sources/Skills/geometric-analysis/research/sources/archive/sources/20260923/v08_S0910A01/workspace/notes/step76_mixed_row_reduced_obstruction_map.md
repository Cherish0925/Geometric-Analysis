# Step 76 mixed-row reduced obstruction map — corrected by Step 77

Session `S0910A01`. Original Step 76 note superseded in its kernel/global-system conclusions by Step 77.

## Corrected status

The local rank-one curvature facts from Step 76 remain useful:

- For the product orbifold
  \[
  \mathcal O=(S^2\times S^2)/\langle(r_\pi,r_\pi)\rangle,
  \qquad \operatorname{Ric}(g_o)=\Lambda g_o>0,
  \]
  each of the four fixed points is an `A_1` singularity.
- In standard self-dual/anti-self-dual bases,
  \[
  R^+(p_j)=R^-(p_j)=\operatorname{diag}(\Lambda,0,0),
  \qquad
  W^\pm=\operatorname{diag}(2\Lambda/3,-\Lambda/3,-\Lambda/3).
  \]
- Hence `ker R^\pm` is two-dimensional.  If the EH direction satisfies
  `\phi_j\in\ker R^{\epsilon_j}`, Ozuch's first obstructions satisfy
  \[
  \lambda_k^j(\phi_j,0)=0\qquad(k=1,2,3).
  \]
- Ozuch's displayed second-obstruction determinant formula proves, for the bare product block in the adapted basis,
  \[
  \mu_1^j=C\det\begin{pmatrix}R_{22}&R_{23}\\R_{32}&R_{33}\end{pmatrix}=0.
  \]

The following Step 76 statements are withdrawn:

1. `\mathbf O(g_o)=0` for Ozuch's full operator.
2. The conclusion that the global `\nu_l` system is empty.
3. The conclusion that all second-order obstructions vanish and only higher-order convergence remains.
4. The suggestion that Ozuch Question 0.8 is a positive-Einstein sufficiency problem.
5. The topology statement `M=#_r(S^2\times S^2)` for `r=1,...,4`.

## Correct kernel statement

Ozuch Definition 1.8 defines
\[
\mathbf O(g)=\ker_{L^2}\left(\frac12\nabla^*\nabla-\mathring R\right)
\]
on all symmetric two-tensors.  It is not the same as the TT kernel.  On the quotient, the axial first harmonics `u_1,u_2` on the two spheres descend under the half-turn and satisfy
\[
\Delta u_i=2\Lambda u_i.
\]
Since each factor metric is parallel and `\mathring R(u_i g_j)=\Lambda u_i g_j`,
\[
P(u_i g_j)=0,
\qquad i,j\in\{1,2\}.
\]
Thus the full Ozuch kernel contains the four scalar-sector modes
\[
u_1g_1,
\quad u_1g_2,
\quad u_2g_1,
\quad u_2g_2.
\]
The zero TT kernel and the nonzero eigenvalue of the shape tensor `g_1-g_2` do not remove these modes.  A geometric Bianchi/diffeomorphism slice may remove some or all of their effect, but then the sliced equations and compatibility conditions must be derived explicitly.

## Correct obstruction problem

The productive object is the coupled, sliced finite-dimensional map.  For an exact nearby Einstein metric Ozuch's estimate gives projected equations
\[
t_j\lambda_k^j(\phi_j,v)+t_j^2\mu_k^j(\phi_j,v)=O(t_{\max}^{5/2}),
\qquad
\nu_l(t\phi,v)=O(t_{\max}^{5/2}).
\]
These are not automatically a full residual bound.  The full construction requires:

1. the finite-dimensional projection equations;
2. a precise slice or inclusion of the four scalar-sector `v_l` variables;
3. the projected residual estimate on the complement;
4. a uniform inverse estimate and nonlinear remainder control.

The crucial interaction is the singular-subtracted Green response.  A bubble at node `j` contributes the `r^{-4}` quadrupole `H^4(\zeta_j)`.  Solving the orbifold equation with the chosen projection and subtracting the singular part produces, at another node `i`, a regular expansion
\[
\bar h_j^4=H_{ij,0}+H_{ij,2}+O(r_i^4),
\]
and `H_{ij,2}` modifies the curvature block entering `\lambda` and `\mu` at node `i`.  Hence the bare rank-one matrix need not remain rank one after inter-node corrections.  This is the main mixed-row computation.

The determinant formula establishes `\mu_1=0` for the bare product block only.  It does not establish `\mu_2=\mu_3=0` until the relevant Biq16/Ozuch formulas have been derived for the corrected effective jet.

## Correct topology table

The four-node fillings have `b_2=6`.  With `k` positive EH kernels, the table from `20260912.tex` is:
\[
\begin{array}{c|c}
k&\text{oriented smooth type}\\\hline
0&\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2\\
1&2\mathbb{CP}^2\#4\overline{\mathbb{CP}}{}^2\\
2\text{ adjacent}&3\mathbb{CP}^2\#3\overline{\mathbb{CP}}{}^2\\
2\text{ opposite}&\#3(S^2\times S^2)\\
3&4\mathbb{CP}^2\#2\overline{\mathbb{CP}}{}^2\\
4&5\mathbb{CP}^2\#\overline{\mathbb{CP}}{}^2.
\end{array}
\]
The mixed rows are positive-branch stress families; resolving their nearby Einstein gluing does not settle the full sign-unrestricted Yau--26 proposition.

## Replacement evidence

Use the Step 77 repair note and data for the corrected state:

- `workspace/notes/step77_mixed_row_obstruction_repair.md`
- `workspace/data/step77_scalar_kernel_and_pairing.json`
- `workspace/data/step77_slice_decomposition_verify.json`
- `workspace/scripts/step77_scalar_kernel_and_pairing.py`
- `workspace/scripts/step77_slice_decomposition_verify.py`

Relevant source anchors in Ozuch's paper: Definition 1.8 (Knowledge lines 243--250), global `\nu_l` construction (lines 625--666), projected estimate (lines 770--795), and Question 0.8 (lines 150--154).
