# TTCS Independent Branch Record

```json
{
  "step_id": 69,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step69_P_form_upper_law_balanced_towers.md",
    "Sessions/S1003A02/workspace/data/step69_balanced_upper_law.json",
    "Sessions/S1003A02/workspace/scripts/step69_balanced_upper_law.py",
    "Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md",
    "Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md",
    "Sessions/S1003A02/workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md",
    "Knowledge/objects/papers/Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8/object.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md"
  ]
}
```

## Task

Verify, as a careful geometric analyst, the note Sessions/S1003A02/workspace/notes/step69_P_form_upper_law_balanced_towers.md. It claims: (1) Lemma 69.Y: for Y[g]<0 and the Yamabe metric ĝ in [g], E(ĝ)=16P(ĝ)/Y^2 and P(g)-P(ĝ)=|ŝ|∫|∇φ|^2+3∫(Δφ/φ)^2, hence alpha(M) <= 16 P(g)/Y[g]^2 for the scale-invariant defect E(g)=inf_λ ∫|Ric-λg|^2/(λ^2 V); (2) Corollary 69.Y': on X#k CP2bar#l(S1xS3), X minimal general type, LeBrun's polarized supply gives Y^2>=32π^2 c1^2(X), so alpha <= P(g)/(2π^2 A) for all g, alpha <= 4 p_*/A; (3) Theorem 69.B: exact non-asymptotic balanced bound alpha/h <= 28/9+(8/9)p_c = 3.99614465... on X#8n CP2bar#7n(S1xS3) for every finite cover X of a preliminary ball-quotient cover with large injectivity radius; (4) handle model (H'): the Green-function blow-up of round S1xS3 at a point is AE, conformally flat, scalar flat, with P=32π^2, and its small-scale gluing into any background changes P by 32π^2+o(1); (5) Theorem 69.KE(a): alpha(X#kCP2bar) < 4k/c1^2(X) for every minimal surface of general type and k>=1, via Corollary 59.KE; (b) cover version; (c) the claim that for non-ball-quotient KE hosts unramified covers force slope sigma->infinity as h->0, so the balanced small-h slice is unreachable there. Check each argument: conventions (Weyl norms, Gauss-Bonnet with AE end, P formula with F_+=4|W+|^2+s^2/12), whether LeBrun's Lemma 1 and Prop 3.2 are used correctly (the supply on manifolds with S1xS3 summands and b+=1 chambers), whether the certified cell P-enclosure (A01 step33 JSON values quoted in the note) can legitimately replace the J value in the coefficient, the topology arithmetic (T+, T-, sigma for Delta=0), the injectivity-radius/ball-count argument, uniformity of 59.R constants on covers, the handle gluing estimate, and the scope corrections in §4(c). Identify any error, missing hypothesis, or overstatement, and say precisely how to repair it. Also say whether Lemma 69.Y / alpha<=4p_*/A is standard (do not invent references; name a knowledge_request if needed).

## Output

# Scientific verification memo

## 1. Lemma 69.Y: the stated equality for \(\mathcal E(\hat g)\) is incorrect

Let \(\hat g\) have constant scalar curvature \(\hat s\ne0\), volume \(\hat V\), and put \(\hat P=P(\hat g)\). Then
\[
\int |\operatorname{Ric}-\lambda \hat g|^2
=\hat P+4\hat V\left(\frac{\hat s}{4}-\lambda\right)^2.
\]
Consequently
\[
\frac{\int |\operatorname{Ric}-\lambda\hat g|^2}{\lambda^2\hat V}
=4-2\hat s\,\lambda^{-1}
+\left(\frac{\hat P}{\hat V}+\frac{\hat s^2}{4}\right)\lambda^{-2}.
\]
Minimizing in \(x=\lambda^{-1}\) gives
\[
\lambda_*=\frac{\hat P+\hat s^2\hat V/4}{\hat s\hat V}
=\frac{\hat s}{4}+\frac{\hat P}{\hat s\hat V}
\]
and therefore
\[
\boxed{\;
\mathcal E(\hat g)
=\frac{16\hat P}{4\hat P+\hat s^2\hat V}
=\frac{16P(\hat g)}{4P(\hat g)+Y[g]^2}.
\;}
\]
The value
\[
\frac{16P(\hat g)}{Y[g]^2}
\]
is only the evaluation at \(\lambda=\hat s/4\), not the infimum unless \(P(\hat g)=0\). The JSON and Python script verify that evaluation but do not perform the minimization over \(\lambda\).

