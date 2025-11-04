# Teoría de Conjuntos

## Definición

- **Notación**:
  - A = {...}
  - $x \in A$ (x pertenece al conjunto A)
  - $x \notin A$ (x no pertenece al conjunto A).
- **Conjunto**:
  - Colección de objetos bien definidos llamados elementos.
  - Se denotan comunmente con letras mayúsculas (A, B, C, etc) y se definen con llaves.
    - Ejemplo: A = {1, 2, 3} es un conjunto con tres elementos: 1, 2 y 3.
  - Un conjunto puede ser finito o infinito.
- **Elemento**:
  - Cada elemento es único e "indivisible".
  - No hay ningún orden entre los elementos, es decir que por ejemplo: A = {1, 2, 3} es equivalente a B = {3, 2, 1}, A = B.

## Formas de expresar conjuntos

1. **Por extensión**:
   - Listando todos los elementos del conjunto.
   - Ejemplo: A = {a, b, c, d}
2. **Por comprensión**:
   - Describiendo una propiedad que caracteriza a los elementos del conjunto.
     - Ejemplo: A = {x | x es un número par y 1 < x < 7} = {2, 4, 6}.
3. **Por diagramas de Venn**:
   - Representación gráfica de conjuntos y sus relaciones.

## Conjunto vacío

- **Notación**: $\emptyset$ o {}.
- **Definición intuitiva**:
  - El conjunto vacío es el conjunto sin elementos.
  - Es decir, ningun objeto puede jamás pertenecer al conjunto vacío.
- **Definición formal**:
  - $(\forall x)(x \notin \emptyset)$

## Operaciones

### Subconjunto estricto

- **Notación**: $A \subset B$.
- **Definición intuitiva**:
  - A es un subconjunto estricto de B si todos los elementos de A están en B, pero B no es igual a A: porque B tiene uno o más elementos que no están en A.
- **Definición formal**:
  - $(\forall x)(x \in A \rightarrow x \in B) \land (\exists x)(x \in B \land x \notin A)$
- **Nota 1**: Si A es subconjunto estricto de B, entonces A es subconjunto no estricto de B.
  - $A \subset B \implies A \subseteq B$
- **Nota 2**: Ningún conjunto es subconjunto estricto de sí mismo.
  - $\forall A (A \not\subset A)$
- **Ejemplo**:
  - Si A = {1, 2} y B = {1, 2, 3} entonces A ⊂ B.

### Subconjunto no estricto

- **Notación**: $A \subseteq B$.
- **Definición intuitiva**:
  - A es un subconjunto de B si todos los elementos de A están en B.
  - A puede ser igual a B.
- **Definición formal**:
  - $(\forall x)(x \in A \rightarrow x \in B)$
- **Nota 1**: El conjunto vacío es subconjunto de cualquier conjunto.
  - $(\forall A) (\emptyset \subseteq A)$
- **Nota 2**: Todo conjunto es subconjunto no estricto de sí mismo.
  - $(\forall A) (A \subseteq A)$
- **Nota 3**: La inclusión es transitiva:
  - Si $A \subseteq B$ y $B \subseteq C$ entonces $A \subseteq C$.
- **Ejemplo**:
  - Si A = {1, 2} y B = {1, 2, 3} entonces A ⊆ B.
  - Si A = {1, 2, 3} y B = {1, 2, 3} entonces A ⊆ B.

### Igualdad

- **Notación**: $A = B$.
- **Definición intuitiva**:
  - A es igual a B si ambos conjuntos tienen **exactamente** los mismos elementos.
- **Definición formal**:
  - $(\forall x)(x \in A \leftrightarrow x \in B)$
- **Equivalencia lógica con el subconjunto**:
  - $A = B \iff (A \subseteq B) \land (B \subseteq A)$
- **Ejemplo**:
  - Si A = {1, 2, 3} y B = {1, 2, 3} entonces A = B.
  - Si A = {1, 2, 3} y B = {3, 2, 1} entonces A = B.

### Intersección

- **Notación**: $A \cap B$.
- **Definición intuitiva**:
  - La intersección de A y B es el conjunto de elementos que pertenecen a **ambos** conjuntos.
- **Definición formal**:
  - $A \cap B = \lbrace x | x \in A \land x \in B \rbrace$
- **Ejemplo**:
  - Si A = {1, 2, 3} y B = {1, 2, 5} entonces $A \cap B$ = {1, 2}.

### Unión

- **Notación**: $A \cup B$.
- **Definición intuitiva**:
  - La unión de A y B es el conjunto de elementos que pertenecen a A, a B, o a ambos.
  - Es decir, todos los elementos de A y todos los elementos de B.
  - Si hay repetidos entre A y B, se cuentan solo una vez.
- **Definición formal**:
  - $A \cup B = \lbrace x | x \in A \lor x \in B \rbrace$
- **Ejemplo**:
  - Si A = {1, 2, 3} y B = {1, 2, 4} entonces $A \cup B$ = {1, 2, 3, 4}.
  - Si A = {1, 2, 3} y B = {4, 5, 6} entonces $A \cup B$ = {1, 2, 3, 4, 5, 6}.

### Diferencia

- **Notación**: $A - B$.
- **Definición intuitiva**:
  - La diferencia de A y B es el conjunto de elementos que pertenecen a A pero no pertenecen a B.
- **Definición formal**:
  - $A - B = \lbrace x | x \in A \land x \notin B \rbrace$
- **Nota 1**: Si $A \cap B = \emptyset$ entonces $A - B = A$.
- **Nota 2**: $A - B \neq B - A$ en general.
- **Ejemplo**:
  - Si A = {1, 2, 3} y B = {1, 2, 4} entonces $A - B$ = {3}.
  - Si A = {1, 2, 3} y B = {4, 5, 6} entonces $A - B$ = {1, 2, 3}.

### Complemento

