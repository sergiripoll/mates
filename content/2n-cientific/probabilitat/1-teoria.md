---
title: Probabilitat: Teoria
tematitol: Probabilitat
curs: 2n
modalitat: cientific
tema: probabilitat
bloc: teoria
ordre: 1
---
# Probabilitat: Teoria

**PROBABILITAT**  
2n Batxillerat  
Matemàtiques II

------------------------------------------------------------------------

La probabilitat és la branca de les matemàtiques que estudia la incertesa. Quan no sabem amb seguretat quin serà el resultat d’una situació, la probabilitat ens dóna una mesura de com de probable és cadascun dels possibles resultats. La fem servir cada dia: al temps, als jocs de cartes, a la medicina, a les assegurances…

## Conceptes bàsics

> **📘 Teoria**
>
> **Experiment aleatori:** Qualsevol acció el resultat de la qual no podem predir amb certesa. Per exemple: llançar un dau, treure una carta d’una baralla, o saber si plourà demà.
>
> **Espai mostral** $\Omega$: El conjunt de *tots* els resultats possibles d’un experiment aleatori.
>
> **Esdeveniment:** Qualsevol subconjunt de l’espai mostral. És a dir, qualsevol resultat o grup de resultats que ens interessi estudiar.

> **✏️ Exemple**
>
> Llançar un dau Llencem un dau de 6 cares. Identifiquem els elements bàsics:
>
> - **Experiment aleatori:** llançar el dau.
>
> - **Espai mostral:** $\Omega = \{1, 2, 3, 4, 5, 6\}$
>
> - **Exemple d’esdeveniment $A$:** “obtenir un nombre parell” $\Rightarrow A = \{2, 4, 6\}$
>
> - **Exemple d’esdeveniment $B$:** “obtenir un nombre major que 4” $\Rightarrow B = \{5, 6\}$

## Propietats de la probabilitat

La probabilitat és un nombre entre 0 i 1 que assignem a cada esdeveniment. Com més proper a 1, més probable és. Com més proper a 0, menys probable.

> **📘 Propietat**
>
> Propietats fonamentals Sigui $A$ un esdeveniment qualsevol de l’espai mostral $\Omega$:
>
> @p7cmp6cm@ **Esdeveniment segur** $\Omega$ & $P\!\left(\Omega\right) = 1$  
> **Esdeveniment impossible** $\emptyset$ & $P\!\left(\emptyset\right) = 0$  
> **Complementari** $\overline{A}$ (“no $A$”) & $P\!\left(\overline{A}\right) = 1 - P\!\left(A\right)$  
> **Unió** $A \cup B$ (“$A$ o $B$”) & $P\!\left(A \cup B\right) = P\!\left(A\right) + P\!\left(B\right) - P\!\left(A \cap B\right)$  

> **Per què es resta $\mathbf{P(A \cap B)}$? La intuïció darrere la fórmula**
>
> **El problema de la pluja:** Sabem que la probabilitat que demà plogui és $0{,}4$; que plogui demà passat és $0{,}3$; i que plogui *els dos dies alhora*, $0{,}2$.
>
> *Quina és la probabilitat que plogui **com a mínim un** dels dos dies?*
>
> Un alumne podria pensar: *“sumo $0{,}4 + 0{,}3 = 0{,}7$ i ja està”*. Però aquí hi ha un error: **estem comptant dues vegades** la situació en què plou els dos dies!
>
> Imagina que totes les situacions possibles les poses dins d’un rectangle:
>
> ![](img/probabilitat-546bc6.svg)
>
> **La solució:** quan sumes $P\!\left(A\right) + P\!\left(B\right)$, la zona del mig (plou els dos dies) entra *una vegada* per $A$ i *una altra vegada* per $B$. Per tant, l’has comptada **dues vegades**, i n’has de treure una:
>
> $$P\!\left(A \cup B\right) = \underbrace{0{,}4}_{\text{plou demà}} + \underbrace{0{,}3}_{\text{plou demà passat}} - \underbrace{0{,}2}_{\substack{\text{trèiem el que} \\ \text{hem comptat dues vegades}}} = \boxed{0{,}5}$$
>
> **Resum visual del que representa cada zona:**
>
> |  **Zona**  | **Significat**                |             **Probabilitat**             |
> |:----------:|:------------------------------|:----------------------------------------:|
> | Només $A$  | Plou demà però NO demà passat |         $0{,}4 - 0{,}2 = 0{,}2$          |
> | Només $B$  | Plou demà passat però NO demà |         $0{,}3 - 0{,}2 = 0{,}1$          |
> | $A \cap B$ | Plou els dos dies             |                 $0{,}2$                  |
> | $A \cup B$ | Plou **almenys** un dia       | $0{,}2 + 0{,}1 + 0{,}2 = \mathbf{0{,}5}$ |
>
> *Sumant les tres zones separades (sense solapament) obtenim el mateix resultat. La fórmula $P\!\left(A\right) + P\!\left(B\right) - P\!\left(A \cap B\right)$ és simplement una drecera per fer aquest càlcul.*

