---
title: Distribució binomial i normal. Intervals de confiança: Exercicis
tematitol: Distribució binomial i normal. Intervals de confiança
curs: 2n
modalitat: cientific
tema: distribucions
bloc: exercicis
ordre: 2
---
# Distribució binomial i normal. Intervals de confiança: Exercicis

### Problemes graduats

> **✏️ Exemple**
>
> Nivell 1 — Clients satisfets d’una empresa Una empresa estima que el 80% dels seus clients estan satisfets. S’escullen 10 clients a l’atzar. Quina és la probabilitat que **exactament 8** estiguin satisfets?
>
> **Pas 1 — Comprova les 4 condicions:** $n=10$ clients (fix), cada client satisfet o no (2 resultats), $p=0{,}8$ constant, clients independents. ✓ $\Rightarrow X \sim B(10,\; 0{,}8)$
>
> **Pas 2 — Aplica la fórmula:** $$P(X=8) = \binom{10}{8} \cdot 0{,}8^8 \cdot 0{,}2^2
= 45 \cdot 0{,}16777 \cdot 0{,}04 = \boxed{0{,}3020}$$
>
> *És el valor màxim probable: l’esperança és $\mu = 10\cdot0{,}8 = 8$ clients satisfets.*

> **✏️ Exemple**
>
> Nivell 1 — Examen tipus test a l’atzar Un examen de 20 preguntes, 4 opcions cadascuna (una correcta). Un alumne respon **a l’atzar**. Quina és la probabilitat d’encertar **exactament 5** preguntes?
>
> $p = \frac{1}{4} = 0{,}25$, $n=20$, $X \sim B(20,\; 0{,}25)$.
>
> $$P(X=5) = \binom{20}{5} \cdot 0{,}25^5 \cdot 0{,}75^{15}
= 15504 \cdot 0{,}000977 \cdot 0{,}01336 = \boxed{0{,}2023}$$
>
> *L’esperança és $\mu = 20 \cdot 0{,}25 = 5$ preguntes encertades a l’atzar. El resultat màxim probable coincideix exactament amb l’esperança.*

> **Estratègia per a “almenys” i “com a màxim”**
>
> p4cm p4.5cm p4.5cm **Expressió** & **Directe** & **Via complementari**  
> $P(X \geq k)$ & Suma des de $k$ fins a $n$ & $= 1 - P(X \leq k{-}1)$ **Millor si $k$ és gran**  
> $P(X \leq k)$ & Suma des de $0$ fins a $k$ & $= 1 - P(X \geq k{+}1)$ **Millor si $k$ és petit**  
> $P(X > k)$ & $= P(X \geq k+1)$ & $= 1 - P(X \leq k)$  
> $P(X < k)$ & $= P(X \leq k-1)$ & $= 1 - P(X \geq k)$  
>
> **Regla pràctica:** si el complementari té *menys termes* que el directe, usa’l.

> **✏️ Exemple**
>
> Nivell 2 — Almenys: bombetes d’un fabricant El 95% de les bombetes d’un fabricant funcionen correctament. Se’n prenen 15 a l’atzar. Quina és la probabilitat que **almenys 14** funcionin?
>
> $X \sim B(15,\; 0{,}95)$. “Almenys 14” = $P(X \geq 14) = P(X=14) + P(X=15)$.
>
> Directe és millor (2 termes vs. 14 del complementari): $$\begin{aligned}
P(X=14) &= \binom{15}{14} \cdot 0{,}95^{14} \cdot 0{,}05^1 = 15 \cdot 0{,}4877 \cdot 0{,}05 = 0{,}3658 \\
P(X=15) &= \binom{15}{15} \cdot 0{,}95^{15} \cdot 0{,}05^0 = 1 \cdot 0{,}4633 \cdot 1 = 0{,}4633 \\[4pt]
P(X \geq 14) &= 0{,}3658 + 0{,}4633 = \boxed{0{,}8290}
\end{aligned}$$

