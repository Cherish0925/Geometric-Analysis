# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 70,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step70_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step70_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the peripheral algebraic reduction for the anisotropic quotient construction. The claim: for a one-cusped orientable hyperbolic 4-manifold piece P with cusp lattice Λ≅Z³ and a primitive character φ:π₁(P)→Z with φ|Λ=dℓ (ℓ primitive, d≥1), the cyclic mod-N cover (N coprime to d) has one cusp with peripheral lattice ker(dℓ mod N) = {v∈Λ: d ℓ(v)≡0 mod N}, which has type (N,1,1) in the basis {ℓ,e₂,e₃}. VERIFY: (1) Is this algebraic claim correct? (2) Does the resulting cover remain a single-cusped manifold (i.e., does the peripheral inclusion being surjective mod N guarantee one cusp)? (3) For the long exact sequence H₁(T³)→H₁(M̄)→H₁(M̄,T³)→0 with Poincaré-Lefschetz H₁(M̄,T³)≅H³(M̄), derive necessary and sufficient conditions on M̄ for the peripheral image in H₁(M̄;Q) to be nonzero. (4) For the Slavich orientable one-cusped 24-cell manifold with H₁≅Z⊕Z₃, determine whether the peripheral image is nonzero.

## Integrated Scientific Memo

## 核验结论

设
\[
G=\pi_1(P),\qquad \Lambda\simeq \mathbb Z^3,\qquad
q_N:G\xrightarrow{\phi}\mathbb Z\to\mathbb Z/N,
\]
并令 \(H_N=\ker q_N\)。

### 1. 外周子格计算正确，但基底记号需修正

因为 \(\phi\) primitive，即 \(\phi:G\to\mathbb Z\) 满射，所以 \(q_N\) 满射，\(H_N\) 给出连通正则 \(N\) 重循环覆盖。

限制到外周群：
\[
q_N(v)=d\ell(v)\pmod N,
\]
故
\[
H_N\cap\Lambda
=\{v\in\Lambda:d\ell(v)\equiv0\pmod N\}.
\]
当 \((d,N)=1\) 时，乘以 \(d\) 在 \(\mathbb Z/N\) 中可逆，所以
\[
H_N\cap\Lambda=\ker(\ell\bmod N).
\]

这里 \(\ell\in\operatorname{Hom}(\Lambda,\mathbb Z)\) 是余向量，不能写成格基向量。应选适配基
\[
f_1,e_2,e_3,\qquad
\ell(f_1)=1,\quad e_2,e_3\in\ker\ell.
\]
于是
\[
H_N\cap\Lambda
=\langle Nf_1,e_2,e_3\rangle ,
\qquad [\Lambda:H_N\cap\Lambda]=N.
\]
因此方向伸长类型确为 \((N,1,1)\)；按通常递增 Smith 不变量记法则是 \((1,1,N)\)。

更一般地，若 \(g=(d,N)\)，则
\[
H_N\cap\Lambda
=\left\langle \frac N g f_1,e_2,e_3\right\rangle .
\]

需要区分：这是**抽象子格类型**，并不推出 \(f_1\) 与 \(\ker\ell\) 在给定平坦 cusp 度量下正交。一般会留下与 \(N\) 无关的固定剪切。因此 Step 69 所需的精确矩形度量类型还要求额外的仿射匹配或过渡来吸收该剪切。

### 2. 覆盖恰有一个 cusp

原流形只有一个 cusp。其逆像的分支数为双陪集数
\[
|H_N\backslash G/\Lambda|.
\]
由于 \(H_N\triangleleft G\)，这等于
\[
[\mathbb Z/N:q_N(\Lambda)].
\]
又因 \(\ell(\Lambda)=\mathbb Z\)，
\[
q_N(\Lambda)=d\mathbb Z\bmod N,
\]
所以
\[
\#\{\text{上方 cusps}\}=(d,N).
\]

因此
\[
\boxed{\text{覆盖单 cusp}
\iff q_N|_\Lambda\text{ 满射}
\iff (d,N)=1.}
\]
在互素情形，唯一 cusp 横截面仍为 \(T^3\)，且它以次数 \(N\) 覆盖原 cusp 横截面。

### 3. 外周像非零的充要条件

