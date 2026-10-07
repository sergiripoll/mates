---
title: Probabilitat condicionada: exercici de classe
curs: 2n
modalitat: tots
tema: probabilitat
tipus: exercicis
---
# Probabilitat condicionada: exercici de classe

**La nostra classe de Matemàtiques**  
Un exercici complet de probabilitat condicionada  
2n Batxillerat · Probabilitat

------------------------------------------------------------------------

Tenim una classe de **30 alumnes** dels quals sabem el sexe i si han aprovat o suspès l’últim examen de Matemàtiques. Les dades són les següents:

|               | **Han aprovat** | **Han suspès** | **Total** |     |
|:--------------|:---------------:|:--------------:|:---------:|:---:|
| **Nois**      |       12        |       3        |    15     |     |
| **Noies**     |        6        |       9        |    15     |     |
| ****Total**** |       18        |       12       |  **30**   |     |

Treballarem aquesta taula des de **zero**, construint a poc a poc tots els conceptes. Segueix l’ordre dels apartats.

## Notació i probabilitats bàsiques (Regla de Laplace)

Definim els nostres esdeveniments: $$N = \text{``l'alumne escollit és noi''} \qquad
A = \text{``l'alumne escollit ha aprovat''}$$ i els seus complementaris: $$\overline{N} = \text{``és noia''} \qquad \overline{A} = \text{``ha suspès''}$$

> **📝 Exercici**
>
> Apartat 1 — Probabilitats bàsiques Calcula directament de la taula:
>
> 1.  $P\!\left(N\right)$, $P\!\left(\overline{N}\right)$, $P\!\left(A\right)$, $P\!\left(\overline{A}\right)$
>
> 2.  $P\!\left(N \cap A\right)$, $P\!\left(N \cap \overline{A}\right)$, $P\!\left(\overline{N} \cap A\right)$, $P\!\left(\overline{N} \cap \overline{A}\right)$

<details><summary>Solució</summary>

Apartat 1 **a)** Directament de la taula (Regla de Laplace, total = 30): $$P\!\left(N\right) = \frac{15}{30} = \frac{1}{2} \qquad
P\!\left(\overline{N}\right) = \frac{15}{30} = \frac{1}{2}$$ $$P\!\left(A\right) = \frac{18}{30} = \frac{3}{5} \qquad
P\!\left(\overline{A}\right) = \frac{12}{30} = \frac{2}{5}$$

**b)** Les interseccions corresponen a cada cel·la de la taula:

|                           |                          **$A$ (aprovat)**                           |                           **$\overline{A}$ (suspès)**                            |
|:--------------------------|:--------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| **$N$ (noi)**             |      $P\!\left(N \cap A\right) = \dfrac{12}{30} = \dfrac{2}{5}$      |      $P\!\left(N \cap \overline{A}\right) = \dfrac{3}{30} = \dfrac{1}{10}$       |
| **$\overline{N}$ (noia)** | $P\!\left(\overline{N} \cap A\right) = \dfrac{6}{30} = \dfrac{1}{5}$ | $P\!\left(\overline{N} \cap \overline{A}\right) = \dfrac{9}{30} = \dfrac{3}{10}$ |

**Comprovació:** La suma de les quatre interseccions ha de ser 1: $\dfrac{2}{5} + \dfrac{1}{10} + \dfrac{1}{5} + \dfrac{3}{10} = \dfrac{4+1+2+3}{10} = \dfrac{10}{10} = 1$

</details>

## Probabilitat condicionada

> **📘 Teoria**
>
> La probabilitat condicionada $P\!\left(A \mid B\right)$ respon a la pregunta: *“Si ja sé que ha passat $B$, quina és la probabilitat que passi $A$?”* $$P\!\left(A \mid B\right) = \frac{P\!\left(A \cap B\right)}{P\!\left(B\right)}$$ En termes pràctics: **restringim** l’espai mostral al grup $B$ i comptem dins d’ell.

