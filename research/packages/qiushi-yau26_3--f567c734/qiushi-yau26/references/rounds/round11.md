# Round 11: closed near-Einstein manifolds beyond surface bundles

21 September 2026.

The main advance is a construction on fixed **closed** four-manifolds,
not another noncompact connector. Shrinking a boundary circle allows an
integral shear to survive topologically while its full Ricci error tends
to zero. A separate long collar absorbs arbitrary mapping-class
holonomy. For explicit cyclic gluings, the resulting manifold is not any
oriented surface bundle over a surface, and no finite cover is Kähler.

These statements concern the same constructed smooth objects. They do
not yet exclude arbitrary negative Einstein metrics on them.

## 1. The closed metric theorem

Take finitely many blocks \(B_v\times F_v\), where \(B_v\) are
compact surfaces with boundary and negative Euler characteristic, and
\(F_v\) are closed surfaces of the same genus at least two. Pair their
boundary components by fixed maps
\[
       (\phi,x)\longmapsto(-\phi+u_e(x),f_e(x)).           \tag{1}
\]
Here \(u_e\) is circle valued and \(f_e\) is an arbitrary
orientation-preserving diffeomorphism; neither finite-order monodromy
nor vanishing integral shear is assumed. Let \(M\) be the closed
smooth assembly.

The [construction proof](round11_closed_gluing.md) gives metrics
\(G_\ell\), \(\ell\downarrow0\), with
\[
 \boxed{\quad
 \|G_\ell^{-1}\operatorname{Ric}_{G_\ell}+3I\|_\infty
       \le C\bigl(|\log\ell|^{-1}+\ell\bigr)\longrightarrow0,
 \qquad
 \operatorname{Vol}(G_\ell)=\frac{4\pi^2}{9}\chi(M).
 \quad}                                                   \tag{2}
\]
All fixed-order curvature derivatives are uniformly bounded. More
strongly, the positive-order derivatives tend uniformly to zero, and
\[
       -3-o(1)\le\operatorname{sec}_{G_\ell}\le o(1).     \tag{3}
\]
The local curvature approaches that of
\(\mathbb H^2_{-3}\times\mathbb H^2_{-3}\), but neither diameter
nor injectivity radius stays controlled. The smooth topology is fixed
throughout.

There are two disjoint interpolation regions:

1. A hyperbolic collar of length comparable to \(|\log\ell|\)
   carries a slow path of hyperbolic fibre metrics from \(h_v\) to
   \(f_e^*h_w\). Its complete Gauss--Codazzi defect is
   \(O(|\log\ell|^{-1})\), including mixed and trace blocks.
2. A fixed-width throat, with circle radius \(a=O(\ell)\), carries
   the connection interpolation \(d\phi+z(t)\beta_e\), where
   \(\beta_e\) is a fixed integral closed one-form. The full mixed
   Ricci terms are \(O(a)\), and the remaining terms are \(O(a^2)\).

The first operation handles mapping classes; the second handles an
integral topological shear. Their separation is why the error bound
controls the actual closed metric, not just independent local models.
Circle-valued gluing maps perform the endpoint identifications, so no
global primitive of \(\beta_e\) is assumed.

An area-preserving choice of the hyperbolic paths also makes these
metrics almost Kähler in both orientations. The forms on each collar
are
\[
 \Omega_\pm=a(t)\,dt\wedge(d\phi+z(t)\beta_e)\pm\omega_F.
\]
The proof includes an endpoint-fixed Moser construction and the actual
global gluing of these forms.

After scaling \(\widehat G_\ell=3G_\ell\), (2) is exactly the
negative normalized Yau26 input:
\[
       \delta_-(\widehat G_\ell)\longrightarrow0.
\]

## 2. A concrete family outside the previous surface-bundle class

Self-glue the two boundaries of
\(F_{h,2}\times\Sigma_g\), with \(h\ge1\), \(g\ge2\),
by (1). Denote the result by \(M(h,g;u,f)\).

The [topology proof](round11_graph_topology.md) establishes
asphericity and
\[
       \chi(M)=4h(g-1)>0,\qquad\tau(M)=0.                \tag{4}
\]
If \(u\ne0\) and \([f]\) has infinite mapping-class order, its
fundamental group is not an extension of a closed hyperbolic surface
group by another. Positive Euler characteristic and asphericity then
exclude the remaining genera. Thus **there is no oriented closed
surface-bundle structure on \(M\)**, not merely no preferred
projection.

For the proof, the vertex group is
\(A\times\Gamma=\pi_1(F_{h,2})\times\pi_1(\Sigma_g)\).
In any putative quotient surface group, the commuting images of its
two nonabelian factors force one factor to vanish. Killing \(\Gamma\)
puts a nonzero centralizing boundary power into the proposed surface
kernel, impossible. Killing \(A\) makes \(\Gamma\) inject into the
quotient with finite index, forcing a power of \(f_*\) to be inner,
also impossible.

