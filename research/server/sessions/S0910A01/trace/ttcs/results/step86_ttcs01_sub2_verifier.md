# TTCS Independent Branch Record

```json
{
  "step_id": 86,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Sessions/S0910A01/workspace/notes/step85_green_response_computational_bridge.md",
    "Sessions/S0910A01/workspace/data/step85_product_operator_sector_ledger.json"
  ]
}
```

## Task

I am computing the exact inter-node obstruction coefficient for mixed-chirality Einstein desingularization of the product orbifold O=(S^2xS^2)/Z_2 with four A_1 (R^4/Z_2) nodes, following Ozuch's higher-order obstruction theory. The decisive structural finding of this step is that the correct inter-node coefficient is NOT a bulk product-Lichnerowicz spectral sum (which produced frame-sensitive proxy numbers -1.22, +0.41, -0.53 in prior work), but Ozuch's exact BOUNDARY PAIRING formula from Proposition 2.10 and Corollary 2.12 of arXiv:2105.13193 (file: Knowledge/objects/papers/Higher-order-obstructions...object.md, lines 606-666). Specifically:
(a) Prop 2.10 line 616: nu_l = 3 * integral over S^3/Z_2 of <H^4, V_{l,2}>_e, valid when lambda_k=0, where H^4=H^4(zeta_j^pm) is the ALE bubble's r^{-4} multipole at source node j, and V_{l,2} is the r^{+2}-growing homogeneous component of the orbifold obstruction/Einstein-deformation basis mode v_l = O(g_o) evaluated near the singular point.
(b) Cor 2.12 line 660: sum_j |zeta_j| lambda_1^j(zeta,v) = C sum_l <v,v_l> nu_l(zeta,0) + O(...), linking bubble first-obstruction variation to orbifold nu_l.
(c) H^4(zeta^+) = -rho(zeta)^- o zeta^+ /(2r^4) and H^4(zeta^-) = -zeta^- o rho(zeta)^+/(2r^4) are DIFFERENT symmetric 2-tensors depending on chirality (established in prior Step 84 with tr(C_ab C_cd)=4 delta_ac delta_bd).

MY CLAIM TO VERIFY: The mixed-row chirality coefficient c_opp - c_same reduces to the difference of boundary pairings nu_l(+) - nu_l(-) = 3 integral over S^3/Z_2 of <H^4(zeta^+) - H^4(zeta^-), V_{l,2}> where V_{l,2} is chirality-independent (it is a property of the orbifold Einstein deformation, common to all fillings), and only the source multipole H^4 carries the chirality. This is a clean r^{-4} source against r^{+2} receiver spherical boundary integral, so ONLY the degree-2 (in the R^4 harmonic sense) part of the receiver V_{l,2} survives against the degree-2 source multipole H^4, by orthogonality of RP^3 Laplacian eigenspaces (line 574, 636). 

QUESTIONS: (1) Is this reduction faithful to Ozuch's Prop 2.10 / Cor 2.12, i.e. is the inter-node coefficient genuinely the boundary integral 3*int<H^4, V_{l,2}> rather than a bulk resolvent, and does the chirality dependence enter only through H^4 with V_{l,2} chirality-independent? (2) What exactly is V_{l,2} for the product orbifold O=(S^2xS^2)/Z_2 -- is it the r^2-Taylor coefficient of the orbifold's Einstein-deformation obstruction modes O(g_o) at the node, and is the relevant space here the H_2-type quadratic tensor with P_e H_2 = Lambda e (line 476)? (3) Does the requirement lambda_k=0 (first obstruction vanishing, which prior steps established via EH-direction-in-kernel choice) legitimately hold at the leading order so that the Prop 2.10 formula applies, or does the mixed-chirality assignment spoil lambda_k=0? (4) Is there a genuine risk that nu_l is a per-NODE quantity (each node contributes its own bar-h^4_j, summed in line 641) so that the 'inter-node' language must be interpreted as: node j's source H^4(zeta_j) pairs with the GLOBAL orbifold mode v_l which is delocalized over all four nodes -- meaning the coupling between distinct nodes is mediated by the global obstruction mode v_l, not by a direct node-to-node Green function? Please read the source lines 449-666 carefully and give a precise mathematical assessment of whether the boundary-pairing reduction is correct and what V_{l,2} and v_l concretely are for this product orbifold.

