# TTCS Independent Branch Record

```json
{
  "step_id": 49,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Sessions/S1003A02/workspace/notes/step49_cell_Y_measurement_bad_set_obstruction.md",
    "Sessions/S1003A02/workspace/scripts/step49_cell_theoremY_profile.py",
    "Sessions/S1003A02/workspace/data/step49_cell_theoremY_profile_x003_X128_N1600.json",
    "Sessions/S1003A01/workspace/notes/step43_period_linear_lebrun_ledger_and_ricci_flow.md",
    "Sessions/S1003A02/workspace/data/step48_bianchi_indicial.json"
  ]
}
```

## Task

Verify the mathematical substance and normalization of Step 49's two principal results. (A) Read the Step-48 Theorem-Y definitions, the new Step-49 note/script/data, and the A01 Step-43 ledger note. Check the conversion among delta W, D_W, Delta V, the spectral integrals Psi/dist^2/splitting, and the conclusion that the certified cell is far from Theorem-Y/LeBrun equality. Identify any formula or normalization error. (B) Check the handwritten exact first-order derivation for the nu=4 triaxial diagonal Bianchi-IX Einstein tail, especially e^{4r} delta W+=diag(-12,12,0) at Ric=-6 and the scalar--4 conclusions delta mu_min=delta|W+|^2=0, sigma=2 eps e^-4r, Psi=16 eps^2 e^-8r. Provide corrected formulas if needed. (C) Assess whether the stated obstruction to an unconditional linear bad-ball count is mathematically valid from the available hypotheses: can critical L2 Ricci defect plus Theorem K/closed identity force linearly many unit balls not C2a-close to CH, absent an Euler-Lagrange equation or per-ball load bound? Focus on correctness and any stronger unconditional weighted statement actually justified.

## Output

# 科学验证备忘录

## A. Theorem Y 通道、cell ledger 与谱积分的归一化

### A.1 \(\delta W\)、\(D_W\)、\(\Delta V\) 的换算正确

在 \(s=-4\) 归一化下，复双曲 Kähler 模型满足
\[
|W_0^+|^2=\frac23.
\]
记所有能量除以 \(8\pi^2\) 后加横线，并定义相对 Weyl 亏量
\[
\delta\bar W
=\frac1{8\pi^2}
\left(
\int_{\rm CH}|W_0^+|^2-\int_{\rm cell}|W^+|^2
\right).
\]
相对体积为 \(\bar\Delta V\)。于是
\[
\bar D_W
=\frac1{8\pi^2}\int_{\rm rel}\left(\frac23-|W^+|^2\right)
=\delta\bar W+\frac23\bar\Delta V.
\]
代入 Step 48 的闭恒等式
\[
8\pi^2k-P=4D_W-4\Delta V
\]
并取单 cell、\(k=1\)，得到
\[
1-\bar P(\hat g)
=4\bar D_W-4\bar\Delta V
=4\delta\bar W-\frac43\bar\Delta V.
\]
这正是 Step 49 与 A01 Step 43 使用的两个等价 ledger。

用 `step49_cell_theoremY_profile_x003_X128_N1600.json` 中的稳定 ledger：
\[
\bar\Delta V=0.0531061582794664,
\qquad
1-\bar P(\hat g)=0.0043391489573660,
\]
可反推
\[
\bar D_W
=\bar\Delta V+\frac{1-\bar P(\hat g)}4
=0.0541909455188079,
\]
以及
\[
\delta\bar W
=\bar D_W-\frac23\bar\Delta V
=0.0187868399991636.
\]
因此
\[
4\bar D_W=0.216763782075232,
\qquad
4\bar\Delta V=0.212424633117866,
\]
二者之差确为
\[
0.004339148957366.
\]
同时
\[
4\delta\bar W=0.075147359996655,
\qquad
\frac43\bar\Delta V=0.070808211039289,
\]
差仍为同一 saving。A01 当前 ledger 的
\[
(\bar\Delta V,\delta\bar W)\simeq(0.0530963,0.0187835)
\]
与此仅有已说明的有限网格相对体积差异。

唯一容易误读之处在 JSON 字段：

```text
"fourDeltaWplus": -0.07514735999665459
```

