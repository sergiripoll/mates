---
title: Límits amb arrels: exercicis resolts
curs: 2n
modalitat: cientific
tema: limits
tipus: exercicis
---
# Límits amb arrels: exercicis resolts

## Introducció

Aquest document conté la resolució pas a pas dels apartats **d, e, g, g) modificat 1, g) modificat 2, h, i, j** de l’exercici 19 sobre límits en l’infinit amb arrels quadrades.

## Apartat d

Calcula el límit: $$\lim_{x \to +\infty} \frac{2x + 1}{\sqrt{x^2 + 2}}$$

### Pas 1: Identificar la indeterminació

En avaluar directament quan $x \to +\infty$: $$\frac{2(+\infty) + 1}{\sqrt{(+\infty)^2 + 2}} = \left[\frac{+\infty}{+\infty}\right]$$

### Pas 2: Dividir pel terme de major grau

Com que $x > 0$, tenim que $x = \sqrt{x^2}$. Dividim numerador i denominador per $x$: $$\lim_{x \to +\infty} \frac{\frac{2x + 1}{x}}{\frac{\sqrt{x^2 + 2}}{x}} = \lim_{x \to +\infty} \frac{2 + \frac{1}{x}}{\sqrt{\frac{x^2 + 2}{x^2}}} = \lim_{x \to +\infty} \frac{2 + \frac{1}{x}}{\sqrt{1 + \frac{2}{x^2}}}$$

### Pas 3: Avaluar el límit

Com que $\lim_{x \to +\infty} \frac{1}{x} = 0$ i $\lim_{x \to +\infty} \frac{2}{x^2} = 0$: $$\frac{2 + 0}{\sqrt{1 + 0}} = \frac{2}{1} = \mathbf{2}$$

—

## Apartat e

Calcula el límit: $$\lim_{x \to +\infty} \frac{5x + 4}{\sqrt{x^3 + 3}}$$

### Pas 1: Identificar la indeterminació

Avaluem el límit: $$\left[\frac{+\infty}{+\infty}\right]$$

### Pas 2: Comparació de graus

- **Grau del numerador:** $1$ (de $5x$).

- **Grau del denominador:** $\frac{3}{2} = 1{,}5$ (ja que $\sqrt{x^3} = x^{3/2}$).

Com que el grau del denominador és **estrictament major** que el del numerador, la fracció tendeix a zero.

### Pas 3: Demostració algebraicament

Dividim numerador i denominador per $x$: $$\lim_{x \to +\infty} \frac{\frac{5x + 4}{x}}{\frac{\sqrt{x^3 + 3}}{x}} = \lim_{x \to +\infty} \frac{5 + \frac{4}{x}}{\sqrt{\frac{x^3 + 3}{x^2}}} = \lim_{x \to +\infty} \frac{5 + \frac{4}{x}}{\sqrt{x + \frac{3}{x^2}}}$$ En avaluar quan $x \to +\infty$: $$\frac{5 + 0}{\sqrt{+\infty + 0}} = \frac{5}{+\infty} = \mathbf{0}$$

—

## Apartat g

Calcula el límit: $$\lim_{x \to +\infty} \left(\sqrt{2x^2 - 3x} - \sqrt{x^2 + 1}\right)$$

### Pas 1: Identificar la indeterminació

Avaluem el límit: $$\sqrt{+\infty} - \sqrt{+\infty} = [+\infty - \infty]$$

### Pas 2: Multiplicar i dividir pel conjugat

Multipliquem i dividim per l’expressió sumant les dues arrels: $$\lim_{x \to +\infty} \frac{\left(\sqrt{2x^2 - 3x} - \sqrt{x^2 + 1}\right)\left(\sqrt{2x^2 - 3x} + \sqrt{x^2 + 1}\right)}{\sqrt{2x^2 - 3x} + \sqrt{x^2 + 1}}$$

### Pas 3: Simplificar el numerador

