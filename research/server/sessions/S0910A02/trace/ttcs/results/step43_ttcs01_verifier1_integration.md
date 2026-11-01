# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 43,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step43_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step43_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step-43 correction to Route A. Read the new Step-43 note, Step-42 mode-projection note/data, the orientation bookkeeping data, and the cited Ozuch/LeBrun-Ozuch/Catino-Dameno source objects. The scientific question is: is the correction sound that det R_+=0 for KE limits is not a ceiling but the orientation-compatible side, while b_+>1 over a KE limit forces reversed EH bubbles testing R_-? Check source fidelity, orientation dictionary, topology/betti bookkeeping for A1/EH bubbles, the claim that Derdzinski-type rigidity does not follow from finitely many singular-point constraints, and the route allocation away from immediate high-order Lambda>0 obstruction theory. Identify any overclaim that would mislead the next research step.

## Integrated Scientific Memo

# 核验结论

Step 43 的**核心定向修正是正确的**，但必须收窄为如下精确陈述：

> 对取复定向的正 Kähler–Einstein 四维极限，
> \[
> R_+=W_++\frac{\Lambda}{3}I
> \]
> 具有谱 \((\Lambda,0,0)\)，所以 \(\det R_+=0\) 自动成立；这只说明存在与该定向兼容的 EH 参数方向通过第一障碍。反向 EH 泡检验的是 \(R_-\)，Kähler 恒等式并不控制它。若在纯 \(A_1\)/EH 拓扑模型中目标 \(b_+>b_+(O)\)，则必须引入正平方、即反向定向的 EH 类，因此相应奇点必须满足 \(R_-\) 的第一障碍。

这不是 Route A 的“天花板”，但也**尚未形成排除定理**。最重要的未决点是：拓扑只迫使反向泡的数量，不保证可用奇点处 \(\det R_-\neq0\)；而 \(S^2\times S^2\) 乘积模型恰有 \(\det R_-=0\) 处处。

## 1. 定向与第一障碍

Ozuch 源文直接给出
\[
\lambda_k(\zeta^\pm)
 =c\big\langle R^\pm(p)\zeta^\pm,\zeta^\pm_{(k)}\big\rangle .
\]
因此，固定 EH 参数时，真正必要的向量条件是
\[
R^\pm(p)\zeta^\pm=0.
\]
允许改变 \(\zeta^\pm\) 后，其存在性条件才是
\[
\det R^\pm(p)=0.
\]

对应关系经源文核验无误：

- 通常定向
  \[
  H^4(\zeta^+)=-\frac{\rho(\zeta)^-\circ\zeta^+}{2r^4}
  \]
  检验 \(R_+\)；
- 反向定向
  \[
  H^4(\zeta^-)=-\frac{\zeta^-\circ\rho(\zeta)^+}{2r^4}
  \]
  检验 \(R_-\)。

因此 Step 43 所说“\(\zeta^+\) 检验 \(R_+\)，\(\zeta^-\) 检验 \(R_-\)”忠于来源。

但“KE 自动满足所有定向兼容 EH 泡的第一障碍”仍略强。因为
\[
R_+=\operatorname{diag}(\Lambda,0,0),
\]
只有
\[
\zeta^+\in\ker R_+=\Lambda^2_{+,0}
\]
的方向通过障碍；具有 Kähler 形式分量的 \(\zeta^+\) 不通过。正确措辞是：

> KE 极限在兼容侧自动满足第一障碍的**行列式/存在性条件**，而非每一个 EH 参数方向都可行。

## 2. KE 曲率块计算

复定向下
\[
\operatorname{spec}(W_+)
 =\left(\frac{2\Lambda}{3},-\frac{\Lambda}{3},-\frac{\Lambda}{3}\right),
\qquad
\operatorname{spec}(R_+)=(\Lambda,0,0).
\]
故 \(\det R_+=0\) 及二维核均正确。

另一手征块是模型依赖的：

- Fubini–Study \(\mathbb{CP}^2\)：
  \[
  W_-=0,\qquad R_-=\frac{\Lambda}{3}I,
  \]
  所以
  \[
  \det R_-=\frac{\Lambda^3}{27}\ne0;
  \]
  反向 EH 泡在每一点都被第一障碍排除。

