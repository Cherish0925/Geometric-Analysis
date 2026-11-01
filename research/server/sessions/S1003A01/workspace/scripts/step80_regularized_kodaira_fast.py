"""Fast regularized Kodaira-current budgets on the Bianchi-VIII model.

The full Step-79 frame engine supplies pointwise F_v,F_eta and flux samples but
is too expensive for a fine epsilon sweep.  This script evaluates it on a
moderate adaptive u grid, reconstructs the radial current flux Phi from
Phi'=measure*F, and compares
    int F/(q+eps) = int Phi*q'/(q+eps)^2
for the same denominator.  It also records the moving flux peaks.

This is numerical evidence about nonuniform epsilon loss, not a proof.
"""
import os,sys,json
import numpy as np
import mpmath as mp
sys.path.insert(0,os.path.dirname(__file__))
# Importing the Step-79 script does not expose its nested analyse function, so
# read precomputed exact model geometry through a light reimplementation of the
# scalar radial Kodaira densities reconstructed from the exact integral engine.
# We generate samples by running the full engine in a subprocess would be slow;
# instead use the identities and exact asymptotic rates only.  This file is kept
# as a placeholder for a future exported analyse API.

# No fabricated output: exit with an explicit record.
def main():
 root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));d=os.path.join(root,'data','step80');os.makedirs(d,exist_ok=True)
 out={'status':'not_run','reason':'Step79 analyse is nested; exporting it or deriving exact F_v,F_eta formulas is needed. Scalar regularized model and exact zero models are the authoritative Step80 computations.'}
 json.dump(out,open(os.path.join(d,'regularized_kodaira_fast.json'),'w'),indent=1);print(out)
if __name__=='__main__':main()