> **✏️ Exemple**
>
> Nivell 2 — Complementari obligatori: cargols defectuosos Una màquina produeix cargols amb un 2% de defectes. S’inspeccionen 50 cargols. Quina és la probabilitat de trobar **més de 2** defectuosos?
>
> $X \sim B(50,\; 0{,}02)$. “Més de 2” = $P(X > 2) = P(X \geq 3)$.
>
> Directe requeriria sumar 48 termes. Usem el complementari: $$P(X > 2) = 1 - P(X \leq 2) = 1 - \bigl[P(X=0) + P(X=1) + P(X=2)\bigr]$$ $$\begin{aligned}
P(X=0) &= 0{,}98^{50} = 0{,}3642 \\
P(X=1) &= 50 \cdot 0{,}02 \cdot 0{,}98^{49} = 0{,}3716 \\
P(X=2) &= \binom{50}{2} \cdot 0{,}02^2 \cdot 0{,}98^{48} = 1225 \cdot 0{,}0004 \cdot 0{,}3716 = 0{,}1858 \\[4pt]
P(X > 2) &= 1 - (0{,}3642 + 0{,}3716 + 0{,}1858) = 1 - 0{,}9216 = \boxed{0{,}0784}
\end{aligned}$$

> **✏️ Exemple**
>
> Nivell 3 — Probabilitat fraccionària: pòlissa d’assegurança Un agent d’assegurances ven pòlisses a 5 persones de la mateixa edat. La probabilitat que cadascuna visqui 30 anys o més és $p = \frac{2}{3}$. Sigui $X$ = “nombre de persones que viuen 30 anys o més”. Llavors $X \sim B\!\left(5,\,\frac{2}{3}\right)$.
>
> **a) Les cinc persones viuen ($k=5$):** $$P(X=5) = \binom{5}{5}\cdot\left(\frac{2}{3}\right)^5\cdot\left(\frac{1}{3}\right)^0
= 1 \cdot \frac{32}{243} \cdot 1 = \frac{32}{243} \approx \boxed{0{,}1317}$$
>
> **b) Almenys tres persones ($k \geq 3$):** $$P(X \geq 3) = P(3) + P(4) + P(5)$$ $$\begin{aligned}
P(X=3) &= \binom{5}{3}\cdot\left(\frac{2}{3}\right)^3\cdot\left(\frac{1}{3}\right)^2
= 10\cdot\frac{8}{27}\cdot\frac{1}{9} = \frac{80}{243} \\
P(X=4) &= \binom{5}{4}\cdot\left(\frac{2}{3}\right)^4\cdot\left(\frac{1}{3}\right)^1
= 5\cdot\frac{16}{81}\cdot\frac{1}{3} = \frac{80}{243} \\
P(X=5) &= \frac{32}{243}
\end{aligned}$$ $$P(X \geq 3) = \frac{80+80+32}{243} = \frac{192}{243} = \frac{64}{81} \approx \boxed{0{,}7901}$$
>
> **c) Exactament dues persones ($k=2$):** $$P(X=2) = \binom{5}{2}\cdot\left(\frac{2}{3}\right)^2\cdot\left(\frac{1}{3}\right)^3
= 10\cdot\frac{4}{9}\cdot\frac{1}{27} = \frac{40}{243} \approx \boxed{0{,}1646}$$

> **✏️ Exemple**
>
> Nivell PAU — Moneda i simetria de la distribució Es llança una moneda **quatre vegades**. Quina és la probabilitat que surtin **més cares que creus**?
>
> “Més cares que creus” vol dir $X > 2$, és a dir, $X = 3$ o $X = 4$. $X \sim B(4,\, 0{,}5)$.
>
> $$\begin{aligned}
P(X=3) &= \binom{4}{3} \cdot 0{,}5^3 \cdot 0{,}5^1 = 4 \cdot \frac{1}{16} = \frac{4}{16} \\
P(X=4) &= \binom{4}{4} \cdot 0{,}5^4 = 1 \cdot \frac{1}{16} = \frac{1}{16} \\[4pt]
P(X \geq 3) &= \frac{4}{16} + \frac{1}{16} = \frac{5}{16} = \boxed{0{,}3125}
\end{aligned}$$
>
> *Nota de simetria: $P(\text{més creus que cares}) = P(X \leq 1)$ = també $\frac{5}{16}$ (per simetria de $p=0{,}5$). La probabilitat d’empat ($X=2$) és $\binom{4}{2}\cdot 0{,}5^4 = \frac{6}{16}$, i $\frac{5}{16}+\frac{6}{16}+\frac{5}{16} = 1$ ✓*

