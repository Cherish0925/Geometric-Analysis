# 本轮数学续研：谱稳定性、轨形分支排除与变分

日期：2026-10-08。入口为 `Einstein_Stability_and_Degeneration.pdf`，对应独立 LaTeX 为同名 `.tex`。正文 7 页；完整推导笔记在 `proofs/`，有限代数核验在 `code/`。这是本轮增量包，不替代系统的整月主稿。

## 可直接接入的结论

1. **已有完备例的严格谱稳定性。**继承系统构造的 `Ric=-3g, R_-=-Id`。应用 Artacho 2026 的局部扭曲旋量恒等式，对所有紧支撑无迹对称张量得到 `⟨Ah,h⟩=||DΦ(h)||²+2||h||²`。Friedrichs 谱在 `[2,∞)`，平滑 L² 零模消失。TT 方向上 `P''=||Ah||²/2≥2||h||²`。一般稳定性方法归于原文；本轮完成该模型上的应用、非紧积分与算子域论证。
2. **指定轨形的全度量障碍及退化分支排除。**在单吹起的双符号全度量实际 SW 供给、`2χ+3τ=A−1` 下，利用反向 `B₂` 的实际 Ricci-flat 平滑，把供给传到收缩所得轨形的每个光滑度量，得到 `P_orb≥8π²(4−A/3)`。因此 `A≤9` 时，严格低于 `8π²` 的序列不能光滑收敛于这种紧轨形。最终证明不再需要先有一列常标量近极小度量；也没有把所有极小序列预设为这一分支。
3. **实际零 P 商泡构造。**`X#CPbar²` 中存在反向 `D(T*RP²)`；插入 Ricci-flat Eguchi–Hanson/Z₂ 后可产生真正光滑退化，`P(g_a)→P_orb(g_0)`，商泡的全曲率为 `6π²`。正的全曲率泡费用不能直接算成正的无迹 Ricci 费用。普通 ADE 球排除与此商型核心有本质区别。
4. **完整混合稳定测试。**负常标量 P 临界点的 TT 方向 h，最佳共形修正为 `f=(6L−2s)^{-1}(⟨Ric°,h⟩−均值)`。相应 Hessian 是原 TT Hessian 减去显式非负的谱项。该公式不预设极小元存在。
5. **已有完备例的全局积分结构。**得到 `∇Ω∈L^p iff p>4/3`、绝对收敛的背景曲率差积分与 Euler 特征数关系、精确边界通量。此前已有二次和四次扭率积分不重复计为新增结果。

## 证明文件对应

| 文件 | 内容 |
|---|---|
| `proofs/q4_chiral_stability.md` | 谱分解、Friedrichs 域、L² 零模、两个 Hessian |
| `proofs/q3_new_global_attainment.md` | 混合变分；第 5 节为最新实际场轨形传递及 A≤9 分支排除 |
| `proofs/q2_exact_infimum_new.md` | 球面格及正 b₂ 半共形平坦 ALE 排除；有理球嵌入、真实匹配、取向预算 |
| `proofs/q4_finite_energy_boundary.md` | Lᵖ 阈值、曲率积分及特征边界项 |
| `proofs/q4_zero_locus_new.md` | 有限阶扭率零点与实际 Ricci-flat 局部例；不是负 Einstein 局部解 |
| `proofs/q4_zero_index_algebra.md` | 必要代数条件的完整计算；不作为实际 Einstein 解 |
| `proofs/q1_exact_einstein_new.md` | Q1 检查所得的有效经典限制和未闭合条件 |
| `proofs/Inherited_Complete_Example.tex` | 继承的完备构造与先前独立核验，供追读；不计本轮新增构造 |

`q2_exact_infimum_new.md` 中轨形转移曾列作条件命题；随后 `q3_new_global_attainment.md` 第 5 节完成指定收敛分支的证明。最终又通过显式平滑去掉对已有序列的依赖，得到正文 Theorem 4.2 的轨形全度量障碍；该定理是本包的最终版本。

## 仍未得到的四个结论

小吹起一般型曲面的全部 Einstein 存在性判定、一般吹起族的匹配全度量最优值、一个光滑非 Bach-flat 全局 P 极小元、闭四维负 Goldberg 的完整解答，均未由本轮证明。分支排除不覆盖普通 ASD 取向有理球、部分塌缩及一般非半共形平坦 Ricci-flat ALE；谱稳定性不把完备非紧例变成闭例。

## 运行核验

三个 Python 文件使用 SymPy。`q4_finite_energy_boundary_check.py` 核对本轮体积、通量、曲率及边界恒等式；`q4_gh_zero_check.py` 核对局部 Ricci-flat 零点模型；`Q4_independent_cartan.py` 是继承的完整 Cartan 核验。程序证明有限代数恒等式；弱极限、可移除性和变分论证由正文提供。

文献已在正文逐项署明；本包不宣布新增解决任何公开猜想，也不声称对全文原创性完成全球查新。
