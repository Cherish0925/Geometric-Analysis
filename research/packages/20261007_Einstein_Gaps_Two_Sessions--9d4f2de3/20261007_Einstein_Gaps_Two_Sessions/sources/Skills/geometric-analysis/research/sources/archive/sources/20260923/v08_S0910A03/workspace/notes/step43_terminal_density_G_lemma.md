# Step 43: Terminal spectral density $\int G$ via gauge-theoretic chain

## 0. Purpose

Derive the bound $\int G \le 6Q + 48\pi^2(-q)_+$ for the nonneg pointwise
LeBrun spectral density $G = f^2 - (b_-)^2$, using the published
Seiberg–Witten monopole inequality, Chern–Weil identities, pointwise
algebraic identities, and the LeBrun generalized-Yamabe spectral lower bound.  This closes the load-bearing input identified by the
Step 42 TTCS as an imported but unproved lemma.

The result applies to any smooth Riemannian metric on a closed oriented
four-manifold carrying an Ishida–LeBrun monopole family.  In particular
it applies to the evolved terminal metric $g(T)$ of the normalized cutoff
flow, requiring only the global $L^2$ Einstein defect $Q(T) = \int|E(T)|^2$.

## 1. Definitions and pointwise algebra

Let $(M^4,g)$ be closed oriented Riemannian.  Write
$W^+ \colon \Lambda^+ \to \Lambda^+$ for the self-dual Weyl endomorphism,
with ordered eigenvalues $\lambda_1 \ge \lambda_2 \ge w$, trace zero.

Define
\[
  u = |W^+|, \qquad
  \alpha = \sqrt{2/3}, \qquad
  q = \sqrt{6}\,u - s = \sqrt{6}\,|W^+| - s.
\]

**Key scalars:**
\[
  f = \frac{2}{3}s - 2\alpha u = -\frac{2}{3}q,
  \qquad
  b = \frac{2}{3}s + 2w.
\]

**Gap variable:** $\xi = w + \alpha u \ge 0$
(since $w \ge -\alpha u$ for any trace-free symmetric $3\times3$ endomorphism).

Then $b = f + 2\xi$, so $b \ge f$ always.

**Pointwise spectral density:**
\[
  G = f^2 - (b_-)^2
  \qquad \text{where } b_- = \min(b,0).
\]

**Lemma 1.1 (pointwise nonnegativity).**
$G \ge 0$.  Moreover $G = 0$ iff $f = 0$ or ($\xi = 0$ and $f < 0$).
(When $\xi = 0$ and $f > 0$: $b = f > 0$, so $G = f^2 > 0$.
When $\xi = 0$ and $f = 0$: $G = 0$.  When $\xi = 0$ and $f < 0$: $b = f < 0$,
so $G = f^2 - f^2 = 0$.)

*Proof.* When $b \ge 0$: $(b_-)^2 = 0 \le f^2$.
When $b < 0$: $f \le b < 0$, so $|f| \ge |b|$, hence $f^2 \ge b^2 = (b_-)^2$.  $\square$

**Lemma 1.2 (spectral determination).**
If $s = -4$ and $|W^+|^2 = 1/24$, then $G = 0$ implies
\[
  \operatorname{Spec}(W^+) = \bigl(-\tfrac{1}{6},\tfrac{1}{12},\tfrac{1}{12}\bigr).
\]

*Proof.* At these values, $f = -3$ and $\xi \in [0,1/6]$,
so $G = 4\xi(3 - \xi)$.  Since $3 - \xi > 0$, $G = 0$ iff $\xi = 0$ iff
$w = -1/6$.  Then $\lambda_1 + \lambda_2 = 1/6$ and
$\lambda_1^2 + \lambda_2^2 = 1/24 - 1/36 = 1/72$, giving
$(\lambda_1 - \lambda_2)^2 = 0$, so $\lambda_1 = \lambda_2 = 1/12$.
$\square$

## 2. Integral identity

Since $f = -2q/3$:
\[
  \int f^2\,d\mu = \frac{4}{9}\int q^2\,d\mu = \frac{4}{9}E,
  \qquad E := \int(s - \sqrt{6}|W^+|)^2\,d\mu.   \tag{2.1}
\]

The spectral deficit is
\[
  D_{\rm spec} := \int G\,d\mu = \frac{4}{9}E - \int(b_-)^2\,d\mu.
                                                         \tag{2.2}
\]

$D_{\rm spec} \ge 0$ by Lemma 1.1.  The upper bound requires the
gauge-theoretic chain below.

## 3. Gauge-theoretic inputs