### Exercicis

> **📝 Exercici**
>
> 16 — Torneig de tennis Un jugador de tennis té un 60% de probabilitat de guanyar cada partit. Si juga **5 partits**, calcula:
>
> 1.  La probabilitat de guanyar **exactament 3** partits.
>
> 2.  La probabilitat de guanyar **almenys 3** partits.
>
> 3.  L’esperança i la desviació típica del nombre de partits guanyats.

<details><summary>Solució</summary>

$X \sim B(5,\; 0{,}6)$.

**a)** $$P(X=3) = \binom{5}{3}\cdot 0{,}6^3\cdot 0{,}4^2 = 10 \cdot 0{,}216 \cdot 0{,}16 = \boxed{0{,}3456}$$

**b)** $$\begin{aligned}
P(X=3) &= 0{,}3456 \\
P(X=4) &= \binom{5}{4}\cdot 0{,}6^4\cdot 0{,}4^1 = 5\cdot 0{,}1296\cdot 0{,}4 = 0{,}2592 \\
P(X=5) &= 0{,}6^5 = 0{,}0778 \\
P(X \geq 3) &= 0{,}3456 + 0{,}2592 + 0{,}0778 = \boxed{0{,}6826}
\end{aligned}$$

**c)** $$\mu = 5 \cdot 0{,}6 = \boxed{3} \text{ partits} \qquad
\sigma = \sqrt{5 \cdot 0{,}6 \cdot 0{,}4} = \sqrt{1{,}2} \approx \boxed{1{,}095}$$

</details>

> **📝 Exercici**
>
> 17 — Components electrònics defectuosos Un fabricant de components electrònics sap que el 3% dels seus productes són defectuosos. En una comanda de 25 unitats, calcula:
>
> 1.  La probabilitat que **cap** sigui defectuosa.
>
> 2.  La probabilitat que **com a màxim una** sigui defectuosa.
>
> 3.  La probabilitat que **més de dues** siguin defectuoses.

<details><summary>Solució</summary>

$X \sim B(25,\; 0{,}03)$.

**a)** $$P(X=0) = 0{,}97^{25} = \boxed{0{,}4670}$$

**b)** $$P(X=1) = 25 \cdot 0{,}03 \cdot 0{,}97^{24} = 25 \cdot 0{,}03 \cdot 0{,}4815 = 0{,}3611$$ $$P(X \leq 1) = 0{,}4670 + 0{,}3611 = \boxed{0{,}8281}$$

**c)** Complementari (sumar des de 3 fins a 25 seria molt llarg): $$P(X=2) = \binom{25}{2}\cdot 0{,}03^2\cdot 0{,}97^{23} = 300 \cdot 0{,}0009 \cdot 0{,}4963 = 0{,}1340$$ $$P(X > 2) = 1 - P(X \leq 2) = 1 - (0{,}4670 + 0{,}3611 + 0{,}1340) = 1 - 0{,}9621 = \boxed{0{,}0379}$$

</details>

> **📝 Exercici**
>
> 18 — PAU: Pòlissa d’assegurança de vida Un agent d’assegurances ven pòlisses a 5 persones joves i sanes. La probabilitat que cada persona visqui 30 anys o més és $\dfrac{2}{3}$. Calcula:
>
> 1.  La probabilitat que totes cinc visquin 30 anys o més.
>
> 2.  La probabilitat que almenys tres visquin 30 anys o més.
>
> 3.  La probabilitat que exactament dues visquin 30 anys o més.
>
> 4.  Quantes persones s’espera que visquin 30 anys o més? Calcula també la desviació típica.

<details><summary>Solució</summary>

$X \sim B\!\left(5,\,\dfrac{2}{3}\right)$, on $\dfrac{1}{3} = 1 - \dfrac{2}{3}$.

**a)** $P(X=5) = \left(\dfrac{2}{3}\right)^5 = \dfrac{32}{243} \approx \boxed{0{,}1317}$

