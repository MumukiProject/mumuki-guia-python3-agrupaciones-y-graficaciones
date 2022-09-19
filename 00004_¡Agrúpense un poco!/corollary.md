Si elegiste alguna de las otras opciones, ¡tiene sentido! Para poder resolver este problema, vamos a tener que _agrupar_ la tabla de cines por `tipo_de_gestión` y luego calcular la sumatoria de las `pantallas`. Y esto se parece bastante a hacer un value_counts....
 
```
cines.value_counts("tipo_gestion")
```
 
... combinado con una `sum()`:
 
cines.value_counts("tipo_gestion").sum()
 
Pero lamentablemente no estamos obteniendo el resultado esperado, porque estamos obteniendo la **suma total** de **todas** las pantallas, en lugar de tener la suma de pantallas por cada `tipo_gestion`.
 
¿Y cómo hacemos entonces? ¡Acompañános a averiguarlo!
