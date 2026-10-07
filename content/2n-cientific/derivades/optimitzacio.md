---
title: Optimització: aplicacions de la derivada
curs: 2n
modalitat: cientific
tema: derivades
tipus: exercicis
---
# Optimització: aplicacions de la derivada

## Àrees màximes i mínimes

### Triangle d’àrea màxima sota $y = x^2 e^{-x}$

> **📝 Enunciat**
>
> Calcula l’àrea màxima d’un triangle rectangle amb un vèrtex a l’origen, un costat sobre l’eix $OX$ i el vèrtex oposat sobre la corba $y = x^2 e^{-x}$ per $x \geq 0$.

#### Pas 1 — Planteja l’àrea

Un triangle de base $x$ i altura $y = x^2 e^{-x}$ té àrea: $$A = \frac{1}{2} \cdot x \cdot y = \frac{1}{2} \cdot x \cdot x^2 e^{-x} = \frac{1}{2} x^3 e^{-x}, \qquad \text{Dom } A = [0, +\infty)$$

#### Pas 2 — Valors als extrems del domini

$$A(0) = 0, \qquad A(+\infty) = \lim_{x\to+\infty} \frac{x^3}{2e^x} = 0$$ Per tant hi ha un màxim interior.

#### Pas 3 — Derivada i punt crític

$$A'(x) = \frac{1}{2}\left(3x^2 e^{-x} - x^3 e^{-x}\right) = \frac{1}{2} e^{-x}\left(3x^2 - x^3\right) = \frac{x^2 e^{-x}}{2}(3 - x)$$

$A'(x) = 0 \implies x^2(3-x) = 0 \implies x = 0$ (mínim) o $\boxed{x = 3}$ (màxim, ja que $A' > 0$ si $x<3$ i $A'<0$ si $x>3$).

#### Pas 4 — Àrea màxima

$$A(3) = \frac{1}{2} \cdot 3^3 \cdot e^{-3} = \frac{27}{2e^3} \approx 0{,}67 \text{ u}^2$$

> **📘 Resultat**
>
> L’àrea màxima del triangle és $$\boxed{A_{\max} = \frac{27}{2e^3} \approx 0{,}67 \text{ u}^2}$$ obtinguda en $x = 3$.

### Rectangle inscrit en un semicercle de radi 10

> **📝 Enunciat**
>
> Un semicercle té radi $r = 10$ m. Calcula les dimensions del rectangle inscrit d’àrea màxima.

#### Pas 1 — Relació entre $x$ i $y$

El semicercle satisfà $x^2 + y^2 = 100$ (amb $y \geq 0$), de manera que: $$y = \sqrt{100 - x^2}$$

#### Pas 2 — Funció àrea

El rectangle té base $2x$ i altura $y$: $$A = 2xy = 2x\sqrt{100 - x^2}, \qquad x \in [0, 10]$$

#### Pas 3 — Derivada

$$A' = 2\sqrt{100-x^2} + 2x \cdot \frac{-x}{\sqrt{100-x^2}} = \frac{2(100-x^2) - 2x^2}{\sqrt{100-x^2}} = \frac{200 - 4x^2}{\sqrt{100-x^2}}$$

$A' = 0 \implies 200 - 4x^2 = 0 \implies x^2 = 50 \implies x = 5\sqrt{2} \approx 7{,}07$ m

#### Pas 4 — Dimensions

$$y = \sqrt{100 - 50} = \sqrt{50} = 5\sqrt{2} \approx 7{,}07 \text{ m}$$

> **📘 Resultat**
>
> El rectangle d’àrea màxima és un **quadrat** de costat $5\sqrt{2}$ m: $$\text{Base} = 2x = 10\sqrt{2} \approx 14{,}14 \text{ m}, \qquad \text{Altura} = 5\sqrt{2} \approx 7{,}07 \text{ m}$$ $$\boxed{A_{\max} = 100 \text{ m}^2}$$

### Rectangle inscrit en un triangle ($x + y = 8$)

> **📝 Enunciat**
>
> Troba les dimensions del rectangle inscrit en el triangle de vèrtexs $O(0,0)$, $(8,0)$ i $(0,8)$ (recta $x + y = 8$) que té superfície màxima.

#### Pas 1 — Variables

Sigui $k$ l’alçada del rectangle. El costat superior toca la recta $y = -x + 8$, de manera que quan $y = k$ tenim $x = 8 - k$.

El rectangle té base $b = 8 - k$ i altura $h = k$: $$A = (8 - k) \cdot k = -k^2 + 8k, \qquad k \in [0, 4]$$

