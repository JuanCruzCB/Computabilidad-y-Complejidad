<h1 align="center">Práctica 2</h1>

## 1. Construir máquinas de Turing que:

### a. Haga un corrimiento a derecha de la cadena binaria en la cinta, marcando con un símbolo especial \# la celda que corresponde al primer símbolo desplazado. $\Gamma = \lbrace B, numeral, 0, 1 \rbrace$.

Si tenemos por ejemplo la cadena $w = 0110$ en la cinta, luego de aplicar el corrimiento a derecha, la cinta debería quedar así: $...numeral 0 1 1 0...$

```
// Cadena vacía
q0, B
qd, #, D

// Cadena que empieza con 0 → q1
q0, 0
q1, #, D

// Cadena que empieza con 1 → q2
q0, 1
q2, #, D

// Si el segundo símbolo es 1 → q2
q1, 1
q2, 0, D

q1, 0
q1, 0, D

q1, B
qd, 0, D

// Si el segundo símbolo es 0 → q1
q2, 0
q1, 1, D

q2, 1
q2, 1, D

q2, B
qd, 1, D
```

### b. Haga un corrimiento a izquierda.

Si tenemos por ejemplo la cadena $w = 0110$ en la cinta, luego de aplicar el corrimiento a izquierda, la cinta debería quedar así: $...0 1 1 0 numeral...$

```
// Ir al final de la cadena
q0, 0
q0, 0, D

q0, 1, D
q0, 1, D

q0, B
q1, B, I

// Poner el símbolo # al final de la cadena
q1, 0
q2, #, I

q1, 1
q3, #, I

// Poner ceros
q2, 0
q2, 0, I

q2, 1
q3, 0, I

q2, B
qd, 0, I

// Poner unos
q3, 0
q2, 1, I

q3, 1
q3, 1, I

q3, B
qd, 1, I
```

## 2. Construir MT:

### a. Construir una máquina de Turing $M$ tal que $L(M) = \lbrace 0^n1^n \mid n \ge 1 \rbrace$ y mostrar la traza de computación de $M$ para las entradas $w_1 = 0011$ y $w_2 = 011$.

Las cadenas de este lenguaje son aquellas que contienen una cantidad igual de ceros y unos, con todos los ceros antes que los unos. Por ejemplo: $01, 0011, 000111, 00001111$, etc. Claramente $\lambda \notin L$.

La solución consiste en asegurarse de que por cada 0 que se encuentre en la cadena, exista un 1 correspondiente. Por lo tanto se encuentra un 0, se borra, se encuentra un 1, se borra, y se repite el proceso hasta que no queden más 0s. Si al finalizar no quedan 1s, la cadena es aceptada.

```
// Si la cadena es lambda o empieza con 1, se rechaza. Si no, se pasa a q1 y se borra ese primer 0.
q0, B
qR, B, D

q0, 1
qR, 1, D

q0, 0
q1, B, D

// Contamos los ceros. Si viene 1 se rechaza porque no podemos volver a tener unos.
q1, 0
q1, 0, D

q1, B
qR, B, D

q1, 1
q2, 1, D

// Contamos los unos. Si viene 0 se rechaza porque no podemos volver a tener ceros.
q2, 1
q2, 1, D

q2, 0
qR, 0, D

q2, B
q3, B, I

// Borramos el uno de más a la derecha
q3, 1
q4, B, I

// Buscamos el primer blanco o cero
q4, 1
q4, 1, I

q4, 0
q5, 0, I

q4, B
q6, B, D

// Encontramos el 0 de más a la izquierda
q5, 0
q5, 0, I

q5, B
q0, B, D

// Si es blanco, se borró la misma cantidad de ceros que de unos y la cadena es válida. Si no, hay más unos que ceros y se rechaza.
q6, B
qA, B, D

q6, 1
qR, 1, D
```

- Traza para $w_1 = 0011$:
  - $q_0 0011 \vdash B q_1 011 \vdash B0 q_1 11 \vdash B01 q_2 1 \vdash B011 q_2 B \vdash B01 q_3 1B \vdash B0 q_4 1BB \vdash B q_4 01BB \vdash q_5 B01BB \vdash B q_0 01BB \vdash BB q_1 1BB \vdash BB1 q_2 BB \vdash BB q_3 1BB \vdash B q_4 BBBB \vdash BB q_6 BBB \vdash BBB q_A BB$
