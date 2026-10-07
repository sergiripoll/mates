---
title: Límits i continuïtat: Exercicis
tematitol: Límits i continuïtat
curs: 2n
modalitat: cientific
tema: limits
bloc: exercicis
ordre: 2
---
# Límits i continuïtat: Exercicis

## Dossier de límits

### Col·lecció d’Exercicis de Consolidació

#### Bloc 1: Càlcul Directe i Límits Laterals (Nivell Bàsic – 30%)

Calcula els límits següents:

2

1.  $\lim_{x \to 3} \frac{x^2 - 9}{x + 1}$

2.  $\lim_{x \to 1} \frac{3x + 1}{4 - 2x}$

3.  $\lim_{x \to -2} \frac{x^2 + 3}{2x + 1}$

4.  $\lim_{x \to -\infty} (3x^3 - 5x^2 + 1)$

5.  $\lim_{x \to +\infty} \frac{5x^2 - 2x + 1}{3 - x^3}$

6.  $\lim_{x \to +\infty} \frac{-4x^4 + 2x^2}{2x^4 + 5}$

#### Bloc 2: Indeterminacions Algebraiques (Nivell Mitjà – 40%)

Resol les següents indeterminacions $\left[\frac{0}{0}\right]$, $\left[\frac{\infty}{\infty}\right]$ i $[\infty - \infty]$:

1.  $\lim_{x \to 4} \frac{x^2 - 16}{2x - 8}$

2.  $\lim_{x \to 1} \frac{x^2 - 3x + 2}{x^2 + x - 2}$

3.  $\lim_{x \to 3} \frac{x - 1}{x^2 - 5x + 6} \quad (\text{Calcula els límits laterals})$

4.  $\lim_{x \to 0} \frac{\sqrt{x + 4} - 2}{x}$

5.  $\lim_{x \to +\infty} \left( \frac{2x^2 + 1}{x - 1} - \frac{2x^2 - 3}{x + 2} \right)$

6.  $\lim_{x \to +\infty} (\sqrt{x^2 + 4x} - x)$

#### Bloc 3: Indeterminació $1^\infty$ i Exponencials (Nivell Mitjà-Alt)

1.  $\lim_{x \to +\infty} \left( \frac{x + 3}{x - 2} \right)^{2x + 1}$

2.  $\lim_{x \to +\infty} \left( \frac{3x^2 + 2}{3x^2 - 1} \right)^{x^2}$

3.  $\lim_{x \to 0} (1 + 3x)^{\frac{2}{x}}$

#### Bloc 4: Assímptotes i Continuïtat (Nivell Alt – 20%)

1.  Determina totes les assímptotes de la funció $f(x) = \frac{x^2 - 9}{x^2 - 4}$.

2.  Determina les assímptotes verticals, horitzontals i oblíques de $g(x) = \frac{2x^2 + 3x}{x - 1}$.

3.  Estudia la continuïtat de la funció següent en $x = 1$ i indica el tipus de discontinuïtat si escau: $$f(x) = \begin{cases} x^2 + 1 & \text{si } x < 1 \\ 4 - x & \text{si } x \ge 1 \end{cases}$$

4.  Troba el valor del paràmetre $a \in \mathbb{R}$ perquè la funció $f(x)$ sigui contínua en $x = 2$: $$f(x) = \begin{cases} 2x + a & \text{si } x \le 2 \\ x^2 - a x + 2 & \text{si } x > 2 \end{cases}$$

### Solucionari Complet

1.  **Resolució:** Substitució directa: $\frac{3^2 - 9}{3 + 1} = \frac{0}{4} = \mathbf{0}$.

2.  **Resolució:** Substitució directa: $\frac{3(1) + 1}{4 - 2(1)} = \frac{4}{2} = \mathbf{2}$.

3.  **Resolució:** Substitució directa: $\frac{(-2)^2 + 3}{2(-2) + 1} = \frac{4 + 3}{-4 + 1} = \mathbf{-\frac{7}{3}}$.

4.  **Resolució:** Domina el terme de grau més alt $3x^3$. Quan $x \to -\infty$, $x^3 \to -\infty$, per tant $3(-\infty) = \mathbf{-\infty}$.

5.  **Resolució:** Grau del numerador (2) $<$ Grau del denominador (3). El límit és $\mathbf{0}$.

