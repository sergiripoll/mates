---
title: Vectors i geometria a l’espai: Teoria
tematitol: Vectors i geometria a l’espai
curs: 2n
modalitat: cientific
tema: vectors
bloc: teoria
ordre: 1
---
# Vectors i geometria a l’espai: Teoria

------------------------------------------------------------------------

  
**VECTORS A L’ESPAI**  
Resum de teoria i exercicis resolts  

------------------------------------------------------------------------

  
**2n de Batxillerat · Matemàtiques**  
Unitat 6  

> **Continguts**  
>
> |     |                                    |
> |:----|:-----------------------------------|
> | 1\. | Coordenades i vectors a l’espai    |
> | 2\. | Operacions amb vectors             |
> | 3\. | Dependència i independència lineal |
> | 4\. | Base i components en una base      |
> | 5\. | Producte escalar                   |
> | 6\. | Producte vectorial i mixt          |
> | 7\. | Exercicis de repàs                 |

Document generat per repassar i practicar

## Coordenades a l’espai

> **📘 Teoria**
>
> **Sistema de coordenades cartesianes**
>
> Un punt $P$ de l’espai queda determinat per tres coordenades reals: $$P(x, y, z) \quad \text{amb } x, y, z \in \mathbb{R}$$
>
> - **Eix $X$:** punts de la forma $(x, 0, 0)$
>
> - **Eix $Y$:** punts de la forma $(0, y, 0)$
>
> - **Eix $Z$:** punts de la forma $(0, 0, z)$
>
> - **Pla $XY$:** punts de la forma $(x, y, 0)$
>
> - **Pla $XZ$:** punts de la forma $(x, 0, z)$
>
> - **Pla $YZ$:** punts de la forma $(0, y, z)$

> **✏️ Exemple**
>
> **Identificació de punts**
>
> - $A(5, 3, 2)$ és un punt general de l’espai
>
> - $B(0, 4, 0)$ és un punt de l’eix $Y$
>
> - $C(2, 0, -1)$ pertany al pla $XZ$
>
> - $D(-3, 0, 0)$ pertany a l’eix $X$ (a distància 3 en sentit negatiu)

## Vectors: definició i operacions bàsiques

### Vector entre dos punts

> **📘 Teoria**
>
> **Components d’un vector**
>
> Donats els punts $A(a_1, a_2, a_3)$ i $B(b_1, b_2, b_3)$, el vector $\overrightarrow{AB}$ és: $$\overrightarrow{AB} = B - A = (b_1 - a_1,\; b_2 - a_2,\; b_3 - a_3)$$ El **mòdul** (longitud) del vector és: $$\left|\vec{AB}\right| = \sqrt{(b_1-a_1)^2 + (b_2-a_2)^2 + (b_3-a_3)^2}$$

> **✏️ Exemple**
>
> **Càlcul de components i mòdul**
>
> Donats $A(-3, -1, 5)$ i $B(2, -4, -1)$: $$\overrightarrow{AB} = (2-(-3),\; -4-(-1),\; -1-5) = (5, -3, -6)$$ $$\left|\vec{AB}\right| = \sqrt{5^2 + (-3)^2 + (-6)^2} = \sqrt{25 + 9 + 36} = \sqrt{70}$$

### Operacions amb vectors

> **📘 Teoria**
>
> **Suma, resta i producte per escalar**
>
> Si $\vec{u} = (u_1, u_2, u_3)$ i $\vec{v} = (v_1, v_2, v_3)$, i $k \in \mathbb{R}$: $$\vec{u} + \vec{v} = (u_1+v_1,\; u_2+v_2,\; u_3+v_3)$$ $$k\,\vec{u} = (k\,u_1,\; k\,u_2,\; k\,u_3)$$ $$|k\,\vec{u}| = |k|\cdot|\vec{u}|$$

