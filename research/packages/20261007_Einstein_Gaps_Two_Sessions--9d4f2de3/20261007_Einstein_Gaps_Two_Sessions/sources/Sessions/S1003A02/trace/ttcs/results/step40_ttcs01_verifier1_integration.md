# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 40,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step40_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step40_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the new Step-40 theorems in workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md against the simultaneous signed-cost identity (Prop. 'Simultaneous signed cost identity', lines 319-447 of variational_selection_and_global_cost.tex) in its normalization s=-4, F^+=2i sigma(Phi), rho=|Phi|^2 in [0,2], psi=2sqrt2 sigma(Phi), W_0=(1/4)(rho^2 I/3 - psi psi). Check in detail: (1) Lemma 1: that the Clifford contraction of the u^perp-valued part of the first jet has kernel exactly the Gray-Hervella W_2 (almost-Kaehler / Nijenhuis) component, that cc*=2, hence rho|v_4|^2=|a+J'b|^2/2 under D_A Phi=0, and that this is correct in the presence of the U(1) connection; (2) the pointwise Weitzenboeck formula (1/2)Delta rho + |nabla Phi|^2 = rho(2-rho)/2 in this normalization (the integrated version K=(1/2)int rho(2-rho) follows from the paper's slack identities); (3) Theorem N as an exact equality, including the polynomial m-rho^2(2-rho) and the (a,b) quadratic form, and the Hermitian corollary P>=8pi^2 Q; (4) Theorem W: the self-dual Weitzenboeck convention (Delta_H = nabla*nabla - 2W^+ + s/3 with W_0 having Kaehler eigenvalue s/6), |d psi|^2 = 2 rho |b|^2 under the Dirac equation, and the collapse of the (a,b) form to -4|zeta|^2; (5) Theorem E: the pointwise envelope g_{t,lambda}, the use of |W^+|^2 = rho^4/24 - rho^2 x/2 + |M|^2 and |M|^2 >= (3/2) x^2, and the exact conclusion that the threshold is t=2/3 binding at rho=3/2. Report any sign, factor, convention, or quantifier error and its repair, and say precisely which statements are proved. Also assess whether Theorem E really shows that no pointwise/algebraic compensation inequality can give k-dependence, and what global terms remain.

## Integrated Scientific Memo

# Step-40 verification memo

## Verdict

In the stated normalization
\[
s=-4,\qquad F_{\mathcal A}^{+}=2i\sigma(\Phi),\qquad
\rho=|\Phi|^2\in[0,2],\qquad
\psi=2\sqrt2\,\sigma(\Phi),\qquad
W_0=\frac14\left(\frac{\rho^2}{3}I-\psi\otimes\psi\right),
\]
the algebraic cores of **Lemma 1, Theorem N, Theorem W, and Theorem E are correct**. In particular:

- \(cc^*=2I\);
- the Dirac equation gives
  \[
  \rho |v_4|^2=\frac12|a+J'b|^2;
  \]
- the pointwise spinor Weitzenböck formula is
  \[
  \frac12\Delta\rho+|\nabla_{\mathcal A}\Phi|^2
  =\frac12\rho(2-\rho);
  \]
- Theorems N and W are exact equalities with the displayed constants and signs;
- the envelope \(g_{t,\lambda}\) is correct, and within the stated affine pointwise method its exact threshold is \(t=2/3\), with contact at \(\rho=3/2\).

The principal repairs are interpretive and quantificational:

1. Theorem E does **not** exclude every conceivable pointwise/algebraic compensation inequality; it exhausts a specified affine family built from the displayed exact identities, positivity, and \(|M|^2\ge\frac32x^2\).
2. The Hermitian tariff needs only a simultaneous **chosen** family of solutions whose Bloch structures are integrable, not that every possible solution be integrable.
3. It does not literally contain the Step-38 theorem for arbitrary Kähler metrics, because scalar-\(-4\) Yamabe replacement generally destroys Kählerity.
4. \(x=M(n,n)\) is a Rayleigh component, not generally a Weyl eigenvalue.
5. The near-minimizer estimate is asymptotic; the quoted numerical coefficient should be approximately \(0.684914\), not \(0.68488\).
6. The scale-law and support-volume interpretations require controlled geometry/multiplicity and, for the latter, are averaged over sign classes.

---

## 1. Lemma 1