## Output

## Verifier memo — the linking-sphere pairing $\nu_l=3\int_{\mathbb S^3/\mathbb Z_2}\langle H^4,V_{l,2}\rangle$ and the mixed-chirality inter-node coefficient

### Short verdict

The reduction you wrote down is faithful **as a statement about $\nu_l$**, the projection of the orbifold obstruction onto the global Einstein-deformation kernel $\mathbf O(\mathbf g_o)$. Ozuch's Prop 2.10 (lines 606–618) does give exactly the surface integral $3\int_{\mathbb S^3/\mathbb Z_2}\langle H^4,V_{l,2}\rangle_e$, valid when $\lambda_k=0$, and in that integral the chirality enters only through $H^4(\zeta^\pm)$ while $V_{l,2}$ is intrinsic to the orbifold. The degree-2 orthogonality argument is also correct.

But three things must be separated cleanly, because the memo currently fuses them:

1. $\nu_l$ (the on-sphere integral) is **not** the pairwise, node-to-node object $c_{ij}=L_iG_P^\perp S_j$ you computed earlier. It is a single scalar per global mode, aggregating all source nodes.
2. The reduction is **vacuous unless $\mathbf O(\mathbf g_o)\neq 0$**, and for $(S^2\times S^2)/\mathbb Z_2$ there is a strong structural reason to expect $\mathbf O(\mathbf g_o)=0$.
3. The genuinely decisive mixed-chirality coupling on this orbifold sits in the second obstruction $\mu_1^j$ / the induced curvature, which needs the compact resolvent $P_{g_o}^{-1}$ **including the direction on which $P$ is below zero** — precisely the piece the on-sphere pairing integrates away.

Details, question by question.

---

### Q1. Is the coefficient the surface integral rather than a resolvent, and does chirality enter only through $H^4$?

**Faithful part.** In the proof of Prop 2.10 (lines 646–658) the integration by parts against $\mathbf v_l$ uses $P_o\mathbf v_l=0$, so the bulk operator drops and only the term on the linking sphere $\{r_o=r\}$ survives:
$$
\int_{M_o}\langle P_o(\chi(H^4+H_2^4)),\mathbf v_l\rangle
= 3\!\int_{\mathbb S^3/\mathbb Z_2}\!\langle H^4,V_{l,2}\rangle_e
+\int_{\mathbb S^3/\mathbb Z_2}\!\langle H_2^4,V_{l,0}\rangle_e .
$$
The $\langle H^4,V_{l,0}\rangle$ piece is absent because $H^4$ (angular content at the second $\mathbb S^3/\mathbb Z_2$ eigenvalue) is orthogonal to the constant $V_{l,0}$ on the sphere (line 636). When $\lambda_k=0$, Lemma 2.3 gives $H_2^4=0$, so the second term drops and $\nu_l=3\int\langle H^4,V_{l,2}\rangle$. **This is genuinely resolvent-free for $\nu_l$**: you do not need to build $\bar h^4$ in the bulk to read off its component along a kernel mode. The factor $3$ is the $\tfrac12(-4-2)$ radial-weight combination from $\nabla_{\partial_r}H^4=-\tfrac4r H^4$, $\nabla_{\partial_r}V_{l,2}=\tfrac2r V_{l,2}$; it is correct.