**b)** $P(X \geq 3) = \dfrac{80+80+32}{243} = \dfrac{192}{243} \approx \boxed{0{,}7901}$

**c)** $P(X=2) = \dbinom{5}{2}\cdot\left(\dfrac{2}{3}\right)^2\cdot\left(\dfrac{1}{3}\right)^3 = 10\cdot\dfrac{4}{9}\cdot\dfrac{1}{27} = \dfrac{40}{243} \approx \boxed{0{,}1646}$

**d)** $\mu = 5\cdot\dfrac{2}{3} = \dfrac{10}{3} \approx \boxed{3{,}33}$ persones $\quad\sigma = \sqrt{5\cdot\dfrac{2}{3}\cdot\dfrac{1}{3}} = \sqrt{\dfrac{10}{9}} \approx \boxed{1{,}054}$

</details>

> **⚠️ Atenció**
>
> **Els errors més freqüents amb la distribució binomial:**
>
> **Error 1 — Confondre “èxit” amb “cosa bona”.** L’èxit és simplement el resultat que comptem. En el problema dels cargols, “l’èxit” és “cargol defectuós” ($p=0{,}02$). No té per què ser positiu.
>
> **Error 2 — Oblidar el complementari.** Quan et demanen “més de 2” amb $n=50$, sumar 48 termes és inviable. Usa *sempre* el complementari quan el costat petit tingui *3 o menys* termes.
>
> **Error 3 — Usar binomial quan no hi ha independència.** Si treus boles d’una urna *sense reposició*, la probabilitat canvia a cada extracció: *no pots* usar la binomial. Cal usar combinatòria clàssica.
>
> **Error 4 — Confondre $P(X > k)$ amb $P(X \geq k)$.** $$P(X > 2) = 1 - P(X \leq 2) \qquad \text{però} \qquad P(X \geq 2) = 1 - P(X \leq 1)$$ Un terme de diferència canvia completament el resultat!

------------------------------------------------------------------------

### Exercicis

> **📝 Exercici**
>
> 19 — Tipificació i probabilitats normals Les puntuacions d’un test psicològic segueixen una distribució $X \sim N(100,\; 15)$. Calcula, raonant el procediment de tipificació:
>
> 1.  $P(X \leq 115)$
>
> 2.  $P(X \geq 85)$
>
> 3.  $P(85 \leq X \leq 115)$
>
> Dada: $P(Z \leq 1) = 0{,}8413$.

<details><summary>Solució</summary>

$X \sim N(100, 15)$, per tant $Z = \dfrac{X - 100}{15}$.

**a)** $$P(X \leq 115) = P\!\left(Z \leq \frac{115-100}{15}\right) = P(Z \leq 1) = \boxed{0{,}8413}$$

**b)** $$P(X \geq 85) = P\!\left(Z \geq \frac{85-100}{15}\right) = P(Z \geq -1) = P(Z \leq 1) = \boxed{0{,}8413}$$

**c)** $$P(85 \leq X \leq 115) = P(-1 \leq Z \leq 1) = 2 \cdot 0{,}8413 - 1 = \boxed{0{,}6826}$$

</details>

> **📝 Exercici**
>
> 20 — PAU: IC per a la mitjana, $\sigma$ coneguda Hem mesurat el pes (en kg) de 36 alumnes d’un institut i hem obtingut una mitjana mostral $\bar{x} = 62{,}4$ kg. Sabem que el pes segueix una distribució normal amb desviació típica $\sigma = 8$ kg.
>
> 1.  Construeix un interval de confiança al 95% per al pes mitjà dels alumnes.
>
> 2.  Construeix un interval de confiança al 99%.
>
> 3.  Explica per quin motiu l’interval al 99% és més ample que el del 95%.
>
> Dades: $P(-1{,}96 \leq Z \leq 1{,}96) = 0{,}95$ i $P(-2{,}58 \leq Z \leq 2{,}58) = 0{,}99$.

<details><summary>Solució</summary>

$n = 36$, $\bar{x} = 62{,}4$, $\sigma = 8$.

**Error estàndard:** $\dfrac{\sigma}{\sqrt{n}} = \dfrac{8}{\sqrt{36}} = \dfrac{8}{6} = 1{,}333$

