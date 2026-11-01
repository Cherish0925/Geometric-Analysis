# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 72,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step72_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step72_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify every statement (A)–(G) in this focused bundle. Check constants, conformal/Yamabe quantifiers, Ricci-flat boundary cases, dumbbell smoothness and O(1) estimates, connected-sum deficit arithmetic, the #n CPbar2 threshold, the general-type KE deficit, and the conversion to the W+ inequality in the stated endomorphism norm. Give corrected statements and concise proofs wherever needed. Do not assume the desired result.

## Integrated Scientific Memo

# Verification memo: statements (A)–(G)

All seven displayed statements are valid with the domain qualifications below. The substantive repairs are:

- The defining quotient gives **\(\mathcal E(g)=4\) at a Ricci-flat metric**, not a value obtained by extending the \(R>0\) formula.
- (D) requires a conformal-class minimization argument, including \(S(g)\ge Y([g])^2\) for **negative** Yamabe classes.
- The numerical dumbbell uses a **\(C^2\), not smooth**, interpolation. A \(C^\infty\) cutoff repairs it without changing the estimates.
- The blow-up signature formula preceding (G) is wrong. It must be
  \[
  \tau(X\#k\overline{\mathbb{CP}}^2)
  =\frac{A-2\chi(X)}3-k.
  \]
  The final constant in (G) is nevertheless correct.

Here \(\alpha(M)=\inf_g\mathcal E(g)\), with \(\mathcal E\) interpreted by its original definition.

## 1. The functional and the Ricci-flat boundary

Since \(|g|^2=4\) and \(\langle\operatorname{Ric},g\rangle=s\),
\[
\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2V}
=4-\frac{2T_s}{V\lambda}+\frac{R}{V\lambda^2}.
\]
Minimizing in \(x=1/\lambda\neq0\) gives, when \(R>0\),
\[
\mathcal E=4-\frac{T_s^2}{RV}
=\frac{4P+L_s}{R}.
\]
If \(T_s=0\), the minimum of the quadratic occurs at the excluded point \(x=0\), but its **infimum** is still \(4\).

If \(R=0\), then \(\operatorname{Ric}\equiv0\), and the original quotient is identically \(4\). Thus
\[
\boxed{\mathcal E(g)=4\quad\text{when }R=0.}
\]
In this case \(P=S=T_s=L_s=0\), and Gauss–Bonnet gives \(d=0\). In particular, Ricci-flat metrics cannot contribute values below \(1\). Universally, \(0\le\mathcal E\le4\).

## 2. (A) and (B): identities and their domains

Gauss–Bonnet gives
\[
P=\frac S{12}+2\mathcal W-16\pi^2\chi,\qquad
R=\frac S3+2\mathcal W-16\pi^2\chi.
\]
Consequently, for \(R>0\),
\[
R(\mathcal E-1)=3P-\frac S4+L_s
=6(\mathcal W-8\pi^2\chi)+L_s.
\]
Thus **(A) is correct**:
\[
\boxed{\mathcal E-1=\frac{-6d+L_s}{R}.}
\]

A Yamabe representative means a minimizer of the Yamabe quotient, not merely an arbitrary constant-scalar-curvature representative. For such a metric,
\[
S(\widehat g)=Y([g])^2,\qquad L_s(\widehat g)=0,
\]
and hence
\[
P(\widehat g)=\frac{Y^2}{12}-2d,\qquad
R(\widehat g)=\frac{Y^2}{3}-2d.
\]
Therefore **(B) is correct whenever \(R(\widehat g)>0\)**:
\[
\boxed{\mathcal E(\widehat g)=1-\frac{6d}{R(\widehat g)}.}
\]

The zero-Yamabe cases are explicit:
\[
Y=0\implies P(\widehat g)=R(\widehat g)=-2d,\qquad d\le0.
\]
If \(d<0\), the formula gives \(\mathcal E(\widehat g)=4\). If \(d=0\), the Yamabe metric is Ricci-flat and again has \(\mathcal E=4\), but the displayed ratio is undefined. These are the only \(R(\widehat g)=0\) cases.

## 3. (C) and (D): all conformal quantifiers

### The threshold criterion (C)

If \(\mathcal E(g)<1\), then \(R>0\), and (A) implies
\[
6d>L_s\ge0.
\]
Conversely, \(d>0\) rules out \(Y=0\), since its scalar-flat Yamabe metric would have \(P=-2d<0\). Its Yamabe representative therefore has \(R>0\), and (B) gives \(\mathcal E<1\).

Thus **(C) is correct**, with the simpler equivalent forms
\[
\boxed{
\alpha(M)<1
\iff \exists[g]\colon d([g])>0
\iff \mathcal W_*(M)<8\pi^2\chi(M)
\iff d_*(M)>0.
}
\]
The condition \(Y([g])\neq0\) in (C) is automatic.

### The missing conformal minimization lemma

