<h1 align="center">13/12/2012 - 2° fecha</h1>

## 1. Pueden existir dos conjuntos $A$ y $B$ tales que $|A| = |B| = |A \cup B|$, con $A \cap B = \emptyset$

### a. Sí

### b. No

### c. No sabe / No contesta

## 2. Dada la siguiente máquina de Turing:

### $M = \langle Q, \Sigma, \Gamma, \delta, q_0, F\rangle$

### $Q = \lbrace q_0, q_1,  \rbrace$

---

<h1 align="center">2014 - 1° fecha</h1>

---

<h1 align="center">2014 - 2° fecha</h1>

---

<h1 align="center">2014 - 3° fecha</h1>

---

<h1 align="center">2022 - 1° fecha</h1>

## 1) Dada la máquina de Turing $M_f$ y los lenguajes $L_1$, $L_2$, $L_3$ y $L_4$, marcar sólo las afirmaciones verdaderas.

- $Q = \lbrace q_0 \rbrace$
- $\Sigma = \lbrace 0, 1 \rbrace$
- $\Gamma = \lbrace 0, 1, B \rbrace$
- $\delta(q_0, 0) = (q_0, 1, D)$
- $\delta(q_0, 1) = (q_0, 0, D)$
- $\delta(q_0, B) = (q_d, B, D)$
- $L_1 = \lbrace 0^n 1^m \mid n, m \geq 0 \rbrace$
- $L_2 = \lbrace 1^n 0^m \mid n, m \geq 0 \rbrace$
- $L_3 = \lbrace 0 w 1 \mid w \in \Sigma^* \rbrace$
- $L_4 = \lbrace 1 w 0 \mid w \in \Sigma^*\rbrace$

### a) $M_f$ computa una función de reducibilidad que permite afirmar que $L_1$ reduce a $L_2$.

✅, la función computada por $M_f$ invierte todos los bits de la cadena de entrada, lo cual se condice con la relación clara que se ve entre $L_1$ y $L_2$. Por ejemplo, la cadena $011$ de $L_1$ se mapea a la cadena $100$ de $L_2$.

### b) $M_f$ computa una función de reducibilidad que permite afirmar que $L_2$ reduce a $L_1$.

✅, misma razón que en a), pero en sentido inverso. Por ejemplo, la cadena $100$ de $L_2$ se mapea a la cadena $011$ de $L_1$.

### c) $M_f$ computa una función de reducibilidad que permite afirmar que $L_3$ reduce a $L_4$.

✅, $L_3$ es un lenguaje muy similar a $L_1$ solo que no incluye a la cadena vacía y agrega un cero al principio y un uno al final de cada cadena. Lo mismo ocurre con $L_4$ respecto a $L_2$. Por lo tanto, la función computada por $M_f$ también mapea cadenas de $L_3$ a cadenas de $L_4$ invirtiendo todos los bits. Por ejemplo, la cadena $0011$ de $L_3$ se mapea a la cadena $1100$ de $L_4$.

### d) $M_f$ computa una función de reducibilidad que permite afirmar que $L_4$ reduce a $L_3$.

✅, misma razón que en c), pero en sentido inverso. Por ejemplo, la cadena $1100$ de $L_4$ se mapea a la cadena $0011$ de $L_3$.

### e) $M_f$ computa una función de reducibilidad que permite afirmar que $L_1$ reduce a $L_4$.

❌, la reducción no se cumple porque no toda cadena de $L_1$ es mapeada por la función a una cadena de $L_4$. Contraejemplo: si viene la cadena $\lambda$ que está en $L_1$, la función la mapea a $\lambda$ que NO está en $L_4$.

### f) $M_f$ computa una función de reducibilidad que permite afirmar que $L_1$ reduce a $L_3$.

❌, la reducción no se cumple porque no toda cadena de $L_1$ es mapeada por la función a una cadena de $L_3$. Contraejemplo: si viene la cadena $\lambda$ que está en $L_1$, la función la mapea a $\lambda$ que NO está en $L_3$.

## 2) Sea $\mathscr{L}$ el conjunto de todos los lenguajes definidos sobre $\Sigma$.

### a) $\mathscr{L} - R = \emptyset$

❌, contraejemplo: $L_D \notin R$, por lo que $(\mathscr{L} - R) \neq \emptyset$.

### b) $RE - R \neq \emptyset$

✅, hay lenguajes que son $RE$ pero no $R$. Por ejemplo $HP$.

### c) $\lbrace \lambda \rbrace \in (\mathscr{L} - \text{CO-RE})$

❌, $\lbrace \lambda \rbrace$ es un lenguaje decidible, por lo que está en $R$. Dado que $R \subseteq \text{CO-RE}$, entonces $\lbrace \lambda \rbrace$ está en $\text{CO-RE}$. Por lo tanto no puede ocurrir que $\lbrace \lambda \rbrace \in (\mathscr{L} - \text{CO-RE})$.

