<h1 align="center">Práctica 6</h1>

## 1. Determinar cuáles de las siguientes afirmaciones son verdaderas y cuáles son falsas:

### a. $\frac{1}{2}n^2 - 3n \in \Theta(n^2)$

- $f(n) = \frac{1}{2}n^2 - 3n$
- $g(n) = n^2$

1. Usando la Regla del límite, sabemos que si $\lim_{n \to \infty} \frac{f(n)}{g(n)} \in \mathbb{R}^+$ entonces $f(n) \in \Theta(g(n))$
2. Reemplazando: $\lim_{n \to \infty} (\frac{\frac{1}{2}n^2 - 3n}{n^2})$
3. Separando los términos: $\lim_{n \to \infty} (\frac{\frac{1}{2}n^2}{n^2} - \frac{3n}{n^2})$
4. Simplificando: $\lim_{n \to \infty} (\frac{1}{2} - \frac{3}{n})$
5. Cuando $n$ tiende a infinito, $\frac{3}{n}$ tiende a 0, por lo que el límite es $\frac{1}{2} - 0 = \frac{1}{2}$
6. Como el límite es un número real positivo $(0.5)$, concluimos que $f(n) \in \Theta(g(n)) \rightarrow (\frac{1}{2}n^2 - 3n \in \Theta(n^2))$

**Por lo tanto, la afirmación es verdadera ✅**.

### b. $n^3 \in O(n^2)$

- $f(n) = n^3$
- $g(n) = n^2$

1. Usamos la Regla del límite y vemos cuál es el resultado, si es un real positivo mayor que cero o es 0, entonces $f(n) \in O(g(n))$, pero si es infinito, entonces no se cumple.
2. Reemplazando: $\lim_{n \to \infty} (\frac{n^3}{n^2})$
3. Simplificando: $\lim_{n \to \infty} (n)$
4. Cuando $n$ tiende a infinito, el límite también tiende a infinito.
5. Por ende, $f(n) \notin O(g(n)) \rightarrow (n^3 \notin O(n^2))$.

**Por lo tanto, la afirmación es falsa ❌**.

### c. $n^2 \in \Omega(n^3)$

- $f(n) = n^2$
- $g(n) = n^3$

1. $\lim_{n \to \infty} (\frac{n^2}{n^3})$
2. Simplificando: $\lim_{n \to \infty} (\frac{1}{n})$
3. Cuando $n$ tiende a infinito, el límite tiende a 0.
4. Como el límite es 0, se sabe por la Regla del Límite que:
   1. $f(n) \in O(g(n)) \implies n^2 \in O(n^3)$
   2. $f(n) \notin \Theta(g(n)) \implies n^2 \notin \Theta(n^3)$
5. Luego, por propiedad se sabe que una función $f(n)$ está en $\Theta(g(n))$ si y solo si está en $O(g(n))$ Y ADEMÁS está en $\Omega(g(n))$.
6. Como $f(n) \notin \Theta(g(n))$, entonces $f(n) \notin \Omega(g(n)) \implies n^2 \notin \Omega(n^3)$.

**Por lo tanto, la afirmación es falsa ❌**.

### d. $2^n \in \Theta(2^{n+1})$

- $f(n) = 2^n$
- $g(n) = 2^{n+1}$

1. $\lim_{n \to \infty} (\frac{2^n}{2^{n+1}})$
2. Transformando la expresión: $\lim_{n \to \infty} (\frac{2^n}{2^n \cdot 2^1})$
3. Simplificando: $\lim_{n \to \infty} (\frac{1}{2}) = \frac{1}{2}$
4. Como el límite es un número real positivo $(0.5)$, se sabe por la Regla del Límite que $f(n) \in \Theta(g(n)) \implies 2^n \in \Theta(2^{n+1})$.

**Por lo tanto, la afirmación es verdadera ✅**.

### e. $n! \in O((n + 1)!)$

- $f(n) = n!$
- $g(n) = (n + 1)!$

1. $\lim_{n \to \infty} (\frac{n!}{(n + 1)!})$
2. Transformando la expresión: $\lim_{n \to \infty} (\frac{n!}{(n + 1) \cdot n!})$
3. Simplificando: $\lim_{n \to \infty} (\frac{1}{n + 1}) = 0$
4. Como el límite es 0, se sabe por la Regla del Límite que $f(n) \in O(g(n)) \implies n! \in O((n + 1)!)$.

**Por lo tanto, la afirmación es verdadera ✅**.