> **Pregunta clau: quan val $\mathbf{P(A \cap B) = P(A) \cdot P(B)}$ i quan no?**
>
> Aquesta és una de les confusions més habituals. La resposta curta és:
>
> \|p5.5cm\|p7.5cm\| **Situació** & **Com calculem $P\!\left(A \cap B\right)$?**  
> $A$ i $B$ **independents** (un no afecta l’altre) & $P\!\left(A \cap B\right) = P\!\left(A\right) \cdot P\!\left(B\right)$ Podem multiplicar directament.  
> $A$ i $B$ **dependents** (un sí afecta l’altre) & $P\!\left(A \cap B\right)$ **ens la donen** al problema, o cal calcular-la per un altre camí.  
>
> **Exemple 1 — Independents (podem multiplicar):**
>
> Llancem una moneda i un dau. Definim:
>
> - $A$ = “surt cara” $\Rightarrow P\!\left(A\right) = 0{,}5$
>
> - $B$ = “surt 6 al dau” $\Rightarrow P\!\left(B\right) = \frac{1}{6}$
>
> El resultat de la moneda **no té res a veure** amb el resultat del dau. Són independents. Per tant: $$P\!\left(A \cap B\right) = P\!\left(A\right) \cdot P\!\left(B\right) = 0{,}5 \cdot \frac{1}{6} = \frac{1}{12} \approx 0{,}083$$
>
> **Exemple 2 — Dependents (NO podem multiplicar):**
>
> El temps de demà i demà passat. Definim:
>
> - $A$ = “plou demà” $\Rightarrow P\!\left(A\right) = 0{,}4$
>
> - $B$ = “plou demà passat” $\Rightarrow P\!\left(B\right) = 0{,}3$
>
> Si avui plou, és **més probable** que demà passat també plogui (les borrasques duren dies). El temps d’un dia **influeix** en el del dia següent: $A$ i $B$ són **dependents**.
>
> Si intentéssim multiplicar: $P\!\left(A\right) \cdot P\!\left(B\right) = 0{,}4 \cdot 0{,}3 = 0{,}12$. Però el problema ens diu que $P\!\left(A \cap B\right) = 0{,}2$. Són valors **diferents** perquè **no podem multiplicar**.
>
> En aquest cas, $P\!\left(A \cap B\right) = 0{,}2$ és una dada que **ens dóna el problema** (obtinguda, per exemple, de dades meteorològiques històriques), no una cosa que puguem deduir multiplicant.
>
> **La pregunta que t’has de fer sempre:**
>
> ![](img/probabilitat-35dbf2.svg)
>
> **Més exemples per entrenar la intuïció:**
>
> p6.5cm c p4cm **Situació** & **Relació** & **Per què?**  
> Treure dues cartes *amb* reposició & Independents & La 2a extracció no depèn de la 1a  
> Treure dues cartes *sense* reposició & Dependents & La 1a carta canvia les que queden  
> Llançar dos daus & Independents & Un dau no afecta l’altre  
> Nota del primer examen i del segon & Dependents & L’esforç, l’estudiant… influeixen  
> Tenir cotxe i tenir febre avui & Independents & No hi ha relació entre els dos  
> Fumar i tenir càncer de pulmó & Dependents & Un factor clarament influeix en l’altre  

> **✏️ Exemple**
>
> Propietats — Calcular la intersecció a partir de la unió Dos successos $A$ i $B$ compleixen: $$P\!\left(A\right) = 0{,}58 \qquad P\!\left(B\right) = 0{,}42 \qquad P\!\left(A \cup B\right) = 0{,}80$$ Calcula $P\!\left(A \cap B\right)$ i indica si $A$ i $B$ són incompatibles.
>
> **Resolució:** Apliquem la fórmula de la unió i aïllem $P\!\left(A \cap B\right)$: $$P\!\left(A \cup B\right) = P\!\left(A\right) + P\!\left(B\right) - P\!\left(A \cap B\right)$$ $$0{,}80 = 0{,}58 + 0{,}42 - P\!\left(A \cap B\right)$$ $$\boxed{P\!\left(A \cap B\right) = 0{,}58 + 0{,}42 - 0{,}80 = 0{,}20}$$
>
> Com que $P\!\left(A \cap B\right) = 0{,}20 \neq 0$, els successos $A$ i $B$ **no són incompatibles**: poden succeir alhora.

