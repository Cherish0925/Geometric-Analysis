# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 88,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step88_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step88_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the four-node assembled chirality source structural theorem for the product orbifold (S²×S²)/Z₂ desingularization. The claim has three parts:

1. NODE-SIGN COINCIDENCE: For the axial Killing-Killing mode h=(*dZ_A)⊙(*dZ_B) with P eigenvalue 1, the source boundary projection satisfies B_j^ε(h) = ε·s_j·(π²/2) where s=(+1,-1,-1,+1) for nodes (NN,NS,SN,SS). The sign vector s coincides with the mixed-chirality assignment pattern. Verify this from the normal-coordinate expansion of *dZ on each S² factor (sign reversal at the south pole of the height-function Killing form).

2. STRUCTURAL NON-CANCELLATION: The four-node chirality-odd assembled source is Σ_j w_j ε_j s_j. For mixed-diagonal (ε_j=s_j), this equals Σ w_j (always positive). For all-same (ε_j=+1) with equal scales, it equals 0. Therefore the mixed-chirality construction activates a global response absent from the symmetric KE control, and no positive scale choice can cancel it.

3. EIGENSPACE ISOLATION: Among the complete quotient-descending TT modes at λ=1, only the axial mode *dZ_A⊙*dZ_B has nonzero chirality source difference at the V₂ boundary-pairing level. The equatorial modes (*dX⊙*dX, etc.) have V₀≠0 at the poles and zero V₂ chirality source difference. Therefore the chirality-odd source at λ=1 is one-dimensional and there is no intra-eigenspace cancellation.

Check each part mathematically. For part 3, verify that the equatorial Killing forms at the poles have constant leading terms that do not produce fully-mixed V₂ derivative/tensor index quartets. Also check: does P h=1>0 mean this is a correction field (not an obstruction), and what is the physical content? Can higher eigenspaces (λ>1) potentially cancel the λ=1 contribution, or does the 1/λ decay in the spectral sum make the leading term dominant?

## Integrated Scientific Memo

# 核验结论

三项结论在**固定全局定向、统一节点标架与固定 EH 插入方向下的 \(V_2\) 源边界配对层面**成立，但必须作两项限定：

1. 数值存在对称积归一化的因子 \(2\)；
2. “不可消去”只对该轴向 \(\lambda=1\) 源分量成立，不能直接提升为完整 Ozuch 径向障碍或完整谱和不可消去。

---

## 1. 节点符号重合

令单位球面高度函数为 \(Z\)，并令 \(K_Z=*dZ\)。在保持球面定向的正规坐标 \((u,v)\) 中，

\[
Z=
\begin{cases}
1-\frac12(u^2+v^2)+O(r^4),&N,\\[1mm]
-1+\frac12(u^2+v^2)+O(r^4),&S.
\end{cases}
\]

因此在 Step 87 的 Hodge 星约定下

\[
K_Z|_N=v\,du-u\,dv+O(r^3),\qquad
K_Z|_S=-(v\,du-u\,dv)+O(r^3).
\]

即每个因子贡献

\[
\sigma_N=+1,\qquad \sigma_S=-1.
\]

对轴向模式

\[
h=K_Z^A\odot K_Z^B
\]

其二次 jet 在节点 \((p,q)\) 相对于 NN 乘以

\[
s_{pq}=\sigma_p\sigma_q,
\]

故按 \((NN,NS,SN,SS)\) 排列，

\[
\boxed{s=(+1,-1,-1,+1)}.
\]

NN 处 Step 87 的精确计算给出

\[
B_+=\frac{\pi^2}{2},\qquad B_-=-\frac{\pi^2}{2}
\]

这里使用的是

\[
h=\alpha\otimes\beta+\beta\otimes\alpha
\]

而不除以 \(2\)。边界配对对二次 jet 线性，所以四节点上

\[
\boxed{B_j^\varepsilon(h)
=\varepsilon s_j\frac{\pi^2}{2}}
\]

成立。

若本文的 \(\odot\) 定义为通常的平均对称积

\[
\alpha\odot\beta
=\frac12(\alpha\otimes\beta+\beta\otimes\alpha),
\]

则正确公式应为

\[
\boxed{B_j^\varepsilon(h)
=\varepsilon s_j\frac{\pi^2}{4}}.
\]

这解释了 Step 88 JSON 表格的 \(1/4\) 与其 theorem 字符串及题目中的 \(1/2\) 之间的冲突。符号结论不受此归一化影响。

