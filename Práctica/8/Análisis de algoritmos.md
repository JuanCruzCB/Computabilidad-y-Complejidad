<h1 align="center">Práctica 8</h1>

## 1. Determinar para cada función $t(n)$ en la siguiente tabla, cuál es el mayor tamaño $n$ de una instancia de un problema que puede ser resuelto en cada uno de los tiempos indicados en las columnas de la tabla, suponiendo que el algoritmo para resolverlo utiliza $t(n)$ microsegundos.

| $t(n)$              | 1 seg.              | 1 min.               | 1 hora                 | 1 día                    | 1 mes                     | 1 año                       | 1 siglo                     |
| ------------------- | ------------------- | -------------------- | ---------------------- | ------------------------ | ------------------------- | --------------------------- | --------------------------- |
| $log_2(n)$          | $2^{10^6}$          | $2^{6 \times 10^7}$  | $2^{36 \times 10^8}$   | $2^{864 \times 10^8}$    | $2^{25920 \times 10^8}$   | $2^{311040 \times 10^8}$    | $2^{31104000 \times 10^8}$  |
| $\sqrt{n}$          | $10^{12}$           | $3.6 \times 10^{15}$ | $1.296 \times 10^{19}$ | $7.46496 \times 10^{21}$ | $6.718464 \times 10^{24}$ | $9.67458816 \times 10^{26}$ | $9.67458816 \times 10^{30}$ |
| $n$                 | $10^6$              | $6 \times 10^7$      | $3.6 \times 10^9$      | $8.64 \times 10^{10}$    | $2.592 \times 10^{12}$    | $3.1104 \times 10^{13}$     | $3.1104 \times 10^{15}$     |
| $n \times log_2(n)$ | $6.275 \times 10^4$ | $2.801 \times 10^6$  | $1.334 \times 10^8$    | $2.755 \times 10^9$      | $7.187 \times 10^{10}$    | $7.871 \times 10^{11}$      | $6.77 \times 10^{13}$       |
| $n^2$               | $10^3$              | $7.746 \times 10^3$  | $6 \times 10^4$        | $2.9393 \times 10^5$     | $1.61046 \times 10^6$     | $5.5757 \times 10^6$        | $5.5757 \times 10^7$        |
| $2^n$               | $19.93$             | $25.84$              | $31.75$                | $36.33$                  | $41.24$                   | $44.82$                     | $51.46$                     |
| $n!$                | $\approx 9$         | $\approx 11$         | $\approx 12$           | $\approx 13$             | $\approx 15$              | $\approx 16$                | $\approx 17$                |

- **Referencias de tiempo en microsegundos ($\mu s$)**:
  - $\text{1 seg} = 10^6 \mu s$
  - $\text{1 min} = 60 \times 10^6 \mu s$
  - $\text{1 hora} = 3600 \times 10^6 \mu s$
  - $\text{1 día} = 24 \times 3600 \times 10^6 \mu s = 86400 \times 10^6 \mu s$
  - $\text{1 mes} = 30 \times 24 \times 3600 \times 10^6 \mu s = 2592000 \times 10^6 \mu s$
  - $\text{1 año} = 12 \times 30 \times 24 \times 3600 \times 10^6 \mu s = 31104000 \times 10^6 \mu s$
  - $\text{1 siglo} = 100 \times 12 \times 30 \times 24 \times 3600 \times 10^6 \mu s = 3110400000 \times 10^6 \mu s$

