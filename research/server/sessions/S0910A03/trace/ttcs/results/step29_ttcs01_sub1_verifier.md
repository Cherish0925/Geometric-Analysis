# TTCS Independent Branch Record

```json
{
  "step_id": 29,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step29_consolidated_conditional_theorem.md",
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md"
  ]
}
```

## Task

Verify the following claims from the consolidated conditional theorem for the Ishida-LeBrun no-Einstein family, checking each step against the supplied mathematical evidence:

1. ABOVE-CRITICAL TOPOLOGICAL GAP: For sigma = D - A/3 > 0, the Chern-Gauss-Bonnet identity I - R = 2A/3 - sigma combined with the monopole inequality I >= 2A/3 forces R >= sigma. Since |Ric_0|^2 <= 4*delta^2 pointwise under Ricci pinching, R <= delta^2*Vol/(2pi^2). Combined with Vol bounded by topology, this gives delta >= c*sqrt(sigma/A). Verify that this chain has no gap and that the volume bound is justified.

2. UNIFORM K_0: For the IL family, int|Rm|^2 = 32pi^2*chi + 6*int|Ric_0|^2 from the decomposition |Rm|^2 = |W|^2 + 2|Ric_0|^2 + s^2/6 and CGB. With chi(M) ~ A + O(1) and Vol ~ 32pi^2A/9, K_0 ~ 9 + O(1/A). Check whether |Rm|^2 = |W|^2 + 2|Ric_0|^2 + s^2/6 is the correct decomposition in dimension 4, and whether the CGB identity used is accurate.

3. VOLUME CANCELLATION: beta = S*H_2^{1/2} = C*r^2*K_0^{1/2} is volume-independent. Check: S = C*r^2*Vol(B_r)^{-1/2} (Maheux-Saloff-Coste), H_2 ~ K_0*Vol(B_r), so S*H_2^{1/2} = C*r^2*K_0^{1/2}. With r = c*K_0^{-1/4}, beta = C*K_0^0 = C.

4. The defect identity D_a = R - sigma - (2/3)((a+)^2 - A) implies D_a <= R - sigma <= R, so the calibration tightens with sigma. Check this chain.

5. The general-p Moser iteration coefficient: the dissipation p*D_p controls |nabla Z_p|^2 with coefficient O(1/p), giving an extra factor p in the loss L_j. The Moser product converges because sum(log(p_j^4))/p_j < infinity. Verify.

## Output

# 科学核验备忘录

## 总结

1. 超临界情形的拓扑 Ricci 能量下界 \(R\ge \sigma\) 正确；体积上界可从同一组公式严格推出，而且能得到显式的 \(\delta\gtrsim\sqrt{\sigma/A}\)。
2. 四维曲率张量的点态分解在全张量范数下正确，但
   \[
   \int|{\rm Rm}|^2=32\pi^2\chi+6\int|{\rm Ric}_0|^2
   \]
   的系数错误，应为 \(4\)。此外，\(\chi(M)=A+O(1)\) 并不由已给出的 Ishida–LeBrun 拓扑数据推出，因此全族一致的 \(K_0\) 上界尚无现成依据。
3. 单个好球上的体积消去机制正确；若 \(r=cK_0^{-1/4}\)，则 \(\beta\le Cc^2\)。但定理中还出现了 \(r=c(A/K_0)^{1/4}\)，两种定义给出完全不同的 \(A\)-依赖。
4. 选定符号类满足 \((a^+)^2\ge A\) 时，\(D_a\le R-\sigma\le R\) 正确。不过校准平方应写成“不超过 \(864\pi^2D_a\)”，而不是等号。
5. 采用较弱的 \(D_p\) 控制确实引入一个额外的 \(p\)，所得 \(L_j\sim p_j^4 4^j\) 不妨碍 Moser 无穷乘积收敛。完整耗散中的 \(p(p-2)D_F\) 实际上还能避免这个额外因子。

---

## 1. 超临界拓扑间隙与体积上界

记

\[
T=(2\chi+3\tau)(M)=\frac{2A}{3}-\sigma.
\]

由给出的 Chern–Gauss–Bonnet 与签名公式，

\[
I-R=T.
\]

选定 Bauer–Furuta 符号类满足 \((a^+)^2\ge A\)，混合标量–Weyl 不等式给出

\[
I\ge \frac23(a^+)^2\ge \frac{2A}{3}.
\]

所以

\[
R=I-T\ge \frac{2A}{3}-\left(\frac{2A}{3}-\sigma\right)=\sigma.
\]

这一步严格成立。

