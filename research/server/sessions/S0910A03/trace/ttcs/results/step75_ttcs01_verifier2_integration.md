# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 75,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step75_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step75_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently read the Step-75 full-residual computation as a mathematical numerical experiment. Check whether the Gaussian Ricci component formulas and orthonormal normalization in the active scripts match g=dr^2+e^{2a}dz^2+e^{2b}dx^2+e^{2c}dy^2; whether the validated Step-69 Yamabe sign and center data are used consistently; whether boundary bases really impose the center and exit jets described; whether all five independent Ricci components enter; and whether the reported locations and sizes support only the stated finite-spectral interpretation. Identify any concrete formula, normalization, basis, or inference error that would change the scientific reading. Also assess whether the center-shape computation supports approach to the exact lower value 3 within its sampled reciprocal-warp family, without treating it as proof of a global infimum.

## Integrated Scientific Memo

# Step-75 数值实验核验结论

## 1. Ricci 分量与正交归一化正确

对
\[
g=dr^2+e^{2a}dz^2+e^{2b}dx^2+e^{2c}dy^2,\qquad E=\Ric_g+3g,
\]
在正交标架
\[
e_{\hat r}=\partial_r,\quad e_{\hat z}=e^{-a}\partial_z,\quad
e_{\hat x}=e^{-b}\partial_x,\quad e_{\hat y}=e^{-c}\partial_y
\]
中，两个活动脚本使用的五个独立分量为
\[
\begin{aligned}
E_{\hat r\hat r}&=3-a_r^2-a_{rr}-b_r^2-b_{rr}-c_r^2-c_{rr},\\
E_{\hat r\hat z}&=e^{-a}\!\left[a_r(b_z+c_z)-b_rb_z-c_rc_z-b_{rz}-c_{rz}\right],\\
E_{\hat z\hat z}&=3-a_r^2-a_rb_r-a_rc_r-a_{rr}\\
&\quad+e^{-2a}(a_zb_z+a_zc_z-b_z^2-b_{zz}-c_z^2-c_{zz}),\\
E_{\hat x\hat x}&=3-a_rb_r-b_r^2-b_rc_r-b_{rr}\\
&\quad+e^{-2a}(a_zb_z-b_z^2-b_zc_z-b_{zz}),\\
E_{\hat y\hat y}&=3-a_rc_r-b_rc_r-c_r^2-c_{rr}\\
&\quad+e^{-2a}(a_zc_z-b_zc_z-c_z^2-c_{zz}).
\end{aligned}
\]
它们逐项吻合 `step70_ricci_T2inv.json`。尤其：

- \(rz\) 坐标分量乘 \(e^{-a}\) 得到正交分量是正确的；
- \(zz,xx,yy\) 中的 \(e^{-2a}\) 因子正确；
- 在该对角、仅依赖 \(r,z\) 的对称类中没有遗漏其他非零分量；
- 两脚本确实都把五个分量放入目标函数；
- 对 \(E_{\hat r\hat z}\) 使用 \(\sqrt2\) 权重，使平方目标成为正交 Frobenius 范数；
- 由 \((\hat r,\hat z)\) 的 \(2\times2\) 块特征值以及 \(E_{\hat x\hat x},E_{\hat y\hat y}\) 计算 operator norm 的公式正确。

未发现会改变结论的 Ricci 符号或归一化错误。

## 2. Step-69 Yamabe 符号正确，但“精确中心”实际是谱投影中心