> **⚠️ Atenció**
>
> Molts alumnes confonen **incompatible** amb **independent**. Recorda:
>
> - **Incompatibles:** $A$ i $B$ no poden passar alhora $\Rightarrow P\!\left(A \cap B\right) = 0$
>
> - **Independents:** el fet que passi $A$ no afecta la probabilitat de $B$ $\Rightarrow P\!\left(A \cap B\right) = P\!\left(A\right) \cdot P\!\left(B\right)$
>
> Dos successos incompatibles (amb probabilitat positiva) **mai** poden ser independents!

## La Regla de Laplace

> **📘 Teoria**
>
> Quan tots els resultats de l’espai mostral són **igualment probables** (com ara llançar un dau no trucat, o treure una carta d’una baralla ben barrejada), podem calcular la probabilitat d’un esdeveniment $A$ com: $$P\!\left(A\right) = \frac{\text{casos favorables}}{\text{casos possibles}} = \frac{n(A)}{n(\Omega)}$$

> **✏️ Exemple**
>
> Laplace — Fitxa de dòmino Tirem un dòmino. Quina és la probabilitat que la suma dels punts d’una fitxa sigui menor que 7?
>
> **Resolució:** Un joc de dòmino té 28 fitxes (de \[0-0\] a \[6-6\]). Cal comptar les fitxes amb suma $< 7$: \[0-0\], \[0-1\], \[0-2\], \[0-3\], \[0-4\], \[0-5\], \[0-6\], \[1-1\], \[1-2\], \[1-3\], \[1-4\], \[1-5\], \[2-2\], \[2-3\], \[2-4\], \[3-3\] $\Rightarrow$ 16 fitxes. $$P\!\left(S < 7\right) = \frac{16}{28} = \frac{4}{7} \approx 0{,}571$$

> **✏️ Exemple**
>
> Laplace i unió — Resultats d’exàmens a una classe En una classe, el 67% dels alumnes van aprovar Matemàtiques i el 63% van aprovar Anglès, mentre que el 38% van aprovar les dues matèries. Escollim un alumne a l’atzar. Calcula la probabilitat que:
>
> Definim: $M$ = “aprovar Matemàtiques”, $A$ = “aprovar Anglès”.
>
> Dades: $P\!\left(M\right) = 0{,}67$, $\quad P\!\left(A\right) = 0{,}63$, $\quad P\!\left(M \cap A\right) = 0{,}38$
>
> **a) Hagi aprovat alguna de les dues matèries.** $$P\!\left(M \cup A\right) = P\!\left(M\right) + P\!\left(A\right) - P\!\left(M \cap A\right) = 0{,}67 + 0{,}63 - 0{,}38 = \boxed{0{,}92}$$
>
> **b) Hagi aprovat *només* Matemàtiques.**
>
> “Només Matemàtiques” vol dir: ha aprovat Matemàtiques però *no* Anglès. $$P\!\left(M \cap \overline{A}\right) = P\!\left(M\right) - P\!\left(M \cap A\right) = 0{,}67 - 0{,}38 = \boxed{0{,}29}$$
>
> **c) No hagi aprovat cap de les dues.**
>
> Complementari de “alguna de les dues”: $$P\!\left(\overline{M \cup A}\right) = 1 - P\!\left(M \cup A\right) = 1 - 0{,}92 = \boxed{0{,}08}$$
>
> **d) Hagi aprovat només una de les dues.** $$P\!\left(\text{només una}\right) = P\!\left(M \cap \overline{A}\right) + P\!\left(\overline{M} \cap A\right) = 0{,}29 + (0{,}63 - 0{,}38) = 0{,}29 + 0{,}25 = \boxed{0{,}54}$$

## Probabilitat condicionada

Sovint no tenim informació completa: sabem que ja ha passat alguna cosa i volem saber com afecta això a la probabilitat d’un altre esdeveniment. Aquí entra la **probabilitat condicionada**.

