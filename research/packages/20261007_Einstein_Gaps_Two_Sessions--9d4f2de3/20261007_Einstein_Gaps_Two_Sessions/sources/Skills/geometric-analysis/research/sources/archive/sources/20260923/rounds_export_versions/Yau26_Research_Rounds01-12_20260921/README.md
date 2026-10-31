# Yau 26: twelve rounds of mathematical research

## The mathematical position

The research has produced three connected developments beyond the earlier
Skill: an intrinsic integral Ricci-defect obstruction in specified monopole
families; new complete and closed near-Einstein constructions; and global
constraints on exact Einstein metrics on the actual constructed objects.
The complete Yau26 problem and both unrestricted four-dimensional sign
branches remain open in this work.

Read the [integrated synthesis](research/SYNTHESIS.md) for the conclusions and their
connections. The three chapters below give a continuous mathematical account;
the linked proof notes retain the detailed arguments rather than replacing
them with these chapters.

Each chapter is supplied in readable Markdown and a corresponding standalone
LaTeX source. No PDF is required. The LaTeX versions carry the same mathematics;
they are not additional results or substitute proofs.

| Chapter | Central question | Principal increment beyond the baseline |
| --- | --- | --- |
| [I. Intrinsic rigidity](research/01_rigidity.md) | Can critical monopole topology support arbitrarily small Einstein defect? | A normalized integral gap without diameter, noncollapse or full-curvature assumptions in its stated class |
| [II. Constructions and repair](research/02_constructions.md) | Which fixed smooth objects admit small residual, and at what cost can it be corrected? | Complete exact models, quantitative repair obstructions, approximate double ends, and closed sheared assemblies beyond surface bundles |
| [III. Global Einstein geometry](research/03_global.md) | What can every exact output on those same objects look like? | Exact free-circle end exclusion, actual topology and basic classes, and compulsory breaking of all continuous local symmetry |

The original exact topology gap, log-Weyl construction, and Dehn-twist bundle
construction are inherited inputs. They are not counted as new discoveries
in these twelve rounds. “New” here describes the change from that baseline;
worldwide publication priority requires comparison with the literature.

## The original problem and the scale of the results

For each dimension, the working problem asks whether a dimension-only
interval of pointwise Ricci bounds forces a closed smooth manifold to admit
some Einstein metric. The output is on the same smooth manifold; its sign,
symmetry and distance from the input are unrestricted. Write
\[
\delta_\sigma(g)=\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{L^\infty,\mathrm{op}},
\qquad e_\sigma(M)=\inf_g\delta_\sigma(g),\quad \sigma=\pm1.
\]
Vanishing defect on a manifold without any Einstein metric defeats one
normalized branch. Defeating both signs in one fixed dimension disproves the
working interval statement; the two signs may use different manifolds. An
affirmative answer requires coverage of every dimension, with a uniform
threshold over the permitted manifolds in each dimension.

The work is predominantly four-dimensional. A complete noncompact model,
a failure of symmetric repair, and a closed all-Einstein obstruction are
different results. Each chapter keeps its manifold, norm and quantifiers
explicit.

## What the three lines reveal together

### 1. A route past one genuine compactness obstacle

The earlier rigidity approach needed a controlled local limit. The new
monopole argument instead builds a bounded spinorial model for self-dual
Weyl curvature, differentiates that model intrinsically, and uses it as a
test in weak Bianchi. The contradiction is obtained on the original closed
metrics. Collapse and uncontrolled anti-self-dual Weyl curvature therefore
do not automatically destroy this particular argument.

For the stated blow-up family, with \(A=c_1^2(X)>0\), the resulting statement is
\[
\mathcal E(g)+(1/3-k/A)_+\ge c_*>0,\qquad
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int|\operatorname{Ric}_g-\lambda g|^2}{\lambda^2\operatorname{Vol}_g M}.
\]
The proof's decisive resource is the actual monopole solution, not a generic
regularity theorem for arbitrary small Ricci residual. Its extension to
special monopole classes spells out the required square and minimax conditions.

### 2. Integral topology can have vanishing pointwise Ricci cost

The closed sheared construction handles two different geometric changes in
two regions. A long collar spreads a fixed mapping-class deformation; a
small circle makes the metric contribution of an integral connection shear
small. Keeping these regions separate controls every Ricci block without
changing the closed smooth manifold. The result includes examples outside
the class of oriented surface bundles and without a Kähler finite cover.

This is more directly relevant to Yau26 than merely improving the convergence
rate on an old input family. The remaining question is whether one of these
specific smooth manifolds admits a nonsymmetric negative Einstein metric.

### 3. Exact rigidity and arbitrarily accurate approximation can coexist

