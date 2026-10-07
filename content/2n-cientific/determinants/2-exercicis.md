---
title: Determinants, matrius i sistemes: Exercicis
tematitol: Determinants, matrius i sistemes
curs: 2n
modalitat: tots
tema: determinants
bloc: exercicis
ordre: 2
---
# Determinants, matrius i sistemes: Exercicis

## Exercici 1 — Determinants 2×2

> **📝 Enunciat**
>
> Calcula el valor dels determinants següents i digues per què alguns són zero:

### a) $\begin{vmatrix} 13 & 6 \\ 4 & 2 \end{vmatrix}$

$$\begin{vmatrix} 13 & 6 \\ 4 & 2 \end{vmatrix} = 13\cdot 2 - 6\cdot 4 = 26 - 24 = \boxed{2}$$

### b) $\begin{vmatrix} 13 & 6 \\ 4 & -2 \end{vmatrix}$

$$\begin{vmatrix} 13 & 6 \\ 4 & -2 \end{vmatrix} = 13\cdot(-2) - 6\cdot 4 = -26 - 24 = \boxed{-50}$$

### c) $\begin{vmatrix} 1 & 0 \\ 11 & 0 \end{vmatrix}$

$$\begin{vmatrix} 1 & 0 \\ 11 & 0 \end{vmatrix} = 1\cdot 0 - 0\cdot 11 = \boxed{0}$$ **Per què és zero?** La segona columna és tota de zeros. Quan una columna (o fila) és tot zeros, el determinant val 0.

### d) $\begin{vmatrix} 7 & -2 \\ 7 & -2 \end{vmatrix}$

$$\begin{vmatrix} 7 & -2 \\ 7 & -2 \end{vmatrix} = 7\cdot(-2) - (-2)\cdot 7 = -14 + 14 = \boxed{0}$$ **Per què és zero?** Les dues files són iguals. Quan dues files (o columnes) són proporcionals, el determinant és 0.

### e) $\begin{vmatrix} 3 & 11 \\ 21 & 77 \end{vmatrix}$

$$\begin{vmatrix} 3 & 11 \\ 21 & 77 \end{vmatrix} = 3\cdot 77 - 11\cdot 21 = 231 - 231 = \boxed{0}$$ **Per què és zero?** La segona fila és 7 vegades la primera ($21=7\cdot3$, $77=7\cdot11$). Files proporcionals $\Rightarrow$ determinant 0.

### f) $\begin{vmatrix} -140 & 7 \\ 60 & -3 \end{vmatrix}$

$$\begin{vmatrix} -140 & 7 \\ 60 & -3 \end{vmatrix} = (-140)\cdot(-3) - 7\cdot 60 = 420 - 420 = \boxed{0}$$ **Per què és zero?** La primera columna és $-20$ vegades la segona ($-140 = -20\cdot7$, $60=-20\cdot(-3)$). Columnes proporcionals $\Rightarrow$ determinant 0.

## Exercici 2 — Afirmacions sobre determinants 2×2

> **📝 Enunciat**
>
> Sigui $A$ una matriu $2\times2$. Justifica si les afirmacions següents són certes o falses.

### a) Per a $|A|=0$ és necessari que els seus quatre elements siguin 0.

**FALSA.**

Contraexemple: $A = \begin{pmatrix}1 & 1 \\ 1 & 1\end{pmatrix}$, on $|A| = 1\cdot1 - 1\cdot1 = 0$, però els elements no són tots zero.

### b) Si els dos elements de la segona columna d’$A$ són 0, llavors $|A|=0$.

**CERTA.**

Si $A=\begin{pmatrix}a & 0 \\ c & 0\end{pmatrix}$, llavors $|A|= a\cdot 0 - 0\cdot c = 0$.

En general, quan una columna (o fila) és tot zeros, el determinant val 0, perquè en desplegar per aquella columna tots els termes són 0.

### c) Si les dues files d’$A$ coincideixen, llavors $|A|=0$.

**CERTA.**

Si $A=\begin{pmatrix}a & b \\ a & b\end{pmatrix}$, llavors $|A|= ab - ba = 0$. Dues files iguals implica determinant 0 (propietat de multilinealitat alternada).

### d) Si $\begin{vmatrix} a & b \\ c & d \end{vmatrix}=-15$, llavors $\begin{vmatrix} c & d \\ a & b \end{vmatrix}=15$.

**CERTA.**

Intercanviar dues files canvia el signe del determinant: $$\begin{vmatrix} c & d \\ a & b \end{vmatrix} = -(\ \begin{vmatrix} a & b \\ c & d \end{vmatrix}\ ) = -(-15) = 15.$$

### e) Si $\begin{vmatrix} m & 3 \\ n & 7 \end{vmatrix}=43$, llavors $\begin{vmatrix} m & 30 \\ n & 70 \end{vmatrix}=430$.

