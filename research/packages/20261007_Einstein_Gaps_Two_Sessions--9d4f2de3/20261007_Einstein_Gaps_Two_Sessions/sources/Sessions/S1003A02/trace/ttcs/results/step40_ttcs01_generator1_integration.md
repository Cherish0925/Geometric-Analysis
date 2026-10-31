# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 40,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step40_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step40_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Research problem: for M = X # k CPbar^2 (X minimal general type, A=c_1^2(X)), is there c>0 with P(g)=int|Ric^o|^2 >= 8 pi^2 c k for every metric when 0<k<A/3 (LeBrun only gives k - A/3), or can metrics drive P/(8pi^2 k) to 0? The Step-40 note proves: the whole Seiberg-Witten saving equals (1/2) E int rho^2 |nabla n|^2_{W2} (Nijenhuis energy of the monopole almost-complex structures) minus nonnegative terms, equivalently Weyl rise W^+(n,n) > aligned value; and that every POINTWISE combination of the exact field identities is exhausted exactly at LeBrun's threshold (binding at uniform amplitude rho=3/2). The Step-38 note shows the exceptional charge of a sign flip lives in the anti-self-dual relative curvature h^- and that paired zeros unwind through S^3. Propose the strongest concrete mathematical mechanisms (with equations, not slogans) that could supply k-dependence through genuinely global or differential information: e.g. localization of Nijenhuis energy by the fixed 4pi^2 of h^- near a 2-cycle dual to E_i, elliptic/Bochner estimates for the SW almost-complex structure, harmonic-projection J_epsilon terms, the zeta (Lee-form) cost, or integral constraints across the 2^k sign family. For each, state the precise inequality to prove, why it could hold, which test object (certified perpendicular cell with saving 0.43%, Kaehler blow-ups, diffuse-rotation metrics) could falsify it, and its cheapest decisive check. Equally, construct the most plausible counter-mechanism: a family where Nijenhuis rotation at density ~1 over volume ~10 pi^2 (1-c) per class has o(k) Walsh and zeta cost, and say what geometric construction might realize it.

## Integrated Scientific Memo

## Integrated scientific memo