6.  **Resolució:** Els graus són iguals (4). El límit és el quocient de coeficients principals: $\frac{-4}{2} = \mathbf{-2}$.

7.  **Resolució:** Indeterminació $\left[\frac{0}{0}\right]$. Factoritzem: $\lim_{x \to 4} \frac{(x - 4)(x + 4)}{2(x - 4)} = \lim_{x \to 4} \frac{x + 4}{2} = \frac{8}{2} = \mathbf{4}$.

8.  **Resolució:** Indeterminació $\left[\frac{0}{0}\right]$. Factoritzem numerador i denominador: $\lim_{x \to 1} \frac{(x - 1)(x - 2)}{(x - 1)(x + 2)} = \lim_{x \to 1} \frac{x - 2}{x + 2} = \frac{1 - 2}{1 + 2} = \mathbf{-\frac{1}{3}}$.

9.  **Resolució:** Substitució directa dona $\frac{2}{0}$. Analitzem els límits laterals en $x = 3$: $x^2 - 5x + 6 = (x - 2)(x - 3)$.

    - $\lim_{x \to 3^-} \frac{x - 1}{(x - 2)(x - 3)} = \frac{2}{(1)(0^-)} = \mathbf{-\infty}$.

    - $\lim_{x \to 3^+} \frac{x - 1}{(x - 2)(x - 3)} = \frac{2}{(1)(0^+)} = \mathbf{+\infty}$.

    Com que els límits laterals són diferents, **no existeix el límit global**.

10. **Resolució:** Indeterminació $\left[\frac{0}{0}\right]$. Multipliquem pel conjugat: $$\lim_{x \to 0} \frac{(\sqrt{x+4}-2)(\sqrt{x+4}+2)}{x(\sqrt{x+4}+2)} = \lim_{x \to 0} \frac{(x+4)-4}{x(\sqrt{x+4}+2)} = \lim_{x \to 0} \frac{x}{x(\sqrt{x+4}+2)} = \lim_{x \to 0} \frac{1}{\sqrt{x+4}+2} = \mathbf{\frac{1}{4}}$$

11. **Resolució:** Indeterminació $[\infty - \infty]$. Reduïm a comú denominador $(x-1)(x+2) = x^2 + x - 2$: $$\lim_{x \to +\infty} \frac{(2x^2 + 1)(x + 2) - (2x^2 - 3)(x - 1)}{x^2 + x - 2} = \lim_{x \to +\infty} \frac{(2x^3 + 4x^2 + x + 2) - (2x^3 - 2x^2 - 3x + 3)}{x^2 + x - 2}$$ $$= \lim_{x \to +\infty} \frac{6x^2 + 4x - 1}{x^2 + x - 2} = \mathbf{6} \quad (\text{igualtat de graus})$$

12. **Resolució:** Indeterminació $[\infty - \infty]$. Multipliquem pel conjugat: $$\lim_{x \to +\infty} \frac{(\sqrt{x^2+4x}-x)(\sqrt{x^2+4x}+x)}{\sqrt{x^2+4x}+x} = \lim_{x \to +\infty} \frac{(x^2+4x) - x^2}{\sqrt{x^2+4x}+x} = \lim_{x \to +\infty} \frac{4x}{\sqrt{x^2+4x}+x}$$ Dividint per $x$: $\lim_{x \to +\infty} \frac{4}{\sqrt{1 + 4/x} + 1} = \frac{4}{1 + 1} = \mathbf{2}$.

13. **Resolució:** Indeterminació $[1^\infty]$. Calculem l’exponent de $e$: $$L = \lim_{x \to +\infty} (2x + 1) \left( \frac{x + 3}{x - 2} - 1 \right) = \lim_{x \to +\infty} (2x + 1) \cdot \frac{5}{x - 2} = \lim_{x \to +\infty} \frac{10x + 5}{x - 2} = 10$$ Resultat: $\mathbf{e^{10}}$.

14. **Resolució:** Indeterminació $[1^\infty]$. Calculem $L$: $$L = \lim_{x \to +\infty} x^2 \left( \frac{3x^2 + 2}{3x^2 - 1} - 1 \right) = \lim_{x \to +\infty} x^2 \cdot \frac{3}{3x^2 - 1} = \lim_{x \to +\infty} \frac{3x^2}{3x^2 - 1} = 1$$ Resultat: $e^1 = \mathbf{e}$.

