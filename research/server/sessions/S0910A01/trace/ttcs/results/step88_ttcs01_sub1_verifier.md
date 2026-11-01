# TTCS Independent Branch Record

```json
{
  "step_id": 88,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step87_missed_mode_green_correction.md",
    "Sessions/S0910A01/workspace/data/step88_four_node_chirality_assembly.json",
    "Sessions/S0910A01/workspace/data/step87_missed_killing_mode_boundary.json",
    "Sessions/S0910A01/workspace/data/step87_l1_oneform_source_matrix.json",
    "Sessions/S0910A01/trace/ttcs/results/step87_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Verify the four-node assembled chirality source structural theorem for the product orbifold (S²×S²)/Z₂ desingularization. The claim has three parts:

1. NODE-SIGN COINCIDENCE: For the axial Killing-Killing mode h=(*dZ_A)⊙(*dZ_B) with P eigenvalue 1, the source boundary projection satisfies B_j^ε(h) = ε·s_j·(π²/2) where s=(+1,-1,-1,+1) for nodes (NN,NS,SN,SS). The sign vector s coincides with the mixed-chirality assignment pattern. Verify this from the normal-coordinate expansion of *dZ on each S² factor (sign reversal at the south pole of the height-function Killing form).

2. STRUCTURAL NON-CANCELLATION: The four-node chirality-odd assembled source is Σ_j w_j ε_j s_j. For mixed-diagonal (ε_j=s_j), this equals Σ w_j (always positive). For all-same (ε_j=+1) with equal scales, it equals 0. Therefore the mixed-chirality construction activates a global response absent from the symmetric KE control, and no positive scale choice can cancel it.

3. EIGENSPACE ISOLATION: Among the complete quotient-descending TT modes at λ=1, only the axial mode *dZ_A⊙*dZ_B has nonzero chirality source difference at the V₂ boundary-pairing level. The equatorial modes (*dX⊙*dX, etc.) have V₀≠0 at the poles and zero V₂ chirality source difference. Therefore the chirality-odd source at λ=1 is one-dimensional and there is no intra-eigenspace cancellation.

Check each part mathematically. For part 3, verify that the equatorial Killing forms at the poles have constant leading terms that do not produce fully-mixed V₂ derivative/tensor index quartets. Also check: does P h=1>0 mean this is a correction field (not an obstruction), and what is the physical content? Can higher eigenspaces (λ>1) potentially cancel the λ=1 contribution, or does the 1/λ decay in the spectral sum make the leading term dominant?

## Output

# 四节点手征源科学核验备忘

## 总结

三项结构结论在固定的定向正规标架、共同的 \(C_{ab}\) 基和共同 EH 插入方向下成立：

1. 轴向 Killing–Killing 模式在四节点的符号确为
   \[
   s=(+1,-1,-1,+1).
   \]
2. 混合手征取值 \(\varepsilon_j=s_j\) 时，该 \(\lambda=1\) 模式的组装源为同号正项之和；任意正权重均不能相消。全同手征且四权重相等时，该模式的组装源为零。
3. 商空间上完整的 \(\lambda=1\) TT 本征空间为五维；在所考察的 \(V_2\) 球面积分配对中，手征奇部分只沿轴向模式，因而是一维的。

有一个必须统一的数值约定：Step 87 使用不除以 \(2\) 的对称积，而 Step 88 的逐节点表格使用了除以 \(2\) 的对称积。二者的符号机制相同，但 \(B_j^\varepsilon\) 相差因子 \(2\)。

---

## 1. 南北极符号与四节点向量

在每个单位 \(S^2\) 上取与球面定向相容的测地正规坐标 \((u,v)\)，并令
\[
K_Z=*dZ.
\]
在北极，
\[
Z=1-\frac{u^2+v^2}{2}+O(r^4),
\]
从而在 Step 87 的 Hodge 星约定下
\[
K_Z=v\,du-u\,dv+O(r^3).
\]
在南极使用同样定向的正规标架时，
\[
Z=-1+\frac{u^2+v^2}{2}+O(r^4),
\]
因此
\[
K_Z=u\,dv-v\,du+O(r^3)
   =-\bigl(v\,du-u\,dv\bigr)+O(r^3).
\]
于是可写成
\[
K_Z|_p=\sigma_p K_{\rm lin}+O(r^3),
\qquad
\sigma_N=+1,\quad \sigma_S=-1.
\]

对
\[
h=K_Z^A\odot K_Z^B
\]
而言，节点 \((p,q)\) 的二次 jet 相对于 NN 节点乘以
\[
s_{pq}=\sigma_p\sigma_q.
\]
按 \((NN,NS,SN,SS)\) 排列即
\[
\boxed{s=(+1,-1,-1,+1)}.
\]

Step 87 源端计算在 NN 给出
\[
B^+_{NN}=\frac{\pi^2}{2},\qquad
B^-_{NN}=-\frac{\pi^2}{2}
\]
（不除以 \(2\) 的对称积）。由于该配对对 \(V_2\) 线性，
\[
\boxed{B_j^\varepsilon(h)
=\varepsilon s_j\frac{\pi^2}{2}},
\qquad \varepsilon\in\{+1,-1\}.
\]
这正是混合手征排列
\[
\varepsilon=(+1,-1,-1,+1)
\]
与节点符号向量重合的来源。

这一推导使用的是定向保持的南北极标架。若四节点另行施加彼此独立的 \(SO(4)\) gluing 旋转，则共同幅值还取决于 EH 插入方向与 \(C_{ab}\) 基的传输；当前四节点数据采用了相同方向的传输。

### 对称积归一化

两个文件中的数值可按下表统一：

\[
\begin{array}{c|c|c}
\text{模式定义}&B_j^\varepsilon&\|h\|^2_{L^2((S^2\times S^2)/\mathbb Z_2)}
\\ \hline
\alpha\otimes\beta+\beta\otimes\alpha
&
\varepsilon s_j\,\pi^2/2
&
64\pi^2/9
\\[2mm]
\frac12(\alpha\otimes\beta+\beta\otimes\alpha)
&
\varepsilon s_j\,\pi^2/4
&
16\pi^2/9
\end{array}
\]

Step 88 表格中的 `B_plus_over_pi2 = 1/4` 对应第二行，而其结构公式中的 \(\pi^2/2\) 对应第一行。投影后的归一化量不受此选择影响：
\[
\frac{(B_j^\varepsilon)^2}{\lambda\|h\|^2}
=\frac{9\pi^2}{256}
\qquad(\lambda=1).
\]

---

## 2. 四节点组装与正权重不相消

记共同幅值为 \(b\)，即不除以 \(2\) 时 \(b=\pi^2/2\)。轴向 \(\lambda=1\) 模式的四节点组装系数是
\[
A_1=b\sum_j w_j\varepsilon_js_j.
\]

### 混合对角手征

若
\[
\varepsilon_j=s_j,
\]
则逐项有 \(\varepsilon_js_j=1\)，所以
\[
\boxed{A_1=b\sum_jw_j}.
\]
当每个 \(w_j>0\) 时，该数严格非零，并在当前符号约定下为正。因此调整正泡尺度所产生的正权重不能使这个 \(\lambda=1\) 源分量相消。

### 全同手征对照

若 \(\varepsilon_j=+1\) 且 \(w_j=w\)，则
\[
A_1=bw(1-1-1+1)=0.
\]
全取 \(-1\) 时同样为零。若四个权重不相等，则全同手征给出的是交错和
\[
b(w_{NN}-w_{NS}-w_{SN}+w_{SS}),
\]
一般不为零。

因此，“混合构造激活而对称 KE 对照不激活”的精确数学含义是：

\[
\Pi_{\lambda=1}S_{\rm mixed}
\quad\text{具有非零轴向分量，}
\]
而全同手征、等尺度对照的这个轴向分量为零。其他本征空间中的修正场并未由此等式排除。

---

## 3. \(\lambda=1\) TT 本征空间及一维手征奇源

令
\[
K_X=*dX,\qquad K_Y=*dY,\qquad K_Z=*dZ.
\]
在单位 \(S^2\) 上，这三个一形式都是 Killing 一形式，并满足
\[
\Delta_HK_U=2K_U,\qquad
\nabla^*\nabla K_U=K_U.
\]
对混合张量
\[
h_{UV}=K_U^A\odot K_V^B
\]
有：

- \(\operatorname{tr}h_{UV}=0\)；
- \(\delta h_{UV}=0\)，因为两个 Killing 一形式余闭且分别只依赖一个因子；
- 乘积曲率对混合 \(AB\) 分量的 \(\mathring R\) 作用为零。

故
\[
P h_{UV}
=\frac12(1+1)h_{UV}
=h_{UV}.
\]

商生成元是两个因子上同时绕 \(Z\) 轴旋转 \(\pi\)。其作用为
\[
K_X\mapsto-K_X,\qquad
K_Y\mapsto-K_Y,\qquad
K_Z\mapsto K_Z.
\]
因此下降到商空间的混合 TT 模式恰为
\[
XX,\ XY,\ YX,\ YY,\ ZZ,
\]
总维数为五。

其他 \(P=1\) 的低阶乘积张量不会再产生 TT 模式。例如，对 \(l_A=l_B=1\) 的标量本征函数
\[
\Delta\phi=2\phi,\qquad \Delta\psi=2\psi,
\]
一般标量生成组合可写成
\[
H=A\phi\psi\,g_A+B\phi\psi\,g_B
 +C\,d\phi\odot d\psi.
\]
无迹条件给出 \(A+B=0\)，而散度为零给出
\[
A=2C,\qquad B=2C.
\]
三式合起来只有 \(A=B=C=0\)。精确–余精确的 \(l=1\) 混合模式散度不为零，而余精确 \(l=1\) 形式是 Killing 形式，其对称协变导数为零，因而没有可补偿的因子内张量。更高 \(l\) 的余精确模式满足
\[
P=\frac12\bigl(l_A(l_A+1)+l_B(l_B+1)-2\bigr)>1
\]
只要至少一个 \(l>1\)。这验证了五维描述的完整性。

### 为什么四个赤道模式的 \(V_2\) 手征差为零

在南北极 \(p\)，对 \(U=X,Y\) 有
\[
U(p)=0,\qquad dU(p)\ne0.
\]
又因
\[
\nabla^2U=-Ug,\qquad
\nabla K_U=*\nabla^2U,
\]
可得
\[
K_U(p)\ne0,\qquad \nabla K_U(p)=0.
\]
因此
\[
K_X,\ K_Y=K^{(0)}+K^{(2)}+O(r^3),
\]
有非零常数项而没有线性项。两个赤道形式的乘积，其二次 jet 只有
\[
K_A^{(2)}\odot K_B^{(0)}
+
K_A^{(0)}\odot K_B^{(2)}.
\]
每一项的两个导数指标都来自同一个球面因子，因而不会产生轴向模式中那种“一条导数来自 \(A\)、另一条来自 \(B\)”的全混合四指标通道。Step 87 的 \(D_{ijpq}\) 张量只在这些全混合通道上给出手征差，所以
\[
B^+_{UV}-B^-_{UV}=0,
\qquad U,V\in\{X,Y\}.
\]

相反，对 \(K_Z\) 有
\[
K_Z(p)=0,\qquad \nabla K_Z(p)\ne0,
\]
故
\[
K_Z^A\odot K_Z^B
=K_A^{(1)}\odot K_B^{(1)}+O(r^4),
\]
恰好产生 Step 87 中的
\[
M_{03,12}=M_{12,03}=-1
\]
等全混合分量，进而给出
\[
B^+-B^-=\pi^2
\]
（不除以 \(2\) 的约定）。

所以在五维 \(\lambda=1\) TT 空间内，\(V_2\) 手征奇源泛函只沿 \(ZZ\) 方向：
\[
\boxed{\dim \operatorname{im} S_{\mathrm{odd},\lambda=1}=1}.
\]
四个赤道模式不能在这个本征空间内抵消轴向分量。它们的非零 \(V_0\) 会影响接收端的背景曲率和标架修正，但不改变这里的 \(V_2\) 源端零值。

---

## 4. \(Ph=h\) 的物理含义

因为该模式的本征值为 \(1\neq0\)，源方程
\[
Pu=S
\]
在这一方向上直接给出
\[
\Pi_1u
=\frac{\langle S,h\rangle}{\|h\|^2}\,h.
\]
所以它是可反演的全局修正场，不是 Fredholm 核投影产生的 obstruction。其几何作用是把四个节点的手征排列投影到一个遍布整个乘积 orbifold 的低本征值 TT 形变上。Step 87 的局部曲率计算
\[
\delta R^+=\operatorname{diag}(-2,1,1),\qquad
\delta R^-=\operatorname{diag}(2,-1,-1)
\]
说明该全局形变在节点处能被径向曲率泛函探测，因此它可以在后续匹配阶进入有限维径向方程。

---

## 5. 更高本征空间能否抵消

这里须区分两个数学对象。

### 作为修正场本身

不同本征空间在 \(L^2\) 中正交。非零的
\[
\Pi_{\lambda=1}u
\]
不能被任何 \(\lambda>1\) 分量消去。因此混合构造确实含有一个不可由高模删除的轴向低模成分。

### 作为某个标量接收量

若最终研究的是
\[
L(P^{-1}S)
=\sum_k
\frac{L(h_k)\,S(h_k)}
{\lambda_k\|h_k\|^2},
\]
则 \(\lambda>1\) 项可能与 \(\lambda=1\) 项数值相消。因子 \(1/\lambda_k\) 本身不能证明首项占优：

- 节点多极源涉及本征张量的二阶 jets，其谱系数未必随 \(\lambda_k\) 衰减；
- 接收曲率泛函也含二阶导数；
- 四维本征值计数和简并度随能量增长；
- 各项符号由源端、节点传输和接收端共同决定。

只有当接收泛函与源泛函相同，并且所求和的谱段满足 \(P>0\) 时，才有
\[
\langle S,P^{-1}S\rangle
=\sum_{\lambda_k>0}
\frac{|S(h_k)|^2}{\lambda_k\|h_k\|^2}\ge0,
\]
此时各正谱项不会相消。当前径向接收泛函尚未被证明等于该自配对。因此现有计算确立了非零的一维低模修正，却尚未确定完整径向标量中高模总和的符号或其相对于 \(\lambda=1\) 项的大小。