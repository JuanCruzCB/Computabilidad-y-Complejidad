<h1 align="center">Práctica 5</h1>

## 1. Sean $L_1$, $L_2$, $L_3$, $L_4$ cuatro lenguajes definidos sobre $\lbrace 0,1 \rbrace^*$

### $L_1 = \lbrace 0^n 1 \mid n \ge 0 \rbrace$

### $L_2 = \lbrace 1^n 0 \mid n \ge 0 \rbrace$

### $L_3 = \lbrace \lambda \rbrace$

### $L_4 = \lbrace 1^n 0 \mid n > 0 \rbrace$

### a. Demuestre que existe una reducción $(L_1$ $\alpha$ $L_2)$

1. **Análisis de los lenguajes**:
   1. Las primeras cadenas de $L_1$ son: $1, 01, 001, 0001, 00001, \dots$
   2. Las primeras cadenas de $L_2$ son: $0, 10, 110, 1110, 11110, \dots$
   3. $\lambda$ no pertenece a ninguno de los dos lenguajes porque por más que $n = 0$, siempre se tiene o un $1$ o un $0$ en la cadena.
   4. Se puede ver claramente que $L_2$ simplemente invierte todos los bits de $L_1$.
2. **Definición de la reducción**:
   1. $L_1 \space \alpha \space L_2$ si existe una función total computable $f: \Sigma^* \rightarrow \Sigma^*$ tal que a cada palabra $w \in L_1$ le corresponde una palabra $f(w) \in L_2$, y a cada palabra $z \notin L_1$ le corresponde una palabra $f(z) \notin L_2$.
3. **Construcción de la $M_f$**:
   1. Podemos definir una MT $M_f$ de cómputo que compute la función $f$ y que siempre se detenga:
   2. $M_f = \langle Q, \Sigma, \Gamma, \delta, q_0, q_d \rangle$ donde:
      - $Q = \lbrace q_0 \rbrace$
      - $\Sigma = \lbrace 0, 1 \rbrace$
      - $\Gamma = \lbrace 0, 1, B \rbrace$
      - $\delta(q_0, 0) = (q_0, 1, D)$
      - $\delta(q_0, 1) = (q_0, 0, D)$
      - $\delta(q_0, B) = (q_d, B, S)$
   3. La MT $M_f$ lee la cadena de entrada y va reemplazando cada $0$ por un $1$ y cada $1$ por un $0$. Cuando llega al símbolo de blanco, se detiene.
4. **Verificación de las condiciones de la reducción**:
   1. $M_f$ es total?
      1. Sí, porque está definida para todos los elementos de $\Sigma^*$. ✅
   2. $M_f$ es computable?
      1. Sí, porque siempre se detiene, debido a que el alfabeto es finito, la cadena de entrada es finita, y no hay bucles infinitos en ninguna transición. ✅
   3. Para cada palabra $w \in L_1$, $f(w) \in L_2$?
      1. Si la cadena de entrada es de la forma $0^n 1$, que pertenece a $L_1$, al aplicar $f(0^n 1)$ se obtiene $1^n 0$, que pertenece a $L_2$. ✅
         1. Por ejemplo, si $w = 001 \in L_1$, al aplicar $f(001)$ se obtiene $110 \in L_2$.
   4. Para cada palabra $z \notin L_1$, $f(z) \notin L_2$?
      1. Si la cadena de entrada es $\lambda$, que no pertenece a $L_1$, al aplicar $f(\lambda)$ se obtiene $\lambda$, que no pertenece a $L_2$. ✅
      2. Si la cadena de entrada no es de la forma $0^n 1$, que no pertenece a $L_1$, al aplicar $f$ a esa cadena, se obtiene una cadena que no es de la forma $1^n 0$, por lo que $f(z) \notin L_2$. ✅
         1. Por ejemplo, si $z = 101 \notin L_1$, al aplicar $f(101)$ se obtiene $010 \notin L_2$.

**Por lo tanto, $L_1 \space \alpha \space L_2$**.

### b. Demuestre que existe una reducción $(L_1$ $\alpha$ $L_3)$

