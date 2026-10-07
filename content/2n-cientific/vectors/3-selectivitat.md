---
title: Vectors i geometria a l’espai: Selectivitat
tematitol: Vectors i geometria a l’espai
curs: 2n
modalitat: cientific
tema: vectors
bloc: selectivitat
ordre: 3
---
# Vectors i geometria a l’espai: Selectivitat

> Problemes **originals** redactats en l’estil de la selectivitat (no són d’exàmens oficials). Cada solució és desplegable.

## Problema 1 (3 punts)
Considera els punts $A(1,2,0)$, $B(3,1,1)$, $C(0,4,2)$ i $E(1,1,1)$.

a) Calcula l'àrea del triangle $ABC$.
b) Troba el punt $D$ perquè $ABCD$ sigui un paral·lelogram.
c) Escriu l'equació del pla que passa per $A$, $B$ i $C$.
d) Calcula el volum del tetràedre de vèrtexs $A$, $B$, $C$ i $E$.

<details><summary>Solució</summary>

Tenim $\vec{AB}=(2,-1,1)$, $\vec{AC}=(-1,2,2)$ i $\vec{AE}=(0,-1,1)$.

**a)** $\vec{AB}\times\vec{AC}=(-4,-5,3)$, de mòdul $\sqrt{50}=5\sqrt2$. L'àrea és $\dfrac{5\sqrt2}{2}\approx3{,}54$ u².

**b)** $D=A+C-B=(1+0-3,\;2+4-1,\;0+2-1)=(-2,5,1)$.

**c)** El vector normal és $(-4,-5,3)$, o bé $(4,5,-3)$: $\;4(x-1)+5(y-2)-3z=0\iff 4x+5y-3z-14=0$. Es comprova que $B$ i $C$ també hi pertanyen.

**d)** $[\vec{AB},\vec{AC},\vec{AE}]=\begin{vmatrix}2&-1&1\\-1&2&2\\0&-1&1\end{vmatrix}=8$, i el volum és $\dfrac{|8|}{6}=\dfrac43$ u³.

</details>

## Problema 2 (2,5 punts)
Siguin el pla $\pi:\;2x-y+2z=5$ i el punt $P(1,2,3)$.

a) Calcula la distància de $P$ al pla.
b) Troba la projecció ortogonal $M$ de $P$ sobre el pla.
c) Troba el punt simètric $P'$ de $P$ respecte del pla.

<details><summary>Solució</summary>

**a)** $d=\dfrac{|2\cdot1-2+2\cdot3-5|}{\sqrt{4+1+4}}=\dfrac13$.

**b)** La recta perpendicular al pla per $P$ és $(1+2t,\;2-t,\;3+2t)$. Substituint al pla: $2(1+2t)-(2-t)+2(3+2t)=5\Rightarrow 9t=-1\Rightarrow t=-\frac19$. Així $M=\left(\frac79,\frac{19}9,\frac{25}9\right)$.

**c)** $M$ és el punt mitjà de $PP'$, i per tant $P'=2M-P=\left(\frac59,\frac{20}9,\frac{23}9\right)$.

</details>

## Problema 3 (2,5 punts)
Siguin els vectors $\vec u=(1,1,m)$, $\vec v=(1,m,1)$ i $\vec w=(m,1,1)$.

a) Per a quins valors de $m$ són linealment dependents?
b) Per a $m=-2$, expressa $\vec w$ com a combinació lineal de $\vec u$ i $\vec v$.
c) Per a $m=0$, calcula el volum del paral·lelepípede que determinen.

<details><summary>Solució</summary>

**a)** Són dependents si el seu determinant és zero: $\begin{vmatrix}1&1&m\\1&m&1\\m&1&1\end{vmatrix}=-(m-1)^2(m+2)=0\iff m=1\ \text{o}\ m=-2$.

**b)** Per a $m=-2$: $\vec u+\vec v+\vec w=(0,0,0)$, de manera que $\vec w=-\vec u-\vec v$.

**c)** Per a $m=0$ el determinant val $-2$, i el volum és $|-2|=2$ u³.

</details>
