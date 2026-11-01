# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step105_cusp_channel_restored_and_cap_charge_theorem.md",
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Sessions/S1003A02/workspace/data/step105/cap_charge_check.json",
    "Sessions/S1003A01/workspace/notes/spirit_step91_global_reduction_and_carrier_scope.md"
  ]
}
```

## Task

Independently check the new A02 Theorem 105.Q/Corollaries 105.L and 105.H in the supplied note. Re-derive all signs, orientations, constants, and limiting arguments from the stated Theorem-G convention. Pay special attention to: boundary orientation in Q_+, whether C^2 boundary convergence controls eta as asserted; existence/order of the double limit defining c_j; whether volume convergence implies cap volume tends to zero; the cap contribution to LeBrun’s mixed estimate and the optimization leading to 9k+8 sum c_j <=3A; Dai–Wei’s adiabatic eta normalization; the formula c=4-r for an S3 Hopf cap; and the inference that a zero-charge -I4 cap must carry its odd form through energy-free collapse. Distinguish proved consequences under (E) from heuristic topology. If a statement needs repair, give the corrected statement and proof. Also assess whether a w2/spin or eta/Dirac argument can actually exclude the zero-charge four-class cap without assuming what is to be proved.

## Output

# 科学核验备忘录

## 1. 总结

从 Theorem G 的约定重新推导后，Theorem 105.Q 的主符号、Corollary 105.L 的常数
\[
9k+8\sum_jc_j\le 3A
\]
以及 \(S^3\)-Hopf cap 的
\[
c=4-r
\]
均正确。

需要四处修订：

1. 总 cap 体积由总体积收敛确定；单个 cap 的体积不必在固定 \(\rho\) 下收敛，更不等于整个尾部体积。
2. 因此前述标量能量和 \(W^+\)-能量最好用 \(\limsup_i\) 后再令 \(\rho\to0\) 表述；若希望保留逐 cap 的普通二重极限，需要再取子列，或加入逐 cap 体积收敛。
3. 105.H 若允许额外 charge \(4\) 的球 cap，显示公式漏掉了这些 cap 的 \(32\)-倍贡献；“carrying \(r_j\) classes”还需明确 \((\chi,\tau)=(1+r_j,-r_j)\)。
4. 零 charge 的 \(-I_4\) cap 并非总曲率能量为零：它有固定的
   \[
   C_-=20,\qquad \int|W^-|^2\longrightarrow40\pi^2.
   \]
   从自旋泡的偶格不能直接排除全局奇格；\(D_4\subset I_4\) 的指数二嵌入正好展示了这一点。

---

## 2. Theorem 105.Q 的符号与极限

令 \(L_\rho=\partial\Omega_\rho\)，取 \(\Omega_\rho\) 的外法向诱导定向。对相应 cap \(C_j^{(\rho)}\)，有
\[
\partial C_j^{(\rho)}=-L_\rho .
\]
记
\[
T_j=(2\chi+3\tau)(C_j).
\]
Theorem G 给出
\[
\widehat P(C_j)
 =C_+(C_j)-T_j+\mathcal Q_+(-L_\rho)
 =C_+(C_j)-T_j-\mathcal Q_+(L_\rho).
\]
所以
\[
C_+(C_j)
 =\widehat P(C_j)+T_j+\mathcal Q_+(L_\rho).
\]
由于
\[
0\le \widehat P(g_i;C_j)\le \widehat P(g_i;M)\to0,
\]
固定 \(\rho\) 后确有
\[
c_j(\rho):=\lim_{i\to\infty}C_+(g_i;C_j^{(\rho)})
 =T_j+\mathcal Q_+(L_\rho;g_\infty).
\]
因此 105.Q(1) 中的加号和截面定向均正确。

### \(C^2\) 收敛与 eta 项

拉回到固定截面后，诱导度量 \(h_i\to h_\infty\) 于 \(C^2\)。Euler transgression 和 \(T_{p_1}\) 都是二阶度量数据的局部积分，故连续。

奇签名算子 \(B_h\) 的核由调和偶次形式组成，其维数为 \(b_0+b_2\)，与度量无关。沿充分接近的度量路径，不会有额外特征值穿过零点。APS 圆柱公式或 eta 变分公式于是把 eta 差写成 gravitational Chern–Simons 差；该量在 \(C^2\) 收敛下趋于零。因此这里的 \(C^2\) 正则性足以推出
\[
\mathcal Q_+(L_\rho;g_i)\to\mathcal Q_+(L_\rho;g_\infty).
\]

### 外层极限的非循环证明

若两个 exhaustion 核满足
\[
\Omega_{\rho_1}\subset\Omega_{\rho_2},
\]
则相应 cap 满足 \(C_j^{(\rho_1)}\supset C_j^{(\rho_2)}\)。对两者之间位于 \(\Omega\) 内的壳层 \(A_j\)，能量可加性及局部 \(C^2\) 收敛给出
\[
c_j(\rho_1)
 =c_j(\rho_2)+C_+(g_\infty;A_j)\ge c_j(\rho_2).
\]
所以随着 exhaustion 核扩大，\(c_j(\rho)\) 单调下降且非负，因而
\[
c_j=\lim_{\rho\to0}c_j(\rho)
\]
存在。继而
\[
\lim_{\rho\to0}\mathcal Q_+(L_\rho;g_\infty)
 =c_j-T_j.
\]
这避免了原文“由第一式本身可知 \(\mathcal Q_+\) 收敛”的循环表述。多个端由同一个 cap 相连时，只需把壳层和 \(\mathcal Q_+\) 对所有相应截面求和。

---

## 3. Cap 体积与标量能量：所需修订

总体积无损给出的是
\[
\lim_{i\to\infty}\sum_j\operatorname{Vol}_{g_i}(C_j^{(\rho)})
 =\operatorname{Vol}_{g_\infty}(\Omega)
  -\operatorname{Vol}_{g_\infty}(\Omega_\rho).
\]
右侧在 \(\rho\to0\) 时趋于零。因此逐 cap 有
\[
\lim_{\rho\to0}\limsup_{i\to\infty}
\operatorname{Vol}_{g_i}(C_j^{(\rho)})=0.
\]
原文逐 cap 等于整个 \(\Omega\setminus\Omega_\rho\) 体积的陈述一般不成立；不同 cap 之间的微小体积可以随 \(i\) 重新分配。

不过证明只需要上式。由
\[
\int_{C_j}s_i^2
 \le 2\int_M(s_i-\bar s_i)^2
   +2\bar s_i^2\operatorname{Vol}_{g_i}(C_j)
\]
得到
\[
\lim_{\rho\to0}\limsup_i\int_{C_j^{(\rho)}}s_i^2=0.
\]
相应地，严谨的逐 cap 表述是
\[
\lim_{\rho\to0}\limsup_i
\left|
\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W^+_{g_i}|^2-c_j(\rho)
\right|=0.
\]
若对可数个 \(\rho\) 取子列，使所有逐 cap 体积收敛，则可恢复原文所写的普通二重极限，并得到
\[
c_j=\lim_{\rho\to0}\lim_i
\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W^+|^2.
\]

### 全局分解

固定 \(\rho\) 时，
\[
C_+(g_i;M)
 =C_+(g_i;\Omega_\rho)+\sum_jC_+(g_i;C_j^{(\rho)}).
\]
闭流形上的 Theorem G 给出
\[
C_+(g_i;M)=A-k+\widehat P(g_i)\to A-k.
\]
先令 \(i\to\infty\)，再以单调收敛令 \(\rho\to0\)，得到
\[
C_+(g_\infty;\Omega)=A-k-\sum_jc_j.
\]
因此 105.Q(3) 正确。

---

## 4. Corollary 105.L

记
\[
C=\sum_jc_j,\qquad
\int_\Omega s_\infty^2=96\pi^2x,\qquad
\int_\Omega|W^+_\infty|^2=2\pi^2y.
\]
由 Theorem 105.Q，
\[
x+y=A-k-C.
\]

### Cap 对 mixed functional 的贡献

在所有 cap 上求和，并用 Cauchy–Schwarz，
\[
\left|
\int_{\cup C_j}s_i|W_i^+|
\right|
\le
\left(\int_{\cup C_j}s_i^2\right)^{1/2}
\left(\int_{\cup C_j}|W_i^+|^2\right)^{1/2}.
\]
第一因子在二重极限中趋于零，第二因子有界。因此实际上有精确的广义二重极限
\[
\int_{\cup C_j}(s_i-\sqrt6|W_i^+|)^2
 \longrightarrow 12\pi^2C.
\]
所以正 charge cap 不能被当作 mixed functional 中的零贡献区域。若 \(c_j>0\)，cap 体积趋零而 \(W^+\) 的 \(L^2\) 能量不趋零，故 \(\sup|W^+|\to\infty\)；这推出曲率集中，但单凭 (E) 尚不能自动产生一个完整的光滑 rescaled bubble。

### Einstein 核上的优化

因为 \(s_\infty<0\)，
\[
\int_\Omega(s_\infty-\sqrt6|W^+|)^2
 \le
\left(\|s_\infty\|_2+\sqrt6\|W^+\|_2\right)^2
 =12\pi^2(\sqrt{8x}+\sqrt y)^2.
\]
Cauchy–Schwarz 给出
\[
(\sqrt{8x}+\sqrt y)^2\le9(x+y),
\]
其中常数 \(9\) 在 \(x:y=8:1\) 时取等。因此仅使用 \(x+y\) 时，
\[
\int_\Omega(s_\infty-\sqrt6|W^+|)^2
 \le108\pi^2(A-k-C).
\]
转移 LeBrun 不等式后，
\[
72\pi^2A
 \le108\pi^2(A-k-C)+12\pi^2C.
\]
化简即
\[
\boxed{9k+8C\le3A}.
\]

第二个不等式需要另行使用
\[
\int_Ms^2\ge32\pi^2A.
\]
Cap 标量能量消失后，
\[
96\pi^2x\ge32\pi^2A,
\qquad x\ge A/3.
\]
再由 \(x\le x+y=A-k-C\) 得
\[
k+C\le\frac{2A}{3}.
\]
因此该结论依赖 scalar estimate；mixed estimate 单独并不直接推出它。

---

## 5. Dai–Wei 归一化与 Hopf cap

对取 \(\partial C\) 定向的圆丛截面，记 Euler 数为 \(e_{\rm out}\)。Dai–Wei 的归一化为
\[
\mathcal H_{\partial C}
 =\frac12\,\mathrm a\!-\!\lim\eta
 =\frac{e_{\rm out}}3-\operatorname{sign}(e_{\rm out}),
\qquad \mathcal E_{\partial C}\to0.
\]
所以
\[
\mathcal Q_+(\partial C)
 =-3\mathcal H_{\partial C}
 =-e_{\rm out}+3\operatorname{sign}(e_{\rm out}).
\]
由于 Einstein 核的截面定向与 \(\partial C\) 相反，
\[
c=(2\chi+3\tau)(C)-\mathcal Q_+(\partial C)
 =(2\chi+3\tau)(C)
   +e_{\rm out}-3\operatorname{sign}(e_{\rm out}).
\]
这正是 105.Q 与 §3 之间的符号转换。

该归一化与模型一致：

- Taub–NUT 的 \(e_{\rm out}=-1\) 取向给出 \(c=4\)。
- 反向取向给出 \(c=0\)。
- Taub-bolt 给出 \(c=3\)。
- \(A_{m-1}\) multi–Taub–NUT，\(e_{\rm out}=m\)，给出 \(c=0\)。

表格最后一列对第一个 Taub–NUT 实际写的是
\[
\frac1{8\pi^2}\int|W^+|^2=1,
\]
而不是 \(C_+=1\)；对应的
\[
C_+=\frac1{2\pi^2}\int|W^+|^2=4.
\]
因此数值一致，但列标题宜改为“独立归一化曲率数据”。JSON 文件核对的是这些代数代入，并不单独验证 Dai–Wei 的谱公式。

### \(S^3\)-Hopf cap

若
\[
b_1=b_3=b_2^+=0,\qquad b_2^-=r,
\]
则
\[
\chi(C)=1+r,\qquad \tau(C)=-r,
\qquad (2\chi+3\tau)(C)=2-r.
\]
于是：

- \(e_{\rm out}=-1\)：
  \[
  c=(2-r)-1+3=4-r.
  \]
- \(e_{\rm out}=+1\)：
  \[
  c=(2-r)+1-3=-r.
  \]

由 \(c\ge0\)，含 \(r\ge1\) 的 cap 只能采用第一种手性，并有 \(r\le4\)。

---

## 6. Corollary 105.H 的修订形式

需明确每个 cap 均满足
\[
(\chi,\tau)=(1+r_j,-r_j),
\]
而不仅是非正式地“携带 \(r_j\) 个类”。

设有 \(N\) 个这样的 cap，\(\sum r_j=k\)，另有 \(B\) 个 \(e_{\rm out}=-1\) 的同调球 cap；每个此类球 cap 的 charge 为 \(4\)。则
\[
C=\sum_{j=1}^N(4-r_j)+4B=4N-k+4B.
\]
因此 105.L 给出
\[
9k+8C
 =k+32N+32B
 \le3A.
\]
原文的
\[
k+32N\le3A
\]
只有在额外球 cap 全部为 charge \(0\)，即 \(B=0\)，或仅将 charge \(4\) cap 的贡献舍去以获得较弱必要条件时成立。

当 \(B=0\) 时：

- \(r_j=1\)、\(N=k\)：
  \[
  33k\le3A,\qquad k\le A/11.
  \]
- \(r_j=4\)、\(N=k/4\)：
  \[
  9k\le3A,\qquad k\le A/3.
  \]

这些是曲率不等式与给定整数数据的相容条件，不构造相应退化。特别地，单个 \(r=4\) cap 在 \(A\ge12\) 时不与该不等式冲突，但存在性仍未由这些公式给出。

---

## 7. 零 charge 的 \(-I_4\) cap 与 \(w_2\)

对 \(r=4\)、\(e_{\rm out}=-1\)，有
\[
\chi=5,\qquad \tau=-4,\qquad c_+=0.
\]
因此在二重极限意义下
\[
\widehat P(C)\to0,\qquad
\int_Cs^2\to0,\qquad
\int_C|W^+|^2\to0.
\]

但另一手性并不消失。因为
\[
\mathcal Q_-(\partial C)
 =3\mathcal H_{\partial C}
 =e_{\rm out}-3\operatorname{sign}(e_{\rm out})=2,
\]
故
\[
c_-=(2\chi-3\tau)(C)-\mathcal Q_-(\partial C)
 =22-2=20.
\]
于是
\[
\frac1{2\pi^2}\int_C|W^-|^2\longrightarrow20,
\qquad
\int_C|W^-|^2\longrightarrow40\pi^2.
\]
零 \(c_+\) 仅表示 \(W^+\)、标量曲率和无迹 Ricci 的相应能量消失，并不表示总曲率能量消失。由于 cap 体积趋零而 \(W^-\) 能量固定，\(W^-\) 也必然发生曲率集中。

若另有标准的光滑 pointed rescaling 提取，则每个所得光滑泡满足
\[
\operatorname{Ric}=0,\qquad W^+=0.
\]
完整且单连通的此类泡为 hyperkähler，因而是 spin，紧支撑交叉格为偶格。可是 (E) 本身没有提供完整的 bubble-tree 分解、同调映射的本原性或所有拓扑均由这些泡生成。

### \(D_4\subset I_4\) 直接阻止简单的 \(w_2\) 排除

令
\[
I_4=(\mathbb Z^4,-\mathrm{Id}),\qquad
D_4=\{x\in\mathbb Z^4:\ \textstyle\sum_i x_i\equiv0\pmod2\}.
\]
则 \(D_4\) 是 \(I_4\) 的指数二偶子格。\(I_4\) 的特征向量可取
\[
K=(1,1,1,1).
\]
对每个 \(x\in D_4\)，
\[
K\cdot x\equiv\sum_i x_i\equiv0\pmod2.
\]
所以全局非零的 \(w_2\) 在 \(D_4\) 子格上可以限制为零。一个 spin 的 \(D_4\) 泡因此完全可能只看到偶子格，而奇的 unimodular 扩张由指数二 gluing 数据产生；它不必表现为另一个非单连通 Ricci-flat 泡。

相应地，原文“奇部分必须由 F-structure 塌缩区或非单连通 ASD Ricci-flat 部件携带”的二分说法尚未推出。可严格表述为：

> 若所有泡都是 spin，且它们的 \(H_2\) 像本原地生成 cap 的 \(H_2\)，则不能得到 \(-I_4\)。  
> 当前材料并未给出这种本原生成性质；\(D_4\subset I_4\) 正是可行的指数二代数模型。

### Dirac/eta 也没有现成矛盾

把 cap 用 \(B^4\) 封合得到 \(\#4\overline{\mathbb{CP}}^2\)。取特征类 \(K=(1,1,1,1)\)，则
\[
K^2=-4,\qquad \sigma=-4,
\]
闭流形 spin\(^c\) Dirac 指数为
\[
\operatorname{ind}D^+
 =\frac{K^2-\sigma}{8}=0.
\]
因此最直接的 spin\(^c\) 指数算术完全相容。签名 eta 已经被 cap-charge 恒等式吸收；Dirac eta 还依赖 determinant connection、纤维自旋 holonomy 和可能的 spectral flow，而这些数据不在 (E) 中。标量曲率只有 \(L^2\) 消失，也不足以应用点态 Lichnerowicz 消失论证。

所以，仅凭 (E)、\(w_2\) 和现有 eta 数据，不能排除零 charge 的四类 cap。可由 (E) 确定的是其手性能量分布；泡格的本原性、指数二 gluing 以及实际退化的存在仍未确定。