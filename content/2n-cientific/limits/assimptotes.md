---
title: Assímptotes
curs: 2n
modalitat: cientific
tema: limits
tipus: teoria
---
# Assímptotes

> **Límits i Asímptotes**  
> *Detecció d’asímptotes horitzontals, verticals i obliqües*  
> Anàlisi Matemàtica · Batxillerat / 1r de carrera

L’estudi dels **límits** d’una funció és fonamental per comprendre el seu comportament a l’infinit i als punts de discontinuïtat. Les **asímptotes** són rectes a les quals la gràfica d’una funció s’aproxima indefinidament, i la seva determinació es basa directament en el càlcul de límits.

En aquest document estudiem els tres tipus d’asímptotes i els criteris basats en límits per trobar-les sistemàticament.

> **📘 Definició**
>
> Definició La recta $x = a$ és una **asímptota vertical** (AV) de $f(x)$ si almenys un dels límits laterals és infinit: $$\lim_{x \to a^+} f(x) = \pm\infty \qquad \text{o} \qquad \lim_{x \to a^-} f(x) = \pm\infty$$

**On buscar asímptotes verticals?** Les AV apareixen als punts on la funció **no és contínua** i el denominador s’anu·la.

| ****Pas**** | **Acció**                                                                                                |
|:------------|:---------------------------------------------------------------------------------------------------------|
|             | Troba els punts on el denominador és zero: $D(x) = 0$                                                    |
| **2**       | Comprova que el numerador $N(a) \neq 0$ en aquell punt                                                   |
|             | Calcula els límits laterals: $\displaystyle\lim_{x \to a^+} f(x)$ i $\displaystyle\lim_{x \to a^-} f(x)$ |
| **4**       | Si algun límit lateral és $\pm\infty$, aleshores $x = a$ és una AV                                       |

> **📘 Definició**
>
> Exemple — $f(x) = \dfrac{1}{x^2 - 4}$
>
> - Denominador: $x^2 - 4 = 0 \;\Rightarrow\; x = 2$ i $x = -2$
>
> - Per $x = 2$: $\displaystyle\lim_{x \to 2^+}\frac{1}{x^2-4} = +\infty$i $\displaystyle\lim_{x \to 2^-}\frac{1}{x^2-4} = -\infty$
>
> - Per $x = -2$: $\displaystyle\lim_{x \to -2^+}\frac{1}{x^2-4} = -\infty$i $\displaystyle\lim_{x \to -2^-}\frac{1}{x^2-4} = +\infty$
>
> - **Conclusió:** $x = 2$ i $x = -2$ són asímptotes verticals.

![](img/assimptotes-efcf25.svg)

**Interpretació gràfica:** La funció creix o decreix sense límit quan $x$ s’apropa al valor $a$ per l’esquerra o per la dreta.

**Important:** Un punt on $N(a) = 0$ i $D(a) = 0$ *no necessàriament* és una AV; pot ser un forat (discontinuïtat evitable). Cal simplificar primer.

> **📘 Definició**
>
> Definició La recta $y = L$ és una **asímptota horitzontal** (AH) de $f(x)$ si: $$\lim_{x \to +\infty} f(x) = L \qquad \text{o} \qquad \lim_{x \to -\infty} f(x) = L$$

Una funció pot tenir fins a **dues asímptotes horitzontals** (una per $+\infty$ i una altra per $-\infty$, que poden ser iguals o diferents).

**Regles per a funcions racionals** $f(x) = \dfrac{N(x)}{D(x)}$:

| ****Cas**** | **Condició**        | **Resultat**       | ****AH****        |
|:------------|:--------------------|:-------------------|:------------------|
| **I**       | $\deg(N) < \deg(D)$ | $\lim = 0$         | **$y = 0$**       |
| **II**      | $\deg(N) = \deg(D)$ | $\lim = a_n / b_m$ | **$y = a_n/b_m$** |
| **III**     | $\deg(N) > \deg(D)$ | $\lim = \pm\infty$ | **No hi ha AH**   |