**CERTA.**

La segona columna de la nova matriu és 10 vegades la de l’original. Per la propietat de linealitat del determinant, treure un factor $k$ d’una columna multiplica el determinant per $k$: $$\begin{vmatrix} m & 30 \\ n & 70 \end{vmatrix} = 10\cdot\begin{vmatrix} m & 3 \\ n & 7 \end{vmatrix} = 10\cdot 43 = 430.$$

## Exercici 3 — Propietats amb determinants

> **📝 Enunciat**
>
> Si $A=\begin{pmatrix}l & m \\ n & p\end{pmatrix}$ i $|A|=-13$, calcula:

Tenim $|A| = lp - mn = -13$.

### a) $\begin{vmatrix} n & p \\ l & m \end{vmatrix}$

S’han intercanviat les dues files d’$A$: $$\begin{vmatrix} n & p \\ l & m \end{vmatrix} = -|A| = -(-13) = \boxed{13}$$

### b) $\begin{vmatrix} l & m \\ 7n & 7p \end{vmatrix}$

La segona fila és $7$ vegades la segona fila d’$A$: $$\begin{vmatrix} l & m \\ 7n & 7p \end{vmatrix} = 7\cdot|A| = 7\cdot(-13) = \boxed{-91}$$

### c) $|3A|$

Per a una matriu $2\times2$, $|kA| = k^2|A|$: $$|3A| = 3^2\cdot|A| = 9\cdot(-13) = \boxed{-117}$$

### d) $\begin{vmatrix} 3n & 5p \\ 3l & 5m \end{vmatrix}$

Reescrivim: $$\begin{vmatrix} 3n & 5p \\ 3l & 5m \end{vmatrix}$$ Traiem factor 3 de la primera columna i factor 5 de la segona: $$= 3\cdot5\cdot\begin{vmatrix} n & p \\ l & m \end{vmatrix} = 15\cdot(-|A|) = 15\cdot 13 = \boxed{195}$$

## Exercici 4 — Determinants 3×3 (regla de Sarrus)

> **📝 Enunciat**
>
> Calcula els determinants següents:

### a) $\begin{vmatrix} 5 & 1 & 4 \\ 0 & 3 & 6 \\ 9 & 6 & 8 \end{vmatrix}$

Desenvolupem per la primera columna (o regla de Sarrus):

**Termes positius:** $5\cdot3\cdot8 + 1\cdot6\cdot9 + 4\cdot0\cdot6 = 120 + 54 + 0 = 174$

**Termes negatius:** $9\cdot3\cdot4 + 6\cdot6\cdot5 + 8\cdot0\cdot1 = 108 + 180 + 0 = 288$

$$\begin{vmatrix} 5 & 1 & 4 \\ 0 & 3 & 6 \\ 9 & 6 & 8 \end{vmatrix} = 174 - 288 = \boxed{-114}$$

*Verificació per cofactors (primera columna):* $$= 5\begin{vmatrix} 3&6\\6&8 \end{vmatrix} - 0\begin{vmatrix} 1&4\\6&8 \end{vmatrix} + 9\begin{vmatrix} 1&4\\3&6 \end{vmatrix}
= 5(24-36) - 0 + 9(6-12)
= 5(-12) + 9(-6) = -60 - 54 = -114\checkmark$$

### b) $\begin{vmatrix} 9 & 0 & 3 \\ -1 & 1 & 0 \\ 0 & 2 & 1 \end{vmatrix}$

**Termes positius:** $9\cdot1\cdot1 + 0\cdot0\cdot0 + 3\cdot(-1)\cdot2 = 9 + 0 - 6 = 3$

**Termes negatius:** $0\cdot1\cdot3 + 2\cdot0\cdot9 + 1\cdot(-1)\cdot0 = 0 + 0 + 0 = 0$

$$\begin{vmatrix} 9 & 0 & 3 \\ -1 & 1 & 0 \\ 0 & 2 & 1 \end{vmatrix} = 3 - 0 = \boxed{3}$$

*Verificació per cofactors (primera fila):* $$= 9\begin{vmatrix} 1&0\\2&1 \end{vmatrix} - 0\begin{vmatrix} -1&0\\0&1 \end{vmatrix} + 3\begin{vmatrix} -1&1\\0&2 \end{vmatrix}
= 9(1) - 0 + 3(-2-0) = 9 - 6 = 3\checkmark$$

## Exercici 5 — Determinants 3×3

> **📝 Enunciat**
>
> Troba el valor d’aquests determinants:

### a) $\begin{vmatrix} 0 & 4 & -1 \\ 1 & 2 & 1 \\ 3 & 0 & 1 \end{vmatrix}$

