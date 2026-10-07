---
title: Funcions, límits i continuïtat: Selectivitat
tematitol: Funcions, límits i continuïtat
curs: 2n
modalitat: social
tema: limits
bloc: selectivitat
ordre: 3
---
# Funcions, límits i continuïtat: Selectivitat

> Problemes **originals** redactats en l’estil de la selectivitat (no són d’exàmens oficials). Cada solució és desplegable.

## Problema 1 (2,5 punts)
Considera la funció
$$f(x)=\begin{cases}\dfrac{x^2-1}{x-1}, & x<1\\[2mm] ax+b, & 1\le x<3\\[2mm] 5, & x\ge3\end{cases}$$

a) Determina $a$ i $b$ perquè $f$ sigui contínua a tot $\mathbb R$.
b) Per als valors trobats, calcula $f(2)$.

<details><summary>Solució</summary>

**a)** Per a $x<1$, $\frac{x^2-1}{x-1}=x+1$, de manera que $\lim_{x\to1^-}f=2$.

- Continuïtat en $x=1$: $a+b=2$.
- Continuïtat en $x=3$: $3a+b=5$.

Restant: $2a=3\Rightarrow a=\frac32$, i llavors $b=\frac12$.

**b)** $f(2)=2a+b=3+\frac12=\frac72=3{,}5$.

</details>

## Problema 2 (2 punts)
Calcula els límits següents:

a) $\displaystyle\lim_{x\to2}\frac{x^2-4}{x^2-x-2}$  b) $\displaystyle\lim_{x\to+\infty}\frac{3x^2-x}{x^2+5}$  c) $\displaystyle\lim_{x\to+\infty}\left(\frac{x^2+1}{x-1}-x\right)$

<details><summary>Solució</summary>

**a)** Indeterminació $\frac00$. Factoritzem: $\dfrac{(x-2)(x+2)}{(x-2)(x+1)}=\dfrac{x+2}{x+1}\to\dfrac43$.

**b)** Graus iguals: el límit és el quocient dels coeficients dominants, $\mathbf{3}$.

**c)** Indeterminació $\infty-\infty$. Operant, $\dfrac{x^2+1-x(x-1)}{x-1}=\dfrac{x+1}{x-1}\to\mathbf{1}$.

</details>

## Problema 3 (2,5 punts)
Sigui $f(x)=\dfrac{2x^2}{x^2-4}$.

a) Troba'n el domini.
b) Calcula'n les asímptotes verticals i l'horitzontal.
c) Estudia la posició de la gràfica respecte de l'asímptota horitzontal.

<details><summary>Solució</summary>

**a)** $x^2-4=0\iff x=\pm2$: $\text{Dom}f=\mathbb R\setminus\{-2,2\}$.

**b)** *Verticals:* $x=2$ i $x=-2$ (per exemple, $\lim_{x\to2^+}f=+\infty$ i $\lim_{x\to2^-}f=-\infty$). *Horitzontal:* $\lim_{x\to\pm\infty}f=2$, així que $y=2$.

**c)** $f(x)-2=\dfrac{8}{x^2-4}$. Si $|x|>2$ és positiu: la gràfica és per sobre de $y=2$; si $|x|<2$ és negatiu: per sota.

</details>