对
\[
h_f=dz^2+e^{2f}dx^2+e^{-2f}dy^2,\qquad q=u^4h_f,
\]
有 \(R_{h_f}=-2(f')^2\)，故 \(R_q=-6\) 等价于
\[
-8u''-2(f')^2u=-6u^5,
\qquad
u''=\frac34u^5-\frac14(f')^2u.
\]
`step69_collapsed_koiso_center.py` 和中心形状搜索均使用这一正确符号。

核心脚本写成
\[
L=l_0+\log\cosh r+\rho(r)G+F,
\]
其中
\[
\rho(0)=\rho'(0)=0,\quad \rho''(0)=1,
\]
而所有自由模式在中心为 \(O(r^4)\)。因此
\[
L(0)=l_0,\qquad L_r(0)=0,\qquad
L_{rr}(0)=I+G.
\]
代码取 \(G=\Ric_{q_0}^{\sharp}+2I\) 的傅里叶投影，连同
\((\log\cosh r)''|_0=1\)，恰给出
\[
L_{rr}(0)=\mathcal P_{K_z}(\Ric_{q_0}^{\sharp}+3I).
\]
所以代码中看似反常的 `center_ric + 2` 实际正确。

但注记中的“固定精确 Step-69 中心/Koiso 二阶 jet”需要限定为：

> 精确固定其 \(K_z=5\) 离散傅里叶投影，而非精确固定连续 Step-69 函数。

JSON 明确给出投影中心的
\[
\|R+6\|_{\infty,\mathrm{grid}}=1.1863\times10^{-3},
\]
中心 Einstein 分量最大约 \(2.96\times10^{-3}\)。记录的
`second_jet_error_sup ≈ 10^{-15}` 仅验证构造的二阶导数与同一投影数组一致，不验证其与连续中心完全一致。这个措辞修正会改变“exact”的科学含义，但不改变有限谱实验的定性解读。

此外，活动脚本依赖但材料未提供的 `step75_full_residual_core_search.py` 定义了 `yamabe_center` 和基础 Ricci 例程；因此这里能核验符号、可见公式和输出一致性，但不能逐行审计该导入实现。

## 3. 边界基底的实际约束

### Core-entry 基底

局部模式 \(x^4e^{-x^2}\) 及全局模式
\[
s^4T_j(2s^2-1)
\]
均为偶函数且在 \(r=0\) 消失到二阶以上，故确实保持：

- 中心度量；
- 反射条件 \(L_r(0)=0\)；
- 投影后的 Koiso 二阶 jet。

外端没有精确 Dirichlet 或 Neumann 条件。第二阶段仅软惩罚
\[
L_r(R)\approx(1,1,1),\qquad \Ric(q_R)\approx0,
\]
且始终允许 \(d_r(R)=b_r(R)-c_r(R)\ne0\)。全局 Chebyshev 模式在外端的值与导数具有秩二变化，因此在截断的每个 \(z\)-模上可独立调整外端值和一阶导数。这里“free exit flux”的描述成立。

### Germ-to-entry 基底

令 \(x=r-T_\ast\)。所有修正是 \(O(x^2)\)，故只强制
\[
L(T_\ast)=L_{\rm germ},\qquad
L_r(T_\ast)=S_{\rm germ}.
\]
它没有固定 \(L_{rr}(T_\ast)\)，更没有固定更高 jet。因此这不是平滑 germ 的完整延拓参数化，而仅是 \(C^1\) 接口匹配。JSON 中内端 \(E_{zz},E_x,E_y\) 达到约 \(16\)–\(23\)，主要正是因为外侧二阶导数可与 germ 的 Einstein 加速度不一致；不能把这些峰值解释成已存 germ 本身的约束误差。

该脚本还有一个实质性的外端基底退化。对
\[
v_j(s)=s^2\cos(j\pi s)
\]
有
\[
v_j'(1)=\frac{2}{R-T_\ast}v_j(1)
\]
对所有 \(j\) 相同。长区间时局部高斯模式在外端指数微小，因而全局模式几乎把外端修正值和导数锁在同一关系中，不能充分独立调节 exit metric 与 shape。这可能显著影响 \(R=6\) 的外端数据。

## 4. 数值结果只能作有限谱、未收敛实验解读

Core-entry residual-only 的采样 operator sup 为
\[
16.0268,\quad16.0348,\quad15.9641
\]
（\(R=2,4,6\)），峰值分别位于
\[
r=0.1957,\quad0.1875,\quad0.1875.
\]
soft-entry 仍约为 \(16\)。\(R=6\) 时虽达到
\[
\|S-I\|_\infty=0.106,\qquad
\|\Ric(q_R)\|_\infty=0.181,
\]
全 Ricci 缺陷没有降低。

Germ-to-entry residual-only 为
\[
23.5201,\quad22.1245,\quad21.5961,
\]
峰值在 \(r=0.15,0.15,0.225\)；soft-entry 亦约 \(22\)–\(23\)。这些数字与 JSON 和注记相符。

不过它们甚至不能解释为相应有限基底内的残差下界：

1. 所有求解均因达到 `max_nfev` 停止，而非达到驻点；部分 optimality 仍高达 \(12.5\)。
2. 优化目标是按 \(dr/R\) 或 \(dr/(R-T_\ast)\) 加权的平均 Frobenius \(L^2\)，不是 operator sup。
3. 固定宽度的内区随 \(R\) 增大在目标中被系统性降权。
4. 例如 \(R=2\) 的 carrier operator sup 为 \(12.78\)，优化后反而升到 \(16.03\)，尽管平均目标下降。
5. 仅在 \(N_z=32\)、约 \(29\)–\(31\) 个径向点上报告采样 supremum；没有独立稠密网格或 off-grid 复核。

因此最强的合法结论只是：

> 这些短程、加权 \(L^2\)、有限谱且未收敛的迭代没有消除中心附近的点态残差峰。

它们既不证明几何转变不可能，也不证明当前有限基底本身存在约 \(16\) 或 \(22\) 的残差底限。

另外：

- `normal_identity_pointwise_sup` 是把 \(E_{rr}\) 定义代回后的代数恒等式检查，接近机器零并非独立数值验证。
- \(R=6\) 时 `normal_budget_quad_sup` 达 \(10^4\)，说明含 \(e^{2r}\) 的加权积分恒等式在该粗网格上有严重求积/消去误差；不能把这个诊断量当作已数值解析。

## 5. 中心形状搜索确实支持“趋近 3”，但不证明极限或全局下确界

中心形状脚本中的共形 Ricci 公式以及
\[
P=\Ric_q^\sharp+3I
\]
均正确。在三维且 \(R_q=-6\) 时，与方向 \(e_i\) 互补的截面曲率满足
\[
K_i=-P_i.
\]
故代码
```python
posK = maximum(-P, 0)
```
正确测量采样最大正截面曲率。

单模数据
\[
\begin{array}{c|ccccc}
A&1&2&3&5&8\\ \hline
\max K_+&5.32335&4.33353&3.74435&3.28337&3.12623
\end{array}
\]
以及三模搜索
\[
f=19.3837\sin z-0.56964\sin2z+3.26556\sin3z,
\qquad \max K_+=3.03297037
\]
都从上方靠近解析定理给出的下界 \(3\)。因此它们有力支持：

> 在已采样的 reciprocal-warp/Yamabe 家族中，高振幅形状正在逼近精确下界 \(3\)，而非产生趋零的初始收缩。

但有三项必要限定：

- 优化所用 \(p=16\) 平滑代理值约 \(2.666<3\)，它不是 supremum；有意义的是稠密网格直接最大值 \(3.03297\)。
- `upp` 由 ODE 右端直接重算，随后又用于 Yamabe 和标量残差，所以 \(10^{-15}\) 残差主要是代数自洽检查，不是独立的 BVP 插值误差估计。
- 没有给出网格加密序列、独立二阶微分或振幅趋无穷的分析证明。

因此该计算不证明 \(3\) 在此傅里叶家族中的确切下确界或可达性，更不证明所有 \(T^3\) 度量的全局下确界。注记所列 \(A=10,15\) 数值也不在所提供 pilot 脚本的 baseline 列表或 JSON 中，不能由当前材料独立复现。

## 总判定

没有发现五分量 Ricci 公式、正交归一化、Step-69 Yamabe 符号或 core-entry 中心 jet 构造的实质错误。需要修正或强化披露的具体事项是：

1. “精确 Step-69 中心”实际为 \(K_z=5\) 投影中心；
2. germ 接口只匹配 \(0\) 阶和 \(1\) 阶 jet，未匹配二阶 Einstein jet；
3. germ 的长区间外端基底近乎耦合值与导数；
4. \(16/22\) 是粗网格、平均目标、达到迭代上限时的采样值，而非优化下界；
5. 中心形状数据支持 sampled-family 中从上方接近 \(3\)，但机器级残差并非独立误差认证，也不构成下确界证明。

这些修正不推翻 Step-75 注记的谨慎结论，反而进一步限制其科学含义：真正有严格数学效力的是解析中心下界与精确通量障碍；全残差计算目前只是未解析中心 jet cascade 的有限谱数值观察。