Desenvolupem per la primera fila: $$= 0\cdot\begin{vmatrix} 2&1\\0&1 \end{vmatrix} - 4\cdot\begin{vmatrix} 1&1\\3&1 \end{vmatrix} + (-1)\cdot\begin{vmatrix} 1&2\\3&0 \end{vmatrix}$$ $$= 0 - 4(1-3) + (-1)(0-6)
= -4(-2) + (-1)(-6) = 8 + 6 = \boxed{14}$$

### b) $\begin{vmatrix} 10 & 47 & 59 \\ 0 & 10 & 91 \\ 0 & 0 & 10 \end{vmatrix}$

És una matriu triangular superior. El determinant d’una matriu triangular és el producte dels elements de la diagonal principal: $$\begin{vmatrix} 10 & 47 & 59 \\ 0 & 10 & 91 \\ 0 & 0 & 10 \end{vmatrix} = 10\cdot10\cdot10 = \boxed{1000}$$

## Exercici 6 — Columna combinació lineal

> **📝 Enunciat**
>
> Donades $A=\begin{pmatrix}5&4&9\\8&1&9\\3&6&9\end{pmatrix}$, $B=\begin{pmatrix}5&4&1\\8&1&7\\3&6&-3\end{pmatrix}$, $C=\begin{pmatrix}5&4&20\\8&1&8\\3&6&18\end{pmatrix}$, justifica si les afirmacions son certes o falses.

Siguin $\mathbf{c}_1, \mathbf{c}_2$ la primera i segona columna de cadascuna de les matrius.

### a) $|A|=0$ perquè la tercera columna és suma de les dues primeres.

**CERTA.**

Efectivament, $\mathbf{c}_3^A = \mathbf{c}_1+\mathbf{c}_2$: $9=5+4$, $9=8+1$, $9=3+6$. Per la propietat de linealitat: $$|A| = |\mathbf{c}_1,\mathbf{c}_2,\mathbf{c}_1+\mathbf{c}_2| = |\mathbf{c}_1,\mathbf{c}_2,\mathbf{c}_1| + |\mathbf{c}_1,\mathbf{c}_2,\mathbf{c}_2| = 0+0 = 0$$ (columna repetida en cada sumand).

### b) $|B|=0$ perquè la tercera columna és diferència de les dues primeres.

**CERTA.**

$\mathbf{c}_3^B = \mathbf{c}_1 - \mathbf{c}_2$: $1=5-4$, $7=8-1$, $-3=3-6$. Anàlogament: $$|B| = |\mathbf{c}_1,\mathbf{c}_2,\mathbf{c}_1-\mathbf{c}_2| = |\mathbf{c}_1,\mathbf{c}_2,\mathbf{c}_1| - |\mathbf{c}_1,\mathbf{c}_2,\mathbf{c}_2| = 0 - 0 = 0$$

### c) $|C|=0$ perquè la tercera columna és producte de les dues primeres.

**FALSA.**

El producte component a component ($5\cdot4=20$, $8\cdot1=8$, $3\cdot6=18$) és cert numèricament. No obstant, la propietat del determinant sobre combinació lineal només és vàlida per a sumes/diferències, no per a productes element a element. Hem de calcular: $$|C| = \begin{vmatrix} 5&4&20\\8&1&8\\3&6&18 \end{vmatrix}$$ $$= 5(18-48)-4(144-24)+20(48-3)
= 5(-30)-4(120)+20(45)
= -150 - 480 + 900 = 270 \neq 0$$ Per tant l’afirmació és falsa: $|C| \neq 0$.

## Exercici 7 — Justificació d’igualtats sense desenvolupar

> **📝 Enunciat**
>
> Justifica, sense desenvolupar, aquestes igualtats:

### a) $\begin{vmatrix} 3 & -1 & 7 \\ 0 & 0 & 0 \\ 1 & 11 & 4 \end{vmatrix}=0$

**Justificació:** La segona fila és tot zeros. Si una fila (o columna) d’una matriu és tot zeros, el determinant val 0, ja que en desplegar per aquella fila la suma és $0\cdot A_{21}+0\cdot A_{22}+0\cdot A_{23}=0$.

### b) $\begin{vmatrix} 4 & 1 & 7 \\ 2 & 9 & 1 \\ -8 & -2 & -14 \end{vmatrix}=0$

**Justificació:** La tercera fila és $-2$ vegades la primera: $(-8,-2,-14)=-2\cdot(4,1,7)$. Dues files proporcionals $\Rightarrow$ determinant 0.

### c) $\begin{vmatrix} 7 & 4 & 1 \\ 2 & 9 & 7 \\ 27 & 94 & 71 \end{vmatrix}=0$

**Justificació:** La tercera columna és suma de la primera i la segona: $1=7-6$? Comprovem si $\mathbf{c}_3 = a\mathbf{c}_1+b\mathbf{c}_2$.

Observem: $\mathbf{c}_3 = \mathbf{c}_1 + \mathbf{c}_2 - \mathbf{c}_1$... provem $\mathbf{c}_3 = \mathbf{c}_2 - \mathbf{c}_1 + ?$

