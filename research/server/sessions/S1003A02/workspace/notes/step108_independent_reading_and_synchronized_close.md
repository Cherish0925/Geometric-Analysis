# Step 108 — Independent reading and synchronized close of the continuation

Session S1003A02, Agent4, Execute. This note independently reads the Step-107 Einstein-end results and records the final state of the owner-authorized Steps 101–108. Inputs: `step107_einstein_end_constraints_D4_object_and_specification.md`, both Step-106/107 scripts and JSON files, the complete TTCS-107 branch, Dai–Wei, the Step-105/106 charge notes, Foscolo/Franchetti and Akbulut topology sources, and A01 Step 93 §8 (after peer correction #894).

## 1. Independent reading of 107.A–C

### 1.1 Fixed-base fibred cusps

For
\[
g_0=dr^2+g_B+u^2\eta^2,\qquad u=e^{-\kappa r}f(b),
\]
the warped/O'Neill calculation gives, in horizontal lifts,
\[
\operatorname{Ric}_{g_0}(\partial_r,\partial_r)=-\kappa^2,
\qquad
\operatorname{Ric}_{g_0}(\partial_r,\widehat Y)=\kappa Y(\log f),
\]
and
\[
\operatorname{Ric}_{g_0}|_{TB}=K_Bg_B-f^{-1}\operatorname{Hess}_Bf+O(e^{-2\kappa r}).
\]
The connection curvature contributes only through an O'Neill tensor of size \(u|d\eta|\), hence quadratically at order \(e^{-2\kappa r}\). Therefore the proof needs only
\[
g-g_0=o(1),\qquad \operatorname{Ric}_g-\operatorname{Ric}_{g_0}=o(1)
\]
in \(g_0\)-orthonormal frames; relative \(C^2\) convergence is sufficient but stronger. If \(\operatorname{Ric}_g=\lambda g\), the three displayed components successively give
\[
\lambda=-\kappa^2,
\qquad df=0,
\qquad K_B=\lambda<0.
\]
Thus Theorem 107.A is correct at this scope. It excludes fixed-base circle-fibred Einstein cusps over \(S^2\), Euclidean \(T^2\), and the corresponding spherical/lens/prism or fixed-base Nil models. It does not touch real- or complex-hyperbolic cusps, in which base directions also shrink, nor any end for which the relative metric/Ricci asymptotics have not been established. Dai–Wei rescaled-bundle smoothness alone does not imply the needed relative derivative or Ricci convergence: a term \(xq(\theta)dy^2\) has a nondecaying derivative along the cusp-unit field \(x^{-1}\partial_\theta\).

Dai–Wei Theorems 3.5 and 5.1 give, with \(e\) oriented as \(\partial C\),
\[
c_+(C)=T_+(C)+e-3\operatorname{sign}e.
\]
The value is genus-independent because on a two-dimensional base only the degree-zero term of \(L(TB)\) enters. For \(C=D_e(\Sigma_g)\),
\[
c_+=4-4g+e.
\]
When \(g\ge2\), nonnegativity forces \(e\ge4g-4\) if \(e>0\), whereas the smooth-base SW adjunction inequality gives \(e\le2g-2\), provided the required blow-up basic class is supplied (\(b_+>1\), or separate chamber data). Hence the ordinary one-surface disc-bundle cap is excluded under that supply. Seifert-orbifold bases and multi-class caps are not covered.

### 1.2 Biaxial and triaxial spherical ends

The Step-107 symbolic output was rerun at Step 108; both `data/step106/D4_cap_ledger.json` and `data/step107/cusp_end_constraints.json` again have `all_ok=true`. The exact left-invariant formula
\[
r_i+r_j=\frac{4(x_i+x_j-x_k)}{x_ix_j}
\]
was checked. A curvature bound controls each logarithmic rate \(\lambda_i=a_i'/a_i\) by Riccati comparison and bounds the slice Ricci tensor through Gauss; ordering \(x_1\ge x_2\ge x_3\) then forces the second-largest scale to stay uniformly positive.

For a finite-volume biaxial end, \(v=a^2c\to0\), so \(a\ge b_0\) and \(c\to0\). The Hamiltonian constraint gives
\[
\lambda_a(\lambda_a+2\lambda_c)=\sigma_2
\ge \frac12s_\Sigma=\frac4{a^2}-\frac{c^2}{a^4}>0.
\]
If \(\lambda_a>0\), the volume rate \(2\lambda_a+\lambda_c\) is positive; if \(\lambda_a<0\), the product lower bound and bounded rates force \(a\) to decay exponentially, contradicting \(a\ge b_0\). Theorem 107.B is therefore correct for an end whose lift to \(S^3\) is biaxial (one should not assert that a global \(U(2)\) action descends through every nonnormal quotient).

For the triaxial case, \(\sigma_2\ge\delta>0\) implies \(H^2\ge3\sigma_2\). Finite volume rules out \(H>0\). If \(H<0\), every pair sum is negative; otherwise \(\sigma_2\le Hu-3u^2/4\le0\). Bounded logarithmic rates then bound every pair sum away from zero, causing every pair product \(a_ia_j\) to decay and contradicting the second-scale lower bound. Proposition 107.C is correct. Under \(\operatorname{Ric}=-3g\), the displayed anisotropy bound
\[
\limsup\frac{(a_1^2-a_2^2)^2}{a_1^2a_2^2a_3^2}<3
\]
is sufficient for \(\liminf\sigma_2>0\).

For the intended Einstein domains, finite tail \(L^2\)-curvature plus the quoted unit-scale Cheeger–Tian ε-regularity theorem supplies the curvature bound used above. No symmetry-free theorem follows from these calculations. The live question is whether every finite-volume negative-Einstein end with Hopf-collapsing \(S^3/\Gamma\) slices has infinite volume. In such a theorem the base \(S^2\) cannot merely shrink while curvature stays bounded; after 107.A, the unresolved geometry is a nonsymmetric, nonstandard/growing-base profile for which one must construct controlled level sets and their second fundamental forms. A positive answer would void every Hopf-cap configuration.

## 2. Independent reading of the D4 object

The rank-four D4 ALF instanton has \(H_2=D_4\), form \(-D_4\), \((\chi,\tau)=(5,-4)\), and end \(S^3/D_2^*=S^3/Q_8\). In the hyperkähler orientation its region-outward charge is \((-2,2)\), so
\[
C_+=0,
\qquad C_-=20,
\qquad \int|W^-|^2=40\pi^2.
\]
The real rank-two disc bundle \(W\to\mathbb{RP}^2\) has the same boundary, \(\pi_1W=\mathbb Z_2\), \(H_2(W)=0\), and double cover the Euler-\(-4\) disc bundle over \(S^2\). The boundary map \(Q_8\to\mathbb Z_2\) is onto. Hence
\[
M_4=N_{D4,\mathrm{trunc}}\cup W
\]
is simply connected. Mayer–Vietoris supplies the index-two extension of \(-D_4\); independently, \(\chi(M_4)=6\), \(\tau(M_4)=-4\), and Donaldson gives \(Q_{M_4}\cong-I_4\). Freedman therefore makes \(M_4\) homeomorphic to \(\#4\overline{\mathbb{CP}}^2\). Its diffeomorphism type is open. The cone-filled space \(W\cup c(S^3/Q_8)\) is simply connected with \(H_2=\mathbb Z_2\), hence a rational homology four-sphere but not a homotopy sphere. Calling \(M_4\) its minimal D4 resolution additionally requires a relative identification of the ALF truncation with the standard D4 plumbing.

Thus the D4 proposal has three genuinely missing pieces: (D4-1) the relative smooth/Kirby identification; (D4-2) a transition on \(W\setminus B^4\) matching the ALF and outer Hopf collars with vanishing full curvature energy; (D4-3) an admissible negative-Einstein domain. The two-chirality ledger permits D4-2 but does not construct it. Even all three would still require a global gluing theorem with defect, scalar-variance, collar-scale and volume control. D4-1 is worth pursuing only while the Einstein-side Hopf end remains possible.

## 3. A01 Step 93: verified scope and new Wahl information

A01 §8 was read after correction #894. Theorem 93.A is sound under explicit finite metric-wise supply (S): the shrinking-Wahl-filler solutions converge to an orbifold SW solution; abelian removability uses \(\Phi\in L^\infty\), \(F_A\in L^2\), the determinant gauge \(e^{if/2}\), and a bootstrap through \(W^{1,p}\), not a false \(W^{2,4}\subset C^{1,\alpha}\) embedding. For \(b_+>1\), the signed canonical blow-up classes supply (S); \(b_+=1\) needs chamber input. Theorem 93.A promotes Question 105.M only at this explicit scope.

Lemma 93.I transfers extendible Dirac indices. The finite script was numerical, while §8 gives an exact all-\(n\) proof that the local Kawasaki correction equals the canonical value exactly for \(m\in n\mathbb Z/n^2\).

Proposition 93.Y is an existential marked complex realization: choose the PPS sphere holomorphic from the outset. It covers odd \(n\ge3\) through the \((-4)\)-curve and \(n=2\) through the \((-3)\)-curve, not arbitrary embeddings and not the even \(n\ge4\) route. The resulting Wahl orbifold is projective, of general type, and nonminimal with non-nef canonical divisor. This is a structural self-similarity with Problem 1, not an equivalence of smooth and orbifold Einstein existence. What transfers is \(a^2\), \(T_+^{\rm orb}=A-k\), extendible Dirac indices, metric-wise supply, and scalar/\(W^+\) LeBrun bounds. The opposite chirality, local characters, forced zeros, full SW invariants, and moduli geometry do not transfer.

For \(n\ge3\), the forced-zero sign subfamily is closed under complementation, so its average positive square remains at least \(A\). Under simultaneous supply, WFL selects a limit with \(\Phi(p)=\nabla\Phi(p)=0\) and \(\int U^2\ge32\pi^2A\); consequently
\[
\int_V(s^-)^2>32\pi^2A
\]
for every orbifold metric in the marked family. This strictness has no uniform size. The quantitative unknown is the dimensionless regularity scale \(\lambda r_0^2\) at the Wahl point: a marked forced character may migrate into shrinking Ricci-flat bubbles while the global defect vanishes. A marked-character bubble tree is therefore the sharpened analytic target on the Wahl branch.

No complex realization of the \(D_{\ge6}\) prism candidate is established in this corpus.

## 4. Synchronized mathematical state

For \(M=X\#k\overline{\mathbb{CP}}^2\), \(0<k<A/3\), the alternatives remain undecided:

1. \(\alpha(M)>0\);
2. \(\alpha(M)=0\) without attainment, through one of the three singular/collapse mechanisms below;
3. a smooth negative Einstein metric, which attains \(\alpha=0\).

The three mechanisms in (2) now have exact, unequal statuses.

- **Wahl.** Actual marked complex orbifolds exist. The standard scalar/\(W^+\) package sees the same threshold as on the smoothing; WFL and index transfer now have precise supply. Einstein existence remains open. Forced-zero classes give strict scalar inequality but no uniform gap; the next analytic object is a marked-character bubble tree or a construction showing scale collapse.
- **\(D_{\ge6}\) prism.** Only necessary lattice, filler and curvature data are available. No compatible global complement, complex realization, or Einstein orbifold has been constructed.
- **Collapsed/cusp Einstein domain.** The cap theorem holds only under (E). It gives
  \[
  C_+(\Omega)=A-k-\sum c_j,
\qquad c_j\ge0,
\qquad 9k+8\sum c_j\le3A.
  \]
  Under Dai–Wei end asymptotics the charges are topological. The controlled chirality sees a removed region exactly through its \(C_+\)-charge; topology can hide from it only by paying in \(C_-\) (the four-class cap has \((c_+,c_-)=(0,20)\)); the Einstein-side equations then determine which ends can host the cap. Fixed-base fibred, biaxial, and small-anisotropy spherical ends are excluded at the scopes above. Symmetry-free Hopf ends, shrinking-base cusps, hyperbolic-base multi-class caps, and extraction of (E) remain unresolved. Extraction of (E) is retained as a named hypothesis, not promoted to a theorem.

The first next moves are therefore: prove the symmetry-free Hopf-end volume-growth theorem; attack Wahl Einstein existence through the marked forced-character scale/bubble tree and constructions; determine whether the \(D_{\ge6}\) prism data admit a complex or otherwise geometric realization; pursue D4 Kirby calculus only if the Hopf host survives; and develop a same-metric smooth relation capable of detecting zero-\(C_+\)/nonzero-\(C_-\) regions while respecting the certified Burns cell and the known coercivity-degenerate loci.

This continuation produced a common chiral mechanism and precise explicit objects, but it did not decide the fixed-topology trichotomy, produce a zero-gap sequence, or construct/exclude a smooth negative Einstein metric.