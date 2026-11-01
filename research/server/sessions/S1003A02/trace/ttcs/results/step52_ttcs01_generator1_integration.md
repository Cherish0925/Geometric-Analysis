# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 52,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step52_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step52_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

The entry programme for minimizing sequences of P(g)=∫|Ric°|² on closed four-manifolds now hinges on Lemma 52.KS in the attached note: an own-scale concentration lemma for the energy-radius-weighted (frozen-weight) gradient flow of P — lifespan ≥ c1 in own-scale time, two-sided comparability of the energy radius, Sobolev persistence — the analogue of Kuwert–Schätzle's lemma for Willmore flow. P is in Bour's strongly parabolic class (a=b=0) but its gradient dissipates only the Ricci part; the Weyl energy must be controlled through the Pfaffian transgression and the Bianchi system δW ~ ∇Ric. Produce the strongest concrete proof architecture you can: the localized energy identity with cutoffs (exact form of d/dt ∫φ|Rm|² or of a better localized quantity), interpolation inequalities replacing Kuwert–Schätzle's, where the Sobolev constant enters, and how the weight's own-scale derivatives enter. If you believe the lemma is false, give a precise counter-mechanism (e.g. Weyl-energy transfer through necks at zero Ricci dissipation) and the weakest replacement that still yields a Palais–Smale minimizing sequence in the sense (PS_ε). Also propose an alternative selection mechanism (not a sixth-order regularization) if you see one that avoids flow lifetime altogether.

## Integrated Scientific Memo

## Conclusion

Lemma 52.KS is **false as stated** for the hard-threshold radius
\[
r_\varepsilon(x)=\sup\Bigl\{r\le r_0:\int_{B(x,r)}|\Rm|^2\le\varepsilon\Bigr\}.
\]
The obstruction is simpler than a hypothetical Weyl-transfer neck: a localized noncritical curvature packet with total energy just above \(\varepsilon\) can dissipate an arbitrarily small amount, fall below the threshold, and make \(r_\varepsilon\) jump from the packet scale to \(r_0\). Thus no universal upper comparison
\[
r_\varepsilon(g(t),x)\le 2r_\varepsilon(g(0),x)
\]
can hold for arbitrary smooth data. The lower-persistence, localized smoothing, and dissipation architecture remains plausible, but the selection argument must use either an output-compatible integrated time, a threshold-averaged adaptive radius, or a static variational selection.

A normalization error in Branch 2 must also be removed. In the norm convention used in Step 52 and Branch 1,
\[
|\Rm|_{\rm ten}^2=R_{ijkl}R^{ijkl},
\]
one has
\[
\int_M|\Rm|_{\rm ten}^2\,d\mu
=4P(g)+32\pi^2\chi(M),
\]
not \(8\pi^2\chi+\frac52P\). The latter belongs to an incompatible curvature normalization/decomposition. All coefficients below use the full tensor norm.

---

# 1. Exact localized identity: the Weyl part is not the main obstruction

Let
\[
E=\Ric^\circ,\qquad P(g)=\int |E|^2\,d\mu,\qquad Q=\grad_{L^2}P,
\]
and consider the geometric fixed-weight flow
\[
\partial_tg=h=-wQ,
\]
where \(w>0\) is frozen during the step. Define
\[
\mathcal E:=|\Rm|_{\rm ten}^2-4|E|^2.
\]
In dimension four,
\[
\mathcal E\,d\mu=32\pi^2 e(TM,g).
\]

For a fixed cutoff \(\phi\), put
\[
P_\phi(g)=\int\phi |E|^2\,d\mu.
\]
Its variation has the exact form
\[
DP_{\phi,g}(h)=\int\langle \phi Q+C_\phi,h\rangle\,d\mu,
\]
where
\[
C_\phi
=2(D\Ric)^*(\phi E)-2\phi(D\Ric)^*E
\]
and therefore
\[
|C_\phi|
\le C\bigl(|\nabla\phi|\,|\nabla E|
            +|\nabla^2\phi|\,|E|\bigr).
\]