> **📝 Exercici**
>
> Apartat 2 — Probabilitat condicionada
>
> 1.  Calcula $P\!\left(A \mid N\right)$: probabilitat d’haver aprovat, **sabent que és noi**.
>
> 2.  Calcula $P\!\left(A \mid \overline{N}\right)$: probabilitat d’haver aprovat, **sabent que és noia**.
>
> 3.  Calcula $P\!\left(N \mid A\right)$: probabilitat que sigui noi, **sabent que ha aprovat**.
>
> 4.  Calcula $P\!\left(N \mid \overline{A}\right)$: probabilitat que sigui noi, **sabent que ha suspès**.

<details><summary>Solució</summary>

Apartat 2

**a)** Ens quedem *només* amb els 15 nois i mirem quants han aprovat: $$P\!\left(A \mid N\right) = \frac{P\!\left(A \cap N\right)}{P\!\left(N\right)} = \frac{12/30}{15/30} = \frac{12}{15} = \boxed{\frac{4}{5}}$$ *Interpretació: el 80% dels nois ha aprovat.*

**b)** Ens quedem *només* amb les 15 noies: $$P\!\left(A \mid \overline{N}\right) = \frac{P\!\left(A \cap \overline{N}\right)}{P\!\left(\overline{N}\right)} = \frac{6/30}{15/30} = \frac{6}{15} = \boxed{\frac{2}{5}}$$ *Interpretació: només el 40% de les noies ha aprovat.*

**c)** Ara ens quedem *només* amb els 18 alumnes que han aprovat: $$P\!\left(N \mid A\right) = \frac{P\!\left(N \cap A\right)}{P\!\left(A\right)} = \frac{12/30}{18/30} = \frac{12}{18} = \boxed{\frac{2}{3}}$$ *Interpretació: 2 de cada 3 alumnes que han aprovat són nois.*

**d)** Ens quedem *només* amb els 12 alumnes que han suspès: $$P\!\left(N \mid \overline{A}\right) = \frac{P\!\left(N \cap \overline{A}\right)}{P\!\left(\overline{A}\right)} = \frac{3/30}{12/30} = \frac{3}{12} = \boxed{\frac{1}{4}}$$ *Interpretació: entre els suspesos, només 1 de cada 4 és noi.*

</details>

> **⚠️ Atenció**
>
> Fixeu-vos que $P\!\left(A \mid N\right) \neq P\!\left(N \mid A\right)$. Aquestes dues probabilitats **no són el mateix**:
>
> - $P\!\left(A \mid N\right) = \dfrac{4}{5}$: probabilitat d’aprovar *si ets noi*.
>
> - $P\!\left(N \mid A\right) = \dfrac{2}{3}$: probabilitat de ser noi *si has aprovat*.
>
> Canviar l’ordre de les condicions canvia completament el resultat!

## La regla del producte i el diagrama d’arbre

> **📘 Teoria**
>
> De la fórmula de la probabilitat condicionada s’obté la **regla del producte**: $$P\!\left(A \cap B\right) = P\!\left(B\right) \cdot P\!\left(A \mid B\right)$$ Això és la base del **diagrama d’arbre**: cada branca terminal té probabilitat igual al *producte de totes les branques del camí*.

Construïm el diagrama d’arbre per a la nostra classe. La primera bifurcació és el sexe, la segona és si ha aprovat o no:

![](img/probabilitat-condicionada-classe-9ba1ee.svg)

> **📝 Exercici**
>
> Apartat 3 — Regla del producte Usa l’arbre per calcular les quatre probabilitats de les branques terminals i comprova que sumen 1.

<details><summary>Solució</summary>

Apartat 3 Multipliquem les probabilitats de cada camí:

| **Branca terminal**                              | **Càlcul**                         |      **Fracció**      | **Alumnes** |
|:-------------------------------------------------|:-----------------------------------|:---------------------:|:-----------:|
| $P\!\left(N \cap A\right)$                       | $\dfrac{1}{2} \times \dfrac{4}{5}$ |    $\dfrac{2}{5}$     |     12      |
| $P\!\left(N \cap \overline{A}\right)$            | $\dfrac{1}{2} \times \dfrac{1}{5}$ |    $\dfrac{1}{10}$    |      3      |
| $P\!\left(\overline{N} \cap A\right)$            | $\dfrac{1}{2} \times \dfrac{2}{5}$ |    $\dfrac{1}{5}$     |      6      |
| $P\!\left(\overline{N} \cap \overline{A}\right)$ | $\dfrac{1}{2} \times \dfrac{3}{5}$ |    $\dfrac{3}{10}$    |      9      |
| **Suma**                                         |                                    | $\dfrac{4+1+2+3}{10}$ |     30      |

