---
title: Probabilitat: Selectivitat
tematitol: Probabilitat
curs: 2n
modalitat: cientific
tema: probabilitat
bloc: selectivitat
ordre: 3
---
# Probabilitat: Selectivitat

## Probabilitat (problemes tipus examen)

### El repte ocult: definir correctament l’espai mostral

En tots els problemes anteriors l’espai mostral era evident. Però en molts problemes reals, la dificultat principal **no és aplicar cap fórmula**: és decidir quins elements formen $\Omega$ i quants en són. Un error en aquesta decisió fa que tot el problema sigui incorrecte, fins i tot si la resta dels càlculs és perfecta.

> **La pregunta que t’has de fer SEMPRE abans de res**
>
> ![](img/probabilitat-2683f0.svg)
>
> **Regla d’or:** Si pots posar etiquetes distintes a tots els elements (persona A, persona B…; dau 1, dau 2…), l’espai mostral és **ordenat**. Si les etiquetes no importa (un grup de tres persones, una mà de cartes), és **no ordenat**.

#### Cas 1: Lletres repetides — el mateix objecte pot ser distint

> **✏️ Exemple**
>
> La paraula MATEMÀTICA Escrivim en targetes individuals les 10 lletres de la paraula MATEMÀTICA i les posem en una bossa:
>
> ![](img/probabilitat-9eaad4.svg)
>
> **Cada targeta és un element distint** encara que tingui la mateixa lletra: hi ha 3 targetes “A” (posicions 2, 6, 10), 2 targetes “M” (posicions 1, 5), 2 targetes “T” (posicions 3, 7).
>
> Treiem **una** targeta a l’atzar. Calcula:
>
> **a)** $P\!\left(\text{lletra A}\right)$ **b)** $P\!\left(\text{lletra M}\right)$ **c)** $P\!\left(\text{vocal}\right)$
>
> **Espai mostral:** $n(\Omega) = 10$ targetes, totes equiprobables.
>
> **a)** Hi ha 3 targetes amb A: $P\!\left(A\right) = \dfrac{3}{10}$
>
> **b)** Hi ha 2 targetes amb M: $P\!\left(M\right) = \dfrac{2}{10} = \dfrac{1}{5}$
>
> **c)** Vocals: A(×3), E(×1), I(×1) $\Rightarrow$ 5 targetes: $P\!\left(\text{vocal}\right) = \dfrac{5}{10} = \dfrac{1}{2}$
>
> Ara treiem **dues** targetes (sense reposició). Calcula $P\!\left(\text{les dues són A}\right)$.
>
> **Espai mostral:** $n(\Omega) = \dbinom{10}{2} = 45$ parelles de targetes.
>
> **Casos favorables:** Triar 2 de les 3 targetes “A”: $\dbinom{3}{2} = 3$ $$P\!\left(\text{dues A}\right) = \frac{3}{45} = \boxed{\frac{1}{15}}$$
>
> > **⚠️ Atenció**
> >
> > Si hagués dit “triem 2 **lletres** de l’alfabet de MATEMÀTICA”, l’espai mostral tindria només **6 lletres distintes** $\{M, A, T, E, I, C\}$ i $P\!\left(\text{dues A}\right) = 0$ perquè A apareix una sola vegada. **Targetes físiques $\neq$ lletres de l’alfabet.**

#### Cas 2: Ordre importa vs. ordre no importa — comitès i càrrecs