脚本实际定义它为
\[
-4\left(\bar D_W-\frac23\bar\Delta V\right)=-4\delta\bar W,
\]
即“cell Weyl 能量减去 CH Weyl 能量”的四倍，而不是 Step 49 文本中取正号定义的 \(4\delta\bar W\)。数学计算没有符号错误，但字段名没有显式说明这个方向。

### A.2 原 metric 与 Yamabe metric 的 \(P\) 已正确区分

脚本直接曲率积分给出
\[
\bar P(g)=0.9956627327621832.
\]
稳定 Yamabe ledger 给出
\[
\bar P(\hat g)=0.9956608510426340,
\]
两者相差
\[
\bar P(g)-\bar P(\hat g)=1.8817198\times10^{-6}.
\]
因此：

- \(1-\bar P(g)=0.0043372672\) 是原 profile 的 saving；
- \(1-\bar P(\hat g)=0.0043391490\) 才是 Theorem Y ledger 使用的 saving。

Step 49 文本在这两处使用上是相互一致的。

### A.3 脚本中的 conformal scaling 与积分测度正确

原 cell 在 \(\operatorname{Ric}_{\rm CH}=-6g\)、\(s=-24\) 尺度，先作
\[
g\longmapsto u^2g,
\]
再乘常数 \(6\) 到 \(s=-4\)。作为 \(\Lambda^+\) 上的端同态，
\[
W^+_{\hat g}=\frac{1}{6u^2}W^+_g,
\qquad
d\mu_{\hat g}=36u^4\,d\mu_g.
\]
脚本相应使用
```python
eig_hat = Wplus/(6*uconf**2)
mhat = 9*measure*uconf**4
```
其中内部 `measure` 是 \(4\,d\mu_g/(8\pi^2)\)：这一点也由
```python
Pnorm = integ(ric0sq/4)
```
和脚本注释
\[
\frac{d\mu}{8\pi^2dx}=\frac{W}{8\sqrt G}
\]
共同确认。因此
\[
9\,\texttt{measure}\,u^4
=36u^4\frac{d\mu_g}{8\pi^2},
\]
恰是所需的 hatted 测度。这里没有遗漏常数 \(4\)、\(6\) 或 \(36\)。

### A.4 \(\Psi\)、orbit distance 与 splitting 的谱公式正确

设排序后的特征值为
\[
\mu_1\le\mu_2\le\mu_3,\qquad \mu_1+\mu_2+\mu_3=0.
\]
脚本取
\[
x=-\mu_1,\qquad
\sigma=\frac{\mu_3-\mu_2}{2},
\]
并计算
\[
\operatorname{dist}(W^+,\mathcal K)^2
=(\mu_1+\tfrac23)^2+(\mu_2-\tfrac13)^2+(\mu_3-\tfrac13)^2.
\]
这是 Hoffman–Wielandt 排序匹配给出的最短正交轨道距离。Step 48 的精确分解为
\[
\Psi=
\begin{cases}
\frac53h^2+\frac4{27}h^3+4\sigma^2,
&h=\frac23-x\ge0,\\[2mm]
3t^2+4\sigma^2,
&t=x-\frac23\ge0.
\end{cases}
\]
故脚本中的 `upper_pair_splitting_contribution_4sigma2` 确实是 \(\Psi\) 的精确 splitting 分量，而非近似替代。

数据给出
\[
\bar\Psi=0.0132326118995176,
\]
\[
\overline{\operatorname{dist}^2}=0.00750240584862390,
\]
\[
\overline{4\sigma^2}=0.0109217156049857.
\]
由此
\[
\frac{\bar\Psi}{\overline{\operatorname{dist}^2}}
=1.76378246745>\frac{10}{9},
\]
与 Lemma 48.2 相符。splitting 约占
\[
\frac{0.0109217156}{0.0132326119}\simeq82.5\%
\]
的总 \(\Psi\)，其余约 \(0.00231090\) 来自最低特征值的 magnitude 位移。

### A.5 “远离等号态”的数值结论成立

在形式闭复制的 \(8\pi^2\) 单位中，Theorem Y 的精确 \(\Psi\) 版本给出
\[
4\bar\Delta V-2\bar\Psi
=0.212424633117866-0.026465223799035
=0.185959409318831.
\]
实际 hatted saving 为
\[
0.004339148957366,
\]
故差为
\[
0.181620260361465.
\]
saving 仅为该右端的约 \(2.33\%\)。

