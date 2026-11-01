"""
SUPERSEDED Step50 probe.

Do not use the original output from this file. It computed a false determinant
(-1296) by substituting linear-equivalence representatives into the degenerate
full toric divisor pairing. The corrected computation is in:

  Sessions/S0910A02/workspace/scripts/step50_mixed_resolution_lattice_probe.py
  Sessions/S0910A02/workspace/data/step50_mixed_resolution_lattice_probe.json

The corrected Picard matrix is the 6x6 toric divisor submatrix after deleting
two divisors whose rays form a Z-basis; it has determinant -1 and signature
(1,5). Mixed rows still require boundary/Kirby data for exact parity/smooth
classification.
"""
print(__doc__)