**a) IC al 95%:** $$62{,}4 \pm 1{,}96 \cdot 1{,}333 = 62{,}4 \pm 2{,}613
\quad\Rightarrow\quad \boxed{[59{,}79\ ,\ 65{,}01]}$$

**b) IC al 99%:** $$62{,}4 \pm 2{,}58 \cdot 1{,}333 = 62{,}4 \pm 3{,}440
\quad\Rightarrow\quad \boxed{[58{,}96\ ,\ 65{,}84]}$$

**c)** L’IC al 99% és més ample perquè $z$ és més gran ($2{,}58 > 1{,}96$). Multipliquem el mateix error estàndard per un nombre més gran, cosa que eixampla l’interval. A canvi, l’estimació és menys precisa però tenim més confiança que $\mu$ hi queda inclòs.

</details>

> **📝 Exercici**
>
> 21 — PAU: IC per a una proporció En una enquesta a 400 estudiants universitaris, 180 afirmen que utilitzen el transport públic diàriament.
>
> 1.  Calcula l’estimació puntual del percentatge d’estudiants que utilitzen transport públic.
>
> 2.  Construeix un interval de confiança al 95% per a aquesta proporció.
>
> 3.  Un estudi anterior afirmava que el 50% dels estudiants utilitzen transport públic. És compatible aquest valor amb l’interval obtingut?
>
> Dada: $P(-1{,}96 \leq Z \leq 1{,}96) = 0{,}95$.

<details><summary>Solució</summary>

**a) Estimació puntual:** $$\hat{p} = \frac{180}{400} = 0{,}45 \quad\Rightarrow\quad \textbf{45\%}$$

**b) Error estàndard:** $$\sqrt{\frac{0{,}45 \cdot 0{,}55}{400}} = \sqrt{\frac{0{,}2475}{400}} = \sqrt{0{,}000619} = 0{,}02488$$ $$\text{IC 95\%} = 0{,}45 \pm 1{,}96 \cdot 0{,}02488 = 0{,}45 \pm 0{,}0488 = \boxed{[40{,}12\%\ ,\ 49{,}88\%]}$$

**c)** El 50% **no** pertany a $[40{,}12\%;\; 49{,}88\%]$. Per tant, amb un 95% de confiança, l’afirmació de l’estudi anterior no és compatible amb les nostres dades.

</details>

> **Resum: les fórmules que necessites a la selectivitat**
>
> p3.5cm p5.5cm p3.5cm **Situació** & **Fórmula de l’IC** & **Quan s’usa**  
> Mitjana, $\sigma$ coneguda & $\bar{x} \pm z_\gamma \cdot \dfrac{\sigma}{\sqrt{n}}$ & $\sigma$ és una dada  
> Mitjana, $\sigma$ desconeguda & $\bar{x} \pm z_\gamma \cdot \dfrac{S}{\sqrt{n}}$ & $n \geq 30$, s’usa $S$  
> Proporció & $\hat{p} \pm z_\gamma \cdot \sqrt{\dfrac{\hat{p}(1-\hat{p})}{n}}$ & Percentatges, enquestes  
>   

> **⚠️ Atenció**
>
> **Errors freqüents a la selectivitat:**
>
> **Error 1 — Confondre $\sigma$ i $S$.** $\sigma$ és la desviació típica poblacional (dada del problema). $S$ és la mostral (calculada de la mostra o donada com a “desviació típica de la mostra”).
>
> **Error 2 — No dividir per $\sqrt{n}$.** L’error estàndard és $\dfrac{\sigma}{\sqrt{n}}$, no $\dfrac{\sigma}{n}$. Amb $n=36$: dividir per $\sqrt{36}=6$, no per 36.
>
> **Error 3 — Interpretar malament el nivell de confiança.** L’IC no diu que $\mu$ hi és dins amb probabilitat 95%. Diu que el mètode encerta el 95% de les vegades.
>
> **Error 4 — Confondre $z=1{,}96$ i $z=2{,}58$.** L’enunciat de selectivitat **sempre** t’indica quin valor has d’usar. Llegeix-lo amb atenció.

------------------------------------------------------------------------