En realitat, comprovem si la tercera fila és combinació lineal de les dues primeres: $\mathbf{f}_3 = \alpha \mathbf{f}_1 + \beta \mathbf{f}_2$: $$7\alpha+2\beta=27,\quad 4\alpha+9\beta=94,\quad \alpha+7\beta=71$$ De la tercera: $\alpha = 71-7\beta$. Substituint a la primera: $7(71-7\beta)+2\beta=27 \Rightarrow 497-49\beta+2\beta=27 \Rightarrow -47\beta=-470 \Rightarrow \beta=10$, $\alpha=1$.

Verificació: $1\cdot(7,4,1)+10\cdot(2,9,7)=(7+20,4+90,1+70)=(27,94,71)$

La tercera fila és combinació lineal de les dues primeres $\Rightarrow$ les files són linealment dependents $\Rightarrow$ determinant 0.

## Exercici 8 — Propietats del determinant

> **📝 Enunciat**
>
> Sabent que $\begin{vmatrix} x & y & z \\ 5 & 0 & 3 \\ 1 & 1 & 1 \end{vmatrix}=1$, calcula, sense desenvolupar, els determinants següents:

Anomenem $D = \begin{vmatrix} x & y & z \\ 5 & 0 & 3 \\ 1 & 1 & 1 \end{vmatrix}=1$.

### a) $\begin{vmatrix} 3x & 3y & 3z \\ 5 & 0 & 3 \\ 1 & 1 & 1 \end{vmatrix}$

Es treu factor 3 de la primera fila: $$= 3\cdot D = 3\cdot1 = \boxed{3}$$

### b) $\begin{vmatrix} 5x & 5y & 5z \\ 1 & 0 & 3/5 \\ 1 & 1 & 1 \end{vmatrix}$

La primera fila és $5$ vegades la original, i la segona fila és $\frac{1}{5}$ vegades la fila $[5,0,3]$: $$= 5\cdot\frac{1}{5}\cdot D = 1\cdot D = \boxed{1}$$

### c) $\begin{vmatrix} x & y & z \\ 2x+5 & 2y & 2z+3 \\ x+1 & y+1 & z+1 \end{vmatrix}$

Descomposem la segona fila com $[2x,2y,2z]+[5,0,3]$ i la tercera com $[x,y,z]+[1,1,1]$: $$\begin{vmatrix} x&y&z\\2x+5&2y&2z+3\\x+1&y+1&z+1 \end{vmatrix}$$

Fem $F_2 \leftarrow F_2 - 2F_1$ i $F_3 \leftarrow F_3 - F_1$ (aquestes operacions no canvien el determinant): $$= \begin{vmatrix} x & y & z \\ 5 & 0 & 3 \\ 1 & 1 & 1 \end{vmatrix} = D = \boxed{1}$$

## Exercici 9 — Determinant de Vandermonde

> **📝 Enunciat**
>
> Si $\begin{vmatrix} 1&1&1\\a&b&c\\a^2&b^2&c^2 \end{vmatrix}=2$, troba els determinants indicats.

Anomeno $V = \begin{vmatrix} 1&1&1\\a&b&c\\a^2&b^2&c^2 \end{vmatrix} = 2$.

### a) $\begin{vmatrix} a-1 & b-1 & c-1 \\ a^2-1 & b^2-1 & c^2-1 \\ 5 & 5 & 5 \end{vmatrix}$

Observem que $a^2-1=(a-1)(a+1)$ i descomposem per linealitat. En el determinant original, substituïm:

La primera fila és $[a,b,c]-[1,1,1]$. La segona fila és $[a^2,b^2,c^2]-[1,1,1]$. La tercera és $5\cdot[1,1,1]$.

$$\begin{vmatrix} a-1 & b-1 & c-1 \\ a^2-1 & b^2-1 & c^2-1 \\ 5 & 5 & 5 \end{vmatrix}$$

Fem $C_j \leftarrow C_j + C_{\text{nova}}$: sumem la fila $[1,1,1]$ a cada fila corresponent. Concretament, $F_1\leftarrow F_1+[1,1,1]$ i $F_2\leftarrow F_2+[1,1,1]$: $$= \begin{vmatrix} a & b & c \\ a^2 & b^2 & c^2 \\ 5 & 5 & 5 \end{vmatrix}$$

Traiem factor 5 de la tercera fila: $$= 5\cdot\begin{vmatrix} a & b & c \\ a^2 & b^2 & c^2 \\ 1 & 1 & 1 \end{vmatrix}$$

Intercanviem la primera i la tercera fila (canvi de signe), i després la nova primera i la tercera (altre canvi de signe):

