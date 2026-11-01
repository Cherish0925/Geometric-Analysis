ClearAll[x, T, A, k, c2, Cp, Cm, kb, Scx, Srev, y];
F = (Sqrt[8 x] + Sqrt[T - x])^2;
gap = FullSimplify[9 x + 3 T - F - 2 (Sqrt[T - x] - Sqrt[2 x])^2,
  Assumptions -> 0 <= x <= T];
host = Expand[9 (4 c2 - A + 5 k + Cm) + 3 (A - k + Cp) - (6 A + Cp)];
hostTarget = 9 Cm + 2 Cp + 42 k + 12 (3 c2 - A);
budget = Expand[9 (-4 ((k - kb) + Scx)) + 2 (-4 Srev) + 42 k];
budgetTarget = 6 k + 36 kb - 36 Scx - 8 Srev;
betaRaw = ((A/3 + k) - A (4 - Sqrt[1 - 3 k/A])^2/27)/4;
betaY = FullSimplify[betaRaw /. A -> 3 k/(1 - y^2), Assumptions -> 0 <= y < 1 && k > 0];
betaTarget = k (5 y + 1)/(18 (1 + y));
Print["gap_identity=", gap];
Print["host_difference=", Expand[host - hostTarget]];
Print["budget_difference=", Expand[budget - budgetTarget]];
Print["beta_y_difference=", FullSimplify[betaY - betaTarget, Assumptions -> 0 <= y < 1 && k > 0]];
Print["beta_y=", Factor[betaY]];
