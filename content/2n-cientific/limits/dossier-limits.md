---
title: Límits i continuïtat: dossier de repàs
curs: 2n
modalitat: cientific
tema: limits
tipus: teoria
---
# Límits i continuïtat: dossier de repàs

> **DOSSIER DE REPÀS I CONSOLIDACIÓ**  
> UNITAT 1: LÍMITS DE FUNCIONS I CONTINUÏTAT  
> Matemàtiques II — 2n de Batxillerat

## Què hem de saber

Aquest dossier recull, estructura i amplia el treball realitzat a l’aula sobre el càlcul de límits, l’estudi d’assímptotes i la continuïtat de funcions. L’objectiu és consolidar els procediments algebraics i preparar-te per als exàmens de 2n de Batxillerat i les proves d’accés a la universitat (PAU).

**Objectius d’aprenentatge del tema:**

- Comprendre el concepte intuïtiu i formal de límit en un punt i a l’infinit.

- Dominar el càlcul d’algebrització de límits i la resolució de totes les indeterminacions ($0/0$, $\infty/\infty$, $\infty-\infty$, $0 \cdot \infty$, $1^\infty$).

- Determinar l’existència d’assímptotes verticals, horitzontals i oblíques en funcions racionals i irracionals.

- Analitzar la continuïtat d’una funció en un punt i en un interval, classificant-ne els tipus de discontinuïtat.

- Trobar paràmetres desconeguts per garantir la continuïtat o l’existència d’assímptotes.

—

## Conceptes Teòrics i Propietats

> **📘 Definició**
>
> Límit d’una funció en un punt Diem que el límit de la funció $f(x)$ quan $x$ tendeix al punt $a$ és el nombre real $L$, i ho escrivim: $$\lim_{x \to a} f(x) = L$$ si a mesura que $x$ s’aproxima a $a$ (però sense ser necessàriament igual a $a$), les imatges $f(x)$ s’aproximen tant com vulguem a $L$.

> **📘 Propietat**
>
> Límits laterals i existència del límit global Perquè existeixi el límit d’una funció en un punt $x = a$, és condició necessària i suficient que existeixin els dos límits laterals (per l’esquerra i per la dreta) i que siguin iguals: $$\lim_{x \to a} f(x) = L \iff \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L$$ Si els límits laterals no coincideixen, o si algun d’ells no existeix o és infinit, diem que **no existeix el límit finit global**.

### Àlgebra de límits

Si $\lim_{x \to a} f(x) = L$ i $\lim_{x \to a} g(x) = M$ (amb $L, M \in \mathbb{R}$), es compleixen les propietats següents:

1.  **Suma / Resta:** $\lim_{x \to a} [f(x) \pm g(x)] = L \pm M$

2.  **Producte:** $\lim_{x \to a} [f(x) \cdot g(x)] = L \cdot M$

3.  **Quocient:** $\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{L}{M} \quad (\text{si } M \neq 0)$

4.  **Producte per una constant:** $\lim_{x \to a} [k \cdot f(x)] = k \cdot L \quad (\forall k \in \mathbb{R})$

5.  **Potència:** $\lim_{x \to a} [f(x)]^{g(x)} = L^M \quad (\text{si } L > 0)$

### Operacions amb l’infinit ($\infty$)

En el càlcul de límits operem sovint amb la recta real ampliada. És fonamental recordar:

2

- $(+\infty) + (+\infty) = +\infty$

- $(-\infty) - (+\infty) = -\infty$

- $k \cdot (\pm\infty) = \pm\infty \quad (\text{si } k > 0)$

- $k \cdot (\pm\infty) = \mp\infty \quad (\text{si } k < 0)$

- $\frac{k}{\pm\infty} = 0 \quad (\forall k \in \mathbb{R})$

- $\frac{k}{0} = \infty \quad (\text{si } k \neq 0, \text{cal mirar laterals})$

- $k^{+\infty} = +\infty \quad (\text{si } k > 1)$

- $k^{+\infty} = 0 \quad (\text{si } 0 < k < 1)$

- $k^{-\infty} = 0 \quad (\text{si } k > 1)$

—