La suma és $\dfrac{10}{10} = 1$ i recuperem exactament la taula inicial.

</details>

## Teorema de la probabilitat total

> **📝 Exercici**
>
> Apartat 4 — Probabilitat total Sense mirar la taula directament, calcula $P\!\left(A\right)$ (probabilitat d’aprovar) usant el teorema de la probabilitat total a partir de l’arbre.

<details><summary>Solució</summary>

Apartat 4 Les dues “vies” per arribar a $A$ (aprovar) són: passant per $N$ (noi) o per $\overline{N}$ (noia). Sumem les dues branques terminals que acaben en aprovat: $$P\!\left(A\right) = P\!\left(N\right) \cdot P\!\left(A \mid N\right) \;+\; P\!\left(\overline{N}\right) \cdot P\!\left(A \mid \overline{N}\right)$$ $$P\!\left(A\right) = \frac{1}{2} \cdot \frac{4}{5} \;+\; \frac{1}{2} \cdot \frac{2}{5}
= \frac{2}{5} + \frac{1}{5} = \boxed{\frac{3}{5}}$$ *Coincideix exactament amb el que llegim directament a la taula: $18/30 = 3/5$.*

</details>

## Independència d’esdeveniments

> **📘 Teoria**
>
> $A$ i $B$ són **independents** si saber que ha passat $B$ *no canvia* la probabilitat de $A$: $$A \perp B \iff P\!\left(A \mid B\right) = P\!\left(A\right) \iff P\!\left(A \cap B\right) = P\!\left(A\right) \cdot P\!\left(B\right)$$ Qualsevol de les tres condicions és equivalent. N’hi ha prou de comprovar-ne una.

> **📝 Exercici**
>
> Apartat 5 — Independència Són independents el sexe i el fet d’aprovar? És a dir, **el ser noi o noia influeix en la probabilitat d’aprovar?** Comprova-ho de dues maneres.

<details><summary>Solució</summary>

Apartat 5

**Mètode 1 — Comparant probabilitats condicionades amb la global:**

Si fossin independents, hauria de complir-se que $P\!\left(A \mid N\right) = P\!\left(A\right)$: $$P\!\left(A \mid N\right) = \frac{4}{5} = 0{,}8 \qquad \text{vs} \qquad P\!\left(A\right) = \frac{3}{5} = 0{,}6$$ Com que $\dfrac{4}{5} \neq \dfrac{3}{5}$, **no són independents**.

**Mètode 2 — Comprovant si $P\!\left(N \cap A\right) = P\!\left(N\right) \cdot P\!\left(A\right)$:** $$P\!\left(N\right) \cdot P\!\left(A\right) = \frac{1}{2} \cdot \frac{3}{5} = \frac{3}{10} \qquad \text{vs} \qquad P\!\left(N \cap A\right) = \frac{12}{30} = \frac{2}{5} = \frac{4}{10}$$ Com que $\dfrac{3}{10} \neq \dfrac{4}{10}$, confirmem que **no són independents**.

**Interpretació:** El sexe *sí* que influeix en la probabilitat d’aprovar. Els nois aproven més (80%) que la mitjana de la classe (60%), mentre que les noies aproven menys (40%). Tenir informació sobre el sexe *canvia* la nostra predicció sobre si l’alumne ha aprovat.

</details>

## Complementaris i unions

> **📝 Exercici**
>
> Apartat 6 — Complementaris i unions
>
> 1.  Calcula $P\!\left(N \cup A\right)$: probabilitat que l’alumne sigui noi **o** hagi aprovat (o les dues coses).
>
> 2.  Calcula $P\!\left(\overline{N \cup A}\right)$: probabilitat que **no** sigui noi **i** tampoc hagi aprovat.
>
> 3.  Comprova que l’apartat b) coincideix amb $P\!\left(\overline{N} \cap \overline{A}\right)$ de la taula.

