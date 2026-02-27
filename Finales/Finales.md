<h1 align="center">Septiembre de 2014</h1>

## 1. ¿Puede demostrarse que un problema no es computacionalmente computable sin el uso de máquinas de Turing? ¿Cómo puede demostrarlo con el uso de máquinas de turing?

Aclarando conceptos clave antes de responder:

1. **Definición de computabilidad**:
   1. Un problema es **computacionalmente computable** si existe un algoritmo que, dada cualquier entrada válida, produce la salida correcta en un tiempo finito.
   2. Sea el conjunto de entradas válidas: $I = \{i_1,i_2,i_3,\dots\}$
   3. No importa si $I$ es infinito: lo relevante es que el algoritmo **termine para cada entrada individual**.
   4. No se exige que el algoritmo procese todas las entradas, solo que siempre termine cuando recibe una.
   5. Un problema es **no computable** si no existe ningún procedimiento efectivo que garantice terminación para todas sus entradas.

2. **Formalización del concepto de problema**:
   1. En teoría de la computación, un problema suele modelarse como un **lenguaje formal** $L \subseteq \Sigma^*$ donde $\Sigma^*$ es el conjunto infinito contable de todos los strings finitos posibles que se pueden formar dado un alfabeto finito $\Sigma$.
   2. Resolver el problema equivale a decidir si un string dado pertenece o no a $L$.

3. **Demostración sin usar máquinas de Turing (argumento de cardinalidad)**:
   1. Todo algoritmo puede describirse con una secuencia finita de símbolos.
   2. Por lo tanto, el conjunto de algoritmos es **infinito contable** (se puede asociar un número natural a cada algoritmo).
   3. Los problemas corresponden a subconjuntos de $\Sigma^*$.
   4. El conjunto de todos los problemas posibles dado un conjunto infinito de strings sobre un alfabeto finito $\Sigma$ es el conjunto potencia: $\mathcal{P}(\Sigma^*)$
   5. Se sabe por teorema de Cantor que el conjunto potencia de un conjunto infinito contable es **infinito incontable**.

Como el conjunto de todos los problemas posibles dado un alfabeto es infinito incontable, y el conjunto de todos los algoritmos es infinito contable, entonces hay estrictamente más problemas que algoritmos. Por lo tanto, obviamente, existen problemas para los cuales **no puede existir ningún algoritmo** que los resuelva, es decir, problemas no computables.

Si usamos máquinas de Turing, se puede demostrar que existen problemas no computables con, por ejemplo, el Halting Problem, mostrando que no existe una máquina de Turing que pueda decidir si otra máquina de Turing se detiene o no para todas las entradas posibles. Lo anterior se logra usando reducciones.

## 2. ¿Existe una reducción de $L_1 = \lbrace \lambda \rbrace$ a $L_2 = \lbrace 0^n1^n \mid n > 0 \rbrace$? Caso positivo, especificarla

1. **Definición de reducción**:
   1. Un lenguaje $L_1$ se reduce a otro lenguaje $L_2$ (denotado $L_1 \space \alpha \space L_2$) si existe una función computable $f: \Sigma^* \to \Sigma^*$ tal que para todo string $w$, se cumplen 2 cosas:
      1. Si $w \in L_1$, entonces $f(w) \in L_2$.
      2. Si $w \notin L_1$, entonces $f(w) \notin L_2$.

## 3. ¿Existe alguna codificación de Máquina de Turing que permita ver que $L(M) = \emptyset$? Justificar

---

<h1 align="center">Noviembre de 2015</h1>

## 1. Sea $A = \lbrace \lbrace x \rbrace \mid x \in N \rbrace$, un conjunto formado por conjuntos unitarios, o sea de un solo elemento.

### a. ¿$A$ es contable?

### b. ¿$\mathcal{P(\mathbb{N})} - A$ es contable?

## 2. Sea el modelo de MT $qA - qR$ ¿existe una selección tal que siempre loopee?

## 3. (algo sobre una reducción)

---

<h1 align="center">Agosto de 2016</h1>

## 1. $L_1$ $\alpha$ $L_u$, con $L_1 = \lbrace 0w \mid w \in \Sigma^* \rbrace$. Describir la función de transición de la MT $M_f$ que aplica la función de reducción.

## 2. $L_1 \space \alpha \space L_2$, con $L_1 = \lbrace \lambda \rbrace$ y $L_2 = \lbrace 0^n1^n \mid n < 0 \rbrace$. Explicar la función de reducción.

## 3. Marcar verdadero o falso, y justificar. Si $A$ y $B$ son conjuntos no contables.

### a. $A - B$ puede ser contable.

### b. $A - B$ puede ser no contable.

---

<h1 align="center">??? de 2016</h1>

## 1. Sean $\Sigma = \lbrace 0, 1 \rbrace$ y $\langle M \rangle = 101011$ el código de la máquina de Turing $M$ (utilizando alguna codificación establecida). Suponga que el par $(\langle M \rangle, w)$ se codifica utilizando el $00$ para separar el código de la máquina, del string de entrada $w$, así $1010110001$ representa el par $(\langle M \rangle, 01)$. Además asuma que $\langle M \rangle \in L(M)$.

### Construya una máquina de Turing (definiendo la función de transición) que compute una función de reducibilidad $L_1$ $\alpha$ $L_u$, siendo $L_1 = \lbrace 0w \mid w \in \Sigma^* \rbrace$ y $L_u$ el lenguaje Universal definido en la teoría.

## 2. Dada una MT del modelo $DIS$ encontrar, si es posible, la MT correspondiente en un modelo en el cual la posición inicial del cabezal es indeterminado. Si no fuera posible indicar la/las razones.

## 3. Si $A$ es un conjunto incontable y $B$ es un conjunto incontable, indicar en cada caso si la afirmación es verdadera o falsa, justificando la respuesta.

### a. $A - B$ puede ser contable.

### b. $A - B$ puede ser incontable.