### d) $\Sigma^* \in R$

✅, $\Sigma^*$ es decidible porque existe una MT que acepta cualquier cadena de entrada y siempre se detiene.

## 3) Marcar solo las afirmaciones verdaderas.

### a) La cardinalidad de $\mathbb{N}$ es mayor que la cardinalidad de los pares.

❌, existe una función inyectiva de $\mathbb{N}$ en los números pares y además existe otra función inyectiva de los números pares en $\mathbb{N}$. Por lo tanto las cardinalidades son iguales.

### b) La cardinalidad de $\mathbb{N}$ es igual a la cardinalidad de $\mathbb{N} - \lbrace 1, 2, 3, 4, 5 \rbrace$

✅, existe una función inyectiva de $\mathbb{N}$ en $\mathbb{N} - \lbrace 1, 2, 3, 4, 5 \rbrace$ y además existe otra función inyectiva de $\mathbb{N} - \lbrace 1, 2, 3, 4, 5 \rbrace$ en $\mathbb{N}$. Por lo tanto las cardinalidades son iguales.

### c) La cardinalidad de $\mathbb{N}$ es mayor a la cardinalidad de $\mathbb{N} - \lbrace n \mid n > 1000000000000 \rbrace$

✅, como $\mathbb{N} - \lbrace n \mid n > 1000000000000 \rbrace$ es igual a un conjunto finito, entonces su cardinalidad es estrictamente menor que la cardinalidad de $\mathbb{N}$. Esto se debe a que el conjunto $\lbrace n \mid n > 1000000000000 \rbrace$ es INFINITO.

### d) La cardinalidad de los racionales es igual que la cardinalidad de $\mathbb{N}$.

✅, existe una función inyectiva de $\mathbb{N}$ en los números racionales y además existe otra función inyectiva de los números racionales en $\mathbb{N}$. Por lo tanto las cardinalidades son iguales.

## 4) Marcar sólo las afirmaciones verdaderas.

### a) La reducción polinomial es simétrica.

❌, si $L_1 \space \alpha_p \space L_2$, no necesariamente implica que $L_2 \space \alpha_p \space L_1$.

### b) La reducción polinomial es antisimétrica.

❌, si $L_1 \space \alpha_p \space L_2$ y $L_2 \space \alpha_p \space L_1$, no necesariamente implica que $L_1 = L_2$.

### c) Si $L_1$ y $L_2$ son lenguajes pertenecientes a $P$, entonces es posible reducir polinomialmente $L_1$ a $L_2$ y $L_2$ a $L_1$, asumiendo que ambos son distintos de $\emptyset$ y de $\Sigma^*$.

✅, se sabe por teorema que todo lenguaje $L$ se puede reducir polinomialmente a cualquier otro lenguaje que no sea ni el lenguaje vacío ni $\Sigma^*$. Debido a esto, es posible que exista una reducción polinomial de $L_1$ a $L_2$ y de $L_2$ a $L_1$ en este caso.

## 5) Marcar solo las afirmaciones verdaderas.

### $L_1 = \lbrace 0^n1 \mid n > 0 \rbrace$, $L_2 = \emptyset$

### a) $L_1$ reduce a $L_2$.

❌, ningún lenguaje se puede reducir al lenguaje vacío excepto el mismo lenguaje vacío.

### b) $L_1$ reduce a $HP$.

✅, se puede construir una reducción de $L_1$ a $HP$.

### c) $TSP$ reduce a $L_1$.

✅, $TSP$ es decidible y $L_1$ también, y se sabe que cualquier lenguaje decidible se puede reducir a cualquier otro lenguaje decidible que no sea ni el lenguaje vacío ni $\Sigma^*$. Por lo tanto, $TSP$ reduce a $L_1$.

### d) $TSP$ reduce a $HP$.

✅, sí, porque como $TSP$ es $NPC$, es $NPH$ también, y se sabe que $HP$ es $NPH$. Por lo tanto, $TSP$ reduce a $HP$.

## 6) Marcar sólo las afirmaciones verdaderas.

### Desde el punto de vista de análisis de algoritmos, teniendo en cuenta los algoritmos Divide And Conquer para la multiplicación de matrices de Strassen y el algoritmo tradicional:

### a) El algoritmo tradicional es mejor que el de Strassen.

❌, el algoritmo tradicional es peor que el de Strassen.

### b) El algoritmo tradicional es igual que el de Strassen.

❌, idem a)

### c) El algoritmo tradicional es del orden de $O(n^{log_2 7})$ y el de Strassen es del orden de $O(n^3)$.

❌, el algoritmo tradicional es del orden de $O(n^3)$ y el de Strassen es del orden de $O(n^{log_2 7})$.

## 7) Marcar sólo las afirmaciones verdaderas.