Apliquem $(a-b)(a+b) = a^2 - b^2$: $$\lim_{x \to +\infty} \frac{(2x^2 - 3x) - (x^2 + 1)}{\sqrt{2x^2 - 3x} + \sqrt{x^2 + 1}} = \lim_{x \to +\infty} \frac{x^2 - 3x - 1}{\sqrt{2x^2 - 3x} + \sqrt{x^2 + 1}}$$

### Pas 4: Avaluar el nou límit

Ara tenim una indeterminació $\left[\frac{+\infty}{+\infty}\right]$:

- **Grau del numerador:** $2$.

- **Grau del denominador:** $1$ (les arrels contenen $x^2$, així que el grau efectiu és $1$).

Com que el grau del numerador és major que el del denominador: $$\mathbf{+\infty}$$

—

## Apartat g) Modificat 1 (Graus diferents: Factor comú)

Calcula el límit: $$\lim_{x \to +\infty} \left(\sqrt{2x^3 - 3x} - \sqrt{x^2 + 1}\right)$$

> **Nota pedagògica**
>
> Quan tenim una indeterminació $[\infty - \infty]$ on els dos termes tenen \*\*diferent grau\*\* ($\text{grau}(\sqrt{2x^3-3x}) = 1{,}5$ i $\text{grau}(\sqrt{x^2+1}) = 1$), \*\*no cal utilitzar el conjugat\*\*. El mètode més elegant i ràpid és extreure com a factor comú el terme dominant (de major grau).

### Pas 1: Extreure factor comú el terme dominant

Treiem factor comú la primera arrel $\sqrt{2x^3 - 3x}$: $$\lim_{x \to +\infty} \sqrt{2x^3 - 3x} \cdot \left(1 - \frac{\sqrt{x^2 + 1}}{\sqrt{2x^3 - 3x}}\right)$$

### Pas 2: Juntar les arrels de la fracció

Unifiquem la fracció dins d’una sola arrel quadrada: $$\lim_{x \to +\infty} \sqrt{2x^3 - 3x} \cdot \left(1 - \sqrt{\frac{x^2 + 1}{2x^3 - 3x}}\right)$$

### Pas 3: Analitzar el límit de la fracció interior

Dins de la segona arrel, el numerador té grau $2$ i el denominador té grau $3$: $$\lim_{x \to +\infty} \frac{x^2 + 1}{2x^3 - 3x} = 0 \implies \sqrt{0} = 0$$

### Pas 4: Avaluar el límit global

Substituïm el resultat: $$(+\infty) \cdot (1 - 0) = (+\infty) \cdot 1 = \mathbf{+\infty}$$

—

## Apartat g) Modificat 2 (Totes dues arrels amb $x^3$: Ús del conjugat i simplificació de $\sqrt{x^3}$)

Calcula el límit: $$\lim_{x \to +\infty} \left(\sqrt{2x^3 - 3x} - \sqrt{x^3 + 1}\right)$$

> **Nota pedagògica: Com simplificar una arrel de $x^3$ desprès del conjugat**
>
> Quan totes dues arrels tenen el mateix grau màxim ($x^3$), apliquem el \*\*conjugat\*\*. Després de simplificar el numerador, ens queda una arrel quadrada de $x^3$ al denominador. Per simplificar-la, dividim numerador i denominador per $\mathbf{\sqrt{x^3}} = x^{3/2}$. Recorda que en entrar $\sqrt{x^3}$ dins d’una arrel quadrada, entra com a \*\*$x^3$\*\*!

### Pas 1: Aplicar el conjugat

Multipliquem i dividim pel conjugat: $$\lim_{x \to +\infty} \frac{\left(\sqrt{2x^3 - 3x} - \sqrt{x^3 + 1}\right)\left(\sqrt{2x^3 - 3x} + \sqrt{x^3 + 1}\right)}{\sqrt{2x^3 - 3x} + \sqrt{x^3 + 1}}$$

### Pas 2: Simplificar el numerador

Apliquem $(a-b)(a+b) = a^2 - b^2$: $$\lim_{x \to +\infty} \frac{(2x^3 - 3x) - (x^3 + 1)}{\sqrt{2x^3 - 3x} + \sqrt{x^3 + 1}} = \lim_{x \to +\infty} \frac{x^3 - 3x - 1}{\sqrt{2x^3 - 3x} + \sqrt{x^3 + 1}}$$