若 \(e_1,\dots,e_4\in[-\delta,\delta]\) 是
\(g^{-1}({\rm Ric}+g)\) 的特征值，则

\[
|{\rm Ric}_0|^2
 =\sum_{\alpha=1}^4(e_\alpha-\bar e)^2
 =\sum_\alpha e_\alpha^2-4\bar e^2
 \le 4\delta^2.
\]

因而

\[
R=\frac1{8\pi^2}\int|{\rm Ric}_0|^2
 \le \frac{\delta^2}{2\pi^2}\operatorname{Vol}(M,g).
\]

### 体积上界的严格推导

设

\[
S=\frac1{4\pi^2}\int\frac{s^2}{24}.
\]

当 \(\delta<1\) 时，\(s=-4+\sum e_\alpha\le-4(1-\delta)\)，故

\[
S\ge \frac{(1-\delta)^2}{6\pi^2}\operatorname{Vol}(M,g).
\]

另一方面，\(S\le I=T+R\)，于是

\[
\frac{(1-\delta)^2}{6\pi^2}\operatorname{Vol}
 \le T+\frac{\delta^2}{2\pi^2}\operatorname{Vol}.
\]

即

\[
\frac{1-2\delta-2\delta^2}{6\pi^2}\operatorname{Vol}\le T.
\tag{1}
\]

例如在 \(\delta\le1/4\) 时，左侧系数至少为 \(3/(48\pi^2)\)，因此：

- 若 \(T\le0\)，不存在满足 \(\delta\le1/4\) 的度量；
- 若 \(T>0\)，则
  \[
  \operatorname{Vol}\le16\pi^2T
  \le\frac{32\pi^2}{3}A.
  \tag{2}
  \]

与 \(R\ge\sigma\) 合并可得

\[
\sigma\le R
\le\frac{\delta^2}{2\pi^2}\operatorname{Vol}
\le\frac{16}{3}\delta^2A,
\]

所以

\[
\delta\ge\sqrt{\frac{3\sigma}{16A}}
\qquad(\delta\le1/4).
\]

对所有 \(\delta\) 可统一写成

\[
\boxed{\displaystyle
\delta\ge
\min\left\{\frac14,\sqrt{\frac{3\sigma}{16A}}\right\}.}
\tag{3}
\]

因此，所需体积上界不仅能够证明，而且可直接得到 \(O(A)\) 的显式估计。

Step 3 中还有一条不使用体积的交叉验证。其

\[
R\le qS,\qquad q=\frac{3\delta^2}{(1-\delta)^2}
\]

与 \(S\le I=T+R\) 给出

\[
R\le q(T+R).
\]

在 \(q<1\) 时，

\[
\sigma\le R\le\frac{qT}{1-q}
\quad\Longrightarrow\quad
q\ge \frac{3\sigma}{2A}.
\]

因此

\[
\frac{\delta}{1-\delta}\ge\sqrt{\frac{\sigma}{2A}},
\]

同样得到 \(\delta\) 的 \(\sqrt{\sigma/A}\) 阶下界。

### 关于体积校准语句

“当 \(\delta\to0\) 时，无论 \(\sigma\) 如何都有
\(I\to2A/3\)、\(\operatorname{Vol}\to32\pi^2A/9\)”需要改写。对固定
\(\sigma>0\) 的流形，公式 (3) 已排除 \(\delta\to0\) 的序列。若允许拓扑变化，则上述公式先强制

\[
\frac{\sigma}{A}\longrightarrow0,
\]

此后才可能得到归一化意义下

\[
\frac{I}{A}\to\frac23,\qquad
\frac{\operatorname{Vol}}{A}\to\frac{32\pi^2}{9}.
\]

---

## 2. 四维曲率分解、CGB 系数与 \(K_0\)

采用全 \((0,4)\) 曲率张量范数时，点态分解确为

\[
|{\rm Rm}|^2
=|W|^2+2|{\rm Ric}_0|^2+\frac{s^2}{6}.
\tag{4}
\]

与此范数相配的四维 CGB 公式是

\[
32\pi^2\chi(M)
=\int_M\left(
 |W|^2-2|{\rm Ric}_0|^2+\frac{s^2}{6}
\right)d\mu.
\tag{5}
\]

由 (4)–(5) 相减得到

\[
\boxed{\displaystyle
\int_M|{\rm Rm}|^2\,d\mu
=32\pi^2\chi(M)+4\int_M|{\rm Ric}_0|^2\,d\mu.}
\tag{6}
\]

因此 Step 29 中的系数 \(6\) 应为 \(4\)。

若使用曲率算子 \(\mathcal R:\Lambda^2\to\Lambda^2\) 的范数，则相应公式为

