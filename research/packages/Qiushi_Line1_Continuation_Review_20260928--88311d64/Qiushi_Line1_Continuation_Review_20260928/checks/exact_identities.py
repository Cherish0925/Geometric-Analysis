"""Exact polynomial checks, standard library only; not PDE proofs."""
from fractions import Fraction as F
import json

class P:
    def __init__(self, data=0):
        self.d = data if isinstance(data, dict) else ({(): F(data)} if data else {})
    def __add__(self, other):
        other = other if isinstance(other, P) else P(other)
        d = dict(self.d)
        for m, c in other.d.items(): d[m] = d.get(m, F(0)) + c
        return P({m:c for m,c in d.items() if c})
    __radd__ = __add__
    def __neg__(self): return P({m:-c for m,c in self.d.items()})
    def __sub__(self, other): return self + -as_p(other)
    def __rsub__(self, other): return as_p(other) + -self
    def __mul__(self, other):
        other = as_p(other); d = {}
        for m,c in self.d.items():
            for n,e in other.d.items():
                z = tuple(sorted(m+n)); d[z] = d.get(z,F(0)) + c*e
        return P({m:c for m,c in d.items() if c})
    __rmul__ = __mul__
    def __pow__(self, n):
        r=P(1)
        for _ in range(n): r=r*self
        return r
def as_p(x): return x if isinstance(x,P) else P(x)
def var(name): return P({(name,):F(1)})
def check(name, p):
    assert not p.d, (name,p.d)
    return {"identity":name,"exact":True}

V,Q,w,B,H,d,a,q,m1,m2,J = map(var,'V Q w B H d a q m1 m2 J'.split())
results=[]
results.append(check('replacement comparison, denominators cleared',
    4*(Q-B)*(4*V+Q)-4*Q*(4*(V+w)+Q-B)+16*(V*B+Q*w)))
results.append(check('replacement corrected remainder',
    -16*(V*B+Q*w)+4*B*(4*(V+w)+Q-B)
    -4*(4*B*w+B*Q-B**2-4*Q*w)))
uncompleted=12*H**2-4*d*H+4*(a-1)**2+2*d*(a-1)+(16+12*a)*q
completed=12*(H-d*F(1,6))**2+4*(a-1+d*F(1,4))**2+(16+12*a)*q-d**2*F(7,12)
results.append(check('conformal square identity',uncompleted-completed))
results.append(check('same-solution scalar slack identity',
    16*V-4*m2+8*J-(16*(m1-m2*F(1,2))+4*(m2-4*m1+4*V)+8*J)))
assert F(1,4)-F(7,12)==-F(1,3)
assert 16*(F(2,9)+F(7,36))==F(20,3)
results.append({"identity":"radial absorption and balanced coefficient","exact":True})
print(json.dumps(results,ensure_ascii=False,indent=2))