> **📘 Teoria**
>
> Donats dos esdeveniments $A$ i $B$ amb $P\!\left(B\right) \neq 0$, la **probabilitat de $A$ condicionada a $B$** és la probabilitat que passi $A$ *sabent que ja ha passat $B$*: $$P\!\left(A \mid B\right) = \frac{P\!\left(A \cap B\right)}{P\!\left(B\right)}$$ D’aquí s’obté la **regla del producte**, molt útil per calcular interseccions: $$P\!\left(A \cap B\right) = P\!\left(B\right) \cdot P\!\left(A \mid B\right) = P\!\left(A\right) \cdot P\!\left(B \mid A\right)$$

> **✏️ Exemple**
>
> Probabilitat condicionada — Cargols defectuosos Tenim una capsa amb 5 cargols de cabota rodona (2 defectuosos) i 8 de cabota quadrada (3 correctes, 5 defectuosos). Escollim un cargol a l’atzar.
>
> Definim: $Q$ = “cabota quadrada”, $D$ = “defectuós”, $\overline{D}$ = “correcte”.
>
> Resum de la situació (13 cargols en total):
>
> |                     | **Correctes** | **Defectuosos** | **Total** |
> |:--------------------|:-------------:|:---------------:|:---------:|
> | **Cabota rodona**   |       3       |        2        |     5     |
> | **Cabota quadrada** |       3       |        5        |     8     |
> | **Total**           |       6       |        7        |    13     |
>
> **a) Probabilitat que sigui de cabota quadrada, sabent que és correcte.** $$P\!\left(Q \mid \overline{D}\right) = \frac{P\!\left(Q \cap \overline{D}\right)}{P\!\left(\overline{D}\right)} = \frac{3/13}{6/13} = \frac{3}{6} = \boxed{\frac{1}{2}}$$
>
> **b) Probabilitat que sigui defectuós, sabent que és de cabota rodona.** $$P\!\left(D \mid \overline{Q}\right) = \frac{P\!\left(D \cap \overline{Q}\right)}{P\!\left(\overline{Q}\right)} = \frac{2/13}{5/13} = \frac{2}{5} = \boxed{0{,}40}$$

### Esdeveniments independents

> **📘 Propietat**
>
> Independència d’esdeveniments Dos esdeveniments $A$ i $B$ són **independents** si el fet que passi un *no afecta* la probabilitat de l’altre. Formalment: $$A \text{ i } B \text{ independents} \iff P\!\left(A \cap B\right) = P\!\left(A\right) \cdot P\!\left(B\right)$$ De manera equivalent: $P\!\left(A \mid B\right) = P\!\left(A\right)$ i $P\!\left(B \mid A\right) = P\!\left(B\right)$.

> **✏️ Exemple**
>
> Independència — Controls de qualitat d’un automòbil Un automòbil passa tres controls independents: mecànic ($M$), elèctric ($E$) i de planxa ($X$), amb probabilitats de fallada $0{,}02$, $0{,}01$ i $0{,}07$ respectivament. Si la fàbrica treu 500 cotxes, quants sortiran amb algun defecte?
>
> **Estratègia:** és més fàcil calcular la probabilitat de *cap* defecte i fer el complementari.
>
> Com que els tres controls són independents: $$P\!\left(\text{cap defecte}\right) = P\!\left(\overline{M}\right) \cdot P\!\left(\overline{E}\right) \cdot P\!\left(\overline{X}\right) = 0{,}98 \cdot 0{,}99 \cdot 0{,}93 = 0{,}9022$$ $$P\!\left(\text{algun defecte}\right) = 1 - 0{,}9022 = \boxed{0{,}0978}$$ $$\text{Cotxes defectuosos esperats} = 500 \cdot 0{,}0978 \approx \boxed{49 \text{ cotxes}}$$

## Teorema de la probabilitat total

> **📘 Teoria**
>
> Quan l’espai mostral es pot dividir en parts que **no se solapen** i **ho cobreixen tot** (sistema complet d’esdeveniments $A_1, A_2, \ldots, A_n$), la probabilitat de qualsevol altre esdeveniment $B$ es pot calcular com: $$P\!\left(B\right) = P\!\left(A_1\right)\cdot P\!\left(B \mid A_1\right) + P\!\left(A_2\right)\cdot P\!\left(B \mid A_2\right) + \cdots + P\!\left(A_n\right)\cdot P\!\left(B \mid A_n\right)$$ Visualment, es fa servir el **diagrama d’arbre**: cada branca representa una “via” per arribar a $B$, i sumem totes les vies.

