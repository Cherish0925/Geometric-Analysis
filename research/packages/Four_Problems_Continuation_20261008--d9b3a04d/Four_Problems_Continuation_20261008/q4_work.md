# Q4: negative Einstein almost-Kähler geometry — a complete endpoint corollary and the remaining equation

Date: 2026-10-08. Source basis: the uploaded research synthesis, its source companion A01.55 and A02.63–64, the original Apostolov–Armstrong–Drăghici (AAD) paper, and LeBrun's actual Seiberg–Witten supply discussion. This note does **not** prove the negative Goldberg conjecture. Its new internal connection is a full derivation from the project's finite-density endpoint theorem to a uniform bound on mean almost-Kähler torsion. That theorem is an input, not reproved here.

## 1. Fixed conventions and exact coupled identities

Let $(M^4,g,J,\omega)$ be closed, connected, almost-Kähler, oriented by $\omega$, with $|\omega|^2=2$ and $\operatorname{Ric}=-g$ (hence $s=-4$). Set
\[
T=2\chi+3\tau=c_1(J)^2>0,\qquad
u=\tfrac14|\nabla\omega|^2,
\]
\[
\eta=W^+(\omega)-(-\tfrac23+u)\omega,
\qquad V_3=W_3^+.
\]
The expression $-2/3+u$ is $s/6+q/4$ with $q=4u$; it is not the coefficient in the canonical curvature, which is $-1+u/2$.

Use averages with respect to $g$ and write
\[
x=\fint u,\quad z=\fint u^2,\quad
e=\fint|\eta|^2,\quad w=\fint|V_3|^2,
\quad v=z-x^2\ge0.
\]
The established AK Einstein integral identity in the source gives exactly
\[
\boxed{3z+e+2w=2x.}\tag{1}
\]
Consequently $0\le x\le2/3$. Put $\delta=2/3-x$. Then (1) is equivalently
\[
\boxed{e+2w+3v=2\delta-3\delta^2.}\tag{2}
\]
This equation is stronger bookkeeping than the separate inequalities: if $\delta\to0$, transverse Weyl curvature, the $W_3$ block, and torsion variance all vanish together in the displayed volume-normalized norms, while $u$ tends to $2/3$ rather than to zero.

With the standard operator norm on $W^+$,
\[
|W^+|^2=\frac{(-4+6u)^2}{24}+|\eta|^2+|V_3|^2.
\]
Combining this with (1),
\[
\boxed{\fint|W^+|^2=\frac23-x+\frac e2
=\delta+\frac e2
\le2\delta-\frac32\delta^2.}\tag{3}
\]
Thus the large-torsion endpoint $x\to2/3$ is exactly an averaged $W^+\to0$ endpoint. It is distinct from the Kähler endpoint $x=0$.

These computations use the normalization in A02.63 and A01.55. In particular no inequality has replaced $W_3$ by zero or treated transverse curvature as independent free data.

## 2. Canonical projection and actual unperturbed SW supply

Let $a=c_1(J)$. The canonical Hermitian connection has real curvature
\[
\gamma=iF_{\mathcal A},\qquad [\gamma]=2\pi a,
\qquad
\gamma^+=(-1+u/2)\omega+\eta.
\]
Since $\omega$ is harmonic and $\eta\perp\omega$ pointwise,
\[
2\pi a\cdot[\omega]=(-2+x)\operatorname{Vol}(g).
\tag{4}
\]
Denote $p=(a_g^+)^2$. Hodge projection and $[\omega]^2=2\operatorname{Vol}(g)$ imply
\[
\boxed{p\ge\frac{(a\cdot[\omega])^2}{[\omega]^2}
=\frac{\operatorname{Vol}(g)}{8\pi^2}(2-x)^2.}\tag{5}
\]
Also $p\ge a^2=T>0$.

The canonical class supplies an ordinary actual SW solution at this metric and every conformal metric:

* If $b^+>1$, this is Taubes's nonvanishing for the symplectic canonical Spin$^c$ structure, followed by compactness as a generic perturbation tends to zero.
* If $b^+=1$, the chamber needs to be checked. Equation (4) gives $a\cdot[\omega]<0$. In LeBrun's convention the perturbed equation is $iF_A^++\sigma(\Phi)=\varphi$; the reducible wall is $\varphi_H=2\pi a^+$. Since $H_g^+=\mathbb R[\omega]$ and $a^+$ is a negative multiple of $[\omega]$, the path $\varphi=t\omega$, $t\ge0$, from a large positive symplectic perturbation down to zero never crosses that wall. Taubes's nonzero invariant is in this positive-perturbation chamber. Compactness supplies the unperturbed solution. In four dimensions conformal metrics have the same self-dual harmonic subspace, so the same chamber argument supplies every conformal metric as needed.

