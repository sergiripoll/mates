---
title: Distribució binomial i normal. Intervals de confiança: Selectivitat
tematitol: Distribució binomial i normal. Intervals de confiança
curs: 2n
modalitat: cientific
tema: distribucions
bloc: selectivitat
ordre: 3
---
# Distribució binomial i normal. Intervals de confiança: Selectivitat

> Problemes **originals** redactats en l’estil de la selectivitat (no són d’exàmens oficials). Cada solució és desplegable.

## Problema 1 (2,5 punts)
Un tirador encerta la diana amb probabilitat $0{,}7$ en cada tir, i els tirs són independents. Fa $10$ tirs. Sigui $X$ el nombre d'encerts.

a) Quina és la distribució de $X$?
b) Calcula $P(X=7)$.
c) Calcula la probabilitat d'encertar-ne almenys $9$.
d) Troba l'esperança i la desviació típica de $X$.

<details><summary>Solució</summary>

**a)** $X\sim B(10;\,0{,}7)$.

**b)** $P(X=7)=\binom{10}{7}0{,}7^7\,0{,}3^3=120\cdot0{,}0823543\cdot0{,}027\approx0{,}267$.

**c)** $P(X\ge9)=P(9)+P(10)=10\cdot0{,}7^9\cdot0{,}3+0{,}7^{10}\approx0{,}1211+0{,}0282=0{,}149$.

**d)** $\mu=np=7$ i $\sigma=\sqrt{npq}=\sqrt{2{,}1}\approx1{,}45$.

</details>

## Problema 2 (2 punts)
El pes (en grams) d'un paquet de cafè segueix una distribució $N(250;\,10)$. Calcula:

a) $P(X>265)$.
b) $P(240<X<260)$.
c) El pes $c$ tal que el $95\,\%$ dels paquets pesen menys que $c$.

<details><summary>Solució</summary>

Tipifiquem amb $Z=\dfrac{X-250}{10}$.

**a)** $P(X>265)=P(Z>1{,}5)=1-0{,}9332=\mathbf{0{,}0668}$.

**b)** $P(-1<Z<1)=2\cdot0{,}8413-1=\mathbf{0{,}6826}$.

**c)** $P(Z<z)=0{,}95\Rightarrow z=1{,}645$, i per tant $c=250+1{,}645\cdot10=\mathbf{266{,}45}$ g.

</details>

## Problema 3 (2,5 punts)
La durada d'un cert component segueix una llei normal de desviació típica $\sigma=8$ hores. En una mostra de $100$ components, la durada mitjana ha estat de $52$ hores.

a) Troba un interval de confiança del $95\,\%$ per a la durada mitjana.
b) Quina mida mínima ha de tenir la mostra perquè l'error màxim sigui com a molt d'$1$ hora, amb el mateix nivell de confiança?
c) En una altra mostra de $500$ components, $300$ han superat les $50$ hores. Troba un interval de confiança del $95\,\%$ per a la proporció.

<details><summary>Solució</summary>

**a)** $E=1{,}96\cdot\dfrac{8}{\sqrt{100}}=1{,}568$, i l'interval és $(52-1{,}568;\;52+1{,}568)=\mathbf{(50{,}43;\;53{,}57)}$.

**b)** $1{,}96\cdot\dfrac{8}{\sqrt n}\le1\Rightarrow n\ge(1{,}96\cdot8)^2\approx245{,}9$, per tant $n=\mathbf{246}$.

**c)** $\hat p=0{,}6$ i $E=1{,}96\sqrt{\dfrac{0{,}6\cdot0{,}4}{500}}\approx0{,}0429$. L'interval és $\mathbf{(0{,}557;\;0{,}643)}$.

</details>
