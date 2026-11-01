# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 13,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step13_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step13_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the normalization-invariant rank-one reduction and the claimed accessibility bootstrap. Check: (1) The structural formulas: vertical Ric[33] = (-|C|² + 2tr(h) + 2|u|²)/2 with the correct sign, matching A03's tr(H) = 1 + ℓ²|F|²/4 (with the appropriate norm convention). (2) The static limit Spec(W+) = {1/3 - η_i} from the reduction output. (3) The bootstrap argument: is the claim that H ≥ 0 implies Ric_B ≥ -I correct? Is 3D Bishop-Gromov applicable? Does 4D cover noncollapse follow? (4) The gap: does the weighted RCD(-1,4) structure really fail to give ordinary base Ricci? Can any other route (4D arguments on the cover, Moser iteration, Bochner identities) close the gap? Assess what is rigorous and what remains conjectural.

## Integrated Scientific Memo

# 核验结论

## 1. 归一化降维与竖直 Ricci 分量

令
\[
g=q+v^2(dz+B)^2,\qquad e^3=v(dz+B),
\]
并定义
\[
u=d\log v,\qquad
h=\nabla^2\log v,\qquad
H=\frac{\nabla^2v}{v}=h+u\otimes u,
\]
\[
F=dB,\qquad C=vF,\qquad
|C|_{\Lambda^2}^2:=\sum_{a<b}C_{ab}^2.
\]

在几何约定 \(\operatorname{Ric}_g=-g\) 下，正确公式是
\[
\boxed{\operatorname{Ric}_g(e_3,e_3)
=-\operatorname{tr}H+\frac12|C|_{\Lambda^2}^2
=-\operatorname{tr}h-|u|^2+\frac12|C|_{\Lambda^2}^2.}
\]

因此 Einstein 方程给出
\[
\boxed{\operatorname{tr}H
=\operatorname{tr}h+|u|^2
=1+\frac12|C|_{\Lambda^2}^2.}
\]

所以任务中所引述的脚本输出
\[
\frac{-|C|^2+2\operatorname{tr}h+2|u|^2}{2}
=\operatorname{tr}H-\frac12|C|^2
\]
实际上等于 \(-\operatorname{Ric}_{33}\)，而非几何约定下的
\(\operatorname{Ric}_{33}\)。若脚本采用相反的 Riemann 曲率符号，则应同时将 Einstein 方程写为脚本意义下的 \(\operatorname{Ric}_{33}=+1\)。这很可能与文中已发现的 \(R_{abdc}\) / \(R_{abcd}\) 次序问题属于同类符号错误。

范数换算完全一致：
\[
C_{ab}C^{ab}=2\sum_{a<b}C_{ab}^2,
\]
故
\[
\frac12|C|_{\Lambda^2}^2
=\frac14C_{ab}C^{ab}
=\frac14v^2F_{ab}F^{ab}.
\]
于是
\[
\boxed{\operatorname{tr}H
=1+\frac14v^2F_{ab}F^{ab},}
\]
与 A03 的
\[
\operatorname{tr}H=1+\frac12|z|^2,
\qquad z=*C,
\]
严格匹配。

归一化本身是正确的：取
\[
z=\ell(p)\psi,\qquad v=\ell/\ell(p),\qquad B=\ell(p)A
\]
后，
\[
g=q+v^2(dz+B)^2,\qquad v(p)=1,
\]
局部度量系数不再含绝对周期 \(\ell(p)\)；\(\ell(p)\) 仅保留在未展开前的纤维周期中。

### 混合方程还需修正

A01 文中的
\[
\operatorname{div}(v^2F)=0
\]
权重不正确。与 A03 的
\[
dz=-2u\wedge z,\qquad \operatorname{div}z=\langle u,z\rangle
\]
相容的方程是
\[
\boxed{\operatorname{div}_q(v^3F)=0,}
\]
等价地
\[
\boxed{\delta_q(v^2C)=0}
\]
以及分量形式
\[
\boxed{\nabla^b C_{ab}+2u^bC_{ab}=0.}
\]
因此任何“加权调和二形式”估计必须使用正确的 \(v^3F\) 或 \(v^2C\) 权重，而不是 A01 所写的 \(v^2F\)。

---

## 2. 静态极限的 \(W^+\) 谱

当 \(C=0\) 时，磁性 Weyl 块消失，并且
\[
W_{a3b3}=\frac13q_{ab}-H_{ab}
\]
（手征选择可能交换 \(W^+\) 与 \(W^-\)）。若
\[
\operatorname{Spec}(H)=\{\eta_1,\eta_2,\eta_3\},
\qquad \operatorname{tr}H=1,
\]
则
\[
\boxed{\operatorname{Spec}(W^+)
=\left\{\frac13-\eta_i\right\}_{i=1}^3.}
\]

