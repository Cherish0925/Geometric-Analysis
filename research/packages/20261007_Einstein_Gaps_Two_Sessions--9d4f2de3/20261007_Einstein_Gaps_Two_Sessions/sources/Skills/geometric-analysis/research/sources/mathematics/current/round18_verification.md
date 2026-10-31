# Round 18: proof review and reproduction

## Files and baseline

The working baseline is local commit **241afd8**, containing Round 17.
This round adds four mathematical notes, four corresponding checks,
and [the synthesis](round18.md). Inherited proofs are unchanged.

| Note | Mathematical review | Finite check groups |
| --- | --- | ---: |
| [Actual monopole intersections](round18_periods.md) | Root review of normalization, common-line estimates, covariance and min--max; independent global-line review, including the actual Bauer--Furuta application | 13 |
| [Finite-monodromy operator](round18_twisted_operator.md) | Root review of all tensor sectors and descent; independent integral-line review of the full nonlinear slice argument | 12 |
| [Positive-object geometry](round18_positive.md) | Root review of topology and discriminant argument; independent construction-line review, including the conformally-Kähler exception | 6 |
| [Unrestricted integral counterexample](round18_integral_limits.md) | Independent integral-line review of BCG, all Einstein signs, fixed-piece gluing and uniform injectivity | 4 |

Each note contains its mathematical arguments and primary-source inputs.
The reviews found no concrete invalidating step in these arguments.
They do not establish that equivalent theorems are absent from the
literature.

## Executed checks

All seven programs below were executed in the isolated Round-18
worktree on 22 September 2026 with Python 3.12.13, SymPy 1.14.0,
and mpmath 1.3.0. Each returned exit status zero with no stderr.

| Program | Groups | Result |
| --- | ---: | --- |
| [round17_integral_check.py](round17_integral_check.py) | 10 | pass |
| [round17_product_operator_check.py](round17_product_operator_check.py) | 10 | pass |
| [round17_positive_check.py](round17_positive_check.py) | 9 | pass |
| [round18_periods_check.py](round18_periods_check.py) | 13 | pass |
| [round18_twisted_operator_check.py](round18_twisted_operator_check.py) | 12 | pass |
| [round18_positive_check.py](round18_positive_check.py) | 6 | pass |
| [round18_integral_limits_check.py](round18_integral_limits_check.py) | 4 | pass |

This is **35 new groups and 29 inherited regression groups**.
The scripts check exact finite identities, constants, matrix
interpretations, scaling, parity and specified incorrect variants.
The collar-capacity check additionally compares an explicitly derived
integral asymptotic. No program certifies an infinite-dimensional
implicit-function theorem, monopole existence, or all smooth topology.
Those parts are proved or cited in the notes.

From this directory, each program runs with a Python interpreter
providing SymPy and mpmath; for example:

~~~bash
python3 round18_periods_check.py
python3 round18_twisted_operator_check.py
python3 round18_positive_check.py
python3 round18_integral_limits_check.py
~~~

The actual interpreter used here was
/data/qiushi/qiushi_engine_v09/.venv/bin/python.
No dependencies were installed or changed.

## Review corrections incorporated

The nonlinear quotient conclusion is phrased in a local Bianchi
slice, modulo sufficiently small diffeomorphisms; it does not
presume a global moduli-space quotient is a smooth manifold.
The thin-limit statement distinguishes the diverging transverse
\(L^2\) inverse from an unproved uniform Hölder assertion.

For the positive object, absence of a global almost complex
structure is not used to extend a singular eigenline. Derdziński's
nowhere-zero alternative supplies the missing step. The negative
self-dual branch remains possible for merely Hermitian patches;
the separate Killing-field argument excludes conformally-Kähler
patches there. The spectral defect set is not claimed to be a
smooth canonical surface.

In the integral dilution checker, the fixed volume offset is allowed
either sign. Only the actual positive total volumes are used.
Growing cover degree and varying topology are explicit throughout.

## Literature comparison

The actual connected-sum monopoles and the scale-critical energy
construction are classical inputs from
[Ishida--LeBrun](https://arxiv.org/pdf/math/0111228).
Their energy-minimizing degeneration picture is not counted as a
new discovery. The present deduction controls the multiplicity of
small *scalar* eigenvalues for every sequence satisfying the stated
energy and actual-class conditions, without prescribing its necks.

A bounded search also located
[Lin--Lipnowski, Seiberg--Witten equations and the length spectrum of hyperbolic three-manifolds](https://archive.ymsc.tsinghua.edu.cn/pacm_download/21/11996-S0894-0347-2021-00982-7.pdf).
Its monopole/spectral mechanism concerns coexact one-forms in
dimension three, rather than the four-dimensional intersection
covariance and scalar-eigenvalue multiplicity here. This is a useful
comparison, not an exhaustive novelty review.

Classical product spectra, integrable Einstein deformations,
Goldberg--Sachs/Derdziński structure, Killing-field extension,
and entropy-volume comparison are credited where used.
No journal prediction or claim of a solved Yau26 branch follows
from the calculations or reviews.

## Operational scope

All changes are new research files in an isolated local Git worktree.
No live service, existing Session, model configuration, installed
Skill, shared runtime dependency, or external repository was changed.