(La restricció $k \leq 4$ prové de la simetria; el domini natural és $[0,8]$ però el màxim és interior.)

#### Pas 2 — Derivada i punt crític

$$A' = -2k + 8 = 0 \implies k = 4$$

Com que $A'' = -2 < 0$, és un màxim.

#### Pas 3 — Àrea màxima

$$A(4) = -16 + 32 = 8$$

> **📘 Resultat**
>
> Les dimensions del rectangle d’àrea màxima són: $$\text{base} = 8 - 4 = 4, \quad \text{altura} = 4$$ $$\boxed{A_{\max} = 8 \text{ u}^2}$$

### Rectangle inscrit sota $y = \sqrt{1-x}$

> **📝 Enunciat**
>
> Calcula l’àrea màxima d’un rectangle inscrit al primer quadrant sota la corba $y = \sqrt{1-x}$, amb un vèrtex a l’origen i el vèrtex oposat sobre la corba.

#### Pas 1 — Funció àrea

El rectangle té base $k$ i altura $y = \sqrt{1-k}$: $$A(k) = k \cdot \sqrt{1-k} = k(1-k)^{1/2}, \qquad k \in [0, 1]$$

#### Pas 2 — Intersecció $y = x$ amb $y = \sqrt{1-x}$

Per trobar el punt on es creuen les dues corbes usem $x = \sqrt{1-x}$, d’on $x^2 = 1-x$, és a dir $x^2 + x - 1 = 0$: $$x = \frac{-1 + \sqrt{5}}{2} \approx 0{,}618$$

#### Pas 3 — Derivada i punt crític

$$A'(k) = (1-k)^{1/2} + k \cdot \frac{-1}{2}(1-k)^{-1/2} = \frac{(1-k) - \frac{k}{2}}{\sqrt{1-k}} = \frac{1 - \frac{3k}{2}}{\sqrt{1-k}}$$

$A' = 0 \implies 1 - \dfrac{3k}{2} = 0 \implies \boxed{k = \dfrac{2}{3}}$

#### Pas 4 — Àrea màxima

$$A\!\left(\tfrac{2}{3}\right) = \frac{2}{3}\sqrt{1 - \frac{2}{3}} = \frac{2}{3} \cdot \frac{1}{\sqrt{3}} = \frac{2}{3\sqrt{3}} = \frac{2\sqrt{3}}{9}$$

> **📘 Resultat**
>
> $$\boxed{A_{\max} = \frac{2\sqrt{3}}{9} \approx 0{,}385 \text{ u}^2}$$ obtinguda en $k = \dfrac{2}{3}$.

## Distàncies mínimes

### Distància mínima del punt $P(0,2)$ a la paràbola $y = 4 - x^2$

> **📝 Enunciat**
>
> Troba el punt (o els punts) de la paràbola $y = 4 - x^2$ més proper(s) al punt $P(0, 2)$.

#### Pas 1 — Funció distància

Un punt genèric de la paràbola és $(x, 4-x^2)$. La distància a $P(0,2)$ és: $$D = \sqrt{x^2 + (4 - x^2 - 2)^2} = \sqrt{x^2 + (2 - x^2)^2} = \sqrt{x^4 - 3x^2 + 4}$$

Minimitzem $u = D^2 = x^4 - 3x^2 + 4$ (equivalent, ja que $D$ és creixent).

#### Pas 2 — Derivada i punts crítics

$$u' = 4x^3 - 6x = 2x(2x^2 - 3) = 0$$

$$x = 0 \qquad \text{o} \qquad x^2 = \frac{3}{2} \implies x = \pm\sqrt{\frac{3}{2}}$$

#### Pas 3 — Classificació dels punts crítics

| $x$  | $-\sqrt{3/2}$ |            |    $0$    |            | $+\sqrt{3/2}$ |
|:----:|:-------------:|:----------:|:---------:|:----------:|:-------------:|
| $u'$ |      $0$      |    $+$     |    $0$    |    $+$     |      $0$      |
| $u$  |      mín      | $\nearrow$ | màx local | $\nearrow$ |      mín      |

$$u(0) = 4 \quad \text{(màxim local)}, \qquad u\!\left(\sqrt{\tfrac{3}{2}}\right) = \frac{9}{4} - \frac{9}{2} + 4 = \frac{7}{4}$$

#### Pas 4 — Punts més propers

Els punts de la paràbola més propers a $P$ corresponen a $x = \pm\sqrt{3/2}$: $$y = 4 - \frac{3}{2} = \frac{5}{2}$$