### f. $f : \mathbb{N} \to \mathbb{R}^{\geq 0}, f (n) \in O(n) \implies [f (n)]^2 \in O(n^2)$

La afirmación dice que sea una función $f$ que mapea números naturales a números reales no negativos, si $f(n)$ está en $O(n)$, entonces el cuadrado de $f(n)$ está en $O(n^2)$.

Como $f(n) \in O(n)$, existen $c \in \mathbb{R}^+$ y $n_0 \in \mathbb{N}$ tales que para todo $n \geq n_0$, se cumple que $f(n) \leq (c \cdot n)$.

1. La desigualdad es $f(n) \leq (c \cdot n)$
2. Al elevar ambos lados al cuadrado, obtenemos: $(f(n))^2 \leq (c \cdot n)^2$
3. Aplicando la potencia: $(f(n))^2 \leq (c^2 \cdot n^2)$
4. Se llegó a la definición de $O(n^2)$, porque existen $c^2 \in \mathbb{R}^+$ y $n_0 \in \mathbb{N}$ tales que para todo $n \geq n_0$, se cumple que $(f(n))^2 \leq (c^2 \cdot n^2)$ y por ende, $(f(n))^2 \in O(n^2)$.

**Por lo tanto, la afirmación es verdadera ✅**.

### g. $f : \mathbb{N} \to \mathbb{R}^{\geq 0}, f (n) \in O(n) \implies 2^{f(n)} \in O(2^n)$

La afirmación dice que sea una función $f$ que mapea números naturales a números reales no negativos, si $f(n)$ está en $O(n)$, entonces $2^{f(n)}$ está en $O(2^n)$.

Como $f(n) \in O(n)$, existen $c \in \mathbb{R}^+$ y $n_0 \in \mathbb{N}$ tales que para todo $n \geq n_0$, se cumple que $f(n) \leq (c \cdot n)$.

1. Se puede proveer un contraejemplo para demostrar que la afirmación es falsa.
2. Sea $f(n) = 3n$, entonces $f(n) \in O(n)$.
3. Evaluando el límite: $\lim_{n \to \infty} (\frac{2^{f(n)}}{2^n}) = \lim_{n \to \infty} (\frac{2^{3n}}{2^n})$
4. Usando la propiedad de potencias de igual base: $\lim_{n \to \infty} (2^{3n - n}) = \lim_{n \to \infty} (2^{2n}) = \infty$
5. Como el límite tiende a infinito, se sabe por la Regla del Límite que $f(n) \notin O(g(n)) \implies 2^{f(n)} \notin O(2^n)$.

**Por lo tanto, la afirmación es falsa ❌**.

### h. $f : \mathbb{N} \to \mathbb{R}^{\geq 0}, k \in \mathbb{R}^{\geq 0} \implies kf (n) \in O(f (n))$

1. Se plantea el límite: $\lim_{n \to \infty} \frac{kf(n)}{f(n)}$
2. Simplificando: $\lim_{n \to \infty} k = k$
3. Como se sabe que $k \in \mathbb{R}^{\geq 0}$, entonces el límite es un número real positivo mayor o igual a cero.
4. Por Regla del Límite, se sabe que ya sea que el límite sea cero o mayor que cero, en ambos casos se cumple que $kf(n) \in O(f(n))$.

**Por lo tanto, la afirmación es verdadera ✅**.

### i. Para todo polinomio $p(n)$ de grado $m$, $p(n) \in O(n^m)$

Definición de polinomio de grado $m$: $p(n) = a_m n^m + a_{m-1} n^{m-1} + ... + a_1 n + a_0$ donde $a_m, a_{m-1}, ..., a_1, a_0 \in \mathbb{R}$ y $a_m \neq 0$.

1. Se plantea el límite: $\lim_{n \to \infty} \frac{p(n)}{n^m}$
2. Reemplazando: $\lim_{n \to \infty} \frac{a_m n^m + a_{m-1} n^{m-1} + ... + a_1 n + a_0}{n^m}$
3. Separando en términos: $\lim_{n \to \infty} (\frac{a_m n^m}{n^m} + a_{m-1} \frac{n^{m-1}}{n^m} + ... + a_1 \frac{n}{n^m} + a_0 \frac{1}{n^m})$
4. Simplificando: $\lim_{n \to \infty} (a_m + a_{m-1} \frac{1}{n} + ... + a_1 \frac{1}{n^{m-1}} + a_0 \frac{1}{n^m})$
5. Cuando $n$ tiende a infinito, todos los términos con $n$ en el denominador tienden a 0, por lo que el límite es $a_m + 0 + ... + 0 = a_m$
6. Como $a_m$ es un número real distinto de cero, por Regla del Límite se concluye que $p(n) \in O(n^m)$.