## Mètodes de Càlcul i Indeterminacions

En avaluar un límit, el primer pas és sempre la **substitució directa**. Quan aquesta condueix a una expressió no definida, ens trobem davant d’una **indeterminació**.

Les 7 indeterminacions clàssiques són: $$\left[\frac{0}{0}\right], \quad \left[\frac{\infty}{\infty}\right], \quad [\infty - \infty], \quad [0 \cdot \infty], \quad [1^\infty], \quad [0^0], \quad [\infty^0]$$

> **📘 Propietat**
>
> Resolució de les Indeterminacions principals
>
> 1.  **Indeterminació $\left[\frac{0}{0}\right]$:**
>
>     - *Funcions racionals:* Factoritzem numerador i denominador (mitjançant Ruffini o treure factor comú) i simplifiquem el factor $(x-a)$.
>
>     - *Funcions amb arrels radicals:* Multipliquem i dividim per l’expressió conjugada.
>
> 2.  **Indeterminació $\left[\frac{\infty}{\infty}\right]$:** En funcions racionals quan $x \to \pm\infty$, comparem els graus del numerador $P(x)$ i denominador $Q(x)$:
>
>     - Si $\text{grau}(P) < \text{grau}(Q) \implies \lim = 0$.
>
>     - Si $\text{grau}(P) = \text{grau}(Q) \implies \lim = \frac{\text{coeficient principal de } P}{\text{coeficient principal de } Q}$.
>
>     - Si $\text{grau}(P) > \text{grau}(Q) \implies \lim = \pm\infty$ (el signe depèn dels coeficients i del signe de $x$).
>
> 3.  **Indeterminació $[\infty - \infty]$:**
>
>     - Si és una resta de fraccions algebraiques: reduïm a comú denominador i operem.
>
>     - Si intervenen radicals: multiplicem i dividim pel conjugat.
>
> 4.  **Indeterminació $[1^\infty]$:** S’aplica la fórmula de la relació amb el nombre $e$: $$\lim_{x \to a} [f(x)]^{g(x)} = e^L \quad \text{on} \quad L = \lim_{x \to a} \left( g(x) \cdot [f(x) - 1] \right)$$

—

## Assímptotes d’una Funció

> **📘 Definició**
>
> Assímptota Vertical (A.V.) La recta vertical $x = a$ és una assímptota vertical de $f(x)$ si es compleix algun dels límits laterals següents: $$\lim_{x \to a^-} f(x) = \pm\infty \quad \text{o} \quad \lim_{x \to a^+} f(x) = \pm\infty$$ **On buscar-les?** En els punts que anul·len el denominador o en els extrems de domini no inclosos.

> **📘 Definició**
>
> Assímptota Horitzontal (A.H.) La recta horitzontal $y = k$ és una assímptota horitzontal quan $x \to +\infty$ (o $x \to -\infty$) si: $$\lim_{x \to +\infty} f(x) = k \quad \text{o} \quad \lim_{x \to -\infty} f(x) = L \quad (k, L \in \mathbb{R})$$

> **📘 Definició**
>
> Assímptota Oblíqua (A.O.) La recta $y = mx + n$ (amb $m \neq 0$) és una assímptota oblíqua quan $x \to \pm\infty$ si existeixen i són finits els límits: $$m = \lim_{x \to \pm\infty} \frac{f(x)}{x}, \qquad n = \lim_{x \to \pm\infty} [f(x) - m x]$$

> **⚠️ Alerta**
>
> Incompatibilitat d’Assímptotes En una mateixa branca ($x \to +\infty$ o $x \to -\infty$), si una funció té assímptota horitzontal, **no pot tenir assímptota oblíqua**. En funcions racionals $\frac{P(x)}{Q(x)}$, hi haurà assímptota oblíqua si i només si $\text{grau}(P) = \text{grau}(Q) + 1$.

—

## Continuïtat de Funcions

