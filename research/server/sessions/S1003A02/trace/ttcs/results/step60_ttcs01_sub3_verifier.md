# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md",
    "Knowledge/objects/papers/Canonical-Metrics-on-3-Manifolds-and-4-Manifolds--8d02c53d4380--0b5d0f7e0ac4/object.md",
    "Sessions/S1003A02/workspace/notes/step58_consolidated_hypothesis_ledger.md"
  ]
}
```

## Task

Verify Part B of the Step-59 note (zero-gap structure) with Part C.4. Check: (1) Prop 59.N: the O(lambda^2) estimate for gluing Ricci-flat ALE trees into Einstein orbifolds of any sign (decay rates, curvature on the annulus, tree induction, orientation compatibility). (2) Prop 59.C: alpha <= 36 Vol_{|r|} with LeBrun's normalization, and the claims that MinVol=0 forces chi=tau=0 and that alpha is never attained on S^1xY (Y hyperbolic/spherical), S^2xT^2, Kodaira surfaces. (3) Prop 59.D: the explicit warped-product interpolations: the real-hyperbolic double (curvatures -(f'^2-f''), -f'^2, volume O(e^{-3T})), the complex-hyperbolic Heisenberg-cusp double (is curvature really bounded when base scales e^{-f} and fibre e^{-2f}, including the mixed terms with f', f''?), and the T^3-cusp Dehn filling for every slope (flattening path of flat metrics on T^3 at scale e^{-T}, turnaround, exponential growth of the gamma-circle while the T^2 stays at size e^{-T}, round cap; volume O(e^{-2T})). Also whether the fillings and doubles are smooth closed manifolds with the claimed topology, and whether 'no Einstein warped T^3 x I neck' supports the stated openness for doubles. (4) Theorem 59.Z: whether Anderson's Theorem 4.10 (read the Knowledge object provided; note his case labels and hypotheses) plus lower semicontinuity of P on compact subsets of the regular set really yields the trichotomy (I) Einstein orbifold, (III) finite-volume complete Einstein domain with s<0 and F-structure complement, (II) total collapse, as stated; whether the minimizers of Z_eps = P + eps int (1+|Ric|^2)^p have P -> alpha; the arguments excluding Ricci-flat and positive Omega in (III); what extra hypotheses are silently used (e.g. local minimality, convergence class); and whether 'attainment iff Einstein' is correctly scoped. Return a direct scientific memo with corrected statements.

## Output

# Scientific verification memo: Step 59, Part B and C.4

## 1. Proposition 59.N: Einstein orbifold plus Ricci-flat ALE trees

The gluing argument gives \(\alpha(M)=0\). The stated \(O(\lambda ^2)\) rate is valid when the ALE decay order is at least two; the displayed curvature formula in the note uses the stronger order-four asymptotics.

Write, in orbifold normal coordinates near a cone point,
\[
g_V=\delta+h,\qquad |\partial^j h|\le C r^{2-j}.
\]
If an ALE metric has derivative-controlled order \(\tau>0\),
\[
g_N=\delta+q,\qquad |\partial^j q(y)|\le C|y|^{-\tau-j},
\]
then after scaling by \(\lambda^2\) and using \(x=\lambda y\),
\[
|\partial^j q_\lambda(x)|\le C\lambda^\tau r^{-\tau-j}.
\]
On a cutoff annulus \(r\asymp t\), the interpolated metric therefore satisfies
\[
|{\rm Rm}|\le C\bigl(1+\lambda^\tau t^{-\tau-2}\bigr),
\]
and its volume is \(O(t^4)\). Hence
\[
P_{\rm ann}
 \le C t^4\bigl(1+\lambda^\tau t^{-\tau-2}\bigr)^2. \tag{1}
\]

For \(\tau\ge2\), choosing \(t=\sqrt{\lambda}\) gives
\[
\lambda^\tau t^{-\tau-2}
 =\lambda^{(\tau-2)/2}\le C,
\qquad
P_{\rm ann}=O(\lambda^2).
\]
For order four, this becomes exactly the estimate written in Step 59,
\[
|{\rm Rm}|\le C(1+\lambda^4t^{-6}).
\]
If only some order \(\tau>0\) is recorded, choosing
\[
t=\lambda^{\tau/(\tau+2)}
\]
keeps the annular curvature bounded and yields
\[
P_{\rm ann}=O\!\left(\lambda^{4\tau/(\tau+2)}\right)\longrightarrow0.
\]
Thus the conclusion \(\alpha(M)=0\) needs only positive derivative-controlled ALE order. The particular \(O(\lambda^2)\) rate needs \(\tau\ge2\). The general Bando–Kasue–Nakajima input should be cited in the decay form actually used; order four is certainly available for the standard Kronheimer examples, but it is unnecessary here.

Outside the annuli, \({\rm Ric}^{\circ}=0\) exactly on both pieces: \(g_V\) is Einstein and \(g_N\) is Ricci-flat. The change in Einstein constant across the construction causes no bulk contribution to \(P\); only the cutoff annulus matters.

For a finite ALE orbifold tree, the same estimate applies at every node after normalizing to the parent scale. Since \(P\) is scale invariant, a fixed relative gluing parameter \(\lambda\) at every edge gives a finite sum of \(O(\lambda^2)\) terms when all pieces have order at least two. More generally, nested relative parameters give a diagonal sequence with total energy tending to zero. The terminal pieces must be smooth so that the resulting \(M\) is a smooth closed manifold.

“Compatible orientation” should mean:

1. the asymptotic group of each ALE end is conjugate to the local orbifold group;
2. the link identification reverses the induced hypersurface orientations, as required for oriented gluing;
3. at an orientation mismatch one may use the same Ricci-flat metric on the oppositely oriented ALE space.

The metric argument itself is independent of orientation. Proposition 59.N directly treats irreducible cone points with one-ended ALE replacements. A reducible orbifold vertex would require a matched multi-ended replacement and is not automatically included.

---

## 2. Proposition 59.C: Ricci minimal volume and nonattainment examples

With LeBrun’s normalization, \(|r|\le3\) means that every eigenvalue \(\rho_i\) of the Ricci endomorphism satisfies \(|\rho_i|\le3\). Therefore
\[
|{\rm Ric}^{\circ}|^2
 =\sum_{i=1}^4(\rho_i-\bar\rho)^2
 =\sum_i\rho_i^2-\frac{s^2}{4}
 \le \sum_i\rho_i^2
 \le36.
\]
For any sequence approaching \({\rm Vol}_{|r|}(M)\),
\[
P(g)\le36\,{\rm Vol}(g),
\]
so
\[
\boxed{\alpha(M)\le36\,{\rm Vol}_{|r|}(M)}.
\]
The constant \(36\) is the correct algebraic constant for the spectral Ricci normalization; equality in the pointwise estimate is possible for eigenvalues \(3,3,-3,-3\).

If \(|K|\le1\), each Ricci eigenvalue is a sum of three sectional curvatures and hence has absolute value at most \(3\). Consequently
\[
{\rm Vol}_{|r|}(M)\le {\rm MinVol}(M),
\]
and therefore
\[
\boxed{\alpha(M)\le36\,{\rm Vol}_{|r|}(M)
       \le36\,{\rm MinVol}(M)}.
\]

If \({\rm MinVol}(M)=0\), take metrics with \(|K|\le1\) and volume tending to zero. Their full curvature is uniformly bounded, while the Euler and signature densities are quadratic in curvature. Chern–Weil then gives
\[
|\chi(M)|+|\tau(M)|\le C\,{\rm Vol}(M,g_i)\longrightarrow0,
\]
so
\[
\chi(M)=\tau(M)=0.
\]

For any closed four-manifold with \(\chi=0\), an Einstein metric would satisfy
\[
8\pi^2\chi
 =\int_M\left(|W|^2+\frac{s^2}{24}\right)d\mu,
\]
and hence \(W=0=s\). Thus every Einstein metric on such a manifold is flat.

The listed examples have \({\rm MinVol}=0\) and admit no flat metric:

- \(S^1\times Y^3\), with \(Y\) closed hyperbolic: its fundamental group is not virtually abelian, whereas a closed flat manifold has a Bieberbach group.
- \(S^1\times Y^3\), with \(Y\) spherical: its fundamental group is virtually \(\mathbb Z\), not virtually \(\mathbb Z^4\).
- \(S^2\times T^2\): it has \(\pi_2\ne0\), while closed flat manifolds are aspherical.
- Primary and secondary Kodaira surfaces: their fundamental groups contain a finite-index nilpotent group which is not virtually abelian, so they are not Bieberbach manifolds.

It follows that these examples have \(\alpha=0\), but no smooth metric realizes the infimum. The general identity behind this is
\[
P(g)=0\quad\Longleftrightarrow\quad {\rm Ric}^{\circ}_g=0
\quad\Longleftrightarrow\quad g\ \text{is Einstein}.
\]

---

## 3. Proposition 59.D: doubles and torus Dehn fillings

### 3.1 Real-hyperbolic double

Let
\[
g=dt^2+e^{-2t}g_N
\]
on a flat cusp. Put \(a=e^{-f}\) on the interpolating collar. The warped-product curvature formulas are
\[
K(\partial_t,X)=-\frac{a''}{a}
 =-\bigl((f')^2-f''\bigr),
\qquad
K(X,Y)=-\left(\frac{a'}a\right)^2=-(f')^2.
\]
A smooth reflected function satisfying
\[
f(t)=t\quad\text{near the first end},\qquad
f(t)=2T+2-t\quad\text{near the second end},
\]
with \(|f'|+|f''|\le C\), therefore gives uniformly bounded curvature. Since \(f\ge T-O(1)\),
\[
{\rm Vol}(\text{neck})
 ={\rm Vol}(N)\int e^{-3f(t)}dt
 =O(e^{-3T}).
\]
The two hyperbolic pieces have \({\rm Ric}^{\circ}=0\), while \(|{\rm Ric}^{\circ}|\le C\) on the neck. Hence
\[
P=O(e^{-3T})\longrightarrow0.
\]

Using all cusp sections, the oriented double
\[
H_T\cup \overline{H_T}
\]
is a smooth closed manifold, independent of \(T\) up to diffeomorphism.

### 3.2 Complex-hyperbolic cusp

Use Heisenberg one-forms \(\eta_1,\eta_2,\theta\), with
\[
d\theta=c_0\,\eta_1\wedge\eta_2.
\]
The interpolating metric has the form
\[
dt^2+a(t)^2(\eta_1^2+\eta_2^2)+c(t)^2\theta^2,
\qquad
a=e^{-f},\quad c=e^{-2f}=a^2.
\]
In an orthonormal coframe, the intrinsic Heisenberg structure coefficient is
\[
\frac{c}{a^2}=1.
\]
The remaining curvature terms are polynomials in
\[
\frac{a'}a=-f',\qquad
\frac{c'}c=-2f',\qquad
\frac{a''}a=(f')^2-f'',\qquad
\frac{c''}c=4(f')^2-2f'',
\]
together with the constant \(c/a^2\). This includes the radial, horizontal–vertical, and Codazzi terms. Thus \(|f'|+|f''|\le C\) gives a uniform full-curvature bound, not merely an intrinsic Nil-curvature bound.

The orbit volume density is
\[
a^2c=e^{-4f},
\]
so
\[
{\rm Vol}(\text{neck})=O(e^{-4T}),
\qquad
P=O(e^{-4T}).
\]
The canonical horizontal/contact splitting of a complex-hyperbolic cusp descends to its compact Heisenberg or infranil quotient, so the construction is globally defined there.

### 3.3 Filling a \(T^3\) cusp along an arbitrary primitive slope

A primitive \(\gamma\in H_1(T^3;\mathbb Z)\) extends to an integral basis. Hence
\[
T^3\cong S^1_\gamma\times T^2
\]
topologically, and attaching \(D^2\times T^2\) with \(\gamma\) as meridian gives a smooth filling. Primitivity is exactly what prevents an orbifold core.

The original cusp flat metric need not be orthogonally split in this basis. This is repaired by a fixed path \(G(u)\) of flat metrics from the cusp metric to a product metric adapted to \(\gamma\). For
\[
du^2+e^{-2T}G(u),
\]
the second fundamental form is
\[
L=\frac12G^{-1}G',
\]
independent of the overall factor \(e^{-2T}\). A fixed smooth path with bounded \(G,G^{-1},G',G''\) therefore has uniformly bounded curvature and volume \(O(e^{-3T})\). Constants may depend on \(\gamma\), which is sufficient for each fixed filling.

After this collar, use
\[
du^2+a(u)^2d\theta^2+e^{-2T}g_{T^2}.
\]
The relevant sectional curvature is
\[
K(\partial_u,\partial_\theta)=-a''/a.
\]
Writing \(a=e^q\), this is controlled by \(q''+(q')^2\). Thus \(q'\) can be changed smoothly from \(-1\) to \(+1\) over a fixed interval while \(a\asymp e^{-T}\), with bounded curvature. On the long growth region take
\[
a(u)=e^{-T+u},\qquad 0\le u\le T+O(1),
\]
which is a hyperbolic two-dimensional piece times a flat \(T^2\) of size \(e^{-T}\). Its volume is
\[
e^{-2T}\int_0^{T+O(1)} e^{-T+u}\,du
 =O(e^{-2T}).
\]
A final disk cap of size \(O(1)\), with
\[
a(\rho)=\rho+O(\rho^3)
\]
at its center, is smooth and contributes \(O(e^{-2T})\) volume. Therefore the whole filling region has uniformly bounded curvature and
\[
P=O(e^{-2T})\longrightarrow0.
\]

For a closed filled manifold, every cusp component must be filled or otherwise paired in a double. The one-cusp formulation is correct as written; with several cusps, the construction is performed on all of them.

### 3.4 Relation to Part C.4

Using the Anderson–Bamler Einstein filling result recorded in C.4, sufficiently long primitive slopes carry Einstein metrics. Since a fixed cusp lattice has only finitely many primitive vectors below a fixed length, all but finitely many slopes are covered. Thus:

- every primitive filling has \(\alpha=0\) by the explicit interpolation;
- sufficiently long fillings realize \(\alpha=0\) by an Einstein metric;
- for the remaining finite set, the supplied material gives \(\alpha=0\) but does not determine Einstein existence.

For a fixed long slope \(M_\gamma\), the constant sequence at its Einstein metric is a compact case-(I) sequence, while the explicit \(T\to\infty\) metrics on the same \(M_\gamma\) form another minimizing sequence with a cusped limit. Varying \(\gamma\) through longer slopes produces Einstein manifolds approaching the cusp across generally varying diffeomorphism types; it is not one Anderson sequence on a fixed manifold.

For an isotropic torus neck
\[
g=dt^2+\phi(t)^2g_{\rm flat},
\]
the Einstein equations give
\[
-3\frac{\phi''}{\phi}
 =
-\frac{\phi''}{\phi}
 -2\left(\frac{\phi'}{\phi}\right)^2,
\]
hence
\[
\phi\phi''=(\phi')^2,\qquad (\log\phi)''=0,
\qquad \phi=Ce^{ct}.
\]
Such a neck cannot turn around unless \(c=0\), in which case it is flat and cannot match a hyperbolic cusp derivative. This excludes only the isotropic warped ansatz. It does not exclude anisotropic torus-invariant Einstein metrics or arbitrary Einstein metrics on \(D(H)\). The Anderson–Bamler filling theorems concern solid-torus fillings and do not address doubles. The supplied sources contain neither an Einstein construction nor a topological obstruction for \(D(H)\), so the literature-status sentence about doubles requires separate source support.

---

## 4. Theorem 59.Z and Anderson’s Theorem 4.10

### 4.1 Perturbed minimizers do approach \(\alpha\)

Let
\[
Q_p(g)=\int_M(1+|{\rm Ric}|^2)^p\,d\mu,
\qquad
m_\varepsilon=\inf_{\operatorname{Vol}=1}\bigl(P+\varepsilon Q_p\bigr).
\]
Since \(P\ge\alpha\),
\[
m_\varepsilon\ge\alpha.
\]
For every \(\delta>0\), choose \(h_\delta\) with
\[
P(h_\delta)\le\alpha+\delta.
\]
Then
\[
m_\varepsilon
 \le \alpha+\delta+\varepsilon Q_p(h_\delta),
\]
so \(m_\varepsilon\to\alpha\). For exact smooth minimizers,
\[
\alpha\le P(g_\varepsilon)\le m_\varepsilon,
\]
and therefore \(P(g_\varepsilon)\to\alpha\). Anderson’s construction may first produce minimizing pairs on orbifold domains rather than global smooth minimizers; the same conclusion holds for the smooth approximating sequence used in Theorem 4.10.

Under the Step-59 convention
\[
\mathcal R^2=32\pi^2\chi+4P,
\]
minimizing \(\mathcal R^2\) is equivalent to minimizing \(P\).

### 4.2 Einstein character of the regular limit

On every compact \(K\) in the regular locus, Anderson’s selected sequence converges smoothly after pullback. Hence, when \(\alpha=0\),
\[
\int_K|{\rm Ric}^{\circ}_{g_0}|^2d\mu_{g_0}
 =
\lim_i\int_{\Phi_i(K)}
 |{\rm Ric}^{\circ}_{g_i}|^2d\mu_{g_i}
 \le\lim_i P(g_i)=0.
\]
Thus
\[
{\rm Ric}^{\circ}_{g_0}=0
\]
on the regular locus. The contracted Bianchi identity makes \(s\) constant on each connected component.

Anderson’s theorem itself states only \(C^0\) extension across the orbifold points. Calling the result a smooth Einstein orbifold also uses the standard Einstein removable-singularity theorem on each local orbifold branch. Without that regularity input, the precise statement is “\(C^0\) orbifold metric, smooth and Einstein on its regular locus.”

### 4.3 Completeness and scalar sign

Theorem 4.10 does not initially state completeness of a proper maximal domain; Remark 4.12 explains that a uniform Ricci lower bound gives completeness. Here each connected component is Einstein,
\[
{\rm Ric}=\frac{s}{4}g,
\]
so it has such a lower bound. Maximality of the thick domain together with Bishop–Gromov comparison rules out finite-distance collapse. Thus each connected component is complete.

Every complete noncompact component has \(s<0\):

- if \(s>0\), the orbifold form of Myers’ theorem makes the component compact;
- if \(s=0\), it is Ricci-flat, and a complete noncompact Ricci-flat space has infinite volume, contrary to Anderson’s finite total volume.

This argument applies componentwise to noncompact components. Anderson’s stated theorem does not explicitly exclude compact components inside a reducible proper-domain configuration. Therefore the unconditional formulation is:

\[
\boxed{\text{every complete noncompact connected component of }\Omega
       \text{ has }s<0.}
\]

The stronger sentence “\(s<0\) on all of \(\Omega\)” additionally needs a proof that every component in the proper-domain case is noncompact.

### 4.4 Correct trichotomy and labels

Anderson’s Theorem 4.10 uses:

- case (I): compact orbifold;
- case (II): maximal orbifold domain, with \(\Omega=\varnothing\) allowed.

The three labels in Step 59 come from Anderson’s introductory Theorem 1.1, which separates the second item into a nonempty domain and total collapse.

A precise consequence for \(\alpha(M)=0\) is therefore:

1. **Compact configuration.** A compact, possibly reducible orbifold \(V\), associated to \(M\), with volume \(1\), whose regular metric is Einstein. Smooth Einstein-orbifold regularity at the cone points uses removable singularities.

2. **Nonempty-domain configuration.** A nonempty maximal orbifold domain \(\Omega\), of total volume in \((0,1]\), Einstein and complete componentwise. Every noncompact component has \(s<0\). Outside large compact subsets, the selected sequence collapses along \(F\)-structures with locally bounded curvature away from finitely many shrinking balls.

3. **Total-collapse configuration.** \(\Omega=\varnothing\); the selected sequence collapses everywhere along \(F\)-structures with locally bounded curvature away from finitely many shrinking balls.

This is an existence statement for an Anderson regularized minimizing sequence. It does not describe every arbitrary sequence with \(P(g_i)\to0\). Local minimality and the fourth-order Euler–Lagrange equations are used inside Anderson’s compactness and regularity theory, but are not separately needed once smooth regular-locus convergence and \(P(g_i)\to0\) are available.

The constructions in Propositions 59.N, 59.C, and 59.D provide sufficient families realizing the three geometric patterns. They do not form a reverse classification of all possible compact, partial-collapse, or total-collapse configurations.

Finally, when “attained” means attained by a smooth Riemannian metric on \(M\),
\[
\boxed{\alpha(M)=0\text{ is attained }
\Longleftrightarrow M\text{ carries an Einstein metric}.}
\]
This equivalence follows directly from \(P\ge0\) and \(P(g)=0\iff{\rm Ric}^{\circ}_g=0\); it does not depend on Anderson’s decomposition.