> **✏️ Exemple**
>
> **Combinació de vectors**
>
> Siguin $\vec{a} = (2,-4,5)$, $\vec{b} = (-5,7,-1)$ i $\vec{c} = (-5,2,3)$.
>
> **Calcula $\vec{a} + \vec{b} - \vec{c}$:** $$(2,-4,5) + (-5,7,-1) - (-5,2,3) = (2-5+5,\; -4+7-2,\; 5-1-3) = (2, 1, 1)$$
>
> **Calcula $-3\vec{a} + 2\vec{b} - 2\vec{c}$:** $$-3(2,-4,5) + 2(-5,7,-1) - 2(-5,2,3) = (-6,12,-15)+(-10,14,-2)+(10,-4,-6)$$ $$= (-6, 22, -23)$$

### Vector unitari

> **📘 Teoria**
>
> **Vector unitari**
>
> El **vector unitari** en la direcció i sentit de $\vec{v}$ és: $$\hat{u} = \frac{\vec{v}}{|\vec{v}|}$$ Té mòdul 1 i mateixa direcció i sentit que $\vec{v}$.

> **✏️ Exemple**
>
> **Càlcul del vector unitari**
>
> Sigui $\vec{a} = (1, -3, 2)$: $$|\vec{a}| = \sqrt{1+9+4} = \sqrt{14}$$ $$\hat{u} = \frac{1}{\sqrt{14}}(1, -3, 2) = \left(\frac{1}{\sqrt{14}},\; \frac{-3}{\sqrt{14}},\; \frac{2}{\sqrt{14}}\right)$$

> **⚠️ Atenció**
>
> Dos vectors **oposats** tenen el mateix mòdul, la mateixa direcció i **sentits contraris**. Si $\vec{v} = (v_1, v_2, v_3)$, el seu oposat és $-\vec{v} = (-v_1, -v_2, -v_3)$.

> 1.  Donats $A(-3,-1,5)$, $B(2,-4,-1)$, $C(0,-4,1)$, $D(-3,5,-6)$. Calcula les components i el mòdul de $\overrightarrow{AB}$ i $\overrightarrow{CD}$.
>
> 2.  El vector $\vec{v} = (2,-6,-1)$ té origen al punt $M$. Si l’extrem és $N(1,0,-4)$, troba les coordenades de $M$.
>
> 3.  Donats $\vec{a}=(2,-4,5)$, $\vec{b}=(-5,7,-1)$ i $\vec{c}=(-5,2,3)$:
>
>     1.  Calcula $\frac{1}{2}(-\vec{a} - 3\vec{b} + 3\vec{c})$
>
>     2.  Calcula $\vec{a} - (\vec{c} - \vec{b})$
>
> 4.  Troba el vector unitari de $\vec{b} = (3,-4,0)$.
>
> 5.  Donats els punts $A(2,4,5)$ i $B(4,6,t)$, calcula els valors de $t$ sabent que $|\overrightarrow{AB}| = 3$.

<details><summary>Solució</summary>

1.  $\overrightarrow{AB}=(5,-3,-6)$, $|\overrightarrow{AB}|=\sqrt{70}$;$\overrightarrow{CD}=(-3,9,-7)$, $|\overrightarrow{CD}|=\sqrt{139}$

2.  De $\vec{v}=\overrightarrow{MN}$: $(2,-6,-1)=(1-x,-y,-4-z)$ $\Rightarrow$ $M(-1, 6, -3)$

3.  \(a\) $\left(-1, -\frac{11}{2}, \frac{7}{2}\right)$ (b) $(2, 1, 1)$

4.  $|\vec{b}|=5 \Rightarrow \hat{u}=\left(\frac{3}{5}, -\frac{4}{5}, 0\right)$

5.  $\overrightarrow{AB}=(2,2,t-5)$, $|\overrightarrow{AB}|=3 \Rightarrow t^2-10t+24=0 \Rightarrow t_1=6$, $t_2=4$

</details>

## Dependència i independència lineal

> **📘 Teoria**
>
> **Combinació lineal**
>
> El vector $\vec{t}$ és **combinació lineal** dels vectors $\vec{u}$, $\vec{v}$, $\vec{w}$ si existeixen $\alpha, \beta, \gamma \in \mathbb{R}$ tals que: $$\vec{t} = \alpha\,\vec{u} + \beta\,\vec{v} + \gamma\,\vec{w}$$