Introduce the double dual curvature tensor
\[
\begin{aligned}
\mathcal R_{ikjl}
={}&R_{ikjl}
-g_{ij}\Ric_{kl}-g_{kl}\Ric_{ij}
+g_{il}\Ric_{kj}+g_{kj}\Ric_{il}\\
&+\frac{s}{2}(g_{ij}g_{kl}-g_{il}g_{kj}),
\end{aligned}
\]
which satisfies
\[
\nabla^k\mathcal R_{ikjl}=0.
\]
The localized Lovelock identity is
\[
D_g\!\left(\int\phi\mathcal E\,d\mu\right)(h)
=
-4\int \mathcal R_{ikjl}\nabla^k\nabla^l\phi\,h^{ij}\,d\mu.
\]
This is the decisive Chern–Weil cancellation: after integration by parts, the Pfaffian flux contains neither \(\nabla W\) nor \(\nabla h\).

Consequently,
\[
\boxed{
\frac d{dt}\int\phi|\Rm|_{\rm ten}^2\,d\mu
=
-4\int\phi w|Q|^2\,d\mu
-4\int w
\left\langle
C_\phi-\mathcal R_{ikjl}\nabla^k\nabla^l\phi,\,
Q
\right\rangle d\mu .
}
\tag{1}
\]
If \(\phi=\phi(t)\), add
\[
\int \partial_t\phi\,|\Rm|_{\rm ten}^2\,d\mu.
\]
For a DeTurck presentation, either pull back to the geometric flow or transport the cutoff by the DeTurck vector field. There is then no separate uncontrolled transport term.

Two important consequences are:

* no derivatives of \(w\) occur in the exact localized energy identity (1);
* the Weyl energy is controlled locally through the Euler transgression without estimating \(\nabla W\) directly.

For \(\phi=\eta^4\), Young’s inequality gives
\[
\boxed{
\begin{aligned}
\frac d{dt}\int\eta^4|\Rm|^2\,d\mu
+2\int\eta^4w|Q|^2\,d\mu
\le C\int w\Bigl[
&\eta^2|\nabla\eta|^2|\nabla E|^2\\
&+\bigl(|\nabla^2\eta|^2+|\nabla\eta|^4\bigr)|\Rm|^2
\Bigr]d\mu .
\end{aligned}}
\tag{2}
\]
On a ball of scale \(r\), if
\[
cr^4\le w\le Cr^4,\qquad
|\nabla\eta|\le Cr^{-1},\qquad
|\nabla^2\eta|\le Cr^{-2},
\]
then
\[
\frac d{dt}\int\eta^4|\Rm|^2
+2D_\eta
\le
Cr^2\int\eta^2|\nabla E|^2
+C\int_{\supp\eta}|\Rm|^2,
\tag{3}
\]
where
\[
D_\eta=\int\eta^4w|Q|^2.
\]

Thus the local concentration estimate reduces to controlling first derivatives of Ricci and scalar curvature by \(Q\).

---

# 2. The coercive Ricci–scalar multiplier

Schematically, with coefficients consistent with the \(P\)-gradient convention,
\[
Q=-\Delta E+\frac12\nabla^2s-\frac14(\Delta s)g
+\Rm*E+E*E,
\qquad
\tr Q=-\frac12\Delta s.
\tag{4}
\]
Pairing \(Q\) only with \(E\) produces a bad scalar-gradient sign. The correct multiplier is
\[
T=E+\frac{s}{2}g.
\]
After integration by parts,
\[
\boxed{
\int\langle Q,T\rangle
=
\int\left(|\nabla E|^2+\frac18|\nabla s|^2\right)
+\int \Rm*E*E .
}
\tag{5}
\]
The last integral denotes fixed algebraic contractions bounded by
\[
C\int |\Rm|\,|E|^2.
\]

With a cutoff \(\eta^2\), the localized version yields
\[
\begin{aligned}
I_\eta
&:=\int\eta^2\bigl(|\nabla E|^2+|\nabla s|^2\bigr)\\
&\le
C\|\eta^2Q\|_2
 \|\Rm\|_{L^2(\supp\eta)}
+C\int|\nabla\eta|^2|\Rm|^2
+C\int\eta^2|\Rm|\,|E|^2 .
\end{aligned}
\tag{6}
\]