- **Notación**: $\overline{A}$.
- **Definición intuitiva**:
  - El complemento de A es el conjunto de elementos que no pertenecen a A.
- **Definición formal**:
  - $\overline{A} = \lbrace x | x \notin A \rbrace$
- **Nota**: El complemento siempre se define respecto a un conjunto universal U, es decir, $\overline{A} = U - A$.
- **Ejemplo**:
  - Si el conjunto universal U = {1, 2, 3, 4, 5} y A = {1, 2, 3} entonces $\overline{A}$ = {4, 5}.

### Producto cartesiano

- **Notación**: $A \times B$.
- **Definición intuitiva**:
  - El producto cartesiano de A y B es el conjunto de todos los pares ordenados (x, y) donde x pertenece a A, y pertenece a B.
- **Definición formal**:
  - $A \times B = \lbrace (x, y) | x \in A \land y \in B \rbrace$
- **Ejemplo**:
  - Si A = {1, 2} y B = {3, 4} entonces $A \times B$ = {(1, 3), (1, 4), (2, 3), (2, 4)}.

### Conjunto potencia

- **Notación**: $\mathcal{P}(A)$.
- **Definición intuitiva**:
  - El conjunto potencia de A es el conjunto de todos los subconjuntos de A, incluyendo el conjunto vacío y A mismo.
- **Definición formal**:
  - $\mathcal{P}(A) = \lbrace B | B \subseteq A \rbrace$
- **Nota 1**: Si A tiene n elementos, entonces $\mathcal{P}(A)$ tiene $2^n$ elementos.
- **Nota 2**: $(\forall A) \emptyset \in \mathcal{P}(A)$ y $A \in \mathcal{P}(A)$.
- **Nota 3**: Si $A \subseteq B$ entonces $\mathcal{P}(A) \subseteq \mathcal{P}(B)$.
- **Ejemplo**:
  - Si A = {1, 2}, entonces $\mathcal{P}(A)$ = {$\emptyset$, {1}, {2}, {1, 2}}.

### Equivalencias de las operaciones

1. **Conmutatividad**:
   1. $A \cup B = B \cup A$
   2. $A \cap B = B \cap A$
2. **Asociatividad**:
   1. $A \cup (B \cup C) = (A \cup B) \cup C$
   2. $A \cap (B \cap C) = (A \cap B) \cap C$
3. **Distributividad**:
   1. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
   2. $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
4. **Leyes de Morgan**:
   1. $\overline{A \cup B} = \overline{A} \cap \overline{B}$
   2. $\overline{A \cap B} = \overline{A} \cup \overline{B}$
5. **Doble complemento**:
   1. $\overline{\overline{A}} = A$

---

# Máquinas de Turing (introducción)

## Concepto

- Modelo matemático de un dispositivo de computación.
- Consiste en una cinta infinita dividida en infinitas celdas, un cabezal que se mueve sobre la cinta y puede leer y escribir símbolos en estas celdas.
- En cada instante de tiempo, la máquina está en un estado determinado de un conjunto finito de estados.
- La máquina puede cambiar de estado, escribir un símbolo en la celda actual y mover el cabezal a la izquierda o a la derecha, dependiendo del símbolo que está leyendo y del estado en el que se encuentra.

## Configuración inicial

- Siempre inicia en el estado $q_0$.
- Si hay una cadena de entrada, esta se encuentra escrita en la cinta, comenzando desde la celda más a la izquierda. Además, esta cadena está delimitada por infinitos símbolos blancos (B) a la izquierda y a la derecha (principio y fin de la cadena en cuestión). No hay ningún blanco entre los símbolos de la cadena.
  - Si no, la cinta está vacía (solo contiene el símbolo blanco, que denotamos como "B").

## Comportamiento

- Está definido por una función de transición matemática que indica, según el estado actual y el símbolo que está leyendo el cabezal:
  - El nuevo estado en el que se encontrará.
  - El símbolo que escribirá en la celda actual (puede ser el mismo que estaba leyendo).
  - La dirección en la que moverá el cabezal (izquierda o derecha).
- Si la función de transición no está definida para el estado actual y el símbolo que está leyendo, la máquina se detiene.
- El resultado del cómputo es la cadena que queda escrita en la cinta cuando la máquina se detiene.

## MT General

- **Notación**: $M = \langle Q, Σ, Γ, δ, q_0 \rangle$
  - $Q$: Conjunto finito de estados.
  - $Σ$: Alfabeto de la entrada.
  - $Γ$: Alfabeto de la cinta $(Σ \subseteq Γ$, $B \in (Γ - Σ))$.
  - $δ$: Función de transición ($δ: Q \times Γ \rightarrow Q \times Γ \times \lbrace D, I \rbrace$).
  - $q_0$: Estado inicial ($q_0 \in Q$).
- Nota: $Q \cap Γ = \emptyset$

## MT Alternativa

- **Notación**: $M = \langle Q, Σ, Γ, δ, q_0, q_d \rangle$
  - $Q$: Conjunto finito de estados.
  - $Σ$: Alfabeto de la entrada.
  - $Γ$: Alfabeto de la cinta $(Σ \subseteq Γ$, $B \in (Γ - Σ))$.
  - $δ$: Función de transición ($δ: Q \times Γ \rightarrow Q \cup \lbrace q_d \rbrace \times Γ \times \lbrace D, I \rbrace$).
  - $q_0$: Estado inicial ($q_0 \in Q$).
  - $q_d$: Estado de detención ($q_d \notin Q$).
- La máquina deja de computar cuando llega a $q_d$ porque $q_d$ no es parte del dominio de $δ$.

## MT Reconocedora