> **📘 Teoria**
>
> **Vectors linealment dependents/independents**
>
> Un conjunt de vectors és **linealment dependent (LD)** si algun d’ells es pot expressar com a combinació lineal dels altres.
>
> És **linealment independent (LI)** si l’única combinació lineal que dóna el vector nul té tots els escalars iguals a zero: $$\lambda_1\vec{v}_1 + \lambda_2\vec{v}_2 + \cdots + \lambda_n\vec{v}_n = \vec{0} \implies \lambda_1 = \lambda_2 = \cdots = \lambda_n = 0$$
>
> **Criteri pràctic:** tres vectors $\vec{u}$, $\vec{v}$, $\vec{w}$ de $\mathbb{R}^3$ són **LD** si i només si: $$\begin{vmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{vmatrix} = 0$$

> **✏️ Exemple**
>
> **Dependència lineal**
>
> **Vectors $\vec{b}_1=(-1,0,2)$, $\vec{b}_2=(2,0,-4)$, $\vec{b}_3=(3,-1,5)$: LD o LI?**
>
> Observem que $\vec{b}_2 = -2\,\vec{b}_1$ (components proporcionals: $\frac{2}{-1}=\frac{0}{0}=\frac{-4}{2}=-2$). Per tant, $\vec{b}_2$ és combinació lineal de $\vec{b}_1$, i els tres vectors són **linealment dependents**.
>
> **Vectors $\vec{c}_1=(1,-2,4)$, $\vec{c}_2=(0,2,1)$, $\vec{c}_3=(-1,-3,0)$: LD o LI?**
>
> Plantegem $\vec{c}_3 = \lambda_1\vec{c}_1 + \lambda_2\vec{c}_2$: $$\begin{cases} -1 = \lambda_1 \\ -3 = -2\lambda_1 + 2\lambda_2 \\ 0 = 4\lambda_1 + \lambda_2 \end{cases}$$ El sistema no té solució $\Rightarrow$ vectors **linealment independents**.

### Punts alineats

> **📘 Teoria**
>
> **Condició d’alineació de punts**
>
> Els punts $A$, $B$, $C$ estan **alineats** si i només si els vectors $\overrightarrow{AB}$ i $\overrightarrow{AC}$ (o $\overrightarrow{BC}$) són **proporcionals**, és a dir: $$\frac{AB_1}{AC_1} = \frac{AB_2}{AC_2} = \frac{AB_3}{AC_3}$$ Equivalentment, $\overrightarrow{AB} = \lambda\,\overrightarrow{AC}$ per a algun $\lambda \in \mathbb{R}$.

> **✏️ Exemple**
>
> **Comprovació d’alineació**
>
> **Comprova que $A(3,-4,1)$, $B(2,-1,4)$ i $C(0,5,10)$ estan alineats.** $$\overrightarrow{AB} = (-1, 3, 3), \quad \overrightarrow{BC} = (-2, 6, 6)$$ $$\overrightarrow{BC} = 2\,\overrightarrow{AB} \implies \text{els punts estan alineats.}$$

> 1.  Esbrina si els conjunts de vectors següents són LD o LI:
>
>     1.  $\vec{a}_1=(2,-1,3)$ i $\vec{a}_2=\left(-\frac{2}{3},\frac{1}{3},-1\right)$
>
>     2.  $\vec{u}_1=(1,2,-3)$, $\vec{u}_2=(3,0,-4)$, $\vec{u}_3=(2,1,-\frac{7}{2})$
>
> 2.  Esbrina si el vector $\vec{v}=(3,-4,1)$ és combinació lineal de $\vec{v}_1=(-1,2,3)$ i $\vec{v}_2=(4,-6,-2)$.
>
> 3.  Sabem que $P$, $Q$ i $R$ estan alineats. Si $P(1,-2,3)$ i $Q(4,1,5)$, determina les coordenades $x$ i $y$ del punt $R$ sabent que $z=9$.
>
> 4.  Expressa $\vec{v}=(2,-4,-1)$ en combinació lineal de $\vec{v}_1=(1,-2,3)$, $\vec{v}_2=(4,1,2)$ i $\vec{v}_3=(1,0,0)$.
>
> 5.  Per a quin valor de $p$ els vectors $\vec{u}_1=(1,2,-3)$, $\vec{u}_2=(3,0,-4)$ i $\vec{u}_3=(2,1,p)$ són LD? Per a quins valors de $p$ són LI?

<details><summary>Solució</summary>

1.  \(a\) $\vec{a}_1 = -3\,\vec{a}_2$ $\Rightarrow$ **LD**.(b) Plantejant el sistema s’obté $\lambda_1=\lambda_2=\frac{1}{2}$, $p=-\frac{7}{2}$ $\Rightarrow$ **LD**.

2.  $\vec{v} = \lambda\vec{v}_1 + \mu\vec{v}_2 \Rightarrow \lambda=\mu=1$. Sí, $\vec{v}=\vec{v}_1+\vec{v}_2$.

3.  $\overrightarrow{PQ}=(3,3,2)$, $\overrightarrow{PR}=(x-1,y+2,6)=k(3,3,2) \Rightarrow k=3 \Rightarrow R(10,7,9)$.

4.  $\lambda_1=1$, $\lambda_2=-2$, $\lambda_3=9$: $\vec{v}=\vec{v}_1 - 2\vec{v}_2 + 9\vec{v}_3$.

5.  LD si $p=-\frac{7}{2}$; LI si $p \neq -\frac{7}{2}$.

</details>

## Base i components en una base

> **📘 Teoria**
>
> **Base de $\mathbb{R}^3$**
>
> Tres vectors no nuls de $\mathbb{R}^3$ formen una **base** si i només si són **linealment independents**.
>
> La **base canònica** és $\{\vec{e}_1, \vec{e}_2, \vec{e}_3\} = \{(1,0,0),(0,1,0),(0,0,1)\}$.
>
> Si $\mathcal{B}=\{\vec{v}_1, \vec{v}_2, \vec{v}_3\}$ és una base, tot vector $\vec{w}$ es pot expressar de manera **única** com: $$\vec{w} = \lambda_1\vec{v}_1 + \lambda_2\vec{v}_2 + \lambda_3\vec{v}_3$$ Els escalars $(\lambda_1, \lambda_2, \lambda_3)$ s’anomenen **components de $\vec{w}$ en la base $\mathcal{B}$**.

> **✏️ Exemple**
>
> **Components en una base**
>
> **Siguin $\vec{v}_1=(1,0,-3)$, $\vec{v}_2=(2,-1,1)$ i $\vec{v}_3=(0,-2,3)$. Comprova que formen base i troba les components de $\vec{v}=(3,2,4)$ en aquesta base.**
>
> Els vectors són LI (determinant $\neq 0$), per tant formen base.
>
> Plantegem $(3,2,4) = \lambda_1(1,0,-3)+\lambda_2(2,-1,1)+\lambda_3(0,-2,3)$: $$\begin{cases} 3 = \lambda_1 + 2\lambda_2 \\ 2 = -\lambda_2 - 2\lambda_3 \\ 4 = -3\lambda_1 + \lambda_2 + 3\lambda_3 \end{cases}
\implies \lambda_1 = -\frac{31}{11},\; \lambda_2 = \frac{32}{11},\; \lambda_3 = -\frac{27}{11}$$

> **✏️ Exemple**
>
> **Canvi de base**
>
> **El vector $\vec{v}=(9,6,-4)$ en base canònica. Troba els components en $\mathcal{B}=\{(2,3,0),(3,1,-2),(1,1,0)\}$.**
>
> $(9,6,-4) = v_1(2,3,0)+v_2(3,1,-2)+v_3(1,1,0)$ $$\begin{cases} 9=2v_1+3v_2+v_3 \\ 6=3v_1+v_2+v_3 \\ -4=-2v_2 \end{cases}
\implies v_1=1,\; v_2=2,\; v_3=1$$ Components en $\mathcal{B}$: $(1,2,1)$.

> 1.  Comprova si els vectors $\vec{v}_1=(1,0,-3)$, $\vec{v}_2=(2,-1,1)$ i $\vec{v}_3=(0,-2,3)$ formen una base de $\mathbb{R}^3$.
>
> 2.  Per a quins valors de $k$ els vectors $\vec{v}_1=(1,1,1)$, $\vec{v}_2=(1,k,1)$ i $\vec{v}_3=(1,1,k)$ formen una base de $\mathbb{R}^3$?
>
> 3.  Els components del vector $\vec{v}$ en la base $\mathcal{B}=\{(1,2,-1),(2,1,0),(-1,3,1)\}$ són $(2,-3,4)$. Troba els components de $\vec{v}$ en la base canònica.
>
> 4.  En la base $\mathcal{B}=\{(1,1,-2),(3,-1,4),(5,-2,0)\}$, els components d’un vector $\vec{v}$ són $(2,-3,0)$. Determina els components en la base canònica.
>
> 5.  Esbrina si els punts $A(1,-2,1)$, $B(0,0,-1)$, $C(-2,-1,3)$ i $D(1,-1,4)$ són coplanaris.

<details><summary>Solució</summary>

1.  El determinant $\neq 0$ $\Rightarrow$ formen base.

2.  $k=1$ fa que el sistema sigui compatible indeterminat; per tant formen base per a tot $k\neq 1$.

3.  $\vec{v}=2(1,2,-1)-3(2,1,0)+4(-1,3,1)=(-8,13,2)$.

4.  $\vec{v}=2(1,1,-2)-3(3,-1,4)+0\cdot(5,-2,0)=(-7,5,-16)$.

5.  $\overrightarrow{AB}=(-1,2,-2)$, $\overrightarrow{AC}=(-3,1,2)$, $\overrightarrow{AD}=(0,1,3)$. El sistema $\overrightarrow{AB}=\alpha\overrightarrow{AC}+\beta\overrightarrow{AD}$ no té solució $\Rightarrow$ **no coplanaris**.

</details>

## Producte escalar

> **📘 Teoria**
>
> **Producte escalar**
>
> Donats $\vec{u}=(u_1,u_2,u_3)$ i $\vec{v}=(v_1,v_2,v_3)$: $$\vec{u}\cdot\vec{v} = u_1v_1 + u_2v_2 + u_3v_3$$ Interpretació geomètrica: $$\vec{u}\cdot\vec{v} = |\vec{u}|\,|\vec{v}|\cos\theta$$ on $\theta$ és l’angle que formen els dos vectors. D’aquí: $$\cos\theta = \frac{\vec{u}\cdot\vec{v}}{|\vec{u}|\,|\vec{v}|}$$
>
> **Perpendiculars:** $\vec{u}\perp\vec{v} \iff \vec{u}\cdot\vec{v}=0$  
> **Mòdul:** $|\vec{v}|^2 = \vec{v}\cdot\vec{v}$

> **⚠️ Atenció**
>
> - Si $\vec{u}\cdot\vec{v} > 0$ $\Rightarrow$ angle **agut** ($0 < \theta < 90°$)
>
> - Si $\vec{u}\cdot\vec{v} < 0$ $\Rightarrow$ angle **obtús** ($90° < \theta < 180°$)
>
> - Si $\vec{u}\cdot\vec{v} = 0$ $\Rightarrow$ vectors **perpendiculars** ($\theta = 90°$)

> **✏️ Exemple**
>
> **Angle entre vectors i perpendicularitat**
>
> **Calcula l’angle entre $\vec{a}=(1,-2,1)$ i $\vec{b}=(3,0,-4)$.** $$\vec{a}\cdot\vec{b} = 3+0-4=-1,\quad |\vec{a}|=\sqrt{6},\quad |\vec{b}|=5$$ $$\cos\theta = \frac{-1}{5\sqrt{6}} \implies \theta \approx 94{,}68°$$
>
> **Troba el vector $\vec{w}=(w_1,w_2)$ perpendicular a $\vec{v}=(2,-1)$ amb $|\vec{w}|=5$.** $$\vec{v}\cdot\vec{w}=0 \implies 2w_1-w_2=0 \implies w_2=2w_1$$ $$w_1^2+w_2^2=25 \implies 5w_1^2=25 \implies w_1=\pm\sqrt{5}$$ Les dues solucions: $\vec{w}_1=(\sqrt{5},2\sqrt{5})$ i $\vec{w}_2=(-\sqrt{5},-2\sqrt{5})$ (vectors oposats).

> **✏️ Exemple**
>
> **Angles d’un triangle**
>
> **Triangle de vèrtexs $A(1,2,-1)$, $B(2,1,0)$, $C(-1,0,1)$. Calcula els angles.**
>
> $\overrightarrow{AB}=(1,-1,1)$, $\overrightarrow{AC}=(-2,-2,2)$, $\overrightarrow{BC}=(-3,-1,1)$
>
> $$\cos\hat{A} = \frac{\overrightarrow{AB}\cdot\overrightarrow{AC}}{|\overrightarrow{AB}||\overrightarrow{AC}|} = \frac{-2-2-2}{\sqrt{3}\cdot\sqrt{12}} \approx 0{,}333 \implies \hat{A}\approx 70{,}5°$$ Anàlogament: $\hat{B}\approx 80°$, $\hat{C}\approx 29{,}5°$. Verif.: $\hat{A}+\hat{B}+\hat{C}=180°$.

> 1.  Siguin $\vec{a}=(1,-2,1)$, $\vec{b}=(3,0,-4)$ i $\vec{c}=(-2,5,1)$. Calcula:
>
>     1.  $\vec{a}\cdot(\vec{b}+\vec{c})$
>
>     2.  $(\vec{a}\cdot\vec{b})\cdot\vec{c}$
>
>     3.  L’angle format per $\vec{a}$ i $\vec{b}$
>
> 2.  El vector $\vec{v}=(v_1,v_2,0)$ és perpendicular a $\vec{w}=(-4,3,1)$. Calcula les components de $\vec{v}$ sabent que $|\vec{v}|=5$.
>
> 3.  $\vec{v}$ i $\vec{w}$ són vectors de mòduls $2$ i $4$ respectivament. Formen un angle de $60°$. Calcula $k$ perquè $\vec{v}+k\vec{w}$ sigui perpendicular a $\vec{v}$.
>
> 4.  Els punts $P(1,2,-1)$, $Q(2,-1,3)$ i $R(1,1,0)$ són tres vèrtexs consecutius d’un paral·lelogram. Determina el quart vèrtex $S$ i calcula els angles del paral·lelogram.

<details><summary>Solució</summary>

1.  \(a\) $\vec{b}+\vec{c}=(1,5,-3)$; $\vec{a}\cdot(\vec{b}+\vec{c})=1-10-3=-12$.(b) $(\vec{a}\cdot\vec{b})\vec{c}=(-1)(-2,5,1)=(2,-5,-1)$.(c) $\theta\approx94{,}68°$.

2.  Sistema: $-4v_1+3v_2=0$ i $v_1^2+v_2^2=25$ $\Rightarrow$ $v_1=\pm3$, $v_2=\pm4$.

3.  $(\vec{v}+k\vec{w})\cdot\vec{v}=0 \Rightarrow |\vec{v}|^2+k(\vec{v}\cdot\vec{w})=0 \Rightarrow 4+k\cdot4=0 \Rightarrow k=-1$.

4.  $\overrightarrow{PQ}=(1,-3,4)=\overrightarrow{SR}$ $\Rightarrow$ $S(0,4,-4)$. Angles: $\hat{P}=\hat{R}\approx174{,}8°$, $\hat{Q}=\hat{S}\approx5{,}2°$.

</details>

## Producte vectorial

> **📘 Teoria**
>
> **Producte vectorial**
>
> Donats $\vec{u}=(u_1,u_2,u_3)$ i $\vec{v}=(v_1,v_2,v_3)$: $$\vec{u}\times\vec{v} =
\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k} \\
u_1 & u_2 & u_3 \\
v_1 & v_2 & v_3
\end{vmatrix}
= (u_2v_3-u_3v_2,\; u_3v_1-u_1v_3,\; u_1v_2-u_2v_1)$$
>
> **Propietats fonamentals:**
>
> - $\vec{u}\times\vec{v}$ és perpendicular a $\vec{u}$ i a $\vec{v}$.
>
> - $|\vec{u}\times\vec{v}|$ = àrea del paral·lelogram construït sobre $\vec{u}$ i $\vec{v}$.
>
> - Àrea del triangle de base $\vec{u}$, $\vec{v}$: $A_\triangle = \frac{1}{2}|\vec{u}\times\vec{v}|$
>
> - $\vec{u}\times\vec{v} = \vec{0} \iff \vec{u}$ i $\vec{v}$ són proporcionals (paral·lels).

