# TTCS Independent Branch Record

```json
{
  "step_id": 47,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/plans/route_assessment_step47_entropy_degree_theorem.md",
    "Sessions/S0910A01/workspace/scripts/step47_entropy_degree_comparison.py",
    "Knowledge/objects/papers/Differentiable-rigidity-under-Ricci-curvature-lower-bound--cfb4c9cdd3c7--65a5a48bd00c/object.md",
    "Sessions/S0910A01/staging/acquired/Extended_graph_4-manifolds__and_Einstein_metrics_36ca3f274012faba/content.md"
  ]
}
```

## Task

Verify the mathematical substance of the Step 47 entropy/degree-map note for Yau Problem 26. Check the Chern--Gauss--Bonnet derivation from ||Ric+g||_op<=delta, the scaling g'=(1+delta)g/3, the boxed degree comparison, the degree-one hyperbolic existence theorem using the actual Bessieres--Besson--Courtois--Gallot theorem, and the X#X threshold asymptotic delta~1/(4 chi(X)). Identify any hidden orientation, sign, quantifier, or theorem-statement issue. Also assess the extended-graph near-equality interpretation and the claim that the argument is target-dependent rather than dimension-uniform. Give exact mathematical corrections, not generic review prose.

## Output

# 科学核验备忘录

## 1. Chern–Gauss–Bonnet 计算

令
\[
A=g^{-1}(\operatorname{Ric}_g+g),
\qquad \|A\|_{\mathrm{op}}\le \delta .
\]
逐点取 \(g\)-正交基使 \(A\) 的特征值为 \(e_i\)，则 \(|e_i|\le\delta\)，而 Ricci 特征值为 \(-1+e_i\)。记 \(E=\sum_i e_i\)，则
\[
s_g=-4+E\le -4(1-\delta),
\]
所以在 \(\delta<1\) 时
\[
|s_g|\ge4(1-\delta).
\]
无迹 Ricci 部分满足精确恒等式
\[
|\operatorname{Ric}^{\circ}_g|^2
 =\sum_i\left(e_i-\frac E4\right)^2
 =\sum_i e_i^2-\frac{E^2}{4}
 \le 4\delta^2.
\]
因此
\[
\frac{s_g^2}{24}-\frac{|\operatorname{Ric}^{\circ}_g|^2}{2}
\ge
\frac{16(1-\delta)^2}{24}-2\delta^2
=
\frac23(1-2\delta-2\delta^2).
\]
这一步常数正确。令
\[
\delta_0=\frac{\sqrt3-1}{2},
\]
则 \(1-2\delta-2\delta^2>0\) 当且仅当 \(0\le\delta<\delta_0\)。由
\[
8\pi^2\chi(Y)
=\int_Y\left(|W|^2+\frac{s^2}{24}
-\frac{|\operatorname{Ric}^{\circ}|^2}{2}\right)d\mu
\]
得到
\[
\operatorname{Vol}_g(Y)
\le
\frac{12\pi^2\chi(Y)}
{1-2\delta-2\delta^2}.
\]
也随即得到：若这种度量存在且 \(\delta<\delta_0\)，则必有 \(\chi(Y)>0\)。

这里定向性并非 Chern–Gauss–Bonnet 这一步所必需；非定向情形可通过定向双覆盖得到同一公式。定向性真正用于整数度数和后面的签名公式。

## 2. 常数缩放与带度数比较