<details><summary>Solució</summary>

Apartat 6 **a)** Fórmula de la unió: $$P\!\left(N \cup A\right) = P\!\left(N\right) + P\!\left(A\right) - P\!\left(N \cap A\right)
= \frac{1}{2} + \frac{3}{5} - \frac{2}{5}
= \frac{5}{10} + \frac{6}{10} - \frac{4}{10} = \boxed{\frac{7}{10}}$$ *El 70% dels alumnes és noi o ha aprovat (o les dues coses).*

**b)** Pel complementari de la unió (llei de De Morgan: $\overline{N \cup A} = \overline{N} \cap \overline{A}$): $$P\!\left(\overline{N \cup A}\right) = 1 - P\!\left(N \cup A\right) = 1 - \frac{7}{10} = \boxed{\frac{3}{10}}$$

**c)** De la taula: les alumnes que *no* són nois i han *suspès* (noies suspeses) són 9: $$P\!\left(\overline{N} \cap \overline{A}\right) = \frac{9}{30} = \frac{3}{10} \checkmark$$

</details>

## Resum visual de tots els resultats

| **Probabilitat**                                                     |   **Fracció**   | **Decimal** |
|:---------------------------------------------------------------------|:---------------:|:-----------:|
| $P\!\left(N\right)$ (ser noi)                                        | $\dfrac{1}{2}$  |   $0{,}5$   |
| $P\!\left(A\right)$ (aprovar)                                        | $\dfrac{3}{5}$  |   $0{,}6$   |
| $P\!\left(N \cap A\right)$ (noi i aprovat)                           | $\dfrac{2}{5}$  |   $0{,}4$   |
| $P\!\left(N \cup A\right)$ (noi o aprovat)                           | $\dfrac{7}{10}$ |   $0{,}7$   |
| $P\!\left(A \mid N\right)$ (aprovar sabent que és noi)               | $\dfrac{4}{5}$  |   $0{,}8$   |
| $P\!\left(A \mid \overline{N}\right)$ (aprovar sabent que és noia)   | $\dfrac{2}{5}$  |   $0{,}4$   |
| $P\!\left(N \mid A\right)$ (ser noi sabent que ha aprovat)           | $\dfrac{2}{3}$  |  $0{,}667$  |
| $P\!\left(N \mid \overline{A}\right)$ (ser noi sabent que ha suspès) | $\dfrac{1}{4}$  |  $0{,}25$   |
|                                                                      |                 |             |

## Exercicis addicionals

> **📝 Exercici**
>
> Extra 1 Escollim un alumne a l’atzar. Sabem que **ha suspès**. Quina és la probabilitat que sigui noia?

<details><summary>Solució</summary>

Extra 1 $$P\!\left(\overline{N} \mid \overline{A}\right) = \frac{P\!\left(\overline{N} \cap \overline{A}\right)}{P\!\left(\overline{A}\right)}
= \frac{9/30}{12/30} = \frac{9}{12} = \boxed{\frac{3}{4}}$$ El 75% dels alumnes suspesos són noies.

</details>

> **📝 Exercici**
>
> Extra 2 Construeix l’arbre en ordre invers: primer la bifurcació **aprovat/suspès**, i després **noi/noia**. Calcula $P\!\left(N\right)$ usant el teorema de la probabilitat total i comprova que segueix sent $\dfrac{1}{2}$.

<details><summary>Solució</summary>

Extra 2 Les dades per a aquest arbre invers: $$P\!\left(A\right) = \frac{3}{5}, \quad P\!\left(\overline{A}\right) = \frac{2}{5}, \quad
P\!\left(N \mid A\right) = \frac{2}{3}, \quad P\!\left(N \mid \overline{A}\right) = \frac{1}{4}$$ $$P\!\left(N\right) = P\!\left(A\right) \cdot P\!\left(N \mid A\right) + P\!\left(\overline{A}\right) \cdot P\!\left(N \mid \overline{A}\right)
= \frac{3}{5} \cdot \frac{2}{3} + \frac{2}{5} \cdot \frac{1}{4}
= \frac{2}{5} + \frac{1}{10} = \frac{4}{10} + \frac{1}{10} = \boxed{\frac{1}{2}} \checkmark$$ *L’ordre de l’arbre no importa: el resultat final és sempre el mateix.*