References for these precise conventions: LeBrun, *Einstein Metrics, Symplectic Minimality, and Pseudo-Holomorphic Curves*, arXiv:math/0409290, pp. 13–14, Theorem 3.4 and the following chamber discussion; LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, arXiv:math/0003068, pp. 5–7, Definition 1 and equations (2)–(3).

This argument does not assert that the distinguished constant canonical spinor itself solves the ordinary unperturbed equations. The actual supplied solution may be a different field. The distinction matters: the transverse term $\eta$ in $\gamma^+$ obstructs identifying the constant canonical spinor with an ordinary SW solution.

## 3. A finite-density torsion-separation theorem

**Input (FD).** Use the project's finite-density endpoint theorem in its stated form: for actual conformal SW supply, $p\ge A>0$, $a^2\ge T$, and $\chi/A\le B$,
\[
\fint|\operatorname{Ric}+g|^2+\frac{D_\beta(g,a)}{\operatorname{Vol}(g)}
\ge c_{\rm FD}(B)\frac{(\beta-2)^2}{\beta^2},\qquad\beta\ge2,
\]
where
\[
D_\beta=(1+\beta^{-1})\int s^2
+6(\beta+1)\int|W^+|^2-72\pi^2p.
\]

**Corollary.** For each finite $B$, any closed almost-Kähler Einstein four-manifold with $s=-4$ and $\chi/T\le B$ satisfies
\[
\boxed{
\fint\frac{|\nabla\omega|^2}{4}
\le\frac23-\varepsilon(B),\qquad
\varepsilon(B)=\min\left\{\frac1{12},\frac{c_{\rm FD}(B)^2}{12288}\right\}>0.
}\tag{6}
\]
Equivalently,
\[
\fint s^*\le-\frac43-4\varepsilon(B).
\]
The statement is scale invariant when written as
\[
\fint\frac{|\nabla\omega|^2}{|s|}
\le\frac23-\varepsilon(B).
\]

**Proof.** The metric is already its negative constant-scalar Yamabe representative. Take $A=p$ in FD. This budget is constant throughout its conformal class; $a^2=T$, and $\chi/p\le\chi/T\le B$, so all FD hypotheses hold by Section 2. The Einstein residual vanishes. By (3) and (5),
\[
\begin{aligned}
\frac{D_\beta}{\operatorname{Vol}(g)}
&\le16(1+\beta^{-1})
+6(\beta+1)\left(2\delta-\frac32\delta^2\right)
-9\left(\frac43+\delta\right)^2\\
&=\frac{16}{\beta}+(12\beta-12)\delta-(9\beta+18)\delta^2\\
&\le\frac{16}{\beta}+12\beta\delta.
\end{aligned}\tag{7}
\]
If $\delta=0$, letting $\beta\to\infty$ contradicts FD. If $0<\delta\le1/12$, take $\beta=2/\sqrt{3\delta}\ge4$. The FD factor is at least $1/4$, while (7) becomes
\[
\frac{c_{\rm FD}(B)}4\le16\sqrt3\sqrt\delta.
\]
Squaring yields $\delta\ge c_{\rm FD}(B)^2/12288$. The branch $\delta>1/12$ supplies the other constant. This proves (6).

No new bound on $W^-$, diameter, injectivity radius or Sobolev constant was inserted. The dependence on $B=\chi/T$ remains exactly through FD.

**Scope.** This is a fully derived consequence of the internal FD theorem and classical supply, not a claim that FD has now been independently reproved. It rules out the maximal averaged torsion/ASD endpoint under finite density. It does not force $x=0$, so it does not settle Goldberg. Nor does it bound pointwise $u$ or pointwise $s^*$; a negative averaged star-scalar bound cannot be substituted into LeBrun's minimality theorem requiring pointwise $s^*\le0$.

The coefficient in (6) is deliberately nonoptimal. Optimizing this constant is not the remaining Goldberg task.

## 4. What the existing AAD theorem already closes

AAD, *Local models and integrability of certain almost Kähler 4-manifolds*, arXiv:math/0109098, Theorem 1, classifies the strictly almost-Kähler branch satisfying $\operatorname{Ric}''=0$ and $W^+(\omega)\parallel\omega$. In their local family the Einstein members are Ricci-flat. Their Theorem 2 gives compact integrability under the third Gray condition.

For an Einstein metric the only extra condition in that theorem is therefore
\[
\eta=0.
\]
One need not also prove $W_3=0$ or constant torsion. In particular a local negative Einstein strictly AK germ cannot have $\eta\equiv0$ on an open region. This is classical, not a new contribution of the present note, and A01.55 already correctly recorded it.