LeBrun magnitude penalty 为
\[
\frac{4}{9}\overline{\int(\sqrt6|W^+|-2)^2}
=0.004297071627642,
\]
所以
\[
4\bar\Delta V-\mathrm{LeB}
=0.208127561490224,
\]
与 saving 的差为
\[
0.203788412532858.
\]
saving 仅为该右端的约 \(2.08\%\)。

Theorem Y 的纯 distance 版本也给出
\[
4\bar\Delta V-\frac{20}{9}\overline{\operatorname{dist}^2}
\simeq0.195752620121,
\]
仍远大于 \(0.00433915\)。

因此 cell 的
\[
\frac{1-\bar P(\hat g)}{4\bar\Delta V}
=0.0204267692
\]
确实表示约 \(2\%\) 的 Yamabe-excess 转换效率。这个结论是相对 cell 通道的稳定浮点测量；孤立非紧 cell 本身没有闭流形的 sign-family 单极子输入。底层 profile 的 \(P\) 有既存证书，而新给出的 \(\Psi\)、distance 与 splitting 数字是浮点求积，不是区间包络。由于等号差约为 \(0.18\)–\(0.20\)，远大于所展示的网格变化，这一几何判断在数值上十分稳固。

---

## B. \(\nu=4\) triaxial tail 的一阶 Weyl splitting

### B.1 \(v_i\) 的一阶变化正确

令
\[
s=\sinh r,\qquad c=\cosh r,\qquad q=e^{-4r},
\]
并取
\[
A=s(1+\varepsilon q),\qquad
B=s(1-\varepsilon q),\qquad
C=sc.
\]
背景满足
\[
v_1=v_2=0,\qquad v_3=3s^2.
\]
对
\[
\gamma_1=\frac{B^2+C^2-A^2}{BC}
\]
求 \(\varepsilon\)-导数：
\[
\dot A'=q(c-4s),
\qquad
\dot\gamma_1=q\left(c-\frac4c\right).
\]
故
\[
\dot v_1
=\dot A'-\dot\gamma_1
=4q\left(\frac1c-s\right)=:d.
\]
交换 \(A,B\) 得
\[
\dot v_2=-d,\qquad \dot v_3=0.
\]
Step 49 的这一步完全正确。

### B.2 Weyl 系数 \(\operatorname{diag}(-12,12,0)\) 正确