1. **Análisis de los lenguajes**:
   1. Las primeras cadenas de $L_1$ son: $1, 01, 001, 0001, 00001, \dots$
   2. La única cadena de $L_3$ es $\lambda$, la cadena vacía.
   3. $\lambda$ no pertenece a $L_1$ porque por más que $n = 0$, siempre se tiene un $1$ en la cadena.
   4. Se puede ver claramente que $L_3$ simplemente convierte cualquier cadena de $L_1$ en la cadena vacía.
2. **Definición de la reducción**:
   1. $L_1 \space \alpha \space L_3$ si existe una función total computable $f: \Sigma^* \rightarrow \Sigma^*$ tal que a cada palabra $w \in L_1$ le corresponde una palabra $f(w) \in L_3$, y a cada palabra $z \notin L_1$ le corresponde una palabra $f(z) \notin L_3$.
   2. Es decir, para cada cadena válida de $L_1$ (de la forma $0^n 1$), lo que la función debe hacer es dejar la cadena vacía en la cinta, y para cada cadena inválida de $L_1$ (de cualquier otra forma), debe dejar algo en la cinta que NO sea la cadena vacía.
3. **Construcción de la $M_f$**:
   1. Podemos definir una MT $M_f$ de cómputo que compute la función $f$ y que siempre se detenga:
   2. $M_f = \langle Q, \Sigma, \Gamma, \delta, q_0, q_d \rangle$ donde:
      - $Q = \lbrace q_0, q_1, q_2 \rbrace$
      - $\Sigma = \lbrace 0, 1 \rbrace$
      - $\Gamma = \lbrace 0, 1, B \rbrace$
      - $\delta(q_0, B) = (q_d, 0, S)$
      - $\delta(q_0, 0) = (q_0, 0, D)$
      - $\delta(q_0, 1) = (q_1, 1, D)$
      - $\delta(q_1, B) = (q_2, B, I)$
      - $\delta(q_1, 0) = (q_d, 0, S)$
      - $\delta(q_1, 1) = (q_d, 1, S)$
      - $\delta(q_2, 0) = (q_2, B, I)$
      - $\delta(q_2, 1) = (q_2, B, I)$
      - $\delta(q_2, B) = (q_d, B, S)$
   3. Lo que hace esta MT es:
      1. Si la cadena de entrada es $\lambda$, deja un 0 en la cinta y termina.
      2. Si la cadena empieza con 0, se mueve hacia la derecha hasta encontrar un 1 o un blanco.
         1. Si encuentra un 1, va al paso 3.
         2. Si encuentra blanco, deja un cero y termina.
      3. Si la cadena empieza con 1, se asegura que el próximo símbolo sea blanco.
         1. Si es blanco, borra toda la cinta.
         2. Si es un 0 o un 1, deja la cadena tal cual y termina.
4. **Verificación de las condiciones de la reducción**:
   1. $M_f$ es total?
      1. Sí, porque está definida para todos los elementos de $\Sigma^*$. ✅
   2. $M_f$ es computable?
      1. Sí, porque siempre se detiene, debido a que el alfabeto es finito, la cadena de entrada es finita, y no hay bucles infinitos en ninguna transición. ✅
   3. Para cada palabra $w \in L_1$, $f(w) \in L_3$?
      1. Si la cadena de entrada es de la forma $0^n 1$, que pertenece a $L_1$, al aplicar $f(0^n 1)$ se obtiene $\lambda$, que pertenece a $L_3$. ✅
         1. Por ejemplo, si $w = 001 \in L_1$, al aplicar $f(001)$ se obtiene $\lambda \in L_3$.
   4. Para cada palabra $z \notin L_1$, $f(z) \notin L_3$?
      1. Si la cadena de entrada es $\lambda$, que no pertenece a $L_1$, al aplicar $f(\lambda)$ se obtiene $0$, que no pertenece a $L_3$. ✅
      2. Si la cadena de entrada no es de la forma $0^n 1$, que no pertenece a $L_1$, al aplicar $f$ a esa cadena, se obtiene una cadena que es igual a $w$ o $w$ concatenada a un cero al final. En ambos casos, $f(z) \notin L_3$. ✅
         1. Por ejemplo, si $z = 101 \notin L_1$, al aplicar $f(101)$ se obtiene $101 \notin L_3$.