> **✏️ Exemple**
>
> **Càlcul del producte vectorial**
>
> **Calcula $\vec{u}\times\vec{v}$ amb $\vec{u}=(2,1,-1)$ i $\vec{v}=(1,3,2)$.** $$\vec{u}\times\vec{v} =
\begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ 2 & 1 & -1 \\ 1 & 3 & 2 \end{vmatrix}
= \vec{i}(1\cdot2-(-1)\cdot3) - \vec{j}(2\cdot2-(-1)\cdot1) + \vec{k}(2\cdot3-1\cdot1)$$ $$= \vec{i}(2+3) - \vec{j}(4+1) + \vec{k}(6-1) = (5,-5,5)$$ **Comprovació:** $(5,-5,5)\cdot(2,1,-1)=10-5-5=0$ ✓ i $(5,-5,5)\cdot(1,3,2)=5-15+10=0$ ✓

## Producte mixt i volums

> **📘 Teoria**
>
> **Producte mixt**
>
> Donats $\vec{u}=(u_1,u_2,u_3)$, $\vec{v}=(v_1,v_2,v_3)$ i $\vec{w}=(w_1,w_2,w_3)$: $$[\vec{u},\vec{v},\vec{w}] =
\begin{vmatrix}
u_1 & u_2 & u_3 \\
v_1 & v_2 & v_3 \\
w_1 & w_2 & w_3
\end{vmatrix}$$
>
> | **Figura**                  |                                    **Volum**                                     |     |
> |:----------------------------|:--------------------------------------------------------------------------------:|:---:|
> | Paral·lelepípede $ABCDEFGH$ | $V = \left|[\overrightarrow{AB},\overrightarrow{AD},\overrightarrow{AE}]\right|$ |     |
> | Piràmide $ABCDE$            |             $V = \dfrac{1}{3}\left|[\vec{u},\vec{v},\vec{w}]\right|$             |     |
> | Tetraedre $ABDE$            |             $V = \dfrac{1}{6}\left|[\vec{u},\vec{v},\vec{w}]\right|$             |     |

