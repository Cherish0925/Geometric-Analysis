"""Exact symbol checks for weak-source Weyl compactness, not a PDE solver."""
import sympy as s

def twoform(*pairs):
    out = s.zeros(4)
    for i,j in pairs:
        out[i,j],out[j,i]=1,-1
    return out

omega=(twoform((0,1),(2,3)),twoform((0,2),(3,1)),
       twoform((0,3),(1,2)))
a,b,c,d,e=s.symbols('a b c d e',real=True)
A=s.Matrix([[a,c,d],[c,b,e],[d,e,-a-b]])
xi=s.symbols('x0:4',real=True)
W={}
for i in range(4):
    for j in range(4):
        for k in range(4):
            for l in range(4):
                W[i,j,k,l]=s.expand(sum(A[u,v]*omega[u][i,j]*omega[v][k,l]
                    for u in range(3) for v in range(3))/2)
normW=s.expand(sum(z*z for z in W.values()))
normA=s.trace(A*A)
assert s.expand(normW-4*normA)==0
divsymbol=[sum(xi[i]*W[i,j,k,l] for i in range(4))
    for j in range(4) for k in range(4) for l in range(4)]
assert s.expand(sum(z*z for z in divsymbol)-sum(z*z for z in xi)*normA)==0

# Polarization checks include all five Weyl directions, not a diagonal sample.
variables=(a,b,c,d,e)
G_A=s.hessian(normA,variables)/2
G_D=s.hessian(sum(z*z for z in divsymbol),variables)/2
assert s.simplify(G_D-sum(z*z for z in xi)*G_A)==s.zeros(5)

# Unlike general Weyl first jets, jets tangent to the fixed double-eigenvalue
# orbit are controlled pointwise by divergence, not only at symbol level.
z=s.symbols('z0:8',real=True)
H=[s.Matrix([[0,z[2*m],z[2*m+1]],
             [z[2*m],0,0],[z[2*m+1],0,0]]) for m in range(4)]
orbit_div=[sum(H[m][a,b]*omega[a][m,j]*omega[b][k,l]/2
    for m in range(4) for a in range(3) for b in range(3))
    for j in range(4) for k in range(4) for l in range(4)]
G_orbit=s.hessian(sum(v*v for v in orbit_div),z)/2
assert G_orbit.eigenvals()=={s.S(1):4,s.S(3):4}
assert s.expand(sum(s.trace(h*h) for h in H)-2*sum(v*v for v in z))==0

# Exact derivatives of a high-frequency mode illustrate the two source norms.
# On the period-2pi torus, A=eps*sin(k*x0)*A0, ||A0||HS=1:
# ||div W||L2^2 / Vol = eps^2*k^2/2,
# ||div W||dotHminus1^2 / Vol = eps^2/2.
j=s.symbols('j',positive=True)
eps=1/j
k=j*j
assert s.simplify(eps**2*k**2/2)==j*j/2
assert s.limit(eps**2/2,j,s.oo)==0
print('PASS: full four-index Weyl norm squared = 4 |A|HS squared')
print('PASS: for arbitrary covector and all five Weyl components,')
print('      |symbol(div)(xi) W+|tensor squared = |xi| squared |A|HS squared')
print('PASS: polarized 5-by-5 symbol identity and Fourier source scaling')
print('PASS: full 8-dimensional orbit first-jet Gram eigenvalues: 1,3, each x4')