A01 脚本在 \(u=0\) 时验证的是 \(H=h\) 的特例；不变量公式应写成 \(H=\nabla^2v/v\)，因而也覆盖静态但 \(u\neq0\) 的点。

两项有效校验是：

* \(H^2\times H^2\)：
  \[
  \operatorname{Spec}(H)=(1,0,0)
  \quad\Longrightarrow\quad
  \operatorname{Spec}(W^+)=
  \left(-\frac23,\frac13,\frac13\right).
  \]
  因而“静态常谱必有 \(W^+=0\)”是错误的。

* 校准剖面
  \[
  \operatorname{Spec}(H)=
  \left(\frac12,\frac14,\frac14\right)
  \]
  给出
  \[
  \operatorname{Spec}(W^+)=
  \left(-\frac16,\frac1{12},\frac1{12}\right),
  \qquad |W^+|^2=\frac1{24}.
  \]

因此静态谱公式成立，但它本身不提供一般静态刚性；一般排除仍须依赖先前的 Derdziński Einstein-germ 论证。

---

## 3. \(H\ge0\)、Bishop–Gromov 与覆盖空间非塌缩

水平 Einstein 方程是
\[
\boxed{\operatorname{Ric}_q
=-q+H+\frac12C_{ac}C_b{}^c.}
\]
其中
\[
X^aX^bC_{ac}C_b{}^c
=\sum_c(X^aC_{ac})^2\ge0.
\]
所以代数蕴含
\[
\boxed{H\ge0\quad\Longrightarrow\quad \operatorname{Ric}_q\ge-q}
\]
完全正确。

但后续结论不成立。

### (a) 静态不推出 \(H\ge0\)

\(C=0\) 只给出
\[
\operatorname{tr}H=1.
\]
迹为正不能推出所有特征值非负。因此 route assessment 中“静态情形 \(H\ge0\)”并未得到证明；它只对列出的特定静态剖面成立。

### (b) Bishop–Gromov 不产生初始体积下界

由 \(\operatorname{Ric}_q\ge-q\) 得到的是相对体积比较；它可以把一个已知尺度的体积下界传递到更小尺度，却不能凭空给出固定尺度的绝对体积下界。具有统一 Ricci 下界的薄平坦环面已经说明塌缩仍可发生。

因此
\[
\operatorname{Ric}_q\ge-q
\not\Longrightarrow
\operatorname{Vol}_q B_r(p)\ge c r^3.
\]

### (c) 3 维曲率控制也不自动给 harmonic radius

即使已有 \(|\operatorname{Ric}_q|\le R\)，在没有体积比、注入半径或展开全部短环的局部覆盖时，也不能得到统一 harmonic radius。当前归一化覆盖只展开所选 circle 方向，并不自动展开基底中的其他短方向。

此外，现有方程实际上连 \(\operatorname{Ric}_q\) 的上界也没有：
\[
\operatorname{Ric}_q=-q+H+\frac12C^2
\]
中的 \(H\) 与 \(C^2\) 都可能很大。

### (d) 四维覆盖非塌缩是附加条件下的结论

若另有：

1. 固定尺度的基底体积下界；
2. \(v\) 的统一上下界，或至少 \(\int v\,dV_q\) 的下界；
3. 固定长度的展开纤维区间；

则
\[
dV_4=v\,dV_q\,dz
\]
确实给出四维覆盖球的体积下界。但这些前提未由 \(H\ge0\) 或 Ricci 下界推出。

故“静态 rank-one 情形已经闭合”应撤回；它至多是在额外基底非塌缩和两侧系数控制下成立的条件命题。

---

## 4. 加权 \(RCD(-1,4)\) 的实际含义

对商空间测度
\[
dm=v\,dV_q,
\]
相应的 \(N=4\) Bakry–Émery 张量是
\[
\boxed{\operatorname{Ric}^{4}_{q,v}
=\operatorname{Ric}_q-\frac{\nabla^2v}{v}
=\operatorname{Ric}_q-H.}
\]
四维 Ricci 下界因此只给出
\[
\operatorname{Ric}_q-H\ge-q,
\]
即加权 \(RCD(-1,4)\) 结构。

这提供的是相对于 \(v\,dV_q\) 的 doubling、Poincaré 和测度紧性，而不是：

* 普通 \(\operatorname{Ric}_q\) 的上下界；
* 普通 \(dV_q\) 的非塌缩；
* \(v\) 远离零；
* 三维光滑 harmonic radius；
* 四维覆盖的重构半径。

所以 A03 关于“加权结构不能代替普通基底 Ricci 控制”的判断是严格正确的，不只是技术性缺口。

---

## 5. 原 bootstrap 的具体失败点

### 加权 Maxwell 估计

