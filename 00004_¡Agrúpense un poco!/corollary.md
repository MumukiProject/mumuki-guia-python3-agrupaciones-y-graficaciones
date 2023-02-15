Si elegiste alguna de las otras opciones, ¡tiene sentido! Para poder resolver este problema, vamos a tener que _agrupar_ la tabla de cines por `sector` y luego calcular la sumatoria de las `screens`. Y esto se parece bastante a hacer un `value_counts`....
 
```python
ムcines.value_counts("sector")
sector
Privado comercial        243
Público municipal         56
Público provincial         9
Privado independiente      8
Público nacional           8
Privado comunitario        4
Otros                      1
dtype: int64
```
 
...combinado con `sum()`:

```python 
ム cines.value_counts("sector").sum()
329
 ```

Pero lamentablemente no estamos obteniendo el resultado esperado, porque estamos obteniendo la **suma total** de **todas** las pantallas, en lugar de tener la suma de pantallas por cada `sector` :disappointed:.
 
¿Y cómo hacemos entonces? :thinking: ¡Acompañános a averiguarlo!