For every \(g\) in a fixed conformal class,
\[
\boxed{S(g)\ge Y([g])^2.}
\]
For \(Y>0\), testing the Yamabe quotient with \(1\) gives
\[
Y\le T_s/\sqrt V\le\sqrt S.
\]
For \(Y\le0\), write \(s_-=\max\{-s,0\}\). For every test function \(u\neq0\),
\[
Q_g(u)
=\frac{\int(6|\nabla u|^2+s_gu^2)}{(\int u^4)^{1/2}}
\ge-\|s_-\|_2.
\]
Taking the infimum gives \(Y\ge-\|s_-\|_2\), so
\[
|Y|\le\|s_-\|_2\le\sqrt S.
\]

In a class with \(d>0\),
\[
P(\widehat g)\ge0
\implies Y^2\ge24d,
\qquad R(\widehat g)=Y^2/3-2d\ge6d>0.
\]
Every representative satisfies
\[
R(g)=S(g)/3-2d\ge R(\widehat g).
\]
Using (A),
\[
\mathcal E(g)
=1+\frac{L_s(g)-6d}{R(g)}
\ge1-\frac{6d}{R(g)}
\ge1-\frac{6d}{R(\widehat g)}
=\mathcal E(\widehat g).
\]
Thus a Yamabe representative minimizes \(\mathcal E\) in every **positive-deficit** class. Equality requires \(L_s=0\) and \(S=Y^2\), which also makes \(g\) a Yamabe minimizer.

Classes with \(d\le0\) give \(\mathcal E\ge1\) when \(R>0\); their Ricci-flat representatives give \(4\). Combining this with the dumbbell upper bound below proves **(D)**. An unambiguous form, including the empty-set convention, is
\[
\boxed{
\alpha(M)=1-6\sup\left(
\{0\}\cup
\left\{\frac{d([g])}{Y([g])^2/3-2d([g])}:d([g])>0\right\}
\right).
}
\]
This equals the bundle’s formula. Classes with \(Y\neq0,d\le0\) only add nonpositive ratios. The denominator is independent of the choice of Yamabe minimizer, and positive-deficit ratios lie in \((0,1/6]\).

## 4. Dumbbell smoothness, estimates, and (E)

