# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 93,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step93_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step93_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 93 correction to the product-orbifold mixed-chirality desingularization target for Yau Problem 26. Check, using the supplied files, whether the curvature correction R^±=diag(Λ,0,0) for S^2×S^2 is correct; whether this invalidates the old Step 92 I/3 critical-scale/e1 ansatz; whether the corrected target should indeed be the Ozuch/Biquard response restricted to ker R^±=ω^⊥ with an angular D8+K invariant equation; and whether the O(t^3) pattern term versus O(t^(5/2)) remainder caveat is stated honestly. Identify any remaining mathematical or source-level errors that could mislead the next computation, and suggest the sharpest concrete formulation of the next coefficient/remainder problem. Do not decide the whole Yau-26 problem; focus on correctness and usefulness of this corrected local target.

## Integrated Scientific Memo

# Step 93 核验结论

## 1. 曲率修正完全正确

设两个曲面因子均有常截面曲率 \(\Lambda\)，则乘积度量满足
\[
\operatorname{Ric}=\Lambda g.
\]
在适应乘积分解的正交标架中，曲率算子在
\[
(e^{12},e^{13},e^{14},e^{23},e^{24},e^{34})
\]
上的矩阵为
\[
\operatorname{diag}(\Lambda,0,0,0,0,\Lambda).
\]
取规范化的自对偶/反自对偶基，首向量为
\[
\kappa^\pm=\frac{e^{12}\pm e^{34}}{\sqrt2},
\]
立即得到
\[
R^+=R^-=\operatorname{diag}(\Lambda,0,0).
\]
又因 \(s=4\Lambda\)，
\[
W^\pm=R^\pm-\frac{s}{12}I
=\operatorname{diag}\!\left(\frac{2\Lambda}{3},
-\frac{\Lambda}{3},-\frac{\Lambda}{3}\right).
\]
因此 \(S^2\times S^2\) 不是共形平坦的；Step 93 的 JSON 与此一致。取商不改变奇点局部覆盖上的曲率计算。

一个记号修正：在标准复定向下，只有 \(\kappa^+\) 是标准乘积复结构的 Kähler 形式；\(\kappa^-\) 对应把一个因子的复结构反向后得到的平行形式。因此宜把两者统称为“秩一平行形式方向”，而不是不加区别地称为 Kähler 方向。

## 2. 旧的 \(I/3\)、临界尺度和 \(e_1\) 假设确实失效

Ozuch 的首阶障碍为
\[
\lambda_k(\zeta^\pm)
=c\left\langle R^\pm\zeta^\pm,\zeta^\pm_{(k)}\right\rangle .
\]
全部 \(\lambda_k\) 消失等价于
\[
R^\pm\zeta^\pm=0.
\]
故乘积节点允许的主导 EH 参数必须满足
\[
\zeta_j=t_j\xi_j,\qquad
\xi_j\in K_j:=\ker R^{\epsilon_j}
=(\kappa_j^{\epsilon_j})^\perp,\qquad \dim K_j=2.
\]

所以：

* \(R^\pm=(\Lambda/3)I\) 错误；
* \(e_1=\kappa^\pm\) 是像方向，不是可允许的核方向；
* 沿 \(e_1\) 的障碍在 \(O(t)\)，不能由 \(O(t^3)\) 的节点间作用在 \(t\to0\) 时抵消；
* \(1/3+t^2K=0\) 及 \(t_*^2=-1/(3K)\) 不是邻近该 orbifold 极限的 gluing 方程。

形式上沿 \(e_1\) 写 \(\Lambda+t^2K=0\) 也只能给出 \(t=O(1)\) 的根，超出小尺度展开的有效范围。

JSON 中单像矩阵
\[
12uu^T-4I
\]
的特征值 \(8,-4,-4\) 本身正确，但它只是单位分离下的平坦代数模型；旧 \(e_1\) 计算位于被排除的像方向，不能决定乘积 orbifold 的物理系数。

## 3. 核平面上的 Ozuch/Biquard 响应是正确目标，但当前公式仍偏示意

令源节点 \(i\) 的全局投影场 \(\bar h_i^4(\xi_i)\) 具有 EH 奇异渐近
\[
H_i^4(t_i\xi_i)=t_i^2H_i^4(\xi_i),
\]
并满足 Bianchi/gauge 条件及对 \(\ker P_{g_o}\) 的正交规范。在接收节点 \(j\neq i\) 附近写
\[
\bar h_i^4=A_{ji,0}+A_{ji,2}+O(r_j^4).
\]
应把物理响应不变量地定义为
\[
Q_{ji}^{\epsilon_j,\epsilon_i}(\xi_i)
=
\left.\frac d{ds}\right|_{s=0}
R^{\epsilon_j}_{g_o+s\bar h_i^4(\xi_i)}(p_j),
\]
其中曲率块必须在随扰动正交化的标架中表达。真正需要计算的是
\[
B_{ji}(\xi_i)
=\Pi_{K_j}Q_{ji}^{\epsilon_j,\epsilon_i}(\xi_i)\Pi_{K_j}
\in\operatorname{Sym}(K_j).
\]

