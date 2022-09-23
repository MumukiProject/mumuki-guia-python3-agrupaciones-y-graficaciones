Lamentablemente, no siempre contaremos con información en el preciso formato en el que la necesitamos 🤷. Ya sea para comprenderla mejor en tablas o gráficamente, en general terminaremos tomando un lote de datos que _más o menos_ se ajuste a lo que estamos buscando, y luego lo adaptaremos a nuestras necesidades :person_juggling:.

Por ejemplo, si estamos estudiando la distribución del tipo de gestión (es decir, si es del sector público o privado) de los cines de Argentina  :movie_camera:, probablemente no encontraremos un lote de datos que contenga exactamente esa información, sino más bien algo como éste que ya trabajamos previamente:

```python
cines = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=969960562&single=true&output=csv")
cines.head(5)
```

||(..)|province|department|city|name|(..)|sector|screens|seats|update_year|
|---|---|---|---|---|---|---|---|---|---|---|
|0|(..)|Catamarca|Capital|Catamarca|Cinemacenter|(..)|Privado comercial|5|743|2018|
|1|(..)|Catamarca|Santa Maria|Santa María|Centro Cultural San Agustín|(..)|Privado comercial|1|440|2018|
|2|(..)|Chaco|San Fernando|Resistencia|Los Cines De La Costa|(..)|Privado comercial|5|820|2018|
|3|(..)|Chubut|Sarmiento|Sarmiento|Deborah Jones De Williams|(..)|Público municipal|1|80|2018|
|4|(..)|Corrientes|Bella Vista|Bella Vista|Fantasio|(..)|Privado comercial|1|240|2018|


Pero, ¿cómo sería nuestra tabla ideal? 🤔 Debería tener dos columnas...
 
 * el tipo de gestión (`sector`): una columna categórica (pública provincial, pública municipal, privada comercial,  etc)
 * la cantidad de pantallas de pantallas de cine de cada gestión (`screens`): una columna numérica con cada uno de los totales de pantallas.
 
... y verse aproximadamente así:

||sector|screens|
|---|---|---|
|0|Privado comercial|879|
|1|Público municipal|57|
|2|Público nacional|14|
|3|Público provincial|11|
|4|Privado independiente|8|
|5|Privado comunitario|4|
|6|Otros|1|


> Cargá en tu cuaderno la tabla anterior y observala detenidamente 🔎. ¿Es posible construir esta tabla usando **únicamente** lo que vimos hasta ahora?