> **📘 Definició**
>
> Continuïtat en un punt Una funció $f(x)$ és contínua en el punt $x = a$ si es compleixen simultàniament les tres condicions següents:
>
> 1.  Existeix la imatge del punt: $a \in \text{Dom}(f) \implies \exists f(a)$.
>
> 2.  Existeix el límit finit en el punt: $\exists \lim_{x \to a} f(x) = L \in \mathbb{R}$.
>
> 3.  El valor del límit coincideix amb la imatge: $\lim_{x \to a} f(x) = f(a)$.

### Tipus de Discontinuïtat

Si no es compleix alguna de les tres condicions, la funció presenta una discontinuïtat en $x = a$:

- **Discontinuïtat Evitable:** Existeix $\lim_{x \to a} f(x) = L \in \mathbb{R}$, però o bé no existeix $f(a)$, o bé $f(a) \neq L$.

- **Discontinuïtat de Salt Finit:** Existeixen els dos límits laterals i són finits, però diferents: $$\lim_{x \to a^-} f(x) = L_1 \neq \lim_{x \to a^+} f(x) = L_2 \implies \text{Salt} = |L_2 - L_1|$$

- **Discontinuïtat de Salt Infinit (o Essencial):** Almenys un dels dos límits laterals és infinit ($\pm\infty$).

—

## Exemples Resolts Pas a Pas

> **✏️ Exemple**
>
> Indeterminació $0/0$ amb factorització Calcula el límit: $\lim_{x \to 3} \frac{3x - 9}{x^2 - 2x - 3}$.
>
> **Resolució:** 1. *Substitució directa:* $\frac{3(3)-9}{3^2 - 2(3) - 3} = \frac{0}{0} \implies$ Indeterminació. 2. *Factorització:*
>
> - Numerador: $3x - 9 = 3(x - 3)$.
>
> - Denominador: Les arrels de $x^2 - 2x - 3 = 0$ són $x = 3$ i $x = -1$, per tant $x^2 - 2x - 3 = (x - 3)(x + 1)$.
>
> 3\. *Simplificació i càlcul:* $$\lim_{x \to 3} \frac{3(x - 3)}{(x - 3)(x + 1)} = \lim_{x \to 3} \frac{3}{x + 1} = \frac{3}{3 + 1} = \frac{3}{4}$$

> **✏️ Exemple**
>
> Indeterminació $0/0$ amb arrels (Conjugat) Calcula el límit: $\lim_{x \to 2} \frac{\sqrt{x + 7} - 3}{x - 2}$.
>
> **Resolució:** 1. *Substitució directa:* $\frac{\sqrt{2 + 7} - 3}{2 - 2} = \frac{3 - 3}{0} = \frac{0}{0} \implies$ Indeterminació. 2. *Multiplicació pel conjugat:* $$\lim_{x \to 2} \frac{(\sqrt{x + 7} - 3)(\sqrt{x + 7} + 3)}{(x - 2)(\sqrt{x + 7} + 3)} = \lim_{x \to 2} \frac{(x + 7) - 9}{(x - 2)(\sqrt{x + 7} + 3)}$$ $$= \lim_{x \to 2} \frac{x - 2}{(x - 2)(\sqrt{x + 7} + 3)} = \lim_{x \to 2} \frac{1}{\sqrt{x + 7} + 3} = \frac{1}{\sqrt{9} + 3} = \frac{1}{6}$$

> **✏️ Exemple**
>
> Indeterminació $1^\infty$ Calcula el límit: $\lim_{x \to +\infty} \left( \frac{2x + 3}{2x - 1} \right)^{3x + 1}$.
>
> **Resolució:** 1. *Substitució directa:* La base tendeix a $\frac{2}{2} = 1$ i l’exponent a $+\infty$. És tipus $[1^\infty]$. 2. *Aplicació de la fórmula del nombre $e$:* $e^L$ on $L = \lim_{x \to +\infty} g(x)[f(x) - 1]$. $$L = \lim_{x \to +\infty} (3x + 1) \left( \frac{2x + 3}{2x - 1} - 1 \right) = \lim_{x \to +\infty} (3x + 1) \left( \frac{2x + 3 - (2x - 1)}{2x - 1} \right)$$ $$= \lim_{x \to +\infty} (3x + 1) \left( \frac{4}{2x - 1} \right) = \lim_{x \to +\infty} \frac{12x + 4}{2x - 1} = \frac{12}{2} = 6$$ 3. *Resultat final:* El límit és $e^6$.