$$\begin{vmatrix} a&b&c\\a^2&b^2&c^2\\1&1&1 \end{vmatrix}
\xrightarrow{F_1\leftrightarrow F_3} -\begin{vmatrix} 1&1&1\\a^2&b^2&c^2\\a&b&c \end{vmatrix}
\xrightarrow{F_2\leftrightarrow F_3} +\begin{vmatrix} 1&1&1\\a&b&c\\a^2&b^2&c^2 \end{vmatrix} = V = 2$$

Per tant: $$= 5\cdot 2 = \boxed{10}$$

### b) $\begin{vmatrix} (a+1)^2 & (b+1)^2 & (c+1)^2 \\ a & b & c \\ a^2 & b^2 & c^2 \end{vmatrix}$

Expandim $(a+1)^2 = a^2+2a+1$, i per linealitat de la primera fila: $$= \begin{vmatrix} a^2&b^2&c^2\\a&b&c\\a^2&b^2&c^2 \end{vmatrix} + 2\begin{vmatrix} a&b&c\\a&b&c\\a^2&b^2&c^2 \end{vmatrix} + \begin{vmatrix} 1&1&1\\a&b&c\\a^2&b^2&c^2 \end{vmatrix}$$

El primer terme té la fila 1 i la fila 3 iguals $\Rightarrow 0$.

El segon terme té les files 1 i 2 iguals $\Rightarrow 0$.

El tercer terme és exactament $V = 2$.

$$= 0 + 0 + V = \boxed{2}$$

## Exercici 10 — Equació amb determinant

> **📝 Enunciat**
>
> Resol l’equació: $\begin{vmatrix} x & -1 & -2x \\ -2x & -x & 1+x \\ 1 & 2x & 0 \end{vmatrix}=0$.

Calculem el determinant desenvolupant per la tercera fila: $$D = 1\cdot\begin{vmatrix} -1&-2x\\-x&1+x \end{vmatrix} - 2x\cdot\begin{vmatrix} x&-2x\\-2x&1+x \end{vmatrix} + 0$$

$$\begin{vmatrix} -1&-2x\\-x&1+x \end{vmatrix} = (-1)(1+x)-(-2x)(-x) = -1-x-2x^2$$

$$\begin{vmatrix} x&-2x\\-2x&1+x \end{vmatrix} = x(1+x)-(-2x)(-2x) = x+x^2-4x^2 = x-3x^2$$

$$D = 1\cdot(-1-x-2x^2) - 2x\cdot(x-3x^2)
= -1-x-2x^2 - 2x^2+6x^3
= 6x^3-4x^2-x-1$$

Resolem $6x^3-4x^2-x-1=0$.

Provem $x=1$: $6-4-1-1=0$

Factoritzem: $(x-1)(6x^2+2x+1)=0$.

Discriminant de $6x^2+2x+1$: $\Delta=4-24=-20<0$ (sense arrels reals).

$$\boxed{x=1}$$

## Exercici 11 — Menors d’una matriu

> **📝 Enunciat**
>
> Troba dos menors d’ordre 2 i dos menors d’ordre 3 de la matriu $M=\begin{pmatrix}2&3&-1&5\\4&6&2&7\\5&-1&2&6\\4&1&1&5\\0&0&3&4\end{pmatrix}$.

Un **menor d’ordre $k$** d’una matriu és el determinant d’una submatriu $k\times k$ obtinguda eliminant files i columnes.

### Menor d’ordre 2: files $\{1,2\}$, columnes $\{1,2\}$

$$M^{12}_{12} = \begin{vmatrix} 2 & 3 \\ 4 & 6 \end{vmatrix} = 12 - 12 = 0$$

### Menor d’ordre 2: files $\{1,3\}$, columnes $\{2,4\}$

$$M^{13}_{24} = \begin{vmatrix} 3 & 5 \\ -1 & 6 \end{vmatrix} = 18-(-5) = 23$$

### Menor d’ordre 3: files $\{1,2,3\}$, columnes $\{1,2,3\}$

$$M^{123}_{123} = \begin{vmatrix} 2 & 3 & -1 \\ 4 & 6 & 2 \\ 5 & -1 & 2 \end{vmatrix}$$ $$= 2(12+2)-3(8-10)+(-1)(-4-30)
= 2(14)-3(-2)+(-1)(-34)
= 28+6+34 = 68$$

### Menor d’ordre 3: files $\{2,3,4\}$, columnes $\{2,3,4\}$

$$M^{234}_{234} = \begin{vmatrix} 6 & 2 & 7 \\ -1 & 2 & 6 \\ 1 & 1 & 5 \end{vmatrix}$$ $$= 6(10-6)-2(-5-6)+7(-1-2)
= 6(4)-2(-11)+7(-3)
= 24+22-21 = 25$$

## Exercici 12 — Cofactors i adjunts

> **📝 Enunciat**
>
> Troba el menor complementari i l’adjunt dels elements $a_{12}$, $a_{33}$ i $a_{43}$ de la matriu $A=\begin{pmatrix}0&2&4&6\\2&-1&3&5\\1&1&2&3\\4&6&5&7\end{pmatrix}$.