- 等半径 \(S^2\times S^2\)：
  \[
  \operatorname{spec}(R_+)=\operatorname{spec}(R_-)=(\Lambda,0,0),
  \]
  所以两侧行列式均为零。这说明反向侧并非普遍障碍，尤其在 Route A 的自然乘积极限中可能完全失效。

- 一般 KE 曲面若
  \[
  \operatorname{spec}(W_-)=(a,b,-a-b),
  \]
  则
  \[
  \det R_-=
  \left(a+\frac{\Lambda}{3}\right)
  \left(b+\frac{\Lambda}{3}\right)
  \left(-a-b+\frac{\Lambda}{3}\right).
  \]
  这是一个真实但仅点态的标量条件。

## 3. \(A_1\)/EH 拓扑与 Betti 数

通常定向 EH 的紧支撑二阶类平方为负，贡献
\[
(\Delta b_+,\Delta b_-)=(0,1);
\]
反向后平方变正，贡献
\[
(\Delta b_+,\Delta b_-)=(1,0).
\]

对仅由 \(A_1\)/EH 替换形成的光滑化，沿 \(\mathbb{RP}^3\) 作 Mayer–Vietoris，实系数下得到交叉形式分裂
\[
H^2(M;\mathbb R)
 \cong H^2(O;\mathbb R)\oplus\bigoplus_j\mathbb R[E_j].
\]
若 \(N_+\) 为通常定向泡、\(N_-\) 为反向泡，则
\[
b_+(M)=b_+(O)+N_-,
\qquad
b_-(M)=b_-(O)+N_+.
\]

因此若
\[
M=\#_k(S^2\times S^2),\qquad b_\pm(M)=k,
\]
并假设 \(b_+(O)=1\)，则
\[
N_-=k-1,\qquad N_+=k-b_-(O).
\]
Step 43 JSON 的各行与这些公式及签名关系一致；负泡数标记为不可行也是正确的。

需要两项限定：

1. “恰有 \(k-1\) 个反向 EH 泡”只适用于**纯 EH 模型**。一般 ALE 或泡树中，正确的不变量是
   \[
   \sum_Y b^{\mathrm{cpt}}_+(Y)=k-1,
   \]
   未必是 \(k-1\) 个独立 EH 泡。

2. \(b_+(O)=1\) 不应从 LeBrun–Ozuch 的 admissible 定理直接导入非 admissible 情形。对正 KE orbifold，这通常可由 orbifold Hodge 理论、正 Ricci 导致 \(H^{2,0}=0\) 及 Hodge 指标定理证明，但 Step 43 尚未提供这段源级论证。因此表格结论目前应明确写成“假设 \(b_+(O)=1\)”。

LeBrun–Ozuch 的“expected topology”使用继承定向下的 Kähler ALE 块，因而只增加负平方方向并保持 \(b_+=1\)。所以 \(b_+(M)>1\) 确实迫使 expected topology 失败；这一结构性解释是可靠的。

## 4. 拓扑强迫不等于已经得到障碍

这是对后续研究最关键的限定。拓扑只能说明至少需要若干反向泡，而每个反向泡必须位于满足
\[
R_-(p)\zeta^-=0
\]
的奇点。要由此推出矛盾，还需证明：

- 每个候选奇点均有 \(\det R_-(p)\ne0\)；或
- 满足 \(\det R_-=0\) 的候选奇点数量/容量不足以承载所需反向泡；或
- 即使行列式为零，实际核方向与拓扑所需 gluing 参数不相容。

目前这些都未建立。特别是乘积 \(S^2\times S^2\) 上 \(\det R_-=0\) 处处，因此“\(b_+>1\) 强迫反向泡”本身不构成第一阶排除。

故 Route A 的第一阶问题应被理解为**必要条件与模型筛选器**，而不是接近完成的 obstruction theorem。

## 5. Derdziński/Catino–Dameno 不能由有限点条件触发

Step 43 对此判断正确。反向泡仅给出有限多个点上的
\[
R_-(p_j)\zeta_j^-=0,
\quad\text{即}\quad
W_-(p_j)\zeta_j^-=-\frac{\Lambda}{3}\zeta_j^-.
\]
这既不给出全局特征线，也不给出特征值重数条件。