### a) Si $P = NP$, entonces $HP$ está en $R$.

❌, $P = NP$ solo implica que problemas que hasta ahora se consideran extremadamente ineficientes de resolver son en realidad posibles de resolver de forma eficiente. No dice nada sobre la decibilidad de los lenguajes.

### b) Si $L$ pertenece a $NPC$ y se demuestra que $L$ reduce polinomialmente a un lenguaje de $P$, entonces se habrá demostrado que $P = NP$.

✅, como todo lenguaje $NPC$ está tanto en $P$ como en $NP$, si se demuestra que un lenguaje $NPC$ reduce polinomialmente a un lenguaje de $P$, entonces se habrá demostrado que $P = NP$.

### c) Si $L_1$ es un lenguaje de $NPC$ y se puede reducir polinomialmente a un lenguaje $L_2$ entonces $L_2$ es un lenguaje de $NPH$.

✅, como $L_1$ es $NPC$, todo lenguaje $NP$ se reduce a $L_1$. Luego, si se puede reducir polinomialmente $L_1$ a $L_2$, por transitividad de la reducción polinomial, todo lo que se reducía a $L_1$ ahora se reduce a $L_2$. Por lo tanto, $L_2$ es al menos igual de difícil que cualquier lenguaje en $NP$, por lo que $L_2$ es $NPH$.

---

<h1 align="center">2023 - 1° fecha</h1>

## 1) Marcar sólo las afirmaciones verdaderas

### a) La cardinalidad de $\mathbb{N}$ es igual a la cardinalidad de los pares

✅, existe una función inyectiva de $\mathbb{N}$ en los números pares y además existe otra función inyectiva de los números pares en $\mathbb{N}$.

### b) La cardinalidad de $\mathbb{N}$ es igual a la cardinalidad de los racionales

✅, existe una función inyectiva de $\mathbb{N}$ en los números racionales y además existe otra función inyectiva de los números racionales en $\mathbb{N}$.

### c) La cardinalidad de $\mathbb{N}$ es igual a la cardinalidad de los reales

❌, los reales tienen una cardinalidad estrictamente mayor que la de los naturales porque son incontables, mientras que los naturales son contables.

### d) Todas las anteriores son falsas

❌, las afirmaciones a) y b) son verdaderas.

## 2) Marcar sólo las afirmaciones verdaderas

### a) La reducción es reflexiva

✅, todo lenguaje se reduce a sí mismo mediante la función identidad.

### b) La reducción es simétrica

❌, si $L_1 \space \alpha_p \space L_2$, no necesariamente implica que $L_2 \space \alpha_p \space L_1$.

### c) La función de reducción entre dos lenguajes debe ser computada por una MT en tiempo polinomial

❌, la función de reducción debe ser total y computable. No importa si en tiempo polinomial o no.

### d) Todas las anteriores son falsas

❌, la afirmación a) es verdadera.

## 3) Marcar sólo las afirmaciones verdaderas acerca de los lenguajes:

- $L_1 = \emptyset$
- $L_2 = \lbrace \lambda \rbrace$
- $L_3 = \Sigma^* \cup L_1$
- $L_4 = \Sigma^* \cup L_2$
- $L_5 = \Sigma^*$

### a) $L_1$ es igual a $L_2$

❌, $L_1$ no contiene ninguna cadena, mientras que $L_2$ contiene la cadena vacía $\lambda$.

### b) La cardinalidad de $L_1$ es igual a la cardinalidad de $L_2$

❌, $|L_1| = 0$ y $|L_2| = 1$.

### c) Una MT que acepte $L_3$ también aceptará $L_4$ y $L_5$

✅, $L_3$ es igual a $\Sigma^*$, dado que la unión con el conjunto vacío no agrega ningún elemento. Además, $L_4$ es igual a $\Sigma^*$ también, dado que el conjunto con la cadena vacía ya está contenido en $\Sigma^*$. Por lo tanto, $L_3 = L_4 = L_5 = \Sigma^*$. Entonces, una MT que acepte $L_3$ también aceptará $L_4$ y $L_5$.

### d) La cardinalidad de ($L_5 - L_1$) es igual a la cardinalidad de ($L_5 - L_2$)

✅, quitarle un elemento a un conjunto infinito contable no cambia su cardinalidad. Entonces, $|L_5 - L_1| = |\Sigma^*|$ y $|L_5 - L_2| = |\Sigma^* - \lbrace \lambda \rbrace|$, y ambos tienen la misma cardinalidad.

### e) Todas las anteriores son falsas

❌, las afirmaciones c) y d) son verdaderas.

## 4) Marcar sólo las afirmaciones verdaderas: en qué casos puede existir la reducción polinomial $L_1 \space \alpha_p \space L_2$?

