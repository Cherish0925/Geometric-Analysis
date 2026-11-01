# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 91,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step91_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step91_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 91 product-orbifold calculation. Read the Step 91 note and supporting scripts/data. Check: (1) whether the product-background odd receiver really reduces to the sparse second-jet formula with no V0/frame/background-curvature correction; (2) whether the checkerboard radial reduction correctly leaves only adjacent ordered pairs in the per-receiver equations; (3) whether the corrected spectral ledger repairs the Step 90 mistakes (m-parity quotient descent, factor trace-free minimum P=2, independent degrees) while preserving P>=1 on the K-odd quotient linear sector; and (4) whether the AB one-form heat computation and its normalization are mathematically plausible as a sector calculation, including any norm/factor/sign/tail caveats. State precisely what is verified and what remains unsupported for the full Ozuch coefficient and Yau-26.

## Integrated Scientific Memo

# Step 91 核验结论

## 1. 乘积背景上的奇接收器

在固定的乘积正规标架
\[
A=\{0,1\},\qquad B=\{2,3\},\qquad
\omega_2^+=e^{02}-e^{13},\quad
\omega_2^-=e^{02}+e^{13}
\]
下，结论成立。

乘积曲率只支撑于 \(01\) 和 \(23\) 二形式方向，因此
\[
\mathcal R_0\omega_2^\pm=0.
\]
故标架、Hodge 分解及二形式归一化的一阶变化所产生的项
\[
\langle\delta\omega,\mathcal R_0\omega_2^\pm\rangle
\]
全部消失。将
\[
(\delta R)_{abcd}
=\frac12(H_{ad,bc}+H_{bc,ad}-H_{ac,bd}-H_{bd,ac})
\]
与 \(\omega_2^\pm\) 收缩，按脚本的 `/8` 归一化再取半个手征差，得到
\[
\boxed{
R_{\rm odd}(H)=\frac12
\bigl(H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01}\bigr).
}
\]
这与 100 个独立对称 Hessian 基向量上的精确有理数检查完全一致。

在点态线性接收器意义下，\(V_1\) 不进入曲率变分；由协变二阶导数替换偏二阶导数产生的 \(R_0*h(0)\) 项，在上述混合指标收缩中也因乘积曲率支撑而消失。因此：

* **已核验：** 产品节点处的完整点态线性奇曲率接收器正是该稀疏二阶 jet 泛函，不含额外 \(V_0,V_1\)、标架或背景曲率项。
* **未由此核验：** 实际 gluing 图表中远离节点的 cutoff、Bianchi 修正或曲率参数子的积分贡献；这些属于源/全局构造，而不是上述点态接收器恒等式。

\(\ell=1\) coexact–coexact 检查也正确：九个乘积模中只有
\[
(*dZ_A)\odot(*dZ_B)
\]
给出 \(R_{\rm odd}=1\)；具有非零 \(V_0\) 的赤道模接收值为零。

---

## 2. Checkerboard 径向约化

对
\[
\varepsilon=(1,-1,-1,1),\qquad
\Delta_i=t_i\sum_jt_j^2(\varepsilon_i\varepsilon_j-1)K_{ij}^{11},
\]
乘子满足：

* \(i=j\) 时为 \(0\)；
* \(NN\leftrightarrow SS\)、\(NS\leftrightarrow SN\) 时为 \(0\)；
* 两节点恰在一个因子上不同，即相邻时为 \(-2\)。

所以恰有八个相邻**有序**对留下，并得到
\[
\begin{aligned}
\Delta_{NN}&=-2t_{NN}(t_{NS}^2K_{NN,NS}+t_{SN}^2K_{NN,SN}),\\
\Delta_{NS}&=-2t_{NS}(t_{NN}^2K_{NS,NN}+t_{SS}^2K_{NS,SS}),\\
\Delta_{SN}&=-2t_{SN}(t_{NN}^2K_{SN,NN}+t_{SS}^2K_{SN,SS}),\\
\Delta_{SS}&=-2t_{SS}(t_{NS}^2K_{SS,NS}+t_{SN}^2K_{SS,SN}).
\end{aligned}
\]
这部分是纯代数恒等式，已核验。