> **✏️ Exemple**
>
> Probabilitat total — Eleccions a dues ciutats En les últimes eleccions, a la ciutat $A$ els grocs van obtenir el 20% dels vots i a la ciutat $B$ el 40%. Escollim una de les dues ciutats a l’atzar i una persona que hi visqui.
>
> **Quina és la probabilitat que la persona hagi votat el partit groc?**
>
> Definim: $A$ = “escollir la ciutat A”, $B$ = “escollir la ciutat B”, $G$ = “votar groc”.
>
> Dades: $P\!\left(A\right) = P\!\left(B\right) = 0{,}5$, $\quad P\!\left(G \mid A\right) = 0{,}20$, $\quad P\!\left(G \mid B\right) = 0{,}40$.
>
> **Diagrama d’arbre:**
>
> ![](img/probabilitat-f1911b.svg)
>
> Apliquem el teorema de la probabilitat total: $$P\!\left(G\right) = P\!\left(A\right)\cdot P\!\left(G \mid A\right) + P\!\left(B\right)\cdot P\!\left(G \mid B\right)
= 0{,}5 \cdot 0{,}20 + 0{,}5 \cdot 0{,}40 = 0{,}10 + 0{,}20 = \boxed{0{,}30}$$

## Teorema de Bayes

> **📘 Teoria**
>
> El teorema de Bayes respon la pregunta inversa: *ja sabem que ha passat $B$, quina és la probabilitat que provingués de la “via $A_i$”?* $$P\!\left(A_i \mid B\right) = \frac{P\!\left(A_i\right) \cdot P\!\left(B \mid A_i\right)}{P\!\left(B\right)} = \frac{P\!\left(A_i\right) \cdot P\!\left(B \mid A_i\right)}{\displaystyle\sum_{j=1}^{n} P\!\left(A_j\right) \cdot P\!\left(B \mid A_j\right)}$$ El denominador no és res més que $P\!\left(B\right)$ calculat amb el teorema de la probabilitat total.

> **✏️ Exemple**
>
> Bayes — Qui ha votat el groc? Seguint l’exemple anterior: **sabent que la persona ha votat el partit groc, quina és la probabilitat que visqui a la ciutat $A$?**
>
> Ara apliquem Bayes, usant $P\!\left(G\right) = 0{,}30$ calculat abans: $$P\!\left(A \mid G\right) = \frac{P\!\left(A\right) \cdot P\!\left(G \mid A\right)}{P\!\left(G\right)} = \frac{0{,}5 \cdot 0{,}20}{0{,}30} = \frac{0{,}10}{0{,}30} = \boxed{0{,}\overline{3}}$$ Només 1 de cada 3 votants grocs prové de la ciutat $A$, perquè malgrat que les dues ciutats es triaven amb la mateixa probabilitat, la ciutat $B$ té el doble de votants grocs.

> **✏️ Exemple**
>
> Bayes PAU — Rellotges defectuosos i dos proveïdors Un joier compra el 60% dels rellotges al proveïdor $P_1$ (0,4% defectuosos) i el 40% al proveïdor $P_2$ (1,5% defectuosos). Un rellotge resulta defectuós. Quina és la probabilitat que provingui de $P_2$?
>
> Definim: $P_1$, $P_2$ = proveïdors; $D$ = “defectuós”.
>
> Dades: $$P\!\left(P_1\right) = 0{,}60,\quad P\!\left(D \mid P_1\right) = 0{,}004 \qquad
P\!\left(P_2\right) = 0{,}40,\quad P\!\left(D \mid P_2\right) = 0{,}015$$
>
> **Pas 1 — Probabilitat total de defecte:** $$P\!\left(D\right) = 0{,}60 \cdot 0{,}004 + 0{,}40 \cdot 0{,}015 = 0{,}0024 + 0{,}0060 = 0{,}0084$$
>
> **Pas 2 — Bayes:** $$P\!\left(P_2 \mid D\right) = \frac{P\!\left(P_2\right) \cdot P\!\left(D \mid P_2\right)}{P\!\left(D\right)} = \frac{0{,}40 \cdot 0{,}015}{0{,}0084} = \frac{0{,}006}{0{,}0084} \approx \boxed{0{,}714}$$
>
> Malgrat que $P_2$ subministra menys rellotges, la seva taxa de defectes és gairebé 4 vegades superior, cosa que fa que el 71% dels rellotges defectuosos provinguin d’ell.