15. **Resolució:** Indeterminació $[1^\infty]$. Calculem $L$: $$L = \lim_{x \to 0} \frac{2}{x} \cdot (1 + 3x - 1) = \lim_{x \to 0} \frac{2}{x} \cdot 3x = \lim_{x \to 0} 6 = 6$$ Resultat: $\mathbf{e^6}$.

16. **Resolució:**

    - Domini: $x^2 - 4 = 0 \implies x = \pm 2$. Així, $\text{Dom}(f) = \mathbb{R} \setminus \{-2, 2\}$.

    - En $x = 2$: $\lim_{x \to 2} \frac{-5}{0} = \infty \implies$ **A.V. en $x = 2$**.

    - En $x = -2$: $\lim_{x \to -2} \frac{-5}{0} = \infty \implies$ **A.V. en $x = -2$**.

    - A.H.: $\lim_{x \to \pm\infty} \frac{x^2 - 9}{x^2 - 4} = 1 \implies$ **A.H. en $y = 1$**.

    - A.O.: En tenir A.H., **no té A.O.**

17. **Resolució:**

    - Domini: $\mathbb{R} \setminus \{1\}$.

    - En $x = 1$: $\lim_{x \to 1} \frac{2(1)^2+3(1)}{1-1} = \frac{5}{0} = \infty \implies$ **A.V. en $x = 1$**.

    - A.H.: $\lim_{x \to \pm\infty} \frac{2x^2+3x}{x-1} = \pm\infty \implies$ No hi ha A.H.

    - A.O. ($y = mx + n$): $m = \lim_{x \to \pm\infty} \frac{2x^2+3x}{x^2-x} = 2$; $n = \lim_{x \to \pm\infty} \left( \frac{2x^2+3x}{x-1} - 2x \right) = \lim \frac{5x}{x-1} = 5 \implies$ **A.O. en $y = 2x + 5$**.

18. **Resolució:** Estudiem el punt de canvi de branca $x = 1$:

    - $f(1) = 4 - 1 = 3$.

    - $\lim_{x \to 1^-} (x^2 + 1) = 1^2 + 1 = 2$.

    - $\lim_{x \to 1^+} (4 - x) = 4 - 1 = 3$.

    Com que els límits laterals existeixen i són finits però diferents ($\lim_{x \to 1^-} f(x) = 2 \neq \lim_{x \to 1^+} f(x) = 3$), la funció presenta una **discontinuïtat de salt finit en $x = 1$** (amb un salt de mida $|3 - 2| = 1$).

19. **Resolució:** Perquè sigui contínua en $x = 2$, cal que $\lim_{x \to 2^-} f(x) = \lim_{x \to 2^+} f(x) = f(2)$:

    - $f(2) = 2(2) + a = 4 + a$.

    - $\lim_{x \to 2^-} (2x + a) = 4 + a$.

    - $\lim_{x \to 2^+} (x^2 - ax + 2) = 2^2 - 2a + 2 = 6 - 2a$.

    Igualant les dues expressions: $4 + a = 6 - 2a \implies 3a = 2 \implies \mathbf{a = \frac{2}{3}}$.

20. **Resolució:**

    - **Continuïtat en $x = 1$:** $\lim_{x \to 1^-} (ax + 2) = a + 2$. $\lim_{x \to 1^+} (x^2 + b) = 1 + b = f(1)$. Per continuïtat: $a + 2 = 1 + b \implies \mathbf{a - b = -1}$.

    - **Continuïtat en $x = 3$:** $\lim_{x \to 3^-} (x^2 + b) = 9 + b = f(3)$. $\lim_{x \to 3^+} \frac{2x + 8}{x - 1} = \frac{14}{2} = 7$. Per continuïtat: $9 + b = 7 \implies \mathbf{b = -2}$.

    Substituint $b = -2$ a la primera equació: $a - (-2) = -1 \implies a + 2 = -1 \implies \mathbf{a = -3}$. Així, els valors són $\mathbf{a = -3}$ i $\mathbf{b = -2}$.

