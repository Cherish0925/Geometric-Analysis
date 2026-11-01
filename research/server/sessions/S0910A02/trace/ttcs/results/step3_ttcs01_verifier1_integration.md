# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 3,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step3_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step3_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check the Step 3 repaired LeBrun/Ishida-LeBrun analysis for Yau Problem 26. Read the active goal, the correction note, the stable integral obstruction theorem note, the repaired script, and the primary source excerpts/files. Verify the constants in the 4D Chern-Gauss-Bonnet identity, the scalar-only k/A=2/3 and mixed k/A=1/3 thresholds, the derivation of the pinching lower bound δ/(1-δ) >= sqrt((p-1/3)/2), and the corrected interpretation of positive collapse via lens spaces. Identify any algebraic mistakes, missing hypotheses (orientation, b_+, monopole class, strict/equality cases), or overclaims relative to the full Yau26 proposition. Give a direct scientific memo, not a checklist.

## Integrated Scientific Memo

# 科学核验备忘录

Step 3 的核心修复是正确的：四维 Chern–Gauss–Bonnet 常数、标量估计的 \(k/A=2/3\) 阈值、混合 Seiberg–Witten 估计的 \(k/A=1/3\) 阈值，以及
\[
\frac{\delta}{1-\delta}\ge \sqrt{\frac{p-1/3}{2}}
\]
均可由所给原始文献严格推出。需要修正脚本的 \(p=2/3\) 端点，并把方向、\(b_+\)/monopole-class、\(p<1\) 与等号情形等假设写明。

## 1. 四维曲率恒等式与标量阈值

对闭定向四维流形，
\[
2\chi+3\tau
=\frac1{4\pi^2}\int_M
\left(2|W^+|^2+\frac{s^2}{24}-\frac{|\mathring r|^2}{2}\right)d\mu .
\]
若 \(\operatorname{Ric}=\lambda g\)，则 \(s=4\lambda\)、\(\mathring r=0\)，因此
\[
8\pi^2(2\chi+3\tau)
=4\int|W^+|^2+\frac43\lambda^2V,
\]
等价于
\[
\int|W^+|^2
=2\pi^2(2\chi+3\tau)-\frac13\lambda^2V .
\]
故原 Step 2 的 \(16/3\) 确为四倍误差，修复后的 \(4/3\) 正确。

令
\[
M=X\#k\overline{\mathbb{CP}}^{\,2},\qquad
A=c_1^2(X)>0,\qquad p=k/A,
\]
并采用复定向，则
\[
2\chi(M)+3\tau(M)=A-k.
\]
LeBrun 1996 对 \(k>0\) 给出严格估计
\[
\int s^2>32\pi^2A.
\]
若 \(g\) Einstein，则
\[
16\lambda^2V>32\pi^2A,\qquad \lambda^2V>2\pi^2A,
\]
从而
\[
\int|W^+|^2
<
2\pi^2(A-k)-\frac23\pi^2A
=\pi^2A\left(\frac43-2p\right).
\]
左端非负，故当
\[
p\ge\frac23
\]
时矛盾；在 \(p=2/3\) 处，正是前述严格不等式给出 \(\int|W^+|^2<0\)。

因此脚本中

```python
"contradiction": coeff < 0
```

以及“contradiction begins only for \(p>2/3\)”是端点错误。应记录为：形式系数在 \(p=2/3\) 等于零，但实际上界是严格小于该系数，所以矛盾从 \(p\ge2/3\) 开始。JSON 的相应描述也应改为 \(k/A\ge2/3\)。

## 2. 混合估计与 \(1/3\) 阈值

LeBrun 2001 Proposition 3.1 给出
\[
F_+(g):=\frac1{4\pi^2}\int_M
\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu
\ge\frac23(a^+)^2.
\]
对于上述 blow-up，符号选择或凸包论证保证：对每个度量可选相应 Seiberg–Witten 类，使
\[
(a^+)^2\ge A.
\]
这里个别 blow-up 类的拓扑平方是 \(A-k\)，但曲率估计使用的是度量依赖的自对偶投影平方 \((a^+)^2\)，所以以 \(A\) 作下界是正确的。

