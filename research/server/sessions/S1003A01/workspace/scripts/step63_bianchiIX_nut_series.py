"""Step 63: regular Bianchi-IX nut series for negative Einstein almost-Kahler germs.

Use u=t^2 and
    a_i=t f_i(u),  H_i=t a_i'/a_i=1+2u f_i'/f_i,
    Z_i=t a_i/(a_j a_k)=f_i/(f_j f_k).
For lambda=-3, the diagonal Einstein equations become analytic at u=0:
    2u H_i' - H_i + H_i sum(H) - 2[Z_i^2-(Z_j-Z_k)^2] - 3u = 0,
with Hamiltonian constraint
    sum_{i<j} H_i H_j + sum Z_i^2 - 2 sum_{i<j} Z_i Z_j - 3u = 0.
A closed invariant self-dual form has squared coefficients X_i=x_i^2 satisfying
    u X_i' = M_i X_i,  M_i=2Z_i-H_j-H_k.
Constant length is sum X_i=1.

The script solves the Einstein nut series recursively in terms of the two
trace-free cubic metric coefficients, propagates X, and prints/factors the
successive constant-length conditions.  This is an exact symbolic test of the
proposed SU(2)-nut realization of an isolated torsion zero.
"""
import sympy as sp
import json, os

u = sp.symbols('u')
lam = sp.Integer(-3)
# trace-free cubic anisotropy: A_i=1/6+d_i, d3=-d1-d2
d1, d2 = sp.symbols('d1 d2', real=True)
d = [d1, d2, -d1-d2]
A = [sp.Rational(1,6)+z for z in d]


def trunc(e, n):
    return sp.series(sp.cancel(e), u, 0, n+1).removeO().expand()


def build_f(order, coeffs):
    return [1 + sum(coeffs[k][i]*u**k for k in range(1, order+1)) for i in range(3)]


def geometry(f, order):
    H = [trunc(1 + 2*u*sp.diff(fi,u)/fi, order) for fi in f]
    Z = [trunc(f[i]/(f[(i+1)%3]*f[(i+2)%3]), order) for i in range(3)]
    E=[]
    for i in range(3):
        j,k=(i+1)%3,(i+2)%3
        e=2*u*sp.diff(H[i],u)-H[i]+H[i]*sum(H)-2*(Z[i]**2-(Z[j]-Z[k])**2)+lam*u
        E.append(trunc(e,order))
    C=sum(H[i]*H[j] for i in range(3) for j in range(i+1,3))+sum(z*z for z in Z)-2*sum(Z[i]*Z[j] for i in range(3) for j in range(i+1,3))+lam*u
    C=trunc(C,order)
    M=[trunc(2*Z[i]-H[(i+1)%3]-H[(i+2)%3],order) for i in range(3)]
    return H,Z,E,C,M


def solve_metric(max_order=5):
    # coeffs[k][i] is coefficient of u^k in f_i.  k=1 is free A_i.
    coeffs={1:A}
    records=[]
    for k in range(2,max_order+1):
        y=sp.symbols('b%d_1 b%d_2 b%d_3'%(k,k,k))
        coeffs[k]=list(y)
        f=build_f(k,coeffs)
        H,Z,E,C,M=geometry(f,k)
        # New coefficient first appears in coefficient u^k of Einstein equations.
        eq=[sp.expand(E[i]).coeff(u,k) for i in range(3)]
        mat,rhs=sp.linear_eq_to_matrix(eq,y)
        solvec=sp.simplify(mat.inv()*rhs) if mat.det()!=0 else sp.linsolve((mat,rhs),y)
        if isinstance(solvec,sp.FiniteSet):
            raise RuntimeError(('singular recurrence',k,solvec))
        sol={y[i]:sp.factor(solvec[i]) for i in range(3)}
        coeffs[k]=[sol[z] for z in y]
        # Check equations and Hamiltonian through this order after substitution.
        f=build_f(k,coeffs); H,Z,E,C,M=geometry(f,k)
        chkE=[sp.factor(sp.expand(e).coeff(u,k)) for e in E]
        chkC=sp.factor(sp.expand(C).coeff(u,k))
        records.append({'order':k,'coeff':[str(sp.factor(x)) for x in coeffs[k]],
                        'E_check':[str(x) for x in chkE], 'C_check':str(chkC)})
        print('metric order',k,'constraint check',chkC,flush=True)
    return coeffs,records


def propagate_X(coeffs,max_order):
    f=build_f(max_order,coeffs); H,Z,E,C,M=geometry(f,max_order)
    R=sp.symbols('R1 R2 R3', real=True)
    # X_i=sum_{n>=0} x[n,i]u^n, with x[0]=R_i.  Solve n x[n]=coeff of M X.
    xcoef={0:list(R)}
    length=[]
    for n in range(1,max_order+1):
        vals=[]
        for i in range(3):
            Xi=sum(xcoef[k][i]*u**k for k in range(n))
            rhs=sp.expand(trunc(M[i]*Xi,n)).coeff(u,n)
            vals.append(sp.factor(rhs/sp.Integer(n)))
        xcoef[n]=vals
        Ln=sp.factor(sum(vals))
        length.append(Ln)
        print('length condition L%d ='%n,sp.factor(Ln),flush=True)
    return R,M,xcoef,length


def main():
    max_order=int(os.environ.get('ORDER','5'))
    coeffs,recs=solve_metric(max_order)
    R,M,xcoef,length=propagate_X(coeffs,max_order)
    out={
      'lambda':-3,
      'A':[str(x) for x in A],
      'metric_records':recs,
      'M':[str(sp.factor(x)) for x in M],
      'X_coeffs':{str(k):[str(sp.factor(x)) for x in v] for k,v in xcoef.items()},
      'length_conditions':[str(sp.factor(x)) for x in length],
      'normalization':'R1+R2+R3=1, with Ri=x_i(0)^2 >=0'
    }
    od=os.path.join(os.path.dirname(__file__),'../data/step63'); os.makedirs(od,exist_ok=True)
    path=os.path.join(od,'bix_nut_series_order%d.json'%max_order)
    with open(path,'w') as fh: json.dump(out,fh,indent=1)
    print('saved',path)

if __name__=='__main__': main()
