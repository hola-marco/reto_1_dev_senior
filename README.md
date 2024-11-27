# reto_1_dev_senior
# 🧪 **Gestión de Experimentos 💻**

> **Una herramienta interactiva para gestionar, analizar y visualizar experimentos científicos.**  
Mediante este programa puedes agregar resultados, generar informes y realizar análisis estadísticos completos, todo desde un entorno de consola.

---

## 📝 **Descripción del Proyecto**
El proyecto **Gestión de Experimentos** nos permite : 
- **Registrar** experimentos con detalles como nombre, tipo, fecha y resultados.  
- **Analizar** los datos mediante estadísticas como promedio, máximo y mínimo.  
- **Visualizar** los resultados a través de gráficos de líneas o dispersión.  
- **Generar** informes completos en un archivo de texto.  
- **Eliminar** experimentos innecesarios del inventario.  

---

## 🛠️ **Descripción del Código**

---

## ⚙️ **Funciones del Programa**

### 🔹 **Gestión de Experimentos**
1. **`agregarExperimento(inventario)`**: Permite agregar un nuevo experimento con su nombre, tipo, fecha y resultados.  
2. **`visualizarExperimentos(inventario)`**: Muestra la lista completa de experimentos registrados.  
3. **`eliminarExperimento(inventario)`**: Elimina un experimento del inventario por su nombre.  

### 🔹 **Análisis y Visualización de Datos**
1. **`calcular_estadisticas(inventario)`**: Calcula estadísticas básicas (promedio, máximo, mínimo) para experimentos con suficientes datos.  
2. **`generar_informe(inventario)`**: Genera un archivo de texto (`informe_investigaciones.txt`) con un resumen detallado de las investigaciones.  
3. **Visualización Gráfica**: Utiliza gráficos de líneas y dispersión para comparar resultados de experimentos   y asi tener un análisis detallado.  

---
## 🖥️ **  Menú Principal **
![alt text](<Captura de pantalla 2024-11-27 111534.png>)

## 🖥️ **  SubMenú **

El programa incluye un submenú interactivo con opciones fáciles de usar:

```text
1️⃣ Agregar Experimento 🧪  
2️⃣ Mostrar Experimentos 📋  
3️⃣ Eliminar Experimento ❌  
4️⃣ Generar Informe 📝  
5️⃣ Salir 🚪  
## 📚 Librerías utilizadas

A continuación, te presentamos las principales librerías empleadas en este proyecto:

- **📅 `datetime`**: Se encarga de la validación y formato de las fechas de los experimentos. Permite que las fechas se ingresen y muestren de forma adecuada.
  
- **🔢 `numpy`**: Utilizada para realizar manipulaciones numéricas avanzadas y trabajar con el manejo de fechas para los gráficos.

- **⏲️ `time`**: Permite hacer pausas en la ejecución del programa para una mejor interacción con el usuario, dando tiempo entre acciones.

- **🖥️ `sys`**: Generalmente usada para interactuar con el sistema operativo, aunque en este código no se emplea de manera activa. Es útil para la administración del entorno.

- **🧰 `os`**: Se utiliza para ejecutar comandos del sistema operativo, como limpiar la terminal para mantener el entorno limpio y organizado.

- **📊 `matplotlib.pyplot`**: Librería para crear gráficos y visualizaciones que permiten representar de forma visual los resultados de las investigaciones.

- **📈 `statistics`**: Se usa para realizar cálculos estadísticos básicos, como el promedio, máximo y mínimo de los resultados de los experimentos.

---

Estas librerías han sido fundamentales para crear una herramienta interactiva de gestión y análisis de experimentos científicos.


