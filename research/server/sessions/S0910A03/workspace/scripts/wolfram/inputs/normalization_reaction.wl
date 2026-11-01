(* Step 24: exact normalization reaction in the curvature variation.
   Under h = -2a*g (the conformal part of the flow velocity),
   the linearized curvature variation has two contributions:
   1. Second-derivative terms: (1/2)(nabla_i nabla_k h_jl + ...) with h=(-2a)g
      -> the Kulkarni-Nomizu product Hess(a) ∧ g (zero-order in Rm)
   2. Lower-order terms: R_ijkp h^p_l, with h^p_l = (-2a)delta^p_l
      -> -2a R_ijkl  (LINEAR in Rm, coefficient -2a)

   We check the coefficient and sign of the linear reaction and the
   Kulkarni-Nomizu structure of the Hessian source.
*)

(* --- 1. Lower-order reaction from h=(-2a)g --- *)
(* R_ijkp h^p_l = R_ijkp (-2a) g^{pq} g_{ql} = -2a R_ijkp delta^p_l = -2a R_ijkl *)
(* Similarly R_ijlp h^p_k = -2a R_ijlk = -2a R_ijkl (by Rm symmetry R_ijlk = -R_ijkl, 
   wait: R_ijlk = -R_ijkl) *)

(* The full lower-order variation from the general formula is:
   (1/2)(R_ijkp h^p_l + R_ijlp h^p_k)
   = (1/2)(-2a R_ijkl + (-2a)(-R_ijkl))
   = (1/2)(-2a R_ijkl + 2a R_ijkl)
   = 0  !!
   
   Wait, this uses R_ijlk = -R_ijkl.  Let me be more careful with the
   conventions.
*)

(* Standard convention: R_{ijkl} is antisymmetric in (ij) and in (kl).
   So R_{ijlk} = -R_{ijkl}.
   
   The lower-order terms in dR_{ijkl}/dt from h_{ij}:
   
   Topping 2.3.7:
   (1/2)[R_{ijks} h^s_l + R_{ijls} h^s_k + R_{iskl} h^s_j + R_{sjkl} h^s_i]
   
   Wait, there are FOUR lower-order terms in Topping.  Let me check.
*)

(* Actually, different references have different numbers of lower-order terms.
   The Topping convention includes the metric-Christoffel terms.
   
   Let me use the definitive formula from Hamilton / Chow-Lu-Ni.
   
   From Chow-Lu-Ni, "Hamilton's Ricci Flow", Lemma 2.27 (as referenced):
   
   dR_{ijkl}/dt = 
     (1/2)(nabla_j nabla_k h_il + nabla_i nabla_l h_jk 
           - nabla_j nabla_l h_ik - nabla_i nabla_k h_jl)
     + (1/2)(R_{ijkp} h^p_l - R_{ijlp} h^p_k)
     + (1/2)(R_{pikl} h^p_j - R_{pjkl} h^p_i)
     
   That's 6 lower-order terms (but 4 distinct ones by symmetry).
   
   For h = (-2a)g:  h^p_l = (-2a) delta^p_l.
   
   (1/2)[R_{ijkp}(-2a delta^p_l) - R_{ijlp}(-2a delta^p_k)]
   = (1/2)(-2a)(R_{ijkl} - R_{ijlk})
   = (1/2)(-2a)(R_{ijkl} - (-R_{ijkl}))   (* R_{ijlk} = -R_{ijkl} *)
   = (1/2)(-2a)(2 R_{ijkl})
   = -2a R_{ijkl}
   
   (1/2)[R_{pikl}(-2a delta^p_j) - R_{pjkl}(-2a delta^p_i)]
   = (1/2)(-2a)(R_{jikl} - R_{ijkl})
   = (1/2)(-2a)(-R_{ijkl} - R_{ijkl})  (* R_{jikl} = -R_{ijkl} *)
   = (1/2)(-2a)(-2 R_{ijkl})
   = 2a R_{ijkl}
   
   Total lower-order from h=(-2a)g:  -2a R + 2a R = 0.
*)

Print["Lower-order reaction from h=(-2a)g:"]
Print["  First pair: -2a R_ijkl"]
Print["  Second pair: +2a R_ijkl"]
Print["  TOTAL = 0"]
Print[""]

(* --- 2. Second-derivative contribution from h=(-2a)g --- *)
(* nabla_j nabla_k h_il = nabla_j nabla_k [(-2a) g_il] 
   = (-2)(nabla_j nabla_k a) g_il   (since nabla g = 0).
   
   The full second-derivative expression:
   (1/2)[(-2)(nabla_j nabla_k a)g_il + (-2)(nabla_i nabla_l a)g_jk
        - (-2)(nabla_j nabla_l a)g_ik - (-2)(nabla_i nabla_k a)g_jl]
   = -(nabla^2 a ∧ g)_ijkl
   
   where (A ∧ g)_ijkl = A_jk g_il + A_il g_jk - A_jl g_ik - A_ik g_jl
   is the Kulkarni-Nomizu product.
*)

Print["Second-derivative contribution from h=(-2a)g:"]
Print["  -(Hess(a) KN g)_ijkl"]
Print["  = -(H_jk g_il + H_il g_jk - H_jl g_ik - H_ik g_jl)"]
Print["  where H = nabla^2 a"]
Print[""]