- Traza para $w_2 = 011$:
  - $q_0 011 \vdash B q_1 11 \vdash B1 q_2 11 \vdash B11 q_2 B \vdash B1 q_3 1B \vdash B q_4 1BB \vdash q_4 B1BB \vdash B q_6 1BB \vdash B1 q_R BB$

### b. Construir una máquina de Turing que busque en la cinta el patrón "abab" y se detenga si y sólo si encuentra ese patrón. $\Gamma = \lbrace a, b, c, B \rbrace$

```
// Buscar la primera 'a'
q0, B
q0, B, D

q0, b
q0, b, D

q0, c
q0, c, D

q0, a
q1, a, D

// Buscar la primera 'b'
q1, B,
q0, B, D

q1, a
q0, a, S

q1, c
q0, c, D

q1, b
q2, b, D

// Buscar la segunda 'a'
q2, B
q0, B, D

q2, b
q0, b, D

q2, c
q0, c, D

q2, a
q3, a, D

// Buscar la segunda 'b'
q3, B
q0, B, D

q3, a
q0, a, D

q3, c
q0, c, D

q3, b
qA, b, D
```

## 3. Construir máquinas de Turing para computar las siguientes funciones:

### a. Suma unaria. $\Sigma = \lbrace +, 1 \rbrace$.

```
// Buscar el signo + y poner 1 en su lugar
q0, B
qd, B, D

q0, 1
q0, 1, D

q0, +
q1, 1, I

// Encontrar el primer 1
q1, 1
q1, 1, I

q1, B
q2, B, D

// Borrar el primer 1
q2, 1
qd, B, D
```

### b. Resta unaria $a - b$ con $a > b$. $\Sigma = \lbrace -, 1 \rbrace$.

```
// Buscar el signo -
q0, B
qd, B, D

q0, 1
q0, 1, D

q0, -
q1, -, D

// Encontrar el 1 más a la derecha
q1, 1
q1, 1, D

q1, B
q2, B, I

// Borrar el 1 más a la derecha
q2, 1
q3, B, 1

q2, -
qd, B, I

// Ir hasta el signo -
q3, 1
q3, 1, I

q3, -
q4, -, I

// Encontrar el 1 más a la izquierda
q4, 1
q4, 1, I

q4, B
q5, B, D

// Borrar el 1 más a la izquierda
q5, 1
q0, B, D
```

### c. Calcular el complemento a 2 de un número binario de 8 bits. $\Sigma = \lbrace 0, 1 \rbrace$

```
// Invertir todos los bits
q0, 1
q0, 0, D

q0, 0
q0, 1, D

q0, B
q1, B, I

// Sumar 1, si hace falta se acarrea un uno
q1, 0
qd, 1, I

q1, 1
q2, 0, I

// Sigo sumando ese uno haciendo los corrimientos necesarios
q2, 1
q2, 0, I

q2, 0
qd, 1, I
```

## 4. Sea $\Sigma = \lbrace a \rbrace$ y $w = a$. Decir cuáles son las palabras que se obtienen como resultado de aplicar las siguientes operaciones:

### a. $ww$

$aa$

### b. $www$

$aaa$

### c. $w^3$

$w^3 = www = aaa$

### d. $w^5$

$w^5 = wwwww = aaaaa$

### e. $w^0$

$\lambda$

### ¿Cuáles son sus longitudes?

- $|ww| = 2$
- $|www| = 3$
- $|w^3| = 3$
- $|w^5| = 5$
- $|w^0| = 0$

### Definir $\Sigma^*$.

$$\Sigma^* = \lbrace \lambda, a, aa, aaa, aaaa, ... \rbrace$$

## 5. Idem al ejercicio anterior, pero con $\Sigma = \lbrace a, b \rbrace$ y $w = aba$.