**Por lo tanto, la afirmación es verdadera ✅**.

### j. $\alpha, \beta \in \mathbb{R}, \alpha < \beta \implies n^\alpha \in O(n^\beta)$

1. Reformulo el problema para no usar los símbolos $\alpha$ y $\beta$: Sea $\alpha = a$ y $\beta = b$ con $a < b$.
2. Entonces, la afirmación queda: $a, b \in \mathbb{R}, a < b \implies n^a \in O(n^b)$
3. Se plantea el límite: $\lim_{n \to \infty} \frac{n^a}{n^b}$
4. Por propiedad de las potencias de igual base: $\lim_{n \to \infty} n^{a - b}$
5. Como se sabe que $a < b$, entonces $a - b < 0$, y se sabe que todo número elevado a una potencia negativa tiende a 0.
6. Por ende, el límite tiende a 0, y por Regla del Límite se concluye que $n^a \in O(n^b)$.

**Por lo tanto, la afirmación es verdadera ✅**.

## 2. Probar que se cumplen las siguientes propiedades para $f, g, h : \mathbb{N} \to \mathbb{R}^{\geq 0}$:

### Reflexividad:

#### a. $f(n) \in O(f(n))$

1. Definición formal: $f(n) \in O(f(n))$ si existen dos constantes positivas $c$ y $n_0$ tales que para todo $n \geq n_0$, se cumple que $f(n) \leq c \cdot f(n)$.
2. Si se elige $c = 1$ y $n_0 = 1$, se puede ver trivialmente que $f(n) \leq 1 \cdot f(n)$ porque siempre se cumple $f(n) \leq f(n)$ para todo $n \geq 1$.
3. Por lo tanto queda demostrada la propiedad de reflexividad para $O(f(n))$.

#### b. $f(n) \in \Theta(f(n))$

1. Definición formal: $f(n) \in \Theta(f(n))$ si existen tres constantes positivas $c_1$, $c_2$ y $n_0$ tales que para todo $n \geq n_0$, se cumple que $c_1 \cdot f(n) \leq f(n) \leq c_2 \cdot f(n)$.
2. Si se elige $c_1 = 1$, $c_2 = 1$ y $n_0 = 1$, se puede ver trivialmente que $1 \cdot f(n) \leq f(n) \leq 1 \cdot f(n)$ porque siempre se cumple $f(n) \leq f(n)$ y $f(n) \geq f(n)$ para todo $n \geq 1$.
3. Por lo tanto queda demostrada la propiedad de reflexividad para $\Theta(f(n))$.

#### c. $f(n) \in \Omega(f(n))$

1. Definición formal: $f(n) \in \Omega(f(n))$ si existen dos constantes positivas $c$ y $n_0$ tales que para todo $n \geq n_0$, se cumple que $f(n) \geq c \cdot f(n)$.
2. Si se elige $c = 1$ y $n_0 = 1$, se puede ver trivialmente que $f(n) \geq 1 \cdot f(n)$ porque siempre se cumple $f(n) \geq f(n)$ para todo $n \geq 1$.
3. Por lo tanto queda demostrada la propiedad de reflexividad para $\Omega(f(n))$.

### Transitividad:

#### d. Si $f(n) \in O(g(n))$ y $g(n) \in O(h(n)) \implies f(n) \in O(h(n))$

1. **Queremos probar que existen dos constantes positivas $c$ y $n_0$ tales que para todo $n \geq n_0$, se cumple que $f(n) \leq c \cdot h(n)$**.
2. Como $f(n) \in O(g(n))$, existen constantes positivas $c_1$ y $n_1$ tales que para todo $n \geq n_1$, se cumple que $f(n) \leq c_1 \cdot g(n)$.
3. Como $g(n) \in O(h(n))$, existen constantes positivas $c_2$ y $n_2$ tales que para todo $n \geq n_2$, se cumple que $g(n) \leq c_2 \cdot h(n)$.
4. Por lo tanto, sustituyendo, tenemos que $f(n) \leq c_1 \cdot c_2 \cdot h(n)$ para todo $n \geq \max(n_1, n_2)$.
5. Como todo producto de números positivos es positivo, entonces $c = c_1 \cdot c_2$ es una constante positiva.
6. Entonces tenemos $f(n) \leq c \cdot h(n)$ para todo $n \geq n_0 = \max(n_1, n_2)$.
7. Por lo tanto queda demostrada la propiedad de transitividad para $O(f(n))$.

