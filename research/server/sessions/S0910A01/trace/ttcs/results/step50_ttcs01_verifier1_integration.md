# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 50,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step50_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step50_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 50 Campedelli/product-quotient smoothing evidence for the Yau 26 project. Read the note and scripts plus the source files. Focus on two mathematical bridges: (1) for the BCGP K^2=2, G=Z_4^2 product-quotient row with six A1 singularities, does the character calculation plausibly compute H^0(Omega^1_S \otimes K_S) for the minimal resolution via quotient/reflexive-form/RDP comparison, or are there missing correction terms at the fixed points/resolution? (2) Does H^2(T_S)=0 for such an RDP canonical model really imply a global Q-Gorenstein smoothing that smooths all six A1 points and yields, via simultaneous resolution and Aubin-Yau, a negative Einstein metric on the smooth four-manifold? Also check the separate explicit six-nodal classical Z_2^3 line arrangement smoothing argument and identify any overstatement or missing source premise. Return a direct mathematical memo with corrections and next computations, not a procedural checklist.

## Integrated Scientific Memo

## 核验结论

Step 50 的两个例子应严格分开：

1. **经典 \((\mathbb Z_2)^3\) 七直线覆盖例子**：六节点模型及其显式全局平滑基本成立，但“由 simultaneous resolution 得到中心极小解与光滑纤维微分同胚”这一表述错误。正确的拓扑桥是：**节点平滑的 Milnor fiber 与 \(A_1\) 极小解的圆盘丛微分同胚**，从而全局替换后得到微分同胚。
2. **BCGP \(G=\mathbb Z_4^2\) product-quotient 行**：脚本的有限角色计算是可信的，但它计算的首先只是覆盖空间上的不变张量。把它直接等同于
   \[
   H^0(S,\Omega_S^1\otimes K_S)
   \]
   目前并未被所给来源证明，且在 \(A_1\) 解消处确有需要处理的对数/余留条件，不能用“反射层跨余维二延拓”自动消除。故该行的 \(H^2(T)=0\) 与全局平滑尚未建立。

---

## 一、BCGP 角色计算：算术正确，但解消比较有实质缺口

设
\[
Y=C_1\times C_2,\qquad X=Y/G,\qquad \rho:S\to X
\]
且 \(S\) 是六个 \(A_1\) 点的极小解。BCGP 的确给出
\[
S_1=((1,3),(1,0),(2,1)),\qquad
S_2=((3,2),(0,1),(1,1)),
\]
并由表及 Proposition 5.2 得知 \(X\) 恰有 \(8-K^2=6\) 个节点。

### 1. 角色算术本身

Chevalley–Weil 输出
\[
H^0(K_{C_1})=(2,3)\oplus(3,0)\oplus(3,1),
\]
\[
H^0(K_{C_2})=(0,3)\oplus(1,2)\oplus(3,3)
\]
与 genus \(3\) 一致。若两曲线非超椭圆，则
\[
\operatorname{Sym}^2H^0(K_{C_i})\simeq H^0(2K_{C_i}),
\]
脚本给出的两个二典范角色分解及两个不变空间维数 \(0\) 都正确。因此已经可靠地证明
\[
H^0(Y,\Omega_Y^1\otimes K_Y)^G=0. \tag{1}
\]

脚本中“每个二阶元素只有至多四个不动点，所以曲线非超椭圆”的论证本身不完整，因为超椭圆 involution 未必属于给定的 \(G\)。可作如下修补：超椭圆 involution 是中心的；若存在，则 \(G\) 在基底 \(\mathbb P^1\) 上的像是有限阿贝尔子群，故只能循环或 \((\mathbb Z_2)^2\)。结合 \(G=\mathbb Z_4^2\) 及 involution 是否位于 \(G\) 分情况即可排除。更稳妥的办法仍是直接用 Chevalley–Weil/Riemann–Roch 计算 \(H^0(2K_C)\)，不依赖超椭圆判别。

### 2. 商空间上的反射层比较

由于 \(q:Y\to X\) 仅在有限点分歧，在光滑轨迹上是 étale，故反射延拓给出可信的等式
\[
H^0\!\left(X,
  \bigl(\Omega_X^{[1]}\otimes\omega_X\bigr)^{**}\right)
 \cong H^0(Y,\Omega_Y^1\otimes K_Y)^G. \tag{2}
\]
结合 (1)，右侧为零。

问题在于 Step 50 还需要
\[
H^0(S,\Omega_S^1\otimes K_S)
 \stackrel{?}{\cong}
H^0\!\left(X,
 \bigl(\Omega_X^{[1]}\otimes\omega_X\bigr)^{**}\right). \tag{3}
\]
所给来源没有证明 (3)，而“RDP 上一形式延拓”不足以证明它。原因是：