1. **$log_2(n)$**:
   1. **1 seg**:
      1. $log_2(n) = 10^6$
      2. $2^{10^6} = n$
      3. $n = 2^{10^6}$
   2. **1 min**:
      1. $log_2(n) = 60 \times 10^6$
      2. $2^{60 \times 10^6} = n$
      3. $n = 2^{60 \times 10^6}$
      4. $n = 2^{6 \times 10^7}$
   3. **1 hora**:
      1. $log_2(n) = 3600 \times 10^6$
      2. $2^{3600 \times 10^6} = n$
      3. $n = 2^{3600 \times 10^6}$
      4. $n = 2^{36 \times 10^8}$
   4. **1 día**:
      1. $log_2(n) = 24 \times 3600 \times 10^6$
      2. $2^{24 \times 3600 \times 10^6} = n$
      3. $n = 2^{24 \times 3600 \times 10^6}$
      4. $n = 2^{24 \times 36 \times 10^8}$
      5. $n = 2^{864 \times 10^8}$
   5. **1 mes**:
      1. $log_2(n) = 30 \times 24 \times 3600 \times 10^6$
      2. $2^{30 \times 24 \times 3600 \times 10^6} = n$
      3. $n = 2^{30 \times 24 \times 3600 \times 10^6}$
      4. $n = 2^{30 \times 24 \times 36 \times 10^8}$
      5. $n = 2^{25920 \times 10^8}$
   6. **1 año**:
      1. $log_2(n) = 12 \times 30 \times 24 \times 3600 \times 10^6$
      2. $2^{12 \times 30 \times 24 \times 3600 \times 10^6} = n$
      3. $n = 2^{12 \times 30 \times 24 \times 3600 \times 10^6}$
      4. $n = 2^{12 \times 30 \times 24 \times 36 \times 10^8}$
      5. $n = 2^{311040 \times 10^8}$
   7. **1 siglo**:
      1. $log_2(n) = 100 \times 12 \times 30 \times 24 \times 3600 \times 10^6$
      2. $2^{100 \times 12 \times 30 \times 24 \times 3600 \times 10^6} = n$
      3. $n = 2^{100 \times 12 \times 30 \times 24 \times 3600 \times 10^6}$
      4. $n = 2^{100 \times 12 \times 30 \times 24 \times 36 \times 10^8}$
      5. $n = 2^{31104000 \times 10^8}$
2. **$\sqrt{n}$**:
   1. **1 seg**:
      1. $\sqrt{n} = 10^6$
      2. $n = (10^6)^2$
      3. $n = 10^{12}$
   2. **1 min**:
      1. $n = 60^2 \times 10^{12}$
      2. $n = 3600 \times 10^{12}$
      3. $n = 3.6 \times 10^{15}$
   3. **1 hora**:
      1. $n = 60^2 \times (3.6 \times 10^{15})$
      2. $n = 3600 \times (3.6 \times 10^{15})$
      3. $n = 12960 \times 10^{15}$
      4. $n = 1.296 \times 10^{19}$
   4. **1 día**:
      1. $n = 24^2 \times (1.296 \times 10^{19})$
      2. $n = 576 \times (1.296 \times 10^{19})$
      3. $n = 746.496 \times 10^{19}$
      4. $n = 7.46496 \times 10^{21}$
   5. **1 mes**:
      1. $n = 30^2 \times (7.46496 \times 10^{21})$
      2. $n = 900 \times (7.46496 \times 10^{21})$
      3. $n = 6718.464 \times 10^{21}$
      4. $n = 6.718464 \times 10^{24}$
   6. **1 año**:
      1. $n = 12^2 \times (6.718464 \times 10^{24})$
      2. $n = 144 \times (6.718464 \times 10^{24})$
      3. $n = 967.458816 \times 10^{24}$
      4. $n = 9.67458816 \times 10^{26}$
   7. **1 siglo**:
      1. $n = 100^2 \times (9.67458816 \times 10^{26})$
      2. $n = 10000 \times (9.67458816 \times 10^{26})$
      3. $n = 96745.8816 \times 10^{26}$
      4. $n = 9.67458816 \times 10^{30}$
3. **$n$**:
   1. **1 seg**:
      1. $n = 10^6$
   2. **1 min**:
      1. $n = 60 \times 10^6$
      2. $n = 6 \times 10^7$
   3. **1 hora**:
      1. $n = 3600 \times 10^6$
      2. $n = 3.6 \times 10^9$
   4. **1 día**:
      1. $n = 24 \times 3600 \times 10^6$
      2. $n = 86400 \times 10^6$
      3. $n = 8.64 \times 10^{10}$
   5. **1 mes**:
      1. $n = 30 \times 24 \times 3600 \times 10^6$
      2. $n = 2592000 \times 10^6$
      3. $n = 2.592 \times 10^{12}$
   6. **1 año**:
      1. $n = 12 \times 30 \times 24 \times 3600 \times 10^6$
      2. $n = 31104000 \times 10^6$
      3. $n = 3.1104 \times 10^{13}$
   7. **1 siglo**:
      1. $n = 100 \times 12 \times 30 \times 24 \times 3600 \times 10^6$
      2. $n = 3110400000 \times 10^6$
      3. $n = 3.1104 \times 10^{15}$