Assume the scale-\(r\) local Sobolev inequality
\[
\|u\|_4^2
\le C_S\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right).
\tag{7}
\]
By Kato and Hölder,
\[
\begin{aligned}
\int\eta^2|\Rm|\,|E|^2
&\le \|\Rm\|_2\,\|\eta E\|_4^2\\
&\le CC_S\|\Rm\|_2
\left[
\int\eta^2|\nabla E|^2
+\int|\nabla\eta|^2|E|^2
+r^{-2}\int\eta^2|E|^2
\right].
\end{aligned}
\]
Hence, if
\[
CC_S
\left(\int_{\supp\eta}|\Rm|^2\right)^{1/2}
\le\frac12,
\tag{8}
\]
the cubic term is absorbed. Writing
\[
H=\int_{\supp\eta}|\Rm|^2,
\]
one obtains
\[
r^2 I_\eta
\le C D_\eta^{1/2}H^{1/2}+CH
\le \theta D_\eta+C_\theta H.
\tag{9}
\]
Substitution into (3) gives the basic localized concentration inequality
\[
\boxed{
\frac d{dt}\int\eta^4|\Rm|^2+cD_\eta
\le CH.
}
\tag{10}
\]

This identifies exactly where \(C_S\) enters: only through the critical \(L^4\) absorption (8). The allowable small-energy threshold is therefore
\[
\varepsilon_0\lesssim C_S^{-2}
\]
up to universal constants.

---

# 3. Recovering derivatives of the full curvature

The Ricci dissipation controls the Weyl derivatives through the Bianchi system. Viewing \(\Rm\) as a bundle-valued two-form,
\[
d^\nabla\Rm=0,\qquad
\delta^\nabla\Rm
=\nabla\Ric-\nabla\Ric^{\rm swap}.
\]
A localized Hodge–Weitzenböck estimate gives
\[
\int\eta^2|\nabla\Rm|^2
\le
C\int\eta^2|\nabla\Ric|^2
+Cr^{-2}\int_{\supp\eta}|\Rm|^2
+C\int\eta^2|\Rm|^3.
\tag{11}
\]
The last term is absorbed under (8), yielding
\[
\boxed{
\int\eta^2|\nabla\Rm|^2
\le
C\int\eta^2|\nabla\Ric|^2
+Cr^{-2}H.
}
\tag{12}
\]

For higher-order estimates, a useful replacement for the Kuwert–Schätzle interpolation inequalities is
\[
\|\xi F\|_4^2
\le CC_S\|\xi F\|_2
\left(
\|\xi\nabla^2F\|_2
+r^{-1}\|\nabla F\|_{L^2(\supp\xi)}
+r^{-2}\|F\|_{L^2(\supp\xi)}
\right).
\tag{13}
\]
In particular,
\[
\int|\xi\Rm|^4
\le CC_S^2H
\left(
\int_{\supp\xi}|\nabla^2\Rm|^2+r^{-4}H
\right).
\tag{14}
\]
Using nested cutoffs, the trace equation in (4), the Ricci equation, and differentiated Bianchi–Weitzenböck estimates then give
\[
\boxed{
r^4\int_{\rm inner}
\left(|\nabla^2\Rm|^2+|\nabla^2s|^2\right)
\le
Cr^4\int_{\rm outer}|Q|^2+CH.
}
\tag{15}
\]
This is the correct endpoint regularity: it yields \(\Rm\in W^{2,2}\), hence every finite \(L^q\), but not an immediate \(L^\infty\) bound at the initial time, exactly as noted in Step 52.

---

# 4. How frozen-weight derivatives enter

Although \(\nabla w\) does not enter the exact energy balance (1), it does enter curvature evolution and parabolic bootstrap:
\[
\nabla^2(wQ)
=w\nabla^2Q+2\nabla w*\nabla Q+\nabla^2w*Q.
\tag{16}
\]
At a ball with initial own scale \(r\), the natural hypotheses are
\[
cr^4\le w\le Cr^4,\qquad
|\nabla^jw|\le K_jr^{4-j}.
\tag{17}
\]
After rescaling \(g\mapsto r^{-2}g\), these become bounded coefficients:
\[
c\le \widehat w\le C,\qquad
|\widehat\nabla^j\widehat w|\le K_j.
\]
For the basic \(m=0\) curvature estimate, \(j\le2\) is enough. To bootstrap through order \(m\), one needs finitely many \(K_j\), typically through \(m+2\).

