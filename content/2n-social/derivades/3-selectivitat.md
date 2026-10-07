---
title: Derivades i aplicacions: Selectivitat
tematitol: Derivades i aplicacions
curs: 2n
modalitat: social
tema: derivades
bloc: selectivitat
ordre: 3
---
# Derivades i aplicacions: Selectivitat

> Problemes **originals** redactats en l’estil de la selectivitat (no són d’exàmens oficials). Cada solució és desplegable.

## Problema 1 (2,5 punts)
Una empresa ven $x$ milers d'unitats d'un producte al preu $p=60-2x$ euros per unitat. El cost total de producció, en milers d'euros, és $C(x)=10+4x$.

a) Escriu la funció de benefici $B(x)$ (en milers d'euros).
b) Quantes unitats ha de vendre per obtenir el benefici màxim? Quin és aquest benefici i a quin preu ven?
c) Calcula la taxa de variació mitjana del benefici entre $x=10$ i $x=14$ i compara-la amb $B'(10)$.

<details><summary>Solució</summary>

**a)** Ingressos $I(x)=x\,p=60x-2x^2$. Benefici: $B(x)=I-C=-2x^2+56x-10$.

**b)** $B'(x)=-4x+56=0\Rightarrow x=14$. Com que $B''=-4<0$, és un màxim: **14 000 unitats**. El benefici és $B(14)=-392+784-10=\mathbf{382}$ milers d'euros, amb preu $p=60-28=32$ €/unitat.

**c)** $B(10)=350$ i $B(14)=382$, així que $\text{TVM}=\dfrac{382-350}{4}=8$. En canvi $B'(10)=16$: a $x=10$ el benefici creix més de pressa que la mitjana de l'interval, perquè $B$ és còncava i el creixement s'alenteix en apropar-se al màxim.

</details>

## Problema 2 (2,5 punts)
Sigui $q(x)=x^3-6x^2+9x+1$.

a) Estudia'n el creixement i troba'n els extrems relatius.
b) Troba'n el punt d'inflexió i els intervals de concavitat.
c) Calcula'n el màxim i el mínim absoluts a l'interval $[0,4]$.

<details><summary>Solució</summary>

**a)** $q'(x)=3x^2-12x+9=3(x-1)(x-3)$. Creixent a $(-\infty,1)\cup(3,+\infty)$ i decreixent a $(1,3)$. Màxim relatiu a $(1,5)$ i mínim relatiu a $(3,1)$.

**b)** $q''(x)=6x-12=0\Rightarrow x=2$; el punt d'inflexió és $(2,3)$. És còncava a $(-\infty,2)$ i convexa a $(2,+\infty)$.

**c)** $q(0)=1$, $q(1)=5$, $q(3)=1$, $q(4)=5$. El **màxim absolut és $5$** (a $x=1$ i $x=4$) i el **mínim absolut és $1$** (a $x=0$ i $x=3$).

</details>

## Problema 3 (2 punts)
Considera la funció $f(x)=x^2-4x+5$.

a) Troba el punt de la gràfica on la recta tangent és paral·lela a $y=2x+1$ i escriu l'equació de la tangent.
b) Calcula la taxa de variació mitjana de $f$ a $[1,3]$ i explica-la.

<details><summary>Solució</summary>

**a)** $f'(x)=2x-4=2\Rightarrow x=3$ i $f(3)=2$. La tangent és $y-2=2(x-3)\iff y=2x-4$.

**b)** $\text{TVM}=\dfrac{f(3)-f(1)}{3-1}=\dfrac{2-2}{2}=0$. De mitjana la funció no varia entre $1$ i $3$ (baixa fins al mínim $f(2)=1$ i torna a pujar).

</details>