> **📘 Definició**
>
> Exemple — $f(x) = \dfrac{3x^2 + 1}{x^2 - 5}$ $\deg(N) = \deg(D) = 2$, per tant apliquem el Cas II: $$\lim_{x \to \pm\infty} \frac{3x^2 + 1}{x^2 - 5} = \frac{3}{1} = 3$$ **Conclusió:** $y = 3$ és una asímptota horitzontal (vàlida tant per $+\infty$ com per $-\infty$).

![](img/assimptotes-8b5bf4.svg)

**Nota sobre funcions no racionals:**

Per a funcions amb exponencials, logaritmes o arrels, cal calcular directament els límits a $\pm\infty$.

**Exemples:**

- $\displaystyle\lim_{x \to +\infty} e^{-x} = 0\;\Rightarrow\; y = 0$ és AH.

- $\displaystyle\lim_{x \to -\infty} \arctan(x) = -\tfrac{\pi}{2}$ i $\displaystyle\lim_{x \to +\infty} \arctan(x) = \tfrac{\pi}{2}$  
  $\Rightarrow$ Té **dues** AH diferents.

> **📘 Definició**
>
> Definició La recta $y = mx + n$ és una **asímptota obliqua** (AO) de $f(x)$ si (amb $m \neq 0$ i $n$ finit): $$\lim_{x\to\pm\infty}\bigl[f(x) - (mx+n)\bigr] = 0$$

Les asímptotes obliqües **només existeixen quan no hi ha asímptota horitzontal**. Per a funcions racionals, la condició necessària (però no suficient!) és $\deg(N) = \deg(D) + 1$. La condició **suficient** requereix verificar que $m \neq 0$ *i* que $n$ sigui finit.

> **Mètode A — Per límits (càlcul de $m$ i $n$)**
>
> | **Pas** | Càlcul                                                          | Si el resultat és…                                         |
> |:--------|:----------------------------------------------------------------|:-----------------------------------------------------------|
> |         | $m = \displaystyle\lim_{x \to \pm\infty} \dfrac{f(x)}{x}$       | $m = 0 \;\Rightarrow\;$ **no hi ha AO** en aquest sentit   |
> | **2**   | $n = \displaystyle\lim_{x \to \pm\infty} \bigl[f(x) - mx\bigr]$ | $n = \pm\infty \;\Rightarrow\;$ **no hi ha AO**            |
> |         | AO: $y = mx + n$                                                | $m \neq 0$ i $n$ finit $\;\Rightarrow\;$ **AO confirmada** |

> **Mètode B — Divisió euclidiana (polinòmica)**
>
> Per a funcions racionals amb $\deg(N) = \deg(D)+1$, es divideix $N(x)$ entre $D(x)$: $$f(x) = \frac{N(x)}{D(x)} = \underbrace{mx + n}_{\text{quocient}} + \frac{r}{D(x)}$$
>
> - El quocient $mx + n$ és directament l’AO (si $m \neq 0$), perquè $\dfrac{r}{D(x)} \to 0$ quan $x \to \pm\infty$.
>
> - Si el quocient és una constant ($m = 0$), és una AH, no AO.
>
> - Avantatge: és **més ràpid** per a funcions racionals.
>
> - Inconvenient: no funciona per a funcions no racionals.

> **Quan usar cada mètode?** El **Mètode B** (divisió) és més àgil per a funcions racionals senzilles. El **Mètode A** (límits) és imprescindible per a funcions no racionals i és el que demostra formalment l’existència de l’AO. A la PAU s’accepten tots dos.