**Por lo tanto, $L_1 \space \alpha \space L_3$**.

### c. Demuestre que existe una reducción $(L_1$ $\alpha$ $L_4)$

1. **Análisis de los lenguajes**:
   1. Las primeras cadenas de $L_1$ son: $1, 01, 001, 0001, 00001, \dots$
   2. Las primeras cadenas de $L_4$ son: $10, 110, 1110, 11110, \dots$
   3. $\lambda$ no pertenece a ninguno de los dos lenguajes.
   4. Se puede ver claramente que la transformación que hay que hacer para pasar de $L_1$ a $L_4$ es, primero invertir todos los bits uno por uno yendo hacia la derecha, y al llegar al símbolo blanco, volver al inicio de la cadena y agregar un uno a la izquierda de su comienzo. Por ejemplo, $001$ se transforma en $110$ al invertir todos sus bits, y luego le agregamos un uno al principio, $1110$, por lo que $001$ se convierte en $1110$, que es $\in L_4$.
2. **Definición de la reducción**:
   1. $L_1 \space \alpha \space L_4$ si existe una función total computable $f: \Sigma^* \rightarrow \Sigma^*$ tal que a cada palabra $w \in L_1$ le corresponde una palabra $f(w) \in L_4$, y a cada palabra $z \notin L_1$ le corresponde una palabra $f(z) \notin L_4$.
3. **Construcción de la $M_f$**:
   1. Podemos definir una MT $M_f$ de cómputo que compute la función $f$ y que siempre se detenga:
   2. $M_f = \langle Q, \Sigma, \Gamma, \delta, q_0, q_d \rangle$ donde:
      - $Q = \lbrace q_0, q_1, q_2 \rbrace$
      - $\Sigma = \lbrace 0, 1 \rbrace$
      - $\Gamma = \lbrace 0, 1, B \rbrace$
      - $\delta(q_0, B) = (q_d, B, S)$
      - $\delta(q_0, 0) = (q_1, 0, S)$
      - $\delta(q_0, 1) = (q_1, 1, S)$
      - $\delta(q_1, 0) = (q_1, 1, D)$
      - $\delta(q_1, 1) = (q_1, 0, D)$
      - $\delta(q_1, B) = (q_2, B, I)$
      - $\delta(q_2, 0) = (q_2, 0, I)$
      - $\delta(q_2, 1) = (q_2, 1, I)$
      - $\delta(q_2, B) = (q_d, 1, S)$
   3. Lo que hace esta MT es:
      1. Si la cadena de entrada es $\lambda$, se detiene dejando $\lambda$.
      2. Si la cadena de entrada comienza con cero o uno, invierte todos los bits yendo hacia la derecha hasta encontrar el símbolo blanco.
      3. Al encontrar el símbolo blanco, vuelve al inicio de la cadena y agrega un uno al comienzo.
4. **Verificación de las condiciones de la reducción**:
   1. $M_f$ es total?
      1. Sí, porque está definida para todos los elementos de $\Sigma^*$. ✅
   2. $M_f$ es computable?
      1. Sí, porque siempre se detiene, debido a que el alfabeto es finito, la cadena de entrada es finita, y no hay bucles infinitos en ninguna transición. ✅
   3. Para cada palabra $w \in L_1$, $f(w) \in L_4$?
      1. Si la cadena de entrada es de la forma $0^n 1$, que pertenece a $L_1$, al aplicar $f(0^n 1)$ se obtiene algo de la forma $1^{n+1}0$, que pertenece a $L_4$. ✅
         1. Por ejemplo, si $w = 001 \in L_1$, al aplicar $f(001)$ se obtiene $1110 \in L_4$.
   4. Para cada palabra $z \notin L_1$, $f(z) \notin L_4$?
      1. Si la cadena de entrada es $\lambda$, que no pertenece a $L_1$, al aplicar $f(\lambda)$ se obtiene $\lambda$, que no pertenece a $L_4$. ✅
      2. Si la cadena de entrada no es de la forma $0^n 1$, que no pertenece a $L_1$, al aplicar $f$ a esa cadena, se obtiene una cadena que no es válida para $L_4$, $f(z) \notin L_4$. ✅
         1. Por ejemplo, si $z = 101 \notin L_1$, al aplicar $f(101)$ se obtiene $1010 \notin L_4$.

