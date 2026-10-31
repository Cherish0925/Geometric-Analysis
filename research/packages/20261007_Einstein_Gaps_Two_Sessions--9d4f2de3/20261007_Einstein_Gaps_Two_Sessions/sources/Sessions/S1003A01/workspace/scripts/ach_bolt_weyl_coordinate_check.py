"""Independent JAX coordinate-curvature limit for the validated ACH bolt 2-jet."""
import sys
from pathlib import Path
import jax,jax.numpy as jnp
jax.config.update('jax_enable_x64',True)
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'Sessions/S1003A02/workspace/scripts'))
from o11_rotated_cell import metric_from,curvature_scalars,ANG
b=4/5; A2=49/20; B2=49/20; C3=-25/24
for t in [1e-2,5e-3,2e-3,1e-3]:
 x=t*t
 # radial coordinate x=t^2, so dx^2/(4x)=dt^2
 prof=lambda xx:(xx,jnp.diag(jnp.array([(b+A2*xx)**2,(b+B2*xx)**2,xx*(1+C3*xx)**2])))
 vals=curvature_scalars(metric_from(prof),jnp.concatenate([jnp.array([x]),ANG]))
 print(t,[float(q) for q in vals])
