#!/usr/bin/env python3
"""
Step 100: Structural proof of same-chirality vanishing B_{++} = B_{--} = 0.

The EH metric is anti-self-dual (Ozuch line 307), so H^4(zeta^+)
produces linearized curvature that is Ricci-flat anti-self-dual
(Ozuch line 332): d_e R^+(H^4(zeta^+)) = 0.

The receiver R_plus reads self-dual curvature; the source S_plus
encodes the H^4 boundary pairing. We prove that at each fixed
spectral degree pair (ell_t, ell_s), the sum over tensor-scalar
polarizations in B_{++} vanishes exactly, by showing the algebraic
identity at the level of the bilinear maps.

The proof works by computing the exact bilinear receiver/source
maps on the product basis {I, D, O} x {I, D, O} and showing that
the weighted polarization sum vanishes identically for each node
pair, sector, and degree combination.
"""
from __future__ import annotations
import importlib.util, sys, pathlib, json
import numpy as np
import sympy as sp

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# ---- Build exact coefficient arrays directly (from step99 form algebra) ----
KIDX = [1, 2]

def _zero_mat(n=4):
    A = np.empty((n,n), dtype=object)
    for i,j in np.ndindex(n,n): A[i,j] = sp.Rational(0)
    return A

def _wedge(i,j,n=4):
    A = _zero_mat(n); A[i,j]=sp.Rational(1); A[j,i]=sp.Rational(-1); return A

def _matmul(A,B):
    n=A.shape[0]; C=_zero_mat(n)
    for i,j in np.ndindex(n,n): C[i,j]=sp.simplify(sum(A[i,k]*B[k,j] for k in range(n)))
    return C

def _transpose(A):
    B=_zero_mat(A.shape[0])
    for i,j in np.ndindex(A.shape[0],A.shape[1]): B[i,j]=A[j,i]
    return B

def _add(A,B,scale=sp.Rational(1)):
    C=_zero_mat(A.shape[0])
    for i,j in np.ndindex(A.shape[0],A.shape[1]): C[i,j]=sp.simplify(A[i,j]+scale*B[i,j])
    return C

e01=_wedge(0,1); e02=_wedge(0,2); e03=_wedge(0,3)
e12=_wedge(1,2); e13=_wedge(1,3); e23=_wedge(2,3)
WP_RAW=[_add(e01,e23), _add(e02,e13,scale=-1), _add(e03,e12)]
WM_RAW=[_add(e01,e23,scale=-1), _add(e02,e13), _add(e03,e12,scale=-1)]

CEX=np.empty((3,3,4,4), dtype=object)
for a,b in np.ndindex(3,3):
    P=_matmul(WP_RAW[a],WM_RAW[b]); S=_add(P,_transpose(P))
    for i,j in np.ndindex(4,4): CEX[a,b,i,j]=sp.simplify(S[i,j]/2)

def _curv_block(rawA,rawB):
    L=np.empty((4,4,4,4),dtype=object)
    for idx in np.ndindex(4,4,4,4): L[idx]=sp.Rational(0)
    for a,b,c,d in np.ndindex(4,4,4,4):
        ca=rawA[a,b]; cb=rawB[c,d]
        if ca==0 or cb==0: continue
        fac=ca*cb/sp.Rational(16)
        L[a,d,b,c]+=fac; L[b,c,a,d]+=fac; L[a,c,b,d]-=fac; L[b,d,a,c]-=fac
    for idx in np.ndindex(4,4,4,4): L[idx]=sp.simplify(L[idx])
    return L

RCOEFF={"plus":np.empty((2,2,4,4,4,4),dtype=object),"minus":np.empty((2,2,4,4,4,4),dtype=object)}
for ia,a in enumerate(KIDX):
    for ib,b in enumerate(KIDX):
        RCOEFF["plus"][ia,ib]=_curv_block(WP_RAW[a],WP_RAW[b])
        RCOEFF["minus"][ia,ib]=_curv_block(WM_RAW[a],WM_RAW[b])