The expected weighted analogue of Streets’ local Sobolev smoothing estimate is
\[
\begin{aligned}
\frac d{dt}\int\eta^{2m+4}|\nabla^m\Rm|^2
+c\int\eta^{2m+4}w|\nabla^{m+2}\Rm|^2
\le{}&
C\int_{\rm outer}|\nabla^m\Rm|^2\\
&+C_m\int_{\rm outer}|\Rm|^2.
\end{aligned}
\tag{18}
\]
The constants depend on \(C_S\), nested cutoff bounds, and finitely many \(K_j\).

The supplied Streets paper does **not** prove this from initial energy-radius control. Its local estimates assume suitable cutoffs and spacetime curvature/control data; its pointwise smoothing theorem assumes a spacetime curvature bound. Its Remark 1.12 explicitly identifies curvature-scale noncollapsing as open. Thus Streets supports the bootstrap after curvature control, not the missing critical-energy startup.

Two unresolved analytic inputs remain:

1. **Intrinsic cutoff/chart startup.** Small \(L^2\)-curvature plus a local Sobolev inequality does not automatically furnish distance cutoffs with controlled Hessian, nor harmonic coordinates with the needed initial regularity. A Coulomb-frame construction may help, but one must convert control of the Levi-Civita connection into metric coordinates and cutoff Hessian estimates.

2. **Sobolev persistence.** If \(h=\partial_tg\), then for a fixed test function
   \[
   \frac d{dt}\int|\nabla u|^2\,d\mu
   =
   \int\left[-h(\nabla u,\nabla u)
   +\frac12(\tr h)|\nabla u|^2\right]d\mu,
   \tag{19}
   \]
   while
   \[
   \frac d{dt}\log\left(\int u^4\,d\mu\right)^{1/2}
   =
   \frac14
   \frac{\int(\tr h)u^4\,d\mu}{\int u^4\,d\mu}.
   \tag{20}
   \]
   The available \(L^2(w^{-1}d\mu)\) control of \(h=-wQ\) does not uniformly control these forms over all \(H^1\) functions. An \(L^\infty\) bound for \(h\) would suffice, but the critical startup estimate is expected to behave like \(t^{-1}\), which is not integrable. Hence the claimed Sobolev persistence cannot presently be inferred from the energy identity.

---

# 5. Precise failure of the hard-radius upper comparison

Take a flat four-torus and perturb it inside a ball of radius \(\ell\):
\[
g_{\ell,a}=g_{\rm flat}+a\,k(x/\ell),
\]
where \(k\) is a fixed smooth compactly supported symmetric tensor and \(a\) is small. The Sobolev constants remain uniformly controlled because the metrics are uniformly bilipschitz to the flat metric. Four-dimensional scaling gives
\[
\int|\Rm(g_{\ell,a})|^2=C_ka^2+O(a^3).
\]
Choose \(a\) so that
\[
\int|\Rm(g_{\ell,a})|^2=\varepsilon+\zeta,
\qquad \zeta>0.
\]
At the packet center,
\[
r_\varepsilon(g_{\ell,a})\asymp\ell.
\]
The frozen weight there is \(w\asymp\ell^4\); after rescaling the packet to unit size, the weighted flow evolves on order-one own-scale time. Choose \(k\) noncritical, so initially
\[
\frac d{dt}\int|\Rm|^2
=-4\int w|Q|^2<0.
\]
Taking \(\zeta\downarrow0\), the total energy crosses below \(\varepsilon\) in arbitrarily short own-scale time. Once it does,
\[
r_\varepsilon(x,t)=r_0
\]
for every \(x\), because the energy of the entire manifold is below the threshold. Hence
\[
\frac{r_\varepsilon(x,t)}{r_\varepsilon(x,0)}
\asymp \frac{r_0}{\ell}\to\infty.
\tag{21}
\]