4. **$n \times log_2(n)$**:
   1. **1 seg**:
      1. $n \times log_2(n) = 10^6$
      2. Esta ecuación no tiene una solución algebraica directa, por lo que se debe resolver numéricamente o mediante aproximaciones.
      3. Se sabe que $n \leq n \times log_2(n) \leq n^2$, por lo que $n$ estará entre $10^3$ y $10^6$.
      4. Usando el programa `metodo_numerico.py`, se obtiene que $n \approx 6.275 \times 10^4$.
   2. **1 min**:
      1. $n \times log_2(n) = 60 \times 10^6$
      2. $n$ estará entre $7.746 \times 10^3$ y $6 \times 10^7$.
      3. Usando el programa `metodo_numerico.py`, se obtiene que $n \approx 2.801 \times 10^6$.
   3. **1 hora**:
      1. $n \times log_2(n) = 3600 \times 10^6$
      2. $n$ estará entre $6 \times 10^4$ y $3.6 \times 10^9$.
      3. Usando el programa `metodo_numerico.py`, se obtiene que $n \approx 1.334 \times 10^8$.
   4. **1 día**:
      1. $n \times log_2(n) = 24 \times 3600 \times 10^6$
      2. $n$ estará entre $2.939 \times 10^5$ y $8.64 \times 10^{10}$.
      3. Usando el programa `metodo_numerico.py`, se obtiene que $n \approx 2.755 \times 10^9$.
   5. **1 mes**:
      1. $n \times log_2(n) = 30 \times 24 \times 3600 \times 10^6$
      2. $n$ estará entre $1.61 \times 10^6$ y $2.592 \times 10^{12}$.
      3. Usando el programa `metodo_numerico.py`, se obtiene que $n \approx 7.187 \times 10^{10}$.
   6. **1 año**:
      1. $n \times log_2(n) = 12 \times 30 \times 24 \times 3600 \times 10^6$
      2. $n$ estará entre $5.576 \times 10^6$ y $3.11 \times 10^{13}$.
      3. Usando el programa `metodo_numerico.py`, se obtiene que $n \approx 7.871 \times 10^{11}$.
   7. **1 siglo**:
      1. $n \times log_2(n) = 100 \times 12 \times 30 \times 24 \times 3600 \times 10^6$
      2. $n$ estará entre $5.576 \times 10^7$ y $3.11 \times 10^{15}$.
      3. Usando el programa `metodo_numerico.py`, se obtiene que $n \approx 6.77 \times 10^{13}$.
5. **$n^2$**:
   1. **1 seg**:
      1. $n^2 = 10^6$
      2. $n = \sqrt{10^6}$
      3. $n = 10^3$
   2. **1 min**:
      1. $n = \sqrt{60} \times 10^3$
      2. $n = 7.746 \times 10^3$
   3. **1 hora**:
      1. $n = \sqrt{60} \times 7.746 \times 10^3$
      2. $n = 7.746 \times 7.746 \times 10^3$
      3. $n = 60 \times 10^3$
      4. $n = 6 \times 10^4$
   4. **1 día**:
      1. $n = \sqrt{24} \times 6 \times 10^4$
      2. $n = 4.898979486 \times 6 \times 10^4$
      3. $n = 29.393 \times 10^4$
      4. $n = 2.9393 \times 10^5$
   5. **1 mes**:
      1. $n = \sqrt{30} \times 2.9393 \times 10^5$
      2. $n = 5.477 \times 2.9393 \times 10^5$
      3. $n = 16.1046 \times 10^5$
      4. $n = 1.61046 \times 10^6$
   6. **1 año**:
      1. $n = \sqrt{12} \times 1.61046 \times 10^6$
      2. $n = 3.4641 \times 1.61046 \times 10^6$
      3. $n = 5.5757 \times 10^6$
   7. **1 siglo**:
      1. $n = \sqrt{100} \times 5.5757 \times 10^6$
      2. $n = 10 \times 5.5757 \times 10^6$
      3. $n = 55.757 \times 10^6$
      4. $n = 5.5757 \times 10^7$