即使改用正确方程
\[
dF=0,\qquad \operatorname{div}(v^3F)=0,
\]
要从 \(L^2\) 推出 \(L^\infty\) 仍需统一椭圆性、权重控制以及基底 Sobolev/几何常数。条件 \(v(p)=1\) 与每个解上 \(v>0\) 不给出序列一致的球内下界。

“正且连续，所以紧子集上 \(v\ge c\)”只能产生依赖于单个解的 \(c\)，不能产生定理所需的统一常数。

### \(v\) 的 Harnack/最大值原理

方程
\[
\Delta_qv=v\left(1+\frac12|C|^2\right)
\]
中的势正是尚未控制的 \(|C|^2\)。次调和性只说明内部最大值受边界控制，并不能从 \(v(p)=1\) 推出固定球上的统一上下界。

因此“先由次调和性控制 \(v\)，再控制 \(F\)，再用 Harnack”的循环没有被打破。

### 四维 Moser iteration

对基底函数 \(v\)，四维覆盖上有
\[
\Delta_{\hat g}v
=v\left(1+\frac12|C|^2+|u|^2\right),
\]
以及
\[
\Delta_{\hat g}\log v=1+\frac12|C|^2.
\]
Moser iteration仍需覆盖空间的 Sobolev 常数和势项积分控制；前者受塌缩影响，后者正是待估量。因此当前条件下不能闭合。

### 四维曲率能量与 smoothing

四维有界 Ricci 加“有界”归一化 \(L^2\) 曲率均值不足以给 harmonic radius。所引 smoothing 结果需要普适小量
\[
\frac{r^4}{\operatorname{Vol}B_r}
\int_{B_r}|\mathrm{Rm}|^2\le\varepsilon,
\]
而校准区域有非零背景曲率密度，现有输入只给有界而非小。

减去校准 Weyl 块的 gauge-covariant smoothing 是有意义的新方案，但当前材料中没有这样的定理。

### Chiral Bochner 路线

已验证结构
\[
a_\pm=u\mp\frac12z,
\qquad
W^\pm=-[\operatorname{sym}\nabla a_\pm+a_\pm\otimes a_\pm]_0,
\]
\[
da_+=a_+\wedge a_-,
\qquad
da_-=-a_+\wedge a_-
\]
准确捕捉了导数 twist。潜在 Bochner 恒等式必须同时控制：

\[
|\nabla a_\pm|^2,\qquad |a_+\wedge a_-|^2
\]
以及未被 \(W^\pm\) 的无迹部分控制的 trace modes
\[
\operatorname{div}a_\pm+|a_\pm|^2.
\]
现有 Weyl 能量不足以单独控制这些迹模；\(u\) 与 \(z\) 还可在一个手征组合中抵消。因此这是一条合理研究路线，但尚非证明。

---

## 6. 最终状态划分

### 已严格成立

1. 局部归一化消除绝对纤维长度，降维方程不依赖原周期。
2. 几何符号下
   \[
   \operatorname{Ric}_{33}
   =-\operatorname{tr}H+\frac12|C|^2.
   \]
3. Einstein 标量方程
   \[
   \operatorname{tr}H
   =1+\frac12|C|_{\Lambda^2}^2
   =1+\frac14v^2F_{ab}F^{ab}.
   \]
4. 静态公式
   \[
   \operatorname{Spec}(W^+)=\{1/3-\eta_i\}.
   \]
5. 代数蕴含
   \[
   H\ge0\Rightarrow \operatorname{Ric}_q\ge-q.
   \]
6. 加权商结构只控制
   \[
   \operatorname{Ric}_q-H,
   \]
   不控制普通基底 Ricci。
7. 导数 twist 以一阶主量进入磁性 Weyl 块，不能仅由 \(|C|\) 小来忽略。

### 必须修正

1. A01 所引脚本的 \(\operatorname{Ric}[33]\) 是几何 Ricci 的负号。
2. 混合方程权重应为
   \[
   \operatorname{div}(v^3F)=0,
   \]
   不是 \(\operatorname{div}(v^2F)=0\)。
3. Bishop–Gromov 不从 Ricci 下界产生固定尺度体积下界。
4. 静态性本身不推出 \(H\ge0\)。
5. “静态 rank-one 情形已闭合”及完整 accessibility theorem 均未证明。

### 精确剩余数学对象

仍缺少一个临界尺度的 coercive compactness/reconstruction 定理：在加权 \(RCD(-1,4)\) 商空间上，若约化 Einstein 方程成立、两手征 Weyl 块具有受控局部 \(L^2\) 均值且 \(W^+\) 校准残差趋零，是否能推出：

* 固定尺度的普通基底正则区及覆盖重构半径；或
* 可量化的迹模／导数 twist／商奇异性集中。

现有四维 Moser、标准 smoothing、普通 Bishop–Gromov 以及未闭合的 chiral Bochner 计算都尚未解决这一对象。