Therefore the universal two-sided comparison in 52.KS is false. This failure is a discontinuity of the hard threshold; it does not require Weyl transport through a neck.

A Weyl-transfer neck remains a possible obstruction to more refined local statements, but it is not needed to refute the lemma. Moreover, the branch claim that an order-one Pfaffian charge can necessarily cross a neck with arbitrarily small \(Q\)-dissipation was not established from the supplied sources and should not be treated as a counterexample without an explicit family satisfying the flow equation and quantitative flux estimates.

A restricted theorem for near minimizers with
\[
P(g)-\alpha(M)\ll\varepsilon
\]
is not ruled out by (21), but it would require a new local-replacement argument showing that Ricci-active threshold packets cannot occur in near-minimizing data. The flow identities alone do not provide that fact.

---

# 6. Weak replacement sufficient for \((\mathrm{PS}_\varepsilon)\)

For a fixed-weight segment define
\[
D(t)=\int w|Q|^2,\qquad
R(t)=\int r_\varepsilon(g(t))^4|Q|^2,
\]
and
\[
A(t)=\max\left\{1,\sup_M\frac{r_\varepsilon(g(t))^4}{w}\right\}.
\]
Then
\[
R(t)\le A(t)D(t),
\qquad
\int_0^TD(t)\,dt
=P(g(0))-P(g(T)).
\]
Define the output-compatible time
\[
\Theta(T)=\int_0^T A(t)^{-1}\,dt.
\]
Since \(D\ge A^{-1}R\),
\[
\boxed{
\inf_{0<t<T}R(t)
\le
\frac{P(g(0))-P(g(T))}{\Theta(T)}
\le
\frac{P(g(0))-\alpha(M)}{\Theta(T)}.
}
\tag{22}
\]

Thus the exact replacement needed for selection is not radius comparability but enough output-compatible time:

* along infinitely many frozen segments,
  \[
  \sum_n\Theta_n=\infty,
  \]
  together with a Sobolev bound at selected times; or

* for a minimizing sequence with excess
  \[
  \delta_i=P(g_i)-\alpha(M),
  \]
  finite paths satisfying
  \[
  \frac{\delta_i}{\Theta_i}\to0.
  \tag{23}
  \]

Then (22) produces
\[
\int r_\varepsilon(g_i(t_i))^4|Q(g_i(t_i))|^2\to0,
\]
which is precisely \((\mathrm{PS}_\varepsilon)\).

This replacement also clarifies why one-sided nonshrinking of the radius is insufficient: the problematic factor is the possible growth of the output radius relative to the frozen weight.

---

# 7. Threshold-averaged radius and adaptive flow

A more stable scale is
\[
\mathfrak r_\varepsilon(x)
=
\left[
\frac1\varepsilon
\int_\varepsilon^{2\varepsilon}r_a(x)^4\,da
\right]^{1/4}.
\tag{24}
\]
It satisfies
\[
r_\varepsilon\le\mathfrak r_\varepsilon\le r_{2\varepsilon},
\tag{25}
\]
and, by Minkowski together with the \(1\)-Lipschitz property of each \(r_a\),
\[
|\mathfrak r_\varepsilon(x)-\mathfrak r_\varepsilon(y)|
\le d(x,y).
\tag{26}
\]
Also,
\[
\int_{B(x,\mathfrak r_\varepsilon(x))}|\Rm|^2\le2\varepsilon,
\tag{27}
\]
and
\[
\int r_\varepsilon^4|Q|^2
\le
\int\mathfrak r_\varepsilon^4|Q|^2.
\tag{28}
\]

An adaptive weight
\[
w(t,\cdot)\asymp\mathfrak r_\varepsilon(g(t),\cdot)^4
\]
therefore tracks the output scale directly and avoids the threshold jump. Importantly, neither the global dissipation identity
\[
\frac d{dt}P=-\int w|Q|^2
\]
nor the localized identity (1) contains \(\partial_tw\). The remaining difficulty is well-posedness for a coefficient depending nonsmoothly on the evolving metric, plus intrinsic cutoff construction and Sobolev persistence. A regularized-in-space, measurable-in-time coefficient formulation may be sufficient; differentiability of \(w\) with respect to \(g\) is not required by the energy law.

