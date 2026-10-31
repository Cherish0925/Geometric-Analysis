# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 25,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step25_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step25_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the controlled-collapse chiral charge limit and the claimed small-bolt matching orders. Read the exact symbolic charge script, its output, the regular Einstein bolt series, and the scale-free coordinate definitions. Decide precisely what follows from smooth bolt regularity alone, what additionally requires a finite-curvature/controlled F-structure matching hypothesis, and whether x=O(z^3), chi=O(z), eta=O(z) is justified at the scale-one collapsed entry. Derive the leading orders and identify any hidden coordinate or slot assumptions. Do not invent results; give equations and a concise mathematical memo.

## Integrated Scientific Memo

## 核验备忘：受控塌缩手性电荷与小 bolt 匹配阶

### 1. 坐标与脚本的精确含义

设实际尺度因子为 \(A_f,A_g,A_h\)，并定义
\[
r=(A_fA_gA_h)^{1/3},\qquad
x=\log\frac{A_f}{A_g},\qquad
q=\log\frac{A_g}{A_h}=-3\log z .
\]
于是
\[
\frac{A_f}{r}=e^{2x/3}z^{-1},\qquad
\frac{A_g}{r}=e^{-x/3}z^{-1},\qquad
\frac{A_h}{r}=e^{-x/3}z^2 .
\]
脚本采用
\[
p=r(\log r)'=r',\qquad \chi=rx',\qquad \eta=rq',
\]
以及 \(\xi=\chi+\eta/2\)。因此其中的 `pf,pg,ph` 正是 \(A_i'\)：
\[
\begin{aligned}
A_f'&=\frac{A_f}{r}\left(p+\frac23\chi+\frac13\eta\right),\\
A_g'&=\frac{A_g}{r}\left(p-\frac13\chi+\frac13\eta\right),\\
A_h'&=\frac{A_h}{r}\left(p-\frac13\chi-\frac23\eta\right).
\end{aligned}\tag{1}
\]
等价地，若 \(k_i=A_i'/A_i\)，
\[
rk_f=p+\frac23\chi+\frac13\eta,\quad
rk_g=p-\frac13\chi+\frac13\eta,\quad
rk_h=p-\frac13\chi-\frac23\eta. \tag{2}
\]

这里有一处记号隐患：笔记中的 \(p=rh'\) 只有在 \(h=\log r\) 时才正确；该 \(h\) 不能与槽标号 \(h\) 混淆。

---

### 2. 受控塌缩电荷极限：符号计算正确

令
\[
x=Xz^3+o(z^3),\quad p=Pz+o(z),\quad
\chi=Cz+o(z),\quad \eta=Nz+o(z). \tag{3}
\]
由 (1) 得
\[
A_f'\to P+\frac23C+\frac13N,\qquad
A_g'\to P-\frac13C+\frac13N,\qquad
A_h'=O(z^3)\to0. \tag{4}
\]

脚本的连接量为
\[
\begin{aligned}
\gamma_f&=\frac{A_g^2+A_h^2-A_f^2}{A_gA_h}
=z^{-3}(1-e^{2x})+z^3,\\
\gamma_g&=\frac{A_h^2+A_f^2-A_g^2}{A_hA_f}
=e^{-x}z^3+(e^x-e^{-x})z^{-3},\\
\gamma_h&=\frac{A_f^2+A_g^2-A_h^2}{A_fA_g}
=e^x+e^{-x}-e^{-x}z^6.
\end{aligned}
\]
故
\[
\gamma_f\to-2X,\qquad \gamma_g\to2X,\qquad \gamma_h\to2.
\]
置 \(u_i=A_i'-\gamma_i\)，则
\[
\boxed{
\begin{aligned}
u_f&\to P+\frac23C+\frac13N+2X,\\
u_g&\to P-\frac13C+\frac13N-2X,\\
u_h&\to-2 .
\end{aligned}}\tag{5}
\]
脚本约定
\[
\mathfrak b_+=2-\sum_i u_i^2-u_fu_gu_h.
\]
由于 \(u_h=-2\)，
\[
\mathfrak b_+^{\rm end}
=-2-(u_f-u_g)^2
=\boxed{-2-(C+4X)^2}. \tag{6}
\]
因此 JSON 输出完全正确，且小 \(o\) 余项不改变极限。\(P,N\) 从加手性电荷中消去，核方向为
\[
C+4X=0. \tag{7}
\]

同一代数给出脚本所定义的
\[
\mathfrak b_-=-2-\frac{(C+2N+6P)^2}{9}.
\]
但源文件只用注释定义了这个“opposite normalized charge”，没有从取向反转或另一手性 Chern–Simons 形式推导它；因此“\(N\) 进入反手性电荷”在当前材料中只是该代数定义的结论，不是独立几何核验。

一个有用的精确恒等式是：若 \(\epsilon_h=u_h+2\)，则
\[
\mathfrak b_+
=-2-(u_f-u_g)^2+\epsilon_h(4-\epsilon_h)-\epsilon_hu_fu_g. \tag{8}
\]
这显示 (6) 不仅需要 \(u_h\to-2\)，还需要最后一项趋零；(3) 正好保证这一点。

---

### 3. 光滑 Einstein bolt 自身给出的阶

`series_n1.json` 对应 bolt 在槽 \(h=3\)：
\[
\begin{aligned}
A_1(t)&=b+c_2t^2+p_4t^4+p_6t^6+\cdots,\\
A_2(t)&=b+c_2t^2+q_4t^4+q_6t^6+\cdots,\\
A_3(t)&=t+r_3t^3+r_5t^5+\cdots,
\end{aligned}\tag{9}
\]
其中
\[
c_2=\frac{3b^2+2}{2b},\qquad r_3=-\frac{2}{3b^2}.
\]
令
\[
d=p_4-q_4.
\]
由文件中的系数相减，
\[
d=
\frac{162b^6-720b^5q_6+540b^4+741b^2+362}
{12b^3(9b^2+34)}. \tag{10}
\]
因此局部三轴各向异性由一个自由参数控制；光滑性本身不对小 \(b\) 时 \(b^3d\) 给出统一界。

对每个固定 \(b>0\)，当 \(t\to0\)：
\[
z^3=\frac{A_3}{A_2}=\frac tb\bigl(1+O_b(t^2)\bigr),\qquad
r=bz\bigl(1+O_b(t^2)\bigr).
\]
于是
\[
x=\log\frac{A_1}{A_2}
=\frac db\,t^4+O_b(t^6)
=b^3d\,z^{12}+O_b(z^{18}), \tag{11}
\]
\[
\chi=rx'=4b^3d\,z^{10}+O_b(z^{16}). \tag{12}
\]
而
\[
(\log r)'=\frac1{3t}+O_b(t),\qquad
q'=-\frac1t+O_b(t),
\]
故
\[
\boxed{
p=\frac1{3z^2}+O_b(z^4),\qquad
\eta=-\frac1{z^2}+O_b(z^4).}\tag{13}
\]

所以光滑 bolt 附近并不满足 (3)。其发散项在 (1) 中抵消，产生
\[
A_1',A_2'\to0,\qquad A_3'\to1.
\]
又有
\[
\gamma_1,\gamma_2\to0,\qquad \gamma_3\to2,
\]
从而
\[
u_1,u_2\to0,\qquad u_3\to-1,\qquad
\mathfrak b_+\to1. \tag{14}
\]
这验证了 \(O(-1)\) bolt 电荷为 \(1\)，也说明 bolt 闭合极限与 Berger/ALF 端极限是不同几何区域。

---

### 4. 光滑 bolt 级数不能推出尺度一入口的受控阶

bolt Taylor 级数控制的是
\[
s=t/b=O(1)
\]
的内区。尺度估计
\[
c_2\sim b^{-1},\quad r_3\sim b^{-2},\quad
p_4,q_4\sim b^{-3},\quad r_5\sim b^{-4}
\]
表明其自然形式是 \(A_i(t)=b\,\widetilde A_i(t/b)\)。当非塌缩半径增长到 \(A_g\asymp1\) 时，一般有 \(s\to\infty\)，有限阶 bolt 级数无法传递到该截面。

在尺度一截面上，若
\[
A_g\to L\in(0,\infty),\qquad
A_h/A_g=z^3\to0, \tag{15}
\]
则
\[
r=A_ge^{x/3}z\asymp z.
\]
此时
\[
p,\chi,\eta=O(z)
\quad\Longleftrightarrow\quad
k_f,k_g,k_h=O(1), \tag{16}
\]
即第二基本形式的各本征值有界。特别地，
\[
k_h=O(1)\quad\Longleftrightarrow\quad
A_h'=O(A_h)=O(z^3). \tag{17}
\]
只要求实际导数 \(A_h'=O(1)\) 不够；若 \(A_h'\to V\neq0\)，则通常
\[
p\sim \frac{V}{3}z^{-2},\qquad
\eta\sim -Vz^{-2}, \tag{18}
\]
bolt 的 \(V=1\) 正是 (13)。

因此，在尺度一塌缩入口处
\[
x=O(z^3),\qquad p,\chi,\eta=O(z) \tag{19}
\]
不是光滑 bolt 正则性的结论。它是额外的全局匹配假设：必须证明该 Einstein 轨道从 \(t\sim b\) 的内区进入 \(A_g\asymp1\) 的塌缩区时，满足 (15)–(17)，并控制自由各向异性参数 \(d(b)\)。

---

### 5. “有限曲率”必须更正为更弱的受控一阶条件

脚本 docstring 和笔记把 \(x=Xz^3\) 称作“finite orbit curvature”。若“曲率”指完整轨道曲率张量，这一说法过强。

在 \(A_g=L\)、\(A_h=Lz^3\)、\(A_f=Le^x\) 时，
\[
(\operatorname{Ric}_{\rm orb})_{ff}
=
\frac{2}{L^2}
\frac{e^{4x}-(1-z^6)^2}{e^{2x}z^6}. \tag{20}
\]
若
\[
x=Xz^3+o(z^3),
\]
则
\[
(\operatorname{Ric}_{\rm orb})_{ff}
=\frac{8X}{L^2z^3}+O(1). \tag{21}
\]
故 \(X\neq0\) 时轨道 Ricci 张量发散；\(x=O(z^3)\) 只保证连接量 \(\gamma_f,\gamma_g\) 和轨道标量曲率有有限极限。完整轨道曲率张量一致有界至少要求
\[
\boxed{x=O(z^6).}\tag{22}
\]

此外，若要求完整四维曲率张量有界，混合/Codazzi 分量还约束径向各向异性导数。由于塌缩方向连接系数量级为 \(A_h^{-1}\sim z^{-3}\)，有界曲率自然要求
\[
x'=O(A_h)=O(z^3),
\qquad\text{从而}\qquad
\chi=rx'=O(z^4), \tag{23}
\]
而不是仅 \(\chi=O(z)\)。在这种真正的有限曲率 F-结构控制下，
\[
X=C=0,\qquad \mathfrak b_+^{\rm end}=-2. \tag{24}
\]

因此应区分：

1. **有限电荷/有界连接与有界第二基本形式类：**
   \[
   x=O(z^3),\qquad p,\chi,\eta=O(z),
   \]
   此时 (6) 成立，但允许某些曲率分量发散。

2. **尺度一完整曲率一致有界类：**
   至少满足 \(x=O(z^6)\)、\(\chi=O(z^4)\) 及 (16)，此时手性电荷只能趋于 \(-2\)。

所以式 (6) 是一个比真正有限曲率类更大的 \(C^1\)-受控塌缩 jet 类上的正确结论；笔记中的“finite-curvature”标签应改为“finite-charge/controlled-first-jet”，除非另有弱化或重标度后的曲率定义。

---

### 6. 隐含的径向 jet 与槽假设

#### (a) \(X\) 与 \(C\) 在单截面 jet 中可独立，但在平缓端部中未必

若在整个端邻域内可微地写成
\[
x=X(t)z^3,
\]
则
\[
\chi=rx'=rX'z^3-X\eta z^3. \tag{25}
\]
若 \(rX'=O(1)\) 且 \(\eta=O(z)\)，则实际上
\[
\chi=O(z^3),
\]
所以 \(C=0\)。非零 \(C\) 描述的是幅度只有 \(O(z^3)\)、但径向变化较快的 jet；它在孤立匹配截面上允许，却不能自动解释为平缓的有限曲率 F-结构端。

#### (b) 槽必须固定一致

bolt 数据中塌缩槽为 \(3\)。要把上述受控入口公式用于小 bolt，必须取
\[
h=3,\qquad (f,g)=(1,2)\ \text{或交换}.
\]
而 `ach_projected.py` 中 `f=0` 指 ACH 纤维为槽 \(1\)，其余槽按 `CYC` 重新排列。故“bolt 塌缩槽”和“ACH 纤维槽”不是同一角色；比较入口与 ACH 尾端时必须显式重标槽，不能直接沿用字母 \(f,g,h\)。

#### (c) \(f\leftrightarrow g\) 不影响主结论

交换 \(f,g\) 时
\[
x\mapsto-x,\qquad C\mapsto-C,
\]
并相应改变 \(N\)，但
\[
(C+4X)^2
\]
保持不变。因此 (6) 与非塌缩两槽的交换一致。

---

### 7. 不由所给材料支持的进一步断言

由 Einstein 差方程可以研究塌缩区的各向异性增长/衰减模，但当前源文件不足以严格推出：

- 正则 bolt 在尺度一入口必满足某条确定关系，如 \(C=4X\)；
- “电荷核方向” \(C=-4X\) 不可由正则 bolt 到达；
- 自由参数 \(d(b)\) 必须服从某个 \(e^{-\kappa/b}\) 调谐律。

这些是可检验的匹配渐近猜想，而不是 bolt 局部级数或电荷脚本的后果。建立它们需要对完整 Einstein ODE 在 \(t/b\to\infty\) 的重叠区作统一估计，或提供相应数值/解析全局轨道数据。

---

## 结论

1. `collapse_chiral_charge_limit.py` 的加手性极限严格正确：
   \[
   \boxed{\mathfrak b_+^{\rm end}=-2-(C+4X)^2}
   \]
   前提是完整受控 jet
   \[
   x=Xz^3+o(z^3),\quad p=Pz+o(z),\quad
   \chi=Cz+o(z),\quad\eta=Nz+o(z).
   \]

2. 光滑 \(O(-1)\) bolt 自身给出
   \[
   x=O_b(z^{12}),\quad \chi=O_b(z^{10}),\quad
   p\sim\tfrac13z^{-2},\quad\eta\sim-z^{-2},
   \]
   且 \(\mathfrak b_+\to1\)。它不是受控 Berger 端。

3. 光滑 bolt 正则性及给定有限阶 Einstein 级数，不能推出尺度一塌缩入口处
   \[
   x=O(z^3),\qquad p,\chi,\eta=O(z).
   \]
   这些是额外的全局 controlled-F-structure/matched-asymptotics 假设。

4. 若“有限曲率”指尺度一完整曲率张量有界，则所需阶更强，至少
   \[
   x=O(z^6),\qquad \chi=O(z^4),
   \]
   因而 \(X=C=0\) 且极限电荷正好为 \(-2\)。原文把 \(x=O(z^3)\) 称作有限曲率条件并不准确。

5. 当前真正未闭合的对象是：对所研究的小 bolt Einstein 全局族，证明其在 \(A_g\asymp1\)、\(A_h/A_g\to0\) 的入口截面上满足哪一种统一 jet 控制，以及自由各向异性参数 \(d(b)\) 如何随 \(b\) 缩放。只有这一全局匹配结果才能把 bolt 电荷 \(1\) 严格连接到受控端电荷公式。