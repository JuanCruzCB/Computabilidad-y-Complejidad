<h1 align="center">Práctica 3</h1>

## 1. Construir máquinas de Turing que acepten los siguientes lenguajes

### a. $L_1 = \Sigma^*$

$\dots$

### b. $L_2 = \lbrace λ \rbrace$

$\dots$

### c. $L_3 = \emptyset$

$\dots$

### d. $L_4 = \lbrace 0^n 1^{2n} \mid n \ge 0  \rbrace$

$\dots$

### e. $L_5 = \lbrace a^n b^n c^n \mid n \ge 0  \rbrace$

$\dots$

### f. $L_6 = \lbrace  a^n b^m c^k \mid k = n + m, n, m \ge 1  \rbrace$

$\dots$

### g. $L_7 = \lbrace ww^R \mid w ∈ \lbrace 0,1 \rbrace^* \rbrace$, dónde $w^R$ es el reverso de $w$

$\dots$

### h. $L_8 = L_7 ∪ \lbrace w0w^R \mid w ∈ \lbrace 0,1 \rbrace^* \rbrace ∪ \lbrace w1w^R \mid w ∈ \lbrace 0,1 \rbrace^* \rbrace$

$\dots$

## 2. Construya una Máquina de Turing de 2 cintas que implemente un contador binario en la segunda cinta para contabilizar la cantidad de letras "$a$" que aparecen en el input de la primera cinta. Con $\Sigma = \lbrace a, b \rbrace; \Gamma = \lbrace  a, b, 0, 1, B \rbrace$

$\dots$

## 3. Sea $M$ una máquina de Turing del modelo DIS. ¿Existe una máquina de Turing $M'$ equivalente a $M$ que comience con el cabezal apuntando a cualquier celda de la cinta? Note que $M'$ puede apuntar a una celda no ocupada por el input. ¿Qué puede decir al respecto si se sabe que $\lambda \notin L(M)$? Justifique su respuesta.

Para que $M$ sea equivalente a $M'$, $M'$ debe aceptar el mismo lenguaje que $M$. Es decir, $L(M) = L(M')$.

Si $\lambda \in L(M)$, entonces $M'$ también debe aceptar $\lambda$. Sin embargo, cuando $M'$ comienza, si su cabezal está apuntando a una celda no ocupada por el input (que puede ocurrir por enunciado), entonces no puede determinar si la entrada es $\lambda$ o no, ya que no hay símbolos en la cinta para leer. Por lo tanto, en este caso, $M'$ no puede aceptar $\lambda$ de manera confiable, lo que significa que $L(M')$ no será igual a $L(M)$.

Si $\lambda \notin L(M)$, como se sabe que las cadenas de entrada nunca pueden contener el símbolo blanco, $M'$ puede comenzar en cualquier celda de la cinta sin afectar su capacidad para aceptar o rechazar cadenas, porque puede simplemente moverse a la derecha repetidamente hasta encontrar el inicio del input. En este caso, $M'$ puede ser diseñado para moverse a la derecha hasta encontrar el primer símbolo no blanco y luego proceder exactamente como $M$. Por lo tanto, en este caso, se puede afirmar que existe una máquina de Turing $M'$ equivalente a $M$ que comienza con el cabezal apuntando a cualquier celda de la cinta.

## 4. Probar que para toda máquina de Turing $M$ reconocedora del modelo DIS, existe una máquina de Turing $M'$ equivalente con la restricción que no puede cambiar el símbolo de la cinta y mover el cabezal simultáneamente, es decir:

### $\delta'(q_i, a_k) = (q_j, a_l, X) \mid a_k \ne a_l \rightarrow X = S$

$\dots$

## 5. Probar que para toda máquina de Turing $M$ reconocedora del modelo DIS, existe una máquina de Turing $M'$ equivalente con la restricción que no puede cambiar de estado y mover el cabezal simultáneamente, es decir:

### $\delta'(q_i, a_k) = (q_j, a_l, X) \mid X \in \lbrace D,I \rbrace \rightarrow i = j$

$\dots$
