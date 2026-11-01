# TTCS Independent Branch Record

```json
{
  "step_id": 25,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/scripts/step25_weighted_curvature_identity_test.py",
    "Sessions/S0910A02/workspace/data/step25_weighted_curvature_identity_test.json",
    "Sessions/S0910A02/workspace/notes/step20_global_build_break_analysis.md",
    "Sessions/S0910A02/workspace/notes/step14_faberkrahn_reduced_system_and_fork.md"
  ]
}
```

## Task

Independently check a claimed correction in a toric reduced-Einstein computation for Yau Problem 26. Context: a twist-free diagonal T^2-invariant Einstein 4-metric g = g_B + p^2 dtheta^2 + q^2 dphi^2 over a 2D orbit space Omega (a polygon), with w = pq, v = log(p/q). The verified reduced equations are: (1) -Delta_B w = 2w with w=0 on dOmega (Einstein lambda=1); the individual warping equations -Delta_B p=(K_B-1)p, -Delta_B q=(K_B-1)q, and <grad p, grad q> = -K_B w. On each rod (boundary segment) the collapsing fiber vanishes at unit slope and the surviving fiber Q(s) satisfies Q''+(1-2K_edge)Q=0 with Q'(0)=1,Q'(L)=-1, giving the exact rod identity int_rod (1-2K_edge)Q ds = 2, i.e. flux Phi_i = int Q ds = 2 + 2 int_rod K_edge Q ds.

CLAIM 1 TO CHECK: A prior note (Step 20) recorded an interior identity 'int_Omega K_B w = int_Omega w'. I now claim this clean interior identity is FALSE because the Green's-identity derivation drops boundary/corner terms. My evidence: for the exact product S^2 x S^2, Omega = [0,pi]^2 flat (K_B=0 in interior), w = sin x sin y, so int_Omega K_B w = 0 but int_Omega w = 4, a contradiction. Is my reasoning correct that the clean interior weighted-curvature identity does not hold, and that the only rigorous boundary-anchored constraints are (a) total flux = 2 int w and (b) the per-rod identity int(1-2K_edge)Q=2? Or is there a correct corner/edge-corrected version of int K_B w = int w that I am missing (e.g. with explicit corner delta-curvature terms), and if so what is it exactly?

CLAIM 2 TO CHECK: For a single rod with constant edge curvature K_edge = -A (A>0), Q = sin(sqrt(1+2A) s)/sqrt(1+2A), L = pi/sqrt(1+2A). I compute the Q-weighted negative-curvature charge G_i := int_rod (-K_edge) Q ds = int_0^L A Q ds = 2A/(2A+1), which tends to 1 as A -> infinity, and Phi_i = 2/(2A+1) = 2 - 2 G_i, tending to 0. Verify these two integrals and the relation Phi_i = 2 - 2 G_i exactly. Confirm or refute that a single constant-curvature rod can drive its flux to 0 while its Q-weighted negative charge G_i saturates at 1.

Do the exact integral algebra yourself. State whether each claim holds, and flag any sign or boundary-term error. Do not invent external literature; reason only from the stated equations.

## Output

## Verification memo: sign of the warping equation, and the two identities

I redid the exact algebra from the stated equations. Bottom line up front: **Claim 1's conclusion is right but its stated mechanism is wrong**, and **Claim 2 is exactly correct** — the "reconcile/FAILS" worry in the script prose is a copying slip, not a real discrepancy. Both issues trace to a single controllable source: a sign in the individual warping equation.

---

### The pivotal object: the individual warping equation has a flipped sign

The scripts use

$$-\Delta_B p=(K_B-1)p,\qquad -\Delta_B q=(K_B-1)q .$$

Derive it instead from the two equations you actually trust. The fiber-direction Einstein equation for $g=g_B+p^2d\theta^2+q^2d\phi^2$ with $\lambda=1$ is

$$-\frac{\Delta_B p}{p}-\frac{\langle\nabla p,\nabla q\rangle}{pq}=1 .$$