21. **Resolució:**

    1.  Com que l’assímptota és $y = 3x - 1$, tenim $m = 3$ i $n = -1$. $$m = \lim_{x \to \infty} \frac{f(x)}{x} = \lim_{x \to \infty} \frac{ax^2 + bx - 3}{x^2 + 2x} = a \implies \mathbf{a = 3}$$ $$n = \lim_{x \to \infty} [f(x) - 3x] = \lim_{x \to \infty} \left( \frac{3x^2 + bx - 3 - 3x(x + 2)}{x + 2} \right) = \lim_{x \to \infty} \frac{(b - 6)x - 3}{x + 2} = b - 6$$ Com que $n = -1 \implies b - 6 = -1 \implies \mathbf{b = 5}$. La funció obtinguda és $f(x) = \frac{3x^2 + 5x - 3}{x + 2}$.

    2.  **Domini:** $\mathbb{R} \setminus \{-2\}$. La funció és contínua en tot $\mathbb{R} \setminus \{-2\}$. En $x = -2$: El numerador val $3(-2)^2 + 5(-2) - 3 = 12 - 10 - 3 = -1 \neq 0$. Límits laterals: $\lim_{x \to -2^-} f(x) = \frac{-1}{0^-} = +\infty$ i $\lim_{x \to -2^+} f(x) = \frac{-1}{0^+} = -\infty$. Per tant, presenta una **discontinuïtat de salt infinit en $x = -2$**, on hi ha l’assímptota vertical $\mathbf{x = -2}$.

## Límits amb arrels: exercicis resolts

### Introducció

Aquest document conté la resolució pas a pas dels apartats **d, e, g, g) modificat 1, g) modificat 2, h, i, j** de l’exercici 19 sobre límits en l’infinit amb arrels quadrades.

### Apartat d

Calcula el límit: $$\lim_{x \to +\infty} \frac{2x + 1}{\sqrt{x^2 + 2}}$$

#### Pas 1: Identificar la indeterminació

En avaluar directament quan $x \to +\infty$: $$\frac{2(+\infty) + 1}{\sqrt{(+\infty)^2 + 2}} = \left[\frac{+\infty}{+\infty}\right]$$

#### Pas 2: Dividir pel terme de major grau

Com que $x > 0$, tenim que $x = \sqrt{x^2}$. Dividim numerador i denominador per $x$: $$\lim_{x \to +\infty} \frac{\frac{2x + 1}{x}}{\frac{\sqrt{x^2 + 2}}{x}} = \lim_{x \to +\infty} \frac{2 + \frac{1}{x}}{\sqrt{\frac{x^2 + 2}{x^2}}} = \lim_{x \to +\infty} \frac{2 + \frac{1}{x}}{\sqrt{1 + \frac{2}{x^2}}}$$

#### Pas 3: Avaluar el límit

Com que $\lim_{x \to +\infty} \frac{1}{x} = 0$ i $\lim_{x \to +\infty} \frac{2}{x^2} = 0$: $$\frac{2 + 0}{\sqrt{1 + 0}} = \frac{2}{1} = \mathbf{2}$$

—

### Apartat e

Calcula el límit: $$\lim_{x \to +\infty} \frac{5x + 4}{\sqrt{x^3 + 3}}$$

#### Pas 1: Identificar la indeterminació

Avaluem el límit: $$\left[\frac{+\infty}{+\infty}\right]$$

#### Pas 2: Comparació de graus

- **Grau del numerador:** $1$ (de $5x$).

- **Grau del denominador:** $\frac{3}{2} = 1{,}5$ (ja que $\sqrt{x^3} = x^{3/2}$).

Com que el grau del denominador és **estrictament major** que el del numerador, la fracció tendeix a zero.

#### Pas 3: Demostració algebraicament

Dividim numerador i denominador per $x$: $$\lim_{x \to +\infty} \frac{\frac{5x + 4}{x}}{\frac{\sqrt{x^3 + 3}}{x}} = \lim_{x \to +\infty} \frac{5 + \frac{4}{x}}{\sqrt{\frac{x^3 + 3}{x^2}}} = \lim_{x \to +\infty} \frac{5 + \frac{4}{x}}{\sqrt{x + \frac{3}{x^2}}}$$ En avaluar quan $x \to +\infty$: $$\frac{5 + 0}{\sqrt{+\infty + 0}} = \frac{5}{+\infty} = \mathbf{0}$$

—

### Apartat g

Calcula el límit: $$\lim_{x \to +\infty} \left(\sqrt{2x^2 - 3x} - \sqrt{x^2 + 1}\right)$$

#### Pas 1: Identificar la indeterminació

Avaluem el límit: $$\sqrt{+\infty} - \sqrt{+\infty} = [+\infty - \infty]$$