于是
\[
F_+(g)\ge\frac23A.
\]
由 CGB 恒等式
\[
F_+(g)=A-k+\frac1{4\pi^2}\int\frac{|\mathring r|^2}{2},
\]
得到
\[
\int_M\frac{|\mathring r|^2}{2}\,d\mu
\ge4\pi^2\left(k-\frac A3\right). \tag{1}
\]
这证明 \(k>A/3\) 时 Einstein 不可能存在。

在端点 \(k=A/3\)，仅凭弱不等式 (1) 尚不能排除 Einstein；LeBrun 2001 Proposition 3.2 的等号刻画才是关键：有 blow-up 或 \(S^1\times S^3\) 手柄时，\(F_+\) 下界不能取等。因此其 Corollary 3.4 的准确结论是
\[
k\ge A/3\quad\Longrightarrow\quad M\text{ 不承载 Einstein 度量}.
\]
所以“混合阈值为 \(1/3\)”正确，但端点必须明确依赖等号排除，而不是只依赖 \(F_+\ge2A/3\)。对 \(k>0\)，来源实际上支持相应严格版本。

## 3. pinching 下界

假设
\[
\|\operatorname{Ric}_g+g\|_{\mathrm{op}}\le\delta<1.
\]
写 Ricci endomorphism 的特征值为 \(-1+e_i\)，其中 \(|e_i|\le\delta\)。则
\[
s=-4+\sum_i e_i,\qquad |s|\ge4(1-\delta),
\]
且
\[
|\mathring r|^2
=\sum_i(e_i-\bar e)^2
\le\sum_i e_i^2\le4\delta^2.
\]
所以
\[
\frac{s^2}{24}\ge\frac23(1-\delta)^2,\qquad
\int\frac{|\mathring r|^2}{2}\le2\delta^2V. \tag{2}
\]

设
\[
b(\delta)=\frac23(1-\delta)^2-2\delta^2.
\]
从 CGB 丢弃非负的 \(2|W^+|^2\)，得到
\[
A-k\ge\frac{V}{4\pi^2}b(\delta).
\]
当 \(b(\delta)>0\) 时，
\[
V\le\frac{4\pi^2(A-k)}{b(\delta)}. \tag{3}
\]
把 (1)、(2)、(3) 结合：
\[
\left(k-\frac A3\right)
\left[\frac23(1-\delta)^2-2\delta^2\right]
\le2\delta^2(A-k).
\]
将左边的 \(-2\delta^2(k-A/3)\) 移至右边，右端合并为
\[
2\delta^2\left[(A-k)+(k-A/3)\right]
=\frac43A\delta^2.
\]
因此
\[
\frac23\left(k-\frac A3\right)(1-\delta)^2
\le\frac43A\delta^2,
\]
即
\[
\boxed{\frac{\delta}{1-\delta}
\ge\sqrt{\frac{k-A/3}{2A}}
=\sqrt{\frac{p-1/3}{2}}.}
\]
故
\[
\delta\ge
\frac{\sqrt{(p-1/3)/2}}
{1+\sqrt{(p-1/3)/2}}.
\]
在 \(p=2/3\) 时，
\[
\delta\ge\frac1{1+\sqrt6}\approx0.289897949.
\]

这里须补充适用域。稳定定理假设
\[
T_+=A-k>0,
\]
所以直接应用范围是
\[
\frac13<p<1.
\]
此外
\[
b(\delta)>0
\iff
\delta<\frac1{1+\sqrt3}.
\]
这不会在 \(1/3<p<1\) 中留下漏洞：若 \(b(\delta)\le0\)，则已有
\[
\delta\ge\frac1{1+\sqrt3},
\]
而这比所要求的下界更强。应在证明中加入这个分情况。\(p=1\) 可单独得到端点值；\(p>1\) 时，上述平方根公式并未由此体积论证建立，不能无条件宣称。

