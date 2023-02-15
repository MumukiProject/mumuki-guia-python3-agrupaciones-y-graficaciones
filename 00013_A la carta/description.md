¡Pero eso no es todo! `agg` permite además usar agregaciones personalizadas, tan solo pasando una función como valor. Por ejemplo, si queremos contar la cantidad de cines que tiene la frase `"Centro cultural"` en su nombre...

||province|name|
|---|---|---|
|0|Buenos Aires|5|
|1|Catamarca|1|
|2|Chaco|0|
|3|Chubut|1|
|4|Ciudad Autónoma de Buenos Aires|3|
|5|Corrientes|0|
|6|Córdoba|2|
|(...)|

...podríamos escribir algo así....
 
```python
cines.groupby("province", as_index=False).agg({
   "name": contar_centros_culturales
})
```
 
... donde en lugar de pasar un string con el nombre de una agregación (como `"sum"` o `"count"`), pasamos la referencia a una función. Estas funciones que `agg` recibe deben tomar una lista con los valores de las filas de cada grupo y en ellas podemos usar todo lo que sabemos sobre recorridos, como variables, repeticiones y alternativas condicionales:

```python
def contar_centros_culturales(nombres):
  cantidad_centros = 0
  for nombre in nombres:
    if "centro cultural" in nombre.lower():
      cantidad_centros += 1
  return cantidad_centros
``` 

De hecho, incluso podemos usar listas por comprensión:

```python
# versión alternativa
def contar_centros_culturales(nombres):
 return len([nombre for nombre in nombres if "centro cultural" in nombre.lower()])
```

Luego, `agg` invocará internamente esta función, pasandolo los valores de la columna agregada de cada grupo para calcular el resultado. Por ejemplo, cuando evalúe a las filas de la provincia `Catamarca`, le pasará todos los nombres de sus cines...


```python
# el código de agg hará aproximadamente esto 
ムcontar_centros_culturales(['Cinemacenter', 'Centro Cultural San Agustín', 'Cinemacenter', 'Cine Teatro Catamarca'])
1
```

... y así sabrá que el valor final de la agregación de `Catamarca` es `1`. Luego repetirá el proceso con cada una de las demás provincias...

```python
# valores de Corrientes
ムcontar_centros_culturales(['Los Cines De La Costa', 'Espacio Incaa Guido Miranda', 'Cinemacenter', 'Cinemacenter'])
0
# valores de Córdoba
ムcontar_centros_culturales(['Sudcinemas', 'Dinosaurio Mall 60 Cuadras',  'Cine Teatro Coop Luz Y Fuerza', ...]
2
# etc...
```

...y de esta forma completará el `DataFrame` resultante. 

> :first_place: ¡Ahora te toca a vos! Construí una tabla `proporcion_cines_comerciales_provinciales` que contenga, para cada provincia, la proporción entre 0 y 1 de cines de gestión `"Privado comercial"`, ordenada según esta proporción de menor a mayor. 