- a)
  - $L_1 = \lbrace 0^n1 \mid n > 0 \rbrace$
  - $L_2 = \emptyset$
- b)
  - $L_1 = \Sigma^*$
  - $L_2 = \lbrace 0^n1 \mid n > 0 \rbrace$
- c)
  - $L_1 = L_D$
  - $L_2 = \lbrace 0^n1 \mid n > 0 \rbrace$
- d)
  - $L_1 = \lbrace 0^n1 \mid n > 0 \rbrace$
  - $L_2 = L_D$

$L_D$ es el Lenguaje Diagonal definido en la teoría.

### a) En (a) puede existir la reducción polinomial de $L_1$ a $L_2$

❌, no puede existir una reducción polinomial de un lenguaje no vacío a un lenguaje vacío, ya que no hay forma de mapear las cadenas que están en $L_1$ a cadenas en $L_2$.

### b) En (b) puede existir la reducción polinomial de $L_1$ a $L_2$

✅, puede existir una reducción polinomial de $L_1$ a $L_2$. Por ejemplo, la función de reducción podría mapear cualquier cadena en $\Sigma^*$ a una cadena en $L_2$ (por ejemplo, mapear cualquier cadena a "01").

### c) En (c) puede existir la reducción polinomial de $L_1$ a $L_2$

❌, no puede existir una reducción polinomial de un lenguaje que no es $RE$ ($L_D$) a un lenguaje que sí es $RE$ ($\lbrace 0^n1 \mid n > 0 \rbrace$). Esto es porque se sabe por teorema que si $L_1 \space \alpha_p \space L_2$ y $L_2 \in RE$, entonces $L_1$ también debe estar en $RE$. Pero $L_D$ no está en $RE$.

### d) En (d) puede existir la reducción polinomial de $L_1$ a $L_2$

✅, se sabe por teorema que todo lenguaje $L$ se puede reducir polinomialmente a cualquier otro lenguaje que no sea ni el lenguaje vacío ni $\Sigma^*$. Debido a esto, es posible que exista una reducción polinomial de $L_1$ a $L_2$ en este caso.

### e) Todas las anteriores son falsas

❌, las afirmaciones b) y d) son verdaderas.

## 5) Marcar sólo las afirmaciones verdaderas

### a) $\emptyset \in RE$

✅, existe una MT que rechaza cualquier cadena de entrada y siempre se detiene, por lo que acepta el lenguaje vacío.

### b) Si $L$ es un lenguaje formado por una sola palabra, entonces $L \in R$

✅, todo lenguaje finito es decidible. Como $L$ posee una sola palabra, claramente es finto, por lo que $L \in R$.

### c) Si $L$ es un lenguaje finito, entonces $L \in R$

✅, idem b).

### d) Si $L$ es un lenguaje infinito contable, entonces $L \in RE$

❌, no todo lenguaje infinito contable está en $RE$. Como se sabe que todo lenguaje es un subconjunto de $\Sigma^*$, y se sabe que $\Sigma^*$ es infinito contable, entonces existen muchos lenguajes infinitos contables que no están en $RE$. Por ejemplo, el lenguaje diagonal $L_D$ es infinito contable pero no está en $RE$.

### e) Todas las anteriores son falsas

❌, las afirmaciones a), b) y c) son verdaderas.

## 6) Sea $M$ la MT definida a continuación, marcar sólo las afirmaciones verdaderas (Todas las $\delta$ que faltan conducen a $q_R$)

- $Q = \lbrace q_0, q_1 \rbrace$
- $\Sigma = \lbrace 0, 1 \rbrace$
- $\Gamma = \lbrace 0, 1, B \rbrace$
- $\delta(q_0, 0) = (q_1, B, D)$
- $\delta(q_1, B) = (q_A, B, D)$
- $\delta(q_1, 0) = (q_A, 0, D)$
- $\delta(q_1, 1) = (q_A, 1, D)$

### a) $L(M) = \Sigma^*$

❌, si la cadena empieza con un uno o con blanco, la MT se detiene en $q_R$ sin aceptar. Por lo tanto, no acepta todas las cadenas de $\Sigma^*$.

### b) $L(M) = \lbrace 0w \mid w \in \Sigma^* \rbrace$

✅, porque primero se chequea que el primer símbolo de la cadena sea cero. Luego se detiene en $q_A$ sin importar qué símbolo le siga a ese cero, si otro cero, un uno, o simplemente blanco.

### c) $L(M) = \lbrace 0, 00, 01 \rbrace$

❌, la MT acepta muchas más cadenas además de estas tres. Por ejemplo, acepta $000$, $001$, $010$, $011$, etc.

### d) $L(M) = \lbrace \lambda, 0, 00, 01 \rbrace$

❌, la MT dada no acepta la cadena vacía.

### e) Ninguno de los anteriores

❌, la afirmación b) es verdadera.