- $ww = abaaba$
- $|ww| = 6$
- $www = abaabaaba$
- $|www| = 9$
- $w^3 = www = abaabaaba$
- $|w^3| = 9$
- $w^5 = wwwww = abaabaabaabaaba$
- $|w^5| = 15$
- $w^0 = \lambda$
- $|w^0| = 0$

$$\Sigma^* = \lbrace \lambda, a, b, aa, bb, ab, ba, aba,... \rbrace$$

## 6. Sea $\Sigma = \lbrace a, b, c \rbrace$, escriba las 13 cadenas más cortas de $\Sigma^*$.

1. $\lambda$
2. $a$
3. $b$
4. $c$
5. $aa$
6. $bb$
7. $cc$
8. $ab$
9. $ac$
10. $ba$
11. $bc$
12. $cb$
13. $ca$

## 7. Dar tres ejemplos de lenguajes basados en el alfabeto $\lbrace 0,1 \rbrace$

1. $L_1 = \lbrace \lambda \rbrace$
2. $L_2 = \emptyset$
3. $L_3 = \Sigma^*$

## 8. ¿Cuántas cadenas de longitud $3$ hay en $\lbrace 0,1, 2 \rbrace^*$, y cuántas de longitud $n$?

Tenemos 3 símbolos en el alfabeto, y cada símbolo de una cadena arbitraria $w$ puede tomar cualquiera de ellos 3. Por lo tanto la cantidad de cadenas de longitud 3 que se pueden generar es igual a $3 \times 3 \times 3 = 27$.

Si queremos cadenas de longitud $n$, se pueden generar $3 \times 3 \times 3 \times ... \times 3$ $n$ veces, lo que equivale a $3^n$.

## 9. Explicar la diferencia (si la hay) entre los lenguajes $L_1$ y $L_2$.

### a. $L_1 = \emptyset$, $L_2 = \lbrace λ \rbrace$

- $L_1$ es el lenguaje vacío, es decir que no contiene ninguna cadena, ni siquiera la cadena vacía $\lambda$.
- $L_2$ no es un lenguaje vacío, contiene una única cadena que es la cadena vacía $\lambda$.
- Por lo tanto $L_1 \ne L_2$.

### b. $L_1 = \Sigma^* ∪ \lbrace λ \rbrace$, $L_2 = \emptyset ∪ \Sigma^*$

- Como $\lbrace \lambda \rbrace \in \Sigma^* \implies \Sigma^* \cup \lbrace λ \rbrace = \Sigma^*$
- Como $\emptyset \in \Sigma^* \implies \emptyset \cup \Sigma^*  = \Sigma^* \cup \emptyset = \Sigma^*$
- Por lo tanto $L_1 = L_2$.

### c. $L_1 = \Sigma^* – \emptyset$, $L_2 = \Sigma^*$

- Como para todo conjunto, restarle $\emptyset$ resulta en ese mismo conjunto, $\Sigma^* – \emptyset = \Sigma^*$
- Por lo tanto $L_1 = L_2$.

### d. $L_1 = \Sigma^* – \lbrace \lambda \rbrace$, $L_2 = \Sigma^*$

- Como $\lbrace \lambda \rbrace \in \Sigma^* \implies \Sigma^* - \lbrace \lambda \rbrace \ne \Sigma^*$
- Por lo tanto $L_1 \ne L_2$.

## 10. Mostrar que $\Sigma^*$ es infinito contable.

Sea $\Sigma$ un alfabeto finito y no vacío. Entonces, $\Sigma^*$ es el conjunto de todas las cadenas posibles (incluyendo la cadena vacía) que se pueden formar con los símbolos de $\Sigma$.

$\Sigma^*$ es infinito porque para cualquier cadena de longitud $n \in \mathbb{N}$, siempre se puede formar una cadena de longitud $n+1$ agregando un símbolo adicional del alfabeto $\Sigma$. Por lo tanto, no hay un límite superior en la longitud de las cadenas que se pueden formar, lo que implica que $\Sigma^*$ es infinito.

$\Sigma^*$ es infinito contable porque se pueden enumerar todos sus elementos creando una correspondencia uno a uno con los números naturales $\mathbb{N}$. Esto se puede lograr mediante el siguiente procedimiento:

1. Se ordenan las cadenas por su longitud: primero la de longitud 0 (la cadena vacía), luego las de longitud 1, luego las de longitud 2, y así sucesivamente.
2. Dentro de cada grupo de cadenas que poseen la misma longitud, se ordenan lexicográficamente (es decir, en orden alfabético).

Por ejemplo, si $\Sigma = \lbrace a, b \rbrace$, la enumeración de $\Sigma^*$ sería:

1. Longitud 0:
   1. $\lambda \rightarrow 0 \in \mathbb{N}$
2. Longitud 1:
   1. $a \rightarrow 1 \in \mathbb{N}$
   2. $b \rightarrow 2 \in \mathbb{N}$
3. Longitud 2:
   1. $aa \rightarrow 3 \in \mathbb{N}$
   2. $ab \rightarrow 4 \in \mathbb{N}$
   3. $ba \rightarrow 5 \in \mathbb{N}$
   4. $bb \rightarrow 6 \in \mathbb{N}$
4. Longitud 3:
   1. $aaa \rightarrow 7 \in \mathbb{N}$
   2. $aab \rightarrow 8 \in \mathbb{N}$
   3. $aba \rightarrow 9 \in \mathbb{N}$
   4. $abb \rightarrow 10 \in \mathbb{N}$
   5. $baa \rightarrow 11 \in \mathbb{N}$
   6. $bab \rightarrow 12 \in \mathbb{N}$
   7. $bba \rightarrow 13 \in \mathbb{N}$
   8. $bbb \rightarrow 14 \in \mathbb{N}$
5. $\dots$

**Así, cada cadena en $\Sigma^*$ puede ser asociada de manera única con un número natural, demostrando que $\Sigma^*$ es infinito contable**.

## 11. Indicar cuál es el lenguaje que se obtiene al intersectar $(\cap)$ los siguientes lenguajes:

### a. $L_1 = \lbrace a^n c^m d^n \mid n \ge 0, m ≥ 0 \rbrace$ con $L_2 = \lbrace c^n \mid n ≥ 0 \rbrace$

$L_1 \cap L_2 = L_2$

### b. $L_1 = \lbrace a^n c^m d^n \mid n > 0, m ≥ 0 \rbrace$ con $L_2 = \lbrace c^n \mid n ≥ 0 \rbrace$

$L_1 \cap L_2 = \emptyset$

### c. $L_1 = \lbrace a^n c^m d^n \mid n \ge 0, m > 10 \rbrace$ con $L_2 = \lbrace c^n \mid n > 5 \rbrace$

$L_1 \cap L_2 = \lbrace c^n \mid n > 10 \rbrace$

### d. $L_1 = \lbrace 1^{2n} 2^{2m + 1} \mid n , m \ge 0 \rbrace$ con $L_2 = \lbrace  2^n \mid n \ge 0 \rbrace$

- $L_1 = \lbrace 2, 222, 22222, \dots, 112, 11112, 1111112, \dots, 11222, 1122222, \dots \rbrace$
- $L_2 = \lbrace \lambda, 2, 22, 222, 2222, 22222, \dots \rbrace$
- $L_1 \cap L_2 = \lbrace \lambda, 2, 222, 22222, \dots \rbrace = \lbrace 2^{2n + 1} \mid n \ge 0 \rbrace$

### e. $L_1 = \lbrace 1^{2n} 2^{2m + 1} \mid n , m \ge 0 \rbrace$ con $L_2 = \lbrace  1^n \mid n \ge 0 \rbrace$

- $L_1 = \lbrace 2, 222, 22222, \dots, 112, 11112, 1111112, \dots, 11222, 1122222, \dots \rbrace$
- $L_2 = \lbrace \lambda, 1, 11, 111, 1111, 11111, \dots \rbrace$
- $L_1 \cap L_2 = \emptyset$

## 12. Encontrar si es posible un lenguaje $L_1$ que cumpla:

### a. $L_1 \cap \lbrace 1^k2^m3^n \mid \text{m = k + n + 1 y n, k} \ge 0 \rbrace = \lbrace 1^n2^{n+1} \mid n \ge 0 \rbrace$

