# Step 71 — The human functional versus the trace-free instrument: the unit wall, attained positive gaps, and the α-reading of the zero-gap theory

Agent2, Execute. Inputs: Agent4 review (Step 70), Spirit #86, `Curvature_Realizability.tex` §§(intrinsic-calibration 10.3: lines 1520–1543; exact conformal comparison: lines 5765–5871; balanced family: 5887–5961), LeBrun–Nayatani–Nitta \cite{lebrunself} (Knowledge `dg-ga-9411001-Self-Dual-Manifolds-with-Positive-Ricci-Curvature…`, lines 37, 52, 94), Ishida–LeBrun \cite{ishida2003curvature} (Knowledge `Curvature-Connected-Sums-and-Seiberg-Witten-Theory…`, line 400). Script `workspace/scripts/step71_functional_split_examples.py` → `workspace/data/step71_functional_split_examples.json` (exit 0, every example consistent).

## 0. Notation fixed for the whole package

- The human functional is the corpus one:
  \[
  \mathscr D(g)=\mathcal E(g)=\inf_{\lambda\neq0}\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2V},\qquad \alpha(M)=\inf_g\mathcal E(g).
  \]
  With \(R=\int|\operatorname{Ric}|^2\), \(T_s=\int s\), \(P=\int|\operatorname{Ric}^\circ|^2\), \(L_s=\int(s-\bar s)^2\):
  \(\mathcal E=4-T_s^2/(RV)=(4P+L_s)/R\) for \(R>0\), and \(\mathcal E=4\) when \(T_s=0\) (in particular at Ricci-flat metrics).