The full negative Goldberg conjecture can consequently be attacked by deriving $\eta=0$ from the complete closed-manifold equations. But writing that reduction is not a proof that the available identities force it.

## 5. Why direct canonical-spinor substitution cannot complete the argument

An ordinary SW equation requires its self-dual connection curvature to equal a quadratic spinor form. For the distinguished spinor with fixed direction $\omega$, the quadratic form is a multiple of $\omega$. The actual canonical curvature above has a transverse term $\eta$. Thus replacing an arbitrary actual SW solution by that distinguished canonical spinor would already require eliminating the transverse component. The almost-Kähler canonical pair naturally solves a perturbed system; the perturbation includes exactly the geometric discrepancy one needs to control.

Accordingly, the useful next analytic statement must compare an ordinary actual SW solution with the canonical almost-Kähler field, while retaining its perturbation, zeros and phase. Simply applying N1/I41 to the canonical pair without such a comparison would assume part of the desired integrability conclusion.

## 6. Exact remaining target and finite-jet implications

Under the established conventions the integrated second-derivative identity is
\[
\int|\nabla^2\omega|^2-3\int|\nabla\omega|^2
=4\int|\eta|^2.
\]
Its sign permits nonzero torsion. The source's transverse Bianchi pairing also gives
\[
\int\sum_i\langle(\delta W_3^+)_{e_i},\nabla_{Je_i}\omega\rangle
=2\int|W_3^+|^2.
\]
These exact identities should be retained together, not replaced by repeated separate absolute-value bounds. A successful completion must provide a new constraint eliminating the transverse term or excluding the remaining range
\[
0<x\le2/3-\varepsilon(B).
\]
The present corollary leaves that interval genuinely available; it is not a proof by exhaustion.

The corrected finite-jet count in A01.55 remains positive, and numerical jets do not furnish a local or global counterexample. A primary-source warning is especially pertinent: Armstrong's 1998 thesis explicitly describes a failed Cartan–Kähler existence proof in its introduction. Some early claimed examples based on an allegedly irreducible homogeneous Kähler surface were later corrected; Apostolov–Drăghici's survey, Section 6, explains that the surface was actually a product. These sources make it especially important not to treat a count or an apparent local model as an existence theorem.

## 7. Primary references and retrieval identifiers

1. AAD, *Local models and integrability of certain almost Kähler 4-manifolds*, https://arxiv.org/pdf/math/0109098 . 
2. LeBrun, *Einstein Metrics, Symplectic Minimality, and Pseudo-Holomorphic Curves*, https://arxiv.org/pdf/math/0409290 . 
3. LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, https://arxiv.org/pdf/math/0003068 . 
4. Apostolov–Drăghici, *The curvature and the integrability of almost-Kähler manifolds: a survey*, https://faculty.fiu.edu/~draghici/research/paperfiles/survey-web.pdf . 
5. Armstrong, *Almost-Kähler Geometry* (1998 thesis), https://johnarmstrongmaths.com/publications/resources/thesis.pdf . 

No complete negative Goldberg proof or closed counterexample was obtained in this investigation. The main deliverable is the explicit FD-to-torsion theorem (6), with all constants and the canonical actual-field input supplied; the remaining unknown is stated as an actual equation rather than concealed in an optimization or jet count.

## 8. A correction to the necessary diffuse-state template in A02.64

Equation (64.1) of the source asserts an equality for the full twist norm from $P=o(k)$. Hodge theory only supplies a lower bound unless a separate efficiency assumption is made. Indeed, writing $\gamma_J^-=\rho_0^J+t_J^-$ and denoting ASD harmonic projection by $\mathsf H^-$,
\[
\mathsf H^-(t_J^-)=2\pi a^- -\mathsf H^-(\rho_0^J),\qquad
\|\rho_0^J\|_2\le\sqrt{P/2}.
\]
The exact orthogonal decomposition is
\[
\|t_J^-\|_2^2
=\|2\pi a^- -\mathsf H^-(\rho_0^J)\|_2^2
+\|(1-\mathsf H^-)t_J^-\|_2^2.
\]
Therefore $P=o(k)$ and $|a^-|^2=k+\Pi$ imply
\[
\|t_J^-\|_2\ge2\pi\sqrt{k+\Pi}-o(\sqrt k),
\]
but do not imply equality or $t_J^-=2\pi a^-+o_{L^2}(\sqrt k)$. Those stronger statements require control of the last nonharmonic term. The lower RMS torsion consequence survives unchanged. A harmonic diffuse construction is a legitimate candidate to investigate, but cannot be designated the mandatory form of every low-$P$ competitor from this argument alone.