- **Notación**: $M = \langle Q, Σ, Γ, δ, q_0, q_A, q_R \rangle$
  - $Q$: Conjunto finito de estados.
  - $Σ$: Alfabeto de la entrada.
  - $Γ$: Alfabeto de la cinta ($Σ \subseteq Γ$).
  - $δ$: Función de transición ($δ: Q \times Γ \rightarrow Q \cup \lbrace q_A, q_R \rbrace \times Γ \times \lbrace D, I \rbrace$).
  - $q_0$: Estado inicial ($q_0 \in Q$).
  - $q_A$: Estado de aceptación ($q_A \notin Q$).
  - $q_R$: Estado de rechazo ($q_R \notin Q$).
- **Estados de detención**:
  - $q_A$ (Aceptación): Si la máquina llega a este estado, se dice que acepta la cadena de entrada.
  - $q_R$ (Rechazo): Si la máquina llega a este estado, se dice que rechaza la cadena de entrada.
  - En ambos casos, la máquina se detiene. Si no llega nunca a ninguno de estos estados, entonces nunca se detendrá.
- **Lenguaje que acepta o reconoce**:
  - El lenguaje que acepta o reconoce una máquina de Turing reconocedora $M$ es el conjunto de todas las cadenas que $M$ **acepta**.
  - Formalmente: $L(M) = \lbrace w \in Σ^*  | M \text{ acepta } w \rbrace$
  - Dicho de otra forma:
    - $w \in L(M) \leftrightarrow$ con entrada $w$, $M$ termina en el estado $q_A$.
    - Para $v \notin L(M)$, se tiene que $M$ termina en el estado $q_R$ o $M$ loopea infinitamente.

---

# Lenguajes Formales

## Símbolo

- **Notación**: x, y, z, ...
- **Definición intuitiva**:
  - Un símbolo es un objeto indivisible.
- **Definición formal**:
  - $x$ es un símbolo si y solo si:
    - $x$ es un objeto indivisible.
  - Un símbolo es un objeto indivisible que pertenece a un conjunto **finito** llamado **alfabeto**.
- **Ejemplo**:
  - a, b, c, 1, 2, 3, @, #, $, %, &, ...

## Alfabeto

- **Notación**: $\Sigma$
- **Definición intuitiva**:
  - Un alfabeto es un conjunto **no vacío** y **finito** de símbolos.
- **Definición formal**:
  - $\Sigma$ es un alfabeto si y solo si:
    - $\Sigma \neq \emptyset$
    - $\Sigma$ es finito
    - $(\forall x)(x \in \Sigma \rightarrow \text{x es un símbolo indivisible})$
- **Ejemplo**:
  - $\Sigma = \lbrace a, b, c \rbrace$ es un alfabeto con tres símbolos: a, b y c.
  - $\Sigma = \lbrace aa, b, c \rbrace$ no es un alfabeto porque "aa" no es un símbolo indivisible.

## Cadena / palabra / sentencia / string

- **Notación**: $w$ o $\lambda$ (para la cadena vacía)
- **Definición intuitiva**:
  - Una cadena es una secuencia **finita** de símbolos tomados de un **alfabeto** $\Sigma$.
- **Definición formal**:
  - $w$ es una cadena si y solo si:
    - $w = x_1 x_2 ... x_n$, donde $n \geq 0$ y $x_i \in \Sigma$ para $1 \leq i \leq n$.
    - Si $n = 0$, entonces $w = \lambda$ (cadena vacía, sin ningún símbolo).
- **Ejemplo**:
  - Si $\Sigma = \lbrace a, b \rbrace$, entonces algunas cadenas posibles son:
    - $w_1 = abba$
    - $w_2 = aab$
    - $w_3 = b$
    - $w_4 = \lambda$ (cadena vacía)
- **Longitud de una cadena**:
  - Se denota como $|w|$ y es el número de símbolos en la cadena $w$.
  - Ejemplo: Si $w = abba$, entonces $|w| = 4$.
  - Para la cadena vacía $\lambda$, $|\lambda| = 0$.
- **Concatenación de cadenas**:
  - Si $w_1$ y $w_2$ son cadenas, la concatenación de $w_1$ y $w_2$ se denota como $w_1 w_2$ y es la cadena formada al unir $w_1$ seguido de $w_2$.
    - Ejemplo: Si $w_1 = ca$ y $w_2 = sa$, entonces $w_1 w_2 = casa$.
  - Esta operación es **asociativa** pero no conmutativa: $(w_1 w_2) w_3 = w_1 (w_2 w_3)$ pero $w_1 w_2 \neq w_2 w_1$ en general.
  - La cadena vacía $\lambda$ actúa como el elemento neutro en la concatenación: $w \lambda = \lambda w = w$ para cualquier cadena $w$.
  - La concatenación de cadenas puede aumentar la longitud: $|w_1 w_2| = |w_1| + |w_2|$.
    - Ejemplo: Si $w_1 = ab$ y $w_2 = ba$, entonces $w_1 w_2 = abba$ y $|w_1 w_2| = 4$.
- **Potencia i-ésima de una cadena**:
  - La potencia i-ésima de una cadena $w$, denotada como $w^i$, es la concatenación de $i$ copias de $w$.
    - Si $i = 0$, entonces $w^0 = \lambda$ (cadena vacía).
    - Si $i > 0$, entonces $w^{(i + 1)} = ww^i (\forall i \geq 0)$.
    - Ejemplo: Si $w = ab$ y $i = 3$, entonces $w^3 = ababab$.
  - Por convención, $w^0 = \lambda$ para cualquier cadena $w$.
- **Inverso de una cadena**:
  - El inverso de una cadena $w = x_1 x_2 ... x_n$ se denota como $w^R$ y es la cadena formada al escribir los símbolos de $w$ en orden inverso: $w^R = x_n x_{n-1} ... x_1$.
    - Ejemplo: Si $w = auto$, entonces $w^R = otua$.

## Sigma estrella

- **Notación**: $\Sigma^*$
- **Definición intuitiva**:
  - $\Sigma^*$ es el conjunto de todas las cadenas (incluyendo la cadena vacía) que se pueden formar con los símbolos del alfabeto $\Sigma$.
  - Es un conjunto infinito.