把所有相邻项替换成一个 \(K_{\rm adj}\) 仍是**条件性步骤**：必须先证明源和接收器标架、节点取向及因子交换下的归一化一致。现有 checkerboard 脚本只把这一点列为假设，并未证明。特别地，当 \(t_i\) 不相等时，对接收器求和不能替代四个径向方程。

“same-orbit companion”只是非严格称呼；这些节点并未被商作用互相识别。消失的真正原因仅是 \(\varepsilon_i\varepsilon_j=1\)。

---

## 3. 修正后的谱账本

三项 Step 90 修正确实正确：

1. 商生成元为同时的 \(\pi\)-旋转，故下降条件是
   \[
   (-1)^{m_A+m_B}=1,
   \]
   而不是 \(\ell_A+\ell_B\) 的奇偶性。

2. 因子 trace-free 块满足
   \[
   P=\frac{\ell_F(\ell_F+1)+\ell_O(\ell_O+1)}2-1,
   \]
   最小值为 \(P=2\)，而不是 \(4\)。

3. AB 一形式块中 \(\ell_A,\ell_B\) 独立，且
   \[
   P=\frac{\ell_A(\ell_A+1)+\ell_B(\ell_B+1)}2-1,
   \]
   最小值在 \((1,1)\) 为 \(P=1\)。

不过可执行账本的 TF 奇偶枚举并不完整：

* 第一因子上的 \(m=0\) magnetic tensor harmonic
  \[
  \operatorname{sym}_0\nabla(*dY_{\ell0})
  \]
  对 \(K\) 可为奇，且在 \(\ell=2\) 已下降；因此并非只有 \(m=2\) 才首次出现。其本征值仍为 \(P=2\)，故不改变下界。
* 固定的 \(K=K_A\) 只反射第一因子。以第二因子支撑、第一因子为常数的 TF 模是 \(K\)-偶的；脚本标签 `AA_or_BB_factor_tracefree` 混合了这两种不同的 \(K\)-奇偶情形。因子交换把 \(K_A\) 变为 \(K_B\)，不能在保持同一个 \(K\) 时直接等同。

尽管如此，
\[
\boxed{P\ge1}
\]
在 \(K\)-奇且可下降的线性张量扇区上仍然成立：已知 \(P=-1\) 的 shape 模 \(g_A-g_B\) 以及相关零模均为 \(K\)-偶；AB 块从 \(1\) 开始，TF 块从 \(2\) 开始。为了把它升级为完全自足的谱定理，仍需给出完整的 scalar/trace、gauge、electric/magnetic tensor-harmonic 分解；当前 `scalar_trace_block_candidate` 的统一 \(P\) 公式本身不足以证明这种完备性。

---

## 4. AB 一形式热计算

### 内部归一化

对无 \(1/2\) 的对称积
\[
h=\alpha_A\otimes\beta_B+\beta_B\otimes\alpha_A,
\]
令
\[
A_{ab}=\partial_b\alpha_a,\qquad B_{\mu\nu}=\partial_\nu\beta_\mu.
\]
稀疏接收器化为
\[
R_{\rm odd}(h)
=-\frac12(A_{01}B_{10}+A_{10}B_{01}),
\]
与代码一致。

若生成标量球谐在整球上 \(L^2\)-归一，则整覆盖空间上的无平均对称积范数为
\[
2\lambda_A\lambda_B.
\]
商积分再除以 \(2\)，故
\[
\|h\|_{\mathcal O}^2=\lambda_A\lambda_B,
\]
正是代码使用的分母。若改用带 \(1/2\) 的 \(\odot\) 约定，所有因子都会改变；因此当前数值只在“无平均对称积”约定下成立。