> **✏️ Exemple**
>
> Comitè o càrrecs? L’espai mostral canvia radicalment Tenim 5 homes i 4 dones (9 persones en total). Volem triar 3 persones.
>
> **Situació A — Comitè sense càrrecs** (un grup de 3): $$n(\Omega) = \binom{9}{3} = \frac{9!}{3!\cdot 6!} = \mathbf{84} \text{ grups}$$
>
> **Situació B — Comitè amb càrrecs** (president, vicepresident, secretari): $$n(\Omega) = V_9^3 = 9 \cdot 8 \cdot 7 = \mathbf{504} \text{ trios ordenats}$$
>
> L’error típic és usar 504 quan el problema diu “grup de 3” i 84 quan diu “càrrecs”. **La paraula clau és si les persones triades tenen rols diferenciats.**
>
> **Amb l’espai mostral A (84):**
>
> **a)** $P\!\left(\text{exactament 2 dones}\right) = \dfrac{\binom{4}{2}\cdot\binom{5}{1}}{84} = \dfrac{6 \cdot 5}{84} = \dfrac{30}{84} = \boxed{\dfrac{5}{14}}$
>
> **b)** $P\!\left(\text{almenys 1 home}\right) = 1 - P\!\left(\text{cap home}\right) = 1 - \dfrac{\binom{4}{3}}{84} = 1 - \dfrac{4}{84} = \boxed{\dfrac{20}{21}}$
>
> **Amb l’espai mostral B (504):**
>
> **c)** $P\!\left(\text{presidenta és dona}\right) = \dfrac{4 \cdot 8 \cdot 7}{504} = \dfrac{224}{504} = \boxed{\dfrac{4}{9}}$
>
> *El càlcul de c) fixa el 1r lloc (presidenta: 4 opcions) i deixa els 2 restants lliures (8 i 7 opcions).*

#### Cas 3: Daus — cada dau és distint encara que no ho sembli

> **✏️ Exemple**
>
> Dos daus: per què l’espai mostral té 36 i no 21 elements? Llencem dos daus iguals. Un alumne podria argumentar: “els daus són iguals, (1,2) i (2,1) és el mateix” i usar un espai de $\binom{6}{2} + 6 = \mathbf{21}$ resultats (parelles no ordenades).
>
> **Per què és incorrecte?** Perquè els dos daus, tot i ser físicament iguals, **es poden distingir**: un és el dau de l’esquerra i l’altre el de la dreta. El resultat (1,2) i el resultat (2,1) són esdeveniments **físicament distints** que ocorren amb la mateixa probabilitat. Si usem 21 elements, aquests no serien equiprobables!
>
> p5cm p5.5cm c **Espai mostral** & **Casos amb suma = 7** & **P(suma = 7)**  
> Correcte: 36 parelles ordenades $(d_1, d_2)$ & (1,6) (2,5) (3,4) (4,3) (5,2) (6,1) → **6 casos** & $\dfrac{6}{36} = \dfrac{1}{6}$  
> Incorrecte: 21 parelles no ordenades $\{d_1,d_2\}$ & {1,6} {2,5} {3,4} → **3 casos** & $\dfrac{3}{21} = \dfrac{1}{7}$  
>
> El resultat és diferent! La probabilitat correcta és $\dfrac{1}{6}$. L’espai de 21 dóna un resultat erroni perquè els elements **no són equiprobables**: $\{1,2\}$ pot sortir de 2 maneres (dau1=1,dau2=2 o dau1=2,dau2=1) però $\{1,1\}$ només d’1 manera.
>
> **Regla:** Quan els objectes físics es poden distingir (fins i tot si semblen idèntics), l’espai mostral és **ordenat**.

#### Exercicis: defineix primer l’espai mostral

> **📝 Exercici**
>
> 13 — Baralla espanyola de 40 cartes D’una baralla espanyola de 40 cartes (4 pals de 10 cartes cadascun: as, 2, 3, 4, 5, 6, 7, sota, cavall i rei) traiem **2 cartes** sense reposició. Abans de calcular cap probabilitat, **justifica quin és l’espai mostral i quants elements té**. Després calcula:
>
> 1.  $P\!\left(\text{les dues cartes són del mateix pal}\right)$
>
> 2.  $P\!\left(\text{almenys una figura (sota, cavall o rei)}\right)$
>
> 3.  $P\!\left(\text{les dues cartes sumen exactament 5}\right)$ (as val 1, figures no sumen)

