# From LeBrun saturation to Ricci-energy selection

23 September 2026. This note separates two consequences of LeBrun
near-equality. The first requires no geometric bounds and determines the
trace-free Ricci energy of every sequence saturating the classical absolute
Ricci-energy bound. The second uses the scalar-band remainder and a scalar
Poincaré bound to obtain an integral almost-Einstein conclusion without
assuming that Ricci curvature is already almost Einstein.

The first consequence is an explicit stability calculation from classical
curvature inequalities and Chern–Weil identities. The second also uses the
new scalar-variance remainder in `line1_scalar_band_remainder.md`. Neither
asserts a new global Einstein-existence theorem or a pointwise Ricci bound.

## 1. Exact identities and a scalar-energy remainder

Let \((M,g)\) be a smooth closed connected oriented four-manifold. Suppose
a specified Spin\(^c\) structure with real class \(a\) has ordinary
Seiberg–Witten solutions for every metric conformal to \(g\). Put

\[
 p=(a_g^+)^2>0,\quad A=a^2,\quad T=2\chi(M)+3\tau(M),\quad
 V=\operatorname{Vol}(M,g),
\]
\[
 S_2=\int s^2,\quad P=\int|\operatorname{Ric}^{\circ}|^2,\quad
 R_2=\int|\operatorname{Ric}|^2=P+\frac{S_2}{4},
\]
\[
 D=\frac1{4\pi^2}\int
       \left(\frac{s^2}{24}+\frac{|W^+|^2}{2}\right)-\frac p2,
 \qquad \delta=144\pi^2D.
 \tag{1}
\]

Weyl norms are Hilbert–Schmidt operator norms on two-forms. All other
curvature norms are ordinary tensor norms. The metric may vary together
with the class; the solvability assumption keeps the selected class fixed
only during conformal rescaling of that metric.

The classical scalar and signed spectral monopole inequalities give

\[
 S_2\ge32\pi^2p,\qquad
 \int(-s+\sqrt6|W^+|)_+^2\ge72\pi^2p.
 \tag{2}
\]

For completeness, the first follows by pairing the ordinary spinor
Weitzenböck equation with the spinor, applying Cauchy–Schwarz to the scalar
term, and using the harmonic projection of its actual determinant
curvature. The second follows from the weighted equations and the
lowest-eigenvalue estimate. The precise normalized derivations, including
sign-changing scalar curvature, are in `round3_monopole_input.md`, Section
6; no pointwise scalar or geometric hypothesis is used there.

Define the *polarized* scalar excess

\[
 B_p=S_2-32\pi^2p\ge0.
 \tag{3}
\]

Chern–Weil gives the following exact identities:

\[
 \boxed{
 R_2=8\pi^2(2p-T)+32\pi^2D,
 \qquad
 P+\frac{B_p}{4}=8\pi^2(p-T)+32\pi^2D.}
 \tag{4}
\]

In terms of \(B=S_2-32\pi^2A\), the equivalent formula is

\[
 P+\frac B4
 =16\pi^2(p-A)+8\pi^2(A-T)+32\pi^2D.
 \tag{5}
\]

Using only \(B\ge0\) loses information: in fact
\(B\ge32\pi^2(p-A)\). The sharper identity (4) will be used below.

There is also a geometry-free quantitative upper bound for \(B_p\):

\[
 \boxed{
 0\le B_p\le b(\delta,p)
 :=\frac49\left[\delta+
       \sqrt{2\delta(72\pi^2p+\delta)}\right].}
 \tag{6}
\]

**Proof.** Set \(w=\sqrt6|W^+|\), \(q=-s+w\), and \(t=s+2w\).
Write \(q_-:=\max\{-q,0\}\) and
\(\Delta_+=\int q_+^2-72\pi^2p\ge0\). The elementary square
identity yields

\[
 \delta=\Delta_++\int q_-^2+\frac12\int t^2.
 \tag{7}
\]

Thus \(D\ge0\), and
\(\beta:=\int q^2-72\pi^2p=\Delta_++\int q_-^2\ge0\).
Since \(s=(t-2q)/3\),

\[
 B_p=\frac49\beta-\frac49\int qt+\frac19\int t^2.
 \tag{8}
\]