> **📘 Resultat**
>
> Els dos punts de la paràbola més propers a $P(0,2)$ són: $$\boxed{\left(\pm\sqrt{\frac{3}{2}},\; \frac{5}{2}\right)}$$ amb distància mínima $D_{\min} = \dfrac{\sqrt{7}}{2}$.

## Triangles d’àrea mínima

### Recta per $A(4,3)$: triangle d’àrea mínima al primer quadrant

> **📝 Enunciat**
>
> Calcula l’equació de la recta que passa per $A(4,3)$ i determina, en el primer quadrant, un triangle d’àrea mínima.

#### Pas 1 — Planteja la recta i els talls amb els eixos

Una recta per $A(4,3)$ amb pendent $m$ talla l’eix $OX$ en el punt $(a, 0)$ i l’eix $OY$ en $(0, b)$. Per semblança de triangles: $$\frac{a-4}{a} = \frac{3}{b} \implies b = \frac{3a}{a-4}, \qquad \text{Dom } A = (4, +\infty)$$

#### Pas 2 — Funció àrea

$$A = \frac{1}{2} a \cdot b = \frac{1}{2} \cdot a \cdot \frac{3a}{a-4} = \frac{3a^2}{2(a-4)}$$

#### Pas 3 — Derivada i punt crític

Regla del quocient: $$A' = \frac{3}{2} \cdot \frac{2a(a-4) - a^2}{(a-4)^2} = \frac{3}{2} \cdot \frac{a^2 - 8a}{(a-4)^2} = \frac{3a(a-8)}{2(a-4)^2}$$

$A' = 0 \implies a(a-8) = 0 \implies a = 0$ (fora del domini) o $\boxed{a = 8}$.

Com que $A' < 0$ per $a \in (4,8)$ i $A' > 0$ per $a > 8$, $a = 8$ és un mínim.

#### Pas 4 — Dimensions i equació de la recta

$$a = 8, \qquad b = \frac{3 \cdot 8}{8 - 4} = \frac{24}{4} = 6$$

La recta passa per $(8, 0)$ i $(0, 6)$, per tant el pendent és: $$m = \frac{6 - 0}{0 - 8} = -\frac{3}{4}$$ Equació punt-pendent passant per $(4,3)$: $$y - 3 = -\frac{3}{4}(x - 4) \implies \boxed{y = -\frac{3}{4}x + 6}$$

> **📘 Resultat**
>
> La recta d’àrea mínima és $y = -\dfrac{3}{4}x + 6$, amb: $$A_{\min} = \frac{3 \cdot 64}{2 \cdot 4} = \frac{3 \cdot 64}{8} = 24 \text{ u}^2$$

## Volums màxims

### Con de generatriu $\sqrt{6}$: volum màxim

> **📝 Enunciat**
>
> De tots els cons de generatriu $\sqrt{6}$, calcula el radi i l’alçada del con de volum màxim.

#### Pas 1 — Relació entre $r$ i $h$

La generatriu $l = \sqrt{6}$ satisfà: $$r^2 + h^2 = l^2 = 6 \implies h^2 = 6 - r^2 \implies h = \sqrt{6 - r^2}$$

#### Pas 2 — Funció volum

$$V(r) = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi r^2 \sqrt{6 - r^2}, \qquad r \in [0, \sqrt{6}]$$

#### Pas 3 — Derivada i punt crític

$$V'(r) = \frac{\pi}{3}\left(2r\sqrt{6-r^2} + r^2 \cdot \frac{-r}{\sqrt{6-r^2}}\right) = \frac{\pi}{3} \cdot \frac{r\left(2(6-r^2) - r^2\right)}{\sqrt{6-r^2}} = \frac{\pi r(12 - 3r^2)}{3\sqrt{6-r^2}}$$

$V' = 0 \implies 12 - 3r^2 = 0 \implies r^2 = 4 \implies \boxed{r = 2}$

#### Pas 4 — Alçada i volum

$$h = \sqrt{6 - 4} = \sqrt{2}, \qquad V_{\max} = \frac{\pi \cdot 4 \cdot \sqrt{2}}{3} = \frac{4\pi\sqrt{2}}{3}$$

Comprovació: $h^2 = 2r^2$, és a dir $\sqrt{2} \cdot r = h$ (relació característica del con de volum màxim).

> **📘 Resultat**
>
> $$\boxed{r = 2, \quad h = \sqrt{2}, \quad V_{\max} = \frac{4\pi\sqrt{2}}{3}}$$

### Triangle isòsceles inscrit en una circumferència de radi 3

