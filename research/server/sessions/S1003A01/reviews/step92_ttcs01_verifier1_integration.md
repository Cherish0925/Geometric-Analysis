# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 92,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step92_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step92_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the new A02 Theorem 105.Q/Corollaries 105.L and 105.H in the supplied note. Re-derive all signs, orientations, constants, and limiting arguments from the stated Theorem-G convention. Pay special attention to: boundary orientation in Q_+, whether C^2 boundary convergence controls eta as asserted; existence/order of the double limit defining c_j; whether volume convergence implies cap volume tends to zero; the cap contribution to LeBrun’s mixed estimate and the optimization leading to 9k+8 sum c_j <=3A; Dai–Wei’s adiabatic eta normalization; the formula c=4-r for an S3 Hopf cap; and the inference that a zero-charge -I4 cap must carry its odd form through energy-free collapse. Distinguish proved consequences under (E) from heuristic topology. If a statement needs repair, give the corrected statement and proof. Also assess whether a w2/spin or eta/Dirac argument can actually exclude the zero-charge four-class cap without assuming what is to be proved.

## Integrated Scientific Memo

# Verification memo: 105.Q, 105.L and 105.H

The **cap sign**, the mixed-estimate constant
\[
\boxed{9k+8\sum_jc_j\le3A},
\]
and the Hopf-cap formula \(c_+=4-r\) are correct. The principal repairs are:

- distinguish the charge of a **group of ends attached to one cap** from separately convergent charges of individual ends;
- correct the cap-volume argument;
- include positive-charge ball caps in 105.H;
- replace “invisible to every aggregate curvature inequality” by “invisible to the transferred \(C_+\)/LeBrun estimate”;
- withdraw the asserted classification of how the odd lattice must survive.

Two disagreements in the independent checks can be resolved decisively. **Fixed-link \(C^2\) convergence does control the odd-signature eta invariant.** And for the zero-\(c_+\) four-class cap, the correct opposite-chirality charge is
\[
\boxed{c_-=20,\qquad \int |W^-|^2\longrightarrow40\pi^2},
\]
not \(24\).

## 1. Theorem-G signs and boundary orientation

Write \(T_\pm(D)=2\chi(D)\pm3\tau(D)\). From the supplied conventions,
\[
2e\pm3L
=
\frac1{2\pi^2}|W^\pm|^2
+\frac1{96\pi^2}s^2
-\frac1{8\pi^2}|\operatorname{Ric}^{\circ}|^2.
\]
Integration gives
\[
T_\pm(D)=C_\pm(D)-\widehat P(D)+2\mathcal E\mp3\mathcal H,
\]
hence
\[
\widehat P(D)=C_\pm(D)-T_\pm(D)+\mathcal Q_\pm(\partial D),
\qquad
\mathcal Q_\pm=2\mathcal E\mp3\mathcal H.
\]

Let \(L_{j,\rho}\) denote all interfaces incident to \(C_j^{(\rho)}\), oriented as boundaries of \(\Omega_\rho\). On the cap side, both the induced boundary orientation and outward normal are reversed. The interface transgressions therefore cancel:
\[
\mathcal Q_\pm(\partial C_j^{(\rho)})
=-\mathcal Q_\pm(L_{j,\rho}).
\]
Consequently,
\[
C_\pm(g_i;C_j^{(\rho)})
=
T_\pm(C_j)+\mathcal Q_\pm(L_{j,\rho};g_i)
+\widehat P(g_i;C_j^{(\rho)}).
\tag{1}
\]
This proves the **plus sign** in 105.Q.

The sign reversal here concerns the two sides of a common interface. It should not be confused with reversing the orientation of the entire four-manifold, which exchanges \(W^+\) and \(W^-\).

## 2. Fixed-link eta convergence: \(C^2\) is sufficient

The note’s conclusion is correct, although “smooth dependence because the kernel is topological” is an abbreviated justification.

