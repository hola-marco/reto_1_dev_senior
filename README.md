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
print(GREEN," "*30,"        +--------------------------+")
        print(GREEN," "*30,"       /|",  azul_rey , "DEV     🐍💻",GREEN,"         /|")
        print(GREEN," "*30,"      / |  ",negro ,"   SENIOR  ",GREEN,"       / |")
        print(GREEN," "*30,"     /  |      ", RESET,"     CODE ",GREEN,"   /  |")
        print(GREEN," "*30,"    +--------------------------+   |")
        print(GREEN," "*30,"    |  |                       |   |")
        print(GREEN," "*30,"    |  |   ██████████████████  |   |")
        print(GREEN," "*30,"    |  |   |",RESET,"MENU PRINCIPAL ",GREEN,"|   |")
        print(GREEN," "*30,"    |  |   |-------------------|   |")
        print(GREEN," "*30,"    |  |🧪 | ",RESET,"1. Gestión de ",GREEN,"|   |")
        print(GREEN," "*30,"    |  |   | ",RESET,"Experimentos ",GREEN," |   |")
        print(GREEN," "*30,"    |  |   |-------------------|   |")
        print(GREEN," "*30,"    |  |🔍 | ",RESET,"2. Análisis de",GREEN,"|   |")
        print(GREEN," "*30,"    |  |   | ",RESET,"Datos        ",GREEN," |   |")
        print(GREEN," "*30,"    |  |   |-------------------|   |")
        print(GREEN," "*30,"    |  |📊 |",RESET,"3.Generación   ",GREEN,"|   |")
        print(GREEN," "*30,"    |  |   | ",RESET,"Informe    ",GREEN,"   |   |")
        print(GREEN," "*30,"    |  |   |-------------------|   |")
        print(GREEN," "*30,"    |  |🔙 |",RESET,"4. Salir    ",GREEN,"   |   |")
        print(GREEN," "*30,"    |  |   +-------------------+   |")
        print(GREEN," "*30,"    |  |                       |   |")
        print(GREEN," "*30,"    |  |                       |   |")
        print(GREEN," "*30,"    |  +-----------------------|   |")
        print(GREEN," "*30,"    +-------------------------+|")

## 🖥️ **  SubMenú **

El programa incluye un menú interactivo con opciones fáciles de usar:

```text
1️⃣ Agregar Experimento 🧪  
2️⃣ Mostrar Experimentos 📋  
3️⃣ Eliminar Experimento ❌  
4️⃣ Generar Informe 📝  
5️⃣ Salir 🚪  