- The instrument is \(P\). Write \(P_*(M)=\inf_gP\) (scale invariant, dimension of \(8\pi^2\)) and \(\mathfrak p_*=P_*/(8\pi^2)\). The symbol \(p_*\) is retired.
- \(T_\pm=2\chi\pm3\tau\) (Hitchin–Thorpe quantities); on \(X\#k\overline{\mathbb{CP}}^2\), \(T_+=A-k\).
- Conventions (LeBrun): \(8\pi^2\chi=\int(|W|^2+s^2/24-|\operatorname{Ric}^\circ|^2/2)\), \(12\pi^2\tau=\int(|W^+|^2-|W^-|^2)\).

## 1. The all-metric identity and the range of α

**Identity 71.1** (inherited: corpus eq. (intrinsic-calibration 10.5)). For every metric with \(R>0\), and for both orientations,
\[
\mathcal E(g)-1=\frac{12\int|W^\pm|^2+L_s-24\pi^2T_\pm}{R},\qquad
R=4P+24\pi^2T_\pm-12\!\int|W^\pm|^2 .
\]
Proof: \(R=P+\int s^2/4\) and Gauss–Bonnet/signature eliminate \(\int s^2\). Checked on round \(S^4\), Fubini–Study, \(S^1\times S^3\), \(S^1\times H^3/\Gamma\), \(\Sigma_g\times S^2\) with opposite curvatures, compact hyperbolic manifolds and Ricci-flat K3 (JSON).

**Consequences for the range.**
1. \(0\le\mathcal E<4\) unless \(T_s=0\), where \(\mathcal E=4\). Ricci-flat metrics, and all metrics of zero total scalar curvature, are the *maxima* of \(\mathcal E\).
2. Every closed \(M\) carries a metric with \(s<0\) (Aubin/Kazdan–Warner), so \(\alpha(M)<4\) always.
3. \(\alpha(M)=0\) attained \(\iff\) \(M\) carries an Einstein metric with \(\lambda\neq0\).

## 2. Theorem 71.B (the unit wall and its equality class)

Orient \(M\) so that \(T_+\le T_-\).

(a) [inherited, corpus line 1532] If \(T_+\le0\) then \(\mathcal E(g)\ge1\) for every metric, so \(\alpha(M)\ge1\).

(b) [new] If \(T_+<0\), then \(\mathcal E(g)\ge1+24\pi^2|T_+|/R>1\) for every metric. Hence if \(\alpha(M)=1\) it is not attained, and any approximating sequence has \(R\to\infty\) relative to \(\int|W^+|^2+L_s+24\pi^2|T_+|\).

(c) [new] If \(T_+=0\), then \(\mathcal E(g)=1\) if and only if \(W^+\equiv0\) and \(s\) is a nonzero constant. Consequently
\[
\alpha(M)=1\ \text{is attained}\iff M \text{ carries a } W^+\!=0 \text{ conformal class with nonzero Yamabe constant,}
\]
and the attaining metrics are exactly the constant-scalar-curvature metrics in such classes. (When \(T_+=T_-=0\), either half may vanish.)

*Proof of (c).* With \(T_+=0\), Identity 71.1 gives \(\mathcal E-1=(12\int|W^+|^2+L_s)/R\ge0\), with equality iff \(W^+=0\) and \(L_s=0\). Equality also needs \(R>0\). If \(s\) were constant and zero, then \(T_s=0\) and \(\mathcal E=4\). In a conformal class, constant-scalar-curvature metrics exist (Yamabe), and the sign of a constant scalar curvature equals the sign of \(Y\). \(W^+=0\) is conformally invariant. \(\square\)

(d) [new] **No attaining metric is Einstein.** Einstein metrics have \(\mathcal E\in\{0,4\}\).

(e) [new] **Positive-scalar equality class.** If \(\mathcal E(g)=1\) with \(s>0\), the Weitzenböck formula for self-dual harmonic forms with \(W^+=0\) gives \(b_+=0\). Then \(T_+=0\) reads \(b_-=4-4b_1\), so \((b_1,b_2)\in\{(0,4),(1,0)\}\).
- If \((b_1,b_2)=(0,4)\), the form is negative definite, hence diagonal by Donaldson. If \(M\) is simply connected, it is homeomorphic to \(\#4\overline{\mathbb{CP}}^2\) (Freedman).
- If \((b_1,b_2)=(1,0)\), then \(\chi=\tau=0\).

The negative-scalar equality class is not constrained by this argument.

## 3. Theorem 71.C (attained positive gaps without Einstein metrics)

1. **\(S^1\times S^3/\Gamma\) and \(S^1\times_\phi H^3/\Gamma\)** (mapping tori of isometries). These have \(\chi=\tau=0\). The locally product metrics are conformally flat with constant \(s=\pm6\) and give \(\mathcal E=1\) exactly (JSON). So \(\alpha=1\), attained. These manifolds carry no Einstein metric (Hitchin's equality case of Hitchin–Thorpe would force flatness, contradicting \(\pi_1\)).

2. **\(\#4\overline{\mathbb{CP}}^2\) (equivalently \(\#4\mathbb{CP}^2\) with reversed orientation).** Here \(\chi=6\), \(\tau=-4\), \(T_+=0\), \(T_-=24\). LeBrun's hyperbolic-ansatz self-dual conformal classes on \(n\mathbb{CP}^2\) exist for every \(n\) and each contains a positive-scalar representative (\cite{lebrunself}, line 37; also \cite{ishida2003curvature}, line 400: \(k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) carries ASD psc metrics). Their Yamabe representatives have \(\mathcal E=1\). Hence
   \[
   \alpha(\#4\overline{\mathbb{CP}}^{2})=1,
   \]
   attained, and the manifold carries no Einstein metric (Hitchin: Einstein with \(2\chi=3|\tau|\) is flat or K3-covered). LeBrun–Nayatani–Nitta's Theorem 1.3 shows that these attaining metrics cannot have nonnegative Ricci operator.

   A general formula follows (JSON). On \(k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\), a constant-scalar ASD metric with \(y=Y^2/(32\pi^2)\) and \(m=k+4\ell-4\) has
   \[
   \mathcal E=\frac{4(3m+y)}{3m+4y}=1+\frac{9m}{3m+4y}.
   \]
   It gives \(0\) at round \(S^4\) (\(m=-4,y=12\)) and at Fubini–Study \(\overline{\mathbb{CP}}^2\) (\(m=-3,y=9\)), and exactly \(1\) for \(m=0\), i.e. \((k,\ell)=(4,0)\) or \((0,1)\).
   - For \(m<0\) (Poon/LeBrun classes on \(2\overline{\mathbb{CP}}^2,3\overline{\mathbb{CP}}^2\)), the value is below 1.
   - For \(m>0\), it lies strictly between 1 and 4, increasing to 4 as \(m\to\infty\) at bounded \(y\le12\).

3. **Ricci-flat manifolds with a zero Hitchin–Thorpe quantity.** For a Ricci-flat metric, \(T_\pm=\int|W^\pm|^2/(2\pi^2)\). K3, \(T^4\), and their flat or Enriques-type quotients have \(T_+=0\), so \(\alpha\ge1\) *although an Einstein metric exists*. Under the human functional, a Ricci-flat Einstein metric is not a zero of the gap; it is its maximum. Attainment of \(\alpha=1\) there is equivalent to the existence of an ASD (for \(T^4\): half-flat) conformal class with \(Y\ne0\). For K3 this requires \(Y<0\) since K3 has no psc metric. For \(T^4\), conformally flat classes are believed flat, which would give \(Y=0\); that source is not yet retrieved. Both questions are open.

4. **\(S^2\times T^2\), Kodaira and \(\chi=0\) elliptic surfaces.** These have \(T_\pm=0\) and \(\alpha\ge1\). The product \(S^2\times T^2\) gives \(\mathcal E=2\), so \(\alpha\in[1,2]\). Attainment at 1 would need a half-flat class with \(Y\ne0\). A psc one is impossible since \(b_\pm=1\). The value is open.

**Reading.** The relation "positive gap ⇔ no Einstein metric" fails in both directions under \(\mathscr D=\mathcal E\):
- K3 and \(T^4\) have Einstein metrics and \(\alpha\ge1\);
- \(\#4\overline{\mathbb{CP}}^2\) and \(S^1\times S^3\) have no Einstein metric, and the infimum is attained.

The correct statement is: \(\alpha=0\) attained ⇔ nonzero-scale Einstein. The unit wall \(\alpha\ge1\) is a purely topological gap, \(T_{\min}\le0\). Its equality class is exactly constant-scalar half-conformally-flat geometry. This is the first family in the package where the gap, its attainment and its extremals are all determined.

## 3bis. Theorem 71.D (the long-circle reservoir: α ≤ 1 after any handle, and exact value 1)

**Statement.** Let \(N\) be any closed oriented four-manifold. Let \(Y\) be a spherical space form or a closed hyperbolic three-manifold, e.g. \(Y=S^3\). Then
\[
\alpha\bigl(N\#(S^1\times Y)\bigr)\le1 .
\]
Consequently, for every \(\ell\ge1\),
\[
\min T_\pm(N)\le4\ell\ \Longrightarrow\ \alpha\bigl(N\#\ell(S^1\times S^3)\bigr)=1,
\]
because \(T_\pm(N\#\ell(S^1\times S^3))=T_\pm(N)-4\ell\). The value is attained iff the resulting \(T_{\min}=0\) and the attainment criterion of 71.B(c) holds. The case \(N=S^4,\ell=1\) is attained; whenever \(T_{\min}<0\) it is not.

**Proof.** Take the product \(S^1_L\times Y\) with constant sectional curvature \(\pm1\) on \(Y\). It is conformally flat with constant \(s=\pm6\), and
\[
R=12L\,\mathrm{vol}(Y),\qquad \mathcal E=1 .
\]
Fix any metric \(h\) on \(N\). Form the connected sum inside a fixed small ball around a point of \(S^1_L\times Y\), gluing a rescaled copy \((N\setminus B,\varepsilon^2h)\) through a fixed neck. The glued region is independent of \(L\).

Each of the following is scale-invariant and bounded independently of \(L\): \(\int|\mathrm{Ric}|^2\), \(\int|W^\pm|^2\), and \(\int s^2\) over the glued region. On the product part \(s\equiv\pm6\) while \(\bar s=\pm6+O(1/L)\), so that part contributes \(O(1/L)\) to \(L_s\).

Hence the numerator \(12\int|W^+|^2+L_s-24\pi^2T_+\) of Identity 71.1 is \(O(1)\), while \(R=12L\,\mathrm{vol}(Y)-O(1)\). Therefore \(\mathcal E(g_L)=1+O(1/L)\to1\). The equality statement is Theorem 71.B(a). \(\square\)

**Readings.**
- On \(X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) with \(X\) minimal general type and \(\ell\ge1\), this gives \(\alpha\le\min\{1,4h/(1+h)\}\) with \(h=(k+4\ell)/A\). The long circle beats the corpus recovery bound \(4h/(1+h)\) (line 5562) for every \(h>1/3\).
- For \(k+4\ell\ge A\) the value is exactly \(\alpha=1\), not attained when \(k+4\ell>A\). For \(1/3<h<1\), Step 70's envelope bound gives \(\alpha\ge(3h-1)/(h+1)\); source comparison is pending.
- The mechanism is a *neutral Ricci reservoir*. The long \(S^1\times Y\) region carries no Euler or signature density and has \(W=0\) and constant scalar curvature, yet its Ricci energy grows linearly in \(L\). Ricci energy is the denominator of \(\mathcal E\), so any topological junk becomes negligible.
- The reservoir requires a four-dimensional neck (connected sum at a point). A long tube around a loop of a general \(M\) would need three-dimensional necks of size \(r\), costing \(\sim L/r\), which defeats it. This is why the theorem needs a handle-type summand \(S^1\times Y\). Whether \(\alpha=1\) on \(T_{\min}<0\) manifolds without such a summand, e.g. \(5\overline{\mathbb{CP}}^2\), is question (U2).

## 4. Lemma 71.T (translating P-statements into α-statements)

For every metric, \(\mathcal E(g)=(4P+L_s)/R\ge 4P/R\). At a constant-scalar Yamabe metric with \(Y\ne0\), \(\mathcal E(\widehat g)=16P(\widehat g)/(4P(\widehat g)+Y^2)\). This is the true \(\lambda\)-minimum; the value at \(\lambda=s/4\), \(16P/Y^2\), is only an upper bound. The Step-69 script now records both.

Consequences:
- A sequence with \(P\to0\) has \(\mathcal E\to0\) iff \((4P+L_s)/R\to0\). For Yamabe representatives this holds iff \(P/Y^2\to0\).
- A zero \(P\)-infimum on a manifold whose \(P\)-small metrics have \(Y\to0\) (Ricci-flat bulks) gives no \(\alpha\)-information.
- On LeBrun-supply manifolds \(Y^2\ge32\pi^2A\) for every class, so \(P\to0\) and \(\alpha\to0\) are equivalent there, and \(\alpha\) is the exact quotient \(\inf4p/(p+A+\upsilon)\).
- **Normalization at the Einstein scale.** If \(\mathcal E(g)\le1-\eta\) and \(\lambda_{\rm opt}=1\), then \(R=T_s=(4-\mathcal E)V\) and \(R\le24\pi^2T_+/\eta\).
- If moreover \(\mathcal E(g_j)\to0\), Gauss–Bonnet gives \(8\pi^2\chi=\int|W|^2+\tfrac23V+o(V)\). So \(V\le12\pi^2\chi(1+o(1))\), and a bounded-curvature totally collapsing sequence (\(V\to0\), \(|\mathrm{Rm}|\le\Lambda\)) is impossible because \(\chi>0\).

**Item-by-item reading of the zero-gap theory (supersedes the α-wording of 59.C, 59.N, 59.Z).**
- **59.C** is a \(P\)-statement: \(P_*\le36\,\mathrm{Vol}_{|r|}\le36\,\mathrm{MinVol}\). Since \(\mathrm{MinVol}=0\Rightarrow\chi=\tau=0\Rightarrow\alpha\ge1\), total collapse never produces an \(\alpha\)-zero. On \(S^1\times Y\), \(S^2\times T^2\) and Kodaira surfaces, \(P_*=0\) while \(\alpha\ge1\). For \(S^1\times S^3/\Gamma\) and \(S^1\times H^3/\Gamma\), \(\alpha=1\) is attained.
- **59.N** gives \(P_*(M)=0\) for Einstein orbifolds of every sign. It gives \(\alpha(M)=0\) only when the orbifold constant \(\lambda\neq0\). Then \(R\to4\lambda^2V_{\rm orb}>0\) and \(\alpha\le\lim(4P+L_s)/R=0\).
  - For Ricci-flat orbifolds (Kummer \(T^4/\pm1\to\) K3), \(P\to0\) but \(\alpha\ge1\).
  - \(\mathbb{CP}^2\#\mathbb{CP}^2\) from \(S^4/\pm1\) (\(\lambda=3\), \(T_+=14\), \(T_-=2\)) survives. On Ozuch's adapted metrics, \(\mathcal E\le(4P+L_s)/R=(8\pi^2a^4+L_s)/(48\pi^2)(1+o(1))\), which is \(a^4/6\) when \(L_s=o(a^4)\). The size of \(L_s\) on these metrics has not been computed.
- **59.D** (negative Einstein cusp-domain fillings and doubles) survives as an \(\alpha\)-statement. The bulk is negative Einstein, \(\chi>0\), and \(R\) stays bounded below.
- **59.Z** is a \(P\)-statement (Anderson's selection is for \(\mathcal R^2=32\pi^2\chi+4P\)). Its \(\alpha\)-version holds for \(\mathcal E\)-small sequences normalized at \(\lambda_{\rm opt}=1\): alternative (II), total collapse with bounded curvature, is excluded by Lemma 71.T. What remains are nonzero-scale Einstein orbifolds with bubbles and negative Einstein domains with cusp-type partial collapse. Attainment of \(\alpha=0\) ⇔ nonzero-scale Einstein metric. Whether Anderson's theorem applies directly to \(\mathcal E\)-minimizing sequences (rather than to \(P\)-selected ones) has not been checked; the statement above uses only Gauss–Bonnet.
- **61.EH** is a \(P\)-rate. Its \(\alpha\)-rate is \((4P+L_s)/R\) with \(R\to4\lambda^2V\), valid only for \(\lambda\ne0\).

## 5. Which results move α itself

- **Move α directly** (supply manifolds, Yamabe-negative):
  - the certified cell and the balanced law \(\alpha/h\le C_c/(1+C_ch/4)\);
  - \(\alpha(X\#k\overline{\mathbb{CP}}^2)<4k/(A+k)\);
  - the Burns second-order law, through the exact quotient;
  - the exceptional-flux ledger and the three-end equality structure, because \(\alpha\) and \(\mathfrak p_*\) vanish together and are comparable:
    \[
    \frac{\mathfrak p_*}{\mathfrak p_*+\tfrac34T_+}\le\alpha\le\frac{4\mathfrak p_*}{A+\mathfrak p_*}.
    \]
- **Move α through the Yamabe weight.** In the open range the exact quotient \(4p/(p+A+\upsilon)\) rewards Yamabe excess \(\upsilon\). This is a genuine second variable, and A01's construction question is: raise \(\upsilon\) at controlled \(p\).
- **P-rates only, unless λ≠0:** Ricci-flat orbifold resolutions, EH/ALE bubble rates, bounded-curvature collapse.
- **New α-results (this note):** the unit wall equality class and the attained positive gaps of Theorem 71.C.

## 6. Open questions created here

- (U1) \(\alpha(K3)\), \(\alpha(T^4)\), \(\alpha(S^2\times T^2)\): is the value 1, and is it attained (ASD classes with \(Y<0\))?
- (U2) For \(T_+<0\) manifolds without an \(S^1\times Y\) summand, is \(\alpha=1\)? Examples are \(k\overline{\mathbb{CP}}^2\) with \(k>4\), and the real-hyperbolic blow-ups \(X_k\) with \(k>2\chi\) of package §3.4. For the latter, Step 23 already found \(\inf\mathcal J=1\) by conformal inflation and \(\inf\mathcal E\in[1,4k/(k+6\chi)]\). Conformal inflation raises \(R\) but creates scalar variance; the long-circle reservoir of 71.D avoids the variance but needs a four-dimensional neck. The ASD formula shows \(\alpha=1\) would follow from ASD classes with \(|Y|\to\infty\).
- (U3) Is \(\sup_M\alpha(M)<4\)? The ASD formula approaches 4 as \(m\to\infty\), but other metrics may do better.
- (U4) The size of \(L_s\) on Ozuch's adapted EH metrics, which fixes the α-rate constant \(a^4/6\) on \(\mathbb{CP}^2\#\mathbb{CP}^2\).


## 7. Late Step-71 strengthening (derived after the verifier was submitted; not yet verified): Theorem 71.D′, the universal bound α ≤ 1

The neutral reservoir needs no \(S^1\) topology. Take the round "dumbbell" \(S^4_L\): two round hemispheres of radius 1 joined by a cylinder \([0,L]\times S^3(1)\). The hemisphere boundaries are totally geodesic and match the cylinder slices to \(C^1\), and they can be smoothed with \(L\)-independent cost. Then form \(M\#S^4_L\cong M\), gluing a fixed metric on \(M\) to one cap through a fixed neck.

Locally the cylinder is \(\mathbb R\times S^3\), with \(\operatorname{Ric}=(0,2,2,2)\), \(W=0\), \(s=6\), and per unit volume \(|\operatorname{Ric}^\circ|^2=3\), \(|\operatorname{Ric}|^2=12\). Its volume is \(2\pi^2L\). Hence
\[
P=6\pi^2L+O(1),\qquad R=24\pi^2L+O(1),\qquad \bar s=6+O(1/L),\qquad L_s=O(1),
\]
with every \(O(1)\) independent of \(L\): the caps, the neck and \(M\) are fixed. Therefore \(\mathcal E(g_L)=(4P+L_s)/R\to1\).

**Theorem 71.D′.** For every closed oriented four-manifold, \(0\le\alpha(M)\le1\). With 71.B(a):
\[
2\chi(M)\le3|\tau(M)|\ \Longrightarrow\ \alpha(M)=1 .
\]
This covers K3, \(T^4\), every \(\chi\le0\) manifold, \(k\overline{\mathbb{CP}}^2\) for \(k\ge4\), \(X\#k\overline{\mathbb{CP}}^2\) for \(k\ge A\) when \(\tau\le0\), and the real-hyperbolic blow-ups \(X_k\) with \(k\ge2\chi\). In particular it settles the value left undetermined in package §3.4 for \(k>2\chi\). Attainment is governed by 71.B(b,c). Questions (U1) (values), (U2) and (U3) are thereby answered: \(\sup_M\alpha(M)=1\), attained.

Consequences:
- The problem reduces to the strict Hitchin–Thorpe region \(T_\pm>0\). The interesting question becomes which of those manifolds have \(\alpha<1\), and by how much.
- On \(X\#k\overline{\mathbb{CP}}^2\): \(\alpha\le\min\{1,4k/(A+k)\}\), with \(\alpha=1\) for \(k\ge A\) and \(\alpha\in[(3h-1)/(h+1),1]\) for \(A/3<k<A\). The lower bound in that range rests on the Step-70 envelope; its source comparison is pending.
- Theorem 71.D (handle summands) is the special case \(S^1\times Y\) of this mechanism.
- Precedence: the corpus records only \(\inf\mathcal J=1\) by conformal inflation (step23 note line 202), where scalar variance blocks the \(\mathcal E\)-version. The dumbbell avoids that variance. No source stating \(\alpha\le1\) for all \(M\) was found in the corpus grep; an external literature search is still needed.
- This argument must be checked by an independent verifier before it is promoted into theorem_package_v1.md.


## 8. Binding verification and Step-72 supersession

The independent verifier is `trace/ttcs/results/step71_ttcs01_verifier1_integration.md`. Its corrections are binding over §§1–7:

1. Identity 71.1, the unit-wall equality class, the attained value on \(\#4\overline{\mathbb{CP}}^2\), and the long-circle reservoir are verified. At \(R=0\) the quotient identities are not evaluated; \(\mathcal E=4\) follows directly from the definition.
2. In the ASD constant-scalar formula set \(y=s^2V/(32\pi^2)\). It equals \(Y([g])^2/(32\pi^2)\) only when the metric is a Yamabe minimizer.
3. The long-circle conclusion on general-type handle families is one-way: \(k+4\ell\ge A\Rightarrow\alpha=1\). The converse was not proved here.
4. Normalization of an \(\mathcal E\)-small sequence is \(\lambda_{\rm opt}=\pm1\), according to the sign of total scalar curvature. The exact normalized identity is
   \[
   48\pi^2\chi=6\int|W|^2+L_s+(4-\mathcal E)(1-\mathcal E)V.
   \]
5. The collapse statement is limited to globally bounded-curvature, bubble-free total collapse of the same normalized \(\mathcal E\)-small sequence. Anderson's P-selected trichotomy has not been transferred to arbitrary \(\mathcal E\)-minimizers; shrinking concentration balls remain possible.
6. The EH coefficient \(a^4/6\) is conditional on \(L_s=o(a^4)\). Without the scalar profile, only the formula \(\mathcal E=(4P+L_s)/R\) and the P-rate are established.
7. §7's universal dumbbell is independently developed and promoted in `step72_orientation_free_weyl_deficit_law.md`. It proves \(\alpha\le1\) universally and supersedes questions U1–U3 at the level of values. The orientation-free Weyl-deficit law in that note is now the primary global formulation of the human functional.