> **✏️ Exemple**
>
> Estudi complet d’assímptotes Troba totes les assímptotes de la funció $f(x) = \frac{x^3 + x^2}{x^2 - 4}$.
>
> **Resolució:** 1. *Domini:* $x^2 - 4 = 0 \implies x = \pm 2$. Així, $\text{Dom}(f) = \mathbb{R} \setminus \{-2, 2\}$. 2. *Assímptotes Verticals:*
>
> - En $x = 2$: $\lim_{x \to 2} \frac{2^3+2^2}{2^2-4} = \frac{12}{0} = \infty$. $\lim_{x \to 2^-} f(x) = \frac{12}{0^-} = -\infty$ i $\lim_{x \to 2^+} f(x) = \frac{12}{0^+} = +\infty$. **A.V. en $x = 2$**.
>
> - En $x = -2$: $\lim_{x \to -2} \frac{(-2)^3+(-2)^2}{(-2)^2-4} = \frac{-4}{0} = \infty$. $\lim_{x \to -2^-} f(x) = \frac{-4}{0^+} = -\infty$ i $\lim_{x \to -2^+} f(x) = \frac{-4}{0^-} = +\infty$. **A.V. en $x = -2$**.
>
> 3\. *Assímptotes Horitzontals:* $\lim_{x \to \pm\infty} \frac{x^3 + x^2}{x^2 - 4} = \pm\infty \implies$ **No hi ha A.H.** 4. *Assímptotes Oblíques ($y = mx + n$):* $$m = \lim_{x \to \pm\infty} \frac{f(x)}{x} = \lim_{x \to \pm\infty} \frac{x^3 + x^2}{x^3 - 4x} = 1$$ $$n = \lim_{x \to \pm\infty} [f(x) - x] = \lim_{x \to \pm\infty} \left( \frac{x^3 + x^2 - x(x^2 - 4)}{x^2 - 4} \right) = \lim_{x \to \pm\infty} \frac{x^2 + 4x}{x^2 - 4} = 1$$ **Té una Assímptota Oblíqua en $y = x + 1$**.

—

## Col·lecció d’Exercicis de Consolidació

### Bloc 1: Càlcul Directe i Límits Laterals (Nivell Bàsic – 30%)

Calcula els límits següents:

2

1.  $\lim_{x \to 3} \frac{x^2 - 9}{x + 1}$

2.  $\lim_{x \to 1} \frac{3x + 1}{4 - 2x}$

3.  $\lim_{x \to -2} \frac{x^2 + 3}{2x + 1}$

4.  $\lim_{x \to -\infty} (3x^3 - 5x^2 + 1)$

5.  $\lim_{x \to +\infty} \frac{5x^2 - 2x + 1}{3 - x^3}$

6.  $\lim_{x \to +\infty} \frac{-4x^4 + 2x^2}{2x^4 + 5}$

### Bloc 2: Indeterminacions Algebraiques (Nivell Mitjà – 40%)

Resol les següents indeterminacions $\left[\frac{0}{0}\right]$, $\left[\frac{\infty}{\infty}\right]$ i $[\infty - \infty]$:

1.  $\lim_{x \to 4} \frac{x^2 - 16}{2x - 8}$

2.  $\lim_{x \to 1} \frac{x^2 - 3x + 2}{x^2 + x - 2}$

3.  $\lim_{x \to 3} \frac{x - 1}{x^2 - 5x + 6} \quad (\text{Calcula els límits laterals})$

4.  $\lim_{x \to 0} \frac{\sqrt{x + 4} - 2}{x}$

5.  $\lim_{x \to +\infty} \left( \frac{2x^2 + 1}{x - 1} - \frac{2x^2 - 3}{x + 2} \right)$

6.  $\lim_{x \to +\infty} (\sqrt{x^2 + 4x} - x)$

### Bloc 3: Indeterminació $1^\infty$ i Exponencials (Nivell Mitjà-Alt)

1.  $\lim_{x \to +\infty} \left( \frac{x + 3}{x - 2} \right)^{2x + 1}$