> **📘 Definició**
>
> Exemple 1 — $f(x) = \dfrac{x^2 + 2x - 1}{x - 1}$(AO existent, dos mètodes)
>
> **Mètode A — Límits:**
>
> - $m = \displaystyle\lim_{x \to \infty} \frac{x^2+2x-1}{x(x-1)} = \lim_{x \to \infty} \frac{x^2+2x-1}{x^2-x} = 1$
>
> - $n = \displaystyle\lim_{x \to \infty} \left[\frac{x^2+2x-1}{x-1} - x\right] = \lim_{x \to \infty} \frac{x^2+2x-1 - x(x-1)}{x-1} = \lim_{x \to \infty} \frac{3x-1}{x-1} = 3$
>
> - $m=1\neq 0$, $n=3$ finit $\;\Rightarrow\;$ **AO: $y = x+3$**
>
> **Mètode B — Divisió euclidiana:** $$x^2 + 2x - 1 \;\div\; (x-1):$$ $$\begin{array}{r@{\;}l}
x^2+2x-1 &= (x-1)\cdot \mathbf{x} + (3x-1) \\
3x - 1   &= (x-1)\cdot \mathbf{3} + 2 \\
\end{array}
\quad\Longrightarrow\quad
f(x) = \underbrace{x + 3}_{\text{AO}} + \frac{2}{x-1}$$ Quocient $= x+3$, residu $= 2$. Com $\dfrac{2}{x-1}\to 0$, confirmem **AO: $y = x+3$**

![](img/assimptotes-0739bf.svg)

**Com fer la divisió euclidiana:**

Dividim $x^2+2x-1$ entre $x-1$ com si fos una divisió de nombres:

1.  Dividim el terme de major grau del dividend pel de major grau del divisor: $x^2 \div x = x$.

2.  Multipliquem: $x \cdot (x-1) = x^2-x$. Restem.

3.  Baixem el següent terme i repetim: $3x \div x = 3$.

4.  Multipliquem: $3\cdot(x-1) = 3x-3$. Restem.

5.  Residu $= 2$ (grau $<$ grau divisor). Aturem.

> **📘 Definició**
>
> Exemple 2 — $g(x) = \dfrac{x^2}{x^2 - 1} \cdot x$$=\dfrac{x^3}{x^2-1}$($m$ surт 0?)  Espera! Aquí $\deg(N)=3$, $\deg(D)=2$, diferència $=1$. Sembla candidata a AO.  **Mètode A:** $$m = \lim_{x \to \infty}\frac{x^3}{x(x^2-1)} = \lim_{x \to \infty}\frac{x^3}{x^3-x} = 1 \neq 0$$ $m=1$. Calculem $n$: $$n = \lim_{x \to \infty}\left[\frac{x^3}{x^2-1} - x\right]
>     = \lim_{x \to \infty}\frac{x^3 - x(x^2-1)}{x^2-1}
>     = \lim_{x \to \infty}\frac{x}{x^2-1} = 0$$ Aquí $m=1\neq 0$ i $n=0$ finit: **AO: $y=x$** (cas on $n=0$, AO passa per l’origen).

**📘 Definició**

Exemple 3 — $h(x) = \dfrac{x^2 + x\sqrt{x}}{x - 1}$($n = \infty$, no hi ha AO!)

$\deg$ del numerador: el terme $x\sqrt{x} = x^{3/2}$ té grau $3/2$, que és el dominant. $\deg$ del denominador: $1$. Diferència $= 1/2$: no és un enter, però analitzem igualment.

**Mètode A:** $$m = \lim_{x \to \infty}\frac{h(x)}{x}
>     = \lim_{x \to \infty}\frac{x^2 + x^{3/2}}{x(x-1)}
>     = \lim_{x \to \infty}\frac{x^2 + x^{3/2}}{x^2-x}
>     = 1 \quad\text{(terme dominant $x^2$)}$$ $$n = \lim_{x \to \infty}\left[h(x) - x\right]
>     = \lim_{x \to \infty}\frac{x^2+x\sqrt{x}-x(x-1)}{x-1}
>     = \lim_{x \to \infty}\frac{x\sqrt{x}+x}{x-1}
>     = \lim_{x \to \infty}\frac{x(\sqrt{x}+1)}{x-1}
>     \;\sim\; \lim_{x \to \infty}\sqrt{x} = +\infty$$ $n = +\infty$ **no és finit** $\;\Rightarrow\;$ **No existeix AO**, malgrat que $m=1$.

