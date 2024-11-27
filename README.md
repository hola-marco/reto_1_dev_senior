# reto_1_dev_senior
# 🌟 Gestión de Experimentos 🌟

### 📜 Descripción del Proyecto
El proyecto **Gestión de Experimentos** es una herramienta interactiva desarrollada en **Python** 🐍 que permite a los usuarios gestionar, analizar y visualizar experimentos científicos 🔬.  

Entre sus principales características se encuentran:  
- 📊 Registro de experimentos.  
- ✍️ Agregado y eliminación de resultados.  
- 📈 Generación de análisis estadísticos.  
- 📝 Creación de informes detallados.  

---

### 💻 Descripción del Código

- **`__init__`**: 🛠️ Inicializa los datos del experimento, como:
  - Nombre.
  - Tipo.
  - Fecha.
  - Lista de resultados.
- **`agregar_resultado`**: ➕ Permite agregar resultados numéricos. Si el usuario escribe **`fin`**, el proceso de adición termina.
- **`mostrar_informacion`**: 🖥️ Muestra:
  - Nombre.
  - Tipo.
  - Fecha.
  - Resultados del experimento.
- **`obtener_analisis`**: 📈 Calcula estadísticas de los resultados:
  - Promedio.
  - Máximo.
  - Mínimo (usando la librería `statistics`).

---

### ✨ Funciones del Programa

1. **`agregar_experimento(inventario)`**: 🧪  
   Permite al usuario agregar un nuevo experimento con nombre, tipo, fecha y resultados.  
2. **`visualizarExperimentos(inventario)`**: 👀  
   Muestra una lista de todos los experimentos almacenados, incluyendo sus detalles.  
3. **`calcular_estadisticas(inventario)`**: 📊  
   Realiza cálculos básicos para experimentos con al menos 3 resultados.  
4. **`generar_informe(inventario)`**: 📝  
   Crea un archivo de texto llamado **`informe_investigaciones.txt`** con un resumen de todos los experimentos.  
5. **`eliminarExperimento(inventario)`**: ❌  
   Elimina un experimento del inventario por su nombre.  
6. **`mostrar_menu()`**: 📜  
   Muestra el menú principal con opciones interactivas.  
7. **`subMenu()`**: 🗂️  
   Presenta un submenú para gestionar experimentos.  
8. **`main()`**: 🚀  
   Es el ciclo principal del programa, donde se controla la interacción con el usuario.

---

### 🗂️ Menú Principal

El programa ofrece un menú interactivo que permite al usuario gestionar experimentos.  


