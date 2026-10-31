# Step 94/99: Gate structure after trace-channel audit and high-dimensional note

Session `S0910A02`.  Step 94 began the three-gate framework; Steps 96--99 corrected it.  This file now records the current version.

## 1. Gate 1: local second obstruction vanishes on the kernel plane

From Ozuch/Biquard, the first obstruction at an \(A_1\) node is
\[
\lambda_k(\zeta^\pm)=c\langle R^\pm\zeta^\pm,\zeta_{(k)}^\pm\rangle.
\]
For the product orbifold \((S^2\times S^2)/\mathbb Z_2\), the corrected curvature block is
\[
R^+=R^- = \operatorname{diag}(\Lambda,0,0),
\]
so the admissible first-order EH periods lie in
\[
K^\pm=\ker R^\pm=\operatorname{span}\{e_2,e_3\}=\omega_1^{\pm\perp}.
\]
When the first obstruction vanishes, Ozuch/Biquard's local next obstruction has the form
\[
\mu_1=C\det\begin{pmatrix}R_{22}&R_{23}\\ R_{32}&R_{33}\end{pmatrix}.
\]
In a basis adapted to any \(\zeta\in K\), the relevant block contains one remaining kernel direction and one Kähler eigenline, hence has determinant zero.  The projected vector obstruction is zero by the corrected \(T^2\)-weight argument: the \(\beta=0\) subcircle acts with weight one on \(K\), and no homogeneous quadratic monomial \(z^a\bar z^b\) has degree two and weight one.

The old SO(2)-transitivity proof was invalid and must not be reused.  Gate 1 remains valid by rank-one curvature plus \(T^2\) parity.

## 2. Compatible Kähler smoothing calibration

The geometric calibration is now source-supported.  Biquard--Rollin write the local Kronheimer/deformation parameter as
\[
\zeta=(\zeta_r,\zeta_c)\in \mathfrak h_{\mathbb R}\oplus\mathfrak h_{\mathbb C},
\]
where \(\zeta_r\) records the local Kähler class.  Their Lemma 6 says root classes are Lagrangian when \(\zeta_r\in\ker\theta\) and holomorphic when \(\zeta_c\in\ker\theta\).  Thus compatible Kähler smoothings of an \(A_1\) node use periods in \(K=\omega^\perp\), whereas the holomorphic resolution direction is the Kähler eigenline.

OSS/Tian--Yau place the unique four-\(A_1\) degree-4 surface \((\mathbb P^1\times\mathbb P^1)/\mathbb Z_2\) at the Kähler--Einstein compactification boundary, with an open smooth degree-4 del Pezzo KE locus.  In a genuine variational LS reduction, the leading quartic obstruction for the compatible pattern must vanish on that open smoothing locus.  Step99's raw spectral audit agrees with this calibration: all physical same-chirality leading inter-node maps in the checked AB and AA/BB sectors vanish.

## 3. Gate 2: corrected finite-dimensional algebra

At node \(j\), the torus character is
\[
\theta_j=s_A^j\alpha+\varepsilon_js_B^j\beta,
\qquad
\sigma_j=\varepsilon_js_A^js_B^j.
\]
The \(\sigma\)-rule remains a useful selection rule for allowed traceless angular channels, but Step99 shows that actual physical leading coefficients have a stronger chirality structure:

- physical same-chirality inter-node maps \(B_{++}\) and \(B_{--}\) vanish in AB and AA/BB sectors at every checked rung;
- physical cross-chirality maps \(B_{+-}=B_{-+}\) carry the nonzero leading response;
- the AB sector is trace/isotropic only, while AA/BB tensor sectors are traceless.

The previous determinant-only comparison
\[
|q_{\rm diag}|\quad\text{vs}\quad |2q_{\rm adj}+q_{\rm diag}|
\]
was only a special equal-scale/equal-phase traceless slice and is no longer the Gate-3 criterion.  The correct linear algebra for a traceless block
\(L(z)=Pz+Q\bar z\) is
\[
\ker L\ne0 \iff |P|=|Q|.
\]
Both strict inequalities are invertible.  The old statement that \(|Q|>|P|\) implies solvability was false.

## 4. Gate 3: audited leading inter-node table