## 7) Marcar sólo las afirmaciones verdaderas acerca del $t(n)$ del siguiente algoritmo:

```
p = 0
for i = 1  to n do
    for j = 1 to n^2 do
        for k = 1 to n^3 do
            p = p + 1
```

### A) $t(n)$ es de $O(n)$

❌, el número total de iteraciones es $n \cdot n^2 \cdot n^3 = n^6$, por lo que no es de $O(n)$.

### B) $t(n)$ es de $O(n^3)$

❌, el número total de iteraciones es $n \cdot n^2 \cdot n^3 = n^6$, por lo que no es de $O(n^3)$.

### C) $t(n)$ es de $O(n^6)$

✅, el número total de iteraciones es $n \cdot n^2 \cdot n^3 = n^6$.

### D) $t(n)$ es de $O(n)$ en el mejor caso y $O(n^6)$ en el peor caso

❌, el número de iteraciones es siempre $O(n^6)$, no hay un caso mejor.

### E) Todas las afirmaciones anteriores son falsas

❌, la afirmación b) es verdadera.

---

<h1 align="center">2024 - 1° fecha</h1>

## 1) ¿Cuál de las siguientes opciones representa una función inyectiva de $\mathbb{N} \times \mathbb{N}$ en $\mathbb{N}$? Esta función puede utilizarse para demostrar que $|\mathbb{N} \times \mathbb{N}| \leq |\mathbb{N}|$

### A) $f(i, j) = i + j$

❌, no es una función inyectiva. Contraejemplo: $f(1, 2) = 3$ y $f(2, 1) = 3$.

### B) $f(i, j) = 2i + j$

❌, no es una función inyectiva. Contraejemplo: $f(1, 2) = 4$ y $f(2, 0) = 4$.

### C) $f(i, j) = i \times j$

❌, no es una función inyectiva. Contraejemplo: $f(2, 1) = 2$ y $f(1, 2) = 2$.

### D) $f(i, j) = \frac{(i + j)(i + j + 1)}{2} + i$

✅, esta es la función de Cantor, que es inyectiva y mapea $\mathbb{N} \times \mathbb{N}$ en $\mathbb{N}$.

### E) $f(i, j) = i^2 + j^2$

❌, no es una función inyectiva. Contraejemplo: $f(1, 2) = 5$ y $f(2, 1) = 5$.

## 2) Dados los lenguajes $L_1 = \emptyset$ y $L_2 = \lbrace \lambda \rbrace$, ¿cuál de las siguientes afirmaciones es verdadera?

### A) $L_1 = L_2$

❌, $L_1$ no contiene ninguna cadena, mientras que $L_2$ contiene la cadena vacía $\lambda$.

### B) $L_1 \subset L_2$

✅, $L_1$ está contenido en $L_2$ porque el conjunto vacío es subconjunto de cualquier conjunto.

### C) $L_2 \subset L_1$

❌, ningun conjunto es subconjunto del conjunto vacío, excepto el mismo conjunto vacío.

### D) $L_1 \cap L_2 = \lbrace \lambda \rbrace$

❌, la intersección entre el conjunto vacío y cualquier otro conjunto es el conjunto vacío.

### E) $L_1 \cup L_2 = \Sigma^*$

❌, la unión de $L_1$ y $L_2$ es simplemente $L_2$, que contiene solo la cadena vacía $\lambda$. Como $\Sigma^*$ contiene todas las cadenas posibles, incluyendo $\lambda$, pero también muchas otras, la unión no es igual a $\Sigma^*$.

## 3) ¿Cuál de las siguientes opciones describe correctamente la función de transición en una Máquina de Turing de 3 cintas?

### A) $\delta: Q \times \Gamma \rightarrow Q \cup \lbrace qA, qR \rbrace \times \Gamma \times \lbrace D, I \rbrace$

❌, esta es la función de transición para una Máquina de Turing de una sola cinta.

### B) $\delta: Q \times \Gamma^3 \rightarrow Q \cup \lbrace qA, qR \rbrace \times (\Gamma \times \lbrace D, I, S \rbrace)^3$

✅, esta es la función de transición para una Máquina de Turing de 3 cintas.

### C) $\delta: Q^3 \times \Gamma^3 \rightarrow Q \cup \lbrace qA, qR \rbrace \times \Gamma \times \lbrace D, I, S \rbrace^3$

❌, la función de transición no debe tomar $Q^3$ como entrada, sino solo $Q$.

### D) $\delta: Q^3 \times \Gamma \rightarrow Q \cup \lbrace qA, qR \rbrace \times (\Gamma \times \lbrace D, I \rbrace)$

❌, idem C).

### E) $\delta: Q^3 \times \Gamma \rightarrow Q^3 \cup \lbrace qA, qR \rbrace \times \Gamma \times \lbrace D \rbrace$

❌, idem C).