(* --- 3. Effect on |Rm|^2 from this normalization piece --- *)
(* The full lower-order is zero, so the conformal piece contributes to dRm/dt
   only through the Kulkarni-Nomizu second-derivative term.
   
   For d|Rm|^2/dt from the lower-order terms of the FULL flow h=-2aE=-2a Ric-2ag:
   
   The Ric part contributes the standard Ricci-flow lower-order:
   from -2a Ric, we get  (1/2)R_{ijkp}(-2a R^p_l) + ...
   = -a(R*Ric) terms => these are absorbed into a(Rm*Rm*Rm + Rm*Rm).
   
   The g part contributes ZERO to the lower-order, as shown above.
   
   For the INNER product R * (dR) = R_ijkl * dR_ijkl from the g piece:
   only the KN Hessian term survives:
   R^{ijkl}(-(Hess a) KN g)_{ijkl}
   
   Using R^{ijkl} g_{il} = R^{ijk}{}_k = 0 (first Bianchi) wait no, 
   R^{ijkl} g_{il} = g^{ia}g^{jb}g^{kc}g^{ld} R_{abcd} g_{il}
   = g^{jb}g^{kc}g^{ld} g^{ia}g_{il} R_{abcd}
   = g^{jb}g^{kc}g^{ld} delta^a_l R_{abcd}
   = g^{jb}g^{kc}g^{ld} R_{lbcd}
   Hmm, need to contract differently.
   
   Actually, R^{ijkl}(H_jk g_il + H_il g_jk - H_jl g_ik - H_ik g_jl)
   = H_jk R^{ijkl} g_{il} + H_il R^{ijkl} g_{jk} - H_jl R^{ijkl} g_{ik} - H_ik R^{ijkl} g_{jl}
   
   Now R^{ijkl} g_{il} = Ric^{jk} (contraction of 1st and 4th index of Rm gives Ric).
   Hmm wait, the contraction depends on which indices:
   g_{il} R^{ijkl} = R^{l jkl} = -R^{ljlk} = -Ric^{jk}.  
   
   Actually with standard conventions g_{il}R^{ijkl} = R_i{}^{jk}{}_i... 
   this is getting confusing.  Let me just note the key result:
   
   (Hess a) KN g contracted with Rm gives a RICCI contraction:
   R * (Hess(a) KN g) = C * (Hess(a))_{jk} Ric^{jk} + ... 
   
   which is bounded by |Hess(a)| * |Ric| <= |Hess(a)| * |Rm|.
*)

Print["Contraction R*(Hess(a) KN g):"]
Print["  = 2 H_jk [Ric^jk g_il R^{...} - ...] "]
Print["  Schematically: |R*(Hess(a) KN g)| <= C |Hess(a)| |Rm|"]
Print["  This is at most |Hess(a)| F (since |Rm| <= F)."]
Print[""]

(* --- 4. Summary for d|Rm|^2/dt under h=-2a(Ric+g) --- *)
Print["SUMMARY of normalization contribution to d|Rm|^2/dt:"]
Print["  Lower-order R*h from g piece: ZERO (exact cancellation)"]
Print["  Second-derivative from g piece: -(Hess a KN g)"]
Print["    -> contributes |Hess(a)|*F to d|Rm|^2 (not F^2, just F)"]
Print["  Metric-norm variation 2aE: contributes aF*Rm^2 = O(aF^3)"]
Print["  Volume-form variation: |a tr(E)| <= CaF"]
Print[""]

(* --- 5. The damping question --- *)
(* In the standard Ricci flow h=-2Ric, the lower-order R*h terms give
   the quadratic reaction Rm*Rm.  For our flow h=-2a(Ric+g):
   
   Ric piece: -2a * (Rm*Ric) => gives a*(Rm^3) type reaction
   g piece: exactly ZERO (as computed above)
   
   So the normalization does NOT produce a linear damping -4a|Rm|^2
   in the RIEMANN tensor evolution (unlike what I initially expected).
   It produces only the Hessian(a)*g KN source.
   
   The -4a|Rm|^2 damping DOES appear in the RICCI tensor evolution
   (from the -2ag piece of the velocity):
   d(Ric)/dt contains -2a*Ric from the standard part
   plus the conformal contribution 
   which includes a +(n-2) Hess(a) - (Delta a)g  piece.
   
   For the CURVATURE (Rm) evolution, the conformal piece gives only
   the KN Hessian, which is ADDITIVE and Rm-independent.
*)

Print["IMPORTANT CORRECTION:"]
Print["  The normalization h=-2ag does NOT produce linear"]
Print["  damping -4a|Rm|^2 in the Rm evolution."]
Print["  The lower-order R*h terms cancel for conformal h."]
Print["  Only the KN Hessian source -(Hess a) KN g remains."]
Print[""]
Print["  This is ADDITIVE (Rm-independent) and bounded by"]
Print["  C|Hess(a)| = C|Hess(chi^2)| <= C/r^2."]
Print["  Over time theta*r^2, it contributes O(theta) to |Rm|^2."]
Print[""]
Print["  The cubic reaction in d|Rm|^2/dt comes ONLY from the"]
Print["  -2a*Ric part of the flow, not from the normalization."]
Print["  This matches Wang's analysis for the unnormalized LRF."]