> **✏️ Exemple**
>
> **Àrea i volum**
>
> **Paral·lelogram $ABCD$ amb $A(3,1,-2)$, $B(5,6,4)$, $C(0,4,-2)$, $D(-2,-1,-8)$.**
>
> $\overrightarrow{AB}=(2,5,6)$, $\overrightarrow{AD}=(-5,-2,6)$ $$\overrightarrow{AB}\times\overrightarrow{AD} =
\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\2&5&6\\-5&-2&6\end{vmatrix}
= (30+12,\;-30-12,\;-4+25) = (42,-42,21)$$ $$A_{ABCD} = |(42,-42,21)| = \sqrt{42^2+42^2+21^2} = \sqrt{1764+1764+441} = \sqrt{3969} = 63$$

> 1.  Calcula el producte vectorial $\vec{a}\times\vec{b}$ amb $\vec{a}=(1,2,-1)$ i $\vec{b}=(3,0,-4)$. Verifica que el resultat és perpendicular a $\vec{a}$ i a $\vec{b}$.
>
> 2.  Calcula l’àrea del triangle de vèrtexs $A(1,0,0)$, $B(0,2,0)$ i $C(0,0,3)$.
>
> 3.  Calcula el volum del paral·lelepípede construït sobre els vectors $\vec{u}=(1,0,1)$, $\vec{v}=(0,1,1)$ i $\vec{w}=(1,1,0)$.
>
> 4.  Comprova que els vectors $\vec{r}=(1,-3,2)$, $\vec{s}=(2,-1,4)$ i $\vec{t}=(3,1,1)$ no formen base, calculant el producte mixt. Interpreta geomètricament el resultat.
>
> 5.  Calcula l’àrea del paral·lelogram de vèrtexs $A(2,3,-1)$, $B(0,-4,-3)$, $C(-4,1,-3)$, $D(-2,8,-1)$. (Pista: usa $\overrightarrow{AB}$ i $\overrightarrow{AD}$.)

