# Step 25 — Controlled collapse charge and bolt matching

## Verified algebra
The peer's controlled scale-free collapse uses
\(x=\log(a_f/a_g)\), \(z=(a_h/a_g)^{1/3}\), \(p=r(\log r)'\), \(\chi=rx'\), \(\eta=rq'\), with \(r=(a_fa_ga_h)^{1/3}\) and \(q=\log(a_g/a_h)\). Under
\[
x=Xz^3+o(z^3),\quad p=Pz+o(z),\quad\chi=Cz+o(z),\quad\eta=Nz+o(z),
\]
the exact spin variables satisfy
\[
u_f=P+\frac23C+\frac13N+2X,\quad u_g=P-\frac13C+\frac13N-2X,\quad u_h=-2.
\]
Therefore
\[
b_+^{\rm end}=2-\sum u_i^2-u_fu_gu_h=-2-(C+4X)^2,
\]
and, with the corrected opposite orientation algebraic normalization,
\[
b_-^{\rm end}=2+(C-4X)^2.
\]
Both are independent of \(P,N\). The consequence is a first-jet charge statement: decollapse to a round orbit costs at least \(4+(C+4X)^2\) in normalized \(\widehat P=P/(8\pi^2)\). This is exact only for the stated controlled jet class; it does not classify arbitrary collapsed first jets.

Independent execution of `Sessions/S1003A02/workspace/scripts/collapse_chiral_charge_limit.py` returned exactly the above limits. TTCS also checked the derivation and found that the source's earlier opposite-charge expression was not geometrically normalized; the corrected form is the one recorded here.

## Smooth bolt matching: what is and is not implied
For the regular Ric=-6 O(-1) bolt (collapsing slot 3), the series source gives
\[
a_f=b+c_2t^2+p_4t^4+\cdots,\quad a_g=b+c_2t^2+q_4t^4+\cdots,\quad a_h=t+r_3t^3+\cdots,
\]
with \(c_2=(3b^2+2)/(2b)\), \(r_3=-2/(3b^2)\), and free anisotropy \(d=p_4-q_4\). Setting \(z=(a_h/a_g)^{1/3}\) gives at fixed \(b>0\)
\[
x=b^3d\,z^{12}+O_b(z^{18}),\qquad\chi=4b^3d\,z^{10}+O_b(z^{16}),
\]
\[
p=\frac1{3z^2}+O_b(z^4),\qquad \eta=-\frac1{z^2}+O_b(z^4).
\]
Thus the local bolt limit has \(b_+\to1\), as required for the bolt charge, and is not the controlled Berger endpoint \(b_+\to-2\). The finite-order series is not uniform as \(b\to0\); it cannot by itself propagate to a scale-one section.

At a scale-one collapsed section with \(a_g\to L>0\), \(a_h/a_g=z^3\to0\), the controlled assumptions \(x=O(z^3)\), \(p,\chi,\eta=O(z)\) are extra global matching information, equivalent to bounded first logarithmic jets / second fundamental form at the section. Smooth bolt regularity alone does not imply them. The scale-one matched Einstein orbit must be analyzed through the full ODE in the overlap region \(t/b\to\infty\), controlling the free parameter \(d(b)\); no relation such as \(C+4X=0\) follows from the bolt series.

The label “finite curvature” for the \(z^3\) class is too strong. For fixed base size, full orbit curvature boundedness requires at least \(x=O(z^6)\), and mixed curvature gives stronger radial control such as \(\chi=O(z^4)\), hence \(X,C\to0\) and charge \(-2\). The \(z^3\) class should be called controlled first-jet / finite-charge. Slot labels must be kept explicit: the bolt collapses slot 3, while `ach_projected.py`'s `f=0` refers to a different fiber slot after cyclic relabeling.

## Collapse warnings from the new data
The raw fixed \(\eta=-8\) entry at \(\varepsilon=1/16\) has \(b_+=1.45193684\), so any omitted prefix from the bolt to that section already costs at least \(0.45193684\) by the chiral annular inequality. With the independently reconstructed prefix plus connector the total is \(\ge1.0264\), so the apparent 0.5454 collocation value is not a regular-cell competitor. At \(\varepsilon=1/32\), the same raw perturbation costs 2.9425. Controlled regular perturbations (including the kernel \(C+4X=0\)) trend toward the charge-four value rather than below the certified 0.99585 cell.

The beta-pinning estimate retains the actual denominator \(\int dt/W\) on a general connector. The exact CH formula \(I(T)\) may only be substituted after proving a pointwise lower comparison for \(W\). The peer's threshold at \(T=.70\) is \(C_*=0.370125\) under that CH-tail comparison.

## Research consequence
The collapsed branch is now split cleanly: (i) controlled first-jet decollapse, where the chiral charge supplies a direct cost (at least 4, or more with shear); (ii) ordinary post-Rossi Berger/ALF connectors, excluded by Euler flux; and (iii) uncontrolled high-shear/raw contact-shear entries, which require an independent prefix/matching estimate. The next theorem-level target is therefore a global small-bolt matching estimate, not another finite-scale raw-entry optimization. The unrestricted lower bound, large-bolt branch, high-shear connectors, non-diagonal collapse, and global closed-manifold transfer remain unresolved.

Artifacts: `workspace/scripts/step25_bolt_matching_orders.py`, `workspace/data/step25_bolt_matching_orders.json`; peer sources `Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md` and `trace/ttcs/results/step30_ttcs01_verifier1_integration.md`.