---
title: Límits i continuïtat: Selectivitat
tematitol: Límits i continuïtat
curs: 2n
modalitat: cientific
tema: limits
bloc: selectivitat
ordre: 3
---
# Límits i continuïtat: Selectivitat

## Dossier de límits (problemes tipus examen)

#### Bloc 5: Problemes Globals i Tipus Examen / PAU (Nivell Molt Alt – 10%)

1.  **\[Model PAU\]** Determina els valors dels paràmetres $a, b \in \mathbb{R}$ perquè la funció $f(x)$ sigui contínua en tot el seu domini: $$f(x) = \begin{cases} a x + 2 & \text{si } x < 1 \\ x^2 + b & \text{si } 1 \le x < 3 \\ \frac{2x + 8}{x - 1} & \text{si } x \ge 3 \end{cases}$$

2.  **\[Model PAU\]** Donada la funció racional $f(x) = \frac{ax^2 + bx - 3}{x + 2}$:

    1.  Troba els valors de $a$ i $b$ sabent que la recta $y = 3x - 1$ és una assímptota oblíqua de $f(x)$.

    2.  Amb els valors obtinguts, estudia la continuïtat de la funció i determina les seves assímptotes verticals.

—

## Problemes originals d’estil selectivitat

> Problemes **originals** redactats en l’estil de la selectivitat (no són d’exàmens oficials). Cada solució és desplegable.

### Problema 1 (2 punts)
Calcula els límits següents:

a) $\displaystyle\lim_{x\to 0}\frac{e^{2x}-1-2x}{x^2}$  b) $\displaystyle\lim_{x\to +\infty}\left(\sqrt{x^2+3x}-x\right)$  c) $\displaystyle\lim_{x\to 0}(\cos x)^{1/x^2}$

<details><summary>Solució</summary>

**a)** És una indeterminació $\frac{0}{0}$. Apliquem L'Hôpital dues vegades: $\displaystyle\lim_{x\to0}\frac{2e^{2x}-2}{2x}$ continua sent $\frac00$ i dona $\displaystyle\lim_{x\to0}\frac{4e^{2x}}{2}=\mathbf{2}$.

**b)** Indeterminació $\infty-\infty$. Multipliquem pel conjugat: $\displaystyle\frac{(x^2+3x)-x^2}{\sqrt{x^2+3x}+x}=\frac{3x}{\sqrt{x^2+3x}+x}$. Dividint per $x$ queda $\displaystyle\frac{3}{\sqrt{1+3/x}+1}\to\frac32$.

**c)** Indeterminació $1^\infty$. El límit val $e^{L}$ amb $L=\displaystyle\lim_{x\to0}\frac{\cos x-1}{x^2}=\lim_{x\to0}\frac{-\sin x}{2x}=-\frac12$. Per tant el límit és $\mathbf{e^{-1/2}}$.

</details>

### Problema 2 (2,5 punts)
Considerem la funció
$$f(x)=\begin{cases}\dfrac{\sin(ax)}{x}, & x<0\\[2mm] b, & x=0\\[2mm] \dfrac{\sqrt{1+x}-1}{x}, & x>0\end{cases}$$

a) Determina $a$ i $b$ perquè $f$ sigui contínua en $x=0$.
b) Per a aquests valors, calcula $\displaystyle\lim_{x\to+\infty}f(x)$ i $\displaystyle\lim_{x\to-\infty}f(x)$ i interpreta'ls geomètricament.

<details><summary>Solució</summary>

**a)** Límit per l'esquerra: $\displaystyle\lim_{x\to0^-}\frac{\sin(ax)}{x}=a$. Límit per la dreta, amb el conjugat: $\displaystyle\frac{x}{x(\sqrt{1+x}+1)}=\frac{1}{\sqrt{1+x}+1}\to\frac12$. Perquè sigui contínua cal $a=\frac12=b$.

**b)** Per a $x\to+\infty$, $\frac{\sqrt{1+x}-1}{x}\sim\frac{\sqrt x}{x}\to 0$. Per a $x\to-\infty$, $\left|\frac{\sin(x/2)}{x}\right|\le\frac1{|x|}\to0$ (criteri del sandvitx). En els dos casos el límit és $0$, de manera que $y=0$ és **asímptota horitzontal** a $+\infty$ i a $-\infty$.

</details>

### Problema 3 (2,5 punts)
Sigui $f(x)=\dfrac{x^3}{x^2-1}$.

a) Troba'n el domini i els punts de tall amb els eixos.
b) Calcula'n totes les asímptotes.
c) Estudia la posició relativa de la gràfica respecte de l'asímptota obliqua.

<details><summary>Solució</summary>

**a)** $\text{Dom}f=\mathbb R\setminus\{-1,1\}$. L'únic punt de tall és $(0,0)$.

**b)** *Verticals:* $x=1$ i $x=-1$ (per exemple, $\lim_{x\to1^+}f=+\infty$ i $\lim_{x\to1^-}f=-\infty$). *Horitzontals:* no n'hi ha, perquè $\lim_{x\to\pm\infty}f=\pm\infty$. *Obliqua* $y=mx+n$: $m=\lim\frac{f(x)}{x}=1$ i $n=\lim\big(f(x)-x\big)=\lim\frac{x}{x^2-1}=0$, per tant $y=x$.

**c)** $f(x)-x=\dfrac{x}{x^2-1}$. Si $x>1$ és positiu: la gràfica és **per sobre** de la recta. Si $x<-1$ és negatiu: la gràfica és **per sota**.

</details>