**📘 Definició**

Exemple 4 — $p(x) = \dfrac{x^2 + 1}{x^2 - x} \cdot \dfrac{1}{x}$$= \dfrac{x^2+1}{x^3-x^2}$($m=0$, no hi ha AO!)  $\deg(N)=2$, $\deg(D)=3$. Diferència $= -1$: en realitat hi ha AH, però per completesa:  **Mètode A:** $$m = \lim_{x \to \infty}\frac{p(x)}{x}
>     = \lim_{x \to \infty}\frac{x^2+1}{x(x^3-x^2)}
>     = \lim_{x \to \infty}\frac{x^2+1}{x^4-x^3} = 0$$ $m = 0 \;\Rightarrow\;$ **No hi ha AO**. Comprovem si hi ha AH: $$\lim_{x \to \infty} p(x) = \lim_{x \to \infty}\frac{x^2+1}{x^3-x^2} = 0
>   \;\Rightarrow\; \textbf{AH: } y = 0$$

**Exemple més clar amb $\deg(N) = \deg(D)+1$ i $m=0$ impossible:** Per una funció racional, si $\deg(N) = \deg(D)+1$ el coeficient $m$ *mai* pot ser $0$ (seria $m = a_n/b_m \neq 0$). El cas $m=0$ ocorre quan $\deg(N) \leq \deg(D)$, que porta a AH. **Per tant, per a funcions racionals, si $\deg(N)=\deg(D)+1$, sempre existeix l’AO** (llevat que $D(x)$ tingui arrels que facin $n=\pm\infty$ en algun sentit).

**Resum — Quan $\deg(N) = \deg(D)+1$ i NO hi ha AO:**

- **$m = 0$**: impossible per a funcions racionals pures (el quocient dels coeficients dominants sempre és $\neq 0$). Sí possible per a funcions no racionals on la part creixent es cancella.

- **$n = \pm\infty$**: ocorre quan hi ha termes de creixement intermedi (ex. $\sqrt{x}$, $\ln x$, $x^{3/2}$) que fan que la diferència $f(x)-mx$ no convergeixi a cap valor finit.

- En ambdós casos, cal reportar-ho explícitament: “$m = \ldots$, però $n = \pm\infty$, per tant **no existeix AO**”.

| ****Tipus****        | ****Recta****  | **Condició (límit)**                                      | **Quan apareix**           |
|:---------------------|:---------------|:----------------------------------------------------------|:---------------------------|
| **Vertical (AV)**    | **$x = a$**    | $\displaystyle\lim_{x \to a^\pm} f(x) = \pm\infty$        | $D(a) = 0$ i $N(a) \neq 0$ |
| **Horitzontal (AH)** | **$y = L$**    | $\displaystyle\lim_{x \to \pm\infty} f(x) = L$            | $\deg(N) \leq \deg(D)$     |
| **Obliqua (AO)**     | **$y = mx+n$** | $m = \lim f/x$, $n = \lim(f - mx)$ ($m\neq 0$, $n$ finit) | $\deg(N) = \deg(D)+1$      |

**💡 Nota**

**Relació entre asímptotes:** Una funció **no pot tenir alhora** asímptota horitzontal i obliqua en el mateix sentit ($+\infty$ o $-\infty$). L’existència d’AH implica que no hi ha AO en aquell sentit, i viceversa. Sí que és possible tenir AH per un costat i AO per l’altre en funcions no racionals.

Quan el denominador s’anul̇a en $x = a$, cal comprovar si el numerador també ho fa. Aquestes dues situacions donen resultats molt diferents:

|     | **Asímptota Vertical ($x = a$)**                 | **Forat / Discontinuïtat evitable**      |
|:----|:-------------------------------------------------|:-----------------------------------------|
|     | $N(a) \neq 0$ **i** $D(a) = 0$                   | $N(a) = 0$ **i** $D(a) = 0$              |
|     | El límit és $\pm\infty$                          | El límit **existeix** i és finit         |
|     | La funció **no es pot simplificar**              | La funció **es pot simplificar**         |
|     | Gràficament: la corba *escapa* cap a $\pm\infty$ | Gràficament: hi ha un *forat* a la corba |