## 4) Si $L = \lbrace \langle M \rangle \mid M \text{ siempre se detiene}\rbrace$ y $L_R = \lbrace \langle M \rangle \mid L(M) \in R\rbrace$, entonces:

$L$ es el conjunto de códigos binarios de MT tal que la MT siempre se detiene para cualquier entrada. Dicho de otra forma, son MT decidibles. Esto implica que el lenguaje aceptado por la MT es un lenguaje decidible.

$L_R$ es el conjunto de códigos binarios de MT tal que el lenguaje aceptado por la MT es un lenguaje decidible. Que la MT reconozca un lenguaje decidible no implica que la MT siempre se detenga para cualquier entrada, ya que puede haber otras MT que reconozcan el mismo lenguaje pero que no siempre se detienen.

### A) $L \subset L_R$

✅, si una MT siempre se detiene, entonces el lenguaje que acepta es decidible, por lo que $L$ está contenido en $L_R$.

### B) $L_R \subset L$

❌, no todas las MT que reconocen lenguajes decidibles siempre se detienen para cualquier entrada.

### C) $L = L_R$

❌, como se cumple $L \subset L_R$ pero no se cumple $L_R \subset L$, entonces no pueden ser iguales.

### D) $L \cap L_R = \emptyset$

❌, como $L$ está contenido en $L_R$, su intersección no puede ser vacía.

### E) $L \cup L_R = RE$

❌, $L$ y $L_R$ no cubren todos los lenguajes recursivamente enumerables. Ejemplo: El lenguaje Halting Problem está en $RE$ pero no está en $L_R$ ni en $L$.

## 5) Si existe una reducción de $L_1$ a $L_2$ $(L_1 \space \alpha \space L_2)$ y se sabe que $L_2 \in R$ ¿qué se puede afirmar de $L_1$?

### A) $L_1 \in (RE - R)$

❌, si $L_2$ es decidible y $L_1$ se reduce a $L_2$, entonces $L_1$ también es decidible, por lo que no puede estar en $RE - R$.

### B) $L_1 \in R$

✅, si $L_1$ se reduce a $L_2$ y $L_2$ es decidible, entonces $L_1$ también es decidible.

### C) $L_1 \notin RE$

❌, si $L_1$ se reduce a $L_2$ y $L_2$ es decidible, entonces $L_1$ también es decidible, por lo que está en $RE$ porque $R \subseteq RE$.

### D) No se puede afirmar nada sobre $L_1$

❌, sí se puede afirmar que $L_1$ es decidible.

### E) Todas las afirmaciones anteriores son falsas

❌, la afirmación B es verdadera.

## 6) ¿Cuál de las siguientes afirmaciones sobre la notación asintótica es falsa?

### A) $n^3 \in O(n^2)$

❌, $n^3$ crece más rápido que $n^2$, por lo que no puede estar en $O(n^2)$.

### B) $(\frac{1}{2}n^2 - 3n) \in \Theta(n^2)$

✅

### C) $n^2 \in O(n^3)$

✅

### D) $2^n \in \Theta(2^{n+1})$

✅

### E) $n! \in O((n + 1)!)$

✅

## 7) Si $L_1$ se reduce polinomialmente a $L_2$ $(L_1 \space \alpha_p \space L_2)$ y $L_1 \in NPC$, entonces:

### A) $L_2$ debe estar en $P$.

❌, no necesariamente. Un lenguaje $NPC$ puede reducirse a un lenguaje que no está en $P$. Contraejemplo: $L_1 = SAT$ y $L_2 = HP$. Sabemos que $SAT \in NPC$ y que $SAT \space \alpha_p \space HP$, pero $HP \notin P$.

### B) $L_2$ debe estar en $NP$.

❌, no necesariamente. Un lenguaje $NPC$ puede reducirse a un lenguaje que no está en $NP$.

### C) Si $L_2 \in NP$, entonces $L_2 \in NPC$.

✅, si $L_1$ es $NPC$ y se reduce polinomialmente a $L_2$, y si además $L_2$ está en $NP$, entonces $L_2$ debe ser $NPC$.

### D) $L_2$ puede o no estar en $NP$.

✅, $L_2$ puede estar en $NP$ o no, ya que la reducción polinomial no implica que $L_2$ deba estar en $NP$.

### E) Ninguna de las afirmaciones anteriores es verdadera.

❌, las afirmaciones C y D son verdaderas.

## 8) Un algoritmo tarda $1$ segundo en procesar $1000$ elementos. Si el tiempo de ejecución es $n^2$, ¿cuánto tardará en procesar $10000$ elementos?

### A) $10$ segundos

❌

### B) $100$ segundos

✅, tenemos que entre $1000$ y $10000$ se multiplica por $10$. Pero como la función es cuadrática, este factor se eleva al cuadrado: $10^2 = 100$. Entonces, si tarda $1$ segundo en procesar $1000$ elementos, tardará $100$ segundos en procesar $10000$ elementos.

