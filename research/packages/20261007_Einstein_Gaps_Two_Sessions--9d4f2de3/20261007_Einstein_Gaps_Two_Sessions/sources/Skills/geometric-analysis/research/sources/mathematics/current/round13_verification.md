# Round 13 verification

Run from this directory, using the existing v09 research interpreter:

```bash
/data/qiushi/qiushi_engine_v09/.venv/bin/python round13_averaging_check.py
/data/qiushi/qiushi_engine_v09/.venv/bin/python round13_radius_check.py
/data/qiushi/qiushi_engine_v09/.venv/bin/python round13_global_check.py
/data/qiushi/qiushi_engine_v09/.venv/bin/python round13_neck_kernel_check.py
```

All four commands returned exit code zero in the final root-agent run.

| Program | Actual check |
| --- | --- |
| Averaging | Coordinate Christoffel/Ricci derivation; averaged transverse Ricci equals \(-\eta^2a^2\); circle and off-diagonal averages vanish; exact frequency scaling |
| Optical receiver | Five exact rational metric-jet tests with spatial radius and both connection-curvature components |
| Global | Eight algebraic checks of volume normalization, first-variation factor, determinant exponent, and Newton inequalities |
| Neck | Product curvature derivative, trace/divergence, finite-parameter waist calculation, and exact shear-residual pairing; wrong \(\operatorname{sech}\) profile fails |

For the optical tests, the independently computed values of \(D\) were
\(276738103,400408903,642562903,1003200103,1482320503\), all divided
by \(1451419200\); each matched the geometric receiver exactly.

Written proof review additionally checked points not certified by these
programs:

- the selected polarized spin-c structure persists for every conformal
  weight, and the connected-sum insertions preserve nonvanishing;
- the circle tensor bounds use covariant derivatives and Killing
  identities, not coordinate derivatives with missing radius factors;
- optical lapse cancellation does not assert a global foliation exists;
- continuous Newton roots must realize a locally continuous family in
  an Einstein-moduli metric topology, not just a weak abstract norm;
- inverse bounds use Hölder spaces, avoiding the false general
  \(C^0\)-to-\(C^2\) elliptic endpoint;
- the full gauged operator is self-adjoint, the collar supports are
  disjoint, and the waist-length functional detects nongauge modes.

The existing twelve-round integral theorem, closed construction, and
non-Kähler equality obstruction are referenced premises. This round
does not rerun their entire proof archive or replace originality
comparison with program success. No live service, Session, installed
Skill, model profile, or GPU allocation was changed.
