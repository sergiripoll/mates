---
title: Funcions, límits i continuïtat: Teoria
tematitol: Funcions, límits i continuïtat
curs: 2n
modalitat: social
tema: limits
bloc: teoria
ordre: 1
---
# Funcions, límits i continuïtat: Teoria

## Domini i recorregut d’una funció

> **📘 Teoria**
>
> Una funció $f$ associa a cada valor $x$ d’un conjunt un únic valor $y=f(x)$.
>
> - **Domini** $\operatorname{Dom} f$: tots els valors de $x$ per als quals existeix $f(x)$ (és a dir, per als quals la funció "es pot calcular").
>
> - **Recorregut** (o imatge) $\operatorname{Im} f$: tots els valors $y=f(x)$ que la funció realment pren.
>
> Per trobar el domini cal fixar-se en les operacions "perilloses":
>
> - Denominadors: no es pot dividir per $0$.
>
> - Arrels d’índex parell: el radicand ha de ser $\ge 0$.
>
> - Logaritmes: l’argument ha de ser $>0$ (es veurà més endavant).
>
> Per trobar el recorregut sol ser útil dibuixar (o imaginar) la gràfica de la funció.

### Funció constant

> **📘 Teoria**
>
> $$f(x)=k, \qquad k\in\mathbb{R}$$ Sigui quin sigui el valor de $x$, la imatge sempre val $k$. La gràfica és una recta horitzontal. $$\operatorname{Dom} f=\mathbb{R}=(-\infty,+\infty), \qquad \operatorname{Im} f=\{k\}$$

> **✏️ Exemple**
>
> $f(x)=7$. Per a qualsevol $x$, $f(x)=7$. $\operatorname{Dom} f=\mathbb{R}$, $\operatorname{Im} f=\{7\}$.

### Funció lineal i funció afí

> **📘 Teoria**
>
> **Funció lineal:** $f(x)=mx$. Totes tallen l’eix $Y$ al punt $(0,0)$.
>
> **Funció afí:** $f(x)=mx+n$ (funció lineal $+$ terme independent $n$). Talla l’eix d’ordenades a $(0,n)$.
>
> El nombre $m$ és el **pendent**: indica la inclinació de la recta i coincideix amb la **derivada** de la funció, $f'(x)=m$ (constant per a tota recta): $$\begin{cases}
m>0 \ \Rightarrow\ \text{funció creixent} \\
m<0 \ \Rightarrow\ \text{funció decreixent} \\
m=0 \ \Rightarrow\ \text{funció constant}
\end{cases}$$ $$\operatorname{Dom} f=\mathbb{R}, \qquad \operatorname{Im} f=\mathbb{R} \quad (\text{si } m\neq 0)$$

> **✏️ Exemple**
>
> $f(x)=3x$: pendent $m=3>0\Rightarrow$ creixent, $f'(x)=3$.
>
> $f(x)=3x+4$: la mateixa inclinació que l’anterior, però desplaçada: talla l’eix $Y$ a $(0,4)$.

### Funció quadràtica

> **📘 Teoria**
>
> $$f(x)=ax^2+bx+c, \qquad a\neq 0$$ La gràfica és una **paràbola**.
>
> - Si $a>0$: paràbola oberta cap amunt $\Rightarrow$ té un **mínim**.
>
> - Si $a<0$: paràbola oberta cap avall $\Rightarrow$ té un **màxim**.
>
> El **vèrtex** (màxim o mínim) es troba a: $$x_v=-\frac{b}{2a}, \qquad y_v=f(x_v)$$ Abans del vèrtex la funció és decreixent (si $a>0$) o creixent (si $a<0$); després, al revés.
>
> $$\operatorname{Dom} f=\mathbb{R}$$ $$\operatorname{Im} f=[y_v,+\infty) \ \text{ si } a>0, \qquad \operatorname{Im} f=(-\infty,y_v] \ \text{ si } a<0$$