- **Definición formal**:
  - $\Sigma^* = \lbrace w | \text{w es una cadena (incluyendo la cadena vacía) formada por símbolos de } \Sigma \rbrace$
- **Ejemplo**:
  - Si $\Sigma = \lbrace a, b \rbrace$, entonces:
    - $\Sigma^* = \lbrace \lambda, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb, ... \rbrace$

## Lenguaje

- **Notación**: $L$
- **Definición intuitiva**:
  - Un lenguaje es un **conjunto** de una o más cadenas formadas a partir de un alfabeto $\Sigma$.
- **Definición formal**:
  - $L$ es un lenguaje si y solo si:
    - $L \subseteq \Sigma^*$
- **Ejemplo**:
  - Si $\Sigma = \lbrace 0, 1 \rbrace$, entonces:
    - $\Sigma^* = \lbrace \lambda, 0, 1, 00, 01, 10, 11, 000, 001, 010, 011, 100, 101, 110, 111, ... \rbrace$
  - Posibles lenguajes definidos sobre $\Sigma$ podrían ser:
    - $L_1 = \lbrace 0, 1, 00, 01 \rbrace$
    - $L_2 = \emptyset$
    - $L_3 = \lbrace \lambda \rbrace$
    - $L_4 = \Sigma^*$
    - $L_5 = \lbrace w | \text{w es una cadena que empieza con 1} \rbrace$
- **Nota**: Si $L$ es un lenguaje sobre el alfabeto $\Sigma$, su complemento también es un lenguaje sobre el mismo alfabeto, definido como $\overline{L} = \Sigma^* - L$.
- **L cursiva ($\mathscr{L}$)**:
  - $\mathscr{L}$ es el conjunto de todos los lenguajes posibles sobre un alfabeto $\Sigma$.
  - Es decir, $\mathscr{L} = \mathcal{P}(\Sigma^*)$.

---

# Máquinas de Turing (continuación)

## Definición de equivalencia de MT

- **Definición intuitiva**:
  - Una máquina de Turing $M_1$ es equivalente a una máquina de Turing $M_2$ si y solo si ambas máquinas reconocen el mismo lenguaje.
- **Definción formal**:
  - $M_1 \equiv M_2 \leftrightarrow L(M_1) = L(M_2)$

## Definición de equivalencia de modelo de MT

- **Definición intuitiva**:
  - Dos modelos de máquinas de Turing son equivalentes si y solo si para cada máquina de un modelo, existe una máquina en el otro modelo que reconoce el mismo lenguaje.
  - Esto implica que ambos modelos tienen la misma capacidad de reconocimiento de lenguajes.
- **Definición formal**:
  - Dos modelos de máquinas de Turing $A$ y $B$ son equivalentes si y solo si:
    - $(\forall M_A \in A)(\exists M_B \in B)(M_A \equiv M_B)$ y
    - $(\forall M_B \in B)(\exists M_A \in A)(M_B \equiv M_A)$

## Modelo D-I-S

- Es una máquina de Turing que admite transiciones sin mover el cabezal.
- **Notación**: $M = \langle Q, Σ, Γ, δ, q_0, q_A, q_R \rangle$
  - $Q$: Conjunto finito de estados.
  - $Σ$: Alfabeto de la entrada.
  - $Γ$: Alfabeto de la cinta ($Σ \subseteq Γ$).
  - $δ$: Función de transición ($δ: Q \times Γ \rightarrow Q \cup \lbrace q_A, q_R \rbrace \times Γ \times \lbrace D, I, S \rbrace$).
  - $q_0$: Estado inicial ($q_0 \in Q$).
  - $q_A$: Estado de aceptación ($q_A \notin Q$).
  - $q_R$: Estado de rechazo ($q_R \notin Q$).

## Modelo k-cintas

- Es una máquina de Turing que tiene $k$ cintas y $k$ cabezales que pueden moverse de forma independiente.
- El input se encuentra en la primer cinta y las demás cintas están inicialmente vacías.
- **Notación**: $M = \langle Q, Σ, Γ, δ, q_0, q_A, q_R \rangle$
  - $Q$: Conjunto finito de estados.
  - $Σ$: Alfabeto de la entrada.
  - $Γ$: Alfabeto de la cinta ($Σ \subseteq Γ$).
  - $δ$: Función de transición ($δ: Q \times Γ^k \rightarrow Q \cup \lbrace q_A, q_R \rbrace \times (Γ \times \lbrace D, I, S \rbrace)^k$).
  - $q_0$: Estado inicial ($q_0 \in Q$).
  - $q_A$: Estado de aceptación ($q_A \notin Q$).
  - $q_R$: Estado de rechazo ($q_R \notin Q$).

---

# Clasificación de lenguajes

## Lenguajes recursivamente enumerables (RE)

- Un lenguaje es recursivamente enumerable ($L \in RE$) si existe una máquina de Turing reconocedora que acepta todas las cadenas del lenguaje, pero **puede no detenerse para las cadenas que no pertenecen al lenguaje**.
- Formalmente:
  - $L \in RE \leftrightarrow \exists M \text{ tal que } L(M) = L$.
  - Si $w \in L$ entonces:
    - $M$ **siempre se detiene** en el estado de aceptación $q_A$.
  - Si $w \notin L$ entonces:
    - $M$ se detiene en el estado de rechazo $q_R$ o **no se detiene y loopea infinitamente**. No es posible saber cuál de los dos casos ocurrirá de antemano (Halting Problem).

## Lenguajes recursivos o decidibles (R)

