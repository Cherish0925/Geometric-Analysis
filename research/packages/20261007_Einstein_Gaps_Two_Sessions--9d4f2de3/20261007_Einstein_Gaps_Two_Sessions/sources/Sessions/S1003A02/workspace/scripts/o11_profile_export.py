"""Export optimized o11_perp_cell profiles and radial derivatives on a dense grid.

Usage:
  python o11_profile_export.py input.json output.npz output.csv
The input is a JSON optimization output from o11_perp_cell.py containing x0,
degU, degw, wpow, theta, z.  Exported quantities use the x-coordinate metric
  g = dx^2/(4G) + h_ij s^i s^j.
Derivatives are automatic derivatives with respect to x.  The data are intended
for independent Chern--Weil/transgression calculations.
"""
import sys, json
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from o11_perp_cell import PerpCell

inp, outnpz, outcsv = sys.argv[1:4]
o = json.load(open(inp))
x0=float(o['x0']); X=float(o.get('X',1.0)); degU=int(o['degU']); degw=int(o['degw'])
c=PerpCell(x0,X,degU,degw,500)
c.wpow=int(o.get('wpow',1))
theta=float(o.get('theta',np.pi/2)); c.beta0=np.pi/2-theta
z=np.asarray(o['z'],dtype=float)
c.degr=max(0,len(z)-(2*degU+degw)); c.nparam=len(z)
prof=c.prof_factory(jnp.array(z))
dprof=jax.jacfwd(prof); ddprof=jax.jacfwd(dprof)
# include a point very near, but not exactly at, the bolt; exact x0 is also
# exported separately through the limiting profile values.
t=np.linspace(0,1,1601)
x=x0+(X-x0)*t*t
rows=[]
for xx in x:
 G,h=prof(jnp.array(xx)); (Gp,hp)=dprof(jnp.array(xx)); (Gpp,hpp)=ddprof(jnp.array(xx))
 rows.append((float(G),np.array(h),float(Gp),np.array(hp),float(Gpp),np.array(hpp)))
G=np.array([r[0] for r in rows]); h=np.stack([r[1] for r in rows]);
Gp=np.array([r[2] for r in rows]); hp=np.stack([r[3] for r in rows]);
Gpp=np.array([r[4] for r in rows]); hpp=np.stack([r[5] for r in rows])
np.savez_compressed(outnpz,x=x,G=G,h=h,Gp=Gp,hp=hp,Gpp=Gpp,hpp=hpp,
                    x0=x0,X=X,theta=theta,wpow=c.wpow,z=z)
header=['x','G','Gp','Gpp']
cols=[x,G,Gp,Gpp]
for name,a in [('h',h),('hp',hp),('hpp',hpp)]:
 for i in range(3):
  for j in range(i,3):
   header.append(f'{name}{i+1}{j+1}'); cols.append(a[:,i,j])
np.savetxt(outcsv,np.column_stack(cols),delimiter=',',header=','.join(header),comments='')
print(json.dumps(dict(input=inp,npz=outnpz,csv=outcsv,n=len(x),x0=x0,X=X,theta=theta,
                      P=o.get('opt',{}).get('P'),slope=o.get('slope'))))