相比之下：

- LeBrun–Ozuch 的条件要求 \(W^+\) 的谱结构几乎处处成立、存在全局正性调和自对偶形式，或 \(\det W^+>0\) 处处；
- Catino–Dameno 要求最大特征值处处简单，或满足统一谱隙。

即使 Einstein 度量解析，解析函数在有限点为零也不推出恒等为零。因此从有限奇点上的 \(\det R_\pm=0\) 推出 conformally Kähler/Hermitian 刚性没有依据。

## 6. Step 42 模态投影仍只是框架

下列代数是正确的：
\[
a''+\frac3\rho a'-\frac8{\rho^2}a=0
\]
的根为 \(2,-4\)，Wronskian 为
\[
W(\rho)=-6\rho^{-3},
\]
且若
\[
a(\rho)=A\rho^2+B\rho^{-4},
\]
则
\[
A=\frac{16a(2R)-a(R)}{63R^2}.
\]

但最关键的解析接口尚未证明：在仅有
\[
\|\operatorname{Ric}(g_i)-\Lambda g_i\|_{L^\infty}\to0
\]
及 \(C^{1,\alpha}\cap W^{2,q}\) neck 正则性时，Bianchi-gauge Einstein 方程是否真的投影为该标量 ODE，并满足
\[
|S_i|\le C\delta_i
\]
且所有非线性、规变换和角向模耦合误差均可控。

此外必须投影到三个 EH Jacobi 场，得到完整向量条件
\[
R^\pm(p)\zeta^\pm=0.
\]
单一二次配对
\[
\langle R^\pm\zeta^\pm,\zeta^\pm\rangle=0
\]
在 \(R^\pm\) 不定时并不推出核条件。

Step 42 所称该方法“同样可读出任意高阶障碍”也属过度主张。高阶 Ozuch 障碍包含共振、非线性交互、全局 Einstein 变形及多泡耦合，不能由一次 \(l=2\) Wronskian 提取直接覆盖。

## 7. 路线分配判断

暂不立即投入宽泛的正 \(\Lambda\) 高阶障碍计划是合理的，因为手征错误应先修复，且当前最基础的近 Einstein 第一障碍桥尚未成立。不过不应把高阶路线无限推迟：

- 若候选极限像 \(\mathbb{CP}^2\)，\(R_-\) 可在第一阶排除反向泡；
- 若候选极限像 \(S^2\times S^2\)，第一阶两侧均退化，此时必须使用更强的 rank-one/二阶 Ozuch 条件或其他全局机制。

因此合理的科学顺序是：先完成近 Einstein 情形的完整三分量手征投影；随后按具体极限判断第一阶是否非空。若 \(R_-\) 已在所需点有核，高阶分析便不再是可选项。

## 必须删除或改写的误导性表述

1. Step 42 JSON 中
   > “The Ozuch obstruction is ALWAYS satisfied for KE orbifolds — they can always be desingularized in principle.”

   应改为：

   > 对复定向兼容的 EH 插入，KE 恒等式使第一障碍的行列式条件自动成立；这既不涵盖反向插入，也不蕴含任何实际 desingularization，更不处理高阶障碍。

2. “\(b_+>1\) forces reversed EH bubbles”应改为：

   > 在纯 \(A_1\)/EH 分裂且 \(b_+(O)=1\) 的模型中，\(b_+(M)>1\) 强迫反向 EH 类；一般情形只强迫 ALE 泡树携带相应总正交叉秩。

3. “排除 EH 泡即可使近圆 orbifold 极限光滑”不成立，除非同时排除其他 \(\Gamma\)、其他 ALE 填充和泡树。

4. Step 43 的“自动满足第一障碍”应明确为**存在某个核方向**，不是任意 gluing 参数均满足。

综上，Step 43 成功修正了最主要的手征误判；其可靠成果是一个精确的 \(A_1\)/EH 必要条件框架。尚未闭合的核心对象是：近 Einstein 序列的三分量弱模态投影定理，以及具体 KE orbifold 上可承载所需反向泡的 \(R_-\) 核点与核方向的计数。