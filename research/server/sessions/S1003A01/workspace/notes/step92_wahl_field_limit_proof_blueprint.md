# Step 92 technical blueprint — fixed supplied Seiberg–Witten fields across a shrinking Wahl filler

This develops the selected route enough that the next Execute step can begin with an actual proof rather than a route label. It is conditional only where explicitly stated.

## 1. Geometric family and the fixed supplied structure

Let \((V,g)\) be a compact four-orbifold with one singular point of type
\[
\Gamma=\frac1{n^2}(1,n-1),
\]
and let \(M\) be its rational smoothing by the Ricci-flat Kähler ALE Wahl filler \(N=B_{n,1}\). Use the standard gluing of Lemma 86.S:
\[
g_\varepsilon=g\quad(r\ge2\rho),\qquad
 g_\varepsilon=\varepsilon^2h\quad(r\le\rho),
\qquad \rho=\varepsilon^{\tau/(\tau+2)},\quad\tau=4.
\]
On the transition annulus the rescaled \(C^2\) error is
\[
\delta_\varepsilon=O\!\left(\rho^2+(\varepsilon/\rho)^4\right)=O(\rho^2),
\]
so \(|\operatorname{Ric}(g_\varepsilon)|\le C\) there, and the changed region has volume \(O(\rho^4)\). In particular
\[
\int_{\{r<2\rho\}}(s_{g_\varepsilon}^-)^2=O(\rho^4).            \tag{1.1}
\]
The same conclusion holds with an outer radius \(R\to0\): for the explicit family,
\[
\lim_{R\downarrow0}\limsup_{\varepsilon\downarrow0}
\int_{\{r<R\}}(s_{g_\varepsilon}^-)^2=0.                         \tag{1.2}
\]

For each \(g_\varepsilon\), choose an unperturbed monopole from the finite signed blow-up family. Passing to a subsequence fixes one smooth spin\(^c\) structure \(\mathfrak s\) and its determinant class \(a\), while preserving
\[
(a^+_{g_\varepsilon})^2\ge A.                                   \tag{1.3}
\]
This finite-pigeonhole step is essential: the local limit is not built from an arbitrary extending structure.

Let \((A_\varepsilon,\Phi_\varepsilon)\) be corresponding solutions and put
\[
U_\varepsilon=|\Phi_\varepsilon|^2.
\]
With the corpus normalization,
\[
D_{A_\varepsilon}\Phi_\varepsilon=0,
\qquad |F^+_{A_\varepsilon}|^2=U_\varepsilon^2/8.                 \tag{1.4}
\]

## 2. Global energy compactness

The integrated Weitzenböck identity is
\[
4\int|\nabla_{A_\varepsilon}\Phi_\varepsilon|^2
+\int s_\varepsilon U_\varepsilon
+\int U_\varepsilon^2=0.                                        \tag{2.1}
\]
It implies
\[
\|U_\varepsilon\|_2\le\|s_\varepsilon^-\|_2,                   \tag{2.2}
\]
\[
4\int|\nabla_{A_\varepsilon}\Phi_\varepsilon|^2
\le\|s_\varepsilon^-\|_2\|U_\varepsilon\|_2,                  \tag{2.3}
\]
and, by harmonic projection and (1.3),
\[
\int U_\varepsilon^2
=8\int|F_A^+|^2
\ge32\pi^2(a^+_{g_\varepsilon})^2
\ge32\pi^2A.                                                    \tag{2.4}
\]
For the fixed class \(a\), Chern–Weil gives
\[
\int|F_A^-|^2=\int|F_A^+|^2-4\pi^2a^2,                          \tag{2.5}
\]
so \(\|F_A\|_2\), \(\|\Phi\|_4\), and \(\|\nabla_A\Phi\|_2\) are uniformly bounded.

On every compact set in \(V^{\rm reg}\), the metrics converge smoothly and ordinary abelian Coulomb gauge plus elliptic bootstrapping gives a subsequential smooth solution \((A_\infty,\Phi_\infty)\). The missing issue is to prevent all positive spinor mass in (2.4) from disappearing into the shrinking filler/neck.

## 3. Direct nonconcentration for the prescribed recovery family

