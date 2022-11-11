¿De qué se tratan entonces las _agrupaciones_? Cuando agrupemos según una columna `A`, estaremos juntando todas las filas que tengan el mismo valor en dicha columna `A`, y luego aplicaremos una _agregación_ sobre todos los valores de una columna `B` que hayan caído en cada grupo.

¿Cómo, cómo...? Bueno, quizás sea más fácil verlo con un ejemplo 😅. Supongamos la siguiente tabla con patentes 🚗 y los montos de sus infracciones de tránsito ⛔:

|patente|infraccion|
|----|---|
|`ab16`|100|
|`xy40`|200|
|`mm12`|150|
|`ab16`|200|
|`xy40`|150|
|`ab16`|200|
|`hz15`|100|

Si quisiéramos saber cuál es el valor total de infracciones de cada patente, deberíamos _agrupar_ según la columna `patente`, colocando juntas todas las filas que tengan la misma patente....


|patente|infraccion||
|----|---|---|
|`ab16`|100|(primer grupo)|
| |200|
| |200|
|`xy40`|200|(segundo grupo)|
| |150|
|`mm12`|150|(tercer grupo)|
|`hz15`|100|(cuarto grupo)|


... y luego, por cada grupo, realizar la sumatoria de la columna `infraccion`:

|patente|infraccion||
|----|---|---|
|`ab16`|500|`(= 100 + 200 + 200)`|
|`xy40`|350|`(= 200 + 150)`|
|`mm12`|150|`(= 150)`|
|`hz15`|100|`(= 100)`|

Con este ejemplo acabamos de ver, paso a paso, qué significa _agrupar según patentes y calcular la sumatoria de infracciones_. Pero cuando agrupemos según una cierta columna, podremos luego usar cualquier otra agregación.

> Si ahora quisiéramos saber el **valor promedio** de las multas que le corresponden a cada patente, ¿qué agrupación deberíamos hacer?