A free-circle reduction excludes exact two-ended smoothly conformally compact
Einstein connectors in its class. Yet explicit degenerating complete metrics
with two ends have Ricci defect tending to zero, even with fixed circle period
and fixed conformal boundary. The precise two-ended example is noncompact,
so it is not itself a counterexample to the closed problem.

The same distinction matters for the closed inputs. Their topology excludes
all local Killing fields for a hypothetical Einstein metric, but an
approximation can have symmetric regions. The unresolved issue is the full
nonsymmetric equation, not another symmetric ansatz.

### 4. The two strongest sides cannot simply be pasted together

The new closed sheared examples \(M(h,g;u,f)\) have monopole ratio
\(T/\alpha^2=1\), whereas
the intrinsic contradiction concerns approach to \(2/3\). The permitted
negative locally symmetric fillings also stay away from that critical ratio
under the stated energy-concentration hypotheses. Thus the existing
construction and existing gap do not already provide a hidden counterexample.

Likewise, nonattainment of scalar or Ricci-energy extrema does not prove
nonattainment of the full-curvature minimum. On the new examples, that last
attainment question remains equivalent to Einstein existence.

## Reading the proof library

The research is organized by mathematics first, not by the number of rounds.
Use the round notes to recover how a mechanism developed, including failed
arguments and estimates that were later strengthened.

| Rounds | Development | Original accounts |
| --- | --- | --- |
| 1–2 | Explicit spectral and curvature estimates; weak transfer; full kernel and quadratic corrections; twisted transport | [1](proofs/README.md), [2](proofs/round2.md) |
| 3–4 | Intrinsic monopole closure and integral formulation; nonlinear complete models and exact charge | [3](proofs/round3.md), [4](proofs/round4.md) |
| 5–6 | Special-monopole scope; whole-fibre repair estimates; linear-radius exclusion; concrete topology and one-ended models | [5](proofs/round5.md), [6](proofs/round6.md) |
| 7–8 | Concentration compatibility; spectral, representation, boundary and gauge constraints | [7](proofs/round7.md), [8](proofs/round8.md) |
| 9–10 | Exact end exclusion versus explicit approximate double ends; harmonic and gauge control examples | [9](proofs/round9.md), [10](proofs/round10.md) |
| 11–12 | New closed sheared inputs; global invariants and ordinary basic classes; symmetry breaking and repair constraints | [11](proofs/round11.md), [12](proofs/round12.md) |

Historical “next question” paragraphs are dated research states. In particular,
the curvature-bound requirement in the early monopole argument and the
early exact free-torus continuation problem were subsequently superseded.
The relevant current conclusions and retained intermediate estimates are
identified in the three chapters. The inherited charged Koiso germ already
existed in the baseline; its later explicit rederivation is not a second
existence theorem.

## Calculations and inherited inputs

The package keeps the original proof notes and finite calculation scripts,
with fresh execution logs in the [reproduction record](reproduction/README.md).
Scripts can be run with an ordinary Python environment; neither old Sessions
nor the Qiushi command wrapper is needed. Their exact algebra and coordinate
checks support specified portions of the arguments. They do not mechanically
verify the analytic estimates, gauge theory, or global topology.

The [baseline manuscripts](baseline/research/20260916.md) and their supporting
Skill files are included as a fixed research snapshot. This avoids requiring
access to the installed Skill or the old Sessions to read inherited derivations.
The baseline is historical input, not an instruction to undo later results.
External classical theorems retain their original citations; a research package
is not a replacement for their published proofs.

The [rigidity](coverage/01_rigidity_coverage.tsv),
[construction](coverage/02_constructions_coverage.tsv), and
[global](coverage/03_global_coverage.tsv) coverage tables locate source sections
in the chapters. The inventory also records every original tracked file, including reviews and verification
notes. This is an explicit preservation boundary: all files in the twelve-round
research tree at commit `50c29cd`, plus the included baseline snapshot and the
new thematic exposition. It does not claim to contain every original chat,
private tool event or unpublished file outside that tree.

## The next decisive mathematical question

The most developed new closed candidates are the sheared manifolds
\(M(h,g;u,f)\), with \(h\ge1\), \(g\ge2\), and nonzero integral shear.
They have actual small-defect metrics. Ordinary basic classes and several
sharp global invariants are now known; an Einstein output, if it exists,
must be negative, non-Kähler and have no nonzero local Killing germ.

A new unrestricted existence or nonexistence argument on one of these
manifolds would change the position on the negative branch. The package
keeps the other constructions and rigidity mechanisms available rather
than treating this choice as compulsory. No current result settles the
positive branch or provides a full all-dimensional existence mechanism.
