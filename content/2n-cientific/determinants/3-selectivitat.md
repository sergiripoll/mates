---
title: Determinants, matrius i sistemes: Selectivitat
tematitol: Determinants, matrius i sistemes
curs: 2n
modalitat: tots
tema: determinants
bloc: selectivitat
ordre: 3
---
# Determinants, matrius i sistemes: Selectivitat

> Problemes **originals** redactats en l’estil de la selectivitat (no són d’exàmens oficials). Cada solució és desplegable.

## Problema 1 (3 punts)
Considera el sistema d'equacions, amb paràmetre $a$:
$$\begin{cases}x+y+az=1\\ x+ay+z=a\\ ax+y+z=a^2\end{cases}$$

a) Discuteix-lo segons els valors d'$a$.
b) Resol-lo per a $a=0$.
c) Resol-lo per a $a=1$.

<details><summary>Solució</summary>

**a)** El determinant de la matriu de coeficients és $|A|=-(a-1)^2(a+2)$.

- Si $a\neq1$ i $a\neq-2$: $|A|\ne0$, rang $A=3=$ rang $A^*$ $\Rightarrow$ **sistema compatible determinat**.
- Si $a=-2$: rang $A=2$ (la suma de les tres files és $0$) però rang $A^*=3$, perquè la suma dels termes independents és $1-2+4=3\ne0$ $\Rightarrow$ **incompatible**.
- Si $a=1$: les tres equacions són $x+y+z=1$, i per tant rang $A=$ rang $A^*=1<3$ $\Rightarrow$ **compatible indeterminat** (2 paràmetres).

**b)** Per a $a=0$: $x+y=1,\; x+z=0,\; y+z=0$. Resolent: $x=\tfrac12,\;y=\tfrac12,\;z=-\tfrac12$.

**c)** Per a $a=1$: $x+y+z=1$. Solució: $(x,y,z)=(1-\lambda-\mu,\;\lambda,\;\mu)$ amb $\lambda,\mu\in\mathbb R$.

</details>

## Problema 2 (2,5 punts)
Siguin $A=\begin{pmatrix}1&2\\1&3\end{pmatrix}$ i $B=\begin{pmatrix}1&0\\2&1\end{pmatrix}$.

a) Comprova que $A^2-4A+I=0$ i dedueix-ne $A^{-1}$.
b) Resol l'equació matricial $AX=B$.
c) Calcula $A^3$ sense multiplicar tres vegades.

<details><summary>Solució</summary>

**a)** $A^2=\begin{pmatrix}3&8\\4&11\end{pmatrix}$, de manera que $A^2-4A+I=\begin{pmatrix}3-4+1&8-8\\4-4&11-12+1\end{pmatrix}=0$. Llavors $A(4I-A)=I$, i per tant $A^{-1}=4I-A=\begin{pmatrix}3&-2\\-1&1\end{pmatrix}$.

**b)** $X=A^{-1}B=\begin{pmatrix}3&-2\\-1&1\end{pmatrix}\begin{pmatrix}1&0\\2&1\end{pmatrix}=\begin{pmatrix}-1&-2\\1&1\end{pmatrix}$.

**c)** De $A^2=4A-I$ surt $A^3=4A^2-A=4(4A-I)-A=15A-4I=\begin{pmatrix}11&30\\15&41\end{pmatrix}$.

</details>

## Problema 3 (2 punts)
a) Resol l'equació $\begin{vmatrix}x&1&1\\1&x&1\\1&1&x\end{vmatrix}=0$.
b) Per a cada solució, calcula el rang de la matriu.

<details><summary>Solució</summary>

**a)** Desenvolupant, el determinant és $x^3-3x+2=(x-1)^2(x+2)$. Les solucions són $x=1$ (doble) i $x=-2$.

**b)** Si $x=1$, totes les files són $(1,1,1)$: **rang $1$**. Si $x=-2$, el rang és $2$: el determinant és $0$, però el menor $\begin{vmatrix}-2&1\\1&-2\end{vmatrix}=3\neq0$. Per a la resta de valors el rang és $3$.

</details>