#### e. Si $f(n) \in \Theta(g(n))$ y $g(n) \in \Theta(h(n)) \implies f(n) \in \Theta(h(n))$

1. **Queremos probar que existen tres constantes positivas $c_1$, $c_2$ y $n_0$ tales que para todo $n \geq n_0$, se cumple que $c_1 \cdot h(n) \leq f(n) \leq c_2 \cdot h(n)$**.
2. Como $f(n) \in \Theta(g(n))$, existen constantes positivas $c_1$, $c_2$ y $n_1$ tales que para todo $n \geq n_1$, se cumple que $c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$.
3. Como $g(n) \in \Theta(h(n))$, existen constantes positivas $c_3$, $c_4$ y $n_2$ tales que para todo $n \geq n_2$, se cumple que $c_3 \cdot h(n) \leq g(n) \leq c_4 \cdot h(n)$.
4. Por lo tanto, sustituyendo, tenemos que $c_1 \cdot c_3 \cdot h(n) \leq f(n) \leq c_2 \cdot c_4 \cdot h(n)$ para todo $n \geq \max(n_1, n_2)$.
5. Como todo producto de números positivos es positivo, entonces $c'_1 = c_1 \cdot c_3$ y $c'_2 = c_2 \cdot c_4$ son constantes positivas.
6. Entonces tenemos $c'_1 \cdot h(n) \leq f(n) \leq c'_2 \cdot h(n)$ para todo $n \geq n_0 = \max(n_1, n_2)$.
7. Por lo tanto queda demostrada la propiedad de transitividad para $\Theta(f(n))$.

#### f. Si $f(n) \in \Omega(g(n))$ y $g(n) \in \Omega(h(n)) \implies f(n) \in \Omega(h(n))$

1. **Queremos probar que existen dos constantes positivas $c$ y $n_0$ tales que para todo $n \geq n_0$, se cumple que $f(n) \geq c \cdot h(n)$**.
2. Como $f(n) \in \Omega(g(n))$, existen constantes positivas $c_1$ y $n_1$ tales que para todo $n \geq n_1$, se cumple que $f(n) \geq c_1 \cdot g(n)$.
3. Como $g(n) \in \Omega(h(n))$, existen constantes positivas $c_2$ y $n_2$ tales que para todo $n \geq n_2$, se cumple que $g(n) \geq c_2 \cdot h(n)$.
4. Por lo tanto, sustituyendo, tenemos que $f(n) \geq c_1 \cdot c_2 \cdot h(n)$ para todo $n \geq \max(n_1, n_2)$.
5. Como todo producto de números positivos es positivo, entonces $c = c_1 \cdot c_2$ es una constante positiva.
6. Entonces tenemos $f(n) \geq c \cdot h(n)$ para todo $n \geq n_0 = \max(n_1, n_2)$.
7. Por lo tanto queda demostrada la propiedad de transitividad para $\Omega(f(n))$.

### Simetría:

#### g. $f(n) \in \Theta(g(n)) \Leftrightarrow g(n) \in \Theta(f(n))$

1. **Tenemos un bicondicional, por lo que debemos demostrar ambas implicaciones**.
2. **Probar que si $f(n) \in \Theta(g(n))$ entonces $g(n) \in \Theta(f(n))$**:

   1. Queremos llegar a que existen tres constantes positivas $c_1$, $c_2$ y $n_0$ tales que para todo $n \geq n_0$, se cumple que $c_1 \cdot f(n) \leq g(n) \leq c_2 \cdot f(n)$.
   2. Como $f(n) \in \Theta(g(n))$, existen constantes positivas $c_3$, $c_4$ y $n_1$ tales que para todo $n \geq n_1$, se cumple que $c_3 \cdot g(n) \leq f(n) \leq c_4 \cdot g(n)$.
   3. Para $c_3 \cdot g(n) \leq f(n)$, dividimos ambos lados por $c_3$ (que es positivo) y obtenemos que $g(n) \leq \frac{1}{c_3} \cdot f(n)$.
   4. Para $f(n) \leq c_4 \cdot g(n)$, dividimos ambos lados por $c_4$ (que es positivo) y obtenemos que $\frac{1}{c_4} \cdot f(n) \leq g(n)$.
   5. Juntando las expresiones, tenemos: $\frac{1}{c_4} \cdot f(n) \leq g(n) \leq \frac{1}{c_3} \cdot f(n)$ para todo $n \geq n_1$.
   6. Asignamos $c_1 = \frac{1}{c_4}$, $c_2 = \frac{1}{c_3}$ y $n_0 = n_1$, que son constantes positivas.
   7. La expresión queda como queríamos: $c_1 \cdot f(n) \leq g(n) \leq c_2 \cdot f(n)$ para todo $n \geq n_0$.
   8. Por lo tanto, queda demostrada esta implicación.

