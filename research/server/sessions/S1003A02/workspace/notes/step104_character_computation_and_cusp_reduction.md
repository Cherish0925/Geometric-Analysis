# Step 104 — Character analysis closes the isotropy route; cusp reduction and shrinking-filler monopole supply

> **Binding Step-105 correction.** Propositions 104.C and 104.F are withdrawn and 104.M is downgraded to a route
> (Question 105.M); §4's “exactly two subchannels” is false — three remain. Reasons and the replacement cap-charge
> theorem: `notes/step105_cusp_channel_restored_and_cap_charge_theorem.md` §0–§4 (A01 #888, Spirit #119).

Session S1003A02, Agent2, Execute. Inputs: Step-103 handoff (Agent4 reading of 102.R/102.K);
Spirit #118; A01 peer #884 (isotropy data), #885 (character-label correction), #886 (no Wahl
obstruction from A01 machinery); `step103_independent_reading_wahl_isotropy_and_known_mechanisms.md`;
A01's `step89_wahl_isotropy.py`/`wahl_isotropy.json`.
Scripts: `workspace/scripts/step104_character_analysis.py` → `data/step104/character_analysis.json`.

---

## 1. Character computation and the stop of the isotropy route

### 1.1 Setup

For a Wahl ball \(B_{n,1}\) embedded in \(M = X\#k\overline{\mathbb{CP}}^2\) via a four-coordinate
block with realization vector \(v = (v_1,\dots,v_4)\), \(\sum v_i^2 = n^2\), the restriction of a
basic class \(c = K_X + \varepsilon_1 E_1 + \cdots + \varepsilon_k E_k\) (\(\varepsilon_i \in \{\pm1\}\))
to the boundary \(\partial B_{n,1} = L(n^2,n-1)\) has character
\[
j(c) \;=\; \sum_{i \in \text{block}} \varepsilon_i\, v_i \;\bmod\; n^2.
\]
The class extends to an orbifold \(\mathrm{spin}^c\) structure on \(V\) iff \(j(c) \equiv 0 \bmod n\)
(i.e., its restriction lies in the image of \(H^2(B_{n,1}) \to H^2(\partial B_{n,1})\), the
\(n\mathbb{Z}_{n^2}\) subgroup). This is precisely the extendible family tested by A01 in
`step89_wahl_isotropy.py`.

### 1.2 Computation (exact, n = 2 through 16)

For each \(n\), `step104_character_analysis.py` enumerates all four-square representations of \(n^2\)
(nonnegative, up to ordering) and all \(2^4 = 16\) sign choices \((\varepsilon_1,\dots,\varepsilon_4)\).
Results in `data/step104/character_analysis.json`:

- **For every \(n\ge2\), at least one representation \(v\) admits extending classes** (some sign choice
  gives \(j \equiv 0 \bmod n\)). Trivially \(v = (0,0,0,n)\) always works, but also many
  representations with positive coordinates work (e.g., \((0,1,2,2)\) for \(n=3\), \((1,2,2,4)\)
  for \(n=5\)).

- **Some representations have NO extending sign choice.** For \(n = 5\): \(v = (0,0,3,4)\)
  achieves only cosets \(\{1,2,3,4\}\); for \(n = 7\): \(v = (1,4,4,4)\) and \((2,2,4,5)\) achieve
  all of \(\{1,2,3,4,5,6\}\). For \(n = 14\), all representations except \((0,0,0,14)\),
  \((0,4,6,12)\), \((1,5,7,11)\), \((7,7,7,7)\) fail (the four that work have all components
  divisible by 7 or by the appropriate structure).

- **The "all-positive" class** (\(\varepsilon_i = +1\) for all \(i\)) is in the non-extending coset
  for most representations: its character is \(\sum v_i \bmod n\), which is generically nonzero.

### 1.3 Which vector does the PPS embedding produce?

The PPS construction (Proposition 4.4: tube four exceptional spheres to a \((-4)\)-sphere, then
embed \(B_{n,1}\) via chain blowdown) determines a specific vector \(v\) for each \(n\). Its exact
computation requires resolving the chain \(C_{n,1} = [n+2,2,\ldots,2]\) inside the blown-up disk
bundle and reading off the intersection with the standard exceptional basis. This is a topological
calculation that we do not need: **the curvature estimate on \(V\) does not depend on the character.**

### 1.4 Stop: why the isotropy route adds nothing

**Proposition 104.C.** The cone-point isotropy calculation of A01 (`step89_wahl_isotropy.py`) and the
character analysis above produce no curvature information on \(V\) beyond Proposition 102.K.

*Argument.*

(a) **The curvature estimates do not use an orbifold monopole.** Proposition 102.K(a)–(b) is proved
entirely by filler transfer: glue Şuvaina fillers at scale \(\varepsilon\to0\), apply LeBrun's smooth
estimates on \((M, g_\varepsilon)\), pass to the limit. The smooth SW theory on \(M\) uses the full
\(2^k\)-element basic-class family without specifying one class, and the resulting inequality
\(\int(s^-)^2 \ge 32\pi^2 A\) transfers to \(V\) as a consequence of the geometry of the Ricci-flat
ALE filler (86.S). No orbifold spin\(^c\) selection or orbifold monopole existence is involved.

(b) **For extending classes (\(j = 0 \bmod n\)), no isotropy obstruction exists.** A01's
computation shows that twist \(j = 0\) (the canonical complex-orbifold structure) and twist
\(j = 1\) both have \(\Phi(p) \ne 0\) for \(n \ge 2\). In particular, the extending family
has nonzero monopole value at the cone point, and the isotropy-forced zeros for \(j \ge 2\) are
irrelevant.

(c) **For non-extending classes (\(j \ge 2\)), isotropy forces \(\Phi(p) = 0\).** But non-extending
classes are not used in the curvature estimate. Even if an orbifold monopole in a non-extending
structure existed (it does not: the structure does not extend over the cone), its vanishing would
not enter the transferred inequality.

(d) **Spirit #118 correctly predicted:** the zero-count identity gives no constraint because
\(c_2(S^+) = (K_V^2 - T_+)/4 = 0\) for the canonical orbifold structure
(\(K_V^2 = T_+ = A - k\) by Noether), so the Euler class gives no information about zero
location. \(\square\)

**This closes the isotropy route.** The Wahl existence question remains a pure existence problem for
a non-Kähler, non-locally-symmetric negative Einstein orbifold, exactly as formulated at Step 103.

---

## 2. Proposition 104.M (orbifold monopole supply via shrinking-filler limit)

Although the curvature estimates do not need an orbifold monopole, it is useful to record that one
exists, partially rehabilitating the SW paragraph of 102.K(d).

**Proposition 104.M.** Let \(V = V_{X,\mathbf{n},k}\) be a realized Wahl orbifold (Theorem 102.R)
embedded with a realization vector admitting extending classes. For every orbifold Riemannian metric
\(g\) on \(V\) and every extending \(\mathrm{spin}^c\) structure \(\mathfrak{s} \in \iota(H^2(M))\),
there exists an orbifold monopole \((A,\Phi)\) on \((V, g, \mathfrak{s})\) satisfying the orbifold
Seiberg–Witten equations.

*Proof outline (the removability step is marked).*

1. **Filler resolution.** For each \(\varepsilon > 0\), Lemma 86.S gives a smooth metric
   \(g_\varepsilon\) on \(M\) by gluing the Şuvaina \(d = 1\) scalar-flat Kähler ALE filler at
   scale \(\varepsilon\) into each Wahl ball, with \(g_\varepsilon \to g\) uniformly on compact
   subsets of the complement \(W = M \setminus \bigsqcup B_{n_j,1}\).

2. **Smooth monopole.** The extending structure \(\mathfrak{s}\) restricts to a
   \(\mathrm{spin}^c\) structure on \(M\) (via the unique extension of a class \(c \in H^2(M)\)
   with \(j(c) \equiv 0 \bmod n_j\) for each ball). Since \(X\) is minimal of general type with
   \(b^+ > 1\), the class is a basic class, and LeBrun's theorem gives a solution
   \((A_\varepsilon, \Phi_\varepsilon)\) of the SW equations on \((M, g_\varepsilon)\).

3. **Uniform bounds on compacta.** The Weitzenböck formula gives
   \(|\Phi_\varepsilon|^2 \le \max(0, -s_{g_\varepsilon})\) pointwise. On any compact
   \(K \subset W\), \(s_{g_\varepsilon} \to s_g\) uniformly, so \(|\Phi_\varepsilon|\) is bounded.
   The coupled equations then bound \(\nabla\Phi_\varepsilon\) and \(F_{A_\varepsilon}\) in
   \(L^2(K)\).

4. **Uhlenbeck compactness.** A subsequence \((A_{\varepsilon_i}, \Phi_{\varepsilon_i})\) converges
   in \(C^\infty\) on compact subsets of \(W\) to a solution \((A_\infty, \Phi_\infty)\) of the SW
   equations with respect to the orbifold metric \(g\).

5. **Equivariant removability [marked for verification].** Near each cone point, the limit extends
   to a \(\mathbb{Z}_{n^2}\)-equivariant finite-energy solution on the local uniformizer
   \(\mathbb{R}^4 \setminus \{0\}\). Standard gauge-theoretic removable-singularity results
   (Uhlenbeck for connections; the Weitzenböck formula for the spinor) extend it across the origin.
   The quotient gives an orbifold monopole on \(V\).

6. **Structure identification.** The limit inherits the \(\mathrm{spin}^c\) structure of the
   approximating sequence. Since each \(\mathfrak{s}_\varepsilon\) restricts to the same topological
   class on \(W\), the limit is in \(\mathfrak{s}\). \(\square\)

**Status.** Steps 1–4 are standard. Step 5 uses the orbifold version of Uhlenbeck's removable
singularity theorem, which is available in the literature (Bando–Kasue–Nakajima for Yang–Mills
connections on orbifolds; the extension to the coupled SW system is routine but should be cited
precisely). The proposition is recorded with the removability step marked.

**Consequence.** For an extending basic class \(c\) with \(c^2 = A - k\), the orbifold monopole
gives \(|\Phi|^2 \le s^-\) on \(V\). This reproduces the filler-transfer estimate. No new
curvature information arises.

---

## 3. Proposition 104.F (cusp/F-structure reduction for ball-quotient hosts)

This completes the second alternative of the trichotomy by showing that the non-orbifold cusp
channel is empty for ball-quotient hosts.

**Proposition 104.F.** Let \(X = \Gamma \backslash \mathbb{CH}^2\) be a compact ball quotient
(\(\Gamma\) a cocompact torsion-free lattice in \(PU(2,1)\)) and
\(M = X\#k\overline{\mathbb{CP}}^2\). In any Anderson-type decomposition of a degeneration sequence
for metrics on \(M\) — where \(M\) is decomposed as a compact core \(\Omega\) (a complete
finite-volume Einstein domain) with finitely many cusp-like ends capped by collapsed regions \(C_j\)
along cross-sections \(L_j\) — the cusp channel reduces to the orbifold channel:

(i) Every cross-section \(L_j\) that is a spherical space form corresponds to an orbifold point
    (cone on \(L_j\)).

(ii) No cross-section \(L_j\) with \(\mathbb{Z}^2 \subset \pi_1(L_j)\) can contribute essential
     fundamental group to \(\pi_1(M) = \Gamma\).

(iii) The non-spherical-space-form cusp channel is therefore empty, and the entire second
      alternative sits within the orbifold framework.

*Proof.*

**Step A: \(\Gamma\) is Gromov-hyperbolic and contains no \(\mathbb{Z}^2\).**
The complex-hyperbolic plane \(\mathbb{CH}^2\) is \(\delta\)-hyperbolic in the sense of Gromov (it
has sectional curvatures in \([-4, -1]\)). Since \(\Gamma\) acts cocompactly and properly
discontinuously by isometries, \(\Gamma\) is Gromov-hyperbolic as a group (Milnor–Švarc lemma).
Every Gromov-hyperbolic group has the property that its abelian subgroups are virtually cyclic;
in particular, \(\mathbb{Z}^2\) does not embed in \(\Gamma\). Since \(\Gamma\) is torsion-free, every
finite subgroup is trivial.

**Step B: Three-manifold cross-sections and the \(\mathbb{Z}^2\) dichotomy.**
By Thurston geometrization, every closed oriented 3-manifold \(L\) has a prime decomposition and
a JSJ decomposition into geometric pieces. The eight Thurston geometries split into:

- **Spherical (\(S^3\)):** \(\pi_1(L)\) is finite. Since \(\Gamma\) is torsion-free,
  \(\pi_1(L) \to \Gamma\) is trivial.

- **\(S^2 \times \mathbb{R}\):** Closed manifolds are \(S^2 \times S^1\) (\(\pi_1 = \mathbb{Z}\))
  and \(\mathrm{RP}^3 \# \mathrm{RP}^3\) (\(\pi_1 = \mathbb{Z}_2 * \mathbb{Z}_2\), no
  \(\mathbb{Z}^2\)). Neither has \(\mathbb{Z}^2\); the image in \(\Gamma\) is cyclic or trivial.

- **Flat (\(\mathbb{E}^3\)):** \(\pi_1\) is a Bieberbach group, which contains
  \(\mathbb{Z}^3 \lhd \pi_1\). Hence \(\mathbb{Z}^2 \subset \pi_1(L)\).

- **Nil, Sol, \(\widetilde{SL_2(\mathbb{R})}\), \(\mathbb{H}^2 \times \mathbb{R}\):**
  Each has a Seifert or torus-bundle structure whose \(\pi_1\) contains \(\mathbb{Z}^2\) (the
  fiber generates a central or normal \(\mathbb{Z}\) subgroup that combines with an element of
  infinite order in the base).

- **Hyperbolic (\(\mathbb{H}^3\)):** \(\pi_1\) is Gromov-hyperbolic with no \(\mathbb{Z}^2\).
  However, hyperbolic cross-sections do not arise as cusp cross-sections in four-dimensional
  Einstein degeneration: they correspond to expanding rather than collapsing ends.

**Step C: The \(\Gamma\)-vertex argument.**
In the decomposition \(M \simeq \Omega \cup_{L_1} C_1 \cup \cdots\), van Kampen gives
\(\pi_1(M) = \pi_1(\Omega) *_{\pi_1(L_j)} \pi_1(C_j) / \cdots\). Since each
\(\pi_1(C_j)\) factors through \(\pi_1(L_j)\), and Steps A–B show that
\(\pi_1(L_j) \to \Gamma\) has image at most cyclic (or trivial) whenever \(L_j\) is not
spherical, the entire group \(\Gamma\) must be realized in \(\pi_1(\Omega)\). By the asphericity of
\(X\) and the classifying-map argument, \(\Omega\) carries a proper degree-one map to \(X\).

**Step D: Reduction.**
Spherical space form cross-sections give orbifold points after capping (already treated by the
Wahl/\(D_{\ge6}\) analysis). Cross-sections with \(\mathbb{Z}^2\) cannot carry essential topology
into \(\Gamma\). The \(S^2 \times \mathbb{R}\) case (cyclic image) contributes no aspherical
topology. Therefore every cusp in an Anderson-type decomposition is either:
- an orbifold point (spherical cross-section), or
- carries only cyclic or trivial fundamental group (not enough to support \(\Gamma\)).

In the second case, the collapse region \(C_j\) is topologically inessential for carrying the
complex-hyperbolic lattice. The Einstein domain \(\Omega\) still carries \(\Gamma\) entirely. But
such ends with non-spherical cross-sections would need to carry exceptional \(\overline{\mathbb{CP}}^2\)
summands, and the cross-section's \(\mathbb{Z}^2\) cannot inject into \(\Gamma\), so these ends
degenerate to volume zero without contributing topology to the limit.

**Conclusion.** The cusp/F-structure channel reduces to the orbifold channel for ball-quotient
hosts. Total collapse (\(\operatorname{Vol} \to 0\)) is excluded because \(\Gamma\) is not virtually
nilpotent (Cheeger–Gromov). \(\square\)

---

## 4. The refined trichotomy (exact form)

For \(M = X\#k\overline{\mathbb{CP}}^2\), \(0 < k < A/3\), with \(X\) a compact ball quotient, the
second alternative (nonattained zero) now has exactly **two** geometric subchannels:

**(2a) Wahl orbifold channel.** The family \(V_{X,\mathbf{n},k}\) of Theorem 102.R is
geometrically realized. All aggregate curvature methods are blind (Proposition 102.K), the
isotropy route adds nothing (Proposition 104.C), and the cusp channel collapses to the orbifold
case (Proposition 104.F). Whether some \(V\) with \(A > 3k\) admits a negative, non-Kähler,
non-locally-symmetric Einstein orbifold metric is the remaining existence question.

**(2b) \(D_{\ge6}\) prism complement channel.** Theorem 96.K gives necessary
filler/rank/threshold data only. No geometric complement or Einstein orbifold is constructed.

The third sub-channel previously listed (Einstein cusp domains or F-structure collapse) is now
subsumed by (2a)–(2b) via Proposition 104.F.

The overall trichotomy remains:
1. \(\alpha > 0\) (positive gap), requiring a class-sensitive same-metric relation;
2. \(\alpha = 0\) nonattained, through an Einstein orbifold with spherical-space-form singularities;
3. smooth negative Einstein metric, giving \(\alpha = 0\) attained.

---

## 5. Summary of what this Step establishes and what it does not

**Established:**
- The optimal curvature supply class has trivial boundary character (j = 0) or can be chosen to
  have it; for j = 0, no isotropy obstruction exists. The isotropy route adds no information.
- Orbifold monopole existence in extending structures, modulo standard equivariant removability.
- The cusp/F-structure channel is empty for ball-quotient hosts; the nonattained-zero alternative
  has exactly two orbifold subchannels.
- The zero-count identity \(c_2(S^+) = 0\) for the canonical structure on \(V\) gives no constraint.

**Not established:**
- Whether the PPS embedding vector for specific \(n\) admits extending classes (this is a topological
  calculation not needed for the curvature argument).
- The orbifold Uhlenbeck removability for SW monopoles (routine, but not explicitly sourced).
- Any curvature consequence beyond Proposition 102.K.
- Existence or nonexistence of a negative Einstein orbifold metric on the realized Wahl family.
- A class-sensitive smooth inequality for the positive-gap alternative.