抽象稳定定理中的
\[
\frac{\delta}{1-\delta}
\ge\sqrt{\frac{L_+-T_+}{3L_+}}
\]
常数也正确。其正归一化版本在纯代数上同样成立，因为只使用 \(s^2\) 与 \(|\mathring r|^2\)；但对这些 general-type blow-up，非零 monopole class 已排除 \(s\ge0\) 的度量，而 \(\|\operatorname{Ric}-g\|_{\rm op}<1\) 强制 \(s>0\)。因此该家族的正分支实际上为空，实质内容是负归一化分支。

## 4. 必须显式列出的几何假设

上述应用依赖：

- \(M\) 是闭、光滑、定向四维流形，并采用 \(X\) 的复定向；否则应改用 \(T_-\)、\(W^-\) 或反向定向。
- \(X\) 是 minimal complex surface of general type，\(A=c_1^2(X)>0\)。
- 每个度量都必须有适用的 monopole/polarized Seiberg–Witten 类。2003 年的全局 monopole-class 表述通常假设 \(b_+\ge2\)；\(b_+=1\) 情形不能仅引用该定义，而应引用 LeBrun 1996/2001 的 polarization/chamber 论证。所给 2001 来源确实覆盖 general-type blow-up 的全体度量。
- \(k>0\) 用于 1996 标量估计的严格性和 2001 混合估计的等号排除。
- \(k=A/3\) 与 \(k=2A/3\) 的“不存在”都含有严格/等号分析，不能只看弱不等式的符号。

## 5. lens-space 正曲率塌缩

令
\[
L(m,1)=S^3/\mathbb Z_m
\]
带单位圆球商度量 \(g_m\)。则
\[
\sec_{g_m}=1,\qquad \operatorname{Ric}_{g_m}=2g_m.
\]
取 \(h_m=2g_m\)。常数缩放不改变 Ricci 的 \((0,2)\)-张量，因此
\[
\operatorname{Ric}_{h_m}=2g_m=h_m;
\]
即归一化正 pinching 参数恰为零。同时
\[
\operatorname{Vol}(L(m,1),h_m)
=2^{3/2}\frac{2\pi^2}{m}\to0,
\]
且 \(m\ge2\) 时
\[
\operatorname{inj}(L(m,1),h_m)
=\frac{\sqrt2\,\pi}{m}\to0.
\]
曲率和直径保持一致有界，所以这是精确 Einstein、 bounded-curvature 的真实塌缩。

其正确含义是：紧正 Ricci pinching 不排除塌缩。这里流形拓扑随 \(m\) 改变，每个成员本身已承载 Einstein 度量，因此它不是 Yau 26 的反例，只是否定“紧 pinching 蕴含非塌缩/拓扑有限性”的推断。Berger 固定丛缩纤维出现 Ricci 各向异性，只说明那一种固定拓扑、固定连接的缩放机制失败，不能推广为一般非塌缩定理。

## 6. 对完整 Yau 26 命题的边界

这些结果只处理四维特定 Seiberg–Witten blow-up 家族，既没有构造 Yau 26 所需的维数常数，也没有处理任意流形或其他维数，更没有给出反例。严格得到的是：

- 固定 \(p>1/3\) 且 \(p<1\) 时，该积分障碍本身给出统一正的负 Ricci pinching 间隙，因此这些流形不能在固定障碍裕量下满足 \(\delta_-\to0\)。
- 该机制尚未排除 \(p\to1/3^+\) 的零裕量序列，但材料中也没有构造任何对应的紧负 pinching 度量。
- “所有已知 no-Einstein 例子都如此”或“任意 Einstein 障碍都稳定”超出所给来源；严格结论仅适用于与四维 CGB 恒等式相连、对所有度量成立的积分下界。

另有一个直接的全命题限制：若四维候选常数满足
\[
c_4<0<C_4,
\]
则不可能成立。任取一个不承载 Einstein 度量的 LeBrun 流形及任意度量 \(g_0\)，对 \(t\to\infty\)，度量 \(tg_0\) 的 Ricci endomorphism 特征值趋于零，故最终满足
\[
c_4\,tg_0\le \operatorname{Ric}_{tg_0}\le C_4\,tg_0,
\]
但底流形仍无 Einstein 度量。因此任何可能成立的四维 Yau 区间至少不能跨过零。