> **📝 Enunciat**
>
> (Pàg. 153) Calcula les dimensions del triangle isòsceles inscrit en una circumferència de radi 3 que té àrea màxima.

#### Pas 1 — Planteja l’àrea

Sigui $x$ la meitat de la base del triangle i $y$ l’alçada. Per Pitàgores (el centre de la circumferència dista $3-y+3 = \ldots$), la relació és:

Sigui $h$ l’alçada total del triangle. El centre dista $3$ de cada vèrtex. La meitat de la base és $x$ i la relació és: $$x^2 + (h - 3)^2 = 9 \implies x^2 = 9 - (h-3)^2$$

L’àrea del triangle: $$A(h) = \frac{1}{2} \cdot 2x \cdot h = xh = h\sqrt{9 - (h-3)^2}$$ Simplificant $(h-3)^2 = h^2 - 6h + 9$: $$A(h) = h\sqrt{6h - h^2} = h\sqrt{h(6-h)}, \qquad h \in (0, 6)$$

#### Pas 2 — Treballem amb $A^2$ per simplificar

$$u = A^2 = h^2(6h - h^2) = 6h^3 - h^4$$ $$u' = 18h^2 - 4h^3 = 2h^2(9 - 2h) = 0 \implies h = 0 \text{ o } \boxed{h = \frac{9}{2}}$$

#### Pas 3 — Dimensions

$$x^2 = 9 - \left(\frac{9}{2} - 3\right)^2 = 9 - \frac{9}{4} = \frac{27}{4} \implies x = \frac{3\sqrt{3}}{2}$$ Base $= 2x = 3\sqrt{3}$, Alçada $= \dfrac{9}{2}$.

> **📘 Resultat**
>
> $$\text{Base} = 3\sqrt{3} \approx 5{,}20 \text{ u}, \qquad \text{Alçada} = \frac{9}{2} = 4{,}5 \text{ u}$$ $$\boxed{A_{\max} = \frac{27\sqrt{3}}{4} \approx 11{,}69 \text{ u}^2}$$

## Problemes de cost i sumes

### Suma mínima amb la condició $xy = 128$

> **📝 Enunciat**
>
> (Pàg. 162, Ex. 63) Dos nombres positius $x$ i $y$ compleixen $xy = 128$. Minimitza la suma $$S = \frac{x}{4} + \frac{y}{2}.$$

#### Pas 1 — Substitució

De $xy = 128$ s’obté $y = \dfrac{128}{x}$: $$S(x) = \frac{x}{4} + \frac{128}{2x} = \frac{x}{4} + \frac{64}{x}, \qquad x > 0$$

#### Pas 2 — Derivada i punt crític

$$S'(x) = \frac{1}{4} - \frac{64}{x^2} = 0 \implies x^2 = 256 \implies \boxed{x = 16}$$

$S''(x) = \dfrac{128}{x^3} > 0$, per tant és un mínim.

#### Pas 3 — Valors òptims

$$y = \frac{128}{16} = 8, \qquad S_{\min} = \frac{16}{4} + \frac{8}{2} = 4 + 4 = 8$$

> **📘 Resultat**
>
> $$\boxed{x = 16, \quad y = 8, \quad S_{\min} = 8}$$

### Caixa de cost mínim (Ex. 65)

> **📝 Enunciat**
>
> (Pàg. 162, Ex. 65) Es vol construir una caixa rectangular sense tapa, de volum $V = 18$ m$^3$, amb base quadrada de costat $a$ i alçada $c = 2$ m. El cost de la base és el doble del cost de les parets laterals. Calcula les dimensions que minimitzen el cost.

#### Pas 1 — Funció cost

Àrea base $= a^2$, àrea 4 cares laterals $= 4 \cdot a \cdot c$.

Suposant cost unitari lateral $= 1$ i cost base $= 2$: $$\text{Cost total} = A(a,c) = 2a^2 + 4ac$$

#### Pas 2 — Restricció de volum

$$V = a^2 c = 18 \implies c = \frac{18}{a^2}$$

Substituïm: $$A(a) = 2a^2 + 4a \cdot \frac{18}{a^2} = 2a^2 + \frac{72}{a}, \qquad a > 0$$

#### Pas 3 — Derivada i punt crític

$$A'(a) = 4a - \frac{72}{a^2} = 0 \implies 4a^3 = 72 \implies a^3 = 18 \implies \boxed{a = \sqrt[3]{18} \approx 2{,}62 \text{ m}}$$

Però de la condició donada $c = 2$ m i $a \cdot b \cdot 2 = 18 \implies ab = 9$. Amb $a = b$: $a^2 = 9 \implies a = 3$ m.