> **✏️ Exemple**
>
> $f(x)=x^2+4$. Com que $a=1>0$, hi ha un mínim a $x_v=-\dfrac{0}{2}=0$, $f(0)=4$.
>
> Vèrtex $(0,4)$: abans decreix, després creix. $$\operatorname{Dom} f=\mathbb{R}, \qquad \operatorname{Im} f=[4,+\infty)$$
>
> ![](img/limits-funcions-22c9a2.svg)

> **💡 Per aprofundir**
>
> Una empresa ven un producte i el seu benefici (en milers d’€) segons el nombre $x$ de unitats produïdes ve donat per $B(x)=-2x^2+40x-150$. Troba el nombre d’unitats que maximitza el benefici i quin és el benefici màxim. Per a quins valors de $x$ l’empresa té pèrdues?

### Funcions polinòmiques

> **📘 Teoria**
>
> Una funció polinòmica és de la forma $$f(x)=a_nx^n+a_{n-1}x^{n-1}+\dots+a_1x+a_0$$ Sigui quin sigui el grau, **tots els polinomis tenen domini** $\operatorname{Dom} f=\mathbb{R}$ (no hi ha denominadors ni arrels). El recorregut pot variar segons el grau i la forma concreta del polinomi.

> **✏️ Exemple**
>
> $f(x)=(x-1)(x-2)x=x^3-3x^2+2x$. És un polinomi de grau $3$, per tant $\operatorname{Dom} f=\mathbb{R}$. Les seves arrels (punts de tall amb l’eix $X$) són $x=0,1,2$.

### Funcions amb radicals

> **📘 Teoria**
>
> $$f(x)=\sqrt[n]{g(x)}$$
>
> - Si $n$ és **parell**: el radicand ha de ser $\geq 0$. Cal resoldre $g(x)\geq 0$. $$\operatorname{Dom} f=\{x: g(x)\geq 0\}$$ A més, com que una arrel parell dona sempre un resultat $\geq 0$, $\operatorname{Im} f\subseteq [0,+\infty)$.
>
> - Si $n$ és **imparell**: no hi ha cap limitació sobre el radicand. $$\operatorname{Dom} f=\mathbb{R}, \qquad \operatorname{Im} f=\mathbb{R}$$

> **✏️ Exemple**
>
> $f(x)=\sqrt{x+3}$ (índex parell): cal $x+3\geq 0 \Rightarrow x\geq -3$. $$\operatorname{Dom} f=[-3,+\infty)$$ $g(x)=\sqrt[3]{x+3}$ (índex imparell): no hi ha restricció. $$\operatorname{Dom} g=\mathbb{R}$$

### Funcions racionals

> **📘 Teoria**
>
> Una funció racional és un quocient de polinomis: $$f(x)=\frac{p(x)}{q(x)}$$ El **domini** exclou els valors que anul·len el denominador: $$\operatorname{Dom} f=\mathbb{R}\setminus\{x: q(x)=0\}$$ En aquests punts "prohibits" la funció sol presentar **asímptotes verticals**. Si el grau del numerador $\leq$ grau del denominador i el quocient dels coeficients principals dona un valor finit, la funció pot tenir una **asímptota horitzontal**.

> **✏️ Exemple**
>
> $$f(x)=\frac{1}{x-5}$$ El denominador s’anul·la a $x=5\Rightarrow \operatorname{Dom} f=\mathbb{R}\setminus\{5\}$.
>
> Estudiem què passa a prop de $x=5$ i quan $x\to\pm\infty$: $$\lim_{x\to 5^-}f(x)=-\infty, \qquad \lim_{x\to 5^+}f(x)=+\infty \quad\Rightarrow\quad \text{A.V. } x=5$$ $$\lim_{x\to \pm\infty}f(x)=0 \quad\Rightarrow\quad \text{A.H. } y=0$$
>
> ![](img/limits-funcions-2a94d4.svg)