(Check on a single round $S^2$: $f=\sin x$, $-\Delta\log f-|\nabla\log f|^2=\csc^2x-\cot^2x=1$, and $-\Delta_B f/f$ reproduces this.) Substituting the relation you list, $\langle\nabla p,\nabla q\rangle=-K_B\,pq$, gives

$$-\frac{\Delta_B p}{p}+K_B=1\;\Longrightarrow\;\boxed{-\Delta_B p=(1-K_B)\,p}.$$

So the correct coefficient is $(1-K_B)$, not $(K_B-1)$.

Two independent consistency tests confirm this:

- **$S^2\times S^2$ direct test.** $p=\sin x$, $K_B=0$: $-\Delta_B p=\sin x=+p$. The equation $-\Delta_B p=(1-K_B)p=p$ holds; the printed $(K_B-1)p=-p$ does not.
- **Consistency with your equation (1).** With $-\Delta_B p=(1-K_B)p$ and $\langle\nabla p,\nabla q\rangle=-K_Bw$,
$$\Delta_B w=q\Delta_Bp+p\Delta_Bq+2\langle\nabla p,\nabla q\rangle=-2(1-K_B)w-2K_Bw=-2w,$$
i.e. $-\Delta_B w=2w$ **identically**. With the printed sign one instead gets $-\Delta_B w=(2-4K_B)w$, which contradicts equation (1) whenever $K_B\neq0$. The $S^2\times S^2$ anchor passed only because $K_B=0$ there makes both signs coincide — the error is invisible on that one anchor.

The $K_B=\tfrac14(|\nabla v|^2-|\nabla\log w|^2)$ relation (eq 4) is unaffected and checks out ($\tfrac14(|\nabla v|^2-|\nabla\log w|^2)=-\langle\nabla\log p,\nabla\log q\rangle=K_B$). The sign slip is localized to the individual-warping statement used in the Step 25 Part A derivation.

---

### Claim 1: the interior identity $\int K_B w=\int w$ — conclusion correct, reason not

Redo the Green computation with the **correct** sign. Multiply $-\Delta_B p=(1-K_B)p$ by $q$ and integrate:

$$\int_\Omega \langle\nabla p,\nabla q\rangle-\int_{\partial\Omega}q\,\partial_\nu p=\int_\Omega(1-K_B)w .$$

Insert $\langle\nabla p,\nabla q\rangle=-K_B w$ on the left and $\int(1-K_B)w=\int w-\int K_B w$ on the right:

$$-\int_\Omega K_B w-\int_{\partial\Omega}q\,\partial_\nu p=\int_\Omega w-\int_\Omega K_B w .$$

The two $\int K_B w$ terms **cancel identically**, leaving

$$\Phi_p:=-\int_{\partial\Omega}q\,\partial_\nu p=\int_\Omega w .$$

So the correctly signed derivation never produces $\int K_B w=\int w$; it produces the clean flux-partition statement $\Phi_p=\int w$ (and symmetrically $\Phi_q=\int w$), with **no interior curvature integral surviving at all**. There is therefore no corner-delta-corrected version of "$\int K_B w=\int w$" to recover — the statement was an artifact of the flipped sign, in which the two $K_B w$ terms added instead of cancelling and left a spurious $\int K_B w$.

Consequently:
- Your **final conclusion is correct**: the interior weighted-curvature identity does not hold.
- Your **stated reason is not**: it is not a matter of corner concentration carrying zero $w$-weight, nor of a hidden Hessian structure. The correct account is simply the sign cancellation above. I would drop the Part A′ "corner delta-curvature" narrative and replace it with this two-line derivation.
- The $S^2\times S^2$ arithmetic you cite is fine and instructive: $\int w=4$, $\int K_Bw=0$, so any purported $\int K_Bw=\int w$ is false. But it is not "4≠0 rescued by corners"; it is that the true identity here is $\Phi_p=\int w$. Verify: $p$-rods sit at $x=0,\pi$, surviving fiber $q=\sin y$, so $\Phi_p=2\int_0^\pi\sin y\,dy=4=\int w$. Exact.

