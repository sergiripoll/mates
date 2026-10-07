---
title: Estadística: intervals de confiança: Teoria
tematitol: Estadística: intervals de confiança
curs: 2n
modalitat: social
tema: estadistica
bloc: teoria
ordre: 1
---
# Estadística: intervals de confiança: Teoria

> **💡 Idea**
>
> **El problema de fons: mai coneixem el valor real de la població.**
>
> Imagina que vols saber el pes mitjà real $\mu$ de tots els estudiants d’una escola. Pesar-los tots és impossible, de manera que peses una mostra de $n$ alumnes i calcules la seva mitjana $\bar{x}$.
>
> El problema: $\bar{x}$ **no** és exactament $\mu$. Si agafessis una altra mostra diferent, obtindries un $\bar{x}$ diferent. Llavors, **on és $\mu$ exactament?**
>
> La resposta honesta és: **no ho sabem**. Però sí que podem dir: *“amb un 95% de confiança, $\mu$ es troba entre aquests dos valors”*. Això és un **interval de confiança**.

**Com es construeix un interval de confiança?**

La idea és sempre la mateixa: partim de l’estimació que tenim ($\bar{x}$ o $\hat{p}$) i li sumem i restem un **marge d’error**: $$\text{Estimació} \;\pm\; \underbrace{z_\gamma \cdot \text{(error estàndard)}}_{\text{marge d'error}}$$

On:

- $z_\gamma$ és un valor que depèn del **nivell de confiança** que volem: $$\text{Confiança 95\%} \;\Rightarrow\; z = 1{,}96
\qquad\qquad
\text{Confiança 99\%} \;\Rightarrow\; z = 2{,}58$$

- L’**error estàndard** depèn del tipus de problema (mitjana o proporció).

![](img/intervals-de-confianca-0c81e0.svg)

------------------------------------------------------------------------

**Les tres fórmules**

> **📘 Fórmula**
>
> Fórmula 1 — IC per a la mitjana amb $\sigma$ coneguda Quan el problema et dóna la desviació típica **de la població** $\sigma$: $$\bar{x}\;\pm\; z_\gamma \cdot \dfrac{\sigma}{\sqrt{n}}$$
>
> p2cm p2cm p2cm p2cm p4cm $\bar{x}$ & $z_\gamma$ & $\sigma$ & $n$ &  
> mitjana de la mostra & 1,96 (95%) o 2,58 (99%) & desv. típica de la **població** & mida de la mostra &  

> **📘 Fórmula**
>
> Fórmula 2 — IC per a la mitjana amb $\sigma$ desconeguda ($n \geq 30$) Quan el problema et dóna la desviació típica **de la mostra** $S$ i $n \geq 30$: $$\bar{x}\;\pm\; z_\gamma \cdot \dfrac{S}{\sqrt{n}}$$
>
> p2cm p2cm p2cm p2cm $\bar{x}$ & $z_\gamma$ & $S$ & $n$  
> mitjana de la mostra & 1,96 o 2,58 & desv. típica de la **mostra** & mida de la mostra  
>
> *La diferència amb la Fórmula 1 és només que $\sigma$ (poblacional) es substitueix per $S$ (mostral). La mecànica és idèntica.*

> **📘 Fórmula**
>
> Fórmula 3 — IC per a una proporció Quan volem estimar un **percentatge** (proporció) a partir d’una enquesta: $$\hat{p}\;\pm\; z_\gamma \cdot \sqrt{\dfrac{\hat{p}\,(1-\hat{p})}{n}}
\quad\text{on}\quad \hat{p}= \dfrac{k}{n}$$
>
> p2.5cm p2cm p2cm p4cm $\hat{p}= k/n$ & $z_\gamma$ & $n$ &  
> proporció mostral ($k$ = casos favorables) & 1,96 o 2,58 & mida de la mostra &  
>
> *L’arrel $\sqrt{\hat{p}(1-\hat{p})/n}$ fa el paper de $\sigma/\sqrt{n}$: és la mesura de com varia $\hat{p}$ d’una mostra a una altra.*

> **⚠️ Atenció**
>
> **Com distingir $\sigma$ de $S$ a l’enunciat:**
>
> - “la desviació típica **de la població** és $\sigma=3$” → Fórmula 1
>
> - “la desviació típica **de la mostra** és $S=3$” → Fórmula 2
>
> - “en la mostra obtenim una desviació típica de 3” → Fórmula 2
>
> - “el problema demana un percentatge / proporció” → Fórmula 3

------------------------------------------------------------------------

**Exemple 1 — Fórmula 1: Iogurts (PAU)**

> **✏️ Exemple**
>
> Els iogurts pesen realment 150 g? Pesem 10 iogurts. El pes segueix $N(\mu, 3)$ (desviació típica poblacional $\sigma=3$ coneguda). Els pesos (en grams) són: $$148,\; 149,\; 147,\; 146,\; 149,\; 146,\; 149,\; 148,\; 149,\; 149$$ Construeix un IC al 95% per a $\mu$ i determina si l’etiqueta (150 g) és errònia.
>
> **Pas 1 — Calcula $\bar{x}$:** $$\bar{x}= \frac{148+149+147+146+149+146+149+148+149+149}{10} = \frac{1480}{10} = 148$$
>
> **Pas 2 — Aplica la Fórmula 1** ($\sigma=3$, $n=10$, $z=1{,}96$): $$\bar{x}\pm z \cdot \frac{\sigma}{\sqrt{n}}
= 148 \pm 1{,}96 \cdot \frac{3}{\sqrt{10}}
= 148 \pm 1{,}96 \cdot 0{,}9487
= 148 \pm 1{,}86$$
>
> **IC al 95%:** $$\boxed{[146{,}14\;,\; 149{,}86]}$$
>
> **Conclusió:** el valor 150 g **no** pertany a l’interval $[146{,}14;\; 149{,}86]$. Per tant, amb un 95% de confiança, la informació de l’etiqueta és errònia: els iogurts contenen de mitjana menys de 150 g.

**Exemple 2 — Fórmula 2: Cafeteria (PAU)**

> **✏️ Exemple**
>
> Quant gasta l’alumnat a la cafeteria? Una mostra de 250 estudiants dóna una despesa setmanal mitjana de $\bar{x}= 5$ € amb desviació típica **mostral** $S = 1{,}5$ €. Construeix un IC al 95% i un altre al 99%.
>
> **Pas 1 — Identifica les dades:** $n=250$, $\bar{x}=5$, $S=1{,}5$. Com que $\sigma$ és *desconeguda* però $n=250\geq30$, usem la Fórmula 2.
>
> **Pas 2 — Error estàndard:** $$\frac{S}{\sqrt{n}} = \frac{1{,}5}{\sqrt{250}} = \frac{1{,}5}{15{,}81} = 0{,}0949$$
>
> **IC al 95%** ($z=1{,}96$): $$5 \pm 1{,}96 \cdot 0{,}0949 = 5 \pm 0{,}186 \quad\Rightarrow\quad \boxed{[4{,}81\;,\; 5{,}19]}$$
>
> **IC al 99%** ($z=2{,}58$): $$5 \pm 2{,}58 \cdot 0{,}0949 = 5 \pm 0{,}245 \quad\Rightarrow\quad \boxed{[4{,}76\;,\; 5{,}25]}$$
>
> **Observació:** l’IC al 99% és més ample que el del 95% perquè $z$ és més gran ($2{,}58 > 1{,}96$): multipliquem el mateix error estàndard per un número més gran.

**Exemple 3 — Fórmula 3: Enquesta (PAU)**

> **✏️ Exemple**
>
> Quants estudiants usen el transport públic? En una enquesta a 400 estudiants, 180 afirmen que usen el transport públic. Construeix un IC al 95% per al percentatge real.
>
> **Pas 1 — Estimació puntual:** $$\hat{p}= \frac{k}{n} = \frac{180}{400} = 0{,}45 \quad\Rightarrow\quad 45\%$$
>
> **Pas 2 — Error estàndard:** $$\sqrt{\frac{\hat{p}(1-\hat{p})}{n}} = \sqrt{\frac{0{,}45 \cdot 0{,}55}{400}} = \sqrt{0{,}000619} = 0{,}0249$$
>
> **Pas 3 — IC al 95%** ($z=1{,}96$): $$0{,}45 \pm 1{,}96 \cdot 0{,}0249 = 0{,}45 \pm 0{,}049 \quad\Rightarrow\quad \boxed{[40{,}1\%\;,\; 49{,}9\%]}$$
>
> **Conclusió:** el 50% **no** pertany a $[40{,}1\%;\; 49{,}9\%]$. Un estudi anterior que afirmés que el 50% dels estudiants usen transport públic no seria compatible amb les nostres dades.

------------------------------------------------------------------------

**Exemple 4 — Les 100 monedes: quan l’IC té menys sentit**

> **💡 Nota**
>
> Aquest exemple és diferent dels anteriors. Aquí sabem d’antemà que $p=0{,}5$ (la moneda és equilibrada). Llavors, **quin sentit té construir un IC?** Cap, en la vida real. Però serveix per entendre *visualment* què fa un IC: ens mostra el rang de valors de $p$ compatibles amb el resultat obtingut.

> **✏️ Exemple**
>
> 100 monedes, 60 cares: l’IC i la decisió Llencem una moneda 100 vegades. Obtenim **60 cares**. Construïm un IC per a la proporció real de cares $p$.
>
> **Estimació puntual:** $\hat{p}= 60/100 = 0{,}60$
>
> **Error estàndard:** $$\sqrt{\frac{0{,}60 \cdot 0{,}40}{100}} = \sqrt{0{,}0024} = 0{,}049$$
>
> **IC al 95%** ($z=1{,}96$): $$0{,}60 \pm 1{,}96 \cdot 0{,}049 = 0{,}60 \pm 0{,}096 \quad\Rightarrow\quad \boxed{[50{,}4\%\;,\; 69{,}6\%]}$$
>
> **IC al 99%** ($z=2{,}58$): $$0{,}60 \pm 2{,}58 \cdot 0{,}049 = 0{,}60 \pm 0{,}126 \quad\Rightarrow\quad \boxed{[47{,}4\%\;,\; 72{,}6\%]}$$
>
> **Visualització:**
>
> ![](img/intervals-de-confianca-d65fa8.svg)
>
> | **Interval**                     | **Conté $p=0{,}5$?** |                  **Conclusió**                   |
> |:---------------------------------|:--------------------:|:------------------------------------------------:|
> | IC 95%: $[50{,}4\%;\; 69{,}6\%]$ |        **No**        |        Al 95%, la moneda *sembla* trucada        |
> | IC 99%: $[47{,}4\%;\; 72{,}6\%]$ |        **Sí**        | Al 99%, no podem descartar que sigui equilibrada |
>
> **Per entendre-ho millor:** amb la distribució binomial havíem calculat que $P(X \geq 60) \approx 2{,}84\%$ quan $p=0{,}5$. Aquesta probabilitat és menor del 5%, i per això l’IC al 95% exclou just $p=0{,}5$. Els dos raonaments diuen el mateix: 60 cares és un resultat inusual per a una moneda equilibrada, però no impossible.

------------------------------------------------------------------------

**Interpretació correcta**

> **⚠️ Atenció**
>
> **Incorrecte:** “La probabilitat que $\mu$ estigui dins l’IC és del 95%”.
>
> $\mu$ és un valor fix que no canvia. O hi és dins, o no. No té probabilitat.
>
> **Correcte:** “Si repetíssim el mostreig moltes vegades, el 95% dels intervals construïts contindrien $\mu$”.
>
> **La metàfora:** $\mu$ és el centre fix d’una diana. Cada mostra llença un dard ($\bar{x}$) i construïm un cercle al voltant d’on ha caigut. Un IC al 95% vol dir que 95 de cada 100 dards cauen prou a prop del centre perquè el seu cercle el contingui.

------------------------------------------------------------------------

**Resum de les tres fórmules**

|                                                                            | **Situació**                             | **Fórmula**                                                                  | **Com identificar-la**                             |
|:---------------------------------------------------------------------------|:-----------------------------------------|:-----------------------------------------------------------------------------|:---------------------------------------------------|
| **F1**                                                                     | Mitjana, $\sigma$ coneguda               | $\displaystyle\bar{x}\pm z_\gamma \cdot \frac{\sigma}{\sqrt{n}}$             | El problema dona $\sigma$                          |
| **F2**                                                                     | Mitjana, $\sigma$ desconeguda, $n\geq30$ | $\displaystyle\bar{x}\pm z_\gamma \cdot \frac{S}{\sqrt{n}}$                  | El problema dona $S$ o “desv. típica de la mostra” |
| **F3**                                                                     | Proporció / percentatge                  | $\displaystyle\hat{p}\pm z_\gamma \cdot \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$ | Pregunten un % o una proporció                     |
| $z_\gamma = 1{,}96$ per al 95% $\qquad\qquad z_\gamma = 2{,}58$ per al 99% |                                          |                                                                              |                                                    |