**📘 Definició**

Cas 1 — Asímptota Vertical $$f(x) = \frac{x - 1}{x^2 - 3x + 2} = \frac{x-1}{(x-1)(x-2)}$$

- $D(x)=0 \;\Rightarrow\; x=1$ i $x=2$

- En $x = 1$: $N(1) = 0$, $D(1) = 0$  
Simplifiquem: $\dfrac{\cancel{(x-1)}}{\cancel{(x-1)}(x-2)} = \dfrac{1}{x-2}$  
$\displaystyle\lim_{x\to 1} f(x) = \frac{1}{1-2} = -1$  
**$\Rightarrow$ Forat a $(1,-1)$. No és AV!**

- En $x = 2$: $N(2) = 1 \neq 0$, $D(2) = 0$  
$\displaystyle\lim_{x\to 2^+} \frac{1}{x-2} = +\infty$  
**$\Rightarrow$ $x = 2$ sí és AV.**

**📘 Definició**

Cas 2 — Forat (discontinuïtat evitable) $$g(x) = \frac{x^2 - 4}{x - 2} = \frac{(x-2)(x+2)}{x-2}$$

- $D(x)=0 \;\Rightarrow\; x = 2$

- $N(2) = 0$ i $D(2) = 0$  
Simplifiquem: $\dfrac{\cancel{(x-2)}(x+2)}{\cancel{(x-2)}} = x + 2$  
$\displaystyle\lim_{x \to 2} g(x) = 2 + 2 = 4$  
**$\Rightarrow$ Forat a $(2,4)$. No és AV!**

- La funció simplificada és $g(x) = x+2$,  
però **amb un forat** en $x = 2$.

![](img/assimptotes-f49e9c.svg)

**💡 Nota**

**Regla pràctica:** Si $N(a) = 0$ i $D(a) = 0$ alhora, **simplifica primer** cancellant el factor comú $(x - a)$. Aleshores:

- Si després de simplificar el denominador **segueix sent $0$** en $x = a$ $\;\Rightarrow\;$ **Asímptota Vertical**.

- Si després de simplificar la funció **és contínua** en $x = a$ $\;\Rightarrow\;$ **Forat (discontinuïtat evitable)**, i el límit val $f_{\text{simpl.}}(a)$.

| ****\#**** | ****Funció****                                | **Resultat**                                            |
|:-----------|:----------------------------------------------|:--------------------------------------------------------|
| **1**      | **$\displaystyle f(x) = \frac{2x+1}{x^2-9}$** | AV: $x=3$ i $x=-3$ AH: $y=0$                            |
| **2**      | **$\displaystyle f(x) = \frac{x^2-1}{x-2}$**  | AV: $x=2$ AO: $y=x+2$                                   |
| **3**      | **$\displaystyle f(x) = \frac{3x^3}{x^3+1}$** | AV: $x=-1$ AH: $y=3$                                    |
| **4**      | **$\displaystyle f(x) = \frac{x^2+x}{2x-4}$** | AV: $x=2$ AO: $y=\tfrac{x}{2}+\tfrac{3}{2}$             |
| **5**      | **$f(x) = \arctan(x^2)$**                     | AH: $y=\tfrac{\pi}{2}$ (per $\pm\infty$) Sense AV ni AO |

***Consell:** Sempre comença buscant les AV (denominador $= 0$), després calcula els límits a l’infinit per determinar si hi ha AH o AO.*

A continuació es resolen detalladament els cinc exercicis proposats a la secció anterior, seguint sempre el mateix ordre: primer les **AV**, després les **AH** o **AO**.

**Exercici 1 $\displaystyle f(x) = \dfrac{2x+1}{x^2-9}$**

**Pas 1 — Asímptotes Verticals**