Suppose $M = (\#_{j=1}^m X_j)\#N$ carries an Ishida–LeBrun monopole family
with $A = \sum c_1^2(X_j)$, $D = 4m - (2\chi+3\tau)(N)$, and topological excess
$q_{\rm top} = D - A/3$.  By the Hirzebruch formula $(2\chi+3\tau)(X_j) = c_1^2(X_j)$
and the connected-sum formula $(2\chi+3\tau)(M) = \sum(2\chi+3\tau)(X_j) +
(2\chi+3\tau)(N) - 4m = A - D$, so
\[
  T_M := (2\chi+3\tau)(M) = A - D = \frac{2A}{3} - q_{\rm top}.
\]

**Identity (CW).** For any smooth metric on a closed oriented $4$-manifold:
\[
  (2\chi+3\tau)(M) = \frac{1}{4\pi^2}\int\left(
  \frac{s^2}{24} + 2|W^+|^2 - \frac{|\operatorname{Ric}^\circ|^2}{2}
  \right)d\mu
  = S + W - R,                                          \tag{3.1}
\]
where
$S = \frac{1}{4\pi^2}\int\frac{s^2}{24}$,
$W = \frac{1}{4\pi^2}\int 2|W^+|^2$,
$R = \frac{1}{4\pi^2}\int\frac{|\operatorname{Ric}^\circ|^2}{2}
= \frac{1}{8\pi^2}\int|\operatorname{Ric}^\circ|^2$.

**Published SW monopole inequality (LeBrun Prop.~3.8).**
For a monopole class $a$ with self-dual period square $p = (a^+)^2$:
\[
  E = \int(s - \sqrt{6}|W^+|)^2\,d\mu \ge 72\pi^2 p.   \tag{3.2}
\]

**Sign-averaging (Ishida–LeBrun).** There exists a sign choice with
$p \ge A$.  This is topological and holds for any metric on $M$.

**Algebraic identity.** From the pointwise identity
$27(s^2/24 + 2|W^+|^2) - (s - \sqrt{6}|W^+|)^2
= \frac{1}{8}(s + 8\sqrt{6}|W^+|)^2$,
integration gives
\[
  K := \frac{E}{72\pi^2} \le \frac{3}{2}(S + W) = \frac{3}{2}I,
  \qquad I = S + W.                                      \tag{3.3}
\]

## 4. The spectral density bound

**Theorem 4.1.** For any smooth metric $g$ on $M$, with
$E = \operatorname{Ric}_g + g$ and $Q = \int|E|^2\,d\mu_g$:
\[
  \int G\,d\mu_g \le 6Q + 48\pi^2(-q_{\rm top})_+.     \tag{4.1}
\]
If $q_{\rm top} \ge 0$, then $\int G \le 6Q$.

*Proof.*

**Step A: CW and $R \le Q/(8\pi^2)$.**
From $\operatorname{Ric} = E - g$:
$\operatorname{Ric}^\circ = E^\circ$
(the trace-free parts agree because the traces differ by $s + 4$
which is the trace of $E$, and $\operatorname{tr}(\operatorname{Ric})
= s$ while $\operatorname{tr}(E) = s + 4$, but the trace-free parts
are identical: $\operatorname{Ric}^\circ = \operatorname{Ric} - s g/4
= E - g - sg/4 = E - (1+s/4)g$, and $E^\circ = E - (s+4)g/4$.
Since $\operatorname{Ric}^\circ = E^\circ$ (both equal the trace-free
Ricci tensor).  Hence:
\[
  R = \frac{1}{8\pi^2}\int|E^\circ|^2
  \le \frac{1}{8\pi^2}\int|E|^2
  = \frac{Q}{8\pi^2}.                                    \tag{4.2}
\]

**Step B: Scalar–Weyl deficit.**
By (CW): $I = T_M + R = 2A/3 - q_{\rm top} + R$.
By (3.3): $K \le 3I/2 = 3(2A/3 - q_{\rm top} + R)/2 = A - 3q_{\rm top}/2 + 3R/2$.
By sign-averaging: $p \ge A$.  Define
$\Delta_a = E - 72\pi^2 p = 72\pi^2(K - p) \ge 0$ (by (3.2)).
Then
\[
  \Delta_a \le 72\pi^2(K - A)
  \le 72\pi^2\bigl(-\tfrac{3}{2}q_{\rm top} + \tfrac{3}{2}R\bigr)
  = 108\pi^2(R - q_{\rm top}).                           \tag{4.3'}
\]

**Step C: From deficit to spectral density (requires LeBrun spectral lower bound).**
The LeBrun conformal/Yamabe decomposition (Codex eq.~24):
\[
  \frac{4}{9}\Delta_a = D_{\rm spec} + D_{\rm Yam} + D_{\rm mono},
                                                          \tag{4.5'}
\]
with $D_{\rm spec} = \frac{4}{9}\mathcal{E}_{\rm SW} - \int(b_-)^2$
(where $\mathcal{E}_{\rm SW} = \int(s-\sqrt6|W^+|)^2$ is the SW scalar integral), $D_{\rm Yam} \ge 0$
(conformal minimization), $D_{\rm mono} \ge 0$ (monopole at minimizer).
All three nonneg.  Hence
\[
  D_{\rm spec} = \int G \le \frac{4}{9}\Delta_a.         \tag{4.4}
\]

Equivalently, (4.4) is the statement $\int(b_-)^2 \ge 32\pi^2 p \ge 32\pi^2 A$,
which is LeBrun's spectral lower bound (Theorem 2.3 and its generalized
Yamabe extension).  The three nonneg summands in (4.5') are the spectral
deficit $D_{\rm spec}$, the conformal Yamabe deficit $D_{\rm Yam} \ge 0$,
and the monopole deficit at the conformal minimizer $D_{\rm mono} \ge 0$.

**Step D: Final bound.**
From (4.4) and (4.3'):
\[
  \int G \le \frac{4}{9} \cdot 108\pi^2(R - q_{\rm top})
  = 48\pi^2(R - q_{\rm top}).                            \tag{4.5}
\]

If $q_{\rm top} \ge 0$: $\int G \le 48\pi^2 R
\le 48\pi^2 \cdot Q/(8\pi^2) = 6Q$.

If $q_{\rm top} < 0$: $\int G \le 48\pi^2 R + 48\pi^2|q_{\rm top}|
\le 6Q + 48\pi^2(-q_{\rm top})_+$.

In either case:
\[
  \boxed{\int G\,d\mu \le 6Q + 48\pi^2(-q_{\rm top})_+.} \tag{4.9}
\]
$\square$

## 5. The full terminal density

Combined with the other calibration estimates:
\[
  \int|E|^2 = Q,                                        \tag{5.1}
\]
\[
  \int(s+4)^2 \le 4Q,                                   \tag{5.2}
\]

(since $|s+4| = |\operatorname{tr}E| \le 2|E|$ in dimension 4),

\[
  \int(s + 8\sqrt{6}|W^+|)^2
  \le 864\pi^2(R - q_{\rm top})
  \le 108Q + 864\pi^2(-q_{\rm top})_+,                  \tag{5.3}
\]

(from the algebraic identity and the monopole bound,
with $\int t^2 = 864\pi^2 I - 576\pi^2 K
\le 864\pi^2(T_M + R) - 576\pi^2 A
= 864\pi^2(R - q_{\rm top})$).

The total terminal density is
\[
  \mathfrak{D} = |E|^2 + (s+4)^2 + (s + 8\sqrt{6}|W^+|)^2 + G.
                                                          \tag{5.4}
\]

\[
  \boxed{\int\mathfrak{D}
  \le 119Q + 912\pi^2(-q_{\rm top})_+.}                  \tag{5.5}
\]

The coefficient $119 = 1 + 4 + 108 + 6$, and $912 = 864 + 48$.
For near-critical escaping families, $q_{\rm top}/A_i \to 0$
and $Q_i(T)/A_i \to 0$, so $\int\mathfrak{D}_i/A_i \to 0$.

## 6. Applicability to the evolved terminal metric

The entire chain uses only:
- Chern–Gauss–Bonnet and Hirzebruch signature (topological, any metric)
- Algebraic identity (18) (pointwise, any metric)  
- Published SW monopole inequality (any smooth metric on the manifold)
- Sign-averaging of monopole classes (topological)
- LeBrun spectral lower bound / generalized Yamabe (any smooth metric)
- $\operatorname{Ric}^\circ = E^\circ$ (algebra)

None of these requires pointwise Ricci pinching on the full manifold.
In particular, the bound applies to the evolved metric $g(T)$ of the
normalized cutoff flow, using $Q(T) = \int_{g(T)}|E(T)|^2$ measured
at the terminal time.  The flow preserves the smooth closed topology,
so the Ishida–LeBrun monopole classes remain valid.

## 7. Source references

- LeBrun Proposition 3.8: `Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md`
- LeBrun older conformal proof: `Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md`
- Ishida–LeBrun sign classes: `Knowledge/objects/papers/Curvature-Connected-Sums-and-Seiberg-Witten-Theory--7e92a6723434--2ac6d11897c5/object.md`
- Codex quantitative deficit analysis: `Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md`, especially equations (9), (12), (24), (30), (32)
- Step 42 TTCS verifier 2 (spectrum determination): `Sessions/S0910A03/trace/ttcs/results/step42_ttcs01_verifier2_integration.md`