设
\[
g'=a g,\qquad a=\frac{1+\delta}{3}.
\]
常数缩放下 Levi-Civita 联络不变，因而作为 \((0,2)\)-张量
\[
\operatorname{Ric}_{g'}=\operatorname{Ric}_g.
\]
原假设给出
\[
-(1+\delta)g\le\operatorname{Ric}_g\le-(1-\delta)g,
\]
所以
\[
-3g'\le\operatorname{Ric}_{g'}
\le-\frac{3(1-\delta)}{1+\delta}g'.
\]
特别地，
\[
0\le \operatorname{Ric}_{g'}+3g'
\le \frac{6\delta}{1+\delta}\,g'.
\tag{2}
\]
四维体积按 \(a^2\) 缩放，故
\[
\operatorname{Vol}_{g'}(Y)
\le
\frac{4\pi^2}{3}\chi(Y)
\frac{(1+\delta)^2}{1-2\delta-2\delta^2}.
\]

对截面曲率为 \(-1\) 的闭实双曲四流形，
\[
\operatorname{Ric}_{g_0}=-3g_0,\qquad s=-12,\qquad W=0,
\]
所以
\[
\operatorname{Vol}_{g_0}(X)=\frac{4\pi^2}{3}\chi(X).
\]
因此对定向闭流形间的非零度数映射 \(f:Y\to X\)，\(k=\deg f\)，确有
\[
\frac{\operatorname{Vol}_{g'}(Y)}
{|k|\operatorname{Vol}_{g_0}(X)}
\le
\frac{\chi(Y)}{|k|\chi(X)}
F(\delta),
\qquad
F(\delta)=\frac{(1+\delta)^2}{1-2\delta-2\delta^2}.
\]
盒中公式完全正确。若 \(Y\) 或 \(X\) 非定向，整数度数这一表述不再直接成立；当前部分定理只处理带指定整数度数映射的定向流形。

## 3. BBCG 度数一结论

所引全文中真正使用的是 Theorem 1.3：
\[
\forall D>0\;\exists\varepsilon(4,D)>0
\]
使得对任意 \(\operatorname{diam}(X,g_0)\le D\) 的闭实双曲四流形，以及任意度数一映射 \(f:Y\to X\)，若某度量 \(q\) 满足
\[
\operatorname{Ric}_q\ge-3q,\qquad
\operatorname{Vol}_q(Y)
\le(1+\varepsilon(4,D))\operatorname{Vol}_{g_0}(X),
\]
则 \(f\) 同伦于微分同胚。论文摘要中的 “bounded below by \(-n(n-1)\)” 不是应采用的规范化；正文 Theorem 1.3 明确是 \(-(n-1)g\)。

取 \(q=g'\)。若 \(\chi(Y)\le\chi(X)\)，则
\[
\operatorname{Vol}_{g'}(Y)
\le F(\delta)\operatorname{Vol}_{g_0}(X).
\]
故在
\[
F(\delta)\le1+\varepsilon(4,D)
\]
时，BBCG 定理确实给出 \(f\simeq\phi\)，其中 \(\phi:Y\to X\) 为微分同胚；于是
\[
h=\phi^*g_0,\qquad \operatorname{Ric}_h=-3h.
\]

更精确的充分不等式其实是
\[
\frac{\chi(Y)}{\chi(X)}F(\delta)
\le1+\varepsilon(4,D);
\]
文中的 \(F(\delta)\le1+\varepsilon\) 是利用 \(\chi(Y)\le\chi(X)\) 后较简洁的版本。

由于 \(F\) 在 \([0,\delta_0)\) 上严格递增，
\[
F'(\delta)=
\frac{2(1+\delta)(2+\delta)}
{(1-2\delta-2\delta^2)^2}>0,
\]
BBCG 对应的最大数值可写为
\[
\delta_D=
\frac{
\sqrt{(4+2\varepsilon)^2+4(3+2\varepsilon)\varepsilon}
-(4+2\varepsilon)}
{2(3+2\varepsilon)},
\qquad \varepsilon=\varepsilon(4,D),
\]
且 \(\delta_D=\varepsilon/4+O(\varepsilon^2)\)。

若 \(\chi(Y)<\chi(X)\)，精确 BCG 体积不等式与盒中上界在
\[
\frac{\chi(Y)}{\chi(X)}F(\delta)<1
\]
时互相矛盾。若同时处于 BBCG 窗口，则 BBCG 还会给出微分同胚，与 Euler 特征数严格不等相冲突。

## 4. \(X\#X\) 的阈值

取标准挤压映射
\[
X\#X\longrightarrow X\vee X
\]
再接两个恒等映射的折叠映射 \(X\vee X\to X\)，可得到度数 \(2\) 的映射。需给两个 summand 取一致定向。四维连通和满足
\[
\chi(X\#X)=2\chi(X)-2.
\]
记 \(m=\chi(X)>1\)，则
\[
\frac{\chi(X\#X)}{2\chi(X)}
=1-\frac1m.
\]
而
\[
F(\delta)=1+4\delta+11\delta^2+O(\delta^3).
\]
方程
\[
\left(1-\frac1m\right)F(\delta)=1
\]
等价于
\[
(3m-1)\delta^2+(4m-2)\delta-1=0.
\]
其正根为
\[
\delta_*(m)
=
\frac{2}
{\,4m-2+\sqrt{16m^2-4m}\,}
=
\frac1{4m}+\frac5{64m^2}+O(m^{-3}).
\]
因此
\[
\delta_*(X)\sim\frac1{4\chi(X)}
\]
完全正确。

文中只写了严格不等号下的矛盾；等号处也可排除。因为此时上下体积估计迫使
\[
\operatorname{Vol}_{g'}(X\#X)
=2\operatorname{Vol}_{g_0}(X),
\]
BCG 等号情形会使该度数二映射同伦于二重 Riemannian covering。但二重覆盖必须满足
\[
\chi(X\#X)=2\chi(X),
\]
与 \(2\chi(X)-2\) 不符。因此 \(0\le\delta\le\delta_*(m)\) 均不可出现这种度量。若 \(m=1\)，则 \(\chi(X\#X)=0\)，Chern–Gauss–Bonnet 已排除全部 \(\delta<\delta_0\)。

脚本中的二分结果与上述根一致。两个代码细节是：

- `F(delta) <= 1 + 8*delta` 只在网格点上由 `assert` 测试；连续区间上的证明来自
  \[
  (1+8\delta)(1-2\delta-2\delta^2)-(1+\delta)^2
  =\delta(4-19\delta-16\delta^2)>0
  \]
  对 \(0\le\delta\le0.05\) 成立。
- `delta_threshold_connected_sum` 的实现按当前上端点适用于 \(m\ge2\)；\(m=1\) 需要单独处理。

BBCG Theorem 1.6 的任意非零度数版本在所给论文中只有定理陈述，证明被略去并指向 Bessières 早期处理。因此度数一结论由当前全文直接支持；Corollary 1.7 和任意度数微分刚性若要求自足推导，还需补入该任意度数证明。精确 BCG 体积不等式 Theorem 1.5 本身则可直接用于上述 \(X\#X\) 阈值。

## 5. Extended graph 四流形

对含 pure real-hyperbolic pieces 的情形，Di Cerbo 的 Lemmas 8–9 给出
\[
V:=\operatorname{Vol}_{\mathrm{Ric}}(M)
=\sum_i\operatorname{Vol}_{-1}(V_i),
\qquad
2\chi(M)=\frac{3}{2\pi^2}V,
\qquad
\tau(M)=0.
\]
代入前述 CGB 上界确有
\[
V\le\operatorname{Vol}_{g'}(M)\le V F(\delta).
\tag{3}
\]
左边来自 \(\operatorname{Ric}_{g'}\ge-3g'\) 和 \(V\) 的定义。

LeBrun 的等号结论只针对 \(\lambda<0\) 的 Einstein 度量。若从“任意 Einstein 度量”开始，还需补齐符号分支：

- \(\lambda>0\)：Myers 定理使 \(\pi_1(M)\) 有限，与其中的 \(\mathbb Z^3\) 冲突。
- \(\lambda=0\)：紧致 Ricci-flat 流形的基本群虚阿贝尔；extended graph 基本群的指数增长与此不相容。
- 因而只剩 \(\lambda<0\)，归一化到 \(\operatorname{Ric}=-3g\) 后，LeBrun 等号情形给出实双曲度量，再由 \(\mathbb Z^3\) 与 Preissmann 定理排除。

近等号部分需要一处实质性改写。仅凭 (3) 的体积接近，或体积熵接近等号，不能产生正的间隔：CSS 构造本身给出同一非双曲 extended graph 流形上的度量 \(q_j\)，满足
\[
|\sec_{q_j}|\le1,\qquad
\operatorname{Ric}_{q_j}\ge-3q_j,\qquad
\operatorname{Vol}_{q_j}(M)\to V.
\]
而 CSS 熵不等式又给出
\[
3\left(\frac{V}{\operatorname{Vol}_{q_j}(M)}\right)^{1/4}
\le h(q_j)\le3,
\]
所以 \(h(q_j)\to3\)。因此，普通的 Ricci 下界、体积接近 \(V\) 和熵接近 \(3\) 已由这些非双曲序列同时实现。

原始两侧 Ricci 夹逼还保留了额外的逐点信息，即式 (2)：
\[
\left\|g'^{-1}(\operatorname{Ric}_{g'}+3g')\right\|_{\mathrm{op}}
\le\frac{6\delta}{1+\delta}.
\]
真正相关的稳定性定理必须使用这一 Ricci 各向同性误差，或与之等价的局部几何信息；单纯的 \(\operatorname{Vol}_{\mathrm{Ric}}\) 或熵近等号不足以支持该推论。

对于没有 pure pieces 的情形，\(\chi(M)=0\)，而 CGB 被积式在 \(\delta<\delta_0\) 时有严格正下界，故直接得到矛盾。这部分给出的数值 \(\delta_0=(\sqrt3-1)/2\) 与具体靶流形无关。

## 6. 量词与靶流形依赖

量词结构确为
\[
\forall D>0\;\exists\varepsilon(4,D)>0,
\]
而不是
\[
\exists\varepsilon_4>0\;\forall D>0.
\]
BBCG 引言中的 Farrell–Jones 讨论明确说明，微分刚性常数不能脱离靶流形的“size”；直径依赖不是记号上的偶然。

同样，对 \(X\#X\) 的初等计算给出
\[
\delta_*(X)\sim\frac1{4\chi(X)}.
\]
沿高次数有限覆盖，Euler 特征数按覆盖次数增长，因此该数值趋于零。Corollary 1.7 中的 \(\varepsilon(X)\) 也是固定 \(X\) 的常数。故 Step 47 的度数映射机制确实产生了严格的固定靶流形结果，但它本身不产生只依赖维数的正夹逼宽度。