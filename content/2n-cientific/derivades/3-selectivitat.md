---
title: Derivades i optimització: Selectivitat
tematitol: Derivades i optimització
curs: 2n
modalitat: cientific
tema: derivades
bloc: selectivitat
ordre: 3
---
# Derivades i optimització: Selectivitat

> Problemes **originals** redactats en l’estil de la selectivitat (no són d’exàmens oficials). Cada solució és desplegable.

## Problema 1 (2,5 punts)
Una empresa vol fabricar un dipòsit cilíndric tancat de volum $32\pi\ \text{dm}^3$. El material de les dues bases costa $2\ \text{€/dm}^2$ i el de la superfície lateral, $1\ \text{€/dm}^2$. Troba les dimensions del dipòsit que fan mínim el cost i calcula'n el cost mínim.

<details><summary>Solució</summary>

Amb radi $r$ i altura $h$: $\pi r^2h=32\pi\Rightarrow h=\dfrac{32}{r^2}$.

Cost: $C(r)=2\cdot2\pi r^2+1\cdot2\pi r h=4\pi r^2+\dfrac{64\pi}{r}$.

$C'(r)=8\pi r-\dfrac{64\pi}{r^2}=0\Rightarrow r^3=8\Rightarrow r=2$. Llavors $h=\dfrac{32}{4}=8$.

És un mínim perquè $C''(r)=8\pi+\dfrac{128\pi}{r^3}>0$. El cost mínim és $C(2)=16\pi+32\pi=48\pi\approx150{,}80$ €, amb $r=2$ dm i $h=8$ dm.

</details>

## Problema 2 (2,5 punts)
Considera la funció $g(x)=x\,e^{-x^2/2}$.

a) Calcula'n el domini i les asímptotes.
b) Estudia'n el creixement i els extrems relatius.
c) Troba'n els punts d'inflexió.
d) Indica'n el recorregut.

<details><summary>Solució</summary>

**a)** $\text{Dom}\,g=\mathbb R$, sense asímptotes verticals. $\lim_{x\to\pm\infty}g(x)=0$, així que $y=0$ és asímptota horitzontal.

**b)** $g'(x)=(1-x^2)e^{-x^2/2}$. És positiva a $(-1,1)$: **creixent**; negativa a $(-\infty,-1)\cup(1,+\infty)$: **decreixent**. Mínim relatiu a $\left(-1,-e^{-1/2}\right)$ i màxim relatiu a $\left(1,e^{-1/2}\right)$.

**c)** $g''(x)=x(x^2-3)e^{-x^2/2}$, que s'anul·la a $x=-\sqrt3,\,0,\,\sqrt3$ i hi canvia de signe: tres punts d'inflexió.

**d)** Com que $g$ és contínua, tendeix a $0$ als extrems i té màxim $e^{-1/2}$ i mínim $-e^{-1/2}$, el recorregut és $\left[-e^{-1/2},\,e^{-1/2}\right]\approx[-0{,}61;\,0{,}61]$.

</details>

## Problema 3 (2 punts)
a) Demostra que l'equació $x^3+3x-5=0$ té una única solució real i que és a l'interval $(1,2)$.
b) Escriu l'equació de la recta tangent a $f(x)=x^3+3x-5$ en $x=1$.
c) Utilitza aquesta tangent per aproximar l'arrel (un pas del mètode de Newton).

<details><summary>Solució</summary>

**a)** $f(1)=-1<0$ i $f(2)=9>0$, i $f$ és contínua: pel teorema de Bolzano hi ha una arrel a $(1,2)$. A més, $f'(x)=3x^2+3>0$ per a tot $x$, de manera que $f$ és estrictament creixent i no pot tenir cap altra arrel.

**b)** $f(1)=-1$, $f'(1)=6$: $\;y+1=6(x-1)\iff y=6x-7$.

**c)** La tangent talla l'eix $OX$ a $6x-7=0\Rightarrow x_1=\dfrac76\approx1{,}167$.

</details>