- Un lenguaje es recursivo o decidible ($L \in R$) si existe una máquina de Turing reconocedora que acepta todas las cadenas del lenguaje y **se detiene para todas las cadenas, ya sea aceptándolas o rechazándolas**.
- Formalmente:
  - $L \in R \leftrightarrow \exists M \text{ tal que } L(M) = L$ y $M \text{ se detiene para todas las cadenas}$.
  - Si $w \in L$ entonces:
    - $M$ **siempre se detiene** en el estado de aceptación $q_A$.
  - Si $w \notin L$ entonces:
    - $M$ **siempre se detiene** en el estado de rechazo $q_R$.
- Todo lenguaje decisible es recursivamente enumerable, pero no todo lenguaje recursivamente enumerable es decidible.
  - $R \subseteq RE$
- **Nota**: La intersección y la unión de dos lenguajes recursivos da como resultado otro lenguaje recursivo.
  - Si $L_1, L_2 \in R$ entonces $L_1 \cap L_2 \in R$ y $L_1 \cup L_2 \in R$.

## Lenguajes Co-R

- Un lenguaje es Co-R ($L \in \text{Co-R}$) si y solo si su complemento respecto de $\Sigma^*$ es decidible.
- Formalmente:
  - $L \in \text{Co-R} \leftrightarrow \overline{L} \in R$
  - $\overline{L} = \Sigma^* - L$

## Lenguajes Co-RE

- Un lenguaje es Co-RE ($L \in \text{Co-RE}$) si y solo si su complemento respecto de $\Sigma^*$ es recursivamente enumerable.
- Formalmente:
  - $L \in \text{Co-RE} \leftrightarrow \overline{L} \in RE$
  - $\overline{L} = \Sigma^* - L$

## Teoremas

- **Todo lenguaje decidible es recursivamente enumerable**.
  - $R \subseteq RE$
- **Todo lenguaje decidible es Co-R**:
  - $R \subseteq \text{Co-R}$
- **Todo lenguaje Co-R es decidible**:
  - $\text{Co-R} \subseteq R$
- **Por lo tanto, todo lenguaje decidible es Co-R y viceversa, y además todo lenguaje Co-R es recursivamente enumerable**:
  - $R = \text{Co-R}$
  - $\text{Co-R} \subseteq RE$
- **Todo lenguaje recursivo es Co-RE**:
  - $R \subseteq \text{Co-RE}$
- Por lo tanto, todo lenguaje decidible es Co-RE y viceversa, y además todo lenguaje Co-RE es recursivamente enumerable:
  - $R = \text{Co-RE}$
  - $R \subseteq (RE \cap \text{Co-RE})$
- **Los lenguajes que son tanto RE como Co-RE son decidibles**:
  - $(RE \cap \text{Co-RE}) \subseteq R$
- **Los lenguajes que son tanto RE como Co-RE son exactamente los mismos que los decidibles**:
  - $(RE \cap \text{Co-RE}) = R$

## Orden canónico para $\Sigma^*$

- Sea $\Sigma$ un alfabeto finito.
- El orden canónico para $\Sigma^*$ es una forma de listar todas las cadenas posibles formadas con los símbolos de $\Sigma$ en orden lexicográfico.
- Ejemplo:
  - Si $\Sigma = \lbrace 0, 1 \rbrace$, entonces el orden canónico para $\Sigma^*$ es:
    - $\lambda, 0, 1, 00, 01, 10, 11, 000, 001, 010, 011, 100, 101, 110, 111, ...$
    - Si $w$ es un string de $\lbrace 0,1 \rbrace^*$, la posición $i$ que ocupa en el orden canónico se escribe en binario como $1w$. Decimos entonces que $w$ es el $i$-ésimo string y por ello lo denotamos $w_i$.
    - Por ejemplo el string $\lambda$ ocupa la posición 1 ($1\lambda$) el string 01 ocupa la posición 5 ($101$), el string 100 la posición 12 ($1100$), etc.

## Codificación binaria de una MT

- Es una forma de representar una máquina de Turing como una cadena binaria para que la misma pueda ser usada como entrada de otra máquina de Turing.
- Ejemplo:
  - Sea $M = \langle Q, Σ, Γ, δ, q_0, q_A, q_R \rangle$ una máquina de Turing reconocedora D-I-S tal que:
  - $Q = \lbrace q_0 \rbrace$
  - $\Sigma = \lbrace a, b \rbrace$
  - $\Gamma = \lbrace B, a, b \rbrace$
  - $\delta(q_0, a) = (q_A, a, D)$
  - $\delta(q_0, b) = (q_R, b, S)$
  - $\delta(q_0, B) = (q_R, B, S)$
  - Donde se codifican los símbolos de la siguiente manera:
    - $q_0 = 111$
    - $q_R = 11$
    - $q_A = 1$
    - $b = 111$
    - $a = 11$
    - $B = 1$
    - $S = 111$
    - $I = 11$
    - $D = 1$
  - Entonces la codificación binaria de $M$ es (usamos dos ceros para separar las funciones de transición):
    - $111_{q_0} 0 11_{a} 0 1_{q_a} 0 11_{a} 0 1_{D} 00_{sig} 111_{q_0} 0 111_{b} 0 11_{q_R} 0 111_{b} 0 111_{S} 00_{sig} 111_{q_0} 0 1_{B} 0 11_{q_R} 0 1_{B} 0 111_{S}$
- Hay N! formas de codificar una MT, si tenemos N funciones de transición. En este caso 3! = 6.
- Se denomina i-ésima máquina de Turing y se denota $M_i$ a la MT cuyo código binario es el i-ésimo string en el orden canónico de $\lbrace 0,1 \rbrace^*$, es decir $\langle M_i \rangle = w_i$.
  - Si se da el caso que $w_i$ no es un código válido de una MT, entonces $M_i$ es una MT ficticia que rechaza todo, es decir $L(M_i) = \emptyset$.
  - Por lo tanto $\forall w_i \in \lbrace 0,1 \rbrace^* \exists M_i$.

## Lenguaje diagonal ($L_D$)