</details>

> **📝 Exercici**
>
> Extra 3 — Difícil Si triem **dos alumnes a l’atzar** (sense reposició), quina és la probabilitat que tots dos hagin aprovat?

<details><summary>Solució</summary>

Extra 3 Aquí intervé la probabilitat condicionada per la reposició. El primer alumne s’escull entre 30 i el segon entre els 29 restants: $$P\!\left(A_1 \cap A_2\right) = P\!\left(A_1\right) \cdot P\!\left(A_2 \mid A_1\right)
= \frac{18}{30} \cdot \frac{17}{29}
= \frac{18 \times 17}{30 \times 29} = \frac{306}{870} = \boxed{\frac{51}{145} \approx 0{,}352}$$ *Si haguéssim considerat les dues eleccions independents (amb reposició), el resultat seria $\left(\dfrac{3}{5}\right)^2 = \dfrac{9}{25} = 0{,}36$, molt proper però no igual.*

</details>

> **💡 Connexió**
>
> **Tots els conceptes que hem treballat amb un sol exemple:**
>
> lp9cm **Laplace** & Probabilitats bàsiques directament de la taula  
> **Intersecció** $P\!\left(A \cap B\right)$ & Cada cel·la de la taula  
> **Unió** $P\!\left(A \cup B\right)$ & Suma de files/columnes menys la intersecció  
> **Complementari** & Canviar de fila/columna o restar d’1  
> **Prob. condicionada** & Restringir l’espai mostral a una fila o columna  
> **Regla del producte** & Multiplicar les branques de l’arbre  
> **Prob. total** & Sumar les branques que arriben al mateix resultat  
> **Independència** & Comprovar si condicionar canvia o no la probabilitat  

------------------------------------------------------------------------

## Reflexió: i si una alumna es declara no binària?

Suposem que una de les 15 alumnes classificades com a “noia” ens diu que **no s’identifica ni com a noi ni com a noia**. Aquesta situació té conseqüències matemàtiques concretes que val la pena entendre.

> **El canvi fonamental: el complementari ja no funciona igual**
>
> Amb **dues categories** (noi / noia), teníem: $$\overline{N} = \text{``no és noi''} = \text{``és noia''} \qquad \Rightarrow \qquad P\!\left(\overline{N}\right) = 1 - P\!\left(N\right)$$ Això funcionava perquè les dues categories eren *exhaustives* (o ets noi o ets noia, no hi havia més opcions) i *excloents* (no podies ser les dues coses).
>
> Ara, amb una persona no binària ($NB$), tenim **tres categories**: $$N = \text{``noi''} \qquad \overline{N} = \text{``no és noi''} = \text{noia \textbf{o} no binari}$$ El complementari $\overline{N}$ ara **agrupa dues coses diferents**. Si ens interessa distingir-les, hem d’usar tres esdeveniments separats: $$N, \quad F \;(\text{noia}), \quad NB \;(\text{no binari})$$ i llavors: $P\!\left(N\right) + P\!\left(F\right) + P\!\left(NB\right) = 1$, però **cap dels tres és el complementari de l’altre**.

### La nova taula (suposem que l’alumna NB va aprovar)

Suposem que l’alumna no binària havia aprovat. Llavors la taula original canvia així:

|               | **Han aprovat** | **Han suspès** | **Total** |     |
|:--------------|:---------------:|:--------------:|:---------:|:---:|
| **Nois**      |       12        |       3        |    15     |     |
| **Noies**     |        5        |       9        |    14     |     |
| **No binari** |        1        |       0        |     1     |     |
| ****Total**** |       18        |       12       |  **30**   |     |

Fixeu-vos que el **total d’aprovats i suspesos no canvia** (segueix sent 18 i 12), però la distribució per gènere sí.

### Què canvia i què no canvia?