### C) $1000$ segundos

❌

### D) $10000$ segundos

❌

### E) $100000$ segundos

❌

---

<h1 align="center">2024 - 2° fecha</h1>

## 1) ¿Cuál o cuáles de las siguientes afirmaciones es verdadera sobre la cardinalidad de $P$ (el conjunto de los números pares)?

### A) $|P| < |\mathbb{N}|$

❌, los números pares se pueden corresponder uno a uno con los números naturales (por ejemplo, mediante la función $f(n) = 2n$), por lo que tienen la misma cardinalidad.

### B) $|P| > |\mathbb{N}|$

❌, idem a).

### C) $|P| = |\mathbb{N}|$

✅, los números pares se pueden corresponder uno a uno con los números naturales (por ejemplo, mediante la función $f(n) = 2n$), por lo que tienen la misma cardinalidad.

### D) $|P| = |\mathbb{Z}|$

✅, los números pares son infinitos contables como los naturales, y se sabe que los números enteros también son infinitos contables, por lo que tienen la misma cardinalidad.

### E) $|P| = |\mathbb{Q}|$

✅, los números pares son infinitos contables como los naturales, y se sabe que los números racionales también son infinitos contables, por lo que tienen la misma cardinalidad.

## 2) ¿Cuál o cuáles de las siguientes opciones representa un lenguaje aceptado por una Máquina de Turing? (Considerar $\Sigma = \lbrace 0,1 \rbrace$)

### A) $L(M) = \lbrace w \in \Sigma^* \mid w \text{ termina en 0} \rbrace$

✅, es un lenguaje válido ya que se puede construir una MT que acepte todas las cadenas que terminan en 0.

### B) $L(M) = \lbrace w \in \Sigma^* \mid w \text{ contiene al menos un 1} \rbrace$

✅, es un lenguaje válido ya que se puede construir una MT que acepte todas las cadenas que contienen al menos un 1.

### C) $L(M) = \lbrace w \in \Sigma^* \mid w \text{ es un número binario terminado en 1} \rbrace$

✅, es un lenguaje válido ya que se puede construir una MT que acepte todos los números binarios que terminan en 1.

### D) $L(M) = \emptyset - \lbrace \lambda \rbrace$

✅, es un lenguaje válido ya que se puede construir una MT que no acepte ninguna cadena y simplemente se detenga rechazando para todo símbolo del alfabeto.

### E) $L(M) = \Sigma^* - \lbrace \lambda \rbrace$

✅, es un lenguaje válido ya que se puede construir una MT que acepte todas las cadenas excepto la cadena vacía.

## 3) ¿Cuál o cuáles de las siguientes afirmaciones describe correctamente la definición de EQUIVALENCIA entre dos Máquinas de Turing (MT)?

### A) Dos MT son equivalentes si tienen el mismo número de estados.

❌, la equivalencia no depende de la cantidad de estados, sino del lenguaje que aceptan.

### B) Dos MT son equivalentes si aceptan el mismo lenguaje.

✅, esta es la definición correcta de equivalencia entre dos MT.

### C) Dos MT son equivalentes si tienen el mismo alfabeto de entrada $(\Sigma)$.

❌, dos MT pueden tener diferentes alfabetos de entrada y aún así ser equivalentes si aceptan el mismo lenguaje.

### D) Dos MT son equivalentes si tienen el mismo alfabeto de entrada $(\Sigma)$ y el mismo alfabeto de cinta $(\Gamma)$.

❌, idem c).

### E) Dos MT son equivalentes si los lenguajes aceptados por ambas tienen exactamente la misma cardinalidad.

❌, la cardinalidad de los lenguajes no es relevante para la equivalencia, lo importante es que acepten el mismo conjunto de cadenas.

## 4) ¿Cuál o cuáles de las siguientes afirmaciones es verdadera?

### A) Un lenguaje $L \in \text{CO-RE}$ si existe una MT $M$ que lo rechaza y siempre se detiene para toda entrada.

❌, CO-RE se define en términos del complemento del lenguaje, no en términos de una MT que lo rechaza.

### B) Un lenguaje $L \in \text{CO-RE}$ si su complemento está en $RE$.

✅, esta es la definición correcta de $CO-RE$.

### C) Un lenguaje $L \in \text{CO-RE}$ si no existe una MT $M$ que lo acepte.

❌, idem a).

### D) Un lenguaje $L \in \text{CO-RE}$ si existe una MT $M$ que lo acepta pero no siempre se detiene para toda entrada.

❌, idem a).

### E) $\text{CO-RE}$ es el complemento de $RE$.

❌, CO-RE está contenido en RE.

## 5) ¿Cual o cuáles de las siguientes afirmaciones describe correctamente el lenguaje Halting Problem $(HP)$?

