# Sources for the 4 October construction

These are dated copies of research produced by the two owner-authorized
Sessions, retained alongside the mathematical comparison. The source root
was `Sessions/<session>/workspace/` in their shared user workspace.

| Bundled file | Original Session and workspace path |
| --- | --- |
| `step10_rigorous_subthreshold_cell_and_O11.md` | S1003A01: `notes/step10_rigorous_subthreshold_cell_and_O11.md` |
| `step11_independent_review_O11_and_mixed_cost.md` | S1003A01: `notes/step11_independent_review_O11_and_mixed_cost.md` |
| `step11_subthreshold_perpendicular_cell.md` | S1003A02: `notes/step11_subthreshold_perpendicular_cell.md` |
| `perp_rigorous_enclosure.py` | S1003A01: `scripts/perp_rigorous_enclosure.py`, including the Step 11 pure-Arb tail calculation |
| `x0.01_X8_J_d8.json` | S1003A01: `data/perp_collar/x0.01_X8_J_d8.json` |
| `strict_rigorous_x0.01_X8_J_d8.json` | S1003A01: `data/perp_collar/strict_rigorous_x0.01_X8_J_d8.json` |

The S1003A01 Step 11 text supersedes Step 10's proposed isolated
pure-handle improvement and its identification of a single-cell infimum
with the unrestricted global optimum. Pure-handle rigidity does not
imply additivity for mixed cells. These are mathematical scope distinctions,
not a prescribed research program.

The coefficient JSON fixes an exact dyadic profile. Its old optimizer
`P` and `J` fields are approximate metadata; the enclosing balls are in
the strict output. The standalone integration code requires `python-flint`
and can be used from this directory:

```bash
qiushi-geometry env core python perp_rigorous_enclosure.py x0.01_X8_J_d8.json --prec 256 --tol 1e-18
```

The integration checks a specified profile; the notes supply smoothness,
topology, collar replacement, and global transfer. Later Session results
may strengthen these dated statements without changing this source copy.