解掉秩一像方向后，核方程的结构确为
\[
\Pi_{K_j}
\left(\sum_{i\ne j}t_i^2Q_{ji}(\xi_i)\right)
\Pi_{K_j}\xi_j=0
\]
再加上同阶的自节点、坐标、orbifold 变形及非线性修正。等尺度时公共 \(t^2\) 可从方向方程中约去，因此这不是临界尺度问题。

不过有三项必须修正或补充。

### 3.1 Proposition 2.10 不是接收节点 \(2\times2\) 块本身

Ozuch Proposition 2.10 的
\[
\nu_l=3\int_{S^3/\mathbb Z_2}\langle H^4,V_{l,2}\rangle
\]
描述全局核投影并构造 \(\bar h^4\)。节点间 \(B_{ji}\) 还需从 \(\bar h_i^4\) 在 \(p_j\) 的正则 jet 中提取，再代入首障碍公式。不能直接把边界积分等同于 \(B_{ji}\)。

### 3.2 暂不能把求和严格限制为异手性节点

EH 平坦近场确有手性互换：
\[
d_{\mathbf e}R^-(H^4(\zeta^+))\in\operatorname{End}(\Omega^-),
\]
但这本身不证明经弯曲乘积 Green 算子传播后，每一个同手性源在另一节点的 \(K\)-块逐对为零。全兼容 Kähler–Einstein 族只能校准完整总和，不能推出每一对作用分别消失。

因此在证明相应保持定理前，应使用
\[
\sum_{i\ne j}B_{ji},
\]
而不是预先只对 \(\epsilon_i\ne\epsilon_j\) 求和。全兼容行必须用于校准完整三阶映射。

### 3.3 “一个角方程”尚未推出

对
\[
\xi_j(\theta)=\cos\theta\,e_{2,j}+\sin\theta\,e_{3,j},
\]
一般 \(K_j\)-值方程有径向和角向两个分量：
\[
f_{\rm rad}=\langle F_j,\xi_j\rangle,\qquad
f_{\rm ang}=\langle F_j,J\xi_j\rangle.
\]
只有明确给出对称群生成元、节点置换及传输矩阵
\[
U_{\gamma,j}:K_j\to K_{\gamma j}
\]
并证明一个分量恒消失或两者相关，才能化成单个角方程。

“\(D_8\times K\)”记号也有歧义：\(K\) 已表示曲率核，而且现有记录甚至把 “\(D_8\) stabilizer” 写成 order \(4\)。应改记为 \(G_{\rm sym}\)，明确群的约定、阶数、生成元和各节点固定子群。又因
\[
H^4(\xi)=H^4(-\xi),
\]
自然角参数空间是
\[
S(K_j)/\{\pm1\}\cong\mathbb{RP}^1.
\]

## 4. \(O(t^3)\) 与 \(O(t^{5/2})\) 的警告是诚实且必要的

Ozuch 当前必要方程给出
\[
t_j\lambda_k^j+t_j^2\mu_k^j=O(t_{\max}^{5/2}).
\]
节点 \(i\) 的远场曲率响应为 \(O(t_i^2)\)，乘接收参数 \(t_j\) 后贡献
\[
O(t_jt_i^2)=O(t^3)
\]
（等尺度情形）。由于
\[
t^3=o(t^{5/2}),
\]
现有粗余项比待计算的三阶模式项更大；非零三阶系数本身不能从该估计推出阻碍或存在。

Step 93 的表述因此是诚实的。不过“对称性杀掉余项”必须精确表述为：整个投影残差在所有低于三阶的阶数上恒为零；仅仅知道残差具有群等变性远远不够。

同时，Ozuch §3.3 已提供更高阶近似度量的模板：加入 \(\bar h^4,\bar h^8\) 及 ALE 高阶 jets，把余项压到目标障碍以下。因此更稳健的路线是证明
\[
\Pi_{K_j}\mathfrak F_j(t)=t^3\mathcal C_j+o(t^3),
\]
最好达到 \(O(t^{3+\alpha})\)，而不应主要依赖尚未证明的奇偶消去。Remark 2.11 允许对数径向项，故还必须检查是否出现 \(t^3\log t\)。

## 5. 在计算三阶系数前仍有实质性缺口

