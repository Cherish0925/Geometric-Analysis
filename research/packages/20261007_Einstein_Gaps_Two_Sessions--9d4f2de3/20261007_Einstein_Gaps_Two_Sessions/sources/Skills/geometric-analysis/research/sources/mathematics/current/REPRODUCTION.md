# Reproducing the finite calculations

The original twelve-round tree contains 57 Python calculation programs.
They use the standard library and SymPy; mpmath is a SymPy dependency.
The accompanying fresh run uses Python 3.12.13, SymPy 1.14.0 and mpmath 1.3.0.
No GPU, external API, old Session directory or network download is used by
these calculations.

On 21 September 2026 all 57 programs completed with exit status zero under
the limits below. The stored logs contain their actual outputs, including
the original assertions and wrong-formula checks. No source calculation
was changed to obtain this result.

From the extracted package root, in an environment with these dependencies:

```sh
python reproduction/rerun.py --proof-dir proofs --output my-check-results --jobs 2
```

For one formula, use its corresponding script directly, for example:

```sh
python proofs/round10_kottler_coordinate_check.py
python proofs/round11_closed_gluing_check.py
python proofs/round12_repair_check.py
```

The runner creates a new output directory and refuses to overwrite one.
It runs at most two calculations at once, caps each at 120 wall/CPU seconds
and 4 GiB address space, and records stdout, stderr, exit status, runtime,
environment versions and the script hash. Timeouts and failed assertions
remain failures; they are not converted to positive mathematical results.

The current execution summary and individual logs are under
`reproduction/results/`. Historical verification notes remain with the
proofs and are distinguishable from this fresh run.

## What is checked

* Exact polynomial, Clifford, Gram-matrix, scaling and integral identities.
* Specific coordinate Christoffel/Ricci calculations, including mixed blocks.
* Finite integer presentations, Smith normal forms and stated Betti numbers.
* Model coefficients and deliberately incorrect formula variants where
  the original program includes them.

Some older programs also print numerical evaluations or optimized algebraic
bounds. Completing their execution does not turn sampling into a strict
continuous supremum certificate. Nor do finite programs establish weighted
inverse estimates, existence of nonlinear solutions, Seiberg–Witten inputs,
topological classification, analytic continuation or literature priority.
Those arguments and their assumptions are in the linked mathematical notes.

## Original scripts and later conclusions

The programs are preserved without altering their mathematical inputs.
An early script may test an intermediate result that was later strengthened;
its output should be read with the current thematic chapter. This rerun
does not execute the separate, much larger historical program appendix in
the inherited Skill snapshot.