**Chirality.** $\mathbf v_l\in\mathbf O(\mathbf g_o)$ is a deformation of the orbifold defined with no reference to any filling. Its Taylor jets $V_{l,0},V_{l,2}$ are intrinsic to the orbifold and the node chart. Gluing a $+$ or $-$ Eguchi–Hanson block does not touch them. So yes, $V_{l,2}$ is chirality-independent and only $H^4(\zeta^\pm)$ carries the chirality:
$$
\nu_l(+)-\nu_l(-)=3\!\int_{\mathbb S^3/\mathbb Z_2}\!\big\langle H^4(\zeta^+)-H^4(\zeta^-),\,V_{l,2}\big\rangle_e ,
\qquad
H^4(\zeta^+)=-\tfrac{\rho(\zeta)^-\!\circ\zeta^+}{2r^4},\;
H^4(\zeta^-)=-\tfrac{\zeta^-\!\circ\rho(\zeta)^+}{2r^4}.
$$

**Where the assertion is not exact.** Your own Step 85 definition is $c_{ij}=L_iG_P^\perp S_j$, an induced field at a receiving node obtained through the compact resolvent. That is a **different object** from $\nu_l$. Prop 2.10 removes the resolvent only from the kernel-projection $\nu_l$; it does not remove it from the induced curvature that enters $\mu_1^j$. So "the inter-node coefficient is the on-sphere integral, not a bulk resolvent" is true for $\nu_l$ and false for the induced-curvature/$\mu_1^j$ mechanism. Equating $c_{opp}-c_{same}$ with $\nu_l(+)-\nu_l(-)$ is only legitimate if the receiver functional $L_i$ is literally the pairing against a global mode $\mathbf v_l$ — in which case it is no longer a node-$i$-to-node-$j$ quantity (see Q4).

---

### Q2. What is $V_{l,2}$ for $O=(S^2\times S^2)/\mathbb Z_2$, and is it the $H_2$ with $P_e H_2=\Lambda e$?

**Correction of an identification.** $V_{l,2}$ is **not** the background quadratic coefficient $H_2$. The two objects satisfy different equations:

- $H_2$ is the $r^2$ jet of the *background metric* $\mathbf g_o=e+H_2+\dots$ and obeys the **inhomogeneous** $P_e H_2=\Lambda e$ (line 476); it encodes the node curvature $\mathbf R^\pm(H_2)$.
- $V_{l,2}$ is the $r^2$ jet of a *kernel mode* $\mathbf v_l\in\ker P_{g_o}$. Expanding $P_{g_o}\mathbf v_l=0$ at the node gives, at order $r^0$, $P_eV_{l,0}=0$ (so $V_{l,0}$ is constant), and at order $r^2$ a homogeneous-type equation with source from the node curvature acting on $V_{l,0}$, schematically $P_eV_{l,2}=\mathring R(H_2)\,V_{l,0}$. So $V_{l,2}$ is sourced by $V_{l,0}$ and the node curvature; it is a degree-2 tensor field, not the Einstein background jet.

**The pressing structural question: is $\mathbf O(\mathbf g_o)=0$?** $\mathbf O(\mathbf g_o)$ is the $L^2$ kernel of $P=\tfrac12\nabla^*\nabla-\mathring R$, i.e. the transverse-traceless infinitesimal Einstein deformations. For the product Kähler–Einstein orbifold this may well be empty:

- $\mathbb{CP}^1\times\mathbb{CP}^1$ is rigid as a Fano ($H^1(M,T^{1,0})=0$), so no infinitesimal Einstein deformations from complex moduli.
- The natural "shape" direction $h_0=g_1-g_2$ is TT ($\operatorname{tr}_{g}h_0=2-2=0$, $\delta h_0=0$) and is an eigenmode, but it is the **destabilizing direction with $\langle Ph_0,h_0\rangle<0$**, not a kernel element. Your own sector ledger records this: the constant-trace block $(\ell_1,\ell_2)=(0,0)$ gives $P=-1$ for $g_A\pm g_B$.
- The apparent $P=0$ modes at $(\ell_1,\ell_2)=(1,0),(0,1)$ in the trace blocks are $u\,g$ with $u$ a first spherical harmonic; on the round $S^2$, $\operatorname{Hess}u+u\,g=0$, so $u\,g\propto\mathcal L_{\nabla u}g$ is pure gauge and does not enter the TT, gauge-fixed $\mathbf O(\mathbf g_o)$.