6. **$2^n$**:
   1. **1 seg**:
      1. $2^n = 10^6$
      2. $log(2^n) = log(10^6)$
      3. $n \times log(2) = log(10^6)$
      4. $n \times log(2) = 6$
      5. $n = \frac{6}{log(2)}$
      6. $n = \frac{6}{0.301}$
      7. $n = 19.93$
   2. **1 min**:
      1. $n = log_2(60) + 19.93$
      2. $n = 5.9069 + 19.93$
      3. $n = 25.84$
   3. **1 hora**:
      1. $n = log_2(60) + 25.84$
      2. $n = 5.9069 + 25.84$
      3. $n = 31.75$
   4. **1 día**:
      1. $n = log_2(24) + 31.75$
      2. $n = 4.5849 + 31.75$
      3. $n = 36.33$
   5. **1 mes**:
      1. $n = log_2(30) + 36.33$
      2. $n = 4.9069 + 36.33$
      3. $n = 41.24$
   6. **1 año**:
      1. $n = log_2(12) + 41.2369$
      2. $n = 3.5849 + 41.2369$
      3. $n = 44.82$
   7. **1 siglo**:
      1. $n = log_2(100) + 44.8218$
      2. $n = 6.6439 + 44.8218$
      3. $n = 51.46$
7. **$n!$**:
   1. **1 seg**:
      1. $n! = 10^6$
      2. $n \approx 9$
   2. **1 min**:
      1. $n! = 60 \times 10^6$
      2. $n \approx 11$
   3. **1 hora**:
      1. $n! = 3600 \times 10^6$
      2. $n \approx 12$
   4. **1 día**:
      1. $n! = 24 \times 3600 \times 10^6$
      2. $n \approx 13$
   5. **1 mes**:
      1. $n! = 30 \times 24 \times 3600 \times 10^6$
      2. $n \approx 15$
   6. **1 año**:
      1. $n! = 365 \times 24 \times 3600 \times 10^6$
      2. $n \approx 16$
   7. **1 siglo**:
      1. $n! = 100 \times 365 \times 24 \times 3600 \times 10^6$
      2. $n \approx 17$

## 2. Si el tiempo de ejecución en el mejor caso de un algoritmo, $t_m(n)$, es tal que $t_m(n) \in \Omega(f (n))$ y el tiempo de ejecución en el peor caso de un algoritmo, $t_p(n)$, es tal que $t_p(n) \in O(f (n))$, ¿Se puede afirmar que el tiempo de ejecución del algoritmo es $\Theta(f (n))$?

- Tiempo de ejecución del algoritmo en el mejor caso: $t_m(n) \in \Omega(f(n))$
- Tiempo de ejecución del algoritmo en el peor caso: $t_p(n) \in O(f(n))$

Sí, se puede afirmar que el tiempo de ejecución del algoritmo es $\Theta(f(n))$, porque por definición de la notación $\Theta$, si una función está acotada inferiormente por $f(n)$ (es decir, pertenece a $\Omega(f(n))$) y acotada superiormente por $f(n)$ (es decir, pertenece a $O(f(n))$), entonces pertenece a $\Theta(f(n))$.

## 3. Un algoritmo tarda 1 segundo en procesar 1000 items en una máquina determinada. ¿Cuánto tiempo tomará procesar 10000 items si se sabe que el tiempo de ejecución del algoritmo es $n^2$? ¿y si se sabe que es $n \times log_2(n)$? ¿Qué se estaría asumiendo en todos los casos?

1. Caso 1: El tiempo de ejecución del algoritmo es $n^2$.
   1. Se puede usar una regla de tres simple.
   2. $\text{1000 items} \rightarrow \text{1 segundo}$
   3. $\text{10000 items} \rightarrow x$
   4. Como se sabe que el tiempo de ejecución es $n^2$, se puede plantear la siguiente ecuación:
   5. $x = \frac{(10000^2) \times 1}{1000^2}$
   6. $x = \frac{100000000 \times 1}{1000000}$
   7. $x = 100 \text{ segundos}$.
2. Caso 2: El tiempo de ejecución del algoritmo es $n \times log_2(n)$.
   1. Se puede usar una regla de tres simple.
   2. $\text{1000 items} \rightarrow \text{1 segundo}$
   3. $\text{10000 items} \rightarrow x$
   4. Como se sabe que el tiempo de ejecución es $n \times log_2(n)$, se puede plantear la siguiente ecuación:
   5. $x = \frac{(10000 \times log_2(10000)) \times 1}{(1000 \times log_2(1000))}$
   6. $x = \frac{(10000 \times 13.287)}{(1000 \times 9.965)}$
   7. $x = \frac{132870}{9965}$
   8. $x \approx 13.333 \text{ segundos}$.

En ambos casos se está asumiendo que no hay casos a analizar, es decir, que el tiempo de ejecución del algoritmo es siempre el mismo independientemente de la entrada que se reciba.

