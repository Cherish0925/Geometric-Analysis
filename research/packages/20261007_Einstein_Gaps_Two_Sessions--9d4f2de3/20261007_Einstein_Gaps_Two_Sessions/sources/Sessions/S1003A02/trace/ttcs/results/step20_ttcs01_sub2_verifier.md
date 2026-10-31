# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Sessions/S1003A02/workspace/scripts/burns_transgression_flux.py",
    "Sessions/S1003A02/workspace/data/burns_transgression_flux.json"
  ]
}
```

## Task

Verify Theorem F (first-order Burns blow-up response for a general closed bulk) in Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md, Section 1, together with the exact flux computation in burns_transgression_flux.py and its output JSON. Claim: gluing the Burns metric delta + x0 h (Kaehler potential |z|^2 + x0 log|z|^2) into g-normal coordinates at p with cutoff radius r0 = x0^{1/5} gives P(ghat) = P(g) + 8 pi^2 (1 - x0 R^+_p(zeta,zeta)) + O(x0^{6/5}), with R^+ = W^+ + s/12 on Lambda^+ in endomorphism norm conventions. Check carefully: (1) the exact topological reduction P(ghat)-P(g)-8pi^2 = 4 Delta W^+ + Delta S/12; (2) whether the inner-region estimate |W^+(ghat)-W^+(g)| <= C min(1, x0/r^2) is valid (bilinear structure, pointwise vanishing of the linearized self-dual curvature of the tail, behavior near the exceptional curve), and hence why no first-order term comes from the inner region; (3) the cut-annulus expansion and that the flux Phi = -int P+ R^lin(chi h) P+ is cutoff independent and is computed correctly by the script (sign of curvature convention, the replacement of d_a d_b f by oint n_a d_b f on the inner sphere, the 1/4 normalization of Lambda^2 pairing, orientation of Lambda^+ for omega = dx12+dx34); (4) that -8 x0 <R^+_p, Phi> equals -8 pi^2 x0 R^+(zeta,zeta) given Phi^{++} = pi^2 w1 w1^T; (5) the consistency checks with Kaehler topology (scalar flux 4 pi^2 x0 = 4 pi area(E), area = pi x0) and with the complex-space-form slopes +6/0/-6 at s=-24. Also check the neck-quantization Lemma Q' (Section 2) and the proportionality rigidity Lemma R (Section 3) for correctness of the Chern-Weil bookkeeping (chi(U)<=2 via Mayer-Vietoris, boundary terms, CH densities 6/pi^2 and 2/pi^2). Report any error, missing hypothesis or wrong constant precisely, and whether each statement is proved as stated.

## Output

# Verification memo: Theorem F, the Burns flux script, and Lemmas Q, Q′, R (Step 20)

## Results at a glance

| Item | Result |
|---|---|
| (1) Topological reduction | Correct and exact. |
| (2) Inner-region estimate | Correct. The mixed-difference argument works only for \(|y|\ge1\); near the exceptional curve \(E\) a separate bounded-geometry argument is needed. That argument is sketched in the note and goes through. |
| (3) Cut annulus and flux | Correct. I re-derived \(\Phi^{++},\Phi^{--},\Phi^{+-}\) by hand, independently of the script, and they agree with the JSON. |
| (4) Assembly | Correct. |
| (5) Consistency checks | The Kähler check and the space-form slopes pass. The written Kähler formula contains a factor-\(\pi\) typo. |
| Lemma Q, Q′ | Correct. In Q′, \(\chi(U)=2\) holds exactly. The \(\eta\)/Chern–Simons term on Σ needs one sentence of justification, supplied below. |
| Lemma R | Correct as stated. The "Consequence" paragraph applies it to all \((k,\ell)\), but the Chern–Weil argument gives nothing when \(\ell=2k\). A convexity argument covers every nontrivial cell. |

**Theorem F is proved as stated.** The remainder can be improved to \(O(x_0^{4/3})\).

---

## 1. Topological reduction (item 1)

Gauss–Bonnet with endomorphism norms reads \(8\pi^2\chi=\int(|W|^2-\tfrac12|\mathrm{Ric}^\circ|^2+s^2/24)\). This is the tensor-norm form \(32\pi^2\chi=\int(|W|_t^2-2|\mathrm{Ric}^\circ|^2+s^2/6)\) with \(|W|_t^2=4|W|^2_{\rm end}\).

Eliminating \(W^-\) with the signature formula gives
\[
P=4\!\int|W^+|^2+\tfrac1{12}\!\int s^2-16\pi^2\chi-24\pi^2\tau .
\]
With \(\Delta\chi=+1\) and \(\Delta\tau=-1\), the topological part changes by \(-16\pi^2+24\pi^2=8\pi^2\). Hence
\[
\Delta P-8\pi^2=4\Delta W^++\Delta S/12
\]
exactly.

The normalizations also hold up on \(\mathbb{CH}^2\) (\(s=-24\)). There \(W^+=\mathrm{diag}(-4,2,2)\), \(|W^+|^2=24\) and \(s^2/24=24\). The densities are \(48/8\pi^2=6/\pi^2\) and \(24/12\pi^2=2/\pi^2\), and these agree with Hirzebruch proportionality: \(\chi(\mathbb{CP}^2)/\mathrm{Vol}_{FS}=3/(\pi^2/2)\).

## 2. Burns metric facts

- **Exact form.** \((i/2)\partial\bar\partial\log|z|^2\) is the metric \(t^{-2}(\delta-\Pi_{\mathrm{span}(x,Jx)})\), and \(\Pi=(xx^T+JxJx^T)/t^2\). So \(B=\delta+x_0h\) holds exactly.
- **Exceptional area.** The radial and \(Jx\) directions carry \(dt^2+t^2\sigma_3^2\). The base \(\sigma_1^2+\sigma_2^2\) is \(S^2(1/2)\), of area \(\pi\). Hence \(\mathrm{area}(E)=\pi x_0\).
- **Scaling.** \(h\) is homogeneous of degree \(-2\), so \(B_{x_0}=x_0\,(y\mapsto B_1)\) with \(y=x/\sqrt{x_0}\).
- **Orientation.** \(\omega=e^{12}+e^{34}\in\Lambda^+\) for \(dx^{1234}\). The script's basis \(e^{12}+e^{34},\ e^{13}+e^{42},\ e^{14}+e^{23}\) is self-dual; I checked \(*e^{13}=-e^{24}\) and \(*e^{14}=e^{23}\). The pointwise vanishing of the \(P_+\)-block confirms that Burns is ASD in this orientation.
- **Smoothness and positivity.** \(B\) and \(\pi^*g\) are smooth on the blow-up, so \(h\) is too. Positivity holds because \(k\ge -Cr^2\delta\ge -Cr^2B\).
- **Linearized self-dual curvature of the tail.** It vanishes because \(W^+(\delta+x_0h)=s(\delta+x_0h)=0\) for all small \(x_0\) at fixed \(t>0\), and this expression is analytic in \(x_0\). It also vanishes for \(x_0<0\) locally, which is not needed. The note's word "affine" refers to the metric, not to the curvature.

## 3. Inner region (item 2)

**Region \(|y|\ge1\).** Here \(h\) and its derivatives are bounded in the Cartesian \(y\)-chart. The mixed second difference \(f(\delta+a+b)-f(\delta+a)-f(\delta+b)+f(\delta)\), with \(a=h\) and \(b=\tilde k\), is a sum of terms containing at least one \(a\)-factor and one \(b\)-factor. The dominant terms are
\[
\partial^2h\cdot\tilde k,\quad \partial h\cdot\partial\tilde k,\quad h\cdot\partial^2\tilde k\ \sim\ x_0|y|^{-2}.
\]
The terms with extra factors are \(\lesssim x_0^2\le x_0|y|^{-2}\) for \(|y|\le r_0/\sqrt{x_0}\). The function \(f\) is evaluated only at metrics uniformly equivalent to \(\delta\).

Since \(W^+(\delta+\tilde k)=x_0W^+(g)\) and \(W^+(B_1)=W^+(\delta)=0\), we get
\[
|\omega|\le x_0^{-1}\cdot Cx_0|y|^{-2}=Cx_0/r^2 .
\]

**Region \(|y|\le1\).** The Cartesian argument does not apply here: \(h\sim|y|^{-2}\) and the chart is singular at \(E\). The correct argument is the bounded-geometry one the note gestures at. \(\pi^*\tilde k\) is smooth on the blow-up, and its \(C^2(B_1)\) norm on \(\{|y|\le2\}\) is \(O(x_0)\). Hence \(W^+(B_1+\tilde k)=O(x_0)\), so \(W^+(\hat g)=O(1)\), and similarly for \(s\) and the volume form.

**Integrated error.** \(\int_0^{r_0}\min(1,x_0/r^2)r^3dr\le C(x_0^2+x_0r_0^2)\), and the squared term gives \(x_0^2\log\). Comparisons of \(W^+\) for two metrics should be read through the scalars \(|W^+|^2dV\). The resulting projector and volume corrections are of the same order \(x_0/r^2\).

**Why no first-order term arises.** The linear term \(2x_0\langle W^+_p,P_+\mathcal R^{\rm lin}(h)P_+\rangle\) has zero spherical mean even without pointwise vanishing (see §4, which shows \(\oint_{S_\rho}\mathcal R^{\rm lin}(h)=0\) for every block). The exact vanishing \(W^+(B)=s(B)=0\) is what is really essential, and it acts at zeroth order. Without it, \(|P_+\mathcal R^{\rm lin}(x_0h)P_+|^2\sim x_0^2r^{-8}\) integrated over \(r\ge\sqrt{x_0}\) would contribute \(O(1)\). So the inner region is clean because the cell is exactly self-dual-flat, not because of a cancellation at first order.

## 4. Cut annulus and flux (item 3)

**Expansion.** The pointwise error orders \(x_0r_0^{-2}\) (curvature-dependent parts of the linearization, projector, volume) and \(x_0^2r_0^{-8}\) (squared linear term) are right. Integrated over a region of volume \(\sim r_0^4\), together with \(W^+(g)=W^+_p+O(r)\), they give the stated \(O(x_0r_0+x_0r_0^2+x_0^2r_0^{-4})\).

**Cutoff independence.** Every term of \(\mathcal R^{\rm lin}\) has the form \(\partial_a\partial_b(\cdot)\). On the annulus, \(\int\partial_a\partial_b(\chi h)=-\oint_{S_{\rho_1}}n_a\partial_bh\), with \(n\) pointing away from the origin and \(\chi h\) vanishing near the outer sphere. Hence \(\Phi=+\oint n_a\partial_bh\), matching the script's sign.

Because \(n\,\partial h\,dS\) is homogeneous of degree 0, the sphere integral is independent of \(\rho_1\). Consequently \(\oint_{S_\rho}\mathcal R^{\rm lin}(h)=0\) for **all** blocks, including \(\Lambda^-\), where the linearized \(W^-\) does not vanish pointwise. So \(\Phi^{--}\) is cutoff-independent as well.

**Independent hand computation.** On \(S^3\), using \(\oint x_ax_b=\tfrac{\pi^2}2\delta_{ab}\) and \(\oint x_ax_bx_cx_d=\tfrac{\pi^2}{12}(\delta\delta+\delta\delta+\delta\delta)\), with \(Q_{ce}=x_cx_e+(Jx)_c(Jx)_e\):
\[
T_{abce}:=\oint n_a\partial_bh_{ce}=-\tfrac{\pi^2}{3}\delta_{ab}\delta_{ce}-\tfrac{\pi^2}{6}\big(\delta_{ac}\delta_{be}+\delta_{ae}\delta_{bc}+J_{ca}J_{eb}+J_{cb}J_{ea}\big).
\]
This is symmetric in \((a,b)\), as commuting derivatives require. Inserting it into \(R_{ijkl}=\tfrac12(T_{jkil}+T_{iljk}-T_{ikjl}-T_{jlik})\) gives
\[
\tfrac{\pi^2}{3}(\delta_{ik}\delta_{jl}-\delta_{il}\delta_{jk})-\tfrac{\pi^2}{12}\Big[2(\delta_{ik}\delta_{jl}-\delta_{il}\delta_{jk})-4J_{ij}J_{kl}-2(J_{ik}J_{jl}-J_{il}J_{jk})\Big].
\]
With the pairing \(\tfrac14\sum w_{ij}w'_{kl}R_{ijkl}\), the three tensor types act on \(\Lambda^2\) as follows:
- \(\delta\delta-\delta\delta\mapsto I\);
- \(J_{ij}J_{kl}\mapsto2w_1w_1^T\), which is zero on \(\Lambda^-\);
- \(J\otimes J\mapsto\mathrm{diag}(1,-1,-1)\) on \(\Lambda^+\) and \(+I\) on \(\Lambda^-\), since \((1,1)\)-forms are \(J\)-invariant.

The result is:
- \(\Lambda^+\): \(\tfrac{\pi^2}{3}I-\tfrac{\pi^2}{12}\mathrm{diag}(-8,4,4)=\mathrm{diag}(\pi^2,0,0)\);
- \(\Lambda^-\): \(\tfrac{\pi^2}{3}I\);
- cross block: \(0\).

This is exactly the JSON output. A built-in consistency check holds: \(\operatorname{tr}\Phi^{++}=\operatorname{tr}\Phi^{--}=\pi^2\), as \(s=4\operatorname{tr}\mathbf R^+=4\operatorname{tr}\mathbf R^-\) requires.

**Script conventions.**
- The sign test returns \(R_{1212}=K\), so \(R_{ijkl}\) matches the operator convention.
- The flux substitution \(\partial_j\partial_kh_{il}\to F[j,k,i,l]\), with the other three terms likewise, matches `Rlin` term by term.
- The \(\tfrac14\) pairing and the \(1/\sqrt2\) normalization of the basis are correct.
- `sphere_monomial` is the standard formula; it gives \(2\pi^2\) at \(\alpha=0\).

**Script defects.** Neither defect affects the result.
- Both `assert` lines are vacuous. Python parses `sp.simplify(... if False else 0)` as `simplify(0)`, so the assumption "denominator \(=c\,t^{2k}\)" is never tested. It is true here, since \(h\) has only powers of \(t^2\) in the denominator.
- `sphere_integral` is unused.

## 5. Assembly, Einstein variant, and remainder (item 4)

**Assembly.** \(4(-2x_0\langle W^+_p,\Phi\rangle)+\tfrac1{12}(-2x_0s_p\cdot4\operatorname{tr}\Phi)=-8x_0\langle W^+_p+\tfrac{s_p}{12}I,\Phi\rangle=-8\pi^2x_0\mathbf R^+_p(w_1,w_1)\). Here \(\langle A,B\rangle=\operatorname{tr}(AB)\), consistent with endomorphism norms.

**Choice of ζ.** Every unit \(\zeta\in\Lambda^+_p\) corresponds to an orthogonal \(J_\zeta\) inducing the orientation of \(M\). The resulting blow-ups are all \(M\#\overline{\mathbb{CP}}^2\), and the choices are isotopic because the space of such \(J\) is an \(S^2\).

**Einstein variant.** \(J=P+\tfrac14\int(s-4\lambda)^2\). For Einstein \(g\), both the \(\delta s\) part and the volume part of the first variation vanish identically, because \(s\equiv4\lambda\). The note's phrase "\(\tfrac12(s_p-4\lambda)\int\delta s\)" is loose wording for this. The second-order part is \(O(x_0^2r_0^{-4}+x_0^2\log)\), so the statement holds.

**Sharper remainder.** The only \(O(x_0r_0)\) error comes from pairing the linear Taylor term \((\partial W^+)_p\cdot x\), and its \(s\)-analogue, with \(\mathcal R^{\rm lin}(\chi h)\). The latter is even in \(x\), because \(h(-x)=h(x)\), so this term integrates to zero. All remaining errors are \(O(x_0r_0^2+x_0^2r_0^{-4}+x_0^2\log)\). Choosing \(r_0=x_0^{1/6}\) gives
\[
P(\hat g)=P(g)+8\pi^2(1-x_0\mathbf R^+_p(\zeta,\zeta))+O(x_0^{4/3}).
\]

**Regularity.** The constant depends on \(C^2\) bounds of \(g_{ij}\) in normal coordinates and on \(|\nabla\mathrm{Rm}|\). Normal-coordinate \(C^2\) control costs roughly one more derivative of the metric than "\(C^3\)" suggests. This is immaterial for smooth \(g\).

## 6. Consistency checks (item 5)

**Kähler topology.** \(\int s\,d\mu=2\int\rho\wedge\omega=4\pi c_1\cdot[\omega]\). With \(c_1(\hat M)=\pi^*c_1-E\) and \([\hat\omega]=\pi^*[\omega]-aE\), where \(a=\mathrm{area}(E)\),
\[
c_1(\hat M)\cdot[\hat\omega]=c_1\cdot[\omega]-\mathrm{area}(E),
\]
**not** \(-\mathrm{area}/\pi\) as written in the note. With area \(=\pi x_0\), the drop is \(4\pi^2x_0=x_0F_s\), so the numerical check passes.

**Second Kähler check.** This one tests the aligned coefficient independently of the script. On Kähler metrics \(|W^+|^2=s^2/24\), so \(4\Delta W^++\Delta S/12=\Delta S/4\approx\tfrac14\cdot2s_p(-4\pi^2x_0)=-2\pi^2x_0s_p\). This equals \(-8\pi^2x_0\mathbf R^+(w_1,w_1)\) with \(\mathbf R^+(w_1,w_1)=s/4\). The perpendicular entry \(b=0\) is not tested by Kähler topology; it rests on the flux computation above.

**Complex space forms.** \(\mathbf R^+=\mathrm{diag}(s/4,0,0)\). This gives slopes \(+6\) (aligned) and \(0\) (perpendicular) for \(\mathbb{CH}^2\), and \(-6\) for Fubini–Study normalized to \(s=+24\).

**Representation theory.** The \(U(2)\)-invariants are confirmed:
- \(S^2_0\Lambda^+\) contains one trivial summand;
- \(S^2_0\Lambda^-\) is irreducible of dimension 5 under \(SU(2)\);
- \(\Lambda^+\otimes\Lambda^-\) has no \(SU(2)\)-invariant.

So \(\Phi^{+-}=0\) and \(\Phi^{--}\propto I\) are forced.

**Consequence 1.** It follows with \(\zeta\) the top eigenvector of \(\mathbf R^+_p\). The conditions \(s_p>0\Rightarrow\lambda_{\max}>0\) and \(\lambda(W^+)>|s|/12\) are correct.

## 7. Lemma Q and Lemma Q′

**Lemma Q.** The algebra is correct: \(P\ge8\pi^2[3|\tau+\eta|-2\chi+2/|\Gamma|]\), giving \(8\pi^2(k+4\ell)\) for \(\Gamma=1\). In the one-blow-up equality case, \(P=8\pi^2+4\int|W^+|^2\). The topology "blow-ups/handles of \(\mathbb R^4\)" with \(\tau=-k\) is an input, not a consequence. Mixed \(\pm\) blow-ups would change \(|\tau|\).

**Lemma Q′.** Mayer–Vietoris with \(H_*(S^3)\) gives \(b_1(U)=0\), and \(b_2(U)+b_2(W)=1\). Hence \(b_2(U)=1\) and \(b_2(W)=0\); the intersection form restricts, so \(\tau(U)=-1\) is automatic. Lefschetz duality gives \(b_3(U)=0\). For connected \(U\), \(\chi(U)=2\) exactly. The bound \(P\ge24\pi^2-32\pi^2+16\pi^2-C\varepsilon=8\pi^2-C\varepsilon\) is correct.

The \(\eta\)/Chern–Simons term on Σ is the one step needing a sentence. One way to avoid continuity of η in \(C^2\):
1. Interpolate inside the collar to an exactly Euclidean annulus. This changes the scale-invariant curvature integrals by \(O(\varepsilon)\), because \(|\mathrm{Rm}|\le C\varepsilon/\rho^2\) on volume \(\sim\rho^4\).
2. Glue on \(\mathbb R^4\setminus B\).
3. Apply Lemma Q with \(\Gamma=1\) and exactly flat end terms (\(8\pi^2\) and \(0\)).

The quantitative consequence for \(\mathfrak P_{1,0}\) follows from \(P(U_0)\ge P(U)\) and the arithmetic. I did not re-verify the cell value \(0.99584841\).

## 8. Lemma R

**As stated.** The steps hold: interior analyticity, \(\nabla\mathrm{Rm}\equiv0\) on connected \(U\), and Cartan's theorem giving local \(\mathbb{CH}^2\) geometry. The collar germ terms coincide with those of the \(\mathbb{CH}^2\) geodesic ball sharing the collar. Then \(\Delta\chi=\tfrac6{\pi^2}\Delta V\), \(\Delta\tau=\tfrac2{\pi^2}\Delta V\), and \(P(U)>0\) follows via Schur.

**The gap.** A cell with \(k\) blow-ups and \(\ell\) handles has \((\Delta\chi,\Delta\tau)=(k-2\ell,-k)\). The relation \(\Delta\chi=3\Delta\tau\) holds iff \(\ell=2k\); for example \((k,\ell)=(1,2)\) gives \((-3,-1)\). For these cells the Chern–Weil argument excludes nothing. So the "Consequence" line "\(\mathfrak P_{k,\ell}=0\) only through degeneration" is not covered by Lemma R for \(\ell=2k\).

**Covering every \((k,\ell)\ne(0,0)\).** Once \(U\) is locally \(\mathbb{CH}^2\), we have \(\sec\le-1<0\), and \(\partial U\) is a geodesic sphere, strictly convex from inside. On the universal cover \(\tilde U\):
1. Convexity keeps geodesics interior.
2. There are no conjugate points.
3. Hence \(\exp_q\) is a diffeomorphism onto \(\tilde U\), a closed 4-ball with connected \(\partial\tilde U\cong S^3\).
4. Since \(\partial U\cong S^3\) is simply connected, its preimage is \(|\pi_1(U)|\) disjoint spheres, so \(\pi_1(U)=1\).
5. Therefore \(U\) is a ball; equivalently, the developing map is an isometric embedding onto the geodesic ball.

So no compact locally-\(\mathbb{CH}^2\) filling of the collar has nontrivial topology, and Lemma R holds for all cells. The Chern–Weil proof then becomes a special case.

## 9. Two framing remarks

- Theorem F is a construction (upper) statement only. The stated hyperbolic-bulk rigidity and the value \(\mathfrak P^{\mathbb H^4}_{1,0}=8\pi^2\) need the matching lower theory at scale \(\sqrt{x_0}\). The note already says this.
- For KE bulk with \(s<0\), \(\lambda_{\max}(\mathbf R^+)=0\) exactly, so Theorem F's linear term vanishes on the whole kernel 2-sphere. The \(x_0^2\log\) coefficient must then dominate the \(O(x_0^{4/3})\) remainder. With the improved remainder, the competing orders are \(x_0^2\log(1/x_0)\) versus \(x_0^{4/3}\). The construction-side remainder is therefore still too coarse to resolve that second-order term, unless the cut is replaced by a gluing that solves the linearized equation in the annulus.