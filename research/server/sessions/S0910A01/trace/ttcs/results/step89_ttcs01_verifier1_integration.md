# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 89,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step89_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step89_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 89 correction of the product-orbifold chirality calculation. Check the corrected flat principal identity S_odd(V2)=(pi^2/2) R_odd(H) and D:H=-16 R_odd under the stated conventions; check whether the shape tensor q=g_A-g_B is indeed TT with Pq=-q and whether the principal odd source/receiver annihilation of q and scalar zero modes follows from the displayed tensor support; check the finite relative mixed-minus-all-same formulation for point-supported quadrupoles, including diagonal self-term cancellation, lack of inherited positivity, possible even/odd cross terms, and order bookkeeping t^3=o(t^(5/2)) relative to Ozuch Proposition 2.19. Please identify any remaining normalization or conceptual errors and state what is actually established versus still needing geometric/Bianchi/Ozuch matching.

## Integrated Scientific Memo

# Step 89 核验结论

Step 89 对平坦主部代数和“相对 Green 量”思路的修正确实成立，但仍有两个应立即修正的规范问题：

1. 必须明确 \(R^\pm_{22}\) 是在长度 \(\sqrt2\) 的基 \(\omega_a^\pm\) 下的**曲率算子矩阵元**，而不是未除以 \(|\omega_a^\pm|^2=2\) 的原始配对；
2. 相对响应若要对应 Ozuch 径向方程，权重应写成 \(a_i=t_i,\ b_j=t_j^2\)，不能沿用 \(w_iw_j\) 且同时令 \(w_j=t_j^2\)。

除此之外，尚未发现平坦恒等式本身的归一化错误。

## 1. 平坦主恒等式

令
\[
V_{2,ij}(x)=\frac12H_{ijpq}x_px_q,\qquad
D=A^+-A^-,
\]
其中
\[
A^+_{ijpq}=\sum_k(C_{2k})_{ij}(C_{2k})_{pq},\qquad
A^-_{ijpq}=\sum_k(C_{k2})_{ij}(C_{k2})_{pq}.
\]
在 \(S^3/\mathbb Z_2\) 上
\[
\int x_ax_bx_px_q\,d\sigma
=\frac{\pi^2}{24}
(\delta_{ab}\delta_{pq}+\delta_{ap}\delta_{bq}+\delta_{aq}\delta_{bp}),
\]
结合 \(\operatorname{tr}C_{ab}=0\) 和
\[
H_\pm^4=-\frac12A^\pm_{ijab}x_ax_b
\]
得到
\[
B^\pm=3\int\langle H_\pm^4,V_2\rangle
=-\frac{\pi^2}{16}A^\pm_{ijpq}H_{ijpq}.
\]
故
\[
\frac{S_{\rm odd}}{\pi^2}
=\frac{B^+-B^-}{2\pi^2}
=-\frac1{32}D:H.
\]

稀疏分量为
\[
D:H=-8H_{01,23}+8H_{03,12}+8H_{12,03}-8H_{23,01},
\]
而在文件所用取向及 Riemann 约定下，
\[
R_{\rm odd}
=\frac12\left(
H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01}
\right).
\]
逐项即得
\[
\boxed{D:H=-16R_{\rm odd}},\qquad
\boxed{S_{\rm odd}(V_2)=\frac{\pi^2}{2}R_{\rm odd}(H)}.
\]

这里的 \(100=10\times10\) 维基检验覆盖
\(\operatorname{Sym}^2\mathbb R^4\otimes\operatorname{Sym}^2\mathbb R^4\)，因此足以验证该固定规范下的完整张量恒等式。

### 必须澄清的曲率规范

上述公式要求
\[
(\delta R^\pm)_{22}
=
\frac{\langle\omega_2^\pm,\delta\mathcal R\,\omega_2^\pm\rangle}
{|\omega_2^\pm|^2},
\qquad |\omega_2^\pm|^2=2.
\]
若 \(R^\pm_{22}\) 被定义成未归一化的原始 \(1/4\)-缩并，则相应公式会变成
\[
S_{\rm odd}=\frac{\pi^2}{4}R_{\rm odd}^{\rm raw}.
\]
因此正文应明确采用“曲率算子矩阵元”或等价地采用 \(\omega^\pm/\sqrt2\) 的正交基。