El **menor complementari** $\alpha_{ij}$ és el determinant de la submatriu que resulta d’eliminar la fila $i$ i la columna $j$.

L’**adjunt** (cofactor) és $A_{ij} = (-1)^{i+j}\alpha_{ij}$.

### Element $a_{12}$ (fila 1, columna 2)

Eliminem fila 1 i columna 2: $$\alpha_{12} = \begin{vmatrix} 2 & 3 & 5 \\ 1 & 2 & 3 \\ 4 & 5 & 7 \end{vmatrix}$$ $$= 2(14-15)-3(7-12)+5(5-8)
= 2(-1)-3(-5)+5(-3)
= -2+15-15 = -2$$ $$A_{12} = (-1)^{1+2}\cdot(-2) = (-1)(-2) = \boxed{2}$$

### Element $a_{33}$ (fila 3, columna 3)

Eliminem fila 3 i columna 3: $$\alpha_{33} = \begin{vmatrix} 0 & 2 & 6 \\ 2 & -1 & 5 \\ 4 & 6 & 7 \end{vmatrix}$$ $$= 0(-7-30)-2(14-20)+6(12+4)
= 0-2(-6)+6(16)
= 0+12+96 = 108$$ $$A_{33} = (-1)^{3+3}\cdot108 = (+1)(108) = \boxed{108}$$

### Element $a_{43}$ (fila 4, columna 3)

Eliminem fila 4 i columna 3: $$\alpha_{43} = \begin{vmatrix} 0 & 2 & 6 \\ 2 & -1 & 5 \\ 1 & 1 & 3 \end{vmatrix}$$ $$= 0(-3-5)-2(6-5)+6(2+1)
= 0-2(1)+6(3)
= 0-2+18 = 16$$ $$A_{43} = (-1)^{4+3}\cdot16 = (-1)(16) = \boxed{-16}$$

## Exercici 13 — Determinants 4×4 (triangulació)

> **📝 Enunciat**
>
> Calcula el valor dels determinants de 4×4 indicats.

### a) $\begin{vmatrix} 4&3&1&27\\1&1&4&9\\2&4&-1&36\\0&6&2&54 \end{vmatrix}$

Apliquem operacions elementals de files:

$F_1 \leftrightarrow F_2$ (canvi de signe): $$-\begin{vmatrix} 1&1&4&9\\4&3&1&27\\2&4&-1&36\\0&6&2&54 \end{vmatrix}$$

$F_2 \leftarrow F_2-4F_1$; $F_3\leftarrow F_3-2F_1$: $$-\begin{vmatrix} 1&1&4&9\\0&-1&-15&-9\\0&2&-9&18\\0&6&2&54 \end{vmatrix}$$

$F_3\leftarrow F_3+2F_2$; $F_4\leftarrow F_4+6F_2$: $$-\begin{vmatrix} 1&1&4&9\\0&-1&-15&-9\\0&0&-39&0\\0&0&-88&0 \end{vmatrix}$$

$F_4\leftarrow F_4 - \frac{88}{39}F_3$: $$-\begin{vmatrix} 1&1&4&9\\0&-1&-15&-9\\0&0&-39&0\\0&0&0&0 \end{vmatrix}$$

La matriu triangular té un zero en la diagonal $\Rightarrow$ el determinant de la matriu triangular és 0, i per tant: $$\boxed{0}$$

### b) $\begin{vmatrix} 1&0&1&0\\2&4&0&3\\612&704&410&103\\6&7&4&1 \end{vmatrix}$

Estratègia: despleguem per cofactors de la primera fila (aprofitant el zero en posició $(1,2)$ i $(1,4)$): $$= 1\cdot A_{11} + 0\cdot A_{12} + 1\cdot A_{13} + 0\cdot A_{14}
= A_{11} + A_{13}$$

$$A_{11} = (+1)\begin{vmatrix} 4&0&3\\704&410&103\\7&4&1 \end{vmatrix}
= 4(410-412) - 0 + 3(2816-2870)
= 4(-2)+3(-54) = -8-162 = -170$$

$$A_{13} = (+1)\begin{vmatrix} 2&4&3\\612&704&103\\6&7&1 \end{vmatrix}
= 2(704-721)-4(612-618)+3(4284-4224)
= 2(-17)-4(-6)+3(60)
= -34+24+180 = 170$$

$$D = -170 + 170 = \boxed{0}$$

### c) $\begin{vmatrix} 4&0&0&0\\0&0&8&0\\0&0&0&1\\0&-3&0&0 \end{vmatrix}$