只有 \(m=0,2\) 标量模在极点具有非零 Hessian，故这一模式筛选对于该接收器是完备的。南极正向标架 \((X,-Y)\) 给出的符号
\[
m=0,c2:\ (-1)^\ell,\qquad s2:\ -(-1)^\ell
\]
也一致。

### 轴向锚点

对轴向模，
\[
Ph=h,\qquad
\|h\|_{\mathcal O}^2=\frac{64\pi^2}{9},\qquad
R_{NN}=1,\quad R_{NS}=-1.
\]
采用 Step 89 主部归一化
\[
S_{\rm odd}=\frac{\pi^2}{2}R_{\rm odd}
\]
后，相邻贡献为
\[
\frac{\pi^2}{2}\frac{R_{NN}R_{NS}}{\|h\|^2}
=-\frac9{128},
\]
热正则化后为 \(-9e^{-\tau}/128\)，与表中全部轴向数据吻合。这同时检查了扇区内的符号、商范数、源因子和本征值。

### 极限及其可靠程度

相邻情形下，\(m=2\) 的四种 polarization 对每个次数对发生精确的符号抵消；剩下的是 \(m=0\) coexact–coexact 双级数。其可写为
\[
K_\tau^{AB}
=\frac1{512}\sum_{\ell,k\ge1}(-1)^k
\frac{(2\ell+1)(2k+1)\lambda_\ell\lambda_k}
{\frac12(\lambda_\ell+\lambda_k)-1}
e^{-\tau[\frac12(\lambda_\ell+\lambda_k)-1]}.
\]
进一步利用 \(e^{-\tau p}/p=\int_\tau^\infty e^{-sp}\,ds\)，它分解为一个普通极点热核导数与一个对踵点热核导数的乘积；后者在短时间指数衰减。这为 \(\tau\downarrow0\) 的 Abel 极限提供了数学上可信的机制。

因此
\[
K_{\rm adj}^{AB}\approx-0.03144249732
\]
是可信的 **AB 主源扇区实验值**。但现有 `last_10_ellA_shell_abs_sum` 不是严格的二维尾界，也没有控制 \(\tau\downarrow0\) 误差的区间包络。各 polarization 子和随 \(\tau\to0\) 很大，而总和依赖精确抵消；应以逐次数的解析恒等式证明该抵消，并给出热核或级数余项估计，才能把小数升级为严格值域。

---

## 5. 对 Ozuch 系数及 Yau–26 的实际含义

当前没有得到完整的 Ozuch 相邻系数。至少仍缺：

* 从真实 ALE 边界配对推出分布源及其总符号、\(\mathbb Z_2\) 各向同性因子；
* cutoff、Bianchi/gauge 修正及所选伪逆投影；
* AA/BB trace-free 扇区，以及 gauge 修正诱导的 scalar/trace 成分；
* 所有相邻有序系数在规范化标架下相等的证明；
* \(m=2\) 抵消和热尾的严格估计；
* 将该 Green 响应匹配到
  \[
  t_i\lambda_i+t_i^2\mu_i
  \]
  中 \(t_it_j^2\) 项，并给出 \(o(t^3)\) 的投影余项。已有 \(O(t_{\max}^{5/2})\) 估计过粗，不能分辨 \(t^3\) 层。

所以 AB 值的符号或非零性目前不能转移给完整径向系数；其他扇区可能加强、改变或抵消它。Step 91 严格确认的是点态接收器与 checkerboard 相邻对约化，并修复了主要谱规则；AB 数值是合理但尚未严格封闭的单扇区计算。

即使最终得到非零完整相邻系数，它也只约束该乘积 orbifold 附近的特定对称反解奇分支，不排除 \(\#_3(S^2\times S^2)\) 上其他 Einstein 度量，更不证明或证伪关于所有维数和所有闭流形的 Yau 第 26 题命题。