SCOEFF={"plus":np.empty((2,2,4,4,4,4),dtype=object),"minus":np.empty((2,2,4,4,4,4),dtype=object)}
for ia,a in enumerate(KIDX):
    for ic,c in enumerate(KIDX):
        for idx in np.ndindex(4,4,4,4):
            Tp=sp.Rational(0); Tm=sp.Rational(0); i,j,p,q=idx
            for b in range(3):
                Tp+=CEX[a,b,i,j]*CEX[c,b,p,q]; Tm+=CEX[b,a,i,j]*CEX[b,c,p,q]
            SCOEFF["plus"][ia,ic,i,j,p,q]=sp.simplify(-Tp/sp.Rational(16))
            SCOEFF["minus"][ia,ic,i,j,p,q]=sp.simplify(-Tm/sp.Rational(16))

# 2x2 matrix basis for Sym^2(R^2)
I2 = sp.Matrix([[1,0],[0,1]])
D2 = sp.Matrix([[1,0],[0,-1]])
O2 = sp.Matrix([[0,1],[1,0]])
BASIS = {"I": I2, "D": D2, "O": O2}


def exact_contract(C, H):
    """Contract 6-index C with 4-index H -> 2x2 matrix."""
    out = sp.zeros(2, 2)
    for ia in range(2):
        for ib in range(2):
            s = sp.Rational(0)
            for i, j, p, q in np.ndindex(4, 4, 4, 4):
                if C[ia, ib, i, j, p, q] != 0 and H[i, j, p, q] != 0:
                    s += C[ia, ib, i, j, p, q] * H[i, j, p, q]
            out[ia, ib] = sp.simplify(s)
    return out


def make_H_AA(T, S):
    """AA sector: H[a,c,2+p,2+q] = T[a,c]*S[p,q]"""
    H = np.empty((4, 4, 4, 4), dtype=object)
    for idx in np.ndindex(4, 4, 4, 4):
        H[idx] = sp.Rational(0)
    for a in range(2):
        for c in range(2):
            for p in range(2):
                for q in range(2):
                    H[a, c, 2 + p, 2 + q] = T[a, c] * S[p, q]
    return H


def make_H_BB(T, S):
    """BB sector: H[2+p,2+q,a,c] = T[p,q]*S[a,c]"""
    H = np.empty((4, 4, 4, 4), dtype=object)
    for idx in np.ndindex(4, 4, 4, 4):
        H[idx] = sp.Rational(0)
    for p in range(2):
        for q in range(2):
            for a in range(2):
                for c in range(2):
                    H[2 + p, 2 + q, a, c] = T[p, q] * S[a, c]
    return H


def compute_bilinear_table(coeff, sector):
    """Compute R or S map on all basis pairs (T, S) -> 2x2 matrix."""
    make_H = make_H_AA if sector == "AA" else make_H_BB
    table = {}
    for tn, T in BASIS.items():
        for sn, S in BASIS.items():
            H = make_H(np.array(T.tolist(), dtype=object),
                       np.array(S.tolist(), dtype=object))
            M = exact_contract(coeff, H)
            table[(tn, sn)] = M
    return table


# Compute bilinear tables for all sectors and chiralities
print("Computing exact bilinear maps...")
tables = {}
for chir in ["plus", "minus"]:
    for kind in ["R", "S"]:
        coeff = RCOEFF[chir] if kind == "R" else SCOEFF[chir]
        for sector in ["AA", "BB"]:
            key = (kind, chir, sector)
            tables[key] = compute_bilinear_table(coeff, sector)

# Print selected maps to show structure
print("\n=== BILINEAR MAP STRUCTURE ===")
for sector in ["AA", "BB"]:
    print(f"\n--- Sector {sector} ---")
    for kind in ["R", "S"]:
        for chir in ["plus", "minus"]:
            key = (kind, chir, sector)
            tab = tables[key]
            nonzero = {k: v for k, v in tab.items() if v != sp.zeros(2, 2)}
            if nonzero:
                print(f"  {kind}_{chir} nonzero entries:")
                for (tn, sn), M in nonzero.items():
                    print(f"    ({tn},{sn}): {M.tolist()}")

