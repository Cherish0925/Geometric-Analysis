# The positive branch and an all-sign integral consequence

## 1. Why add this corollary

The new integral theorem concerns negative Einstein normalization. The
Yau26 working statement leaves the output Einstein sign unrestricted.
For the same monopole families, the positive input branch has an elementary
integral obstruction from the classical scalar monopole inequality and
Chern--Weil. Combining it with the negative result makes the scope of the
family exclusion precise; it does not add a second independent main
discovery.

Use the notation and actual monopole hypothesis of
[the integral rigidity theorem](round4_rigidity.md). In particular
T=2chi+3tau, p=(a+)^2>=A>0, and d=(T/A-2/3)_+.
Set

    r_+(g)=Vol(g)^(-1) integral |Ric_g-g|_g^2.

**Proposition.** Without a sign or pointwise curvature assumption,

    r_+(g)+d > 1/4.                                      (1.1)

The constant is convenient, not asserted optimal. This deduction uses
only the scalar monopole bound and Chern--Weil, not the new spinor
Hessian argument.

## 2. Proof

Let V=Vol(g), r=r_+(g), e=s-4, and P=integral |Ric^circ|^2.
The orthogonal Ricci decomposition gives

    integral e^2 <=4rV,   P<=rV.

On the scalar-negative set, s_-^2<=e^2. The scalar monopole estimate
therefore implies

    32pi^2 A <= integral s_-^2 <=4rV,
    A/V <=r/(8pi^2).                                     (2.1)

If r<=1/4, the reverse triangle inequality in L2 and Chern--Weil give

    4pi^2 T/V
      =V^(-1) integral(s^2/24+2|W+|^2-|Ric^circ|^2/2)
      >=(4-2sqrt(r))^2/24-r/2
      >=1/4.                                            (2.2)

The last inequality follows, with x=sqrt(r)<=1/2, from

    (4-2x)^2/24-x^2/2-1/4
      =(1/2-x)(4x+10)/12 >=0.

On the other hand T<=A(2/3+d). If also d<=1/4, (2.1) gives

    4pi^2 T/V <=(r/2)(2/3+d) <=11/96 <1/4,              (2.3)

contradicting (2.2). Hence r and d cannot both be at most 1/4;
in particular r+d>1/4. QED.

## 3. Scale-free formulation and combination with the negative theorem

For sigma=+1 or -1, define

    R_sigma(g)=inf_(lambda>0)
      integral |Ric_g-sigma lambda g|_g^2/(lambda^2 V_g).

Constant rescaling preserves the harmonic projection of a two-form in
dimension four, so (1.1) implies R_+(g)+d>=1/4. The weak inequality
accounts for taking an infimum. If the selected actual class also obeys
a^2>=-C_A A (or the alternative square condition in the integral
theorem), that theorem gives R_-(g)+d>=c(C_A)>0. Consequently

    min{R_+(g),R_-(g)}+d >=min{1/4,c(C_A)}.                (3.1)

For a metricwise class selection this applies separately to every metric.
No sign information for a hypothetical output Einstein metric is used.

For example, for X minimal general type with b+(X)>1 and A=c1(X)^2>0,
on M=X#k CPbar^2 the verified sign classes have a^2=T=A-k.
The alternative square condition applies with C_A=0. Thus

    inf_(lambda nonzero)
      integral |Ric_g-lambda g|_g^2/(lambda^2 V_g)
        +(1/3-k/A)_+ >=c_* >0                            (3.2)

uniformly in X,k,g. The positive and negative sides in (3.2) have
different proofs; the new analytic content is the negative side.

If R2=integral |Ric|^2 is positive and S=integral s, optimizing the
real parameter gives the transparent formula

    inf_(lambda nonzero)
      integral |Ric-lambda g|^2/(lambda^2 V)
      =4-S^2/(V R2)
      =[4 integral |Ric^circ|^2+integral(s-S/V)^2]/R2.     (3.3)

For S=0 this is the infimum four, approached as |lambda| grows.
R2=0 is impossible here, since the actual monopole with p>=A>0 forces
integral s_-^2>=32pi^2 A. For S nonzero the minimizing signed constant
is lambda=R2/S. This is an energy fraction, not a pointwise curvature
estimate.

In a sufficiently narrow band around k/A=1/3, these topologies cannot
support either sign of arbitrarily tight Ricci input, even in this
weaker integral sense. They are therefore excluded as counterexample
topologies in that band. Outside the specified monopole families and
band, this argument supplies no universal Yau26 theorem.