For
\[
g=dr^2+f(r)^2g_{S^3(1)},
\]
the sectional curvatures are
\[
K_{0a}=-f''/f,\qquad K_{ab}=(1-(f')^2)/f^2.
\]
Where \(f>0\), setting \(dt=dr/f\) shows that \(g\) is conformal to \(dt^2+g_{S^3}\), hence locally conformally flat. Taking \(f=\sin r\) near each pole ensures smoothness there.

On \(f\equiv1\),
\[
\operatorname{Ric}=(0,2,2,2),\quad s=6,\quad
|\operatorname{Ric}^\circ|^2=3,\quad|\operatorname{Ric}|^2=12.
\]
With \(v=\operatorname{Vol}(S^3)=2\pi^2\), all cylinder contributions are therefore correct.

A smooth fixed cap is obtained using an endpoint-flat \(C^\infty\) cutoff to interpolate from \(\sin r\) to \(1\). After inserting a fixed punctured metric on \(M\) through a fixed smooth neck, the resulting metric is on \(M\#S^4\cong M\). Everything outside the length-\(L\) cylinder is independent of \(L\). Thus, exactly,
\[
\begin{aligned}
V&=vL+V_0,&T_s&=6vL+T_0,&S&=36vL+S_0,\\
P&=3vL+P_0,&R&=12vL+R_0.
\end{aligned}
\]
In particular,
\[
L_s=S_0-12T_0+36V_0
-\frac{(T_0-6V_0)^2}{vL+V_0}=O(1),
\]
and
\[
\mathcal E(g_L)=1+O(L^{-1})\longrightarrow1.
\]
This proves **(E)** for every closed four-manifold.

**Numerical artifact correction.** The quintic smoothstep in `step72_dumbbell_numeric.py` matches only two derivatives at the start of the blend, so its metric is not \(C^\infty\). Its curvature formulas and integrals are consistent for that \(C^2\) model, but its cap values must not be presented as values for the repaired smooth metric. Smoothing changes only the fixed constants. The recorded data support the asymptotics; they do not establish smoothness or replace the proof.

For the numerical model, the exact formula above predicts
\[
L_s\to S_0-12T_0+36V_0\approx1520.79,
\qquad
L(\mathcal E-1)\to\frac{1520.79-96\pi^2}{24\pi^2}\approx2.420.
\]
These agree with the supplied trends. The construction need not approach \(1\) from below.

### The \(T_{\min}\le0\) conclusion and attainment

Signature gives
\[
\mathcal W\ge12\pi^2|\tau|,
\qquad
d\le4\pi^2(2\chi-3|\tau|)=4\pi^2T_{\min}.
\]
Hence \(T_{\min}\le0\) implies \(\mathcal E\ge1\), and (E) yields
\[
\boxed{\alpha=1.}
\]

- If \(T_{\min}<0\), every metric has \(\mathcal E>1\); the infimum is not attained.
- If \(T_{\min}=0\), attainment is equivalent to a conformal class with
  \[
  \mathcal W=12\pi^2|\tau|,\qquad Y\neq0.
  \]
  Its Yamabe metric attains \(1\).

The Weyl equality means \(W^-=0\) when \(\tau>0\), and \(W^+=0\) when \(\tau<0\). When \(\tau=0\), it means **\(W=0\)**. At \(\tau=0\), either half-flat condition already forces the other through signature. Thus the bundle’s half-conformally-flat formulation is valid, but this orientation and zero-signature clarification is useful. A scalar-flat equality metric would be Ricci-flat and have \(\mathcal E=4\), so \(Y\neq0\) is essential.

## 5. (F) and the exact \(\#_n\overline{\mathbb{CP}}^2\) deficit

Weyl-energy connected-sum subadditivity gives
\[
\mathcal W_*(M\#N)\le\mathcal W_*(M)+\mathcal W_*(N).
\]
It can also be justified directly: in normal coordinates, flatten each metric in a radius-\(\varepsilon\) ball. Since \(g-\delta=O(r^2)\), cutoff derivatives leave curvature uniformly \(O(1)\) in the transition annulus, whose energy is \(O(\varepsilon^4)\). Join the flat patches by a smooth conformally flat warped neck, adding no Weyl energy, and let \(\varepsilon\to0\).

Together with \(\chi(M\#N)=\chi(M)+\chi(N)-2\), this proves **(F)**:
\[
\boxed{d_*(M\#N)\ge d_*(M)+d_*(N)-16\pi^2.}
\]

For \(\overline{\mathbb{CP}}^2\), signature gives \(\mathcal W\ge12\pi^2\), and reversed Fubini–Study attains equality. Thus \(d_*=12\pi^2\). Iteration gives
\[
d_*(\#_n\overline{\mathbb{CP}}^2)\ge(16-4n)\pi^2.
\]
In fact this is **exact**: \(\chi=n+2,\tau=-n\), so signature supplies the matching upper bound. Therefore, for \(n\ge1\),
\[
\boxed{
\mathcal W_*(\#_n\overline{\mathbb{CP}}^2)=12n\pi^2,\qquad
d_*=4\pi^2(4-n).
}
\]
Consequently,
\[
\boxed{
n\le3:\ \alpha<1;\qquad
n\ge4:\ \alpha=1.
}
\]
For \(n>4\), \(1\) is not attained. At \(n=4\), attainment is equivalent to a \(W^+=0\) class with \(Y\neq0\); existence of such a class is not established by this bundle.

## 6. General-type KE deficit and (G)

Assume that \(X\) actually carries a **smooth negative Kähler–Einstein metric**, \(\operatorname{Ric}=\lambda g\), \(\lambda<0\). Minimal general type alone should not be substituted for that hypothesis.

With the complex orientation, the Ricci form satisfies
\[
\rho=\lambda\omega,\qquad [\rho]=2\pi c_1(X).
\]
Thus
\[
A=c_1^2(X)=\frac{\lambda^2}{4\pi^2}\int\omega^2
=\frac{\lambda^2V}{2\pi^2},
\]
and
\[
R=4\lambda^2V=8\pi^2A.
\]
Since \(P=L_s=0\), (A) gives
\[
\boxed{d=R/6=\frac{4\pi^2A}{3}.}
\]
Applying (F) \(k\) times yields
\[
\boxed{
d_*(X\#k\overline{\mathbb{CP}}^2)
\ge4\pi^2(A/3-k).
}
\]
Therefore \(k<A/3\) implies \(\alpha<1\).

For \(M=X\#k\overline{\mathbb{CP}}^2\), the corrected topology is
\[
A=2\chi(X)+3\tau(X),\quad
\chi(M)=\chi(X)+k,\quad
\tau(M)=\frac{A-2\chi(X)}3-k,
\]
so
\[
2\chi(M)+3\tau(M)=A-k.
\]
Writing \(U(g)=\int|W^+|^2\), signature gives the pointwise-in-metric energy identity
\[
\mathcal W(g)=2U(g)-12\pi^2\tau(M).
\]
It follows that
\[
\begin{aligned}
\inf_g\mathcal W(g)<8\pi^2\chi(M)
&\iff \inf_g U(g)<4\pi^2\chi(M)+6\pi^2\tau(M)\\
&\iff \boxed{\inf_g\int|W^+|^2<2\pi^2(A-k).}
\end{aligned}
\]
This proves **(G)** in the stated endomorphism norm. If
\[
|W^\pm|_{(0,4)}^2=4|W^\pm|_{\mathrm{end}}^2,
\]
the corresponding right-hand side is \(8\pi^2(A-k)\).

The equivalence holds for every \(k\), not just the indicated band. For \(k\ge A\), its right-hand side is nonpositive and the strict inequality is impossible; hence \(\alpha=1\). In the remaining band \(A/3\le k<A\), the supplied results establish the exact criterion (G), but do **not** determine whether it holds. The unresolved object is the pure self-dual Weyl-energy infimum on these blow-ups; resolving it requires a matching lower bound or actual metrics crossing the displayed threshold. No additional gauge-theoretic estimate supplied here closes that question.