If $\mathbf O(\mathbf g_o)=0$, then there are no $\mathbf v_l$, the sum $\sum_l$ is empty, and $\nu_l(+)-\nu_l(-)$ is identically absent — the reduction computes nothing and cannot separate the two chiralities. **Determining $\dim\mathbf O(\mathbf g_o)$ (TT, $\mathbb Z_2$-invariant, gauge-fixed) is the single most decisive missing input** before the on-sphere pairing can be claimed to carry the mixed-chirality answer.

---

### Q3. Does $\lambda_k=0$ hold, and does the mixed assignment spoil it?

Here the transfer to $O$ is clean and checkable. Compute the curvature operator of $S^2(1)\times S^2(1)$ (Einstein constant $\Lambda=1$, scalar $s=4$). Sectional curvature is $1$ on planes tangent to one factor and $0$ on mixed planes, so on $\Lambda^2=\langle\omega_1\rangle\oplus(T_1\otimes T_2)\oplus\langle\omega_2\rangle$ the operator is $\mathbf R(\omega_i)=\omega_i$ and $\mathbf R=0$ on mixed forms. Splitting into $\Lambda^\pm$:
$$
\mathbf R^+=\operatorname{diag}(1,0,0)\ \text{on}\ \{(\omega_1{+}\omega_2)/\sqrt2,\phi_1^+,\phi_2^+\},\qquad
\mathbf R^-=\operatorname{diag}(1,0,0)\ \text{on}\ \{(\omega_1{-}\omega_2)/\sqrt2,\phi_1^-,\phi_2^-\}.
$$
Both are rank one with $\operatorname{tr}\mathbf R^\pm=1=\Lambda$, i.e. exactly Ozuch's form (4) $\operatorname{diag}(0,0,\Lambda)$ — in **both** orientations (the product is ambi-Kähler at equal radii). Consequences:

- $\lambda_k(\zeta^+)=c\langle\mathbf R^+\zeta^+,\zeta^+_{(k)}\rangle=0$ for all $k$ iff $\zeta^+\in\ker\mathbf R^+=\operatorname{span}\{\phi_1^+,\phi_2^+\}$ (2-dimensional). The same holds for $\zeta^-$ with the 2-dimensional $\ker\mathbf R^-$.
- A mixed assignment (some nodes $+$, others $-$) does **not** spoil $\lambda_k=0$: at each node the bubble direction can independently be placed in the appropriate 2-dimensional kernel. Prop 2.10 then applies at each node.
- With $\zeta^+$ in the kernel, the residual $2\times2$ block is $\operatorname{diag}(1,0)$, so $\mu_1=C\det[\cdot]=0$ as well.

So both the first and second obstructions vanish at leading order for either chirality, which is exactly why a higher-order/inter-node quantity is the decisive one — your strategic framing is sound and this fact is a firm, independently verifiable footing.

---

### Q4. Is $\nu_l$ per-node, with coupling mediated by the delocalized global mode?

Yes, and this is the correct reading. The multi-node version (line 641) is
$$
P_o\bar h^4=\sum_l\nu_l\mathbf v_l+\sum_j\sum_k\lambda_k^j\,\overline{\mathbf o}^4_{j,k},
\qquad
\nu_l=\sum_{j}3\!\int_{\text{node }j}\!\langle H^4(\zeta_j),V^{(j)}_{l,2}\rangle_e .
$$
Each summand is an **on-node** integral: $H^4$ of the bubble at node $j$ paired with the jet of $\mathbf v_l$ at the *same* node $j$. There is no term pairing $H^4$ at node $j$ against data at a different node $i$. Distinct nodes are coupled only because they project onto the *same* delocalized kernel mode $\mathbf v_l$. There is no direct node-to-node Green function in the $\nu_l$ obstruction; the "inter-node" content is entirely carried by the global mode's jets at the several nodes. Contrast this with Ozuch's flat-torus induced curvature $\mathbf R^\pm(j_0)=\sum_{i}B^L_{j_0-i}(\zeta_i,\zeta_i)$ (Cor 4.3, eqn 110): *that* is a genuine pairwise lattice sum of $r^{-4}$ tails, and it lives in the second obstruction $\mu_1^{j}=C\det[\cdot]$, not in $\nu_l$.