<details><summary>Solució</summary>

1.  $\vec{a}\times\vec{b}=\begin{vmatrix}\vec{i}&\vec{j}&\vec{k}\\1&2&-1\\3&0&-4\end{vmatrix}=(-8+0,\;-3+4,\;0-6)=(-8,1,-6)$. Comp.: $(-8,1,-6)\cdot(1,2,-1)=-8+2+6=0$ ✓

2.  $\overrightarrow{AB}=(-1,2,0)$, $\overrightarrow{AC}=(-1,0,3)$. $\overrightarrow{AB}\times\overrightarrow{AC}=(6,3,2)$. $A_\triangle=\frac{1}{2}\sqrt{36+9+4}=\frac{\sqrt{49}}{2}=\frac{7}{2}$.

3.  $[\vec{u},\vec{v},\vec{w}]=\begin{vmatrix}1&0&1\\0&1&1\\1&1&0\end{vmatrix}=1(0-1)-0+1(0-1)=-2$. Volum $=|-2|=2$.

4.  $[\vec{r},\vec{s},\vec{t}]=\begin{vmatrix}1&-3&2\\2&-1&4\\3&1&1\end{vmatrix}=0$ $\Rightarrow$ vectors coplanaris, no formen base.

5.  $\overrightarrow{AB}=(-2,-7,-2)$, $\overrightarrow{AD}=(-4,5,0)$. $\overrightarrow{AB}\times\overrightarrow{AD}=(10,8,-38)$. $A=\sqrt{100+64+1444}=\sqrt{1608}=2\sqrt{402}$.

