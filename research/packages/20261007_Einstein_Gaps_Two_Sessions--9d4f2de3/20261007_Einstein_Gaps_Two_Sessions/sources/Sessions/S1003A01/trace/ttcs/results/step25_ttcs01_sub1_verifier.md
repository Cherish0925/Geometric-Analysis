# TTCS Independent Branch Record

```json
{
  "step_id": 25,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/collapse_chiral_charge_limit.py",
    "Sessions/S1003A02/workspace/data/collapse_chiral_charge_limit.json",
    "Sessions/S1003A02/workspace/data/einstein_bolt/series_n1.json",
    "Sessions/S1003A02/workspace/scripts/ach_projected.py",
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md"
  ]
}
```

## Task

Independently verify the controlled-collapse chiral charge limit and the claimed small-bolt matching orders. Read the exact symbolic charge script, its output, the regular Einstein bolt series, and the scale-free coordinate definitions. Decide precisely what follows from smooth bolt regularity alone, what additionally requires a finite-curvature/controlled F-structure matching hypothesis, and whether x=O(z^3), chi=O(z), eta=O(z) is justified at the scale-one collapsed entry. Derive the leading orders and identify any hidden coordinate or slot assumptions. Do not invent results; give equations and a concise mathematical memo.

## Output

# 独立核验备忘

## 1. 尺度不变坐标的准确含义