The conformal comparison for \(P\) is correct. With the norm convention in the note,
\[
P(g)=\int\left(4|W^+|^2+\frac{s^2}{12}\right)d\mu
-8\pi^2(2\chi+3\tau).
\]
Since \(\int|W^+|^2d\mu\) is conformally invariant, LeBrun’s Lemma 1 gives
\[
P(g)-P(\hat g)
=|\hat s|\int|\nabla\phi|_g^2\,d\mu_g
+3\int\left(\frac{\Delta_g\phi}{\phi}\right)^2d\mu_g.
\]
Thus \(P(\hat g)\le P(g)\), and the corrected conclusion is actually stronger:
\[
\boxed{\;
\alpha(M)\le
\frac{16P(g)}{4P(g)+Y[g]^2}
\le \frac{16P(g)}{Y[g]^2}.
\;}
\]
So every upper inequality derived in the note remains valid, despite the incorrect equality.

## 2. Corollary 69.Y′ and the LeBrun input

For each metric polarization, the required sign-selected class has the form
\[
a=c+\sum_i\epsilon_iE_i,
\]
with signs chosen so that
\[
(a^+)^2\ge(c^+)^2\ge c^2=A.
\]
The \(S^1\times S^3\) summands do not alter \(H^2\); their role is in the higher-dimensional Seiberg–Witten invariant through loop insertions. For \(b^+=1\), the chamber must be selected relative to \(H^+(g)\). Since the Hodge star on two-forms is conformally invariant in dimension four, the initial metric and its Yamabe representative have the same polarization.

One logical step should be added. The scalar estimate by itself does not imply \(Y[g]<0\) when \(Y[g]>0\). Rather:

- a Yamabe representative with scalar \(>0\) is incompatible with the supplied actual monopole through the usual Weitzenböck argument;
- \(Y[g]=0\) is incompatible with
  \(\int s^2\ge32\pi^2A>0\).

Hence \(Y[g]<0\), and applying the scalar estimate to the Yamabe representative yields
\[
Y[g]^2\ge32\pi^2A.
\]

Combining this with the corrected defect formula gives
\[
\boxed{\;
\alpha(M)\le
\frac{16P(g)}{4P(g)+32\pi^2A}
=\frac{4p(g)}{A+p(g)},
\qquad p(g)=\frac{P(g)}{8\pi^2}.
\;}
\]
In particular,
\[
\boxed{\;
\alpha(M)\le\frac{4p_*(M)}{A+p_*(M)}
\le\frac{4p_*(M)}{A}.
\;}
\]
Thus the displayed \(\alpha\le4p_*/A\) is correct but not the strongest consequence.

The supplied 1996 paper supports the conformal scalar identity and the blow-up scalar estimate. Independent source confirmation of the handle and \(b^+=1\) quantifiers requires:

> **knowledge_request:** retrieve the complete statement and proof of LeBrun’s 2001 Proposition 3.2, including its hypotheses on \(b^+=1\), \(b_1>0\), the \(\#_\ell(S^1\times S^3)\) loop insertions, and whether the resulting structure is supplied for every metric polarization.

## 3. The balanced ball-quotient theorem

### Topology and arithmetic

For a compact ball quotient with \(\operatorname{Ric}=-g\),
\[
V=2\pi^2A,\qquad \chi=\frac A3,\qquad \tau=\frac A9.
\]
For \(k=8n\), \(\ell=7n\),
\[
Q=k+4\ell=36n,
\]
and
\[
T_+=A-k-4\ell=A-Q,
\]
while
\[
T_-=\frac A3+5k-4\ell=\frac A3+12n.
\]
Therefore
\[
\frac{3T_-}{A}=1+\frac{36n}{A}=1+h,
\qquad
\theta=\frac{k}{Q}=\frac29,
\qquad
\sigma=18\theta=4.
\]
The script and JSON arithmetic are correct.

### Injectivity radius

The residual-finiteness argument needs a small repair. Excluding group elements whose displacement at one selected base point is \(<4R_c\) does not by itself control the global injectivity radius. A short translation axis may lie far from that base point.

Two standard repairs are available:

1. exclude representatives of all conjugacy classes with translation length at most \(4R_c\); compactness gives only finitely many such classes, and normality excludes all conjugates; or
2. if \(D\) is the diameter of a compact fundamental set, exclude every element with base-point displacement at most \(4R_c+2D\).

Residual finiteness then gives a finite normal cover \(X'\) with
\[
\operatorname{inj}(X')>2R_c.
\]
Every further finite cover has at least this injectivity radius.

For a maximal \(2R_c\)-separated set, the \(R_c\)-balls are disjoint and the \(2R_c\)-balls cover. In fact,
\[
N(X)\ge \frac{\operatorname{Vol}(X)}{v_{CH}(2R_c)}
\ge\frac{2\pi^2A}{v_{CH}(4R_c)}.
\]
Thus the weaker count used in the note is valid.

### Use of the certified \(P\)-cell

Replacing the \(J\)-endpoint by the certified \(P\)-endpoint is legitimate:

- the exterior KE region has \(\operatorname{Ric}^{\circ}=0\);
- the cells are exactly CH on their collars;
- hence \(P\) is additive over the inserted regions;
- the exact-collar smoothing changes \(P\) by an arbitrarily small amount.

With
\[
p_c=
\frac{338806471362324583565914367157197246841}
{2^{128}},
\]
the normalized total energy is
\[
\frac{P(\tilde g)}{8\pi^2}
\le 8n\,p_c+28n+o(1).
\]
The note’s linear estimate follows:
\[
\frac{\alpha(M)}h
\le\frac{28}{9}+\frac89p_c
=3.9961446513521015108\ldots.
\]

The corrected defect minimization gives the stronger finite-\(h\) form. Writing
\[
C_c=\frac{28}{9}+\frac89p_c,
\]
one gets
\[
\boxed{\;
\frac{\alpha(M)}h
\le \frac{C_c}{1+C_ch/4}
\le C_c.
\;}
\]
Thus the stated coefficient is valid uniformly, while the sharper expression records the denominator discarded in Lemma 69.Y.

The phrase “no limit” should be replaced by “no cover-degree or \(h\to0\) passage.” The construction still uses shrinking handle cores and arbitrarily small collar-smoothing loss when passing to the infimum.

## 4. The handle model \(H'\)

The geometric computation is correct.

The round product \(S^1\times S^3\) is locally conformally flat and has positive constant scalar curvature. Its conformal Laplacian therefore has a positive Green function. The Green-function metric on
\[
N=(S^1\times S^3)\setminus\{p\}
\]
is complete, scalar-flat, conformally flat, and AE of order two.

Since \(\chi(N)=-1\), the one-ended AE Gauss–Bonnet formula gives
\[
\int_N\left(|W|^2+\frac{s^2}{24}
-\frac{|\operatorname{Ric}^{\circ}|^2}{2}\right)d\mu
=8\pi^2(\chi(N)-1)=-16\pi^2.
\]
As \(W=s=0\),
\[
\boxed{P(N)=32\pi^2.}
\]

For insertion into a background, the clean argument uses
\[
P=\int F_+\,d\mu-8\pi^2T_+,
\qquad
F_+=4|W^+|^2+\frac{s^2}{12}.
\]
Connected summing with \(S^1\times S^3\) changes \(T_+\) by \(-4\), so
\[
P(\tilde g)-P(g)
=32\pi^2+\int\!\bigl(F_+(\tilde g)-F_+(g)\bigr).
\]
Because the inserted AE model has
\[
\mathcal C=(2W^+,s/\sqrt{12})=0,
\]
only cross terms with the background normal-coordinate jet remain. On the intermediate region these are
\[
\mathcal C(\tilde g)-\mathcal C(g)
=O(\delta^2r^{-2}),
\]
and their integrated contribution tends to zero. The fixed outer interpolation contributes \(O(\delta^2)\).

One sentence needs correction: the full curvature on the scaled core is generally \(O(\delta^{-2})\), not \(O(1)\). What is \(O(1)\) after adding the background jet is the chiral curvature \(\mathcal C\) relevant to \(F_+\); its core contribution is \(O(\delta^4)\). With this wording,
\[
P(\tilde g)=P(g)+32\pi^2+o(1)
\]
is justified.

## 5. Theorem 69.KE

### Fixed minimal surface

Corollary 59.KE, with the order of limits recorded in Part D, supplies a smooth competitor with
\[
\frac{P}{8\pi^2}<k.
\]
Therefore
\[
\alpha(X\#k\overline{\mathbb{CP}}^2)
<\frac{4k}{A+k}
<\frac{4k}{A}.
\]
So part (a) is correct and admits this stronger form. For canonical models with ADE points, fixing the Burns scale first and then sending the Kronheimer scale to zero is essential and is correctly stated.

### Finite covers and mixed surgery

The constants in Theorem 59.R depend only on finitely many local derivatives, the cutoff data, and the selected insertion direction. Every lift is locally isometric to the base, so the same \(\varepsilon_X\), support radius, remainder constant, and
\[
\eta_X=1-p_{\mathrm{cell}}(\varepsilon_X)>0
\]
work on all covers.

If \(Q=k+4\ell>0\) and the packing condition
\[
k+\ell\le d_mN_X(\rho_X)
\]
holds, then
\[
\frac{P}{8\pi^2}\le Q-k\eta_X+o(1).
\]
Hence
\[
\boxed{\;
\frac{\alpha}{h}
\le
\frac{4(1-\theta\eta_X)}
{1+h(1-\theta\eta_X)}
\le4-4\theta\eta_X.
\;}
\]
The displayed estimate in the note is therefore valid. For each finite number of handles, their scales can be chosen so the aggregate gluing error tends to zero.

### Unramified covers of a fixed non-ball host

For a degree-\(d_m\) unramified cover,
\[
A_m=d_mA_X,\qquad
\Delta_m=d_m\Delta_X.
\]
Thus
\[
r_m=\frac{\Delta_m}{Q_m}
=\frac{\Delta_X}{h_mA_X},
\qquad
\sigma_m=4r_m+18\theta_m.
\]
If \(\Delta_X>0\) and \(h_m\to0\), then \(r_m,\sigma_m\to\infty\). The balanced equation \(\sigma=4\) requires
\[
r=1-\frac92\theta\le1,
\]
hence necessarily
\[
h\ge\frac{\Delta_X}{A_X}.
\]
This part is correct.

The final two-sided-window sentence needs the inherited hypothesis
\[
0<h\le\frac13
\quad\text{or, equivalently for that argument,}\quad
0\le\theta_\Delta\le\frac13,
\]
as well as the packing condition for the upper construction. Without this, the explicit lower branch from Step 33 is not available as stated.

Also, the geometric conclusion should be phrased for unramified towers of one fixed host. More general sequences of distinct hosts could also reach the balanced small-\(h\) regime whenever \(\Delta_m/A_m\to0\); the ramified towers are one supplied realization.

## 6. Literature status

LeBrun’s 1996 Lemma 1 supplies the scalar conformal identity. The \(P\)-identity then follows immediately from Chern–Gauss–Bonnet, signature, and conformal invariance of \(\int|W^+|^2\). The minimization in \(\lambda\) is an elementary one-variable calculation.

No supplied source states the combined estimate
\[
\alpha\le\frac{4p_*}{A+p_*}
\]
or its weaker form \(4p_*/A\) verbatim. It is best presented as a direct corollary of those ingredients. A publication-precedence search would require:

> **knowledge_request:** search the literature for the direct Einstein-defect functional  
> \(\inf_{\lambda\ne0}\int|\operatorname{Ric}-\lambda g|^2/(\lambda^2V)\)  
> combined with Yamabe minimization and LeBrun’s scalar estimate, especially an explicit inequality of the form \(\alpha\le4p_*/(A+p_*)\).

In summary, the \(P\)-cell coefficient, topology, AE handle tariff, cover uniformity, and fixed-host slope computation are sound. The principal mathematical repair is the exact minimization over \(\lambda\); it preserves every stated upper estimate and strengthens all of them.