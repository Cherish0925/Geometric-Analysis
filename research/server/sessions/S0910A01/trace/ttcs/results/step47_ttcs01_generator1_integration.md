# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 47,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step47_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step47_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Using the Step 47 note and the actual sources, develop the strongest scientifically useful next formulations for the entropy/global-volume and exotic-smooth-structure directions toward the full Yau 26 proposition. In particular: (i) determine what normalized topology/entropy margin would be required for a uniform varying-target negative pinching theorem beyond fixed X; (ii) analyze whether Farrell--Jones real-hyperbolic exotic smoothings could become a strict counterexample route, separating what topology rules out for positive/zero/negative Einstein constants and what remains unknown; (iii) propose a few load-bearing theorem statements or calculations that would materially decide these routes. Do not invent literature or assert a no-Einstein theorem absent from the files.

## Integrated Scientific Memo

## 科学整合备忘录

### 一、变化目标下真正需要的“归一化余量”

先固定 Step 47 的四维实双曲情形。设  
\[
f:Y^4\to X^4,\qquad k=\deg f\neq0,
\]
其中 \(X\) 配备截面曲率 \(-1\) 的双曲度量 \(g_0\)。若
\[
\bigl\|g^{-1}(\Ric_g+g)\bigr\|_{\infty,\mathrm{op}}\le\delta,
\]
令
\[
g'=\frac{1+\delta}{3}g,\qquad
F(\delta)=\frac{(1+\delta)^2}{1-2\delta-2\delta^2}.
\]
则
\[
\Ric_{g'}\ge-3g',
\]
且 Step 47 的 Chern–Gauss–Bonnet 估计给出
\[
\frac{\Vol_{g'}(Y)}{|k|\Vol(X)}
\le
\frac{\chi(Y)}{|k|\chi(X)}F(\delta).
\tag{1}
\]

定义
\[
q_\chi(f)=\frac{\chi(Y)}{|k|\chi(X)},\qquad
R_{\Ric}(f)=
\frac{\Vol_{\Ric}(Y)}{|k|\Vol(X)}.
\]
由 BCG，
\[
R_{\Ric}(f)\ge1,
\]
而由 (1)，
\[
R_{\Ric}(f)\le q_\chi(f)F(\delta).
\tag{2}
\]

因此，若目标 \(X\) 允许变化，所需的不是固定的加法体积差或 Euler 差，而是**尺度无关的乘法余量**
\[
\Gamma(\mathcal C):=
\inf_{f\in\mathcal C}\frac{R_{\Ric}(f)}{q_\chi(f)}.
\tag{3}
\]
若
\[
\Gamma(\mathcal C)>1,
\]
则所有满足
\[
F(\delta)<\Gamma(\mathcal C)
\]
的近负 Einstein 夹逼度量均被排除。解方程 \(F(\delta)=\Gamma\) 得
\[
\delta_*(\Gamma)=
\frac{\sqrt{\Gamma(1+3\Gamma)}-(1+\Gamma)}
{1+2\Gamma}.
\tag{4}
\]

这给出了精确答案：**变化目标的维数一致结论至少需要一个固定的归一化乘法间隙，而不是随目标体积增长而消失的绝对间隙。**

一个已经可证的纯拓扑版本是：若存在固定 \(\alpha>0\)，使整个族满足
\[
q_\chi(f)\le1-\alpha,
\]
则由 (2) 不可能有
\[
F(\delta)<\frac1{1-\alpha}.
\]
相应阈值为
\[
\delta<
\delta_\alpha
=
\frac{-2+\alpha+\sqrt{4-\alpha}}{3-\alpha}
=
\frac{\alpha}{4}+O(\alpha^2).
\tag{5}
\]
所以应寻找的是**相对 Euler 短缺**，而非固定整数 Euler 短缺。

#### 熵版本需要修正

可以定义每个映射同伦类的归一化最小熵
\[
R_{\mathrm{ent}}(f):=
\inf_g
\frac{h(\widetilde Y,g)^4\Vol_g(Y)}
{3^4|k|\Vol(X)}.
\]
BCG 给出 \(R_{\mathrm{ent}}(f)\ge1\)。但不能仅由
\(h(g')\le3\) 和 (1) 推出
\(R_{\mathrm{ent}}\le q_\chi F(\delta)\)，因为这需要用同一个 \(g'\)：
\[
R_{\mathrm{ent}}(f)
\le
\frac{h(g')^4\Vol_{g'}(Y)}
{3^4|k|\Vol(X)}
\le q_\chi(f)F(\delta),
\]
此处才成立。更重要的是，对 \(Y\) 与双曲 \(X\) 同伦等价的 Farrell–Jones 光滑化，这一熵下确界等于双曲最小熵，因而不能区分光滑结构。故熵余量只能在排除了这些同伦等价 exotic smoothings 的受限类别中有希望一致为正。

#### \(X\#X\) 的精确退化

对度二映射 \(X\#X\to X\)，
\[
q_\chi=1-\frac1{\chi(X)}.
\]
BBCG 对每个固定 \(X\) 给出
\[
R_{\Ric}(X\#X\to X)\ge1+\varepsilon(X),
\]
所以真正需要的是
\[
\inf_X
\frac{1+\varepsilon(X)}
{1-1/\chi(X)}>1.
\tag{6}
\]
现有来源仅证明每个固定 \(X\) 的 \(\varepsilon(X)>0\)，并明确说明其依赖目标大小。沿大次数覆盖，\(1/\chi(X)\to0\)，而 Farrell–Jones 现象排除了把 BBCG 的微分刚性阈值做成完全与目标无关的可能。

RCD 稳定性结果也没有消除此障碍：其稳定定理仍含直径参数，而且主要输出接近双曲及覆盖型结论，不提供变化目标上的维数一致光滑结构间隙。

---

### 二、Farrell–Jones 实双曲 exotic smoothings：两种符号已排除，负号仍未解决

BBCG 所述实双曲 Farrell–Jones 序列可写成
\[
Y_i=X_i\#\Sigma,
\]
其中 \(X_i\) 是双曲流形的有限覆盖，\(Y_i\) 与 \(X_i\) 同胚但不同胚，并有截面曲率任意逼近 \(-1\) 的度量。若
\[
-1-\varepsilon_i\le K_{g_i}\le-1+\varepsilon_i,
\]
则
\[
-(n-1)(1+\varepsilon_i)g_i
\le \Ric_{g_i}\le
-(n-1)(1-\varepsilon_i)g_i.
\tag{7}
\]
故它们确实给出任意紧的负 Ricci 夹逼，而不仅是截面曲率信息。

设 \(Y_i\) 上存在 Einstein 度量 \(h\)，
\[
\Ric_h=\lambda h.
\]

#### 1. \(\lambda>0\) 被拓扑排除

Bonnet–Myers 推出 \(\pi_1(Y_i)\) 有限；但
\[
\pi_1(Y_i)\cong\pi_1(X_i)
\]
是无限双曲格点，矛盾。

#### 2. \(\lambda=0\) 也被排除

紧致 Ricci-flat 流形的基本群具有多项式增长（也可经 splitting/Bieberbach 得到有限指数的自由阿贝尔结构）；闭负曲率流形的基本群具有指数增长。因此不可能。

#### 3. 唯一未决的是 \(\lambda<0\)

归一化为
\[
\Ric_h=-(n-1)h.
\]
BCG 只给出
\[
\Vol_h(Y_i)\ge\Vol(X_i),
\tag{8}
\]
等号才迫使 \(h\) 为双曲度量并进而与 exotic 光滑结构矛盾。现有来源完全允许严格不等式，因此不能排除一个具有非零 Weyl 曲率的负 Einstein 度量。

最直接的缺失定理是：

> **双曲同伦型的 Einstein 光滑刚性。**  
> 若闭光滑 \(M^n\) 与闭实双曲 \(X^n\) 同伦等价，且  
> \[
> \Ric_h=-(n-1)h,
> \]
> 则 \(h\) 必须具有常截面曲率 \(-1\)。

或更弱但足够的体积形式：
\[
M\simeq X,\quad \Ric_h=-(n-1)h
\Longrightarrow
\Vol_h(M)\le\Vol(X).
\tag{9}
\]
结合 BCG 即得到等号与双曲刚性。也可用最大熵形式：
\[
M\simeq X,\quad \Ric_h=-(n-1)h
\Longrightarrow h(h)=n-1.
\tag{10}
\]
 supplied sources 均未证明 (9) 或 (10)。

#### 四维情形实际上闭合

若 \(M^4\) 同胚于实双曲 \(X^4\)，且
\[
\Ric_h=-3h,
\]
则 \(\chi(M)=\chi(X)\)、\(\tau(M)=0\)。Einstein CGB/签名公式给出
\[
\Vol_h(M)\le \frac{4\pi^2}{3}\chi(M)=\Vol(X).
\]
BCG 给出反向不等式，于是等号成立，\(h\) 为实双曲。故四维 exotic hyperbolic smoothing 若存在且不同胚，将自动无 Einstein 度量；但所给 Farrell–Jones 实双曲来源只明确覆盖高维构造，不能据此声称已有四维反例。

#### 对 Yau 26 量词的意义

一旦对某个固定维数的 Farrell–Jones 序列证明“无负 Einstein 度量”，则它们事实上无任何符号的 Einstein 度量。由 (7) 和常数缩放，它们可落入每个满足
\[
c<C,\qquad c<0
\]
的 Ricci 窗口：选
\[
\mu\in(c,\min\{C,0\}),
\]
把中心 Ricci 特征值缩放至 \(\mu\)，再令 \(\varepsilon_i\) 足够小即可。因此这会排除该维数中所有下端点 \(c<0\) 的候选 Yau 窗口。

它不能处理 \(c\ge0\) 的窗口；正 Ricci 已被无限基本群排除，非负 Ricci 也与该基本群的增长不相容。因此即使 exotic 路线成功，也只迫使潜在的 Yau 常数取 \(c_n\ge0\)，不会单独否定完整命题。

#### 复双曲来源不能替代实双曲紧夹逼

Kasilingam 只给出实维 \(14,16\) 中
\[
K\in[-4-\varepsilon,-1+\varepsilon].
\]
这仅推出
\[
-(n-1)(4+\varepsilon)g
\le\Ric\le
-(n-1)(1-\varepsilon)g,
\]
相对宽度不趋于零。要用于任意窄 Ricci 窗口，必须额外证明
\[
\left\|
g_\varepsilon^{-1}
(\Ric_{g_\varepsilon}+\kappa_n g_\varepsilon)
\right\|_{\infty,\mathrm{op}}\to0,
\tag{11}
\]
而所给来源没有这一结论。

---

### 三、最能决定两条路线的定理与计算

#### A. 变化目标的统一负夹逼定理应采用如下形式

对一类非覆盖映射 \(f:Y^4\to X^4\)，证明存在仅依赖维数的 \(\eta>0\)，使
\[
\frac{\Vol_{\Ric}(Y)}
{|\,\deg f\,|\Vol(X)}
\ge
(1+\eta)
\frac{\chi(Y)}
{|\,\deg f\,|\chi(X)}.
\tag{12}
\]
这正是 \(\Gamma>1\)。结合 (2) 立即产生维数一致的 Ricci 缺陷下界 (4)。

但不能对所有双曲同伦型 exotic smoothings 期待 (12)：它们与 \(X\) 同伦等价，并有任意近双曲度量，使相关最小体积/熵量逼近双曲值。故任何可行版本必须加入排除条件，或其右端含真正检测光滑结构的量。单纯 \(\chi,\tau,\pi_1\)、simplicial volume、最小熵都不足以区分 \(X\#\Sigma\) 与 \(X\)。

#### B. 四维 \(X\#X\) 是无需解决高维负 Einstein 存在性的备选族

\(X\#X\) 不承载任何 Einstein 度量：

* 正号：无限基本群；
* 零号：指数增长基本群；
* 负号：若归一化 \(\Ric=-3g\)，度二 BCG 给出
  \[
  \Vol_g(X\#X)\ge2\Vol(X).
  \]
  而 Einstein CGB 给出
  \[
  2\chi(X\#X)\ge\frac{3}{2\pi^2}\Vol_g(X\#X).
  \]
  因
  \[
  \chi(X\#X)=2\chi(X)-2,\qquad
  \Vol(X)=\frac{4\pi^2}{3}\chi(X),
  \]
  右边至少为 \(4\chi(X)\)，左边等于
  \(4\chi(X)-4\)，矛盾。

因此关键对象是尺度不变负 Ricci 缺陷
\[
\mathfrak p(M):=
\inf_{a>0,g}
\left\|
a^{-1}g^{-1}(\Ric_g+a g)
\right\|_{\infty,\mathrm{op}}.
\]
现有 CGB+BCG 只给出
\[
\mathfrak p(X\#X)\gtrsim\frac1{4\chi(X)},
\tag{13}
\]
沿覆盖退化。以下任一结论都会实质决定路线：
\[
\inf_X\mathfrak p(X\#X)>0,
\tag{14}
\]
或存在覆盖序列使
\[
\mathfrak p(X_i\#X_i)\to0.
\tag{15}
\]
(15) 将直接产生四维无 Einstein 且任意紧负 Ricci 夹逼的序列。

普通旋转对称颈不能实现 (15)。对
\[
dr^2+f(r)^2g_{S^3},
\]
在喉部 \(f'=0\)，令 \(x=f''/f,\ y=2/f^2\ge0\)，则 Ricci 特征值为
\[
\lambda_r=-3x,\qquad \lambda_t=y-x.
\]
相对目标 \(-3g\)，
\[
\inf_{x,y\ge0}
\frac13\max\{|{-3x+3}|,\ |y-x+3|\}
=\frac12.
\tag{16}
\]
所以若 (15) 成立，必须使用非旋转、各向异性或全局分散的拓扑过渡。

#### C. Farrell–Jones 路线的精确决定性对象

最小充分目标是高维版本的 (9)，或直接证明：

> 对某个实双曲 Farrell–Jones smoothing \(Y=X\#\Sigma\)，不存在  
> \[
> \Ric_h=-(n-1)h.
> \]

反方向也可研究一个局部解析存在定理：

> 若闭流形有截面曲率充分一致地接近 \(-1\)，则同一光滑流形承载负 Einstein 度量。

但 supplied sources 不支持该定理，且不能从截面夹逼直接宣称 Einstein 线性化具有目标无关的可逆常数。即使曲率零阶项接近双曲模型，谱隙、规范固定、注入半径及非线性估计仍需一致控制；有限覆盖的注入半径可以有基底给出的正下界，但 Farrell–Jones 拼接度量本身是否保留所需一致有界几何，来源没有给出。故该方向目前只能表述为待证的定量 Einstein 扰动定理，不能视为预期结论。

#### D. 最有价值的定量数据

对实双曲 Farrell–Jones 构造，应从原始构造提取
\[
\varepsilon_i,\qquad
\frac{\Vol(Y_i,g_i)}{\Vol(X_i)}-1,\qquad
\diam(X_i),\qquad
\inj(Y_i,g_i),
\]
随覆盖次数的关系。它们会直接量化 BBCG 阈值为何退化，并判断局部 Einstein 扰动方法是否可能具有统一常数。

对复双曲构造，首要计算不是继续使用 \([-4-\varepsilon,-1+\varepsilon]\)，而是直接计算 Ricci 张量，检验 (11)。

---

### 结论

变化目标的 entropy/global-volume 路线需要一个**相对双曲体积的固定乘法余量**；现有 BBCG 只提供固定目标余量，而 Farrell–Jones 序列表明纯同伦型熵量无法检测 exotic 光滑结构。实双曲 exotic smoothing 已由拓扑排除正、零 Einstein 常数，唯一缺口是负 Einstein 存在性。最具决定性的三个对象是：

1. 归一化统一间隙 (12)；
2. 高维双曲同伦型的负 Einstein 体积/熵刚性 (9) 或 (10)；
3. 四维 \(X_i\#X_i\) 的 Ricci 缺陷究竟满足统一正下界 (14)，还是可趋零 (15)。

这三者分别准确刻画了 global-volume 路线、exotic-smoothing 路线和四维替代路线目前尚未解决的核心数学量。