The actual Lemma 86.S family gives more than scalar \(L^2\) control. On the transition annulus,
\[
|\operatorname{Ric}(g_\varepsilon)|
\le C\rho^{-2}\left[\rho^2+(\varepsilon/\rho)^4\right]
\le C,
\]
inside the scaled filler \(\operatorname{Ric}=0\), and outside lies the fixed orbifold metric. Hence
\[
\sup_M s^-_{g_\varepsilon}\le C_g.                              \tag{3.1a}
\]
The monopole maximum principle gives
\[
0\le U_\varepsilon\le C_g.                                     \tag{3.1b}
\]
For each fixed small orbifold radius \(R\), the filled ball has volume \(O(R^4)\), uniformly once \(\varepsilon\) is small. Therefore
\[
\boxed{
\limsup_{\varepsilon\downarrow0}
\int_{\{r<R\}}|\Phi_\varepsilon|^4\le C_gR^4.}                 \tag{3.1c}
\]
This proves full spinor and \(F_A^+\) tightness directly. It requires neither a global Sobolev constant nor a new capacity theorem, and it is the operative proof for WFL.

### Optional generalization under scalar \(L^2\) control only

For a real Lipschitz cutoff \(\eta\), multiply the pointwise Weitzenböck equation by \(\eta^2\) and integrate. Absorbing the cross term gives a universal constant \(C\) such that
\[
\int\eta^2U_\varepsilon^2
\le
C\int_{\operatorname{supp}\eta}s_\varepsilon^-U_\varepsilon
+C\int|d\eta|^2U_\varepsilon.                                   \tag{3.1}
\]
Hölder yields
\[
\int\eta^2U_\varepsilon^2
\le
C\|s_\varepsilon^-\|_{L^2(\operatorname{supp}\eta)}
 \|U_\varepsilon\|_2
+C\|d\eta\|_4^2\|U_\varepsilon\|_2.                            \tag{3.2}
\]
The second term is critical in dimension four.

Fix \(R>0\) and choose inner radius \(r_\varepsilon\) containing the filler and transition, with \(r_\varepsilon\asymp\rho\). On the orbifold annulus \(r_\varepsilon<r<R\), set
\[
\eta_\varepsilon(r)=
\begin{cases}
1,&r\le r_\varepsilon,\\[2mm]
\displaystyle\frac{\log(R/r)}{\log(R/r_\varepsilon)},
&r_\varepsilon<r<R,\\[2mm]
0,&r\ge R,
\end{cases}                                                     \tag{3.3}
\]
then smooth near the corners. On a cone \(dr^2+r^2g_{S^3/\Gamma}\),
\[
|d\eta_\varepsilon|=\frac1{r\log(R/r_\varepsilon)},
\]
so
\[
\int|d\eta_\varepsilon|^4
=\frac{\operatorname{Vol}(S^3/\Gamma)}{\log^4(R/r_\varepsilon)}
 \int_{r_\varepsilon}^R\frac{dr}{r}
=\frac{2\pi^2/|\Gamma|}{\log^3(R/r_\varepsilon)}.               \tag{3.4}
\]
The \(C^2\)-small gluing perturbation changes this by \(1+o(1)\). Therefore
\[
\|d\eta_\varepsilon\|_4^2=O\!\left(\log(R/r_\varepsilon)^{-3/2}\right)\to0. \tag{3.5}
\]
Combining (1.2), (2.2), and (3.2) gives only
\[
\lim_{R\downarrow0}\limsup_{\varepsilon\downarrow0}
\int_{\{r<r_\varepsilon\}}U_\varepsilon^2=0.                   \tag{3.6}
\]
The previously proposed complementary-cutoff sentence was false: it does not control the whole annular tail. Full tightness is already supplied by (3.1c). If one later needs a scalar-\(L^2\)-only theorem, use an *outward* logarithmic cutoff equal to one on \(r\le R\), zero on \(r\ge R_0=\sqrt{Rr_*}\), and then let \(R\downarrow0\); this combines local scalar \(L^2\) decay with the critical capacity \(O(\log(R_0/R)^{-3})\).

By (2.4) and (3.7), the regular-part limit obeys
\[
\int_{V^{\rm reg}}|\Phi_\infty|^4\ge32\pi^2A,                  \tag{3.8}
\]
so \(\Phi_\infty\not\equiv0\).

## 4. Removability and the actual lift