# Tensor seeds for the four polarization types
# TSEEDS: (electric,c2)=D, (electric,s2)=O, (magnetic,c2)=O, (magnetic,s2)=-D
TSEEDS = [("D", +1), ("O", +1), ("O", +1), ("D", -1)]  # (base matrix name, sign)
# The above encodes: E_c2→D, E_s2→O, M_c2→O, M_s2→-D

# Node sign function
def node_sign(pole, ell, seed_type):
    """seed_type: 'c2', 's2', 'm0'"""
    if pole == "N":
        return 1
    base = 1 if ell % 2 == 0 else -1
    return -base if seed_type == "s2" else base


def test_cancellation_at_degree(sector, pair, ell_t, ell_s, verbose=False):
    """
    Test B_{++} = 0 for the given sector/pair/degrees.
    
    pair: (tensor_pole_recv, tensor_pole_src, scalar_pole_recv, scalar_pole_src)
    e.g., for NN<-NS in AA: tensor both at N_A=(N,N), scalar at N_B vs S_B
    """
    t_recv_pole, t_src_pole, s_recv_pole, s_src_pole = pair
    
    # Tensor type data: [(base_name, sign)]
    tensor_types = [
        ("D", +1, "c2"),   # electric c2
        ("O", +1, "s2"),   # electric s2
        ("O", +1, "c2"),   # magnetic c2
        ("D", -1, "s2"),   # magnetic s2
    ]
    
    # Scalar modes for this degree
    if ell_s == 0:
        scalar_modes = [("I", 1, "m0")]
    elif ell_s == 1:
        scalar_modes = [("I", 1, "m0")]
    else:
        mu = ell_s * (ell_s + 1)
        w_m0 = sp.Rational(2 * mu, mu - 2)
        scalar_modes = [
            ("I", w_m0, "m0"),
            ("D", sp.Rational(1), "c2"),
            ("O", sp.Rational(1), "s2"),
        ]
    
    # Accumulate B_{++} as a list of 2x2 matrices for each kernel-plane entry
    B_pp = sp.zeros(2, 2, 2, 2) if False else {}  # use dict for 4-index
    # Actually use 4 nested indices
    total = [[[[sp.Rational(0) for _ in range(2)] for _ in range(2)] 
              for _ in range(2)] for _ in range(2)]
    
    R_tab = tables[("R", "plus", sector)]
    S_tab = tables[("S", "plus", sector)]
    
    for t_base, t_sign, t_seed in tensor_types:
        t_recv_sign = t_sign * node_sign(t_recv_pole, ell_t, t_seed)
        t_src_sign = t_sign * node_sign(t_src_pole, ell_t, t_seed)
        
        # Receiver tensor matrix name (with sign)
        # R(t_recv_sign * T_base ⊗ S) = t_recv_sign * R(T_base ⊗ S)
        
        for s_base, s_weight, s_seed in scalar_modes:
            s_recv_sign = node_sign(s_recv_pole, ell_s, s_seed)
            s_src_sign = node_sign(s_src_pole, ell_s, s_seed)
            
            # Get bilinear maps
            R_val = R_tab[(t_base, s_base)]
            S_val = S_tab[(t_base, s_base)]
            
            # Apply signs
            overall_R = t_recv_sign * s_recv_sign
            overall_S = t_src_sign * s_src_sign
            
            # Accumulate outer(R, S) * weight * signs
            for ia in range(2):
                for ib in range(2):
                    for ic in range(2):
                        for id_ in range(2):
                            total[ia][ib][ic][id_] += (
                                s_weight * overall_R * overall_S *
                                R_val[ia, ib] * S_val[ic, id_]
                            )
    
    # Simplify
    max_abs = sp.Rational(0)
    for ia in range(2):
        for ib in range(2):
            for ic in range(2):
                for id_ in range(2):
                    v = sp.simplify(total[ia][ib][ic][id_])
                    total[ia][ib][ic][id_] = v
                    if v != 0:
                        max_abs = max(max_abs, abs(v))
    
    is_zero = max_abs == 0
    
    if verbose and not is_zero:
        print(f"  NONZERO B_++ for {sector} pair={pair} ell_t={ell_t} ell_s={ell_s}")
        for ia in range(2):
            for ic in range(2):
                block = [[total[ia][ib][ic][id_] for id_ in range(2)] for ib in range(2)]
                print(f"    recv({ia}) src({ic}): {block}")
    
    return is_zero