Igualem el denominador a zero: $$x^2 - 9 = 0 \;\Longrightarrow\; (x-3)(x+3) = 0 \;\Longrightarrow\; x = 3 \text{ i } x = -3$$ Comprovem el numerador: $N(3) = 7 \neq 0$ i $N(-3) = -5 \neq 0$. Cap factor comú $\Rightarrow$ no cal simplificar.

Càlcul dels límits laterals: $$\lim_{x \to 3^+} \frac{2x+1}{(x-3)(x+3)}
>   = \frac{7}{0^+ \cdot 6} = +\infty
>   \qquad
>   \lim_{x \to 3^-} \frac{2x+1}{(x-3)(x+3)}
>   = \frac{7}{0^- \cdot 6} = -\infty$$ $$\lim_{x \to -3^+} \frac{2x+1}{(x-3)(x+3)}
>   = \frac{-5}{(-6) \cdot 0^+} = +\infty
>   \qquad
>   \lim_{x \to -3^-} \frac{2x+1}{(x-3)(x+3)}
>   = \frac{-5}{(-6) \cdot 0^-} = -\infty$$

**Pas 2 — Asímptotes Horitzontals**

$\deg(N) = 1 < \deg(D) = 2$, apliquem el Cas I: $$\lim_{x \to \pm\infty} \frac{2x+1}{x^2-9}
>   = \lim_{x \to \pm\infty} \frac{2/x + 1/x^2}{1 - 9/x^2} = \frac{0}{1} = 0$$

**Resultat:** AV: $x = 3$ i $x = -3$ AH: $y = 0$

**Exercici 2 $\displaystyle f(x) = \dfrac{x^2-1}{x-2}$**

**Pas 1 — Asímptotes Verticals**

Denominador zero: $x - 2 = 0 \;\Rightarrow\; x = 2$. Numerador: $N(2) = 4 - 1 = 3 \neq 0$. No cal simplificar. $$\lim_{x \to 2^+} \frac{x^2-1}{x-2} = \frac{3}{0^+} = +\infty
>   \qquad
>   \lim_{x \to 2^-} \frac{x^2-1}{x-2} = \frac{3}{0^-} = -\infty$$

**Pas 2 — Asímptotes Horitzontals?**

$\deg(N) = 2 > \deg(D) = 1$ (Cas III): el límit és $\pm\infty$. **No hi ha AH.**

**Pas 3 — Asímptota Obliqua**

$$m = \lim_{x \to \infty} \frac{f(x)}{x}
>     = \lim_{x \to \infty} \frac{x^2-1}{x(x-2)}
>     = \lim_{x \to \infty} \frac{x^2 - 1}{x^2 - 2x}
>     = 1$$ $$n = \lim_{x \to \infty} \bigl[f(x) - x\bigr]
>     = \lim_{x \to \infty} \frac{x^2 - 1 - x(x-2)}{x-2}
>     = \lim_{x \to \infty} \frac{2x - 1}{x-2}
>     = 2$$ *Verificació per divisió:* $x^2 - 1 = (x-2)(x+2) + 3$, per tant $f(x) = x + 2 + \dfrac{3}{x-2} \xrightarrow{x\to\infty} x + 2$.

**Resultat:** AV: $x = 2$ AO: $y = x + 2$

**Exercici 3 $\displaystyle f(x) = \dfrac{3x^3}{x^3+1}$**

**Pas 1 — Asímptotes Verticals**

Denominador zero: $x^3 + 1 = 0 \;\Rightarrow\; x = -1$ (arrel real única). Numerador: $N(-1) = 3(-1)^3 = -3 \neq 0$. $$\lim_{x \to -1^+} \frac{3x^3}{x^3+1}
>   = \frac{-3}{0^+} = -\infty
>   \qquad
>   \lim_{x \to -1^-} \frac{3x^3}{x^3+1}
>   = \frac{-3}{0^-} = +\infty$$

**Pas 2 — Asímptotes Horitzontals**