Fix \(\rho\), pull back to a fixed link, and let \(h_i\to h_\infty\) in \(C^2\). On the cylinder \(L\times[0,1]\), interpolate by
\[
G_i=dt^2+h_\infty+f(t)(h_i-h_\infty),
\]
where \(f\) is constant near both endpoints. These metrics have product endpoint collars and converge in \(C^2\) to \(dt^2+h_\infty\). The APS signature formula, in the supplied normalization, gives
\[
\eta_G(h_i)-\eta_G(h_\infty)=\int_{L\times[0,1]}L(G_i).
\tag{2}
\]
The cylinder has signature zero. Since \(L(G_i)\) depends continuously on the curvature, \(C^2\) convergence controls its integral. The limiting product metric has no curvature component in the interval direction, so its degree-four \(L\)-form vanishes. Thus
\[
\eta_G(h_i)\longrightarrow\eta_G(h_\infty).
\]

Equivalently, the variation formula expresses the difference through a local gravitational transgression. The odd-signature kernel consists of harmonic forms and has fixed dimension; no additional spectral-flow jump occurs near the limiting metric.

The Euler and collar-signature transgressions are also continuous under \(C^2\) collar convergence. Therefore
\[
\mathcal Q_\pm(L_{j,\rho};g_i)
\longrightarrow
\mathcal Q_\pm(L_{j,\rho};g_\infty).
\tag{3}
\]
No \(C^\infty\) strengthening is needed at a **fixed nondegenerate link**. This does not assert uniform eta control as \(\rho\to0\) and the links collapse.

## 3. Corrected cap-charge theorem under (E)

Use the compatible fixed-domain identifications implicit in (E), and label cap components consistently along the nested exhaustion.

### Fixed-\(\rho\) limit

By (1), (3), and \(0\le\widehat P(C_j)\le\widehat P(M)\to0\),
\[
c_j^\pm(\rho):=\lim_i C_\pm(g_i;C_j^{(\rho)})
=
T_\pm(C_j)+\mathcal Q_\pm(L_{j,\rho};g_\infty).
\tag{4}
\]

### Outer limit: a noncircular proof

