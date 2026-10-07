---
title: Vectors i geometria a l’espai: Exercicis
tematitol: Vectors i geometria a l’espai
curs: 2n
modalitat: cientific
tema: vectors
bloc: exercicis
ordre: 2
---
# Vectors i geometria a l’espai: Exercicis

## Exercicis de repàs generals

> 1.  Donats els punts $A(2,3,-1)$, $B(0,-4,-3)$ i $P(-1,2,-2)$ (centre d’un paral·lelogram $ABCD$). Determina els vèrtexs $C$ i $D$ i calcula els angles del paral·lelogram.
>
> 2.  Demostra que el baricentre d’un triangle $ABC$ té coordenades: $$G = \left(\frac{a_1+b_1+c_1}{3},\; \frac{a_2+b_2+c_2}{3},\; \frac{a_3+b_3+c_3}{3}\right)$$
>
> 3.  Considera el triangle $ABC$ amb $A(3,-1,2)$, $B(1,0,1)$, $C(-3,2,5)$.
>
>     1.  Calcula el baricentre $G$.
>
>     2.  Calcula el punt mitjà de $BC$, $M_{BC}$.
>
>     3.  Comprova que $A$, $G$ i $M_{BC}$ estan alineats i que $AG = 2\,GM_{BC}$.
>
> 4.  El segment d’origen $A(-1,4,-2)$ i extrem $B$ es divideix en cinc parts iguals. Si el segon punt de divisió és $A_2(1,0,2)$, calcula les coordenades de $B$.
>
> 5.  Indica si és cert o fals, justificant la resposta:
>
>     1.  En $\mathbb{R}^2$, dos vectors LI formen sempre una base.
>
>     2.  En $\mathbb{R}^3$, dos vectors LI formen una base.
>
>     3.  Si $\dim(V)=n$, aleshores $n+1$ vectors de $V$ sempre són LD.

> 1.  Siguin $\vec{u}_1=(1,-3,2)$, $\vec{u}_2=(2,-1,4)$ i $\vec{u}_3=(a+1,a-1,4a+2)$.
>
>     1.  Troba el valor de $a$ per al qual $\vec{u}_3$ és combinació lineal de $\vec{u}_1$ i $\vec{u}_2$.
>
>     2.  Comprova que per a $a=0$ els tres vectors són LI.
>
> 2.  Donats $\vec{v}_1=(a+1,2a,1)$, $\vec{v}_2=(-2,a,2a)$ i $\vec{v}_3=(a,-2,4a-2)$:
>
>     1.  Calcula l’angle entre $\vec{v}_1$ i $\vec{v}_2$ per a $a=0$.
>
>     2.  Esbrina per a quin valor de $a$ els tres vectors són perpendiculars dos a dos.
>
> 3.  Els punts $A(k-3,2,4)$, $B(0,k+2,2)$ i $C(-2,6,k+1)$ són tres vèrtexs consecutius d’un rombe.
>
>     1.  Calcula el valor de $k$.
>
>     2.  Demostra que el rombe és un quadrat.
>
> 4.  Donats $\vec{u}=(1,-1,4)$, $\vec{v}=(2,1,3)$ i $\vec{w}=(1,0,0)$ (LI). Calcula la relació entre $a$ i $b$ perquè $\vec{t}=(a,1,b)$ sigui combinació lineal de $\vec{u}$ i $\vec{v}$.

<details><summary>Solució</summary>

**Solucions dels exercicis de repàs — Nivell alt:**

1.  \(a\) Del sistema: $\lambda_1=\frac{3a-1}{5}$, $\lambda_2=\frac{4a+2}{5}$; substituint: $2a+1=\frac{3a-1}{5}+\frac{8a+4}{5} \Rightarrow a=2$.  
    (b) Per $a=0$, $\vec{u}_3=(1,-1,2)$; plantejant el sistema d’homogènia, la solució única és $\lambda_1=\lambda_2=\lambda_3=0$ $\Rightarrow$ LI.

2.  \(a\) $\vec{v}_1=(1,0,1)$, $\vec{v}_2=(-2,0,0)$; $\cos\alpha=\frac{-2}{{\sqrt{2}\cdot2}}=-\frac{\sqrt{2}}{2}$ $\Rightarrow$ $\alpha=135°$.  
    (b) Imposant $\vec{v}_1\cdot\vec{v}_2=0$, $\vec{v}_1\cdot\vec{v}_3=0$, $\vec{v}_2\cdot\vec{v}_3=0$: solució $a=1$.

3.  \(a\) $|\overrightarrow{AB}|=|\overrightarrow{BC}|$: $\sqrt{(3-k)^2+k^2+4}=\sqrt{4+(4-k)^2+(k-1)^2} \Rightarrow k=2$.  
    (b) Per $k=2$: $\overrightarrow{AB}=(1,2,-2)$, $\overrightarrow{BC}=(-2,2,1)$; $\overrightarrow{AB}\cdot\overrightarrow{BC}=0$ $\Rightarrow$ quadrat.

4.  $(a,1,b)=\lambda(1,-1,4)+\mu(2,1,3)$; de les dues primeres equacions: $\lambda=\frac{a-2}{3}$, $\mu=\frac{a+1}{3}$; substituint a la tercera: $\boxed{7a-3b-5=0}$.

</details>