#### Pas 2: Multiplicar i dividir pel conjugat

Multipliquem i dividim per l’expressió sumant les dues arrels: $$\lim_{x \to +\infty} \frac{\left(\sqrt{2x^2 - 3x} - \sqrt{x^2 + 1}\right)\left(\sqrt{2x^2 - 3x} + \sqrt{x^2 + 1}\right)}{\sqrt{2x^2 - 3x} + \sqrt{x^2 + 1}}$$

#### Pas 3: Simplificar el numerador

Apliquem $(a-b)(a+b) = a^2 - b^2$: $$\lim_{x \to +\infty} \frac{(2x^2 - 3x) - (x^2 + 1)}{\sqrt{2x^2 - 3x} + \sqrt{x^2 + 1}} = \lim_{x \to +\infty} \frac{x^2 - 3x - 1}{\sqrt{2x^2 - 3x} + \sqrt{x^2 + 1}}$$

#### Pas 4: Avaluar el nou límit

Ara tenim una indeterminació $\left[\frac{+\infty}{+\infty}\right]$:

- **Grau del numerador:** $2$.

- **Grau del denominador:** $1$ (les arrels contenen $x^2$, així que el grau efectiu és $1$).

Com que el grau del numerador és major que el del denominador: $$\mathbf{+\infty}$$

—

### Apartat g) Modificat 1 (Graus diferents: Factor comú)

Calcula el límit: $$\lim_{x \to +\infty} \left(\sqrt{2x^3 - 3x} - \sqrt{x^2 + 1}\right)$$

> **Nota pedagògica**
>
> Quan tenim una indeterminació $[\infty - \infty]$ on els dos termes tenen \*\*diferent grau\*\* ($\text{grau}(\sqrt{2x^3-3x}) = 1{,}5$ i $\text{grau}(\sqrt{x^2+1}) = 1$), \*\*no cal utilitzar el conjugat\*\*. El mètode més elegant i ràpid és extreure com a factor comú el terme dominant (de major grau).

#### Pas 1: Extreure factor comú el terme dominant

Treiem factor comú la primera arrel $\sqrt{2x^3 - 3x}$: $$\lim_{x \to +\infty} \sqrt{2x^3 - 3x} \cdot \left(1 - \frac{\sqrt{x^2 + 1}}{\sqrt{2x^3 - 3x}}\right)$$

#### Pas 2: Juntar les arrels de la fracció

Unifiquem la fracció dins d’una sola arrel quadrada: $$\lim_{x \to +\infty} \sqrt{2x^3 - 3x} \cdot \left(1 - \sqrt{\frac{x^2 + 1}{2x^3 - 3x}}\right)$$

#### Pas 3: Analitzar el límit de la fracció interior

Dins de la segona arrel, el numerador té grau $2$ i el denominador té grau $3$: $$\lim_{x \to +\infty} \frac{x^2 + 1}{2x^3 - 3x} = 0 \implies \sqrt{0} = 0$$

#### Pas 4: Avaluar el límit global

Substituïm el resultat: $$(+\infty) \cdot (1 - 0) = (+\infty) \cdot 1 = \mathbf{+\infty}$$

—

### Apartat g) Modificat 2 (Totes dues arrels amb $x^3$: Ús del conjugat i simplificació de $\sqrt{x^3}$)

Calcula el límit: $$\lim_{x \to +\infty} \left(\sqrt{2x^3 - 3x} - \sqrt{x^3 + 1}\right)$$

> **Nota pedagògica: Com simplificar una arrel de $x^3$ desprès del conjugat**
>
> Quan totes dues arrels tenen el mateix grau màxim ($x^3$), apliquem el \*\*conjugat\*\*. Després de simplificar el numerador, ens queda una arrel quadrada de $x^3$ al denominador. Per simplificar-la, dividim numerador i denominador per $\mathbf{\sqrt{x^3}} = x^{3/2}$. Recorda que en entrar $\sqrt{x^3}$ dins d’una arrel quadrada, entra com a \*\*$x^3$\*\*!

#### Pas 1: Aplicar el conjugat

Multipliquem i dividim pel conjugat: $$\lim_{x \to +\infty} \frac{\left(\sqrt{2x^3 - 3x} - \sqrt{x^3 + 1}\right)\left(\sqrt{2x^3 - 3x} + \sqrt{x^3 + 1}\right)}{\sqrt{2x^3 - 3x} + \sqrt{x^3 + 1}}$$