\[
|\mathcal R|^2
=|W|^2+\frac12|{\rm Ric}_0|^2+\frac{s^2}{24},
\]

以及

\[
8\pi^2\chi
=\int\left(
 |W|^2-\frac12|{\rm Ric}_0|^2+\frac{s^2}{24}
\right),
\]

故

\[
\int|\mathcal R|^2
=8\pi^2\chi+\int|{\rm Ric}_0|^2.
\]

两种约定彼此相差固定因子，但都不会产生系数 \(6\)。

由 (6) 和 \(|{\rm Ric}_0|^2\le4\delta^2\)，

\[
K_0
:=\frac1{\operatorname{Vol}}\int|{\rm Rm}|^2
\le
\frac{32\pi^2\chi(M)}{\operatorname{Vol}}
+16\delta^2.
\tag{7}
\]

所以原文中的 \(24\delta^2\) 也应改为 \(16\delta^2\)。

### \(\chi(M)\) 与 \(A\) 的关系没有从现有公式推出

对

\[
M=\left(\#_{j=1}^mX_j\right)\#N
\]

有

\[
\chi(M)=\sum_j\chi(X_j)+\chi(N)-2m,
\]

而

\[
A=\sum_j(2\chi(X_j)+3\tau(X_j)),
\]

\[
D=4m-(2\chi(N)+3\tau(N)).
\]

这些等式只控制

\[
2\chi(M)+3\tau(M)=A-D,
\]

并不单独控制 \(\chi(M)\)。因此

\[
\chi(M)=A+O(1)
\]

不是给定拓扑恒等式的推论。要从 (7) 得到全族一致的 \(K_0\)，至少需要定量关系

\[
\frac{\chi(M)}{A}\le C,
\qquad
\frac{\operatorname{Vol}(M,g)}{A}\ge c>0.
\]

若额外有 \(\chi/A\to1\) 和
\(\operatorname{Vol}/A\to32\pi^2/9\)，则修正后的公式确实给出

\[
K_0\to9
\]

以及 \(O(\delta^2)\) 误差。现有材料没有给出第一项所需的全族拓扑估计。因此 Section 6 的一致 \(K_0\) 结论尚未由所列公式建立。

---

## 3. \(\beta\) 中的体积消去

设 \(V_r=\operatorname{Vol}(B_r)\)。Step 26 所引 Maheux–Saloff-Coste 形式为

\[
\mathsf S
\le C(4,(1+\delta)r^2)\,r^2V_r^{-1/2}.
\tag{8}
\]

在同一个最大函数好球上，应使用上界

\[
\widehat H_2
=\int_{\operatorname{supp}\chi}F^2
\le C(1+K_0)V_r,
\qquad F^2=1+|{\rm Rm}|^2.
\tag{9}
\]

于是

\[
\bar\beta
=\mathsf S\,\widehat H_2^{1/2}
\le
C r^2(1+K_0)^{1/2}.
\tag{10}
\]

在 Ricci 夹逼下，点态分解还给出

\[
K_0\ge
\frac1{\operatorname{Vol}}\int\frac{s^2}{6}
\ge\frac83(1-\delta)^2,
\]

所以 \(1+K_0\le CK_0\)。取

\[
r=cK_0^{-1/4}
\]

便得到

\[
\boxed{\bar\beta\le Cc^2.}
\tag{11}
\]

这正是体积消去机制。通过选择小的尺度系数 \(c\)，还可使 \(\bar\beta\) 达到临界吸收所需的小量级。这个局部计算本身不需要 \(K_0\) 有全族一致上界；但若 \(K_0\to\infty\)，则 \(r\to0\)，终端时间 \(T=\theta r^2\) 以及拉回几何中的 \(\rho\) 也会趋于零。因此 A01 的固定 \(\rho,K\) 几何仍然依赖一致的 \(K_0\) 控制。

### 两处尺度定义冲突

A1 写的是

\[
r_*=c(A/K_0)^{1/4},
\]

而 Sections 3 与 6 使用

\[
r_*=cK_0^{-1/4}.
\]

若 \(K_0\) 始终表示平均曲率能量，则第一种定义会给出

\[
\bar\beta\sim Cc^2A^{1/2},
\]

不再是全族一致常数。体积虽然仍被消去，但 \(A\)-依赖没有消去。Section 6 的结论只与第二种尺度相符。

### 好集与多球截断的两个具体问题

Section 3.1 使用 \(C_D\le2\) 保证好集占至少一半。若 \(C_D\) 是标准倍增常数，这在四维欧氏空间中也不成立：半径加倍的体积比为 \(16\)。可将阈值 \(4K_0\) 改成 \(2C_DK_0\)，仍可保留至少一半体积，只会改变维数常数。

此外，\(r/5\)-分离只保证 \(B_{r/10}(p_\alpha)\) 两两不交，并不保证

\[
B_{2r/3}(p_\alpha)
\]

两两不交。倍增几何给出有界重数，但“支持两两不交”并未由现有选择推出。因此：

- 单球上的 \(\bar\beta\) 计算成立；
- 总平台体积 \(\gtrsim A\) 可借助有界重数修正；
- 同时流动所有平台时，截断函数及重叠项仍需一个明确构造。

---

## 4. \(D_a\) 恒等式与 \(\sigma\) 校准

定义混合单极子余量

\[
D_a=I-\frac23(a^+)^2.
\]

利用

\[
I=\frac{2A}{3}-\sigma+R
\]

可得精确恒等式

\[
D_a
=R-\sigma-\frac23\bigl((a^+)^2-A\bigr).
\tag{12}
\]

对符号平均后选出的类，\((a^+)^2\ge A\)，因此

\[
0\le D_a
\le R-\sigma
\le R.
\tag{13}
\]

所以“\(\sigma\) 增大时，在固定 \(R\) 下校准余量减小”完全符合代数。

但完成平方与原始标量–Weyl 不等式给出的是

\[
\boxed{\displaystyle
\int_M(s+8\sqrt6|W^+|)^2\,d\mu
\le864\pi^2D_a
\le864\pi^2(R-\sigma).}
\tag{14}
\]

第一处应为不等号。原因是原始输入是

\[
\int(s-\sqrt6|W^+|)^2
\ge72\pi^2(a^+)^2,
\]

而不是等式。A01 Step 28 的式 (1.4) 也使用了“不超过”。这个修正不影响校准强化结论。

---

## 5. 一般 \(p\) 的耗散系数与 Moser 乘积

令

\[
\mathcal D_p=pD_p+p(p-2)D_F.
\]

由 Step 29 的估计，

\[
\|\nabla Z_p\|_2^2
\le Cp^2D_p+C(p-1)^2r^{-2}K_p.
\]

仅使用 \(\mathcal D_p\ge pD_p\)，便有

\[
\mathcal D_p
\ge \frac{c}{p}\|\nabla Z_p\|_2^2
-Cp\,r^{-2}K_p.
\tag{15}
\]

因此若要把梯度项归一化为固定系数，确实会多付出一个 \(p\)。原先的 \(p^3\) 损耗相应变成

\[
L_j=Cp_j^4\,4^j(t^{-1}+r^{-2}).
\]

取

\[
p_j=p_0(3/2)^j,
\]

则

\[
\log L_j
=O(1)+4\log p_j+j\log4
=O(j),
\]

从而

\[
\sum_{j=0}^\infty\frac{\log L_j}{p_j}
\le
\frac{C}{p_0}\sum_{j=0}^\infty
(j+1)\left(\frac23\right)^j
<\infty.
\tag{16}
\]

所以 Moser 乘积确实收敛。对应的 Sobolev 指数总和也是

\[
\sum_{j=0}^\infty\frac{2}{3p_j}
=\frac{2}{p_0}.
\]

### 更强的耗散读取

额外的 \(p\) 并非完整耗散结构所必需。因为

\[
|\nabla Z_p|^2
\le Cp^2D_F+Cp^2r^{-2}K_p
\]

而

\[
p(p-2)D_F\ge\frac13p^2D_F
\qquad(p\ge3),
\]

所以利用全部 \(\mathcal D_p\) 可以直接得到

\[
\mathcal D_p
\ge c\|\nabla Z_p\|_2^2-Cp^2r^{-2}K_p.
\tag{17}
\]

这恢复了固定梯度系数，并可能保留 \(p^3\) 而不是 \(p^4\) 的损耗。即使采用较弱的 (15)，无穷乘积仍完全可控，因此 Step 29 所述收敛结论正确。

---

## 综合科学结论

无条件的超临界拓扑间隙是可靠的，并可用公式 (3) 定量表达。校准余量和一般 \(p\) 迭代的核心代数也成立，经上述不等号与系数修正后更清楚。

全 Ishida–LeBrun 族的一致常数尚未由当前材料推出，关键数学原因是：

\[
\chi(M)/A
\]

没有给出的全族控制，曲率能量恒等式中的系数写错，以及 \(r_*\) 的两种定义不相同。单个好球上的体积消去机制不受这些问题影响，但固定终端尺度、固定拉回半径以及总平台截断仍依赖相应的全族几何估计。