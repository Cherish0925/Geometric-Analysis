# Step 26 summary — action-budget matching, constraint pinning, and late opening

The small-bolt route was rebuilt around a distinction that prevents an invalid Einstein reduction. For exact Einstein metrics with bolt scale b→0, rescaling by b^{-2} gives Ric=-6b²g# and any sufficiently smooth pointed limit is Ricci-flat. For scalar-normalized near-minimizers with only P-hat≤c<1, the same rescaling leaves P-hat invariant and sends s=-24 to -24b², so a smooth limit is only scalar-flat; nonzero trace-free Ricci action can remain. The regular Einstein bolt series therefore studies only the exact-Einstein branch, not the full cell infimum.

The verified chiral identities imply an exact bolt-to-section budget. For an O(-1) bolt, b+=(1), b-=7, and every diagonal prefix obeys
P-hat_prefix ≥ max{0,b+(Σ)-1,b-(Σ)-7}; retaining the common scalar term gives the stronger max{0,b+-1+SΣ,b--7+SΣ}, where SΣ=(96π²)^{-1}∫s². The two chiral estimates are for the same action and must not be added. Controlled collapsed first jets x=Xz³, p=Pz, chi=Cz, eta=Nz have b+=-2-(C+4X)² and b-=2+(C-4X)². Thus a bounded total action c forces (C-4X)²≤c+5. On the plus kernel C+4X=0, 64X²≤c+5; at c=.99585 this gives |X|≤.306081, so (X,C)=(1,-4) would cost at least 59 in the minus channel. This is an asymptotic controlled-section result, not an all-sequence matching theorem. The raw eta=-8 numerical entry is excluded even more strongly: its b-=8.54957, so its bolt prefix costs at least 1.54957.

I independently re-derived the peer's scalar-normalized constraint equations with zero symbolic residuals in `scripts/step26_independent_constraint_and_D_pin.py`, output `data/step26_independent_constraint_and_D_pin.json`. The Hamiltonian residual C=(e0−Σei)/2 equals Ric°00 at s=-24, propagates by C'=-2SC−Σ(S−yi)ei, and S'=18−S²+R3+C. I independently derived the exact contact-slot equation
(Wq')'=W(Pg−Ph−D), q=log(ag/ah), D=eg−eh,
with Pg−Ph=−8z sinh q+8z²kappa^{-2}sinh(2q). A Green identity gives a drift-corrected D pinning bound P-hat≥M²/[8∫WK²], but only after controlling endpoint momentum, volume, and geometric drift.

A first-barrier correction makes Lemma W sound: if R3≥−rho0, A²=18−rho0>0, m=min{S(T),A}, and the stated C-action smallness holds, then S≥sigma, W grows at least exponentially, and ∫W^{-1}≤(sigma W(T))^{-1}. The proof must use the first point at which S reaches sigma; it does not require S(T)≤A.

A stronger two-stage Green identity now removes the free momentum at the beginning of an expanding block. For T−<T0<T1, J=Wq', K(t)=∫_t^{T1}W^{-1}, and Pi=Pg−Ph, the renormalized mismatch
M=q(T1)−q(T0)−(J(T−)+∫_{T−}^{T0}W Pi)K(T0)−∫_{T0}^{T1}WPiK
satisfies
M=−K(T0)∫_{T−}^{T0}WD−∫_{T0}^{T1}WDK.
Therefore P-hat over both intervals is bounded below by M² divided by 8 times the corresponding Green denominator. In an expanding block with S≥sigma, B=yg+yh≥mu, |q|≤Q, kappa≥kappa0, one obtains explicit bounds on K and Pi drift; if expansion fails, the Hamiltonian residual already costs sigma W(T0)(m−sigma)²/3. The resulting alternative is: upward chiral charge variation, Hamiltonian loss of expansion, or a momentum-renormalized D mismatch. Exact Einstein arcs show why no hypothesis-free positive late-opening cost can follow from q change and a one-sided charge cap alone.

This step materially advances the central lower-bound route but does not close it. The remaining theorem-level work is to establish a global entry/exit estimate for the expanding-block hypotheses and the incoming flux produced before them, while retaining scalar-flat non-Einstein rescaled cores. The D pinning script and the exact chiral budgets are reusable tools for that task. Large-bolt face asymptotics remain numerical; the certified global construction is unchanged.