Matriu quasi diagonal amb permutació. Despleguem per la primera fila (únic element no nul: $a_{11}=4$): $$= 4\cdot(-1)^{1+1}\begin{vmatrix} 0&8&0\\0&0&1\\-3&0&0 \end{vmatrix}$$ $$\begin{vmatrix} 0&8&0\\0&0&1\\-3&0&0 \end{vmatrix} = -3\cdot(-1)^{3+1}\begin{vmatrix} 8&0\\0&1 \end{vmatrix} = -3\cdot(8) = -24$$ $$D = 4\cdot(-24) = \boxed{-96}$$

### d) $\begin{vmatrix} 1&0&0&0\\4&-1&0&0\\7&-1&1&0\\3&1&4&1 \end{vmatrix}$

Matriu triangular inferior. El determinant és el producte de la diagonal: $$= 1\cdot(-1)\cdot1\cdot1 = \boxed{-1}$$

### e) $\begin{vmatrix} 6&0&0&0\\0&8&0&5\\0&0&4&0\\3&0&0&0 \end{vmatrix}$

Despleguem per la primera fila: $$= 6\cdot(-1)^{1+1}\begin{vmatrix} 8&0&5\\0&4&0\\0&0&0 \end{vmatrix}$$ La submatriu $3\times3$ té la tercera fila de zeros $\Rightarrow$ determinant 0. $$D = 6\cdot0 = \boxed{0}$$

## Exercici 14 — Determinants 4×4 generals

> **📝 Enunciat**
>
> Calcula els determinants de 4×4 generals.

### a) $\begin{vmatrix} 7&0&-3&4\\4&0&4&7\\3&7&6&9\\1&0&1&9 \end{vmatrix}$

Despleguem per la segona columna (tres zeros): $$= -0\cdot(\ldots) + 0\cdot(\ldots) - 7\cdot(-1)^{3+2}\begin{vmatrix} 7&-3&4\\4&4&7\\1&1&9 \end{vmatrix} + 0\cdot(\ldots)$$ $$= 7\cdot\begin{vmatrix} 7&-3&4\\4&4&7\\1&1&9 \end{vmatrix}$$ $$\begin{vmatrix} 7&-3&4\\4&4&7\\1&1&9 \end{vmatrix}
= 7(36-7)+3(36-7)+4(4-4)
= 7(29)+3(29)+0
= 29(7+3) = 290$$ $$D = 7\cdot290 = \boxed{2030}$$

### b) $\begin{vmatrix} 3&1&-1&3\\1&4&-1&4\\0&3&2&5\\2&0&0&2 \end{vmatrix}$

Despleguem per la quarta fila: $$= 2\cdot(-1)^{4+1}\begin{vmatrix} 1&-1&3\\4&-1&4\\3&2&5 \end{vmatrix} + 0 + 0 + 2\cdot(-1)^{4+4}\begin{vmatrix} 3&1&-1\\1&4&-1\\0&3&2 \end{vmatrix}$$

$$\begin{vmatrix} 1&-1&3\\4&-1&4\\3&2&5 \end{vmatrix}
= 1(-5-8)+1(20-12)+3(8+3)
= -13+8+33 = 28$$

$$\begin{vmatrix} 3&1&-1\\1&4&-1\\0&3&2 \end{vmatrix}
= 3(8+3)-1(2-0)+(-1)(3-0)
= 33-2-3 = 28$$

$$D = 2\cdot(-1)\cdot28 + 2\cdot(+1)\cdot28 = -56+56 = \boxed{0}$$

### c) $\begin{vmatrix} 0&0&3&4\\1&1&1&0\\2&0&3&5\\0&2&0&1 \end{vmatrix}$

Despleguem per la primera fila ($a_{11}=0$, $a_{12}=0$): $$= 0+0+3\cdot(-1)^{1+3}\begin{vmatrix} 1&1&0\\2&0&5\\0&2&1 \end{vmatrix}+4\cdot(-1)^{1+4}\begin{vmatrix} 1&1&1\\2&0&3\\0&2&0 \end{vmatrix}$$

$$\begin{vmatrix} 1&1&0\\2&0&5\\0&2&1 \end{vmatrix}=1(0-10)-1(2-0)+0=(-10)-2=-12$$

$$\begin{vmatrix} 1&1&1\\2&0&3\\0&2&0 \end{vmatrix}=1(0-6)-1(0-0)+1(4-0)=-6+4=-2$$

$$D = 3(1)(-12)+4(-1)(-2) = -36+8 = \boxed{-28}$$

### d) $\begin{vmatrix} 3&-1&4&0\\5&6&2&0\\0&1&3&0\\8&6&7&1 \end{vmatrix}$

La quarta columna és $(0,0,0,1)^T$. Despleguem per la quarta columna: $$= 1\cdot(-1)^{4+4}\begin{vmatrix} 3&-1&4\\5&6&2\\0&1&3 \end{vmatrix}$$ $$= 3(18-2)+1(15-0)+4(5-0)
= 3(16)+15+20
= 48+15+20 = \boxed{83}$$