- Llamamos $L_X = \lbrace 1^k2^m3^n \mid \text{m = k + n + 1 y n, k} \ge 0 \rbrace$
- Llamamos $L_Y = \lbrace 1^n2^{n+1} \mid n \ge 0 \rbrace$
- $L_X = \lbrace 2, 12223, 112222233, 1112222222333 \dots 2, 122, 11222, 1112222, 111122222, \dots \rbrace$
- $L_Y = \lbrace 2, 122, 11222, 1112222, \dots \rbrace$
- Se necesita $L_1$ tal que $L_1 \cap L_X = L_Y$
- Por lo tanto $L_1 = \lbrace 1^n2^{n+1} \mid n \ge 0\rbrace$

### b. $L_1 \cap \lbrace 1^n2^m \mid n \ne m \text{ y } n, m \ge 0 \rbrace = \lbrace 1^n2^n \mid n > 0 \rbrace$

- Llamamos $L_X = \lbrace 1^n2^m \mid n \ne m \text{ y } n, m \ge 0 \rbrace$
- Llamamos $L_Y = \lbrace 1^n2^n \mid n > 0 \rbrace$
- (0 y 1; 1 y 0; 2 y 1; 1 y 2, 3 y 1, 1 y 3)
- $L_X = \lbrace 2, 1, 112, 122, \dots \rbrace$
- $L_Y = \lbrace 12, 1122, 111222, 11112222, \dots \rbrace$
- Se necesita $L_1$ tal que $L_1 \cap L_X = L_Y$
- No es posible ya que $L_X \nsubseteq L_Y$

## 13. Conteste las siguientes preguntas sobre Máquinas de Turing

### a. ¿Puede el alfabeto de la cinta $(\Gamma)$ ser el mismo que el alfabeto de entrada $(\Sigma)$?

- Es posible que $\Gamma = \Sigma ?$
- No, porque siempre se cumple que $B \in \Gamma$ y a la vez $B \notin \Sigma$, para cualquier $\Sigma$ y $\Gamma$.

### b. ¿Puede una máquina de Turing tener un único estado?

- Es posible que $|Q| = 1 ?$
- Sí, porque el único estado obligatorio de una MT es el estado inicial $q_0$.

### c. ¿Cuántos lenguajes existen definidos sobre el alfabeto $\Sigma = \lbrace 0,1 \rbrace$? ¿y sobre $\Sigma = \lbrace 1 \rbrace$?

Cualquier subconjunto de $\Sigma^*$ es un lenguaje definido sobre $\Sigma$. Por lo tanto, la cantidad de lenguajes definidos sobre un alfabeto $\Sigma$ es igual a la cantidad de subconjuntos de $\Sigma^*$, que es infinito. Por lo tanto existen infinitos lenguajes definidos sobre cualquier alfabeto finito no vacío, incluyendo $\Sigma = \lbrace 0,1 \rbrace$ y $\Sigma = \lbrace 1 \rbrace$.

### d. ¿Cuáles de los siguientes conjuntos son lenguajes definidos sobre $\Sigma$?

#### i. $\emptyset$

Es un lenguaje porque $\emptyset \subseteq \Sigma^*$. ✅

#### ii. $\Sigma$

Es un lenguaje porque $\Sigma \subseteq \Sigma^*$. ✅

#### iii. $\Sigma^*$

Es un lenguaje porque $\Sigma^* \subseteq \Sigma^*$. ✅

#### iv. $\lbrace λ \rbrace$

Es un lenguaje porque $\lbrace λ \rbrace \subseteq \Sigma^*$. ✅

#### v. $\lbrace λ \rbrace ∪ \Sigma$

Es un lenguaje porque $\lbrace λ \rbrace ∪ \Sigma \subseteq \Sigma^*$. ✅

#### vi. $\lbrace \emptyset \rbrace$

No es un lenguaje porque $\lbrace \emptyset \rbrace \not\subseteq \Sigma^*$. ❌

### e. Sea la siguiente máquina de Turing:

#### $M = \langle Q, \Sigma, \Gamma, \delta, q_0, q_A, q_R \rangle$ tal que:

#### $Q = \lbrace q_0, q_1, q_2, q_3 \rbrace$

