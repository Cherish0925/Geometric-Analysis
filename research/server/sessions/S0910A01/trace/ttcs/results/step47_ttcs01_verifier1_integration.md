# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 47,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step47_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step47_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematical substance of the Step 47 entropy/degree-map note for Yau Problem 26. Check the Chern--Gauss--Bonnet derivation from ||Ric+g||_op<=delta, the scaling g'=(1+delta)g/3, the boxed degree comparison, the degree-one hyperbolic existence theorem using the actual Bessieres--Besson--Courtois--Gallot theorem, and the X#X threshold asymptotic delta~1/(4 chi(X)). Identify any hidden orientation, sign, quantifier, or theorem-statement issue. Also assess the extended-graph near-equality interpretation and the claim that the argument is target-dependent rather than dimension-uniform. Give exact mathematical corrections, not generic review prose.

## Integrated Scientific Memo

# Step 47 数学核验与精确修订

## 1. Chern–Gauss–Bonnet 推导正确

设
\[
A=g^{-1}(\Ric_g+g),\qquad \|A\|_{\mathrm{op}}\le \delta,
\]
其特征值为 \(e_i\in[-\delta,\delta]\)。则 \(\Ric_g\) 的特征值为 \(-1+e_i\)，并且
\[
s_g=-4+\sum_i e_i.
\]
当 \(\delta<1\) 时，
\[
s_g\le -4(1-\delta)<0,\qquad |s_g|\ge 4(1-\delta).
\]
无迹 Ricci 张量满足精确恒等式
\[
|\Ric_g^\circ|^2
=\sum_i\left(e_i-\frac14\sum_j e_j\right)^2
=\sum_i e_i^2-\frac14\left(\sum_i e_i\right)^2
\le 4\delta^2.
\]
故
\[
\frac{s_g^2}{24}-\frac{|\Ric_g^\circ|^2}{2}
\ge \frac23(1-\delta)^2-2\delta^2
=\frac23(1-2\delta-2\delta^2).
\]
在
\[
0\le\delta<\delta_0:=\frac{\sqrt3-1}{2}
\]
时右端严格为正。由
\[
8\pi^2\chi(Y)
=\int_Y\left(|W|^2+\frac{s^2}{24}
-\frac{|\Ric^\circ|^2}{2}\right)d\mu
\]
得到
\[
\boxed{\;
\Vol_g(Y)\le
\frac{12\pi^2\chi(Y)}
{1-2\delta-2\delta^2}.
\;}
\]
因此此类度量存在时自动有 \(\chi(Y)>0\)。

这一步不要求 \(Y\) 可定向；Gauss–Bonnet 对闭非定向四流形同样成立，也可由定向双覆盖推出。可定向性在后面的整数度数与签名论证中才是必要假设。

---

## 2. 缩放及盒中度数比较正确