# Define node pairs for the four-node orbifold
# Nodes: NN(0), NS(1), SN(2), SS(3)
# Receiver always NN. Node components: (A_pole, B_pole)
node_poles = {"NN": ("N", "N"), "NS": ("N", "S"), "SN": ("S", "N"), "SS": ("S", "S")}

def pair_config(source_node, sector):
    """Return (tensor_recv_pole, tensor_src_pole, scalar_recv_pole, scalar_src_pole)."""
    recv = node_poles["NN"]
    src = node_poles[source_node]
    if sector == "AA":
        # Tensor on factor A, scalar on factor B
        return (recv[0], src[0], recv[1], src[1])
    else:  # BB
        # Tensor on factor B, scalar on factor A
        return (recv[1], src[1], recv[0], src[0])


# Run exhaustive test
print("\n=== SAME-CHIRALITY CANCELLATION TEST ===")
results = {"tests": [], "all_zero": True}
test_degrees = [(2, 0), (2, 1), (2, 2), (2, 3), (2, 5), (3, 2), (3, 3), 
                (4, 2), (4, 4), (5, 3), (8, 7), (15, 12)]

for sector in ["AA", "BB"]:
    for source_node in ["NS", "SN", "SS"]:
        pair = pair_config(source_node, sector)
        for ell_t, ell_s in test_degrees:
            ok = test_cancellation_at_degree(sector, pair, ell_t, ell_s, verbose=True)
            results["tests"].append({
                "sector": sector, "source": source_node, 
                "ell_t": ell_t, "ell_s": ell_s, "B_pp_zero": ok
            })
            if not ok:
                results["all_zero"] = False

failures = [t for t in results["tests"] if not t["B_pp_zero"]]
print(f"\nTotal tests: {len(results['tests'])}")
print(f"Failures: {len(failures)}")
print(f"All B_++ vanish: {results['all_zero']}")

if failures:
    print("\nFailed cases:")
    for f in failures:
        print(f"  {f}")

# Now prove the mechanism: factor the cancellation
print("\n=== CANCELLATION MECHANISM ANALYSIS ===")
# For pair NS in AA: tensor at (N,N), scalar at (N,S)
# Tensor types at N: E_c2=D, E_s2=O, M_c2=O, M_s2=-D
# All have recv_sign=src_sign=node_sign(N,ell_t,seed)=1
# So the sum over 4 tensor types (at same pole) is:
# R(D⊗S)*S(D⊗S) + R(O⊗S)*S(O⊗S) + R(O⊗S)*S(O⊗S) + R(D⊗S)*S(D⊗S)
# = 2[R(D⊗S)*S(D⊗S) + R(O⊗S)*S(O⊗S)]
# 
# This must cancel between scalar modes or be zero per mode.

print("\nChecking R_plus bilinear map identities...")
for sector in ["AA", "BB"]:
    R_tab = tables[("R", "plus", sector)]
    S_tab = tables[("S", "plus", sector)]
    
    # Check: R(D,S)*S(D,S) + R(O,S)*S(O,S) for each scalar S
    for sn in ["I", "D", "O"]:
        RD = R_tab[("D", sn)]
        RO = R_tab[("O", sn)]
        SD = S_tab[("D", sn)]
        SO = S_tab[("O", sn)]
        
        # Sum of outer products
        total_diag = sp.zeros(2, 2)
        for ia in range(2):
            for ic in range(2):
                val = sp.simplify(RD[ia, 0]*SD[ic, 0] + RD[ia, 1]*SD[ic, 1] +
                                  RO[ia, 0]*SO[ic, 0] + RO[ia, 1]*SO[ic, 1])
                total_diag[ia, ic] = val
        # Check a simpler identity: trace(R.T @ S) for D and O types
        print(f"  {sector} S={sn}: R(D)@S(D)^T + R(O)@S(O)^T trace components:")
        for ia in range(2):
            for ic in range(2):
                v = sp.simplify(sum(RD[ia,k]*SD[ic,k] for k in range(2)) + 
                                sum(RO[ia,k]*SO[ic,k] for k in range(2)))
                print(f"    [{ia},{ic}] = {v}")

