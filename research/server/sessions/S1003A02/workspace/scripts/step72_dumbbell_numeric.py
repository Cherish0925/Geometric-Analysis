#!/usr/bin/env python3
"""Numerical check of the smooth warped S^4 dumbbell used in Theorem 71.D'.

Metric: dr^2 + f(r)^2 g_{S^3(1)}.  Two fixed smooth caps are joined by
a cylinder f=1 of length L.  The cap is sin(r) near its pole and is
blended C^2 to f=1 on [a,b].  We integrate V, total scalar, S, R, P and E.
"""
import json
import math
from pathlib import Path
from scipy.integrate import quad

PI = math.pi
VOL_S3 = 2*PI**2
a = PI/3
b = PI/2
h = b-a


def smoothstep(u):
    return 10*u**3 - 15*u**4 + 6*u**5

def smoothstep1(u):
    return 30*u**2 - 60*u**3 + 30*u**4

def smoothstep2(u):
    return 60*u - 180*u**2 + 120*u**3


def left_cap(r):
    """Return f,f',f'' on [0,b]."""
    if r <= a:
        return math.sin(r), math.cos(r), -math.sin(r)
    u=(r-a)/h
    w=smoothstep(u)
    wp=smoothstep1(u)/h
    wpp=smoothstep2(u)/h**2
    s=math.sin(r); c=math.cos(r)
    f=(1-w)*s+w
    fp=(1-w)*c+wp*(1-s)
    fpp=-(1-w)*s-2*wp*c+wpp*(1-s)
    return f,fp,fpp


def local_quantities(r):
    f,fp,fpp=left_cap(r)
    if r < 1e-7:
        k0=k1=1.0
    else:
        k0=-fpp/f
        k1=(1-fp*fp)/(f*f)
    ric0=3*k0
    ricT=k0+2*k1
    scal=6*(k0+k1)
    ric2=ric0*ric0+3*ricT*ricT
    p=ric2-scal*scal/4
    dv=VOL_S3*f**3
    return dv, scal*dv, scal*scal*dv, ric2*dv, p*dv

# one cap; quad split at blend start

def cap_integral(i):
    fn=lambda r: local_quantities(r)[i]
    return quad(fn,0,a,epsabs=1e-11,epsrel=1e-11,limit=300)[0]+quad(fn,a,b,epsabs=1e-11,epsrel=1e-11,limit=300)[0]

caps=[2*cap_integral(i) for i in range(5)]
# cylinder per unit length: V=2pi^2, s=6, S=72pi^2, R=24pi^2, P=6pi^2
cyl=[2*PI**2,12*PI**2,72*PI**2,24*PI**2,6*PI**2]

rows=[]
for L in [1,2,5,10,20,50,100,200]:
    V,T,S,R,P=[caps[i]+L*cyl[i] for i in range(5)]
    Ls=S-T*T/V
    E=(4*P+Ls)/R
    rows.append({
        "L":L,"V":V,"T_scalar":T,"S":S,"R":R,"P":P,
        "L_s":Ls,"E":E,"L_times_E_minus_1":L*(E-1),
        "GB_residual_chi2":(0 + S/24-P/2)-16*PI**2,
        "P_over_L":P/L,"R_over_L":R/L,
    })

out={
    "construction":{"a":a,"b":b,"blend":"quintic C2","W":"identically zero for warped space-form fibers"},
    "two_cap_integrals":{"V":caps[0],"T_scalar":caps[1],"S":caps[2],"R":caps[3],"P":caps[4]},
    "cylinder_per_length":{"V":cyl[0],"T_scalar":cyl[1],"S":cyl[2],"R":cyl[3],"P":cyl[4]},
    "rows":rows,
}
out_path=Path(__file__).resolve().parents[1]/"data"/"step72_dumbbell_numeric.json"
out_path.write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