令 \(\bar M\) 为紧核，\(\partial\bar M=T^3\)。取 \(\mathbb Q\) 系数。相对同调正合列给出
\[
H_1(T^3)\xrightarrow{i_*}H_1(\bar M)
\xrightarrow{j}H_1(\bar M,T^3)
\longrightarrow H_0(T^3)\longrightarrow H_0(\bar M).
\]
由于边界和 \(\bar M\) 都连通，最后一箭头是同构，故 \(j\) 满射且
\[
\operatorname{im}i_*=\ker j.
\]
Poincaré–Lefschetz 对偶给出
\[
H_1(\bar M,T^3;\mathbb Q)\cong H^3(\bar M;\mathbb Q).
\]
因此
\[
\boxed{
\operatorname{rank}_{\mathbb Q}\operatorname{im}i_*
=b_1(\bar M)-b_3(\bar M).
}
\]

于是下列条件等价：

\[
\operatorname{im}\bigl(H_1(T^3;\mathbb Q)\to H_1(\bar M;\mathbb Q)\bigr)\ne0;
\]
\[
b_1(\bar M)>b_3(\bar M);
\]
\[
i^*:H^1(\bar M;\mathbb Q)\to H^1(T^3;\mathbb Q)\quad\text{非零};
\]
存在整数特征
\[
\phi:\pi_1(\bar M)\to\mathbb Z
\]
使 \(\phi|_\Lambda\ne0\)。

最后一个表述中，先得到非零整数类后除去其整体公因数，即可取 \(\phi\) primitive；其外周限制唯一写为
\[
\phi|_\Lambda=d\ell,\qquad d\ge1,\quad \ell\text{ primitive}.
\]

附带地，由完整正合列的秩计算，
\[
\operatorname{rank}\operatorname{im}
\bigl(H_2(T^3;\mathbb Q)\to H_2(\bar M;\mathbb Q)\bigr)
=3-b_1+b_3.
\]
因此
\[
b_2\ge3-b_1+b_3,\qquad
\chi(\bar M)=1-b_1+b_2-b_3\ge4-2b_1.
\]
这是检查候选 cusp piece 同调数据的一项有用约束。

### 4. \(H_1\simeq\mathbb Z\oplus\mathbb Z_3\) 尚不足以判定 Slavich 例子

给定
\[
H_1(\bar M;\mathbb Z)\simeq\mathbb Z\oplus\mathbb Z_3
\]
只能推出 \(b_1=1\)。故
\[
\operatorname{rank}_{\mathbb Q}\operatorname{im}i_*
=1-b_3.
\]
正合性保证 \(b_3\le1\)，所以只有两种情况：

- \(b_3=0\)：外周像的有理秩为 \(1\)，所需 anisotropic character cover 存在；
- \(b_3=1\)：外周像在有理同调中为零，不存在外周限制非零的 \(\pi_1(\bar M)\to\mathbb Z\)。外周像仍可能落入 \(\mathbb Z_3\)，但这对循环整数特征无用。

因此，基于当前提供材料，Slavich 流形的答案是：

\[
\boxed{
\text{外周像非零}
\iff b_3(\bar M)=0,
}
\]
但给出的 \(H_1\) 数据本身不能决定 \(b_3\)，故不能严谨断言“是”或“否”。

决定该例子的最小附加数据可以是以下任一项：

1. \(b_3(\bar M)\)；
2. \(b_2(\bar M)\) 与 \(\chi(\bar M)\)，因为
   \[
   \chi=1-b_1+b_2-b_3=b_2-b_3;
   \]
3. cusp 三个生成元在
   \[
   H_1(\bar M)\simeq\mathbb Z\oplus\mathbb Z_3
   \]
   中的阿贝尔化像。

若其自由坐标为 \(m_1,m_2,m_3\)，则外周像非零恰当且仅当
\[
(m_1,m_2,m_3)\ne(0,0,0).
\]
此时
\[
d=\gcd(|m_1|,|m_2|,|m_3|),
\]
而 \((m_1/d,m_2/d,m_3/d)\) 给出 primitive \(\ell\)。

综上，循环覆盖代数与单 cusp 论证成立；Slavich 候选是否实际可用于 \((N,1,1)\) 构造，仍精确取决于其 \(b_3\) 或外周阿贝尔化矩阵。