* \(K_S=\rho^*K_X\) 对 Du Val 点成立；
* 但 \(\rho_*\Omega_S^1\) 与 \(\Omega_X^{[1]}\) 未必仅凭反射性自动相同；
* 解消上的一形式与奇点光滑轨迹上的反射一形式之间通常存在沿例外曲线的**对数极点/余留条件**；
* “例外曲线不能支撑一个全局截面”只说明两个截面的差若已是同一无挠层中的截面且在稠密开集消失，则差为零；它不证明每个反射截面都无极点地提升至 \(S\)。

因此当前角色计算没有排除潜在的局部解消修正。这里最需要计算的精确对象是
\[
Q:=\rho_*\Omega_S^1/\text{其在 }\Omega_X^{[1]}
\text{ 中的像或相应饱和差异},
\]
或者等价地，在每个局部模型
\[
X=(\mathbb C^2/\{\pm1\},0),\qquad E^2=-2
\]
上显式计算
\[
\rho_*(\Omega_S^1\otimes K_S)
\longrightarrow
(\Omega_X^{[1]}\otimes\omega_X)^{**}.
\]
必须证明该映射是同构，或计算其像所满足的六组局部条件。未完成该局部计算前，不能宣布
\[
H^0(S,\Omega_S^1\otimes K_S)=0.
\]

---

## 二、正确的 obstruction group 及其与解消的关系

Lee–Park 给出的充分条件是奇异面上的
\[
H^2(X,T_X^0)=0,
\qquad T_X^0=\mathcal Hom(\Omega_X,\mathcal O_X),
\]
而不只是 \(H^2(S,T_S)=0\)。

分支输出提出
\[
\rho_*T_S\simeq T_X^0
\]
并用 \(H^0(E,\mathcal O_E(-2))=0\) 支持这一点；这仍不足。标准自然对象通常是
\[
T_S(-\log E),
\]
即保持例外除子切向的向量场。局部 exact sequence 为
\[
0\to T_S(-\log E)\to T_S\to N_{E/S}\to 0,
\qquad N_{E/S}\simeq\mathcal O_E(-2).
\]
虽然
\[
H^0(E,\mathcal O_E(-2))=0,
\]
但
\[
H^1(E,\mathcal O_E(-2))\cong\mathbb C
\]
非零，所以不能由此忽略解消修正或直接断言全部高阶比较。

更稳健的目标是证明
\[
T_X^0\simeq \rho_*T_S(-\log E)
\]
以及相应的高阶直像陈述，从而推出
\[
H^2(X,T_X^0)
 \cong H^2(S,T_S(-\log E)).
\]
Serre 对偶把后者变成一个**对数微分层**的截面空间，而未必是普通的
\[
H^0(S,\Omega_S^1\otimes K_S).
\]
因此当前脚本很可能缺少的正是六个 \(A_1\) 点产生的局部余留条件。下一步应直接计算
\[
H^0\!\left(S,
  \Omega_S^1(\log E)\otimes K_S
\right)
\]
或其适当对偶层，而不是先假定它等于普通微分形式空间。

---

## 三、若 \(H^2(X,T_X^0)=0\) 真正成立，是否可同时平滑六点？

这一桥基本成立，但应准确表述。

Lee–Park Proposition 2.4 给出
\[
0\to H^1(T_X^0)\to \mathbb T_X^1
 \to \ker\!\left[
 H^0(T_X^1)\to H^2(T_X^0)
 \right]\to0.
\]
六个 \(A_1\) 点各有一维局部平滑方向，因此
\[
H^0(T_X^1)\cong\mathbb C^6.
\]
若 \(H^2(T_X^0)=0\)，一阶局部参数均可提升。所引 Lee–Park 文本进一步明确声称：在此条件下每个局部变形都可全局化；对 RDP 而言局部变形是 Gorenstein，因而也是 \(\mathbb Q\)-Gorenstein。可选取一条基曲线，使六个局部参数在 \(t\neq0\) 时均非零，从而同时平滑全部节点。

但应注明：仅凭展示出的短正合列本身只是一阶陈述；使用“存在实际全局 \(\mathbb Q\)-Gorenstein 平滑”时，必须引用 Lee–Park 随后的全局化定理，而不能仅由切空间满射自行推出无阻碍的解析族。