## Límits

> **📘 Teoria**
>
> El **límit** d’una funció $f$ quan $x$ tendeix a un valor $a$, $\displaystyle\lim_{x\to a}f(x)$, és el valor cap al qual s’acosten les imatges $f(x)$ quan $x$ s’acosta a $a$ (sense necessàriament arribar-hi).

### Límits laterals

> **📘 Teoria**
>
> - **Límit per l’esquerra**: $\displaystyle\lim_{x\to a^-}f(x)$ (valors de $x$ menors que $a$, acostant-s’hi).
>
> - **Límit per la dreta**: $\displaystyle\lim_{x\to a^+}f(x)$ (valors de $x$ majors que $a$, acostant-s’hi).
>
> Aquest càlcul és imprescindible en **funcions definides a trossos**, on cal comprovar què passa a banda i banda del punt d’unió.

> **✏️ Exemple**
>
> $$f(x)=\begin{cases} 3x & x<2 \\ x+1 & x\geq 2 \end{cases}$$ $$\lim_{x\to 2^-}f(x)=\lim_{x\to 2^-}3x=6, \qquad \lim_{x\to 2^+}f(x)=\lim_{x\to 2^+}(x+1)=3$$ Com que $6\neq 3$, el límit $\displaystyle\lim_{x\to 2}f(x)$ **no existeix**.

### Límits a l’infinit. Asímptotes

> **📘 Teoria**
>
> Quan $x\to\pm\infty$, estudiem cap a quin valor s’acosta $f(x)$:
>
> - Si $\displaystyle\lim_{x\to\pm\infty}f(x)=L$ (finit) $\Rightarrow$ hi ha una **asímptota horitzontal** $y=L$.
>
> - Si $\displaystyle\lim_{x\to a}f(x)=\pm\infty$ (amb $a$ finit) $\Rightarrow$ hi ha una **asímptota vertical** $x=a$.