3. **Probar que si $g(n) \in \Theta(f(n))$ entonces $f(n) \in \Theta(g(n))$**:
   1. Queremos llegar a que existen tres constantes positivas $c_1$, $c_2$ y $n_0$ tales que para todo $n \geq n_0$, se cumple que $c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$.
   2. Como $g(n) \in \Theta(f(n))$, existen constantes positivas $c_3$, $c_4$ y $n_1$ tales que para todo $n \geq n_1$, se cumple que $c_3 \cdot f(n) \leq g(n) \leq c_4 \cdot f(n)$.
   3. Para $c_3 \cdot f(n) \leq g(n)$, dividimos ambos lados por $c_3$ (que es positivo) y obtenemos que $f(n) \leq \frac{1}{c_3} \cdot g(n)$.
   4. Para $g(n) \leq c_4 \cdot f(n)$, dividimos ambos lados por $c_4$ (que es positivo) y obtenemos que $\frac{1}{c_4} \cdot g(n) \leq f(n)$.
   5. Juntando las expresiones, tenemos: $\frac{1}{c_4} \cdot g(n) \leq f(n) \leq \frac{1}{c_3} \cdot g(n)$ para todo $n \geq n_1$.
   6. La expresión queda como queríamos: $c_1 \cdot g(n) \leq f(n) \leq c_2 \cdot g(n)$ para todo $n \geq n_0$, con $c_1 = \frac{1}{c_4}$, $c_2 = \frac{1}{c_3}$ y $n_0 = n_1$.
   7. Por lo tanto, queda demostrada esta implicación.
4. Por lo tanto queda demostrada la propiedad de simetría para $\Theta(f(n))$.

### Simetría traspuesta:

#### h. $f(n) \in O(g(n)) \Leftrightarrow g(n) \in \Omega(f(n))$

1. **Tenemos un bicondicional, por lo que debemos demostrar ambas implicaciones**.
2. **Probar que si $f(n) \in O(g(n))$ entonces $g(n) \in \Omega(f(n))$**:
   1. Queremos llegar a que existen dos constantes positivas $c$ y $n_0$ tales que para todo $n \geq n_0$, se cumple que $g(n) \geq c \cdot f(n)$.
   2. Como $f(n) \in O(g(n))$, existen constantes positivas $c_1$ y $n_1$ tales que para todo $n \geq n_1$, se cumple que $f(n) \leq c_1 \cdot g(n)$.
   3. Dividiendo ambos lados por $c_1$ (que es positivo), obtenemos que $\frac{1}{c_1} \cdot f(n) \leq g(n)$.
   4. Asignamos $c = \frac{1}{c_1}$ y $n_0 = n_1$, que son constantes positivas.
   5. Entonces tenemos $g(n) \geq c \cdot f(n)$ para todo $n \geq n_0$.
   6. Por lo tanto queda demostrada esta implicación.
3. **Probar que si $g(n) \in \Omega(f(n))$ entonces $f(n) \in O(g(n))$**:
   1. Queremos llegar a que existen dos constantes positivas $c$ y $n_0$ tales que para todo $n \geq n_0$, se cumple que $f(n) \leq c \cdot g(n)$.
   2. Como $g(n) \in \Omega(f(n))$, existen constantes positivas $c_1$ y $n_1$ tales que para todo $n \geq n_1$, se cumple que $g(n) \geq c_1 \cdot f(n)$.
   3. Dividiendo ambos lados por $c_1$ (que es positivo), obtenemos que $f(n) \leq \frac{1}{c_1} \cdot g(n)$.
   4. Asignamos $c = \frac{1}{c_1}$ y $n_0 = n_1$, que son constantes positivas.
   5. Entonces tenemos $f(n) \leq c \cdot g(n)$ para todo $n \geq n_0$.
   6. Por lo tanto queda demostrada esta implicación.
4. Por lo tanto queda demostrada la propiedad de simetría traspuesta para $O(g(n))$ y $\Omega(f(n))$.