### A) $HP = \lbrace \langle M, w \rangle \mid M \text{ se detiene con input w} \rbrace$

✅, esta es la definición correcta del Halting Problem.

### B) $HP = \lbrace \langle M \rangle \mid M \text{ se detiene para todo input w}\rbrace$

❌, el Halting Problem se refiere a si una máquina de Turing, dado una cadena de entrada, se detiene en algún momento o no.

### C) $HP = \lbrace \langle M, w \rangle \mid M \text{ acepta w }\rbrace$

❌, idem b).

### D) $HP = \lbrace \langle M, w \rangle \mid M \text{ rechaza w }\rbrace$

❌, idem b).

### E) $HP = \lbrace \langle M, w \rangle \mid M \text{ es una MT válida}\rbrace$

❌, idem b).

## 6) ¿Cuál o cuáles de las siguientes afirmaciones es verdadera sobre la Regla del Limite?

### A) Si $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$, entonces $f(n) \in \Omega(g(n))$.

❌, en este caso, $f(n)$ crece más lentamente que $g(n)$, por lo que $f(n) \in O(g(n))$, pero no en $\Omega(g(n))$.

### B) Si $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$, entonces $f(n) \in O(g(n))$.

❌, en este caso, $f(n)$ crece más rápido que $g(n)$, por lo que $f(n) \in \Omega(g(n))$, pero no en $O(g(n))$.

### C) Si $\lim_{n \to \infty} \frac{f(n)}{g(n)} \in \mathbb{R^+}$, entonces $f(n) \in \Theta(g(n))$.

✅, si el límite es una constante positiva, significa que ambas funciones crecen al mismo ritmo asintóticamente, por lo que $f(n) \in \Theta(g(n))$.

### D) Si $\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0$, entonces $f(n) \in O(g(n))$.

✅, en este caso, $f(n)$ crece más lentamente que $g(n)$, por lo que $f(n) \in O(g(n))$.

### E) Si $\lim_{n \to \infty} \frac{f(n)}{g(n)} = \infty$, entonces $f(n) \in \Omega(g(n))$.

✅, en este caso, $f(n)$ crece más rápido que $g(n)$, por lo que $f(n) \in \Omega(g(n))$.

## 7) Si $L$ es un lenguaje $\text{NP-Hard}$ $(NPH)$

### A) $L$ es un lenguaje que puede ser aceptado por una MTD en tiempo polinomial.

❌, si esto fuera cierto, implicaría que $P = NP$, lo cual no está resuelto.

### B) $L$ es un lenguaje que puede ser aceptado por una MTN en tiempo polinomial.

❌, esto solo sería cierto si $L$ también estuviera en $NP$, pero no todos los lenguajes $NPH$ están a su vez en $NP$.

### C) Para todo lenguaje $L' \in NP$, se cumple que $L' \subseteq L$.

❌, es falso que todo lenguaje en $NP$ esté contenido o sea igual a un lenguaje en $NPH$. Contraejemplo: El lenguaje vacío $\emptyset$ está en $NP$ pero no está contenido en ningún lenguaje $NPH$ porque el lenguaje vacío no contiene ninguna cadena, y por lo tanto no puede contener cadenas de ningún otro lenguaje.

### D) Para todo lenguaje $L' \in NP$, se cumple que $L' \space \alpha_p \space L$.

✅, por definición de $NPH$, todo lenguaje en $NP$ se reduce polinomialmente a cualquier lenguaje en $NPH$.

### E) $L \in NPC$.

❌, no todo lenguaje $NPH$ está en $NPC$. Contraejemplo: $HP \in NPH$ pero $HP \notin NPC$ porque $HP \notin NP$ debido a que $NP$ solo contiene lenguajes **decidibles** y $HP$ no es decidible.

## 8) Marcar sólo las afirmaciones verdaderas acerca del $t(n)$ del siguiente algoritmo:

```
p = 0
for i = 1  to n do
    for j = 1 to n^2 do
        for k = 1 to n^3 do
            p = p + 1
```

### A) $t(n)$ es de $O(n)$

❌, tenemos $n \times n^2 \times n^3 = n^6$, por lo que $t(n)$ no es de $O(n)$

### B) $t(n)$ es de $O(n^3)$

❌, tenemos $n \times n^2 \times n^3 = n^6$, por lo que $t(n)$ no es de $O(n^3)$

### C) $t(n)$ es de $O(n^6)$

✅, tenemos $n \times n^2 \times n^3 = n^6$, por lo que $t(n)$ es de $O(n^6)$

### D) $t(n)$ es de $O(n)$ en el mejor caso y $O(n^6)$ en el peor caso

❌, no hay caso peor ni mejor, siempre es $n^6$

### E) Todas las afirmaciones anteriores son falsas

❌, la afirmación C es verdadera