令
\[
g'=ag,\qquad a=\frac{1+\delta}{3}.
\]
常数缩放不改变 Levi-Civita 联络，所以作为 \((0,2)\)-张量
\[
\Ric_{g'}=\Ric_g.
\]
原夹逼等价于
\[
-(1+\delta)g\le \Ric_g\le -(1-\delta)g,
\]
故
\[
-3g'\le\Ric_{g'}
\le-\frac{3(1-\delta)}{1+\delta}g'.
\]
特别地，缩放后不仅有 BBCG 所需的下界，而且保留
\[
\boxed{\;
0\le \Ric_{g'}+3g'
\le \frac{6\delta}{1+\delta}\,g'.
\;}
\tag{2}
\]
四维体积按 \(a^2\) 缩放，因此
\[
\Vol_{g'}(Y)
\le \frac{4\pi^2}{3}\chi(Y)
F(\delta),
\qquad
F(\delta):=
\frac{(1+\delta)^2}{1-2\delta-2\delta^2}.
\]
若 \((X,g_0)\) 为截面曲率 \(-1\) 的闭实双曲四流形，则
\[
\Ric_{g_0}=-3g_0,\quad s=-12,\quad W=0,
\]
从而
\[
\Vol_{g_0}(X)=\frac{4\pi^2}{3}\chi(X).
\]
故对闭定向四流形之间的非零度数映射 \(f:Y\to X\)，\(k=\deg f\)，确有
\[
\boxed{\;
\frac{\Vol_{g'}(Y)}
{|k|\Vol_{g_0}(X)}
\le
\frac{\chi(Y)}{|k|\chi(X)}F(\delta).
\;}
\tag{3}
\]
这里必须明确：通常整数度数要求源、靶均闭、连通且带定向。若欲覆盖非定向情形，必须改用局部系数度数或适当的定向双覆盖，不能原样写 \(k\in\mathbb Z\)。

展开式为
\[
F(\delta)=1+4\delta+11\delta^2+O(\delta^3).
\]

---

## 3. BBCG 度数一存在结论成立，但应按实际定理表述

所给全文中直接适用的是 BBCG Theorem 1.3：

> 对每个 \(n\ge3\) 和 \(D>0\)，存在 \(\varepsilon(n,D)>0\)，使得若  
> \((X,g_0)\) 是直径不超过 \(D\) 的闭实双曲 \(n\)-流形，  
> \(f:Y\to X\) 为度数一映射，并且 \(Y\) 上有度量 \(q\) 满足
> \[
> \Ric_q\ge -(n-1)q,\qquad
> \Vol_q(Y)\le(1+\varepsilon(n,D))\Vol_{g_0}(X),
> \]
> 则 \(f\) 同伦于微分同胚。

论文摘要中的“Ricci bounded below by \(-n(n-1)\)”是无量纲/排版不规范的说法；应采用正文的张量不等式
\[
\Ric_q\ge -(n-1)q.
\]

取 \(n=4\)、\(q=g'\)。若额外假设
\[
\chi(Y)\le \chi(X),
\]
则由 (3)
\[
\Vol_{g'}(Y)\le F(\delta)\Vol_{g_0}(X).
\]
所以
\[
F(\delta)\le1+\varepsilon(4,D)
\]
足以推出 \(f\) 同伦于某微分同胚 \(\phi:Y\to X\)。于是
\[
h=\phi^*g_0,\qquad \Ric_h=-3h.
\]

更精确而较弱的充分条件是
\[
\frac{\chi(Y)}{\chi(X)}F(\delta)
\le1+\varepsilon(4,D).
\]

必须注明：

1. \(\chi(Y)\le\chi(X)\) 是额外拓扑假设，不能由度数一映射自动推出。
2. 若最后得到微分同胚，则必有 \(\chi(Y)=\chi(X)\)。
3. 当 \(\chi(Y)<\chi(X)\) 且
   \[
   \frac{\chi(Y)}{\chi(X)}F(\delta)<1,
   \]
   BBCG/BCG 的精确下界
   \[
   \Vol_{g'}(Y)\ge\Vol_{g_0}(X)
   \]
   与 CGB 上界直接矛盾。因此这一分支是“不存在该 pinched metric”，而不是产生新的 Einstein 流形。
4. 该结果本质上是微分刚性蕴含：它证明满足这些条件的 \(Y\) 已经是双曲靶流形，而不是在新的拓扑类型上构造 Einstein 度量。

---

## 4. 任意度数定理的证据等级

BBCG Theorem 1.5 明确给出并引用 BCG 的任意非零度数体积不等式：
\[
\Vol_q(Y)\ge |\deg f|\Vol_{g_0}(X),
\qquad \Ric_q\ge -(n-1)q,
\]
且等号当且仅当 \(f\) 同伦于相应次数的局部等距覆盖。

BBCG Theorem 1.6 则陈述了任意非零度数的微分刚性窗口，但本文明确省略其证明，并引用 Bessières 的任意度数处理。因此：

- 度数一存在定理由 BBCG Theorem 1.3 直接支撑；
- 任意度数的**体积下界及等号刚性**可安全使用 Theorem 1.5；
- 任意度数的**近等号微分刚性**和依赖它的 Corollary 1.7，在当前文件中只有定理陈述而无完整证明；若要求自足证明，需补入 Bessières 的论证。

故 Step 47 将可靠主结论限制为度数一是正确的。

---

## 5. \(X\#X\) 阈值与端点修正

给两个 summand 一致定向。挤压
\[
X\#X\longrightarrow X\vee X
\]
后在两个楔和分支上各取恒等映射，得到度数 \(2\) 的映射
\[
f:X\#X\to X.
\]
四维连通和满足
\[
\chi(X\#X)=2\chi(X)-2.
\]
令 \(m=\chi(X)\)，则
\[
\frac{\chi(X\#X)}{2\chi(X)}
=1-\frac1m.
\]
结合 (3) 与 Theorem 1.5 的下界，若
\[
\left(1-\frac1m\right)F(\delta)<1,
\]
则矛盾。

阈值方程等价于
\[
(3m-1)\delta^2+(4m-2)\delta-1=0,
\]
其正根为
\[
\boxed{\;
\delta_*(m)
=\frac{2}
{4m-2+\sqrt{16m^2-4m}}
=\frac1{4m}+\frac5{64m^2}+O(m^{-3}).
\;}
\]
因此
\[
\delta_*(X)\sim\frac1{4\chi(X)}
\]
完全正确。

原文只在严格不等式下声称矛盾，但端点也可排除。若
\[
\left(1-\frac1m\right)F(\delta)=1,
\]
上下界迫使 BCG 体积等号成立，于是该度数二映射同伦于二重 Riemannian covering；然而二重覆盖要求
\[
\chi(X\#X)=2\chi(X),
\]
与
\[
\chi(X\#X)=2\chi(X)-2
\]
矛盾。故对 \(m>1\)，实际上
\[
0\le\delta\le\delta_*(m)
\]
全部不可能。

若 \(m=1\)，则 \(\chi(X\#X)=0\)，CGB 已直接排除所有
\[
\delta<\delta_0.
\]
脚本的二分函数应注明其正常使用范围为 \(m\ge2\)。

---

## 6. Extended graph 近等号解释需加强

对含 pure real-hyperbolic pieces 的闭 extended graph 四流形，Di Cerbo 给出
\[
V:=\Vol_{\Ric}(M)
=\sum_i\Vol_{-1}(V_i),
\qquad
2\chi(M)=\frac{3}{2\pi^2}V,
\qquad
\tau(M)=0.
\]
因此
\[
\frac{4\pi^2}{3}\chi(M)=V.
\]
若存在 Step 47 的 pinched metric，则缩放后的 \(g'\) 满足
\[
\Ric_{g'}\ge-3g',
\]
从而由 \(\Vol_{\Ric}\) 定义及 CGB 上界，
\[
\boxed{\;
V\le \Vol_{g'}(M)\le V F(\delta).
\;}
\tag{4}
\]

但不能仅从 (4) 或熵近等号推导双曲近刚性。事实上，Di Cerbo 引用的 CSS 构造本身提供非双曲 extended graph 流形上的度量 \(q_j\)，使
\[
|\sec_{q_j}|\le1,\qquad
\Ric_{q_j}\ge-3q_j,\qquad
\Vol_{q_j}(M)\to V.
\]
熵不等式还给出
\[
3\left(\frac{V}{\Vol_{q_j}(M)}\right)^{1/4}
\le h(q_j)\le3,
\]
所以 \(h(q_j)\to3\)。因此以下数据的同时近等号本身不具有刚性：

- 仅有 \(\Ric\ge-3g\)；
- \(\Vol\to\Vol_{\Ric}\)；
- \(h(g)\to3\)。

真正区别 Step 47 假设的是缩放后仍有逐点各向同性误差 (2)：
\[
0\le \Ric_{g'}+3g'
\le\frac{6\delta}{1+\delta}g'.
\]
所以若要从 extended graph 情形导出正 pinching gap，所需稳定性定理必须实质利用这一双侧 Ricci 近 Einstein 信息，或等价的局部几何控制；“\(\Vol_{\Ric}\) 或熵等号的普通近刚性”不足。

### 精确 Einstein 排除的符号分支

Di Cerbo 的 LeBrun Lemma 7 只直接处理负标量 Einstein 度量。若独立复述“不存在任何 Einstein 度量”，需补齐：

- \(\lambda>0\)：Myers 定理给出有限基本群，与所含 \(\mathbb Z^3\) 矛盾；
- \(\lambda=0\)：需使用紧致 Ricci-flat 流形基本群虚阿贝尔，或直接依照 Di Cerbo 对 Hitchin–Thorpe 等号及基本群增长的处理；
- \(\lambda<0\)：归一化为 \(\Ric=-3g\)，LeBrun 等号推出实双曲，再由 \(\mathbb Z^3\) 与 Preissmann 定理排除。

此外，“含 pure piece 即有 \(\mathbb Z^3\)”应保留 Di Cerbo 证明中“非平凡图分解/多于一个顶点”等结构条件；孤立闭双曲单顶点不能被错误纳入该矛盾。

对无 pure pieces 的情形，\(\chi(M)=0\)，而 CGB 被积式在
\[
\delta<\delta_0
\]
时具有严格正下界，因此该负 Ricci pinching 窗口被直接排除。

---

## 7. 靶依赖与维数一致性的准确结论

BBCG 的量词是
\[
\forall D>0\ \exists\varepsilon(4,D)>0,
\]
不是
\[
\exists\varepsilon_4>0\ \forall D>0.
\]
BBCG 对 Farrell–Jones 例子的讨论明确说明，微分刚性常数不能独立于靶流形的“size”；直径依赖是实质性的。

同样，
\[
\delta_*(X)\sim\frac1{4\chi(X)}
\]
沿 Euler 特征数趋于无穷的双曲靶族退化到零；有限覆盖中 \(\chi\) 按覆盖次数增长。BBCG Corollary 1.7 的常数也是固定 \(X\) 的 \(\varepsilon(X)\)。

因此应准确表述为：

- **双曲度数映射机制是靶流形依赖的**，不能从现有 BBCG 定理推出 Yau 26 所需的仅依赖维数的正宽度。
- 但 Step 47 并非每个结论都靶依赖。CGB 单独给出四维的统一结论：
  \[
  \boxed{\;
  \chi(Y)\le0
  \Longrightarrow
  \text{不存在满足 }
  \|g^{-1}(\Ric_g+g)\|_{\mathrm{op}}
  <\frac{\sqrt3-1}{2}
  \text{ 的度量。}
  \;}
  \]
  这是维数四、靶无关的负 Ricci pinching 排除，但不是 Yau 26 的 Einstein 不存在结论，因为该流形仍可能承载零或正 Einstein 度量。

总体上，Step 47 的核心计算与度数一结论成立；必须修正或强化的点是：明确定向与 Euler 假设、区分 BBCG Theorem 1.3 与未在该文证明的 Theorem 1.6、排除 \(X\#X\) 阈值端点、以及承认普通体积/熵近等号不足以控制 extended graph 情形。