---

### The decisive structural concern for the mixed-chirality decision

Put the two mechanisms side by side for $O$:

- **Route A — $\nu_l$, linking-sphere integral.** Sees only $\ker P$. On the flat torus these are the flat $L$-deformations (real zero modes) and Route A produces the equations (112)–(113). On $(S^2\times S^2)/\mathbb Z_2$ the analogous shape direction $g_1-g_2$ is a **direction on which $P$ is below zero**, not a kernel mode, so it does **not** appear as any $\nu_l$. If $\ker P=0$, Route A is empty.
- **Route B — $\mu_1^j$, induced curvature.** On the flat torus $\mathbf R^\pm_{g_o}=0$, so the entire node curvature is the periodized tail sum $\sum_iB_{j-i}$; the resolvent is explicit. On $O$ the background already sits at form (4) with $\mathbf R^\pm_{g_o}=\operatorname{diag}(1,0,0)$, and the bubble-induced correction to the residual $2\times2$ block is what makes $\mu_1^j$ move off zero. That correction is $L_i P_{g_o}^{-1}S_j$ — a true compact-orbifold resolvent, **not** a closed-form lattice sum, and it necessarily runs through the whole non-kernel spectrum, **including the destabilizing shape direction** with $\langle Ph_0,h_0\rangle<0$.

Because the physics of $S^2\times S^2$ is dominated by that destabilizing direction, and because Route A integrates that direction away (it is not a $\mathbf v_l$), the on-sphere pairing $\nu_l(+)-\nu_l(-)$ is unlikely to be where the mixed-chirality decision lives on this orbifold. The frame-sensitive proxy numbers you obtained earlier ($-1.22,+0.41,-0.53$) were attempts at Route B; their instability is much more plausibly explained by the acknowledged use of raw $H^4$ instead of the matched, gauge-corrected source $S_j^\epsilon$ and by the receiver functional $L_i$ not yet being derived from Ozuch's radial curvature-jet, than by Route B being the wrong operator. Route B is the structurally correct home of the pairwise coefficient; it needs the corrected source/receiver normalizations, not replacement by the on-sphere pairing.

---

### What resolves this, concretely

1. **Compute $\mathbf O(\mathbf g_o)$ for $(S^2\times S^2)/\mathbb Z_2$**: the $\mathbb Z_2$-invariant TT gauge-fixed kernel of $P$. Separate genuine zero modes from the $u\,g$ gauge modes and from the destabilizing $g_1-g_2$ direction (which has $\langle Ph_0,h_0\rangle<0$). If this kernel is $\{0\}$, state that Route A returns an empty sum and the mixed-chirality answer must come from $\mu_1^j$.
2. If nonzero, write the explicit jets $V_{l,0},V_{l,2}$ of each surviving mode at the four nodes, then evaluate $3\int_{\mathbb S^3/\mathbb Z_2}\langle H^4(\zeta^+)-H^4(\zeta^-),V_{l,2}\rangle$ using $\operatorname{tr}(C_{ab}C_{cd})=4\delta_{ac}\delta_{bd}$ and the degree-2 angular projection you already control.
3. In parallel, keep Route B but replace raw $H^4$ by the matched source $S_j^\epsilon$ and derive $L_i$ from the radial curvature-jet; the residual $2\times2$ block correction at a receiving node, run through $P_{g_o}^{-1}$ on the full non-kernel spectrum, is the object that literally decides whether $c_{opp}\neq c_{same}$.

The reduction as written is internally correct for $\nu_l$ and its chirality structure; the open scientific substance is (i) whether $\ker P$ is nonempty here at all, and (ii) whether the mixed-chirality decision is a kernel-projection ($\nu_l$) phenomenon or an induced-curvature ($\mu_1^j$, full resolvent) phenomenon. On present evidence the second is the likelier home.