**Por lo tanto, $L_1 \space \alpha \space L_4$**.

## 2. Sean $L_1$ y $L_2$, dos lenguajes tales que existe una reducción ($L_1 \space \alpha \space L_2$)

### a. Qué se puede afirmar de $L_1$ si se sabe que $L_2 \in R$

Si se sabe que $L_2 \in R$, esto implica, por teorema, que $L_1 \in R$ también.

Es decir, si existe una reducción de $L_1$ a $L_2$, y se sabe que $L_2$ es recursivo, entonces $L_1$ también es recursivo.

### b. Qué se puede afirmar de $L_1$ si se sabe que $L_2 \in (\text{CO-RE} - RE)$

1. $L_2 \in (\text{CO-RE} - RE)$
2. $\implies (L_2 \in \text{CO-RE}) \land (L_2 \notin RE)$ (Por def. de diferencia de conjuntos)
3. $\implies (\overline{L_2} \in RE) \land (L_2 \notin RE)$ (Por def. de CO-RE)
4. $\implies \overline{L_2} \in RE \rightarrow \overline{L_1} \in RE$ (Por teorema)
5. $\implies \overline{L_1} \in RE \rightarrow L_1 \in \text{CO-RE}$ (Por def. de CO-RE)

Por lo tanto se puede afirmar que si se sabe que $L_2 \in (\text{CO-RE} - RE)$, entonces esto implica que $L_1 \in \text{CO-RE}$

### c. Qué se puede afirmar de $L_2$ si se sabe que $L_1 \in R$

Nada. La reducción $L_1 \space \alpha \space L_2$ solo garantiza que si $L_2$ es decidible, entonces $L_1$ también lo es. Pero si se sabe que $L_1$ es decidible pero no se sabe nada de $L_2$, no se puede concluir nada sobre $L_2$.

### d. Qué se puede afirmar de $L_2$ si se sabe que $L_1 \in (\text{CO-RE} - RE)$

Si $L_1 \in (\text{CO-RE} - RE)$, esto implica que $L_1 \notin RE$, y a su vez esto implica que $L_1 \notin R$. Luego, por la contrarrecíproca del teorema, se sabe que si $L_1 \notin R \rightarrow L_2 \notin R$, con lo cual se puede afirmar que $L_2 \notin RE$ y a su vez $L_2 \notin R$.

Por lo tanto se puede afirmar que si se sabe que $L_1 \in (\text{CO-RE} - RE)$, entonces esto implica que $L_2 \notin RE$.

## 3. Sean $\text{HP}$ y $L_u$ los lenguajes Halting Problem y Lenguaje Universal respectivamente.

### $\text{HP} = \lbrace (\langle M\rangle,w) \mid \text{M se detiene con input w} \rbrace$

### $L_u = \lbrace (\langle M\rangle,w) \mid \text{M acepta w} \rbrace$

### Demuestre que existe una reducción $\text{HP}$ $\alpha$ $L_u$

$\dots$

## 4. Sea $\text{HP}_\lambda$ el Halting Problem a partir de la cinta en blanco:

### $\text{HP}_\lambda = \lbrace \langle M\rangle \mid \text{M se detiene con input } \lambda \rbrace$

### Demuestre que existe una reducción $\text{HP}$ $\alpha$ $\text{HP}_\lambda$

$\dots$

## 5. Demuestre que $L_V \notin RE$:

### $L_V = \lbrace \langle M \rangle \mid L(M) = \emptyset \rbrace$.

### Considere que si $\langle M \rangle$ es un código inválido de máquina de Turing también pertence a $L_V$ (ya que no reconoce ningún string). Así $L_V$ es el complemento del lenguaje $L_{NV} = \lbrace \langle M \rangle \mid L(M) \neq \emptyset \rbrace$

### (Ayuda: puede utilizar el complemento de $L_u$ para encontrar una reducción)

$\dots$