The [virtual Kähler proof](round11_kahler.md) requires only \(u\ne0\).
The integral shear forces the Bass--Serre action kernel into
\(\Gamma\cap\ker u\). Gromov--Schoen factorization for a
Kähler group acting on this tree would give a finitely generated normal
kernel there. Surface-group normal-subgroup theory makes this kernel
trivial, after which the resulting Fuchsian group would have to contain
\(\mathbb Z^2\). The contradiction survives every finite cover.
The exact tree theorem used is stated in
[Nicolás, Theorem 25 and Lemma 24](https://arxiv.org/pdf/2102.01128).

A fully specified example has \(h=1\), \(g=2\), primitive nonzero
\(u\), and a mapping class supported on two once-holed tori with
homology action
\[
 f_*=\operatorname{diag}(H,H),\qquad
 H=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]
Its integral homology calculation gives
\[
 \boxed{\quad
 \chi=4,\quad\tau=0,\quad b_1=4,\quad b_2=10,
 \quad b_2^+=b_2^-=5.
 \quad}                                                  \tag{5}
\]
Thus neither the nonbundle result nor the Kähler obstruction is an
odd-Betti-number observation. A second, single-Dehn-twist example has
\(b_1=7\). Both integer presentations are independently reproducible.

The metric construction and the group obstruction exploit the same
operation in different ways: collapse suppresses the shear's analytic
cost, while its integral cohomology class remains visible to the group.

## 3. Exact variational quantities and the remaining Einstein question

For the self-glued family, the symplectic structures and \(b_2^+>1\)
give the usual canonical monopole class. The construction realizes the
sharp lower bounds supplied by that class. The full proofs and norm
conventions are in [the variational note](round11_variational.md):
\[
 \begin{aligned}
 \sigma(M)&=-8\pi\sqrt{\chi(M)},\\
 \inf_{\operatorname{Ric}\ge-g}\operatorname{Vol}(M,g)
       &=4\pi^2\chi(M),\\
 \inf_g\int_Ms_g^2\,d\mu_g&=64\pi^2\chi(M),\\
 \inf_g\int_M|\operatorname{Ric}_g|^2\,d\mu_g
       &=16\pi^2\chi(M).
 \end{aligned}                                          \tag{6}
\]
For \(u\ne0\), none of these extrema is attained: equality in the
relevant monopole scalar estimate would yield a Kähler metric. For
\(\sigma(M)\), this means no conformal class realizes the Yamabe
invariant, not that a conformal class lacks its own Yamabe metric.

The full curvature functional behaves differently. With the full
four-index tensor norm,
\[
 \boxed{\quad
 \inf_g\int_M|\operatorname{Rm}_g|^2\,d\mu_g
        =32\pi^2\chi(M).
 \quad}                                                  \tag{7}
\]
Chern--Gauss--Bonnet makes attainment of (7) equivalent to existence
of an Einstein metric. **That attainment question remains open here.**
Nonattainment of the other four extrema does not answer it.

The manifold's group already excludes positive Einstein and Ricci-flat
metrics. The virtual Kähler theorem excludes Kähler--Einstein metrics,
including those appearing only after finite cover, and also excludes
the familiar product-symmetric alternatives. What remains is a genuinely
non-Kähler negative Einstein metric with no obligation to resemble our
sequence or preserve its decomposition.

## 4. A separate differential advance on the earlier gauge route

[The rank-one note](round11_rankone.md) handles the endpoint where the
previous determinant obstruction vanished. For an everywhere rank-one
Dirac field, let \(b\) be the second fundamental form of its target
image line and \(K\) the complementary line. The complementary
equations imply
\[
 2\pi c_1(K)\cdot[\omega]
 =-\tfrac12\int |b|^2\langle\omega_M,\omega\rangle
   +\int i\mathcal R_{KK}\wedge\omega.                  \tag{8}
\]
Here \(\omega\) is closed self-dual of norm \(\sqrt2\),
\(\omega_M\) is the form of the source spinor line, and
\(\mathcal R\) is the actual curvature-equation residual. No
closedness of \(\omega_M\) is assumed.

On the specified earlier slow-twist metrics, (8) yields the sharp bound
\[
        2\le\|b\|_{2,\mathrm{av}}^2+
                    \|\mathcal R\|_{2,\mathrm{av}}       \tag{9}
\]
under the stated trivial-image and exact trace-equation hypotheses.
Small-mixing rank-one seeds therefore cannot solve this branch. In the
opposite branch, the indicated source-line angle and vanishing real
complement Chern class force exact decoupling and a flat complement.
These statements neither assume automatic reducibility of all rank-one
fields nor choose a favorable sign for the unresolved published
uniformization convention.

## 5. Research consequence

Round 10 supplied explicit complete two-ended near-Einstein geometries
but no fixed closed completion. This round supplies an actual closed
construction by a different matching mechanism. It then rules out
surface-bundle interpretations and virtual Kähler realizations for
specific members, and computes global variational quantities on them.

The decisive next problem is now precise: **does an explicit
\(M(h,g;u,f)\) admit a non-Kähler negative Einstein metric?**
Nonexistence on even one such object would turn its constructed family
into a negative-branch counterexample. Existence would instead require
an Einstein geometry beyond its surface-product and Kähler models.
Either outcome changes the mathematical situation; another reduction of
the already vanishing Ricci residual does not decide it.

No theorem here establishes the unrestricted negative branch, a complete
two-sign counterexample, or a publication-priority claim. The construction
and its topology provide a new research object and proved properties;
the global Einstein question has not been replaced by a restricted one.
