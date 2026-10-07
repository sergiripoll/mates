---
title: Estadística: intervals de confiança: Selectivitat
tematitol: Estadística: intervals de confiança
curs: 2n
modalitat: social
tema: estadistica
bloc: selectivitat
ordre: 3
---
# Estadística: intervals de confiança: Selectivitat

> Problemes **originals** redactats en l’estil de la selectivitat (no són d’exàmens oficials). Cada solució és desplegable.

## Problema 1 (2,5 punts)
Una variable aleatòria té desviació típica $\sigma=9$. En una mostra de $36$ individus s'obté una mitjana de $70$.

a) Troba l'interval de confiança del $95\,\%$ per a la mitjana poblacional.
b) Troba'l amb un nivell de confiança del $99\,\%$ i compara'n l'amplada.
c) Quina mida mínima ha de tenir la mostra perquè l'error màxim, al $95\,\%$, no superi $2$?

<details><summary>Solució</summary>

**a)** $E=1{,}96\cdot\dfrac{9}{\sqrt{36}}=2{,}94$, i l'interval és $\mathbf{(67{,}06;\;72{,}94)}$.

**b)** Amb $z=2{,}576$: $E=2{,}576\cdot1{,}5=3{,}864$ i l'interval és $\mathbf{(66{,}14;\;73{,}86)}$. És **més ample**: més confiança es paga amb menys precisió.

**c)** $1{,}96\cdot\dfrac{9}{\sqrt n}\le2\Rightarrow n\ge\left(\dfrac{1{,}96\cdot9}{2}\right)^2\approx77{,}8$, així que $n=\mathbf{78}$.

</details>

## Problema 2 (2,5 punts)
En un sondeig a $400$ persones, $220$ s'han mostrat a favor d'una mesura.

a) Troba un interval de confiança del $95\,\%$ per a la proporció de persones a favor.
b) Es pot afirmar, amb aquest nivell de confiança, que la majoria de la població hi és favorable? Justifica-ho.

<details><summary>Solució</summary>

**a)** $\hat p=\dfrac{220}{400}=0{,}55$ i $E=1{,}96\sqrt{\dfrac{0{,}55\cdot0{,}45}{400}}\approx0{,}0488$. L'interval és $\mathbf{(0{,}501;\;0{,}599)}$.

**b)** Tot l'interval és per sobre de $0{,}5$ (el límit inferior és $0{,}501$), de manera que, al $95\,\%$, sí que es pot afirmar que la majoria hi és a favor, però **amb molt poc marge**: una mostra una mica més petita o un nivell de confiança més alt ho impediria.

</details>

## Problema 3 (2 punts)
L'alçada (en cm) d'una població segueix una distribució $N(170;\,8)$.

a) Calcula $P(X<158)$ i $P(166<X<182)$.
b) Es pren una mostra de $64$ persones. Quina és la distribució de la mitjana mostral $\overline X$? Calcula $P(\overline X>171{,}5)$.

<details><summary>Solució</summary>

**a)** $P(X<158)=P(Z<-1{,}5)=1-0{,}9332=\mathbf{0{,}0668}$. $P(166<X<182)=P(-0{,}5<Z<1{,}5)=0{,}9332-0{,}3085=\mathbf{0{,}6247}$.

**b)** $\overline X\sim N\!\left(170;\,\dfrac{8}{\sqrt{64}}\right)=N(170;\,1)$. Llavors $P(\overline X>171{,}5)=P(Z>1{,}5)=\mathbf{0{,}0668}$.

</details>