#### Pas 2: Simplificar el numerador

Apliquem $(a-b)(a+b) = a^2 - b^2$: $$\lim_{x \to +\infty} \frac{(2x^3 - 3x) - (x^3 + 1)}{\sqrt{2x^3 - 3x} + \sqrt{x^3 + 1}} = \lim_{x \to +\infty} \frac{x^3 - 3x - 1}{\sqrt{2x^3 - 3x} + \sqrt{x^3 + 1}}$$

#### Pas 3: Com eliminar / simplificar la $\sqrt{x^3}$ del denominador

Avaluem els graus:

- \*\*Grau del numerador:\*\* $3$ (de $x^3$).

- \*\*Grau del denominador:\*\* $\frac{3}{2} = 1{,}5$ (de $\sqrt{x^3}$).

Per simplificar el denominador, dividim el numerador i el denominador pel terme dominant del denominador, que és $\mathbf{\sqrt{x^3}}$:

$$\lim_{x \to +\infty} \frac{\frac{x^3 - 3x - 1}{\sqrt{x^3}}}{\frac{\sqrt{2x^3 - 3x} + \sqrt{x^3 + 1}}{\sqrt{x^3}}}$$

#### Pas 4: Operar amb la $\sqrt{x^3}$

1.  \*\*Al denominador:\*\* Com que $\frac{\sqrt{A}}{\sqrt{B}} = \sqrt{\frac{A}{B}}$, la $\sqrt{x^3}$ entra directament com a $x^3$ dins de cada arrel: $$\frac{\sqrt{2x^3 - 3x}}{\sqrt{x^3}} + \frac{\sqrt{x^3 + 1}}{\sqrt{x^3}} = \sqrt{\frac{2x^3 - 3x}{x^3}} + \sqrt{\frac{x^3 + 1}{x^3}} = \sqrt{2 - \frac{3}{x^2}} + \sqrt{1 + \frac{1}{x^3}}$$ Quan $x \to +\infty$, això tendeix a $\sqrt{2 - 0} + \sqrt{1 + 0} = \mathbf{\sqrt{2} + 1}$.

2.  \*\*Al numerador:\*\* Expressem $\sqrt{x^3} = x^{3/2}$: $$\frac{x^3 - 3x - 1}{x^{3/2}} = \frac{x^3}{x^{3/2}} - \frac{3x}{x^{3/2}} - \frac{1}{x^{3/2}} = x^{3/2} - \frac{3}{\sqrt{x}} - \frac{1}{x\sqrt{x}}$$ Quan $x \to +\infty$, el primer terme $x^{3/2} \to +\infty$ i els altres dos tendeixen a $0$.

#### Pas 5: Avaluar el límit final

Substituïm els valors obtinguts: $$\frac{+\infty - 0 - 0}{\sqrt{2} + 1} = \frac{+\infty}{\sqrt{2} + 1} = \mathbf{+\infty}$$

> **Variant amb coeficients iguals ($x^3$ es cancel·la al numerador)**
>
> Si tinguéssim $\lim_{x \to +\infty} \left(\sqrt{x^3 + 4x^2} - \sqrt{x^3 - 1}\right)$, al fer el conjugat el $x^3$ del numerador es cancel·laria: $$\frac{(x^3 + 4x^2) - (x^3 - 1)}{\sqrt{x^3 + 4x^2} + \sqrt{x^3 - 1}} = \frac{4x^2 + 1}{\sqrt{x^3 + 4x^2} + \sqrt{x^3 - 1}}$$ En dividint numerador i denominador per $\sqrt{x^3}$: $$\frac{\frac{4x^2 + 1}{x^{3/2}}}{\sqrt{1 + \frac{4}{x}} + \sqrt{1 - \frac{1}{x^3}}} = \frac{4\sqrt{x} + \frac{1}{x^{3/2}}}{1 + 1} \to \frac{+\infty}{2} = \mathbf{+\infty}$$ I si el terme de major grau restant fos $x$ (grau $1 < 1{,}5$), el límit donaria \*\*$0$\*\*!

—

### Apartat h

Calcula el límit: $$\lim_{x \to +\infty} \left(\sqrt{x^2 + x} - x\right)$$

#### Pas 1: Identificar la indeterminació

