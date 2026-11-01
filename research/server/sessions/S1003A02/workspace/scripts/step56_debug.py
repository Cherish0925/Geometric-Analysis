import numpy as np, math, importlib.util, sys, os
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("m", os.path.join(here, "step56_Tpoint_log_interaction.py"))
src = open(os.path.join(here, "step56_Tpoint_log_interaction.py")).read().replace("\nrun()\n", "\n")
ns = {"__file__": os.path.join(here, "step56_Tpoint_log_interaction.py")}
exec(compile(src, "m", "exec"), ns)
p = np.array([0.5, 0.3, -0.6, 0.55]); p /= np.linalg.norm(p)
for params in [(0, 1.0, 0, 0), (1.0, 0, 0, 0), (0, 0, 0, 1.0)]:
    T = ns["curv_tensor"](*params)
    evq = ns["make_evaluator"](ns["q_matrix"](T))
    gq, dgq, ddgq = evq(p)
    for e in [1e-2, 1e-3]:
        F, Ric, s = ns["F_density"](np.eye(4) + e * gq, e * dgq, e * ddgq)
        print(params, e, "F/e^2", F / e**2, "s/e", s / e)
    # Bianchi check
    bianchi = T + np.einsum('ijkl->iklj', T) + np.einsum('ijkl->iljk', T)
    print(" bianchi max", np.abs(bianchi).max(), " pair sym", np.abs(T - np.einsum('ijkl->klij', T)).max())
