# A joint gap from actual monopole classes with controlled square

19 September 2026. This note extends the intrinsic calibration theorem
of `round3_rigidity.md` beyond the blow-up specialization. The estimates
use no bound on the Euler characteristic divided by the monopole scale.
Actual monopole existence and the square of the selected class remain
separate, explicit hypotheses.

## 1. A metricwise theorem and its family version

Let `M` be a smooth closed connected oriented four-manifold, let `g` be a
smooth metric, and put

\[
 T=2\chi(M)+3\tau(M),\qquad
 \delta=\|g^{-1}\operatorname{Ric}_g+I\|_{\infty,\mathrm{op}}.
\]

Suppose `A>0` and an actual monopole class `a` have been supplied, with

\[
 p=(a^+)^2\ge A,\qquad a^2\ge-C_AA,\qquad C_A\ge0.
\tag{1}
\]

Here an actual monopole class has the rescaled Seiberg--Witten solvability
used in the intrinsic proof for every smooth positive weight. The two
squares in (1) have different meanings: the first uses the metric's
positive harmonic projection, while the second is topological.

Define

\[
 d_T=(T/A-2/3)_+.
\]

Let `c>0` be the universal constant in Theorem 2 of the intrinsic proof.
Then

\[
 \boxed{\quad
 \delta^2+d_T\ge c(C_A):=
 \min\left\{\frac1{4096},\,
 \frac{c}{760\left(1+25C_A/(32\pi^2)\right)}\right\}>0.
 \quad}
\tag{2}
\]

This theorem is metricwise: only the class selected for this metric is
needed. For a family statement valid for every metric, require for every
metric an actual class with the two properties (1), with the same `A`
for that manifold and a uniform constant `C_A` across the family. The
selected class may depend on the metric. The number `A`, the topology,
and the volume may all vary across the family.

An assertion about an abstract cohomology vector with large positive
projection is insufficient. Likewise, a monopole projection hypothesis
without any control of the selected class's negative square does not
by itself provide the uniform constant in (2).

## 2. Curvature and determinant budgets

It suffices to consider `delta<=1/64`. Use the same calibration density
`D`, its integral `d_cal`, and the selected class's deficit

\[
 q=-s+\sqrt6|W^+|,\qquad
 \Delta=\int q^2-72\pi^2p\ge0
\]

as in the intrinsic and blow-up notes. Let `V=Vol(M,g)` and
`P=integral |Ric^circ|^2`. The scalar monopole inequality gives

\[
 V\ge\frac{2\pi^2 A}{(1+\delta)^2}
        \ge\frac{32\pi^2 A}{25},\qquad
 P\le4\delta^2V.
\tag{3}
\]

For

\[
 I=(4\pi^2)^{-1}\int(s^2/24+2|W^+|^2),\qquad
 J=P/(8\pi^2),
\]

Chern--Weil says `I-J=T`, so

\[
 D_a:=I-2p/3\le J+Ad_T.
\]

The completed-square and lowest-eigenvalue monopole inequalities give,
exactly as verified in `round3_joint_gap.md`,

\[
 \frac{d_{\rm cal}}V\le436\delta^2
                            +432(1+\delta)^2d_T,
\qquad
 \frac\Delta V\le54\delta^2+54(1+\delta)^2d_T.
\tag{4}
\]

The positive part in `d_T` only weakens these upper bounds. All
inequalities concern the same selected actual class. No estimate for
the opposite Weyl half or the total Riemann tensor is used.

Consequently the intrinsic theorem's error and square factor obey

\[
 \varepsilon:=\delta^2+(\Delta+d_{\rm cal})/V
 \le491\delta^2+486(1+\delta)^2d_T
 \le491\delta^2+\frac{6075}{8}d_T
 \le760(\delta^2+d_T),
\tag{5}
\]

\[
 B_a:=\frac{(-a^2)_+}{V}
 \le\frac{(1+\delta)^2}{2\pi^2}C_A
 \le\frac{25C_A}{32\pi^2}.
\tag{6}
\]

Applying `(1+B_a) epsilon>=c` proves (2) for the small-delta range.
For `delta>1/64`, `delta^2>1/4096` supplies the other branch of (2).

The exact small-delta consequence, slightly stronger than the convenient
constant in (2), is

\[
 \left(1+\frac{(1+\delta)^2}{2\pi^2}C_A\right)
 \left(491\delta^2+486(1+\delta)^2d_T\right)\ge c.
\tag{7}
\]

For example one may replace `760` in (2) by
`486(65/64)^2=1026675/2048`, and replace `25/(32pi^2)` by
`4225/(8192pi^2)`, since the proof uses `delta<=1/64`.
These improvements do not change the existential nature of the
uncomputed intrinsic constant `c`.

## 3. A useful square condition involving T

In the small-delta range every such metric has `T>0`, without any
monopole input. Indeed

\[
 4\pi^2T=\int\left(s^2/24+2|W^+|^2
                                   -|\operatorname{Ric}^{\circ}|^2/2\right),
\]

and its integrand is bounded below by

\[
 \frac23(1-\delta)^2-2\delta^2>0.
\tag{8}
\]