#### $\Sigma = \lbrace a, b, c \rbrace$

#### $\Gamma = \lbrace a, b, c, B \rbrace$

#### $\delta(q, s) = (q’, s’, m ) \text{ tal que:}$

##### $q \in Q$

##### $q’ \in Q ∪ \lbrace q_R \rbrace$

##### $s, s’ \in \Gamma, m \in \lbrace D, I \rbrace$

#### ¿Reconoce el lenguaje $\lbrace λ \rbrace$? Si no es así indique cuál es el lenguaje que reconoce.

Como $M$ no posee ninguna transición hacia el estado de aceptación $q_A$, no es capaz de reconocer ningún lenguaje. Por lo tanto $L(M) = \emptyset$.

## 14. Sea $M = \langle Q, \Sigma, \Gamma, \delta, q_0, q_A, q_R \rangle$, en cada caso asumir que los $\delta()$ no especificados son los que hacen detener la MT en $q_R$, determinar $L(M)$:

### a.

#### $Q = \lbrace q_0, q_1 \rbrace$

#### $\Sigma = \lbrace 0,1 \rbrace$

#### $\Gamma = \lbrace 0, 1, B \rbrace$

- $\delta(q_0, 0) = (q_0, 0, I)$
- $\delta(q_0, B) = (q_0, B, D)$
- $\delta(q_0, 1) = (q_1, 1, D)$

Como $M$ no tiene ninguna transición hacia el estado de aceptación $q_A$, no es capaz de reconocer ningún lenguaje. Por lo tanto $L(M) = \emptyset$.

### b.

#### $Q = \lbrace q_0, q_1 \rbrace$

#### $\Sigma = \lbrace 0,1 \rbrace$

#### $\Gamma = \lbrace 0, 1, B \rbrace$

- $\delta(q_0, 0) = (q_1, B, D)$
- $\delta(q_1, B) = (q_A, B, D)$
- $\delta(q_1, 0) = (q_A, 0, D)$
- $\delta(q_1, 1) = (q_A, 1, D)$

$M$ reconoce cadenas que empiezan con un 0. Por lo tanto $L(M) = \lbrace 0w \mid w \in \Sigma^* \rbrace$.

### c.

#### $Q = \lbrace q_0, q_1 \rbrace$

#### $\Sigma = \lbrace 0,1 \rbrace$

#### $\Gamma = \lbrace 0, 1, B \rbrace$

- $\delta(q_0, 0) = (q_0, 0, I)$
- $\delta(q_0, B) = (q_0, B, D)$
- $\delta(q_0, 1) = (q_1, 1, D)$
- $\delta(q_1, 0) = (q_0, B, I)$
- $\delta(q_1, 1) = (q_0, B, D)$

Nuevamente $M$ no tiene ninguna transición hacia el estado de aceptación $q_A$, por lo tanto no es capaz de reconocer ningún lenguaje. $L(M) = \emptyset$.

### d.

#### $Q = \lbrace q_0 \rbrace$

#### $\Sigma = \lbrace 0,1 \rbrace$

#### $\Gamma = \lbrace 0, 1, B \rbrace$

- $\delta(q_0, 1) = (q_0, B, I)$
- $\delta(q_0, 0) = (q_A, B, I)$
- $\delta(q_0, B) = (q_0, B, D)$

$M$ reconoce cadenas que contienen al menos un $0$. Por lo tanto $L(M) = \lbrace w \mid \text{w contiene al menos un cero} \rbrace$.

### e.

#### $Q = \lbrace q_0, q_1 \rbrace$

#### $\Sigma = \lbrace 0, 1 \rbrace$

#### $\Gamma = \lbrace 0, 1, B \rbrace$

- $\delta(q_0, 0) = (q_1, B, D)$
- $\delta(q_1, 0) = (q_1, 1, D)$
- $\delta(q_1, 1) = (q_1, 0, D)$
- $\delta(q_1, B) = (q_A, 1, D)$

$M$ reconoce cadenas que empiezan con un 0. Por lo tanto $L(M) = \lbrace 0w \mid w \in \Sigma^* \rbrace$.