- **Definición intuitiva**: El lenguaje diagonal $L_D$ es el conjunto de todas las cadenas que no son aceptadas por su **correspondiente** máquina de Turing. Consiste en las codificaciones de MT que rechazan su propia codificación.
- **Definición formal**:
  - $\Sigma = \lbrace 0,1 \rbrace$
  - $w_i = \text{i-ésimo string en orden canónico de } \Sigma^*$
  - $M_i = \text{i-ésima máquina de Turing}$
  - $L_D = \lbrace  w_i \in \Sigma^* \mid w_i \notin L(M_i)  \rbrace$
- Este lenguaje no es recursivamente enumerable, por lo tanto no es decidible tampoco y no existe una máquina de Turing que lo reconozca.
- **Teoremas**:
  - $L_D \notin RE$
  - $L_D \notin R$
  - $L_D \in \text{Co-RE}$
  - $\overline{L_D} \in RE$
  - $\overline{L_D} \in (RE-R)$

## Máquina de Turing Universal

- Es una máquina de Turing que recibe como entrada la codificación binaria de otra máquina de Turing junto con una cadena de entrada para esa máquina, y simula el comportamiento de esa máquina con esa cadena de entrada, ejecutándola.

## Lenguaje Universal $L_u$

- **Definición intuitiva**: El lenguaje universal $L_u$ es el conjunto de todos los pares (máquina, cadena) tales que la máquina acepta esa cadena.
- **Definición formal**:
  - $L_u = \lbrace  (\langle M \rangle,w) \mid w \in L(M)  \rbrace$
  - $L_u = L(M_u)$
- **Teoremas**:
  - $L_u \in RE$
  - $L_u \notin R$
  - Por lo tanto: $L_u \in (RE - R)$
  - $\overline{L_u} \notin RE$

## Lenguaje L

- **Definición formal**:
  - $L = \lbrace 1w \mid w \in L_D \rbrace \cup \lbrace 0w \mid w \notin L_D \rbrace$
- **Teorema**: $L \in (\mathscr{L} - (RE \cup \text{Co-RE}))$

## Diagrama de Venn de los lenguajes vistos