| **Probabilitat**                                        |            **Abans**            |             **Ara**              | **Canvia?** |
|:--------------------------------------------------------|:-------------------------------:|:--------------------------------:|:------------|
| $P\!\left(A\right)$ (aprovar)                           | $\dfrac{18}{30} = \dfrac{3}{5}$ | $\dfrac{18}{30} = \dfrac{3}{5}$  | **NO**      |
| $P\!\left(N\right)$ (ser noi)                           | $\dfrac{15}{30} = \dfrac{1}{2}$ | $\dfrac{15}{30} = \dfrac{1}{2}$  | **NO**      |
| $P\!\left(F\right)$ (ser noia)                          | $\dfrac{15}{30} = \dfrac{1}{2}$ | $\dfrac{14}{30} = \dfrac{7}{15}$ | **SÍ**      |
| $P\!\left(\overline{N}\right)$ (“no noi”)               | $\dfrac{15}{30} = \dfrac{1}{2}$ | $\dfrac{15}{30} = \dfrac{1}{2}$  | **NO**      |
| $P\!\left(A \mid N\right)$ (ap. si noi)                 | $\dfrac{12}{15} = \dfrac{4}{5}$ | $\dfrac{12}{15} = \dfrac{4}{5}$  | **NO**      |
| $P\!\left(A \mid F\right)$ (ap. si noia)                | $\dfrac{6}{15} = \dfrac{2}{5}$  |         $\dfrac{5}{14}$          | **SÍ**      |
| $P\!\left(A \mid \overline{N}\right)$ (ap. si “no noi”) | $\dfrac{6}{15} = \dfrac{2}{5}$  |  $\dfrac{6}{15} = \dfrac{2}{5}$  | **NO**$^*$  |
| $P\!\left(NB\right)$ (ser no binari)                    |                —                |         $\dfrac{1}{30}$          | *nova*      |
| $P\!\left(A \mid NB\right)$ (ap. si NB)                 |                —                |        $\dfrac{1}{1} = 1$        | *nova*      |

$^*$Perquè $\overline{N}$ ara inclou la persona NB (que ha aprovat) i una noia menys (que hauria aprovat). En aquest cas concret, la probabilitat condicionada no canvia, però això **depèn dels números concrets** del problema, no és sempre així.

> **La lliçó matemàtica: sistema complet d’esdeveniments**
>
> Quan tenim **més de dues categories**, hem de treballar amb un **sistema complet d’esdeveniments**: un conjunt de categories que:
>
> - Són **mútuament excloents**: ningú pertany a dues categories alhora.
>
> - Són **exhaustives**: tothom pertany a alguna categoria.
>
> Amb dues categories: $\{N, \overline{N}\}$ és un sistema complet. Podem usar el complementari lliurement.
>
> Amb tres categories: $\{N, F, NB\}$ és el sistema complet. Ara: $$P\!\left(N\right) + P\!\left(F\right) + P\!\left(NB\right) = 1$$ $$P\!\left(A\right) = P\!\left(N\right)\cdot P\!\left(A \mid N\right) + P\!\left(F\right)\cdot P\!\left(A \mid F\right) + P\!\left(NB\right)\cdot P\!\left(A \mid NB\right)$$
>
> El teorema de la probabilitat total i el teorema de Bayes **funcionen igual**, simplement sumem **tantes branques com categories tinguem**.
>
> **Resum pràctic:**
>
> - Si treballes amb $\overline{N}$ (“no noi”), inclous la persona NB dins $\overline{N}$: **tot funciona igual**.
>
> - Si vols tractar NB com a categoria pròpia, **cal afegir una branca més** a l’arbre i una fila més a la taula.
>
> - En cap cas es “trenca” la matemàtica: simplement el model s’adapta a la realitat.

### Com quedaria l’arbre amb tres categories?

![](img/probabilitat-condicionada-classe-dced1e.svg)

**Comprovació final** — probabilitat total d’aprovar amb tres categories: $$P\!\left(A\right) = \frac{15}{30}\cdot\frac{4}{5} + \frac{14}{30}\cdot\frac{5}{14} + \frac{1}{30}\cdot 1
= \frac{12}{30} + \frac{5}{30} + \frac{1}{30} = \frac{18}{30} = \frac{3}{5} \checkmark$$