轴向 Killing–Killing 模式满足
\[
H_{03,12}=H_{12,03}=-1,
\]
其余两个相关分量为零，故
\[
D:H=-16,\qquad R_{\rm odd}=1,\qquad S_{\rm odd}=\frac{\pi^2}{2},
\]
与
\[
B^+=\frac{\pi^2}{2},\qquad B^-=-\frac{\pi^2}{2}
\]
完全一致。其商空间范数
\[
\|h\|^2=\frac{64\pi^2}{9}
\]
也给出单模系数
\[
\frac{(\pi^2/2)\cdot1}{1\cdot(64\pi^2/9)}
=\frac9{128}.
\]

## 2. 形状模 \(q=g_A-g_B\)

在单位球乘积上，
\[
\nabla q=0,\qquad
\delta q=0,\qquad
\operatorname{tr}q=2-2=0.
\]
故 \(q\) 是 TT；商作用分别保持 \(g_A,g_B\)，所以它下降到 orbifold。又
\[
\mathring R(g_A)=g_A,\qquad
\mathring R(g_B)=g_B,
\]
从而
\[
Pq=\frac12\nabla^*\nabla q-\mathring R(q)=-q.
\]
因此 Step 88 关于 TT 谱全为正的前提确实错误。

\(q\) 的二次 jet 只有同因子、对角型分量，而 \(D:H\) 只使用上述四个完全混合、非对角分量，所以
\[
S_{\rm odd}^{\rm principal}(q)=0,
\qquad
R_{\rm odd}^{\rm principal}(q)=0.
\]

四个标量零模
\[
u_Ag_A,\quad u_Ag_B,\quad u_Bg_A,\quad u_Bg_B
\]
也具有 \(P=0\)，其平坦奇主部均为零。不过应修正一句解释：对于交叉项 \(u_Ag_B,u_Bg_A\)，并非“张量和微分指标都在同一因子”；它们确实可能具有 \(BB;AA\) 或 \(AA;BB\) 支撑，但张量因子是对角的 \(g_B\) 或 \(g_A\)，而 \(D\) 要求如 \(H_{23,01}\) 之类的非对角分量。等价地，这是 \(C_{11}\) 方向与 \(C_{2k}/C_{k2}\) 奇扇区的正交性。

这些结论只是平坦二阶 jet 的结论。它们尚未证明完整几何源不耦合到 \(q\) 或标量核。

## 3. 相对 mixed-minus-all-same 量

应采用一般源、接收权重
\[
a_i,\qquad b_j,
\]
写成
\[
\mathcal R_\epsilon(\tau)
=\sum_{i,j}a_ib_j
\left(
K^{00}_{ij}
+\epsilon_jK^{01}_{ij}
+\epsilon_iK^{10}_{ij}
+\epsilon_i\epsilon_jK^{11}_{ij}
\right).
\]
减去全 \(+\) 配置得
\[
\Delta_\epsilon(\tau)
=\sum_{i,j}a_ib_j
\left[
(\epsilon_j-1)K^{01}_{ij}
+(\epsilon_i-1)K^{10}_{ij}
+(\epsilon_i\epsilon_j-1)K^{11}_{ij}
\right].
\]

对 \(i=j\)，
\[
\epsilon_i^2-1=0,
\]
所以奇–奇自项在移除正则化之前便代数消失。这一点很重要，因为四维点支撑四极源形式上涉及
\[
\partial^4|x-y|^{-2}\sim |x-y|^{-6},
\]
其对角配对不是普通有限值。