</details>

## Resum de fórmules

> **Formulari ràpid — Vectors a l’espai**
>
> 2 **Vector entre dos punts** $$\overrightarrow{AB}=B-A$$ **Mòdul** $$|\vec{v}|=\sqrt{v_1^2+v_2^2+v_3^2}$$ **Vector unitari** $$\hat{u}=\dfrac{\vec{v}}{|\vec{v}|}$$ **Punt mitjà** $$M=A+\tfrac{1}{2}\overrightarrow{AB}$$ **Baricentre** $$G=\left(\frac{a_1+b_1+c_1}{3},\frac{a_2+b_2+c_2}{3},\frac{a_3+b_3+c_3}{3}\right)$$ **Producte escalar** $$\vec{u}\cdot\vec{v}=u_1v_1+u_2v_2+u_3v_3$$ **Angle entre vectors** $$\cos\theta=\dfrac{\vec{u}\cdot\vec{v}}{|\vec{u}||\vec{v}|}$$ **Perpendicularitat** $$\vec{u}\perp\vec{v}\iff\vec{u}\cdot\vec{v}=0$$ **Àrea paral·lelogram** $$A=|\vec{u}\times\vec{v}|$$ **Volum paral·lelepípede** $$V=|[\vec{u},\vec{v},\vec{w}]|$$