---

# 8. Flow-free selection: weighted Ekeland or proximal descent

The cleanest alternative avoiding lifespan is a weighted metric-slope construction. Define
\[
\|h\|_{\mathfrak r,g}^2
=
\int_M\mathfrak r_\varepsilon(g)^{-4}|h|_g^2\,d\mu_g.
\tag{29}
\]
Formally, its dual norm is
\[
\|DP_g\|_{\mathfrak r,*}^2
=
\int_M\mathfrak r_\varepsilon(g)^4|Q(g)|^2\,d\mu_g.
\tag{30}
\]
If Ekeland’s principle yields a metric \(h\) satisfying
\[
P(v)\ge P(h)-\eta\,d_{\mathfrak r}(v,h)
\]
for nearby \(v\), differentiating along arbitrary smooth metric variations gives
\[
\int\mathfrak r_\varepsilon(h)^4|Q(h)|^2\,d\mu_h
\le\eta^2.
\tag{31}
\]
Taking \(\eta\to0\) along a minimizing sequence immediately implies \((\mathrm{PS}_\varepsilon)\) by (28).

Equivalently, one may minimize the proximal functional
\[
P(h)+\frac1{2\tau}d_{\mathfrak r}(h,g)^2.
\tag{32}
\]
For input excess \(\delta=P(g)-\alpha\),
\[
d_{\mathfrak r}(h,g)^2\le2\tau\delta,
\qquad
\int\mathfrak r_\varepsilon(h)^4|Q(h)|^2
\le\frac{2\delta}{\tau}.
\tag{33}
\]
Choosing \(\tau=\tau_i\) with \(\delta_i/\tau_i\to0\) would give the required residual.

The missing theorem is precise:

> Construct a complete lower-semicontinuous relaxation of the weighted metric space such that a finite-slope point with a uniform local Sobolev inequality and \(2\varepsilon\)-small curvature on its \(\mathfrak r_\varepsilon\)-balls has a nondegenerate metric representative in local \(W^{4,2}\), satisfies the distributional \(P\)-gradient equation, and can be approximated by smooth metrics while preserving \(P\) and the weighted \(L^2\) residual.

The elliptic ingredients are already visible in (4)–(15) and Proposition 52.1. The genuinely unresolved issues are completion/nondegeneracy and preservation of the Sobolev interior. A hard Sobolev constraint cannot simply be imposed: if active, it contributes a multiplier and no longer yields the plain \(Q\)-residual.

A local “solve \(DQ\,u\simeq r^4Q\)” one-step descent is less robust than this metric-slope formulation. Near-minimality controls the first variation only after one proves uniform nonlinear remainder estimates and patches local gauges globally; those are essentially the same critical elliptic regularity problems hidden in a different form.

---

# 9. Corrected analytic target

The strongest defensible replacement for 52.KS is therefore:

### Local concentration/smoothing statement

Under a local Sobolev bound, \(2\varepsilon\)-small curvature energy, frozen coefficient bounds (17), and the availability of controlled nested cutoffs, the fixed-weight flow satisfies (10), (12), (15), and the higher-order estimate (18). This should imply short-time **nonshrinkage** of an appropriate averaged energy scale and positive-time own-scale smoothing.

### Selection statement

Use either:

1. frozen segments satisfying the output-compatible time condition (23);
2. an adaptive weight comparable to \(\mathfrak r_\varepsilon^4\); or
3. weighted Ekeland/proximal selection satisfying (31) or (33).

Any of these, together with uniform local Sobolev control at the selected metrics, is sufficient for Theorem 52.3.

The remaining scientific objects are sharply isolated:

* intrinsic critical-energy cutoffs or startup coordinates;
* Sobolev persistence/noncollapse;
* existence for adaptive coefficients, or completion and regularity for weighted metric-slope selection.

The local Weyl-energy issue itself is substantially resolved by the exact double-dual/Pfaffian identity (1); it is not the central remaining obstruction.