此外，
\[
K_X
\]
确实 ample：\(K_Y\) ample，且 \(q^*K_X=K_Y\)，有限满射检测 ample。缩小平滑基后，相对 canonical ample，故光滑纤维 \(X_t\) 具有 ample \(K_{X_t}\)，Aubin–Yau 给出负 Kähler–Einstein 度量。

### 拓扑桥的纠正

不能说“对平滑族做 simultaneous resolution 后得到一个中心纤维为 \(S\)、一般纤维为 \(X_t\) 的光滑 proper submersion”。ADE simultaneous resolution 是对仍带 ADE 奇点的变形作基变换和解消；对真正的平滑方向，其一般纤维没有例外曲线，而例外 \((-2)\)-曲线只出现在中心纤维，故该映射不可能是 Ehresmann 意义下的光滑纤维丛。

正确局部事实是：\(A_1\) 奇点的

* 极小解邻域是 Euler 数 \(-2\) 的 \(D^2\)-bundle over \(S^2\)；
* Milnor fiber \(T^*S^2\) 的紧截断与该圆盘丛定向微分同胚；
* 两者有同一边界 \(\mathbb{RP}^3\)。

将六个互不相交的局部块替换并与公共外部区域粘合，得到
\[
S\cong_{\mathrm{diff}} X_t
\]
（须固定边界识别及取向）。所以只要全局平滑确立，负 Einstein 结论仍成立，但依据是 ADE smoothing/resolution 的局部四维拓扑，而不是 Ehresmann 应用于“simultaneous resolution family”。

---

## 四、经典 \((\mathbb Z_2)^3\) 六节点直线排列

脚本精确验证了：

\[
\{x,y,z,x-y,y-z,x-z,x-y+z\}=0
\]
是七条不同直线；共有六个三重点、三个二重点、无四重点。给出的标签使每个三重点的三个标签都线性无关。

Alexeev–Pardini Definition 3.1 明确说明：三个标签生成 \((\mathbb Z_2)^3\) 时覆盖上产生一个 \(A_1\) 点。因此该覆盖确有且仅有六个 \(A_1\) 点；普通二重交点不会产生覆盖奇点。并且
\[
K_X=\pi^*(h/2),\qquad K_X^2=2,
\]
故 \(K_X\) ample。

更强的是，Alexeev–Pardini §3.3 明言这些覆盖的局部变形由七条支线的变形给出。因此把直线作小扰动至无三线共点，确实给出一个显式全局 Gorenstein（从而 \(\mathbb Q\)-Gorenstein）平滑；无需再调用 \(H^2(T^0)\) 判据。再用上节所述 \(A_1\) 局部 Milnor fiber/解消圆盘丛的微分同胚，中心极小解与一般光滑 Campedelli 纤维微分同胚，故该四流形承载负 Kähler–Einstein 度量。

需要保留两项限制：

* 这只证明一个经典 \((\mathbb Z_2)^3\) Campedelli 边界模型可平滑；
* 它没有识别 BCGP 的 \(\mathbb Z_4^2\) 商模型与该边界点或该具体平滑族。共同的 \(\pi_1=(\mathbb Z_2)^3\) 和数值不变量不足以完成识别。

另一个措辞修正：所给排列有六个相互关联的三线共点，“independent triple concurrences”若指几何条件彼此独立并未被脚本证明，也不需要。只需给出一条小的一参数扰动，使一般参数下所有三重共点同时消失；这是一般扰动即可做到的有限避开条件。

---

## 建议的决定性计算

BCGP 行现在缺的不是更多角色算术，而是以下局部—全局比较：

1. 在 \(A_1=\mathbb C^2/\{\pm1\}\) 的极小解上显式计算
   \[
   \rho_*(\Omega_S^1\otimes K_S),\qquad
   \rho_*(\Omega_S^1(\log E)\otimes K_S),
   \]
   与
   \[
   (\Omega_X^{[1]}\otimes\omega_X)^{**}
   \]
   之间的商及余留映射。

2. 证明并审计
   \[
   T_X^0\simeq\rho_*T_S(-\log E)
   \]
   及所需的 \(R^1\rho_*\) 项，然后把
   \(H^2(X,T_X^0)\) 写成覆盖空间角色数据加六个局部线性条件。

3. 为避免超椭圆论证，直接用 equivariant Riemann–Roch/Chevalley–Weil 计算两个 \(H^0(2K_{C_i})\)。

在这些修正完成前，可靠结论是：**经典六节点 Campedelli 例子已给出真实的 Einstein-existence 机制；BCGP \(\mathbb Z_4^2\) 行仅通过了覆盖空间角色层面的 obstruction-vanishing 测试，尚未证明全局平滑或 Einstein 存在。**