1. **局部二阶核分量尚未全部消失。**  
   Lemma 2.14 只直接控制径向
   \[
   \mu_1=C\det(R^\pm|_{\xi^\perp}),
   \]
   对秩一块确为零；它不证明所有横向 \(\mu_k\) 消失。真正前提是
   \[
   \Pi_{K_j}\boldsymbol\mu_j(\xi_j)=0.
   \]
   Step 77 已承认 \(\mu_2,\mu_3\) 仍缺直接的 Biquard 公式核验。

2. **全局 \(O(t^2)\) 方程需同时处理。**  
   \(\nu_l\) 必须在所选对称扇区中消失，或通过 orbifold 变形 \(v_2\) 联立求解。现有摘录不足以证明任意手性图案的全部标量/非标量投影自动消失。

3. **投影平面本身会有 \(O(t_i^2)\) 变化。**  
   接收节点的常数 jet \(A_{ji,0}\) 改变正交标架及核方向。若始终使用未扰动的 \(\Pi_K\)，误差恰与目标系数同阶。应采用随扰动传输的投影，或显式加入 projector/frame correction。

4. **完整三阶项不只含节点对作用。**  
   还可能含自节点项、坐标归一化、求解补空间产生的非线性项及 \(v_2\) 项。Step 94 的
   \[
   K_{\rm adj}^{\rm principal}\approx-0.035445
   \]
   只是乘积背景某些谱通道的分量；其符号在加入 EH 规范、Bianchi 投影和标架传输前没有物理判定力。

5. **Step 77 的交换子矩阵有符号错误。**  
   对 \(A^T=-A\)、\(R=\operatorname{diag}(\Lambda,0,0)\)，
   \[
   [A,R]=AR-RA
   \]
   是对称矩阵；Step 77 展示的 \(1a/a1\) 项看起来是反对称的。不过其 \(K\to K\) 块为零这一结论仍成立。

6. **平坦环面公式只能作类比。**  
   Ozuch 显式 \(B_x^L\) 属于 \(\mathbb T^4/\mathbb Z_2\)，不能直接移植为 \(S^2\times S^2\) 系数；而
   \[
   P_{rq}=\frac{\mu_r+\mu_q}{2}-1
   \]
   也应按每个张量通道重新推导，不能作为所有通道的统一分母。

## 6. 最精确的下一目标

固定每个节点的手性 \(\epsilon_j\)、秩一方向 \(\kappa_j\)、核平面
\[
K_j=\kappa_j^\perp,
\]
以及明确的 orbifold charts、节点间标架传输和投影逆 \(P_{g_o}^{-1}\)。证明投影障碍具有展开
\[
\begin{aligned}
\Pi_{K_j}\mathfrak F_j
={}&t_j^2\Pi_{K_j}\boldsymbol\mu_j(\xi_j)\\
&+t_j\Pi_{K_j}\!\left[
D R_j(v_2)
+\sum_{i\ne j}t_i^2Q_{ji}(\xi_i)
+\mathcal S_j^{(2)}
\right]\Pi_{K_j}\xi_j
+\mathcal R_j,
\end{aligned}
\]
其中 \(\mathcal S_j^{(2)}\) 收集同阶自节点、标架、chart 和补空间修正，并证明
\[
\mathcal R_j=o(t_{\max}^3)
\]
或给出包括可能 \(t^3\log t\) 项的完整渐近。

对应的可核验子问题是：

1. 直接计算并证明选定等变扇区内
   \[
   \Pi_{K_j}\boldsymbol\mu_j(\xi_j)=0;
   \]
2. 求解全部二阶 \(\nu_l\) 方程并确定 \(v_2\)；
3. 计算完整物理形式
   \[
   B_{ji}(\xi_i)=\Pi_{K_j}Q_{ji}(\xi_i)\Pi_{K_j},
   \]
   包含 EH \(H^4\) 规范、Bianchi/gauge 投影、零/负模、商归一化和移动标架修正；
4. 用全兼容 degree-4 del Pezzo 行校准完整总响应；
5. 明确 \(G_{\rm sym}\) 的生成元及其在节点与 \(K_j\) 上的作用，再决定不变量方程究竟是一维还是二维；
6. 依 Ozuch §3.3 的高阶构造把投影余项压到 \(o(t^3)\)。

**总评：**Step 93 修正了一个真实且承重的错误；“秩一曲率 \(\Rightarrow\) 核平面方向问题、而非 \(e_1\) 临界尺度问题”是正确的核心结论。仍需收紧之处是：不能尚未证明就只保留异手性逐对响应，不能尚未做表示论就宣称只有一个角方程，也不能在 \(\mu_{2,3}\)、全局二阶投影和 \(o(t^3)\) 余项尚未解决时把任何三阶数值当作决定性物理系数。