### Pas 3: Com eliminar / simplificar la $\sqrt{x^3}$ del denominador

Avaluem els graus:

- \*\*Grau del numerador:\*\* $3$ (de $x^3$).

- \*\*Grau del denominador:\*\* $\frac{3}{2} = 1{,}5$ (de $\sqrt{x^3}$).

Per simplificar el denominador, dividim el numerador i el denominador pel terme dominant del denominador, que és $\mathbf{\sqrt{x^3}}$:

$$\lim_{x \to +\infty} \frac{\frac{x^3 - 3x - 1}{\sqrt{x^3}}}{\frac{\sqrt{2x^3 - 3x} + \sqrt{x^3 + 1}}{\sqrt{x^3}}}$$

### Pas 4: Operar amb la $\sqrt{x^3}$

1.  \*\*Al denominador:\*\* Com que $\frac{\sqrt{A}}{\sqrt{B}} = \sqrt{\frac{A}{B}}$, la $\sqrt{x^3}$ entra directament com a $x^3$ dins de cada arrel: $$\frac{\sqrt{2x^3 - 3x}}{\sqrt{x^3}} + \frac{\sqrt{x^3 + 1}}{\sqrt{x^3}} = \sqrt{\frac{2x^3 - 3x}{x^3}} + \sqrt{\frac{x^3 + 1}{x^3}} = \sqrt{2 - \frac{3}{x^2}} + \sqrt{1 + \frac{1}{x^3}}$$ Quan $x \to +\infty$, això tendeix a $\sqrt{2 - 0} + \sqrt{1 + 0} = \mathbf{\sqrt{2} + 1}$.

2.  \*\*Al numerador:\*\* Expressem $\sqrt{x^3} = x^{3/2}$: $$\frac{x^3 - 3x - 1}{x^{3/2}} = \frac{x^3}{x^{3/2}} - \frac{3x}{x^{3/2}} - \frac{1}{x^{3/2}} = x^{3/2} - \frac{3}{\sqrt{x}} - \frac{1}{x\sqrt{x}}$$ Quan $x \to +\infty$, el primer terme $x^{3/2} \to +\infty$ i els altres dos tendeixen a $0$.

### Pas 5: Avaluar el límit final

Substituïm els valors obtinguts: $$\frac{+\infty - 0 - 0}{\sqrt{2} + 1} = \frac{+\infty}{\sqrt{2} + 1} = \mathbf{+\infty}$$

> **Variant amb coeficients iguals ($x^3$ es cancel·la al numerador)**
>
> Si tinguéssim $\lim_{x \to +\infty} \left(\sqrt{x^3 + 4x^2} - \sqrt{x^3 - 1}\right)$, al fer el conjugat el $x^3$ del numerador es cancel·laria: $$\frac{(x^3 + 4x^2) - (x^3 - 1)}{\sqrt{x^3 + 4x^2} + \sqrt{x^3 - 1}} = \frac{4x^2 + 1}{\sqrt{x^3 + 4x^2} + \sqrt{x^3 - 1}}$$ En dividint numerador i denominador per $\sqrt{x^3}$: $$\frac{\frac{4x^2 + 1}{x^{3/2}}}{\sqrt{1 + \frac{4}{x}} + \sqrt{1 - \frac{1}{x^3}}} = \frac{4\sqrt{x} + \frac{1}{x^{3/2}}}{1 + 1} \to \frac{+\infty}{2} = \mathbf{+\infty}$$ I si el terme de major grau restant fos $x$ (grau $1 < 1{,}5$), el límit donaria \*\*$0$\*\*!

—

## Apartat h

Calcula el límit: $$\lim_{x \to +\infty} \left(\sqrt{x^2 + x} - x\right)$$

### Pas 1: Identificar la indeterminació

Avaluem directament: $$[+\infty - \infty]$$

### Pas 2: Multiplicar i dividir pel conjugat