On \(\{\rho>0\}\), write
\[
\Phi=\sqrt\rho\,u,\qquad
\nabla_{\mathcal A}u=i\beta\otimes u+v\otimes u^\perp,
\qquad
a=d\sqrt\rho,\quad b=\sqrt\rho\,\beta .
\]
Then
\[
\nabla_{\mathcal A}\Phi=(a+ib)\otimes u+\sqrt\rho\,v\otimes u^\perp,
\]
and consequently
\[
|\nabla\Phi|^2=|a|^2+|b|^2+\rho|v|^2,
\qquad
|\zeta|^2=\rho(|a|^2+|b|^2),
\qquad
|\nabla n|^2=4|v|^2.
\]

### Clifford contraction

Define the real-linear map
\[
c:T^*\otimes_{\mathbb R}\mathbb C\longrightarrow S^-,
\qquad
c(v)=\sum_i e_i\cdot(v_i u^\perp).
\]
Its real Hilbert–Schmidt norm squared is \(8\): the eight real basis vectors
\(e^i\otimes u^\perp,e^i\otimes iu^\perp\) have unit-length images. By equivariance, \(cc^*\) is scalar on the real irreducible \(S^-\), so
\[
\operatorname{tr}_{\mathbb R}(cc^*)=8=4\mu
\quad\Longrightarrow\quad
\boxed{cc^*=2I_{S^-}}.
\]
Thus \(c\) is onto, \(\dim_{\mathbb R}\ker c=4\), and on
\((\ker c)^\perp\),
\[
|c(v_4)|^2=2|v_4|^2.
\]

### Kernel and Gray–Hervella component

Only the \(u^\perp\)-jet \(v\) changes the gauge-invariant Bloch form \(n\). In real dimension four the intrinsic torsion of a compatible almost-Hermitian structure consists of
\[
\mathcal W_2\oplus\mathcal W_4,
\]
each of real dimension four. The alternation \(v\mapsto d\omega\) has kernel \(\mathcal W_2\), the pointwise almost-Kähler component. The canonical-spinor identity for an almost-Kähler structure gives
\[
\mathcal W_2\subseteq\ker c.
\]
Both spaces have dimension four, hence
\[
\boxed{\ker c=\mathcal W_2=\ker(v\mapsto d\omega)},
\]
and \((\ker c)^\perp=\mathcal W_4\), the Lee component.

In complex dimension two, vanishing of \(\mathcal W_2\) is equivalent to integrability, so “Nijenhuis component” is appropriate. However, the notation
\(|\nabla n|_{\mathcal W_2}^2=4|v_2|^2\) is a chosen normalization of intrinsic torsion; it should not be equated with a conventionally normalized \(|N_J|^2\) without stating the conversion factor.

The numerical checks corroborate, but do not replace, this representation-theoretic argument: both maps have rank four and their kernels coincide to machine precision.

### Dirac constraint and \(U(1)\) connection

