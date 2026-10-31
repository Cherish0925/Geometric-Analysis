# Positive A1 inputs: topology, curvature budgets, and a global volume restriction

## 1. The concrete conclusion

The positive branch asks whether sufficiently small
\(\delta_+(g)=\|g^{-1}\operatorname{Ric}_g-I\|_{\infty,\mathrm{op}}\)
forces the same closed smooth manifold to admit an Einstein metric of
**some** sign. This note studies the existing marked A1 construction
on positive Einstein orbifolds, not the negative shear manifolds.

On \(M=\mathbb{CP}^2\#\mathbb{CP}^2\), write the inherited two-pole input
in the normalization
\[
 \|\operatorname{Ric}_{g_a}^{\sharp}-3I\|_\infty\longrightarrow0,
 \qquad V_a\longrightarrow V_0=\frac{4\pi^2}{3}.            \tag{1}
\]
Every positive Einstein metric \(h\) on this smooth manifold,
normalized by \(\operatorname{Ric}_h=3h\), must satisfy
\[
 \boxed{\operatorname{Vol}(M,h)<\frac{4\pi^2}{9}=\frac{V_0}{3}.} \tag{2}
\]
Consequently, allowing arbitrary diffeomorphisms,
\[
 \boxed{
 \liminf_{a\to0}
 \inf_{\substack{\operatorname{Ric}_h=3h\\\phi\in\operatorname{Diff}(M)}}
 \|g_a^{-1}\phi^*h-I\|_{\infty,\mathrm{op}}
 \ \ge\ 1-\frac1{\sqrt3}.}                                 \tag{3}
\]
The infimum is \(+\infty\) when the indicated Einstein class is empty.
This is a quantitative application of the classical half-Weyl gap,
not a new general gap theorem. Sections 5–6 give the proof.
No symmetry or proximity hypothesis is imposed on \(h\).

The topological calculations also explain why characteristic numbers,
spin index and fundamental group do not complete a positive-branch
counterexample on these inputs. They specify actual remaining objects;
they do not assert that every possible obstruction has been exhausted.

## 2. The inherited input and norm conventions

We use Theorem A1 in
[the existing construction manuscript](skill/research/20260916_construction.tex),
with its fixed Einstein orbifold, actual EH end markings and fillings,
and corrected core with second-order asymptotics in a common radial
gauge. These inherited hypotheses are not replaced by a formal gluing
picture. Its metrics have vanishing unweighted Ricci endomorphism
defect, smooth convergence away from the nodes and vanishing
replacement volume. Their volumes tend to the orbifold volume.

Positive bulk metrics below have \(\operatorname{Ric}=3g\), hence
\(s=12\). Multiplying the metric by three gives the normalization in
\(\delta_+\). Write \(E=\operatorname{Ric}-sg/4\) and use the
Hilbert–Schmidt **operator** norm on each Weyl block:
\[
\begin{split}
 8\pi^2\chi&=\int\left(|W^+|^2+|W^-|^2+\frac{s^2}{24}
                                  -\frac{|E|^2}{2}\right),\\
 12\pi^2\tau&=\int(|W^+|^2-|W^-|^2).                       \tag{4}
\end{split}
\]
One EH bubble has Weyl energy \(12\pi^2\), or full four-index
Riemann energy \(48\pi^2\).

## 3. Exact transport of the characteristic numbers

Let \(\mathcal O\) have \(N\) A1 points, and set
\[
 \chi_{\mathrm{orb}}=\chi(|\mathcal O|)-N/2,\qquad
 \tau_{\mathrm{orb}}=
 \frac1{12\pi^2}\int_{\mathcal O}(|W^+|^2-|W^-|^2).
\]
For A1 links the signature eta correction vanishes, so
\(\tau_{\mathrm{orb}}\) also equals the rational intersection-form
signature of the punctured orbifold. The orbifold Euler number is
not the Euler number of the underlying topological space.

Suppose the \(i\)-th filling is the disk bundle with Euler number
\(2\epsilon_i\), where \(\epsilon_i\in\{+1,-1\}\) is measured in the
orientation of the final closed manifold. Let \(N_\pm\) count them.
Then
\[
\begin{split}
 \chi(M)&=\chi_{\mathrm{orb}}+\frac32N
          =\chi(|\mathcal O|)+N,\\
 \tau(M)&=\tau_{\mathrm{orb}}+N_+-N_-,\\
 2\chi(M)+3\tau(M)&=
       2\chi_{\mathrm{orb}}+3\tau_{\mathrm{orb}}+6N_+,\\
 2\chi(M)-3\tau(M)&=
       2\chi_{\mathrm{orb}}-3\tau_{\mathrm{orb}}+6N_- .       \tag{5}
\end{split}
\]
Indeed the removed cone has ordinary Euler number one, whereas its
replacement retracts to a sphere and has Euler number two. Its
relative signature is \(\epsilon_i\), and the boundary
\(\mathbb{RP}^3\) is a rational homology sphere. Excision and
signature additivity prove (5).
These identities are already used in
[Round 7, equation (13)](round7_endpoint.md) and are a specialization
of Ozuch's modified-invariant additivity in
[Section 7.1](https://arxiv.org/pdf/1909.12960).
They are not a new theorem of this round.

For a positive Einstein bulk,
\[
 2\chi_{\mathrm{orb}}\pm3\tau_{\mathrm{orb}}
 =\frac1{4\pi^2}\int_{\mathcal O}(6+2|W^\pm|^2)>0.          \tag{6}
\]
Every standard chiral A1 filling therefore satisfies strict
Hitchin–Thorpe, regardless of chirality distribution. This holds
object by object in varying families, without giving a uniform
positive lower bound for the bulk quantity (6).

The actual approximating metrics also satisfy the exact limiting budget
\[
 \lim_{a\to0}\int_M|W^\pm_{g_a}|^2
  =\int_{\mathcal O}|W^\pm_{g_0}|^2+12\pi^2N_\pm.           \tag{7}
\]
The Ricci estimate and volume convergence give
\(\int|E_a|^2\to0\), \(\int s_a^2\to144V_0\).
Solving (4) for the Weyl energies and substituting (5) proves (7).
Smooth exterior convergence identifies the excess as concentrated
near the nodes. Rescaled EH convergence supplies at least
\(12\pi^2\) in the designated Weyl half at every node. Since their
sum exhausts (7), no additional limiting Weyl energy remains in the
annuli. This last assertion uses the actual core convergence.

## 4. Actual marked smooth objects

### 4.1 The two-pole football

For
\(\mathcal O_F=S^4/\langle(x_0,x)\mapsto(x_0,-x)\rangle\),
the regular part between the poles is
\(\mathbb{RP}^3\times(0,1)\), and
\[
 \chi_{\mathrm{orb}}=1,\quad\tau_{\mathrm{orb}}=0,\quad
 V_0=4\pi^2/3,\quad W^\pm=0.
\]
Let \(m\) count positive EH bolts. The simply connected disk bundles
kill the fundamental group of the regular part. Thus
\(\pi_1=0,\ \chi=4,\ b_2=2,\ \tau=2m-2\).

| \(m\) | Marked smooth type | \((b_+,b_-)\) | Spin | Limiting \((\int|W^+|^2,\int|W^-|^2)/\pi^2\) |
| --- | --- | --- | --- | --- |
| 0 | \(\overline{\mathbb{CP}^2\#\mathbb{CP}^2}\) | \((0,2)\) | no | \((0,24)\) |
| 1 | \(S^2\times S^2\) | \((1,1)\) | yes | \((12,12)\) |
| 2 | \(\mathbb{CP}^2\#\mathbb{CP}^2\) | \((2,0)\) | no | \((24,0)\) |

These smooth identifications use the standard orthogonal markings,
not intersection-form classification alone. The proof of the
two-pole proposition in the construction manuscript transports
the torus action through boundary isotopies and applies
[Orlik–Raymond, Section 5](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/orlikraymond1.pdf).
In particular the opposite-sign choice is not the Page manifold
\(\mathbb{CP}^2\#\overline{\mathbb{CP}}^2\).

### 4.2 The four-node product quotient

Give both factors of \(S^2\times S^2\) curvature three and divide by
the simultaneous half-turn. The quotient \(\mathcal O_P\) has
\[
 \chi_{\mathrm{orb}}=2,\quad\tau_{\mathrm{orb}}=0,\quad
 V_0=\frac{8\pi^2}{9},\quad
 \int_{\mathcal O_P}|W^\pm|^2=\frac{16\pi^2}{3}.            \tag{8}
\]
Its punctured cover is simply connected with deck group
\(\mathbb Z_2\), and any filled boundary kills the deck generator.
For \(m\) positive bolts every resolution has
\[
 \pi_1=0,\quad \chi=8,\quad\tau=2m-4,\quad b_2=6,\quad
 (b_+,b_-)=(m+1,5-m),                                    \tag{9}
\]
and
\[
 \lim\frac{\int|W^+|^2}{\pi^2}=\frac{16}{3}+12m,\qquad
 \lim\frac{\int|W^-|^2}{\pi^2}=\frac{16}{3}+12(4-m).        \tag{10}
\]

| Marking | Oriented smooth type | Spin |
| --- | --- | --- |
| \(m=0\) | \(\mathbb{CP}^2\#5\overline{\mathbb{CP}}^2\) | no |
| \(m=1\) | \(2\mathbb{CP}^2\#4\overline{\mathbb{CP}}^2\) | no |
| \(m=2\), adjacent changed corners | \(3\mathbb{CP}^2\#3\overline{\mathbb{CP}}^2\) | no |
| \(m=2\), opposite changed corners | \(\#_3(S^2\times S^2)\) | yes |
| \(m=3\) | \(4\mathbb{CP}^2\#2\overline{\mathbb{CP}}^2\) | no |
| \(m=4\) | \(5\mathbb{CP}^2\#\overline{\mathbb{CP}}^2\) | no |

The actual lattice in the parity calculation is
\[
 L=\mathbb Z^2+\mathbb Z(1/2,1/2),\quad
 u=(1,0),\quad p=(1/2,1/2),\quad v=2p-u,\quad m_0=u-p.
\]
Here \(m_0\) is a characteristic vector, not the bolt count.
The original lines are \(u,v,u,v\); the all-negative inserted lines
are \(p,m_0,p,m_0\). A chirality change switches the corresponding
inserted line. Consecutive primitive vectors have determinant of
absolute value one in \(L\).
The mod-two characteristic criterion requires a homomorphism
\(\ell:L\to\mathbb F_2\) taking value one on every characteristic
vector. Since \(u=p+m_0\), both \(p\) and \(m_0\) cannot occur.
All inserted vectors equal \(p\), or all equal \(m_0\), exactly for
the opposite-corner patterns. The
[Davis–Januszkiewicz characteristic-class formula](https://people.math.osu.edu/davis.12/old_papers/DJ_toric.dmj.pdf)
therefore gives spin precisely then. The smooth torus classification
and (9) identify the table. These marked identifications are inherited
from the standard-model section of
[the cumulative manuscript](skill/research/20260912.tex).

The extreme rows are the two orientations of a smooth type admitting
positive Kähler–Einstein metrics:
[Tian, Theorem 1.1](https://www.maths.ed.ac.uk/~icheltso/cambridge/pdf/tian90.pdf)
includes the five-point blow-up. They are not counterexamples.
The mixed rows are specific additional research objects, not
additional nonexistence theorems.

### 4.3 What the elementary obstructions say

All these marked inputs admit positive scalar curvature and have
finite fundamental group. The displayed examples are simply connected.
A nonzero spin Dirac index or a persistent positive-square monopole
obstruction would obstruct the input itself. For the spin rows
\(\tau=0\) and \(\widehat A=-\tau/8=0\).
For rows with \(b_+>1\), the ordinary Seiberg–Witten invariants
vanish by the positive-scalar-curvature Weitzenböck argument, separately
after orientation reversal whenever its \(b_+\) also exceeds one.
No chamber-independent vanishing is asserted for \(b_+=1\).

The positive Ricci input is incompatible with an infinite-fundamental-
group obstruction on the same manifold. Its universal cover is compact
and has zero volume entropy. The degree-to-hyperbolic and entropy
mechanisms used on other project objects thus do not transfer merely
by changing a node marking. These checks settle the named tests, not
Einstein existence.

## 5. Positive-output volume on the definite filling

**Proposition 1.** For \(M=\mathbb{CP}^2\#\mathbb{CP}^2\), every
\(\operatorname{Ric}_h=3h\) satisfies (2). Equivalently,
\[
 \frac{\int s_h\,d\mu_h}{\operatorname{Vol}(h)^{1/2}}
          =12\operatorname{Vol}(h)^{1/2}<8\pi.              \tag{11}
\]

**Proof.** In the positive definite orientation,
\((\chi,\tau,b_-)=(4,2,0)\), and (4) gives
\[
       \int|W^-_h|^2=4\pi^2-3\operatorname{Vol}(h).        \tag{12}
\]
The tensor \(W^-\) cannot vanish identically. Hitchin's classification
of compact positive half-conformally-flat Einstein four-manifolds
would otherwise make this simply connected manifold \(S^4\) or
\(\mathbb{CP}^2\), contrary to \(b_2=2\).

Gursky–LeBrun's
[Theorem 1 and Corollary 1](https://arxiv.org/pdf/math/9807055)
give, in the norm convention (4),
\[
           \int|W^-_h|^2\ge\int s_h^2/24=6\operatorname{Vol}(h).
                                                               \tag{13}
\]
Equality gives reverse local Kähler geometry. On a simply connected
manifold the parallel Kähler form globalizes, giving a nonzero
anti-self-dual harmonic two-form, contrary to \(b_-=0\).
Hence (13) is strict; (12) then yields \(9\operatorname{Vol}(h)<4\pi^2\).
Equation (11) follows. QED.

The same primary paper records and uses Hitchin's classification in
its proof of Theorem A. Proposition 1 is an application of these
classical results, not an asserted optimal bound for this manifold.
For the actual inputs,
\[
 \frac{\int s_{g_a}}{V_a^{1/2}}\longrightarrow8\pi\sqrt3,
 \qquad \int|W^-_{g_a}|^2\longrightarrow0.                 \tag{14}
\]
Small Ricci defect does not allow applying the positive Einstein
half-Weyl gap to these approximate metrics.

For \(\operatorname{Ric}_h=-3h\), (12) still holds but gives only
\(\operatorname{Vol}(h)\le4\pi^2/3\). The positive-scalar hypothesis
in (13) is essential. Ricci-flat metrics have no nonzero-Einstein-
constant volume normalization. Neither alternative has been excluded.

## 6. Diffeomorphism-invariant C0 separation

**Corollary 2.** Whenever \(V_a>4\pi^2/9\), every
\(\operatorname{Ric}_h=3h\) and every diffeomorphism \(\phi\) satisfy
\[
 \|g_a^{-1}\phi^*h-I\|_{\infty,\mathrm{op}}>
       1-\sqrt{\frac{4\pi^2}{9V_a}}.                      \tag{15}
\]

**Proof.** If the left side is \(e<1\), then
\(\phi^*h\ge(1-e)g_a\). In real dimension four,
\(\operatorname{Vol}(h)\ge(1-e)^2V_a\).
Substitute (2) and solve for \(e\). If \(e\ge1\), (15) is automatic.
Taking the infimum and then the lower limit proves (3). QED.

This bounds all normalized positive outputs on the fixed manifold,
not only torus-invariant metrics or a chosen gluing ansatz.
Rescaling changes the Einstein normalization and is not silently
allowed in (3). Arbitrary output scale and sign are allowed by
Yau26 itself.

## 7. The exact unresolved object

The inherited two-pole theorem provides
\[
             e_+(\mathbb{CP}^2\#\mathbb{CP}^2)=0.          \tag{16}
\]
Thus \(P_4^+\) implies that this same standard smooth manifold has
an Einstein metric. Equations (2)–(3) restrict any positive output,
but do not decide this implication.

There are further precise restrictions. No almost complex structure
exists in either orientation: its integer Todd genus would be
\((\chi+\tau)/4\), but \(\chi+\tau\) is six or two.
Thus a hypothetical Einstein metric is not Hermitian for a global
complex structure. For nonpositive Einstein constant the Bochner
identity and \(b_1=0\) exclude Killing fields, so its isometry group
is finite. For positive Einstein constant, Gursky–LeBrun's Theorem A
also excludes nonnegative sectional curvature everywhere on this
definite manifold.

The inherited spherical-open-set argument in the cumulative manuscript
already excludes Einstein metrics in the whole conformal class of a
literal spherical gluing input. An Einstein metric conformal on that
open set has vanishing Weyl tensor there, hence everywhere by analytic
continuation; its resulting space-form topology is impossible.
This is not new in this round. The input on \(S^2\times S^2\), which
does admit its product Einstein metric, shows why that argument
cannot become an all-metrics nonexistence theorem.

The precise outstanding question is:

> Does the standard smooth manifold
> \(\mathbb{CP}^2\#\mathbb{CP}^2\) admit any Einstein metric—possibly
> negative or Ricci-flat, or positive with volume satisfying (2)?

The arguments and sources used here do not decide it.
All-sign nonexistence would defeat \(P_4^+\) via (16), but not by
itself the interval statement \(Q_4\iff P_4^+\lor P_4^-\).
Conversely existence would settle this object, not the positive
branch on every four-manifold.

## 8. Verification scope

The accompanying Python checker verifies the two chiral transport
identities, all football rows and sixteen product markings, the
integral torus lattice and spin criterion, the separate Weyl and
full-Riemann budgets, and the volume-ratio and C0 coefficients.
It rejects the Page-manifold substitution and a missing orbifold
Euler correction. Finite algebra does not certify the inherited
gluing analysis, Hitchin classification or the half-Weyl gap.
No all-sign Einstein obstruction on the definite filling is proved here.