<details><summary>Solució</summary>

**Espai mostral:** Traiem 2 cartes d’un conjunt de 40. L’ordre **no importa** (no diem “primera” i “segona” carta, sinó una “mà” de 2). Les cartes **sí** es poden distingir (cada carta és única). Per tant: $$n(\Omega) = \binom{40}{2} = \frac{40 \cdot 39}{2} = \mathbf{780} \text{ parelles}$$

**a)** Mateix pal: triem 1 pal de 4 i 2 cartes de les 10 d’aquell pal. $$\text{favorables} = \binom{4}{1}\cdot\binom{10}{2} = 4 \cdot 45 = 180
\qquad\Rightarrow\qquad P\!\left(\right) = \frac{180}{780} = \boxed{\frac{3}{13}}$$

**b)** Complementari — cap figura. Hi ha $4\times3 = 12$ figures i $40-12=28$ no-figures. $$P\!\left(\text{cap figura}\right) = \frac{\binom{28}{2}}{780} = \frac{378}{780}
\qquad\Rightarrow\qquad P\!\left(\text{almenys una}\right) = 1 - \frac{378}{780} = \frac{402}{780} = \boxed{\frac{67}{130}}$$

**c)** Suma 5: les parelles de valors que sumen 5 són $(1,4)$ i $(2,3)$. Cada valor apareix en 4 pals: $$\text{favorables} = \underbrace{4\cdot 4}_{(1,4)} + \underbrace{4\cdot 4}_{(2,3)} = 32
\qquad\Rightarrow\qquad P\!\left(\right) = \frac{32}{780} = \boxed{\frac{8}{195}}$$

</details>

> **📝 Exercici**
>
> 14 — Grup o càrrecs: comitè de professors Un departament té 5 professors i 4 professores. Es trien 3 persones. Per a cadascun dels dos enunciats següents, **justifica primer quin és l’espai mostral** i calcula la probabilitat demanada:
>
> 1.  S’escull un **grup de 3** per assistir a una reunió. Quina és la probabilitat que el grup tingui exactament 2 professores?
>
> 2.  S’escull un **coordinador, un sots-coordinador i un secretari**. Quina és la probabilitat que el coordinador sigui una professora?

<details><summary>Solució</summary>

**a) Grup** → ordre NO importa → $n(\Omega) = \dbinom{9}{3} = 84$

$$P\!\left(\text{2 professores}\right) = \frac{\binom{4}{2}\cdot\binom{5}{1}}{84} = \frac{6\cdot 5}{84} = \frac{30}{84} = \boxed{\frac{5}{14} \approx 35{,}7\%}$$

**b) Càrrecs** → ordre SÍ importa (coordinador $\neq$ secretari) → $n(\Omega) = V_9^3 = 9\cdot 8\cdot 7 = 504$

El coordinador és una de les 4 professores; els altres 2 càrrecs s’omplen amb qualsevol de les 8 persones restants i 7: $$P\!\left(\text{coordinadora}\right) = \frac{4\cdot 8\cdot 7}{504} = \frac{224}{504} = \boxed{\frac{4}{9} \approx 44{,}4\%}$$

*Nota: $\frac{4}{9}$ coincideix exactament amb la proporció de professores ($\frac{4}{9}$ del total), cosa que té sentit: cada persona té la mateixa probabilitat de sortir com a coordinadora.*

</details>

> **📝 Exercici**
>
> 15 — PAU: Tres extractors d’una urna Una urna conté 4 boles blanques i 6 boles negres. Tres persones, $X$, $Y$ i $Z$, treuen una bola cadascuna **sense reposició**, en aquest ordre. **Defineix l’espai mostral** i calcula:
>
> 1.  La probabilitat que les tres boles siguin del mateix color.
>
> 2.  La probabilitat que la tercera persona ($Z$) tregui una bola blanca.
>
> 3.  Sabent que $X$ i $Y$ han tret boles del **mateix color**, quina és la probabilitat que $Z$ tregui una bola blanca?