Multipliquem i dividim per $(\sqrt{x^2 + x} + x)$: $$\lim_{x \to +\infty} \frac{\left(\sqrt{x^2 + x} - x\right)\left(\sqrt{x^2 + x} + x\right)}{\sqrt{x^2 + x} + x}$$

### Pas 3: Desenvolupar el numerador

Apliquem $(a-b)(a+b) = a^2 - b^2$: $$\lim_{x \to +\infty} \frac{(\sqrt{x^2 + x})^2 - x^2}{\sqrt{x^2 + x} + x} = \lim_{x \to +\infty} \frac{x^2 + x - x^2}{\sqrt{x^2 + x} + x} = \lim_{x \to +\infty} \frac{x}{\sqrt{x^2 + x} + x}$$

### Pas 4: Dividir per $x$

Dividim numerador i denominador per $x$ (recordant que $x = \sqrt{x^2}$ per $x>0$): $$\lim_{x \to +\infty} \frac{\frac{x}{x}}{\sqrt{\frac{x^2 + x}{x^2}} + \frac{x}{x}} = \lim_{x \to +\infty} \frac{1}{\sqrt{1 + \frac{1}{x}} + 1} = \frac{1}{\sqrt{1 + 0} + 1} = \mathbf{\frac{1}{2}}$$

—

## Apartat i

Calcula el límit directament dividint pel terme de major grau ($x$): $$\lim_{x \to -\infty} \frac{3x + 1}{\sqrt{x^2 + 1}}$$

### Pas 1: Identificar la indeterminació

En avaluar directament quan $x \to -\infty$: $$\left[\frac{-\infty}{+\infty}\right]$$

### Pas 2: Dividir numerador i denominador per $x$

Dividim el numerador i el denominador pel terme de major grau, que és $x$: $$\lim_{x \to -\infty} \frac{\frac{3x + 1}{x}}{\frac{\sqrt{x^2 + 1}}{x}} = \lim_{x \to -\infty} \frac{3 + \frac{1}{x}}{\frac{\sqrt{x^2 + 1}}{x}}$$

### Pas 3: Introduir la $x$ dins de l’arrel (Explicació clau del signe)

Com que $x \to -\infty$, considerem valors de $x$ estrictament negatius ($x < 0$). Recordem que $\sqrt{x^2} = |x|$. Quan $x < 0$, tenim que $|x| = -x$, per la qual cosa: $$x = -\sqrt{x^2}$$ Per tant, en ficar la $x$ dins de l’arrel quadrada del denominador, el signe menys es manté a fora: $$\frac{\sqrt{x^2 + 1}}{x} = \frac{\sqrt{x^2 + 1}}{-\sqrt{x^2}} = -\sqrt{\frac{x^2 + 1}{x^2}} = -\sqrt{1 + \frac{1}{x^2}}$$

### Pas 4: Avaluar el límit

Reecreiem l’expressió simplificada: $$\lim_{x \to -\infty} \frac{3 + \frac{1}{x}}{-\sqrt{1 + \frac{1}{x^2}}}$$ Com que $\lim_{x \to -\infty} \frac{1}{x} = 0$ i $\lim_{x \to -\infty} \frac{1}{x^2} = 0$: $$\frac{3 + 0}{-\sqrt{1 + 0}} = \frac{3}{-1} = \mathbf{-3}$$

—

## Apartat j

Calcula el límit: $$\lim_{x \to +\infty} \frac{3x + 1}{\sqrt{x^2 + 2}}$$

### Pas 1: Identificar la indeterminació

Avaluem directament: $$\left[\frac{+\infty}{+\infty}\right]$$

### Pas 2: Dividir pel terme de major grau ($x$)

Dividim numerador i denominador per $x = \sqrt{x^2}$: $$\lim_{x \to +\infty} \frac{\frac{3x + 1}{x}}{\sqrt{\frac{x^2 + 2}{x^2}}} = \lim_{x \to +\infty} \frac{3 + \frac{1}{x}}{\sqrt{1 + \frac{2}{x^2}}}$$

### Pas 3: Avaluar el límit

$$\frac{3 + 0}{\sqrt{1 + 0}} = \frac{3}{1} = \mathbf{3}$$