## Exercici 15 — Rang en funció d’un paràmetre

> **📝 Enunciat**
>
> Estudia el rang de les matrius en funció del paràmetre que hi apareix.

### a) $A=\begin{pmatrix}2&1&0\\1&1&-2\\3&1&a\end{pmatrix}$

$$|A| = \begin{vmatrix} 2&1&0\\1&1&-2\\3&1&a \end{vmatrix}
= 2(a+2)-1(a+6)+0 = 2a+4-a-6 = a-2$$

- Si $a\neq 2$: $|A|\neq0 \Rightarrow$ rang$(A)=3$ (matriu regular).

- Si $a=2$: $|A|=0$, estudiem submenors d’ordre 2. Per exemple $\begin{vmatrix} 2&1\\1&1 \end{vmatrix}=1\neq0$, per tant rang$(A)=2$.

$$\operatorname{rang}(A) = \begin{cases} 3 & \text{si } a\neq 2 \\ 2 & \text{si } a=2 \end{cases}$$

### b) $B=\begin{pmatrix}a&1&0\\-1&2a&-2\\1&-1&2\end{pmatrix}$

$$|B| = a(4a-2)-1(-2+2)+0 = a(4a-2) = 2a(2a-1)$$

- Si $a\neq0$ i $a\neq\frac{1}{2}$: rang$(B)=3$.

- Si $a=0$: $B=\begin{pmatrix}0&1&0\\-1&0&-2\\1&-1&2\end{pmatrix}$. Menor $\begin{vmatrix} 1&0\\-1&2 \end{vmatrix}=2\neq0 \Rightarrow$ rang$(B)=2$.

- Si $a=\frac{1}{2}$: $B=\begin{pmatrix}1/2&1&0\\-1&1&-2\\1&-1&2\end{pmatrix}$. Menor $\begin{vmatrix} 1/2&1\\-1&1 \end{vmatrix}=1/2+1=3/2\neq0 \Rightarrow$ rang$(B)=2$.

$$\operatorname{rang}(B) = \begin{cases} 3 & \text{si } a\neq 0 \text{ i } a\neq\tfrac{1}{2} \\ 2 & \text{si } a=0 \text{ o } a=\tfrac{1}{2} \end{cases}$$

### c) $C=\begin{pmatrix}2&-1&a\\a&3&4\\3&-1&2\end{pmatrix}$

$$|C| = 2(6+4)+1(2a-12)+a(-a-9)
= 20+(2a-12)+(-a^2-9a)
= -a^2-7a+8$$

Resolem $-a^2-7a+8=0 \Rightarrow a^2+7a-8=0 \Rightarrow (a+8)(a-1)=0$: $a=-8$ o $a=1$.

- Si $a\neq-8$ i $a\neq1$: rang$(C)=3$.

- Si $a=1$: $C=\begin{pmatrix}2&-1&1\\1&3&4\\3&-1&2\end{pmatrix}$. Menor $\begin{vmatrix} 2&-1\\1&3 \end{vmatrix}=7\neq0 \Rightarrow$ rang$(C)=2$.

- Si $a=-8$: $C=\begin{pmatrix}2&-1&-8\\-8&3&4\\3&-1&2\end{pmatrix}$. Menor $\begin{vmatrix} 2&-1\\-8&3 \end{vmatrix}=-2\neq0 \Rightarrow$ rang$(C)=2$.

$$\operatorname{rang}(C) = \begin{cases} 3 & \text{si } a\neq 1 \text{ i } a\neq -8 \\ 2 & \text{si } a=1 \text{ o } a=-8 \end{cases}$$

### d) $D=\begin{pmatrix}1&1&1\\1&-a&1\\1&1&a\end{pmatrix}$

$$|D| = 1(-a^2-1)-1(a-1)+1(1+a)
= -a^2-1-a+1+1+a = -a^2+1$$

Resolem $-a^2+1=0 \Rightarrow a=\pm1$.

- Si $a\neq\pm1$: rang$(D)=3$.

- Si $a=1$: $D=\begin{pmatrix}1&1&1\\1&-1&1\\1&1&1\end{pmatrix}$. Files 1 i 3 iguals, i $\begin{vmatrix} 1&1\\1&-1 \end{vmatrix}=-2\neq0 \Rightarrow$ rang$(D)=2$.

- Si $a=-1$: $D=\begin{pmatrix}1&1&1\\1&1&1\\1&1&-1\end{pmatrix}$. Files 1 i 2 iguals, i $\begin{vmatrix} 1&1\\1&-1 \end{vmatrix}=-2\neq0 \Rightarrow$ rang$(D)=2$.

$$\operatorname{rang}(D) = \begin{cases} 3 & \text{si } a\neq 1 \text{ i } a\neq -1 \\ 2 & \text{si } a=1 \text{ o } a=-1 \end{cases}$$