<details><summary>Solució</summary>

**Espai mostral:** Les tres persones treuen boles en ordre i sense reposició. L’ordre **importa** ($X$ treu primer, $Z$ últim). Com que les boles del mateix color **no** es distingeixen entre elles, comptem seqüències de colors: $$n(\Omega) = 10 \cdot 9 \cdot 8 = 720 \quad \text{(boles distingibles per posició)}$$ O equivalentment, usem probabilitats condicionades directament.

**a)** Tres boles del mateix color: $$\begin{aligned}
P\!\left(\text{3 blanques}\right) &= \frac{4}{10}\cdot\frac{3}{9}\cdot\frac{2}{8} = \frac{24}{720} = \frac{1}{30}\\[4pt]
P\!\left(\text{3 negres}\right)   &= \frac{6}{10}\cdot\frac{5}{9}\cdot\frac{4}{8} = \frac{120}{720} = \frac{1}{6}\\[4pt]
P\!\left(\text{3 iguals}\right)   &= \frac{1}{30} + \frac{1}{6} = \frac{1}{30} + \frac{5}{30} = \boxed{\frac{6}{30} = \frac{1}{5}}
\end{aligned}$$

**b)** Per simetria, la posició d’extracció no afecta la probabilitat marginal: $$P\!\left(Z \text{ treu blanca}\right) = \frac{4}{10} = \boxed{\frac{2}{5}}$$ *La probabilitat és la mateixa que si $Z$ hagués tret la primera: el fet de no saber el resultat de $X$ i $Y$ preserva la simetria.*

**c)** Condicionem a que $X$ i $Y$ treuen del **mateix color**. Primer calculem $P\!\left(X \text{ i } Y \text{ igual}\right)$: $$P\!\left(\text{XY blanques}\right) = \frac{4}{10}\cdot\frac{3}{9} = \frac{12}{90} = \frac{2}{15}
\qquad
P\!\left(\text{XY negres}\right) = \frac{6}{10}\cdot\frac{5}{9} = \frac{30}{90} = \frac{1}{3}$$ $$P\!\left(\text{XY iguals}\right) = \frac{2}{15} + \frac{1}{3} = \frac{2}{15} + \frac{5}{15} = \frac{7}{15}$$

Ara apliquem probabilitat total per a $Z$ blanca, condicionant a cada cas: $$\begin{aligned}
P\!\left(Z_B \mid \text{XY iguals}\right) &= \frac{P\!\left(\text{XY blanques}\right)\cdot P\!\left(Z_B\mid\text{XY B}\right) + P\!\left(\text{XY negres}\right)\cdot P\!\left(Z_B\mid\text{XY N}\right)}{P\!\left(\text{XY iguals}\right)}\\[6pt]
&= \frac{\dfrac{2}{15}\cdot\dfrac{2}{8} + \dfrac{1}{3}\cdot\dfrac{4}{8}}{\dfrac{7}{15}}
= \frac{\dfrac{4}{120} + \dfrac{4}{24}}{\dfrac{7}{15}}
= \frac{\dfrac{1}{30} + \dfrac{1}{6}}{\dfrac{7}{15}}
= \frac{\dfrac{1}{5}}{\dfrac{7}{15}} = \frac{1}{5}\cdot\frac{15}{7} = \boxed{\frac{3}{7}}
\end{aligned}$$

*Fixeu-vos que $\frac{3}{7} \neq \frac{2}{5}$: saber que $X$ i $Y$ van treure del mateix color **sí** afecta la probabilitat de $Z$, a diferència de l’apartat b) on no sabíem res.*

</details>