$$a = 3, \quad b = 3, \quad c = 2 \text{ m}$$

Comprovació: $3 \cdot 3 \cdot 2 = 18$

$$A(3) = 2(9) + 4(3)(2) = 18 + 24 = 42 \text{ (unitats de cost)}$$

> **📘 Resultat**
>
> $$\boxed{a = b = 3 \text{ m}, \quad c = 2 \text{ m}}$$ $$\text{Cost mínim} = 2(3)^2 + 4(3)(2) = 18 + 24 = 42 \text{ u}$$

### Caixa oberta des d’una planxa de $12 \times 12$ cm

> **📝 Enunciat**
>
> A partir d’una planxa quadrada de $12 \times 12$ cm es fabriquen caixes obertes retallant quadrats de costat $x$ als quatre cantons. Calcula el valor de $x$ que maximitza el volum.

#### Pas 1 — Funció volum

Retallant quadrats de costat $x$, la base queda de costat $(12 - 2x)$ i l’alçada és $x$: $$V(x) = (12 - 2x)^2 \cdot x, \qquad x \in [0, 6]$$

#### Pas 2 — Valors als extrems

$$V(0) = 144 \cdot 0 = 0, \qquad V(6) = 0^2 \cdot 6 = 0$$

El màxim és interior.

#### Pas 3 — Derivada i punt crític

Expandim: $V(x) = (144 - 48x + 4x^2)x = 144x - 48x^2 + 4x^3$

$$V'(x) = 144 - 96x + 12x^2 = 12(x^2 - 8x + 12) = 12(x-2)(x-6)$$

$V' = 0 \implies x = 2$ o $x = 6$.

Com que $x = 6$ dona volum zero, el màxim és $\boxed{x = 2}$ cm.

#### Pas 4 — Volum màxim

$$V(2) = (12 - 4)^2 \cdot 2 = 64 \cdot 2 = 128 \text{ cm}^3$$

> **📘 Resultat**
>
> $$\boxed{x = 2 \text{ cm}, \quad \text{Dimensions}: 8 \times 8 \times 2 \text{ cm}, \quad V_{\max} = 128 \text{ cm}^3}$$

## Sumes de distàncies

### Suma de distàncies des d’un punt als vèrtexs d’un triangle

> **📝 Enunciat**
>
> Donat un triangle amb vèrtexs $A$, $B(5, 0)$ i $C$ on $BC = 13$, $AB = 5$ i $h = 12$. Un punt $P$ es troba sobre el segment $AB$, a distància $x$ de $A$. Troba la posició de $P$ que minimitza la suma $S = 2\cdot d(P,A) + d(P,C)$, amb $x \in [0, 12]$.

#### Pas 1 — Distàncies

Per Pitàgores: $d(P, C) = \sqrt{(12 - x)^2 + 0} = 12 - x$ (si $P$ és a distància $x$ del vèrtex vertical).

Amb les coordenades del problema: $$d(P, A) = \sqrt{5^2 + x^2} = \sqrt{25 + x^2}$$ $$S(x) = 2\sqrt{25 + x^2} + (12 - x), \qquad x \in [0, 12]$$

#### Pas 2 — Derivada i punt crític

$$S'(x) = \frac{2x}{\sqrt{25 + x^2}} - 1 = 0 \implies 2x = \sqrt{25 + x^2}$$ $$4x^2 = 25 + x^2 \implies 3x^2 = 25 \implies x = \frac{5}{\sqrt{3}} = \frac{5\sqrt{3}}{3}$$

#### Pas 3 — Comparació als extrems i al punt crític

$$S(0) = 2 \cdot 5 + 12 = 22 \quad \text{(màxim)}$$ $$S\!\left(\tfrac{5}{\sqrt{3}}\right) = 2\sqrt{25 + \tfrac{25}{3}} + 12 - \tfrac{5}{\sqrt{3}} = \frac{20}{\sqrt{3}} + 12 - \frac{5}{\sqrt{3}} = \frac{15}{\sqrt{3}} + 12 = 5\sqrt{3} + 12 \approx 20{,}66 \quad \text{(mínim)}$$ $$S(12) = 2\sqrt{25 + 144} + 0 = 2 \cdot 13 = 26 \quad \text{(màxim global)}$$

> **📘 Resultat**
>
> $$\text{Mínim: } S_{\min} = 5\sqrt{3} + 12 \approx 20{,}66 \quad \text{en } x = \frac{5\sqrt{3}}{3}$$ $$\text{Màxim: } S_{\max} = 26 \quad \text{en } x = 12$$