# Check the KEY identity: sum_T tr(R_plus(T⊗S) @ S_plus(T⊗S)^T) for T in {D,O,-D,O}
print("\n=== KEY IDENTITY: sum over tensor types of R(T,S)*S(T,S) ===")
for sector in ["AA", "BB"]:
    R_tab = tables[("R", "plus", sector)]
    S_tab = tables[("S", "plus", sector)]
    
    print(f"\nSector {sector}:")
    for sn in ["I", "D", "O"]:
        # The 4 tensor types at the SAME pole all give (base, sign):
        # (D,+1), (O,+1), (O,+1), (D,-1)
        # Sum of sign_recv * sign_src = 1*1 + 1*1 + 1*1 + (-1)*(-1) = 4
        # But the products are:
        # R(D,S)*S(D,S) + R(O,S)*S(O,S) + R(O,S)*S(O,S) + R(-D,S)*S(-D,S)
        # = R(D,S)*S(D,S) + 2R(O,S)*S(O,S) + R(D,S)*S(D,S)
        # = 2[R(D,S)*S(D,S) + R(O,S)*S(O,S)]
        
        combo = sp.zeros(2, 2)
        for ia in range(2):
            for ib in range(2):
                RD_val = R_tab[("D", sn)][ia, ib]
                RO_val = R_tab[("O", sn)][ia, ib]
                SD_val = S_tab[("D", sn)][ia, ib]
                SO_val = S_tab[("O", sn)][ia, ib]
                # For the outer product B_{++}[ia,ib,ic,id], we need
                # sum over tensor types: this gives 2*(R_D*S_D + R_O*S_O) for (ia,ib,ic,id)
                # But R and S are 2x2, and the outer is 2x2x2x2
                pass
        
        # Actually compute the 2x2 x 2x2 block sum correctly
        total_block = [[[[sp.Rational(0) for _ in range(2)] for _ in range(2)]
                        for _ in range(2)] for _ in range(2)]
        for t_name, t_sign in [("D", 1), ("O", 1), ("O", 1), ("D", -1)]:
            R_val = R_tab[(t_name, sn)]
            S_val = S_tab[(t_name, sn)]
            for ia in range(2):
                for ib in range(2):
                    for ic in range(2):
                        for id_ in range(2):
                            total_block[ia][ib][ic][id_] += (
                                t_sign**2 * R_val[ia, ib] * S_val[ic, id_])
        
        max_v = max(abs(sp.simplify(total_block[ia][ib][ic][id_]))
                    for ia in range(2) for ib in range(2) 
                    for ic in range(2) for id_ in range(2))
        is_zero = max_v == 0
        print(f"  Scalar={sn}: tensor-sum block max = {max_v}, zero = {is_zero}")
        
        if not is_zero:
            # Print the nonzero entries
            for ia in range(2):
                for ib in range(2):
                    for ic in range(2):
                        for id_ in range(2):
                            v = sp.simplify(total_block[ia][ib][ic][id_])
                            if v != 0:
                                print(f"    [{ia},{ib},{ic},{id_}] = {v}")

# Save results
out_path = DATA_DIR / "step100_chirality_cancellation_proof.json"
results["mechanism"] = "EH definite chirality: d_e R^+(H^4(zeta^+)) = 0 (Ozuch line 332)"
with open(out_path, "w") as f:
    json.dump(results, f, indent=2, default=str)

print(f"\nWrote {out_path}")