A02 Step99 parsed A01 Step98 data and independently reran selected A01 spectral computations.  The selected rerun exactly matched the stored data.  Current evidence files:

- A02 audit note: `Sessions/S0910A02/workspace/notes/step99_a01_trace_obstruction_audit.md`
- A02 audit data: `Sessions/S0910A02/workspace/data/step99_a01_trace_obstruction_audit.json`
- A02 selected rerun: `Sessions/S0910A02/workspace/data/step99_selected_spectral_recompute.json`
- A01 source data: `Sessions/S0910A01/workspace/data/step98_full_chirality_tensor_maps.json`, `Sessions/S0910A01/workspace/data/step96_kernel_plane_ab_map.json`

For a physical cross-chirality pair at receiver `NN` in the positive product mirror:

| source | pair type | AB trace \(c_0\) | isotropic eigen \(c_0/2\) | AA/BB traceless |
|---|---:|---:|---:|---:|
| `NS` | adjacent | \(+0.12576998928\) | \(+0.06288499464\) | Q-type \(0.0080049973185\) |
| `SN` | adjacent | \(+0.12576998928\) | \(+0.06288499464\) | P-type \(0.0080049973185\) |
| `SS` | diagonal | \(-0.070907042884\) | \(-0.035453521442\) | 0 |

Same-chirality entries vanish in the checked inter-node table.

### 4.1 Diagonal balanced pattern

For \(\varepsilon=(+,-,-,+)\), each receiver has two opposite-chirality adjacent sources and one same-chirality diagonal source.  The raw leading inter-node matrix has the form
\[
A_j^{\rm inter}=0.06288499464\,(u_1+u_2)I_K+T_j,
\qquad
\|T_j\|\le0.0080049973185\,(u_1+u_2),
\]
for scale-squares \(u_i=t_i^2>0\).  The margin
\[
0.0548799973215>0
\]
makes this uniformly positive definite/invertible for all positive scales and phases.  This is a strong leading local obstruction candidate for the diagonal-balanced row \(\#_3(S^2\times S^2)\).

### 4.2 Adjacent balanced pattern

For the adjacent balanced representative \(\varepsilon=(+,+,-,-)\), each receiver has one opposite-chirality adjacent source and one opposite-chirality diagonal source.  The scalar part is
\[
P=0.06288499464\,u_{\rm adj}-0.035453521442\,u_{\rm diag},
\]
with traceless bound \(|Q|\le0.0080049973185\,u_{\rm adj}\).  Hence \(|P|=|Q|\) is possible for positive ratios
\[
u_{\rm diag}/u_{\rm adj}\approx1.54794206864\quad\text{or}\quad1.99951906257,
\]
and \(P=0\) near \(1.77373056560\).  The leading table therefore does not uniformly obstruct the adjacent-balanced row; it may split the two balanced topologies.

## 5. What remains before any local theorem

The raw leading inter-node table becomes a theorem only after the following are supplied in one consistent gauge/normalization:

1. a slice-compatible variational or projected Lyapunov--Schmidt reduction;
2. self-interaction terms and proof of their chirality-pattern role;
3. complement Schur terms, frame/projector motion, and any product/global Einstein deformation coupling;
4. a relative expansion with remainder \(o(t^3)\), including possible logarithmic terms;
5. matching of the product-orbifold coordinates with the KE smoothing calibration.

Until then, the diagonal-balanced result is a verified leading inter-node obstruction candidate, not a complete desingularization obstruction theorem.

## 6. High-dimensional structural note

For \(n\ge5\), the project still lacks a certified closed manifold with no Einstein metric.  Known negative-Einstein nonexistence reservoirs are four-dimensional: they use the Einstein Chern--Gauss--Bonnet identity or \(\Lambda^2=\Lambda^+\oplus\Lambda^-\) gauge-theoretic tools.  These mechanisms do not directly transfer to higher dimensions.  Positive simplicial volume still obstructs nonnegative Einstein constants in all dimensions by Gromov's estimate \(\|M\|\le C(n)\operatorname{Vol}\) under \(\operatorname{Ric}\ge-(n-1)g\) and scaling any \(\operatorname{Ric}\ge0\) metric to volume zero.  This is a structural limitation of current methods, not evidence that Yau 26 is true in higher dimensions.