> **Resum: les 4 preguntes per definir l’espai mostral**
>
> p0.5cm p5.5cm p4.5cm p2.5cm & **Pregunta** & **Exemple** & **Fórmula**  
> **1** & Els elements es poden distingir? & Targetes amb lletres repetides: SÍ & Depèn de 2–4  
> **2** & L’ordre importa? & Grup $\neq$ president/secretari & SÍ→$V$, NO→$\binom{n}{k}$  
> **3** & Hi ha reposició? & Treure boles tornant-les vs. sense tornar & SÍ→$n^k$, NO→$V$ o $\binom{n}{k}$  
> **4** & Tots els elements de $\Omega$ són equiprobables? & Daus: parelles ordenades sí, no ordenades no & Cal verificar!  
>
> **Si la resposta a la pregunta 4 és NO**, no pots usar la Regla de Laplace. Hauràs de calcular probabilitats amb **producte de branques** (regla del producte) com a l’exercici 15.

------------------------------------------------------------------------

## Problemes originals d’estil selectivitat

> Problemes **originals** redactats en l’estil de la selectivitat (no són d’exàmens oficials). Cada solució és desplegable.

### Problema 1 (2,5 punts)
Una fàbrica té tres màquines: la $A$ produeix el $50\,\%$ de les peces, la $B$ el $30\,\%$ i la $C$ el $20\,\%$. El percentatge de peces defectuoses és del $2\,\%$ a $A$, del $3\,\%$ a $B$ i del $5\,\%$ a $C$. Es tria una peça a l'atzar.

a) Quina és la probabilitat que sigui defectuosa?
b) Si és defectuosa, quina és la probabilitat que vingui de $C$?
c) Si no és defectuosa, quina és la probabilitat que vingui de $A$?

<details><summary>Solució</summary>

**a)** Probabilitat total: $P(D)=0{,}5\cdot0{,}02+0{,}3\cdot0{,}03+0{,}2\cdot0{,}05=0{,}01+0{,}009+0{,}01=\mathbf{0{,}029}$.

**b)** Bayes: $P(C\mid D)=\dfrac{0{,}2\cdot0{,}05}{0{,}029}=\dfrac{10}{29}\approx0{,}345$.

**c)** $P(A\mid\overline D)=\dfrac{0{,}5\cdot0{,}98}{1-0{,}029}=\dfrac{0{,}49}{0{,}971}\approx0{,}505$.

</details>

### Problema 2 (2 punts)
Siguin $A$ i $B$ dos esdeveniments amb $P(A)=0{,}5$, $P(B)=0{,}4$ i $P(A\cup B)=0{,}7$.

a) Calcula $P(A\cap B)$.
b) Són independents $A$ i $B$?
c) Calcula $P(\overline A\cap\overline B)$.
d) Calcula $P(A\mid A\cup B)$.

<details><summary>Solució</summary>

**a)** $P(A\cap B)=P(A)+P(B)-P(A\cup B)=0{,}5+0{,}4-0{,}7=0{,}2$.

**b)** Sí: $P(A)\cdot P(B)=0{,}5\cdot0{,}4=0{,}2=P(A\cap B)$.

**c)** $P(\overline A\cap\overline B)=1-P(A\cup B)=0{,}3$.

**d)** $P(A\mid A\cup B)=\dfrac{P(A)}{P(A\cup B)}=\dfrac{0{,}5}{0{,}7}=\dfrac57$.

</details>

### Problema 3 (2 punts)
Una urna conté $5$ boles vermelles i $3$ de blaves. S'extreuen $3$ boles **sense reposició**.

a) Calcula la probabilitat que exactament $2$ siguin vermelles.
b) Sabent que les dues primeres han estat de colors diferents, calcula la probabilitat que la tercera sigui vermella.

<details><summary>Solució</summary>

**a)** Cas favorable: 2 vermelles i 1 blava. $\dfrac{\binom52\binom31}{\binom83}=\dfrac{10\cdot3}{56}=\dfrac{15}{28}$.

**b)** Si les dues primeres són de colors diferents, n'han sortit una vermella i una blava. A l'urna en queden $4$ de vermelles i $2$ de blaves, així que la probabilitat és $\dfrac46=\dfrac23$.

</details>