但完整相对量的有限性尚未由此得到：对角交叉项
\[
(\epsilon_i-1)K^{01}_{ii}
+(\epsilon_i-1)K^{10}_{ii}
\]
一般仍在，并可能同样奇异。只有真正的局部取向对称性、主符号正交性或匹配减法才能将其消去；当前平坦奇–奇恒等式不能做到这一点。

有限非对角量也不继承正性：

- \(Pq=-q\) 表明 \(P^{-1}\) 在完整 TT 空间上不正；
- 即使正则化全矩阵曾为半正定，删去奇异对角也不保持半正定；非零、对角为零的对称矩阵不可能半正定。

轴向截断仍是有效的精确单模信号：
\[
K_{ij}^{11,\rm axial}=\frac9{128}s_is_j.
\]
对棋盘配置 \(\epsilon_i=s_i\)，
\[
(\epsilon_i\epsilon_j-1)K_{ij}^{11,\rm axial}
=\frac9{128}(1-s_is_j),
\]
故同号节点对贡献零，异号节点对贡献 \(9/64>0\)。这只是一个 \(\lambda=1\) 通道的贡献，不决定完整 Green 相互作用的符号。

## 4. 阶数与权重修正

Ozuch 使用
\[
\zeta_j=t_j\phi_j,\qquad
H^4(t_j\phi_j)=t_j^2H^4(\phi_j).
\]
节点 \(j\) 发出的场在节点 \(i\) 引起
\[
\delta\lambda_i=O(t_j^2),
\]
而径向方程中出现 \(t_i\lambda_i\)，故跨节点项为
\[
t_i\delta\lambda_i
=t_it_j^2\mathcal I_{ij}.
\]
可比尺度下这是 \(O(t^3)\)，并且
\[
t^3=o(t^{5/2}).
\]
因此 Proposition 2.19 的
\[
t_i\lambda_i+t_i^2\mu_i=O(t_{\max}^{5/2})
\]
无法识别 \(t^3\) 系数；需要余项至少为 \(o(t^3)\) 的更精细投影展开。

这里暴露出 Step 89 的记号不一致：若沿用 Step 88 的 \(w_j=t_j^2\)，则 \(w_iw_j=O(t^4)\)，并非径向 \(O(t^3)\) 项。与 Ozuch 匹配时应取
\[
\boxed{a_i=t_i,\qquad b_j=t_j^2.}
\]
这不影响奇–奇对角消去的代数，但影响最终系数和阶数。

## 5. 实际已经建立的内容

已严格建立：

- 固定取向和曲率算子规范下
  \[
  S_{\rm odd}=\frac{\pi^2}{2}R_{\rm odd},
  \qquad D:H=-16R_{\rm odd};
  \]
- 轴向值、节点符号模式及单模系数 \(9/128\)；
- \(q\) 为下降的 TT 模且 \(Pq=-q\)；
- \(q\) 和四个标量零模的平坦奇主源/接收均为零；
- mixed-minus-all-same 的奇–奇对角自项代数消去；
- 完整量不具有继承正性，且 even–odd/odd–even 项可能保留；
- 跨节点径向层为 \(t_it_j^2=O(t^3)\)，低于 Proposition 2.19 的分辨率。

尚未建立且对几何结论不可缺少：

- 包含 cutoff、Bianchi 修正、曲背景 parametrix、\(V_0\)/标架项及 \(H_2^4\) 的完整源；
- 与完整径向曲率接收器及 Ozuch 常数、符号、尺度的统一匹配；
- 在所选 slice 上的伪逆、完整核投影，以及所有负特征模的处理；
- 完整源对 \(q\) 的真正零耦合；目前只有主部消失；
- even–odd 和 odd–even 对角奇异项的消去或重整化；
- 匹配正则化下非对角 Green 极限的存在及其实际数值；
- 高谱贡献的收敛和求和；
- 余项为 \(o(t^3)\) 的投影展开。

因此，Step 89 成功修复了平坦代数和错误的正性推论，并确定了正确的有限比较目标；它尚未给出完整 Ozuch 径向系数，更未形成 Einstein 反解奇化障碍或存在性结论。