Now \(\beta+\frac12\int t^2=\delta\), so
\(4\beta+\int t^2\le4\delta\). Also
\(\int q^2\le72\pi^2p+\delta\) and \(\int t^2\le2\delta\).
Cauchy–Schwarz in (8) proves (6). This proof uses neither the scalar-band
theorem nor any regularity or compactness theorem.

## 2. All metrics near the absolute Ricci-energy bound

Fix numbers \(A_0>0\), \(d\ge0\), and a smooth topology with
\(T=A_0-d\). Suppose the metricwise class in Section 1 satisfies
\(p\ge A_0\). Define

\[
 \varepsilon=R_2-8\pi^2(A_0+d).
 \tag{9}
\]

**Theorem 1.** Every such metric satisfies

\[
 \varepsilon=16\pi^2(p-A_0)+32\pi^2D\ge0,
 \tag{10}
\]
\[
 \boxed{
 8\pi^2d-\sqrt{\varepsilon(8\pi^2A_0+\varepsilon)}
 \le P\le8\pi^2d+\varepsilon.}
 \tag{11}
\]

In particular, any sequence with \(\varepsilon_j\to0\) satisfies

\[
 p_j\to A_0,\qquad D_j\to0,\qquad
 S_{2,j}\to32\pi^2A_0,\qquad
 P_j\to8\pi^2d.
 \tag{12}
\]

No scalar band, volume normalization, spectral gap, Kähler hypothesis,
noncollapse, or uniform Sobolev constant is assumed.

**Proof.** Equation (10) follows from (4). It implies
\(p-A_0\le\varepsilon/(16\pi^2)\) and
\(\delta\le(9/2)\varepsilon\). Equation (6), whose right side is
increasing in both arguments, therefore gives

\[
 B_p\le2\varepsilon
              +4\sqrt{\varepsilon(8\pi^2A_0+\varepsilon)}.
 \tag{13}
\]

From the first identity in (4),

\[
 P-8\pi^2d
 =\varepsilon-8\pi^2(p-A_0)-\frac{B_p}{4}.
 \tag{14}
\]

The middle term lies between \(0\) and \(\varepsilon/2\).
Use \(B_p\ge0\) for the upper bound and (13) for the lower bound.
This proves (11); (12) follows immediately.

For the classical general-type application,
\(A_0=c_1^2(X)\) and \(d=k+4\ell\) for
\(X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3)\).
The required metricwise class selection and conformal solvability must
be supplied by the appropriate blow-up/connected-sum and chamber results.
Theorem 1 does not replace those topological inputs or assert the
existence of a minimizing sequence where attainability of the numerical
infimum is not known. Where the classical absolute Ricci-energy infimum
is known to equal the bound, its conclusion applies to **every**
minimizing sequence, not just the Kähler or explicit gluing examples.

### Relative Einstein defect retains scalar variance

Let \(L=\int(s-\bar s)^2\) and define

\[
 \mathcal E(g)=\inf_{\lambda\ne0}
 \frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2 V}.
\]

Since \(R_2>0\), direct minimization in \(1/\lambda\) gives

\[
 \mathcal E=4-\frac{(\int s)^2}{VR_2}
            =\frac{4P+L}{R_2}.
 \tag{15}
\]

If \(\int s=0\), the value is the infimum \(4\) as
\(|\lambda|\to\infty\); no finite optimizer is being asserted.
Along a sequence from (12), \(0\le L_j\le S_{2,j}\) is bounded, and

\[
 \boxed{
 \mathcal E(g_j)=\frac{4d}{A_0+d}
       +\frac{L_j}{8\pi^2(A_0+d)}+o(1).}
 \tag{16}
\]

Thus \(d>0\) gives a strictly positive limiting lower bound for the
relative Einstein defect of absolute Ricci-energy minimizers. If
\(d=0\), their relative Einstein defect tends to zero **if and only if**
their scalar variance tends to zero. No geometric assumption in this
section supplies that variance conclusion. This is precisely the term
that must remain when passing from Kähler test families to all metrics.

## 3. A converse bridge with scalar-band and spectral control

Assume in addition to Section 1 that
\(-S\le s\le-s_0<0\). Put

\[
 K=\frac S{\sqrt{s_0}},\qquad
 C_0=\left(1+\frac{3S}{2s_0}\right)^2,\qquad
 C_{\rm var}=\frac23+\frac{4C_0}{3}
                         +\frac{2K^2}{\lambda_1(g)},
 \tag{17}
\]