> **✏️ Exemple**
>
> $$f(x)=\frac{1}{x^2-5x+4}$$ El denominador s’anul·la a $x=1$ i $x=4\Rightarrow$ possibles A.V. Comprovem-ho: $$\lim_{x\to 1^-}f(x)=+\infty \quad (\text{el denominador s'acosta a } 0^+)$$ Com que $\displaystyle\lim_{x\to\pm\infty}f(x)=0$ (grau del denominador $>$ grau del numerador), hi ha A.H. $y=0$.

### Indeterminacions

> **📘 Teoria**
>
> En calcular límits sovint apareixen expressions sense un valor determinat a priori, anomenades **indeterminacions**. Les més habituals en aquest curs són: $$\frac{0}{0}, \qquad \frac{\infty}{\infty}, \qquad \infty-\infty$$ Estratègies típiques per resoldre-les:
>
> - $\dfrac{0}{0}$ en funcions racionals: **factoritzar** numerador i denominador i simplificar.
>
> - $\dfrac{\infty}{\infty}$ en funcions racionals: dividir numerador i denominador per la potència més gran de $x$, o comparar directament els graus.

> **✏️ Exemple**
>
> $$\lim_{x\to 3}\frac{2x+5}{x^3-16}\Bigg|_{\text{comprovem}} \qquad \text{amb } \lim_{x\to 3}\frac{x^2-9}{x-3}$$ Substituint directament $x=3$ obtenim $\dfrac{0}{0}$ (indeterminació). Factoritzem: $$\lim_{x\to 3}\frac{x^2-9}{x-3}=\lim_{x\to 3}\frac{(x-3)(x+3)}{x-3}=\lim_{x\to 3}(x+3)=6$$

## Continuïtat

> **📘 Teoria**
>
> Una funció $f$ és **contínua** en $x=a$ si es compleixen tres condicions:
>
> 1.  Existeix $f(a)$ (el punt pertany al domini).
>
> 2.  Existeix $\displaystyle\lim_{x\to a}f(x)$ (els límits laterals coincideixen).
>
> 3.  $\displaystyle\lim_{x\to a}f(x)=f(a)$.
>
> Si no es compleix alguna d’aquestes tres condicions, la funció és **discontínua** a $x=a$.

### Tipus de discontinuïtat

> **📘 Teoria**
>
> - **Evitable**: existeix $\displaystyle\lim_{x\to a}f(x)$ però no coincideix amb $f(a)$, o bé $f(a)$ no existeix (un "forat" a la gràfica).
>
> - **De salt finit**: existeixen els límits laterals però són diferents entre si.
>
> - **De salt infinit (asimptòtica)**: algun dels límits laterals val $+\infty$ o $-\infty$ (asímptota vertical).

> **✏️ Exemple**
>
> $$f(x)=\frac{x^2-16}{x-4}$$ Simplificant: $f(x)=x+4$ per a $x\neq 4$, però $f(4)$ no existeix (denominador $0$). $$\lim_{x\to 4}f(x)=8 \quad \text{però } f(4) \text{ no existeix} \Rightarrow \text{discontinuïtat evitable a } x=4$$
>
> Funcions elementals com les polinòmiques, racionals (fora dels punts que anul·len el denominador) i les radicals (dins del seu domini) són **contínues** allà on estan definides.

### Continuïtat de funcions definides a trossos

> **📘 Teoria**
>
> Quan una funció es defineix per trossos, cal comprovar la continuïtat **només** en els punts on canvia de tros (els altres trams, si són polinòmics, racionals, etc., ja són continus dins del seu interval). El procediment és:
>
> 1.  Calcular $\displaystyle\lim_{x\to a^-}f(x)$ substituint a l’expressió vàlida per $x<a$.
>
> 2.  Calcular $\displaystyle\lim_{x\to a^+}f(x)$ substituint a l’expressió vàlida per $x>a$.
>
> 3.  Calcular $f(a)$ amb l’expressió que inclou el propi punt $a$.
>
> 4.  Comprovar si els tres valors coincideixen.
>
> Sovint aquest procediment serveix també per trobar un paràmetre desconegut que faci contínua la funció (igualant els dos límits laterals).

> **✏️ Exemple**
>
> $$P(t)=\begin{cases} 5(t+1)^2-5 & 0\leq t\leq 2\\ -4t+48 & 2<t\leq 10\end{cases}$$ Comprovem la continuïtat a $t=2$: $$\lim_{t\to 2^-}5(t+1)^2-5=5\cdot 9-5=40, \qquad \lim_{t\to 2^+}(-4t+48)=-8+48=40$$ Com que els dos límits laterals coincideixen (i valen el mateix que $P(2)$, calculat amb la primera expressió), la funció **és contínua** a $t=2$: el gràfic no fa cap salt en el moment d’enllaçar els dos trams.

## Resum final

> **📘 Teoria**
>
> - El **domini** depèn del tipus de funció: polinomis $\to\mathbb{R}$; racionals $\to$ excloure zeros del denominador; arrels parells $\to$ radicand $\geq 0$.
>
> - Un **límit** existeix si i només si els límits laterals coincideixen; els límits a l’infinit donen les asímptotes horitzontals, i els límits infinits en un punt finit donen les asímptotes verticals.
>
> - Una funció és **contínua** en un punt si hi existeix, hi té límit, i aquest límit coincideix amb el valor de la funció; en funcions a trossos cal comprovar-ho sempre en els punts d’unió.
>
> - La **derivada** és el pendent de la recta tangent i indica el creixement ($f'>0$), el decreixement ($f'<0$) o els possibles extrems ($f'=0$).
>
> - En els problemes d’**optimització**: plantejar la funció, reduir-la a una variable amb el lligam, derivar, igualar a zero, i comprovar que la solució té sentit dins del context del problema.