Therefore the metricwise square condition

\[
 a^2\ge T-C_AA
\tag{9}
\]

also suffices for (2). It implies the required lower bound on `a^2`
whenever the small-delta argument is needed. In particular, a separately
established inequality `a^2>=T` supplies `C_A=0`.
This condition is not inferred merely from the words “monopole class.”
It must follow from the specific class construction or another stated
theorem.

## 4. Connected-sum families with actual full-sign monopoles

Consider

\[
 M=(\#_{j=1}^{m}X_j)\#N,\qquad m=2\ \hbox{or}\ 3,
 \qquad A=\sum_j A_j>0.
\]

Assume the actual full-sign monopole input in the manuscript's
Ishida--LeBrun setting: there are orthogonal classes `c_j` from the
positive summands, with `c_j^2=A_j>0`, and a diagonal integral basis
`E_ell` for the negative-definite intersection form of `N`, with square
`-1`, such that every class

\[
 a_{\boldsymbol\epsilon}
       =\sum_j\epsilon_jc_j+\sum_{\ell=1}^{b_-(N)}\epsilon_\ell E_\ell
\tag{10}
\]

is an actual monopole class on the specified smooth manifold. Also assume
`T(X_j)=A_j`, as holds for the complex-surface summands under discussion.
These are substantive hypotheses. This note does not assert them for
every collection of general-type surfaces or every negative-definite `N`.
Parity, orientation, and other requirements of the applicable actual
monopole theorem must still be satisfied. The input is stated explicitly
in the live manuscript's connected-sum section; this corollary does not
replace that input by numerical topology.

Let `b=b_-(N)` and `h=b_1(N)`. Since `b_+(N)=0`,

\[
 T(N)=4-4h-b,
\qquad D=4m-T(N)=4m-4+4h+b,
\qquad T(M)=A-D.
\tag{11}
\]

Every sign class in (10) has topological square

\[
 a_{\boldsymbol\epsilon}^2=A-b
       =T(M)+4m-4+4h\ge T(M).
\tag{12}
\]

Sign averaging of their positive projections gives

\[
 \operatorname{Av}_{\boldsymbol\epsilon}(a_{\boldsymbol\epsilon}^+)^2
 =\sum_j\|c_j^+\|_2^2+\sum_\ell\|E_\ell^+\|_2^2\ge A.
\tag{13}
\]

Thus a class with `p>=A` can be selected for each metric, and (12) gives
the square condition (9) with `C_A=0`. Equations (2) and (11) prove

\[
 \boxed{\quad
 \delta(g)^2+\left(\frac13-\frac DA\right)_+
 \ge c_{\rm IL}:=\min\{1/4096,c/760\}>0.
 \quad}
\tag{14}
\]

This applies throughout every family with the stated full-sign monopole
input, not just at the exact critical locus `D=A/3`. No upper bound on
`b_-(N)/A`, `b_1(N)/A`, or `chi(M)/A` is needed. If those quantities make
`T(M)<=0`, equation (8) already excludes all small-delta metrics.

The ratio in (14) is `D/A`, not generally `k/A`. For example, when
`N=#_k CPbar^2`, it is `D=k+4` for `m=2` and `D=k+8` for `m=3`.

If an alternative actual monopole construction uses a negative-factor
class `c_N` with `c_N^2=-L_N` rather than the diagonal signs in (10),
the corresponding square is `a^2=A-L_N=T+(D-L_N)`. The required
topological check is then

\[
 L_N-D\le C_AA,
\tag{15}
\]

in addition to actual class existence and a proof that the selected
positive projection is at least `A`. Without those two class-specific
checks, (14) cannot be transferred to the alternative construction.

## 5. Uniform forbidden bands and the scope of the result

For any family satisfying the metricwise selection hypotheses of (2),
put `gamma=c(C_A)/2` and `epsilon_*=sqrt(c(C_A)/2)`. If

\[
 T/A\le2/3+\gamma,
\]

then every metric on that manifold has `delta>=epsilon_*`.
For the connected sums, the condition is equivalently
`D/A>=1/3-gamma`, with the universal `C_A=0` constant.
Any negative Einstein metric would rescale to `delta=0` and is therefore
excluded. Nonnegative Einstein constants are excluded by the actual
monopole projection condition and the spinor maximum principle.

The conclusion is a uniform near-negative-Einstein and all-sign
exact-Einstein forbidden band for these explicit monopole families.
It is not a general Einstein-existence theorem and does not decide
unrestricted Yau26. Its added scope is that neither the intrinsic proof
nor these family applications require a relative Euler bound. The
necessary replacement is the controlled square of the selected actual
monopole class, automatic from (12) in the stated connected-sum class.

## Verification

The proof uses the intrinsic theorem and the independently checked
scalar, scalar--Weyl, and lowest-eigenvalue budgets in
`round3_rigidity_review.md`. A fresh exact symbolic check verified the
general `T` budget identities, the coefficients in (5)--(7), the
connected-sum topology in (11)--(12), and both shifted examples for `D`.
This is algebraic verification, not a replacement for the supplied
monopole existence theorem.