![Diagrama de Venn](https://i.imgur.com/ltqDKfF.png)

---

# Reducibilidad

## Definición de reducción

- Sean $L_1$ y $L_2$ dos lenguajes sobre un alfabeto $\Sigma$.
- $L1$ se reduce a $L2$ (denotado $L_1$ $\alpha$ $L_2$) si existe una **función total computable** $f: \Sigma^* \rightarrow \Sigma^*$ tal que: $$(\forall w \in \Sigma^*)(w \in L_1 \leftrightarrow f(w) \in L_2)$$
- Equivalentemente: $$(\forall w \in \Sigma^*)((w \in L_1 \rightarrow f(w) \in L_2) \land (f(w) \in L_2 \rightarrow w \in L_1))$$
- O, por contrarecíproco $(A \rightarrow B \Leftrightarrow \lnot B \rightarrow \lnot A)$ de lo anterior: $$(\forall w \in \Sigma^*)((w \in L_1 \rightarrow f(w) \in L_2) \land (w \notin L_1 \rightarrow f(w) \notin L_2)$$
- Intuitivamente, una reducibilidad es una función que transforma instancias de un problema/lenguaje en otro.
  - A cada palabra de $L_1$ se le asigna una palabra de $L_2$.
  - A cada palabra que NO pertenece a $L_1$ se le asigna una palabra que NO pertenece a $L_2$.

## Función total computable

- Una función $f$ es **computable** si existe una máquina de Turing que la computa y que siempre se detiene.
- Una función $f$ es **total** si está definida para todos los elementos de su dominio, es decir, se debe poder aplicar a cualquier cadena de $\Sigma^*$.

![](https://i.imgur.com/Lw0eePJ.png)

- $M_f$ nunca loopea. La expresión $M_f(w)$ se refiere a la función computada por la máquina de Turing $M_f$.

## Ejemplo 1

- Sea $L_1 = \lbrace w \in \lbrace a, b \rbrace^* \mid \text{w comienza con a} \rbrace$
- Sea $L_2 = \lbrace w \in \lbrace a, b \rbrace^* \mid \text{w comienza con b} \rbrace$

Se demostrará que existe una reducción: $L_1$ $\alpha$ $L_2$.

Para esto, queremos encontrar una función total computable $f: \lbrace a, b \rbrace^* \rightarrow \lbrace a, b \rbrace^*$ tal que: $$(\forall w \in \lbrace a, b \rbrace^*)(w \in L_1 \leftrightarrow f(w) \in L_2)$$

Para lo anterior, necesitamos encontrar una MT $M_f$ que compute la función $f$ mencionada y que siempre se detenga.

$M_f$ es una MT de cómputo y se define de la siguiente manera:

$M_f = \langle Q, Σ, Γ, δ, q_0, q_d\rangle$ donde:

- $Q = \lbrace q_0 \rbrace$
- $\Sigma = \lbrace a, b \rbrace$
- $\Gamma = \lbrace a, b, B \rbrace$

Y su función de transición $δ$ es:

- $δ(q_0, a) = (q_d, b, S)$
- $δ(q_0, b) = (q_d, a, S)$
- $δ(q_0, B) = (q_d, B, S)$

Es decir, $M_f$ lee **únicamente el primer símbolo de la cadena de entrada** y lo reemplaza por el símbolo "opuesto" (a por b, b por a). Si la cadena está vacía, no hace nada.

Podemos ver que:

1. $M_f$ **siempre se detiene**, ya que en cualquier caso llega al estado de detención $q_d$ después de leer el primer símbolo.
2. $f$ es **total**, ya que está definida para todas las cadenas en $\lbrace a, b \rbrace^*$.
3. La función $f$ cumple con la **condición de reducción**:

   - $(\forall w \in \Sigma^*)(w \in L_1 \rightarrow f(w) \in L_2)$ se cumple porque si $w$ comienza con "a", entonces $f(w)$ comenzará con "b", por lo cual se cumple que $f(w) \in L_2$, ya que cumple la condición de $L_2$.
   - $(\forall w \in \Sigma^*)(w \notin L_1 \rightarrow f(w) \notin L_2)$ se cumple porque si $w$ no comienza con "a" (es decir, comienza con "b" o es la cadena vacía), entonces $f(w)$ no comenzará con "b" (comenzará con "a" o será vacío).

## Ejemplo 2

- Sea $L_1 = \lbrace w \in \lbrace 0, 1 \rbrace^* \mid \text{Cantidad de unos de w es par} \rbrace$
- Sea $L_2 = \lbrace w \in \lbrace 0, 1 \rbrace^* \mid \text{Cantidad de unos de w es impar} \rbrace$

Se demostrará que existe una reducción: $L_1$ $\alpha$ $L_2$.

Para esto, queremos encontrar una función total computable $f: \lbrace 0, 1 \rbrace^* \rightarrow \lbrace 0, 1 \rbrace^*$ tal que: $$(\forall w \in \lbrace 0, 1 \rbrace^*)(w \in L_1 \leftrightarrow f(w) \in L_2)$$

Para lo anterior, necesitamos encontrar una MT $M_f$ que compute la función $f$ mencionada y que siempre se detenga.

$M_f$ es una MT de cómputo y se define de la siguiente manera:

$M_f = \langle Q, Σ, Γ, δ, q_0, q_d\rangle$ donde:

- $Q = \lbrace q_0, q_1 \rbrace$
- $\Sigma = \lbrace 0, 1 \rbrace$
- $\Gamma = \lbrace 0, 1, B \rbrace$

Y su función de transición $δ$ es:

- $δ(q_0, 0) = (q_1, 0, I)$
- $δ(q_0, 1) = (q_1, 1, I)$
- $δ(q_0, B) = (q_1, B, I)$
- $δ(q_1, B) = (q_d, 1, S)$

Es decir, $M_f$ se mueve una posición a la izquierda al comenzar, y como está al inicio de la cadena, siempre llega a un símbolo blanco. En ese momento escribe un 1 en ese lugar y se detiene.

Podemos ver que:

1. $M_f$ **siempre se detiene**, ya que en cualquier caso llega al estado de detención $q_d$ después de leer el primer símbolo y moverse a la izquierda, dado que siempre hay blanco a la izquierda del inicio de la cadena.
2. $f$ es **total**, ya que está definida para todas las cadenas en $\lbrace 0, 1 \rbrace^*$.
3. La función $f$ cumple con la **condición de reducción**:

   - $(\forall w \in \Sigma^*)(w \in L_1 \rightarrow f(w) \in L_2)$ se cumple porque si $w$ tiene una cantidad par de unos, al agregarle un 1 al inicio, la cantidad de unos en $f(w)$ siempre será impar, por lo cual se cumple que $f(w) \in L_2$, ya que cumple la condición de $L_2$ que es tener una cantidad impar de unos.
   - $(\forall w \in \Sigma^*)(w \notin L_1 \rightarrow f(w) \notin L_2)$ se cumple porque si $w$ tiene una cantidad impar de unos, al agregarle un 1 al inicio, la cantidad de unos en $f(w)$ siempre será par, por lo cual se cumple que $f(w) \notin L_2$, ya que no cumple la condición de $L_2$.
   - **En ambos casos se aprovecha la propiedad matemática**: $$\text{par} + 1 = \text{impar}$$ $$\text{impar} + 1 = \text{par}$$

## Implicaciones de la reducción

Sean $L_1$ y $L_2$ dos lenguajes. $L_1$ $\alpha$ $L_2$ implica que:

1. Se puede construir una MT que acpete $L_1$ a partir de la MT que acepta $L_2$ (si existe).
2. Intuitivamente, $L_1$ no puede ser más difícil computacionalmente que $L_2$, porque se puede usar $L_2$ para resolver $L_1$.
3. Intuitivamente, la reducción establece una relación de $\leq$ grado de dificultad computacional entre los lenguajes. Si $L_1$ $\alpha$ $L_2$, entonces $L_1$ no es más dificil que $L_2$, es o igual de difícil o más fácil. Si puedo computar $L_2$, entonces puedo computar $L_1$.

## Teoremas fundamentales

### Decibilidad

- Sean $L_1$ y $L_2$ dos lenguajes tal que $L_1$ $\alpha$ $L_2$. Entonces:
  - $L_2 \in R \rightarrow L_1 \in R$
  - $L_1 \notin R \rightarrow L_2 \notin R$ (por contrarrecíproco)
  - Es decir, si $L_2$ es decidible, entonces $L_1$ es decidible.
- Este teorema nos sirve para poder determinar si un lenguaje es decidible o no, partiendo de saber que otro lenguaje al que se reduce es decidible o no.

## Recursivamente enumerable

- Sean $L_1$ y $L_2$ dos lenguajes tal que $L_1$ $\alpha$ $L_2$. Entonces:
  - $L_2 \in RE \rightarrow L_1 \in RE$
  - $L_1 \notin RE \rightarrow L_2 \notin RE$ (por contrarrecíproco)
  - Es decir, si $L_2$ es recursivamente enumerable, entonces $L_1$ es recursivamente enumerable.
- Este teorema nos sirve para poder determinar si un lenguaje es recursivamente enumerable o no, partiendo de saber que otro lenguaje al que se reduce es recursivamente enumerable o no.

# Halting Problem (HP)

## Definición

- El lenguaje Halting Problem se define como: $$HP = \lbrace (\langle M \rangle, w) \mid \text{M es una MT que se detiene con input w} \rbrace$$
- Intuitivamente, este lenguaje contiene las codificaciones de todas las máquinas de Turing que se detienen al recibir una cadena de entrada específica.
- Este lenguaje es **recursivamente enumerable pero no decidible**, es decir: $$ HP \in (RE - R) \Leftrightarrow (HP \in RE) \land (HP \notin R)$$

# Lenguaje $L_{\Sigma^*}$

## Definición

- El lenguaje $L_{\Sigma^*}$ se define como: $$L_{\Sigma^*} = \lbrace \langle M \rangle \mid \text{M es una MT y } L(M) = \Sigma^*  \rbrace$$
- Intuitivamente, este lenguaje contiene las codificaciones de todas las máquinas de Turing que aceptan todas las cadenas posibles sobre el alfabeto $\Sigma$.
- Este lenguaje no es decidible ni recursivamente enumerable:
  - $L_{\Sigma^*} \notin R$
  - $L_{\Sigma^*} \notin RE$

# Lenguaje $L_{EQ}$

## Definición

- El lenguaje $L_{EQ}$ se define como: $$L_{EQ} = \lbrace (\langle M_1 \rangle, \langle M_2 \rangle) \mid L(M_1) = L(M_2)  \rbrace$$
- Intuitivamente, este lenguaje contiene los pares de codificaciones de máquinas de Turing que reconocen el mismo lenguaje.
- Este lenguaje no es recursivamente enumerable:
  - $L_{EQ} \notin RE$

---

# Notación Asintótica

## Contexto

- La notación asintótica está asociada al crecimiento de las funciones matemáticas.
- En el contexto de la computación, asociamos estas funciones a la cantidad de operaciones o tareas que el algoritmo debe realizar en función del tamaño de la entrada.
- Normalmente, a mayor entrada, mayor cantidad de operaciones (monotonía).
- La notación asintótica nos permite describir el comportamiento de estas funciones cuando la entrada crece arbitrariamente, es decir, tiende a infinito.

## Primera definición de Orden O

- Sea $t(n)$ una función.
- Decimos que $t(n)$ está en el orden de $f(n)$ si:
  - $\exists c \in \mathbb{R}, c > 0$
  - $\exists u_0 \in \mathbb{N}, u_0 > 0$
  - Tal que $t(n) \leq c \cdot f(n) \quad \forall n > u_0$
- Notaciones útiles:

## Notaciones útiles

- **Conjuntos**:
  - $\mathbb{N}$ es el conjunto de todos los números naturales, **incluyendo el cero**.
  - $\mathbb{R}^{\geq 0}$ es el conjunto de todos los números reales positivos, **incluyendo el cero**.
  - $\mathbb{R}^+$ es el conjunto de todos los números reales positivos, **excluyendo el cero**.
- **Cuantificadores**:
  - $\exists$: Existe al menos un elemento que satisface la propiedad.
  - $\exists^\infty$: Existen **infinitos** elementos que satisfacen la propiedad.
  - $\forall$: Todos los elementos satisfacen la propiedad, sin excepción.
  - $\forall^\infty$: Todos los elementos excepto un número **finito** de ellos satisfacen la propiedad.

## Segunda definición de Orden O

- $O(f(n)) = \lbrace t: \mathbb{N} \rightarrow \mathbb{R}^{\geq 0} \mid (\exists c \in \mathbb{R}^+)(\forall^\infty n \in \mathbb{N}) \space [t(n) \leq c \cdot f(n)] \rbrace$
  - Es decir, es un conjunto de funciones de los naturales a los reales mayores o iguales a cero, tales que existe una constante real positiva y hay infinitos naturales para los cuales se cumple que la función $t(n)$ es acotada superiormente por $c \cdot f(n)$.
- $O(f(n)) = \lbrace t: \mathbb{N} \rightarrow \mathbb{R}^+ \mid \exists c \in \mathbb{R}^+, \space n_0 \in \mathbb{N} \mid t(n) \leq c \cdot f(n), n \geq n_0 \rbrace$
  - Esta es una definición alternativa, donde en vez de ir de los naturales a los reales mayores o iguales a cero, va de los naturales a los reales estrictamente mayores que cero, y además se reemplaza el cuantificador $\forall^\infty$ por el umbral, es decir, existe un $n_0$ a partir del cual se cumple la condición.
  - Es una cota **superior**.

## Definición de Orden Omega $(\Omega)$

- La definición es muy similar a la de Orden O, pero en este caso se trata de una cota **inferior**:
- $\Omega(f(n)) = \lbrace t: \mathbb{N} \rightarrow \mathbb{R}^+ \mid \exists c \in \mathbb{R}^+, \space n_0 \in \mathbb{N} \mid t(n) \geq c \cdot f(n), n \geq n_0 \rbrace$

## Definición de Orden Theta $(\Theta)$

- La definición de Orden Theta combina las definiciones de Orden O y Orden Omega:
- $\Theta(f(n)) = \lbrace t: \mathbb{N} \rightarrow \mathbb{R}^+ \mid \exists c_1, c_2 \in \mathbb{R}^+, \space n_0 \in \mathbb{N} \mid c_1 \cdot f(n) \leq t(n) \leq c_2 \cdot f(n), n \geq n_0 \rbrace$
  - Es decir, es el conjunto de funciones que están acotadas **tanto superior como inferiormente** por $f(n)$.
  - En este sentido, $t(n)$ crece de manera "similar" a $f(n)$.

## Propiedades

- **$g(n) \in \Omega(f(n)) \leftrightarrow f(n) \in O(g(n))$** (Regla de dualidad)
- **$g(n) \in \Theta(f(n)) \leftrightarrow [g(n) \in O(f(n)) \land g(n) \in \Omega(f(n))]$**
- **$\Theta(f(n)) = O(f(n)) \cap \Omega(f(n))$**
- **$f(n) \in O(f(n))$** (Reflexividad)
- **[$f(n) \in O(g(n)) \land g(n) \in O(h(n))] \rightarrow f(n) \in O(h(n))$** (Transitividad)

---

# Complejidad Temporal

---

# Análisis de Algoritmos