2.  $\lim_{x \to +\infty} \left( \frac{3x^2 + 2}{3x^2 - 1} \right)^{x^2}$

3.  $\lim_{x \to 0} (1 + 3x)^{\frac{2}{x}}$

### Bloc 4: Assímptotes i Continuïtat (Nivell Alt – 20%)

1.  Determina totes les assímptotes de la funció $f(x) = \frac{x^2 - 9}{x^2 - 4}$.

2.  Determina les assímptotes verticals, horitzontals i oblíques de $g(x) = \frac{2x^2 + 3x}{x - 1}$.

3.  Estudia la continuïtat de la funció següent en $x = 1$ i indica el tipus de discontinuïtat si escau: $$f(x) = \begin{cases} x^2 + 1 & \text{si } x < 1 \\ 4 - x & \text{si } x \ge 1 \end{cases}$$

4.  Troba el valor del paràmetre $a \in \mathbb{R}$ perquè la funció $f(x)$ sigui contínua en $x = 2$: $$f(x) = \begin{cases} 2x + a & \text{si } x \le 2 \\ x^2 - a x + 2 & \text{si } x > 2 \end{cases}$$

### Bloc 5: Problemes Globals i Tipus Examen / PAU (Nivell Molt Alt – 10%)

1.  **\[Model PAU\]** Determina els valors dels paràmetres $a, b \in \mathbb{R}$ perquè la funció $f(x)$ sigui contínua en tot el seu domini: $$f(x) = \begin{cases} a x + 2 & \text{si } x < 1 \\ x^2 + b & \text{si } 1 \le x < 3 \\ \frac{2x + 8}{x - 1} & \text{si } x \ge 3 \end{cases}$$

2.  **\[Model PAU\]** Donada la funció racional $f(x) = \frac{ax^2 + bx - 3}{x + 2}$:

    1.  Troba els valors de $a$ i $b$ sabent que la recta $y = 3x - 1$ és una assímptota oblíqua de $f(x)$.

    2.  Amb els valors obtinguts, estudia la continuïtat de la funció i determina les seves assímptotes verticals.

—

## Resum Final i Errors Habituals

> **📘 Propietat**
>
> Esquema de Resolució d’un Límit 1. **Substitueix el punt.** Si obtens un nombre real, aquest és el resultat. 2. **Si obtens $k/0$:** Fes límits laterals per determinar si és $+\infty$, $-\infty$ o no existeix. 3. **Si és $\left[\frac{0}{0}\right]$:** Factoritza si són polinomis; multiplica pel conjugat si hi ha arrels. 4. **Si és $\left[\frac{\infty}{\infty}\right]$:** Compara els graus dels polinomis. 5. **Si és $[\infty - \infty]$:** Fes comú denominador o multiplica pel conjugat. 6. **Si és $[1^\infty]$:** Utilitza la fórmula basada en el nombre $e$: $e^{\lim g(x)[f(x)-1]}$.

> **⚠️ Alerta**
>
> Top 5 Errors en Exàmens de Batxillerat
>
> 1.  **Escriure la paraula "lim" inapropiadament:** Cal mantenir la notació $\lim_{x \to a}$ en TOTS els passos fins que se substitueix la $x$ pel valor numèric.
>
> 2.  **Confondre $k/0$ amb $0/0$:** $k/0$ dona $\infty$ (cal mirar laterals), mentre que $0/0$ és una indeterminació que cal resoldre algebraicament.
>
> 3.  **Simplificar malament sumes:** En expressions com $\frac{x^2 + 4}{x}$, NO es pot simplificar la $x$ del numerador amb la del denominador. Només es simplifiquen factors que multipliquen a TOTA l’expressió.
>
> 4.  **Oblidar el parèntesi en el conjugat:** Quan multipliquem pel conjugat, cal protegir els polinomis amb parèntesis per no cometre errors de signe.
>
> 5.  **Buscar assímptotes oblíques quan ja hi ha horitzontal:** Si una funció racional té assímptota horitzontal quan $x \to +\infty$, NO té assímptota oblíqua en aquella mateixa branca.

## Solucionari Complet

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