As the exhaustion grows, the corresponding cap shrinks. If \(C_j^{(\rho')}\subset C_j^{(\rho)}\), their intervening shell \(S_j\) is contained in \(\Omega\). Energy additivity and local convergence give
\[
c_j^\pm(\rho)-c_j^\pm(\rho')
=C_\pm(g_\infty;S_j)\ge0.
\tag{5}
\]
Thus \(c_j^\pm(\rho)\) decreases to a finite nonnegative limit:
\[
c_j^\pm=\lim_{\rho\to0}\lim_i C_\pm(g_i;C_j^{(\rho)})\ge0.
\tag{6}
\]
In particular, (4) proves convergence of the **total interface charge incident to each cap**, without Dai–Wei asymptotics.

There is one scope correction. If a cap meets several ends, (E) directly proves
\[
c_j^+
=
T_+(C_j)+
\lim_{\rho\to0}\sum_{\ell\in J_j}
\mathcal Q_+(L_{\ell,\rho};g_\infty).
\tag{7}
\]
It does not, merely from convergence of this sum, prove that every summand has a separate limit. The original sum of individual \(\mathcal Q_+^\infty(L_\ell)\) is justified when separate limits are supplied—for example by fibred-cusp asymptotics, or by fixed product-topology end shells, where the individual annulus identity gives the same monotonicity argument.

The order in (6) is essential. The proof does not establish an arbitrary simultaneous limit with \(\rho=\rho_i\).

### Cap volume and scalar energy

At fixed \(\rho\), volume convergence gives
\[
\lim_i\sum_j\operatorname{Vol}_{g_i}(C_j^{(\rho)})
=
V_\infty(\Omega)-V_\infty(\Omega_\rho).
\tag{8}
\]
A single cap is **not** generally equal in volume to this entire tail.

The immediate consequence sufficient for all estimates is
\[
\lim_{\rho\to0}\limsup_i
\operatorname{Vol}_{g_i}(C_j^{(\rho)})=0.
\tag{9}
\]
Moreover, the nesting already used in (5) actually recovers ordinary fixed-\(\rho\) limits; no extra subsequence is necessary. For a farther exhaustion level,
\[
\operatorname{Vol}_{g_i}(C_j^{(\rho)})
=
\operatorname{Vol}_{g_i}(S_j)
+\operatorname{Vol}_{g_i}(C_j^{(\rho')}).
\]
The shell volume converges locally, and the last term has limsup bounded by the total tail volume at \(\rho'\), which tends to zero. Hence
\[
\lim_i\operatorname{Vol}_{g_i}(C_j^{(\rho)})
=
\operatorname{Vol}_{g_\infty}(C_j^{(\rho)}\cap\Omega).
\tag{10}
\]

Put \(\epsilon_i=\int_M(s_i-\bar s_i)^2\to0\). For any measurable region \(D\),
\[
\left|\int_Ds_i^2-\bar s_i^2\operatorname{Vol}_{g_i}(D)\right|
\le
\epsilon_i+
2|\bar s_i|\sqrt{\epsilon_i\,\operatorname{Vol}_{g_i}(D)}.
\tag{11}
\]
Total volume is bounded, so the right side tends to zero uniformly in \(D\). Equations (10)–(11) prove fixed-\(\rho\) scalar-energy convergence and
\[
\lim_{\rho\to0}\lim_i\int_{C_j^{(\rho)}}s_i^2=0.
\tag{12}
\]
Subtracting the scalar term from (4) now justifies the original ordinary iterated limit:
\[
\boxed{
c_j^+
=
\lim_{\rho\to0}\lim_i
\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W_i^+|^2.
}
\tag{13}
\]

### Global decomposition

On the closed manifold,
\[
C_+(g_i;M)=A-k+\widehat P(g_i;M)\longrightarrow A-k.
\]
Splitting at fixed \(\rho\), then using monotone convergence on \(\Omega\), yields
\[
\boxed{
C_+(g_\infty;\Omega)=A-k-\sum_jc_j^+.
}
\tag{14}
\]
The identical argument gives
\[
C_-(g_\infty;\Omega)
=(2\chi-3\tau)(M)-\sum_jc_j^-.
\tag{15}
\]

Thus 105.Q is valid with the corrected grouped-end formulation (7) and the repaired volume proof.

## 4. LeBrun transfer and optimization

Let \(C=\sum_jc_j^+\), and define
\[
\int_\Omega s_\infty^2=96\pi^2x,\qquad
\int_\Omega|W_\infty^+|^2=2\pi^2y.
\]
Then
\[
x+y=A-k-C.
\tag{16}
\]

### Cap contribution is exactly \(12\pi^2C\)

On the cap union \(K_\rho\),
\[
\int_{K_\rho}(s_i-\sqrt6|W_i^+|)^2
=
\int_{K_\rho}s_i^2
+6\int_{K_\rho}|W_i^+|^2
-2\sqrt6\int_{K_\rho}s_i|W_i^+|.
\]
The scalar integral vanishes in the iterated limit, and
\[
\left|\int_{K_\rho}s_i|W_i^+|\right|
\le
\|s_i\|_{L^2(K_\rho)}\|W_i^+\|_{L^2(K_\rho)}
\longrightarrow0.
\]
Therefore, in the iterated limsup/liminf sense, sufficient even if the mixed integral has no fixed-\(\rho\) limit,
\[
\boxed{
\int_{K_\rho}(s_i-\sqrt6|W_i^+|)^2
\longrightarrow12\pi^2C.
}
\tag{17}
\]
A positive-charge cap cannot be omitted from this functional.

### Einstein-domain contribution

Cauchy–Schwarz gives
\[
\int_\Omega(s_\infty-\sqrt6|W_\infty^+|)^2
\le
12\pi^2(\sqrt{8x}+\sqrt y)^2
\le108\pi^2(x+y).
\tag{18}
\]
The last coefficient is optimal for nonnegative \(x,y\) with fixed sum:
\[
(\sqrt{8x}+\sqrt y)^2\le9(x+y),
\]
with equality at \(x:y=8:1\). Equality in the preceding integral estimate also requires \(|W^+|\) proportional to \(|s_\infty|\) almost everywhere; since \(s_\infty\) is constant, this requires constant \(|W^+|\). These are algebraic equality conditions, not a demonstrated geometric realization.

Combining (17)–(18) with the stipulated LeBrun estimate gives
\[
72\pi^2A
\le108\pi^2(A-k-C)+12\pi^2C,
\]
hence
\[
\boxed{9k+8C\le3A}.
\tag{19}
\]

The scalar estimate \(\int_Ms^2\ge32\pi^2A\), if separately supplied, transfers to \(x\ge A/3\) and gives the note’s
\[
k+C\le2A/3.
\]
But this second conclusion is redundant in the stated blow-up setting: \(k,C\ge0\) and (19) already imply the stronger
\[
\boxed{k+C\le3A/8}.
\tag{20}
\]

Positive charge and vanishing volume force unbounded curvature and concentration. They do **not**, without compactness and rescaling estimates, automatically produce complete smooth bubbles.

## 5. Dai–Wei normalization and Hopf charges

The external Dai–Wei paper is not reproduced in the bounded input. What can be checked here is the quoted normalization against Theorem G and the independent model integrals in Step 33.

Let \(\eta_G\) denote the signature correction used in Theorem G. The quoted Dai–Wei convention is
\[
\mathcal H_\infty
=\frac12\,\mathrm a\!-\!\lim\eta_{\rm DW}
=\frac e3-\operatorname{sign}e,
\qquad
\mathcal E_\infty=0.
\tag{21}
\]
Thus \(\eta_G\) is the **half-normalized** Dai–Wei eta in this formula. Substituting the full \(\eta_{\rm DW}\) into Theorem G would introduce a factor-two error.

With the link oriented as \(\partial\Omega\),
\[
\mathcal Q_+^\infty=-e+3\operatorname{sign}e,\qquad
\mathcal Q_-^\infty=e-3\operatorname{sign}e.
\tag{22}
\]
Writing \(e_{\rm out}=-e\) in the cap-boundary orientation gives
\[
\boxed{
c_\pm=T_\pm(C)\ \pm\
\bigl(e_{\rm out}-3\operatorname{sign}e_{\rm out}\bigr).
}
\tag{23}
\]

For \(e_{\rm out}=-1\), the **cap-oriented** charges are
\[
(\mathcal Q_+,\mathcal Q_-)=(-2,+2),
\tag{24}
\]
exactly the Step-33 Taub–NUT model. The opposite orientation gives \((+2,-2)\).

The supplied checks then agree:

- Taub–NUT, \(W^-=0\): \(c_+=2+2=4\).
- Taub–NUT, \(W^+=0\): \(c_+=2-2=0\).
- Taub-bolt: \(c_+=1+2=3\).
- Multi–Taub–NUT: \(c_+=(3-m)+(m-3)=0\).

The Taub–NUT table heading should be corrected: its displayed
\[
(8\pi^2)^{-1}\int|W^+|^2=1
\]
means \(C_+=4\), not \(C_+=1\). The JSON verifies algebraic substitutions, not the spectral or asymptotic theorem itself.

For a connected \(S^3\)-boundary cap with the stated Betti numbers,
\[
\chi=1+r,\qquad \tau=-r,\qquad T_+=2-r.
\]
Therefore
\[
\boxed{
c_+=
\begin{cases}
4-r,&e_{\rm out}=-1,\\
-r,&e_{\rm out}=+1.
\end{cases}}
\tag{25}
\]
Positivity excludes the second chirality for \(r>0\), and imposes \(r\le4\) in the first. The disk-bundle values \(4-p\) and \(p-2\) follow similarly from \((\chi,\tau)=(2,-1)\) and \(e_{\rm out}=\mp p\).

These evaluations require the stated fibred asymptotics, including vanishing collar corrections. An intrinsically collapsing Berger metric alone does not determine the charge of an uncontrolled collar.

## 6. Corrected Corollary 105.H

“Carries \(r_j\) classes” must mean that the cap has the stated topology, or at least
\[
(\chi,\tau)=(1+r_j,-r_j),
\]
with no additional contributions to these invariants.

Suppose there are \(N\) exceptional caps, \(\sum r_j=k\), and \(B\) additional ball caps of charge \(4\). Other ball caps have charge zero. Then
\[
C=\sum_{j=1}^N(4-r_j)+4B=4N-k+4B,
\]
so (19) becomes
\[
\boxed{k+32N+32B\le3A}.
\tag{26}
\]
The note’s equivalence with \(k+32N\le3A\) is correct only when \(B=0\); otherwise that formula is merely a weaker necessary condition.

When \(B=0\):

- singleton caps: \(N=k\), hence \(k\le A/11\);
- four-class caps: \(N=k/4\), hence \(k\le A/3\).

These are **necessary compatibility conditions**, not constructions. “Survives precisely” should be replaced by “is not excluded by this inequality.” Integer constraints and \(1\le r_j\le4\) remain, and actual degeneration geometry has not been established.

## 7. The zero-charge four-class cap

For \(\chi=5,\tau=-4,e_{\rm out}=-1\),
\[
T_+=-2,\qquad T_-=22.
\]
Using the cap-oriented charges (24),
\[
c_+=-2-(-2)=0,\qquad
\boxed{c_-=22-2=20}.
\tag{27}
\]
Thus, in the ordered cap limits,
\[
\int|W^+|^2\to0,\qquad
\int s^2\to0,\qquad
\int|\operatorname{Ric}^{\circ}|^2\to0,
\]
but
\[
\boxed{
\int|W^-|^2\to40\pi^2,\qquad
\frac1{8\pi^2}\int|W^-|^2\to5.
}
\tag{28}
\]
The cap is not energy-free in total curvature. Since its volume vanishes, its \(W^-\) curvature must concentrate.

If a suitable smooth pointed rescaling is independently obtained, scale invariance of these four-dimensional energies forces its smooth limit to satisfy
\[
\operatorname{Ric}=0,\qquad W^+=0.
\]
A simply connected such limit is hyperkähler: the connection on \(\Lambda^+\) is flat, giving a global parallel triple. It is spin and has even intersection pairing on compact cycles.

But (E) supplies neither a complete bubble-tree extraction nor topological accounting of the residual regions. It therefore does **not** prove that all curvature concentrations are classified smooth bubbles, that the remaining regions admit F-structures, or that their total curvature energy vanishes.

### Why even bubble lattices do not exclude \(-I_4\)

There is a concrete algebraic obstruction to the proposed inference:
\[
-D_4\subset-I_4,\qquad
D_4=\{x\in\mathbb Z^4:\ \sum_i x_i\equiv0\pmod2\},
\]
is an index-two even sublattice. Indeed,
\[
x^2=-\sum_i x_i^2\equiv\sum_i x_i\equiv0\pmod2
\quad(x\in D_4).
\]
For the characteristic vector \(K=(1,1,1,1)\) of \(-I_4\),
\[
K\cdot x\equiv0\pmod2\quad(x\in D_4).
\]
Thus spin pieces can detect an even sublattice while the full cap lattice is an odd index-two overlattice. The missing information can lie in integral gluing data; it need not be represented by a separately identifiable “odd collapsed region” or a non-simply-connected Ricci-flat piece.

A spin argument would work if an independently proved decomposition showed that compatible spin pieces and necks glue to a spin cap, or that an even lattice generates the full cap lattice integrally. Neither property follows from (E). The \(D_4\) inclusion is a possible lattice model, not a geometric realization.

### Eta and Dirac do not presently give an exclusion

The signature eta correction is already accounted for in (27); it yields no contradiction. A Dirac eta invariant additionally depends on spin/spin\(^c\) data, determinant connection, and limiting holonomy, none of which is specified by (E).

There is also no immediate closed spin\(^c\) index contradiction. Closing the cap by \(B^4\), the characteristic class \(K=(1,1,1,1)\) has
\[
K^2=-4,\qquad \sigma=-4,\qquad
\operatorname{ind}D_K^+=\frac{K^2-\sigma}{8}=0.
\]
Other characteristic classes do not supply an analytic contradiction without corresponding connection and spinor control. In particular, \(L^2\)-small scalar curvature is not a pointwise nonnegativity condition permitting a Lichnerowicz vanishing argument.

Consequently, **neither \(w_2\)/spin nor the supplied eta data exclude the four-class cap**. A noncircular exclusion requires new analytic and topological information—such as spin-compatible gluing, integral homology generation, or a controlled actual spin\(^c\)/monopole limit. The precise unresolved object is the realization or obstruction of a degeneration of
\[
\#4\overline{\mathbb{CP}}^2\setminus B^4
\]
with the specified Hopf-boundary charge and energy split (27)–(28). The verified identities constrain that object substantially, but do not decide its existence.