There is an orthogonal complex structure \(J'\) on \(T^*\) such that
\[
(ib)\cdot u=(J'b)\cdot u,\qquad
|(a+ib)\cdot u|=|a+J'b|.
\]
Decomposing \(v=v_2+v_4\), the Dirac equation is
\[
(a+ib)\cdot u+\sqrt\rho\,c(v_4)=0.
\]
Using \(cc^*=2I\),
\[
v_4=-\frac1{2\sqrt\rho}\,
c^*((a+ib)\cdot u),
\]
so
\[
\boxed{\rho|v_4|^2=\frac12|a+J'b|^2}.
\]

This remains correct in the presence of the \(U(1)\) connection: its local contribution is precisely the phase form \(\beta\), hence \(b=\sqrt\rho\,\beta\). Gauge changes rotate \(u,u^\perp\), but leave \(n\), the norms, and the \(\mathcal W_2\oplus\mathcal W_4\) decomposition invariant. “Dirac does not see \(\mathcal W_2\)” is therefore correct as a statement about the pointwise first-jet symbol; the curvature equation and global PDE can still constrain it.

---

## 2. Spinor Weitzenböck formula

The normalized spinor equation is
\[
4\nabla_{\mathcal A}^*\nabla_{\mathcal A}\Phi
+(-4+2\rho)\Phi=0,
\]
hence
\[
\nabla_{\mathcal A}^*\nabla_{\mathcal A}\Phi
=\left(1-\frac\rho2\right)\Phi.
\]
With \(\Delta=d^*d\),
\[
\frac12\Delta|\Phi|^2
=\langle\nabla^*\nabla\Phi,\Phi\rangle-|\nabla\Phi|^2,
\]
therefore
\[
\boxed{
\frac12\Delta\rho+|\nabla_{\mathcal A}\Phi|^2
=\frac12\rho(2-\rho).}
\]
On the closed manifold this gives
\[
\boxed{K=\frac12\int\rho(2-\rho),}
\]
in agreement with the paper’s slack identity.

Multiplying by \(2\rho\) and integrating yields
\[
\int 2\rho|\nabla\Phi|^2+\int\rho\Delta\rho
=\int\rho^2(2-\rho).
\]
Since \(d\rho=2\sqrt\rho\,a\),
\[
\int\rho\Delta\rho=\int|d\rho|^2=4\int\rho|a|^2,
\]
so the exact zero identity used in Theorem N is
\[
\boxed{
\int\left[
2\rho|\nabla\Phi|^2+4\rho|a|^2-\rho^2(2-\rho)
\right]=0.}
\]

---

## 3. Theorem N

From the simultaneous signed-cost identity,
\[
\mathfrak S:=8\pi^2Q-P
=4\mathbb E K-\mathcal W
-\mathbb E\left[
8\|\zeta\|^2+4\|M\|^2
+\int b(\rho)(2-\rho)^2
\right],
\]
where
\[
b(\rho)=\frac{-\rho^2+8\rho+2}{6}.
\]
Using \(4K=2\int\rho(2-\rho)\), this becomes
\[
\mathfrak S
=\mathbb E\int m(\rho)
-8\mathbb E\|\zeta\|^2
-4\mathbb E\|M\|^2-\mathcal W,
\]
with
\[
m(\rho)
=\frac{(2-\rho)(-\rho^3+10\rho^2-2\rho-4)}6.
\]

Add the zero identity above. Since
\[
|\nabla\Phi|^2
=|a|^2+|b|^2+|v_2|^2\rho+\frac12|a+J'b|^2,
\]
one obtains
\[
2\rho^2|v_2|^2
=\frac12\rho^2|\nabla n|_{\mathcal W_2}^2
\]
and the derivative contribution
\[
-\rho\left(|a|^2+5|b|^2-2\langle a,J'b\rangle\right).
\]
The polynomial identity is
\[
m(\rho)-\rho^2(2-\rho)
=-\frac{(2-\rho)^2(2+2\rho-\rho^2)}6.
\]

Therefore the displayed Theorem N is exactly correct:
\[
\boxed{
\begin{aligned}
\mathfrak S={}&
\frac12\mathbb E\int\rho^2|\nabla n|_{\mathcal W_2}^2\\
&-\mathbb E\int
\frac{(2-\rho)^2(2+2\rho-\rho^2)}6\\
&-\mathbb E\int
\rho\left(|a|^2+5|b|^2-2\langle a,J'b\rangle\right)\\
&-4\mathbb E\|M\|^2-\mathcal W .
\end{aligned}}
\]
The signs are as claimed because
\[
2+2\rho-\rho^2>0\qquad(0\le\rho\le2),
\]
and
\[
\begin{pmatrix}1&-1\\-1&5\end{pmatrix}
\]
has determinant \(4\) and positive trace.

### Hermitian corollary

If a simultaneous chosen family of solutions has integrable Bloch structures \(J_\epsilon\) on \(\{\Phi_\epsilon\ne0\}\), then
\[
|\nabla n_\epsilon|_{\mathcal W_2}=0.
\]
The weight \(\rho^2\) makes the zero set harmless, and every remaining term in Theorem N is nonpositive. Thus
\[
\mathfrak S\le0,\qquad
\boxed{P\ge8\pi^2Q}.
\]

**Quantifier repair:** existence of one simultaneous integrable choice is sufficient. “Every SW-selected structure” is acceptable only if “selected” refers to the fixed choice; “every possible solution” is unnecessarily strong.

**Scope repair:** this contains the scalar-\(-4\) Kähler/Hermitian instance, but it does not by itself reproduce the Step-38 theorem for every Kähler metric. A general Kähler metric need not have \(s=-4\), and its scalar-\(-4\) Yamabe representative need not remain Kähler.

### Near-minimizers

For pure blow-ups, if
\[
\frac{P}{8\pi^2k}\to c<1,
\]
then the precise consequence is
\[
\boxed{
\liminf_{k\to\infty}\frac1k\,
\mathbb E_\epsilon\int
\rho_\epsilon^2|\nabla n_\epsilon|_{\mathcal W_2}^2
\ge16\pi^2(1-c).}
\]
At finite \(k\), an \(o(k)\) term must be retained unless the ratio is exactly \(c\).

For
\[
1-c\in[0.0043372672289,0.0043372672468],
\]
the coefficient is approximately
\[
16\pi^2(1-c)\in[0.68491378,0.68491379].
\]
Thus \(0.68488\) is a small numerical error.

The \(O(r^2)\) scaling is valid for a fixed-angle rotation in a geometrically controlled four-dimensional region of diameter \(r\):
\[
|\nabla n|^2=O(r^{-2}),\qquad \operatorname{Vol}=O(r^4).
\]
It does not alone rule out many shrinking regions, anisotropic tubes, or uncontrolled collapse, so the “unit-size regions” conclusion needs corresponding geometry and multiplicity assumptions.

---

## 4. Theorem W

### Self-dual Weitzenböck convention

For a self-dual two-form,
\[
\boxed{\Delta_H=\nabla^*\nabla-2W^++\frac{s}{3}},
\]
equivalently
\[
\nabla^*\nabla\psi
=\Delta_H\psi+2W^+\psi-\frac{s}{3}\psi.
\]
At \(s=-4\), self-duality gives \(\|d^*\psi\|=\|d\psi\|\), hence
\[
\int|\nabla\psi|^2
=2\|d\psi\|^2+2\int W^+(\psi,\psi)+\frac43\int\rho^2.
\]

Since
\[
W_0\psi=-\frac{\rho^2}{6}\psi,
\]
writing \(M=W^+-W_0\), \(n=\psi/\rho\), and \(x=M(n,n)\), gives
\[
\boxed{
\int|\nabla\psi|^2
=2\|d\psi\|^2
+2\int\rho^2x
+\int\frac{\rho^2}{3}(4-\rho^2).}
\]
At \(\rho=2\), the \(n\)-eigenvalue of \(W_0\) is \(-2/3=s/6\), so the Kähler convention is correct.

### The \(d\psi\) identity

The first-jet Fierz identity together with the Dirac equation gives
\[
|d\psi|^2=|d^*\psi|^2
=2|\operatorname{Im}\zeta|^2.
\]
Since \(\operatorname{Im}\zeta=\sqrt\rho\,b\),
\[
\boxed{|d\psi|^2=2\rho|b|^2.}
\]
The \(\mathcal W_2\) component contributes nothing because it is precisely the kernel of the alternation map \(v\mapsto d\omega\).

The supplied numerical matrix has eigenvalues \(\{0^4,2^4\}\) and is consistent with this formula. For a cleaner reproducible check, the script should record the direct residual
\[
\|Q_d-2I_b\|,
\]
rather than leaving `Qd_minus_combo` null.

### Collapse of the quadratic form

Because \(\psi=\rho n\),
\[
|\nabla\psi|^2
=4\rho|a|^2+4\rho^2|v_2|^2
+2\rho|a+J'b|^2.
\]
Substitution into the self-dual Weitzenböck identity gives
\[
\begin{aligned}
2\rho^2|v_2|^2={}&
2\rho|b|^2+\rho^2x+\frac{\rho^2}{6}(4-\rho^2)\\
&-2\rho|a|^2-\rho|a+J'b|^2.
\end{aligned}
\]
Combining this with Theorem N, the full \((a,b)\)-expression is
\[
\begin{aligned}
&2\rho|b|^2-2\rho|a|^2-\rho|a+J'b|^2\\
&\quad-\rho\left(|a|^2+5|b|^2-2\langle a,J'b\rangle\right)\\
&=-4\rho(|a|^2+|b|^2)
=-4|\zeta|^2.
\end{aligned}
\]
The remaining polynomial identity is
\[
\frac{\rho^2}{6}(4-\rho^2)
-\frac{(2-\rho)^2(2+2\rho-\rho^2)}6
=\frac{(2-\rho)(\rho-1)(3\rho+2)}3.
\]

Thus Theorem W is exactly:
\[
\boxed{
\begin{aligned}
\mathfrak S={}&
\mathbb E\int\left[\rho^2x-4|M|^2\right]\\
&+\mathbb E\int
\frac{(2-\rho)(\rho-1)(3\rho+2)}3\\
&-4\mathbb E\|\zeta\|^2-\mathcal W .
\end{aligned}}
\]

**Interpretive repair:** \(x=M(n,n)\) is a Rayleigh component and
\[
x=W^+(n,n)+\frac{\rho^2}{6}.
\]
It need not be an eigenvalue unless \(n\) is a \(W^+\)-eigenvector. Moreover, \(x>0\) alone does not imply \(|W^+|<|W_0|\); transverse and off-diagonal parts of \(M\) matter. The exact saving channel is
\[
\rho^2x-4|M|^2.
\]

---

## 5. Theorem E

Assume \(\ell=0\), so \(Q=k\).

Combining the amplitude and Weyl forms with constant weight \(\lambda\) gives
\[
\begin{aligned}
\mathfrak S
={}&\mathbb E\int\Big[
\lambda\rho^2x+\lambda p_2(\rho)
+(1-\lambda)m(\rho)-4|M|^2\\
&\hspace{28mm}-(8-4\lambda)|\zeta|^2
\Big]-\mathcal W,
\end{aligned}
\]
where
\[
p_2(\rho)=\frac{(2-\rho)(\rho-1)(3\rho+2)}3.
\]
To drop the \(\zeta\)-term in the required direction one needs
\[
\lambda\le2;
\]
the convex range \(0\le\lambda\le1\) already suffices for the threshold result.

The closed identity is
\[
P=-8\pi^2(A-k)+
\mathbb E\int
\left(\frac{\rho^4}{6}+\frac43-2\rho^2x+4|M|^2\right),
\]
because
\[
\boxed{
|W^+|^2
=\frac{\rho^4}{24}-\frac{\rho^2x}{2}+|M|^2.}
\]
Indeed, \(|W_0|^2=\rho^4/24\) and
\(\langle W_0,M\rangle=-\rho^2x/4\).

Combining the field estimate with weight \(t\) and the closed identity with weight \(1-t\), the \(M,x\) terms are
\[
4|M|^2-c\rho^2x,\qquad
c=t\lambda+2-2t.
\]
For trace-free symmetric \(M:\Lambda^+\to\Lambda^+\),
\[
|M|^2\ge\frac32x^2,
\]
with equality at eigenvalues \(x,-x/2,-x/2\). Therefore
\[
4|M|^2-c\rho^2x
\ge6x^2-c\rho^2x
\ge-\frac{c^2\rho^4}{24}.
\]
This yields
\[
\boxed{
P\ge8\pi^2[k-(1-t)A]
+\mathbb E\int g_{t,\lambda}(\rho)}
\]
with
\[
\boxed{
\begin{aligned}
g_{t,\lambda}(\rho)
={}&(1-t)\left(\frac{\rho^4}{6}+\frac43\right)\\
&-t\left[
\lambda\frac{(2-\rho)(\rho-1)(3\rho+2)}3
+(1-\lambda)m(\rho)\right]\\
&-\frac{(t\lambda+2-2t)^2\rho^4}{24}.
\end{aligned}}
\]

At \(t=\lambda=2/3\),
\[
g_{2/3,2/3}(\rho)
=-\frac2{243}(2\rho-3)^2(\rho^2-24\rho-18).
\]
Since \(\rho^2-24\rho-18<0\) on \([0,2]\),
\[
g_{2/3,2/3}\ge0,
\]
with equality only at \(\rho=3/2\). Consequently,
\[
P\ge8\pi^2\left(k-\frac A3\right),
\]
equivalently
\[
\boxed{C_+\ge\frac23A}.
\]

At \(\rho=3/2\),
\[
\max_\lambda g_{t,\lambda}(3/2)
=-\frac34(3t-2),
\qquad
\lambda_{\rm opt}=2-\frac8{9t}.
\]
Thus for every \(t>2/3\), no constant \(\lambda\) makes
\(g_{t,\lambda}\ge0\) on all of \([0,2]\). The optimizer satisfies
\(\lambda_{\rm opt}<2\), so it lies in the admissible sign range. Finally,
\[
g_{2/3,2/3}(2)=\frac{124}{243}>0,
\]
so the contact is at \(\rho=3/2\), not at the Kähler–Einstein amplitude \(\rho=2\).

The Nijenhuis form does not improve this affine threshold: as an identity it is a reorganization of the amplitude form by the weighted spinor Weitzenböck equality. A positive coefficient on its \(\mathcal W_2\)-energy cannot be discarded in the upper bound for \(\mathfrak S\); converting it via the self-dual Weitzenböck identity returns to the Weyl form.

---

## 6. Exact scope of the exhaustion claim

What is proved is:

> Among constant affine combinations of the amplitude, Nijenhuis/Weyl, and closed Weyl–volume identities, followed by discarding terms of known sign and applying the sharp pointwise estimate \(|M|^2\ge\frac32M(n,n)^2\), the largest coefficient obtainable is \(t=2/3\).

This is enough to show that this natural affine pointwise scheme cannot produce a \(k\)-tariff for \(0<k<A/3\), since a bound \(P\ge c\,8\pi^2k\) would require
\[
C_+\ge A-(1-c)k,
\]
whose coefficient of \(A\) is \(>2/3\) in that range.

The stronger statement

> “No pointwise/algebraic compensation inequality whatsoever can give \(k\)-dependence”

is **not proved**. The calculation does not exhaust, for example:

- non-affine pointwise inequalities;
- other weighted spinor Weitzenböck multipliers;
- pointwise correlations among all \(2^k\) fields sharing the same \(W^+\);
- unreduced Walsh tensors or additional inter-spinor Fierz relations;
- algebraic constraints imposed jointly by several actual monopoles.

Nor does the \(\rho=3/2\) contact produce an actual closed metric and simultaneous monopole family realizing that algebraic state.

A precise replacement for Theorem E’s headline is therefore:

> **Affine pointwise exhaustion theorem.** The displayed exact identities, under constant affine combination, sign discarding, and sharp Weyl Cauchy–Schwarz, do not improve the LeBrun threshold \(C_+\ge2A/3\).

---

## 7. Global information still available

The quantities discarded by the pointwise envelope, and hence the natural sources of any \(k\)-dependent improvement, are:

1. **Walsh energy**
   \[
   \mathcal W
   =2\|f_\varnothing^-\|^2
   +2\sum_{I\ne\varnothing}\|f_I^+\|^2.
   \]

2. **Harmonic-projection information**
   \[
   \mathcal W
   =8\pi^2(\mathbb E p_\epsilon-A)
   +2\mathbb E J_\epsilon.
   \]

3. **Amplitude/Lee energy**
   \[
   \mathbb E\|\zeta_\epsilon\|^2,
   \]
   which controls amplitude gradients and the Dirac-forced \(\mathcal W_4\) component.

4. **Differential control of the free \(\mathcal W_2\) component**, including whether its energy must localize near topology carrying the fixed singleton anti-self-dual curvature charge.

5. **Multi-field elliptic correlations**, because all sign solutions live on the same metric and share the same \(W^+\).

6. **Global topology and localization**, especially relations between the \(4\pi^2\) relative anti-self-dual charge, exceptional cycles, and the self-dual/Walsh sectors.

The stated \(F_{3/4}\le0.8\) calculation, if used, gives only an **averaged** support-volume requirement:
\[
\mathbb E_\epsilon\operatorname{Vol}
\{F_{3/4}(\rho_\epsilon)>0\}
\ge10\pi^2(1-c)k+o(k),
\]
not the same lower bound for each individual sign class.

## Final classification

- **Lemma 1:** proved, subject only to presenting the standard spinorial identification \(\ker c=\mathcal W_2\) analytically rather than relying on the numerical check.
- **Pointwise and integrated spinor Weitzenböck formula:** proved with the displayed sign and factor.
- **Theorem N:** proved as an exact equality.
- **Hermitian tariff:** proved under the corrected simultaneous-choice quantifier.
- **Theorem W:** proved as an exact equality; \(x\) must be described as a Rayleigh component.
- **Theorem E:** \(g_{t,\lambda}\), the sharp \(M\)-elimination, and the \(t=2/3\), \(\rho=3/2\) threshold are proved.
- **Universal impossibility of all pointwise/algebraic compensation:** not proved; only the specified affine envelope is exhausted.