代入
\[
R^+_{ii}
=-\frac{v_i'}{2A_i}
+\frac{-v_i-v_jv_k/2}{A_jA_k},
\]
得到
\[
\dot R^+_{11}
=-\frac{d'}{2s}
+\frac{d(3s^2/2-1)}{s^2c},
\]
\[
\dot R^+_{22}=-\dot R^+_{11},
\qquad
\dot R^+_{33}=0.
\]
写成
\[
\dot R^+_{11}=qF(r),
\]
直接展开可得
\[
F(r)=-12+96e^{-2r}+O(e^{-4r}).
\]
特别地，
\[
e^{4r}\dot R^+
\longrightarrow
\operatorname{diag}(-12,12,0).
\]
三个分量的一阶迹为零，而 \(\operatorname{tr}R^+=s/4\)，故一阶标量曲率变化也为零，所以
\[
\dot W^+=\dot R^+.
\]
因此
\[
e^{4r}\dot W^+
\longrightarrow
\operatorname{diag}(-12,12,0)
\]
是正确的。

在 \((A,B,C)\) spin 基下，背景为
\[
R^+_0=\operatorname{diag}(0,0,-6),
\qquad
W^+_0=\operatorname{diag}(2,2,-4)
\]
于 \(\operatorname{Ric}=-6g\) 尺度。乘 metric 常数 \(6\) 后，
\[
W^+_0=\operatorname{diag}\left(\frac13,\frac13,-\frac23\right),
\]
而一阶变化除以 \(6\)。所以
\[
W^+_\varepsilon
=
\operatorname{diag}\left(\frac13,\frac13,-\frac23\right)
+\varepsilon e^{-4r}\operatorname{diag}(-2,2,0)
+O(\varepsilon e^{-6r})
+O(\varepsilon^2e^{-8r}).
\]

### B.3 最低特征值、范数与 \(\Psi\) 的主项正确

最低特征值对应第三个、Kähler/fibre 槽，因此
\[
\left.\frac{d}{d\varepsilon}\right|_0\mu_{\min}=0.
\]
同时
\[
\left.\frac{d}{d\varepsilon}\right|_0|W^+|^2
=2\left\langle
\operatorname{diag}\left(\frac13,\frac13,-\frac23\right),
\operatorname{diag}(-2,2,0)
\right\rangle
=0.
\]
这里的等式是“一阶导数为零”；完整的范数差从二阶开始，并非恒等于零。

若使用带符号 splitting 坐标，
\[
\widetilde\sigma
=2\varepsilon e^{-4r}
+O(\varepsilon e^{-6r})
+O(\varepsilon^2e^{-8r}).
\]
若 \(\sigma=(\mu_3-\mu_2)/2\) 按排序定义为非负半间隙，则应写成
\[
\sigma
=2|\varepsilon|e^{-4r}
+O(|\varepsilon|e^{-6r})
+O(\varepsilon^2e^{-8r}).
\]
于是
\[
\operatorname{dist}(W^+,\mathcal K)
=2\sqrt2\,|\varepsilon|e^{-4r}
+O(|\varepsilon|e^{-6r})
+O(\varepsilon^2e^{-8r}).
\]

更精确地，裸 ansatz 的一阶 splitting 满足
\[
\sigma=\frac{|\varepsilon|e^{-4r}|F(r)|}{6}+O(\varepsilon^2),
\]
故 splitting 对 \(\Psi\) 的二阶贡献为
\[
4\sigma^2
=\frac{\varepsilon^2e^{-8r}F(r)^2}{9}+o(\varepsilon^2).
\]
由于 \(F(r)\to-12\)，
\[
\Psi
=16\varepsilon^2e^{-8r}
+O(\varepsilon^2e^{-10r})
+\text{更高阶的 }\varepsilon\text{ 项}.
\]
因此系数 \(16\) 正确。

Step 49 中唯一需要修正的公式精度是
\[
\sigma=2\varepsilon e^{-4r}+O(\varepsilon^2e^{-8r}).
\]
作为 \(r\to\infty\) 的展开，它漏写了线性但更快衰减的
\[
O(\varepsilon e^{-6r})
\]
项。若 \(\sigma\) 指排序后的半间隙，还应把主项写成 \(2|\varepsilon|e^{-4r}\)。这不改变任何主导系数或积分性质：

- \(\operatorname{dist}\sim e^{-4r}\)，与 \(e^{4r}\) 的 CH 壳层体积相乘产生长度型增长；
- \(\Psi\sim e^{-8r}\)，乘 \(e^{4r}\) 后可积。

所以 marginal \(L^1\) signal 与有限 Theorem-Y quadratic cost 的主要结论成立。

---

## C. 无条件线性 bad-ball 数目不能由现有输入推出

### C.1 三个数学原因

1. **\(P=\int|\operatorname{Ric}^\circ|^2\) 不提供 \(C^{2,\alpha}\) 正则性。**  
   常标量条件只是一条标量方程；任意常标量 metric 并不满足控制全曲率与其导数的临界椭圆系统。Theorem 48.L 从已经给定的 gauge 与 \(C^{2,\alpha}\)-接近性出发，而不是从小 \(P\) 推导这种接近性。局部高频、窄支撑的变化可以使 \(C^{2,\alpha}\) 距离明显，同时只贡献很小的 Ricci \(L^2\) 质量；Weyl 曲率及其导数更没有被 \(P\) 单独控制。

2. **Theorem K 给出总 \(L^1\) 权重，不给每个单位球的最大承载量。**  
   即使
   \[
   8\pi^2k-P\asymp k
   \]
   强迫
   \[
   \int\operatorname{dist}(W^+,\mathcal K)\asymp k,
   \]
   这份权重仍可集中在少数几何区域。现有公式没有排除一个单位球承载大量 Weyl 能量、体积或多条 exceptional classes。多中心拓扑也可聚集在同一拓扑核心中。

3. **任意 competing metric 没有天然的全局 CH marking。**  
   各局部球分别接近某个 CH 模型，并不自动拼成一个统一标记的复双曲 bulk。Theorem 48.LY 所需的参考映射、gauge 与 interface 数据并非由 Theorem K 或闭恒等式产生。

因此，缺少 Euler–Lagrange 型方程、局部正则性以及每球 Weyl/体积/拓扑载荷上界时，不能从现有输入推出 \(ck\) 个两两不交的单位 bad balls。

### C.2 可严格推出的全局加权关系

在 \(s=-4\) 下令
\[
d_K(x)=\operatorname{dist}(W^+(x),\mathcal K),
\qquad
\mathcal L=
\frac{(8\pi^2k-P)_+}{4\sqrt6/3}.
\]
Theorem K 给出
\[
\mathcal L\le\int_M d_K.
\]
点态上
\[
d_K^2\le2|W^+|^2+\frac43.
\]
结合闭恒等式
\[
\int_M\left(|W^+|^2+\frac13\right)
=2\pi^2(A-k)+\frac14P
\]
可得
\[
\int_M d_K^2
\le
2\int_M|W^+|^2+\frac43V
\le
8\pi^2(A-k)+P.
\]
因此有完全全局的兼容关系
\[
\boxed{
\mathcal L^2
\le
V\,[8\pi^2(A-k)+P].
}
\]

更具体地，对任意阈值 \(\tau>0\)，令
\[
B_\tau=\{x:d_K(x)>\tau\}.
\]
则
\[
\int_{M\setminus B_\tau}d_K\le\tau V,
\]
从而
\[
\boxed{
\operatorname{Vol}(B_\tau)
\ge
\frac{(\mathcal L-\tau V)_+^2}
{8\pi^2(A-k)+P}.
}
\]
这可以强迫一定体积的 Weyl-orbit departure；当 \(k\) 与 \(A\) 同阶且 \(\tau V\) 较小时，右端可为 \(O(k)\)。但它仍是坏区域体积或权重的结论，不是单位球数目的结论：一个单位球的体积与加权曲率没有统一常数上界。

### C.3 Step 49 的 good/bad 分解公式正确，并可稍作强化

若已有标记区域 \(G\) 满足
\[
E_G:=\int_Gd_K^2
\le
C\left(P(G_1)+\varepsilon_0^2V_{\rm margin}\right),
\]
令 \(B=M\setminus G\)。Cauchy–Schwarz 给出
\[
\mathcal L
\le
\sqrt{V_GE_G}
+
\sqrt{V_B\int_Bd_K^2},
\]
而
\[
\int_Bd_K^2
\le
2\int_B|W^+|^2+\frac43V_B.
\]
故
\[
\boxed{
\bigl(\mathcal L-\sqrt{V_GE_G}\bigr)_+^2
\le
V_B\left(
2\int_B|W^+|^2+\frac43V_B
\right).
}
\]
这正是 Step 49 所述的 weighted bad-region concentration。

再使用全局恒等式，还得到
\[
\boxed{
V_B
\ge
\frac{
\bigl(\mathcal L-\sqrt{V_GE_G}\bigr)_+^2
}{
8\pi^2(A-k)+P
}.
}
\]
这比单纯说“存在坏区域”更定量，但仍不产生线性 bad-ball 数目。要把总权重转成球数，数学上需要每个单位球只能承载至多固定量的 Weyl/体积/拓扑权重，或由选定近极小序列的方程导出局部正则性与能量原子化。现有 all-metric 输入没有提供这些结构。

## 总结

- Step 49 的 cell ledger、conformal scaling、\(\delta W\leftrightarrow D_W\leftrightarrow\Delta V\) 换算以及 \(\Psi\)/distance/splitting 积分均正确。
- JSON 的 `fourDeltaWplus` 存在方向符号易读错的问题；它等于 \(-4\delta\bar W\)。
- cell 在形式闭复制 ledger 中确实远离 Theorem Y 与 LeBrun 等号态；新谱数字是稳定浮点结果，而非区间包络。
- triaxial tail 的主系数
  \[
  e^{4r}\dot W^+\to\operatorname{diag}(-12,12,0)
  \]
  以及
  \[
  \delta\mu_{\min}=0,\quad
  \delta|W^+|^2=0,\quad
  \Psi\sim16\varepsilon^2e^{-8r}
  \]
  均正确。
- 需要修正的是 splitting 的余项：
  \[
  \sigma
  =2|\varepsilon|e^{-4r}
  +O(|\varepsilon|e^{-6r})
  +O(\varepsilon^2e^{-8r}),
  \]
  其中绝对值对应排序后的半间隙。
- 现有信息可推出坏区域的加权能量或体积估计，不能推出线性多个两两不交单位 bad balls。