记实际轨道尺度因子为 \(A_f,A_g,A_h\)，并令
\[
r=(A_fA_gA_h)^{1/3},\qquad H=\log r,
\]
\[
x=\log\frac{A_f}{A_g},\qquad
q=\log\frac{A_g}{A_h}=-3\log z,
\]
\[
p=rH',\qquad \chi=rx',\qquad \eta=rq'.
\]
脚本中的 `af,ag,ah` 实际是体积归一化尺度
\[
\bar a_i=\frac{A_i}{r}.
\]
由 \(\beta=x+q/2\) 得
\[
\bar a_f=e^{2x/3}z^{-1},\qquad
\bar a_g=e^{-x/3}z^{-1},\qquad
\bar a_h=e^{-x/3}z^2.
\]
再令 \(\xi=\chi+\eta/2\)，则脚本中的 `pf,pg,ph` 正是实际导数 \(A_i'\)：
\[
\begin{aligned}
A_f'&=\bar a_f\left(p+\frac23\xi\right),\\
A_g'&=\bar a_g\left(p-\frac13\xi+\frac12\eta\right),\\
A_h'&=\bar a_h\left(p-\frac13\xi-\frac12\eta\right).
\end{aligned}
\]
等价地，若 \(k_i=A_i'/A_i\)，则
\[
\begin{aligned}
rk_f&=p+\frac23\chi+\frac13\eta,\\
rk_g&=p-\frac13\chi+\frac13\eta,\\
rk_h&=p-\frac13\chi-\frac23\eta.
\end{aligned} \tag{1}
\]

这些公式也说明：\(p,\chi,\eta=O(z)\) 对应的是三个对数导数 \(k_i=O(1)\)，而不只是三个 \(A_i'\) 有界。

---

## 2. 受控塌缩电荷极限：符号计算正确

置
\[
x=Xz^3+o(z^3),\quad
p=Pz+o(z),\quad
\chi=Cz+o(z),\quad
\eta=Nz+o(z).
\]
由上式直接得到
\[
\begin{aligned}
A_f'&\longrightarrow P+\frac23C+\frac13N,\\
A_g'&\longrightarrow P-\frac13C+\frac13N,\\
A_h'&=O(z^3)\longrightarrow0.
\end{aligned} \tag{2}
\]

脚本使用的轨道连接量为
\[
\begin{aligned}
g_f&=\frac{\bar a_g^2+\bar a_h^2-\bar a_f^2}
          {\bar a_g\bar a_h}
=z^{-3}(1-e^{2x})+z^3,\\
g_g&=\frac{\bar a_h^2+\bar a_f^2-\bar a_g^2}
          {\bar a_h\bar a_f}
=e^{-x}z^3+(e^x-e^{-x})z^{-3},\\
g_h&=\frac{\bar a_f^2+\bar a_g^2-\bar a_h^2}
          {\bar a_f\bar a_g}
=e^x+e^{-x}-e^{-x}z^6.
\end{aligned}
\]
因此
\[
g_f\to-2X,\qquad g_g\to2X,\qquad g_h\to2.
\]
对 \(u_i=A_i'-g_i\)，极限为
\[
\boxed{
\begin{aligned}
u_f&\to P+\frac23C+\frac13N+2X,\\
u_g&\to P-\frac13C+\frac13N-2X,\\
u_h&\to-2.
\end{aligned}} \tag{3}
\]
在脚本约定
\[
\mathfrak b_+=2-\sum_i u_i^2-u_fu_gu_h
\]
下，由 \(u_h=-2\) 可化为
\[
\mathfrak b_+
=-2-(u_f-u_g)^2
=\boxed{-2-(C+4X)^2}. \tag{4}
\]
这与 `collapse_chiral_charge_limit.json` 完全一致。反手性结果也可压缩为
\[
\mathfrak b_-
=-2-(u_f+u_g)^2
=-2-\frac{(C+2N+6P)^2}{9},
\]
展开后正是 JSON 中的多项式。

因此，作为一列具有上述完整一阶轨道数据的截面，电荷极限及其核方向
\[
C+4X=0
\]
均已严格验证。小 \(o\) 余项足以保持该极限。

这里还有一个重要的隐含条件：式 (2) 强制塌缩槽满足
\[
A_h'\to0.
\]
若只假设实际导数 \(A_h'\) 有界而其极限为 \(V\neq0\)，则 \(p,\eta\) 通常具有 \(z^{-2}\) 主项，\(u_h\to V-2\)，公式 (4) 不再成立。

---

## 3. \(O(-1)\) Einstein bolt 的局部阶数

`series_n1.json` 给出，在塌缩槽为 \(h=3\)、非塌缩槽为 \(f=1,g=2\) 时，
\[
\begin{aligned}
A_1(t)&=b+c_2t^2+p_4t^4+p_6t^6+\cdots,\\
A_2(t)&=b+c_2t^2+q_4t^4+q_6t^6+\cdots,\\
A_3(t)&=t+r_3t^3+r_5t^5+\cdots,
\end{aligned} \tag{5}
\]
其中
\[
c_2=\frac{3b^2+2}{2b},\qquad r_3=-\frac{2}{3b^2}.
\]
\(O(-1)\) 光滑性给出偶/奇结构、\(A_1(0)=A_2(0)\)、\(A_3'(0)=1\)，并且第一条对角三轴模出现在 \(t^4\)。这也可由奇异轨道的 \(S^1\) 表示看出：bolt 切平面的无迹对称二张量具有权 \(4\)，而 \(O(-1)\) 法向复坐标具有权 \(1\)。Einstein 方程进一步给出 \(c_2,r_3,\ldots\) 的显示值。

令
\[
d=p_4-q_4.
\]
由 JSON 中两式直接相减，
\[
\boxed{
d=
\frac{
162b^6-720b^5q_6+540b^4+741b^2+362
}{
12b^3(9b^2+34)
}.} \tag{6}
\]
所以局部自由参数 \(q_6\) 等价地控制 \(d\)。若写
\[
Q=b^5q_6,\qquad \delta=b^3d,
\]
则
\[
\delta=
\frac{
162b^6-720Q+540b^4+741b^2+362
}{
12(9b^2+34)
}. \tag{7}
\]
光滑 bolt 本身并不提供关于小 \(b\) 时 \(\delta\) 的统一估计；通过 \(Q\) 可改变其大小。

对每个固定 \(b>0\)，当 \(t\to0\) 时，
\[
z^3=\frac{A_3}{A_2}=\frac tb\bigl(1+O_b(t^2)\bigr),
\qquad
r=bz\bigl(1+O_b(t^2)\bigr).
\]
由 (5) 得
\[
x=\log\frac{A_1}{A_2}
=\frac db\,t^4+O_b(t^6)
=\delta z^{12}+O_b(z^{18}), \tag{8}
\]
以及
\[
\chi=rx'=4\delta z^{10}+O_b(z^{16}). \tag{9}
\]
另一方面，
\[
H'=\frac1{3t}+O_b(t),\qquad
q'=-\frac1t+O_b(t),
\]
故
\[
\boxed{
p=\frac1{3z^2}+O_b(z^4),\qquad
\eta=-\frac1{z^2}+O_b(z^4).} \tag{10}
\]

所以在 bolt 本身：

* \(x\) 和 \(\chi\) 比 \(z^3,z\) 小得多；
* \(p,\eta\) 并非 \(O(z)\)，而是具有 \(z^{-2}\) 的极坐标主项；
* 这些发散项在实际尺度导数中精确抵消，给出
  \[
  A_1',A_2'\to0,\qquad A_3'\to1.
  \]

相应地，
\[
g_f,g_g\to0,\qquad g_h\to2,
\]
\[
u_f,u_g\to0,\qquad u_h\to-1,
\]
从而
\[
\mathfrak b_+\to1,
\]
正好是 \(O(-1)\) bolt 电荷，而不是 Berger/ALF 端部的 \(-2\)。

---

## 4. 小 bolt 级数不能单独推出尺度一入口的阶数

令 \(s=t/b\)。从给定系数可见
\[
c_2\sim b^{-1},\quad r_3\sim b^{-2},\quad
p_4,q_4\sim b^{-3},\quad r_5\sim b^{-4},
\]
在自然参数化 \(q_6\sim b^{-5}\) 下，每一项都组织为
\[
A_i(t)=b\,\widetilde A_i(s).
\]
因此局部展开真正控制的是 \(s=t/b\) 有界的 bolt 尺度。若非塌缩半径从 \(b\) 墙大到数量级一，则相应 \(s\to\infty\)。有限阶 Taylor 级数不能把 (8)–(10) 传递到这样的截面。

更明确地，要在一列尺度一截面上得到脚本使用的阶数，需要额外存在
\[
A_g\to L\in(0,\infty),\qquad
\varepsilon:=\frac{A_h}{A_g}=z^3\to0, \tag{11}
\]
并满足
\[
\frac{A_f}{A_g}=1+O(\varepsilon),\qquad
k_f,k_g,k_h=O(1). \tag{12}
\]
由于
\[
r=A_g e^{x/3}z=Lz(1+o(1)),
\]
式 (1) 表明 (12) 与
\[
p,\chi,\eta=O(z)
\]
等价。特别是
\[
k_h=O(1)
\quad\Longleftrightarrow\quad
A_h'=O(A_h)=O(\varepsilon). \tag{13}
\]
单独的 \(A_h'=O(1)\) 不够：若 \(A_h'\to V\neq0\)，则
\[
p\sim\frac V3z^{-2},\qquad
\eta\sim-Vz^{-2}.
\]
bolt 的 \(V=1\) 正是式 (10)。

所以 \(x=O(z^3),\chi=O(z),\eta=O(z)\) 描述的是从极坐标 bolt 区域进入近 ALF/F-structure 区域后的附加匹配性质。它不由 bolt 光滑性或 `series_n1.json` 的局部递推单独推出。所需的实质内容是一列全局截面满足 (11)–(13)，并对自由三轴参数 \(d(b)\) 给出相应控制。

---

## 5. “有限曲率”一词需要区分曲率标量与曲率张量

令尺度一截面上
\[
A_g=L,\qquad A_h=L\varepsilon,\qquad A_f=Le^x,
\qquad \varepsilon=z^3.
\]
脚本中的 \(g_f,g_g\) 有界恰好要求
\[
x=O(\varepsilon)=O(z^3).
\]
三维轨道标量曲率也允许这一阶数。事实上
\[
R_{\rm orb}
=
\frac{2}{L^2}
\frac{
-e^{4x}-1-\varepsilon^4
+2e^{2x}+2\varepsilon^2+2e^{2x}\varepsilon^2
}{
e^{2x}\varepsilon^2
},
\]
若 \(x=X\varepsilon+o(\varepsilon)\)，则
\[
R_{\rm orb}\longrightarrow \frac{8(1-X^2)}{L^2}.
\]

但完整 Ricci/截面曲率要求更强。例如
\[
(\operatorname{Ric}_{\rm orb})_{ff}
=
\frac{2}{L^2}
\frac{e^{4x}-(1-\varepsilon^2)^2}
     {e^{2x}\varepsilon^2}. \tag{14}
\]
代入 \(x=X\varepsilon+o(\varepsilon)\) 得
\[
(\operatorname{Ric}_{\rm orb})_{ff}
=
\frac{8X}{L^2\varepsilon}+O(1).
\]
因此轨道曲率张量一致有界需要
\[
\boxed{x=O(\varepsilon^2)=O(z^6),} \tag{15}
\]
而不是只有 \(x=O(z^3)\)。在 \(p,\chi,\eta=O(z)\) 时，三个 \(k_i\) 有界，Gauss 方程中的第二基本形式乘积也是有界的，所以四维曲率张量一致有界同样导向 (15)。

故 \(x=Xz^3\) 最准确的几何含义是：

* 它保证脚本中的连接量及 Chern–Simons 型电荷有有限极限；
* 它保证轨道标量曲率有限；
* 若 \(X\neq0\)，它并不保证完整曲率张量有界。

在更强的 \(x=O(z^6)\) 情形，式 (4) 中 \(X=0\)，于是
\[
\mathfrak b_+^{\rm end}=-2-C^2.
\]
若水平一阶数据还满足 \(\chi=o(z)\)，则 \(C=0\)，恢复标准值 \(-2\)。核方向 \(C+4X=0\) 只消去该手性电荷中的平方项，并不消去式 (14) 的曲率增长。

---

## 6. 另一个隐含的一阶数据问题

脚本把 \(X,P,C,N\) 当作一列轨道一阶 jet 的独立极限。它没有对关系 \(x=Xz^3\) 沿径向求导。若在同一个端部邻域内有可微渐近展开 \(x=X(t)z^3\)，则
\[
\chi=rx'
=rX'z^3-X\eta z^3.
\]
若 \(X\) 平缓、\(rX'=O(1)\) 且 \(\eta=O(z)\)，便有 \(\chi=O(z^3)\)，从而 \(C=0\)。非零 \(C\) 表示水平各向异性虽只有 \(O(z^3)\)，其径向导数仍可为数量级一；作为单个匹配截面的 jet 这是允许的，但作为一个平缓 F-structure 端部还需额外的径向正则信息。

## 总结

1. `collapse_chiral_charge_limit.py` 的代数及 JSON 输出正确：
   \[
   \mathfrak b_+^{\rm end}=-2-(C+4X)^2.
   \]
2. 该公式依赖 \(A_h'\to0\)，等价于塌缩槽具有有界对数导数；普通意义下“实际一阶导数有界”并不能推出它。
3. 光滑 \(O(-1)\) bolt 在自身附近满足
   \[
   x=O(z^{12}),\quad \chi=O(z^{10}),\quad
   p\sim\tfrac13z^{-2},\quad \eta\sim-z^{-2},
   \]
   并具有电荷 \(1\)。
4. 从 bolt 电荷 \(1\) 过渡到受控端部电荷 \(-2-(C+4X)^2\) 是全局匹配问题；给定局部 Einstein 级数尚未推出尺度一入口处的
   \[
   x=O(z^3),\quad p,\chi,\eta=O(z).
   \]
5. 若“有限曲率”指完整曲率张量一致有界，则水平各向异性应满足更强的 \(x=O(z^6)\)。\(x=O(z^3)\) 对应的是有限电荷/有限标量曲率的受控 jet 类。