Avaluem directament: $$[+\infty - \infty]$$

#### Pas 2: Multiplicar i dividir pel conjugat

Multipliquem i dividim per $(\sqrt{x^2 + x} + x)$: $$\lim_{x \to +\infty} \frac{\left(\sqrt{x^2 + x} - x\right)\left(\sqrt{x^2 + x} + x\right)}{\sqrt{x^2 + x} + x}$$

#### Pas 3: Desenvolupar el numerador

Apliquem $(a-b)(a+b) = a^2 - b^2$: $$\lim_{x \to +\infty} \frac{(\sqrt{x^2 + x})^2 - x^2}{\sqrt{x^2 + x} + x} = \lim_{x \to +\infty} \frac{x^2 + x - x^2}{\sqrt{x^2 + x} + x} = \lim_{x \to +\infty} \frac{x}{\sqrt{x^2 + x} + x}$$

#### Pas 4: Dividir per $x$

Dividim numerador i denominador per $x$ (recordant que $x = \sqrt{x^2}$ per $x>0$): $$\lim_{x \to +\infty} \frac{\frac{x}{x}}{\sqrt{\frac{x^2 + x}{x^2}} + \frac{x}{x}} = \lim_{x \to +\infty} \frac{1}{\sqrt{1 + \frac{1}{x}} + 1} = \frac{1}{\sqrt{1 + 0} + 1} = \mathbf{\frac{1}{2}}$$

—

### Apartat i

Calcula el límit directament dividint pel terme de major grau ($x$): $$\lim_{x \to -\infty} \frac{3x + 1}{\sqrt{x^2 + 1}}$$

#### Pas 1: Identificar la indeterminació

En avaluar directament quan $x \to -\infty$: $$\left[\frac{-\infty}{+\infty}\right]$$

#### Pas 2: Dividir numerador i denominador per $x$

Dividim el numerador i el denominador pel terme de major grau, que és $x$: $$\lim_{x \to -\infty} \frac{\frac{3x + 1}{x}}{\frac{\sqrt{x^2 + 1}}{x}} = \lim_{x \to -\infty} \frac{3 + \frac{1}{x}}{\frac{\sqrt{x^2 + 1}}{x}}$$

#### Pas 3: Introduir la $x$ dins de l’arrel (Explicació clau del signe)

Com que $x \to -\infty$, considerem valors de $x$ estrictament negatius ($x < 0$). Recordem que $\sqrt{x^2} = |x|$. Quan $x < 0$, tenim que $|x| = -x$, per la qual cosa: $$x = -\sqrt{x^2}$$ Per tant, en ficar la $x$ dins de l’arrel quadrada del denominador, el signe menys es manté a fora: $$\frac{\sqrt{x^2 + 1}}{x} = \frac{\sqrt{x^2 + 1}}{-\sqrt{x^2}} = -\sqrt{\frac{x^2 + 1}{x^2}} = -\sqrt{1 + \frac{1}{x^2}}$$

#### Pas 4: Avaluar el límit

Reecreiem l’expressió simplificada: $$\lim_{x \to -\infty} \frac{3 + \frac{1}{x}}{-\sqrt{1 + \frac{1}{x^2}}}$$ Com que $\lim_{x \to -\infty} \frac{1}{x} = 0$ i $\lim_{x \to -\infty} \frac{1}{x^2} = 0$: $$\frac{3 + 0}{-\sqrt{1 + 0}} = \frac{3}{-1} = \mathbf{-3}$$

—

### Apartat j

Calcula el límit: $$\lim_{x \to +\infty} \frac{3x + 1}{\sqrt{x^2 + 2}}$$

#### Pas 1: Identificar la indeterminació

Avaluem directament: $$\left[\frac{+\infty}{+\infty}\right]$$

#### Pas 2: Dividir pel terme de major grau ($x$)

Dividim numerador i denominador per $x = \sqrt{x^2}$: $$\lim_{x \to +\infty} \frac{\frac{3x + 1}{x}}{\sqrt{\frac{x^2 + 2}{x^2}}} = \lim_{x \to +\infty} \frac{3 + \frac{1}{x}}{\sqrt{1 + \frac{2}{x^2}}}$$

#### Pas 3: Avaluar el límit

$$\frac{3 + 0}{\sqrt{1 + 0}} = \frac{3}{1} = \mathbf{3}$$