$\deg(N) = \deg(D) = 3$ (Cas II). Dividim pels coeficients dominants: $$\lim_{x \to +\infty} \frac{3x^3}{x^3 + 1}
>   = \lim_{x \to +\infty} \frac{3}{1 + 1/x^3} = 3
>   \qquad
>   \lim_{x \to -\infty} \frac{3x^3}{x^3 + 1}
>   = \frac{3}{1} = 3$$ El límit és el mateix per $\pm\infty$: hi ha **una sola** AH.

**Resultat:** AV: $x = -1$ AH: $y = 3$

**Exercici 4 $\displaystyle f(x) = \dfrac{x^2+x}{2x-4}$**

**Pas 1 — Asímptotes Verticals**

Denominador zero: $2x - 4 = 0 \;\Rightarrow\; x = 2$. Numerador: $N(2) = 4 + 2 = 6 \neq 0$. $$\lim_{x \to 2^+} \frac{x^2+x}{2x-4}
>   = \frac{6}{0^+} = +\infty
>   \qquad
>   \lim_{x \to 2^-} \frac{x^2+x}{2x-4}
>   = \frac{6}{0^-} = -\infty$$

**Pas 2 — Asímptotes Horitzontals?**

$\deg(N) = 2 > \deg(D) = 1$ (Cas III). **No hi ha AH.**

**Pas 3 — Asímptota Obliqua**

$$m = \lim_{x \to \infty} \frac{f(x)}{x}
>     = \lim_{x \to \infty} \frac{x^2 + x}{x(2x-4)}
>     = \lim_{x \to \infty} \frac{x^2 + x}{2x^2 - 4x}
>     = \frac{1}{2}$$ $$n = \lim_{x \to \infty} \left[f(x) - \frac{x}{2}\right]
>     = \lim_{x \to \infty} \frac{x^2 + x - \frac{x}{2}(2x-4)}{2x-4}
>     = \lim_{x \to \infty} \frac{x^2 + x - x^2 + 2x}{2x-4}
>     = \lim_{x \to \infty} \frac{3x}{2x-4}
>     = \frac{3}{2}$$ *Verificació per divisió:* $\dfrac{x^2+x}{2x-4} = \dfrac{x}{2} + \dfrac{3}{2} + \dfrac{6}{2x-4}$, i el residu $\dfrac{6}{2x-4} \to 0$.

**Resultat:** AV: $x = 2$ AO: $y = \dfrac{x}{2} + \dfrac{3}{2}$

**Exercici 5 $f(x) = \arctan(x^2)$**

**Pas 1 — Asímptotes Verticals**

La funció $\arctan$ és contínua a tot $\mathbb{R}$ i $x^2 \geq 0$ per a tot $x$. **No hi ha AV.**

**Pas 2 — Asímptotes Horitzontals**

Quan $x \to +\infty$, $x^2 \to +\infty$: $$\lim_{x \to +\infty} \arctan(x^2) = \frac{\pi}{2}$$ Quan $x \to -\infty$, $x^2 \to +\infty$ (el quadrat sempre és positiu!): $$\lim_{x \to -\infty} \arctan(x^2) = \frac{\pi}{2}$$ Ambdós límits coincideixen: hi ha **una única** AH per als dos sentits.
>
> *Nota:* Cal no confondre amb $\arctan(x)$, on els límits laterals serien $\pm\pi/2$ (dues AH diferents). Aquí la composició amb $x^2$ fa que el comportament sigui simètric.
>
> **Pas 3 — Asímptota Obliqua?**
>
> No pot haver-hi AO si ja existeix AH en el mateix sentit. **No hi ha AO.**
>
> > **Resultat:** Sense AV ni AO AH: $y = \dfrac{\pi}{2}$  (per a $x \to +\infty$ i $x \to -\infty$)

> ***Resum dels resultats:** (1) AV: $x=\pm 3$, AH: $y=0$ (2) AV: $x=2$, AO: $y=x+2$ (3) AV: $x=-1$, AH: $y=3$ (4) AV: $x=2$, AO: $y=\tfrac{x}{2}+\tfrac{3}{2}$ (5) AH: $y=\tfrac{\pi}{2}$*
