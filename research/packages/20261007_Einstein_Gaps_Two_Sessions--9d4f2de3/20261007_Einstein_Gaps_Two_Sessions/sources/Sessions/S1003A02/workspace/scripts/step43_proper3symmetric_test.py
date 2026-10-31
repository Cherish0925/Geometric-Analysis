"""Exact curvature/torsion density test on the proper 4D 3-symmetric AK model.

AAD record (their normalization): scalar s=-3/4, conformal scalar kappa=3/4,
Ricci eigenvalues (0,0,-3/8,-3/8), and
kappa-s=(3/2)|nabla Omega|^2.
Compute the Einstein-defect / quartic-torsion ratio.  These are local
homogeneous densities, not a closed-manifold integral theorem.
"""
from pathlib import Path
import sympy as s, json
sc=s.Rational(-3,4)
kappa=s.Rational(3,4)
ric=[s.Rational(0),s.Rational(0),s.Rational(-3,8),s.Rational(-3,8)]
mean=sc/4
ric0=[s.simplify(x-mean) for x in ric]
Pdens=s.simplify(sum(x*x for x in ric0))
tors2=s.simplify(s.Rational(2,3)*(kappa-sc))
tors4=s.simplify(tors2**2)
ratio=s.simplify(Pdens/tors4)
out={
 'scalar':str(sc),'conformal_scalar_kappa':str(kappa),
 'ricci_eigenvalues':[str(x) for x in ric],
 'ricci0_eigenvalues':[str(x) for x in ric0],
 'ricci0_norm_sq_density':str(Pdens),
 'nabla_Omega_norm_sq_density':str(tors2),
 'nabla_Omega_norm_fourth_density':str(tors4),
 'P_over_quartic_torsion_density':str(ratio),
 'interpretation':'Proper 3-symmetric local AK model is strictly non-Kahler with Kähler-type algebraic W+ and J-invariant Ricci. It does not refute a quartic inequality, but any pointwise universal constant is at most 9/64 in these conventions. Noncompact/local: no closed gap follows.'
}
p=Path(__file__).resolve().parents[1]/'data'/'step43_proper3symmetric_test.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