**The genuinely valid, $\partial\Omega$-anchored identities are three, not two:**
1. total flux $=-\int_{\partial\Omega}\partial_\nu w=2\int_\Omega w$ (from eq 1);
2. per-rod $\int_{\text{rod}}(1-2K_{\text{edge}})Q\,ds=2$;
3. the partition $\Phi_p=\Phi_q=\int_\Omega w$ (from the corrected Green identity).

Item 3 is a nontrivial statement your note discards; it says the total flux splits equally between the two rod families and each half equals $\int w$. Worth keeping.

Also note item 2 holds for **any** $K_{\text{edge}}(s)$, not only constant: $\int_0^L(1-2K_{\text{edge}})Q\,ds=\int_0^L(-Q'')\,ds=-(Q'(L)-Q'(0))=-(-1-1)=2$, using only $Q'(0)=1,\,Q'(L)=-1$. This robustness is useful and independent of the curvature profile.

---

### Claim 2: single rod with $K_{\text{edge}}=-A$, $A>0$ — exactly correct

With $Q''+(1+2A)Q=0$, $Q(0)=0$, $Q'(0)=1$: $Q=\sin(\omega s)/\omega$, $\omega=\sqrt{1+2A}$, $Q'=\cos(\omega s)$. Closure $Q'(L)=-1$ forces $\omega L=\pi$, so $L=\pi/\sqrt{1+2A}$ and $Q(L)=0$. All consistent.

$$\Phi_i=\int_0^L\frac{\sin(\omega s)}{\omega}\,ds=\frac{1-\cos(\omega L)}{\omega^2}=\frac{1-\cos\pi}{1+2A}=\frac{2}{1+2A}.$$

$$G_i=\int_0^L A\,Q\,ds=A\,\Phi_i=\frac{2A}{1+2A}.$$

Relation:
$$2-2G_i=2-\frac{4A}{1+2A}=\frac{2(1+2A)-4A}{1+2A}=\frac{2}{1+2A}=\Phi_i.\quad\checkmark$$

Limits: $G_i\to1$, $\Phi_i\to0$ as $A\to\infty$. So **yes**, a single rod with constant $K_{\text{edge}}=-A$ drives its flux to $0$ while its $Q$-weighted charge $G_i$ saturates at $1$ (not $1/2$). Claim 2 holds exactly, including the per-rod identity $\int(1-2K_{\text{edge}})Q=(1+2A)\Phi_i=2$.

**The "FAILS numerically / re-derive the sign" panic in `part_B_reconcile` is a copying error, not a real discrepancy.** The prose "$G_i=A/(1+2A)\to1/2$" contradicts the code's own symbolic output $G_i=2A/(2A+1)$. The nonzero "difference $=2A/(2A+1)$" is exactly what you get by feeding the wrong $G_i=A/(1+2A)$ into $2-2G_i-\Phi_i$; with the correct $G_i=2A/(1+2A)$ the difference is $0$, and the code's `check_Phi=2-2G` already reports `0`. Nothing needs re-deriving; the hand-written commentary should simply be corrected to $G_i=2A/(1+2A)$.

---

### What this does and does not settle for the larger question

The single-rod result is consistent with the Step 14 §8 uniform-$K$ stabilization arithmetic: taking $-K_{\text{edge}}=A\sim\pi\chi/(2\,\mathrm{Area})\to\infty$ gives each $G_i\to1$, $\Phi_i\sim 2\,\mathrm{Area}/(\pi\chi)\to0$, and $\chi$ rods multiply back to a finite total $\sim2\,\mathrm{Area}/\pi$. So the per-rod computation neither forces total flux to zero nor pins it above zero on its own; it supplies the correct building block, and the open question remains whether the traceless equation (eq 3) plus equal-partition ($\Phi_p=\Phi_q=\int w$) permit the strongly non-uniform edge-curvature profile a genuine collapse would need. That coupling is not decided by anything in these three files.

One propagation point to check downstream: since the individual warping sign was flipped, any earlier step that used $-\Delta_B p=(K_B-1)p$ (rather than eq 1 or eq 4 directly) should be re-inspected. Equations (1) and (4), the rod ODE, and the $\Phi=2\int w$ identity are all sign-correct as written; the corrected partition identity $\Phi_p=\Phi_q=\int w$ is the one new consequence to fold in.