Let
\[
M=X\#k\overline{\mathbf{CP}}^{\,2},\qquad A=c_1^2(X),\qquad 0<k<A/3,
\]
and normalize to the scalar-\(-4\) Yamabe representative. Put
\[
\mathfrak S(g)=8\pi^2k-P(g),\qquad P(g)=\int_M|\Ric_g^\circ|^2.
\]
Step 40 gives the exact obstruction:
\[
\mathfrak S=
\frac12\mathbb E_\epsilon\int\rho_\epsilon^2
|\nabla n_\epsilon|_{\mathcal W_2}^2-\mathcal R,
\tag{1}
\]
where
\[
\begin{aligned}
\mathcal R={}&
\mathbb E_\epsilon\int
\frac{(2-\rho_\epsilon)^2(2+2\rho_\epsilon-\rho_\epsilon^2)}6\\
&+\mathbb E_\epsilon\int
\rho_\epsilon\bigl(|a_\epsilon|^2+5|b_\epsilon|^2
-2\langle a_\epsilon,J'b_\epsilon\rangle\bigr)
+4\mathbb E_\epsilon\|M_\epsilon\|_2^2+\mathcal W
\ge0 .
\end{aligned}
\tag{2}
\]
Thus a universal \(c>0\) would follow from the differential/global estimate
\[
\boxed{\quad
\frac12\mathbb E_\epsilon\int\rho_\epsilon^2
|\nabla n_\epsilon|_{\mathcal W_2}^2
\le \mathcal R+C\,P(g)
\quad}
\tag{3}
\]
with a uniform finite \(C\), since then
\[
P(g)\ge \frac{8\pi^2}{1+C}\,k.
\tag{4}
\]
No pointwise manipulation can prove (3): Step 40 shows exact exhaustion at \(t=2/3\), binding at \(\rho=3/2\).

The viable mechanisms divide into two logically distinct tasks:

1. locate and account for the topology-carrying relative defects;
2. control the **common** diffuse Nijenhuis mode, which can be almost independent of the sign vector.

The fixed \(4\pi^2\) in \(h^-\) addresses only the first.

---

# 1. Relative Berry curvature: the sharpest link between \(E_i\) and spinor rotation

On \(\{\Phi_\epsilon\neq0\}\), write
\[
\Phi_\epsilon=\sqrt{\rho_\epsilon}\,u_\epsilon,\qquad
\nabla_{\mathcal A_\epsilon}u_\epsilon
=i\beta_\epsilon u_\epsilon+v_\epsilon u_\epsilon^\perp.
\]
In a unitary frame \((u_\epsilon,u_\epsilon^\perp)\), the diagonal curvature entry has the form
\[
\langle u_\epsilon,F_{\nabla^{S^+_{\epsilon}}}u_\epsilon\rangle
=i\,d\beta_\epsilon-\bar v_\epsilon\wedge v_\epsilon.
\]
After separating determinant and Levi–Civita curvature, this gives, up to the fixed sign convention,
\[
\boxed{\quad
\frac12f_\epsilon=d\beta_\epsilon-r(n_\epsilon)-B_\epsilon,
\qquad
B_\epsilon=-i\bar v_\epsilon\wedge v_\epsilon .
\quad}
\tag{5}
\]
The convention-independent estimates are
\[
|r(n_\epsilon)^-|\le C|\Ric^\circ|,
\qquad
|B_\epsilon|\le C|\nabla n_\epsilon|^2 .
\tag{6}
\]
Here \(W^-\) does not enter the anti-self-dual curvature block acting on \(S^+\); that block is controlled by \(\Ric^\circ\).

For one flip \(\epsilon'=\epsilon\oplus i\),
\[
h_i^\epsilon=\frac{f_\epsilon-f_{\epsilon'}}2,\qquad
\left[\frac{h_i^\epsilon}{2\pi}\right]=\pm E_i,
\]
and
\[
\|h_i^-\|_2^2-\|h_i^+\|_2^2=4\pi^2.
\tag{7}
\]
Subtracting (5) gives
\[
h_i^\epsilon
=d(\beta_\epsilon-\beta_{\epsilon'})
-\bigl[r(n_\epsilon)-r(n_{\epsilon'})\bigr]
-\bigl[B_\epsilon-B_{\epsilon'}\bigr].
\tag{8}
\]
Thus if \(P\) and Lee costs are small, the exceptional class must be represented by concentrated differences of the quadratic Berry curvatures \(B_\epsilon\).

A first defensible target, initially away from spinor zeros, is
\[
\boxed{\quad
k\le C\left[
P+\mathbb E_\epsilon\int|\nabla n_\epsilon|^4
+\text{zero-set/Lee contributions}
\right].
\quad}
\tag{9}
\]
It follows by harmonic projection of the singleton Walsh components of (5), using
\[
\sum_{i=1}^k\|(f_{\{i\}})_H^-\|_2^2\ge4\pi^2k.
\]
The zero-set terms are essential: \(d\beta\) may have nontrivial phase currents around zeros and cannot simply be discarded.

### Why (9) is not yet a tariff

A defect supported in a four-ball of radius \(r\), with order-one rotation, has
\[
\int|\nabla n|^4=O(1),\qquad
\int|\nabla n|^2=O(r^2).
\tag{10}
\]
Therefore the fixed exceptional charge can survive while the Nijenhuis contribution to the saving tends to zero. This is useful localization information but does not control diffuse common rotation.

The stronger localization statement needed is: there exist marked defect regions \(U_i\) with radii \(r_i\) such that
\[
\sum_i\int_{U_i}|B_{\epsilon,i}|^2\gtrsim k,\qquad
\mathbb E_\epsilon\int_{\cup U_i}\rho_\epsilon^2
|\nabla n_\epsilon|_{\mathcal W_2}^2
\le C\sum_i r_i^2,
\tag{11}
\]
and, on the complement,
\[
\boxed{\quad
\frac12\mathbb E_\epsilon
\int_{M\setminus\cup U_i}\rho_\epsilon^2
|\nabla n_\epsilon|_{\mathcal W_2}^2
\le
\mathcal R(M\setminus\cup U_i)+CP+o(k).
\quad}
\tag{12}
\]
Equations (11)–(12) imply (3) whenever \(\sum r_i^2=o(k)\).

### Falsifiers and cheapest check

- **Kähler blow-ups:** should exhibit concentrated relative charge but zero Nijenhuis energy. They test consistency, not positivity.
- **Certified perpendicular cell:** tests whether saving occurs in a macroscopic collar separated from the topology-carrying core.
- **Diffuse common rotation plus tiny relative defects:** directly falsifies (12) while remaining compatible with (9).

The cheapest rigorous check is first to derive (5) in the exact Step-40 Clifford convention. The first meaningful numerical check requires actual closed-manifold monopoles; the failed isolated-cell shooting problem does not provide them.

---

# 2. Cutoff Bochner estimates: useful only if the annular term is topologically forced

For \(\psi_\epsilon=\rho_\epsilon n_\epsilon\), Step 40 gives
\[
\begin{aligned}
\int|\nabla\psi_\epsilon|^2
={}&2\|d\psi_\epsilon\|_2^2
+2\int M_\epsilon(\psi_\epsilon,\psi_\epsilon)
+\int\frac{\rho_\epsilon^2}{3}(4-\rho_\epsilon^2),\\
|d\psi_\epsilon|^2={}&2\rho_\epsilon|b_\epsilon|^2,
\end{aligned}
\tag{13}
\]
and
\[
|\nabla\psi_\epsilon|^2
=4\rho_\epsilon|a_\epsilon|^2
+\rho_\epsilon^2|\nabla n_\epsilon|_{\mathcal W_2}^2
+2\rho_\epsilon|a_\epsilon+J'b_\epsilon|^2.
\tag{14}
\]
A cutoff \(\chi_i\) supported near the \(i\)-th marked region yields an estimate of the form
\[
\boxed{
\begin{aligned}
\int\chi_i\rho_\epsilon^2|\nabla n_\epsilon|_{\mathcal W_2}^2
\le{}&
C\int\chi_i\Bigl(
|M_\epsilon|^2+|\zeta_\epsilon|^2+(2-\rho_\epsilon)^2
\Bigr)\\
&+C\int |\psi_\epsilon|^2|\nabla\chi_i|^2 .
\end{aligned}}
\tag{15}
\]
This is a valid differential mechanism, but the last term is not automatically quantized by the ASD class \(E_i\). Step 38 shows why: the exceptional charge lies in \(h_i^-\), whereas \(\psi_\epsilon\) and the cutoff term are self-dual data.

Accordingly, the missing proposition is not merely (15), but
\[
\boxed{\quad
\sum_i\mathbb E_\epsilon
\int|\psi_\epsilon|^2|\nabla\chi_i|^2
\le
CP+\text{terms absorbable in }\mathcal R+o(k),
\quad}
\tag{16}
\]
or an opposite lower bound that enters a marked-core tariff. Neither follows from Chern–Weil alone.

### Falsifiers and cheapest check

For a tube of radius \(r\) around an exceptional sphere of area \(A_E\),
\[
\int|\nabla n|^2=O(A_E),\qquad
\int|w|^2=O(A_Er^2).
\tag{17}
\]
Hence shrinking-area perpendicular cells can make the annulus contribution vanish while retaining the fixed \(4\pi^2\) in \(h^-\). Computing the cutoff residual of (15) across nested tubes in the certified cell is the cheapest decisive test. If it scales to zero with \(A_E\), this route cannot alone provide uniform \(c\).

---

# 3. Harmonic projection and Lee cost: the inequality direction matters

For each field,
\[
J_\epsilon
=\|f_\epsilon^+-(f_\epsilon^+)_H\|_2^2
=\frac12\int\rho_\epsilon^2-4\pi^2p_\epsilon ,
\tag{18}
\]
and
\[
\mathcal W
=8\pi^2(\mathbb E_\epsilon p_\epsilon-A)
+2\mathbb E_\epsilon J_\epsilon.
\tag{19}
\]
Combining these gives the exact identity
\[
\boxed{\quad
\mathcal W=
\mathbb E_\epsilon\int\rho_\epsilon^2-8\pi^2A.
\quad}
\tag{20}
\]
Thus
\[
\mathbb E_\epsilon\int\rho_\epsilon^2\ge8\pi^2A.
\tag{21}
\]
Since \(0\le\rho\le2\),
\[
4V\ge\mathbb E_\epsilon\int\rho_\epsilon^2
=8\pi^2A+\mathcal W,
\tag{22}
\]
equivalently
\[
\boxed{\quad
V\ge2\pi^2A+\frac14\mathcal W.
\quad}
\tag{23}
\]
An expression involving \(\int(4-\rho^2)\) must be handled carefully because
\[
\mathbb E\int(4-\rho^2)=4V-8\pi^2A-\mathcal W
\tag{24}
\]
is an identity, not an additional positive correction to (23). It cannot be counted again as an independent scalar-volume tariff.

The Hodge spectral estimate also has a definite direction. Since \(f_\epsilon^+-(f_\epsilon^+)_H\) is orthogonal to harmonic forms,
\[
\lambda_1 J_\epsilon
\le \|df_\epsilon^+\|_2^2+\|d^*f_\epsilon^+\|_2^2.
\tag{25}
\]
Thus
\[
\boxed{\quad
J_\epsilon\le \lambda_1^{-1}
\bigl(\|df_\epsilon^+\|_2^2+\|d^*f_\epsilon^+\|_2^2\bigr),
\quad}
\tag{26}
\]
not \(J_\epsilon\ge\lambda_1^{-1}\|d^*f_\epsilon^+\|^2\). Using the SW identities, the right side is controlled by Lee/amplitude derivatives. Consequently, small Lee cost plus a uniform Hodge spectral gap forces \(f_\epsilon^+\) close to harmonic, but this does **not** control the free Nijenhuis mode: a harmonic self-dual form can define a nonintegrable almost-Kähler structure.

A useful global theorem would therefore need the reverse geometric input
\[
\boxed{\quad
\mathbb E_\epsilon\int\rho_\epsilon^2
|\nabla n_\epsilon|_{\mathcal W_2}^2
\le
C\bigl(P+\mathbb E J_\epsilon+\text{amplitude/Lee terms}\bigr),
\quad}
\tag{27}
\]
under noncollapse and a uniform spectral gap. Without such hypotheses, long-neck and collapsing metrics can make \(\lambda_1\to0\).

### Falsifiers and cheapest check

- Kähler blow-ups have \(J=0\) and no Nijenhuis energy.
- A diffuse harmonic almost-Kähler form with nonzero Nijenhuis tensor falsifies any claim that \(J\) alone prices rotation.
- The cheapest check is the constrained scalar optimization using (20), the exact Step-40 polynomials, and the closed Weyl-volume identity. Because Theorem E already combines the available pointwise and integral mass information, one should expect no improvement unless a genuine spectral or localization constraint is added.

---

# 4. Lee-form periods: conditional on suppressing \(S^3\)-unwinding

For a pair differing at \(E_i\), define
\[
u_{\epsilon\epsilon'}=\langle\Phi_{\epsilon'},\Phi_\epsilon\rangle,
\qquad
w_{\epsilon\epsilon'}=\Phi_\epsilon\wedge\Phi_{\epsilon'}.
\]
Then \(c_1(u)=\pm E_i\), but
\[
q=(u,w)\in N^*\oplus D,\qquad |q|^2=\rho_\epsilon\rho_{\epsilon'},
\]
and \(c_2(N^*\oplus D)=0\). Where both spinors are nonzero, \(q/|q|\in S^3\); hence the phase winding of \(u\) can unwind through \(w\), since \(\pi_1(S^3)=0\).

A Lee-period estimate is therefore valid only under a quantitative polarization hypothesis such as
\[
|w_{\epsilon\epsilon'}|
\le\delta\sqrt{\rho_\epsilon\rho_{\epsilon'}}
\quad\text{on a linking annulus},\qquad \delta<1.
\tag{28}
\]
Then \(u\) stays nonzero there and has a well-defined phase degree. A capacity inequality could take the form
\[
\boxed{\quad
\int_{\mathcal A_i}
|\zeta_\epsilon-\zeta_{\epsilon'}|^2
\ge
4\pi^2\,\mathrm{Cap}(\mathcal A_i)
-O\!\left(\int_{\mathcal A_i}|w_{\epsilon\epsilon'}|^2\right).
\quad}
\tag{29}
\]
Summing over separated annuli would yield an \(\Omega(k)\) Lee cost if their capacities have a uniform lower bound.

### Falsifiers and cheapest check

The direct falsifier is exactly the Step-38 mechanism: \(u\) crosses zero through a region where \(w\) is large, destroying the \(S^1\) degree. Long thin tubes also make capacity tend to zero. The cheapest check on the certified cell is to measure simultaneously:

- the phase degree of \(u\) on linking circles;
- \(\int|w|^2\) where \(u\) is small;
- the annular capacity.

A missing phase period accompanied by \(w\)-dominance rules out this mechanism for that geometry.

---

# 5. The \(2^k\) sign family: edge energy alone does not imply Walsh energy of order \(k\)

The self-dual curvatures have the Walsh expansion
\[
f_\epsilon^+=\sum_I\chi_I(\epsilon)f_I^+,
\qquad \chi_I(\epsilon)=\prod_{i\in I}\epsilon_i.
\tag{30}
\]
For hypercube edges,
\[
\boxed{\quad
\sum_{i=1}^k\mathbb E_\epsilon
\|f_\epsilon^+-f_{\epsilon^{(i)}}^+\|_2^2
=
4\sum_{I\ne\varnothing}|I|\,\|f_I^+\|_2^2.
\quad}
\tag{31}
\]
But the cost identity contains
\[
2\sum_{I\ne\varnothing}\|f_I^+\|_2^2,
\tag{32}
\]
without the factor \(|I|\). Therefore a lower bound of constant size on every edge only yields a lower bound on the degree-weighted Fourier mass; it may concentrate at high Walsh degree and give merely \(O(1)\) unweighted mass.

A sufficient global inequality must either use all pairs,
\[
\boxed{
\begin{aligned}
&\|h_{\epsilon\epsilon'}^+\|_2^2
+\mathcal C_{\epsilon\epsilon'}^{\rm amp}
+\mathcal C_{\epsilon\epsilon'}^{\rm Lee}
+CP\\
&\hspace{4em}\ge
\eta\,4\pi^2\,d_H(\epsilon,\epsilon'),
\end{aligned}}
\tag{33}
\]
or prove a low-degree theorem
\[
\boxed{\quad
\sum_{|I|\ge2}|I|\,\|f_I^+\|_2^2
\le C\sum_i\|f_{\{i\}}^+\|_2^2
+\text{absorbable terms}.
\quad}
\tag{34}
\]
Averaging (33) uses
\[
\mathbb E_{\epsilon,\epsilon'}d_H(\epsilon,\epsilon')=\frac k2
\tag{35}
\]
and avoids the Fourier-degree loss.

Neither (33) nor (34) follows from topology. The paired zero can be arbitrarily thin, and the exceptional charge remains in \(h^-\).

### Falsifiers and cheapest check

A coordinated family
\[
f_\epsilon^+=f_0^++\sum_i\epsilon_i\beta_i+\text{high-degree terms},
\qquad
\|\beta_i\|_2=o(1),\quad
\|\nabla\beta_i\|_2=O(1),
\tag{36}
\]
can have small Walsh cost but substantial rotational energy. The decisive diagnostics on any closed numerical example are:

- unweighted Walsh mass \(\sum_{I\ne\varnothing}\|f_I^+\|^2\);
- degree-weighted mass \(\sum |I|\|f_I^+\|^2\);
- all-pairs distance versus Hamming distance;
- locations of amplitude zeros and \(u\)-to-\(w\) unwinding.

---

# 6. Whole marked cores: the strongest geometric route to a positive tariff

For a connected negative-definite ALE core \(N\),
\[
\begin{aligned}
P_N={}&8\pi^2m+32\pi^2r
+16\pi^2(e-2+q_\infty)-24\pi^2\eta_\infty\\
&+4W_N^++\frac1{12}S_N.
\end{aligned}
\tag{37}
\]
For a whole AE core,
\[
P_N
=8\pi^2b_2(N)+32\pi^2(b_1(N)+e-1)
+4W_N^++\frac1{12}S_N.
\tag{38}
\]
Thus one-ended, \(b_1=0\), negative-definite whole AE cores obey
\[
P_N\ge8\pi^2b_2(N).
\tag{39}
\]
Terminal ALE bubbles do not: Eguchi–Hanson has \(b_2=1\) and \(P_N=0\). End corrections must be telescoped through the entire marked bubble tree before assigning a cost to an exceptional class.

For a compact marked region \(U\) with outer \(S^3\), \(\chi(U)=m+1\), and \(\tau(U)=-m\), the relative formula has the form
\[
\boxed{\quad
P_U=8\pi^2m+4W_U^++\frac1{12}S_U+\mathcal T_U,
\quad}
\tag{40}
\]
where \(\mathcal T_U\) is the sum of Gauss–Bonnet and signature boundary transgressions, normalized so that \(\mathcal T_U\to0\) for a Euclidean outer marking.

A positive tariff follows from the marked-core statement
\[
\sum_\nu m_\nu=k_{\rm core},\qquad
\sum_\nu(\mathcal T_{U_\nu})_-=o(k),
\tag{41}
\]
together with
\[
\sum_\nu P_{U_\nu}\ge8\pi^2c_0k_{\rm core}-o(k)
\tag{42}
\]
and a bulk estimate controlling the remaining classes by (27) or (12).

The key point is that arbitrary outer cuts are useless: enlarging a region through an Einstein background changes the boundary transgression despite adding no \(P\). The correct object is a complete marked core with its outer geometry retained.

### Falsifiers and cheapest check

- Burns cores support the unit tariff.
- Eguchi–Hanson falsifies any tariff assigned to terminal ALE pieces without end corrections.
- The perpendicular cell tests whether the \(0.43\%\) saving lies in the topology-carrying core or a macroscopic collar.

The cheapest check needs no monopoles: evaluate (40) on nested outer hypersurfaces of the certified cell and locate where the negative transgression responsible for the saving occurs.

---

# 7. Bulk Einstein coercivity: the correct target for common diffuse rotation

The hardest saving mode may be common to almost all signs and therefore invisible to relative topology. For constant amplitude \(\rho=r>0\), \(\zeta=0\), and \(d\psi=0\),
\[
|\nabla n|^2=2(2-r),
\qquad
\nabla^*\nabla n=2W^+n+\frac43n,
\]
hence
\[
\boxed{\quad
W^+(n,n)=\frac43-r.
\quad}
\tag{43}
\]
This is a genuine almost-Kähler channel. Pricing it by \(P\) is closely related to quantitative rigidity for negatively curved Einstein almost-Kähler geometry.

Near an Einstein Kähler metric \(g_0\), in transverse-traceless gauge,
\[
D\Ric^\circ_{g_0}[H]
=\mathcal L_EH
=\frac12(\nabla^*\nabla H-2\mathring RH),
\tag{44}
\]
and
\[
P(g_0+tH)=t^2\|\mathcal L_EH\|_2^2+O(t^3).
\tag{45}
\]
Let \(\mathcal TH\) be the linearized Nijenhuis tensor in the compatible almost-Kähler sector. The decisive spectral quantity is
\[
\boxed{\quad
C_{\rm AK}(g_0)=
\sup_{H\perp\{\text{gauge, KE moduli}\}}
\frac{\|\mathcal TH\|_2^2}{\|\mathcal L_EH\|_2^2}.
\quad}
\tag{46}
\]
A uniform finite bound, plus nonlinear elliptic control, would yield on the regular bulk
\[
\boxed{\quad
\mathcal N_B
\le C P_B+
C\bigl(\mathcal R_{\rm amp,B}
+\mathcal R_{\rm Lee,B}
+\mathcal R_{\rm align,B}\bigr),
\quad}
\tag{47}
\]
with constants needing to be sharp enough for absorption into (2).

The obstruction is a sequence
\[
\|\mathcal TH_j\|_2=1,\qquad
\|\mathcal L_EH_j\|_2\to0.
\tag{48}
\]
Such soft torsion modes are most plausible on large covers, long regions, or collapsing geometries.

The cheapest decisive test is a spectral computation of (46) on the complex-hyperbolic model and relevant covering families. The certified cell lies outside the perturbative regime; diffuse-rotation metrics are the direct nonlinear falsifier.

---

# 8. Most plausible counter-mechanism

The strongest formal counterexample is not \(k\) disjoint order-one rotations; it is a **shallow common rotation spread over the \(O(A)\) host volume**, plus small sign-dependent defects carrying the exceptional classes.

Consider a formal common-mode state with
\[
\rho=r,\qquad \zeta=0,\qquad
W^+n=\left(\frac43-r\right)n,
\tag{49}
\]
and the two remaining Weyl eigenvalues equal. Then
\[
|\nabla n|^2=2(2-r),\qquad
|W^+|^2=\frac32\left(\frac43-r\right)^2.
\tag{50}
\]
If the Walsh and harmonic-projection excesses are negligible,
\[
r^2V=8\pi^2A.
\tag{51}
\]
Substitution into the closed curvature identity gives
\[
\boxed{\quad
\frac{P}{8\pi^2}
=k-A\beta(r),\qquad
\beta(r)=\frac{16}{r}-5-\frac{12}{r^2}.
\quad}
\tag{52}
\]
The pointwise saving density is
\[
\boxed{\quad
16r-5r^2-12
=\frac45-5\left(r-\frac85\right)^2.
\quad}
\tag{53}
\]
Hence:

- \(r=3/2\) gives \(\beta=1/3\), the LeBrun threshold;
- \(r=8/5\) gives the maximum density \(4/5\), requiring volume
  \[
  10\pi^2(1-c)k
  \tag{54}
  \]
  for saving \(8\pi^2(1-c)k\);
- for \(h=k/A\to0\), the equation \(\beta(r)=h\) has
  \[
  r=2-h+O(h^2).
  \tag{55}
  \]
Then
\[
|\nabla n|^2=2h+O(h^2),\qquad
V=2\pi^2A+O(k),
\tag{56}
\]
while amplitude and Weyl-alignment penalties are
\[
O(Ah^2)=O(kh)=o(k).
\tag{57}
\]
This is exactly the sought family with order-\(k\) Nijenhuis saving and \(o(k)\) local penalties.

The sign structures cannot coincide globally, because their determinant classes differ. The plausible realization is:

1. a common diffuse almost-Kähler structure over most of \(M\);
2. tiny sign-dependent defects \(U_i\) carrying \([h_i/(2\pi)]=\pm E_i\) in \(h_i^-\);
3. relative inner-product zeros unwinding through \(w_i\), so there is no forced Lee period;
4. defect scales satisfying
   \[
   \sum_i r_i^2=o(k),
   \tag{58}
   \]
   making Walsh and Lee costs sublinear.

A formal curvature ansatz is
\[
f_\epsilon=f_0+\sum_i\epsilon_i\eta_i+\beta_\epsilon,
\tag{59}
\]
where each \(\eta_i\) is predominantly ASD with
\[
[\eta_i/(2\pi)]=E_i,\qquad \|\eta_i^-\|_2^2\approx4\pi^2,
\tag{60}
\]
and \(\beta_\epsilon^+\) is small in \(L^2\) but adjusts the common self-dual field to the SW equation. The topology then sits in the ASD sector, while the saving sits in a common self-dual Nijenhuis mode.

### Geometric carriers

Ordinary Burns cores cannot realize \(P=o(k)\): each already contributes approximately \(8\pi^2\), and exterior geometry cannot cancel a nonnegative \(P\)-integral. The topology carriers must instead have vanishing or subunit Ricci cost before completion.

Two plausible sources are:

- quotient-ended or collapsed cores whose characteristic corrections cancel the \(8\pi^2\) topological term;
- ALF bolt geometries, such as a Ricci-flat Taub-bolt-type core with a square-\(-1\) bolt, retained through a long collapsed transition rather than completed immediately to an AE end.

The decisive quantity is not the Ricci energy of the isolated ALF core but the cost of completing it inside a closed manifold:
\[
\boxed{\quad
P_{\rm transition}=o(1)
\quad\text{per exceptional class}.
\quad}
\tag{61}
\]
If every smooth completion to the ambient geometry costs a fixed positive amount, a tariff survives. If collapsed transitions satisfying (61) exist while maintaining the diffuse common mode, then \(P/(8\pi^2k)\to0\) becomes plausible.

For the ramified/complex-hyperbolic route, isolated invariant monopole shooting is not decisive: a closed monopole need not restrict to the symmetric cell solution. The correct construction problem is metric-geometric first—build closed cells/cores and transitions with controlled \(P\)—then solve or estimate the actual closed SW fields.

---

# 9. Decisive mathematical alternatives

The positive-gap mechanism can be stated compactly as the conjunction
\[
\boxed{
\begin{gathered}
\text{marked whole-core accounting for the topology,}\\
\text{Berry localization of relative defects,}\\
\text{bulk coercivity for common Nijenhuis rotation.}
\end{gathered}}
\tag{62}
\]
A theorem of the following form would suffice:
\[
P_{\rm cores}\ge8\pi^2c_0k_{\rm core}-o(k),
\qquad
\frac12\mathcal N_{\rm bulk}
\le\mathcal R_{\rm bulk}+C P_{\rm bulk}+o(k),
\tag{63}
\]
with all remaining exceptional classes assigned either to cores or to bulk defects. Then \(P\ge8\pi^2c\,k-o(k)\) for some explicit \(c>0\).

The counter-mechanism requires all three failures:
\[
\boxed{
\begin{gathered}
\text{low-cost non-AE/collapsed topology carriers,}\\
\text{a soft common almost-Kähler torsion mode,}\\
\mathcal W+\mathbb E\|\zeta\|^2=o(k)
\text{ via thin }S^3\text{-unwinding defects}.
\end{gathered}}
\tag{64}
\]

The cheapest decisive investigations are therefore:

1. **Derive the projective-spinor curvature identity (5)** and its zero-current correction rigorously.
2. **Telescope boundary corrections on the certified cell** to determine whether its \(0.43\%\) saving is a core or collar effect.
3. **Compute the bulk torsion quotient (46)** on complex-hyperbolic models and large covers.
4. **Compute ALF-to-ambient transition energy**, testing (61).
5. On any closed monopole computation, record unweighted and degree-weighted Walsh mass, \(J_\epsilon\), Lee energy, and \(u/w\) unwinding; isolated cell ODE data are insufficient.

At present the supplied identities do not decide whether a universal \(c>0\) exists. They do identify the exact unresolved object: a uniform coercive coupling between common Nijenhuis rotation and either Ricci energy or the nonnegative Step-40 remainder, after the topology-carrying defects and their outer markings have been separated.