节点手征标签必须相对于同一个四维全局定向定义；若独立使用反定向节点标架，SD/ASD 会交换，所谓 \(s=\varepsilon\) 将不再是良定义陈述。商生成元是两个球面上绕 \(Z\) 轴的同步 \(\pi\)-旋转，节点附近线性作用为 \(-I_{\mathbb R^4}\)，不是球面的无固定点 antipodal map。

---

## 2. 四节点结构性不相消

记共同正幅值为 \(b\)，其中未平均对称积时 \(b=\pi^2/2\)，平均对称积时 \(b=\pi^2/4\)。轴向模式的组装源分量是

\[
A_1=b\sum_jw_j\varepsilon_js_j.
\]

### 混合对角手征

若

\[
\varepsilon_j=s_j,
\]

则 \(\varepsilon_js_j=1\)，故

\[
\boxed{A_1=b\sum_jw_j}.
\]

所以只要 \(w_j>0\)，该轴向 \(\lambda=1\) 源投影严格非零，任何正尺度选择都不能在这个源分量内相消。

### 全同手征、等尺度

若 \(\varepsilon_j=+1\) 且 \(w_j=w\)，则

\[
A_1=bw(1-1-1+1)=0.
\]

全取 \(-1\) 亦然。若尺度不等，则全同手征得到

\[
b(w_{NN}-w_{NS}-w_{SN}+w_{SS}),
\]

一般不为零。

因此严格成立的是：

\[
\boxed{\text{混合对角构造激活轴向 }\lambda=1\text{ 源分量，等尺度全同手征对照不激活它。}}
\]

但这还不能表述成完整几何响应或完整障碍不可消去。真正的节点间量是

\[
L_iG_P^\perp S_j,
\]

其中 Green 传输及接收泛函可能带来额外节点符号。当前证明的是纯源组装 \(\sum_jw_jB_j^{\varepsilon_j}\) 的结构，不是完整 \(c_{\rm opp}-c_{\rm same}\) 的符号定理。

---

## 3. \(\lambda=1\) 空间中的源隔离

令

\[
K_X=*dX,\qquad K_Y=*dY,\qquad K_Z=*dZ.
\]

单位 \(S^2\) 上这些 Killing 一形式满足

\[
\Delta_HK_U=2K_U,\qquad
\nabla^*\nabla K_U=K_U.
\]

混合张量

\[
h_{UV}=K_U^A\odot K_V^B
\]

无迹且散度为零；乘积曲率对混合 \(AB\) 分量的 \(\mathring R\) 作用为零。因此在所用约定

\[
P=\frac12\nabla^*\nabla-\mathring R
\]

下，

\[
Ph_{UV}=h_{UV}.
\]

同步 \(\pi\)-旋转使 \(K_X,K_Y\) 变号而保持 \(K_Z\)，所以下降到商空间的这些 TT 模式恰为

\[
XX,\ XY,\ YX,\ YY,\ ZZ.
\]

在标准乘积张量分解下没有额外的 \(\lambda=1\) TT 标量生成分量：若候选写为

\[
H=A\phi\psi\,g_A+B\phi\psi\,g_B
  +C\,d\phi\odot d\psi,
\qquad \Delta\phi=\Delta\psi=2(\cdot),
\]

无迹给出 \(A+B=0\)，而散度条件给出 \(A=2C,\ B=2C\)，故只有零解。因子内 \(S^2\) TT 二张量不存在；至少一个因子的余精确阶数 \(l>1\) 时相应混合一形式本征值严格大于 \(1\)。因此在这一分解下商上的 \(\lambda=1\) TT 空间确为上述五维空间。

### 赤道模式为何没有 \(V_2\) 手征差

在 \(Z\)-轴的南北极，对于 \(U=X,Y\)，

\[
K_U(p)\neq0,\qquad \nabla K_U(p)=0.
\]

故其局部展开为

\[
K_U=K_U^{(0)}+K_U^{(2)}+O(r^3).
\]

于是 \(h_{UV}\) 的二次项只有

\[
K_{U,A}^{(2)}\odot K_{V,B}^{(0)}
+
K_{U,A}^{(0)}\odot K_{V,B}^{(2)}.
\]

每项的两个导数指标都位于同一个球面因子，不会形成轴向模式中的完全混合 quartet——即张量指标分别属于 \(A,B\)，而两个导数指标也分别属于 \(A,B\)。相应地，

\[
D_{ij,pq}M_{ij,pq}=0,
\qquad
B^+_{UV}-B^-_{UV}=0
\]

