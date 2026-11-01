"""
Step 12: exact rectangular/separable sanity check for the toric determinant equation.

For a twist-free T^2 metric over a rectangle with p=0 on vertical edges, q=0 on
horizontal edges and smooth unit closure, the separated first mode is
  p=(Lx/pi) sin(pi x/Lx), q=(Ly/pi) sin(pi y/Ly)
so p_x(0)=1, q_y(0)=1.  The determinant w=pq satisfies -Delta w=lambda w with
lambda=pi^2/Lx^2+pi^2/Ly^2.  Imposing positive Einstein lambda=2 fixes scale.
The 4D volume is (2pi)^2 int w.
"""
import math, json, os

def volume_for_Lx(Lx):
    # lambda condition: pi^2/Lx^2 + pi^2/Ly^2 = 2
    denom = 2 - math.pi**2/Lx**2
    if denom <= 0:
        return None
    Ly = math.pi / math.sqrt(denom)
    intw = 4*Lx**2*Ly**2/math.pi**4
    vol4 = (2*math.pi)**2 * intw
    return {"Lx":Lx,"Ly":Ly,"int_w":intw,"volume4":vol4,"ratio_to_S2xS2":vol4/(16*math.pi**2)}

# admissible Lx > pi/sqrt(2)
Lmin = math.pi/math.sqrt(2)
# sample and numerical minimum
samples=[]
for Lx in [Lmin*1.01, 2.5, math.pi, 4.0, 6.0, 10.0]:
    samples.append(volume_for_Lx(Lx))
# grid min
best=None
for i in range(1,20000):
    Lx=Lmin*(1+1e-5)+i*0.001
    r=volume_for_Lx(Lx)
    if r is None: continue
    if best is None or r["volume4"]<best["volume4"]: best=r

out={
    "lambda_condition":"pi^2/Lx^2 + pi^2/Ly^2 = 2",
    "volume_formula":"Vol4=(2*pi)^2 * 4*Lx^2*Ly^2/pi^4",
    "analytic_minimum":"By AM-GM on u=Lx^2,v=Ly^2 with 1/u+1/v=2/pi^2, uv is minimized at u=v=pi^2; Vol4_min=16*pi^2.",
    "admissible_Lx_lower_bound":Lmin,
    "grid_best":best,
    "samples":samples
}
OUTDIR=os.path.abspath(os.path.join(os.path.dirname(__file__),"..","data")); os.makedirs(OUTDIR,exist_ok=True)
OUT=os.path.join(OUTDIR,"step12_rectangular_toric_volume_gap.json")
with open(OUT,"w") as f: json.dump(out,f,indent=2)
print(json.dumps(out,indent=2))
print("Saved",OUT)