where \(\lambda_1(g)>0\) is the first positive scalar Laplace
eigenvalue. The independently established scalar-band remainder gives

\[
 L\le144\pi^2C_{\rm var}D.
 \tag{18}
\]

Let \(\kappa=-\bar s/4>0\), and set
\(Q_\kappa=\int|\operatorname{Ric}+\kappa g|^2=P+L/4\).

**Theorem 2.** Without assuming any Ricci bound,

\[
 \boxed{
 Q_\kappa\le8\pi^2(p-T)
                  +(32\pi^2+36\pi^2C_{\rm var})D.}
 \tag{19}
\]

In particular, define the nonnegative primitive/topological supply

\[
 \mathcal P=(p-A)+(A-T)_+,\qquad
 U=8\pi^2\mathcal P+(32\pi^2+36\pi^2C_{\rm var})D.
 \tag{20}
\]

Then

\[
 \boxed{
 Q_\kappa\le U,\qquad
 \mathcal E(g)\le\frac{4U}{4\kappa^2V+U}
                   \le\frac{16U}{s_0^2V}.}
 \tag{21}
\]

**Proof.** The nonnegative \(B_p\) in (4) yields
\(P\le8\pi^2(p-T)+32\pi^2D\). Adding (18)/4 proves (19).
Since \(p-A=\|a_g^-\|_2^2\ge0\), \(p-T\le\mathcal P\).
Finally
\(R_2=4\kappa^2V+Q_\kappa\) and
\(\mathcal E=4Q_\kappa/(4\kappa^2V+Q_\kappa)\), while
\(\kappa\ge s_0/4\). This proves (21).

For a sequence in a fixed scalar band, the sufficient conditions are

\[
 \frac{\mathcal P_j}{V_j}\to0,\qquad
 \frac{D_j}{V_j}\to0,\qquad
 \frac{D_j}{\lambda_1(g_j)V_j}\to0.
 \tag{22}
\]

A uniform positive scalar spectral gap is one way to ensure the third
condition, not the only way. It must not be omitted. The conclusion is
relative integral Einstein approximation; no \(L^\infty\) Ricci
approximation or exact Einstein metric follows from this proof.

At equality \(D=0\), the scalar-band theorem gives a compatible negative
cscK metric. If also \(\mathcal P=0\), (21) forces
\(Q_\kappa=0\), hence negative Kähler–Einstein. The primitive supply
excludes unequal-curvature hyperbolic products: for them \(D=0\) but
\(p-A>0\).

## 4. What is added, and what is not

The identities (4)–(5) are classical Chern–Weil algebra. Inequality (6)
retains the scalar-energy remainder quantitatively. Theorem 1 packages
these inequalities into an all-metric selection statement at the
classical absolute Ricci-energy boundary, with the explicit variance
term (16). It does not create a new absolute Ricci-energy infimum.

Round 17 takes \(P\) and scalar-normalization error as inputs to a
curvature-profile estimate. Theorem 2 instead obtains their sum from
LeBrun saturation, an actual polarized class, the primitive/topological
quantity, and the displayed scalar spectral control. This direction is
not obtained by simply feeding the already allowed Weyl root into the
Round 21 spectral-selection theorem. The new analytic dependency is
the scalar-variance bound (18), not another use of that spectral root.

The geometric limitation is correspondingly specific: absent spectral
control, small differential energy need not prevent scalar scale-splitting
across a degenerating geometry. Neither the theorem nor the all-metric
energy selection removes this issue.

### Sources and reproducibility

- Claude LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten
  Theory*, Propositions 4.1–4.2 and the general-type Ricci-energy
  applications: https://arxiv.org/abs/math/0003068.
- `round3_monopole_input.md`, Section 6: normalized scalar and signed
  spectral inequalities from actual weighted solutions.
- `line1_scalar_band_remainder.md`, equation (11): scalar variance from
  the retained weighted-monopole defects and scalar Poincaré inequality.
- `round17_integral.md`, Theorem 1 and Section 6: prior structural
  estimates with Ricci and scalar errors as inputs.
- `line1_ricci_remainder_check.py`: exact algebra and constant reductions
  in this note; it does not verify the PDE solvability hypotheses.