与源矩阵数据一致。

对 \(K_Z\) 则有

\[
K_Z(p)=0,\qquad \nabla K_Z(p)\neq0,
\]

所以

\[
K_Z^A\odot K_Z^B
=K_{Z,A}^{(1)}\odot K_{Z,B}^{(1)}+O(r^4),
\]

并产生例如

\[
M_{03,12}=M_{12,03}=-1,
\qquad
D_{03,12}=D_{12,03}=2.
\]

精确收缩 \(D:M=-8\) 给出

\[
B_+-B_-=-\frac{\pi^2}{8}(D:M)=\pi^2
\]

（未平均对称积约定）。因此

\[
\boxed{\text{在完整 }\lambda=1\text{ TT 空间的 }V_2
\text{ 源配对中，手征奇泛函秩为 }1,}
\]

其唯一方向是 \(ZZ\)。所以不存在同一 \(\lambda=1\) 空间内的源端抵消。

需要保留限定：赤道模式有 \(V_0\neq0\)。它们虽没有 \(V_2\) 手征源差，但仍可能经接收端背景曲率、Hodge 星和标架修正进入完整节点间响应。

---

## 4. \(Ph=h>0\) 的含义

因为 \(\lambda=1\neq0\)，该模式不属于 Fredholm 核，因而不是线性可解性的 obstruction。源方程在该方向上可直接反演：

\[
\Pi_1(P^{-1}S)
=\frac{\langle S,h\rangle}{\|h\|^2}\,h.
\]

所以它是一个由节点手征排列激发的全局低频 TT **修正场**。其物理/几何意义在于，该场传播到其他节点后改变局部曲率，并可能在下一匹配阶反馈进有限维径向障碍方程。Step 87 的局部计算

\[
\delta R^+=\operatorname{diag}(-2,1,1),\qquad
\delta R^-=\operatorname{diag}(2,-1,-1)
\]

证明选定径向曲率接收方向能探测该模式，但尚未把此接收泛函完全归一化为 Ozuch/Biquard 的径向变量。

---

## 5. 高本征空间能否抵消

须区分两个问题。

### 修正场的谱分量

不同本征空间 \(L^2\)-正交。因此非零的

\[
\Pi_{\lambda=1}P^{-1}S
\]

不能被任何 \(\lambda>1\) 分量作为张量场消掉。轴向低模成分本身是真实且不可由高模删除的。

### 最终标量接收量

最终量若为

\[
L(P^{-1}S)
=\sum_k
\frac{L(h_k)\,S(h_k)}
{\lambda_k\|h_k\|^2},
\]

则高模完全可能与 \(\lambda=1\) 项数值相消。仅有 \(1/\lambda_k\) 不足以证明低模主导，因为：

- 节点源和曲率接收泛函都涉及二阶 jets，其谱系数可随 \(\lambda\) 增长；
- 本征空间维数随能量增长；
- \(L\) 与 \(S\) 不是已证明相同的泛函，各谱项无固定符号；
- 负谱（尤其材料所述 \(P=-1\) shape mode）带相反 resolvent 权重；
- 当前尚无控制完整正则化谱和尾项的估计。

只有在证明接收端等于源端并且限制于 \(P>0\) 后，自配对

\[
\langle S,P^{-1}S\rangle
=\sum_{\lambda_k>0}
\frac{|S(h_k)|^2}{\lambda_k\|h_k\|^2}
\]

才具有逐项非负性。现有情形尚未满足这一条件。

---

## 最终判定

\[
\boxed{\text{三项结构定理在固定框架的 }\lambda=1,\ V_2
\text{ 源投影层面成立。}}
\]

精确版本是：

- 节点符号 \(s=(+,-,-,+)\)；
- 混合对角手征使轴向源成为正权重总和，等尺度全同手征使其消失；
- \(\lambda=1\) TT 空间中的手征奇 \(V_2\) 源是一维的；
- \(Ph=h\) 表示可反演修正场，而非核 obstruction。

尚未解决的对象仍是完整、定向一致、节点间、规范化并正则化的

\[
\boxed{\sum_{i,j}L_iG_P^\perp
       (S_j^+-S_j^-)}
\]

包括所有本征空间、负模、核投影、接收端 \(V_0\) 修正和同节点奇异部分扣除。因而当前结果不能证明完整 \(c_{\rm opp}-c_{\rm same}\) 非零，也不能证明 \(\lambda=1\) 项在最终标量中占优。