An explicit PPS integer character is not a prerequisite for the analytic theorem. Relative to a fixed canonical local lift, line twists are indexed by
\[
H^2(B\Gamma;\mathbb Z)\cong H^2(S^3/\Gamma;\mathbb Z)\cong\mathbb Z_{n^2},
\]
so the affine spin\(^c\) restriction is a bijection. A fixed marked smooth structure on the complement therefore determines a unique orbifold lift abstractly, denoted \(\operatorname{res}(\mathfrak s)\). For even \(n\), retain the full spin\(^c\) lift rather than only its determinant, because determinant doubling loses two-torsion information. Its explicit character may be computed in parallel.

The analytic extension should be proved on the punctured uniformizer \(B^4\setminus\{0\}\) after pulling back by \(\Gamma\). Equations (2.5) and (3.7) give finite connection curvature and spinor energy. Standard smooth point-removability arguments (Feehan–Leness proves the analogous smooth punctured-ball theorem for PU(2) monopoles) should then be applied equivariantly. Because the gauge group on the punctured quotient has disconnected sectors, one must record the limiting holonomy representation
\[
\rho_{\mathfrak s}:\Gamma\to U(1)                               \tag{4.1}
\]
rather than gauge it away. The extended bundle is precisely the orbifold line representation determined by \(\rho_{\mathfrak s}\).

The optional topology calculation needed for an explicit numerical character is:

1. choose one explicit odd-\(n\) PPS embedding \(B_{n,1}\subset V_{-4}\subset\#_4\overline{\mathbb{CP}}^2\);
2. give a Kirby/plumbing presentation of the boundary inclusion;
3. compute the restriction of the fixed affine spin\(^c\) set, including a reference structure;
4. distinguish line twists from determinant characters (factor two);
5. compare the result with (4.1).

The Step-104 formula \(j=\sum\varepsilon_iv_i\) is withdrawn and must not be reused.

## 5. Einstein consequence after WFL

Assume the orbifold metric is Einstein with \(s=-\lambda<0\). After extension, the maximum principle is global and gives
\[
0\le U\le\lambda,
\qquad
4\int|\nabla_A\Phi|^2=\int U(\lambda-U).                         \tag{5.1}
\]
Let \(\mathcal F=iF_A\) and decompose
\[
\mathcal F=2\pi h_a+d\alpha
\]
with \(h_a\) the orbifold harmonic representative of the identified determinant class. Hodge orthogonality gives
\[
\boxed{
\frac18\int U^2-4\pi^2\|a_g^+\|^2
=
\int|F_A^-|^2-4\pi^2\|a_g^-\|^2
=
\frac12\|d\alpha\|_2^2.}                                      \tag{5.2}
\]
For \(\psi=iF_A^+=iq(\Phi)\), the closed self-dual form identity is
\[
2\int\langle W^+\psi,\psi\rangle
=
\int|\nabla\psi|^2+\frac{s}{3}\int|\psi|^2
-
\int(|d\psi|^2+|d^*\psi|^2).                                   \tag{5.3}
\]
Equations (5.1)–(5.3), together with \(\delta W^+=0\), are the actual same-metric inputs for the next obstruction search. They are not themselves an exclusion theorem.

## 6. Proof dependencies and failure modes

The WFL route succeeds only if all of the following are established on the same family:

- a fixed genuinely supplied smooth spin\(^c\) structure;
- (3.7), not only weak complement convergence;
- finite-energy equivariant removability;
- marked limiting holonomy and orbifold lift;
- nonzero limit, from (2.4) plus tightness;
- a new implication from the Einstein–field identities beyond the already transferred scalar/mixed inequalities.

After finite-energy extension and real class identification, rational-ball/cone replacement preserves the determinant square \(a_V^2=a_M^2\). Direct \(F_A^+\)-energy convergence and Chern–Weil then imply full determinant-curvature energy convergence:
\[
\lim_\varepsilon\int_M|F_{A_\varepsilon}|^2
=\int_V|F_{A_\infty}|^2.
\]
Thus no hidden ASD **abelian** curvature energy remains in the filler or neck; this says nothing analogous about metric \(W^-\). The integrated Weitzenböck identity similarly gives equality of spinor-gradient energies once scalar and spinor mass converge.

Potential failure is informative. If equivariant removal or deck-action extension fails, the missing quotient gauge theorem is explicit. If removability holds but supplied lifts evade local isotropy restrictions, that closes the local-character entrance and directs the next work to (5.1)–(5.3). If the limit is reducible or its field degenerates despite the uniform mass lower bound and (3.1c), a normalization or compactness argument is wrong and must be repaired before any Einstein conclusion.