## 4. Un algoritmo toma $n^2$ días y otro $n^3$ segundos para resolver una instancia de tamaño $n$ de un problema. Mostrar que el segundo algoritmo superará en tiempo al primero solamente en instancias que requieran más de 20 millones de años para ser resueltas.

- $t_1(n) = n^2$ días
- $t_2(n) = n^3$ segundos
- Convertir a la misma unidad de tiempo:
  - $t_1(n) = n^2 \times 86400$ segundos (ya que un día tiene 86400 segundos)
  - $t_2(n) = n^3$ segundos
- Se quiere encontrar el valor de $n$ tal que $t_2(n) > t_1(n)$:
  - $n^3 > n^2 \times 86400$
  - Dividiendo ambos lados por $n^2$ (asumiendo $n > 0$):
  - $n > 86400$
  - Es decir, el segundo algoritmo solo se vuelve más lento cuando la entrada es estrictamente mayor a $86400$.
  - Reemplazando en la función: $t_1(86400) = (86400)^2 \text{ días} = 7464960000 \text{ días}$
  - Usando un [conversor online de días a años](https://www.inchcalculator.com/convert/day-to-year/) se tiene que $7464960000 \text{ días} \approx 20438366 \text{ años}$, es decir, más de $20$ millones de años.
- Por lo tanto, se ha demostrado que el segundo algoritmo superará en tiempo al primero solamente en instancias que requieran aproximadamente más de 20 millones de años para ser resueltas.

## 5. ¿Cuáles y cuántas serían las operaciones elementales necesarias para multiplicar dos enteros $n$ y $m$ por medio del algoritmo enseñado en la escuela primaria? ¿Esta cantidad depende de la entrada? Justifique.

El algoritmo enseñado en la escuela primaria consiste en multiplicar cada dígito del segundo número por cada dígito del primer número y luego sumar los resultados parciales.

Sea $n$ un número con $d_n$ dígitos y $m$ un número con $d_m$ dígitos. Por ejemplo, si $n = 1998$, entonces $d_n = 4$, y si $m = 123$, entonces $d_m = 3$.

Una operación elemental en este contexto es una multiplicación de dos dígitos o una suma de dos dígitos. Por ejemplo, $8 \times 3$ es una operación elemental, al igual que $24 + 15$.

El algoritmo realiza los siguientes pasos:

1. Multiplicar cada dígito de $m$ por cada dígito de $n$, uno por uno.
   1. Como $m$ tiene $d_m$ dígitos y $n$ tiene $d_n$ dígitos, esto produce $(d_n \times d_m)$ multiplicaciones.
   2. Por ejemplo, si $n = 1998$ y $m = 123$, se realizan $4 \times 3 = 12$ multiplicaciones.
2. Una vez se hicieron todas las multiplicaciones, se tiene una lista de resultados parciales que deben sumarse de forma vertical.
   1. Se deben sumar $d_m$ filas, donde cada fila tiene aproximadamente $d_n$ dígitos
   2. El total de sumas aproximado es $(d_n \times d_m)$
3. Por lo tanto, el total de operaciones elementales necesarias para multiplicar dos enteros $n$ y $m$ es aproximadamente:
   1. Total de multiplicaciones: $d_n \times d_m$
   2. Total de sumas: $d_n \times d_m$
   3. Total de operaciones elementales: $2 \times (d_n \times d_m)$
4. Entonces el orden de complejidad del algoritmo es $O(d_n \times d_m)$. Si ambos números tienen la misma cantidad de dígitos $d$, entonces la complejidad es $O(d^2)$, es decir, cuadrática en función del número de dígitos.
5. La cantidad de operaciones depende directamente de la entrada, y en particular de la cantidad de dígitos de los números que se están multiplicando. A medida que los números crecen en tamaño (más dígitos), el número de operaciones elementales necesarias para realizar la multiplicación también aumenta.

## 6. Dar el tiempo de ejecución en función de $n$ de los siguientes algoritmos y una $f(n)$ tal que el tiempo de ejecución pertenezca a $\Theta(f(n))$. Determine si cada algoritmo o partes del mismo tiene casos de análisis (peor, mejor, etc).

### a.

![](https://i.imgur.com/w2i68Qr.png)

1. $1 + \sum_{i=1}^{n} \sum_{j=1}^{n^2} \sum_{k=1}^{n^3} 2$
2. $1 + \sum_{i=1}^{n} \sum_{j=1}^{n^2} (2n^3)$
3. $1 + \sum_{i=1}^{n} n^2 \cdot (2n^3)$
4. $1 + \sum_{i=1}^{n} (2n^5)$
5. $1 + n \cdot (2n^5)$
6. $1 + 2n^6$
7. El tiempo de ejecución en función de $n$ del algoritmo es $t(n) = 1 + 2n^6$.
8. Se pide hallar una función $f(n)$ tal que $t(n) \in \Theta(f(n))$.
9. Como $t(n)$ es un polinomio de grado 6 y el orden $\Theta$ ignora las constantes multiplicativas y los términos de menor grado, se tiene que $t(n) \in \Theta(n^6)$, es decir $f(n) = n^6$.
10. El análisis del algoritmo no tiene casos especiales, ya que el tiempo de ejecución es siempre el mismo independientemente de la entrada que se reciba, por lo que no hay un mejor o peor caso.

### b.

![](https://i.imgur.com/ePivfyT.png)

1. $1 + \sum_{i=1}^{n} \sum_{j=1}^i \sum_{k=1}^n 2$
2. $1 + \sum_{i=1}^{n} \sum_{j=1}^i n \cdot 2$
3. $1 + \sum_{i=1}^{n} \sum_{j=1}^i 2n$
4. $1 + \sum_{i=1}^{n} i \cdot 2n$
5. Usamos la equivalencia $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$
6. $1 + \frac{n(n+1)}{2} \cdot 2n$
7. $1 + \frac{n^2 + n}{2} \cdot 2n$
8. $1 + (n^2 + n) \cdot n$
9. $1 + n^3 + n^2$
10. El tiempo de ejecución en función de $n$ del algoritmo es $t(n) = 1 + n^3 + n^2$.
11. Se pide hallar una función $f(n)$ tal que $t(n) \in \Theta(f(n))$.
12. Como $t(n)$ es un polinomio de grado 3 y el orden $\Theta$ ignora las constantes multiplicativas y los términos de menor grado, se tiene que $t(n) \in \Theta(n^3)$, es decir $f(n) = n^3$.
13. El análisis del algoritmo no tiene casos especiales, ya que el tiempo de ejecución es siempre el mismo independientemente de la entrada que se reciba, por lo que no hay un mejor o peor caso.

## 7. Definir y analizar el tiempo de ejecución de la multiplicación de una matriz triangular inferior por una matriz completa (en la que todos sus elementos pueden ser diferentes de 0). ¿Qué formas tiene de hallar $t(n)$? ¿De cuántas formas podría encontrar la pertenencia a $O()$ o a $\Theta()$ del algoritmo?

1. Una matriz triangular inferior es una matriz cuadrada en la que todos los elementos por encima de la diagonal principal son cero. Su forma general es:

   $\begin{pmatrix}
   a_{1,1} & 0 & 0 & \cdots & 0 \\
   a_{2,1} & a_{2,2} & 0 & \cdots & 0 \\
   a_{3,1} & a_{3,2} & a_{3,3} & \cdots & 0 \\
   \vdots & \vdots & \vdots & \ddots & \vdots \\
   a_{n,1} & a_{n,2} & a_{n,3} & \cdots & a_{n,n}
   \end{pmatrix}$

2. Una matriz completa, por otro lado, es una matriz en la que todos sus elementos pueden ser diferentes de cero. Su forma general es:

   $\begin{pmatrix}
   b_{1,1} & b_{1,2} & b_{1,3} & \cdots & b_{1,n} \\
   b_{2,1} & b_{2,2} & b_{2,3} & \cdots & b_{2,n} \\
   b_{3,1} & b_{3,2} & b_{3,3} & \cdots & b_{3,n} \\
   \vdots & \vdots & \vdots & \ddots & \vdots \\
   b_{n,1} & b_{n,2} & b_{n,3} & \cdots & b_{n,n}
   \end{pmatrix}$

3. La multiplicación de matrices se realiza tomando cada fila de la primera matriz y multiplicándola por cada columna de la segunda matriz, sumando los productos correspondientes. Como la primera matriz es triangular inferior, muchos de sus elementos son cero, lo que reduce la cantidad de multiplicaciones necesarias.
4. Para calcular el tiempo de ejecución $t(n)$ de la multiplicación de una matriz triangular inferior por una matriz completa, se puede observar que:
   1. En la primera fila de la matriz triangular inferior, solo hay un elemento distinto de cero, por lo que se realizan $n$ multiplicaciones.
   2. En la segunda fila, hay dos elementos distintos de cero, por lo que se realizan $2n$ multiplicaciones.
   3. En la tercera fila, hay tres elementos distintos de cero, por lo que se realizan $3n$ multiplicaciones.
   4. Este patrón continúa hasta la última fila, donde hay $n$ elementos distintos de cero, por lo que se realizan $nn = n^2$ multiplicaciones.
   5. Por lo tanto, el total de multiplicaciones necesarias es: $T(n) = n + 2n + 3n + \cdots + nn = n(1 + 2 + 3 + \cdots + n) = (n \cdot \sum_{i=1}^{n} i) = n \cdot (\frac{n(n+1)}{2}) = n \cdot (\frac{n^2 + n}{2}) = \frac{n^3 + n^2}{2}$.
   6. Así, el tiempo de ejecución en función de $n$ es $t(n) = \frac{n^3 + n^2}{2}$.
   7. Se pide hallar una función $f(n)$ tal que $t(n) \in \Theta(f(n))$.
   8. Como $t(n)$ es un polinomio de grado 3 y el orden $\Theta$ ignora las constantes multiplicativas y los términos de menor grado, se tiene que $t(n) \in \Theta(n^3)$, es decir $f(n) = n^3$.

Lo anterior es el método analítico de hallar $t(n)$. Otra forma de hallarlo es planteando el pseudocódigo correspondiente al problema, y luego convirtiendo sus bucles en sumatorias, similar al ejercicio 6.

## 8. ¿Encuentra algún inconveniente para analizar las iteraciones `while` y `repeat` como recurrencias?

Las iteraciones `while` y `repeat` suelen ser complicadas de analizar como recurrencias ya que su número de iteraciones puede variar según condiciones que dependen de la entrada o del estado interno del algoritmo. A diferencia de los bucles `for`, donde el número de iteraciones es generalmente conocido de antemano, los bucles `while` y `repeat` pueden continuar ejecutándose hasta que se cumpla una condición específica, lo que puede hacer que el análisis sea más complejo.

## 9. Considerar las matrices $A, B, C \in \mathbb{R}^{(n \times n)}$, y la notación tal que $X_{i, j}$, con $1 \leq i, j \leq 2$ y $X$ cualquiera de las matrices $A, B$ o $C$, identifica una de las cuatro submatrices de orden $\frac{n}{2}$

### a. Dar el orden del tiempo de ejecución del algoritmo D&C que se describe con las ecuaciones:

#### $C_{1,1} = A_{1,1} \times B_{1,1} + A_{1,2} \times B_{2,1}$

#### $C_{1,2} = A_{1,1} \times B_{1,2} + A_{1,2} \times B_{2,2}$

#### $C_{2,1} = A_{2,1} \times B_{1,1} + A_{2,2} \times B_{2,1}$

#### $C_{2,2} = A_{2,1} \times B_{1,2} + A_{2,2} \times B_{2,2}$

#### ¿Sería necesario definir algo más?

Se plantea una forma de multiplicar matrices distinta a la tradicional. En el enfoque dado, la estrategia es de tipo Divide & Conquer, donde cada matriz, $A$ y $B$, se divide en cuatro submatrices de tamaño $\frac{n}{2} \times \frac{n}{2}$. Luego, se realizan multiplicaciones y sumas de estas submatrices para obtener las submatrices de la matriz resultante $C$. Por ejemplo, si $n = 16$, entonces cada submatriz tendrá un tamaño de $8 \times 8$.

Para dar el orden del tiempo de ejecución del algoritmo D&C, se puede armar la ecuación de recurrencia $t(n)$. Como el problema es de tipo Divide & Conquer, la receta que se usa es la de reducción por división, que tiene la fórmula general: $t(n) = a \cdot t(\frac{n}{b}) + f(n)$, donde:

- $a$ es la cantidad de llamadas recursivas, es decir, subproblemas.
- $b$ es el factor por el cual se divide el tamaño del problema en cada llamada recursiva.
- $f(n)$ son operaciones extra a las llamadas recursivas, normalmente el costo de combinar los resultados parciales.

Analizando las ecuaciones dadas, tenemos 8 multiplicaciones de submatrices (cada una de tamaño $\frac{n}{2} \times \frac{n}{2}$) y 4 sumas de matrices (cada una de tamaño $\frac{n}{2} \times \frac{n}{2}$). Por lo tanto: $a = 8$, $b = 2$ y $f(n) = O(n^2)$ ya que sumar dos matrices de tamaño $\frac{n}{2} \times \frac{n}{2}$ toma tiempo proporcional a $\left(\frac{n}{2}\right)^2 = \frac{n^2}{4}$, y hay 4 sumas, por lo que se tiene $4 \cdot \frac{n^2}{4} = n^2$.

La ecuación de recurrencia queda entonces: $t(n) = 8 \cdot t(\frac{n}{2}) + n^2$.

$f(n) \in O(n^k)$, con $k = 2$.

Se tiene que $a > b^k$ porque $8 > 2^2$. Entonces, por teorema maestro, el tiempo de ejecución es: $t(n) \in O(n^{log_b(a)}) = O(n^{log_2(8)}) = O(n^3)$.

Por lo tanto, el orden del tiempo de ejecución del algoritmo D&C es $O(n^3)$.

### b. Buscar el algoritmo de Strassen, dar su definición en función de las submatrices $X_{i, j}$ anteriores y dar su orden de tiempo de ejecución.

El algoritmo de Strassen es otro algoritmo de multiplicación de matrices que tiene como ventaja un menor tiempo de ejecución en comparación con el método tradicional. Su definición en función de las submatrices $X_{i, j}$ es la siguiente:

- $M_1 = (A_{1,1} + A_{2,2}) \times (B_{1,1} + B_{2,2})$
- $M_2 = (A_{2,1} + A_{2,2}) \times B_{1,1}$
- $M_3 = A_{1,1} \times (B_{1,2} - B_{2,2})$
- $M_4 = A_{2,2} \times (B_{2,1} - B_{1,1})$
- $M_5 = (A_{1,1} + A_{1,2}) \times B_{2,2}$
- $M_6 = (A_{2,1} - A_{1,1}) \times (B_{1,1} + B_{1,2})$
- $M_7 = (A_{1,2} - A_{2,2}) \times (B_{2,1} + B_{2,2})$

Luego, las submatrices de la matriz resultante $C$ se calculan como:

- $C_{1,1} = M_1 + M_4 - M_5 + M_7$
- $C_{1,2} = M_3 + M_5$
- $C_{2,1} = M_2 + M_4$
- $C_{2,2} = M_1 - M_2 + M_3 + M_6$

Para obtener el orden de tiempo de ejecución del algoritmo de Strassen, se puede armar la ecuación de recurrencia $t(n)$. En este caso, se realizan 7 multiplicaciones de submatrices (cada una de tamaño $\frac{n}{2} \times \frac{n}{2}$) y varias sumas y restas de matrices (cada una de tamaño $\frac{n}{2} \times \frac{n}{2}$). Por lo tanto: $a = 7$, $b = 2$ y $f(n) = O(n^2)$.

La ecuación de recurrencia queda entonces: $t(n) = 7 \cdot t(\frac{n}{2}) + n^2$.

Usando teorema maestro, se tiene que $a > b^k$ porque $7 > 2^2$. Entonces, el tiempo de ejecución es: $t(n) \in O(n^{log_b(a)}) = O(n^{log_2(7)})$. Calculando $log_2(7) \approx 2.807$, se tiene que el tiempo de ejecución es $O(n^{2.807})$.

### c. Comparar los dos algoritmos de multiplicación de matrices. ¿Los dos son algoritmos D&C? ¿Alguno de los dos es "mejor" que el otro en cuanto a tiempo de ejecución?

Claramente ambos algoritmos son de tipo Divide & Conquer, ya que ambos dividen las matrices en submatrices más pequeñas, las multiplican, y suman los resultados parciales para obtener la matriz resultante.

El algoritmo de Strassen es mejor que el algoritmo D&C tradicional si hablamos estrictamente del tiempo de ejecución, ya que tiene un orden de tiempo de ejecución de $O(n^{2.807})$, que es menor que el orden de tiempo de ejecución del algoritmo D&C tradicional, que es $O(n^3)$. Esto implica que para matrices de gran tamaño, el algoritmo de Strassen será más eficiente y rápido en comparación con el método tradicional. Sin embargo, es importante tener en cuenta que el algoritmo de Strassen puede ser más complejo de implementar y además usa mucha más memoria debido a las múltiples submatrices y operaciones adicionales involucradas.
